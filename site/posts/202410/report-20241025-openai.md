---
date: '2024-10-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f8a58ce...MicrosoftDocs:edd8070
summary: この変更は、Azure OpenAIリソースのバッチジョブ管理に関するドキュメンテーションを向上させ、ユーザーの使いやすさを高めることを目的としています。新たに、バッチジョブを自動取得するためのPythonコード例が追加され、ページネーションのサポートが強調されています。また、REST
  APIの説明では、`has_more`というブール値が返されることが明記され、バッチジョブリストの扱いがより直感的になります。これらの改善により、開発者は効率的にプログラムをセットアップし、ジョブを効果的に処理できるようになります。全体として、開発者エクスペリエンスの向上が期待されます。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f8a58ce...MicrosoftDocs:edd8070){target="_blank"}

# ハイライト

このコードの変更は、Azure OpenAIリソースのバッチジョブを管理するためのドキュメンテーションを改善することにより、ユーザーの使いやすさを向上させるものです。

## 新機能
- バッチジョブのリストを自動的に取得するためのPythonコード例が追加され、ページネーションを含む全てのジョブを取得できるようになりました。
- REST APIの説明に、ページネーションがサポートされていること、及びその際に`has_more`ブール値が返されることが明記されました。

## 破壊的変更
- 特別な破壊的変更は含まれていませんが、ドキュメンテーションの理解が必要です。

## その他の更新
- バッチリストAPIの効率と明確性に関する微細な改善。

# 洞察

今回の変更は、Azure OpenAIプラットフォームでバッチジョブを利用する開発者にとって非常に役立つものです。特に、バッチ処理は大量のデータを効率的に処理するための一般的な手法であり、これをサポートするためのPythonサンプルコードの追加は、開発者がプログラムを迅速にセットアップし、実行するための素晴らしいリソースとなります。ページネーションをサポートすることで、開発者はすべてのジョブをシンプルに取得・処理することが可能になります。

さらに、REST APIの改善により、API利用者はより直感的にバッチジョブリストを扱えます。新たに追加された`has_more`プロパティにより、リクエストがどの程度進んでいるかを知ることが容易になり、それに応じた処理に変更を加えることができます。これにより、システムのパフォーマンス向上やエラー削減に繋がります。

これらの改善は全体として、開発者エクスペリエンスを向上させるものであり、より効率的で効果的な開発を推進すると考えられます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [batch-python.md](#item-3121c2) | minor update | バッチジョブのリスト方法の更新 | modified | 16 | 1 | 17 | 
| [batch-rest.md](#item-bcccd9) | minor update | バッチジョブリストAPIの改善 | modified | 3 | 1 | 4 | 


# Modified Contents
## articles/ai-services/openai/includes/batch/batch-python.md{#item-3121c2}

<details>
<summary>Diff</summary>
````diff
@@ -401,12 +401,27 @@ client.batches.cancel("batch_abc123") # set to your batch_id for the job you wan
 
 ### List batch
 
-List all batch jobs for a particular Azure OpenAI resource.
+List batch jobs for a particular Azure OpenAI resource.
 
 ```python
 client.batches.list()
 ```
 
+List methods in the Python library are paginated.
+
+To list all jobs:
+
+```python
+all_jobs = []
+# Automatically fetches more pages as needed.
+for job in client.batches.list(
+    limit=20,
+):
+    # Do something with job here
+    all_jobs.append(job)
+print(all_jobs)
+```
+
 ### List batch (Preview)
 
 Use the REST API to list all batch jobs with additional sorting/filtering options.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチジョブのリスト方法の更新"
}
```

### Explanation
この変更は、Azure OpenAI リソースのバッチジョブをリストする際のPythonコードのドキュメンテーションを改善するためのものであり、16行が追加され、1行が削除されました。具体的には、バッチジョブのリストを取得する関連情報が強化され、ページネーションの方法や全ジョブを取得するためのサンプルコードが追加されています。また、サンプルコードは、ユーザーが複数ページのジョブを自動的に取得できるようにすることで、実用性が向上しています。変更の結果、ユーザーはバッチ処理機能をより簡単に理解し、利用できるようになります。

## articles/ai-services/openai/includes/batch/batch-rest.md{#item-bcccd9}

<details>
<summary>Diff</summary>
````diff
@@ -245,13 +245,15 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches/{batch_id}/cance
 
 ### List batch
 
-List all existing batch jobs for a given Azure OpenAI resource.
+List existing batch jobs for a given Azure OpenAI resource.
 
 ```http
 curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024-10-21 \
   -H "api-key: $AZURE_OPENAI_API_KEY" 
 ```
 
+The list API call is paginated. The response contains a boolean `has_more` to indicate when there are more results to iterate through.
+
 <a id="List"></a>
 
 ### List batch (Preview)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチジョブリストAPIの改善"
}
```

### Explanation
このコードの変更では、Azure OpenAIリソースに関連するバッチジョブをリストするためのREST APIのドキュメンテーションが改善されました。具体的には、3行が追加され、1行が削除されており、バッチジョブのリストを表示するための説明が明確になっています。更新された内容には、リストAPIコールがページネーションをサポートし、結果がさらにある場合には`has_more`というブール値が返されることが記載されています。この改善により、ユーザーはAPIの動作についての理解を深めやすくなり、より効果的にバッチジョブを管理できるようになります。


