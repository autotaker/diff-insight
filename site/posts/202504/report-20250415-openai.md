---
date: '2025-04-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f2cba99...MicrosoftDocs:1f18936
summary: このコードの差分では、Azure OpenAIに関連するドキュメントが更新され、新しい「GPT-4.1」モデルの導入やバッチ処理、クォータに関する詳細な情報が追加されています。これにより、ユーザーは新機能や制限をより理解しやすくなります。特に新モデルは性能を向上させ、バッチ処理に関してはより明確なガイドラインが提供され、ユーザーの利便性が向上します。また、クォータに関する情報も豊富になり、リソース管理が容易になります。全体として、ユーザーは最新技術を活用しやすくなっています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f2cba99...MicrosoftDocs:1f18936){target="_blank"}

<format>
# Highlights
このコードの差分では、Azure OpenAIに関連する複数のドキュメントが細かく更新されています。主なハイライトとしては、新しい「GPT-4.1」モデルの導入、およびバッチ処理とクォータに関する詳細な説明の追加が挙げられます。これにより、ユーザーの利便性と理解が向上される変更となっています。

## New features
- 新しい「GPT-4.1」モデルのリリース情報とその特性の記載。
- バッチ処理に関する新しい設定オプションの導入。
- クォータに関する情報がモデル別に更新されました。

## Breaking changes
- 特に開発者やユーザー側に影響を与えるような破壊的変更は報告されていません。

## Other updates
- 各ドキュメントの更新日が刷新され、より現在の内容と整合しています。
- 説明文や記述が一部改善され、ドキュメントの可読性が向上しました。

# Insights
このドキュメントの更新は、Azure OpenAIプラットフォームのユーザーが新機能や制限を正確に理解し、適切に活用するためのものです。

特に「GPT-4.1」の導入は、モデルの性能や機能性の向上を示しています。このシリーズでは、従来のモデルに比べてより多くのコンテキストを扱うことが可能になり、企業および一般ユーザーがそのコンピューティング能力をより効果的に利用するための選択肢を提供します。

バッチ処理に関しては、PythonドキュメントおよびREST APIドキュメントの両方に対して、グローバルなバッチ展開とファイルの有効期限設定に関するより明確なガイドラインが追加されました。これは大量データ処理に携わる開発者にとって重要な改善点です。具体的なファイルアップロードおよび出力ファイルの取り扱い方の詳細が強調されており、それによって処理効率の向上とエラーの削減が期待できます。

クォータおよび制限に関する更新は、ユーザーが異なるプランに基づくリソースの消耗管理を行う上での指針を提供します。複数のティアにおける新しい制限とトークンの管理方法について詳細な情報が示されており、拡張されたサービスを無駄なく利用するための助けとなります。

