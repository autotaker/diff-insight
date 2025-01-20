---
date: '2025-01-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1d7cc3c...MicrosoftDocs:06d2c74
summary: このコードの更新では、Azure AI Studio関連の複数のドキュメントにおいてAPIのバージョン更新や記載内容の改訂が行われました。これにより、ユーザーは最新のAPI仕様を使用でき、FAQやリクエスト用コードスニペットがより明確かつ読みやすくなります。新しい機能は追加されていませんが、既存の情報が更新され、互換性も維持されています。FAQの表現が若干修正され、モデル推論APIなどのバージョンが最新に更新されました。この変更の目的は、開発者やユーザーが常に最新の情報で作業を進められるようにすることです。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1d7cc3c...MicrosoftDocs:06d2c74){target="_blank"}

# ハイライト
このコードの更新では、Azure AI Studio関連の複数のドキュメントにおいて、APIのバージョン更新や記載内容の改訂が行われています。これにより、ユーザーが最新のAPI仕様を使用できるようになり、FAQやリクエスト用コードスニペットの内容をより明確かつ読みやすくなるよう改善が図られています。

## 新機能
- 特に新機能といえる追加項目は今回の変更には含まれていませんが、既存の情報が最新の仕様に適合するよう更新されています。

## 破壊的変更
- 破壊的な変更は含まれておらず、既存のシステムに対する互換性も維持されています。

## その他の更新
- FAQの内容に若干言葉遣いの修正が加えられ、「あなた」を「彼ら」といった第三者的な表現に変更。
- モデル推論API、チャット完了API、埋め込みベクトルAPI、画像とテキストのペア埋め込みAPI、モデル情報APIのバージョンが全て「2024-05-01-preview」に更新。

# 洞察
この変更は、Azure AI StudioのドキュメントとAPIの最新バージョンを提供するためのもので、主な目的は開発者やユーザーが常に最新の情報に基づいて作業を進められるようにすることです。APIのバージョンを最新のものに更新することで、新たな機能や改善点が確実に利用できるようになります。

APIバージョンの最新化は、主に以下の点で利点があります。第一に、これにより開発者は最新のエンドポイントとパラメータを用いることができ、システムの信頼性が向上します。第二に、ユーザーが最新の仕様を確認し、不一致による動作不良を防ぐことができます。さらに、FAQの更新により、利用者がより直感的にドキュメントを理解できるようになり、ユーザー体験が向上します。

