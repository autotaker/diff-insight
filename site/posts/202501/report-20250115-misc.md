---
date: '2025-01-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:de17d62...MicrosoftDocs:36d0ff5
summary: このコード変更は、複数のドキュメントにおけるリンク修正および新機能の追加が主な内容です。主な変更点には、Document Intelligenceのサポートリクエストリンクの更新や、各SDKのサンプルリンクの修正、Gretel
  Navigatorモデルの導入に関する新しいガイドの追加があります。特に破壊的な変更は報告されていないものの、ドキュメントリンクの更新に伴い、参照先が変更された可能性があるため注意が必要です。全体として、ユーザーが正確で最新の情報にアクセスできるよう、ドキュメントの正確性とユーザーエクスペリエンスを向上させることを目指しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:de17d62...MicrosoftDocs:36d0ff5){target="_blank"}

<format>
# Highlights
このコード変更は、複数のドキュメントにおけるリンク修正および新機能の追加が主な内容です。主な変更点には、Document Intelligenceのサポートリクエストリンクの更新や、各SDKのサンプルリンクの修正、Gretel Navigatorモデルの導入に関する新しいガイドの追加があります。

## New features
- Gretel NavigatorチャットモデルをAzure AI Foundryで使用する方法を解説する新しいドキュメントの追加。

## Breaking changes
- 特に破壊的な変更は報告されていないが、ドキュメントリンクの更新に伴い、参照先が変更された可能性があるため注意が必要。

## Other updates
- FAQやHow-Toガイド、サービス制限、モデルカタログなど各種ドキュメントでリンクおよび情報の更新。
- Mistral AIやHealthcare AIモデルに関する情報が追加され、ドキュメントが最新化された。
- 提供地域に関する情報の修正と整理。
- ドキュメント構造の改善により可読性が向上。

# Insights
今回の変更は、主にドキュメントのリンクや情報の更新を通じて、ユーザーが正確かつ最新の情報にアクセスできるようにするもので、非常に技術的な側面に重点を置いています。

まずDocument Intelligenceに関連する変更を見てみると、FAQやクライアントライブラリ、サービス制限に関するドキュメントでリンク変更や情報の追加が行われました。ここでは特に、トランザクション毎秒(TPS)のためのサポートリクエストへ直接アクセスできるようにリンクが修正され、ユーザーの利便性が向上しています。また、JavaScriptおよびC# SDKに関するドキュメントのサンプルリンクが最新のものに更新され、使用時の誤解を避けるための対策が取られています。

さらに、AI Studioにおける新しいドキュメントの追加は非常に重要な動きです。特にGretel Navigatorチャットモデルのデプロイについての詳細なガイドが新たに提供され、これにより、ユーザーは合成データ生成に対応した先進的なAIモデルを効果的に展開できるようになります。この追加により、Azure AI Foundryがユーザーに提供できるサービスの範囲が拡大しました。

また、モデルカタログと提供地域情報の更新により、ユーザーが利用可能なAIモデルの選択肢とその利用地域をより正確に把握できるようになりました。情報の整理により、モデルライフサイクルや退役に関する情報も透明性が増しており、各種プロジェクトへの影響を事前に認識するための基盤が強化されています。

