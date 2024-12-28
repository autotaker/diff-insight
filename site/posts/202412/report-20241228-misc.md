---
date: '2024-12-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f98b838...MicrosoftDocs:dfca068
summary: この差分では、2つの文書がマイナーアップデートされており、新機能や破壊的変更はありません。領収書モデルのドキュメントが最新版に更新され、v4.0.0に関する情報が追加されました。また、Azure
  OpenAI Serviceの用語が「AOAI」から「Azure OpenAI Service」に変更され、接続に関する説明が明確化されています。これにより、利用者はサービスの理解を深め、最新の機能をより簡単に活用できるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f98b838...MicrosoftDocs:dfca068){target="_blank"}

# Highlights
この差分では、2つの主要な文書がマイナーアップデートされていますが、新機能の導入や破壊的変更はありません。それぞれの文書について、内容の明確化と用語の最新化が行われています。

## New features
特に新機能の追加はありません。

## Breaking changes
破壊的変更はありません。

## Other updates
- 領収書モデルのドキュメントが最新版に更新され、v4.0.0バージョンに関する情報が追加されました。
- Azure OpenAI Serviceに関する文書の用語が更新され、「AOAI」から「Azure OpenAI Service」へと変更され、接続に関する説明がより明快にされています。

# Insights
このコード差分には、技術的なドキュメントのアップデートが含まれています。それぞれの変更は以下のような意図があります。

まず、領収書モデルに関するドキュメント更新について。新しいマーカー（v4.0.0のモニカーレンジ）が追加されており、これにより、ユーザーは最新のモデルバージョンが導入され、その内容についても理解しやすくなっています。モデルのサポートされるタイプの詳細が最新バージョンの情報に整合されており、利用者は現行の特徴や機能を簡便に把握できます。

また、Azure OpenAI Serviceに関する文書の修正では、用語「AOAI」が「Azure OpenAI Service」に統一されました。これは、オープンAIサービスに関わる利用者が混乱することなく、正確に情報を取得しやすくするための措置です。さらに、GPTモデルのデプロイメントに関するコメントが修正され、具体的にユーザーが何を必要としているのかを正確に示すことで、より的確なサポート情報を提供するという意図が見られます。

全体として、これらの文書の更新は、利用者がサービスをより理解しやすく、新しい機能を活用するための重要性が増しています。具体的な機能への参照や用語の統一は、技術的な課題を解決する上で不可欠な役割を果たします。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [receipt.md](#item-089054) | minor update | 領収書モデルのドキュメントが更新されました | modified | 2 | 1 | 3 | 
| [online-evaluation.md](#item-d9591b) | minor update | Azure OpenAI Serviceの接続名に関する情報が更新されました | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/document-intelligence/prebuilt/receipt.md{#item-089054}

<details>
<summary>Diff</summary>
````diff
@@ -14,6 +14,7 @@ ms.author: lajanuar
 
 # Document Intelligence receipt model
 
+::: moniker range="doc-intel-4.0.0"
 [!INCLUDE [applies to v4.0](../includes/applies-to-v40.md)]
 ::: moniker-end
 
@@ -31,7 +32,7 @@ ms.author: lajanuar
 
 The Document Intelligence receipt model combines powerful Optical Character Recognition (OCR) capabilities with deep learning models to analyze and extract key information from sales receipts. Receipts can be of various formats and quality including printed and handwritten receipts. The API extracts key information such as merchant name, merchant phone number, transaction date, tax, and transaction total and returns structured JSON data. Receipt model v4.0 (GA) also supports other fields including `ReceiptType`, `TaxDetails.NetAmount`, `TaxDetails.Description`, `TaxDetails.Rate` and `CountryRegion`.
 
-**Supported receipt types:**
+**Supported receipt types in the latest version (4.0):**
 
 * Meal
 * Supplies
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "領収書モデルのドキュメントが更新されました"
}
```

### Explanation
この変更は、ドキュメントの情報を最新のバージョンに合わせて更新するためのものです。具体的には、領収書モデルに関する文書に以下の変更が加えられました。まず、v4.0.0のモニカーレンジを示す新しいマーカーが追加され、ユーザーに最新の機能を利用可能であることを示しています。次に、領収書モデルのサポートされるタイプの説明が更新され、最新バージョン（4.0）に関連する情報が明確に記されています。この変更により、ユーザーは新しいバージョンの強化された特徴や機能をより理解しやすくなります。

## articles/ai-studio/how-to/online-evaluation.md{#item-d9591b}

<details>
<summary>Diff</summary>
````diff
@@ -224,11 +224,11 @@ app_insights_config = ApplicationInsightsConfiguration(
     service_name=SERVICE_NAME
 )
 
-# Connect to your AOAI resource, you must use an AOAI GPT model
+# Connect to your Azure OpenAI Service resource. You must use a GPT model deployment for this example.
 deployment_name = "gpt-4"
 api_version = "2024-08-01-preview"
 
-# This is your AOAI connection name, which can be found in your Azure AI Foundry project under the 'Models + Endpoints' tab
+# This is your Azure OpenAI Service connection name, which can be found in your Azure AI Foundry project under the 'Models + Endpoints' tab.
 default_connection = project_client.connections._get_connection(
     "aoai_connection_name"
 )
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI Serviceの接続名に関する情報が更新されました"
}
```

### Explanation
この変更では、Azure OpenAI Serviceに関連する文書の内容が最近の名詞と用語に合わせて修正されました。具体的には、接続に関する説明が明確化され、元の用語「AOAI」から「Azure OpenAI Service」へと更新されています。これにより、ユーザーがより正確にサービスを理解し、リソースに接続する際に必要な情報を得やすくなります。また、コメント文の内容も少し変更され、具体的に「GPTモデルのデプロイメントを使用する必要がある」という点が強調されています。この更新は、使用するサービスとその設定に対する理解を深めるためのものです。


