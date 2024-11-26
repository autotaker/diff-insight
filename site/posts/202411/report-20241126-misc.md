---
date: '2024-11-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:32f452e...MicrosoftDocs:9760ca7
summary: 今回の変更は、AIスタジオ関連のSDKおよびチュートリアルのドキュメントに対するマイナーアップデートです。変更内容には、日付やライブラリ名の修正、説明の簡潔化、プロセスステップの明確化が含まれます。また、いくつかのチュートリアルに新しいチェックリストの項目が追加されています。特に破壊的な変更はありませんが、「デプロイ」ステップの削除が行われました。このアップデートにより、ドキュメントの精度とユーザビリティが向上し、ユーザーがよりスムーズに正しい手順を理解できるようになっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:32f452e...MicrosoftDocs:9760ca7){target="_blank"}

<format>
# Highlights
今回の変更は、AIスタジオ関連のSDKおよびチュートリアルのドキュメントに対するマイナーアップデートです。これにより、日付やライブラリ名の修正、説明の簡潔化、プロセスステップの明確化が行われました。また、いくつかのチュートリアルに新しいチェックリストの項目が追加されています。

## New features
- SDK概要ドキュメントの日付更新とクライアントライブラリ名の修正。
- チュートリアルにおける、ユーザーが例データを取得する手順の明示化。
- チュートリアルのチェックリストに、新たにアプリを改善するための項目が追加。

## Breaking changes
- 特に破壊的な変更は行われていませんが、説明プロセスから「デプロイ」ステップが削除されている点に注意が必要です。

## Other updates
- チュートリアルの説明を簡潔にし、主要ステップにフォーカスするための言語修正が行われています。

