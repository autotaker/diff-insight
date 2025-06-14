---
date: '2025-06-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d0f373d...MicrosoftDocs:0496181
summary: 本変更では、特定のAIサービス関連のドキュメントがマイナーアップデートされ、情報の精度や実用性が向上しました。主にDALL-E REST APIに新しいモデルが追加され、プロビジョニングスループットのドキュメントも更新されました。これにより、ユーザーはより適切なサービス情報を得られ、開発者は新たな画像生成アプリケーションを作成しやすくなります。全体として、これらの改善はAzure
  OpenAIサービスを使用するユーザーにとって、より価値のある体験を提供することを目指しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d0f373d...MicrosoftDocs:0496181){target="_blank"}

# ハイライト

本変更では、特定のAIサービス関連のドキュメントがマイナーアップデートされ、情報の精度や実用性が向上しました。特に、プロビジョニングスループットのオンボーディングとロールベースのアクセス制御、そしてDALL-E REST APIに関する情報が更新されました。

## 新機能
- DALL-E REST API に新しいモデル「dalle3」および「gpt-image-1」が追加され、Pythonスクリプトを使った具体的な使用例が提供されています。

## 重大な変更点
- 特に重大な変更はありませんが、情報の精度向上を目的とした変更が行われました。

## その他の更新
- プロビジョニングスループットに関する日付の変更とレイテンシターゲット値の説明が明確化されました。
- 「ms.service」が「azure-ai-language」から「azure-ai-openai」に修正され、サービス名の正確さが向上しました。

# 洞察

このコード差分は、Azureに関するAIドキュメントのユーザー体験を向上させるための一連の小規模な変更を示しています。まず、プロビジョニングスループットのオンボーディングに関するドキュメントの更新では、レイテンシターゲット値の説明が改良されており、利用者が性能要件をより明確に理解できるようになっています。これはクラウドサービスのコストと性能を管理する企業にとって重要です。

次に、ロールベースのアクセス制御のドキュメントでは、`ms.service`の修正が行われました。これにより、ユーザーがドキュメントを通じて正確なサービス情報にアクセスできるようになり、混乱を避けることができます。このような小さな整合性の改善は、ドキュメントの信頼性を高め、ユーザーによる適切なリソース管理を支援します。

最後に、DALL-E REST APIの更新では、新しいモデルを用いた画像生成と編集の例が追加され、特にPythonを用いた実践的なガイドが提供されました。これにより、開発者はAzure OpenAIの機能を利用して、より高度な画像生成アプリケーションを開発できるようになり、イノベーションを加速させることが可能になります。加えて、有害な内容の生成を防ぐ説明が含まれており、安全な使用が促進されています。

