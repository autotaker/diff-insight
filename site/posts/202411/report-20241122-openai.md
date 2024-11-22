---
date: '2024-11-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f59daa8...MicrosoftDocs:567d1b1
summary: このコード差分は、Azure OpenAI サービスに関連する文書を2024年のIgniteイベントに合わせて小規模に更新したものです。主に、複数の文書のメタデータフィールドに`ignite-2024`を追加し、イベントとの関連性を強化しています。新機能はないものの、文書は最新の情報に対応し、ユーザーが関連情報を見つけやすくなっています。破壊的変更はなく、文書全体の可読性向上のためにフォーマット調整も行われています。この更新により、ユーザーが最新の技術やイベント情報にアクセスしやすくなっています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f59daa8...MicrosoftDocs:567d1b1){target="_blank"}

# ハイライト
このコード差分は、Azure OpenAI サービスに関連する複数の文書について、2024年のIgniteイベントを意識した小規模な更新を行っています。具体的には、複数の文書におけるメタデータフィールド（主に`ms.custom`フィールド）に`ignite-2024`を追加し、イベントとの関連性を高めています。これにより、文書は最新の情報に調整され、ユーザーがイベントに関連する情報をより簡単に見つけられるようになります。

## 新機能
特に新機能が追加されたわけではありませんが、文書が最新のイベント情報に対応するように更新されました。

## 破壊的変更
破壊的な変更はありません。全ての文書更新は小規模なものであり、それによってこれまでの内容が読めなくなることはありません。

## その他の更新
文書全体の可読性や整合性を保つために、フォーマット調整や余分な空白や改行の削除が行われています。

# 洞察
この更新は、ドキュメントの「見つけやすさ」と「関連性」を向上させる目的があります。特に`ignite-2024`というラベルは、2024年のIgniteイベントの関連情報をユーザーに即時に認識させる手法として有効です。イベントに関連付けられたラベルやメタデータの追加は、普遍的かつシンプルな方法論として、継続的なドキュメント管理や改善で重要な役割を果たします。

また、各文書における細かなフォーマット調整（例: 余分な空白の削除や改行の統一）は、文書の品質を向上させる一側面です。こういった細やかな調整は、文書全体の可読性を高め、ユーザーが必要とする情報を素早く取得できる環境を提供します。

