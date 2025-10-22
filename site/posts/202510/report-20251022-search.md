---
date: '2025-10-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a411aa0...MicrosoftDocs:46d1709
summary: このコードの差分では、Azure AIのコグニティブサービスに関するドキュメントが更新され、特に翻訳やバージョンの改訂、セクションの追加が行われました。新たにコグニティブサービスの種類を示す画像が追加され、視覚的に理解しやすくなっています。また、用語の見直しやドキュメントの表現の更新が行われ、ユーザーが情報にアクセスしやすくなっています。デバッグセッション関連の詳細も追加され、特にセキュリティ関連の設定に役立つ情報が提供されています。これらの変更は、Azure
  AIプラットフォームの利用をさらに簡単にし、ユーザーのエクスペリエンスを向上させることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a411aa0...MicrosoftDocs:46d1709){target="_blank"}

# ハイライト
このコードの差分は、Azure AIのコグニティブサービスに関連するドキュメントの様々な部分での翻訳やバージョン更新、セクション追加が行われたことを示しています。特に新しい機能として、コグニティブサービスの種類を示す画像が追加されています。

## 新機能
- `cognitive-services-kind.png`という新しい画像が追加され、コグニティブサービスの種類を視覚的に説明するものが提供されました。

## 破壊的変更
- なし

## その他の更新
- ドキュメントの日付や文書表現の更新。
- 用語の変更（例：クラシックAzure AIサービスリソース）。
- デバッグセッション設定の詳細追加。
- JSON出力の構造変更とそれに関する注意事項の追加。
- Azure Searchドキュメントでの誤字修正。

# インサイト
この差分の変更は、Azure AIプラットフォームを利用する際に、より正確で役立つ情報を提供するためのものであり、更新されたドキュメントの構成と情報が強化されています。

まず、コグニティブサービスの連携において、APIのバージョンを最新のものに更新し、用語の見直しによって、ユーザーがサービス設定や請求に関する情報にアクセスする際により直感的に理解できるようになっています。これにより、新しいAzure AIサービスの機能を最大限に生かせるようになります。

デバッグセッションに関しては、新たに追加されたプライベート接続のセクションがユーザーにとって非常に有益です。これにより、特にセキュリティに敏感な設定が要求される場面でのトラブルシューティングが改善されるでしょう。具体的な手順が示されることで、ユーザーは必要な権限やネットワーク設定を正しく構成しやすくなります。

また、ドキュメントインテリジェンスのレイアウトに関する修正では、出力が簡素化され、注釈が追加されたことで、出力構造を理解し必要な設定を行うための明確なガイドラインが提供されています。

さらに、新しい画像の追加は、特にビジュアルを通じた学習を重視するユーザーに対して効果的です。異なるコグニティブサービスの種類やその機能を直感的に理解する手助けとなり、ドキュメントの視覚的側面を強化します。

