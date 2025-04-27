---
date: '2025-04-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8f8bd66...MicrosoftDocs:0b33f02
summary: Azure GovernmentにおけるAIモデルおよびOpenAI APIの画像生成機能に関するドキュメントが更新され、新機能の追加や既存機能の説明が明確化されました。新たに「o3-mini
  USGov DataZone」がAIサービスの展開情報に追加され、OpenAI APIには「background」や「compression_level」といった新しいパラメータが導入されました。これにより、ユーザーはよりカスタマイズされた画像生成が可能になります。また、既存のパラメータに関する説明も整理され、開発者が必要な情報に迅速にアクセスできるよう改善されています。これらの更新は、AzureとOpenAIのサービスの利用促進とユーザーエクスペリエンスの向上を目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8f8bd66...MicrosoftDocs:0b33f02){target="_blank"}

# ハイライト
Azure GovernmentにおけるAIモデルおよびOpenAI APIの画像生成機能に関するドキュメントが更新され、追加機能や既存機能に関する説明が明確化されました。

## 新機能
- 「o3-mini USGov DataZone」という新しい列がAzure GovernmentのAIサービスの展開情報に追加されました。
- OpenAI APIの画像生成機能に「background」や「compression_level」などの新しいパラメータが追加されました。

## 重大な変更
- 特にありませんが、重要情報の明確化および追加機能により、利用状況に影響を与える可能性があります。

## その他の更新
- USGov DataZoneのモデルアクセスに関する新しい注釈が追加されました。
- OpenAI API画像生成機能の既存パラメータにおける説明の整理と明確化が行われました。

# 洞察
このドキュメントの更新は、Azure GovernmentにおけるAIサービスの展開とOpenAI APIの画像生成機能を利用する開発者に向けて、さらなる情報の透明性と機能の明確化を図るものです。

まず、Azure GovernmentのAIモデルの展開情報に「o3-mini USGov DataZone」が導入されています。これにより、usgovarizonaとusgovvirginiaの両方からデータゾーンへアクセス可能であり、データの地域保持が強調されている点は、政府機関や堅牢なセキュリティが求められる業界にとって重要です。今後、これらのデータゾーンモデルが提供する利便性によって、Azure Governmentユーザーの柔軟性が向上すると考えられます。

さらに、OpenAI APIの画像生成機能の改善は、よりカスタマイズ可能で詳細な生成プロセスを可能にします。「background」や「compression_level」といった新しいフィールドの追加により、生成された画像の多様性が増し、異なるアプリケーションでの利用が促進されるでしょう。また、既存のパラメータについても使いやすく整理され、開発者が必要な情報を迅速に取得できるようになっています。

