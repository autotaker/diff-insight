---
date: '2025-05-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2512fb2...MicrosoftDocs:71433b6
summary: このコード変更は、複数のドキュメントの更新を包括しており、主に新しい日付への更新、手順の明確化、APIバージョンの更新が焦点です。ユーザーがより効率的に操作できるように、モデルの対応状況や地域情報の見直しが行われています。また、画像の更新や削除も含まれ、視覚的な情報の精度向上が図られています。全体として、これらの変更はユーザーエクスペリエンスの向上を目的としており、特に音声生成モデルやリアルタイムモデルに関する手順が強化されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2512fb2...MicrosoftDocs:71433b6){target="_blank"}

# Highlights
このコードの変更は、複数のドキュメントの更新を包括しています。特に主な焦点は、新しい日付への更新、手順の明確化、APIバージョンの更新にあります。また、モデルの対応状況と地域情報が見直され、ユーザーがより効率的に操作できるようになっています。画像の更新や削除も含まれ、視覚的な情報の精度向上を図っています。

## New features
- 新しい音声およびモデル用の手順の明確化
- APIバージョンのアップデート
- モデルの提供地域情報の更新

## Breaking changes
- リアルタイムプレイグラウンド画像の削除により、関連ドキュメントから視覚的情報が失われる可能性

## Other updates
- ドキュメント日付の更新が行われ、全体の一貫性と最新情報の提供が強化されています。
- 目次ファイルの整備により、ユーザビリティの向上が図られています。

# Insights
このコード変更は、ユーザーエクスペリエンスの向上に重きが置かれています。更新された日付は、技術文書が最新であることを示し、信頼性を維持します。新しい手順の追加は、Azure AI Foundryポータルを利用する際のユーザーの混乱を避けることを目的としています。特に音声生成モデルやリアルタイムモデル関連での手順の強化は、実践的かつ明確なガイダンスを提供します。

APIバージョンの更新は、新機能や修正を利用者へ迅速に提供するために重要です。最新のAPI仕様に基づいた情報は、ユーザーが直面する可能性のあるエラーを未然に防ぐ助けとなります。また、グローバルおよび地域モデルの提供状況の更新は、ユーザーがそれぞれのニーズに応じて最適なモデルを選択する手助けとなります。

