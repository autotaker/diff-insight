---
date: '2025-06-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8d764d4...MicrosoftDocs:45b2d74
summary: |-
  今回のコード変更は、Azure AI Foundryポータルへのリンクにクエリパラメータを追加し、学習資料へのアクセスを容易にすることを目的としています。具体的には、リンクに `?cid=learnDocs` が追加され、ユーザーは必要なリソースに簡単にアクセスできるようになります。

  特に大きな破壊的変更はありませんが、リンクのURLが変更されたため、ユーザーのブックマークが更新される必要があるかもしれません。全体的に、リンクの更新はドキュメントの整合性を向上させ、ユーザー体験の向上に寄与します。

  この変更により、ユーザーはAzureの学習資料やAI機能にアクセスしやすくなり、生産性の向上が期待されます。また、ドキュメントへのアクセスの手間が減ることで、新しい機能やサービスの活用が促進され、ビジネスの成長にも寄与する重要な更新です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8d764d4...MicrosoftDocs:45b2d74){target="_blank"}

<format>
# ハイライト
今回のコード変更は、Azure AI Foundryポータルへのリンクに関するもので、多くのファイルにわたってクエリパラメータの追加が行われました。主な目的は、ユーザーがAzureの学習資料や関連リソースにより簡単にアクセスできるようにすることです。

## 新機能
- Azure AI Foundryポータルへのリンクにクエリパラメータ `?cid=learnDocs` が一貫して追加され、学習資料へのアクセスが容易になりました。

## 破壊的変更
- 特に大きな破壊的変更はありません。ただし、リンクのURL変更により、ユーザーのブックマークが更新される必要があるかもしれません。

## その他の更新
- 各ファイルで同様のリンク更新が施され、ドキュメントの整合性が向上しました。

# 洞察
今回の変更は、Azure AIの学習資料へのアクセス性を高めることを主な目的としています。リンクにクエリパラメータ `?cid=learnDocs` を追加することで、ユーザーがAI Foundryのリソースをより効果的に利用し、学びを深める機会を提供しています。

このようなリンク更新は、小さな変更でありながらも、ユーザー体験に直接影響を与える重要な役割を果たします。例えば、特定のクエリパラメータが追加されることで、特定のキャンペーンや情報をプッシュしやすくなるという利点が考えられます。また、ユーザーがAI機能を試す際に、必要なドキュメントをすばやく見つけられることで、生産性の向上にもつながるでしょう。

