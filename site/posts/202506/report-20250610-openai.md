---
date: '2025-06-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:35b42f4...MicrosoftDocs:4e306c3
summary: |-
  この報告は、DALL-E 3の画像編集APIにおける変更点についてまとめています。新機能として、必須パラメータ`deployment-id`が追加されました。また、互換性に影響のある変更として、画像入力が最大20MBに制限され、形式はPNGまたはJPGに限定されました。その他、APIのバージョンが`2025-04-01-preview`に更新され、エンドポイントのURLやリクエストパラメータの見直しが行われました。

  この更新は、ユーザーがDALL-E APIを円滑に利用できるように、画像のサイズや形式に関する具体的なガイドラインを提供します。デプロイメントの識別を可能にする`deployment-id`の追加により、APIの運用がより効率的になります。改訂されたドキュメントは、これらの新仕様に基づく運用を支援し、DALL-E 3の信頼性を高める要素となることが期待されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:35b42f4...MicrosoftDocs:4e306c3){target="_blank"}

# ハイライト

## 新機能
- DALL-E 3の画像編集APIにおいて、新たな必須パラメータ`deployment-id`が追加された。

## 互換性に影響のある変更
- 画像入力に関して、サイズが最大20MBに制限され、形式はPNGまたはJPGでなければならないと明示された。

## その他の更新
- APIバージョンが`2025-04-01-preview`に更新され、エンドポイントのURLおよびリクエストパラメータが見直された。
- APIドキュメントにおいて、エンドポイント構造やリクエストヘッダー、レスポンスの具体的な詳細が更新された。

# インサイト

このコード更新は、DALL-E 3の画像編集APIの利用における具体的なガイドラインを提供することを目的としています。特に、入力する画像のサイズと形式に関する制限が明文化され、利用者に対して誤りのない正確な情報を提供しています。これにより、ユーザーがDALL-E APIを使用する際の混乱を軽減し、正しいファイル形式やサイズの画像を用いることを促します。

さらに、エンドポイントやパラメータの見直しは、将来的なサービスの拡張やアプリケーション連携の効率化を見据えたものであると言えます。特に、新たに追加された`deployment-id`は、デプロイメントの識別を可能にし、より細かい管理を可能にするものです。このような変化は、開発者がAPIをより効果的に利用し、サービスの柔軟性と拡張性を向上させるものと考えられます。

