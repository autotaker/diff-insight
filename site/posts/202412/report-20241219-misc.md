---
date: '2024-12-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:aba0ab5...MicrosoftDocs:6ebedb4
summary: この更新では、Azure AI Document Intelligenceおよび関連するSDKとサービスに関する複数の文書がマイナーに変更されました。主な変更点として、日付やタイトルの修正、リンクの更新、新しい画像の追加、そして新機能の紹介が含まれています。特に、「トレース機能」の導入に関する手順や画像が追加され、評価機能が改善されています。また、文書の質向上を図るための画像削除や、各SDKおよびサービスに関する情報の最新化も行われています。この更新は、Azure
  AIのドキュメント精度を高め、開発者やユーザーに直感的で最新の情報を提供するための取り組みです。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:aba0ab5...MicrosoftDocs:6ebedb4){target="_blank"}

# ハイライト
この更新では、Azure AI Document Intelligenceおよび関連するSDKとサービスに関する複数の文書がマイナーに変更されました。主な変更点は、日付やタイトルの修正、リンクの更新、新しい画像の追加、そして新機能の紹介になります。さらに、「トレース機能」の導入とそれに関連した手順や画像が追加され、評価機能の改善も行われています。

## 新機能
- 画像のぼやけチェック結果や評価結果の詳細を示すための新しい画像が追加されました。
- LangChainのトレース機能の実装に関する新しい説明と画像が提供されました。

## 破壊的変更
- あるアシスタント応答に関する根拠のない画像が削除され、ユーザー体験の改善が図られました。

## その他の更新
- 各SDKおよびサービスに関するドキュメントの日付やリンク、タイトルが最新の情報に更新されました。
- トレーシングや評価プロセスにおける安全性とユーザー体験の向上を目的とした複数の画像更新と説明追加が行われました。

# インサイト
今回の更新は、Azure AIのドキュメント精度を高め、開発者やユーザーに最新でより直感的な情報を提供する取り組みの一環となっています。日付やリンクの更新によって、最新のSDKやAPIバージョンを使用することへの保証がされており、特に複数のプログラミング言語にわたってリリースされた新しいSDKバージョンの存在を強調しています。

新しい画像や詳細な説明の追加を通じて、ユーザーはトレーシングや評価といった開発のさまざまなフェーズにおいて、より深い理解を得ることができ、特に視覚的なフィードバックを得ることで、間違いなく改善が見られます。LangChainの新しいトレーシング用画像や手順は、開発者がトレースデータを効果的に利用する助けとなり、デバッグやパフォーマンスの解析を容易にします。

