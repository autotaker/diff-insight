---
date: '2025-01-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f3626a8...MicrosoftDocs:0fcd6d7
summary: このコード変更は、Azureドキュメントの小規模な更新を目的としており、文書の明瞭性と新機能の追加、認証に関する注意事項、地域可用性の情報、およびモデル利用に関する情報を強化しています。具体的には、ドキュメントインテリジェンスの「検索可能なPDF」機能の追加や、Phi-4モデルのサーバーレスAPIエンドポイントに関する詳細情報が含まれています。また、一部の機能が削除され、文言や警告メッセージが改善されました。全体として、これらの変更はAzureドキュメントの質と可読性を向上させ、ユーザーエクスペリエンスを強化することを目指しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f3626a8...MicrosoftDocs:0fcd6d7){target="_blank"}

# ハイライト
このコード変更はAzureドキュメントの小規模な更新を中心に据えており、特にドキュメントの明瞭性の向上と新しい機能の追加、認証の注意事項、地域可用性の情報、モデル利用に関する情報の強化に焦点を当てています。

## 新機能
- ドキュメントインテリジェンスの「検索可能なPDF」機能がアドオンとして追加されました。
- Phi-4モデルのサーバーレスAPIエンドポイントのデプロイメントについての詳細が追加されました。
- Azure AIコンテンツ安全性の機能が新たに紹介されています。

## 破壊的変更
- 目次から「Completions」に関連する項目が削除されました。
- モデル推論APIのリストから「Text completions」が削除されました。

## その他の更新
- 文言や警告メッセージの改善、認証に関する注意点の明確化。
- 地域可用性に関する新たな情報とテーブルの追加。
- 不要な情報の削除とスムーズな流れを目的とした文言の調整。
- 一貫性を保つためのフォーマット修正。

# 洞察
今回の変更は、Azureドキュメントの質を向上させるための一連の措置として、細部にわたって文書全体の可読性と技術的な正確性を強化することを目的としています。 

特に、ドキュメントインテリジェンスの新しい機能として「検索可能なPDF」機能を導入することにより、ユーザーに対して新しい付加価値を提供しています。一方で、Phi-4モデルのサーバーレスAPIエンドポイントを詳細に記述することで、利用者により柔軟なデプロイメントオプションを提供し、エンタープライズ環境においても安心して利用できる情報基盤を構築しています。

「Text completions」が推論APIリストや目次から削除されたことは、恐らくこの機能が再評価された結果であり、Azureが提供するサービスの最新情報として、ユーザーへの信頼性を維持するための変更である可能性があります。また、地域可用性に関する情報を強化することで、計画段階での地理的な考慮事項を明確にし、利用者に最適なシステムの選択を支援することを目的としています。

