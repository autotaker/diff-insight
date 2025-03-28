---
date: '2025-03-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4f20510...MicrosoftDocs:86d029a
summary: このコードの変更は、OpenAIサービスに関するドキュメントの日付を更新し、モデルやAPIバージョンの情報を最新化することを目的としています。一部の記事は内容調整が行われ、冗長性の解消やモデルの更新がなされています。特に、PythonやREST
  API関連のドキュメントには重要なBreaking Changeが含まれており、全体の記事の日付が2025年3月に設定されています。新機能としては最新のAPIバージョンが導入され、Breaking
  Changesでは認証方法やモデル名の大幅更新が行われています。また、その他の更新としてエンドポイント利用に関する情報も改訂されました。この変更はAzure OpenAIサービスの進化を反映しており、ユーザーが最新の技術にアクセスしやすくなることを目的としています。運用中のシステムへの影響を抑えつつ、新技術の統合が今後の課題となります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4f20510...MicrosoftDocs:86d029a){target="_blank"}

<format>
# ハイライト
このコードの変更は、OpenAIサービスに関するドキュメントの多くの記事に日付の更新を施し、いくつかのモデルやAPIバージョンの情報を最新化することが目的とされています。一部の記事においては、内容自体も調整され、冗長性の解消やモデルの更新が行われています。特筆すべき変更点として、PythonやREST API関連のドキュメントでは、重要なBreaking Changeが含まれ、小規模な共通点としては、広範囲の記事の日付が2025年3月に設定されました。

## 新機能
- 最新のAPIバージョン（2025-03-01-preview）の導入、一部で包括的な利用を促進するための新しいセクションの追加。

## Breaking changes
- 「python.md」や「chat-completion.md」のドキュメントで、モデル名や認証方法が大幅に更新され、従来の手法とは異なる実装が要求されています。
- OpenAI Pythonクライアントを中心に、認証の取り扱い方法に大きな変更が加えられ、セキュリティと機能性の向上が図られています。

## その他の更新
- APIバージョン変更に伴い、エンドポイント利用に関する情報が更新され、「GPT-4o」や「GPT-4.5」などのモデル名が随所に反映されています。
- 一部のファイルでは、HTTPSメソッドやコマンドライン指示の微調整が行われ、正確性が高まりました。

