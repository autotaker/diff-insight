---
date: '2025-05-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a7ab2bd...MicrosoftDocs:4f76879
summary: Azure OpenAIのAPIドキュメントに大きな変更が行われ、ユーザーが新しいAPI機能や仕様にアクセスしやすくなっています。主な更新として、APIバージョン非推奨文書の削除、新しいバージョンライフサイクル文書の追加、ブラウザ操作の自動化機能の導入（Playwrightの統合）、最新のv1プレビューREST
  APIリファレンス文書の作成があります。また、Responses APIの大幅な改訂が行われ、ユーザーは新たな機能への移行が必要になる可能性があります。全体的に、これらの変更により、ユーザーが技術情報や支援をより容易に得られるような配慮がなされています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a7ab2bd...MicrosoftDocs:4f76879){target="_blank"}

<format>
# Highlights
Azure OpenAIのAPIドキュメントに大きな変更が行われました。いくつかの重要な更新と新しい文書の導入があり、ユーザーが新しいAPI機能や仕様にアクセスしやすくなっています。主な更新はAPIバージョン非推奨文書の削除や新たなバージョンライフサイクル文書の追加、そしてPlaywrightを用いたブラウザ操作の自動化機能などがあります。

## New features
- 新しいAPIバージョンライフサイクル文書の追加。
- ブラウザ操作の自動化機能の導入（Playwrightの統合）。
- 最新プレビューAPIの新規文書追加。
- 最新のv1プレビューREST APIリファレンス文書の作成。

## Breaking changes
- Azure OpenAI APIバージョン非推奨に関する文書の削除。
- Responses APIの大幅な改訂。

## Other updates
- モデル文書やプロビジョニング情報などの軽微な更新（誤字修正や内容の明確化）。
- 各ドキュメントのリンクや情報の整合性を保つための調整。
- 新しいモデルや地域対応情報の追加。
- クォータと制限情報の修正。

# Insights
このコード変更では、Azure OpenAIのAPIに関する一貫した情報提供と最新機能の周知に力が入っています。まず、大きな更新としては、「APIバージョン非推奨」の情報を削除し、新たに「バージョンライフサイクル」文書を追加することで、ユーザーに対するAPI管理の見通しを改善しました。この新しい文書により、ユーザーはAPIの進化やサポートに関する最新情報を求めることができます。

また、ブラウザ操作の自動化はPlaywrightライブラリを通じて実現され、多様な操作をAIに委任できるようになるため、現実的なアプリケーション利用の幅が広がります。これは、特に開発者が自動化や効率化を図りやすくなるための重要なステップです。

一方で、Responses APIに対する大規模な改訂はユーザーにとって新しい機能への移行が必要となる場合があります。また、地域対応や新しいAPIの文書追加など、細かいドラフト調整も行われ、地域やモデル対応の明示化が進められました。

