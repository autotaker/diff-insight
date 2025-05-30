---
date: '2025-05-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:64fe7dc...MicrosoftDocs:768223a
summary: この差分では、言語サービスの概要ドキュメントにいくつかのマイナーな更新が行われました。主な変更点は、新しいエージェント機能の追加と文書の日付の更新です。具体的には、「意図ルーティングエージェント」と「正確な質問回答エージェント」が新たに追加され、ユーザーの意図を正確に判断し、特定の質問に対する的確な回答を提供する能力が強化されています。また、文書の日付が2025年3月5日から2025年5月28日に更新され、最新の情報が反映されています。この変更にはブレイキングチェンジは含まれていません。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:64fe7dc...MicrosoftDocs:768223a){target="_blank"}

# Highlights
この差分では、言語サービスの概要ドキュメントに対して数点のマイナーな更新が行われています。主なポイントとして、新しいエージェント機能の追加と日付の更新があります。

## New features
- **意図ルーティングエージェント**と**正確な質問回答エージェント**の詳細が追加されました。これらはユーザーの意図を的確に判断し、特定の質問に対する正しい答えを導き出す能力を持つエージェントです。

## Breaking changes
この変更には特にブレイキングチェンジは含まれていません。

## Other updates
- 文書の日付が「2025年3月5日」から「2025年5月28日」に更新されました。

# Insights
今回の更新で追加されたエージェント機能は、言語サービスの利用において大きな進化を示します。ユーザーの意図を正確に把握し、適切な回答を提供することができるこれらのエージェントは、特に自然言語処理やチャットボットなどのアプリケーションで重要な役割を果たします。

「意図ルーティングエージェント」は、ユーザーの入力を解析し、最も適した次のステップを導き出すもので、これは特に複雑なインタラクション管理において有用です。例えば、ユーザーが特定のサポートクエリを入力したとき、そのクエリを適切なサポートチームや情報源にルーティングすることで、より効率的に問題解決を行います。

一方「正確な質問回答エージェント」は、ユーザーの質問に対して正確かつ迅速に答えるために設計されています。このエージェントの存在により、情報検索の効率が向上し、例えばFAQセクションにおいて瞬時に回答を提供することが可能になります。

これらの追加が示すのは、今後の言語サービスがよりインテリジェントでユーザーエクスペリエンスを向上させる方向に進化しているということです。最新の日付への更新も、ドキュメントが最新の情報を反映していることを示しており、ユーザーは安心して最新の機能にアクセスし利用することができます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [overview.md](#item-f138b4) | minor update | 言語サービスの概要の更新 | modified | 2 | 1 | 3 | 


# Modified Contents
## articles/ai-services/language-service/overview.md{#item-f138b4}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 03/05/2025
+ms.date: 05/28/2025
 ms.author: lajanuar
 ---
 
@@ -24,6 +24,7 @@ The Language service also provides several new features as well, which can eithe
 * Customizable, which means you train an AI model using our tools to fit your data specifically.
 
 Language features are also utilized in [agent templates](https://github.com/azure-ai-foundry/foundry-samples/tree/main/samples/agent-catalog):
+
 * [Intent routing agent](https://github.com/azure-ai-foundry/foundry-samples/tree/main/samples/agent-catalog/msft-agent-samples/foundry-agent-service-sdk/intent-routing-agent) detects user intent and provides exact answering. Perfect for deterministically intent routing and exact question answering with human controls.
 * [Exact question answering agent](https://github.com/azure-ai-foundry/foundry-samples/tree/main/samples/agent-catalog/msft-agent-samples/foundry-agent-service-sdk/exact-qna-agent) answers high-value predefined questions deterministically to ensure consistent and accurate responses.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サービスの概要の更新"
}
```

### Explanation
この更新は、`articles/ai-services/language-service/overview.md`ファイルに対するもので、いくつかの重要な変更が加えられました。主な変更点は、文書の日付が「2025年3月5日」から「2025年5月28日」に更新されたことです。また、新しいエージェント機能が追加されました。「意図ルーティングエージェント」と「正確な質問回答エージェント」の詳細が加わっており、これらのエージェントはユーザーの意図を検出し、特定の質問に正確に回答する能力を持っています。この変更により、ユーザーは最新の機能やサービスをよりよく理解できるようになります。


