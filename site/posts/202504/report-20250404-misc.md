---
date: '2025-04-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b48656b...MicrosoftDocs:a4ad9b8
summary: この差分では、Document Intelligenceおよび関連コンテンツのドキュメントに対してマイナーアップデートが行われました。新バージョンのサポートや新機能の追加につれて、ユーザーは最新の情報を基に設定を行いやすくなり、エンティティカテゴリの構造修正により情報の可視性も向上しました。具体的には、Document
  Intelligence v4.0のサポート開始やAPIリンクの追加が行われ、全体として情報の整理と可視化が進められています。この更新により、技術者やユーザーはより効果的にサービスを利用できるようになることが期待されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b48656b...MicrosoftDocs:a4ad9b8){target="_blank"}

<format>
# ハイライト
この差分では、Document Intelligenceおよび関連コンテンツのドキュメントに対してのマイナーアップデートが行われました。主に新バージョンをサポートする情報や新機能の追加によって、ユーザーは最新の情報を基に設定を行うことが可能になります。また、エンティティカテゴリの構造修正により情報の可視性が向上しました。

## 新機能
- Document Intelligence v4.0のサポート開始。
- REST APIやクライアントライブラリへのリンクの追加。

## 破壊的変更
- 特に大きな破壊的変更はありませんが、モニカーの適用範囲が変更されています。

## その他の更新
- エンティティカテゴリのドキュメントでの構造が修正され、見やすくなりました。
- サポートされるバージョン情報の更新。

# インサイト
この差分は、Document Intelligenceのコンテナに関する情報を最新化し、ユーザーが最も新しいバージョンを適切に利用しやすくするために行われた更新です。Document Intelligence v4.0について特に多くの情報が追加され、2024年11月30日のバージョンサポートが強調されました。このことは、コンテナを活用する企業や開発者にとって、最新の技術を用いたサービス提供・開発の計画が容易になることを意味します。

