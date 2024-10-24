---
date: '2024-10-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6f58d1b...MicrosoftDocs:f8a58ce
summary: このコードの更新では、Azure OpenAIサービスに対して多くの微細な変更が加えられ、新機能や既存機能の明確化が図られています。主なハイライトとしては、グローバルバッチ機能の一般提供、新APIアクセスの追加、使用量制限の緩和、プロンプトキャッシュ機能の情報追加が挙げられます。これにより、大規模なタスクの効率的な処理が可能となり、ユーザーはコスト管理を容易に行えるようになります。また、APIバージョンの更新により、新しい機能を利用可能にし、特に大量のデータ処理を必要とする現代のニーズに応えています。全体として、これらの変更はAzure
  OpenAIサービスの柔軟性と機能性を向上させることを目指しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6f58d1b...MicrosoftDocs:f8a58ce){target="_blank"}

<format>
# Highlights
このコードの更新では、Azure OpenAIサービスに対する数多くの微細な変更が加えられ、新たな機能や既存機能の明確化が図られています。新たなプロンプトキャッシュ機能の情報追加やAPIバージョンの更新、使用量制限の緩和、そしてグローバルバッチ機能の一般提供開始が主なハイライトです。

## New features
- グローバルバッチ機能が一般提供されることになり、大規模かつ高ボリュームのタスクの効率的な処理が可能となりました。
- `o1-preview`および`o1-mini`モデルへの新たなAPIアクセスおよびデプロイメントが可能になりました。

## Breaking changes
なし

## Other updates
- プロンプトキャッシングとモデルへの割引情報が追加され、`gpt-4o`シリーズが新たにサポートされるようになった。
- APIバージョンが新しくなり、最新の機能を利用できるように調整。
- 使用量制限が緩和され、トークン使用量が従来よりも増量された。

# Insights
今回の変更は、Azure OpenAIサービスをより効率的に活用するための微細な調整と拡張が行われています。プロンプトキャッシングに関する更新では、これまでにないコスト削減の機会を提案しており、新規に`gpt-4o`シリーズのモデルがキャッシングサポートされることで利用範囲が広がります。キャッシュされた入力トークンについての割引情報により、ユーザーはコスト管理がしやすくなったと言えます。

APIバージョンの更新は、新しい機能やパフォーマンスの向上を反映し、最新の技術を取り入れることを可能にします。これにより、開発者はAzure OpenAIサービスの新たな側面を活用できます。

使用量制限の更新では、より広範な利用が可能となり、特に大容量のモデルを活用するユーザーにとって、サービスの利用が容易になります。

そして最も目を引くのは、グローバルバッチの一般提供です。これは、一度に大量のデータ処理を非同期で行い、業務効率化を大幅に推進する基盤を提供します。特にバッチ処理を利用することで、業務コスト削減が期待され、様々なビジネスユースケースでの適用が可能になります。

