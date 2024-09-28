---
date: '2024-09-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:552467e...MicrosoftDocs:ceaf221
summary: 今回の変更は、Microsoft Azureのドキュメントを新バージョンのAPIおよびモデルに対応させるための情報更新を行ったものです。具体的には、Cohere
  Command R+ 08-2024およびCohere Command R 08-2024モデルに関する詳細情報の追加や、地域可用性情報の更新が行われました。すべてはマイナーアップデートであり、互換性を壊すような大幅な変更はありません。また、APIバージョンを新しい「2024-07-31-preview」に変更し、目次ファイルのリンク修正も行いました。これにより、ユーザーは正確な情報を元に新しいAPIやモデルを効果的に利用できるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:552467e...MicrosoftDocs:ceaf221){target="_blank"}

# ハイライト
今回の変更は、主にMicrosoft Azureの各種ドキュメントにおいて、新バージョンのAPIおよびモデルに対応した情報の更新を行っています。新機能の追加やモデルのバージョン更新に伴い、複数のドキュメントが修正されました。

## 新機能
- Cohere Command R+ 08-2024およびCohere Command R 08-2024モデルに関する詳細情報の追加。
- Cohereモデルの地域可用性情報の更新と新モデルの追加。

## 互換性に関する変更
- すべてがマイナーアップデートであり、以前の大幅な変更や再設計は行われていないため、互換性を壊す変更はない。

## その他の更新
- AzureドキュメントのAPIバージョンを新しい「2024-07-31-preview」に変更。
- 目次ファイル（toc.yml）のリンク修正。

# インサイト
この変更は主に軽微なものですが、ユーザーにとって非常に重要な要素を含んでいます。まず、AzureのREST APIに関しては新しいバージョン「2024-07-31-preview」に対応した内容が追加されました。予想されるAPIの動作や使用方法に齟齬がないように、cURLコマンドの例や説明文も最新の仕様に一致するように修正されています。これにより、開発者は新しいAPIを利用する際に迷うことなく進行できるでしょう。

次に、Cohereモデルに対する更新が注目されます。CohereはAIモデルの一種であり、今回の変更で詳細な使用方法や機能が追加されました。具体的には、新しいCohere Command R+ 08-2024およびCohere Command R 08-2024モデルに関する情報がドキュメントに追加されました。ユーザーはこれらのモデルについて、アーキテクチャや使用ケース、対応言語などの情報を基に適切に利用できるようになるでしょう。

さらに、地域可用性情報の更新もユーザーにとって重要です。特定の地域でサービスを利用する必要がある場合、この情報は不可欠です。新しいモデルは特定の地域でも利用可能となり、ユーザーの選択肢が広がります。

最後に、目次ファイル（toc.yml）のリンク修正は一見地味ですが、ドキュメント全体の整合性と可読性を維持するためには重要です。この小さな変更によって、関連情報にアクセスしやすくなり、ユーザー体験が向上します。

