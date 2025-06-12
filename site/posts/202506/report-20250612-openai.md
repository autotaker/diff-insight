---
date: '2025-06-12'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:776cc95...MicrosoftDocs:da65020
summary: このドキュメントは、Azure OpenAIサービスにおけるファインチューニングとモデル引退に関する情報を更新したものです。新しい機能として、ファインチューニングに関する文書が具体的な利点や効率を説明し、適用事例やコスト削減の可能性についての詳細が追加されました。また、モデルの引退日が更新され、デプロイメント計画を最新の情報に基づいて立てられるようになっています。特に重大な破壊的変更は報告されていないものの、引退日の延長がデプロイメント戦略に影響を与える可能性があります。さらに、ドキュメントの見出しが整理され、関連リソースへのリンクが提供されることで、情報の把握がしやすくなっています。この更新は、透明性と効率性の向上に寄与するものです。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:776cc95...MicrosoftDocs:da65020){target="_blank"}

# Highlights

## New features
- ファインチューニングに関する文書の更新により、利点や効率をより具体的に説明。
- 特定用途への適用やコスト削減の可能性についての詳細が追加。
- 引退日更新により、モデル利用計画のスケジュールに関する情報が最新化。

## Breaking changes
- 特に重大な破壊的変更は報告されていないが、モデルの引退日が延長されたため、デプロイメント戦略に影響がある可能性。

## Other updates
- ドキュメントのセクションの見出しが整理され、読み手が情報を把握しやすくなった。
- 関連リソースへのリンクが提供され、技術的知識を深めるための参考資料が追加。

# Insights

このドキュメントの更新は、Azure OpenAIサービスにおけるファインチューニングとモデル引退のプロセスに関する情報を最新版に揃えるためのものです。ファインチューニングドキュメントの更新について見てみると、従来のバージョンよりも内容が集約され、非常に詳細な情報が追加されていることがわかります。たとえば、モデル精度の向上や短いプロンプトでの効率的なリクエスト処理の強調は、ファインチューニングを選択する際の重要な判断材料となります。この変更は、モデルをカスタム用途に特化させ、運用コストを低減する具体的な方法を提供することを目的としています。