# Insights
この変更により、ドキュメントの精度とユーザビリティが向上しました。特に、AIスタジオでのSDKに関する情報が最新のものに更新され、正確なライブラリ名を使用することで、ユーザーが適切なインストールを行えるようになっています。また、各種チュートリアルにおいて、「デプロイ」ステップを削除したことは、より明確に現在の焦点を示すものとして、ユーザーがステップを誤解することなく目指すべきゴールに到達しやすくなる効果があります。さらに、チェックリストの新項目を加えることで、プロセスの改善の一環としてユーザーへの指導も強化されています。これは、ユーザーのスキルアップにも寄与する意図が見て取れ、特にアプリの評価段階での反復改善の重要性が強調されています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [sdk-overview.md](#item-d3ab19) | minor update | SDKの概要ドキュメントの更新 | modified | 3 | 3 | 6 | 
| [copilot-sdk-build-rag.md](#item-b77dba) | minor update | コパイロットSDKチュートリアルの文書修正 | modified | 2 | 1 | 3 | 
| [copilot-sdk-create-resources.md](#item-552960) | minor update | コパイロットSDKリソース作成チュートリアルの文書修正 | modified | 1 | 1 | 2 | 
| [copilot-sdk-evaluate.md](#item-bb5754) | minor update | コパイロットSDK評価チュートリアルの文書修正 | modified | 2 | 1 | 3 | 


# Modified Contents
## articles/ai-studio/how-to/develop/sdk-overview.md{#item-d3ab19}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: overview
-ms.date: 11/19/2024
+ms.date: 11/25/2024
 ms.reviewer: dantaylo
 ms.author: sgilley
 author: sdgilley
@@ -181,7 +181,7 @@ The [Azure AI model inference service](/azure/ai-studio/ai-services/model-infere
 
 To use the model inference service, first ensure that your project has an AI Services connection (in the management center).
 
-Install the `azure-ai-inferencing` client library:
+Install the `azure-ai-inference` client library:
 
 ::: zone pivot="programming-language-python"
 
@@ -237,7 +237,7 @@ To learn more about using the Azure AI inferencing client, check out the [Azure
 
 The inferencing client supports for creating prompt messages from templates.  The template allows you to dynamically generate prompts using inputs that are available at runtime.
 
-To use prompt templates, install the `azure-ai-inferencing` package:
+To use prompt templates, install the `azure-ai-inference` package:
 
 ```bash
 pip install azure-ai-inference
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SDKの概要ドキュメントの更新"
}
```

### Explanation
この変更は、AIスタジオのSDKに関するドキュメントの一部を更新するために行われました。具体的には、いくつかのエントリーが次のように修正されました：日付が「11/19/2024」から「11/25/2024」に変更され、クライアントライブラリの名前が「azure-ai-inferencing」から「azure-ai-inference」に修正されました。この更新により、読者が正しいパッケージをインストールし、最新の日付情報に基づいてインフォメーションを得ることができます。全体で3行が追加され、3行が削除され、合計6行の変更が行われました。

## articles/ai-studio/tutorials/copilot-sdk-build-rag.md{#item-b77dba}

<details>
<summary>Diff</summary>
````diff
@@ -15,11 +15,12 @@ ms.custom: copilot-learning-hub, ignite-2024
 
 # Tutorial:  Part 2 - Build a custom knowledge retrieval (RAG) app with the Azure AI Foundry SDK
 
-In this tutorial, you use the Azure AI Foundry SDK (and other libraries) to build, configure, evaluate, and deploy a chat app for your retail company called Contoso Trek. Your retail company specializes in outdoor camping gear and clothing. The chat app should answer questions about your products and services. For example, the chat app can answer questions such as "which tent is the most waterproof?" or "what is the best sleeping bag for cold weather?".
+In this tutorial, you use the Azure AI Foundry SDK (and other libraries) to build, configure, and evaluate a chat app for your retail company called Contoso Trek. Your retail company specializes in outdoor camping gear and clothing. The chat app should answer questions about your products and services. For example, the chat app can answer questions such as "which tent is the most waterproof?" or "what is the best sleeping bag for cold weather?".
 
 This part two shows you how to enhance a basic chat application by adding [retrieval augmented generation (RAG)](../concepts/retrieval-augmented-generation.md) to ground the responses in your custom data. Retrieval Augmented Generation (RAG) is a pattern that uses your data with a large language model (LLM) to generate answers specific to your data. In this part two, you learn how to:
 
 > [!div class="checklist"]
+> - Get example data
 > - Create a search index of the data for the chat app to use
 > - Develop custom RAG code
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コパイロットSDKチュートリアルの文書修正"
}
```

### Explanation
この変更は、Azure AI Foundry SDKを用いたカスタム知識検索アプリケーションの構築に関するチュートリアルの一部を修正するために行われました。具体的には、チュートリアルの説明文において、「構築、設定、評価、デプロイ」のプロセスのうち、「デプロイ」が削除され、「構築、設定、評価」に修正されました。これにより、説明がより簡潔になり、チュートリアルの主なステップに焦点を当てることができるようになりました。その他にも、チェックリストの項目が追加され、ユーザーが例データを取得する手順が明示されました。全体で2行が追加され、1行が削除され、合計3行の変更が行われています。

## articles/ai-studio/tutorials/copilot-sdk-create-resources.md{#item-552960}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ author: sdgilley
 # Tutorial:  Part 1 - Set up project and development environment to build a custom knowledge retrieval (RAG) app with the Azure AI Foundry SDK
 
 
-In this tutorial, you use the Azure AI Foundry SDK (and other libraries) to build, configure, evaluate, and deploy a chat app for your retail company called Contoso Trek. Your retail company specializes in outdoor camping gear and clothing. The chat app should answer questions about your products and services. For example, the chat app can answer questions such as "which tent is the most waterproof?" or "what is the best sleeping bag for cold weather?".
+In this tutorial, you use the Azure AI Foundry SDK (and other libraries) to build, configure, and evaluate a chat app for your retail company called Contoso Trek. Your retail company specializes in outdoor camping gear and clothing. The chat app should answer questions about your products and services. For example, the chat app can answer questions such as "which tent is the most waterproof?" or "what is the best sleeping bag for cold weather?".
 
 This tutorial is part one of a three-part tutorial.  This part one gets you ready to write code in part two and evaluate your chat app in part three. In this part, you:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コパイロットSDKリソース作成チュートリアルの文書修正"
}
```

### Explanation
この変更は、Azure AI Foundry SDKを用いたカスタム知識検索アプリケーションを構築するためのチュートリアルの一部を修正する目的で行われました。具体的には、チュートリアルの説明文から「デプロイ」が削除され、文の最後の部分が「構築、設定、評価」に修正されました。この変更により、チュートリアル内容がより明確になり、ユーザーが行うべきステップの理解が深まりました。全体で1行が追加され、1行が削除され、合計2行の変更が行われています。

## articles/ai-studio/tutorials/copilot-sdk-evaluate.md{#item-bb5754}

<details>
<summary>Diff</summary>
````diff
@@ -16,11 +16,12 @@ author: sdgilley
 
 # Tutorial: Part 3 - Evaluate a custom chat application with the Azure AI Foundry SDK
 
-In this tutorial, you use the Azure AI SDK (and other libraries) to  evaluate and deploy the chat app you built in [Part 2 of the tutorial series](copilot-sdk-build-rag.md). In this part three, you learn how to:
+In this tutorial, you use the Azure AI SDK (and other libraries) to  evaluate the chat app you built in [Part 2 of the tutorial series](copilot-sdk-build-rag.md). In this part three, you learn how to:
 
 > [!div class="checklist"]
 > - Create an evaluation dataset
 > - Evaluate the chat app with Azure AI evaluators
+> - Iterate and improve your app
 
 
 This tutorial is part three of a three-part tutorial.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コパイロットSDK評価チュートリアルの文書修正"
}
```

### Explanation
この変更は、Azure AI Foundry SDKを利用したカスタムチャットアプリケーションの評価に関するチュートリアルの一部を修正するために行われました。具体的には、チュートリアルの内容から「デプロイ」が削除され、「評価」のみが残されました。さらに、チェックリストに「アプリを反復し改善する（Iterate and improve your app）」という項目が追加されました。これにより、評価プロセスにおけるアプリの改善の重要性が強調されています。全体で2行が追加され、1行が削除され、合計3行の変更が行われています。


