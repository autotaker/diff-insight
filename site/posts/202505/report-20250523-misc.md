---
date: '2025-05-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:aedda49...MicrosoftDocs:2512fb2
summary: このコードの変更では、特定のチュートリアルに関連する`toc.yml`ファイルの一部リンクを削除し、`prompt-flow.md`ファイルを全体的に削除しています。これらの変更は、ナビゲーションの明確化とサービスの方針変更を目的としています。新機能は追加されておらず、いくつかの重大な変更として、チュートリアルリンクの削除や、利用不可となるチュートリアルの存在が挙げられます。この更新は、ユーザー体験の向上を図るためのものであり、サービスの進化に伴い、ドキュメントが常に最新の状態であることの重要性を再認識させる内容となっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:aedda49...MicrosoftDocs:2512fb2){target="_blank"}

# ハイライト
このコードの変更では、特定のチュートリアルに関連する`toc.yml`ファイルの一部リンクの削除と、`prompt-flow.md`ファイル全体の削除が行われています。変更は、ナビゲーションの明確化とサービスの方針変更を目的としています。

## 新機能
特に新機能の追加はありません。

## 破壊的変更
1. チュートリアルリンク「Use language in prompt flow」の`toc.yml`からの削除。
2. `prompt-flow.md`ファイルの削除によるチュートリアル「Use Language in Azure prompt flow」の利用不可。

## その他の更新
特にその他の更新はありません。

# インサイト
今回の差分は、ナビゲーションの整頓とサービス戦略の変更に伴うものと考えられます。まず、`toc.yml`ファイルから特定のチュートリアルリンクが削除されている点に注目できます。このリンク削除は、ドキュメント全体の構造をシンプルにし、ユーザーが関連情報を見つけやすくするためのものです。これにより、ユーザー体験の向上が期待されます。

次に、`prompt-flow.md`の削除について、これは特定の機能やサービスが現在のリソースから不要となった、もしくは刷新される可能性を示唆しています。このドキュメントはAzureのプロンプトフローにおける言語の使用方法を説明していました。関連するユーザーにとっては、このリソースの消失は重要な情報源の欠如を意味し、他の情報源の利用が求められるでしょう。おそらく、サービスの進化や、新しい方法論の導入によって内容が古くなったため削除に至ったと考えられます。