これらの更新は、Azure AIプラットフォームの多様な利用シナリオに対応し、ユーザーエクスペリエンスを向上させ、より信頼性が高く正確な情報を提供することに寄与しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | コグニティブサービスに関連する文書の更新 | modified | 12 | 7 | 19 | 
| [cognitive-search-debug-session.md](#item-edf092) | minor update | コグニティブ検索デバッグセッションに関する文書の更新 | modified | 12 | 1 | 13 | 
| [cognitive-search-skill-document-intelligence-layout.md](#item-62c06f) | minor update | ドキュメントインテリジェンスレイアウトに関する文書の修正 | modified | 4 | 3 | 7 | 
| [cognitive-services-kind.png](#item-5247d9) | new feature | コグニティブサービスの種類を示す画像の追加 | added | 0 | 0 | 0 | 
| [search-what-is-azure-search.md](#item-93853a) | minor update | Azure Searchに関する文書のテキスト修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: HeidiSteen
 ms.author: heidist 
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/11/2025
+ms.date: 10/20/2025
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
@@ -16,7 +16,7 @@ ms.custom:
 
 # Attach an Azure AI services resource to a skillset in Azure AI Search
 
-If you're using built-in skills for optional [AI enrichment](cognitive-search-concept-intro.md) in Azure AI Search, you can enrich a small number of documents free of charge, limited to 20 transactions daily per index. For larger and more frequent workloads, you should attach a billable [Azure AI services multi-service resource](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills?pivots=azportal). 
+If you're using built-in skills for optional [AI enrichment](cognitive-search-concept-intro.md) in Azure AI Search, you can enrich a small number of documents free of charge, limited to 20 transactions daily per index. For larger and more frequent workloads, you should attach a billable [classic Azure AI services multi-service resource](/azure/ai-services/multi-services-resource-search-skills). 
 
 Azure AI Search uses dedicated, internally hosted Azure AI services multi-service resources for built-in skills execution, but needs your multi-service resource for billing purposes. 
 
@@ -26,7 +26,7 @@ An Azure AI services multi-service resource provides a collection of Azure AI se
 + [Azure AI Language](/azure/ai-services/language-service/overview) for language detection, entity recognition, sentiment analysis, and key phrase extraction
 + [Azure AI Translator](/azure/ai-services/translator/translator-overview) for machine text translation
 
-Exceptions to billing through the multi-service resource include [AzureOpenAIEmbedding](cognitive-search-skill-azure-openai-embedding.md) or the [AML skill](cognitive-search-aml-skill.md) billing. Azure AI Search doesn't internally host models from Azure OpenAI or the Azure AI Foundry model catalog. Usage for AML and Azure OpenAI skills and vectorizers are through [Azure OpenAI Standard pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing) and [Azure Machine Learning Standard pricing](https://azure.microsoft.com/pricing/details/machine-learning/), respectively. A few other skills, such as Text Split and Text Merge, aren't billable.
+Exceptions to billing through the multi-service resource include the [AzureOpenAIEmbedding skill](cognitive-search-skill-azure-openai-embedding.md), [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md), and [AML skill](cognitive-search-aml-skill.md) billing. Azure AI Search doesn't internally host models from Azure OpenAI or the Azure AI Foundry model catalog. Usage for AML and Azure OpenAI skills and vectorizers are through [Azure OpenAI Standard pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing) and [Azure Machine Learning Standard pricing](https://azure.microsoft.com/pricing/details/machine-learning/), respectively. A few other skills, such as Text Split and Text Merge, aren't billable.
 
 To attach an Azure AI multi-service resource, you must provide connection information in the skillset. You can use a key on the connection, or implement a keyless approach that's currently in preview.
 
@@ -35,8 +35,13 @@ To attach an Azure AI multi-service resource, you must provide connection inform
 
 ## Prerequisites
 
-+ Connectivity over a public endpoint, unless your search service meets the creation date, tier, and region requirements for private connections to an Azure AI services multi-service resource.
-+ [Azure AI multi-service resource](/azure/ai-services/multi-service-resource) created via the [Azure portal](https://portal.azure.com) only.
++ Connectivity over a public endpoint, unless your search service meets the creation date, tier, and region requirements for [private connections](search-indexer-howto-access-private.md) to an Azure AI services multi-service resource.
+
++ [Azure AI multi-service resource](/azure/ai-services/multi-services-resource-search-skills) created via the [Azure portal](https://portal.azure.com) only.
+
+  Your multi-service resource should have API kind set to `CognitiveServices`. You can view this property in the Azure portal page for your multi-service account:
+
+  :::image type="content" source="media/cognitive-search-attach-cognitive-services/cognitive-services-kind.png" alt-text="Screenshot of the API kind property in the Azure portal." border="true":::
 
 > [!NOTE]
 > If your Azure AI resource is configured to use a private endpoint, Azure AI Search can connect [using a shared private link](search-indexer-howto-access-private.md) For more information, see the [requirements and limits for using shared private links](search-limits-quotas-capacity.md#shared-private-link-resource-limits).
@@ -68,7 +73,7 @@ As with keys, the details you provide about the Azure AI Services resource are u
 Identity is set to null.
 
 ```http
-POST https://[service-name].search.windows.net/skillsets/[skillset-name]?api-version=2024-11-01-Preview  
+POST https://[service-name].search.windows.net/skillsets/[skillset-name]?api-version=2025-09-01  
 
 {  
     "name": "my skillset name",  
@@ -92,7 +97,7 @@ Identity is set to the resource ID of the user-assigned managed identity. To fin
 For a user-assigned managed identity, set the `@odata.type` and the `userAssignedIdentity` properties.
 
 ```http
-POST https://[service-name].search.windows.net/skillsets/[skillset-name]?api-version=2024-11-01-Preview  
+POST https://[service-name].search.windows.net/skillsets/[skillset-name]?api-version=2025-09-01 
 
 {  
     "name": "my skillset name",  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブサービスに関連する文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるコグニティブサービスの連携に関する文書の更新を反映しています。具体的には、いくつかの文章の修正と日付の更新が行われました。変更の主な点は以下の通りです。

1. ドキュメントの設定情報が更新され、新しい日付「2025年10月20日」が設定されました。
2. 条件の説明に若干の改良があり、従来の「Azure AI services multi-service resource」から「classic Azure AI services multi-service resource」に用語が変更され、より明確な説明となりました。
3. 一部のスキルに対する請求に関する注意事項が更新され、異なるスキルの請求条件が詳しく説明されました。
4. 接続の要件についても、プライベート接続やパブリックエンドポイントに関する指示がより具体的になりました。
5. APIのバージョンが「2024-11-01-Preview」から「2025-09-01」に変更され、最新のバージョンが反映されています。

これらの変更は、Azureユーザーがコグニティブサービスを利用する際により正確で明確な情報を得るために重要です。

## articles/search/cognitive-search-debug-session.md{#item-edf092}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 09/21/2025
+ms.date: 10/21/2025
 ms.update-cycle: 365-days
 ---
 
@@ -67,6 +67,17 @@ If the enrichment pipeline doesn't have any errors, a debug session can be used
 
 Debug sessions help identify the root cause of errors or warnings by analyzing the data, skill inputs and outputs, and field mappings. If the indexer encounters configuration issues, such as incorrect network setup, permission-related access errors, or similar, please review the specific error message along with the linked documentation provided. For troubleshooting guidance, refer to the [common indexer errors and warnings](cognitive-search-common-errors-warnings.md).
 
+## Debug Sessions with private connectivity
+
+If your AI enrichment pipeline uses shared private links to access Azure resources, additional configuration is required to ensure indexer and debug sessions work correctly. This includes permissions, trusted access, and network setup.
+
+- If you're using [managed identity](search-how-to-managed-identities.md), assign the necessary roles to your search service identity, including `Storage Blob Data Contributor`, so debug sessions can write session data to your storage account.
+- Ensure the search service has access to all resources referenced in the [skillset definition](cognitive-search-working-with-skillsets.md), including any used in the debug session.
+- In your storage account, [enable trusted services](search-indexer-howto-access-trusted-service-exception.md) to allow access from Azure AI Search.
+- Set `"executionEnvironment" = "private"` property in the indexer definition to ensure the [indexer runs in a private context](search-indexer-howto-access-private.md?#4---configure-the-indexer-to-run-in-the-private-environment).
+- Create a [shared private link](search-indexer-howto-access-private.md) for each resource accessed by the search service, including: your data source, if configured to indexer AI enrichment cache and knowledge store, and any other resources configured in your skillset.
+- For other troubleshooting guidance, refer to the [common indexer errors and warnings](cognitive-search-common-errors-warnings.md).
+
 
 ## Debug session layout
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブ検索デバッグセッションに関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchのデバッグセッションに関する文書の一部を更新しています。主な変更点を以下に示します。

1. **日付の更新**: 文書の日付が「2025年9月21日」から「2025年10月21日」に変更され、最新の情報が反映されています。
   
2. **新しいセクションの追加**: 「プライベート接続を使用したデバッグセッション」という新しいセクションが追加されました。このセクションでは、AIエンリッチメントパイプラインがAzureリソースにアクセスする際の追加設定について説明しています。特に、必要な権限やネットワーク設定についての指示が含まれています。

3. **詳細な手順の提示**: デバッグセッションが正しく機能するために、マネージドIDの役割設定、ストレージアカウントへの信頼されたサービスの有効化、インデクサ定義内でのプライベート実行環境の設定、リソースへの共有プライベートリンクの作成など、具体的な手順が明記されています。

4. **その他のトラブルシューティング**: トラブルシューティングに関する情報も強調されており、一般的なインデクサのエラーや警告へのリンクが再確認されています。

この更新は、デバッグセッションの設定やトラブルシューティングに関心のあるユーザーにとって、より役立つ情報を提供することを目的としています。

## articles/search/cognitive-search-skill-document-intelligence-layout.md{#item-62c06f}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: reference
-ms.date: 09/29/2025
+ms.date: 10/21/2025
 ms.update-cycle: 365-days
 ---
 
@@ -249,7 +249,7 @@ This example demonstrates how to output text content in fixed-sized chunks and e
           "ordinalPosition": 0,
           "boundingPolygons": "[[{\"x\":1.5548,\"y\":0.4036},{\"x\":6.9691,\"y\":0.4033},{\"x\":6.9691,\"y\":0.8577},{\"x\":1.5548,\"y\":0.8581}],[{\"x\":1.181,\"y\":1.0627},{\"x\":7.1393,\"y\":1.0626},{\"x\":7.1393,\"y\":1.7363},{\"x\":1.181,\"y\":1.7365}],[{\"x\":1.1923,\"y\":2.1466},{\"x\":3.4585,\"y\":2.1496},{\"x\":3.4582,\"y\":2.4251},{\"x\":1.1919,\"y\":2.4221}],[{\"x\":1.1813,\"y\":2.6518},{\"x\":7.2464,\"y\":2.6375},{\"x\":7.2486,\"y\":3.5913},{\"x\":1.1835,\"y\":3.6056}],[{\"x\":1.3349,\"y\":3.9489},{\"x\":2.1237,\"y\":3.9508},{\"x\":2.1233,\"y\":4.1128},{\"x\":1.3346,\"y\":4.111}],[{\"x\":1.5705,\"y\":4.5322},{\"x\":5.801,\"y\":4.5326},{\"x\":5.801,\"y\":4.7311},{\"x\":1.5704,\"y\":4.7307}]]"
         },
-        "sections": ["sectionHeading"]
+        "sections": []
       },
       {
         "id": "2_25134f52-04c3-415a-ab3d-80729bd58e67",
@@ -259,7 +259,7 @@ This example demonstrates how to output text content in fixed-sized chunks and e
           "ordinalPosition": 1,
           "boundingPolygons": "[[{\"x\":2.2041,\"y\":0.4109},{\"x\":4.3967,\"y\":0.4131},{\"x\":4.3966,\"y\":0.5505},{\"x\":2.204,\"y\":0.5482}],[{\"x\":2.5042,\"y\":0.6422},{\"x\":4.8539,\"y\":0.6506},{\"x\":4.8527,\"y\":0.993},{\"x\":2.5029,\"y\":0.9845}],[{\"x\":2.3705,\"y\":1.1496},{\"x\":2.6859,\"y\":1.15},{\"x\":2.6858,\"y\":1.2612},{\"x\":2.3704,\"y\":1.2608}],[{\"x\":3.7418,\"y\":1.1709},{\"x\":3.8082,\"y\":1.171},{\"x\":3.8081,\"y\":1.2508},{\"x\":3.7417,\"y\":1.2507}],[{\"x\":3.9692,\"y\":1.1445},{\"x\":4.0541,\"y\":1.1445},{\"x\":4.0542,\"y\":1.2621},{\"x\":3.9692,\"y\":1.2622}],[{\"x\":4.5326,\"y\":1.2263},{\"x\":5.1065,\"y\":1.229},{\"x\":5.106,\"y\":1.346},{\"x\":4.5321,\"y\":1.3433}],[{\"x\":5.5508,\"y\":1.2267},{\"x\":5.8992,\"y\":1.2268},{\"x\":5.8991,\"y\":1.3408},{\"x\":5.5508,\"y\":1.3408}]]"
         },
-        "sections": ["sectionHeading", "title"]
+        "sections": []
        }
     ],
     "normalized_images": [ 
@@ -286,6 +286,7 @@ This example demonstrates how to output text content in fixed-sized chunks and e
     ] 
 }
 ```
+Note that the `“sections”` in the sample output above appear blank. To populate them, you’ll need to add an additional skill configured with `outputFormat` set to `markdown`to ensure the sections are properly filled.
 
 The skill uses [Azure AI Document Intelligence](/azure/ai-services/document-intelligence/overview) to compute locationMetadata. Refer to [Document Intelligence layout model](/azure/ai-services/document-intelligence/concept-layout) for details on how pages and bounding polygon coordinates are defined.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスレイアウトに関する文書の修正"
}
```

### Explanation
この変更は、Azure AI Document Intelligenceのレイアウトに関するドキュメントの一部を修正したものです。主な変更点は以下の通りです。

1. **日付の更新**: 文書の日付が「2025年9月29日」から「2025年10月21日」に変更され、最新の情報が反映されています。

2. **JSON出力の修正**: サンプル出力において、「sections」フィールドが以前は"sectionHeading"や"title"などを含んでいましたが、これが空の配列に変更されました。これにより、出力の構造が簡素化されました。

3. **補足説明の追加**: 新たに、空の「sections」が表示される理由についての注釈が追加され、適切に埋めるためには、`outputFormat`を`markdown`に設定した追加のスキルが必要であることが説明されています。

4. **技術的な詳細の提供**: ドキュメントインテリジェンスを使用して`locationMetadata`を算出することについて言及されており、ページやバウンディングポリゴン座標がどのように定義されるかについての詳細な情報へのリンクも提供されています。

これらの変更により、ユーザーがドキュメンテーションを利用する際の明確性が向上し、正確な情報に基づく操作が促進されます。

## articles/search/media/cognitive-search-attach-cognitive-services/cognitive-services-kind.png{#item-5247d9}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "コグニティブサービスの種類を示す画像の追加"
}
```

### Explanation
この変更は、Azure AI ドキュメントに新しい画像ファイルを追加したものです。具体的には、コグニティブサービスの種類を示す画像 (`cognitive-services-kind.png`) が新たに追加されました。この画像は、コグニティブサービスとその関連情報を視覚的に説明するために使用されます。

追加された画像については以下のポイントがあります。

- **ファイルの場所**: 画像は、`articles/search/media/cognitive-search-attach-cognitive-services/` ディレクトリに保存されています。
  
- **視覚的なサポート**: この画像は、文章内でコグニティブサービスの種類を具体的に示す際に役立ち、ユーザーがサービスの選択や理解を深める手助けとなります。

- **ドキュメントの充実**: 画像の追加により、文書の視覚的な情報提供が強化され、読者の理解を助けることが期待されます。

この変更は、Azure コグニティブサービスに関するコンテンツの一部を視覚的に補完し、利用者にとってよりわかりやすい情報を提供することを目的としています。

## articles/search/search-what-is-azure-search.md{#item-93853a}

<details>
<summary>Diff</summary>
````diff
@@ -47,7 +47,7 @@ Architecturally, a search service sits between the external data stores that con
 
 ![Azure AI Search architecture](media/search-what-is-azure-search/azure-search.svg "Azure AI Search architecture")
 
-On the indexing side, if your content is on Azure, you can used indexers and skillsets for automated and AI-enriched indexing. Or, create a logic app workflow for equivalent automation over an even broader set of supported data sources. 
+On the indexing side, if your content is on Azure, you can use indexers and skillsets for automated and AI-enriched indexing. Or, create a logic app workflow for equivalent automation over an even broader set of supported data sources. 
 
 On the retrieval side, your app can be an agent or tool, a bot, or any client that sends requests to a search index or knowledge agent.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Searchに関する文書のテキスト修正"
}
```

### Explanation
この変更は、Azure Searchに関する文書 (`search-what-is-azure-search.md`) 内のテキストを修正したものです。主な変更点は、文中の一部表現の誤字修正です。

具体的には、以下のポイントが含まれます：

- **誤字の修正**: "used"が"usse"に誤って記載されていたのを、正しく"use"に修正しました。この誤字は、文の意味に影響を及ぼすため、正確な表現へと更新されています。

- **文の流れと明確性の向上**: 一貫性のある文法を保つことで、文書全体の可読性が高まり、読者がAzure Searchの機能をより理解しやすくなります。

この修正により、閲覧者がAzure Searchの導入に関する重要な情報を正しく受到できることを目指しています。テキストの正確性を保つことで、信頼性の向上も図られます。