これらの更新を通じて、Azure AI Studioは機能性とユーザー体験の両面でさらに進化し、信頼できるプラットフォームとしての地位を強固にしています。ドキュメントの改善はシステムの利用しやすさを高め、技術者や意思決定者にとって重要なリソースとなるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [add-on-capabilities.md](#item-96ed69) | minor update | ドキュメントインテリジェンスのアドオン機能の更新 | modified | 6 | 6 | 12 | 
| [deploy-models-phi-3-5-vision.md](#item-8d6d7d) | minor update | Phi-3.5モデルのデプロイ方法の更新 | modified | 24 | 27 | 51 | 
| [deploy-models-phi-3-vision.md](#item-bd5aae) | minor update | Phi-3ビジョンモデルのデプロイ方法の更新 | modified | 18 | 21 | 39 | 
| [deploy-models-phi-3.md](#item-47e305) | minor update | Phi-3モデルのデプロイ方法に関する更新 | modified | 31 | 34 | 65 | 
| [deploy-models-phi-4.md](#item-c40212) | minor update | Phi-4モデルのデプロイに関する更新 | modified | 249 | 27 | 276 | 
| [model-catalog-overview.md](#item-278001) | minor update | モデルカタログの概要に関する更新 | modified | 1 | 1 | 2 | 
| [region-availability-maas.md](#item-35d79c) | minor update | モデルの地域可用性に関する更新 | modified | 8 | 1 | 9 | 
| [reference-model-inference-api.md](#item-9fe240) | minor update | モデル推論APIの参照に関する修正 | modified | 0 | 1 | 1 | 
| [region-support.md](#item-d402e1) | minor update | 地域サポートに関するドキュメントの更新 | modified | 13 | 21 | 34 | 
| [toc.yml](#item-2745cd) | minor update | 目次からの項目の削除 | modified | 0 | 2 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/concept/add-on-capabilities.md{#item-96ed69}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jaep3347
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 11/19/2024
+ms.date: 01/15/2025
 ms.author: lajanuar
 monikerRange: '>=doc-intel-3.1.0'
 ---
@@ -64,14 +64,14 @@ Document Intelligence supports more sophisticated and modular analysis capabilit
 
 |Add-on Capability| Add-On/Free|**2024-11-30 (GA)**|[`2023-07-31` (GA)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)|[`2022-08-31` (GA)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)|[v2.1 (GA)](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)|
 |----------------|-----------|---|--|---|---|
-|Font property extraction|Add-On| ✔️| ✔️| n/a| n/a|
-|Formula extraction|Add-On| ✔️| ✔️| n/a| n/a|
-|High resolution extraction|Add-On| ✔️| ✔️| n/a| n/a|
 |Barcode extraction|Free| ✔️| ✔️| n/a| n/a|
 |Language detection|Free| ✔️| ✔️| n/a| n/a|
 |Key value pairs|Free| ✔️|n/a|n/a| n/a|
-|Query fields|Add-On*| ✔️|n/a|n/a| n/a|
-|Searhable pdf|Add-On**| ✔️|n/a|n/a| n/a|
+|Searchable PDF|Free| ✔️|n/a|n/a| n/a|
+|Font property extraction|**Add-On**| ✔️| ✔️| n/a| n/a|
+|Formula extraction|**Add-On**| ✔️| ✔️| n/a| n/a|
+|High resolution extraction|**Add-On**| ✔️| ✔️| n/a| n/a|
+|Query fields|**Add-On**| ✔️|n/a|n/a| n/a|
 
 ✱ Add-On - Query fields are priced differently than the other add-on features. See [pricing](https://azure.microsoft.com/pricing/details/ai-document-intelligence/) for details. </br>
 ** Add-On - Searchable pdf is available only with Read model as an add-on feature. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのアドオン機能の更新"
}
```

### Explanation
この変更は、Azure Document Intelligence のアドオン機能に関連するドキュメンテーションの小さな更新を示しています。具体的には、文書のメタデータである日付が2024年11月19日から2025年1月15日に変更され、いくつかのアドオン機能がハイライトされています。これにより、情報の最新性が保たれ、ユーザーに対する明確なガイダンスが提供されています。

変更に伴い、アドオン機能としての「フォントプロパティ抽出」、「数式抽出」、「高解像度抽出」などが強調され、新たに「検索可能なPDF」機能が「アドオン」として記載されました。テーブル内の一部の機能の状態も修正され、情報が明確に表現されています。これらの更新は、利用者が機能や価格の違いを理解しやすくするための重要な手直しです。

## articles/ai-studio/how-to/deploy-models-phi-3-5-vision.md{#item-8d6d7d}

<details>
<summary>Diff</summary>
````diff
@@ -113,7 +113,7 @@ client = ChatCompletionsClient(
 ```
 
 > [!NOTE]
-> Currently, serverless API endpoints do not support using Microsoft Entra ID for authentication.
+> Currently, serverless API endpoints don't support using Microsoft Entra ID for authentication.
 
 ### Get the model's capabilities
 
@@ -227,7 +227,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormat
+from azure.ai.inference.models import ChatCompletionsResponseFormatText
 
 response = client.complete(
     messages=[
@@ -240,12 +240,12 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
+    response_format={ "type": ChatCompletionsResponseFormatText() },
 )
 ```
 
 > [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -272,10 +272,10 @@ The following extra parameters can be passed to Phi-3.5 chat model with vision:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `bool` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `int` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ### Apply content safety
@@ -479,7 +479,7 @@ const client = new ModelClient(
 ```
 
 > [!NOTE]
-> Currently, serverless API endpoints do not support using Microsoft Entra ID for authentication.
+> Currently, serverless API endpoints don't support using Microsoft Entra ID for authentication.
 
 ### Get the model's capabilities
 
@@ -625,7 +625,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -657,10 +657,10 @@ The following extra parameters can be passed to Phi-3.5 chat model with vision:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `bool` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `int` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ### Apply content safety
@@ -891,7 +891,7 @@ client = new ChatCompletionsClient(
 ```
 
 > [!NOTE]
-> Currently, serverless API endpoints do not support using Microsoft Entra ID for authentication.
+> Currently, serverless API endpoints don't support using Microsoft Entra ID for authentication.
 
 ### Get the model's capabilities
 
@@ -1037,7 +1037,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
 > [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1066,10 +1066,10 @@ The following extra parameters can be passed to Phi-3.5 chat model with vision:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `bool` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `int` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ### Apply content safety
@@ -1239,7 +1239,7 @@ First, create the client to consume the model. The following code uses an endpoi
 When you deploy the model to a self-hosted online endpoint with **Microsoft Entra ID** support, you can use the following code snippet to create a client.
 
 > [!NOTE]
-> Currently, serverless API endpoints do not support using Microsoft Entra ID for authentication.
+> Currently, serverless API endpoints don't support using Microsoft Entra ID for authentication.
 
 ### Get the model's capabilities
 
@@ -1446,7 +1446,7 @@ Explore other parameters that you can specify in the inference client. For a ful
 ```
 
 > [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1485,10 +1485,10 @@ The following extra parameters can be passed to Phi-3.5 chat model with vision:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `bool` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `int` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ### Apply content safety
@@ -1542,7 +1542,7 @@ Phi-3.5-vision-Instruct can reason across text and images and generate text comp
 To see this capability, download an image and encode the information as `base64` string. The resulting data should be inside of a [data URL](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs):
 
 > [!TIP]
-> You will need to construct the data URL using an scripting or programming language. This tutorial use [this sample image](../media/how-to/sdks/small-language-models-chart-example.jpg) in JPEG format. A data URL has a format as follows: `data:image/jpg;base64,0xABCDFGHIJKLMNOPQRSTUVWXYZ...`.
+> You need to construct the data URL using a scripting or programming language. This article uses [this sample image](../media/how-to/sdks/small-language-models-chart-example.jpg) in JPEG format. A data URL has a format as follows: `data:image/jpg;base64,0xABCDFGHIJKLMNOPQRSTUVWXYZ...`.
 
 Visualize the image:
 
@@ -1613,14 +1613,11 @@ For more examples of how to use Phi-3 family models, see the following examples
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
-| CURL request                              | Bash              | [Link](https://aka.ms/phi-3/webrequests-sample)         |
-| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples) |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
-| Python web requests                       | Python            | [Link](https://aka.ms/phi-3/webrequests-sample)         |
-| OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/phi-3/openaisdk)                  |
-| LangChain                                 | Python            | [Link](https://aka.ms/phi-3/langchain-sample)           |
-| LiteLLM                                   | Python            | [Link](https://aka.ms/phi-3/litellm-sample)             | 
+| LangChain                                 | Python            | [Link](https://aka.ms/azureai/langchain)           |
+| Llama-Index                               | Python            | [Link](https://aka.ms/azureai/llamaindex)             | 
 
 
 ## Cost and quota considerations for Phi-3 family models deployed as serverless API endpoints
@@ -1631,7 +1628,7 @@ Quota is managed per deployment. Each deployment has a rate limit of 200,000 tok
 
 Phi-3 family models deployed to managed compute are billed based on core hours of the associated compute instance. The cost of the compute instance is determined by the size of the instance, the number of instances running, and the run duration.
 
-It is a good practice to start with a low number of instances and scale up as needed. You can monitor the cost of the compute instance in the Azure portal.
+It's a good practice to start with a low number of instances and scale up as needed. You can monitor the cost of the compute instance in the Azure portal.
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3.5モデルのデプロイ方法の更新"
}
```

### Explanation
この変更は、Azure AI Studio における Phi-3.5 モデルのデプロイ方法に関するドキュメンテーションの小規模な更新を表しています。主な変更点として、文言の調整といくつかの定義を明確にするためのコード行の修正があります。

特に、Microsoft Entra ID に関する注意書きの表現が改善され、使用していない箇所でのコードが更新されました。これには、新しいインポート文や、レスポンスのフォーマット指定に関する変更が含まれています。たとえば、 `ChatCompletionsResponseFormat` から `ChatCompletionsResponseFormatText` への変更が行われ、さらにレスポンスのフォーマットが適切に指定されるようになりました。

他にも、ロギットバイアス（`logit_bias`）や、プロンプトの使用に関する説明がより明確にされ、各パラメータの詳細説明が整備されています。非推奨の情報の削除や文言の整理により、ドキュメント全体の可読性と正確性が向上しました。全体として、この更新はユーザーがPhi-3.5モデルをより理解しやすく、効果的にデプロイできるようにすることを目的としています。

## articles/ai-studio/how-to/deploy-models-phi-3-vision.md{#item-bd5aae}

<details>
<summary>Diff</summary>
````diff
@@ -233,7 +233,7 @@ response = client.complete(
 ```
 
 > [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -260,10 +260,10 @@ The following extra parameters can be passed to Phi-3 chat model with vision:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `bool` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `int` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ## Use chat completions with images
@@ -565,7 +565,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -597,10 +597,10 @@ The following extra parameters can be passed to Phi-3 chat model with vision:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `bool` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `int` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ## Use chat completions with images
@@ -923,7 +923,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
 > [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -952,10 +952,10 @@ The following extra parameters can be passed to Phi-3 chat model with vision:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `bool` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `int` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ## Use chat completions with images
@@ -1278,7 +1278,7 @@ Explore other parameters that you can specify in the inference client. For a ful
 ```
 
 > [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1317,10 +1317,10 @@ The following extra parameters can be passed to Phi-3 chat model with vision:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `object` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `bool` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `int` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ## Use chat completions with images
@@ -1333,7 +1333,7 @@ Phi-3-vision-128k-Instruct can reason across text and images and generate text c
 To see this capability, download an image and encode the information as `base64` string. The resulting data should be inside of a [data URL](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs):
 
 > [!TIP]
-> You will need to construct the data URL using an scripting or programming language. This tutorial use [this sample image](../media/how-to/sdks/small-language-models-chart-example.jpg) in JPEG format. A data URL has a format as follows: `data:image/jpg;base64,0xABCDFGHIJKLMNOPQRSTUVWXYZ...`.
+> You need to construct the data URL using a scripting or programming language. This article uses [this sample image](../media/how-to/sdks/small-language-models-chart-example.jpg) in JPEG format. A data URL has a format as follows: `data:image/jpg;base64,0xABCDFGHIJKLMNOPQRSTUVWXYZ...`.
 
 Visualize the image:
 
@@ -1404,21 +1404,18 @@ For more examples of how to use Phi-3 family models, see the following examples
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
-| CURL request                              | Bash              | [Link](https://aka.ms/phi-3/webrequests-sample)         |
-| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)                  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples) |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
-| Python web requests                       | Python            | [Link](https://aka.ms/phi-3/webrequests-sample)         |
-| OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/phi-3/openaisdk)                  |
-| LangChain                                 | Python            | [Link](https://aka.ms/phi-3/langchain-sample)           |
-| LiteLLM                                   | Python            | [Link](https://aka.ms/phi-3/litellm-sample)             | 
+| LangChain                                 | Python            | [Link](https://aka.ms/azureai/langchain)           |
+| Llama-Index                               | Python            | [Link](https://aka.ms/azureai/llamaindex)             |  
 
 
 ## Cost and quota considerations for Phi-3 family models deployed to managed compute
 
 Phi-3 family models deployed to managed compute are billed based on core hours of the associated compute instance. The cost of the compute instance is determined by the size of the instance, the number of instances running, and the run duration.
 
-It is a good practice to start with a low number of instances and scale up as needed. You can monitor the cost of the compute instance in the Azure portal.
+It's a good practice to start with a low number of instances and scale up as needed. You can monitor the cost of the compute instance in the Azure portal.
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3ビジョンモデルのデプロイ方法の更新"
}
```

### Explanation
この変更は、Azure AI Studio における Phi-3 ビジョンモデルのデプロイ手順に関するドキュメントの小規模な更新を示しています。主なポイントは、コード内の文言の微調整と一部の説明の明確化です。

具体的には、警告メッセージ内の表記が改善され、「JSON出力フォーマットがサポートされない」という内容の表現が一貫して修正されました。また、`logit_bias` の説明がより簡潔化され、理解しやすくなっています。他の引数に関する注意事項も明確に記載されています。加えて、`n` パラメータに関する説明も料金に関する情報が調整されました。

最後に、Phi-3モデルの利用例が整理され、一部のリンクが最新のものに更新されています。これにより、ユーザーがモデルを効果的にデプロイ実行し、潜在的なコストに対応しやすくなっています。全体として、この更新は文書の明瞭性と一貫性を向上させ、ユーザーがモデルを活用する際の理解を助けることを目指しています。

## articles/ai-studio/how-to/deploy-models-phi-3.md{#item-47e305}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ Phi-3.5 models are lightweight, state-of-the-art open models. These models were
 
 Phi-3.5 Mini uses 3.8B parameters, and is a dense decoder-only transformer model using the same tokenizer as Phi-3 Mini.
 
-Phi-3.5 MoE (mixture-of-expert) uses 16x3.8B parameters with 6.6B active parameters when using 2 experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
+Phi-3.5 MoE (mixture-of-expert) uses 16x3.8B parameters with 6.6B active parameters when using two experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
 
 The models underwent a rigorous enhancement process, incorporating both supervised fine-tuning, proximal policy optimization, and direct preference optimization to ensure precise instruction adherence and robust safety measures. When assessed against benchmarks that test common sense, language understanding, math, code, long context and logical reasoning, Phi-3.5 models showcased robust and state-of-the-art performance among models with less than 13 billion parameters.
 
@@ -147,7 +147,7 @@ client = ChatCompletionsClient(
 ```
 
 > [!NOTE]
-> Currently, serverless API endpoints do not support using Microsoft Entra ID for authentication.
+> Currently, serverless API endpoints don't support using Microsoft Entra ID for authentication.
 
 ### Get the model's capabilities
 
@@ -189,7 +189,7 @@ response = client.complete(
 ```
 
 > [!NOTE]
-> Phi-3.5-Mini-Instruct, Phi-3.5-MoE-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> Phi-3.5-Mini-Instruct, Phi-3.5-MoE-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct, and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -261,7 +261,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormat
+from azure.ai.inference.models import ChatCompletionsResponseFormatText
 
 response = client.complete(
     messages=[
@@ -279,7 +279,7 @@ response = client.complete(
 ```
 
 > [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -306,10 +306,10 @@ The following extra parameters can be passed to Phi-3 family chat models:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ### Apply content safety
@@ -363,7 +363,7 @@ Phi-3.5 models are lightweight, state-of-the-art open models. These models were
 
 Phi-3.5 Mini uses 3.8B parameters, and is a dense decoder-only transformer model using the same tokenizer as Phi-3 Mini.
 
-Phi-3.5 MoE (mixture-of-expert) uses 16x3.8B parameters with 6.6B active parameters when using 2 experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
+Phi-3.5 MoE (mixture-of-expert) uses 16x3.8B parameters with 6.6B active parameters when using two experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
 
 The models underwent a rigorous enhancement process, incorporating both supervised fine-tuning, proximal policy optimization, and direct preference optimization to ensure precise instruction adherence and robust safety measures. When assessed against benchmarks that test common sense, language understanding, math, code, long context and logical reasoning, Phi-3.5 models showcased robust and state-of-the-art performance among models with less than 13 billion parameters.
 
@@ -473,7 +473,7 @@ const client = new ModelClient(
 ```
 
 > [!NOTE]
-> Currently, serverless API endpoints do not support using Microsoft Entra ID for authentication.
+> Currently, serverless API endpoints don't support using Microsoft Entra ID for authentication.
 
 ### Get the model's capabilities
 
@@ -517,7 +517,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!NOTE]
-> Phi-3.5-Mini-Instruct, Phi-3.5-MoE-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> Phi-3.5-Mini-Instruct, Phi-3.5-MoE-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct, and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -619,7 +619,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -651,10 +651,10 @@ The following extra parameters can be passed to Phi-3 family chat models:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ### Apply content safety
@@ -714,7 +714,7 @@ Phi-3.5 models are lightweight, state-of-the-art open models. These models were
 
 Phi-3.5 Mini uses 3.8B parameters, and is a dense decoder-only transformer model using the same tokenizer as Phi-3 Mini.
 
-Phi-3.5 MoE (mixture-of-expert) uses 16x3.8B parameters with 6.6B active parameters when using 2 experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
+Phi-3.5 MoE (mixture-of-expert) uses 16x3.8B parameters with 6.6B active parameters when using two experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
 
 The models underwent a rigorous enhancement process, incorporating both supervised fine-tuning, proximal policy optimization, and direct preference optimization to ensure precise instruction adherence and robust safety measures. When assessed against benchmarks that test common sense, language understanding, math, code, long context and logical reasoning, Phi-3.5 models showcased robust and state-of-the-art performance among models with less than 13 billion parameters.
 
@@ -839,7 +839,7 @@ client = new ChatCompletionsClient(
 ```
 
 > [!NOTE]
-> Currently, serverless API endpoints do not support using Microsoft Entra ID for authentication.
+> Currently, serverless API endpoints don't support using Microsoft Entra ID for authentication.
 
 ### Get the model's capabilities
 
@@ -882,7 +882,7 @@ Response<ChatCompletions> response = client.Complete(requestOptions);
 ```
 
 > [!NOTE]
-> Phi-3.5-Mini-Instruct, Phi-3.5-MoE-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> Phi-3.5-Mini-Instruct, Phi-3.5-MoE-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct, and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -985,7 +985,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
 > [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1014,10 +1014,10 @@ The following extra parameters can be passed to Phi-3 family chat models:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ### Apply content safety
@@ -1077,7 +1077,7 @@ Phi-3.5 models are lightweight, state-of-the-art open models. These models were
 
 Phi-3.5 Mini uses 3.8B parameters, and is a dense decoder-only transformer model using the same tokenizer as Phi-3 Mini.
 
-Phi-3.5 MoE (mixture-of-expert) uses 16x3.8B parameters with 6.6B active parameters when using 2 experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
+Phi-3.5 MoE (mixture-of-expert) uses 16x3.8B parameters with 6.6B active parameters when using two experts. The model is a mixture-of-expert decoder-only transformer model, using a tokenizer with vocabulary size of 32,064.
 
 The models underwent a rigorous enhancement process, incorporating both supervised fine-tuning, proximal policy optimization, and direct preference optimization to ensure precise instruction adherence and robust safety measures. When assessed against benchmarks that test common sense, language understanding, math, code, long context and logical reasoning, Phi-3.5 models showcased robust and state-of-the-art performance among models with less than 13 billion parameters.
 
@@ -1156,7 +1156,7 @@ First, create the client to consume the model. The following code uses an endpoi
 When you deploy the model to a self-hosted online endpoint with **Microsoft Entra ID** support, you can use the following code snippet to create a client.
 
 > [!NOTE]
-> Currently, serverless API endpoints do not support using Microsoft Entra ID for authentication.
+> Currently, serverless API endpoints don't support using Microsoft Entra ID for authentication.
 
 ### Get the model's capabilities
 
@@ -1200,7 +1200,7 @@ The following example shows how you can create a basic chat completions request
 ```
 
 > [!NOTE]
-> Phi-3.5-Mini-Instruct, Phi-3.5-MoE-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> Phi-3.5-Mini-Instruct, Phi-3.5-MoE-Instruct, Phi-3-mini-4k-Instruct, Phi-3-mini-128k-Instruct, Phi-3-small-8k-Instruct, Phi-3-small-128k-Instruct, and Phi-3-medium-128k-Instruct don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -1363,7 +1363,7 @@ Explore other parameters that you can specify in the inference client. For a ful
 ```
 
 > [!WARNING]
-> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-3 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1402,10 +1402,10 @@ The following extra parameters can be passed to Phi-3 family chat models:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ### Apply content safety
@@ -1457,14 +1457,11 @@ For more examples of how to use Phi-3 family models, see the following examples
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
-| CURL request                              | Bash              | [Link](https://aka.ms/phi-3/webrequests-sample)         |
-| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)                  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples) |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
-| Python web requests                       | Python            | [Link](https://aka.ms/phi-3/webrequests-sample)         |
-| OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/phi-3/openaisdk)                  |
-| LangChain                                 | Python            | [Link](https://aka.ms/phi-3/langchain-sample)           |
-| LiteLLM                                   | Python            | [Link](https://aka.ms/phi-3/litellm-sample)             | 
+| LangChain                                 | Python            | [Link](https://aka.ms/azureai/langchain)           |
+| Llama-Index                               | Python            | [Link](https://aka.ms/azureai/llamaindex)             |  
 
 
 ## Cost and quota considerations for Phi-3 family models deployed as serverless API endpoints
@@ -1475,11 +1472,11 @@ Quota is managed per deployment. Each deployment has a rate limit of 200,000 tok
 
 Phi-3 family models deployed to managed compute are billed based on core hours of the associated compute instance. The cost of the compute instance is determined by the size of the instance, the number of instances running, and the run duration.
 
-It is a good practice to start with a low number of instances and scale up as needed. You can monitor the cost of the compute instance in the Azure portal.
+It's a good practice to start with a low number of instances and scale up as needed. You can monitor the cost of the compute instance in the Azure portal.
 
 ## Sample notebook
 
-You can use this [sample notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/finetuning/standalone/chat-completion/chat_completion_with_model_as_service.ipynb)  to create a standalone fine-tuning job to enhance a model's ability to summarize dialogues between two people using the Samsum dataset. The training data utilized is the ultrachat_200k dataset, which is divided into four splits suitable for supervised fine-tuning (sft) and generation ranking (gen). The notebook employs the available Azure AI models for the chat-completion task (If you would like to use a different model than what's used in the notebook, you can replace the model name). The notebook includes setting up prerequisites, selecting a model to fine-tune, creating training and validation datasets, configuring and submitting the fine-tuning job, and finally, creating a serverless deployment using the fine-tuned model for sample inference.
+You can use this [sample notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/finetuning/standalone/chat-completion/chat_completion_with_model_as_service.ipynb)  to create a standalone fine-tuning job to enhance a model's ability to summarize dialogues between two people using the `Samsum` dataset. The training data utilized is the `ultrachat_200k` dataset, which is divided into four splits suitable for supervised fine-tuning (sft) and generation ranking (gen). The notebook employs the available Azure AI models for the chat-completion task (If you would like to use a different model than what's used in the notebook, you can replace the model name). The notebook includes setting up prerequisites, selecting a model to fine-tune, creating training and validation datasets, configuring and submitting the fine-tuning job, and finally, creating a serverless deployment using the fine-tuned model for sample inference.
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3モデルのデプロイ方法に関する更新"
}
```

### Explanation
この変更は、Azure AI Studio における Phi-3 モデルのデプロイ手順のドキュメントに関する小規模な更新を示しています。主な改訂は、文言の改善といくつかの技術的な詳細の修正です。

具体的には、以下のような変更が行われました：
- Phi-3.5 MoE（Mixture-of-Expert）モデルの説明内で、"2"という数字が"two"に修正され、より明確な表現となっています。
- 複数のノートと警告メッセージにおける表現が一貫性向上のために調整され、「サーバーレス API エンドポイントが Microsoft Entra ID 認証をサポートしていない」という情報が簡潔になりました。
- JSON出力フォーマットに関する警告が統一された文体になり、一貫性があります。
- 一部のパラメータ説明が明瞭化され、例えば `logit_bias` の詳細が一層クリアになりました。
- サンプルノートブックの文言が若干整理され、使用するデータセット名がコードフォントで強調されています。

全体として、この更新はユーザーがモデルをデプロイする際の理解と作業を助けることを目指しており、文書全体の可読性と技術的正確性を向上させています。

## articles/ai-studio/how-to/deploy-models-phi-4.md{#item-c40212}

<details>
<summary>Diff</summary>
````diff
@@ -5,9 +5,9 @@ description: Learn how to use Phi-4 family chat models with Azure AI Foundry.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 12/12/2024
-ms.reviewer: fasantia
-reviewer: santiagxf
+ms.date: 01/09/2025
+ms.reviewer: v-vkonjarla
+reviewer: VindyaKonjarla
 ms.author: mopeakande
 author: msakande
 ms.custom: references_regions, generated
@@ -45,6 +45,15 @@ To use Phi-4 family chat models with Azure AI Foundry, you need the following pr
 
 ### A model deployment
 
+**Deployment to serverless APIs**
+
+Phi-4 family chat models can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Foundry portal, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
 **Deployment to a self-hosted managed compute**
 
 Phi-4 family chat models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
@@ -75,7 +84,7 @@ Read more about the [Azure AI inference package and reference](https://aka.ms/az
 In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
 
 > [!TIP]
-> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry with the same code and structure, including Phi-4 family chat models.
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry portal with the same code and structure, including Phi-4 family chat models.
 
 ### Create a client to consume the model
 
@@ -107,6 +116,9 @@ client = ChatCompletionsClient(
 )
 ```
 
+> [!NOTE]
+> Currently, serverless API endpoints don't support using Microsoft Entra ID for authentication.
+
 ### Get the model's capabilities
 
 The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
@@ -146,6 +158,9 @@ response = client.complete(
 )
 ```
 
+> [!NOTE]
+> Phi-4 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+
 The response is as follows, where you can see the model's usage statistics:
 
 
@@ -234,7 +249,7 @@ response = client.complete(
 ```
 
 > [!WARNING]
-> Phi-4 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-4 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -261,12 +276,48 @@ The following extra parameters can be passed to Phi-4 family chat models:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
+### Apply content safety
+
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+
+The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
+
+
+```python
+from azure.ai.inference.models import AssistantMessage, UserMessage, SystemMessage
+
+try:
+    response = client.complete(
+        messages=[
+            SystemMessage(content="You are an AI assistant that helps people find information."),
+            UserMessage(content="Chopping tomatoes and cutting them into cubes or wedges are great ways to practice your knife skills."),
+        ]
+    )
+
+    print(response.choices[0].message.content)
+
+except HttpResponseError as ex:
+    if ex.status_code == 400:
+        response = ex.response.json()
+        if isinstance(response, dict) and "error" in response:
+            print(f"Your request triggered an {response['error']['code']} error:\n\t {response['error']['message']}")
+        else:
+            raise
+    raise
+```
+
+> [!TIP]
+> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+
+> [!NOTE]
+> Azure AI content safety is only available for models deployed as serverless API endpoints.
+
 ::: zone-end
 
 
@@ -292,6 +343,15 @@ To use Phi-4 family chat models with Azure AI Foundry, you need the following pr
 
 ### A model deployment
 
+**Deployment to serverless APIs**
+
+Phi-4 family chat models can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Foundry portal, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
 **Deployment to a self-hosted managed compute**
 
 Phi-4 family chat models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
@@ -320,7 +380,7 @@ npm install @azure-rest/ai-inference
 In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
 
 > [!TIP]
-> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry with the same code and structure, including Phi-4 family chat models.
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry portal with the same code and structure, including Phi-4 family chat models.
 
 ### Create a client to consume the model
 
@@ -352,6 +412,9 @@ const client = new ModelClient(
 );
 ```
 
+> [!NOTE]
+> Currently, serverless API endpoints don't support using Microsoft Entra ID for authentication.
+
 ### Get the model's capabilities
 
 The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
@@ -393,6 +456,9 @@ var response = await client.path("/chat/completions").post({
 });
 ```
 
+> [!NOTE]
+> Phi-4 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+
 The response is as follows, where you can see the model's usage statistics:
 
 
@@ -493,7 +559,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!WARNING]
-> Phi-4 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-4 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -525,11 +591,53 @@ The following extra parameters can be passed to Phi-4 family chat models:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
+
+
+### Apply content safety
+
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
+The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
+
+
+```javascript
+try {
+    var messages = [
+        { role: "system", content: "You are an AI assistant that helps people find information." },
+        { role: "user", content: "Chopping tomatoes and cutting them into cubes or wedges are great ways to practice your knife skills." },
+    ];
+
+    var response = await client.path("/chat/completions").post({
+        body: {
+            messages: messages,
+        }
+    });
+
+    console.log(response.body.choices[0].message.content);
+}
+catch (error) {
+    if (error.status_code == 400) {
+        var response = JSON.parse(error.response._content);
+        if (response.error) {
+            console.log(`Your request triggered an ${response.error.code} error:\n\t ${response.error.message}`);
+        }
+        else
+        {
+            throw error;
+        }
+    }
+}
+```
+
+> [!TIP]
+> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+
+> [!NOTE]
+> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ::: zone-end
 
@@ -556,6 +664,15 @@ To use Phi-4 family chat models with Azure AI Foundry, you need the following pr
 
 ### A model deployment
 
+**Deployment to serverless APIs**
+
+Phi-4 family chat models can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Foundry portal, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
 **Deployment to a self-hosted managed compute**
 
 Phi-4 family chat models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
@@ -607,7 +724,7 @@ using System.Reflection;
 In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
 
 > [!TIP]
-> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry with the same code and structure, including Phi-4 family chat models.
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry portal with the same code and structure, including Phi-4 family chat models.
 
 ### Create a client to consume the model
 
@@ -631,6 +748,9 @@ client = new ChatCompletionsClient(
 );
 ```
 
+> [!NOTE]
+> Currently, serverless API endpoints don't support using Microsoft Entra ID for authentication.
+
 ### Get the model's capabilities
 
 The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
@@ -671,6 +791,9 @@ ChatCompletionsOptions requestOptions = new ChatCompletionsOptions()
 Response<ChatCompletions> response = client.Complete(requestOptions);
 ```
 
+> [!NOTE]
+> Phi-4 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+
 The response is as follows, where you can see the model's usage statistics:
 
 
@@ -772,7 +895,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
 > [!WARNING]
-> Phi-4 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-4 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -801,11 +924,53 @@ The following extra parameters can be passed to Phi-4 family chat models:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
+
+
+### Apply content safety
 
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+
+The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
+
+
+```csharp
+try
+{
+    requestOptions = new ChatCompletionsOptions()
+    {
+        Messages = {
+            new ChatRequestSystemMessage("You are an AI assistant that helps people find information."),
+            new ChatRequestUserMessage(
+                "Chopping tomatoes and cutting them into cubes or wedges are great ways to practice your knife skills."
+            ),
+        },
+    };
+
+    response = client.Complete(requestOptions);
+    Console.WriteLine(response.Value.Choices[0].Message.Content);
+}
+catch (RequestFailedException ex)
+{
+    if (ex.ErrorCode == "content_filter")
+    {
+        Console.WriteLine($"Your query has trigger Azure Content Safety: {ex.Message}");
+    }
+    else
+    {
+        throw;
+    }
+}
+```
+
+> [!TIP]
+> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+
+> [!NOTE]
+> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ::: zone-end
 
@@ -832,6 +997,15 @@ To use Phi-4 family chat models with Azure AI Foundry, you need the following pr
 
 ### A model deployment
 
+**Deployment to serverless APIs**
+
+Phi-4 family chat models can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Foundry portal, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
 **Deployment to a self-hosted managed compute**
 
 Phi-4 family chat models can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served.
@@ -853,14 +1027,17 @@ Models deployed with the [Azure AI model inference API](https://aka.ms/azureai/m
 In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
 
 > [!TIP]
-> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry with the same code and structure, including Phi-4 family chat models.
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry portal with the same code and structure, including Phi-4 family chat models.
 
 ### Create a client to consume the model
 
 First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
 
 When you deploy the model to a self-hosted online endpoint with **Microsoft Entra ID** support, you can use the following code snippet to create a client.
 
+> [!NOTE]
+> Currently, serverless API endpoints don't support using Microsoft Entra ID for authentication.
+
 ### Get the model's capabilities
 
 The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
@@ -902,6 +1079,9 @@ The following example shows how you can create a basic chat completions request
 }
 ```
 
+> [!NOTE]
+> Phi-4 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+
 The response is as follows, where you can see the model's usage statistics:
 
 
@@ -1063,7 +1243,7 @@ Explore other parameters that you can specify in the inference client. For a ful
 ```
 
 > [!WARNING]
-> Phi-4 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Phi-4 family models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1102,11 +1282,52 @@ The following extra parameters can be passed to Phi-4 family chat models:
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
+
+
+### Apply content safety
 
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+
+The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
+
+
+```json
+{
+    "messages": [
+        {
+            "role": "system",
+            "content": "You are an AI assistant that helps people find information."
+        },
+                {
+            "role": "user",
+            "content": "Chopping tomatoes and cutting them into cubes or wedges are great ways to practice your knife skills."
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
+> [!NOTE]
+> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ::: zone-end
 
@@ -1116,21 +1337,22 @@ For more examples of how to use Phi-4 family models, see the following examples
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
-| CURL request                              | Bash              | [Link](https://aka.ms/phi-3/webrequests-sample)         |
-| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)                  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples) |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
-| Python web requests                       | Python            | [Link](https://aka.ms/phi-3/webrequests-sample)         |
-| OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/phi-3/openaisdk)                  |
-| LangChain                                 | Python            | [Link](https://aka.ms/phi-3/langchain-sample)           |
-| LiteLLM                                   | Python            | [Link](https://aka.ms/phi-3/litellm-sample)             | 
+| LangChain                                 | Python            | [Link](https://aka.ms/azureai/langchain)           |
+| Llama-Index                               | Python            | [Link](https://aka.ms/azureai/llamaindex)             |  
+
+
+## Cost and quota considerations for Phi-4 family models deployed as serverless API endpoints
 
+Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
 ## Cost and quota considerations for Phi-4 family models deployed to managed compute
 
 Phi-4 family models deployed to managed compute are billed based on core hours of the associated compute instance. The cost of the compute instance is determined by the size of the instance, the number of instances running, and the run duration.
 
-It is a good practice to start with a low number of instances and scale up as needed. You can monitor the cost of the compute instance in the Azure portal.
+It's a good practice to start with a low number of instances and scale up as needed. You can monitor the cost of the compute instance in the Azure portal.
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-4モデルのデプロイに関する更新"
}
```

### Explanation
このコードの変更は、Azure AI StudioにおけるPhi-4ファミリーチャットモデルのデプロイ方法に関するドキュメントに対する大幅な更新を示しています。以下の重要な変更点があります：

1. **新しいデプロイメントオプションの追加**:
   - サーバーレスAPIエンドポイントへのデプロイメントについての詳細が追加され、これによりモデルをホスティングすることなくAPIとして利用できるようになります。このデプロイ方法は、エンタープライズのセキュリティとコンプライアンスを維持したまま、従量課金制で利用できる利点があります。

2. **認証に関する注意事項の強調**:
   - サーバーレスAPIエンドポイントがMicrosoft Entra IDによる認証をサポートしていないことが明確に記載されました。

3. **コンテンツの安全性に関する情報の追加**:
   - Azure AIコンテンツ安全性の機能が新たに追加され、入力や出力を分類モデルのアンサンブルで分析して有害なコンテンツの出力を防ぐ仕組みが提供されています。また、その具体的な使用例とエラーハンドリングについても説明が加えられています。

4. **メッセージのシステムメッセージに関する制約**:
   - Phi-4ファミリーがシステムメッセージをサポートしていないという情報が明確化され、ユーザーメッセージに変換されることが説明されています。

5. **パラメータに関する詳細**:
   - `logit_bias`などのパラメータに関する説明が整理され、利用方法についての注意が促されています。

全体として、この更新はPhi-4ファミリーのモデル利用に関連する重要な情報を追加し、開発者やユーザーにとってよりアクセスしやすいリソースにすることを目指しています。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -83,7 +83,7 @@ Gretel | Not available | Gretel-Navigator
 Healthcare AI family Models | MedImageParse<BR>  MedImageInsight<BR>  CxrReportGen<BR>  Virchow<BR>  Virchow2<BR>  Prism<BR>  BiomedCLIP-PubMedBERT<BR>  microsoft-llava-med-v1.5<BR>  m42-health-llama3-med4<BR>  biomistral-biomistral-7b<BR>  microsoft-biogpt-large-pub<BR>  microsoft-biomednlp-pub<BR>  stanford-crfm-biomedlm<BR>  medicalai-clinicalbert<BR>  microsoft-biogpt<BR>  microsoft-biogpt-large<BR>  microsoft-biomednlp-pub<BR> | Not Available
 JAIS | Not available | jais-30b-chat
 Meta Llama family models | Llama-3.3-70B-Instruct<BR> Llama-3.2-3B-Instruct<BR>  Llama-3.2-1B-Instruct<BR>  Llama-3.2-1B<BR>  Llama-3.2-90B-Vision-Instruct<BR>  Llama-3.2-11B-Vision-Instruct<BR>  Llama-3.1-8B-Instruct<BR>  Llama-3.1-8B<BR>  Llama-3.1-70B-Instruct<BR>  Llama-3.1-70B<BR>  Llama-3-8B-Instruct<BR>  Llama-3-70B<BR>  Llama-3-8B<BR>  Llama-Guard-3-1B<BR>  Llama-Guard-3-8B<BR>  Llama-Guard-3-11B-Vision<BR>  Llama-2-7b<BR>  Llama-2-70b<BR>  Llama-2-7b-chat<BR>  Llama-2-13b-chat<BR>  CodeLlama-7b-hf<BR>  CodeLlama-7b-Instruct-hf<BR>  CodeLlama-34b-hf<BR>  CodeLlama-34b-Python-hf<BR>  CodeLlama-34b-Instruct-hf<BR>  CodeLlama-13b-Instruct-hf<BR>  CodeLlama-13b-Python-hf<BR>  Prompt-Guard-86M<BR>  CodeLlama-70b-hf<BR> | Llama-3.3-70B-Instruct<BR> Llama-3.2-90B-Vision-Instruct<br>  Llama-3.2-11B-Vision-Instruct<br>  Llama-3.1-8B-Instruct<br>  Llama-3.1-70B-Instruct<br>  Llama-3.1-405B-Instruct<br>  Llama-3-8B-Instruct<br>  Llama-3-70B-Instruct<br>  Llama-2-7b<br>  Llama-2-7b-chat<br>  Llama-2-70b<br>  Llama-2-70b-chat<br>  Llama-2-13b<br>  Llama-2-13b-chat<br>
-Microsoft Phi family models | Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> Phi-3-vision-128k-Instruct <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct <br> Phi-4| Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct
+Microsoft Phi family models | Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> Phi-3-vision-128k-Instruct <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct <br> Phi-4| Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct <br> Phi-4
 Mistral family models | mistralai-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x22B-Instruct-v0-1 <br> mistral-community-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x7B-v01 <br> mistralai-Mistral-7B-Instruct-v0-2 <br> mistralai-Mistral-7B-v01 <br> mistralai-Mixtral-8x7B-Instruct-v01 <br> mistralai-Mistral-7B-Instruct-v01 | Mistral-large (2402) <br> Mistral-large (2407) <br> Mistral-small <br> Ministral-3B <br> Mistral-NeMo
 Nixtla | Not available | TimeGEN-1
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルカタログの概要に関する更新"
}
```

### Explanation
このコードの変更は、Azure AI Studioの「モデルカタログの概要」ドキュメントにおける情報の軽微な修正を示しています。主な変更は次の通りです。

1. **内容の明確化**:
   - Microsoft Phiファミリーモデルに関する記述において、たった一つのスペースが修正され、整合性が向上しました。具体的には、記載されているモデル名のリストにおいて、行の区切りの一貫性が確保されました。

2. **全体のフォーマットの一貫性**:
   - 変更により、モデル名やバージョン名のフォーマットが統一され、可読性の向上に寄与しています。 

この更新は、ドキュメント全体の品質と可読性の向上を目的としており、ユーザーに対してより明確な情報を提供する役割を果たします。

## articles/ai-studio/includes/region-availability-maas.md{#item-35d79c}

<details>
<summary>Diff</summary>
````diff
@@ -50,10 +50,11 @@ Llama 3.1 8B Instruct <br> Llama 3.1 70B Instruct <br> Llama-3.2-11B-Vision-Inst
 Llama 3.1 405B Instruct  | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3     | Not available  |
 
 
-### Microsoft Phi-3 family models
+### Microsoft Phi family models
 
 | Model | Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
+Phi-4                       | Not applicable | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available       |
 Phi-3.5-vision-Instruct     | Not applicable | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available       |
 Phi-3.5-MoE-Instruct     | Not applicable | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | East US 2       |
 Phi-3.5-Mini-Instruct     | Not applicable | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | East US 2  | East US 2       |
@@ -92,3 +93,9 @@ TimeGEN-1     | [Microsoft Managed countries/regions](/partner-center/marketplac
 |---------|---------|---------|---------|
 AI21-Jamba-1.5-Mini | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) | East US 2 <br> South Central US <br> East US <br> West US 3 <br> West US <br> North Central US       |  Not available       |
 AI21-Jamba-1.5-Large | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) | East US 2 <br> South Central US <br> East US <br> West US 3 <br> West US <br> North Central US       |  Not available       |
+
+### Bria models
+
+|Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
+|---------|---------|---------|---------|
+Bria-2.3-Fast   | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  | East US 2   | Not available       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの地域可用性に関する更新"
}
```

### Explanation
このコードの変更は、Azure AI Studioにおける「地域可用性」ドキュメントの一部の更新を示しています。主な変更点は以下の通りです。

1. **見出しの修正**:
   - 「Microsoft Phi-3 family models」という見出しが「Microsoft Phi family models」に変更され、モデルの名称がより正確な表記に修正されました。

2. **Phiモデルに関連する地域の追加**:
   - Phi-4、Phi-3.5-vision-Instruct、およびPhi-3.5-MoE-Instructのモデルについて、利用可能な地域として「East US」、「Sweden Central」などが明示されました。この情報はユーザーにとって流通ルートや地理的制約を理解するのに役立ちます。

3. **新しいモデル「Bria models」の追加**:
   - 「Bria models」というセクションが新たに追加され、「Bria-2.3-Fast」モデルについての可用性が記載されました。具体的には、Hub/Project Region for Deploymentとして「East US 2」が指定されていますが、ファインチューニングについては「Not available」とされています。

この更新は、地域におけるモデルの可用性に関する情報を強化し、ユーザーがそれぞれのモデルを利用できる場所を理解するための重要な情報を提供しています。

## articles/ai-studio/reference/reference-model-inference-api.md{#item-9fe240}

<details>
<summary>Diff</summary>
````diff
@@ -73,7 +73,6 @@ The API indicates how developers can consume predictions for the following modal
 
 * [Get info](reference-model-inference-info.md): Returns the information about the model deployed under the endpoint.
 * [Text embeddings](reference-model-inference-embeddings.md): Creates an embedding vector representing the input text.
-* [Text completions](reference-model-inference-completions.md): Creates a completion for the provided prompt and parameters.
 * [Chat completions](reference-model-inference-chat-completions.md): Creates a model response for the given chat conversation.
 * [Image embeddings](reference-model-inference-images-embeddings.md): Creates an embedding vector representing the input text and image.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル推論APIの参照に関する修正"
}
```

### Explanation
このコードの変更は、Azure AI Studioの「モデル推論APIの参照」ドキュメントにおける軽微な修正を示しています。主な変更点は以下の通りです。

1. **リスト項目の削除**:
   - 「Text completions」という項目がリストから削除されました。この変更により、APIが提供する機能の一部として「テキスト補完」が示されなくなりました。

この修正は、おそらくAPIの機能に関する最新の情報を反映するものであり、正確で信頼性の高いドキュメントを維持するための重要な更新です。これにより、開発者は利用可能なAPI機能をより明確に理解できるようになります。

## articles/ai-studio/reference/region-support.md{#item-d402e1}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.custom: references_regions, build-2024
 
 Azure AI Foundry brings together various Azure AI capabilities that previously were only available as standalone Azure services. While we strive to make all features available in all regions where Azure AI Foundry is supported at the same time, feature availability may vary by region. In this article, you'll learn what Azure AI Foundry features are available across cloud regions.  
 
-## Azure Public regions
+## Azure AI Foundry projects
 
 Azure AI Foundry is currently available in the following Azure regions. You can create [projects in Azure AI Foundry portal](../how-to/create-projects.md) in these regions.
 
@@ -44,30 +44,22 @@ Azure AI Foundry is currently available in the following Azure regions. You can
 - West US
 - West US 3
 
-### Azure Government regions
-
-Azure AI Foundry is currently not available in Azure Government regions or air-gap regions.
-
-## Azure OpenAI
-
-For information on the availability of Azure OpenAI models, see [Azure OpenAI Model summary table and region availability](../../ai-services/openai/concepts/models.md#model-summary-table-and-region-availability).
-
 > [!NOTE]
-> Some models might not be available within the Azure AI Foundry model catalog.
-
-For more information, see [Azure OpenAI quotas and limits](/azure/ai-services/openai/quotas-limits).
-
-## Speech capabilities
-
-Azure AI Speech capabilities including custom neural voice vary in regional availability due to underlying hardware availability. See [Speech service supported regions](../../ai-services/speech-service/regions.md) for an overview.
-
-## Serverless API deployments
+> Azure AI Foundry is currently not available in Azure Government regions or air-gap regions.
 
-Some models in the model catalog can be deployed as a serverless API with pay-as-you-go billing. For information on the regions where each model is available, see [Region availability for models in Serverless API endpoints](../how-to/deploy-models-serverless-availability.md).
+## Azure AI Foundry features
+ 
+You can add features from different regions to your project. You may need to use a different region for a particular feature, based on the region availability of that feature.
 
-## Azure AI Content Safety
+The following table lists the availability of Azure AI Foundry features across Azure regions.
 
-To use the Content Safety APIs, you must create your Azure AI Content Safety resource in a supported region. For a list of supported regions, see [What is Azure AI Content Safety?](../../ai-services/content-safety/overview.md#region-availability)
+| Service                        | Description                                                                                                                                          | Link                                                                                                      |
+|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
+| Azure OpenAI                   | Note that some models might not be available within the Azure AI Foundry model catalog.                                                              | [Azure OpenAI quotas and limits](/azure/ai-services/openai/quotas-limits)
+| Speech capabilities            | Azure AI Speech capabilities including custom neural voice vary in regional availability due to underlying hardware availability.                     | [Speech service supported regions](../../ai-services/speech-service/regions.md)                           |
+| Serverless API deployments     | Some models in the model catalog can be deployed as a serverless API with pay-as-you-go billing.                                                      | [Region availability for models in Serverless API endpoints](../how-to/deploy-models-serverless-availability.md) |
+| Azure AI Content Safety        | To use the Content Safety APIs, you must create your Azure AI Content Safety resource in a supported region.                                           | [What is Azure AI Content Safety?](../../ai-services/content-safety/overview.md#region-availability)       |
+| Azure AI Agent Service         | Azure AI Agent Service supports the same models as the chat completions API in Azure OpenAI.                                                          | [Azure AI Agent Service region availability](../../ai-services/agents/concepts/model-region-support.md#azure-openai-models) |
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域サポートに関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、Azure AI Studioにおける「地域サポート」のドキュメントに対する修正を示しています。主な変更点は以下の通りです。

1. **セクションタイトルの変更**:
   - 「Azure Public regions」というセクションタイトルが「Azure AI Foundry projects」に変更され、全体の内容がプロジェクトに関連する情報にフォーカスされるようになりました。

2. **新たな情報の追加**:
   - 特定の地域で利用可能なAzure AI Foundryの機能について、追加の詳細が提供されました。ユーザーがプロジェクトに地域ごとの機能を追加できることに言及されています。

3. **テーブルの追加**:
   - Azure AI Foundryの機能が異なるAzure地域でどのように利用可能であるかを示すテーブルが追加されました。この表には各サービスとその説明、リンクが含まれており、ユーザーが容易に情報を参照できるようになっています。

4. **不要な情報の削除**:
   - 以前のセクションに含まれていた「Azure Government regions」や「Azure OpenAI」など、いくつかの情報が削除され、文書がより簡潔になりました。

今回の変更は、ユーザーが地域の可用性を理解し、適切なサービスを選択する際の助けとなる情報を強化することを目的としています。これにより、ユーザーがプロジェクトを効果的に管理できるようになります。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -453,8 +453,6 @@ items:
           href: reference/reference-model-inference-info.md
         - name: Embeddings
           href: reference/reference-model-inference-embeddings.md
-        - name: Completions
-          href: reference/reference-model-inference-completions.md
         - name: Chat Completions
           href: reference/reference-model-inference-chat-completions.md
         - name: Images Embeddings
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次からの項目の削除"
}
```

### Explanation
このコードの変更は、Azure AI Studioの目次ファイル（toc.yml）における軽微な修正を示しています。主な変更点は以下の通りです。

1. **リスト項目の削除**:
   - 「Completions」という項目が目次から削除されました。これにより、ユーザーが参照できる情報から「テキスト補完」に関連する内容が取り除かれました。

2. **構成のシンプル化**:
   - リストの内容が簡素化され、残りの項目（「Embeddings」や「Chat Completions」、「Images Embeddings」）がより明確に残されました。この変更は、情報の優先順位や関連性を高めることを目的としています。

この修正は、文書全体の整合性を保つための重要な措置であり、ユーザーが現在利用可能なリソースを特定しやすくしています。これにより、閲覧者は必要な情報に迅速にアクセスできるようになります。


