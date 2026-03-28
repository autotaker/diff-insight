---
date: '2026-03-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:91b94fa...MicrosoftDocs:c19e4d2
summary: このコードの変更は、ドキュメント内のリンクテキストや表現の刷新と新機能情報の追加を含んでおり、主に明瞭性と統一性の向上を目的としています。特に、AIドキュメントインテリジェンスサービスに新しい税務書類対応モデルの情報が追加されました。また、絵文字による新マークが削除され、リンクテキストやURLの更新が行われており、よりプロフェッショナルな印象を与える改良が施されています。全体として、ドキュメントの品質維持と整合性向上に向けた重要な改善が実施されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:91b94fa...MicrosoftDocs:c19e4d2){target="_blank"}

<format>
# ハイライト
このコードの変更は、主にドキュメント内のリンクテキストや表現の刷新を含んでおり、一部新機能情報の追加もなされています。絵文字による新マークの削除やリンクの更新を行うことで、ドキュメントの統一と明瞭性を向上させることを目的としています。特筆すべきは、AIドキュメントインテリジェンスサービスにおいて新しい税務書類対応モデルの情報を追加した点が挙げられます。

## 新機能
- `whats-new.md` において、2026年3月の更新として、米国の税務書類モデルの品質改善が記載されました。

## 破壊的変更
- 破壊的変更はありません。

## その他の更新
- 各ドキュメントでの新マーク（🆕）の絵文字が削除され、一貫したスタイルに変更。
- `layout.md` や `release-history.md` など、複数のファイルでリンクテキストやリンクURLの更新。
- `foundry-tools-agents.md` にて、Azureサブスクリプション作成リンクの転送先を適切なURLに修正。
- `PII` 関連ファイルでは、用語の簡略化や、新規マークの削除を伴う整備。

# 洞察
このコードの更新全体を見てみると、Azure Language サービスと AIドキュメントインテリジェンスに関するドキュメントの品質維持と整合性向上を目的とした小規模ながらも重要な改善が行われていることがわかります。絵文字による新マークの多用が避けられ、よりプロフェッショナルな印象を与えることが意図されているようです。また、リンクの更新がいくつか行われており、ユーザーが最新かつ有用なリソースにアクセスしやすくする配慮も感じられます。

特に注目すべきは、2026年3月の更新における新機能の情報追加です。これは、新たな米国税務書類モデルの機能改善を通じて利用者がより効率的にデータを抽出できるようにするためのもので、ドキュメント自体の価値を大いに高めています。このようなアップデートは、利用者の実用的なニーズを直接反映したものであり、AIサービスの競争力を高める一助となるでしょう。

