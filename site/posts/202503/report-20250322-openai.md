---
date: '2025-03-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:34ecec7...MicrosoftDocs:3341d93
summary: このコードの差分には、新機能の追加や重大な変更が含まれています。特に、画像処理の詳細設定パラメータの追加、ファインチューニング用Pythonコードの大幅な更新、およびチュートリアルの大幅な改訂が強調されています。新機能には、画像処理用の詳細パラメータの導入、リアルタイムオーディオサポートの改善、リンクの正規化が含まれます。ブレイキングチェンジとしては、古いコードの削除やTutorialの構造的変更が報告されています。これらのアップデートは、ユーザーが最新の技術を使用して、より効果的にサービスを活用できるようにするためのものです。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:34ecec7...MicrosoftDocs:3341d93){target="_blank"}

<format>
# ハイライト
このコードの差分には、新しい機能の追加や重大な変更が含まれています。特に注目すべきは、画像処理の詳細設定パラメータの追加や、ファインチューニング用Pythonコードの大幅な更新と古いコードの削除、そしてファインチューニングに関するチュートリアルの大幅な更新です。

## 新機能
- 画像処理用に`"detail"`パラメータが追加され、低、高、または自動解像度を選択可能。
- Pythonのリアルタイムオーディオサポートの改善では、新しい`AsyncAzureOpenAI`クラスの導入。
- データ構成やファインチューニングスタジオ関連のリンクが正規化された。

## ブレイキングチェンジ
- ファインチューニング用Pythonコードの大幅な変更と、古いライブラリ使用法の削除。
- ファインチューニングに関するチュートリアルの大幅な更新による構造的な変更。

## その他の更新
- 多数のドキュメント内リンクの更新（例：`https://oai.azure.com`から`https://ai.azure.com`への変更）。
- 文書やリンクの細かな修正により、ユーザーエクスペリエンスが向上。

# インサイト
この差分では、Azure OpenAIのドキュメント全体にわたる小規模ながら重要な更新が示されています。リンクや名称の変更は、ポータルへのアクセス性を向上させ、ユーザーが正確な情報に基づいて操作できるようにしている点が注目されます。特に、画像処理の詳細設定が加わったことは、Azure OpenAIのビジュアルモデルの使い方に柔軟性をもたらす重要な追加といえます。

ファインチューニング関連のブレイキングチェンジは、最新のAPIとライブラリのバージョンに対応するためのものです。古いコードの削除と新しい標準へのシフトによって、より安全で最新の環境での作業が可能になります。これにより、ユーザーは常に最新の技術を採用したモデル操作が可能になり、エンジニアやデータサイエンティストは最新のベストプラクティスに基づいた効率的なモデル開発を進めることができるようになります。

