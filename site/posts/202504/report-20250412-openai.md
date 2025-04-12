---
date: '2025-04-12'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2873777...MicrosoftDocs:f593d78
summary: このコードの差分では、複数のマイナーアップデートと新機能の追加が行われ、特にバッチジョブのキューイングとフェイルファースト機能が注目されています。また、リンクテキストの修正やコードキー名の一貫性向上、ストレージ完了機能のサポート範囲の拡大も見られます。これらの変更は、Azure
  AIサービスの文書のユーザービリティと機能を向上させることを目指しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2873777...MicrosoftDocs:f593d78){target="_blank"}

<format>
# ハイライト
このコードの差分では、複数のマイナーアップデートと一部の新機能追加が行われており、新機能であるバッチジョブのキューイングとフェイルファースト機能の導入が特に注目されます。また、リンクテキストの修正、コードキー名の一貫性を高めるための変更や、ストレージ完了機能のサポート範囲の拡大が見られます。

## 新機能
- バッチジョブのキューイングとフェイルファースト機能がPythonドキュメントに追加され、負荷の高いジョブの管理が改善されました。

## 破壊的変更
- 特に破壊的変更は含まれていませんが、一貫性を保つためのキー名変更が行われました。

## その他の更新
- リンクテキストの簡潔化
- バッチ処理に関する新しいヒントの追加
- ストレージ完了機能のサポート範囲が拡大

# 洞察
この変更では、Azure AIサービスの文書に対してさまざまなアップデートが行われており、ユーザービリティの向上と機能の拡張が図られています。

まず、リンクテキストの簡潔化により、ユーザーはより直感的に情報にアクセスでき、ナビゲーションが容易になります。リンクの視覚的なシンプルさが、ユーザーエクスペリエンスを改善します。

バッチ処理に関するヒントの追加は、特に大規模なバッチを扱うユーザーにとって有用です。エンキューされたトークン制限に対する対策が具体的に示され、円滑なバッチ処理を支援します。

また、ストレージ完了機能がより多くのデプロイメントに対応したことで、ユーザーがこの機能を利用する柔軟性が高まります。異なるモデルと地域のサポートが体制を強化し、システムの採用を促進するでしょう。

さらに、新機能の追加であるフェイルファースト機能は、システムの効率を大幅に向上させる可能性があります。自動キューイングとリトライにより、バッチジョブの管理がより自動化され、負荷の高いシナリオでのパフォーマンスが向上します。これにより、開発者はシステムの管理に費やす時間を削減し、他の重要なタスクに集中できるようになるでしょう。

