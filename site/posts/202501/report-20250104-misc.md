---
date: '2025-01-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2f26af9...MicrosoftDocs:fbdf37a
summary: この差分は、Azure AI Studioおよび関連サービスのドキュメントに対するマイナーな修正を中心にしています。主な内容として、Azure OpenAI
  Studioの統合やプロジェクト作成手順、画像メタデータの更新が含まれています。新情報の提供と文書の可読性向上を目的とし、特に新機能の追加はありませんが、既存情報が最新に更新されています。互換性に影響を与える変更はなく、細かな修正が全体にわたっています。これにより、ユーザーはより正確で簡潔な情報を得られ、Azure
  AI Studioの利用がスムーズになることを目指しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2f26af9...MicrosoftDocs:fbdf37a){target="_blank"}

# ハイライト

この差分は、Azure AI Studioおよび関連するサービスのドキュメントに対するマイナーな修正を中心にしています。具体的には、Azure OpenAI Studioの統合、プロジェクト作成の手順、画像メタデータの更新などが含まれています。新しい情報提供と文書の可読性向上を主目的としています。

## 新機能
- 特に新機能の追加はありませんが、既存の情報が最新の状態に更新されています。

## 互換性に影響がある変更
- 互換性に影響を与える変更はありません。

## その他の更新
- 日付の更新、手順の明確化、メタデータの更新など、細かな修正が文書全体にわたって施されています。

# インサイト

このコード差分は、Azure AI Studioおよび関連ドキュメントの多方面にわたる調整を反映しています。特に、Azure OpenAI StudioがAzure AI Foundryポータルに統合されたことを示すために、言及されている「新しい名前」のインクルード文の削除が目立ちます。この更新により、ユーザーは現状に基づいた情報を取得できるようになっており、ドキュメントの理解が助けられています。

また、プロジェクト作成に関するドキュメントでは、特定の作成方法（Azure AI Foundryポータル、Python SDK、Azure CLI）についての説明がタブ形式で整理され、それぞれの前提条件が具体的に示されるようになりました。これにより、新規ユーザーや異なるバックグラウンドを持つユーザーがスムーズにプロジェクトを立ち上げられるようになっています。

さらに、画像資料のメタデータ更新は、目に見えない部分での品質向上を目指しています。直接的な内容の変更はありませんが、最新情報と一致させることで、ドキュメント全体の整合性を確保しています。

