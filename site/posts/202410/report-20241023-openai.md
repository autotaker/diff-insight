---
date: '2024-10-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bf31bc8...MicrosoftDocs:6f58d1b
summary: 今回の変更では、Azure OpenAIに関するドキュメントが更新され、新しい機能や情報の精度向上が図られています。特にプロンプトキャッシングに関する新しいガイドが追加され、その機能と利用方法が詳しく説明されています。また、モデル関連の情報も更新され、APIドキュメントが改善されています。破壊的変更は報告されていませんが、既存の情報に軽微な修正が施されています。全体として、ユーザー体験を向上させるための重要な更新となっています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bf31bc8...MicrosoftDocs:6f58d1b){target="_blank"}

# ハイライト
今回の変更では、Azure OpenAI関連のドキュメントに対する更新が行われており、新しい機能の追加や情報の精度向上が図られています。特に、新しいプロンプトキャッシングのガイドが追加され、その機能と使用方法について詳細に説明されています。また、モデルに関する情報更新やAPIドキュメントの改善も見られ、新旧の情報がはっきりとアップデートされています。

## 新機能
- **プロンプトキャッシングに関する新しいガイド追加**：Azure OpenAIサービスのプロンプトキャッシングに関するガイドが新たに追加され、その利用方法と利点について詳述されています。
- **目次に新しいトピック「Prompt caching」の追加**：ユーザーがプロンプトキャッシングの情報にアクセスしやすくなるよう、新しいトピックが目次に追加されています。

## 破壊的変更
- 特に破壊的変更は報告されていませんが、既存の情報に軽微な修正が加えられています。

## その他の更新
- **モデル情報の更新**：特にGPT-4oとそのバリエーションに関する情報が簡略化され、関連リンクが整理されています。
- **バッチ処理APIドキュメントの修正**：監視方法やコマンドの整形が改善され、より理解しやすいものに。
- **Azure OpenAI Studioドキュメントの文言修正**：誤字の修正により、情報の正確性が向上しています。

# インサイト
今回のドキュメント更新は、Azure OpenAIユーザーにとって重要なアップデートを含んでいます。主に、新機能であるプロンプトキャッシングが導入され、これがどのように実装されるのかを具体的に理解するためのガイドが詳細に説明されています。プロンプトキャッシングは、リクエストの効率を向上させるものであり、長い文を繰り返し使う場面でのコスト削減と効率化に寄与します。

モデルについての説明の更新は、ユーザーが最新の情報にアクセスできるように配慮されたもので、特にファインチューニングに関する理解を深める助けとなります。また、バッチ処理APIの改善は、開発者が効率的に機能を活用できることを意図しており、これにより実装の便益が向上します。