今回の更新は、Azureの開発やAIサービスの今後の方向性を示唆しており、ドキュメントが常に最新の状態であることの重要性を再確認させるものです。ユーザーは、今後のドキュメントの変更に注視し、最新情報を適用する準備が求められます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [toc.yml](#item-12f1f0) | minor update | TOCから一部のチュートリアルリンクを削除 | modified | 0 | 2 | 2 | 
| [prompt-flow.md](#item-22c24b) | breaking change | チュートリアル「Use Language in Azure prompt flow」の削除 | removed | 0 | 65 | 65 | 


# Modified Contents
## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -713,8 +713,6 @@ items:
     href: tutorials/use-kubernetes-service.md
   - name: Use language in power automate flows
     href: tutorials/power-automate.md
-  - name: Use language in prompt flow
-    href: tutorials/prompt-flow.md
   - name: Native document support
     items:
     - name: Native documents for language processing
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCから一部のチュートリアルリンクを削除"
}
```

### Explanation
この変更は、`toc.yml`ファイル内の内容を更新したもので、特定のチュートリアルリンクが削除されました。具体的には、「Use language in prompt flow」という項目が削除されています。この変更は、リストの整頓を目的としており、全体的なナビゲーションの明確さを向上させることに寄与します。ファイル内の他の項目はそのまま維持されており、削除されたリンク以外の情報には影響を与えないため、システムの機能には大きな変更はありません。

## articles/ai-services/language-service/tutorials/prompt-flow.md{#item-22c24b}

<details>
<summary>Diff</summary>
````diff
@@ -1,65 +0,0 @@
----
-title: Use Language in Azure prompt flow
-description: Learn how to use Azure AI Language in prompt flow.
-author: jboback
-ms.author: jboback
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 01/31/2025
----
-
-# Use Language in Azure prompt flow
-
-> [!IMPORTANT]
-> Some of the features described in this article might only be available in preview. This preview is provided without a service-level agreement, and we don't recommend it for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
-
-[Prompt flow in Azure AI Foundry portal](../../../ai-foundry/how-to/prompt-flow.md) is a development tool designed to streamline the entire development cycle of AI applications powered by Large Language Models (LLMs). You can explore and quickly start to use and fine-tune various natural language processing capabilities from Azure AI Language, reducing your time to value and deploying solutions with reliable evaluation.
-
-This tutorial teaches you how to use Language in prompt flow utilizing [Azure AI Foundry](https://ai.azure.com).                            
-
-## Prerequisites
-
-- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
-
-- Your subscription needs to be below your [quota limit](../../../ai-foundry/how-to/quota.md) to deploy a new flow in this tutorial.
-
-## Create a project in Azure AI Foundry portal
-
-Your project is used to organize your work and save state. 
-
-[!INCLUDE [Create project](../../../ai-foundry/includes/create-hub-project.md)]
-
-## Using Azure AI Language via the prompt flow gallery
-
-You can create an Azure AI Language flow by either cloning the samples available in the gallery or creating a flow from scratch. If you already have flow files in local or file share, you can also import the files to create a flow. For the purposes of this tutorial we'll be using the prebuilt **Analyze Conversations** flow.
-
-To create a prompt flow from the gallery in [Azure AI Foundry portal](https://ai.azure.com/):
-
-1. Sign in to Azure AI Foundry and select your project.
-
-1. From the collapsible left menu, select Prompt flow.
-
-1. Select + Create.
-
-1. Find the **Analyze Conversations** tile in the gallery and select *Clone*.
-
-1. In the right sidebar, name the folder and click the **Clone** button.
-
-1. After the process is complete, you'll be taken to the prompt flow wizard. Click **Start Compute Session** in the upper right hand corner to begin. The various parts of the wizard are out lined below:
-
-    :::image type="content" source="../media/prompt-flow/prompt-flow-wizard.png" alt-text="Screenshot of the prompt flow wizard page with each part of the tool numbered." lightbox="../media/prompt-flow/prompt-flow-wizard.png":::
-
-    1. A graph view of your flow.
-    1. Files in your flow. Click the arrow to expand this section.
-    1. Azure AI Language tools in the "More tools" dropdown menu, which you can add capabilities that you need for your flow. There are more tools that you can add from LLM, Prompt, and Python menu. This menu is only accessible after the compute session has started.
-    1. Configure your output.
-    1. Configure steps (or tools) in the flow.
-    1. Run, evaluate, and deploy your flow.
-
-1. Once you've configured everything to your liking, press the run button in the upper right hand corner.
-
-## Related content
-
-* [Azure AI Language homepage](https://aka.ms/azure-language)
-* [Azure AI Language product demo videos](https://aka.ms/language-videos)
-* [Explore Azure AI Language in Azure AI Foundry portal](https://aka.ms/AzureAiLanguage)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "チュートリアル「Use Language in Azure prompt flow」の削除"
}
```

### Explanation
この変更は、`prompt-flow.md`ファイルが完全に削除されたことを示しています。このチュートリアルは、Azureの「プロンプトフロー」における言語の使用方法についての説明を提供していましたが、今後は利用できなくなります。この変更により、関連する機能や情報を必要とするユーザーに対するリソースが削除されるため、今後の参考にすることができません。チュートリアルに含まれていた情報は、プロジェクト作成やフローの利用方法、必須条件、関連コンテンツなどを網羅していたため、削除による影響は大きいです。この決定は、特定の機能の見直しやサービスの方針変更に基づくものと見られます。


