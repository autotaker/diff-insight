---
date: '2025-07-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dbb4e58...MicrosoftDocs:ebd05f8
summary: この差分は、Azure AI Languageの文書に関する小さな更新を示しています。新機能として、Conversational Language
  Understanding (CLU)のトレーニング構成が更新され、新しいREST APIのバージョンが今後利用可能になることが記載されています。これにより、ユーザーは最新機能をより活用しやすくなります。具体的には、`trainingConfigVersion
  2025-07-01-preview`が導入され、利用方法に関するリンクも追加されました。全体として、ユーザー体験を向上させるための重要なステップとなっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dbb4e58...MicrosoftDocs:ebd05f8){target="_blank"}

# ハイライト

この差分は、Azure AI Languageの最新情報に関する文書の小さな更新を示しています。新しい機能として、Conversational Language Understanding (CLU)のトレーニング構成が更新され、今後のリリースにおいて新たなREST APIのバージョンが利用可能となることが記載されました。これにより、ユーザーが最新の機能を活用しやすくなっています。

## 新機能

- 新しいConversational Language Understanding (CLU)のトレーニング構成が導入され、`trainingConfigVersion 2025-07-01-preview`としてREST APIを通じて利用可能になりました。
  
## 破壊的変更

- 特に破壊的な変更は記載されていません。

## その他の更新

- 日付が「2025年7月14日」に変更されました。
- 新しい機能の利用方法に関するリンクが追加されました。

# 洞察

今回の文書の更新は、Azure AI Languageサービスの利用を検討中または既に利用中のユーザーに向けた、コンテンツの質を向上させる重要なステップです。日付の更新によって、最新の情報がユーザーに届けられることが保証され、さらに新しいトレーニング構成がREST API経由で使用可能になる情報が追加されることで、開発者やデータサイエンティストに新しい選択肢を提供します。

`trainingConfigVersion 2025-07-01-preview`というタグは、今後の機能拡張やツールの使い勝手の向上を示しており、それによりAzureのAIサービスが進化し続けていることを示唆しています。このような更新は、特に新しい技術をいち早く取り入れたい企業にとって、競争力を維持するための手段として非常に意義があります。

リンクの追加によって、ユーザーは新機能の具体的な使い方を素早く理解することが可能になり、これによりAzure AI Languageの利用フローはさらに円滑になるでしょう。このように細やかなドキュメントの更新は、ユーザー体験を向上させるための重要な要素であり、Microsoftが製品改善に注力していることを実感させます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [whats-new.md](#item-69b272) | minor update | 2025年7月の新機能に関する情報の更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: whats-new
-ms.date: 07/09/2025
+ms.date: 07/14/2025
 ms.author: lajanuar
 ---
 
@@ -16,7 +16,7 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 
 ## June 2025
 
-* A new version of the Conversational Language Understanding (CLU) training configuration, aimed at minimizing overpredictions of the [None intent](conversational-language-understanding/concepts/none-intent.md)—particularly in multilingual contexts—is now supported in [REST API version 2025-15-05-preview](/rest/api/language/analyze-conversations/analyze-conversations?view=rest-language-2025-05-15-preview&preserve-view=true).
+* A new version of the Conversational Language Understanding (CLU) training configuration, aimed at minimizing overpredictions of the [None intent](conversational-language-understanding/concepts/none-intent.md)—particularly in multilingual contexts—is now available via the REST API using **trainingConfigVersion 2025-07-01-preview**. For more information, *see* [Train your model: request body data](conversational-language-understanding/how-to/train-model.md?tabs=rest-api#request-body).
 
 * The [Build your conversational agent](https://github.com/Azure-Samples/Azure-Language-OpenAI-Conversational-Agent-Accelerator) accelerator project is updated to include a new routing strategy—**TRIAGE_AGENT**. This strategy uses an agent hosted on Azure AI Foundry Agent Service. It utilizes Conversational Language Understanding (CLU) and Custom Question Answering (CQA) as tools to triage user intent for downstream agent routing. Additionally, these tools help deliver precise answers to specific questions. For more information, *see* [TechCommunity Blog Post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-azure-ai-language-new-features-to-accelerate-your-agent-development/4415216)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "2025年7月の新機能に関する情報の更新"
}
```

### Explanation
この変更は、Azure AI Languageの「whats-new.md」ドキュメントの更新に関連しています。主に、日付と新機能に関する情報が修正されました。具体的には、日付が「2025年7月14日」に変更され、新しいConversational Language Understanding (CLU)のトレーニング構成が、REST APIを通じて「trainingConfigVersion 2025-07-01-preview」で利用可能であることが追記されました。また、利用方法に関するリンクも追加され、ユーザーが最新の機能を理解しやすくなっています。これにより、ドキュメントは最新の状態を反映し、ユーザーが新しい機能を利用するための情報が簡単に見つかるようになります。


