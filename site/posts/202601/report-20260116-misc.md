---
date: '2026-01-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b8d6e71...MicrosoftDocs:a88a880
summary: この差分では、Azureの「Document Intelligence」サービスに関するサービス制限、テキスト分析リファレンスサンプル、個人識別情報の概要文書の更新が行われました。主な変更内容は、文書の簡略化、日付の更新、リンクの修正であり、情報の明確性と最新性を向上させることを目的としています。新機能の追加はありませんが、既存の情報がより明確になっています。破壊的変更も特になく、ユーザーエクスペリエンスの向上が図られています。これにより、利用者は迅速に情報を理解でき、関連情報へのアクセスも改善されました。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b8d6e71...MicrosoftDocs:a88a880){target="_blank"}

### ハイライト
この差分では、Azureの"Document Intelligence"サービスのサービス制限およびテキスト分析リファレンスサンプル、そして個人識別情報に関する概要文書に関する更新が行われました。それぞれのドキュメントでの変更は主に内容の簡略化、文書の日付更新、リンクの修正であり、情報の明確性と最新性を向上させることを目的としています。

## 新機能
特定の新機能は追加されていませんが、既存の情報がより明確に表現されています。

## 破壊的変更
破壊的変更は特にありません。

## その他の更新
- "Document Intelligence"のドキュメントにおいて、文体の簡略化と明確化が行われました。
- テキスト分析リファレンスサンプルの文書日付が「2026年1月18日」に更新され、リンクが最新のAPIドキュメントのパスに修正されました。
- 個人識別情報の概要文書においても、日付が更新されました。

### インサイト
このコード差分では、主に既存ドキュメントの改良を通じてユーザーエクスペリエンスの向上が図られています。まず、"Document Intelligence"のサービス制限に関するドキュメントでは、文体が簡略化され冗長な部分が削除されたことで、サービスに関する情報を利用者が迅速に理解できるようになりました。これにより、ユーザーが誤った理解や混乱を避けるのに役立ちます。

次に、テキスト分析リファレンスサンプルでは、文書日付の更新により情報の最新性が確認され、また、APIドキュメントへのリンクの修正は利用者が関連情報にアクセスしやすい環境を形成しています。さらに、検索エンジンなどによるSEO対策にも貢献するでしょう。

個人識別情報に関しては、大きな内容変更はありませんが、文書が常に最新の情報を反映していることを示すための日付更新が行われました。こうした日付更新は信頼性を裏付ける要素として重要であり、ドキュメントの人気を持続的に保つための基本的な施策といえます。

