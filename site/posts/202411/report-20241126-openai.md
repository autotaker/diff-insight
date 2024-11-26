---
date: '2024-11-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:32f452e...MicrosoftDocs:9760ca7
summary: この差分の主な変更点は、Azure AI Studioのコンテンツフィルターに関するドキュメントの更新です。特に、間接攻撃に対するプロンプトシールドのデフォルト設定が変更され、「Groundedness」に関連する情報が新たに追加されました。ユーザーは、この新しい設定によりデフォルトのセキュリティがどのように提供されているかを再確認する必要があります。また、ドキュメントの埋め込みとフォーマットの要件が強調され、データの信頼性が重要であることが示されています。この更新により、ユーザーはAzure
  AI Studioをより効果的に活用できるようになることが期待されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:32f452e...MicrosoftDocs:9760ca7){target="_blank"}

<format>
# ハイライト

この差分の主な変更点は、Azure AI Studioのコンテンツフィルターに関するドキュメントの更新です。特に、「間接攻撃に対するプロンプトシールド」のデフォルト設定が変更され、「Groundedness*」に関連する情報が追加されています。

## 新機能

- 間接攻撃に対するプロンプトシールドのデフォルト設定に関する情報が更新されました。

## 破壊的な変更

- ありません。

## その他の更新

- Groundedness*に関するセクションに、ドキュメントの埋め込みとフォーマットの要件が追加されました。

# 洞察

今回の差分は、Azure AI Studioのコンテンツフィルター機能に関連するドキュメントを改訂することにより、ユーザーの理解を助けることを目的としています。

「間接攻撃に対するプロンプトシールド」のデフォルト設定が「オン」から「オフ」に変更されたことで、ユーザーはデフォルトでどのようなセキュリティが提供されているかを再認識する必要があります。これにより、ユーザーが自身の環境に応じて適切なフィルター設定を選択するための意識を促します。

また、「Groundedness*」に関するドキュメントの埋め込みとフォーマットの必要性が明記されたことにより、データの信頼性と整合性を保証する重要性が強調されています。この更新は、AIモデルがどのようなデータソースを参照し、どのように情報を表示するべきかについて、ユーザーに明確なガイドラインを提供します。

ドキュメントのクリアさと適用性を高めることで、ユーザーがAzure AI Studioをより効果的に利用できるようになることが期待されます。改訂された内容は、ルールや設定についての理解を深め、より安全で信頼できるAI環境の構築をサポートします。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [content-filters.md](#item-6f0627) | minor update | コンテンツフィルターの設定の更新 | modified | 2 | 3 | 5 | 


# Modified Contents
## articles/ai-services/openai/how-to/content-filters.md{#item-6f0627}

<details>
<summary>Diff</summary>
````diff
@@ -38,12 +38,11 @@ You can configure the following filter categories in addition to the default har
 |Filter category  |Status |Default setting  |Applied to prompt or completion?  |Description  |
 |---------|---------|---------|---------|---|
 |Prompt Shields for direct attacks (jailbreak)     |GA|    On     |   User prompt      |   Filters / annotates user prompts that might present a Jailbreak Risk. For more information about annotations, visit [Azure OpenAI Service content filtering](/azure/ai-services/openai/concepts/content-filter?tabs=python#annotations-preview). |
-|Prompt Shields for indirect attacks  | GA| On| User prompt | Filter / annotate Indirect Attacks, also referred to as Indirect Prompt Attacks or Cross-Domain Prompt Injection Attacks, a potential vulnerability where third parties place malicious instructions inside of documents that the generative AI system can access and process. Required: [Document ](/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cuser-prompt%2Cpython-new#embedding-documents-in-your-prompt)formatting. |
+|Prompt Shields for indirect attacks  | GA| Off | User prompt | Filter / annotate Indirect Attacks, also referred to as Indirect Prompt Attacks or Cross-Domain Prompt Injection Attacks, a potential vulnerability where third parties place malicious instructions inside of documents that the generative AI system can access and process. Requires: [Document embedding and formatting](/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cuser-prompt%2Cpython-new#embedding-documents-in-your-prompt). |
 | Protected material - code |GA| On | Completion | Filters protected code or gets the example citation and license information in annotations for code snippets that match any public code sources, powered by GitHub Copilot. For more information about consuming annotations, see the [content filtering concepts guide](/azure/ai-services/openai/concepts/content-filter#annotations-preview) |
 | Protected material - text | GA| On | Completion | Identifies and blocks known text content from being displayed in the model output (for example, song lyrics, recipes, and selected web content).  |
-| Groundedness* | Preview |Off | Completion |Detects whether the text responses of large language models (LLMs) are grounded in the source materials provided by the users. Ungroundedness refers to instances where the LLMs produce information that is non-factual or inaccurate from what was present in the source materials. |
+| Groundedness* | Preview |Off | Completion |Detects whether the text responses of large language models (LLMs) are grounded in the source materials provided by the users. Ungroundedness refers to instances where the LLMs produce information that is non-factual or inaccurate from what was present in the source materials. Requires: [Document embedding and formatting](/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cuser-prompt%2Cpython-new#embedding-documents-in-your-prompt).|
 
-*Requires embedding documents in your prompt. [Read more](/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cuser-prompt%2Cpython-new#embedding-documents-in-your-prompt). 
 
 
 ## Configure content filters with Azure AI Studio
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルターの設定の更新"
}
```

### Explanation
このコードの変更は、Azure AI Studioでのコンテンツフィルター機能に関するドキュメントの更新に関係しています。具体的には、「間接攻撃に対するプロンプトシールド」のデフォルト設定が「オン」から「オフ」に変更され、その説明が強化されています。また、Groundedness*のセクションにも、ドキュメントの埋め込みとフォーマットが必要であることが追加されました。これにより、ユーザーが間接的な脅威に対する設定や、データの信頼性を高めるための要件を理解しやすくなっています。全体として、わずかな削除と追加を通じて、情報が明確化されました。