このような一連の修正は、ユーザーへの情報提供をより正確かつ簡潔にすることを目的としており、Azure AI Studioの利用者にとって負担を軽減することに寄与しています。ドキュメントの質的向上は、システムの信頼性維持とユーザーエクスペリエンスの向上に貢献しているといえるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-openai-in-ai-studio.md](#item-07639b) | minor update | Azure OpenAI Studioの統合についての修正 | modified | 0 | 2 | 2 | 
| [architecture.md](#item-22ed18) | minor update | Azure AI Foundryアーキテクチャに関するドキュメントの修正 | modified | 0 | 2 | 2 | 
| [create-projects.md](#item-cb10b3) | minor update | プロジェクト作成に関するドキュメントの更新 | modified | 23 | 5 | 28 | 
| [create-projects.md](#item-676667) | minor update | プロジェクト作成に関するインクルードドキュメントの更新 | modified | 2 | 2 | 4 | 
| [projects-create-details.png](#item-85d6e0) | minor update | プロジェクト作成の詳細図の更新 | modified | 0 | 0 | 0 | 
| [projects-create-review-finish.png](#item-47b678) | minor update | プロジェクトレビュー完了の詳細図の更新 | modified | 0 | 0 | 0 | 
| [projects-customize-hub.png](#item-11174c) | minor update | カスタマイズハブの詳細図の更新 | modified | 0 | 0 | 0 | 
| [what-is-ai-studio.md](#item-3ab62e) | minor update | AI Studioに関するドキュメントのテキスト修正 | modified | 0 | 2 | 2 | 


# Modified Contents
## articles/ai-studio/azure-openai-in-ai-studio.md{#item-07639b}

<details>
<summary>Diff</summary>
````diff
@@ -18,8 +18,6 @@ ms.custom: ignite-2023, build-2024, ignite-2024
 
 Azure OpenAI Service provides REST API access to OpenAI's powerful language models. Azure OpenAI Studio was previously where you went to access and work with the Azure OpenAI Service. This studio is now integrated into Azure AI Foundry portal. 
 
-[!INCLUDE [new-name](includes/new-name.md)]
-
 ## Access Azure OpenAI Service in Azure AI Foundry portal
 
 From the [Azure AI Foundry portal](https://ai.azure.com) landing page, use the **Let's go** button in the **Focused on Azure OpenAI Service?** section.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI Studioの統合についての修正"
}
```

### Explanation
この修正では、Azure OpenAI Studioに関するドキュメントの一部が更新されました。具体的には、Azure OpenAI StudioがAzure AI Foundryポータルに統合されたことを反映するため、2行が削除されました。この変更により、ユーザーに最新の情報を提供し、より正確にサービスへのアクセス方法を示しています。修正された部分では、「新しい名前」を示すインクルード文が削除されており、これによりドキュメントが一層明確になります。

## articles/ai-studio/concepts/architecture.md{#item-22ed18}

<details>
<summary>Diff</summary>
````diff
@@ -18,8 +18,6 @@ author: Blackmist
     
 Azure AI Foundry provides a unified experience for AI developers and data scientists to build, evaluate, and deploy AI models through a web portal, SDK, or CLI. Azure AI Foundry is built on capabilities and services provided by other Azure services.
 
-[!INCLUDE [new-name](../includes/new-name.md)]
-
 :::image type="content" source="../media/concepts/ai-studio-architecture.png" alt-text="Diagram of the high-level architecture of Azure AI Foundry." lightbox="../media/concepts/ai-studio-architecture.png":::
 
 At the top level, Azure AI Foundry provides access to the following resources:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryアーキテクチャに関するドキュメントの修正"
}
```

### Explanation
この修正は、Azure AI Foundryのアーキテクチャに関するドキュメント内で行われました。具体的には、2行が削除され、以前に含まれていた「新しい名前」を示すインクルード文が排除されました。この変更により、ドキュメントが一層簡潔になり、Azure AI Foundryの提供するリソースへのアクセスに関する情報が明確になります。全体として、この修正はドキュメントの整合性を高め、読者にとっての理解を助けるものです。

## articles/ai-studio/how-to/create-projects.md{#item-cb10b3}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: how-to
-ms.date: 10/01/2024
+ms.date: 01/03/2025
 ms.reviewer: deeikele
 ms.author: sgilley
 author: sdgilley
@@ -26,13 +26,29 @@ For more information about the projects and hubs model, see [Azure AI Foundry hu
 
 ## Prerequisites
 
+Use the following tabs to select the method you plan to use to create a project:
+
+# [Azure AI Foundry portal](#tab/ai-studio)
+
 - An Azure subscription. If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/).
-- For Python SDK or CLI steps, an Azure AI Foundry hub. If you don't have a hub, see [How to create and manage an Azure AI Foundry hub](create-azure-ai-resource.md). 
-- For Azure AI Foundry, a hub isn't required. It is created for you when needed.
+
+# [Python SDK](#tab/python)
+
+- An Azure subscription. If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/).
+- [Azure Machine Learning SDK v2](https://aka.ms/sdk-v2-install).
+- An Azure AI Foundry hub. If you don't have a hub, see [Create a hub using the Azure Machine Learning SDK and CLI](develop/create-hub-project-sdk.md).
+
+
+# [Azure CLI](#tab/azurecli)
+
+- An Azure subscription. If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/).
+- [Azure CLI and the machine learning extension](/azure/machine-learning/how-to-configure-cli).
+- An Azure AI Foundry hub. If you don't have a hub, see [Create a hub using the Azure Machine Learning SDK and CLI](develop/create-hub-project-sdk.md).
+
+---
 
 ## Create a project
 
-Use the following tabs to select the method you plan to use to create a project:
 
 # [Azure AI Foundry portal](#tab/ai-studio)
 
@@ -78,9 +94,11 @@ The code in this section assumes you have an existing hub.  If you don't have a
 1. Once the extension is installed and authenticated to your Azure subscription, use the following command to create a new Azure AI Foundry project from an existing Azure AI Foundry hub:
 
     ```azurecli
-    az ml workspace create --kind project --hub-id {my_hub_ARM_ID} --resource-group {my_resource_group} --name {my_project_name}
+    az ml workspace create --kind project --hub-id {my_hub_ID} --resource-group {my_resource_group} --name {my_project_name}
     ```
 
+    Form `my_hub_ID` with this syntax: `/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{hub_name}`.
+
 ---
 
 ## View project settings
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクト作成に関するドキュメントの更新"
}
```

### Explanation
この修正では、Azure AI Studioのプロジェクト作成に関するドキュメントが更新され、全体で28箇所の変更が行われました。主な変更点として、日付が「2024年10月1日」から「2025年1月3日」に更新され、事前条件のセクションが明確化されました。特に、プロジェクトを作成するための異なる方法（Azure AI Foundryポータル、Python SDK、Azure CLI）に分かりやすいタブを追加し、各方法に関連する前提条件が詳細に記載されています。また、コマンドラインの構文が強化され、ハブの識別子についての具体例が加えられました。これにより、ユーザーがプロジェクトをスムーズに作成できるようになりました。

## articles/ai-studio/includes/create-projects.md{#item-676667}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.reviewer: deeikele
 ms.author: sgilley
 ms.service: azure-ai-studio
 ms.topic: include
-ms.date: 11/19/2024
+ms.date: 01/03/2025
 ms.custom: include, build-2024, ignite-2024
 ---
 
@@ -23,7 +23,7 @@ To create a project in [Azure AI Foundry](https://ai.azure.com), follow these st
 
 1. If you don't have a hub, a default one is created for you.  If you want to customize the default values, see the next section.
 
-1. Select **Create a project**.  Or, if you want to customize a new hub, follow the steps in the next section.
+1. Select **Create**.  Or, if you want to customize a new hub, follow the steps in the next section.
 
 ### Customize the hub
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクト作成に関するインクルードドキュメントの更新"
}
```

### Explanation
この修正は、Azure AI Studioにおけるプロジェクト作成に関連するインクルードドキュメントに対して行われました。主な変更点は、メタデータの日付が「2024年11月19日」から「2025年1月3日」に更新されたことと、プロジェクト作成の手順で「**Create a project**」という表現を「**Create**」に変更したことです。この修正により、ドキュメントの内容が最新の情報を反映し、より簡潔になりました。また、手順が明確化され、ユーザーがプロジェクトを作成する際の理解が向上します。全体として、ドキュメントの可読性や利便性が高まっていると言えます。

## articles/ai-studio/media/how-to/projects/projects-create-details.png{#item-85d6e0}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクト作成の詳細図の更新"
}
```

### Explanation
この変更は、Azure AI Studioのプロジェクト作成に関する詳細を示す画像（`projects-create-details.png`）に関して行われましたが、具体的な追加や削除はなく、内容に変更はありません。この修正では、画像のメタデータが更新された可能性がありますが、視覚的なコンテンツ自体には影響がありません。ユーザーにとっての重要性は低いものの、ドキュメント全体の整合性を保つために必要な更新と言えます。画像が最新情報に対応していることを確認することは、全体的なユーザー体験を向上させるために重要です。

## articles/ai-studio/media/how-to/projects/projects-create-review-finish.png{#item-47b678}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクトレビュー完了の詳細図の更新"
}
```

### Explanation
この変更は、Azure AI Studioにおけるプロジェクトレビューの完了に関する画像（`projects-create-review-finish.png`）に関連していますが、実際には追加や削除はなく、画像自体の内容に変更はありません。この変更は、画像のメタデータが調整された可能性があります。確固たる変更はないため、ユーザーへの影響はほとんどありませんが、ドキュメントの整合性と最新の状態を保つためには重要な更新です。このような更新により、ドキュメント全体の品質が向上し、ユーザーにより良い体験を提供することができます。

## articles/ai-studio/media/how-to/projects/projects-customize-hub.png{#item-11174c}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタマイズハブの詳細図の更新"
}
```

### Explanation
この変更は、Azure AI Studioのプロジェクトにおけるカスタマイズハブを示す画像（`projects-customize-hub.png`）に関連しています。変更内容としては、追加や削除は行われておらず、画像自体に対する具体的な変更もありません。この変更は、画像のメタデータなどが更新された可能性がありますが、視覚的なコンテンツには影響がないため、ユーザーにとっての重要性は低いです。しかし、このような更新はドキュメントの整合性を保つために重要であり、常に最新の情報を提供し続けるための一環と考えられます。こうしたマイナーな修正が、全体的なユーザー体験に貢献します。

## articles/ai-studio/what-is-ai-studio.md{#item-3ab62e}

<details>
<summary>Diff</summary>
````diff
@@ -18,8 +18,6 @@ ms.custom: ignite-2023, build-2024, ignite-2024
 
 [Azure AI Foundry](https://ai.azure.com) is a trusted platform that empowers developers to drive innovation and shape the future with AI in a safe, secure, and responsible way.
 
-[!INCLUDE [new-name](includes/new-name.md)]
-
 [Azure AI Foundry](https://ai.azure.com) is designed for developers to:
 
 - Build generative AI applications on an enterprise-grade platform.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Studioに関するドキュメントのテキスト修正"
}
```

### Explanation
この変更は、AI Studioに関する文書（`what-is-ai-studio.md`）におけるテキストの修正に関連しています。具体的には、2行のテキストが削除され、内容の整理が行われました。削除された部分は、Azure AI Foundryの記述の前に「[!INCLUDE [new-name](includes/new-name.md)]」という命令と、その後の改行を含んでいます。この修正により、文書がよりスムーズに読みやすくなり、情報の伝達が向上しています。内容自体の重要性には影響がないため、この変更は主に文書のクオリティ向上に寄与するものです。


