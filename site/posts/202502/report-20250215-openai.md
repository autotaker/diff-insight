---
date: '2025-02-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f2b9798...MicrosoftDocs:b07793e
summary: このコード変更では、OpenAI APIおよびDALL-Eモデルに関する文書が更新され、DALL-E 2に関連する情報が大幅に削除されました。今後はDALL-E
  3に焦点を当て、視覚機能を持つモデルやカスタムモデルの文書が修正・更新されています。新しい機能は追加されていませんが、ユーザーにとっての利用しやすさが向上しています。ユーザーはDALL-E
  2からDALL-E 3へ移行する必要があります。また、OpenAI APIバージョンの非推奨に関する文書も修正されています。全体として、技術の進化に応じた重要な更新であり、ユーザーの利便性を高めるためのものです。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f2b9798...MicrosoftDocs:b07793e){target="_blank"}

# ハイライト

このコード変更では、OpenAI APIおよびDALL-Eモデルに関する文書の更新と削除が行われています。具体的な新機能の追加はありませんが、DALL-E 2に関連する情報が大幅に削除され、DALL-E 3に焦点が当てられています。また、カスタムモデルや視覚機能を持つチャットモデルの文書が修正・更新されています。

## 新機能

特に新しい機能そのものが追加されたわけではありませんが、視覚機能を持つモデルのガイドが更新され、ユーザーにとっての利用しやすさが向上しています。

## 破壊的変更

- DALL-E 2に関する情報が大幅に削除され、DALL-E 3に関する記述のみが残されました。これにより、DALL-E 2に依存していたユーザーは、新しいバージョンに移行する必要があります。

## その他の更新

- OpenAI APIバージョンの非推奨に関する文書が修正され、一部モデル名が削除されました。
- 視覚機能を持つモデルやカスタムモデルに関連する文書のタイトルや内容が更新されました。

# インサイト

ドキュメントの今回の変更は、最新の技術仕様や利用方法にユーザーがスムーズに対応できるよう設計されています。特にDALL-Eモデルに関する情報の更新は、技術の進化に合わせた重要なステップです。DALL-E 2に関する情報が削除されたことは、OpenAIがDALL-E 3を推奨し、これに焦点を当てていることを示唆しています。これにより、ユーザーは最新の技術を活用するための情報にアクセスしやすくなり、過去のスペックによる混乱を避けることが可能となります。

視覚機能に関するクイックスタートガイドやカスタムモデルの説明が強化されたことは、新しい技術に興味を持つユーザーに対して、実践的な情報を提供することを目的としています。これらの文書の調整により、ユーザーは新機能のテストと導入を簡単に行えるようになり、学習曲線が緩和されるでしょう。

