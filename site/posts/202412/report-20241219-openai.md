---
date: '2024-12-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:aba0ab5...MicrosoftDocs:6ebedb4
summary: このコード差分は、Azure OpenAIサービスに関連する文書の複数の更新を含んでおり、主な改変点はモデル名称の変更、新機能「直接好み最適化（DPO）」の追加、日付やリンクの更新、視覚的資料のマイナーアップデート、目次の再構成、役割ベースのアクセス制御の強化です。特にDPOはファインチューニングプロセスを改善し、ユーザーがより効率的にモデルをカスタマイズできるようにしています。この更新により、文書の整合性や視認性が向上し、ユーザーエクスペリエンスが改善されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:aba0ab5...MicrosoftDocs:6ebedb4){target="_blank"}

# Highlights
このコード差分は、Azure OpenAIサービスに関する複数の文書の更新を含んでいます。主な改変点は以下のとおりです。

- モデルの名称変更：「o1-preview」と「o1-mini」が「o1」と「o1-mini」に修正されました。
- 新しい機能として「直接好み最適化（DPO）」が追加されました。
- ドキュメントの様々な箇所における日付やリンクの更新。
- 画像ファイルや図版のマイナーな更新を行い、視覚的な資料の最新性を保持。
- 目次の再構成による可読性の向上や、新しい「推論モデル」セクションの追加。
- 役割ベースのアクセス制御やストレージ完了関連の権限強化。

## New features
- 直接好み最適化（DPO）が新たに導入され、大規模言語モデルのファインチューニングにおける新しい手法が説明されました。
- 推論モデル「o1」のセクションが追加され、新しい使用例が提供されています。

## Breaking changes
- 旧バージョンのモデル名称が修正されたことにより、従来のドキュメントとの不整合が発生する可能性があります。

## Other updates
- 様々な新機能に応じた文書や画像のマイナーな更新と修正が行われました。新しいモデルや機能へのアクセスリンクが更新され、利用者が容易に必要情報を得られるようになっています。
- 役割ベースのアクセス権が明確化され、ユーザーは権限を正確に理解しやすくなっています。

# Insights
このコード差分はAzure OpenAIサービスの効率性とユーザビリティの向上に大きく寄与しています。主なポイントを以下にまとめます。

Azure OpenAIサービスは、新しい機能やモデル、特に直接好み最適化（DPO）などを導入することで、ファインチューニングプロセスをさらに改善しています。これにより、ユーザーはより効率的にモデルをカスタマイズでき、特定のシナリオにおける運用効果が向上します。DPOは、主観的な要素が影響する場面で特に効果的で、多様なユーザーニーズに応えることを目的としています。

さらに、構造的な更新や改修により、ドキュメントの整合性や視認性が改善されました。具体的には、古いモデル名称の修正、アクセスリンクの再構築、および画像メタデータの更新を通じて、文書の最新性が維持されています。これにより、ユーザーは最新の情報をもとに正確な判断と選択を行うことが可能になります。

