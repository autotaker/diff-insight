---
date: '2024-10-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:00d70d8...MicrosoftDocs:6e9a4a2
summary: |-
  この更新では、Azure OpenAIサービスに関するスループットの詳細が追加され、バッチ処理のAPIサポート情報やPythonコードが改善されました。これにより、ユーザーは機能をより効率的に利用できるようになります。また、概要ドキュメントのリンクも改善され、情報へのアクセスが向上しました。

  特に、各モデルのスループット情報が追加されたことで、ユーザーは特定モデルのトークン処理数を把握しやすくなりました。REST APIのレスポンスに新たにヘッダが追加され、バッチ処理でのトークン数の情報が得やすくなっています。破壊的な変更はありませんが、コードの最適化により、導入や使用に若干の調整が必要かもしれません。

  この更新は、Azure OpenAIサービスの使いやすさと効率性を向上させ、ユーザーがデータに基づいたモデル選択を行えるようにすることを目的としています。バッチ処理APIの拡張により、リアルタイムでの性能モニタリングが可能になり、問題追跡や改善のための情報が得やすくなりました。全体的な改善により、開発者にとっても取り組みやすい環境が整えられ、継続的なユーザーエクスペリエンスの向上が期待されます。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:00d70d8...MicrosoftDocs:6e9a4a2){target="_blank"}

# ハイライト

現在の更新では、Azure OpenAIサービスのスループットに関する詳細が追加され、バッチ処理のAPIサポート情報やPythonコードが修正されました。これにより、ユーザーはより効果的にこれらの機能を活用できるようになります。また、概要ドキュメントにはリンクの改善が行われました。

## 新しい機能

- 各モデルのスループット情報の追加により、特定モデルのトークン処理数をユーザーが把握しやすくなりました。
- REST APIのレスポンスに関する新しいヘッダが追加され、バッチ処理におけるトークン数の情報が得やすくなりました。

## 破壊的変更

- 特に破壊的な変更はないが、コードの最適化や説明の簡略化により、現場での導入および使用方法に若干の調整が必要かもしれません。

## 他の更新

- PythonコードとREST APIドキュメントの改善により、バッチ処理がより明確に理解できるようになりました。
- サポートドキュメント内のリンクとメタデータの修正で、情報へアクセスする利便性が向上しました。

# 洞察

この更新は、Azure OpenAIサービスの使いやすさと効率性を向上させるための一連の改善点が含まれています。主に、スループットの情報を提供することで、ユーザーはモデル選択をデータ駆動の方法で行えるようになりました。このような情報は、特定の処理ニーズに応じてリソースを最適化するのに役立ちます。

また、バッチ処理に関連するAPIの拡張により、開発者はシステムの性能をリアルタイムでモニターでき、効率的なタスク管理を実現できます。特に、APIレスポンスの詳細が増えることで、問題追跡や改善の根拠を得ることが容易になります。このアップデートによって、ユーザーはより効果的にAzure OpenAIサービスの潜在力を引き出せるようになり、これにより新たなビジネス価値を生み出すことが期待されます。

