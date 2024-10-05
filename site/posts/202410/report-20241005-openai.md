---
date: '2024-10-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7d913a4...MicrosoftDocs:1b56c27
summary: 今回の変更では、OpenAIモデルに関する文書に新たなAPIパラメータ`max_completion_tokens`が導入され、古い`max_tokens`パラメータが非推奨となりました。また、.NETに関連するクイックスタートガイドが複数追加され、特にGPT-4
  TurboやWhisperモデル用の.NET SDKの利用方法が詳しく説明されています。さらに、C#やテキストから音声への変換、コンテンツフィルターに関する図が新たに追加・更新された一方、一部の画像が削除され、視覚的なユーザー体験に影響を与える可能性があります。今回の変更は、API仕様の変更や.NET言語でのサポート拡充に重点を置いており、開発者が最新のフレームワークやサービスを効果的に活用できる情報整備が目的とされています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7d913a4...MicrosoftDocs:1b56c27){target="_blank"}

<format>
# Highlights

OpenAIモデル関連文書に新たなAPIパラメータ`max_completion_tokens`の導入と古い`max_tokens`パラメーターの非推奨化が記載された。また、.NET関連のクイックスタートガイドが複数追加され、特にGPT-4 Turbo用やWhisperモデル用の.NET SDK利用方法が詳述されている。新たにC#やテキストから音声への変換、コンテンツフィルター関連の図が追加・更新されている一方、一部の画像が削除されており、視覚的なユーザー体験に影響を及ぼす可能性がある。

## New features

- `max_completion_tokens`パラメーターの導入。
- 新しいC#ドキュメントと.NET SDKに関するクイックスタート追加。
- Global BatchとGlobal Provisionedモデルの新しいドキュメント。
- テキストから音声への変換機能に関する新しい.NETガイド追加。

## Breaking changes

- コンテンツフィルタリングに関する複数の画像の削除。

## Other updates

- 一部画像の更新や日付の更新を含む細かな文書の改善。
- 各プログラミング言語用のクイックスタートガイドの整理と.NET対応の拡充。

# Insights

今回の変更はAzure OpenAIサービスの文書におけるAPI仕様の変更や.NET言語対応の拡充に焦点が当たっており、開発者がより最新のフレームワークやサービスを効果的に活用できるよう情報を整備する目的が感じられます。特に新たに追加された`max_completion_tokens`パラメーターはAPI使用において重要な役割を果たす一方、古い`max_tokens`パラメーターが非推奨になることで、ユーザーは新たな仕様への移行が求められるでしょう。

また、.NET クイックスタートガイドが複数追加され、.NETエコシステムとの統合が強化されています。これにより、特にC#ユーザーにとって非常に有用なリソースとなり、開発者によるAzure OpenAIサービスへのアクセスや利用が一層便利になります。

一方で、コンテンツフィルタリング関連の画像の削除により、特に初心者ユーザーが視覚的なガイダンスを得ることが難しくなる可能性があります。削除された画像に代わる新しい図や説明の強化が今後求められるでしょう。