さらに、今回のリンク更新により、Azure AIサービスの利用促進が期待されます。ユーザーがドキュメントにアクセスする際の手間が減ることで、新機能やサービスをより積極的に探求し、導入する可能性が高まります。このように、技術的な更新が間接的にビジネスの成長をバックアップする一例として、非常に効果的な変更と言えます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [studio-overview.md](#item-db8fa3) | minor update | Azure AI Foundryポータルのリンク更新 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-1ec8d3) | minor update | Azure AI Foundryポータルのリンク更新 | modified | 1 | 1 | 2 | 
| [build-schema.md](#item-623a8b) | minor update | AI Foundryリンクのクエリパラメータ追加 | modified | 1 | 1 | 2 | 
| [tag-utterances.md](#item-3d1b2f) | minor update | AI Foundryリンクに学習資料パラメータ追加 | modified | 1 | 1 | 2 | 
| [development-options.md](#item-8a2549) | minor update | AI Foundryリンクにクエリパラメータ追加 | modified | 1 | 1 | 2 | 
| [development-options.md](#item-00997b) | minor update | AI Foundryリンクにクエリパラメータ追加 | modified | 1 | 1 | 2 | 
| [development-options.md](#item-8f1dfc) | minor update | AI Foundryリンクにクエリパラメータ追加 | modified | 1 | 1 | 2 | 
| [overview.md](#item-f138b4) | minor update | AI Foundryリンクにクエリパラメータ追加 | modified | 1 | 1 | 2 | 
| [development-options.md](#item-1bd5c9) | minor update | AI Foundryリンクにクエリパラメータ追加 | modified | 1 | 1 | 2 | 
| [development-options.md](#item-62db06) | minor update | AI Foundryリンクにクエリパラメータ追加 | modified | 1 | 1 | 2 | 
| [development-options.md](#item-f33a53) | minor update | AI Foundryリンクにクエリパラメータ追加 | modified | 2 | 2 | 4 | 
| [call-api.md](#item-a1a7d7) | minor update | Azure AI Foundryリンクにクエリパラメータ追加 | modified | 1 | 1 | 2 | 
| [development-options.md](#item-0d0fa6) | minor update | AI Foundryリンクにクエリパラメータ追加 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-69b272) | minor update | AI Foundryリンクにクエリパラメータ追加 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/document-intelligence/studio-overview.md{#item-db8fa3}

<details>
<summary>Diff</summary>
````diff
@@ -76,7 +76,7 @@ Use the help wizard, labeling interface, training step, and interactive visualiz
 
 ### [**Azure AI Foundry portal**](#tab/ai-foundry)
 
-Document Intelligence is part of the Azure AI services offerings in the [Azure AI Foundry portal](https://ai.azure.com/). Each of the Azure AI services helps developers and organizations rapidly create intelligent, cutting-edge, market-ready, and responsible applications with out-of-the-box and prebuilt and customizable APIs and models.
+Document Intelligence is part of the Azure AI services offerings in the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs). Each of the Azure AI services helps developers and organizations rapidly create intelligent, cutting-edge, market-ready, and responsible applications with out-of-the-box and prebuilt and customizable APIs and models.
 
 Learn how to [connect your AI services hub](../../ai-services/connect-services-ai-foundry-portal.md) with AI services and get started using Document Intelligence.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク更新"
}
```

### Explanation
この変更は、"studio-overview.md"ファイル内のAzure AI Foundryポータルへのリンクを更新するものです。具体的には、リンクのクエリパラメータを変更し、ユーザーがより適切な情報にアクセスできるように改善しました。変更内容は、以前のリンクが「https://ai.azure.com/」だったのに対し、新しいリンクは「https://ai.azure.com/?cid=learnDocs」となっています。この更新により、ユーザーがAzure AIサービスに関する学習資料に直接アクセスしやすくなることが期待されます。

## articles/ai-services/document-intelligence/whats-new.md{#item-1ec8d3}

<details>
<summary>Diff</summary>
````diff
@@ -95,7 +95,7 @@ For more information, *see* client libraries for the following supported program
 
 The Document Intelligence [**2024-07-31-preview**](/rest/api/aiservices/document-models?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true) REST API is now available. This preview API introduces new and updated capabilities:
 
-* Public preview version [**2024-07-31-preview**](/rest/api/aiservices/operation-groups?view=rest-aiservices-2024-07-31-preview&preserve-view=true) is currently available only in the following Azure regions. The new document field extraction model in [Azure AI Foundry portal](https://ai.azure.com/) is only available in North Central US region:
+* Public preview version [**2024-07-31-preview**](/rest/api/aiservices/operation-groups?view=rest-aiservices-2024-07-31-preview&preserve-view=true) is currently available only in the following Azure regions. The new document field extraction model in [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) is only available in North Central US region:
 
 * **East US**
 * **West US2**
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク更新"
}
```

### Explanation
この変更は、"whats-new.md"ファイル内のAzure AI Foundryポータルへのリンクを更新するもので、クエリパラメータが追加されました。以前のリンクは「https://ai.azure.com/」でしたが、更新後は「https://ai.azure.com/?cid=learnDocs」となり、ユーザーが関連する学習資料にアクセスしやすくなっています。この変更により、Document Intelligenceの新しい機能や公共プレビュー情報をより効果的に利用できるようになります。他の情報やモデルに関連するリンクも引き続き有効です。

## articles/ai-services/language-service/conversational-language-understanding/how-to/build-schema.md{#item-623a8b}

<details>
<summary>Diff</summary>
````diff
@@ -39,7 +39,7 @@ They might create an intent to represent each of these actions. They might also
 
 ## Add intents
 
-To build a project schema within [AI Foundry](https://ai.azure.com):
+To build a project schema within [AI Foundry](https://ai.azure.com/?cid=learnDocs):
 
 1. Select **Define schema** from the left side menu.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryリンクのクエリパラメータ追加"
}
```

### Explanation
この変更は、"build-schema.md"ファイル内のAI Foundryへのリンクを更新するもので、リンクにクエリパラメータが追加されました。具体的には、以前のリンク「https://ai.azure.com/」は、更新後は「https://ai.azure.com/?cid=learnDocs」となり、ユーザーが学習資料に直接アクセスしやすくなっています。このアップデートにより、AI Foundry内でプロジェクトスキーマを構築する手順が明確になるだけでなく、関連情報を簡単に見つけられるようになります。

## articles/ai-services/language-service/conversational-language-understanding/how-to/tag-utterances.md{#item-3d1b2f}

<details>
<summary>Diff</summary>
````diff
@@ -54,7 +54,7 @@ As you add utterances and label them, keep in mind:
 
 Use the following steps to label your utterances:
 
-1. Go to your project page in [AI Foundry](https://ai.azure.com).
+1. Go to your project page in [AI Foundry](https://ai.azure.com/?cid=learnDocs).
 
 1. From the left side menu, select `Manage data`. In this page, you can start adding your utterances and labeling them. You can also upload your utterances directly by clicking on `Upload utterance file` from the top menu. Make sure it follows the [accepted format](../concepts/data-formats.md#utterance-file-format).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryリンクに学習資料パラメータ追加"
}
```

### Explanation
この変更は、"tag-utterances.md"ファイル内のAI Foundryへのリンクを更新したものです。具体的には、以前のリンク「https://ai.azure.com/」が新しいリンク「https://ai.azure.com/?cid=learnDocs」に変更され、ユーザーが学習に関連する資料に簡単にアクセスできるようになっています。この更新により、プロジェクトページにアクセスする際の利便性が向上し、ユーザーは発話を追加したりラベル付けを行う手順をよりスムーズに行えるようになります。

## articles/ai-services/language-service/key-phrase-extraction/includes/development-options.md{#item-8a2549}

<details>
<summary>Diff</summary>
````diff
@@ -12,6 +12,6 @@ To use key phrase extraction, you submit raw unstructured text for analysis and
 
 |Development option  |Description  |
 |---------|---------|
-|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use entity linking with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
+|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use entity linking with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com/?cid=learnDocs) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
 |REST API or Client library (Azure SDK)      | Integrate key phrase extraction into your applications using the REST API, or the client library available in a variety of languages. For more information, see the [key phrase extraction quickstart](../quickstart.md).        |
 | Docker container | Use the available Docker container to [deploy this feature on-premises](../how-to/use-containers.md). These docker containers enable you to bring the service closer to your data for compliance, security, or other operational reasons. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryリンクにクエリパラメータ追加"
}
```

### Explanation
この変更は、"development-options.md"ファイル内のAI Foundryへのリンクを更新したもので、リンクにクエリパラメータが追加されました。具体的には、以前のリンク「https://ai.azure.com」が新しいリンク「https://ai.azure.com/?cid=learnDocs」に変更され、ユーザーが学習資料に簡単にアクセスできるようになっています。この修正により、AI Foundryのウェブベースプラットフォームの使用が促進され、利用者は自分のデータを使用してのエンティティリンクの手順をより効果的に理解できるようになります。

## articles/ai-services/language-service/language-detection/includes/development-options.md{#item-00997b}

<details>
<summary>Diff</summary>
````diff
@@ -12,6 +12,6 @@ To use language detection, you submit raw unstructured text for analysis and han
 
 |Development option  |Description  |
 |---------|---------|
-|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use entity linking with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
+|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use entity linking with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com/?cid=learnDocs) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
 |REST API or Client library (Azure SDK)      | Integrate language detection into your applications using the REST API, or the client library available in a variety of languages. For more information, see the [language detection quickstart](../quickstart.md).        |
 | Docker container | Use the available Docker container to [deploy this feature on-premises](../how-to/use-containers.md). These docker containers enable you to bring the service closer to your data for compliance, security, or other operational reasons. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryリンクにクエリパラメータ追加"
}
```

### Explanation
この変更は、"development-options.md"ファイル内のAI Foundryへのリンクを更新したもので、リンクにクエリパラメータが追加されています。具体的には、以前のリンク「https://ai.azure.com」が新しいリンク「https://ai.azure.com/?cid=learnDocs」に変更されました。これにより、ユーザーは学習資料にアクセスしやすくなり、言語検出のためのAI Foundryプラットフォームの利便性が向上します。この更新は、ユーザーが自分のデータを使ってエンティティリンク機能を利用する際に、必要な情報をスムーズに得られるようにすることを目的としています。

## articles/ai-services/language-service/named-entity-recognition/includes/development-options.md{#item-8f1dfc}

<details>
<summary>Diff</summary>
````diff
@@ -12,5 +12,5 @@ To use named entity recognition, you submit raw unstructured text for analysis a
 
 |Development option  |Description  |
 |---------|---------|
-|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use named entity recognition with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
+|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use named entity recognition with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com/?cid=learnDocs) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
 |REST API or Client library (Azure SDK)      | Integrate named entity recognition into your applications using the REST API, or the client library available in a variety of languages. For more information, see the [named entity recognition quickstart](../quickstart.md).        |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryリンクにクエリパラメータ追加"
}
```

### Explanation
この変更は、"development-options.md"ファイル内のAI Foundryへのリンクを改訂したもので、リンクにクエリパラメータが追加されています。具体的には、以前のリンク「https://ai.azure.com」が新しいリンク「https://ai.azure.com/?cid=learnDocs」に更新されました。これにより、利用者は学習資料やリソースにアクセスしやすくなり、名前付きエンティティ認識のためのAI Foundryプラットフォームの活用が促進されます。この修正は、ユーザーが自分のデータを使って名前付きエンティティ認識機能を効果的に活用できるように情報を提供することを目的としています。

## articles/ai-services/language-service/overview.md{#item-f138b4}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ Language features are also utilized in [agent templates](https://github.com/azur
 > [!TIP]
 > Unsure which feature to use? See [Which Language service feature should I use](#which-language-service-feature-should-i-use) to help you decide.
 
-[**Azure AI Foundry**](https://ai.azure.com) enables you to use most of the following service features without needing to write code.
+[**Azure AI Foundry**](https://ai.azure.com/?cid=learnDocs) enables you to use most of the following service features without needing to write code.
 
 ### Named Entity Recognition (NER)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryリンクにクエリパラメータ追加"
}
```

### Explanation
この変更は、"overview.md"ファイル内のAzure AI Foundryへのリンクを更新しており、リンクにクエリパラメータが追加されています。具体的には、これまでのリンク「https://ai.azure.com」が新しいリンク「https://ai.azure.com/?cid=learnDocs」に修正されました。これにより、ユーザーがAzureの学習資料やリソースにアクセスする際、より効果的に利用できるようになります。この変更は、プログラミングなしでAIサービスの機能を利用したいユーザーに対して、必要な情報を簡単に得られるようにすることを目的としています。

## articles/ai-services/language-service/personally-identifiable-information/includes/development-options.md{#item-1bd5c9}

<details>
<summary>Diff</summary>
````diff
@@ -12,5 +12,5 @@ To use PII detection, you submit text for analysis and handle the API output in
 
 |Development option  |Description  |
 |---------|---------|
-|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use personally identifying information detection with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
+|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use personally identifying information detection with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com/?cid=learnDocs) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
 |REST API or Client library (Azure SDK)      | Integrate PII detection into your applications using the REST API, or the client library available in various languages. For more information, see the [PII detection quickstart](../quickstart.md).        |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryリンクにクエリパラメータ追加"
}
```

### Explanation
この変更は、"development-options.md"ファイル内の個人を特定できる情報（PII）検出に関するAzure AI Foundryへのリンクを改善したものです。具体的には、リンクが「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」に更新されています。この変更により、ユーザーが自身のデータを使用してPII検出のためのテキストサンプルを活用する際、学習コンテンツへのアクセスが容易になり、技術的なサポートを受けやすくなります。この修正は、ユーザーがPII検出機能を効果的に利用できるように、追加情報を通じてサポートすることを目指しています。

## articles/ai-services/language-service/sentiment-opinion-mining/includes/development-options.md{#item-62db06}

<details>
<summary>Diff</summary>
````diff
@@ -12,6 +12,6 @@ To use sentiment analysis, you submit raw unstructured text for analysis and han
 
 |Development option  |Description  |
 |---------|---------|
-|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use entity linking with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
+|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use entity linking with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com/?cid=learnDocs) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
 |REST API or Client library (Azure SDK)      | Integrate sentiment analysis into your applications using the REST API, or the client library available in a variety of languages. For more information, see the [sentiment analysis quickstart](../quickstart.md).        |
 | Docker container | Use the available Docker container to [deploy this feature on-premises](../how-to/use-containers.md). These docker containers enable you to bring the service closer to your data for compliance, security, or other operational reasons. |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryリンクにクエリパラメータ追加"
}
```

### Explanation
この変更は、"development-options.md"ファイル内の感情分析に関連するAzure AI Foundryへのリンクを更新したものです。具体的には、リンクが「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」に修正されました。この更新により、ユーザーは自分のデータを使用してエンティティリンクを活用する際に、より多くの学習資料にアクセスできるようになります。この変更の目的は、感情分析機能を利用するユーザーがスムーズに必要な情報やリソースに到達できるようにすることです。結果的に、Azure AI Foundryの利用が促進され、より効果的な応用が可能となります。

## articles/ai-services/language-service/summarization/includes/development-options.md{#item-f33a53}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ To use summarization, you submit for analysis and handle the API output in your
 
 |Development option  |Description  |
 |---------|---------|
-|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use entity linking with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
+|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use entity linking with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com/?cid=learnDocs) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
 |REST API or Client library (Azure SDK)      | Integrate text summarization into your applications using the REST API, or the client library available in various languages. For more information, see the [summarization quickstart](../quickstart.md).        |
 
 
@@ -29,7 +29,7 @@ To use summarization, you submit for analysis and handle the API output in your
 
 |Development option  |Description  |
 |---------|---------|
-|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use entity linking with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
+|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use entity linking with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com/?cid=learnDocs) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
 |REST API or Client library (Azure SDK)      | Integrate text summarization into your applications using the REST API, or the client library available in various languages. For more information, see the [summarization quickstart](../quickstart.md).  
 
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryリンクにクエリパラメータ追加"
}
```

### Explanation
この変更は、"development-options.md"ファイルにおける要約機能に関連するAzure AI Foundryへのリンクを更新した内容です。具体的には、リンクが「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」に修正されています。この更新により、ユーザーが自身のデータを用いてエンティティリンクを利用する際に、学習資料へのアクセスがより容易になります。変更の目的は、要約機能を利用するユーザーが必要な情報に素早く辿り着けるようにすることです。また、これによりAzure AI Foundryの利用を促進し、ユーザー体験の向上につながることを期待しています。

## articles/ai-services/language-service/text-analytics-for-health/how-to/call-api.md{#item-a1a7d7}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,7 @@ ms.custom: language-service-health
 Text Analytics for health can be used to extract and label relevant medical information from unstructured texts such as doctors' notes, discharge summaries, clinical documents, and electronic health records. The service performs [named entity recognition](../concepts/health-entity-categories.md), [relation extraction](../concepts/relation-extraction.md), [entity linking](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/index.html), and [assertion detection](../concepts/assertion-detection.md) to uncover insights from the input text. For information  on the returned confidence scores, see the [transparency note](/legal/cognitive-services/text-analytics/transparency-note#general-guidelines-to-understand-and-improve-performance?context=/azure/ai-services/text-analytics/context/context).
 
 > [!TIP]
-> If you want to test out the feature without writing any code, use [Azure AI Foundry](https://ai.azure.com).
+> If you want to test out the feature without writing any code, use [Azure AI Foundry](https://ai.azure.com/?cid=learnDocs).
 
 There are two ways to call the service: 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryリンクにクエリパラメータ追加"
}
```

### Explanation
この変更は、"call-api.md"ファイル内のAzure AI Foundryへのリンクを更新した内容です。具体的には、リンクが「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」に修正されました。この更新は、Azure AI Foundryを利用して機能をコードなしで試したいユーザーに対して、より多くの学びのリソースへアクセスできるようにすることを目的としています。変更によって、ユーザーが関連情報に容易にアクセスできるようになり、サービスをより効果的に活用できるよう改善されました。

## articles/ai-services/language-service/text-analytics-for-health/includes/development-options.md{#item-0d0fa6}

<details>
<summary>Diff</summary>
````diff
@@ -13,6 +13,6 @@ To use Text Analytics for health, you submit raw unstructured text for analysis
 
 |Development option  |Description  |
 |---------|---------|
-|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use entity linking with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
+|Azure AI Foundry     | Azure AI Foundry is a web-based platform that lets you use entity linking with text examples with your own data when you sign up. For more information, see the [Azure AI Foundry website](https://ai.azure.com/?cid=learnDocs) or [Azure AI Foundry documentation](../../../../ai-foundry/what-is-azure-ai-foundry.md).         |
 |REST API or Client library (Azure SDK)      | Integrate Text Analytics for health into your applications using the REST API, or the client library available in a variety of languages. For more information, see the [Text Analytics for health quickstart](../quickstart.md).        |
 | Docker container | Use the available Docker container to [deploy this feature on-premises](../how-to/use-containers.md). These docker containers enable you to bring the service closer to your data for compliance, security, or other operational reasons. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryリンクにクエリパラメータ追加"
}
```

### Explanation
この変更は、"development-options.md"ファイルにおけるテキスト分析サービスに関連するAzure AI Foundryへのリンクを更新した内容です。具体的には、リンクが「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」に修正されています。この変更により、Azure AI Foundryを利用するユーザーは、より多くの学習リソースにアクセスしやすくなります。特に、独自のデータを使用してエンティティリンクを試験的に利用する際に、目的の情報を見つけやすくなることを目的としています。この更新は、ユーザー体験を向上させ、サービスの利用促進につながることが期待されます。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -56,7 +56,7 @@ More on these releases can be found on our TechCommunity Blog Post
 ## February 2025
 
 * Document and text abstractive summarization is now powered by fine-tuned Phi-3.5-mini! Check out the [Announcing Blog](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/exciting-update-abstractive-summarization-in-azure-ai-language-now-powered-by-ph/4369025) for more information.
-* More skills are available in [Azure AI Foundry](https://ai.azure.com): Extract key phrase, Extract named entities, Analyze sentiment, and Detect language. More skills are yet to come.
+* More skills are available in [Azure AI Foundry](https://ai.azure.com/?cid=learnDocs): Extract key phrase, Extract named entities, Analyze sentiment, and Detect language. More skills are yet to come.
 
 ## January 2025
 
@@ -76,7 +76,7 @@ More on these releases can be found on our TechCommunity Blog Post
 
 ## November 2024
 
-* Azure AI Language is moving to [Azure AI Foundry](https://ai.azure.com). These skills are now available in AI Foundry playground: Extract health information, Extract PII from conversation, Extract PII from text, Summarize text, Summarize conversation, Summarize for call center. More skills follow.
+* Azure AI Language is moving to [Azure AI Foundry](https://ai.azure.com/?cid=learnDocs). These skills are now available in AI Foundry playground: Extract health information, Extract PII from conversation, Extract PII from text, Summarize text, Summarize conversation, Summarize for call center. More skills follow.
 * Runtime Container for Conversational Language Understanding (CLU) is available for on-premises connections.
 * Both our [Text PII redaction service](personally-identifiable-information/overview.md?tabs=text-pii) and our Conversational PII service preview API (version 2024-11-15-preview) now support the option to mask detected sensitive entities with a label beyond just redaction characters. Customers can specify if personal data content such as names and phone numbers, that is, "John Doe received a call from 424-878-9192" are masked with a redaction character, that is, "******** received a call from ************" or masked with an entity label, that is, "`PERSON_1` received a call from `PHONENUMBER_1`." More on how to specify the redaction policy style for your outputs can be found in our [how-to guides](personally-identifiable-information/how-to-call.md).
 * Native document support gating is removed with the latest API version, 2024-11-15-preview, allowing customers to access native document support for PII redaction and summarization. Key updates in this version include:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryリンクにクエリパラメータ追加"
}
```

### Explanation
この変更は、"whats-new.md"ファイルの内容を更新するもので、Azure AI Foundryへのリンクが更新されました。具体的には、リンクが「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」に修正されています。この変更により、ユーザーは新たに追加されたスキルや機能へのアクセスをより簡単に行えるようになります。特に、文章やテキストの要約機能が向上したことに加え、ユーザーは自分のデータを使ったエンティティリンクや感情分析を試すことができるようになっています。このアップデートは、ユーザーが利用しやすくなることを目指したものであり、サービスの利便性を高める役割を果たしています。