さらに、エンティティカテゴリの構造修正では、情報の整理と可視化向上が行われており、これによりユーザーは必要な情報を迅速に取得することができます。この更新により、Document Intelligenceや言語サービスをより効果的に活用するための基盤が整備されており、技術者やユーザーの体験の質を向上させることが期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [configuration.md](#item-e17282) | minor update | コンテナの設定に関する最新情報の更新 | modified | 12 | 5 | 17 | 
| [disconnected.md](#item-c70d0b) | minor update | オフライン環境におけるコンテナ設定の更新 | modified | 7 | 5 | 12 | 
| [image-tags.md](#item-6a7764) | minor update | コンテナのイメージタグに関する情報の更新 | modified | 22 | 5 | 27 | 
| [whats-new.md](#item-1ec8d3) | minor update | Document Intelligence v4.0に関する最新情報の追加 | modified | 7 | 0 | 7 | 
| [entity-categories.md](#item-ba2623) | minor update | エンティティカテゴリの構造の修正 | modified | 2 | 1 | 3 | 


# Modified Contents
## articles/ai-services/document-intelligence/containers/configuration.md{#item-e17282}

<details>
<summary>Diff</summary>
````diff
@@ -14,25 +14,32 @@ ms.author: lajanuar
 
 # Configure Document Intelligence containers
 
-:::moniker range="doc-intel-2.1.0 || doc-intel-4.0.0"
+:::moniker range="doc-intel-2.1.0"
 
-Document Intelligence doesn't support containers for v4.0. Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models and `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt, and ID Document models:
+Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models, `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt, and ID Document models, and `2024-11-30 (GA)` for Layout model:
 
 * [REST API `2022-08-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
 * [REST API `2023-07-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.1%20(2023-07-31)&tabs=HTTP&preserve-view=true)
+* [REST API `2024-11-30 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v4.0%20(2024-11-30)&tabs=HTTP&preserve-view=true)
 * [Client libraries targeting `REST API 2022-08-31 (GA)`](../sdk-overview-v3-0.md)
 * [Client libraries targeting `REST API 2023-07-31 (GA)`](../sdk-overview-v3-1.md)
+* [Client libraries targeting `REST API 2024-11-30 (GA)`](../sdk-overview-v4-0.md)
 
-✔️ See [**Configure Document Intelligence v3.0 containers**](?view=doc-intel-3.0.0&preserve-view=true) or [**Configure Document Intelligence v3.1 containers**](?view=doc-intel-3.1.0&preserve-view=true) for supported versions of container documentation.
+
+✔️ See [**Configure Document Intelligence v3.0 containers**](?view=doc-intel-3.0.0&preserve-view=true) or [**Configure Document Intelligence v3.1 containers**](?view=doc-intel-3.1.0&preserve-view=true) or [**Configure Document Intelligence v4.0 containers**](?view=doc-intel-4.0.0&preserve-view=true) for supported versions of container documentation.
 
 :::moniker-end
 
-:::moniker range="doc-intel-3.0.0 || doc-intel-3.1.0"
+:::moniker range=">=doc-intel-3.0.0"
 
-**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** ![checkmark](../media/yes-icon.png) **v3.1 (GA)**
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** ![checkmark](../media/yes-icon.png) **v4.0 (GA)**
 
 With Document Intelligence containers, you can build an application architecture optimized to take advantage of both robust cloud capabilities and edge locality. Containers provide a minimalist, isolated environment that can be easily deployed on-premises and in the cloud. In this article, we show you how to configure the Document Intelligence container run-time environment by using the `docker compose` command arguments. Document Intelligence features are supported by seven Document Intelligence feature containers—**Read**, **Layout**, **Business Card**,**ID Document**,  **Receipt**, **Invoice**, **Custom**. These containers have both required and optional settings. For a few examples, see the [Example docker-compose.yml file](#example-docker-composeyml-file) section.
 
+> [!IMPORTANT]
+>
+> Document Intelligence v4.0 container is currently available for Layout model only.
+
 ## Configuration settings
 
 Each container has the following configuration settings:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテナの設定に関する最新情報の更新"
}
```

### Explanation
この変更では、Document Intelligence コンテナに関する設定を更新しています。具体的には、サポートされるバージョンに関する情報が追加され、メモリに保持される情報に関して、最新の情報が反映されました。

以下に主要な変更点を示します：
- ドキュメントに記載されているサポート対象バージョンが更新され、2024年11月30日のバージョンが追加されました。
- 新しいバージョンにおける REST API とクライアントライブラリへのリンクも追加されました。
- 記述しているモニカの範囲が変更され、より広範なバージョンに適応できるように改善されました。

また、新しいバージョンのコンテナ情報として、バージョン 4.0 に関する重要な注意点も追加されています。この更新により、ユーザーは最新の情報に基づいてDocumentation Intelligence のコンテナを適切に設定できるようになります。

## articles/ai-services/document-intelligence/containers/disconnected.md{#item-c70d0b}

<details>
<summary>Diff</summary>
````diff
@@ -13,22 +13,24 @@ ms.author: lajanuar
 
 # Containers in disconnected (offline) environments
 
-:::moniker range="doc-intel-2.1.0 || doc-intel-4.0.0"
+:::moniker range="doc-intel-2.1.0"
 
-Document Intelligence doesn't support containers for v4.0. Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models and `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt, and ID Document models:
+Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models and `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt, and ID Document models, and `2024-11-30 (GA)` for Layout model:
 
 * [REST API `2022-08-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
 * [REST API `2023-07-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.1%20(2023-07-31)&tabs=HTTP&preserve-view=true)
+* [REST API `v4.0: 2024-11-30 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v4.0%20(2024-11-30)&tabs=HTTP&preserve-view=true)
 * [Client libraries targeting `REST API 2022-08-31 (GA)`](../sdk-overview-v3-0.md)
 * [Client libraries targeting `REST API 2023-07-31 (GA)`](../sdk-overview-v3-1.md)
+* [Client libraries targeting `REST API v4.0: 2024-11-30 (GA)`](../sdk-overview-v4-0.md)
 
-✔️ See [**Document Intelligence v3.0 containers in disconnected environments**](?view=doc-intel-3.0.0&preserve-view=true) or [**Document Intelligence v3.1 containers in disconnected environments**](?view=doc-intel-3.1.0&preserve-view=true) for supported versions of container documentation.
+✔️ See [**Document Intelligence v3.0 containers in disconnected environments**](?view=doc-intel-3.0.0&preserve-view=true) or [**Document Intelligence v3.1 containers in disconnected environments**](?view=doc-intel-3.1.0&preserve-view=true) or [**Document Intelligence v4.0 containers in disconnected environments**](?view=doc-intel-4.0.0&preserve-view=true) for supported versions of container documentation.
 
 :::moniker-end
 
-:::moniker range="doc-intel-3.0.0 || doc-intel-3.1.0"
+:::moniker range=">=doc-intel-3.0.0"
 
-**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** ![checkmark](../media/yes-icon.png) **v3.1 (GA)**
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** ![checkmark](../media/yes-icon.png) **v4.0 (GA)**
 
 ## What are disconnected containers?
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オフライン環境におけるコンテナ設定の更新"
}
```

### Explanation
この変更では、オフライン環境におけるDocument Intelligence コンテナの設定に関する情報が更新されました。主に、サポートされるバージョン情報の追加と、モニカーの範囲の修正が行われています。

具体的な変更点は次の通りです：
- 文書内に新たに追加されたバージョンとして、2024年11月30日のLayoutモデルに関するサポートが明示されました。
- 新しいREST APIおよびクライアントライブラリへのリンクが追加され、ユーザーが最新の情報にアクセスできるようになっています。
- モニカー範囲が現在のバージョンに応じてより柔軟に設定され、バージョン3.0以降すべてに対応するよう改訂されています。

これにより、ユーザーはDocument Intelligenceのオフライン環境でのコンテナ設定に関して、より包括的な理解を得ることができるようになります。この更新は、特に新しいバージョンを利用するユーザーにとって重要です。

## articles/ai-services/document-intelligence/containers/image-tags.md{#item-6a7764}

<details>
<summary>Diff</summary>
````diff
@@ -14,16 +14,18 @@ ms.author: lajanuar
 
 <!-- markdownlint-disable MD051 -->
 
-:::moniker range="doc-intel-2.1.0 || doc-intel-4.0.0"
+:::moniker range="doc-intel-2.1.0"
 
-Document Intelligence doesn't support containers for v4.0. Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models and `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt, and ID Document models:
+Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models, `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt, and ID Document models, and `2024-11-30 (GA)` for Layout model:
 
 * [REST API `2022-08-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
 * [REST API `2023-07-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.1%20(2023-07-31)&tabs=HTTP&preserve-view=true)
+* [REST API `2024-11-30 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v4.0%20(2024-11-30)&tabs=HTTP&preserve-view=true)
 * [Client libraries targeting `REST API 2022-08-31 (GA)`](../sdk-overview-v3-0.md)
 * [Client libraries targeting `REST API 2023-07-31 (GA)`](../sdk-overview-v3-1.md)
+* [Client libraries targeting `REST API 2024-11-30 (GA)`](../sdk-overview-v4-0.md)
 
-✔️ See [**Document Intelligence v3.0 container image tags**](?view=doc-intel-3.0.0&preserve-view=true) or [**Document Intelligence v3.1 container image tags**](?view=doc-intel-3.1.0&preserve-view=true) for supported versions of container documentation.
+✔️ See [**Document Intelligence v3.0 container image tags**](?view=doc-intel-3.0.0&preserve-view=true) or [**Document Intelligence v3.1 container image tags**](?view=doc-intel-3.1.0&preserve-view=true) or [**Document Intelligence v4.0 container image tags**](?view=doc-intel-4.0.0&preserve-view=true) for supported versions of container documentation.
 
 :::moniker-end
 
@@ -72,11 +74,26 @@ The following containers support DocumentIntelligence v3.1 models and features:
 
 ::: moniker-end
 
+::: moniker range="doc-intel-4.0.0"
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v4.0 (GA)**
+
+## Microsoft container registry (MCR)
+
+Document Intelligence container images can be found within the [**Microsoft Artifact Registry** (also know as Microsoft Container Registry(MCR))](https://mcr.microsoft.com/catalog?search=document%20intelligence), the primary registry for all Microsoft published container images.
+
+The following containers support DocumentIntelligence v3.1 models and features:
+
+| Container name |image |
+|---|---|
+| [**Layout 4.0**](https://mcr.microsoft.com/en-us/product/azure-cognitive-services/form-recognizer/layout-4.0/tags) |`mcr.microsoft.com/azure-cognitive-services/form-recognizer/layout-4.0:latest`|
+::: moniker-end
+
+
 :::moniker range="doc-intel-2.1.0"
 
 > [!IMPORTANT]
 >
-> Document Intelligence v3.0 containers are now generally available. If you are getting started with containers, consider using the v3 containers.
+> Document Intelligence v3.0 containers are now generally available. If you're getting started with containers, consider using the v3 containers.
 The following containers:
 
 ## Feature containers
@@ -100,4 +117,4 @@ Document Intelligence containers support the following features:
 
 > [!div class="nextstepaction"]
 > [Install and run Document Intelligence containers](install-run.md)
-:::moniker-end
\ No newline at end of file
+:::moniker-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテナのイメージタグに関する情報の更新"
}
```

### Explanation
この変更により、Document Intelligence コンテナのイメージタグに関する情報が更新されました。具体的には、サポートされるバージョンの追加や、Microsoftコンテナレジストリに関する詳細が含まれています。

主な変更点は以下の通りです：
- 新しいバージョン2024年11月30日のLayoutモデルに関するサポートが明示され、関連するREST APIおよびクライアントライブラリへのリンクが追加されました。
- Document IntelligenceのコンテナイメージはMicrosoft Artifact Registry（MCR）で見つけられるという情報が追加され、コンテナイメージの検索に便利なリンクも提供されています。
- v4.0に関する内容が新しく追加され、v4.0 (GA)が利用可能であることが示されています。
- テーブル形式で、Layout 4.0のイメージタグが明示されることで、利用者は必要なコンテナ情報を簡単に確認できるようになっています。

これにより、ユーザーはDocument Intelligenceの最新のコンテナ設定に関する情報に簡単にアクセスできるようになり、利便性が向上しました。

## articles/ai-services/document-intelligence/whats-new.md{#item-1ec8d3}

<details>
<summary>Diff</summary>
````diff
@@ -27,6 +27,13 @@ Document Intelligence service is updated on an ongoing basis. Bookmark this page
 > [!IMPORTANT]
 > Preview API versions are retired once the GA API is released. The 2023-02-28-preview API version is retiring. If you're still using the preview API or the associated SDK versions, update your code to target the latest API version `2024-11-30 (GA)`. </br>
 
+## April 2025
+**Document Intelligence v4.0 container is now available! Currently, Layout model is the only supported model for v4.0 release.**
+<br>
+For more information, *see:*
+* [Install and run containers](containers/install-run.md?view=doc-intel-4.0.0&preserve-view=true)
+* [Container image tags](containers/image-tags.md?view=doc-intel-4.0.0&preserve-view=true)
+
 ## December 2024
 
 **Document Intelligence v4.0 programming language SDKs are now generally available (GA)**! <br><br>The latest client libraries default to the [**2024-11-30 REST API (GA)**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) version of the service.<br><br>
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence v4.0に関する最新情報の追加"
}
```

### Explanation
この変更では、Document Intelligenceに関する最新情報が追加され、特にv4.0のリリースに関する詳細が記載されています。具体的には、2025年4月にDocument Intelligence v4.0のコンテナが利用可能になったことが伝えられており、現在はLayoutモデルのみがサポートされていることが強調されています。

さらに、以下の情報が追加されています：
- Document Intelligence v4.0に基づくコンテナのインストールおよび実行に関するリンクが提供され、ユーザーが最新のコンテナを利用する際の手引きが示されています。
- コンテナのイメージタグに関するページへのリンクも含まれ、ユーザーは必要な情報を簡単に確認できるようになっています。

この更新により、ユーザーはDocument Intelligenceの最新バージョンとその機能についての理解を深めることができ、特に新しいv4.0リリースに対するデモや実装に役立つリソースにアクセスしやすくなっています。

## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories.md{#item-ba2623}

<details>
<summary>Diff</summary>
````diff
@@ -399,7 +399,8 @@ The entity in this category can have the following subcategories.
       **Supported languages**
       
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      
+      :::column-end:::
+:::row-end:::
 ## Subcategory: Age
 
 The PII service supports the Age subcategory within the broader Quantity category (since Age is the personally identifiable piece of information). 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティカテゴリの構造の修正"
}
```

### Explanation
この変更では、エンティティカテゴリに関するドキュメントの構造が修正されました。具体的には、サポートされる言語のリストの表示方法が改善されています。

主な変更点は以下の通りです：
- サポートされる言語のリストに関するセクションが整形され、視覚的に見やすくなるよう、コラムと行の終端を示すマークアップが追加されました。この変更により、情報がより整理された形で表示され、ユーザーはサポートされている言語を把握しやすくなりました。
- 「年齢」というサブカテゴリに関する文も引き続き説明されており、個人を特定可能な情報（PII）の一部としての位置付けが明示されています。

この修正により、情報の可読性が向上し、ユーザーは自分に必要な言語情報やPIIのサブカテゴリに関する理解を深めることができるようになります。