以上のように、今回のドキュメント更新はユーザーが最新かつ正確な情報を利用して効果的にAPIやモデルを活用するためのものであり、非常に価値のあるものと言えます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [rest-api.md](#item-9d952f) | minor update | REST APIのバージョン更新およびドキュメント修正 | modified | 5 | 5 | 10 | 
| [deploy-models-cohere-command.md](#item-3e97f4) | minor update | Cohereモデルに関するドキュメントの更新と追加 | modified | 201 | 49 | 250 | 
| [model-catalog-overview.md](#item-278001) | minor update | Cohereモデルのバージョン情報の更新 | modified | 1 | 1 | 2 | 
| [region-availability-maas.md](#item-35d79c) | minor update | Cohereモデルの地域可用性情報の更新 | modified | 3 | 1 | 4 | 
| [toc.yml](#item-2745cd) | minor update | TOCファイルのリンク修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/quickstarts/includes/rest-api.md{#item-9d952f}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.date: 09/09/2024
 ms.author: lajanuar
 ---
 
-<!-- markdownlint-disable MD036 -->
+<!-- markdownlint-disable MD036 -->
 
 :::moniker range="doc-intel-4.0.0"
 | [Document Intelligence REST API](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true) | [Supported Azure SDKS](../../sdk-overview-v4-0.md)
@@ -109,7 +109,7 @@ Before you run the cURL command, make the following changes to the [post request
 :::moniker range="doc-intel-4.0.0"
 
 ```bash
-curl -v -i POST "{endpoint}/documentintelligence/documentModels/{modelId}:analyze?api-version=2024-02-29-preview" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: {key}" --data-ascii "{'urlSource': '{your-document-url}'}"
+curl -v -i POST "{endpoint}/documentintelligence/documentModels/{modelId}:analyze?api-version=2024-07-31-preview" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: {key}" --data-ascii "{'urlSource': '{your-document-url}'}"
 ```
 
 :::moniker-end
@@ -140,7 +140,7 @@ You receive a `202 (Success)` response that includes a read-only **Operation-Loc
 
 :::moniker range="doc-intel-4.0.0"
 
-After you call the [`Analyze document`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2024-02-29-preview&preserve-view=true&branch=docintelligence&tabs=HTTP) API, call the [**Get analyze result**](/rest/api/aiservices/document-models/get-analyze-result?view=rest-aiservices-2024-02-29-preview&preserve-view=true&branch=docintelligence&tabs=HTTP) API to get the status of the operation and the extracted data. Before you run the command, make these changes:
+After you call the [`Analyze document`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true&tabs=HTTP) API, call the [**Get analyze result**](/rest/api/aiservices/document-models/get-analyze-result?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true&tabs=HTTP) API to get the status of the operation and the extracted data. Before you run the command, make these changes:
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
@@ -165,7 +165,7 @@ After you call the [`Analyze document`](/rest/api/aiservices/document-models/ana
 :::moniker range="doc-intel-4.0.0"
 
 ```bash
-curl -v -X GET "{endpoint}/documentintelligence/documentModels/{modelId}/analyzeResults/{resultId}?api-version=2024-02-29-preview" -H "Ocp-Apim-Subscription-Key: {key}"
+curl -v -X GET "{endpoint}/documentintelligence/documentModels/{modelId}/analyzeResults/{resultId}?api-version=2024-07-31-preview" -H "Ocp-Apim-Subscription-Key: {key}"
 ```
 
 :::moniker-end
@@ -202,7 +202,7 @@ You receive a `200 (Success)` response with JSON output. The first field, `"stat
     "createdDateTime": "2024-03-25T19:31:37Z",
     "lastUpdatedDateTime": "2024-03-25T19:31:43Z",
     "analyzeResult": {
-        "apiVersion": "2024-02-29-preview",
+        "apiVersion": "2024-07-31-preview",
         "modelId": "prebuilt-invoice",
         "stringIndexType": "textElements"...
     ..."pages": [
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIのバージョン更新およびドキュメント修正"
}
```

### Explanation
この変更は、Microsoft Azureのドキュメントインテリジェンスに関連するREST APIのドキュメントに対する軽微な更新を行っています。具体的には、APIのバージョンを「2024-02-29-preview」から「2024-07-31-preview」へ変更しています。この変更により、コマンド例や関連リンクも新しいバージョンの仕様に合わせて調整されています。

主な変更点は以下の通りです：
- コメント内のMarkdownLint無効化指示の形式が修正されました。
- cURLコマンドのAPI呼び出し部分のバージョン番号が更新され、正しいAPIエンドポイントが反映されています。
- API呼び出しに関する説明文も、最新のAPIバージョンと一致するように調整されています。

このような更新は、利用者が最新のAPIを利用する際の誤解を避け、より正確な情報を提供するために重要です。

## articles/ai-studio/how-to/deploy-models-cohere-command.md{#item-3e97f4}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Cohere Command chat models with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 08/08/2024
+ms.date: 09/23/2024
 ms.reviewer: shubhiraj
 reviewer: shubhirajMsft
 ms.author: mopeakande
@@ -29,14 +29,52 @@ The Cohere family of models includes various models optimized for different use
 
 The Cohere Command chat models include the following models:
 
+# [Cohere Command R+ 08-2024](#tab/cohere-command-r-plus-08-2024)
+
+Command R+ 08-2024 is a generative large language model optimized for various use cases, including reasoning, summarization, and question answering.
+
+* **Model Architecture**: Command R+ 08-2024 is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The mode is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
+* **Context length:** Command R+ 08-2024 supports a context length of 128 K.
+* **Input:** Text only.
+* **Output:** Text only.
+
+We recommend using Command R+ 08-2024 for those workflows that lean on complex retrieval augmented generation (RAG) functionality, multi-step tool use (agents), and structured outputs.
+
+
+The following models are available:
+
+* [Cohere-command-r-plus-08-2024](https://aka.ms/azureai/landing/Cohere-command-r-plus-08-2024)
+
+
+# [Cohere Command R 08-2024](#tab/cohere-command-r-08-2024)
+
+Command R 08-2024 is a large language model optimized for various use cases, including reasoning, summarization, and question answering.
+
+* **Model Architecture**: Command R 08-2024 is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
+* **Context length:** Command R 08-2024 supports a context length of 128 K.
+* **Input:** Text only.
+* **Output:** Text only.
+
+
+The following models are available:
+
+* [Cohere-command-r-08-2024](https://aka.ms/azureai/landing/Cohere-command-r-08-2024)
+
+
 # [Cohere Command R+](#tab/cohere-command-r-plus)
 
 Command R+ is a generative large language model optimized for various use cases, including reasoning, summarization, and question answering.
 
-* **Model Architecture**: Both Command R and Command R+ are autoregressive language models that use an optimized transformer architecture. After pre-training, the models use supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
-* **Languages covered**: The models are optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Model Architecture**: Command R+ is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
 * **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
-* **Context length:** Command R and Command R+ support a context length of 128 K.
+* **Context length:** Command R+ supports a context length of 128 K.
+* **Input:** Text only.
+* **Output:** Text only.
 
 We recommend using Command R+ for those workflows that lean on complex retrieval augmented generation (RAG) functionality and multi-step tool use (agents).
 
@@ -50,10 +88,10 @@ The following models are available:
 
 Command R is a large language model optimized for various use cases, including reasoning, summarization, and question answering.
 
-* **Model Architecture**: Both Command R and Command R+ are autoregressive language models that use an optimized transformer architecture. After pre-training, the models use supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
-* **Languages covered**: The models are optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Model Architecture**: Command R is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
 * **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
-* **Context length:** Command R and Command R+ support a context length of 128 K.
+* **Context length:** Command R supports a context length of 128 K.
 
 Command R is great for simpler retrieval augmented generation (RAG) and single-step tool use tasks. It's also great for use in applications where price is a major consideration.
 
@@ -141,7 +179,7 @@ print("Model provider name:", model_info.model_provider_name)
 ```
 
 ```console
-Model name: Cohere-command-r-plus
+Model name: Cohere-command-r-plus-08-2024
 Model type: chat-completions
 Model provider name: Cohere
 ```
@@ -175,7 +213,7 @@ print("\tCompletion tokens:", response.usage.completion_tokens)
 
 ```console
 Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
-Model: Cohere-command-r-plus
+Model: Cohere-command-r-plus-08-2024
 Usage: 
   Prompt tokens: 19
   Total tokens: 91
@@ -244,7 +282,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormatText() },
 )
 ```
 
@@ -264,7 +302,7 @@ response = client.complete(
                       " the following format: { ""answer"": ""response"" }."),
         UserMessage(content="How many languages are in the world?"),
     ],
-    response_format=ChatCompletionsResponseFormatJSON()
+    response_format={ "type": ChatCompletionsResponseFormatJSON() }
 )
 ```
 
@@ -332,7 +370,7 @@ def get_flight_info(loc_origin: str, loc_destination: str):
 ```
 
 > [!NOTE]
-> Cohere-command-r-plus and Cohere-command-r require a tool's responses to be a valid JSON content formatted as a string. When constructing messages of type *Tool*, ensure the response is a valid JSON string.
+> Cohere-command-r-plus-08-2024, Cohere-command-r-08-2024, Cohere-command-r-plus, and Cohere-command-r require a tool's responses to be a valid JSON content formatted as a string. When constructing messages of type *Tool*, ensure the response is a valid JSON string.
 
 Prompt the model to book flights with the help of this function:
 
@@ -464,14 +502,52 @@ except HttpResponseError as ex:
 
 The Cohere Command chat models include the following models:
 
+# [Cohere Command R+ 08-2024](#tab/cohere-command-r-plus-08-2024)
+
+Command R+ 08-2024 is a generative large language model optimized for various use cases, including reasoning, summarization, and question answering.
+
+* **Model Architecture**: Command R+ 08-2024 is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The mode is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
+* **Context length:** Command R+ 08-2024 supports a context length of 128 K.
+* **Input:** Text only.
+* **Output:** Text only.
+
+We recommend using Command R+ 08-2024 for those workflows that lean on complex retrieval augmented generation (RAG) functionality, multi-step tool use (agents), and structured outputs.
+
+
+The following models are available:
+
+* [Cohere-command-r-plus-08-2024](https://aka.ms/azureai/landing/Cohere-command-r-plus-08-2024)
+
+
+# [Cohere Command R 08-2024](#tab/cohere-command-r-08-2024)
+
+Command R 08-2024 is a large language model optimized for various use cases, including reasoning, summarization, and question answering.
+
+* **Model Architecture**: Command R 08-2024 is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
+* **Context length:** Command R 08-2024 supports a context length of 128 K.
+* **Input:** Text only.
+* **Output:** Text only.
+
+
+The following models are available:
+
+* [Cohere-command-r-08-2024](https://aka.ms/azureai/landing/Cohere-command-r-08-2024)
+
+
 # [Cohere Command R+](#tab/cohere-command-r-plus)
 
 Command R+ is a generative large language model optimized for various use cases, including reasoning, summarization, and question answering.
 
-* **Model Architecture**: Both Command R and Command R+ are autoregressive language models that use an optimized transformer architecture. After pre-training, the models use supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
-* **Languages covered**: The models are optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Model Architecture**: Command R+ is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
 * **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
-* **Context length:** Command R and Command R+ support a context length of 128 K.
+* **Context length:** Command R+ supports a context length of 128 K.
+* **Input:** Text only.
+* **Output:** Text only.
 
 We recommend using Command R+ for those workflows that lean on complex retrieval augmented generation (RAG) functionality and multi-step tool use (agents).
 
@@ -485,10 +561,10 @@ The following models are available:
 
 Command R is a large language model optimized for various use cases, including reasoning, summarization, and question answering.
 
-* **Model Architecture**: Both Command R and Command R+ are autoregressive language models that use an optimized transformer architecture. After pre-training, the models use supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
-* **Languages covered**: The models are optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Model Architecture**: Command R is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
 * **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
-* **Context length:** Command R and Command R+ support a context length of 128 K.
+* **Context length:** Command R supports a context length of 128 K.
 
 Command R is great for simpler retrieval augmented generation (RAG) and single-step tool use tasks. It's also great for use in applications where price is a major consideration.
 
@@ -574,7 +650,7 @@ console.log("Model provider name: ", model_info.body.model_provider_name)
 ```
 
 ```console
-Model name: Cohere-command-r-plus
+Model name: Cohere-command-r-plus-08-2024
 Model type: chat-completions
 Model provider name: Cohere
 ```
@@ -614,7 +690,7 @@ console.log("\tCompletion tokens:", response.body.usage.completion_tokens);
 
 ```console
 Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
-Model: Cohere-command-r-plus
+Model: Cohere-command-r-plus-08-2024
 Usage: 
   Prompt tokens: 19
   Total tokens: 91
@@ -788,7 +864,7 @@ function get_flight_info(loc_origin, loc_destination) {
 ```
 
 > [!NOTE]
-> Cohere-command-r-plus and Cohere-command-r require a tool's responses to be a valid JSON content formatted as a string. When constructing messages of type *Tool*, ensure the response is a valid JSON string.
+> Cohere-command-r-plus-08-2024, Cohere-command-r-08-2024, Cohere-command-r-plus, and Cohere-command-r require a tool's responses to be a valid JSON content formatted as a string. When constructing messages of type *Tool*, ensure the response is a valid JSON string.
 
 Prompt the model to book flights with the help of this function:
 
@@ -913,14 +989,52 @@ catch (error) {
 
 The Cohere Command chat models include the following models:
 
+# [Cohere Command R+ 08-2024](#tab/cohere-command-r-plus-08-2024)
+
+Command R+ 08-2024 is a generative large language model optimized for various use cases, including reasoning, summarization, and question answering.
+
+* **Model Architecture**: Command R+ 08-2024 is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The mode is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
+* **Context length:** Command R+ 08-2024 supports a context length of 128 K.
+* **Input:** Text only.
+* **Output:** Text only.
+
+We recommend using Command R+ 08-2024 for those workflows that lean on complex retrieval augmented generation (RAG) functionality, multi-step tool use (agents), and structured outputs.
+
+
+The following models are available:
+
+* [Cohere-command-r-plus-08-2024](https://aka.ms/azureai/landing/Cohere-command-r-plus-08-2024)
+
+
+# [Cohere Command R 08-2024](#tab/cohere-command-r-08-2024)
+
+Command R 08-2024 is a large language model optimized for various use cases, including reasoning, summarization, and question answering.
+
+* **Model Architecture**: Command R 08-2024 is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
+* **Context length:** Command R 08-2024 supports a context length of 128 K.
+* **Input:** Text only.
+* **Output:** Text only.
+
+
+The following models are available:
+
+* [Cohere-command-r-08-2024](https://aka.ms/azureai/landing/Cohere-command-r-08-2024)
+
+
 # [Cohere Command R+](#tab/cohere-command-r-plus)
 
 Command R+ is a generative large language model optimized for various use cases, including reasoning, summarization, and question answering.
 
-* **Model Architecture**: Both Command R and Command R+ are autoregressive language models that use an optimized transformer architecture. After pre-training, the models use supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
-* **Languages covered**: The models are optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Model Architecture**: Command R+ is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
 * **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
-* **Context length:** Command R and Command R+ support a context length of 128 K.
+* **Context length:** Command R+ supports a context length of 128 K.
+* **Input:** Text only.
+* **Output:** Text only.
 
 We recommend using Command R+ for those workflows that lean on complex retrieval augmented generation (RAG) functionality and multi-step tool use (agents).
 
@@ -934,10 +1048,10 @@ The following models are available:
 
 Command R is a large language model optimized for various use cases, including reasoning, summarization, and question answering.
 
-* **Model Architecture**: Both Command R and Command R+ are autoregressive language models that use an optimized transformer architecture. After pre-training, the models use supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
-* **Languages covered**: The models are optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Model Architecture**: Command R is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
 * **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
-* **Context length:** Command R and Command R+ support a context length of 128 K.
+* **Context length:** Command R supports a context length of 128 K.
 
 Command R is great for simpler retrieval augmented generation (RAG) and single-step tool use tasks. It's also great for use in applications where price is a major consideration.
 
@@ -969,7 +1083,7 @@ Deployment to a serverless API endpoint doesn't require quota from your subscrip
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -995,7 +1109,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also use the following namespaces but you may not always need them:
+This example also uses the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -1042,7 +1156,7 @@ Console.WriteLine($"Model provider name: {modelInfo.Value.ModelProviderName}");
 ```
 
 ```console
-Model name: Cohere-command-r-plus
+Model name: Cohere-command-r-plus-08-2024
 Model type: chat-completions
 Model provider name: Cohere
 ```
@@ -1077,7 +1191,7 @@ Console.WriteLine($"\tCompletion tokens: {response.Value.Usage.CompletionTokens}
 
 ```console
 Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
-Model: Cohere-command-r-plus
+Model: Cohere-command-r-plus-08-2024
 Usage: 
   Prompt tokens: 19
   Total tokens: 91
@@ -1260,7 +1374,7 @@ static string getFlightInfo(string loc_origin, string loc_destination)
 ```
 
 > [!NOTE]
-> Cohere-command-r-plus and Cohere-command-r require a tool's responses to be a valid JSON content formatted as a string. When constructing messages of type *Tool*, ensure the response is a valid JSON string.
+> Cohere-command-r-plus-08-2024, Cohere-command-r-08-2024, Cohere-command-r-plus, and Cohere-command-r require a tool's responses to be a valid JSON content formatted as a string. When constructing messages of type *Tool*, ensure the response is a valid JSON string.
 
 Prompt the model to book flights with the help of this function:
 
@@ -1387,14 +1501,52 @@ catch (RequestFailedException ex)
 
 The Cohere Command chat models include the following models:
 
+# [Cohere Command R+ 08-2024](#tab/cohere-command-r-plus-08-2024)
+
+Command R+ 08-2024 is a generative large language model optimized for various use cases, including reasoning, summarization, and question answering.
+
+* **Model Architecture**: Command R+ 08-2024 is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The mode is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
+* **Context length:** Command R+ 08-2024 supports a context length of 128 K.
+* **Input:** Text only.
+* **Output:** Text only.
+
+We recommend using Command R+ 08-2024 for those workflows that lean on complex retrieval augmented generation (RAG) functionality, multi-step tool use (agents), and structured outputs.
+
+
+The following models are available:
+
+* [Cohere-command-r-plus-08-2024](https://aka.ms/azureai/landing/Cohere-command-r-plus-08-2024)
+
+
+# [Cohere Command R 08-2024](#tab/cohere-command-r-08-2024)
+
+Command R 08-2024 is a large language model optimized for various use cases, including reasoning, summarization, and question answering.
+
+* **Model Architecture**: Command R 08-2024 is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
+* **Context length:** Command R 08-2024 supports a context length of 128 K.
+* **Input:** Text only.
+* **Output:** Text only.
+
+
+The following models are available:
+
+* [Cohere-command-r-08-2024](https://aka.ms/azureai/landing/Cohere-command-r-08-2024)
+
+
 # [Cohere Command R+](#tab/cohere-command-r-plus)
 
 Command R+ is a generative large language model optimized for various use cases, including reasoning, summarization, and question answering.
 
-* **Model Architecture**: Both Command R and Command R+ are autoregressive language models that use an optimized transformer architecture. After pre-training, the models use supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
-* **Languages covered**: The models are optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Model Architecture**: Command R+ is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
 * **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
-* **Context length:** Command R and Command R+ support a context length of 128 K.
+* **Context length:** Command R+ supports a context length of 128 K.
+* **Input:** Text only.
+* **Output:** Text only.
 
 We recommend using Command R+ for those workflows that lean on complex retrieval augmented generation (RAG) functionality and multi-step tool use (agents).
 
@@ -1408,10 +1560,10 @@ The following models are available:
 
 Command R is a large language model optimized for various use cases, including reasoning, summarization, and question answering.
 
-* **Model Architecture**: Both Command R and Command R+ are autoregressive language models that use an optimized transformer architecture. After pre-training, the models use supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
-* **Languages covered**: The models are optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
+* **Model Architecture**: Command R is an autoregressive language model that uses an optimized transformer architecture. After pre-training, the model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
+* **Languages covered**: The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, simplified Chinese, and Arabic.
 * **Pre-training data also included the following 13 languages:** Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
-* **Context length:** Command R and Command R+ support a context length of 128 K.
+* **Context length:** Command R supports a context length of 128 K.
 
 Command R is great for simpler retrieval augmented generation (RAG) and single-step tool use tasks. It's also great for use in applications where price is a major consideration.
 
@@ -1475,7 +1627,7 @@ The response is as follows:
 
 ```json
 {
-    "model_name": "Cohere-command-r-plus",
+    "model_name": "Cohere-command-r-plus-08-2024",
     "model_type": "chat-completions",
     "model_provider_name": "Cohere"
 }
@@ -1508,7 +1660,7 @@ The response is as follows, where you can see the model's usage statistics:
     "id": "0a1234b5de6789f01gh2i345j6789klm",
     "object": "chat.completion",
     "created": 1718726686,
-    "model": "Cohere-command-r-plus",
+    "model": "Cohere-command-r-plus-08-2024",
     "choices": [
         {
             "index": 0,
@@ -1565,7 +1717,7 @@ You can visualize how streaming generates content:
     "id": "23b54589eba14564ad8a2e6978775a39",
     "object": "chat.completion.chunk",
     "created": 1718726371,
-    "model": "Cohere-command-r-plus",
+    "model": "Cohere-command-r-plus-08-2024",
     "choices": [
         {
             "index": 0,
@@ -1588,7 +1740,7 @@ The last message in the stream has `finish_reason` set, indicating the reason fo
     "id": "23b54589eba14564ad8a2e6978775a39",
     "object": "chat.completion.chunk",
     "created": 1718726371,
-    "model": "Cohere-command-r-plus",
+    "model": "Cohere-command-r-plus-08-2024",
     "choices": [
         {
             "index": 0,
@@ -1639,7 +1791,7 @@ Explore other parameters that you can specify in the inference client. For a ful
     "id": "0a1234b5de6789f01gh2i345j6789klm",
     "object": "chat.completion",
     "created": 1718726686,
-    "model": "Cohere-command-r-plus",
+    "model": "Cohere-command-r-plus-08-2024",
     "choices": [
         {
             "index": 0,
@@ -1689,7 +1841,7 @@ Cohere Command chat models can create JSON outputs. Set `response_format` to `js
     "id": "0a1234b5de6789f01gh2i345j6789klm",
     "object": "chat.completion",
     "created": 1718727522,
-    "model": "Cohere-command-r-plus",
+    "model": "Cohere-command-r-plus-08-2024",
     "choices": [
         {
             "index": 0,
@@ -1778,7 +1930,7 @@ The following code example creates a tool definition that is able to look from f
 In this example, the function's output is that there are no flights available for the selected route, but the user should consider taking a train.
 
 > [!NOTE]
-> Cohere-command-r-plus and Cohere-command-r require a tool's responses to be a valid JSON content formatted as a string. When constructing messages of type *Tool*, ensure the response is a valid JSON string.
+> Cohere-command-r-plus-08-2024, Cohere-command-r-08-2024, Cohere-command-r-plus, and Cohere-command-r require a tool's responses to be a valid JSON content formatted as a string. When constructing messages of type *Tool*, ensure the response is a valid JSON string.
 
 Prompt the model to book flights with the help of this function:
 
@@ -1833,7 +1985,7 @@ You can inspect the response to find out if a tool needs to be called. Inspect t
     "id": "0a1234b5de6789f01gh2i345j6789klm",
     "object": "chat.completion",
     "created": 1718726007,
-    "model": "Cohere-command-r-plus",
+    "model": "Cohere-command-r-plus-08-2024",
     "choices": [
         {
             "index": 0,
@@ -1972,7 +2124,7 @@ The following example shows how to handle events when the model detects harmful
 
 ## More inference examples
 
-For more examples of how to use Cohere, see the following examples and tutorials:
+For more examples of how to use Cohere models, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
@@ -1995,7 +2147,7 @@ For more examples of how to use Cohere, see the following examples and tutorials
 | Command R+ tool/function calling, using LangChain | `cohere`, `langchain`, `langchain_cohere` | [command_tools-langchain.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/cohere/command_tools-langchain.ipynb) |
 
 
-## Cost and quota considerations for Cohere family of models deployed as serverless API endpoints
+## Cost and quota considerations for Cohere models deployed as serverless API endpoints
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
@@ -2012,4 +2164,4 @@ For more information on how to track costs, see [Monitor costs for models offere
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cohereモデルに関するドキュメントの更新と追加"
}
```

### Explanation
この変更は、Azure AI StudioにおけるCohereモデルのインストール手順や機能を詳述したドキュメントに対する更新です。新しいCohere Command R+ 08-2024およびCohere Command R 08-2024モデルに関する詳細が追加され、使い方や推奨される使用ケースについての情報が強化されています。具体的には、モデルのアーキテクチャ、サポートされる言語、文脈の長さ、入力と出力の形式が明記されています。

主な変更点は以下の通りです：
- `ms.date`が08/08/2024から09/23/2024に更新されました。
- 新しいモデルに関するセクションが追加され、各モデルの仕様や特徴が詳しく説明されています。
- 既存のモデル情報が整理され、満たすべき条件や推奨事項が更新されています。
- コード例やノートが修正され、最新のモデル名やAPIの使用方法に合わせて調整されています。

これにより、ユーザーは最新の情報に基づいてCohereモデルを適切に利用できるようになります。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -66,7 +66,7 @@ Model | Managed compute | Serverless API (pay-as-you-go)
 --|--|--
 Llama family models | Llama-2-7b <br> Llama-2-7b-chat <br> Llama-2-13b <br> Llama-2-13b-chat <br> Llama-2-70b <br> Llama-2-70b-chat <br> Llama-3-8B-Instruct <br> Llama-3-70B-Instruct <br> Llama-3-8B <br> Llama-3-70B | Llama-3-70B-Instruct <br> Llama-3-8B-Instruct <br> Llama-2-7b <br> Llama-2-7b-chat <br> Llama-2-13b <br> Llama-2-13b-chat <br> Llama-2-70b <br> Llama-2-70b-chat
 Mistral family models | mistralai-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x22B-Instruct-v0-1 <br> mistral-community-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x7B-v01 <br> mistralai-Mistral-7B-Instruct-v0-2 <br> mistralai-Mistral-7B-v01 <br> mistralai-Mixtral-8x7B-Instruct-v01 <br> mistralai-Mistral-7B-Instruct-v01 | Mistral-large (2402) <br> Mistral-large (2407) <br> Mistral-small <br> Mistral-NeMo
-Cohere family models | Not available | Cohere-command-r-plus <br> Cohere-command-r <br> Cohere-embed-v3-english <br> Cohere-embed-v3-multilingual <br> Cohere-rerank-v3-english <br> Cohere-rerank-v3-multilingual
+Cohere family models | Not available | Cohere-command-r-plus-08-2024 <br> Cohere-command-r-08-2024 <br> Cohere-command-r-plus <br> Cohere-command-r <br> Cohere-embed-v3-english <br> Cohere-embed-v3-multilingual <br> Cohere-rerank-v3-english <br> Cohere-rerank-v3-multilingual
 JAIS | Not available | jais-30b-chat
 Phi-3 family models | Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> Phi-3-vision-128k-Instruct <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct | Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct
 Nixtla | Not available | TimeGEN-1
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cohereモデルのバージョン情報の更新"
}
```

### Explanation
この変更は、Azure AI Studioのモデルカタログに関するドキュメントで、Cohereモデルに関する情報が更新されました。具体的には、Cohereのモデル名が新しいバージョン番号を含むように修正されています。

主な変更点は以下の通りです：
- 「Cohere family models」セクションの中で、Cohere-command-r-plusおよびCohere-command-rモデルのバージョンが「08-2024」として更新されました。これにより、最新のモデルバージョンが明示されています。
- その他のCohereモデルのリストについては、依然として変更はありませんが、最新の情報により、利用者がより正確なバージョン情報を得られるようになっています。

これにより、Cohereモデルを利用しようとしているユーザーは、最新のリリース情報に基づいて適切なモデルを選択できるようになります。

## articles/ai-studio/includes/region-availability-maas.md{#item-35d79c}

<details>
<summary>Diff</summary>
````diff
@@ -15,8 +15,10 @@ ms.custom: include, references_regions
 
 |Model   |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
-Cohere Command R      | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar     | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3       | Not available        |
+Cohere Command R+ 08-2024     |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available        |
+Cohere Command R 08-2024     |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available        |
 Cohere Command R+     |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar  |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available        |
+Cohere Command R      | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar     | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3       | Not available        |
 Cohere Rerank 3 - English   |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar  | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available       |
 Cohere Rerank 3 - Multilingual   |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar  | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available       |
 Cohere Embed 3 - English    |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar   |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3    | Not available       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cohereモデルの地域可用性情報の更新"
}
```

### Explanation
この変更は、Azure AI StudioのドキュメントにおけるCohereモデルの地域可用性に関する情報が更新されたものです。具体的には、Cohere Command RおよびCohere Command R+の新しいバージョン（08-2024）が含まれるように、モデル名が修正され、可用性に関する情報が追加されています。

主な変更点は以下の通りです：
- 「Cohere Command R+ 08-2024」および「Cohere Command R 08-2024」という新しいエントリが追加され、地域の可用性が明示されています。
- 他のCohereモデル（Cohere Command R、Cohere Rerank 3など）に関する情報は従来通りに残されており、既存の可用性地域が再確認されています。
- モデル名や対応する地域のリンクが変更されておらず、Microsoftが管理する国々にも言及されています。

この更新により、ユーザーは新しいモデルの可用性について最新の情報を得ることができ、適切な地域で利用できるサービスを選択しやすくなります。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -65,7 +65,7 @@ items:
     - name: Create a project
       href: how-to/create-projects.md
     - name: Create and manage compute
-    href: how-to/create-manage-compute.md
+      href: how-to/create-manage-compute.md
   - name: Connect to services and resources
     items:
     - name: Connections overview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCファイルのリンク修正"
}
```

### Explanation
この変更は、Azure AI Studioの目次ファイル（toc.yml）におけるリンクの修正です。具体的には、「Create and manage compute」という項目のリンクにおいて、ハイフンの位置が修正されました。

主な変更点は以下の通りです：
- 「Create and manage compute」セクションの下にあるリンクが、正しいインデントに合わせて修正されました。この変更は見た目には小さなものですが、YAML形式の構文においては重要です。
- リンク先である「how-to/create-manage-compute.md」の行が正しくインデントされることで、他の項目との整合性が保たれています。

これにより、目次ファイルの可読性が向上し、適切なリンクを利用できるように整備されました。この修正によって、ユーザーは関連する情報に正確にアクセスできるようになります。


