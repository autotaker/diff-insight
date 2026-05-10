---
date: '2026-05-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:68b7656...MicrosoftDocs:2cf0ebe
summary: この変更は、FoundryツールエージェントとAzure Languageサービスのドキュメントにおけるマイナーな修正を含んでいます。主な目的は情報の簡素化と可読性の向上であり、特にエージェントの作成方法や新機能の説明に対するリンクの削除に焦点を当てています。新機能や破壊的変更は特にありませんが、冗長な説明の削除やテキストの簡素化が行われ、ユーザーが情報をより直感的に理解できるようになっています。これにより、全体的なドキュメントの品質向上とユーザーエクスペリエンスの改善を図っています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:68b7656...MicrosoftDocs:2cf0ebe){target="_blank"}

# ハイライト
この変更は、FoundryツールエージェントとAzure Languageサービスのドキュメントにおけるマイナーな修正を含んでいます。情報の簡素化と可読性の向上を目的とした変更であり、特にエージェントの作成方法と新機能の説明に対するリンクの削除に集中しています。

## 新機能
特に新機能の追加はありません。

## 破壊的変更
特に破壊的な変更はありません。

## その他の更新
- Foundryツールエージェントの文書から冗長な説明を削除し、簡潔な表現に置き換え。
- Azure Languageサービスの「新機能」の一部からリンクを削除し、テキストの簡素化を実施。

# インサイト
このドキュメントの変更は、ユーザーがより直感的に情報を理解できるようにすることを意図しています。具体的には、Foundryツールエージェントの作成方法の説明が冗長であったため、ユーザーにエージェント作成の手順を理解しやすくするために文を端的に修正しています。特に、元々は「正確な質問応答エージェントテンプレートから作成することに加えて」という冗長な部分を「あなたのCQAプロジェクトから直接エージェントを作成できます」と簡略化しました。これにより、ユーザーが無駄な説明に煩わされず、必要な情報だけに集中できるようになっています。

また、Azure Languageサービスに関する「新機能」セクションの変更では、特に「Exact question answering」の項目からリンクを削除しています。これも、文脈上、リンクが必須でない場合に情報を集中させ、ユーザーの視線を分散させない工夫です。結果として、情報が簡素に保たれ、ユーザーが読みやすくなっています。これらの変更は、全体的なドキュメントの品質向上に寄与し、ユーザーエクスペリエンスを高める意図が明確です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [foundry-tools-agents.md](#item-7b932c) | minor update | Foundryツールエージェントに関する修正 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-69b272) | minor update | 新しいエージェントテンプレートに関する修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/language-service/concepts/foundry-tools-agents.md{#item-7b932c}

<details>
<summary>Diff</summary>
````diff
@@ -136,7 +136,7 @@ The agent combines Foundry Agent Service capabilities with [**Custom Question An
 
 The agent works well for scenarios where answer accuracy is important, such as customer service, help desk operations, or compliance information delivery.
 
-In addition to creating the agent from the exact question answering agent template in Agent Catalog, you can also create the agent directly from your CQA project in the Foundry portal. For more information, see [Create and deploy a CQA agent](../question-answering/how-to/deploy-agent.md).
+You can also create the agent directly from your CQA project in the Foundry portal. For more information, see [Create and deploy a CQA agent](../question-answering/how-to/deploy-agent.md).
 
 ### Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Foundryツールエージェントに関する修正"
}
```

### Explanation
このコードの変更は、Foundryツールエージェントについてのドキュメントの一部を修正したものです。具体的には、エージェントを作成する方法に関する説明を簡略化しています。元の文では「正確な質問応答エージェントテンプレートから作成することに加えて」と記載されていた部分が削除され、「あなたのCQAプロジェクトから直接エージェントを作成できます」と非常にシンプルになりました。この変更は、ドキュメントの可読性を向上させることを目的としており、情報をより明確に伝えることを意図しています。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -175,7 +175,7 @@ Stay informed about recent releases and enhancements designed to help you get th
 **New agent templates**. Azure Language now supports the following agent templates:
 
 * [Intent routing](../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md): Detects user intent and provides precise answers, ideal for deterministic intent routing, and exact question answering with human oversight.
-* [Exact question answering](../agents/concepts/agent-catalog.md): Delivers consistent, accurate responses to high-value predefined questions through deterministic methods.
+* Exact question answering: Delivers consistent, accurate responses to high-value predefined questions through deterministic methods.
 
 **PII detection enhancements**. Azure Language introduces new customization and entity subtype features for PII detection:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいエージェントテンプレートに関する修正"
}
```

### Explanation
このコードの変更は、Azure Languageサービスの「新機能」セクションに関連する内容の修正です。具体的には、「エージェントテンプレート」のリストの1つである「Exact question answering」の前に、リンクが削除されました。元の文ではこの項目に対してリンクが提供されていましたが、修正後はリンクなしで直接説明が記載されるようになりました。この変更は、情報のコンパクトさを向上させ、情報をよりスムーズに読み取れるようにすることを目的としています。


