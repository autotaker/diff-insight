---
date: '2026-01-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:00b1f65...MicrosoftDocs:c3cf15d
summary: この更新では、Azure Language サービスのオーケストレーションワークフローに関するドキュメントが改良され、「LUIS」アプリケーションの言及が削除され、「Custom
  question answering」アプリケーションに焦点が当てられました。また、文体調整や日付の修正が行われ、内容が明確化されています。これにより、ユーザーはオーケストレーションワークフローの機能をより深く理解できるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:00b1f65...MicrosoftDocs:c3cf15d){target="_blank"}

# ハイライト

この更新では、Azure Language サービスのオーケストレーションワークフローの概要に関するドキュメントが改良されました。特に、「LUIS」アプリケーションの言及が省かれ、「Custom question answering」アプリケーションに焦点が当てられたことが主要な変更点です。また、文体の調整や日付の修正も行われ、内容の明確化が図られています。

## 新機能

- 「Custom question answering」アプリケーションの表現が強調され、関連情報が強化されました。

## 破壊的な変更

- 「LUIS」アプリケーションの言及が削除されました。

## その他の更新

- ドキュメントの日付が2025年12月17日から2026年1月17日に変更されました。
- 読みやすさを向上させるための文体調整が行われました。
- オーケストレーションワークフローの機能と用途についての説明が精緻化されました。

# インサイト

今回のドキュメントの更新は、Azure の言語サービス利用者にとって非常に有意義であると言えます。「LUIS」の言及が削除された背景としては、技術の進化に伴い、「Custom question answering」機能がより重要視されていることが考えられます。Microsoftがこの機能に注力していることを示しており、ユーザーにはこの新しい構想を理解してもらうことが意図されています。