全体として、この更新はAzure OpenAIサービスに柔軟性と機能性を持たせ、ユーザーにより良いサービス提供を行うためのものであることが明らかです。特に、高度なデータ処理が求められる現代のニーズに適合した内容となっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [provisioned-throughput.md](#item-022e0c) | minor update | プロンプトキャッシュの説明を追加 | modified | 5 | 4 | 9 | 
| [batch.md](#item-a131d5) | minor update | バッチ展開の説明を更新 | modified | 8 | 3 | 11 | 
| [prompt-caching.md](#item-1631df) | minor update | プロンプトキャッシングに関する情報を更新 | modified | 11 | 4 | 15 | 
| [batch-python.md](#item-3121c2) | minor update | APIバージョンを更新 | modified | 2 | 2 | 4 | 
| [batch-rest.md](#item-bcccd9) | minor update | APIバージョンを更新 | modified | 7 | 7 | 14 | 
| [batch-studio.md](#item-d4822e) | minor update | バッチジョブメニューの修正 | modified | 1 | 1 | 2 | 
| [create-batch-job-empty.png](#item-8d7507) | minor update | 画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [create-batch-job.png](#item-fd1371) | minor update | 画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [monitor-openai-reference.md](#item-8d8887) | minor update | 機械学習メトリクスのリスト更新 | modified | 10 | 2 | 12 | 
| [overview.md](#item-97d507) | minor update | 仮想ネットワークサポートの表現修正 | modified | 1 | 1 | 2 | 
| [quotas-limits.md](#item-06c6f9) | minor update | 使用量制限の更新 | modified | 4 | 4 | 8 | 
| [whats-new.md](#item-53303b) | new feature | グローバルバッチの一般提供 | modified | 25 | 1 | 26 | 


# Modified Contents
## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -35,6 +35,7 @@ An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model.
 | Latency | Max latency constrained from the model. Overall latency is a factor of call shape.  |
 | Utilization | Provisioned-managed Utilization V2 measure provided in Azure Monitor. |
 | Estimating size | Provided calculator in the studio & benchmarking script. |
+| Prompt caching | For supported models, we discount up to 100% of cached input tokens. |
 
 
 ## How much throughput per PTU you get for each model
@@ -153,12 +154,12 @@ In the Provisioned-Managed and Global Provisioned-Managed offerings, each reques
 For Provisioned-Managed and Global Provisioned-Managed, we use a variation of the leaky bucket algorithm to maintain utilization below 100% while allowing some burstiness in the traffic. The high-level logic is as follows:
 
 1.	Each customer has a set amount of capacity they can utilize on a deployment
-2.	When a request is made:
+1. When a request is made:
 
-    a.	When the current utilization is above 100%, the service returns a 429 code with the `retry-after-ms` header set to the time until utilization is below 100%
-     
-    b.	Otherwise, the service estimates the incremental change to utilization required to serve the request by combining prompt tokens and the specified `max_tokens` in the call. If the `max_tokens` parameter is not specified, the service estimates a value. This estimation can lead to lower concurrency than expected when the number of actual generated tokens is small.  For highest concurrency, ensure that the `max_tokens` value is as close as possible to the true generation size. 
+   a.	When the current utilization is above 100%, the service returns a 429 code with the `retry-after-ms` header set to the time until utilization is below 100%
 
+   b.	Otherwise, the service estimates the incremental change to utilization required to serve the request by combining prompt tokens and the specified `max_tokens` in the call. For requests that include at least 1024 cached tokens, the cached tokens are subtracted from the prompt token value. A customer can receive up to a 100% discount on their prompt tokens depending on the size of their cached tokens. If the `max_tokens` parameter is not specified, the service estimates a value. This estimation can lead to lower concurrency than expected when the number of actual generated tokens is small.  For highest concurrency, ensure that the `max_tokens` value is as close as possible to the true generation size. 
+   
 3.	When a request finishes, we now know the actual compute cost for the call. To ensure an accurate accounting, we correct the utilization using the following logic:
 
     a.	If the actual > estimated, then the difference is added to the deployment's utilization
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトキャッシュの説明を追加"
}
```

### Explanation
このコードの変更は、`provisioned-throughput.md`ファイルにいくつかの小さな更新を加えました。主な変更点は、プロンプトキャッシングに関する新しい情報の追加です。具体的には、サポートされているモデルに対して、キャッシュされた入力トークンに基づいて最大100%の割引を受けることができるという内容が追加されました。

また、リクエスト処理の流れに関する説明が微修正されており、キャッシュされたトークンの使用が明確にされ、リクエストの実行時にトークンの重み付けがどのように行われるかにも言及されています。これにより、ユーザーはリクエストの結果をより正確に理解し、最適な`max_tokens`の設定を選択できるようになります。この更新は、Azure OpenAIサービスの利用時のパフォーマンスを改善するための重要な情報を提供します。

## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ recommendations: false
 zone_pivot_groups: openai-fine-tuning-batch
 ---
 
-# Getting started with Azure OpenAI global batch deployments (preview)
+# Getting started with Azure OpenAI global batch deployments
 
 The Azure OpenAI Batch API is designed to handle large-scale and high-volume processing tasks efficiently. Process asynchronous groups of requests with separate quota, with 24-hour target turnaround, at [50% less cost than global standard](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). With batch processing, rather than send one request at a time you send a large number of requests in a single file. Global batch requests have a separate enqueued token quota avoiding any disruption of your online workloads.  
 
@@ -65,7 +65,12 @@ Refer to the [models page](../concepts/models.md) for the most up-to-date inform
 
 ### API support
 
-API support was first added with `2024-07-01-preview`. Use `2024-10-01-preview` to take advantage of the latest features.
+|   | API Version   |
+|---|---|
+|**Latest GA API release:**| `2024-10-21`|
+|**Latest Preview API release:**| `2024-10-01-preview`|
+
+Support first added in: `2024-07-01-preview`
 
 ### Feature support
 
@@ -75,7 +80,7 @@ The following aren't currently supported:
 - Integration with Azure OpenAI On Your Data feature.
 
 > [!NOTE]
-> Structured outputs is now supported with Global Batch when used in conjunction with API version `2024-08-01-preview` or later. Use `2024-10-01-preview` for the latest features.
+> Structured outputs is now supported with Global Batch.
 
 ### Global batch deployment
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ展開の説明を更新"
}
```

### Explanation
このコードの変更は、`batch.md`ファイルに対するいくつかの修正を含んでいます。主な更新点は、Azure OpenAIグローバルバッチ展開に関する説明文の改訂です。具体的には、プレビューから正式版へのタイトルの変更と、APIサポートのバージョンに関する情報が明確にされています。

新たに表形式でAPIバージョンの情報が追加され、最新のGA（一般提供）APIリリースやプレビューバージョンについて簡単に参照できるようになりました。また、構造化出力がグローバルバッチでサポートされるようになったことが強調され、関連するAPIのバージョン情報も更新されました。

これらの変更により、読者が最新のAPI機能を利用し、バッチ処理の効果を最大化する方法を容易に理解できるようになっています。バッチ機能の利点や使用方法がわかりやすく整理されており、Azure OpenAIサービスの利用が向上することが期待されます。

## articles/ai-services/openai/how-to/prompt-caching.md{#item-1631df}

<details>
<summary>Diff</summary>
````diff
@@ -14,18 +14,21 @@ recommendations: false
 
 # Prompt caching
 
-Prompt caching allows you to reduce overall request latency and cost for longer prompts that have identical content at the beginning of the prompt. *"Prompt"* in this context is referring to the input you send to the model as part of your chat completions request. Rather than reprocess the same input tokens over and over again, the model is able to retain a temporary cache of processed input data to improve overall performance. Prompt caching has no impact on the output content returned in the model response beyond a reduction in latency and cost.  
+Prompt caching allows you to reduce overall request latency and cost for longer prompts that have identical content at the beginning of the prompt. *"Prompt"* in this context is referring to the input you send to the model as part of your chat completions request. Rather than reprocess the same input tokens over and over again, the model is able to retain a temporary cache of processed input data to improve overall performance. Prompt caching has no impact on the output content returned in the model response beyond a reduction in latency and cost. For supported models, cached tokens are billed at a [50% discount on input token pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/).
 
 ## Supported models
 
 Currently only the following models support prompt caching with Azure OpenAI:
 
 - `o1-preview-2024-09-12`
 - `o1-mini-2024-09-12`
+- `gpt-4o-2024-05-13`
+- `gpt-4o-2024-08-06`
+- `gpt-4o-mini-2024-07-18`
 
 ## API support
 
-Official support for prompt caching was first added in API version `2024-10-01-preview`.
+Official support for prompt caching was first added in API version `2024-10-01-preview`. At this time, only `o1-preview-2024-09-12` and `o1-mini-2024-09-12` models support the `cached_tokens` API response parameter.
 
 ## Getting started
 
@@ -67,7 +70,7 @@ A single character difference in the first 1,024 tokens will result in a cache m
 
 The o1-series models are text only and don't support system messages, images, tool use/function calling, or structured outputs. This limits the efficacy of prompt caching for these models to the user/assistant portions of the messages array which are less likely to have an identical 1024 token prefix.
 
-Once prompt caching is enabled for other supported models prompt caching will expand to support:  
+For `gpt-4o` and `gpt-4o-mini` models, prompt caching is supported for:  
 
 | **Caching Supported** | **Description** |
 |--------|--------|
@@ -80,4 +83,8 @@ To improve the likelihood of cache hits occurring, you should structure your req
 
 ## Can I disable prompt caching?
 
-Prompt caching is enabled by default. There is no opt-out option.
\ No newline at end of file
+Prompt caching is enabled by default. There is no opt-out option.
+
+## How does prompt caching work for Provisioned deployments?
+
+For supported models on provisioned deployments, we discount up to 100% of cached input tokens. For more information, see our [Provisioned Throughput documentation](/azure/ai-services/openai/concepts/provisioned-throughput). 
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトキャッシングに関する情報を更新"
}
```

### Explanation
このコードの変更は、`prompt-caching.md`ファイルに対するいくつかの修正を含んでおり、特にプロンプトキャッシングの機能に関する情報が強化されています。変更点としては、プロンプトキャッシングが同じ内容で始まる長いプロンプトのリクエストレイテンシーとコストを削減する方法についての説明の補足があります。

具体的には、サポートされているモデルに対して、キャッシュされたトークンが入力トークン料金の50%割引で請求されることと、新たにサポートされたモデルのリストに`gpt-4o`シリーズのモデルが追加されました。また、プロビジョンド展開におけるプロンプトキャッシングの実装方法に関する情報も加わり、サポートされているモデルに対してはキャッシュされた入力トークンが最大100%割引されることも記載されています。

これらの修正により、読者はプロンプトキャッシングの利点をより効果的に理解できるようになり、特に新しいモデルやコストに関する情報についての透明性が向上しています。全体的に、プロンプトキャッシング機能の利用に関するガイダンスが明確化され、使用方法がはっきりと説明されています。

## articles/ai-services/openai/includes/batch/batch-python.md{#item-3121c2}

<details>
<summary>Diff</summary>
````diff
@@ -94,7 +94,7 @@ token_provider = get_bearer_token_provider(
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   azure_ad_token_provider=token_provider,
-  api_version="2024-10-01-preview"
+  api_version="2024-10-21"
 )
 
 # Upload a file with a purpose of "batch"
@@ -117,7 +117,7 @@ from openai import AzureOpenAI
     
 client = AzureOpenAI(
     api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-    api_version="2024-10-01-preview",
+    api_version="2024-10-21",
     azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
     )
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンを更新"
}
```

### Explanation
このコードの変更は、`batch-python.md`ファイルにおけるAPIバージョンの更新に関連しています。具体的には、Azure OpenAIクライアントの構築において使用されるAPIバージョンが`2024-10-01-preview`から`2024-10-21`に変更されています。

この変更により、最新のAPI機能や改善点を利用できることが期待されます。APIバージョンの更新は、開発者が新しい機能や修正を活用できるようにするための重要なステップであり、これによりバッチ処理やファイルアップロードを行う際のパフォーマンスや互換性が向上する可能性があります。

全体として、このマイナーな更新は、ドキュメントを最新の状態に保ち、Azure OpenAIサービスの効率的な利用を促進する目的があります。

## articles/ai-services/openai/includes/batch/batch-rest.md{#item-bcccd9}

<details>
<summary>Diff</summary>
````diff
@@ -73,7 +73,7 @@ Once your input file is prepared, you first need to upload the file to then be a
 [!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 ```http
-curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files?api-version=2024-10-01-preview \
+curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files?api-version=2024-10-21 \
   -H "Content-Type: multipart/form-data" \
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -F "purpose=batch" \
@@ -103,7 +103,7 @@ The above code assumes a particular file path for your test.jsonl file. Adjust t
 Depending on the size of your upload file it might take some time before it's fully uploaded and processed. To check on your file upload status run:
 
 ```http
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{file-id}?api-version=2024-10-01-preview \
+curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{file-id}?api-version=2024-10-21 \
   -H "api-key: $AZURE_OPENAI_API_KEY"
 ```
 
@@ -127,7 +127,7 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{file-id}?api-vers
 Once your file has uploaded successfully you can submit the file for batch processing.
 
 ```http
-curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024-10-01-preview \
+curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024-10-21 \
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -H "Content-Type: application/json" \
   -d '{
@@ -176,7 +176,7 @@ curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-vers
 Once you have created batch job successfully you can monitor its progress either in the Studio or programatically. When checking batch job progress we recommend waiting at least 60 seconds in between each status call.
 
 ```http
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches/{batch_id}?api-version=2024-10-01-preview \
+curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches/{batch_id}?api-version=2024-10-21 \
   -H "api-key: $AZURE_OPENAI_API_KEY" 
 ```
 
@@ -228,7 +228,7 @@ The following status values are possible:
 ## Retrieve batch job output file
 
 ```http
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{output_file_id}/content?api-version=2024-10-01-preview \
+curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{output_file_id}/content?api-version=2024-10-21 \
   -H "api-key: $AZURE_OPENAI_API_KEY" > batch_output.jsonl
 ```
 
@@ -239,7 +239,7 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{output_file_id}/c
 Cancels an in-progress batch. The batch will be in status `cancelling` for up to 10 minutes, before changing to `cancelled`, where it will have partial results (if any) available in the output file.
 
 ```http
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches/{batch_id}/cancel?api-version=2024-10-01-preview \
+curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches/{batch_id}/cancel?api-version=2024-10-21 \
   -H "api-key: $AZURE_OPENAI_API_KEY" 
 ```
 
@@ -248,7 +248,7 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches/{batch_id}/cance
 List all existing batch jobs for a given Azure OpenAI resource.
 
 ```http
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024-10-01-preview \
+curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024-10-21 \
   -H "api-key: $AZURE_OPENAI_API_KEY" 
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンを更新"
}
```

### Explanation
このコードの変更は、`batch-rest.md`ファイルにおける一連のAPI呼び出しのAPIバージョンを更新することに関連しています。これにより、REST APIのエンドポイントで使用されるバージョンが`2024-10-01-preview`から`2024-10-21`に変更されています。

具体的には、ファイルのアップロード、ファイルのステータス確認、バッチ処理の開始、バッチジョブの進行状況の確認、出力ファイルの取得、およびバッチのキャンセルに関する各APIリクエストが影響を受けています。新しいバージョンへの更新は、APIの機能やパフォーマンス、セキュリティの向上を反映している可能性が高く、開発者が最新のリソースを利用できるようになります。

この変更により、ユーザーは最新のAPIを使用することで、改善された機能や新機能を体験できることが期待されます。全体として、このマイナーな更新は、ドキュメントを最新のものに維持し、Azure OpenAIサービスの効果的な使い方を促進するための重要なステップです。

## articles/ai-services/openai/includes/batch/batch-studio.md{#item-d4822e}

<details>
<summary>Diff</summary>
````diff
@@ -72,7 +72,7 @@ Once your input file is prepared, you first need to upload the file to then be a
 
 1. Sign in to [AI Studio](https://ai.azure.com).
 2. Select the Azure OpenAI resource where you have a global batch model deployment available.
-3. Select **Batch jobs PREVIEW** > **+Create batch jobs**.
+3. Select **Batch jobs** > **+Create batch jobs**.
 
     :::image type="content" source="../../media/how-to/global-batch/create-batch-job-empty.png" alt-text="Screenshot that shows the batch job creation experience in Azure AI Studio." lightbox="../../media/how-to/global-batch/create-batch-job-empty.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチジョブメニューの修正"
}
```

### Explanation
このコードの変更は、`batch-studio.md`ファイルにおいて、AI Studio内でのバッチジョブの作成手順に関する記述修正を行ったものです。具体的には、バッチジョブを作成するためのメニューの項目名が`Batch jobs PREVIEW`から`Batch jobs`に変更されています。

この修正は、ユーザーが正確な手順に従ってバッチジョブを作成できるようにするためのものです。バッチ処理の設定や管理が容易になるように、インターフェースの変更に伴ってドキュメントも適切に更新されています。

全体的に見て、このマイナーな更新は、ユーザーの体験を向上させ、AI Studioの操作に関する情報の正確性を保つために重要です。

## articles/ai-services/openai/media/how-to/global-batch/create-batch-job-empty.png{#item-8d7507}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの更新"
}
```

### Explanation
このコードの変更は、`create-batch-job-empty.png`という画像ファイルに関するものです。この変更は、ファイル自体の内容には何の追加や削除もなく、単に画像が更新されたことを示しています。具体的にどのような変更が加えられたかは不明ですが、更新された画像の存在は、ドキュメントやユーザーの体験を改善するためのものであると考えられます。

画像は、バッチジョブの作成プロセスにおいて、視覚的な指示や参考情報を提供するために重要です。したがって、これもまたユーザーが操作を理解しやすくするための助けとなる重要な要素です。

## articles/ai-services/openai/media/how-to/global-batch/create-batch-job.png{#item-fd1371}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの更新"
}
```

### Explanation
このコードの変更は、`create-batch-job.png`という画像ファイルに関するもので、ファイル自体の内容に変更はありませんが、更新が行われたことを示しています。具体的な追加や削除は行われておらず、更新された内容についての詳細は不明ですが、これにより画像の品質や視覚的な情報が改善された可能性があります。

画像は、バッチジョブの作成に関するプロセスを示すための重要な要素であり、手順を視覚的に理解するための支援を提供します。この更新は、ユーザーが情報をより効果的に理解できるようにするための取り組みとして位置づけられます。

## articles/ai-services/openai/monitor-openai-reference.md{#item-8d8887}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,7 @@ See [Monitor Azure OpenAI](./how-to/monitor-openai.md) for details on the data y
 
 ### Supported metrics for Microsoft.CognitiveServices/accounts
 
-Here are the most important metrics we think you should monitor for Azure OpenAI. Later in this article is a longer list of all available OpenAI metrics, which contains more details on metrics in this shorter list.
+Here are the most important metrics we think you should monitor for Azure OpenAI. Later in this article is a longer list of all available Azure AI services metrics which contains more details on metrics in this shorter list.
 
 - Azure OpenAI Requests
 - Active Tokens
@@ -30,7 +30,15 @@ Here are the most important metrics we think you should monitor for Azure OpenAI
 - Provisioned-managed Utilization V2
 - Prompt Token Cache Match Rate
 - Time to Response
-- Time Between Tokens 
+- Time Between Tokens
+
+You can also monitor Content Safety metrics that are used by other Azure AI services. 
+- Blocked Volume
+- Harmful Volume Detected
+- Potential Abusive User Count
+- Safety System Event
+- Total Volume Sent for Safety Check 
+
 
 > [!NOTE]
 > The **Provisioned-managed Utilization** metric is now deprecated and is no longer recommended. This metric has been replaced by the **Provisioned-managed Utilization V2** metric.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "機械学習メトリクスのリスト更新"
}
```

### Explanation
このコードの変更は、`monitor-openai-reference.md`というマークダウンファイルに対するもので、主にメトリクスに関する情報を更新しています。具体的には、10行の新しいテキストが追加され、2行が削除され、全体で12行にわたる変更が行われました。

主な変更点は、「Azure OpenAI」のモニタリングに関する重要なメトリクスのリストが明確化され、Azure AIサービスの他のメトリクスにも言及されています。特に、内容として新たに追加されたメトリクスには「コンテンツ安全性」に関連する項目が含まれており、利用者が注意を払うべき指標が強調されています。また、「Provisioned-managed Utilization」メトリクスが廃止され、「Provisioned-managed Utilization V2」メトリクスに置き換えられたことが注記されています。

これらの更新により、ユーザーはAzure OpenAIのパフォーマンスや安全性をより適切に監視できるようになることが期待されます。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -23,7 +23,7 @@ Azure OpenAI Service provides REST API access to OpenAI's powerful language mode
 | Models available | **o1-preview** & **o1-mini** - (Limited Access - [Request Access](https://aka.ms/oai/modelaccess))<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
 | Fine-tuning | `GPT-4o-mini` (preview) <br> `GPT-4` (preview) <br>`GPT-3.5-Turbo` (0613) <br> `babbage-002` <br> `davinci-002`.|
 | Price | [Available here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> For details on GPT-4 Turbo with Vision, see the [special pricing information](../openai/concepts/gpt-with-vision.md#special-pricing-information).|
-| Virtual network support & private link support | Yes, unless using [Azure OpenAI on your data](./concepts/use-your-data.md).  |
+| Virtual network support & private link support | Yes.  |
 | Managed Identity| Yes, via Microsoft Entra ID | 
 | UI experience | [Azure portal](https://portal.azure.com) for account & resource management, <br> [Azure AI Studio](https://ai.azure.com) for model exploration and fine-tuning |
 | Model regional availability | [Model availability](./concepts/models.md) |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "仮想ネットワークサポートの表現修正"
}
```

### Explanation
このコードの変更は、`overview.md`ファイルに対するもので、Azure OpenAIサービスに関する概要を提供しています。具体的には、仮想ネットワークサポートとプライベートリンクサポートについての記述が更新され、1行のテキストが追加され、1行が削除された結果、合計で2行の変更が行われました。

変更内容は、仮想ネットワークサポートとプライベートリンクサポートの部分が修正され、より明確な表現になっています。元の表現では「はい、ただし[Azure OpenAIをあなたのデータで使用する場合](./concepts/use-your-data.md)以外は」と限定的な表現がされていたのが、「はい」と単純化されました。この変更により、ユーザーは仮想ネットワーク機能についての理解がより容易になり、サービスのサポート内容がより一貫した形で提供されることになります。

この微調整は、ユーザーがAzure OpenAIサービスの機能を理解する上での助けとなることを目指しています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 10/11/2024
+ms.date: 10/23/2024
 ms.author: mbullwin
 ---
 
@@ -132,14 +132,14 @@ The Usage Limit determines the level of usage above which customers might see la
 
 |Model| Usage Tiers per month |
 |----|----|
-|`gpt-4o` | 8 Billion tokens |
-|`gpt-4o-mini` | 45 Billion tokens |
+|`gpt-4o` | 12 Billion tokens |
+|`gpt-4o-mini` | 85 Billion tokens |
 
 #### GPT-4 standard
 
 |Model| Usage Tiers per month|
 |---|---|
-| `gpt-4` + `gpt-4-32k`  (all versions) | 4 Billion |
+| `gpt-4` + `gpt-4-32k`  (all versions) | 6 Billion |
 
 
 ## Other offer types
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "使用量制限の更新"
}
```

### Explanation
このコードの変更は、`quotas-limits.md`ファイルに対するもので、Azure OpenAIサービスの使用量に関する制限を更新しています。具体的には、合計で4行の新しいテキストが追加され、4行が削除されることで、全体で8行の変更が行われました。

主な変更点は、いくつかのモデルに対する月間使用量の制限が引き上げられたことです。例えば、`gpt-4o`モデルのトークン使用量が8億から12億に、`gpt-4o-mini`モデルは450億から850億に増加しました。また、`gpt-4`及び`gpt-4-32k`モデルの使用量も、4億から6億に引き上げられています。これらの更新は、ユーザーにより大きな使用量の範囲を提供し、サービスの利用を促進することを目的としています。

さらに、ドキュメントのメタデータの日付も更新されており、これにより最新の情報が反映されていることが示されています。全体として、この変更は、利用者に対してより柔軟な使用量のオプションを提供することに寄与しています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: whats-new
-ms.date: 10/01/2024
+ms.date: 10/22/2024
 recommendations: false
 ---
 
@@ -20,6 +20,30 @@ This article provides a summary of the latest releases and major documentation u
 
 ## October 2024
 
+### Global Batch GA
+
+Azure OpenAI global batch is now generally available.
+
+The Azure OpenAI Batch API is designed to handle large-scale and high-volume processing tasks efficiently. Process asynchronous groups of requests with separate quota, with 24-hour target turnaround, at [50% less cost than global standard](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). With batch processing, rather than send one request at a time you send a large number of requests in a single file. Global batch requests have a separate enqueued token quota avoiding any disruption of your online workloads.  
+
+Key use cases include:
+
+* **Large-Scale Data Processing:** Quickly analyze extensive datasets in parallel.
+
+* **Content Generation:** Create large volumes of text, such as product descriptions or articles.
+
+* **Document Review and Summarization:** Automate the review and summarization of lengthy documents.
+
+* **Customer Support Automation:** Handle numerous queries simultaneously for faster responses.
+
+* **Data Extraction and Analysis:** Extract and analyze information from vast amounts of unstructured data.
+
+* **Natural Language Processing (NLP) Tasks:** Perform tasks like sentiment analysis or translation on large datasets.
+
+* **Marketing and Personalization:** Generate personalized content and recommendations at scale.
+
+For more information on [getting started with global batch deployments](./how-to/batch.md).
+
 ### o1-preview and o1-mini models limited access
 
 The `o1-preview` and `o1-mini` models are now available for API access and model deployment. **Registration is required, and access will be granted based on Microsoft's eligibility criteria**.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "グローバルバッチの一般提供"
}
```

### Explanation
このコードの変更は、`whats-new.md`ファイルに対するもので、Azure OpenAIサービスの最新の機能と更新に関する情報が追加されています。具体的には、25行の新しいテキストが追加され、1行が削除され、合計で26行の変更が行われました。

主な内容は、Azure OpenAIグローバルバッチ機能が一般提供されることに関するもので、これにより、大規模かつ高ボリュームの処理タスクを効率的に処理できるようになります。具体的には、非同期リクエストのグループを処理し、オンラインワークロードの中断を避けるために、別々のクォータを使用することができるようになります。また、バッチ処理を利用することで、一度に大量のリクエストを送信できるようになるため、コストを50％削減することも可能です。

新たに追加された特徴的なユースケースには、データの大規模処理、コンテンツ生成、自動文書レビュー、顧客サポートの自動化、データ抽出と分析、NLPタスク、マーケティングとパーソナリゼーションが含まれます。

さらに、`o1-preview`および`o1-mini`モデルへのAPIアクセスとモデルデプロイメントも可能になったことが伝えられていますが、登録が必要であり、アクセスはMicrosoftの適格基準に基づいて与えられることも明記されています。

この更新は、ユーザーに対して新しい機能と利用方法を提示し、Azure OpenAIサービスの活用の幅を広げることを目的としています。