全体として、この一連の変更は、ドキュメントの利便性を向上させつつ、Azure AIサービスの機能を強化するものです。ユーザーはこれらの情報をもとに、より効果的にサービスを活用できるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [customizing-llms.md](#item-067bef) | minor update | リンクテキストの修正 | modified | 1 | 1 | 2 | 
| [batch.md](#item-a131d5) | minor update | バッチ処理に関する新しいヒントの追加 | modified | 6 | 1 | 7 | 
| [code-interpreter.md](#item-95efbd) | minor update | ツールリソースのキー名の修正 | modified | 1 | 1 | 2 | 
| [stored-completions.md](#item-ccc7e6) | minor update | ストレージ完了サポートの範囲の拡大 | modified | 2 | 6 | 8 | 
| [batch-python.md](#item-3121c2) | new feature | バッチジョブのキューイングとフェイルファースト機能の追加 | modified | 123 | 1 | 124 | 


# Modified Contents
## articles/ai-services/openai/concepts/customizing-llms.md{#item-067bef}

<details>
<summary>Diff</summary>
````diff
@@ -62,7 +62,7 @@ A corporate HR department is looking to provide an intelligent assistant that an
 
 ### Getting started
 
-- [Retrieval Augmented Generation in [Azure AI Foundry portal](https://ai.azure.com/) - Azure AI Foundry | Microsoft Learn](../../../ai-foundry/concepts/retrieval-augmented-generation.md)
+- [Retrieval Augmented Generation in Azure AI Foundry portal](../../../ai-foundry/concepts/retrieval-augmented-generation.md)
 - [Retrieval Augmented Generation (RAG) in Azure AI Search](/azure/search/retrieval-augmented-generation-overview)
 - [Retrieval Augmented Generation using Azure Machine Learning prompt flow (preview)](/azure/machine-learning/concept-retrieval-augmented-generation)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクテキストの修正"
}
```

### Explanation
この変更は、ファイル `customizing-llms.md` 内のリンクテキストを修正するためのマイナーな更新です。具体的には、Azure AI Foundry ポータルに関するリンクの表記が調整されました。元々は「Retrieval Augmented Generation in [Azure AI Foundry portal](https://ai.azure.com/) - Azure AI Foundry | Microsoft Learn」となっていた部分が、「Retrieval Augmented Generation in Azure AI Foundry portal」に変更され、リンクから「- Azure AI Foundry | Microsoft Learn」が削除されました。この修正により、リンクの見た目がシンプルになり、関連情報へのアクセスがより明確になります。変更は1行の追加と1行の削除で構成されており、全体的な内容に対する影響は最小限です。

## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: references_regions
 ms.topic: how-to
-ms.date: 01/14/2025
+ms.date: 04/14/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -33,6 +33,11 @@ Key use cases include:
 
 * **Marketing and Personalization:** Generate personalized content and recommendations at scale.
 
+> [!TIP]
+> If your batch jobs are so large that you are hitting the enqueued token limit even after maxing out the quota for your deployment, certain regions now support a new feature that allows you to queue multiple batch jobs with exponential backoff. 
+>
+>Once your enqueued token quota is available, the next batch job can be created and kicked off automatically.To learn more, see [**automating retries of large batch jobs with exponential backoff**](#queueing-batch-jobs).
+
 > [!IMPORTANT]
 > We aim to process batch requests within 24 hours; we don't expire the jobs that take longer. You can [cancel](#cancel-batch) the job anytime. When you cancel the job, any remaining work is cancelled and any already completed work is returned. You'll be charged for any completed work.
 >
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理に関する新しいヒントの追加"
}
```

### Explanation
この変更は、`batch.md` ファイルにバッチ処理に関する新しい情報を追加するためのマイナーな更新です。主な変更点として、以下の内容があります。

1. **日付の更新**: ドキュメントの日付が `01/14/2025` から `04/14/2025` に更新されました。
   
2. **バッチ処理のヒント追加**: 新しいヒントが2つ追加されています。
   - 最初のヒントでは、大きなバッチジョブに対してエンキューされたトークン制限に引っかかる場合の対処法について説明しており、特定のリージョンで新しい機能を使って、指数バックオフを伴う複数のバッチジョブをエンキューできることを紹介しています。この情報は、ユーザーが長時間のバッチ処理に対して効率的に対応できるようサポートします。
   - もう一つの重要なヒントでは、バッチリクエストは24時間以内に処理されることを目指しているが、処理が長引く場合にジョブをキャンセルでき、その際に完了した作業に対して料金が発生することが明示されています。

これらの更新により、ユーザーはバッチ処理に関する重要な情報をより良く理解し、実装の際の指針を得ることができます。

## articles/ai-services/openai/how-to/code-interpreter.md{#item-95efbd}

<details>
<summary>Diff</summary>
````diff
@@ -138,7 +138,7 @@ assistant = client.beta.assistants.create(
   instructions="You are an AI assistant that can write code to help answer math questions.",
   model="gpt-4-1106-preview",
   tools=[{"type": "code_interpreter"}],
-  tool_resources={"code interpreter":{"file_ids":[file.id]}}
+  tool_resources={"code_interpreter":{"file_ids":[file.id]}}
 )
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ツールリソースのキー名の修正"
}
```

### Explanation
この変更は、`code-interpreter.md` ファイルにおけるコードの小規模な修正を示しています。具体的には、`tool_resources` オブジェクト内のキー名を `{"code interpreter"` から `{"code_interpreter"` に修正しました。この変更により、キー名が一貫性を持ち、正しい形式で使用されることになります。

この修正は1行の追加と1行の削除から構成されており、コードの動作に影響を与えることなく、より適切な命名規則を適用するものです。これにより、コードの可読性が向上し、今後の修正やメンテナンスが容易になることが期待されます。

## articles/ai-services/openai/how-to/stored-completions.md{#item-ccc7e6}

<details>
<summary>Diff</summary>
````diff
@@ -24,15 +24,11 @@ Support first added in `2024-10-01-preview`, use `2025-02-01-preview` or later f
 
 ### Deployment type
 
-Currently only `Standard` model deployments support stored completions.
+Stored completions is supported for all Azure OpenAI Deployment types: standard, global, datazone, and provisioned.
 
 ### Model & region availability
 
-| **Region**     | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-05-13**  | **gpt-4o-mini**, **2024-07-18**   |
-|:---|:---:|:---:|:---:|:---:|:---:|
-| Sweden Central | ✅ | ✅  | ✅ | ✅ | ✅ |
-| North Central US | - | - | ✅ | - | - |
-| East US 2 | - | - | ✅ | - | - |
+As long as you're using the Chat Completions API for inferencing, you can leverage stored completions. It is supported for all Azure OpenAI models, and in all supported regions (including global-only regions).
 
 ## Configure stored completions
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ストレージ完了サポートの範囲の拡大"
}
```

### Explanation
この変更は、`stored-completions.md` ファイルにおいてストレージ完了機能に関する内容を更新するためのマイナーな改訂です。主な変更点は以下の通りです。

1. **デプロイメントタイプの拡大**: ストレージ完了機能が以前は「Standard」モデルデプロイメントのみをサポートしていましたが、現在はすべての Azure OpenAI デプロイメントタイプ（標準、グローバル、データゾーン、およびプロビジョンド）がサポートされることを明示しています。これにより、ユーザーはより広範囲なデプロイメントオプションでストレージ完了機能を利用できるようになります。

2. **モデルと地域の利用可能性についての説明の簡潔化**: ストレージ完了機能がChat Completions APIを使用した推論において全てのAzure OpenAIモデルおよび全ての対応地域（グローバル専用地域を含む）でサポートされていることが強調されています。これにより、ユーザーがシステムの導入や利用を検討する際の理解が容易になります。

全体として、この変更はユーザーに対してストレージ完了機能の利用可能性を明確にし、導入の幅を広げることを目的としています。

## articles/ai-services/openai/includes/batch/batch-python.md{#item-3121c2}

<details>
<summary>Diff</summary>
````diff
@@ -201,6 +201,8 @@ print(batch_response.model_dump_json(indent=2))
 }
 ```
 
+If your batch jobs are so large that you are hitting the enqueued token limit even after maxing out the quota for your deployment, certain regions now support a new [fail fast](#queueing-batch-jobs) feature that allows you to queue multiple batch jobs with exponential backoff so once one large batch job completes the next can be kicked off automatically. To learn more about what regions support this feature and how to adapt your code to take advantage of it, see [queuing batch jobs](#queueing-batch-jobs).  
+
 ## Track batch job progress
 
 Once you have created batch job successfully you can monitor its progress either in the Studio or programatically. When checking batch job progress we recommend waiting at least 60 seconds in between each status call.
@@ -620,4 +622,124 @@ else:
   "has_more": false,
   "last_id": "batch_6287485f-50fc-4efa-bcc5-b86690037f43"
 }
-```
\ No newline at end of file
+```
+
+## Queueing batch jobs
+
+If your batch jobs are so large that you are hitting the enqueued token limit even after maxing out the quota for your deployment, certain regions now support a new fail fast feature that allows you to queue multiple batch jobs with exponential backoff. Once one large batch job completes and your enqueued token quota is once again available, the next batch job can be created and kicked off automatically. 
+
+**Old behavior:**
+
+1. Large Batch job/s already running and using all available tokens for your deployment.
+2. New batch job submitted.
+3. New batch job goes into validation phase which can last up to a few minutes.
+4. Token count for new job is checked against currently available quota.
+5. New batch job fails with error reporting token limit exceeded.
+
+**New behavior:**
+
+1. Large Batch job/s already running and using all available tokens for your deployment
+2. New batch job submitted
+3. Approximate token count of new job immediately compared against currently available batch quota job fails fast allowing you to more easily handle retries programmatically.
+
+### Region support
+
+The following regions support the new fail fast behavior:
+
+- australiaeast
+- eastus
+- germanywestcentral
+- italynorth
+- northcentralus
+- polandcentral
+- swedencentral
+- eastus2
+- westus
+
+The code below demonstrates the basic mechanics of handling the fail fast behavior to allow automating retries and batch job queuing with exponential backoff.
+
+Depending on the size of your batch jobs you may need to greatly increase the `max_retries` or alter this example further.
+
+```python
+import time
+from openai import BadRequestError
+
+max_retries = 10
+retries = 0
+initial_delay = 5
+delay = initial_delay
+
+while True:
+    try:
+        batch_response = client.batches.create(
+            input_file_id=file_id,
+            endpoint="/chat/completions",
+            completion_window="24h",
+        )
+        
+        # Save batch ID for later use
+        batch_id = batch_response.id
+        
+        print(f"✅ Batch created successfully after {retries} retries")
+        print(batch_response.model_dump_json(indent=2))
+        break  
+        
+    except BadRequestError as e:
+        error_message = str(e)
+        
+        # Check if it's a token limit error
+        if 'token_limit_exceeded' in error_message:
+            retries += 1
+            if retries >= max_retries:
+                print(f"❌ Maximum retries ({max_retries}) reached. Giving up.")
+                raise
+            
+            print(f"⏳ Token limit exceeded. Waiting {delay} seconds before retry {retries}/{max_retries}...")
+            time.sleep(delay)
+            
+            # Exponential backoff - increase delay for next attempt
+            delay *= 2
+        else:
+            # If it's a different error, raise it immediately
+            print(f"❌ Encountered non-token limit error: {error_message}")
+            raise
+```
+
+**Output:**
+
+```console
+⏳ Token limit exceeded. Waiting 5 seconds before retry 1/10...
+⏳ Token limit exceeded. Waiting 10 seconds before retry 2/10...
+⏳ Token limit exceeded. Waiting 20 seconds before retry 3/10...
+⏳ Token limit exceeded. Waiting 40 seconds before retry 4/10...
+⏳ Token limit exceeded. Waiting 80 seconds before retry 5/10...
+⏳ Token limit exceeded. Waiting 160 seconds before retry 6/10...
+⏳ Token limit exceeded. Waiting 320 seconds before retry 7/10...
+✅ Batch created successfully after 7 retries
+{
+  "id": "batch_1e1e7b9f-d4b4-41fa-bd2e-8d2ec50fb8cc",
+  "completion_window": "24h",
+  "created_at": 1744402048,
+  "endpoint": "/chat/completions",
+  "input_file_id": "file-e2ba4ccaa4a348e0976c6fe3c018ea92",
+  "object": "batch",
+  "status": "validating",
+  "cancelled_at": null,
+  "cancelling_at": null,
+  "completed_at": null,
+  "error_file_id": "",
+  "errors": null,
+  "expired_at": null,
+  "expires_at": 1744488444,
+  "failed_at": null,
+  "finalizing_at": null,
+  "in_progress_at": null,
+  "metadata": null,
+  "output_file_id": "",
+  "request_counts": {
+    "completed": 0,
+    "failed": 0,
+    "total": 0
+  }
+}
+```
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "バッチジョブのキューイングとフェイルファースト機能の追加"
}
```

### Explanation
この変更は、`batch-python.md` ファイルにおいて新たな機能を追加し、バッチジョブの管理に関する重要な情報を提供するための大規模な更新です。主な内容は以下の通りです。

1. **バッチジョブのキューイング**: ユーザーがバッチジョブを送信する際、高負荷のジョブが実行中でトークンの制限に達している場合でも、新しい「フェイルファースト」機能が導入されました。この機能により、エクスポネンシャルバックオフを使って複数のバッチジョブをキューイングでき、前のジョブが完了すると次のジョブが自動的に開始されます。

2. **動作の説明**: 新しい動作の流れが明記されており、特にトークン制限を超えた場合の処理において、すぐに現在のバッチクオータと新しいジョブの大体のトークン数を比較することが強調されています。

3. **地域サポート**: この新しいフェイルファースト機能に対応する地域のリストが追加され、ユーザーはどの地域でこの機能を利用できるかを容易に確認できます。

4. **コード例の追加**: フェイルファースト機能を利用して自動的にリトライとバッチジョブのキューイングを操作する方法を示す Python コード例が追加されており、ユーザーがこの機能を実装する際に役立つ具体的な手順が提供されています。

これにより、ユーザーは高負荷のバッチ処理をより効果的に管理できるようになり、システムの効率が向上することが期待されます。