また、日付の更新は、ドキュメントの正確性を反映しており、ユーザーに対して最新の情報を提供する姿勢を見せています。文体や内容の調整により、ユーザーはオーケストレーションワークフローがどのような状況でどのように活用できるかをより深く理解できるようになりました。これにより、ユーザーの開発プロセスにおいて、ワークフローがどのように役立つかを具体的にイメージできるようになります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [overview.md](#item-53d49f) | minor update | オーケストレーションワークフローの概要の更新 | modified | 20 | 21 | 41 | 


# Modified Contents
## articles/ai-services/language-service/orchestration-workflow/overview.md{#item-53d49f}

<details>
<summary>Diff</summary>
````diff
@@ -1,49 +1,48 @@
 ---
 title: Orchestration workflows - Foundry Tools
 titleSuffix: Foundry Tools
-description: Customize an AI model to connect your Conversational Language Understanding, question answering and LUIS applications.
+description: Customize an AI model to connect your Conversational Language Understanding and Custom question answering applications.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 12/17/2025
+ms.date: 01/17/2026
 ms.author: lajanuar
 ms.custom: language-service-orchestration
 ---
+<!-- markdownlint-disable MD025 -->
 # What is orchestration workflow?
 
+Orchestration workflow is one of the features offered by [Azure Language in Foundry Tools](../overview.md). This cloud-based API service uses machine learning to facilitate the development of orchestration models that seamlessly integrate [Conversational Language Understanding (CLU)](../conversational-language-understanding/overview.md) and [Custom question Answering](../question-answering/overview.md) projects.
+Developers can create an orchestration workflow to iteratively tag utterances, train models, and evaluate their performance before deployment.
 
-Orchestration workflow is one of the features offered by [Azure Language in Foundry Tools](../overview.md). It is a cloud-based API service that applies machine-learning intelligence to enable you to build orchestration models to connect [Conversational Language Understanding (CLU)](../conversational-language-understanding/overview.md), [Question Answering](../question-answering/overview.md) projects and [LUIS](../../luis/what-is-luis.md) applications.
-By creating an orchestration workflow, developers can iteratively tag utterances, train and evaluate model performance before making it available for consumption. 
-To simplify building and customizing your model, the service offers a custom playground that can be accessed through the [Microsoft Foundry](https://ai.azure.com/). You can easily get started with the service by following the steps in this [quickstart](quickstart.md). 
-
+To simplify building and customizing your model, the service offers a custom playground that can be accessed through the [Microsoft Foundry](https://ai.azure.com/). You can easily get started with the service by following the steps in this [quickstart](quickstart.md).
 
 This documentation contains the following article types:
 
 * [Quickstarts](quickstart.md) are getting-started instructions to guide you through making requests to the service.
 * [Concepts](concepts/evaluation-metrics.md) provide explanations of the service functionality and features.
 * [How-to guides](how-to/create-project.md) contain instructions for using the service in more specific or customized ways.
 
-
 ## Example usage scenarios
 
-Orchestration workflow can be used in multiple scenarios across a variety of industries. Some examples are:
+Orchestration workflow can be used in multiple scenarios across various industries. Some examples are:
 
 ### Enterprise chat bot
 
-In a large corporation, an enterprise chat bot might handle a variety of employee affairs. It might be able to handle frequently asked questions served by a custom question answering knowledge base, a calendar specific skill served by conversational language understanding, and an interview feedback skill served by LUIS. The bot needs to be able to appropriately route incoming requests to the correct service. Orchestration workflow allows you to connect those skills to one project that handles the routing of incoming requests appropriately to power the enterprise bot.
+In a large corporation, an enterprise chat bot might handle various employee affairs. For example, it could process frequently asked questions using a custom question answering knowledge base. Additionally, it might manage calendar-specific operations through conversational language understanding capabilities. The bot could also handle interview feedback processing. To support these diverse functions, the bot needs to appropriately route incoming requests to the correct service. Orchestration workflow allows you to connect those skills to one project that handles the routing of incoming requests appropriately to power the enterprise bot.
 
 ## Project development lifecycle
 
-Creating an orchestration workflow project typically involves several different steps. 
+Creating an orchestration workflow project typically involves several different steps.
 
 :::image type="content" source="media/development-lifecycle.png" alt-text="Diagram showing the development lifecycle." lightbox="media/development-lifecycle.png":::
 
 Follow these steps to get the most out of your model:
 
 1. **Define your schema**: Know your data and define the actions and relevant information that needs to be recognized from user's input utterances. Create the [intents](glossary.md#intent) that you want to assign to user's utterances and the projects you want to connect to your orchestration project.
 
-2. **Label your data**: The quality of data tagging is a key factor in determining model performance. 
+2. **Label your data**: The quality of data tagging is a key factor in determining model performance.
 
 3. **Train a model**: Your model starts learning from your tagged data.
 
@@ -59,23 +58,23 @@ Follow these steps to get the most out of your model:
 
 As you use orchestration workflow, see the following reference documentation and samples for Azure Language in Foundry Tools:
 
-|Development option / language  |Reference documentation |Samples  |
-|---------|---------|---------|
-|REST APIs (Authoring)   | [REST API documentation](https://aka.ms/clu-authoring-apis)        |         |
-|REST APIs (Runtime)    | [REST API documentation](/rest/api/language/2023-04-01/conversation-analysis-runtime/analyze-conversation)        |         |
-|C#  (Runtime)   | [C# documentation](/dotnet/api/overview/azure/ai.language.conversations-readme)        | [C# samples](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/cognitivelanguage/Azure.AI.Language.Conversations/samples)        |
-|Python (Runtime)| [Python documentation](/python/api/overview/azure/ai-language-conversations-readme?view=azure-python-preview&preserve-view=true)        | [Python samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/cognitivelanguage/azure-ai-language-conversations/samples) |
+| Development option / language | Reference documentation | Samples |
+| --- | --- | --- |
+| REST APIs (Authoring) | [REST API documentation](https://aka.ms/clu-authoring-apis)| |
+| REST APIs (Runtime) | [REST API documentation](/rest/api/language/2023-04-01/conversation-analysis-runtime/analyze-conversation) |  |
+| C#  (Runtime) | [C# documentation](/dotnet/api/overview/azure/ai.language.conversations-readme) | [C# samples](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/cognitivelanguage/Azure.AI.Language.Conversations/samples) |
+| Python (Runtime) | [Python documentation](/python/api/overview/azure/ai-language-conversations-readme?view=azure-python-preview&preserve-view=true) | [Python samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/cognitivelanguage/azure-ai-language-conversations/samples) |
 
-## Responsible AI 
+## Responsible AI
 
-An AI system includes not only the technology, but also the people who will use it, the people who will be affected by it, and the environment in which it is deployed. Read the transparency note for CLU and orchestration workflow to learn about responsible AI use and deployment in your systems. 
+An AI system includes not only the technology, but also the people who use it, the people who it affects, and the deployment environment. Read the transparency note for CLU and orchestration workflow to learn about responsible AI use and deployment in your systems.
 
 [!INCLUDE [Responsible AI links](../includes/overview-responsible-ai-links.md)]
 
 ## Next steps
 
-* Use the [quickstart article](quickstart.md) to start using orchestration workflow.  
+* Use the [quickstart article](quickstart.md) to start using orchestration workflow.
 
-* As you go through the project development lifecycle, review the [glossary](glossary.md) to learn more about the terms used throughout the documentation for this feature. 
+* As you go through the project development lifecycle, review the [glossary](glossary.md) to learn more about the terms used throughout the documentation for this feature.
 
 * Remember to view the [service limits](service-limits.md) for information such as regional availability.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オーケストレーションワークフローの概要の更新"
}
```

### Explanation
この変更は、Azure Language サービスに関するオーケストレーションワークフローの概要に関するドキュメントの更新です。主な変更点は、記述の簡略化といくつかの情報の明確化です。

1. **説明の修正**: 記述内容が微調整され、"LUIS" アプリケーションという言葉が削除され、"Custom question answering" アプリケーションの表現が強調されました。
2. **日付の更新**: 以前の投稿日が 2025 年 12 月 17 日から 2026 年 1 月 17 日に変更されました。
3. **文体の整備**: 文中の言い回しが調整され、読みやすさが向上しています。
4. **内容の精緻化**: オーケストレーションワークフローの機能と用途についての情報が明確になり、さまざまな使用シナリオや開発ライフサイクルの手順の記載が改善されています。

この変更により、開発者がオーケストレーションワークフローを利用する際の理解が深まり、より効果的にサービスを活用できるようになることを目指しています。全体として、ユーザーのための情報提供が強化されたといえます。


