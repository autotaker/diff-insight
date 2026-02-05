---
date: '2026-02-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:800bcb1...MicrosoftDocs:f5997cf
summary: この差分では、新機能の追加と大規模な更新が行われ、一部がBreaking Changeに分類されています。リソース管理の改善や関連ドキュメントのリンク更新もあり、ユーザビリティが向上しています。新しいガイドが追加され、特に無料および有料プランのリソースクリーンアップガイドが特徴です。一方で、フルテキスト検索ガイドの大規模な再編成により、ユーザーに新しい内容に慣れる必要があり、重要情報の補完も求められます。全体として、これらの更新はAzure
  AI Searchのユーザーにとって、より簡単で安全な作業環境を提供することを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:800bcb1...MicrosoftDocs:f5997cf){target="_blank"}

# Highlights

この差分では、いくつかの新機能の追加と大規模な更新が行われ、一部はBreaking Changeに分類されるため注意が必要です。また、リソース管理の改善と関連ドキュメントのリンク更新により、ユーザビリティの向上も図られています。

## New features
- 新しいガイドを含むファイル`resource-cleanup-free.md`および`resource-cleanup-paid.md`の追加。
- `resource-endpoint.md`により、Azure AI Searchサービスのエンドポイント取得方法が示されています。

## Breaking changes
- `full-text-intro.md`の削除により、フルテキスト検索の基本的な情報が失われました。
- `full-text-csharp.md`を含む多くのクイックスタートガイドにおいて、大規模な構成変更が行われ、合計で数百行の減少と追加が発生しています。

## Other updates
- リソースのクリーンアップガイドのリンク置き換えや、認証に関するドキュメントの調整。
- `search-how-to-integrated-vectorization.md`や`tutorial-adls-gen2-indexer-acls.md`にて、Visual Studio CodeのRESTクライアントに関する説明の改良。

# Insights

この差分によって、強調されるべき点は主にリソースの管理とフルテキスト検索のガイドラインの再構築です。このアップデートは、Azure AI Searchを用いた開発の導線を整理するためのものです。具体的には、ユーザーがリソースを効率的に管理し、不要なリソースに対する無駄なコストを削減できるよう、無料および有料プランそれぞれに対応したリソースクリーンアップガイドが追加されました。

一方で、フルテキスト検索ガイドの大規模な再編成により、ユーザーに分かりやすく、実践的な指導が提供されるよう調整されています。ただし、既存の構成からの大きな変化により、ユーザーは新しいガイドに慣れる必要があります。特に`full-text-intro.md`が削除されたため、そこから得られた重要な情報は別の文書内で補完される必要があります。

また、リソース認証やエンドポイント取得のガイドラインの更新は、認証やアクセス管理において重視されるポイントを網羅し、セキュリティ面の向上と利便性を兼ね備えた内容となっています。

