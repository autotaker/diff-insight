---
date: '2024-10-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6ee615c...MicrosoftDocs:2061c5e
summary: このレポートでは、AI関連のドキュメントに対する小規模な更新が行われ、新しいタグ「ai-learning-hub」が追加されたことをまとめています。このタグの追加により、Azure
  AI Studioに関連する新しい学習リソースへのアクセスと認識が向上しました。また、破滅的な変更はなく、一部のリンク構造が改善されました。これらの変更は、ユーザーが必要な情報をより迅速に見つけられるようにするためのもので、特に新規ユーザーにとっての学習を容易にします。全体として、ユーザーエクスペリエンスの向上に寄与する重要なアップデートです。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6ee615c...MicrosoftDocs:2061c5e){target="_blank"}

# ハイライト

各種のAI関連ドキュメントに対する小規模な更新が行われ、新しいタグ「ai-learning-hub」が追加されました。これにより、AIリソースへのアクセスと認識が向上します。

## 新機能
- 「ai-learning-hub」というタグが特定のドキュメントに追加され、Azure AI Studio関連の新しい学習リソースが利用可能になりました。

## 破滅的変更
- 破滅的な変更はありません。

## その他の更新
- 一部のリンク構造が修正され、より整然とした形式で表示されるように改善されました。

# インサイト

このコードの変更は、Azure AI Studio関連のドキュメントにおいて新たに「AI Learning Hub」への参照を追加することで、リソースの可視性とナビゲーションの改善を図っています。具体的には、ドキュメント全体に`ms.custom`セクションを用いて、AI Learning Hubという一貫したタグが導入されました。このアプローチにより、ユーザーはAI関連の追加リソースや参考情報をより素早く見つけることができます。

変更は主にタグの追加という小さなものであるため、他のコンテンツや既存の構造に大きな影響を与えていません。しかし、この`ai-learning-hub`タグの導入によって、リソースの探索が効率化されており、AIに新たに触れるユーザーにとってもアクセスしやすいものになっています。こうした小さなアップデートは、ユーザーエクスペリエンスの向上と情報提供の最適化に寄与するものであり、今後のAzure AI Studioの利用を支える基盤となるでしょう。