一方で、個々の修正は内容の変更を伴わない表現の微調整が多いため、ドキュメントの基礎がしっかり固まり、ユーザーに対して一貫性のある確実な情報提供が行われることを確認できます。このような継続的なドキュメント改善の取り組みは、技術情報の信頼性向上にも貢献しています。</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index.yml](#item-9c57d7) | minor update | 文書インテリジェンスのリンクテキストの更新 | modified | 2 | 2 | 4 | 
| [layout.md](#item-f7c4c8) | minor update | レイアウト解析結果操作の表記修正 | modified | 1 | 1 | 2 | 
| [release-history.md](#item-c6d7ad) | minor update | リリース履歴のリンクテキストの表記修正 | modified | 3 | 3 | 6 | 
| [whats-new.md](#item-1ec8d3) | new feature | 2026年3月の更新内容追加 | modified | 7 | 0 | 7 | 
| [foundry-tools-agents.md](#item-7b932c) | minor update | 接続設定に関するリンクと説明の修正 | modified | 5 | 5 | 10 | 
| [overview.md](#item-bdc923) | minor update | 見出しの改訂 | modified | 1 | 1 | 2 | 
| [faq.md](#item-d9acbf) | minor update | REST API に関する参照文書のリンク更新 | modified | 3 | 3 | 6 | 
| [faq.md](#item-038891) | minor update | REST API の参照ドキュメントのリンク更新 | modified | 2 | 2 | 4 | 
| [migration-studio-to-foundry.md](#item-12d575) | minor update | リソース関連リンクの更新 | modified | 9 | 9 | 18 | 
| [overview.md](#item-f138b4) | minor update | エージェントセクションの更新 | modified | 6 | 4 | 10 | 
| [redact-text-pii.md](#item-9e48af) | minor update | PII 検出設定の更新 | modified | 7 | 7 | 14 | 
| [migrate-language-service-latest.md](#item-97f571) | minor update | 古いAPIバージョンに関する情報の削除 | modified | 0 | 4 | 4 | 
| [toc.yml](#item-12f1f0) | minor update | TOCの新規マークの削除 | modified | 7 | 7 | 14 | 
| [whats-new.md](#item-69b272) | minor update | 日付とテキストの修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/document-intelligence/index.yml{#item-9c57d7}

<details>
<summary>Diff</summary>
````diff
@@ -70,9 +70,9 @@ landingContent:
      linkLists:
          - linkListType: concept
            links:
-             - text: 🆕 Retrieval-Augmented Generation (RAG)
+             - text:  Retrieval-Augmented Generation (RAG)
                url:  concept/retrieval-augmented-generation.md
-             - text: 🆕 Batch document analysis
+             - text:  Batch document analysis
                url:  concept-batch-analysis.md
              - text: Accuracy and confidence scores
                url: concept/accuracy-confidence.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書インテリジェンスのリンクテキストの更新"
}
```

### Explanation
この変更は、`articles/ai-services/document-intelligence/index.yml` ファイル内のリンクテキストの微調整を含みます。具体的には、リンクの前に付いていた絵文字（🆕）が削除されました。これにより、2つのリンクテキストが影響を受けており、いずれも新しいテキストが適用されています。この変更は、プロジェクトの整合性を保つための小さな更新であり、ユーザーに提供される情報の一貫性を向上させることを目指しています。リンク先のURLは変更されていないため、機能には影響を及ぼさない変更です。

## articles/ai-services/document-intelligence/prebuilt/layout.md{#item-f7c4c8}

<details>
<summary>Diff</summary>
````diff
@@ -1198,7 +1198,7 @@ For large multipage documents, use the `pages` query parameter to indicate speci
 
 ## The Get Analyze Layout Result operation
 
-The second step is to call the [Get Analyze Layout Result](https://westcentralus.dev.cognitive.microsoft.com/docs/services/form-recognizer-api-v2-1/operations/GetAnalyzeLayoutResult) operation. This operation takes as input the Result ID that the `Analyze Layout` operation created. It returns a JSON response that contains a **status** field with the following possible values.
+The second step is to call the `Get Analyze Layout Result` operation. This operation takes as input the Result ID that the `Analyze Layout` operation created. It returns a JSON response that contains a **status** field with the following possible values.
 
 |Field| Type | Possible values |
 |:-----|:----:|:----|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レイアウト解析結果操作の表記修正"
}
```

### Explanation
この変更は、`articles/ai-services/document-intelligence/prebuilt/layout.md` ファイル内のテキストの微調整に関するものです。具体的には、"Get Analyze Layout Result" 操作に関する記述の一部が変更され、操作名がコードスタイルのバッククオートで囲む形式になりました。この修正により、テキストの可読性が向上し、プログラミングに関連する用語であることが明確になります。変更の内容は不変で、新機能の追加やバグ修正ではなく、主に文書表現の改善を目的としています。

## articles/ai-services/document-intelligence/reference/release-history.md{#item-c6d7ad}

<details>
<summary>Diff</summary>
````diff
@@ -41,7 +41,7 @@ The v3.1 API introduces new and updated capabilities:
 * Support for [high resolution documents](../concept/add-on-capabilities.md).
 * Custom neural models now require a single labeled sample to train.
 * Custom neural models language expansion. Train a neural model for documents in 30 languages. See [language support](../language-support/custom.md) for the complete list of supported languages.
-* 🆕 [Prebuilt health insurance card model](../prebuilt/health-insurance-card.md).
+*  [Prebuilt health insurance card model](../prebuilt/health-insurance-card.md).
 * [Prebuilt invoice model locale expansion](../prebuilt/invoice.md#supported-languages-and-locales).
 * [Prebuilt receipt model language and locale expansion](../prebuilt/receipt.md#supported-languages-and-locales) with more than 100 languages supported.
 * [Prebuilt ID model](../prebuilt/id-document.md#supported-document-types) now supports European IDs.
@@ -98,9 +98,9 @@ The v3.1 API introduces new and updated capabilities:
 
 **Introducing refreshed documentation for Build 2023**
 
-* [🆕 Document Intelligence Overview](../overview.md?view=doc-intel-3.0.0&preserve-view=true) enhanced navigation, structured access points, and enriched images.
+* [ Document Intelligence Overview](../overview.md?view=doc-intel-3.0.0&preserve-view=true) enhanced navigation, structured access points, and enriched images.
 
-* [🆕 Choose a Document Intelligence model](../concept/choose-model-feature.md?view=doc-intel-3.0.0&preserve-view=true) provides guidance for choosing the best Document Intelligence solution for your projects and workflows.
+* [ Choose a Document Intelligence model](../concept/choose-model-feature.md?view=doc-intel-3.0.0&preserve-view=true) provides guidance for choosing the best Document Intelligence solution for your projects and workflows.
 
 ## April 2023
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リリース履歴のリンクテキストの表記修正"
}
```

### Explanation
この変更は、`articles/ai-services/document-intelligence/reference/release-history.md` ファイル内のリンクテキストから絵文字（🆕）を削除する修正です。具体的には、いくつかの文書で、「Prebuilt health insurance card model」及び「Document Intelligence Overview」に関する記述で、リンクの前に付いていた絵文字が取り除かれました。この修正により、表現が簡素化され、ドキュメント全体の一貫性が保たれます。この変更は、新機能の追加とは関係なく、文書の明確さを向上させるためのものです。

## articles/ai-services/document-intelligence/whats-new.md{#item-1ec8d3}

<details>
<summary>Diff</summary>
````diff
@@ -38,6 +38,13 @@ Key features include:
 * **Flexible deployment options**. Build applications, automate document workflows, or enable AI-driven analytics with scalable cloud infrastructure.
 * **Unified content extraction**. Utilize a single service to handle diverse content types, reducing complexity and improving operational efficiency.
 
+## March 2026
+
+**Updated prebuilt tax form models**
+
+Prebuilt models for US tax forms have been updated supporting 2025 tax forms including quality improvement to address multi-copy extraction (e.g., multiple W-2s or 1099s in one document). You can now extract data from multi-form filings in a single request and get more comprehensive field coverage.
+
+
 ## June 2025
 
 **Document Intelligence v4.0 Read container is now available!**
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "2026年3月の更新内容追加"
}
```

### Explanation
この変更は、`articles/ai-services/document-intelligence/whats-new.md` ファイルに新しい情報を追加したもので、2026年3月に関する更新内容が盛り込まれました。このセクションでは、更新された米国の税務書類用のプリビルトモデルについて説明されています。具体的には、2025年の税務書類に対応し、複数のコピーの抽出に関する品質改善が行われたことが述べられています。この更新により、利用者は一度のリクエストで複数のフォームのデータを抽出し、より包括的なフィールドカバレッジを得ることができるようになります。この変更は新機能の追加に該当し、ドキュメントの内容を最新の情報で充実させることを目的としています。

## articles/ai-services/language-service/concepts/foundry-tools-agents.md{#item-7b932c}

<details>
<summary>Diff</summary>
````diff
@@ -62,12 +62,12 @@ The MCP server exposes Azure Language features through an agent-friendly endpoin
 
 To use the Azure Language MCP server with agents:
 
-* An Azure subscription. [Create one for free](https://azure.microsoft.com/free/cognitive-services).
+* An Azure subscription. [Create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 * A Foundry resource and project. You need Contributor or Owner role on the resource group.
 * An Azure Language resource.
 * A configured connection in your Foundry project so the agent can authenticate to the Azure Language endpoint.
 
-For connection setup details, see [Create a connection](../../../ai-foundry/how-to/connections-add.md?view=foundry&preserve-view=true).
+For connection setup details, see [Create a connection](../../../foundry/how-to/connections-add.md).
 
 ### Security considerations
 
@@ -92,7 +92,7 @@ The agent prioritizes deterministic behavior, making it suitable for enterprise
 
 Before you set up the intent routing agent, make sure you have the following resources and configurations in place:
 
-* **Azure subscription**: [Create one for free](https://azure.microsoft.com/free/cognitive-services). You need Contributor or Owner role on the resource group.
+* **Azure subscription**: [Create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn). You need Contributor or Owner role on the resource group.
 
 * **Foundry resource**: You need an active Foundry resource to host your agent.
 
@@ -142,7 +142,7 @@ In addition to creating the agent from the exact question answering agent templa
 
 Before you set up the exact question answering agent, make sure you have the following resources and configurations in place:
 
-* **Azure subscription**: [Create one for free](https://azure.microsoft.com/free/cognitive-services). You need Contributor or Owner role on the resource group.
+* **Azure subscription**: [Create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn). You need Contributor or Owner role on the resource group.
 
 * **Foundry resource**: You need an active Foundry resource to host your agent.
 
@@ -189,7 +189,7 @@ Both the intent routing agent and the exact question answering agent require a c
 1. For Foundry and AI hub resources, find the resource key on the resource overview page in the Foundry portal management center.
 1. For any resource type, you can also find the key in the Azure portal.
 
-For detailed connection instructions, see [Create a connection](../../../ai-foundry/how-to/connections-add.md?view=foundry&preserve-view=true).
+For detailed connection instructions, see [Create a connection](../../../foundry/how-to/connections-add.md).
 
 To verify the connection is working, send a test message to the agent. If the agent returns a response from your CQA knowledge base, the connection is configured correctly.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "接続設定に関するリンクと説明の修正"
}
```

### Explanation
この変更は、`articles/ai-services/language-service/concepts/foundry-tools-agents.md` ファイルにおける接続設定に関するリンクおよび関連説明の修正を含んでいます。具体的には、Azureサブスクリプションの作成リンクがより適切なURL（https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn）に更新されました。また、接続設定に関する指示リンクも同様に修正され、旧いURLから新しいものに置き換えられました。

こうした変更は、利用者が必要なリソースや手順にアクセスしやすくすることを目的としており、文書の正確性と使いやすさを向上させるためのものです。この修正は、大きな機能追加ではなく、既存の情報を明確にするためのマイナーアップデートに該当します。

## articles/ai-services/language-service/conversational-language-understanding/overview.md{#item-bdc923}

<details>
<summary>Diff</summary>
````diff
@@ -27,7 +27,7 @@ This documentation contains the following article types:
 
 CLU can be used in multiple scenarios across various industries. Some examples are:
 
-### Multi-turn conversations 🆕
+### Multi-turn conversations 
 
 Use CLU with entity slot filling to enable natural, progressive information gathering across multiple conversation turns. Instead of overwhelming users with complex forms, your application can collect required details as they emerge naturally in dialogue. This approach is ideal for scenarios like booking systems, customer service workflows, or any application where complete information needs to be gathered through conversational exchanges.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "見出しの改訂"
}
```

### Explanation
この変更は、`articles/ai-services/language-service/conversational-language-understanding/overview.md` ファイル内の見出しに関する軽微な更新を含んでいます。具体的には、「Multi-turn conversations」というセクションの見出しから新しいアイコン（🆕）が削除され、見出しテキストがシンプルになりました。この修正は、情報の明瞭さのために行われたもので、内容自体に大きな変更はないものの、文書の一貫性やプロフェッショナルな印象を向上させることを目的としています。このため、この変更はマイナーアップデートに分類されます。

## articles/ai-services/language-service/custom-named-entity-recognition/faq.md{#item-d9acbf}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ The training process can take a long time. As a rough estimate, the expected tra
 
 [!INCLUDE [SDK limitations](includes/sdk-limitations.md)]
 
-You can use the [REST APIs](https://westus.dev.cognitive.microsoft.com/docs/services/language-authoring-clu-apis-2022-03-01-preview/operations/Projects_TriggerImportProjectJob) to build your custom models. Follow this [quickstart](quickstart.md?pivots=rest-api) to get started with creating a project and creating a model through APIs for examples of how to call the Authoring API.
+You can use the [REST API Reference Documentation](/rest/api/aifoundry) to build your custom models. Follow this [quickstart](quickstart.md?pivots=rest-api) to get started with creating a project and creating a model through APIs for examples of how to call the Authoring API.
 
 When you're ready to start [using your model to make predictions](#how-do-i-use-my-trained-model-for-predictions), you can use the REST API, or the client library.
 
@@ -95,12 +95,12 @@ After deploying your model, you [call the prediction API](how-to/call-api.md), u
 
 ## Data privacy and security
 
-Your data is only stored in your Azure Storage account. Custom NER only has access to read from it during training. Custom NER users have full control to view, export, or delete any user content either through the [Foundry](https://ai.azure.com/) or programmatically by using [REST APIs](https://westus.dev.cognitive.microsoft.com/docs/services/language-authoring-clu-apis-2022-03-01-preview/operations/Projects_TriggerImportProjectJob). For more information, *see* [Data, privacy, and security for Language](/azure/ai-foundry/responsible-ai/language-service/data-privacy)
+Your data is only stored in your Azure Storage account. Custom NER only has access to read from it during training. Custom NER users have full control to view, export, or delete any user content either through the [Foundry](https://ai.azure.com/) or programmatically by using [REST API Reference Documentation](/rest/api/aifoundry)). For more information, *see* [Data, privacy, and security for Language](/azure/ai-foundry/responsible-ai/language-service/data-privacy)
 
 
 ## How to clone my project?
 
-To clone your project, you need to use the export API  to export the project assets, and then import them into a new project. See the [REST API](https://westus.dev.cognitive.microsoft.com/docs/services/language-authoring-clu-apis-2022-03-01-preview/operations/Projects_TriggerImportProjectJob) reference for both operations.
+To clone your project, you need to use the export API  to export the project assets, and then import them into a new project. See the [REST API Reference Documentation](/rest/api/aifoundry) for both operations.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST API に関する参照文書のリンク更新"
}
```

### Explanation
この変更は、`articles/ai-services/language-service/custom-named-entity-recognition/faq.md` ファイルにおける REST API の参照についてのリンクを更新するマイナーアップデートです。具体的には、REST API に関するリンクが新しい URL（/rest/api/aifoundry）に変更され、より明確な文書への参照を提供するようになりました。この修正により、開発者がカスタムモデルを構築するための情報や手順をより簡単に見つけられるようになっています。

その他にも、データプライバシーとセキュリティの部分での文書の参照が一貫性を持って修正されており、特定の操作に関するリンクが同様に新しい参照に統一されています。この更新は、文書の整合性を保ちながら、読者に対してより良い情報を提供することを目指しています。

## articles/ai-services/language-service/custom-text-classification/faq.md{#item-038891}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ The training process can take some time. As a rough estimate, the expected train
 
 ## How do I build my custom model programmatically?
 
-You can use the [REST APIs](https://westus.dev.cognitive.microsoft.com/docs/services/language-authoring-clu-apis-2022-03-01-preview/operations/Projects_TriggerImportProjectJob) to build your custom models. Follow this [quickstart](quickstart.md?pivots=rest-api) to get started with creating a project and creating a model through APIs for examples of how to call the Authoring API. 
+You can use the [REST API Reference Documentation](/rest/api/aifoundry) to build your custom models. Follow this [quickstart](quickstart.md?pivots=rest-api) to get started with creating a project and creating a model through APIs for examples of how to call the Authoring API. 
 
 When you're ready to start [using your model to make predictions](#how-do-i-use-my-trained-model-to-make-predictions), you can use the REST API, or the client library.
 
@@ -88,7 +88,7 @@ For more information, *see* [Data, privacy, and security for Azure Language in F
 
 ## How to clone my project?
 
-To clone your project, you need to use the export API  to export the project assets, and then import them into a new project. See [REST APIs](https://westus.dev.cognitive.microsoft.com/docs/services/language-authoring-clu-apis-2022-03-01-preview/operations/Projects_TriggerImportProjectJob) reference for both operations.
+To clone your project, you need to use the export API  to export the project assets, and then import them into a new project. See [REST API Reference Documentation](/rest/api/aifoundry) for both operations.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST API の参照ドキュメントのリンク更新"
}
```

### Explanation
この変更は、`articles/ai-services/language-service/custom-text-classification/faq.md` ファイルにおける REST API の参照リンクを更新する軽微な修正です。具体的には、カスタムモデルの構築方法に関する指示で、リンクが以前の形式（https://westus.dev.cognitive.microsoft.com/...）から新しい参照ドキュメント（/rest/api/aifoundry）に変更されました。この修正により、開発者は情報へのアクセスがより簡単になり、最新のドキュメンテーションを利用しやすくなっています。

さらに、プロジェクトをクローンする方法に関する記述でも同様にリンクが更新されており、全体として文書の整合性を向上させることを狙いとしています。このようなリンクの更新は、読者にとって役立つ情報へのアクセスを簡素化し、ナビゲーションを改善します。

## articles/ai-services/language-service/migration-studio-to-foundry.md{#item-12d575}

<details>
<summary>Diff</summary>
````diff
@@ -57,9 +57,9 @@ If you have an existing Azure Language resource with custom projects, you can co
 
 To use Azure AI Language capabilities with a Language resource, you need a Foundry hub and an associated hub-based project. Set up these resources using either of the following approaches:
 
-* **Azure portal**. Create a hub first, then create an associated project. This approach provides explicit control over resource configuration settings. For step-by-step instructions, *see* [Create a hub in the Azure portal](/azure/ai-foundry/how-to/create-azure-ai-resource?view=foundry-classic&preserve-view=true&tabs=portal#create-a-hub-in-the-azure-portal). After creating your hub, navigate to your hub resource, select **Projects** or **Management center** under **Resource management**, and then select **+ New project**.
+* **Azure portal**. Create a hub first, then create an associated project. This approach provides explicit control over resource configuration settings. For step-by-step instructions, *see* [Create a hub in the Azure portal](/azure/foundry-classic/how-to/create-azure-ai-resource?tabs=portal#create-a-hub-in-the-azure-portal). After creating your hub, navigate to your hub resource, select **Projects** or **Management center** under **Resource management**, and then select **+ New project**.
 
-* **Microsoft Foundry portal**. Create a hub-based project directly in Microsoft Foundry, which automatically provisions the underlying hub. This approach streamlines setup by handling hub creation automatically. For step-by-step instructions, *see* [Create a project](/azure/ai-foundry/how-to/create-projects?view=foundry-classic&preserve-view=true&tabs=foundry).
+* **Microsoft Foundry portal**. Create a hub-based project directly in Microsoft Foundry, which automatically provisions the underlying hub. This approach streamlines setup by handling hub creation automatically. For step-by-step instructions, *see* [Create a project](/azure/foundry-classic/how-to/create-projects?tabs=foundry).
 
 ### Step 2: Confirm prerequisites and region support
 
@@ -68,7 +68,7 @@ The following table lists the custom capabilities available in Microsoft Foundry
 |Capability|Required prerequisites|Region support|
 |---|---|---|
 |[**Conversational Language Understanding (CLU)**](conversational-language-understanding/quickstart.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for CLU](concepts/regional-support.md).|
-|[**Custom Question Answering (CQA)**](question-answering/quickstart/sdk.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.</br>&bullet; Azure AI Search resource connected to your hub or hub-based project via the Foundry Management Center. For more information, *see* [Create a new connection](/azure/ai-foundry/how-to/connections-add?view=foundry-classic&preserve-view=true&tabs=foundry-portal#create-a-new-connection).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
+|[**Custom Question Answering (CQA)**](question-answering/quickstart/sdk.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.</br>&bullet; Azure AI Search resource connected to your hub or hub-based project via the Foundry Management Center. For more information, *see* [Create a new connection](/azure/foundry-classic/how-to/connections-add?tabs=foundry-portal#create-a-new-connection).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
 |[**Orchestration workflow**](orchestration-workflow/quickstart.md)|&bullet; Foundry resource and Foundry project, or Language resource and Foundry hub-based project.</br>&bullet; A `CLU` or `CQA` project created in the same resource.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for Orchestration workflow](concepts/regional-support.md).|
 |[**Custom Named Entity Recognition (CNER)**](custom-named-entity-recognition/quickstart.md)|&bullet; Language resource with a storage account linked during resource creation.</br>&bullet; Foundry hub-based project created in the Azure portal.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for CNER](concepts/regional-support.md).|
 
@@ -87,7 +87,7 @@ To access and manage your existing Language resource projects in Microsoft Found
 1. Select your Azure Language resource or Foundry resource from the list.
 1. Select **Add connection**.
 
-For more information, *see* [Connect Foundry Tools to a Foundry project](/azure/ai-foundry/how-to/connections-add?view=foundry-classic&preserve-view=true&tabs=foundry-portal).
+For more information, *see* [Connect Foundry Tools to a Foundry project](/azure/foundry-classic/how-to/connections-add?tabs=foundry-portal).
 
 ### Step 4: Validate and test your migrated projects
 
@@ -145,7 +145,7 @@ To use Azure AI Language capabilities with a Foundry resource, you need both the
 
 * **Azure portal**. Create a Foundry resource first, then create an associated Foundry project. This approach provides explicit control over resource configuration settings. For step-by-step instructions, *see* [Create a Foundry resource in the Azure portal](/azure/ai-services/multi-service-resource?pivots=azportal#create-a-new-microsoft-foundry-resource).
 
-* **Microsoft Foundry portal**. Create a Foundry project directly, which automatically provisions the underlying Foundry resource. This approach streamlines setup by handling resource creation automatically. For step-by-step instructions, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects?view=foundry-classic&preserve-view=true&tabs=foundry).
+* **Microsoft Foundry portal**. Create a Foundry project directly, which automatically provisions the underlying Foundry resource. This approach streamlines setup by handling resource creation automatically. For step-by-step instructions, *see* [Create a Foundry project](/azure/foundry-classic/how-to/create-projects?tabs=foundry).
 
 > [!IMPORTANT]
 > **Custom NER (CNER)** requires a storage account to be linked to the Foundry resource during initial resource creation. To establish this link, you must configure the Foundry resource in the [Azure portal](https://portal.azure.com/).
@@ -215,9 +215,9 @@ After importing your projects, validate that the migration is successful:
 >
 > **Post-retirement project recreation**. After the March 20, 2027 retirement date, Language Studio export functionality is no longer available. However, you can recreate your custom projects directly in Microsoft Foundry:
 >
-> * **Existing Azure Language resources**. You can access and continue to use your current Azure Language resources within the Microsoft Foundry portal by creating a **Foundry hub** and an associated **hub-based project**. For more information, *see* [Create a hub in the Azure portal](/azure/ai-foundry/how-to/create-azure-ai-resource?view=foundry-classic&preserve-view=true&tabs=portal#create-a-hub-in-the-azure-portal).
+> * **Existing Azure Language resources**. You can access and continue to use your current Azure Language resources within the Microsoft Foundry portal by creating a **Foundry hub** and an associated **hub-based project**. For more information, *see* [Create a hub in the Azure portal](/azure/foundry-classic/how-to/create-azure-ai-resource?tabs=portal#create-a-hub-in-the-azure-portal).
 >
-> * **Existing Foundry resource-based projects**. You can access your current **Foundry projects** directly in the Microsoft Foundry portal. Alternatively, create a new project and transfer your project assets to the new environment. For more information, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects?view=foundry-classic&preserve-view=true&tabs=foundry).
+> * **Existing Foundry resource-based projects**. You can access your current **Foundry projects** directly in the Microsoft Foundry portal. Alternatively, create a new project and transfer your project assets to the new environment. For more information, *see* [Create a Foundry project](/azure/foundry-classic/how-to/create-projects?tabs=foundry).
 
 #### Pretrained models (prebuilt) supported in Microsoft Foundry
 
@@ -243,8 +243,8 @@ The following table lists the pretrained (prebuilt) capabilities available in Mi
 |Capability|Required prerequisites|Region support|
 |---|---|---|
 |[**Conversational Language Understanding (CLU)**](conversational-language-understanding/quickstart.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for Conversational Language Understanding](concepts/regional-support.md#conversational-language-understanding-and-orchestration-workflow).|
-|[**Custom Question Answering (CQA)**](question-answering/quickstart/sdk.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.</br>&bullet; Azure AI Search resource connected to your project via the Foundry Management Center. For more information, *see* [Create a new connection](/azure/ai-foundry/how-to/connections-add?view=foundry-classic&preserve-view=true&tabs=foundry-portal#create-a-new-connection).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
-|[**Custom Question Answering agent**](question-answering/how-to/deploy-agent.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.</br>&bullet; Azure AI Search resource connected to your project via the Foundry Management Center. For more information, *see* [Create a new connection](/azure/ai-foundry/how-to/connections-add?view=foundry-classic&preserve-view=true&tabs=foundry-portal#create-a-new-connection).</br>&bullet; Deployed knowledge base.</br>&bullet; Deployed Azure OpenAI model in Microsoft Foundry.</br>&bullet; API key connected to your project.|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
+|[**Custom Question Answering (CQA)**](question-answering/quickstart/sdk.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.</br>&bullet; Azure AI Search resource connected to your project via the Foundry Management Center. For more information, *see* [Create a new connection](/azure/foundry-classic/how-to/connections-add?tabs=foundry-portal#create-a-new-connection).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
+|[**Custom Question Answering agent**](question-answering/how-to/deploy-agent.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.</br>&bullet; Azure AI Search resource connected to your project via the Foundry Management Center. For more information, *see* [Create a new connection](/azure/foundry-classic/how-to/connections-add?tabs=foundry-portal#create-a-new-connection).</br>&bullet; Deployed knowledge base.</br>&bullet; Deployed Azure OpenAI model in Microsoft Foundry.</br>&bullet; API key connected to your project.|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
 |[**Custom Named Entity Recognition (CNER)**](custom-named-entity-recognition/quickstart.md)|&bullet; Language resource with a storage account **linked during resource creation** in the Foundry portal.</br>&bullet; Foundry project created in the Azure portal.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for CNER](concepts/regional-support.md#custom-named-entity-recognition).|
 |[**Orchestration Workflow**](orchestration-workflow/quickstart.md)|&bullet; Foundry resource and Foundry project, or Language resource and Foundry hub-based project.</br>&bullet; A `CLU` or `CQA` project created in the same resource.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for Orchestration workflow](concepts/regional-support.md#conversational-language-understanding-and-orchestration-workflow).|
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソース関連リンクの更新"
}
```

### Explanation
この変更は、`articles/ai-services/language-service/migration-studio-to-foundry.md` ファイルに対する軽微な更新であり、Azure Language サービスを Microsoft Foundry に移行する際のガイドラインに関連するリソースリンクが修正されています。特に、Azure ポータルおよび Microsoft Foundry ポータルにおけるプロジェクトの作成手順に関するリンクが新しい参照に更新されました。

具体的には、Azure ポータルでハブとプロジェクトを作成する手順のリンク、ならびに Microsoft Foundry ポータルでのプロジェクト作成手順のリンクが、最新のドキュメントを指すように変更されています。この修正により、ユーザーは具体的な手順をより簡単に追従でき、全体の文書の整合性が向上します。さらに、いくつかの段落でリンクの構造が整理され、ユーザーに対する明確な案内が強化されています。

## articles/ai-services/language-service/overview.md{#item-f138b4}

<details>
<summary>Diff</summary>
````diff
@@ -9,15 +9,17 @@ ms.topic: overview
 ms.date: 11/18/2025
 ms.author: lajanuar
 ---
+
+<!-- markdownlint-disable MD025 -->
 # What is Azure Language in Foundry Tools?
 
-Azure Language is a cloud-based service that provides Natural Language Processing (NLP) features for understanding and analyzing text. Use this service to help build intelligent applications using the web-based Microsoft Foundry, REST APIs, and client libraries. For AI agent development, the service capabilities are also available as tools in Azure Language [MCP server](#azure-language-mcp-server-), which is available both as a remote server in the **Microsoft Foundry Tool Catalog** and as a local server for self-hosted environments.
+Azure Language is a cloud-based service that provides Natural Language Processing (NLP) features for understanding and analyzing text. Use this service to help build intelligent applications using the web-based Microsoft Foundry, REST APIs, and client libraries. For AI agent development, the service capabilities are also available as tools in Azure Language [MCP server](#azure-language-mcp-server), which is available both as a remote server in the **Microsoft Foundry Tool Catalog** and as a local server for self-hosted environments.
 
 ## Available tools
 
 Azure Language provides specialized tools that enable seamless integration between AI agents and language processing services through standardized protocols.
 
-### Azure Language MCP server 🆕
+### Azure Language MCP server 
 
 The MCP (Model Context Protocol) server creates a standardized bridge that connects AI agents directly to Azure Language services through industry-standard protocols. This integration enables developers to build sophisticated conversational applications with reliable natural language processing capabilities while ensuring enterprise-grade compliance, data protection, and processing accuracy throughout their AI workflows. 
 
@@ -31,13 +33,13 @@ For more information, *see* [Azure Language MCP server](concepts/foundry-tools-a
 
 Azure Language offers prebuilt agents that handle specific conversational AI scenarios with built-in governance, routing logic, and quality control mechanisms.
 
-### Azure Language Intent Routing agent 🆕
+### Azure Language Intent Routing agent 
 
 The Intent Routing agent intelligently manages conversation flows by understanding user intentions and delivering accurate responses in conversational AI applications. This agent uses predictable decision-making processes combined with controlled response generation to ensure consistent, reliable interactions that organizations can trust and monitor. 
 
 For more information, *see* [Azure Language Intent Routing agent](concepts/foundry-tools-agents.md#azure-language-intent-routing-agent-preview).
 
-### Azure Language Exact Question Answering agent 🆕
+### Azure Language Exact Question Answering agent 
 
 The Exact Question Answering agent provides reliable, word-for-word responses to your most important business questions. This agent automates frequently asked questions while maintaining human oversight and quality control to ensure accuracy and compliance.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントセクションの更新"
}
```

### Explanation
この変更は、`articles/ai-services/language-service/overview.md` ファイルに対する軽微な更新で、Azure Language サービスの概要を述べるセクションにおいて、文の整形とエージェントに関する情報が整理されています。特に、各エージェントのタイトルから「新規（🆕）」マークが削除され、より正式な表現となっています。

具体的には、Azure Language MCP サーバー、Intent Routing エージェント、および Exact Question Answering エージェントの3つの重要な機能が記述されており、それぞれの役割や利点についての説明が含まれています。この修正によって、情報がより一貫性を持ち、読みやすさが向上し、ユーザーがサービスの機能を直感的に理解しやすくなっています。また、マークダウンのチェックを無効にするためのコメントが追加され、文書作成のルールが明示されています。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-text-pii.md{#item-9e48af}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/18/2025
+ms.date: 03/17/2026
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
@@ -27,31 +27,31 @@ By default, this feature uses the latest available AI model on your text. You ca
 
 When you submit input text to be processed, you can specify which of [the supported languages](../language-support.md) they're written in. If you don't specify a language, extraction defaults to English. The API may return offsets in the response to support different [multilingual and emoji encodings](../../concepts/multilingual-emoji-support.md).
 
-##  Additional configuration parameters (2025-11-15-preview)
+##  New configuration parameters (2025-11-15-preview)
 
 > [!IMPORTANT]
 >
-> * Azure Language in Foundry Tools public preview releases provide early access to features that are in active development.
+> * Azure Language public preview releases provide early access to features that are in active development.
 > * Features, approaches, and processes may change, before General Availability (GA), based on user feedback.
 > * Preview features are subject to the terms applicable to **Previews** as described in the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms) and the [Microsoft Products and Services Data Protection Addendum (DPA)](https://www.microsoft.com/licensing/docs/view/microsoft-products-and-services-data-protection-addendum-dpa).
 
 ### Redaction policies
 
-Starting with version `2025-11-15-preview` and onward, you can specify the `redactionPolicies` parameter to define which redaction policies are applied when processing text. You can include more than one policy in a single request, with one policy specified as the `defaultRedactionPolicy` and additional policy overrides for specified entities.
+Starting with version `2025-11-15-preview` and onward, you can specify the `redactionPolicies` parameter to define which redaction policies are applied when processing text. You can include more than one policy in a single request, with one policy specified as the `defaultRedactionPolicy` and further added policy overrides for specified entities.
 
 The policy field accepts four policy types:
 
 > [!div class="checklist"]
 >
-> * [`SyntheticReplacement 🆕`](#syntheticreplacement-policy-type-)
+> * [`SyntheticReplacement `](#syntheticreplacement-policy-type)
 > * [`CharacterMask` (default)](#charactermask-policy-type)
 > * [`NoMask`](#nomask-policy-type)
 > * [`EntityMask`](#entitymask-policy-type)
 
 For more information, *see* [REST API PII task parameters](/rest/api/language/analyze-text/analyze-text/analyze-text?view=rest-language-analyze-text-2025-11-15-preview&preserve-view=true&tabs=HTTP#piitaskparameters).
 
 <!-- markdownlint-disable MD001 -->
-##### syntheticReplacement policy type 🆕
+##### syntheticReplacement policy type 
 
 > [!IMPORTANT]
 > The Azure Language in Foundry Tools Text Personally Identifiable Information (PII) detection **anonymization feature** (synthetic replacement) is currently available in `preview` and licensed to you as part of your Azure subscription. Your use of this feature is subject to the terms applicable to **Previews** as described in the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms) and the [Microsoft Products and Services Data Protection Addendum (DPA)](https://www.microsoft.com/licensing/docs/view/microsoft-products-and-services-data-protection-addendum-dpa).
@@ -157,7 +157,7 @@ The **entityMask** policy type** enables you to mask the detected PII entity tex
 
 To learn more, *see* [Transparency Note for Personally Identifiable Information (PII)](/azure/ai-foundry/responsible-ai/language-service/transparency-note-personally-identifiable-information).
 
-### ConfidenceScoreThreshold 🆕
+### ConfidenceScoreThreshold 
 
 The PII feature currently redacts all detected entities, regardless of their confidence scores. Thus, entities with low confidence scores are also removed, even if retaining them is preferred. To enhance flexibility, you can configure a confidence threshold that determines the minimum confidence score an entity must have to remain in the output.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PII 検出設定の更新"
}
```

### Explanation
この変更は、`articles/ai-services/language-service/personally-identifiable-information/how-to/redact-text-pii.md` ファイルに対する軽微な更新で、特に個人情報 (PII) の検出とマスキングに関連する設定項目が修正されています。具体的には、日付の更新やセクションタイトルの変更、そして一部の表現が整理されています。

変更内容には、`Azure Language in Foundry Tools` から `Azure Language` への表現の簡略化が含まれ、公開プレビューの特徴についての記述が更新されています。また、`syntheticReplacement` ポリシーの説明から「新規（🆕）」のマークが削除され、文書の一貫性が向上しています。さらに、`ConfidenceScoreThreshold` セクションも同様に新規マークが削除され、より標準的な形式での説明が行われています。

全体として、この更新はドキュメントの明確さと整合性を強化し、サポート情報を利用するユーザーにとってより使いやすい内容となっています。

## articles/ai-services/language-service/reference/migrate-language-service-latest.md{#item-97f571}

<details>
<summary>Diff</summary>
````diff
@@ -125,10 +125,6 @@ The key phrase extraction feature functionality currently isn't changed outside
 
 * [What is Azure Language in Foundry Tools?](../overview.md)
 * [Language developer guide](../concepts/developer-guide.md)
-* See the following reference documentation for information on previous API versions.
-  * [Version 2.1](https://westcentralus.dev.cognitive.microsoft.com/docs/services/TextAnalytics-v2-1/operations/56f30ceeeda5650db055a3c9)
-  * [Version 3.0](https://westus.dev.cognitive.microsoft.com/docs/services/TextAnalytics-v3-0/operations/Sentiment)
-  * [Version 3.1](https://westcentralus.dev.cognitive.microsoft.com/docs/services/TextAnalytics-v3-1/operations/Sentiment)
 * Use the following quickstart guides to see examples for the current version of these features.
   * [Entity linking](../entity-linking/quickstart.md)
   * [Key phrase extraction](../key-phrase-extraction/quickstart.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "古いAPIバージョンに関する情報の削除"
}
```

### Explanation
この変更は、`articles/ai-services/language-service/reference/migrate-language-service-latest.md` ファイルに対する軽微な更新で、古いAPIバージョンに関する情報が削除されています。具体的には、以前のAPIバージョンに関連するリファレンス文書へのリンクが削除され、より最新の情報に焦点を当てる内容に改訂されています。

具体的には、旧バージョンのAPI（バージョン2.1、3.0、3.1）へのリンクが取り除かれ、現在のバージョンの機能に関するクイックスタートガイドへとシフトされています。これにより、ユーザーは最新の機能やドキュメントにアクセスしやすくなり、古い情報に惑わされることなく、最も関連性の高いリソースに集中できるようになっています。全体として、この更新は情報の明瞭さを向上させ、より良いユーザーエクスペリエンスを提供することを目的としています。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ items:
   - name: Configure Azure resources
     href: conversational-language-understanding/how-to/configure-azure-resources.md
     displayName: configuration, fine-tuning, azure ai foundry, azure portal
-  - name: Migrate to Microsoft Foundry 🆕
+  - name: Migrate to Microsoft Foundry 
     href: migration-studio-to-foundry.md
     displayName: migrate, foundry, studio, permissions, roles, access, requisites, requirements
 - name: Azure Language in Foundry Tools capabilities
@@ -41,7 +41,7 @@ items:
         - name: Get started
           href: conversational-language-understanding/quickstart.md
           displayName: getting started, tutorial, conversational ai setup
-        - name: Try multi-turn conversations 🆕
+        - name: Try multi-turn conversations 
           href: conversational-language-understanding/how-to/quickstart-multi-turn-conversations.md
           displayName: slot-filling, intent, entities, entity, association, foundry
     - name: Language support
@@ -62,7 +62,7 @@ items:
         href: /azure/ai-foundry/responsible-ai/clu/clu-data-privacy-security?context=/azure/ai-services/language-service/context/context
     - name: How-to guides
       items:
-        - name: Build a multi-turn conversation model 🆕
+        - name: Build a multi-turn conversation model 
           href:  conversational-language-understanding/how-to/build-multi-turn-model.md
           displayName: slot-filling, intent, entities, entity, association, foundry
         - name: Use containers
@@ -103,7 +103,7 @@ items:
           displayName: disaster recovery, failover, clu
     - name: Concepts
       items:
-        - name: Multi-turn conversations 🆕
+        - name: Multi-turn conversations 
           href:  conversational-language-understanding/concepts/multi-turn-conversations.md
           displayName: slot-filling, intent, entities, entity, association, foundry
         - name: Best practices
@@ -166,7 +166,7 @@ items:
       - name: Create, test, and deploy a knowledge base
         href: question-answering/how-to/create-test-deploy.md
         displayName: knowledge base, test deploy
-      - name: Deploy a CQA agent 🆕
+      - name: Deploy a CQA agent 
         href: question-answering/how-to/deploy-agent.md
         displayName: virtual assistant, chatbot, knowledge base, deployment
       - name: Export/import/refresh
@@ -458,7 +458,7 @@ items:
           href: ../cognitive-services-container-support.md
     - name: Concepts
       items:
-      - name: Recognized entity categories 🆕
+      - name: Recognized entity categories 
         href: named-entity-recognition/concepts/named-entity-categories.md
       - name: Entity Metadata
         href: named-entity-recognition/concepts/entity-metadata.md
@@ -773,7 +773,7 @@ items:
   - name: Developer guide
     href: concepts/developer-guide.md
     displayName: development, sdk guide, programming
-  - name: Azure tools and agents 🆕
+  - name: Azure tools and agents 
     href: concepts/foundry-tools-agents.md
     displayName: mcp, exact, question, answering, intent, routing
   - name: Role-based-access-control
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCの新規マークの削除"
}
```

### Explanation
この変更は、`articles/ai-services/language-service/toc.yml` ファイルに対する軽微な更新で、特にTOC（目次）内の項目から「新規（🆕）」のマークが削除されています。このマークは、新しく追加された内容を示すために使用されていましたが、これにより目次の表示が統一され、文書の整合性が向上しています。

具体的には、複数のセクションにわたって「新規」マークが削除され、各項目のタイトルがよりクリーンでシンプルな表現になりました。これにより、ユーザーは目次を閲覧する際に、不要な情報によって混乱することなく、より容易に内容を把握できるようになります。この変更は、ドキュメントのナビゲーションを向上させ、全体的なユーザーエクスペリエンスの向上に寄与しています。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: whats-new
-ms.date: 02/09/2026
+ms.date: 03/17/2026
 ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD025 -->
@@ -70,7 +70,7 @@ Stay informed about recent releases and enhancements designed to help you get th
 
 * **Anonymization**. The `syntheticReplacement` [redaction policy](personally-identifiable-information/how-to/redact-text-pii.md#redaction-policies) enables masking detected PII entities with synthetic replacement values. For example, "John Doe received a call from 424-878-9193" can be transformed into "Sam Johnson received a call from 401-255-6901."
 * **Disable type-validation enforcement**. Disable [entity type validation](personally-identifiable-information/how-to/redact-text-pii.md#disableentityvalidation) to bypass strict validation when operational efficiency is prioritized over data integrity checks.
-* **Confidence threshold score**. Set a minimum [confidence score](personally-identifiable-information/how-to/redact-text-pii.md#confidencescorethreshold-) threshold to control which entities appear in the output based on detection confidence.
+* **Confidence threshold score**. Set a minimum [confidence score](personally-identifiable-information/how-to/redact-text-pii.md#confidencescorethreshold) threshold to control which entities appear in the output based on detection confidence.
 
 **Entity Tags generally available**. [Entity Tags](named-entity-recognition/concepts/named-entity-categories.md) are now generally available, providing enhanced metadata and categorization for named entities.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付とテキストの修正"
}
```

### Explanation
この変更は、`articles/ai-services/language-service/whats-new.md` ファイルに対する軽微な更新であり、主に日付情報の修正と特定のテキストの微調整が含まれています。

具体的には、文書内の「最終更新日」が `02/09/2026` から `03/17/2026` に変更され、最新の情報を反映しています。また、「Confidence threshold score」に関する部分のリンクにおいて、末尾のハイフンが削除され、テキストがより正確になっています。この修正により、コンテンツの整合性が改善され、読者に提供される情報がより鮮明で最新版であることが保証されます。

全体として、この更新により、文書は一層信頼性を増し、ユーザーにとっての可読性と理解度が向上しています。


