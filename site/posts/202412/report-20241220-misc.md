---
date: '2024-12-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6ebedb4...MicrosoftDocs:53fdfa0
summary: 今回の変更では、主に文書の更新日や手順の追加に関する小規模な更新が行われています。特に、「Copilot SDKを使用してRAGを構築する」チュートリアルにテレメトリログを追加する手順が導入され、利用者はこの機能を理解しやすくなりました。また、「Copilot
  SDKを使用した評価」のチュートリアルでは、前提条件としてテレメトリロギング設定の確認が追加され、準備がしやすくなりました。破壊的な変更はなく、文書の日付が更新され、モデルカードのメタデータも改善されています。これにより、文書の正確性や信頼性が保たれ、ユーザー体験が向上することが期待されます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6ebedb4...MicrosoftDocs:53fdfa0){target="_blank"}

# ハイライト
今回の変更では、主に文書の更新日や手順の追加に関する小規模な更新が行われています。特に注目すべき点は、以下の通りです。

## 新機能
- 「Copilot SDKを使用してRAGを構築する」チュートリアルに、テレメトリログを追加する手順が追加されました。この更新により、利用者はテレメトリロギングの有効化方法を明確に理解できるようになります。
- 「Copilot SDKを使用した評価」のチュートリアルでは、前提条件にテレメトリロギング設定の確認が追加され、利用者が必要な準備を確認しやすくなりました。

## 破壊的変更
- 特に破壊的な変更は行われていません。

## その他の更新
- 各文書の日付が最新の情報を反映するように更新されました。これは、文書の精度と信頼性を保つために重要です。
- モデルカードの画像ファイルに対するメタデータや構造に関する更新が行われていますが、ユーザーへの直接的な影響はありません。

# インサイト
ドキュメントの更新は、その内容の正確性と信頼性を保つための基本的で重要な作業です。特に、日付情報の更新は、ユーザーが文書が最新であることを確認するための指標となります。この一貫した日付の更新を保つことは、長期的に見て、製品やサービスの信頼性を高める重要な要素です。

さらに、テレメトリログの追加など、ユーザー体験を向上させるための新たな手順が追加されていることは、ドキュメントが利用者のニーズに適応していることを示しています。テレメトリロギングのような機能は、問題解決やプロジェクトの最適化に役立つため、ユーザーにとって非常に有益です。