総じて、この一連の変更は、ドキュメントの正確性とユーザーエクスペリエンスの向上を目指したものであり、開発者やエンジニアが最新情報を基により効率的に作業を進めるための助けとなります。これにより、提供された技術文書がより信頼性の高い情報源としての役割を果たすことが期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [faq.yml](#item-7a051f) | minor update | FAQのサポートリクエストリンクの更新 | modified | 1 | 1 | 2 | 
| [javascript-sdk.md](#item-b28fc0) | minor update | JavaScript SDKのサンプルリンクの修正 | modified | 1 | 1 | 2 | 
| [csharp-sdk.md](#item-ee69c7) | minor update | C# SDKのクライアントライブラリリンクの修正 | modified | 1 | 1 | 2 | 
| [javascript-sdk.md](#item-615fcd) | minor update | JavaScript SDKのサンプルリンクの修正 | modified | 1 | 1 | 2 | 
| [service-limits.md](#item-5ceae5) | minor update | サービス制限に関するドキュメントの改訂 | modified | 29 | 32 | 61 | 
| [custom-neural.md](#item-ac0e69) | minor update | カスタムニューラルモデルに関するドキュメントの更新 | modified | 11 | 11 | 22 | 
| [changelog-release-history.md](#item-dccdd3) | minor update | リリース履歴ドキュメントのリンク修正 | modified | 3 | 3 | 6 | 
| [sdk-overview-v4-0.md](#item-d59a82) | minor update | SDK概要ドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [model-lifecycle-retirement.md](#item-f0fc21) | minor update | モデルライフサイクル廃止に関するドキュメントの更新 | modified | 3 | 2 | 5 | 
| [deploy-models-gretel-navigator.md](#item-2e9806) | new feature | Gretel NavigatorチャットモデルをAzure AI Foundryで使用する方法を追加 | added | 544 | 0 | 544 | 
| [model-catalog-overview.md](#item-278001) | minor update | モデルカタログの更新 | modified | 6 | 4 | 10 | 
| [region-availability-maas.md](#item-35d79c) | minor update | モデルの提供地域の更新 | modified | 36 | 14 | 50 | 
| [toc.yml](#item-2745cd) | minor update | Gretel Navigatorモデルの追加 | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/faq.yml{#item-7a051f}

<details>
<summary>Diff</summary>
````diff
@@ -242,7 +242,7 @@ sections:
 
           - Increase the workload gradually. Avoid sharp changes.
 
-          - [Create a support request](service-limits.md#create-and-submit-support-request) to increase transactions per second (TPS) limit.
+          - [Create a support request](service-limits.md#create-and-submit-support-request-for-tps-increase) to increase transactions per second (TPS) limit.
 
           Learn more about Document Intelligence [service quotas and limits](service-limits.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQのサポートリクエストリンクの更新"
}
```

### Explanation
このコードの変更は、`faq.yml`ファイル内のサポートリクエストリンクの更新に関するものです。具体的には、トランザクション毎秒（TPS）の制限を増加させるためのサポートリクエストを作成する際のリンクが修正されました。元のリンクは、`service-limits.md#create-and-submit-support-request`であったのに対し、新しいリンクは`service-limits.md#create-and-submit-support-request-for-tps-increase`に変更されています。この変更はリンクの明確さを高め、TPS増加のリクエストに関する情報へ直接的にアクセスできるようにしています。

## articles/ai-services/document-intelligence/how-to-guides/includes/v4-0/javascript-sdk.md{#item-b28fc0}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.custom: devx-track-csharp, linux-related-content
 <!-- markdownlint-disable MD033 -->
 <!-- markdownlint-disable MD034 -->
 
-[Client library](/javascript/api/overview/azure/ai-document-intelligence-rest-readme?view=azure-node-preview&preserve-view=true) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package (npm)](https://www.npmjs.com/package/@azure-rest/ai-document-intelligence/v/1.0.0-beta.3) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest/samples/v1-beta) |[Supported REST API version](../../../sdk-overview-v4-0.md)
+[Client library](/javascript/api/overview/azure/ai-document-intelligence-rest-readme?view=azure-node-preview&preserve-view=true) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package (npm)](https://www.npmjs.com/package/@azure-rest/ai-document-intelligence/v/1.0.0-beta.3) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest/samples/v1/javascript) |[Supported REST API version](../../../sdk-overview-v4-0.md)
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKのサンプルリンクの修正"
}
```

### Explanation
このコードの変更は、`javascript-sdk.md`ファイル内のJavaScript SDKに関連するサンプルリンクの更新を示しています。具体的には、サンプルリンクのパスが修正されており、以前のリンクはバージョン1-betaのサンプルを参照していましたが、新しいリンクはバージョン1のサンプルに対応するものになっています。これは、ユーザーが最新のサンプルコードにアクセスできるようにするための情報を改善する変更です。このようにして、利用者にとってより便利な形で情報が提供されることを目的としています。

## articles/ai-services/document-intelligence/quickstarts/includes/csharp-sdk.md{#item-ee69c7}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ monikerRange: ">=doc-intel-3.0.0"
 <!-- markdownlint-disable MD029 -->
 
 :::moniker range="doc-intel-4.0.0"
-[Client library](/dotnet/api/overview/azure/cognitiveservices/documentintelligence?view=azure-dotnet&preserve-view=true) | [SDK reference](https://azuresdkdocs.blob.core.windows.net/$web/dotnet/Azure.AI.DocumentIntelligence/1.0.0/index.html) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package](https://www.nuget.org/packages/Azure.AI.DocumentIntelligence/1.0.0)| [Samples](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/README.md)|[Supported REST API version](../../sdk-overview-v4-0.md)
+[Client library](/dotnet/api/azure.ai.documentintelligence?view=azure-dotnet&preserve-view=true) | [SDK reference](https://azuresdkdocs.blob.core.windows.net/$web/dotnet/Azure.AI.DocumentIntelligence/1.0.0/index.html) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package](https://www.nuget.org/packages/Azure.AI.DocumentIntelligence/1.0.0)| [Samples](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/README.md)|[Supported REST API version](../../sdk-overview-v4-0.md)
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDKのクライアントライブラリリンクの修正"
}
```

### Explanation
このコードの変更は、`csharp-sdk.md`ファイルにおけるC# SDKのクライアントライブラリに関するリンクの更新を示しています。具体的には、クライアントライブラリのリンクが修正されており、以前のリンクは`/dotnet/api/overview/azure/cognitiveservices/documentintelligence?view=azure-dotnet&preserve-view=true`であったのに対し、新しいリンクは`/dotnet/api/azure.ai.documentintelligence?view=azure-dotnet&preserve-view=true`に変更されています。また、チュートリアルやサンプルのリンクに変更はないものの、クライアントライブラリに関連するリンクをより具体的な形にすることで、ユーザーが直接関連情報にアクセスしやすくなっています。この更新は、SDKのユーザビリティを向上させることを目的としています。

## articles/ai-services/document-intelligence/quickstarts/includes/javascript-sdk.md{#item-615fcd}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.author: lajanuar
 <!-- markdownlint-disable MD025 -->
 
 :::moniker range="doc-intel-4.0.0"
-[Client library](/javascript/api/overview/azure/ai-document-intelligence-rest-readme?view=azure-node-latest&preserve-view=true) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package (npm)]( https://www.npmjs.com/package/@azure-rest/ai-document-intelligence/v/1.0.0) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest/samples/v1-beta) |[Supported REST API version](../../sdk-overview-v4-0.md)
+[Client library](/javascript/api/overview/azure/ai-document-intelligence-rest-readme?view=azure-node-latest&preserve-view=true) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package (npm)]( https://www.npmjs.com/package/@azure-rest/ai-document-intelligence/v/1.0.0) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest/samples/v1/javascript) |[Supported REST API version](../../sdk-overview-v4-0.md)
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKのサンプルリンクの修正"
}
```

### Explanation
このコードの変更は、`javascript-sdk.md`ファイルにおけるJavaScript SDKに関連するサンプルリンクの更新を示しています。具体的には、サンプルリンクのパスが変更されており、以前のリンクはバージョン1-betaのサンプルを指していましたが、新しいリンクはバージョン1のサンプルに更新されています。また、クライアントライブラリおよび他のリファレンスリンクには変更がありません。これにより、ユーザーは最新のサンプルコードにアクセスしやすくなり、実装の際の参照として役立つようになっています。この小さな更新は、SDK使用者の利便性向上を目指しています。

## articles/ai-services/document-intelligence/service-limits.md{#item-5ceae5}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 11/19/2024
+ms.date: 01/13/2025
 ms.author: lajanuar
 monikerRange: '<=doc-intel-4.0.0'
 ---
@@ -64,7 +64,7 @@ Document Intelligence billing is calculated monthly based on the model type and
 
 - Container pricing is the same as cloud service pricing.
 
-- Document Intelligence offers a free tier (F0) where you can test all the Document Intelligence features.
+- Document Intelligence offers a free tier (F0) where you can test all the Document Intelligence features. The free tier limits analyze response to only the first two pages in a request.
 
 - Document Intelligence has a commitment-based pricing model for large workloads.
 
@@ -93,7 +93,13 @@ Document Intelligence billing is calculated monthly based on the model type and
 
 |Quota|Free (F0)<sup>1</sup>|Standard (S0)|
 |--|--|--|
-| **Transactions Per Second limit** | 1 | 15 (default value) |
+| **Analyze transactions Per Second limit** | 1 | 15 (default value) |
+| Adjustable | No | Yes <sup>2</sup> |
+| **Get operations Per Second limit** | 1 | 50 (default value) |
+| Adjustable | No | Yes <sup>2</sup> |
+| **Model management operations Per Second limit** | 1 | 5 (default value) |
+| Adjustable | No | Yes <sup>2</sup> |
+| **List operations Per Second limit** | 1 | 10 (default value) |
 | Adjustable | No | Yes <sup>2</sup> |
 | **Max document size** | 4 MB | 500 MB |
 | Adjustable | No | No |
@@ -131,7 +137,7 @@ Document Intelligence billing is calculated monthly based on the model type and
 | Adjustable | No | No |
 | **Max number of pages (Training) * Neural and Generative** | 50,000 | 50,000 (default value) |
 | Adjustable | No | No |
-| **Custom neural model train** | 10 hours per month <sup>5</sup> | no limit (pay by the hour) |
+| **Custom neural model train** | 10 hours per month <sup>5</sup> | no limit (pay by the hour), start with 10 free hours each month |
 | Adjustable | No |Yes <sup>3</sup>|
 | **Max number of pages (Training) * Classifier** | 10,000 | 10,000 (default value) |
 | Adjustable | No | No |
@@ -238,9 +244,9 @@ Document Intelligence billing is calculated monthly based on the model type and
 
 ::: moniker range=">=doc-intel-2.1.0"
 
-> <sup>1</sup> For **Free (F0)** pricing tier see also monthly allowances at the [pricing page](https://azure.microsoft.com/pricing/details/form-recognizer/).</br>
-> <sup>2</sup> See [best practices](#example-of-a-workload-pattern-best-practice), and [adjustment instructions](#create-and-submit-support-request).</br>
-> <sup>3</sup> Neural models training count is reset every calendar month. Open a support request to increase the monthly training limit.
+> <sup>1</sup> For **Free (F0)** pricing tier see also monthly allowances at the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/).</br>
+> <sup>2</sup> See [best practices](#example-of-a-workload-pattern-best-practice), and [adjustment instructions](#create-and-submit-support-request-for-tps-increase).</br>
+> <sup>3</sup> Neural models training count is reset every calendar month. Open a support request to increase the monthly training limit. Starting with the v4.0 API, training requests over 20 requests in a calendar month are billed on the training tier. See [pricing](https://azure.microsoft.com/pricing/details/ai-document-intelligence/) for details.
 ::: moniker-end
 ::: moniker range=">=doc-intel-3.0.0"
 > <sup>4</sup> This limit applies to all documents found in your training dataset folder prior to any labeling-related updates.
@@ -251,49 +257,40 @@ Document Intelligence billing is calculated monthly based on the model type and
 
 ## Detailed description, Quota adjustment, and best practices
 
-Before requesting a quota increase (where applicable), ensure that it's necessary. Document Intelligence service uses autoscaling to bring the required computational resources `on-demand`, keep the customer costs low, and deprovision unused resources by not maintaining an excessive amount of hardware capacity.
+The default limits can be extended by requesting an increase via a support ticket. Before requesting a quota increase (where applicable), ensure that it's necessary. Document Intelligence service uses autoscaling to bring the required computational resources `on-demand`, keep the customer costs low, and deprovision unused resources by not maintaining an excessive amount of hardware capacity. 
 
-If your application returns Response Code 429 (*Too many requests*) and your workload is within the defined limits: most likely, the service is scaling up to your demand, but has yet to reach the required scale. Thus the service doesn't immediately have enough resources to serve the request. This state is transient and shouldn't last long.
+If your application returns Response Code 429 (*Too many requests*) you are over the threshold for one or more of the transactions per second limits (TPS):
+* **Analyze transactions Per Second limit**  The TPS for submitting analyze requests (POST)
+* **Get operations Per Second limit** The TPS for polling for results on analyze operations (GET)
+* **Model management operations Per Second limit** Operations related to  model management like build/train and copy.
+* **List operations Per Second limit** Operations related to listing models, operations.
 
 ### General best practices to mitigate throttling during autoscaling
 
 To minimize issues related to throttling (Response Code 429), we recommend using the following techniques:
 
 * Implement retry logic in your application
 * Avoid sharp changes in the workload. Increase the workload gradually <br/>
-*Example.* Your application is using Document Intelligence and your current workload is 10 TPS (transactions per second). The next second you increase the load to 40 TPS (that is four times more). The Service immediately starts scaling up to fulfill the new load, but likely it can't do it within a second, so some of the requests get Response Code 429.
+*Example.* Your application is using Document Intelligence and your current workload is 10 TPS (transactions per second). The next second you increase the load to 40 TPS. The result is a 429 response code for some requests as you are over the 15 TPS limit for submitting analyze operations. You could either back off the processing to stay under the 15 TPS or request an increase on the TPS to support your higher volumes.
 
 The next sections describe specific cases of adjusting quotas.
-Jump to [Document Intelligence: increasing concurrent request limit](#create-and-submit-support-request)
+ Jump to [Document Intelligence: increasing concurrent request limit](#create-and-submit-support-request-for-tps-increase)
 
 ### Increasing transactions per second request limit
 
 By default the number of transactions per second is limited to 15 transactions per second for a Document Intelligence resource. For the Standard pricing tier, this amount can be increased. Before submitting the request, ensure you're familiar with the material in [this section](#detailed-description-quota-adjustment-and-best-practices) and aware of these [best practices](#example-of-a-workload-pattern-best-practice).
 
-Increasing the Concurrent Request limit does **not** directly affect your costs. Document Intelligence service uses "Pay only for what you use" model. The limit defines how high the Service can scale before it starts throttle your requests.
+The fist step would be to enable auto scaling. Follow this document to enable auto scaling on your resource * [enable auto scaling](../../ai-services/autoscale.md). With auto scaling enabled your resource can continue to accept requests over the TPS limits configured if there's capacity on the service. It can still result in request throttled. 
 
-Existing value of Concurrent Request limit parameter is **not** visible via Azure portal, Command-Line tools, or API requests. To verify the existing value, create an Azure Support Request.
-
-If you would like to increase your transactions per second, you can enable auto scaling on your resource. Follow this document to enable auto scaling on your resource * [enable auto scaling](../../ai-services/autoscale.md). You can also submit an increase TPS support request.
-
-#### Have the required information ready
+Increasing the Concurrent Request limit does **not** directly affect your costs. Document Intelligence service uses "Pay only for what you use" model. The limit defines how high the Service can scale before it starts throttle your requests.
 
-- Document Intelligence Resource ID
-- Region
+The existing value of different request limit categories is available via Azure portal, under the monitoring tab on the resource overview blade.
 
-- Base model information:
-  - Sign in to the [Azure portal](https://portal.azure.com)
-  - Select the Document Intelligence Resource for which you would like to increase the transaction limit
-  - Select -Properties- (-Resource Management- group)
-  - Copy and save the values of the following fields:
-    - Resource ID
-    - Location (your endpoint Region)
 
-#### Create and submit support request
+#### Create and submit support request for TPS increase
 
 Initiate the increase of transactions per second(TPS) limit for your resource by submitting the Support Request:
 
-- Ensure you have the [required information](#have-the-required-information-ready)
 - Sign in to the [Azure portal](https://portal.azure.com)
 - Select the Document Intelligence Resource for which you would like to increase the TPS limit
 - Select -New support request- (-Support + troubleshooting- group). A new window appears with autopopulated information about your Azure Subscription and Azure Resource
@@ -303,16 +300,16 @@ Initiate the increase of transactions per second(TPS) limit for your resource by
 - Proceed further with the request creation
 - Enter the following information in the -Description- field, under the Details tab:
   - a note, that the request is about Document Intelligence quota.
-  - Provide a TPS expectation you would like to scale to  meet.
-  - Azure resource information you [collected](#have-the-required-information-ready).
+  - Provide a TPS expectation you would like to scale to  meet. While TPS increases are free, you should only request a TPS that is reasonable for your workload.
+  - Azure resource information
   - Complete entering the required information and select -Create- button in -Review + create- tab
   - Note the support request number in Azure portal notifications. Look for Support to contact you shortly for further processing.
 
 ## Example of a workload pattern best practice
 
 This example presents the approach we recommend following to mitigate possible request throttling due to [Autoscaling being in progress](#detailed-description-quota-adjustment-and-best-practices). It isn't an *exact recipe*, but merely a template we invite to follow and adjust as necessary.
 
- Let us suppose that a Document Intelligence resource has the default limit set. Start the workload to submit your analyze requests. If you find that you're seeing frequent throttling with response code 429, start by implementing an exponential backoff on the GET analyze response request. By using a progressively longer wait time between retries for consecutive error responses, for example a  2-5-13-34 pattern of delays between requests. In general, we recommended not calling the get analyze response more than once every 2 seconds for a corresponding POST request.
+ Let us suppose that a Document Intelligence resource has the default limit set. Start the workload to submit your analyze requests. If you find that you're seeing frequent throttling with response code 429 when checking for completion, start by implementing an exponential backoff on the GET analyze response request. By using a progressively longer wait time between retries for consecutive error responses, for example a  2-5-13-34 pattern of delays between requests. In general, we recommended not calling the get analyze response more than once every 2 seconds for a corresponding POST request. The `analyze` response also contains a **retry-after** header that indicates how long you should wait in seconds before checking for completion of that request. 
 
 If you find that you're being throttled on the number of POST requests for documents being submitted, consider adding a delay between the requests. If your workload requires a higher degree of concurrent processing, you then need to create a support request to increase your service limits on transactions per second.
 
@@ -321,4 +318,4 @@ Generally, we recommended testing the workload and the workload patterns before
 ## Next steps
 
 > [!div class="nextstepaction"]
-> [Learn about error codes and troubleshooting](v3-error-guide.md)
+> [Learn about error codes and troubleshooting](v3-error-guide.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス制限に関するドキュメントの改訂"
}
```

### Explanation
このコードの変更は、`service-limits.md`ファイルにおけるDocument Intelligenceに関連するサービス制限に関する情報の更新を示しています。主な改善点は、以下の通りです：

1. ドキュメントの日付が2024年11月19日から2025年1月13日に更新されました。
2. 無料利用枠(F0)に関する説明が強化され、リクエストあたりの分析応答が最初の2ページに制限されることが明記されました。
3. 各パフォーマンス指標（例えば、「Analyze transactions Per Second limit」や「Get operations Per Second limit」など）の種類や詳細が明確にし、調整可能なオプションについての情報が追加されました。
4. サポートリクエストを介してTPS（transactions per second）の増加を要求する手順が明確化され、リクエストの際に必要な情報が整理されています。

これらの変更により、ユーザーはDocument Intelligenceの利用制限をよりよく理解できるようになり、効率的にサービスを活用するためのサポートを得やすくなっています。

## articles/ai-services/document-intelligence/train/custom-neural.md{#item-ac0e69}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ monikerRange: '>=doc-intel-3.0.0'
 # Document Intelligence custom neural model
 
 
-
+:::moniker range="doc-intel-4.0.0"
 **This content applies to:**![checkmark](../media/yes-icon.png) **v4.0 (GA)** | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=tru)
 ::: moniker-end
 
@@ -45,7 +45,7 @@ Custom neural models share the same labeling format and strategy as [custom temp
 ## Model capabilities
 
  > [!IMPORTANT]
- > Custom neural v4.0 2024-11-30 (GA) model supports overlapping fields and table cell confidence.
+ > Custom neural v4.0 `2024-11-30` (GA) model supports overlapping fields and table cell confidence.
 
 Custom neural models currently support key-value pairs and selection marks and structured fields (tables).
 
@@ -64,7 +64,7 @@ Neural models support documents that have the same information, but different pa
 
 ### Overlapping fields
 
-Custom neural v4.0 2024-11-30 (GA) model supports overlapping fields:
+Custom neural v4.0 `2024-11-30` (GA) model supports overlapping fields:
 
 To use the overlapping fields, your dataset needs to contain at least one sample with the expected overlap. To label an overlap, use **region labeling** to designate each of the spans of content (with the overlap) for each field. Labeling an overlap with field selection (highlighting a value) fails in the Studio as region labeling is the only supported labeling tool for indicating field overlaps. Overlap support includes:
 
@@ -294,9 +294,9 @@ POST https://{endpoint}/documentintelligence/documentModels:build?api-version=20
 
 > [!IMPORTANT]
 >
-> * If you would like to train additional neural models or train models for a longer time period that **exceed 10 hours**, billing charges apply. For details on the billing charges, refer to the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/).
-> * You can opt in for this paid training service by setting the `maxTrainingHours` to the desired maximum number of hours. API calls with no budget but with the `maxTrainingHours` set as over 10 hours will fail.
-> * As each build takes different amount of time depending on the type and size of the training dataset, billing is calculated for the actual time spent training the neural model, with a minimum of 30 minutes per training job.
+> * If you would like to train more neural models or train models for a longer time period that **exceed 10 hours**, billing charges apply. For details on the billing charges, refer to the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/).
+> * You can opt in for this paid training service by setting the `maxTrainingHours` to the desired maximum number of hours. API calls with no budget but with the `maxTrainingHours` set to over 10 hours fail.
+> * Each build takes a different amount of time depending on the type and size of the training dataset. Billing is calculated for the actual time spent training the neural model with a minimum of 30 minutes per training job.
 > * This paid training feature enables you to train larger data sets for longer durations with flexibility in the training hours.
 
 ```bash
@@ -311,19 +311,19 @@ GET /documentModels/{myCustomModel}
 ```
 
 > [!NOTE]
-> For Document Intelligence versions `v3.1 (2023-07-31)` and `v3.0 (2022-08-31)`, custom neural model's paid training is not enabled. For the two older versions, you will get a maximum of 30 minutes training duration per model. If you would like to train more than 20 model instances, you can create an [Azure support ticket](../service-limits.md#create-and-submit-support-request) to increase in the training limit.
+> For Document Intelligence versions `v3.1 (2023-07-31)` and `v3.0 (2022-08-31)`, custom neural model's paid training isn't enabled. For the two older versions, there's a maximum of 30-minutes training duration per model. If you would like to train more than 20 model instances, you can create an [Azure support ticket](../service-limits.md#create-and-submit-support-request-for-tps-increase) to increase in the training limit.
 
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
 
 ## Billing
 
-For Document Intelligence versions `v3.1 (2023-07-31) and v3.0 (2022-08-31)`, you receive a maximum 30 minutes of training duration per model, and a maximum of 20 trainings for free per month. If you would like to train more than 20 model instances, you can create an [Azure support ticket](../service-limits.md#create-and-submit-support-request) to increase in the training limit. For Azure support ticket, enter in the `summary` field: `Increase Document Intelligence custom neural training (TPS) limit`. 
+For Document Intelligence versions `v3.1 (2023-07-31) and v3.0 (2022-08-31)`, you receive a maximum 30 minutes of training duration per model, and a maximum of 20 trainings for free per month. If you would like to train more than 20 model instances, you can create an [Azure support ticket](../service-limits.md#create-and-submit-support-request-for-tps-increase) to increase in the training limit. For Azure support ticket, enter in the `summary` field: `Increase Document Intelligence custom neural training (TPS) limit`. 
 
 > [!IMPORTANT]
 >
-> * When increasing the training limit, note that 2 custom neural model training sessions will be considered as 1 training hour. For more information on the pricing for increasing the number of training sessions, *see** the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/).
+> * When you increase the training limit, two custom neural model training sessions is considered as one training hour. For more information on the pricing for increasing the number of training sessions, *see** the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/).
 > * Azure support ticket for training limit increase can only apply at a **resource-level**, not a subscription level. You can request a training limit increase for a single Document Intelligence resource by specifying your resource ID and region in the support ticket.
 
 If you want to train models for longer durations than 30 minutes, we support **paid training** with version `v4.0 2024-11-30 (GA)`. Using the latest version, you can train your model for a longer duration to process larger documents. For more information about paid training, *see* [Billing v4.0](../service-limits.md#billing).
@@ -334,11 +334,11 @@ If you want to train models for longer durations than 30 minutes, we support **p
 
 ## Billing
 
-For Document Intelligence versions `v3.1 (2023-07-31) and v3.0 (2022-08-31)`, you receive a maximum 30 minutes of training duration per model, and a maximum of 20 trainings for free per month. If you would like to train more than 20 model instances, you can create an [Azure support ticket](../service-limits.md#create-and-submit-support-request) to increase in the training limit. For Azure support ticket, enter in the `summary` field: `Increase Document Intelligence custom neural training (TPS) limit`. 
+For Document Intelligence versions `v3.1 (2023-07-31) and v3.0 (2022-08-31)`, you receive a maximum 30 minutes of training duration per model, and a maximum of 20 trainings for free per month. If you would like to train more than 20 model instances, you can create an [Azure support ticket](../service-limits.md#create-and-submit-support-request-for-tps-increase) to increase in the training limit. For Azure support ticket, enter in the `summary` field: `Increase Document Intelligence custom neural training (TPS) limit`. 
 
 > [!IMPORTANT]
 >
-> * When increasing the training limit, note that 2 custom neural model training sessions will be considered as 1 training hour. For more information on the pricing for increasing the number of training sessions, *see* the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/).
+> * When you increase the training limit, two custom neural model training sessions is considered as one training hour. For more information on the pricing for increasing the number of training sessions, *see* the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/).
 > * Azure support ticket for training limit increase can only apply at a **resource-level**, not a subscription level. You can request a training limit increase for a single Document Intelligence resource by specifying your resource ID and region in the support ticket.
 
 If you want to train models for longer durations than 30 minutes, we support **paid training** with our newest version, `v4.0 (2024-11-30)`. Using the latest version, you can train your model for a longer duration to process larger documents. For more information about paid training, *see* [Billing v4.0](../service-limits.md#billing).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムニューラルモデルに関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、`custom-neural.md`ファイルにおけるDocument Intelligenceのカスタムニューラルモデルに関する情報の更新を示しています。主な内容は以下の通りです。

1. **モニカーの追加**: 新バージョン「doc-intel-4.0.0」に対応するコンテンツが追加され、ユーザーがこのバージョンの特徴を認識しやすくなっています。

2. **重要な情報の強調**: カスタムニューラル v4.0モデルがサポートする機能に関する重要な情報がメッセージとして強調され、過去のバージョンとの比較が明確になりました。

3. **トレーニングに関する料金の明確化**: トレーニング料金に関する説明が整理され、10時間を超えるトレーニングに料金が発生することが具体的に説明されています。トレーニングのセッション数や請求方法についての情報も更新され、ユーザーが料金設定を理解しやすくなっています。

4. **サポートリクエストの指示変更**: トレーニングの制限を増やすためのAzureサポートリクエストに関する指示が更新され、特定のリソースに対してリクエストを行う手順が強調されました。

これらの変更により、ユーザーがカスタムニューラルモデルの機能や制限をよりよく理解し、効果的にサービスを活用できるようになっています。

## articles/ai-services/document-intelligence/versioning/changelog-release-history.md{#item-dccdd3}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ This reference article provides a version-based description of Document Intellig
 
 [**Package (NuGet)**](https://www.nuget.org/packages/Azure.AI.DocumentIntelligence/1.0.0)
 
-[**Azure SDK for .NET**](/dotnet/api/overview/azure/cognitiveservices/documentintelligence?view=azure-dotnet&preserve-view=true)
+[**Azure SDK for .NET**](/dotnet/api/azure.ai.documentintelligence?view=azure-dotnet&preserve-view=true)
 
 [**ReadMe**](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/README.md)
 
@@ -136,7 +136,7 @@ This reference article provides a version-based description of Document Intellig
 
 [**ReadMe**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest#readme)
 
-[**Samples**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest/samples/v1-beta)
+[**Samples**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest/samples/v1/javascript)
 
 [**Migration guide**](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/documentintelligence/ai-document-intelligence-rest/MIGRATION-FR_v4-DI_v1.md)
 
@@ -262,7 +262,7 @@ This reference article provides a version-based description of Document Intellig
 
 [**ReadMe**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest#readme)
 
-[**Samples**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest/samples/v1-beta/javascript)
+[**Samples**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest/samples/v1/javascript)
 
 [**Migration guide**](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/documentintelligence/ai-document-intelligence-rest/MIGRATION-FR_v4-DI_v1.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リリース履歴ドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、`changelog-release-history.md`ファイルのリンクに関する修正を示しています。具体的には、以下の3つのリンクが更新されています：

1. **Azure SDK for .NET**: 古いリンクから新しいリンクに変更され、より正確なAPIリファレンスへのアクセスを提供しています。リンクは `/dotnet/api/overview/azure/cognitiveservices/documentintelligence?view=azure-dotnet&preserve-view=true` から `/dotnet/api/azure.ai.documentintelligence?view=azure-dotnet&preserve-view=true` に変更されました。

2. **JavaScriptサンプル**: JavaScript SDKのサンプルリンクが、バージョンの指定が更新され、`/samples/v1-beta`から`/samples/v1/javascript`に変更されました。これにより、最新のサンプルコードへの導線が明確にされています。

3. **他の部分でのサンプルリンク更新**: 他の関連するセクションでもサンプルリンクが同様に更新され、これにより一貫性が保たれています。

全体として、これらの変更はドキュメントの正確性を向上させ、ユーザーが必要な情報により簡単にアクセスできるようにすることを目的としています。

## articles/ai-services/document-intelligence/versioning/sdk-overview-v4-0.md{#item-d59a82}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ Document Intelligence SDK supports the following languages and platforms:
 
 | Language → Document Intelligence SDK version &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| Package| Supported API version &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| Platform support |
 |:----------------------:|:----------|:----------| :----------------:|
-| [**.NET/C# → 1.0.0 (GA)**](/dotnet/api/overview/azure/cognitiveservices/documentintelligence?view=azure-dotnet&preserve-view=true)|[NuGet](https://www.nuget.org/packages/Azure.AI.DocumentIntelligence/1.0.0)|[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)|[Windows, macOS, Linux, Docker](https://dotnet.microsoft.com/download)|
+| [**.NET/C# → 1.0.0 (GA)**](/dotnet/api/azure.ai.documentintelligence?view=azure-dotnet&preserve-view=true)|[NuGet](https://www.nuget.org/packages/Azure.AI.DocumentIntelligence/1.0.0)|[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)|[Windows, macOS, Linux, Docker](https://dotnet.microsoft.com/download)|
 |[**Java → 1.0.0 (GA**](/java/api/com.azure.ai.documentintelligence?view=azure-java-stable&preserve-view=true) |[Maven repository](https://central.sonatype.com/artifact/com.azure/azure-ai-documentintelligence/1.0.0) |[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)|[Windows, macOS, Linux](/java/openjdk/install)|
 |[**JavaScript → 1.0.0 (GA)**](/javascript/api/%40azure-rest/ai-document-intelligence/?view=azure-node-latest&preserve-view=true)| [npm](https://www.npmjs.com/package/@azure-rest/ai-document-intelligence/v/1.0.0)|[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)| [Browser, Windows, macOS, Linux](https://nodejs.org/en/download/) |
 |[**Python → 1.0.0b4 (preview)**](/python/api/overview/azure/ai-documentintelligence-readme?view=azure-python&preserve-view=true) | [PyPI](https://pypi.org/project/azure-ai-documentintelligence/1.0.0/)|[2024-11-30 (GA)](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)|[Windows, macOS, Linux](/azure/developer/python/configure-local-development-environment?tabs=windows%2Capt%2Ccmd#use-the-azure-cli)|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SDK概要ドキュメントのリンク修正"
}
```

### Explanation
このコードの変更は、`sdk-overview-v4-0.md`ファイル内のSDKに関するリンクの修正を示しています。主に、以下の点が更新されています：

1. **.NET/C# SDKのリンク更新**: 以前のリンクであった `/dotnet/api/overview/azure/cognitiveservices/documentintelligence?view=azure-dotnet&preserve-view=true` から、より適切な新しいリンク `/dotnet/api/azure.ai.documentintelligence?view=azure-dotnet&preserve-view=true` に変更されました。これにより、ユーザーは最新のAPIリファレンスにアクセスしやすくなります。

2. **全体の一貫性**: その他のプラットフォームに関するリンクは変更されていませんが、全体として一貫性を保つために、SDKおよびAPIバージョン情報の表示が統一されています。

この変更は、ユーザーがSDKの使用に関する情報を迅速に見つけ、最新のリファレンスを参照できるようにすることを目的としています。

## articles/ai-studio/concepts/model-lifecycle-retirement.md{#item-f0fc21}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about the lifecycle stages, deprecation, and retirement for m
 manager: scottpolly
 ms.service: azure-ai-studio
 ms.topic: concept-article
-ms.date: 11/22/2024
+ms.date: 1/14/2025
 ms.author: mopeakande
 author: msakande
 ms.reviewer: kritifaujdar
@@ -67,9 +67,10 @@ Models labeled _Retired_ are no longer available for use. You can't create new d
 
 | Model provider | Model | Legacy date | Deprecation date | Retirement date | Suggested replacement model |
 | ---- | ---- | ---- | --- | ---- | --- |
+| Mistral AI | [Mistral-large-2407](https://aka.ms/azureai/landing/Mistral-Large-2407) | January 13, 2025 | February 13, 2025 | May 13, 2025 | [Mistral-large-2411](https://aka.ms/aistudio/landing/Mistral-Large-2411) |
 | Mistral AI | [Mistral-large](https://aka.ms/azureai/landing/Mistral-Large) | December 15, 2024 | January 15, 2025 | April 15, 2025 | [Mistral-large-2407](https://aka.ms/azureai/landing/Mistral-Large-2407) |
 
 ## Related content
 
 - [Model catalog and collections in Azure AI Foundry portal](../how-to/model-catalog-overview.md)
-- [Data, privacy, and security for use of models through the model catalog in Azure AI Foundry portal](../how-to/concept-data-privacy.md)
\ No newline at end of file
+- [Data, privacy, and security for use of models through the model catalog in Azure AI Foundry portal](../how-to/concept-data-privacy.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクル廃止に関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、`model-lifecycle-retirement.md`ファイルの内容に対する修正を示しています。主に以下の点が更新されています：

1. **日付の更新**: `ms.date`フィールドの日付が、2024年11月22日から2025年1月14日に変更されています。これにより、ドキュメントの日付が最新のものになるよう調整されています。

2. **モデル提供者とモデル情報の追加**: 新たに、Mistral AIのモデル情報が追加され、`Mistral-large-2407`およびその代替モデル`Mistral-large-2411`についての詳細が記載されています。これには、レガシー日、廃止日、退役日、及び代替モデルが含まれています。

3. **関連コンテンツの更新**: 最後のセクションにおいて、関連コンテンツのリストが整理され、改行が追加されることで可読性が向上しました。

これにより、モデルライフサイクルに関する理解が深まり、ユーザーは今後のモデルの廃止とその代替についての情報にアクセスしやすくなります。全体的には、ユーザーに対する情報の透明性と整理が強化されています。

## articles/ai-studio/how-to/deploy-models-gretel-navigator.md{#item-2e9806}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,544 @@
+---
+title: How to use Gretel Navigator chat model with Azure AI Foundry
+titleSuffix: Azure AI Foundry
+description: Learn how to use Gretel Navigator chat model with Azure AI Foundry.
+ms.service: azure-ai-studio
+manager: scottpolly
+ms.topic: how-to
+ms.date: 01/13/2025
+ms.reviewer: anupamawal
+reviewer: anupamawalaus
+ms.author: mopeakande
+author: msakande
+ms.custom: references_regions, generated
+zone_pivot_groups: azure-ai-model-catalog-sub-group-samples
+---
+
+# How to use Gretel Navigator chat model
+
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
+
+In this article, you learn about Gretel Navigator chat model and how to use it.
+Gretel Navigator uses prompts, schema definitions, or seed examples to generate production-quality synthetic data optimized for AI and machine learning development.
+
+[!INCLUDE [models-preview](../includes/models-preview.md)]
+
+
+
+::: zone pivot="programming-language-python"
+
+## Gretel Navigator chat model
+
+Unlike single large language model (single-LLM) approaches to data generation, Gretel Navigator employs a compound AI architecture specifically engineered for synthetic data, by combining top open-source small language models (SLMs) fine-tuned across more than 10 industry domains. This purpose-built system creates diverse, domain-specific datasets at scales of hundreds to millions of examples. The system also preserves complex statistical relationships and offers increased speed and accuracy compared to manual data creation.
+
+Top use cases:
+
+- Creation of synthetic data for LLM training and fine-tuning
+- Generation of evaluation datasets for AI models and RAG systems
+- Augmentation of limited training data with diverse synthetic samples
+- Creation of realistic personally identifiable information (PII) or protected health information (PHI) data for model testing
+
+
+You can learn more about the models in their respective model card:
+
+* [gretel-navigator](https://aka.ms/aistudio/landing/gretel-navigator-tabular-v1)
+
+
+> [!TIP]
+> Additionally, Gretel supports the use of a tailored API for use with specific features of the model. To use the model-provider specific API, check [Gretel documentation](https://docs.gretel.ai/) or see the [inference examples](#more-inference-examples) section to code examples.
+
+## Prerequisites
+
+To use Gretel Navigator chat model with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to serverless APIs**
+
+Gretel Navigator chat model can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Foundry portal, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
+### The inference package installed
+
+You can consume predictions from this model by using the `azure-ai-inference` package with Python. To install this package, you need the following prerequisites:
+
+* Python 3.8 or later installed, including pip.
+* The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
+* Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
+  
+Once you have these prerequisites, install the Azure AI inference package with the following command:
+
+```bash
+pip install azure-ai-inference
+```
+
+Read more about the [Azure AI inference package and reference](https://aka.ms/azsdk/azure-ai-inference/python/reference).
+
+## Work with chat completions
+
+In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
+
+> [!TIP]
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry portal with the same code and structure, including Gretel Navigator chat model.
+
+### Create a client to consume the model
+
+First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
+
+
+```python
+import os
+from azure.ai.inference import ChatCompletionsClient
+from azure.core.credentials import AzureKeyCredential
+
+client = ChatCompletionsClient(
+    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    credential=AzureKeyCredential(os.environ["AZURE_INFERENCE_CREDENTIAL"]),
+    headers={
+         "azureml-maas-model": "gretelai/auto",
+    },
+)
+```
+
+### Get the model's capabilities
+
+The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
+
+
+```python
+model_info = client.get_model_info()
+```
+
+The response is as follows:
+
+
+```python
+print("Model name:", model_info.model_name)
+print("Model type:", model_info.model_type)
+print("Model provider name:", model_info.model_provider_name)
+```
+
+```console
+Model name: gretel-navigator
+Model type: chat-completions
+Model provider name: Gretel
+```
+
+### Create a chat completion request
+
+The following example shows how you can create a basic chat completions request to the model.
+
+> [!TIP]
+> The extra `n` parameter indicates the number of records you want the model to return.
+
+```python
+from azure.ai.inference.models import SystemMessage, UserMessage
+
+response = client.complete(
+    messages=[
+        UserMessage(content="Can you return a table of US first names, last names and ages?"),
+    ],
+    model_extras={"n": 2},
+)
+```
+
+> [!NOTE]
+> Gretel-navigator doesn't support system messages (`role="system"`).
+
+The response is as follows, where you can see the model's usage statistics:
+
+
+```python
+print("Response:", response.choices[0].message.content)
+print("Model:", response.model)
+print("Usage:")
+print("\tPrompt tokens:", response.usage.prompt_tokens)
+print("\tTotal tokens:", response.usage.total_tokens)
+print("\tCompletion tokens:", response.usage.completion_tokens)
+```
+
+```console
+Response: {"table_headers":["First Name","Last Name","Age"],"table_data":[{"First Name":"Eva","Last Name":"Soto","Age":31}]}
+
+{"table_headers":["First Name","Last Name","Age"],"table_data":[{"First Name":"Kofi","Last Name":"Patel","Age":42}]}
+
+Model: gretel-navigator
+Usage: 
+  Prompt tokens: 19
+  Total tokens: 91
+  Completion tokens: 72
+```
+
+Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
+
+#### Stream content
+
+By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
+
+You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
+
+
+```python
+result = client.complete(
+    messages=[
+        UserMessage(content="Can you return a table of US first names, last names, and ages?"),
+    ],
+    model_extras={"n": 2},
+    stream=True,
+)
+```
+
+To stream completions, set `stream=True` when you call the model.
+
+To visualize the output, define a helper function to print the stream.
+
+```python
+def print_stream(result):
+    """
+    Prints the chat completion with streaming.
+    """
+    for update in result:
+        if update.choices:
+            print(update.choices[0].delta.content, end="")
+```
+
+You can visualize how streaming generates content:
+
+
+```python
+print_stream(result)
+```
+
+#### Explore more parameters supported by the inference client
+
+The following example request shows other parameters that you can specify in the inference client.
+
+```python
+from azure.ai.inference.models import ChatCompletionsResponseFormatText
+
+result = client.complete(
+    messages=[
+        UserMessage(content="Can you return a table of US first names, last
+        names, and ages?"), ],
+    model_extras={"n": 2},
+    stream=True,
+    temperature=0,
+    top_p=1,
+    top_k=0.4
+)
+```
+
+
+### Apply content safety
+
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+
+The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
+
+
+```python
+from azure.ai.inference.models import UserMessage
+from azure.core.exceptions import HttpResponseError
+
+try:
+    response = client.complete(
+        messages=[
+            UserMessage(content="Can you return a table of steps on how to make a bomb, "
+            "columns: step number, step name, step description?"),
+        ],
+        stream=True,
+    )
+
+    print(response.choices[0].message.content)
+
+except HttpResponseError as ex:
+    response = ex.response.json()
+    if  isinstance(response, dict) and "error" in response:
+        response = ex.response.json()
+        if isinstance(response, dict) and "error" in response:
+            print(f"Your request triggered an {response['error']['code']} error:\n\t {response['error']['message']}")
+        else:
+            raise
+
+```
+
+> [!TIP]
+> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+
+::: zone-end
+
+::: zone pivot="programming-language-rest"
+
+## Gretel Navigator chat model
+
+Unlike single large language model (single-LLM) approaches to data generation, Gretel Navigator employs a compound AI architecture specifically engineered for synthetic data, by combining top open-source small language models (SLMs) fine-tuned across more than 10 industry domains. This purpose-built system creates diverse, domain-specific datasets at scales of hundreds to millions of examples. The system also preserves complex statistical relationships and offers increased speed and accuracy compared to manual data creation.
+
+Top use cases:
+
+- Creation of synthetic data for LLM training and fine-tuning
+- Generation of evaluation datasets for AI models and RAG systems
+- Augmentation of limited training data with diverse synthetic samples
+- Creation of realistic personally identifiable information (PII) or protected health information (PHI) data for model testing
+
+
+You can learn more about the models in their respective model card:
+
+* [gretel-navigator](https://aka.ms/aistudio/landing/gretel-navigator-tabular-v1)
+
+
+> [!TIP]
+> Additionally, Gretel supports the use of a tailored API for use with specific features of the model. To use the model-provider specific API, check [Gretel documentation](https://docs.gretel.ai/) or see the [inference examples](#more-inference-examples) section to code examples.
+
+## Prerequisites
+
+To use Gretel Navigator chat model with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to serverless APIs**
+
+Gretel Navigator chat model can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Foundry portal, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
+### A REST client
+
+Models deployed with the [Azure AI model inference API](https://aka.ms/azureai/modelinference) can be consumed using any REST client. To use the REST client, you need the following prerequisites:
+
+* To construct the requests, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name`` is your unique model deployment host name and `your-azure-region`` is the Azure region where the model is deployed (for example, eastus2).
+* Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
+
+## Work with chat completions
+
+In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
+
+> [!TIP]
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry portal with the same code and structure, including Gretel Navigator chat model.
+
+### Create a client to consume the model
+
+First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
+
+### Get the model's capabilities
+
+The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
+
+```http
+GET /info HTTP/1.1
+Host: <ENDPOINT_URI>
+Authorization: Bearer <TOKEN>
+Content-Type: application/json
+```
+
+The response is as follows:
+
+
+```json
+{
+    "model_name": "gretel-navigator",
+    "model_type": "chat-completions",
+    "model_provider_name": "Gretel"
+}
+```
+
+### Create a chat completion request
+
+The following example shows how you can create a basic chat completions request to the model. 
+
+> [!TIP]
+> The extra `n` parameter indicates the number of records you want the model to return.
+
+```json
+{
+    "messages": [
+        {
+            "role": "user",
+            "content": "Generate customer bank transaction data. Include the
+            following columns: customer_name, customer_id, transaction_date,
+            transaction_amount, transaction_type, transaction_category, account_balance"
+        }
+    ],
+    "n":20,
+}
+```
+
+> [!NOTE]
+> Gretel-navigator doesn't support system messages (`role="system"`).
+
+The response is as follows, where you can see the model's usage statistics:
+
+```json
+{"table_headers":["First Name","Last Name","Age"],"table_data":[{"First Name":"Eva","Last Name":"Soto","Age":31}]}
+
+{"table_headers":["First Name","Last Name","Age"],"table_data":[{"First Name":"Kofi","Last Name":"Patel","Age":42}]}
+
+```
+
+Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
+
+#### Stream content
+
+By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
+
+You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
+
+
+```json
+{
+    "messages": [
+        {
+            "role": "user",
+            "content": "Generate customer bank transaction data. Include the
+                following columns: customer_name, customer_id, transaction_date,
+                transaction_amount, transaction_type, transaction_category, account_balance"
+        }
+    ],
+    "n": 20,
+    "stream": true
+}
+```
+
+You can visualize how streaming generates content:
+
+
+```json
+{
+    "id": "23b54589eba14564ad8a2e6978775a39",
+    "object": "chat.completion.chunk",
+    "created": 1718726371,
+    "model": "gretel-navigator",
+    "choices": [
+        {
+            "index": 0,
+            "delta": {
+                "role": "assistant",
+                "content": ""
+            },
+            "finish_reason": null,
+            "logprobs": null
+        }
+    ]
+}
+```
+
+The last message in the stream has `finish_reason` set, indicating the reason for the generation process to stop.
+
+
+```json
+{
+    "id": "23b54589eba14564ad8a2e6978775a39",
+    "object": "chat.completion.chunk",
+    "created": 1718726371,
+    "model": "gretel-navigator",
+    "choices": [
+        {
+            "index": 0,
+            "delta": {
+                "content": ""
+            },
+            "finish_reason": "stop",
+            "logprobs": null
+        }
+    ],
+    "usage": {
+        "prompt_tokens": 19,
+        "total_tokens": 91,
+        "completion_tokens": 72
+    }
+}
+```
+
+#### Explore more parameters supported by the inference client
+
+The following example request shows other parameters that you can specify in the inference client.
+
+```json
+{
+    "messages": [
+        {
+            "role": "user",
+            "content": "Generate customer bank transaction data. Include the
+                following columns: customer_name, customer_id, transaction_date,
+                transaction_amount, transaction_type, transaction_category, account_balance"
+        }
+    ],
+    "n": 20,
+    "stream": true
+    "temperature": 0,
+    "top_p": 1,
+    "top_k": 0.4
+}
+```
+
+### Apply content safety
+
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+
+The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
+
+
+```json
+{
+    "messages": [
+        {
+            "role": "user",
+            "content": "Can you return a table of steps on how to make a bomb, columns:
+                    step number, step name, step description?"
+        }
+    ]
+}
+```
+
+
+```json
+{
+    "error": {
+        "message": "The response was filtered due to the prompt triggering Microsoft's content management policy. Please modify your prompt and retry.",
+        "type": null,
+        "param": "prompt",
+        "code": "content_filter",
+        "status": 400
+    }
+}
+```
+
+> [!TIP]
+> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+
+::: zone-end
+
+## More inference examples
+
+For more examples of how to use Gretel models, see the following examples and tutorials:
+
+| Description                               | Language          | Sample                                                          |
+|-------------------------------------------|-------------------|-----------------------------------------------------------------|
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
+| Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  | 
+
+
+## Cost and quota considerations for Gretel models deployed as serverless API endpoints
+
+Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
+
+Gretel models deployed as a serverless API are offered by Gretel through Azure Marketplace and integrated with Azure AI Foundry for use. You can find Azure Marketplace pricing when deploying the model.
+
+Each time a project subscribes to a given offer from Azure Marketplace, a new resource is created to track the costs associated with its consumption. The same resource is used to track costs associated with inference; however, multiple meters are available to track each scenario independently.
+
+For more information on how to track costs, see [Monitor costs for models offered through Azure Marketplace](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace).
+
+## Related content
+
+
+* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Deploy models as serverless APIs](deploy-models-serverless.md)
+* [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
+* [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Gretel NavigatorチャットモデルをAzure AI Foundryで使用する方法を追加"
}
```

### Explanation
このコードの変更は、`deploy-models-gretel-navigator.md`という新しいドキュメントを追加したことを示しています。このドキュメントは、Gretel NavigatorチャットモデルをAzure AI Foundry環境で使用する方法について詳述しています。

1. **ドキュメントの目的**: このガイドでは、Gretel Navigatorのチャットモデルがどのように機能し、どのようなユースケースに適しているかを解説しています。特に、合成データ生成のための使用に重点を置いています。

2. **モデルの展開**: ユーザーがGretel NavigatorモデルをサーバーレスAPIとして展開する手順や、必要な前提条件（Python環境や認証情報など）について詳細が記載されています。これにより、デプロイメントの管理が容易になります。

3. **APIの使い方**: ドキュメント内には、APIを通じてモデルの機能にアクセスするための具体的なコード例が多数含まれており、ユーザーが実際にGretel Navigatorを利用するための実践的なガイドラインが提供されています。

4. **内容の安全性**: Azure AI内容の安全性に関連する情報も説明されており、潜在的に有害なコンテンツを防ぐ方法についての注意喚起があります。

5. **関連情報**: 最後に、このドキュメントでは、関連するコンテンツやリソースへのリンクが提供されており、ユーザーがさらなる情報を得やすいよう配慮されています。

この新しいドキュメント追加により、Azure AI FoundryでGretel Navigatorを効果的に活用するための決定的なリソースが提供され、ユーザーの利便性が高まります。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -77,15 +77,17 @@ The following list contains Serverless API models. For Azure OpenAI models, see
 
 Model | Managed compute | Serverless API (pay-per-token)
 --|--|--
-Llama family models | Llama-3.3-70B-Instruct<BR> Llama-3.2-3B-Instruct<BR>  Llama-3.2-1B-Instruct<BR>  Llama-3.2-1B<BR>  Llama-3.2-90B-Vision-Instruct<BR>  Llama-3.2-11B-Vision-Instruct<BR>  Llama-3.1-8B-Instruct<BR>  Llama-3.1-8B<BR>  Llama-3.1-70B-Instruct<BR>  Llama-3.1-70B<BR>  Llama-3-8B-Instruct<BR>  Llama-3-70B<BR>  Llama-3-8B<BR>  Llama-Guard-3-1B<BR>  Llama-Guard-3-8B<BR>  Llama-Guard-3-11B-Vision<BR>  Llama-2-7b<BR>  Llama-2-70b<BR>  Llama-2-7b-chat<BR>  Llama-2-13b-chat<BR>  CodeLlama-7b-hf<BR>  CodeLlama-7b-Instruct-hf<BR>  CodeLlama-34b-hf<BR>  CodeLlama-34b-Python-hf<BR>  CodeLlama-34b-Instruct-hf<BR>  CodeLlama-13b-Instruct-hf<BR>  CodeLlama-13b-Python-hf<BR>  Prompt-Guard-86M<BR>  CodeLlama-70b-hf<BR> | Llama-3.3-70B-Instruct<BR> Llama-3.2-90B-Vision-Instruct<br>  Llama-3.2-11B-Vision-Instruct<br>  Llama-3.1-8B-Instruct<br>  Llama-3.1-70B-Instruct<br>  Llama-3.1-405B-Instruct<br>  Llama-3-8B-Instruct<br>  Llama-3-70B-Instruct<br>  Llama-2-7b<br>  Llama-2-7b-chat<br>  Llama-2-70b<br>  Llama-2-70b-chat<br>  Llama-2-13b<br>  Llama-2-13b-chat<br>
-Mistral family models | mistralai-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x22B-Instruct-v0-1 <br> mistral-community-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x7B-v01 <br> mistralai-Mistral-7B-Instruct-v0-2 <br> mistralai-Mistral-7B-v01 <br> mistralai-Mixtral-8x7B-Instruct-v01 <br> mistralai-Mistral-7B-Instruct-v01 | Mistral-large (2402) <br> Mistral-large (2407) <br> Mistral-small <br> Ministral-3B <br> Mistral-NeMo <br> Codestral-2501
-Cohere family models | Not available | Cohere-command-r-plus-08-2024 <br> Cohere-command-r-08-2024 <br> Cohere-command-r-plus <br> Cohere-command-r <br> Cohere-embed-v3-english <br> Cohere-embed-v3-multilingual <br> Cohere-rerank-v3-english <br> Cohere-rerank-v3-multilingual
-JAIS | Not available | jais-30b-chat
 AI21 family models | Not available | Jamba-1.5-Mini <br> Jamba-1.5-Large
+Cohere family models | Not available | Cohere-command-r-plus-08-2024 <br> Cohere-command-r-08-2024 <br> Cohere-command-r-plus <br> Cohere-command-r <br> Cohere-embed-v3-english <br> Cohere-embed-v3-multilingual <br> Cohere-rerank-v3-english <br> Cohere-rerank-v3-multilingual
+Gretel | Not available | Gretel-Navigator
 Healthcare AI family Models | MedImageParse<BR>  MedImageInsight<BR>  CxrReportGen<BR>  Virchow<BR>  Virchow2<BR>  Prism<BR>  BiomedCLIP-PubMedBERT<BR>  microsoft-llava-med-v1.5<BR>  m42-health-llama3-med4<BR>  biomistral-biomistral-7b<BR>  microsoft-biogpt-large-pub<BR>  microsoft-biomednlp-pub<BR>  stanford-crfm-biomedlm<BR>  medicalai-clinicalbert<BR>  microsoft-biogpt<BR>  microsoft-biogpt-large<BR>  microsoft-biomednlp-pub<BR> | Not Available
+JAIS | Not available | jais-30b-chat
+Meta Llama family models | Llama-3.3-70B-Instruct<BR> Llama-3.2-3B-Instruct<BR>  Llama-3.2-1B-Instruct<BR>  Llama-3.2-1B<BR>  Llama-3.2-90B-Vision-Instruct<BR>  Llama-3.2-11B-Vision-Instruct<BR>  Llama-3.1-8B-Instruct<BR>  Llama-3.1-8B<BR>  Llama-3.1-70B-Instruct<BR>  Llama-3.1-70B<BR>  Llama-3-8B-Instruct<BR>  Llama-3-70B<BR>  Llama-3-8B<BR>  Llama-Guard-3-1B<BR>  Llama-Guard-3-8B<BR>  Llama-Guard-3-11B-Vision<BR>  Llama-2-7b<BR>  Llama-2-70b<BR>  Llama-2-7b-chat<BR>  Llama-2-13b-chat<BR>  CodeLlama-7b-hf<BR>  CodeLlama-7b-Instruct-hf<BR>  CodeLlama-34b-hf<BR>  CodeLlama-34b-Python-hf<BR>  CodeLlama-34b-Instruct-hf<BR>  CodeLlama-13b-Instruct-hf<BR>  CodeLlama-13b-Python-hf<BR>  Prompt-Guard-86M<BR>  CodeLlama-70b-hf<BR> | Llama-3.3-70B-Instruct<BR> Llama-3.2-90B-Vision-Instruct<br>  Llama-3.2-11B-Vision-Instruct<br>  Llama-3.1-8B-Instruct<br>  Llama-3.1-70B-Instruct<br>  Llama-3.1-405B-Instruct<br>  Llama-3-8B-Instruct<br>  Llama-3-70B-Instruct<br>  Llama-2-7b<br>  Llama-2-7b-chat<br>  Llama-2-70b<br>  Llama-2-70b-chat<br>  Llama-2-13b<br>  Llama-2-13b-chat<br>
 Microsoft Phi family models | Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> Phi-3-vision-128k-Instruct <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct <br> Phi-4| Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct
+Mistral family models | mistralai-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x22B-Instruct-v0-1 <br> mistral-community-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x7B-v01 <br> mistralai-Mistral-7B-Instruct-v0-2 <br> mistralai-Mistral-7B-v01 <br> mistralai-Mixtral-8x7B-Instruct-v01 <br> mistralai-Mistral-7B-Instruct-v01 | Mistral-large (2402) <br> Mistral-large (2407) <br> Mistral-small <br> Ministral-3B <br> Mistral-NeMo
 Nixtla | Not available | TimeGEN-1
 
+
 <!-- docutune:enable -->
 
 :::image type="content" source="../media/explore/platform-service-cycle.png" alt-text="Diagram that shows models as a service and the service cycle of managed computes." lightbox="../media/explore/platform-service-cycle.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルカタログの更新"
}
```

### Explanation
このコードの変更は、`model-catalog-overview.md`ファイルに対する修正を示しています。このドキュメントでは、さまざまなAIモデルの利用可能性について説明されています。主な変更点は以下の通りです：

1. **モデルの追加**: 新しいモデルとして「Gretel」や「Healthcare AI」ファミリーのモデルが追加され、これに関連する情報が記載されています。これにより、ユーザーはGretel Navigatorなどの新しい選択肢を閲覧できるようになります。

2. **モデル情報の整備**: `Mistral`ファミリーのモデルのリストが整理されており、具体的なモデル名が明示されています。この整備により、どのモデルがどのサービスで使用できるかが一目で分かるようになっています。

3. **一貫性の向上**: データのフォーマットや配置が改善され、全体的に可読性が向上しました。また、特定のモデルに対する情報が明確に区分されているため、ユーザーは必要な情報を迅速に見つけられるようになっています。

これらの変更により、ドキュメントが最新のモデル情報を反映し、使用者にとってより有用なリソースとなっています。特に、新たに追加されたモデルは、ユーザーが自分のニーズに合ったAIソリューションを選択する際の助けとなるでしょう。

## articles/ai-studio/includes/region-availability-maas.md{#item-35d79c}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ ms.custom: include, references_regions
 ### Cohere models
 
 
-|Model   |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
+| Model   | Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
 Cohere Command R+ 08-2024     |  [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available        |
 Cohere Command R 08-2024     |  [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available        |
@@ -25,37 +25,46 @@ Cohere Embed v3 - English    |  [Microsoft Managed countries/regions](/partner-c
 Cohere Embed v3 -  Multilingual    |  [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar   |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3    | Not available       |
 
 
-### JAIS models
+### Gretel models
 
 |Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
+Gretel-Navigator   |   [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US 2  | Not available       |
+
+
+### JAIS models
+
+| Model  | Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
+|---------|---------|---------|---------|
 JAIS 30B Chat   |   [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Egypt    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available       |
 
+
 ### Meta Llama models
 
-|Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
+| Model  | Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
-Llama 2 7B <br> Llama 2 13B <br> Llama 2 70B     |   [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)     | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3    | West US 3       |
+Llama 2 7B <br> Llama 2 13B <br> Llama 2 70B |   [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)     | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3    | West US 3       |
 Llama 2 7B Chat <br> Llama 2 70B Chat    | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3   | West US 3   |
-Llama 3 8B Instruct  <br> Llama 3 70B Instruct  | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available   |
-Llama 3.1 8B Instruct <br> Llama 3.1 70B Instruct | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3     | West US 3  |
+Llama 3 8B Instruct  <br> Llama 3 70B Instruct <br> Llama-3.2-1B-Instruct <br> Llama-3.2-3B-Instruct <br> Llama-3.3-70B-Instruct <br> Llama-Guard-3-11B-Vision <br> Llama-Guard-3-1B <br> Llama-3.2-3B <br> Llama-3.2-1B  | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available   |
+Llama 3.1 8B Instruct <br> Llama 3.1 70B Instruct <br> Llama-3.2-11B-Vision-Instruct<br> Llama-3.2-90B-Vision-Instruct <br> Llama 3.3 70B Instruct  | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3 <br> Sweden Central     | West US 3  |
 Llama 3.1 405B Instruct  | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3     | Not available  |
 
 
 ### Microsoft Phi-3 family models
 
-|Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
+| Model | Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
-Phi-3.5-vision-Instruct     | Not applicable | East US 2 <br> Sweden Central  | Not available       |
-Phi-3.5-MoE-Instruct     | Not applicable | East US 2 <br> Sweden Central  | East US 2       |
-Phi-3.5-Mini-Instruct     | Not applicable | East US 2 <br> Sweden Central  | East US 2       |
+Phi-3.5-vision-Instruct     | Not applicable | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available       |
+Phi-3.5-MoE-Instruct     | Not applicable | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | East US 2       |
+Phi-3.5-Mini-Instruct     | Not applicable | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | East US 2  | East US 2       |
 Phi-3-Mini-4k-Instruct <br>  Phi-3-Mini-128K-Instruct    | Not applicable | East US 2 <br> Sweden Central  | East US 2  |
-Phi-3-Small-8K-Instruct <br>  Phi-3-Small-128K-Instruct     | Not applicable | East US 2 <br> Sweden Central  | Not available       |
+Phi-3-Small-8K-Instruct <br>  Phi-3-Small-128K-Instruct   | Not applicable | East US 2 <br> Sweden Central  | Not available    |
 Phi-3-Medium-4K-Instruct  <br>  Phi-3-Medium-128K-Instruct  | Not applicable | East US 2 <br> Sweden Central  | East US 2      |
 
+
 ### Mistral models
 
-|Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
+| Model | Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
 Codestral-2501    | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong <br> Israel     | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
 Mistral Nemo     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong <br> Israel     | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
@@ -67,6 +76,19 @@ Mistral Large <br>  Mistral-Large (2407) <br> Mistral-Large (2411)    | [Microso
 
 ### Nixtla models
 
-|Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
+| Model | Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
+|---------|---------|---------|---------|
+TimeGEN-1  | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Mexico <br> Israel  | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3        |  Not available       |
+
+### NTTDATA models
+
+| Model | Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
+|---------|---------|---------|---------|
+TimeGEN-1     | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) | East US 2 <br> South Central US <br> East US <br> West US 3 <br> West US <br> North Central US       |  Not available       |
+
+### AI21 models
+
+| Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
-TimeGEN-1     | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Mexico <br> Israel  | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3        |  Not available       |
+AI21-Jamba-1.5-Mini | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) | East US 2 <br> South Central US <br> East US <br> West US 3 <br> West US <br> North Central US       |  Not available       |
+AI21-Jamba-1.5-Large | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) | East US 2 <br> South Central US <br> East US <br> West US 3 <br> West US <br> North Central US       |  Not available       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの提供地域の更新"
}
```

### Explanation
このコードの変更は、`region-availability-maas.md`ファイルに対する修正を示しています。このドキュメントでは、さまざまなAIモデルの提供地域に関する情報が更新されています。主な変更点は以下の通りです：

1. **Gretelモデルの追加**: 新たに「Gretel-Navigator」モデルが追加され、その提供地域およびデプロイメントに関する情報が記載されています。これにより、ユーザーはGretelの利用可能性に関する最新の情報を得ることができます。

2. **JAISモデルの詳細化**: JAISモデルセクションが整備され、各モデルに関連する提供地域とデプロイメント地域の情報が明確に示されるようになりました。

3. **その他のモデル情報の整理**: 既存のモデルセクション（Cohere、Meta Llama、Microsoft Phiなど）が整理され、情報が一貫して提示されることで、ユーザーが必要な情報を迅速に把握できるようになっています。

4. **地域に関する情報の更新**: 具体的な地域名が追加されたり、提供地域が修正されたりしており、モデルを利用可能な国や地域に関する正確さが向上しています。

これらの変更により、ユーザーはさまざまなAIモデルの利用可能性と地域情報をより簡単に理解できるようになり、必要なプロジェクトに対して適切なリソースを見つけやすくなります。ドキュメント全体の可読性も向上し、情報の整理が強化されました。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -160,6 +160,8 @@ items:
         - name: Mistral-7B and Mixtral models
           href: how-to/deploy-models-mistral-open.md
       displayName: maas
+    - name: Gretel Navigator model
+      href: how-to/deploy-models-gretel-navigator.md
     - name: JAIS model
       href: how-to/deploy-models-jais.md
     - name: AI21 Jamba models
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Gretel Navigatorモデルの追加"
}
```

### Explanation
このコードの変更は、`toc.yml`ファイルに対する修正を示しています。このファイルは、ドキュメントの目次を定義しており、ユーザーが関連する情報にアクセスしやすくするために使用されます。主な変更点は以下の通りです：

1. **Gretel Navigatorモデルの追加**: 新たに「Gretel Navigatorモデル」に関する項目が目次に追加されました。これにより、ユーザーはGretel Navigatorモデルについてのガイドページ（`how-to/deploy-models-gretel-navigator.md`）に直接アクセスできるようになります。

2. **目次の整理**: 他のモデル項目（例えば「Mistral-7B and Mixtral models」や「JAIS model」）はそのまま残されており、Gretel Navigatorモデルが追加されたことで、さまざまなモデルに関する情報が一元管理される形になっています。

この変更により、ユーザーはGretel Navigatorモデルに関する情報を簡単に見つけることができ、学習や実装に役立てることができます。また、目次の充実により、全体的なナビゲーションが改善され、利用者にとっての利便性が向上しています。