このようにして、Azure OpenAI サービスに関する文書は継続的に最新の情報と結びつけられ、ユーザーが最新の技術ならびにイベント情報と常に接触できるように維持されていると言えます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [abuse-monitoring.md](#item-b7afcb) | minor update | Azure OpenAI サービスの不正利用監視機能に関する更新 | modified | 2 | 2 | 4 | 
| [provisioned-migration.md](#item-68e143) | minor update | プロビジョニングされた移行に関するドキュメント更新 | modified | 2 | 3 | 5 | 
| [use-your-data.md](#item-455d6e) | minor update | データ利用に関するドキュメントの更新 | modified | 1 | 1 | 2 | 
| [weights-and-biases-integration.md](#item-8ae868) | minor update | Weights & Biases統合に関するドキュメントの更新 | modified | 3 | 2 | 5 | 
| [assistants-ai-studio.md](#item-1632e2) | minor update | AI Studioアシスタントに関するドキュメントの更新 | modified | 1 | 0 | 1 | 
| [connect-your-data-studio.md](#item-c34da8) | minor update | データスタジオ接続に関するドキュメントの更新 | modified | 2 | 0 | 2 | 
| [gpt-v-studio.md](#item-dcd50e) | minor update | GPT-4 Turbo with Visionに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [use-your-data-studio.md](#item-705daf) | minor update | データスタジオの使用に関するドキュメントの更新 | modified | 2 | 1 | 3 | 
| [realtime-audio-quickstart.md](#item-727df8) | minor update | リアルタイムオーディオに関するクイックスタートガイドの更新 | modified | 1 | 1 | 2 | 
| [mongo-db.md](#item-7516e1) | minor update | MongoDBに関するリファレンス文書の更新 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-53303b) | minor update | 新機能の更新情報にignite-2024を追加 | modified | 1 | 0 | 1 | 


# Modified Contents
## articles/ai-services/openai/concepts/abuse-monitoring.md{#item-b7afcb}

<details>
<summary>Diff</summary>
````diff
@@ -5,9 +5,9 @@ description: Learn about the abuse monitoring capabilities of Azure OpenAI Servi
 author: mrbullwinkle
 ms.author: mbullwin
 ms.service: azure-ai-openai
-ms.topic: conceptual 
+ms.topic: conceptual
 ms.date: 09/20/2024
-ms.custom: template-concept
+ms.custom: template-concept, ignite-2024
 manager: nitinme
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI サービスの不正利用監視機能に関する更新"
}
```

### Explanation
このコードの変更は、Azure OpenAI サービスの不正利用監視に関する文書の小規模な更新です。具体的には、`ms.topic` と `ms.custom` のメタデータフィールドに変更が加えられました。`ms.topic` フィールドは形式が整えられ、空白が削除されました。また、`ms.custom` フィールドには新たに `ignite-2024` が追加され、文書が Ignite 2024 に関連することを示しています。この修正により、文書の整合性と情報の最新性が向上しています。

## articles/ai-services/openai/concepts/provisioned-migration.md{#item-68e143}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,8 @@ titleSuffix: Azure OpenAI
 description: Learn about the improvements to Provisioned Throughput
 manager: nitinme
 ms.service: azure-ai-openai
-ms.custom: 
+ms.custom:
+  - ignite-2024
 ms.topic: how-to
 ms.date: 11/11/2024
 author: mrbullwinkle
@@ -357,5 +358,3 @@ The same approaches apply in moving the commitment and deployment within the reg
 ### View and edit an existing resource
 
 In Azure OpenAI Studio, select **Quota** > **Provisioned** > **Manage commitments** and select a resource with an existing commitment to view/change it. 
-
-
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされた移行に関するドキュメント更新"
}
```

### Explanation
この変更は、Azure OpenAI サービスの「プロビジョニングされた移行」に関する文書に対する小規模な更新です。主な変更点として、`ms.custom` フィールドに新たに `ignite-2024` が追加され、文書が Ignite 2024 に関連することを示しています。また、文書の一部の空白行が削除され、全体的なフォーマットが整理されました。この修正により、文書の可読性と情報の関連性が向上しています。

## articles/ai-services/openai/concepts/use-your-data.md{#item-455d6e}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ author: aahill
 ms.author: aahi
 ms.date: 10/25/2024
 recommendations: false
-ms.custom: references_regions 
+ms.custom: references_regions, ignite-2024
 ---
 
 # Azure OpenAI On Your Data 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ利用に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAI サービスにおける「データ利用」に関する文書に対する小規模な更新です。具体的には、`ms.custom` フィールドに `ignite-2024` が追加され、文書が Ignite 2024 に関連することを示しています。この修正は、文書の関連性を高めるとともに、情報の整理を促進しました。全体的に、文書はより明確に最新の情報を反映しています。

## articles/ai-services/openai/how-to/weights-and-biases-integration.md{#item-8ae868}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,8 @@ titleSuffix: Azure OpenAI
 description: Learn how to integrate Weights & Biases and Azure OpenAI fine-tuning.
 manager: nitinme
 ms.service: azure-ai-openai
-ms.custom: 
+ms.custom:
+  - ignite-2024
 ms.topic: how-to
 ms.date: 11/10/2024
 author: mrbullwinkle
@@ -96,4 +97,4 @@ Give your Azure OpenAI resource the **Key Vault Secrets Officer** role.
 
 3. Now when you create new fine-tuning jobs you'll have the option to log data from the job to your Weights & Biases account.
 
-    :::image type="content" source="../media/how-to/weights-and-biases/dashboards.png" alt-text="Screenshot of the weights and biases dashboards." lightbox="../media/how-to/weights-and-biases/dashboards.png":::
\ No newline at end of file
+    :::image type="content" source="../media/how-to/weights-and-biases/dashboards.png" alt-text="Screenshot of the weights and biases dashboards." lightbox="../media/how-to/weights-and-biases/dashboards.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Weights & Biases統合に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAI サービスにおける「Weights & Biases統合」に関する文書の小規模な更新を示しています。具体的には、`ms.custom` フィールドに `ignite-2024` が追加され、文書が Ignite 2024 に関連付けられました。また、内容の一部が整理され、特に画像の記述における無駄な改行が削除されています。この修正により、文書の構造がより明確になり、関連情報が強調されることで、ユーザーにとっての利用価値が向上しています。

## articles/ai-services/openai/includes/assistants-ai-studio.md{#item-1632e2}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 ms.service: azure-ai-studio
 ms.custom:
   - build-2024
+  - ignite-2024
 ms.topic: include
 ms.date: 03/04/2024
 ms.author: mbullwin
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Studioアシスタントに関するドキュメントの更新"
}
```

### Explanation
この変更は、AI Studio に関連するアシスタントのドキュメントに対する小規模な更新です。具体的には、`ms.custom` フィールドに `ignite-2024` が追加され、文書が Ignite 2024 に関連付けられました。この修正は、関連するイベントに対して文書の明確な視認性を高めることを目的としており、ユーザーにとっての情報の有用性を向上させることが期待されます。文書の整合性と最新の関連情報を反映するための重要なステップとなっています。

## articles/ai-services/openai/includes/connect-your-data-studio.md{#item-c34da8}

<details>
<summary>Diff</summary>
````diff
@@ -3,6 +3,8 @@ titleSuffix: Azure OpenAI
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
+ms.custom:
+  - ignite-2024
 ms.topic: include
 author: aahill
 ms.author: aahi
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データスタジオ接続に関するドキュメントの更新"
}
```

### Explanation
この変更は、「データスタジオとの接続」に関する文書の小規模な更新を示しています。具体的には、`ms.custom` フィールドに `ignite-2024` が追加され、文書が Ignite 2024 に関連付けられました。この修正により、関連情報が強調され、ユーザーが最新のイベントに基づいた情報を取得しやすくなります。文書の整合性と関連情報の明確化を図る重要な変更です。

## articles/ai-services/openai/includes/gpt-v-studio.md{#item-dcd50e}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,12 @@
 ---
 title: 'Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the Azure OpenAI Service'
 titleSuffix: Azure OpenAI
-description: Use this article to get started using Azure AI Studio to deploy and use the GPT-4 Turbo with Vision model.  
+description: Use this article to get started using Azure AI Studio to deploy and use the GPT-4 Turbo with Vision model.
 services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.custom: references_regions
+ms.custom: references_regions, ignite-2024
 ms.date: 10/03/2024
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turbo with Visionに関するドキュメントの更新"
}
```

### Explanation
この変更は、GPT-4 Turbo with Vision に関するドキュメントの内容を小規模に更新したものです。具体的には、`description` 行の末尾の余分な空白が削除され、`ms.custom` フィールドに `ignite-2024` が追加されました。この修正により、文書が Ignite 2024 に関連付けられ、コンテンツがより整然とした形で提供されるようになります。結果として、ユーザーはこの技術に関する最新の情報を理解しやすくなることが期待されます。

## articles/ai-services/openai/includes/use-your-data-studio.md{#item-705daf}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,8 @@ description: Use this article to import and use your data in Azure OpenAI.
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
+ms.custom:
+  - ignite-2024
 ms.topic: quickstart
 author: aahill
 ms.author: aahi
@@ -39,4 +41,3 @@ Queries that require data analysis would probably fail, such as "*Which health p
 Chats are constrained by the number of documents (chunks) returned in the response (limited to 3-20 in Azure OpenAI Studio playground). As you can imagine, posing a question about "all of the titles" requires a full scan of the entire vector store.
 
 [!INCLUDE [deploy-web-app](deploy-web-app.md)]
-
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データスタジオの使用に関するドキュメントの更新"
}
```

### Explanation
この変更は、「データスタジオの使用」に関する文書の小規模な更新を示しています。主な変更点は、`ms.custom` フィールドに `ignite-2024` が追加されたことです。これにより、文書が Ignite 2024 に関連付けられ、読者が最新のイベントに基づいた情報にアクセスしやすくなります。また、文書の最後から不要な空行が削除され、内容がより整然と表示されるようになりました。この改善により、ユーザーはAzure OpenAIのデータ利用についての情報をより明確に理解できるようになります。

## articles/ai-services/openai/realtime-audio-quickstart.md{#item-727df8}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.topic: how-to
 ms.date: 10/3/2024
 author: eric-urban
 ms.author: eur
-ms.custom: references_regions
+ms.custom: references_regions, ignite-2024
 zone_pivot_groups: openai-studio-js
 recommendations: false
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオに関するクイックスタートガイドの更新"
}
```

### Explanation
この変更は、「リアルタイムオーディオに関するクイックスタートガイド」の内容を小規模に更新したものです。主な変更点は、`ms.custom` フィールドに `ignite-2024` が追加されたことです。これにより、文書が Ignite 2024 に関連付けられ、ユーザーがイベントの関連情報にアクセスしやすくなります。また、`ms.custom` フィールドの内容が若干変更されたこと以外には、大きな構造的な変更はありません。この更新により、Azure OpenAIのリアルタイムオーディオ機能についての情報がより強調されることが期待されます。

## articles/ai-services/openai/references/mongo-db.md{#item-7516e1}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.date: 10/25/2024
 author: aahill
 ms.author: aahi
 recommendations: false
-ms.custom: devx-track-python
+ms.custom: devx-track-python, ignite-2024
 ---
 
 # Data source - Mongo DB Atlas
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MongoDBに関するリファレンス文書の更新"
}
```

### Explanation
この変更は、「MongoDBに関するリファレンス文書」の内容を小規模に更新したものです。主な変更点は、`ms.custom` フィールドに `ignite-2024` が追加されたことです。これにより、文書が Ignite 2024 に関連付けられることで、ユーザーが最新のイベントに関連する情報にアクセスしやすくなります。変更は1つの追加と1つの削除が行われており、全体的な構造には大きな影響を与えない軽微な調整です。この更新によって、MongoDBに関する情報がより明確に整理されることが期待されます。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -9,6 +9,7 @@ ms.service: azure-ai-openai
 ms.custom:
   - ignite-2023
   - references_regions
+  - ignite-2024
 ms.topic: whats-new
 ms.date: 11/12/2024
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能の更新情報にignite-2024を追加"
}
```

### Explanation
この変更は、「新機能」セクションにおける内容の小規模な更新です。具体的には、`ms.custom` フィールドに新たに `ignite-2024` が追加されました。これにより、文書が Ignite 2024 に関連付けられ、ユーザーが最新のイベントや機能に関する情報を見つけやすくなります。その他の部分については削除はなく、全体的な構造の変更はありません。今回の更新は、Azure OpenAI サービスの最新情報を提供する際に重要な役割を果たすことが期待されています。