一部のドキュメントではリンク構造の調整も行われており、これも情報の整合性を保つための重要な取り組みです。リンクが適切に機能することで、ユーザーは必要な情報や追加の資料に迅速にアクセスでき、学習曲線が緩和されます。これは特にAI関連の学習リソースが豊富であるAzure AI Studioにおいては、大きな利点となるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [ai-resources.md](#item-14adb9) | minor update | AI Learning Hubの追加 | modified | 1 | 0 | 1 | 
| [deploy-models-llama.md](#item-6274a7) | minor update | AI Learning Hubの追加とリンクの修正 | modified | 2 | 2 | 4 | 
| [deploy-models-openai.md](#item-de796b) | minor update | AI Learning Hubの追加 | modified | 1 | 0 | 1 | 
| [model-benchmarks.md](#item-82de8e) | minor update | AI Learning Hubの追加 | modified | 1 | 0 | 1 | 
| [model-catalog-overview.md](#item-278001) | minor update | AI Learning Hubの追加 | modified | 1 | 0 | 1 | 


# Modified Contents
## articles/ai-studio/concepts/ai-resources.md{#item-14adb9}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.service: azure-ai-studio
 ms.custom:
   - ignite-2023
   - build-2024
+  - ai-learning-hub
 ms.topic: conceptual
 ms.date: 06/24/2024
 ms.reviewer: deeikele
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Learning Hubの追加"
}
```

### Explanation
この変更は、`ai-resources.md`というファイルに対して小規模な更新を行い、新しい項目「ai-learning-hub」を追加しました。この追加は、マークアップの一部として、Azure AI Studioの関連リソースに対するタグのリストに加えられています。具体的には、次のような形式で行われました：

```diff
+  - ai-learning-hub
```

この変更により、AI Learning Hubの情報がさらに強調され、AIに関連するリソースの認識が向上することが期待されます。ファイル全体に対する変更は1行のみであり、他のコンテンツには影響を与えていません。この更新は、より良いリソースのナビゲーションを提供するためのものです。

## articles/ai-studio/how-to/deploy-models-llama.md{#item-6274a7}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.reviewer: shubhiraj
 reviewer: shubhirajMsft
 ms.author: ssalgado
 author: ssalgadodev
-ms.custom: references_regions, generated
+ms.custom: references_regions, generated, ai-learning-hub
 zone_pivot_groups: azure-ai-model-catalog-samples-chat
 ---
 
@@ -1488,4 +1488,4 @@ It is a good practice to start with a low number of instances and scale up as ne
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Learning Hubの追加とリンクの修正"
}
```

### Explanation
この変更は、`deploy-models-llama.md`というファイルに対する小規模な更新を行いました。具体的には、いくつかの修正が加えられています。まず、`ms.custom`の項目に「ai-learning-hub」が追加され、AI関連のリソースがさらに強調されています。これにより、AI Learning Hubへの参照が強化され、ユーザーが追加のリソースを簡単に見つけられるようになります。

また、文書の最後の方では、コスト管理に関連するリンクを修正し、新しい行が追加されています。この部分においては、リスト項目の形式が調整され、整然とした表示が維持されています。全体として、これらの変更は情報の整理とアクセシビリティの向上を目指したものです。

## articles/ai-studio/how-to/deploy-models-openai.md{#item-de796b}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.service: azure-ai-studio
 ms.custom:
   - ignite-2023
   - build-2024
+  - ai-learning-hub
 ms.topic: how-to
 ms.date: 5/21/2024
 ms.reviewer: fasantia
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Learning Hubの追加"
}
```

### Explanation
この変更は、`deploy-models-openai.md`というファイルに対する小規模な更新を行い、新しい項目「ai-learning-hub」を追加しました。この追加は、Azure AI Studioに関連するリソースのタグ一覧に加えられたもので、ユーザーがAI Learning Hubへの参照を見つけやすくすることを目的としています。

具体的には、`ms.custom`セクションに次のような行が追加されました：

```diff
+  - ai-learning-hub
```

この変更により、AI Learning Hubが強調され、AIに関するリソースを探索する際の指標として機能することが期待されます。ファイルの他の部分には影響を与えておらず、情報が整理されている状態を保っています。この更新は、AI関連のリソースの可視性を向上させるためのものです。

## articles/ai-studio/how-to/model-benchmarks.md{#item-82de8e}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: scottpolly
 ms.service: azure-ai-studio
 ms.custom:
   - build-2024
+  - ai-learning-hub
 ms.topic: how-to
 ms.date: 5/21/2024
 ms.reviewer: jcioffi
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Learning Hubの追加"
}
```

### Explanation
この変更は、`model-benchmarks.md`というファイルに対して小規模な更新を行い、新たに「ai-learning-hub」という項目を追加しました。この変更は、マークダウンファイルの`ms.custom`セクションに加えられ、現在のタグリストにAI Learning Hubを含めることで、関連情報へのアクセスを向上させることを目的としています。

具体的には、以下の行が追加されました：

```diff
+  - ai-learning-hub
```

この追加により、ユーザーはAI Learning Hubに関するリソースを探しやすくなり、Azure AI Studioの利用体験がより充実することが期待されます。また、他の部分には変更がなく、全体の整合性は保たれています。この小さな更新は、リソースの可視性を高めるための重要なステップとなります。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.service: azure-ai-studio
 ms.custom:
   - ignite-2023
   - build-2024
+  - ai-learning-hub
 ms.topic: how-to
 ms.date: 5/21/2024
 ms.reviewer: jcioffi
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Learning Hubの追加"
}
```

### Explanation
この変更は、`model-catalog-overview.md`ファイルに対する小規模な更新を行い、「ai-learning-hub」という新しい項目を`ms.custom`セクションに追加しました。この追加により、Azure AI Studioのリソースの関連性が向上し、AI Learning Hubに関する情報を利用しやすくすることを目指しています。

具体的には、以下の行が追加されました：

```diff
+  - ai-learning-hub
```

この更新によって、ユーザーはAI Learning Hubのリソースをより簡単に見つけることができ、関連情報にアクセスしやすくなります。全体としては、他の情報には影響を与えず、一貫性を保ちながら重要な新情報が提供されています。このような小さな変更は、ユーザーエクスペリエンスを向上させるための重要なステップです。


