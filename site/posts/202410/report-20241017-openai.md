---
date: '2024-10-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9a3d20f...MicrosoftDocs:00d70d8
summary: この一連の変更は、Azure OpenAI Serviceに関連するドキュメントの更新に関するもので、主にAPIバージョンやサポートライフサイクルの日付、バッチ処理のポリシーと制限に関する情報が詳しく、明確に提供されています。新機能として、2024-10-01-previewのAPIバージョンが導入され、バッチ処理のレスポンスヘッダーが追加されました。また、DALL-Eモデルの使用例やスタイルガイドも改良されています。注意すべきは、一部のAPIバージョンが変更されているため、旧版を使っている場合には留意が必要です。さらに、モデルのクォータ制限が見直され、バッチ処理のドキュメントがPythonとREST専用に具体例を豊富に更新されました。これらの更新は、開発者やデータサイエンティストにとって非常に役立つもので、ユーザーエクスペリエンスの向上を目指しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9a3d20f...MicrosoftDocs:00d70d8){target="_blank"}

# ハイライト
この一連の変更は、Azure OpenAI Serviceに関連するドキュメントの更新を主としています。更新内容は、APIのバージョンやサポートライフサイクルの日付、バッチ処理のポリシー、制限に関する情報を中心に、より詳細で明確な情報を提供することに焦点を当てています。

## 新機能
- 新しいAPIバージョンとして`2024-10-01-preview`が導入されました。
- バッチ処理において、REST APIの呼び出しにおける新たなレスポンスヘッダーの追加。
- DALL-Eモデルにおいて、使用例やスタイルガイドの改良。

## ブレイクポイント
- APIバージョンの一部が新たに変更されているため、旧版を明示的に使用している場合、注意が必要です。

## その他の更新
- OpenAIのモデルクォータ制限が見直され、バッチクォータの制限が一部変更されています。
- バッチ処理機能のドキュメントの多くがPythonとREST専用に更新され、具体例がより豊富に示されています。

# インサイト
この更新は、Azure OpenAIのサービスを利用する開発者やデータサイエンティストにとって、相当に役立つと言えるでしょう。APIバージョンやバッチ処理に関する更新は、ユーザーが最新の技術進化に追随するために不可欠です。

特に注目するべきは、バッチ処理に関連する新たな推奨事項や制限情報が追加された点です。これにより、ユーザーは大規模なバッチ処理をより効率的に管理し、予期しないエラーや制限違反を未然に防ぐことが容易になります。また、バッチ処理におけるファイル管理に関するガイダンスは、特定の実装における最適な戦略を提供しています。

DALL-Eモデルに関する更新では、具体的な使用事例が増加しており、ユーザーが創造的なタスクをAzureの機能を利用して実現するための知識ベースが強化されています。さらに、エラーハンドリングやプロンプトフィルタリングの情報も追加されたため、ユーザーはより洗練されたAPI呼び出しを実現しやすくなります。