さらに、コードの整備により、開発者はコードの可読性が向上し、理解が容易になりました。この改善は、新しい開発者や他の技術者が迅速にプロジェクトに参加し、貢献できる環境を整える一助となります。最終的に、この全体的な改善は、継続的なユーザーエクスペリエンスの向上につながります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [provisioned-throughput.md](#item-022e0c) | minor update | パフォーマンス向上とスループットに関する情報の追加 | modified | 31 | 16 | 47 | 
| [batch.md](#item-a131d5) | minor update | バッチ処理に関するAPIサポート情報の追加 | modified | 57 | 3 | 60 | 
| [batch-python.md](#item-3121c2) | minor update | バッチ処理に関するPythonコードの修正 | modified | 6 | 8 | 14 | 
| [batch-rest.md](#item-bcccd9) | minor update | バッチ処理のファイルアップロードに関する説明の修正 | modified | 1 | 1 | 2 | 
| [create-azure-openai-resource-portal.png](#item-8b9bf8) | minor update | 画像ファイルのメタデータの修正 | modified | 0 | 0 | 0 | 
| [overview.md](#item-97d507) | minor update | Azure OpenAIサービスの概要のリンク修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -36,12 +36,20 @@ An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model.
 | Utilization | Provisioned-managed Utilization V2 measure provided in Azure Monitor. |
 | Estimating size | Provided calculator in the studio & benchmarking script. |
 
-## What models and regions are available for provisioned throughput?
 
-[!INCLUDE [Provisioned](../includes/model-matrix/provisioned-models.md)]
+## How much thoughput per PTU you get for each model
+The amount of throughput (tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in the minute. Generating output tokens requires more processing than input tokens and so the more output tokens generated the lower your overall TPM. The service dynamically balances the input & output costs, so users do not have to set specific input and output limits. This approach means your deployment is resilient to fluctuations in the workload shape. 
+
+To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the `gpt-4o` and `gpt-4o-mini` models
+
+|     | **gpt-4o**, **2024-05-13**   & **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | 
+| --- | --- | --- |
+| Deployable Increments | 50 | 25|
+| Input TPM per PTU | 2,500 | 37,000  |
+| Output TPM per PTU | 833  | 12,333 |
+
+\** For a full list see the [AOAI Studio calcualator](https://oai.azure.com/portal/calculator)
 
-> [!NOTE]
-> The provisioned version of `gpt-4` **Version:** `turbo-2024-04-09` is currently limited to text only.
 
 ## Key concepts
 
@@ -67,7 +75,7 @@ az cognitiveservices account deployment create \
 
 #### Provisioned throughput units 
 
-Provisioned throughput units (PTU) are generic units of model processing capacity that you can use to size provisioned deployments to achieve the required throughput for processing prompts and generating completions.   Provisioned throughput units are granted to a subscription as quota on a regional basis, which defines the maximum number of PTUs that can be assigned to deployments in that subscription and region.
+Provisioned throughput units (PTU) are generic units of model processing capacity that you can use to size provisioned deployments to achieve the required throughput for processing prompts and generating completions.   Provisioned throughput units are granted to a subscription as quota. Each quota is specific to a region and defines  the maximum number of PTUs that can be assigned to deployments in that subscription and region.
 
 
 #### Model independent quota
@@ -76,36 +84,36 @@ Unlike the Tokens Per Minute (TPM) quota used by other Azure OpenAI offerings, P
 
 :::image type="content" source="../media/provisioned/model-independent-quota.png" alt-text="Diagram of model independent quota with one pool of PTUs available to multiple Azure OpenAI models." lightbox="../media/provisioned/model-independent-quota.png":::
 
-For provisioned deployments, the new quota shows up in Azure OpenAI Studio as a quota item named **Provisioned Managed Throughput Unit**. For global provisioned managed deployments, the new quota shows up in the Azure OpenAI Studio as a quota item named **Global Provisioned Managed Throughput Unit**.  In the Studio Quota pane, expanding the quota item will show the deployments contributing to usage of each quota.
+For provisioned deployments, the new quota shows up in Azure OpenAI Studio as a quota item named **Provisioned Managed Throughput Unit**. For global provisioned managed deployments, the new quota shows up in the Azure OpenAI Studio as a quota item named **Global Provisioned Managed Throughput Unit**.  In the Studio Quota pane, expanding the quota item shows the deployments contributing to usage of each quota.
 
 :::image type="content" source="../media/provisioned/ptu-quota-page.png" alt-text="Screenshot of quota UI for Azure OpenAI provisioned." lightbox="../media/provisioned/ptu-quota-page.png":::
 
 #### Obtaining PTU Quota 
 
-PTU quota is available by default in many regions. If additional quota is required, customers can request additional quota via the Request Quota link to the right of the Provisioned Managed Throughput Unit or Global Provisioned Managed Throughput Unit quota items in Azure OpenAI Studio. The form allows the customer to request an increase in the specified PTU quota for a given region. The customer will receive an email at the included address once the request is approved, typically within two business days. 
+PTU quota is available by default in many regions. If more quota is required, customers can request quota via the Request Quota link. This link can be found to the right of the Provisioned Managed Throughput Unit or Global Provisioned Managed Throughput Unit quota tabs in the Azure OpenAI Studio. The form allows the customer to request an increase in the specified PTU quota for a given region. The customer receives an email at the included address once the request is approved, typically within two business days. 
 
 #### Per-Model PTU Minimums 
 
 The minimum PTU deployment, increments, and processing capacity associated with each unit varies by model type & version. 
 
 ## Capacity transparency
 
-Azure OpenAI is a highly sought-after service where customer demand might exceed service GPU capacity. Microsoft strives to provide capacity for all in-demand regions and models, but selling out a region is always a possibility. This can limit some customers’ ability to create a deployment of their desired model, version, or number of PTUs in a desired region - even if they have quota available in that region. Generally speaking:
+Azure OpenAI is a highly sought-after service where customer demand might exceed service GPU capacity. Microsoft strives to provide capacity for all in-demand regions and models, but selling out a region is always a possibility. This constraint can limit some customers’ ability to create a deployment of their desired model, version, or number of PTUs in a desired region - even if they have quota available in that region. Generally speaking:
 
-- Quota places a limit on the maximum number of PTUs that can be deployed in a subscription and region, and is not a guarantee of capacity availability. 
+- Quota places a limit on the maximum number of PTUs that can be deployed in a subscription and region, and does not guarantee of capacity availability. 
 - Capacity is allocated at deployment time and is held for as long as the deployment exists.  If service capacity is not available, the deployment will fail
 - Customers use real-time information on quota/capacity availability to choose an appropriate region for their scenario with the necessary model capacity
 - Scaling down or deleting a deployment releases capacity back to the region.  There is no guarantee that the capacity will be available should the deployment be scaled up or re-created later.
 
 #### Regional capacity guidance
 
-To help users find the capacity needed for their deployments, customers will use a new API and Studio experience to provide real-time information on.
+To find the capacity needed for their deployments, use the capacity  API or the Studio deployment experience to provide real-time information on capacity availability.
 
-In Azure OpenAI Studio, the deployment experience will identify when a region lacks the capacity to support the desired model, version and number of PTUs, and will direct the user to a select an alternative region when needed.
+In Azure OpenAI Studio, the deployment experience identifies when a region lacks the capacity needed to deploy the model. This looks at the desired model, version and number of PTUs. If cpacity is unavailable, the experience direct  users to a select an alternative region.
 
 Details on the new deployment experience can be found in the Azure OpenAI [Provisioned get started guide](../how-to/provisioned-get-started.md).
 
-The new [model capacities API](/rest/api/aiservices/accountmanagement/model-capacities/list?view=rest-aiservices-accountmanagement-2024-04-01-preview&tabs=HTTP&preserve-view=true) can also be used to programmatically identify the maximum sized deployment of a specified model that can be created in each region based on the availability of both quota in the subscription and service capacity in the region.
+The new [model capacities API](/rest/api/aiservices/accountmanagement/model-capacities/list?view=rest-aiservices-accountmanagement-2024-04-01-preview&tabs=HTTP&preserve-view=true) can  be used to programmatically identify the maximum sized deployment of a specified model.  The API consideres both the your quota and service capacity in the region.
 
 If an acceptable region isn't available to support the desire model, version and/or PTUs, customers can also try the following steps:
 
@@ -119,13 +127,13 @@ PTUs represent an amount of model processing capacity. Similar to your computer
 
 A few high-level considerations:
 - Generations require more capacity than prompts
-- Larger calls are progressively more expensive to compute. For example, 100 calls of with a 1000 token prompt size requires less capacity than one call with 100,000 tokens in the prompt. This also means that the distribution of these call shapes is important in overall throughput. Traffic patterns with a wide distribution that includes some very large calls might experience lower throughput per PTU than a narrower distribution with the same average prompt & completion token sizes.
+- For GPT-4o and later models, the TPM per PTU is set for input and output tokens separately. For older models, larger calls are progressively more expensive to compute. For example, 100 calls of with a 1000 token prompt size requires less capacity than one call with 100,000 tokens in the prompt. This tiering means that the distribution of these call shapes is important in overall throughput. Traffic patterns with a wide distribution that includes some large calls might experience lower throughput per PTU than a narrower distribution with the same average prompt & completion token sizes.
 
 ### How utilization performance works
 
 Provisioned and global provisioned deployments provide you with an allocated amount of model processing capacity to run a given model.
 
-In Provisioned-Managed and Global Provisioned-Managed deployments, when capacity is exceeded, the API will immediately return a 429 HTTP Status Error. This enables the user to make decisions on how to manage their traffic. Users can redirect requests to a separate deployment, to a standard pay-as-you-go instance, or leverage a retry strategy to manage a given request. The service will continue to return the 429 HTTP status code until the utilization drops below 100%.
+In Provisioned-Managed and Global Provisioned-Managed deployments, when capacity is exceeded, the API will return a 429 HTTP Status Error. This fast response enables the user to make decisions on how to manage their traffic. Users can redirect requests to a separate deployment, to a standard pay-as-you-go instance, or use a retry strategy to manage a given request. The service continues to return the 429 HTTP status code until the utilization drops below 100%.
 
 ### How can I monitor capacity?
 
@@ -149,7 +157,7 @@ For Provisioned-Managed and Global Provisioned-Managed, we use a variation of th
 
     a.	When the current utilization is above 100%, the service returns a 429 code with the `retry-after-ms` header set to the time until utilization is below 100%
      
-    b.	Otherwise, the service estimates the incremental change to utilization required to serve the request by combining prompt tokens and the specified `max_tokens` in the call. If the `max_tokens` parameter is not specified, the service will estimate a value. This estimation can lead to lower concurrency than expected when the number of actual generated tokens is small.  For highest concurrency, ensure that the `max_tokens` value is as close as possible to the true generation size. 
+    b.	Otherwise, the service estimates the incremental change to utilization required to serve the request by combining prompt tokens and the specified `max_tokens` in the call. If the `max_tokens` parameter is not specified, the service estimates a value. This estimation can lead to lower concurrency than expected when the number of actual generated tokens is small.  For highest concurrency, ensure that the `max_tokens` value is as close as possible to the true generation size. 
 
 3.	When a request finishes, we now know the actual compute cost for the call. To ensure an accurate accounting, we correct the utilization using the following logic:
 
@@ -166,7 +174,14 @@ For Provisioned-Managed and Global Provisioned-Managed, we use a variation of th
 
 #### How many concurrent calls can I have on my deployment?
 
-The number of concurrent calls you can achieve depends on each call's shape (prompt size, max_token parameter, etc.). The service will continue to accept calls until the utilization reach 100%. To determine the approximate number of concurrent calls you can model out the maximum requests per minute for a particular call shape in the [capacity calculator](https://oai.azure.com/portal/calculator). If the system generates less than the number of samplings tokens like max_token, it will accept more requests.
+The number of concurrent calls you can achieve depends on each call's shape (prompt size, max_token parameter, etc.). The service continues to accept calls until the utilization reach 100%. To determine the approximate number of concurrent calls, you can model out the maximum requests per minute for a particular call shape in the [capacity calculator](https://oai.azure.com/portal/calculator). If the system generates less than the number of samplings tokens like max_token, it will accept more requests.
+
+## What models and regions are available for provisioned throughput?
+
+[!INCLUDE [Provisioned](../includes/model-matrix/provisioned-models.md)]
+
+> [!NOTE]
+> The provisioned version of `gpt-4` **Version:** `turbo-2024-04-09` is currently limited to text only.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "パフォーマンス向上とスループットに関する情報の追加"
}
```

### Explanation
このコードの変更は、「provisioned-throughput.md」ファイルにおいて、Azure OpenAIサービスのスループットやプロビジョニングに関する情報を強化するためのもので、合計47の変更が加えられています。主要な変更には、各モデルごとのスループット（トークン毎分：TPM）の詳細が追加され、利用者が異なるモデルや地域におけるプロビジョニング単位（PTU）に関連する情報をより良く理解できるようになっています。

新しいセクションでは、特に「gpt-4o」および「gpt-4o-mini」モデルに対するTPM値やプロビジョニング単位の詳細が提供されており、ユーザーが自身のニーズに合ったスループットを計算できるようサポートしています。また、プロビジョニング単位の要求方法や、サービスの可用性に関する情報も明確に表現されています。

この更新は、Azure OpenAI Studioにおけるユーザー体験を改善し、スループットの管理やモデルのデプロイにおける選択肢を増やすことを目的としています。全体的に、ユーザーがサービスの能力をより効果的に利用できるようにするための情報が整理されています。

## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -61,8 +61,6 @@ The following models support global batch:
 | `gpt-35-turbo` | 1106 | text |
 | `gpt-35-turbo` | 0613 | text |
 
-
-
 Refer to the [models page](../concepts/models.md) for the most up-to-date information on regions/models where global batch is currently supported.
 
 ### API support
@@ -166,7 +164,63 @@ The `2024-10-01-preview` REST API adds two new response headers:
 * `deployment-enqueued-tokens` - A approximate token count for your jsonl file calculated immediately after the batch request is submitted. This value represents an estimate based on the number of characters and is not the true token count.
 * `deployment-maximum-enqueued-tokens` The total available enqueued tokens available for this global batch model deployment.
 
-These response headers are only available when making a POST request to begin batch processing of a file with the REST API. The language specific client libraries do not currently return these new response headers.
+These response headers are only available when making a POST request to begin batch processing of a file with the REST API. The language specific client libraries do not currently return these new response headers. To return all response headers you can add `-i` to the standard REST request.
+
+```http
+curl -i -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024-10-01-preview \
+  -H "api-key: $AZURE_OPENAI_API_KEY" \
+  -H "Content-Type: application/json" \
+  -d '{
+    "input_file_id": "file-abc123",
+    "endpoint": "/chat/completions",
+    "completion_window": "24h"
+  }'
+```
+
+```output
+HTTP/1.1 200 OK
+Content-Length: 619
+Content-Type: application/json; charset=utf-8
+Vary: Accept-Encoding
+Request-Context: appId=
+x-ms-response-type: standard
+deployment-enqueued-tokens: 139
+deployment-maximum-enqueued-tokens: 740000
+Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
+X-Content-Type-Options: nosniff
+x-aml-cluster: vienna-swedencentral-01
+x-request-time: 2.125
+apim-request-id: c8bf4351-c6f5-4bfe-9a79-ef3720eca8af
+x-ms-region: Sweden Central
+Date: Thu, 17 Oct 2024 01:45:45 GMT
+
+{
+  "cancelled_at": null,
+  "cancelling_at": null,
+  "completed_at": null,
+  "completion_window": "24h",
+  "created_at": 1729129545,
+  "error_file_id": null,
+  "expired_at": null,
+  "expires_at": 1729215945,
+  "failed_at": null,
+  "finalizing_at": null,
+  "id": "batch_c8dd49a7-c808-4575-9957-b188cd0dd642",
+  "in_progress_at": null,
+  "input_file_id": "file-f89384af0082485da43cb26b49dc25ce",
+  "errors": null,
+  "metadata": null,
+  "object": "batch",
+  "output_file_id": null,
+  "request_counts": {
+    "total": 0,
+    "completed": 0,
+    "failed": 0
+  },
+  "status": "validating",
+  "endpoint": "/chat/completions"
+}
+```
 
 ### What happens if the API doesn't complete my request within the 24 hour time frame?
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理に関するAPIサポート情報の追加"
}
```

### Explanation
このコードの変更は、「batch.md」ファイルにおいて、グローバルバッチ処理に関するAPIのサポート情報を強化するためのもので、主に新しいレスポンスヘッダに関する説明が追加されています。変更には57の行が追加され、主にAPIレスポンスに関する詳細情報が含まれています。

具体的には、2024年10月1日プレビュー版のREST APIにおける新しいレスポンスヘッダ「deployment-enqueued-tokens」と「deployment-maximum-enqueued-tokens」が紹介されており、バッチ処理のファイルが提出された後のトークン数の近似値や、利用可能な最大トークン数について説明しています。また、これらのレスポンスヘッダを含むリクエストの例がcurlコマンドを使って示されており、ユーザーがどのようにAPIを介して情報を取得できるかが具体的に示されています。

さらに、レスポンスヘッダを取得する方法や、リクエストが24時間以内に完了しない場合の処理についても簡潔に説明されています。これにより、ユーザーはAPIを通じてバッチ処理のステータスや結果をより明確に把握できるようになります。全体として、この更新はAPIの使い方とその応答に関する理解を深める助けとなっています。

## articles/ai-services/openai/includes/batch/batch-python.md{#item-3121c2}

<details>
<summary>Diff</summary>
````diff
@@ -74,8 +74,6 @@ For this article we'll create a file named `test.jsonl` and will copy the conten
 
 Once your input file is prepared, you first need to upload the file to then be able to kick off a batch job. File upload can be done both programmatically or via the Studio. This example uses environment variables in place of the key and endpoint values. If you're unfamiliar with using environment variables with Python refer to one of our [quickstarts](../../chatgpt-quickstart.md) where the process of setting up the environment variables in explained step-by-step.
 
-[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
-
 # [Python (Microsoft Entra ID)](#tab/python-secure)
 
 ```python
@@ -105,6 +103,8 @@ file_id = file.id
 
 # [Python (API Key)](#tab/python-key)
 
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+
 ```python
 import os
 from openai import AzureOpenAI
@@ -144,7 +144,7 @@ file_id = file.id
 
 ## Create batch job
 
-Once your file has uploaded successfully by reaching a status of `processed` you can submit the file for batch processing.
+Once your file has uploaded successfully you can submit the file for batch processing.
 
 ```python
 # Submit a batch job with the file
@@ -405,7 +405,7 @@ client.batches.list()
 
 Use the REST API to list all batch jobs with additional sorting/filtering options.
 
-In the examples below we are providing the `generate_time_filter` function to make constructing the filter easier. If you don't wish to use this function the format of the filter string would look like `created_at gt 1728773533 and created_at lt 1729032733 and status eq 'Completed'`.
+In the examples below we are providing the `generate_time_filter` function to make constructing the filter easier. If you don't wish to use this function the format of the filter string would look like `created_at gt 1728860560 and status eq 'Completed'`.
 
 # [Python (Microsoft Entra ID)](#tab/python-secure)
 
@@ -441,9 +441,8 @@ def generate_time_filter(time_range, status=None):
         raise ValueError("Invalid time range format. Use 'past X day(s)' or 'past X hour(s)'")
     
     start_timestamp = int(start_time.timestamp())
-    end_timestamp = int(now.timestamp())
     
-    filter_string = f"created_at gt {start_timestamp} and created_at lt {end_timestamp}"
+    filter_string = f"created_at gt {start_timestamp}"
     
     if status:
         filter_string += f" and status eq '{status}'"
@@ -504,9 +503,8 @@ def generate_time_filter(time_range, status=None):
         raise ValueError("Invalid time range format. Use 'past X day(s)' or 'past X hour(s)'")
     
     start_timestamp = int(start_time.timestamp())
-    end_timestamp = int(now.timestamp())
     
-    filter_string = f"created_at gt {start_timestamp} and created_at lt {end_timestamp}"
+    filter_string = f"created_at gt {start_timestamp}"
     
     if status:
         filter_string += f" and status eq '{status}'"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理に関するPythonコードの修正"
}
```

### Explanation
このコードの変更は、「batch-python.md」ファイルにおいて、バッチ処理に関するPythonコードの一部を修正・最適化するために行われました。変更内容としては、主に6行の追加と8行の削除があり、合計で14行が変更されています。

具体的な修正点は以下の通りです：

1. **Azure Key Vaultに関するインクルードの位置変更**: `Azure key vault` のインクルードが誤っていた位置から正しい位置に移動されています。これにより、コードのセクションの文脈が明確になります。

2. **バッチ処理のファイルアップロードの説明簡略化**: ファイルが正常にアップロードされた後の処理に関する文言が簡略化され、「processed」という状態に達する必要がなくなったことが強調されています。

3. **フィルタリング関数の改善**: `generate_time_filter`関数のフィルタ文字列が改善され、`created_at`の開始タイムスタンプのみに基づくシンプルな構造に変更されています。これにより、ユーザーがフィルタを構成する際にわかりやすくなっています。

これらの変更は、ユーザーがより簡潔かつ効果的にバッチ処理を実施できるようにすることを目的としており、全体的なコードの可読性と効率性を向上させています。

## articles/ai-services/openai/includes/batch/batch-rest.md{#item-bcccd9}

<details>
<summary>Diff</summary>
````diff
@@ -118,7 +118,7 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{file-id}?api-vers
 
 ## Create batch job
 
-Once your file has uploaded successfully by reaching a status of `processed` you can submit the file for batch processing.
+Once your file has uploaded successfully you can submit the file for batch processing.
 
 ```http
 curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024-10-01-preview \
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理のファイルアップロードに関する説明の修正"
}
```

### Explanation
このコードの変更は、「batch-rest.md」ファイルにおいて、バッチ処理に関する説明を簡略化するために行われました。具体的には、1行が追加され、1行が削除されるという小さな変更があり、合計で2行が変更されています。

主な修正点は、ファイルが正常にアップロードされた後の処理に関する説明です。以前は、「processed」という状態に達することが強調されていましたが、今回の変更ではその文言が削除され、ファイルがアップロードされた後に直接バッチ処理を提出できることが示されています。この変更により、ユーザーはファイルのアップロード後に行える処理について、よりシンプルに理解できるようになります。

全体的に、変更は説明を明確にし、ユーザーがバッチ処理を実行する際の手順を簡易化することを目的としています。

## articles/ai-services/openai/media/create-resource/create-azure-openai-resource-portal.png{#item-8b9bf8}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルのメタデータの修正"
}
```

### Explanation
この変更は、「create-azure-openai-resource-portal.png」ファイルに関連しており、実際のファイル内容の変更はありません。ただし、ファイルのメタデータや関連情報に修正が施されている可能性があります。

具体的には、追加や削除された行はなく、ファイルに対する変更内容は0であるため、視覚的なコンテンツ自体には影響が見られません。このような場合、変更はファイルの説明を改善することや、その他の補足情報を整えるためのものであることが考えられます。

全体的に、この更新はファイルの管理や文書の整合性を保つための小さな修正であり、ユーザーにとってより良い体験を提供することを狙っています。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ recommendations: false
 
 # What is Azure OpenAI Service?
 
-Azure OpenAI Service provides REST API access to OpenAI's powerful language models including o1-preview, o1-mini, GPT-4o, GPT-4o mini, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, image understanding, semantic search, and natural language to code translation. Users can access the service through REST APIs, Python SDK, or our web-based interface in the Azure OpenAI Studio.
+Azure OpenAI Service provides REST API access to OpenAI's powerful language models including o1-preview, o1-mini, GPT-4o, GPT-4o mini, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your specific task including but not limited to content generation, summarization, image understanding, semantic search, and natural language to code translation. Users can access the service through REST APIs, Python SDK, or in the [Azure AI Studio](https://ai.azure.com).
 
 ### Features overview
 
@@ -25,7 +25,7 @@ Azure OpenAI Service provides REST API access to OpenAI's powerful language mode
 | Price | [Available here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> For details on GPT-4 Turbo with Vision, see the [special pricing information](../openai/concepts/gpt-with-vision.md#special-pricing-information).|
 | Virtual network support & private link support | Yes, unless using [Azure OpenAI on your data](./concepts/use-your-data.md).  |
 | Managed Identity| Yes, via Microsoft Entra ID | 
-| UI experience | **Azure portal** for account & resource management, <br> **Azure OpenAI Service Studio** for model exploration and fine-tuning |
+| UI experience | [Azure portal](https://portal.azure.com) for account & resource management, <br> [Azure AI Studio](https://ai.azure.com) for model exploration and fine-tuning |
 | Model regional availability | [Model availability](./concepts/models.md) |
 | Content filtering | Prompts and completions are evaluated against our content policy with automated systems. High severity content will be filtered. |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスの概要のリンク修正"
}
```

### Explanation
この変更は、「overview.md」ファイルに伴うもので、Azure OpenAIサービスに関する情報に関して微調整が行われました。具体的には、合計で2行が追加され、2行が削除され、結果として4行の変更がありました。

変更内容の主な部分は、ユーザーがAzure OpenAIサービスにアクセスする方法の部分において、リンクが追加されたことです。具体的には、「Azure OpenAI Studio」へのリンクが明示されるようになり、ユーザーがそのプラットフォームに簡単にアクセスできるようになっています。これにより、関連情報の参照が容易になり、ユーザーは必要なリソースに直接アクセスできるようになります。

さらに、ユーザーインターフェースに関する部分でも、Azure portalとAzure AI Studioへのリンクが追加されており、より明確な情報提供が行われています。

全体的に、この更新はドキュメントの可読性とナビゲーションの向上を図ったものであり、ユーザーにとっての利便性を高めることを目的としています。