リアルタイムオーディオのサポートや他のライブラリのインポート方法の改善は、開発者が迅速かつ簡潔なコードを書くための重要な変更点であり、Azure OpenAIをより使いやすくするための工夫がなされています。全体的に見て、これらの更新は、Azure OpenAIが提供するサービスをユーザーがより効果的かつ効率的に活用できることを目的とした、利便性の高い変更です。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [provisioned-throughput.md](#item-022e0c) | minor update | プロビジョニングスループットに関するドキュメントの更新 | modified | 4 | 4 | 8 | 
| [use-your-data.md](#item-455d6e) | minor update | データ活用に関するドキュメントのリンク更新 | modified | 1 | 1 | 2 | 
| [batch.md](#item-a131d5) | minor update | バッチ処理に関するエラーメッセージのフォーマット修正 | modified | 2 | 2 | 4 | 
| [create-resource.md](#item-c1c8a3) | minor update | リソース作成に関するドキュメントのメタデータ更新 | modified | 1 | 1 | 2 | 
| [fine-tuning-deploy.md](#item-286d57) | minor update | Azure AI Foundryポータルのリンク修正 | modified | 1 | 1 | 2 | 
| [gpt-with-vision.md](#item-4d8502) | minor update | 画像処理における詳細設定パラメータの追加 | modified | 23 | 8 | 31 | 
| [on-your-data-configuration.md](#item-4875d3) | minor update | Azure AI Foundryポータルのリンク修正 | modified | 2 | 2 | 4 | 
| [stored-completions.md](#item-ccc7e6) | minor update | Azure AI Foundryポータルのリンク修正 | modified | 3 | 3 | 6 | 
| [chatgpt-studio.md](#item-ab43f3) | minor update | Azure AI Foundryポータルの名称修正 | modified | 1 | 1 | 2 | 
| [fine-tuning-python.md](#item-976f58) | breaking change | ファインチューニング用Pythonコードの更新と古いコードの削除 | modified | 4 | 43 | 47 | 
| [fine-tuning-studio.md](#item-439f1e) | minor update | Azure AI Foundryポータルのリンク修正 | modified | 1 | 1 | 2 | 
| [fine-tuning-unified.md](#item-718336) | minor update | Azure OpenAIのリンクと文言の修正 | modified | 2 | 2 | 4 | 
| [realtime-javascript.md](#item-3c125e) | minor update | AzureOpenAIのインポート文の修正 | modified | 2 | 2 | 4 | 
| [realtime-python.md](#item-1291c0) | minor update | Pythonでのリアルタイムオーディオクライアントのアップデート | modified | 120 | 101 | 221 | 
| [realtime-typescript.md](#item-eacc9c) | minor update | AzureOpenAIのインポート文の修正 | modified | 2 | 2 | 4 | 
| [studio.md](#item-eeeaff) | minor update | Azure AI Foundry ポータルへのリンクの修正 | modified | 2 | 2 | 4 | 
| [fine-tune.md](#item-8f87b5) | breaking change | ファインチューニングチュートリアルの大幅な更新 | modified | 7 | 184 | 191 | 


# Modified Contents
## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -46,7 +46,7 @@ An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model.
 ## How much throughput per PTU you get for each model
 The amount of throughput (tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in the minute. Generating output tokens requires more processing than input tokens. For the models specified in the table below, 1 output token counts as 3 input tokens towards your TPM per PTU limit. The service dynamically balances the input & output costs, so users do not have to set specific input and output limits. This approach means your deployment is resilient to fluctuations in the workload shape.
 
-To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the specified models. To understand the impact of output tokens on the TPM per PTU limit, use the 3 input token to 1 output token ratio. For a detailed understanding of how different ratios of input and output tokens impact the throughput your workload needs, see the [Azure OpenAI capacity calculator](https://oai.azure.com/portal/calculator). The table also shows Service Level Agreement (SLA) Latency Target Values per model.  For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
+To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the specified models. To understand the impact of output tokens on the TPM per PTU limit, use the 3 input token to 1 output token ratio. For a detailed understanding of how different ratios of input and output tokens impact the throughput your workload needs, see the [Azure OpenAI capacity calculator](https://ai.azure.com/resource/calculator). The table also shows Service Level Agreement (SLA) Latency Target Values per model.  For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
 
 |Topic| **gpt-4o**   | **gpt-4o-mini**  | **o1**|
 | --- | --- | --- | --- |
@@ -57,7 +57,7 @@ To help with simplifying the sizing effort, the following table outlines the TPM
 |Input TPM per PTU |2,500|37,000|230|
 |Latency Target Value |25 Tokens Per Second|33 Tokens Per Second|25 Tokens Per Second|
 
-For a full list see the [Azure OpenAI Service in Azure AI Foundry portal calculator](https://oai.azure.com/portal/calculator).
+For a full list see the [Azure OpenAI Service in Azure AI Foundry portal calculator](https://ai.azure.com/resource/calculator).
 
 
 > [!NOTE]
@@ -135,7 +135,7 @@ If an acceptable region isn't available to support the desire model, version and
 
 ### Determining the number of PTUs needed for a workload
 
-PTUs represent an amount of model processing capacity. Similar to your computer or databases, different workloads or requests to the model will consume different amounts of underlying processing capacity. The conversion from throughput needs to PTUs can be approximated using historical token usage data or call shape estimations (input tokens, output tokens, and requests per minute) as outlined in our [performance and latency](../how-to/latency.md) documentation. To simplify this process, you can use the [Azure OpenAI Capacity calculator](https://oai.azure.com/portal/calculator) to size specific workload shapes.
+PTUs represent an amount of model processing capacity. Similar to your computer or databases, different workloads or requests to the model will consume different amounts of underlying processing capacity. The conversion from throughput needs to PTUs can be approximated using historical token usage data or call shape estimations (input tokens, output tokens, and requests per minute) as outlined in our [performance and latency](../how-to/latency.md) documentation. To simplify this process, you can use the [Azure OpenAI Capacity calculator](https://ai.azure.com/resource/calculator) to size specific workload shapes.
 
 A few high-level considerations:
 - Generations require more capacity than prompts
@@ -187,7 +187,7 @@ For provisioned deployments, we use a variation of the leaky bucket algorithm to
 
 #### How many concurrent calls can I have on my deployment?
 
-The number of concurrent calls you can achieve depends on each call's shape (prompt size, `max_tokens` parameter, etc.). The service continues to accept calls until the utilization reaches 100%. To determine the approximate number of concurrent calls, you can model out the maximum requests per minute for a particular call shape in the [capacity calculator](https://oai.azure.com/portal/calculator). If the system generates less than the number of output tokens set for the `max_tokens` parameter, then the provisioned deployment will accept more requests.
+The number of concurrent calls you can achieve depends on each call's shape (prompt size, `max_tokens` parameter, etc.). The service continues to accept calls until the utilization reaches 100%. To determine the approximate number of concurrent calls, you can model out the maximum requests per minute for a particular call shape in the [capacity calculator](https://ai.azure.com/resource/calculator). If the system generates less than the number of output tokens set for the `max_tokens` parameter, then the provisioned deployment will accept more requests.
 
 ## What models and regions are available for provisioned throughput?
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングスループットに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「プロビジョニングスループット」に関する文書に対する小規模な更新です。主に、いくつかのリンクが更新され、正しいURLに修正されています。具体的には、トークン生成に関する説明で使用されるリソースのリンクが以前の 'oai.azure.com' から 'ai.azure.com' に変更されており、これによりユーザーはより正確な情報にアクセスできるようになります。また、ドキュメント内の他の関連情報についても、同様のリンクの修正が行われています。

これらの変更により、ユーザーはプロビジョニングスループットの理解を深め、Azure OpenAIサービスの利用における計算リソースの把握を向上させることができます。文書全体の整合性が向上し、最新のアクセス先情報を利用することができるため、文書の精度が増しています。

## articles/ai-services/openai/concepts/use-your-data.md{#item-455d6e}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,7 @@ Use this article to learn about Azure OpenAI On Your Data, which makes it easier
 
 ## What is Azure OpenAI On Your Data
 
-Azure OpenAI On Your Data enables you to run advanced AI models such as GPT-35-Turbo and GPT-4 on your own enterprise data without needing to train or fine-tune models. You can chat on top of and analyze your data with greater accuracy. You can specify sources to support the responses based on the latest information available in your designated data sources. You can access Azure OpenAI On Your Data using a REST API, via the SDK or the web-based interface in the [Azure AI Foundry portal](https://oai.azure.com/). You can also create a web app that connects to your data to enable an enhanced chat solution or deploy it directly as a copilot in the Copilot Studio (preview).
+Azure OpenAI On Your Data enables you to run advanced AI models such as GPT-35-Turbo and GPT-4 on your own enterprise data without needing to train or fine-tune models. You can chat on top of and analyze your data with greater accuracy. You can specify sources to support the responses based on the latest information available in your designated data sources. You can access Azure OpenAI On Your Data using a REST API, via the SDK or the web-based interface in the [Azure AI Foundry portal](https://ai.azure.com/). You can also create a web app that connects to your data to enable an enhanced chat solution or deploy it directly as a copilot in the Copilot Studio (preview).
 
 ## Developing with Azure OpenAI On Your Data
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ活用に関するドキュメントのリンク更新"
}
```

### Explanation
この変更は、Azure OpenAIの「データ活用」に関する文書に対する小規模な更新です。具体的には、Azure OpenAI On Your Dataに関する説明文の中のリンクが、以前の 'oai.azure.com' から 'ai.azure.com' に修正されています。この変更により、ユーザーは最新の情報にアクセスしやすくなります。

文書の内容自体には大きな変更はなく、主にリンクの選択肢の更新に伴うものであり、ユーザーがリアルタイムで正確なデータに基づいた応答を得るためのサポートが向上しています。また、この変更は、Azure OpenAI On Your Dataを利用する際に必要な情報へのアクセスをよりスムーズにすることを目指しています。文書全体の信頼性とユーザーエクスペリエンスが向上しています。

## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -202,8 +202,8 @@ When a job failure occurs, you'll find details about the failure in the `errors`
                 "object": “list”,
                 "data": [
                 {
-               “code”: “empty_file”,
-               “message”: “The input file is empty. Please ensure that the batch contains at least one   request.”
+               "code": "empty_file",
+               "message": "The input file is empty. Please ensure that the batch contains at least one   request."
                     }
                 ]
           },
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理に関するエラーメッセージのフォーマット修正"
}
```

### Explanation
この変更は、Azure OpenAIの「バッチ処理」に関する文書におけるエラーメッセージのフォーマット修正に関するものです。具体的には、エラーメッセージを含むコードブロック内の引用符の形式が、異なるスタイル（“ ”）から通常の引用符（" "）に変更されています。

これにより、エラーメッセージがコンピュータプログラムの標準的な形式に合わせて整えられ、ユーザーにとって理解しやすくなります。文書全体の整合性が向上し、開発者がエラーメッセージの意味を正確に把握しやすくなります。文書の品質向上に寄与しています。

## articles/ai-services/openai/how-to/create-resource.md{#item-c1c8a3}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to get started with Azure OpenAI Service and create your
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
-ms.custom: devx-track-azurecli, build-2023, build-2023-dataai, devx-track-azurepowershell
+ms.custom: devx-track-azurecli, build-2023, build-2023-dataai, devx-track-azurepowershell, innovation-engine
 ms.topic: how-to
 ms.date: 01/31/2025
 zone_pivot_groups: openai-create-resource
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソース作成に関するドキュメントのメタデータ更新"
}
```

### Explanation
この変更は、Azure OpenAIの「リソース作成」に関するドキュメントのメタデータに少しの修正が加えられたことに関するものです。具体的には、`ms.custom`フィールドに新たに「innovation-engine」というタグが追加され、他のタグと併せて文書の特性をより細かく分類できるようになっています。

この変更により、ドキュメントはより正確に管理され、特定のトピックに関連する情報を探す際のユーザー体験が改善されます。新しいタグの追加は、Azureの最新の機能やサービスに関連する情報を提供するための取り組みの一環であり、ユーザーがリソース作成のプロセスに関する最新情報に迅速にアクセスできるようにするためのものです。

## articles/ai-services/openai/how-to/fine-tuning-deploy.md{#item-286d57}

<details>
<summary>Diff</summary>
````diff
@@ -306,7 +306,7 @@ az cognitiveservices account deployment create
 
 ## [Portal](#tab/portal)
 
-After your custom model deploys, you can use it like any other deployed model. You can use the **Playgrounds** in [Azure AI Foundry portal](https://oai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models.
+After your custom model deploys, you can use it like any other deployed model. You can use the **Playgrounds** in the [Azure AI Foundry portal](https://ai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models.
 
 :::image type="content" source="../media/quickstarts/playground-load-new.png" alt-text="Screenshot of the Playground pane in Azure AI Foundry portal, with sections highlighted." lightbox="../media/quickstarts/playground-load-new.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク修正"
}
```

### Explanation
この変更は、Azure OpenAIの「ファインチューニングとデプロイ」に関するドキュメント内で、Azure AI Foundryポータルのリンクが修正されたことに関するものです。具体的には、ポータルのURLが`https://oai.azure.com`から`https://ai.azure.com`に変更されました。

この修正により、ユーザーが正しいポータルにアクセスできるようになり、カスタムモデルのデプロイ後にPlaygroundsを利用する際の利便性が向上します。また、他のデプロイされたモデルと同様に、`temperature`や`max_tokens`などのパラメータを使用できることが引き続き保証されています。この変更は、ユーザーが最新の情報に基づいて作業できるよう支援する重要な修正です。

## articles/ai-services/openai/how-to/gpt-with-vision.md{#item-4d8502}

<details>
<summary>Diff</summary>
````diff
@@ -162,7 +162,29 @@ The following is a sample request body. The format is the same as the chat compl
 > ...
 > ```
 
-### Output
+### Detail parameter settings  
+
+You can optionally define a `"detail"` parameter in the `"image_url"` field. Choose one of three values, `low`, `high`, or `auto`, to adjust the way the model interprets and processes images. 
+- `auto` setting: The default setting. The model decides between low or high based on the size of the image input.
+- `low` setting: the model does not activate the "high res" mode, instead processes a lower resolution 512x512 version, resulting in quicker responses and reduced token consumption for scenarios where fine detail isn't crucial.
+- `high` setting: the model activates "high res" mode. Here, the model initially views the low-resolution image and then generates detailed 512x512 segments from the input image. Each segment uses double the token budget, allowing for a more detailed interpretation of the image.
+
+You set the value using the format shown in this example:
+
+```json
+{ 
+    "type": "image_url",
+    "image_url": {
+        "url": "<image URL>",
+        "detail": "high"
+    }
+}
+```
+
+For details on how the image parameters impact tokens used and pricing please see - [What is Azure OpenAI? Image Tokens](../overview.md#image-tokens)
+
+
+## Output
 
 The API response should look like the following.
 
@@ -236,13 +258,6 @@ Every response includes a `"finish_reason"` field. It has the following possible
 - `length`: Incomplete model output due to the `max_tokens` input parameter or model's token limit.
 - `content_filter`: Omitted content due to a flag from our content filters.
 
-### Detail parameter settings in image processing: Low, High, Auto  
-
-The _detail_ parameter in the model offers three choices: `low`, `high`, or `auto`, to adjust the way the model interprets and processes images. The default setting is auto, where the model decides between low or high based on the size of the image input. 
-- `low` setting: the model does not activate the "high res" mode, instead processes a lower resolution 512x512 version, resulting in quicker responses and reduced token consumption for scenarios where fine detail isn't crucial.
-- `high` setting: the model activates "high res" mode. Here, the model initially views the low-resolution image and then generates detailed 512x512 segments from the input image. Each segment uses double the token budget, allowing for a more detailed interpretation of the image.''
-
-For details on how the image parameters impact tokens used and pricing please see - [What is Azure OpenAI? Image Tokens](../overview.md#image-tokens)
 
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像処理における詳細設定パラメータの追加"
}
```

### Explanation
この変更は、Azure OpenAIの「GPTとビジョン」に関するドキュメントにおいて、画像処理のための詳細設定パラメータが新たに追加されたことに関するものです。

具体的には、`"image_url"`フィールド内にオプションとして`"detail"`パラメータを導入しました。このパラメータには、`low`、`high`、`auto`の3つの値を選択でき、モデルが画像を解釈し処理する方法を調整できます。それぞれの設定は次のようになります：

- **auto設定**: デフォルト設定で、モデルが画像サイズに基づいて低解像度または高解像度を決定します。
- **low設定**: モデルは「高解像度」モードを有効にせず、より低解像度の512x512バージョンを処理し、迅速な応答とトークン消費の削減が実現されます。
- **high設定**: モデルは「高解像度」モードを有効にし、低解像度の画像を初めに視認し、入力画像から詳細な512x512セグメントを生成します。この場合、各セグメントは2倍のトークン予算を使用します。

この新しい設定方法とその影響についての具体例が示され、ユーザーがモデルの性能を必要に応じて調整できるようになります。この変更は、モデルを使用する上での柔軟性と効率を向上させるための重要な追加です。

## articles/ai-services/openai/how-to/on-your-data-configuration.md{#item-4875d3}

<details>
<summary>Diff</summary>
````diff
@@ -29,7 +29,7 @@ When you use Azure OpenAI On Your Data to ingest data from Azure blob storage, l
 
 * Steps 1 and 2 are only used for file upload.
 * Downloading URLs to your blob storage is not illustrated in this diagram. After web pages are downloaded from the internet and uploaded to blob storage, steps 3 onward are the same.
-* One indexer, one index, and one data source in the Azure AI Search resource is created using prebuilt skills and [integrated vectorization](/azure/search/vector-search-integrated-vectorization.md).
+* One indexer, one index, and one data source in the Azure AI Search resource is created using prebuilt skills and [integrated vectorization](/azure/search/vector-search-integrated-vectorization).
 * Azure AI Search handles the extraction, chunking, and vectorization of chunked documents through integrated vectorization. If a scheduling interval is specified, the indexer will run accordingly. 
 
 For the managed identities used in service calls, only system assigned managed identities are supported. User assigned managed identities aren't supported.
@@ -59,7 +59,7 @@ Azure OpenAI On Your Data lets you restrict the documents that can be used in re
     `group_ids` is the default field name. If you use a different field name like `my_group_ids`, you can map the field in [index field mapping](../concepts/use-your-data.md#index-field-mapping).
 
 1. Make sure each sensitive document in the index has this security field value set to the permitted groups of the document.
-1. In [Azure AI Foundry portal](https://oai.azure.com/portal), add your data source. in the [index field mapping](../concepts/use-your-data.md#index-field-mapping) section, you can map zero or one value to the **permitted groups** field, as long as the schema is compatible. If the **permitted groups** field isn't mapped, document level access is disabled. 
+1. In the [Azure AI Foundry portal](https://ai.azure.com/portal), add your data source. In the [index field mapping](../concepts/use-your-data.md#index-field-mapping) section, you can map zero or one value to the **permitted groups** field, as long as the schema is compatible. If the **permitted groups** field isn't mapped, document level access is disabled. 
 
 **Azure AI Foundry portal**
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク修正"
}
```

### Explanation
この変更は、Azure OpenAIの「データ構成に関するガイド」において、Azure AI Foundryポータルへのリンクが修正されたことを示しています。具体的には、ポータルのURLが`https://oai.azure.com/portal`から`https://ai.azure.com/portal`に変更されました。

さらに、変更されたドキュメントでは、Azure AI Searchリソースで使用されるインデクサー、インデックス、およびデータソースの構成に関する情報が引き続き提供されています。この部分には、事前構築されたスキルと統合ベクトル化を使用してインデクサーが作成されることや、機密文書の管理に関する詳細が含まれています。

このリンクの修正は、ユーザーが正しいポータルにアクセスできるようにし、作業の効率を向上させるための重要な更新です。ドキュメント全体にわたり、情報の正確性と整合性を確保することが目的です。

## articles/ai-services/openai/how-to/stored-completions.md{#item-ccc7e6}

<details>
<summary>Diff</summary>
````diff
@@ -249,7 +249,7 @@ curl $AZURE_OPENAI_ENDPOINT/openai/deployments/gpt-4o/chat/completions?api-versi
 
 ---
 
-Once stored completions are enabled for an Azure OpenAI deployment, they'll begin to show up in the [Azure AI Foundry portal](https://oai.azure.com) in the **Stored Completions** pane.
+Once stored completions are enabled for an Azure OpenAI deployment, they'll begin to show up in the [Azure AI Foundry portal](https://ai.azure.com) in the **Stored Completions** pane.
 
 :::image type="content" source="../media/stored-completions/stored-completions.png" alt-text="Screenshot of the stored completions User Experience." lightbox="../media/stored-completions/stored-completions.png":::
 
@@ -259,7 +259,7 @@ Distillation allows you to turn your stored completions into a fine-tuning datas
 
 Distillation requires a minimum of 10 stored completions, though it's recommended to provide hundreds to thousands of stored completions for the best results.
 
-1. From the **Stored Completions** pane in the [Azure AI Foundry portal](https://oai.azure.com) use the **Filter** options to select the completions you want to train your model with.
+1. From the **Stored Completions** pane in the [Azure AI Foundry portal](https://ai.azure.com) use the **Filter** options to select the completions you want to train your model with.
 
 2. To begin distillation, select **Distill**
 
@@ -288,7 +288,7 @@ The [evaluation](./evaluations.md) of large language models is a critical step i
 
 Stored completions can be used as a dataset for running evaluations.
 
-1. From the **Stored Completions** pane in the [Azure AI Foundry portal](https://oai.azure.com) use the **Filter** options to select the completions you want to be part of your evaluation dataset.
+1. From the **Stored Completions** pane in the [Azure AI Foundry portal](https://ai.azure.com) use the **Filter** options to select the completions you want to be part of your evaluation dataset.
 
 2. To configure the evaluation, select **Evaluate**
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク修正"
}
```

### Explanation
この変更は、Azure OpenAIの「保存済み完了」に関するドキュメントにおいて、Azure AI Foundryポータルへのリンクが修正されたことを示しています。具体的には、ポータルのURLが旧URLの`https://oai.azure.com`から新URLの`https://ai.azure.com`に更新されました。

この修正は、文中の複数の箇所において行われており、保存済み完了がポータル内の**保存済み完了**ペインに表示されることや、モデルのトレーニングや評価のためにどのように保存済み完了を選択するかの手順が説明された部分にも影響しています。

このリンクの更新は、ユーザーが正確なポータルにアクセスできるようにし、作業を円滑に進められるようにすることを目的としています。また、情報の正確性と一貫性を保つために重要な修正です。

## articles/ai-services/openai/includes/chatgpt-studio.md{#item-ab43f3}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.date: 09/19/2024
 
 ## Go to Azure AI Foundry
 
-Navigate to [Azure AI Foundry](https://oai.azure.com/) and sign-in with credentials that have access to your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
+Navigate to the [Azure AI Foundry portal](https://ai.azure.com/) and sign-in with credentials that have access to your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
 
 From Azure AI Foundry, select **Chat playground**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルの名称修正"
}
```

### Explanation
この変更は、Azure OpenAIに関する「ChatGPTスタジオ」のドキュメントにおいて、Azure AI Foundryへの案内に関する文言が修正されたことを示しています。具体的には、「Azure AI Foundry」のリンクが`https://oai.azure.com/`から`https://ai.azure.com/`に変更され、その際に名称が「Azure AI Foundry」から「Azure AI Foundryポータル」に更新されました。

この修正は、ユーザーが正しいポータルにアクセスできることを保証し、サインインプロセス中に必要なディレクトリ、Azureサブスクリプション、Azure OpenAIリソースの選択についての指示内容の明確さを改善することを目的としています。正確な情報を提供することで、ユーザー体験を向上させる重要な更新です。

## articles/ai-services/openai/includes/fine-tuning-python.md{#item-976f58}

<details>
<summary>Diff</summary>
````diff
@@ -110,8 +110,6 @@ For large data files, we recommend that you import from an Azure Blob  store. La
 
 The following Python example uploads local training and validation files by using the Python SDK, and retrieves the returned file IDs.
 
-# [OpenAI Python 1.x](#tab/python-new)
-
 ```python
 # Upload fine-tuning files
 
@@ -144,42 +142,6 @@ print("Validation file ID:", validation_file_id)
 
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-[!INCLUDE [Deprecation](../includes/deprecation.md)]
-
-```python
-# Upload fine-tuning files
-
-import openai
-import os
-
-openai.api_key = os.getenv("AZURE_OPENAI_API_KEY") 
-openai.api_base =  os.getenv("AZURE_OPENAI_ENDPOINT")
-openai.api_type = 'azure'
-openai.api_version = '2024-02-01' # This API version or later is required
-
-training_file_name = 'training_set.jsonl'
-validation_file_name = 'validation_set.jsonl'
-
-# Upload the training and validation dataset files to Azure OpenAI with the SDK.
-
-training_response = openai.File.create(
-    file=open(training_file_name, "rb"), purpose="fine-tune", user_provided_filename="training_set.jsonl"
-)
-training_file_id = training_response["id"]
-
-validation_response = openai.File.create(
-    file=open(validation_file_name, "rb"), purpose="fine-tune", user_provided_filename="validation_set.jsonl"
-)
-validation_file_id = validation_response["id"]
-
-print("Training file ID:", training_file_id)
-print("Validation file ID:", validation_file_id)
-```
-
----
-
 ## Create a customized model
 
 After you upload your training and validation files, you're ready to start the fine-tuning job.
@@ -205,7 +167,6 @@ print("Job ID:", response.id)
 print("Status:", response.id)
 print(response.model_dump_json(indent=2))
 ```
----
 
 You can also pass additional optional parameters like hyperparameters to take greater control of the fine-tuning process. For initial training we recommend using the automatic defaults that are present without specifying these parameters. 
 
@@ -226,7 +187,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-02-01"  # This API version or later is required
+  api_version="2024-10-21"  # This API version or later is required
 )
 
 client.fine_tuning.jobs.create(
@@ -265,7 +226,7 @@ When each training epoch completes a checkpoint is generated. A checkpoint is a
 You can run the list checkpoints command to retrieve the list of checkpoints associated with an individual fine-tuning job. You might need to upgrade your OpenAI client library to the latest version with `pip install openai --upgrade` to run this command.
 
 ```python
-response = client.fine_tuning.jobs.list_events(fine_tuning_job_id=job_id, limit=10)
+response = client.fine_tuning.jobs.checkpoints.list(job_id)
 print(response.model_dump_json(indent=2))
 ```
 
@@ -336,7 +297,7 @@ resource_group = "<YOUR_RESOURCE_GROUP_NAME>"
 resource_name = "<YOUR_AZURE_OPENAI_RESOURCE_NAME>"
 model_deployment_name ="gpt-35-turbo-ft" # custom deployment name that you will use to reference the model when making inference calls.
 
-deploy_params = {'api-version': "2024-10-21"} 
+deploy_params = {'api-version': "2024-10-01"} # control plane API version rather than dataplane API for this call 
 deploy_headers = {'Authorization': 'Bearer {}'.format(token), 'Content-Type': 'application/json'}
 
 deploy_data = {
@@ -378,7 +339,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-02-01"  
+  api_version="2024-10-21"  
 )
 
 response = client.fine_tuning.jobs.create(
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "ファインチューニング用Pythonコードの更新と古いコードの削除"
}
```

### Explanation
この変更は、ファインチューニングに関連するPythonコードに大幅な変更を加えたもので、古いコードの削除と新しいコードの追加が行われています。具体的には、以下のようなことが行われています。

1. **古いコードの削除**: OpenAI Pythonライブラリのバージョン0.28.1に関連する古いサンプルコードが完全に削除されました。この部分には、ファインチューニング用のデータファイルをアップロードするための詳細な手順が含まれていました。

2. **新しいコードの追加**: Python SDKを使用して、トレーニングおよび検証ファイルをアップロードする際の例が簡素化され、必要な変更のみが残されています。

3. **APIバージョンの更新**: 古いAPIバージョンから、より最新のバージョン（2024-10-21）への更新が行われました。この変更により、利用者は新しい機能や改善点を活用できるようになります。

4. **新しいチェックポイントコマンド**: チェックポイントのリストを取得するためのコマンドが変更され、`list_events`から`checkpoints.list`に更新されました。これにより、ユーザーはファインチューニングジョブに関連する情報をより効率的に取得できます。

この変更は、新しいAPIに適応するための重要な更新であり、ユーザーが最新の手法を使用してファインチューニングを行えるようにすることを目的としています。

## articles/ai-services/openai/includes/fine-tuning-studio.md{#item-439f1e}

<details>
<summary>Diff</summary>
````diff
@@ -101,7 +101,7 @@ In general, doubling the dataset size can lead to a linear increase in model qua
 
 Azure AI Foundry portal provides the **Create custom model** wizard, so you can interactively create and train a fine-tuned model for your Azure resource.
 
-1. Open Azure AI Foundry portal at <a href="https://oai.azure.com/" target="_blank">https://oai.azure.com/</a> and sign in with credentials that have access to your Azure OpenAI resource. During the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
+1. Go to the Azure AI Foundry portal at <a href="https://ai.azure.com/" target="_blank">https://ai.azure.com/</a> and sign in with credentials that have access to your Azure OpenAI resource. During the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
 
 1. In Azure AI Foundry portal, browse to the **Tools > Fine-tuning** pane, and select **Fine-tune model**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク修正"
}
```

### Explanation
この変更は、Azure AI Foundryポータルに関する文書において、一部のリンクと文言が修正されたことを示しています。具体的には、以下の点が修正されています。

1. **リンクの変更**: Azure AI FoundryポータルのURLが`https://oai.azure.com/`から`https://ai.azure.com/`に変更されました。これにより、ユーザーが正しいポータルにアクセスできることが保証されます。

2. **文言の修正**: 「Open Azure AI Foundry portal」の表現が「Go to the Azure AI Foundry portal」に変更されています。この変更は、より自然な表現で指示を伝えることを目的としています。

この修正により、ユーザーが最新のリソースに正確にアクセスし、ファインチューニングモデルを作成する手順を明確に理解できるようになります。全体として、ユーザー体験を向上させるための重要な改善です。

## articles/ai-services/openai/includes/fine-tuning-unified.md{#item-718336}

<details>
<summary>Diff</summary>
````diff
@@ -14,9 +14,9 @@ ms.author: mbullwin
 There are two unique fine-tuning experiences in the Azure AI Foundry portal:
 
 * [Hub/Project view](https://ai.azure.com) - supports fine-tuning models from multiple providers including Azure OpenAI, Meta Llama, Microsoft Phi, etc.
-* [Azure OpenAI centric view](https://oai.azure.com) - only supports fine-tuning Azure OpenAI models, but has support for additional features like the [Weights & Biases (W&B) preview integration](../how-to/weights-and-biases-integration.md). 
+* [Azure OpenAI centric view](https://ai.azure.com/resource/overview) - only supports fine-tuning Azure OpenAI models, but has support for additional features like the [Weights & Biases (W&B) preview integration](../how-to/weights-and-biases-integration.md). 
 
-If you are only fine-tuning Azure OpenAI models, we recommend the Azure OpenAI centric fine-tuning experience which is available by navigating to [https://oai.azure.com](https://oai.azure.com). 
+If you are only fine-tuning Azure OpenAI models, we recommend the Azure OpenAI centric fine-tuning experience which is available by navigating to [https://ai.azure.com/resource/overview](https://ai.azure.com/resource/overview). 
 
 # [Azure OpenAI](#tab/azure-openai)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIのリンクと文言の修正"
}
```

### Explanation
この変更は、Azure AI Foundryポータルに関する文書で、Azure OpenAIに関するリンクと説明文が修正されたことを示しています。具体的には、以下の点が修正されています。

1. **リンクの変更**: Azure OpenAIセントリックビューのリンクが`https://oai.azure.com`から`https://ai.azure.com/resource/overview`に変更されました。これにより、ユーザーが正確なリソースページにアクセスできるようになります。

2. **文言の修正**: サンプリングの文中で、Azure OpenAIモデルのファインチューニングに関する推奨が更新されています。新しいリンクが使用されたことに伴い、説明文もそれに合わせて調整されました。

これらの変更により、ユーザーは正確で最新の情報をもとにAzure OpenAIモデルのファインチューニングを行うことができ、より良いユーザーエクスペリエンスが提供されます。全体として、情報の整合性と明瞭さを向上させるための重要な更新です。

## articles/ai-services/openai/includes/realtime-javascript.md{#item-3c125e}

<details>
<summary>Diff</summary>
````diff
@@ -66,7 +66,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
     ```javascript 
     import { OpenAIRealtimeWS } from "openai/beta/realtime/ws";
-    import { AzureOpenAI } from "openai/index.mjs";
+    import { AzureOpenAI } from "openai";
     import { DefaultAzureCredential, getBearerTokenProvider } from "@azure/identity";
     async function main() {
         // You will need to set these environment variables or edit the following values
@@ -149,7 +149,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
     ```javascript 
     import { OpenAIRealtimeWS } from "openai/beta/realtime/ws";
-    import { AzureOpenAI } from "openai/index.mjs";
+    import { AzureOpenAI } from "openai";
     async function main() {
         // You will need to set these environment variables or edit the following values
         const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AzureOpenAIのインポート文の修正"
}
```

### Explanation
この変更は、リアルタイムJavaScriptに関する文書で、AzureOpenAIのインポート記述を修正することを目的としています。具体的には、以下の点が更新されています。

1. **インポートパスの変更**: `import { AzureOpenAI } from "openai/index.mjs";`から`import { AzureOpenAI } from "openai";`に変更されています。この修正により、より簡潔で標準的なインポート方法が使用されるようになります。

この変更は、開発者がAzureOpenAIを利用する際の設定手順を明確にし、使いやすさを向上させることを意図しています。また、標準化されたインポート文により、将来の更新や互換性の維持が容易になります。全体として、ユーザーにとって重要で便利な情報の改善が図られています。

## articles/ai-services/openai/includes/realtime-python.md{#item-1291c0}

<details>
<summary>Diff</summary>
````diff
@@ -62,11 +62,15 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     > [!TIP]
     > We recommend that you create and activate a new Python environment to use to install the packages you need for this tutorial. Don't install packages into your global python installation. You should always use a virtual or conda environment when installing python packages, otherwise you can break your global installation of Python.
 
-1. Install the real-time audio client library for Python with:
+
+1. Install the OpenAI Python client library with:
 
     ```console
-    pip install "https://github.com/Azure-Samples/aoai-realtime-audio-sdk/releases/download/py%2Fv0.5.3/rtclient-0.5.3.tar.gz"
+    pip install openai[realtime]
     ```
+    
+    > [!NOTE]
+    > This library is maintained by OpenAI. Refer to the [release history](https://github.com/openai/openai-python/releases) to track the latest updates to the library.
 
 1. For the **recommended** keyless authentication with Microsoft Entra ID, install the `azure-identity` package with:
 
@@ -78,122 +82,138 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 [!INCLUDE [resource authentication](resource-authentication.md)]
 
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+
 ## Text in audio out
 
 ## [Microsoft Entra ID](#tab/keyless)
 
 1. Create the `text-in-audio-out.py` file with the following code:
 
     ```python
+    import os
     import base64
     import asyncio
-    from azure.identity.aio import DefaultAzureCredential
-    from rtclient import (
-        ResponseCreateMessage,
-        RTLowLevelClient,
-        ResponseCreateParams
-    )
-    
-    # Set environment variables or edit the corresponding values here.
-    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"] or "https://<your-resource-name>.openai.azure.com/"
-    deployment = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] or "gpt-4o-mini-realtime-preview"
-    
-    async def text_in_audio_out():
-        async with RTLowLevelClient(
-            url=endpoint,
-            azure_deployment=deployment,
-            token_credential=DefaultAzureCredential(),
-        ) as client:
-            await client.send(
-                ResponseCreateMessage(
-                    response=ResponseCreateParams(
-                        modalities={"audio", "text"}, 
-                        instructions="Please assist the user."
-                    )
+    from openai import AsyncAzureOpenAI
+    from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider
+    
+    async def main() -> None:
+        """
+        When prompted for user input, type a message and hit enter to send it to the model.
+        Enter "q" to quit the conversation.
+        """
+    
+        credential = DefaultAzureCredential()
+        token_provider=get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")
+        client = AsyncAzureOpenAI(
+            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
+            azure_ad_token_provider=token_provider,
+            api_version="2024-10-01-preview",
+        )
+        async with client.beta.realtime.connect(
+            model="gpt-4o-realtime-preview",  # name of your deployment
+        ) as connection:
+            await connection.session.update(session={"modalities": ["text", "audio"]})  
+            while True:
+                user_input = input("Enter a message: ")
+                if user_input == "q":
+                    break
+    
+                await connection.conversation.item.create(
+                    item={
+                        "type": "message",
+                        "role": "user",
+                        "content": [{"type": "input_text", "text": user_input}],
+                    }
                 )
-            )
-            done = False
-            while not done:
-                message = await client.recv()
-                match message.type:
-                    case "response.done":
-                        done = True
-                    case "error":
-                        done = True
-                        print(message.error)
-                    case "response.audio_transcript.delta":
-                        print(f"Received text delta: {message.delta}")
-                    case "response.audio.delta":
-                        buffer = base64.b64decode(message.delta)
-                        print(f"Received {len(buffer)} bytes of audio data.")
-                    case _:
-                        pass
-    
-    async def main():
-        await text_in_audio_out()
+                await connection.response.create()
+                async for event in connection:
+                    if event.type == "response.text.delta":
+                        print(event.delta, flush=True, end="")
+                    elif event.type == "response.audio.delta":
+                        
+                        audio_data = base64.b64decode(event.delta)
+                        print(f"Received {len(audio_data)} bytes of audio data.")
+                    elif event.type == "response.audio_transcript.delta":
+                        print(f"Received text delta: {event.delta}")
+                    elif event.type == "response.text.done":
+                        print()
+                    elif event.type == "response.done":
+                        break
+    
+        await credential.close()
     
     asyncio.run(main())
     ```
 
+1. Sign in to Azure with the following command:
+
+    ```shell
+    az login
+    ```
+
 1. Run the Python file.
 
     ```shell
     python text-in-audio-out.py
     ```
 
+1. When prompted for user input, type a message and hit enter to send it to the model. Enter "q" to quit the conversation.
+
 ## [API key](#tab/api-key)
 
 1. Create the `text-in-audio-out.py` file with the following code:
 
     ```python
+    import os
     import base64
     import asyncio
-    from azure.core.credentials import AzureKeyCredential
-    from rtclient import (
-        ResponseCreateMessage,
-        RTLowLevelClient,
-        ResponseCreateParams
-    )
-    
-    # Set environment variables or edit the corresponding values here.
-    api_key = os.environ["AZURE_OPENAI_API_KEY"]    
-    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
-    deployment = "gpt-4o-mini-realtime-preview"
-    
-    async def text_in_audio_out():
-        async with RTLowLevelClient(
-            url=endpoint,
-            azure_deployment=deployment,
-            key_credential=AzureKeyCredential(api_key) 
-        ) as client:
-            await client.send(
-                ResponseCreateMessage(
-                    response=ResponseCreateParams(
-                        modalities={"audio", "text"}, 
-                        instructions="Please assist the user."
-                    )
-                )
-            )
-            done = False
-            while not done:
-                message = await client.recv()
-                match message.type:
-                    case "response.done":
-                        done = True
-                    case "error":
-                        done = True
-                        print(message.error)
-                    case "response.audio_transcript.delta":
-                        print(f"Received text delta: {message.delta}")
-                    case "response.audio.delta":
-                        buffer = base64.b64decode(message.delta)
-                        print(f"Received {len(buffer)} bytes of audio data.")
-                    case _:
-                        pass
-    
-    async def main():
-        await text_in_audio_out()
+    from openai import AsyncAzureOpenAI
+    from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider
     
+    async def main() -> None:
+        """
+        When prompted for user input, type a message and hit enter to send it to the model.
+        Enter "q" to quit the conversation.
+        """
+    
+        client = AsyncAzureOpenAI(
+            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
+            api_key=os.environ["AZURE_OPENAI_API_KEY"],
+            api_version="2024-10-01-preview",
+        )
+        async with client.beta.realtime.connect(
+            model="gpt-4o-realtime-preview",  # deployment name of your model
+        ) as connection:
+            await connection.session.update(session={"modalities": ["text", "audio"]})  
+            while True:
+                user_input = input("Enter a message: ")
+                if user_input == "q":
+                    break
+    
+                await connection.conversation.item.create(
+                    item={
+                        "type": "message",
+                        "role": "user",
+                        "content": [{"type": "input_text", "text": user_input}],
+                    }
+                )
+                await connection.response.create()
+                async for event in connection:
+                    if event.type == "response.text.delta":
+                        print(event.delta, flush=True, end="")
+                    elif event.type == "response.audio.delta":
+                        
+                        audio_data = base64.b64decode(event.delta)
+                        print(f"Received {len(audio_data)} bytes of audio data.")
+                    elif event.type == "response.audio_transcript.delta":
+                        print(f"Received text delta: {event.delta}")
+                    elif event.type == "response.text.done":
+                        print()
+                    elif event.type == "response.done":
+                        break
+        
     asyncio.run(main())
     ```
 
@@ -203,6 +223,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     python text-in-audio-out.py
     ```
 
+1. When prompted for user input, type a message and hit enter to send it to the model. Enter "q" to quit the conversation.
 ---
 
 Wait a few moments to get the response.
@@ -211,29 +232,27 @@ Wait a few moments to get the response.
 
 The script gets a response from the model and prints the transcript and audio data received.
 
-The output will look similar to the following:
+The output looks similar to the following:
 
 ```console
-Received text delta: Hello
+Enter a message: Please assist the user
+Received text delta: Of
+Received text delta:  course
 Received text delta: !
 Received text delta:  How
 Received 4800 bytes of audio data.
 Received 7200 bytes of audio data.
-Received text delta:  can
 Received 12000 bytes of audio data.
+Received text delta:  can
 Received text delta:  I
 Received text delta:  assist
-Received text delta:  you
 Received 12000 bytes of audio data.
 Received 12000 bytes of audio data.
+Received text delta:  you
 Received text delta:  today
 Received text delta: ?
 Received 12000 bytes of audio data.
-Received 12000 bytes of audio data.
-Received 12000 bytes of audio data.
-Received 12000 bytes of audio data.
-Received 28800 bytes of audio data.
+Received 24000 bytes of audio data.
+Received 36000 bytes of audio data.
+Enter a message: q
 ```
-
-
-
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonでのリアルタイムオーディオクライアントのアップデート"
}
```

### Explanation
この変更は、Pythonを利用したリアルタイムオーディオサポートに関する文書が更新された結果です。主な修正点は以下のとおりです。

1. **クライアントライブラリのインポート変更**: オーディオクライアントライブラリのインポート方法が変更され、`rtclient`から`openai`のライブラリに移行されています。具体的には、`AsyncAzureOpenAI`クラスが新たに導入され、これによりリアルタイム機能の利用が簡素化されています。

2. **Installation Commandの更新**: リアルタイムオーディオクライアントのインストールコマンドが具体的に更新されており、旧来のURLから`pip install openai[realtime]`という明確なコマンドに変更されています。

3. **サンプルコードの改訂**: 新しいコードスニペットが追加され、ユーザーが入力したメッセージに基づいてオーディオとテキストの出力をリアルタイムで行う処理が強化されています。また、対話式の入力処理や、レスポンスの受信処理が改良され、最新のトークンを利用した認証が追加されています。

4. **注意文の追加**: 環境変数に対して設定するべき要件や、キーを用いない認証方法に関する注意喚起が新たに追加され、ユーザーに対する情報がより明確になっています。

全体として、この改訂はPython利用者に対してより効率的で簡単な方法でのリアルタイムオーディオに関する実装手順を提供しており、より良い開発体験を実現することを目指しています。

## articles/ai-services/openai/includes/realtime-typescript.md{#item-eacc9c}

<details>
<summary>Diff</summary>
````diff
@@ -74,7 +74,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
     ```typescript
     import { OpenAIRealtimeWS } from "openai/beta/realtime/ws";
-    import { AzureOpenAI } from "openai/index.mjs";
+    import { AzureOpenAI } from "openai";
     import { DefaultAzureCredential, getBearerTokenProvider } from "@azure/identity";
     
     async function main(): Promise<void> {
@@ -187,7 +187,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
     ```typescript
     import { OpenAIRealtimeWS } from "openai/beta/realtime/ws";
-    import { AzureOpenAI } from "openai/index.mjs";
+    import { AzureOpenAI } from "openai";
     
     async function main(): Promise<void> {
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AzureOpenAIのインポート文の修正"
}
```

### Explanation
この変更は、TypeScriptに関するリアルタイム機能についての文書の更新です。主な修正点は次の通りです。

1. **インポートパスの変更**: `import { AzureOpenAI } from "openai/index.mjs";`の行が削除され、`import { AzureOpenAI } from "openai";`に変更されています。この修正により、インポート文がよりシンプルかつ標準的な形式となり、開発者にとって利用しやすくなっています。

この変更は、TypeScriptユーザーの利便性を向上させることを目的としており、将来のパッケージ構成の変更に対しても柔軟に対応できるよう設計されています。また、文書内での一貫性も保たれ、より明確な情報提供がなされています。全体として、開発者がAzureOpenAIを利用する際の負担を軽減する良い改訂となっています。

## articles/ai-services/openai/includes/studio.md{#item-eeeaff}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.date: 09/19/2023
 
 ## Go to the Azure AI Foundry
 
-Navigate to <a href="https://oai.azure.com/" target="_blank">Azure AI Foundry</a> and sign-in with credentials that have access to your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
+Navigate to the <a href="https://ai.azure.com/" target="_blank">Azure AI Foundry portal</a> and sign-in with credentials that have access to your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
 
 ## Playground
 
@@ -39,7 +39,7 @@ In the Completions playground you can also view Python and curl code samples pre
 
 To use the Azure OpenAI for text summarization in the Completions playground, follow these steps:
 
-1. Sign in to [Azure AI Foundry](https://oai.azure.com).
+1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com).
 1. Select the subscription and OpenAI resource to work with. 
 1. Select **Completions playground** on the landing page.
 1. Select your deployment from the **Deployments** dropdown. If your resource doesn't have a deployment, select **Create a deployment** and then revisit this step.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundry ポータルへのリンクの修正"
}
```

### Explanation
この変更は、Azure AI Foundryに関する文書内のリンクについての更新です。具体的には、以下の内容が修正されています。

1. **リンクURLの更新**: 文書内の「Azure AI Foundry」へのリンクが、`https://oai.azure.com/`から`https://ai.azure.com/`に変更されています。この変更により、より正確なポータルのURLが使用されることになります。

2. **文言の修正**: 同様に、文中の「Azure AI Foundry」の表現が「Azure AI Foundry portal」に更新されており、ポータルであることが明示されています。

この更新は、ユーザーが正確な情報をもとにAzure AI Foundryポータルにアクセスできるようにするためのものであり、情報の明確性と整合性を向上させることを目的としています。全体として、ユーザビリティを向上させるための小規模な改善ですが、重要な修正となっています。

## articles/ai-services/openai/tutorials/fine-tune.md{#item-8f87b5}

<details>
<summary>Diff</summary>
````diff
@@ -44,26 +44,12 @@ In this tutorial you learn how to:
 
 ### Python libraries
 
-# [OpenAI Python 1.x](#tab/python-new)
-
 This tutorial provides examples of some of the latest OpenAI features include seed/events/checkpoints. In order to take advantage of these features, you might need to run `pip install openai --upgrade` to upgrade to the latest release.
 
 ```cmd
 pip install openai requests tiktoken numpy
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-[!INCLUDE [Deprecation](../includes/deprecation.md)]
-
-If you haven't already, you need to install the following libraries:
-
-```cmd
-pip install "openai==0.28.1" requests tiktoken numpy
-```
-
----
-
 [!INCLUDE [get-key-endpoint](../includes/get-key-endpoint.md)]
 
 ### Environment variables
@@ -295,8 +281,6 @@ p5 / p95: 10.7, 19.999999999999996
 
 ## Upload fine-tuning files
 
-# [OpenAI Python 1.x](#tab/python-new)
-
 ```python
 # Upload fine-tuning files
 
@@ -306,7 +290,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
   api_key = os.getenv("AZURE_OPENAI_API_KEY"),
-  api_version = "2024-08-01-preview"  # This API version or later is required to access seed/events/checkpoint features
+  api_version = "2025-02-01-preview"  
 )
 
 training_file_name = 'training_set.jsonl'
@@ -328,40 +312,6 @@ print("Training file ID:", training_file_id)
 print("Validation file ID:", validation_file_id)
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-```Python
-# Upload fine-tuning files
-
-import openai
-import os
-
-openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
-openai.api_base =  os.getenv("AZURE_OPENAI_ENDPOINT")
-openai.api_type = 'azure'
-openai.api_version = '2023-05-01' 
-
-training_file_name = 'training_set.jsonl'
-validation_file_name = 'validation_set.jsonl'
-
-# Upload the training and validation dataset files to Azure OpenAI with the SDK.
-
-training_response = openai.File.create(
-    file = open(training_file_name, "rb"), purpose="fine-tune", user_provided_filename="training_set.jsonl"
-)
-training_file_id = training_response["id"]
-
-validation_response = openai.File.create(
-    file = open(validation_file_name, "rb"), purpose="fine-tune", user_provided_filename="validation_set.jsonl"
-)
-validation_file_id = validation_response["id"]
-
-print("Training file ID:", training_file_id)
-print("Validation file ID:", validation_file_id)
-```
-
----
-
 **Output:**
 
 ```output
@@ -373,8 +323,6 @@ Validation file ID: file-8556c3bb41b7416bb7519b47fcd1dd6b
 
 Now that the fine-tuning files are successfully uploaded you can submit your fine-tuning training job:
 
-# [OpenAI Python 1.x](#tab/python-new)
-
 In this example, we're also passing the seed parameter. The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but can differ in rare cases. If a seed isn't specified, one is generated for you.
 
 ```python
@@ -397,31 +345,7 @@ print("Status:", response.status)
 print(response.model_dump_json(indent=2))
 ```
 
-
-# [OpenAI Python 0.28.1](#tab/python)
-
-```python
-# Submit fine-tuning training job
-
-response = openai.FineTuningJob.create(
-    training_file = training_file_id,
-    validation_file = validation_file_id,
-    model = "gpt-4o-mini-2024-07-18",
-)
-
-job_id = response["id"]
-
-# You can use the job ID to monitor the status of the fine-tuning job.
-# The fine-tuning job will take some time to start and complete.
-
-print("Job ID:", response["id"])
-print("Status:", response["status"])
-print(response)
-```
-
----
-
-**Python 1.x Output:**
+**Output:**
 
 ```json
 Job ID: ftjob-900fcfc7ea1d4360a9f0cb1697b4eaa6
@@ -455,9 +379,6 @@ Status: pending
 
 If you would like to poll the training job status until it's complete, you can run:
 
-
-# [OpenAI Python 1.x](#tab/python-new)
-
 ```python
 # Track training status
 
@@ -490,43 +411,7 @@ response = client.fine_tuning.jobs.list()
 print(f'Found {len(response.data)} fine-tune jobs.')
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-```python
-# Track training status
-
-from IPython.display import clear_output
-import time
-
-start_time = time.time()
-
-# Get the status of our fine-tuning job.
-response = openai.FineTuningJob.retrieve(job_id)
-
-status = response["status"]
-
-# If the job isn't done yet, poll it every 10 seconds.
-while status not in ["succeeded", "failed"]:
-    time.sleep(10)
-
-    response = openai.FineTuningJob.retrieve(job_id)
-    print(response)
-    print("Elapsed time: {} minutes {} seconds".format(int((time.time() - start_time) // 60), int((time.time() - start_time) % 60)))
-    status = response["status"]
-    print(f'Status: {status}')
-    clear_output(wait=True)
-
-print(f'Fine-tuning job {job_id} finished with status: {status}')
-
-# List all fine-tuning jobs for this resource.
-print('Checking other fine-tune jobs for this resource.')
-response = openai.FineTuningJob.list()
-print(f'Found {len(response["data"])} fine-tune jobs.')
-```
-
----
-
-**Python 1.x Output:**
+**Output:**
 
 ```json
 Job ID: ftjob-900fcfc7ea1d4360a9f0cb1697b4eaa6
@@ -570,20 +455,12 @@ API version: `2024-08-01-preview` or later is required for this command.
 
 While not necessary to complete fine-tuning, it can be helpful to examine the individual fine-tuning events that were generated during training. The full training results can also be examined after training is complete in the [training results file](../how-to/fine-tuning.md#analyze-your-customized-model).
 
-# [OpenAI Python 1.x](#tab/python-new)
-
 ```python
 response = client.fine_tuning.jobs.list_events(fine_tuning_job_id=job_id, limit=10)
 print(response.model_dump_json(indent=2))
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-This command isn't available in the 0.28.1 OpenAI Python library. Upgrade to the latest release.
-
----
-
-**Python 1.x Output:**
+**Output:**
 
 ```json
 {
@@ -734,20 +611,12 @@ API version: `2024-08-01-preview` or later is required for this command.
 
 When each training epoch completes a checkpoint is generated. A checkpoint is a fully functional version of a model which can both be deployed and used as the target model for subsequent fine-tuning jobs. Checkpoints can be useful, as they can provide a snapshot of your model prior to overfitting having occurred. When a fine-tuning job completes, you have the three most recent versions of the model available to deploy. The final epoch will be represented by your fine-tuned model, the previous two epochs are available as checkpoints.
 
-# [OpenAI Python 1.x](#tab/python-new)
-
 ```python
 response = client.fine_tuning.jobs.checkpoints.list(job_id)
 print(response.model_dump_json(indent=2))
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-This command isn't available in the 0.28.1 OpenAI Python library. Upgrade to the latest release.
-
----
-
-**Python 1.x Output:**
+**Output:**
 
 ```json
 {
@@ -813,8 +682,6 @@ This command isn't available in the 0.28.1 OpenAI Python library. Upgrade to the
 
 To get the final results, run the following:
 
-# [OpenAI Python 1.x](#tab/python-new)
-
 ```python
 # Retrieve fine_tuned_model name
 
@@ -824,19 +691,6 @@ print(response.model_dump_json(indent=2))
 fine_tuned_model = response.fine_tuned_model
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-```python
-# Retrieve fine_tuned_model name
-
-response = openai.FineTuningJob.retrieve(job_id)
-
-print(response)
-fine_tuned_model = response["fine_tuned_model"]
-```
-
----
-
 ## Deploy fine-tuned model
 
 Unlike the previous Python SDK commands in this tutorial, since the introduction of the quota feature, model deployment must be done using the [REST API](/rest/api/aiservices/accountmanagement/deployments/create-or-update?tabs=HTTP), which requires separate authorization, a different API path, and a different API version.
@@ -866,7 +720,7 @@ resource_group = "<YOUR_RESOURCE_GROUP_NAME>"
 resource_name = "<YOUR_AZURE_OPENAI_RESOURCE_NAME>"
 model_deployment_name = "gpt-4o-mini-2024-07-18-ft" # Custom deployment name you chose for your fine-tuning model
 
-deploy_params = {'api-version': "2023-05-01"}
+deploy_params = {'api-version': "2024-10-01"} # Control plane API version
 deploy_headers = {'Authorization': 'Bearer {}'.format(token), 'Content-Type': 'application/json'}
 
 deploy_data = {
@@ -900,8 +754,6 @@ It isn't uncommon for this process to take some time to complete when dealing wi
 
 After your fine-tuned model is deployed, you can use it like any other deployed model in either the [Chat Playground of Azure AI Foundry portal](https://ai.azure.com), or via the chat completion API. For example, you can send a chat completion call to your deployed model, as shown in the following Python example. You can continue to use the same parameters with your customized model, such as temperature and max_tokens, as you can with other deployed models.
 
-# [OpenAI Python 1.x](#tab/python-new)
-
 ```python
 # Use the deployed customized model
 
@@ -911,7 +763,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
   api_key = os.getenv("AZURE_OPENAI_API_KEY"),
-  api_version = "2024-06-01"
+  api_version = "2024-10-21"
 )
 
 response = client.chat.completions.create(
@@ -927,35 +779,6 @@ response = client.chat.completions.create(
 print(response.choices[0].message.content)
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-```python
-# Use the deployed customized model
-
-import os
-import openai
-
-openai.api_type = "azure"
-openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
-openai.api_version = "2024-06-01"
-openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
-
-response = openai.ChatCompletion.create(
-    engine = "gpt-4o-mini-2024-07-18-ft", # engine = "Custom deployment name you chose for your fine-tuning model"
-    messages = [
-        {"role": "system", "content": "You are a helpful assistant."},
-        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
-        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
-        {"role": "user", "content": "Do other Azure AI services support this too?"}
-    ]
-)
-
-print(response)
-print(response['choices'][0]['message']['content'])
-```
-
----
-
 ## Delete deployment
 
 Unlike other types of Azure OpenAI models, fine-tuned/customized models have [an hourly hosting cost](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing) associated with them once they're deployed. It's **strongly recommended** that once you're done with this tutorial and have tested a few chat completion calls against your fine-tuned model, that you **delete the model deployment**.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "ファインチューニングチュートリアルの大幅な更新"
}
```

### Explanation
この変更は、ファインチューニングに関するチュートリアル文書の大幅な更新を示しており、主に以下の要素が修正されています。

1. **コンテンツの大幅な削減**: 文書内で180行以上の削除が行われ、新しくなった内容が追加されています。これにより、旧バージョンのOpenAI Pythonライブラリに関する古い情報が取り除かれ、新しいバージョンに焦点が当てられています。

2. **APIバージョンの更新**: 使用されるAPIバージョンが、例えば`"2024-08-01-preview"`から`"2025-02-01-preview"`に更新されています。これにより、最新の機能や改善点を考慮した正しいバージョンが指定されています。

3. **コードサンプルの削除と統合**: 古いコードサンプルが削除され、新しいバージョンのライブラリに基づくコード例が挿入されています。これにより、ユーザーは新しいライブラリに準拠した正しい実装方法を学ぶことができます。

4. **チュートリアルの流れの見直し**: チュートリアル自体の構成も見直され、新しい手順や説明が追加されているため、ユーザーはより分かりやすく、直感的にファインチューニングの流れを把握できるようになっています。

この更新内容は、ファインチューニングを行う際の新しい手法や設定についての情報を具体的に示すことで、開発者が効果的に新しい機能を利用できるようにするためのものです。全体として、ユーザー体験の向上を図るための重要な変更です。