チュートリアルにおける前提条件の明確化や手順の追加により、ユーザーはよりスムーズに学習プロセスを進めることができ、結果的にAI技術の習得や利用が容易になります。このような正確で包括的なドキュメントは、開発者コミュニティにおけるAzure AI Studioの評価向上にもつながります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [concept-model-distillation.md](#item-5d97fa) | minor update | 更新された日付情報: Model Distillation | modified | 1 | 1 | 2 | 
| [concept-synthetic-data.md](#item-2f06f6) | minor update | 更新された日付情報: Synthetic Data | modified | 1 | 1 | 2 | 
| [concept-data-privacy.md](#item-af88ce) | minor update | 更新された日付情報: Data Privacy | modified | 1 | 1 | 2 | 
| [fine-tune-model-llama.md](#item-2a42d8) | minor update | 更新された日付情報: Llamaモデルのファインチューニング | modified | 1 | 1 | 2 | 
| [fine-tune-phi-3.md](#item-5b722a) | minor update | 更新された日付情報: Phi-3モデルのファインチューニング | modified | 1 | 1 | 2 | 
| [index-add.md](#item-1b013b) | minor update | 更新された日付情報: インデックスの追加 | modified | 1 | 1 | 2 | 
| [model-card.png](#item-fb3efb) | minor update | 画像ファイルのメタデータ更新: モデルカード | modified | 0 | 0 | 0 | 
| [copilot-sdk-build-rag.md](#item-b77dba) | minor update | テレメトリログを追加する手順の更新: Copilot SDKチュートリアル | modified | 3 | 1 | 4 | 
| [copilot-sdk-evaluate.md](#item-bb5754) | minor update | テレメトリロギングの確認手順の追加: Copilot SDK評価チュートリアル | modified | 1 | 0 | 1 | 


# Modified Contents
## articles/ai-studio/concepts/concept-model-distillation.md{#item-5d97fa}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to do distillation in Azure AI Foundry portal.
 manager: scottpolly
 ms.service: azure-ai-studio
 ms.topic: how-to
-ms.date: 07/23/2024
+ms.date: 12/15/2024
 ms.reviewer: vkann
 reviewer: anshirga
 ms.author: ssalgado
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新された日付情報: Model Distillation"
}
```

### Explanation
この変更は、Azure AI Studioに関連する文書の中で、モデル蒸留に関するページの日付情報を更新するものです。具体的には、以前の更新日である2024年7月23日から、2024年12月15日に変更されました。このような日付の更新は、ドキュメントの最新性を保ち、読者に正確な情報を提供するために重要です。この変更は、ファイル全体の流れには大きな影響を与えませんが、情報の整合性を確保するために必要なものです。

## articles/ai-studio/concepts/concept-synthetic-data.md{#item-2f06f6}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to generate a synthetic dataset in Azure AI Foundry porta
 manager: scottpolly
 ms.service: azure-ai-studio
 ms.topic: how-to
-ms.date: 07/23/2024
+ms.date: 12/15/2024
 ms.reviewer: vkann
 reviewer: anshirga
 ms.author: ssalgado
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新された日付情報: Synthetic Data"
}
```

### Explanation
この変更は、Azure AI Studioにおける合成データ生成に関する文書の更新を反映しています。具体的には、ドキュメントの日付が2024年7月23日から2024年12月15日に修正されました。この日付更新は、文書が最新の情報を提供し続けるために必要で、読者に対して正確なタイムラインを示すものです。この変更は、全体の内容や構成には影響を与えませんが、文書の整合性を保つために重要です。

## articles/ai-studio/how-to/concept-data-privacy.md{#item-af88ce}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: scottpolly
 ms.service: azure-ai-studio
 ms.custom: references_regions, build-2024
 ms.topic: conceptual
-ms.date: 10/29/2024
+ms.date: 12/19/2024
 ms.reviewer: shubhirajMsft
 ms.author: scottpolly
 author: s-polly
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新された日付情報: Data Privacy"
}
```

### Explanation
この変更は、Azure AI Studioにおけるデータプライバシーに関する文書での日付情報を更新するものです。具体的には、文書の更新日が2024年10月29日から2024年12月19日に変更されました。この日付の変更は、文書が最新の状態であり、読者に対して正確な情報を提供するための重要なステップです。全体のドキュメント構造や内容には影響を与えませんが、情報の整合性を維持するために非常に重要です。

## articles/ai-studio/how-to/fine-tune-model-llama.md{#item-2a42d8}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to fine-tune Meta Llama models in Azure AI Foundry portal
 manager: scottpolly
 ms.service: azure-ai-studio
 ms.topic: how-to
-ms.date: 7/23/2024
+ms.date: 12/16/2024
 ms.reviewer: rasavage
 reviewer: shubhirajMsft
 ms.author: ssalgado
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新された日付情報: Llamaモデルのファインチューニング"
}
```

### Explanation
この変更は、Azure AI StudioにおけるMeta Llamaモデルのファインチューニングに関する文書に対する日付の更新を含んでいます。具体的には、文書の日付が2024年7月23日から2024年12月16日に変更されました。このような日付更新は、文書が最新の情報を保持するのに重要で、読者に適切なタイミングでの情報提供を行うためのものです。内容自体には変更がないため、文書の整合性と信頼性を確保することを目的としています。

## articles/ai-studio/how-to/fine-tune-phi-3.md{#item-5b722a}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: scottpolly
 ms.service: azure-ai-studio
 ms.custom:
 ms.topic: how-to
-ms.date: 7/16/2024
+ms.date: 12/16/2024
 ms.author: ssalgado
 author: ssalgadodev
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新された日付情報: Phi-3モデルのファインチューニング"
}
```

### Explanation
この変更は、Azure AI StudioにおけるPhi-3モデルのファインチューニングに関する文書での日付情報を更新するものです。具体的には、文書の日付が2024年7月16日から2024年12月16日に変更されました。この更新は、文書が最新の情報を反映することを目的としており、読者にとって正確で信頼できる情報源となるようにします。内容の他の部分に変更はなく、日付の更新によって文書の整合性を維持するための重要な措置です。

## articles/ai-studio/how-to/index-add.md{#item-1b013b}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 12/11/2024
 ms.reviewer: estraight
 ms.author: ssalgado
 author: ssalgadodev
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新された日付情報: インデックスの追加"
}
```

### Explanation
この変更は、Azure AI Studioにおける「インデックスの追加」に関する文書の日付情報を更新するものです。具体的には、文書の日付が2024年5月21日から2024年12月11日に変更されました。この更新は、内容が最新の状態を反映することを目的としており、読者に対して信頼性のある情報を提供するために重要です。文書の他の内容には変更がないため、主に日付の更新によって文書の整合性と最新情報の保持が図られています。

## articles/ai-studio/media/deploy-monitor/serverless/model-card.png{#item-fb3efb}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルのメタデータ更新: モデルカード"
}
```

### Explanation
この変更は、Azure AI Studioのデプロイと監視に関する「モデルカード」の画像ファイルに関連していますが、実際のファイル内容には変更がありません。変更内容としては、画像のメタデータやプロジェクト構造に関連する要素かもしれませんが、追加や削除は行われていません。この更新は、プロジェクトの整合性や管理のための適切な手続きとして重要です。ユーザーには直接的な影響はありませんが、ファイルの最新の状態を維持するための措置として評価できます。

## articles/ai-studio/tutorials/copilot-sdk-build-rag.md{#item-b77dba}

<details>
<summary>Diff</summary>
````diff
@@ -156,9 +156,11 @@ Now that you have both the script and the template, run the script to test your
 python chat_with_products.py --query "I need a new tent for 4 people, what would you recommend?"
 ```
 
+### <a name="logging"></a> Add telemetry logging
+
 To enable logging of telemetry to your project:
 
-1. Enable tracing by adding an Application Insights resource to your project.  Navigate to the **Tracing** tab in the [Azure AI Foundry portal](https://ai.azure.com/), and create a new resource if you don't already have one.
+1. Add an Application Insights resource to your project.  Navigate to the **Tracing** tab in the [Azure AI Foundry portal](https://ai.azure.com/), and create a new resource if you don't already have one.
 
     :::image type="content" source="../../ai-services/agents/media/ai-foundry-tracing.png" alt-text="A screenshot of the tracing screen in the Azure AI Foundry portal." lightbox="../../ai-services/agents/media/ai-foundry-tracing.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テレメトリログを追加する手順の更新: Copilot SDKチュートリアル"
}
```

### Explanation
この変更は、Azure AI Studioのチュートリアル「Copilot SDKを使用してRAGを構築する」において、テレメトリロギングの設定に関する手順を更新したものです。具体的には、ログのテレメトリを有効にするための手順が増え、記述がわかりやすくなりました。新たに「ログ記録を追加する」というセクションが追加され、1つの手順が文章の整合性を保つために再構成されています。この更新により、ユーザーはテレメトリの設定方法をより明確に理解できるようになり、プロジェクトへの適切なトレーシングを実施できるようになります。全体として、内容が充実し、利用者の利便性が向上しています。

## articles/ai-studio/tutorials/copilot-sdk-evaluate.md{#item-bb5754}

<details>
<summary>Diff</summary>
````diff
@@ -29,6 +29,7 @@ This tutorial is part three of a three-part tutorial.
 ## Prerequisites
 
 - Complete [part 2 of the tutorial series](copilot-sdk-build-rag.md) to build the chat application.
+- Make sure you've completed the steps to [add telemetry logging](copilot-sdk-build-rag.md#logging) from part 2.
 
 
 ## <a name="evaluate"></a> Evaluate the quality of the chat app responses
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テレメトリロギングの確認手順の追加: Copilot SDK評価チュートリアル"
}
```

### Explanation
この変更は、Azure AI Studioのチュートリアル「Copilot SDKを使用した評価」の内容を更新したものです。具体的には、チュートリアルの前提条件セクションに、前のパートである「RAGを構築する」チュートリアルにおいてテレメトリロギングを追加する手順を完了していることを確認するための指示が追加されました。この更新により、ユーザーはこのチュートリアルを実行する際に、必要な準備が整っているかどうかをより明確に把握できるようになります。全体として、チュートリアルの流れがスムーズになり、ユーザーの理解を助ける内容になります。