一方、モデル引退に関するドキュメントの更新は、利用者が最新のスケジュールを基にデプロイメント計画を立てることを可能にします。特に`computer-use-preview`モデルの引退日が延長されたことは、利用者が開発の進行状況を見直す余裕をもたらすでしょう。この変更は、最新の技術動向に即した決定を行うために欠かせない情報を提供し、開発者視点で非常に有用と言えます。このように、いずれのドキュメント更新も、Azure OpenAIサービスを利用する際の透明性と効率性の向上に貢献しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [fine-tuning-considerations.md](#item-71d8ac) | minor update | Azure OpenAI のファインチューニングに関する考察の更新 | modified | 34 | 57 | 91 | 
| [model-retirements.md](#item-03fc2e) | minor update | Azure OpenAI モデルの引退日更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/openai/concepts/fine-tuning-considerations.md{#item-71d8ac}

<details>
<summary>Diff</summary>
````diff
@@ -11,92 +11,69 @@ recommendations: false
 ms.custom:
 ---
 
-# When to use Azure OpenAI fine-tuning
+# Azure OpenAI in Azure AI Foundry Models fine-tuning considerations
 
-When deciding whether or not fine-tuning is the right solution to explore for a given use case, there are some key terms that it's helpful to be familiar with:
+Fine-tuning is the process of taking a pretrained language model and adapting it to perform a specific task or improve its performance on a particular dataset. This involves training the model on a smaller, task-specific dataset while adjusting the model's weights slightly. Fine-tuning leverages the knowledge the model acquired during its initial training on a large, diverse dataset, allowing it to specialize without starting from scratch. This approach is often more efficient and effective than training a new model from scratch, especially for specialized tasks. 
 
-- [Prompt Engineering](/azure/ai-services/openai/concepts/prompt-engineering) is a technique that involves designing prompts for natural language processing models. This process improves accuracy and relevancy in responses, optimizing the performance of the model.
-- [Retrieval Augmented Generation (RAG)](/azure/machine-learning/concept-retrieval-augmented-generation?view=azureml-api-2&preserve-view=true) improves Large Language Model (LLM) performance by retrieving data from external sources and incorporating it into a prompt. RAG allows businesses to achieve customized solutions while maintaining data relevance and optimizing costs.
-- [Fine-tuning](/azure/ai-services/openai/how-to/fine-tuning?pivots=programming-language-studio) retrains an existing Large Language Model using example data, resulting in a new "custom" Large Language Model that has been optimized using the provided examples.
+## Key benefits of fine-tuning
 
-## What is Fine Tuning with Azure OpenAI?
+### Enhanced accuracy and relevance
 
-When we talk about fine tuning, we really mean *supervised fine-tuning* not continuous pre-training or Reinforcement Learning through Human Feedback (RLHF). Supervised fine-tuning refers to the process of retraining pre-trained models on specific datasets, typically to improve model performance on specific tasks or introduce information that wasn't well represented when the base model was originally trained.
+Fine-tuning improves the model's performance on particular tasks by training it with task-specific data. This often results in more accurate and relevant high-quality outputs compared to using general prompts. 
 
-Fine-tuning is an advanced technique that requires expertise to use appropriately. The questions below will help you evaluate whether you're ready for fine-tuning, and how well you've thought through the process. You can use these to guide your next steps or identify other approaches that might be more appropriate.
+Unlike few-shot learning, where only a limited number of examples can be included in a prompt, fine-tuning allows you to train the model on an additional dataset. Fine-tuning helps the model learn more nuanced patterns and improves task performance. 
 
-## Why do you want to fine-tune a model?
+### Efficiency and potential cost savings
 
-- You should be able to clearly articulate a specific use case for fine-tuning and identify the [model](models.md#fine-tuning-models) you hope to fine-tune.
-- Good use cases for fine-tuning include steering the model to output content in a specific and customized style, tone, or format, or scenarios where the information needed to steer the model is too long or complex to fit into the prompt window.
+Fine-tuned models require shorter prompts because they are trained on relevant examples. This process reduces the number of tokens needed in each request, which can lead to cost savings depending on the use case. 
 
-**Common signs you might not be ready for fine-tuning yet:**
+Since fine-tuned models need fewer examples in the prompt, they process requests faster, resulting in quicker response times. 
 
-- No clear use case for fine tuning, or an inability to articulate much more than “I want to make a model better”.
-- If you identify cost as your primary motivator, proceed with caution. Fine-tuning might reduce costs for certain use cases by shortening prompts or allowing you to use a smaller model but there’s a higher upfront cost to training and you'll have to pay for hosting your own custom model. Refer to the [pricing page](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) for more information on Azure OpenAI fine-tuning costs.
-- If you want to add out of domain knowledge to the model, you should start with retrieval augmented generation (RAG) with features like Azure OpenAI's [on your data](./use-your-data.md) or [embeddings](../tutorials/embeddings.md). Often, this is a cheaper, more adaptable, and potentially more effective option depending on the use case and data.
+### Scalability and specialization
 
-## What have you tried so far?
+Fine-tuning applies the extensive pretraining of language models and hones their capabilities for specific applications, making them more efficient and effective for targeted use cases. 
 
-Fine-tuning is an advanced capability, not the starting point for your generative AI journey. You should already be familiar with the basics of using Large Language Models (LLMs). You should start by evaluating the performance of a base model with prompt engineering and/or Retrieval Augmented Generation (RAG) to get a baseline for performance.
+Fine-tuning smaller models can achieve performance levels comparable to larger, more expensive models for specific tasks. This approach reduces computational costs and increases speed, making it a cost-effective scalable solution for deploying AI in resource-constrained environments. 
 
-Having a baseline for performance without fine-tuning is essential for knowing whether or not fine-tuning has improved model performance. Fine-tuning with bad data makes the base model worse, but without a baseline, it's hard to detect regressions.
+## When to fine-tune
 
-**If you are ready for fine-tuning you:**
+Fine-tuning is suited for times when you have a small amount of data and want to improve the performance of your model. Fine-tuning can be for different kinds of use cases - but they often fall into broader categories. 
 
-- Should be able to demonstrate evidence and knowledge of Prompt Engineering and RAG based approaches.
-- Be able to share specific experiences and challenges with techniques other than fine-tuning that were already tried for your use case.
-- Need to have quantitative assessments of baseline performance, whenever possible.  
+* **Reducing prompt engineering overhead**: Many users begin with few-shot learning, appending examples of desired outputs to their system message. Over time, this process can lead to increasingly long prompts, driving up token counts and latency. Fine-tuning lets you embed these examples into the model by training on the expected outputs, which is valuable in scenarios with numerous edge cases.
 
-**Common signs you might not be ready for fine-tuning yet:**
+* **Modifying style and tone**: Fine-tuning helps align model outputs with a desired style or tone, ensuring consistency in applications like customer service chatbots and brand-specific communication.
 
-- Starting with fine-tuning without having tested any other techniques.
-- Insufficient knowledge or understanding on how fine-tuning applies specifically to Large Language Models (LLMs).
-- No benchmark measurements to assess fine-tuning against.
+* **Generating outputs in specific formats or schemas**: Models can be fine-tuned to produce outputs in specific formats or schemas, making them ideal for structured data generation, reports, or formatted responses.
 
-## What isn’t working with alternate approaches?
+* **Enhancing tool usage**: While the chat completions API supports tool calling, listing many tools increases token usage and may lead to hallucinations. Fine-tuning with tool examples enhances accuracy and consistency, even without full tool definitions.
 
-Understanding where prompt engineering falls short should provide guidance on going about your fine-tuning. Is the base model failing on edge cases or exceptions? Is the base model not consistently providing output in the right format, and you can’t fit enough examples in the context window to fix it?
+* **Enhancing retrieval-based performance**: Combining fine-tuning with retrieval methods improves a model’s ability to integrate external knowledge, perform complex tasks, and provide more accurate, context-aware responses. Fine-tuning trains the model to effectively use retrieved data while filtering out irrelevant information.
 
-Examples of failure with the base model and prompt engineering will help you identify the data they need to collect for fine-tuning, and how you should be evaluating your fine-tuned model.
+* **Optimizing for efficiency**: Fine-tuning can also be used to transfer knowledge from a larger model to a smaller one, allowing the smaller model to achieve similar task performance with lower cost and latency. For example, production data from a high-performing model can be used to fine-tune a smaller, more efficient model. This approach helps scale AI solutions while maintaining quality and reducing computational overhead.
 
-Here’s an example: A customer wanted to use GPT-3.5-Turbo to turn natural language questions into queries in a specific, non-standard query language. They provided guidance in the prompt (“Always return GQL”) and used RAG to retrieve the database schema. However, the syntax wasn't always correct and often failed for edge cases. They collected thousands of examples of natural language questions and the equivalent queries for their database, including cases where the model had failed before – and used that data to fine-tune the model. Combining their new fine-tuned model with their engineered prompt and retrieval brought the accuracy of the model outputs up to acceptable standards for use.
+* **Distillation**: Model Distillation uses a large model's outputs to fine-tune a smaller model, allowing it to perform similarly on a specific task, for example collecting production traffic from an o1 deployment and using that as training data to fine tune 4o-mini. This process can cut cost and latency since smaller models can be more efficient. 
 
-**If you are ready for fine-tuning you:**
+## Types of fine-tuning
 
-- Have clear examples on how you have approached the challenges in alternate approaches and what’s been tested as possible resolutions to improve performance.
-- Identified shortcomings using a base model, such as inconsistent performance on edge cases, inability to fit enough few shot prompts in the context window to steer the model, high latency, etc.
+Azure AI Foundry offers multiple types of fine -tuning techniques:
 
-**Common signs you might not be ready for fine-tuning include:**
+* **Supervised fine-tuning**: This allows you to provide custom data (prompt/completion or conversational chat, depending on the model) to teach the base model new skills. This process involves further training the model on a high-quality labeled dataset, where each data point is associated with the correct output or answer. The goal is to enhance the model's performance on a particular task by adjusting its parameters based on the labeled data. This technique works best when there are finite ways of solving a problem and you want to teach the model a particular task and improve its accuracy and conciseness.
 
-- Insufficient knowledge from the model or data source.
-- Inability to find the right data to serve the model.
+* **Reinforcement fine-tuning**: This is a model customization technique, beneficial for optimizing model behavior in highly complex or dynamic environments, enabling the model to learn and adapt through iterative feedback and decision-making. For example, financial services providers can optimize the model for faster, more accurate risk assessments or personalized investment advice. In healthcare and pharmaceuticals, o3-mini can be tailored to accelerate drug discovery, enabling more efficient data analysis, hypothesis generation, and identification of promising compounds. RFT is a great way to fine-tune when there are infinite or high number of ways to solve a problem. The grader rewards the model incrementally and makes reasoning better.
 
-## What data are you going to use for fine-tuning?
+* **Direct Preference Optimization (DPO)**: This is another new alignment technique for large language models, designed to adjust model weights based on human preferences. Unlike Reinforcement Learning from Human Feedback (RLHF), DPO doesn't require fitting a reward model and uses binary preferences for training. This method is computationally lighter and faster, making it equally effective at alignment while being more efficient. You share thenon-preferred and preferred response to the training set and use the DPO technique.
 
-Even with a great use case, fine-tuning is only as good as the quality of the data that you're able to provide. You need to be willing to invest the time and effort to make fine-tuning work. Different models will require different data volumes but you often need to be able to provide fairly large quantities of high-quality curated data.
+You can also stack techniques: first using SFT to create a customized model – optimized for your use case – then using preference fine tuning to align the responses to your specific preferences. During the SFT step, you focus on data quality and representativeness of the tasks, while the DPO step adjusts responses with specific comparisons. 
 
-Another important point is even with high quality data if your data isn't in the necessary format for fine-tuning you'll need to commit engineering resources in order to properly format the data.
+## Challenges and limitations of fine-tuning
 
-| Data   | GPT-3.5-Turbo <br> GPT-4o & GPT-4o mini <br> GPT-4 |
-|---|---|
-| Volume  | Thousands of Examples |
-| Format | Conversational Chat |
+Fine-tuning large language models scan be a powerful technique to adapt them to specific domains and tasks. However, fine-tuning also comes with some challenges and disadvantages that need to be considered before applying it to a real-world problem. Below are a few of these challenges and disadvantages. 
 
-**If you are ready for fine-tuning you:**
-
-- Identified a dataset for fine-tuning.
-- Formatted the dataset appropriately for training.
-- Curated the dataset to ensure quality.
-
-**Common signs you might not be ready for fine-tuning yet:**
-
-- Dataset hasn't been identified yet.
-- Dataset format doesn't match the model you wish to fine-tune.
-
-## How will you measure the quality of your fine-tuned model?
-
-There isn’t a single right answer to this question, but you should have clearly defined goals for what success with fine-tuning looks like. Ideally, this shouldn't just be qualitative but should include quantitative measures of success like utilizing a holdout set of data for validation, as well as user acceptance testing or A/B testing the fine-tuned model against a base model.
+- Fine-tuning requires high-quality, sufficiently large, and representative training data matching the target domain and task. Quality data is relevant, accurate, consistent, and diverse enough to cover the possible scenarios and variations the model will encounter in the real world. Poor-quality or unrepresentative data leads to over-fitting, under-fitting, or bias in the fine-tuned model, which harms its generalization and robustness.
+- Fine-tuning large language models means extra costs associated with training and hosting the custom model.
+- Formatting input/output pairs used to fine-tune a large language model can be crucial to its performance and usability.
+- Fine-tuning may need to be repeated whenever the data is updated, or when an updated base model is released. This involves monitoring and updating regularly.
+- Fine-tuning is a repetitive task (trial and error) so, the hyperparameters need to be carefully set. Fine-tuning requires much experimentation and testing to find the best combination of hyperparameters and settings to achieve desired performance and quality.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI のファインチューニングに関する考察の更新"
}
```

### Explanation
このコードの差分は、Azure OpenAI のファインチューニングに関する文書の内容を更新したものです。主に、ファインチューニングの考慮事項やその重要性に関する情報が明確に説明され、旧いバージョンよりも具体的で詳細な内容に改善されています。具体的には、ファインチューニングの利点、効率、コスト削減の可能性、および特定の用途への適用方法について詳述されています。

また、セクションの見出しが変更され、内容が整理されています。例えば、ファインチューニングの利点として、モデルの精度や関連性の向上が強調され、さらに短いプロンプトでのリクエスト処理の速さについても触れています。これは、ファインチューニングを行うことで得られる効果を具体的に示しており、リーダーに対してその重要性を理解させることを意図しています。

この更新は、ドキュメントの情報量を増加させ、読者にとってファインチューニングのプロセスやその技術的背景を理解しやすくするためのものです。また、技術的な専門知識を持つユーザーに対して、関連リソースへのリンクも提供されています。学生や開発者がファインチューニングを用いる際の参考情報として役立ちます。

## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 04/23/2025
+ms.date: 06/11/2025
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -93,7 +93,7 @@ These models are currently available for use in Azure OpenAI.
 
 | Model                     | Version         | Retirement date                    | Replacement model                    |
 | --------------------------|-----------------|------------------------------------|--------------------------------------|
-| `computer-use-preview`    | 2025-03-11      | No earlier than June 11, 2025      |                                      |
+| `computer-use-preview`    | 2025-03-11      | No earlier than September 1, 2025  |                                      |
 | `dall-e-3`                | 3               | No earlier than June 30, 2025      |                                      |
 | `gpt-35-turbo-16k`        | 0613            | April  30, 2025                    | `gpt-4.1-mini` version: `2025-04-14` |
 | `gpt-35-turbo`            | 1106            | No earlier than July 16, 2025      | `gpt-4.1-mini` version: `2025-04-14` |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI モデルの引退日更新"
}
```

### Explanation
このコードの差分は、Azure OpenAI のモデル引退に関する文書の更新を示しています。具体的には、いくつかのモデルの引退日が変更され、最新の日付に更新されています。

まず、全体の文書日付が2025年4月23日から2025年6月11日に変更され、これにより新しい情報が反映されています。特に、`computer-use-preview` モデルの引退日は、「2025年6月11日」から「2025年9月1日」へと延長されました。この変更は、ユーザーがモデルの使用計画を立てる際に重要な情報であり、デプロイメントの戦略に影響を与える可能性があります。

さらに、他のいくつかのモデルに関する引退日も確認されており、これによりユーザーは最新のモデル情報を把握しやすくなっています。この更新は、技術的文書における信頼性を高め、Azure OpenAI を利用する開発者にとって有意義なリソースとなるでしょう。


