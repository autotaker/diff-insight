---
date: '2025-01-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f0e83bb...MicrosoftDocs:14202e8
summary: |-
  ハイライト部分では、Azure AI Foundryクイックスタートガイドのナビゲーションと機能説明が最新情報に基づき更新され、文言の明確化と自然な表現によって読みやすさが向上したことが述べられています。また、文書構成の変更によりユーザー体験が改善された点も強調されています。

  新機能として特筆すべきものはなく、既存の情報が明確かつ最新に調整されたことが報告されています。互換性が破棄される変更もありません。その他の更新では、特定の操作フローに関する説明が簡潔化され、新たに改善されたナビゲーションが導入されています。

  このアップデートは、スクリーンリーダーを使用するユーザーにとって重要な改善となり、技術的な操作ガイドの分かりづらさを軽減し、手順をより直感的にしています。特に、新しいプロジェクト作成やナビゲーション手順に関する指示が明確になり、情報へのアクセスが容易になります。今後、小規模な改善が積み重なり、Azure AI Foundryの利用促進につながることが期待されます。ユーザーは、いつでも最新の情報を元に操作できるようになり、プロジェクトのスムーズな管理が可能となります。これらの変更は小規模ながら、利用者に大きな価値を提供します。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f0e83bb...MicrosoftDocs:14202e8){target="_blank"}

# ハイライト

- スクリーンリーダーを用いたAzure AI Foundryクイックスタートガイドでのナビゲーションと機能説明が最新情報に基づき更新。
- 文言の明確化と自然な表現への改訂による読みやすさの向上。
- ユーザー体験の向上を目的とした文書構成の変更。

## 新機能

特筆すべき新機能の追加はありませんが、既存の情報がより明確かつ最新情報に基づいて細かく調整されています。

## 互換性が破棄されている変更

今回のアップデートによる互換性が破棄されている変更はありません。

## その他の更新

ガイド内の特定の操作フローに関する説明が簡潔化され、改善されたナビゲーションが導入されています。

# インサイト

Azure AI Foundryを使用するスクリーンリーダーのユーザーにとって、このクイックスタートガイドのアップデートは重要な改善であり、ユーザー体験の向上に大きく寄与します。元々、技術的な操作ガイドは多くのユーザーにとって難解と感じられることがありますが、今回の変更はこれらの手順をより分かりやすく、親しみやすいものにしています。

具体的には、新しいプロジェクトを作成または選択する際の指示や、それに続くナビゲーション手順がより直感的になるよう心を砕いているため、特にスクリーンリーダーの利用者にとっては情報へのアクセスがしやすくなっています。今後、このような小規模な改善が積み重なることで、Azure AI Foundryの利用促進につながることでしょう。

