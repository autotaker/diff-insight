---
date: '2024-11-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7c64df0...MicrosoftDocs:635ff11
summary: このコード変更では、Azure OpenAIのドキュメントが更新され、新しいTypeScript向けクイックスタートガイドの追加やAPIのバージョンと仕様の更新が行われました。これにより、いくつかの破壊的変更が生じ、ユーザーはAPIの使用方法を見直す必要があります。また、地域ごとの利用可能性に関する情報も追加され、ユーザーエクスペリエンスが向上しています。全体として、これらの変更はAzure
  OpenAIサービスの最新の情報や機能を提供し、ユーザーの利便性を高めることを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7c64df0...MicrosoftDocs:635ff11){target="_blank"}

# Highlights
このコード変更では、Azure OpenAIのドキュメントが多岐にわたる内容で更新され、非常に詳細な追加や修正が施されています。特に新機能として、TypeScriptを使用したクイックスタートガイドの追加が目立ちます。また、APIのバージョンや仕様の更新により、いくつかの破壊的変更があります。これらの変更は、ユーザーに最新の情報や機能を提供するために行われています。

## New features
- **TypeScript向けクイックスタートガイド**: TypeScriptを使ったAzure OpenAIサービスの利用方法に関する新しいガイドが追加されています。
- **Datazone standard model availability**: 地域ごとの利用可能性に関する詳細情報の追加。

## Breaking changes
- **最新の推論APIの更新**: 主要パラメータの追加・変更に伴い、以前のバージョンとの互換性が失われる可能性があるため、ユーザーはAPIの使用方法を見直す必要があります。

## Other updates
- APIバージョンやリリース日、仕様の更新。
- FAQセクションやモデルの可用性に関する情報が整理され、最新化されました。
- 各ドキュメントには、地域情報の追加やリンクの訂正、内容の精緻化が含まれています。

# Insights
このコード変更は、Azure OpenAIドキュメントの最新性と正確性を高め、ユーザーエクスペリエンスを向上させることを目的としています。特にTypeScriptに関する新機能の追加は、TypeScriptを利用する開発者へのサポートを強化する狙いがあり、開発者コミュニティにとって非常に有益な追加です。また、APIのバージョン更新や仕様の詳細化により、ユーザーが最新の情報に基づいて効率的にAzure OpenAIサービスを利用できるようにしています。