こういったマイナーアップデートでも、正確で最新の情報を提供することは重要であり、特に技術文書においてはその価値が高まります。これにより、製品の信頼性が高まり、ユーザーとのコミュニケーションが改善されることを期待できます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [faq.yml](#item-e7baa2) | minor update | AI Studio FAQの更新 | modified | 5 | 5 | 10 | 
| [reference-model-inference-api.md](#item-9fe240) | minor update | モデル推論APIのバージョン更新 | modified | 4 | 4 | 8 | 
| [reference-model-inference-chat-completions.md](#item-e09823) | minor update | チャット完了APIのバージョン更新 | modified | 1 | 1 | 2 | 
| [reference-model-inference-embeddings.md](#item-5e9064) | minor update | 埋め込みベクトルAPIのバージョン更新 | modified | 1 | 1 | 2 | 
| [reference-model-inference-images-embeddings.md](#item-70c7ac) | minor update | 画像とテキストの埋め込みベクトルAPIのバージョン更新 | modified | 1 | 1 | 2 | 
| [reference-model-inference-info.md](#item-e465b4) | minor update | モデル情報APIのバージョン更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-studio/faq.yml{#item-e7baa2}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ metadata:
   ms.custom:
     - build-2024
   ms.topic: faq
-  ms.date: 5/21/2024
+  ms.date: 01/17/2025
   ms.reviewer: sgilley
   ms.author: sgilley
   author: sdgilley
@@ -25,7 +25,7 @@ sections:
       - question: |
           How can customers access Azure AI Foundry? 
         answer: |
-          Customers can explore Azure AI Foundry unauthenticated - including its cutting-edge AI capabilities. When they're ready to begin using templates, tools, and the robust model catalog to stitch together their own AI solutions, they'll be prompted to register or sign in to their Azure account. During preview, there's no extra charge for using Azure AI Foundry. When deploying solutions, Azure AI services, Azure Machine Learning, and other Azure resources used inside of Azure AI Foundry will be billed at their existing rates. Pricing is subject to change when Azure AI Foundry is generally available.
+          Customers can explore Azure AI Foundry unauthenticated - including its cutting-edge AI capabilities. When you're ready to begin using templates, tools, and the robust model catalog to stitch together your own AI solutions, you're prompted to register or sign in to your Azure account. Currently, there's no extra charge for using Azure AI Foundry. When deploying solutions, you're billed for the Azure AI services, Azure Machine Learning, and other Azure resources used inside of Azure AI Foundry at their existing rates.
       - question: |
           What regions is Azure AI Foundry available in?
         answer: | 
@@ -37,23 +37,23 @@ sections:
       - question: |
           Can I use models other than ChatGPT in Azure AI Foundry portal? 
         answer: |
-          Yes. Azure AI Foundry includes a robust and growing catalog of frontier and open-source models from OpenAI, Hugging Face, Meta and more that can be applied over your data. You can even compare models by task using open-source datasets and evaluate the model with your own test data to see how the pre-trained model would perform to fit your own use case.
+          Yes. Azure AI Foundry includes a robust and growing catalog of frontier and open-source models from OpenAI, Hugging Face, Meta, and more that can be applied over your data. You can even compare models by task using open-source datasets and evaluate the model with your own test data to see how the pretrained model would perform to fit your own use case.
       - question: |
           Will there be multiple varying model benchmarks in Azure AI Foundry portal based on individual projects and data sources? 
         answer: |
           In the model benchmarks view, customers can view varying model benchmarks published by Azure AI. 
       - question: |
           Is prompt flow Microsoft's equivalent to LangChain? 
         answer: |
-          Prompt flow is complementary to LangChain and Semantic Kernel and it can work with either. Prompt flow supports LLMOps for generative AI solutions, providing evaluation, connection management, and flow logic to help debug applications, manage deployment and monitor at scale.
+          Prompt flow is complementary to LangChain and Semantic Kernel and it can work with either. Prompt flow supports LLMOps for generative AI solutions, providing evaluation, connection management, and flow logic to help debug applications, manage deployment, and monitor at scale.
       - question: |
           How is prompt injection handled, and how do we ensure no malicious code is running from prompt injection? 
         answer: |
           Prompt templates in prompt flow provide robust examples and instructions for avoiding prompt injection attacks in the application. Azure AI Content Safety helps detect offensive or inappropriate content in text and images. Content moderation also checks for jailbreaks.
       - question: |
           What is the billing model for Model-as-a-Service (MaaS)? 
         answer: |
-          Azure AI Foundry offers paygo inference APIs and hosted fine-tuning for [Llama 2 family models](how-to/deploy-models-llama.md). During preview, there's no extra charge for Azure AI Foundry outside of typical AI services and other Azure resource charges.
+          Azure AI Foundry offers pay-as-you-go inference APIs and hosted fine-tuning for [Llama 2 family models](how-to/deploy-models-llama.md). Currently, there's no extra charge for Azure AI Foundry outside of typical AI services and other Azure resource charges.
       - question: |
           Can all models be secured with content filtering? 
         answer: |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Studio FAQの更新"
}
```

### Explanation
このコードの変更は、Azure AI StudioのFAQセクションに対するマイナーな更新を反映しています。具体的には、いくつかの回答における日付や文体の変更が含まれています。日付が2024年5月21日から2025年1月17日に更新され、また一貫性を持たせるために「あなた」という言葉が「彼ら」から置き換えられるなど、より個別的かつ直接的な表現が含まれています。さらに、プレトレーニングされたモデルについて、利用に関する料金の表現も改善されています。この変更は、FAQの記述をより明確で読みやすくし、利用者の理解を助けることを目的としています。

## articles/ai-studio/reference/reference-model-inference-api.md{#item-9fe240}

<details>
<summary>Diff</summary>
````diff
@@ -202,7 +202,7 @@ Use the reference section to explore the API design and which parameters are ava
 __Request__
 
 ```HTTP/1.1
-POST /chat/completions?api-version=2024-04-01-preview
+POST /chat/completions?api-version=2024-05-01-preview
 Authorization: Bearer <bearer-token>
 Content-Type: application/json
 ```
@@ -277,7 +277,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 __Request__
 
 ```HTTP/1.1
-POST /chat/completions?api-version=2024-04-01-preview
+POST /chat/completions?api-version=2024-05-01-preview
 Authorization: Bearer <bearer-token>
 Content-Type: application/json
 extra-parameters: pass-through
@@ -411,7 +411,7 @@ catch (RequestFailedException ex)
 __Request__
 
 ```HTTP/1.1
-POST /chat/completions?api-version=2024-04-01-preview
+POST /chat/completions?api-version=2024-05-01-preview
 Authorization: Bearer <bearer-token>
 Content-Type: application/json
 ```
@@ -552,7 +552,7 @@ catch (RequestFailedException ex)
 __Request__
 
 ```HTTP/1.1
-POST /chat/completions?api-version=2024-04-01-preview
+POST /chat/completions?api-version=2024-05-01-preview
 Authorization: Bearer <bearer-token>
 Content-Type: application/json
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル推論APIのバージョン更新"
}
```

### Explanation
この変更は、Azure AI Studioのモデル推論APIに関連するドキュメントの一部を更新したもので、APIのバージョンを「2024-04-01-preview」から「2024-05-01-preview」に変更しています。この変更は、コードスニペット内のすべての関連するリクエスト部分で行われており、APIのエンドポイントが最新のものに適応していることを示しています。この更新は、ユーザーが常に最新のAPI仕様を使用できるようにするためのものであり、特に開発者にとっては、正確な情報に基づいて作業を行えるようにするために重要です。

## articles/ai-studio/reference/reference-model-inference-chat-completions.md{#item-e09823}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ ms.custom:
 Creates a model response for the given chat conversation.
 
 ```http
-POST /chat/completions?api-version=2024-04-01-preview
+POST /chat/completions?api-version=2024-05-01-preview
 ```
 
 ## URI Parameters
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャット完了APIのバージョン更新"
}
```

### Explanation
この変更は、Azure AI Studioのチャット完了APIに関するドキュメントの更新で、HTTPリクエストのエンドポイントに記載されているAPIのバージョンを「2024-04-01-preview」から「2024-05-01-preview」に変更しています。この更新は、現在使用しているAPIの最新バージョンを反映しており、開発者やユーザーが最新の仕様に基づいて作業できるようにすることを目的としています。変更は小規模ですが、正確な仕様を維持することは、製品の信頼性と整合性を保つ上で非常に重要です。

## articles/ai-studio/reference/reference-model-inference-embeddings.md{#item-5e9064}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ ms.custom:
 Creates an embedding vector representing the input text.
 
 ```http
-POST /embeddings?api-version=2024-04-01-preview
+POST /embeddings?api-version=2024-05-01-preview
 ```
 
 ## URI Parameters
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "埋め込みベクトルAPIのバージョン更新"
}
```

### Explanation
この変更は、Azure AI Studioの埋め込みベクトルAPIに関連するドキュメントの更新です。具体的には、HTTPリクエストのエンドポイントに示されているAPIのバージョンを「2024-04-01-preview」から「2024-05-01-preview」に変更しています。この更新により、ドキュメントが最新のAPIバージョンを反映し、ユーザーが正確な情報に基づいて作業できるようになっています。変更はわずかですが、最新の仕様を提供することは、ユーザー体験の向上に寄与します。このようなマイナーアップデートは、APIの信頼性を保ち、常に最新の情報をユーザーに提供することを目的としています。

## articles/ai-studio/reference/reference-model-inference-images-embeddings.md{#item-70c7ac}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ ms.custom:
 Creates an embedding vector representing the input image and text pair.
 
 ```http
-POST /images/embeddings?api-version=2024-04-01-preview
+POST /images/embeddings?api-version=2024-05-01-preview
 ```
 
 ## URI Parameters
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像とテキストの埋め込みベクトルAPIのバージョン更新"
}
```

### Explanation
この変更は、Azure AI Studioの画像とテキストのペアに関連する埋め込みベクトルAPIのドキュメントに対する更新です。具体的には、HTTPリクエストのエンドポイントに記載されているAPIのバージョンが「2024-04-01-preview」から「2024-05-01-preview」に変更されました。この変更により、ドキュメントが最新のAPIバージョンを反映し、開発者やユーザーが適切な情報に基づいて作業できることを目的としています。変更は僅かですが、正確で最新の情報を提供することは、ユーザーの利便性向上に寄与します。このようなマイナーアップデートは、APIの整合性を保つ上での重要な一歩となります。

## articles/ai-studio/reference/reference-model-inference-info.md{#item-e465b4}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ ms.custom:
 Returns the information about the model deployed under the endpoint.
 
 ```http
-GET /info?api-version=2024-04-01-preview
+GET /info?api-version=2024-05-01-preview
 ```
 
 ## URI Parameters
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル情報APIのバージョン更新"
}
```

### Explanation
この変更は、Azure AI Studioにおけるモデル情報の取得に関するAPIのドキュメントの更新です。具体的には、HTTPリクエストのエンドポイントで示されているAPIのバージョンが「2024-04-01-preview」から「2024-05-01-preview」に更新されています。このマイナーな変更により、ドキュメントは最新のAPIバージョンを反映し、ユーザーが新しい機能や修正された点を正しく利用できるようになります。正確なAPI情報の提供は、開発者にとって重要であり、最新の仕様に基づいて作業することで、システムの信頼性と効率が向上します。


