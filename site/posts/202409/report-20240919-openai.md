---
date: '2024-09-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:78943fc...MicrosoftDocs:e496207
summary: このコードの変更は、Azure OpenAIサービスに関連する多数の更新と改良を含んでいます。主なポイントとして、GPT-4 Turbo with
  Visionに関する情報の削除、グローバルプロビジョンドデプロイメントの説明の統合、新たに追加されたテキスト読み上げ機能と音声認識機能があります。具体的には、JavaScript環境でのテキスト読み上げ機能とWhisperモデルを使用した音声認識機能が利用可能になりました。一方で、GPT-4
  Turbo with Visionに関する情報が大幅に削除されたことは、ユーザーにとっての影響が大きいとされています。全体として、これらの変更はAzure OpenAIサービスの情報の明確性を高め、ユーザー体験の向上を目指しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:78943fc...MicrosoftDocs:e496207){target="_blank"}

# Highlights
このコードの変更には、Azure OpenAIサービスに関する多くの更新と改良が含まれています。特に重要な点として、GPT-4 Turbo with Visionに関する情報の削除や、グローバルプロビジョンドデプロイメントタイプの統合説明、テキスト読み上げや音声認識機能に関する新機能の追加があります。

## 新機能
1. **JavaScriptにおけるテキスト読み上げ機能の追加**  
   JavaScript環境内でAzure OpenAIのテキスト読み上げ機能を利用できるようになりました。
   
2. **JavaScriptにおける音声認識機能（Whisper）の追加**  
   JavaScript環境でAzure OpenAIのWhisperモデルを使用し、音声認識を実行するためのドキュメントが追加されました。

## 破壊的変更
1. **GPT-4 Turbo with Visionに関する情報の大幅な削除**  
   `gpt-v-python.md`、`gpt-v-rest.md`、`gpt-v-studio.md`ファイルから、GPT-4 Turbo with Visionに関連する多くの情報が削除されました。これにより、ユーザーがこれまでの機能を利用するための詳細なガイドやコード例が失われています。

## その他の更新
1. **グローバルプロビジョンドデプロイメントタイプの統合説明**  
   Azure OpenAIのプロビジョンドデプロイメントとグローバルプロビジョンドデプロイメントの説明が統合され、リソースの管理や利用方法がより明確になりました。
   
2. **目次の更新**  
   目次に「Completions (legacy)」という項目が追加され、レガシー補完機能を明示的に示すようになりました。
   
3. **モデル情報の修正**   
   「GPT-4o mini」という新しいモデル名が追加され、全体のモデル情報が最新化されました。

# Insights
今回の変更内容は、Azure OpenAIサービスの情報の精度と明確性を向上させることを目的としています。また、新しい機能の追加により、開発者がより多様なツールを使用できるようになり、ユーザー体験が向上することが期待されます。

### GPT-4 Turbo with Visionに関する破壊的変更
GPT-4 Turbo with Visionに関する変更は、多くのユーザーにとって大きな衝撃を与える可能性があります。具体的には、Azure AI Visionを活用した補強機能やOCR機能、動画プロンプトに関する情報が削除されました。これにより、ユーザーはこれらの機能を利用するための詳細なガイドや具体的なコード例を参照できなくなります。この変更はドキュメントの簡潔さを追求したものの、技術的な詳細が不足する結果となるため、ユーザーにとっては混乱や利用の制約を引き起こす可能性があります。

### 新機能の追加
一方、新しいテキスト読み上げ機能や音声認識機能（Whisper）の追加は、開発者にとって非常に有益です。JavaScriptを使用してこれらの機能を簡単に統合できるようになったため、アプリケーションの開発がさらに効率化されます。特に音声認識機能は、ユーザーインターフェースの操作性を大幅に向上させる可能性があり、さまざまな応用が期待されます。

### グローバルプロビジョンドデプロイメントと目次の更新
また、グローバルプロビジョンドデプロイメントに関する説明の統合も重要なポイントです。ユーザーはこれにより、リソースの管理やデプロイメントの選択肢をより明確に理解することができます。目次の更新により、目次が整理され、レガシー補完機能が明示的に示されるようになったことで、ユーザビリティが向上しました。