これらの更新は、ユーザーエクスペリエンスを強化し、ドキュメントを参照するユーザーにとって価値ある情報を提供するために行われたものであり、AzureとOpenAIのサービス利用者にとって、より便利で効率的なツールの利用を可能にします。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-government.md](#item-a47549) | minor update | Azure GovernmentにおけるAIモデルの展開情報の更新 | modified | 12 | 4 | 16 | 
| [latest-inference-preview.md](#item-24bf0f) | minor update | 画像生成APIのパラメータの拡張と詳細追加 | modified | 42 | 13 | 55 | 


# Modified Contents
## articles/ai-services/openai/azure-government.md{#item-a47549}

<details>
<summary>Diff</summary>
````diff
@@ -24,10 +24,18 @@ The following sections show model availability by region and deployment type. Mo
 <br>
 
 ## Standard deployment model availability
-|   **Region**  | **gpt-4o**, **2024-05-13** | **gpt-4o-mini**, **2024-07-18** | **gpt-4**, **1106-Preview** | **gpt-35-turbo**, **0125** | **gpt-35-turbo**, **1106** | **text-embedding-3-large**, **1** | **text-embedding-ada-002**, **2** |
-|:--------------|:--------------------------:|:-------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:---------------------------------:|:---------------------------------:|
-| usgovarizona  | ✅ | ✅ | ✅ | ✅ | -  | ✅ | ✅ |
-| usgovvirginia | ✅ | -  | ✅ | ✅ | ✅ |  - | ✅ |
+|   **Region**  | **o3-mini USGov DataZone** | **gpt-4o**, **2024-05-13** | **gpt-4o-mini**, **2024-07-18** | **gpt-4**, **1106-Preview** | **gpt-35-turbo**, **0125** | **gpt-35-turbo**, **1106** | **text-embedding-3-large**, **1** | **text-embedding-ada-002**, **2** |
+|:--------------|:--------------------------:|:--------------------------:|:-------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:---------------------------------:|:---------------------------------:|
+| usgovarizona  | ✅ | ✅ | ✅ | ✅ | ✅ | -  | ✅ | ✅ |
+| usgovvirginia | ✅ | ✅ | -  | ✅ | ✅ | ✅ |  - | ✅ |
+
+* USGov DataZone provides access to the model from both usgovarizona and usgovvirginia.
+* Data stored at rest remains in the designated Azure region of the resource.
+* Data may be processed for inferencing in either of the two Azure Government regions. 
+
+SKU name in code: DataZoneStandard
+
+Data zone standard deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. Data zone standard provides higher default quotas than our Azure geography-based deployment types.
 
 To request quota increases for these models, submit a request at [https://aka.ms/AOAIGovQuota](https://aka.ms/AOAIGovQuota). Note the following maximum quota limits allowed via that form:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure GovernmentにおけるAIモデルの展開情報の更新"
}
```

### Explanation
このコードの変更は、Azure GovernmentにおけるAIサービスのドキュメントに関するもので、主にモデルの展開状況に関する新しい情報が追加されています。具体的には、表のヘッダーに「o3-mini USGov DataZone」という新しい列が追加され、各地域の利用可能なモデルのリストが更新されました。また、新しい注釈が追加され、USGov DataZoneがusgovarizonaとusgovvirginia両方からモデルへのアクセスを提供し、データが指定されたAzureリソースの地域内に留まること、及び推論のためにどちらかの地域で処理される可能性があることが明記されています。

更新された箇所には、Data zone standard deploymentsがAzure OpenAIリソース内で利用可能であることや、各リクエストに対して最適な可用性を持つデータセンターにトラフィックを動的にルーティングできることに関する詳細が含まれています。これにより、ユーザーはAzure GovernmentのAIサービスの新しい展開モデルについてより深く理解できるようになります。

## articles/ai-services/openai/includes/api-versions/latest-inference-preview.md{#item-24bf0f}

<details>
<summary>Diff</summary>
````diff
@@ -1215,17 +1215,21 @@ Generates a batch of images from a text caption on a given DALL-E or GPT-image-1
 
 **Content-Type**: application/json
 
+
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
 | n | integer | The number of images to generate. | No | 1 |
 | prompt | string | A text description of the desired image(s). The maximum length is 4000 characters. | Yes |  |
 | quality | [imageQuality](#imagequality) | The quality of the image that will be generated. | No | standard (for DALL-E)</br>high (for GPT-image-1) |
 | response_format | [imagesResponseFormat](#imagesresponseformat) | The format in which the generated images are returned. | No | url |
 | size | [imageSize](#imagesize) | The size of the generated images. | No | 1024x1024 |
-| style | [imageStyle](#imagestyle) | The style of the generated images. | No | vivid |
+| style | [imageStyle](#imagestyle) | The style of the generated images. (DALL-E 3 only)| No | vivid |
 | user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse. | No |  |
-| output_format | string | The format in which the generated images are returned. GPT-image-1 models only. | No | PNG |
-| output_compression | integer | The compression level (on a scale of 0-100) of the generated images. GPT-image-1 | No | 0 |
+| output_format | [imageOutputFormat](#imageoutputformat) | The format in which the generated images are returned. (GPT-image-1 only) | No | PNG |
+| safety | [imageSafety](#imagesafety) | The safety setting of the image generation process. (GPT-image-1 only) | No | auto |
+ | No | auto |
+| background | [imageBackground](#imagebackground) | The desired appearance of the background of the image. (GPT-image-1 only) | No | auto |
+| compression_level | integer | The compression level (on a scale of 0-100) of the generated images. (GPT-image-1 only) | No | 0 |
 
 ### Responses
 
@@ -1355,6 +1359,7 @@ Generates an image based on an input image and text prompt instructions. Require
 
 **Content-Type**: application/json
 
+
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
 | image | file | The input image to edit. Must be a valid image URL or base64-encoded image. | Yes |  |
@@ -1364,10 +1369,8 @@ Generates an image based on an input image and text prompt instructions. Require
 | quality | string | The quality of the image that will be generated. Values are 'low', 'medium', 'high' | No | high |
 | response_format | [imagesResponseFormat](#imagesresponseformat) | The format in which the generated images are returned. | No | url |
 | size | [imageSize](#imagesize) | The size of the generated images. | No | 1024x1024 |
-| style | [imageStyle](#imagestyle) | The style of the generated images. | No | vivid |
 | user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse. | No |  |
 | output_format | [imageOutputFormat](#imageoutputformat) | The format in which the generated images are returned. | No | PNG |
-| output_compression | integer | The compression level (on a scale of 0-100) of the generated images. GPT-image-1 | No | 0 |
 
 
 ### Responses
@@ -6121,13 +6124,24 @@ Speech request.
 | speed | number | The speed of the synthesized audio. Select a value from `0.25` to `4.0`. `1.0` is the default. | No | 1.0 |
 | voice | enum | The voice to use for speech synthesis.<br>Possible values: `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer` | Yes |  |
 
+### imageBackground
+
+The desired appearance of the background of the image.
+
+| Property | Value |
+|----------|-------|
+| **Description** | The desired appearance of the background of the image. |
+| **Type** | string |
+| **Default** | auto |
+| **Values** | `transparent`</br>`opaque`</br>`auto`|
+
 ### imageOutputFormat
 
-The requested output format for the generated image.
+The format in which the generated images are returned.
 
 | Property | Value |
 |----------|-------|
-| **Description** | The requested output format for the generated image. |
+| **Description** | The format in which the generated images are returned. |
 | **Type** | string |
 | **Default** | PNG |
 | **Values** | `PNG`<br>`JPEG` |
@@ -6154,6 +6168,19 @@ The format in which the generated images are returned.
 | **Default** | url |
 | **Values** | `url`<br>`b64_json` |
 
+### imageSafety
+
+The safety setting of the image generation process.
+
+| Property | Value |
+|----------|-------|
+| **Description** | The safety setting of the image generation process. |
+| **Type** | string |
+| **Default** | auto |
+| **Values** | `strict`</br>`auto`|
+
+
+
 ### imageSize
 
 The size of the generated images.
@@ -6163,7 +6190,7 @@ The size of the generated images.
 | **Description** | The size of the generated images. |
 | **Type** | string |
 | **Default** | 1024x1024 |
-| **Values** | `256x256`<br>`512x512`<br>`1792x1024`<br>`1024x1792`<br>`1024x1024` |
+| **Values** | `256x256`, `512x512`, `1792x1024`, `1024x1792`, `1024x1024` (for DALL-E)</br>`1024x1024`, `1024x1536`, `1536x1024` (for GPT-image-1) |
 
 ### imageStyle
 
@@ -6185,10 +6212,13 @@ The style of the generated images.
 | quality | [imageQuality](#imagequality) | The quality of the image that will be generated. | No | standard (for DALL-E)</br>high (for GPT-image-1) |
 | response_format | [imagesResponseFormat](#imagesresponseformat) | The format in which the generated images are returned. | No | url |
 | size | [imageSize](#imagesize) | The size of the generated images. | No | 1024x1024 |
-| style | [imageStyle](#imagestyle) | The style of the generated images. | No | vivid |
+| style | [imageStyle](#imagestyle) | The style of the generated images. (DALL-E 3 only)| No | vivid |
 | user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse. | No |  |
-| output_format | string | The format in which the generated images are returned. GPT-image-1 models only. | No | PNG |
-| output_compression | integer | The compression level (on a scale of 0-100) of the generated images. GPT-image-1 | No | 0 |
+| output_format | [imageOutputFormat](#imageoutputformat) | The format in which the generated images are returned. (GPT-image-1 only) | No | PNG |
+| safety | [imageSafety](#imagesafety) | The safety setting of the image generation process. (GPT-image-1 only) | No | auto |
+ | No | auto |
+| background | [imageBackground](#imagebackground) | The desired appearance of the background of the image. (GPT-image-1 only) | No | auto |
+| compression_level | integer | The compression level (on a scale of 0-100) of the generated images. (GPT-image-1 only) | No | 0 |
 
 ### imageEditsRequest
 
@@ -6202,10 +6232,9 @@ The style of the generated images.
 | quality | string | The quality of the image that will be generated. Values are 'low', 'medium', 'high' | No | high |
 | response_format | [imagesResponseFormat](#imagesresponseformat) | The format in which the generated images are returned. | No | url |
 | size | [imageSize](#imagesize) | The size of the generated images. | No | 1024x1024 |
-| style | [imageStyle](#imagestyle) | The style of the generated images. | No | vivid |
 | user | string | A unique identifier representing your end-user, which can help to monitor and detect abuse. | No |  |
 | output_format | [imageOutputFormat](#imageoutputformat) | The format in which the generated images are returned. | No | PNG |
-| output_compression | integer | The compression level (on a scale of 0-100) of the generated images. GPT-image-1 | No | 0 |
+
 
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像生成APIのパラメータの拡張と詳細追加"
}
```

### Explanation
このコードの変更は、OpenAI APIの画像生成機能に関するドキュメントに対するもので、いくつかの新しいパラメータが追加され、既存のパラメータに対する説明が明確化されています。具体的には、画像生成の際のオプションとして、「background」や「compression_level」などの新しいフィールドが追加され、特にGPT-image-1モデルでの使用が強調されています。また、他のオプションについても、デフォルト値や使用可能な値が整理されています。

加えて、既存のパラメータである「style」や「output_format」も、モデルによって適用される条件が明記されています。これにより、開発者はAPIを通じて生成される画像の特性について、より詳細な情報を得ることができ、必要に応じて適切な設定を行えるようになることを目的としています。全体として、この更新により、APIの使いやすさと明確さが向上し、開発者がより効果的に利用できるようになっています。


