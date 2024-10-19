---
date: '2024-10-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6e9a4a2...MicrosoftDocs:418033b
summary: 今回の報告では、Azure OpenAIサービスにおけるバッチ操作および構造化出力のサポートが強化されたことが強調されています。新しいAPIバージョン`2024-08-01-preview`で構造化出力が利用可能になり、具体的なコード例も追加されました。これにより、ユーザーはデータをより効率的に処理できるようになります。また、ドキュメントの更新により、日付や著者情報の整理が行われ、説明が明確化されることで、ユーザーの理解が向上することが期待されています。現在、報告された破壊的変更はありません。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6e9a4a2...MicrosoftDocs:418033b){target="_blank"}

# ハイライト

- **新機能**: Azure OpenAIサービスにおけるバッチ操作および構造化出力のサポートが拡充。APIの新しいバージョンである`2024-08-01-preview`で構造化出力がサポートされ、具体的なコード例が追加されました。
- **その他の更新**: ドキュメントの日付や著者情報の更新、説明の整理などにより、ユーザーの理解が向上。

## 新機能

- バッチ処理における構造化出力のサポートが強化され、Python、REST API、スタジオに関する具体的なコード例が追加されました。
- APIバージョン`2024-08-01-preview`以降で構造化出力を利用可能になりました。

## ブレイキングチェンジ（破壊的変更）

- 現時点で破壊的変更は特に報告されていません。

## その他の更新

- 日付、著者情報、APIバージョンの更新。
- 説明の明確化と読みやすさの向上を目的としたテキスト整理。

# インサイト

今回の変更は、Azure OpenAIの既存機能をより充実させるためのもので、特に構造化出力に関するサポートが強化されました。構造化出力はデータの可視化や整理において重要な役割を果たし、今後より多くのユースケースで活用されることが期待されます。

## 技術的背景

AIや機械学習の分野では、大量のデータを効率的に処理し、価値のある情報を抽出することが重要です。今回の構造化出力のサポートは、ユーザーがデータを扱いやすくするとともに、実際のプロジェクトやビジネスアプリケーションでのAIの活用をより現実的にしています。

特に、バッチ処理において構造化出力がサポートされることで、ユーザーは複数のデータポイントを一度に処理し、カスタマイズされたレスポンスを得ることができます。これにより、データ処理の効率が向上し、結果としてより素早い意思決定が可能になります。

## 更新の意図

