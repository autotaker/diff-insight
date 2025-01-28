---
date: '2025-01-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9cc44af...MicrosoftDocs:2067774
summary: プロンプトキャッシングに関する情報が更新され、o1シリーズモデルのサポートが追加されました。また、キャッシング対象メッセージとして「開発者のメッセージ」が含まれるようになり、情報の保持範囲が拡大しました。特に、これによりAIサービスの使いやすさが向上し、開発者は新しいモデルを活用しやすくなり、より多様なユースケースに対応できるようになりました。ユーザーはキャッシング機能をより効果的に利用でき、パフォーマンスの向上やコスト削減が期待されます。この更新は、大規模なプロジェクトや多くのリクエストを扱うアプリケーションにとって特に有益です。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9cc44af...MicrosoftDocs:2067774){target="_blank"}

<format>
# Highlights
「プロンプトキャッシング」に関する情報が更新され、o1シリーズモデルに対するサポートが追加されました。さらに、キャッシングの対象メッセージが「開発者のメッセージ」を含むように拡張され、利用可能なデータの範囲が広がりました。

## New features
- o1シリーズモデルのサポートが追加。
- キャッシング対象メッセージの範囲に「開発者のメッセージ」を含むように変更。

## Breaking changes
- 特になし。

## Other updates
- 文書全体の整理と使い方の推奨が示されている点。

# Insights
今回の変更により、AIサービスにおけるプロンプトキャッシングの使用性が向上しました。特に、o1シリーズモデルのサポート追加は、新しいモデルを使用したい開発者にとって重要なアップデートです。また、キャッシングの範囲に「開発者のメッセージ」を含めることで、プロンプトキャッシング機能を活用する際に保持できる情報が増え、より多様なユースケースに対応可能になりました。

この更新は、開発者がAIサービス機能を活用する際の選択肢を広げ、より包括的なアプローチを提供します。これにより、開発者はより効果的にキャッシング機能を活用し、パフォーマンスの向上やコストの削減を図ることができます。特に大規模なプロジェクトや多くのリクエストを必要とするアプリケーションにおいて、この機能強化は大いに役立つでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [prompt-caching.md](#item-1631df) | minor update | プロンプトキャッシングに関する情報の更新 | modified | 5 | 5 | 10 | 


# Modified Contents
## articles/ai-services/openai/how-to/prompt-caching.md{#item-1631df}

<details>
<summary>Diff</summary>
````diff
@@ -75,16 +75,16 @@ A single character difference in the first 1,024 tokens will result in a cache m
 
 ## What is cached?
 
-The o1-series models are text only and don't support system messages, images, tool use/function calling, or structured outputs. This limits the efficacy of prompt caching for these models to the user/assistant portions of the messages array which are less likely to have an identical 1024 token prefix.
+o1-series models feature support varies by model. For more details, see our dedicated [reasoning models guide](./reasoning.md). 
 
 Prompt caching is supported for:
 
 |**Caching supported**|**Description**|**Supported models**|
 |--------|--------|--------|
-| **Messages** | The complete messages array: system, user, and assistant content | `gpt-4o`<br/>`gpt-4o-mini`<br/>`gpt-4o-realtime-preview` (version 2024-12-17) |
-| **Images** | Images included in user messages, both as links or as base64-encoded data. The detail parameter must be set the same across requests. | `gpt-4o`<br/>`gpt-4o-mini` |
-| **Tool use** | Both the messages array and tool definitions. | `gpt-4o`<br/>`gpt-4o-mini`<br/>`gpt-4o-realtime-preview` (version 2024-12-17) |
-| **Structured outputs** | Structured output schema is appended as a prefix to the system message. | `gpt-4o`<br/>`gpt-4o-mini` |
+| **Messages** | The complete messages array: system, developer, user, and assistant content | `gpt-4o`<br/>`gpt-4o-mini`<br/>`gpt-4o-realtime-preview` (version 2024-12-17) <br> `o1` (version 2024-12-17) |
+| **Images** | Images included in user messages, both as links or as base64-encoded data. The detail parameter must be set the same across requests. | `gpt-4o`<br/>`gpt-4o-mini` <br> `o1` (version 2024-12-17)  |
+| **Tool use** | Both the messages array and tool definitions. | `gpt-4o`<br/>`gpt-4o-mini`<br/>`gpt-4o-realtime-preview` (version 2024-12-17) <br> `o1` (version 2024-12-17) |
+| **Structured outputs** | Structured output schema is appended as a prefix to the system message. | `gpt-4o`<br/>`gpt-4o-mini` <br> `o1` (version 2024-12-17) |
 
 To improve the likelihood of cache hits occurring, you should structure your requests such that repetitive content occurs at the beginning of the messages array.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトキャッシングに関する情報の更新"
}
```

### Explanation
このコードの変更は、「プロンプトキャッシング」に関する情報を更新しています。具体的には、o1シリーズモデルのサポート内容に関して、「モデルごとの機能サポートの変動」を明記し、サポート対象のモデルリストにo1シリーズを追加しました。また、キャッシングの対象となるメッセージの内容を「開発者のメッセージ」を含むように拡張しました。これにより、プロンプトキャッシング機能を利用する際の利用可能なデータの範囲が広がり、より詳細な情報を提供しています。内容は全体的に整理され、使い方の推奨が示されています。