全体として、今回の文書更新はAzure OpenAIサービスの最新機能を効果的に活用するための情報基盤を提供し、開発者がより迅速に能力を向上させるための支援を目的としていることが示されています。</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | モデルに関するドキュメントの更新 | modified | 176 | 117 | 293 | 
| [gpt-v-quickstart.md](#item-2a6183) | minor update | .NETクイックスタートの追加 | modified | 6 | 0 | 6 | 
| [batch.md](#item-a131d5) | minor update | バッチ処理に関するパフォーマンスの推奨事項の追加 | modified | 3 | 1 | 4 | 
| [content-filters.md](#item-6f0627) | minor update | コンテンツフィルターに関する手順の更新 | modified | 9 | 29 | 38 | 
| [fine-tuning.md](#item-5c0e85) | minor update | ファインチューニングに関する記事の日付更新 | modified | 1 | 1 | 2 | 
| [risks-safety-monitor.md](#item-b2be0b) | minor update | リスクと安全監視に関する記事の日付更新 | modified | 1 | 1 | 2 | 
| [structured-outputs.md](#item-cc2557) | minor update | Microsoft Entra IDに関する文の修正 | modified | 1 | 1 | 2 | 
| [assistants-csharp.md](#item-cc4697) | new feature | C# における新しいアシスタント機能の実装 | modified | 175 | 82 | 257 | 
| [fine-tuning-studio.md](#item-439f1e) | minor update | ファインチューニングスタジオのガイドラインの修正 | modified | 11 | 11 | 22 | 
| [gpt-4-turbo.md](#item-e233e0) | minor update | GPT-4 Turbo ドキュメントの軽微な修正 | modified | 1 | 5 | 6 | 
| [gpt-v-dotnet.md](#item-120a68) | new feature | GPT-4 Turbo with Visionの.NET SDKクイックスタートガイドの追加 | added | 122 | 0 | 122 | 
| [global-batch.md](#item-929e6a) | new feature | Global Batchモデルの可用性に関する新しいドキュメントの追加 | added | 15 | 0 | 15 | 
| [provisioned-global.md](#item-340884) | new feature | Global Provisionedモデルの可用性に関する新しいドキュメントの追加 | added | 37 | 0 | 37 | 
| [quota.md](#item-389aa1) | minor update | Quotaドキュメントの更新 | modified | 26 | 26 | 52 | 
| [standard-global.md](#item-17a84b) | new feature | Global Standardモデルの可用性に関する新しいドキュメントの追加 | added | 34 | 0 | 34 | 
| [standard-gpt-4.md](#item-d4064a) | minor update | Standard GPT-4モデルの可用性ドキュメントの更新 | modified | 2 | 2 | 4 | 
| [standard-models.md](#item-af04c4) | minor update | Standardモデルに関するドキュメントの変更 | modified | 21 | 22 | 43 | 
| [text-to-speech-dotnet.md](#item-fea66a) | new feature | テキストから音声への変換に関する.NETのガイド追加 | added | 112 | 0 | 112 | 
| [whisper-dotnet.md](#item-562a58) | new feature | Whisperモデルに関する.NETのガイド追加 | added | 111 | 0 | 111 | 
| [advanced.png](#item-634795) | breaking change | コンテンツフィルタリングに関する画像の削除 | removed | 0 | 0 | 0 | 
| [create-filter.jpg](#item-7c9550) | breaking change | コンテンツフィルタ作成に関する画像の削除 | removed | 0 | 0 | 0 | 
| [create-filter.png](#item-dc4d68) | new feature | コンテンツフィルタ作成に関する画像の追加 | added | 0 | 0 | 0 | 
| [delete.png](#item-db8934) | minor update | コンテンツフィルタ削除に関する画像の更新 | modified | 0 | 0 | 0 | 
| [edit-deployment.png](#item-9c1621) | minor update | コンテンツフィルタデプロイメント編集に関する画像の更新 | modified | 0 | 0 | 0 | 
| [filter-view.jpg](#item-794e84) | breaking change | コンテンツフィルタビュー画像の削除 | removed | 0 | 0 | 0 | 
| [filter-view.png](#item-027c18) | new feature | コンテンツフィルタビュー画像の追加 | added | 0 | 0 | 0 | 
| [multiple.png](#item-e633fb) | minor update | コンテンツフィルタのマルチビジュアルの修正 | modified | 0 | 0 | 0 | 
| [off.jpg](#item-7ca291) | breaking change | コンテンツフィルタのオフ状態画像の削除 | removed | 0 | 0 | 0 | 
| [select-filter.png](#item-dbe513) | minor update | コンテンツフィルタ選択画像の修正 | modified | 0 | 0 | 0 | 
| [settings.jpg](#item-8aadc0) | breaking change | コンテンツフィルタ設定画像の削除 | removed | 0 | 0 | 0 | 
| [severity-level.jpg](#item-5fce08) | breaking change | コンテンツフィルタの深刻度レベル画像の削除 | removed | 0 | 0 | 0 | 
| [studio.png](#item-343759) | minor update | コンテンツフィルタスタジオ画像の更新 | modified | 0 | 0 | 0 | 
| [models.png](#item-140ef7) | minor update | ファインチューニングモデル画像の更新 | modified | 0 | 0 | 0 | 
| [studio-advanced-options.png](#item-a35a88) | minor update | ファインチューニングスタジオの高度なオプション画像の更新 | modified | 0 | 0 | 0 | 
| [studio-continuous.png](#item-df67b2) | minor update | ファインチューニングスタジオの連続オプション画像の更新 | modified | 0 | 0 | 0 | 
| [studio-create-custom-model.png](#item-973d92) | minor update | カスタムモデル作成スタジオの画像更新 | modified | 0 | 0 | 0 | 
| [studio-model-details.png](#item-b997df) | minor update | モデル詳細スタジオの画像更新 | modified | 0 | 0 | 0 | 
| [studio-models-deploy-model.png](#item-6001dd) | minor update | モデルデプロイメントスタジオの画像更新 | modified | 0 | 0 | 0 | 
| [studio-models-deploy.png](#item-f8d724) | minor update | モデルデプロイメントに関する画像更新 | modified | 0 | 0 | 0 | 
| [studio-models-job-running.png](#item-695374) | minor update | ジョブ実行に関する画像更新 | modified | 0 | 0 | 0 | 
| [studio-review.png](#item-ee9fdd) | minor update | モデルレビューに関する画像更新 | modified | 0 | 0 | 0 | 
| [studio-training-data-blob.png](#item-a20ade) | minor update | トレーニングデータに関する画像更新 | modified | 0 | 0 | 0 | 
| [studio-training-data-local.png](#item-514edb) | minor update | ローカルトレーニングデータに関する画像更新 | modified | 0 | 0 | 0 | 
| [studio-training-data.png](#item-a1df9a) | minor update | ファインチューニングのためのトレーニングデータ画像更新 | modified | 0 | 0 | 0 | 
| [studio-validation-data-blob.png](#item-5a25bd) | minor update | バリデーションデータに関する画像更新 | modified | 0 | 0 | 0 | 
| [studio-validation-data-local.png](#item-042951) | minor update | ローカルバリデーションデータ画像の更新 | modified | 0 | 0 | 0 | 
| [studio-validation-data.png](#item-9541db) | minor update | ファインチューニング用バリデーションデータ画像の更新 | modified | 0 | 0 | 0 | 
| [content-detection.png](#item-d8de97) | minor update | コンテンツ検出用画像の更新 | modified | 0 | 0 | 0 | 
| [potentially-abusive-user.png](#item-f49240) | minor update | 潜在的に悪用されるユーザーに関する画像の更新 | modified | 0 | 0 | 0 | 
| [text-to-speech-quickstart.md](#item-c344ad) | minor update | テキスト読み上げクイックスタートの更新 | modified | 7 | 2 | 9 | 
| [whats-new.md](#item-53303b) | minor update | 最新情報の更新 | modified | 1 | 1 | 2 | 
| [whisper-quickstart.md](#item-4cae3d) | minor update | Whisperモデルのクイックスタートの更新 | modified | 7 | 1 | 8 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,175 @@ Once access has been granted, you will need to create a deployment for each mode
 
 Support for the **o1 series** models was added in API version `2024-09-01-preview`.
 
-The `max_tokens` parameter has been deprecated and replaced with the new `max_completion_tokens` parameter. **o1 series** models will only work with the `max_completions_tokens` parameter. 
+The `max_tokens` parameter has been deprecated and replaced with the new `max_completion_tokens` parameter. **o1 series** models will only work with the `max_completion_tokens` parameter.
+
+### Usage
+
+These models do not currently support the same set of parameters as other models that use the chat completions API. Only a very limited subset is currently supported, so common parameters like `temperature`, `top_p`, are not available and including them will cause your request to fail. `o1-preview` and `o1-mini` models will also not accept the system message role as part of the messages array.
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
+
+You may need to upgrade your version of the OpenAI Python library to take advantage of the new `max_completion_tokens` parameter.
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
+  api_version="2024-09-01-preview"
+)
+
+response = client.chat.completions.create(
+    model="o1-preview-new", # replace with the model deployment name of your o1-preview, or o1-mini model
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
+You may need to upgrade your version of the OpenAI Python library to take advantage of the new `max_completion_tokens` parameter.
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
+  api_version="2024-09-01-preview"
+)
+
+response = client.chat.completions.create(
+    model="o1-preview-new", # replace with the model deployment name of your o1-preview, or o1-mini model
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
+# [Output](#tab/python-output)
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
+        "content": "Writing your first Python API is an exciting step in developing software that can communicate with other applications. An API (Application Programming Interface) allows different software systems to interact with each other, enabling data exchange and functionality sharing. Here are the steps you should consider when creating your first Python API:\n\n1. **Define the Purpose and Requirements**\n\n   - **Identify the Functionality**: Clearly outline what your API is supposed to do. What data or services will it provide to the users?\n   - **Determine the Endpoints**: Plan the different URLs (endpoints) through which users can access the API functionalities.\n   - **Specify Request and Response Formats**: Decide on the data formats (usually JSON) for incoming requests and outgoing responses.\n\n2. **Choose the Right Framework**\n\n   Python offers several frameworks for building APIs. Two of the most popular are:\n\n   - **Flask**: A lightweight and flexible web framework, great for small to medium-sized APIs.\n   - **FastAPI**: A modern, high-performance framework for building APIs with Python 3.6+ types, offering automatic interactive documentation.\n\n   **Example**:\n   ```bash\n   pip install flask\n   ```\n   or\n   ```bash\n   pip install fastapi uvicorn\n   ```\n\n3. **Set Up the Development Environment**\n\n   - **Create a Virtual Environment**: Isolate your project dependencies using `venv` or `conda`.\n   - **Install Required Packages**: Ensure all necessary libraries and packages are installed.\n\n   **Example**:\n   ```bash\n   python -m venv env\n   source env/bin/activate  # On Windows use `env\\Scripts\\activate`\n   ```\n\n4. **Implement the API Endpoints**\n\n   - **Write the Code for Each Endpoint**: Implement the logic that handles requests and returns responses.\n   - **Use Decorators to Define Routes**: In frameworks like Flask, you use decorators to specify the URL endpoints.\n\n   **Example with Flask**:\n   ```python\n   from flask import Flask, request, jsonify\n\n   app = Flask(__name__)\n\n   @app.route('/hello', methods=['GET'])\n   def hello_world():\n       return jsonify({'message': 'Hello, World!'})\n\n   if __name__ == '__main__':\n       app.run(debug=True)\n   ```\n\n5. **Handle Data Serialization and Deserialization**\n\n   - **Parsing Incoming Data**: Use libraries to parse JSON or other data formats from requests.\n   - **Formatting Output Data**: Ensure that responses are properly formatted in JSON or XML.\n\n6. **Implement Error Handling**\n\n   - **Handle Exceptions Gracefully**: Provide meaningful error messages and HTTP status codes.\n   - **Validate Input Data**: Check for required fields and appropriate data types to prevent errors.\n\n   **Example**:\n   ```python\n   @app.errorhandler(404)\n   def resource_not_found(e):\n       return jsonify(error=str(e)), 404\n   ```\n\n7. **Add Authentication and Authorization (If Necessary)**\n\n   - **Secure Endpoints**: If your API requires, implement security measures such as API keys, tokens (JWT), or OAuth.\n   - **Manage User Sessions**: Handle user login states and permissions appropriately.\n\n8. **Document Your API**\n\n   - **Use Tools Like Swagger/OpenAPI**: Automatically generate interactive API documentation.\n   - **Provide Usage Examples**: Help users understand how to interact with your API.\n\n   **Example with FastAPI**:\n   FastAPI automatically generates docs at `/docs` using Swagger UI.\n\n9. **Test Your API**\n\n   - **Write Unit and Integration Tests**: Ensure each endpoint works as expected.\n   - **Use Testing Tools**: Utilize tools like `unittest`, `pytest`, or API testing platforms like Postman.\n\n   **Example**:\n   ```python\n   import unittest\n   class TestAPI(unittest.TestCase):\n       def test_hello_world(self):\n           response = app.test_client().get('/hello')\n           self.assertEqual(response.status_code, 200)\n   ```\n\n10. **Optimize Performance**\n\n    - **Improve Response Times**: Optimize your code and consider using asynchronous programming if necessary.\n    - **Manage Resource Utilization**: Ensure your API can handle the expected load.\n\n11. **Deploy Your API**\n\n    - **Choose a Hosting Platform**: Options include AWS, Heroku, DigitalOcean, etc.\n    - **Configure the Server**: Set up the environment to run your API in a production setting.\n    - **Use a Production Server**: Instead of the development server, use WSGI servers like Gunicorn or Uvicorn.\n\n    **Example**:\n    ```bash\n    uvicorn main:app --host 0.0.0.0 --port 80\n    ```\n\n12. **Monitor and Maintain**\n\n    - **Logging**: Implement logging to track events and errors.\n    - **Monitoring**: Use monitoring tools to track performance and uptime.\n    - **Update and Patch**: Keep dependencies up to date and patch any security vulnerabilities.\n\n13. **Consider Versioning**\n\n    - **Plan for Updates**: Use versioning in your API endpoints to manage changes without breaking existing clients.\n    - **Example**:\n      ```python\n      @app.route('/v1/hello', methods=['GET'])\n      ```\n\n14. **Gather Feedback and Iterate**\n\n    - **User Feedback**: Encourage users to provide feedback on your API.\n    - **Continuous Improvement**: Use the feedback to make improvements and add features.\n\n**Additional Tips**:\n\n- **Keep It Simple**: Start with a minimal viable API and expand functionality over time.\n- **Follow RESTful Principles**: Design your API according to REST standards to make it intuitive and standard-compliant.\n- **Security Best Practices**: Always sanitize inputs and protect against common vulnerabilities like SQL injection and cross-site scripting (XSS).\nBy following these steps, you'll be well on your way to creating a functional and robust Python API. Good luck with your development!",
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
+  "model": "o1-preview-2024-09-12",
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
+---
 
 ### Region availability
 
@@ -196,11 +364,9 @@ You can also use the OpenAI text to speech voices via Azure AI Speech. To learn
 
 [!INCLUDE [Standard Models](../includes/model-matrix/standard-models.md)]
 
-This table doesn't include [global standard](../how-to/deployment-types.md) model deployment regional availability for GPT-4o, or fine-tuning regional availability information.  Consult the dedicated [global standard deployment section](#global-standard-model-availability) and the [fine-tuning section](#fine-tuning-models) for this information.
-
-### Standard and global standard deployment model quota
+This table doesn't include fine-tuning regional availability information.  Consult the [fine-tuning section](#fine-tuning-models) for this information.
 
-[!INCLUDE [Quota](../includes/model-matrix/quota.md)]
+For information on default quota, refer to the [quota and limits article](../quotas-limits.md).
 
 ### Provisioned deployment model availability
 
@@ -209,126 +375,19 @@ This table doesn't include [global standard](../how-to/deployment-types.md) mode
 > [!NOTE]
 > The provisioned version of `gpt-4` **Version:** `turbo-2024-04-09` is currently limited to text only.
 
-### How do I get access to Provisioned?
-
-You need to speak with your Microsoft sales/account team to acquire provisioned throughput. If you don't have a sales/account team, unfortunately at this time, you cannot purchase provisioned throughput.
-
 For more information on Provisioned deployments, see our [Provisioned guidance](./provisioned-throughput.md).
 
 ### Global standard model availability
 
-`gpt-4o` **Version:** `2024-08-06`
-
-**Supported regions:**
-- eastus            
-- eastus2           
-- northcentralus    
-- southcentralus    
-- swedencentral     
-- westus            
-- westus3           
-
-`gpt-4o` **Version:** `2024-05-13`  
-
-**Supported regions:**
-
-- australiaeast     
-- brazilsouth       
-- canadaeast        
-- eastus            
-- eastus2           
-- francecentral     
-- germanywestcentral
-- japaneast         
-- koreacentral      
-- northcentralus    
-- norwayeast        
-- polandcentral
-- spaincentral     
-- southafricanorth  
-- southcentralus    
-- southindia        
-- swedencentral     
-- switzerlandnorth  
-- uksouth           
-- westeurope        
-- westus            
-- westus3           
-
-`gpt-4o-mini` **Version:** `2024-07-18`  
-
-**Supported regions:**
-
-- australiaeast     
-- brazilsouth       
-- canadaeast        
-- eastus            
-- eastus2           
-- francecentral     
-- germanywestcentral
-- japaneast         
-- koreacentral      
-- northcentralus    
-- norwayeast        
-- polandcentral
-- spaincentral     
-- southafricanorth  
-- southcentralus    
-- southindia        
-- swedencentral     
-- switzerlandnorth  
-- uksouth           
-- westeurope        
-- westus            
-- westus3           
-
-`gpt-4` **Version:** `turbo-2024-04-09`
-
-- australiaeast     
-- brazilsouth       
-- canadaeast        
-- eastus            
-- eastus2           
-- francecentral     
-- germanywestcentral
-- japaneast         
-- koreacentral      
-- northcentralus    
-- norwayeast        
-- polandcentral
-- spaincentral     
-- southafricanorth  
-- southcentralus    
-- southindia        
-- swedencentral     
-- switzerlandnorth  
-- uksouth           
-- westeurope        
-- westus            
-- westus3           
+[!INCLUDE [Standard Global](../includes/model-matrix/standard-global.md)]
 
-### Global batch model availability
-
-### Region and model support
+### Global provisioned managed model availability
 
-The following models support global batch:
+[!INCLUDE [Provisioned Managed Global](../includes/model-matrix/provisioned-global.md)]
 
-| Model | Version | Input format |
-|---|---|---|
-|`gpt-4o` | 2024-08-06 |text + image |
-|`gpt-4o-mini`| 2024-07-18 | text + image |
-|`gpt-4o` | 2024-05-13 |text + image |
-|`gpt-4` | turbo-2024-04-09 | text |
-|`gpt-4` | 0613 | text |
-| `gpt-35-turbo` | 0125 | text |
-| `gpt-35-turbo` | 1106 | text |
-| `gpt-35-turbo` | 0613 | text |
-
-Global batch is currently supported in the following regions:
+### Global batch model availability
 
-- East US
-- West US
-- Sweden Central
+[!INCLUDE [Global batch](../includes/model-matrix/global-batch.md)]
 
 ### GPT-4 and GPT-4 Turbo model availability
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルに関するドキュメントの更新"
}
```

### Explanation
この変更は、OpenAI モデルに関するドキュメント（`models.md`）の更新です。主な変更点として、API バージョン「2024-09-01-preview」で導入された新しいパラメーター `max_completion_tokens` の使用に関する詳細が追加され、古い `max_tokens` パラメーターの非推奨化が明記されました。また、新しいセクションが追加され、`o1` シリーズのモデルがサポートする有限なパラメーターセットについても言及され、一般的なパラメーター（`temperature` や `top_p` など）が現在サポートされていないことが説明されています。

さらに、Python による新しい使用例が導入され、OpenAI Python ライブラリのアップグレードに関する追加指示も含まれています。このライブラリを使用して、Azure OpenAI と通信するための具体的なコード例が示されています。ドキュメントの一部が削除され、一部が再整理されることで、情報が最新かつ明確になるよう努められています。

全体として、これらの更新は、ユーザーが新しい機能を活用し、既存の機能の変更に適応できるようにすることを目的としています。新しい情報に基づいたクリーンで効果的なデベロッパーエクスペリエンスの提供が強調されています。

## articles/ai-services/openai/gpt-v-quickstart.md{#item-2a6183}

<details>
<summary>Diff</summary>
````diff
@@ -45,6 +45,12 @@ Get started using GPT-4 Turbo with images with the Azure OpenAI Service.
 
 ::: zone-end
 
+::: zone pivot="programming-language-dotnet"
+
+[!INCLUDE [.NET quickstart](includes/gpt-v-dotnet.md)]
+
+::: zone-end
+
 ## Next steps
 
 * Learn more about these APIs in the [GPT-4 Turbo with Vision how-to guide](./gpt-v-quickstart.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": ".NETクイックスタートの追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスにおける GPT-4 Turbo の使用に関するクイックスタートドキュメント（`gpt-v-quickstart.md`）への追加を示しています。具体的には、プログラミング言語が `.NET` のセクションが新たに追加され、特に `.NET` を用いたクイックスタートのリンクが挿入されました。

変更点では、以下のような情報が追加されました：

- `.NET` に関連する新しいゾーンを定義し、その中に `.NET` 用のクイックスタートガイドへのリンクを含めたこと。
- これにより、ユーザーは `.NET` 環境でのセットアップと使用についてより具体的なガイダンスを受けられるようになりました。

このアップデートは、特に `.NET` 開発者が Azure OpenAI サービスを利用する際の利便性を向上させることを目的としています。ユーザーは新しいセクションを通じて、迅速に必要なリソースにアクセスできるようになります。

## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -83,7 +83,9 @@ In the Studio UI the deployment type will appear as `Global-Batch`.
 :::image type="content" source="../media/how-to/global-batch/global-batch.png" alt-text="Screenshot that shows the model deployment dialog in Azure OpenAI Studio with Global-Batch deployment type highlighted." lightbox="../media/how-to/global-batch/global-batch.png":::
 
 > [!TIP]
-> Each line of your input file for batch processing has a `model` attribute that requires a global batch **deployment name**. For a given input file, all names must be the same deployment name. This is different from OpenAI where the concept of model deployments does not exist.
+> Each line of your input file for batch processing has a `model` attribute that requires a global batch **deployment name**. For a given input file, all names must be the same deployment name. This is different from OpenAI where the concept of model deployments does not exist. 
+>
+> For the best performance we recommend submitting large files for patch processing, rather than a large number of small files with only a few lines in each file.
 
 ::: zone pivot="programming-language-ai-studio"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理に関するパフォーマンスの推奨事項の追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスにおけるバッチ処理に関するドキュメント（`batch.md`）の更新を示しています。具体的には、バッチ処理の入力ファイルで必要となる `model` 属性に関する説明が強化され、最適なパフォーマンスに関する新しい推奨事項が追加されました。

主な変更点は以下の通りです：

- バッチ処理用の入力ファイルの各行には、グローバルバッチの **デプロイメント名** が必要であるという内容が保持され、OpenAI との違いが再確認されています。
- 新たに追加された文では、最適なパフォーマンスを得るためには、大量の小さなファイルを処理するのではなく、大きなファイルを提出することを推奨しています。これにより、ユーザーはバッチ処理の効率を向上させることができます。

全体として、この更新は、ドキュメントの明確化とユーザーのバッチ処理経験を改善するための情報提供を目的としています。

## articles/ai-services/openai/how-to/content-filters.md{#item-6f0627}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ description: Learn how to use and configure the content filters that come with A
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 09/25/2024
+ms.date: 10/04/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -49,51 +49,31 @@ The following steps show how to set up a customized content filtering configurat
 
 1. Go to Azure OpenAI Studio and navigate to the Content Filters tab (in the bottom left navigation, as designated by the red box below).
 
-    :::image type="content" source="../media/content-filters/studio.png" alt-text="Screenshot of the AI Studio UI with Content Filters highlighted" lightbox="../media/content-filters/studio.png":::
+    :::image type="content" source="../media/content-filters/studio.png" alt-text="Screenshot of the AI Studio UI with Content Filters highlighted." lightbox="../media/content-filters/studio.png":::
 
 1. Create a new customized content filtering configuration.
 
-   :::image type="content" source="../media/content-filters/create-filter.jpg" alt-text="Screenshot of the content filtering configuration UI with create selected" lightbox="../media/content-filters/create-filter.jpg":::
+   :::image type="content" source="../media/content-filters/create-filter.png" alt-text="Screenshot of the content filtering configuration UI with create selected." lightbox="../media/content-filters/create-filter.png":::
 
-    This leads to the following configuration view, where you can choose a name for the custom content filtering configuration.
+    This leads to the following configuration view, where you can choose a name for the custom content filtering configuration. After entering a name, you can configure the **input filters** (user prompts) and **output filters** (model response). For the first four content categories there are three severity levels that are configurable: Low, medium, and high. You can use the sliders to set the severity threshold if you determine that your application or usage scenario requires different filtering than the default values. Some filters enable you to determine if the model should annotate and/or block. Selecting **Annotate** runs the respective model and return annotations via API response, but it will not filter content. In addition to annotations, you can also choose to filter content by switching the **Filter** toggle to on.
 
-    :::image type="content" source="../media/content-filters/filter-view.jpg" alt-text="Screenshot of the content filtering configuration UI" lightbox="../media/content-filters/filter-view.jpg":::
+    If your use case was approved for modified content filters as outlined above, you receive full control over content filtering configurations and can choose to turn filtering partially or fully off.
 
-1. This is the view of the default content filtering configuration, where content is filtered at medium and high severity levels for all categories. You can modify the content filtering severity level for both user prompts and model completions separately (configuration for prompts is in the left column and configuration for completions is in the right column, as designated with the blue boxes below) for each of the four content categories (content categories are listed on the left side of the screen, as designated with the green box below). There are three severity levels for each category that are configurable: Low, medium, and high. You can use the slider to set the severity threshold.
-
-    :::image type="content" source="../media/content-filters/severity-level.jpg" alt-text="Screenshot of the content filtering configuration UI with user prompts and model completions highlighted" lightbox="../media/content-filters/severity-level.jpg":::
-
-1. If you determine that your application or usage scenario requires  stricter filtering for some or all content categories, you can configure the settings, separately for prompts and completions, to filter at more severity levels than the default setting. An example is shown in the image below, where the filtering level for user prompts is set to the strictest configuration for hate and sexual, with low severity content filtered along with content classified as medium and high severity (outlined in the red box below). In the example, the filtering levels for model completions are set at the strictest configuration for all content categories (blue box below). With this modified filtering configuration in place, low, medium, and high severity content will be filtered for the hate and sexual categories in user prompts; medium and high severity content will be filtered for the self-harm and violence categories in user prompts; and low, medium, and high severity content will be filtered for all content categories in model completions.
-
-    :::image type="content" source="../media/content-filters/settings.jpg" alt-text="Screenshot of the content filtering configuration with low, medium, high, highlighted." lightbox="../media/content-filters/settings.jpg":::
-
-1. If your use case was approved for modified content filters as outlined above, you receive full control over content filtering configurations and can choose to turn filtering partially or fully off. In the image below, filtering is turned off for violence (green box below), while default configurations are retained for other categories. While this disabled the filter functionality for violence, content will still be annotated. To turn off all filters and annotations, toggle off Filters and annotations (red box below).
-
-    :::image type="content" source="../media/content-filters/off.jpg" alt-text="Screenshot of the content filtering configuration with self harm and violence set to off." lightbox="../media/content-filters/off.jpg":::
-
-    You can create multiple content filtering configurations as per your requirements.
-
-1. To turn on the optional models, you can select any of the checkboxes at the left hand side. When each of the optional models is turned on, you can indicate whether the model should Annotate or Filter.
-
-1. Selecting Annotate runs the respective model and return annotations via API response, but it will not filter content. In addition to annotations, you can also choose to filter content by switching the Filter toggle to on. 
+    :::image type="content" source="../media/content-filters/filter-view.png" alt-text="Screenshot of the content filtering configuration UI." lightbox="../media/content-filters/filter-view.png":::
 
 1. You can create multiple content filtering configurations as per your requirements.
 
     :::image type="content" source="../media/content-filters/multiple.png" alt-text="Screenshot of multiple content configurations in the Azure portal." lightbox="../media/content-filters/multiple.png":::
 
-1. Next, to make a custom content filtering configuration operational, assign a configuration to one or more deployments in your resource. To do this, go to the **Deployments** tab and select **Edit deployment** (outlined near the top of the screen in a red box below).
+1. Next, to make a custom content filtering configuration operational, assign a configuration to one or more deployments in your resource. To do this, go to the **Deployments** tab and select your deployment. Then select **Edit**.
 
     :::image type="content" source="../media/content-filters/edit-deployment.png" alt-text="Screenshot of the content filtering configuration with edit deployment highlighted." lightbox="../media/content-filters/edit-deployment.png":::
 
-1. Go to advanced options (outlined in the blue box below) select the content filter configuration suitable for that deployment from the **Content Filter** dropdown (outlined near the bottom of the dialog box in the red box below).
-
-    :::image type="content" source="../media/content-filters/advanced.png" alt-text="Screenshot of edit deployment configuration with advanced options selected." lightbox="../media/content-filters/advanced.png":::
-
-1. Select **Save and close** to apply the selected configuration to the deployment.
+1. In the **Update deployment** window that appears, select your custom filter from the **Content filter** dropdown menu. Then select **Save and close** to apply the selected configuration to the deployment.
 
     :::image type="content" source="../media/content-filters/select-filter.png" alt-text="Screenshot of edit deployment configuration with content filter selected." lightbox="../media/content-filters/select-filter.png":::
 
-1. You can also edit and delete a content filter configuration if required. To do this, navigate to the content filters tab and select the desired action (options outlined near the top of the screen in the red box below). You can edit/delete only one filtering configuration at a time.  
+1. You can also edit and delete a content filter configuration if required. To do this, navigate to the content filters tab and select a configuration. Then select the desired action. You can only edit one filtering configuration at a time.  
 
     :::image type="content" source="../media/content-filters/delete.png" alt-text="Screenshot of content filter configuration with edit and delete highlighted." lightbox="../media/content-filters/delete.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルターに関する手順の更新"
}
```

### Explanation
この変更は、Azure OpenAI サービスにおけるコンテンツフィルターの使用方法に関するドキュメント（`content-filters.md`）の更新を示しています。主な内容は、新しい手順の追加や、既存の情報の簡素化・明確化を目的として修正が行われています。

主な変更点は以下の通りです：

- ドキュメントの最初に、日付が更新され、最新の編集日を反映しました。
- コンテンツフィルターの設定方法に関する手順が再構築され、詳細な説明が新たに追加されました。特に、フィルターの入力や出力を設定する方法に関して、より具体的なガイダンスが提供されています。
- スクリーンショットの alt テキストが変更され、内容がより具体的に説明されるようになりました。これにより、視覚的にも情報が明確になります。
- 古い手順の一部が削除され、より効率的で簡約した手順に改善されました。特に、フィルター設定の実装方法や、その適用に関する流れが明確に示されています。

このように、全体的な構造の見直しが行われ、ユーザーがコンテンツフィルターの設定を行いやすくなるように配慮された内容となっています。

## articles/ai-services/openai/how-to/fine-tuning.md{#item-5c0e85}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: build-2023, build-2023-dataai, devx-track-python
 ms.topic: how-to
-ms.date: 09/05/2024
+ms.date: 10/03/2024
 author: mrbullwinkle
 ms.author: mbullwin
 zone_pivot_groups: openai-fine-tuning-new
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングに関する記事の日付更新"
}
```

### Explanation
この変更は、Azure OpenAI サービスにおけるファインチューニングに関するドキュメント（`fine-tuning.md`）の更新を示しています。主に、ドキュメントの更新日を変更することが目的です。

具体的には、以下のような変更が行われました：

- ドキュメントの最初にある日付が、もともと「2024年09月05日」から「2024年10月03日」に更新されました。これにより、読者は情報が最新であることを確認できます。

この変更は内容の追加や削除ではなく、日付の変更に留まるため、全体的な情報の正確性を確保することを意図しています。これにより、文書が最新の状態であることが維持され、ユーザーに正確な情報を提供する助けとなります。

## articles/ai-services/openai/how-to/risks-safety-monitor.md{#item-b2be0b}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: PatrickFarley
 ms.author: pafarley 
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 03/19/2024
+ms.date: 10/03/2024
 manager: nitinme
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リスクと安全監視に関する記事の日付更新"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関するリスクと安全監視の手法についてのドキュメント（`risks-safety-monitor.md`）の更新を示しています。変更の主な内容は、ドキュメント内の日付を更新することです。

具体的には、次のような変更が行われました：

- ドキュメントの最初にある日付が「2024年03月19日」から「2024年10月03日」に更新されました。この変更は、情報が最新であることを示すために重要です。

このような日付の更新は、全体の内容には変更がなく、ユーザーに正確で最新の状況を提供する手段として実施されており、ドキュメントの信頼性を高める役割を果たしています。

## articles/ai-services/openai/how-to/structured-outputs.md{#item-cc2557}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ You can use [`Pydantic`](https://docs.pydantic.dev/latest/) to define object sch
 pip install openai pydantic --upgrade
 ```
 
-If you new to using Microsoft Entra ID for authentication see [How to configure Azure OpenAI Service with Microsoft Entra ID authentication](./managed-identity.md).
+If you are new to using Microsoft Entra ID for authentication see [How to configure Azure OpenAI Service with Microsoft Entra ID authentication](./managed-identity.md).
 
 ```python
 from pydantic import BaseModel
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Microsoft Entra IDに関する文の修正"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関するドキュメント（`structured-outputs.md`）の一部文言を修正することを目的としています。具体的には、Microsoft Entra ID の認証に関連する部分の文章が明確に修正されています。

主な変更点は以下の通りです：

- 文章中の「If you new to using Microsoft Entra ID for authentication」が「If you are new to using Microsoft Entra ID for authentication」に修正されました。この変更により、文の文法が正しくなり、読者にとって理解しやすくなっています。

このようなマイナーな更新は、ドキュメントの正確性や可読性を向上させるために重要であり、ユーザーに対してより良い情報提供を行うことを目指しています。

## articles/ai-services/openai/includes/assistants-csharp.md{#item-cc4697}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: aapowell
 ms.author: aapowell
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 03/05/2024
+ms.date: 9/27/2024
 ---
 
 [Reference documentation](/dotnet/api/overview/azure/ai.openai.assistants-readme?context=/azure/ai-services/openai/context/context) |  [Source code](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/openai/Azure.AI.OpenAI/src) | [Package (NuGet)](https://www.nuget.org/packages/Azure.AI.OpenAI/)
@@ -24,123 +24,216 @@ ms.date: 03/05/2024
 
 ### Create a new .NET Core application
 
-In a console window (such as cmd, PowerShell, or Bash), use the `dotnet new` command to create a new console app with the name `azure-openai-quickstart`. This command creates a simple "Hello World" project with a single C# source file: *Program.cs*.
+1. In a console window (such as cmd, PowerShell, or Bash), use the [`dotnet new`](/dotnet/core/tools/dotnet-new) command to create a new console app with the name `azure-openai-quickstart`:
+    
+    ```dotnetcli
+    dotnet new console -n azure-openai-assistants-quickstart
+    ```
 
-```dotnetcli
-dotnet new console -n azure-openai-assistants-quickstart
-```
-
-Change your directory to the newly created app folder. You can build the application with:
+2. Change into the directory of the newly created app folder and build the app with the [`dotnet build`](/dotnet/core/tools/dotnet-build) command:
 
-```dotnetcli
-dotnet build
-```
+    ```dotnetcli
+    dotnet build
+    ```
 
-The build output should contain no warnings or errors.
+    The build output should contain no warnings or errors.
+    
+    ```output
+    ...
+    Build succeeded.
+     0 Warning(s)
+     0 Error(s)
+    ...
+    ```
 
-```output
-...
-Build succeeded.
- 0 Warning(s)
- 0 Error(s)
-...
-```
+3. Install the [OpenAI .NET client library](https://www.nuget.org/packages/Azure.AI.OpenAI/) with the [dotnet add package](/dotnet/core/tools/dotnet-add-package) command:
 
-Install the OpenAI .NET client library with:
-
-```console
-dotnet add package Azure.AI.OpenAI.Assistants --prerelease
-```
+    ```console
+    dotnet add package Azure.AI.OpenAI --prerelease
+    ```
 
 [!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
 
 [!INCLUDE [environment-variables](environment-variables.md)]
 
-## Create an assistant
+### Passwordless authentication is recommended
+
+Passwordless authentication is more secure than key-based alternatives and is the recommended approach for connecting to Azure services. If you choose Passwordless authentication, you'll need to complete the following:
 
-In our code we are going to specify the following values:
+1. Add the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package.
 
-| **Name** | **Description** |
-|:---|:---|
-| **Assistant name** | Your deployment name that is associated with a specific model. |
-| **Instructions** | Instructions are similar to system messages this is where you give the model guidance about how it should behave and any context it should reference when generating a response. You can describe the assistant's personality, tell it what it should and shouldn't answer, and tell it how to format responses. You can also provide examples of the steps it should take when answering responses. |
-| **Model** | This is where you set which model deployment name to use with your assistant. The retrieval tool requires `gpt-35-turbo (1106)` or `gpt-4 (1106-preview)` model. **Set this value to your deployment name, not the model name unless it is the same.** |
-| **Code interpreter** | Code interpreter provides access to a sandboxed Python environment that can be used to allow the model to test and execute code. |
+    ```dotnetcli
+    dotnet add package Azure.Identity
+    ```
 
-### Tools
+1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal on your OpenAI resource under **Access control (IAM)** > **Add role assignment**.
+1. Sign-in to Azure using Visual Studio or the Azure CLI via `az login`.
 
-An individual assistant can access up to 128 tools including `code interpreter`, as well as any custom tools you create via [functions](../how-to/assistant-functions.md).
+### Create the assistant
 
-Create and run an assistant with the following:
+Update the `Program.cs` file with the following code to create an assistant:
 
 ```csharp
 using Azure;
 using Azure.AI.OpenAI.Assistants;
 
-string endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT") ?? throw new ArgumentNullException("AZURE_OPENAI_ENDPOINT");
-string key = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY") ?? throw new ArgumentNullException("AZURE_OPENAI_API_KEY");
-AssistantsClient client = new AssistantsClient(new Uri(endpoint), new AzureKeyCredential(key));
-
-// Create an assistant
-Assistant assistant = await client.CreateAssistantAsync(
-    new AssistantCreationOptions("gpt-4-1106-preview") // Replace this with the name of your model deployment
+// Assistants is a beta API and subject to change
+// Acknowledge its experimental status by suppressing the matching warning.
+string endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
+string key = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
+
+var openAIClient = new AzureOpenAIClient(new Uri(endpoint), new AzureKeyCredential(key));
+
+// Use for passwordless auth
+//var openAIClient = new AzureOpenAIClient(new Uri(endpoint), new DefaultAzureCredential()); 
+
+FileClient fileClient = openAIClient.GetFileClient();
+AssistantClient assistantClient = openAIClient.GetAssistantClient();
+
+// First, let's contrive a document we'll use retrieval with and upload it.
+using Stream document = BinaryData.FromString("""
+            {
+                "description": "This document contains the sale history data for Contoso products.",
+                "sales": [
+                    {
+                        "month": "January",
+                        "by_product": {
+                            "113043": 15,
+                            "113045": 12,
+                            "113049": 2
+                        }
+                    },
+                    {
+                        "month": "February",
+                        "by_product": {
+                            "113045": 22
+                        }
+                    },
+                    {
+                        "month": "March",
+                        "by_product": {
+                            "113045": 16,
+                            "113055": 5
+                        }
+                    }
+                ]
+            }
+            """).ToStream();
+
+OpenAIFileInfo salesFile = await fileClient.UploadFileAsync(
+    document,
+    "monthly_sales.json",
+    FileUploadPurpose.Assistants);
+
+// Now, we'll create a client intended to help with that data
+AssistantCreationOptions assistantOptions = new()
+{
+    Name = "Example: Contoso sales RAG",
+    Instructions =
+        "You are an assistant that looks up sales data and helps visualize the information based"
+        + " on user queries. When asked to generate a graph, chart, or other visualization, use"
+        + " the code interpreter tool to do so.",
+    Tools =
+            {
+                new FileSearchToolDefinition(),
+                new CodeInterpreterToolDefinition(),
+            },
+    ToolResources = new()
     {
-        Name = "Math Tutor",
-        Instructions = "You are a personal math tutor. Write and run code to answer math questions.",
-        Tools = { new CodeInterpreterToolDefinition() }
-    });
-
-// Create a thread
-AssistantThread thread = await client.CreateThreadAsync();
-
-// Add a user question to the thread
-ThreadMessage message = await client.CreateMessageAsync(
-    thread.Id,
-    MessageRole.User,
-    "I need to solve the equation `3x + 11 = 14`. Can you help me?");
-
-// Run the thread
-ThreadRun run = await client.CreateRunAsync(
-    thread.Id,
-    new CreateRunOptions(assistant.Id)
-);
-
-// Wait for the assistant to respond
+        FileSearch = new()
+        {
+            NewVectorStores =
+                    {
+                        new VectorStoreCreationHelper([salesFile.Id]),
+                    }
+        }
+    },
+};
+
+Assistant assistant = await assistantClient.CreateAssistantAsync(deploymentName, assistantOptions);
+
+// Create and run a thread with a user query about the data already associated with the assistant
+ThreadCreationOptions threadOptions = new()
+{
+    InitialMessages = { "How well did product 113045 sell in February? Graph its trend over time." }
+};
+
+ThreadRun threadRun = await assistantClient.CreateThreadAndRunAsync(assistant.Id, threadOptions);
+
+// Check back to see when the run is done
 do
 {
-    await Task.Delay(TimeSpan.FromMilliseconds(500));
-    run = await client.GetRunAsync(thread.Id, run.Id);
-}
-while (run.Status == RunStatus.Queued
-    || run.Status == RunStatus.InProgress);
+    Thread.Sleep(TimeSpan.FromSeconds(1));
+    threadRun = assistantClient.GetRun(threadRun.ThreadId, threadRun.Id);
+} while (!threadRun.Status.IsTerminal);
 
-// Get the messages
-PageableList<ThreadMessage> messagesPage = await client.GetMessagesAsync(thread.Id);
-IReadOnlyList<ThreadMessage> messages = messagesPage.Data;
+// Finally, we'll print out the full history for the thread that includes the augmented generation
+AsyncCollectionResult<ThreadMessage> messages
+    = assistantClient.GetMessagesAsync(
+        threadRun.ThreadId,
+        new MessageCollectionOptions() { Order = MessageCollectionOrder.Ascending });
 
-// Note: messages iterate from newest to oldest, with the messages[0] being the most recent
-foreach (ThreadMessage threadMessage in messages.Reverse())
+await foreach (ThreadMessage message in messages)
 {
-    Console.Write($"{threadMessage.CreatedAt:yyyy-MM-dd HH:mm:ss} - {threadMessage.Role,10}: ");
-    foreach (MessageContent contentItem in threadMessage.ContentItems)
+    Console.Write($"[{message.Role.ToString().ToUpper()}]: ");
+    foreach (MessageContent contentItem in message.Content)
     {
-        if (contentItem is MessageTextContent textItem)
+        if (!string.IsNullOrEmpty(contentItem.Text))
         {
-            Console.Write(textItem.Text);
+            Console.WriteLine($"{contentItem.Text}");
+
+            if (contentItem.TextAnnotations.Count > 0)
+            {
+                Console.WriteLine();
+            }
+
+            // Include annotations, if any.
+            foreach (TextAnnotation annotation in contentItem.TextAnnotations)
+            {
+                if (!string.IsNullOrEmpty(annotation.InputFileId))
+                {
+                    Console.WriteLine($"* File citation, file ID: {annotation.InputFileId}");
+                }
+                if (!string.IsNullOrEmpty(annotation.OutputFileId))
+                {
+                    Console.WriteLine($"* File output, new file ID: {annotation.OutputFileId}");
+                }
+            }
+        }
+        if (!string.IsNullOrEmpty(contentItem.ImageFileId))
+        {
+            OpenAIFileInfo imageInfo = await fileClient.GetFileAsync(contentItem.ImageFileId);
+            BinaryData imageBytes = await fileClient.DownloadFileAsync(contentItem.ImageFileId);
+            using FileStream stream = File.OpenWrite($"{imageInfo.Filename}.png");
+            imageBytes.ToStream().CopyTo(stream);
+
+            Console.WriteLine($"<image: {imageInfo.Filename}.png>");
         }
-        Console.WriteLine();
     }
+    Console.WriteLine();
 }
 ```
 
-This will print an output as follows:
+Run the app using the [`dotnet run`](/dotnet/core/tools/dotnet-run) command:
 
+```csharp
+dotnet run
 ```
-2024-03-05 03:38:17 -       user: I need to solve the equation `3x + 11 = 14`. Can you help me?
-2024-03-05 03:38:25 -  assistant: The solution to the equation \(3x + 11 = 14\) is \(x = 1\).
-```
 
-New messages can be created on the thread before re-running, which will see the assistant use the past messages as context within the thread.
+The console output should resemble the following:
+
+```text
+[USER]: How well did product 113045 sell in February? Graph its trend over time.
+
+[ASSISTANT]: Product 113045 sold 22 units in February. Let's visualize its sales trend over the given months (January through March).
+
+I'll create a graph to depict this trend.
+
+[ASSISTANT]: <image: 553380b7-fdb6-49cf-9df6-e8e6700d69f4.png>
+The graph above visualizes the sales trend for product 113045 from January to March. As seen, the sales peaked in February with 22 units sold, and fluctuated over the period from January (12 units) to March (16 units).
+
+If you need further analysis or more details, feel free to ask!
+```
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "C# における新しいアシスタント機能の実装"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関連する C# ドキュメント（`assistants-csharp.md`）に大幅な修正と新機能の追加を伴うものです。具体的には、アシスタントを作成し、データを視覚化するプロセスを中心に、コード例を改善しています。

主な変更点は以下の通りです：

1. **日付の更新**: ドキュメントの日付を「2024年03月05日」から「2024年09月27日」に変更しました。

2. **手順の整理**: アシスタントを作成するための手順が構造化され、具体的なコマンドやコードスニペットが追加されています。特に、`.NET Core` アプリケーションの新規作成やビルド手順、そして OpenAI .NET クライアントライブラリのインストール手順が詳述されています。

3. **新機能の追加**: パスワードレス認証の推奨と、それに必要な手順が追加されました。これによって、アプリケーションのセキュリティが向上しています。

4. **コードサンプルの強化**: アシスタントの作成方法や、ユーザーからの質問に対する応答処理の方法を示す新しいコードが追加され、これにより具体的な利用方法が明確になっています。

5. **出力結果の改善**: アスistantが生成した出力のサンプルが提供され、ユーザーは実際の動作をイメージしやすくなっています。

このような大規模な改訂は、ユーザーが新しい機能を効果的に利用できるよう、具体的で実用的な情報を提供するための重要なステップです。

## articles/ai-services/openai/includes/fine-tuning-studio.md{#item-439f1e}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ description: Learn how to create your own custom model with Azure OpenAI Service
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 03/06/2024
+ms.date: 10/03/2024
 author: mrbullwinkle    
 ms.author: mbullwin
 ---
@@ -50,7 +50,7 @@ Take a moment to review the fine-tuning workflow for using Azure OpenAI Studio:
     1. [Select a base model](#select-the-base-model).
     1. [Choose your training data](#choose-your-training-data).
     1. Optionally, [choose your validation data](#choose-your-validation-data).
-    1. Optionally, [configure advanced options](#configure-advanced-options) for your fine-tuning job.
+    1. Optionally, [configure task parameters](#configure-task-parameters) for your fine-tuning job.
     1. [Review your choices and train your new custom model](#review-your-choices-and-train-your-model).
 1. Check the status of your custom fine-tuned model.
 1. Deploy your custom model for use.
@@ -91,7 +91,7 @@ In addition to the JSONL format, training and validation data files must be enco
 
 ### Create your training and validation datasets
 
-The more training examples you have, the better. Fine tuning jobs will not proceed without at least 10 training examples, but such a small number are not enough to noticeably influence model responses. It is best practice to provide hundreds, if not thousands, of training examples to be successful.
+The more training examples you have, the better. Fine tuning jobs will not proceed without at least 10 training examples, but such a small number isn't enough to noticeably influence model responses. It is best practice to provide hundreds, if not thousands, of training examples to be successful.
 
 In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively impact performance. If you train the model on a large amount of internal data, without first pruning the dataset for only the highest quality examples you could end up with a model that performs much worse than expected.
 
@@ -149,7 +149,7 @@ Azure OpenAI Studio provides the **Create custom model** wizard, so you can inte
 
 1. Open Azure OpenAI Studio at <a href="https://oai.azure.com/" target="_blank">https://oai.azure.com/</a> and sign in with credentials that have access to your Azure OpenAI resource. During the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
 
-1. In Azure OpenAI Studio, browse to the **Management > Models** pane, and select **Create a custom model**.
+1. In Azure OpenAI Studio, browse to the **Tools > Fine-tuning** pane, and select **Fine-tune model**.
 
    :::image type="content" source="../media/fine-tuning/studio-create-custom-model.png" alt-text="Screenshot that shows how to access the Create custom model wizard in Azure OpenAI Studio." lightbox="../media/fine-tuning/studio-create-custom-model.png":::
 
@@ -182,9 +182,9 @@ The next step is to either choose existing prepared training data or upload new
 
 :::image type="content" source="../media/fine-tuning/studio-training-data.png" alt-text="Screenshot of the Training data pane for the Create custom model wizard in Azure OpenAI Studio." lightbox="../media/fine-tuning/studio-training-data.png":::
 
-- If your training data is already uploaded to the service, select **Choose dataset**.
+- If your training data is already uploaded to the service, select **Files from Azure OpenAI Connection**.
 
-   - Select the file from the list shown in the **Training data** pane.
+   - Select the file from the dropdown list shown.
 
 - To upload new training data, use one of the following options:
 
@@ -217,7 +217,7 @@ You can import a training dataset from Azure Blob or another shared web location
 
 1. For the **File location**, provide the Azure Blob URL, the Azure Storage shared access signature (SAS), or other link to an accessible shared web location.
 
-1. Select **Upload file** to import the training dataset to the service.
+1. Select **Import** to import the training dataset to the service.
 
 After you select and upload the training dataset, select **Next** to continue.
 
@@ -266,15 +266,15 @@ You can import a validation dataset from Azure Blob or another shared web locati
 
 1. For the **File location**, provide the Azure Blob URL, the Azure Storage shared access signature (SAS), or other link to an accessible shared web location.
 
-1. Select **Upload file** to import the training dataset to the service.
+1. Select **Import** to import the training dataset to the service.
 
 After you select and upload the validation dataset, select **Next** to continue.
 
 :::image type="content" source="../media/fine-tuning/studio-validation-data-blob.png" alt-text="Screenshot of the Validation data pane for the Create custom model wizard, with Azure Blob and shared web location options." lightbox="../media/fine-tuning/studio-validation-data-blob.png":::
 
-### Configure advanced options
+### Configure task parameters
 
-The **Create custom model** wizard shows the parameters for training your fine-tuned model on the **Advanced options** pane. The following parameters are available:
+The **Create custom model** wizard shows the parameters for training your fine-tuned model on the **Task parameters** pane. The following parameters are available:
 
 
 |**Name**| **Type**| **Description**|
@@ -286,7 +286,7 @@ The **Create custom model** wizard shows the parameters for training your fine-t
 
 :::image type="content" source="../media/fine-tuning/studio-advanced-options.png" alt-text="Screenshot of the Advanced options pane for the Create custom model wizard, with default options selected." lightbox="../media/fine-tuning/studio-advanced-options.png":::
 
-Select **Default** to use the default values for the fine-tuning job, or select **Advanced** to display and edit the hyperparameter values. When defaults are selected, we determine the correct value algorithmically based on your training data.
+Select **Default** to use the default values for the fine-tuning job, or select **Custom** to display and edit the hyperparameter values. When defaults are selected, we determine the correct value algorithmically based on your training data.
 
 After you configure the advanced options, select **Next** to [review your choices and train your fine-tuned model](#review-your-choices-and-train-your-model).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングスタジオのガイドラインの修正"
}
```

### Explanation
この変更は、Azure OpenAI サービスのファインチューニングスタジオに関するドキュメント（`fine-tuning-studio.md`）において、いくつかの文言ならびに手順の改善を含んでいます。主な目的は、ユーザーがカスタムモデルを作成する手順をより明確に、また最新の情報に基づいて提供することです。

以下が主な変更点です：

1. **日付の更新**: 文書の日付が「2024年03月06日」から「2024年10月03日」に変更され、情報が最新であることを示しています。

2. **手順タイトルの変更**: 「高度なオプションの設定」という項目が「タスクパラメータの設定」という新しいタイトルに変更され、用語の統一性を図っています。

3. **手順内容の修正**:
   - モデル作成の手順において、メニュー項目が「管理 > モデル」から「ツール > ファインチューニング」に変更され、インターフェースの更新に対応しています。
   - トレーニングデータや検証データのインポート手順で使用するボタンの名称が「ファイルをアップロード」から「インポート」に変更され、操作の分かりやすさを向上させています。

4. **文言の微調整**: 一部の文章が改善され、明確さや流暢さが向上しています。

これらの修正は、ドキュメントの信頼性とユーザーエクスペリエンスを向上させるためのものであり、ユーザーがファインチューニングプロセスをより効果的に理解し、実行できることを目的としています。

## articles/ai-services/openai/includes/gpt-4-turbo.md{#item-e233e0}

<details>
<summary>Diff</summary>
````diff
@@ -31,10 +31,6 @@ This is the replacement for the following preview models:
 
 - `gpt-4` **Version:** `turbo-2024-04-09` is available for both standard and provisioned deployments. Currently the provisioned version of this model **doesn't support image/vision inference requests**. Provisioned deployments of this model only accept text input. Standard model deployments accept both text and image/vision inference requests.
 
-### Region availability
-
-For information on model regional availability consult the model matrix for [standard](../concepts/models.md#gpt-4-and-gpt-4-turbo-model-availability), and [provisioned deployments](../concepts/models.md#provisioned-deployment-model-availability).
-
 ### Deploying GPT-4 Turbo with Vision GA
 
-To deploy the GA model from the Studio UI, select `GPT-4` and then choose the `turbo-2024-04-09` version from the dropdown menu. The default quota for the `gpt-4-turbo-2024-04-09` model will be the same as current quota for GPT-4-Turbo. See the [regional quota limits.](../concepts/models.md#standard-and-global-standard-deployment-model-quota)
+To deploy the GA model from the Studio UI, select `GPT-4` and then choose the `turbo-2024-04-09` version from the dropdown menu. The default quota for the `gpt-4-turbo-2024-04-09` model will be the same as current quota for GPT-4-Turbo. See the [regional quota limits.](../quotas-limits.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turbo ドキュメントの軽微な修正"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関する GPT-4 Turbo のドキュメント（`gpt-4-turbo.md`）における軽微な修正を含んでいます。具体的には、文中の情報が整理され、いくつかの不要なセクションが削除されました。

主な変更点は以下の通りです：

1. **不必要な説明の削除**: 以前のバージョンでは、`gpt-4` モデルの詳細な説明と、地域的な可用性に関するセクションが含まれていましたが、この変更によりその部分が削除されました。

2. **地域可用性セクションの削除**: モデルの地域的な可用性についての情報が削除され、文書がより簡潔になりました。この情報は他のドキュメントで確認できるため、重複を避ける形で削除されたと考えられます。

3. **リンクの更新**: 地域的なクォータ制限に関するリンクが更新され、正確性と関連性が向上しています。

これらの修正は、ユーザーが情報を素早く見つけやすくするためのものであり、全体的な文書の明瞭性と使用感を改善することを目的としています。

## articles/ai-services/openai/includes/gpt-v-dotnet.md{#item-120a68}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,122 @@
+---
+title: 'Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the .NET SDK'
+titleSuffix: Azure OpenAI
+description: Get started using the Azure OpenAI .NET SDK to deploy and use the GPT-4 Turbo with Vision model.
+services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.custom: references_regions
+ms.date: 01/22/2024
+---
+
+Use this article to get started using the Azure OpenAI .NET SDK to deploy and use the GPT-4 Turbo with Vision model. 
+
+## Prerequisites
+
+- An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
+- [The .NET 8.0 SDK](https://dotnet.microsoft.com/en-us/download)
+- An Azure OpenAI Service resource with a GPT-4 Turbo with Vision model deployed. See [GPT-4 and GPT-4 Turbo Preview model availability](../concepts/models.md#gpt-4-and-gpt-4-turbo-model-availability) for available regions. For more information about resource creation, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).
+
+## Set up
+
+### Retrieve key and endpoint
+
+To successfully make a call against Azure OpenAI, you need an **endpoint** and a **key**.
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.|
+| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+
+Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+
+:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location highlighted." lightbox="../media/quickstarts/endpoint.png":::
+
+
+## Create the .NET app
+
+1. Create a .NET app using the `dotnet new` command:
+
+    ```dotnetcli
+    dotnet new console -n OpenAISpeech
+    ```
+
+1. Change into the directory of the new app:
+
+    ```dotnetcli
+    cd OpenAISpeech
+    ```
+
+## Install the client library
+
+Install the [`Azure.OpenAI`](https://www.nuget.org/packages/Azure.AI.OpenAI/) client library:
+
+```dotnetcli
+dotnet add package Azure.AI.OpenAI
+```
+
+## Passwordless authentication is recommended
+
+Passwordless authentication is more secure than key-based alternatives and is the recommended approach for connecting to Azure services. If you choose to use Passwordless authentication, you'll need to complete the following:
+
+1. Add the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package.
+
+    ```dotnetcli
+    dotnet add package Azure.Identity
+    ```
+
+1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal on your OpenAI resource under **Access control (IAM)** > **Add role assignment**.
+1. Sign-in to Azure using Visual Studio or the Azure CLI via `az login`.
+
+## Update the app code
+
+1. Replace the contents of `program.cs` with the following code and update the placeholder values with your own.
+
+    ```csharp
+    using Azure;
+    using Azure.AI.OpenAI;
+    using Azure.Identity;
+    using OpenAI.Chat; // Required for Passwordless auth
+    
+    var endpoint = new Uri("YOUR_AZURE_OPENAI_ENDPOINT");
+    var credentials = new AzureKeyCredential("YOUR_AZURE_OPENAI_KEY");
+    // var credentials = new DefaultAzureCredential(); // Use this line for Passwordless auth
+    var deploymentName = "gpt-4"; // Default name, update with your own if needed
+    
+    var openAIClient = new AzureOpenAIClient(endpoint, credentials);
+    var chatClient = openAIClient.GetChatClient(deploymentName);
+    
+    var imageUri = "YOUR_IMAGE_URL";
+    
+    List<ChatMessage> messages = [
+        new UserChatMessage(
+            ChatMessageContentPart.CreateTextMessageContentPart("Please describe the following image:"),
+            ChatMessageContentPart.CreateImageMessageContentPart(new Uri(imageUri), "image/png"))
+    ];
+    
+    ChatCompletion chatCompletion = await chatClient.CompleteChatAsync(messages);
+    
+    Console.WriteLine($"[ASSISTANT]:");
+    Console.WriteLine($"{chatCompletion.Content[0].Text}");
+    ```
+
+    > [!IMPORTANT]
+    > For production, store and access your credentials using a secure method, such as [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see [Azure AI services security](../../security-features.md).
+
+1. Run the application using the `dotnet run` command or the run button at the top of Visual Studio:
+
+    ```dotnetcli
+    dotnet run
+    ```
+
+  The app generates an audio file at the location you specified for the `speechFilePath` variable. Play the file on your device to hear the generated audio.
+
+## Clean up resources
+
+If you want to clean up and remove an Azure OpenAI resource, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
+
+- [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
+- [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
+
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "GPT-4 Turbo with Visionの.NET SDKクイックスタートガイドの追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスの GPT-4 Turbo with Vision モデルを使用するための .NET SDK に関する新しいドキュメント（`gpt-v-dotnet.md`）を追加するものです。この記事は、ユーザーがこのモデルを展開し、使用する手順を提供することを目的としています。

主な内容は以下の通りです：

1. **導入**: このドキュメントでは、Azure OpenAI .NET SDK を使用して、GPT-4 Turbo with Vision モデルをデプロイし、利用する方法について説明しています。

2. **前提条件**: ユーザーが必要とする条件（Azure サブスクリプション、.NET 8.0 SDK、GPT-4 Turbo with Vision モデルを持つ Azure OpenAI サービスリソース）を明記しています。

3. **設定方法**: Azure OpenAI へアクセスするためのエンドポイントとキーの取得方法について具体的に説明しています。

4. **.NET アプリの作成**: 新しい .NET アプリの作成手順を示すコマンドが含まれており、クライアントライブラリのインストール方法も提供されています。

5. **パスワードレス認証の推奨**: よりセキュアな接続方法として、パスワードレス認証を用いることが推奨され、そのための手順も詳細に説明されています。

6. **アプリコードの更新**: ユーザーがアプリのコードを書き換えるための具体的なコードスニペットが提供され、必要な変更点が説明されています。

7. **リソースのクリーンアップ**: Azure OpenAI リソースを削除する際の手順も記載されており、ユーザーがリソースを管理しやすいように配慮されています。

このドキュメントの追加により、ユーザーが GPT-4 Turbo with Vision モデルを円滑に利用できるようになり、特に.NET 開発者にとって有用なガイドラインとなっています。

## articles/ai-services/openai/includes/model-matrix/global-batch.md{#item-929e6a}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,15 @@
+---
+title: Global Batch model availability
+titleSuffix: Azure OpenAI Service
+description: Regional availability for Global Batch models
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 10/03/2024
+---
+
+| **Region**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
+|:-----------------|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
+| eastus           | ✅                | ✅                            | ✅                       | ✅                       | ✅                            | ✅                       | ✅                       | ✅                       |
+| swedencentral    | ✅                | ✅                            | ✅                       | ✅                       | ✅                            | ✅                       | ✅                       | ✅                       |
+| westus           | ✅                | ✅                            | ✅                       | ✅                       | ✅                            | ✅                       | ✅                       | ✅                       |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Global Batchモデルの可用性に関する新しいドキュメントの追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスの Global Batch モデルに関する可用性を示す新しいドキュメント（`global-batch.md`）を追加するものです。この文書は、異なる地域における各モデルのサポート状況を表にまとめて提供します。

主な内容は以下の通りです：

1. **タイトルと説明**: ドキュメントのタイトルは「Global Batch model availability」であり、地域ごとのモデルの可用性に関する情報を提供することを目的としています。

2. **可用性の表**: 提供される表では、さまざまなモデル（例: gpt-4、gpt-35-turboなど）の地域別の可用性が示されています。各地域において、どのモデルが利用可能であるかを明示しています。

3. **地域の確認**: 表に示された地域には、`eastus`、`swedencentral`、`westus` が含まれ、これらの地域で利用可能な異なるモデルがチェックマークで表示されています。

この文書の追加により、ユーザーは特定の地域で利用可能なモデルを簡単に確認できるようになり、Azure OpenAI サービスを使用する際の利便性が向上します。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,37 @@
+---
+title: Global Provisioned model availability
+titleSuffix: Azure OpenAI Service
+description: Global PTU-managed model availability by region.
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.custom: references_regions
+ms.date: 10/03/2024
+---
+
+| **Region**     | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:--------------------------:|:-------------------------------:|
+| australiaeast      | ✅                       | ✅                            |
+| brazilsouth        | ✅                       | ✅                            |
+| canadacentral      | ✅                       | ✅                            |
+| canadaeast         | ✅                       | ✅                            |
+| eastus             | ✅                       | ✅                            |
+| eastus2            | ✅                       | ✅                            |
+| francecentral      | ✅                       | ✅                            |
+| germanywestcentral | ✅                       | ✅                            |
+| japaneast          | ✅                       | ✅                            |
+| koreacentral       | ✅                       | ✅                            |
+| northcentralus     | ✅                       | ✅                            |
+| norwayeast         | ✅                       | ✅                            |
+| polandcentral      | ✅                       | ✅                            |
+| southafricanorth   | ✅                       | ✅                            |
+| southcentralus     | ✅                       | ✅                            |
+| southindia         | ✅                       | ✅                            |
+| spaincentral       | ✅                       | ✅                            |
+| swedencentral      | ✅                       | ✅                            |
+| switzerlandnorth   | ✅                       | ✅                            |
+| switzerlandwest    | ✅                       | ✅                            |
+| uksouth            | ✅                       | ✅                            |
+| westeurope         | ✅                       | ✅                            |
+| westus             | ✅                       | ✅                            |
+| westus3            | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Global Provisionedモデルの可用性に関する新しいドキュメントの追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスの Global Provisioned モデルに関する可用性を示す新しいドキュメント（`provisioned-global.md`）を追加するものです。この文書は、各地域におけるモデルのサポート状況を明確にすることを目的としています。

主な内容は以下の通りです：

1. **タイトルと説明**: ドキュメントのタイトルは「Global Provisioned model availability」であり、地域ごとの PTU（Provisioned Throughput Unit）管理モデルの可用性に関する情報を提供します。

2. **可用性の表**: 提供される表では、さまざまな地域におけるモデル（例: gpt-4o、gpt-4o-mini）の可用性が示されています。各地域で利用可能なモデルがチェックマークで表示されています。

3. **地域の確認**: 表に示された地域には、`australiaeast`、`canadacentral`、`japaneast` などが含まれ、これらの地域で利用可能なモデルがすべての列でチェックマークにて表示されています。

この文書の追加により、ユーザーは特定の地域で利用可能な Global Provisioned モデルを簡単に確認できるようになり、Azure OpenAI サービスをより効果的に活用できるようになります。

## articles/ai-services/openai/includes/model-matrix/quota.md{#item-389aa1}

<details>
<summary>Diff</summary>
````diff
@@ -5,32 +5,32 @@ description: Azure OpenAI model quota
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 09/22/2024
+ms.date: 10/04/2024
 ---
 
 
-| Region             | GPT-4   | GPT-4-32K   | GPT-4-Turbo   | GPT-4-Turbo-V   | gpt-4o   | gpt-4o-mini   | GPT-35-Turbo   | GPT-35-Turbo-Instruct   | gpt-4o - GlobalStandard   | gpt-4o-mini - GlobalStandard   | GPT-4-Turbo - GlobalStandard   | GPT-4o - Global-Batch   | GPT-4o-mini - Global-Batch   | GPT-4 - Global-Batch   | GPT-4-Turbo - Global-Batch   | gpt-35-turbo - Global-Batch   | Text-Embedding-Ada-002   | text-embedding-3-small   | text-embedding-3-large   | GPT-4o - finetune   | GPT-4o-mini - finetune   | GPT-4 - finetune   | Babbage-002   | Babbage-002 - finetune   | Davinci-002   | Davinci-002 - finetune   | GPT-35-Turbo - finetune   | GPT-35-Turbo-1106 - finetune   | GPT-35-Turbo-0125 - finetune   |
-|:-------------------|:-------:|:-----------:|:-------------:|:---------------:|:--------:|:-------------:|:--------------:|:-----------------------:|:-------------------------:|:------------------------------:|:------------------------------:|:-----------------------:|:----------------------------:|:----------------------:|:----------------------------:|:-----------------------------:|:------------------------:|:------------------------:|:------------------------:|:-------------------:|:------------------------:|:------------------:|:-------------:|:------------------------:|:-------------:|:------------------------:|:-------------------------:|:------------------------------:|:-------------------------------|
-| australiaeast      | 40 K    | 80 K        | 80 K          | 30 K            | -        | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| brazilsouth        | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| canadaeast         | 40 K    | 80 K        | 80 K          | -               | -        | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| eastus             | -       | -           | 80 K          | -               | 1 M      | 2 M           | 240 K          | 240 K                   | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 240 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| eastus2            | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | 250 K               | -                        | -                  | -             | -                        | -             | -                        | 250 K                     | 250 K                          | 250 K                          |
-| francecentral      | 20 K    | 60 K        | 80 K          | -               | -        | -             | 240 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| germanywestcentral | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| japaneast          | -       | -           | -             | 30 K            | -        | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| koreacentral       | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| northcentralus     | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
-| norwayeast         | -       | -           | 150 K         | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| polandcentral      | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| southafricanorth   | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| southcentralus     | -       | -           | 80 K          | -               | 1 M      | -             | 240 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| southindia         | -       | -           | 150 K         | -               | -        | -             | 300 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| spaincentral       | -       | -           | -             | -               | -        | -             | -              | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| swedencentral      | 40 K    | 80 K        | 150 K         | 30 K            | 1 M      | 2 M           | 300 K          | 240 K                   | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | 350 K                    | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
-| switzerlandnorth   | 40 K    | 80 K        | -             | 30 K            | -        | -             | 300 K          | -                       | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| switzerlandwest    | -       | -           | -             | -               | -        | -             | -              | -                       | -                         | -                              | -                              | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | 250 K                    | -             | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
-| uksouth            | -       | -           | 80 K          | -               | -        | -             | 240 K          | -                       | 30 M                      | -                              | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| westeurope         | -       | -           | -             | -               | -        | -             | 240 K          | -                       | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| westus             | -       | -           | 80 K          | 30 K            | 1 M      | 2 M           | 300 K          | -                       | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| westus3            | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
\ No newline at end of file
+| Region             | o1-mini   | o1    | GPT-4   | GPT-4-32K   | GPT-4-Turbo   | GPT-4-Turbo-V   | gpt-4o   | gpt-4o-mini   | GPT-35-Turbo   | GPT-35-Turbo-Instruct   | o1-mini - GlobalStandard   | o1 - GlobalStandard   | gpt-4o - GlobalStandard   | gpt-4o-mini - GlobalStandard   | GPT-4-Turbo - GlobalStandard   | GPT-4o - Global-Batch   | GPT-4o-mini - Global-Batch   | GPT-4 - Global-Batch   | GPT-4-Turbo - Global-Batch   | gpt-35-turbo - Global-Batch   | Text-Embedding-Ada-002   | text-embedding-3-small   | text-embedding-3-large   | GPT-4o - finetune   | GPT-4o-mini - finetune   | GPT-4 - finetune   | Babbage-002   | Babbage-002 - finetune   | Davinci-002   | Davinci-002 - finetune   | GPT-35-Turbo - finetune   | GPT-35-Turbo-1106 - finetune   | GPT-35-Turbo-0125 - finetune   |
+|:-------------------|:---------:|:-----:|:-------:|:-----------:|:-------------:|:---------------:|:--------:|:-------------:|:--------------:|:-----------------------:|:--------------------------:|:---------------------:|:-------------------------:|:------------------------------:|:------------------------------:|:-----------------------:|:----------------------------:|:----------------------:|:----------------------------:|:-----------------------------:|:------------------------:|:------------------------:|:------------------------:|:-------------------:|:------------------------:|:------------------:|:-------------:|:------------------------:|:-------------:|:------------------------:|:-------------------------:|:------------------------------:|:-------------------------------|
+| australiaeast      | -         | -     | 40 K    | 80 K        | 80 K          | 30 K            | -        | -             | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| brazilsouth        | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| canadaeast         | -         | -     | 40 K    | 80 K        | 80 K          | -               | -        | -             | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| eastus             | -         | -     | -       | -           | 80 K          | -               | 1 M      | 2 M           | 240 K          | 240 K                   | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 240 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| eastus2            | 1 M       | 600 K | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | 50 M                       | 15 M                  | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | 250 K               | -                        | -                  | -             | -                        | -             | -                        | 250 K                     | 250 K                          | 250 K                          |
+| francecentral      | -         | -     | 20 K    | 60 K        | 80 K          | -               | -        | -             | 240 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| germanywestcentral | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| japaneast          | -         | -     | -       | -           | -             | 30 K            | -        | -             | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| koreacentral       | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| northcentralus     | -         | -     | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
+| norwayeast         | -         | -     | -       | -           | 150 K         | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| polandcentral      | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| southafricanorth   | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| southcentralus     | -         | -     | -       | -           | 80 K          | -               | 1 M      | 2 M           | 240 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| southindia         | -         | -     | -       | -           | 150 K         | -               | -        | -             | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| spaincentral       | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| swedencentral      | 1 M       | 600 K | 40 K    | 80 K        | 150 K         | 30 K            | 1 M      | 2 M           | 300 K          | 240 K                   | 50 M                       | 15 M                  | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | 350 K                    | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
+| switzerlandnorth   | -         | -     | 40 K    | 80 K        | -             | 30 K            | -        | -             | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| switzerlandwest    | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | -                         | -                              | -                              | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | 250 K                    | -             | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
+| uksouth            | -         | -     | -       | -           | 80 K          | -               | -        | -             | 240 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| westeurope         | -         | -     | -       | -           | -             | -               | -        | -             | 240 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| westus             | -         | -     | -       | -           | 80 K          | 30 K            | 1 M      | 2 M           | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| westus3            | -         | -     | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Quotaドキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAI サービスの Quota ドキュメント（`quota.md`）の内容を更新したものです。主な変更点は以下の通りです：

1. **日付の更新**: ドキュメントの最終更新日が「09/22/2024」から「10/04/2024」へと変更されました。この変更により、最新の情報に基づいていることが示されています。

2. **表の形式変更**: モデル名や地域に関する情報を詳細に表示するために、既存の表の形式が更新されました。これにより、各地域ごとの使用可能なモデルとそのクオータがより明確に示されています。

3. **モデル名の追加**: 新しいモデル名（o1-mini、o1など）が表に追加され、これによりユーザーは利用可能な全モデルを一目で確認できるようになりました。

全体的にこの変更は、ユーザーが各モデルの利用可能性とクオータに関する情報を最新のものとして簡単に確認できるようにするものであり、Azure OpenAI サービスの利用者にとっては重要な情報更新となります。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,34 @@
+---
+title: Global Standard model availability
+titleSuffix: Azure OpenAI Service
+description: Regional availability for Global Standard models.
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 10/03/2024
+---
+
+| **Region**     | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-10-01**   |
+|:-------------------|:------------------------------:|:---------------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|
+| australiaeast      | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| brazilsouth        | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| canadaeast         | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| eastus             | -                          | -                       | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
+| eastus2            | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                                        |
+| francecentral      | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| germanywestcentral | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| japaneast          | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| koreacentral       | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| northcentralus     | -                          | -                       | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
+| norwayeast         | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| polandcentral      | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| southafricanorth   | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| southcentralus     | -                          | -                       | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
+| southindia         | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| spaincentral       | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| swedencentral      | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                                        |
+| switzerlandnorth   | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| uksouth            | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| westeurope         | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
+| westus             | -                          | -                       | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
+| westus3            | -                          | -                       | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Global Standardモデルの可用性に関する新しいドキュメントの追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスにおける Global Standard モデルの地域別可用性を示す新しいドキュメント（`standard-global.md`）を追加するものです。このドキュメントは、各モデルがどの地域で利用可能かを明確に示しています。

主な内容は以下の通りです：

1. **タイトルと説明**: ドキュメントのタイトルは「Global Standard model availability」であり、Global Standard モデルの地域別可用性に関する情報を提供しています。

2. **可用性の表**: 各モデル（例: o1-preview、gpt-4、gpt-4oなど）の可用性が示された表が追加されています。地域ごとに ✅ が表示されており、そのモデルがどの地域で利用可能かを簡単に確認できます。

3. **表示される地域**: 表には、「australiaeast」、「brazilsouth」、「canadaeast」、「eastus」など、様々な地域が含まれています。

この新しいドキュメントの追加により、ユーザーは特定の地域で利用できる Global Standard モデルの情報を迅速に確認でき、Azure OpenAI サービスの利用の効率が向上します。

## articles/ai-services/openai/includes/model-matrix/standard-gpt-4.md{#item-d4064a}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Standard GPT-4 model availability
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 09/22/2024
+ms.date: 10/04/2024
 ---
 
 | **Region**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **vision-preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4-32k**, **0613**   |
@@ -18,7 +18,7 @@ ms.date: 09/22/2024
 | japaneast        | -               | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | -                   |
 | northcentralus   | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   |
 | norwayeast       | -               | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | -                   |
-| southcentralus   | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   |
+| southcentralus   | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   |
 | southindia       | -               | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | -                   |
 | swedencentral    | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    |
 | switzerlandnorth | ✅                | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Standard GPT-4モデルの可用性ドキュメントの更新"
}
```

### Explanation
この変更は、Standard GPT-4 モデルの可用性に関するドキュメント（`standard-gpt-4.md`）の内容を更新したものです。変更内容は以下の通りです。

1. **日付の更新**: ドキュメントの更新日が「09/22/2024」から「10/04/2024」へと変更され、最新の情報を反映しています。

2. **表の修正**: `southcentralus` の行において、特定のモデルに関するチェックマークが追加されました。追加されたチェックマークは、`gpt-4o-mini` モデルの可用性を示しており、この地域でのサービス利用可能性が改善されていることを示しています。

これによって、ユーザーは Standard GPT-4 モデルの最新の可用性情報を確認しやすくなり、より適切なサービス利用の決定に役立てることができます。全体として、この更新はドキュメントの正確性と信頼性を向上させるものです。

## articles/ai-services/openai/includes/model-matrix/standard-models.md{#item-af04c4}

<details>
<summary>Diff</summary>
````diff
@@ -5,27 +5,26 @@ description: Quota and limits for Azure OpenAI by region.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 09/22/2024
+ms.date: 10/04/2024
 ---
 
-
-| **Region**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **vision-preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **0301**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   | **gpt-35-turbo-16k**, **0613**   | **gpt-35-turbo-instruct**, **0914**   | **text-embedding-ada-002**, **1**   | **text-embedding-ada-002**, **2**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **dall-e-2**, **2.0**   | **dall-e-3**, **3.0**   | **babbage-002**, **1**   | **davinci-002**, **1**   | **tts**, **001**   | **tts-hd**, **001**   | **whisper**, **001**   |
-|:-----------------|:-------------------:|:---------------------------:|:---------------------------:|:-----------------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:------------------------------:|:-----------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------:|:---------------------:|:----------------------:|:----------------------:|:----------------:|:-------------------:|:--------------------:|
-| australiaeast    | ✅                | ✅                        | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | ✅                  | -                  | -                  | -            | -               | -                |
-| brazilsouth      | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
-| canadaeast       | ✅                | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| eastus           | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | ✅                  | -                  | -                  | -            | -               | -                |
-| eastus2          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| francecentral    | ✅                | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | ✅                    | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| japaneast        | -               | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | -                   | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| northcentralus   | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
-| norwayeast       | -               | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| southafricanorth | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
-| southcentralus   | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | -                           | -                   | ✅                       | -                      | -                      | ✅                       | -                          | -                               | ✅                              | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
-| southindia       | -               | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | ✅                       | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| swedencentral    | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           | ✅                                | -                             | ✅                              | -                             | ✅                              | -                 | ✅                  | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
-| switzerlandnorth | ✅                | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| uksouth          | -               | ✅                        | ✅                        | -                         | -                           | -                      | -                      | -                           | -                   | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| westeurope       | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| westus           | -               | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
-| westus3          | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
\ No newline at end of file
+| **Region**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **vision-preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **0301**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   | **gpt-35-turbo-16k**, **0613**   | **gpt-35-turbo-instruct**, **0914**   | **text-embedding-ada-002**, **1**   | **text-embedding-ada-002**, **2**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **dall-e-2**, **2.0**   | **dall-e-3**, **3.0**   | **babbage-002**, **1**   | **davinci-002**, **1**   | **tts**, **001**   | **tts-hd**, **001**   | **whisper**, **001**   |
+|:-----------------|:------------------------------:|:---------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-----------------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:------------------------------:|:-----------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------:|:---------------------:|:----------------------:|:----------------------:|:----------------:|:-------------------:|:--------------------:|
+| australiaeast    | -                          | -                       | ✅                | ✅                        | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | ✅                  | -                  | -                  | -            | -               | -                |
+| brazilsouth      | -                          | -                       | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
+| canadaeast       | -                          | -                       | ✅                | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| eastus           | -                          | -                       | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | ✅                  | -                  | -                  | -            | -               | -                |
+| eastus2          | ✅                           | ✅                        | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| francecentral    | -                          | -                       | ✅                | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | ✅                    | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| japaneast        | -                          | -                       | -               | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | -                   | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| northcentralus   | -                          | -                       | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
+| norwayeast       | -                          | -                       | -               | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| southafricanorth | -                          | -                       | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
+| southcentralus   | -                          | -                       | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | ✅                       | -                      | -                      | ✅                       | -                          | -                               | ✅                              | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
+| southindia       | -                          | -                       | -               | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | ✅                       | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| swedencentral    | ✅                           | ✅                        | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           | ✅                                | -                             | ✅                              | -                             | ✅                              | -                 | ✅                  | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
+| switzerlandnorth | -                          | -                       | ✅                | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| uksouth          | -                          | -                       | -               | ✅                        | ✅                        | -                         | -                           | -                      | -                      | -                           | -                   | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| westeurope       | -                          | -                       | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
+| westus           | -                          | -                       | -               | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
+| westus3          | -                          | -                       | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Standardモデルに関するドキュメントの変更"
}
```

### Explanation
この変更は、Standardモデルに関するドキュメント（`standard-models.md`）の内容を更新したものです。主な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの最終更新日が「09/22/2024」から「10/04/2024」に変更され、最新の情報が反映されています。

2. **表の修正**: モデルの可用性を示す表の内容が変更され、特定のモデルが利用可能な地域やその表示が更新されました。たとえば、`southcentralus` や `uk-south` などの地域でのモデルの可用性が再評価され、いくつかのモデルに対するチェックマークが追加または削除されています。

3. **全体的な構造の調整**: 追加された項目や削除された項目があり、特にモデルの名前やバージョンに関する情報がより明確になっています。

これにより、ユーザーは最新のモデルの可用性情報を確認しやすくなり、Azure OpenAI サービスの利用に役立つ情報を得ることができます。全体として、この更新はドキュメントの精度と信頼性を向上させるものです。

## articles/ai-services/openai/includes/text-to-speech-dotnet.md{#item-fea66a}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,112 @@
+---
+ms.topic: include
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 09/23/2024
+ms.reviewer: v-baolianzou
+ms.author: alexwolf
+author: alexwolfmsft
+recommendations: false
+---
+
+## Prerequisites
+
+- An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
+- An Azure OpenAI resource with a Whisper model deployed in a [supported region](../concepts/models.md#whisper-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- [The .NET 8.0 SDK](https://dotnet.microsoft.com/en-us/download)
+
+## Create the .NET app
+
+1. Create a .NET app using the `dotnet new` command:
+
+    ```dotnetcli
+    dotnet new console -n TextToSpeech
+    ```
+
+1. Change into the directory of the new app:
+
+    ```dotnetcli
+    cd OpenAISpeech
+    ```
+
+1. Install the [`Azure.OpenAI`](https://www.nuget.org/packages/Azure.AI.OpenAI/) client library:
+    
+    ```dotnetcli
+    dotnet add package Azure.AI.OpenAI
+    ```
+
+## Authenticate and connect to Azure OpenAI
+
+To make requests to your Azure OpenAI service, you need the service endpoint as well as authentication credentials via one of the following options:
+
+- [Microsoft Entra ID](/entra/fundamentals/whatis) is the recommended approach for authenticating to Azure services and is more secure than key-based alternatives. 
+- Access keys allow you to provide a secret key to connect to your resource.
+
+    > [!IMPORTANT]
+    > Access keys should be used with caution. If your service access key is lost or accidentally exposed in an insecure location, your service may become vulnerable. Anyone who has the access key is able to authorize requests against the Azure OpenAI service.
+
+### Get the Azure OpenAI endpoint
+
+The service endpoint can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.
+
+:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location highlighted." lightbox="../media/quickstarts/endpoint.png":::
+
+### Authenticate using Microsoft Entra ID
+
+If you choose to use Microsoft Entra ID authentication, you'll need to complete the following:
+
+1. Add the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package.
+
+    ```dotnetcli
+    dotnet add package Azure.Identity
+    ```
+
+1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal on your OpenAI resource under **Access control (IAM)** > **Add role assignment**.
+1. Sign-in to Azure using Visual Studio or the Azure CLI via `az login`.
+
+### Authenticate using keys
+
+The access key value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+
+## Update the app code
+
+1. Replace the contents of `program.cs` with the following code and update the placeholder values with your own.
+
+    ```csharp
+    using Azure;
+    using Azure.AI.OpenAI;
+    using Azure.Identity; // Required for Passwordless auth
+    
+    var endpoint = new Uri(
+        Environment.GetEnvironmentVariable("YOUR_OPENAI_ENDPOINT") ?? throw new ArgumentNullException());
+    var credentials = new DefaultAzureCredential();
+
+    // Use this line for key auth
+    // var credentials = new AzureKeyCredential(
+    //    Environment.GetEnvironmentVariable("YOUR_OPENAI_KEY") ?? throw new ArgumentNullException());
+
+    var deploymentName = "tts"; // Default deployment name, update with your own if necessary
+    var speechFilePath = "YOUR_AUDIO_FILE_PATH";
+    
+    var openAIClient = new AzureOpenAIClient(endpoint, credentials);
+    var audioClient = openAIClient.GetAudioClient(deploymentName);
+    
+    var result = await audioClient.GenerateSpeechAsync(
+                    "the quick brown chicken jumped over the lazy dogs");
+    
+    Console.WriteLine("Streaming response to ${speechFilePath}");
+    await File.WriteAllBytesAsync(speechFilePath, result.Value.ToArray());
+    Console.WriteLine("Finished streaming");
+    ```
+
+    > [!IMPORTANT]
+    > For production, store and access your credentials using a secure method, such as [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see [Azure AI services security](../../security-features.md).
+
+1. Run the application using the `dotnet run` command or the run button at the top of Visual Studio:
+
+    ```dotnetcli
+    dotnet run
+    ```
+
+    The app generates an audio file at the location you specified for the `speechFilePath` variable. Play the file on your device to hear the generated audio.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "テキストから音声への変換に関する.NETのガイド追加"
}
```

### Explanation
この変更は、テキストから音声への変換機能に関する新しいガイドを `.NET` に追加したものです。このガイドは、Azure OpenAI サービスを利用してテキストを音声に変換するための手順を詳細に説明しています。主な内容は以下の通りです。

1. **前提条件の明記**: Azure サブスクリプションや、Whisper モデルがデプロイされた Azure OpenAI リソース、.NET 8.0 SDK などが必要です。

2. **.NETアプリケーションの作成手順**: 
   - 新しい.NETアプリを作成するためのコマンドと、そのディレクトリに移動する手順が示されています。
   - `Azure.OpenAI` クライアントライブラリのインストール方法が説明されています。

3. **Azure OpenAIへの認証と接続方法**:
   - Microsoft Entra ID またはアクセスキーを利用して、Azure OpenAIサービスに接続するための手順が提供されています。
   - サービスエンドポイントの取得方法も説明されています。

4. **アプリケーションコードの更新**: 
   - `program.cs` の内容をどのように変更すべきかが示されており、生成した音声ファイルを指定した場所に保存する方法が詳述されています。
   - 注意点として、認証情報を安全に管理する方法についても触れられています。

5. **アプリの実行手順**: 最後にアプリを実行するためのコマンドが提供されており、実行後に生成された音声ファイルをデバイスで再生できるようになります。

このガイドの追加によって、ユーザーは Azure OpenAI サービスを利用したテキストから音声への変換を簡単に実行できるようになり、具体的なコードの例が提供されていることで、実施が容易になります。全体として、この新しい機能は、開発者にとって非常に有用なリソースとなります。

## articles/ai-services/openai/includes/whisper-dotnet.md{#item-562a58}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,111 @@
+---
+services: ai-services
+author: mrbullwinkle
+ms.author: mbullwin
+ms.service: openai
+ms.topic: include
+ms.date: 3/19/2024
+---
+
+## Prerequisites
+
+- An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
+- An Azure OpenAI resource with a Whisper model deployed in a [supported region](../concepts/models.md#whisper-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- [The .NET 8.0 SDK](https://dotnet.microsoft.com/en-us/download)
+
+## Set up
+
+### Retrieve key and endpoint
+
+To successfully make a call against Azure OpenAI, you need an *endpoint* and a *key*.
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.|
+| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+
+Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you'll need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+
+:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location circled in red." lightbox="../media/quickstarts/endpoint.png":::
+
+## Create the .NET app
+
+1. Create a .NET app using the `dotnet new` command:
+
+    ```dotnetcli
+    dotnet new console -n OpenAIWhisper
+    ```
+
+1. Change into the directory of the new app:
+
+    ```dotnetcli
+    cd OpenAIWhisper
+    ```
+
+1. Install the [`Azure.OpenAI`](https://www.nuget.org/packages/Azure.AI.OpenAI/) client library:
+
+    ```dotnetcli
+    dotnet add package Azure.AI.OpenAI
+    ```
+
+## Passwordless authentication is recommended
+
+Passwordless authentication is more secure than key-based alternatives and is the recommended approach for connecting to Azure services. If you choose to use Passwordless authentication, you'll need to complete the following:
+
+1. Add the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package.
+
+    ```dotnetcli
+    dotnet add package Azure.Identity
+    ```
+
+1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal on your OpenAI resource under **Access control (IAM)** > **Add role assignment**.
+1. Sign-in to Azure using Visual Studio or the Azure CLI via `az login`.
+
+## Update the app code
+
+1. Replace the contents of `program.cs` with the following code and update the placeholder values with your own.
+
+    > [!NOTE]
+    > You can get sample audio files, such as *wikipediaOcelot.wav*, from the [Azure AI Speech SDK repository at GitHub](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/sampledata/audiofiles).
+    
+    ```csharp
+    using Azure;
+    using Azure.AI.OpenAI;
+    using Azure.Identity; // Required for Passwordless auth
+    
+    var endpoint = new Uri("YOUR_OPENAI_ENDPOINT");
+    var credentials = new AzureKeyCredential("YOUR_OPENAI_KEY");
+    // var credentials = new DefaultAzureCredential(); // Use this line for Passwordless auth
+    var deploymentName = "whisper"; // Default deployment name, update with your own if necessary
+    var audioFilePath = "YOUR_AUDIO_FILE_PATH";
+    
+    var openAIClient = new AzureOpenAIClient(endpoint, credentials);
+    
+    var audioClient = openAIClient.GetAudioClient(deploymentName);
+    
+    var result = await audioClient.TranscribeAudioAsync(audioFilePath);
+    
+    Console.WriteLine("Transcribed text:");
+    foreach (var item in result.Value.Text)
+    {
+        Console.Write(item);
+    }
+    ```
+
+    > [!IMPORTANT]
+    > For production, store and access your credentials using a secure method, such as [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see [Azure AI services security](../../security-features.md).
+
+1. Run the application using the `dotnet run` command or the run button at the top of Visual Studio:
+
+    ```dotnetcli
+    dotnet run
+    ```
+
+    If you are using the sample audio file, you should see the following text printed out in the console:
+
+    ```text
+    The ocelot, Lepardus paradalis, is a small wild cat native to the southwestern United States, 
+    Mexico, and Central and South America. This medium-sized cat is characterized by solid 
+    black spots and streaks on its coat, round ears...
+    ```
+    
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Whisperモデルに関する.NETのガイド追加"
}
```

### Explanation
この変更は、Whisperモデルを使用したテキストのトランスクリプション機能に関する新しいガイドを `.NET` 用に追加したことを示しています。このガイドでは、Azure OpenAI サービスを利用して音声データをテキストに変換するための手順を詳細に説明しています。主な内容は以下の通りです。

1. **前提条件の明示**: AzureサブスクリプションやWhisperモデルがデプロイされたAzure OpenAIリソース、および.NET 8.0 SDKの取得が必要であることが説明されています。

2. **エンドポイントとAPIキーの取得**: Azureポータルでリソースを確認し、エンドポイントとAPIキー（`KEY1`または`KEY2`）を取得する方法が詳細に説明されています。

3. **.NETアプリケーションのセットアップ**:
   - 新しい.NETアプリを作成する手順と、必要なライブラリ（`Azure.OpenAI`）のインストール方法が示されています。

4. **パスワードレス認証の推奨**: より安全な接続のために、パスワードレス認証を使用するための手順が紹介されており、`Azure.Identity`パッケージの追加や、ユーザーアカウントに対する役割の割り当て方法が含まれています。

5. **アプリケーションコードの更新**: 
   - `program.cs`の内容をどのように変更すべきかが説明され、実際のトランスクリプション処理を行うコードも提供されています。具体的には、音声ファイルを指定してトランスクリプション結果をコンソールに出力する流れが説明されています。

6. **アプリの実行手順**: 最後にアプリを実行するためのコマンドが提供されており、サンプル音声ファイルを使用した場合の出力の例も示されています。

この新しいガイドの追加により、ユーザーはAzure OpenAIを通じて音声からテキストへの変換を簡単に実行できるようになります。特に具体的なコード例が提供されていることで、開発者にとって実装が容易となり、Azureの利用価値が高まります。

## articles/ai-services/openai/media/content-filters/advanced.png{#item-634795}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "コンテンツフィルタリングに関する画像の削除"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関連するコンテンツフィルタリングを示す画像（`advanced.png`）が削除されたことを示しています。この画像は、関連するドキュメントやガイドで使用されていた可能性がありますが、現在はその内容が不要または不適切と判断されたために削除されました。

削除の影響としては、関連情報を視覚的に伝えるためのリソースが失われることになります。ユーザーにとっては、コンテンツフィルタリングの理解が図示された形でサポートされなくなるため、テキストだけの説明に頼らざるを得ないことになります。このことにより、利用者は情報を把握する際に若干の不便を感じる可能性があります。

今後のドキュメントやガイドでは、削除された画像に代わる新しい視覚的リソースが追加されるか、テキストでの説明の充実が図られることが期待されます。

## articles/ai-services/openai/media/content-filters/create-filter.jpg{#item-7c9550}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "コンテンツフィルタ作成に関する画像の削除"
}
```

### Explanation
この変更は、コンテンツフィルタを作成するプロセスを示す画像（`create-filter.jpg`）が削除されたことを示しています。この画像は、ドキュメント内でフィルタ作成の手順や概念を視覚的に補完する役割を果たしていた可能性があります。

画像の削除により、関連するドキュメントやガイドにおいて、コンテンツフィルタの作成手順がテキストだけで説明されることになります。これにより、ユーザーは視覚的な手助けがなくなり、手順を理解する上で多少の難しさを感じることがあるかもしれません。

今後、この削除された画像の代わりに新しい視覚資料が提供されるか、テキストでの説明がより詳細に記載されることが求められます。ユーザーにとっての理解を深めるために、適切な補足情報が用意されることが期待されます。

## articles/ai-services/openai/media/content-filters/create-filter.png{#item-dc4d68}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "コンテンツフィルタ作成に関する画像の追加"
}
```

### Explanation
この変更は、コンテンツフィルタを作成する手順を示す画像（`create-filter.png`）が新たに追加されたことを示しています。この画像は、ドキュメント内でフィルタ作成のプロセスを視覚的に補完し、ユーザーの理解を助ける役割を果たすことが期待されます。

新たな画像の導入により、ユーザーはテキストだけの説明ではなく、具体的な視覚資料を通してフィルタの作成手順を学ぶことができ、理解が深まるでしょう。このような視覚的な補助は、特に複雑な手順を説明する際に有効です。

今後もこのような視覚資料が増えることにより、ユーザーに対する情報提供の質が向上し、より多くのユーザーがAzure OpenAI サービスを効果的に利用できるようになることが期待されます。

## articles/ai-services/openai/media/content-filters/delete.png{#item-db8934}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタ削除に関する画像の更新"
}
```

### Explanation
この変更は、コンテンツフィルタを削除する手順を示す画像（`delete.png`）が変更されたことを示しています。この更新は、既存の視覚資料に対して調整や改善が行われた結果であり、より明確で理解しやすい内容になった可能性があります。

具体的な詳細は記載されていないものの、画像の更新により、ユーザーはフィルタ削除のプロセスをより正確に理解できるようになるでしょう。このようなマイナーな更新は、文書の信頼性を高めるために重要です。

ユーザーにとっては、視覚的な補助がより効果的になることで、手順を実行する自信が増し、全体的な体験が向上することが期待されます。今後もこうした更新が続くことによって、Azure OpenAI サービスに関連するドキュメントの質が一層向上することが見込まれます。

## articles/ai-services/openai/media/content-filters/edit-deployment.png{#item-9c1621}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタデプロイメント編集に関する画像の更新"
}
```

### Explanation
この変更は、コンテンツフィルタのデプロイメントを編集する手順を示す画像（`edit-deployment.png`）が修正されたことを示しています。具体的な内容変更は記載されていないものの、視覚的な説明が改善され、ユーザーにとっての理解が向上したことが期待されます。

更新された画像により、ユーザーはフィルタのデプロイメント編集プロセスをより明確に理解できるようになり、関連する手順が一層分かりやすくなるでしょう。このようなマイナーな更新でも、特に視覚資料を含む文書では、情報の正確さと質を高めるために重要です。

今後もこのような小さな改良が続くことで、Azure OpenAI サービスのドキュメント全体のユーザー体験が向上し、利用者がより効果的に情報を活用できるようになることが期待されます。

## articles/ai-services/openai/media/content-filters/filter-view.jpg{#item-794e84}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "コンテンツフィルタビュー画像の削除"
}
```

### Explanation
この変更は、コンテンツフィルタのビューを示す画像（`filter-view.jpg`）が削除されたことを示しています。この削除は、ドキュメントやコンテンツの整合性に大きな影響を与える可能性があるため、ブレイキングチェンジとして分類されます。

この画像が削除されることにより、ユーザーは現在のドキュメント内で関連情報を視覚的に確認する手段を失うことになります。したがって、情報の透明性や理解を助けるためのビジュアル補助が欠如することとなります。

今後、同様の情報を別の方法で補完することが必要になるかもしれません。例えば、テキストや他の視覚資料での説明が強化されることで、ユーザーの理解を支援する必要があります。この変更により、Azure OpenAI サービスに関するユーザー体験が影響を受ける可能性があるため、重要な修正として認識されています。

## articles/ai-services/openai/media/content-filters/filter-view.png{#item-027c18}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "コンテンツフィルタビュー画像の追加"
}
```

### Explanation
この変更は、コンテンツフィルタのビューを示す新しい画像（`filter-view.png`）が追加されたことを示しています。この更新により、関連の手続きや機能が視覚的に示され、ユーザーの理解が向上することが期待されます。

追加された画像は、コンテンツフィルタの使用方法や設定に関する具体的なビジュアルガイダンスを提供し、ドキュメントの質を高めます。特に、技術的な内容を持つ文書では、視覚的要素が情報伝達の効果を大きく左右するため、非常に重要です。

今後、ユーザーがこの画像を参照することで、コンテンツフィルタの機能や操作がより明確に理解できるようになり、Azure OpenAI サービスの体験が向上することが期待されます。このような新機能の追加は、ユーザーの満足度を高め、サービス利用の促進に寄与するでしょう。

## articles/ai-services/openai/media/content-filters/multiple.png{#item-e633fb}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタのマルチビジュアルの修正"
}
```

### Explanation
この変更は、コンテンツフィルタに関する画像（`multiple.png`）が修正されたことを示しています。具体的には、画像に関する何らかの調整が行われたが、追加や削除は行われていません。このようなマイナーなアップデートは、一般的に画像の品質向上や視覚要素の明確化を目的としています。

修正された画像は、コンテンツフィルタがどのように複数のオプションや設定を扱うかを示すために使用されている可能性があります。ユーザーにとって、視覚的にわかりやすい情報は重要であり、変更後の画像はより分かりやすくなっていることが期待されます。

このように、マイナーアップデートは全体的なドキュメントのクオリティを向上させ、ユーザーがコンテンツフィルタの機能をより理解しやすくするために重要です。これにより、Azure OpenAI サービスに関する情報の有用性が高まり、ユーザーエクスペリエンスの向上に寄与するでしょう。

## articles/ai-services/openai/media/content-filters/off.jpg{#item-7ca291}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "コンテンツフィルタのオフ状態画像の削除"
}
```

### Explanation
この変更は、コンテンツフィルタがオフの状態を示す画像（`off.jpg`）が削除されたことを示しています。この変更は重要なものであり、ドキュメントやサービスの参照に影響を与える可能性があります。

画像の削除は、コンテンツフィルタの機能・設定に関する情報提供の一環として行われたと考えられます。このような変更は、特定の機能がもはやサポートされていない、または調整が必要であることを示唆しています。そのため、ユーザーはこの画像の参照を失い、コンテンツフィルタのオフ状態を視覚的に理解する手段が減少することになります。

このようなブレイキングチェンジは、特に新しいユーザーに対して混乱を招く可能性があるため、他の関連するドキュメントやガイドラインの更新も必要になるでしょう。ユーザーは変更内容を把握し、他の情報源やドキュメントに基づいて代替の視覚的な理解を確保する必要があります。

## articles/ai-services/openai/media/content-filters/select-filter.png{#item-dbe513}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタ選択画像の修正"
}
```

### Explanation
この変更は、コンテンツフィルタに関連する選択画像（`select-filter.png`）が修正されたことを示しています。具体的には、この画像に対しての調整が行われたが、追加や削除は行われていません。

画像の更新は、利用者に対して提供される情報の品質を向上させることを目的としています。この更新により、選択フィルタの機能や使用方法がより明確に表現されていることが期待され、ユーザーの理解を助ける役割を果たすでしょう。

一般的に、マイナーな更新は視覚的な要素がより直感的に理解できるように改善されることが多く、ドキュメント全体のユーザビリティを向上させるために重要です。特に、技術文書やガイドにおいては、視覚的な情報の正確性と明瞭さが、使用者にとっての価値を高めることに繋がります。そのため、このような変更は、Azure OpenAI サービスに関する理解を促進する助けとなるでしょう。

## articles/ai-services/openai/media/content-filters/settings.jpg{#item-8aadc0}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "コンテンツフィルタ設定画像の削除"
}
```

### Explanation
この変更は、コンテンツフィルタの設定を示す画像（`settings.jpg`）が削除されたことを示しています。この削除は、関連するドキュメントや情報源に対して重大な影響を及ぼす可能性があります。

設定画像の削除により、ユーザーはコンテンツフィルタの設定方法に関する視覚的な手助けを失うことになります。これは、特に新規ユーザーや視覚的な情報に依存しているユーザーにとっては、理解を困難にする要素となるかもしれません。このようなブレイキングチェンジは、ドキュメントの内容やサービスの使用方法に対する理解に影響を与えるため、使用者は必ず代替の情報源を求める必要があります。

そのため、このような変更が行われた理由や、新しい指示がどのように提供されるのかを明確にすることが重要です。また、他の関連文書を見直し、必要に応じて更新することで、ユーザーが適切な情報にアクセスできるようにすることも重要です。

## articles/ai-services/openai/media/content-filters/severity-level.jpg{#item-5fce08}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "コンテンツフィルタの深刻度レベル画像の削除"
}
```

### Explanation
この変更は、コンテンツフィルタに関連する深刻度レベルを示す画像（`severity-level.jpg`）が削除されたことを示しています。深刻度レベルの画像の削除は、特にその画像を参照しながら内容を理解しようとしているユーザーにとって、情報の欠如を引き起こす可能性があります。

この画像が削除されたことにより、使用者はどの深刻度レベルがどのように機能するのかについてのビジュアルガイダンスを失うことになります。これは、特に技術的な内容を理解する際に視覚的な情報に依存しているユーザーにとって大きな影響を及ぼす可能性があります。

そのため、このブレイキングチェンジは、コンテンツフィルタを利用するすべてのユーザーにとって重要な情報源を失うことを意味します。コンテンツフィルタの機能や使い方に関する影響、あるいは代替となる情報源やガイドラインを示すことが重要です。変更の理由を明示し、今後の参照先や利用方法についても考慮することが求められます。

## articles/ai-services/openai/media/content-filters/studio.png{#item-343759}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタスタジオ画像の更新"
}
```

### Explanation
この変更は、コンテンツフィルタに関連するスタジオ画像（`studio.png`）が修正されたことを示しています。具体的な変更内容は詳細に記載されていませんが、画像の更新は通常、視覚的な情報の改善、ブランドの更新、あるいは機能をより明確に伝えるために行われるものです。

画像の更新により、ユーザーはコンテンツフィルタの使用方法や機能についての理解が深まる可能性があります。また、最新のデザインやスタイルを反映させることで、ドキュメント全体の一貫性が保たれることも期待されます。

このマイナーアップデートは、特に新しいユーザーや情報に敏感なユーザーにとって、視覚的なアクセシビリティや理解を向上させる要素となるため、重要な改善と見なすことができます。ただし、具体的な変更点や改善された点については、公式のドキュメントやガイドラインと共に確認することが推奨されます。

## articles/ai-services/openai/media/fine-tuning/models.png{#item-140ef7}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングモデル画像の更新"
}
```

### Explanation
この変更は、ファインチューニングに関連するモデルの画像（`models.png`）が修正されたことを示しています。具体的な変更内容についての詳細は提供されていませんが、画像の更新は通常、表示内容の改善、情報の最新化、もしくはユーザーへの視覚的なメッセージの明確化を意図しています。

この画像が更新されることにより、ユーザーはファインチューニングプロセスやそれに関連するモデルに関する理解を深めることが期待されます。また、視覚的に情報を提供することが、ユーザーの学習を助ける重要な役割を果たします。

マイナーアップデートであるため、ユーザーに対する影響は軽微かもしれませんが、新しい画像によって、より良い利用体験が提供される可能性があります。また、更新された情報をもとに、ユーザーがファインチューニングのプロセスをより効果的に活用できるようサポートする役割も果たすでしょう。詳細な変更点については、公式のドキュメントやリソースを参照することが推奨されます。

## articles/ai-services/openai/media/fine-tuning/studio-advanced-options.png{#item-a35a88}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングスタジオの高度なオプション画像の更新"
}
```

### Explanation
この変更は、ファインチューニングに関連するスタジオの高度なオプションを示す画像（`studio-advanced-options.png`）が修正されたことを示しています。具体的な変更内容は記載されていませんが、画像の更新は一般的に情報の明確化や視覚的な改善を目的としています。

新しい画像は、ユーザーがファインチューニングの高度なオプションを理解する手助けをし、より効果的に作業を進められるようにする可能性があります。公式のドキュメントやガイドラインと連動して、この画像は視覚的なコンテンツとしてユーザーに情報を提供し、学習体験を向上させる重要な役割を果たします。

このマイナーアップデートは、特定の機能やオプションに関する情報をより正確に伝えることを目的としており、ユーザーが最新情報に基づいて作業を行うために重要です。詳しい変更点については、公式リソースを参照することが推奨されます。

## articles/ai-services/openai/media/fine-tuning/studio-continuous.png{#item-df67b2}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングスタジオの連続オプション画像の更新"
}
```

### Explanation
この変更は、ファインチューニングスタジオの連続オプションを示す画像（`studio-continuous.png`）が更新されたことを示しています。具体的な変更内容については記載されていませんが、画像の更新は通常、情報の正確性を向上させたり、視覚的表現を改善したりするために行われます。

この画像の更新により、ユーザーはファインチューニングプロセスにおける連続オプションに関してより明確な理解を得ることができるでしょう。視覚的なコンテンツは、特に技術的な情報を理解する上で重要であり、ユーザーの学習を支援する役割を果たします。

このマイナーアップデートは、ユーザーが最新の情報を基に効果的に作業を進めることを助け、ファインチューニングの活用を促進することが期待されます。具体的な変更点については、公式のドキュメントやリソースを確認することが推奨されます。

## articles/ai-services/openai/media/fine-tuning/studio-create-custom-model.png{#item-973d92}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムモデル作成スタジオの画像更新"
}
```

### Explanation
この変更は、カスタムモデルを作成する際に関連する画像（`studio-create-custom-model.png`）が更新されたことを示しています。具体的な変更内容は記載されていませんが、この更新は通常、視覚的な明確化や情報の正確性を向上させるために行われます。

新しい画像は、ユーザーに対してカスタムモデルの作成プロセスをより分かりやすく示すことを目的としています。技術的な操作や選択肢を説明する際に、視覚的なコンテンツは重要な役割を果たし、ユーザーの理解を助けるための手段となります。

このマイナーアップデートにより、最新の情報とともに、ユーザーがカスタムモデルを効率的に作成できるようになることが期待されます。詳細な変更内容については、公式ドキュメントを参照することが推奨されます。

## articles/ai-services/openai/media/fine-tuning/studio-model-details.png{#item-b997df}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル詳細スタジオの画像更新"
}
```

### Explanation
この変更は、モデル詳細を示す画像（`studio-model-details.png`）が更新されたことを示しています。具体的な変更内容については記載されていませんが、画像の更新は通常、情報の明確化や視覚的な改善を目的としています。

更新された画像により、ユーザーはファインチューニングスタジオにおけるモデルの詳細について、より直感的に理解できるようになることが期待されます。特に技術的な過程や設定に関する情報は、視覚的な表現によって大幅に理解が助けられるため、この更新は重要です。

このマイナーアップデートによって、ユーザーは最新の情報をもとにより効率的に作業を進めることができるでしょう。具体的な変更点については、公式のドキュメントやリソースを確認することが推奨されます。

## articles/ai-services/openai/media/fine-tuning/studio-models-deploy-model.png{#item-6001dd}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルデプロイメントスタジオの画像更新"
}
```

### Explanation
この変更は、モデルデプロイメントに関連する画像（`studio-models-deploy-model.png`）が更新されたことを示しています。更新内容の詳細は記載されていませんが、画像の改善や新しい情報の反映を目的としたマイナーな修正であると考えられます。

この画像の変更により、ユーザーはファインチューニングされたモデルをデプロイする際の手順やオプションをより理解しやすくすることができます。視覚的なガイドは、特に複雑な技術的プロセスにおいて、ユーザーが正しい操作を行うために重要です。

この更新によって、ユーザーは最新の情報に基づいてモデルをデプロイするプロセスを効率的に進めることができるようになります。具体的な変更点の詳細については、関連する公式ドキュメントを確認することが推奨されます。

## articles/ai-services/openai/media/fine-tuning/studio-models-deploy.png{#item-f8d724}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルデプロイメントに関する画像更新"
}
```

### Explanation
この変更は、モデルデプロイメントに関する画像（`studio-models-deploy.png`）が更新されたことを示しています。具体的な内容の変更は記載されていませんが、通常、画像の更新は情報の視覚的な向上や新しい手順の反映を目的としています。

この画像の改訂により、ユーザーはモデルをデプロイする際のプロセスや手順をより把握しやすくなることが期待されます。技術的な情報を含む画像は、特に新しいユーザーや技術に不慣れな方にとって、理解を助けるための重要な要素です。

このマイナーアップデートによって、視覚的なリソースが最新の情報を反映し、ユーザーがモデルを正確にデプロイする際のガイドとして役立つことを目指しています。詳細な変更点については、公式のドキュメントを参照することが推奨されます。

## articles/ai-services/openai/media/fine-tuning/studio-models-job-running.png{#item-695374}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ジョブ実行に関する画像更新"
}
```

### Explanation
この変更は、ジョブ実行に関する画像（`studio-models-job-running.png`）が更新されたことを示しています。具体的にどのような変更が行われたかは記載されていませんが、通常、この種の更新は情報の視覚的な改善を目的としています。

画像の更新によって、ユーザーはファインチューニング済みモデルの実行状況やプロセスをより効果的に理解できるようになることが期待されます。特に複雑な技術的な手順においては、視覚的な情報がユーザーの理解を助ける重要な要素となります。

このマイナーアップデートは、最新の情報を反映させたビジュアルリソースを提供することで、ユーザーがジョブの実行状況をより良く把握できるようにすることを目的としています。詳細な情報については、公式ドキュメントを確認することが推奨されます。

## articles/ai-services/openai/media/fine-tuning/studio-review.png{#item-ee9fdd}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルレビューに関する画像更新"
}
```

### Explanation
この変更は、モデルレビューに関連する画像（`studio-review.png`）が更新されたことを示しています。具体的な変更内容は提供されていませんが、一般的には画像の更新は情報の最新化や視覚的な改善を目的としています。

画像の内容は、モデルのレビュー過程や評価の指標を効果的に示すものであると考えられ、ユーザーがファインチューニングしたモデルの評価を理解する助けとなります。このような視覚資源は、ユーザーが技術的な手順を把握する上で重要です。

このマイナーアップデートによって、最新の情報が反映されたビジュアルリソースが提供されることで、ユーザーはより良い理解を得られることが期待されます。具体的な詳細については、公式のドキュメントを確認することをお勧めします。

## articles/ai-services/openai/media/fine-tuning/studio-training-data-blob.png{#item-a20ade}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トレーニングデータに関する画像更新"
}
```

### Explanation
この変更は、トレーニングデータに関連する画像（`studio-training-data-blob.png`）が更新されたことを意味しています。具体的な変更内容は記載されていませんが、画像の更新は通常、情報の最新化や視覚的な表現の向上を目的としています。

この画像は、トレーニングデータの構造や管理方法に関する視覚的なガイドを提供するものであり、ユーザーがファインチューニングのプロセスにおいてトレーニングデータを適切に扱う手助けとなることが期待されます。特に技術的な情報が多い場合、視覚的なコンテンツは理解をサポートする重要な要素です。

このマイナー更新によって、ユーザーは最新の情報を反映したビジュアルリソースを利用できるようになり、トレーニングデータの取り扱いについての理解をより深めることができます。詳細については、公式ドキュメントを参照することをお勧めします。

## articles/ai-services/openai/media/fine-tuning/studio-training-data-local.png{#item-514edb}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ローカルトレーニングデータに関する画像更新"
}
```

### Explanation
この変更は、ローカルトレーニングデータに関連する画像（`studio-training-data-local.png`）が更新されたことを示しています。具体的な変更内容は記録に残っていませんが、画像の更新は通常、情報の更新や内容の改善を目的としています。

この画像は、ローカル環境でのトレーニングデータの扱いや使用方法に関するビジュアルなガイドを提供しており、ユーザーが実際にローカルデータを活用する際の参考になることが期待されます。特に、操作手順や設定方法を理解するためには、視覚的な情報が非常に重要です。

このマイナーアップデートによって、ユーザーはより正確で新しい情報を基にした視覚リソースを使うことができ、ローカルトレーニングデータの取り扱いについての理解が深まることが望まれます。詳細は公式文書を参照することが推奨されます。

## articles/ai-services/openai/media/fine-tuning/studio-training-data.png{#item-a1df9a}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングのためのトレーニングデータ画像更新"
}
```

### Explanation
この変更は、ファインチューニングに関連するトレーニングデータの画像（`studio-training-data.png`）が更新されたことを示しています。具体的な変更内容は記載されていませんが、画像の更新は通常、情報の明確化や視覚的表現の改善を目的としています。

この画像は、ファインチューニングプロセスに必要なトレーニングデータの管理や視覚化に関する重要なリソースであり、ユーザーがファインチューニングを行う際に役立つ情報を提供します。特に、視覚的なコンテンツは複雑な情報を理解する上で効果的です。

このマイナーアップデートにより、ユーザーは最新かつ正確な情報をもとにしたビジュアルリソースを利用できるようになり、トレーニングデータを適切に扱うための理解が深まることが期待されます。詳細については、公式ドキュメントを確認することが勧められます。

## articles/ai-services/openai/media/fine-tuning/studio-validation-data-blob.png{#item-5a25bd}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バリデーションデータに関する画像更新"
}
```

### Explanation
この変更は、モデルのファインチューニングにおけるバリデーションデータを示す画像（`studio-validation-data-blob.png`）が更新されたことを示しています。具体的な変更内容は記録されていないものの、画像の更新は通常、情報の向上や内容の明確化を目的としています。

この画像は、バリデーションデータの利用とその意味合いに関する視覚的な情報を提供し、ユーザーがファインチューニングプロセスを理解するのに役立つことが期待されます。視覚的なリソースは、テキスト情報だけでは理解しにくい内容を補完し、重要な概念を効果的に伝える効果があります。

このマイナーアップデートによって、ユーザーは最新の情報を基にしたビジュアルリソースを使用でき、バリデーションデータの取り扱いやその重要性についての理解が深まることが見込まれます。詳細については、公式のドキュメントを参照することが推奨されます。

## articles/ai-services/openai/media/fine-tuning/studio-validation-data-local.png{#item-042951}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ローカルバリデーションデータ画像の更新"
}
```

### Explanation
この変更は、ファインチューニングにおけるローカルバリデーションデータを示す画像（`studio-validation-data-local.png`）が更新されたことを示しています。具体的な更新内容は記載されていませんが、画像の更新は通常、内容の明確化や視覚的な改善を目的としています。

この画像は、ローカルで使用されるバリデーションデータの手法やその重要性についての視覚的情報を提供します。ユーザーがファインチューニングプロセスを理解するうえで、視覚的なコンテンツは非常に役立ちます。特に、視覚的な要素はテキスト情報だけでは理解しにくい複雑なアイデアを説明するのに効果的です。

このマイナーアップデートにより、ユーザーは最新の情報を基にした画像を活用でき、ローカルバリデーションデータの適切な使用法やその意義についての理解が深まることが期待されます。詳細な情報については、公式ドキュメントを確認することが推奨されます。

## articles/ai-services/openai/media/fine-tuning/studio-validation-data.png{#item-9541db}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニング用バリデーションデータ画像の更新"
}
```

### Explanation
この変更は、ファインチューニングに使用されるバリデーションデータを示す画像（`studio-validation-data.png`）が更新されたことを示しています。具体的な変更内容は記載されていませんが、画像の更新は通常、情報の正確性や明確性の向上を目的としています。

この画像は、ファインチューニングプロセスにおけるバリデーションデータの役割を視覚的に説明するためのものであり、ユーザーがこのデータをどのように活用するかを理解する手助けとなることが期待されます。視覚的リソースは、テキストや数値情報だけでは伝えきれない重要な概念を簡潔に表現するのに有効です。

このマイナーアップデートによって、ユーザーは最新のビジュアル情報を基にファインチューニングを行うことができ、データの特性やその利用方法についての理解を深めることができるでしょう。詳細な内容については、関連する公式ドキュメントを参照することが推奨されます。

## articles/ai-services/openai/media/how-to/content-detection.png{#item-d8de97}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツ検出用画像の更新"
}
```

### Explanation
この変更は、コンテンツ検出に関する情報を視覚的に示す画像（`content-detection.png`）が更新されたことを示しています。具体的な変更内容は記載されていませんが、誤解を招く可能性のある古い情報を修正したり、視覚的な表現を改善したりするための一般的な更新であると考えられます。

この画像は、コンテンツ検出の手法や実装方法に関する理解を深めるために重要です。特に、テキストやコードの説明だけでは分かりにくいプロセスや結果をより明確にするためには、ビジュアル情報が有効です。このような更新が行われることで、ユーザーは新しい方法やベストプラクティスをより直感的に学ぶことができます。

このマイナーアップデートにより、ユーザーは最新の視覚リソースに基づいてコンテンツ検出機能の理解を深めることができ、技術の活用に役立つでしょう。詳細については関連ドキュメントを参照することが推奨されています。

## articles/ai-services/openai/media/how-to/potentially-abusive-user.png{#item-f49240}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "潜在的に悪用されるユーザーに関する画像の更新"
}
```

### Explanation
この変更は、潜在的に悪用されるユーザーに関する説明を補足するための画像（`potentially-abusive-user.png`）が更新されたことを示しています。具体的な変更内容は記載されていませんが、通常このような更新は、視覚情報の正確性や関連性を向上させるために行われます。

この画像は、悪用の可能性があるユーザーを識別する方法に関する重要な情報を視覚的に表現することを目的としており、ユーザーに対してその判断基準や注意点を伝える役割を果たします。適切な画像の使用により、テキストのみの説明では伝えきれない内容をより明確にすることができます。

このマイナーアップデートにより、ユーザーは最新の情報を基に潜在的な悪用のリスクについて理解を深めることができ、必要な対策を講じる手助けとなるでしょう。詳細な内容については関連する公式ドキュメントを参照することが推奨されています。

## articles/ai-services/openai/text-to-speech-quickstart.md{#item-c344ad}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.reviewer: v-baolianzou
 ms.author: eur
 author: eric-urban
 recommendations: false
-zone_pivot_groups: programming-languages-rest-js
+zone_pivot_groups: programming-languages-rest-js-cs
 ---
 
 # Quickstart: Text to speech with the Azure OpenAI Service
@@ -19,7 +19,6 @@ In this quickstart, you use the Azure OpenAI Service for text to speech with Ope
 
 The available voices are: `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer`. For more information, see [Azure OpenAI Service reference documentation for text to speech](./reference.md#text-to-speech).
 
-
 ::: zone pivot="rest-api"
 
 [!INCLUDE [REST API quickstart](includes/text-to-speech-rest.md)]
@@ -32,6 +31,12 @@ The available voices are: `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer
 
 ::: zone-end
 
+::: zone pivot="programming-language-dotnet"
+
+[!INCLUDE [.NET quickstart](includes/text-to-speech-dotnet.md)]
+
+::: zone-end
+
 ## Clean up resources
 
 If you want to clean up and remove an Azure OpenAI resource, you can delete the resource. Before deleting the resource, you must first delete any deployed models.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト読み上げクイックスタートの更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスを用いたテキスト読み上げのクイックスタートに関するドキュメント（`text-to-speech-quickstart.md`）の更新を示しています。具体的には、いくつかの新しいゾーンピボットが追加され、リファレンスをより分かりやすくするための細かい修正が行われました。

変更内容には以下が含まれています：
- `zone_pivot_groups`の値が`programming-languages-rest-js`から`programming-languages-rest-js-cs`に更新され、情報の精度が向上しました。
- 新しいゾーンピボットが追加され、.NETのクイックスタートへのリンクが提供されました。これにより、ユーザーは異なるプログラミング言語でのテキスト読み上げ機能の実装方法を容易に学ぶことができます。
- 不要な空行が削除され、全体の文書がすっきりとしました。

これらのマイナーな更新により、ユーザーはAzure OpenAIサービスのテキスト読み上げ機能をより効果的に利用できるようになります。詳細や具体的な使用方法については、リンク先のリファレンス文書を参照することが推奨されます。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ Customers who were already approved and have access to the model through the ear
 
 Support for the **o1 series** models was added in API version `2024-09-01-preview`.
 
-The `max_tokens` parameter has been deprecated and replaced with the new `max_completion_tokens` parameter. **o1 series** models will only work with the `max_completions_tokens` parameter.
+The `max_tokens` parameter has been deprecated and replaced with the new `max_completion_tokens` parameter. **o1 series** models will only work with the `max_completion_tokens` parameter.
 
 **Region availability**:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関する最新情報が記載された文書（`whats-new.md`）の更新を示しています。具体的には、`max_tokens`パラメーターの廃止と新しい`max_completion_tokens`パラメーターの導入に関する記述の表現が修正されました。

修正された箇所は以下の通りです：
- `max_tokens`パラメーターに関する説明が一行変更され、旧バージョンの説明がより明確に、且つ正確なパラメータ名（`max_completion_tokens`）を用いて記載されています。
- この変更により、ユーザーは最新のAPI仕様に基づく正しいパラメータを理解しやすくなり、特に**o1シリーズ**モデルの利用に際しての混乱を避けることができるようになります。

このマイナーアップデートによって、利用者は新しいパラメータを正しく利用し、機能を最大限に活用できるようになるでしょう。詳細な情報は、関連の公式ドキュメントを参照することが推奨されています。

## articles/ai-services/openai/whisper-quickstart.md{#item-4cae3d}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.reviewer: v-baolianzou
 ms.author: eur
 author: eric-urban
 recommendations: false
-zone_pivot_groups: programming-languages-rest-ps-py-js
+zone_pivot_groups: programming-languages-rest-ps-py-js-cs
 ---
 
 # Quickstart: Speech to text with the Azure OpenAI Whisper model
@@ -32,6 +32,12 @@ The file size limit for the Whisper model is 25 MB. If you need to transcribe a
 
 ::: zone-end
 
+::: zone pivot="programming-language-dotnet"
+
+[!INCLUDE [.NET SDK quickstart](includes/whisper-dotnet.md)]
+
+::: zone-end
+
 ::: zone pivot="programming-language-javascript"
 
 [!INCLUDE [JavaScript quickstart](includes/whisper-javascript.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisperモデルのクイックスタートの更新"
}
```

### Explanation
この変更は、Azure OpenAI Whisperモデルに関するクイックスタート文書（`whisper-quickstart.md`）の更新を示しています。主に、プログラミング言語に関連する情報が追加され、使いやすさが向上しました。

具体的な変更点は以下の通りです：
- `zone_pivot_groups`の値が拡張され、`programming-languages-rest-ps-py-js`から`programming-languages-rest-ps-py-js-cs`に変更されました。これにより、.NETを使用した開発者向けの情報が追加されました。
- 新たに.NET用のゾーンピボットが導入され、Whisperモデルを使用した.NET SDKのクイックスタートへのリンクが追加されました。これにより、.NET開発者がWhisperモデルをより簡単に利用できるようになりました。
- 他のプログラミング言語（JavaScriptなど）用のクイックスタートへのリンクも引き続き提供されています。

これらのマイナー更新は、ユーザーが関心のあるプログラミング言語でWhisperモデルの機能を効果的に活用できるよう支援することを目的としています。詳細な情報や具体的な使用方法については、追加されたリンクを通じて確認することができます。