また、画像の削除といった破壊的な変更も、最終的にはユーザーがより信頼性の高い情報を得られるようにするためのものであり、ドキュメントの質を維持し続けるための重要なプロセスであると考えられます。全体として、この更新は、Azure AIにおけるユーザーの利便性と体験を向上させるために意図されています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [get-started-sdks-rest-api.md](#item-ed53bc) | minor update | ドキュメントインテリジェンスのクイックスタートガイドの更新 | modified | 3 | 3 | 6 | 
| [csharp-sdk.md](#item-ee69c7) | minor update | Document Intelligence C# SDKに関するクイックスタートの更新 | modified | 4 | 4 | 8 | 
| [java-sdk.md](#item-166b2e) | minor update | Document Intelligence Java SDKに関するクイックスタートの更新 | modified | 3 | 3 | 6 | 
| [javascript-sdk.md](#item-615fcd) | minor update | Document Intelligence JavaScript SDKに関するクイックスタートの更新 | modified | 2 | 2 | 4 | 
| [python-sdk.md](#item-83c83f) | minor update | Document Intelligence Python SDKに関するクイックスタートの更新 | modified | 4 | 4 | 8 | 
| [changelog-release-history.md](#item-dccdd3) | minor update | Document Intelligenceの変更履歴文書の更新 | modified | 75 | 1 | 76 | 
| [sdk-overview-v4-0.md](#item-d59a82) | minor update | Document Intelligence SDKの概要文書の更新 | modified | 6 | 6 | 12 | 
| [whats-new.md](#item-1ec8d3) | minor update | Document Intelligenceの新機能に関する文書の更新 | modified | 16 | 3 | 19 | 
| [prompt-flow-wizard.png](#item-170004) | minor update | Prompt Flowウィザードの画像の更新 | modified | 0 | 0 | 0 | 
| [trace.md](#item-b469ed) | minor update | トレース機能の有効化に関する情報を追加 | modified | 6 | 0 | 6 | 
| [langchain.md](#item-0d59f1) | minor update | LangChainの記事にトレーシング機能とデバッグ手法を追加 | modified | 172 | 16 | 188 | 
| [evaluate-results.md](#item-416e77) | minor update | 評価結果のページにマルチモーダル評価の詳細を追加 | modified | 11 | 1 | 12 | 
| [models-endpoints-ai-services-deployments.png](#item-d7d49f) | minor update | AIサービスのエンドポイントに関連する画像の更新 | modified | 0 | 0 | 0 | 
| [fine-tune-azure-ai-services.png](#item-794ba3) | minor update | Azure AIサービスのファインチューニングに関する画像の更新 | modified | 0 | 0 | 0 | 
| [ai-services-model-catalog.png](#item-94fb65) | minor update | AIサービスモデルカタログに関する画像の更新 | modified | 0 | 0 | 0 | 
| [ai-services-capabilities.png](#item-39cf6c) | minor update | AIサービスの機能に関する画像の更新 | modified | 0 | 0 | 0 | 
| [azure-ai-services-playgrounds.png](#item-4ffa5c) | minor update | Azure AIサービスプレイグラウンドに関する画像の更新 | modified | 0 | 0 | 0 | 
| [language-playground.png](#item-14b15a) | minor update | 言語プレイグラウンドに関する画像の更新 | modified | 0 | 0 | 0 | 
| [image-check-blur-image.png](#item-9357b0) | new feature | 画像のぼやけチェック結果を示す新しい画像の追加 | added | 0 | 0 | 0 | 
| [image-detail-table.png](#item-326e38) | new feature | 評価結果の詳細を示す新しい画像の追加 | added | 0 | 0 | 0 | 
| [image-per-turn-pop-up.png](#item-21f1d7) | new feature | ターンごとのポップアップ表示画像の追加 | added | 0 | 0 | 0 | 
| [langchain-portal-tracing-example.png](#item-89dbdd) | new feature | LangChainポータルトレースの例示画像の追加 | added | 0 | 0 | 0 | 
| [assistant-reply-not-grounded.png](#item-80b5c9) | breaking change | アシスタント応答が根拠のない画像の削除 | removed | 0 | 0 | 0 | 
| [get-started-playground.md](#item-e4d7fb) | minor update | クイックスタートガイドの文章修正 | modified | 0 | 2 | 2 | 
| [copilot-sdk-build-rag.md](#item-b77dba) | minor update | RAGベースのチャットアプリ構築に関するチュートリアルの修正 | modified | 7 | 3 | 10 | 
| [copilot-sdk-create-resources.md](#item-552960) | minor update | カスタム知識取得アプリ構築のためのリソース作成チュートリアルの更新 | modified | 5 | 8 | 13 | 


# Modified Contents
## articles/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api.md{#item-ed53bc}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - devx-track-js
   - devx-track-python
 ms.topic: quickstart
-ms.date: 11/19/2024
+ms.date: 12/17/2024
 ms.author: lajanuar
 zone_pivot_groups: programming-languages-set-formre
 ---
@@ -29,7 +29,7 @@ zone_pivot_groups: programming-languages-set-formre
 
 **This content applies to:** ![checkmark](../media/yes-icon.png) **v4.0 (GA)** **Earlier versions:** ![blue-checkmark](../media/blue-yes-icon.png) [v3.1 (GA)](?view=doc-intel-3.1.0&preserve-view=true) ![blue-checkmark](../media/blue-yes-icon.png) [v3.0 (GA)](?view=doc-intel-3.0.0&preserve-view=true)
 
-* Get started with Azure AI Document Intelligence latest stable version v4.0 2024-11-30 (GA).
+* Get started with Azure AI Document Intelligence latest stable version v4.0 `2024-11-30` (GA).
 
 :::moniker-end
 
@@ -53,7 +53,7 @@ zone_pivot_groups: programming-languages-set-formre
 
 * You can easily integrate document processing models into your workflows and applications by using a programming language SDK or calling the REST API.
 
-* For this quickstart, we recommend that you use the free service while you're learning the technology. Remember that the number of free pages is limited to 500 per month.
+* We recommend that you use the free service while you're learning the technology for this quickstart. Remember that the number of free pages is limited to 500 per month.
 
 To learn more about the API features and development options, visit our [Overview](../overview.md) page.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azure AI Document Intelligenceに関するクイックスタートガイドの一部の更新を示しています。主に日付の修正が行われ、公開日が2024年11月19日から2024年12月17日に変更されました。また、最新の安定版v4.0のリリース日が、コーディングブロック内で明示的にフォーマットされるようになり、より明瞭な表現となっています。さらに、クイックスタートを学ぶ際に推奨される無料サービスの利用についての文言も調整されています。このようなマイナーな更新により、情報の正確性と明確性が向上しました。

## articles/ai-services/document-intelligence/quickstarts/includes/csharp-sdk.md{#item-ee69c7}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,12 @@
 ---
-title: "Quickstart: Document Intelligence C# SDK | v4.0 | v3.1 | v3.0"
+title: "Quickstart: Document Intelligence C# SDK"
 titleSuffix: Azure AI services
 description: 'Form and document processing, data extraction, and analysis using Document Intelligence C# client library.'
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: include
-ms.date: 11/19/2024
+ms.date: 12/17/2024
 ms.author: lajanuar
 monikerRange: ">=doc-intel-3.0.0"
 ---
@@ -16,7 +16,7 @@ monikerRange: ">=doc-intel-3.0.0"
 <!-- markdownlint-disable MD029 -->
 
 :::moniker range="doc-intel-4.0.0"
-[Client library](/dotnet/api/overview/azure/ai.documentintelligence-readme?view=azure-dotnet-preview&preserve-view=true) | [SDK reference](https://azuresdkdocs.blob.core.windows.net/$web/dotnet/Azure.AI.DocumentIntelligence/1.0.0-beta.3/index.html) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package](https://www.nuget.org/packages/Azure.AI.DocumentIntelligence/1.0.0-beta.3)| [Samples]( https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/README.md)|[Supported REST API version](../../sdk-overview-v4-0.md)
+[Client library](/dotnet/api/overview/azure/cognitiveservices/documentintelligence?view=azure-dotnet&preserve-view=true) | [SDK reference](https://azuresdkdocs.blob.core.windows.net/$web/dotnet/Azure.AI.DocumentIntelligence/1.0.0/index.html) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package](https://www.nuget.org/packages/Azure.AI.DocumentIntelligence/1.0.0)| [Samples](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/README.md)|[Supported REST API version](../../sdk-overview-v4-0.md)
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
@@ -164,7 +164,7 @@ To interact with the Form Recognizer service, you need to create an instance of
 
 1. Open the **Program.cs** file.
 
-1. Delete the pre-existing code, including the line `Console.Writeline("Hello World!")`, and select one of the following code samples to copy and paste into your application's Program.cs file:
+1. Delete the existing code, including the line `Console.Writeline("Hello World!")`, and select one of the following code samples to copy and paste into your application's Program.cs file:
 
     * [**Layout model**](#layout-model)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence C# SDKに関するクイックスタートの更新"
}
```

### Explanation
この変更は、Azure AI Document IntelligenceのC# SDKに関するクイックスタートガイドのテキストを更新したものです。主な変更点は、タイトルの簡略化と日付の変更です。以前のタイトルは「Quickstart: Document Intelligence C# SDK | v4.0 | v3.1 | v3.0」でしたが、これを単に「Quickstart: Document Intelligence C# SDK」に変更しました。また、公開日が2024年11月19日から2024年12月17日に修正されました。

さらに、SDKの参照リンクやREST APIの参照リンクが最新の情報に更新され、ユーザーにとってより役立つ内容になっています。文中の指示文も微調整され、「pre-existing code」は「existing code」に改訂されています。全体として、これらの更新はドキュメントの明確性と正確性を向上させています。

## articles/ai-services/document-intelligence/quickstarts/includes/java-sdk.md{#item-166b2e}

<details>
<summary>Diff</summary>
````diff
@@ -1,19 +1,19 @@
 ---
-title: "Quickstart: Document Intelligence Java SDK (beta) | v3.1 | v3.0"
+title: "Quickstart: Document Intelligence Java SDK"
 titleSuffix: Azure AI services
 description: Form and document processing, data extraction, and analysis using Document Intelligence Java client library.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: include
-ms.date: 11/19/2024
+ms.date: 12/17/2024
 ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD025 -->
 <!-- markdownlint-disable MD036 -->
 
 :::moniker range="doc-intel-4.0.0"
-[Client library](/java/api/overview/azure/ai-documentintelligence-readme?view=azure-java-preview&preserve-view=true) | [SDK reference](https://azuresdkdocs.blob.core.windows.net/$web/java/azure-ai-documentintelligence/1.0.0-beta.4/index.html) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package (Maven)](https://mvnrepository.com/artifact/com.azure/azure-ai-documentintelligence/1.0.0-beta.4) | [Samples](https://github.com/Azure/azure-sdk-for-java/tree/azure-ai-documentintelligence_1.0.0-beta.4/sdk/documentintelligence/azure-ai-documentintelligence/src/samples) |[Supported REST API version](../../sdk-overview-v4-0.md)
+[Client library](/java/api/overview/azure/ai-documentintelligence-readme?view=azure-java-preview&preserve-view=true) | [SDK reference](https://azuresdkdocs.blob.core.windows.net/$web/java/azure-ai-documentintelligence/1.0.0/index.html) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package (Maven)](https://mvnrepository.com/artifact/com.azure/azure-ai-documentintelligence/1.0.0-beta.4) | [Samples](https://github.com/Azure/azure-sdk-for-java/tree/azure-ai-documentintelligence_1.0.0/sdk/documentintelligence/azure-ai-documentintelligence/src/samples#examples) |[Supported REST API version](../../sdk-overview-v4-0.md)
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence Java SDKに関するクイックスタートの更新"
}
```

### Explanation
この変更は、Azure AI Document IntelligenceのJava SDKに関するクイックスタートガイドの内容を更新したものです。主な変更点は、タイトルの簡略化と日付の修正です。以前のタイトルは「Quickstart: Document Intelligence Java SDK (beta) | v3.1 | v3.0」でしたが、これを「Quickstart: Document Intelligence Java SDK」に変更しました。この変更により、現在の内容により焦点を当てた表現になっています。

また、日付の修正も行われ、2024年11月19日から2024年12月17日に更新されました。さらに、Java SDKに関するリンクが最新の情報に更新され、SDKリファレンスやREST APIリファレンスへのリンクが改善されました。全体として、これらのマイナーな修正は、ドキュメントの明確さと正確さを向上させています。

## articles/ai-services/document-intelligence/quickstarts/includes/javascript-sdk.md{#item-615fcd}

<details>
<summary>Diff</summary>
````diff
@@ -6,13 +6,13 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: include
-ms.date: 11/19/2024
+ms.date: 12/17/2024
 ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD025 -->
 
 :::moniker range="doc-intel-4.0.0"
-[Client library](/javascript/api/overview/azure/ai-document-intelligence-rest-readme?view=azure-node-preview&preserve-view=true) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package (npm)](https://www.npmjs.com/package/@azure-rest/ai-document-intelligence/v/1.0.0-beta.3) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest/samples/v1-beta) |[Supported REST API version](../../sdk-overview-v4-0.md)
+[Client library](/javascript/api/overview/azure/ai-document-intelligence-rest-readme?view=azure-node-latest&preserve-view=true) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package (npm)]( https://www.npmjs.com/package/@azure-rest/ai-document-intelligence/v/1.0.0) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest/samples/v1-beta) |[Supported REST API version](../../sdk-overview-v4-0.md)
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence JavaScript SDKに関するクイックスタートの更新"
}
```

### Explanation
この変更は、Azure AI Document IntelligenceのJavaScript SDKに関するクイックスタートガイドの内容を改善するためのマイナーな更新です。主な変更点は、日付の修正とURLの更新です。具体的には、公開日が2024年11月19日から2024年12月17日に変更されました。

また、クライアントライブラリのリンクが最新の情報に調整され、以前のバージョンのリンクから最新バージョンのリファレンスに変更されました。これにより、ユーザーは最新のSDKおよびAPIをより容易に参照できるようになっています。全体として、これらの修正はドキュメントの正確さと利用価値を向上させています。

## articles/ai-services/document-intelligence/quickstarts/includes/python-sdk.md{#item-83c83f}

<details>
<summary>Diff</summary>
````diff
@@ -6,13 +6,13 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: include
-ms.date: 11/19/2024
+ms.date: 12/17/2024
 ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD025 -->
 
 :::moniker range="doc-intel-4.0.0"
-[Client library](/python/api/overview/azure/ai-documentintelligence-readme?view=azure-python-preview&preserve-view=true) |[SDK reference](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-documentintelligence/1.0.0b4/index.html) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package (PyPi)](https://pypi.org/project/azure-ai-documentintelligence/1.0.0b4/) | [Samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/documentintelligence/azure-ai-documentintelligence/samples) | [Supported REST API version](../../sdk-overview-v4-0.md#supported-programming-languages)
+[Client library](/python/api/overview/azure/ai-documentintelligence-readme?view=azure-python-preview&preserve-view=true) |[SDK reference](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-documentintelligence/latest/index.html) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package (PyPi)](https://pypi.org/project/azure-ai-documentintelligence/1.0.0b4/) | [Samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/documentintelligence/azure-ai-documentintelligence/samples) | [Supported REST API version](../../sdk-overview-v4-0.md#supported-programming-languages)
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
@@ -249,7 +249,7 @@ After you add a code sample to your application, build and run your program:
 
 :::moniker range="doc-intel-3.1.0"
 
-To analyze a given file at a URL, you'll use the `begin_analyze_document_from_url` method and pass in `prebuilt-layout` as the model Id. The returned value is a `result` object containing data about the submitted document.
+To analyze a given file at a URL, use the `begin_analyze_document_from_url` method and pass in `prebuilt-layout` as the model ID. The returned value is a `result` object containing data about the submitted document.
 
 **Add the following code sample to your form_recognizer_quickstart.py application. Make sure you update the key and endpoint variables with values from your Azure portal Form Recognizer instance:**
 
@@ -778,7 +778,7 @@ After you add a code sample to your application, build and run your program:
 
 :::moniker range="doc-intel-3.1.0"
 
-To analyze a given file at a URI, you'll use the `begin_analyze_document_from_url` method and pass `prebuilt-invoice` as the model Id. The returned value is a `result` object containing data about the submitted document.
+To analyze a given file at a URI, use the `begin_analyze_document_from_url` method and pass `prebuilt-invoice` as the model ID. The returned value is a `result` object containing data about the submitted document.
 
 **Add the following code sample to your form_recognizer_quickstart.py application. Make sure you update the key and endpoint variables with values from your Azure portal Form Recognizer instance:**
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence Python SDKに関するクイックスタートの更新"
}
```

### Explanation
この変更は、Azure AI Document IntelligenceのPython SDKに関するクイックスタートガイドの内容を更新したものです。主な変更点は3つです。

1. **日付の更新**: ドキュメントの公開日が2024年11月19日から2024年12月17日に変更されました。
   
2. **リンクの更新**: クライアントライブラリのSDKリファレンスリンクが最新のバージョンに変更され、以前の特定バージョンから最新バージョンへとリダイレクトされるようになっています。これにより、ユーザーは最新情報に容易にアクセスできるようになります。

3. **文言の修正**: コードサンプルに関連する説明が、より直感的な表現に更新されています。具体的には、"you'll use" から "use" に修正され、より直接的な指示に変わっています。これにより、ユーザーが手順を理解しやすくなります。

全体として、これらの更新はドキュメントの明確さと正確さを向上させ、ユーザーにとっての価値を高めるものとなっています。

## articles/ai-services/document-intelligence/versioning/changelog-release-history.md{#item-dccdd3}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: reference
-ms.date: 11/19/2024
+ms.date: 12/17/2024
 ms.author: lajanuar
 ---
 
@@ -19,6 +19,80 @@ ms.author: lajanuar
 
 This reference article provides a version-based description of Document Intelligence feature and capability releases, changes, updates, and enhancements.
 
+#### December 2024 (GA) release
+
+
+### [**.NET (C#)**](#tab/csharp)
+
+* Document Intelligence **1.0.0**
+* **Targets REST API 2024-11-30 (GA) by default**
+
+[**Changelog/Release History**](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/CHANGELOG.md#100-2024-12-16)
+
+[**Package (NuGet)**](https://www.nuget.org/packages/Azure.AI.DocumentIntelligence/1.0.0)
+
+[**Azure SDK for .NET**](/dotnet/api/overview/azure/cognitiveservices/documentintelligence?view=azure-dotnet&preserve-view=true)
+
+[**ReadMe**](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/README.md)
+
+[**Samples**](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/README.md)
+
+[**Migration guide**](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/MigrationGuide.md)
+
+### [**Java**](#tab/java)
+
+* Document Intelligence **1.0.0**
+* **Targets REST API 2024-11-30 (GA) by default**
+
+[**Changelog/Release History**](https://github.com/Azure/azure-sdk-for-java/blob/azure-ai-documentintelligence_1.0.0/sdk/documentintelligence/azure-ai-documentintelligence/CHANGELOG.md#100-2024-12-16)
+
+[**Package Maven**](https://central.sonatype.com/artifact/com.azure/azure-ai-documentintelligence/1.0.0)
+
+[**Azure SDK for Java**](/java/api/com.azure.ai.documentintelligence?view=azure-java-stable&preserve-view=true)
+
+[**ReadMe**](https://github.com/Azure/azure-sdk-for-java/blob/azure-ai-documentintelligence_1.0.0/sdk/documentintelligence/azure-ai-documentintelligence/README.md)
+
+[**Samples**](https://github.com/Azure/azure-sdk-for-java/tree/azure-ai-documentintelligence_1.0.0/sdk/documentintelligence/azure-ai-documentintelligence/src/samples#examples)
+
+[**Migration guide**](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/MIGRATION_GUIDE.md)
+
+### [**JavaScript**](#tab/javascript)
+
+* Document Intelligence **1.0.0**
+* **Targets REST API 2024-11-30 (GA) by default**
+
+[**Changelog/Release History**](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/documentintelligence/ai-document-intelligence-rest/CHANGELOG.md#100-2024-12-16)
+
+[**Package (npm)**](https://www.npmjs.com/package/@azure-rest/ai-document-intelligence/v/1.0.0)
+
+[**Azure SDK for JavaScript**](/javascript/api/%40azure-rest/ai-document-intelligence/?view=azure-node-latest&preserve-view=true)
+
+[**ReadMe**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest#azure-documentintelligence-formerly-formrecognizer-rest-client-library-for-javascript)
+
+[**Samples**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest/samples/v1)
+
+[**Migration guide**](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/documentintelligence/ai-document-intelligence-rest/MIGRATION-FR_v4-DI_v1.md)
+
+### [**Python**](#tab/python)
+
+* Document Intelligence **1.0.0**
+* **Targets REST API 2024-11-30 (GA) by default**
+
+[**Changelog/Release History**](https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-documentintelligence_1.0.0/sdk/documentintelligence/azure-ai-documentintelligence/CHANGELOG.md#100-2024-12-17)
+
+[**Package (PyPi)**](https://pypi.org/project/azure-ai-documentintelligence/1.0.0/)
+
+[**Azure SDK for Python**](/python/api/overview/azure/ai-documentintelligence-readme?view=azure-python&preserve-view=true)
+
+[**ReadMe**](https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-documentintelligence_1.0.0/sdk/documentintelligence/azure-ai-documentintelligence/README.md)
+
+[**Samples**](https://github.com/Azure/azure-sdk-for-python/tree/azure-ai-documentintelligence_1.0.0/sdk/documentintelligence/azure-ai-documentintelligence/samples)
+
+[**Migration guide**](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/MIGRATION_GUIDE.md)
+
+---
+
+
 #### August 2024 (preview) release
 
 ### [**.NET (C#)**](#tab/csharp)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligenceの変更履歴文書の更新"
}
```

### Explanation
この変更は、Azure AI Document Intelligenceの「変更履歴」文書に関するマイナーな更新を反映したものです。主な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの公開日が2024年11月19日から2024年12月17日に変更され、最新情報が反映されました。

2. **新しいリリース情報の追加**: 2024年12月のGA（一般提供）リリースに関する詳細が追加されました。これには、.NET、Java、JavaScript、およびPythonに関するDocument Intelligenceのバージョン1.0.0の説明が含まれ、各プログラミング言語のSDK、パッケージリンク、およびマイグレーションガイドが新たに示されています。これにより、開発者は新機能に簡単にアクセスし、利用できるようになります。

3. **変更履歴の整理**: 各言語のセクションが一貫した形式で整理され、リンクが明確に分かれて表示されるようになりました。これにより、ユーザー体験が向上し、必要な情報を迅速に見つけることが可能となります。

これらの変更は、Document Intelligenceの最新機能をユーザーが理解しやすくするために設計されており、情報の透明性が促進されています。

## articles/ai-services/document-intelligence/versioning/sdk-overview-v4-0.md{#item-d59a82}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - devx-track-js
   - devx-track-python
 ms.topic: conceptual
-ms.date: 11/19/2024
+ms.date: 12/17/2024
 ms.author: lajanuar
 monikerRange: 'doc-intel-4.0.0'
 --- 
@@ -22,7 +22,7 @@ monikerRange: 'doc-intel-4.0.0'
 <!-- markdownlint-disable MD001 -->
 <!-- markdownlint-disable MD051 -->
 
-# SDK target: REST API v4.0
+# SDK target: REST API v4.0 (GA)
 
 ![Document Intelligence checkmark](../media/yes-icon.png) **REST API version 2024-11-30 GA**
 
@@ -34,10 +34,10 @@ Document Intelligence SDK supports the following languages and platforms:
 
 | Language → Document Intelligence SDK version &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| Package| Supported API version &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| Platform support |
 |:----------------------:|:----------|:----------| :----------------:|
-| [**.NET/C# → 1.0.0-beta.3 (preview)**](/dotnet/api/overview/azure/ai.documentintelligence-readme?view=azure-dotnet-preview&preserve-view=true)|[NuGet](https://www.nuget.org/packages/Azure.AI.DocumentIntelligence/1.0.0-beta.3)|[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)|[Windows, macOS, Linux, Docker](https://dotnet.microsoft.com/download)|
-|[**Java → 1.0.0-beta.4 (preview)**](/java/api/overview/azure/ai-documentintelligence-readme?view=azure-java-preview&preserve-view=true) |[Maven repository](https://mvnrepository.com/artifact/com.azure/azure-ai-documentintelligence/1.0.0-beta.4) |[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)|[Windows, macOS, Linux](/java/openjdk/install)|
-|[**JavaScript → 1.0.0-beta.3 (preview)**](/javascript/api/overview/azure/ai-document-intelligence-rest-readme?view=azure-node-preview&preserve-view=true)| [npm](https://www.npmjs.com/package/@azure-rest/ai-document-intelligence/v/1.0.0-beta.3)|[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)| [Browser, Windows, macOS, Linux](https://nodejs.org/en/download/) |
-|[**Python → 1.0.0b4 (preview)**](/python/api/overview/azure/ai-documentintelligence-readme?view=azure-python-preview&preserve-view=true) | [PyPI](https://pypi.org/project/azure-ai-documentintelligence/1.0.0b4/)|[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)|[Windows, macOS, Linux](/azure/developer/python/configure-local-development-environment?tabs=windows%2Capt%2Ccmd#use-the-azure-cli)|
+| [**.NET/C# → 1.0.0 (GA)**](/dotnet/api/overview/azure/cognitiveservices/documentintelligence?view=azure-dotnet&preserve-view=true)|[NuGet](https://www.nuget.org/packages/Azure.AI.DocumentIntelligence/1.0.0)|[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)|[Windows, macOS, Linux, Docker](https://dotnet.microsoft.com/download)|
+|[**Java → 1.0.0 (GA**](/java/api/com.azure.ai.documentintelligence?view=azure-java-stable&preserve-view=true) |[Maven repository](https://central.sonatype.com/artifact/com.azure/azure-ai-documentintelligence/1.0.0) |[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)|[Windows, macOS, Linux](/java/openjdk/install)|
+|[**JavaScript → 1.0.0 (GA)**](/javascript/api/%40azure-rest/ai-document-intelligence/?view=azure-node-latest&preserve-view=true)| [npm](https://www.npmjs.com/package/@azure-rest/ai-document-intelligence/v/1.0.0)|[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)| [Browser, Windows, macOS, Linux](https://nodejs.org/en/download/) |
+|[**Python → 1.0.0b4 (preview)**](/python/api/overview/azure/ai-documentintelligence-readme?view=azure-python&preserve-view=true) | [PyPI](https://pypi.org/project/azure-ai-documentintelligence/1.0.0/)|[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)|[Windows, macOS, Linux](/azure/developer/python/configure-local-development-environment?tabs=windows%2Capt%2Ccmd#use-the-azure-cli)|
 
 For more information on other SDK versions, see:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence SDKの概要文書の更新"
}
```

### Explanation
この変更は、Azure AI Document IntelligenceのSDKに関する概要文書を更新したものです。主な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの日付が2024年11月19日から2024年12月17日に変更され、最新のリリース情報が反映されています。

2. **SDKターゲットのバージョン表記修正**: SDKのターゲットが「REST API v4.0」から「REST API v4.0 (GA)」に変更されたことで、提供されるAPIの状態が明確になりました。これにより、ユーザーはAPIのリリースが安定版であることを理解しやすくなります。

3. **言語別SDKのバージョン表示変更**: 各プログラミング言語（.NET、Java、JavaScript、Python）について、SDKのバージョンがプレビュー版から正式版（GA）に更新され、それぞれの最新のパッケージリンクも変更されました。これにより、開発者は安定版のSDKを容易に見つけ、利用できるようになります。

これにより、ドキュメントはユーザーが利用可能なSDKの最新情報をよりわかりやすく提供するものとなり、開発者にとっての利便性が向上しています。

## articles/ai-services/document-intelligence/whats-new.md{#item-1ec8d3}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: whats-new
-ms.date: 11/19/2024
+ms.date: 12/17/2024
 ms.author: lajanuar
 ms.custom:
   - references_regions
@@ -25,11 +25,24 @@ ms.custom:
 Document Intelligence service is updated on an ongoing basis. Bookmark this page to stay up to date with release notes, feature enhancements, and our newest documentation.
 
 > [!IMPORTANT]
-> Preview API versions are retired once the GA API is released. The 2023-02-28-preview API version is being retired, if you are still using the preview API or the associated SDK versions, please update your code to target the latest API version 2023-07-31 (GA). </br>
+> Preview API versions are retired once the GA API is released. The 2023-02-28-preview API version is being retired, if you are still using the preview API or the associated SDK versions, please update your code to target the latest API version 2024-11-30 (GA). </br>
+
+## December 2024
+
+**Document Intelligence v4.0 programming language SDKs are now generally available (GA)**! <br><br>The latest client SDKs default to the [**2024-11-30 REST API (GA)**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) version of the service.<br><br>
+For more information, *see* client libraries for the following supported programming languages:
+
+* [🆕 .NET (C#)](versioning/changelog-release-history.md?view=doc-intel-4.0.0&tabs=csharp&preserve-view=true)
+
+* [🆕 Java](versioning/changelog-release-history.md?view=doc-intel-4.0.0&tabs=java&preserve-view=true)
+
+* [🆕 JavaScript](versioning/changelog-release-history.md?view=doc-intel-4.0.0&tabs=javascript&preserve-view=true)
+
+* [🆕 Python](versioning/changelog-release-history.md?view=doc-intel-4.0.0&tabs=python&preserve-view=true)
 
 ## November 2024
 
-**Document Intelligence v4.0 (2024-11-30) is now generally available (GA)**! The API version corresponds to 2024-11-30. The v4.0 API includes the following changes as listed:
+**Document Intelligence REST API v4.0: [**2024-11-30 REST API (GA)**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) is now generally available (GA)**! The v4.0 REST API includes the following changes:
 
 * [🆕 Batch API](concept-batch-analysis.md)
   * Batch API now supports all models, including all read, layout, prebuilt verticals, and custom models.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligenceの新機能に関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Document Intelligenceの「新機能」文書を更新したもので、主な修正内容は以下の通りです。

1. **日付の更新**: ドキュメントの日付が2024年11月19日から2024年12月17日に変更され、新しい情報に基づいて内容が最新化されました。

2. **APIバージョンの更新**: 旧バージョンのAPI（2023-02-28-preview）が廃止され、2024年11月30日付の最新のGA（一般提供）APIが登場したことに関連する情報が追加されました。これにより、開発者は最新のAPIを利用するよう促されます。

3. **新機能の紹介**: 2024年12月にはDocument Intelligence v4.0のプログラミング言語SDKが一般提供（GA）されることが明記され、最新のクライアントSDKが2024-11-30 REST API（GA）バージョンをデフォルトでターゲットとしていることが説明されています。

4. **プログラミング言語SDKのリンク追加**: .NET、Java、JavaScript、Pythonの最新SDKへのリンクが追加され、開発者が簡単に必要な情報にアクセスできるようになっています。

これにより、ユーザーはDocument Intelligenceの最新の状態とリリース情報を把握しやすくなり、開発環境を最新のものに保つための手助けが行われています。

## articles/ai-services/language-service/media/prompt-flow/prompt-flow-wizard.png{#item-170004}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Prompt Flowウィザードの画像の更新"
}
```

### Explanation
この変更は、Azure AI Language Serviceの「Prompt Flow」ウィザードに関連する画像を更新したものです。具体的には、画像ファイル `prompt-flow-wizard.png` が改変されましたが、追加や削除された内容はありません。この更新は、画像自体の品質や内容を改善することを目的としていると考えられます。

画像の変更により、ユーザーはPrompt Flowウィザードの最新のビジュアルを確認でき、より直感的にサービスを利用できるようになります。このようなビジュアルの更新は、ドキュメントの理解を助け、ユーザーエクスペリエンスを向上させるために重要です。

## articles/ai-studio/concepts/trace.md{#item-b469ed}

<details>
<summary>Diff</summary>
````diff
@@ -63,6 +63,12 @@ Trace exporters are responsible for sending trace data to a backend system for s
 
 Trace visualization refers to the graphical representation of trace data. Azure AI integrates with visualization tools like Azure AI Foundry Tracing, Aspire dashboard, and Prompty Trace viewer  to provide developers with an intuitive way to explore and analyze traces, helping them to quickly identify issues and understand the behavior of their applications.
 
+## Enable tracing
+
+In order to enable tracing, you need to add an Application Insights resource to your Azure AI Foundry project. To add an Application Insights resource, navigate to the **Tracing** tab in the [AI Foundry portal](https://ai.azure.com/), and create a new resource if you don't already have one.
+
+:::image type="content" source="../../ai-services/agents/media/ai-foundry-tracing.png" alt-text="A screenshot of the tracing screen in the AI Foundry portal." lightbox="../../ai-services/agents/media/ai-foundry-tracing.png":::
+
 ## Conclusion
 
 Azure AI's tracing capabilities are designed to empower developers with the tools they need to gain deep insights into their AI applications. By providing a robust, intuitive, and scalable tracing feature, Azure AI helps reduce debugging time, enhance application reliability, and improve overall performance. With a focus on user experience and system observability, Azure AI's tracing solution is set to revolutionize the way developers interact with and understand their Gen AI applications.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トレース機能の有効化に関する情報を追加"
}
```

### Explanation
この変更は、Azure AI Studioの「トレース」に関する文書を更新し、トレース機能を有効化するための手順を追加したものです。具体的には、以下のような変更が行われました。

1. **トレース機能の有効化**: ユーザーがトレース機能を有効にするために必要な手順として、Azure AI FoundryプロジェクトにApplication Insightsリソースを追加する方法が明記されました。この説明により、ユーザーはトレース機能を容易に利用開始できるようになります。

2. **手順の具体化**: AI Foundryポータルの「Tracing」タブに移動し、既存のリソースがない場合は新しいリソースを作成する必要があることが説明されています。

3. **画像の追加**: トレース機能の設定画面を示すスクリーンショットが挿入され、視覚的な情報が提供されています。これにより、ユーザーが手順をより理解しやすくなっています。

この情報の追加によって、Azure AIのトレース機能に対する理解と利用が向上し、ユーザーは自分のAIアプリケーションのパフォーマンスを効率的に監視および分析できるようになります。

## articles/ai-studio/how-to/develop/langchain.md{#item-0d59f1}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ To run this tutorial, you need:
 
     * You can follow the instructions at [Deploy models as serverless APIs](../deploy-models-serverless.md).
 
-* Python 3.8 or later installed, including pip.
+* Python 3.9 or later installed, including pip.
 * LangChain installed. You can do it with:
 
     ```bash
@@ -73,7 +73,7 @@ Once configured, create a client to connect to the endpoint. In this case, we ar
 
 ```python
 import os
-from langchain_azure_ai import AzureAIChatCompletionsModel
+from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
 
 model = AzureAIChatCompletionsModel(
     endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
@@ -88,7 +88,7 @@ If your endpoint is serving more than one model, like with the [Azure AI model i
 
 ```python
 import os
-from langchain_azure_ai import AzureAIChatCompletionsModel
+from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
 
 model = AzureAIChatCompletionsModel(
     endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
@@ -97,16 +97,17 @@ model = AzureAIChatCompletionsModel(
 )
 ```
 
-Alternatively, if your endpoint support Microsoft Entra ID, you can use the following code to create the client:
+You can use the following code to create the client if your endpoint supports Microsoft Entra ID:
 
 ```python
 import os
 from azure.identity import DefaultAzureCredential
-from langchain_azure_ai import AzureAIChatCompletionsModel
+from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
 
 model = AzureAIChatCompletionsModel(
     endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
     credential=DefaultAzureCredential(),
+    model_name="mistral-large-2407",
 )
 ```
 
@@ -119,11 +120,12 @@ If you are planning to use asynchronous calling, it's a best practice to use the
 from azure.identity.aio import (
     DefaultAzureCredential as DefaultAzureCredentialAsync,
 )
-from langchain_azure_ai import AzureAIChatCompletionsModel
+from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
 
 model = AzureAIChatCompletionsModel(
     endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
     credential=DefaultAzureCredentialAsync(),
+    model_name="mistral-large-2407",
 )
 ```
 
@@ -145,7 +147,6 @@ model.invoke(messages)
 You can also compose operations as needed in what's called **chains**. Let's now use a prompt template to translate sentences:
 
 ```python
-from langchain_core.prompts import ChatPromptTemplate
 from langchain_core.output_parsers import StrOutputParser
 
 system_template = "Translate the following into {language}:"
@@ -157,6 +158,7 @@ prompt_template = ChatPromptTemplate.from_messages(
 As you can see from the prompt template, this chain has a `language` and `text` input. Now, let's create an output parser:
 
 ```python
+from langchain_core.prompts import ChatPromptTemplate
 parser = StrOutputParser()
 ```
 
@@ -180,9 +182,11 @@ chain.invoke({"language": "italian", "text": "hi"})
 
 Models deployed to Azure AI Foundry support the Azure AI model inference API, which is standard across all the models. Chain multiple LLM operations based on the capabilities of each model so you can optimize for the right model based on capabilities. 
 
-In the following example, we create 2 model clients, one is a producer and another one is a verifier. To make the distinction clear, we are using a multi-model endpoint like the [Azure AI model inference service](../../ai-services/model-inference.md) and hence we are passing the parameter `model_name` to use a `Mistral-Large` and a `Mistral-Small` model, quoting the fact that **producing content is more complex than verifying it**.
+In the following example, we create two model clients, one is a producer and another one is a verifier. To make the distinction clear, we are using a multi-model endpoint like the [Azure AI model inference service](../../ai-services/model-inference.md) and hence we are passing the parameter `model_name` to use a `Mistral-Large` and a `Mistral-Small` model, quoting the fact that **producing content is more complex than verifying it**.
 
 ```python
+from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
+
 producer = AzureAIChatCompletionsModel(
     endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
     credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
@@ -196,15 +200,20 @@ verifier = AzureAIChatCompletionsModel(
 )
 ```
 
+> [!TIP]
+> Explore the model card of each of the models to understand the best use cases for each model.
+
 The following example generates a poem written by an urban poet:
 
 ```python
+from langchain_core.prompts import PromptTemplate
+
 producer_template = PromptTemplate(
     template="You are an urban poet, your job is to come up \
              verses based on a given topic.\n\
              Here is the topic you have been asked to generate a verse on:\n\
              {topic}",
-    input_variables=["topic"]
+    input_variables=["topic"],
 )
 
 verifier_template = PromptTemplate(
@@ -213,14 +222,25 @@ verifier_template = PromptTemplate(
               report it. Your response should be only one word either True or False.\n \
               Here is the lyrics submitted to you:\n\
               {input}",
-    input_variables=["input"]
+    input_variables=["input"],
 )
 ```
 
 Now let's chain the pieces:
 
 ```python
-chain = producer_template | producer | parser | verifier_template | verifier
+chain = producer_template | producer | parser | verifier_template | verifier | parser
+```
+
+The previous chain returns the output of the step `verifier` only. Since we want to access the intermediate result generated by the `producer`, in LangChain you need to use a `RunnablePassthrough` object to also output that intermediate step. The following code shows how to do it:
+
+```python
+from langchain_core.runnables import RunnablePassthrough, RunnableParallel
+
+generate_poem = producer_template | producer | parser
+verify_poem = verifier_template | verifier | parser
+
+chain = generate_poem | RunnableParallel(poem=RunnablePassthrough(), verification=RunnablePassthrough() | verify_poem)
 ```
 
 To invoke the chain, identify the inputs required and provide values using the `invoke` method:
@@ -229,9 +249,12 @@ To invoke the chain, identify the inputs required and provide values using the `
 chain.invoke({"topic": "living in a foreign country"})
 ```
 
-> [!TIP]
-> Explore the model card of each of the models to understand the best use cases for each model.
-
+```output
+{
+  "peom": "...",
+  "verification: "false"
+}
+```
 
 ## Use embeddings models
 
@@ -250,6 +273,7 @@ from langchain_azure_ai.embeddings import AzureAIEmbeddingsModel
 embed_model = AzureAIEmbeddingsModel(
     endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
     credential=os.environ['AZURE_INFERENCE_CREDENTIAL'],
+    model_name="text-embedding-3-large",
 )
 ```
 
@@ -286,7 +310,7 @@ for doc in results:
 If you are using Azure OpenAI service or Azure AI model inference service with OpenAI models with `langchain-azure-ai` package, you may need to use `api_version` parameter to select a specific API version. The following example shows how to connect to an Azure OpenAI model deployment in Azure OpenAI service:
 
 ```python
-from langchain_azure_ai import AzureAIChatCompletionsModel
+from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
 
 llm = AzureAIChatCompletionsModel(
     endpoint="https://<resource>.openai.azure.com/openai/deployments/<deployment-name>",
@@ -301,7 +325,7 @@ llm = AzureAIChatCompletionsModel(
 If the deployment is hosted in Azure AI Services, you can use the Azure AI model inference service:
 
 ```python
-from langchain_azure_ai import AzureAIChatCompletionsModel
+from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
 
 llm = AzureAIChatCompletionsModel(
     endpoint="https://<resource>.services.ai.azure.com/models",
@@ -311,8 +335,140 @@ llm = AzureAIChatCompletionsModel(
 )
 ```
 
+## Debugging and troubleshooting
+
+If you need to debug your application and understand the requests sent to the models in Azure AI Foundry, you can use the debug capabilities of the integration as follows:
+
+First, configure logging to the level you are interested in:
+
+```python
+import sys
+import logging
+
+# Acquire the logger for this client library. Use 'azure' to affect both
+# 'azure.core` and `azure.ai.inference' libraries.
+logger = logging.getLogger("azure")
+
+# Set the desired logging level. logging.INFO or logging.DEBUG are good options.
+logger.setLevel(logging.DEBUG)
+
+# Direct logging output to stdout:
+handler = logging.StreamHandler(stream=sys.stdout)
+# Or direct logging output to a file:
+# handler = logging.FileHandler(filename="sample.log")
+logger.addHandler(handler)
+
+# Optional: change the default logging format. Here we add a timestamp.
+formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
+handler.setFormatter(formatter)
+```
+
+To see the payloads of the requests, when instantiating the client, pass the argument `logging_enable`=`True` to the `client_kwargs`:
+
+```python
+import os
+from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
+
+model = AzureAIChatCompletionsModel(
+    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
+    model_name="mistral-large-2407",
+    client_kwargs={"logging_enable": True},
+)
+```
+
+Use the client as usual in your code.
+
+## Tracing
+
+You can use the tracing capabilities in Azure AI Foundry by creating a tracer. Logs are stored in Azure Application Insights and can be queried at any time using Azure Monitor or Azure AI Foundry portal. Each AI Hub has an Azure Application Insights associated with it.
+
+### Get your instrumentation connection string
+
+You can configure your application to send telemetry to Azure Application Insights either by:
+
+1. Using the connection string to Azure Application Insights directly:
+
+    1. Go to [Azure AI Foundry portal](https://ai.azure.com) and select **Tracing**.
+
+    2. Select **Manage data source**. In this screen you can see the instance that is associated with the project.
+
+    3. Copy the value at **Connection string** and set it to the following variable:
+
+        ```python
+        import os
+      
+        application_insights_connection_string = "instrumentation...."
+        ```
+
+2. Using the Azure AI Foundry SDK and the project connection string.
+
+    1. Ensure you have the package `azure-ai-projects` installed in your environment.
+
+    2. Go to [Azure AI Foundry portal](https://ai.azure.com).
+    
+    3. Copy your project's connection string and set it the following code:
+
+        ```python
+        from azure.ai.projects import AIProjectClient
+        from azure.identity import DefaultAzureCredential
+        
+        project_client = AIProjectClient.from_connection_string(
+            credential=DefaultAzureCredential(),
+            conn_str="<your-project-connection-string>",
+        )
+        
+        application_insights_connection_string = project_client.telemetry.get_connection_string()
+        ```
+
+### Configure tracing for Azure AI Foundry
+
+The following code creates a tracer connected to the Azure Application Insights behind a project in Azure AI Foundry. Notice that the parameter `enable_content_recording` is set to `True`. This enables the capture of the inputs and outputs of the entire application as well as the intermediate steps. Such is helpful when debugging and building applications, but you may want to disable it on production environments. It defaults to the environment variable `AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED`:
+
+```python
+from langchain_azure_ai.callbacks.tracers import AzureAIInferenceTracer
+
+tracer = AzureAIInferenceTracer(
+    connection_string=application_insights_connection_string,
+    enable_content_recording=True,
+)
+```
+
+To configure tracing with your chain, indicate the value config in the `invoke` operation as a callback:
+
+```python
+chain.invoke({"topic": "living in a foreign country"}, config={"callbacks": [tracer]})
+```
+
+To configure the chain itself for tracing, use the `.with_config()` method:
+
+```python
+chain = chain.with_config({"callbacks": [tracer]})
+```
+
+Then use the `invoke()` method as usual:
+
+```python
+chain.invoke({"topic": "living in a foreign country"})
+```
+
+### View traces
+
+To see traces:
+
+1. Go to [Azure AI Foundry portal](https://ai.azure.com).
+
+2. Navigate to **Tracing** section.
+
+3. Identify the trace you have created. It may take a couple of seconds for the trace to show.
+
+    :::image type="content" source="../../media/how-to/develop-langchain/langchain-portal-tracing-example.png" alt-text="A screenshot showing the trace of a chain." lightbox="../../media/how-to/develop-langchain/langchain-portal-tracing-example.png":::
+
+Learn more about [how to visualize and manage traces](visualize-traces.md).
+
 ## Next steps
 
 * [Develop applications with LlamaIndex](llama-index.md)
+* [Visualize and manage traces in Azure AI Foundry](visualize-traces.md)
 * [Use the Azure AI model inference service](../../ai-services/model-inference.md)
 * [Reference: Azure AI model inference API](../../reference/reference-model-inference-api.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "LangChainの記事にトレーシング機能とデバッグ手法を追加"
}
```

### Explanation
この変更は、Azure AI Studioの「LangChain」に関する文書を大幅に更新し、トレーシング機能とデバッグ手法に関する詳細を追加したものです。具体的には、172行の新しい情報が追加され、16行が削除され、全体で188行の変更がありました。主なポイントは以下の通りです。

1. **Pythonのバージョン要件の更新**: LangChainを使用するために必要なPythonのバージョンが3.8から3.9以上に更新されました。

2. **トレース機能の導入**: Azure AI Foundryでのアプリケーションのトレースを設定するための手順が詳細に説明されています。これにより、ユーザーはアプリケーションの実行時にどのようなデータが送信されているかを簡単に把握できるようになります。

3. **デバッグ手法の追加**: ログの設定方法と、クライアントのインスタンスを生成する際にリクエストのペイロードを確認するためのオプションが追加されています。これにより、開発者はエラーの原因を迅速に特定し、アプリケーションの信頼性を向上させることができます。

4. **新しいサンプルコードの提供**: 具体的なコード例が追加され、ユーザーは新しいトレーシング機能やデバッグ方法をすぐに試すことができるようになっています。特に、Azure Application Insightsへの接続やトレーシングの設定方法が詳しく説明されています。

この更新により、LangChainを使用する開発者は、アプリケーションの動作をより良く理解し、問題解決に役立つ強力なツールを手に入ることが期待されます。

## articles/ai-studio/how-to/evaluate-results.md{#item-416e77}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 12/18/2024
 ms.reviewer: wenxwei
 ms.author: lagayhar
 author: lgayhardt
@@ -92,6 +92,16 @@ For multi-turn conversation scenario, you can select “View evaluation results
 
 :::image type="content" source="../media/evaluations/view-results/metric-per-turn.png" alt-text="Screenshot of evaluation results per turn." lightbox="../media/evaluations/view-results/metric-per-turn.png":::
 
+For a safety evaluation in a multi-modal scenario (text + images), you can review the images from both the input and output in the detailed metrics result table to better understand the evaluation result. Since multi-modal evaluation is currently supported only for conversation scenarios, you can select "View evaluation results per turn" to examine the input and output for each turn.  
+
+:::image type="content" source="../media/evaluations/view-results/image-detail-table.png" alt-text="Screenshot of detailed metrics results." lightbox="../media/evaluations/view-results/image-detail-table.png":::
+
+:::image type="content" source="../media/evaluations/view-results/image-per-turn-pop-up.png" alt-text="Screenshot of the image popup from conversation column." lightbox="../media/evaluations/view-results/image-per-turn-pop-up.png":::
+
+Select the image to expand and view it. By default, all images are blurred to protect you from potentially harmful content. To view the image clearly, turn on the "Check Blur Image" toggle.
+
+:::image type="content" source="../media/evaluations/view-results/image-check-blur-image.png" alt-text="Screenshot of blurred image that shows the check blue image toggle." lightbox="../media/evaluations/view-results/image-check-blur-image.png":::
+
 For risk and safety metrics, the evaluation provides a severity score and reasoning for each score. Here are some examples of risk and safety metrics results for the question answering scenario:
 
 :::image type="content" source="../media/evaluations/view-results/risk-safety-metric-example.png" alt-text="Screenshot of risk and safety metrics results for question answering scenario." lightbox="../media/evaluations/view-results/risk-safety-metric-example.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価結果のページにマルチモーダル評価の詳細を追加"
}
```

### Explanation
この変更は、Azure AI Studioの「評価結果」に関する文書を更新し、マルチモーダル評価シナリオに関する新しい情報を追加したものです。具体的な内容は以下の通りです。

1. **日付の更新**: ドキュメントの日付が2024年11月19日から2024年12月18日に変更され、最新の情報を反映しています。

2. **マルチモーダル評価の情報追加**: マルチモーダルシナリオ（テキストと画像の組み合わせ）における安全性評価についての詳細が新たに追加されました。このセクションでは、評価結果をよりよく理解するために、入力と出力の画像を確認する方法が説明されています。

3. **評価結果の表示方法**: ユーザーは「View evaluation results per turn」を選択して、各ターンの入力と出力を検査できることが強調されており、ユーザビリティが向上しています。

4. **画像の表示と操作**: 画像を選択して拡大表示し、デフォルトではすべての画像がぼやけて表示されることが説明されています。これにより、潜在的に有害なコンテンツからユーザーを保護していることが示されています。ぼやけた画像をクリアに表示するための「Check Blur Image」トグルの使用方法が説明されています。

5. **リスクと安全性メトリックの説明**: 評価結果には、リスクと安全性に関する評価スコアとその理由の説明が含まれていることが言及され、具体的なスコアの例が提供されています。

この更新により、ユーザーはマルチモーダルシナリオにおける評価結果をより深く理解し、具体的な評価プロセスが効果的に行えるようになります。

## articles/ai-studio/media/ai-services/endpoint/models-endpoints-ai-services-deployments.png{#item-d7d49f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIサービスのエンドポイントに関連する画像の更新"
}
```

### Explanation
この変更は、AI Studioにおける「AIサービスのエンドポイント」に関連する画像ファイルが変更されたことに関するものです。具体的には、何も追加されたり削除されたりすることはなく、変更内容としては以下の点が挙げられます。

1. **画像の修正**: `models-endpoints-ai-services-deployments.png`という画像が更新されましたが、具体的な変更内容は記載されていません。画像の品質や情報の正確性が向上している可能性があります。

2. **ドキュメントとの関連性**: 更新された画像は、AIサービスのエンドポイントにおけるモデルのデプロイメントを視覚的に支援するためのものであり、利用者がプロセスを理解するのに役立つことが期待されます。

この画像の更新は、全体としてAI Studioのドキュメントが最新の情報を反映していることを示しており、ユーザーに対してより良い情報提供を目指しています。

## articles/ai-studio/media/ai-services/fine-tune-azure-ai-services.png{#item-794ba3}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AIサービスのファインチューニングに関する画像の更新"
}
```

### Explanation
この変更は、AI Studioに関する文書の中で「Azure AIサービスのファインチューニング」に関連する画像ファイルが更新されたことを示しています。具体的には、次のような内容です。

1. **画像の修正**: `fine-tune-azure-ai-services.png`という画像が更新されましたが、具体的な内容については言及されていません。画像の視覚的な品質や情報が改善されたと考えられます。

2. **コンテキストの重要性**: この画像は、Azure AIサービスにおけるファインチューニングの手順や概念を視覚的にサポートするために使用されているため、更新によりユーザーがこのプロセスをより理解しやすくなることが期待されます。

この更新は、ユーザーが最新の情報を得られるようにするためのものであり、全体としてAI Studioのドキュメントが継続的に改善されていることを示しています。

## articles/ai-studio/media/ai-services/models/ai-services-model-catalog.png{#item-94fb65}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIサービスモデルカタログに関する画像の更新"
}
```

### Explanation
この変更は、AI Studioにおいて「AIサービスモデルカタログ」に関連する画像ファイルが更新されることを示しています。具体的には、以下の点が挙げられます。

1. **画像の修正**: `ai-services-model-catalog.png`という画像が更新されましたが、具体的な変更内容は記載されていません。画像の内容やデザインが改善された可能性があります。

2. **文書における役割**: その画像はユーザーがAIサービスのモデルカタログを理解する手助けをするために使用されており、更新されたことにより、提供される情報がより効果的または視覚的に明確になると考えられます。

この更新は、AI Studioのドキュメントが時代に即して進化し続けていることを示しており、ユーザーに対する情報の質を向上させる目的があります。

## articles/ai-studio/media/ai-services/overview/ai-services-capabilities.png{#item-39cf6c}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIサービスの機能に関する画像の更新"
}
```

### Explanation
この変更は、AI Studioにおける「AIサービスの機能」に関連する画像ファイルが更新されたことを示しています。以下のポイントが特徴的です。

1. **画像の修正**: `ai-services-capabilities.png`という画像が修正されましたが、具体的な変更内容は提示されていません。新しいデザインや内容の改良が施された可能性があります。

2. **説明文書に対する影響**: 更新された画像は、AIサービスの能力や特徴を視覚的に表現するために使用されており、これによりユーザーがAIサービスの概要をより簡単に理解できるようになります。

この更新は、AI Studioのドキュメントが常に改善されていることを反映しており、利用者にとっての理解を深めるための重要な一歩です。

## articles/ai-studio/media/ai-services/playgrounds/azure-ai-services-playgrounds.png{#item-4ffa5c}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AIサービスプレイグラウンドに関する画像の更新"
}
```

### Explanation
この変更は、AI Studioにおける「Azure AIサービスプレイグラウンド」という画像ファイルが更新されたことを示しています。以下にその主なポイントを説明します。

1. **画像の修正**: `azure-ai-services-playgrounds.png`という画像が更新されましたが、具体的な変更内容は記載されていません。デザインの改善や情報の追加が考えられます。

2. **ユーザーインターフェースの強化**: 更新された画像は、Azure AIサービスのプレイグラウンドに関連する情報を視覚的に表現しており、ユーザーがこのサービスの使用方法や機能を理解しやすくすることを目的としています。

この更新により、ユーザーは最新の情報を基にAzure AIサービスの利用をよりスムーズに行えるようになると期待されます。

## articles/ai-studio/media/ai-services/playgrounds/language-playground.png{#item-14b15a}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語プレイグラウンドに関する画像の更新"
}
```

### Explanation
この変更は、AI Studio内の「言語プレイグラウンド」に関連する画像ファイルが更新されたことを示しています。主なポイントは以下の通りです。

1. **画像の修正**: `language-playground.png`という画像が更新されました。具体的な変更内容は明示されていませんが、更新に伴いデザインや情報の改良があったと考えられます。

2. **視覚的表現の向上**: 新しい画像は、言語プレイグラウンドの機能や利用方法をより分かりやすく示すことを目的としており、ユーザーがこの機能を利用する際の理解を助けるものとなっています。

この変更により、ユーザーは言語プレイグラウンドの利用をより円滑に行えるようになることが期待されます。

## articles/ai-studio/media/evaluations/view-results/image-check-blur-image.png{#item-9357b0}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "画像のぼやけチェック結果を示す新しい画像の追加"
}
```

### Explanation
この変更は、AI Studioの評価機能に関連する新しい画像ファイルが追加されたことを示しています。具体的なポイントを以下に説明します。

1. **新しい画像の追加**: `image-check-blur-image.png`という新しい画像が追加されました。この画像は、画像がぼやけているかどうかをチェックする結果を示すために使われるものです。

2. **評価機能の強化**: この新しい画像は、ユーザーが評価結果を視覚的に確認できるようにすることで、評価プロセスの理解を深めることを目的としています。特に、画像の品質に対するフィードバックを提供することで、ユーザーが結果をより簡単に解釈できるようになります。

この変更により、AI Studioの利用者は、画像評価の結果をさらにわかりやすく受け取ることができるようになり、全体的なユーザーエクスペリエンスの向上が期待されます。

## articles/ai-studio/media/evaluations/view-results/image-detail-table.png{#item-326e38}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "評価結果の詳細を示す新しい画像の追加"
}
```

### Explanation
この変更は、AI Studioの評価機能に関連する新しい画像ファイルが追加されたことを示しています。以下に、具体的な内容を説明します。

1. **新しい画像の追加**: `image-detail-table.png`という画像が新たに追加されました。この画像は、評価結果の詳細を示すためのもので、ユーザーが結果をよりよく理解するのに役立ちます。

2. **情報の視覚化**: 新しい画像は、評価の結果を詳細に表示するため、ユーザーがデータを視覚的に把握できるように設計されています。これにより、ユーザーは評価プロセスにおけるさまざまな側面をより深く理解できるようになります。

この変更によって、AI Studioのユーザーは、評価結果を簡単に解析し、より効果的に利用することが可能になるため、全体的なユーザー体験の向上が期待されます。

## articles/ai-studio/media/evaluations/view-results/image-per-turn-pop-up.png{#item-21f1d7}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ターンごとのポップアップ表示画像の追加"
}
```

### Explanation
この変更は、AI Studioの評価機能に関連する新しい画像ファイルが追加されたことを示しています。具体的な情報は以下の通りです。

1. **新しい画像の追加**: `image-per-turn-pop-up.png`という新しい画像が追加されました。この画像は、評価結果や情報をターンごとにポップアップで表示する様子を示しています。

2. **ユーザーインターフェースの向上**: 新しい画像は、ユーザーが各ターンにおけるフィードバックや評価を視覚的に確認できるようにするため、情報の提示方法を改善する役割を果たしています。これにより、ユーザーはリアルタイムでの評価結果をより直感的に理解できるようになります。

この変更により、AI Studioのユーザーは、インタラクティブな評価体験を得ることができ、操作性や理解度が向上することが期待されます。

## articles/ai-studio/media/how-to/develop-langchain/langchain-portal-tracing-example.png{#item-89dbdd}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "LangChainポータルトレースの例示画像の追加"
}
```

### Explanation
この変更は、AI StudioにおけるLangChainの開発に関連する新しい画像ファイルが追加されたことを示しています。具体的な内容は以下の通りです。

1. **新しい画像の追加**: `langchain-portal-tracing-example.png`という画像が新たに追加されました。この画像は、LangChainのポータルトレースに関する具体例を視覚的に説明するためのものです。

2. **学習支援の強化**: 追加された画像は、ユーザーがLangChainのトレース機能を理解するのに役立つ情報を提供します。具体的には、ポータルを用いたトレースの手順や結果を示しており、ユーザーがこの技術をより効果的に利用できるようにするための支援を行います。

この変更により、AI StudioのユーザーはLangChainの機能をより深く理解し、開発プロセスを円滑に進めることができるようになることが期待されます。

## articles/ai-studio/media/tutorials/chat/assistant-reply-not-grounded.png{#item-80b5c9}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "アシスタント応答が根拠のない画像の削除"
}
```

### Explanation
この変更は、AI Studioのチュートリアルセクションから特定の画像ファイルが削除されたことを示しています。具体的な内容は以下の通りです。

1. **削除された画像**: `assistant-reply-not-grounded.png`という画像が削除されました。この画像は、アシスタントの応答が根拠のない状況を示すために使用されていたと考えられます。

2. **コンテンツの調整**: 画像の削除は、情報の正確性や適切性を向上させるための見直しの一環と考えられます。特定のビジュアルがテキストやチュートリアルの内容と一致しない場合、その画像の削除は全体の質を高める目的があります。

この変更により、AI Studioのユーザーや開発者は、より正確で信頼性の高い情報に基づいた学習体験を得ることができるようになることが期待されます。

## articles/ai-studio/quickstarts/get-started-playground.md{#item-e4d7fb}

<details>
<summary>Diff</summary>
````diff
@@ -59,8 +59,6 @@ To chat with your deployed model in the chat playground, follow these steps:
 
 1. The assistant either replies that it doesn't know the answer or provides a generic response. For example, the assistant might say, "The price of TrailWalker hiking shoes can vary depending on the brand, model, and where you purchase them." The model doesn't have access to current product information about the TrailWalker hiking shoes. 
 
-    :::image type="content" source="../media/tutorials/chat/assistant-reply-not-grounded.png" alt-text="Screenshot of the assistant's reply without grounding data." lightbox="../media/tutorials/chat/assistant-reply-not-grounded.png":::
-
 Next, you can add your data to the model to help it answer questions about your products. Try the [Deploy an enterprise chat web app](../tutorials/deploy-chat-web-app.md) tutorial to learn more.
 
 ## Related content
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートガイドの文章修正"
}
```

### Explanation
この変更は、AI Studioのクイックスタートガイドにおいて、文章の一部を修正したことを示しています。具体的な内容は以下の通りです。

1. **文の簡略化**: ファイル内で2行のテキストが削除されました。これにより、アシスタントの応答に関する説明がよりコンパクトで明確になりました。具体的には、「アシスタントの応答が根拠のない場合を示すスクリーンショット」の記述が削除されています。

2. **ユーザーの理解の向上**: 不要な情報を削除することで、ユーザーは重要な点に集中しやすくなり、モデルにデータを追加する手順の指示がより明確になります。これにより、製品に関する質問に答えるためのデータ追加の重要性が強調されます。

この変更は、クイックスタートガイドの全体的な流れや理解を改善し、ユーザーがAI Studioでの作業をスムーズに始める手助けをすることを目的としています。

## articles/ai-studio/tutorials/copilot-sdk-build-rag.md{#item-b77dba}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description:  Learn how to build a RAG-based chat app using the Azure AI Foundry
 manager: scottpolly
 ms.service: azure-ai-studio
 ms.topic: tutorial
-ms.date: 11/11/2024
+ms.date: 12/18/2024
 ms.reviewer: lebaro
 ms.author: sgilley
 author: sdgilley
@@ -156,7 +156,11 @@ Now that you have both the script and the template, run the script to test your
 python chat_with_products.py --query "I need a new tent for 4 people, what would you recommend?"
 ```
 
-<!-- To enable logging of telemetry to your project:
+To enable logging of telemetry to your project:
+
+1. Enable tracing by adding an Application Insights resource to your project.  Navigate to the **Tracing** tab in the [Azure AI Foundry portal](https://ai.azure.com/), and create a new resource if you don't already have one.
+
+    :::image type="content" source="../../ai-services/agents/media/ai-foundry-tracing.png" alt-text="A screenshot of the tracing screen in the Azure AI Foundry portal." lightbox="../../ai-services/agents/media/ai-foundry-tracing.png":::
 
 1. Install `azure-monitor-opentelemetry`:
 
@@ -169,7 +173,7 @@ python chat_with_products.py --query "I need a new tent for 4 people, what would
    ```bash
    python chat_with_products.py --query "I need a new tent for 4 people, what would you recommend?" --enable-telemetry 
    ```
--->
+
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGベースのチャットアプリ構築に関するチュートリアルの修正"
}
```

### Explanation
この変更は、Azure AI Foundryを使用したRAG（Retrieval-Augmented Generation）ベースのチャットアプリ構築に関するチュートリアルの内容を修正したことを示しています。具体的な内容は以下の通りです。

1. **日付の更新**: チュートリアルの日付が「2024年11月11日」から「2024年12月18日」に変更されました。これにより、最新の情報や手順が反映されていることが強調されます。

2. **テレメトリのロギングに関する詳細な説明の追加**: コードの一部が変更され、テレメトリをプロジェクトにログする方法についての手順が具体的に追加されました。特に、Application Insightsリソースを追加するための手順が明確に示されています。

3. **画像の追加**: Azure AI Foundryポータルでのトレーシング画面を示すスクリーンショットが追加され、ユーザーが手順を追いやすくなるようにビジュアルサポートが提供されています。

この修正により、ユーザーはテレメトリの設定手順をより理解しやすくなり、チュートリアルの内容がより具体的かつ実用的になっています。また、日付の更新によりチュートリアルの信頼性も向上しています。

## articles/ai-studio/tutorials/copilot-sdk-create-resources.md{#item-552960}

<details>
<summary>Diff</summary>
````diff
@@ -1,22 +1,21 @@
 ---
 title: "Part 1: Set up project and development environment to build a custom knowledge retrieval (RAG) app"
 titleSuffix: Azure AI Foundry
-description:  Build a custom chat app using the Azure AI Foundry SDK. Part 1 of a 3-part tutorial series, which shows how to create the resources you'll need for parts 2 and 3.
+description:  Build a custom chat app using the Azure AI Foundry SDK. Part 1 of a 3-part tutorial series, which shows how to create the resources you need for parts 2 and 3.
 manager: scottpolly
 ms.service: azure-ai-studio
 ms.custom:
   - ignite-2024
 ms.topic: tutorial
-ms.date: 11/11/2024
+ms.date: 12/18/2024
 ms.reviewer: lebaro
 ms.author: sgilley
 author: sdgilley
-#customer intent: As a developer, I want to learn how to use the prompt flow SDK so that I can build a RAG-based chat app.
+#customer intent: As a developer, I want to create a project and set up my development environment to build a custom knowledge retrieval (RAG) app with the Azure AI Foundry SDK.
 ---
 
 # Tutorial:  Part 1 - Set up project and development environment to build a custom knowledge retrieval (RAG) app with the Azure AI Foundry SDK
 
-
 In this tutorial, you use the Azure AI Foundry SDK (and other libraries) to build, configure, and evaluate a chat app for your retail company called Contoso Trek. Your retail company specializes in outdoor camping gear and clothing. The chat app should answer questions about your products and services. For example, the chat app can answer questions such as "which tent is the most waterproof?" or "what is the best sleeping bag for cold weather?".
 
 This tutorial is part one of a three-part tutorial.  This part one gets you ready to write code in part two and evaluate your chat app in part three. In this part, you:
@@ -106,13 +105,11 @@ In the Azure AI Foundry portal, check for an Azure AI Search connected resource.
 1. Find your Azure AI Search service in the options and select **Add connection**.
 1. Use **API key** for **Authentication**.
 
-    > [!NOTE]
-    > You can instead use **Microsoft Entra ID** for **Authentication**. If you do this, you must also configure access control for the Azure AI Search service. Assign the **Search Index Data Contributor** and **Search Service Contributor** roles to your user account. If you don't know how to do this, or don't have the necessary permissions, use the **API key** for **Authentication**.
+    > [!IMPORTANT]
+    > The **API key** option isn't recommended for production. To select and use the recommended **Microsoft Entra ID** authentication option, you must also configure access control for the Azure AI Search service. Assign the *Search Index Data Contributor* and *Search Service Contributor* roles to your user account. For more information, see [Connect to Azure AI Search using roles](../../search/search-security-rbac.md) and [Role-based access control in Azure AI Foundry portal](../concepts/rbac-ai-studio.md).
 
 1. Select **Add connection**.  
 
-
-
 ## <a name="installs"></a> Install the Azure CLI and sign in 
 
 [!INCLUDE [Install the Azure CLI](../includes/install-cli.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム知識取得アプリ構築のためのリソース作成チュートリアルの更新"
}
```

### Explanation
この変更は、Azure AI Foundry SDKを使用したカスタム知識取得（RAG）アプリのリソース作成に関するチュートリアルの内容を更新したことを示しています。具体的な内容は以下の通りです。

1. **説明文の修正**: チュートリアルの説明が、「必要なリソース」を示す表現から「必要なリソースに」変更され、より正確な表現になっています。この小変更は、読者に対してチュートリアルの内容をよりクリアに伝える意図があります。

2. **日付の更新**: チュートリアルの日付が「2024年11月11日」から「2024年12月18日」に変更されており、これは最新の情報を提供するためのものです。

3. **顧客の意図の明確化**: 顧客の意図に関する表現が変更され、開発者が自分のプロジェクトを作成し、開発環境を設定する手順により焦点を当てるように改善されています。このことにより、ユーザーに対する明確な目標設定がなされています。

4. **重要な注意事項の更新**: APIキー認証の使用に関する警告が「重要」な情報として強調され、プロダクション環境において推奨されない理由が明確にされました。また、Microsoft Entra IDを使用する際の設定手順が追記され、ユーザーが安全に認証を行うための情報が提供されています。

この修正により、ユーザーがチュートリアルに従う際に、設定すべき内容や重要な注意点についての理解が向上し、全体的なプロジェクトの実施が容易になっています。


