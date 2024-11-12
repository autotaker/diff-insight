---
date: '2024-11-12'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6042051...MicrosoftDocs:d63c476
summary: このコードの変更では、AIサービス関連の文書が更新され、モデル機能やライフサイクル、言語サポート、地域可用性に関する情報が改訂されました。新機能の追加や情報の有効期限の延長、見出しの調整が行われ、特定地域でのモデルの利用可能情報も明確化されています。特に、`document-intelligence`に新機能が追加され、79言語のサポートが具体化されました。利用者は情報の更新に伴い、プランの見直しが求められるものの、破壊的な変更はありません。全体として、利用者がAIサービスを効率的に活用できるよう、情報の明確化とアクセス性向上が図られています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6042051...MicrosoftDocs:d63c476){target="_blank"}

# Highlights
このコードの変更では、AIサービス関連のいくつかの文書が更新され、モデル機能、ライフサイクル、言語サポート、地域可用性などに関する情報が改訂されました。新しい情報の追加や有効期限の延長、見出しの調整、特定地域でのモデル利用可能可視化などが行われています。

## New features
- `document-intelligence` にて、モデルの `content extraction` と `prebuilt-contract` に新機能が追加されました。
- `language-service` の PII 検出に関する言語サポートの一覧が提供され、79言語のサポート状況が明確化されました。

## Breaking changes
特に破壊的な変更はありませんが、情報の更新により利用者は新たな期限や機能に合わせて計画を見直す必要があります。

## Other updates
- モデルライフサイクルにて、トレーニング構成の有効期限が延長されました。
- 文書見出しが、より正確な内容を反映するように修正されました。
- オンプレミスリソースのアクセス手順やフローモジュール開発の誤字が修正されました。
- 地域可用性に関する情報が具体化され、東US2でのモデル利用可能情報が追加されました。

# Insights
このコードの変更は、利用者がAIサービスをより効率的に活用できるようにと情報をより具体的で、アクセスしやすくすることを目的としています。ユーザーがどのモデルを利用するべきかを判断しやすくするために、特定の機能強化と有効期限の延長が行われています。

特に、`document-intelligence` の機能強化によって、モデルが提供する抽出機能の幅が広がり、ユーザーはデータ処理能力の向上を期待できます。また、`language-service` での大幅な言語サポートの提供は、世界中の多様な需要に対応する競争力を向上させます。

