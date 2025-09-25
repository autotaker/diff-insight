---
date: '2025-09-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:212d966...MicrosoftDocs:8d9466e
summary: この一連の変更では、主に3つのファイルに対するマイナーな更新と、gpt-5という新しいモデルの追加が行われました。これにより、AIエージェントの能力が向上し、インデクサーのスケジューリングに関する詳細情報が提供されます。新機能として、最新のOpenAIモデルを選択して検索エージェントで活用できるようになり、特にデータインデックスの管理が重要な業務に役立つ情報が追加されました。全体として、ユーザーはAIの最新技術を活かし、より効率的なシステム運用が期待できます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:212d966...MicrosoftDocs:8d9466e){target="_blank"}

# ハイライト
この一連の変更では、主に3つのファイルに対してマイナーな更新が行われ、gpt-5という新しいモデルが追加されました。これにより、AIエージェントの能力が向上し、インデクサーのスケジューリングに関する情報が詳述されています。

## 新しい機能
- `articles/search/search-agentic-retrieval-how-to-create.md`と`articles/search/search-agentic-retrieval-how-to-pipeline.md`に、gpt-5という最新モデルの導入が行われました。
- これにより、最新のOpenAIモデルまたはオープンソースモデルを選択して、検索エージェントで利用することが可能になります。

## 重要な変更
- 特定の破壊的な変更は行われていませんが、新しい情報が加わったことで既存の設定や理解に対する影響があるかもしれません。

## その他の更新
- `articles/search/search-howto-schedule-indexers.md`では、インデクサーの実行に関する新しい情報が追加されました。特に、メンテナンス中や復旧時のインデクサーの実行方法について詳しく説明されています。

# 洞察
これらの変更は、AzureやOpenAIモデルの利用を考慮しているユーザーにとって非常に有益です。gpt-5の追加により、さらに高性能なAIエージェントの開発が可能になりました。特に、最新のAI技術を検索エージェントやパイプラインに統合できるようになることで、ユーザーはより高精度かつ効率的な情報取得を実現できるようになります。

また、インデクサーの更新に関する情報は、特にデータインデックスの更新スケジュールを管理する必要がある業務に従事するユーザーにとって重要です。特に、壊れやすいスケジュールを持つシステムでのインデクサーの挙動を理解し、適切に対処するための指針を提供します。

今回の改定により、ユーザーはAIの最新トレンドを活かしつつ、より柔軟なシステム運用を目指すことができます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-agentic-retrieval-how-to-create.md](#item-310fbe) | minor update | 検索エージェント型情報取得のための新しいモデルの追加 | modified | 1 | 0 | 1 | 
| [search-agentic-retrieval-how-to-pipeline.md](#item-1ad1c3) | minor update | パイプラインにおける新しいモデルの追加 | modified | 1 | 0 | 1 | 
| [search-howto-schedule-indexers.md](#item-d57e7b) | minor update | インデクサーの実行に関する新しい情報の追加 | modified | 3 | 1 | 4 | 


# Modified Contents
## articles/search/search-agentic-retrieval-how-to-create.md{#item-310fbe}

<details>
<summary>Diff</summary>
````diff
@@ -64,6 +64,7 @@ Use Azure OpenAI or an equivalent open source model:
 + `gpt-4.1`
 + `gpt-4.1-nano`
 + `gpt-4.1-mini`
++ `gpt-5`
 
 ## Configure access
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索エージェント型情報取得のための新しいモデルの追加"
}
```

### Explanation
この変更では、`articles/search/search-agentic-retrieval-how-to-create.md`というファイルにおいて、Azure OpenAIまたは同等のオープンソースモデルとして使用可能な新しいモデル`gpt-5`が追加されました。この更新により、利用できるモデルの選択肢が広がり、ユーザーは最新のモデルを利用して検索エージェント型情報取得を実現できるようになります。具体的には、追加された行は次のようになります:

```
+ `gpt-5`
```

この変更は、より多様なAIモデルを活用するために重要であり、ユーザー体験を向上させることが期待されます。

## articles/search/search-agentic-retrieval-how-to-pipeline.md{#item-1ad1c3}

<details>
<summary>Diff</summary>
````diff
@@ -47,6 +47,7 @@ Use one of the following chat completion models with your AI agent:
 + `gpt-4.1`
 + `gpt-4.1-nano`
 + `gpt-4.1-mini`
++ `gpt-5`
 
 ### Package version requirements
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "パイプラインにおける新しいモデルの追加"
}
```

### Explanation
この変更では、`articles/search/search-agentic-retrieval-how-to-pipeline.md`というファイルに対して、AIエージェントで使用できるチャット完了モデルのリストに新たに`gpt-5`が追加されました。これにより、ユーザーは最新のAIモデルをパイプラインに取り入れることができ、より高性能の検索エージェントを構築する選択肢が増えることになります。変更された部分は以下の通りです:

```
+ `gpt-5`
```

このアップデートは、AIエージェントの能力を向上させ、ユーザーに新たな機能を提供します。

## articles/search/search-howto-schedule-indexers.md{#item-d57e7b}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 03/11/2025
+ms.date: 09/24/2025
 ms.update-cycle: 365-days
 ---
 
@@ -126,6 +126,8 @@ Let’s consider an example to make this more concrete. Suppose we configure an
 
 1. The third execution is scheduled to start at 10:00 AM UTC, but at that time the previous execution is still running. This scheduled execution is then skipped. The next execution of the indexer won't start until 11:00 AM UTC.
 
+In rare cases, such as during maintenance or when recovering from transient conditions, multiple indexer runs are queued up. When this occurs, the indexer executes pending workloads sequentially within the scheduled window. For example, if an indexer is scheduled to run hourly and several runs were delayed or triggered on-demand, those queued up jobs will execute back-to-back until the queue is drained. These are not additional runs, but represent previously scheduled or requested executions. While this behavior is uncommon in most scenarios, the indexer is designed to eventually process all queued tasks to maintain consistency and data freshness.
+
 > [!NOTE]
 > If you have strict indexer execution requirements that are time-sensitive, you should consider using the [push API model](search-what-is-data-import.md#pushing-data-to-an-index) so you can control the indexing pipeline directly.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーの実行に関する新しい情報の追加"
}
```

### Explanation
この変更では、`articles/search/search-howto-schedule-indexers.md`というファイルに対して、インデクサーの実行に関する新しい情報が追加されました。具体的には、インデクサーがメンテナンス中や一時的な条件からの復旧時に、複数の実行がキューに積まれる可能性があることが説明されています。以下のような重要な内容が追加されました:

- インデクサーは、スケジュールされたウィンドウ内で保留中の作業を逐次的に実行することができるという説明。
- 時間に敏感なインデクサーの実行要件がある場合には、[プッシュAPIモデル](search-what-is-data-import.md#pushing-data-to-an-index)を使用することを検討すべきであるという推奨。

変更により、ユーザーはインデクサーの動作についてより深く理解できるようになり、特にスケジュールの管理についてのベストプラクティスを知ることができます。更新された日付も変更されており、最新の情報が反映されています。