全体として、これらのドキュメント更新は、Azure OpenAIサービスの利用を容易にし、ユーザーエクスペリエンスを向上させることを目的としています。最新の更新内容を反映したドキュメントは、問題解決の加速と新規開発の効率化に寄与することでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [api-version-deprecation.md](#item-1cad50) | minor update | APIバージョンの更新に関するドキュメント修正 | modified | 3 | 3 | 6 | 
| [batch.md](#item-a131d5) | minor update | バッチ処理に関するAzure OpenAIサービスのドキュメント更新 | modified | 13 | 6 | 19 | 
| [dall-e.md](#item-ac9616) | minor update | DALL-Eモデルに関するドキュメントの更新 | modified | 23 | 28 | 51 | 
| [api-surface.md](#item-a25fa2) | minor update | API表のリリース日付の更新 | modified | 2 | 2 | 4 | 
| [latest-inference-preview.md](#item-24bf0f) | minor update | 最新推論プレビューAPIに関するドキュメントの更新 | modified | 226 | 159 | 385 | 
| [batch-python.md](#item-3121c2) | minor update | バッチ処理に関するPythonドキュメントの更新 | modified | 236 | 2 | 238 | 
| [batch-rest.md](#item-bcccd9) | minor update | REST APIによるバッチ処理のドキュメント更新 | modified | 22 | 7 | 29 | 
| [batch-studio.md](#item-d4822e) | minor update | バッチスタジオに関するドキュメントの更新 | modified | 2 | 0 | 2 | 
| [global-batch-limits.md](#item-73207b) | minor update | グローバルバッチ制限に関するドキュメント改訂 | modified | 6 | 6 | 12 | 
| [quota.md](#item-389aa1) | minor update | モデルクォータに関するドキュメントの更新 | modified | 3 | 3 | 6 | 
| [global-batch.png](#item-6fbc0c) | minor update | グローバルバッチに関する画像の更新 | modified | 0 | 0 | 0 | 
| [reference-preview.md](#item-e197a2) | minor update | Azure OpenAIのリファレンスプレビューの更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/openai/api-version-deprecation.md{#item-1cad50}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 10/01/2024
+ms.date: 10/16/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -23,8 +23,8 @@ This article is to help you understand the support lifecycle for the Azure OpenA
 
 Azure OpenAI API latest release:
 
-- Inference: [2024-09-01-preview](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2024-09-01-preview/inference.json)
-- Authoring: [2024-08-01-preview](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/2024-08-01-preview/azureopenai.json)
+- Inference: [2024-10-01-preview](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2024-10-01-preview/inference.json)
+- Authoring: [2024-10-01-preview](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/2024-10-01-preview/azureopenai.json)
 
 This version contains support for the latest Azure OpenAI features including:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新に関するドキュメント修正"
}
```

### Explanation
この変更は、Azure OpenAI APIに関するドキュメントの更新を示しています。具体的には、サポートライフサイクルに関連する日付やバージョン番号が修正されています。従来の更新日は2024年10月1日に変更され、最新のリリース情報が反映されています。また、InferenceおよびAuthoringのプレビュー版のリリース日も2024年10月1日としてアップデートされています。この変更は、ユーザーが最新の情報を把握できるようにするための重要な調整です。

## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn how to use global batch with Azure OpenAI Service
 manager: nitinme
 ms.service: azure-ai-openai
-ms.custom: 
+ms.custom: references_regions
 ms.topic: how-to
 ms.date: 10/14/2024
 author: mrbullwinkle
@@ -67,7 +67,7 @@ Refer to the [models page](../concepts/models.md) for the most up-to-date inform
 
 ### API support
 
-API support was first added with `2024-07-01-preview`. 
+API support was first added with `2024-07-01-preview`. Use `2024-10-01-preview` to take advantage of the latest features.
 
 ### Not supported
 
@@ -90,9 +90,7 @@ In the Studio UI the deployment type will appear as `Global-Batch`.
 :::image type="content" source="../media/how-to/global-batch/global-batch.png" alt-text="Screenshot that shows the model deployment dialog in Azure OpenAI Studio with Global-Batch deployment type highlighted." lightbox="../media/how-to/global-batch/global-batch.png":::
 
 > [!TIP]
-> Each line of your input file for batch processing has a `model` attribute that requires a global batch **deployment name**. For a given input file, all names must be the same deployment name. This is different from OpenAI where the concept of model deployments does not exist. 
->
-> For the best performance we recommend submitting large files for batch processing, rather than a large number of small files with only a few lines in each file.
+> We recommend enabling **dynamic quota** for all global batch model deployments to help avoid job failures due to insufficient enqueued token quota. Dynamic quota allows your deployment to opportunistically take advantage of more quota when extra capacity is available. When dynamic quota is set to off, your deployment will only be able to process requests up to the enqueued token limit that was defined when you created the deployment.
 
 ::: zone pivot="programming-language-ai-studio"
 
@@ -161,6 +159,15 @@ Yes. Similar to other deployment types, you can create content filters and assoc
 
 Yes, from the quota page in the Studio UI. Default quota allocation can be found in the [quota and limits article](../quotas-limits.md#global-batch-quota).
 
+### How do I tell how many tokens my batch request contains, and how many tokens are available as quota?
+
+The `2024-10-01-preview` REST API adds two new response headers:
+
+* `deployment-enqueued-tokens` - A approximate token count for your jsonl file calculated immediately after the batch request is submitted. This value represents an estimate based on the number of characters and is not the true token count.
+* `deployment-maximum-enqueued-tokens` The total available enqueued tokens available for this global batch model deployment.
+
+These response headers are only available when making a POST request to begin batch processing of a file with the REST API. The language specific client libraries do not currently return these new response headers.
+
 ### What happens if the API doesn't complete my request within the 24 hour time frame?
 
 We aim to process these requests within 24 hours; we don't expire the jobs that take longer. You can cancel the job anytime. When you cancel the job, any remaining work is cancelled and any already completed work is returned. You'll be charged for any completed work.
@@ -236,4 +243,4 @@ When a job failure occurs, you'll find details about the failure in the `errors`
 ## See also
 
 * Learn more about Azure OpenAI [deployment types](./deployment-types.md)
-* Learn more about Azure OpenAI [quotas and limits](../quotas-limits.md)
\ No newline at end of file
+* Learn more about Azure OpenAI [quotas and limits](../quotas-limits.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理に関するAzure OpenAIサービスのドキュメント更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスのバッチ処理に関するドキュメントの改訂を示しています。主な更新内容として、APIサポートに関する情報が追加され、2024年10月1日のプレビュー版を利用することで最新機能を活用できることが明記されています。また、グローバルバッチモデルデプロイメントにおけるダイナミッククォータの有効化に関する推奨事項も加えられました。さらに、2024年10月1日プレビュー版のREST APIにおいて、新しいレスポンスヘッダとして「deployment-enqueued-tokens」と「deployment-maximum-enqueued-tokens」が追加され、バッチリクエストのトークン数や使用可能なトークン数を知る方法が説明されています。これにより、ユーザーがバッチ処理をより効果的に管理できるようになっています。

## articles/ai-services/openai/how-to/dall-e.md{#item-ac9616}

<details>
<summary>Diff</summary>
````diff
@@ -7,14 +7,14 @@ ms.author: pafarley
 ms.service: azure-ai-openai
 ms.custom: 
 ms.topic: how-to
-ms.date: 03/04/2024
+ms.date: 10/02/2024
 manager: nitinme
 keywords: 
 zone_pivot_groups: 
 # Customer intent: as an engineer or hobbyist, I want to know how to use DALL-E image generation models to their full capability.
 ---
 
-# Learn how to work with the DALL-E models
+# How to work with the DALL-E models
 
 OpenAI's DALL-E models generate images based on user-provided text prompts. This guide demonstrates how to use the DALL-E models and configure their options through REST API calls.
 
@@ -23,14 +23,14 @@ OpenAI's DALL-E models generate images based on user-provided text prompts. This
 
 #### [DALL-E 3](#tab/dalle3)
 
-- An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
-- An Azure OpenAI resource created in the `SwedenCentral` region.
-- Then, you need to deploy a `dalle3` model with your Azure resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure subscription. You can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?icid=ai-services).
+- An Azure OpenAI resource created in the *Sweden Central* region. For more information, see [Create and deploy an Azure OpenAI Service resource](../how-to/create-resource.md).
+- Deploy a *dall-e-3* model with your Azure OpenAI resource.
 
 #### [DALL-E 2 (preview)](#tab/dalle2)
 
-- An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
-- An Azure OpenAI resource created in the East US region. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure subscription. You can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?icid=ai-services).
+- An Azure OpenAI resource created in the *East US* region. For more information, see [Create and deploy an Azure OpenAI Service resource](../how-to/create-resource.md).
 
 ---
 
@@ -41,14 +41,13 @@ The following command shows the most basic way to use DALL-E with code. If this
 
 #### [DALL-E 3](#tab/dalle3)
 
-
 Send a POST request to:
 
 ```
 https://<your_resource_name>.openai.azure.com/openai/deployments/<your_deployment_name>/images/generations?api-version=<api_version>
 ```
 
-where:
+**Replace the following placeholders**:
 - `<your_resource_name>` is the name of your Azure OpenAI resource.
 - `<your_deployment_name>` is the name of your DALL-E 3 model deployment.
 - `<api_version>` is the version of the API you want to use. For example, `2024-02-01`.
@@ -82,7 +81,7 @@ First, send a POST request to:
 https://<your_resource_name>.openai.azure.com/openai/images/generations:submit?api-version=<api_version>
 ```
 
-where:
+**Replace the following placeholders**:
 - `<your_resource_name>` is the name of your Azure OpenAI resource.
 - `<api_version>` is the version of the API you want to use. For example, `2023-06-01-preview`.
 
@@ -106,7 +105,7 @@ The operation returns a `202` status code and a JSON object containing the ID an
 
 ```json
 {
-  "id": "f508bcf2-e651-4b4b-85a7-58ad77981ffa",
+  "id": "3d3d3d3d-4444-eeee-5555-6f6f6f6f6f6f",
   "status": "notRunning"
 }
 ```
@@ -117,7 +116,7 @@ To retrieve the image generation results, make a GET request to:
 GET https://<your_resource_name>.openai.azure.com/openai/operations/images/<operation_id>?api-version=<api_version>
 ```
 
-where:
+**Replace the following placeholders**:
 - `<your_resource_name>` is the name of your Azure OpenAI resource.
 - `<operation_id>` is the ID of the operation returned in the previous step.
 - `<api_version>` is the version of the API you want to use. For example, `2023-06-01-preview`.
@@ -135,7 +134,6 @@ The response from this API call contains your generated image.
 
 The output from a successful image generation API call looks like the following example. The `url` field contains a URL where you can download the generated image. The URL stays active for 24 hours.
 
-
 #### [DALL-E 3](#tab/dalle3)
 
 ```json
@@ -173,7 +171,6 @@ The output from a successful image generation API call looks like the following
 ---
 
 
-
 ### API call rejection
 
 Prompts and images are filtered based on our content policy, returning an error when a prompt or image is flagged.
@@ -202,14 +199,14 @@ If your prompt is flagged, the `error.code` value in the message is set to `cont
        "code": "contentFilter",
        "message": "Your task failed as a result of our safety system."
    },
-   "id": "9484f239-9a05-41ba-997b-78252fec4b34",
+   "id": "4e4e4e4e-5555-ffff-6666-7a7a7a7a7a7a",
    "status": "failed"
 }
 ```
 
 ---
 
-It's also possible that the generated image itself is filtered. In this case, the error message is set to `Generated image was filtered as a result of our safety system.`. Here's an example:
+It's also possible that the generated image itself is filtered. In this case, the error message is set to *Generated image was filtered as a result of our safety system*. Here's an example:
 
 #### [DALL-E 3](#tab/dalle3)
 
@@ -230,7 +227,7 @@ It's also possible that the generated image itself is filtered. In this case, th
 {
    "created": 1589478378,
    "expires": 1589478399,
-   "id": "9484f239-9a05-41ba-997b-78252fec4b34",
+   "id": "4e4e4e4e-5555-ffff-6666-7a7a7a7a7a7a",
    "lastActionDateTime": 1589478378,
    "data": [
        {
@@ -251,7 +248,7 @@ It's also possible that the generated image itself is filtered. In this case, th
 
 ## Writing image prompts
 
-Your image prompts should describe the content you want to see in the image, as well as the visual style of image. 
+Your image prompts should describe the content you want to see in the image, and the visual style of image.
 
 When writing prompts, consider that the image generation APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it doesn't generate an image. For more information, see [Content filtering](../concepts/content-filter.md).
 
@@ -269,24 +266,23 @@ The following API body parameters are available for DALL-E image generation.
 
 Specify the size of the generated images. Must be one of `1024x1024`, `1792x1024`, or `1024x1792` for DALL-E 3 models. Square images are faster to generate.
 
-
 ### Style
 
-DALL-E 3 introduces two style options: `natural` and `vivid`. The `natural` style is more similar to the DALL-E 2 default style, while the `vivid` style generates more hyper-real and cinematic images.
+DALL-E 3 introduces two style options: `natural` and `vivid`. The natural style is more similar to the DALL-E 2 default style, while the vivid style generates more hyper-real and cinematic images.
 
-The `natural` style is useful in cases where DALL-E 3 over-exaggerates or confuses a subject that's meant to be more simple, subdued, or realistic.
+The natural style is useful in cases where DALL-E 3 over-exaggerates or confuses a subject that's meant to be more simple, subdued, or realistic.
 
 The default value is `vivid`.
 
 ### Quality
 
-There are two options for image quality: `hd` and `standard`. `hd` creates images with finer details and greater consistency across the image. `standard` images can be generated faster.
+There are two options for image quality: `hd` and `standard`. The hd option creates images with finer details and greater consistency across the image. Standard images can be generated faster.
 
 The default value is `standard`.
 
 ### Number
 
-With DALL-E 3, you cannot generate more than one image in a single API call: the _n_ parameter must be set to `1`. If you need to generate multiple images at once, make parallel requests.
+With DALL-E 3, you can't generate more than one image in a single API call: the `n` parameter must be set to *1*. If you need to generate multiple images at once, make parallel requests.
 
 ### Response format
 
@@ -300,18 +296,17 @@ Specify the size of the generated images. Must be one of `256x256`, `512x512`, o
 
 ### Number
 
-Set the _n_ parameter to an integer between 1 and 10 to generate multiple images at the same time using DALL-E 2. The images will share an operation ID; you receive them all with the same retrieval API call.
+Set the `n` parameter to an integer between 1 and 10 to generate multiple images at the same time using DALL-E 2. The images share an operation ID; you receive them all with the same retrieval API call.
 
 ---
 
-## Next steps
+## Related content
 
-* [Learn more about Azure OpenAI](../overview.md).
-* [DALL-E quickstart](../dall-e-quickstart.md)
+* [What is Azure OpenAI Service?](../overview.md)
+* [Quickstart: Generate images with Azure OpenAI Service](../dall-e-quickstart.md)
 * [Image generation API reference](/azure/ai-services/openai/reference#image-generation)
 
 
 <!-- OAI HT guide https://platform.openai.com/docs/guides/images/usage
 dall-e 3 features here: https://cookbook.openai.com/articles/what_is_new_with_dalle_3 -->
 
-
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL-Eモデルに関するドキュメントの更新"
}
```

### Explanation
この変更は、DALL-Eモデルに関する Azure のドキュメントを更新したもので、いくつかの重要な改善点が含まれています。まず、ドキュメントの日付が変更され、最新の情報が提供されています。また、DALL-E 3およびDALL-E 2（プレビュー）を使用する際の要件がより明確に記載され、Azureサブスクリプションやリソースの作成に関するリンクが改善されました。さらに、API呼び出しの際のプレースホルダーの説明が強調され、コマンド例も更新されています。

具体的には、DALL-E 3のスタイルや品質オプションに関する説明が改善され、生成される画像の品質に関する情報が明確化されています。また、エラーハンドリングやプロンプトフィルタリングに関する内容も追加されました。関連コンテンツのセクションも整理され、ユーザーが必要な情報に迅速にアクセスできるようになっています。このアップデートは、ユーザーがDALL-Eモデルをより効果的に利用できるようにするための重要なステップです。

## articles/ai-services/openai/includes/api-surface.md{#item-a25fa2}

<details>
<summary>Diff</summary>
````diff
@@ -22,8 +22,8 @@ Each API surface/specification encapsulates a different set of Azure OpenAI capa
 | API | Latest preview release | Latest GA release | Specifications | Description |
 |:---|:----|:----|:----|:---|
 | **Control plane** | [`2024-06-01-preview`](/rest/api/aiservices/accountmanagement/operation-groups?view=rest-aiservices-accountmanagement-2024-06-01-preview&preserve-view=true) | [`2023-05-01`](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices) | Azure OpenAI shares a common control plane with all other Azure AI Services. The control plane API is used for things like [creating Azure OpenAI resources](/rest/api/aiservices/accountmanagement/accounts/create?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), [model deployment](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), and other higher level resource management tasks. The control plane also governs what is possible to do with capabilities like Azure Resource Manager, Bicep, Terraform, and Azure CLI.|
-| **Data plane - authoring** | [`2024-08-01-preview`](/rest/api/azureopenai/operation-groups?view=rest-azureopenai-2024-08-01-preview&preserve-view=true) | [`2024-06-01`](/rest/api/azureopenai/operation-groups?view=rest-azureopenai-2024-06-01&preserve-view=true) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
-| **Data plane - inference** | [`2024-09-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-06-01`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, speech/whisper, on your data, Dall-e, assistants, etc. |
+| **Data plane - authoring** | `2024-10-01-preview` | [`2024-06-01`](/rest/api/azureopenai/operation-groups?view=rest-azureopenai-2024-06-01&preserve-view=true) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
+| **Data plane - inference** | [`2024-10-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-06-01`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, speech/whisper, on your data, Dall-e, assistants, etc. |
 
 ## Authentication
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "API表のリリース日付の更新"
}
```

### Explanation
この変更は、Azure OpenAIのAPIサーフェスに関するドキュメントの更新であり、APIのリリース日付が調整されています。具体的には、データプレーンの著作APIと推論APIの最新のプレビューリリース日がそれぞれ `2024-10-01-preview` に変更されました。この変更により、ユーザーが最新のAPIリリースを正確に把握し、利用できるようになります。また、表内の情報は整備され、関連するリンクが引き続き有効であることが確認されています。このアップデートは、ドキュメントの正確性を保つために重要です。

## articles/ai-services/openai/includes/api-versions/latest-inference-preview.md{#item-24bf0f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新推論プレビューAPIに関するドキュメントの更新"
}
```

### Explanation
この変更は、最新の推論プレビューAPIに関するドキュメントの内容を大幅に更新したものです。具体的には、追加された226行と削除された159行により、全体で385行にわたる内容の変更が行われました。この更新により、APIの使用方法、利用可能な機能、エンドポイント、レスポンス形式、そしてリクエストの構成について、より詳細かつ明確な説明が追加されています。

ユーザーは、この更新を通じて新しい機能や改善点を理解し、実際のAPI使用時に役立てることができます。特に、具体的なリクエスト例やエラーハンドリングに関する情報が充実しているため、開発者が迅速に実装を行う際の助けになります。このドキュメントのアップデートは、Azure OpenAIサービスを利用する上での重要なリソースとして、より効果的な使用を促進します。

## articles/ai-services/openai/includes/batch/batch-python.md{#item-3121c2}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Azure OpenAI model global batch Python
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 07/22/2024
+ms.date: 10/15/2024
 ---
 
 ## Prerequisites
@@ -63,6 +63,8 @@ The `custom_id` is required to allow you to identify which individual batch requ
 
 > [!IMPORTANT]
 > The `model` attribute must be set to match the name of the Global Batch deployment you wish to target for inference responses. The **same Global Batch model deployment name must be present on each line of the batch file.** If you want to target a different deployment you must do so in a separate batch file/job.
+>
+> For the best performance we recommend submitting large files for batch processing, rather than a large number of small files with only a few lines in each file.
 
 ### Create input file
 
@@ -74,13 +76,42 @@ Once your input file is prepared, you first need to upload the file to then be a
 
 [!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
+# [Python (Microsoft Entra ID)](#tab/python-secure)
+
+```python
+import os
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+client = AzureOpenAI(
+  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+  azure_ad_token_provider=token_provider,
+  api_version="2024-10-01-preview"
+)
+
+# Upload a file with a purpose of "batch"
+file = client.files.create(
+  file=open("test.jsonl", "rb"), 
+  purpose="batch"
+)
+
+print(file.model_dump_json(indent=2))
+file_id = file.id
+```
+
+# [Python (API Key)](#tab/python-key)
+
 ```python
 import os
 from openai import AzureOpenAI
     
 client = AzureOpenAI(
     api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-    api_version="2024-07-01-preview",
+    api_version="2024-10-01-preview",
     azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
     )
 
@@ -94,6 +125,8 @@ print(file.model_dump_json(indent=2))
 file_id = file.id
 ```
 
+---
+
 **Output:**
 
 ```json
@@ -367,3 +400,204 @@ List all batch jobs for a particular Azure OpenAI resource.
 ```python
 client.batches.list()
 ```
+
+### List batch (Preview)
+
+Use the REST API to list all batch jobs with additional sorting/filtering options.
+
+In the examples below we are providing the `generate_time_filter` function to make constructing the filter easier. If you don't wish to use this function the format of the filter string would look like `created_at gt 1728773533 and created_at lt 1729032733 and status eq 'Completed'`.
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
+
+```python
+import requests
+import json
+from datetime import datetime, timedelta
+from azure.identity import DefaultAzureCredential
+
+token_credential = DefaultAzureCredential()
+token = token_credential.get_token('https://cognitiveservices.azure.com/.default')
+
+endpoint = "https://{YOUR_RESOURCE_NAME}.openai.azure.com/"
+api_version = "2024-10-01-preview"
+url = f"{endpoint}openai/batches"
+order = "created_at asc"
+time_filter =  lambda: generate_time_filter("past 8 hours")
+
+# Additional filter examples:
+#time_filter =  lambda: generate_time_filter("past 1 day")
+#time_filter =  lambda: generate_time_filter("past 3 days", status="Completed")
+
+def generate_time_filter(time_range, status=None):
+    now = datetime.now()
+    
+    if 'day' in time_range:
+        days = int(time_range.split()[1])
+        start_time = now - timedelta(days=days)
+    elif 'hour' in time_range:
+        hours = int(time_range.split()[1])
+        start_time = now - timedelta(hours=hours)
+    else:
+        raise ValueError("Invalid time range format. Use 'past X day(s)' or 'past X hour(s)'")
+    
+    start_timestamp = int(start_time.timestamp())
+    end_timestamp = int(now.timestamp())
+    
+    filter_string = f"created_at gt {start_timestamp} and created_at lt {end_timestamp}"
+    
+    if status:
+        filter_string += f" and status eq '{status}'"
+    
+    return filter_string
+
+filter = time_filter()
+
+headers = {'Authorization': 'Bearer ' + token.token}
+
+params = {
+    "api-version": api_version,
+    "$filter": filter,
+    "$orderby": order
+}
+
+response = requests.get(url, headers=headers, params=params)
+
+json_data = response.json()
+
+if response.status_code == 200:
+    print(json.dumps(json_data, indent=2))
+else:
+    print(f"Request failed with status code: {response.status_code}")
+    print(response.text)  
+```
+
+# [Python (API Key)](#tab/python-key)
+
+```python
+import os
+import requests
+import json
+from datetime import datetime, timedelta
+
+api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
+endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
+api_version = "2024-10-01-preview"
+url = f"{endpoint}openai/batches"
+order = "created_at asc"
+
+time_filter = lambda: generate_time_filter("past 8 hours")
+
+# Additional filter examples:
+#time_filter =  lambda: generate_time_filter("past 1 day")
+#time_filter =  lambda: generate_time_filter("past 3 days", status="Completed")
+
+def generate_time_filter(time_range, status=None):
+    now = datetime.now()
+    
+    if 'day' in time_range:
+        days = int(time_range.split()[1])
+        start_time = now - timedelta(days=days)
+    elif 'hour' in time_range:
+        hours = int(time_range.split()[1])
+        start_time = now - timedelta(hours=hours)
+    else:
+        raise ValueError("Invalid time range format. Use 'past X day(s)' or 'past X hour(s)'")
+    
+    start_timestamp = int(start_time.timestamp())
+    end_timestamp = int(now.timestamp())
+    
+    filter_string = f"created_at gt {start_timestamp} and created_at lt {end_timestamp}"
+    
+    if status:
+        filter_string += f" and status eq '{status}'"
+    
+    return filter_string
+
+filter = time_filter()
+
+headers = {
+    "api-key": api_key
+}
+
+params = {
+    "api-version": api_version,
+    "$filter": filter,
+    "$orderby": order
+}
+
+response = requests.get(url, headers=headers, params=params)
+
+json_data = response.json()
+
+if response.status_code == 200:
+    print(json.dumps(json_data, indent=2))
+else:
+    print(f"Request failed with status code: {response.status_code}")
+    print(response.text)  
+```
+
+---
+
+**Output:**
+
+```output
+{
+  "data": [
+    {
+      "cancelled_at": null,
+      "cancelling_at": null,
+      "completed_at": 1729011896,
+      "completion_window": "24h",
+      "created_at": 1729011128,
+      "error_file_id": "file-472c0626-4561-4327-9e4e-f41afbfb30e6",
+      "expired_at": null,
+      "expires_at": 1729097528,
+      "failed_at": null,
+      "finalizing_at": 1729011805,
+      "id": "batch_4ddc7b60-19a9-419b-8b93-b9a3274b33b5",
+      "in_progress_at": 1729011493,
+      "input_file_id": "file-f89384af0082485da43cb26b49dc25ce",
+      "errors": null,
+      "metadata": null,
+      "object": "batch",
+      "output_file_id": "file-62bebde8-e767-4cd3-a0a1-28b214dc8974",
+      "request_counts": {
+        "total": 3,
+        "completed": 2,
+        "failed": 1
+      },
+      "status": "completed",
+      "endpoint": "/chat/completions"
+    },
+    {
+      "cancelled_at": null,
+      "cancelling_at": null,
+      "completed_at": 1729016366,
+      "completion_window": "24h",
+      "created_at": 1729015829,
+      "error_file_id": "file-85ae1971-9957-4511-9eb4-4cc9f708b904",
+      "expired_at": null,
+      "expires_at": 1729102229,
+      "failed_at": null,
+      "finalizing_at": 1729016272,
+      "id": "batch_6287485f-50fc-4efa-bcc5-b86690037f43",
+      "in_progress_at": 1729016126,
+      "input_file_id": "file-686746fcb6bc47f495250191ffa8a28e",
+      "errors": null,
+      "metadata": null,
+      "object": "batch",
+      "output_file_id": "file-04399828-ae0b-4825-9b49-8976778918cb",
+      "request_counts": {
+        "total": 3,
+        "completed": 2,
+        "failed": 1
+      },
+      "status": "completed",
+      "endpoint": "/chat/completions"
+    }
+  ],
+  "first_id": "batch_4ddc7b60-19a9-419b-8b93-b9a3274b33b5",
+  "has_more": false,
+  "last_id": "batch_6287485f-50fc-4efa-bcc5-b86690037f43"
+}
+```
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理に関するPythonドキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAIのバッチ処理に関するPython用のドキュメントを更新し、重要な情報を追加したものです。追加された内容は236行で、削除された行はわずか2行にとどまります。この更新により、APIの使用方法やバッチ処理の実装に関する具体的なコード例が豊富に提供されています。

特に、Azure Entra IDを使用して認証する方法や、APIキーを用いた接続方法のコード例が含まれており、ユーザーは具体的な実装方法を手に入れることができます。また、新たにバッチ処理を行う際のパフォーマンス向上のための推奨事項が追加され、ユーザーが効率的にバッチファイルを処理するためのガイダンスが強化されています。

このように、ドキュメントは使用者がAzure OpenAIのバッチ機能を効果的に利用するために必要な情報を見つけやすく、わかりやすく提供しています。更新された内容は、ドキュメントを訪れる開発者やデータサイエンティストにとって、特に実用的なリソースとなるでしょう。

## articles/ai-services/openai/includes/batch/batch-rest.md{#item-bcccd9}

<details>
<summary>Diff</summary>
````diff
@@ -52,6 +52,9 @@ The `custom_id` is required to allow you to identify which individual batch requ
 
 > [!IMPORTANT]
 > The `model` attribute must be set to match the name of the Global Batch deployment you wish to target for inference responses. The **same Global Batch model deployment name must be present on each line of the batch file.** If you want to target a different deployment you must do so in a separate batch file/job.
+>
+> For the best performance we recommend submitting large files for batch processing, rather than a large number of small files with only a few lines in each file.
+
 
 ### Create input file
 
@@ -64,7 +67,7 @@ Once your input file is prepared, you first need to upload the file to then be a
 [!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 ```http
-curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files?api-version=2024-07-01-preview \
+curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files?api-version=2024-10-01-preview \
   -H "Content-Type: multipart/form-data" \
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -F "purpose=batch" \
@@ -94,7 +97,7 @@ The above code assumes a particular file path for your test.jsonl file. Adjust t
 Depending on the size of your upload file it might take some time before it's fully uploaded and processed. To check on your file upload status run:
 
 ```http
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{file-id}?api-version=2024-07-01-preview \
+curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{file-id}?api-version=2024-10-01-preview \
   -H "api-key: $AZURE_OPENAI_API_KEY"
 ```
 
@@ -118,7 +121,7 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{file-id}?api-vers
 Once your file has uploaded successfully by reaching a status of `processed` you can submit the file for batch processing.
 
 ```http
-curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024-07-01-preview \
+curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024-10-01-preview \
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -H "Content-Type: application/json" \
   -d '{
@@ -168,7 +171,7 @@ curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-vers
 Once you have created batch job successfully you can monitor its progress either in the Studio or programatically. When checking batch job progress we recommend waiting at least 60 seconds in between each status call.
 
 ```http
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches/{batch_id}?api-version=2024-07-01-preview \
+curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches/{batch_id}?api-version=2024-10-01-preview \
   -H "api-key: $AZURE_OPENAI_API_KEY" 
 ```
 
@@ -220,7 +223,7 @@ The following status values are possible:
 ## Retrieve batch job output file
 
 ```http
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{output_file_id}/content?api-version=2024-07-01-preview \
+curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{output_file_id}/content?api-version=2024-10-01-preview \
   -H "api-key: $AZURE_OPENAI_API_KEY"  > batch_output.jsonl
 ```
 
@@ -231,7 +234,7 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{output_file_id}/c
 Cancels an in-progress batch. The batch will be in status `cancelling` for up to 10 minutes, before changing to `cancelled`, where it will have partial results (if any) available in the output file.
 
 ```http
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches/{batch_id}/cancel?api-version=2024-07-01-preview \
+curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches/{batch_id}/cancel?api-version=2024-10-01-preview \
   -H "api-key: $AZURE_OPENAI_API_KEY" 
 ```
 
@@ -240,6 +243,18 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches/{batch_id}/cance
 List all existing batch jobs for a given Azure OpenAI resource.
 
 ```http
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024-07-01-preview \
+curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024-10-01-preview \
   -H "api-key: $AZURE_OPENAI_API_KEY" 
 ```
+
+### List batch (Preview)
+
+Use the REST API to list all batch jobs with additional sorting/filtering options.
+
+```http
+curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024-10-01-preview \
+  -H "api-key: $AZURE_OPENAI_API_KEY" \
+  -H "filter: 'created_at gt 1728773533 and created_at lt 1729032733 and status eq 'Completed''" \
+  -H "orderby: created_at asc"
+
+```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIによるバッチ処理のドキュメント更新"
}
```

### Explanation
この変更は、Azure OpenAIのREST APIを使用したバッチ処理に関するドキュメントを更新し、重要な情報を追加したものです。変更には22行の追加と7行の削除が含まれ、全体で29行の内容が変更されています。このアップデートによって、バージョン情報が新しいAPIバージョンに更新され、ユーザーには最新のAPIの使用方法が提供されています。

特に、重要な注意点として、バッチ処理の際には大きなファイルを使用することが推奨されていることが記載され、ユーザーが処理効率を最適化できるようアドバイスが加えられています。また、新たにバッチ処理ジョブをリスト表示する機能が追加され、ユーザーが特定の条件でバッチジョブをフィルタリングできる方法や、ソートオプションの提供が説明されています。

これにより、ユーザーはバッチ処理のジョブをより効率的に管理できるようになり、APIを利用する上での理解を深めることができます。最新の情報を反映したこのドキュメントは、開発者やデータサイエンティストがAzure OpenAIサービスを利用する際の重要なリソースとして機能します。

## articles/ai-services/openai/includes/batch/batch-studio.md{#item-d4822e}

<details>
<summary>Diff</summary>
````diff
@@ -52,6 +52,8 @@ The `custom_id` is required to allow you to identify which individual batch requ
 
 > [!IMPORTANT]
 > The `model` attribute must be set to match the name of the Global Batch deployment you wish to target for inference responses. The **same Global Batch model deployment name must be present on each line of the batch file.** If you want to target a different deployment you must do so in a separate batch file/job.
+>
+> For the best performance we recommend submitting large files for batch processing, rather than a large number of small files with only a few lines in each file.
 
 ### Create input file
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチスタジオに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAIのバッチスタジオに関するドキュメントを更新し、重要な提言を追加したものです。具体的には、ファイルの中に新たに2行が追加され、バッチ処理のパフォーマンスに関する推奨事項が明記されました。

追加された内容では、バッチ処理の際に少数の大きなファイルを送信することが推奨されており、複数の小さなファイルを使用することは避けるべきであるとしています。これは、処理効率や性能を向上させるための重要な指針を提供しており、ユーザーにとって有益な情報となります。

この更新により、利用者はバッチ処理を行う際に最適なファイル管理方法を理解し、より効率的にリソースを活用できるようになります。全体として、この変更は開発者やデータサイエンティストがAzure OpenAIサービスを利用する際の重要な参考となるでしょう。

## articles/ai-services/openai/includes/global-batch-limits.md{#item-73207b}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Azure OpenAI model global batch limits
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 07/22/2024
+ms.date: 10/14/2024
 ---
 
 ## Global batch limits
@@ -22,10 +22,10 @@ The table shows the batch quota limit. Quota values for global batch are represe
 
 |Model|Enterprise agreement|Default| Monthly credit card based subscriptions | MSDN subscriptions | Azure for Students, Free Trials |
 |---|---|---|---|---|---|
-| `gpt-4o` | 5 B | 50 M | 1.35 M | 90 K | N/A|
-| `gpt-4o-mini` | 5 B | 50 M | 1.35 M | 90 K | N/A |
-| `gpt-4-turbo` | 300 M | 40 M | 1.35 M | 90 K | N/A |
-| `gpt-4` | 150 M | 5 M | 200 K | 100 K | N/A |
-| `gpt-35-turbo` | 10 B | 100 M | 5 M | 2 M | 50 K |
+| `gpt-4o` | 5 B | 200 M | 50 M | 90 K | N/A|
+| `gpt-4o-mini` | 15 B | 1 B | 50 M | 90 K | N/A |
+| `gpt-4-turbo` | 300 M | 80 M | 40 M | 90 K | N/A |
+| `gpt-4` | 150 M | 30 M | 5 M | 100 K | N/A |
+| `gpt-35-turbo` | 10 B | 1 B | 100 M | 2 M | 50 K |
 
 B = billion | M = million | K = thousand
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルバッチ制限に関するドキュメント改訂"
}
```

### Explanation
この変更は、Azure OpenAIのグローバルバッチ制限に関するドキュメントを更新したもので、全体で12行が変更され、その中で6行が追加され、6行が削除されています。特に、モデルのバッチクォータ制限が改訂されており、いくつかのモデルに関する制限値が見直されています。

具体的には、各モデルに対するエンタープライズ契約、デフォルト、月額クレジットカードベースのサブスクリプション、MSDNサブスクリプション、学生向けや無料トライアルのサブスクリプションにおける新しい制限値が示されています。この変更により、特定のモデルに対するリソースの上限や利用可能な制限がより明確になります。

例えば、`gpt-4o-mini`の制限が15Bに引き上げられ、以前の50Mから変更されています。また、`gpt-4-turbo`のデフォルト制限も80Mに変更されるなど、ユーザーが期待される利用状況に基づいて見直されました。

このアップデートは、利用者がAzure OpenAIのモデルを適切に活用し、リソース管理の計画を立てる際に役立つ情報を提供します。また、特定の条件下での効率的なリソース利用を促すことを目的としています。

## articles/ai-services/openai/includes/model-matrix/quota.md{#item-389aa1}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.date: 10/04/2024
 | australiaeast      | -         | -     | 40 K    | 80 K        | 80 K          | 30 K            | -        | -             | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | brazilsouth        | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | canadaeast         | -         | -     | 40 K    | 80 K        | 80 K          | -               | -        | -             | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| eastus             | 1 M       | 600 K | -       | -           | 80 K          | -               | 1 M      | 2 M           | 240 K          | 240 K                   | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 240 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| eastus             | 1 M       | 600 K | -       | -           | 80 K          | -               | 1 M      | 2 M           | 240 K          | 240 K                   | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 15 B                          | 150 M                  | 300 M                        | 10 B                          | 240 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | eastus2            | 1 M       | 600 K | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | 250 K               | -                        | -                  | -             | -                        | -             | -                        | 250 K                     | 250 K                          | 250 K                          |
 | francecentral      | -         | -     | 20 K    | 60 K        | 80 K          | -               | -        | -             | 240 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | germanywestcentral | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
@@ -27,10 +27,10 @@ ms.date: 10/04/2024
 | southcentralus     | 1 M       | 600 K | -       | -           | 80 K          | -               | 1 M      | 2 M           | 240 K          | -                       | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | southindia         | -         | -     | -       | -           | 150 K         | -               | -        | -             | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | spaincentral       | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| swedencentral      | 1 M       | 600 K | 40 K    | 80 K        | 150 K         | 30 K            | 1 M      | 2 M           | 300 K          | 240 K                   | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | 350 K                    | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
+| swedencentral      | 1 M       | 600 K | 40 K    | 80 K        | 150 K         | 30 K            | 1 M      | 2 M           | 300 K          | 240 K                   | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 15 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | 350 K                    | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
 | switzerlandnorth   | -         | -     | 40 K    | 80 K        | -             | 30 K            | -        | -             | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | switzerlandwest    | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | -                         | -                              | -                              | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | 250 K                    | -             | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
 | uksouth            | -         | -     | -       | -           | 80 K          | -               | -        | -             | 240 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | westeurope         | -         | -     | -       | -           | -             | -               | -        | -             | 240 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| westus             | 1 M       | 600 K | -       | -           | 80 K          | 30 K            | 1 M      | 2 M           | 300 K          | -                       | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| westus             | 1 M       | 600 K | -       | -           | 80 K          | 30 K            | 1 M      | 2 M           | 300 K          | -                       | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 15 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | westus3            | 1 M       | 600 K | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルクォータに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAIのモデルクォータに関するドキュメントを更新したものであり、変更された内容は合計で6行です。具体的には、モデルごとのバッチクォータ制限値が見直され、いくつかのモデルの制限が増加しています。

主な変更点としては、`eastus`、`swedencentral`、`westus`などの地理的リージョンにおいて、特定のモデルに対するバッチ制限が引き上げられています。例えば、`eastus`の条件で、以前は5Bだったバッチ制限が15Bに増加しており、`swedencentral`と`westus`でも同様に制限が引き上げられています。

これにより、ユーザーはより大きなデータセットをバッチ処理できるようになり、効率的なリソース使用が促進されます。また、これらの制限の変更は、特に大規模なプロジェクトや高負荷のアプリケーションにおいて、利用者にとって重要な情報となります。

このアップデートは、モデルの利用計画や実行の際に役立つ情報を提供し、クォータの理解を深めることで、リソースの最適な管理をサポートします。全体として、この変更はAzure OpenAIサービスを利用する開発者やデータ専門家にとって、貴重なリソースです。

## articles/ai-services/openai/media/how-to/global-batch/global-batch.png{#item-6fbc0c}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルバッチに関する画像の更新"
}
```

### Explanation
この変更は、グローバルバッチに関するメディアファイルである画像`global-batch.png`に関するものですが、相違点はありません。具体的には、追加や削除は行われておらず、変更された行数も0です。これは、画像自体の内容やファイルの構造に対して物理的な変更がなかったことを示しています。

このような修正が行われる理由としては、画像のメタデータの更新や適切な参照のための調整、またはファイルへのリンク等の非表示の変更が考えられます。しかし、具体的な内容の変更はないため、画像についてのユーザーへの直接的な影響はありません。

このファイルは、Azure OpenAIサービスの文脈において情報を視覚的に伝える役割を果たしているため、関連するコンテンツが更新された際に、適切にリンクされた状態を保つことが重要です。ユーザーは、今後関連する情報を読み進める際に、この画像が必要であることを意識し続けることが期待されます。

## articles/ai-services/openai/reference-preview.md{#item-e197a2}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's latest preview REST API. In this ar
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 09/09/2024
+ms.date: 10/16/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -20,7 +20,7 @@ This article provides details on the inference REST API endpoints for Azure Open
 
 ## Data plane inference
 
-The rest of the article covers the latest preview release of the Azure OpenAI data plane inference specification, `2024-09-01-preview`. This article includes documentation for the latest preview capabilities like assistants, threads, and vector stores.
+The rest of the article covers the latest preview release of the Azure OpenAI data plane inference specification, `2024-10-01-preview`. This article includes documentation for the latest preview capabilities like assistants, threads, and vector stores.
 
 If you're looking for documentation on the latest GA API release, refer to the [latest GA data plane inference API](./reference.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIのリファレンスプレビューの更新"
}
```

### Explanation
この変更は、Azure OpenAIのリファレンスプレビューに関連するドキュメント`reference-preview.md`の更新を示しています。具体的には、文書内のいくつかのメタデータと内容が調整されています。

主な変更点として、`ms.date`が`2024-09-09`から`2024-10-16`に更新されており、これはドキュメントの更新日を反映しています。また、データプラン推論仕様のバージョンも、 `2024-09-01-preview`から`2024-10-01-preview`に変更されています。これにより、最新のプレビュー機能が文書に反映されていることが伝えられています。

これらの更新は、ユーザーに最新のAPI仕様を提供し、Azure OpenAIサービスを利用する際の参照を容易にするために重要です。ドキュメント内容の正確な更新は、開発者が新機能や改善された機能を利用する際に不可欠であり、この情報は最新の技術動向を追う助けとなります。ユーザーは、この文書を参考にして最新の機能を効果的に活用できるようになります。