全体を通して、この変更はAzure OpenAIのAPIが進化し続けていることを反映しており、技術者や開発者が常に最新情報に触れ、効率的に開発を続けられるよう配慮されています。新しい機能を導入しつつ、既存情報の透明性を保つための戦略的な文書管理が見受けられます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [api-version-deprecation.md](#item-1cad50) | breaking change | APIバージョン非推奨に関する文書の削除 | removed | 0 | 129 | 129 | 
| [api-version-lifecycle.md](#item-92ab49) | new feature | Azure OpenAI APIのバージョンライフサイクルに関する新しい文書の追加 | added | 352 | 0 | 352 | 
| [models.md](#item-db2c37) | minor update | モデルに関するドキュメントの日付更新と内容変更 | modified | 1 | 3 | 4 | 
| [use-your-data.md](#item-455d6e) | minor update | モデルサポートに関する情報の更新 | modified | 1 | 0 | 1 | 
| [computer-use.md](#item-6fbca8) | new feature | Playwrightとの統合によるブラウザ操作の自動化 | modified | 839 | 7 | 846 | 
| [migration-javascript.md](#item-19dac7) | minor update | APIバージョンに関するドキュメントリンクの更新 | modified | 1 | 1 | 2 | 
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | モデル名の変更とプロビジョニング情報の更新 | modified | 8 | 8 | 16 | 
| [reasoning.md](#item-a54b2f) | minor update | クライアント設定とAPIバージョンの更新 | modified | 4 | 4 | 8 | 
| [responses.md](#item-b9757d) | breaking change | Responses APIの大幅な改訂と新機能の追加 | modified | 593 | 817 | 1410 | 
| [use-web-app.md](#item-802413) | minor update | Webアプリの起動コマンドに関する更新 | modified | 1 | 1 | 2 | 
| [api-surface.md](#item-a25fa2) | minor update | 新しいプレビュー推論APIの追加に関する通知 | modified | 3 | 0 | 3 | 
| [new-inference-preview.md](#item-bd665f) | new feature | 新しい推論プレビューAPIに関する文書の追加 | added | 4740 | 0 | 4740 | 
| [batch-python.md](#item-3121c2) | minor update | 文書内の誤字修正 | modified | 1 | 1 | 2 | 
| [batch-rest.md](#item-bcccd9) | minor update | 文書内の誤字修正 | modified | 1 | 1 | 2 | 
| [provisioned-global.md](#item-340884) | minor update | モデル対応地域の更新 | modified | 5 | 5 | 10 | 
| [provisioned-models.md](#item-8ee639) | minor update | モデルのプロビジョニング情報の修正 | modified | 1 | 1 | 2 | 
| [standard-image-generation.md](#item-dd78ea) | minor update | 標準画像生成モデルの地域対応修正 | modified | 7 | 5 | 12 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータと制限情報の文言修正 | modified | 5 | 5 | 10 | 
| [reference-preview-latest.md](#item-dbae2a) | new feature | Azure OpenAIの最新v1プレビューREST APIリファレンスの追加 | added | 30 | 0 | 30 | 
| [reference-preview.md](#item-e197a2) | minor update | データプレーン推論仕様のプレビューリリース日付の更新 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c945af) | minor update | APIリファレンスとリンクの更新 | modified | 5 | 3 | 8 | 
| [whats-new.md](#item-53303b) | minor update | Whats New文書の更新 | modified | 10 | 10 | 20 | 


# Modified Contents
## articles/ai-services/openai/api-version-deprecation.md{#item-1cad50}

<details>
<summary>Diff</summary>
````diff
@@ -1,129 +0,0 @@
----
-title: Azure OpenAI in Azure AI Foundry Models API version lifecycle
-description: Learn more about API version retirement in Azure OpenAI.
-services: cognitive-services
-manager: nitinme
-ms.service: azure-ai-openai
-ms.topic: conceptual 
-ms.date: 03/25/2025
-author: mrbullwinkle
-ms.author: mbullwin
-recommendations: false
-ms.custom:
----
-
-# Azure OpenAI in Azure AI Foundry Models API preview lifecycle
-
-This article is to help you understand the support lifecycle for the Azure OpenAI API previews. New preview APIs target a monthly release cadence. Whenever possible we recommend using either the latest GA, or preview API releases.
-
-> [!NOTE]
-> New API response objects may be added to the API response without version changes. We recommend you only parse the response objects you require.
->
-> The latest Azure OpenAI spec uses OpenAPI 3.1. It is a known issue that this is currently not fully supported by [Azure API Management](/azure/api-management/api-management-key-concepts)
-
-## Latest preview API releases
-
-Azure OpenAI API latest release:
-
-- Inference: [2025-04-01-preview](reference-preview.md)
-- Authoring: [2025-04-01-preview](authoring-reference-preview.md)
-
-This version contains support for the latest Azure OpenAI features including:
-
-- `GPT-image-1`, the evaluations API, reasoning summary with `o3` and `o4-mini` . [**Added in 2025-04-01-preview**]
-- [Responses API & support for `computer-use-preview` model](./how-to/responses.md) [**Added in 2025-03-01-preview**]
-- [Stored Completions (distillation) API](./how-to/stored-completions.md#stored-completions-api) [**Added in 2025-02-01-preview**]
-- [Predicted Outputs](./how-to/predicted-outputs.md) [**Added in 2025-01-01-preview**]
-- [Reasoning models](./how-to/reasoning.md) [**Added in 2024-12-01-preview**]
-- [Stored completions/distillation](./how-to/stored-completions.md) [**Added in 2024-12-01-preview**]
-- Assistants V2 [**Added in 2024-05-01-preview**]
-- Embeddings `encoding_format` and `dimensions` parameters [**Added in 2024-03-01-preview**]
-- [Assistants API](./assistants-reference.md). [**Added in 2024-02-15-preview**]
-- [Text to speech](./text-to-speech-quickstart.md). [**Added in 2024-02-15-preview**]
-- [DALL-E 3](./dall-e-quickstart.md). [**Added in 2023-12-01-preview**]
-- [Fine-tuning](./how-to/fine-tuning.md). [**Added in 2023-10-01-preview**]
-- [Speech to text](./whisper-quickstart.md). [**Added in 2023-09-01-preview**]
-- [Function calling](./how-to/function-calling.md)  [**Added in 2023-07-01-preview**]
-- [Retrieval augmented generation with your data feature](./use-your-data-quickstart.md).  [**Added in 2023-06-01-preview**]
-
-## Changes between 2025-04-01-preview and 2025-03-01-preview
-
-- [`GPT-image-1` support](/azure/ai-services/openai/how-to/dall-e)
-- [Reasoning summary for `o3` and `o4-mini`](/azure/ai-services/openai/how-to/reasoning)
-- [Evaluation API](/azure/ai-services/openai/authoring-reference-preview#evaluation---create)
-
-## Changes between 2025-03-01-preview and 2025-02-01-preview
-
-- [Responses API](./how-to/responses.md)
-- [Computer use](./how-to/computer-use.md)
-
-## Changes between 2025-02-01-preview and 2025-01-01-preview
-
-- [Stored completions (distillation)](./how-to/stored-completions.md#stored-completions-api) API support.
-
-## Changes between 2025-01-01-preview and 2024-12-01-preview
-
-- `prediction` parameter added for [predicted outputs](./how-to/predicted-outputs.md) support.
-- `gpt-4o-audio-preview` [model support](./audio-completions-quickstart.md).
-
-## Changes between 2024-12-01-preview and 2024-10-01-preview
-
-- `store`, and `metadata` parameters added for [stored completions support](./how-to/stored-completions.md).
-- `reasoning_effort` added for latest [reasoning models](./how-to/reasoning.md).
-- `user_security_context` added for [Microsoft Defender for Cloud integration](https://aka.ms/TP4AI/Documentation/EndUserContext).
-
-## Changes between 2024-09-01-preview and 2024-08-01-preview
-
-- `max_completion_tokens` added to support `o1-preview` and `o1-mini` models. `max_tokens` does not work with the **o1 series** models.
-- `parallel_tool_calls` added.
-- `completion_tokens_details` & `reasoning_tokens` added.
-- `stream_options` & `include_usage` added.
-
-## Changes between 2024-07-01-preview and 2024-08-01-preview API specification
-
-- [Structured outputs support](./how-to/structured-outputs.md).
-- Large file upload API added.
-- On your data changes:
-    * [Mongo DB integration](./reference-preview.md#example-7).
-    * `role_information` parameter removed.
-    *  [`rerank_score`](https://github.com/Azure/azure-rest-api-specs/blob/2b700e5e84d4a95880d373e6a4bce5d16882e4b5/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2024-08-01-preview/inference.json#L5532) added to citation object.
-    * AML datasource removed.
-    * AI Search vectorization integration improvements.
-
-## Changes between 2024-5-01-preview and 2024-07-01-preview API specification
-
-- [Batch API support added](./how-to/batch.md)
-- [Vector store chunking strategy parameters](/azure/ai-services/openai/reference-preview?#request-body-17)
-- `max_num_results` that the file search tool should output.
-
-## Changes between 2024-04-01-preview and 2024-05-01-preview API specification
-
-- Assistants v2 support - [File search tool and vector storage](https://go.microsoft.com/fwlink/?linkid=2272425)
-- Fine-tuning [checkpoints](https://github.com/Azure/azure-rest-api-specs/blob/9583ed6c26ce1f10bbea92346e28a46394a784b4/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/2024-05-01-preview/azureopenai.json#L586), [seed](https://github.com/Azure/azure-rest-api-specs/blob/9583ed6c26ce1f10bbea92346e28a46394a784b4/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/2024-05-01-preview/azureopenai.json#L1574), [events](https://github.com/Azure/azure-rest-api-specs/blob/9583ed6c26ce1f10bbea92346e28a46394a784b4/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/2024-05-01-preview/azureopenai.json#L529)
-- On your data updates
-- DALL-E 2 now supports model deployment and can be used with the latest preview API.
-- Content filtering updates
-
-## Changes between 2024-03-01-preview and 2024-04-01-preview API specification
-
-- **Breaking Change**: Enhancements parameters removed. This impacts the `gpt-4` **Version:** `vision-preview` model.
-- [timestamp_granularities](https://github.com/Azure/azure-rest-api-specs/blob/fbc90d63f236986f7eddfffe3dca6d9d734da0b2/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2024-04-01-preview/inference.json#L5217) parameter added.
-- [`audioWord`](https://github.com/Azure/azure-rest-api-specs/blob/fbc90d63f236986f7eddfffe3dca6d9d734da0b2/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2024-04-01-preview/inference.json#L5286) object added.
-- Additional TTS [`response_formats`: wav & pcm](https://github.com/Azure/azure-rest-api-specs/blob/fbc90d63f236986f7eddfffe3dca6d9d734da0b2/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2024-04-01-preview/inference.json#L5333).
-
-## Latest GA API release
-
-Azure OpenAI API version [2024-10-21](./reference.md) is currently the latest GA API release. This API version is the replacement for the previous `2024-06-01` GA API release.
-
-## Updating API versions
-
-We recommend first testing the upgrade to new API versions to confirm there's no impact to your application from the API update before making the change globally across your environment.
-
-If you're using the OpenAI Python or JavaScript client libraries, or the REST API, you'll need to update your code directly to the latest preview API version.
-
-If you're using one of the Azure OpenAI SDKs for C#, Go, or Java, you'll instead need to update to the latest version of the SDK. Each SDK release is hardcoded to work with specific versions of the Azure OpenAI API.
-
-## Next steps
-
-- [Learn more about Azure OpenAI](overview.md)
-- [Learn about working with Azure OpenAI models](./how-to/working-with-models.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "APIバージョン非推奨に関する文書の削除"
}
```

### Explanation
この変更は、Azure OpenAI APIのバージョン非推奨に関する文書が削除されたことを示しています。このファイル（`api-version-deprecation.md`）には、Azure OpenAI APIプレビューのサポートライフサイクルを理解するための情報が記載されており、新しいプレビューAPIの月次リリースの対象についても言及されていました。

削除された内容には、最新のAPIリリース、機能の変更、バージョンの更新方法、推奨事項など、多くの重要な情報が含まれていました。この情報は、ユーザーが新しいAPIバージョンに移行する際に必要な指針を提供するもので、破壊的な変更によってドキュメントが利用できなくなることで、ユーザーは新しいドキュメントやリソースを探す必要があります。

この変更は、APIのバージョン管理やサポートライフサイクルの透明性を確保するためのもので、利用者への影響を考慮して行われたものと考えられます。新しい情報や指針が他の文書で提供される可能性があるため、利用者には最新のドキュメントを参照することが推奨されます。

## articles/ai-services/openai/api-version-lifecycle.md{#item-92ab49}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,352 @@
+---
+title: Azure OpenAI in Azure AI Foundry Models API version lifecycle
+description: Learn more about API version retirement in Azure OpenAI.
+services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: conceptual 
+ms.date: 05/25/2025
+author: mrbullwinkle
+ms.author: mbullwin
+recommendations: false
+ms.custom:
+---
+
+# Azure OpenAI in Azure AI Foundry Models API lifecycle
+
+This article is to help you understand the support lifecycle for Azure OpenAI APIs.
+
+> [!NOTE]
+> New API response objects may be added to the API response without version changes. We recommend you only parse the response objects you require.
+>
+> The `2025-04-01-preview` Azure OpenAI spec uses OpenAPI 3.1, is a known issue that this is currently not fully supported by [Azure API Management](/azure/api-management/api-management-key-concepts)
+
+## API evolution
+
+Historically, Azure OpenAI received monthly updates of new API versions. Taking advantage of new features required constantly updating code and environment variables with each new API release. Azure OpenAI also required the extra step of using Azure specific clients which created overhead when migrating code between OpenAI and Azure OpenAI. Starting in May 2025, you can now opt in to our next generation of v1 Azure OpenAI APIs which add support for:
+
+- Ongoing access to the latest features with no need to update `api-version` each month.
+- OpenAI client support with minimal code changes to swap between OpenAI and Azure OpenAI when using key-based authentication.
+
+For the initial preview launch we are only supporting a subset of the inference API. While in preview, operations may have incomplete functionality that will be continually expanded.
+
+## Code changes
+
+# [API Key](#tab/key)
+
+### Last generation API 
+
+```python
+import os
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
+    api_version="2025-04-01-preview",
+    azure_endpoint="https://YOUR-RESOURCE-NAME.openai.azure.com")
+    )
+
+response = client.responses.create(
+    model="gpt-4.1-nano", # Replace with your model deployment name 
+    input="This is a test."
+)
+
+print(response.model_dump_json(indent=2)) 
+```
+
+### Next generation API
+
+```python
+import os
+from openai import OpenAI
+
+client = OpenAI(
+    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
+    base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",
+    default_query={"api-version": "preview"}, 
+)
+
+response = client.responses.create(   
+  model="gpt-4.1-nano", # Replace with your model deployment name 
+  input="This is a test.",
+)
+
+print(response.model_dump_json(indent=2)) 
+```
+
+- `OpenAI()` client is used instead of `AzureOpenAI()`.
+- `base_url` passes the Azure OpenAI endpoint and `/openai/v1` is appended to the endpoint address.
+- `default_query={"api-version": "preview"}` indicates that the version-less always up-to-date preview API is being used.
+
+Once we release the GA next generation v1 API, we will support two values: `latest` and `preview`. If `api-version` is not passed traffic is automatically routed to the `latest` GA version. Currently only `preview` is supported.
+
+# [Microsoft Entra ID](#tab/entra)
+
+### Last generation API 
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
+  azure_endpoint = "https://YOUR-RESOURCE-NAME.openai.azure.com/", 
+  azure_ad_token_provider=token_provider,
+  api_version="2025-04-01-preview"
+)
+
+response = client.responses.create(
+    model="gpt-4.1-nano", # Replace with your model deployment name 
+    input="This is a test."
+)
+
+print(response.model_dump_json(indent=2)) 
+```
+
+### Next generation API
+
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
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
+  azure_ad_token_provider=token_provider,
+  api_version="preview"
+)
+
+response = client.responses.create(
+    model="gpt-4.1-nano",
+    input= "This is a test" 
+)
+
+print(response.model_dump_json(indent=2)) 
+```
+
+- `AzureOpenAI()` is used to take advantage of automatic token refresh provided by `azure_ad_token_provider`.
+- `base_url` passes the Azure OpenAI endpoint and `/openai/v1` is appended to the endpoint address.
+- `api-version="preview"` indicates that the version-less always up-to-date preview API is being used.
+
+Once we release the GA next generation v1 API, we will support two values: `latest` and `preview`. If `api-version` is not passed traffic is automatically routed to the `latest` GA version. Currently only `preview` is supported.
+
+# [REST](#tab/rest)
+
+### Last generation API 
+
+**API Key**:
+
+```bash
+curl -X POST https://YOUR-RESOURCE-NAME.openai.azure.com/openai/responses?api-version=2025-04-01-preview \
+  -H "Content-Type: application/json" \
+  -H "api-key: $AZURE_OPENAI_API_KEY" \
+  -d '{
+     "model": "gpt-4.1-nano",
+     "input": "This is a test"
+    }'
+```
+
+**Microsoft Entra ID**:
+
+```bash
+curl -X POST https://YOUR-RESOURCE-NAME.openai.azure.com/openai/responses?api-version=2025-04-01-preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+  -d '{
+     "model": "gpt-4.1-nano",
+     "input": "This is a test"
+    }'
+```
+
+### Next generation API
+
+**API Key**:
+
+```bash
+curl -X POST https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses?api-version=preview \
+  -H "Content-Type: application/json" \
+  -H "api-key: $AZURE_OPENAI_API_KEY" \
+  -d '{
+     "model": "gpt-4.1-nano",
+     "input": "This is a test"
+    }'
+```
+
+**Microsoft Entra ID**:
+
+```bash
+curl -X POST https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses?api-version=preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+  -d '{
+     "model": "gpt-4o",
+     "input": "This is a test"
+    }'
+```
+
+# [Output](#tab/output)
+
+```json
+{
+  "id": "resp_682f7eb5dc408190b491cbbe57be2fbf0f98d661c3dc276d",
+  "created_at": 1747943093.0,
+  "error": null,
+  "incomplete_details": null,
+  "instructions": null,
+  "metadata": {},
+  "model": "gpt-4.1-nano",
+  "object": "response",
+  "output": [
+    {
+      "id": "msg_682f7eb61d908190926a004c15c5ddd00f98d661c3dc276d",
+      "content": [
+        {
+          "annotations": [],
+          "text": "Hello! It looks like you've sent a test message. How can I assist you today?",
+          "type": "output_text"
+        }
+      ],
+      "role": "assistant",
+      "status": "completed",
+      "type": "message"
+    }
+  ],
+  "parallel_tool_calls": true,
+  "temperature": 1.0,
+  "tool_choice": "auto",
+  "tools": [],
+  "top_p": 1.0,
+  "background": null,
+  "max_output_tokens": null,
+  "previous_response_id": null,
+  "reasoning": {
+    "effort": null,
+    "generate_summary": null,
+    "summary": null
+  },
+  "service_tier": "default",
+  "status": "completed",
+  "text": {
+    "format": {
+      "type": "text"
+    }
+  },
+  "truncation": "disabled",
+  "usage": {
+    "input_tokens": 12,
+    "input_tokens_details": {
+      "cached_tokens": 0
+    },
+    "output_tokens": 19,
+    "output_tokens_details": {
+      "reasoning_tokens": 0
+    },
+    "total_tokens": 31
+  },
+  "user": null,
+  "store": true
+}
+```
+
+---
+
+## Preview API releases
+
+Azure OpenAI API latest releases:
+
+- [**NEW** v1 Preview API](reference-preview-latest.md)
+- Inference: [2025-04-01-preview](reference-preview.md)
+- Authoring: [2025-04-01-preview](authoring-reference-preview.md)
+
+## Changes between v1 preview release and 2025-04-01-preview
+
+- [v1 preview API](#api-evolution)
+
+## Changes between 2025-04-01-preview and 2025-03-01-preview
+
+- [`GPT-image-1` support](/azure/ai-services/openai/how-to/dall-e)
+- [Reasoning summary for `o3` and `o4-mini`](/azure/ai-services/openai/how-to/reasoning)
+- [Evaluation API](/azure/ai-services/openai/authoring-reference-preview#evaluation---create)
+
+## Changes between 2025-03-01-preview and 2025-02-01-preview
+
+- [Responses API](./how-to/responses.md)
+- [Computer use](./how-to/computer-use.md)
+
+## Changes between 2025-02-01-preview and 2025-01-01-preview
+
+- [Stored completions (distillation)](./how-to/stored-completions.md#stored-completions-api) API support.
+
+## Changes between 2025-01-01-preview and 2024-12-01-preview
+
+- `prediction` parameter added for [predicted outputs](./how-to/predicted-outputs.md) support.
+- `gpt-4o-audio-preview` [model support](./audio-completions-quickstart.md).
+
+## Changes between 2024-12-01-preview and 2024-10-01-preview
+
+- `store`, and `metadata` parameters added for [stored completions support](./how-to/stored-completions.md).
+- `reasoning_effort` added for latest [reasoning models](./how-to/reasoning.md).
+- `user_security_context` added for [Microsoft Defender for Cloud integration](https://aka.ms/TP4AI/Documentation/EndUserContext).
+
+## Changes between 2024-09-01-preview and 2024-08-01-preview
+
+- `max_completion_tokens` added to support `o1-preview` and `o1-mini` models. `max_tokens` does not work with the **o1 series** models.
+- `parallel_tool_calls` added.
+- `completion_tokens_details` & `reasoning_tokens` added.
+- `stream_options` & `include_usage` added.
+
+## Changes between 2024-07-01-preview and 2024-08-01-preview API specification
+
+- [Structured outputs support](./how-to/structured-outputs.md).
+- Large file upload API added.
+- On your data changes:
+    * [Mongo DB integration](./reference-preview.md#example-7).
+    * `role_information` parameter removed.
+    *  [`rerank_score`](https://github.com/Azure/azure-rest-api-specs/blob/2b700e5e84d4a95880d373e6a4bce5d16882e4b5/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2024-08-01-preview/inference.json#L5532) added to citation object.
+    * AML datasource removed.
+    * AI Search vectorization integration improvements.
+
+## Changes between 2024-5-01-preview and 2024-07-01-preview API specification
+
+- [Batch API support added](./how-to/batch.md)
+- [Vector store chunking strategy parameters](/azure/ai-services/openai/reference-preview?#request-body-17)
+- `max_num_results` that the file search tool should output.
+
+## Changes between 2024-04-01-preview and 2024-05-01-preview API specification
+
+- Assistants v2 support - [File search tool and vector storage](https://go.microsoft.com/fwlink/?linkid=2272425)
+- Fine-tuning [checkpoints](https://github.com/Azure/azure-rest-api-specs/blob/9583ed6c26ce1f10bbea92346e28a46394a784b4/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/2024-05-01-preview/azureopenai.json#L586), [seed](https://github.com/Azure/azure-rest-api-specs/blob/9583ed6c26ce1f10bbea92346e28a46394a784b4/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/2024-05-01-preview/azureopenai.json#L1574), [events](https://github.com/Azure/azure-rest-api-specs/blob/9583ed6c26ce1f10bbea92346e28a46394a784b4/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/2024-05-01-preview/azureopenai.json#L529)
+- On your data updates
+- DALL-E 2 now supports model deployment and can be used with the latest preview API.
+- Content filtering updates
+
+## Changes between 2024-03-01-preview and 2024-04-01-preview API specification
+
+- **Breaking Change**: Enhancements parameters removed. This impacts the `gpt-4` **Version:** `vision-preview` model.
+- [timestamp_granularities](https://github.com/Azure/azure-rest-api-specs/blob/fbc90d63f236986f7eddfffe3dca6d9d734da0b2/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2024-04-01-preview/inference.json#L5217) parameter added.
+- [`audioWord`](https://github.com/Azure/azure-rest-api-specs/blob/fbc90d63f236986f7eddfffe3dca6d9d734da0b2/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2024-04-01-preview/inference.json#L5286) object added.
+- Additional TTS [`response_formats: wav & pcm`](https://github.com/Azure/azure-rest-api-specs/blob/fbc90d63f236986f7eddfffe3dca6d9d734da0b2/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2024-04-01-preview/inference.json#L5333).
+
+## Latest GA API release
+
+Azure OpenAI API version [2024-10-21](./reference.md) is currently the latest GA API release. This API version is the replacement for the previous `2024-06-01` GA API release.
+
+## Updating API versions
+
+We recommend first testing the upgrade to new API versions to confirm there's no impact to your application from the API update before making the change globally across your environment.
+
+If you're using the OpenAI Python or JavaScript client libraries, or the REST API, you'll need to update your code directly to the latest preview API version.
+
+If you're using one of the Azure OpenAI SDKs for C#, Go, or Java, you'll instead need to update to the latest version of the SDK. Each SDK release is hardcoded to work with specific versions of the Azure OpenAI API.
+
+## Next steps
+
+- [Learn more about Azure OpenAI](overview.md)
+- [Learn about working with Azure OpenAI models](./how-to/working-with-models.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAI APIのバージョンライフサイクルに関する新しい文書の追加"
}
```

### Explanation
この変更は、Azure OpenAI APIのバージョンライフサイクルに関する新しい文書（`api-version-lifecycle.md`）が追加されたことを示しています。この文書は、Azure OpenAI APIのサポートライフサイクルの理解を助けるために作成されており、APIの進化と、どのように新機能にアクセスできるかについてのガイダンスを提供しています。

文書には、APIの進化に関する歴史的背景、新しいAPIの設計、使用方法の例（APIキーを使った接続やMicrosoft Entra IDを使用した接続）などが含まれており、特に次世代APIについての詳細が記載されています。また、ユーザーが新しいAPIバージョンに移行する際の注意点や、現行のプレビューAPIの使用に関する情報も提供しています。

この追加により、ユーザーはAzure OpenAI APIの使用において、最新の仕様やベストプラクティスを理解しやすくなり、情報を効果的に活用できるようになります。新しい文書は352行にわたるもので、APIの機能や利用方法に関する包括的な情報源となっています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 05/23/2025
+ms.date: 05/28/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -434,8 +434,6 @@ These models can only be used with Embedding API requests.
 
 [!INCLUDE [Image Generation](../includes/model-matrix/standard-image-generation.md)]
 
-### Image generation models
-
 |  Model ID  | Max Request (characters) |
 |  --- | :---: |
 | gpt-image-1 | 4,000 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルに関するドキュメントの日付更新と内容変更"
}
```

### Explanation
この変更は、Azure OpenAIに関するモデルのドキュメント（`models.md`）に対する軽微な更新を示しています。具体的には、ドキュメントの日付が更新され（`ms.date`が2025年5月23日から2025年5月28日に変更）、また、いくつかの行が削除されて内容が簡略化されています。特に、「画像生成モデル」というセクション全体が削除され、視覚的モデルに関する具体的な情報が文書から省かれています。

この変更により、読者に最新の情報を提供しつつ、無駄が省かれた、より集中した内容になっていることが示唆されています。変更内容は、総じてモデルの使用に関する情報の明確性を高めるためのものと見受けられます。これにより、ユーザーはAzure OpenAIのモデルについて理解しやすくなり、適切なモデルを選択する助けとなります。

## articles/ai-services/openai/concepts/use-your-data.md{#item-455d6e}

<details>
<summary>Diff</summary>
````diff
@@ -721,6 +721,7 @@ Each user message can translate to multiple search queries, all of which get sen
 > The following models are not supported by Azure OpenAI On Your Data:
 > * o1 models
 > * o3 models
+> * model-router
 
 | Region | `gpt-35-turbo-16k (0613)` | `gpt-35-turbo (1106)` | `gpt-4-32k (0613)` | `gpt-4 (1106-preview)` | `gpt-4 (0125-preview)` | `gpt-4 (0613)`  | `gpt-4o`\*\* | `gpt-4 (turbo-2024-04-09)` |
 |------|---|---|---|---|---|----|----|----|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルサポートに関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIにおけるデータの使用に関する文書（`use-your-data.md`）に対する軽微な更新を示しています。具体的には、サポートされていないモデルのリストに「model-router」が追加されました。この更新により、ユーザーは使用できないモデルについての最新情報を得ることができ、サポートされるモデルの選択時に考慮すべき追加要素が明確になっています。

これにより、ユーザーはモデル選択の際に誤った選択を避けることができ、より良い意思決定を行う手助けとなるでしょう。この変更は、ユーザーが利用可能なリソースをより効果的に活用できるようにするためのものであり、実践的なガイダンスを提供しています。

## articles/ai-services/openai/how-to/computer-use.md{#item-6fbca8}

<details>
<summary>Diff</summary>
````diff
@@ -64,10 +64,10 @@ from openai import AzureOpenAI
 #from openai import OpenAI
 token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")
 
-client = AzureOpenAI(
-    azure_ad_token_provider=token_provider,
-    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
-    api_version="2025-03-01-preview"
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
+  azure_ad_token_provider=token_provider,
+  api_version="preview"
 )
 
 response = client.responses.create(
@@ -108,7 +108,7 @@ print(response.output)
 ## [REST API](#tab/rest-api)
 
 ```bash
-curl ${MY_ENDPOINT}/openai/responses?api-version=2025-03-01-preview \ 
+curl ${MY_ENDPOINT}/openai/v1/responses?api-version=preview \ 
   -H "Content-Type: application/json" \ 
   -H "api-key: $MY_API_KEY" \ 
   -d '{ 
@@ -244,7 +244,7 @@ response_2 = client.responses.create(
 ## [REST API](#tab/rest-api)
 
 ```bash
-curl ${MY_ENDPOINT}/openai/responses?api-version=2025-03-01-preview \ 
+curl ${MY_ENDPOINT}/openai/v1/responses?api-version=preview \ 
   -H "Content-Type: application/json" \ 
   -H "api-key: $MY_API_KEY" \ 
   -d '{ 
@@ -359,8 +359,840 @@ In all cases where `pending_safety_checks` are returned, actions should be hande
 * `malicious_instructions` and `irrelevant_domain`: end users should review model actions and confirm that the model is behaving as intended.
 * `sensitive_domain`: ensure an end user is actively monitoring the model actions on these sites. Exact implementation of this "watch mode" can vary by application, but a potential example could be collecting user impression data on the site to make sure there is active end user engagement with the application.
 
+## Playwright integration
+
+In this section, we provide a simple example script that integrates Azure OpenAI's `computer-use-preview` model with [Playwright](https://playwright.dev/) to automate basic browser interactions. Combining the model with [Playwright](https://playwright.dev/) allows the model to see the browser screen, make decisions, and perform actions like clicking, typing, and navigating websites. You should exercise caution when running this example code. This code is designed to be run locally but should only be executed in a test environment. Use a human to confirm decisions and don't give the model access to sensitive data.
+
+:::image type="content" source="../media/computer-use-preview.gif" alt-text="Animated gif of computer-use-preview model integrated with playwright." lightbox="../media/computer-use-preview.gif":::
+
+First you'll need to install the Python library for [Playwright](https://playwright.dev/).
+
+```cmd
+pip install playwright
+```
+
+Once the package is installed, you'll also need to run
+
+```cmd
+playwright install
+```
+
+### Imports and configuration
+
+First, we import the necessary libraries and define our configuration parameters. Since we're using `asyncio` we'll be executing this code outside of Jupyter notebooks. We'll walk through the code first in chunks and then demonstrate how to use it.
+
+```python
+import os
+import asyncio
+import base64
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+from playwright.async_api import async_playwright, TimeoutError
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+
+# Configuration
+
+BASE_URL = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/"
+MODEL = "computer-use-preview" # Set to model deployment name
+DISPLAY_WIDTH = 1024
+DISPLAY_HEIGHT = 768
+API_VERSION = "preview" #Use this API version or later
+ITERATIONS = 5 # Max number of iterations before returning control to human supervisor
+```
+
+### Key mapping for browser interaction
+
+Next, we set up mappings for special keys that the model might need to pass to Playwright. Ultimately the model is never performing actions itself, it passes representations of commands and you have to provide the final integration layer that can take those commands and execute them in your chosen environment.
+
+This isn't an exhaustive list of possible key mappings. You can expand this list as needed. This dictionary is specific to integrating the model with Playwright. If you were integrating the model with an alternate library to provide API access to your operating systems keyboard/mouse you would need to provide a mapping specific to that library.
+
+```python
+# Key mapping for special keys in Playwright
+KEY_MAPPING = {
+    "/": "Slash", "\\": "Backslash", "alt": "Alt", "arrowdown": "ArrowDown",
+    "arrowleft": "ArrowLeft", "arrowright": "ArrowRight", "arrowup": "ArrowUp",
+    "backspace": "Backspace", "ctrl": "Control", "delete": "Delete", 
+    "enter": "Enter", "esc": "Escape", "shift": "Shift", "space": " ",
+    "tab": "Tab", "win": "Meta", "cmd": "Meta", "super": "Meta", "option": "Alt"
+}
+```
+
+This dictionary translates user-friendly key names to the format expected by Playwright's keyboard API.
+
+### Coordinate validation function
+
+To make sure that any mouse actions that are passed from the model stay within the browser window boundaries we'll add the following utility function:
+
+```python
+def validate_coordinates(x, y):
+    """Ensure coordinates are within display bounds."""
+    return max(0, min(x, DISPLAY_WIDTH)), max(0, min(y, DISPLAY_HEIGHT))
+```
+
+This simple utility attempts to prevent out-of-bounds errors by clamping coordinates to the window dimensions.
+
+### Action handling
+
+The core of our browser automation is the action handler that processes various types of user interactions and convert them into actions within the browser.
+
+```python
+async def handle_action(page, action):
+    """Handle different action types from the model."""
+    action_type = action.type
+    
+    if action_type == "drag":
+        print("Drag action is not supported in this implementation. Skipping.")
+        return
+        
+    elif action_type == "click":
+        button = getattr(action, "button", "left")
+        # Validate coordinates
+        x, y = validate_coordinates(action.x, action.y)
+        
+        print(f"\tAction: click at ({x}, {y}) with button '{button}'")
+        
+        if button == "back":
+            await page.go_back()
+        elif button == "forward":
+            await page.go_forward()
+        elif button == "wheel":
+            await page.mouse.wheel(x, y)
+        else:
+            button_type = {"left": "left", "right": "right", "middle": "middle"}.get(button, "left")
+            await page.mouse.click(x, y, button=button_type)
+            try:
+                await page.wait_for_load_state("domcontentloaded", timeout=3000)
+            except TimeoutError:
+                pass
+        
+    elif action_type == "double_click":
+        # Validate coordinates
+        x, y = validate_coordinates(action.x, action.y)
+        
+        print(f"\tAction: double click at ({x}, {y})")
+        await page.mouse.dblclick(x, y)
+        
+    elif action_type == "scroll":
+        scroll_x = getattr(action, "scroll_x", 0)
+        scroll_y = getattr(action, "scroll_y", 0)
+        # Validate coordinates
+        x, y = validate_coordinates(action.x, action.y)
+        
+        print(f"\tAction: scroll at ({x}, {y}) with offsets ({scroll_x}, {scroll_y})")
+        await page.mouse.move(x, y)
+        await page.evaluate(f"window.scrollBy({{left: {scroll_x}, top: {scroll_y}, behavior: 'smooth'}});")
+        
+    elif action_type == "keypress":
+        keys = getattr(action, "keys", [])
+        print(f"\tAction: keypress {keys}")
+        mapped_keys = [KEY_MAPPING.get(key.lower(), key) for key in keys]
+        
+        if len(mapped_keys) > 1:
+            # For key combinations (like Ctrl+C)
+            for key in mapped_keys:
+                await page.keyboard.down(key)
+            await asyncio.sleep(0.1)
+            for key in reversed(mapped_keys):
+                await page.keyboard.up(key)
+        else:
+            for key in mapped_keys:
+                await page.keyboard.press(key)
+                
+    elif action_type == "type":
+        text = getattr(action, "text", "")
+        print(f"\tAction: type text: {text}")
+        await page.keyboard.type(text, delay=20)
+        
+    elif action_type == "wait":
+        ms = getattr(action, "ms", 1000)
+        print(f"\tAction: wait {ms}ms")
+        await asyncio.sleep(ms / 1000)
+        
+    elif action_type == "screenshot":
+        print("\tAction: screenshot")
+        
+    else:
+        print(f"\tUnrecognized action: {action_type}")
+```
+
+This function attempts to handle various types of actions. We need to translate between the commands that the `computer-use-preview` will generate and the Playwright library which will execute the actions. For more information refer to the reference documentation for `ComputerAction`.
+
+- [Click](/azure/ai-services/openai/reference-preview#click)
+- [DoubleClick](/azure/ai-services/openai/reference-preview#doubleclick)
+- [Drag](/azure/ai-services/openai/reference-preview#drag)
+- [KeyPress](/azure/ai-services/openai/reference-preview#keypress)
+- [Move](/azure/ai-services/openai/reference-preview#move)
+- [Screenshot](/azure/ai-services/openai/reference-preview#screenshot)
+- [Scroll](/azure/ai-services/openai/reference-preview#scroll)
+- [Type](/azure/ai-services/openai/reference-preview#type)
+- [Wait](/azure/ai-services/openai/reference-preview#wait)
+
+### Screenshot capture
+
+In order for the model to be able to see what it's interacting with the model needs a way to capture screenshots. For this code we're using Playwright to capture the screenshots and we're limiting the view to just the content in the browser window. The screenshot won't include the url bar or other aspects of the browser GUI. If you need the model to see outside the main browser window you could augment the model by creating your own screenshot function. 
+
+```python
+async def take_screenshot(page):
+    """Take a screenshot and return base64 encoding with caching for failures."""
+    global last_successful_screenshot
+    
+    try:
+        screenshot_bytes = await page.screenshot(full_page=False)
+        last_successful_screenshot = base64.b64encode(screenshot_bytes).decode("utf-8")
+        return last_successful_screenshot
+    except Exception as e:
+        print(f"Screenshot failed: {e}")
+        print(f"Using cached screenshot from previous successful capture")
+        if last_successful_screenshot:
+            return last_successful_screenshot
+```
+
+This function captures the current browser state as an image and returns it as a base64-encoded string, ready to be sent to the model. We'll constantly do this in a loop after each step allowing the model to see if the command it tried to execute was successful or not, which then allows it to adjust based on the contents of the screenshot. We could let the model decide if it needs to take a screenshot, but for simplicity we will force a screenshot to be taken for each iteration.
+
+### Model response processing
+
+This function processes the model's responses and executes the requested actions:
+
+```python
+async def process_model_response(client, response, page, max_iterations=ITERATIONS):
+    """Process the model's response and execute actions."""
+    for iteration in range(max_iterations):
+        if not hasattr(response, 'output') or not response.output:
+            print("No output from model.")
+            break
+        
+        # Safely access response id
+        response_id = getattr(response, 'id', 'unknown')
+        print(f"\nIteration {iteration + 1} - Response ID: {response_id}\n")
+        
+        # Print text responses and reasoning
+        for item in response.output:
+            # Handle text output
+            if hasattr(item, 'type') and item.type == "text":
+                print(f"\nModel message: {item.text}\n")
+                
+            # Handle reasoning output
+            if hasattr(item, 'type') and item.type == "reasoning":
+                # Extract meaningful content from the reasoning
+                meaningful_content = []
+                
+                if hasattr(item, 'summary') and item.summary:
+                    for summary in item.summary:
+                        # Handle different potential formats of summary content
+                        if isinstance(summary, str) and summary.strip():
+                            meaningful_content.append(summary)
+                        elif hasattr(summary, 'text') and summary.text.strip():
+                            meaningful_content.append(summary.text)
+                
+                # Only print reasoning section if there's actual content
+                if meaningful_content:
+                    print("=== Model Reasoning ===")
+                    for idx, content in enumerate(meaningful_content, 1):
+                        print(f"{content}")
+                    print("=====================\n")
+        
+        # Extract computer calls
+        computer_calls = [item for item in response.output 
+                         if hasattr(item, 'type') and item.type == "computer_call"]
+        
+        if not computer_calls:
+            print("No computer call found in response. Reverting control to human operator")
+            break
+        
+        computer_call = computer_calls[0]
+        if not hasattr(computer_call, 'call_id') or not hasattr(computer_call, 'action'):
+            print("Computer call is missing required attributes.")
+            break
+        
+        call_id = computer_call.call_id
+        action = computer_call.action
+        
+        # Handle safety checks
+        acknowledged_checks = []
+        if hasattr(computer_call, 'pending_safety_checks') and computer_call.pending_safety_checks:
+            pending_checks = computer_call.pending_safety_checks
+            print("\nSafety checks required:")
+            for check in pending_checks:
+                print(f"- {check.code}: {check.message}")
+            
+            if input("\nDo you want to proceed? (y/n): ").lower() != 'y':
+                print("Operation cancelled by user.")
+                break
+            
+            acknowledged_checks = pending_checks
+        
+        # Execute the action
+        try:
+           await page.bring_to_front()
+           await handle_action(page, action)
+           
+           # Check if a new page was created after the action
+           if action.type in ["click"]:
+               await asyncio.sleep(1.5)
+               # Get all pages in the context
+               all_pages = page.context.pages
+               # If we have multiple pages, check if there's a newer one
+               if len(all_pages) > 1:
+                   newest_page = all_pages[-1]  # Last page is usually the newest
+                   if newest_page != page and newest_page.url not in ["about:blank", ""]:
+                       print(f"\tSwitching to new tab: {newest_page.url}")
+                       page = newest_page  # Update our page reference
+           elif action.type != "wait":
+               await asyncio.sleep(0.5)
+               
+        except Exception as e:
+           print(f"Error handling action {action.type}: {e}")
+           import traceback
+           traceback.print_exc()    
+
+        # Take a screenshot after the action
+        screenshot_base64 = await take_screenshot(page)
+
+        print("\tNew screenshot taken")
+        
+        # Prepare input for the next request
+        input_content = [{
+            "type": "computer_call_output",
+            "call_id": call_id,
+            "output": {
+                "type": "input_image",
+                "image_url": f"data:image/png;base64,{screenshot_base64}"
+            }
+        }]
+        
+        # Add acknowledged safety checks if any
+        if acknowledged_checks:
+            acknowledged_checks_dicts = []
+            for check in acknowledged_checks:
+                acknowledged_checks_dicts.append({
+                    "id": check.id,
+                    "code": check.code,
+                    "message": check.message
+                })
+            input_content[0]["acknowledged_safety_checks"] = acknowledged_checks_dicts
+        
+        # Add current URL for context
+        try:
+            current_url = page.url
+            if current_url and current_url != "about:blank":
+                input_content[0]["current_url"] = current_url
+                print(f"\tCurrent URL: {current_url}")
+        except Exception as e:
+            print(f"Error getting URL: {e}")
+        
+        # Send the screenshot back for the next step
+        try:
+            response = client.responses.create(
+                model=MODEL,
+                previous_response_id=response_id,
+                tools=[{
+                    "type": "computer_use_preview",
+                    "display_width": DISPLAY_WIDTH,
+                    "display_height": DISPLAY_HEIGHT,
+                    "environment": "browser"
+                }],
+                input=input_content,
+                truncation="auto"
+            )
+
+            print("\tModel processing screenshot")
+        except Exception as e:
+            print(f"Error in API call: {e}")
+            import traceback
+            traceback.print_exc()
+            break
+    
+    if iteration >= max_iterations - 1:
+        print("Reached maximum number of iterations. Stopping.")
+```
+
+In this section we have added code that:
+
+- Extracts and displays text and reasoning from the model.
+- Processes computer action calls.
+- Handles potential safety checks requiring user confirmation.
+- Executes the requested action.
+- Captures a new screenshot.
+- Sends the updated state back to the model and defines the [`ComputerTool`](/azure/ai-services/openai/reference-preview#computertool).
+- Repeats this process for multiple iterations.
+
+### Main function
+
+The main function coordinates the entire process:
+
+```python
+    # Initialize OpenAI client
+    client = AzureOpenAI(
+        base_url=BASE_URL,
+        azure_ad_token_provider=token_provider,
+        api_version=API_VERSION
+    )
+    
+    # Initialize Playwright
+    async with async_playwright() as playwright:
+        browser = await playwright.chromium.launch(
+            headless=False,
+            args=[f"--window-size={DISPLAY_WIDTH},{DISPLAY_HEIGHT}", "--disable-extensions"]
+        )
+        
+        context = await browser.new_context(
+            viewport={"width": DISPLAY_WIDTH, "height": DISPLAY_HEIGHT},
+            accept_downloads=True
+        )
+        
+        page = await context.new_page()
+        
+        # Navigate to starting page
+        await page.goto("https://www.bing.com", wait_until="domcontentloaded")
+        print("Browser initialized to Bing.com")
+        
+        # Main interaction loop
+        try:
+            while True:
+                print("\n" + "="*50)
+                user_input = input("Enter a task to perform (or 'exit' to quit): ")
+                
+                if user_input.lower() in ('exit', 'quit'):
+                    break
+                
+                if not user_input.strip():
+                    continue
+                
+                # Take initial screenshot
+                screenshot_base64 = await take_screenshot(page)
+                print("\nTake initial screenshot")
+                
+                # Initial request to the model
+                response = client.responses.create(
+                    model=MODEL,
+                    tools=[{
+                        "type": "computer_use_preview",
+                        "display_width": DISPLAY_WIDTH,
+                        "display_height": DISPLAY_HEIGHT,
+                        "environment": "browser"
+                    }],
+                    instructions = "You are an AI agent with the ability to control a browser. You can control the keyboard and mouse. You take a screenshot after each action to check if your action was successful. Once you have completed the requested task you should stop running and pass back control to your human operator.",
+                    input=[{
+                        "role": "user",
+                        "content": [{
+                            "type": "input_text",
+                            "text": user_input
+                        }, {
+                            "type": "input_image",
+                            "image_url": f"data:image/png;base64,{screenshot_base64}"
+                        }]
+                    }],
+                    reasoning={"generate_summary": "concise"},
+                    truncation="auto"
+                )
+                print("\nSending model initial screenshot and instructions")
+
+                # Process model actions
+                await process_model_response(client, response, page)
+                
+        except Exception as e:
+            print(f"An error occurred: {e}")
+            import traceback
+            traceback.print_exc()
+        
+        finally:
+            # Close browser
+            await context.close()
+            await browser.close()
+            print("Browser closed.")
+
+if __name__ == "__main__":
+    asyncio.run(main())
+```
+
+The main function:
+
+- Initializes the AzureOpenAI client.
+- Sets up the Playwright browser.
+- Starts at Bing.com.
+- Enters a loop to accept user tasks.
+- Captures the initial state.
+- Sends the task and screenshot to the model.
+- Processes the model's response.
+- Repeats until the user exits.
+- Ensures the browser is properly closed.
+
+### Complete script
+
+> [!CAUTION]
+> This code is experimental and for demonstration purposes only. It's only intended to illustrate the basic flow of the responses API and the `computer-use-preview` model. While you can execute this code on your local computer, we strongly recommend running this code on a low privilege virtual machine with no access to sensitive data. This code is for basic testing purposes only.
+
+```python
+import os
+import asyncio
+import base64
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+from playwright.async_api import async_playwright, TimeoutError
+
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+# Configuration
+
+BASE_URL = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/"
+MODEL = "computer-use-preview"
+DISPLAY_WIDTH = 1024
+DISPLAY_HEIGHT = 768
+API_VERSION = "preview"
+ITERATIONS = 5 # Max number of iterations before forcing the model to return control to the human supervisor
+
+# Key mapping for special keys in Playwright
+KEY_MAPPING = {
+    "/": "Slash", "\\": "Backslash", "alt": "Alt", "arrowdown": "ArrowDown",
+    "arrowleft": "ArrowLeft", "arrowright": "ArrowRight", "arrowup": "ArrowUp",
+    "backspace": "Backspace", "ctrl": "Control", "delete": "Delete", 
+    "enter": "Enter", "esc": "Escape", "shift": "Shift", "space": " ",
+    "tab": "Tab", "win": "Meta", "cmd": "Meta", "super": "Meta", "option": "Alt"
+}
+
+def validate_coordinates(x, y):
+    """Ensure coordinates are within display bounds."""
+    return max(0, min(x, DISPLAY_WIDTH)), max(0, min(y, DISPLAY_HEIGHT))
+
+async def handle_action(page, action):
+    """Handle different action types from the model."""
+    action_type = action.type
+    
+    if action_type == "drag":
+        print("Drag action is not supported in this implementation. Skipping.")
+        return
+        
+    elif action_type == "click":
+        button = getattr(action, "button", "left")
+        # Validate coordinates
+        x, y = validate_coordinates(action.x, action.y)
+        
+        print(f"\tAction: click at ({x}, {y}) with button '{button}'")
+        
+        if button == "back":
+            await page.go_back()
+        elif button == "forward":
+            await page.go_forward()
+        elif button == "wheel":
+            await page.mouse.wheel(x, y)
+        else:
+            button_type = {"left": "left", "right": "right", "middle": "middle"}.get(button, "left")
+            await page.mouse.click(x, y, button=button_type)
+            try:
+                await page.wait_for_load_state("domcontentloaded", timeout=3000)
+            except TimeoutError:
+                pass
+        
+    elif action_type == "double_click":
+        # Validate coordinates
+        x, y = validate_coordinates(action.x, action.y)
+        
+        print(f"\tAction: double click at ({x}, {y})")
+        await page.mouse.dblclick(x, y)
+        
+    elif action_type == "scroll":
+        scroll_x = getattr(action, "scroll_x", 0)
+        scroll_y = getattr(action, "scroll_y", 0)
+        # Validate coordinates
+        x, y = validate_coordinates(action.x, action.y)
+        
+        print(f"\tAction: scroll at ({x}, {y}) with offsets ({scroll_x}, {scroll_y})")
+        await page.mouse.move(x, y)
+        await page.evaluate(f"window.scrollBy({{left: {scroll_x}, top: {scroll_y}, behavior: 'smooth'}});")
+        
+    elif action_type == "keypress":
+        keys = getattr(action, "keys", [])
+        print(f"\tAction: keypress {keys}")
+        mapped_keys = [KEY_MAPPING.get(key.lower(), key) for key in keys]
+        
+        if len(mapped_keys) > 1:
+            # For key combinations (like Ctrl+C)
+            for key in mapped_keys:
+                await page.keyboard.down(key)
+            await asyncio.sleep(0.1)
+            for key in reversed(mapped_keys):
+                await page.keyboard.up(key)
+        else:
+            for key in mapped_keys:
+                await page.keyboard.press(key)
+                
+    elif action_type == "type":
+        text = getattr(action, "text", "")
+        print(f"\tAction: type text: {text}")
+        await page.keyboard.type(text, delay=20)
+        
+    elif action_type == "wait":
+        ms = getattr(action, "ms", 1000)
+        print(f"\tAction: wait {ms}ms")
+        await asyncio.sleep(ms / 1000)
+        
+    elif action_type == "screenshot":
+        print("\tAction: screenshot")
+        
+    else:
+        print(f"\tUnrecognized action: {action_type}")
+
+async def take_screenshot(page):
+    """Take a screenshot and return base64 encoding with caching for failures."""
+    global last_successful_screenshot
+    
+    try:
+        screenshot_bytes = await page.screenshot(full_page=False)
+        last_successful_screenshot = base64.b64encode(screenshot_bytes).decode("utf-8")
+        return last_successful_screenshot
+    except Exception as e:
+        print(f"Screenshot failed: {e}")
+        print(f"Using cached screenshot from previous successful capture")
+        if last_successful_screenshot:
+            return last_successful_screenshot
+
+
+async def process_model_response(client, response, page, max_iterations=ITERATIONS):
+    """Process the model's response and execute actions."""
+    for iteration in range(max_iterations):
+        if not hasattr(response, 'output') or not response.output:
+            print("No output from model.")
+            break
+        
+        # Safely access response id
+        response_id = getattr(response, 'id', 'unknown')
+        print(f"\nIteration {iteration + 1} - Response ID: {response_id}\n")
+        
+        # Print text responses and reasoning
+        for item in response.output:
+            # Handle text output
+            if hasattr(item, 'type') and item.type == "text":
+                print(f"\nModel message: {item.text}\n")
+                
+            # Handle reasoning output
+            if hasattr(item, 'type') and item.type == "reasoning":
+                # Extract meaningful content from the reasoning
+                meaningful_content = []
+                
+                if hasattr(item, 'summary') and item.summary:
+                    for summary in item.summary:
+                        # Handle different potential formats of summary content
+                        if isinstance(summary, str) and summary.strip():
+                            meaningful_content.append(summary)
+                        elif hasattr(summary, 'text') and summary.text.strip():
+                            meaningful_content.append(summary.text)
+                
+                # Only print reasoning section if there's actual content
+                if meaningful_content:
+                    print("=== Model Reasoning ===")
+                    for idx, content in enumerate(meaningful_content, 1):
+                        print(f"{content}")
+                    print("=====================\n")
+        
+        # Extract computer calls
+        computer_calls = [item for item in response.output 
+                         if hasattr(item, 'type') and item.type == "computer_call"]
+        
+        if not computer_calls:
+            print("No computer call found in response. Reverting control to human supervisor")
+            break
+        
+        computer_call = computer_calls[0]
+        if not hasattr(computer_call, 'call_id') or not hasattr(computer_call, 'action'):
+            print("Computer call is missing required attributes.")
+            break
+        
+        call_id = computer_call.call_id
+        action = computer_call.action
+        
+        # Handle safety checks
+        acknowledged_checks = []
+        if hasattr(computer_call, 'pending_safety_checks') and computer_call.pending_safety_checks:
+            pending_checks = computer_call.pending_safety_checks
+            print("\nSafety checks required:")
+            for check in pending_checks:
+                print(f"- {check.code}: {check.message}")
+            
+            if input("\nDo you want to proceed? (y/n): ").lower() != 'y':
+                print("Operation cancelled by user.")
+                break
+            
+            acknowledged_checks = pending_checks
+        
+        # Execute the action
+        try:
+           await page.bring_to_front()
+           await handle_action(page, action)
+           
+           # Check if a new page was created after the action
+           if action.type in ["click"]:
+               await asyncio.sleep(1.5)
+               # Get all pages in the context
+               all_pages = page.context.pages
+               # If we have multiple pages, check if there's a newer one
+               if len(all_pages) > 1:
+                   newest_page = all_pages[-1]  # Last page is usually the newest
+                   if newest_page != page and newest_page.url not in ["about:blank", ""]:
+                       print(f"\tSwitching to new tab: {newest_page.url}")
+                       page = newest_page  # Update our page reference
+           elif action.type != "wait":
+               await asyncio.sleep(0.5)
+               
+        except Exception as e:
+           print(f"Error handling action {action.type}: {e}")
+           import traceback
+           traceback.print_exc()    
+
+        # Take a screenshot after the action
+        screenshot_base64 = await take_screenshot(page)
+
+        print("\tNew screenshot taken")
+        
+        # Prepare input for the next request
+        input_content = [{
+            "type": "computer_call_output",
+            "call_id": call_id,
+            "output": {
+                "type": "input_image",
+                "image_url": f"data:image/png;base64,{screenshot_base64}"
+            }
+        }]
+        
+        # Add acknowledged safety checks if any
+        if acknowledged_checks:
+            acknowledged_checks_dicts = []
+            for check in acknowledged_checks:
+                acknowledged_checks_dicts.append({
+                    "id": check.id,
+                    "code": check.code,
+                    "message": check.message
+                })
+            input_content[0]["acknowledged_safety_checks"] = acknowledged_checks_dicts
+        
+        # Add current URL for context
+        try:
+            current_url = page.url
+            if current_url and current_url != "about:blank":
+                input_content[0]["current_url"] = current_url
+                print(f"\tCurrent URL: {current_url}")
+        except Exception as e:
+            print(f"Error getting URL: {e}")
+        
+        # Send the screenshot back for the next step
+        try:
+            response = client.responses.create(
+                model=MODEL,
+                previous_response_id=response_id,
+                tools=[{
+                    "type": "computer_use_preview",
+                    "display_width": DISPLAY_WIDTH,
+                    "display_height": DISPLAY_HEIGHT,
+                    "environment": "browser"
+                }],
+                input=input_content,
+                truncation="auto"
+            )
+
+            print("\tModel processing screenshot")
+        except Exception as e:
+            print(f"Error in API call: {e}")
+            import traceback
+            traceback.print_exc()
+            break
+    
+    if iteration >= max_iterations - 1:
+        print("Reached maximum number of iterations. Stopping.")
+        
+async def main():    
+    # Initialize OpenAI client
+    client = AzureOpenAI(
+        base_url=BASE_URL,
+        azure_ad_token_provider=token_provider,
+        api_version=API_VERSION
+    )
+    
+    # Initialize Playwright
+    async with async_playwright() as playwright:
+        browser = await playwright.chromium.launch(
+            headless=False,
+            args=[f"--window-size={DISPLAY_WIDTH},{DISPLAY_HEIGHT}", "--disable-extensions"]
+        )
+        
+        context = await browser.new_context(
+            viewport={"width": DISPLAY_WIDTH, "height": DISPLAY_HEIGHT},
+            accept_downloads=True
+        )
+        
+        page = await context.new_page()
+        
+        # Navigate to starting page
+        await page.goto("https://www.bing.com", wait_until="domcontentloaded")
+        print("Browser initialized to Bing.com")
+        
+        # Main interaction loop
+        try:
+            while True:
+                print("\n" + "="*50)
+                user_input = input("Enter a task to perform (or 'exit' to quit): ")
+                
+                if user_input.lower() in ('exit', 'quit'):
+                    break
+                
+                if not user_input.strip():
+                    continue
+                
+                # Take initial screenshot
+                screenshot_base64 = await take_screenshot(page)
+                print("\nTake initial screenshot")
+                
+                # Initial request to the model
+                response = client.responses.create(
+                    model=MODEL,
+                    tools=[{
+                        "type": "computer_use_preview",
+                        "display_width": DISPLAY_WIDTH,
+                        "display_height": DISPLAY_HEIGHT,
+                        "environment": "browser"
+                    }],
+                    instructions = "You are an AI agent with the ability to control a browser. You can control the keyboard and mouse. You take a screenshot after each action to check if your action was successful. Once you have completed the requested task you should stop running and pass back control to your human supervisor.",
+                    input=[{
+                        "role": "user",
+                        "content": [{
+                            "type": "input_text",
+                            "text": user_input
+                        }, {
+                            "type": "input_image",
+                            "image_url": f"data:image/png;base64,{screenshot_base64}"
+                        }]
+                    }],
+                    reasoning={"generate_summary": "concise"},
+                    truncation="auto"
+                )
+                print("\nSending model initial screenshot and instructions")
+
+                # Process model actions
+                await process_model_response(client, response, page)
+                
+        except Exception as e:
+            print(f"An error occurred: {e}")
+            import traceback
+            traceback.print_exc()
+        
+        finally:
+            # Close browser
+            await context.close()
+            await browser.close()
+            print("Browser closed.")
+
+if __name__ == "__main__":
+    asyncio.run(main())
+```
+
+
 ## See also
 
 * [Responses API](./responses.md)
     * [Computer Use with playwright](./responses.md#computer-use)
-* [Computer Use Assistant sample on Github](https://github.com/Azure-Samples/computer-use-model)
+* [Computer Use Assistant sample on GitHub](https://github.com/Azure-Samples/computer-use-model)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Playwrightとの統合によるブラウザ操作の自動化"
}
```

### Explanation
この変更は、Azure OpenAIの使用に関する文書（`computer-use.md`）に大規模な改訂をもたらし、Playwrightライブラリを用いたブラウザ操作の自動化機能を新たに追加しています。具体的には、ユーザーがブラウザ内で実施するタスクをAIエージェントに委任できるようにし、AIがキーボードやマウスを制御してブラウザ内のさまざまなアクションを実行できるようにするコード例が紹介されています。

主な変更点には、以下の要素が含まれます：
- **Playwrightの統合**: AIモデルとPlaywrightを使用して、ブラウザ内での基本的な操作を自動化する簡単なスクリプトが追加されました。
- **新たな設定と手順の追加**: Playwrightライブラリのインストール手順、ライブラリのインポート、設定パラメータの定義が含まれています。
- **ユーザー操作の処理**: ユーザーの入力に基づいて自動的にブラウザ操作を行うためのアクションハンドリング機能や、モデルの応答処理に関する詳細なコードセクションが追加されました。
- **安全性チェック**: AIモデルがユーザーの承認を求める安全性チェックを行う機能が実装されており、ユーザーの監視の下で自動化が行われることを強調しています。

この更新により、ユーザーはAIを利用して具体的なブラウザ操作を実行する能力を得るとともに、その操作は常にユーザーがモニタリングし、承認することで安全性が確保されるよう設計されています。この改良は、AIの実用的な活用方法を拡張するものとして、基礎的なテクニカルスキルを持つユーザーに新しい可能性を提供します。

## articles/ai-services/openai/how-to/migration-javascript.md{#item-19dac7}

<details>
<summary>Diff</summary>
````diff
@@ -68,7 +68,7 @@ const client = new AzureOpenAI(options);
 
 The endpoint of the Azure OpenAI resource can be specified by setting the `endpoint` option but it can also be loaded by the client from the environment variable `AZURE_OPENAI_ENDPOINT`. This is the recommended way to set the endpoint because it allows the client to be used in different environments without changing the code and also to protect the endpoint from being exposed in the code.
 
-The API version is required to be specified, this is necessary to ensure that existing code doesn't break between preview API versions. Refer to [API versioning documentation](../api-version-deprecation.md) to learn more about Azure OpenAI API versions. Additionally, the `deployment` property isn't required but it's recommended to be set. Once `deployment` is set, it's used as the default deployment for all operations that require it. If the client isn't created with the `deployment` option, the `model` property in the options object should be set with the deployment name. However, audio operations such as `audio.transcriptions.create` require the client to be created with the `deployment` option set to the deployment name.
+The API version is required to be specified, this is necessary to ensure that existing code doesn't break between preview API versions. Refer to [API versioning documentation](../api-version-lifecycle.md) to learn more about Azure OpenAI API versions. Additionally, the `deployment` property isn't required but it's recommended to be set. Once `deployment` is set, it's used as the default deployment for all operations that require it. If the client isn't created with the `deployment` option, the `model` property in the options object should be set with the deployment name. However, audio operations such as `audio.transcriptions.create` require the client to be created with the `deployment` option set to the deployment name.
 
 # [Azure OpenAI JavaScript (previous)](#tab/javascript-old)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンに関するドキュメントリンクの更新"
}
```

### Explanation
この変更は、Azure OpenAIに関するJavaScriptの移行ガイド文書（`migration-javascript.md`）の軽微な更新を示しています。具体的には、APIバージョンに関連するドキュメントへのリンクが更新されました。

変更の詳細としては、以下の点が挙げられます：
- **APIバージョンのドキュメントリンクの変更**: 以前のリンクが新しいリンク（`../api-version-lifecycle.md`）に置き換えられています。これにより、ユーザーはAPIバージョンについてのライフサイクル情報にアクセスできるようになり、最新の情報を得ることができます。

この更新は、ユーザーがAzure OpenAI APIのバージョンに関する重要な情報を追跡しやすくするためのものであり、ドキュメントの信頼性と有用性が向上します。これにより、開発者はコードが異なるプレビューAPIバージョン間で壊れないよう、より確実にバージョン管理が行えるようになります。

## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -77,14 +77,14 @@ The amount of throughput (measured in tokens per minute or TPM) a deployment get
 
 For example, for `gpt-4.1:2025-04-14`, 1 output token counts as 4 input tokens towards your utilization limit which matches the [pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). Older models use a different ratio and for a deeper understanding on how different ratios of input and output tokens impact the throughput your workload needs, see the [Azure OpenAI capacity calculator](https://ai.azure.com/resource/calculator).
 
-|Topic| **gpt-4.1** | **gpt-4.1-mini** | **o3-mini** | **o1** | **gpt-4o** | **gpt-4o-mini** |
-| --- | --- | --- | --- | --- | --- | --- |
-|Global & data zone provisioned minimum deployment|15|15|15|15|15|15|
-|Global & data zone provisioned scale increment|5|5|5|5|5|5|
-|Regional provisioned minimum deployment|50|25|25|25|50|25|
-|Regional provisioned scale increment|50|25|25|50|50|25|
-|Input TPM per PTU|3,000|14,900|2,500|230|2,500|37,000|
-|Latency Target Value|44 Tokens Per Second|50 Tokens Per Second| 66 Tokens Per Second |25 Tokens Per Second|25 Tokens Per Second|33 Tokens Per Second|
+|Topic| **gpt-4.1** | **gpt-4.1-mini** | **gpt-4.1-nano** | **o3** | **o3-mini** | **o1** | **gpt-4o** | **gpt-4o-mini** |
+| --- | --- |  --- |  --- | --- | --- | --- | --- | --- |
+|Global & data zone provisioned minimum deployment|15|15| 15 | 15 |15|15|15|15|
+|Global & data zone provisioned scale increment|5|5| 5 | 5 |5|5|5|5|
+|Regional provisioned minimum deployment|50|25| 25 |50 | 25|25|50|25|
+|Regional provisioned scale increment|50|25| 25 | 50 | 25|50|50|25|
+|Input TPM per PTU|3,000|14,900| 59,400 | 600 | 2,500|230|2,500|37,000|
+|Latency Target Value|44 Tokens Per Second|50 Tokens Per Second| 50 Tokens Per Second | 40 Tokens Per Second | 66 Tokens Per Second |25 Tokens Per Second|25 Tokens Per Second|33 Tokens Per Second|
 
 
 For a full list, see the [Azure OpenAI in Azure AI Foundry Models in Azure AI Foundry portal calculator](https://ai.azure.com/resource/calculator).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル名の変更とプロビジョニング情報の更新"
}
```

### Explanation
この変更は、Azure OpenAIに関する文書（`provisioned-throughput-onboarding.md`）に対する軽微な更新を示しており、特にモデル名の変更とプロビジョニングに関する情報が改訂されました。

主要な変更点は次のとおりです：
- **モデル名の更新**: 表形式でのモデル名が修正され、新しく `gpt-4.1-nano` 、 `o3` などのモデルが追加されました。
- **プロビジョニング情報の変更**: 各モデルにおけるグローバルおよび地域ごとのプロビジョニングに関する最小デプロイメント、スケール増分、入力TPS（Tokens Per Minute）およびレイテンシターゲット値の数値が更新されました。これにより、各モデルのスループットに対する新しい要件が反映されています。

これらの変更によって、ユーザーは継続的に進化するAzure OpenAIのリソースと、それに伴うプロビジョニングの要件を正確に把握できるようになります。また、性能向上や新しい機能に関する重要な情報を適切に反映させることができ、開発者は最適な設定を利用することが可能です。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -406,10 +406,10 @@ token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
 )
 
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
   azure_ad_token_provider=token_provider,
-  api_version="2025-04-01-preview" # You must use this version or greater to access reasoning summary
+  api_version="preview"
 )
 
 response = client.responses.create(
@@ -427,7 +427,7 @@ print(response.model_dump_json(indent=2))
 # [REST](#tab/REST)
 
 ```bash
-curl -X POST "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/responses?api-version=2025-04-01-preview" \
+curl -X POST "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses?api-version=preview" \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
  -d '{
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クライアント設定とAPIバージョンの更新"
}
```

### Explanation
この変更は、Azure OpenAIに関する文書（`reasoning.md`）の軽微な更新を示しており、クライアントの設定やAPIバージョンに関する情報が修正されました。

主要な変更点は以下の通りです：
- **クライアントの初期化**: `AzureOpenAI`クラスのインスタンス作成時に使用される`azure_endpoint`が`base_url`に変更され、具体的なURL（`https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/`）が設定されています。
- **APIバージョンの変更**: APIバージョンが`"2025-04-01-preview"`から`"preview"`に変更され、より柔軟に最新のAPI機能にアクセスできるようになっています。

これにより、クライアントの設定が最新のAPI仕様に準拠し、開発者は今後のアップデートに対しても容易に対応可能になります。また、文書内の指示が一貫性を持つことで、ユーザーは理解しやすくなります。これらの変更は、よりスムーズな開発体験と最新の機能利用を促進します。

## articles/ai-services/openai/how-to/responses.md{#item-b9757d}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's new stateful Responses API.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 05/19/2025
+ms.date: 05/25/2025
 author: mrbullwinkle    
 ms.author: mbullwin
 ms.custom: references_regions
@@ -19,7 +19,7 @@ The Responses API is a new stateful API from Azure OpenAI. It brings together th
 
 ### API support
 
-`2025-03-01-preview` or later
+- [v1 preview API is required for access to the latest features](../api-version-lifecycle.md#api-evolution)
 
 ### Region Availability
 
@@ -56,11 +56,13 @@ Not every model is available in the regions supported by the responses API. Chec
 > Not currently supported:
 > - The web search tool
 > - Fine-tuned models
->
+> - Image generation via streaming. Coming soon.
+> - Images can't be uploaded as a file and then referenced as input. Coming soon.
+> - There's a known issue with performance when background mode is used with streaming. The issue is expected to be resolved soon. 
 
 ### Reference documentation
 
-- [Responses API reference documentation](/azure/ai-services/openai/reference-preview?#responses-api---create)
+- [Responses API reference documentation](/azure/ai-services/openai/reference-preview-latest?#responses-api---create)
 
 ## Getting started with the responses API
 
@@ -82,18 +84,18 @@ token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
 )
 
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
   azure_ad_token_provider=token_provider,
-  api_version="2025-03-01-preview"
+  api_version="preview"
 )
 
 response = client.responses.create(
-    model="gpt-4o", # replace with your model deployment name 
-    input="This is a test."
-    #truncation="auto" required when using computer-use-preview model.
-
+    model="gpt-4.1-nano",
+    input= "This is a test" 
 )
+
+print(response.model_dump_json(indent=2)) 
 ```
 
 # [Python (API Key)](#tab/python-key)
@@ -102,28 +104,28 @@ response = client.responses.create(
 
 ```python
 import os
-from openai import AzureOpenAI
-
-client = AzureOpenAI(
-    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-    api_version="2025-03-01-preview",
-    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
-    )
+from openai import OpenAI
 
-response = client.responses.create(
-    model="gpt-4o", # replace with your model deployment name 
-    input="This is a test."
-    #truncation="auto" required when using computer-use-preview model.
+client = OpenAI(
+    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
+    base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",
+    default_query={"api-version": "preview"}, 
+)
 
+response = client.responses.create(   
+  model="gpt-4.1-nano", # Replace with your model deployment name 
+  input="This is a test.",
 )
+
+print(response.model_dump_json(indent=2)) 
 ```
 
 # [REST API](#tab/rest-api)
 
 ### Microsoft Entra ID
 
 ```bash
-curl -X POST "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/responses?api-version=2025-03-01-preview" \
+curl -X POST https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses?api-version=preview \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
   -d '{
@@ -135,11 +137,11 @@ curl -X POST "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/responses?api-v
 ### API Key
 
 ```bash
-curl -X POST https://YOUR-RESOURCE-NAME.openai.azure.com/openai/responses?api-version=2025-03-01-preview \
+curl -X POST https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses?api-version=preview \
   -H "Content-Type: application/json" \
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -d '{
-     "model": "gpt-4o",
+     "model": "gpt-4.1-nano",
      "input": "This is a test"
     }'
 ```
@@ -214,10 +216,10 @@ token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
 )
 
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
   azure_ad_token_provider=token_provider,
-  api_version="2025-03-01-preview"
+  api_version="preview"
 )
 
 response = client.responses.retrieve("resp_67cb61fa3a448190bcf2c42d96f0d1a8")
@@ -231,13 +233,13 @@ print(response.model_dump_json(indent=2))
 
 ```python
 import os
-from openai import AzureOpenAI
+from openai import OpenAI
 
-client = AzureOpenAI(
-    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-    api_version="2025-03-01-preview",
-    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
-    )
+client = OpenAI(
+    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
+    base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",
+    default_query={"api-version": "preview"}, 
+)
 
 response = client.responses.retrieve("resp_67cb61fa3a448190bcf2c42d96f0d1a8")
 ```
@@ -247,15 +249,15 @@ response = client.responses.retrieve("resp_67cb61fa3a448190bcf2c42d96f0d1a8")
 ### Microsoft Entra ID
 
 ```bash
-curl -X GET "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/responses/{response_id}?api-version=2025-03-01-preview" \
+curl -X GET https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses/{response_id}?api-version=preview \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" 
 ```
 
 ### API Key
 
 ```bash
-curl -X GET https://YOUR-RESOURCE-NAME.openai.azure.com/openai/responses/{response_id}?api-version=2025-03-01-preview \
+curl -X GET https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses/{response_id}?api-version=preview \
   -H "Content-Type: application/json" \
   -H "api-key: $AZURE_OPENAI_API_KEY" 
 ```
@@ -325,10 +327,10 @@ token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
 )
 
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
   azure_ad_token_provider=token_provider,
-  api_version="2025-03-01-preview"
+  api_version="preview"
 )
 
 response = client.responses.delete("resp_67cb61fa3a448190bcf2c42d96f0d1a8")
@@ -348,10 +350,10 @@ token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
 )
 
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
   azure_ad_token_provider=token_provider,
-  api_version="2025-03-01-preview"
+  api_version="preview"
 )
 
 response = client.responses.create(
@@ -432,10 +434,10 @@ token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
 )
 
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
   azure_ad_token_provider=token_provider,
-  api_version="2025-03-01-preview"
+  api_version="preview"
 )
 
 
@@ -469,10 +471,10 @@ token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
 )
 
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
-  azure_ad_token_provider = token_provider,
-  api_version = "2025-04-01-preview" 
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
+  azure_ad_token_provider=token_provider,
+  api_version="preview"
 )
 
 response = client.responses.create(
@@ -500,10 +502,10 @@ token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
 )
 
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
   azure_ad_token_provider=token_provider,
-  api_version="2025-03-01-preview"
+  api_version="preview"
 )
 
 response = client.responses.create(  
@@ -564,10 +566,10 @@ token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
 )
 
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
   azure_ad_token_provider=token_provider,
-  api_version="2025-03-01-preview"
+  api_version="preview"
 )
 
 response = client.responses.input_items.list("resp_67d856fcfba0819081fd3cffee2aa1c0")
@@ -612,10 +614,10 @@ token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
 )
 
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
   azure_ad_token_provider=token_provider,
-  api_version="2025-03-01-preview"
+  api_version="preview"
 )
 
 response = client.responses.create(
@@ -649,10 +651,10 @@ token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
 )
 
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
   azure_ad_token_provider=token_provider,
-  api_version="2025-03-01-preview"
+  api_version="preview"
 )
 
 def encode_image(image_path):
@@ -684,837 +686,611 @@ response = client.responses.create(
 print(response)
 ```
 
-## Reasoning models
+## Using remote MCP servers
 
-For examples of how to use reasoning models with the responses API see the [reasoning models guide](./reasoning.md#reasoning-summary).
+You can extend the capabilities of your model by connecting it to tools hosted on remote Model Context Protocol (MCP) servers. These servers are maintained by developers and organizations and expose tools that can be accessed by MCP-compatible clients, such as the Responses API.
 
-## Computer use
+[Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) is an open standard that defines how applications provide tools and contextual data to large language models (LLMs). It enables consistent, scalable integration of external tools into model workflows.
 
-In this section, we provide a simple example script that integrates Azure OpenAI's `computer-use-preview` model with [Playwright](https://playwright.dev/) to automate basic browser interactions. Combining the model with [Playwright](https://playwright.dev/) allows the model to see the browser screen, make decisions, and perform actions like clicking, typing, and navigating websites. You should exercise caution when running this example code. This code is designed to be run locally but should only be executed in a test environment. Use a human to confirm decisions and don't give the model access to sensitive data.
+The following example demonstrates how to use the fictitious MCP server to query information about the Azure REST API. This allows the model to retrieve and reason over repository content in real time.
 
-:::image type="content" source="../media/computer-use-preview.gif" alt-text="Animated gif of computer-use-preview model integrated with playwright." lightbox="../media/computer-use-preview.gif":::
+```bash
+curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses?api-version=preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+  -d '{
+  "model": "gpt-4.1",
+  "tools": [
+    {
+      "type": "mcp",
+      "server_label": "github",
+      "server_url": "https://contoso.com/Azure/azure-rest-api-specs",
+      "require_approval": "never"
+    }
+  ],
+  "input": "What is this repo in 100 words?"
+}'
+```
 
-First you'll need to install the Python library for [Playwright](https://playwright.dev/).
+```python
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
 
-```cmd
-pip install playwright
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
+  azure_ad_token_provider=token_provider,
+  api_version="preview"
+)
+
+response = client.responses.create(
+    model="gpt-4.1", # replace with your model deployment name 
+    tools=[
+        {
+            "type": "mcp",
+            "server_label": "github",
+            "server_url": "https://contoso.com/Azure/azure-rest-api-specs",
+            "require_approval": "never"
+        },
+    ],
+    input="What transport protocols are supported in the 2025-03-26 version of the MCP spec?",
+)
+
+print(response.output_text)
 ```
 
-Once the package is installed, you'll also need to run
+The MCP tool works only in the Responses API, and is available across all newer models (gpt-4o, gpt-4.1, and our reasoning models). When you're using the MCP tool, you only pay for tokens used when importing tool definitions or making tool calls—there are no additional fees involved.
 
-```cmd
-playwright install
+### Approvals
+
+By default, the Responses API requires explicit approval before any data is shared with a remote MCP server. This approval step helps ensure transparency and gives you control over what information is sent externally.
+
+We recommend reviewing all data being shared with remote MCP servers and optionally logging it for auditing purposes.
+
+When an approval is required, the model returns a `mcp_approval_request` item in the response output. This object contains the details of the pending request and allows you to inspect or modify the data before proceeding.
+
+```json
+{
+  "id": "mcpr_682bd9cd428c8198b170dc6b549d66fc016e86a03f4cc828",
+  "type": "mcp_approval_request",
+  "arguments": {},
+  "name": "fetch_azure_rest_api_docs",
+  "server_label": "github"
+}
 ```
 
-### Imports and configuration
+To proceed with the remote MCP call, you must respond to the approval request by creating a new response object that includes an mcp_approval_response item. This object confirms your intent to allow the model to send the specified data to the remote MCP server.
 
-First, we import the necessary libraries and define our configuration parameters. Since we're using `asyncio` we'll be executing this code outside of Jupyter notebooks. We'll walk through the code first in chunks and then demonstrate how to use it.
+```bash
+curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses?api-version=preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+  -d '{
+  "model": "gpt-4.1",
+  "tools": [
+    {
+      "type": "mcp",
+      "server_label": "github",
+      "server_url": "https://contoso.com/Azure/azure-rest-api-specs",
+      "require_approval": "never"
+    }
+  ],
+  "previous_response_id": "resp_682f750c5f9c8198aee5b480980b5cf60351aee697a7cd77",
+  "input": [{
+    "type": "mcp_approval_response",
+    "approve": true,
+    "approval_request_id": "mcpr_682bd9cd428c8198b170dc6b549d66fc016e86a03f4cc828"
+  }]
+}'
+```
 
 ```python
-import os
-import asyncio
-import base64
 from openai import AzureOpenAI
 from azure.identity import DefaultAzureCredential, get_bearer_token_provider
-from playwright.async_api import async_playwright, TimeoutError
 
 token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
 )
 
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
+  azure_ad_token_provider=token_provider,
+  api_version="preview"
+)
 
-# Configuration
-
-AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
-MODEL = "computer-use-preview" # Set to model deployment name
-DISPLAY_WIDTH = 1024
-DISPLAY_HEIGHT = 768
-API_VERSION = "2025-03-01-preview" #Use this API version or later
-ITERATIONS = 5 # Max number of iterations before returning control to human supervisor
+response = client.responses.create(
+    model="gpt-4.1", # replace with your model deployment name 
+    tools=[
+        {
+            "type": "mcp",
+            "server_label": "github",
+            "server_url": "https://contoso.com/Azure/azure-rest-api-specs",
+            "require_approval": "never"
+        },
+    ],
+    previous_response_id="resp_682f750c5f9c8198aee5b480980b5cf60351aee697a7cd77",
+    input=[{
+        "type": "mcp_approval_response",
+        "approve": True,
+        "approval_request_id": "mcpr_682bd9cd428c8198b170dc6b549d66fc016e86a03f4cc828"
+    }],
+)
 ```
 
-### Key mapping for browser interaction
+### Authentication
 
-Next, we set up mappings for special keys that the model might need to pass to Playwright. Ultimately the model is never performing actions itself, it passes representations of commands and you have to provide the final integration layer that can take those commands and execute them in your chosen environment.
+Unlike the GitHub MCP server, most remote MCP servers require authentication. The MCP tool in the Responses API supports custom headers, allowing you to securely connect to these servers using the authentication scheme they require.
 
-This isn't an exhaustive list of possible key mappings. You can expand this list as needed. This dictionary is specific to integrating the model with Playwright. If you were integrating the model with an alternate library to provide API access to your operating systems keyboard/mouse you would need to provide a mapping specific to that library.
+You can specify headers such as API keys, OAuth access tokens, or other credentials directly in your request. The most commonly used header is the `Authorization` header.
+
+```bash
+curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses?api-version=preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+  -d '{
+        "model": "gpt-4.1",
+        "input": "What is this repo in 100 words?"
+        "tools": [
+            {
+                "type": "mcp",
+                "server_label": "github",
+                "server_url": "https://contoso.com/Azure/azure-rest-api-specs",
+                "headers": {
+                    "Authorization": "Bearer $YOUR_API_KEY"
+            }
+        ]
+    }'
+```
 
 ```python
-# Key mapping for special keys in Playwright
-KEY_MAPPING = {
-    "/": "Slash", "\\": "Backslash", "alt": "Alt", "arrowdown": "ArrowDown",
-    "arrowleft": "ArrowLeft", "arrowright": "ArrowRight", "arrowup": "ArrowUp",
-    "backspace": "Backspace", "ctrl": "Control", "delete": "Delete", 
-    "enter": "Enter", "esc": "Escape", "shift": "Shift", "space": " ",
-    "tab": "Tab", "win": "Meta", "cmd": "Meta", "super": "Meta", "option": "Alt"
-}
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
+  azure_ad_token_provider=token_provider,
+  api_version="preview"
+)
+
+response = client.responses.create(
+    model="gpt-4.1",
+    input="What is this repo in 100 words?",
+    tools=[
+        {
+            "type": "mcp",
+            "server_label": "github",
+            "server_url": "https://gitmcp.io/Azure/azure-rest-api-specs",
+            "headers": {
+                "Authorization": "Bearer $YOUR_API_KEY"
+        }
+    ]
+)
+
+print(response.output_text)
 ```
 
-This dictionary translates user-friendly key names to the format expected by Playwright's keyboard API.
+## Background tasks
+
+Background mode allows you to run long-running tasks asynchronously using models like o3 and o1-pro. This is especially useful for complex reasoning tasks that may take several minutes to complete, such as those handled by agents like Codex or Deep Research.
 
-### Coordinate validation function
+By enabling background mode, you can avoid timeouts and maintain reliability during extended operations. When a request is sent with `"background": true`, the task is processed asynchronously, and you can poll for its status over time.
 
-To make sure that any mouse actions that are passed from the model stay within the browser window boundaries we'll add the following utility function:
+To start a background task, set the background parameter to true in your request:
+
+```bash
+curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses?api-version=preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+  -d '{
+    "model": "o3",
+    "input": "Write me a very long story",
+    "background": true
+  }'
+```
 
 ```python
-def validate_coordinates(x, y):
-    """Ensure coordinates are within display bounds."""
-    return max(0, min(x, DISPLAY_WIDTH)), max(0, min(y, DISPLAY_HEIGHT))
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
+  azure_ad_token_provider=token_provider,
+  api_version="preview"
+)
+
+response = client.responses.create(
+    model = "o3",
+    input = "Write me a very long story",
+    background = True
+)
+
+print(response.status)
+```
+
+Use the `GET` endpoint to check the status of a background response. Continue polling while the status is queued or in_progress. Once the response reaches a final (terminal) state, it will be available for retrieval.
+
+```bash
+curl GET https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses/resp_1234567890?api-version=preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN"
 ```
 
-This simple utility attempts to prevent out-of-bounds errors by clamping coordinates to the window dimensions.
+```python
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
+  azure_ad_token_provider=token_provider,
+  api_version="preview"
+)
 
-### Action handling
+response = client.responses.create(
+    model = "o3",
+    input = "Write me a very long story",
+    background = True
+)
 
-The core of our browser automation is the action handler that processes various types of user interactions and convert them into actions within the browser.
+while response.status in {"queued", "in_progress"}:
+    print(f"Current status: {resp.status}")
+    sleep(2)
+    response = client.responses.retrieve(response.id)
+
+print(f"Final status: {response.status}\nOutput:\n{response.output_text}")
+```
+
+You can cancel an in-progress background task using the cancel endpoint. Canceling is idempotent—subsequent calls will return the final response object.
+
+```bash
+curl -X POST https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses/resp_1234567890/cancel?api-version=preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN"
+```
 
 ```python
-async def handle_action(page, action):
-    """Handle different action types from the model."""
-    action_type = action.type
-    
-    if action_type == "drag":
-        print("Drag action is not supported in this implementation. Skipping.")
-        return
-        
-    elif action_type == "click":
-        button = getattr(action, "button", "left")
-        # Validate coordinates
-        x, y = validate_coordinates(action.x, action.y)
-        
-        print(f"\tAction: click at ({x}, {y}) with button '{button}'")
-        
-        if button == "back":
-            await page.go_back()
-        elif button == "forward":
-            await page.go_forward()
-        elif button == "wheel":
-            await page.mouse.wheel(x, y)
-        else:
-            button_type = {"left": "left", "right": "right", "middle": "middle"}.get(button, "left")
-            await page.mouse.click(x, y, button=button_type)
-            try:
-                await page.wait_for_load_state("domcontentloaded", timeout=3000)
-            except TimeoutError:
-                pass
-        
-    elif action_type == "double_click":
-        # Validate coordinates
-        x, y = validate_coordinates(action.x, action.y)
-        
-        print(f"\tAction: double click at ({x}, {y})")
-        await page.mouse.dblclick(x, y)
-        
-    elif action_type == "scroll":
-        scroll_x = getattr(action, "scroll_x", 0)
-        scroll_y = getattr(action, "scroll_y", 0)
-        # Validate coordinates
-        x, y = validate_coordinates(action.x, action.y)
-        
-        print(f"\tAction: scroll at ({x}, {y}) with offsets ({scroll_x}, {scroll_y})")
-        await page.mouse.move(x, y)
-        await page.evaluate(f"window.scrollBy({{left: {scroll_x}, top: {scroll_y}, behavior: 'smooth'}});")
-        
-    elif action_type == "keypress":
-        keys = getattr(action, "keys", [])
-        print(f"\tAction: keypress {keys}")
-        mapped_keys = [KEY_MAPPING.get(key.lower(), key) for key in keys]
-        
-        if len(mapped_keys) > 1:
-            # For key combinations (like Ctrl+C)
-            for key in mapped_keys:
-                await page.keyboard.down(key)
-            await asyncio.sleep(0.1)
-            for key in reversed(mapped_keys):
-                await page.keyboard.up(key)
-        else:
-            for key in mapped_keys:
-                await page.keyboard.press(key)
-                
-    elif action_type == "type":
-        text = getattr(action, "text", "")
-        print(f"\tAction: type text: {text}")
-        await page.keyboard.type(text, delay=20)
-        
-    elif action_type == "wait":
-        ms = getattr(action, "ms", 1000)
-        print(f"\tAction: wait {ms}ms")
-        await asyncio.sleep(ms / 1000)
-        
-    elif action_type == "screenshot":
-        print("\tAction: screenshot")
-        
-    else:
-        print(f"\tUnrecognized action: {action_type}")
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
+  azure_ad_token_provider=token_provider,
+  api_version="preview"
+)
+
+response = client.responses.cancel("resp_1234567890")
+
+print(response.status)
 ```
 
-This function attempts to handle various types of actions. We need to translate between the commands that the `computer-use-preview` will generate and the Playwright library which will execute the actions. For more information refer to the reference documentation for `ComputerAction`.
+### Stream a background response
 
-- [Click](/azure/ai-services/openai/reference-preview#click)
-- [DoubleClick](/azure/ai-services/openai/reference-preview#doubleclick)
-- [Drag](/azure/ai-services/openai/reference-preview#drag)
-- [KeyPress](/azure/ai-services/openai/reference-preview#keypress)
-- [Move](/azure/ai-services/openai/reference-preview#move)
-- [Screenshot](/azure/ai-services/openai/reference-preview#screenshot)
-- [Scroll](/azure/ai-services/openai/reference-preview#scroll)
-- [Type](/azure/ai-services/openai/reference-preview#type)
-- [Wait](/azure/ai-services/openai/reference-preview#wait)
+To stream a background response, set both `background` and `stream` to true. This is useful if you want to resume streaming later in case of a dropped connection. Use the sequence_number from each event to track your position.
 
-### Screenshot capture
+```bash
+curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses?api-version=preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+  -d '{
+    "model": "o3",
+    "input": "Write me a very long story",
+    "background": true,
+    "stream": true
+  }'
 
-In order for the model to be able to see what it's interacting with the model needs a way to capture screenshots. For this code we're using Playwright to capture the screenshots and we're limiting the view to just the content in the browser window. The screenshot won't include the url bar or other aspects of the browser GUI. If you need the model to see outside the main browser window you could augment the model by creating your own screenshot function. 
+```
 
 ```python
-async def take_screenshot(page):
-    """Take a screenshot and return base64 encoding with caching for failures."""
-    global last_successful_screenshot
-    
-    try:
-        screenshot_bytes = await page.screenshot(full_page=False)
-        last_successful_screenshot = base64.b64encode(screenshot_bytes).decode("utf-8")
-        return last_successful_screenshot
-    except Exception as e:
-        print(f"Screenshot failed: {e}")
-        print(f"Using cached screenshot from previous successful capture")
-        if last_successful_screenshot:
-            return last_successful_screenshot
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
+  azure_ad_token_provider=token_provider,
+  api_version="preview"
+)
+
+# Fire off an async response but also start streaming immediately
+stream = client.responses.create(
+    model="o3",
+    input="Write me a very long story",
+    background=True,
+    stream=True,
+)
+
+cursor = None
+for event in stream:
+    print(event)
+    cursor = event["sequence_number"]
 ```
 
-This function captures the current browser state as an image and returns it as a base64-encoded string, ready to be sent to the model. We'll constantly do this in a loop after each step allowing the model to see if the command it tried to execute was successful or not, which then allows it to adjust based on the contents of the screenshot. We could let the model decide if it needs to take a screenshot, but for simplicity we will force a screenshot to be taken for each iteration.
+> [!NOTE] 
+> Background responses currently have a higher time-to-first-token latency than synchronous responses. Improvements are underway to reduce this gap.
 
-### Model response processing
+### Limitations
 
-This function processes the model's responses and executes the requested actions:
+* Background mode requires `store=true`. Stateless requests are not supported.
+* You can only resume streaming if the original request included `stream=true`.
+* To cancel a synchronous response, terminate the connection directly.
 
-```python
-async def process_model_response(client, response, page, max_iterations=ITERATIONS):
-    """Process the model's response and execute actions."""
-    for iteration in range(max_iterations):
-        if not hasattr(response, 'output') or not response.output:
-            print("No output from model.")
-            break
-        
-        # Safely access response id
-        response_id = getattr(response, 'id', 'unknown')
-        print(f"\nIteration {iteration + 1} - Response ID: {response_id}\n")
-        
-        # Print text responses and reasoning
-        for item in response.output:
-            # Handle text output
-            if hasattr(item, 'type') and item.type == "text":
-                print(f"\nModel message: {item.text}\n")
-                
-            # Handle reasoning output
-            if hasattr(item, 'type') and item.type == "reasoning":
-                # Extract meaningful content from the reasoning
-                meaningful_content = []
-                
-                if hasattr(item, 'summary') and item.summary:
-                    for summary in item.summary:
-                        # Handle different potential formats of summary content
-                        if isinstance(summary, str) and summary.strip():
-                            meaningful_content.append(summary)
-                        elif hasattr(summary, 'text') and summary.text.strip():
-                            meaningful_content.append(summary.text)
-                
-                # Only print reasoning section if there's actual content
-                if meaningful_content:
-                    print("=== Model Reasoning ===")
-                    for idx, content in enumerate(meaningful_content, 1):
-                        print(f"{content}")
-                    print("=====================\n")
-        
-        # Extract computer calls
-        computer_calls = [item for item in response.output 
-                         if hasattr(item, 'type') and item.type == "computer_call"]
-        
-        if not computer_calls:
-            print("No computer call found in response. Reverting control to human operator")
-            break
-        
-        computer_call = computer_calls[0]
-        if not hasattr(computer_call, 'call_id') or not hasattr(computer_call, 'action'):
-            print("Computer call is missing required attributes.")
-            break
-        
-        call_id = computer_call.call_id
-        action = computer_call.action
-        
-        # Handle safety checks
-        acknowledged_checks = []
-        if hasattr(computer_call, 'pending_safety_checks') and computer_call.pending_safety_checks:
-            pending_checks = computer_call.pending_safety_checks
-            print("\nSafety checks required:")
-            for check in pending_checks:
-                print(f"- {check.code}: {check.message}")
-            
-            if input("\nDo you want to proceed? (y/n): ").lower() != 'y':
-                print("Operation cancelled by user.")
-                break
-            
-            acknowledged_checks = pending_checks
-        
-        # Execute the action
-        try:
-           await page.bring_to_front()
-           await handle_action(page, action)
-           
-           # Check if a new page was created after the action
-           if action.type in ["click"]:
-               await asyncio.sleep(1.5)
-               # Get all pages in the context
-               all_pages = page.context.pages
-               # If we have multiple pages, check if there's a newer one
-               if len(all_pages) > 1:
-                   newest_page = all_pages[-1]  # Last page is usually the newest
-                   if newest_page != page and newest_page.url not in ["about:blank", ""]:
-                       print(f"\tSwitching to new tab: {newest_page.url}")
-                       page = newest_page  # Update our page reference
-           elif action.type != "wait":
-               await asyncio.sleep(0.5)
-               
-        except Exception as e:
-           print(f"Error handling action {action.type}: {e}")
-           import traceback
-           traceback.print_exc()    
-
-        # Take a screenshot after the action
-        screenshot_base64 = await take_screenshot(page)
-
-        print("\tNew screenshot taken")
-        
-        # Prepare input for the next request
-        input_content = [{
-            "type": "computer_call_output",
-            "call_id": call_id,
-            "output": {
-                "type": "input_image",
-                "image_url": f"data:image/png;base64,{screenshot_base64}"
-            }
-        }]
-        
-        # Add acknowledged safety checks if any
-        if acknowledged_checks:
-            acknowledged_checks_dicts = []
-            for check in acknowledged_checks:
-                acknowledged_checks_dicts.append({
-                    "id": check.id,
-                    "code": check.code,
-                    "message": check.message
-                })
-            input_content[0]["acknowledged_safety_checks"] = acknowledged_checks_dicts
-        
-        # Add current URL for context
-        try:
-            current_url = page.url
-            if current_url and current_url != "about:blank":
-                input_content[0]["current_url"] = current_url
-                print(f"\tCurrent URL: {current_url}")
-        except Exception as e:
-            print(f"Error getting URL: {e}")
-        
-        # Send the screenshot back for the next step
-        try:
-            response = client.responses.create(
-                model=MODEL,
-                previous_response_id=response_id,
-                tools=[{
-                    "type": "computer_use_preview",
-                    "display_width": DISPLAY_WIDTH,
-                    "display_height": DISPLAY_HEIGHT,
-                    "environment": "browser"
-                }],
-                input=input_content,
-                truncation="auto"
-            )
-
-            print("\tModel processing screenshot")
-        except Exception as e:
-            print(f"Error in API call: {e}")
-            import traceback
-            traceback.print_exc()
-            break
-    
-    if iteration >= max_iterations - 1:
-        print("Reached maximum number of iterations. Stopping.")
+### Resume streaming from a specific point
+
+```bash
+curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses/resp_1234567890?stream=true&starting_after=42&api-version=2025-04-01-preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN"
 ```
 
-In this section we have added code that:
+## Encrypted Reasoning Items
 
-- Extracts and displays text and reasoning from the model.
-- Processes computer action calls.
-- Handles potential safety checks requiring user confirmation.
-- Executes the requested action.
-- Captures a new screenshot.
-- Sends the updated state back to the model and defines the [`ComputerTool`](/azure/ai-services/openai/reference-preview#computertool).
-- Repeats this process for multiple iterations.
+When using the Responses API in stateless mode — either by setting `store` to false or when your organization is enrolled in zero data retention — you must still preserve reasoning context across conversation turns. To do this, include encrypted reasoning items in your API requests.
 
-### Main function
+To retain reasoning items across turns, add `reasoning.encrypted_content` to the `include` parameter in your request. This ensures that the response includes an encrypted version of the reasoning trace, which can be passed along in future requests.
+
+```bash
+curl https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses?api-version=preview \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+  -d '{
+    "model": "o4-mini",
+    "reasoning": {"effort": "medium"},
+    "input": "What is the weather like today?",
+    "tools": [<YOUR_FUNCTION GOES HERE>],
+    "include": ["reasoning.encrypted_content"]
+  }'
+```
+
+## Image generation
+
+The Responses API enables image generation as part of conversations and multi-step workflows. It supports image inputs and outputs within context and includes built-in tools for generating and editing images.
+
+Compared to the standalone Image API, the Responses API offers several advantages:
+
+* **Multi-turn editing**: Iteratively refine and edit images using natural language prompts.
+* **Streaming**: Display partial image outputs during generation to improve perceived latency.
+* **Flexible inputs**: Accept image File IDs as inputs, in addition to raw image bytes.
+
+> [!NOTE]
+> The image generation tool in the Responses API is only supported by the `gpt-image-1` model. You can however call this model from this list of supported models - `gpt-4o`, `gpt-4o-mini`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `o3`.
+
+Use the Responses API if you want to:
+
+* Build conversational image experiences with GPT Image.
+* Enable iterative image editing through multi-turn prompts.
+* Stream partial image results during generation for a smoother user experience.
+
+Generate an image
 
-The main function coordinates the entire process:
 
 ```python
-    # Initialize OpenAI client
-    client = AzureOpenAI(
-        azure_endpoint=AZURE_ENDPOINT,
-        azure_ad_token_provider=token_provider,
-        api_version=API_VERSION
-    )
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
+  azure_ad_token_provider=token_provider,
+  api_version="preview",
+  default_headers={"x-ms-oai-image-generation-deployment":"YOUR-GPT-IMAGE1-DEPLOYMENT-NAME"}
+)
+
+response = client.responses.create(
+    model="o3",
+    input="Generate an image of gray tabby cat hugging an otter with an orange scarf",
+    tools=[{"type": "image_generation"}],
+)
+
+# Save the image to a file
+image_data = [
+    output.result
+    for output in response.output
+    if output.type == "image_generation_call"
+]
     
-    # Initialize Playwright
-    async with async_playwright() as playwright:
-        browser = await playwright.chromium.launch(
-            headless=False,
-            args=[f"--window-size={DISPLAY_WIDTH},{DISPLAY_HEIGHT}", "--disable-extensions"]
-        )
-        
-        context = await browser.new_context(
-            viewport={"width": DISPLAY_WIDTH, "height": DISPLAY_HEIGHT},
-            accept_downloads=True
-        )
-        
-        page = await context.new_page()
-        
-        # Navigate to starting page
-        await page.goto("https://www.bing.com", wait_until="domcontentloaded")
-        print("Browser initialized to Bing.com")
-        
-        # Main interaction loop
-        try:
-            while True:
-                print("\n" + "="*50)
-                user_input = input("Enter a task to perform (or 'exit' to quit): ")
-                
-                if user_input.lower() in ('exit', 'quit'):
-                    break
-                
-                if not user_input.strip():
-                    continue
-                
-                # Take initial screenshot
-                screenshot_base64 = await take_screenshot(page)
-                print("\nTake initial screenshot")
-                
-                # Initial request to the model
-                response = client.responses.create(
-                    model=MODEL,
-                    tools=[{
-                        "type": "computer_use_preview",
-                        "display_width": DISPLAY_WIDTH,
-                        "display_height": DISPLAY_HEIGHT,
-                        "environment": "browser"
-                    }],
-                    instructions = "You are an AI agent with the ability to control a browser. You can control the keyboard and mouse. You take a screenshot after each action to check if your action was successful. Once you have completed the requested task you should stop running and pass back control to your human operator.",
-                    input=[{
-                        "role": "user",
-                        "content": [{
-                            "type": "input_text",
-                            "text": user_input
-                        }, {
-                            "type": "input_image",
-                            "image_url": f"data:image/png;base64,{screenshot_base64}"
-                        }]
-                    }],
-                    reasoning={"generate_summary": "concise"},
-                    truncation="auto"
-                )
-                print("\nSending model initial screenshot and instructions")
-
-                # Process model actions
-                await process_model_response(client, response, page)
-                
-        except Exception as e:
-            print(f"An error occurred: {e}")
-            import traceback
-            traceback.print_exc()
-        
-        finally:
-            # Close browser
-            await context.close()
-            await browser.close()
-            print("Browser closed.")
-
-if __name__ == "__main__":
-    asyncio.run(main())
+if image_data:
+    image_base64 = image_data[0]
+    with open("otter.png", "wb") as f:
+        f.write(base64.b64decode(image_base64))
 ```
 
-The main function:
+You can perform multi-turn image generation by using the output of image generation in subsequent calls or just using the `1previous_response_id`.
 
-- Initializes the AzureOpenAI client.
-- Sets up the Playwright browser.
-- Starts at Bing.com.
-- Enters a loop to accept user tasks.
-- Captures the initial state.
-- Sends the task and screenshot to the model.
-- Processes the model's response.
-- Repeats until the user exits.
-- Ensures the browser is properly closed.
+```python
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
 
-### Complete script
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
+  azure_ad_token_provider=token_provider,
+  api_version="preview",
+  default_headers={"x-ms-oai-image-generation-deployment":"YOUR-GPT-IMAGE1-DEPLOYMENT-NAME"}
+)
 
-> [!CAUTION]
-> This code is experimental and for demonstration purposes only. It's only intended to illustrate the basic flow of the responses API and the `computer-use-preview` model. While you can execute this code on your local computer, we strongly recommend running this code on a low privilege virtual machine with no access to sensitive data. This code is for basic testing purposes only.
+image_data = [
+    output.result
+    for output in response.output
+    if output.type == "image_generation_call"
+]
+
+if image_data:
+    image_base64 = image_data[0]
+
+    with open("cat_and_otter.png", "wb") as f:
+        f.write(base64.b64decode(image_base64))
+
+
+# Follow up
+
+response_followup = client.responses.create(
+    model="gpt-4.1-mini",
+    previous_response_id=response.id,
+    input="Now make it look realistic",
+    tools=[{"type": "image_generation"}],
+)
+
+image_data_followup = [
+    output.result
+    for output in response_followup.output
+    if output.type == "image_generation_call"
+]
+
+if image_data_followup:
+    image_base64 = image_data_followup[0]
+    with open("cat_and_otter_realistic.png", "wb") as f:
+        f.write(base64.b64decode(image_base64))
+```
+
+### Streaming
+
+You can stream partial images using Responses API. The `partial_images` can be used to receive 1-3 partial images
 
 ```python
-import os
-import asyncio
-import base64
 from openai import AzureOpenAI
 from azure.identity import DefaultAzureCredential, get_bearer_token_provider
-from playwright.async_api import async_playwright, TimeoutError
-
 
 token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
 )
 
-# Configuration
-
-AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
-MODEL = "computer-use-preview"
-DISPLAY_WIDTH = 1024
-DISPLAY_HEIGHT = 768
-API_VERSION = "2025-03-01-preview"
-ITERATIONS = 5 # Max number of iterations before forcing the model to return control to the human supervisor
-
-# Key mapping for special keys in Playwright
-KEY_MAPPING = {
-    "/": "Slash", "\\": "Backslash", "alt": "Alt", "arrowdown": "ArrowDown",
-    "arrowleft": "ArrowLeft", "arrowright": "ArrowRight", "arrowup": "ArrowUp",
-    "backspace": "Backspace", "ctrl": "Control", "delete": "Delete", 
-    "enter": "Enter", "esc": "Escape", "shift": "Shift", "space": " ",
-    "tab": "Tab", "win": "Meta", "cmd": "Meta", "super": "Meta", "option": "Alt"
-}
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
+  azure_ad_token_provider=token_provider,
+  api_version="preview",
+  default_headers={"x-ms-oai-image-generation-deployment":"YOUR-GPT-IMAGE1-DEPLOYMENT-NAME"}
+)
 
-def validate_coordinates(x, y):
-    """Ensure coordinates are within display bounds."""
-    return max(0, min(x, DISPLAY_WIDTH)), max(0, min(y, DISPLAY_HEIGHT))
+stream = client.responses.create(
+    model="gpt-4.1",
+    input="Draw a gorgeous image of a river made of white owl feathers, snaking its way through a serene winter landscape",
+    stream=True,
+    tools=[{"type": "image_generation", "partial_images": 2}],
+)
 
-async def handle_action(page, action):
-    """Handle different action types from the model."""
-    action_type = action.type
-    
-    if action_type == "drag":
-        print("Drag action is not supported in this implementation. Skipping.")
-        return
-        
-    elif action_type == "click":
-        button = getattr(action, "button", "left")
-        # Validate coordinates
-        x, y = validate_coordinates(action.x, action.y)
-        
-        print(f"\tAction: click at ({x}, {y}) with button '{button}'")
-        
-        if button == "back":
-            await page.go_back()
-        elif button == "forward":
-            await page.go_forward()
-        elif button == "wheel":
-            await page.mouse.wheel(x, y)
-        else:
-            button_type = {"left": "left", "right": "right", "middle": "middle"}.get(button, "left")
-            await page.mouse.click(x, y, button=button_type)
-            try:
-                await page.wait_for_load_state("domcontentloaded", timeout=3000)
-            except TimeoutError:
-                pass
-        
-    elif action_type == "double_click":
-        # Validate coordinates
-        x, y = validate_coordinates(action.x, action.y)
-        
-        print(f"\tAction: double click at ({x}, {y})")
-        await page.mouse.dblclick(x, y)
-        
-    elif action_type == "scroll":
-        scroll_x = getattr(action, "scroll_x", 0)
-        scroll_y = getattr(action, "scroll_y", 0)
-        # Validate coordinates
-        x, y = validate_coordinates(action.x, action.y)
-        
-        print(f"\tAction: scroll at ({x}, {y}) with offsets ({scroll_x}, {scroll_y})")
-        await page.mouse.move(x, y)
-        await page.evaluate(f"window.scrollBy({{left: {scroll_x}, top: {scroll_y}, behavior: 'smooth'}});")
-        
-    elif action_type == "keypress":
-        keys = getattr(action, "keys", [])
-        print(f"\tAction: keypress {keys}")
-        mapped_keys = [KEY_MAPPING.get(key.lower(), key) for key in keys]
-        
-        if len(mapped_keys) > 1:
-            # For key combinations (like Ctrl+C)
-            for key in mapped_keys:
-                await page.keyboard.down(key)
-            await asyncio.sleep(0.1)
-            for key in reversed(mapped_keys):
-                await page.keyboard.up(key)
-        else:
-            for key in mapped_keys:
-                await page.keyboard.press(key)
-                
-    elif action_type == "type":
-        text = getattr(action, "text", "")
-        print(f"\tAction: type text: {text}")
-        await page.keyboard.type(text, delay=20)
-        
-    elif action_type == "wait":
-        ms = getattr(action, "ms", 1000)
-        print(f"\tAction: wait {ms}ms")
-        await asyncio.sleep(ms / 1000)
-        
-    elif action_type == "screenshot":
-        print("\tAction: screenshot")
-        
-    else:
-        print(f"\tUnrecognized action: {action_type}")
-
-async def take_screenshot(page):
-    """Take a screenshot and return base64 encoding with caching for failures."""
-    global last_successful_screenshot
-    
-    try:
-        screenshot_bytes = await page.screenshot(full_page=False)
-        last_successful_screenshot = base64.b64encode(screenshot_bytes).decode("utf-8")
-        return last_successful_screenshot
-    except Exception as e:
-        print(f"Screenshot failed: {e}")
-        print(f"Using cached screenshot from previous successful capture")
-        if last_successful_screenshot:
-            return last_successful_screenshot
-
-
-async def process_model_response(client, response, page, max_iterations=ITERATIONS):
-    """Process the model's response and execute actions."""
-    for iteration in range(max_iterations):
-        if not hasattr(response, 'output') or not response.output:
-            print("No output from model.")
-            break
-        
-        # Safely access response id
-        response_id = getattr(response, 'id', 'unknown')
-        print(f"\nIteration {iteration + 1} - Response ID: {response_id}\n")
-        
-        # Print text responses and reasoning
-        for item in response.output:
-            # Handle text output
-            if hasattr(item, 'type') and item.type == "text":
-                print(f"\nModel message: {item.text}\n")
-                
-            # Handle reasoning output
-            if hasattr(item, 'type') and item.type == "reasoning":
-                # Extract meaningful content from the reasoning
-                meaningful_content = []
-                
-                if hasattr(item, 'summary') and item.summary:
-                    for summary in item.summary:
-                        # Handle different potential formats of summary content
-                        if isinstance(summary, str) and summary.strip():
-                            meaningful_content.append(summary)
-                        elif hasattr(summary, 'text') and summary.text.strip():
-                            meaningful_content.append(summary.text)
-                
-                # Only print reasoning section if there's actual content
-                if meaningful_content:
-                    print("=== Model Reasoning ===")
-                    for idx, content in enumerate(meaningful_content, 1):
-                        print(f"{content}")
-                    print("=====================\n")
-        
-        # Extract computer calls
-        computer_calls = [item for item in response.output 
-                         if hasattr(item, 'type') and item.type == "computer_call"]
-        
-        if not computer_calls:
-            print("No computer call found in response. Reverting control to human supervisor")
-            break
-        
-        computer_call = computer_calls[0]
-        if not hasattr(computer_call, 'call_id') or not hasattr(computer_call, 'action'):
-            print("Computer call is missing required attributes.")
-            break
-        
-        call_id = computer_call.call_id
-        action = computer_call.action
-        
-        # Handle safety checks
-        acknowledged_checks = []
-        if hasattr(computer_call, 'pending_safety_checks') and computer_call.pending_safety_checks:
-            pending_checks = computer_call.pending_safety_checks
-            print("\nSafety checks required:")
-            for check in pending_checks:
-                print(f"- {check.code}: {check.message}")
-            
-            if input("\nDo you want to proceed? (y/n): ").lower() != 'y':
-                print("Operation cancelled by user.")
-                break
-            
-            acknowledged_checks = pending_checks
-        
-        # Execute the action
-        try:
-           await page.bring_to_front()
-           await handle_action(page, action)
-           
-           # Check if a new page was created after the action
-           if action.type in ["click"]:
-               await asyncio.sleep(1.5)
-               # Get all pages in the context
-               all_pages = page.context.pages
-               # If we have multiple pages, check if there's a newer one
-               if len(all_pages) > 1:
-                   newest_page = all_pages[-1]  # Last page is usually the newest
-                   if newest_page != page and newest_page.url not in ["about:blank", ""]:
-                       print(f"\tSwitching to new tab: {newest_page.url}")
-                       page = newest_page  # Update our page reference
-           elif action.type != "wait":
-               await asyncio.sleep(0.5)
-               
-        except Exception as e:
-           print(f"Error handling action {action.type}: {e}")
-           import traceback
-           traceback.print_exc()    
-
-        # Take a screenshot after the action
-        screenshot_base64 = await take_screenshot(page)
-
-        print("\tNew screenshot taken")
-        
-        # Prepare input for the next request
-        input_content = [{
-            "type": "computer_call_output",
-            "call_id": call_id,
-            "output": {
-                "type": "input_image",
-                "image_url": f"data:image/png;base64,{screenshot_base64}"
-            }
-        }]
-        
-        # Add acknowledged safety checks if any
-        if acknowledged_checks:
-            acknowledged_checks_dicts = []
-            for check in acknowledged_checks:
-                acknowledged_checks_dicts.append({
-                    "id": check.id,
-                    "code": check.code,
-                    "message": check.message
-                })
-            input_content[0]["acknowledged_safety_checks"] = acknowledged_checks_dicts
-        
-        # Add current URL for context
-        try:
-            current_url = page.url
-            if current_url and current_url != "about:blank":
-                input_content[0]["current_url"] = current_url
-                print(f"\tCurrent URL: {current_url}")
-        except Exception as e:
-            print(f"Error getting URL: {e}")
-        
-        # Send the screenshot back for the next step
-        try:
-            response = client.responses.create(
-                model=MODEL,
-                previous_response_id=response_id,
-                tools=[{
-                    "type": "computer_use_preview",
-                    "display_width": DISPLAY_WIDTH,
-                    "display_height": DISPLAY_HEIGHT,
-                    "environment": "browser"
-                }],
-                input=input_content,
-                truncation="auto"
-            )
-
-            print("\tModel processing screenshot")
-        except Exception as e:
-            print(f"Error in API call: {e}")
-            import traceback
-            traceback.print_exc()
-            break
-    
-    if iteration >= max_iterations - 1:
-        print("Reached maximum number of iterations. Stopping.")
-        
-async def main():    
-    # Initialize OpenAI client
-    client = AzureOpenAI(
-        azure_endpoint=AZURE_ENDPOINT,
-        azure_ad_token_provider=token_provider,
-        api_version=API_VERSION
+for event in stream:
+    if event.type == "response.image_generation_call.partial_image":
+        idx = event.partial_image_index
+        image_base64 = event.partial_image_b64
+        image_bytes = base64.b64decode(image_base64)
+        with open(f"river{idx}.png", "wb") as f:
+            f.write(image_bytes)
+```
+
+
+### Edit images
+
+```python
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+import base64
+
+client = AzureOpenAI(  
+  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
+  azure_ad_token_provider=token_provider,
+  api_version="preview",
+  default_headers={"x-ms-oai-image-generation-deployment":"YOUR-GPT-IMAGE1-DEPLOYMENT-NAME"}
+)
+
+def create_file(file_path):
+  with open(file_path, "rb") as file_content:
+    result = client.files.create(
+        file=file_content,
+        purpose="vision",
     )
-    
-    # Initialize Playwright
-    async with async_playwright() as playwright:
-        browser = await playwright.chromium.launch(
-            headless=False,
-            args=[f"--window-size={DISPLAY_WIDTH},{DISPLAY_HEIGHT}", "--disable-extensions"]
-        )
-        
-        context = await browser.new_context(
-            viewport={"width": DISPLAY_WIDTH, "height": DISPLAY_HEIGHT},
-            accept_downloads=True
-        )
-        
-        page = await context.new_page()
-        
-        # Navigate to starting page
-        await page.goto("https://www.bing.com", wait_until="domcontentloaded")
-        print("Browser initialized to Bing.com")
-        
-        # Main interaction loop
-        try:
-            while True:
-                print("\n" + "="*50)
-                user_input = input("Enter a task to perform (or 'exit' to quit): ")
-                
-                if user_input.lower() in ('exit', 'quit'):
-                    break
-                
-                if not user_input.strip():
-                    continue
-                
-                # Take initial screenshot
-                screenshot_base64 = await take_screenshot(page)
-                print("\nTake initial screenshot")
-                
-                # Initial request to the model
-                response = client.responses.create(
-                    model=MODEL,
-                    tools=[{
-                        "type": "computer_use_preview",
-                        "display_width": DISPLAY_WIDTH,
-                        "display_height": DISPLAY_HEIGHT,
-                        "environment": "browser"
-                    }],
-                    instructions = "You are an AI agent with the ability to control a browser. You can control the keyboard and mouse. You take a screenshot after each action to check if your action was successful. Once you have completed the requested task you should stop running and pass back control to your human supervisor.",
-                    input=[{
-                        "role": "user",
-                        "content": [{
-                            "type": "input_text",
-                            "text": user_input
-                        }, {
-                            "type": "input_image",
-                            "image_url": f"data:image/png;base64,{screenshot_base64}"
-                        }]
-                    }],
-                    reasoning={"generate_summary": "concise"},
-                    truncation="auto"
-                )
-                print("\nSending model initial screenshot and instructions")
-
-                # Process model actions
-                await process_model_response(client, response, page)
-                
-        except Exception as e:
-            print(f"An error occurred: {e}")
-            import traceback
-            traceback.print_exc()
-        
-        finally:
-            # Close browser
-            await context.close()
-            await browser.close()
-            print("Browser closed.")
-
-if __name__ == "__main__":
-    asyncio.run(main())
+    return result.id
+
+def encode_image(file_path):
+    with open(file_path, "rb") as f:
+        base64_image = base64.b64encode(f.read()).decode("utf-8")
+    return base64_image
+
+prompt = """Generate a photorealistic image of a gift basket on a white background 
+labeled 'Relax & Unwind' with a ribbon and handwriting-like font, 
+containing all the items in the reference pictures."""
+
+base64_image1 = encode_image("image1.png")
+base64_image2 = encode_image("image2.png")
+file_id1 = create_file("image3.png")
+file_id2 = create_file("image4.png")
+
+response = client.responses.create(
+    model="gpt-4.1",
+    input=[
+        {
+            "role": "user",
+            "content": [
+                {"type": "input_text", "text": prompt},
+                {
+                    "type": "input_image",
+                    "image_url": f"data:image/jpeg;base64,{base64_image1}",
+                },
+                {
+                    "type": "input_image",
+                    "image_url": f"data:image/jpeg;base64,{base64_image2}",
+                },
+                {
+                    "type": "input_image",
+                    "file_id": file_id1,
+                },
+                {
+                    "type": "input_image",
+                    "file_id": file_id2,
+                }
+            ],
+        }
+    ],
+    tools=[{"type": "image_generation"}],
+)
+
+image_generation_calls = [
+    output
+    for output in response.output
+    if output.type == "image_generation_call"
+]
+
+image_data = [output.result for output in image_generation_calls]
+
+if image_data:
+    image_base64 = image_data[0]
+    with open("gift-basket.png", "wb") as f:
+        f.write(base64.b64decode(image_base64))
+else:
+    print(response.output.content)
 ```
+
+
+## Reasoning models
+
+For examples of how to use reasoning models with the responses API see the [reasoning models guide](./reasoning.md#reasoning-summary).
+
+## Computer use
+
+Computer use with Playwright has moved to the [dedicated computer use model guide](./computer-use.md#playwright-integration)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Responses APIの大幅な改訂と新機能の追加"
}
```

### Explanation
この変更は、Azure OpenAIの`responses.md`文書における大幅な修正を示しており、Responses APIに関する新機能の追加と既存の機能の改訂が含まれています。ここでは、主要な変更点をいくつか挙げます。

主要な変更点：
1. **APIバージョン情報の更新**: 使用するAPIバージョンが`2025-03-01-preview`から`preview`へと変更され、最新の機能へのアクセスが強調されています。
2. **機能の拡充**: 新リリースに関連する様々な設定や利用方法が文書に反映され、特にMCP（Model Context Protocol）サーバーとの統合について詳述されています。
3. **レスポンスの処理方法の変更**: モデルのレスポンス処理方法が更新されており、具体的には`gpt-4.1-nano`モデルが使用されるようになっています。
4. **新しいツールと以前の機能との連携**: 画像生成機能が追加され、多段階のプロンプトを使用して画像の作成と編集を支持する新しい仕組みが導入されています。これにより、ユーザーは対話形式で画像を生成できるようになり、柔軟な利用が可能となります。

これらの変更により、開発者とユーザーはResponses APIを通じてAzure OpenAIの機能をより広範に利用でき、最新の機能へも容易にアクセスできるようになります。全体として、この更新はユーザーに優れた体験と高度な機能を提供することを目的としています。

## articles/ai-services/openai/how-to/use-web-app.md{#item-802413}

<details>
<summary>Diff</summary>
````diff
@@ -387,7 +387,7 @@ For further instructions on enabling these data sources, see the [GitHub reposit
 > [!NOTE]
 > As of February 1, 2024, the web app requires the app startup command to be set to `python3 -m gunicorn app:app`. When you're updating an app that was published before February 1, 2024, you need to manually add the startup command from the **App Service Configuration** page.
 
-We recommend pulling changes from the `main` branch for the web app's source code frequently to ensure that you have the latest bug fixes, API version, and improvements. Additionally, the web app must be synchronized every time the API version that you're using is [retired](../api-version-deprecation.md). Consider selecting either the **Watch** or the **Star** button on the web app's [GitHub repo](https://github.com/microsoft/sample-app-aoai-chatGPT) to be notified about changes and updates to the source code.
+We recommend pulling changes from the `main` branch for the web app's source code frequently to ensure that you have the latest bug fixes, API version, and improvements. Additionally, the web app must be synchronized every time the API version that you're using is [retired](../api-version-lifecycle.md). Consider selecting either the **Watch** or the **Star** button on the web app's [GitHub repo](https://github.com/microsoft/sample-app-aoai-chatGPT) to be notified about changes and updates to the source code.
 
 If you haven't customized the web app, you can use these steps to synchronize it:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Webアプリの起動コマンドに関する更新"
}
```

### Explanation
この変更は、Azure OpenAIの`use-web-app.md`文書の軽微な更新を示しており、Webアプリに関する起動コマンドの注意点が改訂されました。

主な変更点は以下の通りです：
1. **起動コマンドの指定**: 2024年2月1日以降、Webアプリの起動コマンドを`python3 -m gunicorn app:app`に設定する必要があることが強調されています。これにより、アプリケーションの正しい起動が促進されます。
2. **情報の標準化**: 旧文からの更新点として、APIバージョンの管理に関する情報が統一されています。特にAPIバージョンが廃止された際にWebアプリを同期する必要があることが明確に述べられています。

この更新によって、開発者はWebアプリを適切に管理し、最新のバージョンを参照するための手順を維持しやすくなります。また、GitHubリポジトリにおける変更通知の受け取り方法についても触れ、開発者の利便性を向上させています。全体として、この修正はユーザーにとって重要な運用上の注意点を明確に示しています。

## articles/ai-services/openai/includes/api-surface.md{#item-a25fa2}

<details>
<summary>Diff</summary>
````diff
@@ -19,6 +19,9 @@ Managing and interacting with Azure OpenAI models and resources is divided acros
 
 Each API surface/specification encapsulates a different set of Azure OpenAI capabilities. Each API has its own unique set of preview and stable/generally available (GA) API releases. Preview releases currently tend to follow a monthly cadence.
 
+> [!IMPORTANT]
+> There is now a new preview inference API. Learn more in our [API lifecycle guide](../api-version-lifecycle.md#api-evolution).
+
 | API | Latest preview release | Latest GA release | Specifications | Description |
 |:---|:----|:----|:----|:---|
 | **Control plane** | [`2024-06-01-preview`](/rest/api/aiservices/accountmanagement/operation-groups?view=rest-aiservices-accountmanagement-2024-06-01-preview&preserve-view=true) | [`2024-10-01`](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices) | Azure OpenAI shares a common control plane with all other services. The control plane API is used for things like [creating Azure OpenAI resources](/rest/api/aiservices/accountmanagement/accounts/create?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), [model deployment](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), and other higher level resource management tasks. The control plane also governs what is possible to do with capabilities like Azure Resource Manager, Bicep, Terraform, and Azure CLI.|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいプレビュー推論APIの追加に関する通知"
}
```

### Explanation
この変更は、Azure OpenAIに関連する`api-surface.md`文書の軽微な更新を示しており、新しいプレビュー推論APIについての情報が追加されました。

主な変更点は以下の通りです：
1. **新しい注意喚起の追加**: 新プレビュー推論APIが登場したことに関する重要な情報が追加され、ユーザーに向けてその詳細を案内する内容が記載されています。この注意事項は、APIの進化に関連する指針を参照することを促しています。
   
2. **情報の整理**: プレビューとGA（一般提供）バージョンのリリースについての説明が強調され、ユーザーがAPIのバージョン管理を理解しやすくなっています。

この更新により、開発者は新しい推論APIの存在を認識し、さらにそれに関する詳細情報にアクセスすることが容易になります。総じて、変更はユーザーにとってAPIの利用についての理解を深めるものであり、開発プロセスにおいて有益な情報を提供することを目的としています。

## articles/ai-services/openai/includes/api-versions/new-inference-preview.md{#item-bd665f}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい推論プレビューAPIに関する文書の追加"
}
```

### Explanation
この変更は、Azure OpenAIのAPIバージョンに関連する新しい文書`new-inference-preview.md`の追加を示しており、合計で4740行の詳細なコンテンツが含まれています。

主なポイントは以下の通りです：
1. **新しいプレビューAPIの詳細**: 新しい推論APIに関する包括的な情報が追加されており、APIの機能、使用方法、ベストプラクティスなどについて詳しく説明されています。これにより、開発者は新機能を理解し、実装に活かすことができるようになります。

2. **豊富なコンテンツ**: この文書は4730行を超える情報を含んでおり、さまざまな側面から新しいAPIについての詳細が網羅されています。具体的には、エンドポイント、リクエスト・レスポンスの形式、エラーハンドリング、サンプルコードなどが考えられます。

この更新により、ユーザーは新しい推論APIに関する包括的なリソースにアクセスできるようになり、APIを利用する際の理解が深まることを目的としています。全体として、この文書はAzure OpenAIの機能を最大限に活用するための重要なガイドとなります。

## articles/ai-services/openai/includes/batch/batch-python.md{#item-3121c2}

<details>
<summary>Diff</summary>
````diff
@@ -226,7 +226,7 @@ If your batch jobs are so large that you're hitting the enqueued token limit eve
 
 ## Track batch job progress
 
-Once you have created batch job successfully you can monitor its progress either in the Studio or programatically. When checking batch job progress we recommend waiting at least 60 seconds in between each status call.
+Once you have created batch job successfully you can monitor its progress either in the Studio or programmatically. When checking batch job progress we recommend waiting at least 60 seconds in between each status call.
 
 ```Python
 import time
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書内の誤字修正"
}
```

### Explanation
この変更は、`batch-python.md`文書内の軽微な修正を示しており、具体的には「programatic」を「programmatically」に修正するという内容です。総計で2行が変更され、そのうち1行が追加され、1行が削除されています。

主なポイントは以下の通りです：
1. **誤字の修正**: プログラムでのバッチジョブの進行状況を監視する方法についての説明文中にあった誤字が修正されました。この変更により、文の正確さが向上し、読者が情報を誤解するリスクが減少します。

2. **コンテンツの明確化**: 誤字を修正することで、文書全体のプロフェッショナルな質が向上し、ユーザーが指示内容をより簡単に理解できるようになります。

この軽微な更新は、文書の全体的な品質を向上させ、ユーザーにとっての有用性が高まることを目的としています。全般的に、文書の正確性を維持することは、技術文書において重要です。

## articles/ai-services/openai/includes/batch/batch-rest.md{#item-bcccd9}

<details>
<summary>Diff</summary>
````diff
@@ -189,7 +189,7 @@ The default 500 max file limit per resource also applies to output files. Here y
 
 ## Track batch job progress
 
-Once you have created batch job successfully you can monitor its progress either in the Studio or programatically. When checking batch job progress we recommend waiting at least 60 seconds in between each status call.
+Once you have created batch job successfully you can monitor its progress either in the Studio or programmatically. When checking batch job progress we recommend waiting at least 60 seconds in between each status call.
 
 ```http
 curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches/{batch_id}?api-version=2025-03-01-preview \
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書内の誤字修正"
}
```

### Explanation
この変更は、`batch-rest.md`文書内の軽微な修正を示しており、具体的には「programatic」を「programmatically」に修正するという内容です。総計で2行が変更され、そのうち1行が追加され、1行が削除されています。

主なポイントは以下の通りです：
1. **誤字の修正**: バッチジョブの進行状況を監視する方法に関する文中にあった誤字が修正されました。この変更により、文書の正確性が向上し、利用者が情報を誤解するリスクを軽減します。

2. **文書の信頼性向上**: 修正により、文書全体の専門性が強化され、ユーザーが説明に従いやすくなります。技術的な内容では正確な表現が特に重要であるため、この修正はユーザーエクスペリエンスの向上に貢献します。

この軽微な更新は、全体の文書品質を向上させ、ユーザーにとってより有益なリソースとなることを目的としています。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ ms.date: 05/05/2025
 | **Region**     | **o3**, **2025-04-16**   | **o4-mini**, **2025-04-16**   | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-nano**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
 |:-------------------|:----------------------:|:---------------------------:|:---------------------------:|:--------------------------------:|:--------------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
 | australiaeast      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| brazilsouth        | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| brazilsouth        | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | canadaeast         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | eastus             | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | eastus2            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
@@ -25,14 +25,14 @@ ms.date: 05/05/2025
 | northcentralus     | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | norwayeast         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | polandcentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southafricanorth   | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southafricanorth   | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | southcentralus     | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southeastasia      | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southindia         | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southeastasia      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southindia         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | spaincentral       | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | swedencentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | switzerlandnorth   | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandwest    | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandwest    | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | uaenorth           | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | uksouth            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | westeurope         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル対応地域の更新"
}
```

### Explanation
今回の変更は、`provisioned-global.md`文書におけるサービスが提供される地域に関する情報を更新したものです。この差分では、5行が追加され、5行が削除され、合計で10行の変更が行われています。

主なポイントは以下の通りです：
1. **地域情報の拡充**: 各モデルが利用可能な地域に対して、新たにサービスの提供が確立されたことが確認でき、これによりユーザーが利用可能なリソースを理解しやすくなります。具体的には、いくつかの地域における前の「-」の部分が「✅」に置き換えられ、これによりその地域での対応が強調されています。

2. **視認性の向上**: 各地域の対応状況が明確に示されることで、ユーザーが自身の地域に基づく利用計画の策定が容易になります。この更新は、モデルを利用したいユーザーにとっての利便性を高め、選択肢を拡大する効果があります。

3. **文書の整合性維持**: 更新された情報により、文書全体の整合性が保たれ、最新のサービス情報が反映されるため、技術文書としての信頼性も高まります。

この変更は、モデルと地域の対応に関する重要な情報の正確性を高め、ユーザーに対してより良い理解と選択肢を提供することを目的としています。

## articles/ai-services/openai/includes/model-matrix/provisioned-models.md{#item-8ee639}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ ms.date: 05/07/2025
 | francecentral      | -                  | -                       | -                       | -                            | -                            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | -                      | ✅                       |
 | germanywestcentral | -                  | -                       | -                       | -                            | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | -                      |
 | japaneast          | -                  | -                       | -                       | -                            | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | -               | ✅                        | ✅                        | ✅                            | -                   | -                      | ✅                       |
-| koreacentral       | -                  | -                       | -                       | -                            | -                            | ✅                        | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | -                       | -                       | ✅                            | ✅                    | ✅                       | -                      |
+| koreacentral       | -                  | -                       | ✅                        | -                            | -                            | ✅                        | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | -                       | -                       | ✅                            | ✅                    | ✅                       | -                      |
 | northcentralus     | -                  | ✅                        | ✅                        | -                            | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | norwayeast         | -                  | -                       | -                       | -                            | -                            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                           | ✅                    | -                      | -                      |
 | polandcentral      | -                  | -                       | -                       | -                            | -                            | -                       | -                  | ✅                       | -                      | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのプロビジョニング情報の修正"
}
```

### Explanation
この変更は、`provisioned-models.md`文書におけるモデルのプロビジョニングに関する情報を修正したものです。変更は、合計2行にわたり、1行の追加と1行の削除が行われています。

主なポイントは以下の通りです：
1. **モデルの状態の更新**: 特に「koreacentral」地域に関して、モデルの利用可能状況に変化がありました。元々「-」で示されていた部分が「✅」に変更され、特定のモデルがその地域で使用できるようになったことが示されています。この更新により、ユーザーはどのモデルがいつ利用可能かを把握しやすくなります。

2. **ユーザビリティの向上**: 各モデルの対応状況が明確に示されることで、利用者は自身にとって最適なモデルを選択しやすくなるため、実際の利用における利便性が向上します。この情報は、特定の地域での利用可能モデルを検討しているユーザーにとって非常に重要です。

3. **文書の整合性維持**: プロビジョニング情報が最新の状況に更新されることで、文書の信頼性が保たれ、技術的な正確性が向上します。このような更新は、ユーザーが情報を信頼できるようにするために不可欠です。

この変更は、モデルがどこで利用可能であるかを明確にし、ユーザーの選択肢を広げることを目的としています。

## articles/ai-services/openai/includes/model-matrix/standard-image-generation.md{#item-dd78ea}

<details>
<summary>Diff</summary>
````diff
@@ -9,8 +9,10 @@ ms.custom: references_regions
 ms.date: 02/06/2025
 ---
 
-| **Region**   | **dall-e-3**, **3.0**   |
-|:-----------------|:---------------------:|
-| australiaeast    | ✅                  |
-| eastus           | ✅                  |
-| swedencentral    | ✅                  |
\ No newline at end of file
+| **Region**   | **dall-e-3**, **3.0**   | **gpt-image-1** |
+|:-----------------|:---------------------:|---|
+| australiaeast    | ✅                  |  |
+| eastus           | ✅                  |  |
+| swedencentral    | ✅                  |  |
+| westus3   |                   | ✅ |
+| uaenorth    |                  |✅   |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準画像生成モデルの地域対応修正"
}
```

### Explanation
この変更は、`standard-image-generation.md`文書において、標準画像生成モデルの対応地域に関する情報を更新したものです。合計12行の変更があり、7行が追加され、5行が削除されています。

主なポイントは以下の通りです：
1. **新しいモデルの追加**: この文書に「gpt-image-1」モデルが追加されました。このモデルの地域対応が新たに記載されたことで、利用者はこのモデルが利用できる地域を理解できるようになりました。

2. **地域情報の更新**: 既存の「dall-e-3」モデルに対する地域情報が更新され、以前は記載されていなかった地域（「westus3」および「uaenorth」）が追加されることで、特にこれらの地域における新たな利用可能性が提示されています。

3. **表のフォーマットの改善**: 新たに列が作成され、可視性が向上しています。これにより、ユーザーは各モデルの地域対応状況をより簡単に比較できます。

これらの変更は、標準画像生成に関連する利用可能なモデルを明示し、ユーザーに対して提供する情報の範囲を拡大することを目的としています。ユーザーは、自身の地域でどのモデルが利用できるかを知ることで、より適切な選択を行えるようになります。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -195,7 +195,7 @@ M = million | K = thousand
 
 ### gpt-4o audio
 
-The rate limits for each `gpt-4o` audio model deployment are 100 K TPM and 1 K RPM. During the preview, [Azure AI Foundry portal](https://ai.azure.com/) and APIs might inaccurately show different rate limits. Even if you try to set a different rate limit, the actual rate limit will be 100 K TPM and 1 K RPM.
+The rate limits for each `gpt-4o` audio model deployment are 100 K TPM and 1 K RPM. During the preview, [Azure AI Foundry portal](https://ai.azure.com/) and APIs might inaccurately show different rate limits. Even if you try to set a different rate limit, the actual rate limit is 100 K TPM and 1 K RPM.
 
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
 |---|---|:---:|:---:|
@@ -231,7 +231,7 @@ The Usage Limit determines the level of usage above which customers might see la
 
 ## Other offer types
 
-If your Azure subscription is linked to certain [offer types](https://azure.microsoft.com/support/legal/offer-details/) your max quota values are lower than the values indicated in the above tables.
+If your Azure subscription is linked to certain [offer types](https://azure.microsoft.com/support/legal/offer-details/), your max quota values are lower than the values indicated in the above tables.
 
 |Tier| Quota Limit in tokens per minute (TPM) |
 |---|:---|
@@ -246,7 +246,7 @@ If your Azure subscription is linked to certain [offer types](https://azure.micr
 
 <sup>*</sup>This only applies to a small number of legacy CSP sandbox subscriptions. Use the query below to determine what `quotaId` is associated with your subscription.
 
-To determine the offer type that is associated with your subscription. you can check your `quotaId`. If your `quotaId` isn't listed in this table your subscription qualifies for default quota.
+To determine the offer type that is associated with your subscription, you can check your `quotaId`. If your `quotaId` isn't listed in this table, your subscription qualifies for default quota.
 
 # [REST](#tab/REST)
 
@@ -313,15 +313,15 @@ To minimize issues related to rate limits, it's a good idea to use the following
 
 ## How to request quota increases
 
-Quota increase requests can be submitted via the [quota increase request form](https://aka.ms/oai/stuquotarequest). Due to high demand, quota increase requests are being accepted and will be filled in the order they're received. Priority is given to customers who generate traffic that consumes the existing quota allocation, and your request might be denied if this condition isn't met.
+Quota increase requests can be submitted via the [quota increase request form](https://aka.ms/oai/stuquotarequest). Due to high demand, quota increase requests are being accepted and are filled in the order they're received. Priority is given to customers who generate traffic that consumes the existing quota allocation, and your request might be denied if this condition isn't met.
 
 For other rate limits, [submit a service request](../cognitive-services-support-options.md?context=/azure/ai-services/openai/context/context).
 
 ## Regional quota capacity limits
 
 You can view quota availability by region for your subscription in the [Azure AI Foundry portal](https://ai.azure.com/resource/quota).
 
-Alternatively to view quota capacity by region for a specific model/version you can query the [capacity API](/rest/api/aiservices/accountmanagement/model-capacities/list) for your subscription. Provide a `subscriptionId`, `model_name`, and `model_version` and the API will return the available capacity for that model across all regions, and deployment types for your subscription.
+Alternatively to view quota capacity by region for a specific model/version you can query the [capacity API](/rest/api/aiservices/accountmanagement/model-capacities/list) for your subscription. Provide a `subscriptionId`, `model_name`, and `model_version` and the API returns the available capacity for that model across all regions, and deployment types for your subscription.
 
 > [!NOTE]
 > Currently both the Azure AI Foundry portal and the capacity API return quota/capacity information for models that are [retired](./concepts/model-retirements.md) and no longer available.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータと制限情報の文言修正"
}
```

### Explanation
この変更は、`quotas-limits.md`文書におけるクォータと制限に関する説明文の修正を行ったものです。合計で10行の変更があり、そのうち5行が追加され、5行が削除されています。

主なポイントは以下の通りです：
1. **文言の言い回しの修正**: いくつかの文で、動詞の時制が一貫するように修正されています。特に、`actual rate limit will be`から`actual rate limit is`への変更などによって、より現在形での表現が強調されています。

2. **明確さの向上**: 修正された文言により、ユーザーにとって情報がより明確になり、理解しやすくなっています。特に、クォータに関連する情報や条件に対しての記述が整理され、誤解を招かないよう配慮されています。

3. **一貫性の向上**: 文全体にわたって用語の使い方が統一され、クォータに関する情報が一貫した形式で記載されています。これにより、読者が情報を簡単に参照できるようになります。

これらの変更は、文書が提供する情報の正確性と信頼性を高め、ユーザーがより簡単に情報を把握できるようにすることを目的としています。特にクォータの管理や制限についての理解が重要なため、このような修正は特に効果的です。

## articles/ai-services/openai/reference-preview-latest.md{#item-dbae2a}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,30 @@
+---
+title: Azure OpenAI in Azure AI Foundry Models REST API v1 preview reference
+titleSuffix: Azure OpenAI
+description: Learn how to use Azure OpenAI's latest v1 preview REST API. In this article, you learn about authorization options,  how to structure a request and receive a response.
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: conceptual
+ms.date: 05/28/2025
+author: mrbullwinkle
+ms.author: mbullwin
+recommendations: false
+ms.custom:
+---
+
+# Azure OpenAI in Azure AI Foundry Models REST API v1 preview reference
+
+This article provides details on the inference REST API endpoints for Azure OpenAI.
+
+## Data plane inference
+
+The rest of the article covers our new v1 preview API release of the Azure OpenAI data plane inference specification. Learn more in our [API lifecycle guide](./api-version-lifecycle.md#api-evolution).
+
+If you're looking for documentation on the latest GA API release, refer to the [latest GA data plane inference API](./reference.md)
+
+[!INCLUDE [API surfaces](./includes/api-versions/new-inference-preview.md)]
+
+## Next steps
+
+Learn about [Models, and fine-tuning with the REST API](/rest/api/azureopenai/fine-tuning).
+Learn more about the [underlying models that power Azure OpenAI](./concepts/models.md).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIの最新v1プレビューREST APIリファレンスの追加"
}
```

### Explanation
この変更は、`reference-preview-latest.md`という新しい文書が追加されたことを示しています。この文書は、Azure OpenAIの最新のv1プレビューREST APIに関するリファレンス情報を提供しています。合計で30行の新しい内容が追加されており、削除された行はありません。

主なポイントは以下の通りです：
1. **新規情報の追加**: Azure OpenAIのデータプレーン推論に関連するREST APIエンドポイントに関する詳細が提供されており、利用者がプレビューAPIの使用に必要な情報を得られます。

2. **明確な構造**: 記事は、Azure OpenAIの最新v1プレビューリリースに関する情報をシンプルに整理しています。ユーザーは認証オプション、リクエストの構造、レスポンスの受け取り方について学ぶことができるようになります。

3. **次のステップの案内**: ユーザーが更に学ぶことを促すリンクが含まれており、モデルやファインチューニングに関する情報へのアクセスが容易に行えます。

4. **APIライフサイクルガイドへのリンク**: 新しいv1プレビュAPIの仕様について、APIライフサイクルに関するガイドへのリンクが記載されており、ユーザーがより詳細な情報を参照できるよう配慮されています。

この文書は、Azure OpenAIのAPIの利用を拡大する目的で作成されており、特に新しいAPIを試したい開発者や研究者にとって有用なリソースとなるでしょう。

## articles/ai-services/openai/reference-preview.md{#item-e197a2}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ This article provides details on the inference REST API endpoints for Azure Open
 
 ## Data plane inference
 
-The rest of the article covers the latest preview release of the Azure OpenAI data plane inference specification, `2025-03-01-preview`. This article includes documentation for the latest preview capabilities like assistants, threads, and vector stores.
+The rest of the article covers the `2025-04-01-preview` preview release of the Azure OpenAI data plane inference specification.
 
 If you're looking for documentation on the latest GA API release, refer to the [latest GA data plane inference API](./reference.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データプレーン推論仕様のプレビューリリース日付の更新"
}
```

### Explanation
この変更は、`reference-preview.md`文書内のデータプレーン推論仕様に関する記述が更新されたことを示しています。具体的には、プレビューリリースの日付が`2025-03-01-preview`から`2025-04-01-preview`に変更されています。この変更により、合計で2行の変更が行われ、1行が追加され、1行が削除されています。

主なポイントは以下の通りです：
1. **リリース日付の更新**: 記事内で言及されているプレビューリリースの日付が新しい日の`2025-04-01-preview`に更新されています。これにより、読者には最新の情報が提供されます。

2. **その他の情報の保持**: 変更された文は、引き続きAzure OpenAIのデータプレーン推論の仕様についての情報を提供しており、技術的な内容や新機能に関連する情報がきちんと維持されています。

この小規模な更新は、特にAPIを利用する開発者や研究者にとって、最新のプレビューリリースに関する正確な情報を提供することを目的としています。これにより、ユーザーはAPIの新しい機能を迅速に把握し、利用に向けた準備を整えることができるようになります。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -115,7 +115,7 @@ items:
 - name: How-to 
   items:
   - name: API version lifecycle
-    href: ./api-version-deprecation.md
+    href: ./api-version-lifecycle.md
   - name: Assistants (preview)
     items:
     - name: Getting started with Assistants
@@ -342,11 +342,13 @@ items:
       href: /legal/cognitive-services/openai/customer-copyright-commitment?context=/azure/ai-services/openai/context/context
 - name: Reference
   items:
+    - name: Latest Inference Preview API
+      href: reference-preview-latest.md
     - name: Inference GA API reference
       href: reference.md
-    - name: Authoring preview API reference
+    - name: 2025-04-01-preview - Authoring 
       href: authoring-reference-preview.md
-    - name: Inference preview API reference
+    - name: 2025-04-01-preview - Inference 
       href: reference-preview.md
     - name: Assistants API Reference
       items:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリファレンスとリンクの更新"
}
```

### Explanation
この変更は、`toc.yml`ファイル内の要素が更新されたことを示しています。具体的には、APIのバージョンライフサイクルに関連するリンクが変更され、新しい項目が追加されるなど、合計で8つの変更が行われています。5行が追加され、3行が削除されています。

主なポイントは以下の通りです：
1. **リンクの更新**: "API version lifecycle"という項目のリンクが`./api-version-deprecation.md`から`./api-version-lifecycle.md`に変更されており、より適切なリソースにリダイレクトするようになっています。

2. **新しい項目の追加**: "Latest Inference Preview API"という新しい項目が追加され、`reference-preview-latest.md`へのリンクが提供されるようになっています。これにより、最新のプレビューAPIに関する情報が簡単にアクセスできるようになりました。

3. **プレビューAPIの更新**: "Authoring preview API reference"と"Inference preview API reference"の項目が、それぞれ`2025-04-01-preview - Authoring`と`2025-04-01-preview - Inference`に変更され、最新のプレビュー情報が明確に示されるようになっています。

これらの変更は、特に開発者やユーザーがAzure OpenAIに関する最新の情報に迅速にアクセスできるようサポートすることを目的としています。全体として、これらの更新は文書の整合性と使いやすさを向上させることに寄与しています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: whats-new
-ms.date: 04/16/2025
+ms.date: 5/28/2025
 recommendations: false
 ---
 
@@ -147,7 +147,7 @@ For more information, see the [GPT-4o real-time audio quickstart](realtime-audio
 
 ### o1 reasoning model released for limited access
 
-The latest `o1` model is now available for API access and model deployment. **Registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who previously applied and received access to `o1-preview`, don't need to reapply as they are automatically on the wait-list for the latest model.
+The latest `o1` model is now available for API access and model deployment. **Registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who previously applied and received access to `o1-preview`, don't need to reapply as they're automatically on the wait-list for the latest model.
 
 Request access: [limited access model application](https://aka.ms/OAI/o1access)
 
@@ -161,7 +161,7 @@ To learn more about the advanced `o1` series models see, [getting started with o
 
 ### Preference fine-tuning (preview)
 
-[Direct preference optimization (DPO)](./how-to/fine-tuning-direct-preference-optimization.md) is a new alignment technique for large language models, designed to adjust model weights based on human preferences. Unlike reinforcement learning from human feedback (RLHF), DPO does not require fitting a reward model and uses simpler data (binary preferences) for training. This method is computationally lighter and faster, making it equally effective at alignment while being more efficient. DPO is especially useful in scenarios where subjective elements like tone, style, or specific content preferences are important. We’re excited to announce the public preview of DPO in Azure OpenAI, starting with the `gpt-4o-2024-08-06` model.
+[Direct preference optimization (DPO)](./how-to/fine-tuning-direct-preference-optimization.md) is a new alignment technique for large language models, designed to adjust model weights based on human preferences. Unlike reinforcement learning from human feedback (RLHF), DPO doesn't require fitting a reward model and uses simpler data (binary preferences) for training. This method is computationally lighter and faster, making it equally effective at alignment while being more efficient. DPO is especially useful in scenarios where subjective elements like tone, style, or specific content preferences are important. We’re excited to announce the public preview of DPO in Azure OpenAI, starting with the `gpt-4o-2024-08-06` model.
 
 For fine-tuning model region availability, see the [models page](./concepts/models.md#fine-tuning-models).
 
@@ -199,7 +199,7 @@ For fine-tuning model region availability, see the [models page](./concepts/mode
 
 ### NEW AI abuse monitoring
 
-We are introducing new forms of abuse monitoring that leverage LLMs to improve efficiency of detection of potentially abusive use of the Azure OpenAI and to enable abuse monitoring without the need for human review of prompts and completions. Learn more, see [Abuse monitoring](/azure/ai-services/openai/concepts/abuse-monitoring).
+We're introducing new forms of abuse monitoring that leverage LLMs to improve efficiency of detection of potentially abusive use of the Azure OpenAI and to enable abuse monitoring without the need for human review of prompts and completions. Learn more, see [Abuse monitoring](/azure/ai-services/openai/concepts/abuse-monitoring).
 
 Prompts and completions that are flagged through content classification and/or identified to be part of a potentially abusive pattern of use are subjected to an additional review process to help confirm the system's analysis and inform actioning decisions. Our abuse monitoring systems have been expanded to enable review by LLM by default and by humans when necessary and appropriate. 
 
@@ -312,13 +312,13 @@ OpenAI has incorporated additional safety measures into the `o1` models, includi
 
 ### Availability
 
-The `o1-preview` and `o1-mini` are available in the East US2 region for limited access through the [Azure AI Foundry portal](https://ai.azure.com) early access playground. Data processing for the `o1` models might occur in a different region than where they are available for use.
+The `o1-preview` and `o1-mini` are available in the East US2 region for limited access through the [Azure AI Foundry portal](https://ai.azure.com) early access playground. Data processing for the `o1` models might occur in a different region than where they're available for use.
 
 To try the `o1-preview` and `o1-mini` models in the early access playground **registration is required, and access will be granted based on Microsoft’s eligibility criteria.**
 
 Request access: [limited access model application](https://aka.ms/oai/modelaccess)
 
-Once access has been granted, you will need to:
+Once access has been granted, you'll need to:
 
 1. Navigate to https://ai.azure.com/resources and select a resource in the `eastus2` region. If you don't have an Azure OpenAI resource in this region you'll need to [create one](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI).  
 2. Once the `eastus2` Azure OpenAI resource is selected, in the upper left-hand panel under **Playgrounds** select **Early access playground (preview)**.
@@ -375,7 +375,7 @@ Unlike the previous early access playground, the [Azure AI Foundry portal](https
 > [!NOTE]
 > Prompts and completions made through the early access playground (preview) might be processed in any Azure OpenAI region, and are currently subject to a 10 request per minute per Azure subscription limit. This limit might change in the future.
 >
-> Azure OpenAI abuse monitoring is enabled for all early access playground users even if approved for modification; default content filters are enabled and cannot be modified.
+> Azure OpenAI abuse monitoring is enabled for all early access playground users even if approved for modification; default content filters are enabled and can't be modified.
 
 To test out GPT-4o `2024-08-06`, sign-in to the Azure AI early access playground (preview) using this [link](https://aka.ms/oai/docs/earlyaccessplayground).
 
@@ -562,7 +562,7 @@ Prompt Shields protect applications powered by Azure OpenAI models from two type
 
 ### 2024-05-01-preview API release
 
-- For more information, see the [API version lifecycle](./api-version-deprecation.md).
+- For more information, see the [API version lifecycle](./api-version-lifecycle.md).
 
 ### GPT-4 Turbo model general availability (GA)
 
@@ -615,7 +615,7 @@ Azure OpenAI Studio now provides a Risks & Safety dashboard for each of your dep
 
 This is the latest GA API release and is the replacement for the previous `2023-05-15` GA release. This release adds support for the latest Azure OpenAI GA features like Whisper, DALLE-3, fine-tuning, on your data, and more.
 
-Features that are in preview such as Assistants, text to speech (TTS), and some of the "on your data" datasources, require a preview API version. For more information, check out our [API version lifecycle guide](./api-version-deprecation.md).
+Features that are in preview such as Assistants, text to speech (TTS), and some of the "on your data" datasources, require a preview API version. For more information, check out our [API version lifecycle guide](./api-version-lifecycle.md).
 
 ### Whisper general availability (GA)
 
@@ -644,7 +644,7 @@ We have added a page to track [model deprecations and retirements](./concepts/mo
 - `encoding_format` allows you to specify the format to generate embeddings in `float`, or `base64`. The default is `float`.
 - `dimensions` allows you set the number of output embeddings. This parameter is only supported with the new third generation embeddings models: `text-embedding-3-large`, `text-embedding-3-small`. Typically larger embeddings are more expensive from a compute, memory, and storage perspective. Being able to adjust the number of dimensions allows more control over overall cost and performance. The `dimensions` parameter isn't supported in all versions of the OpenAI 1.x Python library, to take advantage of this parameter  we recommend upgrading to the latest version: `pip install openai --upgrade`.
 
-If you're currently using a preview API version to take advantage of the latest features, we recommend consulting the [API version lifecycle](./api-version-deprecation.md) article to track how long your current API version will be supported.
+If you're currently using a preview API version to take advantage of the latest features, we recommend consulting the [API version lifecycle](./api-version-lifecycle.md) article to track how long your current API version will be supported.
 
 ### Update to GPT-4-1106-Preview upgrade plans
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whats New文書の更新"
}
```

### Explanation
この変更は、`whats-new.md`文書に対する重要な更新を示しています。合計で20行の変更があり、その中で10行が追加され、10行が削除されています。主に日付の更新やテキストの微調整が含まれています。

主なポイントは以下の通りです：
1. **日付の更新**: 文書内の日付が`04/16/2025`から`5/28/2025`に変更されており、これにより情報が最新のものになっています。

2. **コンテンツの修正**: 複数の段落で微細な文の改善が行われており、これにより文章の流れや可読性が向上しています。たとえば、「don’t」が「don’t」に修正されるなどの軽微な変更がある一方で、内容は変わっていません。

3. **新機能の導入**: 新しい`o1`モデルやダイレクト・プレファレンス・オプティマイゼーション（DPO）技術についての説明が引き続き含まれており、新しいAIの悪用監視機能に関する情報も強調されています。これにより、読者はこの技術の進展に関する最新の情報を得ることができます。

4. **他のリンクの更新**: APIのバージョンライフサイクルに関するリンクも更新され、正確な情報を提供するために変更されました。

これらの修正は、技術者や開発者がAzure OpenAIサービスの最新の機能や変更について把握しやすくすることを目的としており、全体的な文書の整合性と有用性が向上しています。


