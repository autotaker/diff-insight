---
date: '2025-12-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ccb0359...MicrosoftDocs:b8c3414
summary: この差分では、`agentic-retrieval-how-to-create-pipeline.md`というドキュメントのエージェントに関する指示文が軽微に修正されました。具体的には、ユーザーからの指示に関連する表現がより簡潔で明確なものに変更されました。変更は機能に影響を与えず、文書の可読性と指示の明確さを向上させることを目的としています。また、新機能や破壊的変更はなく、指示文の表現が改善されたことが主な更新点です。今回の修正は技術的な取り扱いに変化をもたらさないものの、ユーザーエクスペリエンスを向上させる重要な要素となります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ccb0359...MicrosoftDocs:b8c3414){target="_blank"}

# ハイライト

この差分では、`agentic-retrieval-how-to-create-pipeline.md`というドキュメント内のエージェントの指示文に関する軽微な修正が施されています。具体的な変更として、ユーザーからの指示に関連する表現が、より簡潔で明確なものへと修正されました。この修正は機能に影響を与えるものではなく、文書の可読性と指示の明確さを向上させることを目的としています。

## 新機能

この修正により新機能が追加されたわけではありません。

## 破壊的変更

本修正による破壊的な変更はありません。

## その他の更新

文書の指示文がより簡潔で明確になるように調整されたことが更新点として挙げられます。

# インサイト

今回の変更は主に言語の明確さと簡潔さを求めたものであり、技術的な取り扱いに変化をもたらすものではないため、システムの動作やエージェントの機能には影響を与えません。しかし、エージェントがユーザーとやりとりするときの指示がより明確になり、結果としてエージェントの応答の品質が向上する可能性があります。こうした細かい調整は、一見目に見えにくいですが、ユーザーエクスペリエンスを向上させ、特に大規模なユーザーベースを持つシステムにおいては重要な要素となることがあります。

このような軽微な修正は、技術的なドキュメントの改善の一環として理解することができ、今後のプロジェクトや他の文書のレビューにおいても同様の姿勢が求められるでしょう。文書がシンプルで効果的なコミュニケーションを促進するよう、一貫した努力が重要です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | エージェントの指示文の軽微な修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -386,7 +386,7 @@ For more information about this step, see [Quickstart: Create a new agent](/azur
 from azure.ai.projects.models import PromptAgentDefinition, MCPTool
 
 instructions = """
-You are a helpful assistant that must use the knowledge base to answer all the questions from the user. You must never answer from your own knowledge under any circumstances.
+You are a helpful assistant that must use the knowledge base to answer all the questions from user. You must never answer from your own knowledge under any circumstances.
 Every answer must always provide annotations for using the MCP knowledge base tool and render them as: `【message_idx:search_idx†source_name】`
 If you cannot find the answer in the provided knowledge base you must respond with "I don't know".
 """
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントの指示文の軽微な修正"
}
```

### Explanation
この修正は、`agentic-retrieval-how-to-create-pipeline.md`というファイルにおけるエージェントの指示文の修正を含んでいます。具体的には、元の文の「from the user」が「from user」に変更されました。この変更によって、文がより簡潔になり、エージェントがユーザーの質問に対してその知識ベースを利用する際の指示が明確になります。このような小さな修正は、文書全体の可読性を改善するのに寄与します。修正前のコード行と修正後のコード行は以下の通りです：

- 修正前: `You must never answer from your own knowledge under any circumstances.`
- 修正後: `You must never answer from your own knowledge under any circumstances.`

この変更は、機能には影響を与えず、文書の表現を洗練させるためのものです。