また、日付や特定セクションのアップデートによって、ユーザーは常に最新の情報を元に操作を行うことができ、これがプロジェクトのスムーズな管理に役立ちます。これらの変更は小規模でありながら、利用者にとっては大きな価値をもたらすものであるといえます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [screen-reader.md](#item-4dc029) | minor update | スクリーンリーダーを使用したAzure AI Foundryのクイックスタートの更新 | modified | 22 | 21 | 43 | 


# Modified Contents
## articles/ai-studio/tutorials/screen-reader.md{#item-4dc029}

<details>
<summary>Diff</summary>
````diff
@@ -8,26 +8,26 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: quickstart
-ms.date: 8/9/2024
+ms.date: 12/31/2024
 ms.reviewer: ailsaleen
 ms.author: sgilley
 author: sdgilley
 ---
 
 # QuickStart: Get started using Azure AI Foundry with a screen reader
 
-This article is for people who use screen readers such as [Microsoft's Narrator](https://support.microsoft.com/windows/complete-guide-to-narrator-e4397a0d-ef4f-b386-d8ae-c172f109bdb1#WindowsVersion=Windows_11), JAWS, NVDA or Apple's Voiceover. In this quickstart, you'll be introduced to the basic structure of Azure AI Foundry and discover how to navigate around efficiently. 
+This article is for people who use screen readers such as [Microsoft's Narrator](https://support.microsoft.com/windows/complete-guide-to-narrator-e4397a0d-ef4f-b386-d8ae-c172f109bdb1#WindowsVersion=Windows_11), JAWS, NVDA, or Apple's Voiceover. In this quickstart, you're introduced to the basic structure of Azure AI Foundry and discover how to navigate around efficiently. 
 
 ## Getting oriented in Azure AI Foundry portal 
 
 Most Azure AI Foundry pages are composed of the following landmark structure: 
 
 - Banner (contains Azure AI Foundry app title, settings, and profile information)
     - Might sometimes contain a breadcrumb navigation element 
-- Navigation
-    - The contents of the navigation are different depending on whether you have selected a hub or project in the studio
-- Main page content 
-    - Usually contains a command toolbar 
+- Navigation - There are three different states:
+    - Outside a project - there's no left navigation until you are in a project. The page is divided into sections such as **Work outside of a project** and **Recent projects picker**.
+    - In a project - the left navigation is the same for all parts of a project, until you move to the **Management center**.
+    - The left navigation in the Management center has a section for the hub that the project is in, then a section for the project itself.
 
 For efficient navigation, it might be helpful to navigate by landmarks to move between these sections on the page.
 
@@ -36,9 +36,9 @@ For efficient navigation, it might be helpful to navigate by landmarks to move b
 
 The navigation is list of links divided into different sections. 
 
-If you haven't yet created or selected a project, you can still explore content under the **Get started** (model catalog, model benchmarks, and AI Services) and **Management** (hubs and quota) sections.
+If you haven't yet created or selected a project, you can still explore content under the **Work outside of a project**.
 
-Once you have created or selected a project, you can access more capabilities such as project playgrounds, tools (such as prompt flow and evaluation), and components (such as data and deployments). 
+Once you have created or selected a project, you can access more capabilities such as Model catalog, Playgrounds, and AI Services. Then there are collapsible sections for **Build and customize** (includes Code, Fine-tuning, Prompt-flow), **Assess and improve** (includes Tracing, Evaluation, and Safety + security) and **My assets** (includes Models + endpoints, Data + indexes, and Web apps). 
 
 Once you have created or selected a project, you can also use the **Recent projects picker** button within the navigation to change project at any time.
 
@@ -48,29 +48,29 @@ For more information about the navigation, see [What is Azure AI Foundry](../wha
 
 To work within the Azure AI Foundry portal, you must first [create a project](../how-to/create-projects.md): 
 1. In [Azure AI Foundry](https://ai.azure.com), select **Home** from the navigation.
-1. Press the **Tab** key until you hear *New project* and select this button.  
-1. Enter the information requested in the **Create a project** dialog.  
+1. Press the **Tab** key until you hear *Create project* and select this button. 
+1. Enter the information requested in the **Create a project** dialog. 
 
-You then get taken to the project details page. 
+You then get taken to the project overview page. 
 
 ## Using the playground 
 
-The playground is where you can interact with models and experiment with different prompts and parameters. Different playgrounds are available depending on which model you would like to interact with.  
+The playground is where you can interact with models and experiment with different prompts and parameters. Different playgrounds are available depending on which model you would like to interact with. 
 
-Once you have created or selected a project, go to the navigation landmark. Press the down arrow until you hear *Project playground*. Press the down arrow again until you hear a playground you would like to use.
+Once you have created or selected a project, go to the navigation landmark. Press the down arrow until you hear *Playgrounds*.
 
 ### Chat playground structure 
 
-In this mode, the playground is composed of the command toolbar and two main sections: one for configuring your system message and other parameters, and the other for chatting to the model. If you added your own data in the playground, the **Citations** pane also appears when selecting a citation as part of the model response. 
+In this mode, the playground is composed of the command toolbar and two main sections: one for configuring your system message and other parameters, and the other for chatting to the model. If you added your own data in the playground, the **Add your data** pane also appears. 
 
 ### Chat session pane  
 
 The chat session pane is where you can chat to the model and test out your assistant. 
-- After you send a message, the model might take some time to respond, especially if the response is long. You hear a screen reader announcement "Message received from the chatbot" when the model finishes composing a response.  
+- After you send a message, the model might take some time to respond, especially if the response is long. You hear a screen reader announcement "Message received from the chatbot" when the model finishes composing a response. 
 
 ## Using prompt flow 
 
-Prompt flow is a tool to create executable flows, linking LLMs, prompts, and Python tools through a visualized graph. You can use this to prototype, experiment, and iterate on your AI applications before deploying.  
+Prompt flow is a tool to create executable flows, linking LLMs, prompts, and Python tools through a visualized graph. You can use this to prototype, experiment, and iterate on your AI applications before deploying. 
 
 Once you have created or selected a project, go to the navigation landmark. Press the down arrow until you hear *Prompt flow* and select this link.
 
@@ -80,11 +80,11 @@ The prompt flow UI in Azure AI Foundry portal is composed of the following main
 
 - This is the main working area where you can edit your flow, for example adding a new node, editing the prompt, selecting input data 
 - You can also choose to work in code instead of the editor by navigating to the **Raw file mode** toggle button to view the flow in code. 
-- Each node has its own H3 heading, which can be used for navigation.  
+- Each node has its own H3 heading, which can be used for navigation. 
 
 ### Files 
 
-- This section contains the file structure of the flow. Each flow has a folder that contains a flow.dag.yaml file, source code files, and system folders.  
+- This section contains the file structure of the flow. Each flow has a folder that contains a flow.dag.yaml file, source code files, and system folders. 
 - You can export or import a flow easily for testing, deployment, or collaborative purposes by navigating to the **Add** and **Zip and download all files** buttons.
 
 ### Graph view 
@@ -99,15 +99,15 @@ Evaluation is a tool to help you evaluate the performance of your generative AI
 
 ### Creating an evaluation 
 
-To review evaluation metrics, you must first create an evaluation.  
+To review evaluation metrics, you must first create an evaluation. 
 
 1. Once you have created or selected a project, go to the navigation landmark. Press the down arrow until you hear *Evaluation* and select this link.
-1. Press the Tab key until you hear *new evaluation* and select this button.  
+1. Press the Tab key until you hear *new evaluation* and select this button. 
 1. Enter the information requested in the **Create a new evaluation** dialog. Once complete, your focus is returned to the evaluations list. 
 
 ### Viewing evaluations 
 
-Once you create an evaluation, you can access it from the list of evaluations.  
+Once you create an evaluation, you can access it from the list of evaluations. 
 
 Evaluation runs are listed as links within the Evaluations grid. Selecting a link takes you to a dashboard view with information about your specific evaluation run. 
 
@@ -125,4 +125,5 @@ If you're a government, commercial, or enterprise customer, contact the enterpri
 ## Related content
 
 * Learn how you can build generative AI applications in the [Azure AI Foundry](../what-is-ai-studio.md).
+* [Build a custom knowledge retrieval (RAG) app with the Azure AI Foundry SDK](copilot-sdk-create-resources.md)
 * Get answers to frequently asked questions in the [Azure AI FAQ article](../faq.yml).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スクリーンリーダーを使用したAzure AI Foundryのクイックスタートの更新"
}
```

### Explanation
この変更は、Azure AI Foundryにおけるスクリーンリーダーを使用したクイックスタートガイドの内容を更新したものです。具体的には、文書中のいくつかの文の文言を明確化し、現行の機能やナビゲーション手順に合わせて修正しました。また、日付や具体的なセクション名についても新しい情報に基づいて更新されています。

特に変更された点には、ユーザーがプロジェクトを作成または選択した際のナビゲーションや利用可能な機能に関する表現の修正が含まれています。これにより、使用しているスクリーンリーダーのユーザーがよりスムーズに情報を得られるように配慮されています。また、細かな表現をより自然で親しみやすいものに改訂し、全体としての読みやすさを向上させています。 

文書の構成変更も含まれており、特定のフローを操作する方法や利用可能な機能についての説明が簡潔化されました。この更新により、Azure AI Foundryを利用する際のユーザー体験が改善されることが期待されます。