まとめると、今回の更新は多岐にわたる内容であり、特に新機能の追加と既存機能

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [gpt-with-vision.md](#item-991388) | minor update | GPT-4 Turbo with Visionの機能削除 | modified | 0 | 36 | 36 | 
| [provisioned-migration.md](#item-68e143) | minor update | 予約サイズに関するリンクの修正 | modified | 1 | 1 | 2 | 
| [provisioned-throughput.md](#item-022e0c) | minor update | ProvisionedとGlobal Provisionedデプロイメントタイプの統合説明 | modified | 14 | 13 | 27 | 
| [completions.md](#item-79f39a) | minor update | レガシーコンプリーションAPIに関する情報の明確化 | modified | 3 | 3 | 6 | 
| [deployment-types.md](#item-210814) | minor update | デプロイメントタイプの詳細とグローバルプロビジョニングの追加 | modified | 22 | 15 | 37 | 
| [gpt-with-vision.md](#item-4d8502) | breaking change | GPT-4ターボとビジョンに関する文書の大幅な簡略化 | modified | 1 | 414 | 415 | 
| [provisioned-get-started.md](#item-c8df1c) | minor update | プロビジョニングされたデプロイメントの説明の改善 | modified | 13 | 13 | 26 | 
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | プロビジョニングおよびグローバルプロビジョニングに関する内容の調整 | modified | 10 | 11 | 21 | 
| [gpt-v-python.md](#item-366276) | breaking change | GPT-4 Turbo with Visionに関連する情報の削除 | modified | 0 | 91 | 91 | 
| [gpt-v-rest.md](#item-65c91c) | breaking change | GPT-4 Turbo with Visionに関する詳細情報の削除 | modified | 0 | 97 | 97 | 
| [gpt-v-studio.md](#item-dcd50e) | breaking change | GPT-4 Turbo with Visionに関連する詳細情報の削除 | modified | 0 | 61 | 61 | 
| [text-to-speech-javascript.md](#item-e9b653) | new feature | JavaScriptにおけるテキスト読み上げ機能の追加 | added | 247 | 0 | 247 | 
| [text-to-speech-rest.md](#item-d067a1) | minor update | テキスト音声化のREST APIの前提条件とセットアップ手順の追加 | modified | 59 | 1 | 60 | 
| [whisper-javascript.md](#item-3ee990) | new feature | JavaScriptにおける音声認識機能（Whisper）の追加 | added | 235 | 0 | 235 | 
| [whisper-powershell.md](#item-7db269) | minor update | Whisperモデル用PowerShellの前提条件とセットアップ手順の詳細化 | modified | 61 | 1 | 62 | 
| [whisper-python.md](#item-e61179) | minor update | Whisperモデル用Pythonの前提条件とセットアップ手順の詳細化 | modified | 67 | 4 | 71 | 
| [whisper-rest.md](#item-639ccb) | minor update | Whisperモデル用REST APIの前提条件とセットアップ手順の詳細化 | modified | 63 | 1 | 64 | 
| [index.yml](#item-0adb87) | minor update | Azure OpenAIサービスのモデル情報の修正 | modified | 3 | 3 | 6 | 
| [overview.md](#item-97d507) | minor update | Azure OpenAIサービスの言語モデル情報の補足 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-7d1656) | minor update | レガシー補完APIを使用したクイックスタートのタイトル変更 | modified | 3 | 3 | 6 | 
| [text-to-speech-quickstart.md](#item-c344ad) | minor update | テキスト読み上げクイックスタートの内容を更新 | modified | 8 | 53 | 61 | 
| [toc.yml](#item-c945af) | minor update | 目次の更新 - 補完機能のレガシー参照追加 | modified | 3 | 3 | 6 | 
| [whats-new.md](#item-53303b) | minor update | 新機能の追加 - GPT-4oおよびグローバル展開タイプ | modified | 10 | 0 | 10 | 
| [whisper-quickstart.md](#item-4cae3d) | minor update | Whisperモデルのクイックスタートガイド改良 | modified | 9 | 61 | 70 | 


# Modified Contents
## articles/ai-services/openai/concepts/gpt-with-vision.md{#item-991388}

<details>
<summary>Diff</summary>
````diff
@@ -20,31 +20,6 @@ To try out GPT-4 Turbo with Vision, see the [quickstart](/azure/ai-services/open
 
 The GPT-4 Turbo with Vision model answers general questions about what's present in the images or videos you upload.
 
-## Enhancements
-
-Enhancements let you incorporate other Azure AI services (such as Azure AI Vision) to add new functionality to the chat-with-vision experience.
-
-> [!IMPORTANT]
-> To use Vision enhancement, you need a Computer Vision resource. It must be in the paid (S1) tier and in the same Azure region as your GPT-4 Turbo with Vision resource.
-
-> [!IMPORTANT]
-> Vision enhancements are not supported by the GPT-4 Turbo GA model. They are only available with the preview models.
-
-**Object grounding**: Azure AI Vision complements GPT-4 Turbo with Vision’s text response by identifying and locating salient objects in the input images. This lets the chat model give more accurate and detailed responses about the contents of the image.
-
-:::image type="content" source="../media/concepts/gpt-v/object-grounding.png" alt-text="Screenshot of an image with object grounding applied. Objects have bounding boxes with labels.":::
-
-:::image type="content" source="../media/concepts/gpt-v/object-grounding-response.png" alt-text="Screenshot of a chat response to an image prompt about an outfit. The response is an itemized list of clothing items seen in the image.":::
-
-**Optical Character Recognition (OCR)**: Azure AI Vision complements GPT-4 Turbo with Vision by providing high-quality OCR results as supplementary information to the chat model. It allows the model to produce higher quality responses for images with dense text, transformed images, and numbers-heavy financial documents, and increases the variety of languages the model can recognize in text.
-
-:::image type="content" source="../media/concepts/gpt-v/receipts.png" alt-text="Photo of several receipts.":::
-
-:::image type="content" source="../media/concepts/gpt-v/ocr-response.png" alt-text="Screenshot of the JSON response of an OCR call.":::
-
-**Video prompt**: The **video prompt** enhancement lets you use video clips as input for AI chat, enabling the model to generate summaries and answers about video content. It uses Azure AI Vision Video Retrieval to sample a set of frames from a video and create a transcript of the speech in the video.
-
-> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RW1eHRf]
 
 ## Special pricing information
 
@@ -59,15 +34,6 @@ Base Pricing for GPT-4 Turbo with Vision is:
 
 See the [Tokens section of the overview](/azure/ai-services/openai/overview#tokens) for information on how text and images translate to tokens.
 
-If you turn on Enhancements, additional usage applies for using GPT-4 Turbo with Vision with Azure AI Vision functionality.
-
-| Model        | Price        |
-|-----------------|-----------------|
-| + Enhanced add-on features for OCR | $1.5 per 1000 transactions |
-| + Enhanced add-on features for Object Detection | $1.5 per 1000 transactions |
-| + Enhanced add-on feature for “Video Retrieval” integration **<sup>1</sup>** | Ingestion: $0.05 per minute of video <br>Transactions: $0.25 per 1000 queries of the Video Retrieval index |
-
-**<sup>1</sup>** Processing videos involves the use of extra tokens to identify key frames for analysis. The number of these additional tokens will be roughly equivalent to the sum of the tokens in the text input, plus 700 tokens.
 
 ### Example image price calculation
 > [!IMPORTANT]
@@ -108,9 +74,7 @@ This section describes the limitations of GPT-4 Turbo with Vision.
 
 ### Image support
 
-- **Limitation on image enhancements per chat session**: Enhancements cannot be applied to multiple images within a single chat call.
 - **Maximum input image size**: The maximum size for input images is restricted to 20 MB.
-- **Object grounding in enhancement API**: When the enhancement API is used for object grounding, and the model detects duplicates of an object, it will generate one bounding box and label for all the duplicates instead of separate ones for each.
 - **Low resolution accuracy**: When images are analyzed using the "low resolution" setting, it allows for faster responses and uses fewer input tokens for certain use cases. However, this could impact the accuracy of object and text recognition within the image.
 - **Image chat restriction**: When you upload images in Azure OpenAI Studio or the API, there is a limit of 10 images per chat call.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turbo with Visionの機能削除"
}
```

### Explanation
このコードの変更は、`gpt-with-vision.md`ファイルの36行が削除されたことに関するもので、GPT-4 TurboとVisionに関連する機能や要件についての情報が含まれています。具体的には、Azure AI Visionを活用した補強機能やOCR機能、動画プロンプトに関連する内容が大幅に削除されています。これにより、ドキュメントはより簡潔になり、GPT-4 Turbo with Visionの基本的な機能と料金情報が強調されています。また、画像のサポートや制限に関する項目も調整されています。この変更により、ユーザーに提供される情報が整理され、必要な詳細が明確にされていると考えられます。

## articles/ai-services/openai/concepts/provisioned-migration.md{#item-68e143}

<details>
<summary>Diff</summary>
````diff
@@ -79,7 +79,7 @@ We also recommend that customers using commitments now create their deployments
 See the following links for more information. The guidance for reservations and commitments is the same:
 
 * [Capacity Transparency](#self-service-migration)
-* [Sizing reservations](../how-to/provisioned-throughput-onboarding.md#important-sizing-azure-openai-provisioned-reservations)
+* [Sizing reservations](../how-to/provisioned-throughput-onboarding.md#important-sizing-azure-openai-provisioned--global-provisioned-reservations)
 
 ## New hourly reservation payment model
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "予約サイズに関するリンクの修正"
}
```

### Explanation
このコードの変更は、`provisioned-migration.md`ファイル内の予約サイズに関するリンクを修正したものです。元のリンクでは「Azure OpenAI Provisioned Reservations」に関する情報が示されていましたが、更新後は「Azure OpenAI Provisioned Global Reservations」に関する情報に変更されています。この修正により、ユーザーはより正確なリソースとガイダンスにアクセスできるようになり、予約に関連する情報の配信が改善されます。全体として、この変更はドキュメントの明確さと精度を向上させるものとなっています。

## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -17,23 +17,23 @@ recommendations: false
  
 The provisioned throughput capability allows you to specify the amount of throughput you require in a deployment. The service then allocates the necessary model processing capacity and ensures it's ready for you. Throughput is defined in terms of provisioned throughput units (PTU) which is a normalized way of representing the throughput for your deployment. Each model-version pair requires different amounts of PTU to deploy and provide different amounts of throughput per PTU. 
 
-## What does the provisioned deployment type provide?
+## What do the provisioned and global provisioned deployment types provide?
 
 - **Predictable performance:** stable max latency and throughput for uniform workloads. 
 - **Reserved processing capacity:** A deployment configures the amount of throughput. Once deployed, the throughput is available whether used or not.
 - **Cost savings:** High throughput workloads might provide cost savings vs token-based consumption.
 
-An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model. A deployment provides customer access to a model for inference and integrates more features like Content Moderation ([See content moderation documentation](content-filter.md)).
+An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model. A deployment provides customer access to a model for inference and integrates more features like Content Moderation ([See content moderation documentation](content-filter.md)). Global deployments are available in the same Azure OpenAI resources as non-global deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center with best availability for each request.
 
 ## What do you get?
 
 | Topic | Provisioned|
 |---|---|
 | What is it? | Provides guaranteed throughput at smaller increments than the existing provisioned offer. Deployments have a consistent max latency for a given model-version. |
 | Who is it for? | Customers who want guaranteed throughput with minimal latency variance. |
-| Quota | Provisioned-managed throughput Units for a given model. |
+| Quota | Provisioned Managed Throughput Unit or Global Provisioned Managed Throughput Unit assigned per region. Quota can be used across any available Azure OpenAI model.|
 | Latency | Max latency constrained from the model. Overall latency is a factor of call shape.  |
-| Utilization | Provisioned-managed Utilization measure provided in Azure Monitor. |
+| Utilization | Provisioned-managed Utilization V2 measure provided in Azure Monitor. |
 | Estimating size | Provided calculator in the studio & benchmarking script. |
 
 ## What models and regions are available for provisioned throughput?
@@ -47,9 +47,9 @@ An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model.
 
 ### Deployment types
 
-When creating a provisioned deployment in Azure OpenAI Studio, the deployment type on the Create Deployment dialog is Provisioned-Managed.
+When creating a provisioned deployment in Azure OpenAI Studio, the deployment type on the Create Deployment dialog is Provisioned-Managed. When creating a global provisioned managed deployment in Azure Open Studio, the deployment type on the Create Deployment dialog is Global Provisioned-Managed.
 
-When creating a provisioned deployment in Azure OpenAI via CLI or API, you need to set the `sku-name` to be Provisioned-Managed. The `sku-capacity` specifies the number of PTUs assigned to the deployment. 
+When creating a provisioned deployment in Azure OpenAI via CLI or API, you need to set the `sku-name` to be `ProvisionedManaged`. When creating a global provisioned deployment in Azure OpenAI via CLI or API, you need to set the `sku-name` to be `GlobalProvisionedManaged`. The `sku-capacity` specifies the number of PTUs assigned to the deployment. 
 
 ```azurecli
 az cognitiveservices account deployment create \
@@ -76,13 +76,13 @@ Unlike the Tokens Per Minute (TPM) quota used by other Azure OpenAI offerings, P
 
 :::image type="content" source="../media/provisioned/model-independent-quota.png" alt-text="Diagram of model independent quota with one pool of PTUs available to multiple Azure OpenAI models." lightbox="../media/provisioned/model-independent-quota.png":::
 
-The new quota shows up in Azure OpenAI Studio as a quota item named **Provisioned Managed Throughput Unit**. In the Studio Quota pane, expanding the quota item will show the deployments contributing to usage of the quota.
+For provisioned deployments, the new quota shows up in Azure OpenAI Studio as a quota item named **Provisioned Managed Throughput Unit**. For global provisioned managed deployments, the new quota shows up in the Azure OpenAI Studio as a quota item named **Global Provisioned Managed Throughput Unit**.  In the Studio Quota pane, expanding the quota item will show the deployments contributing to usage of each quota.
 
 :::image type="content" source="../media/provisioned/ptu-quota-page.png" alt-text="Screenshot of quota UI for Azure OpenAI provisioned." lightbox="../media/provisioned/ptu-quota-page.png":::
 
 #### Obtaining PTU Quota 
 
-PTU quota is available by default in many regions. If additional quota is required, customers can request additional quota via the Request Quota link to the right of the Provisioned Managed Throughput Unit quota item in Azure OpenAI Studio. The form allows the customer to request an increase in PTU quota for a specified region. The customer will receive an email at the included address once the request is approved, typically within two business days. 
+PTU quota is available by default in many regions. If additional quota is required, customers can request additional quota via the Request Quota link to the right of the Provisioned Managed Throughput Unit or Global Provisioned Managed Throughput Unit quota items in Azure OpenAI Studio. The form allows the customer to request an increase in the specified PTU quota for a given region. The customer will receive an email at the included address once the request is approved, typically within two business days. 
 
 #### Per-Model PTU Minimums 
 
@@ -123,13 +123,13 @@ A few high-level considerations:
 
 ### How utilization performance works
 
-Provisioned deployments provide you with an allocated amount of model processing capacity to run a given model.
+Provisioned and global provisioned deployments provide you with an allocated amount of model processing capacity to run a given model.
 
-In Provisioned-Managed deployments, when capacity is exceeded, the API will immediately return a 429 HTTP Status Error. This enables the user to make decisions on how to manage their traffic. Users can redirect requests to a separate deployment, to a standard pay-as-you-go instance, or leverage a retry strategy to manage a given request. The service will continue to return the 429 HTTP status code until the utilization drops below 100%.
+In Provisioned-Managed and Global Provisioned-Managed deployments, when capacity is exceeded, the API will immediately return a 429 HTTP Status Error. This enables the user to make decisions on how to manage their traffic. Users can redirect requests to a separate deployment, to a standard pay-as-you-go instance, or leverage a retry strategy to manage a given request. The service will continue to return the 429 HTTP status code until the utilization drops below 100%.
 
 ### How can I monitor capacity?
 
-The [Provisioned-Managed Utilization V2 metric](../how-to/monitoring.md#azure-openai-metrics) in Azure Monitor measures a given deployments utilization on 1-minute increments. Provisioned-Managed deployments are optimized to ensure that accepted calls are processed with a consistent model processing time (actual end-to-end latency is dependent on a call's characteristics).  
+The [Provisioned-Managed Utilization V2 metric](../how-to/monitoring.md#azure-openai-metrics) in Azure Monitor measures a given deployments utilization on 1-minute increments. Provisioned-Managed and Global Provisioned-Managed deployments are optimized to ensure that accepted calls are processed with a consistent model processing time (actual end-to-end latency is dependent on a call's characteristics).  
 
 #### What should  I do when I receive a 429 response?
 The 429 response isn't an error, but instead part of the design for telling users that a given deployment is fully utilized at a point in time. By providing a fast-fail response, you have control over how to handle these situations in a way that best fits your application requirements.
@@ -140,9 +140,10 @@ The  `retry-after-ms` and `retry-after` headers in the response tell you the tim
 
 #### How does the service decide when to send a 429?
 
-In the Provisioned-Managed offering, each request is evaluated individually according to its prompt size, expected generation size, and model to determine its expected utilization. This is in contrast to pay-as-you-go deployments, which have a [custom rate limiting behavior](../how-to/quota.md) based on the estimated traffic load. For pay-as-you-go deployments this can lead to HTTP 429 errors being generated prior to defined quota values being exceeded if traffic is not evenly distributed.
+In the Provisioned-Managed and Global Provisioned-Managed offerings, each request is evaluated individually according to its prompt size, expected generation size, and model to determine its expected utilization. This is in contrast to pay-as-you-go deployments, which have a [custom rate limiting behavior](../how-to/quota.md) based on the estimated traffic load. For pay-as-you-go deployments this can lead to HTTP 429 errors being generated prior to defined quota values being exceeded if traffic is not evenly distributed.
+
+For Provisioned-Managed and Global Provisioned-Managed, we use a variation of the leaky bucket algorithm to maintain utilization below 100% while allowing some burstiness in the traffic. The high-level logic is as follows:
 
-For Provisioned-Managed, we use a variation of the leaky bucket algorithm to maintain utilization below 100% while allowing some burstiness in the traffic. The high-level logic is as follows:
 1.	Each customer has a set amount of capacity they can utilize on a deployment
 2.	When a request is made:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ProvisionedとGlobal Provisionedデプロイメントタイプの統合説明"
}
```

### Explanation
このコードの変更は、`provisioned-throughput.md`ファイルにおけるProvisionedデプロイメントタイプに関する説明を更新し、新たにGlobal Provisionedデプロイメントタイプを統合したものです。具体的には、グローバルデプロイメントの利点やそれに伴う予約容量の管理が説明されており、デプロイメント作成時のSKU名の設定も更新されています。また、QuotaやUtilizationの説明においても、グローバルデプロイメントに対応する情報が追加されています。これにより、ユーザーは不均一なトラフィックの処理やサービス利用時のパフォーマンスについて、より明確な理解を得られるようになっています。全体として、ドキュメントは機能性と明確性が向上し、利用者にとっての利便性が増しています。

## articles/ai-services/openai/how-to/completions.md{#item-79f39a}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: 'How to generate text with Azure OpenAI Service'
+title: 'How to generate text with the legacy completions API'
 titleSuffix: Azure OpenAI
-description: Learn how to generate or manipulate text, including code by using a completion endpoint in Azure OpenAI Service.
+description: Learn how to generate or manipulate text, including code by using the legacy completion endpoint in Azure OpenAI Service.
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
@@ -13,7 +13,7 @@ recommendations: false
 
 ---
 
-# Learn how to generate or manipulate text
+# Learn how to generate or manipulate text using the legacy completions API
 
 Azure OpenAI Service provides a **completion endpoint** that can be used for a wide variety of tasks. The endpoint supplies a simple yet powerful text-in, text-out interface to any [Azure OpenAI model](../concepts/models.md). To trigger the completion, you input some text as a prompt. The model generates the completion and attempts to match your context or pattern. Suppose you provide the prompt "As Descartes said, I think, therefore" to the API. For this prompt, Azure OpenAI returns the completion endpoint " I am" with high probability.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レガシーコンプリーションAPIに関する情報の明確化"
}
```

### Explanation
このコードの変更は、`completions.md`ファイルにおいて、Azure OpenAI Serviceのテキスト生成に関連するコンテンツのタイトルと説明を更新したものです。具体的には、古いバージョンのコンプリーションAPIに焦点を当てるため、「How to generate text with Azure OpenAI Service」のタイトルが「How to generate text with the legacy completions API」に変更され、説明文も「legacy completion endpoint」への言及を含むように編集されています。この変更により、ユーザーは古いAPIを使用する方法に関する情報をより明確に理解できるようになります。全体として、ドキュメントはより正確で明瞭になり、対象となるAPIのバージョンとの差異が明示されることで、利用者にとっての利便性が向上しています。

## articles/ai-services/openai/how-to/deployment-types.md{#item-210814}

<details>
<summary>Diff</summary>
````diff
@@ -13,34 +13,34 @@ ms.author: mbullwin
 
 # Azure OpenAI deployment types
 
-Azure OpenAI provides customers with choices on the hosting structure that fits their business and usage patterns. The service offers two main types of deployment: **standard** and **provisioned**. Standard is offered with a global deployment option, routing traffic globally to provide higher throughput. All deployments can perform the exact same inference operations, however the billing, scale and performance are substantially different. As part of your solution design, you will need to make two key decisions:
+Azure OpenAI provides customers with choices on the hosting structure that fits their business and usage patterns. The service offers two main types of deployment: **standard** and **provisioned**. Standard is offered with a global deployment option, routing traffic globally to provide higher throughput. Provisioned is also offered with a global deployment option, allowing customers to purchase and deploy provisioned throughput units across Azure global infrastructure. All deployments can perform the exact same inference operations, however the billing, scale and performance are substantially different. As part of your solution design, you will need to make two key decisions:
 
 - **Data residency needs**: global vs. regional resources  
 - **Call volume**: standard vs. provisioned
 
 ## Global versus regional deployment types
 
-For standard deployments you have an option of two types of configurations within your resource – **global** or **regional**. Global standard is the recommended starting point. 
+For standard and provisioned deployments, you have an option of two types of configurations within your resource – **global** or **regional**. Global standard is the recommended starting point. 
 
-Global deployments leverage Azure's global infrastructure, dynamically route customer traffic to the data center with best availability for the customer’s inference requests. This means you will get the higest initial throughput limits and best model availability with Global while still providing our uptime SLA and low latency.For high voulmne workloads above the specified usage tiers, you may experience increased latency variation. For customers that require the lower latency variance at large workload usage, we recommend purchasing provisioned throughput.
+Global deployments leverage Azure's global infrastructure, dynamically route customer traffic to the data center with best availability for the customer’s inference requests. This means you will get the highest initial throughput limits and best model availability with Global while still providing our uptime SLA and low latency. For high volume workloads above the specified usage tiers on standard and global standard, you may experience increased latency variation. For customers that require the lower latency variance at large workload usage, we recommend purchasing provisioned throughput.
 
 Our global deployments will be the first location for all new models and features. Customers with very large throughput requirements should consider our provisioned deployment offering.
 
 ## Deployment types
 
 Azure OpenAI offers three types of deployments. These provide a varied level of capabilities that provide trade-offs on: throughput, SLAs, and price. Below is a summary of the options followed by a deeper description of each.
 
-| **Offering** | **Global-Batch** | **Global-Standard** | **Standard** | **Provisioned**  |
-|---|:---|:---|:---|:---|
-| **Best suited for**      | Offline scoring <br><br> Workloads that are not latency sensitive and can be completed in hours.<br><br> For use cases that do not have data processing residency requirements.| Recommended starting place for customers. <br><br>Global-Standard will have the higher default quota and larger number of models available than Standard. | For customers with data residency requirements. Optimized for low to medium volume. | Real-time scoring for large consistent volume. Includes the highest commitments and limits.|
-| **How it works**         | Offline processing via files |Traffic may be routed anywhere in the world | | |
-| **Getting started**      | [Global-Batch](./batch.md) | [Model deployment](./create-resource.md) | [Model deployment](./create-resource.md) | [Provisioned onboarding](./provisioned-throughput-onboarding.md) |
-| **Cost**                 | [Least expensive option](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> 50% less cost compared to Global Standard prices. Access to all new models with larger quota allocations.  | [Global deployment pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) |  [Regional pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) | May experience cost savings for consistent usage |
-| **What you get**         |[Significant discount compared to Global Standard](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) | Easy access to all new models with highest default pay-per-call limits.<br><br> Customers with high volume usage may see higher latency variability | Easy access with [SLA on availability](https://azure.microsoft.com/support/legal/sla/). Optimized for low to medium volume workloads with high burstiness. <br><br>Customers with high consistent volume may experience greater latency variability. | Regional access with very high & predictable throughput. Determine throughput per PTU using the provided [capacity calculator](./provisioned-throughput-onboarding.md#estimate-provisioned-throughput-and-cost) |
-| **What you don’t get**   |❌Real-time call performance <br><br>❌Data processing guarantee<br> <br> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/)  |❌Data processing guarantee<br> <br> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) | ❌High volume w/consistent low latency | ❌Pay-per-call flexibility |
-| **Per-call Latency**     | Not Applicable (file based async process) | Optimized for real-time calling & low to medium volume usage. Customers with high volume usage may see higher latency variability. Threshold set per model | Optimized for real-time calling & low to medium volume usage. Customers with high volume usage may see higher latency variability. Threshold set per model | Optimized for real-time. |
-| **Sku Name in code**     |  `GlobalBatch` |   `GlobalStandard`               | `Standard`   |      `ProvisionedManaged`       |
-| **Billing model**        |  Pay-per-token |Pay-per-token | Pay-per-token | Monthly Commitments |
+| **Offering** | **Global-Batch** | **Global-Standard**|  **Global-Provisioned**  | **Standard** | **Provisioned**  |
+|---|:---|:---| -------- |:---|:---|
+| **Best suited for**      | Offline scoring <br><br> Workloads that are not latency sensitive and can be completed in hours.<br><br> For use cases that do not have data processing residency requirements.|Recommended starting place for customers. <br><br>Global-Standard will have the higher default quota and larger number of models available than Standard. |Real-time scoring for large consistent volume. Includes the highest commitments and limits.                                                                                               For use cases that do not have data residency requirements.| For customers with data residency requirements. Optimized for low to medium volume. |Real-time scoring for large consistent volume. Includes the highest commitments and limits.                                                                                          For use cases with data residency requirements|
+| **How it works**         | Offline processing via files |Traffic may be routed anywhere in the world |Traffic may be routed anywhere in the world| | |
+| **Getting started**      | [Global-Batch](./batch.md) | [Model deployment](./create-resource.md) |[Provisioned onboarding](/azure/ai-services/openai/how-to/provisioned-throughput-onboarding)| [Model deployment](./create-resource.md) | [Provisioned onboarding](./provisioned-throughput-onboarding.md) |
+| **Cost**                 | [Least expensive option](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> 50% less cost compared to Global Standard prices. Access to all new models with larger quota allocations.  | [Global deployment pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) |May experience cost savings for consistent usage|  [Regional pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) |May experience cost savings for consistent usage |
+| **What you get**         |[Significant discount compared to Global Standard](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) | Easy access to all new models with highest default pay-per-call limits.<br><br> Customers with high volume usage may see higher latency variability |Access to high & predictable throughput across Azure global infrastructure. Determine throughput per PTU using the provided [capacity calculator](/azure/ai-services/openai/how-to/provisioned-throughput-onboarding). | Easy access with [SLA on availability](https://azure.microsoft.com/support/legal/sla/). Optimized for low to medium volume workloads with high burstiness. <br><br>Customers with high consistent volume may experience greater latency variability. | Regional access with very high & predictable throughput. Determine throughput per PTU using the provided [capacity calculator](./provisioned-throughput-onboarding.md#estimate-provisioned-throughput-and-cost) |
+| **What you don’t get**   |❌Real-time call performance <br><br>❌Data processing guarantee<br> <br> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/)  |❌Data processing guarantee<br> <br> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) |❌Pay-per-call flexibility <br> <br>❌Data processing guarantee<br> <br> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/)| ❌High volume w/consistent low latency | ❌Pay-per-call flexibility |
+| **Per-call Latency**     | Not Applicable (file based async process) | Optimized for real-time calling & low to medium volume usage. Customers with high volume usage may see higher latency variability. Threshold set per model |Optimized for real-time calling & high-volume usage. | Optimized for real-time calling & low to medium volume usage. Customers with high volume usage may see higher latency variability. Threshold set per model |Optimized for real-time calling & high-volume usage.|
+| **Sku Name in code**     |  `GlobalBatch` |   `GlobalStandard`               |`GlobalProvisionedManaged`| `Standard`   |      `ProvisionedManaged`       |
+| **Billing model**        |  Pay-per-token |Pay-per-token |Hourly billing with optional purchase of monthly or yearly reservations| Pay-per-token |Hourly billing with optional purchase of monthly or yearly reservations|
 
 ## Provisioned
 
@@ -61,6 +61,13 @@ Global deployments are available in the same Azure OpenAI resources as non-globa
 
 Customers with high consistent volume may experience greater latency variability. The threshold is set per model. See the [quotas page to learn more](./quota.md).  For applications that require the lower latency variance at large workload usage, we recommend purchasing provisioned throughput.
 
+## Global provisioned
+
+> [!IMPORTANT]
+> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/).
+
+Global deployments are available in the same Azure OpenAI resources as non-global deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center with best availability for each request. Global provisioned deployments provide reserved model processing capacity for high and predictable throughput using Azure global infrastructure.  
+
 ## Global batch
 
 > [!IMPORTANT]
@@ -88,7 +95,7 @@ Key use cases include:
 
 Azure Policy helps to enforce organizational standards and to assess compliance at-scale. Through its compliance dashboard, it provides an aggregated view to evaluate the overall state of the environment, with the ability to drill down to the per-resource, per-policy granularity. It also helps to bring your resources to compliance through bulk remediation for existing resources and automatic remediation for new resources. [Learn more about Azure Policy and specific built-in controls for AI services](/azure/ai-services/security-controls-policy).
 
-You can use the following policy to disable access to Azure OpenAI global standard deployments.
+You can use the following policy to disable access to Azure OpenAI global standard deployments. To disable access to Azure global provisioned or global batch deployments, replace `GlobalStandard` with `GlobalProvisionedManaged` or `GlobalBatch` for the intended sku name. 
 
 ```json
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントタイプの詳細とグローバルプロビジョニングの追加"
}
```

### Explanation
このコードの変更は、`deployment-types.md`ファイルにおけるAzure OpenAIのデプロイメントタイプに関する情報を更新し、特にグローバルプロビジョニングについて詳述したものです。変更の主な内容は、標準デプロイメントとプロビジョンドデプロイメントの両方にグローバルオプションがあることを明確にし、顧客がプロビジョンドスループットユニットをAzureのグローバルインフラストラクチャ全体で購入・デプロイできるようになったことを強調しています。また、複数のデプロイメントオプション（グローバルバッチ、グローバルスタンダード、スタンダード、プロビジョンド）が明確に区別され、それぞれに対する提案や必要事項が詳述されています。

さらに、デプロイメントの選択肢、特徴、利点について、より詳細な情報が表形式で追加され、特にビリングモデルやレイテンシーに関する比較も行われるようになりました。この変更により、ユーザーは自分のビジネスニーズに最も適したデプロイメントオプションを選択する際に、より明確な判断を行えるようになります。全体的に、ドキュメントがさらに充実し、ユーザーエクスペリエンスが向上する結果となっています。

## articles/ai-services/openai/how-to/gpt-with-vision.md{#item-4d8502}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ manager: nitinme
 
 GPT-4 Turbo with Vision is a large multimodal model (LMM) developed by OpenAI that can analyze images and provide textual responses to questions about them. It incorporates both natural language processing and visual understanding.
 
-The GPT-4 Turbo with Vision model answers general questions about what's present in images. You can also show it video if you use [Vision enhancement](#use-vision-enhancement-with-video).
+The GPT-4 Turbo with Vision model answers general questions about what's present in images.
 
 > [!TIP]
 > To use GPT-4 Turbo with Vision, you call the Chat Completion API on a GPT-4 Turbo with Vision model that you have deployed. If you're not familiar with the Chat Completion API, see the [GPT-4 Turbo & GPT-4 how-to guide](/azure/ai-services/openai/how-to/chatgpt?tabs=python&pivots=programming-language-chat-completions).
@@ -249,143 +249,7 @@ The _detail_ parameter in the model offers three choices: `low`, `high`, or `aut
 
 For details on how the image parameters impact tokens used and pricing please see - [What is OpenAI? Image Tokens with GPT-4 Turbo with Vision](../overview.md#image-tokens-gpt-4-turbo-with-vision-and-gpt-4o)
 
-## Use Vision enhancement with images
 
-GPT-4 Turbo with Vision provides exclusive access to Azure AI Services tailored enhancements. When combined with Azure AI Vision, it enhances your chat experience by providing the chat model with more detailed information about visible text in the image and the locations of objects.
-
-The **Optical character recognition (OCR)** integration allows the model to produce higher quality responses for dense text, transformed images, and number-heavy financial documents. It also covers a wider range of languages.
-
-The **object grounding** integration brings a new layer to data analysis and user interaction, as the feature can visually distinguish and highlight important elements in the images it processes.
-
-> [!IMPORTANT]
-> To use the Vision enhancement with an Azure OpenAI resource, you need to specify a Computer Vision resource. It must be in the paid (S1) tier and in the same Azure region as your GPT-4 Turbo with Vision resource. If you're using an Azure AI Services resource, you don't need an additional Computer Vision resource.
-
-> [!IMPORTANT]
-> Vision enhancements are not supported by the GPT-4 Turbo GA model. They are only available with the preview models.
-
-> [!CAUTION]
-> Azure AI enhancements for GPT-4 Turbo with Vision will be billed separately from the core functionalities. Each specific Azure AI enhancement for GPT-4 Turbo with Vision has its own distinct charges. For details, see the [special pricing information](../concepts/gpt-with-vision.md#special-pricing-information).
-
-#### [REST](#tab/rest)
-
-Send a POST request to `https://{RESOURCE_NAME}.openai.azure.com/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version=2024-02-15-preview` where 
-
-- RESOURCE_NAME is the name of your Azure OpenAI resource 
-- DEPLOYMENT_NAME is the name of your GPT-4 Turbo with Vision model deployment 
-
-**Required headers**: 
-- `Content-Type`: application/json 
-- `api-key`: {API_KEY} 
-
-**Body**: 
-
-The format is similar to that of the chat completions API for GPT-4, but the message content can be an array containing strings and images (either a valid HTTP or HTTPS URL to an image, or a base-64-encoded image).
-
-You must also include the `enhancements` and `dataSources` objects. `enhancements` represents the specific Vision enhancement features requested in the chat. It has a `grounding` and `ocr` property, which both have a boolean `enabled` property. Use these to request the OCR service and/or the object detection/grounding service. `dataSources` represents the Computer Vision resource data that's needed for Vision enhancement. It has a `type` property which should be `"AzureComputerVision"` and a `parameters` property. Set the `endpoint` and `key` to the endpoint URL and access key of your Computer Vision resource. 
-
-> [!IMPORTANT]
-> Remember to set a `"max_tokens"` value, or the return output will be cut off.
-
-
-```json
-{
-    "enhancements": {
-            "ocr": {
-              "enabled": true
-            },
-            "grounding": {
-              "enabled": true
-            }
-    },
-    "dataSources": [
-    {
-        "type": "AzureComputerVision",
-        "parameters": {
-            "endpoint": "<your_computer_vision_endpoint>",
-            "key": "<your_computer_vision_key>"
-        }
-    }],
-    "messages": [
-        {
-            "role": "system",
-            "content": "You are a helpful assistant."
-        },
-        {
-            "role": "user",
-            "content": [
-	            {
-	                "type": "text",
-	                "text": "Describe this picture:"
-	            },
-	            {
-	                "type": "image_url",
-	                "image_url": {
-                        "url":"<image URL>" 
-                    }
-                }
-           ] 
-        }
-    ],
-    "max_tokens": 100, 
-    "stream": false 
-} 
-```
-
-#### [Python](#tab/python)
-
-You call the same method as in the previous step, but include the new *extra_body* parameter. It contains the `enhancements` and `dataSources` fields. 
-
-`enhancements` represents the specific Vision enhancement features requested in the chat. It has a `grounding` and `ocr` field, which both have a boolean `enabled` property. Use these to request the OCR service and/or the object detection/grounding service. 
-
-`dataSources` represents the Computer Vision resource data that's needed for Vision enhancement. It has a `type` field which should be `"AzureComputerVision"` and a `parameters` field. Set the `endpoint` and `key` to the endpoint URL and access key of your Computer Vision resource. R
-
-> [!IMPORTANT]
-> Remember to set a `"max_tokens"` value, or the return output will be cut off.
-
-
-```python
-response = client.chat.completions.create(
-    model=deployment_name,
-    messages=[
-        { "role": "system", "content": "You are a helpful assistant." },
-        { "role": "user", "content": [  
-            { 
-                "type": "text", 
-                "text": "Describe this picture:" 
-            },
-            { 
-                "type": "image_url",
-                "image_url": {
-                    "url": "<image URL>"
-                }
-            }
-        ] } 
-    ],
-    extra_body={
-        "dataSources": [
-            {
-                "type": "AzureComputerVision",
-                "parameters": {
-                    "endpoint": "<your_computer_vision_endpoint>",
-                    "key": "<your_computer_vision_key>"
-                }
-            }],
-        "enhancements": {
-            "ocr": {
-                "enabled": True
-            },
-            "grounding": {
-                "enabled": True
-            }
-        }
-    },
-    max_tokens=2000
-)
-print(response)
-```
-
-
----
 
 ### Output
 
@@ -409,28 +273,6 @@ The chat responses you receive from the model should now include enhanced inform
             {
                 "role": "assistant",
                 "content": "The image shows a close-up of an individual with dark hair and what appears to be a short haircut. The person has visible ears and a bit of their neckline. The background is a neutral light color, providing a contrast to the dark hair."
-            },
-            "enhancements":
-            {
-                "grounding":
-                {
-                    "lines":
-                    [
-                        {
-                            "text": "The image shows a close-up of an individual with dark hair and what appears to be a short haircut. The person has visible ears and a bit of their neckline. The background is a neutral light color, providing a contrast to the dark hair.",
-                            "spans":
-                            [
-                                {
-                                    "text": "the person",
-                                    "length": 10,
-                                    "offset": 99,
-                                    "polygon": [{"x":0.11950000375509262,"y":0.4124999940395355},{"x":0.8034999370574951,"y":0.4124999940395355},{"x":0.8034999370574951,"y":0.6434999704360962},{"x":0.11950000375509262,"y":0.6434999704360962}]
-                                }
-                            ]
-                        }
-                    ],
-                    "status": "Success"
-                }
             }
         }
     ],
@@ -448,61 +290,7 @@ Every response includes a `"finish_reason"` field. It has the following possible
 - `length`: Incomplete model output due to the `max_tokens` input parameter or model's token limit.
 - `content_filter`: Omitted content due to a flag from our content filters.
 
-## Use Vision enhancement with video
-
-GPT-4 Turbo with Vision provides exclusive access to Azure AI Services tailored enhancements. The **video prompt** integration uses Azure AI Vision video retrieval to sample a set of frames from a video and create a transcript of the speech in the video. It enables the AI model to give summaries and answers about video content.
-
-Follow these steps to set up a video retrieval system and integrate it with your AI chat model.
-
-> [!IMPORTANT]
-> To use the Vision enhancement with an Azure OpenAI resource, you need to specify a Computer Vision resource. It must be in the paid (S1) tier and in the same Azure region as your GPT-4 Turbo with Vision resource. If you're using an Azure AI Services resource, you don't need an additional Computer Vision resource.
-
-> [!IMPORTANT]
-> Vision enhancements are not supported by the GPT-4 Turbo GA model. They are only available with the preview models.
-
-> [!CAUTION]
-> Azure AI enhancements for GPT-4 Turbo with Vision will be billed separately from the core functionalities. Each specific Azure AI enhancement for GPT-4 Turbo with Vision has its own distinct charges. For details, see the [special pricing information](../concepts/gpt-with-vision.md#special-pricing-information).
-
-> [!TIP]
-> If you prefer, you can carry out the below steps using a Jupyter notebook instead: [Video chat completions notebook](https://github.com/Azure-Samples/azureai-samples/blob/main/scenarios/GPT-4V/video/video_chatcompletions_example_restapi.ipynb). 
-
-### Upload videos to Azure Blob Storage
-
-You need to upload your videos to an Azure Blob Storage container. [Create a new storage account](https://ms.portal.azure.com/#create/Microsoft.StorageAccount) if you don't have one already.
 
-Once your videos are uploaded, you can get their SAS URLs, which you use to access them in later steps.
-
-#### Ensure proper read access
-
-Depending on your authentication method, you may need to do some extra steps to grant access to the Azure Blob Storage container. If you're using an Azure AI Services resource instead of an Azure OpenAI resource, you need to use Managed Identities to grant it **read** access to Azure Blob Storage:
-
-#### [using System assigned identities](#tab/system-assigned)
-
-Enable System assigned identities on your Azure AI Services resource by following these steps:
-1. From your AI Services resource in Azure portal select **Resource Management** -> **Identity** and toggle the status to **ON**.
-1. Assign **Storage Blob Data Read** access to the AI Services resource: From the **Identity** page, select **Azure role assignments**, and then **Add role assignment** with the following settings:
-    - scope: storage
-    - subscription: {your subscription}
-    - Resource: {select the Azure Blob Storage resource}
-    - Role: Storage Blob Data Reader
-1. Save your settings.
-
-#### [using User assigned identities](#tab/user-assigned)
-
-To use a User assigned identity on your Azure AI Services resource, follow these steps:
-1. Create a new Managed Identity resource in the Azure portal.
-1. Navigate to the new resource, then to **Azure Role Assignments**.
-1. Add a **New Role Assignment** with the following settings:
-    - scope: storage
-    - subscription: {your subscription}
-    - Resource: {select the Azure Blob Storage resource}
-    - Role: Storage Blob Data Reader
-1. Save your new configuration.
-1. Navigate to your AI Services resource's **Identity** page.
-1. Select the **User Assigned** Tab, then click **+Add** to select the newly created Managed Identity.
-1. Save your configuration.
-
----
 
 ### Create a video retrieval index
 
@@ -579,207 +367,6 @@ To use a User assigned identity on your Azure AI Services resource, follow these
     curl.exe -v -X GET "https://<YOUR_ENDPOINT_URL>/computervision/retrieval/indexes/my-video-index/ingestions?api-version=2023-05-01-preview&$top=20" -H "ocp-apim-subscription-key: <YOUR_SUBSCRIPTION_KEY>"
     ```
 
-### Integrate your video index with GPT-4 Turbo with Vision
-
-#### [REST](#tab/rest)
-
-1. Prepare a POST request to `https://{RESOURCE_NAME}.openai.azure.com/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version=2024-02-15-preview` where 
-
-    - RESOURCE_NAME is the name of your Azure OpenAI resource 
-    - DEPLOYMENT_NAME is the name of your GPT-4 Vision model deployment 
-        
-    **Required headers**: 
-    - `Content-Type`: application/json 
-    - `api-key`: {API_KEY} 
-1. Add the following JSON structure in the request body:
-    ```json
-    {
-        "enhancements": {
-                "video": {
-                  "enabled": true
-                }
-        },
-        "dataSources": [
-        {
-            "type": "AzureComputerVisionVideoIndex",
-            "parameters": {
-                "computerVisionBaseUrl": "<your_computer_vision_endpoint>",
-                "computerVisionApiKey": "<your_computer_vision_key>",
-                "indexName": "<name_of_your_index>",
-                "videoUrls": ["<your_video_SAS_URL>"]
-            }
-        }],
-        "messages": [ 
-            {
-                "role": "system", 
-                "content": "You are a helpful assistant." 
-            },
-            {
-                "role": "user",
-                "content": [
-                        {
-                            "type": "acv_document_id",
-                            "acv_document_id": "<your_video_ID>"
-                        },
-                        {
-                            "type": "text",
-                            "text": "Describe this video:"
-                        }
-                    ]
-            }
-        ],
-        "max_tokens": 100, 
-    } 
-    ```
-
-    The request includes the `enhancements` and `dataSources` objects. `enhancements` represents the specific Vision enhancement features requested in the chat. `dataSources` represents the Computer Vision resource data that's needed for Vision enhancement. It has a `type` property which should be `"AzureComputerVisionVideoIndex"` and a `parameters` property which contains your AI Vision and video information.
-1. Fill in all the `<placeholder>` fields above with your own information: enter the endpoint URLs and keys of your OpenAI and AI Vision resources where appropriate, and retrieve the video index information from the earlier step.
-1. Send the POST request to the API endpoint. It should contain your OpenAI and AI Vision credentials, the name of your video index, and the ID and SAS URL of a single video.
-
-#### [Python](#tab/python)
-
-In your Python script, call the client's **create** method as in the previous sections, but include the *extra_body* parameter. Here, it contains the `enhancements` and `data_sources` fields. `enhancements` represents the specific Vision enhancement features requested in the chat. It has a `video` field, which has a boolean `enabled` property. Use this to request the video retrieval service. 
-
-`data_sources` represents the external resource data that's needed for Vision enhancement. It has a `type` field which should be `"AzureComputerVisionVideoIndex"` and a `parameters` field. 
-
-Set the `computerVisionBaseUrl` and `computerVisionApiKey` to the endpoint URL and access key of your Computer Vision resource. Set `indexName` to the name of your video index. Set `videoUrls` to a list of SAS URLs of your videos. 
-
-> [!IMPORTANT]
-> Remember to set a `"max_tokens"` value, or the return output will be cut off.
-
-```python
-response = client.chat.completions.create(
-    model=deployment_name,
-    messages=[
-        { "role": "system", "content": "You are a helpful assistant." },
-        { "role": "user", "content": [  
-            {
-                "type": "acv_document_id",
-                "acv_document_id": "<your_video_ID>"
-            },
-            { 
-                "type": "text", 
-                "text": "Describe this video:" 
-            }
-        ] } 
-    ],
-    extra_body={
-        "data_sources": [
-            {
-                "type": "AzureComputerVisionVideoIndex",
-                "parameters": {
-                    "computerVisionBaseUrl": "<your_computer_vision_endpoint>", # your endpoint should look like the following https://YOUR_RESOURCE_NAME.cognitiveservices.azure.com/computervision
-                    "computerVisionApiKey": "<your_computer_vision_key>",
-                    "indexName": "<name_of_your_index>",
-                    "videoUrls": ["<your_video_SAS_URL>"]
-                }
-            }],
-        "enhancements": {
-            "video": {
-                "enabled": True
-            }
-        }
-    },
-    max_tokens=100
-)
-
-print(response)
-```
----
-
-> [!IMPORTANT]
-> The `"data_sources"` object's content varies depending on which Azure resource type and authentication method you're using. See the following reference:
-> 
-> #### [Azure OpenAI resource](#tab/resource)
-> 
-> ```json
-> "data_sources": [
-> {
->     "type": "AzureComputerVisionVideoIndex",
->     "parameters": {
->     "endpoint": "<your_computer_vision_endpoint>",
->     "computerVisionApiKey": "<your_computer_vision_key>",
->     "indexName": "<name_of_your_index>",
->     "videoUrls": ["<your_video_SAS_URL>"]
->     }
-> }],
-> ```
-> 
-> #### [Azure AIServices resource + SAS authentication](#tab/resource-sas)
-> 
-> ```json
-> "data_sources": [
-> {
->     "type": "AzureComputerVisionVideoIndex",
->     "parameters": {
->     "indexName": "<name_of_your_index>",
->     "videoUrls": ["<your_video_SAS_URL>"]
->     }
-> }],
-> ```	
-> 
-> #### [Azure AIServices resource + Managed Identities](#tab/resource-mi)
-> 
-> ```json
-> "data_sources": [
-> {
->     "type": "AzureComputerVisionVideoIndex",
->     "parameters": {
->         "indexName": "<name_of_your_index>",
->         "documentAuthenticationKind": "managedidentity",
->     }
-> }],
-> ```	
-> ---
-
-### Output
-
-The chat responses you receive from the model should include information about the video. The API response should look like the following.
-
-```json
-{
-    "id": "chatcmpl-8V4J2cFo7TWO7rIfs47XuDzTKvbct",
-    "object": "chat.completion",
-    "created": 1702415412,
-    "model": "gpt-4",
-    "choices":
-    [
-        {
-            "finish_reason":"stop",
-            "index": 0,
-            "message":
-            {
-                "role": "assistant",
-                "content": "The advertisement video opens with a blurred background that suggests a serene and aesthetically pleasing environment, possibly a workspace with a nature view. As the video progresses, a series of frames showcase a digital interface with search bars and prompts like \"Inspire new ideas,\" \"Research a topic,\" and \"Organize my plans,\" suggesting features of a software or application designed to assist with productivity and creativity.\n\nThe color palette is soft and varied, featuring pastel blues, pinks, and purples, creating a calm and inviting atmosphere. The backgrounds of some frames are adorned with abstract, organically shaped elements and animations, adding to the sense of innovation and modernity.\n\nMidway through the video, the focus shifts to what appears to be a browser or software interface with the phrase \"Screens simulated, subject to change; feature availability and timing may vary,\" indicating the product is in development and that the visuals are illustrative of its capabilities.\n\nThe use of text prompts continues with \"Help me relax,\" followed by a demonstration of a 'dark mode' feature, providing a glimpse into the software's versatility and user-friendly design.\n\nThe video concludes by revealing the product name, \"Copilot,\" and positioning it as \"Your everyday AI companion,\" implying the use of artificial intelligence to enhance daily tasks. The final frames feature the Microsoft logo, associating the product with the well-known technology company.\n\nIn summary, the advertisement video is for a Microsoft product named \"Copilot,\" which seems to be an AI-powered software tool aimed at improving productivity, creativity, and organization for its users. The video conveys a message of innovation, ease, and support in daily digital interactions through a visually appealing and calming presentation."
-            }
-        }
-    ],
-    "usage":
-    {
-        "prompt_tokens": 2068,
-        "completion_tokens": 341,
-        "total_tokens": 2409
-    }
-}
-```
-
-Every response includes a `"finish_reason"` field. It has the following possible values:
-- `stop`: API returned complete model output.
-- `length`: Incomplete model output due to the `max_tokens` input parameter or model's token limit.
-- `content_filter`: Omitted content due to a flag from our content filters.
-
-### Pricing example for Video prompts
-The pricing for GPT-4 Turbo with Vision is dynamic and depends on the specific features and inputs used. For a comprehensive view of Azure OpenAI pricing see [Azure OpenAI Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/).
-
-The base charges and additional features are outlined below:
-
-Base Pricing for GPT-4 Turbo with Vision is:
-- Input: $0.01 per 1000 tokens
-- Output: $0.03 per 1000 tokens
-  
-Video prompt integration with Video Retrieval Add-on:
-- Ingestion: $0.05 per minute of video
-- Transactions: $0.25 per 1000 queries of the Video Retrieval
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "GPT-4ターボとビジョンに関する文書の大幅な簡略化"
}
```

### Explanation
このコードの変更は、`gpt-with-vision.md`ファイルにおけるGPT-4 Turbo with Visionに関するドキュメントを大幅に簡略化したものです。具体的には、内容のうち約414行が削除され、関連する情報が1行だけ追加されました。これにより、以前に存在した詳細な説明や手順、ビデオおよび画像のビジョン強化機能に関する情報がすべて取り除かれました。

削除された内容には、ビジョン強化機能の利用方法、具体的なAPIリクエストの説明、PythonおよびREST APIによる実装方法、入力や出力に対する価格情報などが含まれていました。この変更によって、ユーザーは基本的な利用方法を知ることはできますが、より詳細な操作ガイドや高度な機能にアクセスするためには別のリソースを参照する必要があります。全体として、ドキュメントは簡潔になりましたが、特定の技術的な詳細が失われたため、ユーザーに対しては利用上の制約が生じる可能性があります。

## articles/ai-services/openai/how-to/provisioned-get-started.md{#item-c8df1c}

<details>
<summary>Diff</summary>
````diff
@@ -37,40 +37,40 @@ Creating a new deployment requires available (unused) quota to cover the desired
 
 Then 200 PTUs of quota are considered used, and there are 300 PTUs available for use to create new deployments. 
 
-A default amount of PTU quota is assigned to all subscriptions in several regions. You can view the quota available to you in a region by visiting the Quotas blade in Azure OpenAI Studio and selecting the desired subscription and region. For example, the screenshot below shows a quota limit of 500 PTUs in West US for the selected subscription. Note that you might see lower values of available default quotas. 
- 
+A default amount of provisioned and global provisioned quota is assigned to all subscriptions in several regions. You can view the quota available to you in a region by visiting the Quotas blade in Azure OpenAI Studio and selecting the desired subscription and region. For example, the screenshot below shows a quota limit of 500 PTUs in West US for the selected subscription. Note that you might see lower values of available default quotas. 
+
 :::image type="content" source="../media/provisioned/available-quota.png" alt-text="A screenshot of the available quota in Azure OpenAI studio." lightbox="../media/provisioned/available-quota.png":::
 
 Additional quota can be requested by clicking the Request Quota link to the right of the “Usage/Limit” column.  (This is off-screen in the screenshot above). 
 
 ## Create an Azure OpenAI resource 
 
-Provisioned Throughput deployments are created via Azure OpenAI resource objects within Azure. You must have an Azure OpenAI resource in each region where you intend to create a deployment. Use the Azure portal to [create a resource](./create-resource.md) in a region with available quota, if required.  
+Provisioned and global provisioned deployments are created via Azure OpenAI resource objects within Azure. You must have an Azure OpenAI resource in each region where you intend to create a deployment. Use the Azure portal to [create a resource](./create-resource.md) in a region with available quota, if required.  
 
 > [!NOTE]
-> Azure OpenAI resources can support multiple types of Azure OpenAI deployments at the same time.  It is not necessary to dedicate new resources for your provisioned deployments. 
-
-## Create your provisioned deployment - capacity is available
+> Azure OpenAI resources can support multiple types of Azure OpenAI deployments at the same time.  It is not necessary to dedicate new resources for your provisioned or global provisioned deployments. 
+## Create your provisioned or global provisioned deployment - capacity is available
 
-After you purchase a commitment on your quota, you can create a deployment. To create a provisioned deployment, you can follow these steps; the choices described reflect the entries shown in the screenshot. 
+once you have verified your quota, you can create a deployment. To create a provisioned deployment, you can follow these steps; the choices described reflect the entries shown in the screenshot. 
 
 :::image type="content" source="../media/provisioned/deployment-screen.png" alt-text="Screenshot of the Azure OpenAI Studio deployment page for a provisioned deployment." lightbox="../media/provisioned/deployment-screen.png":::
 
 
 
 1.	Sign into the [Azure OpenAI Studio](https://oai.azure.com)
-2.	Choose the subscription that was enabled for provisioned deployments & select the desired resource in a region where you have the quota.
+1. Choose the subscription that was enabled for provisioned and global provisioned deployments & select the desired resource in a region where you have the quota.
+
 3.	Under **Management** in the left-nav select **Deployments**.
 4.	Select Create new deployment and configure the following fields. Expand the **advanced options** drop-down menu.
 5.	Fill out the values in each field. Here's an example:
 
 | Field | Description |	Example |
-|--|--|--| 
+|--|--|--|
 | Select a model|	Choose the specific model you wish to deploy.	| GPT-4 |
 | Model version |	Choose the version of the model to deploy.	 | 0613 |
 | Deployment Name	 | The deployment name is used in your code to call the model by using the client libraries and the REST APIs.	| gpt-4|
 | Content filter	| Specify the filtering policy to apply to the deployment. Learn more on our [Content Filtering](../concepts/content-filter.md) how-to. | 	Default |
-| Deployment Type	|This impacts the throughput and performance. Choose Provisioned-Managed for your provisioned deployment 	| Provisioned-Managed |
+| Deployment Type	|This impacts the throughput and performance. Choose Provisioned-Managed or Global Provisioned-Managed for your deployment 	| Provisioned-Managed |
 | Provisioned Throughput Units |	Choose the amount of throughput you wish to include in the deployment. |	100 |
 
 Important things to note: 
@@ -87,7 +87,7 @@ The image below shows the pricing confirmation you will see. The price shown is
 
 :::image type="content" source="../media/provisioned/confirm-pricing.png" alt-text="Screenshot showing the pricing confirmation screen." lightbox="../media/provisioned/confirm-pricing.png":::
 
-If you wish to create your deployment programmatically, you can do so with the following Azure CLI command. Update the `sku-capacity` with the desired number of provisioned throughput units.
+If you wish to create your deployment programmatically, you can do so with the following Azure CLI command. To specify the deployment type, modify the `sku-name` to `ProvisionedManaged` or `GlobalProvisionedManaged` based on the intended deployment type. Update the `sku-capacity` with the desired number of provisioned throughput units.
 
 ```cli
 az cognitiveservices account deployment create \
@@ -101,9 +101,9 @@ az cognitiveservices account deployment create \
 --sku-name ProvisionedManaged
 ```
 
-REST, ARM template, Bicep, and Terraform can also be used to create deployments. See the section on automating deployments in the [Managing Quota](quota.md?tabs=rest#automate-deployment) how-to guide and replace the `sku.name` with "ProvisionedManaged" rather than "Standard."
+REST, ARM template, Bicep, and Terraform can also be used to create deployments. See the section on automating deployments in the [Managing Quota](quota.md?tabs=rest#automate-deployment) how-to guide and replace the `sku.name` with "ProvisionedManaged" or "GlobalProvisionedManaged" rather than "Standard."
 
-## Create your provisioned deployment – Capacity is not available 
+## Create your provisioned or global provisioned deployment – Capacity is not available
 
 Due to the dynamic nature of capacity availability, it is possible that the region of your selected resource might not have the service capacity to create the deployment of the specified model, version, and number of PTUs. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされたデプロイメントの説明の改善"
}
```

### Explanation
このコードの変更は、`provisioned-get-started.md`ファイルにおけるプロビジョンドデプロイメントに関する説明を改善したものです。変更された内容では、プロビジョンドデプロイメントとグローバルプロビジョンドデプロイメントに関する情報が強調され、両方のデプロイメントタイプが統一的に扱われるようになりました。具体的には、以下の点が修正されました。

1. プロビジョンドデプロイメントに関するデフォルトのPTU（Provisioned Throughput Units）クォータに加え、グローバルプロビジョンドデプロイメントのクォータについても言及されるようになりました。
2. リソース作成やデプロイメントの際に必要なクォータの確認方法が明確化され、どちらのデプロイメントタイプを選択するかを明示するようになりました。
3. コマンドラインインターフェース（CLI）や自動化ツールを使用してデプロイメントを作成する際に、新たに「GlobalProvisionedManaged」タイプの指定ができるように詳細が追加されました。

これらの変更により、ユーザーはプロビジョンドデプロイメントとグローバルプロビジョンドデプロイメントの違いをより理解しやすくなり、リソースの管理やデプロイメントの作成時に必要な情報を簡単に把握できるようになります。全体として、ドキュメントがより包括的で理解しやすくなり、ユーザーの体験が向上しています。

## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -27,7 +27,7 @@ You should consider switching from pay-as-you-go to provisioned throughput when
 > [!NOTE]
 > In function calling and agent use cases, token usage can be variable. You should understand your expected Tokens Per Minute (TPM) usage in detail prior to migrating workloads to PTU.
 
-## Sizing and estimation: provisioned managed only
+## Sizing and estimation: provisioned and global provisioned
 
 Determining the right amount of provisioned throughput, or PTUs, you require for your workload is an essential step to optimizing performance and cost. This section describes how to use the Azure OpenAI capacity planning tool. The tool provides you with an estimate of the required PTU to meet the needs of your workload.
 
@@ -56,38 +56,37 @@ The values in the output column are the estimated value of PTU units required fo
 
 ## Understanding the Provisioned Throughput Purchase Model 
 
-Azure OpenAI Provisioned is purchased on-demand at an hourly basis based on the number of deployed PTUs, with substantial term discount available via the purchase of Azure Reservations.   
+Azure OpenAI Provisioned and Global Provisiones are purchased on-demand at an hourly basis based on the number of deployed PTUs, with substantial term discount available via the purchase of Azure Reservations.   
 
-The hourly model is useful for short-term deployment needs, such as validating new models or acquiring capacity for a hackathon.  However, the discounts provided by the Azure Reservation for Azure OpenAI Provisioned are considerable and most customers with consistent long-term usage will find a reserved model to be a better value proposition. 
+The hourly model is useful for short-term deployment needs, such as validating new models or acquiring capacity for a hackathon.  However, the discounts provided by the Azure Reservation for Azure OpenAI Provisioned and Global Provisioned are considerable and most customers with consistent long-term usage will find a reserved model to be a better value proposition. 
 
 > [!NOTE]
 > Azure OpenAI Provisioned customers onboarded prior to the August self-service update use a purchase model called the Commitment model.  These customers can continue to use this older purchase model alongside the Hourly/reservation purchase model.  The Commitment model is not available for new customers.  For details on the Commitment purchase model and options for coexistence and migration, please see the [Azure OpenAI Provisioned August Update](../concepts/provisioned-migration.md).
-
 ## Hourly Usage  
 
-Provisioned Throughput deployments are charged an hourly rate ($/PTU/hr) on the number of PTUs that have been deployed.  For example, a 300 PTU deployment will be charged the hourly rate times 300.  All Azure OpenAI pricing is available in the Azure Pricing Calculator. 
+Provisioned and Global Provisioned deployments are charged an hourly rate ($/PTU/hr) on the number of PTUs that have been deployed.  For example, a 300 PTU deployment will be charged the hourly rate times 300.  All Azure OpenAI pricing is available in the Azure Pricing Calculator. 
 
 If a deployment exists for a partial hour, it will receive a prorated charge based on the number of minutes it was deployed during the hour.  For example, a deployment that exists for 15 minutes during an hour will receive 1/4th the hourly charge.  
 
 If the deployment size is changed, the costs of the deployment will adjust to match the new number of PTUs.   
 
 :::image type="content" source="../media/provisioned/hourly-billing.png" alt-text="A diagram showing hourly billing." lightbox="../media/provisioned/hourly-billing.png":::
 
-Paying for provisioned deployments on an hourly basis is ideal for short-term deployment scenarios.  For example: Quality and performance benchmarking of new models, or temporarily increasing PTU capacity to cover an event such as a hackathon.  
+Paying for provisioned and global provisioned deployments on an hourly basis is ideal for short-term deployment scenarios.  For example: Quality and performance benchmarking of new models, or temporarily increasing PTU capacity to cover an event such as a hackathon.  
 
-Customers that require long-term usage of provisioned deployments, however, might pay significantly less per month by purchasing a term discount via an Azure Reservation as discussed in the next section. 
+Customers that require long-term usage of provisioned and global provisioned deployments, however, might pay significantly less per month by purchasing a term discount via an Azure Reservation as discussed in the next section. 
 
 > [!NOTE]
 > It is not recommended to scale production deployments according to incoming traffic and pay for them purely on an hourly basis. There are two reasons for this:
 > * The cost savings achieved by purchasing an Azure Reservation for Azure OpenAI Provisioned are significant, and it will be less expensive in many cases to maintain a deployment sized for full production volume paid for via a reservation than it would be to scale the deployment with incoming traffic.
 > * Having unused provisioned quota (PTUs) does not guarentee that capacity will be available to support increasing the size of the deployment when required. Quota limits the maximum number of PTUs that can be deployed, but it is not a capacity guarantee. Provisioned capacity for each region and modal dynamically changes throughout the day and might not be available when required. As a result, it is recommended to maintain a permanant deployment to cover your traffic needs (paid for via a reservation).
 > * Charges for deployments on a deleted resource will continue until the resource is purged.  To prevent this, delete a resource’s deployment before deleting the resource.  For more information, see [Recover or purge deleted Azure AI services resources](../../recover-purge-resources.md). 
 
-## Azure Reservations for Azure OpenAI Provisioned   
+## Azure Reservations for Azure OpenAI Provisioned and Global Provisioned
 
-Discounts on top of the hourly usage price can be obtained by purchasing an Azure Reservation for Azure OpenAI Provisioned. An Azure Reservation is a term-discounting mechanism shared by many Azure products. For example, Compute and Cosmos DB. For Azure OpenAI Provisioned, the reservation provides a discount for committing to payment for fixed number of PTUs for a one-month or one-year period.  
+Discounts on top of the hourly usage price can be obtained by purchasing an Azure Reservation for Azure OpenAI Provisioned and Global Provisioned. An Azure Reservation is a term-discounting mechanism shared by many Azure products. For example, Compute and Cosmos DB. For Azure OpenAI Provisioned and Global Provisioned, the reservation provides a discount for committing to payment for fixed number of PTUs for a one-month or one-year period.  
 
-* Azure Reservations are purchased via the Azure portal, not Azure OpenAI Studio  Link to Azure reservation portal. 
+* Azure Reservations are purchased via the Azure portal, not Azure OpenAI Studio Link to Azure reservation portal. 
 
 * Reservations are purchased regionally and can be flexibly scoped to cover usage from a group of deployments. Reservation scopes include: 
 
@@ -110,7 +109,7 @@ Discounts on top of the hourly usage price can be obtained by purchasing an Azur
 >
 > * The Azure role and tenant policy requirements to purchase a reservation are different than those required to create a deployment or Azure OpenAI resource.  Verify authorization to purchase reservations in advance of needing to do so. See Azure OpenAI [Provisioned reservation documentation](https://aka.ms/oai/docs/ptum-reservations) for more details.
 
-## Important: Sizing Azure OpenAI Provisioned Reservations 
+## Important: Sizing Azure OpenAI Provisioned & Global Provisioned Reservations
 
 The PTU amounts in reservation purchases are independent of PTUs allocated in quota or used in deployments. It is possible to purchase a reservation for more PTUs than you have in quota, or can deploy for the desired region, model, or version.   Credits for over-purchasing a reservation are limited, and customers must take steps to ensure they maintain their reservation sizes in line with their deployed PTUs.  
  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングおよびグローバルプロビジョニングに関する内容の調整"
}
```

### Explanation
このコードの変更は、`provisioned-throughput-onboarding.md`ファイルにおけるプロビジョニングおよびグローバルプロビジョニングに関する説明を調整したものです。変更された内容では、プロビジョンドデプロイメントに加えてグローバルプロビジョンドデプロイメントが明示され、ドキュメント内のいくつかのセクションが更新されました。

1. **セクションタイトルの更新**: 「Sizing and estimation」というセクションタイトルが「provisioned managed only」から「provisioned and global provisioned」に変更され、両方のデプロイメントタイプに焦点が当てられました。

2. **購入モデルの明確化**: プロビジョンドおよびグローバルプロビジョンドのデプロイメントが、デプロイされたPTUの数に基づいてオンデマンドで購入されることが明記され、料金モデルについての理解が促進されました。

3. **利用料金に関する情報の統一**: プロビジョンドデプロイメントとグローバルプロビジョンドデプロイメントの両方が、同様の料金体系で課金されることが強調されました。

4. **Azure Reservationsの言及の拡大**: Azure Reservationsに関連する情報は、プロビジョンドとグローバルプロビジョンドの両方に適用されることが強調され、予約時の割引を受ける際の条件についても更新されました。

この変更により、ユーザーはプロビジョンドおよびグローバルプロビジョンドのデプロイメントについてより明確な理解を持てるようになり、料金体系や予約の利用方法についての情報が一貫性を持つようになりました。全体として、ドキュメントの内容が整理され、ユーザーの利便性が向上しています。

## articles/ai-services/openai/includes/gpt-v-python.md{#item-366276}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,6 @@ Use this article to get started using the Azure OpenAI Python SDK to deploy and
 - <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>.
 - The following Python libraries: `os`
 - An Azure OpenAI Service resource with a GPT-4 Turbo with Vision model deployed. See [GPT-4 and GPT-4 Turbo Preview model availability](../concepts/models.md#gpt-4-and-gpt-4-turbo-model-availability) for available regions. For more information about resource creation, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).
-- For Vision enhancement (optional): An Azure Computer Vision resource in the same region as your Azure OpenAI resource, in the paid (S1) tier.
 
 ## Set up 
 
@@ -44,7 +43,6 @@ pip install openai
 
 Create a new Python file named _quickstart.py_. Open the new file in your preferred editor or IDE.
 
-#### [Image prompts](#tab/image)
 
 1. Replace the contents of _quickstart.py_ with the following code. 
     
@@ -98,95 +96,6 @@ Create a new Python file named _quickstart.py_. Open the new file in your prefer
     python quickstart.py
     ```
 
-#### [Image prompt enhancements](#tab/enhanced)
-
-GPT-4 Turbo with Vision provides exclusive access to Azure AI Services tailored enhancements. When combined with Azure AI Vision, it enhances your chat experience by providing the chat model with more detailed information about visible text in the image and the locations of objects.
-
-The **Optical Character Recognition (OCR)** integration allows the model to produce higher quality responses for dense text, transformed images, and number-heavy financial documents. It also covers a wider range of languages.
-
-The **object grounding** integration brings a new layer to data analysis and user interaction, as the feature can visually distinguish and highlight important elements in the images it processes.
-
-> [!CAUTION]
-> Azure AI enhancements for GPT-4 Turbo with Vision will be billed separately from the core functionalities. Each specific Azure AI enhancement for GPT-4 Turbo with Vision has its own distinct charges. For details, see the [special pricing information](../concepts/gpt-with-vision.md#special-pricing-information).
-
-> [!IMPORTANT]
-> Vision enhancements are not supported by the GPT-4 Turbo GA model. They are only available with the preview models.
-
-
-1. Replace the contents of _quickstart.py_ with the following code. 
-    
-    ```python
-    from openai import AzureOpenAI
-    
-    api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
-    api_key= os.getenv("AZURE_OPENAI_API_KEY")
-    deployment_name = '<your_deployment_name>'
-    api_version = '2023-12-01-preview' # this might change in the future
-    
-    client = AzureOpenAI(
-        api_key=api_key,  
-        api_version=api_version,
-        base_url=f"{api_base}/openai/deployments/{deployment_name}/extensions",
-    )
-    
-    response = client.chat.completions.create(
-        model=deployment_name,
-        messages=[
-            { "role": "system", "content": "You are a helpful assistant." },
-            { "role": "user", "content": [  
-                { 
-                    "type": "text", 
-                    "text": "Describe this picture:" 
-                },
-                { 
-                    "type": "image_url",
-                    "image_url": {
-                        "url": "<image URL>"
-                    }
-                }
-            ] } 
-        ],
-        extra_body={
-            "dataSources": [
-                {
-                    "type": "AzureComputerVision",
-                    "parameters": {
-                        "endpoint": "<your_computer_vision_endpoint>",
-                        "key": "<your_computer_vision_key>"
-                    }
-                }],
-            "enhancements": {
-                "ocr": {
-                    "enabled": True
-                },
-                "grounding": {
-                    "enabled": True
-                }
-            }
-        },
-        max_tokens=2000
-    )
-    
-    print(response)
-    ```
-
-1. Make the following changes:
-    1. Enter your GPT-4 Turbo with Vision deployment name in the appropriate field. 
-    1. Enter your Computer Vision endpoint URL and key in the appropriate fields.
-    1. Change the value of the `"url"` field to the URL of your image.
-        > [!TIP]
-        > You can also use a base 64 encoded image data instead of a URL. For more information, see the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-a-local-image).
-1. Run the application with the `python` command:
-
-    ```console
-    python quickstart.py
-    ```
-
-#### [Video prompt enhancements](#tab/video)
-
-Video prompt integration is outside the scope of this quickstart. See the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-vision-enhancement-with-video) for detailed instructions on setting up video prompts in chat completions programmatically.
-
----
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "GPT-4 Turbo with Visionに関連する情報の削除"
}
```

### Explanation
このコードの変更は、`gpt-v-python.md`ファイルからGPT-4 Turbo with Visionに関連する詳細な情報を削除したものです。具体的には、以下のような詳細が削除されました。

1. **必要な要件の削除**: GPT-4 Turbo with Visionを使用するために必要な条件、例えばAzure Computer Visionリソースの指定が削除されました。

2. **画像プロンプトの情報削除**: GPT-4 Turbo with Visionの画像プロンプトの強化に関するセクションが丸ごと削除され、OCRやオブジェクトグラウンディング等の統合の説明が消えました。これにより、ユーザーは以前提供されていたこれらの機能に関する情報を失いました。

3. **コード例の削除**: プロンプトの強化機能を使用したコード例が削除され、ユーザーはGPT-4 Turbo with Visionの機能を利用するための実装方法を把握できなくなりました。

この変更により、ドキュメントはより簡潔になりますが、一方でユーザーがGPT-4 Turbo with Visionの機能を理解し利用する上での重要な情報が失われる結果となります。そのため、これらの機能を利用したいユーザーにとっては混乱を招く可能性があります。全体として、この変更は大きな情報が削除されたため、実用性において重要な影響を及ぼします。

## articles/ai-services/openai/includes/gpt-v-rest.md{#item-65c91c}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,6 @@ Use this article to get started using the Azure OpenAI REST APIs to deploy and u
 - <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>.
 - The following Python libraries: `requests`, `json`.
 - An Azure OpenAI Service resource with a GPT-4 Turbo with Vision model deployed. See [GPT-4 and GPT-4 Turbo Preview model availability](../concepts/models.md#gpt-4-and-gpt-4-turbo-model-availability) for available regions. For more information about resource creation, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).
-- For Vision enhancement (optional): An Azure Computer Vision resource in the same region as your Azure OpenAI resource, in the paid (S1) tier.
 
 > [!NOTE]
 > It is currently not supported to turn off content filtering for the GPT-4 Turbo with Vision model.
@@ -40,7 +39,6 @@ Go to your resource in the Azure portal. On the navigation pane, select **Keys a
 
 Create a new Python file named _quickstart.py_. Open the new file in your preferred editor or IDE.
 
-#### [Image prompts](#tab/image)
 
 1. Replace the contents of _quickstart.py_ with the following code. 
     
@@ -99,101 +97,6 @@ Create a new Python file named _quickstart.py_. Open the new file in your prefer
     python quickstart.py
     ```
 
-#### [Image prompt enhancements](#tab/enhanced)
-
-GPT-4 Turbo with Vision provides exclusive access to Azure AI Services tailored enhancements. When combined with Azure AI Vision, it enhances your chat experience by providing the chat model with more detailed information about visible text in the image and the locations of objects.
-
-The **Optical Character Recognition (OCR)** integration allows the model to produce higher quality responses for dense text, transformed images, and number-heavy financial documents. It also covers a wider range of languages.
-
-The **object grounding** integration brings a new layer to data analysis and user interaction, as the feature can visually distinguish and highlight important elements in the images it processes.
-
-> [!CAUTION]
-> Azure AI enhancements for GPT-4 Turbo with Vision will be billed separately from the core functionalities. Each specific Azure AI enhancement for GPT-4 Turbo with Vision has its own distinct charges. For details, see the [special pricing information](../concepts/gpt-with-vision.md#special-pricing-information).
-
-> [!IMPORTANT]
-> Vision enhancements are not supported by the GPT-4 Turbo GA model. They are only available with the preview models.
-
-
-1. Replace the contents of _quickstart.py_ with the following code. 
-    
-    ```python
-    # Packages required:
-    import requests 
-    import json 
-    
-    api_base = '<your_azure_openai_endpoint>' 
-    deployment_name = '<your_deployment_name>'
-    API_KEY = '<your_azure_openai_key>'
-    
-    base_url = f"{api_base}openai/deployments/{deployment_name}" 
-    headers = {   
-        "Content-Type": "application/json",   
-        "api-key": API_KEY 
-    } 
-    
-    # Prepare endpoint, headers, and request body 
-    endpoint = f"{base_url}/extensions/chat/completions?api-version=2023-12-01-preview" 
-    data = {
-        "model": "gpt-4-vision-preview",
-        "enhancements": {
-            "ocr": {
-              "enabled": True
-            },
-            "grounding": {
-              "enabled": True
-            }
-        },
-        "dataSources": [
-        {
-            "type": "AzureComputerVision",
-            "parameters": {
-                "endpoint": "<your_computer_vision_endpoint>",
-                "key": "<your_computer_vision_key>"
-            }
-        }],
-        "messages": [ 
-            { "role": "system", "content": "You are a helpful assistant." }, 
-            { "role": "user", 
-            "content": [  
-                { 
-                    "type": "text", 
-                    "text": "Describe this picture:" 
-                },
-                { 
-                    "type": "image_url", 
-                    "image_url": {
-                        "url" : "<image URL>"
-                    }
-                }
-            ]} 
-        ], 
-        "max_tokens": 2000 
-    }   
-    
-    # Make the API call   
-    response = requests.post(endpoint, headers=headers, data=json.dumps(data))   
-
-    print(f"Status Code: {response.status_code}")   
-    print(response.text)
-    ```
-
-1. Make the following changes:
-    1. Enter your GPT-4 Turbo with Vision deployment name in the appropriate field. 
-    1. Enter your Computer Vision endpoint URL and key in the appropriate fields.
-    1. Change the value of the `"image"` field to the URL of your image.
-        > [!TIP]
-        > You can also use a base 64 encoded image data instead of a URL. For more information, see the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-a-local-image).
-1. Run the application with the `python` command:
-
-    ```console
-    python quickstart.py
-    ```
-
-#### [Video prompt enhancements](#tab/video)
-
-Video prompt integration is outside the scope of this quickstart. See the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-vision-enhancement-with-video) for detailed instructions on setting up video prompts in chat completions programmatically.
-
----
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "GPT-4 Turbo with Visionに関する詳細情報の削除"
}
```

### Explanation
このコードの変更は、`gpt-v-rest.md`ファイルからGPT-4 Turbo with Visionに関連する詳細な情報を削除したものです。主な変更点は以下の通りです。

1. **必須条件の削除**: GPT-4 Turbo with Visionを使用するための条件として挙げられていた「Azure Computer Visionリソースの必要性」が削除され、これに関する手引きやリソース作成に関するリンクも失われました。

2. **画像プロンプトの情報削除**: 画像プロンプトを使用した際の強化機能、例えばOCRやオブジェクトグラウンディングの利用についての説明が完全に削除されました。これにより、これらの機能をどのように活用するかに関する具体的なガイダンスが無くなります。

3. **コード例の削除**: GPT-4 Turbo with Visionを利用したAPI呼び出しに関する具体的なコード例も削除され、ユーザーが実装する際の手引きが欠如しています。

4. **警告や注意事項の削除**: Vision強化機能に関連する注意事項や料金体系に関する情報が含まれていたが、これもすべて削除されました。

この変更により、ドキュメントはより簡潔になりますが、これに伴い、ユーザーはGPT-4 Turbo with Visionの機能を理解し、利用するための重要な情報を失うことになります。特に、これまで利用されていた機能についての具体的なガイダンスが無くなるため、ユーザーにとっては大きな影響を及ぼす可能性があります。全体として、この変更は利用者にとって重要な情報の削除を伴うため、実用性を大きく損なう結果となります。

## articles/ai-services/openai/includes/gpt-v-studio.md{#item-dcd50e}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,6 @@ Start exploring GPT-4 Turbo with Vision capabilities with a no-code approach thr
 
 - An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
 - An Azure OpenAI Service resource with a GPT-4 Turbo with Vision model deployed. See [GPT-4 and GPT-4 Turbo Preview model availability](../concepts/models.md#gpt-4-and-gpt-4-turbo-model-availability) for available regions. For more information about resource creation, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).
-- For Vision enhancement (optional): An Azure Computer Vision resource in the same region as your Azure OpenAI resource, in the paid (S1) tier.
 
 > [!NOTE]
 > It is currently not supported to turn off content filtering for the GPT-4 Turbo with Vision model.
@@ -53,66 +52,6 @@ In this chat session, you're instructing the assistant to aid in understanding i
 
 :::image type="content" source="../media/quickstarts/studio-vision.png" lightbox="../media/quickstarts/studio-vision.png" alt-text="Screenshot of OpenAI studio chat playground.":::
 
-#### [Image prompt enhancements](#tab/enhanced)
-
-GPT-4 Turbo with Vision provides exclusive access to Azure AI Services tailored enhancements. When combined with Azure AI Vision, it enhances your chat experience by providing the chat model with more detailed information about visible text in the image and the locations of objects.
-
-The **Optical Character Recognition (OCR)** integration allows the model to produce higher quality responses for dense text, transformed images, and number-heavy financial documents. It also covers a wider range of languages.
-
-The **object grounding** integration brings a new layer to data analysis and user interaction, as the feature can visually distinguish and highlight important elements in the images it processes.
-
-> [!CAUTION]
-> Azure AI enhancements for GPT-4 Turbo with Vision will be billed separately from the core functionalities. Each specific Azure AI enhancement for GPT-4 Turbo with Vision has its own distinct charges. For details, see the [special pricing information](../concepts/gpt-with-vision.md#special-pricing-information).
-
-> [!IMPORTANT]
-> Vision enhancements are not supported by the GPT-4 Turbo GA model. They are only available with the preview models.
-
-
-In this chat session, you try out the capabilities of the enhanced Vision model.
-1. To start, select your GPT-4 Turbo with Vision deployment from the dropdown.
-1. In the **Configuration** tab on the right side of the chat experience, turn on the option for **Vision** under the **Enhancements** section.
-1. You're required to select a Computer Vision resource to try the enhanced Vision API. Select your resource, and **Save**. 
-1. In the **Assistant setup** pane, provide a System Message to guide the assistant. The default System Message is: "You are an AI assistant that helps people find information." You can tailor the System Message to the image or scenario that you're uploading.  
-
-    > [!NOTE]
-    > It is recommended to update the System Message to be specific to the task in order to avoid unhelpful responses from the model.
-    
-1. Save your changes, and when prompted to confirm updating the system message, select **Continue**.
-1. In the **Chat session** pane, enter a text prompt like "Describe this image," and upload an image with the attachment button. You can use a different text prompt for your use case. Then select **Send**.  
-1. You should receive a response with more detailed information about visible text in the image and the locations of objects. Consider asking follow-up questions related to the analysis of your image to learn more.
-
-:::image type="content" source="../media/quickstarts/studio-vision-enhanced.png" lightbox="../media/quickstarts/studio-vision-enhanced.png" alt-text="Screenshot of OpenAI studio chat playground with Enhancements turned on and the Computer Vision resource selection box.":::
-
-#### [Video prompt enhancements](#tab/video)
-
-GPT-4 Turbo with Vision provides exclusive access to Azure AI Services tailored enhancements. The **video prompt** integration uses Azure AI Vision video retrieval to sample a set of frames from a video and create a transcript of the speech in the video. It enables the AI model to give summaries and answers about video content.
-
-> [!CAUTION]
-> Azure AI enhancements for GPT-4 Turbo with Vision will be billed separately from the core functionalities. Each specific Azure AI enhancement for GPT-4 Turbo with Vision has its own distinct charges. For details, see the [special pricing information](../concepts/gpt-with-vision.md#special-pricing-information).
-
-> [!IMPORTANT]
-> Vision enhancements are not supported by the GPT-4 Turbo GA model. They are only available with the preview models.
-
-1. To start, select your GPT-4 Turbo with Vision deployment from the dropdown.
-1. In the **Configuration** tab on the right side of the chat experience, turn on the option for **Vision** under the **Enhancements** section.
-1. You're required to select a Computer Vision resource to try the enhanced Vision API. Select your resource, and **Save**. 
-1. In the **Assistant setup** pane, provide a System Message to guide the assistant. The default System Message is: "You are an AI assistant that helps people find information." You can tailor the System Message to the video or scenario that you're uploading.  
-
-    > [!NOTE]
-    > It is recommended to update the System Message to be specific to the task in order to avoid unhelpful responses from the model.
-    
-1. Save your changes, and when prompted to confirm updating the system message, select **Continue**.
-1. In the chat session pane, enter a question about the video like: "Describe this video in detail. Focus on brands, technology and people." You can use a different text prompt for your use case. Upload a video using the attachment button and then select **Send**. 
-
-    > [!NOTE]
-    > Currently the chat playground only supports videos that are less than 3 minutes long.
-
-1. You should receive a response describing the video. Consider asking follow-up questions related to the analysis of your video to learn more.
-
-
-:::image type="content" source="../media/quickstarts/studio-vision-enhanced-video.png" alt-text="Screenshot of OpenAI studio chat playground with Enhancements turned on and the Computer Vision resource selection box. Video-specific text prompt." lightbox="../media/quickstarts/studio-vision-enhanced-video.png":::
-
----
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "GPT-4 Turbo with Visionに関連する詳細情報の削除"
}
```

### Explanation
このコードの変更は、`gpt-v-studio.md`ファイルにおいて、GPT-4 Turbo with Visionに関連する詳細情報が削除されたことを示しています。以下のポイントが主な変更内容です。

1. **必須条件の削除**: Azure OpenAI Serviceを利用するための条件として、Azure Computer Visionリソースの必要性が削除されました。これにより、ユーザーにはこれらのリソースを使用することについての指示や情報が提供されなくなりました。

2. **画像プロンプトの情報の削除**: GPT-4 Turbo with Visionの機能を強化するための具体的な操作手順や、OCRおよびオブジェクトグラウンディングに関する説明が削除されています。この変更により、ユーザーがこれらの機能をどのように利用するかについての情報が欠如しています。

3. **ビデオプロンプトに関する情報の削除**: ビデオに関連する機能も削除され、ユーザーがビデオに関して質問するための操作手順が失われました。これによって、ビデオコンテンツの分析方法に対する具体的なガイダンスもなくなっています。

4. **注意事項や警告の削除**: Vision強化機能や、それに伴う料金についての注意事項が削除されており、従来のユーザーはこれらの機能を使用する際のコストに関する理解を損なう恐れがあります。

全体的に、この変更はユーザーにとって重要な情報を削除するものであり、特にGPT-4 Turbo with Visionの機能を利用しようとするユーザーにとって、利用方法についての理解を困難にする可能性があります。そのため、実用性やユーザー体験において重大な影響を及ぼすと考えられます。

## articles/ai-services/openai/includes/text-to-speech-javascript.md{#item-e9b653}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,247 @@
+---
+ms.topic: include
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 09/12/2024
+ms.reviewer: v-baolianzou
+ms.author: eur
+author: eric-urban
+recommendations: false
+---
+
+[Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
+
+## Prerequisites
+
+#### [JavaScript](#tab/javascript)
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+
+
+#### [TypeScript](#tab/typescript)
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [TypeScript](https://www.typescriptlang.org/download/)
+- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+
+
+
+---
+
+## Set up
+
+### Retrieve key and endpoint
+
+To successfully make a call against Azure OpenAI, you need an **endpoint** and a **key**.
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.|
+| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+
+Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+
+:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location highlighted." lightbox="../media/quickstarts/endpoint.png":::
+
+### Environment variables
+
+Create and assign persistent environment variables for your key and endpoint.
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+
+# [Command Line](#tab/command-line)
+
+```CMD
+setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
+```
+
+```CMD
+setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
+```
+
+# [PowerShell](#tab/powershell)
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_KEY_VALUE_HERE', 'User')
+```
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_ENDPOINT_HERE', 'User')
+```
+
+# [Bash](#tab/bash)
+
+```Bash
+echo export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE" >> /etc/environment && source /etc/environment
+```
+
+```Bash
+echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/environment && source /etc/environment
+```
+---
+
+## Create a Node application
+
+In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+
+```console
+npm init
+```
+
+## Install the client library
+
+Install the client libraries with:
+
+```console
+npm install openai @azure/identity
+```
+
+Your app's _package.json_ file will be updated with the dependencies.
+
+## Create a speech file
+
+
+
+#### [JavaScript](#tab/javascript)
+
+1. Create a new file named _Text-to-speech.js_ and open it in your preferred code editor. Copy the following code into the _Text-to-speech.js_ file:
+
+    ```javascript
+    require("dotenv/config");
+    const { writeFile } = require("fs/promises");
+    const { AzureOpenAI } = require("openai");
+    require("openai/shims/node");
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+    const speechFilePath =
+      process.env["SPEECH_FILE_PATH"] || "<path to save the speech file>";
+    
+    // Required Azure OpenAI deployment name and API version
+    const deploymentName = "tts";
+    const apiVersion = "2024-08-01-preview";
+    
+    function getClient() {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    
+    async function generateAudioStream(
+      client,
+      params
+    ) {
+      const response = await client.audio.speech.create(params);
+      if (response.ok) return response.body;
+      throw new Error(`Failed to generate audio stream: ${response.statusText}`);
+    }
+    export async function main() {
+      console.log("== Text to Speech Sample ==");
+    
+      const client = getClient();
+      const streamToRead = await generateAudioStream(client, {
+        model: deploymentName,
+        voice: "alloy",
+        input: "the quick brown chicken jumped over the lazy dogs",
+      });
+    
+      console.log(`Streaming response to ${speechFilePath}`);
+      await writeFile(speechFilePath, streamToRead);
+      console.log("Finished streaming");
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
+    
+    ```
+
+1. Run the script with the following command:
+
+    ```console
+    node Text-to-speech.js
+    ```
+    
+
+#### [TypeScript](#tab/typescript)
+
+1. Create a new file named _Text-to-speech.ts_ and open it in your preferred code editor. Copy the following code into the _Text-to-speech.ts_ file:
+
+    ```typescript
+    import "dotenv/config";
+    import { writeFile } from "fs/promises";
+    import { AzureOpenAI } from "openai";
+    import type { SpeechCreateParams } from "openai/resources/audio/speech";
+    import "openai/shims/node";
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+    const speechFilePath =
+      process.env["SPEECH_FILE_PATH"] || "<path to save the speech file>";
+    
+    // Required Azure OpenAI deployment name and API version
+    const deploymentName = "tts";
+    const apiVersion = "2024-08-01-preview";
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    
+    async function generateAudioStream(
+      client: AzureOpenAI,
+      params: SpeechCreateParams
+    ): Promise<NodeJS.ReadableStream> {
+      const response = await client.audio.speech.create(params);
+      if (response.ok) return response.body;
+      throw new Error(`Failed to generate audio stream: ${response.statusText}`);
+    }
+    export async function main() {
+      console.log("== Text to Speech Sample ==");
+    
+      const client = getClient();
+      const streamToRead = await generateAudioStream(client, {
+        model: deploymentName,
+        voice: "alloy",
+        input: "the quick brown chicken jumped over the lazy dogs",
+      });
+    
+      console.log(`Streaming response to ${speechFilePath}`);
+      await writeFile(speechFilePath, streamToRead);
+      console.log("Finished streaming");
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
+    
+    ```
+    
+   The import of `"openai/shims/node"` is necessary when running the code in a Node.js environment. It ensures that the output type of the `client.audio.speech.create` method is correctly set to `NodeJS.ReadableStream`.
+
+1. Build the application with the following command:
+
+    ```console
+    tsc
+    ```
+
+1. Run the application with the following command:
+
+    ```console
+    node Text-to-speech.js
+    ```
+
+---
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "JavaScriptにおけるテキスト読み上げ機能の追加"
}
```

### Explanation
このコードの変更は、`text-to-speech-javascript.md`という新しいファイルを追加することで、JavaScriptを用いたテキスト読み上げ機能に関すの内容を提供しています。以下のポイントが主な内容です。

1. **概要**: このドキュメントは、Azure OpenAIのテキスト読み上げ機能をJavaScript環境で利用するための手順とサンプルコードを含んでいます。

2. **前提条件**: Azureのサブスクリプション、Node.jsのLTSバージョン、そしてサポートされているリージョンに作成されたAzure OpenAIリソースが必要であることが説明されています。

3. **セットアップ手順**: Azure OpenAI APIを呼び出すために必要なエンドポイントとAPIキーを取得する方法が詳細に記載されています。また、環境変数を設定する手順も示されています。

4. **Nodeアプリケーションの作成**: 新しいNodeアプリケーションを作成するための手順が説明されています。具体的には、ディレクトリを作成してnpmを使用して初期化する方法が含まれています。

5. **クライアントライブラリのインストール**: `openai`と`@azure/identity`のクライアントライブラリをインストールする方法が示されています。

6. **テキスト読み上げスクリプトの作成**: JavaScriptとTypeScriptの両方のサンプルコードが含まれており、実際に音声を生成するためのスクリプトが提供されています。これにより、ユーザーは特定の入力テキストに対して音声を生成し、指定したファイルパスに保存することができます。

7. **実行方法**: 作成したスクリプトを実行するためのコマンドが提示されており、これによりユーザーは簡単にテキスト読み上げ機能を試すことができます。

この新機能により、JavaScript開発者はAzure OpenAIのテキスト読み上げ機能を利用したアプリケーションを簡単に構築できるようになり、学習や応用の幅が広がります。

## articles/ai-services/openai/includes/text-to-speech-rest.md{#item-d067a1}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,65 @@ author: eric-urban
 recommendations: false
 ---
 
-## REST API
+## Prerequisites
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
+- An Azure OpenAI resource created in the North Central US or Sweden Central regions with the `tts-1` or `tts-1-hd` model deployed. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+
+## Set up
+
+### Retrieve key and endpoint
+
+To successfully make a call against Azure OpenAI, you need an **endpoint** and a **key**.
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.|
+| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+
+Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+
+:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location highlighted." lightbox="../media/quickstarts/endpoint.png":::
+
+### Environment variables
+
+Create and assign persistent environment variables for your key and endpoint.
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+
+# [Command Line](#tab/command-line)
+
+```CMD
+setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
+```
+
+```CMD
+setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
+```
+
+# [PowerShell](#tab/powershell)
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_KEY_VALUE_HERE', 'User')
+```
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_ENDPOINT_HERE', 'User')
+```
+
+# [Bash](#tab/bash)
+
+```Bash
+echo export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE" >> /etc/environment && source /etc/environment
+```
+
+```Bash
+echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/environment && source /etc/environment
+```
+---
+
+
+## Create a REST request and response
 
 In a bash shell, run the following command. You need to replace `YourDeploymentName` with the deployment name you chose when you deployed the text to speech model. The deployment name isn't necessarily the same as the model name. Entering the model name results in an error unless you chose a deployment name that is identical to the underlying model name.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト音声化のREST APIの前提条件とセットアップ手順の追加"
}
```

### Explanation
このコード変更は、`text-to-speech-rest.md`ファイルに対する更新であり、テキスト音声化機能のREST APIを利用するための前提条件およびセットアップ手順を追加しています。以下が主な変更点です。

1. **前提条件の明記**: Azureのサブスクリプションや、特定の地域（ノースセントラルUSまたはスウェーデンセントラル）において`tts-1`または`tts-1-hd`モデルが展開されたAzure OpenAIリソースが必要であることが明記されました。

2. **セットアップ手順の追加**: 
   - **エンドポイントとキーの取得**: Azure OpenAIに対してAPIコールを行うために必要なエンドポイントとキーの取得方法が詳細に説明されています。具体的には、Azureポータル内のリソース管理セクションにおいて、これらの情報がどこで見つかるかが示されています。
   - **環境変数の設定**: APIキーとエンドポイントのための永続的な環境変数を作成し設定する方法が追加されており、コマンドライン、PowerShell、Bashの各手法における具体的なコマンド例が含まれています。

3. **RESTリクエストとレスポンスの作成**: 最後に、テキスト音声化モデルを使用するためのRESTリクエストの実行方法が示されています。ここでは、デプロイ名を正しく指定することが強調されています。入力する名前がモデル名と異なる場合、エラーが発生することが明記されています。

新たに追加されたこれらの情報により、ユーザーはAzure OpenAIのテキスト音声化機能をよりスムーズに利用できるようになり、設定や操作の手順が明確になっています。

## articles/ai-services/openai/includes/whisper-javascript.md{#item-3ee990}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,235 @@
+---
+ms.topic: include
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 9/12/2024
+ms.reviewer: v-baolianzou
+ms.author: eur
+author: eric-urban
+---
+
+[Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
+
+## Prerequisites
+
+#### [JavaScript](#tab/javascript)
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+
+
+
+#### [TypeScript](#tab/typescript)
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [TypeScript](https://www.typescriptlang.org/download/)
+- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+
+
+---
+
+
+## Set up
+
+### Retrieve key and endpoint
+
+To successfully make a call against Azure OpenAI, you need an *endpoint* and a *key*.
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.|
+| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+
+Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you'll need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+
+:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location circled in red." lightbox="../media/quickstarts/endpoint.png":::
+
+### Environment variables
+
+Create and assign persistent environment variables for your key and endpoint.
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+
+# [Command Line](#tab/command-line)
+
+```CMD
+setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
+```
+
+```CMD
+setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
+```
+
+# [PowerShell](#tab/powershell)
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_KEY_VALUE_HERE', 'User')
+```
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_ENDPOINT_HERE', 'User')
+```
+
+# [Bash](#tab/bash)
+
+```Bash
+echo export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE" >> /etc/environment && source /etc/environment
+```
+
+```Bash
+echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/environment && source /etc/environment
+```
+---
+
+## Passwordless authentication is recommended
+
+For passwordless authentication, you need to 
+
+1. Use the `@azure/identity` package.
+1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal under **Access control (IAM)** > **Add role assignment**.
+1. Sign in with the Azure CLI such as `az login`.
+
+## Create a Node application
+
+In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+
+```console
+npm init
+```
+
+## Install the client library
+
+Install the client libraries with:
+
+```console
+npm install openai @azure/identity
+```
+
+---
+Your app's _package.json_ file will be updated with the dependencies.
+
+## Create a sample application
+
+
+#### [JavaScript](#tab/javascript)
+
+1. Create a new file named _Whisper.js_ and open it in your preferred code editor. Copy the following code into the _Whisper.js_ file:
+
+    ```javascript
+    require("dotenv/config");
+    const { createReadStream } = require("fs");
+    const { AzureOpenAI } = require("openai");
+    
+    // You will need to set these environment variables or edit the following values
+    const audioFilePath = process.env["AUDIO_FILE_PATH"] || "<audio file path>";
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+    
+    // Required Azure OpenAI deployment name and API version
+    const apiVersion = "2024-08-01-preview";
+    const deploymentName = "whisper";
+    
+    function getClient() {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    
+    export async function main() {
+      console.log("== Transcribe Audio Sample ==");
+    
+      const client = getClient();
+      const result = await client.audio.transcriptions.create({
+        model: "",
+        file: createReadStream(audioFilePath),
+      });
+    
+      console.log(`Transcription: ${result.text}`);
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
+    ```
+
+1. Run the script with the following command:
+
+    ```console
+    node Whisper.js
+    ```
+
+
+#### [TypeScript](#tab/typescript)
+
+1. Create a new file named _Whisper.js_ and open it in your preferred code editor. Copy the following code into the _Whisper.js_ file:
+    
+    ```typescript
+    import "dotenv/config";
+    import { createReadStream } from "fs";
+    import { AzureOpenAI } from "openai";
+    
+    // You will need to set these environment variables or edit the following values
+    const audioFilePath = process.env["AUDIO_FILE_PATH"] || "<audio file path>";
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+    
+    // Required Azure OpenAI deployment name and API version
+    const apiVersion = "2024-08-01-preview";
+    const deploymentName = "whisper";
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    
+    export async function main() {
+      console.log("== Transcribe Audio Sample ==");
+    
+      const client = getClient();
+      const result = await client.audio.transcriptions.create({
+        model: "",
+        file: createReadStream(audioFilePath),
+      });
+    
+      console.log(`Transcription: ${result.text}`);
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
+    ```
+
+1. Build the application with the following command:
+
+    ```console
+    tsc
+    ```
+
+1. Run the application with the following command:
+
+    ```console
+    node Whisper.js
+    ```
+
+---
+
+You can get sample audio files, such as *wikipediaOcelot.wav*, from the [Azure AI Speech SDK repository at GitHub](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/sampledata/audiofiles).
+
+> [!IMPORTANT]
+> For production, store and access your credentials using a secure method, such as [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see [Azure AI services security](../../security-features.md).
+
+## Output
+
+```json
+{"text":"The ocelot, Lepardus paradalis, is a small wild cat native to the southwestern United States, Mexico, and Central and South America. This medium-sized cat is characterized by solid black spots and streaks on its coat, round ears, and white neck and undersides. It weighs between 8 and 15.5 kilograms, 18 and 34 pounds, and reaches 40 to 50 centimeters 16 to 20 inches at the shoulders. It was first described by Carl Linnaeus in 1758. Two subspecies are recognized, L. p. paradalis and L. p. mitis. Typically active during twilight and at night, the ocelot tends to be solitary and territorial. It is efficient at climbing, leaping, and swimming. It preys on small terrestrial mammals such as armadillo, opossum, and lagomorphs."}
+```
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "JavaScriptにおける音声認識機能（Whisper）の追加"
}
```

### Explanation
このコード変更は、`whisper-javascript.md`という新しいファイルが追加され、Azure OpenAIのWhisperモデルをJavaScriptで利用する方法を詳述しています。このドキュメントは、ユーザーが音声を認識するための手順を提供しており、以下の要素が含まれています。

1. **前提条件**: 
   - Azureのサブスクリプション、LTSバージョンのNode.js、及びサポートされている地域に作成されたAzure OpenAIリソースが必要です。
   - TypeScriptを使用するオプションも明記されています。

2. **セットアップ手順**: 
   - **エンドポイントとAPIキーの取得**: Azure OpenAIに対するAPIコールに必要なエンドポイントとAPIキーの取得方法が詳しく説明されています。
   - **環境変数の設定**: APIキーとエンドポイントを環境変数として設定する方法がコマンドライン、PowerShell、Bashで示されています。

3. **パスワードレス認証の推奨**: `@azure/identity`パッケージを使用したパスワードレス認証の手順が説明されており、ユーザーアカウントに対する役割の割り当ても求められます。

4. **Nodeアプリケーションの作成**: 新たにNodeアプリケーションを作成するための手順が提供されており、`npm init`コマンドを用いることが推奨されています。

5. **クライアントライブラリのインストール**: `openai`と`@azure/identity`パッケージのインストール方法が示されています。

6. **サンプルアプリケーションの作成**: 
   - JavaScriptとTypeScriptの両方で音声をテキストに変換するサンプルコードが提供されています。
   - ユーザーは指定した音声ファイルを読み込み、音声認識を実行してその結果をコンソールに出力することができます。

7. **実行方法**: サンプルアプリケーションを実行するための具体的なコマンドが提示されており、音声ファイルのサンプルや、セキュアに資格情報を管理する方法のヒントも紹介されています。

この新機能により、JavaScript開発者はAzureの音声認識機能を利用して、簡単に音声からテキストへの変換を行うアプリケーションを開発できるようになります。

## articles/ai-services/openai/includes/whisper-powershell.md{#item-7db269}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,67 @@ ms.author: eur
 author: eric-urban
 ---
 
-## PowerShell
+## Prerequisites
+
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- <a href="https://aka.ms/installpowershell" target="_blank">You can use either the latest version, PowerShell 7, or Windows PowerShell 5.1.</a>
+- An Azure OpenAI Service resource with a model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
+- An Azure OpenAI Service resource with either the `gpt-35-turbo` or the `gpt-4` models deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
+
+## Set up
+
+### Retrieve key and endpoint
+
+To successfully make a call against Azure OpenAI, you need an *endpoint* and a *key*.
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.|
+| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+
+Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you'll need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+
+:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location circled in red." lightbox="../media/quickstarts/endpoint.png":::
+
+### Environment variables
+
+Create and assign persistent environment variables for your key and endpoint.
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+
+# [Command Line](#tab/command-line)
+
+```CMD
+setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
+```
+
+```CMD
+setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
+```
+
+# [PowerShell](#tab/powershell)
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_KEY_VALUE_HERE', 'User')
+```
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_ENDPOINT_HERE', 'User')
+```
+
+# [Bash](#tab/bash)
+
+```Bash
+echo export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE" >> /etc/environment && source /etc/environment
+```
+
+```Bash
+echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/environment && source /etc/environment
+```
+---
+
+## Create a PowerShell app
 
 Run the following command. You need to replace `YourDeploymentName` with the deployment name you chose when you deployed the Whisper model. The deployment name isn't necessarily the same as the model name. Entering the model name results in an error unless you chose a deployment name that is identical to the underlying model name.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisperモデル用PowerShellの前提条件とセットアップ手順の詳細化"
}
```

### Explanation
このコード変更は、`whisper-powershell.md`ファイルに関する更新で、Azure OpenAIのWhisperモデルをPowerShellで利用するための前提条件やセットアップ手順が詳しく説明されています。主な変更点は以下の通りです。

1. **前提条件の追加**: 新たに3つの前提条件が追加されました。これには、Azureのサブスクリプションの取得、最新のPowerShellバージョン（PowerShell 7またはWindows PowerShell 5.1）の使用、および`gpt-35-turbo`または`gpt-4`モデルのデプロイされたAzure OpenAIサービスリソースが含まれます。

2. **セットアップ手順の詳細化**:
   - **エンドポイントとAPIキーの取得**: Azure OpenAIへのAPIコールに必要なエンドポイントとAPIキーの取得手順が明記されており、それをどこで見つけるか、具体的な場所が示されています。また、エンドポイントとキーを安全に管理するための詳細な手順も強調されています。
   
3. **環境変数の設定**: 環境変数の設定方法について、PowerShell、コマンドライン、Bashなど複数の環境での設定方法が明確に示されています。

4. **PowerShellアプリの作成**: Whisperモデルをデプロイした際のデプロイ名を使用して、PowerShellアプリを作成する方法についての指示も追加されています。デプロイ名がモデル名と異なる場合の注意点も含まれています。

これらの変更により、ユーザーはPowerShellを使用してWhisperモデルを効果的に利用できるようになり、前提条件や手順がより明確になっています。

## articles/ai-services/openai/includes/whisper-python.md{#item-e61179}

<details>
<summary>Diff</summary>
````diff
@@ -7,14 +7,75 @@ ms.topic: include
 ms.date: 3/19/2024
 ---
 
-## Python
-
-### Prerequisites
+## Prerequisites
 
+- An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
+- An Azure OpenAI resource with a Whisper model deployed in a [supported region](../concepts/models.md#whisper-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 - [Python 3.8 or later](https://www.python.org)
 - The following Python library: os
 
-### Set up
+## Set up
+
+### Retrieve key and endpoint
+
+To successfully make a call against Azure OpenAI, you need an *endpoint* and a *key*.
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.|
+| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+
+Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you'll need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+
+:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location circled in red." lightbox="../media/quickstarts/endpoint.png":::
+
+### Environment variables
+
+Create and assign persistent environment variables for your key and endpoint.
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+
+# [Command Line](#tab/command-line)
+
+```CMD
+setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
+```
+
+```CMD
+setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
+```
+
+# [PowerShell](#tab/powershell)
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_KEY_VALUE_HERE', 'User')
+```
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_ENDPOINT_HERE', 'User')
+```
+
+# [Bash](#tab/bash)
+
+```Bash
+echo export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE" >> /etc/environment && source /etc/environment
+```
+
+```Bash
+echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/environment && source /etc/environment
+```
+---
+
+## Passwordless authentication is recommended
+
+For passwordless authentication, you need to 
+
+1. Use the `@azure/identity` package.
+1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal under **Access control (IAM)** > **Add role assignment**.
+1. Sign in with the Azure CLI such as `az login`.
+
+
+## Create a Python environment
 
 Install the OpenAI Python client library with:
 
@@ -34,6 +95,8 @@ pip install openai==0.28.1
 
 ---
 
+## Create the Python app
+
 1. Create a new Python file called *quickstart.py*. Then open it up in your preferred editor or IDE.
 
 1. Replace the contents of *quickstart.py* with the following code. Modify the code to add your deployment name:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisperモデル用Pythonの前提条件とセットアップ手順の詳細化"
}
```

### Explanation
このコード変更は、`whisper-python.md`ファイルに関する更新で、Azure OpenAIのWhisperモデルをPythonで利用する方法について、前提条件やセットアップ手順が詳細に記述されています。主な変更点は以下の通りです。

1. **前提条件の追加**: 
   - Azureのサブスクリプションの作成、サポートされている地域にWhisperモデルがデプロイされたAzure OpenAIリソースの必要性が強調されています。また、Pythonのバージョン（3.8以上）や必要なライブラリ（os）の情報も含まれています。

2. **セットアップ手順の詳細化**:
   - **エンドポイントとAPIキーの取得**: Azure OpenAIへのAPIコールに必要なエンドポイントとAPIキーの取得方法が詳しく説明されており、どこでそれを見つけられるかが明記されています。また、キーの安全な管理方法についても言及されています。
   
3. **環境変数の設定**: 環境変数の設定方法が、コマンドライン、PowerShell、Bashなど複数の環境で提供されています。これにより、ユーザーが必要な設定を自分の環境に応じて行いやすくなっています。

4. **パスワードレス認証の推奨**: `@azure/identity`パッケージを使用することで、パスワードレス認証を行う方法が新たに加わりました。この手順では、ユーザーアカウントに「Cognitive Services User」役割を割り当てる方法も説明されています。

5. **Python環境の作成とアプリケーションの準備**: OpenAIのPythonクライアントライブラリをインストールした後、新しいPythonファイルを作成してWhisperモデルを使用するためのコードを記述する手順が追加されています。

これらの変更により、開発者はPythonを使用してAzureのWhisperモデルに簡単にアクセスし、実行可能なアプリケーションを作成するための具体的で明確な手順を得ることができます。

## articles/ai-services/openai/includes/whisper-rest.md{#item-639ccb}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,69 @@ ms.author: eur
 author: eric-urban
 ---
 
-## REST API
+## Prerequisites
+
+- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
+
+- An Azure OpenAI resource deployed in a [supported region and with a supported model](../concepts/use-your-data.md#regional-availability-and-model-support).
+
+- Be sure that you are assigned at least the [Cognitive Services Contributor](../how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
+
+- Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
+
+## Set up
+
+### Retrieve key and endpoint
+
+To successfully make a call against Azure OpenAI, you need an *endpoint* and a *key*.
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.|
+| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+
+Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you'll need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+
+:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location circled in red." lightbox="../media/quickstarts/endpoint.png":::
+
+### Environment variables
+
+Create and assign persistent environment variables for your key and endpoint.
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+
+# [Command Line](#tab/command-line)
+
+```CMD
+setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
+```
+
+```CMD
+setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
+```
+
+# [PowerShell](#tab/powershell)
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_KEY_VALUE_HERE', 'User')
+```
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_ENDPOINT_HERE', 'User')
+```
+
+# [Bash](#tab/bash)
+
+```Bash
+echo export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE" >> /etc/environment && source /etc/environment
+```
+
+```Bash
+echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/environment && source /etc/environment
+```
+---
+
+## Create a REST API request and response
 
 In a bash shell, run the following command. You need to replace `YourDeploymentName` with the deployment name you chose when you deployed the Whisper model. The deployment name isn't necessarily the same as the model name. Entering the model name results in an error unless you chose a deployment name that is identical to the underlying model name.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisperモデル用REST APIの前提条件とセットアップ手順の詳細化"
}
```

### Explanation
このコード変更は、`whisper-rest.md`ファイルに関する更新で、Azure OpenAIのWhisperモデルを利用するためのREST APIに関する前提条件やセットアップ手順が詳細に記述されています。主な変更点は以下の通りです。

1. **前提条件の追加**:
   - Azureのサブスクリプションを取得する必要性が強調され、リンクが提供されています。また、適切な地域にデプロイされたWhisperモデルを持つAzure OpenAIリソースの必要性も記載されています。
   - Azure OpenAIリソースに対して「Cognitive Services Contributor」ロールが割り当てられていることを確認する必要があります。
   - サンプルデータをGitHubからダウンロードする手順も新たに加わりました。

2. **セットアップ手順の詳細化**:
   - **エンドポイントとAPIキーの取得**: Azure OpenAIへのAPIコールに必要なエンドポイントとAPIキーの取得方法が詳しく説明されており、これらを見つける場所が明記されています。また、キーの安全な管理方法についても説明されています。
   
3. **環境変数の設定**: コマンドライン、PowerShell、Bashなど複数の環境における環境変数の設定方法が提供されており、これによりユーザーは自身の環境に応じた設定を行いやすくなっています。

4. **REST APIリクエストとレスポンスの作成**: Bashシェルで実行するコマンドを使用してREST APIリクエストを作成する手順が追加されています。この際、デプロイ名とモデル名の違いについての注意事項も含まれています。

これらの変更により、開発者はAzureのWhisperモデルに対してREST APIを使用して簡単にアクセスし、効果的にリクエストを行う方法を学ぶことができ、スムーズな開発が可能になります。

## articles/ai-services/openai/index.yml{#item-0adb87}

<details>
<summary>Diff</summary>
````diff
@@ -1,17 +1,17 @@
 ### YamlMime:Landing
 
 title: Azure OpenAI Service documentation # < 60 chars
-summary: Azure OpenAI Service provides access to OpenAI's models including the GPT-4, GPT-4 Turbo with Vision, GPT-3.5-Turbo, DALLE-3 and Embeddings model series with the security and enterprise capabilities of Azure. 
+summary: Azure OpenAI Service provides access to OpenAI's models including the GPT-4o, GPT-4o mini, GPT-4, GPT-4 Turbo with Vision, GPT-3.5-Turbo, DALLE-3 and Embeddings model series with the security and enterprise capabilities of Azure. 
   
 metadata:
   title: Azure OpenAI Service documentation - Quickstarts, Tutorials, API Reference - Azure AI services | Microsoft Docs
-  description: Learn how to use Azure OpenAI's powerful models including the GPT-4, GPT-4 Turbo with Vision, GPT-3.5-Turbo, DALL-E 3 and Embeddings model series
+  description: Learn how to use Azure OpenAI's powerful models including the GPT-4o, GPT-4o mini, GPT-4, GPT-4 Turbo with Vision, GPT-3.5-Turbo, DALL-E 3 and Embeddings model series
   ms.service: azure-ai-openai
   ms.custom:
   ms.topic: landing-page
   author: mrbullwinkle
   ms.author: mbullwin
-  ms.date: 08/31/2024
+  ms.date: 09/18/2024
 
 # linkListType: architecture | concept | deploy | download | get-started | how-to-guide | learn | overview | quickstart | reference | tutorial | video | whats-new
 # Limits: https://review.learn.microsoft.com/help/contribute/contribute-how-to-write-landing-page?branch=main#limits
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスのモデル情報の修正"
}
```

### Explanation
このコード変更は、`index.yml`ファイルに関する更新で、Azure OpenAIサービスに関連するモデルの情報が修正されています。主な変更点は以下の通りです。

1. **モデル名の修正**:
   - サマリーと説明の部分で、「GPT-4」および「DALLE-3」のモデル名が「GPT-4o」、「GPT-4o mini」、「DALL-E 3」として変更されています。この変更により、より正確な情報が提供されるようになっています。

2. **日付の更新**:
   - 最終更新日が「08/31/2024」から「09/18/2024」に変更されています。これにより、ドキュメントが最新の状態であることが示されています。

3. **メタデータの修正**:
   - メタデータの内容も合わせて更新されており、最新のモデルに基づいた情報が正確に反映されています。

これらの変更により、Azure OpenAIサービスに関する文書が、最新のモデル情報を基にしており、ユーザーが正確で信頼できる情報を得られるようになっています。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ recommendations: false
 
 # What is Azure OpenAI Service?
 
-Azure OpenAI Service provides REST API access to OpenAI's powerful language models including GPT-4o, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, image understanding, semantic search, and natural language to code translation. Users can access the service through REST APIs, Python SDK, or our web-based interface in the Azure OpenAI Studio.
+Azure OpenAI Service provides REST API access to OpenAI's powerful language models including GPT-4o, GPT-4o mini, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, image understanding, semantic search, and natural language to code translation. Users can access the service through REST APIs, Python SDK, or our web-based interface in the Azure OpenAI Studio.
 
 ### Features overview
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスの言語モデル情報の補足"
}
```

### Explanation
このコード変更は、`overview.md`ファイルに関する更新で、Azure OpenAIサービスの紹介文に関連する内容が微細に修正されています。主な変更点は以下の通りです。

1. **モデル名の追記**:
   - 説明文において、Azure OpenAIサービスが提供する言語モデルに「GPT-4o mini」という新しいモデル名が追加されています。この変更により、利用可能なモデルの範囲がより明確に示されることになりました。

2. **文の整形**:
   - 文の整形は行われていないものの、新しいモデル名の追加により、全体の流れや理解が向上しています。

この更新により、Azure OpenAIサービスの説明がより包括的になり、ユーザーが利用できる言語モデルに関する情報が一層充実しました。これにより、ユーザーは適切なモデルを選択しやすくなります。

## articles/ai-services/openai/quickstart.md{#item-7d1656}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: 'Quickstart - Deploy a model and generate text using Azure OpenAI Service'
+title: 'Quickstart - Deploy a model and generate text using the legacy completions API'
 titleSuffix: Azure OpenAI
-description: Walkthrough on how to get started with Azure OpenAI and make your first completions call.
+description: Walkthrough on how to get started with Azure OpenAI and make your first legacy completions API call.
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
@@ -14,7 +14,7 @@ zone_pivot_groups: openai-quickstart-new
 recommendations: false
 ---
 
-# Quickstart: Get started generating text using Azure OpenAI Service
+# Quickstart: Get started generating text using the legacy completions API
 
 Use this article to get started making your first calls to Azure OpenAI.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レガシー補完APIを使用したクイックスタートのタイトル変更"
}
```

### Explanation
このコード変更は、`quickstart.md`ファイルに関する更新で、Azure OpenAIサービスにおけるクイックスタートガイドのタイトルと説明が修正されています。主な変更点は以下の通りです。

1. **タイトルの変更**:
   - タイトルが「Quickstart - Deploy a model and generate text using Azure OpenAI Service」から「Quickstart - Deploy a model and generate text using the legacy completions API」に変更されました。この変更により、使用するAPIの種類（レガシー補完API）が明確になりました。

2. **説明の修正**:
   - 説明文にも「legacy completions API」という表現が追加され、最初の呼び出しを行う際に使用する特定のAPIが強調されています。この修正により、ユーザーはどのAPIを使用するかをより明確に理解できるようになります。

これらの変更は、クイックスタートガイドの内容が特定のAPIに基づいていることを反映しており、ユーザーが正しい手順を踏むための指針を提供しています。結果として、利用者に対して一貫した情報を提供し、より良い体験を促進します。

## articles/ai-services/openai/text-to-speech-quickstart.md{#item-c344ad}

<details>
<summary>Diff</summary>
````diff
@@ -5,11 +5,12 @@ description: Use the Azure OpenAI Service for text to speech with OpenAI voices.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: quickstart
-ms.date: 2/1/2024
+ms.date: 9/12/2024
 ms.reviewer: v-baolianzou
 ms.author: eur
 author: eric-urban
 recommendations: false
+zone_pivot_groups: programming-languages-rest-js
 ---
 
 # Quickstart: Text to speech with the Azure OpenAI Service
@@ -18,64 +19,18 @@ In this quickstart, you use the Azure OpenAI Service for text to speech with Ope
 
 The available voices are: `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer`. For more information, see [Azure OpenAI Service reference documentation for text to speech](./reference.md#text-to-speech).
 
-## Prerequisites
 
-- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
-- An Azure OpenAI resource created in the North Central US or Sweden Central regions with the `tts-1` or `tts-1-hd` model deployed. For more information, see [Create a resource and deploy a model with Azure OpenAI](how-to/create-resource.md).
+::: zone pivot="rest-api"
 
-## Set up
-
-### Retrieve key and endpoint
-
-To successfully make a call against Azure OpenAI, you need an **endpoint** and a **key**.
-
-|Variable name | Value |
-|--------------------------|-------------|
-| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.|
-| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
-
-Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
-
-:::image type="content" source="media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location highlighted." lightbox="media/quickstarts/endpoint.png":::
-
-### Environment variables
-
-Create and assign persistent environment variables for your key and endpoint.
-
-[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
-
-# [Command Line](#tab/command-line)
-
-```CMD
-setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
-```
-
-```CMD
-setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
-```
-
-# [PowerShell](#tab/powershell)
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_KEY_VALUE_HERE', 'User')
-```
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_ENDPOINT_HERE', 'User')
-```
+[!INCLUDE [REST API quickstart](includes/text-to-speech-rest.md)]
 
-# [Bash](#tab/bash)
+::: zone-end
 
-```Bash
-echo export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE" >> /etc/environment && source /etc/environment
-```
+::: zone pivot="programming-language-javascript"
 
-```Bash
-echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/environment && source /etc/environment
-```
----
+[!INCLUDE [JavaScript quickstart](includes/text-to-speech-javascript.md)]
 
-[!INCLUDE [REST API quickstart](includes/text-to-speech-rest.md)]
+::: zone-end
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト読み上げクイックスタートの内容を更新"
}
```

### Explanation
このコード変更は、`text-to-speech-quickstart.md`ファイルにおいて、Azure OpenAIサービスを使用したテキスト読み上げに関するクイックスタートガイドの内容が大幅に更新されたものです。主な変更点は以下の通りです。

1. **日付の更新**:
   - ドキュメントの日付が「2/1/2024」から「9/12/2024」に変更され、新しい日付が反映されています。

2. **タイトルと説明の修正**:
   - タイトルと説明において、Azure OpenAIサービスの利用方法が強調され、新しい情報を反映するために内容が調整されています。

3. **コンテンツの再構成**:
   - いくつかのセクションが削除され、代わりにREST APIに関するクイックスタートのインクルードが追加されています。また、プログラミング言語や環境変数の設定に関する情報が見直され、一部が再編成されています。具体的には、BashやPowerShellのスクリプトが削除され、JavaScriptに関連する情報が追加されています。

4. **ピボットゾーンの導入**:
   - ゾーンが設定されており、異なるプログラミング言語やAPIのバリエーションに基づいた内容がフレンドリーに提示されています。これにより、ユーザーは自分のニーズに応じた情報を簡単に取得できるようになっています。

これらの変更により、クイックスタートガイドは最新の情報を反映し、Azure OpenAIサービスを利用したテキスト読み上げ機能の呼び出しをよりわかりやすく、実用的にしています。ユーザーは手順に従いながら、システムを迅速に導入できるようになっています。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -29,8 +29,6 @@ items:
   items:
     - name: Assistants (preview)
       href: assistants-quickstart.md
-    - name: Completions
-      href: quickstart.md
     - name: Chat
       href: chatgpt-quickstart.md  
       displayName: ChatGPT, chatgpt
@@ -44,6 +42,8 @@ items:
       href: whisper-quickstart.md
     - name: Text to speech (preview)
       href: text-to-speech-quickstart.md
+    - name: Completions (legacy)
+      href: quickstart.md
 - name: Concepts
   items:
     - name: Assistants
@@ -118,7 +118,7 @@ items:
       href: ./how-to/dall-e.md
     - name: Function calling
       href: ./how-to/function-calling.md
-    - name: Completions
+    - name: Completions (legacy)
       href: ./how-to/completions.md
     - name: JSON mode
       href: ./how-to/json-mode.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新 - 補完機能のレガシー参照追加"
}
```

### Explanation
このコード変更は、`toc.yml`ファイルにおいて、目次の構成が更新されたものです。主な変更点は以下の通りです。

1. **補完機能の項目の追加と修正**:
   - 元の目次では「Completions」という項目が削除され、新たに「Completions (legacy)」という名称で再追加されています。これにより、レガシー補完機能を明示的に示す項目が設けられ、ユーザーが異なる補完機能を識別しやすくなりました。

2. **項目の並び替え**:
   - 「Assistants (preview)」の項目の下に「Completions (legacy)」が追加され、これにより目次が整理されています。また、「Chat」や「Text to speech (preview)」セクションの近くにも同様の変更が施されています。

3. **項目の名前の調整**:
   - 視認性を向上させるため、目次の表示名に「(legacy)」というフレーズが追加されています。これによって、ユーザーはこのコンテンツが最新のものでないことを一目で理解できます。

これらの変更により、目次はより明確で、ユーザーは古いリソースと新しいリソースを簡単に区別できるようになっています。目次の整頓によって、ドキュメント全体の可読性が向上し、ユーザー体験が改善される効果が期待されます。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -20,6 +20,16 @@ This article provides a summary of the latest releases and major documentation u
 
 ## September 2024
 
+### GPT-4o 2024-08-06 provisioned deployments
+GPT-4o 2024-08-06 is now available for provisioned deployments in East US, East US 2, North Central US, and Sweden Central. It is also available for global provisioned deployments.
+
+For the latest information on model availability, see the [models page](/azure/ai-services/openai/concepts/models#provisioned-deployment-model-availability).
+
+### NEW Global provisioned deployment type
+Global deployments are available in the same Azure OpenAI resources as non-global deployment types but allow you to leverage Azure's global infrastructure to dynamically route traffic to the data center with best availability for each request. Global provisioned deployments provide reserved model processing capacity for high and predictable throughput using Azure global infrastructure. Global provisioned deployments are supported on `gpt-4o-2024-08-06` and `gpt-4o-mini-2024-07-18` models.
+
+For more information, see the [deployment types guide](https://aka.ms/aoai/docs/deployment-types).
+
 ### NEW o1-preview and o1-mini models available for limited access
 
 The Azure OpenAI `o1-preview` and `o1-mini` models are specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能の追加 - GPT-4oおよびグローバル展開タイプ"
}
```

### Explanation
このコード変更は、`whats-new.md`ファイルにおいて、Azure OpenAIの最新機能に関する情報が追加されたものです。主な変更点は以下の通りです。

1. **新しいモデル情報の追加**:
   - 新たに「GPT-4o 2024-08-06」というモデルが、特定の地域（East US、East US 2、North Central US、Sweden Central）で使用可能になったことが記載されています。これにより、ユーザーはこのモデルがいつ、どの地域で利用できるかを把握できるようになっています。

2. **グローバルプロビジョンド展開タイプの導入**:
   - グローバル展開タイプの新しい機能が追加されました。この展開タイプは、Azureのグローバルインフラを活用し、リクエストごとに最適なデータセンターにトラフィックを動的にルーティングします。この機能により、高いスループットと予測可能な処理能力を持つモデルが提供可能になっています。

3. **新しいモデル「o1-preview」と「o1-mini」の情報**:
   - その他、新たに「o1-preview」と「o1-mini」モデルが限られたアクセスで利用可能になったことが言及されています。これらのモデルは、推論や問題解決タスクに特化して設計されており、科学、コーディング、数学の分野において強力なパフォーマンスを発揮します。

これらの変更により、ユーザーは最新のモデルおよび展開オプションに関する必要な情報を簡単に把握できるようになり、Azure OpenAIサービスの利用ケースを広げる手助けとなることが期待されます。最新機能の明示的な説明は、ユーザー体験の向上に寄与します。

## articles/ai-services/openai/whisper-quickstart.md{#item-4cae3d}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.reviewer: v-baolianzou
 ms.author: eur
 author: eric-urban
 recommendations: false
-zone_pivot_groups: openai-whisper
+zone_pivot_groups: programming-languages-rest-ps-py-js
 ---
 
 # Quickstart: Speech to text with the Azure OpenAI Whisper model
@@ -23,67 +23,21 @@ The file size limit for the Whisper model is 25 MB. If you need to transcribe a
 > [!NOTE]
 > The OpenAI Whisper model is currently in Limited Access Public Preview.
 
-## Prerequisites
-
-- An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
-- An Azure OpenAI resource with a Whisper model deployed in a [supported region](./concepts/models.md#whisper-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](how-to/create-resource.md).
-
-## Set up
-
-### Retrieve key and endpoint
-
-To successfully make a call against Azure OpenAI, you need an *endpoint* and a *key*.
-
-|Variable name | Value |
-|--------------------------|-------------|
-| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.|
-| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
-
-Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you'll need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
-
-:::image type="content" source="media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location circled in red." lightbox="media/quickstarts/endpoint.png":::
-
-### Environment variables
-
-Create and assign persistent environment variables for your key and endpoint.
-
-[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
-
-# [Command Line](#tab/command-line)
-
-```CMD
-setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
-```
-
-```CMD
-setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
-```
-
-# [PowerShell](#tab/powershell)
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_KEY_VALUE_HERE', 'User')
-```
+::: zone pivot="rest-api"
 
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_ENDPOINT_HERE', 'User')
-```
+[!INCLUDE [REST API quickstart](includes/whisper-rest.md)]
 
-# [Bash](#tab/bash)
+::: zone-end
 
-```Bash
-echo export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE" >> /etc/environment && source /etc/environment
-```
+::: zone pivot="programming-language-python"
 
-```Bash
-echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/environment && source /etc/environment
-```
----
+[!INCLUDE [Python SDK quickstart](includes/whisper-python.md)]
 
+::: zone-end
 
-::: zone pivot="rest-api"
+::: zone pivot="programming-language-javascript"
 
-[!INCLUDE [REST API quickstart](includes/whisper-rest.md)]
+[!INCLUDE [JavaScript quickstart](includes/whisper-javascript.md)]
 
 ::: zone-end
 
@@ -93,12 +47,6 @@ echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/envi
 
 ::: zone-end
 
-::: zone pivot="programming-language-python"
-
-[!INCLUDE [Python quickstart](includes/whisper-python.md)]
-
-::: zone-end
-
 ## Clean up resources
 
 If you want to clean up and remove an Azure OpenAI resource, you can delete the resource. Before deleting the resource, you must first delete any deployed models.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisperモデルのクイックスタートガイド改良"
}
```

### Explanation
このコード変更は、`whisper-quickstart.md`ファイルにおいて、Azure OpenAIのWhisperモデルに関するクイックスタートガイドが改良されたもので、主に以下の点が挙げられます。

1. **コンテンツの簡素化**:
   - 元のドキュメントから66行が削除され、必要な情報が整理されました。特に、環境変数の設定やエンドポイントの取得方法に関する詳細な手順が省略され、全体の分量が削減されています。

2. **新しいゾーンピボットの追加**:
   - 「programming-languages-rest-ps-py-js」という新しいゾーンが追加され、ユーザーはさまざまなプログラミング言語に基づくクイックスタートガイドにアクセスしやすくなりました。これにより、ユーザーは自分の利用したいプログラミング言語に応じた情報を見つけやすくなります。

3. **REST APIおよびSDKに関する情報の統合**:
   - REST APIおよびPython SDKのクイックスタートセクションが整理され、必要な情報が適切なゾーンに含められています。この変更により、ユーザーはAPI利用に必要なガイドを効率的に参照できるようになりました。

これらの変更により、Whisperモデルのクイックスタートガイドはより直感的で使いやすくなり、特に新規ユーザーにとって情報を得やすい内容へと改善されています。ユーザーが必要な情報を迅速に取得できることで、Azure OpenAIサービスを始める際の障壁が低減されることが期待されます。


