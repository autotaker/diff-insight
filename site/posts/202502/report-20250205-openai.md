---
date: '2025-02-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:89e0bdf...MicrosoftDocs:d46a0e8
summary: Azure GovernmentにおけるOpenAIサービスに関する更新が行われ、情報の明確さと関連性が向上しました。主な変更点は、Azure OpenAI
  Assistants APIに「利用可能なモデル」セクションが追加され、関連情報の整理が促進されたことです。新情報の追加や既存情報の更新が行われましたが、機能の廃止や削除はありません。また、特定のモデルが利用できないといった記述が削除され、ユーザーが必要な情報を容易に参照できるよう工夫されています。画像ファイルについては内容の変更はありませんが、参照の整合性が保たれています。この結果、ドキュメントの信頼性と使いやすさが向上し、ユーザーがよりサポートを受けやすい環境が整っています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:89e0bdf...MicrosoftDocs:d46a0e8){target="_blank"}

# Highlights
Azure GovernmentにおけるOpenAIサービス、Azure OpenAI Assistants API、ならびに関連画像ファイルの微調整に関する更新が行われました。主に情報の明確さと関連性を向上させるための変更です。

## New features
- Azure OpenAI Assistants APIの記事に「利用可能なモデル」セクションが追加され、利用できるモデルのリストへのリンクが提供されました。

## Breaking changes
- 変更には実質的な機能の廃止や削除はなく、新しい情報の追加と既存情報の更新が主体です。

## Other updates
- Azure Government向けOpenAIサービスの記事では、特定のモデルが利用できない等の記述を削除し、読者が参考にすべきリンクや制限についての情報が追加されました。
- 画像ファイル「search-trusted-service.png」が更新されたが、実質的には内容変更はなく、参照の整合性確保が図られています。

# Insights
この更新によって、Azure OpenAIサービスに関連する情報がより整理され、ピンポイントに重要な内容だけを伝える形になりました。特に、Azure OpenAI Assistants APIに関する変更では、開発者が本文から簡単に関連モデルを確認することができ、サービス開始日も明記されたため、計画や実装に関する誤解が減少することが期待されます。

