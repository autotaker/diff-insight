---
date: '2024-10-31'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a68723c...MicrosoftDocs:b16ebe2
summary: |-
  この報告書では、最近の変更内容についての要約を提供します。

  新機能として、いくつかのサービスにリタイア通知が追加され、ユーザーはサービス終了に関する明確な情報を得られるようになりました。また、Azure OpenAIに関するドキュメントが削除され、関連情報が利用できなくなっています。その他の更新としては、ドキュメントが修正され、サービス移行やアクセス制御に関する情報が最新のものに更新されました。

  具体的には、カスタムテキスト分析とカスタム感情分析のリタイア通知が追加され、2025年1月のリタイアに備えるよう促されています。一方で、Azure OpenAIに関する文書の削除は、技術の方向性における大きな変化を示しています。これにより、従来の情報や移行の指針が失われ、ユーザーは新たな代替手段を模索しなければなりません。

  さらに、セキュアデータプレイグラウンドに関する情報も更新され、アクセス制御の強化とリソース管理の透明性が向上しています。この変更は、Azureのユーザーがより安全かつ効率的にサービスを利用できることを目指したものです。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a68723c...MicrosoftDocs:b16ebe2){target="_blank"}

# Highlights

- 新機能として、いくつかのサービスのリタイア通知が追加されました。これにより、ユーザーは今後のサービス終了について明確な情報を得ることができます。
- ブレイキングチェンジとして、Azure OpenAI統合に関するドキュメントが削除されました。これによって、ユーザーはこのリソースを参照できなくなります。
- その他のアップデートでは、ドキュメントが修正され、サービス移行や役割ベースのアクセス制御についての情報が最新のものに更新されました。

## New features
- カスタムヘルス向けテキスト分析のリタイア通知が追加され、ユーザーが2025年1月10日のリタイアに備えられるようになりました。
- カスタム感情分析のクイックスタートにもリタイア通知が追加され、利用者は他のサービスへの移行を考慮するよう促されています。

## Breaking changes
- Azure OpenAI統合に関するすべてのドキュメントが削除されました。これにより、これに関連する情報はすべて利用できなくなります。

## Other updates
- 「QnA Makerからの移行」ドキュメントの一部が修正され、Azure OpenAIに関連する注意書きが削除されました。
- セキュアデータプレイグラウンドに対する情報の更新では、Microsoft Entra IDに関する内容が追加されました。

# Insights

このドキュメントの更新全体を通して、主要なフォーカスは「カスタムテキスト分析 for health」や「カスタム感情分析」などのサービスのリタイア情報を通じて、ユーザーが予期しないサービス停止に対応する準備を促すことにあります。2025年1月に予定されているリタイア情報を早期に伝えることで、現在のユーザーだけでなく、新規プロジェクトを計画するユーザーへの影響を最小限に抑える意図があります。

一方で、Azure OpenAIに関するドキュメントの削除は、技術的な方向性の大きなシフトを表しています。これにより、Azure OpenAIに依存していた情報や移行の指針が突然なくなり、代替手段を探さなければならない状況が生まれました。この背景には、技術やサービス戦略の変更があるかもしれません。