アップデートの意図としては、最新のAPIバージョンでサポートされた新機能をユーザーに周知し、効果的に利用できるようにすることがあります。ドキュメントの明確化は、開発者が実装を簡単に理解し、導入をスムーズに行うための一助となります。また、具体的なコード例の追加は、具体的な実装に際してのガイドラインとして機能します。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [batch.md](#item-a131d5) | minor update | バッチ操作に関する更新 | modified | 3 | 72 | 75 | 
| [code-interpreter.md](#item-95efbd) | minor update | コードインタプリタに関する更新 | modified | 14 | 10 | 24 | 
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | プロビジョンドスループットオンボーディングに関する更新 | modified | 2 | 2 | 4 | 
| [structured-outputs.md](#item-cc2557) | minor update | 構造化出力に関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [batch-python.md](#item-3121c2) | minor update | バッチ処理における構造化出力のサポートを追加 | modified | 6 | 0 | 6 | 
| [batch-rest.md](#item-bcccd9) | minor update | バッチ処理における構造化出力のサポートを追加 | modified | 6 | 0 | 6 | 
| [batch-studio.md](#item-d4822e) | minor update | バッチスタジオに構造化出力のサポートを追加 | modified | 7 | 0 | 7 | 


# Modified Contents
## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: references_regions
 ms.topic: how-to
-ms.date: 10/14/2024
+ms.date: 10/18/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -67,19 +67,15 @@ Refer to the [models page](../concepts/models.md) for the most up-to-date inform
 
 API support was first added with `2024-07-01-preview`. Use `2024-10-01-preview` to take advantage of the latest features.
 
-### Not supported
+### Feature support
 
 The following aren't currently supported:
 
 - Integration with the Assistants API.
 - Integration with Azure OpenAI On Your Data feature.
 
 > [!NOTE]
-> There is a known issue with Azure OpenAI global batch and [structured outputs](./structured-outputs.md). Currently, lines in your jsonl file with structured output requests will fail with the following error message written to the error file:
->
-> ***response_format value as json_schema is enabled only for api versions 2024-08-01-preview and later***.
->
->This error will occur even when your code targets the latest preview APIs which support structured outputs. Once the issue is resolved, this page will be updated.
+> Structured outputs is now supported with Global Batch when used in conjunction with API version `2024-08-01-preview` or later. Use `2024-10-01-preview` for the latest features.
 
 ### Global batch deployment
 
@@ -157,71 +153,6 @@ Yes. Similar to other deployment types, you can create content filters and assoc
 
 Yes, from the quota page in the Studio UI. Default quota allocation can be found in the [quota and limits article](../quotas-limits.md#global-batch-quota).
 
-### How do I tell how many tokens my batch request contains, and how many tokens are available as quota?
-
-The `2024-10-01-preview` REST API adds two new response headers:
-
-* `deployment-enqueued-tokens` - A approximate token count for your jsonl file calculated immediately after the batch request is submitted. This value represents an estimate based on the number of characters and is not the true token count.
-* `deployment-maximum-enqueued-tokens` The total available enqueued tokens available for this global batch model deployment.
-
-These response headers are only available when making a POST request to begin batch processing of a file with the REST API. The language specific client libraries do not currently return these new response headers. To return all response headers you can add `-i` to the standard REST request.
-
-```http
-curl -i -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024-10-01-preview \
-  -H "api-key: $AZURE_OPENAI_API_KEY" \
-  -H "Content-Type: application/json" \
-  -d '{
-    "input_file_id": "file-abc123",
-    "endpoint": "/chat/completions",
-    "completion_window": "24h"
-  }'
-```
-
-```output
-HTTP/1.1 200 OK
-Content-Length: 619
-Content-Type: application/json; charset=utf-8
-Vary: Accept-Encoding
-Request-Context: appId=
-x-ms-response-type: standard
-deployment-enqueued-tokens: 139
-deployment-maximum-enqueued-tokens: 740000
-Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
-X-Content-Type-Options: nosniff
-x-aml-cluster: vienna-swedencentral-01
-x-request-time: 2.125
-apim-request-id: c8bf4351-c6f5-4bfe-9a79-ef3720eca8af
-x-ms-region: Sweden Central
-Date: Thu, 17 Oct 2024 01:45:45 GMT
-
-{
-  "cancelled_at": null,
-  "cancelling_at": null,
-  "completed_at": null,
-  "completion_window": "24h",
-  "created_at": 1729129545,
-  "error_file_id": null,
-  "expired_at": null,
-  "expires_at": 1729215945,
-  "failed_at": null,
-  "finalizing_at": null,
-  "id": "batch_c8dd49a7-c808-4575-9957-b188cd0dd642",
-  "in_progress_at": null,
-  "input_file_id": "file-f89384af0082485da43cb26b49dc25ce",
-  "errors": null,
-  "metadata": null,
-  "object": "batch",
-  "output_file_id": null,
-  "request_counts": {
-    "total": 0,
-    "completed": 0,
-    "failed": 0
-  },
-  "status": "validating",
-  "endpoint": "/chat/completions"
-}
-```
-
 ### What happens if the API doesn't complete my request within the 24 hour time frame?
 
 We aim to process these requests within 24 hours; we don't expire the jobs that take longer. You can cancel the job anytime. When you cancel the job, any remaining work is cancelled and any already completed work is returned. You'll be charged for any completed work.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ操作に関する更新"
}
```

### Explanation
この変更は、Azure OpenAIバッチ操作に関するドキュメントのアップデートです。主な修正点は、日付の更新とサポートされる機能に関する情報の追加です。具体的には、旧バージョンのAPIがサポートしていなかった構造化出力が、APIバージョン`2024-08-01-preview`以降でサポートされるようになったことが強調されています。

さらに、ドキュメントの中で、バッチリクエストのトークンに関する詳細な説明が削除され、新たに必要な情報のみが残されて、シンプルで読みやすい形式に整えられています。全体として、変更は75行に及び、3行が追加され、72行が削除されました。これにより、ユーザーがバッチ処理を行う際の理解が容易になることを目的としています。

## articles/ai-services/openai/how-to/code-interpreter.md{#item-95efbd}

<details>
<summary>Diff</summary>
````diff
@@ -6,16 +6,16 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 05/20/2024
-author: mrbullwinkle
-ms.author: mbullwin
+ms.date: 10/15/2024
+author: aahill
+ms.author: aahi
 recommendations: false
 
 ---
 
 # Azure OpenAI Assistants Code Interpreter (Preview)
 
-Code Interpreter allows the Assistants API to write and run Python code in a sandboxed execution environment.  With Code Interpreter enabled, your Assistant can run code iteratively to solve more challenging code, math, and data analysis problems. When your Assistant writes code that fails to run, it can iterate on this code by modifying and running different code until the code execution succeeds.
+Code Interpreter allows the Assistants API to write and run Python code in a sandboxed execution environment. With Code Interpreter enabled, your Assistant can run code iteratively to solve more challenging code, math, and data analysis problems. When your Assistant writes code that fails to run, it can iterate on this code by modifying and running different code until the code execution succeeds.
 
 > [!IMPORTANT]
 > Code Interpreter has [additional charges](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) beyond the token based fees for Azure OpenAI usage. If your Assistant calls Code Interpreter simultaneously in two different threads, two code interpreter sessions are created. Each session is active by default for one hour.
@@ -28,7 +28,7 @@ Code Interpreter allows the Assistants API to write and run Python code in a san
 
 The [models page](../concepts/models.md#assistants-preview) contains the most up-to-date information on regions/models where Assistants and code interpreter are supported.
 
-We recommend using assistants with the latest models to take advantage of the new features, as well as the larger context windows, and more up-to-date training data.
+We recommend using assistants with the latest models to take advantage of the new features, larger context windows, and more up-to-date training data.
 
 ### API Versions
 
@@ -69,7 +69,7 @@ We recommend using assistants with the latest models to take advantage of the ne
 
 ### File upload API reference
 
-Assistants use the [same API for file upload as fine-tuning](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-02-15-preview&tabs=HTTP&preserve-view=true). When uploading a file you have to specify an appropriate value for the [purpose parameter](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-02-15-preview&tabs=HTTP&preserve-view=true#purpose).
+Assistants use the [same API for file upload as fine-tuning](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-02-15-preview&tabs=HTTP&preserve-view=true). When uploading a file, you have to specify an appropriate value for the [purpose parameter](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-02-15-preview&tabs=HTTP&preserve-view=true#purpose).
 
 ## Enable Code Interpreter
 
@@ -136,7 +136,7 @@ assistant = client.beta.assistants.create(
   instructions="You are an AI assistant that can write code to help answer math questions.",
   model="gpt-4-1106-preview",
   tools=[{"type": "code_interpreter"}],
-  file_ids=[file.id]
+  tool_resources={"code interpreter":{"file_ids":[file.id]}}
 )
 ```
 
@@ -145,14 +145,14 @@ assistant = client.beta.assistants.create(
 ```console
 # Upload a file with an "assistants" purpose
 
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files?api-version=2024-05-01-preview \
+curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files?api-version=2024-08-01-preview \
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -F purpose="assistants" \
   -F file="@c:\\path_to_file\\file.csv"
 
 # Create an assistant using the file ID
 
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/assistants?api-version=2024-05-01-preview \
+curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/assistants?api-version=2024-08-01-preview \
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -H 'Content-Type: application/json' \
   -d '{
@@ -161,7 +161,11 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/assistants?api-version=2
       { "type": "code_interpreter" }
     ],
     "model": "gpt-4-1106-preview",
-    "file_ids": ["assistant-123abc456"]
+    "tool_resources"{
+      "code interpreter": {
+          "file_ids": ["assistant-1234"]
+      }
+    }
   }'
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コードインタプリタに関する更新"
}
```

### Explanation
この変更は、Azure OpenAIのコードインタプリタに関するドキュメントを更新したものです。主に日付、著者情報、及び特定の記述が変更されました。具体的には、最終更新日が2024年5月20日から2024年10月15日に更新され、著者が「mrbullwinkle」から「aahill」に変更されています。

また、コードインタプリタがどのように機能するかに関する説明が少し整理されて明確になり、使用するモデルの推奨がより簡潔に表現されています。APIバージョンの情報も最新のバージョンに更新され、コードの例が新しい形式に修正されています。全体的に、変更は24行にわたり、14行が追加され、10行が削除されています。この更新により、ユーザーはコードインタプリタの最新情報をより理解しやすくなっています。

## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Azure OpenAI Service Provisioned Throughput Units (PTU) onboarding
 description: Learn about provisioned throughput units onboarding and Azure OpenAI. 
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 09/12/2024
+ms.date: 10/18/2024
 manager: nitinme
 author: mrbullwinkle 
 ms.author: mbullwin 
@@ -33,7 +33,7 @@ Determining the right amount of provisioned throughput, or PTUs, you require for
 
 ### Estimate provisioned throughput and cost
 
-To get a quick estimate for your workload, open the capacity planner in the [Azure OpenAI Studio](https://oai.azure.com). The capacity planner is under **Management** > **Quotas** > **Provisioned**.
+To get a quick estimate for your workload, open the capacity planner in the [Azure OpenAI Studio](https://oai.azure.com). The capacity planner is under **Shared resources** > **Quota** > **Azure OpenAI Provisioned**.
 
 The **Provisioned** option and the capacity planner are only available in certain regions within the Quota pane, if you don't see this option setting the quota region to *Sweden Central* will make this option available. Enter the following parameters based on your workload.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョンドスループットオンボーディングに関する更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスのプロビジョンドスループットユニット（PTU）に関するオンボーディングドキュメントの更新です。主な変更点は、ドキュメントの日付が2024年9月12日から2024年10月18日に変更されたことと、使用方法のセクションでの表現の見直しです。

具体的には、Azure OpenAI Studio内のキャパシティプランナーのナビゲーションが変更され、以前は「管理」>「クォータ」>「プロビジョン」とされていた部分が、「共有リソース」>「クォータ」>「Azure OpenAIプロビジョンド」に更新されました。この変更により、ユーザーはより正確なナビゲーションによって作業がしやすくなります。

変更は合計で4行に及び、2行が追加され、2行が削除されました。この更新は、ユーザーが必要な情報を迅速に探し出せるようにし、より良い体験を提供することを目指しています。

## articles/ai-services/openai/how-to/structured-outputs.md{#item-cc2557}

<details>
<summary>Diff</summary>
````diff
@@ -18,8 +18,8 @@ Structured outputs make a model follow a [JSON Schema](https://json-schema.org/o
 
 > [!NOTE]
 > * Currently structured outputs is not supported on [bring your own data](../concepts/use-your-data.md) scenario.
->
-> * There is a known issue blocking structured outputs support for [global batch](batch.md).
+
+
 
 ## Supported models
 
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
この変更は、構造化出力に関するAzure OpenAIのドキュメントを更新したものです。主な更新点は、注意書き部分の情報を整理したことです。具体的には、構造化出力が「自分のデータを持ち込む」シナリオではサポートされていないことを示す注記の下に、既知の問題に関する情報が追加されました。

元々、構造化出力サポートに関する「グローバルバッチ」での既知の問題に関する記述がありましたが、以前のテキストではこの情報が少し曖昧でした。更新後、これらの情報がより明確に示され、ユーザーが構造化出力を使用する際の制限を理解しやすくなっています。

この変更は合計で4行にわたっており、2行が追加され、2行が削除されています。全体的に、この更新はユーザーにより良い情報を提供し、誤解を避けるためのサポートを強化しています。

## articles/ai-services/openai/includes/batch/batch-python.md{#item-3121c2}

<details>
<summary>Diff</summary>
````diff
@@ -55,6 +55,12 @@ Like [fine-tuning](../../how-to/fine-tuning.md), global batch uses files in JSON
 {"custom_id": "request-1", "method": "POST", "url": "/chat/completions", "body": {"model": "REPLACE-WITH-MODEL-DEPLOYMENT-NAME", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": [{"type": "text", "text": "What’s in this image?"},{"type": "image_url","image_url": {"url": "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/ai-services/openai/media/how-to/generated-seattle.png"}}]}],"max_tokens": 1000}}
 ```
 
+# [Structured outputs](#tab/structured-outputs)
+
+```json
+{"custom_id": "task-0", "method": "POST", "url": "/chat/completions", "body": {"model": "REPLACE-WITH-MODEL-DEPLOYMENT-NAME", "messages": [{"role": "system", "content": "Extract the event information."}, {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."}], "response_format": {"type": "json_schema", "json_schema": {"name": "CalendarEventResponse", "strict": true, "schema": {"type": "object", "properties": {"name": {"type": "string"}, "date": {"type": "string"}, "participants": {"type": "array", "items": {"type": "string"}}}, "required": ["name", "date", "participants"], "additionalProperties": false}}}}}
+```
+
 ---
 
 The `custom_id` is required to allow you to identify which individual batch request corresponds to a given response. Responses won't be returned in identical order to the order defined in the `.jsonl` batch file.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理における構造化出力のサポートを追加"
}
```

### Explanation
この変更は、Azure OpenAIのバッチ処理に関連するPythonでの実装において、構造化出力をサポートするためのコード例を追加するものです。具体的には、バッチリクエストのフォーマットを示すJSONコードブロックが3つ追加されました。

変更点は、構造化出力に関するセクションの下に新しいコードスニペットが挿入され、ユーザーが構造化出力を使用する際の具体的な例を提供しています。新しいスニペットでは、カスタムIDの使い方や、バッチリクエストの内容について詳しく説明されています。特に、イベント情報を抽出するモデルリクエストの例が示されており、どのように構造化出力を取り扱うかが明確になっています。

このドキュメントには合計6行が追加されており、削除はありません。これにより、ユーザーはバッチ処理における構造化出力の利用方法をより具体的に理解できるようになります。全体として、更新はユーザーの利便性を向上させることを目的としたものです。

## articles/ai-services/openai/includes/batch/batch-rest.md{#item-bcccd9}

<details>
<summary>Diff</summary>
````diff
@@ -44,6 +44,12 @@ Like [fine-tuning](../../how-to/fine-tuning.md), global batch uses files in JSON
 {"custom_id": "request-1", "method": "POST", "url": "/chat/completions", "body": {"model": "REPLACE-WITH-MODEL-DEPLOYMENT-NAME", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": [{"type": "text", "text": "What’s in this image?"},{"type": "image_url","image_url": {"url": "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/ai-services/openai/media/how-to/generated-seattle.png"}}]}],"max_tokens": 1000}}
 ```
 
+# [Structured outputs](#tab/structured-outputs)
+
+```json
+{"custom_id": "task-0", "method": "POST", "url": "/chat/completions", "body": {"model": "REPLACE-WITH-MODEL-DEPLOYMENT-NAME", "messages": [{"role": "system", "content": "Extract the event information."}, {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."}], "response_format": {"type": "json_schema", "json_schema": {"name": "CalendarEventResponse", "strict": true, "schema": {"type": "object", "properties": {"name": {"type": "string"}, "date": {"type": "string"}, "participants": {"type": "array", "items": {"type": "string"}}}, "required": ["name", "date", "participants"], "additionalProperties": false}}}}}
+```
+
 ---
 
 The `custom_id` is required to allow you to identify which individual batch request corresponds to a given response. Responses won't be returned in identical order to the order defined in the `.jsonl` batch file.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理における構造化出力のサポートを追加"
}
```

### Explanation
この変更は、Azure OpenAIのバッチ処理に関連するREST APIドキュメントに構造化出力のサポートを追加したものです。具体的には、バッチリクエストの構造化出力を示すための新しいJSONコード例が6行追加されました。

新しく追加されたコードスニペットでは、ユーザーが構造化出力を利用してイベント情報を抽出する方法が具体的に示されています。特に、カスタムIDの usage や、バッチリクエストの内容に関する詳細な説明が含まれており、ユーザーが応答を追跡しやすくなっています。これにより、構造化出力を使用した際のリクエストフォーマットや期待される応答の形式が明確に理解できるようになります。

全体として、この更新はバッチ処理の利用において構造化データの取り扱いがより容易になることを目的としており、ユーザーの利便性を向上させる内容となっています。今回の修正は6行の追加のみで、削除された行はありません。

## articles/ai-services/openai/includes/batch/batch-studio.md{#item-d4822e}

<details>
<summary>Diff</summary>
````diff
@@ -44,6 +44,13 @@ Like [fine-tuning](../../how-to/fine-tuning.md), global batch uses files in JSON
 {"custom_id": "request-1", "method": "POST", "url": "/chat/completions", "body": {"model": "REPLACE-WITH-MODEL-DEPLOYMENT-NAME", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": [{"type": "text", "text": "What’s in this image?"},{"type": "image_url","image_url": {"url": "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/ai-services/openai/media/how-to/generated-seattle.png"}}]}],"max_tokens": 1000}}
 ```
 
+# [Structured outputs](#tab/structured-outputs)
+
+```json
+{"custom_id": "task-0", "method": "POST", "url": "/chat/completions", "body": {"model": "REPLACE-WITH-MODEL-DEPLOYMENT-NAME", "messages": [{"role": "system", "content": "Extract the event information."}, {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."}], "response_format": {"type": "json_schema", "json_schema": {"name": "CalendarEventResponse", "strict": true, "schema": {"type": "object", "properties": {"name": {"type": "string"}, "date": {"type": "string"}, "participants": {"type": "array", "items": {"type": "string"}}}, "required": ["name", "date", "participants"], "additionalProperties": false}}}}}
+```
+
+
 ---
 
 The `custom_id` is required to allow you to identify which individual batch request corresponds to a given response. Responses won't be returned in identical order to the order defined in the `.jsonl` batch file.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチスタジオに構造化出力のサポートを追加"
}
```

### Explanation
この変更は、Azure OpenAIのバッチスタジオに関連するドキュメントに構造化出力のサポートを追加したものです。具体的には、バッチリクエストの構造化出力を示す新しいJSONコードの例が7行追加されました。

追加されたコードは、ユーザーがイベント情報を抽出するためのリクエストの具体的な例を提供しています。この例には、カスタムIDを使用してリクエストと応答を関連付ける方法や、構造化出力のフォーマットが含まれています。特に、正確な情報を取得するためのJSONスキーマが定義されている点が重要です。

この更新により、バッチスタジオを使用するユーザーは、構造化出力の機能を理解し、効果的に利用できるようになります。変更内容は全体で7行の追加のみで、削除はありません。これにより、ドキュメントの有用性が向上し、バッチ処理の導入がよりスムーズになることが期待されます。