また、Azure Governmentの記事の更新により、利用可能な機能や制限事項についての情報提供が強化され、ユーザーが独自に調査を行う際の負担が軽減されました。画像ファイルについての更新は、見た目に大きな変化はないものの、コンテンツの正確性を維持するための重要な作業と言えます。これらの変更により、ドキュメントの信頼性と使い勝手が向上し、多様なユーザーに対してよりサポートしやすい環境が整えられています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-government.md](#item-a47549) | minor update | Azure GovernmentにおけるOpenAIサービスの更新 | modified | 2 | 2 | 4 | 
| [assistants.md](#item-eab970) | minor update | Azure OpenAI Assistants APIの更新 | modified | 6 | 2 | 8 | 
| [search-trusted-service.png](#item-0ef102) | minor update | 画像ファイルの更新 | modified | 0 | 0 | 0 | 


# Modified Contents
## articles/ai-services/openai/azure-government.md{#item-a47549}

<details>
<summary>Diff</summary>
````diff
@@ -12,14 +12,14 @@ recommendations: false
 
 # Azure OpenAI Service and features in Azure Government
 
-This article highlights the differences when using Azure OpenAI in Azure Government as compared to the commercial cloud offering. If not specified, the Azure OpenAI model or feature should be assumed to be not available in the Azure Government environment. Learn more about the Azure OpenAI Service itself in [Azure OpenAI Service documentation](/azure/ai-services/openai/).
+This article highlights the differences when using Azure OpenAI in Azure Government as compared to the commercial cloud offering. Learn more about the Azure OpenAI Service itself in [Azure OpenAI Service documentation](/azure/ai-services/openai/).
 <br><br>
 
 ## Azure OpenAI models
 
 Learn more about the different capabilities of each model in [Azure OpenAI Service models](./concepts/models.md). For customers with [Business Continuity and Disaster Recovery (BCDR) considerations](./how-to/business-continuity-disaster-recovery.md), take careful note of the deployment types, regions, and model availability as not all model/type combinations are available in both regions. 
 
-The following sections show model availability by region and deployment type. Models and versions not listed are not currently available in Azure Government. 
+The following sections show model availability by region and deployment type. Models and versions not listed are not currently available in Azure Government. For general limits, quotas, and other details refer to [Azure OpenAI Service quotas and limits](/azure/ai-services/openai/quotas-limits/). 
 
 <br>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure GovernmentにおけるOpenAIサービスの更新"
}
```

### Explanation
このコードの変更は、Azure GovernmentにおけるOpenAIサービスに関する記事の内容を微調整したものです。具体的には、特定のモデルや機能がAzure Government環境で利用できないことを明示的に述べる部分が削除され、代わりに一般的な制限やクォータ、その他の詳細情報についてのリファレンスが追加されました。これにより、読者はAzure OpenAIサービスに関する情報提供の流れがスムーズになり、利用可能な情報の参照が容易になります。変更された部分は、関連リンクの挿入があり、情報の明瞭性を高める目的で行われています。全体として、この更新は情報の簡潔さと関連性を向上させることを目的としています。

## articles/ai-services/openai/concepts/assistants.md{#item-eab970}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Azure OpenAI Service Assistants API concepts
 titleSuffix: Azure OpenAI Service
 description: Learn about the concepts behind the Azure OpenAI Assistants API.
 ms.topic: conceptual
-ms.date: 08/21/2024
+ms.date: 02/04/2025
 ms.service: azure-ai-openai
 manager: nitinme
 author: aahill
@@ -13,7 +13,7 @@ recommendations: false
 
 # Azure OpenAI Assistants API (Preview)
 
-Assistants, a new feature of Azure OpenAI Service, is now available in public preview. Assistants API makes it easier for developers to create applications with sophisticated copilot-like experiences that can sift through data, suggest solutions, and automate tasks.
+Assistants, a feature of Azure OpenAI Service, is available in public preview starting in the `2024-02-15-preview` API version. Assistants API makes it easier for developers to create applications with sophisticated copilot-like experiences that can sift through data, suggest solutions, and automate tasks.
 
 * Assistants can call Azure OpenAI’s [models](../concepts/models.md) with specific instructions to tune their personality and capabilities.
 * Assistants can access **multiple tools in parallel**. These can be both Azure OpenAI-hosted tools like [code interpreter](../how-to/code-interpreter.md) and [file search](../how-to/file-search.md), or tools you build, host, and access through [function calling](../how-to/function-calling.md).
@@ -38,6 +38,10 @@ Assistants API is built on the same capabilities that power OpenAI’s GPT produ
 > [!IMPORTANT]
 > Retrieving untrusted data using Function calling, Code Interpreter or File Search with file input, and Assistant Threads functionalities could compromise the security of your Assistant, or the application that uses the Assistant. Learn about mitigation approaches [here](https://aka.ms/oai/assistant-rai).
 
+## Available models
+
+To see a list of Azure OpenAI models that you can use with assitants, see the [Models](./models.md#assistants-preview) article.
+
 ## Assistants playground
 
 We provide a walkthrough of the Assistants playground in our [quickstart guide](../assistants-quickstart.md). This provides a no-code environment to test out the capabilities of assistants.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI Assistants APIの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAI ServiceのAssistants APIに関する記事の内容を更新したものです。主な変更点は、Assistantsの利用開始日が2024年2月15日からのプレビュー版として明記されたことです。また、記事の最初の公開日も更新され、2025年2月4日の日付が新たに設定されました。さらに、新しいセクション「利用可能なモデル」が追加され、Assistantsと共に使用できるAzure OpenAIのモデルのリストを参照するリンクが提供されました。これにより、開発者はAssistants APIの利用をより容易に理解できるようになっています。全体として、これらの変更により、情報の正確さと現行の機能に関する明瞭さが向上しています。

## articles/ai-services/openai/media/use-your-data/search-trusted-service.png{#item-0ef102}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAI Serviceに関連する記事内の画像ファイル「search-trusted-service.png」に対するもので、具体的なコンテンツの追加や削除は行われていません。変更のステータスは「modified」となっていますが、実際には内容の変更はなく、画像のメタデータや参照が更新されている可能性があります。この更新により、画像が正しいリンクや文脈で参照されていることを再確認するための作業が行われたと推測されます。全体として、実質的な変更はないものの、情報の整合性や正確性が保たれていると考えられます。