最後に、推論モデルに関する新たなセクションの追加や、新しいファインチューニング手法の紹介は、ユーザーがAzure OpenAIの持つ可能性を最大限に活用する手助けをしています。文書全体を通じて、ユーザーエクスペリエンスの向上と情報の可視化が明確に図られています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | モデルの名称変更と情報の更新 | modified | 14 | 181 | 195 | 
| [fine-tuning.md](#item-5c0e85) | new feature | 直接好み最適化（DPO）の追加 | modified | 54 | 0 | 54 | 
| [gpt-with-vision.md](#item-4d8502) | minor update | 文書内容の軽微な修正 | modified | 3 | 3 | 6 | 
| [on-your-data-configuration.md](#item-4875d3) | minor update | Cognitive Services User ロールの削除 | modified | 0 | 1 | 1 | 
| [prompt-caching.md](#item-1631df) | minor update | サポートされるモデルの追加 | modified | 1 | 0 | 1 | 
| [realtime-audio.md](#item-482ba3) | minor update | リアルタイムオーディオAPIに関するガイドの更新 | modified | 14 | 9 | 23 | 
| [reasoning.md](#item-a54b2f) | new feature | Azure OpenAIの推論モデルに関する新しいセクションの追加 | added | 303 | 0 | 303 | 
| [role-based-access-control.md](#item-4b9817) | minor update | 役割ベースのアクセス制御ドキュメントの更新 | modified | 5 | 0 | 5 | 
| [structured-outputs.md](#item-cc2557) | minor update | 構造化出力に関するドキュメントの更新 | modified | 2 | 3 | 5 | 
| [fine-tuning-openai-in-ai-studio.md](#item-723c8d) | minor update | AI Studioにおけるファインチューニングの設定内容の更新 | modified | 1 | 0 | 1 | 
| [fine-tuning-studio.md](#item-439f1e) | minor update | ファインチューニングスタジオのパラメータの更新 | modified | 3 | 0 | 3 | 
| [gpt-v-dotnet.md](#item-120a68) | minor update | GPT-4 Turboに関するクイックスタートガイドのタイトル更新 | modified | 1 | 1 | 2 | 
| [gpt-v-javascript.md](#item-a128c9) | minor update | GPT-4 Turboに関するクイックスタートガイドのタイトル更新 | modified | 1 | 1 | 2 | 
| [gpt-v-python.md](#item-366276) | minor update | GPT-4 Turboに関するクイックスタートガイドのタイトル更新 | modified | 1 | 1 | 2 | 
| [gpt-v-rest.md](#item-65c91c) | minor update | GPT-4 Turboに関するクイックスタートガイドのタイトル更新 | modified | 1 | 1 | 2 | 
| [gpt-v-studio.md](#item-dcd50e) | minor update | Azure OpenAI Serviceに関するクイックスタートガイドのタイトル修正 | modified | 1 | 1 | 2 | 
| [gpt-v-typescript.md](#item-03ec34) | minor update | JavaScript SDKに関するクイックスタートガイドのタイトル修正 | modified | 1 | 1 | 2 | 
| [apply-system-message.png](#item-ad3af6) | minor update | システムメッセージの適用に関する画像のメタデータ更新 | modified | 0 | 0 | 0 | 
| [fine-tune-new.png](#item-60c08f) | minor update | 新しいファインチューニング画像のメタデータ更新 | modified | 0 | 0 | 0 | 
| [preference-optimization.gif](#item-6b0b5a) | new feature | 新しいファインチューニング用画像の追加 | added | 0 | 0 | 0 | 
| [content-detection.png](#item-d8de97) | minor update | コンテンツ検出画像のメタデータ更新 | modified | 0 | 0 | 0 | 
| [create-batch-job-empty.png](#item-8d7507) | minor update | バッチジョブ作成画面の画像更新 | modified | 0 | 0 | 0 | 
| [real-time-playground.png](#item-a36b1d) | minor update | リアルタイムプレイグラウンド画像の更新 | modified | 0 | 0 | 0 | 
| [navigate-chat-playground.png](#item-80edd6) | minor update | チャットプレイグラウンド画像の更新 | modified | 0 | 0 | 0 | 
| [navigate-system-message.png](#item-f8571e) | minor update | システムメッセージ画像の更新 | modified | 0 | 0 | 0 | 
| [deployment-screen.jpg](#item-5ce772) | minor update | デプロイメント画面画像の削除 | removed | 0 | 0 | 0 | 
| [ptu-quota-page.png](#item-aedb7d) | minor update | PTUクオーターページ画像の更新 | modified | 0 | 0 | 0 | 
| [quota-new.png](#item-9f797f) | minor update | クオーターニュー画像の更新 | modified | 0 | 0 | 0 | 
| [review-system-message.png](#item-9a1b06) | minor update | レビューシステムメッセージ画像の更新 | modified | 0 | 0 | 0 | 
| [select-system-message.png](#item-80fc6b) | minor update | セレクトシステムメッセージ画像の更新 | modified | 0 | 0 | 0 | 
| [overview.md](#item-97d507) | minor update | Azure OpenAIサービスの概要の更新 | modified | 3 | 3 | 6 | 
| [toc.yml](#item-c945af) | minor update | 目次に推論モデルのセクションを追加 | modified | 2 | 0 | 2 | 
| [whats-new.md](#item-53303b) | minor update | 最新のリリース情報の追加 | modified | 25 | 1 | 26 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 
 | Models | Description |
 |--|--|
-| [o1-preview and o1-mini](#o1-preview-and-o1-mini-models-limited-access) | Limited access models, specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability.  |
+| [o1 & o1-mini](#o1-and-o1-mini-models-limited-access) | Limited access models, specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability.  |
 | [GPT-4o & GPT-4o mini & GPT-4 Turbo](#gpt-4o-and-gpt-4-turbo) | The latest most capable Azure OpenAI models with multimodal versions, which can accept both text and images as input. |
 | [GPT-4o-Realtime-Preview](#gpt-4o-realtime-preview) | A GPT-4o model that supports low-latency, "speech in, speech out" conversational interactions. |
 | [GPT-4](#gpt-4) | A set of models that improve on GPT-3.5 and can understand and generate natural language and code. |
@@ -28,200 +28,33 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 | [Whisper](#whisper-models) | A series of models in preview that can transcribe and translate speech to text. |
 | [Text to speech](#text-to-speech-models-preview) (Preview) | A series of models in preview that can synthesize text to speech. |
 
-## o1-preview and o1-mini models limited access
+## o1 and o1-mini models limited access
 
-The Azure OpenAI `o1-preview` and `o1-mini` models are specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
+The Azure OpenAI `o1` and `o1-mini` models are specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
 
 |  Model ID  | Description | Max Request (tokens) | Training Data (up to)  |
 |  --- |  :--- |:--- |:---: |
-|`o1-preview` (2024-09-12) | The most capable model in the o1 series, offering enhanced reasoning abilities.| Input: 128,000  <br> Output: 32,768 | Oct 2023 |
+| `o1` (2024-12-17) | The most capable model in the o1 series, offering enhanced reasoning abilities. <br> **Request access: [limited access model application](https://aka.ms/OAI/o1access)** <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools <br> | Input: 200,000 <br> Output: 100,000 | |  
+|`o1-preview` (2024-09-12) | Older preview version | Input: 128,000  <br> Output: 32,768 | Oct 2023 |
 | `o1-mini` (2024-09-12) | A faster and more cost-efficient option in the o1 series, ideal for coding tasks requiring speed and lower resource consumption.| Input: 128,000  <br> Output: 65,536 | Oct 2023 |
 
 ### Availability
 
-The `o1-preview` and `o1-mini` models are now available for API access and model deployment. **Registration is required, and access will be granted based on Microsoft's eligibility criteria**.
+The `o1` and `o1-mini` models are now available for API access and model deployment. **Registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who previously applied and received access to `o1-preview`, don't need to reapply as they are automatically on the wait-list for the latest model.
 
-Request access: [limited access model application](https://aka.ms/oai/modelaccess)
+Request access: [limited access model application](https://aka.ms/OAI/o1access)
 
-Once access has been granted, you will need to create a deployment for each model.
+Once access has been granted, you will need to create a deployment for each model. If you have an existing `o1-preview` deployment in place upgrade is currently not supported, you will need to create a new deployment.
 
-### API support
-
-Support for the **o1 series** models was added in API version `2024-09-01-preview`.
-
-The `max_tokens` parameter has been deprecated and replaced with the new `max_completion_tokens` parameter. **o1 series** models will only work with the `max_completion_tokens` parameter.
-
-### Usage
-
-These models do not currently support the same set of parameters as other models that use the chat completions API. Only a very limited subset is currently supported, so common parameters like `temperature`, `top_p`, are not available and including them will cause your request to fail. `o1-preview` and `o1-mini` models will also not accept the system message role as part of the messages array.
-
-# [Python (Microsoft Entra ID)](#tab/python-secure)
-
-You may need to upgrade your version of the OpenAI Python library to take advantage of the new `max_completion_tokens` parameter.
-
-```cmd
-pip install openai --upgrade
-```
-
-If you are new to using Microsoft Entra ID for authentication see [How to configure Azure OpenAI Service with Microsoft Entra ID authentication](../how-to/managed-identity.md).
-
-```python
-from openai import AzureOpenAI
-from azure.identity import DefaultAzureCredential, get_bearer_token_provider
-
-token_provider = get_bearer_token_provider(
-    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
-)
-
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
-  azure_ad_token_provider=token_provider,
-  api_version="2024-09-01-preview"
-)
-
-response = client.chat.completions.create(
-    model="o1-preview-new", # replace with the model deployment name of your o1-preview, or o1-mini model
-    messages=[
-        {"role": "user", "content": "What steps should I think about when writing my first Python API?"},
-    ],
-    max_completion_tokens = 5000
-
-)
-
-print(response.model_dump_json(indent=2))
-```
-
-# [Python (key-based auth)](#tab/python)
-
-You may need to upgrade your version of the OpenAI Python library to take advantage of the new `max_completion_tokens` parameter.
-
-```cmd
-pip install openai --upgrade
-```
-
-```python
-
-from openai import AzureOpenAI
-
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
-  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-09-01-preview"
-)
-
-response = client.chat.completions.create(
-    model="o1-preview-new", # replace with the model deployment name of your o1-preview, or o1-mini model
-    messages=[
-        {"role": "user", "content": "What steps should I think about when writing my first Python API?"},
-    ],
-    max_completion_tokens = 5000
-
-)
-
-print(response.model_dump_json(indent=2))
-```
-
-# [Output](#tab/python-output)
-
-```json
-{
-  "id": "chatcmpl-AEj7pKFoiTqDPHuxOcirA9KIvf3yz",
-  "choices": [
-    {
-      "finish_reason": "stop",
-      "index": 0,
-      "logprobs": null,
-      "message": {
-        "content": "Writing your first Python API is an exciting step in developing software that can communicate with other applications. An API (Application Programming Interface) allows different software systems to interact with each other, enabling data exchange and functionality sharing. Here are the steps you should consider when creating your first Python API:\n\n1. **Define the Purpose and Requirements**\n\n   - **Identify the Functionality**: Clearly outline what your API is supposed to do. What data or services will it provide to the users?\n   - **Determine the Endpoints**: Plan the different URLs (endpoints) through which users can access the API functionalities.\n   - **Specify Request and Response Formats**: Decide on the data formats (usually JSON) for incoming requests and outgoing responses.\n\n2. **Choose the Right Framework**\n\n   Python offers several frameworks for building APIs. Two of the most popular are:\n\n   - **Flask**: A lightweight and flexible web framework, great for small to medium-sized APIs.\n   - **FastAPI**: A modern, high-performance framework for building APIs with Python 3.6+ types, offering automatic interactive documentation.\n\n   **Example**:\n   ```bash\n   pip install flask\n   ```\n   or\n   ```bash\n   pip install fastapi uvicorn\n   ```\n\n3. **Set Up the Development Environment**\n\n   - **Create a Virtual Environment**: Isolate your project dependencies using `venv` or `conda`.\n   - **Install Required Packages**: Ensure all necessary libraries and packages are installed.\n\n   **Example**:\n   ```bash\n   python -m venv env\n   source env/bin/activate  # On Windows use `env\\Scripts\\activate`\n   ```\n\n4. **Implement the API Endpoints**\n\n   - **Write the Code for Each Endpoint**: Implement the logic that handles requests and returns responses.\n   - **Use Decorators to Define Routes**: In frameworks like Flask, you use decorators to specify the URL endpoints.\n\n   **Example with Flask**:\n   ```python\n   from flask import Flask, request, jsonify\n\n   app = Flask(__name__)\n\n   @app.route('/hello', methods=['GET'])\n   def hello_world():\n       return jsonify({'message': 'Hello, World!'})\n\n   if __name__ == '__main__':\n       app.run(debug=True)\n   ```\n\n5. **Handle Data Serialization and Deserialization**\n\n   - **Parsing Incoming Data**: Use libraries to parse JSON or other data formats from requests.\n   - **Formatting Output Data**: Ensure that responses are properly formatted in JSON or XML.\n\n6. **Implement Error Handling**\n\n   - **Handle Exceptions Gracefully**: Provide meaningful error messages and HTTP status codes.\n   - **Validate Input Data**: Check for required fields and appropriate data types to prevent errors.\n\n   **Example**:\n   ```python\n   @app.errorhandler(404)\n   def resource_not_found(e):\n       return jsonify(error=str(e)), 404\n   ```\n\n7. **Add Authentication and Authorization (If Necessary)**\n\n   - **Secure Endpoints**: If your API requires, implement security measures such as API keys, tokens (JWT), or OAuth.\n   - **Manage User Sessions**: Handle user login states and permissions appropriately.\n\n8. **Document Your API**\n\n   - **Use Tools Like Swagger/OpenAPI**: Automatically generate interactive API documentation.\n   - **Provide Usage Examples**: Help users understand how to interact with your API.\n\n   **Example with FastAPI**:\n   FastAPI automatically generates docs at `/docs` using Swagger UI.\n\n9. **Test Your API**\n\n   - **Write Unit and Integration Tests**: Ensure each endpoint works as expected.\n   - **Use Testing Tools**: Utilize tools like `unittest`, `pytest`, or API testing platforms like Postman.\n\n   **Example**:\n   ```python\n   import unittest\n   class TestAPI(unittest.TestCase):\n       def test_hello_world(self):\n           response = app.test_client().get('/hello')\n           self.assertEqual(response.status_code, 200)\n   ```\n\n10. **Optimize Performance**\n\n    - **Improve Response Times**: Optimize your code and consider using asynchronous programming if necessary.\n    - **Manage Resource Utilization**: Ensure your API can handle the expected load.\n\n11. **Deploy Your API**\n\n    - **Choose a Hosting Platform**: Options include AWS, Heroku, DigitalOcean, etc.\n    - **Configure the Server**: Set up the environment to run your API in a production setting.\n    - **Use a Production Server**: Instead of the development server, use WSGI servers like Gunicorn or Uvicorn.\n\n    **Example**:\n    ```bash\n    uvicorn main:app --host 0.0.0.0 --port 80\n    ```\n\n12. **Monitor and Maintain**\n\n    - **Logging**: Implement logging to track events and errors.\n    - **Monitoring**: Use monitoring tools to track performance and uptime.\n    - **Update and Patch**: Keep dependencies up to date and patch any security vulnerabilities.\n\n13. **Consider Versioning**\n\n    - **Plan for Updates**: Use versioning in your API endpoints to manage changes without breaking existing clients.\n    - **Example**:\n      ```python\n      @app.route('/v1/hello', methods=['GET'])\n      ```\n\n14. **Gather Feedback and Iterate**\n\n    - **User Feedback**: Encourage users to provide feedback on your API.\n    - **Continuous Improvement**: Use the feedback to make improvements and add features.\n\n**Additional Tips**:\n\n- **Keep It Simple**: Start with a minimal viable API and expand functionality over time.\n- **Follow RESTful Principles**: Design your API according to REST standards to make it intuitive and standard-compliant.\n- **Security Best Practices**: Always sanitize inputs and protect against common vulnerabilities like SQL injection and cross-site scripting (XSS).\nBy following these steps, you'll be well on your way to creating a functional and robust Python API. Good luck with your development!",
-        "refusal": null,
-        "role": "assistant",
-        "function_call": null,
-        "tool_calls": null
-      },
-      "content_filter_results": {
-        "hate": {
-          "filtered": false,
-          "severity": "safe"
-        },
-        "protected_material_code": {
-          "filtered": false,
-          "detected": false
-        },
-        "protected_material_text": {
-          "filtered": false,
-          "detected": false
-        },
-        "self_harm": {
-          "filtered": false,
-          "severity": "safe"
-        },
-        "sexual": {
-          "filtered": false,
-          "severity": "safe"
-        },
-        "violence": {
-          "filtered": false,
-          "severity": "safe"
-        }
-      }
-    }
-  ],
-  "created": 1728073417,
-  "model": "o1-preview-2024-09-12",
-  "object": "chat.completion",
-  "service_tier": null,
-  "system_fingerprint": "fp_503a95a7d8",
-  "usage": {
-    "completion_tokens": 1843,
-    "prompt_tokens": 20,
-    "total_tokens": 1863,
-    "completion_tokens_details": {
-      "audio_tokens": null,
-      "reasoning_tokens": 448
-    },
-    "prompt_tokens_details": {
-      "audio_tokens": null,
-      "cached_tokens": 0
-    }
-  },
-  "prompt_filter_results": [
-    {
-      "prompt_index": 0,
-      "content_filter_results": {
-        "custom_blocklists": {
-          "filtered": false
-        },
-        "hate": {
-          "filtered": false,
-          "severity": "safe"
-        },
-        "jailbreak": {
-          "filtered": false,
-          "detected": false
-        },
-        "self_harm": {
-          "filtered": false,
-          "severity": "safe"
-        },
-        "sexual": {
-          "filtered": false,
-          "severity": "safe"
-        },
-        "violence": {
-          "filtered": false,
-          "severity": "safe"
-        }
-      }
-    }
-  ]
-}
-```
-
----
+To learn more about the advanced `o1` series models see, [getting started with o1 series reasoning models](../how-to/reasoning.md).
 
 ### Region availability
 
-Available for standard and global standard deployment in East US, East US2, North Central US, South Central US, Sweden Central, West US, and West US3 for approved customers.
+| Model | Region |
+|---|---|
+|`o1` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
+| `o1-preview` | See the [models table](#global-standard-model-availability). |
+| `o1-mini` | See the [models table](#global-provisioned-managed-model-availability). |
 
 ## GPT-4o-Realtime-Preview
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの名称変更と情報の更新"
}
```

### Explanation
この変更では、Azure OpenAI Serviceのドキュメント内でモデルに関する情報が更新され、特に「o1-preview」と「o1-mini」というモデルの名称がそれぞれ「o1」と「o1-mini」に変更されています。また、新しいモデルに関する詳細や、ユーザーが新しいモデルにアクセスするための手続きが明確に記載された分、情報の整理と更新が行われました。具体的には、以下のような主なポイントがあります。

1. **モデル名の変更**: この変更により、ユーザーは「o1-preview」を「o1」と呼び、「o1-mini」についても同様の修正が行われました。

2. **説明内容の改善**: 新しいモデルの説明が詳細になり、強化された機能や利用方法に関する情報が追加されています。

3. **アクセシビリティの強調**: 新しいo1モデルがAPIアクセスおよびデプロイメントに利用可能であることが明確にされ、旧バージョンからの移行手続きが案内されています。

4. **リファレンスの更新**: ユーザーが新しいモデルにアクセスする際の手続きを記載したリンクが更新され、利用者が必要な情報をすぐに見つけられるように配慮されています。

このように、モデルに関する情報が整理され、ユーザーにとってより利用しやすい文書へと進化しているといえます。

## articles/ai-services/openai/how-to/fine-tuning.md{#item-5c0e85}

<details>
<summary>Diff</summary>
````diff
@@ -97,6 +97,60 @@ Images containing the following will be excluded from your dataset and not used
 
 Azure OpenAI fine-tuning supports prompt caching with select models. Prompt caching allows you to reduce overall request latency and cost for longer prompts that have identical content at the beginning of the prompt. To learn more about prompt caching, see [getting started with prompt caching](./prompt-caching.md).
 
+## Direct preference optimization (DPO) (preview)
+
+Direct preference optimization (DPO) is an alignment technique for large language models, used to adjust model weights based on human preferences. It differs from reinforcement learning from human feedback (RLHF) in that it does not require fitting a reward model and uses simpler binary data preferences for training. It is computationally lighter weight and faster than RLHF, while being equally effective at alignment.
+
+### Why is DPO useful?
+
+DPO is especially useful in scenarios where there's no clear-cut correct answer, and subjective elements like tone, style, or specific content preferences are important. This approach also enables the model to learn from both positive examples (what's considered correct or ideal) and negative examples (what's less desired or incorrect).
+
+DPO is believed to be a technique that will make it easier for customers to generate high-quality training data sets. While many customers struggle to generate sufficient large data sets for supervised fine-tuning, they often have preference data already collected based on user logs, A/B tests, or smaller manual annotation efforts.
+
+### Direct preference optimization dataset format
+
+Direct preference optimization files have a different format than supervised fine-tuning. Customers provide a "conversation" containing the system message and the initial user message, and then "completions" with paired preference data. Users can only provide two completions.
+
+Three top-level fields: `input`, `preferred_output` and `non_preferred_output`
+
+- Each element in the preferred_output/non_preferred_output must contain at least one assistant message
+- Each element in the preferred_output/non_preferred_output can only have roles in (assistant, tool)
+
+```json
+{  
+  "input": {  
+    "messages": {"role": "system", "content": ...},  
+    "tools": [...],  
+    "parallel_tool_calls": true  
+  },  
+  "preferred_output": [{"role": "assistant", "content": ...}],  
+  "non_preferred_output": [{"role": "assistant", "content": ...}]  
+}  
+```
+
+Training datasets must be in `jsonl` format:
+
+```jsonl
+{{"input": {"messages": [{"role": "system", "content": "You are a chatbot assistant. Given a user question with multiple choice answers, provide the correct answer."}, {"role": "user", "content": "Question: Janette conducts an investigation to see which foods make her feel more fatigued. She eats one of four different foods each day at the same time for four days and then records how she feels. She asks her friend Carmen to do the same investigation to see if she gets similar results. Which would make the investigation most difficult to replicate? Answer choices: A: measuring the amount of fatigue, B: making sure the same foods are eaten, C: recording observations in the same chart, D: making sure the foods are at the same temperature"}]}, "preferred_output": [{"role": "assistant", "content": "A: Measuring The Amount Of Fatigue"}], "non_preferred_output": [{"role": "assistant", "content": "D: making sure the foods are at the same temperature"}]}
+}
+```
+
+### Direct preference optimization model support
+
+- `gpt-4o-2024-08-06` supports direct preference optimization in its respective fine-tuning regions. Latest region availability is updated in the [models page](../concepts/models.md#fine-tuning-models)
+
+Users can use preference fine tuning with base models as well as models that have already been fine-tuned using supervised fine-tuning as long as they are of a supported model/version.
+
+### How to use direct preference optimization fine-tuning?
+
+   :::image type="content" border="true" source="/azure/ai-services/openai/media/fine-tuning/preference-optimization.gif" alt-text="GIF of preference optimization fine-tuning steps.":::
+
+1. Prepare `jsonl` datasets in the [preference format](#direct-preference-optimization-dataset-format).
+2. Select the model and then select the method of customization **Direct Preference Optimization**.
+3. Upload datasets – training and validation. Preview as needed.
+4. Select hyperparameters, defaults are recommended for initial experimentation.
+5. Review the selections and create a fine tuning job.
+
 ## Troubleshooting
 
 ### How do I enable fine-tuning?
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "直接好み最適化（DPO）の追加"
}
```

### Explanation
この変更は、Azure OpenAIのファインチューニングに関する文章に「直接好み最適化（DPO）」という新しい機能が追加されたものです。DPOは、大規模言語モデルにおいて人間の好みに基づいてモデルの重みを調整するための手法であり、強化学習（RLHF）とは異なり、報酬モデルをフィッティングする必要がなく、単純なバイナリデータの好みを使用してトレーニングを行います。この変更の主なポイントは以下の通りです。

1. **DPOの導入**: DPOは、主観的な要素が重要なシナリオで特に有用で、正しい答えが明確でない場合にモデルがトーンやスタイル、具体的なコンテンツの好みを学ぶのを助けるために設計されています。これにより、高品質なトレーニングデータセットの生成が容易になるとされています。

2. **データセットフォーマットの説明**: DPO用のデータセットは、従来の監視付きファインチューニングとは異なるフォーマットを持っており、顧客はシステムメッセージと最初のユーザーメッセージを含む「会話」と、ペアの好みデータを持つ「コンプリート」を提供する必要があります。

3. **使用方法のガイド**: 具体的な使用手順が提示され、DPOを利用したファインチューニングの流れが説明されています。これには、データセットの準備、モデルの選択、データのアップロード、ハイパーパラメータの選定などが含まれています。

4. **モデルサポートの情報**: DPOをサポートするモデル名とそれらが利用できるファインチューニングの地域についても情報が提供されています。

これにより、ユーザーは直接的な好み最適化を活用して、より効果的なファインチューニングが可能になります。

## articles/ai-services/openai/how-to/gpt-with-vision.md{#item-4d8502}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ manager: nitinme
 
 Vision-enabled chat models are large multimodal models (LMM) developed by OpenAI that can analyze images and provide textual responses to questions about them. They incorporate both natural language processing and visual understanding. The current vision-enabled models are GPT-4 Turbo with Vision, GPT-4o, and GPT-4o-mini.
 
-The vision-enabled models answer general questions about what's present in the images or videos you upload.
+The vision-enabled models answer general questions about what's present in the images you upload.
 
 > [!TIP]
 > To use vision-enabled models, you call the Chat Completion API on a supported model that you have deployed. If you're not familiar with the Chat Completion API, see the [Vision-enabled chat how-to guide](/azure/ai-services/openai/how-to/chatgpt?tabs=python&pivots=programming-language-chat-completions).
@@ -290,7 +290,7 @@ Every response includes a `"finish_reason"` field. It has the following possible
 - `length`: Incomplete model output due to the `max_tokens` input parameter or model's token limit.
 - `content_filter`: Omitted content due to a flag from our content filters.
 
-
+<!--
 
 ### Create a video retrieval index
 
@@ -366,7 +366,7 @@ Every response includes a `"finish_reason"` field. It has the following possible
     ```bash
     curl.exe -v -X GET "https://<YOUR_ENDPOINT_URL>/computervision/retrieval/indexes/my-video-index/ingestions?api-version=2023-05-01-preview&$top=20" -H "ocp-apim-subscription-key: <YOUR_SUBSCRIPTION_KEY>"
     ```
-
+-->
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書内容の軽微な修正"
}
```

### Explanation
この変更は、Azure OpenAIの「画像を使ったGPT」ガイドにおける文書の軽微な修正を示しています。具体的には、以下のポイントに焦点が当てられています。

1. **文言の修正**: モデルが画像や動画に関しての質問に答えるという記述部分で、「videos（動画）」という言葉が削除され、「images（画像）」のみに言及するように修正されました。これにより、システムが主に画像に焦点を当てていることがより明確になっています。

2. **コメントアウトの追加**: 特定の行の間にHTMLコメントが追加されています。これは文書内の内容を整理し、将来的に利用できるように保つための措置である可能性があります。

3. **全体的な構造保守**: これらの変更は情報の正確性と明瞭さを高めるために行われたものであり、システムの使用方法に関する基本的な理解を補完しています。

これらの修正により、ユーザーは画像を使ったGPTモデルの機能をより適切に理解できるようになります。

## articles/ai-services/openai/how-to/on-your-data-configuration.md{#item-4875d3}

<details>
<summary>Diff</summary>
````diff
@@ -286,7 +286,6 @@ To enable the developers to use these resources to build applications, the admin
 |Role| Resource | Description |
 |--|--|--|
 | `Cognitive Services OpenAI Contributor` | Azure OpenAI | Call public ingestion API from Azure OpenAI Studio. The `Contributor` role is not enough, because if you only have `Contributor` role, you cannot call data plane API via Microsoft Entra ID authentication, and Microsoft Entra ID authentication is required in the secure setup described in this article. |
-| `Cognitive Services User` | Azure OpenAI | List API-Keys from Azure OpenAI Studio.|
 | `Contributor` | Azure AI Search | List API-Keys to list indexes from Azure OpenAI Studio.|
 | `Contributor` | Storage Account | List Account SAS to upload files from Azure OpenAI Studio.|
 | `Contributor` | The resource group or Azure subscription where the developer need to deploy the web app to | Deploy web app to the developer's Azure subscription.|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cognitive Services User ロールの削除"
}
```

### Explanation
この変更は、Azure OpenAIに関するドキュメントの一部において、Cognitive Servicesに関連するユーザーロールの説明を軽微に修正したものです。具体的には、以下のポイントが挙げられます。

1. **ロールの削除**: ドキュメント内の表において、「Cognitive Services User」ロールに関する行が削除されました。このロールは以前、Azure OpenAIスタジオからAPIキーをリストするために必要とされていましたが、更新により不要と判断された可能性があります。

2. **文書の簡素化**: この変更により、ユーザーは必要なロールに関する情報をより明確に理解できるようになります。特に、APIにアクセスするために必要なロールの情報が整理され、混乱を避けることができるようになっています。

3. **全体的な構造保守**: 他のロールに関する情報は維持されており、ドキュメントの一貫性が保たれています。この修正は、特にデベロッパーに対して必要な権限を明確に理解させ、誤解を避けるために重要です。

結果として、ユーザーはAzure OpenAIのリソースを利用するための適切なロールを把握しやすくなります。

## articles/ai-services/openai/how-to/prompt-caching.md{#item-1631df}

<details>
<summary>Diff</summary>
````diff
@@ -22,6 +22,7 @@ Caches are typically cleared within 5-10 minutes of inactivity and are always re
 
 Currently only the following models support prompt caching with Azure OpenAI:
 
+- `o1-2024-12-17`
 - `o1-preview-2024-09-12`
 - `o1-mini-2024-09-12`
 - `gpt-4o-2024-05-13`
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サポートされるモデルの追加"
}
```

### Explanation
この変更は、Azure OpenAI に関する「プロンプトキャッシング」ドキュメントの更新であり、主にサポートされるモデルに1つの追加が行われました。以下のポイントが特徴です。

1. **モデルの追加**: プロンプトキャッシングをサポートするモデルのリストに、「o1-2024-12-17」という新しいモデルが加えられました。これにより、ユーザーは最新のモデルについての情報を得られるようになります。

2. **他のモデルの維持**: 既存のモデル（`o1-preview-2024-09-12`、`o1-mini-2024-09-12`、`gpt-4o-2024-05-13`）は引き続きリストに記載されており、ユーザーに対して、どのモデルがプロンプトキャッシングを使用できるかを明確に示しています。

3. **情報の鮮度向上**: 新しいモデルの追加は、利用者が新しい機能や使用可能なリソースを把握し、適切な選択を行うために重要です。

この更新は、ユーザーが最新の情報をもとにキャッシング機能を利用する際に役立つ、非常に小さなが重要な改善となっています。

## articles/ai-services/openai/how-to/realtime-audio.md{#item-482ba3}

<details>
<summary>Diff</summary>
````diff
@@ -44,15 +44,10 @@ Before you can use GPT-4o real-time audio, you need:
 - An Azure OpenAI resource created in a [supported region](#supported-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](create-resource.md).
 - You need a deployment of the `gpt-4o-realtime-preview` model in a supported region as described in the [supported models](#supported-models) section. You can deploy the model from the [Azure AI Foundry portal model catalog](../../../ai-studio/how-to/model-catalog-overview.md) or from your project in AI Foundry portal. 
 
-For steps to deploy and use the `gpt-4o-realtime-preview` model, see [the real-time audio quickstart](../realtime-audio-quickstart.md).
-
-For more information about the API and architecture, see the remaining sections in this guide.
-
-## Sample code
-
-Right now, the fastest way to get started development with the GPT-4o Realtime API is to download the sample code from the [Azure OpenAI GPT-4o real-time audio repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk).
-
-[The Azure-Samples/aisearch-openai-rag-audio repo](https://github.com/Azure-Samples/aisearch-openai-rag-audio) contains an example of how to implement RAG support in applications that use voice as their user interface, powered by the GPT-4o realtime API for audio.
+Here are some of the ways you can get started with the GPT-4o Realtime API for speech and audio:
+- For steps to deploy and use the `gpt-4o-realtime-preview` model, see [the real-time audio quickstart](../realtime-audio-quickstart.md).
+- Download the sample code from the [Azure OpenAI GPT-4o real-time audio repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk).
+- [The Azure-Samples/aisearch-openai-rag-audio repo](https://github.com/Azure-Samples/aisearch-openai-rag-audio) contains an example of how to implement RAG support in applications that use voice as their user interface, powered by the GPT-4o realtime API for audio.
 
 ## Connection and authentication
 
@@ -269,6 +264,16 @@ sequenceDiagram
   Server->>Client: conversation.item.deleted
 -->
 
+## Response interuption
+
+The client [`response.cancel`](../realtime-audio-reference.md#realtimeclienteventresponsecancel) event is used to cancel an in-progress response. 
+
+A user might want to interrupt the assistant's response or ask the assistant to stop talking. The server produces audio faster than realtime. The client can send a [`conversation.item.truncate`](../realtime-audio-reference.md#realtimeclienteventconversationitemtruncate) event to truncate the audio before it's played. 
+- The server's understanding of the audio with the client's playback is synchronized. 
+- Truncating audio deletes the server-side text transcript to ensure there isn't text in the context that the user doesn't know about.
+- The server responds with a [`conversation.item.truncated`](../realtime-audio-reference.md#realtimeservereventconversationitemtruncated) event.
+
+
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオAPIに関するガイドの更新"
}
```

### Explanation
この変更は、Azure OpenAI の「リアルタイムオーディオ」に関するドキュメントの更新で、いくつかの新情報が追加され、既存の内容が整理されました。以下のポイントが主な特徴です。

1. **情報の整理**: リアルタイムオーディオAPIを使用するための手順が明確に整理され、よりスムーズに始められるようになっています。具体的には、新たに「ここから始める方法」というセクションが追加され、必要なリソースの構成やサンプルコードのダウンロードリンクが示されています。

2. **新しいセクションの追加**: 「レスポンスの中断」に関する新しいセクションが追加され、ユーザーがリアルタイムに音声応答を中断したり、アシスタントに話をやめさせる方法が説明されています。この新情報により、ユーザーはより柔軟にAPIを使用できるようになります。

3. **サンプルコードの取得方法**: サンプルコードに関する記述が簡潔にまとめられ、GitHub上でのコード取得方法へのリンクも強調されています。また、RAG（Retrieval-Augmented Generation）サポートの実装例についても言及されています。

4. **全体的な流れの改善**: この更新により、ドキュメントの流れが改善され、ユーザーが知りたい情報に迅速にアクセスできるようになっています。これにより、AIを利用した音声インターフェースの統合が円滑に進むことが期待されます。

この変更は、ユーザーがリアルタイムオーディオAPIを活用するためのガイドラインをさらに充実させた、重要な改善となっています。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,303 @@
+---
+title: Azure OpenAI o1 series reasoning models
+titleSuffix: Azure OpenAI
+description: Learn how to use Azure OpenAI's advanced o1 series reasoning models
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 12/17/2024
+author: mrbullwinkle    
+ms.author: mbullwin
+---
+
+
+# Azure OpenAI reasoning models
+
+Azure OpenAI `o1` and `o1-mini` models are designed to tackle reasoning and problem-solving tasks with increased focus and capability. These models spend more time processing and understanding the user's request, making them exceptionally strong in areas like science, coding, and math compared to previous iterations.
+
+**Key capabilities of the o1 series:**
+
+- Complex Code Generation: Capable of generating algorithms and handling advanced coding tasks to support developers.
+- Advanced Problem Solving: Ideal for comprehensive brainstorming sessions and addressing multifaceted challenges.
+- Complex Document Comparison: Perfect for analyzing contracts, case files, or legal documents to identify subtle differences.
+- Instruction Following and Workflow Management: Particularly effective for managing workflows requiring shorter contexts.
+
+## Availability
+
+The **o1 series** models are now available for API access and model deployment. **Registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who previously applied and received access to `o1-preview`, don't need to reapply as they are automatically on the wait-list for the latest model.
+
+Request access: [limited access model application](https://aka.ms/OAI/o1access)
+
+Once access has been granted, you'll need to create a deployment for each model. If you have an existing `o1-preview` deployment, in-place upgrade is currently not supported, you'll need to create a new deployment.
+
+### Region availability
+
+| Model | Region |
+|---|---|
+|`o1` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
+| `o1-preview` | See [models page](../concepts/models.md#global-standard-model-availability). |
+| `o1-mini` | See [models page](../concepts/models.md#global-standard-model-availability). |
+
+## API support
+
+Initial support for the **o1-preview** and **o1-mini** preview models was added in API version `2024-09-01-preview`. 
+
+As part of this release, the `max_tokens` parameter was deprecated and replaced with the new `max_completion_tokens` parameter. **o1 series** models will only work with the `max_completion_tokens` parameter.
+
+The latest most capable **o1 series** model is `o1` **Version: 2024-12-17**. This  general availability (GA) model should be used with API version `2024-12-01-preview`.
+
+### 2024-12-01-preview
+
+`2024-12-01-preview` adds support for the new `reasoning_effort` parameter, [structured outputs](./structured-outputs.md), and developer messages. The older preview reasoning models do not currently support these features. For reasoning models, these features are currently only available with `o1` **Version: 2024-12-17**.
+
+## Usage
+
+These models do not currently support the same set of parameters as other models that use the chat completions API. Only a limited subset is currently supported. Using standard parameters like `temperature` and `top_p` will result in errors.
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
+
+You will need to upgrade your OpenAI client library for access to the latest parameters.
+
+```cmd
+pip install openai --upgrade
+```
+
+If you are new to using Microsoft Entra ID for authentication see [How to configure Azure OpenAI Service with Microsoft Entra ID authentication](../how-to/managed-identity.md).
+
+```python
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
+  api_version="2024-12-01-preview"
+)
+
+response = client.chat.completions.create(
+    model="o1-new", # replace with the model deployment name of your o1-preview, or o1-mini model
+    messages=[
+        {"role": "user", "content": "What steps should I think about when writing my first Python API?"},
+    ],
+    max_completion_tokens = 5000
+
+)
+
+print(response.model_dump_json(indent=2))
+```
+
+# [Python (key-based auth)](#tab/python)
+
+You might need to upgrade your version of the OpenAI Python library to take advantage of the new parameters like `max_completion_tokens`.
+
+```cmd
+pip install openai --upgrade
+```
+
+```python
+
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
+  api_version="2024-12-01-preview"
+)
+
+response = client.chat.completions.create(
+    model="o1-new", # replace with the model deployment name of your o1 deployment.
+    messages=[
+        {"role": "user", "content": "What steps should I think about when writing my first Python API?"},
+    ],
+    max_completion_tokens = 5000
+
+)
+
+print(response.model_dump_json(indent=2))
+```
+
+---
+
+**Output:**
+
+```json
+{
+  "id": "chatcmpl-AEj7pKFoiTqDPHuxOcirA9KIvf3yz",
+  "choices": [
+    {
+      "finish_reason": "stop",
+      "index": 0,
+      "logprobs": null,
+      "message": {
+        "content": "Writing your first Python API is an exciting step in developing software that can communicate with other applications. An API (Application Programming Interface) allows different software systems to interact with each other, enabling data exchange and functionality sharing. Here are the steps you should consider when creating your first Python API...truncated for brevity.",
+        "refusal": null,
+        "role": "assistant",
+        "function_call": null,
+        "tool_calls": null
+      },
+      "content_filter_results": {
+        "hate": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "protected_material_code": {
+          "filtered": false,
+          "detected": false
+        },
+        "protected_material_text": {
+          "filtered": false,
+          "detected": false
+        },
+        "self_harm": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "sexual": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "violence": {
+          "filtered": false,
+          "severity": "safe"
+        }
+      }
+    }
+  ],
+  "created": 1728073417,
+  "model": "o1-2024-12-17",
+  "object": "chat.completion",
+  "service_tier": null,
+  "system_fingerprint": "fp_503a95a7d8",
+  "usage": {
+    "completion_tokens": 1843,
+    "prompt_tokens": 20,
+    "total_tokens": 1863,
+    "completion_tokens_details": {
+      "audio_tokens": null,
+      "reasoning_tokens": 448
+    },
+    "prompt_tokens_details": {
+      "audio_tokens": null,
+      "cached_tokens": 0
+    }
+  },
+  "prompt_filter_results": [
+    {
+      "prompt_index": 0,
+      "content_filter_results": {
+        "custom_blocklists": {
+          "filtered": false
+        },
+        "hate": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "jailbreak": {
+          "filtered": false,
+          "detected": false
+        },
+        "self_harm": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "sexual": {
+          "filtered": false,
+          "severity": "safe"
+        },
+        "violence": {
+          "filtered": false,
+          "severity": "safe"
+        }
+      }
+    }
+  ]
+}
+```
+
+
+
+> [!NOTE]
+> Reasoning models have `reasoning_tokens` as part of `completion_tokens_details` in the model response. These are hidden tokens that are not returned as part of the message response content but are used by the model to help generate a final answer to your request. `2024-12-01-preview` adds an additional new parameter `reasoning_effort` which can be set to `low`, `medium`, or `high` with the latest `o1` model. The higher the effort setting, the longer the model will spend processing the request, which will generally result in a larger number of `reasoning_tokens`.
+
+## Developer messages
+
+Functionally developer messages ` "role": "developer"` are the same as system messages.
+
+- **System messages are not supported** with the **o1 series** reasoning models. 
+- `o1-2024-12-17` with API version: `2024-12-01-preview` and later adds support for developer messages. 
+
+Adding a developer message to the previous code example would look as follows:
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
+
+You will need to upgrade your OpenAI client library for access to the latest parameters.
+
+```cmd
+pip install openai --upgrade
+```
+
+If you're new to using Microsoft Entra ID for authentication see [How to configure Azure OpenAI Service with Microsoft Entra ID authentication](../how-to/managed-identity.md).
+
+```python
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
+  api_version="2024-12-01-preview"
+)
+
+response = client.chat.completions.create(
+    model="o1-new", # replace with the model deployment name of your o1-preview, or o1-mini model
+    messages=[
+        {"role": "developer","content": "You are a helpful assistant."}, # optional equivalent to a system message for reasoning models 
+        {"role": "user", "content": "What steps should I think about when writing my first Python API?"},
+    ],
+    max_completion_tokens = 5000
+
+)
+
+print(response.model_dump_json(indent=2))
+```
+
+# [Python (key-based auth)](#tab/python)
+
+You might need to upgrade your version of the OpenAI Python library to take advantage of the new parameters like `max_completion_tokens`.
+
+```cmd
+pip install openai --upgrade
+```
+
+```python
+
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
+  api_version="2024-12-01-preview"
+)
+
+response = client.chat.completions.create(
+    model="o1-new", # replace with the model deployment name of your o1 deployment.
+    messages=[
+        {"role": "developer","content": "You are a helpful assistant."}, # optional equivalent to a system message for reasoning models 
+        {"role": "user", "content": "What steps should I think about when writing my first Python API?"},
+    ],
+    max_completion_tokens = 5000
+)
+
+print(response.model_dump_json(indent=2))
+```
+
+---
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIの推論モデルに関する新しいセクションの追加"
}
```

### Explanation
この変更は、Azure OpenAI の「推論モデル」に関する新しいドキュメントが追加されたことを示しています。このセクションは、`o1`と`o1-mini`モデルの機能や使用方法、APIのサポートについて詳しく解説しています。以下の要点が主な内容です。

1. **推論モデルの概要**: 新しいセクションでは、Azure OpenAI の推論モデルが複雑な問題解決やコーディングタスクにおいて強力な性能を発揮する旨が説明されています。これにより、科学、数学、プログラミングなどの分野での応用が期待されます。

2. **重要な機能**: このモデル群の主な特長として、複雑なコード生成、問題解決能力、文書比較、指示の実行とワークフロー管理が挙げられています。これにより、ユーザーは具体的なタスクへの適用方法を見込むことができます。

3. **利用可能性とアクセスポリシー**: モデルの利用には事前登録が必要で、既に`o1-preview`にアクセス権を持っているユーザーは自動的に最新モデルへのウェイトリストに載せられることが説明されています。

4. **APIサポートと変更点**: `o1`シリーズモデルは、特定のAPIバージョンで提供され、旧バージョンのパラメータは非推奨になったことが強調されています。また、新しいパラメータや機能も紹介され、開発者が新しいモデルを効果的に活用するための手順が提供されています。

5. **使用例とコードスニペット**: Pythonを用いた具体的な使用例が提示され、APIへのアクセス方法やモデルへのリクエストの作成方法が丁寧に解説されています。

この文書の追加により、Azure OpenAI の推論モデルの理解が深まり、開発者やユーザーがその機能を活用するための貴重な情報源となることが期待されます。

## articles/ai-services/openai/how-to/role-based-access-control.md{#item-4b9817}

<details>
<summary>Diff</summary>
````diff
@@ -62,6 +62,7 @@ A user with only this role assigned would be unable to:
 ❌ Create new model deployments or edit existing model deployments <br>
 ❌ Create/deploy custom fine-tuned models <br>
 ❌ Upload datasets for fine-tuning <br>
+❌ View, query, filter Stored completions data <br>
 ❌ Access quota <br>
 ❌ Create customized content filters <br>
 ❌ Add a data source for the use your data feature
@@ -72,6 +73,7 @@ This role has all the permissions of Cognitive Services OpenAI User and is also
 
 ✅ Create custom fine-tuned models <br>
 ✅ Upload datasets for fine-tuning <br>
+✅ View, query, filter Stored completions data <br>
 ✅ Create new model deployments or edit existing model deployments **[Added Fall 2023]**
 
 A user with only this role assigned would be unable to:
@@ -98,6 +100,8 @@ This role is typically granted access at the resource group level for a user in
 ✅ Create custom fine-tuned models **[Added Fall 2023]**<br>
 ✅ Upload datasets for fine-tuning **[Added Fall 2023]**<br>
 ✅ Create new model deployments or edit existing model deployments (via Azure AI Foundry) **[Added Fall 2023]**
+✅ View, query, filter Stored completions data <br>
+
 
 A user with only this role assigned would be unable to:
 
@@ -145,6 +149,7 @@ All the capabilities of Cognitive Services Contributor plus the ability to:
 |Create or edit model deployments|❌|✅|✅| ➖ |
 |Create or deploy custom fine-tuned models|❌|✅|✅| ➖ |
 |Upload datasets for fine-tuning|❌|✅|✅| ➖ |
+|View, query, filter Stored competions data|❌|✅|✅| ➖ |
 |Create new Azure OpenAI resources|❌|❌|✅| ➖ |
 |View/Copy/Regenerate keys under “Keys and Endpoint”|❌|❌|✅| ➖ |
 |Create customized content filters|❌|❌|✅| ➖ |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "役割ベースのアクセス制御ドキュメントの更新"
}
```

### Explanation
この変更は、役割ベースのアクセス制御に関するドキュメントに新たに情報が追加され、特定の機能についての明確化が図られています。以下は、主な更新内容です。

1. **新機能の追加**: 
   - ユーザーが「Stored completions data」を表示、クエリ、フィルタリングできる権限が新たに付与されました。この更新により、ユーザーは過去の応答データへのアクセスが可能になり、より効率的にデータを利用できるようになります。

2. **役割の権限強化**: 各役割に関連する権限が明確に整理され、特に「Cognitive Services OpenAI User」や「Cognitive Services Contributor」などの役割についての機能が強化されています。
   - 具体的には、カスタムファインチューニングモデルの作成、データセットのアップロード、新規モデルデプロイメントの作成や編集に関する権限が強調されています。

3. **特定の機能に関する注記**: ドキュメント内で追加情報として「Fall 2023」が明記され、これに該当する権限がいつから適用されるのかが示されています。

4. **情報の可視化**: 表形式で権限の有無を示すセクションが強化され、ユーザーはそれぞれの役割が持つ権限を一目で確認しやすくなっています。

この更新により、役割ベースのアクセス制御に関するガイドラインが一層明確になり、ユーザーが自分の権限を把握しやすくなることが期待されています。

## articles/ai-services/openai/how-to/structured-outputs.md{#item-cc2557}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 11/20/2024
+ms.date: 12/18/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -19,10 +19,9 @@ Structured outputs make a model follow a [JSON Schema](https://json-schema.org/o
 > [!NOTE]
 > * Currently structured outputs is not supported on [bring your own data](../concepts/use-your-data.md) scenario.
 
-
-
 ## Supported models
 
+- `o1` version: `2024-12-17`
 - `gpt-4o-mini` version: `2024-07-18`
 - `gpt-4o` version: `2024-08-06`
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "構造化出力に関するドキュメントの更新"
}
```

### Explanation
この変更は、構造化出力に関するドキュメントが更新され、いくつかの重要な情報が修正されています。以下は、主な変更点の概要です。

1. **日付の更新**: 最終更新日が「11/20/2024」から「12/18/2024」に変更され、文書の最新性が維持されています。

2. **モデルのサポート情報**: 
   - 構造化出力をサポートするモデルのリストが明確化され、新しいバージョンが追加されています。特に、新たに`o1`バージョン`2024-12-17`がサポートされることが明記されました。

3. **情報の整理**: 一部の不要な行が削除され、文書が簡潔になります。これにより、ユーザーが必要な情報を簡単に見つけやすくなっています。

4. **重要な注意書き**: 構造化出力が「持ち込みデータ」シナリオではサポートされていないことが強調されています。この情報は、ユーザーが利用できる機能を正確に理解するために重要です。

これらの変更により、構造化出力の使用に関する情報が整理され、ユーザーにとってより理解しやすくなりました。

## articles/ai-services/openai/includes/fine-tuning-openai-in-ai-studio.md{#item-723c8d}

<details>
<summary>Diff</summary>
````diff
@@ -221,6 +221,7 @@ Optionally, configure parameters for your fine-tuning job. The following are ava
 | `learning_rate_multiplier` | number | The learning rate multiplier to use for training. The fine-tuning learning rate is the original learning rate used for pre-training multiplied by this value. Larger learning rates tend to perform better with larger batch sizes. We recommend experimenting with values in the range 0.02 to 0.2 to see what produces the best results. A smaller learning rate may be useful to avoid overfitting. |
 |`n_epochs` | integer | The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset. If set to -1, the number of epochs is determined dynamically based on the input data. |
 |`seed` | integer | The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases. If a seed isn't specified, one will be generated for you. |
+| `Beta`| integer | Temperature parameter for the dpo loss, typically in the range 0.1 to 0.5. This controls how much attention we pay to the reference model. The smaller the beta, the more we allow the model to drift away from the reference model. As beta gets smaller the more, we ignore the reference model.  |
 
 You can choose to leave the default configuration or customize the values to your preference. After you finish making your configurations, select **Next**. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Studioにおけるファインチューニングの設定内容の更新"
}
```

### Explanation
この変更は、AI Studioにおけるファインチューニングの設定項目に関するドキュメントが更新され、新たに「Beta」パラメータに関する情報が追加されました。以下は、主な変更点の概要です。

1. **新しいパラメータの追加**:
   - 新しく「Beta」という温度パラメータが導入されました。これはdpoロスに関するもので、通常は0.1から0.5の範囲で設定されます。このパラメータは、参照モデルに対する注意の度合いを制御し、小さい値に設定することでモデルが参照モデルからどれだけ逸脱するかを調整します。説明には、値が小さくなるほど参照モデルを無視する傾向が強くなることが強調されています。

2. **情報の明確化**:
   - この新しい情報によって、ユーザーはファインチューニングの際に「Beta」パラメータがどのように機能するかを理解し、適切な範囲で設定することでモデルのパフォーマンス向上を図ることができるようになります。

全体として、この更新はファインチューニングのオプションに関する情報を補完し、ユーザーがより効果的にモデルをカスタマイズするための手助けとなることを目的としています。

## articles/ai-services/openai/includes/fine-tuning-studio.md{#item-439f1e}

<details>
<summary>Diff</summary>
````diff
@@ -288,6 +288,9 @@ The **Create custom model** wizard shows the parameters for training your fine-t
 | `learning_rate_multiplier` | number | The learning rate multiplier to use for training. The fine-tuning learning rate is the original learning rate used for pre-training multiplied by this value. Larger learning rates tend to perform better with larger batch sizes. We recommend experimenting with values in the range 0.02 to 0.2 to see what produces the best results. A smaller learning rate may be useful to avoid overfitting. |
 |`n_epochs` | integer | The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset. |
 | `seed` | integer | The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases. If a seed isn't specified, one will be generated for you|
+| `Beta`| integer | Temperature parameter for the dpo loss, typically in the range 0.1 to 0.5. This controls how much attention we pay to the reference model. The smaller the beta, the more we allow the model to drift away from the reference model. As beta gets smaller the more, we ignore the reference model.  |
+
+
 
 :::image type="content" source="../media/fine-tuning/studio-advanced-options.png" alt-text="Screenshot of the Advanced options pane for the Create custom model wizard, with default options selected." lightbox="../media/fine-tuning/studio-advanced-options.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングスタジオのパラメータの更新"
}
```

### Explanation
この変更は、ファインチューニングスタジオに関するドキュメントが更新され、いくつかの重要な情報が追加されました。以下は、主な変更点の概要です。

1. **新しいパラメータの追加**:
   - 「Beta」という新しい温度パラメータが導入されました。このパラメータはdpoロスに関連しており、通常は0.1から0.5の範囲で設定されます。Beta値が小さいほど、モデルが参照モデルから逸脱する許容度が高くなり、逆に大きいほど参照モデルに対する依存度が強くなります。この情報は、ファインチューニングを行う際の設定に特に重要です。

2. **画像の追加**:
   - ファインチューニングを行うウィザードの「高度なオプション」パネルのスクリーンショットが追加されました。これにより、ユーザーはオプションのデフォルト設定を視覚的に確認できるようになります。

3. **表の更新**:
   - ファインチューニングのためのパラメータの表に、追加された「Beta」パラメータが含まれています。これにより、ユーザーは様々なパラメータの意味や役割を一目で把握しやすくなっています。

全体として、この更新はファインチューニングスタジオの使い方に関する情報を補完し、ユーザーがより効果的にモデルをカスタマイズできるようサポートしています。

## articles/ai-services/openai/includes/gpt-v-dotnet.md{#item-120a68}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the .NET SDK'
+title: 'Quickstart: Use GPT-4 Turbo with Vision on your images with the .NET SDK'
 titleSuffix: Azure OpenAI
 description: Get started using the Azure OpenAI .NET SDK to deploy and use the GPT-4 Turbo with Vision model.
 services: cognitive-services
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turboに関するクイックスタートガイドのタイトル更新"
}
```

### Explanation
この変更は、GPT-4 Turboに関連するクイックスタートガイドのタイトルが更新されたことを示しています。具体的には、以下の変更が行われました。

1. **タイトルの修正**:
   - タイトルが「Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the .NET SDK」から「Quickstart: Use GPT-4 Turbo with Vision on your images with the .NET SDK」に修正されました。この変更により、ガイドの内容が画像と動画の両方ではなく、画像のみに焦点を当てていることが明確になりました。

2. **テキストの調整**:
   - タイトルの変更に伴い、情報がより正確にユーザーに伝わるようになったことで、混乱を避けることができます。

全体として、この更新は内容の整合性を保つためのものであり、ユーザーが必要な情報をより迅速に見つけることができるよう促進しています。

## articles/ai-services/openai/includes/gpt-v-javascript.md{#item-a128c9}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the JavaScript SDK'
+title: 'Quickstart: Use GPT-4 Turbo with Vision on your images with the JavaScript SDK'
 titleSuffix: Azure OpenAI
 description: Get started using the OpenAI JavaScript SDK to deploy and use the GPT-4 Turbo with Vision model.
 services: cognitive-services
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turboに関するクイックスタートガイドのタイトル更新"
}
```

### Explanation
この変更は、GPT-4 Turboに関連するクイックスタートガイドのタイトルが更新されたことを示しています。具体的には、以下の重要なポイントがあります。

1. **タイトルの変更**:
   - タイトルが「Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the JavaScript SDK」から「Quickstart: Use GPT-4 Turbo with Vision on your images with the JavaScript SDK」に修正されました。この変更により、ガイドの対象が画像のみであることが明確に示され、ユーザーが内容をより正確に理解できるようになっています。

2. **情報の整合性向上**:
   - タイトルの修正により、クイックスタートガイドの内容と一致する情報が提供されるため、混乱を避けることができます。

この更新は、ユーザーが必要な情報を迅速に取得する手助けとなることを目的としており、ドキュメントの品質向上に寄与しています。

## articles/ai-services/openai/includes/gpt-v-python.md{#item-366276}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the Python SDK'
+title: 'Quickstart: Use GPT-4 Turbo with Vision on your images with the Python SDK'
 titleSuffix: Azure OpenAI
 description: Get started using the Azure OpenAI Python SDK to deploy and use the GPT-4 Turbo with Vision model.
 services: cognitive-services
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turboに関するクイックスタートガイドのタイトル更新"
}
```

### Explanation
この変更は、GPT-4 Turboに関連するクイックスタートガイドのタイトルが更新されたことを示しています。具体的には、次の2つの主要な点があります。

1. **タイトルの改訂**:
   - タイトルが「Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the Python SDK」から「Quickstart: Use GPT-4 Turbo with Vision on your images with the Python SDK」に変更されました。この修正により、ガイドの内容が画像のみに限定されることが明示され、利用者の混乱を減らすことができます。

2. **情報の明確化**:
   - 新しいタイトルによって、クイックスタートガイドは画像に特化していることが強調され、ユーザーが必要な情報を迅速に見つけられるようになっています。

この変更は、ユーザー体験を向上させ、正確な情報を提供することを目的としています。

## articles/ai-services/openai/includes/gpt-v-rest.md{#item-65c91c}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the Azure OpenAI REST API'
+title: 'Quickstart: Use GPT-4 Turbo with Vision on your images with the Azure OpenAI REST API'
 titleSuffix: Azure OpenAI
 description: Get started using the Azure OpenAI REST APIs to deploy and use the GPT-4 Turbo with Vision model.
 services: cognitive-services
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turboに関するクイックスタートガイドのタイトル更新"
}
```

### Explanation
この変更は、GPT-4 Turboに関連するクイックスタートガイドのタイトルが更新されたことを示しています。主な変更点は次の通りです。

1. **タイトルの修正**:
   - タイトルが「Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the Azure OpenAI REST API」から「Quickstart: Use GPT-4 Turbo with Vision on your images with the Azure OpenAI REST API」に変更されました。この変更により、ガイドの対象が画像のみに明確に特定され、混乱を減らすことができます。

2. **情報の一貫性向上**:
   - タイトルの修正により、ガイドの内容とタイトルが一致し、ユーザーが必要な情報を効率よく見つけられるようになります。

この更新は、ユーザーの理解を深め、Azure OpenAI REST APIの使用に関する混乱を避けることを目的としています。

## articles/ai-services/openai/includes/gpt-v-studio.md{#item-dcd50e}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Quickstart: Use images and videos in chats with the Azure OpenAI Service'
+title: 'Quickstart: Use images in chats with the Azure OpenAI Service'
 titleSuffix: Azure OpenAI
 description: Use this article to get started using Azure AI Foundry to deploy and use an image-capable model.
 services: cognitive-services
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI Serviceに関するクイックスタートガイドのタイトル修正"
}
```

### Explanation
この変更は、Azure OpenAI Serviceに関連するクイックスタートガイドのタイトルが更新されたことを示しています。具体的には以下の点が挙げられます。

1. **タイトルの修正**:
   - タイトルが「Quickstart: Use images and videos in chats with the Azure OpenAI Service」から「Quickstart: Use images in chats with the Azure OpenAI Service」に変更されました。この修正により、ガイドの内容が画像に特化していることが強調され、ユーザーが求める情報を見つけやすくなります。

2. **明確さの向上**:
   - このタイトルの更新により、ユーザーはこのガイドが画像に関するものであることを迅速に理解でき、混乱を避けることができます。

この変更は、ユーザーがAzure AI Foundryを使用して画像対応モデルを展開するための準備を整えるサポートを強化することを目的としています。

## articles/ai-services/openai/includes/gpt-v-typescript.md{#item-03ec34}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the JavaScript SDK'
+title: 'Quickstart: Use GPT-4 Turbo with Vision on your images with the JavaScript SDK'
 titleSuffix: Azure OpenAI
 description: Get started using the OpenAI JavaScript SDK to deploy and use the GPT-4 Turbo with Vision model.
 services: cognitive-services
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKに関するクイックスタートガイドのタイトル修正"
}
```

### Explanation
この変更は、JavaScript SDKに関連するクイックスタートガイドのタイトルが更新されたことを示しています。具体的には、以下の点が明確に変更されました。

1. **タイトルの修正**:
   - タイトルが「Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the JavaScript SDK」から「Quickstart: Use GPT-4 Turbo with Vision on your images with the JavaScript SDK」に変更されました。この変更により、ガイドが画像の使用に特化していることがより明確に示されています。

2. **情報の鮮明さの向上**:
   - 画像とビデオ両方の使用が暗示されていたものが、画像のみの使用に焦点を当てることで、ユーザーが必要な情報をより早く理解できるようになります。

この更新は、OpenAI JavaScript SDKを使用してGPT-4 Turbo with Visionモデルをデプロイする際、ユーザーの混乱を減らし、より効果的にタスクを実行できるようサポートすることを目的としています。

## articles/ai-services/openai/media/apply-system-message.png{#item-ad3af6}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "システムメッセージの適用に関する画像のメタデータ更新"
}
```

### Explanation
この変更は、システムメッセージの適用に関する画像ファイルに関するもので、特に内容の変更はありませんが、メタデータが更新されている可能性があります。具体的には以下の点が考えられます。

1. **画像ファイルの更新**:
   - ファイル「apply-system-message.png」は変更されていないものの、GitHubリポジトリのバージョン管理により、画像が新しいバージョンとして再登録されたか、更新された情報に関連している可能性があります。これにより、公式なドキュメントやガイド内での使用状況が正確であることが保証されます。

2. **ドキュメントの整合性**:
   - 画像が含まれるドキュメントの一貫性を保つために、画像のメタデータやバージョン管理を行うことは重要です。この更新によって、今後のユーザー向け資料の品質や整合性が確保されることが期待されます。

このような変更は、ユーザーが参考にする資料やガイドが最新のものであるよう努めるための重要なステップです。

## articles/ai-services/openai/media/fine-tuning/ai-studio/fine-tune-new.png{#item-60c08f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいファインチューニング画像のメタデータ更新"
}
```

### Explanation
この変更は、ファインチューニングに関する画像「fine-tune-new.png」に関連しています。具体的には、以下の点が挙げられます。

1. **画像の状態変更**:
   - 画像自体には追加や削除はなく、内容の変更もありませんが、リポジトリ内での管理上、画像が新しいバージョンとして再登録されたことが示唆されています。これにより、最新の資料に対する整合性が保たれることが期待されます。

2. **ドキュメント整備**:
   - 画像のメタデータが更新されることで、今後の使用において適切なリファレンスが保証され、ユーザーが資料を閲覧する際に利用可能な情報が最新であることが確認できます。

このような画像メタデータの更新は、公式なドキュメントやガイドの品質向上に寄与し、ユーザーが正確な情報にアクセスできるようにするための重要な手段です。

## articles/ai-services/openai/media/fine-tuning/preference-optimization.gif{#item-6b0b5a}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しいファインチューニング用画像の追加"
}
```

### Explanation
この変更は、ファインチューニングに関連する新しい画像ファイル「preference-optimization.gif」の追加を示しています。具体的には以下の点が特徴です。

1. **新しい画像ファイルの追加**:
   - 新たに追加された「preference-optimization.gif」は、ファインチューニングに関する情報を視覚的に表現したもので、ドキュメントをより分かりやすくする役割を果たします。この画像は、ユーザーに対する説明や理解を助けるための重要なリソースとなります。

2. **説明の充実**:
   - 画像が追加されることにより、特定のコンセプトやプロセスに対する視覚的な説明が充実し、利用者がファインチューニングの手法や効果についてより簡単に理解できるようになるでしょう。

こうした新機能、すなわち新しい画像の追加は、ドキュメント全体の質を向上させ、ユーザーエクスペリエンスを向上させるための重要なステップです。ドキュメントに視覚的要素が加わることで、より多くの情報を効果的に伝えることができます。

## articles/ai-services/openai/media/how-to/content-detection.png{#item-d8de97}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツ検出画像のメタデータ更新"
}
```

### Explanation
この変更は、「content-detection.png」という画像に関連しています。主な内容は以下の通りです。

1. **画像の状態変更**:
   - 具体的な内容の変更は行われていませんが、画像のメタデータや管理情報として、何らかの理由で画像が更新されたことが示されています。これにより、古い情報を排除し、最新の資料に整合性を持たせる意図があります。

2. **ドキュメントの維持**:
   - 画像のメタデータの更新は、将来的な文書管理や整合性の観点から重要です。これにより、ユーザーがドキュメントを利用する際に、内容が正確であることが保証されます。

このようなマイナーな更新は、全体的なドキュメントの品質を向上させ、ユーザーが信頼性のある情報にアクセスできるようにするための重要なステップです。新しい情報源が追加されるわけではありませんが、既存の情報の整備が行われることによって、より良いユーザーエクスペリエンスを提供することが期待されます。

## articles/ai-services/openai/media/how-to/global-batch/create-batch-job-empty.png{#item-8d7507}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチジョブ作成画面の画像更新"
}
```

### Explanation
この変更は、「create-batch-job-empty.png」という画像に関するもので、以下の要点があります。

1. **画像の状態変更**:
   - 具体的なコンテンツの変化はないものの、画像に関連する情報の更新が行われたことを示しています。この更新は、ドキュメントにおける画像の管理やリンクの整理目的で行われている可能性があります。

2. **資料の一貫性向上**:
   - 画像の更新は、特に技術文書において重要です。情報が最新のものに保たれることで、読者が誤解なく内容を理解しやすくなるため、文書の信頼性が向上します。

このようなマイナーな更新は、ドキュメント全体の整合性を保つために不可欠であり、ユーザーが求める正確で最新な情報へのアクセスを促進します。特に技術的なプロセスを説明する資料では、正確な情報が求められるため、この更新の重要性は高いといえます。

## articles/ai-services/openai/media/how-to/real-time/real-time-playground.png{#item-a36b1d}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムプレイグラウンド画像の更新"
}
```

### Explanation
この変更は、「real-time-playground.png」という画像に関連しており、以下のポイントがあります。

1. **画像の状態変更**:
   - 画像自体の内容には変更はなく、また追加や削除もされていないため、メタデータやファイルの管理に関する更新であると考えられます。このような変更は、ドキュメントの運用を円滑にするために重要です。

2. **ドキュメントの品質向上**:
   - 技術的な文書において、画像は視覚的な情報を提供する重要な要素です。定期的に画像の管理や更新を行うことで、ユーザーがアクセスする情報の信頼性を保つことができます。これにより、ユーザーは最新で正確な情報を得ることができ、全体的な使用体験が向上します。

このようなマイナーな更新は、特に技術文書や教育資料において、情報の正確性を保つために非常に重要です。ユーザーが目的の情報を迅速に取得しやすくするための基盤を築いています。

## articles/ai-services/openai/media/navigate-chat-playground.png{#item-80edd6}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットプレイグラウンド画像の更新"
}
```

### Explanation
この変更は、「navigate-chat-playground.png」という画像に関するもので、以下の点に焦点を当てています。

1. **画像の状態変更**:
   - 具体的な変更や追加、削除は行われていないものの、ファイルの管理やリンクの更新が行われていると思われます。このようなマイナーな更新は、ドキュメントの整合性を保つのに役立ちます。

2. **ユーザー体験の向上**:
   - 技術的な資料やガイドにおいて、画像は情報を視覚化し理解を助ける重要な要素です。定期的に画像を見直し、管理することで、ユーザーはより明確で正確な情報を得ることができ、全体的な体験が向上します。

このようなマイナーな更新は、特にドキュメントの品質を保つために不可欠です。ユーザーが最新の情報にアクセスできるようにすることで、信頼性のある情報源としての役割を果たしています。

## articles/ai-services/openai/media/navigate-system-message.png{#item-f8571e}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "システムメッセージ画像の更新"
}
```

### Explanation
この変更は、「navigate-system-message.png」という画像に関連しており、以下の要点があります。

1. **画像の状態変更**:
   - この変更では、ファイルの具体的な内容に変更はなく、追加や削除もされていません。これは画像のメタデータや管理に関するマイナーな更新であると考えられます。

2. **ドキュメントの整合性保持**:
   - 技術的な文書において、正確な情報を提供するために画像の管理は重要です。画像を定期的に見直すことにより、ユーザーは情報が最新であることを確認でき、信頼性のある資料としての価値が高まります。

画像は視覚的に情報を伝えるための重要な要素であり、特に技術的なガイドやリファレンス文書においては、その重要性が増します。この更新により、ユーザーは最新の情報へ容易にアクセスでき、自信を持って利用できる内容が提供されます。

## articles/ai-services/openai/media/provisioned/deployment-screen.jpg{#item-5ce772}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメント画面画像の削除"
}
```

### Explanation
この変更は、「deployment-screen.jpg」という画像が削除されたことを示しています。以下のポイントに注目することができます。

1. **画像の削除**:
   - この変更では、特定の画像が文書から削除されたことを示しており、これは更新されたコンテンツにおける整理の一環と考えられます。画像の削除は、内容の relevancy（関連性）や精度を向上させるために行われることがあります。

2. **内容の精査**:
   - 不要な画像や情報を削除することは、技術文書の整合性と信頼性を保つために重要です。ユーザーに対して最新の、かつ正確な情報を提供するためのストラテジーの一部と言えるでしょう。

この変更は、文書のクオリティと利用するユーザー体験を向上させる手段として行われていると理解できます。不要な情報を取り除くことにより、より焦点を当てた内容を提供し、利用者が必要な情報をより迅速に得られるようになります。

## articles/ai-services/openai/media/provisioned/ptu-quota-page.png{#item-aedb7d}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PTUクオーターページ画像の更新"
}
```

### Explanation
この変更は、「ptu-quota-page.png」という画像に関連しており、以下の点が考えられます。

1. **画像の状態変更**:
   - この変更では、画像自体に対して具体的な追加や削除は行われていませんが、ファイルの更新が実施されたことを示しています。このファイルの役割は、PTU（プランニングとテストのユニット）に関する情報を視覚的に伝えることです。

2. **ドキュメントの信頼性向上**:
   - 画像の更新は、文書の情報が最新かつ正確であることを保証するために不可欠です。画像は、ユーザーが理解しやすい形式で情報を提示する手段であり、適切な更新を行うことで、読者にとっての価値が向上します。

この変更は、「ptu-quota-page.png」が文書において正確で信頼できる情報提供を続けるための重要なステップです。ユーザーは、現行の情報に基づいて正しい判断を下すことができるため、このような更新は非常に意義があります。

## articles/ai-services/openai/media/quota/quota-new.png{#item-9f797f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クオーターニュー画像の更新"
}
```

### Explanation
この変更は、「quota-new.png」という画像の更新に関するもので、以下の点に注目できます。

1. **画像更新の重要性**:
   - 「quota-new.png」は、クオータープランに関連する情報を視覚的に提供する役割を担っています。このファイルの更新は、情報が最新であることを保証するために行われます。画像が新しいデータや視覚的な改善を反映している可能性があり、ユーザーに対してより有益な情報を提供することが期待されます。

2. **信頼性とユーザーエクスペリエンス**:
   - 技術文書において画像の最新性を保つことは、ユーザーエクスペリエンスを向上させる重要な要素です。更新された画像が導入されることにより、ユーザーは最新の情報や状況を理解しやすくなり、意思決定を行いやすくなります。

このように、この変更は文書の質を向上させるための重要な施策の一環であり、利用者に対する情報の信頼性を高める役割を果たしています。

## articles/ai-services/openai/media/review-system-message.png{#item-9a1b06}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レビューシステムメッセージ画像の更新"
}
```

### Explanation
この変更は、「review-system-message.png」という画像の更新に関するものであり、以下のポイントが挙げられます。

1. **画像の目的**:
   - 「review-system-message.png」は、システムメッセージのレビュープロセスやそれに関連する情報を視覚的に示すための画像です。画像が適切に更新されることで、情報の正確性が保たれ、ユーザーが理解しやすい状態が維持されます。

2. **最新情報の提供**:
   - この更新は、ユーザーに対して最新の情報を提供し続けるために重要です。特に、AIサービスやその関連機能についてのガイドラインやヘルプドキュメントにおいて、更新された画像はユーザーが正しい理解を持つために役立ちます。

3. **ドキュメントの整合性**:
   - 更新された画像は、全体的な文書の整合性やプロフェッショナリズムを向上させる要素でもあります。視覚的な一貫性があることは、特に技術文書において重要で、読者の信頼を得るために寄与します。

このように、この変更は文書の質を高め、ユーザーが情報を正確に理解する助けとなることを目的としています。

## articles/ai-services/openai/media/select-system-message.png{#item-80fc6b}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セレクトシステムメッセージ画像の更新"
}
```

### Explanation
この変更は、「select-system-message.png」という画像の更新に関するものであり、以下の点が重要です。

1. **画像の役割**:
   - 「select-system-message.png」は、ユーザーがシステムメッセージを選択する際に参考となるビジュアルガイドです。システムの動作や機能を視覚的に説明することで、ユーザーの理解を助ける役割を果たしています。

2. **情報の正確性の確保**:
   - この画像が更新されることにより、最新の情報や変更が反映されます。AIサービスに関連する文書において、情報が古いままだとユーザーに誤解を招く可能性があるため、定期的な更新が重要です。

3. **ユーザーエクスペリエンスの向上**:
   - 視覚的な情報が最新のものであることは、ユーザーエクスペリエンスを向上させます。明確で一貫性のある視覚的資料は、ユーザーが必要な情報を迅速に得られるようにするために不可欠です。

このように、この変更はドキュメントの質を高め、ユーザーに対する理解の促進を目的としています。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -7,20 +7,20 @@ author: mrbullwinkle
 ms.author: mbullwin
 ms.service: azure-ai-openai
 ms.topic: overview
-ms.date: 08/14/2024
+ms.date: 12/15/2024
 ms.custom: build-2023, build-2023-dataai
 recommendations: false
 ---
 
 # What is Azure OpenAI Service?
 
-Azure OpenAI Service provides REST API access to OpenAI's powerful language models including o1-preview, o1-mini, GPT-4o, GPT-4o mini, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, image understanding, semantic search, and natural language to code translation. Users can access the service through REST APIs, Python SDK, or in the [Azure AI Foundry](https://ai.azure.com).
+Azure OpenAI Service provides REST API access to OpenAI's powerful language models including o1, o1-mini, GPT-4o, GPT-4o mini, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, image understanding, semantic search, and natural language to code translation. Users can access the service through REST APIs, Python SDK, or in the [Azure AI Foundry](https://ai.azure.com).
 
 ### Features overview
 
 | Feature | Azure OpenAI |
 | --- | --- |
-| Models available | **o1-preview** & **o1-mini** - (Limited Access - [Request Access](https://aka.ms/oai/modelaccess))<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
+| Models available | **o1** & **o1-mini** - (Limited Access - [Request Access](https://aka.ms/OAI/o1access))<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
 | Fine-tuning | `GPT-4o-mini` (preview) <br> `GPT-4` (preview) <br>`GPT-3.5-Turbo` (0613) <br> `babbage-002` <br> `davinci-002`.|
 | Price | [Available here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> For details on vision-enabled chat models, see the [special pricing information](../openai/concepts/gpt-with-vision.md#special-pricing-information).|
 | Virtual network support & private link support | Yes.  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスの概要の更新"
}
```

### Explanation
この変更は、「overview.md」ファイルに対する更新であり、主に以下の点が重要です。

1. **日付の更新**:
   - 文書内の日付が「08/14/2024」から「12/15/2024」に変更されました。これにより、情報がより最新の状態に保たれ、ユーザーに正確な時期を示すことができます。

2. **モデル名の修正**:
   - モデル名の一部が「o1-preview」から「o1」に修正されました。この変更により、ユーザーは現在利用可能なモデルの最新情報を得ることができます。

3. **ユーザーアクセス情報の、リンクの更新**:
   - 限定アクセスを持つモデルに対するアクセスリクエストのURLが修正されました。具体的には、アクセスリクエストのリンクが「https://aka.ms/oai/modelaccess」から「https://aka.ms/OAI/o1access」に変更されています。これにより、ユーザーは正しい情報に基づいて簡単にアクセスリクエストを行えるようになります。

4. **情報の一貫性の保持**:
   - 他のテーブルの情報は、機能の概要や料金情報、ファインチューニングのオプションなど、全体としての統一感を持たせるために整えられています。これにより、ユーザーが必要な情報を迅速に把握できるようになっています。

このように、変更内容は文書の正確性とユーザビリティの向上に寄与しており、特に最新の情報を提供することに重きを置いています。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -119,6 +119,8 @@ items:
     href: ./how-to/batch.md
   - name: Completions & chat completions
     items:
+    - name: Reasoning models
+      href: ./how-to/reasoning.md
     - name: GPT-35-Turbo & GPT-4 
       href: ./how-to/chatgpt.md
       displayName: ChatGPT, chatgpt
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次に推論モデルのセクションを追加"
}
```

### Explanation
この変更は、「toc.yml」ファイルに対する更新であり、主に以下の点が重要です。

1. **新しいセクションの追加**:
   - 目次に「Reasoning models」という新しいセクションが追加されました。このセクションは、推論モデルに関する情報を提供するためのもので、ユーザーが関連するコンテンツにアクセスしやすくなります。

2. **リンクの設定**:
   - 新たに追加された「Reasoning models」セクションには、関連するコンテンツへのリンクが設定されています。このリンクは「./how-to/reasoning.md」に向けられており、ユーザーは推論モデルに関する具体的な手順や説明を簡単に参照できるようになります。

3. **全体の構成の向上**:
   - 目次に新しい情報を追加することにより、ユーザーはAIサービスに関連するさまざまなトピックを迅速に見つけることができ、情報の検索や学習が効率的になります。

このように、この更新は文書の可読性およびユーザーエクスペリエンスを向上させ、特に推論モデルに関する知識を深める手助けをすることを目的としています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: whats-new
-ms.date: 11/16/2024
+ms.date: 11/18/2024
 recommendations: false
 ---
 
@@ -21,6 +21,30 @@ This article provides a summary of the latest releases and major documentation u
 
 ## December 2024
 
+### o1 reasoning model released for limited access
+
+The latest `o1` model is now available for API access and model deployment. **Registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who previously applied and received access to `o1-preview`, don't need to reapply as they are automatically on the wait-list for the latest model.
+
+Request access: [limited access model application](https://aka.ms/OAI/o1access)
+
+To learn more about the advanced `o1` series models see, [getting started with o1 series reasoning models](./how-to/reasoning.md).
+
+### Region availability
+
+| Model | Region |
+|---|---|
+|`o1` <br>(Version: 2024-12-17)| East US2 (Global Standard) <br> Sweden Central (Global Standard) |
+
+### Preference fine-tuning (preview)
+
+[Direct preference optimization (DPO)](./how-to/fine-tuning.md#direct-preference-optimization-dpo-preview) is a new alignment technique for large language models, designed to adjust model weights based on human preferences. Unlike reinforcement learning from human feedback (RLHF), DPO does not require fitting a reward model and uses simpler data (binary preferences) for training. This method is computationally lighter and faster, making it equally effective at alignment while being more efficient. DPO is especially useful in scenarios where subjective elements like tone, style, or specific content preferences are important. We’re excited to announce the public preview of DPO in Azure OpenAI Service, starting with the `gpt-4o-2024-08-06` model.
+
+For fine-tuning model region availability, see the [models page](./concepts/models.md#fine-tuning-models).
+
+### Stored completions & distillation
+
+[Stored completions](./how-to/stored-completions.md) allow you to capture the conversation history from chat completions sessions to use as datasets for [evaluations](./how-to/evaluations.md) and [fine-tuning](./how-to/fine-tuning.md).
+
 ### GPT-4o 2024-11-20
 
 `gpt-4o-2024-11-20` is now available for [global standard deployment](./how-to/deployment-types.md) in:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新のリリース情報の追加"
}
```

### Explanation
この変更は、「whats-new.md」ファイルに対する大規模な更新であり、主に以下の点が重要です。

1. **日付の更新**:
   - 文書内の日付が「11/16/2024」から「11/18/2024」に変更され、最新の連絡先情報を反映しています。

2. **新機能の追加**:
   - 「o1 reasoning model」が限定アクセスでリリースされたことが新たに追加されました。このモデルはAPIアクセスやモデルのデプロイメントが可能であり、登録が必要で、Microsoftの適格基準に基づいてアクセスが提供されることが明記されています。

3. **アクセスリクエストのリンク**:
   - 新モデルへのアクセスリクエストのためのリンクが提供され、「limited access model application」としてアクセス申請が可能です。既に「o1-preview」にアクセスしている顧客は、自動的に最新モデルの待機リストに入ることが説明されています。

4. **地域の可用性の詳細**:
   - 新たに「o1」モデルの地域別の可用性が表で示されています。これにより、ユーザーはどの地域で利用可能かを一目で把握できます。

5. **新しいファインチューニング手法の紹介**:
   - 「Preference fine-tuning (preview)」として、直接的な好み最適化（DPO）が紹介され、これは大規模言語モデルの新しい調整手法であることが記されています。DPOは、より効率的に主観的な要素を調整できることが強調されています。

6. **ストレージ完了と蒸留に関する情報**:
   - 「Stored completions」機能が説明され、会話履歴を保存し、評価やファインチューニングのデータセットとして利用する方法が紹介されています。

これらの変更により、ユーザーは最新のモデルとその機能、地域の可用性、および新しいファインチューニング技術についての理解を深め、より効果的にAzure OpenAIサービスを活用できるようになります。