今回のドキュメント改訂によって、ユーザーはAzure OpenAIサービスの機能を余すことなく活用し、最新の技術を取り入れたサービス環境を構築できるようになります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | モデルに関する最新情報の更新 | modified | 18 | 3 | 21 | 
| [batch-python.md](#item-3121c2) | minor update | バッチ処理に関するPythonのドキュメントの更新 | modified | 34 | 13 | 47 | 
| [batch-rest.md](#item-bcccd9) | minor update | バッチ処理に関するREST APIドキュメントの更新 | modified | 26 | 11 | 37 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータおよび制限に関するドキュメントの更新 | modified | 12 | 4 | 16 | 
| [whats-new.md](#item-53303b) | minor update | Azure OpenAIサービスの新機能に関する記事の更新 | modified | 8 | 2 | 10 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,11 +4,11 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 04/01/2025
+ms.date: 04/14/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
-ms.author: mbullwin #chrhoder
+ms.author: mbullwin #chrhoder#
 recommendations: false
 ---
 
@@ -18,6 +18,7 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 
 | Models | Description |
 |--|--|
+| [GPT-4.1 series](#gpt-41-series) | Latest model release from Azure OpenAI |
 | [computer-use-preview](#computer-use-preview) | An experimental model trained for use with the Responses API computer use tool. |
 | [GPT-4.5 Preview](#gpt-45-preview) |The latest GPT model that excels at diverse text and image tasks.  |
 | [o-series models](#o-series-models) |[Reasoning models](../how-to/reasoning.md) with advanced problem-solving and increased focus and capability.  |
@@ -30,6 +31,20 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 | [Whisper](#whisper-models) | A series of models in preview that can transcribe and translate speech to text. |
 | [Text to speech](#text-to-speech-models-preview) (Preview) | A series of models in preview that can synthesize text to speech. |
 
+## GPT 4.1 series
+
+### Region Availability
+
+| Model | Region |
+|---|---|
+| `gpt-4.1` (2025-04-14) | East US2 (Global Standard), Sweden Central (Global Standard) |
+
+### Capabilities
+
+|  Model ID  | Description | Context Window | Max Output Tokens | Training Data (up to)  |
+|  --- |  :--- |:--- |:---|:---: |
+| `gpt-4.1` (2025-04-14) <br> <br> **Latest model from Azure OpenAI**  | - Text & image input <br> - Text output <br> - Chat completions API <br>- Responses API <br> - Streaming <br> - Function calling <br> Structured outputs (chat completions)   | 1,047,576 | 32,768 | May 31, 2024 |
+
 ## computer-use-preview
 
 An experimental model trained for use with the [Responses API](../how-to/responses.md) computer use tool. It can be used in conjunction with 3rd-party libraries to allow the model to control mouse & keyboard input while getting context from screenshots of the current environment.
@@ -70,7 +85,7 @@ Once access has been granted, you will need to create a deployment for the model
 
 |  Model ID  | Description | Context Window | Max Output Tokens | Training Data (up to)  |
 |  --- |  :--- |:--- |:---|:---: |
-| `gpt-4.5-preview` (2025-02-27) <br> **GPT-4.5 Preview**  | The **latest GPT model** that excels at diverse text and image tasks. <br>-Structured outputs <br>-Prompt caching <br>-Tools <br>-Streaming<br>-Text(input/output)<br>- Image(input)   | 128,000 | 16,384 | Oct 2023 |
+| `gpt-4.5-preview` (2025-02-27) <br> **GPT-4.5 Preview**  | [GPT 4.1](#gpt-41-series) is the recommended replacement for this model. Excels at diverse text and image tasks. <br>-Structured outputs <br>-Prompt caching <br>-Tools <br>-Streaming<br>-Text(input/output)<br>- Image(input)   | 128,000 | 16,384 | Oct 2023 |
 
 > [!NOTE]
 > It is expected behavior that the model cannot answer questions about itself. If you want to know when the knowledge cutoff for the model's training data is, or other details about the model you should refer to the model documentation above.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルに関する最新情報の更新"
}
```

### Explanation
この変更は、Azure OpenAI の「モデル」に関するドキュメントの特定の部分を更新しています。主に、モデルに関する情報が追加され、新しい「GPT-4.1」シリーズのモデルが新たに紹介されています。また、いくつかの既存のモデルに関する詳細な説明が強化され、更新日が改訂されています。具体的には、以下の変更が含まれています：

- 更新された日付が「04/01/2025」から「04/14/2025」に変更されました。
- 新しい「GPT-4.1シリーズ」モデルのリリースに関する情報が追加され、新しいモデルの地域的な可用性と機能が明記されました。
- 「computer-use-preview」モデルの説明が追加され、このモデルがどのようにして他のツールと連携するのかが詳述されています。
- 一部の既存モデルに関する情報が更新され、推奨される置き換えモデルとして「GPT 4.1」が挙げられています。

これにより、利用者は新しいモデルの利点や特性を理解しやすくなり、最新の情報にアクセスできるようになります。

## articles/ai-services/openai/includes/batch/batch-python.md{#item-3121c2}

<details>
<summary>Diff</summary>
````diff
@@ -75,7 +75,7 @@ The `custom_id` is required to allow you to identify which individual batch requ
 
 ### Create input file
 
-For this article we'll create a file named `test.jsonl` and will copy the contents from standard input code block above to the file. You will need to modify and add your global batch deployment name to each line of the file. Save this file in the same directory that you're executing your Jupyter Notebook.
+For this article we'll create a file named `test.jsonl` and will copy the contents from standard input code block above to the file. You'll need to modify and add your global batch deployment name to each line of the file. Save this file in the same directory that you're executing your Jupyter Notebook.
 
 ## Upload batch file
 
@@ -101,10 +101,15 @@ client = AzureOpenAI(
 # Upload a file with a purpose of "batch"
 file = client.files.create(
   file=open("test.jsonl", "rb"), 
-  purpose="batch"
+  purpose="batch",
+  #extra_body={"expires_after":{"seconds": 1209600, "anchor": "created_at"}} # Optional you can set to a number between 1209600-2592000. This is equivalent to 14-30 days
 )
 
+
 print(file.model_dump_json(indent=2))
+
+#print(f"File expiration: {datetime.fromtimestamp(file.expires_at) if file.expires_at is not None else 'Not set'}")
+
 file_id = file.id
 ```
 
@@ -125,30 +130,41 @@ client = AzureOpenAI(
 # Upload a file with a purpose of "batch"
 file = client.files.create(
   file=open("test.jsonl", "rb"), 
-  purpose="batch"
+  purpose="batch",
+  #extra_body={"expires_after":{"seconds": 1209600, "anchor": "created_at"}} # Optional you can set to a number between 1209600-2592000. This is equivalent to 14-30 days
 )
 
+
 print(file.model_dump_json(indent=2))
+
+#print(f"File expiration: {datetime.fromtimestamp(file.expires_at) if file.expires_at is not None else 'Not set'}")
+
 file_id = file.id
 ```
 
 ---
 
+By uncommenting and adding `extra_body={"expires_after":{"seconds": 1209600, "anchor": "created_at"}}` you're setting our upload file to expire in 14 days. There's a max limit of 500 batch files per resource when no expiration is set. By setting a value for expiration the number of batch files per resource is increased to 10,000 files per resource. This feature isn't currently available in all regions. Output when file upload expiration is set:
+
 **Output:**
 
 ```json
 {
-  "id": "file-9f3a81d899b4442f98b640e4bc3535dd",
-  "bytes": 815,
-  "created_at": 1722476551,
+  "id": "file-655111ec9cfc44489d9af078f08116ef",
+  "bytes": 176064,
+  "created_at": 1743391067,
   "filename": "test.jsonl",
   "object": "file",
   "purpose": "batch",
-  "status": null,
+  "status": "processed",
+  "expires_at": 1744600667,
   "status_details": null
 }
+File expiration: 2025-04-13 23:17:47
 ```
 
+
+
 ## Create batch job
 
 Once your file has uploaded successfully you can submit the file for batch processing.
@@ -159,16 +175,21 @@ batch_response = client.batches.create(
     input_file_id=file_id,
     endpoint="/chat/completions",
     completion_window="24h",
+    #extra_body={"output_expires_after":{"seconds": 1209600, "anchor": "created_at"}} # Optional you can set to a number between 1209600-2592000. This is equivalent to 14-30 days
 )
 
+
 # Save batch ID for later use
 batch_id = batch_response.id
 
 print(batch_response.model_dump_json(indent=2))
+
 ```
 
+The default 500 max file limit per resource also applies to output files. Here you can uncomment this line to add  `extra_body={"output_expires_after":{"seconds": 1209600, "anchor": "created_at"}}` so that your output files expire in 14 days. By setting a value for expiration the number of batch files per resource is increased to 10,000 files per resource. This feature isn't currently available in all regions.
+
 > [!NOTE]
-> Currently the completion window must be set to 24h. If you set any other value than 24h your job will fail. Jobs taking longer than 24 hours will continue to execute until canceled.
+> Currently the completion window must be set to `24h`. If you set any other value than `24h` your job will fail. Jobs taking longer than 24 hours will continue to execute until canceled.
 
 **Output:**
 
@@ -178,7 +199,7 @@ print(batch_response.model_dump_json(indent=2))
   "completion_window": "24h",
   "created_at": 1722476583,
   "endpoint": null,
-  "input_file_id": "file-9f3a81d899b4442f98b640e4bc3535dd",
+  "input_file_id": "file-655111ec9cfc44489d9af078f08116ef",
   "object": "batch",
   "status": "validating",
   "cancelled_at": null,
@@ -201,7 +222,7 @@ print(batch_response.model_dump_json(indent=2))
 }
 ```
 
-If your batch jobs are so large that you are hitting the enqueued token limit even after maxing out the quota for your deployment, certain regions now support a new [fail fast](#queueing-batch-jobs) feature that allows you to queue multiple batch jobs with exponential backoff so once one large batch job completes the next can be kicked off automatically. To learn more about what regions support this feature and how to adapt your code to take advantage of it, see [queuing batch jobs](#queueing-batch-jobs).  
+If your batch jobs are so large that you're hitting the enqueued token limit even after maxing out the quota for your deployment, certain regions now support a new [fail fast](#queueing-batch-jobs) feature that allows you to queue multiple batch jobs with exponential backoff so once one large batch job completes the next can be kicked off automatically. To learn more about what regions support this feature and how to adapt your code to take advantage of it, see [queuing batch jobs](#queueing-batch-jobs).  
 
 ## Track batch job progress
 
@@ -311,7 +332,7 @@ if output_file_id:
 
 **Output:**
 
-For brevity, we are only including a single chat completion response of output. If you follow the steps in this article you should have three responses similar to the one below:
+For brevity, we're only including a single chat completion response of output. If you follow the steps in this article you should have three responses similar to the one below:
 
 ```json
 {
@@ -429,7 +450,7 @@ print(all_jobs)
 
 Use the REST API to list all batch jobs with additional sorting/filtering options.
 
-In the examples below we are providing the `generate_time_filter` function to make constructing the filter easier. If you don't wish to use this function the format of the filter string would look like `created_at gt 1728860560 and status eq 'Completed'`.
+In the examples below we're providing the `generate_time_filter` function to make constructing the filter easier. If you don't wish to use this function the format of the filter string would look like `created_at gt 1728860560 and status eq 'Completed'`.
 
 # [Python (Microsoft Entra ID)](#tab/python-secure)
 
@@ -626,7 +647,7 @@ else:
 
 ## Queueing batch jobs
 
-If your batch jobs are so large that you are hitting the enqueued token limit even after maxing out the quota for your deployment, certain regions now support a new fail fast feature that allows you to queue multiple batch jobs with exponential backoff. Once one large batch job completes and your enqueued token quota is once again available, the next batch job can be created and kicked off automatically. 
+If your batch jobs are so large that you're hitting the enqueued token limit even after maxing out the quota for your deployment, certain regions now support a new fail fast feature that allows you to queue multiple batch jobs with exponential backoff. Once one large batch job completes and your enqueued token quota is once again available, the next batch job can be created and kicked off automatically. 
 
 **Old behavior:**
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理に関するPythonのドキュメントの更新"
}
```

### Explanation
この変更では、Azure OpenAI の「バッチ処理」に関する Python のドキュメントが更新され、いくつかの新しい情報が追加されました。主な変更点は次のとおりです：

- 入力ファイル作成セクションで、ユーザーが `test.jsonl` ファイルを作成する際に、グローバルバッチ展開名を行に追加する必要があることが、より明確に説明されています。
- ファイルアップロードの際のオプション引数 `extra_body` に関する情報が追加され、ファイルの有効期限を設定することで、リソースあたりのバッチファイルの最大数を増やすことができることが説明されています。このオプションを使用すると、有効期限を設定して10,000ファイルまで増加させることが可能です。
- バッチジョブを作成する際の最大ファイル制限に関する説明も更新され、出力ファイルにも同様の制限が適用されることが記載されました。
- 一部の文で言い回しが改善され、読みやすさが向上しています。

この更新により、ユーザーはバッチ処理に際しての設定や制約をより正確に理解できるようになります。

## articles/ai-services/openai/includes/batch/batch-rest.md{#item-bcccd9}

<details>
<summary>Diff</summary>
````diff
@@ -65,7 +65,7 @@ The `custom_id` is required to allow you to identify which individual batch requ
 
 ### Create input file
 
-For this article we'll create a file named `test.jsonl` and will copy the contents from standard input code block above to the file. You will need to modify and add your global batch deployment name to each line of the file.
+For this article we'll create a file named `test.jsonl` and will copy the contents from standard input code block above to the file. You'll need to modify and add your global batch deployment name to each line of the file.
 
 ## Upload batch file
 
@@ -78,21 +78,29 @@ curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files?api-versio
   -H "Content-Type: multipart/form-data" \
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -F "purpose=batch" \
-  -F "file=@C:\\batch\\test.jsonl;type=application/json"
+  -F "file=@C:\\batch\\test.jsonl;type=application/json" \
+  -F "expires_after.seconds=1209600" \
+  -F "expires_after.anchor=created_at"
+
 ```
 
-The above code assumes a particular file path for your test.jsonl file. Adjust this file path as necessary for your local system.
+The above code assumes a particular file path for your test.jsonl file. Adjust this file path as necessary for your local system. 
+
+By adding the optional `"expires_after.seconds=1209600"` and `"expires_after.anchor=created_at"` parameters  you're setting your upload file to expire in 14 days. There's a max limit of 500 batch files per resource when no expiration is set. By setting a value for expiration the number of batch files per resource is increased to 10,000 files per resource. You can set to a number between 1209600-2592000. This is equivalent to 14-30 days. This feature isn't currently available in all regions.
+
+
 
 **Output:**
 
 ```json
 {
-  "status": "pending",
-  "bytes": 686,
+  "status": "processed",
+  "bytes": 817,
   "purpose": "batch",
   "filename": "test.jsonl",
-  "id": "file-21006e70789246658b86a1fc205899a4",
-  "created_at": 1721408291,
+  "expires_at": 1744607747,
+  "id": "file-7733bc35e32841e297a62a9ee50b3461",
+  "created_at": 1743398147,
   "object": "file"
 }
 
@@ -116,7 +124,8 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{file-id}?api-vers
   "bytes": 686,
   "purpose": "batch",
   "filename": "test.jsonl",
-  "id": "file-21006e70789246658b86a1fc205899a4",
+  "expires_at": 1744607747,
+  "id": "file-7733bc35e32841e297a62a9ee50b3461",
   "created_at": 1721408291,
   "object": "file"
 }
@@ -134,12 +143,18 @@ curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-vers
   -d '{
     "input_file_id": "file-abc123",
     "endpoint": "/chat/completions",
-    "completion_window": "24h"
+    "completion_window": "24h",
+    "output_expires_after": {
+        "seconds": 1209600
+    },
+    "anchor": "created_at"
   }'
 ```
 
+The default 500 max file limit per resource also applies to output files. Here you can optionally add  `"output_expires_after":{"seconds": 1209600},` and `"anchor": "created_at"` so that your output files expire in 14 days. By setting a value for expiration the number of batch files per resource is increased to 10,000 files per resource. The file expiration feature is currently not available in all regions.
+
 > [!NOTE]
-> Currently the completion window must be set to 24h. If you set any other value than 24h your job will fail. Jobs taking longer than 24 hours will continue to execute until canceled.
+> Currently the completion window must be set to `24h`. If you set any other value than `24h` your job will fail. Jobs taking longer than 24 hours will continue to execute until canceled.
 
 **Output:**
 
@@ -221,7 +236,7 @@ The following status values are possible:
 | `in_progress`|The input file was successfully validated and the batch is currently running. |
 | `finalizing`|The batch has completed and the results are being prepared. |
 | `completed`|The batch has been completed and the results are ready.  |
-| `expired`|The batch was not able to be completed within the 24-hour time window.|
+| `expired`|The batch wasn't able to be completed within the 24-hour time window.|
 | `cancelling`|The batch is being `cancelled` (This can take up to 10 minutes to go into effect.) |
 | `cancelled`|the batch was `cancelled`.|
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理に関するREST APIドキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAI のバッチ処理に関するREST APIのドキュメントを更新したもので、以下の重要な点が含まれています：

- `test.jsonl` というファイルの作成に関する説明が微調整されており、ユーザーがグローバルバッチ展開名を行に追加する必要があることが強調されています。
- バッチファイルのアップロードに関して、`expires_after` パラメータ（有効期限）を追加するオプションが明示的に説明されています。これにより、ファイルの有効期限を設定し、リソースあたりのバッチファイルの最大数を500から10,000に増やすことができることが強調されています。このオプションは、最大で14日（1,209,600秒）から30日（2,592,000秒）間の有効期限を設定可能です。
- バッチ作成の際に出力ファイルの有効期限を設定するオプションについても説明が追加され、出力ファイルも同様に最大数の制限が適用されることについて記載されています。
- 文中の一部表現が改良され、明確さが増し、より読みやすくなっています。

これにより、ユーザーはバッチ処理に関連する新たなオプションや機能についての理解を深め、その使用方法をより効果的に学ぶことができるようになります。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 4/09/2025
+ms.date: 4/14/2025
 ms.author: mbullwin
 ---
 
@@ -60,6 +60,14 @@ The following sections provide you with a quick guide to the default quotas and
 
 [!INCLUDE [Quota](./includes/global-batch-limits.md)]
 
+## GPT 4.1 series
+
+| Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
+|---|---|:---:|:---:|
+| `gpt-4.1` (2025-04-14) | Enterprise Tier | 5 M | 5 K |
+| `gpt-4.1` (2025-04-14) | Default | 1 M | 1 K |
+
+
 ## computer-use-preview global standard
 
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
@@ -199,9 +207,9 @@ If your Azure subscription is linked to certain [offer types](https://azure.micr
 
 |Tier| Quota Limit in tokens per minute (TPM) |
 |---|:---|
-|`Azure for Students` | 1 K (all models) <br>Exception o-series & GPT 4.5 Preview: 0|
-| `MSDN` | GPT-4o-mini: 200 K <br> GPT 3.5 Turbo Series: 200 K <br> GPT-4 series: 50 K <br>computer-use-preview: 8 K <br> gpt-4o-realtime-preview: 1 K <br> o-series: 0 <br> GPT 4.5 Preview: 0  |
-|`Pay-as-you-go` | GPT-4o-mini: 200 K <br> GPT 3.5 Turbo Series: 200 K <br> GPT-4 series: 50 K <br>computer-use-preview: 30 K <br> o-series: 0 <br> GPT 4.5 Preview: 0   |
+|`Azure for Students` | 1 K (all models) <br>Exception o-series & GPT-4.1 & GPT 4.5 Preview: 0|
+| `MSDN` | GPT-4o-mini: 200 K <br> GPT 3.5 Turbo Series: 200 K <br> GPT-4 series: 50 K <br>computer-use-preview: 8 K <br> gpt-4o-realtime-preview: 1 K <br> o-series: 0 <br> GPT 4.5 Preview: 0 <br> GPT-4.1: 0  |
+|`Pay-as-you-go` | GPT-4o-mini: 200 K <br> GPT 3.5 Turbo Series: 200 K <br> GPT-4 series: 50 K <br>computer-use-preview: 30 K <br> o-series: 0 <br> GPT 4.5 Preview: 0  <br> GPT-4.1: 0  |
 | `Azure_MS-AZR-0111P`  <br> `Azure_MS-AZR-0035P` <br> `Azure_MS-AZR-0025P` <br> `Azure_MS-AZR-0052P` <br>| GPT-4o-mini: 200 K <br> GPT 3.5 Turbo Series: 200 K <br> GPT-4 series: 50 K   |
 | `CSP Integration Sandbox` <sup>*</sup> | All models: 0 |
 | `Lightweight trial`<br>`Free Trials`<br>`Azure Pass`  | All models: 0 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータおよび制限に関するドキュメントの更新"
}
```

### Explanation
この変更では、Azure OpenAI のクォータおよび制限に関するドキュメントが修正され、以下の重要な情報が追加および更新されました：

- ドキュメントの更新日が変更され、以前の「2025年4月9日」から「2025年4月14日」に更新されました。
- 新たに「GPT 4.1シリーズ」に関するセクションが追加され、このモデルに対するトークンの制限（TPM）やリクエスト数に関するクォータが明記されました。具体的には、エンタープライズティアでは1分あたり5Mトークンと5Kリクエスト、デフォルトでは1分あたり1Mトークンと1Kリクエストの制限が設定されています。
- 「Azure for Students」、「MSDN」、「Pay-as-you-go」プランに関するクォータの詳細も更新され、GPT 4.1とGPT 4.5プレビューに関する制限が追加されました。

これらの更新により、ユーザーは新しいモデルの利用可能性や、異なるプランにおける具体的な制限についてより詳細に理解できるようになります。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -4,21 +4,27 @@ titleSuffix: Azure AI services
 description: Learn about the latest news and features updates for Azure OpenAI.
 manager: nitinme
 author: mrbullwinkle
-ms.author: mbullwin
+ms.author: mbullwin #
 ms.service: azure-ai-openai
 ms.custom:
   - ignite-2023
   - references_regions
   - ignite-2024
 ms.topic: whats-new
-ms.date: 03/05/2025
+ms.date: 04/14/2025
 recommendations: false
 ---
 
 # What's new in Azure OpenAI Service
 
 This article provides a summary of the latest releases and major documentation updates for Azure OpenAI Service.
 
+## April 2025
+
+### GPT-4.1 released
+
+The latest model from Azure OpenAI with a 1 million token context limit. For more information, see the [models page](./concepts/models.md#gpt-41-series).
+
 ## March 2025
 
 ### Responses API & computer-use-preview model
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスの新機能に関する記事の更新"
}
```

### Explanation
この変更では、Azure OpenAIサービスに関する「What's New」記事が更新され、以下のポイントが追加されています：

- ドキュメントの更新日が「2025年3月5日」から「2025年4月14日」に変更されました。
- 新たに「2025年4月」のセクションが追加され、「GPT-4.1」モデルのリリースが特記されました。このモデルは1百万トークンのコンテキスト制限を持ち、詳細は関連するモデルのページに記載されています。
- また、著者名といくつかのカスタムメタデータが更新され、新しい情報や関連するイベント（例：ignite-2024）が追加されています。

これらの更新により、ユーザーは最新のリリースとドキュメント更新の概要を把握することができ、新しいモデルについての具体的な情報を得ることができます。