全体として、今回の文書更新は、技術の最新動向を取り入れたものであり、ユーザーの利便性を高めるために向けられたものです。新しいAPIやモデルへの移行を考慮し、ユーザーが適切にインフォームされ、準備が整うようにすることが適材されています。これにより、開発者やエンドユーザーは革新的なAI技術を活用するための基盤を強化することができます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [api-version-deprecation.md](#item-1cad50) | minor update | APIバージョン非推奨に関するドキュメントの更新 | modified | 1 | 1 | 2 | 
| [gpt-v-quickstart.md](#item-2a6183) | minor update | 視覚機能を備えたモデルのクイックスタートガイドのタイトル修正 | modified | 5 | 1 | 6 | 
| [dall-e.md](#item-ac9616) | breaking change | DALL-Eに関するドキュメントの大幅な削除 | modified | 0 | 156 | 156 | 
| [dall-e-python.md](#item-c91824) | breaking change | DALL-E 2に関する情報の削除 | modified | 0 | 75 | 75 | 
| [dall-e-rest.md](#item-4bac64) | breaking change | DALL-E 2に関する情報の大幅な削除 | modified | 1 | 127 | 128 | 
| [fine-tuning-studio.md](#item-439f1e) | minor update | カスタムモデルの使用に関する説明の修正 | modified | 1 | 1 | 2 | 
| [gpt-v-studio.md](#item-dcd50e) | minor update | 視覚機能を持つチャットに関するクイックスターションの更新 | modified | 62 | 12 | 74 | 


# Modified Contents
## articles/ai-services/openai/api-version-deprecation.md{#item-1cad50}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ This version contains support for the latest Azure OpenAI features including:
 - [Assistants API](./assistants-reference.md). [**Added in 2024-02-15-preview**]
 - [Text to speech](./text-to-speech-quickstart.md). [**Added in 2024-02-15-preview**]
 - [DALL-E 3](./dall-e-quickstart.md). [**Added in 2023-12-01-preview**]
-- [Fine-tuning](./how-to/fine-tuning.md) `gpt-35-turbo`, `babbage-002`, and `davinci-002` models.[**Added in 2023-10-01-preview**]
+- [Fine-tuning](./how-to/fine-tuning.md). [**Added in 2023-10-01-preview**]
 - [Whisper](./whisper-quickstart.md). [**Added in 2023-09-01-preview**]
 - [Function calling](./how-to/function-calling.md)  [**Added in 2023-07-01-preview**]
 - [Retrieval augmented generation with your data feature](./use-your-data-quickstart.md).  [**Added in 2023-06-01-preview**]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョン非推奨に関するドキュメントの更新"
}
```

### Explanation
この変更は、OpenAI APIのバージョン非推奨に関するドキュメントの一部を更新し、特定の機能のリストからモデル名を修正しています。具体的には、`gpt-35-turbo`、`babbage-002`、および`davinci-002`モデルの名前が削除され、文書の整合性を図るために内容が簡素化されました。これにより、ユーザーが最新の機能やAPIのサポートについての情報をより理解しやすくなるように改善されています。

## articles/ai-services/openai/gpt-v-quickstart.md{#item-2a6183}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Quickstart: Use vision-enabled models with the Azure OpenAI Service'
+title: 'Quickstart: Use vision-enabled chats with the Azure OpenAI Service'
 titleSuffix: Azure OpenAI
 description: Use this article to get started using Azure OpenAI to deploy and use the GPT-4 Turbo with Vision model or other vision-enabled models. 
 services: cognitive-services
@@ -22,6 +22,10 @@ Get started using GPT-4 Turbo with images with the Azure OpenAI Service.
 >
 > The latest vision-capable models are `gpt-4o` and `gpt-4o mini`. These models are in public preview. The latest available GA model is `gpt-4` version `turbo-2024-04-09`.
 
+> [!IMPORTANT]
+> Extra usage fees might apply when using chat completion models with vision functionality.
+
+
 ::: zone pivot="ai-foundry-portal"
 
 [!INCLUDE [Azure AI Foundry portal quickstart](includes/gpt-v-studio.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "視覚機能を備えたモデルのクイックスタートガイドのタイトル修正"
}
```

### Explanation
この変更は、Azure OpenAIサービスを使用した視覚機能を備えたモデルに関するクイックスタートガイドのタイトルを修正し、より具体的な内容を反映するようにしています。具体的には、タイトルが「視覚機能を備えたチャットを使用するクイックスタート」に更新され、ドキュメント全体が視覚機能を強調した内容になっています。また、視覚モデルを使用する際に追加の利用料金が発生する可能性についての警告が追加され、ユーザーへの重要な情報を提供する変更が行われました。これにより、ユーザーは視覚機能を持つチャットモデルを利用する際の注意点を理解しやすくなります。

## articles/ai-services/openai/how-to/dall-e.md{#item-ac9616}

<details>
<summary>Diff</summary>
````diff
@@ -21,26 +21,14 @@ OpenAI's DALL-E models generate images based on user-provided text prompts. This
 
 ## Prerequisites
 
-#### [DALL-E 3](#tab/dalle3)
-
 - An Azure subscription. You can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?icid=ai-services).
 - An Azure OpenAI resource created in a supported region. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
 - - Deploy a *dall-e-3* model with your Azure OpenAI resource.
 
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
-- An Azure subscription. You can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?icid=ai-services).
-- An Azure OpenAI resource created in a supported region. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability). For more information, see [Create and deploy an Azure OpenAI Service resource](../how-to/create-resource.md).
-
----
-
 ## Call the Image Generation APIs
 
 The following command shows the most basic way to use DALL-E with code. If this is your first time using these models programmatically, we recommend starting with the [DALL-E quickstart](/azure/ai-services/openai/dall-e-quickstart).
 
-
-#### [DALL-E 3](#tab/dalle3)
-
 Send a POST request to:
 
 ```
@@ -70,72 +58,10 @@ The following is a sample request body. You specify a number of options, defined
 }
 ```
 
-
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
-Image generation with DALL-E 2 is asynchronous and requires two API calls.
-
-First, send a POST request to:
-
-```
-https://<your_resource_name>.openai.azure.com/openai/images/generations:submit?api-version=<api_version>
-```
-
-**Replace the following placeholders**:
-- `<your_resource_name>` is the name of your Azure OpenAI resource.
-- `<api_version>` is the version of the API you want to use. For example, `2023-06-01-preview`.
-
-**Required headers**:
-- `Content-Type`: `application/json`
-- `api-key`: `<your_API_key>`
-
-**Body**:
-
-The following is a sample request body. You specify a number of options, defined in later sections.
-
-```json
-{
-    "prompt": "a multi-colored umbrella on the beach, disposable camera",  
-    "size": "1024x1024",
-    "n": 1
-}
-```
-
-The operation returns a `202` status code and a JSON object containing the ID and status of the operation
-
-```json
-{
-  "id": "3d3d3d3d-4444-eeee-5555-6f6f6f6f6f6f",
-  "status": "notRunning"
-}
-```
-
-To retrieve the image generation results, make a GET request to:
-
-```
-GET https://<your_resource_name>.openai.azure.com/openai/operations/images/<operation_id>?api-version=<api_version>
-```
-
-**Replace the following placeholders**:
-- `<your_resource_name>` is the name of your Azure OpenAI resource.
-- `<operation_id>` is the ID of the operation returned in the previous step.
-- `<api_version>` is the version of the API you want to use. For example, `2023-06-01-preview`.
-
-**Required headers**:
-- `Content-Type`: `application/json`
-- `api-key`: `<your_API_key>`
-
-The response from this API call contains your generated image.
-
----
-
-
 ## Output
 
 The output from a successful image generation API call looks like the following example. The `url` field contains a URL where you can download the generated image. The URL stays active for 24 hours.
 
-#### [DALL-E 3](#tab/dalle3)
-
 ```json
 { 
     "created": 1698116662, 
@@ -148,37 +74,12 @@ The output from a successful image generation API call looks like the following
 } 
 ```
 
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
-```json
-{
-    "created": 1685130482,
-    "expires": 1685216887,
-    "id": "<operation_id>",
-    "result":
-    {
-        "data":
-        [
-            {
-                "url": "<URL_to_generated_image>"
-            }
-        ]
-    },
-    "status": "succeeded"
-}
-```
-
----
-
-
 ### API call rejection
 
 Prompts and images are filtered based on our content policy, returning an error when a prompt or image is flagged.
 
 If your prompt is flagged, the `error.code` value in the message is set to `contentFilter`. Here's an example:
 
-#### [DALL-E 3](#tab/dalle3)
-
 ```json
 {
     "created": 1698435368,
@@ -190,26 +91,8 @@ If your prompt is flagged, the `error.code` value in the message is set to `cont
 }
 ```
 
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
-```json
-{
-   "created": 1589478378,
-   "error": {
-       "code": "contentFilter",
-       "message": "Your task failed as a result of our safety system."
-   },
-   "id": "4e4e4e4e-5555-ffff-6666-7a7a7a7a7a7a",
-   "status": "failed"
-}
-```
-
----
-
 It's also possible that the generated image itself is filtered. In this case, the error message is set to *Generated image was filtered as a result of our safety system*. Here's an example:
 
-#### [DALL-E 3](#tab/dalle3)
-
 ```json
 {
     "created": 1698435368,
@@ -221,31 +104,6 @@ It's also possible that the generated image itself is filtered. In this case, th
 }
 ```
 
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
-```json
-{
-   "created": 1589478378,
-   "expires": 1589478399,
-   "id": "4e4e4e4e-5555-ffff-6666-7a7a7a7a7a7a",
-   "lastActionDateTime": 1589478378,
-   "data": [
-       {
-           "url": "<URL_TO_IMAGE>"
-       },
-       {
-           "error": {
-               "code": "contentFilter",
-               "message": "Generated image was filtered as a result of our safety system."
-           }
-       }
-   ],
-   "status": "succeeded"
-}
-```
-
----
-
 ## Writing image prompts
 
 Your image prompts should describe the content you want to see in the image, and the visual style of image.
@@ -260,8 +118,6 @@ When writing prompts, consider that the image generation APIs come with a conten
 
 The following API body parameters are available for DALL-E image generation.
 
-#### [DALL-E 3](#tab/dalle3)
-
 ### Size
 
 Specify the size of the generated images. Must be one of `1024x1024`, `1792x1024`, or `1024x1792` for DALL-E 3 models. Square images are faster to generate.
@@ -288,18 +144,6 @@ With DALL-E 3, you can't generate more than one image in a single API call: the
 
 The format in which the generated images are returned. Must be one of `url` (a URL pointing to the image) or `b64_json` (the base 64-byte code in JSON format). The default is `url`.
 
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
-### Size
-
-Specify the size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024` for DALL-E 2 models.
-
-### Number
-
-Set the `n` parameter to an integer between 1 and 10 to generate multiple images at the same time using DALL-E 2. The images share an operation ID; you receive them all with the same retrieval API call.
-
----
-
 ## Related content
 
 * [What is Azure OpenAI Service?](../overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "DALL-Eに関するドキュメントの大幅な削除"
}
```

### Explanation
この変更は、DALL-Eに関するドキュメントの大部分を削除するものであり、主にDALL-E 2（プレビュー）に関連する情報が除去されました。この削除により、DALL-E 3に焦点を当てた構成へとシフトし、関連する手順やAPIの使用法を明確にすることが目的です。これにより、ユーザーが最新のDALL-E 3モデルを使用する際の情報が一層充実し、特にDALL-E 2に関する古い情報が排除されることで混乱を避ける効果があります。この結果、文書はよりシンプルで一貫性のあるものとなっています。

## articles/ai-services/openai/includes/dall-e-python.md{#item-c91824}

<details>
<summary>Diff</summary>
````diff
@@ -17,22 +17,11 @@ Use this guide to get started generating images with the Azure OpenAI SDK for Py
 
 ## Prerequisites
 
-#### [DALL-E 3](#tab/dalle3)
-
 - An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
 - <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>.
 - An Azure OpenAI resource created in a compatible region. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
 - Then, you need to deploy a `dalle3` model with your Azure resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
-- An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
-- <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>.
-- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
-
----
-
-
 ## Setup
 
 ### Retrieve key and endpoint
@@ -55,38 +44,22 @@ Go to your resource in the Azure portal. On the navigation pane, select **Keys a
 
 Open a command prompt and browse to your project folder. Install the OpenAI Python SDK by using the following command:
 
-#### [DALL-E 3](#tab/dalle3)
-
 ```bash
 pip install openai
 ```
 
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
-> [!IMPORTANT]
-> The latest release of the [OpenAI Python library](https://pypi.org/project/openai/) does not currently support DALL-E 2 when used with Azure OpenAI. To access DALL-E 2 with Azure OpenAI use version `0.28.1`. Or, follow the [migration guide](/azure/ai-services/openai/how-to/migration?tabs=python%2Cdalle-fix) to use DALL-E 2 with OpenAI 1.x.
-
-```bash
-pip install openai==0.28.1
-```
----
-
 Install the following libraries as well:
-
 ```bash
 pip install requests
 pip install pillow 
 ```
 
-
 ## Generate images with DALL-E
 
 Create a new python file, _quickstart.py_. Open it in your preferred editor or IDE.
 
 Replace the contents of _quickstart.py_ with the following code. 
 
-#### [DALL-E 3](#tab/dalle3)
-
 ```python
 from openai import AzureOpenAI
 import os
@@ -133,54 +106,6 @@ image.show()
 1. Change the value of `prompt` to your preferred text.
 1. Change the value of `model` to the name of your deployed DALL-E 3 model.
 
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
-```python
-import openai
-import os
-import requests
-from PIL import Image
-
-# Get endpoint and key from environment variables
-openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
-openai.api_key = os.environ['AZURE_OPENAI_API_KEY']     
-
-# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
-openai.api_version = '2023-06-01-preview'
-openai.api_type = 'azure'
-
-# Create an image by using the image generation API
-generation_response = openai.Image.create(
-    prompt='A painting of a dog',    # Enter your prompt text here
-    size='1024x1024',
-    n=2
-)
-
-# Set the directory for the stored image
-image_dir = os.path.join(os.curdir, 'images')
-
-# If the directory doesn't exist, create it
-if not os.path.isdir(image_dir):
-    os.mkdir(image_dir)
-
-# Initialize the image path (note the filetype should be png)
-image_path = os.path.join(image_dir, 'generated_image.png')
-
-# Retrieve the generated image
-image_url = generation_response["data"][0]["url"]  # extract image URL from response
-generated_image = requests.get(image_url).content  # download the image
-with open(image_path, "wb") as image_file:
-    image_file.write(generated_image)
-
-# Display the image in the default image viewer
-image = Image.open(image_path)
-image.show()
-```
-1. Enter your endpoint URL and key in the appropriate fields. 
-1. Change the value of `prompt` to your preferred text.
-
----
-
 > [!IMPORTANT]
 > Remember to remove the key from your code when you're done, and never post your key publicly. For production, use a secure way of storing and accessing your credentials. For more information, see [Azure Key Vault](/azure/key-vault/general/overview).
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "DALL-E 2に関する情報の削除"
}
```

### Explanation
この変更では、DALL-E 2に関連するすべての情報がドキュメントから削除され、主にDALL-E 3の使用に特化した内容へと刷新されました。DALL-E 2に関する設定手順やコード例、必要なライブラリのインストール方法が削除され、その結果、DALL-E 3の導入方法がより明確に示されています。この変更により、ユーザーは最新のDALL-E 3モデルを使用する際に必要な情報に直接アクセスできるようになり、従来のバージョンに対する混乱が減少します。全体として、ドキュメントはシンプルで一貫性を持つものとなり、より効率的に利用できるようになります。

## articles/ai-services/openai/includes/dall-e-rest.md{#item-4bac64}

<details>
<summary>Diff</summary>
````diff
@@ -15,25 +15,14 @@ Use this guide to get started calling the Azure OpenAI Service image generation
 
 ## Prerequisites
 
-#### [DALL-E 3](#tab/dalle3)
-
 - An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
 - <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>.
 - The following Python libraries installed: `os`, `requests`, `json`.
 - An Azure OpenAI resource created in a supported region. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
 - Then, you need to deploy a `dalle3` model with your Azure resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
-- An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
-- <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>.
-- The following Python libraries installed: `os`, `requests`, `json`.
-- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
-
----
-
-
 ## Setup 
+
 ### Retrieve key and endpoint
 
 To successfully call the Azure OpenAI APIs, you need the following information about your Azure OpenAI resource:
@@ -55,8 +44,6 @@ Create a new Python file named _quickstart.py_. Open the new file in your prefer
 
 1. Replace the contents of _quickstart.py_ with the following code. Change the value of `prompt` to your preferred text.
 
-    #### [DALL-E 3](#tab/dalle3)
-
     You also need to replace `<dalle3>` in the URL with the deployment name you chose when you deployed the DALL-E 3 model. Entering the model name will result in an error unless you chose a deployment name that is identical to the underlying model name. If you encounter an error, double check to make sure that you don't have a doubling of the `/` at the separation between your endpoint and `/openai/deployments`.
     
     ```python
@@ -86,46 +73,6 @@ Create a new Python file named _quickstart.py_. Open the new file in your prefer
 
     The script makes a synchronous image generation API call.
 
-    #### [DALL-E 2 (preview)](#tab/dalle2)
-
-    ```python
-    import requests
-    import time
-    import os
-
-    api_base = os.environ['AZURE_OPENAI_ENDPOINT'] # Enter your endpoint here
-    api_key = os.environ['AZURE_OPENAI_API_KEY']         # Enter your API key here
-
-    # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
-    api_version = '2023-06-01-preview'
-
-    # Define the prompt for the image generation
-    url = f"{api_base}openai/images/generations:submit?api-version={api_version}"
-    headers= { "api-key": api_key, "Content-Type": "application/json" }
-    body = {
-        # Enter your prompt text here
-        "prompt": "a multi-colored umbrella on the beach, disposable camera",  
-        "size": "1024x1024",
-        "n": 1
-    }
-    submission = requests.post(url, headers=headers, json=body)
-
-    # Call the API to generate the image and retrieve the response
-    operation_location = submission.headers['operation-location']
-    status = ""
-    while (status != "succeeded"):
-        time.sleep(1)
-        response = requests.get(operation_location, headers=headers)
-        status = response.json()['status']
-    image_url = response.json()['result']['data'][0]['url']
-
-    print(image_url)
-    ```
-    
-    The script makes an image generation API call and then loops until the generated image is ready.
-
-    ---
-    
     > [!IMPORTANT]
     > Remember to remove the key from your code when you're done, and never post your key publicly. For production, use a secure way of storing and accessing your credentials. For more information, see [Azure Key Vault](/azure/key-vault/general/overview).
 
@@ -141,9 +88,6 @@ Create a new Python file named _quickstart.py_. Open the new file in your prefer
 
 The output from a successful image generation API call looks like the following example. The `url` field contains a URL where you can download the generated image. The URL stays active for 24 hours.
 
-
-#### [DALL-E 3](#tab/dalle3)
-
 ```json
 { 
     "created": 1698116662, 
@@ -156,35 +100,10 @@ The output from a successful image generation API call looks like the following
 } 
 ```
 
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
-```json
-{
-    "created": 1685130482,
-    "expires": 1685216887,
-    "id": "088e4742-89e8-4c38-9833-c294a47059a3",
-    "result":
-    {
-        "data":
-        [
-            {
-                "url": "<URL_to_generated_image>"
-            }
-        ]
-    },
-    "status": "succeeded"
-}
-```
-
----
-
 The image generation APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it doesn't generate an image. For more information, see [Content filtering](../concepts/content-filter.md). For examples of error responses, see the [DALL-E how-to guide](../how-to/dall-e.md).
 
 The system returns an operation status of `Failed` and the `error.code` value in the message is set to `contentFilter`. Here's an example:
 
-
-#### [DALL-E 3](#tab/dalle3)
-
 ```json
 {
     "created": 1698435368,
@@ -196,28 +115,9 @@ The system returns an operation status of `Failed` and the `error.code` value in
 }
 ```
 
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
-```json
-{
-   "created": 1589478378,
-   "error": {
-       "code": "contentFilter",
-       "message": "Your task failed as a result of our safety system."
-   },
-   "id": "9484f239-9a05-41ba-997b-78252fec4b34",
-   "status": "failed"
-}
-```
-
-
----
-
 It's also possible that the generated image itself is filtered. In this case, the error message is set to `Generated image was filtered as a result of our safety system.`. Here's an example:
 
 
-#### [DALL-E 3](#tab/dalle3)
-
 ```json
 {
     "created": 1698435368,
@@ -229,32 +129,6 @@ It's also possible that the generated image itself is filtered. In this case, th
 }
 ```
 
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
-```json
-{
-   "created": 1589478378,
-   "expires": 1589478399,
-   "id": "9484f239-9a05-41ba-997b-78252fec4b34",
-   "lastActionDateTime": 1589478378,
-   "data": [
-       {
-           "url": "<URL_TO_IMAGE>"
-       },
-       {
-           "error": {
-               "code": "contentFilter",
-               "message": "Generated image was filtered as a result of our safety system."
-           }
-       }
-   ],
-   "status": "succeeded"
-}
-```
-
-
----
-
 ## Clean up resources
 
 If you want to clean up and remove an Azure OpenAI resource, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "DALL-E 2に関する情報の大幅な削除"
}
```

### Explanation
この変更では、DALL-E 2に関連するすべての情報が文書から大幅に削除され、DALL-E 3の使用に焦点を当てた内容へと更新されています。具体的には、DALL-E 2に必要な設定手順やAPI呼び出しのコード例が完全に除去され、DALL-E 3に関する情報だけが残されています。この結果、ユーザーは最新のDALL-E 3モデルに関連した情報にアクセスしやすくなるため、混乱を避けることができます。また、変更が1行追加されているものの、全体としては127行が削除されており、文書がよりシンプルで明瞭になっています。これにより、DALL-E 3を利用する開発者にとっての利便性が向上し、必要な情報が一元化されています。

## articles/ai-services/openai/includes/fine-tuning-studio.md{#item-439f1e}

<details>
<summary>Diff</summary>
````diff
@@ -302,7 +302,7 @@ Cross subscription/region deployment can be accomplished via [Python](/azure/ai-
 
 ## Use a deployed custom model
 
-After your custom model deploys, you can use it like any other deployed model. You can use the **Playgrounds** in [Azure AI Foundry portal](https://oai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models. For fine-tuned `babbage-002` and `davinci-002` models you will use the Completions playground and the Completions API. For fine-tuned `gpt-35-turbo-0613` models you will use the Chat playground and the Chat completion API.
+After your custom model deploys, you can use it like any other deployed model. You can use the **Playgrounds** in [Azure AI Foundry portal](https://oai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models.
 
 :::image type="content" source="../media/quickstarts/playground-load-new.png" alt-text="Screenshot of the Playground pane in Azure AI Foundry portal, with sections highlighted." lightbox="../media/quickstarts/playground-load-new.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムモデルの使用に関する説明の修正"
}
```