さらに、誤字修正や文書の再編成によってより明確かつ正確な情報が提供されており、ユーザーエクスペリエンスの向上を目指しています。これらの修正は、小さな変更かもしれませんが、全体的な文書の品質を高め、情報をより素早く、確実に理解できるようにしています。地域可用性の更新も、ユーザーが地域に応じたモデルの利用戦略を練る際に有用です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-analysis-features.md](#item-0fe95e) | minor update | モデル分析機能に関する文書の更新 | modified | 2 | 2 | 4 | 
| [model-lifecycle.md](#item-417f3f) | minor update | モデルライフサイクルに関する文書の更新 | modified | 4 | 5 | 9 | 
| [overview.md](#item-4ff047) | minor update | 文書の見出しの更新 | modified | 1 | 1 | 2 | 
| [language-support.md](#item-d332b1) | minor update | 個人情報（PII）検出に関する言語サポートの更新 | modified | 86 | 1 | 87 | 
| [fine-tuning-overview.md](#item-31b07b) | minor update | ファインチューニングに関する概要の更新 | modified | 15 | 28 | 43 | 
| [access-on-premises-resources.md](#item-8e3926) | minor update | オンプレミスリソースへのアクセスに関する文書の更新 | modified | 1 | 1 | 2 | 
| [flow-develop.md](#item-d1ac3e) | minor update | フローモジュールの開発に関する文書の修正 | modified | 1 | 1 | 2 | 
| [region-availability-maas.md](#item-35d79c) | minor update | 地域可用性に関する情報の更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/document-intelligence/includes/model-analysis-features.md{#item-0fe95e}

<details>
<summary>Diff</summary>
````diff
@@ -9,11 +9,11 @@ ms.author: lajanuar
 
 |Model ID|Content Extraction|Query fields|Paragraphs|Paragraph Roles|Selection Marks|Tables|Key-Value Pairs|Languages|Barcodes|Document Analysis|Formulas*|Style Font*|High Resolution*|Searchable PDF
 |:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
-|prebuilt-read|✓| | | | | |O|O| |O|O|O||✓|
+|prebuilt-read|✓| |✓ | | | | |O|O| |O|O|O|✓|
 |prebuilt-layout|✓|✓|✓|✓|✓|✓| |O|O| |O|O|O|
 |prebuilt-document|✓|✓|✓|✓|✓|✓|✓|O|O| |O|O|O|
 |prebuilt-businessCard|✓|✓| | | | | | | |✓| | | |
-|prebuilt-contract|✓|✓|✓|✓| | |O|O|✓|O|O|O||
+|prebuilt-contract|✓|✓|✓|✓| | |O|O|✓|✓|O|O||
 |prebuilt-healthInsuranceCard.us|✓|✓| | | | | |O|O|✓|O|O|O|
 |prebuilt-idDocument|✓|✓|| | | | |O|O|✓|O|O|O|
 |prebuilt-invoice|✓|✓| | |✓|✓|O|O|O|✓|O|O|O|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル分析機能に関する文書の更新"
}
```

### Explanation
この変更では、`articles/ai-services/document-intelligence/includes/model-analysis-features.md` ファイルにおけるモデルの機能に関する情報が更新されました。具体的には、前のバージョンからの比較で、以下の2つの行が追加されました。

1. **content extraction**列の「query fields」の項目に「✓」が追加されました。
2. **prebuilt-contract**の行の「searchable PDF」項目に「✓」が追加されました。

これにより、"prebuilt-read" と "prebuilt-contract" モデルの機能が強化され、より具体的な情報が提供されるようになっています。全体として、この変更は文書の明確さを高め、ユーザーがモデルの機能を理解しやすくしています。

## articles/ai-services/language-service/concepts/model-lifecycle.md{#item-417f3f}

<details>
<summary>Diff</summary>
````diff
@@ -64,11 +64,10 @@ Use the table below to find which model versions are supported by each feature:
 
 | Feature                                     | Supported Training Config Versions         | Training Config Expiration         | Deployment Expiration  |
 |---------------------------------------------|--------------------------------------------|------------------------------------|------------------------|
-| Conversational language understanding       | `2022-05-01`                               | October 28, 2022 (expired)         | October 28, 2023       |
-| Conversational language understanding       | `2022-09-01` (latest)**                    | February 28, 2024                  | February 27, 2025      |
-| Orchestration workflow                      | `2022-09-01` (latest)**                    | April 30, 2024                     | April 30, 2025         |
-| Custom named entity recognition             | `2022-05-01` (latest)**                    | April 30, 2024                     | April 30, 2025         |
-| Custom text classification                  | `2022-05-01` (latest)**                    | April 30, 2024                     | April 30, 2025         |
+| Conversational language understanding       | `2022-09-01` (latest)**                    | August 26, 2025                    | August 26, 2026        |
+| Orchestration workflow                      | `2022-09-01` (latest)**                    | October 22, 2025                   | October 22, 2026       |
+| Custom named entity recognition             | `2022-05-01` (latest)**                    | October 22, 2025                   | October 22, 2026       |
+| Custom text classification                  | `2022-05-01` (latest)**                    | October 22, 2025                   | October 22, 2026       |
 
 ** *For latest training configuration versions, the posted expiration dates are subject to availability of a newer model version. If no newer model versions are available, the expiration date may be extended.*
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルに関する文書の更新"
}
```

### Explanation
この変更では、`articles/ai-services/language-service/concepts/model-lifecycle.md` ファイルにおけるモデルのライフサイクルに関する情報が更新されました。具体的には、いくつかのモデル機能のサポートされているトレーニング構成バージョンとその有効期限に関するデータが改訂されました。

主な変更点は以下の通りです：

1. **Conversational language understanding** のトレーニング構成の有効期限が「2024年2月28日」から「2025年8月26日」に延長されました。
2. **Orchestration workflow** のトレーニング構成の有効期限が「2024年4月30日」から「2025年10月22日」に延長されました。
3. **Custom named entity recognition** と **Custom text classification** のトレーニング構成の有効期限も「2024年4月30日」から「2025年10月22日」に変更されました。

これにより、ユーザーはこれらのモデル機能の最新の有効期限を明確に把握できるようになり、より適切な使用計画を立てることが可能になります。

## articles/ai-services/language-service/key-phrase-extraction/overview.md{#item-4ff047}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ This documentation contains the following types of articles:
 [!INCLUDE [Typical workflow for pre-configured language features](../includes/overview-typical-workflow.md)]
 
 
-## Get started with entity linking
+## Get started with Key phrase extraction
 
 [!INCLUDE [development options](./includes/development-options.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書の見出しの更新"
}
```

### Explanation
この変更では、`articles/ai-services/language-service/key-phrase-extraction/overview.md` ファイルの見出しが更新されました。具体的には、「Get started with entity linking」という見出しが「Get started with Key phrase extraction」に変更されました。

この更新は、ドキュメントの内容をより正確に反映させ、ユーザーが関心を持つであろうキーフレーズ抽出に関する情報に直接誘導するためのものです。これにより、利用者が求めている情報を見つけやすくなることを目的としています。

## articles/ai-services/language-service/personally-identifiable-information/language-support.md{#item-d332b1}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,92 @@ ms.custom: language-service-pii, build-2024
 
 # Personally Identifiable Information (PII) detection language support 
 
-Use this article to learn which natural languages are supported by the PII and conversation PII features of Azure AI Language.
+Use this article to learn which natural languages are supported by the text PII, document PII, and conversation PII features of Azure AI Language.
+# [Text PII](#tab/text)
+
+## Text PII language support
+
+|Language             |Language code|Notes             |
+|---------------------|-------------|------------------|
+|Afrikaans            |`af`         |                  |
+|Albanian             |`sq`         |                  |
+|Amharic              |`am`         |                  |
+|Arabic               |`ar`         |                  |
+|Armenian             |`hy`         |                  |
+|Assamese             |`as`         |                  |
+|Azerbaijani          |`az`         |                  |
+|Basque               |`eu`         |                  |
+|Bengali              |`bn`         |                  |
+|Bosnian              |`bs`         |                  |
+|Bulgarian            |`bg`         |                  |
+|Burmese              |`my`         |                  |
+|Catalan              |`ca`         |                  |
+|Chinese-Simplified   |`zh-hans`    |`zh` also accepted|
+|Chinese-Traditional  |`zh-hant`    |                  |
+|Croatian             |`hr`         |                  |
+|Czech                |`cs`         |                  |
+|Danish               |`da`         |                  |
+|Dutch                |`nl`         |                  |
+|English              |`en`         |                  |
+|Estonian             |`et`         |                  |
+|Finnish              |`fi`         |                  |
+|French               |`fr`         |                  |
+|Galician             |`gl`         |                  |
+|Georgian             |`ka`         |                  |
+|German               |`de`         |                  |
+|Greek                |`el`         |                  |
+|Gujarati             |`gu`         |                  |
+|Hebrew               |`he`         |                  |
+|Hindi                |`hi`         |                  |
+|Hungarian            |`hu`         |                  |
+|Indonesian           |`id`         |                  |
+|Irish                |`ga`         |                  |
+|Italian              |`it`         |                  |
+|Japanese             |`ja`         |                  |
+|Kannada              |`kn`         |                  |
+|Kazakh               |`kk`         |                  |
+|Khmer                |`km`         |                  |
+|Korean               |`ko`         |                  |
+|Kurdish(Kurmanji)    |`ku`         |                  |
+|Kyrgyz               |`ky`         |                  |
+|Lao                  |`lo`         |                  |
+|Latvian              |`lv`         |                  |
+|Lithuanian           |`lt`         |                  |
+|Macedonian           |`mk`         |                  |
+|Malagasy             |`mg`         |                  |
+|Malay                |`ms`         |                  |
+|Malayalam            |`ml`         |                  |
+|Marathi              |`mr`         |                  |
+|Mongolian            |`mn`         |                  |
+|Nepali               |`ne`         |                  |
+|Norwegian  (Bokmål)  |`no`         |`nb` also accepted|
+|Odia                 |`or`         |                  |
+|Pashto               |`ps`         |                  |
+|Persian              |`fa`         |                  |
+|Polish               |`pl`         |                  |
+|Portuguese (Brazil)  |`pt-BR`      |                  |
+|Portuguese (Portugal)|`pt-PT`      |`pt` also accepted|
+|Punjabi              |`pa`         |                  |
+|Romanian             |`ro`         |                  |
+|Russian              |`ru`         |                  |
+|Serbian              |`sr`         |                  |
+|Slovak               |`sk`         |                  |
+|Slovenian            |`sl`         |                  |
+|Somali               |`so`         |                  |
+|Spanish              |`es`         |                  |
+|Swahili              |`sw`         |                  |
+|Swazi                |`ss`         |                  |
+|Swedish              |`sv`         |                  |
+|Tamil                |`ta`         |                  |
+|Telugu               |`te`         |                  |
+|Thai                 |`th`         |                  |
+|Turkish              |`tr`         |                  |
+|Ukrainian            |`uk`         |                  |
+|Urdu                 |`ur`         |                  |
+|Uyghur               |`ug`         |                  |
+|Uzbek                |`uz`         |                  |
+|Vietnamese           |`vi`         |                  |
+|Welsh                |`cy`         |                  |
 
 # [PII for documents](#tab/documents)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人情報（PII）検出に関する言語サポートの更新"
}
```

### Explanation
この変更では、`articles/ai-services/language-service/personally-identifiable-information/language-support.md` ファイルにおいて、個人情報（PII）検出機能に対応する言語サポートに関する情報が大幅に更新されました。

具体的には、以下の内容が追加されました：

1. **テキストPIIの言語サポート**に関する新しいセクションが追加され、サポートされる言語とその言語コードの詳細が表形式で示されています。これにより、ユーザーは利用可能な言語を簡単に確認することが可能になりました。
2. 言語のリストには79の言語が含まれており、各言語に対するコードや特記事項も記載されています。

この更新によって、Azure AI LanguageのテキストPII、文書PII、および会話PII機能の利用者が、どの言語がサポートされているかを理解しやすくなり、機能の利用が促進されることが期待されます。

## articles/ai-studio/concepts/fine-tuning-overview.md{#item-31b07b}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: scottpolly
 ms.service: azure-ai-studio
 ms.custom:
   - build-2024
+  - code01
 ms.topic: conceptual
 ms.date: 10/31/2024
 ms.reviewer: sgilley
@@ -30,23 +31,18 @@ When you're deciding whether or not fine-tuning is the right solution for your u
 - [Prompt engineering](../../ai-services/openai/concepts/prompt-engineering.md) is a technique that involves designing prompts for natural language processing models. This process improves accuracy and relevancy in responses, to optimize the performance of the model.
 - [Retrieval-augmented generation (RAG)](../concepts/retrieval-augmented-generation.md) improves LLM performance by retrieving data from external sources and incorporating it into a prompt. RAG can help businesses achieve customized solutions while maintaining data relevance and optimizing costs.
 
-Fine-tuning is an advanced technique that requires expertise to use appropriately. The following questions can help you evaluate whether you're ready for fine-tuning, and how well you thought through the process. You can use these questions to guide your next steps or to identify other approaches that might be more appropriate.
+Fine-tuning is a great way to get higher quality results while reducing latency. The following questions can help you better understand why fine-tuning and evaluate whether you're ready for fine-tuning through the process. You can use these questions to guide your next steps.
 
 ### Why do you want to fine-tune a model?
 
-You might be ready for fine-tuning if:
-
-- You can clearly articulate a specific use case for fine-tuning and identify the [model](../how-to/model-catalog.md) that you hope to fine-tune.
+Before you begin fine-tuning a model, consider if you've identified shortcomings when using a base model. These shortcomings can include: an inconsistent performance on edge cases, inability to fit enough prompts in the context window to steer the model, or high latency.
 
-  Good use cases for fine-tuning include steering the model to output content in a specific and customized style, tone, or format. They also include scenarios where the information needed to steer the model is too long or complex to fit into the prompt window.
-- You have clear examples of how you addressed the challenges in alternate approaches and what you tested as possible resolutions to improve performance.
-- You identified shortcomings by using a base model, such as inconsistent performance on edge cases, inability to fit enough shot prompts in the context window to steer the model, or high latency.
+Base models are already pre-trained on vast amounts of data, but most times you will add instructions and examples to the prompt to get the quality responses that you're looking for. This process of "few-shot learning" can be improved with fine-tuning.
 
-You might not be ready for fine-tuning if:
+Fine-tuning allows you to train a model with many more examples. You can tailor your examples to meet your specific use-case. This can help you reduce the number of tokens in the prompt leading to potential cost savings and requests with lower latency.
 
-- There's insufficient knowledge from the model or data source.
-- You can't find the right data to serve the model.
-- You don't have a clear use case for fine-tuning, or you can't articulate more than "I want to make a model better."
+Use cases for fine-tuning a model can be:
+- Steering the model to output content in a specific and customized style, tone, or format.
 
 If you identify cost as your primary motivator, proceed with caution. Fine-tuning might reduce costs for certain use cases by shortening prompts or allowing you to use a smaller model. But typically there's a higher upfront cost to training, and you have to pay for hosting your own custom model. 
 
@@ -64,38 +60,29 @@ Fine-tuning is an advanced capability, not the starting point for your generativ
 
 Having a baseline for performance without fine-tuning is essential for knowing whether or not fine-tuning improves model performance. Fine-tuning with bad data makes the base model worse, but without a baseline, it's hard to detect regressions.
 
-You might be ready for fine-tuning if:
+Before you begin fine-tuning a model, you need to ensure:
 
-- You can demonstrate evidence and knowledge of prompt engineering and RAG-based approaches.
+- You can demonstrate evidence and knowledge of using prompt engineering and RAG-based approaches on your LLM.
 - You can share specific experiences and challenges with techniques other than fine-tuning that you tried for your use case.
-- You have quantitative assessments of baseline performance, whenever possible.  
-
-You might not be ready for fine-tuning if:
-
-- You haven't tested any other techniques.
-- You have insufficient knowledge or understanding of how fine-tuning applies specifically to LLMs.
-- You have no benchmark measurements to assess fine-tuning against.
+- You have quantitative assessments of baseline performance, whenever possible.
+- You have a labeled dataset that corresponds with the specific usecase you want to train your LLM. 
 
 ### What data are you going to use for fine-tuning?
 
-Even with a great use case, fine-tuning is only as good as the quality of the data that you can provide. You need to be willing to invest the time and effort to make fine-tuning work. Different models require different data volumes, but you often need to be able to provide fairly large quantities of high-quality curated data.
+Even with a great use case, fine-tuning is only as good as the quality of the data that you can provide. You need to be willing to invest the time and effort to make fine-tuning work. Different models require different data volumes, but you often need to be able to provide fairly large quantities of high-quality curated data. In supervised fine-tuning, a generic moddel is trained on a topic specific labeled dataset. The model with adjust it's parameters to the new data and apply pre-existing knowledge when outputting new content. 
 
 Another important point is that even with high-quality data, if your data isn't in the necessary format for fine-tuning, you need to commit engineering resources for the formatting. 
 
 You might be ready for fine-tuning if:
 
 - You identified a dataset for fine-tuning.
-- Your dataset is in the appropriate format for training.
+- Your dataset is in the appropriate format for training on your existing model.
 - You employed some level of curation to ensure dataset quality.
 
-You might not be ready for fine-tuning if:
-
-- An appropriate dataset hasn't been identified.
-- The dataset format doesn't match the model that you want to fine-tune.
 
-### How can you measure the quality of your fine-tuned model?
+### How will you measure the quality of your fine-tuned model?
 
-There isn't a single right answer to this question, but you should have clearly defined goals for what success with fine-tuning looks like. Ideally, this effort shouldn't just be qualitative. It should include quantitative measures of success, like using a holdout set of data for validation, in addition to user acceptance testing or A/B testing the fine-tuned model against a base model.
+There isn't a single right answer to this question, but you should have clearly defined goals for what success with fine-tuning looks like. Ideally, this effort shouldn't just be qualitative. It should include quantitative measures of success, like using a holdout set of data for validation, in addition to user acceptance testing or A/B testing the fine-tuned model against a base model. 
 
 ## Supported models for fine-tuning in Azure AI Studio
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングに関する概要の更新"
}
```

### Explanation
この変更では、`articles/ai-studio/concepts/fine-tuning-overview.md` ファイルにおいて、ファインチューニングの概要に関連する情報が更新されました。主な変更点は以下の通りです：

1. **コンテンツの整理**: 新しい項目が追加され、一部の内容が削除または簡素化され、全体的に文書が整理されました。特に、ファインチューニングのメリットやそれを行うべき理由に関する説明が改善されています。

2. **ファインチューニングの目的**: ファインチューニングの目的について、具体的に未熟な点や改善の必要なエリアを考慮することが強調され、ユーザーがファインチューニングを行うべきかどうかをより良く理解できるように配慮されています。

3. **使用ケースとデータの重要性**: ファインチューニングを行う前に考慮すべき使用ケースや、適切なデータセットの選定が重要であることが明確にされ、質の高いデータの提供が求められています。

4. **評価指標**: モデルのファインチューニングの成功を測る方法についても、成功の定義における定量的な指標の必要性が強調されています。

これにより、読者はファインチューニングの重要性、特定の状況における使用方法、および実施する際の考慮事項について、より深く理解できるようになります。

## articles/ai-studio/how-to/access-on-premises-resources.md{#item-8e3926}

<details>
<summary>Diff</summary>
````diff
@@ -64,7 +64,7 @@ Follow the [Quickstart: Direct web traffic using the portal](/azure/application-
         - Name: Provide a name for your private link configuration
         - Private link subnet: Select a subnet in your virtual network. 
         - Frontend IP Configuration: `appGwPrivateFrontendIpIPv4`
-    - To verify the Private link is set up correctly, navigate to the __Private endpoint connections__ tab and select __+ Private endpoint__. On the __Resource__ tab, the __Target sub-resource__ should be the name of your private Frontend IP configuration, `appGwPrivateFrontendIpIPv4`. If no value appears in the __Target sub-resource__, then the Application Gateway listener wasn't configured correctly. 
+    - To verify the Private link is set up correctly, navigate to the __Private endpoint connections__ tab and select __+ Private endpoint__. On the __Resource__ tab, the __Target sub-resource__ should be the name of your private Frontend IP configuration, `appGwPrivateFrontendIpIPv4`. If no value appears in the __Target sub-resource__, then the Application Gateway listener wasn't configured correctly. For more on setting up Private link in Application Gateway, see [Configure Azure Application Gateway Private Link](/azure/application-gateway/private-link-configure).
 
 ## Configure private link
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オンプレミスリソースへのアクセスに関する文書の更新"
}
```

### Explanation
この変更では、`articles/ai-studio/how-to/access-on-premises-resources.md` ファイルにおいて、オンプレミスリソースへのアクセス手順に関する内容が更新されました。主な変更点は以下の通りです：

1. **手順の詳細追加**: プライベートリンクが正しく設定されているかを確認する手順に、リソースタブの設定に関する追加情報が含まれました。具体的には、アプリケーションゲートウェイのプライベートIP構成名や、プライベートリンクの設定に関する情報の参照先が明示されています。

2. **リンクの追加**: 「アプリケーションゲートウェイのプライベートリンクの設定」に関する新しいリンクが追加され、ユーザーが設定内容を確認しやすくなっています。このリンクを通じて関連情報にアクセスできることで、ユーザーはよりスムーズに手順を理解し、実行できるようになります。

この更新により、文書の明確性が向上し、プライベートリンク設定の確認方法がより理解しやすくなっています。ユーザーは、関連情報を迅速に確認できるため、手順の実行が容易になります。

## articles/ai-studio/how-to/flow-develop.md{#item-d1ac3e}

<details>
<summary>Diff</summary>
````diff
@@ -132,7 +132,7 @@ By selecting a span, you can see the detailed information on the right side. Thi
 :::image type="content" source="../media/prompt-flow/authoring-trace.png" alt-text=" Screenshot of trace detail." lightbox="../media/prompt-flow/authoring-trace.png":::
 
 > [!NOTE]
-> In prompt flow SDK, we defined serval span types, including **LLM**, **Function**, **Embedding**, **Retrieval**, and **Flow**. And the system automatically creates spans with execution information in designated attributes and events.
+> In prompt flow SDK, we defined several span types, including **LLM**, **Function**, **Embedding**, **Retrieval**, and **Flow**. And the system automatically creates spans with execution information in designated attributes and events.
 >
 > To learn more about span types, see  [Trace span](https://microsoft.github.io/promptflow/reference/trace-span-spec-reference.html).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フローモジュールの開発に関する文書の修正"
}
```

### Explanation
この変更では、`articles/ai-studio/how-to/flow-develop.md` ファイルにおいて、フローモジュールの開発に関する説明文が修正されました。主な変更点は以下の通りです：

1. **誤字修正**: 「several」という単語が「serval」に誤って記載されていた部分が修正され、「several」となりました。これにより、文書の正確性が向上しました。

2. **情報の明確化**: フロープロンプトSDKにおけるスパンタイプの説明部分において、情報がより明確になりました。この修正により、ユーザーがスパンの役割や種類を正しく理解できるようになっています。

これらの修正は小規模ですが、文書の全体的な品質を向上させ、ユーザーがより容易に情報を理解できるようにしています。

## articles/ai-studio/includes/region-availability-maas.md{#item-35d79c}

<details>
<summary>Diff</summary>
````diff
@@ -47,8 +47,8 @@ Llama 3.1 405B Instruct  | [Microsoft Managed Countries](/partner-center/marketp
 |Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
 Phi-3.5-vision-Instruct     | Not applicable | East US 2 <br> Sweden Central  | Not available       |
-Phi-3.5-MoE-Instruct     | Not applicable | East US 2 <br> Sweden Central  | Not available       |
-Phi-3.5-Mini-Instruct     | Not applicable | East US 2 <br> Sweden Central  | Not available       |
+Phi-3.5-MoE-Instruct     | Not applicable | East US 2 <br> Sweden Central  | East US 2       |
+Phi-3.5-Mini-Instruct     | Not applicable | East US 2 <br> Sweden Central  | East US 2       |
 Phi-3-Mini-4k-Instruct <br>  Phi-3-Mini-128K-Instruct    | Not applicable | East US 2 <br> Sweden Central  | East US 2  |
 Phi-3-Small-8K-Instruct <br>  Phi-3-Small-128K-Instruct     | Not applicable | East US 2 <br> Sweden Central  | Not available       |
 Phi-3-Medium-4K-Instruct  <br>  Phi-3-Medium-128K-Instruct  | Not applicable | East US 2 <br> Sweden Central  | East US 2      |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域可用性に関する情報の更新"
}
```

### Explanation
この変更では、`articles/ai-studio/includes/region-availability-maas.md` ファイルにおいて、地域可用性に関する表が更新されました。主な変更点は以下の通りです：

1. **可用性の明確化**: Phi-3.5-MoE-Instruct と Phi-3.5-Mini-Instruct の「Hub/Project Region for Fine tuning」列において、これらのモデルが「East US 2」で利用可能であることが明示されました。これにより、ユーザーはそれぞれのモデルでのファインチューニング地域をより理解しやすくなります。

2. **表の整備**: 全体として表の情報が整理され、モデルごとの地域別の詳細が明確に示されるようになりました。特に、ファインチューニングを行う際の地域情報が付加されたことで、ユーザーがどの地域でリソースを利用できるかを把握しやすくなりました。

この修正は、文書の可読性を高め、ユーザーが必要とする情報を迅速に見つけられるようにするために重要です。