一方で、リアルタイムプレイグラウンド画像の削除は、ユーザーは他のリソースに頼らなければならず、潜在的な混乱を引き起こす可能性があります。これを補うために、代替のビジュアルコンテンツや詳細な説明が他のドキュメントで求められます。全体として、これらの変更は、ユーザーがAzure OpenAIサービスをより効果的に利用するための一歩として機能します。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [audio-completions-quickstart.md](#item-be5860) | minor update | 音声生成のクイックスタートの日付更新 | modified | 1 | 1 | 2 | 
| [models.md](#item-db2c37) | minor update | モデルに関するドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [audio-completions-ai-foundry.md](#item-748538) | minor update | 音声生成モデルのChatプレイグラウンドへのアクセス手順の更新 | modified | 8 | 2 | 10 | 
| [audio-completions-deploy-model.md](#item-c5a63e) | minor update | 音声生成モデルのデプロイ手順の更新 | modified | 6 | 6 | 12 | 
| [datazone-provisioned-managed.md](#item-ae7f5b) | minor update | モデルの対応状況マトリックスの更新 | modified | 15 | 15 | 30 | 
| [provisioned-global.md](#item-340884) | minor update | グローバルモデルマトリックスの更新 | modified | 29 | 28 | 57 | 
| [provisioned-models.md](#item-8ee639) | minor update | プロビジョニングされたモデルの更新 | modified | 28 | 27 | 55 | 
| [realtime-deploy-model.md](#item-21f911) | minor update | リアルタイムモデルデプロイ手順の更新 | modified | 6 | 6 | 12 | 
| [realtime-portal.md](#item-1b81a2) | minor update | リアルタイムポータルの使用手順の改善 | modified | 9 | 8 | 17 | 
| [text-to-speech-rest.md](#item-d067a1) | minor update | テキスト音声合成APIのバージョン更新 | modified | 2 | 2 | 4 | 
| [text-to-speech-typescript.md](#item-1335d5) | minor update | テキスト音声合成APIのTypeScriptサンプルのバージョン更新 | modified | 2 | 2 | 4 | 
| [real-time-playground-start-listening.png](#item-076ae4) | breaking change | リアルタイムプレイグラウンド画像の削除 | removed | 0 | 0 | 0 | 
| [real-time-playground.png](#item-a36b1d) | minor update | リアルタイムプレイグラウンド画像の更新 | modified | 0 | 0 | 0 | 
| [realtime-audio-quickstart.md](#item-727df8) | minor update | リアルタイムオーディオクイックスタートの更新 | modified | 1 | 1 | 2 | 
| [text-to-speech-quickstart.md](#item-c344ad) | minor update | テキストから音声へのクイックスタートの更新 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c945af) | minor update | 目次ファイルの更新 | modified | 0 | 2 | 2 | 
| [whisper-quickstart.md](#item-4cae3d) | minor update | Whisperクイックスタートの更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/audio-completions-quickstart.md{#item-be5860}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Walkthrough on how to get started with audio generation using Azure
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 2/6/2025
+ms.date: 5/23/2025
 author: eric-urban
 ms.author: eur
 ms.custom: references_regions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "音声生成のクイックスタートの日付更新"
}
```

### Explanation
この変更は、ドキュメント「audio-completions-quickstart.md」の修正を示しています。具体的には、ファイル内の更新が1つ追加され、1つが削除されました。主な変更点は、文書の日付を「2025年2月6日」から「2025年5月23日」へと更新したことです。この更新により、音声生成に関するチュートリアルの最新の情報を提供し、利用者が正確なリリース日を把握できるようになっています。リンク先のリポジトリや変更内容の詳細も反映されています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 05/07/2025
+ms.date: 05/23/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルに関するドキュメントの日付更新"
}
```

### Explanation
この変更は、「models.md」という文書の修正を示しています。具体的には、文書内の日付が「2025年5月7日」から「2025年5月23日」へと更新されました。この変更により、Azure OpenAI に関連するモデルの異なる機能に関する最新の情報が反映され、利用者に正確な日付を提供します。加えて、他のメタ情報や管理者、著者に関する情報も維持されています。この文書は、Azure OpenAI のモデルについての概念的な内容を学ぶためのものです。

## articles/ai-services/openai/includes/audio-completions-ai-foundry.md{#item-748538}

<details>
<summary>Diff</summary>
````diff
@@ -17,8 +17,14 @@ ms.date: 1/7/2025
 
 To chat with your deployed `gpt-4o-mini-audio-preview` model in the **Chat** playground of [Azure AI Foundry portal](https://ai.azure.com), follow these steps:
 
-1. Go to the [Azure OpenAI in Azure AI Foundry Models page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI in Azure AI Foundry Models resource and the deployed `gpt-4o-mini-audio-preview` model.
-1. Select the **Chat** playground from under **Resource playground** in the left pane.
+1. Go to the [Azure AI Foundry portal](https://ai.azure.com) and select your project that has your deployed `gpt-4o-mini-audio-preview` model.
+1. Go to your project in [Azure AI Foundry](https://ai.azure.com). 
+1. Select **Playgrounds** from the left pane.
+1. Select **Audio playground** > **Try the Chat playground**. 
+
+    > [!NOTE]
+    > The **Audio playground** doesn't support the `gpt-4o-mini-audio-preview` model. Use the **Chat playground** as described in this section.
+
 1. Select your deployed `gpt-4o-mini-audio-preview` model from the **Deployment** dropdown. 
 1. Start chatting with the model and listen to the audio responses.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "音声生成モデルのChatプレイグラウンドへのアクセス手順の更新"
}
```

### Explanation
この変更は、「audio-completions-ai-foundry.md」ファイルの更新を示しており、主に音声生成モデル「gpt-4o-mini-audio-preview」を使用する際の指示が明確にされています。具体的には、手順が8行追加され、2行が削除されており、合計で10の変更が加えられました。

新しい手順では、まずAzure AI Foundryポータルにアクセスし、プロジェクトを選択することから始まり、次に左のペインから「Playgrounds」を選ぶことが求められており、音声生成に関連する情報が整理されています。また、「Audio playground」では「gpt-4o-mini-audio-preview」モデルがサポートされていないことを示す注釈も追加され、利用者に正しい手順を提供しています。この変更により、ユーザーは音声モデルをより効率的に利用できるようになります。

## articles/ai-services/openai/includes/audio-completions-deploy-model.md{#item-c5a63e}

<details>
<summary>Diff</summary>
````diff
@@ -4,15 +4,15 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 1/21/2025
+ms.date: 5/23/2025
 ---
 
 To deploy the `gpt-4o-mini-audio-preview` model in the Azure AI Foundry portal:
-1. Go to the [Azure OpenAI in Azure AI Foundry Models page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI in Azure AI Foundry Models resource and the deployed `gpt-4o-mini-audio-preview` model.
-1. Select the **Chat** playground from under **Playgrounds** in the left pane.
-1. Select **+ Create new deployment** > **From base models** to open the deployment window. 
-1. Search for and select the `gpt-4o-mini-audio-preview` model and then select **Deploy to selected resource**.
-1. In the deployment wizard, select the `2024-12-17` model version.
+1. Go to the [Azure AI Foundry portal](https://ai.azure.com) and create or select your project. 
+1. Select **Models + endpoints** from under **My assets** in the left pane.
+1. Select **+ Deploy model** > **Deploy base model** to open the deployment window. 
+1. Search for and select the `gpt-4o-mini-audio-preview` model and then select **Confirm**.
+1. Review the deployment details and select **Deploy**.
 1. Follow the wizard to finish deploying the model.
 
 Now that you have a deployment of the `gpt-4o-mini-audio-preview` model, you can interact with it in the Azure AI Foundry portal **Chat** playground or chat completions API.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "音声生成モデルのデプロイ手順の更新"
}
```

### Explanation
この変更は、「audio-completions-deploy-model.md」という文書の修正を示しており、音声モデル「gpt-4o-mini-audio-preview」をAzure AI Foundryポータルでデプロイするための手順が更新されました。具体的には、手順が古い情報から新しい構成に変更され、合計で12の変更が行われています。このうち6行が追加され、6行が削除されました。

新しい手順では、ポータルのアクセス方法が明確に指示され、以前の手順に比べて分かりやすくなっています。ユーザーは「My assets」セクションから「Models + endpoints」を選択し、新しいモデルデプロイの手順に沿ってモデルを確認することが求められています。また、モデルのバージョンに関する情報も更新され、より正確な手順がユーザーに提供されています。この変更により、ユーザーは音声モデルのデプロイをスムーズに行うことができるようになります。

## articles/ai-services/openai/includes/model-matrix/datazone-provisioned-managed.md{#item-ae7f5b}

<details>
<summary>Diff</summary>
````diff
@@ -10,18 +10,18 @@ ms.date: 05/05/2025
 ---
 
 
-| **Region**     | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:---------------------------:|:--------------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
-| eastus             | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus2            | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| francecentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| italynorth         | ✅                        | -                            | -                       | -                  | -                      | -                      | -                      | -                           |
-| northcentralus     | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| polandcentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southcentralus     | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| spaincentral       | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westeurope         | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus             | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| **Region**     | **o3**, **2025-04-16**   | **o4-mini**, **2025-04-16**   | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-nano**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:----------------------:|:---------------------------:|:---------------------------:|:--------------------------------:|:--------------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
+| eastus             | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus2            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| italynorth         | ✅                   | ✅                        | ✅                        | ✅                             | -                            | -                       | -                  | -                      | -                      | -                      | -                           |
+| northcentralus     | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの対応状況マトリックスの更新"
}
```

### Explanation
この変更は、「datazone-provisioned-managed.md」ファイル内のモデルマトリックスに関する情報の更新を反映しています。具体的には、モデルのバージョンと提供地域の情報が見直され、合計で30の変更が行われました。このうち15行が新たに追加され、15行が削除されています。

変更点では、以前のモデル名が新しいモデル名に置き換えられており、モデルのバージョンや地域に関する情報が更新されています。新しいテーブルは「o3」や「o4-mini」などのモデルを追加し、より多くの地域について最新の対応状況を示しています。この変更により、ユーザーは利用可能なモデルのバージョンと地域を容易に把握でき、適切な選択を行うことができるようになります。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -9,31 +9,32 @@ ms.custom: references_regions
 ms.date: 05/05/2025
 ---
 
-| **Region**     | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:---------------------------:|:--------------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
-| australiaeast      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| brazilsouth        | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| canadaeast         | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus             | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus2            | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| francecentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| italynorth         | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| japaneast          | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| koreacentral       | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| northcentralus     | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| norwayeast         | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| polandcentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southafricanorth   | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southcentralus     | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southeastasia      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southindia         | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| spaincentral       | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandnorth   | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandwest    | ✅                        | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| uaenorth           | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| uksouth            | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westeurope         | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus             | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+
+| **Region**     | **o3**, **2025-04-16**   | **o4-mini**, **2025-04-16**   | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-nano**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:----------------------:|:---------------------------:|:---------------------------:|:--------------------------------:|:--------------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
+| australiaeast      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| brazilsouth        | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| canadaeast         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus             | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus2            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| italynorth         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| japaneast          | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| koreacentral       | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| northcentralus     | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| norwayeast         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southafricanorth   | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southeastasia      | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southindia         | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandnorth   | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandwest    | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| uaenorth           | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| uksouth            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                   | ✅                        | ✅                        | -                            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                   | ✅                        | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルモデルマトリックスの更新"
}
```

### Explanation
この変更は、「provisioned-global.md」ファイルにおけるグローバルモデルマトリックスの更新を示しています。合計で57の変更が行われ、29行が新しく追加され、28行が削除されました。主な変更点は、モデル名とそのバージョンに関する情報が新しいものに更新されたことです。

新たに追加されたモデルやバージョンには「o3」や「o4-mini」などが含まれ、さらに対応する地域のモデル使用可能状況が再構成されています。すべての地域に対して最新の情報が反映され、ユーザーが特定のモデルが利用可能な地域をより簡単に確認できるようになっています。この更新により、ユーザーはより正確で信頼できる情報に基づいてモデルの選択を行うことができるようになります。

## articles/ai-services/openai/includes/model-matrix/provisioned-models.md{#item-8ee639}

<details>
<summary>Diff</summary>
````diff
@@ -10,30 +10,31 @@ ms.date: 05/07/2025
 ---
 
 
-| **Region**     | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
-|:-------------------|:---------------------------:|:--------------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|
-| australiaeast      | -                       | -                            | ✅                        | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| brazilsouth        | -                       | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | -                      |
-| canadaeast         | -                       | -                            | ✅                        | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      |
-| eastus             | ✅                        | ✅                             | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| eastus2            | ✅                        | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| francecentral      | -                       | -                            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | -                      | ✅                       |
-| germanywestcentral | -                       | -                            | -                       | -                  | ✅                       | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | -                      |
-| japaneast          | -                       | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | -               | ✅                        | ✅                        | ✅                            | -                   | -                      | ✅                       |
-| koreacentral       | -                       | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | -                       | -                       | ✅                            | ✅                    | ✅                       | -                      |
-| northcentralus     | ✅                        | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| norwayeast         | -                       | -                            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                           | ✅                    | -                      | -                      |
-| polandcentral      | -                       | -                            | -                       | -                  | ✅                       | -                      | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| southafricanorth   | -                       | -                            | -                       | -                  | ✅                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                            | ✅                    | ✅                       | -                      |
-| southcentralus     | ✅                        | -                            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| southeastasia      | -                       | -                            | -                       | -                  | -                      | ✅                       | ✅                       | ✅                            | -               | -                       | -                       | -                           | -                   | -                      | -                      |
-| southindia         | -                       | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | ✅                       |
-| spaincentral       | -                       | -                            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
-| swedencentral      | -                       | ✅                             | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| switzerlandnorth   | -                       | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| switzerlandwest    | -                       | -                            | -                       | -                  | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
-| uaenorth           | -                       | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | -                           | -               | ✅                        | -                       | -                           | -                   | ✅                       | ✅                       |
-| uksouth            | -                       | -                            | -                       | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| westeurope         | -                       | -                            | -                       | -                  | -                      | -                      | ✅                       | -                           | -               | -                       | -                       | -                           | -                   | -                      | -                      |
-| westus             | ✅                        | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| westus3            | ✅                        | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+
+| **Region**     | **o3**, **2025-04-16**   | **o4-mini**, **2025-04-16**   | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-nano**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
+|:-------------------|:----------------------:|:---------------------------:|:---------------------------:|:--------------------------------:|:--------------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|
+| australiaeast      | -                  | -                       | -                       | -                            | -                            | ✅                        | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| brazilsouth        | -                  | -                       | -                       | -                            | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | -                      |
+| canadaeast         | -                  | -                       | -                       | -                            | -                            | ✅                        | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      |
+| eastus             | -                  | ✅                        | ✅                        | ✅                             | ✅                             | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| eastus2            | ✅                   | ✅                        | ✅                        | -                            | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| francecentral      | -                  | -                       | -                       | -                            | -                            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | -                      | ✅                       |
+| germanywestcentral | -                  | -                       | -                       | -                            | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | -                      |
+| japaneast          | -                  | -                       | -                       | -                            | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | -               | ✅                        | ✅                        | ✅                            | -                   | -                      | ✅                       |
+| koreacentral       | -                  | -                       | -                       | -                            | -                            | ✅                        | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | -                       | -                       | ✅                            | ✅                    | ✅                       | -                      |
+| northcentralus     | -                  | ✅                        | ✅                        | -                            | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| norwayeast         | -                  | -                       | -                       | -                            | -                            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                           | ✅                    | -                      | -                      |
+| polandcentral      | -                  | -                       | -                       | -                            | -                            | -                       | -                  | ✅                       | -                      | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| southafricanorth   | -                  | -                       | -                       | -                            | -                            | -                       | -                  | ✅                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                            | ✅                    | ✅                       | -                      |
+| southcentralus     | -                  | ✅                        | ✅                        | -                            | -                            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| southeastasia      | -                  | -                       | -                       | -                            | -                            | -                       | -                  | -                      | ✅                       | ✅                       | ✅                            | -               | -                       | -                       | -                           | -                   | -                      | -                      |
+| southindia         | -                  | -                       | -                       | -                            | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | ✅                       |
+| spaincentral       | -                  | -                       | -                       | -                            | -                            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
+| swedencentral      | -                  | -                       | -                       | ✅                             | ✅                             | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| switzerlandnorth   | -                  | -                       | -                       | -                            | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| switzerlandwest    | -                  | -                       | -                       | -                            | -                            | -                       | -                  | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
+| uaenorth           | -                  | -                       | -                       | -                            | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | -                           | -               | ✅                        | -                       | -                           | -                   | ✅                       | ✅                       |
+| uksouth            | -                  | -                       | -                       | -                            | -                            | -                       | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| westeurope         | -                  | -                       | -                       | -                            | -                            | -                       | -                  | -                      | -                      | ✅                       | -                           | -               | -                       | -                       | -                           | -                   | -                      | -                      |
+| westus             | -                  | ✅                        | ✅                        | -                            | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| westus3            | -                  | ✅                        | ✅                        | -                            | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされたモデルの更新"
}
```

### Explanation
この変更は、「provisioned-models.md」ファイルにおけるプロビジョニングされたモデルに関する情報の更新を反映しています。合計で55の変更が行われ、28行が追加され、27行が削除されています。この変更では、モデルのバージョン名及び利用可能な地域の情報が見直され、最新の情報が提供されています。

新たに追加されたモデルとして「o3」や「o4-mini」があり、特定の地域におけるモデルの利用可能状況が更新されています。テーブルの内容が整理され、ユーザーは各地域で利用可能なモデルを迅速に確認できるようになりました。また、利用できないモデルについても明示的に示されており、情報のクリアさが向上しています。この更新により、ユーザーはプロビジョニングされたモデルの選択肢をより容易に把握し、効率的に利用できるようになります。

## articles/ai-services/openai/includes/realtime-deploy-model.md{#item-21f911}

<details>
<summary>Diff</summary>
````diff
@@ -8,11 +8,11 @@ ms.date: 1/21/2025
 ---
 
 To deploy the `gpt-4o-mini-realtime-preview` model in the Azure AI Foundry portal:
-1. Go to the [Azure OpenAI in Azure AI Foundry Models page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI in Azure AI Foundry Models resource (with or without model deployments.)
-1. Select the **Real-time audio** playground from under **Playgrounds** in the left pane.
-1. Select **+ Create new deployment** > **From base models** to open the deployment window. 
-1. Search for and select the `gpt-4o-mini-realtime-preview` model and then select **Deploy to selected resource**.
-1. In the deployment wizard, select the `2024-12-17` model version.
+1. Go to the [Azure AI Foundry portal](https://ai.azure.com) and create or select your project. 
+1. Select **Models + endpoints** from under **My assets** in the left pane.
+1. Select **+ Deploy model** > **Deploy base model** to open the deployment window. 
+1. Search for and select the `gpt-4o-mini-realtime-preview` model and then select **Confirm**.
+1. Review the deployment details and select **Deploy**.
 1. Follow the wizard to finish deploying the model.
 
-Now that you have a deployment of the `gpt-4o-mini-realtime-preview` model, you can interact with it in real time in the Azure AI Foundry portal **Real-time audio** playground or Realtime API.
+Now that you have a deployment of the `gpt-4o-mini-realtime-preview` model, you can interact with it in the Azure AI Foundry portal **Audio** playground or Realtime API.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムモデルデプロイ手順の更新"
}
```

### Explanation
この変更は、「realtime-deploy-model.md」ファイルにおけるリアルタイムモデルのデプロイ手順の更新を示しています。合計で12の変更が行われ、6行が新しく追加され、6行が削除されました。変更内容は、Azure AI Foundryポータルでの手順の具体的な部分を更新し、最新のインターフェースに合わせた形になっています。

新しい手順では、アプリケーションのナビゲーションやモデルデプロイの際のオプションを再構成しており、より直感的で簡単に理解できるようになっています。具体的には、モデルをデプロイするためのページへのアクセス方法や、デプロイメントプロセスの各ステップが明確化され、ユーザーが採用すべき流れがより分かりやすくなっています。

最終的に、ユーザーはリアルタイムオーディオプレイグラウンドまたはリアルタイムAPIを通じて、`gpt-4o-mini-realtime-preview`モデルとインタラクションすることができることを強調する内容も更新されています。この手順の修正によって、ユーザーエクスペリエンスが向上し、モデルのデプロイが一層容易になっています。

## articles/ai-services/openai/includes/realtime-portal.md{#item-1b81a2}

<details>
<summary>Diff</summary>
````diff
@@ -15,17 +15,18 @@ ms.date: 3/20/2025
 
 To chat with your deployed `gpt-4o-mini-realtime-preview` model in the [Azure AI Foundry](https://ai.azure.com) **Real-time audio** playground, follow these steps:
 
-1. Go to the [Azure OpenAI in Azure AI Foundry Models page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI in Azure AI Foundry Models resource and the deployed `gpt-4o-mini-realtime-preview` model.
-1. Select the **Real-time audio** playground from under **Playgrounds** in the left pane.
-1. Select your deployed `gpt-4o-mini-realtime-preview` model from the **Deployment** dropdown. 
-1. Select **Enable microphone** to allow the browser to access your microphone. If you already granted permission, you can skip this step.
+1. Go to the [Azure AI Foundry portal](https://ai.azure.com) and select your project that has your deployed `gpt-4o-mini-realtime-preview` model.
+1. Select **Playgrounds** from the left pane.
+1. Select **Audio playground** > **Try the Audio playground**. 
 
-    :::image type="content" source="../media/how-to/real-time/real-time-playground.png" alt-text="Screenshot of the real-time audio playground with the deployed model selected." lightbox="../media/how-to/real-time/real-time-playground.png":::
+    > [!NOTE]
+    > The **Chat playground** doesn't support the `gpt-4o-mini-realtime-preview` model. Use the **Audio playground** as described in this section.
+
+1. Select your deployed `gpt-4o-mini-realtime-preview` model from the **Deployment** dropdown.
+
+    :::image type="content" source="../media/how-to/real-time/real-time-playground.png" alt-text="Screenshot of the audio playground with the deployed model selected." lightbox="../media/how-to/real-time/real-time-playground.png":::
 
 1. Optionally, you can edit contents in the **Give the model instructions and context** text box. Give the model instructions about how it should behave and any context it should reference when generating a response. You can describe the assistant's personality, tell it what it should and shouldn't answer, and tell it how to format responses.
 1. Optionally, change settings such as threshold, prefix padding, and silence duration.
 1. Select **Start listening** to start the session. You can speak into the microphone to start a chat.
-
-    :::image type="content" source="../media/how-to/real-time/real-time-playground-start-listening.png" alt-text="Screenshot of the real-time audio playground with the start listening button and microphone access enabled." lightbox="../media/how-to/real-time/real-time-playground-start-listening.png":::
-
 1. You can interrupt the chat at any time by speaking. You can end the chat by selecting the **Stop listening** button.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムポータルの使用手順の改善"
}
```

### Explanation
この変更は、「realtime-portal.md」ファイルにおけるリアルタイムポータルでのモデル使用手順の改善を示しています。合計で17の変更が行われ、9行が追加され、8行が削除されました。変更内容は、ユーザーが`gpt-4o-mini-realtime-preview`モデルを使用してリアルタイムオーディオプレイグラウンドでチャットするための手順を最新のインターフェースに合わせて更新しています。

手順の具体的な変更点として、Azure AI Foundryポータル内のナビゲーションの改善が見られます。ユーザーがプロジェクトを選択するプロセスや、「オーディオプレイグラウンド」に軸を置いた新しい指示が追加されました。また、`gpt-4o-mini-realtime-preview`モデルを使用する際、「チャットプレイグラウンド」ではなく「オーディオプレイグラウンド」に移動するように指示しています。

これにより、ユーザーはよりスムーズにインターフェースを利用できるようになり、必要なモードで適切な手順を踏むことができるため、全体的なエクスペリエンスが向上しています。また、手順中に画像を挿入することで、視覚的な補助も加わり、理解しやすい内容になっています。

## articles/ai-services/openai/includes/text-to-speech-rest.md{#item-d067a1}

<details>
<summary>Diff</summary>
````diff
@@ -73,7 +73,7 @@ echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/envi
 In a bash shell, run the following command. You need to replace `YourDeploymentName` with the deployment name you chose when you deployed the text to speech model. The deployment name isn't necessarily the same as the model name. Entering the model name results in an error unless you chose a deployment name that is identical to the underlying model name.
 
 ```bash
-curl $AZURE_OPENAI_ENDPOINT/openai/deployments/YourDeploymentName/audio/speech?api-version=2024-02-15-preview \
+curl $AZURE_OPENAI_ENDPOINT/openai/deployments/YourDeploymentName/audio/speech?api-version=2025-04-01-preview \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
@@ -83,7 +83,7 @@ curl $AZURE_OPENAI_ENDPOINT/openai/deployments/YourDeploymentName/audio/speech?a
 }' --output speech.mp3
 ```
 
-The format of your first line of the command with an example endpoint would appear as follows curl `https://aoai-docs.openai.azure.com/openai/deployments/{YourDeploymentName}/audio/speech?api-version=2024-02-15-preview \`. 
+The format of your first line of the command with an example endpoint would appear as follows curl `https://aoai-docs.openai.azure.com/openai/deployments/{YourDeploymentName}/audio/speech?api-version=2025-04-01-preview \`. 
 
 > [!IMPORTANT]
 > For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see this [security](../../security-features.md) article.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト音声合成APIのバージョン更新"
}
```

### Explanation
この変更は、「text-to-speech-rest.md」ファイルにおけるテキスト音声合成APIの使用に関するコマンドのバージョンを更新したことを示しています。具体的には、APIのバージョンが「2024-02-15-preview」から「2025-04-01-preview」に変更されており、合計で4つの変更が行われています。2行が追加され、2行が削除されました。

具体的には、`curl`コマンドの一部が変更され、適切なAPIバージョンに合わせて修正されています。この変更により、ユーザーが最新のAPIを利用できるようにし、新しいバージョンによる機能や修正を反映させています。また、コマンドの最初の行に示されたエンドポイントも更新され、新しいバージョンに適した記述となっています。

この変更は、ユーザーがテキストを音声に変換するプロセスを進める際に、正しいAPIバージョンを使用するために重要です。さらに、セキュリティに関する注意喚起も含まれており、Azure Key Vaultの使用を推奨しています。全体として、ドキュメントが最新の情報を反映していることにより、ユーザーエクスペリエンスが向上しています。

## articles/ai-services/openai/includes/text-to-speech-typescript.md{#item-1335d5}

<details>
<summary>Diff</summary>
````diff
@@ -86,7 +86,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     
     // Required Azure OpenAI deployment name and API version
     const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "tts";
-    const apiVersion = process.env.OPENAI_API_VERSION || "2024-08-01-preview";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2025-04-01-preview";
 
     // keyless authentication    
     const credential = new DefaultAzureCredential();
@@ -184,7 +184,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     
     // Required Azure OpenAI deployment name and API version
     const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "tts";
-    const apiVersion = process.env.OPENAI_API_VERSION || "2024-08-01-preview";
+    const apiVersion = process.env.OPENAI_API_VERSION || "2025-04-01-preview";
     
     function getClient(): AzureOpenAI {
       return new AzureOpenAI({
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト音声合成APIのTypeScriptサンプルのバージョン更新"
}
```

### Explanation
この変更は、「text-to-speech-typescript.md」ファイルにおけるテキスト音声合成APIのTypeScriptサンプルコードで、APIバージョンが「2024-08-01-preview」から「2025-04-01-preview」に更新されたことを示しています。全体で4つの変更が加えられ、2行が追加され、2行が削除されています。

具体的には、APIを使用する際に必要とされるパラメータの一つである`apiVersion`が新しいバージョンに更新されており、これによりユーザーは最新の機能や修正を反映したAPIを利用することができます。また、管理された認証情報を使用してAzure OpenAIサービスにアクセスするための設定方法も引き続き提示されています。

この修正により、ユーザーはTypeScriptを使用して最新のAPI仕様に対応したアプリケーションを構築しやすくなり、正しいAPIバージョンを示すことでエラーの発生を防ぐ助けとなります。全体として、ドキュメントが時代に即した情報を提供していることが強調されています。

## articles/ai-services/openai/media/how-to/real-time/real-time-playground-start-listening.png{#item-076ae4}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "リアルタイムプレイグラウンド画像の削除"
}
```

### Explanation
この変更は、「real-time-playground-start-listening.png」ファイルが削除されたことを示しています。これにより、リアルタイムプレイグラウンドに関するリソースから重要な画像が失われることになります。今回の変更には行数の追加や削除はなく、まさに対象ファイルの削除のみが行われています。

この画像は、ユーザーがリアルタイムプレイグラウンドを使用開始する方法に関する情報を視覚的に提供していた可能性がありますが、その削除により、ドキュメントの参照先が一部欠ける形となります。この変更は、ユーザーが関連する手順や情報を理解するために影響を及ぼす可能性があるため、注意が必要です。利用者には、他のリソースを参照することが推奨されます。

## articles/ai-services/openai/media/how-to/real-time/real-time-playground.png{#item-a36b1d}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムプレイグラウンド画像の更新"
}
```

### Explanation
この変更は、「real-time-playground.png」ファイルに関するもので、ファイル自体に対する実質的な変更（追加や削除）はありませんが、ファイルが更新されたことを示しています。この画像は、リアルタイムプレイグラウンドに関するビジュアルコンテンツを提供しており、最新のコンテンツや表現が反映されている可能性があります。

場合によっては、画像が修正されたり、解像度が向上したり、あるいは他の視覚的改善が行われているかもしれません。ユーザーはこの更新によって、より鮮明で正確な情報を得ることができるでしょう。また、ドキュメント内容の整合性を保つためにも、画像の更新は重要です。

この変更は、ユーザー体験を向上させる目的があり、リアルタイムプレイグラウンドの適切な使用法を視覚的に理解するために役立ちます。

## articles/ai-services/openai/realtime-audio-quickstart.md{#item-727df8}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use GPT-4o Realtime API for speech and audio with Azur
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 3/20/2025
+ms.date: 5/23/2025
 author: eric-urban
 ms.author: eur
 ms.custom: references_regions, ignite-2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオクイックスタートの更新"
}
```

### Explanation
この変更は、「realtime-audio-quickstart.md」ドキュメントの内容に対するもので、具体的にはドキュメント内の日付が更新されました。変更内容は、1行の削除と1行の追加があり、合計で2つの変更が行われています。

具体的には、旧日付「3/20/2025」が新日付「5/23/2025」に変更されています。このような日付の更新は、ドキュメントが最新の情報を反映していることを確保するために重要です。特に技術文書においては、正確な日付は非常に価値があり、ユーザーが情報の新しさや関連性を評価するための指標となります。

この変更により、ユーザーは最新の指示や情報をもとに作業を進められるため、リアルタイムオーディオ機能の利用に際してより信頼性のあるガイダンスを得ることができます。

## articles/ai-services/openai/text-to-speech-quickstart.md{#item-c344ad}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Use the Azure OpenAI for text to speech with OpenAI voices.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: quickstart
-ms.date: 3/10/2025
+ms.date: 5/23/2025
 ms.reviewer: eur
 ms.author: eur
 author: eric-urban
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキストから音声へのクイックスタートの更新"
}
```

### Explanation
この変更は、「text-to-speech-quickstart.md」ドキュメントにおいて、一部の情報が更新されたことを示しています。主に、ドキュメント内の日付が「3/10/2025」から「5/23/2025」に変更されており、これにより、文書の内容が最新の情報を反映していることが保証されています。変更の内容は、1行の削除と1行の追加があり、合計で2つの変更となっています。

日付の更新は、ユーザーがこのドキュメントが新しいものであるかどうかを判断する際に重要です。特に技術的な文書においては、正確な日付表示が必要であり、最新のガイダンスや手順に基づいて作業することが求められます。この更新により、ユーザーはAzure OpenAIを使用したテキストから音声への変換に関する最新の情報を活用できるようになり、より効率的にサービスを利用することができるでしょう。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -294,8 +294,6 @@ items:
           href: ./how-to/spillover-traffic-management.md
         - name: Azure OpenAI PTU updates
           href: ./concepts/provisioned-migration.md
-        - name: Azure OpenAI PTU in Azure Government
-          href: ./concepts/gov-provisioned.md
       - name: Plan and manage costs
         href: ./how-to/manage-costs.md
       - name: Performance & latency
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次ファイルの更新"
}
```

### Explanation
この変更は、「toc.yml」ファイルに対するものであり、主に目次に関連する情報が更新されています。具体的には、2つの項目が削除されており、これにより目次が整理されています。変更内容は、合計で2行の削除があり、内容の簡略化が図られています。

削除された項目は「Azure OpenAI PTU in Azure Government」に関するものであり、これによりこのテーマに関連するリソースリンクが目次から外されています。このような変更は、目次を最新の状態に保ち、ユーザーがリソースを見つけやすくするために行われます。

この更新により、ユーザーは関連性のある情報にアクセスしやすくなり、Azure OpenAIの利用においてより効果的にナビゲートできるようになるでしょう。また、不要な情報が排除されることで、ドキュメントの明確さが向上します。

## articles/ai-services/openai/whisper-quickstart.md{#item-4cae3d}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: devx-track-python
 ms.topic: quickstart
-ms.date: 3/10/2025
+ms.date: 5/23/2025
 ms.reviewer: eur
 ms.author: eur
 author: eric-urban
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisperクイックスタートの更新"
}
```

### Explanation
この変更は、「whisper-quickstart.md」ドキュメントにおいて、日付が更新されたことを示しています。具体的には、日付が「3/10/2025」から「5/23/2025」に変更され、これによって文書がより新しい情報を反映していることが確認できます。この変更は、ユーザーが最新のリソースを使用しているかどうかを判断する際に重要です。

更新された日付により、ユーザーはこの手順が常に最新のガイドラインに基づいていることを認識できるため、信頼性が向上します。特に技術文書においては、タイムリーな情報が肝心であり、ユーザーが最新の機能や手順に基づいて作業する場合に重要な要素となります。この変更により、Azure OpenAIのWhisper機能に関する最新の情報を容易に得ることができるようになります。