地域可用性情報に関する文書の更新は、国際展開するサービスで特に重要な要素です。これにより、ユーザーは使用可能なリソースを正確に把握し、ビジネスニーズに合わせてAzure OpenAIを効果的に利用することができます。全体的に、これらの変更はユーザーの利便性とサービスの信頼性を高め、組織のデジタル変革をサポートします。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [api-version-deprecation.md](#item-1cad50) | minor update | APIバージョンの更新と日付の変更 | modified | 2 | 4 | 6 | 
| [assistants-quickstart.md](#item-eaf614) | minor update | TypeScript用のクイックスタートセクションの追加 | modified | 6 | 0 | 6 | 
| [chatgpt-quickstart.md](#item-0634b2) | minor update | TypeScript用のクイックスタートセクションの追加 | modified | 6 | 0 | 6 | 
| [models.md](#item-db2c37) | minor update | データゾーン標準モデルの可用性セクションの更新 | modified | 6 | 7 | 13 | 
| [faq.yml](#item-6deb71) | minor update | Azure OpenAI FAQセクションの更新 | modified | 5 | 5 | 10 | 
| [batch.md](#item-a131d5) | minor update | グローバルバッチの地域情報の更新 | modified | 1 | 3 | 4 | 
| [gpt-with-vision.md](#item-4d8502) | minor update | Azure OpenAI画像トークン情報の更新 | modified | 1 | 1 | 2 | 
| [api-surface.md](#item-a25fa2) | minor update | APIサーフェスのリリース日付更新 | modified | 4 | 4 | 8 | 
| [latest-inference.md](#item-b30a63) | breaking change | 最新の推論APIドキュメントの更新 | modified | 437 | 287 | 724 | 
| [assistants-javascript.md](#item-ad3627) | minor update | JavaScript用のAzure OpenAIサービスのクイックスタート改訂 | modified | 21 | 287 | 308 | 
| [assistants-typescript.md](#item-3195a9) | new feature | Azure OpenAIサービスのTypeScript用クイックスタートガイドの追加 | added | 391 | 0 | 391 | 
| [chatgpt-javascript.md](#item-cbf09f) | minor update | ChatGPT用JavaScriptガイドの改訂 | modified | 32 | 185 | 217 | 
| [chatgpt-typescript.md](#item-6d2f1f) | new feature | Azure OpenAIサービスを使用したTypeScriptのクイックスタートガイドの追加 | added | 241 | 0 | 241 | 
| [javascript.md](#item-f4828f) | minor update | JavaScript SDKに関するガイドの修正 | modified | 29 | 184 | 213 | 
| [datazone-standard.md](#item-188333) | new feature | グローバルバッチモデルの地域Availabilityに関するDatazone標準モデルの追加 | added | 24 | 0 | 24 | 
| [global-batch.md](#item-929e6a) | minor update | グローバルバッチモデルの地域可用性に関する情報の更新 | modified | 7 | 2 | 9 | 
| [provisioned-models.md](#item-8ee639) | minor update | プロビジョニングモデルの地域可用性に関する情報の更新 | modified | 5 | 4 | 9 | 
| [standard-audio.md](#item-1d8db7) | minor update | 標準音声モデルの地域可用性に関する情報の更新 | modified | 1 | 0 | 1 | 
| [standard-chat-completions.md](#item-aae3f1) | minor update | 標準チャット完了モデルの情報更新 | modified | 2 | 1 | 3 | 
| [standard-embeddings.md](#item-656427) | minor update | 標準埋め込みモデルの情報更新 | modified | 3 | 1 | 4 | 
| [standard-global.md](#item-17a84b) | minor update | 標準グローバルモデルの情報更新 | modified | 2 | 1 | 3 | 
| [standard-models.md](#item-af04c4) | minor update | 標準モデルの地域情報更新 | modified | 3 | 1 | 4 | 
| [typescript.md](#item-ee5b93) | new feature | Azure OpenAIサービスでTypeScriptを使用するためのクイックスタートガイドを追加 | added | 223 | 0 | 223 | 
| [use-your-data-javascript.md](#item-786699) | minor update | Node.jsアプリケーションの初期化およびサンプルコードの変更 | modified | 20 | 34 | 54 | 
| [use-your-data-typescript.md](#item-ec0b7e) | new feature | TypeScriptを使用したデータの利用に関するガイドを追加 | added | 245 | 0 | 245 | 
| [overview.md](#item-97d507) | minor update | 画像トークンに関する詳細を更新 | modified | 23 | 22 | 45 | 
| [quickstart.md](#item-7d1656) | minor update | TypeScript向けクイックスタートガイドへのリンクを追加 | modified | 5 | 0 | 5 | 
| [reference.md](#item-7b1183) | minor update | 日付と仕様バージョンの更新 | modified | 2 | 2 | 4 | 
| [use-your-data-quickstart.md](#item-52c1f4) | minor update | TypeScriptに関する内容の強化と日付の更新 | modified | 18 | 8 | 26 | 
| [whats-new.md](#item-53303b) | minor update | 新しいデータゾーン標準展開タイプの説明を更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/openai/api-version-deprecation.md{#item-1cad50}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 10/16/2024
+ms.date: 11/01/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -79,9 +79,7 @@ This version contains support for the latest Azure OpenAI features including:
 
 ## Latest GA API release
 
-Azure OpenAI API version [2024-06-01](./reference.md) is currently the latest GA API release. This API version is the replacement for the previous `2024-02-01` GA API release.
-
-This version contains support for the latest GA features like Whisper, DALL-E 3, fine-tuning, on your data, etc. Any preview features that were released after the `2023-12-01-preview` release like Assistants, TTS, certain on your data datasources, are only supported in the latest preview API releases.
+Azure OpenAI API version [2024-10-21](./reference.md) is currently the latest GA API release. This API version is the replacement for the previous `2024-06-01` GA API release.
 
 ## Updating API versions
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新と日付の変更"
}
```

### Explanation
この変更は、Azure OpenAI APIのドキュメントにおいて、最新のGA（一般提供）APIリリースの日付とバージョン情報を更新したものです。具体的には、ファイル内のバージョン番号が「2024-06-01」から「2024-10-21」に変更され、関連する日付も「2024年10月16日」から「2024年11月1日」に更新されました。このアップデートにより、最新のAPI情報が正確に反映され、ユーザーが適切な情報を持つことができるようになります。また、以前のバージョンや最近のプレビュー機能についての記述が削除され、文書を簡潔に保つ工夫もされています。

## articles/ai-services/openai/assistants-quickstart.md{#item-eaf614}

<details>
<summary>Diff</summary>
````diff
@@ -42,6 +42,12 @@ Azure OpenAI Assistants (Preview) allows you to create AI assistants tailored to
 
 ::: zone-end
 
+::: zone pivot="programming-language-typescript"
+
+[!INCLUDE [TypeScript quickstart](includes/assistants-typescript.md)]
+
+::: zone-end
+
 ::: zone pivot="rest-api"
 
 [!INCLUDE [REST API quickstart](includes/assistants-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScript用のクイックスタートセクションの追加"
}
```

### Explanation
この変更は、Azure OpenAI Assistantsのクイックスタートガイドにおいて、TypeScriptに関する情報を新たに追加したものです。具体的には、TypeScript用のクイックスタートセクションが新設され、対応するインクルードファイルへの参照が追加されました。これにより、ユーザーはTypeScriptを使用してAIアシスタントを作成する際の手順を簡単に確認できるようになります。このアップデートにより、特にTypeScriptを使用する開発者に対して、さらに充実した情報を提供することが可能となり、全体のドキュメントの価値が向上します。

## articles/ai-services/openai/chatgpt-quickstart.md{#item-0634b2}

<details>
<summary>Diff</summary>
````diff
@@ -54,6 +54,12 @@ Use this article to get started using Azure OpenAI.
 
 ::: zone-end
 
+::: zone pivot="programming-language-typescript"
+
+[!INCLUDE [TypeScript quickstart](includes/chatgpt-typescript.md)]
+
+::: zone-end
+
 ::: zone pivot="programming-language-python"
 
 [!INCLUDE [Python SDK quickstart](includes/chatgpt-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScript用のクイックスタートセクションの追加"
}
```

### Explanation
この変更は、Azure OpenAI ChatGPTのクイックスタートガイドにおいて、TypeScriptに関する情報を新たに追加したものです。具体的には、TypeScript用のクイックスタートセクションが新設され、対応するインクルードファイルへの参照が追加されています。これにより、ユーザーはTypeScriptを使ってChatGPTを利用する際の手順をより容易に確認できるようになり、特にTypeScriptを使用する開発者に対する支援が強化されています。このアップデートは、ドキュメント全体の情報を充実させ、さまざまなプログラミング言語に対応したリソースを提供することを目的としています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -384,6 +384,12 @@ All deployments can perform the exact same inference operations, however the bil
 
 [!INCLUDE [Global batch](../includes/model-matrix/global-batch.md)]
 
+# [Data Zone Standard](#tab/datazone-standard)
+
+### Data zone standard model availability
+
+[!INCLUDE [Global batch](../includes/model-matrix/datazone-standard.md)]
+
 # [Standard](#tab/standard)
 
 ### Standard deployment model availability
@@ -405,13 +411,6 @@ For more information on Provisioned deployments, see our [Provisioned guidance](
 
 This table doesn't include fine-tuning regional availability information.  Consult the [fine-tuning section](#fine-tuning-models) for this information.
 
-### Data zone standard model availability
-
-|Model|United States Data zone regions|European Union Data zone regions|
-|---|---|---|
-| `gpt-4o` (2024-08-06, 2024-05-13)| East US 2 <br> West US 3 <br> | Spain Central <br> West Europe|
-| `gpt-4o-mini` (2024-07-18) | East US 2 <br> West US 3 <br> | Spain Central <br> West Europe|
-
 ### Standard models by endpoint
 
 # [Chat Completions](#tab/standard-chat-completions)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データゾーン標準モデルの可用性セクションの更新"
}
```

### Explanation
この変更は、Azure OpenAIのモデルに関するドキュメントの内容を更新し、データゾーンの標準モデルの可用性に関する新しいセクションを追加したものです。具体的には、データゾーンの標準モデルの利用可能性についての情報が新しいタブとして設けられ、これに関連するインクルードファイルへのリンクも追加されています。また、以前のセクションが削除されることで、情報が整理され、理解しやすくなっています。このアップデートにより、ユーザーは最新のモデル可用性についての具体的な情報をより簡単に確認できるようになります。全体として、ドキュメントの内容が洗練され、情報のアクセス性が向上しています。

## articles/ai-services/openai/faq.yml{#item-6deb71}

<details>
<summary>Diff</summary>
````diff
@@ -162,6 +162,10 @@ sections:
           Where can I find out what region a model is available in?
         answer: |
           Consult the Azure OpenAI [model availability guide](./concepts/models.md#model-summary-table-and-region-availability) for region availability.
+      - question: |
+          What are the SLAs (Service Level Agreements) in Azure OpenAI?
+        answer:
+          We do offer an Availability SLA for all resources and a Latency SLA for Provisioned-Managed Deployments. For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page](https://azure.microsoft.com/support/legal/sla/cognitive-services/v1_1/). 
       - question: |
           How do I enable fine-tuning? Create a custom model is greyed out in Azure AI Studio.  
         answer: |
@@ -173,11 +177,7 @@ sections:
       - question: |
           What is the maximum number of fine-tuned models I can create?
         answer: |
-          100
-      - question: |
-          What are the SLAs for API responses in Azure OpenAI?
-        answer:
-          We don't have a defined API response time Service Level Agreement (SLA) at this time. For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page](https://azure.microsoft.com/support/legal/sla/cognitive-services/v1_1/).  
+          100  
       - question: |
           Why was my fine-tuned model deployment deleted? 
         answer:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI FAQセクションの更新"
}
```

### Explanation
この変更は、Azure OpenAIのFAQ（よくある質問）セクションを更新し、新たにサービスレベルアグリーメント（SLA）に関する質問を追加したものです。具体的には、Azure OpenAIに関するSLAの詳細を尋ねる新しい質問が追加され、その回答として全リソースに対する可用性SLAと、プロビジョン管理型デプロイメントに対するレイテンシSLAについて説明しています。また、以前にあったAPIレスポンスに関するSLAの質問は削除され、その代わりに回答の内容がわかりやすく整理されています。このアップデートは、ユーザーがAzure OpenAIサービスに関する重要な情報を容易に探索できるようにし、ドキュメントの正確性を向上させることを目的としています。全体として、FAQの内容がより明確かつ最新の情報に基づいていることが反映されています。

## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -44,9 +44,7 @@ Key use cases include:
 
 Global batch is currently supported in the following regions:
 
-- East US
-- West US
-- Sweden Central
+[!INCLUDE [Global batch](../includes/model-matrix/global-batch.md)]
 
 The following models support global batch:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルバッチの地域情報の更新"
}
```

### Explanation
この変更では、Azure OpenAIのバッチ処理に関するドキュメントにおいて、グローバルバッチが現在サポートされている地域の情報を更新しています。具体的には、以前列挙されていた地域（東米、西米、スウェーデン中央）が削除され、その代わりに、地域情報を提供するためのインクルードファイルへのリンクが追加されました。この変更により、ユーザーは最新の地域情報を一元的に確認できるようになり、ドキュメントのメンテナンスが容易になります。全体として、情報の整理が進み、利用者にとってのアクセス性が向上しています。

## articles/ai-services/openai/how-to/gpt-with-vision.md{#item-4d8502}

<details>
<summary>Diff</summary>
````diff
@@ -247,7 +247,7 @@ The _detail_ parameter in the model offers three choices: `low`, `high`, or `aut
 - `low` setting: the model does not activate the "high res" mode, instead processes a lower resolution 512x512 version, resulting in quicker responses and reduced token consumption for scenarios where fine detail isn't crucial.
 - `high` setting: the model activates "high res" mode. Here, the model initially views the low-resolution image and then generates detailed 512x512 segments from the input image. Each segment uses double the token budget, allowing for a more detailed interpretation of the image.''
 
-For details on how the image parameters impact tokens used and pricing please see - [What is OpenAI? Image Tokens with GPT-4 Turbo with Vision](../overview.md#image-tokens-gpt-4-turbo-with-vision-and-gpt-4o)
+For details on how the image parameters impact tokens used and pricing please see - [What is Azure OpenAI? Image Tokens](../overview.md#image-tokens)
 
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI画像トークン情報の更新"
}
```

### Explanation
この変更では、Azure OpenAIの「GPT with Vision」に関するドキュメントの一部を更新し、画像パラメータがトークン使用量と価格に与える影響についてのリンク表記を修正しています。具体的には、以前のリンクが「OpenAI」に関する情報を指していたのに対し、現在は「Azure OpenAI」に関連する情報に変更されました。この変更により、ユーザーは正確で関連性のある情報にアクセスしやすくなり、製品の理解を深めることができます。全体として、ドキュメントの正確性と明瞭さが向上しています。

## articles/ai-services/openai/includes/api-surface.md{#item-a25fa2}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Information on the division of control plane and data plane API sur
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 09/09/2024
+ms.date: 11/01/2024
 ---
 
 
@@ -21,9 +21,9 @@ Each API surface/specification encapsulates a different set of Azure OpenAI capa
 
 | API | Latest preview release | Latest GA release | Specifications | Description |
 |:---|:----|:----|:----|:---|
-| **Control plane** | [`2024-06-01-preview`](/rest/api/aiservices/accountmanagement/operation-groups?view=rest-aiservices-accountmanagement-2024-06-01-preview&preserve-view=true) | [`2023-05-01`](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices) | Azure OpenAI shares a common control plane with all other Azure AI Services. The control plane API is used for things like [creating Azure OpenAI resources](/rest/api/aiservices/accountmanagement/accounts/create?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), [model deployment](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), and other higher level resource management tasks. The control plane also governs what is possible to do with capabilities like Azure Resource Manager, Bicep, Terraform, and Azure CLI.|
-| **Data plane - authoring** | `2024-10-01-preview` | [`2024-06-01`](/rest/api/azureopenai/operation-groups?view=rest-azureopenai-2024-06-01&preserve-view=true) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
-| **Data plane - inference** | [`2024-10-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-06-01`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, speech/whisper, on your data, Dall-e, assistants, etc. |
+| **Control plane** | [`2024-06-01-preview`](/rest/api/aiservices/accountmanagement/operation-groups?view=rest-aiservices-accountmanagement-2024-06-01-preview&preserve-view=true) | [`2024-10-01`](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices) | Azure OpenAI shares a common control plane with all other Azure AI Services. The control plane API is used for things like [creating Azure OpenAI resources](/rest/api/aiservices/accountmanagement/accounts/create?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), [model deployment](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), and other higher level resource management tasks. The control plane also governs what is possible to do with capabilities like Azure Resource Manager, Bicep, Terraform, and Azure CLI.|
+| **Data plane - authoring** | `2024-10-01-preview` | `2024-10-21` | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
+| **Data plane - inference** | [`2024-10-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-10-21`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, speech/whisper, on your data, Dall-e, assistants, etc. |
 
 ## Authentication
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIサーフェスのリリース日付更新"
}
```

### Explanation
この変更では、Azure OpenAI関連のAPIサーフェスに関するドキュメントの一部を更新しています。具体的には、コントロールプレーンおよびデータプレーンの最新のGA（一般提供）リリースの日付が更新されており、情報はより正確になっています。また、マークダウン内での関連するリンクや記述の修正も行われています。この変更によって、ユーザーは最新のAPIリリース情報にアクセスでき、Azure OpenAIサービスの利用に対する理解を深めることができます。全体として、ドキュメントの信頼性と正確性が向上しています。

## articles/ai-services/openai/includes/api-versions/latest-inference.md{#item-b30a63}

<details>
<summary>Diff</summary>
````diff
@@ -5,23 +5,23 @@ description: Latest data plane inference documentation generated from OpenAPI 3.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 07/09/2024
+ms.date: 11/01/2024
 ---
 
 ## Completions
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/completions?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/completions?api-version=2024-10-21
 ```
 
-Creates a completion for the provided prompt, parameters and chosen model.
+Creates a completion for the provided prompt, parameters, and chosen model.
 
 ### URI Parameters
 
 | Name | In | Required | Type | Description |
 |------|------|----------|------|-----------|
 | endpoint | path | Yes | string<br>url | Supported Azure OpenAI endpoints (protocol and hostname, for example: `https://aoairesource.openai.azure.com`. Replace "aoairesource" with your Azure OpenAI resource name). https://{your-resource-name}.openai.azure.com |
-| deployment-id | path | Yes | string | Deployment id of the model which was deployed. |
+| deployment-id | path | Yes | string | Deployment ID of the model which was deployed. |
 | api-version | query | Yes | string | API version |
 
 ### Request Header
@@ -36,53 +36,33 @@ Creates a completion for the provided prompt, parameters and chosen model.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| prompt | string or array | The prompt(s) to generate completions for, encoded as a string or array of strings.<br>Note that <&#124;endoftext&#124;> is the document separator that the model sees during training, so if a prompt isn'tspecified the model will generate as if from the beginning of a new document. Maximum allowed size of string list is 2048. | No |  |
-| max_tokens | integer | The token count of your prompt plus max_tokens can't exceed the model's context length. Most models have a context length of 2048 tokens (except for the newest models, which support 4096). Has minimum of 0. | No | 16 |
-| temperature | number | What sampling temperature to use. Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (arg max sampling) for ones with a well-defined answer.<br>We generally recommend altering this or top_p but not both. | No | 1 |
-| top_p | number | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br>We generally recommend altering this or temperature but not both. | No | 1 |
-| logit_bias | object | Defaults to null. Modify the likelihood of specified tokens appearing in the completion. Accepts a json object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100. You can use this tokenizer tool (which works for both GPT-2 and GPT-3) to convert text to token IDs. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. As an example, you can pass {"50256"&#58;-100} to prevent the <&#124;endoftext&#124;> token from being generated. | No |  |
-| user | string | A unique identifier representing your end-user, which can help monitoring and detecting abuse | No |  |
-| n | integer | How many completions to generate for each prompt. Minimum of 1 and maximum of 128 allowed.<br>Note: Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for max_tokens and stop. | No | 1 |
-| stream | boolean | Whether to stream back partial progress. If set, tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a data: [DONE] message. | No | False |
-| logprobs | integer | Include the log probabilities on the logprobs most likely tokens, as well the chosen tokens. For example, if logprobs is 5, the API will return a list of the 5 most likely tokens. The API will always return the logprob of the sampled token, so there may be up to logprobs+1 elements in the response.<br>Minimum of 0 and maximum of 5 allowed. | No | None |
-| suffix | string | The suffix that comes after a completion of inserted text. | No |  |
-| echo | boolean | Echo back the prompt in addition to the completion | No | False |
-| stop | string or array | Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence. | No |  |
-| completion_config | string |  | No |  |
-| presence_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. | No | 0 |
-| frequency_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. | No | 0 |
-| best_of | integer | Generates best_of completions server-side and returns the "best" (defined as the one with the highest log probability per token). Results can't be streamed.<br>When used with n, best_of controls the number of candidate completions and n specifies how many to return - best_of must be greater than n.<br>Note: Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for max_tokens and stop. Has maximum value of 128. | No |  |
+| prompt | string or array | The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.<br><br>Note that <&#124;endoftext&#124;> is the document separator that the model sees during training, so if a prompt isn't specified the model will generate as if from the beginning of a new document.<br> | Yes |  |
+| best_of | integer | Generates `best_of` completions server-side and returns the "best" (the one with the highest log probability per token). Results can't be streamed.<br><br>When used with `n`, `best_of` controls the number of candidate completions and `n` specifies how many to return â€“ `best_of` must be greater than `n`.<br><br>**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.<br> | No | 1 |
+| echo | boolean | Echo back the prompt in addition to the completion<br> | No | False |
+| frequency_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.<br> | No | 0 |
+| logit_bias | object | Modify the likelihood of specified tokens appearing in the completion.<br><br>Accepts a JSON object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.<br><br>As an example, you can pass `{"50256": -100}` to prevent the <&#124;endoftext&#124;> token from being generated.<br> | No | None |
+| logprobs | integer | Include the log probabilities on the `logprobs` most likely output tokens, as well the chosen tokens. For example, if `logprobs` is 5, the API will return a list of the five most likely tokens. The API will always return the `logprob` of the sampled token, so there may be up to `logprobs+1` elements in the response.<br><br>The maximum value for `logprobs` is 5.<br> | No | None |
+| max_tokens | integer | The maximum number of tokens that can be generated in the completion.<br><br>The token count of your prompt plus `max_tokens` can't exceed the model's context length. | No | 16 |
+| n | integer | How many completions to generate for each prompt.<br><br>**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.<br> | No | 1 |
+| presence_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.<br> | No | 0 |
+| seed | integer | If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.<br><br>Determinism isn't guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.<br> | No |  |
+| stop | string or array | Up to four sequences where the API will stop generating further tokens. The returned text won't contain the stop sequence.<br> | No |  |
+| stream | boolean | Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. | No | False |
+| suffix | string | The suffix that comes after a completion of inserted text.<br><br>This parameter is only supported for `gpt-3.5-turbo-instruct`.<br> | No | None |
+| temperature | number | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.<br><br>We generally recommend altering this or `top_p` but not both.<br> | No | 1 |
+| top_p | number | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br><br>We generally recommend altering this or `temperature` but not both.<br> | No | 1 |
+| user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse.<br> | No |  |
 
 ### Responses
 
-| Name | Type | Description | Required | Default |
-|------|------|-------------|----------|---------|
-| id | string |  | Yes |  |
-| object | string |  | Yes |  |
-| created | integer |  | Yes |  |
-| model | string |  | Yes |  |
-| prompt_filter_results | [promptFilterResults](#promptfilterresults) | Content filtering results for zero or more prompts in the request. In a streaming request, results for different prompts may arrive at different times or in different orders. | No |  |
-| choices | array |  | Yes |  |
-| usage | object |  | No |  |
-
-
-### Properties for usage
-
-#### completion_tokens
-
-| Name | Type | Description | Default |
-|------|------|-------------|--------|
-| completion_tokens | number |  |  |
-| prompt_tokens | number |  |  |
-| total_tokens | number |  |  |
-
 **Status Code:** 200
 
 **Description**: OK 
 
 |**Content-Type**|**Type**|**Description**|
 |:---|:---|:---|
-|application/json | object | |
+|application/json | [createCompletionResponse](#createcompletionresponse) | Represents a completion response from the API. Note: both the streamed and nonstreamed response objects share the same shape (unlike the chat endpoint).
+|
 
 **Status Code:** default
 
@@ -96,10 +76,10 @@ Creates a completion for the provided prompt, parameters and chosen model.
 
 ### Example
 
-Creates a completion for the provided prompt, parameters and chosen model.
+Creates a completion for the provided prompt, parameters, and chosen model.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/completions?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/completions?api-version=2024-10-21
 
 {
  "prompt": [
@@ -139,7 +119,7 @@ Status Code: 200
 ## Embeddings
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/embeddings?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/embeddings?api-version=2024-10-21
 ```
 
 Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms.
@@ -164,7 +144,7 @@ Get a vector representation of a given input that can be easily consumed by mach
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| input | string or array | Input text to get embeddings for, encoded as a string. To get embeddings for multiple inputs in a single request, pass an array of strings. Each array must not exceed 2048 inputs in length.<br>Unless you're embedding code, we suggest replacing newlines (\n) in your input with a single space, as we have observed inferior results when newlines are present. | Yes |  |
+| input | string or array | Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays. The input must not exceed the max input tokens for the model (8,192 tokens for `text-embedding-ada-002`), can't be an empty string, and any array must be 2,048 dimensions or less.| Yes |  |
 | user | string | A unique identifier representing your end-user, which can help monitoring and detecting abuse. | No |  |
 | input_type | string | input type of embedding search to use | No |  |
 | encoding_format | string | The format to return the embeddings in. Can be either `float` or `base64`. Defaults to `float`. | No |  |
@@ -210,7 +190,7 @@ Get a vector representation of a given input that can be easily consumed by mach
 Return the embeddings for a given prompt.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/embeddings?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/embeddings?api-version=2024-10-21
 
 {
  "input": [
@@ -248,6 +228,29 @@ Status Code: 200
           0.020790534,
           0.00074595667,
           0.008397198,
+          -0.00535031,
+          0.008968075,
+          0.014351576,
+          -0.014086051,
+          0.015055214,
+          -0.022211088,
+          -0.025198232,
+          0.0065186154,
+          -0.036350243,
+          0.009180495,
+          -0.009698266,
+          0.009446018,
+          -0.008463579,
+          -0.0040426035,
+          -0.03443847,
+          -0.00091273896,
+          -0.0019217303,
+          0.002349888,
+          -0.021560553,
+          0.016515596,
+          -0.015572986,
+          0.0038666942,
+          -8.432463e-05
         ]
       }
     ],
@@ -259,10 +262,10 @@ Status Code: 200
 }
 ```
 
-## Chat completions
+## Chat completions 
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-10-21
 ```
 
 Creates a completion for the chat message
@@ -272,7 +275,7 @@ Creates a completion for the chat message
 | Name | In | Required | Type | Description |
 |------|------|----------|------|-----------|
 | endpoint | path | Yes | string<br>url | Supported Azure OpenAI endpoints (protocol and hostname, for example: `https://aoairesource.openai.azure.com`. Replace "aoairesource" with your Azure OpenAI resource name). https://{your-resource-name}.openai.azure.com |
-| deployment-id | path | Yes | string | Deployment id of the model which was deployed. |
+| deployment-id | path | Yes | string | Deployment ID of the model which was deployed. |
 | api-version | query | Yes | string | API version |
 
 ### Request Header
@@ -287,35 +290,28 @@ Creates a completion for the chat message
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| temperature | number | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.<br>We generally recommend altering this or `top_p` but not both. | No | 1 |
-| top_p | number | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br>We generally recommend altering this or `temperature` but not both. | No | 1 |
-| stream | boolean | If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a `data: [DONE]` message. | No | False |
-| stop | string or array | Up to 4 sequences where the API will stop generating further tokens. | No |  |
-| max_tokens | integer | The maximum number of tokens allowed for the generated answer. By default, the number of tokens the model can return will be (4096 - prompt tokens). | No | 4096 |
-| presence_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. | No | 0 |
-| frequency_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. | No | 0 |
-| logit_bias | object | Modify the likelihood of specified tokens appearing in the completion. Accepts a json object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | No |  |
-| user | string | A unique identifier representing your end-user, which can help Azure OpenAI to monitor and detect abuse. | No |  |
-| messages | array | A list of messages comprising the conversation so far. [Example Python code](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb). | No |  |
+| temperature | number | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.<br><br>We generally recommend altering this or `top_p` but not both.<br> | No | 1 |
+| top_p | number | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br><br>We generally recommend altering this or `temperature` but not both.<br> | No | 1 |
+| stream | boolean | If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. | No | False |
+| stop | string or array | Up to four sequences where the API will stop generating further tokens.<br> | No |  |
+| max_tokens | integer | The maximum number of tokens that can be generated in the chat completion.<br><br>The total length of input tokens and generated tokens is limited by the model's context length.| No |  |
+| max_completion_tokens | integer | An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens. | No |  |
+| presence_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.<br> | No | 0 |
+| frequency_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.<br> | No | 0 |
+| logit_bias | object | Modify the likelihood of specified tokens appearing in the completion.<br><br>Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.<br> | No | None |
+| user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse.<br> | No |  |
+| messages | array | A list of messages comprising the conversation so far. | Yes |  |
 | data_sources | array |   The configuration entries for Azure OpenAI chat extensions that use them.<br>  This additional specification is only compatible with Azure OpenAI. | No |  |
-| n | integer | How many chat completion choices to generate for each input message. | No | 1 |
-| seed | integer | If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result. Determinism isn'tguaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend. | No | 0 |
-| logprobs | boolean | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. This option is currently not available on the `gpt-4-vision-preview` model. | No | False |
-| top_logprobs | integer | An integer between 0 and 5 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | No |  |
-| response_format | object | An object specifying the format that the model must output. Used to enable JSON mode. | No |  |
-| tools | array | A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. | No |  |
-| tool_choice | [chatCompletionToolChoiceOption](#chatcompletiontoolchoiceoption) | Controls which (if any) function is called by the model. `none` means the model will not call a function and instead generates a message. `auto` means the model can pick between generating a message or calling a function. Specifying a particular function via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that function. | No |  |
-| functions | array | Deprecated in favor of `tools`. A list of functions the model may generate JSON inputs for. | No |  |
-| function_call | string or object | Deprecated in favor of `tool_choice`. Controls how the model responds to function calls. "none" means the model doesn't call a function, and responds to the end-user. "auto" means the model can pick between an end-user or calling a function.  Specifying a particular function via `{"name":\ "my_function"}` forces the model to call that function. "none" is the default when no functions are present. "auto" is the default if functions are present. | No |  |
-
-
-### Properties for response_format
-
-#### Type
-
-| Name | Type | Description | Default |
-|------|------|-------------|--------|
-| type | [chatCompletionResponseFormat](#chatcompletionresponseformat) | Setting to `json_object` enables JSON mode. This guarantees that the message the model generates is valid JSON. | text |
+| logprobs | boolean | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | No | False |
+| top_logprobs | integer | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | No |  |
+| n | integer | How many chat completion choices to generate for each input message. Note that you'll be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs. | No | 1 |
+| parallel_tool_calls | [ParallelToolCalls](#paralleltoolcalls) | Whether to enable parallel function calling during tool use. | No | True |
+| response_format | [ResponseFormatText](#responseformattext) or [ResponseFormatJsonObject](#responseformatjsonobject) or [ResponseFormatJsonSchema](#responseformatjsonschema) | An object specifying the format that the model must output. Compatible with [GPT-4o](/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models), [GPT-4o mini](/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models), [GPT-4 Turbo](/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models) and all [GPT-3.5](/azure/ai-services/openai/concepts/models#gpt-35) Turbo models newer than `gpt-3.5-turbo-1106`.<br><br>Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which guarantees the model will match your supplied JSON schema.<br><br>Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.<br><br>**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.<br> | No |  |
+| seed | integer | This feature is in Beta.<br>If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.<br>Determinism isn't guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.<br> | No |  |
+| tools | array | A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.<br> | No |  |
+| tool_choice | [chatCompletionToolChoiceOption](#chatcompletiontoolchoiceoption) | Controls which (if any) tool is called by the model. `none` means the model won't call any tool and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools. Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool. `none` is the default when no tools are present. `auto` is the default if tools are present. | No |  |
+| function_call | string or [chatCompletionFunctionCallOption](#chatcompletionfunctioncalloption) | Deprecated in favor of `tool_choice`.<br><br>Controls which (if any) function is called by the model.<br>`none` means the model won't call a function and instead generates a message.<br>`auto` means the model can pick between generating a message or calling a function.<br>Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.<br><br>`none` is the default when no functions are present. `auto` is the default if functions are present.<br> | No |  |
+| functions | array | Deprecated in favor of `tools`.<br><br>A list of functions the model may generate JSON inputs for.<br> | No |  |
 
 ### Responses
 
@@ -325,7 +321,7 @@ Creates a completion for the chat message
 
 |**Content-Type**|**Type**|**Description**|
 |:---|:---|:---|
-|application/json | [createChatCompletionResponse](#createchatcompletionresponse) | |
+|application/json | [createChatCompletionResponse](#createchatcompletionresponse) or [createChatCompletionStreamResponse](#createchatcompletionstreamresponse) | |
 
 **Status Code:** default
 
@@ -339,16 +335,16 @@ Creates a completion for the chat message
 
 ### Example
 
-Creates a completion for the provided prompt, parameters and chosen model.
+Creates a completion for the provided prompt, parameters, and chosen model.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-10-21
 
 {
  "messages": [
   {
    "role": "system",
-   "content": "you're a helpful assistant that talks like a pirate"
+   "content": "you are a helpful assistant that talks like a pirate"
   },
   {
    "role": "user",
@@ -390,7 +386,7 @@ Status Code: 200
 Creates a completion based on Azure Search data and system-assigned managed identity.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-10-21
 
 {
  "messages": [
@@ -458,7 +454,7 @@ Status Code: 200
 Creates a completion based on Azure Search vector data, previous assistant message and user-assigned managed identity.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-10-21
 
 {
  "messages": [
@@ -496,7 +492,7 @@ POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-
     "in_scope": true,
     "top_n_documents": 5,
     "strictness": 3,
-    "role_information": "you're an AI assistant that helps people find information.",
+    "role_information": "You are an AI assistant that helps people find information.",
     "fields_mapping": {
      "content_fields_separator": "\\n",
      "content_fields": [
@@ -559,7 +555,7 @@ Status Code: 200
 Creates a completion for the provided Azure Cosmos DB.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=2024-10-21
 
 {
  "messages": [
@@ -636,10 +632,10 @@ Status Code: 200
 }
 ```
 
-## Transcriptions
+## Transcriptions - Create
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/audio/transcriptions?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/audio/transcriptions?api-version=2024-10-21
 ```
 
 Transcribes audio into the input language.
@@ -649,7 +645,7 @@ Transcribes audio into the input language.
 | Name | In | Required | Type | Description |
 |------|------|----------|------|-----------|
 | endpoint | path | Yes | string<br>url | Supported Azure OpenAI endpoints (protocol and hostname, for example: `https://aoairesource.openai.azure.com`. Replace "aoairesource" with your Azure OpenAI resource name). https://{your-resource-name}.openai.azure.com |
-| deployment-id | path | Yes | string | Deployment id of the whisper model. |
+| deployment-id | path | Yes | string | Deployment ID of the whisper model. |
 | api-version | query | Yes | string | API version |
 
 ### Request Header
@@ -688,7 +684,7 @@ Transcribes audio into the input language.
 Gets transcribed text and associated metadata from provided spoken audio data.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/audio/transcriptions?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/audio/transcriptions?api-version=2024-10-21
 
 ```
 
@@ -707,7 +703,7 @@ Status Code: 200
 Gets transcribed text and associated metadata from provided spoken audio data.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/audio/transcriptions?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/audio/transcriptions?api-version=2024-10-21
 
 "---multipart-boundary\nContent-Disposition: form-data; name=\"file\"; filename=\"file.wav\"\nContent-Type: application/octet-stream\n\nRIFF..audio.data.omitted\n---multipart-boundary--"
 
@@ -722,10 +718,10 @@ Status Code: 200
 }
 ```
 
-## Translations
+## Translations - Create
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/audio/translations?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/audio/translations?api-version=2024-10-21
 ```
 
 Transcribes and translates input audio into English text.
@@ -735,7 +731,7 @@ Transcribes and translates input audio into English text.
 | Name | In | Required | Type | Description |
 |------|------|----------|------|-----------|
 | endpoint | path | Yes | string<br>url | Supported Azure OpenAI endpoints (protocol and hostname, for example: `https://aoairesource.openai.azure.com`. Replace "aoairesource" with your Azure OpenAI resource name). https://{your-resource-name}.openai.azure.com |
-| deployment-id | path | Yes | string | Deployment id of the whisper model which was deployed. |
+| deployment-id | path | Yes | string | Deployment ID of the whisper model which was deployed. |
 | api-version | query | Yes | string | API version |
 
 ### Request Header
@@ -773,7 +769,7 @@ Transcribes and translates input audio into English text.
 Gets English language transcribed text and associated metadata from provided spoken audio data.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/audio/translations?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/audio/translations?api-version=2024-10-21
 
 "---multipart-boundary\nContent-Disposition: form-data; name=\"file\"; filename=\"file.wav\"\nContent-Type: application/octet-stream\n\nRIFF..audio.data.omitted\n---multipart-boundary--"
 
@@ -794,7 +790,7 @@ Status Code: 200
 Gets English language transcribed text and associated metadata from provided spoken audio data.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/audio/translations?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/audio/translations?api-version=2024-10-21
 
 "---multipart-boundary\nContent-Disposition: form-data; name=\"file\"; filename=\"file.wav\"\nContent-Type: application/octet-stream\n\nRIFF..audio.data.omitted\n---multipart-boundary--"
 
@@ -812,17 +808,17 @@ Status Code: 200
 ## Image generation
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/images/generations?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/images/generations?api-version=2024-10-21
 ```
 
-Generates a batch of images from a text caption on a given DALLE model deployment
+Generates a batch of images from a text caption on a given dall-e model deployment
 
 ### URI Parameters
 
 | Name | In | Required | Type | Description |
 |------|------|----------|------|-----------|
 | endpoint | path | Yes | string<br>url | Supported Azure OpenAI endpoints (protocol and hostname, for example: `https://aoairesource.openai.azure.com`. Replace "aoairesource" with your Azure OpenAI resource name). https://{your-resource-name}.openai.azure.com |
-| deployment-id | path | Yes | string | Deployment id of the `dall-e` model which was deployed. |
+| deployment-id | path | Yes | string | Deployment ID of the dall-e model which was deployed. |
 | api-version | query | Yes | string | API version |
 
 ### Request Header
@@ -837,7 +833,7 @@ Generates a batch of images from a text caption on a given DALLE model deploymen
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| prompt | string | A text description of the desired image(s). The maximum length is 4000 characters. | Yes |  |
+| prompt | string | A text description of the desired image(s). The maximum length is 4,000 characters. | Yes |  |
 | n | integer | The number of images to generate. | No | 1 |
 | size | [imageSize](#imagesize) | The size of the generated images. | No | 1024x1024 |
 | response_format | [imagesResponseFormat](#imagesresponseformat) | The format in which the generated images are returned. | No | url |
@@ -870,7 +866,7 @@ Generates a batch of images from a text caption on a given DALLE model deploymen
 Creates images given a prompt.
 
 ```HTTP
-POST https://{endpoint}/openai/deployments/{deployment-id}/images/generations?api-version=2024-06-01
+POST https://{endpoint}/openai/deployments/{deployment-id}/images/generations?api-version=2024-10-21
 
 {
  "prompt": "In the style of WordArt, Microsoft Clippy wearing a cowboy hat.",
@@ -958,7 +954,7 @@ Status Code: 200
 | message | string |  | No |  |
 
 
-### Error
+### error
 
 
 
@@ -1075,7 +1071,7 @@ Inner error with additional details.
 |------|------|-------------|--------|
 | URL | string |  |  |
 
-#### License
+#### license
 
 | Name | Type | Description | Default |
 |------|------|-------------|--------|
@@ -1113,7 +1109,7 @@ Information about the content filtering category (hate, sexual, violence, self_h
 
 ### contentFilterChoiceResults
 
-Information about the content filtering category (hate, sexual, violence, self_harm), if it has been detected, as well as the severity level (very_low, low, medium, high-scale that determines the intensity and risk level of harmful content) and if it has been filtered or not. Information about third-party text and profanity, if it has been detected, and if it has been filtered or not. And information about customer blocklist, if it has been filtered and its id.
+Information about the content filtering category (hate, sexual, violence, self_harm), if it has been detected, as well as the severity level (very_low, low, medium, high-scale that determines the intensity and risk level of harmful content) and if it has been filtered or not. Information about third party text and profanity, if it has been detected, and if it has been filtered or not. And information about customer blocklist, if it has been filtered and its id.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
@@ -1141,6 +1137,8 @@ Content filtering results for a single prompt in the request.
 
 Content filtering results for zero or more prompts in the request. In a streaming request, results for different prompts may arrive at different times or in different orders.
 
+No properties defined for this component.
+
 
 ### dalleContentFilterResults
 
@@ -1177,166 +1175,213 @@ Information about the content filtering category (hate, sexual, violence, self_h
 | temperature | number | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.<br>We generally recommend altering this or `top_p` but not both. | No | 1 |
 | top_p | number | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br>We generally recommend altering this or `temperature` but not both. | No | 1 |
 | stream | boolean | If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a `data: [DONE]` message. | No | False |
-| stop | string or array | Up to 4 sequences where the API will stop generating further tokens. | No |  |
-| max_tokens | integer | The maximum number of tokens allowed for the generated answer. By default, the number of tokens the model can return will be (4096 - prompt tokens). | No | 4096 |
+| stop | string or array | Up to four sequences where the API will stop generating further tokens. | No |  |
+| max_tokens | integer | The maximum number of tokens allowed for the generated answer. By default, the number of tokens the model can return will be (4096 - prompt tokens). This value is now deprecated in favor of `max_completion_tokens`, and isn't compatible with o1 series models. | No | 4096 |
+| max_completion_tokens | integer | An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens. | No |  |
 | presence_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. | No | 0 |
 | frequency_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. | No | 0 |
 | logit_bias | object | Modify the likelihood of specified tokens appearing in the completion. Accepts a json object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | No |  |
 | user | string | A unique identifier representing your end-user, which can help Azure OpenAI to monitor and detect abuse. | No |  |
 
 
-### createChatCompletionRequest
+### createCompletionRequest
 
 
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| temperature | number | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.<br>We generally recommend altering this or `top_p` but not both. | No | 1 |
-| top_p | number | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br>We generally recommend altering this or `temperature` but not both. | No | 1 |
-| stream | boolean | If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a `data: [DONE]` message. | No | False |
-| stop | string or array | Up to 4 sequences where the API will stop generating further tokens. | No |  |
-| max_tokens | integer | The maximum number of tokens allowed for the generated answer. By default, the number of tokens the model can return will be (4096 - prompt tokens). | No | 4096 |
-| presence_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. | No | 0 |
-| frequency_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. | No | 0 |
-| logit_bias | object | Modify the likelihood of specified tokens appearing in the completion. Accepts a json object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | No |  |
-| user | string | A unique identifier representing your end-user, which can help Azure OpenAI to monitor and detect abuse. | No |  |
-| messages | array | A list of messages comprising the conversation so far. [Example Python code](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb). | No |  |
-| data_sources | array |   The configuration entries for Azure OpenAI chat extensions that use them.<br>  This additional specification is only compatible with Azure OpenAI. | No |  |
-| n | integer | How many chat completion choices to generate for each input message. | No | 1 |
-| seed | integer | If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result. Determinism isn'tguaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend. | No | 0 |
-| logprobs | boolean | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. This option is currently not available on the `gpt-4-vision-preview` model. | No | False |
-| top_logprobs | integer | An integer between 0 and 5 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | No |  |
-| response_format | object | An object specifying the format that the model must output. Used to enable JSON mode. | No |  |
-| tools | array | A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. | No |  |
-| tool_choice | [chatCompletionToolChoiceOption](#chatcompletiontoolchoiceoption) | Controls which (if any) function is called by the model. `none` means the model will not call a function and instead generates a message. `auto` means the model can pick between generating a message or calling a function. Specifying a particular function via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that function. | No |  |
-| functions | array | Deprecated in favor of `tools`. A list of functions the model may generate JSON inputs for. | No |  |
-| function_call | string or object | Deprecated in favor of `tool_choice`. Controls how the model responds to function calls. "none" means the model doesn't call a function, and responds to the end-user. "auto" means the model can pick between an end-user or calling a function.  Specifying a particular function via `{"name":\ "my_function"}` forces the model to call that function. "none" is the default when no functions are present. "auto" is the default if functions are present. | No |  |
+| prompt | string or array | The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.<br><br>Note that <&#124;endoftext&#124;> is the document separator that the model sees during training, so if a prompt isn't specified the model will generate as if from the beginning of a new document.<br> | Yes |  |
+| best_of | integer | Generates `best_of` completions server-side and returns the "best" (the one with the highest log probability per token). Results can't be streamed.<br><br>When used with `n`, `best_of` controls the number of candidate completions and `n` specifies how many to return â€“ `best_of` must be greater than `n`.<br><br>**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.<br> | No | 1 |
+| echo | boolean | Echo back the prompt in addition to the completion<br> | No | False |
+| frequency_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.<br> | No | 0 |
+| logit_bias | object | Modify the likelihood of specified tokens appearing in the completion.<br><br>Accepts a JSON object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.<br><br>As an example, you can pass `{"50256": -100}` to prevent the <&#124;endoftext&#124;> token from being generated.<br> | No | None |
+| logprobs | integer | Include the log probabilities on the `logprobs` most likely output tokens, as well the chosen tokens. For example, if `logprobs` is 5, the API will return a list of the five most likely tokens. The API will always return the `logprob` of the sampled token, so there may be up to `logprobs+1` elements in the response.<br><br>The maximum value for `logprobs` is 5.<br> | No | None |
+| max_tokens | integer | The maximum number of tokens that can be generated in the completion.<br><br>The token count of your prompt plus `max_tokens` can't exceed the model's context length.| No | 16 |
+| n | integer | How many completions to generate for each prompt.<br><br>**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.<br> | No | 1 |
+| presence_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.<br> | No | 0 |
+| seed | integer | If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.<br><br>Determinism isn't guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.<br> | No |  |
+| stop | string or array | Up to four sequences where the API will stop generating further tokens. The returned text won't contain the stop sequence.<br> | No |  |
+| stream | boolean | Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message.  | No | False |
+| suffix | string | The suffix that comes after a completion of inserted text.<br><br>This parameter is only supported for `gpt-3.5-turbo-instruct`.<br> | No | None |
+| temperature | number | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.<br><br>We generally recommend altering this or `top_p` but not both.<br> | No | 1 |
+| top_p | number | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br><br>We generally recommend altering this or `temperature` but not both.<br> | No | 1 |
+| user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse.<br> | No |  |
 
 
-### Properties for response_format
+### createCompletionResponse
 
-#### Type
+Represents a completion response from the API. Note: both the streamed and nonstreamed response objects share the same shape (unlike the chat endpoint).
 
-| Name | Type | Description | Default |
-|------|------|-------------|--------|
-| type | [chatCompletionResponseFormat](#chatcompletionresponseformat) | Setting to `json_object` enables JSON mode. This guarantees that the message the model generates is valid JSON. | text |
 
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| id | string | A unique identifier for the completion. | Yes |  |
+| choices | array | The list of completion choices the model generated for the input prompt. | Yes |  |
+| created | integer | The Unix timestamp (in seconds) of when the completion was created. | Yes |  |
+| model | string | The model used for completion. | Yes |  |
+| prompt_filter_results | [promptFilterResults](#promptfilterresults) | Content filtering results for zero or more prompts in the request. In a streaming request, results for different prompts may arrive at different times or in different orders. | No |  |
+| system_fingerprint | string | This fingerprint represents the backend configuration that the model runs with.<br><br>Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.<br> | No |  |
+| object | enum | The object type, which is always "text_completion"<br>Possible values: text_completion | Yes |  |
+| usage | [completionUsage](#completionusage) | Usage statistics for the completion request. | No |  |
 
-### chatCompletionResponseFormat
 
-Setting to `json_object` enables JSON mode. This guarantees that the message the model generates is valid JSON.
+### createChatCompletionRequest
 
-**Description**: Setting to `json_object` enables JSON mode. This guarantees that the message the model generates is valid JSON.
 
-**Type**: string
 
-**Default**: text
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| temperature | number | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.<br><br>We generally recommend altering this or `top_p` but not both.<br> | No | 1 |
+| top_p | number | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br><br>We generally recommend altering this or `temperature` but not both.<br> | No | 1 |
+| stream | boolean | If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. | No | False |
+| stop | string or array | Up to four sequences where the API will stop generating further tokens.<br> | No |  |
+| max_tokens | integer | The maximum number of tokens that can be generated in the chat completion.<br><br>The total length of input tokens and generated tokens is limited by the model's context length.| No |  |
+| max_completion_tokens | integer | An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens. | No |  |
+| presence_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.<br> | No | 0 |
+| frequency_penalty | number | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.<br> | No | 0 |
+| logit_bias | object | Modify the likelihood of specified tokens appearing in the completion.<br><br>Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.<br> | No | None |
+| user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse.<br> | No |  |
+| messages | array | A list of messages comprising the conversation so far. | Yes |  |
+| data_sources | array |   The configuration entries for Azure OpenAI chat extensions that use them.<br>  This additional specification is only compatible with Azure OpenAI. | No |  |
+| logprobs | boolean | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | No | False |
+| top_logprobs | integer | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | No |  |
+| n | integer | How many chat completion choices to generate for each input message. Note that you'll be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs. | No | 1 |
+| parallel_tool_calls | [ParallelToolCalls](#paralleltoolcalls) | Whether to enable parallel function calling during tool use. | No | True |
+| response_format | [ResponseFormatText](#responseformattext) or [ResponseFormatJsonObject](#responseformatjsonobject) or [ResponseFormatJsonSchema](#responseformatjsonschema) | An object specifying the format that the model must output. Compatible with [GPT-4o](/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models), [GPT-4o mini](/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models), [GPT-4 Turbo](/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models) and all [GPT-3.5](/azure/ai-services/openai/concepts/models#gpt-35) Turbo models newer than `gpt-3.5-turbo-1106`.<br><br>Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which guarantees the model will match your supplied JSON schema.<br><br>Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.<br><br>**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.<br> | No |  |
+| seed | integer | This feature is in Beta.<br>If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.<br>Determinism isn't guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.<br> | No |  |
+| tools | array | A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.<br> | No |  |
+| tool_choice | [chatCompletionToolChoiceOption](#chatcompletiontoolchoiceoption) | Controls which (if any) tool is called by the model. `none` means the model won't call any tool and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools. Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool. `none` is the default when no tools are present. `auto` is the default if tools are present. | No |  |
+| function_call | string or [chatCompletionFunctionCallOption](#chatcompletionfunctioncalloption) | Deprecated in favor of `tool_choice`.<br><br>Controls which (if any) function is called by the model.<br>`none` means the model won't call a function and instead generates a message.<br>`auto` means the model can pick between generating a message or calling a function.<br>Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.<br><br>`none` is the default when no functions are present. `auto` is the default if functions are present.<br> | No |  |
+| functions | array | Deprecated in favor of `tools`.<br><br>A list of functions the model may generate JSON inputs for.<br> | No |  |
 
-**Enum Name**: ChatCompletionResponseFormat
 
-**Enum Values**:
+### chatCompletionFunctions
 
-| Value | Description |
-|-------|-------------|
-| text | Response format is a plain text string. |
-| json_object | Response format is a JSON object. |
 
 
-### chatCompletionFunction
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| description | string | A description of what the function does, used by the model to choose when and how to call the function. | No |  |
+| name | string | The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. | Yes |  |
+| parameters | [FunctionParameters](#functionparameters) | The parameters the functions accepts, described as a JSON Schema object. See the guide](/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. <br><br>Omitting `parameters` defines a function with an empty parameter list. | No |  |
 
 
+### chatCompletionFunctionCallOption
+
+Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.
+
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| name | string | The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. | Yes |  |
-| description | string | The description of what the function does. | No |  |
-| parameters | [chatCompletionFunctionParameters](#chatcompletionfunctionparameters) | The parameters the functions accepts, described as a JSON Schema object. See  the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. | No |  |
+| name | string | The name of the function to call. | Yes |  |
 
 
-### chatCompletionFunctionParameters
+### chatCompletionRequestMessage
 
-The parameters the functions accepts, described as a JSON Schema object. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.
 
 
-### chatCompletionRequestMessage
+This component can be one of the following:
+
+
+### chatCompletionRequestSystemMessage
 
 
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| role | [chatCompletionRequestMessageRole](#chatcompletionrequestmessagerole) | The role of the messages author. | Yes |  |
+| content | string or array | The contents of the system message. | Yes |  |
+| role | enum | The role of the messages author, in this case `system`.<br>Possible values: system | Yes |  |
+| name | string | An optional name for the participant. Provides the model information to differentiate between participants of the same role. | No |  |
 
 
-### chatCompletionRequestMessageRole
+### chatCompletionRequestUserMessage
 
-The role of the messages author.
 
-**Description**: The role of the messages author.
 
-**Type**: string
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| content | string or array | The contents of the user message.<br> | Yes |  |
+| role | enum | The role of the messages author, in this case `user`.<br>Possible values: user | Yes |  |
+| name | string | An optional name for the participant. Provides the model information to differentiate between participants of the same role. | No |  |
 
-**Default**: 
 
-**Enum Name**: ChatCompletionRequestMessageRole
+### chatCompletionRequestAssistantMessage
 
-**Enum Values**:
 
-| Value | Description |
-|-------|-------------|
-| system | The message author role is system. |
-| user | The message author role is user. |
-| assistant | The message author role is assistant. |
-| tool | The message author role is tool. |
-| function | Deprecated. The message author role is function. |
 
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| content | string or array | The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified.<br> | No |  |
+| refusal | string | The refusal message by the assistant. | No |  |
+| role | enum | The role of the messages author, in this case `assistant`.<br>Possible values: assistant | Yes |  |
+| name | string | An optional name for the participant. Provides the model information to differentiate between participants of the same role. | No |  |
+| tool_calls | [chatCompletionMessageToolCalls](#chatcompletionmessagetoolcalls) | The tool calls generated by the model, such as function calls. | No |  |
+| function_call | object | Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model. | No |  |
 
-### chatCompletionRequestMessageSystem
 
+### Properties for function_call
 
+#### arguments
 
-| Name | Type | Description | Required | Default |
-|------|------|-------------|----------|---------|
-| role | [chatCompletionRequestMessageRole](#chatcompletionrequestmessagerole) | The role of the messages author. | Yes |  |
-| content | string | The contents of the message. | No |  |
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model doesn't always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. |  |
 
+#### name
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| name | string | The name of the function to call. |  |
 
-### chatCompletionRequestMessageUser
+
+### chatCompletionRequestToolMessage
 
 
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| role | [chatCompletionRequestMessageRole](#chatcompletionrequestmessagerole) | The role of the messages author. | Yes |  |
-| content | string or array |  | No |  |
+| role | enum | The role of the messages author, in this case `tool`.<br>Possible values: tool | Yes |  |
+| content | string or array | The contents of the tool message. | Yes |  |
+| tool_call_id | string | Tool call that this message is responding to. | Yes |  |
 
 
-### chatCompletionRequestMessageContentPart
+### chatCompletionRequestFunctionMessage
 
 
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| type | [chatCompletionRequestMessageContentPartType](#chatcompletionrequestmessagecontentparttype) | The type of the content part. | Yes |  |
+| role | enum | The role of the messages author, in this case `function`.<br>Possible values: function | Yes |  |
+| content | string | The contents of the function message. | Yes |  |
+| name | string | The name of the function to call. | Yes |  |
 
 
-### chatCompletionRequestMessageContentPartType
+### chatCompletionRequestSystemMessageContentPart
 
-The type of the content part.
 
-**Description**: The type of the content part.
 
-**Type**: string
+This component can be one of the following:
 
-**Default**: 
 
-**Enum Name**: ChatCompletionRequestMessageContentPartType
+### chatCompletionRequestUserMessageContentPart
 
-**Enum Values**:
 
-| Value | Description |
-|-------|-------------|
-| text | The content part type is text. |
-| image_url | The content part type is image_url. |
+
+This component can be one of the following:
+
+
+### chatCompletionRequestAssistantMessageContentPart
+
+
+
+This component can be one of the following:
+
+
+### chatCompletionRequestToolMessageContentPart
+
+
+
+This component can be one of the following:
 
 
 ### chatCompletionRequestMessageContentPartText
@@ -1345,8 +1390,8 @@ The type of the content part.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| type | [chatCompletionRequestMessageContentPartType](#chatcompletionrequestmessagecontentparttype) | The type of the content part. | Yes |  |
-| text | string | The text content. | No |  |
+| type | enum | The type of the content part.<br>Possible values: text | Yes |  |
+| text | string | The text content. | Yes |  |
 
 
 ### chatCompletionRequestMessageContentPartImage
@@ -1355,42 +1400,33 @@ The type of the content part.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| type | [chatCompletionRequestMessageContentPartType](#chatcompletionrequestmessagecontentparttype) | The type of the content part. | Yes |  |
-| url | string | Either a URL of the image or the base64 encoded image data. | No |  |
-| detail | [imageDetailLevel](#imagedetaillevel) | Specifies the detail level of the image. | No | auto |
+| type | enum | The type of the content part.<br>Possible values: image_url | Yes |  |
+| image_url | object |  | Yes |  |
 
 
-### imageDetailLevel
-
-Specifies the detail level of the image.
-
-**Description**: Specifies the detail level of the image.
-
-**Type**: string
+### Properties for image_url
 
-**Default**: auto
+#### url
 
-**Enum Name**: ImageDetailLevel
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| url | string | Either a URL of the image or the base64 encoded image data. |  |
 
-**Enum Values**:
+#### detail
 
-| Value | Description |
-|-------|-------------|
-| auto | The image detail level is auto. |
-| low | The image detail level is low. |
-| high | The image detail level is high. |
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| detail | string | Specifies the detail level of the image. Learn more in the [Vision guide](/azure/ai-services/openai/how-to/gpt-with-vision?tabs=rest%2Csystem-assigned%2Cresource#detail-parameter-settings-in-image-processing-low-high-auto). | auto |
 
 
-### chatCompletionRequestMessageAssistant
+### chatCompletionRequestMessageContentPartRefusal
 
 
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| role | [chatCompletionRequestMessageRole](#chatcompletionrequestmessagerole) | The role of the messages author. | Yes |  |
-| content | string | The contents of the message. | No |  |
-| tool_calls | array | The tool calls generated by the model, such as function calls. | No |  |
-| context | [azureChatExtensionsMessageContext](#azurechatextensionsmessagecontext) |   A representation of the additional context information available when Azure OpenAI chat extensions are involved<br>  in the generation of a corresponding chat completions response. This context information is only populated when<br>  using an Azure OpenAI request configured to use a matching extension. | No |  |
+| type | enum | The type of the content part.<br>Possible values: refusal | Yes |  |
+| refusal | string | The refusal message generated by the model. | Yes |  |
 
 
 ### azureChatExtensionConfiguration
@@ -1410,7 +1446,7 @@ Specifies the detail level of the image.
   completions request that should use Azure OpenAI chat extensions to augment the response behavior.
   The use of this configuration is compatible only with Azure OpenAI.
 
-**Description**:   A representation of configuration data for a single Azure OpenAI chat extension. This will be used by a chat<br>  Completions request that should use Azure OpenAI chat extensions to augment the response behavior.<br>  The use of this configuration is compatible only with Azure OpenAI.
+**Description**:   A representation of configuration data for a single Azure OpenAI chat extension. This will be used by a chat completions request that should use Azure OpenAI chat extensions to augment the response behavior. The use of this configuration is compatible only with Azure OpenAI.
 
 **Type**: string
 
@@ -1481,7 +1517,7 @@ The type of Azure Search retrieval query that should be executed when using it a
 
 **Default**: 
 
-**Enum Name**: azureSearchQueryType
+**Enum Name**: AzureSearchQueryType
 
 **Enum Values**:
 
@@ -1622,7 +1658,7 @@ An abstract representation of a vectorization source for Azure OpenAI On Your Da
 Represents the available sources Azure OpenAI On Your Data can use to configure vectorization of data for use with
 vector search.
 
-**Description**: Represents the available sources Azure OpenAI On Your Data can use to configure vectorization of data for use with<br>Vector search.
+**Description**: Represents the available sources Azure OpenAI On Your Data can use to configure vectorization of data for use with<br>vector search.
 
 **Type**: string
 
@@ -1635,7 +1671,7 @@ vector search.
 | Value | Description |
 |-------|-------------|
 | endpoint | Represents vectorization performed by public service calls to an Azure OpenAI embedding model. |
-| deployment_name | Represents an Ada model deployment name to use. This model deployment must be in the same Azure OpenAI resource, but<br>The on your data feature will use this model deployment via an internal call rather than a public one, which enables vector<br>search even in private networks. |
+| deployment_name | Represents an Ada model deployment name to use. This model deployment must be in the same Azure OpenAI resource, but<br>On Your Data will use this model deployment via an internal call rather than a public one, which enables vector<br>search even in private networks. |
 
 
 ### onYourDataDeploymentNameVectorizationSource
@@ -1652,7 +1688,7 @@ on an internal embeddings model deployment name in the same Azure OpenAI resourc
 ### onYourDataEndpointVectorizationSource
 
 The details of a vectorization source, used by Azure OpenAI On Your Data when applying vector search, that is based
-on public embeddings endpoint for Azure OpenAI.
+on a public Azure OpenAI endpoint call for embeddings.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
@@ -1673,9 +1709,9 @@ on public embeddings endpoint for Azure OpenAI.
 | intent | string | The detected intent from the chat history, used to pass to the next turn to carry over the context. | No |  |
 
 
-### Citation
+### citation
 
-Citation information for a chat completions response message.
+citation information for a chat completions response message.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
@@ -1699,17 +1735,17 @@ Citation information for a chat completions response message.
 
 ### Properties for function
 
-#### Name
+#### name
 
 | Name | Type | Description | Default |
 |------|------|-------------|--------|
 | name | string | The name of the function to call. |  |
 
-#### Arguments
+#### arguments
 
 | Name | Type | Description | Default |
 |------|------|-------------|--------|
-| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model doesn't always generate valid JSON, and may fabricate parameters not defined by your function schema. Validate the arguments in your code before calling your function. |  |
+| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model doesn't always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. |  |
 
 
 ### toolCallType
@@ -1737,7 +1773,6 @@ The type of the tool call, in this case `function`.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| role | [chatCompletionRequestMessageRole](#chatcompletionrequestmessagerole) | The role of the messages author. | Yes |  |
 | tool_call_id | string | Tool call that this message is responding to. | No |  |
 | content | string | The contents of the message. | No |  |
 
@@ -1748,25 +1783,104 @@ The type of the tool call, in this case `function`.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| role | enum | The role of the messages author, in this case `function`.<br>Possible values: function | Yes |  |
+| role | enum | The role of the messages author, in this case `function`.<br>Possible values: function | No |  |
 | name | string | The contents of the message. | No |  |
 | content | string | The contents of the message. | No |  |
 
 
 ### createChatCompletionResponse
 
-
+Represents a chat completion response returned by model, based on the provided input.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
 | id | string | A unique identifier for the chat completion. | Yes |  |
-| object | [chatCompletionResponseObject](#chatcompletionresponseobject) | The object type. | Yes |  |
+| prompt_filter_results | [promptFilterResults](#promptfilterresults) | Content filtering results for zero or more prompts in the request. In a streaming request, results for different prompts may arrive at different times or in different orders. | No |  |
+| choices | array | A list of chat completion choices. Can be more than one if `n` is greater than 1. | Yes |  |
 | created | integer | The Unix timestamp (in seconds) of when the chat completion was created. | Yes |  |
 | model | string | The model used for the chat completion. | Yes |  |
+| system_fingerprint | string | This fingerprint represents the backend configuration that the model runs with.<br><br>Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.<br> | No |  |
+| object | enum | The object type, which is always `chat.completion`.<br>Possible values: chat.completion | Yes |  |
 | usage | [completionUsage](#completionusage) | Usage statistics for the completion request. | No |  |
-| system_fingerprint | string | Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism. | No |  |
-| prompt_filter_results | [promptFilterResults](#promptfilterresults) | Content filtering results for zero or more prompts in the request. In a streaming request, results for different prompts may arrive at different times or in different orders. | No |  |
-| choices | array |  | No |  |
+
+
+### createChatCompletionStreamResponse
+
+Represents a streamed chunk of a chat completion response returned by model, based on the provided input.
+
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| id | string | A unique identifier for the chat completion. Each chunk has the same ID. | Yes |  |
+| choices | array | A list of chat completion choices. Can contain more than one elements if `n` is greater than 1.<br> | Yes |  |
+| created | integer | The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same timestamp. | Yes |  |
+| model | string | The model to generate the completion. | Yes |  |
+| system_fingerprint | string | This fingerprint represents the backend configuration that the model runs with.<br>Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.<br> | No |  |
+| object | enum | The object type, which is always `chat.completion.chunk`.<br>Possible values: chat.completion.chunk | Yes |  |
+
+
+### chatCompletionStreamResponseDelta
+
+A chat completion delta generated by streamed model responses.
+
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| content | string | The contents of the chunk message. | No |  |
+| function_call | object | Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model. | No |  |
+| tool_calls | array |  | No |  |
+| role | enum | The role of the author of this message.<br>Possible values: system, user, assistant, tool | No |  |
+| refusal | string | The refusal message generated by the model. | No |  |
+
+
+### Properties for function_call
+
+#### arguments
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model doesn't always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. |  |
+
+#### name
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| name | string | The name of the function to call. |  |
+
+
+### chatCompletionMessageToolCallChunk
+
+
+
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| index | integer |  | Yes |  |
+| id | string | The ID of the tool call. | No |  |
+| type | enum | The type of the tool. Currently, only `function` is supported.<br>Possible values: function | No |  |
+| function | object |  | No |  |
+
+
+### Properties for function
+
+#### name
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| name | string | The name of the function to call. |  |
+
+#### arguments
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model doesn't always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. |  |
+
+
+### chatCompletionStreamOptions
+
+Options for streaming response. Only set this when you set `stream: true`.
+
+
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| include_usage | boolean | If set, an additional chunk will be streamed before the `data: [DONE]` message. The `usage` field on this chunk shows the token usage statistics for the entire request, and the `choices` field will always be an empty array. All other chunks will also include a `usage` field, but with a null value.<br> | No |  |
 
 
 ### chatCompletionChoiceLogProbs
@@ -1776,6 +1890,7 @@ Log probability information for the choice.
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
 | content | array | A list of message content tokens with log probability information. | Yes |  |
+| refusal | array | A list of message refusal tokens with log probability information. | No |  |
 
 
 ### chatCompletionTokenLogprob
@@ -1786,7 +1901,7 @@ Log probability information for the choice.
 |------|------|-------------|----------|---------|
 | token | string | The token. | Yes |  |
 | logprob | number | The log probability of this token. | Yes |  |
-| bytes | array | A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token. | Yes |  |
+| bytes | array | A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there's no bytes representation for the token. | Yes |  |
 | top_logprobs | array | List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned. | Yes |  |
 
 
@@ -1796,8 +1911,9 @@ A chat completion message generated by the model.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| role | [chatCompletionResponseMessageRole](#chatcompletionresponsemessagerole) | The role of the author of the response message. | No |  |
-| content | string | The contents of the message. | No |  |
+| role | [chatCompletionResponseMessageRole](#chatcompletionresponsemessagerole) | The role of the author of the response message. | Yes |  |
+| refusal | string | The refusal message generated by the model. | Yes |  |
+| content | string | The contents of the message. | Yes |  |
 | tool_calls | array | The tool calls generated by the model, such as function calls. | No |  |
 | function_call | [chatCompletionFunctionCall](#chatcompletionfunctioncall) | Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model. | No |  |
 | context | [azureChatExtensionsMessageContext](#azurechatextensionsmessagecontext) |   A representation of the additional context information available when Azure OpenAI chat extensions are involved<br>  in the generation of a corresponding chat completions response. This context information is only populated when<br>  using an Azure OpenAI request configured to use a matching extension. | No |  |
@@ -1820,7 +1936,7 @@ The role of the author of the response message.
 
 ### chatCompletionToolChoiceOption
 
-Controls which (if any) function is called by the model. `none` means the model will not call a function and instead generates a message. `auto` means the model can pick between generating a message or calling a function. Specifying a particular function via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that function.
+Controls which (if any) tool is called by the model. `none` means the model won't call any tool and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools. Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool. `none` is the default when no tools are present. `auto` is the default if tools are present.
 
 This component can be one of the following:
 
@@ -1831,121 +1947,155 @@ Specifies a tool the model should use. Use to force the model to call a specific
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| type | enum | The type of the tool. Currently, only `function` is supported.<br>Possible values: function | No |  |
-| function | object |  | No |  |
+| type | enum | The type of the tool. Currently, only `function` is supported.<br>Possible values: function | Yes |  |
+| function | object |  | Yes |  |
 
 
 ### Properties for function
 
-#### Name
+#### name
 
 | Name | Type | Description | Default |
 |------|------|-------------|--------|
 | name | string | The name of the function to call. |  |
 
 
+### ParallelToolCalls
+
+Whether to enable parallel function calling during tool use.
+
+No properties defined for this component.
+
+
+### chatCompletionMessageToolCalls
+
+The tool calls generated by the model, such as function calls.
+
+No properties defined for this component.
+
+
 ### chatCompletionFunctionCall
 
 Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
 | name | string | The name of the function to call. | Yes |  |
-| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model doesn't always generate valid JSON, and may fabricate parameters not defined by your function schema. Validate the arguments in your code before calling your function. | Yes |  |
+| arguments | string | The arguments to call the function with, as generated by the model in JSON format. Note that the model doesn't always generate valid JSON, and may generate parameters not defined by your function schema. Validate the arguments in your code before calling your function. | Yes |  |
 
 
-### chatCompletionsResponseCommon
+### completionUsage
+
+Usage statistics for the completion request.
+
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| prompt_tokens | integer | Number of tokens in the prompt. | Yes |  |
+| completion_tokens | integer | Number of tokens in the generated completion. | Yes |  |
+| total_tokens | integer | Total number of tokens used in the request (prompt + completion). | Yes |  |
+| completion_tokens_details | object | Breakdown of tokens used in a completion. | No |  |
+
+
+### Properties for completion_tokens_details
+
+#### reasoning_tokens
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| reasoning_tokens | integer | Tokens generated by the model for reasoning. |  |
+
+
+### chatCompletionTool
 
 
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| id | string | A unique identifier for the chat completion. | Yes |  |
-| object | [chatCompletionResponseObject](#chatcompletionresponseobject) | The object type. | Yes |  |
-| created | integer | The Unix timestamp (in seconds) of when the chat completion was created. | Yes |  |
-| model | string | The model used for the chat completion. | Yes |  |
-| usage | [completionUsage](#completionusage) | Usage statistics for the completion request. | No |  |
-| system_fingerprint | string | Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism. | No |  |
+| type | enum | The type of the tool. Currently, only `function` is supported.<br>Possible values: function | Yes |  |
+| function | [FunctionObject](#functionobject) |  | Yes |  |
 
 
-### chatCompletionResponseObject
+### FunctionParameters
 
-The object type.
+The parameters the functions accepts, described as a JSON Schema object. See the guide](/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. 
 
-**Description**: The object type.
+Omitting `parameters` defines a function with an empty parameter list.
 
-**Type**: string
+No properties defined for this component.
 
-**Default**: 
 
-**Enum Name**: ChatCompletionResponseObject
+### FunctionObject
 
-**Enum Values**:
 
-| Value | Description |
-|-------|-------------|
-| chat.completion | The object type is chat completion. |
 
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| description | string | A description of what the function does, used by the model to choose when and how to call the function. | No |  |
+| name | string | The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. | Yes |  |
+| parameters | [FunctionParameters](#functionparameters) | The parameters the functions accepts, described as a JSON Schema object. See the guide](/azure/ai-services/openai/how-to/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. <br><br>Omitting `parameters` defines a function with an empty parameter list. | No |  |
+| strict | boolean | Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. | No | False |
+
+
+### ResponseFormatText
 
-### completionUsage
 
-Usage statistics for the completion request.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| prompt_tokens | integer | Number of tokens in the prompt. | Yes |  |
-| completion_tokens | integer | Number of tokens in the generated completion. | Yes |  |
-| total_tokens | integer | Total number of tokens used in the request (prompt + completion). | Yes |  |
+| type | enum | The type of response format being defined: `text`<br>Possible values: text | Yes |  |
 
 
-### chatCompletionTool
+### ResponseFormatJsonObject
 
 
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| type | [chatCompletionToolType](#chatcompletiontooltype) | The type of the tool. Currently, only `function` is supported. | Yes |  |
-| function | object |  | Yes |  |
+| type | enum | The type of response format being defined: `json_object`<br>Possible values: json_object | Yes |  |
 
 
-### Properties for function
+### ResponseFormatJsonSchemaSchema
 
-#### Description
+The schema for the response format, described as a JSON Schema object.
 
-| Name | Type | Description | Default |
-|------|------|-------------|--------|
-| description | string | A description of what the function does, used by the model to choose when and how to call the function. |  |
+No properties defined for this component.
 
-#### Name
 
-| Name | Type | Description | Default |
-|------|------|-------------|--------|
-| name | string | The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. |  |
+### ResponseFormatJsonSchema
 
-#### Parameters
 
-| Name | Type | Description | Default |
-|------|------|-------------|--------|
-| parameters | [chatCompletionFunctionParameters](#chatcompletionfunctionparameters) | The parameters the functions accepts, described as a JSON Schema object. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. |  |
 
+| Name | Type | Description | Required | Default |
+|------|------|-------------|----------|---------|
+| type | enum | The type of response format being defined: `json_schema`<br>Possible values: json_schema | Yes |  |
+| json_schema | object |  | Yes |  |
 
-### chatCompletionToolType
 
-The type of the tool. Currently, only `function` is supported.
+### Properties for json_schema
 
-**Description**: The type of the tool. Currently, only `function` is supported.
+#### description
 
-**Type**: string
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| description | string | A description of what the response format is for, used by the model to determine how to respond in the format. |  |
 
-**Default**: 
+#### name
 
-**Enum Name**: ChatCompletionToolType
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| name | string | The name of the response format. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. |  |
 
-**Enum Values**:
+#### schema
 
-| Value | Description |
-|-------|-------------|
-| function | The tool type is function. |
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| schema | [ResponseFormatJsonSchemaSchema](#responseformatjsonschemaschema) | The schema for the response format, described as a JSON Schema object. |  |
+
+#### strict
+
+| Name | Type | Description | Default |
+|------|------|-------------|--------|
+| strict | boolean | Whether to enable strict schema adherence when generating the output. If set to true, the model will always follow the exact schema defined in the `schema` field. Only a subset of JSON Schema is supported when `strict` is `true`. | False |
 
 
 ### chatCompletionChoiceCommon
@@ -2032,14 +2182,14 @@ Transcription or translation segment.
 |------|------|-------------|----------|---------|
 | id | integer | Segment identifier. | No |  |
 | seek | number | Offset of the segment. | No |  |
-| start | number | The segment start offset. | No |  |
+| start | number | Segment start offset. | No |  |
 | end | number | Segment end offset. | No |  |
 | text | string | Segment text. | No |  |
 | tokens | array | Tokens of the text. | No |  |
 | temperature | number | Temperature. | No |  |
 | avg_logprob | number | Average log probability. | No |  |
 | compression_ratio | number | Compression ratio. | No |  |
-| no_speech_prob | number | Probability of 'no speech'. | No |  |
+| no_speech_prob | number | Probability of `no speech`. | No |  |
 
 
 ### imageQuality
@@ -2129,7 +2279,7 @@ The style of the generated images.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| prompt | string | A text description of the desired image(s). The maximum length is 4000 characters. | Yes |  |
+| prompt | string | A text description of the desired image(s). The maximum length is 4,000 characters. | Yes |  |
 | n | integer | The number of images to generate. | No | 1 |
 | size | [imageSize](#imagesize) | The size of the generated images. | No | 1024x1024 |
 | response_format | [imagesResponseFormat](#imagesresponseformat) | The format in which the generated images are returned. | No | url |
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "最新の推論APIドキュメントの更新"
}
```

### Explanation
この変更では、Azure OpenAIの最新の推論APIに関連するドキュメントを大幅に更新しています。主な変更点は、APIバージョンの更新、リクエストやレスポンスパラメータの追加・変更、及び全体的な内容の整理です。具体的には、いくつかの新しいパラメータが追加され（例えば `max_completion_tokens` や `seed`）、いくつかのパラメータの名称が変更されたり、機能が更新されました。これにより、ユーザーは最新のAPI仕様に基づいて、より効率的かつ効果的にAzure OpenAIを利用できるようになります。また、ドキュメント全体がより明確かつ一貫性を持つように整備されています。これに伴い、以前のバージョンとの互換性がない部分もあるため、ユーザーはAPIの使用方法の見直しを求められる可能性があります。

## articles/ai-services/openai/includes/assistants-javascript.md{#item-ad3627}

<details>
<summary>Diff</summary>
````diff
@@ -1,14 +1,14 @@
 ---
-title: 'Quickstart: Use the OpenAI Service via the JavaScript SDK'
+title: 'Quickstart: Use the Azure OpenAI Service via the JavaScript SDK'
 titleSuffix: Azure OpenAI Service
 description: Walkthrough on how to get started with Azure OpenAI and make your first completions call with the JavaScript SDK. 
 manager: nitinme
 author: mrbullwinkle
 ms.author: mbullwin
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 10/09/2024
-ms.custom: passwordless-js, devex-track-javascript
+ms.date: 10/28/2024
+ms.custom: passwordless-ts, devex-track-js
 ---
 
 <a href="/javascript/api/@azure/openai-assistants" target="_blank">Reference documentation</a> | <a href="https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai" target="_blank">Library source code</a> | <a href="https://www.npmjs.com/package/@azure/openai-assistants" target="_blank">Package (npm)</a> |
@@ -17,15 +17,14 @@ ms.custom: passwordless-js, devex-track-javascript
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
 - <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
-- [TypeScript](https://www.typescriptlang.org/download/) installed globally
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI. 
 - An Azure OpenAI resource with a [compatible model in a supported region](../concepts/models.md#assistants-preview).
 - We recommend reviewing the [Responsible AI transparency note](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=text) and other [Responsible AI resources](/legal/cognitive-services/openai/overview?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext) to familiarize yourself with the capabilities and limitations of the Azure OpenAI Service.
 - An Azure OpenAI resource with the `gpt-4 (1106-preview)` model deployed was used testing this example. 
 
-## Passwordless authentication is recommended
+## Microsoft Entra ID authentication is recommended
 
-For passwordless authentication, you need to 
+For _keyless_ authentication, you need to 
 
 1. Use the `@azure/identity` package.
 1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal under **Access control (IAM)** > **Add role assignment**.
@@ -67,32 +66,19 @@ For passwordless authentication, you need to
 
 ## Retrieve resource information
 
-> [!CAUTION]
-> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
-
-#### [TypeScript keyless (Recommended)](#tab/typescript-keyless)
-
-[!INCLUDE [assistants-keyless-environment-variables](assistants-env-var-without-key.md)]
-
-
-#### [TypeScript with API key](#tab/typescript-key)
-
-[!INCLUDE [assistants-key-environment-variables](assistants-env-var-key.md)]
-
-
-#### [JavaScript keyless](#tab/javascript-keyless)
+#### [Microsoft Entra ID](#tab/javascript-keyless)
 
 [!INCLUDE [assistants-keyless-environment-variables](assistants-env-var-without-key.md)]
 
 
-#### [JavaScript with API key](#tab/javascript-key)
+#### [API key](#tab/javascript-key)
 
 [!INCLUDE [assistants-key-environment-variables](assistants-env-var-key.md)]
 
 ---
 
 > [!CAUTION]
-> Don't set `AZURE_OPENAI_API_KEY` when using keyless authentication.
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 
 ## Create an assistant
@@ -109,272 +95,19 @@ In our code we're going to specify the following values:
 ### Tools
 
 An individual assistant can access up to 128 tools including `code interpreter`, and any custom tools you create via [functions](../how-to/assistant-functions.md).
-
-#### [TypeScript keyless (Recommended)](#tab/typescript-keyless)
-
-1. Create the `index.ts` file with the following code:
-
-    ```typescript
-    import { AzureOpenAI } from "openai";
-    import {
-      Assistant,
-      AssistantCreateParams,
-      AssistantTool,
-    } from "openai/resources/beta/assistants";
-    import { Message, MessagesPage } from "openai/resources/beta/threads/messages";
-    import { Run } from "openai/resources/beta/threads/runs/runs";
-    import { Thread } from "openai/resources/beta/threads/threads";
-    
-    // Add `Cognitive Services User` to identity for Azure OpenAI resource
-    import {
-      DefaultAzureCredential,
-      getBearerTokenProvider,
-    } from "@azure/identity";
-    
-    // Get environment variables
-    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT as string;
-    const azureOpenAIDeployment = process.env
-      .AZURE_OPENAI_DEPLOYMENT_NAME as string;
-    const openAIVersion = process.env.OPENAI_API_VERSION as string;
-    
-    // Check env variables
-    if (!azureOpenAIEndpoint || !azureOpenAIDeployment || !openAIVersion) {
-      throw new Error(
-        "Please ensure to set AZURE_OPENAI_DEPLOYMENT_NAME and AZURE_OPENAI_ENDPOINT in your environment variables."
-      );
-    }
     
-    // Get Azure SDK client
-    const getClient = (): AzureOpenAI => {
-      const credential = new DefaultAzureCredential();
-      const scope = "https://cognitiveservices.azure.com/.default";
-      const azureADTokenProvider = getBearerTokenProvider(credential, scope);
-      const assistantsClient = new AzureOpenAI({
-        endpoint: azureOpenAIEndpoint,
-        apiVersion: openAIVersion,
-        azureADTokenProvider,
-      });
-      return assistantsClient;
-    };
-    
-    const assistantsClient = getClient();
-    
-    const options: AssistantCreateParams = {
-      model: azureOpenAIDeployment, // Deployment name seen in Azure AI Studio
-      name: "Math Tutor",
-      instructions:
-        "You are a personal math tutor. Write and run JavaScript code to answer math questions.",
-      tools: [{ type: "code_interpreter" } as AssistantTool],
-    };
-    const role = "user";
-    const message = "I need to solve the equation `3x + 11 = 14`. Can you help me?";
-    
-    // Create an assistant
-    const assistantResponse: Assistant =
-      await assistantsClient.beta.assistants.create(options);
-    console.log(`Assistant created: ${JSON.stringify(assistantResponse)}`);
-    
-    // Create a thread
-    const assistantThread: Thread = await assistantsClient.beta.threads.create({});
-    console.log(`Thread created: ${JSON.stringify(assistantThread)}`);
-    
-    // Add a user question to the thread
-    const threadResponse: Message =
-      await assistantsClient.beta.threads.messages.create(assistantThread.id, {
-        role,
-        content: message,
-      });
-    console.log(`Message created:  ${JSON.stringify(threadResponse)}`);
-    
-    // Run the thread and poll it until it is in a terminal state
-    const runResponse: Run = await assistantsClient.beta.threads.runs.createAndPoll(
-      assistantThread.id,
-      {
-        assistant_id: assistantResponse.id,
-      },
-      { pollIntervalMs: 500 }
-    );
-    console.log(`Run created:  ${JSON.stringify(runResponse)}`);
-    
-    // Get the messages
-    const runMessages: MessagesPage =
-      await assistantsClient.beta.threads.messages.list(assistantThread.id);
-    for await (const runMessageDatum of runMessages) {
-      for (const item of runMessageDatum.content) {
-        // types are: "image_file" or "text"
-        if (item.type === "text") {
-          console.log(`Message content: ${JSON.stringify(item.text?.value)}`);
-        }
-      }
-    }
-    ```
-    
-
+## Create a new JavaScript application
 
-1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
-
-    ```json
-    {
-        "compilerOptions": {
-          "module": "NodeNext",
-          "target": "ES2022", // Supports top-level await
-          "moduleResolution": "NodeNext",
-          "skipLibCheck": true, // Avoid type errors from node_modules
-          "strict": true // Enable strict type-checking options
-        },
-        "include": ["*.ts"]
-    }
-    ```
-
-1. Transpile from TypeScript to JavaScript.
-
-    ```shell
-    tsc
-    ```
-    
-1. Sign in to Azure with the following command:
-
-    ```shell
-    az login
-    ```
-
-1. Run the code with the following command:
-
-    ```shell
-    node index.js
-    ```
-
-#### [TypeScript with API key](#tab/typescript-key)
-
-1. Create the `index.ts` file with the following code:
-
-    ```typescript
-    import { AzureOpenAI } from "openai";
-    import {
-      Assistant,
-      AssistantCreateParams,
-      AssistantTool,
-    } from "openai/resources/beta/assistants";
-    import { Message, MessagesPage } from "openai/resources/beta/threads/messages";
-    import { Run } from "openai/resources/beta/threads/runs/runs";
-    import { Thread } from "openai/resources/beta/threads/threads";
-    
-    // Get environment variables
-    const azureOpenAIKey = process.env.AZURE_OPENAI_KEY as string;
-    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT as string;
-    const azureOpenAIDeployment = process.env
-      .AZURE_OPENAI_DEPLOYMENT_NAME as string;
-    const openAIVersion = process.env.OPENAI_API_VERSION as string;
-    
-    // Check env variables
-    if (!azureOpenAIKey || !azureOpenAIEndpoint || !azureOpenAIDeployment || !openAIVersion) {
-      throw new Error(
-        "Please set AZURE_OPENAI_KEY and AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_DEPLOYMENT_NAME in your environment variables."
-      );
-    }
-    
-    // Get Azure SDK client
-    const getClient = (): AzureOpenAI => {
-      const assistantsClient = new AzureOpenAI({
-        endpoint: azureOpenAIEndpoint,
-        apiVersion: openAIVersion,
-        apiKey: azureOpenAIKey,
-      });
-      return assistantsClient;
-    };
-    
-    const assistantsClient = getClient();
-    
-    const options: AssistantCreateParams = {
-      model: azureOpenAIDeployment, // Deployment name seen in Azure AI Studio
-      name: "Math Tutor",
-      instructions:
-        "You are a personal math tutor. Write and run JavaScript code to answer math questions.",
-      tools: [{ type: "code_interpreter" } as AssistantTool],
-    };
-    const role = "user";
-    const message = "I need to solve the equation `3x + 11 = 14`. Can you help me?";
-    
-    // Create an assistant
-    const assistantResponse: Assistant =
-      await assistantsClient.beta.assistants.create(options);
-    console.log(`Assistant created: ${JSON.stringify(assistantResponse)}`);
-    
-    // Create a thread
-    const assistantThread: Thread = await assistantsClient.beta.threads.create({});
-    console.log(`Thread created: ${JSON.stringify(assistantThread)}`);
-    
-    // Add a user question to the thread
-    const threadResponse: Message =
-      await assistantsClient.beta.threads.messages.create(assistantThread.id, {
-        role,
-        content: message,
-      });
-    console.log(`Message created:  ${JSON.stringify(threadResponse)}`);
-    
-    // Run the thread and poll it until it is in a terminal state
-    const runResponse: Run = await assistantsClient.beta.threads.runs.createAndPoll(
-      assistantThread.id,
-      {
-        assistant_id: assistantResponse.id,
-      },
-      { pollIntervalMs: 500 }
-    );
-    console.log(`Run created:  ${JSON.stringify(runResponse)}`);
-    
-    // Get the messages
-    const runMessages: MessagesPage =
-      await assistantsClient.beta.threads.messages.list(assistantThread.id);
-    for await (const runMessageDatum of runMessages) {
-      for (const item of runMessageDatum.content) {
-        // types are: "image_file" or "text"
-        if (item.type === "text") {
-          console.log(`Message content: ${JSON.stringify(item.text?.value)}`);
-        }
-      }
-    }
-    ```
-    
-
-1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
-
-    ```json
-    {
-        "compilerOptions": {
-          "module": "NodeNext",
-          "target": "ES2022", // Supports top-level await
-          "moduleResolution": "NodeNext",
-          "skipLibCheck": true, // Avoid type errors from node_modules
-          "strict": true // Enable strict type-checking options
-        },
-        "include": ["*.ts"]
-    }
-    ```
-
-1. Transpile from TypeScript to JavaScript.
-
-    ```shell
-    tsc
-    ```
-
-1. Run the code with the following command:
-
-    ```shell
-    node index.js
-    ```
-
-#### [JavaScript keyless](#tab/javascript-keyless)
+#### [Microsoft Entra ID](#tab/javascript-keyless)
 
 1. Create the `index.js` file with the following code:
 
-    ```nodejs
-    import { AzureOpenAI } from "openai";
-    
-    // Add `Cognitive Services User` to identity for Azure OpenAI resource
-    import {
+    ```javascript
+    const { AzureOpenAI } = require("openai");
+    const {
       DefaultAzureCredential,
       getBearerTokenProvider,
-    } from "@azure/identity";
+    } = require("@azure/identity");
     
     // Get environment variables
     const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT;
@@ -393,6 +126,7 @@ An individual assistant can access up to 128 tools including `code interpreter`,
       const credential = new DefaultAzureCredential();
       const scope = "https://cognitiveservices.azure.com/.default";
       const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+
       const assistantsClient = new AzureOpenAI({
         endpoint: azureOpenAIEndpoint,
         apiVersion: azureOpenAIVersion,
@@ -469,12 +203,14 @@ An individual assistant can access up to 128 tools including `code interpreter`,
     node index.js
     ```
 
-#### [JavaScript with API key](#tab/javascript-key)
+
+
+#### [API key](#tab/javascript-key)
 
 1. Create the `index.js` file with the following code:
 
-    ```nodejs
-    import { AzureOpenAI } from "openai";
+    ```javascript
+    const { AzureOpenAI } = require("openai");
     
     // Get environment variables
     const azureOpenAIKey = process.env.AZURE_OPENAI_KEY;
@@ -561,7 +297,7 @@ An individual assistant can access up to 128 tools including `code interpreter`,
     node index.js
     ```
 
-```
+---
 
 ## Output
 
@@ -578,8 +314,6 @@ Message content: "I need to solve the equation `3x + 11 = 14`. Can you help me?"
 
 It's important to remember that while the code interpreter gives the model the capability to respond to more complex queries by converting the questions into code and running that code iteratively in JavaScript until it reaches a solution, you still need to validate the response to confirm that the model correctly translated your question into a valid representation in code.
 
----
-
 ## Clean up resources
 
 If you want to clean up and remove an Azure OpenAI resource, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript用のAzure OpenAIサービスのクイックスタート改訂"
}
```

### Explanation
このコードの変更では、Azure OpenAIサービスのJavaScript SDKに関するドキュメントが更新されています。主な更新項目として、タイトルが「Azure OpenAI Service via the JavaScript SDK」に変更され、日付やカスタムタグが修正されています。また、パスワードレス認証の説明が「Microsoft Entra ID認証」に改訂され、関連する認証手順が簡略化されました。具体的なコード例や手順が整理され、一部の冗長な部分が削除されています。この更新により、ドキュメントがより明確になり、Azure OpenAIの利用が簡単に理解できるようになっています。

## articles/ai-services/openai/includes/assistants-typescript.md{#item-3195a9}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,391 @@
+---
+title: 'Quickstart: Use the Azure OpenAI Service via the JavaScript SDK'
+titleSuffix: Azure OpenAI Service
+description: Walkthrough on how to get started with Azure OpenAI and make your first completions call with the JavaScript SDK. 
+manager: nitinme
+author: mrbullwinkle
+ms.author: mbullwin
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 10/09/2024
+ms.custom: passwordless-js, devex-track-typescript
+---
+
+<a href="/javascript/api/@azure/openai-assistants" target="_blank">Reference documentation</a> | <a href="https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai" target="_blank">Library source code</a> | <a href="https://www.npmjs.com/package/@azure/openai-assistants" target="_blank">Package (npm)</a> |
+
+## Prerequisites
+
+- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
+- <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
+- [TypeScript](https://www.typescriptlang.org/download/) installed globally
+- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI. 
+- An Azure OpenAI resource with a [compatible model in a supported region](../concepts/models.md#assistants-preview).
+- We recommend reviewing the [Responsible AI transparency note](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=text) and other [Responsible AI resources](/legal/cognitive-services/openai/overview?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext) to familiarize yourself with the capabilities and limitations of the Azure OpenAI Service.
+- An Azure OpenAI resource with the `gpt-4 (1106-preview)` model deployed was used testing this example. 
+
+## Passwordless authentication is recommended
+
+For passwordless authentication, you need to 
+
+1. Use the `@azure/identity` package.
+1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal under **Access control (IAM)** > **Add role assignment**.
+1. Sign in with the Azure CLI such as `az login`.
+
+## Set up
+
+1. Create a new folder `assistants-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
+
+    ```shell
+    mkdir assistants-quickstart && code assistants-quickstart
+    ```
+    
+
+1. Create the `package.json` with the following command:
+
+    ```shell
+    npm init -y
+    ```
+
+1. Update the `package.json` to ECMAScript with the following command: 
+
+    ```shell
+    npm pkg set type=module
+    ```
+    
+
+1. Install the OpenAI Assistants client library for JavaScript with:
+
+    ```console
+    npm install openai
+    ```
+
+1. For the **recommended** passwordless authentication:
+
+    ```console
+    npm install @azure/identity
+    ```
+
+## Retrieve resource information
+
+
+#### [Microsoft Entra ID](#tab/typescript-keyless)
+
+[!INCLUDE [assistants-keyless-environment-variables](assistants-env-var-without-key.md)]
+
+
+#### [API key](#tab/typescript-key)
+
+[!INCLUDE [assistants-key-environment-variables](assistants-env-var-key.md)]
+
+---
+
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+
+
+## Create an assistant
+
+In our code we're going to specify the following values:
+
+| **Name** | **Description** |
+|:---|:---|
+| **Assistant name** | Your deployment name that is associated with a specific model. |
+| **Instructions** | Instructions are similar to system messages this is where you give the model guidance about how it should behave and any context it should reference when generating a response. You can describe the assistant's personality, tell it what it should and shouldn't answer, and tell it how to format responses. You can also provide examples of the steps it should take when answering responses. |
+| **Model** | This is the deployment name. |
+| **Code interpreter** | Code interpreter provides access to a sandboxed Python environment that can be used to allow the model to test and execute code. |
+
+### Tools
+
+An individual assistant can access up to 128 tools including `code interpreter`, and any custom tools you create via [functions](../how-to/assistant-functions.md).
+
+    
+## Create a new TypeScript application
+
+#### [Microsoft Entra ID](#tab/typescript-keyless)
+
+1. Create the `index.ts` file with the following code:
+
+    ```typescript
+    import { AzureOpenAI } from "openai";
+    import {
+      Assistant,
+      AssistantCreateParams,
+      AssistantTool,
+    } from "openai/resources/beta/assistants";
+    import { Message, MessagesPage } from "openai/resources/beta/threads/messages";
+    import { Run } from "openai/resources/beta/threads/runs/runs";
+    import { Thread } from "openai/resources/beta/threads/threads";
+    
+    // Add `Cognitive Services User` to identity for Azure OpenAI resource
+    import {
+      DefaultAzureCredential,
+      getBearerTokenProvider,
+    } from "@azure/identity";
+    
+    // Get environment variables
+    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT as string;
+    const azureOpenAIDeployment = process.env
+      .AZURE_OPENAI_DEPLOYMENT_NAME as string;
+    const openAIVersion = process.env.OPENAI_API_VERSION as string;
+    
+    // Check env variables
+    if (!azureOpenAIEndpoint || !azureOpenAIDeployment || !openAIVersion) {
+      throw new Error(
+        "Please ensure to set AZURE_OPENAI_DEPLOYMENT_NAME and AZURE_OPENAI_ENDPOINT in your environment variables."
+      );
+    }
+    
+    // Get Azure SDK client
+    const getClient = (): AzureOpenAI => {
+      const credential = new DefaultAzureCredential();
+      const scope = "https://cognitiveservices.azure.com/.default";
+      const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+      const assistantsClient = new AzureOpenAI({
+        endpoint: azureOpenAIEndpoint,
+        apiVersion: openAIVersion,
+        azureADTokenProvider,
+      });
+      return assistantsClient;
+    };
+    
+    const assistantsClient = getClient();
+    
+    const options: AssistantCreateParams = {
+      model: azureOpenAIDeployment, // Deployment name seen in Azure AI Studio
+      name: "Math Tutor",
+      instructions:
+        "You are a personal math tutor. Write and run JavaScript code to answer math questions.",
+      tools: [{ type: "code_interpreter" } as AssistantTool],
+    };
+    const role = "user";
+    const message = "I need to solve the equation `3x + 11 = 14`. Can you help me?";
+    
+    // Create an assistant
+    const assistantResponse: Assistant =
+      await assistantsClient.beta.assistants.create(options);
+    console.log(`Assistant created: ${JSON.stringify(assistantResponse)}`);
+    
+    // Create a thread
+    const assistantThread: Thread = await assistantsClient.beta.threads.create({});
+    console.log(`Thread created: ${JSON.stringify(assistantThread)}`);
+    
+    // Add a user question to the thread
+    const threadResponse: Message =
+      await assistantsClient.beta.threads.messages.create(assistantThread.id, {
+        role,
+        content: message,
+      });
+    console.log(`Message created:  ${JSON.stringify(threadResponse)}`);
+    
+    // Run the thread and poll it until it is in a terminal state
+    const runResponse: Run = await assistantsClient.beta.threads.runs.createAndPoll(
+      assistantThread.id,
+      {
+        assistant_id: assistantResponse.id,
+      },
+      { pollIntervalMs: 500 }
+    );
+    console.log(`Run created:  ${JSON.stringify(runResponse)}`);
+    
+    // Get the messages
+    const runMessages: MessagesPage =
+      await assistantsClient.beta.threads.messages.list(assistantThread.id);
+    for await (const runMessageDatum of runMessages) {
+      for (const item of runMessageDatum.content) {
+        // types are: "image_file" or "text"
+        if (item.type === "text") {
+          console.log(`Message content: ${JSON.stringify(item.text?.value)}`);
+        }
+      }
+    }
+    ```
+    
+
+
+1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
+
+    ```json
+    {
+        "compilerOptions": {
+          "module": "NodeNext",
+          "target": "ES2022", // Supports top-level await
+          "moduleResolution": "NodeNext",
+          "skipLibCheck": true, // Avoid type errors from node_modules
+          "strict": true // Enable strict type-checking options
+        },
+        "include": ["*.ts"]
+    }
+    ```
+
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
+    tsc
+    ```
+    
+1. Sign in to Azure with the following command:
+
+    ```shell
+    az login
+    ```
+
+1. Run the code with the following command:
+
+    ```shell
+    node index.js
+    ```
+
+
+
+#### [API key](#tab/typescript-key)
+
+1. Create the `index.ts` file with the following code:
+
+    ```typescript
+    import { AzureOpenAI } from "openai";
+    import {
+      Assistant,
+      AssistantCreateParams,
+      AssistantTool,
+    } from "openai/resources/beta/assistants";
+    import { Message, MessagesPage } from "openai/resources/beta/threads/messages";
+    import { Run } from "openai/resources/beta/threads/runs/runs";
+    import { Thread } from "openai/resources/beta/threads/threads";
+    
+    // Get environment variables
+    const azureOpenAIKey = process.env.AZURE_OPENAI_KEY as string;
+    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT as string;
+    const azureOpenAIDeployment = process.env
+      .AZURE_OPENAI_DEPLOYMENT_NAME as string;
+    const openAIVersion = process.env.OPENAI_API_VERSION as string;
+    
+    // Check env variables
+    if (!azureOpenAIKey || !azureOpenAIEndpoint || !azureOpenAIDeployment || !openAIVersion) {
+      throw new Error(
+        "Please set AZURE_OPENAI_KEY and AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_DEPLOYMENT_NAME in your environment variables."
+      );
+    }
+    
+    // Get Azure SDK client
+    const getClient = (): AzureOpenAI => {
+      const assistantsClient = new AzureOpenAI({
+        endpoint: azureOpenAIEndpoint,
+        apiVersion: openAIVersion,
+        apiKey: azureOpenAIKey,
+      });
+      return assistantsClient;
+    };
+    
+    const assistantsClient = getClient();
+    
+    const options: AssistantCreateParams = {
+      model: azureOpenAIDeployment, // Deployment name seen in Azure AI Studio
+      name: "Math Tutor",
+      instructions:
+        "You are a personal math tutor. Write and run JavaScript code to answer math questions.",
+      tools: [{ type: "code_interpreter" } as AssistantTool],
+    };
+    const role = "user";
+    const message = "I need to solve the equation `3x + 11 = 14`. Can you help me?";
+    
+    // Create an assistant
+    const assistantResponse: Assistant =
+      await assistantsClient.beta.assistants.create(options);
+    console.log(`Assistant created: ${JSON.stringify(assistantResponse)}`);
+    
+    // Create a thread
+    const assistantThread: Thread = await assistantsClient.beta.threads.create({});
+    console.log(`Thread created: ${JSON.stringify(assistantThread)}`);
+    
+    // Add a user question to the thread
+    const threadResponse: Message =
+      await assistantsClient.beta.threads.messages.create(assistantThread.id, {
+        role,
+        content: message,
+      });
+    console.log(`Message created:  ${JSON.stringify(threadResponse)}`);
+    
+    // Run the thread and poll it until it is in a terminal state
+    const runResponse: Run = await assistantsClient.beta.threads.runs.createAndPoll(
+      assistantThread.id,
+      {
+        assistant_id: assistantResponse.id,
+      },
+      { pollIntervalMs: 500 }
+    );
+    console.log(`Run created:  ${JSON.stringify(runResponse)}`);
+    
+    // Get the messages
+    const runMessages: MessagesPage =
+      await assistantsClient.beta.threads.messages.list(assistantThread.id);
+    for await (const runMessageDatum of runMessages) {
+      for (const item of runMessageDatum.content) {
+        // types are: "image_file" or "text"
+        if (item.type === "text") {
+          console.log(`Message content: ${JSON.stringify(item.text?.value)}`);
+        }
+      }
+    }
+    ```
+    
+
+1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
+
+    ```json
+    {
+        "compilerOptions": {
+          "module": "NodeNext",
+          "target": "ES2022", // Supports top-level await
+          "moduleResolution": "NodeNext",
+          "skipLibCheck": true, // Avoid type errors from node_modules
+          "strict": true // Enable strict type-checking options
+        },
+        "include": ["*.ts"]
+    }
+    ```
+
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
+    tsc
+    ```
+
+1. Run the code with the following command:
+
+    ```shell
+    node index.js
+    ```
+
+---
+
+## Output
+
+```console
+Assistant created: {"id":"asst_zXaZ5usTjdD0JGcNViJM2M6N","createdAt":"2024-04-08T19:26:38.000Z","name":"Math Tutor","description":null,"model":"daisy","instructions":"You are a personal math tutor. Write and run JavaScript code to answer math questions.","tools":[{"type":"code_interpreter"}],"fileIds":[],"metadata":{}}
+Thread created: {"id":"thread_KJuyrB7hynun4rvxWdfKLIqy","createdAt":"2024-04-08T19:26:38.000Z","metadata":{}}
+Message created:  {"id":"msg_o0VkXnQj3juOXXRCnlZ686ff","createdAt":"2024-04-08T19:26:38.000Z","threadId":"thread_KJuyrB7hynun4rvxWdfKLIqy","role":"user","content":[{"type":"text","text":{"value":"I need to solve the equation `3x + 11 = 14`. Can you help me?","annotations":[]},"imageFile":{}}],"assistantId":null,"runId":null,"fileIds":[],"metadata":{}}
+Created run
+Run created:  {"id":"run_P8CvlouB8V9ZWxYiiVdL0FND","object":"thread.run","status":"queued","model":"daisy","instructions":"You are a personal math tutor. Write and run JavaScript code to answer math questions.","tools":[{"type":"code_interpreter"}],"metadata":{},"usage":null,"assistantId":"asst_zXaZ5usTjdD0JGcNViJM2M6N","threadId":"thread_KJuyrB7hynun4rvxWdfKLIqy","fileIds":[],"createdAt":"2024-04-08T19:26:39.000Z","expiresAt":"2024-04-08T19:36:39.000Z","startedAt":null,"completedAt":null,"cancelledAt":null,"failedAt":null}
+Message content: "The solution to the equation \\(3x + 11 = 14\\) is \\(x = 1\\)."
+Message content: "Yes, of course! To solve the equation \\( 3x + 11 = 14 \\), we can follow these steps:\n\n1. Subtract 11 from both sides of the equation to isolate the term with x.\n2. Then, divide by 3 to find the value of x.\n\nLet me calculate that for you."
+Message content: "I need to solve the equation `3x + 11 = 14`. Can you help me?"
+```
+
+It's important to remember that while the code interpreter gives the model the capability to respond to more complex queries by converting the questions into code and running that code iteratively in JavaScript until it reaches a solution, you still need to validate the response to confirm that the model correctly translated your question into a valid representation in code.
+
+## Clean up resources
+
+If you want to clean up and remove an Azure OpenAI resource, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
+
+- [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
+- [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
+
+## Sample code
+
+* [Quickstart sample code](https://github.com/Azure-Samples/azure-typescript-e2e-apps/tree/main/quickstarts/azure-openai-assistants)
+
+## See also
+
+* Learn more about how to use Assistants with our [How-to guide on Assistants](../how-to/assistant.md).
+* [Azure OpenAI Assistants API samples](https://github.com/Azure-Samples/azureai-samples/tree/main/scenarios/Assistants)
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIサービスのTypeScript用クイックスタートガイドの追加"
}
```

### Explanation
この変更では、Azure OpenAIサービスを利用するためのTypeScript向けの新しいクイックスタートガイドが追加されました。このドキュメントでは、Azure OpenAIサービスの使用方法を学ぶための手順が詳述されています。内容には、必要な前提条件、パスワードレス認証の推奨、TypeScriptアプリケーションの設定、資源情報の取得、アシスタントの作成、及び関連するコマンドやコード例が含まれています。具体的には、Azure OpenAIのクライアントライブラリを使用したアシスタントの生成やユーザーとのインタラクトの方法が示されており、ユーザーはこれを基に独自のアプリケーションを簡単に開発できるようになります。このドキュメントは391行のコードと説明を含んでおり、Azure OpenAIの利用をスムーズに開始できるための重要なリソースとなっています。

## articles/ai-services/openai/includes/chatgpt-javascript.md{#item-cbf09f}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-openai
 ms.topic: include
 author: mrbullwinkle
 ms.author: mbullwin
-ms.date: 05/21/2024
+ms.date: 10/22
 ---
 
 [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
@@ -18,26 +18,14 @@ ms.date: 05/21/2024
 
 ## Prerequisites
 
-## [**TypeScript**](#tab/typescript)
-
-- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
-- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
-- [TypeScript](https://www.typescriptlang.org/download/)
-- An Azure OpenAI Service resource with a `gpt-35-turbo` or `gpt-4` series models deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
-
-> [!div class="nextstepaction"]
-> [I ran into an issue with the prerequisites.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=JAVASCRIPT&Pillar=AOAI&Product=Chatgpt&Page=quickstart&Section=Prerequisites)
-
-## [**JavaScript**](#tab/javascript)
-
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI Service resource with either a `gpt-35-turbo` or `gpt-4` series models deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 
 > [!div class="nextstepaction"]
 > [I ran into an issue with the prerequisites.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=JAVASCRIPT&Pillar=AOAI&Product=Chatgpt&Page=quickstart&Section=Prerequisites)
 
----
 
 ## Set up
 
@@ -54,7 +42,7 @@ In a console window (such as cmd, PowerShell, or Bash), create a new directory f
 Install the required packages for JavaScript with npm from within the context of your new directory:
 
 ```console
-npm install openai dotenv @azure/identity
+npm install openai @azure/identity
 ```
 
 Your app's _package.json_ file will be updated with the dependencies.
@@ -66,94 +54,69 @@ Your app's _package.json_ file will be updated with the dependencies.
 
 Open a command prompt where you want the new project, and create a new file named ChatCompletion.js. Copy the following code into the ChatCompletion.js file.
 
-## [**TypeScript**](#tab/typescript)
 
-```typescript
-import "dotenv/config";
-import { AzureOpenAI } from "openai";
-import type {
-  ChatCompletion,
-  ChatCompletionCreateParamsNonStreaming,
-} from "openai/resources/index";
+## [Microsoft Entra ID](#tab/javascript-keyless)
+
+```javascript
+const { AzureOpenAI } = require("openai");
+const { 
+  DefaultAzureCredential, 
+  getBearerTokenProvider 
+} = require("@azure/identity");
 
 // You will need to set these environment variables or edit the following values
 const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+const apiVersion = "2024-05-01-preview";
+const deployment = "gpt-4o"; //This must match your deployment name.
 
-// Required Azure OpenAI deployment name and API version
-const apiVersion = "2024-08-01-preview";
-const deploymentName = "gpt-4o-mini"; //This must match your deployment name.
 
-function getClient(): AzureOpenAI {
-  return new AzureOpenAI({
-    endpoint,
-    apiKey,
-    apiVersion,
-    deployment: deploymentName,
-  });
-}
+// keyless authentication    
+const credential = new DefaultAzureCredential();
+const scope = "https://cognitiveservices.azure.com/.default";
+const azureADTokenProvider = getBearerTokenProvider(credential, scope);
 
-function createMessages(): ChatCompletionCreateParamsNonStreaming {
-  return {
+async function main() {
+
+  const client = new AzureOpenAI({ endpoint, apiKey, azureADTokenProvider, deployment });
+  const result = await client.chat.completions.create({
     messages: [
-      { role: "system", content: "You are a helpful assistant." },
-      {
-        role: "user",
-        content: "Does Azure OpenAI support customer managed keys?",
-      },
-      {
-        role: "assistant",
-        content: "Yes, customer managed keys are supported by Azure OpenAI?",
-      },
-      { role: "user", content: "Do other Azure AI services support this too?" },
+    { role: "system", content: "You are a helpful assistant." },
+    { role: "user", content: "Does Azure OpenAI support customer managed keys?" },
+    { role: "assistant", content: "Yes, customer managed keys are supported by Azure OpenAI?" },
+    { role: "user", content: "Do other Azure AI services support this too?" },
     ],
     model: "",
-  };
-}
-async function printChoices(completion: ChatCompletion): Promise<void> {
-  for (const choice of completion.choices) {
+  });
+
+  for (const choice of result.choices) {
     console.log(choice.message);
   }
 }
-export async function main() {
-  const client = getClient();
-  const messages = createMessages();
-  const result = await client.chat.completions.create(messages);
-  await printChoices(result);
-}
 
 main().catch((err) => {
   console.error("The sample encountered an error:", err);
 });
-```
-
-Build the script with the following command:
 
-```cmd
-tsc
+module.exports = { main };
 ```
 
 Run the script with the following command:
 
 ```cmd
-node.exe Completion.js
+node.exe ChatCompletion.js
 ```
 
-## [**JavaScript**](#tab/javascript)
+
+## [API key](#tab/javascript-key)
 
 ```javascript
 const { AzureOpenAI } = require("openai");
 
-// Load the .env file if it exists
-const dotenv = require("dotenv");
-dotenv.config();
-
 // You will need to set these environment variables or edit the following values
 const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
 const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
 const apiVersion = "2024-05-01-preview";
 const deployment = "gpt-4o"; //This must match your deployment name.
-require("dotenv/config");
 
 async function main() {
 
@@ -198,122 +161,6 @@ node.exe ChatCompletion.js
 }
 ```
 
-## Microsoft Entra ID
-
-> [!IMPORTANT]
-> In the previous example we are demonstrating key-based authentication. Once you have tested with key-based authentication successfully, we recommend using the more secure [Microsoft Entra ID](/entra/fundamentals/whatis) for authentication which is demonstrated in the next code sample. Getting started with [Microsoft Entra ID] will require some additional [prerequisites](https://www.npmjs.com/package/@azure/identity).
-
-## [**TypeScript**](#tab/typescript)
-
-```typescript
-import {
-  DefaultAzureCredential,
-  getBearerTokenProvider,
-} from "@azure/identity";
-import "dotenv/config";
-import { AzureOpenAI } from "openai";
-import type {
-  ChatCompletion,
-  ChatCompletionCreateParamsNonStreaming,
-} from "openai/resources/index";
-
-// You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-
-// Required Azure OpenAI deployment name and API version
-const apiVersion = "2024-08-01-preview";
-const deploymentName = "gpt-4o-mini"; //This must match your deployment name.
-
-function getClient(): AzureOpenAI {
-  const scope = "https://cognitiveservices.azure.com/.default";
-  const azureADTokenProvider = getBearerTokenProvider(
-    new DefaultAzureCredential(),
-    scope
-  );
-  return new AzureOpenAI({
-    endpoint,
-    azureADTokenProvider,
-    deployment: deploymentName,
-    apiVersion,
-  });
-}
-
-function createMessages(): ChatCompletionCreateParamsNonStreaming {
-  return {
-    messages: [
-      { role: "system", content: "You are a helpful assistant." },
-      {
-        role: "user",
-        content: "Does Azure OpenAI support customer managed keys?",
-      },
-      {
-        role: "assistant",
-        content: "Yes, customer managed keys are supported by Azure OpenAI?",
-      },
-      { role: "user", content: "Do other Azure AI services support this too?" },
-    ],
-    model: "",
-  };
-}
-async function printChoices(completion: ChatCompletion): Promise<void> {
-  for (const choice of completion.choices) {
-    console.log(choice.message);
-  }
-}
-export async function main() {
-  const client = getClient();
-  const messages = createMessages();
-  const result = await client.chat.completions.create(messages);
-  await printChoices(result);
-}
-
-main().catch((err) => {
-  console.error("The sample encountered an error:", err);
-});
-```
-
-
-## [**JavaScript**](#tab/javascript)
-
-```javascript
-const { AzureOpenAI } = require("openai");
-const { DefaultAzureCredential, getBearerTokenProvider } = require("@azure/identity");
-
-// Set AZURE_OPENAI_ENDPOINT to the endpoint of your
-// OpenAI resource. You can find this in the Azure portal.
-// Load the .env file if it exists
-require("dotenv/config");
-
-async function main() {
-  console.log("== Chat Completions Sample ==");
-
-  const scope = "https://cognitiveservices.azure.com/.default";
-  const azureADTokenProvider = getBearerTokenProvider(new DefaultAzureCredential(), scope);
-  const deployment = "gpt-35-turbo";
-  const apiVersion = "2024-04-01-preview";
-  const client = new AzureOpenAI({ azureADTokenProvider, deployment, apiVersion });
-  const result = await client.chat.completions.create({
-    messages: [
-    { role: "system", content: "You are a helpful assistant." },
-    { role: "user", content: "Does Azure OpenAI support customer managed keys?" },
-    { role: "assistant", content: "Yes, customer managed keys are supported by Azure OpenAI?" },
-    { role: "user", content: "Do other Azure AI services support this too?" },
-    ],
-    model: "",
-  });
-
-  for (const choice of result.choices) {
-    console.log(choice.message);
-  }
-}
-
-main().catch((err) => {
-  console.error("The sample encountered an error:", err);
-});
-
-module.exports = { main };
-```
-
 ---
 
 > [!NOTE]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ChatGPT用JavaScriptガイドの改訂"
}
```

### Explanation
このコードの変更では、Azure OpenAIのChatGPTを使用するためのJavaScriptガイドが更新されています。更新内容には、ページの日付が2024年10月22日に変更され、前提条件の項目が簡素化され、Azure CLIを用いたパスワードレス認証の設定方法が追加されました。また、TypeScript関連の説明が削除され、JavaScriptでの設定に焦点が当てられています。具体的には、必要なパッケージのインストール手順が明確化され、新しいコードサンプルが提供されています。これにより、ユーザーはより使いやすく、最新の開発環境に沿った情報を得ることができるようになっています。この更新によって、全体の内容が217行にわたり整理され、受けやすくなっています。

## articles/ai-services/openai/includes/chatgpt-typescript.md{#item-6d2f1f}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,241 @@
+---
+title: 'Quickstart: Use Azure OpenAI Service with the JavaScript SDK'
+titleSuffix: Azure OpenAI
+description: Walkthrough on how to get started with Azure OpenAI and make your first chat completions call with the JavaScript SDK. 
+#services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+author: mrbullwinkle
+ms.author: mbullwin
+ms.date: 10/22
+---
+
+[Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
+
+> [!NOTE]
+> This article has been updated to use the [latest OpenAI npm package](https://www.npmjs.com/package/openai) which now fully supports Azure OpenAI. If you are looking for code examples for the legacy Azure OpenAI JavaScript SDK they are currently still [available in this repo](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples/v2-beta/javascript).
+
+## Prerequisites
+
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [TypeScript](https://www.typescriptlang.org/download/)
+- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
+- An Azure OpenAI Service resource with a `gpt-35-turbo` or `gpt-4` series models deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
+
+> [!div class="nextstepaction"]
+> [I ran into an issue with the prerequisites.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=JAVASCRIPT&Pillar=AOAI&Product=Chatgpt&Page=quickstart&Section=Prerequisites)
+
+
+## Set up
+
+[!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
+
+[!INCLUDE [environment-variables](environment-variables.md)]
+
+## Create a Node application
+
+In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. 
+
+## Install the client library
+
+Install the required packages for JavaScript with npm from within the context of your new directory:
+
+```console
+npm install openai @azure/identity
+```
+
+Your app's _package.json_ file will be updated with the dependencies.
+
+> [!div class="nextstepaction"]
+> [I ran into an issue with the setup.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=JAVASCRIPT&Pillar=AOAI&Product=Chatgpt&Page=quickstart&Section=Set-up-the-environment)
+
+## Create a sample application
+
+Open a command prompt where you want the new project, and create a new file named ChatCompletion.ts. Copy the following code into the ChatCompletion.ts file.
+
+## [Microsoft Entra ID](#tab/typescript-keyless)
+
+```typescript
+import { AzureOpenAI } from "openai";
+import { 
+  DefaultAzureCredential, 
+  getBearerTokenProvider 
+} from "@azure/identity";
+import type {
+  ChatCompletion,
+  ChatCompletionCreateParamsNonStreaming,
+} from "openai/resources/index";
+
+// You will need to set these environment variables or edit the following values
+const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+
+// Required Azure OpenAI deployment name and API version
+const apiVersion = "2024-08-01-preview";
+const deploymentName = "gpt-4o-mini"; //This must match your deployment name.
+
+// keyless authentication    
+const credential = new DefaultAzureCredential();
+const scope = "https://cognitiveservices.azure.com/.default";
+const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+
+function getClient(): AzureOpenAI {
+  return new AzureOpenAI({
+    endpoint,
+    azureADTokenProvider,
+    apiVersion,
+    deployment: deploymentName,
+  });
+}
+
+function createMessages(): ChatCompletionCreateParamsNonStreaming {
+  return {
+    messages: [
+      { role: "system", content: "You are a helpful assistant." },
+      {
+        role: "user",
+        content: "Does Azure OpenAI support customer managed keys?",
+      },
+      {
+        role: "assistant",
+        content: "Yes, customer managed keys are supported by Azure OpenAI?",
+      },
+      { role: "user", content: "Do other Azure AI services support this too?" },
+    ],
+    model: "",
+  };
+}
+async function printChoices(completion: ChatCompletion): Promise<void> {
+  for (const choice of completion.choices) {
+    console.log(choice.message);
+  }
+}
+export async function main() {
+  const client = getClient();
+  const messages = createMessages();
+  const result = await client.chat.completions.create(messages);
+  await printChoices(result);
+}
+
+main().catch((err) => {
+  console.error("The sample encountered an error:", err);
+});
+```
+
+Build the script with the following command:
+
+```cmd
+tsc
+```
+
+Run the script with the following command:
+
+```cmd
+node.exe ChatCompletion.js
+```
+
+## [API Key](#tab/typescript-key)
+
+```typescript
+import { AzureOpenAI } from "openai";
+import type {
+  ChatCompletion,
+  ChatCompletionCreateParamsNonStreaming,
+} from "openai/resources/index";
+
+// You will need to set these environment variables or edit the following values
+const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+
+// Required Azure OpenAI deployment name and API version
+const apiVersion = "2024-08-01-preview";
+const deploymentName = "gpt-4o-mini"; //This must match your deployment name.
+
+function getClient(): AzureOpenAI {
+  return new AzureOpenAI({
+    endpoint,
+    apiKey,
+    apiVersion,
+    deployment: deploymentName,
+  });
+}
+
+function createMessages(): ChatCompletionCreateParamsNonStreaming {
+  return {
+    messages: [
+      { role: "system", content: "You are a helpful assistant." },
+      {
+        role: "user",
+        content: "Does Azure OpenAI support customer managed keys?",
+      },
+      {
+        role: "assistant",
+        content: "Yes, customer managed keys are supported by Azure OpenAI?",
+      },
+      { role: "user", content: "Do other Azure AI services support this too?" },
+    ],
+    model: "",
+  };
+}
+async function printChoices(completion: ChatCompletion): Promise<void> {
+  for (const choice of completion.choices) {
+    console.log(choice.message);
+  }
+}
+export async function main() {
+  const client = getClient();
+  const messages = createMessages();
+  const result = await client.chat.completions.create(messages);
+  await printChoices(result);
+}
+
+main().catch((err) => {
+  console.error("The sample encountered an error:", err);
+});
+```
+
+Build the script with the following command:
+
+```cmd
+tsc
+```
+
+Run the script with the following command:
+
+```cmd
+node.exe ChatCompletion.js
+```
+
+---
+
+## Output
+
+```output
+== Chat Completions Sample ==
+{
+  content: 'Yes, several other Azure AI services also support customer managed keys for enhanced security and control over encryption keys.',
+  role: 'assistant'
+}
+```
+
+---
+
+> [!NOTE]
+> If your receive the error: *Error occurred: OpenAIError: The `apiKey` and `azureADTokenProvider` arguments are mutually exclusive; only one can be passed at a time.* You may need to remove a pre-existing environment variable for the API key from your system. Even though the Microsoft Entra ID code sample is not explicitly referencing the API key environment variable, if one is present on the system executing this sample, this error will still be generated.
+
+> [!div class="nextstepaction"]
+> [I ran into an issue when running the code sample.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=JAVASCRIPT&Pillar=AOAI&Product=Chatgpt&Page=quickstart&Section=Create-application)
+
+## Clean up resources
+
+If you want to clean up and remove an Azure OpenAI resource, you can delete the resource. Before deleting the resource, you must first delete any deployed models.
+
+- [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
+- [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
+
+## Next steps
+
+* [Azure OpenAI Overview](../overview.md)
+* For more examples, check out the [Azure OpenAI Samples GitHub repository](https://aka.ms/AOAICodeSamples)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIサービスを使用したTypeScriptのクイックスタートガイドの追加"
}
```

### Explanation
この変更では、Azure OpenAIサービスをTypeScriptで利用するための新しいクイックスタートガイドが追加されました。このガイドは、Azure OpenAIとJavaScript SDKを活用して、最初のチャット完了呼び出しを実行する手順を詳しく説明しています。内容としては、Azureサブスクリプションの作成、Node.jsやTypeScriptのインストール、Azure CLIによるパスワードレス認証の設定、依存関係となる必要なパッケージのインストール方法が含まれています。また、サンプルアプリケーションの作成方法や、APIキーとMicrosoft Entra IDを用いた認証方法についての具体的なコード例も提供されています。一連のプロセスは、ユーザーが容易にAzure OpenAIサービスを活用できるように設計されており、合計241行のコードと説明が含まれています。さらに、リソースのクリーンアップ手順や次のステップに関する情報も含まれ、より包括的なサポートが提供されています。

## articles/ai-services/openai/includes/javascript.md{#item-f4828f}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-openai
 ms.topic: include
 author: mrbullwinkle
 ms.author: mbullwin
-ms.date: 05/20/2024
+ms.date: 10/22/2024
 ---
 
 [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
@@ -18,26 +18,15 @@ ms.date: 05/20/2024
 
 ## Prerequisites
 
-## [**TypeScript**](#tab/typescript)
 
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
-- [TypeScript](https://www.typescriptlang.org/download/)
+- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI Service resource with the `gpt-35-turbo-instruct` model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 
 > [!div class="nextstepaction"]
 > [I ran into an issue with the prerequisites.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=JAVASCRIPT&Pillar=AOAI&&Product=gpt&Page=quickstart&Section=Prerequisites)
 
-## [**JavaScript**](#tab/javascript)
-
-- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
-- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
-- An Azure OpenAI Service resource with the `gpt-35-turbo-instruct` model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
-
-> [!div class="nextstepaction"]
-> [I ran into an issue with the prerequisites.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=JAVASCRIPT&Pillar=AOAI&&Product=gpt&Page=quickstart&Section=Prerequisites)
-
----
 
 ## Set up
 
@@ -52,7 +41,7 @@ In a console window (such as cmd, PowerShell, or Bash), create a new directory f
 Install the required packages for JavaScript with npm from within the context of your new directory:
 
 ```console
-npm install openai dotenv @azure/identity
+npm install openai @azure/identity
 ```
 
 Your app's _package.json_ file will be updated with the dependencies.
@@ -64,66 +53,45 @@ Your app's _package.json_ file will be updated with the dependencies.
 
 Open a command prompt where you created the new project, and create a new file named Completion.js. Copy the following code into the Completion.js file.
 
-## [**TypeScript**](#tab/typescript)
 
-```typescript
-import "dotenv/config";
-import { AzureOpenAI } from "openai";
-import { type Completion } from "openai/resources/index";
+## [Microsoft Entra ID](#tab/javascript-keyless)
+
+```javascript
+const { AzureOpenAI } = require("openai");
+const { 
+  DefaultAzureCredential, 
+  getBearerTokenProvider 
+} = require("@azure/identity");
 
 // You will need to set these environment variables or edit the following values
 const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+const apiVersion = "2024-04-01-preview";
+const deployment = "gpt-35-turbo-instruct"; //The deployment name for your completions API model. The instruct model is the only new model that supports the legacy API.
 
-// Required Azure OpenAI deployment name and API version
-const apiVersion = "2024-08-01-preview";
-const deploymentName = "gpt-35-turbo-instruct";
+// keyless authentication    
+const credential = new DefaultAzureCredential();
+const scope = "https://cognitiveservices.azure.com/.default";
+const azureADTokenProvider = getBearerTokenProvider(credential, scope);
 
-// Chat prompt and max tokens
 const prompt = ["When was Microsoft founded?"];
-const maxTokens = 128;
-
-function getClient(): AzureOpenAI {
-  return new AzureOpenAI({
-    endpoint,
-    apiKey,
-    apiVersion,
-    deployment: deploymentName,
-  });
-}
-async function getCompletion(
-  client: AzureOpenAI,
-  prompt: string[],
-  max_tokens: number
-): Promise<Completion> {
-  return client.completions.create({
-    prompt,
-    model: "",
-    max_tokens,
-  });
-}
-async function printChoices(completion: Completion): Promise<void> {
-  for (const choice of completion.choices) {
-    console.log(choice.text);
-  }
-}
-export async function main() {
+
+async function main() {
   console.log("== Get completions Sample ==");
 
-  const client = getClient();
-  const completion = await getCompletion(client, prompt, maxTokens);
-  await printChoices(completion);
+  const client = new AzureOpenAI({ endpoint, azureADTokenProvider, apiVersion, deployment });  
+
+  const result = await client.completions.create({ prompt, model: deployment, max_tokens: 128 });
+
+  for (const choice of result.choices) {
+    console.log(choice.text);
+  }
 }
 
 main().catch((err) => {
   console.error("Error occurred:", err);
 });
-```
-
-Build the script with the following command:
 
-```cmd
-tsc
+module.exports = { main };
 ```
 
 Run the script with the following command:
@@ -132,15 +100,12 @@ Run the script with the following command:
 node.exe Completion.js
 ```
 
-## [**JavaScript**](#tab/javascript)
+
+## [API key](#tab/javascript-key)
 
 ```javascript
 const { AzureOpenAI } = require("openai");
 
-// Load the .env file if it exists
-const dotenv = require("dotenv");
-dotenv.config();
-
 // You will need to set these environment variables or edit the following values
 const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
 const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
@@ -184,126 +149,6 @@ node.exe Completion.js
 Microsoft was founded on April 4, 1975.
 ```
 
-## Microsoft Entra ID
-
-> [!IMPORTANT]
-> In the previous example we are demonstrating key-based authentication. Once you have tested with key-based authentication successfully, we recommend using the more secure [Microsoft Entra ID](/entra/fundamentals/whatis) for authentication which is demonstrated in the next code sample. Getting started with [Microsoft Entra ID] will require some additional [prerequisites](https://www.npmjs.com/package/@azure/identity).
-
-## [**TypeScript**](#tab/typescript)
-
-```typescript
-import {
-  DefaultAzureCredential,
-  getBearerTokenProvider,
-} from "@azure/identity";
-import "dotenv/config";
-import { AzureOpenAI } from "openai";
-import { type Completion } from "openai/resources/index";
-
-// You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-
-// Required Azure OpenAI deployment name and API version
-const apiVersion = "2024-08-01-preview";
-const deploymentName = "gpt-35-turbo-instruct";
-
-// Chat prompt and max tokens
-const prompt = ["When was Microsoft founded?"];
-const maxTokens = 128;
-
-function getClient(): AzureOpenAI {
-  const scope = "https://cognitiveservices.azure.com/.default";
-  const azureADTokenProvider = getBearerTokenProvider(
-    new DefaultAzureCredential(),
-    scope
-  );
-  return new AzureOpenAI({
-    endpoint,
-    azureADTokenProvider,
-    deployment: deploymentName,
-    apiVersion,
-  });
-}
-async function getCompletion(
-  client: AzureOpenAI,
-  prompt: string[],
-  max_tokens: number
-): Promise<Completion> {
-  return client.completions.create({
-    prompt,
-    model: "",
-    max_tokens,
-  });
-}
-async function printChoices(completion: Completion): Promise<void> {
-  for (const choice of completion.choices) {
-    console.log(choice.text);
-  }
-}
-export async function main() {
-  console.log("== Get completions Sample ==");
-
-  const client = getClient();
-  const completion = await getCompletion(client, prompt, maxTokens);
-  await printChoices(completion);
-}
-
-main().catch((err) => {
-  console.error("Error occurred:", err);
-});
-
-```
-
-Build the script with the following command:
-
-```cmd
-tsc
-```
-
-Run the script with the following command:
-
-```cmd
-node.exe Completion.js
-```
-
-
-## [**JavaScript**](#tab/javascript)
-
-```javascript
-const { AzureOpenAI } = require("openai");
-const { DefaultAzureCredential, getBearerTokenProvider } = require("@azure/identity");
-
-// Set AZURE_OPENAI_ENDPOINT to the endpoint of your
-// OpenAI resource. You can find this in the Azure portal.
-// Load the .env file if it exists
-require("dotenv/config");
-
-const prompt = ["When was Microsoft founded?"];
-
-async function main() {
-  console.log("== Get completions Sample ==");
-
-  const scope = "https://cognitiveservices.azure.com/.default";
-  const azureADTokenProvider = getBearerTokenProvider(new DefaultAzureCredential(), scope);
-  const deployment = "gpt-35-turbo-instruct";
-  const apiVersion = "2024-04-01-preview";
-  const client = new AzureOpenAI({ azureADTokenProvider, deployment, apiVersion });
-  const result = await client.completions.create({ prompt, model: deployment, max_tokens: 128 });
-
-  for (const choice of result.choices) {
-    console.log(choice.text);
-  }
-}
-
-main().catch((err) => {
-  console.error("Error occurred:", err);
-});
-
-module.exports = { main };
-```
-
----
-
 > [!NOTE]
 > If your receive the error: *Error occurred: OpenAIError: The `apiKey` and `azureADTokenProvider` arguments are mutually exclusive; only one can be passed at a time.* You may need to remove a pre-existing environment variable for the API key from your system. Even though the Microsoft Entra ID code sample is not explicitly referencing the API key environment variable, if one is present on the system executing this sample, this error will still be generated.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKに関するガイドの修正"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスに関するJavaScript SDKのガイドの更新を含んでいます。主な変更点は、最新の日付が2024年10月22日に更新され、前提条件のセクションが簡略化されたことです。特に、TypeScriptに関する情報が削除され、JavaScriptでの実装に集中しています。

新たに追加された「Microsoft Entra ID」を使用した認証方法と、依存関係となるパッケージのインストール手順が明確に示されています。また、`client.completions.create`メソッドの使用法も更新され、コード例が整理されています。これにより、ユーザーはパスワードレス認証を利用した新しい方法でスムーズにAPIを呼び出せるようになります。

この変更によって、文書全体において184行が削除され、29行が追加され、合計213行の変更が行われ、全体の内容がより明確で効率的なものとなっています。

## articles/ai-services/openai/includes/model-matrix/datazone-standard.md{#item-188333}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,24 @@
+---
+title: Datazone standard model availability
+titleSuffix: Azure OpenAI Service
+description: Regional availability for Global Batch models
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 10/31/2024
+---
+
+| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|
+| eastus             | ✅                       | ✅                       | ✅                            |
+| eastus2            | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                       | ✅                       | ✅                            |
+| northcentralus     | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "グローバルバッチモデルの地域Availabilityに関するDatazone標準モデルの追加"
}
```

### Explanation
この変更では、Azure OpenAIサービスにおけるグローバルバッチモデルの地域ごとの利用可能性を示す新しい「Datazone standard model availability」ドキュメントが追加されました。この文書では、特定の地域でのモデルの可用性について詳細な情報が提供されています。具体的には、`gpt-4o`と`gpt-4o-mini`の各モデルについて、異なるデプロイ日（2024年5月13日、2024年8月6日、2024年7月18日）における地域ごとの利用状況が示された表が含まれています。

表には、各地域でのモデルが利用可能かどうかがチェックマーク（✅）で示されており、これによりユーザーがどの地域でどのモデルを使用できるかを一目で確認できるようになっています。合計で24行の新しいコンテンツが追加され、この情報はAzure OpenAIサービスを利用する開発者にとって重要なリソースとなります。

## articles/ai-services/openai/includes/model-matrix/global-batch.md{#item-929e6a}

<details>
<summary>Diff</summary>
````diff
@@ -5,11 +5,16 @@ description: Regional availability for Global Batch models
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 10/24/2024
+ms.date: 10/31/2024
 ---
 
 | **Region**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
 |:-----------------|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
+| canadaeast       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | eastus           | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| eastus2          | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| northcentralus   | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southcentralus   | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | swedencentral    | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westus           | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
\ No newline at end of file
+| westus           | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westus3          | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルバッチモデルの地域可用性に関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるグローバルバッチモデルの地域可用性に関する「global-batch.md」ドキュメントの更新を含んでいます。主な変更点は、モデルの対応地域が増え、日付の更新が行われたことです。

具体的には、`ms.date`プロパティが2024年10月24日から2024年10月31日に変更され、いくつかの新しい地域（`canadaeast`、`eastus2`、`northcentralus`、`southcentralus`、`westus3`）が表に追加されました。これにより、各モデル（`gpt-4o`、`gpt-4o-mini`、`gpt-4`、`gpt-35-turbo`など）の地域ごとの利用可能性をより詳細に示すことができます。この更新により、7行が追加され、2行が削除され、文書全体の整合性が向上しました。

## articles/ai-services/openai/includes/model-matrix/provisioned-models.md{#item-8ee639}

<details>
<summary>Diff</summary>
````diff
@@ -17,10 +17,10 @@ ms.date: 10/24/2024
 | canadaeast         | ✅                       | -                      | ✅                            | ✅                | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      |
 | eastus             | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | eastus2            | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| francecentral      | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | -                      | ✅                       |
+| francecentral      | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | -                      | ✅                       |
 | germanywestcentral | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | -                      |
-| japaneast          | ✅                       | -                      | ✅                            | -               | ✅                        | ✅                        | ✅                            | -                   | -                      | ✅                       |
-| koreacentral       | ✅                       | -                      | ✅                            | ✅                | -                       | -                       | ✅                            | ✅                    | ✅                       | -                      |
+| japaneast          | ✅                       | ✅                       | ✅                            | -               | ✅                        | ✅                        | ✅                            | -                   | -                      | ✅                       |
+| koreacentral       | ✅                       | ✅                       | ✅                            | ✅                | -                       | -                       | ✅                            | ✅                    | ✅                       | -                      |
 | northcentralus     | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | norwayeast         | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                           | ✅                    | -                      | -                      |
 | polandcentral      | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
@@ -30,6 +30,7 @@ ms.date: 10/24/2024
 | swedencentral      | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | switzerlandnorth   | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | switzerlandwest    | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
+| uaenorth           | ✅                       | -                      | -                           | -               | ✅                        | -                       | -                           | -                   | ✅                       | ✅                       |
 | uksouth            | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | westus             | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| westus3            | ✅                       | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
\ No newline at end of file
+| westus3            | ✅                       | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングモデルの地域可用性に関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「provisioned-models.md」ドキュメントにおけるプロビジョニングモデルの地域可用性情報の更新を含んでいます。主な内容として、表形式で示されたモデルの可用性に関するデータが修正され、一部地域の可用性が追加されたり、修正されたりしました。

具体的には、`francecentral`、`japaneast`、および`koreacentral`の地域のモデル可用性が更新され、特定のモデルに対してチェック（✅）が追加されたり削除されたりしました。また、新たに`uaenorth`地域が追加され、その地域におけるモデルの可用性も反映されています。これにより、5行が追加され、4行が削除され、ドキュメント全体の可読性と正確性が向上しました。これらの変更は、ユーザーが選択可能なモデルの可用性をより正確に把握できるようにするためのものです。

## articles/ai-services/openai/includes/model-matrix/standard-audio.md{#item-1d8db7}

<details>
<summary>Diff</summary>
````diff
@@ -17,4 +17,5 @@ ms.date: 10/25/2024
 | southindia       | -            | -               | ✅                 |
 | swedencentral    | ✅             | ✅                | ✅                 |
 | switzerlandnorth | -            | -               | ✅                 |
+| uaenorth         | -            | -               | ✅                 |
 | westeurope       | -            | -               | ✅                 |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準音声モデルの地域可用性に関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「standard-audio.md」ドキュメントにおける標準音声モデルの地域可用性情報の更新を反映しています。具体的には、表に新たに`uaenorth`地域が追加され、その地域における標準音声モデルの可用性が示されています。この変更によって、ユーザーは利用可能なモデルの地域的な選択肢をより正確に理解できるようになります。

更新内容は、1行の追加のみであり、他に削除された行はありません。この修正により、標準音声モデルのドキュメントの整合性と包括性が向上しました。全体として、このマイナーアップデートは、ユーザーに対して標準音声モデルの利用可能地域に関する具体的な情報を提供することを目的としています。

## articles/ai-services/openai/includes/model-matrix/standard-chat-completions.md{#item-aae3f1}

<details>
<summary>Diff</summary>
````diff
@@ -26,4 +26,5 @@ ms.date: 10/25/2024
 | uksouth          | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | ✅                        | -                         | -                           | -                   | ✅                       | ✅                       | ✅                       | ✅                       | ✅                           |
 | westeurope       | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          |
 | westus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | ✅                          | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          |
-| westus3          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          |
\ No newline at end of file
+| westus3          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          |
+
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準チャット完了モデルの情報更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「standard-chat-completions.md」ドキュメントに関連します。主に、標準チャット完了モデルの利用可能性に関する表において、情報が更新されました。具体的には、`westus3`地域に関する行が修正され、同地域の標準チャット完了モデルに適用される情報の一部が明確に更新されました。

更新内容としては、2行が追加され、1行が削除されており、全体で3つの変更が行われました。この修正により、ドキュメントはより正確で最新の情報を提供できるようになり、ユーザーが標準チャット完了モデルの利用可能性を理解するための参考情報を強化しています。全体的には、このマイナーアップデートは、モデルの利用に関する選択肢をより明確に示すことを目的としています。

## articles/ai-services/openai/includes/model-matrix/standard-embeddings.md{#item-656427}

<details>
<summary>Diff</summary>
````diff
@@ -19,11 +19,13 @@ ms.date: 03/25/2024
 | japaneast        | ✅                              | ✅                              | -                             | ✅                              |
 | northcentralus   | -                             | -                             | -                             | ✅                              |
 | norwayeast       | -                             | ✅                              | -                             | ✅                              |
+| polandcentral    | -                             | ✅                              | -                             | -                             |
 | southafricanorth | -                             | -                             | -                             | ✅                              |
 | southcentralus   | -                             | -                             | ✅                              | ✅                              |
 | southindia       | -                             | ✅                              | -                             | ✅                              |
 | swedencentral    | -                             | ✅                              | -                             | ✅                              |
-| switzerlandnorth | -                             | -                             | -                             | ✅                              |
+| switzerlandnorth | -                             | ✅                              | -                             | ✅                              |
+| uaenorth         | -                             | -                             | -                             | ✅                              |
 | uksouth          | -                             | ✅                              | -                             | ✅                              |
 | westeurope       | -                             | -                             | -                             | ✅                              |
 | westus           | -                             | -                             | -                             | ✅                              |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準埋め込みモデルの情報更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「standard-embeddings.md」ドキュメントに関するもので、標準埋め込みモデルの地域可用性に関する情報が更新されました。具体的には、表に新たに`polandcentral`および`uaenorth`地域が追加され、各地域の埋め込みモデルの利用状況が明確化されています。

追加された情報は、モデルの可用性を示すもので、地域ごとに異なるサポート状況を反映しています。また、`switzerlandnorth`地域の情報も若干修正されています。この修正により、ユーザーは各地域での標準埋め込みモデルに関する最新の可用性情報を得ることができ、より具体的な選択肢を持つことができるようになります。

全体として、このマイナーアップデートは、ドキュメントの正確性を高め、ユーザーにとって有用な情報を提供することを目的としています。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,8 @@ ms.date: 10/25/2024
 | spaincentral       | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
 | swedencentral      | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                            |
 | switzerlandnorth   | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| uaenorth           | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
 | uksouth            | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
 | westeurope         | -                          | -                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
 | westus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| westus3            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
\ No newline at end of file
+| westus3            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準グローバルモデルの情報更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「standard-global.md」ドキュメントに関するもので、標準グローバルモデルに関する地域の可用性情報が更新されました。具体的には、新たに`uaenorth`地域が追加され、この地域でのモデルの利用状況が示された表が更新されています。

更新の中で、2行が追加され、1行が削除されており、全体で3つの変更が行われました。特に、`westus3`地域の情報は、変更前後で一貫して表示されています。この修正により、ユーザーはより正確で最新の利用可能性情報を参照することができ、特に`uaenorth`地域におけるモデル利用の可用性を理解する手助けとなります。

全体として、このマイナーアップデートは、利用可能なオプションを明確にすることで、ユーザー体験を向上させることを目的としています。

## articles/ai-services/openai/includes/model-matrix/standard-models.md{#item-af04c4}

<details>
<summary>Diff</summary>
````diff
@@ -19,11 +19,13 @@ ms.date: 10/25/2024
 | japaneast        | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | ✅                          | -                           | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
 | northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
 | norwayeast       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| polandcentral    | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
 | southafricanorth | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
 | southcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | -                      | -                      | ✅                       | -                          | -                               | -                             | -                             | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
 | southindia       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | ✅                       | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | swedencentral    | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           | ✅                                | -                             | ✅                              | -                             | ✅                              | -                 | ✅                  | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
-| switzerlandnorth | -                          | -                       | -                      | -                      | -                           | ✅                | -                       | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| switzerlandnorth | -                          | -                       | -                      | -                      | -                           | ✅                | -                       | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| uaenorth         | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | uksouth          | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | ✅                        | -                         | -                           | -                   | ✅                       | ✅                       | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
 | westeurope       | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | westus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | ✅                          | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準モデルの地域情報更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「standard-models.md」ドキュメントに関するもので、標準モデルの地域可用性情報が更新されています。この更新では、3行が追加され、1行が削除される形で全体で4つの変更が行われました。主に、新たに`polandcentral`および`uaenorth`地域が表に追加され、各地域でのモデルの利用状況に関する詳細が明らかにされています。

具体的には、これによりユーザーは、各地域でどのモデルが利用可能であるかをより明確に把握できるようになります。また、既存の`switzerlandnorth`地域についても、モデルの利用可能性情報が若干修正されています。

整体として、このマイナーアップデートは、利用可能な標準モデルに関する情報を充実させ、より多くの地域における即応性を向上させることを目指しています。これにより、ユーザーは自らのニーズに応じたモデルを選択する際に、より具体的な情報に基づいた判断を下すことができます。

## articles/ai-services/openai/includes/typescript.md{#item-ee5b93}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,223 @@
+---
+title: 'Quickstart: Use Azure OpenAI Service with the JavaScript SDK and the completions API'
+titleSuffix: Azure OpenAI
+description: Walkthrough on how to get started with Azure OpenAI and make your first completions call with the JavaScript SDK. 
+#services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+author: mrbullwinkle
+ms.author: mbullwin
+ms.date: 10/22/2024
+---
+
+[Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
+
+> [!NOTE]
+> This article has been updated to use the [latest OpenAI npm package](https://www.npmjs.com/package/openai) which now fully supports Azure OpenAI. If you are looking for code examples for the legacy Azure OpenAI JavaScript SDK they are currently still [available in this repo](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples/v2-beta/javascript).
+
+## Prerequisites
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [TypeScript](https://www.typescriptlang.org/download/)
+- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
+- An Azure OpenAI Service resource with the `gpt-35-turbo-instruct` model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
+
+> [!div class="nextstepaction"]
+> [I ran into an issue with the prerequisites.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=JAVASCRIPT&Pillar=AOAI&&Product=gpt&Page=quickstart&Section=Prerequisites)
+
+## Set up
+
+[!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
+
+[!INCLUDE [environment-variables](environment-variables.md)]
+
+In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it.
+
+## Install the client library
+
+Install the required packages for JavaScript with npm from within the context of your new directory:
+
+```console
+npm install openai @azure/identity
+```
+
+Your app's _package.json_ file will be updated with the dependencies.
+
+> [!div class="nextstepaction"]
+> [I ran into an issue with the setup.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=JAVASCRIPT&Pillar=AOAI&&Product=gpt&Page=quickstart&Section=Set-up-the-environment)
+
+## Create a sample application
+
+Open a command prompt where you created the new project, and create a new file named Completion.ts. Copy the following code into the Completion.ts file.
+
+## [Microsoft Entra ID](#tab/typescript-keyless)
+
+```typescript
+import { 
+  DefaultAzureCredential, 
+  getBearerTokenProvider 
+} from "@azure/identity";
+import { AzureOpenAI } from "openai";
+import { type Completion } from "openai/resources/index";
+
+// You will need to set these environment variables or edit the following values
+const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+
+// Required Azure OpenAI deployment name and API version
+const apiVersion = "2024-08-01-preview";
+const deploymentName = "gpt-35-turbo-instruct";
+
+// keyless authentication    
+const credential = new DefaultAzureCredential();
+const scope = "https://cognitiveservices.azure.com/.default";
+const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+
+// Chat prompt and max tokens
+const prompt = ["When was Microsoft founded?"];
+const maxTokens = 128;
+
+function getClient(): AzureOpenAI {
+  return new AzureOpenAI({
+    endpoint,
+    azureADTokenProvider,
+    apiVersion,
+    deployment: deploymentName,
+  });
+}
+async function getCompletion(
+  client: AzureOpenAI,
+  prompt: string[],
+  max_tokens: number
+): Promise<Completion> {
+  return client.completions.create({
+    prompt,
+    model: "",
+    max_tokens,
+  });
+}
+async function printChoices(completion: Completion): Promise<void> {
+  for (const choice of completion.choices) {
+    console.log(choice.text);
+  }
+}
+export async function main() {
+  console.log("== Get completions Sample ==");
+
+  const client = getClient();
+  const completion = await getCompletion(client, prompt, maxTokens);
+  await printChoices(completion);
+}
+
+main().catch((err) => {
+  console.error("Error occurred:", err);
+});
+```
+
+Build the script with the following command:
+
+```cmd
+tsc
+```
+
+Run the script with the following command:
+
+```cmd
+node.exe Completion.js
+```
+
+## [API key](#tab/typescript-key)
+
+```typescript
+import { AzureOpenAI } from "openai";
+import { type Completion } from "openai/resources/index";
+
+// You will need to set these environment variables or edit the following values
+const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+
+// Required Azure OpenAI deployment name and API version
+const apiVersion = "2024-08-01-preview";
+const deploymentName = "gpt-35-turbo-instruct";
+
+// Chat prompt and max tokens
+const prompt = ["When was Microsoft founded?"];
+const maxTokens = 128;
+
+function getClient(): AzureOpenAI {
+  return new AzureOpenAI({
+    endpoint,
+    apiKey,
+    apiVersion,
+    deployment: deploymentName,
+  });
+}
+async function getCompletion(
+  client: AzureOpenAI,
+  prompt: string[],
+  max_tokens: number
+): Promise<Completion> {
+  return client.completions.create({
+    prompt,
+    model: "",
+    max_tokens,
+  });
+}
+async function printChoices(completion: Completion): Promise<void> {
+  for (const choice of completion.choices) {
+    console.log(choice.text);
+  }
+}
+export async function main() {
+  console.log("== Get completions Sample ==");
+
+  const client = getClient();
+  const completion = await getCompletion(client, prompt, maxTokens);
+  await printChoices(completion);
+}
+
+main().catch((err) => {
+  console.error("Error occurred:", err);
+});
+```
+
+Build the script with the following command:
+
+```cmd
+tsc
+```
+
+Run the script with the following command:
+
+```cmd
+node.exe Completion.js
+```
+
+---
+
+## Output
+
+```output
+== Get completions Sample ==
+
+Microsoft was founded on April 4, 1975.
+```
+
+> [!NOTE]
+> If your receive the error: *Error occurred: OpenAIError: The `apiKey` and `azureADTokenProvider` arguments are mutually exclusive; only one can be passed at a time.* You may need to remove a pre-existing environment variable for the API key from your system. Even though the Microsoft Entra ID code sample is not explicitly referencing the API key environment variable, if one is present on the system executing this sample, this error will still be generated.
+
+> [!div class="nextstepaction"]
+> [I ran into an issue when running the code sample.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=JAVASCRIPT&Pillar=AOAI&&Product=gpt&Page=quickstart&Section=Create-application)
+
+## Clean up resources
+
+If you want to clean up and remove an Azure OpenAI resource, you can delete the resource. Before deleting the resource, you must first delete any deployed models.
+
+- [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
+- [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
+
+## Next steps
+
+* [Azure OpenAI Overview](../overview.md)
+* For more examples, check out the [Azure OpenAI Samples GitHub repository](https://aka.ms/AOAICodeSamples)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIサービスでTypeScriptを使用するためのクイックスタートガイドを追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるTypeScriptの使用に関する新しいドキュメントが追加されたことを示しています。新しいファイル「typescript.md」には、Azure OpenAI ServiceをJavaScript SDKとcompletions APIと共に使用するためのクイックスタートガイドが含まれており、223行が追加されています。

ドキュメントには、必要な準備、クライアントライブラリのインストール手順、サンプルアプリケーションの作成方法、実際のコード例、出力結果が詳述されています。また、Microsoft Entra IDを用いたキーレス認証やAPIキーを利用した認証の手法も示されています。

この追加により、開発者はAzure OpenAIサービスをTypeScriptで迅速に使用開始できるようになり、コード例やセットアップ手順が明確に提示されています。また、リソースのクリーンアップ手順や次のステップへのリンクも提供されており、使いやすさが向上しています。

全体的に、この新機能は、開発者がTypeScriptを使用してAzure OpenAIサービスに迅速にアクセスできるようにすることを目指しています。

## articles/ai-services/openai/includes/use-your-data-javascript.md{#item-786699}

<details>
<summary>Diff</summary>
````diff
@@ -5,13 +5,14 @@ author: glharper
 ms.author: glharper
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 09/06/2024
+ms.date: 10/22/2024
 ---
 
 [!INCLUDE [Set up required variables](./use-your-data-common-variables.md)]
 
 
-## Create a Node application
+
+## Initialize a Node.js application
 
 In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
 
@@ -23,50 +24,40 @@ npm init
 
 Install the Azure OpenAI client and Azure Identity libraries for JavaScript with npm:
 
-#### [TypeScript](#tab/typescript)
-
-```console
-npm install openai @azure/identity @azure/openai 
-```
-
-The `@azure/openai/types` dependency is included to extend the Azure OpenAI model for the `data_sources` property. This import is only necessary for TypeScript.
-
-#### [JavaScript](#tab/javascript)
-
 ```console
 npm install @azure/openai @azure/identity
 ```
 
----
-
 Your app's _package.json_ file will be updated with the dependencies.
 
-## Create a sample application
+## Add the JavaScript code
 
-#### [TypeScript](#tab/typescript)
+#### [Microsoft Entra ID](#tab/javascript-keyless)
 
-1. Open a command prompt where you want the new project, and create a new file named `ChatWithOwnData.ts`. Copy the following code into the `ChatWithOwnData.ts` file.
+1. Open a command prompt where you want the new project, and create a new file named `ChatWithOwnData.js`. Copy the following code into the `ChatWithOwnData.js` file.
     
-    ```typescript
-    import "dotenv/config";
-    import { AzureOpenAI } from "openai";
-    import "@azure/openai/types";
+    ```javascript
+    const { DefaultAzureCredential, getBearerTokenProvider } = require("@azure/identity");
+    const { AzureOpenAI } = require("openai");
     
     // Set the Azure and AI Search values from environment variables
     const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"];
     const searchEndpoint = process.env["AZURE_AI_SEARCH_ENDPOINT"];
-    const searchKey = process.env["AZURE_AI_SEARCH_API_KEY"];
     const searchIndex = process.env["AZURE_AI_SEARCH_INDEX"];
-    
+
+    // keyless authentication    
+    const credential = new DefaultAzureCredential();
+    const scope = "https://cognitiveservices.azure.com/.default";
+    const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+
     // Required Azure OpenAI deployment name and API version
     const deploymentName = "gpt-4";
     const apiVersion = "2024-07-01-preview";
     
-    function getClient(): AzureOpenAI {
+    function getClient() {
       return new AzureOpenAI({
         endpoint,
-        apiKey,
+        azureADTokenProvider,
         deployment: deploymentName,
         apiVersion,
       });
@@ -126,24 +117,18 @@ Your app's _package.json_ file will be updated with the dependencies.
     });
     ```
 
-1. Build the application with the following command:
-
-    ```console
-    tsc
-    ```
-
 1. Run the application with the following command:
 
     ```console
     node ChatWithOwnData.js
     ```
 
-#### [JavaScript](#tab/javascript)
+
+#### [API key](#tab/javascript-key)
 
 1. Open a command prompt where you want the new project, and create a new file named `ChatWithOwnData.js`. Copy the following code into the `ChatWithOwnData.js` file.
     
     ```javascript
-    require("dotenv/config");
     const { AzureOpenAI } = require("openai");
     
     // Set the Azure and AI Search values from environment variables
@@ -228,6 +213,7 @@ Your app's _package.json_ file will be updated with the dependencies.
 
 ---
 
+
 > [!IMPORTANT]
 > For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see the Azure AI services [security](../../security-features.md) article.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Node.jsアプリケーションの初期化およびサンプルコードの変更"
}
```

### Explanation
この変更は、Azure OpenAIサービスを利用するJavaScriptコードに関するドキュメント「use-your-data-javascript.md」に加えられたもので、主に内容の更新と構造の改善が行われました。20行が追加され、34行が削除され、全体で54行の変更が行われています。

変更点には、Node.jsアプリケーションの初期化手順が「Create a Node application」から「Initialize a Node.js application」に名称変更され、手順がより明確になった点が含まれています。また、TypeScriptに関する項目が削除され、JavaScriptにのみ焦点を当てるように整理されています。

さらに、最初のサンプルコードがTypeScriptからJavaScriptに更新され、`dotenv`モジュールは使用せず、Microsoft Entra IDを用いたキーレス認証が導入されています。また、APIキーを必要としない形式が強調され、クライアントを初期化するためのコードも簡素化されています。

全体として、このマイナーアップデートは、JavaScriptユーザーにとっての可用性を向上させ、特にAzure OpenAIサービスを利用する際のコードの整然さと使いやすさを向上させることを目的としています。さらに、セキュリティ関連の重要な注意事項も追加されており、実運用環境での資格情報の安全な管理方法が強調されています。

## articles/ai-services/openai/includes/use-your-data-typescript.md{#item-ec0b7e}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,245 @@
+---
+#services: cognitive-services
+manager: nitinme
+author: glharper
+ms.author: glharper
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 10/22/2024
+---
+
+[!INCLUDE [Set up required variables](./use-your-data-common-variables.md)]
+
+
+## Initialize a Node.js application
+
+In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+
+```console
+npm init
+```
+
+## Install the client library
+
+Install the Azure OpenAI client and Azure Identity libraries for JavaScript with npm:
+
+```console
+npm install openai @azure/identity @azure/openai 
+```
+
+The `@azure/openai/types` dependency is included to extend the Azure OpenAI model for the `data_sources` property. This import is only necessary for TypeScript.
+
+
+Your app's _package.json_ file will be updated with the dependencies.
+
+## Add the TypeScript code
+
+#### [Microsoft Entra ID](#tab/typescript-keyless)
+
+1. Open a command prompt where you want the new project, and create a new file named `ChatWithOwnData.ts`. Copy the following code into the `ChatWithOwnData.ts` file.
+    
+    ```typescript
+    import { AzureOpenAI } from "openai";
+    import { DefaultAzureCredential, getBearerTokenProvider } from "@azure/identity";
+    import "@azure/openai/types";
+    
+    // Set the Azure and AI Search values from environment variables
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
+    const searchEndpoint = process.env["AZURE_AI_SEARCH_ENDPOINT"];
+    const searchIndex = process.env["AZURE_AI_SEARCH_INDEX"];
+    
+    // keyless authentication    
+    const credential = new DefaultAzureCredential();
+    const scope = "https://cognitiveservices.azure.com/.default";
+    const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+
+    // Required Azure OpenAI deployment name and API version
+    const deploymentName = "gpt-4";
+    const apiVersion = "2024-07-01-preview";
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        azureADTokenProvider,
+        deployment: deploymentName,
+        apiVersion,
+      });
+    }
+    
+    async function main() {
+      const client = getClient();
+    
+      const messages = [
+        { role: "user", content: "What are my available health plans?" },
+      ];
+    
+      console.log(`Message: ${messages.map((m) => m.content).join("\n")}`);
+    
+      const events = await client.chat.completions.create({
+        stream: true,
+        messages: [
+          {
+            role: "user",
+            content:
+              "What's the most common feedback we received from our customers about the product?",
+          },
+        ],
+        max_tokens: 128,
+        model: "",
+        data_sources: [
+          {
+            type: "azure_search",
+            parameters: {
+              endpoint: searchEndpoint,
+              index_name: searchIndex,
+              authentication: {
+                type: "api_key",
+                key: searchKey,
+              },
+            },
+          },
+        ],
+      });
+    
+      let response = "";
+      for await (const event of events) {
+        for (const choice of event.choices) {
+          const newText = choice.delta?.content;
+          if (newText) {
+            response += newText;
+            // To see streaming results as they arrive, uncomment line below
+            // console.log(newText);
+          }
+        }
+      }
+      console.log(response);
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
+    node ChatWithOwnData.js
+    ```
+
+
+#### [API key](#tab/typescript-key)
+
+1. Open a command prompt where you want the new project, and create a new file named `ChatWithOwnData.ts`. Copy the following code into the `ChatWithOwnData.ts` file.
+    
+    ```typescript
+    import { AzureOpenAI } from "openai";
+    import "@azure/openai/types";
+    
+    // Set the Azure and AI Search values from environment variables
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"];
+    const searchEndpoint = process.env["AZURE_AI_SEARCH_ENDPOINT"];
+    const searchKey = process.env["AZURE_AI_SEARCH_API_KEY"];
+    const searchIndex = process.env["AZURE_AI_SEARCH_INDEX"];
+    
+    // Required Azure OpenAI deployment name and API version
+    const deploymentName = "gpt-4";
+    const apiVersion = "2024-07-01-preview";
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        deployment: deploymentName,
+        apiVersion,
+      });
+    }
+    
+    async function main() {
+      const client = getClient();
+    
+      const messages = [
+        { role: "user", content: "What are my available health plans?" },
+      ];
+    
+      console.log(`Message: ${messages.map((m) => m.content).join("\n")}`);
+    
+      const events = await client.chat.completions.create({
+        stream: true,
+        messages: [
+          {
+            role: "user",
+            content:
+              "What's the most common feedback we received from our customers about the product?",
+          },
+        ],
+        max_tokens: 128,
+        model: "",
+        data_sources: [
+          {
+            type: "azure_search",
+            parameters: {
+              endpoint: searchEndpoint,
+              index_name: searchIndex,
+              authentication: {
+                type: "api_key",
+                key: searchKey,
+              },
+            },
+          },
+        ],
+      });
+    
+      let response = "";
+      for await (const event of events) {
+        for (const choice of event.choices) {
+          const newText = choice.delta?.content;
+          if (newText) {
+            response += newText;
+            // To see streaming results as they arrive, uncomment line below
+            // console.log(newText);
+          }
+        }
+      }
+      console.log(response);
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
+    node ChatWithOwnData.js
+    ```
+
+
+---
+
+
+> [!IMPORTANT]
+> For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see the Azure AI services [security](../../security-features.md) article.
+
+
+## Output
+
+```output
+Message: What are my available health plans?
+The available health plans in the Contoso Electronics plan and benefit packages are the Northwind Health Plus and Northwind Standard plans.
+
+```
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "TypeScriptを使用したデータの利用に関するガイドを追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスでTypeScriptを使用してデータを利用するための新しいドキュメント「use-your-data-typescript.md」が追加されたことを示しています。245行が新規追加され、削除はありません。この新しいガイドは、Node.jsアプリケーションを初期化し、Azure OpenAIを利用するためのクライアントライブラリのインストール手順、及びサンプルコードを詳細に説明しています。

具体的には、まず新しいNode.jsアプリケーションを初期化し、必要なライブラリ（`openai`および`@azure/identity`）をインストールする手順が示されています。次に、Microsoft Entra IDを活用したキーレス認証の実装方法が説明され、実際にクライアントを作成し、チャットメッセージを送信するプロセスが記述されています。サンプルコードは、ユーザーからのメッセージを受け取り、Azure AI Searchからのデータを取得して応答を生成する流れを示しています。

また、アプリケーションのビルドや実行方法に関する指示も提供されており、実運用環境での資格情報の安全な管理に関する重要な注意事項が追加されています。

全体として、この新機能は、TypeScriptを使用するユーザーに対して、Azure OpenAIサービスを活用したデータの利用方法を提供し、初期設定から実践的なコード例まで幅広くサポートする内容となっています。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -72,28 +72,29 @@ Azure OpenAI processes text by breaking it down into tokens. Tokens can be words
 
 The total number of tokens processed in a given request depends on the length of your input, output and request parameters. The quantity of tokens being processed will also affect your response latency and throughput for the models.
  
-#### Image tokens (GPT-4 Turbo with Vision and GPT-4o)
-
-The token cost of an input image depends on two main factors: the size of the image and the detail setting (low or high) used for each image. Here's a breakdown of how it works:
-
-- **Detail: Low resolution mode**
-    - Low detail allows the API to return faster responses and consume fewer input tokens for use cases that don’t require high detail.
-    - These images cost 85 tokens each, regardless of the image size.
-    - **Example: 4096 x 8192 image (low detail)**: The cost is a fixed 85 tokens, because it's a low detail image, and the size doesn't affect the cost in this mode.
-      
-- **Detail: High resolution mode**
-    - High detail lets the API see the image in more detail by cropping it into smaller squares. Each square uses more tokens to generate text.
-    - The token cost is calculated by a series of scaling steps:
-        1. The image is first scaled to fit within a 2048 x 2048 square while maintaining its aspect ratio.
-        1. The image is then scaled down so that the shortest side is 768 pixels long.
-        1. The image is divided into 512-pixel square tiles, and the number of these tiles (rounding up for partial tiles) determines the final cost. Each tile costs 170 tokens.
-        1. An additional 85 tokens are added to the total cost.
-    - **Example: 2048 x 4096 image (high detail)**
-        1. Initially resized to 1024 x 2048 to fit in the 2048 square.
-        1. Further resized to 768 x 1536.
-        1. Requires six 512px tiles to cover.
-        1. Total cost is `170 × 6 + 85 = 1105` tokens.
-
+#### Image tokens
+
+Azure OpenAI's image processing capabilities with GPT-4o, GPT-4o mini, and GPT-4 Turbo with Vision models uses image tokenization to determine the total number of tokens consumed by image inputs. The number of tokens consumed is calculated based on two main factors: the level of image detail (low or high) and the image’s dimensions. Here's how token costs are calculated:
+
+- **Low resolution mode**
+  - Low detail allows the API to return faster responses for scenarios that don't require high image resolution analysis. The tokens consumed for low detail images are:
+    - **GPT-4o and GPT-4 Turbo with Vision**: Flat rate of **85 tokens per image**, regardless of size.
+    - **GPT-4o mini**: Flat rate of **2833 tokens per image**, regardless of size.
+  - **Example: 4096 x 8192 image (low detail)**: The cost is a fixed 85 tokens, because it's a low detail image, and the size doesn't affect the cost in this mode.
+- **High resolution mode**
+  - Low detail allows the API to analyze images in more detail. Image tokens are calculated based on the image's dimensions. The calculation involves the following steps:
+    1. **Image resizing**: The image is resized to fit within a 2048 x 2048 pixel square. If the shortest side is larger than 768 pixels, the image is further resized so that the shortest side is 768 pixels long. The aspect ratio is preserved during resizing.
+    1. **Tile calculation**: Once resized, the image is divided into 512 x 512 pixel tiles. Any partial tiles are rounded up to a full tile. The number of tiles determines the total token cost.
+    1. **Token calculation**:
+        - **GPT-4o and GPT-4 Turbo with Vision**: Each 512 x 512 pixel tile costs **170 tokens**. An extra **85 base tokens** are added to the total.
+        - **GPT-4o mini**: Each 512 x 512 pixel tile costs **5667 tokens**. An extra **2833 base tokens** are added to the total.
+  - **Example: 2048 x 4096 image (high detail)**:
+    1. The image is initially resized to 1024 x 2048 pixels to fit within the 2048 x 2048 pixel square.
+    2. The image is further resized to 768 x 1536 pixels to ensure the shortest side is a maximum of 768 pixels long.
+    3. The image is divided into 2 x 3 tiles, each 512 x 512 pixels.
+    4. **Final calculation**: 
+        - For GPT-4o and GPT-4 Turbo with Vision, the total token cost is 6 tiles x 170 tokens per tile + 85 base tokens = 1105 tokens.
+        - For GPT-4o mini, the total token cost is 6 tiles x 5667 tokens per tile + 2833 base tokens = 36835 tokens.
 
 ### Resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像トークンに関する詳細を更新"
}
```

### Explanation
この変更は、Azure OpenAIの「overview.md」ドキュメントにおいて、画像トークンの処理に関する情報を更新したものです。今回の変更では、23行が追加され、22行が削除され、合計で45行の変更が行われています。

主な更新点として、画像処理に関するセクションが整理され、トークンコストの計算方法が明確に説明されています。具体的には、GPT-4o、GPT-4o mini、GPT-4 Turbo with Visionモデルの各画像トークンの消費方法が異なる詳細として記載されています。

低解像度モードでは、画像サイズに関わらず、GPT-4oおよびGPT-4 Turbo with Visionが1枚あたり85トークン、GPT-4o miniが2833トークンで処理されることが記載されています。また、高解像度モードでは、画像を512x512ピクセルのタイルに分割し、特定のトークンコストをもとに計算するプロセスが追加されています。これにより、トークンの最終コストがどのように算出されるかが詳細に説明され、ユーザーがより理解しやすくなるように修正されています。

この更新により、AIサービス利用者に対して、画像トークンの計算についての情報がより具体的かつ体系的に提供され、実際の使用シナリオでの理解を助けることを目的としています。

## articles/ai-services/openai/quickstart.md{#item-7d1656}

<details>
<summary>Diff</summary>
````diff
@@ -52,6 +52,11 @@ Use this article to get started making your first calls to Azure OpenAI.
 
 [!INCLUDE [JavaScript quickstart](includes/javascript.md)]
 
+::: zone-end
+::: zone pivot="programming-language-typescript"
+
+[!INCLUDE [TypeScript quickstart](includes/typescript.md)]
+
 ::: zone-end
 
 ::: zone pivot="programming-language-python"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScript向けクイックスタートガイドへのリンクを追加"
}
```

### Explanation
この変更は、「quickstart.md」ドキュメントにおいてTypeScript向けのクイックスタートガイドへのリンクを追加したことを示しています。具体的には、5行が追加され、削除はありません。

更新内容としては、TypeScriptプログラミング言語のセクションが追加され、対応する「includes/typescript.md」ファイルへのリンクが示されています。この追加により、ユーザーはJavaScriptとPythonに加えて、TypeScriptを用いたAzure OpenAIの利用方法を簡単に確認できるようになります。

これによって、クイックスタートガイドがより包括的になり、さまざまなプログラミング言語のユーザーに対するサポートが強化されることを目的としています。特に、TypeScriptを利用した開発者にとって、迅速に必要な情報へアクセスできることが期待されます。

## articles/ai-services/openai/reference.md{#item-7b1183}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's REST API. In this article, you lear
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 09/09/2024
+ms.date: 11/01/2024
 author: mrbullwinkle 
 ms.author: mbullwin
 recommendations: false
@@ -21,7 +21,7 @@ This article provides details on the inference REST API endpoints for Azure Open
 
 ## Data plane inference
 
-The rest of the article covers the latest GA release of the Azure OpenAI data plane inference specification, `2024-06-01`.
+The rest of the article covers the latest GA release of the Azure OpenAI data plane inference specification, `2024-10-21`.
 
 If you're looking for documentation on the latest preview API release, refer to the [latest preview data plane inference API](./reference-preview.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付と仕様バージョンの更新"
}
```

### Explanation
この変更は、「reference.md」ドキュメントにおいて、日付とAzure OpenAIデータプレーン推論仕様のバージョンを更新したことを示しています。具体的には、2行が追加され、2行が削除され、合計で4行の変更が行われています。

主な内容としては、ドキュメント内の文の更新が含まれています。具体的には、文書のメタデータに記載されている日付が「09/09/2024」から「11/01/2024」に変更されており、また、Azure OpenAIデータプレーン推論仕様の最新GAリリースのバージョンも「2024-06-01」から「2024-10-21」に更新されています。

この更新により、ユーザーは最新のAPIリリースおよびその仕様に関する正確な情報にアクセスできるようになり、Azure OpenAIの利用における信頼性が向上します。これにより、文書が常に最新の情報を反映することが保証され、利用者にとって有益なリソースとなることが目的とされています。

## articles/ai-services/openai/use-your-data-quickstart.md{#item-52c1f4}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom: devx-track-dotnet, devx-track-extended-java, devx-track-js, devx-trac
 ms.topic: quickstart
 author: aahill
 ms.author: aahi
-ms.date: 08/21/2024
+ms.date: 10/22/2024
 recommendations: false
 zone_pivot_groups: openai-use-your-data
 ---
@@ -84,38 +84,48 @@ The following resources:
 
 ## Prerequisites
 
-#### [TypeScript](#tab/typescript)
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
-
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
-- [TypeScript](https://www.typescriptlang.org/download/)
-
+- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI resource deployed in a [supported region and with a supported model](./concepts/use-your-data.md#regional-availability-and-model-support).
 
 - Be sure that you're assigned at least the [Cognitive Services Contributor](./how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
 
 - Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
 
 
-#### [JavaScript](#tab/javascript)
+[Reference documentation](https://platform.openai.com/docs/api-reference/chat) | [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
+
+
+[!INCLUDE [Connect your data to OpenAI](includes/connect-your-data-studio.md)]
+
+[!INCLUDE [JavaScript quickstart](includes/use-your-data-javascript.md)]
+
+::: zone-end
+
+::: zone pivot="programming-language-typescript"
+
+## Prerequisites
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
+
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [TypeScript](https://www.typescriptlang.org/download/)
+- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI resource deployed in a [supported region and with a supported model](./concepts/use-your-data.md#regional-availability-and-model-support).
 
 - Be sure that you're assigned at least the [Cognitive Services Contributor](./how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
 
 - Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
 
----
 
 [Reference documentation](https://platform.openai.com/docs/api-reference/chat) | [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
 
 
 [!INCLUDE [Connect your data to OpenAI](includes/connect-your-data-studio.md)]
 
-[!INCLUDE [JavaScript quickstart](includes/use-your-data-javascript.md)]
+[!INCLUDE [TypeScript quickstart](includes/use-your-data-typescript.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptに関する内容の強化と日付の更新"
}
```

### Explanation
この変更は、「use-your-data-quickstart.md」ドキュメントに対して行われ、主にTypeScriptに関連するコンテンツの強化と日付の更新が含まれています。具体的には、18行が追加され、8行が削除され、合計で26行の変更が行われています。

主な更新点としては、以下の変更が含まれています：

1. 文書のメタデータにおいて、最終更新日が「08/21/2024」から「10/22/2024」に変更されました。
2. TypeScriptに関するセクションが追加され、設定に必要なリソースや手順が詳しく説明されています。このセクションには、Azure CLI の使用や、Node.js と TypeScript のサポート情報が含まれています。
3. TypeScript向けのクイックスタートガイドへのリンクが、新たに追加されました。

これにより、TypeScriptを使用した開発者にとって、必要な情報がより明確に提供されるとともに、ガイドが最新の状態を反映するようになります。この更新は、Azure OpenAIの利用方法を学ぶ開発者にとって、より実用的で有益なリソースとなることを目指しています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ This article provides a summary of the latest releases and major documentation u
 ## October 2024
 
 ### NEW data zone standard deployment type
-Data zone standard deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. Data zone standard provides higher default quotas than our Azure geography-based deployment types.  Data zone standard deployments are supported on `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13, and `gpt-4o-mini-2024-07-18` models.
+Data zone standard deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. Data zone standard provides higher default quotas than our Azure geography-based deployment types.  Data zone standard deployments are supported on `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, and `gpt-4o-mini-2024-07-18` models.
 
 For more information, see the [deployment types guide](https://aka.ms/aoai/docs/deployment-types).
 
@@ -825,4 +825,4 @@ New training course:
 
 ## Next steps
 
-Learn more about the [underlying models that power Azure OpenAI](./concepts/models.md).
\ No newline at end of file
+Learn more about the [underlying models that power Azure OpenAI](./concepts/models.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいデータゾーン標準展開タイプの説明を更新"
}
```

### Explanation
この変更は、「whats-new.md」ドキュメントに対して行われ、主に新しいデータゾーン標準展開タイプに関する説明の軽微な修正が含まれています。具体的には、2行が追加され、2行が削除され、合計で4行の変更が行われています。

主な更新内容としては、以下の事項が挙げられます：

1. **モデルズのサポート表記の修正**：データゾーン標準展開がサポートするモデルのリストにおいて、モデル名の間のカンマの記述に誤りがありましたが、これが修正されました。具体的には、`gpt-4o-2024-05-13`の後にカンマが追加されています。
   
2. **全体的な文の流れの維持**：基本的に内容は変更されていないものの、モデル名の表記を整理することで、情報の正確性が向上しています。

この更新は、Azure OpenAIの新たな展開タイプについての情報を正確に反映させることを目的としており、ユーザーが最新のリリースや機能に関する理解を深めるのに役立ちます。また、ドキュメント全体の整合性を保つことで、開発者や利用者にとってより信頼性の高い情報源となることを目指しています。