### Explanation
この変更では、カスタムモデルの使用に関する説明が修正され、より明確になります。具体的には、カスタムモデルがデプロイされた後の使用方法に関する文がわずかに調整されています。この変更により、ユーザーは自分のカスタムモデルを他のデプロイ済みモデルと同様に使用できることを明確に理解できるようになり、実験のためにAzure AI FoundryポータルのPlaygroundsを利用する指示が強調されています。変更内容は限られていますが、全体としてドキュメントの可読性や使いやすさが向上しています。

## articles/ai-services/openai/includes/gpt-v-studio.md{#item-dcd50e}

<details>
<summary>Diff</summary>
````diff
@@ -1,33 +1,45 @@
 ---
-title: 'Quickstart: Use images in chats with the Azure OpenAI Service'
+title: 'Quickstart: Use vision-enabled chats with the Azure OpenAI Service'
 titleSuffix: Azure OpenAI
 description: Use this article to get started using Azure AI Foundry to deploy and use an image-capable model.
 services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions, ignite-2024
-ms.date: 12/05/2024
+ms.date: 01/29/2025
 ---
 
-Start using images in your AI chats with a no-code approach through Azure AI Foundry.
+Use this article to get started using [Azure AI Foundry](https://ai.azure.com) to deploy and test a chat completion model with image understanding. 
+
 
 ## Prerequisites
 
 - An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
-- An Azure OpenAI Service resource. For more information about resource creation, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).
+- Once you have your Azure subscription, <a href="/azure/ai-services/openai/how-to/create-resource?pivots=web-portal"  title="Create an Azure OpenAI resource."  target="_blank">create an Azure OpenAI resource </a>.
+ For more information about resource creation, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).
+- An [Azure AI Foundry hub](/azure/ai-studio/how-to/create-azure-ai-resource) with your Azure OpenAI resource added as a connection. 
+
+## Prepare your media
+
+You need an image to complete this quickstart. You can use this sample image or any other image you have available.
+
+:::image type="content" source="/azure/ai-studio/media/quickstarts/multimodal-vision/car-accident.png" alt-text="Photo of a car accident that can be used to complete the quickstart." lightbox="/azure/ai-studio/media/quickstarts/multimodal-vision/car-accident.png":::
 
 ## Go to Azure AI Foundry
 
