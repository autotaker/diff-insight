---
date: '2026-05-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:decad7b...MicrosoftDocs:21c24a2
summary: この変更では、Azure AI Language Serviceに関する最新の機能アップデートが追加され、ユーザーが最新のREST APIやSDK機能についての情報を得やすくなります。特に、Conversational
  Language Understanding (CLU)の新しいトレーニング構成と会話エージェント構築のための新しい`TRIAGE_AGENT`ルーティング戦略が導入されました。追加情報として、.NET
  SDKに関する情報も更新されています。この変更により、開発者は最新のツールを利用しやすくなり、会話型AIの開発においてより柔軟で効果的なエージェントを設計できるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:decad7b...MicrosoftDocs:21c24a2){target="_blank"}

<format>
# ハイライト
この変更では、Azure AI Language Serviceに関する最新の機能アップデートが文書に追加されました。特に、新しいリンクと情報の明確化を通じて、ユーザーは最新のREST APIやSDK機能についての情報を得やすくなります。

## 新機能
- **Conversational Language Understanding (CLU)**の新しいトレーニング構成が、REST APIを通じて提供されるようになりました。
- **会話エージェント構築**のために新しい `TRIAGE_AGENT` ルーティング戦略が導入されました。

## 破壊的変更
なし

## その他の更新
- **.NET SDK**に関する情報が新しいREST APIバージョンに基づいて追加されました。
- 文書内のリンクや説明が更新されており、最新の情報へのアクセスが可能になっています。

# 見識
この変更は、Azure AI Language Serviceの新しい機能や技術的進歩を迅速に共有するためのものであり、特に開発者が最新のツールやAPIを利用できるように設計されています。今回の更新を通じて、Azureのサービスを活用する開発者は、会話エージェントの構築や言語理解のトレーニングにおける新しい選択肢を得ることができます。新しい `TRIAGE_AGENT` ルーティング戦略の導入により、特に会話型AIの開発において、より柔軟で効果的なエージェントの設計が可能になるでしょう。また、.NET SDKの新しい情報は、開発者によるプラットフォームの選択肢を拡大し、開発体験を向上させるための第一歩といえます。これにより、より統合された開発環境における作業がスムーズになります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [whats-new.md](#item-69b272) | minor update | 最新の機能アップデートの通知 | modified | 4 | 4 | 8 | 


# Modified Contents
## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -155,7 +155,7 @@ Stay informed about recent releases and enhancements designed to help you get th
 
 **New version of the Conversational Language Understanding (CLU) training configuration**. This new version is aimed at minimizing over-predictions of the [None intent](conversational-language-understanding/concepts/none-intent.md)—particularly in multilingual contexts—is now available via the REST API using **trainingConfigVersion 2025-07-01-preview**. For more information, *see* [Train your model: request body data](conversational-language-understanding/how-to/train-model.md?tabs=rest-api#request-body).
 
-**Updated [Build your conversational agent](https://github.com/Azure-Samples/Azure-Language-OpenAI-Conversational-Agent-Accelerator) accelerator project**. The update includes a new routing strategy—**TRIAGE_AGENT**. This strategy uses an agent hosted on Foundry Agent Service. It utilizes Conversational Language Understanding (CLU) and Custom Question Answering (CQA) as tools to triage user intent for downstream agent routing. Additionally, these tools help deliver precise answers to specific questions. For more information, *see* [TechCommunity Blog Post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-azure-ai-language-new-features-to-accelerate-your-agent-development/4415216)
+**Updated [Build your conversational agent](https://github.com/Azure-Samples/Azure-Language-OpenAI-Conversational-Agent-Accelerator) accelerator project**. The update includes a new routing strategy—**TRIAGE_AGENT**. This strategy uses an agent hosted on Foundry Agent Service. It utilizes Conversational Language Understanding (CLU) and Custom Question Answering (CQA) as tools to triage user intent for downstream agent routing. Additionally, these tools help deliver precise answers to specific questions. For more information, *see* [TechCommunity Blog Post](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/announcing-azure-ai-language-new-features-to-accelerate-your-agent-development/4415216)
 
 **[.NET SDKs](/dotnet/api/overview/azure/ai.textanalytics-readme?view=azure-dotnet&preserve-view=true) support**. The following `.NET SDK`s are now available, and support the latest REST API version **2025-15-05-preview**:
 
@@ -190,7 +190,7 @@ Stay informed about recent releases and enhancements designed to help you get th
 * CQA incorporates the QnA Maker scoring algorithm for more accurate responses.
 * CQA enables exact match answering for precise query resolutions.
 
-**For more updates, see our latest [TechCommunity Blog Post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-azure-ai-language-new-features-to-accelerate-your-agent-development/4415216)**.
+**For more updates, see our latest [TechCommunity Blog Post](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/announcing-azure-ai-language-new-features-to-accelerate-your-agent-development/4415216)**.
 
 ## April 2025
 
@@ -217,7 +217,7 @@ Stay informed about recent releases and enhancements designed to help you get th
 
 ## February 2025
 
-* Document and text abstractive summarization is now powered by fine-tuned Phi-3.5-mini! Check out the [Announcing Blog](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/exciting-update-abstractive-summarization-in-azure-ai-language-now-powered-by-ph/4369025) for more information.
+* Document and text abstractive summarization is now powered by fine-tuned Phi-3.5-mini! Check out the [Announcing Blog](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/exciting-update-abstractive-summarization-in-azure-ai-language-now-powered-by-ph/4369025) for more information.
 * More skills are available in [Foundry](https://ai.azure.com/?cid=learnDocs): Extract key phrase, Extract named entities, Analyze sentiment, and Detect language. More skills are yet to come.
 
 ## January 2025
@@ -254,7 +254,7 @@ Stay informed about recent releases and enhancements designed to help you get th
 
 ## September 2024
 
-* PII detection now has container support. See more details in the Azure Update post: [Announcing Text PII Redaction Container Release](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-text-pii-redaction-container-release/4264655).
+* PII detection now has container support. See more details in the Azure Update post: [Announcing Text PII Redaction Container Release](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/announcing-text-pii-redaction-container-release/4264655).
 * Custom sentiment analysis (preview) will be retired January 10, 2025. You can transition to other custom model training services, such as custom text classification in Azure Language. See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom sentiment analysis (preview) in Azure Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-sentiment-analysis-retirement).
 * Custom text analytics for health (preview) will be retired on January 10, 2025. Transition to other custom model training services, such as custom named entity recognition in Azure Language, by that date. See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom text analytics for health (preview) in Azure Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-text-analytics-for-health-retirement).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新の機能アップデートの通知"
}
```

### Explanation
この変更は、Azure AI Language Serviceに関する最新の機能やアップデートを紹介する文書に対する小規模な更新です。主に、リンクの更新と情報の明確化が行われています。具体的には、複数のリンクのURLが変更され、最新の情報源を指すように修正されています。

### 重要な変更内容:
1. **Conversational Language Understanding (CLU)**トレーニング構成の新しいバージョンの紹介が、REST APIを通じて利用可能になった旨が記載されています。
2. **会話エージェント構築**のための新しいルーティング戦略 `TRIAGE_AGENT` が含まれるようアップデートされ、その詳細もリンクされています。
3. **.NET SDKs**のサポートに関連する新しい情報を追加しています。これは最新のREST APIバージョンに基づいています。
4. 文書内の一部の説明やリンクは、最新情報へのアクセスを提供するために更新されています。

この修正により、読者は最新情報にアクセスしやすくなり、Azure AI Language Serviceの新機能についての理解を深めることができます。


