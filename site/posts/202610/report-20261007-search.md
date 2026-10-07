---
date: '2026-10-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6393a03...MicrosoftDocs:7fdfa16
summary: この差分のハイライトは、サーバーレスインデクサーに関するコスト情報の明確化です。誤解を招く可能性のあった表現を修正し、インデクサーの実行やインデックスへの文書の書き込みに関連するコストについての理解を向上させました。新機能は追加されていないものの、情報の正確性が改善されています。破壊的変更はなく、文書表現の修正により、ユーザーがコストについてより正確に理解できるようになります。また、外部サービスへの呼び出しやスキルセット実行に関連するコストについての言及も追加されています。この更新により、ユーザーは実際の費用を把握しやすくなり、予算管理が向上することが期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6393a03...MicrosoftDocs:7fdfa16){target="_blank"}

# ハイライト
この差分のハイライトは、サーバーレスインデクサーのコストに関する情報の明確化です。インデクサーの実行やインデックスへの文書の書き込みに関連するコストに関して、誤解を招く可能性のあった表現を修正しています。

## 新機能
特に新機能を追加したわけではありませんが、情報の正確性を向上させるための改善がなされています。

## 破壊的変更
破壊的な変更はありませんが、文書の表現が修正されたことで、利用者がコストについてより正確な理解を持つことができるようになります。

## その他の更新
外部サービスへの呼び出しやスキルセットの実行に関連したコストについての言及が追加されています。

# インサイト
このコード差分の目的は、Azure サーバーレスインデクサーを利用する際の費用に関する文書の透明性を向上させることにあります。以前のドキュメントでは、インデクサーの実行が無料であると誤解される可能性がありましたが、今回の変更により、インデクサー実行や文書の書き込みにはコストがかかることが明示されました。

特に注目すべきは、スキルを除いたインデクサーの実行と文書の書き込みにコストが発生する点が明確化され、さらにスキルセットの実行や外部サービスへの呼び出しの料金にも注意が払われていることです。この更新により、ユーザーは実際の費用を想定しやすくなり、予算管理がより正確に行えるようになると考えられます。

このような文書の更新は、ユーザーに対する透明性の向上だけでなく、Azure サービス全体の利用において、予期しないコストが発生するリスクを低減する効果も期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-indexer-high-density-serverless-overview.md](#item-2bc606) | minor update | サーバーレスインデクサーのコストに関する情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-indexer-high-density-serverless-overview.md{#item-2bc606}

<details>
<summary>Diff</summary>
````diff
@@ -174,7 +174,7 @@ Throughput can vary materially with document complexity and profile, chunking, t
 
 During the preview, Serverless indexers are designed to simplify ingestion for retrieval-augmented generation (RAG) and knowledge base scenarios:
 
-+ Indexer execution (excluding skills) is currently free. Writing documents to an index incurs a cost.
++ You [incur a cost](serverless-cost-optimization.md) for indexer execution (excluding skills) and writing documents to an index.
 
 + Skillset execution is billed the same way as on dedicated indexers. Calls to external services, such as the Azure OpenAI Embedding skill, GenAI Prompt skill, and Azure Content Understanding skill, are billed through the attached [Foundry or Azure AI services resource](cognitive-search-attach-cognitive-services.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスインデクサーのコストに関する情報の更新"
}
```

### Explanation
この変更は、サーバーレスインデクサーに関するドキュメントのコスト情報を明確にするためのマイナーな更新です。以前の文言では、インデクサーの実行は無料であると記載されていましたが、最新の更新では「インデクサー実行（スキルを除く）およびインデックスへの文書の書き込みにコストが発生します」と修正されました。この変更により、利用者はサーバーレスインデクサーを使用する際の費用についてより正確な情報を得ることができます。また、スキルセットの実行や外部サービスへの呼び出しの料金についても言及されており、より包括的な説明が提供されています。