-Browse to [Azure AI Foundry](https://ai.azure.com/) and sign in with the credentials associated with your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
+1. Browse to [Azure AI Foundry](https://ai.azure.com/) and sign in with the credentials associated with your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
+1. Select the hub you'd like to work in.
+1. On the left nav menu, select **Models + endpoints** and select **+ Deploy model**.
+1. Choose an image-capable deployment by selecting model name: **gpt-4o** or **gpt-4o-mini**. In the window that appears, select a name and deployment type. Make sure your Azure OpenAI resource is connected. For more information about model deployment, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).
+1. Select **Deploy**.
+1. Next, select your new model and select **Open in playground**. In the chat playground, the deployment you created should be selected in the **Deployment** dropdown.
 
-Create a project or select an existing one. Navigate to the **Models + endpoints** option on the left, and select **Deploy model**. Choose an image-capable deployment by selecting model name: **gpt-4o** or **gpt-4o-mini**. For more information about model deployment, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).  
 
-Select the new deployment and select **Open in playground**.
 
 ## Playground
 
-From this page, you can quickly iterate and experiment with the model's capabilities. 
+In this chat session, you instruct the assistant to aid you in understanding images that you input.
 
 For general help with assistant setup, chat sessions, settings, and panels, refer to the [Chat quickstart](/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line&pivots=programming-language-studio). 
 