全体として、今回の変更はユーザーの体験を高めるための重要なステップを踏んでおり、正確な情報提供と新機能の活用を促進するものになっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | モデルに関する情報を更新 | modified | 2 | 2 | 4 | 
| [prompt-caching.md](#item-1631df) | new feature | Azure OpenAIサービスのプロンプトキャッシングに関する新しいガイド | added | 83 | 0 | 83 | 
| [batch-rest.md](#item-bcccd9) | minor update | バッチ処理のAPIコマンドの修正と追加 | modified | 4 | 3 | 7 | 
| [chatgpt-studio.md](#item-ab43f3) | minor update | Azure OpenAI Studioの前提条件の文言修正 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c945af) | new feature | 新しいトピック「Prompt caching」の追加 | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -466,7 +466,7 @@ These models can only be used with Embedding API requests.
 | `gpt-4o-mini` <sup>**1**</sup> (2024-07-18) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 64,536 | Oct 2023 |
 | `gpt-4o` <sup>**1**</sup> (2024-08-06) | East US2 <br> North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 64,536 | Oct 2023 | 
 
-**<sup>1</sup>** GPT-4, GPT-4o, and GPT-4o mini fine-tuning is currently in public preview. See our [GPT-4, GPT-4o,  & GPT-4o mini fine-tuning safety evaluation guidance](/azure/ai-services/openai/how-to/fine-tuning?tabs=turbo%2Cpython-new&pivots=programming-language-python#safety-evaluation-gpt-4-fine-tuning---public-preview) for more information.
+**<sup>1</sup>** GPT-4 is currently in public preview.
 
 ### Whisper models
 
@@ -507,4 +507,4 @@ For the latest information on model retirements, refer to the [model retirement
 - [Model retirement and deprecation](./model-retirements.md)
 - [Learn more about working with Azure OpenAI models](../how-to/working-with-models.md)
 - [Learn more about Azure OpenAI](../overview.md)
-- [Learn more about fine-tuning Azure OpenAI models](../how-to/fine-tuning.md)
\ No newline at end of file
+- [Learn more about fine-tuning Azure OpenAI models](../how-to/fine-tuning.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルに関する情報を更新"
}
```

### Explanation
この変更は、ドキュメント内のモデルに関する情報を更新するもので、Minor Updateに該当します。具体的には、`gpt-4o-mini` と `gpt-4o` モデルの公開プレビューに関する説明が修正され、特に `GPT-4o` と `GPT-4o mini` のファインチューニングについての表記を簡略化しました。さらに、ファインチューニングモデルに関するリンクも整理されています。

変更点としては、以下の内容が含まれます：

1. **GPT-4モデルの公開プレビューについての声明の修正** - GPT-4、GPT-4o、及びGPT-4o miniのファインチューニングが現在はGPT-4のみに言及されています。
2. **関連リンクの更新** - "Learn more about fine-tuning Azure OpenAI models" というリンクが追加され、ドキュメント内でのリソースへのアクセスが容易になりました。

この更新は、モデルの利用者に対して最新の情報を提供し、正確な理解を促進することを目的としています。

## articles/ai-services/openai/how-to/prompt-caching.md{#item-1631df}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,83 @@
+---
+title: 'Prompt caching with Azure OpenAI Service'
+titleSuffix: Azure OpenAI
+description: Learn how to use prompt caching with Azure OpenAI
+services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: how-to
+ms.date: 10/18/2024
+author: mrbullwinkle
+ms.author: mbullwin
+recommendations: false
+---
+
+# Prompt caching
+
+Prompt caching allows you to reduce overall request latency and cost for longer prompts that have identical content at the beginning of the prompt. *"Prompt"* in this context is referring to the input you send to the model as part of your chat completions request. Rather than reprocess the same input tokens over and over again, the model is able to retain a temporary cache of processed input data to improve overall performance. Prompt caching has no impact on the output content returned in the model response beyond a reduction in latency and cost.  
+
+## Supported models
+
+Currently only the following models support prompt caching with Azure OpenAI:
+
+- `o1-preview-2024-09-12`
+- `o1-mini-2024-09-12`
+
+## API support
+
+Official support for prompt caching was first added in API version `2024-10-01-preview`.
+
+## Getting started
+
+For a request to take advantage of prompt caching the request must be both:
+
+- A minimum of 1,024 tokens in length.
+- The first 1,024 tokens in the prompt must be identical.
+
+When a match is found between a prompt and the current content of the prompt cache, it's referred to as a cache hit. Cache hits will show up as [`cached_tokens`](/azure/ai-services/openai/reference-preview#cached_tokens) under [`prompt_token_details`](/azure/ai-services/openai/reference-preview#properties-for-prompt_tokens_details) in the chat completions response.
+
+```json
+{
+  "created": 1729227448,
+  "model": "o1-preview-2024-09-12",
+  "object": "chat.completion",
+  "service_tier": null,
+  "system_fingerprint": "fp_50cdd5dc04",
+  "usage": {
+    "completion_tokens": 1518,
+    "prompt_tokens": 1566,
+    "total_tokens": 3084,
+    "completion_tokens_details": {
+      "audio_tokens": null,
+      "reasoning_tokens": 576
+    },
+    "prompt_tokens_details": {
+      "audio_tokens": null,
+      "cached_tokens": 1408
+    }
+  }
+}
+```
+
+After the first 1,024 tokens cache hits will occur for every 128 additional identical tokens.
+
+A single character difference in the first 1,024 tokens will result in a cache miss which is characterized by a `cached_tokens` value of 0. Prompt caching is enabled by default with no additional configuration needed for supported models.
+
+## What is cached?
+
+The o1-series models are text only and don't support system messages, images, tool use/function calling, or structured outputs. This limits the efficacy of prompt caching for these models to the user/assistant portions of the messages array which are less likely to have an identical 1024 token prefix.
+
+Once prompt caching is enabled for other supported models prompt caching will expand to support:  
+
+| **Caching Supported** | **Description** |
+|--------|--------|
+|**Messages** | The complete messages array: system, user, and assistant content |
+|**Images** | Images included in user messages, both as links or as base64-encoded data. The detail parameter must be set the same across requests.
+|**Tool use**| Both the messages array and tool definitions |
+|**Structured outputs** | Structured output schema is appended as a prefix to the system message|
+
+To improve the likelihood of cache hits occurring, you should structure your requests such that repetitive content occurs at the beginning of the messages array.
+
+## Can I disable prompt caching?
+
+Prompt caching is enabled by default. There is no opt-out option.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIサービスのプロンプトキャッシングに関する新しいガイド"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるプロンプトキャッシングに関する新しいガイドを追加するもので、新機能に該当します。このドキュメントは、プロンプトキャッシングの利用方法を学ぶ手助けを目的としています。

主な内容は以下の通りです：

1. **プロンプトキャッシングの説明** - プロンプトキャッシングを使用することで、特に先頭部分が同一の長いプロンプトにおいて、リクエストのレイテンシとコストを削減できることが説明されています。キャッシングを用いることで、同じ入力トークンを何度も再処理する必要がなくなり、モデルのパフォーマンスが向上します。

2. **サポートされているモデル** - 現在、プロンプトキャッシングをサポートしているモデルとして、`o1-preview-2024-09-12`と`o1-mini-2024-09-12`が紹介されています。

3. **APIサポート** - プロンプトキャッシングはAPIバージョン`2024-10-01-preview`で初めて公式サポートが追加されたことが記されています。

4. **開始方法** - キャッシングを利用するためのリクエストの条件（最小トークン長さや、先頭部分の要求トークンの一致条件）について詳しく述べられています。

5. **キャッシュの詳細** - キャッシュヒットとキャッシュミスに関する情報や、キャッシュがどのように利用されるかの具体例が示されています。

6. **キャッシングの無効化** - プロンプトキャッシングはデフォルトで有効であり、オプトアウトのオプションがないことも説明されています。

この新しいガイドは、ユーザーがAzure OpenAIにおけるプロンプトキャッシング機能を理解し活用するための貴重なリソースとなります。

## articles/ai-services/openai/includes/batch/batch-rest.md{#item-bcccd9}

<details>
<summary>Diff</summary>
````diff
@@ -173,7 +173,6 @@ curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-vers
 
 ## Track batch job progress
 
-
 Once you have created batch job successfully you can monitor its progress either in the Studio or programatically. When checking batch job progress we recommend waiting at least 60 seconds in between each status call.
 
 ```http
@@ -230,7 +229,7 @@ The following status values are possible:
 
 ```http
 curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{output_file_id}/content?api-version=2024-10-01-preview \
-  -H "api-key: $AZURE_OPENAI_API_KEY"  > batch_output.jsonl
+  -H "api-key: $AZURE_OPENAI_API_KEY" > batch_output.jsonl
 ```
 
 ### Additional batch commands
@@ -253,13 +252,15 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024
   -H "api-key: $AZURE_OPENAI_API_KEY" 
 ```
 
+<a id="List"></a>
+
 ### List batch (Preview)
 
 Use the REST API to list all batch jobs with additional sorting/filtering options.
 
 ```http
 curl "YOUR_RESOURCE_NAME.openai.azure.com/batches?api-version=2024-10-01-preview&$filter=created_at%20gt%201728773533%20and%20created_at%20lt%201729032733%20and%20status%20eq%20'Completed'&$orderby=created_at%20asc" \
-  -H "api-key: $AZURE_OPENAI_API_KEY""
+  -H "api-key: $AZURE_OPENAI_API_KEY"
 ```
 
 To avoid the error `URL rejected: Malformed input to a URL function` spaces are replaced with `%20`.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理のAPIコマンドの修正と追加"
}
```

### Explanation
この変更は、バッチ処理に関するAPIコマンドのドキュメントを更新するもので、Minor Updateに該当します。具体的には、バッチジョブの進捗状況の監視方法やコマンドの整形に関する調整が行われています。

主な変更内容は以下の通りです：

1. **監視方法の説明の修正** - バッチジョブを作成した後、進捗を監視する際の推奨待機時間について、説明文が明確化されています。進捗確認の際は、呼び出しごとに最低でも60秒待つことが推奨されています。

2. **cURLコマンドの整形** - 一部のcURLコマンドの書式が修正され、可読性が向上しています。具体的には、末尾のコマンドラインの書式が統一されています。

3. **バッチリスト機能の追加** - REST APIを使用して全てのバッチジョブをリストする新しいセクションが追加され、並べ替えやフィルタリングのオプションが提示されています。これにより、ユーザーは作成日時や状態に基づいてバッチジョブを容易に管理できるようになります。

4. **URLでのスペースの処理方法** - エラーメッセージに関する注意文が追加され、URLのスペースが正しく処理される方法について説明されています。

この更新は、ユーザーがバッチ処理を効果的に利用するための情報をより明確にし、実装の際の利便性を向上させることを目的としています。

## articles/ai-services/openai/includes/chatgpt-studio.md{#item-ab43f3}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.date: 09/19/2024
 ## Prerequisites
 
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
-- An Azure OpenAI Service resource with either `gpt-4o` or the `gpt-4o-mini` models deployed. We recommend using standard or global standard model [deployment tpyes](../how-to/deployment-types.md) for initial exploration. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
+- An Azure OpenAI Service resource with either `gpt-4o` or the `gpt-4o-mini` models deployed. We recommend using standard or global standard model [deployment types](../how-to/deployment-types.md) for initial exploration. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 
 ## Go to Azure OpenAI Studio
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI Studioの前提条件の文言修正"
}
```

### Explanation
この変更は、Azure OpenAI Studioに関するドキュメントの前提条件セクションを更新するもので、Minor Updateに該当します。具体的には、テキストの軽微な修正が行われています。

主な変更内容は以下の通りです：

1. **文言の修正** - Azure OpenAI Serviceリソースに関する説明文において、`deployment tpyes`という誤りが`deployment types`に訂正されました。これにより、情報の正確性が向上し、利用者がより理解しやすくなります。

この修正は、文書の明瞭性を高めることを目的としており、特に新規ユーザーがAzure OpenAIサービスを利用する際に、適切な情報を得られるように配慮されています。全体として、この変更はドキュメントの質を向上させるためのものであり、他の内容は変更されていません。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -130,6 +130,8 @@ items:
       href: ./how-to/completions.md
     - name: JSON mode
       href: ./how-to/json-mode.md
+    - name: Prompt caching
+      href: ./how-to/prompt-caching.md
     - name: Reproducible output
       href: ./how-to/reproducible-output.md
     - name: Structured outputs
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しいトピック「Prompt caching」の追加"
}
```

### Explanation
この変更は、Azure OpenAIに関する目次ファイル（toc.yml）に新しいトピックを追加するもので、新機能の実装に該当します。具体的には、Prompt cachingに関する新たなリンクが追加されています。

主な変更内容は以下の通りです：

1. **新しいトピックの追加** - 目次に「Prompt caching」という項目が追加され、その関連リンクが設定されました。このトピックは、ユーザーがプロンプトのキャッシング方法について学べるように導入されたものです。

この更新は、ユーザーに対して新しい情報源を提供するものであり、特にPrompt cachingについての詳細な理解を得るためのリソースを提供することを目的としています。全体として、ドキュメントの情報量と価値を高めるための重要な改善がなされています。