全体として、これらの改善はAzure OpenAIサービスを用いるユーザーにとって、より豊かで価値のある体験を提供することを目的としています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | プロビジョニングスループットのオンボーディングに関する更新 | modified | 3 | 2 | 5 | 
| [role-based-access-control.md](#item-4b9817) | minor update | ロールベースのアクセス制御に関するサービス情報の更新 | modified | 1 | 1 | 2 | 
| [dall-e-rest.md](#item-4bac64) | minor update | DALL-E REST API に関するガイドラインの更新 | modified | 96 | 2 | 98 | 


# Modified Contents
## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title:  Understanding costs associated with provisioned throughput units (PTU)
 description: Learn about provisioned throughput costs and billing in Azure AI Foundry. 
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 05/28/2025
+ms.date: 06/13/2025
 manager: nitinme
 author: aahill 
 ms.author: aahi 
@@ -84,8 +84,9 @@ For example, for `gpt-4.1:2025-04-14`, 1 output token counts as 4 input tokens t
 |Regional provisioned minimum deployment|25| 50|25| 25 |50 | 25|25|50|25| NA|NA|
 |Regional provisioned scale increment|25| 50|25| 25 | 50 | 25|50|50|25|NA|NA|
 |Input TPM per PTU|5,400 | 3,000|14,900| 59,400 | 600 | 2,500|230|2,500|37,000|4,000|4,000|
-|Latency Target Value| 66 Tokens Per Second | 40 Tokens Per Second|50 Tokens Per Second| 60 Tokens Per Second | 40 Tokens Per Second | 66 Tokens Per Second |25 Tokens Per Second|25 Tokens Per Second|33 Tokens Per Second|50 Tokens Per Second|50 Tokens Per Second|
+|Latency Target Value| 99% > 66 Tokens Per Second\* | 99% > 40 Tokens Per Second\* | 99% > 50 Tokens Per Second\*| 99% > 60 Tokens Per Second\* | 99% > 40 Tokens Per Second\* | 99% > 66 Tokens Per Second\* | 99% > 25 Tokens Per Second\* | 99% > 25 Tokens Per Second\* | 99% > 33 Tokens Per Second\* | 99% > 50 Tokens Per Second\*| 99% > 50 Tokens Per Second\*|
 
+\* Calculated as the average request latency on a per-minute basis across the month.
 
 For a full list, see the [Azure AI Foundry calculator](https://ai.azure.com/resource/calculator).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングスループットのオンボーディングに関する更新"
}
```

### Explanation
この変更では、ドキュメント「プロビジョニングスループットのオンボーディング」に関する情報が更新されました。主な変更点は、日付が「2025年5月28日」から「2025年6月13日」へと変更されたことです。また、レイテンシターゲット値の説明が強化され、「99%以上のトークンパーセカンド」が追加され、計算方法に関する注釈が付け加えられました。これにより、利用者がスループットに関連するコストや性能要件をより明確に理解できるようになっています。全体として、文書の精度と情報の更新が行われ、利用者への有用性が向上しました。

## articles/ai-services/openai/how-to/role-based-access-control.md{#item-4b9817}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Role-based access control for Azure OpenAI
 description: Learn how to use Azure RBAC for managing individual access to Azure OpenAI resources.
 author: mrbullwinkle
 manager: nitinme
-ms.service: azure-ai-language
+ms.service: azure-ai-openai
 ms.topic: how-to
 ms.date: 02/24/2025
 ms.author: mbullwin
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ロールベースのアクセス制御に関するサービス情報の更新"
}
```

### Explanation
この変更では、Azure OpenAIに関する「ロールベースのアクセス制御」のドキュメントが更新され、サービス情報が修正されました。具体的には、`ms.service`の値が「azure-ai-language」から「azure-ai-openai」に変更されました。この更新により、ドキュメントが対象とするサービスがより正確に反映され、ユーザーへの情報提供が向上しています。また、全体的な説明や指示は変更されていませんが、正確なサービス名への変更は、関連するリソース管理の理解を助けるものとなります。

## articles/ai-services/openai/includes/dall-e-rest.md{#item-4bac64}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ Use this guide to get started calling the Azure OpenAI in Azure AI Foundry Model
 - <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>.
 - The following Python libraries installed: `os`, `requests`, `json`.
 - An Azure OpenAI resource created in a supported region. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
-- Then, you need to deploy a `dalle3` model with your Azure resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- Then, you need to deploy a `gpt-image-1` or `dalle3` model with your Azure resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 ## Setup 
 
@@ -41,6 +41,98 @@ Go to your resource in the Azure portal. On the navigation pane, select **Keys a
 
 Create a new Python file named _quickstart.py_. Open the new file in your preferred editor or IDE.
 
+#### [GPT-image-1](#tab/gpt-image-1)
+
+1. Replace the contents of _quickstart.py_ with the following code. Change the value of `prompt` to your preferred text. Also set `deployment` to the deployment name you chose when you deployed the GPT-image-1 model.
+    
+    ```python
+    import os
+    import requests
+    import base64
+    from PIL import Image
+    from io import BytesIO
+    
+    # set environment variables
+    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
+    subscription_key = os.getenv("AZURE_OPENAI_API_KEY")
+    
+    deployment = "gpt-image-1" # the name of your GPT-image-1 deployment
+    api_version = "2025-04-01-preview" # or later version
+    
+    def decode_and_save_image(b64_data, output_filename):
+      image = Image.open(BytesIO(base64.b64decode(b64_data)))
+      image.show()
+      image.save(output_filename)
+    
+    def save_all_images_from_response(response_data, filename_prefix):
+      for idx, item in enumerate(response_data['data']):
+        b64_img = item['b64_json']
+        filename = f"{filename_prefix}_{idx+1}.png"
+        decode_and_save_image(b64_img, filename)
+        print(f"Image saved to: '{filename}'")
+    
+    base_path = f'openai/deployments/{deployment}/images'
+    params = f'?api-version={api_version}'
+    
+    generation_url = f"{endpoint}{base_path}/generations{params}"
+    generation_body = {
+      "prompt": "girl falling asleep",
+      "n": 1,
+      "size": "1024x1024",
+      "quality": "medium",
+      "output_format": "png"
+    }
+    generation_response = requests.post(
+      generation_url,
+      headers={
+        'Api-Key': subscription_key,
+        'Content-Type': 'application/json',
+      },
+      json=generation_body
+    ).json()
+    save_all_images_from_response(generation_response, "generated_image")
+    
+    # In addition to generating images, you can edit them.
+    edit_url = f"{endpoint}{base_path}/edits{params}"
+    edit_body = {
+      "prompt": "girl falling asleep",
+      "n": 1,
+      "size": "1024x1024",
+      "quality": "medium"
+    }
+    files = {
+      "image": ("generated_image_1.png", open("generated_image_1.png", "rb"), "image/png"),
+      # You can use a mask to specify which parts of the image you want to edit.
+      # The mask must be the same size as the input image.
+      # "mask": ("mask.png", open("mask.png", "rb"), "image/png"),
+    }
+    edit_response = requests.post(
+      edit_url,
+      headers={'Api-Key': subscription_key},
+      data=edit_body,
+      files=files
+    ).json()
+    save_all_images_from_response(edit_response, "edited_image")
+    ```
+
+    The script makes a synchronous image generation API call.
+
+    > [!IMPORTANT]
+    > Remember to remove the key from your code when you're done, and never post your key publicly. For production, use a secure way of storing and accessing your credentials. For more information, see [Azure Key Vault](/azure/key-vault/general/overview).
+
+1. Run the application with the `python` command:
+
+    ```console
+    python quickstart.py
+    ```
+
+    Wait a few moments to get the response.
+
+
+
+#### [DALL-E](#tab/dall-e-3)
+
+
 1. Replace the contents of _quickstart.py_ with the following code. Change the value of `prompt` to your preferred text.
 
     You also need to replace `<dalle3>` in the URL with the deployment name you chose when you deployed the DALL-E 3 model. Entering the model name will result in an error unless you chose a deployment name that is identical to the underlying model name. If you encounter an error, double check to make sure that you don't have a doubling of the `/` at the separation between your endpoint and `/openai/deployments`.
@@ -83,6 +175,8 @@ Create a new Python file named _quickstart.py_. Open the new file in your prefer
 
     Wait a few moments to get the response.
 
+---
+
 ## Output
 
 The output from a successful image generation API call looks like the following example. The `url` field contains a URL where you can download the generated image. The URL stays active for 24 hours.
@@ -99,7 +193,7 @@ The output from a successful image generation API call looks like the following
 } 
 ```
 
-The Image APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it doesn't generate an image. For more information, see [Content filtering](../concepts/content-filter.md). For examples of error responses, see the [DALL-E how-to guide](../how-to/dall-e.md).
+The Image APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it doesn't generate an image. For more information, see [Content filtering](../concepts/content-filter.md). For examples of error responses, see the [Image generation how-to guide](../how-to/dall-e.md).
 
 The system returns an operation status of `Failed` and the `error.code` value in the message is set to `contentFilter`. Here's an example:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL-E REST API に関するガイドラインの更新"
}
```

### Explanation
この変更では、DALL-E REST APIに関するドキュメントが大幅に更新されました。主な変更点として、デプロイするモデルに「dalle3」が追加され、さらに新しいモデル「gpt-image-1」についての具体的な使用方法が紹介されています。特に、Pythonスクリプトの例が追加され、画像生成のためのAPI呼び出しや編集の方法が詳しく説明されています。

具体的には、ユーザーは新しい機能を利用して、テキストプロンプトに基づいた画像を生成したり、既存の画像を編集したりすることができるようになっています。また、生成した画像の処理や保存に関する手順も含まれており、実用的な情報が充実しています。さらに、内容モデレーションフィルターについての説明も更新され、内容が有害な場合には画像が生成されないことが明記されています。

全体として、ユーザーがAzure OpenAIをより効果的に利用できるよう、ドキュメントが具体的かつ実践的な情報で強化されました。