@@ -36,14 +48,50 @@ For general help with assistant setup, chat sessions, settings, and panels, refe
 
 In this chat session, you're instructing the assistant to aid in understanding images that you input. 
 1. To start, make sure your image-capable deployment is selected in the **Deployment** dropdown.
-2. In the **Setup** pane, provide a System Message to guide the assistant. The default System Message is: "You are an AI assistant that helps people find information." You can tailor the System Message to the image or scenario that you're uploading. 
+1. In the context text box on the **Setup** panel, provide this prompt to guide the assistant: `"You're an AI assistant that helps people find information."` Or, you can tailor the prompt to your image or scenario.
 
    > [!NOTE]
     > We recommend you update the System Message to be specific to the task in order to avoid unhelpful responses from the model.
 
-1. Save your changes, and when prompted to confirm updating the system message, select **Continue**.
-1. In the **Chat session** pane, enter a text prompt like "Describe this image," and upload an image with the attachment button. You can use a different text prompt for your use case. Then select **Send**. 
-1. Observe the output provided. Consider asking follow-up questions related to the analysis of your image to learn more.
+1. Select **Apply changes** to save your changes. 
+1. In the chat session pane, select the attachment button and then **Upload image**. Choose your image.
+1. Add the following prompt in the chat field: `Describe this image`, and then select the send icon to submit it.
+1. The send icon is replaced by a stop button. If you select it, the assistant stops processing your request. For this quickstart, let the assistant finish its reply.
+1. The assistant replies with a description of the image.
+1. Ask a follow-up question related to the analysis of your image. You could enter, `"What should I highlight about this image to my insurance company?"`.
+1. You should receive a relevant response similar to what's shown here:
+    ```
+    When reporting the incident to your insurance company, you should highlight the following key points from the image:  
+       
+    1. **Location of Damage**: Clearly state that the front end of the car, particularly the driver's side, is damaged. Mention the crumpled hood, broken front bumper, and the damaged left headlight.  
+       
+    2. **Point of Impact**: Indicate that the car has collided with a guardrail, which may suggest that no other vehicles were involved in the accident.  
+       
+    3. **Condition of the Car**: Note that the damage seems to be concentrated on the front end, and there is no visible damage to the windshield or rear of the car from this perspective.  
+       
+    4. **License Plate Visibility**: Mention that the license plate is intact and can be used for identification purposes.  
+       
+    5. **Environment**: Report that the accident occurred near a roadside with a guardrail, possibly in a rural or semi-rural area, which might help in establishing the accident location and context.  
+       
+    6. **Other Observations**: If there were any other circumstances or details not visible in the image that may have contributed to the accident, such as weather conditions, road conditions, or any other relevant information, be sure to include those as well.  
+       
+    Remember to be factual and descriptive, avoiding speculation about the cause of the accident, as the insurance company will conduct its own investigation.
+    ```
+## View and export code
+
+At any point in the chat session, you can enable the **Show raw JSON** switch at the top of the chat window to see the conversation formatted as JSON. Heres' what it looks like at the beginning of the quickstart chat session:
+
+```json
+[
+	{
+		"role": "system",
+		"content": [
+			"You are an AI assistant that helps people find information."
+		]
+	},
+]
+```
+
 
 
 ## Clean up resources
@@ -52,3 +100,5 @@ If you want to clean up and remove an Azure OpenAI resource, you can delete the
 
 - [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
 - [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
+
+
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "視覚機能を持つチャットに関するクイックスターションの更新"
}
```

### Explanation
この変更では、Azure OpenAI Serviceを使用した視覚機能を持つチャットのクイックスターションが更新され、内容が大幅に拡充されました。まず、タイトルが「画像を使用したチャット」から「視覚機能を持つチャット」に変更され、より具体的な目的が示されています。また、前提条件セクションに新たに「Azure AI Foundry hub」の設定や、準備として必要な画像についての情報が追加されました。

手順の構成も更新され、Azure AI Foundryでの操作手順が順を追って明示されるようになり、ユーザーがモデルをデプロイしてテストする際の流れが分かりやすくなっています。特に、画像をアップロードしてその分析を行うための具体的な手順や、モデルの応答例が含まれており、利用者にとって実用的なガイドとなっています。全体として、このドキュメントは、視覚的要素を利用したチャット体験を強化するための重要な手引きとなっています。