このように、今回の変更によりドキュメントの実用性と正確性がさらに向上され、利用者の体験を向上させるものであると考えられます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [service-limits.md](#item-5ceae5) | minor update | サービス制限に関するドキュメント更新 | modified | 5 | 6 | 11 | 
| [reference-samples-text-analytics.md](#item-31fe2c) | minor update | テキスト分析リファレンスサンプルの更新 | modified | 2 | 2 | 4 | 
| [overview.md](#item-8a6932) | minor update | 個人識別情報の概要更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/service-limits.md{#item-5ceae5}

<details>
<summary>Diff</summary>
````diff
@@ -262,15 +262,15 @@ Document Intelligence billing is calculated monthly based on the model type and
 
 ## Detailed description, Quota adjustment, and best practices
 
-The default limits can be extended by requesting an increase via a support ticket. Before requesting a quota increase (where applicable), ensure that it's necessary. Document Intelligence service uses autoscaling to bring the required computational resources `on-demand`, keep the customer costs low, and deprovision unused resources by not maintaining an excessive amount of hardware capacity. 
+The default limits can be extended by requesting an increase via a support ticket. Before requesting a quota increase (where applicable), ensure that it's necessary.
 
 If your application returns Response Code 429 (*Too many requests*) you are over the threshold for one or more of the transactions per second limits (TPS):
 * **Analyze transactions Per Second limit**  The TPS for submitting analyze requests (POST)
 * **Get operations Per Second limit** The TPS for polling for results on analyze operations (GET)
 * **Model management operations Per Second limit** Operations related to  model management like build/train and copy.
 * **List operations Per Second limit** Operations related to listing models, operations.
 
-### General best practices to mitigate throttling during autoscaling
+### General best practices to mitigate throttling
 
 To minimize issues related to throttling (Response Code 429), we recommend using the following techniques:
 
@@ -285,7 +285,6 @@ The next sections describe specific cases of adjusting quotas.
 
 By default the number of transactions per second is limited to 15 transactions per second for a Document Intelligence resource. For the Standard pricing tier, TPS increase requests can be submitted, but whether they can be approved and at what TPS level adjustment will depend on the daily usage patterns and the best practices that are being followed. Before submitting the request, ensure you're familiar with the material in [this section](#detailed-description-quota-adjustment-and-best-practices) and aware of these [best practices](#example-of-a-workload-pattern-best-practice).
 
-The first step would be to enable auto scaling. Follow this document to enable auto scaling on your resource * [enable auto scaling](../../ai-services/autoscale.md). With auto scaling enabled your resource can continue to accept requests over the TPS limits configured if there's capacity on the service. It can still result in request throttled. 
 
 Increasing the Concurrent Request limit does **not** directly affect your costs. Document Intelligence service uses "Pay only for what you use" model. The limit defines how high the Service can scale before it starts throttle your requests.
 
@@ -312,13 +311,13 @@ Initiate the increase of transactions per second(TPS) limit for your resource by
 
 ## Example of a workload pattern best practice
 
-This example presents the approach we recommend following to mitigate possible request throttling due to [Autoscaling being in progress](#detailed-description-quota-adjustment-and-best-practices). It isn't an *exact recipe*, but merely a template we invite to follow and adjust as necessary.
+This example presents the approach we recommend following to mitigate possible request throttling. It isn't an *exact recipe*, but merely a template we invite to follow and adjust as necessary.
 
- Let us suppose that a Document Intelligence resource has the default limit set. Start the workload to submit your analyze requests. If you find that you're seeing frequent throttling with response code 429 when checking for completion, start by implementing an exponential backoff on the GET analyze response request. By using a progressively longer wait time between retries for consecutive error responses, for example a  2-5-13-34 pattern of delays between requests. In general, we recommended not calling the get analyze response more than once every 2 seconds for a corresponding POST request. The `analyze` response also contains a **retry-after** header that indicates how long you should wait in seconds before checking for completion of that request. 
+ Let us suppose that a Document Intelligence resource has the default limit set. Start the workload to submit your analyze requests. If you find that you're seeing frequent throttling with response code 429 when checking for completion, start by implementing an exponential backoff on the GET analyze response request. By using a progressively longer wait time between retries for consecutive error responses, for example a  2-5-13-34 pattern of delays between requests. In general, we recommend not calling the get analyze response more than once every 2 seconds for a corresponding POST request. The `analyze` response also contains a **retry-after** header that indicates how long you should wait in seconds before checking for completion of that request.
 
 If you find that you're being throttled on the number of POST requests for documents being submitted, consider adding a delay between the requests. If your workload requires a higher degree of concurrent processing, you then need to create a support request to increase your service limits on transactions per second.
 
-Generally, we recommended testing the workload and the workload patterns before going to production.
+Generally, we recommend testing the workload and the workload patterns before going to production.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス制限に関するドキュメント更新"
}
```

### Explanation
この差分は、"Document Intelligence"サービスの制限に関するドキュメントの更新を示しています。主要な変更点としては、いくつかの文が簡略化され、より明確な表現に置き換えられています。また、スラングや冗長な表現が削除され、情報の提供がよりスムーズになっています。

具体的には、ドキュメント内のセクションタイトルや説明文が更新されています。「一般的なベストプラクティス」のタイトルが「autoscaling」の文脈から独立して示され、調整の必要性を強調するために説明が若干短縮されました。また、例を挙げてリクエストのサイクルに関する推奨事項を再確認するための文も整理されています。このような変更は、利用者が情報を迅速に理解し、効果的にサービスを利用できるようにするためのものです。 

全体として、文書はより効率的に情報を提供するように改善されており、特にユーザーがサポートチケットを提出する際の注意点や、トランザクションの処理に関する推奨事項が引き続き重要視されています。これにより、文書は利用者にとってより使いやすく、実用的なものとなっています。

## articles/ai-services/language-service/includes/reference-samples-text-analytics.md{#item-31fe2c}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 11/18/2025
+ms.date: 01/18/2026
 author: laujan
 ms.author: lajanuar
 manager: nitinme
@@ -12,7 +12,7 @@ As you use this feature in your applications, see the following reference docume
 
 |Development option / language  |Reference documentation |Samples  |
 |---------|---------|---------|
-|REST API     | [REST API documentation](https://go.microsoft.com/fwlink/?linkid=2239169)        |         |
+|REST API     | [REST API documentation](/rest/api/language/)        |         |
 |C#     | [C# documentation](/dotnet/api/azure.ai.textanalytics?view=azure-dotnet-preview&preserve-view=true)        | [C# samples](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics/samples)        |
 | Java     | [Java documentation](/java/api/overview/azure/ai-textanalytics-readme?view=azure-java-preview&preserve-view=true)        | [Java Samples](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics/src/samples) |
 |JavaScript     | [JavaScript documentation](/javascript/api/overview/azure/ai-language-text-readme)        | [JavaScript samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/cognitivelanguage/ai-language-text/samples/v1) |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト分析リファレンスサンプルの更新"
}
```

### Explanation
このコードの差分は、テキスト分析用のリファレンスサンプルが含まれる文書の更新を示しています。主な変更点は、文書の日付およびいくつかの参照リンクです。

具体的には、文書の日付が「2025年11月18日」から「2026年1月18日」に変更されています。これにより、情報が最新のものであることが示されます。また、REST APIのドキュメントへのリンクが更新され、旧リンクから新しい相対パスへのリンクに修正されました。このリンク修正により、利用者が手軽に最新のAPIドキュメントにアクセスできるようになっています。

全体として、これらの変更は文書の正確性を保つためのものであり、ユーザーが関連情報を迅速に見つけられるようにするために意図されています。

## articles/ai-services/language-service/personally-identifiable-information/overview.md{#item-8a6932}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 11/18/2025
+ms.date: 01/18/2026
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人識別情報の概要更新"
}
```

### Explanation
このコードの差分は、個人識別情報に関する概要文書の更新を示しています。変更点は主に文書の日付の更新に関係しており、日付が「2025年11月18日」から「2026年1月18日」に変更されています。

このような日付の更新は、文書が最新の情報を反映していることを示すために重要であり、利用者に対して正確でタイムリーな情報を提供することを目的としています。この変更により、文書の信頼性と有用性が向上しています。全体として、本文自体には大きな変更はないものの、日付の更新によって文書がより現在の状況に即したものとなっています。