総合的に、これらの更新は、Azure AI Searchのユーザーにより簡単で安全な作業環境を提供することを目的としています。文書の整合性とユーザーエクスペリエンスの向上に向けた意識が強く反映されているといえるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | パイプライン作成手順の更新 | modified | 4 | 4 | 8 | 
| [get-started-portal-agentic-retrieval.md](#item-2bf1dc) | minor update | リソースのクリーンアップ手順の更新 | modified | 1 | 3 | 4 | 
| [agentic-retrieval-csharp.md](#item-f93ed3) | minor update | クイックスタートのクリーンアップ手順の更新 | modified | 1 | 3 | 4 | 
| [agentic-retrieval-java.md](#item-4e2c55) | minor update | クイックスタートのクリーンアップ手順の更新 | modified | 2 | 2 | 4 | 
| [agentic-retrieval-javascript.md](#item-715283) | minor update | クイックスタートのリソースクリーンアップ手順の更新 | modified | 1 | 3 | 4 | 
| [agentic-retrieval-python.md](#item-efee6a) | minor update | クイックスタートのリソースクリーンアップ手順と環境設定の更新 | modified | 4 | 4 | 8 | 
| [agentic-retrieval-rest.md](#item-3df373) | minor update | クイックスタートのリソースクリーンアップ手順の更新 | modified | 1 | 7 | 8 | 
| [agentic-retrieval-typescript.md](#item-e6370b) | minor update | クイックスタートのリソースクリーンアップ手順の更新 | modified | 1 | 3 | 4 | 
| [full-text-csharp.md](#item-2e943a) | breaking change | フルテキスト検索クイックスタートの全面的な更新 | modified | 120 | 598 | 718 | 
| [full-text-intro.md](#item-f655a1) | breaking change | フルテキスト検索のイントロダクションセクションの削除 | removed | 0 | 12 | 12 | 
| [full-text-java.md](#item-d659f9) | breaking change | フルテキスト検索のクイックスタートに関する大規模な更新 | modified | 99 | 548 | 647 | 
| [full-text-javascript.md](#item-568e3a) | breaking change | フルテキスト検索に関するJavaScriptクイックスタートの大幅な更新 | modified | 106 | 522 | 628 | 
| [full-text-powershell.md](#item-1b28d3) | minor update | PowerShellを用いたフルテキスト検索のクイックスタートガイドの改訂 | modified | 151 | 274 | 425 | 
| [full-text-python.md](#item-9bba1c) | minor update | Pythonを使用したフルテキスト検索のクイックスタートガイドの改訂 | modified | 230 | 119 | 349 | 
| [full-text-rest.md](#item-5d3419) | minor update | REST APIを使用したフルテキスト検索のクイックスタートガイドの改訂 | modified | 128 | 180 | 308 | 
| [full-text-typescript.md](#item-6630e8) | minor update | TypeScriptを使用したフルテキスト検索のクイックスタートガイドの改訂 | modified | 192 | 293 | 485 | 
| [search-get-started-portal-new-wizard.md](#item-114e35) | minor update | ポータルウィザードによる検索の開始に関するガイドの文言修正 | modified | 1 | 1 | 2 | 
| [search-get-started-vector-python.md](#item-53085f) | minor update | Pythonでのベクトル検索の開始ガイドの前提条件の更新 | modified | 3 | 1 | 4 | 
| [search-get-started-vector-rest.md](#item-c7d261) | minor update | RESTを使用したベクトル検索のガイド文言修正 | modified | 2 | 2 | 4 | 
| [resource-authentication.md](#item-381ff1) | minor update | リソース認証に関する文書の改善 | modified | 13 | 22 | 35 | 
| [resource-cleanup-free.md](#item-99ba27) | new feature | 無料プラン向けのAzure AI Searchリソースクリーンアップガイドの追加 | added | 16 | 0 | 16 | 
| [resource-cleanup-paid.md](#item-a9aef4) | new feature | 有料プラン向けのAzure AI Searchリソースクリーンアップガイドの追加 | added | 14 | 0 | 14 | 
| [resource-endpoint.md](#item-2b31be) | new feature | Azure AI Searchサービスのエンドポイント取得ガイドの追加 | added | 20 | 0 | 20 | 
| [search-create-app-portal.md](#item-19ab44) | minor update | リソースのクリーンアップセクションの更新 | modified | 1 | 5 | 6 | 
| [search-explorer.md](#item-738774) | minor update | リソースのクリーンアップセクションの更新 | modified | 1 | 5 | 6 | 
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | リソースのクリーンアップセクションのリンク更新 | modified | 1 | 1 | 2 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | リソースのクリーンアップセクションのリンク更新 | modified | 1 | 1 | 2 | 
| [search-get-started-portal.md](#item-6d0cb1) | minor update | リソースのクリーンアップセクションのリンク更新 | modified | 1 | 6 | 7 | 
| [search-get-started-semantic.md](#item-2b3902) | minor update | リソースのクリーンアップセクションのリンク更新 | modified | 1 | 3 | 4 | 
| [search-get-started-skillset.md](#item-079744) | minor update | リソースのクリーンアップセクションのリンク更新 | modified | 1 | 5 | 6 | 
| [search-get-started-text.md](#item-935941) | minor update | 日付の更新およびリソースのクリーンアップリンクの修正 | modified | 2 | 6 | 8 | 
| [search-how-to-integrated-vectorization.md](#item-86fb1e) | minor update | RESTクライアントの拡張機能に関する説明の修正 | modified | 1 | 1 | 2 | 
| [tutorial-adls-gen2-indexer-acls.md](#item-6881a0) | minor update | RESTクライアントの拡張機能に関する説明の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -46,7 +46,9 @@ In this tutorial, you:
 
 + The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-+ [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter package](https://pypi.org/project/jupyter/).
+- The latest version of [Python](https://www.python.org/downloads/).
+
+- [Visual Studio Code](https://code.visualstudio.com/download) with the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions.
 
 ## Understand the solution
 
@@ -532,9 +534,7 @@ response.to_dict()
 
 ### Clean up resources
 
-When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
-
-In the Azure portal, you can manage your Azure AI Search and Microsoft Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
+[!INCLUDE [clean up resources (paid)](includes/resource-cleanup-paid.md)]
 
 You can also run the following code to delete individual objects:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "パイプライン作成手順の更新"
}
```

### Explanation
このコードの差分は、`agentic-retrieval-how-to-create-pipeline.md` ファイルに対する小規模な更新を示しています。主に、必要なツールとリソースのリストが改善されています。具体的には、Azure CLI の使用が強調され、以前の記述から Visual Studio Code に関連する内容が整理され、新たな情報が追加されました。また、リソースのクリーンアップに関する重要な注意事項も、具体的な手順からリンクによる参照に置き換えられています。これにより、情報の精度が向上し、ユーザーが必要なリソースを効率的に管理できるようになります。

## articles/search/get-started-portal-agentic-retrieval.md{#item-2bf1dc}

<details>
<summary>Diff</summary>
````diff
@@ -275,9 +275,7 @@ To review the auto-generated objects:
 
 ## Clean up resources
 
-When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
-
-In the Azure portal, you can manage your Azure AI Search, Azure Blob Storage, and Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
+[!INCLUDE [clean up resources (paid)](includes/resource-cleanup-paid.md)]
 
 You can also delete the knowledge source and knowledge base on their respective portal pages. When you delete the knowledge source, the portal prompts you to delete the associated data source, skillset, index, and indexer.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースのクリーンアップ手順の更新"
}
```

### Explanation
このコードの差分は、`get-started-portal-agentic-retrieval.md` ファイルに対する小規模な修正を示しています。リソースのクリーンアップに関するセクションが修正され、リソース管理に関する具体的な手順が簡略化されました。特に、ユーザーがリソースのクリーンアップを行う際に、注意事項としてポイントされていた内容が、リンクによる参照に変更されました。このリンクは、クリーンアップ作業に関する詳細な情報を提供する `includes/resource-cleanup-paid.md` に向けられており、ユーザーが不必要なリソースを管理する手助けとなります。この変更により、情報が整理され、ユーザビリティが向上しています。

## articles/search/includes/quickstarts/agentic-retrieval-csharp.md{#item-f93ed3}

<details>
<summary>Diff</summary>
````diff
@@ -844,9 +844,7 @@ foreach (var reference in retrievalResult.Value.References)
 
 ## Clean up resources
 
-When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
-
-In the Azure portal, you can manage your Azure AI Search and Microsoft Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
+[!INCLUDE [clean up resources (paid)](../resource-cleanup-paid.md)]
 
 Otherwise, the following code from `Program.cs` deleted the objects you created in this quickstart.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートのクリーンアップ手順の更新"
}
```

### Explanation
このコードの差分は、`agentic-retrieval-csharp.md` ファイルに対する小規模な変更を示しています。具体的には、リソースのクリーンアップに関するセクションが更新され、詳細な手順が簡潔な形式に整理されています。従来の具体的な手順は削除され、代わりにリソースのクリーンアップに関する情報へのリンクが追加されています。このリンクは、クリーンアップの手続きに関する詳細を提供する `../resource-cleanup-paid.md` に向けられています。これにより、ユーザーは不必要なリソースを効率的に管理できるようになり、情報が分かりやすく整理されています。

## articles/search/includes/quickstarts/agentic-retrieval-java.md{#item-4e2c55}

<details>
<summary>Diff</summary>
````diff
@@ -1385,9 +1385,9 @@ messages.add(userMessage);
 
 ## Clean up resources
 
-When working in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money. You can delete resources individually, or you can delete the resource group to delete the entire set of resources.
+[!INCLUDE [clean up resources (paid)](../resource-cleanup-paid.md)]
 
-In the Azure portal, you can find and manage resources by selecting **All resources** or **Resource groups** from the left pane. You can also run the following code to delete the objects you created in this quickstart.
+You can also run the following code to delete the objects you created in this quickstart.
 
 ### Delete the knowledge agent
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートのクリーンアップ手順の更新"
}
```

### Explanation
このコードの差分は、`agentic-retrieval-java.md` ファイルに対する小規模な修正を示しています。リソースのクリーンアップに関する手順が簡略化され、具体的な指示がリンクに置き換えられました。この更新により、リソース管理についての詳細が、`../resource-cleanup-paid.md` のドキュメントに参照される形となりました。また、削除作業を行うためのコードに関する情報が保持され、手順が明確に示されています。これにより、ユーザーはリソースのクリーンアップを効率的に行うことができるようになり、文書全体の構成が改善されています。

## articles/search/includes/quickstarts/agentic-retrieval-javascript.md{#item-715283}

<details>
<summary>Diff</summary>
````diff
@@ -937,9 +937,7 @@ if (result2.references) {
 
 ## Clean up resources
 
-When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
-
-In the [Azure portal](https://portal.azure.com/), you can manage your Azure AI Search and Microsoft Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
+[!INCLUDE [clean up resources (paid)](../resource-cleanup-paid.md)]
 
 Otherwise, the following code from `index.js` deleted the objects you created in this quickstart.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートのリソースクリーンアップ手順の更新"
}
```

### Explanation
このコードの差分は、`agentic-retrieval-javascript.md` ファイルに対する小さな変更を示しています。リソースのクリーンアップに関するセクションが更新され、具体的な手順の説明が削除され、代わりにリソース管理に関するリンクが追加されました。このリンクは、クリーンアップ手続きに関する詳細を提供する `../resource-cleanup-paid.md` への参照です。ユーザーは、利用しているリソースを効率的に管理するための情報を、より簡潔に得ることができるようになりました。また、リソースの削除に関するコードの実行方法についての説明はそのまま維持されています。これにより、文書全体が整理され、使用者が必要な情報を迅速に見つけやすくなっています。

## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,9 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 + The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-+ [Visual Studio Code](https://code.visualstudio.com/download) and the latest version of [Python](https://www.python.org/downloads/).
++ The latest version of [Python](https://www.python.org/downloads/).
+
++ [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
 
 [!INCLUDE [Setup](./agentic-retrieval-setup.md)]
 
@@ -779,9 +781,7 @@ print("references_content:\n", references_content)
 
 ## Clean up resources
 
-When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
-
-In the [Azure portal](https://portal.azure.com/), you can manage your Azure AI Search and Microsoft Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
+[!INCLUDE [clean up resources (paid)](../resource-cleanup-paid.md)]
 
 Otherwise, the following code from `agentic-retrieval.py` deleted the objects you created in this quickstart.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートのリソースクリーンアップ手順と環境設定の更新"
}
```

### Explanation
このコードの差分は、`agentic-retrieval-python.md` ファイルに対する軽微な変更を示しています。主に、環境設定に関連する情報が更新され、Microsoft Entra ID を使用したキーレス認証についての新しい情報が追加されました。また、必要なソフトウェアのインストール手順も改善され、Visual Studio Code と Python の最新バージョンのリンクが明確化されました。さらに、リソースのクリーンアップに関するセクションが、より簡潔に `[!INCLUDE [clean up resources (paid)](../resource-cleanup-paid.md)]` のリンクに置き換えられています。この変更により、ユーザーはリソース管理に必要な情報をより効率的に得ることができ、文書全体の整理が図られています。追加された情報と、リンク形式による簡略化が、ユーザーの体験を向上させています。

## articles/search/includes/quickstarts/agentic-retrieval-rest.md{#item-3df373}

<details>
<summary>Diff</summary>
````diff
@@ -627,16 +627,10 @@ The output should contain the following components:
 
 ## Clean up resources
 
-When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
-
-In the [Azure portal](https://portal.azure.com/), you can manage your Azure AI Search and Microsoft Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
+[!INCLUDE [clean up resources (paid)](../resource-cleanup-paid.md)]
 
 Otherwise, the following requests from `agentic-retrieval.rest` deleted the objects you created in this quickstart.
 
-<!-- You can delete resources individually or delete the entire resource group.
-
-In the Azure portal, you can find and manage resources by selecting **All resources** or **Resource groups** from the left pane. -->
-
 ### Delete the knowledge base
 
 ```HTTP
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートのリソースクリーンアップ手順の更新"
}
```

### Explanation
このコードの差分は、`agentic-retrieval-rest.md` ファイルに対する軽微な修正を表しています。リソースのクリーンアップに関するセクションが変更され、詳細な手順の説明が削除され、代わりに `[!INCLUDE [clean up resources (paid)](../resource-cleanup-paid.md)]` という新しい参照が追加されました。この変更により、ユーザーはリソース管理に関する情報をより簡単にアクセスできるようになり、冗長な説明を省くことで文書がクリーンになりました。また、リソースを削除するためのリクエストに関する部分はそのまま残されており、具体的なコードの実行方法が依然として提供されています。この更新により、文書全体の可読性が向上し、必要な情報へのアクセスが改善されています。

## articles/search/includes/quickstarts/agentic-retrieval-typescript.md{#item-e6370b}

<details>
<summary>Diff</summary>
````diff
@@ -998,9 +998,7 @@ console.log("\n✅ Quickstart completed successfully!");
 
 ## Clean up resources
 
-When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
-
-In the [Azure portal](https://portal.azure.com/), you can manage your Azure AI Search and Microsoft Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
+[!INCLUDE [clean up resources (paid)](../resource-cleanup-paid.md)]
 
 Otherwise, the following code from `index.ts` deleted the objects you created in this quickstart.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートのリソースクリーンアップ手順の更新"
}
```

### Explanation
このコードの差分は、`agentic-retrieval-typescript.md` ファイルにおける軽微な変更を示しています。リソースのクリーンアップに関するセクションが簡略化され、詳細な説明が削除されて新たに `[!INCLUDE [clean up resources (paid)](../resource-cleanup-paid.md)]` というリンクが追加されました。この変更により、ユーザーはより具体的なリソース管理手順に容易にアクセスできるようになります。一方で、クイックスタートで作成したオブジェクトを削除するためのコードセクションはそのまま残されており、ユーザーが必要な情報を保持したまま、文書がより明瞭で簡潔になっています。全体として、情報の整理と可読性の向上が図られ、ユーザーエクスペリエンスが改善されています。

## articles/search/includes/quickstarts/full-text-csharp.md{#item-2e943a}

<details>
<summary>Diff</summary>
````diff
@@ -4,669 +4,193 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 02/02/2026
 ---
 
-[!INCLUDE [Full text introduction](full-text-intro.md)]
+In this quickstart, you use the [Azure AI Search client library for .NET](/dotnet/api/overview/azure/search) to create, load, and query a search index for [full-text search](../../search-lucene-query-architecture.md), also known as keyword search.
+
+Full-text search uses Apache Lucene for indexing and queries and the BM25 ranking algorithm for scoring results. This quickstart uses fictional hotel data from the [azure-search-sample-data](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/hotels/hotel-json-documents) GitHub repository to populate the index.
 
 > [!TIP]
-> You can download the [source code](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-keyword-search) to start with a finished project or follow these steps to create your own.
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-keyword-search) on GitHub.
 
 ## Prerequisites
 
 - An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. For this quickstart, you can use a free service.
+- An [Azure AI Search service](../../search-create-service-portal.md). You can use a free service for this quickstart.
 
-## Microsoft Entra ID prerequisites
+- The latest version of the [.NET SDK](https://dotnet.microsoft.com/download).
 
-For the recommended keyless authentication with Microsoft Entra ID, you must:
+- [Visual Studio Code](https://code.visualstudio.com/download).
 
-- Install the [Azure CLI](/cli/azure/install-azure-cli).
+- [Git](https://git-scm.com/downloads) to clone the sample repository.
 
-- Assign the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
+- The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-## Get service information
+## Configure access
 
 [!INCLUDE [resource authentication](../resource-authentication.md)]
 
-## Set up
+## Get endpoint
 
-1. Create a new folder `full-text-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
+[!INCLUDE [resource endpoint](../resource-endpoint.md)]
 
-    ```shell
-    mkdir full-text-quickstart && cd full-text-quickstart
-    ```
+## Set up the environment
 
-1. Create a new console application with the following command:
+1. Use Git to clone the sample repository.
 
-    ```shell
-    dotnet new console
-    ```
+   ```console
+   git clone https://github.com/Azure-Samples/azure-search-dotnet-samples
+   ```
 
-1. Install the Azure AI Search client library ([Azure.Search.Documents](/dotnet/api/overview/azure/search.documents-readme)) for .NET with:
+1. Open the `azure-search-dotnet-samples/quickstart-keyword-search/AzureSearchQuickstart` folder in Visual Studio Code.
 
-    ```console
-    dotnet add package Azure.Search.Documents
-    ```
+1. Open the `Program.cs` file.
 
-1. For the **recommended** keyless authentication with Microsoft Entra ID, install the [Azure.Identity](https://www.nuget.org/packages/Azure.Identity) package with:
+1. Replace the placeholder value for `serviceEndpoint` with the URL you obtained in [Get endpoint](#get-endpoint).
 
-    ```console
-    dotnet add package Azure.Identity
-    ```
+1. Install the dependencies from the `AzureSearchQuickstart.csproj` file.
+
+   ```console
+   dotnet restore
+   ```
 
-1. For the **recommended** keyless authentication with Microsoft Entra ID, sign in to Azure with the following command:
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service.
 
-    ```console
+    ```azurecli
     az login
     ```
 
-## Create, load, and query a search index
+## Run the code
 
-In the prior [set up](#set-up) section, you created a new console application and installed the Azure AI Search client library. 
+Build and run the application.
 
-In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [Explaining the code](#explaining-the-code) section.
+```console
+dotnet run
+```
 
-The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
+### Output
 
-#### [Microsoft Entra ID](#tab/keyless)
+The output should be similar to the following:
 
-```csharp
-Uri serviceEndpoint = new Uri($"https://<Put your search service NAME here>.search.windows.net/");
-DefaultAzureCredential credential = new();
 ```
+Deleting index...
 
-#### [API key](#tab/api-key)
+Creating index...
 
-```csharp
-Uri serviceEndpoint = new Uri($"https://<Put your search service NAME here>.search.windows.net/");
-AzureKeyCredential credential = new AzureKeyCredential("<Your search service admin key>");
-```
----
+Uploading documents...
 
-1. In *Program.cs*, paste the following code. Edit the `serviceName` and `apiKey` variables with your search service name and admin API key.
+Waiting for indexing...
 
-    ```csharp
-    using System;
-    using Azure;
-    using Azure.Identity;
-    using Azure.Search.Documents;
-    using Azure.Search.Documents.Indexes;
-    using Azure.Search.Documents.Indexes.Models;
-    using Azure.Search.Documents.Models;
-    
-    namespace AzureSearch.Quickstart
-    
-    {
-        class Program
-        {
-            static void Main(string[] args)
-            {    
-                // Your search service endpoint
-                Uri serviceEndpoint = new Uri($"https://<Put your search service NAME here>.search.windows.net/");
-    
-                // Use the recommended keyless credential instead of the AzureKeyCredential credential.
-                DefaultAzureCredential credential = new();
-                //AzureKeyCredential credential = new AzureKeyCredential("Your search service admin key");
-    
-                // Create a SearchIndexClient to send create/delete index commands
-                SearchIndexClient searchIndexClient = new SearchIndexClient(serviceEndpoint, credential);
-    
-                // Create a SearchClient to load and query documents
-                string indexName = "hotels-quickstart";
-                SearchClient searchClient = new SearchClient(serviceEndpoint, indexName, credential);
-    
-                // Delete index if it exists
-                Console.WriteLine("{0}", "Deleting index...\n");
-                DeleteIndexIfExists(indexName, searchIndexClient);
-    
-                // Create index
-                Console.WriteLine("{0}", "Creating index...\n");
-                CreateIndex(indexName, searchIndexClient);
-    
-                SearchClient ingesterClient = searchIndexClient.GetSearchClient(indexName);
-    
-                // Load documents
-                Console.WriteLine("{0}", "Uploading documents...\n");
-                UploadDocuments(ingesterClient);
-    
-                // Wait 2 secondsfor indexing to complete before starting queries (for demo and console-app purposes only)
-                Console.WriteLine("Waiting for indexing...\n");
-                System.Threading.Thread.Sleep(2000);
-    
-                // Call the RunQueries method to invoke a series of queries
-                Console.WriteLine("Starting queries...\n");
-                RunQueries(searchClient);
-    
-                // End the program
-                Console.WriteLine("{0}", "Complete. Press any key to end this program...\n");
-                Console.ReadKey();
-            }
-    
-            // Delete the hotels-quickstart index to reuse its name
-            private static void DeleteIndexIfExists(string indexName, SearchIndexClient searchIndexClient)
-            {
-                searchIndexClient.GetIndexNames();
-                {
-                    searchIndexClient.DeleteIndex(indexName);
-                }
-            }
-            // Create hotels-quickstart index
-            private static void CreateIndex(string indexName, SearchIndexClient searchIndexClient)
-            {
-                FieldBuilder fieldBuilder = new FieldBuilder();
-                var searchFields = fieldBuilder.Build(typeof(Hotel));
-    
-                var definition = new SearchIndex(indexName, searchFields);
-    
-                var suggester = new SearchSuggester("sg", new[] { "HotelName", "Category", "Address/City", "Address/StateProvince" });
-                definition.Suggesters.Add(suggester);
-    
-                searchIndexClient.CreateOrUpdateIndex(definition);
-            }
-    
-            // Upload documents in a single Upload request.
-            private static void UploadDocuments(SearchClient searchClient)
-            {
-                IndexDocumentsBatch<Hotel> batch = IndexDocumentsBatch.Create(
-                    IndexDocumentsAction.Upload(
-                        new Hotel()
-                        {
-                            HotelId = "1",
-                            HotelName = "Stay-Kay City Hotel",
-                            Description = "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
-                            Category = "Boutique",
-                            Tags = new[] { "view", "air conditioning", "concierge" },
-                            ParkingIncluded = false,
-                            LastRenovationDate = new DateTimeOffset(2022, 1, 18, 0, 0, 0, TimeSpan.Zero),
-                            Rating = 3.6,
-                            Address = new Address()
-                            {
-                                StreetAddress = "677 5th Ave",
-                                City = "New York",
-                                StateProvince = "NY",
-                                PostalCode = "10022",
-                                Country = "USA"
-                            }
-                        }),
-                    IndexDocumentsAction.Upload(
-                        new Hotel()
-                        {
-                            HotelId = "2",
-                            HotelName = "Old Century Hotel",
-                            Description = "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
-                            Category = "Boutique",
-                            Tags = new[] { "pool", "free wifi", "concierge" },
-                            ParkingIncluded = false,
-                            LastRenovationDate = new DateTimeOffset(2019, 2, 18, 0, 0, 0, TimeSpan.Zero),
-                            Rating = 3.60,
-                            Address = new Address()
-                            {
-                                StreetAddress = "140 University Town Center Dr",
-                                City = "Sarasota",
-                                StateProvince = "FL",
-                                PostalCode = "34243",
-                                Country = "USA"
-                            }
-                        }),
-                    IndexDocumentsAction.Upload(
-                        new Hotel()
-                        {
-                            HotelId = "3",
-                            HotelName = "Gastronomic Landscape Hotel",
-                            Description = "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
-                            Category = "Suite",
-                            Tags = new[] { "restaurant", "bar", "continental breakfast" },
-                            ParkingIncluded = true,
-                            LastRenovationDate = new DateTimeOffset(2015, 9, 20, 0, 0, 0, TimeSpan.Zero),
-                            Rating = 4.80,
-                            Address = new Address()
-                            {
-                                StreetAddress = "3393 Peachtree Rd",
-                                City = "Atlanta",
-                                StateProvince = "GA",
-                                PostalCode = "30326",
-                                Country = "USA"
-                            }
-                        }),
-                    IndexDocumentsAction.Upload(
-                        new Hotel()
-                        {
-                            HotelId = "4",
-                            HotelName = "Sublime Palace Hotel",
-                            Description = "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.",
-                            Category = "Boutique",
-                            Tags = new[] { "concierge", "view", "air conditioning" },
-                            ParkingIncluded = true,
-                            LastRenovationDate = new DateTimeOffset(2020, 2, 06, 0, 0, 0, TimeSpan.Zero),
-                            Rating = 4.60,
-                            Address = new Address()
-                            {
-                                StreetAddress = "7400 San Pedro Ave",
-                                City = "San Antonio",
-                                StateProvince = "TX",
-                                PostalCode = "78216",
-                                Country = "USA"
-                            }
-                        })
-                    );
-    
-                try
-                {
-                    IndexDocumentsResult result = searchClient.IndexDocuments(batch);
-                }
-                catch (Exception)
-                {
-                    // If for some reason any documents are dropped during indexing, you can compensate by delaying and
-                    // retrying. This simple demo just logs the failed document keys and continues.
-                    Console.WriteLine("Failed to index some of the documents: {0}");
-                }
-            }
-    
-            // Run queries, use WriteDocuments to print output
-            private static void RunQueries(SearchClient searchClient)
-            {
-                SearchOptions options;
-                SearchResults<Hotel> response;
-    
-                // Query 1
-                Console.WriteLine("Query #1: Search on empty term '*' to return all documents, showing a subset of fields...\n");
-    
-                options = new SearchOptions()
-                {
-                    IncludeTotalCount = true,
-                    Filter = "",
-                    OrderBy = { "" }
-                };
-    
-                options.Select.Add("HotelId");
-                options.Select.Add("HotelName");
-                options.Select.Add("Rating");
-    
-                response = searchClient.Search<Hotel>("*", options);
-                WriteDocuments(response);
-    
-                // Query 2
-                Console.WriteLine("Query #2: Search on 'hotels', filter on 'Rating gt 4', sort by Rating in descending order...\n");
-    
-                options = new SearchOptions()
-                {
-                    Filter = "Rating gt 4",
-                    OrderBy = { "Rating desc" }
-                };
-    
-                options.Select.Add("HotelId");
-                options.Select.Add("HotelName");
-                options.Select.Add("Rating");
-    
-                response = searchClient.Search<Hotel>("hotels", options);
-                WriteDocuments(response);
-    
-                // Query 3
-                Console.WriteLine("Query #3: Limit search to specific fields (pool in Tags field)...\n");
-    
-                options = new SearchOptions()
-                {
-                    SearchFields = { "Tags" }
-                };
-    
-                options.Select.Add("HotelId");
-                options.Select.Add("HotelName");
-                options.Select.Add("Tags");
-    
-                response = searchClient.Search<Hotel>("pool", options);
-                WriteDocuments(response);
-    
-                // Query 4 - Use Facets to return a faceted navigation structure for a given query
-                // Filters are typically used with facets to narrow results on OnClick events
-                Console.WriteLine("Query #4: Facet on 'Category'...\n");
-    
-                options = new SearchOptions()
-                {
-                    Filter = ""
-                };
-    
-                options.Facets.Add("Category");
-    
-                options.Select.Add("HotelId");
-                options.Select.Add("HotelName");
-                options.Select.Add("Category");
-    
-                response = searchClient.Search<Hotel>("*", options);
-                WriteDocuments(response);
-    
-                // Query 5
-                Console.WriteLine("Query #5: Look up a specific document...\n");
-    
-                Response<Hotel> lookupResponse;
-                lookupResponse = searchClient.GetDocument<Hotel>("3");
-    
-                Console.WriteLine(lookupResponse.Value.HotelId);
-    
-    
-                // Query 6
-                Console.WriteLine("Query #6: Call Autocomplete on HotelName...\n");
-    
-                var autoresponse = searchClient.Autocomplete("sa", "sg");
-                WriteDocuments(autoresponse);
-    
-            }
-    
-            // Write search results to console
-            private static void WriteDocuments(SearchResults<Hotel> searchResults)
-            {
-                foreach (SearchResult<Hotel> result in searchResults.GetResults())
-                {
-                    Console.WriteLine(result.Document);
-                }
-    
-                Console.WriteLine();
-            }
-    
-            private static void WriteDocuments(AutocompleteResults autoResults)
-            {
-                foreach (AutocompleteItem result in autoResults.Results)
-                {
-                    Console.WriteLine(result.Text);
-                }
-    
-                Console.WriteLine();
-            }
-        }
-    }
-    ```
+Starting queries...
 
-1. In the same folder, create a new file named *Hotel.cs* and paste the following code. This code defines the structure of a hotel document. 
+Query #1: Search on empty term '*' to return all documents, showing a subset of fields...
 
-    ```csharp
-    using System;
-    using System.Text.Json.Serialization;
-    using Azure.Search.Documents.Indexes;
-    using Azure.Search.Documents.Indexes.Models;
-    
-    namespace AzureSearch.Quickstart
-    {
-        public partial class Hotel
-        {
-            [SimpleField(IsKey = true, IsFilterable = true)]
-            public string HotelId { get; set; }
-    
-            [SearchableField(IsSortable = true)]
-            public string HotelName { get; set; }
-    
-            [SearchableField(AnalyzerName = LexicalAnalyzerName.Values.EnLucene)]
-            public string Description { get; set; }
-    
-            [SearchableField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
-            public string Category { get; set; }
-    
-            [SearchableField(IsFilterable = true, IsFacetable = true)]
-            public string[] Tags { get; set; }
-    
-            [SimpleField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
-            public bool? ParkingIncluded { get; set; }
-    
-            [SimpleField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
-            public DateTimeOffset? LastRenovationDate { get; set; }
-    
-            [SimpleField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
-            public double? Rating { get; set; }
-    
-            [SearchableField]
-            public Address Address { get; set; }
-        }
-    }
-    ```
+HotelId: 3
+Name: Gastronomic Landscape Hotel
+Rating: 4.8
 
-1. Create a new file named *Hotel.cs* and paste the following code to define the structure of a hotel document. Attributes on the field determine how it's used in an application. For example, the `IsFilterable` attribute must be assigned to every field that supports a filter expression.
+HotelId: 2
+Name: Old Century Hotel
+Rating: 3.6
 
-    ```csharp
-    using System;
-    using System.Text.Json.Serialization;
-    using Azure.Search.Documents.Indexes;
-    using Azure.Search.Documents.Indexes.Models;
-    
-    namespace AzureSearch.Quickstart
-    {
-        public partial class Hotel
-        {
-            [SimpleField(IsKey = true, IsFilterable = true)]
-            public string HotelId { get; set; }
-    
-            [SearchableField(IsSortable = true)]
-            public string HotelName { get; set; }
-    
-            [SearchableField(AnalyzerName = LexicalAnalyzerName.Values.EnLucene)]
-            public string Description { get; set; }
-    
-            [SearchableField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
-            public string Category { get; set; }
-    
-            [SearchableField(IsFilterable = true, IsFacetable = true)]
-            public string[] Tags { get; set; }
-    
-            [SimpleField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
-            public bool? ParkingIncluded { get; set; }
-    
-            [SimpleField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
-            public DateTimeOffset? LastRenovationDate { get; set; }
-    
-            [SimpleField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
-            public double? Rating { get; set; }
-    
-            [SearchableField]
-            public Address Address { get; set; }
-        }
-    }
-    ```
+HotelId: 4
+Name: Sublime Palace Hotel
+Rating: 4.6
 
-1. Create a new file named *Address.cs* and paste the following code to define the structure of an address document.
+HotelId: 1
+Name: Stay-Kay City Hotel
+Rating: 3.6
 
-    ```csharp
-    using Azure.Search.Documents.Indexes;
-    
-    namespace AzureSearch.Quickstart
-    {
-        public partial class Address
-        {
-            [SearchableField(IsFilterable = true)]
-            public string StreetAddress { get; set; }
-    
-            [SearchableField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
-            public string City { get; set; }
-    
-            [SearchableField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
-            public string StateProvince { get; set; }
-    
-            [SearchableField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
-            public string PostalCode { get; set; }
-    
-            [SearchableField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
-            public string Country { get; set; }
-        }
-    }
-    ```
 
-1. Create a new file named *Hotel.Methods.cs* and paste the following code to define a `ToString()` override for the `Hotel` class. 
+Query #2: Search on 'hotels', filter on 'Rating gt 4', sort by Rating in descending order...
 
-    ```csharp
-    using System;
-    using System.Text;
-    
-    namespace AzureSearch.Quickstart
-    {
-        public partial class Hotel
-        {
-            public override string ToString()
-            {
-                var builder = new StringBuilder();
-    
-                if (!String.IsNullOrEmpty(HotelId))
-                {
-                    builder.AppendFormat("HotelId: {0}\n", HotelId);
-                }
-    
-                if (!String.IsNullOrEmpty(HotelName))
-                {
-                    builder.AppendFormat("Name: {0}\n", HotelName);
-                }
-    
-                if (!String.IsNullOrEmpty(Description))
-                {
-                    builder.AppendFormat("Description: {0}\n", Description);
-                }
-    
-                if (!String.IsNullOrEmpty(Category))
-                {
-                    builder.AppendFormat("Category: {0}\n", Category);
-                }
-    
-                if (Tags != null && Tags.Length > 0)
-                {
-                    builder.AppendFormat("Tags: [ {0} ]\n", String.Join(", ", Tags));
-                }
-    
-                if (ParkingIncluded.HasValue)
-                {
-                    builder.AppendFormat("Parking included: {0}\n", ParkingIncluded.Value ? "yes" : "no");
-                }
-    
-                if (LastRenovationDate.HasValue)
-                {
-                    builder.AppendFormat("Last renovated on: {0}\n", LastRenovationDate);
-                }
-    
-                if (Rating.HasValue)
-                {
-                    builder.AppendFormat("Rating: {0}\n", Rating);
-                }
-    
-                if (Address != null && !Address.IsEmpty)
-                {
-                    builder.AppendFormat("Address: \n{0}\n", Address.ToString());
-                }
-    
-                return builder.ToString();
-            }
-        }
-    }
-    ```
+HotelId: 3
+Name: Gastronomic Landscape Hotel
+Rating: 4.8
 
-1. Create a new file named *Address.Methods.cs* and paste the following code to define a `ToString()` override for the `Address` class.
+HotelId: 4
+Name: Sublime Palace Hotel
+Rating: 4.6
 
-    ```csharp
-    using System;
-    using System.Text;
-    using System.Text.Json.Serialization;
-    
-    namespace AzureSearch.Quickstart
-    {
-        public partial class Address
-        {
-            public override string ToString()
-            {
-                var builder = new StringBuilder();
-    
-                if (!IsEmpty)
-                {
-                    builder.AppendFormat("{0}\n{1}, {2} {3}\n{4}", StreetAddress, City, StateProvince, PostalCode, Country);
-                }
-    
-                return builder.ToString();
-            }
-    
-            [JsonIgnore]
-            public bool IsEmpty => String.IsNullOrEmpty(StreetAddress) &&
-                                   String.IsNullOrEmpty(City) &&
-                                   String.IsNullOrEmpty(StateProvince) &&
-                                   String.IsNullOrEmpty(PostalCode) &&
-                                   String.IsNullOrEmpty(Country);
-        }
-    }
-    ```
 
-1. Build and run the application with the following command:
+Query #3: Limit search to specific fields (pool in Tags field)...
 
-    ```shell
-    dotnet run
-    ```
+HotelId: 2
+Name: Old Century Hotel
+Tags: [ pool, free wifi, concierge ]
 
-Output includes messages from [Console.WriteLine](/dotnet/api/system.console.writeline), with the addition of query information and results.
 
-## Explaining the code
+Query #4: Facet on 'Category'...
 
-In the previous sections, you created a new console application and installed the Azure AI Search client library. You added code to create a search index, load it with documents, and run queries. You ran the program to see the results in the console. 
+HotelId: 3
+Name: Gastronomic Landscape Hotel
+Category: Suite
 
-In this section, we explain the code you added to the console application.
+HotelId: 2
+Name: Old Century Hotel
+Category: Boutique
 
-### Create a search client
+HotelId: 4
+Name: Sublime Palace Hotel
+Category: Boutique
 
-In *Program.cs*, you created two clients:
-- [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient) creates the index.
-- [SearchClient](/dotnet/api/azure.search.documents.searchclient) loads and queries an existing index. 
+HotelId: 1
+Name: Stay-Kay City Hotel
+Category: Boutique
 
-Both clients need the search service endpoint and credentials described previously in the [Get service information](#get-service-information) section.
 
-The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
+Query #5: Look up a specific document...
 
-#### [Microsoft Entra ID](#tab/keyless)
+3
+Query #6: Call Autocomplete on HotelName...
 
-```csharp
-Uri serviceEndpoint = new Uri($"https://<Put your search service NAME here>.search.windows.net/");
-DefaultAzureCredential credential = new();
+san
+sarasota
+
+Complete. Press any key to end this program...
 ```
 
-#### [API key](#tab/api-key)
+## Understand the code
 
-```csharp
-Uri serviceEndpoint = new Uri($"https://<Put your search service NAME here>.search.windows.net/");
-AzureKeyCredential credential = new AzureKeyCredential("<Your search service admin key>");
-```
----
+Now that you've run the code, let's break down the key steps:
 
-```csharp
-static void Main(string[] args)
-{
-    // Your search service endpoint
-    Uri serviceEndpoint = new Uri($"https://<Put your search service NAME here>.search.windows.net/");
+1. [Create a search client](#create-a-search-client)
+1. [Create a search index](#create-a-search-index)
+1. [Upload documents to the index](#upload-documents-to-the-index)
+1. [Query the index](#query-the-index)
 
-    // Use the recommended keyless credential instead of the AzureKeyCredential credential.
-    DefaultAzureCredential credential = new();
-    //AzureKeyCredential credential = new AzureKeyCredential("Your search service admin key");
+### Create a search client
 
-    // Create a SearchIndexClient to send create/delete index commands
-    SearchIndexClient searchIndexClient = new SearchIndexClient(serviceEndpoint, credential);
+In `Program.cs`, you create two clients:
 
-    // Create a SearchClient to load and query documents
-    string indexName = "hotels-quickstart";
-    SearchClient searchClient = new SearchClient(serviceEndpoint, indexName, credential);
-    
-    // REDACTED FOR BREVITY . . . 
-}
-```
+- [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient) creates the index.
+- [SearchClient](/dotnet/api/azure.search.documents.searchclient) loads and queries an existing index.
 
-### Create an index
+Both clients require the service endpoint and a credential for authentication. In this quickstart, you use [DefaultAzureCredential](/dotnet/api/azure.identity.defaultazurecredential) for keyless authentication with Microsoft Entra ID.
 
-This quickstart builds a Hotels index that you load with hotel data and execute queries against. In this step, you define the fields in the index. Each field definition includes a name, data type, and attributes that determine how the field is used.
+### Create a search index
 
-In this example, synchronous methods of the *Azure.Search.Documents* library are used for simplicity and readability. However, for production scenarios, you should use asynchronous methods to keep your app scalable and responsive. For example, you would use [CreateIndexAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindexasync) instead of [CreateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindex).
+This quickstart builds a hotels index that you load with hotel data and execute queries against. In this step, you define the fields in the index. Each field definition includes a name, data type, and attributes that determine how the field is used.
+
+This example uses synchronous methods of the [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient) class for simplicity and readability. However, for production scenarios, use asynchronous methods to keep your app scalable and responsive. For example, use [CreateIndexAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindexasync) instead of [CreateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindex).
 
 #### Define the structures
 
-You created two helper classes, *Hotel.cs* and *Address.cs*, to define the structure of a hotel document and its address. The `Hotel` class includes fields for a hotel ID, name, description, category, tags, parking, renovation date, rating, and address. The `Address` class includes fields for street address, city, state/province, postal code, and country/region.
+You create two helper classes, `Hotel.cs` and `Address.cs`, to define the structure of a hotel document and its address. The `Hotel` class includes fields for a hotel ID, name, description, category, tags, parking, renovation date, rating, and address. The `Address` class includes fields for street address, city, state/province, postal code, and country/region.
 
-In the *Azure.Search.Documents* client library, you can use [SearchableField](/dotnet/api/azure.search.documents.indexes.models.searchablefield) and [SimpleField](/dotnet/api/azure.search.documents.indexes.models.simplefield) to streamline field definitions. Both are derivatives of a [SearchField](/dotnet/api/azure.search.documents.indexes.models.searchfield) and can potentially simplify your code:
+In the Azure.Search.Documents client library, you can use [SearchableField](/dotnet/api/azure.search.documents.indexes.models.searchablefield) and [SimpleField](/dotnet/api/azure.search.documents.indexes.models.simplefield) to streamline field definitions. Both are helper classes that generate a [SearchField](/dotnet/api/azure.search.documents.indexes.models.searchfield) and can potentially simplify your code:
 
-+ `SimpleField` can be any data type, is always non-searchable (ignored for full text search queries), and is retrievable (not hidden). Other attributes are off by default, but can be enabled. You might use a `SimpleField` for document IDs or fields used only in filters, facets, or scoring profiles. If so, be sure to apply any attributes that are necessary for the scenario, such as `IsKey = true` for a document ID. For more information, see [SimpleFieldAttribute.cs](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/src/Indexes/SimpleFieldAttribute.cs) in source code.
++ `SimpleField` can be any data type, is always nonsearchable (ignored for full-text search queries), and is retrievable (not hidden). Other attributes are off by default, but can be enabled. You might use a `SimpleField` for document IDs or fields used only in filters, facets, or scoring profiles. If so, apply any attributes that are necessary for the scenario, such as `IsKey = true` for a document ID.
 
-+ `SearchableField` must be a string, and is always searchable and retrievable. Other attributes are off by default, but can be enabled. Because this field type is searchable, it supports synonyms and the full complement of analyzer properties. For more information, see the [SearchableFieldAttribute.cs](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/src/Indexes/SearchableFieldAttribute.cs) in source code.
++ `SearchableField` must be a string, and is always searchable and retrievable. Other attributes are off by default, but can be enabled. Because this field type is searchable, it supports synonyms and the full complement of analyzer properties.
 
 Whether you use the basic `SearchField` API or either one of the helper models, you must explicitly enable filter, facet, and sort attributes. For example, [IsFilterable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfilterable), [IsSortable](/dotnet/api/azure.search.documents.indexes.models.searchfield.issortable), and [IsFacetable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfacetable) must be explicitly attributed, as shown in the previous sample.
 
 #### Create the search index
 
-In *Program.cs*, you create a [SearchIndex](/dotnet/api/azure.search.documents.indexes.models.searchindex) object, and then call the [CreateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindex) method to express the index in your search service. The index also includes a [SearchSuggester](/dotnet/api/azure.search.documents.indexes.models.searchsuggester) to enable autocomplete on the specified fields.
+In `Program.cs`, you create a [SearchIndex](/dotnet/api/azure.search.documents.indexes.models.searchindex) object, and then call the [CreateOrUpdateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createorupdateindex) method to express the index in your search service. The index also includes a [SearchSuggester](/dotnet/api/azure.search.documents.indexes.models.searchsuggester) to enable autocomplete on the specified fields.
 
 ```csharp
 // Create hotels-quickstart index
@@ -684,15 +208,15 @@ private static void CreateIndex(string indexName, SearchIndexClient searchIndexC
 }
 ```
 
-### Load documents
+### Upload documents to the index
 
 Azure AI Search searches over content stored in the service. In this step, you load JSON documents that conform to the hotel index you created.
 
-In Azure AI Search, search documents are data structures that are both inputs to indexing and outputs from queries. As obtained from an external data source, document inputs might be rows in a database, blobs in Blob storage, or JSON documents on disk. In this example, we're taking a shortcut and embedding JSON documents for four hotels in the code itself.
+In Azure AI Search, search documents are data structures that are both inputs to indexing and outputs from queries. As obtained from an external data source, document inputs might be rows in a database, blobs in Azure Blob Storage, or JSON documents on disk. In this example, you take a shortcut and embed JSON documents for four hotels directly.
 
 When uploading documents, you must use an [IndexDocumentsBatch](/dotnet/api/azure.search.documents.models.indexdocumentsbatch-1) object. An `IndexDocumentsBatch` object contains a collection of [Actions](/dotnet/api/azure.search.documents.models.indexdocumentsbatch-1.actions), each of which contains a document and a property telling Azure AI Search what action to perform ([upload, merge, delete, and mergeOrUpload](/azure/search/search-what-is-data-import#indexing-actions)).
 
-In *Program.cs*, you create an array of documents and index actions, and then pass the array to `IndexDocumentsBatch`. The following documents conform to the hotels-quickstart index, as defined by the hotel class.
+In `Program.cs`, you create an array of documents and index actions, and then pass the array to `IndexDocumentsBatch`. The following documents conform to the hotels-quickstart index, as defined by the hotel class.
 
 ```csharp
 // Upload documents in a single Upload request.
@@ -723,9 +247,7 @@ private static void UploadDocuments(SearchClient searchClient)
 }
 ```
 
-Once you initialize the [IndexDocumentsBatch](/dotnet/api/azure.search.documents.models.indexdocumentsbatch-1) object, you can send it to the index by calling [IndexDocuments](/dotnet/api/azure.search.documents.searchclient.indexdocuments) on your [SearchClient](/dotnet/api/azure.search.documents.searchclient) object.
-
-You load documents using SearchClient in `Main()`, but the operation also requires admin rights on the service, which is typically associated with SearchIndexClient. One way to set up this operation is to get SearchClient through `SearchIndexClient` (`searchIndexClient` in this example).
+The `UploadDocuments` method creates an [IndexDocumentsBatch](/dotnet/api/azure.search.documents.models.indexdocumentsbatch-1) and calls [IndexDocuments](/dotnet/api/azure.search.documents.searchclient.indexdocuments) on a [SearchClient](/dotnet/api/azure.search.documents.searchclient) to upload the documents. This quickstart obtains `SearchClient` from `SearchIndexClient` using [GetSearchClient](/dotnet/api/azure.search.documents.indexes.searchindexclient.getsearchclient), which reuses the same credentials.
 
 ```csharp
 SearchClient ingesterClient = searchIndexClient.GetSearchClient(indexName);
@@ -735,25 +257,25 @@ Console.WriteLine("{0}", "Uploading documents...\n");
 UploadDocuments(ingesterClient);
 ```
 
-Because we have a console app that runs all commands sequentially, we add a 2-second wait time between indexing and queries.
+Because this console app runs all commands sequentially, the code adds a two-second wait time between indexing and queries.
 
 ```csharp
 // Wait 2 seconds for indexing to complete before starting queries (for demo and console-app purposes only)
 Console.WriteLine("Waiting for indexing...\n");
 System.Threading.Thread.Sleep(2000);
 ```
 
-The 2-second delay compensates for indexing, which is asynchronous, so that all documents can be indexed before the queries are executed. Coding in a delay is typically only necessary in demos, tests, and sample applications.
+The two-second delay compensates for indexing, which is asynchronous, so that all documents can be indexed before the queries are executed. Coding in a delay is typically only necessary in demos, tests, and sample applications.
 
-### Search an index
+### Query the index
 
 You can get query results as soon as the first document is indexed, but actual testing of your index should wait until all documents are indexed.
 
-This section adds two pieces of functionality: query logic, and results. For queries, use the [Search](/dotnet/api/azure.search.documents.searchclient.search) method. This method takes search text (the query string) and other [options](/dotnet/api/azure.search.documents.searchoptions).
+This section adds two pieces of functionality: query logic and results. For queries, use the [Search](/dotnet/api/azure.search.documents.searchclient.search) method. This method takes search text (the query string) and other [options](/dotnet/api/azure.search.documents.searchoptions).
 
 The [SearchResults](/dotnet/api/azure.search.documents.models.searchresults-1) class represents the results.
 
-In *Program.cs*, the `WriteDocuments` method prints search results to the console.
+In `Program.cs`, the `WriteDocuments` method prints search results to the console.
 
 ```csharp
 // Write search results to console
@@ -801,7 +323,7 @@ private static void RunQueries(SearchClient searchClient)
 
     options.Select.Add("HotelId");
     options.Select.Add("HotelName");
-    options.Select.Add("Address/City");
+    options.Select.Add("Rating");
 
     response = searchClient.Search<Hotel>("*", options);
     WriteDocuments(response);
@@ -811,7 +333,7 @@ private static void RunQueries(SearchClient searchClient)
 
 #### Query example 2
 
-In the second query, search on a term, add a filter that selects documents where *Rating* is greater than 4, and then sort by Rating in descending order. Filter is a boolean expression that is evaluated over [IsFilterable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfilterable) fields in an index. Filter queries either include or exclude values. As such, there's no relevance score associated with a filter query.
+In the second query, search on a term, add a filter that selects documents where `Rating` is greater than 4, and then sort by `Rating` in descending order. A filter is a boolean expression evaluated over [IsFilterable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfilterable) fields in an index. Filter queries either include or exclude values. As such, there's no relevance score associated with a filter query.
 
 ```csharp
 // Query 2
@@ -833,7 +355,7 @@ WriteDocuments(response);
 
 #### Query example 3
 
-The third query demonstrates `searchFields`, used to scope a full text search operation to specific fields.
+The third query demonstrates `searchFields`, used to scope a full-text search operation to specific fields.
 
 ```csharp
 // Query 3
@@ -877,7 +399,7 @@ WriteDocuments(response);
 
 #### Query example 5
 
-In the fifth query, return a specific document. A document lookup is a typical response to `OnClick` event in a result set.
+In the fifth query, return a specific document. A document lookup is a typical response to an `OnClick` event in a result set.
 
 ```csharp
 // Query 5
@@ -891,11 +413,11 @@ Console.WriteLine(lookupResponse.Value.HotelId);
 
 #### Query example 6
 
-The last query shows the syntax for autocomplete, simulating a partial user input of *sa* that resolves to two possible matches in the sourceFields associated with the suggester you defined in the index.
+The last query shows the syntax for autocomplete, simulating a partial user input of *sa* that resolves to two possible matches in the `sourceFields` associated with the suggester you defined in the index.
 
 ```csharp
 // Query 6
-Console.WriteLine("Query #6: Call Autocomplete on HotelName that starts with 'sa'...\n");
+Console.WriteLine("Query #6: Call Autocomplete on HotelName...\n");
 
 var autoresponse = searchClient.Autocomplete("sa", "sg");
 WriteDocuments(autoresponse);
@@ -905,5 +427,5 @@ WriteDocuments(autoresponse);
 
 The previous queries show multiple [ways of matching terms in a query](/azure/search/search-query-overview#types-of-queries): full-text search, filters, and autocomplete.
 
-Full text search and filters are performed using the [SearchClient.Search](/dotnet/api/azure.search.documents.searchclient.search) method. A search query can be passed in the `searchText` string, while a filter expression can be passed in the [Filter](/dotnet/api/azure.search.documents.searchoptions.filter) property of the [SearchOptions](/dotnet/api/azure.search.documents.searchoptions) class. To filter without searching, just pass `"*"` for the `searchText` parameter of the [Search](/dotnet/api/azure.search.documents.searchclient.search) method. To search without filtering, leave the `Filter` property unset, or don't pass in a `SearchOptions` instance at all.
+The [SearchClient.Search](/dotnet/api/azure.search.documents.searchclient.search) method performs full-text search and filters. You can pass a search query in the `searchText` string, while you pass a filter expression in the [Filter](/dotnet/api/azure.search.documents.searchoptions.filter) property of the [SearchOptions](/dotnet/api/azure.search.documents.searchoptions) class. To filter without searching, just pass `"*"` for the `searchText` parameter of the [Search](/dotnet/api/azure.search.documents.searchclient.search) method. To search without filtering, leave the `Filter` property unset, or don't pass in a `SearchOptions` instance at all.
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "フルテキスト検索クイックスタートの全面的な更新"
}
```

### Explanation
このコードの差分は、`full-text-csharp.md` ファイルに対して大規模な変更が行われたことを示しています。主な変更点は、全体的な構成やコンテンツの見直しであり、合計で120行が追加され、598行が削除されるという大規模な修正が行われました。新しいコンテンツでは、Azure AI Searchクライアントライブラリを使用して検索インデックスの作成、読み込み、およびクエリの実行に関する詳細な手順が説明されています。

新しい形式では、クイックスタートのセクションが明確に分けられた上で、具体的なステップが示されており、ユーザーが必要としている情報にすぐにアクセスできるようになっています。また、Apache LuceneとBM25ランキングアルゴリズムに基づくフルテキスト検索の基本概念も明確に説明されています。さらに、例として使用される架空のホテルデータへのリンクが追加され、具体的なコード実行の流れが視覚的に明示されています。

全体として、文書はより整理され、高度な情報が統合されており、ユーザーエクスペリエンスが大きく向上しています。これらの変更は、コードの可読性や実用性を向上させ、ユーザーが技術的な課題に対処する際の支援となるよう設計されています。

## articles/search/includes/quickstarts/full-text-intro.md{#item-f655a1}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +0,0 @@
----
-manager: nitinme
-author: haileytap
-ms.author: haileytapia
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 06/26/2025
----
-
-In this quickstart, you use the Azure.Search.Documents client library to create, load, and query a search index with sample data for [full-text search](../../search-lucene-query-architecture.md). Full-text search uses Apache Lucene for indexing and queries and the BM25 ranking algorithm for scoring results.
-
-This quickstart uses fictional hotel data from the [azure-search-sample-data](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/hotels/hotel-json-documents) repo to populate the index.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "フルテキスト検索のイントロダクションセクションの削除"
}
```

### Explanation
このコードの差分は、`full-text-intro.md` ファイルに対する重要な変更を示しています。このファイルは完全に削除され、12行のコンテンツが削除されました。この変更により、フルテキスト検索に関する導入情報が提供されていたセクションが消失しました。

削除された内容には、Azure.Search.Documents クライアントライブラリを使用して、サンプルデータを使った検索インデックスの作成、読み込み、クエリ実行に関する基本的な説明が含まれていました。また、Apache Luceneの使用やBM25ランキングアルゴリズムについても言及されていました。このセクションは、ユーザーがフルテキスト検索の理解を深めるための基本的な情報源であったと言えます。

この変更は、関連するドキュメントの構造に大きな影響を及ぼす可能性があり、ユーザーには新たに情報を取得するための他のリソースを探す必要があるかもしれません。全体として、これによりフルテキスト検索のコンテキストが失われ、ユーザー体験の一部が損なわれる結果となっています。

## articles/search/includes/quickstarts/full-text-java.md{#item-d659f9}

<details>
<summary>Diff</summary>
````diff
@@ -4,604 +4,155 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 02/02/2026
 ---
 
-[!INCLUDE [Full text introduction](full-text-intro.md)]
+In this quickstart, you use the [Azure AI Search client library for Java](/java/api/overview/azure/search-documents-readme) to create, load, and query a search index for [full-text search](../../search-lucene-query-architecture.md), also known as keyword search.
+
+Full-text search uses Apache Lucene for indexing and queries and the BM25 ranking algorithm for scoring results. This quickstart uses fictional hotel data from the [azure-search-sample-data](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/hotels/hotel-json-documents) GitHub repository to populate the index.
 
 > [!TIP]
-> You can download the [source code](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart-keyword-search) to start with a finished project or follow these steps to create your own.
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart-keyword-search) on GitHub.
 
 ## Prerequisites
 
 - An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. For this quickstart, you can use a free service.
+- An [Azure AI Search service](../../search-create-service-portal.md). You can use a free service for this quickstart.
 
-## Microsoft Entra ID prerequisites
+- [Java 21 (LTS)](/java/openjdk/install) and [Maven](https://maven.apache.org/download.cgi).
 
-For the recommended keyless authentication with Microsoft Entra ID, you must:
+- [Visual Studio Code](https://code.visualstudio.com/download).
 
-- Install the [Azure CLI](/cli/azure/install-azure-cli).
+- [Git](https://git-scm.com/downloads) to clone the sample repository.
 
-- Assign the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
+- The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-## Get service information
+## Configure access
 
 [!INCLUDE [resource authentication](../resource-authentication.md)]
 
-## Set up
-
-The sample in this quickstart works with the Java Runtime. Install a Java Development Kit such as [Azul Zulu OpenJDK](https://www.azul.com/downloads/?package=jdk). The [Microsoft Build of OpenJDK](https://www.microsoft.com/openjdk) or your preferred JDK should also work.
-
-1. Install [Apache Maven](https://maven.apache.org/install.html). Then run `mvn -v` to confirm successful installation.
-1. Create a new `pom.xml` file in the root of your project, and copy the following code into it:
-
-    ```xml
-    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
-        <modelVersion>4.0.0</modelVersion>
-        <groupId>azure.search.sample</groupId>
-        <artifactId>azuresearchquickstart</artifactId>
-        <version>1.0.0-SNAPSHOT</version>
-        <build>
-            <sourceDirectory>src</sourceDirectory>
-            <plugins>
-            <plugin>
-                <artifactId>maven-compiler-plugin</artifactId>
-                <version>3.7.0</version>
-                <configuration>
-                <source>1.8</source>
-                <target>1.8</target>
-                </configuration>
-            </plugin>
-            </plugins>
-        </build>
-        <dependencies>
-            <dependency>
-                <groupId>junit</groupId>
-                <artifactId>junit</artifactId>
-                <version>4.11</version>
-                <scope>test</scope>
-            </dependency>
-            <dependency>
-                <groupId>com.azure</groupId>
-                <artifactId>azure-search-documents</artifactId>
-                <version>11.7.3</version>
-            </dependency>
-            <dependency>
-                <groupId>com.azure</groupId>
-                <artifactId>azure-core</artifactId>
-                <version>1.53.0</version>
-            </dependency>
-            <dependency>
-                <groupId>com.azure</groupId>
-                <artifactId>azure-identity</artifactId>
-                <version>1.15.1</version>
-            </dependency>
-        </dependencies>
-    </project>
-    ```
+## Get endpoint
+
+[!INCLUDE [resource endpoint](../resource-endpoint.md)]
 
-1. Install the dependencies including the Azure AI Search client library ([Azure.Search.Documents](/java/api/overview/azure/search)) for Java and [Azure Identity client library for Java](https://mvnrepository.com/artifact/com.azure/azure-identity) with:
+## Set up the environment
+
+1. Use Git to clone the sample repository.
 
    ```console
-   mvn clean dependency:copy-dependencies
+   git clone https://github.com/Azure-Samples/azure-search-java-samples
    ```
 
-1. For the **recommended** keyless authentication with Microsoft Entra ID, sign in to Azure with the following command:
+1. Open the `azure-search-java-samples/quickstart-keyword-search` folder in Visual Studio Code.
 
-    ```console
-    az login
-    ```
+1. Open the `App.java` file in the `src/main/java/azure/search/sample` folder.
 
-## Create, load, and query a search index
+1. Replace the placeholder value for `searchServiceEndpoint` with the URL you obtained in [Get endpoint](#get-endpoint).
 
-In the prior [set up](#set-up) section, you installed the Azure AI Search client library and other dependencies. 
+1. Use a terminal in Visual Studio Code to install the dependencies.
 
-In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [Explaining the code](#explaining-the-code) section.
+   ```console
+   mvn clean dependency:copy-dependencies
+   ```
 
-The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service.
 
-#### [Microsoft Entra ID](#tab/keyless)
+    ```azurecli
+    az login
+    ```
 
-```java
-String searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
-DefaultAzureCredential credential = new DefaultAzureCredentialBuilder().build();
-```
+## Run the code
 
-#### [API key](#tab/api-key)
+Compile and run the application.
 
-```java
-String searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
-AzureKeyCredential credential = new AzureKeyCredential("<Your search service admin key>");
+```console
+javac -d target/classes -cp "target/dependency/*" src/main/java/azure/search/sample/*.java
+java -cp "target/classes;target/dependency/*" azure.search.sample.App
 ```
----
-
-1. Create a new file named *App.java* and paste the following code into *App.java*:
-
-    ```java
-    import java.util.Arrays;
-    import java.util.ArrayList;
-    import java.time.OffsetDateTime;
-    import java.time.ZoneOffset;
-    import java.time.LocalDateTime;
-    import java.time.LocalDate;
-    import java.time.LocalTime;
-    import com.azure.core.util.Configuration;
-    import com.azure.core.util.Context;
-    import com.azure.identity.DefaultAzureCredential;
-    import com.azure.identity.DefaultAzureCredentialBuilder;
-    import com.azure.search.documents.SearchClient;
-    import com.azure.search.documents.SearchClientBuilder;
-    import com.azure.search.documents.indexes.SearchIndexClient;
-    import com.azure.search.documents.indexes.SearchIndexClientBuilder;
-    import com.azure.search.documents.indexes.models.IndexDocumentsBatch;
-    import com.azure.search.documents.models.SearchOptions;
-    import com.azure.search.documents.indexes.models.SearchIndex;
-    import com.azure.search.documents.indexes.models.SearchSuggester;
-    import com.azure.search.documents.util.AutocompletePagedIterable;
-    import com.azure.search.documents.util.SearchPagedIterable;
-    
-    public class App {
-    
-        public static void main(String[] args) {
-            // Your search service endpoint
-            "https://<Put your search service NAME here>.search.windows.net/";
-    
-            // Use the recommended keyless credential instead of the AzureKeyCredential credential.
-            DefaultAzureCredential credential = new DefaultAzureCredentialBuilder().build();
-            //AzureKeyCredential credential = new AzureKeyCredential("<Your search service admin key>");
-    
-            // Create a SearchIndexClient to send create/delete index commands
-            SearchIndexClient searchIndexClient = new SearchIndexClientBuilder()
-                .endpoint(searchServiceEndpoint)
-                .credential(credential)
-                .buildClient();
-            
-            // Create a SearchClient to load and query documents
-            String indexName = "hotels-quickstart-java";
-            SearchClient searchClient = new SearchClientBuilder()
-                .endpoint(searchServiceEndpoint)
-                .credential(credential)
-                .indexName(indexName)
-                .buildClient();
-    
-            // Create Search Index for Hotel model
-            searchIndexClient.createOrUpdateIndex(
-                new SearchIndex(indexName, SearchIndexClient.buildSearchFields(Hotel.class, null))
-                .setSuggesters(new SearchSuggester("sg", Arrays.asList("HotelName"))));
-    
-            // Upload sample hotel documents to the Search Index
-            uploadDocuments(searchClient);
-    
-            // Wait 2 seconds for indexing to complete before starting queries (for demo and console-app purposes only)
-            System.out.println("Waiting for indexing...\n");
-            try
-            {
-                Thread.sleep(2000);
-            }
-            catch (InterruptedException e)
-            {
-            }
-    
-            // Call the RunQueries method to invoke a series of queries
-            System.out.println("Starting queries...\n");
-            RunQueries(searchClient);
-    
-            // End the program
-            System.out.println("Complete.\n");
-        }
-    
-        // Upload documents in a single Upload request.
-        private static void uploadDocuments(SearchClient searchClient)
-        {
-            var hotelList = new ArrayList<Hotel>();
-    
-            var hotel = new Hotel();
-            hotel.hotelId = "1";
-            hotel.hotelName = "Stay-Kay City Hotel";
-            hotel.description = "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.";
-            hotel.category = "Boutique";
-            hotel.tags = new String[] { "view", "air conditioning", "concierge" };
-            hotel.parkingIncluded = false;
-            hotel.lastRenovationDate = OffsetDateTime.of(LocalDateTime.of(LocalDate.of(2022, 1, 18), LocalTime.of(0, 0)), ZoneOffset.UTC);
-            hotel.rating = 3.6;
-            hotel.address = new Address();
-            hotel.address.streetAddress = "677 5th Ave";
-            hotel.address.city = "New York";
-            hotel.address.stateProvince = "NY";
-            hotel.address.postalCode = "10022";
-            hotel.address.country = "USA";
-            hotelList.add(hotel);
-    
-            hotel = new Hotel();
-            hotel.hotelId = "2";
-            hotel.hotelName = "Old Century Hotel";
-            hotel.description = "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
-            hotel.category = "Boutique";
-            hotel.tags = new String[] { "pool", "free wifi", "concierge" };
-            hotel.parkingIncluded = false;
-            hotel.lastRenovationDate = OffsetDateTime.of(LocalDateTime.of(LocalDate.of(2019, 2, 18), LocalTime.of(0, 0)), ZoneOffset.UTC);
-            hotel.rating = 3.60;
-            hotel.address = new Address();
-            hotel.address.streetAddress = "140 University Town Center Dr";
-            hotel.address.city = "Sarasota";
-            hotel.address.stateProvince = "FL";
-            hotel.address.postalCode = "34243";
-            hotel.address.country = "USA";
-            hotelList.add(hotel);
-    
-            hotel = new Hotel();
-            hotel.hotelId = "3";
-            hotel.hotelName = "Gastronomic Landscape Hotel";
-            hotel.description = "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.";
-            hotel.category = "Suite";
-            hotel.tags = new String[] { "restaurant", "bar", "continental breakfast" };
-            hotel.parkingIncluded = true;
-            hotel.lastRenovationDate = OffsetDateTime.of(LocalDateTime.of(LocalDate.of(2015, 9, 20), LocalTime.of(0, 0)), ZoneOffset.UTC);
-            hotel.rating = 4.80;
-            hotel.address = new Address();
-            hotel.address.streetAddress = "3393 Peachtree Rd";
-            hotel.address.city = "Atlanta";
-            hotel.address.stateProvince = "GA";
-            hotel.address.postalCode = "30326";
-            hotel.address.country = "USA";
-            hotelList.add(hotel);
-    
-            hotel = new Hotel();
-            hotel.hotelId = "4";
-            hotel.hotelName = "Sublime Palace Hotel";
-            hotel.description = "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.";
-            hotel.category = "Boutique";
-            hotel.tags = new String[] { "concierge", "view", "air conditioning" };
-            hotel.parkingIncluded = true;
-            hotel.lastRenovationDate = OffsetDateTime.of(LocalDateTime.of(LocalDate.of(2020, 2, 06), LocalTime.of(0, 0)), ZoneOffset.UTC);
-            hotel.rating = 4.60;
-            hotel.address = new Address();
-            hotel.address.streetAddress = "7400 San Pedro Ave";
-            hotel.address.city = "San Antonio";
-            hotel.address.stateProvince = "TX";
-            hotel.address.postalCode = "78216";
-            hotel.address.country = "USA";
-            hotelList.add(hotel);
-    
-            var batch = new IndexDocumentsBatch<Hotel>();
-            batch.addMergeOrUploadActions(hotelList);
-            try
-            {
-                searchClient.indexDocuments(batch);
-            }
-            catch (Exception e)
-            {
-                e.printStackTrace();
-                // If for some reason any documents are dropped during indexing, you can compensate by delaying and
-                // retrying. This simple demo just logs failure and continues
-                System.err.println("Failed to index some of the documents");
-            }
-        }
-    
-        // Write search results to console
-        private static void WriteSearchResults(SearchPagedIterable searchResults)
-        {
-            searchResults.iterator().forEachRemaining(result ->
-            {
-                Hotel hotel = result.getDocument(Hotel.class);
-                System.out.println(hotel);
-            });
-    
-            System.out.println();
-        }
-    
-        // Write autocomplete results to console
-        private static void WriteAutocompleteResults(AutocompletePagedIterable autocompleteResults)
-        {
-            autocompleteResults.iterator().forEachRemaining(result ->
-            {
-                String text = result.getText();
-                System.out.println(text);
-            });
-    
-            System.out.println();
-        }
-    
-        // Run queries, use WriteDocuments to print output
-        private static void RunQueries(SearchClient searchClient)
-        {
-            // Query 1
-            System.out.println("Query #1: Search on empty term '*' to return all documents, showing a subset of fields...\n");
-    
-            SearchOptions options = new SearchOptions();
-            options.setIncludeTotalCount(true);
-            options.setFilter("");
-            options.setOrderBy("");
-            options.setSelect("HotelId", "HotelName", "Address/City");
-    
-            WriteSearchResults(searchClient.search("*", options, Context.NONE));
-    
-            // Query 2
-            System.out.println("Query #2: Search on 'hotels', filter on 'Rating gt 4', sort by Rating in descending order...\n");
-    
-            options = new SearchOptions();
-            options.setFilter("Rating gt 4");
-            options.setOrderBy("Rating desc");
-            options.setSelect("HotelId", "HotelName", "Rating");
-    
-            WriteSearchResults(searchClient.search("hotels", options, Context.NONE));
-    
-            // Query 3
-            System.out.println("Query #3: Limit search to specific fields (pool in Tags field)...\n");
-    
-            options = new SearchOptions();
-            options.setSearchFields("Tags");
-    
-            options.setSelect("HotelId", "HotelName", "Tags");
-    
-            WriteSearchResults(searchClient.search("pool", options, Context.NONE));
-    
-            // Query 4
-            System.out.println("Query #4: Facet on 'Category'...\n");
-    
-            options = new SearchOptions();
-            options.setFilter("");
-            options.setFacets("Category");
-            options.setSelect("HotelId", "HotelName", "Category");
-    
-            WriteSearchResults(searchClient.search("*", options, Context.NONE));
-    
-            // Query 5
-            System.out.println("Query #5: Look up a specific document...\n");
-    
-            Hotel lookupResponse = searchClient.getDocument("3", Hotel.class);
-            System.out.println(lookupResponse.hotelId);
-            System.out.println();
-    
-             // Query 6
-            System.out.println("Query #6: Call Autocomplete on HotelName that starts with 's'...\n");
-    
-            WriteAutocompleteResults(searchClient.autocomplete("s", "sg"));
-        }
-    }
-    ```
 
-1. Create a new file named *Hotel.java* and paste the following code into *Hotel.java*:
+### Output
 
-    ```java
-    import com.azure.search.documents.indexes.SearchableField;
-    import com.azure.search.documents.indexes.SimpleField;
-    import com.fasterxml.jackson.annotation.JsonInclude;
-    import com.fasterxml.jackson.annotation.JsonProperty;
-    import com.fasterxml.jackson.core.JsonProcessingException;
-    import com.fasterxml.jackson.databind.ObjectMapper;
-    import com.fasterxml.jackson.annotation.JsonInclude.Include;
-    
-    import java.time.OffsetDateTime;
-    
-    /**
-     * Model class representing a hotel.
-     */
-    @JsonInclude(Include.NON_NULL)
-    public class Hotel {
-        /**
-         * Hotel ID
-         */
-        @JsonProperty("HotelId")
-        @SimpleField(isKey = true)
-        public String hotelId;
-    
-        /**
-         * Hotel name
-         */
-        @JsonProperty("HotelName")
-        @SearchableField(isSortable = true)
-        public String hotelName;
-    
-        /**
-         * Description
-         */
-        @JsonProperty("Description")
-        @SearchableField(analyzerName = "en.microsoft")
-        public String description;
-    
-        /**
-         * Category
-         */
-        @JsonProperty("Category")
-        @SearchableField(isFilterable = true, isSortable = true, isFacetable = true)
-        public String category;
-    
-        /**
-         * Tags
-         */
-        @JsonProperty("Tags")
-        @SearchableField(isFilterable = true, isFacetable = true)
-        public String[] tags;
-    
-        /**
-         * Whether parking is included
-         */
-        @JsonProperty("ParkingIncluded")
-        @SimpleField(isFilterable = true, isSortable = true, isFacetable = true)
-        public Boolean parkingIncluded;
-    
-        /**
-         * Last renovation time
-         */
-        @JsonProperty("LastRenovationDate")
-        @SimpleField(isFilterable = true, isSortable = true, isFacetable = true)
-        public OffsetDateTime lastRenovationDate;
-    
-        /**
-         * Rating
-         */
-        @JsonProperty("Rating")
-        @SimpleField(isFilterable = true, isSortable = true, isFacetable = true)
-        public Double rating;
-    
-        /**
-         * Address
-         */
-        @JsonProperty("Address")
-        public Address address;
-    
-        @Override
-        public String toString()
-        {
-            try
-            {
-                return new ObjectMapper().writeValueAsString(this);
-            }
-            catch (JsonProcessingException e)
-            {
-                e.printStackTrace();
-                return "";
-            }
-        }
-    }
-    ```
+The output should be similar to the following:
 
-1. Create a new file named *Address.java* and paste the following code into *Address.java*:
+```
+Waiting for indexing...
 
-    ```java
-    import com.azure.search.documents.indexes.SearchableField;
-    import com.fasterxml.jackson.annotation.JsonInclude;
-    import com.fasterxml.jackson.annotation.JsonProperty;
-    import com.fasterxml.jackson.annotation.JsonInclude.Include;
-    
-    /**
-     * Model class representing an address.
-     */
-    @JsonInclude(Include.NON_NULL)
-    public class Address {
-        /**
-         * Street address
-         */
-        @JsonProperty("StreetAddress")
-        @SearchableField
-        public String streetAddress;
-    
-        /**
-         * City
-         */
-        @JsonProperty("City")
-        @SearchableField(isFilterable = true, isSortable = true, isFacetable = true)
-        public String city;
-    
-        /**
-         * State or province
-         */
-        @JsonProperty("StateProvince")
-        @SearchableField(isFilterable = true, isSortable = true, isFacetable = true)
-        public String stateProvince;
-    
-        /**
-         * Postal code
-         */
-        @JsonProperty("PostalCode")
-        @SearchableField(isFilterable = true, isSortable = true, isFacetable = true)
-        public String postalCode;
-    
-        /**
-         * Country
-         */
-        @JsonProperty("Country")
-        @SearchableField(isFilterable = true, isSortable = true, isFacetable = true)
-        public String country;
-    }
-    ```
+Starting queries...
 
+Query #1: Search on empty term '*' to return all documents, showing a subset of fields...
 
-1. Run your new console application:
+{"HotelId":"3","HotelName":"Gastronomic Landscape Hotel","Address":{"City":"Atlanta"}}
+{"HotelId":"2","HotelName":"Old Century Hotel","Address":{"City":"Sarasota"}}
+{"HotelId":"4","HotelName":"Sublime Palace Hotel","Address":{"City":"San Antonio"}}
+{"HotelId":"1","HotelName":"Stay-Kay City Hotel","Address":{"City":"New York"}}
 
-    ```console
-    javac Address.java App.java Hotel.java -cp ".;target\dependency\*"
-    java -cp ".;target\dependency\*" App
-    ```
+Query #2: Search on 'hotels', filter on 'Rating gt 4', sort by Rating in descending order...
 
-## Explaining the code
+{"HotelId":"3","HotelName":"Gastronomic Landscape Hotel","Rating":4.8}
+{"HotelId":"4","HotelName":"Sublime Palace Hotel","Rating":4.6}
 
-In the previous sections, you created a new console application and installed the Azure AI Search client library. You added code to create a search index, load it with documents, and run queries. You ran the program to see the results in the console. 
+Query #3: Limit search to specific fields (pool in Tags field)...
 
-In this section, we explain the code you added to the console application.
+{"HotelId":"2","HotelName":"Old Century Hotel","Tags":["pool","free wifi","concierge"]}
 
-### Create a search client
+Query #4: Facet on 'Category'...
 
-In *App.java* you created two clients:
+{"HotelId":"3","HotelName":"Gastronomic Landscape Hotel","Category":"Suite"}
+{"HotelId":"2","HotelName":"Old Century Hotel","Category":"Boutique"}
+{"HotelId":"4","HotelName":"Sublime Palace Hotel","Category":"Boutique"}
+{"HotelId":"1","HotelName":"Stay-Kay City Hotel","Category":"Boutique"}
 
-- SearchIndexClient creates the index.
-- SearchClient loads and queries an existing index.
+Query #5: Look up a specific document...
 
-Both clients need the search service endpoint and credentials described previously in the resource information section.
+3
 
-The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
+Query #6: Call Autocomplete on HotelName that starts with 's'...
 
-#### [Microsoft Entra ID](#tab/keyless)
+stay
+sublime
 
-```java
-String searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
-DefaultAzureCredential credential = new DefaultAzureCredentialBuilder().build();
+Complete.
 ```
 
-#### [API key](#tab/api-key)
+## Understand the code
 
-```java
-String searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
-AzureKeyCredential credential = new AzureKeyCredential("<Your search service admin key>");
-```
----
+Now that you've run the code, let's break down the key steps:
 
-```java
-public static void main(String[] args) {
-    // Your search service endpoint
-    String searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
-
-    // Use the recommended keyless credential instead of the AzureKeyCredential credential.
-    DefaultAzureCredential credential = new DefaultAzureCredentialBuilder().build();
-    //AzureKeyCredential credential = new AzureKeyCredential("Your search service admin key");
-
-    // Create a SearchIndexClient to send create/delete index commands
-    SearchIndexClient searchIndexClient = new SearchIndexClientBuilder()
-        .endpoint(searchServiceEndpoint)
-        .credential(credential)
-        .buildClient();
-    
-    // Create a SearchClient to load and query documents
-    String indexName = "hotels-quickstart-java";
-    SearchClient searchClient = new SearchClientBuilder()
-        .endpoint(searchServiceEndpoint)
-        .credential(credential)
-        .indexName(indexName)
-        .buildClient();
-
-    // Create Search Index for Hotel model
-    searchIndexClient.createOrUpdateIndex(
-        new SearchIndex(indexName, SearchIndexClient.buildSearchFields(Hotel.class, null))
-        .setSuggesters(new SearchSuggester("sg", Arrays.asList("HotelName"))));
-
-    // REDACTED FOR BREVITY . . . 
-}
-```
+1. [Create a search client](#create-a-search-client)
+1. [Create a search index](#create-a-search-index)
+1. [Upload documents to the index](#upload-documents-to-the-index)
+1. [Query the index](#query-the-index)
 
+### Create a search client
 
-### Create an index
+In `App.java`, you create two clients:
 
-This quickstart builds a Hotels index that you load with hotel data and execute queries against. In this step, you define the fields in the index. Each field definition includes a name, data type, and attributes that determine how the field is used.
+- [SearchIndexClient](/java/api/com.azure.search.documents.indexes.searchindexclient) creates the index.
+- [SearchClient](/java/api/com.azure.search.documents.searchclient) loads and queries an existing index.
 
-In this example, synchronous methods of the *Azure.Search.Documents* library are used for simplicity and readability. However, for production scenarios, you should use asynchronous methods to keep your app scalable and responsive. For example, you would use [CreateIndexAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindexasync) instead of [CreateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindex).
+Both clients require the service endpoint and a credential for authentication. In this quickstart, you use [DefaultAzureCredential](/java/api/com.azure.identity.defaultazurecredential) for keyless authentication with Microsoft Entra ID.
+
+### Create a search index
+
+This quickstart builds a hotels index that you load with hotel data and execute queries against. In this step, you define the fields in the index. Each field definition includes a name, data type, and attributes that determine how the field is used.
+
+This example uses synchronous methods of the [SearchIndexClient](/java/api/com.azure.search.documents.indexes.searchindexclient) class for simplicity and readability. However, for production scenarios, use the [SearchIndexAsyncClient](/java/api/com.azure.search.documents.indexes.searchindexasyncclient) class to keep your app scalable and responsive.
 
 #### Define the structures
 
-You created two helper classes, *Hotel.java* and *Address.java*, to define the structure of a hotel document and its address. The Hotel class includes fields for a hotel ID, name, description, category, tags, parking, renovation date, rating, and address. The Address class includes fields for street address, city, state/province, postal code, and country/region.
+You create two helper classes, `Hotel.java` and `Address.java`, to define the structure of a hotel document and its address. The `Hotel` class includes fields for a hotel ID, name, description, category, tags, parking, renovation date, rating, and address. The `Address` class includes fields for street address, city, state/province, postal code, and country/region.
 
-In the Azure.Search.Documents client library, you can use [SearchableField](/java/api/com.azure.search.documents.indexes.searchablefield) and [SimpleField](/java/api/com.azure.search.documents.indexes.simplefield) to streamline field definitions.
+In the azure-search-documents client library, you can use [SearchableField](/java/api/com.azure.search.documents.indexes.searchablefield) and [SimpleField](/java/api/com.azure.search.documents.indexes.simplefield) to streamline field definitions. Both are annotations that you can apply to fields or methods to generate a [SearchField](/java/api/com.azure.search.documents.indexes.models.searchfield):
 
-* `SimpleField` can be any data type, is always non-searchable (ignored for full text search queries), and is retrievable (not hidden). Other attributes are off by default, but can be enabled. You might use a SimpleField for document IDs or fields used only in filters, facets, or scoring profiles. If so, be sure to apply any attributes that are necessary for the scenario, such as IsKey = true for a document ID.
-* `SearchableField` must be a string, and is always searchable and retrievable. Other attributes are off by default, but can be enabled. Because this field type is searchable, it supports synonyms and the full complement of analyzer properties.
++ `SimpleField` can be any data type, is always nonsearchable (ignored for full-text search queries), and is retrievable (not hidden). Other attributes are off by default, but can be enabled. You might use a `SimpleField` for document IDs or fields used only in filters, facets, or scoring profiles. If so, apply any attributes that are necessary for the scenario, such as `isKey = true` for a document ID.
++ `SearchableField` must be a string, and is always searchable and retrievable. Other attributes are off by default, but can be enabled. Because this field type is searchable, it supports synonyms and the full complement of analyzer properties.
 
-Whether you use the basic `SearchField` API or either one of the helper models, you must explicitly enable filter, facet, and sort attributes. For example, `isFilterable`, `isSortable`, and `isFacetable` must be explicitly attributed, as shown in the previous sample.
+Whether you use the basic `SearchField` API or either one of the helper models, you must explicitly enable filter, facet, and sort attributes. For example, [isFilterable](/java/api/com.azure.search.documents.indexes.models.searchfield), [isSortable](/java/api/com.azure.search.documents.indexes.models.searchfield), and [isFacetable](/java/api/com.azure.search.documents.indexes.models.searchfield) must be explicitly attributed, as shown in the previous sample.
 
 #### Create the search index
 
-In `App.java`, you create a `SearchIndex` object in the `main` method, and then call the `createOrUpdateIndex` method to create the index in your search service. The index also includes a `SearchSuggester` to enable autocomplete on the specified fields.
+In `App.java`, you create a [SearchIndex](/java/api/com.azure.search.documents.indexes.models.searchindex) object, and then call the [createOrUpdateIndex](/java/api/com.azure.search.documents.indexes.searchindexclient) method to express the index in your search service. The index also includes a [SearchSuggester](/java/api/com.azure.search.documents.indexes.models.searchsuggester) to enable autocomplete on the specified fields.
 
 ```java
 // Create Search Index for Hotel model
@@ -610,15 +161,15 @@ searchIndexClient.createOrUpdateIndex(
     .setSuggesters(new SearchSuggester("sg", Arrays.asList("HotelName"))));
 ```
 
-### Load documents
+### Upload documents to the index
 
 Azure AI Search searches over content stored in the service. In this step, you load JSON documents that conform to the hotel index you created.
 
-In Azure AI Search, search documents are data structures that are both inputs to indexing and outputs from queries. As obtained from an external data source, document inputs might be rows in a database, blobs in Blob storage, or JSON documents on disk. In this example, we're taking a shortcut and embedding JSON documents for four hotels in the code itself.
+In Azure AI Search, search documents are data structures that are both inputs to indexing and outputs from queries. As obtained from an external data source, document inputs might be rows in a database, blobs in Azure Blob Storage, or JSON documents on disk. In this example, you take a shortcut and embed JSON documents for four hotels directly.
 
-When uploading documents, you must use an [IndexDocumentsBatch](/java/api/com.azure.search.documents.indexes.models.indexdocumentsbatch) object. An `IndexDocumentsBatch` object contains a collection of [IndexActions](/java/api/com.azure.search.documents.models.indexaction), each of which contains a document and a property telling Azure AI Search what action to perform (upload, merge, delete, and mergeOrUpload).
+When uploading documents, you must use an [IndexDocumentsBatch](/java/api/com.azure.search.documents.indexes.models.indexdocumentsbatch) object. An `IndexDocumentsBatch` object contains a collection of [IndexActions](/java/api/com.azure.search.documents.models.indexaction), each of which contains a document and a property telling Azure AI Search what action to perform ([upload, merge, delete, and mergeOrUpload](/azure/search/search-what-is-data-import#indexing-actions)).
 
-In `App.java`, you create documents and index actions, and then pass them to `IndexDocumentsBatch`. The following documents conform to the hotels-quickstart index, as defined by the hotel class.
+In `App.java`, you create an array of documents and index actions, and then pass the array to `IndexDocumentsBatch`. The following documents conform to the hotels-quickstart index, as defined by the hotel class.
 
 ```java
 private static void uploadDocuments(SearchClient searchClient)
@@ -660,15 +211,13 @@ private static void uploadDocuments(SearchClient searchClient)
 }
 ```
 
-Once you initialize the `IndexDocumentsBatch` object, you can send it to the index by calling [indexDocuments](/java/api/com.azure.search.documents.searchclient#com-azure-search-documents-searchclient-indexdocuments(com-azure-search-documents-indexes-models-indexdocumentsbatch(-))) on your `SearchClient` object.
-
-You load documents using SearchClient in `main()`, but the operation also requires admin rights on the service, which is typically associated with SearchIndexClient. One way to set up this operation is to get SearchClient through `SearchIndexClient` (`searchIndexClient` in this example).
+The `uploadDocuments` method creates an [IndexDocumentsBatch](/java/api/com.azure.search.documents.indexes.models.indexdocumentsbatch) and calls [indexDocuments](/java/api/com.azure.search.documents.searchclient) on a [SearchClient](/java/api/com.azure.search.documents.searchclient) to upload the documents. This quickstart creates `SearchClient` independently using [SearchClientBuilder](/java/api/com.azure.search.documents.searchclientbuilder), which requires configuring the endpoint and credentials separately.
 
 ```java
 uploadDocuments(searchClient);
 ```
 
-Because we have a console app that runs all commands sequentially, we add a 2-second wait time between indexing and queries.
+Because this console app runs all commands sequentially, the code adds a two-second wait time between indexing and queries.
 
 ```java
 // Wait 2 seconds for indexing to complete before starting queries (for demo and console-app purposes only)
@@ -682,13 +231,15 @@ catch (InterruptedException e)
 }
 ```
 
-The 2-second delay compensates for indexing, which is asynchronous, so that all documents can be indexed before the queries are executed. Coding in a delay is typically only necessary in demos, tests, and sample applications.
+The two-second delay compensates for indexing, which is asynchronous, so that all documents can be indexed before the queries are executed. Coding in a delay is typically only necessary in demos, tests, and sample applications.
 
-### Search an index
+### Query the index
 
 You can get query results as soon as the first document is indexed, but actual testing of your index should wait until all documents are indexed.
 
-This section adds two pieces of functionality: query logic and results. For queries, use the Search method. This method takes search text (the query string) and other options.
+This section adds two pieces of functionality: query logic and results. For queries, use the [search](/java/api/com.azure.search.documents.searchclient) method. This method takes search text (the query string) and other [options](/java/api/com.azure.search.documents.models.searchoptions).
+
+The [SearchPagedIterable](/java/api/com.azure.search.documents.util.searchpagediterable) class represents the results.
 
 In `App.java`, the `WriteDocuments` method prints search results to the console.
 
@@ -741,7 +292,7 @@ private static void RunQueries(SearchClient searchClient)
 
 #### Query example 2
 
-In the second query, search on a term, add a filter that selects documents where Rating is greater than 4, and then sort by *Rating* in descending order. Filter is a boolean expression that is evaluated over `isFilterable` fields in an index. Filter queries either include or exclude values. As such, there's no relevance score associated with a filter query.
+In the second query, search on a term, add a filter that selects documents where `Rating` is greater than 4, and then sort by `Rating` in descending order. A filter is a boolean expression evaluated over [isFilterable](/java/api/com.azure.search.documents.indexes.models.searchfield) fields in an index. Filter queries either include or exclude values. As such, there's no relevance score associated with a filter query.
 
 ```java
 // Query 2
@@ -757,7 +308,7 @@ WriteSearchResults(searchClient.search("hotels", options, Context.NONE));
 
 #### Query example 3
 
-The third query demonstrates `searchFields`, used to scope a full text search operation to specific fields.
+The third query demonstrates `searchFields`, used to scope a full-text search operation to specific fields.
 
 ```java
 // Query 3
@@ -789,7 +340,7 @@ WriteSearchResults(searchClient.search("*", options, Context.NONE));
 
 #### Query example 5
 
-In the fifth query, return a specific document.
+In the fifth query, return a specific document. A document lookup is a typical response to an `OnClick` event in a result set.
 
 ```java
 // Query 5
@@ -813,7 +364,7 @@ WriteAutocompleteResults(searchClient.autocomplete("s", "sg"));
 
 #### Summary of queries
 
-The previous queries show multiple ways of matching terms in a query: full-text search, filters, and autocomplete.
+The previous queries show multiple [ways of matching terms in a query](/azure/search/search-query-overview#types-of-queries): full-text search, filters, and autocomplete.
 
-Full text search and filters are performed using the [SearchClient.search](/java/api/com.azure.search.documents.searchclient#com-azure-search-documents-searchclient-search(java-lang-string)) method. A search query can be passed in the `searchText` string, while a filter expression can be passed in the `filter` property of the [SearchOptions](/java/api/com.azure.search.documents.models.searchoptions) class. To filter without searching, just pass "*" for the `searchText` parameter of the `search` method. To search without filtering, leave the `filter` property unset, or don't pass in a `SearchOptions` instance at all.
+The [SearchClient.search](/java/api/com.azure.search.documents.searchclient) method performs full-text search and filters. You can pass a search query in the `searchText` string, while you pass a filter expression in the [filter](/java/api/com.azure.search.documents.models.searchoptions) property of the [SearchOptions](/java/api/com.azure.search.documents.models.searchoptions) class. To filter without searching, just pass `"*"` for the `searchText` parameter of the [search](/java/api/com.azure.search.documents.searchclient) method. To search without filtering, leave the `filter` property unset, or don't pass in a `SearchOptions` instance at all.
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "フルテキスト検索のクイックスタートに関する大規模な更新"
}
```

### Explanation
このコードの差分は、`full-text-java.md` ファイルに対する大規模な変更を示しています。このファイルでは、99行の新規追加が行われ、548行が削除されるという大幅な修正が実施されました。変更の目的は、より効果的にフルテキスト検索を使ったクイックスタートの内容を改善することです。

新しい内容では、Azure AI Search Javaクライアントライブラリを使用して検索インデックスを作成、読み込み、クエリを行う手順が簡潔に説明されています。Apache LuceneとBM25ランキングアルゴリズムの利用や、サンプルデータの取り扱いについても新たに詳細に記載されています。特に、Azureの各種ツールのセットアップや依存関係のインストール手順が明確に示されており、ユーザーの理解を助ける構成になっています。

加えて、新しい形式では、コードの実行手順や環境設定の指示が明確に分けられ、ユーザーが早く開始できるよう配慮されています。最後に、典型的なクエリの実行手順やその出力例が追加され、実際の使用方法について具体的な洞察を提供しています。

全体として、これによりドキュメントは一貫性を持ち、分かりやすくなり、ユーザーがフルテキスト検索の機能を効果的に活用できるように設計されていることが強調されています。

## articles/search/includes/quickstarts/full-text-javascript.md{#item-568e3a}

<details>
<summary>Diff</summary>
````diff
@@ -4,553 +4,145 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 02/02/2026
 ---
 
-[!INCLUDE [Full text introduction](full-text-intro.md)]
+In this quickstart, you use the [Azure AI Search client library for JavaScript](/javascript/api/overview/azure/search-documents-readme) to create, load, and query a search index for [full-text search](../../search-lucene-query-architecture.md), also known as keyword search.
+
+Full-text search uses Apache Lucene for indexing and queries and the BM25 ranking algorithm for scoring results. This quickstart uses fictional hotel data from the [azure-search-sample-data](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/hotels/hotel-json-documents) GitHub repository to populate the index.
 
 > [!TIP]
-> You can download the [source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-keyword-search) to start with a finished project or follow these steps to create your own.
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-keyword-search) on GitHub.
 
 ## Prerequisites
 
 - An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. For this quickstart, you can use a free service.
+- An [Azure AI Search service](../../search-create-service-portal.md). You can use a free service for this quickstart.
 
-## Microsoft Entra ID prerequisites
+- The latest LTS version of [Node.js](https://nodejs.org/en/download/).
 
-For the recommended keyless authentication with Microsoft Entra ID, you must:
+- [Visual Studio Code](https://code.visualstudio.com/download).
 
-- Install the [Azure CLI](/cli/azure/install-azure-cli).
+- [Git](https://git-scm.com/downloads) to clone the sample repository.
 
-- Assign the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
+- The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-## Get service information
+## Configure access
 
 [!INCLUDE [resource authentication](../resource-authentication.md)]
 
-## Set up
+## Get endpoint
 
-1. Create a new folder `full-text-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
+[!INCLUDE [resource endpoint](../resource-endpoint.md)]
 
-    ```shell
-    mkdir full-text-quickstart && cd full-text-quickstart
-    ```
+## Set up the environment
 
-1. Create the `package.json` with the following command:
+1. Use Git to clone the sample repository.
 
-    ```shell
-    npm init -y
-    ```
+   ```console
+   git clone https://github.com/Azure-Samples/azure-search-javascript-samples
+   ```
 
-1. Install the Azure AI Search client library ([Azure.Search.Documents](/javascript/api/overview/azure/search-documents-readme)) for JavaScript with:
+1. Open the `azure-search-javascript-samples/quickstart-keyword-search` folder in Visual Studio Code.
 
-    ```console
-    npm install @azure/search-documents
-    ```
+1. Rename the `sample.env` file to `.env`, and then open the file.
 
-1. For the **recommended** passwordless authentication, install the Azure Identity client library with:
+1. Replace the placeholder value for `SEARCH_API_ENDPOINT` with the URL you obtained in [Get endpoint](#get-endpoint).
+
+1. Use a terminal in Visual Studio Code to install the dependencies.
 
     ```console
-    npm install @azure/identity
+    npm install
     ```
 
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service.
 
+    ```azurecli
+    az login
+    ```
 
-## Create, load, and query a search index
+## Run the code
 
-In the prior [set up](#set-up) section, you installed the Azure AI Search client library and other dependencies. 
+Run the application.
 
-In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [Explaining the code](#explaining-the-code) section.
+```console
+node index.js
+```
 
-The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
+### Output
 
-#### [Microsoft Entra ID](#tab/keyless)
+The output should be similar to the following:
 
-```java
-String searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
-DefaultAzureCredential credential = new DefaultAzureCredentialBuilder().build();
 ```
-
-#### [API key](#tab/api-key)
-
-```java
-String searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
-AzureKeyCredential credential = new AzureKeyCredential("<Your search service admin key>");
+Running Azure AI Search Javascript quickstart...
+Checking if index exists...
+Deleting index...
+Creating index...
+Index named hotels-quickstart-js has been created.
+Uploading documents...
+Index operations succeeded: true
+Querying the index...
+
+Query #1 - search everything:
+{"HotelId":"3","HotelName":"Gastronomic Landscape Hotel","Rating":4.8}
+{"HotelId":"2","HotelName":"Old Century Hotel","Rating":3.6}
+{"HotelId":"4","HotelName":"Sublime Palace Hotel","Rating":4.6}
+{"HotelId":"1","HotelName":"Stay-Kay City Hotel","Rating":3.6}
+Result count: 4
+
+Query #2 - search with filter, orderBy, and select:
+{"HotelId":"2","HotelName":"Old Century Hotel","Rating":3.6}
+
+Query #3 - limit searchFields:
+{"HotelId":"4","HotelName":"Sublime Palace Hotel","Rating":4.6}
+
+Query #4 - limit searchFields and use facets:
+{"HotelId":"3","HotelName":"Gastronomic Landscape Hotel","Rating":4.8}
+{"HotelId":"2","HotelName":"Old Century Hotel","Rating":3.6}
+{"HotelId":"4","HotelName":"Sublime Palace Hotel","Rating":4.6}
+{"HotelId":"1","HotelName":"Stay-Kay City Hotel","Rating":3.6}
+
+Query #5 - Lookup document:
+HotelId: 3; HotelName: Gastronomic Landscape Hotel
 ```
----
-
-1. Create a new file named *index.js* and paste the following code into *index.js*:
-
-    ```javascript
-    // Import from the @azure/search-documents library
-    import { SearchIndexClient, odata } from "@azure/search-documents";
-    // Import from the Azure Identity library
-    import { DefaultAzureCredential } from "@azure/identity";
-    // Importing the hotels sample data
-    import hotelData from './hotels.json' assert { type: "json" };
-    // Load the .env file if it exists
-    import * as dotenv from "dotenv";
-    dotenv.config();
-    // Defining the index definition
-    const indexDefinition = {
-        "name": "hotels-quickstart",
-        "fields": [
-            {
-                "name": "HotelId",
-                "type": "Edm.String",
-                "key": true,
-                "filterable": true
-            },
-            {
-                "name": "HotelName",
-                "type": "Edm.String",
-                "searchable": true,
-                "filterable": false,
-                "sortable": true,
-                "facetable": false
-            },
-            {
-                "name": "Description",
-                "type": "Edm.String",
-                "searchable": true,
-                "filterable": false,
-                "sortable": false,
-                "facetable": false,
-                "analyzerName": "en.lucene"
-            },
-            {
-                "name": "Description_fr",
-                "type": "Edm.String",
-                "searchable": true,
-                "filterable": false,
-                "sortable": false,
-                "facetable": false,
-                "analyzerName": "fr.lucene"
-            },
-            {
-                "name": "Category",
-                "type": "Edm.String",
-                "searchable": true,
-                "filterable": true,
-                "sortable": true,
-                "facetable": true
-            },
-            {
-                "name": "Tags",
-                "type": "Collection(Edm.String)",
-                "searchable": true,
-                "filterable": true,
-                "sortable": false,
-                "facetable": true
-            },
-            {
-                "name": "ParkingIncluded",
-                "type": "Edm.Boolean",
-                "filterable": true,
-                "sortable": true,
-                "facetable": true
-            },
-            {
-                "name": "LastRenovationDate",
-                "type": "Edm.DateTimeOffset",
-                "filterable": true,
-                "sortable": true,
-                "facetable": true
-            },
-            {
-                "name": "Rating",
-                "type": "Edm.Double",
-                "filterable": true,
-                "sortable": true,
-                "facetable": true
-            },
-            {
-                "name": "Address",
-                "type": "Edm.ComplexType",
-                "fields": [
-                    {
-                        "name": "StreetAddress",
-                        "type": "Edm.String",
-                        "filterable": false,
-                        "sortable": false,
-                        "facetable": false,
-                        "searchable": true
-                    },
-                    {
-                        "name": "City",
-                        "type": "Edm.String",
-                        "searchable": true,
-                        "filterable": true,
-                        "sortable": true,
-                        "facetable": true
-                    },
-                    {
-                        "name": "StateProvince",
-                        "type": "Edm.String",
-                        "searchable": true,
-                        "filterable": true,
-                        "sortable": true,
-                        "facetable": true
-                    },
-                    {
-                        "name": "PostalCode",
-                        "type": "Edm.String",
-                        "searchable": true,
-                        "filterable": true,
-                        "sortable": true,
-                        "facetable": true
-                    },
-                    {
-                        "name": "Country",
-                        "type": "Edm.String",
-                        "searchable": true,
-                        "filterable": true,
-                        "sortable": true,
-                        "facetable": true
-                    }
-                ]
-            }
-        ],
-        "suggesters": [
-            {
-                "name": "sg",
-                "searchMode": "analyzingInfixMatching",
-                "sourceFields": [
-                    "HotelName"
-                ]
-            }
-        ]
-    };
-    async function main() {
-        // Your search service endpoint
-        const searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
-        // Use the recommended keyless credential instead of the AzureKeyCredential credential.
-        const credential = new DefaultAzureCredential();
-        //const credential = new AzureKeyCredential(Your search service admin key);
-        // Create a SearchIndexClient to send create/delete index commands
-        const searchIndexClient = new SearchIndexClient(searchServiceEndpoint, credential);
-        // Creating a search client to upload documents and issue queries
-        const indexName = "hotels-quickstart";
-        const searchClient = searchIndexClient.getSearchClient(indexName);
-        console.log('Checking if index exists...');
-        await deleteIndexIfExists(searchIndexClient, indexName);
-        console.log('Creating index...');
-        let index = await searchIndexClient.createIndex(indexDefinition);
-        console.log(`Index named ${index.name} has been created.`);
-        console.log('Uploading documents...');
-        let indexDocumentsResult = await searchClient.mergeOrUploadDocuments(hotelData['value']);
-        console.log(`Index operations succeeded: ${JSON.stringify(indexDocumentsResult.results[0].succeeded)} `);
-        // waiting one second for indexing to complete (for demo purposes only)
-        sleep(1000);
-        console.log('Querying the index...');
-        console.log();
-        await sendQueries(searchClient);
-    }
-    async function deleteIndexIfExists(searchIndexClient, indexName) {
-        try {
-            await searchIndexClient.deleteIndex(indexName);
-            console.log('Deleting index...');
-        }
-        catch {
-            console.log('Index does not exist yet.');
-        }
-    }
-    async function sendQueries(searchClient) {
-        // Query 1
-        console.log('Query #1 - search everything:');
-        let searchOptions = {
-            includeTotalCount: true,
-            select: ["HotelId", "HotelName", "Rating"]
-        };
-        let searchResults = await searchClient.search("*", searchOptions);
-        for await (const result of searchResults.results) {
-            console.log(`${JSON.stringify(result.document)}`);
-        }
-        console.log(`Result count: ${searchResults.count}`);
-        console.log();
-        // Query 2
-        console.log('Query #2 - search with filter, orderBy, and select:');
-        let state = 'FL';
-        searchOptions = {
-            filter: odata `Address/StateProvince eq ${state}`,
-            orderBy: ["Rating desc"],
-            select: ["HotelId", "HotelName", "Rating"]
-        };
-        searchResults = await searchClient.search("wifi", searchOptions);
-        for await (const result of searchResults.results) {
-            console.log(`${JSON.stringify(result.document)}`);
-        }
-        console.log();
-        // Query 3
-        console.log('Query #3 - limit searchFields:');
-        searchOptions = {
-            select: ["HotelId", "HotelName", "Rating"],
-            searchFields: ["HotelName"]
-        };
-        searchResults = await searchClient.search("sublime palace", searchOptions);
-        for await (const result of searchResults.results) {
-            console.log(`${JSON.stringify(result.document)}`);
-        }
-        console.log();
-        // Query 4
-        console.log('Query #4 - limit searchFields and use facets:');
-        searchOptions = {
-            facets: ["Category"],
-            select: ["HotelId", "HotelName", "Rating"],
-            searchFields: ["HotelName"]
-        };
-        searchResults = await searchClient.search("*", searchOptions);
-        for await (const result of searchResults.results) {
-            console.log(`${JSON.stringify(result.document)}`);
-        }
-        console.log();
-        // Query 5
-        console.log('Query #5 - Lookup document:');
-        let documentResult = await searchClient.getDocument('3');
-        console.log(`HotelId: ${documentResult.HotelId}; HotelName: ${documentResult.HotelName}`);
-        console.log();
-    }
-    function sleep(ms) {
-        return new Promise(resolve => setTimeout(resolve, ms));
-    }
-    main().catch((err) => {
-        console.error("The sample encountered an error:", err);
-    });
-    ```
 
-1. Create a file named *hotels.json* and paste the following code into *hotels.json*:
-
-    ```json
-    {
-        "value": [
-            {
-                "HotelId": "1",
-                "HotelName": "Stay-Kay City Hotel",
-                "Description": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
-                "Category": "Boutique",
-                "Tags": ["view", "air conditioning", "concierge"],
-                "ParkingIncluded": false,
-                "LastRenovationDate": "2022-01-18T00:00:00Z",
-                "Rating": 3.6,
-                "Address": {
-                    "StreetAddress": "677 5th Ave",
-                    "City": "New York",
-                    "StateProvince": "NY",
-                    "PostalCode": "10022"
-                }
-            },
-            {
-                "HotelId": "2",
-                "HotelName": "Old Century Hotel",
-                "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
-                "Category": "Boutique",
-                "Tags": ["pool", "free wifi", "concierge"],
-                "ParkingIncluded": "false",
-                "LastRenovationDate": "2019-02-18T00:00:00Z",
-                "Rating": 3.6,
-                "Address": {
-                    "StreetAddress": "140 University Town Center Dr",
-                    "City": "Sarasota",
-                    "StateProvince": "FL",
-                    "PostalCode": "34243"
-                }
-            },
-            {
-                "HotelId": "3",
-                "HotelName": "Gastronomic Landscape Hotel",
-                "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
-                "Category": "Suite",
-                "Tags": ["restaurant", "bar", "continental breakfast"],
-                "ParkingIncluded": "true",
-                "LastRenovationDate": "2015-09-20T00:00:00Z",
-                "Rating": 4.8,
-                "Address": {
-                    "StreetAddress": "3393 Peachtree Rd",
-                    "City": "Atlanta",
-                    "StateProvince": "GA",
-                    "PostalCode": "30326"
-                }
-            },
-            {
-                "HotelId": "4",
-                "HotelName": "Sublime Palace Hotel",
-                "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.",
-                "Category": "Boutique",
-                "Tags": ["concierge", "view", "air conditioning"],
-                "ParkingIncluded": true,
-                "LastRenovationDate": "2020-02-06T00:00:00Z",
-                "Rating": 4.6,
-                "Address": {
-                    "StreetAddress": "7400 San Pedro Ave",
-                    "City": "San Antonio",
-                    "StateProvince": "TX",
-                    "PostalCode": "78216"
-                }
-            }
-        ]
-    }
-    ```
+## Understand the code
 
-1. Create a file named *hotels_quickstart_index.json* and paste the following code into *hotels_quickstart_index.json*:
-
-    ```json
-    {
-    	"name": "hotels-quickstart",
-    	"fields": [
-    		{
-    			"name": "HotelId",
-    			"type": "Edm.String",
-    			"key": true,
-    			"filterable": true
-    		},
-    		{
-    			"name": "HotelName",
-    			"type": "Edm.String",
-    			"searchable": true,
-    			"filterable": false,
-    			"sortable": true,
-    			"facetable": false
-    		},
-    		{
-    			"name": "Description",
-    			"type": "Edm.String",
-    			"searchable": true,
-    			"filterable": false,
-    			"sortable": false,
-    			"facetable": false,
-    			"analyzerName": "en.lucene"
-    		},
-    		{
-    			"name": "Category",
-    			"type": "Edm.String",
-    			"searchable": true,
-    			"filterable": true,
-    			"sortable": true,
-    			"facetable": true
-    		},
-    		{
-    			"name": "Tags",
-    			"type": "Collection(Edm.String)",
-    			"searchable": true,
-    			"filterable": true,
-    			"sortable": false,
-    			"facetable": true
-    		},
-    		{
-    			"name": "ParkingIncluded",
-    			"type": "Edm.Boolean",
-    			"filterable": true,
-    			"sortable": true,
-    			"facetable": true
-    		},
-    		{
-    			"name": "LastRenovationDate",
-    			"type": "Edm.DateTimeOffset",
-    			"filterable": true,
-    			"sortable": true,
-    			"facetable": true
-    		},
-    		{
-    			"name": "Rating",
-    			"type": "Edm.Double",
-    			"filterable": true,
-    			"sortable": true,
-    			"facetable": true
-    		},
-    		{
-    			"name": "Address",
-    			"type": "Edm.ComplexType",
-    			"fields": [
-    				{
-    					"name": "StreetAddress",
-    					"type": "Edm.String",
-    					"filterable": false,
-    					"sortable": false,
-    					"facetable": false,
-    					"searchable": true
-    				},
-    				{
-    					"name": "City",
-    					"type": "Edm.String",
-    					"searchable": true,
-    					"filterable": true,
-    					"sortable": true,
-    					"facetable": true
-    				},
-    				{
-    					"name": "StateProvince",
-    					"type": "Edm.String",
-    					"searchable": true,
-    					"filterable": true,
-    					"sortable": true,
-    					"facetable": true
-    				},
-    				{
-    					"name": "PostalCode",
-    					"type": "Edm.String",
-    					"searchable": true,
-    					"filterable": true,
-    					"sortable": true,
-    					"facetable": true
-    				},
-    				{
-    					"name": "Country",
-    					"type": "Edm.String",
-    					"searchable": true,
-    					"filterable": true,
-    					"sortable": true,
-    					"facetable": true
-    				}
-    			]
-    		}
-    	],
-    	"suggesters": [
-    		{
-    			"name": "sg",
-    			"searchMode": "analyzingInfixMatching",
-    			"sourceFields": [
-    				"HotelName"
-    			]
-    		}
-    	]
-    }
-    ```
+Now that you've run the code, let's break down the key steps:
 
-1. Sign in to Azure with the following command:
+1. [Create a search client](#create-a-search-client)
+1. [Create a search index](#create-a-search-index)
+1. [Upload documents to the index](#upload-documents-to-the-index)
+1. [Query the index](#query-the-index)
 
-    ```shell
-    az login
-    ```
+### Create a search client
 
-1. Run the JavaScript code with the following command:
+In `index.js`, you create two clients:
 
-    ```shell
-    node index.js
-    ```
+- [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient) creates the index.
+- [SearchClient](/javascript/api/@azure/search-documents/searchclient) loads and queries an existing index.
 
-## Explaining the code
+Both clients require the service endpoint and a credential for authentication. In this quickstart, you use [DefaultAzureCredential](/javascript/api/@azure/identity/defaultazurecredential) for keyless authentication with Microsoft Entra ID.
 
-### Create index
+```javascript
+const credential = new DefaultAzureCredential();
+const indexClient = new SearchIndexClient(endpoint, credential);
+```
 
-The *hotels_quickstart_index.json* file defines how Azure AI Search works with the documents you load in the next step. Each field is identified by a `name` and has a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
+### Create a search index
 
-With our index definition in place, we want to import *hotels_quickstart_index.json* at the top of *index.js* so the main function can access the index definition.
+This quickstart builds a hotels index that you load with hotel data and execute queries against. In this step, you import an index definition from a JSON file and create the index on your search service.
 
-```javascript
-const indexDefinition = require('./hotels_quickstart_index.json');
-```
+The `hotels_quickstart_index.json` file defines the index schema, including the fields and their attributes. Each field is identified by a `name` and has a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `Address`, are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create).
 
-Within the main function, we then create a `SearchIndexClient`, which is used to create and manage indexes for Azure AI Search. 
+The following code imports `hotels_quickstart_index.json` at the top of `index.js` so the main function can access the index definition.
 
 ```javascript
-const indexClient = new SearchIndexClient(endpoint, new AzureKeyCredential(apiKey));
+const indexDefinition = require('./hotels_quickstart_index.json');
 ```
 
-Next, we want to delete the index if it already exists. This operation is a common practice for test/demo code.
-
-We do this by defining a simple function that tries to delete the index.
+This quickstart deletes the index if it already exists, which is a common practice for test/demo code. The following function tries to delete the index.
 
 ```javascript
 async function deleteIndexIfExists(indexClient, indexName) {
@@ -563,7 +155,7 @@ async function deleteIndexIfExists(indexClient, indexName) {
 }
 ```
 
-To run the function, we extract the index name from the index definition and pass the `indexName` along with the `indexClient` to the `deleteIndexIfExists()` function.
+The following code extracts the index name from the index definition and passes the `indexName` along with the `indexClient` to the `deleteIndexIfExists()` function.
 
 ```javascript
 const indexName = indexDefinition["name"];
@@ -572,7 +164,7 @@ console.log('Checking if index exists...');
 await deleteIndexIfExists(indexClient, indexName);
 ```
 
-After that, we're ready to create the index with the `createIndex()` method.
+After that, you create the index with the `createIndex()` method.
 
 ```javascript
 console.log('Creating index...');
@@ -581,31 +173,25 @@ let index = await indexClient.createIndex(indexDefinition);
 console.log(`Index named ${index.name} has been created.`);
 ```
 
-### Load documents 
+### Upload documents to the index
 
-In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this case, we'll programmatically push the documents to the index.
+In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this quickstart, you programmatically push the documents to the index.
 
-Document inputs might be rows in a database, blobs in Blob storage, or, as in this sample, JSON documents on disk. Similar to what we did with the `indexDefinition`, we also need to import `hotels.json` at the top of *index.js* so that the data can be accessed in our main function.
+Document inputs might be rows in a database, blobs in Azure Blob Storage, or JSON documents on disk, as in this quickstart. Similar to the `indexDefinition`, you import `hotels.json` at the top of `index.js` so that the data can be accessed in the main function.
 
 ```javascript
 const hotelData = require('./hotels.json');
 ```
 
-To index data into the search index, we now need to create a `SearchClient`. While the `SearchIndexClient` is used to create and manage an index, the `SearchClient` is used to upload documents and query the index.
+To index data into the search index, you create a [SearchClient](/javascript/api/@azure/search-documents/searchclient). While `SearchIndexClient` creates and manages an index, `SearchClient` uploads documents and queries the index.
 
-There are two ways to create a `SearchClient`. The first option is to create a `SearchClient` from scratch:
-
-```javascript
- const searchClient = new SearchClient(endpoint, indexName, new AzureKeyCredential(apiKey));
-```
-
-Alternatively, you can use the `getSearchClient()` method of the `SearchIndexClient` to create the `SearchClient`:
+This quickstart obtains `SearchClient` from `SearchIndexClient` using [getSearchClient](/javascript/api/@azure/search-documents/searchindexclient#@azure-search-documents-searchindexclient-getsearchclient), which reuses the same credentials.
 
 ```javascript
 const searchClient = indexClient.getSearchClient(indexName);
 ```
 
-Now that the client is defined, upload the documents into the search index. In this case, we use the `mergeOrUploadDocuments()` method, which uploads the documents or merges them with an existing document if a document with the same key already exists.
+The following code uploads the documents into the search index using the `mergeOrUploadDocuments()` method, which uploads the documents or merges them with an existing document if a document with the same key already exists.
 
 ```javascript
 console.log('Uploading documents...');
@@ -614,17 +200,17 @@ let indexDocumentsResult = await searchClient.mergeOrUploadDocuments(hotelData['
 console.log(`Index operations succeeded: ${JSON.stringify(indexDocumentsResult.results[0].succeeded)}`);
 ```
 
-### Search an index
+### Query the index
 
-With an index created and documents uploaded, you're ready to send queries to the index. In this section, we send five different queries to the search index to demonstrate different pieces of query functionality available to you.
+With an index created and documents uploaded, you're ready to send queries to the index. This section sends five different queries to the search index to demonstrate different pieces of query functionality available to you.
 
-The queries are written in a `sendQueries()` function that we call in the main function as follows:
+The queries are written in a `sendQueries()` function called in the main function as follows:
 
 ```javascript
 await sendQueries(searchClient);
 ```
 
-Queries are sent using the `search()` method of `searchClient`. The first parameter is the search text and the second parameter specifies search options.
+The `search()` method of `searchClient` sends queries. The first parameter is the search text and the second parameter specifies search options.
 
 #### Query example 1
 
@@ -654,7 +240,7 @@ The remaining queries outlined below should also be added to the `sendQueries()`
 
 #### Query example 2
 
-In the next query, we specify the search term `"wifi"` and also include a filter to only return results where the state is equal to `'FL'`. Results are also ordered by the Hotel's `Rating`.
+The next query specifies the search term `"wifi"` and includes a filter to only return results where the state is equal to `'FL'`. Results are also ordered by the Hotel's `Rating`. A filter is a boolean expression evaluated over filterable fields in an index. Filter queries either include or exclude values. As such, there's no relevance score associated with a filter query.
 
 ```javascript
 console.log('Query #2 - Search with filter, orderBy, and select:');
@@ -673,7 +259,7 @@ for await (const result of searchResults.results) {
 
 #### Query example 3
 
-Next, the search is limited to a single searchable field using the `searchFields` parameter. This approach is a great option to make your query more efficient if you know you're only interested in matches in certain fields. 
+The third query limits the search to a single searchable field using the `searchFields` parameter. This approach is a great option to make your query more efficient if you know you're only interested in matches in certain fields.
 
 ```javascript
 console.log('Query #3 - Limit searchFields:');
@@ -682,20 +268,18 @@ searchOptions = {
     searchFields: ["HotelName"]
 };
 
-searchResults = await searchClient.search("Sublime Palace", searchOptions);
+searchResults = await searchClient.search("sublime cliff", searchOptions);
 for await (const result of searchResults.results) {
     console.log(`${JSON.stringify(result.document)}`);
 }
-console.log();
 ```
 
-
 #### Query example 4
 
-Another common option to include in a query is `facets`. Facets allow you to build out filters on your UI to make it easy for users to know what values they can filter down to.
+Another common option to include in a query is `facets`. Facets allow you to build out filters on your UI to make it easy for users to know what values they can filter down to. This query also limits the search to the `HotelName` field.
 
 ```javascript
-console.log('Query #4 - Use facets:');
+console.log('Query #4 - limit searchFields and use facets:');
 searchOptions = {
     facets: ["Category"],
     select: ["HotelId", "HotelName", "Rating"],
@@ -710,7 +294,7 @@ for await (const result of searchResults.results) {
 
 #### Query example 5
 
-The final query uses the `getDocument()` method of the `searchClient`. This allows you to efficiently retrieve a document by its key. 
+The final query uses the `getDocument()` method of the `searchClient`. This allows you to efficiently retrieve a document by its key.
 
 ```javascript
 console.log('Query #5 - Lookup document:');
@@ -720,6 +304,6 @@ console.log(`HotelId: ${documentResult.HotelId}; HotelName: ${documentResult.Hot
 
 #### Summary of queries
 
-The previous queries show multiple ways of matching terms in a query: full-text search, filters, and autocomplete.
+The previous queries show multiple ways of matching terms in a query: full-text search, filters, and document lookup.
 
-Full text search and filters are performed using the `searchClient.search` method. A search query can be passed in the `searchText` string, while a filter expression can be passed in the `filter` property of the `SearchOptions` class. To filter without searching, just pass "*" for the `searchText` parameter of the `search` method. To search without filtering, leave the `filter` property unset, or don't pass in a `SearchOptions` instance at all.
+The `searchClient.search` method performs full-text search and filters. You can pass a search query in the `searchText` string, while you pass a filter expression in the `filter` property of the `SearchOptions` class. To filter without searching, just pass `"*"` for the `searchText` parameter of the `search` method. To search without filtering, leave the `filter` property unset, or don't pass in a `SearchOptions` instance at all.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "フルテキスト検索に関するJavaScriptクイックスタートの大幅な更新"
}
```

### Explanation
このコードの差分は、`full-text-javascript.md` ファイルに対する大規模な変更を示しています。106行の新規追加が行われ、522行が削除されるなど、628行の変更があります。この変更の目的は、JavaScriptを使用したフルテキスト検索のクイックスタートガイドを刷新し、より効果的に学ぶためのリソースを提供することです。

新しい内容では、Azure AI SearchのJavaScriptクライアントライブラリを活用して、検索インデックスの作成、データのロード、およびクエリ実行のステップが整理されています。特に、Apache Luceneに基づく全文検索と、BM25ランキングアルゴリズムについての簡潔な説明が追加され、ユーザーがこの機能を効果的に利用できるようになっています。加えて、サンプルデータの具体的な利用方法やGitHubからのソースコードのダウンロード手順がクリアに示されています。

変更点には、環境設定の手順も含まれており、Node.jsの最新LTS版利用や、Visual Studio Code、Gitのインストールが求められています。従来の手順が整理され、効率的な開発体験を提供するために構造が改善されていることが強調されています。

さらに、コードの実行手順が明確に示され、クエリ結果の例が豊富に提示されることで、ユーザーは実際のデータを用いてどのように検索が行われるかを具体的に理解できるよう工夫されています。全体として、これにより、JavaScriptを使用したAzure AI Searchのフルテキスト検索がよりアクセスしやすく、実用的なリソースとなっています。

## articles/search/includes/quickstarts/full-text-powershell.md{#item-1b28d3}

<details>
<summary>Diff</summary>
````diff
@@ -4,360 +4,237 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 06/30/2025
+ms.date: 02/02/2026
 ---
 
-In this quickstart, you use PowerShell and the [Azure AI Search REST APIs](/rest/api/searchservice/) to create, load, and query a search index for [full-text search](../../search-lucene-query-architecture.md). Full-text search uses Apache Lucene for indexing and queries and the BM25 ranking algorithm for scoring results.
+In this quickstart, you use PowerShell and the [Azure AI Search REST APIs](/rest/api/searchservice/) to create, load, and query a search index for [full-text search](../../search-lucene-query-architecture.md), also known as keyword search.
 
-This quickstart uses fictional hotel data from the [azure-search-sample-data](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/hotels/hotel-json-documents) repo to populate the index.
+Full-text search uses Apache Lucene for indexing and queries and the BM25 ranking algorithm for scoring results. This quickstart uses fictional hotel data from the [azure-search-sample-data](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/hotels/hotel-json-documents) GitHub repository to populate the index.
 
 > [!TIP]
-> You can download the [source code](https://github.com/Azure-Samples/azure-search-powershell-samples/tree/main/Quickstart) to start with a finished project or follow these steps to create your own.
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-powershell-samples/tree/main/Quickstart) on GitHub.
 
 ## Prerequisites
 
-+ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An Azure AI Search service. [Create a service](../../search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription. For this quickstart, you can use a free service.
+- An [Azure AI Search service](../../search-create-service-portal.md). You can use a free service for this quickstart.
 
-+ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
+- The latest version of [PowerShell](https://github.com/PowerShell/PowerShell).
 
-+ [PowerShell 7.3](https://github.com/PowerShell/PowerShell) or later. This quickstart uses [Invoke-RestMethod](/powershell/module/Microsoft.PowerShell.Utility/Invoke-RestMethod) to make REST API calls.
+- [Git](https://git-scm.com/downloads) to clone the sample repository.
 
-## Configure access
-
-You can connect to your Azure AI Search service using API keys or Microsoft Entra ID with role assignments. Keys are easier to start with, but roles are more secure.
-
-To configure the recommended role-based access:
-
-1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
-
-1. From the left pane, select **Settings** > **Keys**.
-
-1. Under **API Access control**, select **Both**.
-
-   This option enables both key-based and keyless authentication. After you assign roles, you can return to this step and select **Role-based access control**.
+- The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-1. From the left pane, select **Access control (IAM)**.
-
-1. Select **Add** > **Add role assignment**.
-
-1. Assign the **Search Service Contributor** and **Search Index Data Contributor** roles to your user account.
+## Configure access
 
-For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
+[!INCLUDE [resource authentication](../resource-authentication.md)]
 
 ## Get endpoint
 
-In the next section, you specify the following endpoint to establish a connection to your Azure AI Search service. These steps assume that you [configured role-based access](#configure-access).
-
-To get your service endpoint:
-
-1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
-
-1. From the left pane, select **Overview**.
-
-1. Make a note of the URL, which should be similar to `https://my-service.search.windows.net`.
+[!INCLUDE [resource endpoint](../resource-endpoint.md)]
 
-## Connect to Azure AI Search
+## Set up the environment
 
-Before you can make REST API calls to your Azure AI Search service, you must authenticate and connect to the service. You perform the following steps in PowerShell, which supports the Azure CLI commands used in steps two and three.
+1. Use Git to clone the sample repository.
 
-To connect to your search service:
+   ```powershell
+   git clone https://github.com/Azure-Samples/azure-search-powershell-samples
+   ```
 
-1. On your local system, open PowerShell.
+1. Navigate to the `Quickstart` folder.
 
-1. Sign in to your Azure subscription. If you have multiple subscriptions, select the one that contains your search service.
+   ```powershell
+   cd azure-search-powershell-samples/Quickstart
+   ```
 
-    ```azurecli
-    az login
-    ```
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service.
 
-1. Create a `$token` object to store your access token.
+   ```azurecli
+   az login
+   ```
 
-    ```azurecli
-    $token = az account get-access-token --resource https://search.azure.com/ --query accessToken --output tsv
-    ```
+1. Open the `azure-search-powershell-samples/Quickstart/azure-search-quickstart.ps1` file in a text editor.
 
-1. Create a `$headers` object to store your token and content type.
+1. Replace the placeholder value for `$baseUrl` with the URL you obtained in [Get endpoint](#get-endpoint).
 
-    ```powershell
-    $headers = @{
-    'Authorization' = "Bearer $token"
-    'Content-Type' = 'application/json' 
-    'Accept' = 'application/json' }
-    ```
+## Run the code
 
-    You only need to set the header once per session, but you must add it to each request.
+In the same terminal, run the following PowerShell script to execute this quickstart.
 
-1. Create a `$url` object that targets the indexes collection on your search service. Replace `<YOUR-SEARCH-SERVICE>` with the value you obtained in [Get endpoint](#get-endpoint).
-
-    ```powershell
-    $url = "<YOUR-SEARCH-SERVICE>/indexes?api-version=2025-09-01&`$select=name"
-    ```
-
-1. Run `Invoke-RestMethod` to send a GET request to your search service. Include `ConvertTo-Json` to view responses from the service.
+```powershell
+.\azure-search-quickstart.ps1
+```
 
-    ```powershell
-    Invoke-RestMethod -Uri $url -Headers $headers | ConvertTo-Json
-    ```
+### Output
 
-   If your service is empty and has no indexes, the response is similar to the following example. Otherwise, you see a JSON representation of index definitions.
+The script deletes any existing index, creates a new index, uploads documents, and runs multiple full-text search queries. The output shows the full HTTP requests and responses for each operation. The following example shows the response when searching for "restaurant wifi".
 
-    ```json
+```json
+{
+  "value": [
     {
-        "@odata.context":  "https://my-service.search.windows.net/$metadata#indexes",
-        "value":  [
-
-                  ]
+      "@search.score": 0.6931472,
+      "HotelName": "Old Century Hotel",
+      "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
+      "Tags": ["pool", "free wifi", "concierge"]
+    },
+    {
+      "@search.score": 0.5575875,
+      "HotelName": "Gastronomic Landscape Hotel",
+      "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel's restaurant services.",
+      "Tags": ["restaurant", "bar", "continental breakfast"]
     }
-    ```
-
-## Create a search index
-
-Before you add content to Azure AI Search, you must create an index to define how the content is stored and structured. An index is conceptually similar to a table in a relational database, but it's specifically designed for search operations, such as full-text search.
-
-Run the following commands in the same PowerShell session you started in the previous section.
+  ]
+}
+```
 
-To create an index:
+## Understand the code
 
-1. Create a `$body` object to define the index schema.
+Now that you've run the code, let's break down the key steps:
 
-    ```powershell
-    $body = @"
-    {
-        "name": "hotels-quickstart",  
-        "fields": [
-            {"name": "HotelId", "type": "Edm.String", "key": true, "filterable": true},
-            {"name": "HotelName", "type": "Edm.String", "searchable": true, "filterable": false, "sortable": true, "facetable": false},
-            {"name": "Description", "type": "Edm.String", "searchable": true, "filterable": false, "sortable": false, "facetable": false, "analyzer": "en.lucene"},
-            {"name": "Category", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true},
-            {"name": "Tags", "type": "Collection(Edm.String)", "searchable": true, "filterable": true, "sortable": false, "facetable": true},
-            {"name": "ParkingIncluded", "type": "Edm.Boolean", "filterable": true, "sortable": true, "facetable": true},
-            {"name": "LastRenovationDate", "type": "Edm.DateTimeOffset", "filterable": true, "sortable": true, "facetable": true},
-            {"name": "Rating", "type": "Edm.Double", "filterable": true, "sortable": true, "facetable": true},
-            {"name": "Address", "type": "Edm.ComplexType", 
-                "fields": [
-                {"name": "StreetAddress", "type": "Edm.String", "filterable": false, "sortable": false, "facetable": false, "searchable": true},
-                {"name": "City", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true},
-                {"name": "StateProvince", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true},
-                {"name": "PostalCode", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true},
-                {"name": "Country", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true}
-            ]
-         }
-      ]
-    }
-    "@
-    ```
+1. [Create a search index](#create-a-search-index)
+1. [Upload documents to the index](#upload-documents-to-the-index)
+1. [Query the index](#query-the-index)
 
-2. Update the `$url` object to target the new index. Replace `<YOUR-SEARCH-SERVICE>` with the value you obtained in [Get endpoint](#get-endpoint).
+### Create a search index
 
-    ```powershell
-    $url = "<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart?api-version=2025-09-01"
-    ```
-
-3. Run `Invoke-RestMethod` to create the index on your search service.
+Before you add content to Azure AI Search, you must create an index to define how the content is stored and structured. An index is conceptually similar to a table in a relational database, but it's specifically designed for search operations, such as full-text search.
 
-    ```powershell
-    Invoke-RestMethod -Uri $url -Headers $headers -Method Put -Body $body | ConvertTo-Json
-    ```
+This quickstart first deletes any existing index with the same name, which is a common practice for test/demo code that runs repeatedly.
 
-    The response should contain the JSON representation of the index schema.
+```powershell
+Send-Request DELETE "$baseUrl/indexes/hotels-quickstart?api-version=2025-09-01" $headers
+```
 
-### About the create index request
+This quickstart then calls [Indexes - Create (REST API)](/rest/api/searchservice/indexes/create) to build a search index named `hotels-quickstart` and its physical data structures on your search service.
 
-This quickstart calls [Indexes - Create (REST API)](/rest/api/searchservice/indexes/create) to build a search index named `hotels-quickstart` and its physical data structures on your search service.
+```powershell
+$body = @"
+{
+    "name": "hotels-quickstart",
+    "fields": [
+        {"name": "HotelId", "type": "Edm.String", "key": true, "filterable": true},
+        {"name": "HotelName", "type": "Edm.String", "searchable": true, "filterable": false, "sortable": true, "facetable": false},
+        {"name": "Description", "type": "Edm.String", "searchable": true, "filterable": false, "sortable": false, "facetable": false, "analyzer": "en.lucene"},
+        ...
+    ]
+}
+"@
+
+Send-RequestWithBody POST "$baseUrl/indexes?api-version=2025-09-01" $headers $body
+```
 
 Within the index schema, the `fields` collection defines the structure of hotel documents. Each field has a `name`, data `type`, and attributes that determine its behavior during indexing and queries. The `HotelId` field is marked as the key, which Azure AI Search requires to uniquely identify each document in an index.
 
 Key points about the index schema:
 
 + Use string fields (`Edm.String`) to make numeric data full-text searchable. Other [supported data types](/rest/api/searchservice/supported-data-types), such as `Edm.Int32`, are filterable, sortable, facetable, and retrievable but aren't searchable.
 
-+ Most of our fields are simple data types, but you can define complex types to represent nested data, such as the `Address` field.
++ Most of the fields are simple data types, but you can define complex types to represent nested data, such as the `Address` field.
 
 + Field attributes determine allowed actions. The REST APIs allow [many actions by default](/rest/api/searchservice/indexes/create#request-body). For example, all strings are searchable and retrievable. With the REST APIs, you might only use attributes if you need to disable a behavior.
 
-## Load the index
+### Upload documents to the index
 
 Newly created indexes are empty. To populate an index and make it searchable, you must upload JSON documents that conform to the index schema.
 
 In Azure AI Search, documents serve as both inputs for indexing and outputs for queries. For simplicity, this quickstart provides sample hotel documents as inline JSON. In production scenarios, however, content is often pulled from connected data sources and transformed into JSON using [indexers](../../search-indexer-overview.md).
 
-To upload documents to your index:
-
-1. Create a `$body` object to store the JSON payload of four sample documents.
+This quickstart calls [Documents - Index (REST API)](/rest/api/searchservice/documents/) to add four sample hotel documents to your index. Compared to the previous request, the URI is extended to include the `docs` collection and `index` operation.
 
-    ```powershell
-    $body = @"
+```powershell
+$body = @"
+{
+    "value": [
         {
-            "value": [
-            {
             "@search.action": "upload",
             "HotelId": "1",
             "HotelName": "Stay-Kay City Hotel",
-            "Description": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
-            "Category": "Boutique",
-            "Tags": [ "view", "air conditioning", "concierge" ],
-            "ParkingIncluded": false,
-            "LastRenovationDate": "2022-01-18T00:00:00Z",
-            "Rating": 3.60,
-            "Address": 
-                {
-                "StreetAddress": "677 5th Ave",
-                "City": "New York",
-                "StateProvince": "NY",
-                "PostalCode": "10022",
-                "Country": "USA"
-                } 
-            },
-            {
-            "@search.action": "upload",
-            "HotelId": "2",
-            "HotelName": "Old Century Hotel",
-            "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
-            "Category": "Boutique",
-            "Tags": [ "pool", "free wifi", "concierge" ],
-            "ParkingIncluded": false,
-            "LastRenovationDate": "2019-02-18T00:00:00Z",
-            "Rating": 3.60,
-            "Address": 
-                {
-                "StreetAddress": "140 University Town Center Dr",
-                "City": "Sarasota",
-                "StateProvince": "FL",
-                "PostalCode": "34243",
-                "Country": "USA"
-                } 
-            },
-            {
-            "@search.action": "upload",
-            "HotelId": "3",
-            "HotelName": "Gastronomic Landscape Hotel",
-            "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
-            "Category": "Suite",
-            "Tags": [ "restaurant", "bar", "continental breakfast" ],
-            "ParkingIncluded": true,
-            "LastRenovationDate": "2015-09-20T00:00:00Z",
-            "Rating": 4.80,
-            "Address": 
-                {
-                "StreetAddress": "3393 Peachtree Rd",
-                "City": "Atlanta",
-                "StateProvince": "GA",
-                "PostalCode": "30326",
-                "Country": "USA"
-                } 
-            },
-            {
-            "@search.action": "upload",
-            "HotelId": "4",
-            "HotelName": "Sublime Palace Hotel",
-            "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.",
-            "Category": "Boutique",
-            "Tags": [ "concierge", "view", "air conditioning" ],
-            "ParkingIncluded": true,
-            "LastRenovationDate": "2020-02-06T00:00:00Z",
-            "Rating": 4.60,
-            "Address": 
-                {
-                "StreetAddress": "7400 San Pedro Ave",
-                "City": "San Antonio",
-                "StateProvince": "TX",
-                "PostalCode": "78216",
-                "Country": "USA"
-                }
-            }
-          ]
-        }
-    "@
-    ```
-
-2. Update the `$url` object to target the indexing endpoint. Replace `<YOUR-SEARCH-SERVICE>` with the value you obtained in [Get endpoint](#get-endpoint).
-
-    ```powershell
-    $url = "<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs/index?api-version=2025-09-01"
-    ```
-
-3. Run `Invoke-RestMethod` to send the upload request to your search service.
-
-    ```powershell
-    Invoke-RestMethod -Uri $url -Headers $headers -Method Post -Body $body | ConvertTo-Json
-    ```
-
-    The response should contain the key and status of each uploaded document.
-
-### About the upload request
-
-This quickstart calls [Documents - Index (REST API)](/rest/api/searchservice/documents/) to add four sample hotel documents to your index. Compared to the previous request, the URI is extended to include the `docs` collection and `index` operation.
+            "Description": "This classic hotel is...",
+            ...
+        },
+        ...
+    ]
+}
+"@
+
+Send-RequestWithBody POST "$baseUrl/indexes/hotels-quickstart/docs/index?api-version=2025-09-01" $headers $body
+```
 
-Each document in the `value` array represents a hotel and contains fields that match the index schema. The `@search.action` parameter specifies the operation to perform for each document. Our example uses `upload`, which adds the document if it doesn't exist or updates the document if it does exist.
+Each document in the `value` array represents a hotel and contains fields that match the index schema. The `@search.action` parameter specifies the operation to perform for each document. This example uses `upload`, which adds the document if it doesn't exist or updates the document if it does exist.
 
-## Query the index
+### Query the index
 
 Now that documents are loaded into your index, you can use full-text search to find specific terms or phrases within their fields.
 
-To run a full-text query against your index:
+This quickstart calls [Documents - Search Post (REST API)](/rest/api/searchservice/documents/search-post) to find hotel documents that match your search criteria. The URI targets the `/docs/search` operation.
 
-1. Update the `$url` object to specify search parameters. Replace `<YOUR-SEARCH-SERVICE>` with the value you obtained in [Get endpoint](#get-endpoint).
+Full-text search requests include a `search` parameter with the query text, which can contain terms, phrases, or operators. The query searches across all searchable fields in each document. The following examples demonstrate common query patterns.
 
-    ```powershell
-    $url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2025-09-01&search=attached restaurant&searchFields=Description,Tags&$select=HotelId,HotelName,Tags,Description&$count=true'
-    ```
+#### Query example 1
 
-2. Run `Invoke-RestMethod` to send the query request to your search service.
+The following query searches for the terms "restaurant wifi" across all searchable fields. By default, Azure AI Search returns documents that match any of the search terms.
 
-    ```powershell
-    Invoke-RestMethod -Uri $url -Headers $headers | ConvertTo-Json
-    ```
+```powershell
+$body = @"
+{
+    "search": "restaurant wifi",
+    "select": "HotelName, Description, Tags"
+}
+"@
+
+Send-RequestWithBody POST "$baseUrl/indexes/hotels-quickstart/docs/search?api-version=2025-09-01" $headers $body
+```
 
-    The response should be similar to the following example, which shows one matching hotel document, its relevance score, and its selected fields.
+The `select` parameter limits the fields returned in the response to `HotelName`, `Description`, and `Tags`.
 
-    ```json
-    {
-      "@odata.context": "https://my-service.search.windows.net/indexes('hotels-quickstart')/$metadata#docs(*)",
-      "@odata.count": 1,
-      "value": [
-        {
-          "@search.score": 0.5575875,
-          "HotelId": "3",
-          "HotelName": "Gastronomic Landscape Hotel",
-          "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel's restaurant services.",
-          "Tags": "restaurant bar continental breakfast"
-        }
-      ]
-    }
-    ```
+#### Query example 2
 
-### About the query request
+The following query uses a `filter` expression to return only hotels with a rating greater than 4.
 
-This quickstart calls [Documents - Search Post (REST API)](/rest/api/searchservice/documents/search-post) to find hotel documents that match your search criteria. The URI still targets the `docs` collection but no longer includes the `index` operation.
+```powershell
+$body = @"
+{
+    "search": "*",
+    "filter": "Rating gt 4",
+    "select": "HotelName,Rating"
+}
+"@
+
+Send-RequestWithBody POST "$baseUrl/indexes/hotels-quickstart/docs/search?api-version=2025-09-01" $headers $body
+```
+
+The `search` parameter is set to `*`, which matches all documents. The `filter` parameter applies a Boolean condition to narrow the results.
 
-Full-text search requests always include a `search` parameter that contains the query text. The query text can include one or more terms, phrases, or operators. In addition to `search`, you can specify other parameters to refine the search behavior and results.
+#### Query example 3
 
-Our query searches for the terms "attached restaurant" in the `Description` and `Tags` fields of each hotel document. The `$select` parameter limits the fields returned in the response to `HotelId`, `HotelName`, `Tags`, and `Description`. The `$count` parameter requests the total number of matching documents.
+The following query searches for "boutique" and uses `top` to return only the first two results.
+
+```powershell
+$body = @"
+{
+    "search": "boutique",
+    "select": "HotelName,Category",
+    "top": 2
+}
+"@
+
+Send-RequestWithBody POST "$baseUrl/indexes/hotels-quickstart/docs/search?api-version=2025-09-01" $headers $body
+```
 
-#### Other query examples
+#### Query example 4
 
-Run the following commands to explore the query syntax. You can perform string searches, use `$filter` expressions, limit result sets, select specific fields, and more. Remember to replace `<YOUR-SEARCH-SERVICE>` with the value you obtained in [Get endpoint](#get-endpoint).
+The following query searches for "pool" and uses `orderby` to sort results by `Rating` in descending order.
 
 ```powershell
-# Query example 1
-# Search the index for the terms 'restaurant' and 'wifi'
-# Return only the HotelName, Description, and Tags fields
-$url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2025-09-01&search=restaurant wifi&$count=true&$select=HotelName,Description,Tags'
-
-# Query example 2 
-# Use a filter to find hotels rated 4 or higher
-# Return only the HotelName and Rating fields
-$url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2025-09-01&search=*&$filter=Rating gt 4&$select=HotelName,Rating'
-
-# Query example 3
-# Take the top two results
-# Return only the HotelName and Category fields
-$url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2025-09-01&search=boutique&$top=2&$select=HotelName,Category'
-
-# Query example 4
-# Sort by a specific field (Address/City) in ascending order
-# Return only the HotelName, Address/City, Tags, and Rating fields
-$url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2025-09-01&search=pool&$orderby=Address/City asc&$select=HotelName, Address/City, Tags, Rating'
+$body = @"
+{
+    "search": "pool",
+    "select": "HotelName,Description,Tags,Rating",
+    "orderby": "Rating desc"
+}
+"@
+
+Send-RequestWithBody POST "$baseUrl/indexes/hotels-quickstart/docs/search?api-version=2025-09-01" $headers $body
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PowerShellを用いたフルテキスト検索のクイックスタートガイドの改訂"
}
```

### Explanation
このコードの差分は、`full-text-powershell.md` ファイルに対する重要な変更を示しています。151行の新規追加と274行の削除が行われ、全体で425行の変更がありました。この変更の目標は、PowerShellを使用してフルテキスト検索を行うためのクイックスタートガイドを最新の情報に基づいて改善することです。

新しい内容では、Azure AI Search REST APIを使ったインデックスの作成、データのロード、クエリの実行手順がより明確にしています。特に、全文検索がApache Luceneを利用していることやBM25ランキングアルゴリズムの使用に関する説明が強調されています。また、サンプルデータのURLやスクリプトの使用方法が改善され、ユーザーが迅速に始められるよう配慮されています。

また、インストール手順や前提条件に関する説明が整理され、PowerShellの最新バージョンの利用やGitによるリポジトリのクローンに関する情報が明示されています。こうした情報は、ユーザーが必要な環境を簡単に設定できるようにするために重要です。さらに、出力結果として得られるJSONの例がより具体的に示され、実際にどのように検索結果が得られるのか理解しやすくなっています。

全体として、これによりPowerShellを使用したAzure AI Searchのフルテキスト検索ガイドは、ユーザーフレンドリーに改善されており、より多くの情報が適切に提供されています。

## articles/search/includes/quickstarts/full-text-python.md{#item-9bba1c}

<details>
<summary>Diff</summary>
````diff
@@ -4,166 +4,277 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 02/02/2026
 ---
 
-[!INCLUDE [Full text introduction](full-text-intro.md)]
+In this quickstart, you use the [Azure AI Search client library for Python](/python/api/overview/azure/search-documents-readme) to create, load, and query a search index for [full-text search](../../search-lucene-query-architecture.md), also known as keyword search.
+
+Full-text search uses Apache Lucene for indexing and queries and the BM25 ranking algorithm for scoring results. This quickstart uses fictional hotel data from the [azure-search-sample-data](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/hotels/hotel-json-documents) GitHub repository to populate the index.
 
 > [!TIP]
-> You can download the [source code](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Keyword-Search) to start with a finished project or follow these steps to create your own.
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Keyword-Search) on GitHub.
 
 ## Prerequisites
 
 - An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. For this quickstart, you can use a free service.
-
-- [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) or an equivalent IDE with Python 3.10 or later. If you haven't installed a suitable version of Python, follow the instructions in the [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter).
+- An [Azure AI Search service](../../search-create-service-portal.md). You can use a free service for this quickstart.
 
-## Microsoft Entra ID prerequisites
+- The latest version of [Python](https://www.python.org/downloads/).
 
-For the recommended keyless authentication with Microsoft Entra ID, you must:
+- [Visual Studio Code](https://code.visualstudio.com/download) with the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions.
 
-- Install the [Azure CLI](/cli/azure/install-azure-cli).
+- [Git](https://git-scm.com/downloads) to clone the sample repository.
 
-- Assign the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
+- The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-## Get service information
+## Configure access
 
 [!INCLUDE [resource authentication](../resource-authentication.md)]
 
-## Set up your environment
+## Get endpoint
 
-You run the sample code in a Jupyter notebook. So, you need to set up your environment to run Jupyter notebooks.
+[!INCLUDE [resource endpoint](../resource-endpoint.md)]
 
-1. Download or copy the [sample notebook from GitHub](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Keyword-Search).
+## Set up the environment
 
-1. Open the notebook in Visual Studio Code.
+1. Use Git to clone the sample repository.
 
-1. Create a new Python environment to use to install the packages you need for this tutorial. 
+   ```console
+   git clone https://github.com/Azure-Samples/azure-search-python-samples
+   ```
 
-    > [!IMPORTANT]
-    > Don't install packages into your global python installation. You should always use a virtual or conda environment when installing python packages, otherwise you can break your global install of Python.
+1. Open the `azure-search-python-samples/Quickstart-Keyword-Search` folder in Visual Studio Code.
 
-    # [Windows](#tab/windows)
-    
-    ```bash
-    py -3 -m venv .venv
-    .venv\scripts\activate
-    ```
-    
-    # [Linux](#tab/linux)
-    
-    ```bash
-    python3 -m venv .venv
-    source .venv/bin/activate
-    ```
-    
-    # [macOS](#tab/macos)
-    
-    ```bash
-    python3 -m venv .venv
-    source .venv/bin/activate
-    ```
-    
-    ---
+1. Open the `azure-search-quickstart.ipynb` file.
 
-    It can take a minute to set up. If you run into problems, see [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments).
+1. In the upper-right corner of the notebook, select **Select Kernel** > **Python Environments...** > **Create Python Environment**, and then follow the prompts to create a virtual environment.
 
-1. Install Jupyter notebooks and the IPython Kernel for Jupyter notebooks if you don't have them already.
+1. Run the first code cell to install the required packages.
 
-    ```bash
-    pip install jupyter
-    pip install ipykernel
-    python -m ipykernel install --user --name=.venv
-    ```
+1. In the second code cell, replace the placeholder value for `search_endpoint` with the URL you obtained in [Get endpoint](#get-endpoint), and then run the cell.
 
-1. Select the notebook kernel.
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service.
 
-    1. In the top right corner of the notebook, select **Select Kernel**.
-    1. If you see `.venv` in the list, select it. If you don't see it, select **Select Another Kernel** > **Python environments** > `.venv`.
-
-## Create, load, and query a search index
-
-In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [Explaining the code](#explaining-the-code) section.
-
-1. Make sure the notebook is open in the `.venv` kernel as described in the previous section.
-1. Run the first code cell to install the required packages, including [azure-search-documents](/python/api/azure-search-documents). 
-
-    ```python
-    ! pip install azure-search-documents==11.6.0b1 --quiet
-    ! pip install azure-identity --quiet
-    ! pip install python-dotenv --quiet
+    ```azurecli
+    az login
     ```
 
-1. Replace contents of the second code cell with the following code depending on your authentication method. 
-
-    > [!NOTE]
-    > The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
+## Run the code
 
-    #### [Microsoft Entra ID](#tab/keyless)
-    
-    ```python
-    from azure.core.credentials import AzureKeyCredential
-    from azure.identity import DefaultAzureCredential, AzureAuthorityHosts
-    
-    search_endpoint: str = "https://<Put your search service NAME here>.search.windows.net/"
-    authority = AzureAuthorityHosts.AZURE_PUBLIC_CLOUD
-    credential = DefaultAzureCredential(authority=authority)
+Run the remaining code cells sequentially to create an index, upload documents, and query the index.
+
+### Output
+
+Each code cell prints its output to the notebook. The following example is the output of the first query, an empty search that returns all documents in the index.
+
+```
+Total Documents Matching Query: 4
+1.0
+Gastronomic Landscape Hotel
+['restaurant', 'bar', 'continental breakfast']
+Description: The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.
+1.0
+Old Century Hotel
+['pool', 'free wifi', 'concierge']
+Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
+1.0
+Sublime Palace Hotel
+['concierge', 'view', 'air conditioning']
+Description: Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.
+1.0
+Stay-Kay City Hotel
+['view', 'air conditioning', 'concierge']
+Description: This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.
+```
+
+## Understand the code
+
+Now that you've run the code, let's break down the key steps:
+
+1. [Create the clients](#create-the-clients)
+1. [Create a search index](#create-a-search-index)
+1. [Upload documents to the index](#upload-documents-to-the-index)
+1. [Query the index](#query-the-index)
+1. [Remove the index](#remove-the-index)
+
+### Create the clients
+
+The notebook creates two clients:
+
+- [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient) creates and manages indexes.
+- [SearchClient](/python/api/azure-search-documents/azure.search.documents.searchclient) loads documents and runs queries.
+
+Both clients require the service endpoint and a credential. In this quickstart, you use [DefaultAzureCredential](/python/api/azure-identity/azure.identity.defaultazurecredential) for keyless authentication with Microsoft Entra ID.
+
+### Create a search index
+
+This quickstart builds a hotels index that you load with hotel data and run queries against. In this step, you define the fields in the index. Each field definition includes a name, data type, and attributes that determine how the field is used.
+
+The notebook uses `SimpleField`, `SearchableField`, and `ComplexField` from the [models package](/python/api/azure-search-documents/azure.search.documents.indexes.models) to define the schema. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create).
+
+```python
+# Create a search schema
+index_client = SearchIndexClient(
+    endpoint=search_endpoint, credential=credential)
+fields = [
+        SimpleField(name="HotelId", type=SearchFieldDataType.String, key=True),
+        SearchableField(name="HotelName", type=SearchFieldDataType.String, sortable=True),
+        SearchableField(name="Description", type=SearchFieldDataType.String, analyzer_name="en.lucene"),
+        SearchableField(name="Category", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
+
+        SearchableField(name="Tags", collection=True, type=SearchFieldDataType.String, facetable=True, filterable=True),
+
+        SimpleField(name="ParkingIncluded", type=SearchFieldDataType.Boolean, facetable=True, filterable=True, sortable=True),
+        SimpleField(name="LastRenovationDate", type=SearchFieldDataType.DateTimeOffset, facetable=True, filterable=True, sortable=True),
+        SimpleField(name="Rating", type=SearchFieldDataType.Double, facetable=True, filterable=True, sortable=True),
+
+        ComplexField(name="Address", fields=[
+            SearchableField(name="StreetAddress", type=SearchFieldDataType.String),
+            SearchableField(name="City", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
+            SearchableField(name="StateProvince", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
+            SearchableField(name="PostalCode", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
+            SearchableField(name="Country", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
+        ])
+    ]
+
+scoring_profiles = []
+suggester = [{'name': 'sg', 'source_fields': ['Tags', 'Address/City', 'Address/Country']}]
+
+# Create the search index=
+index = SearchIndex(name=index_name, fields=fields, suggesters=suggester, scoring_profiles=scoring_profiles)
+result = index_client.create_or_update_index(index)
+print(f' {result.name} created')
+```
+
+### Upload documents to the index
+
+Azure AI Search searches over content stored in the service. In this step, you load JSON documents that conform to the hotel index you created.
+
+In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. The notebook defines a documents payload as a list of dictionaries containing hotel data:
+
+```python
+# Create a documents payload
+documents = [
+    {
+    "@search.action": "upload",
+    "HotelId": "1",
+    "HotelName": "Stay-Kay City Hotel",
+    "Description": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
+    "Category": "Boutique",
+    "Tags": [ "view", "air conditioning", "concierge" ],
+    "ParkingIncluded": "false",
+    "LastRenovationDate": "2020-01-18T00:00:00Z",
+    "Rating": 3.60,
+    "Address": {
+        "StreetAddress": "677 5th Ave",
+        "City": "New York",
+        "StateProvince": "NY",
+        "PostalCode": "10022",
+        "Country": "USA"
+        }
+    },
+    {
+    "@search.action": "upload",
+    "HotelId": "2",
+    "HotelName": "Old Century Hotel",
+    "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
+    "Category": "Boutique",
+    "Tags": [ "pool", "free wifi", "concierge" ],
+    "ParkingIncluded": "false",
+    "LastRenovationDate": "2019-02-18T00:00:00Z",
+    "Rating": 3.60,
+    "Address": {
+        "StreetAddress": "140 University Town Center Dr",
+        "City": "Sarasota",
+        "StateProvince": "FL",
+        "PostalCode": "34243",
+        "Country": "USA"
+        }
+    },
+    {
+    "@search.action": "upload",
+    "HotelId": "3",
+    "HotelName": "Gastronomic Landscape Hotel",
+    "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
+    "Category": "Suite",
+    "Tags": [ "restaurant", "bar", "continental breakfast" ],
+    "ParkingIncluded": "true",
+    "LastRenovationDate": "2015-09-20T00:00:00Z",
+    "Rating": 4.80,
+    "Address": {
+        "StreetAddress": "3393 Peachtree Rd",
+        "City": "Atlanta",
+        "StateProvince": "GA",
+        "PostalCode": "30326",
+        "Country": "USA"
+        }
+    },
+    {
+    "@search.action": "upload",
+    "HotelId": "4",
+    "HotelName": "Sublime Palace Hotel",
+    "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.",
+    "Category": "Boutique",
+    "Tags": [ "concierge", "view", "air conditioning" ],
+    "ParkingIncluded": "true",
+    "LastRenovationDate": "2020-02-06T00:00:00Z",
+    "Rating": 4.60,
+    "Address": {
+        "StreetAddress": "7400 San Pedro Ave",
+        "City": "San Antonio",
+        "StateProvince": "TX",
+        "PostalCode": "78216",
+        "Country": "USA"
+        }
+    }
+]
+```
+
+The `upload_documents` method adds documents to the index, creating them if they don't exist or updating them if they do.
+
+```python
+search_client = SearchClient(endpoint=search_endpoint,
+                      index_name=index_name,
+                      credential=credential)
+
+try:
+    result = search_client.upload_documents(documents=documents)
+    print("Upload of new document succeeded: {}".format(result[0].succeeded))
+except Exception as ex:
+    print (ex.message)
+```
+
+### Query the index
 
-    index_name: str = "hotels-quickstart-python"
-    ```
-    
-    #### [API key](#tab/api-key)
-    
-    ```python
-    from azure.core.credentials import AzureKeyCredential
-    from azure.identity import DefaultAzureCredential, AzureAuthorityHosts
-    
-    search_endpoint: str = "https://<Put your search service NAME here>.search.windows.net/"
-    credential = AzureKeyCredential("Your search service admin key")
-
-    index_name: str = "hotels-quickstart-python"
-    ```
-    ---
-
-1. Remove the following two lines from the **Create an index** code cell. Credentials are already set in the previous code cell.
-
-    ```python
-    from azure.core.credentials import AzureKeyCredential
-    credential = AzureKeyCredential(search_api_key)
-    ```
-
-1. Run the **Create an index** code cell to create a search index.
-1. Run the remaining code cells sequentially to load documents and run queries.
+You can get query results as soon as the first document is indexed, but actual testing of your index should wait until all documents are indexed.
 
-## Explaining the code
+Use the `search` method of [SearchClient](/python/api/azure-search-documents/azure.search.documents.searchclient) to run queries.
 
-### Create an index
+The sample queries in the notebook demonstrate common patterns:
 
-`SearchIndexClient` is used to create and manage indexes for Azure AI Search. Each field is identified by a `name` and has a specified `type`. 
+- **Empty search**: Executes an empty search (`search_text="*"`), returning an unranked list (search score = 1.0) of arbitrary documents. Because there are no criteria, all documents are included in results.
 
-Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
+- **Term search**: Adds whole terms to the search expression (`search_text="wifi"`). This query specifies that results contain only those fields in the `select` parameter. Limiting the fields that come back minimizes the amount of data sent back over the wire and reduces search latency.
 
-### Create a documents payload and upload documents
+- **Filtered search**: Adds a filter expression, returning only those hotels with a rating greater than four, sorted in descending order.
 
-Use an [index action](/python/api/azure-search-documents/azure.search.documents.models.indexaction) for the operation type, such as upload or merge-and-upload. Documents originate from the [HotelsData](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotels/HotelsData_toAzureSearch.JSON) sample on GitHub.
+- **Fielded search**: Adds `search_fields` to scope query execution to specific fields.
 
-### Search an index
+- **Faceted search**: Generates facets for positive matches found in search results. There are no zero matches. If search results don't include the term "wifi", then "wifi" doesn't appear in the faceted navigation structure.
 
-You can get query results as soon as the first document is indexed, but actual testing of your index should wait until all documents are indexed.
+- **Document lookup**: Returns a document based on its key. This operation is useful if you want to provide drillthrough when a user selects an item in a search result.
 
-Use the *search* method of the [search.client class](/python/api/azure-search-documents/azure.search.documents.searchclient).
-
-The sample queries in the notebook are:
-- Basic query: Executes an empty search (`search=*`), returning an unranked list (search score = 1.0) of arbitrary documents. Because there are no criteria, all documents are included in results.
-- Term query: Adds whole terms to the search expression ("wifi"). This query specifies that results contain only those fields in the `select` statement. Limiting the fields that come back minimizes the amount of data sent back over the wire and reduces search latency.
-- Filtered query: Add a filter expression, returning only those hotels with a rating greater than four, sorted in descending order.
-- Fielded scoping: Add `search_fields` to scope query execution to specific fields.
-- Facets: Generate facets for positive matches found in search results. There are no zero matches. If search results don't include the term *wifi*, then *wifi* doesn't appear in the faceted navigation structure.
-- Look up a document: Return a document based on its key. This operation is useful if you want to provide drill through when a user selects an item in a search result.
-- Autocomplete: Provide potential matches as the user types into the search box. Autocomplete uses a suggester (`sg`) to know which fields contain potential matches to suggester requests. In this quickstart, those fields are `Tags`, `Address/City`, `Address/Country`. To simulate autocomplete, pass in the letters *sa* as a partial string. The autocomplete method of [SearchClient](/python/api/azure-search-documents/azure.search.documents.searchclient) sends back potential term matches.
+- **Autocomplete**: Provides potential matches as the user types into the search box. Autocomplete uses a suggester (`sg`) to know which fields contain potential matches to suggester requests. In this quickstart, those fields are `Tags`, `Address/City`, and `Address/Country`. To simulate autocomplete, pass in the letters "sa" as a partial string. The `autocomplete` method of `SearchClient` sends back potential term matches.
 
 ### Remove the index
 
-If you're finished with this index, you can delete it by running the **Clean up** code cell. Deleting unnecessary indexes frees up space for stepping through more quickstarts and tutorials.
\ No newline at end of file
+If you're finished with this index, you can delete it by running the `Clean up` code cell. Deleting unnecessary indexes frees up space for stepping through more quickstarts and tutorials.
+
+```python
+try:
+    result = index_client.delete_index(index_name)
+    print ('Index', index_name, 'Deleted')
+except Exception as ex:
+    print (ex)
+```
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonを使用したフルテキスト検索のクイックスタートガイドの改訂"
}
```

### Explanation
このコードの差分は、`full-text-python.md` ファイルに関する大規模な変更を示しています。この変更では、230行の新規追加が行われ、119行が削除され、合計349行の変更が加えられました。目的は、Pythonを使用したAzure AI Searchのフルテキスト検索のクイックスタートガイドを更新し、よりユーザーフレンドリーかつ教育的な内容にすることです。

新しい内容では、Pythonクライアントライブラリを使用して検索インデックスを作成、データをロード、クエリを実行する方法が説明されています。特に、フルテキスト検索やBM25ランキングアルゴリズムについての明確な説明が追加され、ユーザーがこれらの技術を理解しやすくする工夫がされています。また、サンプルデータの具体的な利用方法とGitHubリンクが強調され、すぐにプロジェクトを始められるような内容になっています。

前提条件のセクションも整理され、Pythonの最新バージョン、Visual Studio CodeやJupyterノートブックのインストール手順が含まれています。Gitを用いてサンプルリポジトリをクローンする手順が明記されており、開発環境の設定がシンプルになっています。

コード実行に関する手順が一層具体的になり、これによりユーザーは容易に各ステップを実行できるようになっています。クエリ実行後の出力例も与えられ、実際のデータを用いた応答がどのように得られるかを明示的に示しています。

全体として、この修正により、Pythonを用いたAzure AI Searchのフルテキスト検索の利用がより明確で分かりやすく、また実践的なリソースとなるよう改善されています。

## articles/search/includes/quickstarts/full-text-rest.md{#item-5d3419}

<details>
<summary>Diff</summary>
````diff
@@ -4,178 +4,167 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 06/30/2025
+ms.date: 02/02/2026
 ---
 
-In this quickstart, you use the [Azure AI Search REST APIs](/rest/api/searchservice) to create, load, and query a search index for [full-text search](../../search-lucene-query-architecture.md). Full-text search uses Apache Lucene for indexing and queries and the BM25 ranking algorithm for scoring results.
+In this quickstart, you use the [Azure AI Search REST APIs](/rest/api/searchservice) to create, load, and query a search index for [full-text search](../../search-lucene-query-architecture.md), also known as keyword search.
 
-This quickstart uses fictional hotel data from the [azure-search-sample-data](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/hotels/hotel-json-documents) repo to populate the index.
+Full-text search uses Apache Lucene for indexing and queries and the BM25 ranking algorithm for scoring results. This quickstart uses fictional hotel data from the [azure-search-sample-data](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/hotels/hotel-json-documents) GitHub repository to populate the index.
 
 > [!TIP]
-> You can download the [source code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-keyword-search) to start with a finished project or follow these steps to create your own.
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-keyword-search) on GitHub.
 
 ## Prerequisites
 
-+ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An Azure AI Search service. [Create a service](../../search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription. For this quickstart, you can use a free service.
+- An [Azure AI Search service](../../search-create-service-portal.md). You can use a free service for this quickstart.
 
-+ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
+- [Visual Studio Code](https://code.visualstudio.com/download) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
-+ [Visual Studio Code](https://code.visualstudio.com/download) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
+- [Git](https://git-scm.com/downloads) to clone the sample repository.
 
-## Configure access
-
-You can connect to your Azure AI Search service using API keys or Microsoft Entra ID with role assignments. Keys are easier to start with, but roles are more secure.
-
-To configure the recommended role-based access:
-
-1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
-
-1. From the left pane, select **Settings** > **Keys**.
-
-1. Under **API Access control**, select **Both**.
-
-   This option enables both key-based and keyless authentication. After you assign roles, you can return to this step and select **Role-based access control**.
+- The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-1. From the left pane, select **Access control (IAM)**.
-
-1. Select **Add** > **Add role assignment**.
+## Configure access
 
-1. Assign the **Search Service Contributor** and **Search Index Data Contributor** roles to your user account.
+[!INCLUDE [resource authentication](../resource-authentication.md)]
 
-For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
+## Get endpoint
 
-## Get endpoint and token
+[!INCLUDE [resource endpoint](../resource-endpoint.md)]
 
-In the next section, you specify the following endpoint and token to establish a connection to your Azure AI Search service. These steps assume that you [configured role-based access](#configure-access).
+## Set up the environment
 
-To get your service endpoint and token:
+1. Use Git to clone the sample repository.
 
-1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
+   ```console
+   git clone https://github.com/Azure-Samples/azure-search-rest-samples
+   ```
 
-1. From the left pane, select **Overview**.
+1. Open the `azure-search-rest-samples/Quickstart-keyword-search` folder in Visual Studio Code.
 
-1. Make a note of the URL, which should be similar to `https://my-service.search.windows.net`.
+1. Open the `az-search-quickstart.rest` file.
 
-1. On your local system, open a terminal.
+1. Replace the placeholder value for `@baseUrl` with the URL you obtained in [Get endpoint](#get-endpoint).
 
-1. Sign in to your Azure subscription. If you have multiple subscriptions, select the one that contains your search service.
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service.
 
     ```azurecli
     az login
     ```
 
-1. Make a note of your Microsoft Entra token.
+1. For keyless authentication with Microsoft Entra ID, generate an access token.
 
     ```azurecli
-    az account get-access-token --scope https://search.azure.com/.default
+    az account get-access-token --scope https://search.azure.com/.default --query accessToken -o tsv
     ```
 
-## Set up your file
+1. Replace the placeholder value for `@token` with the access token from the previous step.
 
-Before you can make REST API calls to your Azure AI Search service, you must create a file to store your service endpoint, authentication token, and eventual requests. The REST Client extension in Visual Studio Code supports this task.
+## Run the code
 
-To set up your request file:
+1. Under `### List existing indexes by name`, select **Send Request** to verify your connection.
 
-1. On your local system, open Visual Studio Code.
+   A response should appear in an adjacent pane. If you have existing indexes, they're listed. Otherwise, the list is empty. If the HTTP code is `200 OK`, you're ready to proceed.
 
-1. Create a `.rest` or `.http` file.
+1. Send the remaining requests sequentially to create an index, upload documents, and query the index.
 
-1. Paste the following placeholders and request into the file.
+### Output
 
-    ```http
-    @baseUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
-    @token = PUT-YOUR-PERSONAL-IDENTITY-TOKEN-HERE
-
-    ### List existing indexes by name
-    GET {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
-        Authorization: Bearer {{token}}
-    ```
+Each request returns different JSON based on the operation.  The key output is from `### Run a query`, which should look similar to the following:
 
-1. Replace the `@baseUrl` and `@token` placeholders with the values you obtained in [Get endpoint and token](#get-endpoint-and-token). Don't include quotation marks.
+```json
+{
+  "value": [
+    {
+      "@search.score": 0.5575875,
+      "HotelId": "3",
+      "HotelName": "Gastronomic Landscape Hotel",
+      "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel's restaurant services.",
+      "Tags": [
+        "restaurant",
+        "bar",
+        "continental breakfast"
+      ]
+    }
+  ]
+}
+```
 
-1. Under `### List existing indexes by name`, select **Send Request**.
+## Understand the code
 
-    A response should appear in an adjacent pane. If you have existing indexes, they're listed. Otherwise, the list is empty. If the HTTP code is `200 OK`, you're ready for the next steps.
+Now that you've run the code, let's break down the key steps:
 
-    :::image type="content" source="../../media/search-get-started-rest/rest-client-request-setup.png" lightbox="../../media/search-get-started-rest/rest-client-request-setup.png" alt-text="Screenshot that shows a REST client configured for a search service request.":::
+1. [Create a search index](#create-a-search-index)
+1. [Upload documents to the index](#upload-documents-to-the-index)
+1. [Query the index](#query-the-index)
 
-## Create a search index
+### Create a search index
 
 Before you add content to Azure AI Search, you must create an index to define how the content is stored and structured. An index is conceptually similar to a table in a relational database, but it's specifically designed for search operations, such as full-text search.
 
-To create an index:
+This quickstart calls [Indexes - Create (REST API)](/rest/api/searchservice/indexes/create) to build a search index named `hotels-quickstart` and its physical data structures on your search service.
 
-1. Paste the following request into your file.
+Within the index schema, the `fields` collection defines the structure of hotel documents. Each field has a `name`, data `type`, and attributes that determine its behavior during indexing and queries. The `HotelId` field is marked as the key, which Azure AI Search requires to uniquely identify each document in an index.
 
-    ```http
-    ### Create a new index
-    POST {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
-        Content-Type: application/json
-        Authorization: Bearer {{token}}
-    
-        {
-            "name": "hotels-quickstart",  
+```http
+### Create a new index
+POST {{baseUrl}}/indexes?api-version={{api-version}}  HTTP/1.1
+Content-Type: application/json
+Authorization: Bearer {{token}}
+
+{
+    "name": "hotels-quickstart",  
+    "fields": [
+        {"name": "HotelId", "type": "Edm.String", "key": true, "filterable": true},
+        {"name": "HotelName", "type": "Edm.String", "searchable": true, "filterable": false, "sortable": true, "facetable": false},
+        {"name": "Description", "type": "Edm.String", "searchable": true, "filterable": false, "sortable": false, "facetable": false, "analyzer": "en.lucene"},
+        {"name": "Category", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true},
+        {"name": "Tags", "type": "Collection(Edm.String)", "searchable": true, "filterable": true, "sortable": false, "facetable": true},
+        {"name": "ParkingIncluded", "type": "Edm.Boolean", "filterable": true, "sortable": true, "facetable": true},
+        {"name": "LastRenovationDate", "type": "Edm.DateTimeOffset", "filterable": true, "sortable": true, "facetable": true},
+        {"name": "Rating", "type": "Edm.Double", "filterable": true, "sortable": true, "facetable": true},
+        {"name": "Address", "type": "Edm.ComplexType", 
             "fields": [
-                {"name": "HotelId", "type": "Edm.String", "key": true, "filterable": true},
-                {"name": "HotelName", "type": "Edm.String", "searchable": true, "filterable": false, "sortable": true, "facetable": false},
-                {"name": "Description", "type": "Edm.String", "searchable": true, "filterable": false, "sortable": false, "facetable": false, "analyzer": "en.lucene"},
-                {"name": "Category", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true},
-                {"name": "Tags", "type": "Collection(Edm.String)", "searchable": true, "filterable": true, "sortable": false, "facetable": true},
-                {"name": "ParkingIncluded", "type": "Edm.Boolean", "filterable": true, "sortable": true, "facetable": true},
-                {"name": "LastRenovationDate", "type": "Edm.DateTimeOffset", "filterable": true, "sortable": true, "facetable": true},
-                {"name": "Rating", "type": "Edm.Double", "filterable": true, "sortable": true, "facetable": true},
-                {"name": "Address", "type": "Edm.ComplexType", 
-                    "fields": [
-                    {"name": "StreetAddress", "type": "Edm.String", "filterable": false, "sortable": false, "facetable": false, "searchable": true},
-                    {"name": "City", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true},
-                    {"name": "StateProvince", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true},
-                    {"name": "PostalCode", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true},
-                    {"name": "Country", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true}
-                    ]
-                }
+            {"name": "StreetAddress", "type": "Edm.String", "filterable": false, "sortable": false, "facetable": false, "searchable": true},
+            {"name": "City", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true},
+            {"name": "StateProvince", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true},
+            {"name": "PostalCode", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true},
+            {"name": "Country", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true}
             ]
         }
-    ```
-
-2. Under `### Create a new index`, select **Send Request**.
-
-   You should receive an `HTTP/1.1 201 Created` response whose body contains the JSON representation of the index schema.
-
-### About the create index request
-
-This quickstart calls [Indexes - Create (REST API)](/rest/api/searchservice/indexes/create) to build a search index named `hotels-quickstart` and its physical data structures on your search service.
-
-Within the index schema, the `fields` collection defines the structure of hotel documents. Each field has a `name`, data `type`, and attributes that determine its behavior during indexing and queries. The `HotelId` field is marked as the key, which Azure AI Search requires to uniquely identify each document in an index.
+    ]
+}
+```
 
 Key points about the index schema:
 
 + Use string fields (`Edm.String`) to make numeric data full-text searchable. Other [supported data types](/rest/api/searchservice/supported-data-types), such as `Edm.Int32`, are filterable, sortable, facetable, and retrievable but aren't searchable.
 
-+ Most of our fields are simple data types, but you can define complex types to represent nested data, such as the `Address` field.
++ Most of the fields are simple data types, but you can define complex types to represent nested data, such as the `Address` field.
 
 + Field attributes determine allowed actions. The REST APIs allow [many actions by default](/rest/api/searchservice/indexes/create#request-body). For example, all strings are searchable and retrievable. With the REST APIs, you might only use attributes if you need to disable a behavior.
 
-## Load the index
+### Upload documents to the index
 
 Newly created indexes are empty. To populate an index and make it searchable, you must upload JSON documents that conform to the index schema.
 
 In Azure AI Search, documents serve as both inputs for indexing and outputs for queries. For simplicity, this quickstart provides sample hotel documents as inline JSON. In production scenarios, however, content is often pulled from connected data sources and transformed into JSON using [indexers](../../search-indexer-overview.md).
 
-To upload documents to your index:
+This quickstart calls [Documents - Index (REST API)](/rest/api/searchservice/documents/index) to add four sample hotel documents to your index. Compared to the previous request, the URI is extended to include the `docs` collection and `index` operation.
 
-1. Paste the following request into your file.
+Each document in the `value` array represents a hotel and contains fields that match the index schema. The `@search.action` parameter specifies the operation to perform for each document. This example uses `upload`, which adds the document if it doesn't exist or updates the document if it does exist.
 
-    ```http
-    ### Upload documents
-    POST {{baseUrl}}/indexes/hotels-quickstart/docs/index?api-version=2025-09-01  HTTP/1.1
-        Content-Type: application/json
-        Authorization: Bearer {{token}}
-    
+```http
+### Upload documents
+POST {{baseUrl}}/indexes/hotels-quickstart/docs/index?api-version={{api-version}}  HTTP/1.1
+Content-Type: application/json
+Authorization: Bearer {{token}}
+
+{
+    "value": [
         {
-            "value": [
-            {
             "@search.action": "upload",
             "HotelId": "1",
             "HotelName": "Stay-Kay City Hotel",
@@ -186,135 +175,94 @@ To upload documents to your index:
             "LastRenovationDate": "2022-01-18T00:00:00Z",
             "Rating": 3.60,
             "Address": 
-                {
+            {
                 "StreetAddress": "677 5th Ave",
                 "City": "New York",
                 "StateProvince": "NY",
                 "PostalCode": "10022",
                 "Country": "USA"
-                } 
-            },
-            {
+            } 
+        },
+        {
             "@search.action": "upload",
             "HotelId": "2",
             "HotelName": "Old Century Hotel",
             "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
-             "Category": "Boutique",
+            "Category": "Boutique",
             "Tags": [ "pool", "free wifi", "concierge" ],
             "ParkingIncluded": false,
             "LastRenovationDate": "2019-02-18T00:00:00Z",
             "Rating": 3.60,
             "Address": 
-                {
+            {
                 "StreetAddress": "140 University Town Center Dr",
                 "City": "Sarasota",
                 "StateProvince": "FL",
                 "PostalCode": "34243",
                 "Country": "USA"
-                } 
-            },
-            {
+            } 
+        },
+        {
             "@search.action": "upload",
             "HotelId": "3",
             "HotelName": "Gastronomic Landscape Hotel",
-            "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel's restaurant services.",
+            "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
             "Category": "Suite",
             "Tags": [ "restaurant", "bar", "continental breakfast" ],
             "ParkingIncluded": true,
             "LastRenovationDate": "2015-09-20T00:00:00Z",
             "Rating": 4.80,
             "Address": 
-                {
+            {
                 "StreetAddress": "3393 Peachtree Rd",
                 "City": "Atlanta",
                 "StateProvince": "GA",
                 "PostalCode": "30326",
                 "Country": "USA"
-                } 
-            },
-            {
+            } 
+        },
+        {
             "@search.action": "upload",
             "HotelId": "4",
             "HotelName": "Sublime Palace Hotel",
             "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.",
-            "Category": "Luxury",
             "Tags": [ "concierge", "view", "air conditioning" ],
             "ParkingIncluded": true,
             "LastRenovationDate": "2020-02-06T00:00:00Z",
             "Rating": 4.60,
             "Address": 
-                {
+            {
                 "StreetAddress": "7400 San Pedro Ave",
                 "City": "San Antonio",
                 "StateProvince": "TX",
                 "PostalCode": "78216",
                 "Country": "USA"
-                }
             }
-          ]
         }
-    ```
-
-2. Under `### Upload documents`, select **Send Request**.
-
-   You should receive an `HTTP/1.1 200 OK` response whose body contains the key and status of each uploaded document.
-
-### About the upload request
+    ]
+}
+```
 
-This quickstart calls [Documents - Index (REST API)](/rest/api/searchservice/documents/) to add four sample hotel documents to your index. Compared to the previous request, the URI is extended to include the `docs` collection and `index` operation.
-
-Each document in the `value` array represents a hotel and contains fields that match the index schema. The `@search.action` parameter specifies the operation to perform for each document. Our example uses `upload`, which adds the document if it doesn't exist or updates the document if it does exist.
-
-## Query the index
+### Query the index
 
 Now that documents are loaded into your index, you can use full-text search to find specific terms or phrases within their fields.
 
-To run a full-text query against your index:
-
-1. Paste the following request into your file.
-
-    ```http
-    ### Run a query
-    POST {{baseUrl}}/indexes/hotels-quickstart/docs/search?api-version=2025-09-01  HTTP/1.1
-      Content-Type: application/json
-      Authorization: Bearer {{token}}
-    
-      {
-          "search": "attached restaurant",
-          "select": "HotelId, HotelName, Tags, Description",
-          "searchFields": "Description, Tags",
-          "count": true
-      }
-    ```
-
-2. Under `### Run a query`, select **Send Request**.
-
-   You should receive an `HTTP/1.1 200 OK` response similar to the following example, which shows one matching hotel document, its relevance score, and its selected fields.
-
-    ```json
-    {
-      "@odata.context": "https://my-service.search.windows.net/indexes('hotels-quickstart')/$metadata#docs(*)",
-      "@odata.count": 1,
-      "value": [
-        {
-          "@search.score": 0.5575875,
-          "HotelId": "3",
-          "HotelName": "Gastronomic Landscape Hotel",
-          "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel\u2019s restaurant services.",
-          "Tags": [
-            "restaurant",
-            "bar",
-            "continental breakfast"
-          ]
-        }
-      ]
-    }
-    ```
-
-### About the query request
-
 This quickstart calls [Documents - Search Post (REST API)](/rest/api/searchservice/documents/search-post) to find hotel documents that match your search criteria. The URI now targets the `/docs/search` operation.
 
 Full-text search requests always include a `search` parameter that contains the query text. The query text can include one or more terms, phrases, or operators. In addition to `search`, you can specify other parameters to refine the search behavior and results.
 
-Our query searches for the terms "attached restaurant" in the `Description` and `Tags` fields of each hotel document. The `select` parameter limits the fields returned in the response to `HotelId`, `HotelName`, `Tags`, and `Description`. The `count` parameter requests the total number of matching documents.
+The query searches for the terms "attached restaurant" in the `Description` and `Tags` fields of each hotel document. The `select` parameter limits the fields returned in the response to `HotelId`, `HotelName`, `Tags`, and `Description`. The `count` parameter requests the total number of matching documents.
+
+```http
+### Run a query
+POST {{baseUrl}}/indexes/hotels-quickstart/docs/search?api-version={{api-version}}  HTTP/1.1
+Content-Type: application/json
+Authorization: Bearer {{token}}
+
+{
+    "search": "attached restaurant",
+    "select": "HotelId, HotelName, Tags, Description",
+    "searchFields": "Description, Tags",
+    "count": true
+}
+```
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIを使用したフルテキスト検索のクイックスタートガイドの改訂"
}
```

### Explanation
このコードの差分は、`full-text-rest.md` ファイルに関する変更を示します。全体で128行の新規追加と180行の削除があり、合計308行の変更が行われました。この変更の目的は、Azure AI SearchのREST APIを使用してフルテキスト検索を行うためのクイックスタートガイドを更新して、より明確で使いやすくすることです。

新しい内容では、クイックスタートでの手順や要件が分かりやすく説明されています。フルテキスト検索がキーワード検索としても知られていることが明示され、Apache LuceneやBM25ランキングアルゴリズムの説明が追加されています。また、使用するサンプルデータのリポジトリに関するリンクも更新され、ユーザーがコードを簡単にダウンロードできるようになっています。

前提条件セクションは整理され、AzureアカウントやAzure AI Searchサービスの具体的な作成方法が示されています。さらに、Visual Studio CodeやREST Clientの必要性が強調され、Gitによるサンプルリポジトリのクローン手順も追加されています。

接続設定やトークン取得のセクションも改訂され、容易に必要な情報を得られるようインストラクションが詳細化されています。特に、REST APIを使用したドキュメントのインデックス作成や検索の手順が改善され、より直感的に理解できる内容になっています。

このクイックスタートガイドは、ユーザーがAPIを通じてフルテキスト検索を迅速に始められるように設計されており、コードの実行に伴う出力例も具体的に示されています。全体として、これによりAzure AI Searchの利用がより容易になり、実践的なリソースとなることが期待されます。

## articles/search/includes/quickstarts/full-text-typescript.md{#item-6630e8}

<details>
<summary>Diff</summary>
````diff
@@ -4,96 +4,93 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 02/02/2026
 ---
 
-[!INCLUDE [Full text introduction](full-text-intro.md)]
+In this quickstart, you use the [Azure AI Search client library for JavaScript](/javascript/api/overview/azure/search-documents-readme) (compatible with TypeScript) to create, load, and query a search index for [full-text search](../../search-lucene-query-architecture.md), also known as keyword search.
+
+Full-text search uses Apache Lucene for indexing and queries and the BM25 ranking algorithm for scoring results. This quickstart uses fictional hotel data from the [azure-search-sample-data](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/hotels/hotel-json-documents) GitHub repository to populate the index.
 
 > [!TIP]
-> You can download the [source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-keyword-search) to start with a finished project or follow these steps to create your own.
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-keyword-search) on GitHub.
 
 ## Prerequisites
 
 - An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. For this quickstart, you can use a free service.
 
-## Microsoft Entra ID prerequisites
+- An [Azure AI Search service](../../search-create-service-portal.md). You can use a free service for this quickstart.
 
-For the recommended keyless authentication with Microsoft Entra ID, you must:
+- The latest LTS version of [Node.js](https://nodejs.org/en/download/).
 
-- Install the [Azure CLI](/cli/azure/install-azure-cli).
+- [Visual Studio Code](https://code.visualstudio.com/download).
 
-- Assign the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
+- [Git](https://git-scm.com/downloads) to clone the sample repository.
 
-## Get service information
+- The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-[!INCLUDE [resource authentication](../resource-authentication.md)]
+## Configure access
 
-## Set up
+[!INCLUDE [resource authentication](../resource-authentication.md)]
 
-1. Create a new folder `full-text-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
+## Get endpoint
 
-    ```shell
-    mkdir full-text-quickstart && cd full-text-quickstart
-    ```
+[!INCLUDE [resource endpoint](../resource-endpoint.md)]
 
-1. Create the `package.json` with the following command:
+## Set up the environment
 
-    ```shell
-    npm init -y
-    ```
+1. Use Git to clone the sample repository.
 
-1. Update the `package.json` to ECMAScript with the following command: 
+   ```console
+   git clone https://github.com/Azure-Samples/azure-search-javascript-samples
+   ```
 
-    ```shell
-    npm pkg set type=module
-    ```
+1. Open the `azure-search-javascript-samples/quickstart-keyword-search` folder in Visual Studio Code.
 
-1. Install the Azure AI Search client library ([Azure.Search.Documents](/javascript/api/overview/azure/search-documents-readme)) for JavaScript with:
+1. Rename the `sample.env` file to `.env`, and then open the file.
 
-    ```console
-    npm install @azure/search-documents
-    ```
+1. Replace the placeholder value for `SEARCH_API_ENDPOINT` with the URL you obtained in [Get endpoint](#get-endpoint).
 
-1. For the **recommended** passwordless authentication, install the Azure Identity client library with:
+1. Use a terminal in Visual Studio Code to install the dependencies and initialize the project for TypeScript.
 
     ```console
-    npm install @azure/identity
+    npm install
+    npm install typescript @types/node --save-dev
+    npm pkg set type=module
     ```
 
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service.
 
-## Create, load, and query a search index
-
-In the prior [set up](#set-up) section, you installed the Azure AI Search client library and other dependencies. 
-
-In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [Explaining the code](#explaining-the-code) section.
-
-The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
-
-#### [Microsoft Entra ID](#tab/keyless)
+    ```azurecli
+    az login
+    ```
 
-```javascript
-const searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
-const credential = new DefaultAzureCredential();
-```
+## Run the code
 
-#### [API key](#tab/api-key)
+1. Create a file named `tsconfig.json`, and then paste the following code into it.
 
-```javascript
-const searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
-const credential = new AzureKeyCredential(apiKey);
-```
----
+    ```json
+    {
+      "compilerOptions": {
+        "module": "NodeNext",
+        "target": "ES2022",
+        "moduleResolution": "NodeNext",
+        "skipLibCheck": true,
+        "strict": true,
+        "resolveJsonModule": true
+      },
+      "include": ["*.ts"],
+      "exclude": ["node_modules"]
+    }
+    ```
 
-1. Create a new file named *index.ts* and paste the following code into *index.ts*:
+1. Rename the `index.js` file to `index.ts`, and then replace the contents with the following code. This code converts the CommonJS syntax to ES module imports, which are required for TypeScript compilation.
 
     ```typescript
     // Import from the @azure/search-documents library
     import {
         SearchIndexClient,
         SearchClient,
         SearchFieldDataType,
-        AzureKeyCredential,
         odata,
         SearchIndex
     } from "@azure/search-documents";
@@ -102,11 +99,10 @@ const credential = new AzureKeyCredential(apiKey);
     import { DefaultAzureCredential } from "@azure/identity";
     
     // Importing the hotels sample data
-    import hotelData from './hotels.json' assert { type: "json" };
+    import hotelData from './hotels.json' with { type: "json" };
     
     // Load the .env file if it exists
-    import * as dotenv from "dotenv";
-    dotenv.config();
+    import "dotenv/config";
     
     // Defining the index definition
     const indexDefinition: SearchIndex = {
@@ -231,14 +227,14 @@ const credential = new AzureKeyCredential(apiKey);
     };
     
     async function main() {
-        
-    	// Your search service endpoint
-    	const searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
-    	
+    
+    	// Your search service endpoint (from .env file)
+    	const searchServiceEndpoint = process.env.SEARCH_API_ENDPOINT || "";
+    
     	// Use the recommended keyless credential instead of the AzureKeyCredential credential.
     	const credential = new DefaultAzureCredential();
     	//const credential = new AzureKeyCredential(Your search service admin key);
-    	
+    
     	// Create a SearchIndexClient to send create/delete index commands
     	const searchIndexClient: SearchIndexClient = new SearchIndexClient(
     		searchServiceEndpoint,
@@ -261,7 +257,7 @@ const credential = new AzureKeyCredential(apiKey);
         console.log(`Index operations succeeded: ${JSON.stringify(indexDocumentsResult.results[0].succeeded)} `);
     
         // waiting one second for indexing to complete (for demo purposes only)
-        sleep(1000);
+        await sleep(1000);
     
         console.log('Querying the index...');
         console.log();
@@ -351,247 +347,164 @@ const credential = new AzureKeyCredential(apiKey);
     });
     ```
 
-1. Create a file named *hotels.json* and paste the following code into *hotels.json*:
-
-    ```json
-    {
-        "value": [
-            {
-                "HotelId": "1",
-                "HotelName": "Stay-Kay City Hotel",
-                "Description": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
-                "Category": "Boutique",
-                "Tags": ["view", "air conditioning", "concierge"],
-                "ParkingIncluded": false,
-                "LastRenovationDate": "2022-01-18T00:00:00Z",
-                "Rating": 3.6,
-                "Address": {
-                    "StreetAddress": "677 5th Ave",
-                    "City": "New York",
-                    "StateProvince": "NY",
-                    "PostalCode": "10022"
-                }
-            },
-            {
-                "HotelId": "2",
-                "HotelName": "Old Century Hotel",
-                "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
-                "Category": "Boutique",
-                "Tags": ["pool", "free wifi", "concierge"],
-                "ParkingIncluded": "false",
-                "LastRenovationDate": "2019-02-18T00:00:00Z",
-                "Rating": 3.6,
-                "Address": {
-                    "StreetAddress": "140 University Town Center Dr",
-                    "City": "Sarasota",
-                    "StateProvince": "FL",
-                    "PostalCode": "34243"
-                }
-            },
-            {
-                "HotelId": "3",
-                "HotelName": "Gastronomic Landscape Hotel",
-                "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
-                "Category": "Suite",
-                "Tags": ["restaurant, "bar", "continental breakfast"],
-                "ParkingIncluded": "true",
-                "LastRenovationDate": "2015-09-20T00:00:00Z",
-                "Rating": 4.8,
-                "Address": {
-                    "StreetAddress": "3393 Peachtree Rd",
-                    "City": "Atlanta",
-                    "StateProvince": "GA",
-                    "PostalCode": "30326"
-                }
-            },
-            {
-                "HotelId": "4",
-                "HotelName": "Sublime Palace Hotel",
-                "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.",
-                "Category": "Boutique",
-                "Tags": ["concierge", "view", "air conditioning"],
-                "ParkingIncluded": true,
-                "LastRenovationDate": "2020-02-06T00:00:00Z",
-                "Rating": 4.6,
-                "Address": {
-                    "StreetAddress": "7400 San Pedro Ave",
-                    "City": "San Antonio",
-                    "StateProvince": "TX",
-                    "PostalCode": "78216"
-                }
-            }
-        ]
-    }
-    ```
-
-1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
-
-    ```json
-    {
-        "compilerOptions": {
-          "module": "NodeNext",
-          "target": "ES2022", // Supports top-level await
-          "moduleResolution": "NodeNext",
-          "skipLibCheck": true, // Avoid type errors from node_modules
-          "strict": true // Enable strict type-checking options
-        },
-        "include": ["*.ts"]
-    }
-    ```
-
 1. Transpile from TypeScript to JavaScript.
 
-    ```shell
-    tsc
-    ```
-    
-1. Sign in to Azure with the following command:
-
-    ```shell
-    az login
+    ```console
+    npx tsc
     ```
 
-1. Run the JavaScript code with the following command:
+1. Run the application.
 
-    ```shell
+    ```console
     node index.js
     ```
 
-## Explaining the code
+### Output
 
-### Create index
+The output should be similar to the following:
 
-Create a file *hotels_quickstart_index.json*. This file defines how Azure AI Search works with the documents you load in the next step. Each field is identified by a `name` and has a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
-
-We want to import *hotels_quickstart_index.json* so the main function can access the index definition.
-
-```typescript
-import indexDefinition from './hotels_quickstart_index.json';
-
-interface HotelIndexDefinition {
-    name: string;
-    fields: SimpleField[] | ComplexField[];
-    suggesters: SearchSuggester[];
-};
-const hotelIndexDefinition: HotelIndexDefinition = indexDefinition as HotelIndexDefinition;
 ```
-
-Within the main function, we then create a `SearchIndexClient`, which is used to create and manage indexes for Azure AI Search. 
-
-```javascript
-const indexClient = new SearchIndexClient(endpoint, new AzureKeyCredential(apiKey));
+Checking if index exists...
+Deleting index...
+Creating index...
+Index named hotels-quickstart has been created.
+Uploading documents...
+Index operations succeeded: true 
+Querying the index...
+
+Query #1 - search everything:
+{"HotelId":"3","HotelName":"Gastronomic Landscape Hotel","Rating":4.8}
+{"HotelId":"2","HotelName":"Old Century Hotel","Rating":3.6}
+{"HotelId":"4","HotelName":"Sublime Palace Hotel","Rating":4.6}
+{"HotelId":"1","HotelName":"Stay-Kay City Hotel","Rating":3.6}
+Result count: 4
+
+Query #2 - search with filter, orderBy, and select:
+{"HotelId":"2","HotelName":"Old Century Hotel","Rating":3.6}
+
+Query #3 - limit searchFields:
+{"HotelId":"4","HotelName":"Sublime Palace Hotel","Rating":4.6}
+
+Query #4 - limit searchFields and use facets:
+{"HotelId":"3","HotelName":"Gastronomic Landscape Hotel","Rating":4.8}
+{"HotelId":"2","HotelName":"Old Century Hotel","Rating":3.6}
+{"HotelId":"4","HotelName":"Sublime Palace Hotel","Rating":4.6}
+{"HotelId":"1","HotelName":"Stay-Kay City Hotel","Rating":3.6}
+
+Query #5 - Lookup document:
+HotelId: 3; HotelName: Gastronomic Landscape Hotel
 ```
 
-Next, we want to delete the index if it already exists. This operation is a common practice for test/demo code.
+## Understand the code
 
-We do this by defining a simple function that tries to delete the index.
+Now that you've run the code, let's break down the key steps:
 
-```typescript
-async function deleteIndexIfExists(indexClient: SearchIndexClient, indexName: string): Promise<void> {
-    try {
-        await indexClient.deleteIndex(indexName);
-        console.log('Deleting index...');
-    } catch {
-        console.log('Index does not exist yet.');
-    }
-}
-```
+1. [Create a search client](#create-a-search-client)
+1. [Create a search index](#create-a-search-index)
+1. [Upload documents to the index](#upload-documents-to-the-index)
+1. [Query the index](#query-the-index)
 
-To run the function, we extract the index name from the index definition and pass the `indexName` along with the `indexClient` to the `deleteIndexIfExists()` function.
+### Create a search client
 
-```typescript
-// Getting the name of the index from the index definition
-const indexName: string = hotelIndexDefinition.name;
+In `index.ts`, you create two clients:
 
-console.log('Checking if index exists...');
-await deleteIndexIfExists(indexClient, indexName);
-```
+- [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient) creates the index.
+- [SearchClient](/javascript/api/@azure/search-documents/searchclient) loads and queries an existing index.
 
-After that, we're ready to create the index with the `createIndex()` method.
+Both clients require the service endpoint and a credential for authentication. In this quickstart, you use [DefaultAzureCredential](/javascript/api/@azure/identity/defaultazurecredential) for keyless authentication with Microsoft Entra ID.
 
 ```typescript
-console.log('Creating index...');
-let index = await indexClient.createIndex(hotelIndexDefinition);
-
-console.log(`Index named ${index.name} has been created.`);
-``` 
-
-### Load documents 
-
-In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this case, we'll programmatically push the documents to the index.
+const credential = new DefaultAzureCredential();
+const searchIndexClient: SearchIndexClient = new SearchIndexClient(
+    searchServiceEndpoint,
+    credential
+);
+```
 
-Document inputs might be rows in a database, blobs in Blob storage, or, as in this sample, JSON documents on disk. You can either download [hotels.json](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart-keyword-search/hotels.json) or create your own *hotels.json* file with the following content:
+### Create a search index
 
+This quickstart builds a hotels index that you load with hotel data and execute queries against. In this step, you define the fields in the index.
 
-Similar to what we did with the indexDefinition, we also need to import `hotels.json` at the top of *index.ts* so that the data can be accessed in our main function.
+The `indexDefinition` object defines how Azure AI Search works with the documents you load in the next step. Each field is identified by a `name` and has a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `Address`, are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create).
 
 ```typescript
-import hotelData from './hotels.json';
-
-interface Hotel {
-    HotelId: string;
-    HotelName: string;
-    Description: string;
-    Category: string;
-    Tags: string[];
-    ParkingIncluded: string | boolean;
-    LastRenovationDate: string;
-    Rating: number;
-    Address: {
-        StreetAddress: string;
-        City: string;
-        StateProvince: string;
-        PostalCode: string;
-    };
+const indexDefinition: SearchIndex = {
+    "name": "hotels-quickstart",
+    "fields": [
+        {
+            "name": "HotelId",
+            "type": "Edm.String" as SearchFieldDataType,
+            "key": true,
+            "filterable": true
+        },
+        {
+            "name": "HotelName",
+            "type": "Edm.String" as SearchFieldDataType,
+            "searchable": true,
+            "filterable": false,
+            "sortable": true,
+            "facetable": false
+        },
+        // REDACTED FOR BREVITY
+    ],
+    "suggesters": [
+        {
+            "name": "sg",
+            "searchMode": "analyzingInfixMatching",
+            "sourceFields": ["HotelName"]
+        }
+    ]
 };
-
-const hotels: Hotel[] = hotelData["value"];
 ```
 
-To index data into the search index, we now need to create a `SearchClient`. While the `SearchIndexClient` is used to create and manage an index, the `SearchClient` is used to upload documents and query the index.
-
-There are two ways to create a `SearchClient`. The first option is to create a `SearchClient` from scratch:
+This quickstart deletes the index if it already exists, which is a common practice for test/demo code.
 
 ```typescript
- const searchClient = new SearchClient<Hotel>(endpoint, indexName, new AzureKeyCredential(apiKey));
+async function deleteIndexIfExists(searchIndexClient: SearchIndexClient, indexName: string) {
+    try {
+        await searchIndexClient.deleteIndex(indexName);
+        console.log('Deleting index...');
+    } catch {
+        console.log('Index does not exist yet.');
+    }
+}
 ```
 
-Alternatively, you can use the `getSearchClient()` method of the `SearchIndexClient` to create the `SearchClient`:
+After that, the index is created with the `createIndex()` method.
 
 ```typescript
-const searchClient = indexClient.getSearchClient<Hotel>(indexName);
+let index: SearchIndex = await searchIndexClient.createIndex(indexDefinition);
 ```
 
-Now that the client is defined, upload the documents into the search index. In this case, we use the `mergeOrUploadDocuments()` method, which uploads the documents or merges them with an existing document if a document with the same key already exists. Then check that the operation succeeded because at least the first document exists.
+### Upload documents to the index
 
-```typescript
-console.log("Uploading documents...");
-const indexDocumentsResult = await searchClient.mergeOrUploadDocuments(hotels);
+In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this quickstart, you programmatically push the documents to the index.
 
-console.log(`Index operations succeeded: ${JSON.stringify(indexDocumentsResult.results[0].succeeded)}`);
+Document inputs might be rows in a database, blobs in Azure Blob Storage, or JSON documents on disk, as in this quickstart. The hotel data is imported at the top of the file:
+
+```typescript
+import hotelData from './hotels.json' with { type: "json" };
 ```
 
-Run the program again with `tsc && node index.ts`. You should see a slightly different set of messages from those you saw in Step 1. This time, the index *does* exist, and you should see a message about deleting it before the app creates the new index and posts data to it. 
+To index data into the search index, you create a [SearchClient](/javascript/api/@azure/search-documents/searchclient). While `SearchIndexClient` creates and manages an index, `SearchClient` uploads documents and queries the index.
 
-Before we run the queries in the next step, define a function to have the program wait for one second. This is done just for test/demo purposes to ensure the indexing finishes and that the documents are available in the index for our queries.
+This quickstart obtains `SearchClient` from `SearchIndexClient` using [getSearchClient](/javascript/api/@azure/search-documents/searchindexclient#@azure-search-documents-searchindexclient-getsearchclient), which reuses the same credentials.
 
 ```typescript
-function sleep(ms: number): Promise<void> {
-    return new Promise((resolve) => setTimeout(resolve, ms));
-}
+const searchClient: SearchClient<any> = searchIndexClient.getSearchClient(indexName);
 ```
 
-To have the program wait for one second, call the `sleep` function:
+The `mergeOrUploadDocuments()` method uploads the documents or merges them with an existing document if a document with the same key already exists.
 
 ```typescript
-sleep(1000);
+let indexDocumentsResult = await searchClient.mergeOrUploadDocuments(hotelData['value']);
 ```
 
-### Search an index
+### Query the index
 
-With an index created and documents uploaded, you're ready to send queries to the index. In this section, we send five different queries to the search index to demonstrate different pieces of query functionality available to you.
+With an index created and documents uploaded, you're ready to send queries to the index. This section sends five different queries to the search index to demonstrate different pieces of query functionality available to you.
 
-The queries are written in a `sendQueries()` function that we call in the main function as follows:
+The queries are written in a `sendQueries()` function that is called in the main function:
 
 ```typescript
 await sendQueries(searchClient);
@@ -601,104 +514,90 @@ Queries are sent using the `search()` method of `searchClient`. The first parame
 
 #### Query example 1
 
-The first query searches `*`, which is equivalent to searching everything and selects three of the fields in the index. It's a best practice to only `select` the fields you need because pulling back unnecessary data can add latency to your queries.
+The first query searches `*`, which is equivalent to searching everything, and selects three of the fields in the index. It's a best practice to only `select` the fields you need because pulling back unnecessary data can add latency to your queries.
 
-The `searchOptions` for this query also has `includeTotalCount` set to `true`, which will return the number of matching results found.
+The `searchOptions` for this query also has `includeTotalCount` set to `true`, which returns the number of matching results found.
 
 ```typescript
-async function sendQueries(
-    searchClient: SearchClient<Hotel>
-): Promise<void> {
-
-    // Query 1
-    console.log('Query #1 - search everything:');
-    const selectFields: SearchFieldArray<Hotel> = [
-        "HotelId",
-        "HotelName",
-        "Rating",
-    ];
-    const searchOptions1 = { 
-        includeTotalCount: true, 
-        select: selectFields 
-    };
-
-    let searchResults = await searchClient.search("*", searchOptions1);
-    for await (const result of searchResults.results) {
-        console.log(`${JSON.stringify(result.document)}`);
-    }
-    console.log(`Result count: ${searchResults.count}`);
+console.log('Query #1 - search everything:');
+let searchOptions: any = {
+    includeTotalCount: true,
+    select: ["HotelId", "HotelName", "Rating"]
+};
 
-    // remaining queries go here
+let searchResults = await searchClient.search("*", searchOptions);
+for await (const result of searchResults.results) {
+    console.log(`${JSON.stringify(result.document)}`);
 }
+console.log(`Result count: ${searchResults.count}`);
 ```
 
-The remaining queries outlined below should also be added to the `sendQueries()` function. They're separated here for readability.
-
 #### Query example 2
 
-In the next query, we specify the search term `"wifi"` and also include a filter to only return results where the state is equal to `'FL'`. Results are also ordered by the Hotel's `Rating`.
+In the next query, the search term `"wifi"` is specified with a filter to only return results where the state is equal to `'FL'`. Results are also ordered by the Hotel's `Rating`.
 
 ```typescript
 console.log('Query #2 - search with filter, orderBy, and select:');
 let state = 'FL';
-const searchOptions2 = {
+searchOptions = {
     filter: odata`Address/StateProvince eq ${state}`,
     orderBy: ["Rating desc"],
-    select: selectFields
+    select: ["HotelId", "HotelName", "Rating"]
 };
-searchResults = await searchClient.search("wifi", searchOptions2);
+
+searchResults = await searchClient.search("wifi", searchOptions);
 for await (const result of searchResults.results) {
     console.log(`${JSON.stringify(result.document)}`);
 }
 ```
 
 #### Query example 3
 
-Next, the search is limited to a single searchable field using the `searchFields` parameter. This approach is a great option to make your query more efficient if you know you're only interested in matches in certain fields. 
+The search is limited to a single searchable field using the `searchFields` parameter. This approach is a great option to make your query more efficient if you know you're only interested in matches in certain fields.
 
 ```typescript
 console.log('Query #3 - limit searchFields:');
-const searchOptions3 = {
-    select: selectFields,
-    searchFields: ["HotelName"] as const
+searchOptions = {
+    select: ["HotelId", "HotelName", "Rating"],
+    searchFields: ["HotelName"]
 };
 
-searchResults = await searchClient.search("Sublime Palace", searchOptions3);
+searchResults = await searchClient.search("sublime palace", searchOptions);
 for await (const result of searchResults.results) {
     console.log(`${JSON.stringify(result.document)}`);
 }
 ```
 
 #### Query example 4
 
-Another common option to include in a query is `facets`. Facets allow you to provide self-directed drilldown from the results in your UI. The facets results can be turned into checkboxes in the result pane. 
+Another common option to include in a query is `facets`. Facets allow you to provide self-directed drilldown from the results in your UI. The facets results can be turned into checkboxes in the result pane.
 
 ```typescript
 console.log('Query #4 - limit searchFields and use facets:');
-const searchOptions4 = {
+searchOptions = {
     facets: ["Category"],
-    select: selectFields,
-    searchFields: ["HotelName"] as const
+    select: ["HotelId", "HotelName", "Rating"],
+    searchFields: ["HotelName"]
 };
 
-searchResults = await searchClient.search("*", searchOptions4);
+searchResults = await searchClient.search("*", searchOptions);
 for await (const result of searchResults.results) {
     console.log(`${JSON.stringify(result.document)}`);
 }
 ```
 
 #### Query example 5
 
-The final query uses the `getDocument()` method of the `searchClient`. This allows you to efficiently retrieve a document by its key. 
+The final query uses the `getDocument()` method of the `searchClient`. This allows you to efficiently retrieve a document by its key.
 
 ```typescript
 console.log('Query #5 - Lookup document:');
-let documentResult = await searchClient.getDocument('3')
-console.log(`HotelId: ${documentResult.HotelId}; HotelName: ${documentResult.HotelName}`)
+let documentResult = await searchClient.getDocument('3');
+console.log(`HotelId: ${documentResult.HotelId}; HotelName: ${documentResult.HotelName}`);
 ```
 
 #### Summary of queries
 
-The previous queries show multiple ways of matching terms in a query: full-text search, filters, and autocomplete.
+The previous queries show multiple ways of matching terms in a query: full-text search, filters, and document lookup.
 
-Full text search and filters are performed using the `searchClient.search` method. A search query can be passed in the `searchText` string, while a filter expression can be passed in the `filter` property of the `SearchOptions` class. To filter without searching, just pass "*" for the `searchText` parameter of the `search` method. To search without filtering, leave the `filter` property unset, or don't pass in a `SearchOptions` instance at all.
+The `searchClient.search` method performs full-text search and filters. You can pass a search query in the `searchText` string, while you pass a filter expression in the `filter` property of the `SearchOptions` class. To filter without searching, just pass `"*"` for the `searchText` parameter of the `search` method. To search without filtering, leave the `filter` property unset, or don't pass in a `SearchOptions` instance at all.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptを使用したフルテキスト検索のクイックスタートガイドの改訂"
}
```

### Explanation
このコードの差分は、`full-text-typescript.md` ファイルに関する大規模な更新を示しています。192行が新たに追加され、293行が削除され、合計485行の変更が加えられました。この変更の目的は、TypeScriptを使用したAzure AI Searchのフルテキスト検索のクイックスタートガイドを最新化し、より明確で使いやすい内容にすることです。

修正後の内容では、Azure AI Searchのクライアントライブラリを利用して、検索インデックスを作成し、データをロードし、クエリを実行する手順が詳細に記載されています。全体が整理されて重要な情報が強調され、新たに必要な前提条件や手続きが明示されています。

特に、Azure AI Searchにアクセスするための推奨されるパスワードレス認証や、最新のNode.jsのバージョンに関する情報が強調されています。また、プロジェクトの設定、依存関係のインストール、環境設定がより詳細になり、具体的なコマンドが示されています。

コードセクションでは、TypeScriptとJavaScriptの記法が適切に変換され、分かりやすくなっています。ドキュメントのインデックス作成、データのアップロード、クエリの実行に関する明確な手順と、各段階での重要なポイントが詳しく説明されています。さらに、クエリの結果を表示する方法や、どのようにしてデータを検索できるかが具体的に示されています。

この修正により、ユーザーがAzure AI Searchを活用したフルテキスト検索をスムーズに実装できるようになり、非常に実用的な資源とされています。全体として、コードの説明も親しみやすく、読みやすくなり、フルテキスト検索機能を活用する際に必要な知識を提供していると言えます。

## articles/search/includes/quickstarts/search-get-started-portal-new-wizard.md{#item-114e35}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ The wizard creates multiple objects on your search service, including a searchab
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](../../search-create-service-portal.md). You can use the Free tier for this quickstart.
++ An [Azure AI Search service](../../search-create-service-portal.md). You can use a free service for this quickstart.
 
 + An [Azure Storage account](/azure/storage/common/storage-account-create). Use Azure Blob Storage or Azure Data Lake Storage Gen2 (storage account with a hierarchical namespace) on a standard performance (general-purpose v2) account. To avoid bandwidth charges, use the same region as Azure AI Search.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータルウィザードによる検索の開始に関するガイドの文言修正"
}
```

### Explanation
このコードの差分は、`search-get-started-portal-new-wizard.md` ファイルの軽微な修正を示しています。1行の追加と1行の削除が行われ、合計2行が変更されました。この変更の目的は、文中の表現をより明確にすることです。

変更された内容は、特にAzure AI Searchサービスの使用に関する記述です。元の文章では「Free tier」を使用するとの表現がありましたが、新たに「free service」と修正されています。この簡素な修正により、ユーザーにとって理解しやすい言葉に改善され、Azure AI Searchサービスを利用する際の選択肢が明確になっています。

全体的に、この更新は、特にAzureのサービスを利用する初心者に対してよりフレンドリーなガイダンスを提供し、正確な情報を発信することを目指しています。

## articles/search/includes/quickstarts/search-get-started-vector-python.md{#item-53085f}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,9 @@ In Azure AI Search, a vector index has an index schema that defines vector and n
     
     + To run the semantic hybrid query, you must [enable semantic ranker](../../semantic-how-to-enable-disable.md).
 
-+ [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter package](https://pypi.org/project/jupyter/).
++ The latest version of [Python](https://www.python.org/downloads/).
+
++ [Visual Studio Code](https://code.visualstudio.com/download) with the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions.
 
 + [Git](https://git-scm.com/downloads) to clone the sample repo.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonでのベクトル検索の開始ガイドの前提条件の更新"
}
```

### Explanation
このコードの差分は、`search-get-started-vector-python.md` ファイルに対する小規模な更新を示しています。3行の追加と1行の削除が行われ、合計4行が変更されました。この変更の目的は、Pythonでのベクトル検索を利用するための前提条件を明確にすることです。

具体的には、最新のPythonのバージョンを必須条件として追加し、ユーザーにPythonの更新を促しています。また、Visual Studio Codeの説明も更新され、PythonおよびJupyterの拡張機能のリンクが正確に記載されています。

加えて、Gitを使用してサンプルリポジトリをクローンするための情報も新たに追加されており、これにより、ユーザーが必要な環境を整えやすくなっています。このように、変更後のドキュメントは、ユーザーが作業をスムーズに開始できるような情報を提供しています。全体的に、これらの修正は、特に初心者にとって有益であり、理解しやすさを向上させることに寄与しています。

## articles/search/includes/quickstarts/search-get-started-vector-rest.md{#item-c7d261}

<details>
<summary>Diff</summary>
````diff
@@ -916,7 +916,7 @@ To create a single vector search with a filter:
 
 ### Hybrid search
 
-Hybrid search consists of keyword queries and vector queries in a single search request. This example runs the vector query and full text search concurrently:
+Hybrid search consists of keyword queries and vector queries in a single search request. This example runs the vector query and full-text search concurrently:
 
 + Search string: `historic hotel walk to restaurants and shopping`
 + Vector query string: `quintessential lodging near running trails, eateries, retail` (vectorized into a mathematical representation)
@@ -989,7 +989,7 @@ To create a hybrid search:
     
     Because RRF merges results, it helps to review the inputs individually. 
     
-    The following results are from the full-text portion of the query: *historic hotel walk to restaurants and shopping*. In the full text query, the top three results are Sublime Palace Hotel, Stay-Kay City Hotel, and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score. In the fused query, only two of these matches are in the top 3, and the second match (Stay-Kay City Hotel) doesn't appear in the top 5 at all.
+    The following results are from the full-text portion of the query: *historic hotel walk to restaurants and shopping*. In the full-text query, the top three results are Sublime Palace Hotel, Stay-Kay City Hotel, and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score. In the fused query, only two of these matches are in the top 3, and the second match (Stay-Kay City Hotel) doesn't appear in the top 5 at all.
     
     ```json
       "value": [
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTを使用したベクトル検索のガイド文言修正"
}
```

### Explanation
このコードの差分は、`search-get-started-vector-rest.md` ファイル内の軽微な修正を反映しています。2行の追加と2行の削除が行われ、合計4行が変更されました。この変更の主な目的は、用語の統一感を保つことです。

具体的には、「full text search」という表現が「full-text search」に修正されています。これにより、関連する用語の一貫性が向上し、ユーザーが文書をより理解しやすくなります。また、本文全体において、文章の流れを妨げることなく内容が明確に伝わるよう、文言が調整されています。

特にハイブリッド検索に関するセクションでは、キーワードクエリとベクトルクエリの同時実行について説明されていますが、言葉の使い方が適切に修正されていることで、技術的な内容を扱う文書にふさわしい表現となっています。全体的に、この変更は、文書の専門的な一貫性を高め、ユーザーにとっての利便性を向上させることを目指しています。

## articles/search/includes/resource-authentication.md{#item-381ff1}

<details>
<summary>Diff</summary>
````diff
@@ -1,33 +1,24 @@
 ---
-author: HeidiSteen 
-ms.author: heidist 
+title: Include File
+description: Include file for Azure AI Search authentication and role-based access configuration.
+author: haileytap 
+ms.author: haileytapia 
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/12/2025
+ms.date: 02/02/2026
+# Use this file to describe authentication for search-only, non-integrated scenarios. For managed identities, use resource-authentication-identity.md.
 ---
 
-You need to retrieve the following information to authenticate your application with your Azure AI Search service:
+Before you begin, make sure you have permissions to access content and operations in Azure AI Search. This quickstart uses Microsoft Entra ID for authentication and role-based access for authorization. You must be an **Owner** or **User Access Administrator** to assign roles. If roles aren't feasible, use [key-based authentication](../search-security-api-keys.md) instead.
 
-#### [Microsoft Entra ID](#tab/keyless)
+To configure the recommended role-based access:
 
-|Variable name | Value |
-|--------------------------|-------------|
-| `SEARCH_API_ENDPOINT` | This value can be found in the Azure portal. Select your search service and then from the left menu, select **Overview**. The **Url** value under **Essentials** is the endpoint that you need. An example endpoint might look like `https://mydemo.search.windows.net`. |
+1. [Enable role-based access](../search-security-enable-roles.md) for your search service.
 
-Learn more about [keyless authentication](/azure/search/keyless-connections) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
-
-#### [API key](#tab/api-key)
-
-|Variable name | Value |
-|--------------------------|-------------|
-| `SEARCH_API_ENDPOINT` | This value can be found in the Azure portal. Select your search service and then from the left menu, select **Overview**. The **Url** value under **Essentials** is the endpoint that you need. An example endpoint might look like `https://mydemo.search.windows.net`. |
-| `SEARCH_API_KEY` | This value can be found in the Azure portal. Select your search service and then from the left menu, select **Settings** > **Keys**. You can use either `KEY1` or `KEY2`.|
-
-Learn more about [finding API keys](/azure/search/search-security-api-keys) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
-
-[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
-
----
+1. [Assign the following roles](../search-security-rbac.md) to your user account.
 
+    + **Search Service Contributor**
 
+    + **Search Index Data Contributor**
 
+    + **Search Index Data Reader**
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソース認証に関する文書の改善"
}
```

### Explanation
このコードの差分は、`resource-authentication.md` ファイルの大幅な修正を示しています。13行の追加と22行の削除が行われ、内容が35行変更されました。主な目的は、Azure AI Searchにおける認証と役割ベースのアクセス管理に関する説明を改善することです。

変更の一つの重要な点は、ファイルのタイトルと説明が更新され、現在の内容が明確に反映されるようになったことです。また、以前のセクションは削除され、新しい情報が追加されています。具体的には、Microsoft Entra IDを使った認証と、役割ベースのアクセス管理の設定についての手順が強調されています。

更新された内容では、ユーザーに必要な権限について説明し、役割ベースのアクセスを有効にする手順が具体的に示されています。その中では、特定の役割（Search Service Contributor、Search Index Data Contributor、Search Index Data Reader）をユーザーアカウントに割り当てる方法についても触れられています。

この変更により、ユーザーが認証とアクセス管理の設定をより容易に行えるようになり、全体として文書の分かりやすさと実用性が向上しました。

## articles/search/includes/resource-cleanup-free.md{#item-99ba27}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,16 @@
+---
+title: Include File
+description: Include file for cleaning up Azure AI Search resources on the free tier.
+author: haileytap 
+ms.author: haileytapia 
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 02/02/2026
+# Use this file for quickstarts that only use a free search service.
+---
+
+When you work in your own subscription, it's a good idea to finish a project by removing the resources you no longer need. Resources that are left running can cost you money.
+
+In the Azure portal, select **All resources** or **Resource groups** from the left pane to find and manage resources. You can delete resources individually or delete the resource group to remove all resources at once.
+
+If you're using a free search service, remember that you're limited to three indexes, indexers, and data sources. You can [delete individual items](../search-how-to-manage-index.md) in the portal to stay under the limit.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "無料プラン向けのAzure AI Searchリソースクリーンアップガイドの追加"
}
```

### Explanation
このコードの差分は、`resource-cleanup-free.md` という新しいファイルの追加を示しています。このファイルは、Azure AI Searchの無料プランを利用しているユーザー向けに、不要なリソースのクリーンアップに関するガイドを提供しています。新たに16行が追加され、リソース管理の重要性と手順について説明されています。

具体的には、Azureポータルを通じて不要なリソースを効果的に削除する方法が説明されており、ユーザーがコストを削減するためにプロジェクトを完了する際のベストプラクティスが示されています。特に、リソースグループを使用して複数のリソースを一度に削除する方法や、無料プランにおける制限（インデックス、インデクサ、データソースの数）についても触れられています。

この新しいファイルは、ユーザーが無料プランを利用する際に役立つ具体的な手順と注意点を提供し、リソース管理の効率性を向上させる一助となることを目的としています。全体として、無料プランでのリソース管理を理解しやすくするための重要な資料となっています。

## articles/search/includes/resource-cleanup-paid.md{#item-a9aef4}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,14 @@
+---
+title: Include File
+description: Include file for cleaning up Azure AI Search resources on paid tiers.
+author: haileytap 
+ms.author: haileytapia 
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 02/02/2026
+# Use this file for quickstarts that require billable services.
+---
+
+When you work in your own subscription, it's a good idea to finish a project by removing the resources you no longer need. Resources that are left running can cost you money.
+
+In the Azure portal, select **All resources** or **Resource groups** from the left pane to find and manage resources. You can delete resources individually or delete the resource group to remove all resources at once.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "有料プラン向けのAzure AI Searchリソースクリーンアップガイドの追加"
}
```

### Explanation
このコードの差分は、`resource-cleanup-paid.md` という新しいファイルの追加を示しています。このファイルは、Azure AI Searchの有料プランを使用するユーザーに向けて、不要なリソースをクリーンアップする方法を説明したガイドです。この新しい文書では、14行が追加されています。

内容には、ユーザーが自分のサブスクリプションでプロジェクトを終了する際に不要なリソースを削除することの重要性が強調されています。特に、動作中のリソースはコストが発生する可能性があるため、適切に管理することが求められます。

Azureポータルを利用して、リソースを個別に削除する方法や、リソースグループを使用してすべてのリソースを一度に削除する手段が示されています。この情報は、有料プラン利用者が費用を適切に管理し、無駄を省くための具体的な手助けとなります。

全体的に、この新しいファイルは、有料プランの利用者に向けた有益なリソース管理の情報を提供し、プロジェクトの整理整頓に役立つ内容となっています。

## articles/search/includes/resource-endpoint.md{#item-2b31be}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,20 @@
+---
+title: Include File
+description: Include file for getting the endpoint of an Azure AI Search service.
+author: haileytap 
+ms.author: haileytapia 
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 02/02/2026
+---
+
+Each Azure AI Search service has an *endpoint*, which is a unique URL that identifies and provides network access to the service. In a later section, you specify this endpoint to connect to your search service programmatically.
+
+To get the endpoint:
+
+1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
+
+1. From the left pane, select **Overview**.
+
+1. Make a note of the endpoint, which should look like `https://my-service.search.windows.net`.
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Searchサービスのエンドポイント取得ガイドの追加"
}
```

### Explanation
このコードの差分は、`resource-endpoint.md` という新しいファイルの追加を示しています。このファイルは、Azure AI Searchサービスのエンドポイントを取得する方法についてのガイドを提供しており、合計で20行が追加されています。

新たに追加された内容では、各Azure AI Searchサービスには独自のエンドポイントがあり、それがネットワークアクセスを提供するために必要なURLであることが説明されています。このエンドポイントはプログラムから検索サービスに接続する際に使用されます。

エンドポイントを取得する手順も詳細に記載されており、以下の手順が含まれています：
1. Azureポータルにサインインし、検索サービスを選択します。
2. 左側のペインから「概要」を選択します。
3. エンドポイントをメモします。このエンドポイントは通常 `https://my-service.search.windows.net` の形式を取ります。

この新しいガイドにより、ユーザーはAzure AI Searchサービスに接続するための重要なエンドポイント情報を簡単に取得できるようになります。全体として、ユーザーがサービスを円滑に利用するための有益なリソースとなっています。

## articles/search/search-create-app-portal.md{#item-19ab44}

<details>
<summary>Diff</summary>
````diff
@@ -118,11 +118,7 @@ To finish the wizard and use the demo app:
 
 ## Clean up resources
 
-When you work in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-In the Azure portal, you can find and manage resources by selecting **All resources** or **Resource groups** from the left pane.
-
-Remember that a free search service is limited to three indexes, three indexers, and three data sources. To stay under the limit, you can delete these items individually in the Azure portal.
+[!INCLUDE [clean up resources (free)](includes/resource-cleanup-free.md)]
 
 ## Next step
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースのクリーンアップセクションの更新"
}
```

### Explanation
このコードの差分は、`search-create-app-portal.md`というファイルの修正を示しています。変更内容としては、1行の追加と5行の削除があり、合計で6行が変更されています。

修正された部分は、「リソースのクリーンアップ」セクションに関連しています。元々は、ユーザーが自分のサブスクリプション内でプロジェクト終了時に不要なリソースを識別し、削除する重要性について詳しく説明されていました。この内容は削除され、代わりにリソースクリーンアップに関するリンクが追加されました。

具体的には、`[!INCLUDE [clean up resources (free)](includes/resource-cleanup-free.md)]`というマクロが追加され、無料の検索サービスを利用しているユーザー向けのリソースクリーンアップガイドが参照されるようになりました。この変更により、情報が一元化され、ユーザーは必要に応じて関連するドキュメントにアクセスできるようになります。

全体として、この更新は文書の簡潔さを保ちながら、必要なリソース管理情報を効率的に提供するための調整と言えます。

## articles/search/search-explorer.md{#item-738774}

<details>
<summary>Diff</summary>
````diff
@@ -195,11 +195,7 @@ In this quickstart, you used **Search explorer** to query an index using the RES
 
 ## Clean up resources
 
-When you work in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-In the Azure portal, you can find and manage resources by selecting **All resources** or **Resource groups** from the left pane.
-
-Remember that a free search service is limited to three indexes, three indexers, and three data sources. To stay under the limit, you can delete these items individually in the Azure portal.
+[!INCLUDE [clean up resources (free)](includes/resource-cleanup-free.md)]
 
 ## Next step
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースのクリーンアップセクションの更新"
}
```

### Explanation
このコードの差分は、`search-explorer.md`というファイルの修正を示しています。変更内容には、1行の追加と5行の削除が含まれており、合計で6行の変更が行われています。

変更された部分は、「リソースのクリーンアップ」セクションに関する内容です。以前は、プロジェクト終了時に不要なリソースを識別し、削除する重要性が説明されていましたが、その具体的な説明は削除されました。代わりに、リソースのクリーンアップに関する外部ドキュメントへのリンクが追加されました。

具体的には、`[!INCLUDE [clean up resources (free)](includes/resource-cleanup-free.md)]`というマクロが追加されています。これにより、無料の検索サービスを利用しているユーザー向けのリソースクリーンアップガイドが別の文書として参照される形になりました。この変更は、情報の整理を図り、ユーザーがより効率的にリソース管理の情報を取得できるようにすることを目的としています。

全体として、この更新は文書の一貫性を保ちながら、より効果的な情報提供を目指した修正であると言えます。

## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -469,7 +469,7 @@ To query your multimodal index:
 
 ## Clean up resources
 
-This quickstart uses billable Azure resources. If you no longer need the resources, delete them from your subscription to avoid charges.
+[!INCLUDE [clean up resources (paid)](includes/resource-cleanup-paid.md)]
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースのクリーンアップセクションのリンク更新"
}
```

### Explanation
このコードの差分は、`search-get-started-portal-image-search.md`というファイルの修正を示しています。変更内容は、1行の追加と1行の削除があり、合計で2行の変更が行われました。

具体的には、「リソースのクリーンアップ」セクションの内容が更新されました。以前は、プロジェクトに使用する課金対象のAzureリソースについて、不要な場合はサブスクリプションから削除して料金が発生しないようにすることが勧められていました。この説明が削除され、その代わりに、課金対象のリソースのクリーンアップに関する外部ドキュメントへのリンクが追加されました。

追加された内容は、`[!INCLUDE [clean up resources (paid)](includes/resource-cleanup-paid.md)]`というマクロです。この変更により、ユーザーは関連するリソース管理のガイドラインに直接アクセスできるようになります。 

この修正は、情報の集約と整合性を向上させることを目的としており、ユーザーが必要な情報を簡単に見つけられるようになる利点があります。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -601,7 +601,7 @@ To query your vector index:
 
 ## Clean up resources
 
-This quickstart uses billable Azure resources. If you no longer need the resources, delete them from your subscription to avoid charges.
+[!INCLUDE [clean up resources (paid)](includes/resource-cleanup-paid.md)]
 
 ## Next step
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースのクリーンアップセクションのリンク更新"
}
```

### Explanation
このコードの差分は、`search-get-started-portal-import-vectors.md`というファイルの修正を示しています。変更内容は、1行の追加と1行の削除があり、合計で2行の変更が行われました。

具体的には、「リソースのクリーンアップ」セクションにおける内容が更新されています。従来の説明では、課金対象のAzureリソースを使用している場合、不要なリソースをサブスクリプションから削除することで料金が発生しないようにすることが勧められていました。その文が削除され、その代わりに、課金対象のリソースのクリーンアップに関する外部ドキュメントへのリンクが追加されています。

新たに追加された内容は、`[!INCLUDE [clean up resources (paid)](includes/resource-cleanup-paid.md)]`というマクロで、これにより、ユーザーは関連するリソース管理のガイドラインにアクセスしやすくなります。

この変更は、情報を整理し、ユーザーが必要な情報を効率よく取得できるようにすることを目的としています。

## articles/search/search-get-started-portal.md{#item-6d0cb1}

<details>
<summary>Diff</summary>
````diff
@@ -149,12 +149,7 @@ Take a minute to try these example queries on your index. For more information,
 
 ## Clean up resources
 
-When you work in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-In the Azure portal, you can find and manage resources by selecting **All resources** or **Resource groups** from the left pane.
-
-> [!NOTE]
-> If you're using a free search service, remember that the limit is three indexes, three indexers, and three data sources. You can delete individual objects in the Azure portal to stay under the limit.
+[!INCLUDE [clean up resources (free)](includes/resource-cleanup-free.md)]
 
 ## Next step
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースのクリーンアップセクションのリンク更新"
}
```

### Explanation
このコードの差分は、`search-get-started-portal.md`というファイルの変更を示しています。変更は、1行の追加と6行の削除があり、合計で7行の変更が行われました。

具体的には、「リソースのクリーンアップ」セクションの内容が更新されました。以前の説明では、プロジェクトの終了時に作成したリソースがまだ必要かどうかを判断し、不要なリソースを削除することが推奨されていました。また、Azureポータルでリソースを管理する方法についての詳細と、無料の検索サービスの制限に関する注意書きも含まれていました。

これらの詳細は削除され、その代わりに、無料プランのリソースクリーンアップに関する外部ドキュメントへのリンクが追加されました。この更新により、ユーザーは最新の情報に基づいてリソースを簡単に管理できるようになります。

追加された内容は、`[!INCLUDE [clean up resources (free)](includes/resource-cleanup-free.md)]`というもので、ユーザーが必要なガイダンスを効果的に得ることができる利点があります。

この変更は、情報を明確かつ効率的に提供するための調整として位置づけられます。

## articles/search/search-get-started-semantic.md{#item-2b3902}

<details>
<summary>Diff</summary>
````diff
@@ -55,9 +55,7 @@ zone_pivot_groups: search-get-started-semantic
 
 ## Clean up resources
 
-When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-You can find and manage resources in the Azure portal, using the **All resources** or **Resource groups** link in the left-navigation pane.
+[!INCLUDE [clean up resources (paid)](includes/resource-cleanup-paid.md)]
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースのクリーンアップセクションのリンク更新"
}
```

### Explanation
このコードの差分は、`search-get-started-semantic.md`というファイルの修正を示しています。変更は、1行の追加と3行の削除があり、合計で4行の変更が行われました。

変更の内容としては、「リソースのクリーンアップ」セクションが更新され、以前はプロジェクト終了時に作成したリソースの必要性を判断し、不要なリソースを削除することが推奨されていました。この旨の具体的な手順や、Azureポータルでリソースを管理する方法が説明されていましたが、それらの詳細は削除されました。

その代わりに、課金対象のリソースのクリーンアップに関する外部のドキュメントへのリンクが追加されました。この新しい内容は、`[!INCLUDE [clean up resources (paid)](includes/resource-cleanup-paid.md)]`というマクロで表現されています。

この変更により、ユーザーは最新のリソース管理に関する情報を簡単に参照できるようになり、より効率的なリソースのクリーンアップが可能となります。全体として、この更新は情報の明確性を向上させることを目的としています。

## articles/search/search-get-started-skillset.md{#item-079744}

<details>
<summary>Diff</summary>
````diff
@@ -229,11 +229,7 @@ Finally, you learned that you can verify content by querying the index. Ultimate
 
 ## Clean up resources
 
-When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-You can find and manage resources in the Azure portal by selecting **All resources** or **Resource groups** from the left pane.
-
-If you used a free service, remember that you're limited to three indexes, indexers, and data sources. You can delete individual items in the Azure portal to stay under the limit. 
+[!INCLUDE [clean up resources (free)](includes/resource-cleanup-free.md)]
 
 ## Next step
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースのクリーンアップセクションのリンク更新"
}
```

### Explanation
このコードの差分は、`search-get-started-skillset.md`というファイルに対する変更を示しています。今回の変更では、1行が追加され、5行が削除され、合計で6行の変更が行われました。

具体的には、「リソースのクリーンアップ」セクションが修正されました。以前は、プロジェクトの終了時に作成したリソースの必要性を評価し、不要に残しているリソースがある場合は削除することが推奨されていました。このセクションでは、Azureポータルでのリソース管理方法と、無料サービスの制限についても言及されていました。

しかし、これらの具体的な手順や詳細は削除され、その代わりに、無料プランでのリソースクリーンアップに関する外部ドキュメントへのリンクが追加されました。新しい内容は、`[!INCLUDE [clean up resources (free)](includes/resource-cleanup-free.md)]`という形式です。

この更新によって、ユーザーはリソース管理に関する最新の情報を迅速に参照でき、効率的にリソースを管理できるようになります。全体として、この変更は情報の簡素化と明確化を目的としています。

## articles/search/search-get-started-text.md{#item-935941}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.custom:
   - ignite-2023
 ms.topic: quickstart
 zone_pivot_groups: search-quickstart-full-text
-ms.date: 11/20/2025
+ms.date: 02/02/2026
 ---
 
 # Quickstart: Full-text search
@@ -64,11 +64,7 @@ ms.date: 11/20/2025
 
 ## Clean up resources
 
-When working in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money. You can delete resources individually, or you can delete the resource group to delete the entire set of resources.
-
-In the [Azure portal](https://portal.azure.com/), you can find and manage resources by selecting **All resources** or **Resource groups** from the left pane.
-
-If you're using a free service, remember that you're limited to three indexes, indexers, and data sources. You can delete individual items in the Azure portal to stay under the limit.
+[!INCLUDE [clean up resources (free)](includes/resource-cleanup-free.md)]
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新およびリソースのクリーンアップリンクの修正"
}
```

### Explanation
このコードの差分は、`search-get-started-text.md`というファイルの変更を示しています。変更には2行の追加と6行の削除があり、合計で8行の変更が記録されています。

具体的には、最初の変更はメタデータの一部で、`ms.date`フィールドが2025年11月20日から2026年2月2日に更新されました。これは、ドキュメントの日付を最新のものにするための調整です。

次に、「リソースのクリーンアップ」セクションが修正されました。このセクションでは、プロジェクト終了時に作成したリソースの必要性を確認し、不要なリソースを削除することが推奨されていますが、以前の具体的な手順は削除されました。その代わり、無料プランのリソースクリーンアップに関する外部ドキュメントへのリンクが新しく追加されました。新しい内容は、`[!INCLUDE [clean up resources (free)](includes/resource-cleanup-free.md)]`という形式です。

この変更により、ユーザーは最新の情報を参照しやすくなり、効率的にリソースを管理できるようになります。また、日付の更新はドキュメントの鮮度を保つためにも重要です。全体として、この変更は情報の明確性と信頼性を向上させることを目的としています。

## articles/search/search-how-to-integrated-vectorization.md{#item-86fb1e}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ This article describes the end-to-end workflow for [integrated vectorization](ve
 
 + Completion of [Quickstart: Connect without keys](search-get-started-rbac.md) and [Configure a system-assigned managed identity](search-how-to-managed-identities.md#create-a-system-managed-identity). Although you can use key-based authentication for data plane operations, this article assumes [roles and managed identities](#role-based-access), which are more secure.
 
-+ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)<!--or the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter package](https://pypi.org/project/jupyter/)-->.
++ [Visual Studio Code](https://code.visualstudio.com/download) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)<!--or Python prerequisites-->.
 
 ### Supported data sources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTクライアントの拡張機能に関する説明の修正"
}
```

### Explanation
このコードの差分は、`search-how-to-integrated-vectorization.md`というファイルに対する変更を示しています。変更には1行の追加と1行の削除があり、合計で2行の変更が記録されています。

今回の変更は、記事内の説明部分に関するもので、特にVisual Studio Codeに関する言及が修正されました。以下が具体的な変更内容です：

1. **追加された説明**: 記事に、"[Quickstart: Connect without keys](search-get-started-rbac.md)"および"[Configure a system-assigned managed identity](search-how-to-managed-identities.md#create-a-system-managed-identity)"を完了することが推奨されている旨の新しい行が追加されました。この変更によって、ユーザーが記事を理解する上で必要な前提条件が明確になりました。

2. **RESTクライアントの説明の修正**: Visual Studio Codeを使用することを推奨する部分について、元の記載は「REST client」としていたところを「REST Client extension」と変更しました。これにより、より具体的に拡張機能としての利用を促進しています。

全体として、これらの修正は、ユーザーに対する情報の明確さを増し、作業を進める上での障壁を減らすことを目的としています。

## articles/search/tutorial-adls-gen2-indexer-acls.md{#item-6881a0}

<details>
<summary>Diff</summary>
````diff
@@ -41,7 +41,7 @@ Use a REST client to complete this tutorial and the [latest preview REST API](/r
 
 + [Azure AI Search](search-create-service-portal.md), any region. Basic tier or higher is required for managed identity support.
 
-+ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) or a [Python client](https://code.visualstudio.com/docs/languages/python) and [Jupyter package](https://pypi.org/project/jupyter/).
++ [Visual Studio Code](https://code.visualstudio.com/download) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
 ## Prepare sample data
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTクライアントの拡張機能に関する説明の修正"
}
```

### Explanation
このコードの差分は、`tutorial-adls-gen2-indexer-acls.md`というファイルに対する変更を示しています。変更内容は、1行の追加と1行の削除があり、合計で2行の変更が記録されています。

具体的な変更内容は以下の通りです：

1. **RESTクライアントの説明の修正**: 記事内でVisual Studio Codeを使用する際の推奨構成についての説明が更新され、元々は「REST client」と記載されていた部分が具体的に「REST Client extension」と修正されました。これにより、ユーザーに対して、どの拡張機能を使用するべきかが明確になります。

2. **前提条件の明記**: また、Azure AI Searchに関する記載も追加され、管理されたアイデンティティのサポートにはBasic tierまたはそれ以上が必要であることが強調されています。

全体として、これらの修正は、ユーザーの作業に必要な情報をより明確にし、直接的に役立つリソースを示すことを意図しています。これにより、チュートリアルを完了するための理解が深まり、ユーザーの体験が向上します。