改訂されたドキュメントは、APIの新仕様に基づく運用を円滑に進めるために重要な役割を果たすことが期待され、開発者や利用者にとって直接的な恩恵があります。こうした更新により、DALL-E 3はより具体的で信頼性の高いAI画像編集プラットフォームとしての地位を強固にするでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [dall-e.md](#item-ac9616) | minor update | DALL-E APIの画像入力制限についての更新 | modified | 2 | 1 | 3 | 
| [new-inference-preview.md](#item-bd665f) | minor update | 画像編集APIエンドポイントとパラメータの更新 | modified | 14 | 13 | 27 | 


# Modified Contents
## articles/ai-services/openai/how-to/dall-e.md{#item-ac9616}

<details>
<summary>Diff</summary>
````diff
@@ -239,7 +239,8 @@ The format in which DALL-E 3 generated images are returned. Must be one of `url`
 
 The Image Edit API allows you to modify existing images based on text prompts you provide. The API call is similar to the image generation API call, but you also need to provide an input image (base64-encoded image data).
 
-
+> [!IMPORTANT]
+> The input image must be less than 20 MB in size and must be a PNG or JPG file.
 
 #### [GPT-image-1](#tab/gpt-image-1)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL-E APIの画像入力制限についての更新"
}
```

### Explanation
この変更では、DALL-E 3の画像編集APIに関するドキュメントが更新されました。具体的には、入力画像のサイズおよび形式に関する重要な注意事項が追加されました。変更内容は、入力画像の最大サイズが20MBであり、PNGまたはJPGファイルでなければならないという点を明示しています。この情報は、利用者がDALL-E APIを使用する際の注意を促すものであり、より明確なガイドラインを提供することを目的としています。変更によって文書はより分かりやすく、利用者が正しい形式の画像を使用する手助けになります。

## articles/ai-services/openai/includes/api-versions/new-inference-preview.md{#item-bd665f}

<details>
<summary>Diff</summary>
````diff
@@ -634,20 +634,21 @@ Status Code: 200
 }
 ```
 
-## Create image edit
+## Image generations - Edit
 
 ```HTTP
-POST {endpoint}/openai/v1/images/edits?api-version=preview
+POST https://{endpoint}/openai/deployments/{deployment-id}/images/edits?api-version=2025-04-01-preview
 ```
 
-
+Edits an image from a text caption on a given gpt-image-1 model deployment
 
 ### URI Parameters
 
 | Name | In | Required | Type | Description |
 |------|------|----------|------|-----------|
 | endpoint | path | Yes | string<br>url | Supported Azure OpenAI endpoints (protocol and hostname, for example: `https://aoairesource.openai.azure.com`. Replace "aoairesource" with your Azure OpenAI resource name). https://{your-resource-name}.openai.azure.com |
-| api-version | query | No |  | The explicit Azure AI Foundry Models API version to use for this request.<br>`latest` if not otherwise specified. |
+| deployment-id | path | Yes | string |  |
+| api-version | query | Yes | string |  |
 
 ### Request Header
 
@@ -663,34 +664,34 @@ POST {endpoint}/openai/v1/images/edits?api-version=preview
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| background | enum | Allows to set transparency for the background of the generated image(s). <br>This parameter is only supported for `gpt-image-1`. Must be one of <br>`transparent`, `opaque` or `auto` (default value). When `auto` is used, the <br>model will automatically determine the best background for the image.<br><br>If `transparent`, the output format needs to support transparency, so it <br>should be set to either `png` (default value) or `webp`.<br>Possible values: `transparent`, `opaque`, `auto` | No |  |
-| image | string or array |  | Yes |  |
-| mask | string |  | No |  |
-| model | string | The model deployment to use for the image edit operation. | Yes |  |
-| n | integer | The number of images to generate. Must be between 1 and 10. | No | 1 |
-| prompt | string | A text description of the desired image(s). The maximum length is 1000 characters for `dall-e-2`, and 32000 characters for `gpt-image-1`. | Yes |  |
+| image | string or array | The image(s) to edit. Must be a supported image file or an array of images. Each image should be a png, or jpg file less than 25MB. | Yes |  |
+| mask | string | An additional image whose fully transparent areas (e.g., where alpha is zero) indicate where the image should be edited. If there are multiple images provided, the mask will be applied to the first image. Must be a valid PNG file, less than 4MB, and have the same dimensions as the image. | No |  |
+| n | integer | The number of images to generate. | No | 1 |
+| prompt | string | A text description of the desired image(s). The maximum length is 32000 characters. | Yes |  |
 | quality | enum | The quality of the image that will be generated. `high`, `medium` and `low` are only supported for `gpt-image-1`. `dall-e-2` only supports `standard` quality. Defaults to `auto`.<br>Possible values: `standard`, `low`, `medium`, `high`, `auto` | No |  |
 | response_format | enum | The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated. This parameter is only supported for `dall-e-2`, as `gpt-image-1` will always return base64-encoded images.<br>Possible values: `url`, `b64_json` | No |  |
 | size | enum | The size of the generated images. Must be one of `1024x1024`, `1536x1024` (landscape), `1024x1536` (portrait), or `auto` (default value) for `gpt-image-1`, and one of `256x256`, `512x512`, or `1024x1024` for `dall-e-2`.<br>Possible values: `256x256`, `512x512`, `1024x1024`, `1536x1024`, `1024x1536`, `auto` | No |  |
 | user | string | A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.  | No |  |
 
+
 ### Responses
 
 **Status Code:** 200
 
-**Description**: The request has succeeded. 
+**Description**: Ok 
 
 |**Content-Type**|**Type**|**Description**|
 |:---|:---|:---|
 |application/json | [AzureImagesResponse](#azureimagesresponse) | |
 
 **Status Code:** default
 
-**Description**: An unexpected error response. 
+**Description**: An error occurred. 
 
 |**Content-Type**|**Type**|**Description**|
 |:---|:---|:---|
-|application/json | [AzureErrorResponse](#azureerrorresponse) | |
+|application/json | [azureerrorresponse](#azureerrorresponse) | |
+
 
 ## Create image
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像編集APIエンドポイントとパラメータの更新"
}
```

### Explanation
この変更では、DALL-E 3の画像編集APIに関連するドキュメントが更新されました。主な改訂内容は、エンドポイントのURLおよびリクエストパラメータに関する詳細の見直しです。特に、APIのバージョンが`2025-04-01-preview`に更新され、画像編集に必要なパラメータの説明が強化され、新しい必須項目として`deployment-id`が追加されました。

具体的には、エンドポイントの構造が変更され、期待されるリクエストヘッダーやレスポンスの詳細も更新されました。また、画像ファイルのサイズ制限や形式についても具体的なガイドラインが記載され、ユーザーにとって理解しやすくなっています。このように、この更新は、ユーザーがAPIを効果的に利用できるようにするための重要な情報を提供しています。