さらに、セキュアデータプレイグラウンドにおける更新では、アクセス制御の強化とリソース管理の明確化が図られており、Azureの利用者がよりセキュアかつ効率的にサービスを利用できるように配慮されています。これにより、開発者は自身のプロジェクトにおいて、適切なアクセス権を取得しやすくなるとともに、セキュリティリスクを低減させることができるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [overview.md](#item-6f599b) | minor update | カスタムヘルス向けテキスト分析のリタイア通知の追加 | modified | 4 | 1 | 5 | 
| [quickstart.md](#item-5bcba3) | minor update | カスタムヘルス向けテキスト分析のリタイア通知の追加 | modified | 3 | 0 | 3 | 
| [azure-openai-integration.md](#item-66f86d) | breaking change | Azure OpenAI統合に関するドキュメントの削除 | removed | 0 | 76 | 76 | 
| [migrate-qnamaker.md](#item-0646f1) | minor update | QnA Makerからの移行に関する注意書きの修正 | modified | 0 | 3 | 3 | 
| [overview.md](#item-631b23) | minor update | カスタム質問応答の概要の更新 | modified | 0 | 3 | 3 | 
| [sdk.md](#item-a86876) | minor update | カスタム質問応答のクイックスタートガイドの更新 | modified | 0 | 3 | 3 | 
| [quickstart.md](#item-32972e) | minor update | カスタム感情分析のクイックスタートガイドの更新 | modified | 3 | 0 | 3 | 
| [secure-data-playground.md](#item-b7fa5e) | minor update | セキュアデータプレイグラウンドの更新 | modified | 20 | 14 | 34 | 


# Modified Contents
## articles/ai-services/language-service/custom-text-analytics-for-health/overview.md{#item-6f599b}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,10 @@ ms.author: jboback
 ms.custom: language-service-custom-ta4h
 ---
 
-# What is custom Text Analytics for health? 
+# What is custom Text Analytics for health?
+
+> [!NOTE]
+> Custom text analytics for health (preview) will be retired on 10 January 2025, please transition to other custom model training services, such as custom named entity recognition in Azure AI Language, by that date. From now to 10 January 2025, you can continue to use custom text analytics for health (preview) in your existing projects without disruption. You can’t create new projects. On 10 January 2025 – workloads running on custom text analytics for health (preview) will be deleted and associated project data will be lost.
 
 Custom Text Analytics for health is one of the custom features offered by [Azure AI Language](../overview.md). It is a cloud-based API service that applies machine-learning intelligence to enable you to build custom models on top of [Text Analytics for health](../text-analytics-for-health/overview.md) for custom healthcare entity recognition tasks.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムヘルス向けテキスト分析のリタイア通知の追加"
}
```

### Explanation
この変更は、「カスタムテキスト分析 for health」の概要に関するドキュメントの内容を更新しました。具体的には、2025年1月10日にサービスがリタイアされる旨の警告を追加しました。この通知には、現在のプロジェクトでは引き続き利用可能であること、ただし新しいプロジェクトの作成はできないこと、リタイア日には関連データが失われることが含まれています。セクションのタイトルは変更されていませんが、重要な注意事項が追加されたことで、ユーザーに対する情報がより明確になりました。

## articles/ai-services/language-service/custom-text-analytics-for-health/quickstart.md{#item-5bcba3}

<details>
<summary>Diff</summary>
````diff
@@ -15,6 +15,9 @@ zone_pivot_groups: usage-custom-language-features
 
 # Quickstart: custom Text Analytics for health
 
+> [!NOTE]
+> Custom text analytics for health (preview) will be retired on 10 January 2025, please transition to other custom model training services, such as custom named entity recognition in Azure AI Language, by that date. From now to 10 January 2025, you can continue to use custom text analytics for health (preview) in your existing projects without disruption. You can’t create new projects. On 10 January 2025 – workloads running on custom text analytics for health (preview) will be deleted and associated project data will be lost.
+
 Use this article to get started with creating a custom Text Analytics for health project where you can train custom models on top of Text Analytics for health for custom entity recognition. A model is artificial intelligence software that's trained to do a certain task. For this system, the models extract healthcare related named entities and are trained by learning from labeled data.
 
 In this article, we use Language Studio to demonstrate key concepts of custom Text Analytics for health. As an example we’ll build a custom Text Analytics for health model to extract the Facility or treatment location from short discharge notes.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムヘルス向けテキスト分析のリタイア通知の追加"
}
```

### Explanation
この変更は、「カスタムテキスト分析 for health」のクイックスタートガイドに関する内容を更新しました。具体的に、2025年1月10日にサービスがリタイアされることを知らせる注意書きが追加されました。この注意書きでは、利用者は引き続き既存のプロジェクトでサービスを使用できるが、新しいプロジェクトを作成することはできず、リタイア日にはすべての関連データが失われることが明記されています。この更新により、ユーザーは将来のサービス終了に備え、他のカスタムモデルトレーニングサービスへの移行を検討する重要性を理解できるようになります。

## articles/ai-services/language-service/question-answering/how-to/azure-openai-integration.md{#item-66f86d}

<details>
<summary>Diff</summary>
````diff
@@ -1,76 +0,0 @@
----
-title: Connect custom question answering with Azure OpenAI on your data 
-titleSuffix: Azure AI services
-description: Learn how to use custom question answering with Azure OpenAI.
-ms.service: azure-ai-language
-author: jboback
-ms.author: jboback
-ms.topic: how-to
-ms.date: 02/09/2024
----
-
-# Connect custom question answering with Azure OpenAI on your data 
-
-Custom question answering enables you to create a conversational layer on your data based on sophisticated Natural Language Processing (NLP) capabilities with enhanced relevance using a deep learning ranker, precise answers, and end-to-end region support. Most use cases for custom question answering rely on finding appropriate answers for inputs by integrating it with chat bots, social media applications and speech-enabled desktop applications. 
-
-AI runtimes however, are evolving due to the development of Large Language Models (LLMs), such as GPT-35-Turbo and GPT-4 offered by [Azure OpenAI](../../../openai/overview.md) can address many chat-based use cases, which you may want to integrate with.
-
-At the same time, customers often require a custom answer authoring experience to achieve more granular control over the quality and content of question-answer pairs, and allow them to address content issues in production. Read this article to learn how to integrate Azure OpenAI On Your Data (Preview) with question-answer pairs from your custom question answering project, using your project's underlying Azure AI Search indexes.
-
-## Prerequisites
-
-* An existing Azure OpenAI resource. If you don't already have an Azure OpenAI resource, then [create one and deploy a model](../../../openai/how-to/create-resource.md).
-* An Azure Language Service resource and custom question answering project. If you don’t have one already, then [create one](../quickstart/sdk.md). 
-    * Be sure that you are assigned at least the [Cognitive Services OpenAI Contributor role](/azure/role-based-access-control/built-in-roles#cognitive-services-openai-contributor) for the Azure OpenAI resource.
-
-
-## Connect Azure OpenAI on your data and custom question answering
-
-1.	Sign in to [Language Studio](https://aka.ms/languageStudio) and navigate to your custom question answering project with an existing deployment.
-
-    :::image type="content" source="../media/question-answering/deployment-sources.png" alt-text="A screenshot showing a custom question answering deployment." lightbox="../media/question-answering/deployment-sources.png":::
-
-1. Select the **Azure Search** tab on the navigation menu to the left.
-
-1. Make a note of your Azure Search details, such as Azure Search resource name, subscription, and location. You will need this information when you connect your Azure AI Search index to Azure OpenAI.
-
-    :::image type="content" source="../media/question-answering/azure-search.png" alt-text="A screenshot showing the Azure search section for a custom question answering project." lightbox="../media/question-answering/azure-search.png":::
-
-1. Navigate to [Azure OpenAI Studio](https://oai.azure.com/) and sign-in with credentials that have access to your Azure OpenAI resource.
-
-1. Select the **Bring your own data** tile to start connecting your search index. You can also select the **Chat playground** tile.
-
-    :::image type="content" source="../../../openai/media/quickstarts/chat-playground-card.png" alt-text="A screenshot of the Azure OpenAI Studio landing page." lightbox="../../../openai/media/quickstarts/chat-playground-card.png":::
-
-    And on the **Assistant setup** tile, select **Add your data (preview)** > **+ Add a data source**.
-
-    :::image type="content" source="../../../openai/media/quickstarts/chatgpt-playground-add-your-data.png" alt-text="A screenshot showing the button for adding your data in Azure OpenAI Studio." lightbox="../../../openai/media/quickstarts/chatgpt-playground-add-your-data.png":::
-
-1. In the pane that appears, select **Azure AI Search** under **Select or add data source**. This will update the screen with **Data field mapping** options depending on your data source.
-        
-    :::image type="content" source="../media/question-answering/data-source-selection.png" alt-text="A screenshot showing data selection options in Azure OpenAI Studio." lightbox="../media/question-answering/data-source-selection.png":::
-                    
-1. Select the subscription, Azure AI Search service and Azure AI Search Index associated with your custom question Answering project. Select the acknowledgment that connecting it will incur usage on your account. Then select **Next**.
-
-    :::image type="content" source="../media/question-answering/azure-search-data-source.png" alt-text="A screenshot showing selection information for Azure AI Search in Azure OpenAI Studio." lightbox="../media/question-answering/azure-search-data-source.png":::
-
-1. On the **Index data field mapping** screen, select *answer* for **Content data** field. The other fields such as **File name**, **Title** and **URL** are optional depending on the nature of your data source.
-
-    :::image type="content" source="../media/question-answering/data-field-mapping.png" alt-text="A screenshot showing index field mapping information for Azure AI Search in Azure OpenAI Studio." lightbox="../media/question-answering/data-field-mapping.png":::
-
-1. Select **Next**. Select a search type from the dropdown menu. You can choose **Keyword** or **Semantic**. semantic” search requires an existing semantic search configuration which may or may not be available for your project.  
-    
-    :::image type="content" source="../media/question-answering/data-management.png" alt-text="A screenshot showing the data management options for Azure AI Search indexes." lightbox="../media/question-answering/data-management.png":::
-    
-1. Review the information you provided, and select **Save and close**. 
-
-    :::image type="content" source="../media/question-answering/confirm-details.png" alt-text="A screenshot showing the confirmation screen." lightbox="../media/question-answering/confirm-details.png":::
-
-1. Your data source has now been added. Select your model's deployment name under the **Configuration** > **Deployment** tab on the menu to the right. 
-
-    :::image type="content" source="../media/question-answering/chat-playground.png" alt-text="A screenshot of the playground page of the Azure OpenAI Studio with sections highlighted." lightbox="../media/question-answering/chat-playground.png":::
-
-You can now start exploring Azure OpenAI capabilities with a no-code approach through the chat playground. It's simply a text box where you can submit a prompt to generate a completion. From this page, you can quickly iterate and experiment with the capabilities. You can also launch a [web app](../../../openai/how-to/use-web-app.md) to chat with the model over the web.
-
-## Next steps
-* [Using Azure OpenAI on your data](../../../openai/concepts/use-your-data.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azure OpenAI統合に関するドキュメントの削除"
}
```

### Explanation
この変更は、「Azure OpenAI統合」についてのドキュメントが完全に削除されたことを示しています。このドキュメントは、カスタム質問応答とAzure OpenAIの接続方法、必要な前提条件、接続手順、ならびにその結果得られる機能について詳細に説明していました。更新に伴い、ユーザーはこの情報を利用できなくなり、他のリソースやガイドを探す必要があります。この削除により、関連する内容は利用停止状態となるため、ユーザーにとっては情報の欠落が生じる可能性があります。また、今後のリソースや手順について確認する必要があることが示唆されています。

## articles/ai-services/language-service/question-answering/how-to/migrate-qnamaker.md{#item-0646f1}

<details>
<summary>Diff</summary>
````diff
@@ -11,9 +11,6 @@ ms.custom: language-service-question-answering
 
 # Migrate from QnA Maker knowledge bases to custom question answering
 
-> [!NOTE]
-> You can also migrate to [Azure OpenAI](../../../qnamaker/How-To/migrate-to-openai.md).
-
 Custom question answering, a feature of Azure AI Language was introduced in May 2021 with several new capabilities including enhanced relevance using a deep learning ranker, precise answers, and end-to-end region support. Each custom question answering project is equivalent to a knowledge base in QnA Maker. You can easily migrate knowledge bases from a QnA Maker resource to custom question answering projects within a [language resource](https://aka.ms/create-language-resource). You can also choose to migrate knowledge bases from multiple QnA Maker resources to a specific language resource.
 
 To successfully migrate knowledge bases, **the account performing the migration needs contributor access to the selected QnA Maker and language resource**. When a knowledge base is migrated, the following details are copied to the new custom question answering project:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "QnA Makerからの移行に関する注意書きの修正"
}
```

### Explanation
この変更は、「QnA Makerからカスタム質問応答への移行」に関するドキュメントの一部を修正したものです。具体的には、移行先としてのAzure OpenAIに関する注意書きが削除されました。元の文には、QnA MakerからAzure OpenAIへの移行が可能であるという情報が含まれていましたが、この箇所が削除されたことにより、ドキュメントはQnA Makerからカスタム質問応答への移行プロセスに重点を置く形となっています。この変更により、ユーザーはAzure OpenAIのオプションが示されなくなり、QnA Makerからカスタム質問応答への具体的な移行手順に集中できるようになります。

## articles/ai-services/language-service/question-answering/overview.md{#item-631b23}

<details>
<summary>Diff</summary>
````diff
@@ -13,9 +13,6 @@ ms.custom: language-service-question-answering
 
 # What is custom question answering?
 
-> [!NOTE]
-> [Azure OpenAI On Your Data](../../openai/concepts/use-your-data.md) utilizes large language models (LLMs) to produce similar results to Custom Question Answering. If you wish to connect an existing Custom Question Answering project to Azure OpenAI On Your Data, please check out our [guide]( how-to/azure-openai-integration.md).
-
 Custom question answering provides cloud-based Natural Language Processing (NLP) that allows you to create a natural conversational layer over your data. It is used to find appropriate answers from customer input or from a project.
 
 Custom question answering is commonly used to build conversational client applications, which include social media applications, chat bots, and speech-enabled desktop applications. This offering includes features like enhanced relevance using a deep learning ranker, precise answers, and end-to-end region support.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム質問応答の概要の更新"
}
```

### Explanation
この変更は、「カスタム質問応答」の概要に関するドキュメントの一部を修正したものです。具体的には、Azure OpenAIに関する注釈が削除されました。この注釈では、Azure OpenAIが大規模言語モデル（LLMs）を利用してカスタム質問応答と類似の結果を生成できること、および既存のカスタム質問応答プロジェクトをAzure OpenAIに接続する際のガイドへのリンクが提供されていました。この修正により、このドキュメントはカスタム質問応答の機能に集中する形になり、Azure OpenAIに関連する情報は含まれていないため、ユーザーは新しい情報を求める際には他のリソースを参照する必要があります。

## articles/ai-services/language-service/question-answering/quickstart/sdk.md{#item-a86876}

<details>
<summary>Diff</summary>
````diff
@@ -15,9 +15,6 @@ zone_pivot_groups: custom-qna-quickstart
 
 # Quickstart: custom question answering
 
-> [!NOTE]
-> [Azure OpenAI On Your Data](../../../openai/concepts/use-your-data.md) utilizes large language models (LLMs) to produce similar results to Custom Question Answering. If you wish to connect an existing Custom Question Answering project to Azure OpenAI On Your Data, please check out our [guide](../how-to/azure-openai-integration.md).
-
 > [!NOTE]
 > Are you looking to migrate your workloads from QnA Maker? See our [migration guide](../how-to/migrate-qnamaker-to-question-answering.md) for information on feature comparisons and migration steps.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム質問応答のクイックスタートガイドの更新"
}
```

### Explanation
この変更は、「カスタム質問応答」のクイックスタートガイドにおける情報を修正したものです。具体的には、Azure OpenAIに関する注釈と、QnA Makerからの移行ガイドに関する注釈が削除されました。元の文では、Azure OpenAIが大規模言語モデル（LLMs）を利用してカスタム質問応答と似た結果をもたらすこと、ならびに既存のカスタム質問応答プロジェクトをAzure OpenAIに接続するためのガイドを参照するよう促す内容が含まれていました。また、QnA Makerから移行する際の情報を提供するためのリンクも含まれていました。これらの修正により、ユーザーはより特定のクイックスタートの操作に集中できるようになり、既存のリソースとの関連付けの情報は省かれています。

## articles/ai-services/language-service/sentiment-opinion-mining/custom/quickstart.md{#item-32972e}

<details>
<summary>Diff</summary>
````diff
@@ -15,6 +15,9 @@ zone_pivot_groups: usage-custom-language-features
 
 # Quickstart: Custom sentiment analysis (preview)
 
+> [NOTE]
+> Custom sentiment analysis (preview) will be retired on 10 January 2025, please transition to other custom model training services, such as custom text classification in Azure AI Language, by that date. From now to 10 January 2025, you can continue to use custom sentiment analysis (preview) in your existing projects without disruption. You can’t create new projects. On 10 January 2025 – workloads running on custom sentiment analysis (preview) will be deleted and associated project data will be lost. 
+
 Use this article to get started with creating a Custom sentiment analysis project where you can train custom models for detecting the sentiment of text. A model is artificial intelligence software that's trained to do a certain task. For this system, the models classify text, and are trained by learning from tagged data.
 
 ::: zone pivot="language-studio"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム感情分析のクイックスタートガイドの更新"
}
```

### Explanation
この変更は、「カスタム感情分析」（プレビュー）のクイックスタートガイドに関する内容を更新したものです。特に、新たに追加された注釈では、カスタム感情分析が2025年1月10日に廃止されることが明記されています。そのため、利用者はこの日までに他のカスタムモデルのトレーニングサービス、例えばAzure AI Languageのカスタムテキスト分類に移行するよう促されています。この変更により、現在のプロジェクトではカスタム感情分析を中断することなく利用し続けることができるものの、新しいプロジェクトの作成はできないという重要な情報が提供されています。このように、ユーザーは今後の計画を考慮する上で必要な指針を得ることができます。

## articles/ai-studio/how-to/secure-data-playground.md{#item-b7fa5e}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ Ensure that the AI Studio hub is deployed with the __Identity-based access__ set
 
 - In the Azure portal, select the hub and then select __Settings__, __Properties__, and __Options__. At the bottom of the page, verify that __Storage account access type__ is set to __Identity-based access__.
 - If deploying using Azure Resource Manager or Bicep templates, include the `systemDatastoresAuthMode: 'identity'` property in your deployment template.
-
+- You must be familiar with using Microsoft Entra ID role-based access control to assign roles to resources and users. For more information, visit the [Role-based access control](/azure/role-based-access-control/overview) article.
 
 ## Configure Network Isolated AI Studio Hub
 
@@ -179,6 +179,8 @@ Repeat these steps for each resource that you want to connect to using Microsoft
 
 The services need to authorize each other to access the connected resources. The admin performing the configuration needs to have the __Owner__ role on these resources to add role assignments. The following table lists the required role assignments for each resource. The __Assignee__ column refers to the system-assigned managed identity of the listed resource. The __Resource__ column refers to the resource that the assignee needs to access. For example, the Azure AI Search has a system-assigned managed identity that needs to be assigned the __Storage Blob Data Contributor__ role for the Azure Storage Account.
 
+For more information on assigning roles, see [Tutorial: Grant a user access to resources](/azure/role-based-access-control/quickstart-assign-role-user-portal).
+
 | Resource | Role | Assignee | Description |
 |----------|------|----------|-------------|
 | Azure AI Search | Search Index Data Contributor | Azure AI services/OpenAI | Read-write access to content in indexes. Import, refresh, or query the documents collection of an index. Only used for ingestion and inference scenarios. |
@@ -192,19 +194,23 @@ The services need to authorize each other to access the connected resources. The
 > [!NOTE]
 > The Cognitive Services OpenAI User role is only required if you are using two Azure OpenAI resources: one for your chat model and one for your embedding model. If this applies, enable Trusted Services AND ensure the Connection for your embedding model Azure OpenAI resource has EntraID enabled.  
 
-To enable your developers to use these resources to build applications, add the developers' identity with the following role assignments to the listed resources.
-
-| Resource | Role | Description |
-|----------|------|-------------|
-| Azure AI Search | Contributor | List API-Keys to list indexes from Azure OpenAI Studio. |
-| Azure AI Search | Search Index Data Contributor | Required for the indexing scenario. |
-| Azure AI services/OpenAI | Cognitive Services OpenAI Contributor | Call public ingestion API from Azure OpenAI Studio. |
-| Azure AI services/OpenAI | Cognitive Services User | List API-Keys from Azure OpenAI Studio. |
-| Azure AI services/OpenAI | Contributor | Allows for calls to the control plane. |
-| Azure Storage Account | Contributor | List Account SAS to upload files from Azure OpenAI Studio. |
-| Azure Storage Account | Storage Blob Data Contributor | Needed for developers to read and write to blob storage. |
-| Azure Storage Account | Storage File Data Privileged Contributor | Needed to Access File Share in Storage for Promptflow data. |
-| The resource group or Azure subscription where the developer need to deploy the web app to | Contributor | Deploy web app to the developer's Azure subscription. |
+### Assign roles to developers
+
+To enable your developers to use these resources to build applications, assign the following roles to your developer's identity in Microsoft Entra ID. For example, assign the __Search Services Contributor__ role to the developer's Microsoft Entra ID for the Azure AI Search resource.
+
+For more information on assigning roles, see [Tutorial: Grant a user access to resources](/azure/role-based-access-control/quickstart-assign-role-user-portal).
+
+| Resource | Role | Assignee | Description |
+|----------|------|----------|-------------|
+| Azure AI Search | Search Services Contributor | Developer's Microsoft Entra ID | List API-Keys to list indexes from Azure OpenAI Studio. |
+| Azure AI Search | Search Index Data Contributor | Developer's Microsoft Entra ID | Required for the indexing scenario. |
+| Azure AI services/OpenAI | Cognitive Services OpenAI Contributor | Developer's Microsoft Entra ID | Call public ingestion API from Azure OpenAI Studio. |
+| Azure AI services/OpenAI | Cognitive Services User | Developer's Microsoft Entra ID | List API-Keys from Azure OpenAI Studio. |
+| Azure AI services/OpenAI | Contributor | Developer's Microsoft Entra ID | Allows for calls to the control plane. |
+| Azure Storage Account | Contributor | Developer's Microsoft Entra ID | List Account SAS to upload files from Azure OpenAI Studio. |
+| Azure Storage Account | Storage Blob Data Contributor | Developer's Microsoft Entra ID | Needed for developers to read and write to blob storage. |
+| Azure Storage Account | Storage File Data Privileged Contributor | Developer's Microsoft Entra ID | Needed to Access File Share in Storage for Promptflow data. |
+| The resource group or Azure subscription where the developer need to deploy the web app to | Contributor | Developer's Microsoft Entra ID | Deploy web app to the developer's Azure subscription. |
 
 ## Use your data in AI Studio  
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セキュアデータプレイグラウンドの更新"
}
```

### Explanation
この変更は、「セキュアデータプレイグラウンド」に関する記事を更新し、役割の割り当てやリソースへのアクセス権に関する情報を追加したものです。具体的には、Microsoft Entra IDによる役割ベースのアクセス制御に関する内容が強調され、開発者がリソースを使用してアプリケーションを構築するために、どのように役割を割り当てるかが明記されています。

新たに追加された情報には、開発者の識別情報に対して必要な役割を割り当てる手順が含まれています。また、リソースごとの役割やその説明が詳細に示されており、開発者は必要な権限を理解した上で、Azureのさまざまなリソースにアクセスできるようになります。この更新により、開発者はリソースの設定とアクセス権の管理をより効率的に行うことができるようになります。