# 洞察
この変更の流れは、Azure OpenAIサービスが急速に進化を遂げていることを示しています。特にAPIのバージョンアップデートやモデル名の整合が大きな焦点となっており、これはユーザーが最新の技術にアクセスし、直感的に利用できるようにするための戦略的な更新と考えられます。  
最新のモデルとAPIを採用することによって、性能面での改善、セキュリティの向上、そして新しい機能の利用が促進されることで、実際のビジネスアプリケーションにおける柔軟性と信頼性が高まることが期待されます。  
また、破壊的変更が導入されているドキュメントやプログラム実装例では、ユーザーへの注意喚起が不可欠であり、従来の方法に依存した環境ではさらなる調整が求められる可能性があります。運用中のシステムへの影響を最低限に抑えつつ、新しい技術を効率的に統合することが、今後の重要な課題となるでしょう。  
全体的に、ドキュメントの更新は常に精緻さを図りながら、技術進展に伴う適切な情報提供を目指しているといえます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [abuse-monitoring.md](#item-b7afcb) | minor update | 更新された日付と内容の調整 | modified | 2 | 2 | 4 | 
| [advanced-prompt-engineering.md](#item-ff39d1) | minor update | システムメッセージの説明を更新 | modified | 4 | 4 | 8 | 
| [customizing-llms.md](#item-067bef) | minor update | カスタマイズされたLLMに関する日付の更新 | modified | 1 | 1 | 2 | 
| [fine-tuning-considerations.md](#item-71d8ac) | minor update | ファインチューニングに関する日付の更新 | modified | 1 | 1 | 2 | 
| [prompt-engineering.md](#item-884584) | minor update | プロンプトエンジニアリングに関するテクニックの修正 | modified | 2 | 2 | 4 | 
| [provisioned-migration.md](#item-68e143) | minor update | プロビジョニングされた移行に関する日付の更新 | modified | 2 | 2 | 4 | 
| [provisioned-throughput.md](#item-022e0c) | minor update | プロビジョニングスループットに関する日付の更新 | modified | 1 | 1 | 2 | 
| [red-teaming.md](#item-0916c9) | minor update | レッドチーミングに関する日付の更新 | modified | 1 | 1 | 2 | 
| [system-message.md](#item-10456c) | minor update | システムメッセージに関する日付の更新 | modified | 1 | 1 | 2 | 
| [understand-embeddings.md](#item-736ec2) | minor update | 埋め込みに関する日付の更新 | modified | 1 | 1 | 2 | 
| [encrypt-data-at-rest.md](#item-765ec8) | minor update | データ暗号化に関する日付の更新 | modified | 1 | 1 | 2 | 
| [faq.yml](#item-6deb71) | minor update | FAQファイルの日付更新 | modified | 1 | 1 | 2 | 
| [business-continuity-disaster-recovery.md](#item-0d0259) | minor update | 事業継続と災害復旧に関する日付の更新 | modified | 1 | 1 | 2 | 
| [chat-markup-language.md](#item-e61acf) | minor update | ChatMLに関する注意事項の更新 | modified | 2 | 2 | 4 | 
| [chatgpt.md](#item-ae297a) | minor update | タイトルと説明の更新および日付の修正 | modified | 4 | 4 | 8 | 
| [completions.md](#item-79f39a) | minor update | 説明と日付の更新 | modified | 3 | 3 | 6 | 
| [dotnet-migration.md](#item-64142b) | minor update | 日付およびベータ版のAPIバージョンラベルの更新 | modified | 2 | 2 | 4 | 
| [embeddings.md](#item-e38d07) | breaking change | APIバージョンの変更と内容の簡素化 | modified | 4 | 24 | 28 | 
| [fine-tuning.md](#item-5c0e85) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [json-mode.md](#item-50fa9e) | minor update | APIバージョンと日付の更新 | modified | 2 | 2 | 4 | 
| [latency.md](#item-80eeec) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [migration.md](#item-3013aa) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [monitor-openai.md](#item-fcba4d) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [provisioned-get-started.md](#item-c8df1c) | minor update | APIバージョンと日付の更新 | modified | 3 | 4 | 7 | 
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [reproducible-output.md](#item-8d515c) | minor update | APIバージョンと日付の更新 | modified | 5 | 5 | 10 | 
| [switching-endpoints.yml](#item-1cbadc) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [weights-and-biases-integration.md](#item-8ae868) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [work-with-code.md](#item-b193c2) | minor update | タイトルと内容の更新 | modified | 5 | 5 | 10 | 
| [working-with-models.md](#item-7ec098) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [batch-rest.md](#item-bcccd9) | minor update | HTTPメソッドの追加 | modified | 1 | 1 | 2 | 
| [chat-completion.md](#item-1deb8a) | breaking change | モデル名とAPIバージョンの更新 | modified | 13 | 199 | 212 | 
| [embeddings-python.md](#item-3ad1b9) | minor update | APIバージョンと日付の更新 | modified | 3 | 3 | 6 | 
| [fine-tune.md](#item-be8a2e) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [dotnet.md](#item-46e881) | minor update | 日付とバージョンの更新 | modified | 4 | 2 | 6 | 
| [go.md](#item-a289f2) | minor update | 日付とAPIバージョンの更新 | modified | 3 | 3 | 6 | 
| [java.md](#item-5edb45) | minor update | 日付とバージョンの更新 | modified | 3 | 3 | 6 | 
| [javascript.md](#item-50536a) | minor update | 日付とプレビューAPIバージョンの更新 | modified | 2 | 2 | 4 | 
| [python.md](#item-9cca6c) | minor update | 日付、プレビューAPIバージョン、および新規セクションの追加 | modified | 6 | 2 | 8 | 
| [prompt-chat-completion.md](#item-fd2907) | minor update | 更新されたモデルの情報と日付の変更 | modified | 2 | 2 | 4 | 
| [prompt-completion.md](#item-d52cc1) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [python.md](#item-989064) | breaking change | OpenAI Pythonクライアントの更新と実装の変更 | modified | 25 | 31 | 56 | 
| [rest.md](#item-071924) | minor update | APIバージョンの更新とコマンドの追加 | modified | 16 | 3 | 19 | 
| [studio.md](#item-eeeaff) | minor update | ドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [index.yml](#item-0adb87) | minor update | 要約とリンクリストの更新 | modified | 10 | 10 | 20 | 
| [quickstart.md](#item-7d1656) | minor update | クイックスタートの日付更新 | modified | 1 | 1 | 2 | 
| [supported-languages.md](#item-12c019) | minor update | サポートされている言語の日付更新 | modified | 1 | 1 | 2 | 
| [embeddings.md](#item-1f01e7) | minor update | 埋め込みチュートリアルの日付更新 | modified | 1 | 1 | 2 | 
| [fine-tune.md](#item-8f87b5) | minor update | ファインチューニングチュートリアルの日付更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/abuse-monitoring.md{#item-b7afcb}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: mrbullwinkle
 ms.author: mbullwin
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 09/20/2024
+ms.date: 03/27/2025
 ms.custom: template-concept, ignite-2024
 manager: nitinme
 ---
@@ -29,7 +29,7 @@ There are several components to abuse monitoring:
 
 ## Modified abuse monitoring 
 
-Some customers may want to use the Azure OpenAI Service for a use case that involves the processing of highly sensitive or highly confidential data, or otherwise may conclude that they don't want or don't have the right to permit Microsoft to store and conduct human review on their prompts and completions for abuse detection. To address these concerns, Microsoft allows customers who meet additional Limited Access eligibility criteria to apply to modify abuse monitoring by completing [this ](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUOE9MUTFMUlpBNk5IQlZWWkcyUEpWWEhGOCQlQCN0PWcu)form. Learn more about applying for modified abuse monitoring at [Limited access to Azure OpenAI Service](/legal/cognitive-services/openai/limited-access?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext), and about the impact of modified abuse monitoring on data processing at [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=azure-portal).    
+Some customers may want to use the Azure OpenAI Service for a use case that involves the processing of highly sensitive or highly confidential data, or otherwise may conclude that they don't want or don't have the right to permit Microsoft to store and conduct human review on their prompts and completions for abuse detection. To address these concerns, Microsoft allows customers who meet additional Limited Access eligibility criteria to apply to modify abuse monitoring by completing [this](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUOE9MUTFMUlpBNk5IQlZWWkcyUEpWWEhGOCQlQCN0PWcu)form. Learn more about applying for modified abuse monitoring at [Limited access to Azure OpenAI Service](/legal/cognitive-services/openai/limited-access?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext), and about the impact of modified abuse monitoring on data processing at [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=azure-portal).    
 
 > [!NOTE]
 > When abuse monitoring is modified and human review is not performed, detection of potential abuse may be less accurate. Customers are notified of potential abuse detection as described above, and should be prepared to respond to such notification to avoid service interruption if possible.  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新された日付と内容の調整"
}
```

### Explanation
この変更では、ドキュメント「abuse-monitoring.md」が2行追加され、2行削除されることで内容が調整されました。具体的には、更新された日付が2024年9月20日から2025年3月27日に変更され、文章の一部が繰り返しを避ける形で再構成されています。この調整により、顧客がAzure OpenAIサービスの使用を希望する際の個人情報の取り扱いや、手動レビューを行わない場合における潜在的な乱用検出の精度についての注意点が強調されています。また、顧客が修正された乱用監視に申し込む方法についてのリンクも維持されています。全体として、この更新は情報の明確性と正確性を向上させることを目的としています。

## articles/ai-services/openai/concepts/advanced-prompt-engineering.md{#item-ff39d1}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,12 @@
 ---
 title: Design system messages with Azure OpenAI
 titleSuffix: Azure OpenAI Service
-description: Learn about system message design with GPT-3, GPT-35-Turbo, and GPT-4 models.
+description: Learn about system message design
 author: mrbullwinkle
 ms.author: mbullwin 
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 09/05/2024
+ms.date: 03/26/2025
 manager: nitinme
 keywords: ChatGPT, GPT-4, meta prompts, chain of thought
 ---
@@ -17,9 +17,9 @@ This guide will walk you through some techniques in system message design.
 
 
 
-## What is a system message? 
+## What is a system message?
 
-A system message is a feature-specific set of instructions or contextual frameworks given to a generative AI model (e.g. GPT4-o, GPT3.5 Turbo, etc.) to direct and improve the quality and safety of a model’s output. This is particularly helpful in situations that need certain degrees of formality, technical language, or industry-specific terms.  
+A system message is a feature-specific set of instructions or contextual frameworks given to a generative AI model (e.g. GPT-4o, GPT-3.5 Turbo, etc.) to direct and improve the quality and safety of a model’s output. This is particularly helpful in situations that need certain degrees of formality, technical language, or industry-specific terms.  
 
 
 There is no prescribed length. A system message can be one short sentence:  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "システムメッセージの説明を更新"
}
```

### Explanation
この変更では、「advanced-prompt-engineering.md」ファイルにおいて、文書の説明と日付が更新され、いくつかの代替案が修正されました。具体的には、システムメッセージの設計に関する説明が「Learn about system message design with GPT-3, GPT-35-Turbo, and GPT-4 models.」から「Learn about system message design」に簡略化されました。また、更新された日付が2024年9月5日から2025年3月26日に変更されました。

内容の他の部分では、システムメッセージの定義が若干修正され、形式やテクニカルな言語、業界特有の用語が必要な状況における生成AIモデルの出力の質と安全性を向上させるための指示や文脈的な枠組みとしての役割が明確化されています。この更新は、情報の精度と関連性を向上させ、読者が知識を深めるための参考資料となることを目的としています。

## articles/ai-services/openai/concepts/customizing-llms.md{#item-067bef}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Azure OpenAI Service getting started with customizing a large language mo
 titleSuffix: Azure OpenAI Service
 description: Learn more about the concepts behind customizing an LLM with Azure OpenAI.
 ms.topic: conceptual
-ms.date: 09/20/2024
+ms.date: 03/27/2025
 ms.service: azure-ai-openai
 manager: nitinme
 author: mrbullwinkle
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタマイズされたLLMに関する日付の更新"
}
```

### Explanation
この変更では、「customizing-llms.md」ファイルにおける情報が微調整されました。具体的には、文書の日付が2024年9月20日から2025年3月27日に変更されました。また、文書の説明として「Learn more about the concepts behind customizing an LLM with Azure OpenAI.」の部分はそのまま維持されています。この微調整は、情報の最新性を保持し、読者がカスタマイズされた大規模言語モデル（LLM）についての理解を深める上での参考資料を提供することを目的としています。全体として、この変更は内容の信頼性と正確性を向上させるための小さな更新です。

## articles/ai-services/openai/concepts/fine-tuning-considerations.md{#item-71d8ac}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn more about what you should take into consideration before fin
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 08/29/2024
+ms.date: 03/26/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングに関する日付の更新"
}
```

### Explanation
この変更では、「fine-tuning-considerations.md」ファイルの日付が更新されました。具体的には、文書の日付が2024年8月29日から2025年3月26日に変更されています。文書の説明は「Learn more about what you should take into consideration before fine-tuning」のままとなっており、内容自体には大きな変更はありません。この更新は、情報が最新であることを確保し、読者がファインチューニングに関する考慮事項についての理解を深めるための参考資料としての役割を保つことを目的としています。全体的には、信頼性の向上を図るための軽微な変更です。

## articles/ai-services/openai/concepts/prompt-engineering.md{#item-884584}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn how to use prompt engineering to optimize your work with Azure OpenAI Service.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 08/29/2024
+ms.date: 03/26/2025
 ms.custom: references_regions, build-2023, build-2023-dataai
 manager: nitinme
 author: mrbullwinkle
@@ -14,7 +14,7 @@ recommendations: false
 
 # Prompt engineering techniques
 
-GPT-3, GPT-3.5, GPT-4, and GPT-4o models from OpenAI are prompt-based. With prompt-based models, the user interacts with the model by entering a text prompt, to which the model responds with a text completion. This completion is the model’s continuation of the input text.
+GPT-3, GPT-3.5, GPT-4, and GPT-4o models from OpenAI are prompt-based. With prompt-based models, the user interacts with the model by entering a text prompt, to which the model responds with a text completion. This completion is the model’s continuation of the input text. These techniques are note recommended for o-series models.
 
 While these models are extremely powerful, their behavior is also very sensitive to the prompt. This makes prompt construction an important skill to develop.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトエンジニアリングに関するテクニックの修正"
}
```

### Explanation
この変更では、「prompt-engineering.md」ファイルが修正され、いくつかの文言が追加および削除されました。主な変更点は、ファイルの日付が2024年8月29日から2025年3月26日に変更されたことです。また、プロンプトエンジニアリングの技術に関する説明文に、「These techniques are note recommended for o-series models」という新しい文が追加されました。この追加により、読者はOシリーズモデルにはこれらの技術が推奨されないことを理解できるようになります。他の部分については大きな変更はなく、内容全体を通じてプロンプトエンジニアリングの重要性が引き続き強調されています。この修正は、情報の正確性と関連性を補強するための軽微な更新です。

## articles/ai-services/openai/concepts/provisioned-migration.md{#item-68e143}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-openai
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 03/10/2025
+ms.date: 03/26/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -120,7 +120,7 @@ In addition to the updates for the hourly payment model, in December 2024 new [A
 |gpt-4| 0613, 1106-Preview, 0125-Preview|
 |gpt-4-turbo| 2024-04-09|
 |gpt-4-32k| 0613|
-|gpt-4o| 2042-05-13, 2024-08-06|
+|gpt-4o| 2024-05-13, 2024-08-06|
 |gpt-4o-mini| 2024-07-18|
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされた移行に関する日付の更新"
}
```

### Explanation
この変更では、「provisioned-migration.md」ファイルが修正され、いくつかの文言が更新されました。特に注目すべきポイントは、文書の日付が2025年3月10日から2025年3月26日に変更されたことです。さらに、gpt-4oモデルに関する行において、モデルのバージョン情報が少し修正されました。具体的には、日付形式の変化を反映し、モデルのリリース日付が正確に表記されています。この更新は、情報の最新性と正確性を確保するための軽微な変更であり、読者にとっても重要な内容となります。全体的に、文書は依然としてプロビジョニングされた移行の具体的な詳細を提供する役割を果たしています。

## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Azure OpenAI Service provisioned throughput
 description: Learn about provisioned throughput and Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 08/07/2024
+ms.date: 03/26/2025
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
 ms.author: mbullwin #chrhoder
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングスループットに関する日付の更新"
}
```

### Explanation
この変更では、「provisioned-throughput.md」ファイルが修正され、いくつかの文言が更新されました。主な変更点は、文書の日付が2024年8月7日から2025年3月26日に変更されたことです。この変更は、情報が最新のものであることを反映しています。文書自体は、Azure OpenAIサービスにおけるプロビジョニングスループットの概念について学ぶためのリソースを提供するもので、他の内容には大きな変更は見られません。この軽微な更新は、ドキュメンテーションの正確性を維持するために重要です。

## articles/ai-services/openai/concepts/red-teaming.md{#item-0916c9}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI Service
 description: Learn about how red teaming and adversarial testing are an essential practice in the responsible development of systems and features using large language models (LLMs)
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 11/30/2024
+ms.date: 03/27/2025
 manager: nitinme
 author: mrbullwinkle
 ms.author: mbullwin
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レッドチーミングに関する日付の更新"
}
```

### Explanation
この変更では、「red-teaming.md」ファイルが修正され、主に文書の日付が更新されました。具体的には、2024年11月30日から2025年3月27日に変更されています。この日付の更新は、文書の新しい情報を反映し、最新の内容を提供することを目的としています。文書のテーマであるレッドチーミングと逆境テストは、大規模な言語モデル（LLM）を用いたシステムや機能の責任ある開発に欠かせない実践について説明しており、他の内容には特に大きな変更はありません。軽微な更新ながら、文書の正確性と信頼性を保つためには重要なステップです。

## articles/ai-services/openai/concepts/system-message.md{#item-10456c}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI Service
 description: Learn about how to construct system messages also know as metaprompts to guide an AI system's behavior.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 09/20/2024
+ms.date: 03/27/2025
 ms.custom:
   - ignite-2023
 manager: nitinme
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "システムメッセージに関する日付の更新"
}
```

### Explanation
この変更では、「system-message.md」ファイルが修正され、文書の日付が更新されました。具体的には、日付が2024年9月20日から2025年3月27日に変更されています。この変更は、文書の情報を最新に保つことを目的としており、システムメッセージまたはメタプロンプトの構築方法に関する内容を提供しています。システムメッセージは、AIシステムの振る舞いを導く重要な要素であり、文書全体の主旨や価値に影響を与えない範囲での軽微な更新です。この修正により、文書の信頼性が向上し、読者に正確な情報を提供することができます。

## articles/ai-services/openai/concepts/understand-embeddings.md{#item-736ec2}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn more about how the Azure OpenAI embeddings API uses cosine si
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: tutorial
-ms.date: 10/6/2024
+ms.date: 03/27/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "埋め込みに関する日付の更新"
}
```

### Explanation
この変更では、「understand-embeddings.md」ファイルの更新により、文書の日付が変更されました。具体的には、元の日付である2024年10月6日から新しい日付である2025年3月27日に修正されています。この更新は、Azure OpenAI 埋め込み API の機能の説明を含むコンテンツについて、最新の情報を反映させることを目的としています。埋め込み技術は、AIシステムのパフォーマンスを向上させるために重要であり、この修正により、読者に対して質の高い情報を提供し続けることが可能となります。軽微な更新ではありますが、文書の整合性と新鮮さを保つためには重要な措置です。

## articles/ai-services/openai/encrypt-data-at-rest.md{#item-765ec8}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: mrbullwinkle
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 12/02/2024
+ms.date: 03/27/2025
 ms.author: mbullwin
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ暗号化に関する日付の更新"
}
```

### Explanation
この変更では、「encrypt-data-at-rest.md」ファイルの日付が修正されました。元の日付である2024年12月2日が、2025年3月27日に変更されています。この更新は、データが静止状態にあるときの暗号化に関するコンテンツが最新の情報を反映するために行われました。暗号化はデータ保護の重要な側面であり、この軽微な変更により、文書の正確性と信頼性が向上します。コンテンツの更新は、ユーザーに対して有益な情報を常に提供するために必要な措置です。

## articles/ai-services/openai/faq.yml{#item-6deb71}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ metadata:
   manager: nitinme
   ms.service: azure-ai-openai
   ms.topic: faq
-  ms.date: 08/13/2024
+  ms.date: 03/27/2025
   ms.author: mbullwin
   author: mrbullwinkle
 title: Azure OpenAI Service frequently asked questions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQファイルの日付更新"
}
```

### Explanation
この変更は、「faq.yml」ファイルにおける日付の修正を示しています。具体的には、旧日付の2024年8月13日が新日付の2025年3月27日に変更されました。この更新は、Azure OpenAI サービスに関するよくある質問のセクションを最新の情報に保つために行われました。時期を適切に反映させることで、ユーザーが信頼できる情報を得られるようにすることが目的とされています。この軽微な更新は、情報の正確性を維持し、読者のニーズに応えるために重要です。

## articles/ai-services/openai/how-to/business-continuity-disaster-recovery.md{#item-0d0259}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Considerations for implementing Business Continuity and Disaster Re
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 12/03/2024
+ms.date: 03/27/2025
 author: mrbullwinkle    
 ms.author: mbullwin
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "事業継続と災害復旧に関する日付の更新"
}
```

### Explanation
この変更は、「business-continuity-disaster-recovery.md」ファイルの日付の修正を示しています。元の日付2024年12月3日は、2025年3月27日に変更されました。この更新は、事業継続と災害復旧に関する実装に関して最新の情報を提供するために行われたものです。内容の日付を新しくすることで、ユーザーがより信頼性のある情報を得られるようにすることが目的です。この軽微な更新は、文書全体の正確性や関連性を維持し、読者の信頼を高めるために重要です。

## articles/ai-services/openai/how-to/chat-markup-language.md{#item-e61acf}

<details>
<summary>Diff</summary>
````diff
@@ -6,15 +6,15 @@ author: mrbullwinkle #dereklegenzoff
 ms.author: mbullwin #delegenz
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 12/02/2024
+ms.date: 03/27/2025
 manager: nitinme
 keywords: ChatGPT
 ---
 
 # Chat Markup Language ChatML (Preview)
 
 > [!IMPORTANT]
-> Using GPT-3.5-Turbo models with the completion endpoint as described in this article remains in preview and is only possible with `gpt-35-turbo` version (0301) which is [slated for retirement as early as August 1, 2024](../concepts/model-retirements.md#current-models). We strongly recommend using the [GA Chat Completion API/endpoint](./chatgpt.md). The Chat Completion API is the recommended method of interacting with the GPT-3.5-Turbo models. The Chat Completion API is also the only way to access the GPT-4 models.
+> Using GPT-3.5-Turbo models with the completion endpoint as described in this article remains in preview and is only possible with `gpt-35-turbo` version (0301) which was [retired for standard deployment in February 2025](../concepts/model-retirements.md#current-models). We strongly recommend using the [GA Chat Completion API/endpoint](./chatgpt.md) or the [Responses API](./responses.md). The Chat Completion API is the recommended method of interacting with the GPT-3.5-Turbo models. The Chat Completion API is also the only way to access the GPT-4 models.
 
 The following code snippet shows the most basic way to use the GPT-3.5-Turbo models with ChatML. If this is your first time using these models programmatically we recommend starting with our [GPT-35-Turbo & GPT-4 Quickstart](../chatgpt-quickstart.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ChatMLに関する注意事項の更新"
}
```

### Explanation
この変更は、「chat-markup-language.md」ファイルにおいて、注意事項の内容及び日付が修正されたことを示しています。具体的には、旧日付の2024年12月2日が新日付の2025年3月27日に更新され、GPT-3.5-Turboモデルが記載されている内容も変更されました。特に、モデルが2025年2月に標準デプロイメントとしてリタイアしたことに言及され、より明確な情報が提供されています。さらに、利用を推奨するAPIとして「GA Chat Completion API/endpoint」または「Responses API」が加えられています。このマイナーアップデートは、ユーザーに対して最新の推奨事項やリリース状況を提供し、正確な情報を示すために重要です。

## articles/ai-services/openai/how-to/chatgpt.md{#item-ae297a}

<details>
<summary>Diff</summary>
````diff
@@ -1,18 +1,18 @@
 ---
-title: Work with the GPT-35-Turbo and GPT-4 models 
+title: Work with chat completion models
 titleSuffix: Azure OpenAI Service
-description: Learn about the options for how to use the GPT-35-Turbo and GPT-4 models.
+description: Learn about the options for how to use models with the chat completions API
 author: mrbullwinkle #dereklegenzoff
 ms.author: mbullwin #delegenz
 ms.service: azure-ai-openai
 ms.custom: build-2023, build-2023-dataai, devx-track-python
 ms.topic: how-to
-ms.date: 09/05/2024
+ms.date: 03/26/2025
 manager: nitinme
 keywords: ChatGPT
 ---
 
-# Work with the GPT-3.5-Turbo, GPT-4 models, and GPT-4o models
+# Work with chat completions models
 
 GPT-3.5-Turbo, GPT-4, and GPT-4o series models are language models that are optimized for conversational interfaces. The models behave differently than the older GPT-3 models. Previous models were text-in and text-out, which means they accepted a prompt string and returned a completion to append to the prompt. However, the latest models are conversation-in and message-out. The models expect input formatted in a specific chat-like transcript format. They return a completion that represents a model-written message in the chat. This format was designed specifically for multi-turn conversations, but it can also work well for nonchat scenarios.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "タイトルと説明の更新および日付の修正"
}
```

### Explanation
この変更は、「chatgpt.md」ファイルに関するもので、ドキュメントのタイトル、説明、および日付が修正されています。具体的には、タイトルが「Work with the GPT-35-Turbo and GPT-4 models」から「Work with chat completion models」に変更され、説明も「Learn about the options for how to use the GPT-35-Turbo and GPT-4 models.」から「Learn about the options for how to use models with the chat completions API」に更新されました。加えて、日付が2024年9月5日から2025年3月26日に変更されています。

このアップデートは、最新のAPI仕様や使用方法に関する情報をより具体的に示すことを目的としており、ユーザーに対して最新の情報を提供するために重要です。また、GPT-3.5およびGPT-4モデルに対する説明が、会話型インターフェースに特化した最新のモデルの利用方法に合わせて改善されています。

## articles/ai-services/openai/how-to/completions.md{#item-79f39a}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to generate or manipulate text, including code by using t
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 08/29/2024
+ms.date: 03/26/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -17,7 +17,7 @@ recommendations: false
 Azure OpenAI Service provides a **completion endpoint** that can be used for a wide variety of tasks. The endpoint supplies a simple yet powerful text-in, text-out interface to any [Azure OpenAI model](../concepts/models.md). To trigger the completion, you input some text as a prompt. The model generates the completion and attempts to match your context or pattern. Suppose you provide the prompt "As Descartes said, I think, therefore" to the API. For this prompt, Azure OpenAI returns the completion endpoint " I am" with high probability.
 
 > [!IMPORTANT]
-> Unless you have a specific use case that requires the completions endpoint, we recommend instead using the [chat completions endpoint](./chatgpt.md) which allows you to take advantage of the latest models like GPT-4o, GPT-4o mini, and GPT-4 Turbo. 
+> Unless you have a specific use case that requires the completions endpoint, we recommend instead using the [responses API](./responses.md) of [chat completions endpoint](./chatgpt.md) which allows you to take advantage of the latest models like GPT-4o, GPT-4o mini, and GPT-4 Turbo. 
 
 The best way to start exploring completions is through the playground in [Azure AI Foundry](https://ai.azure.com). It's a simple text box where you enter a prompt to generate a completion. You can start with a simple prompt like this one:
 
@@ -36,7 +36,7 @@ The completion results that you see can differ because the Azure OpenAI API prod
 The simple text-in, text-out interface means you can "program" the Azure OpenAI model by providing instructions or just a few examples of what you'd like it to do. The output success generally depends on the complexity of the task and quality of your prompt. A general rule is to think about how you would write a word problem for a pre-teenage student to solve. A well-written prompt provides enough information for the model to know what you want and how it should respond.
 
 > [!NOTE]
-> The model training data can be different for each model type. The [latest model's training data currently extends through September 2021 only](/azure/ai-services/openai/concepts/models). Depending on your prompt, the model might not have knowledge of related current events.
+> The model training data can be different for each model type. Depending on your prompt, the model might not have knowledge of related current events.
 
 ## Design prompts
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "説明と日付の更新"
}
```

### Explanation
この変更は、「completions.md」ファイルにおいて、主に説明文と日付の修正が行われています。具体的には、最初の部分で日付が2024年8月29日から2025年3月26日に更新され、API推奨エンドポイントの変更が反映されています。特に、従来の「chat completions endpoint」に加えて「responses API」が紹介され、より包括的な使用方法を示す内容となっています。

この修正は、ユーザーに対して最新の情報を提供するために重要であり、特定のユースケースが必要な場合を除いて、最新のモデルを利用するための最適な方法を強調しています。また、モデルのトレーニングデータや応答の質についての注意事項も更新され、ユーザーがAPIの利用をより理解しやすくなっています。

## articles/ai-services/openai/how-to/dotnet-migration.md{#item-64142b}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: mbullwin
 ms.service: azure-ai-openai
 ms.custom: devx-track-dotnet
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 03/27/2025
 manager: nitinme
 ---
 
@@ -25,7 +25,7 @@ Stable releases of `Azure.AI.OpenAI` are associated with a corresponding stable
 dotnet add package Azure.AI.OpenAI
 ```
 
-Beta releases of `Azure.AI.OpenAI` are associated with a corresponding preview Azure OpenAI Service API version label, for example, `2024-10-01-preview`.
+Beta releases of `Azure.AI.OpenAI` are associated with a corresponding preview Azure OpenAI Service API version label, for example, `2024-03-01-preview`.
 
 ```dotnetcli
 dotnet add package Azure.AI.OpenAI --prerelease
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付およびベータ版のAPIバージョンラベルの更新"
}
```

### Explanation
この変更は、「dotnet-migration.md」ファイルにおいて、日付とベータ版のAPIバージョンラベルが修正されています。具体的には、文書の日付が2024年11月19日から2025年3月27日に更新され、ベータ版リリースに関連付けられるAzure OpenAI Service APIのバージョンラベルが「2024-10-01-preview」から「2024-03-01-preview」に変更されました。

この修正は、最新の情報を反映するために重要であり、ユーザーが使用する際の正確性を保つことに寄与しています。特にベータ版に関する情報の更新は、新しいバージョンを適切に利用するための支援となり、開発者は自分のプロジェクトに最新の追加機能を導入しやすくなります。

## articles/ai-services/openai/how-to/embeddings.md{#item-e38d07}

<details>
<summary>Diff</summary>
````diff
@@ -6,22 +6,22 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: devx-track-python
 ms.topic: how-to
-ms.date: 08/29/2024
+ms.date: 03/27/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
 ---
 # Learn how to generate embeddings with Azure OpenAI
 
-An embedding is a special format of data representation that can be easily utilized by machine learning models and algorithms. The embedding is an information dense representation of the semantic meaning of a piece of text. Each embedding is a vector of floating point numbers, such that the distance between two embeddings in the vector space is correlated with semantic similarity between two inputs in the original format. For example, if two texts are similar, then their vector representations should also be similar. Embeddings power vector similarity search in Azure Databases such as [Azure Cosmos DB for MongoDB vCore](/azure/cosmos-db/mongodb/vcore/vector-search) , [Azure SQL Database](/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications?view=azuresql&preserve-view=true#vector-search) or [Azure Database for PostgreSQL - Flexible Server](/azure/postgresql/flexible-server/how-to-use-pgvector).
+An embedding is a special format of data representation that can be easily utilized by machine learning models and algorithms. The embedding is an information dense representation of the semantic meaning of a piece of text. Each embedding is a vector of floating point numbers, such that the distance between two embeddings in the vector space is correlated with semantic similarity between two inputs in the original format. For example, if two texts are similar, then their vector representations should also be similar. Embeddings power vector similarity search in Azure Databases such as [Azure Cosmos DB for NoSQL](/azure/cosmos-db/nosql/vector-search), [Azure Cosmos DB for MongoDB vCore](/azure/cosmos-db/mongodb/vcore/vector-search), [Azure SQL Database](/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications?view=azuresql&preserve-view=true#vector-search) or [Azure Database for PostgreSQL - Flexible Server](/azure/postgresql/flexible-server/how-to-use-pgvector).
 
 ## How to get embeddings
 
 To obtain an embedding vector for a piece of text, we make a request to the embeddings endpoint as shown in the following code snippets:
 
 # [console](#tab/console)
 ```console
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME/embeddings?api-version=2024-02-01\
+curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME/embeddings?api-version=2024-10-21\
   -H 'Content-Type: application/json' \
   -H 'api-key: YOUR_API_KEY' \
   -d '{"input": "Sample Document goes here"}'
@@ -35,7 +35,7 @@ from openai import AzureOpenAI
 
 client = AzureOpenAI(
   api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version = "2024-06-01",
+  api_version = "2024-10-21",
   azure_endpoint =os.getenv("AZURE_OPENAI_ENDPOINT") 
 )
 
@@ -47,26 +47,6 @@ response = client.embeddings.create(
 print(response.model_dump_json(indent=2))
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-[!INCLUDE [Deprecation](../includes/deprecation.md)]
-
-```python
-import openai
-
-openai.api_type = "azure"
-openai.api_key = "YOUR_API_KEY"
-openai.api_base = "https://YOUR_RESOURCE_NAME.openai.azure.com"
-openai.api_version = "2024-06-01"
-
-response = openai.Embedding.create(
-    input="Your text string goes here",
-    engine="YOUR_DEPLOYMENT_NAME"
-)
-embeddings = response['data'][0]['embedding']
-print(embeddings)
-```
-
 # [C#](#tab/csharp)
 ```csharp
 using Azure;
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "APIバージョンの変更と内容の簡素化"
}
```

### Explanation
この変更は、「embeddings.md」ファイルにおいて、いくつかの重要な更新が行われています。主な変更点は、APIのバージョンが「2024-06-01」から「2024-10-21」に更新されたことと、一部の記述が簡素化されたことです。特に、Azure Cosmos DBの記述が改訂され、データベースが「NoSQL」として明示されるようになりました。

また、古いPythonコードのスニペットが削除され、必要な情報をより明確にするために、内容が短縮されました。これにより、ユーザーが最新のエンドポイントとAPIバージョンを利用して埋め込みを取得する方法を理解しやすくなります。この変更は、開発者が実際の適用時に遭遇する可能性のある混乱を避けるために重要です。全体として、内容の整理と最新技術への対応が強化されています。

## articles/ai-services/openai/how-to/fine-tuning.md{#item-5c0e85}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: build-2023, build-2023-dataai, devx-track-python, references_regions
 ms.topic: how-to
-ms.date: 02/27/2025
+ms.date: 03/27/2025
 author: mrbullwinkle
 ms.author: mbullwin
 zone_pivot_groups: openai-fine-tuning
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、「fine-tuning.md」ファイルにおいて、日付が2025年2月27日から2025年3月27日に更新されただけの修正です。この修正は、文書の内容を最新の情報に保つために重要です。更新された日付は、ユーザーが提供される情報の信頼性を判断する上で役立ち、新しいガイダンスや機能が利用可能であることを示しています。このような小規模な更新でも、ドキュメントの正確性と有用性を保つためには欠かせない要素です。

## articles/ai-services/openai/how-to/json-mode.md{#item-50fa9e}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 08/29/2024
+ms.date: 03/26/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -51,7 +51,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-03-01-preview"
+  api_version="2025-03-01-preview"
 )
 
 response = client.chat.completions.create(
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンと日付の更新"
}
```

### Explanation
この変更は、「json-mode.md」ファイルにおいて、APIのバージョンと日付が更新されたことを反映しています。具体的には、日付が2024年8月29日から2025年3月26日に変更され、APIバージョンが「2024-03-01-preview」から「2025-03-01-preview」に更新されています。

このような更新は文書の正確性を維持し、最新の技術やバージョンに対応するために不可欠です。ユーザーにとっては、最新のAPIを使用するための指針となり、開発プロセスにおいて適切な情報を得る手助けとなります。全体として、この小規模な修正は、ドキュメンテーションの信頼性と有用性を保つために重要です。

## articles/ai-services/openai/how-to/latency.md{#item-80eeec}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about performance and latency with Azure OpenAI
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 09/20/2024
+ms.date: 03/26/2025
 author: mrbullwinkle 
 ms.author: mbullwin
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、「latency.md」ファイルにおける日付が更新されたことを示しています。具体的には、日付が2024年9月20日から2025年3月26日に変更されています。

この修正は、文書の情報が最新であることを確保し、ユーザーに対して信頼性のあるデータを提供するためのものです。日付の更新は、ユーザーにとって新しい情報が提供されていることを示し、現行の技術に基づいた内容を参照する以外にも、将来的な更新の可能性を示唆しています。全体として、この小規模な修正はドキュメントの正確性を保つために重要です。

## articles/ai-services/openai/how-to/migration.md{#item-3013aa}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: mbullwin
 ms.service: azure-ai-openai
 ms.custom: devx-track-python
 ms.topic: how-to
-ms.date: 09/26/2024
+ms.date: 03/27/2025
 manager: nitinme
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、「migration.md」ファイルにおいて、日付が更新されたことを示しています。具体的には、日付が2024年9月26日から2025年3月27日に変更されています。

この日付の更新は、ドキュメントの内容を最新の情報に合わせるためのもので、ユーザーが正確かつ信頼性のある情報を参照できるようにすることを目的としています。文書の更新情報を常に最新の状態に保つことは、利用者が最新の技術や手法に基づいた内容を扱う上で非常に重要です。全体として、この小規模な修正は、ドキュメントの正確性と有用性を維持することに寄与しています。

## articles/ai-services/openai/how-to/monitor-openai.md{#item-fcba4d}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Monitor Azure OpenAI Service
 description: Start here to learn how to use Azure Monitor tools like Log Analytics to capture and analyze metrics and data logs for your Azure OpenAI Service.
-ms.date: 08/20/2024
+ms.date: 03/26/2025
 ms.custom: horz-monitor, subject-monitoring
 ms.topic: conceptual
 author: mrbullwinkle
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、「monitor-openai.md」ファイルにおいて、文書の日付が更新されたことを示しています。具体的には、日付が2024年8月20日から2025年3月26日に変更されています。

この更新は、ユーザーに最新の情報を提供するためのものであり、文書の信頼性を高める役割を果たしています。最新の日付を表示することにより、読者が現在の状況や関連する技術についての最新の指針を得ることができるようになります。このような小規模な修正でも、正確な情報に基づいたコンテンツを維持することが重要であるため、この変更はドキュメントの整合性を保つために不可欠です。

## articles/ai-services/openai/how-to/provisioned-get-started.md{#item-c8df1c}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom: openai
 ms.topic: how-to
 author: mrbullwinkle
 ms.author: mbullwin
-ms.date: 09/20/2024
+ms.date: 03/26/2025
 recommendations: false
 ---
 
@@ -136,14 +136,13 @@ The inferencing code for provisioned deployments is the same a standard deployme
 
 
 ```python
-    #Note: The openai-python library support for Azure OpenAI is in preview. 
     import os
     from openai import AzureOpenAI
 
     client = AzureOpenAI(
         azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
         api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-        api_version="2024-02-01"
+        api_version="2024-10-21"
     )
 
     response = client.chat.completions.create(
@@ -203,7 +202,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
     azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
     api_key=os.getenv("AZURE_OPENAI_API_KEY"),
-    api_version="2024-02-01",
+    api_version="2024-10-21",
     max_retries=5,# default is 2
 )
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンと日付の更新"
}
```

### Explanation
この変更は、「provisioned-get-started.md」ファイルにおいて、APIバージョンと日付が更新されたことを示しています。具体的には、日付が2024年9月20日から2025年3月26日に変更され、APIバージョンが「2024-02-01」から「2024-10-21」に変更されています。

これにより、ユーザーは最新のAPIに基づく手順を確認できるようになり、進化する技術に対応した情報を得ることができます。また、日付の更新は文書の信頼性を高め、コンテンツが最新の状態であることを示しています。このような小規模な修正は、ユーザーがアプリケーションの開発や実装を行う際に、最新の情報に基づいた正確な手順を提供するために重要です。全体として、この更新はユーザー体験の向上に寄与します。

## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Azure OpenAI Service Provisioned Throughput Units (PTU) onboarding
 description: Learn about provisioned throughput units onboarding and Azure OpenAI. 
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 10/18/2024
+ms.date: 03/27/2025
 manager: nitinme
 author: mrbullwinkle 
 ms.author: mbullwin 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、「provisioned-throughput-onboarding.md」ファイルの日付情報が更新されたことを示しています。具体的には、日付が2024年10月18日から2025年3月27日に変更されています。

この修正は、ユーザーに対して最新の情報を提供し、ドキュメントの信頼性を向上させる目的があります。特に、コンテンツに記載されている手順やガイダンスが時代に即したものであることを示すために、日付の更新は重要です。このような小規模な修正であっても、正確な情報を維持することで、ユーザーはより効果的にAzure OpenAIのサービスを利用できるようになります。全体として、この変更は文書の質を高め、読者に信頼できる情報源を提供することを目的としています。

## articles/ai-services/openai/how-to/reproducible-output.md{#item-8d515c}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 09/20/2024
+ms.date: 03/26/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -50,7 +50,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-02-01"
+  api_version="2024-10-21"
 )
 
 for i in range(3):
@@ -79,7 +79,7 @@ for i in range(3):
 $openai = @{
    api_key     = $Env:AZURE_OPENAI_API_KEY
    api_base    = $Env:AZURE_OPENAI_ENDPOINT # like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
-   api_version = '2024-02-01' # may change in the future
+   api_version = '2024-10-21' # may change in the future
    name        = 'YOUR-DEPLOYMENT-NAME-HERE' # name you chose for your deployment
 }
 
@@ -145,7 +145,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-02-01"
+  api_version="2024-10-21"
 )
 
 for i in range(3):
@@ -174,7 +174,7 @@ for i in range(3):
 $openai = @{
    api_key     = $Env:AZURE_OPENAI_API_KEY
    api_base    = $Env:AZURE_OPENAI_ENDPOINT # like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
-   api_version = '2024-02-01' # may change in the future
+   api_version = '2024-10-21' # may change in the future
    name        = 'YOUR-DEPLOYMENT-NAME-HERE' # name you chose for your deployment
 }
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンと日付の更新"
}
```

### Explanation
この変更は、「reproducible-output.md」ファイルに対して行われ、主にAPIバージョンと日付が更新されています。具体的には、従来の日付である2024年9月20日が2025年3月26日に変更され、またAPIバージョンが「2024-02-01」から「2024-10-21」に変更されています。

このような修正は、ユーザーに最新の技術情報を提供し、ドキュメントの内容が時代に即していることを保証するために重要です。特にAPIに関連する情報は頻繁に更新されるため、正しいバージョン番号を提供することで、ユーザーが正確な手順を追ってアプリケーションを実装できるようになります。

全体として、この変更はユーザーエクスペリエンスの向上と、最新の情報に基づく利用促進に寄与しています。特に、これらの更新は信頼性と文書の一貫性を保つために不可欠です。

## articles/ai-services/openai/how-to/switching-endpoints.yml{#item-1cbadc}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ metadata:
   author: mrbullwinkle
   ms.author: mbullwin
   manager: nitinme
-  ms.date: 08/29/2024
+  ms.date: 03/27/2025
   ms.service: azure-ai-openai
   ms.topic: how-to
   ms.custom:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、「switching-endpoints.yml」ファイルの日付情報を更新するもので、具体的には「ms.date」が2024年8月29日から2025年3月27日に変更されています。

日付の更新は、文書が新しい情報や変更を反映していることを示す重要な要素であり、読者に対して最新のコンテンツを提供するために必要です。この修正により、ユーザーは、Azure OpenAIサービスのエンドポイント切り替えに関する手順が正確であり、利用する際に信頼できる情報に基づいていることを確認できます。

このような小規模な更新でも、情報の正確性と関連性を確保することは重要であり、ユーザーエクスペリエンスを向上させるために貢献しています。

## articles/ai-services/openai/how-to/weights-and-biases-integration.md{#item-8ae868}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-openai
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/10/2024
+ms.date: 03/27/2025
 author: mrbullwinkle
 ms.author: mbullwin
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、「weights-and-biases-integration.md」ファイルに対するもので、主に「ms.date」の情報が更新されています。具体的には、日付が2024年11月10日から2025年3月27日に変更されています。

文書の日付の更新は、コンテンツが最新の情報を反映していることを視覚的に示すものであり、特にユーザーが情報の鮮度を重視する技術文書においては重要です。この修正によって、ユーザーはWeights and Biasesの統合に関する最新の手順を参照できるようになり、その結果、より効果的にAzure OpenAIサービスを利用することができます。

全体として、この小さな変更は、情報の正確性を維持し、ユーザーの信頼を高めるために重要です。

## articles/ai-services/openai/how-to/work-with-code.md{#item-b193c2}

<details>
<summary>Diff</summary>
````diff
@@ -5,17 +5,17 @@ description: Learn how to use the Codex models on Azure OpenAI to handle a varie
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 09/20/2024
+ms.date: 03/26/2025
 author: mrbullwinkle
 ms.author: mbullwin
 ---
 
-# Codex models and Azure OpenAI Service
+# Completion models and code with Azure OpenAI Service
 
 > [!IMPORTANT]
-> This article was authored and tested against the [legacy code generation models](/azure/ai-services/openai/concepts/legacy-models). These models use the completions API, and its prompt/completion style of interaction. If you wish to test the techniques described in this article verbatim we recommend using the `gpt-35-turbo-instruct` model which allows access to the completions API. However, for code generation the chat completions API and the latest GPT-4o models will yield the best results, but the prompts would need to be converted to the conversational style specific to interacting with those models.
+> This article was authored and tested against the [legacy code generation models](/azure/ai-services/openai/concepts/legacy-models). These models use the completions API, and its prompt/completion style of interaction. If you wish to test the techniques described in this article verbatim we recommend using the `gpt-35-turbo-instruct` model which allows access to the completions API. However, for code generation the chat completions API and the latest GPT-4o and o-series models will yield the best results. To use these newer models these prompts would need to be converted to the conversational style specific to interacting with those models.
 
-The Codex model series is a descendant of our GPT-3 series that's been trained on both natural language and billions of lines of code. It's most capable in Python and proficient in over a dozen languages including C#, JavaScript, Go, Perl, PHP, Ruby, Swift, TypeScript, SQL, and even Shell.
+The Codex model series was a descendant of our GPT-3 series that's been trained on both natural language and billions of lines of code. It's most capable in Python and proficient in over a dozen languages including C#, JavaScript, Go, Perl, PHP, Ruby, Swift, TypeScript, SQL, and even Shell.
 
 You can use Codex for a variety of tasks including:
 
@@ -27,7 +27,7 @@ You can use Codex for a variety of tasks including:
 
 ## How to use completions models with code
 
-Here are a few examples of using Codex that can be tested in the [Azure AI Foundry](https://ai.azure.com) playground with a deployment of a Codex series model, such as `code-davinci-002`.
+Here are a few examples of using completion models that can be tested in the [Azure AI Foundry](https://ai.azure.com) playground with a deployment of `gpt-35-turbo-instruct`.
 
 ### Saying "Hello" (Python)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "タイトルと内容の更新"
}
```

### Explanation
この変更は、「work-with-code.md」ファイルに対するもので、文書のタイトルやいくつかの内容の修正が含まれています。主な変更点は、記事のタイトルが「Codex models and Azure OpenAI Service」から「Completion models and code with Azure OpenAI Service」に変更されたことです。また、本文中のいくつかの文も修正されています。

具体的には、文書の日付が2024年9月20日から2025年3月26日に更新され、最新の情報が反映されています。また、Codexモデルに関する説明文が微調整され、新しいモデルである「GPT-4o」と「o-seriesモデル」についての言及が追加されました。しかし、Codex自身の説明が歴史的背景として保持されている点も特徴的です。

この更新により、読者は最新のモデルに関する正確な情報を得ることができ、コーディングタスクにおいてどのモデルを使用すべきかの指針が示されています。全体として、この変更は、ユーザーにとって文書の関連性を高め、理解を深めるために重要です。

## articles/ai-services/openai/how-to/working-with-models.md{#item-7ec098}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about managing model deployment life cycle, updates, & retirement.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 08/29/2024
+ms.date: 03/26/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, devx-track-azurepowershell
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、「working-with-models.md」ファイルに対するもので、主に文書の日付が更新されています。具体的には、日付が2024年8月29日から2025年3月26日に変更されました。

この日付の更新は、文書が最新の情報であることを示すために重要であり、特に技術文書においては、常に最新の情報が反映されていることが求められます。このファイルは、モデルのデプロイメントライフサイクル、更新、退役に関する情報を提供しており、読者が最新のベストプラクティスにアクセスできるようになっています。

全体として、この小さな変更は文書の信頼性を向上させ、ユーザーにとっての利便性を高めるために重要です。

## articles/ai-services/openai/includes/batch/batch-rest.md{#item-bcccd9}

<details>
<summary>Diff</summary>
````diff
@@ -240,7 +240,7 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/files/{output_file_id}/c
 Cancels an in-progress batch. The batch will be in status `cancelling` for up to 10 minutes, before changing to `cancelled`, where it will have partial results (if any) available in the output file.
 
 ```http
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches/{batch_id}/cancel?api-version=2024-10-21 \
+curl -X POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches/{batch_id}/cancel?api-version=2024-10-21 \
   -H "api-key: $AZURE_OPENAI_API_KEY" 
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "HTTPメソッドの追加"
}
```

### Explanation
この変更は、「batch-rest.md」ファイルに対するもので、バッチのキャンセルに関するリクエストで使用するHTTPメソッドを更新しました。具体的には、バッチをキャンセルするためのcURLコマンドが修正され、単に`curl`から`curl -X POST`に変更されました。

この修正により、バッチキャンセル操作が正しく実行されることが保障され、ユーザーがHTTPのPOSTメソッドを使用する必要があることが明確になっています。この変更は、API利用者が意図した通りにリクエストを送信できるようにするため、重要な内容の更新です。

全体として、これにより、ユーザーがAzure OpenAI APIを使用する際の正確性が向上し、期待通りの動作を実現する手助けとなります。

## articles/ai-services/openai/includes/chat-completion.md{#item-1deb8a}

<details>
<summary>Diff</summary>
````diff
@@ -16,23 +16,19 @@ keywords: ChatGPT
 
 The following code snippet shows the most basic way to interact with models that use the Chat Completion API. If this is your first time using these models programmatically, we recommend that you start with the [chat completions quickstart](../chatgpt-quickstart.md).
 
-> [!NOTE]  
-> In the Azure OpenAI documentation, we refer to GPT-3.5-Turbo and GPT-35-Turbo interchangeably. The official name of the model on OpenAI is `gpt-3.5-turbo`. For Azure OpenAI, because of Azure-specific character constraints, the underlying model name is `gpt-35-turbo`.
-
-# [OpenAI Python 1.x](#tab/python-new)
 
 ```python
 import os
 from openai import AzureOpenAI
 
 client = AzureOpenAI(
   api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version = "2024-02-01",
+  api_version = "2024-10-21",
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
 )
 
 response = client.chat.completions.create(
-    model="gpt-35-turbo", # model = "deployment_name".
+    model="gpt-4o", # model = "deployment_name".
     messages=[
         {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
         {"role": "user", "content": "Who were the founders of Microsoft?"}
@@ -77,7 +73,7 @@ print(response.choices[0].message.content)
     }
   ],
   "created": 1698892410,
-  "model": "gpt-35-turbo",
+  "model": "gpt-4o",
   "object": "chat.completion",
   "usage": {
     "completion_tokens": 73,
@@ -111,87 +107,18 @@ print(response.choices[0].message.content)
 Microsoft was founded by Bill Gates and Paul Allen. They established the company on April 4, 1975. Bill Gates served as the CEO of Microsoft until 2000 and later as Chairman and Chief Software Architect until his retirement in 2008, while Paul Allen left the company in 1983 but remained on the board of directors until 2000.
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-[!INCLUDE [Deprecation](../includes/deprecation.md)]
-
-```python
-import os
-import openai
-openai.api_type = "azure"
-openai.api_version = "2024-02-01" 
-openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # Your Azure OpenAI resource's endpoint value.
-openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
-
-response = openai.ChatCompletion.create(
-    engine="gpt-35-turbo", # The deployment name you chose when you deployed the GPT-3.5-Turbo or GPT-4 model.
-    messages=[
-        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
-        {"role": "user", "content": "Who were the founders of Microsoft?"}
-    ]
-)
-
-print(response)
-
-# To print only the response content text:
-# print(response['choices'][0]['message']['content'])
-```
-
-### Output
-
-JSON formatting added artificially for ease of reading.
-
-```json
-{
-  "choices": [
-    {
-      "finish_reason": "stop",
-      "index": 0,
-      "message": {
-        "content": "The founders of Microsoft are Bill Gates and Paul Allen. They co-founded the company in 1975.",
-        "role": "assistant"
-      }
-    }
-  ],
-  "created": 1679014551,
-  "id": "chatcmpl-6usfn2yyjkbmESe3G4jaQR6bsScO1",
-  "model": "gpt-3.5-turbo-0301",
-  "object": "chat.completion",
-  "usage": {
-    "completion_tokens": 86,
-    "prompt_tokens": 37,
-    "total_tokens": 123
-  }
-}
-
-```
-
----
-
-> [!NOTE]  
-> The following parameters aren't available with the new GPT-35-Turbo and GPT-4 models: `logprobs`, `best_of`, and `echo`. If you set any of these parameters, you get an error.
-
 Every response includes `finish_reason`. The possible values for `finish_reason` are:
 
 * **stop**: API returned complete model output.
 * **length**: Incomplete model output because of the `max_tokens` parameter or the token limit.
 * **content_filter**: Omitted content because of a flag from our content filters.
 * **null**: API response still in progress or incomplete.
 
-Consider setting `max_tokens` to a slightly higher value than normal, such as 300 or 500. A higher value ensures that the model doesn't stop generating text before it reaches the end of the message.
-
-## Model versioning
-
-> [!NOTE]  
-> The version `gpt-35-turbo` is equivalent to the `gpt-3.5-turbo` model from OpenAI.
-
-Unlike previous GPT-3 and GPT-3.5 models, the `gpt-35-turbo` model and the `gpt-4` and `gpt-4-32k` models will continue to be updated. When you create a [deployment](../how-to/create-resource.md#deploy-a-model) of these models, you also need to specify a model version.
-
-You can find the model retirement dates for these models on the [models](../concepts/models.md) page.
+Consider setting `max_tokens` to a slightly higher value than normal. A higher value ensures that the model doesn't stop generating text before it reaches the end of the message.
 
 ## Work with the Chat Completion API
 
-OpenAI trained the GPT-35-Turbo and GPT-4 models to accept input formatted as a conversation. The messages parameter takes an array of message objects with a conversation organized by role. When you use the Python API, a list of dictionaries is used.
+OpenAI trained chat completion models to accept input formatted as a conversation. The messages parameter takes an array of message objects with a conversation organized by role. When you use the Python API, a list of dictionaries is used.
 
 The format of a basic chat completion is:
 
@@ -232,11 +159,11 @@ To trigger a response from the model, end with a user message to indicate that i
 
 ### Message prompt examples
 
-The following section shows examples of different styles of prompts that you can use with the GPT-35-Turbo and GPT-4 models. These examples are only a starting point. You can experiment with different prompts to customize the behavior for your own use cases.
+The following section shows examples of different styles of prompts that you can use with chat completions models. These examples are only a starting point. You can experiment with different prompts to customize the behavior for your own use cases.
 
 #### Basic example
 
-If you want the GPT-35-Turbo model to behave similarly to [chat.openai.com](https://chat.openai.com/), you can use a basic system message like `Assistant is a large language model trained by OpenAI.`
+If you want you chat completions model to behave similarly to [chatgpt.com](https://chatgpt.com/), you can use a basic system message like `Assistant is a large language model trained by OpenAI.`
 
 ```
 {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
@@ -309,15 +236,13 @@ The examples so far show the basic mechanics of interacting with the Chat Comple
 
 Every time a new question is asked, a running transcript of the conversation so far is sent along with the latest question. Because the model has no memory, you need to send an updated transcript with each new question or the model will lose the context of the previous questions and answers.
 
-# [OpenAI Python 1.x](#tab/python-new)
-
 ```python
 import os
 from openai import AzureOpenAI
 
 client = AzureOpenAI(
   api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version = "2024-02-01",
+  api_version = "2024-10-21",
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")  # Your Azure OpenAI resource's endpoint value.
 )
 
@@ -328,48 +253,21 @@ while True:
     conversation.append({"role": "user", "content": user_input})
 
     response = client.chat.completions.create(
-        model="gpt-35-turbo", # model = "deployment_name".
+        model="gpt-4o", # model = "deployment_name".
         messages=conversation
     )
 
     conversation.append({"role": "assistant", "content": response.choices[0].message.content})
     print("\n" + response.choices[0].message.content + "\n")
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-```python
-import os
-import openai
-openai.api_type = "azure"
-openai.api_version = "2024-02-01" 
-openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # Your Azure OpenAI resource's endpoint value.
-openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
-
-conversation=[{"role": "system", "content": "You are a helpful assistant."}]
-
-while True:
-    user_input = input()      
-    conversation.append({"role": "user", "content": user_input})
-
-    response = openai.ChatCompletion.create(
-        engine="gpt-35-turbo", # The deployment name you chose when you deployed the GPT-35-turbo or GPT-4 model.
-        messages=conversation
-    )
-
-    conversation.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
-    print("\n" + response['choices'][0]['message']['content'] + "\n")
-```
-
----
-
 When you run the preceding code, you get a blank console window. Enter your first question in the window and then select the `Enter` key. After the response is returned, you can repeat the process and keep asking questions.
 
 ## Manage conversations
 
-The previous example runs until you hit the model's token limit. With each question asked, and answer received, the `messages` list grows in size. The token limit for `gpt-35-turbo` is 4,096 tokens. The token limits for `gpt-4` and `gpt-4-32k` are 8,192 and 32,768, respectively. These limits include the token count from both the message list sent and the model response. The number of tokens in the messages list combined with the value of the `max_tokens` parameter must stay under these limits or you receive an error.
+The previous example runs until you hit the model's token limit. With each question asked, and answer received, the `messages` list grows in size. The token limit for chat completions models varies across models and versions The token limits for `gpt-4` and `gpt-4-32k` are 8,192 and 32,768, respectively. These limits include the token count from both the message list sent and the model response. The number of tokens in the messages list combined with the value of the `max_tokens` parameter must stay under these limits or you receive an error. Consult the [models page](../concepts/models.md) for each models token limits/context windows.
 
-It's your responsibility to ensure that the prompt and completion fall within the token limit. For longer conversations, you need to keep track of the token count and only send the model a prompt that falls within the limit.
+It's your responsibility to ensure that the prompt and completion fall within the token limit. For longer conversations, you need to keep track of the token count and only send the model a prompt that falls within the limit. Alternatively, with the [responses API](../how-to/responses.md) you can have the API handle truncation/management of the conversation history for you.
 
 > [!NOTE]  
 > We strongly recommend that you stay within the [documented input token limit](../concepts/models.md) for all models, even if you discover that you can exceed that limit.
@@ -378,16 +276,14 @@ The following code sample shows a simple chat loop example with a technique for
 
 The code uses tiktoken `0.5.1`. If you have an older version, run `pip install tiktoken --upgrade`.
 
-# [OpenAI Python 1.x](#tab/python-new)
-
 ```python
 import tiktoken
 import os
 from openai import AzureOpenAI
 
 client = AzureOpenAI(
   api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version = "2024-02-01",
+  api_version = "2024-10-21",
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")  # Your Azure OpenAI resource's endpoint value.
 )
 
@@ -457,86 +353,6 @@ while True:
     print("\n" + response.choices[0].message.content + "\n")
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-```python
-import tiktoken
-import openai
-import os
-
-openai.api_type = "azure"
-openai.api_version = "2024-02-01" 
-openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # Your Azure OpenAI resource's endpoint value.
-openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
-
-system_message = {"role": "system", "content": "You are a helpful assistant."}
-max_response_tokens = 250
-token_limit = 4096
-conversation = []
-conversation.append(system_message)
-
-def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
-    """Return the number of tokens used by a list of messages."""
-    try:
-        encoding = tiktoken.encoding_for_model(model)
-    except KeyError:
-        print("Warning: model not found. Using cl100k_base encoding.")
-        encoding = tiktoken.get_encoding("cl100k_base")
-    if model in {
-        "gpt-3.5-turbo-0613",
-        "gpt-3.5-turbo-16k-0613",
-        "gpt-4-0314",
-        "gpt-4-32k-0314",
-        "gpt-4-0613",
-        "gpt-4-32k-0613",
-        }:
-        tokens_per_message = 3
-        tokens_per_name = 1
-    elif model == "gpt-3.5-turbo-0301":
-        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
-        tokens_per_name = -1  # if there's a name, the role is omitted
-    elif "gpt-3.5-turbo" in model:
-        print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
-        return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
-    elif "gpt-4" in model:
-        print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
-        return num_tokens_from_messages(messages, model="gpt-4-0613")
-    else:
-        raise NotImplementedError(
-            f"""num_tokens_from_messages() is not implemented for model {model}."""
-        )
-    num_tokens = 0
-    for message in messages:
-        num_tokens += tokens_per_message
-        for key, value in message.items():
-            num_tokens += len(encoding.encode(value))
-            if key == "name":
-                num_tokens += tokens_per_name
-    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
-    return num_tokens
-
-while True:
-    user_input = input("")     
-    conversation.append({"role": "user", "content": user_input})
-    conv_history_tokens = num_tokens_from_messages(conversation)
-
-    while conv_history_tokens + max_response_tokens >= token_limit:
-        del conversation[1] 
-        conv_history_tokens = num_tokens_from_messages(conversation)
-
-    response = openai.ChatCompletion.create(
-        engine="gpt-35-turbo", # The deployment name you chose when you deployed the GPT-35-Turbo or GPT-4 model.
-        messages=conversation,
-        temperature=0.7,
-        max_tokens=max_response_tokens,
-    )
-
-    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
-    print("\n" + response['choices'][0]['message']['content'] + "\n")
-```
-
----
-
 In this example, after the token count is reached, the oldest messages in the conversation transcript are removed. For efficiency, `del` is used instead of `pop()`. We start at index 1 to always preserve the system message and only remove user or assistant messages. Over time, this method of managing the conversation can cause the conversation quality to degrade as the model gradually loses the context of the earlier portions of the conversation.
 
 An alternative approach is to limit the conversation duration to the maximum token length or a specific number of turns. After the maximum token limit is reached, the model would lose context if you were to allow the conversation to continue. You can prompt the user to begin a new conversation and clear the messages list to start a new conversation with the full token limit available.
@@ -545,8 +361,6 @@ The token counting portion of the code demonstrated previously is a simplified v
 
 ## Troubleshooting
 
-Here's a troubleshooting tip.
-
 ### Don't use ChatML syntax or special tokens with the chat completion endpoint
 
 Some customers try to use the [legacy ChatML syntax](../how-to/chat-markup-language.md) with the chat completion endpoints and newer models. ChatML was a preview capability that only worked with the legacy completions endpoint with the `gpt-35-turbo` version 0301 model. This model is [slated for retirement](../concepts/model-retirements.md). If you attempt to use ChatML syntax with newer models and the chat completion endpoint, it can result in errors and unexpected model response behavior. We don't recommend this use. This same issue can occur when using common special tokens.
@@ -564,5 +378,5 @@ Some customers try to use the [legacy ChatML syntax](../how-to/chat-markup-langu
 ## Next steps
 
 * [Learn more about Azure OpenAI](../overview.md).
-* Get started with the GPT-35-Turbo model with [the GPT-35-Turbo quickstart](../chatgpt-quickstart.md).
+* Get started with chat completions models with [the chat completion quickstart](../chatgpt-quickstart.md).
 * For more examples, see the [Azure OpenAI Samples GitHub repository](https://github.com/Azure-Samples/openai).
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデル名とAPIバージョンの更新"
}
```

### Explanation
この変更は、「chat-completion.md」ファイルにおける大規模な修正であり、特に新しい情報が追加され、古い情報が削除されています。主な変更点は、モデル名が「gpt-35-turbo」から「gpt-4o」に変更され、APIバージョンが「2024-02-01」から「2024-10-21」にアップデートされたことです。

具体的には、以下のような重要な変更が行われました：

1. **モデル名の変更**: 使用するモデルが「gpt-35-turbo」から「gpt-4o」に切り替わり、これにより機能や性能が向上することが期待されます。
2. **APIバージョンの更新**: 新しいAPIバージョンが導入されたことで、最新の機能と最適化を利用することが可能になります。
3. **不要な情報の削除**: 古い情報や冗長な説明が削除され、文書がスリム化され、読みやすさが向上しました。具体的には、古いコード例や使用されなくなったパラメータに関する詳細が大幅に削減されました。

このように、大規模な変更が行われたことで、ユーザーは最新のモデルとAPI機能にアクセスできるようになり、使い勝手が向上します。また、文書全体が整理されたことで、情報の理解が容易になっています。

## articles/ai-services/openai/includes/embeddings-python.md{#item-3ad1b9}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 11/06/2023
+ms.date: 03/26/2025
 author: mrbullwinkle #noabenefraim
 ms.author: mbullwin
 ---
@@ -135,9 +135,9 @@ RESOURCE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
 openai.api_type = "azure"
 openai.api_key = API_KEY
 openai.api_base = RESOURCE_ENDPOINT
-openai.api_version = "2022-12-01"
+openai.api_version = "2024-10-21"
 
-url = openai.api_base + "/openai/deployments?api-version=2022-12-01" 
+url = openai.api_base + "/openai/deployments?api-version=2024-10-21" 
 
 r = requests.get(url, headers={"api-key": API_KEY})
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンと日付の更新"
}
```

### Explanation
この変更は、「embeddings-python.md」ファイルに対するもので、主にAPIのバージョンとドキュメントの日付が更新されました。具体的には、次の点が修正されています：

1. **日付の更新**: ファイルの最終更新日が「2023年11月6日」から「2025年3月26日」に変更されました。これにより、ドキュメントが最新の情報に基づいていることを示しています。

2. **APIバージョンの変更**: 使用されるAPIバージョンが「2022-12-01」から「2024-10-21」に更新されました。これにより、APIが最新の機能や改善を反映していることが期待されます。

これらの変更は、ユーザーに対して、最新のAPIバージョンを使用するよう促すものであり、ドキュメントがより信頼できるソースとして位置づけられるようになったことを示しています。また、ドキュメントの維持管理が行き届いていることも示しています。

## articles/ai-services/openai/includes/fine-tune.md{#item-be8a2e}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: mrbullwinkle
 ms.author: mbullwin 
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 09/01/2023
+ms.date: 03/26/2025
 manager: nitinme
 keywords: ChatGPT
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、「fine-tune.md」ファイルに対するもので、主にドキュメントの日付が更新されました。具体的には、以下の点が修正されています：

1. **日付の更新**: 最終更新日が「2023年9月1日」から「2025年3月26日」に変更されました。この変更により、ドキュメントが現在の状況を反映していることが示されています。

このタイプの更新は、ユーザーに最新の情報を提供し、ドキュメントの信頼性を向上させるために重要です。日付が更新されることで、利用者はこの情報が最新のものであると認識することができます。

## articles/ai-services/openai/includes/language-overview/dotnet.md{#item-46e881}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Azure OpenAI C# support
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 11/18/2024
+ms.date: 03/27/2025
 ---
 
 
@@ -34,10 +34,12 @@ The [stable release](/dotnet/api/azure.ai.openai.azureopenaiclientoptions.servic
 
 The [preview release](/dotnet/api/azure.ai.openai.azureopenaiclientoptions.serviceversion?view=azure-dotnet-preview&preserve-view=true) can currently target:
 
-- `2024-06-01`
 - `2024-08-01-preview`
 - `2024-09-01-preview`
 - `2024-10-01-preview`
+- `2024-12-01-preview`
+- `2025-01-01-preview`
+- `2025-03-01-preview`
 
 ## Installation
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付とバージョンの更新"
}
```

### Explanation
この変更は、「dotnet.md」ファイルに対するもので、主にドキュメントの日付とAPIバージョンのリストが更新されました。具体的には、以下の点が修正されています：

1. **日付の更新**: 最終更新日が「2024年11月18日」から「2025年3月27日」に変更されました。これにより、ドキュメントの情報が最新であることが確認できます。

2. **バージョンの追加**: 使用可能なプレビューリリースのリストに新しいバージョンが追加されました。具体的には、「2024-12-01-preview」、「2025-01-01-preview」、「2025-03-01-preview」の3つのバージョンが新たに加わり、将来的なリリースをサポートすることが示されています。

これらの更新は、ユーザーに対して最新の情報を提供し、特にプログラミング環境や使用するAPIバージョンに関して、より有用なリソースであることを保証するために重要です。

## articles/ai-services/openai/includes/language-overview/go.md{#item-a289f2}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Azure OpenAI Go support
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 11/18/2024
+ms.date: 03/27/2025
 ---
 
 [Source code](https://github.com/Azure/azure-sdk-for-go/tree/main/sdk/ai/azopenai) | [Package (pkg.go.dev)](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/ai/azopenai) | [API reference documentation](../../reference.md) | [Package reference documentation](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/ai/azopenai)   [Samples](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/ai/azopenai#pkg-examples)
@@ -15,9 +15,9 @@ ms.date: 11/18/2024
 
 Unlike the Azure OpenAI client libraries for Python and JavaScript, the Azure OpenAI Go library is targeted to a specific Azure OpenAI API version. Having access to the latest API versions impacts feature availability.
 
-Current Azure OpenAI API version target: `2024-10-01-preview`
+Current Azure OpenAI API version target: `2025-01-01-preview`
 
-This is defined in the [**custom_client.go**](https://github.com/Azure/azure-sdk-for-go/blob/9ebef43f64796118ae206a42821d9f541a231daa/sdk/ai/azopenai/custom_client.go#L37) file.
+This is defined in the [**custom_client.go**](https://github.com/Azure/azure-sdk-for-go/blob/main/sdk/ai/azopenai/custom_client.go) file.
 
 ## Installation
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付とAPIバージョンの更新"
}
```

### Explanation
この変更は、「go.md」ファイルに対するもので、主にドキュメントの日付とAPIバージョンの情報が更新されました。具体的には、以下の点が修正されています：

1. **日付の更新**: 最終更新日が「2024年11月18日」から「2025年3月27日」に変更され、ドキュメントの情報が最新であることが示されています。

2. **APIバージョンの変更**: 「Azure OpenAI Goライブラリ」が対応するAzure OpenAI APIのターゲットバージョンが「2024-10-01-preview」から「2025-01-01-preview」に変更されました。これにより、最新の機能が利用可能であることが示されています。

3. **リンクの修正**: `custom_client.go`ファイルへのリンクが、特定のコミットからメインブランチのリンクに変更されており、最新のコードを参照しやすくなっています。

これらの更新は、ユーザーに対して正確で最新の情報を提供し、特にAPIの使用に関する理解を深めるために重要です。

## articles/ai-services/openai/includes/language-overview/java.md{#item-5edb45}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Azure OpenAI Java support
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 11/18/2024
+ms.date: 03/27/2025
 ---
 
 
@@ -19,7 +19,7 @@ Version selection is controlled by the [`OpenAIServiceVersion`](/java/api/com.az
 
 The latest Azure OpenAI preview API supported is:
 
--`2024-08-01-preview`
+-`2025-01-01-preview`
 
 The latest stable (GA) release supported is:
 
@@ -33,7 +33,7 @@ The latest stable (GA) release supported is:
 <dependency>
     <groupId>com.azure</groupId>
     <artifactId>azure-ai-openai</artifactId>
-    <version>1.0.0-beta.12</version>
+    <version>1.0.0-beta.16</version>
 </dependency>
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付とバージョンの更新"
}
```

### Explanation
この変更は、「java.md」ファイルに対するもので、主に日付やAPIバージョン、依存関係のバージョンに関する情報が更新されました。具体的には、以下の点が修正されています：

1. **日付の更新**: 最終更新日が「2024年11月18日」から「2025年3月27日」に変更され、ドキュメントが最新の情報に基づいていることが示されています。

2. **APIバージョンの変更**: サポートされている最新のAzure OpenAIプレビューAPIバージョンが「2024-08-01-preview」から「2025-01-01-preview」に変更されました。これにより、新しい機能へのアクセスが可能であることが示されています。

3. **依存関係のバージョン更新**: Maven依存関係のバージョンも「1.0.0-beta.12」から「1.0.0-beta.16」に変更され、最新の安定版が反映されています。

これらの変更は、ユーザーが最新の情報や機能を把握しやすくし、Javaを使用したAzure OpenAIの接続を円滑に行えるようにするために重要です。

## articles/ai-services/openai/includes/language-overview/javascript.md{#item-50536a}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Azure OpenAI JavaScript support
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 02/13/2025
+ms.date: 03/27/2025
 ---
 
 [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Reference](../../reference.md) |
@@ -17,7 +17,7 @@ Feature availability in Azure OpenAI is dependent on what version of the REST AP
 
 | Latest GA API | Latest Preview API|
 |:-----|:------|
-|`2024-10-21` |`2025-01-01-preview`|
+|`2024-10-21` |`2025-03-01-preview`|
 
 ## Installation
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付とプレビューAPIバージョンの更新"
}
```

### Explanation
この変更は、「javascript.md」ファイルに対するもので、主に日付と最新のプレビューAPIバージョンに関する情報が更新されました。具体的には、以下の点が修正されています：

1. **日付の更新**: ドキュメントの最終更新日が「2025年2月13日」から「2025年3月27日」に変更され、情報が最新であることを示しています。

2. **プレビューAPIバージョンの変更**: 最新のプレビューAPIバージョンが「2025-01-01-preview」から「2025-03-01-preview」に変更されました。これにより、最新の機能や改良が反映されています。

3. **冗長性の解消**: いくつかの情報が削除され、より簡潔で明確なフォーマットに改善されています。

これらの変更は、Azure OpenAIをJavaScriptで活用する開発者に対して、最新の情報と利用可能な機能を正確に伝えるために重要です。また、ユーザーが正しいバージョンのAPIを使用することを助けます。

## articles/ai-services/openai/includes/language-overview/python.md{#item-9cca6c}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Azure OpenAI Python support
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 11/18/2024
+ms.date: 03/27/2024
 ---
 
 [Library source code](https://github.com/openai/openai-python?azure-portal=true) | [Package (PyPi)](https://pypi.org/project/openai?azure-portal=true) | [Reference](../../reference.md) |
@@ -19,7 +19,7 @@ Feature availability in Azure OpenAI is dependent on what version of the REST AP
 
 | Latest GA API | Latest Preview API|
 |:-----|:------|
-|`2024-10-21` |`2025-01-01-preview`|
+|`2024-10-21` |`2025-03-01-preview`|
 
 ## Installation
 
@@ -488,6 +488,10 @@ print(generate_image.model_dump_json(indent=2))
 
 ---
 
+## Responses API
+
+See the [Responses API](../../how-to/responses.md) documentation.
+
 ## Completions (legacy)
 
 ### completions.create()
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付、プレビューAPIバージョン、および新規セクションの追加"
}
```

### Explanation
この変更は、「python.md」ファイルに対するもので、主に日付の更新、最新のプレビューAPIバージョンの変更、そして新しいセクションの追加が行われました。具体的には、以下のポイントが修正されています：

1. **日付の更新**: ドキュメントの最終更新日が「2024年11月18日」から「2024年3月27日」に変更され、情報がより新しくなりました。

2. **プレビューAPIバージョンの変更**: 最新のプレビューAPIバージョンが「2025-01-01-preview」から「2025-03-01-preview」に更新され、最新の開発状況を反映しています。

3. **新しいセクションの追加**: 「Responses API」という新しいセクションが追加され、関連するドキュメントへのリンクが提供されることで、ユーザーがより多くの情報にアクセスできるようになりました。

4. **冗長性の削減**: 一部の情報が削除され、文書がより明確で簡潔になっています。

これらの変更は、Pythonを使用するAzure OpenAIのユーザーに対して、最新のAPIバージョンと新しい機能についての情報を提供し、ドキュメントの質を向上させることを目的としています。

## articles/ai-services/openai/includes/prompt-chat-completion.md{#item-fd2907}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: mrbullwinkle
 ms.author: mbullwin 
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 02/16/2024
+ms.date: 03/26/2025
 manager: nitinme
 keywords: ChatGPT
 
@@ -15,7 +15,7 @@ keywords: ChatGPT
 This guide doesn't go in-depth into the mechanics behind the message structure for Chat Completions. If you aren't familiar with interacting with Chat Completions models programmatically, we recommend reading our [how-to guide on the Chat Completion API first](../how-to/chatgpt.md).  
 
 > [!NOTE]
-> All of the examples in this section of the guide were tested against a base GPT-4 model in English. If you are reading a localized version of this article in another language, these responses represent a localized translation of the English results. To learn more about potential limitations depending on what language you are using to prompt a model, please consult our [Responsible AI transparency note](/legal/cognitive-services/openai/transparency-note?context=/azure/ai-services/openai/context/context#limitations).  
+> All of the examples in this section of the guide were tested against a base GPT-4 model in English. Some techniques may produce different results with newer models like gpt-4o, and gpt 4.5. If you are reading a localized version of this article in another language, these responses represent a localized translation of the English results. To learn more about potential limitations depending on what language you are using to prompt a model, please consult our [Responsible AI transparency note](/legal/cognitive-services/openai/transparency-note?context=/azure/ai-services/openai/context/context#limitations).  
 
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新されたモデルの情報と日付の変更"
}
```

### Explanation
この変更は、「prompt-chat-completion.md」ファイルに対するもので、日付の更新と例に関する注釈の修正が行われています。具体的には次のような点が挙げられます：

1. **日付の更新**: ドキュメントの最終更新日が「2024年2月16日」から「2025年3月26日」に更新され、最新の情報を反映しています。

2. **モデル情報の更新**: ガイド内の例が「GPT-4」モデルに基づいてテストされたことに加え、新しいモデル「gpt-4o」や「gpt 4.5」が言及されました。これにより、最新のモデルを使用した場合に異なる結果が得られる場合があることが読者に通知されています。

3. **情報の明確化**: モデルにおける応答のローカライズに関する説明は引き続き含まれており、言語による制約や注意点についても言及されています。

これらの変更は、ユーザーが最新のモデルや日付の情報に基づいてガイドを理解し、自身のプロンプトがどのように行われるかを考慮するための重要な情報を提供しています。

## articles/ai-services/openai/includes/prompt-completion.md{#item-d52cc1}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: mrbullwinkle
 ms.author: mbullwin 
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 02/16/2024
+ms.date: 03/26/2025
 manager: nitinme
 keywords: ChatGPT
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、「prompt-completion.md」ファイルに対するもので、主にドキュメントの最終更新日が更新されています。具体的には、以下のポイントが修正されています：

1. **日付の変更**: ドキュメントの日付が「2024年2月16日」から「2025年3月26日」に更新され、最新のコンテンツが反映されています。

この変更により、ユーザーはドキュメントが最新の情報であることを確認でき、信頼性が向上します。特に技術文書では、正確な日付は重要であり、利用者が現在の開発状況を把握するための助けとなります。

## articles/ai-services/openai/includes/python.md{#item-989064}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Walkthrough on how to get started with Azure OpenAI and make your f
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 01/03/2024
+ms.date: 03/26/2025
 ---
 
 <a href="https://github.com/openai/openai-python" target="_blank">Library source code</a> | <a href="https://pypi.org/project/openai/" target="_blank">Package (PyPi)</a> |
@@ -22,22 +22,10 @@ ms.date: 01/03/2024
 
 Install the OpenAI Python client library with:
 
-# [OpenAI Python 1.x](#tab/python-new)
-
 ```console
 pip install openai
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-[!INCLUDE [Deprecation](../includes/deprecation.md)]
-
-```console
-pip install openai==0.28.1
-```
-
----
-
 > [!NOTE]
 > This library is maintained by OpenAI. Refer to the [release history](https://github.com/openai/openai-python/releases) to track the latest updates to the library.
 
@@ -64,16 +52,21 @@ Go to your resource in the Azure portal. The **Keys and Endpoint** can be found
 
 2. Replace the contents of quickstart.py with the following code. Modify the code to add your key, endpoint, and deployment name: 
 
-# [OpenAI Python 1.x](#tab/python-new)
+# [Microsoft Entra ID](#tab/entra)
 
 ```python
 import os
 from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
     
 client = AzureOpenAI(
-    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-    api_version="2024-02-01",
-    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
+    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+    azure_ad_token_provider=token_provider,
+    api_version="2024-10-21"
     )
     
 deployment_name='REPLACE_WITH_YOUR_DEPLOYMENT_NAME' #This will correspond to the custom name you chose for your deployment when you deployed a model. Use a gpt-35-turbo-instruct deployment. 
@@ -85,25 +78,27 @@ response = client.completions.create(model=deployment_name, prompt=start_phrase,
 print(start_phrase+response.choices[0].text)
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
+# [API Key](#tab/key)
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 ```python
 import os
-import openai
-
-openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
-openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
-openai.api_type = 'azure'
-openai.api_version = '2024-02-01' # this might change in the future
-
-deployment_name='REPLACE_WITH_YOUR_DEPLOYMENT_NAME' #This will correspond to the custom name you chose for your deployment when you deployed a model. 
-
+from openai import AzureOpenAI
+    
+client = AzureOpenAI(
+    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
+    api_version="2024-10-21",
+    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
+    )
+    
+deployment_name='REPLACE_WITH_YOUR_DEPLOYMENT_NAME' #This will correspond to the custom name you chose for your deployment when you deployed a model. Use a gpt-35-turbo-instruct deployment. 
+    
 # Send a completion call to generate an answer
 print('Sending a test completion job')
 start_phrase = 'Write a tagline for an ice cream shop. '
-response = openai.Completion.create(engine=deployment_name, prompt=start_phrase, max_tokens=10)
-text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
-print(start_phrase+text)
+response = client.completions.create(model=deployment_name, prompt=start_phrase, max_tokens=10)
+print(start_phrase+response.choices[0].text)
 ```
 
 ---
@@ -128,7 +123,6 @@ Write a tagline for an ice cream shop. The coldest ice cream in town!
 
 Run the code a few more times to see what other types of responses you get as the response won't always be the same.
 
-
 ### Understanding your results
 
 Since our example of `Write a tagline for an ice cream shop.` provides little context, it's normal for the model to not always return expected results. You can adjust the maximum number of tokens if the response seems unexpected or truncated.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "OpenAI Pythonクライアントの更新と実装の変更"
}
```

### Explanation
この変更は、「python.md」ファイルに対するもので、主にOpenAI Pythonクライアントに関する内容と実装方法が更新されています。以下のポイントが重要です：

1. **日付の更新**: ドキュメントの日付が「2024年1月3日」から「2025年3月26日」に変更され、最新の情報を反映しています。

2. **OpenAI Pythonクライアントのコマンド変更**: 以前のバージョン（0.28.1）から最新のバージョン（1.x）への移行が強調されており、インストール手順が簡素化されています。`pip install openai` のコマンドが推奨されています。

3. **APIの利用方法の変更**: APIの呼び出し方法が大きく変わりました。具体的には、Azureの認証メカニズムを使用してトークンを取得するための新しいコードが追加され、従来のAPIキーによる認証から、AzureのIdentityを利用した認証方法に移行しています。この変更により、セキュリティが強化されます。

4. **利用方法の具体例**: Pythonコードの実装例が更新され、`AzureOpenAI`クライアントを使用した新しいAPIの呼び出し方法が示されています。 

これにより、ユーザーは最新の実装基準に従ってOpenAIの機能を利用できるようになりますが、古いAPIに依存していたアプリケーションやスクリプトは動作しなくなる可能性があるため、注意が必要です。

## articles/ai-services/openai/includes/rest.md{#item-071924}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Walkthrough on how to get started with Azure OpenAI and make your f
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 02/02/2023
+ms.date: 03/26/2025
 ---
 
 ## Prerequisites
@@ -38,14 +38,27 @@ Go to your resource in the Azure portal. The **Endpoint and Keys** can be found
 
 In a bash shell, run the following command. You will need to replace `gpt-35-turbo-instruct` with the deployment name you chose when you deployed the `gpt-35-turbo-instruct` model. Entering the model name will result in an error unless you chose a deployment name that is identical to the underlying model name.
 
+# [Microsoft Entra ID](#tab/entra)
+
 ```bash
-curl $AZURE_OPENAI_ENDPOINT/openai/deployments/gpt-35-turbo-instruct/completions?api-version=2024-02-01 \
+curl $AZURE_OPENAI_ENDPOINT/openai/deployments/gpt-35-turbo-instruct/completions?api-version=2024-10-21 \
+  -H "Content-Type: application/json" \
+  -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
+  -d "{\"prompt\": \"Once upon a time\"}"
+```
+
+# [API Key](#tab/key)
+
+```bash
+curl $AZURE_OPENAI_ENDPOINT/openai/deployments/gpt-35-turbo-instruct/completions?api-version=2024-10-21 \
   -H "Content-Type: application/json" \
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -d "{\"prompt\": \"Once upon a time\"}"
 ```
 
-The format of your first line of the command with an example endpoint would appear as follows `curl https://docs-test-001.openai.azure.com/openai/deployments/{YOUR-DEPLOYMENT_NAME_HERE}/completions?api-version=2024-02-01 \`. If you encounter an error double check to make sure that you don't have a doubling of the `/` at the separation between your endpoint and `/openai/deployments`.
+---
+
+The format of your first line of the command with an example endpoint would appear as follows `curl https://docs-test-001.openai.azure.com/openai/deployments/{YOUR-DEPLOYMENT_NAME_HERE}/completions?api-version=2024-10-21 \`. If you encounter an error double check to make sure that you don't have a doubling of the `/` at the separation between your endpoint and `/openai/deployments`.
 
 If you want to run this command in a normal Windows command prompt you would need to alter the text to remove the `\` and line breaks.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新とコマンドの追加"
}
```

### Explanation
この変更は、「rest.md」ファイルに対するもので、主にAPIに関する情報が更新されています。以下のポイントが重要です：

1. **日付の更新**: ドキュメントの日付が「2023年2月2日」から「2025年3月26日」に変更され、最新の情報を反映しています。

2. **APIバージョンの変更**: コマンド内のAPIバージョンが「2024-02-01」から「2024-10-21」に更新されており、最新のバージョンが利用されることが明示されています。

3. **認証方法の追加**: 新たに「Microsoft Entra ID」と「API Key」の両方の認証方法が示され、整数を明確にしたコマンドが追加されています。それにより、ユーザーは性格な認証メカニズムを選べるようになります。

4. **コマンドのフォーマット**: `curl`コマンドの構成が明確に記載され、新しいAPIバージョンに基づいた正確なリクエスト方法が説明されています。また、Windowsのコマンドプロンプト用の修正が必要な場合についても言及されています。

これにより、ユーザーは新しいバージョンのAPIに対する正しいリクエストを送信でき、より効率的にAzure OpenAIサービスを利用できるようになります。

## articles/ai-services/openai/includes/studio.md{#item-eeeaff}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Walkthrough on how to get started with Azure OpenAI and make your f
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 09/19/2023
+ms.date: 03/26/2025
 ---
 
 ## Prerequisites
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントの日付更新"
}
```

### Explanation
この変更は、「studio.md」ファイルに対するもので、主にドキュメントの日付が更新されています。以下のポイントが重要です：

1. **日付の変更**: ドキュメントの日付が「2023年9月19日」から「2025年3月26日」に更新されており、これは最新の情報を示すためです。この更新により、読者は資料が新しいものであることを認識できます。

2. **変更の最小化**: 実際のコンテンツの変更は最小限であり、日付以外には文の削除や追加はありません。これは、ドキュメントの内容が大きく変わっていないことを示しています。

この変更により、ユーザーは最新の文書を基にした情報を得られ、Azure OpenAIに関する現在の実装やガイドラインに沿って作業を行えるようになります。

## articles/ai-services/openai/index.yml{#item-0adb87}

<details>
<summary>Diff</summary>
````diff
@@ -1,17 +1,17 @@
 ### YamlMime:Landing
 
 title: Azure OpenAI Service documentation # < 60 chars
-summary: Azure OpenAI Service provides access to OpenAI's models including the GPT-4o, GPT-4o mini, GPT-4, GPT-4 Turbo with Vision, GPT-3.5-Turbo, DALLE-3 and Embeddings model series with the security and enterprise capabilities of Azure. 
+summary: Azure OpenAI Service provides access to OpenAI's models including o-series, GPT-4o, GPT-4o mini, GPT-4, GPT-4 Turbo with Vision, GPT-3.5-Turbo, DALLE-3 and Embeddings model series with the security and enterprise capabilities of Azure. 
   
 metadata:
   title: Azure OpenAI Service documentation - Quickstarts, Tutorials, API Reference - Azure AI services | Microsoft Docs
-  description: Learn how to use Azure OpenAI's powerful models including the GPT-4o, GPT-4o mini, GPT-4, GPT-4 Turbo with Vision, GPT-3.5-Turbo, DALL-E 3 and Embeddings model series
+  description: Learn how to use Azure OpenAI's powerful models including o-series, GPT-4o, GPT-4o mini, GPT-4, GPT-4 Turbo with Vision, GPT-3.5-Turbo, DALL-E 3 and Embeddings model series
   ms.service: azure-ai-openai
   ms.custom:
   ms.topic: landing-page
   author: mrbullwinkle
   ms.author: mbullwin
-  ms.date: 09/18/2024
+  ms.date: 03/27/2025
 
 # linkListType: architecture | concept | deploy | download | get-started | how-to-guide | learn | overview | quickstart | reference | tutorial | video | whats-new
 # Limits: https://review.learn.microsoft.com/help/contribute/contribute-how-to-write-landing-page?branch=main#limits
@@ -86,17 +86,17 @@ landingContent:
      linkLists:
          - linkListType: get-started
            links:
-             - text: Migrate to OpenAI Python 1.x
-               url: ./how-to/migration.md
-             - text: Manage models
-               url: ./how-to/working-with-models.md
+             - text: Responses API & computer-use-preview
+               url: ./how-to/responses.md
+             - text: Reasoning models
+               url: ./how-to/reasoning.md
              - text: OpenAI versus Azure OpenAI (Python)
                url: ./how-to/switching-endpoints.yml
              - text: Global batch
                url: ./how-to/batch.md
-             - text: Role-based access control (Azure RBAC)
-               url: ./how-to/role-based-access-control.md 
-             - text: GPT-3.5 Turbo & GPT-4
+             - text: Structured outputs
+               url: ./how-to/structured-outputs.md
+             - text: Chat completion models
                url:  ./how-to/chatgpt.md
              - text: Vision-enabled models
                url:  ./how-to/gpt-with-vision.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "要約とリンクリストの更新"
}
```

### Explanation
この変更は、「index.yml」ファイルに対するもので、主に要約とリンクリストが更新されています。以下のポイントが重要です：

1. **要約の修正**: ドキュメントの要約が更新され、「GPT-4o」などのモデル名の表記に変更が加えられています。この変更により、利用可能なモデルの情報がより正確に反映されています。

2. **説明文の更新**: 説明文内でもモデル名が整備されており、誤りや冗長な表現が修正されています。このようにすることで、読者が情報をより理解しやすくなっています。

3. **リンクリストの変更**: 「get-started」リンクリスト内の一部のリンクが更新され、新しいトピックやリソースが追加されています。これにより、ユーザーは最新の情報にアクセスしやすくなっています。特に「Responses API & computer-use-preview」や「Reasoning models」など、新しい項目が導入されています。

4. **日付の更新**: 最後に、ドキュメントの日付が「2024年9月18日」から「2025年3月27日」に変更され、これが最新の情報に基づいていることを強調しています。

これらの変更により、Azure OpenAIサービスに関する情報が最新かつ正確になり、ユーザーが効果的に利用できるようになります。

## articles/ai-services/openai/quickstart.md{#item-7d1656}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom: devx-track-dotnet, devx-track-python, devx-track-extended-java, devx-
 ms.topic: quickstart
 author: mrbullwinkle
 ms.author: mbullwin
-ms.date: 09/05/2024
+ms.date: 03/26/2025
 zone_pivot_groups: openai-quickstart-new
 recommendations: false
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートの日付更新"
}
```

### Explanation
この変更は、「quickstart.md」ファイルに対するもので、主にドキュメントの日付が更新されています。以下のポイントが重要です：

1. **日付の変更**: ドキュメントの日付が「2024年9月5日」から「2025年3月26日」に更新されており、これは最新の情報を示すための修正です。この変更により、読者は資料が近年のものであると認識できます。

2. **その他の項目の変更なし**: 改訂では他の内容に関する変更はなく、日付以外の情報についてはそのままとなっています。これにより、ドキュメントの基本的な情報は保持されています。

この更新は、Azure OpenAIのクイックスタートに関する情報を最新化し、ユーザーがより信頼性の高い情報にアクセスできるようにするために行われました。

## articles/ai-services/openai/supported-languages.md{#item-12c019}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom:
 ms.topic: conceptual
-ms.date: 11/18/2024
+ms.date: 03/27/2025
 ms.author: mbullwin
 zone_pivot_groups: openai-supported-languages
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サポートされている言語の日付更新"
}
```

### Explanation
この変更は、「supported-languages.md」ファイルに対するもので、主に日付が更新されています。以下のポイントが重要です：

1. **日付の変更**: ドキュメントの日付が「2024年11月18日」から「2025年3月27日」に更新されました。この変更により、文書が新しい内容を反映していることが示されます。

2. **内容の変更なし**: 他の情報に関しては変更がなく、基本的な構成はそのまま保持されています。これにより、ドキュメントの信頼性は維持されています。

この更新は、Azure OpenAIに関連するサポート言語の情報を最新化し、読者がアクセスする情報が最新版であることを保証するために行われました。

## articles/ai-services/openai/tutorials/embeddings.md{#item-1f01e7}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's embeddings API for document search
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: tutorial
-ms.date: 08/30/2024
+ms.date: 03/26/2025
 author: mrbullwinkle #noabenefraim
 ms.author: mbullwin
 zone_pivot_groups: "openai-embeddings"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "埋め込みチュートリアルの日付更新"
}
```

### Explanation
この変更は、「embeddings.md」ファイルに対するもので、主に日付が更新されています。以下に主要なポイントを示します：

1. **日付の変更**: 「埋め込み」チュートリアルの日付が「2024年8月30日」から「2025年3月26日」に更新されました。この変更は、ドキュメントの内容が最新であることを示すために重要です。

2. **その他の内容の変更なし**: 日付以外の情報については変更がなく、他の部分はそのまま保持されています。これにより、チュートリアルの主な情報は安定性を保っています。

この更新は、Azure OpenAIの埋め込みAPIに関するチュートリアルの情報を最新化し、ユーザーが信頼できる最新の情報にアクセスできるようにするために行われました。

## articles/ai-services/openai/tutorials/fine-tune.md{#item-8f87b5}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's latest fine-tuning capabilities wit
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: tutorial
-ms.date: 09/09/2024
+ms.date: 03/26/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングチュートリアルの日付更新"
}
```

### Explanation
この変更は、「fine-tune.md」ファイルにおける日付の更新に関連しています。具体的なポイントは次の通りです：

1. **日付の変更**: チュートリアルの日付が「2024年9月9日」から「2025年3月26日」に更新されました。この変更により、ドキュメントが最新の情報を反映していることを示します。

2. **内容の一貫性**: その他の情報やコンテンツは変更されておらず、チュートリアルの構造はそのまま維持されています。これにより、内容の整合性が確保されています。

この更新は、Azure OpenAIの最新のファインチューニング機能に関する情報を最新化し、ユーザーが常に信頼できる情報を得られるようにすることを目的としています。


