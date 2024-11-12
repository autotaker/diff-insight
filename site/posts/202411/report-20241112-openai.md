---
date: '2024-11-12'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6042051...MicrosoftDocs:d63c476
summary: この差分では、Azure OpenAIサービスのドキュメントに対して複数のマイナーアップデートが行われました。主な変更点は、モデル名の変更や計算ロジックの追加、役割ベースのアクセス制御やファインチューニング手順の改善、画像や用語の一貫性向上に関するものです。新機能としてはファインチューニングに関する統一ガイドが追加され、用語やプロセスの変更により、既存のドキュメントに依存しているプロジェクトに影響を与える可能性があります。全体として、これらの更新はユーザビリティと一致性を高め、ユーザーが最新情報に容易にアクセスできるようにすることを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6042051...MicrosoftDocs:d63c476){target="_blank"}

# Highlights
この差分では、Azure OpenAIサービスのドキュメントに対して複数のマイナーアップデートが施されています。変更の焦点は、モデル名の変更、計算ロジックの追加から、役割ベースのアクセス制御やファインチューニング手順の改善、画像や用語の一貫性の向上など多岐にわたります。

## 新機能
- プロジェクトのファインチューニングに関する新しい統一ガイドが追加されました。

## 破壊的変更
- 特に報じられていないが、用語の変更やプロセスの更新があるため、既存のドキュメントに依存しているプロジェクトには影響を与える可能性があります。

## その他の更新
- **モデル名の変更**：「GPT-4o audio」から「GPT-4o-Realtime-Preview」へ変更。
- **計算ロジックの追加**：Provisioned-ManagedおよびGlobal Provisioned-Managed利用状況の計算ロジックの追加。
- **リンクとタイトルの修正**：関連リンクとタイトルの整合性を改善。
- **トークン制限の詳細な説明追加**：埋め込みリクエストでのトークン制限に関する情報を更新。
- **画像の更新**：複数の画像ファイルが更新はされたが、内容に変化はないと思われます。

# Insights
この変更は、Azure OpenAIサービスのユーザビリティと一貫性を向上させるために設計されています。大部分の変更は、ドキュメント内の用語や手続きの一貫性を高めるためのものであり、ユーザーが最新の情報を容易にアクセスできるようにすることが目的です。また、高度なファインチューニングや監視機能を可能にするための新機能とメトリクスの追加が、ユーザーがリソースを効率的に管理するのに役立ちます。

特に、Azure OpenAIサービスとAzure AI Studioの用語が整理され、一貫性が保たれることで、ユーザーが異なるコンテキストで混乱することなくサービスを利用できる環境が整っています。新しいファインチューニングのガイドの追加により、ユーザーはニーズに合わせた適切な手法を選択しやすくなり、プロジェクトのカスタマイズがよりスムーズに進められるでしょう。

全体を通して、これらの更新はAzure OpenAIサービスの利便性とパフォーマンスを向上させる一環として機能し、ドキュメントが常に最新であることを確認する努力の一部です。このように適応性と透明性が強化された結果、ユーザーはこれまで以上に効率的にテクノロジーを活用できるようになることが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | モデル名の変更および説明の更新 | modified | 2 | 2 | 4 | 
| [provisioned-throughput.md](#item-022e0c) | minor update | 利用状況の計算ロジックの追加 | modified | 1 | 0 | 1 | 
| [system-message.md](#item-10456c) | minor update | リンクの更新と削除 | modified | 1 | 1 | 2 | 
| [content-filters.md](#item-6f0627) | minor update | タイトルの修正 | modified | 2 | 2 | 4 | 
| [embeddings.md](#item-e38d07) | minor update | トークン制限に関する説明の更新 | modified | 1 | 1 | 2 | 
| [fine-tuning.md](#item-5c0e85) | minor update | ファインチューニングに関するドキュメントの更新 | modified | 3 | 9 | 12 | 
| [monitor-openai.md](#item-fcba4d) | minor update | 監視に関するドキュメントの軽微な修正 | modified | 0 | 2 | 2 | 
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | プロビジョニングスループットに関する情報の更新 | modified | 5 | 5 | 10 | 
| [role-based-access-control.md](#item-4b9817) | minor update | 役割ベースのアクセス制御に関する情報の更新 | modified | 18 | 18 | 36 | 
| [working-with-models.md](#item-7ec098) | minor update | モデルによる作業に関する情報の更新 | modified | 5 | 5 | 10 | 
| [create-resource-portal.md](#item-cb2503) | minor update | リソースポータルに関する情報の更新 | modified | 2 | 2 | 4 | 
| [fine-tuning-studio.md](#item-439f1e) | minor update | ファインチューニングスタジオに関する情報の更新 | modified | 26 | 27 | 53 | 
| [fine-tuning-unified.md](#item-718336) | new feature | ファインチューニングの統一インクルードガイドの追加 | added | 24 | 0 | 24 | 
| [studio.png](#item-343759) | minor update | コンテンツフィルター画像の更新 | modified | 0 | 0 | 0 | 
| [error.png](#item-b79279) | minor update | エラーメッセージ画像の更新 | modified | 0 | 0 | 0 | 
| [studio-create-custom-model.png](#item-973d92) | minor update | カスタムモデル作成に関する画像の更新 | modified | 0 | 0 | 0 | 
| [update-policy-new.png](#item-c99209) | minor update | モデルの更新ポリシーに関する画像の更新 | modified | 0 | 0 | 0 | 
| [chatgpt-playground-load-new.png](#item-8ad889) | minor update | ChatGPTプレイグラウンドのロードに関する画像の更新 | modified | 0 | 0 | 0 | 
| [playground-load-new.png](#item-9023ae) | minor update | プレイグラウンドのロードに関する画像の更新 | modified | 0 | 0 | 0 | 
| [monitor-openai-reference.md](#item-8d8887) | minor update | OpenAIモニタリングリファレンスのメトリクス更新 | modified | 4 | 0 | 4 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 |--|--|
 | [o1-preview and o1-mini](#o1-preview-and-o1-mini-models-limited-access) | Limited access models, specifically designed to tackle reasoning and problem-solving tasks with increased focus and capability.  |
 | [GPT-4o & GPT-4o mini & GPT-4 Turbo](#gpt-4o-and-gpt-4-turbo) | The latest most capable Azure OpenAI models with multimodal versions, which can accept both text and images as input. |
-| [GPT-4o audio](#gpt-4o-audio) | A GPT-4o model that supports low-latency, "speech in, speech out" conversational interactions. |
+| [GPT-4o-Realtime-Preview](#gpt-4o-realtime-preview) | A GPT-4o model that supports low-latency, "speech in, speech out" conversational interactions. |
 | [GPT-4](#gpt-4) | A set of models that improve on GPT-3.5 and can understand and generate natural language and code. |
 | [GPT-3.5](#gpt-35) | A set of models that improve on GPT-3 and can understand and generate natural language and code. |
 | [Embeddings](#embeddings-models) | A set of models that can convert text into numerical vector form to facilitate text similarity. |
@@ -223,7 +223,7 @@ print(response.model_dump_json(indent=2))
 
 Available for standard and global standard deployment in East US, East US2, North Central US, South Central US, Sweden Central, West US, and West US3 for approved customers.
 
-## GPT-4o audio
+## GPT-4o-Realtime-Preview
 
 The `gpt-4o-realtime-preview` model is part of the GPT-4o model family and supports low-latency, "speech in, speech out" conversational interactions. GPT-4o audio is designed to handle real-time, low-latency conversational interactions, making it a great fit for support agents, assistants, translators, and other use cases that need highly responsive back-and-forth with a user.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル名の変更および説明の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関するドキュメントの一部である「models.md」ファイルにおける軽微な更新を含んでいます。具体的には、「GPT-4o audio」というモデル名が「GPT-4o-Realtime-Preview」に変更され、その説明も若干の調整が行われました。この変更は、モデルの機能により良く一致するように行われたものであり、リアルタイムでの低遅延の「音声入出力」対話インタラクションをサポートすることに重点が置かれています。

全体として、今回の更新はモデルの理解を深めるためのものであり、特にサポートエージェントや翻訳者などに関連する用途への適用を強調しています。変更はマイナーではありますが、ドキュメントの正確性と一貫性向上に寄与しています。

## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -164,6 +164,7 @@ For Provisioned-Managed and Global Provisioned-Managed, we use a variation of th
 3.	When a request finishes, we now know the actual compute cost for the call. To ensure an accurate accounting, we correct the utilization using the following logic:
 
     a.	If the actual > estimated, then the difference is added to the deployment's utilization
+
     b.	If the actual < estimated, then the difference is subtracted. 
 
 4.	The overall utilization is decremented down at a continuous rate based on the number of PTUs deployed. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "利用状況の計算ロジックの追加"
}
```

### Explanation
この変更は、「provisioned-throughput.md」ファイルにおいて、Provisioned-ManagedおよびGlobal Provisioned-Managedの利用状況を計算するためのロジックに関する軽微な更新を加えています。具体的には、リクエストに対する実際の計算コストの見積もりと実際の差を考慮する新たなロジックが追加されました。

更新された内容では、実際のコストが見積もりよりも大きい場合は、その差がデプロイメントの利用状況に加算される一方、実際のコストが見積もりよりも小さい場合にはその差が減算されると述べられています。この変更によって、より正確な利用状況の追跡と管理が可能になり、リソースの効率的な使用が促進されることが期待されます。全体として、今回の更新は、システムのパフォーマンスを改善するための重要な一歩です。

## articles/ai-services/openai/concepts/system-message.md{#item-10456c}

<details>
<summary>Diff</summary>
````diff
@@ -165,5 +165,5 @@ Finally, remember that system messages, or metaprompts, are not "one size fits a
 
 - [Azure OpenAI Service](/azure/ai-services/openai/concepts/prompt-engineering)
 - [System message design with Azure OpenAI](/azure/ai-services/openai/concepts/advanced-prompt-engineering?pivots=programming-language-chat-completions) 
-- [Announcing Safety System Messages in Azure AI Studio and Azure OpenAI Studio](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/announcing-safety-system-messages-in-azure-ai-studio-and-azure/ba-p/4146991) - Microsoft Community Hub 
+- [Announcing Safety System Messages in Azure AI Studio](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/announcing-safety-system-messages-in-azure-ai-studio-and-azure/ba-p/4146991) - Microsoft Community Hub 
 - [Safety system message templates ](./safety-system-message-templates.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの更新と削除"
}
```

### Explanation
この変更は、「system-message.md」ファイルにおいて、関連リンクの軽微な更新を行いました。具体的には、リンクの一部が修正され、誤って重複していた部分が削除されました。具体的には、「Azure AI StudioとAzure OpenAI Studioにおける安全システムメッセージの発表」というリンクが短縮され、「Azure AI Studioにおける安全システムメッセージの発表」に修正されています。

これにより、リンクがより明確になり、情報が整理されました。全体として、ドキュメントの明確性と整合性が向上し、ユーザーが関連情報にアクセスしやすくなることが期待されます。

## articles/ai-services/openai/how-to/content-filters.md{#item-6f0627}

<details>
<summary>Diff</summary>
````diff
@@ -43,11 +43,11 @@ You can configure the following filter categories in addition to the default har
 | Protected material - text | GA| On | Completion | Identifies and blocks known text content from being displayed in the model output (for example, song lyrics, recipes, and selected web content).  |
 
 
-## Configure content filters via Azure OpenAI Studio
+## Configure content filters via Azure AI Studio
 
 The following steps show how to set up a customized content filtering configuration for your resource.
 
-1. Go to Azure OpenAI Studio and navigate to the Content Filters tab (in the bottom left navigation, as designated by the red box below).
+1. Go to Azure AI Studio and navigate to the Content Filters tab (in the bottom left navigation, as designated by the red box below).
 
     :::image type="content" source="../media/content-filters/studio.png" alt-text="Screenshot of the AI Studio UI with Content Filters highlighted." lightbox="../media/content-filters/studio.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "タイトルの修正"
}
```

### Explanation
この変更は、「content-filters.md」ファイルにおいて、Azureの名称に関する軽微な修正を行いました。具体的には、タイトルおよび関連する指示文において「Azure OpenAI Studio」という表現が「Azure AI Studio」へと変更されました。この修正により、ドキュメント内の用語が一貫性を持つようになり、ユーザーが正確な情報を得やすくなることが期待されます。

さらに、設定手順の最初のステップにおいても同様に「Azure OpenAI Studio」から「Azure AI Studio」への変更が反映されています。このような用語の統一は、特にユーザーが製品やサービスに関連する操作を行う際に重要であり、混乱を避けるのに役立ちます。全体としては、ドキュメントの明確性と正確性が向上しました。

## articles/ai-services/openai/how-to/embeddings.md{#item-e38d07}

<details>
<summary>Diff</summary>
````diff
@@ -128,7 +128,7 @@ return $response.data.embedding
 
 - The maximum length of input text for our latest embedding models is 8,192 tokens. You should verify that your inputs don't exceed this limit before making a request.
 - If sending an array of inputs in a single embedding request the max array size is 2048.
-- The sum of the token count of the entire array of inputs sent in a single API call is subject to the max token limit of 8192. For example, you cannot send an array of 2,048 inputs with each input having five tokens or more. The total token count of this API request would be 10,240 total tokens, 2,048 tokens over the 8192 per API call token limit.
+- When sending an array of inputs in a single request, remember that the number of tokens per minute in your requests must remain below the quota limit that was assigned at model deployment. By default, the latest generation 3 embeddings models are subject to a 350 K TPM per region limit.  
 
 
 ## Limitations & risks
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トークン制限に関する説明の更新"
}
```

### Explanation
この変更は、「embeddings.md」ファイルにおいて、トークン制限に関する記述を更新しました。具体的には、以前の説明で「APIコールにおける最大トークン数80,192」という制約に加えて、リクエストの数に関する新しい情報が追加されました。

修正された部分では、単一のリクエストで配列を送信する際に、リクエストのトークン数の合計がモデルデプロイ時に割り当てられた制限（デフォルトで地域ごとに350 K TPM）を超えないようにする必要があることが強調されています。この変更により、ユーザーは最新の埋め込みモデルを使用する際の制限や考慮事項をより明確に理解できるようになります。全体として、ドキュメントの情報が最新の状態に保たれ、正確な運用が促進されることが期待されます。

## articles/ai-services/openai/how-to/fine-tuning.md{#item-5c0e85}

<details>
<summary>Diff</summary>
````diff
@@ -7,10 +7,10 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: build-2023, build-2023-dataai, devx-track-python
 ms.topic: how-to
-ms.date: 10/03/2024
+ms.date: 11/11/2024
 author: mrbullwinkle
 ms.author: mbullwin
-zone_pivot_groups: openai-fine-tuning-new
+zone_pivot_groups: openai-fine-tuning-newest
 ---
 
 # Customize a model with fine-tuning
@@ -31,13 +31,7 @@ We use LoRA, or low rank approximation, to fine-tune models in a way that reduce
 
 ::: zone pivot="programming-language-studio"
 
-[!INCLUDE [Azure OpenAI Studio fine-tuning](../includes/fine-tuning-studio.md)]
-
-::: zone-end
-
-::: zone pivot="programming-language-ai-studio"
-
-[!INCLUDE [AI Studio fine-tuning](../includes/fine-tuning-openai-in-ai-studio.md)]
+[!INCLUDE [Azure OpenAI Studio fine-tuning](../includes/fine-tuning-unified.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングに関するドキュメントの更新"
}
```

### Explanation
この変更は、「fine-tuning.md」ファイルにおいて、ファインチューニングに関連する情報を更新しました。具体的には、ファインチューニングのための特定の日付やリソースの参照が変更され、最新の情報が反映されています。

修正内容には、ドキュメントの日付が「2024年10月3日」から「2024年11月11日」に更新され、更新されたリソースの参照が「fine-tuning-studio.md」や「fine-tuning-openai-in-ai-studio.md」から「fine-tuning-unified.md」へと変更されました。これにより、ユーザーは最新のリソースにアクセスできるようになり、使用する際の情報がより一貫性を持つことが期待されます。

このような更新は、ファインチューニングのプロセスをよりスムーズにするための重要なステップです。全体として、使用者が最新の知識を得られることに寄与しています。

## articles/ai-services/openai/how-to/monitor-openai.md{#item-fcba4d}

<details>
<summary>Diff</summary>
````diff
@@ -71,8 +71,6 @@ After you configure the diagnostic settings, you can work with metrics and log d
 
 After you deploy an Azure OpenAI model, you can send some completions calls by using the **playground** environment in [Azure AI Studio](https://oai.azure.com/).
 
-:::image type="content" source="../media/monitoring/azure-openai-studio-playground.png" alt-text="Screenshot that shows how to generate completions for an Azure OpenAI resource in the Azure OpenAI Studio playground." lightbox="../media/monitoring/azure-openai-studio-playground.png" border="false":::
-
 Any text that you enter in the **Completions playground** or the **Chat completions playground** generates metrics and log data for your Azure OpenAI resource. In the Log Analytics workspace for your resource, you can query the monitoring data by using the [Kusto](/azure/data-explorer/kusto/query/) query language.
 
 > [!IMPORTANT]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "監視に関するドキュメントの軽微な修正"
}
```

### Explanation
この変更は、「monitor-openai.md」ファイルの監視に関する情報における軽微な修正を行いました。具体的には、ドキュメントから2つの画像参照が削除されました。これにより、情報が簡素化され、読みやすさが向上することが期待されます。

削除された画像は、Azure OpenAI Studioのプレイグラウンドから生成されるコンプリーションの方法を示すものでした。これに伴い、ユーザーがコンプリーションプレイグラウンドやチャットコンプリーションプレイグラウンドで入力したテキストがメトリクスやログデータを生成することに関する説明はそのまま残されています。この変更は、視覚的な情報が不要と判断された結果であり、ユーザーが必要な情報を得るために、テキストベースの説明に集中できるようになっています。

全体として、文書の構成が改善され、ユーザーに対する情報提供がより効率的に行われることが期待されます。

## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ Determining the right amount of provisioned throughput, or PTUs, you require for
 
 ### Estimate provisioned throughput and cost
 
-To get a quick estimate for your workload, open the capacity planner in the [Azure OpenAI Studio](https://oai.azure.com). The capacity planner is under **Shared resources** > **Quota** > **Azure OpenAI Provisioned**.
+To get a quick estimate for your workload, open the capacity planner in the [Azure AI Studio](https://ai.azure.com). The capacity calculator is under **Shared resources** > **Model Quota** > **Azure OpenAI Provisioned**.
 
 The **Provisioned** option and the capacity planner are only available in certain regions within the Quota pane, if you don't see this option setting the quota region to *Sweden Central* will make this option available. Enter the following parameters based on your workload.
 
@@ -49,14 +49,14 @@ After you fill in the required details, select **Calculate** button in the outpu
 
 The values in the output column are the estimated value of PTU units required for the provided workload inputs. The first output value represents the estimated PTU units required for the workload, rounded to the nearest PTU scale increment. The second output value represents the raw estimated PTU units required for the workload. The token totals are calculated using the following equation: `Total = Peak calls per minute * (Tokens in prompt call + Tokens in model response)`.
 
-:::image type="content" source="../media/how-to/provisioned-onboarding/capacity-calculator.png" alt-text="Screenshot of the Azure OpenAI Studio landing page." lightbox="../media/how-to/provisioned-onboarding/capacity-calculator.png":::
+:::image type="content" source="../media/how-to/provisioned-onboarding/capacity-calculator.png" alt-text="Screenshot of the capacity calculator" lightbox="../media/how-to/provisioned-onboarding/capacity-calculator.png":::
 
 > [!NOTE]
 > The capacity calculator provides an estimate based on simple input criteria. The most accurate way to determine your capacity is to benchmark a deployment with a representational workload for your use case.
 
 ## Understanding the Provisioned Throughput Purchase Model 
 
-Azure OpenAI Provisioned and Global Provisiones are purchased on-demand at an hourly basis based on the number of deployed PTUs, with substantial term discount available via the purchase of Azure Reservations.   
+Azure OpenAI Provisioned and Global Provisioned are purchased on-demand at an hourly basis based on the number of deployed PTUs, with substantial term discount available via the purchase of Azure Reservations.   
 
 The hourly model is useful for short-term deployment needs, such as validating new models or acquiring capacity for a hackathon.  However, the discounts provided by the Azure Reservation for Azure OpenAI Provisioned and Global Provisioned are considerable and most customers with consistent long-term usage will find a reserved model to be a better value proposition. 
 
@@ -86,7 +86,7 @@ Customers that require long-term usage of provisioned and global provisioned dep
 
 Discounts on top of the hourly usage price can be obtained by purchasing an Azure Reservation for Azure OpenAI Provisioned and Global Provisioned. An Azure Reservation is a term-discounting mechanism shared by many Azure products. For example, Compute and Cosmos DB. For Azure OpenAI Provisioned and Global Provisioned, the reservation provides a discount for committing to payment for fixed number of PTUs for a one-month or one-year period.  
 
-* Azure Reservations are purchased via the Azure portal, not Azure OpenAI Studio Link to Azure reservation portal. 
+* Azure Reservations are purchased via the Azure portal, not the Azure AI Studio Link to Azure reservation portal.
 
 * Reservations are purchased regionally and can be flexibly scoped to cover usage from a group of deployments. Reservation scopes include: 
 
@@ -115,7 +115,7 @@ The PTU amounts in reservation purchases are independent of PTUs allocated in qu
  
 The best practice is to always purchase a reservation after deployments have been created.  This prevents purchasing a reservation and then finding out that the required capacity is not available for the desired region or model. 
  
-To assist customers with purchasing the correct reservation amounts. The total number of PTUs in a subscription and region that can be covered by a reservation are listed on the Quotas page of Azure OpenAI Studio. See the message "PTUs Available for reservation." 
+To assist customers with purchasing the correct reservation amounts. The total number of PTUs in a subscription and region that can be covered by a reservation are listed on the Quotas page of Azure AI Studio. See the message "PTUs Available for reservation." 
 
 :::image type="content" source="../media/provisioned/available-quota.png" alt-text="A screenshot showing available PTU quota." lightbox="../media/provisioned/available-quota.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングスループットに関する情報の更新"
}
```

### Explanation
この変更は、「provisioned-throughput-onboarding.md」ファイルに関する軽微な修正を行いました。具体的には、Azure OpenAI Studioに関連する表現が更新され、いくつかの語句が修正されました。

主な変更点としては、Azure OpenAI Studioの名前が「Azure OpenAI Studio」から「Azure AI Studio」に変更され、キャパシティプランナーの場所も「Shared resources > Quota > Azure OpenAI Provisioned」から「Shared resources > Model Quota > Azure OpenAI Provisioned」に変更されています。これにより、ユーザーが必要な情報にアクセスしやすくなるように、文書が整備されました。

また、キャパシティプランナーの出力に関連する説明や、ペイメントモデルに関する表現も明確にされ、特に「Azure OpenAI Provisioned」が「Azure OpenAI Provisioned and Global Provisioned」に統一されたことで、企業はより一貫した情報を得ることができます。

全体として、これらの変更はユーザーエクスペリエンスの向上と必要情報の一貫性を目指して行われており、より適切なリソース利用を促進することが期待されます。

## articles/ai-services/openai/how-to/role-based-access-control.md{#item-4b9817}

<details>
<summary>Diff</summary>
````diff
@@ -50,8 +50,8 @@ If a user were granted role-based access to only this role for an Azure OpenAI r
 
 ✅ View the resource in [Azure portal](https://portal.azure.com) <br>
 ✅ View the resource endpoint under **Keys and Endpoint** <br>
-✅ Ability to view the resource and associated model deployments in Azure OpenAI Studio. <br>
-✅ Ability to view what models are available for deployment in Azure OpenAI Studio. <br>
+✅ Ability to view the resource and associated model deployments in Azure AI Studio. <br>
+✅ Ability to view what models are available for deployment in Azure AI Studio. <br>
 ✅ Use the Chat, Completions, and DALL-E (preview) playground experiences to generate text and images with any models that have already been deployed to this Azure OpenAI resource. <br>
 ✅ Make inference API calls with Microsoft Entra ID.
 
@@ -90,14 +90,14 @@ This role is typically granted access at the resource group level for a user in
 ✅ View resources in the assigned resource group in the [Azure portal](https://portal.azure.com). <br>
 ✅ View the resource endpoint under **Keys and Endpoint** <br>
 ✅ View/Copy/Regenerate keys under **Keys and Endpoint** <br>
-✅ Ability to view what models are available for deployment in Azure OpenAI Studio <br>
+✅ Ability to view what models are available for deployment in Azure AI Studio <br>
 ✅ Use the Chat, Completions, and DALL-E (preview) playground experiences to generate text and images with any models that have already been deployed to this Azure OpenAI resource <br>
 ✅ Create customized content filters <br>
 ✅ Add a data source for the use your data feature <br>
 ✅ Create new model deployments or edit existing model deployments (via API) <br>
 ✅ Create custom fine-tuned models **[Added Fall 2023]**<br>
 ✅ Upload datasets for fine-tuning **[Added Fall 2023]**<br>
-✅ Create new model deployments or edit existing model deployments (via Azure OpenAI Studio) **[Added Fall 2023]**
+✅ Create new model deployments or edit existing model deployments (via Azure AI Studio) **[Added Fall 2023]**
 
 A user with only this role assigned would be unable to:
 
@@ -110,37 +110,37 @@ Viewing quota requires the **Cognitive Services Usages Reader** role. This role
 
 This role can be found in the Azure portal under **Subscriptions** > ***Access control (IAM)** > **Add role assignment** > search for **Cognitive Services Usages Reader**. The role must be applied at the subscription level, it does not exist at the resource level.
 
-If you don't wish to use this role, the subscription **Reader** role provides equivalent access, but it also grants read access beyond the scope of what is needed for viewing quota. Model deployment via the Azure OpenAI Studio is also partially dependent on the presence of this role.
+If you don't wish to use this role, the subscription **Reader** role provides equivalent access, but it also grants read access beyond the scope of what is needed for viewing quota. Model deployment via the Azure AI Studio is also partially dependent on the presence of this role.
 
 This role provides little value by itself and is instead typically assigned in combination with one or more of the previously described roles.
 
 #### Cognitive Services Usages Reader + Cognitive Services OpenAI User
 
 All the capabilities of Cognitive Services OpenAI User plus the ability to:
 
-✅ View quota allocations in Azure OpenAI Studio
+✅ View quota allocations in Azure AI Studio
 
 #### Cognitive Services Usages Reader + Cognitive Services OpenAI Contributor
 
 All the capabilities of Cognitive Services OpenAI Contributor plus the ability to:
 
-✅ View quota allocations in Azure OpenAI Studio
+✅ View quota allocations in Azure AI Studio
 
 #### Cognitive Services Usages Reader + Cognitive Services Contributor
 
 All the capabilities of Cognitive Services Contributor plus the ability to:
 
-✅ View & edit quota allocations in Azure OpenAI Studio <br>
-✅ Create new model deployments or edit existing model deployments (via Azure OpenAI Studio) <br>
+✅ View & edit quota allocations in Azure AI Studio <br>
+✅ Create new model deployments or edit existing model deployments (via Azure AI Studio) <br>
 
 ## Summary
 
 | Permissions | Cognitive Services OpenAI User | Cognitive Services OpenAI Contributor |Cognitive Services Contributor |  Cognitive Services Usages Reader |
 |-------------|--------------------|------------------------|------------------|-------------------------|
-|View the resource in Azure Portal |✅|✅|✅| ➖ |
+|View the resource in Azure portal |✅|✅|✅| ➖ |
 |View the resource endpoint under “Keys and Endpoint” |✅|✅|✅| ➖ |
-|View the resource and associated model deployments in Azure OpenAI Studio |✅|✅|✅| ➖ |
-|View what models are available for deployment in Azure OpenAI Studio|✅|✅|✅| ➖ |
+|View the resource and associated model deployments in Azure AI Studio |✅|✅|✅| ➖ |
+|View what models are available for deployment in Azure AI Studio|✅|✅|✅| ➖ |
 |Use the Chat, Completions, and DALL-E (preview) playground experiences with any models that have already been deployed to this Azure OpenAI resource.|✅|✅|✅| ➖ |
 |Create or edit model deployments|❌|✅|✅| ➖ |
 |Create or deploy custom fine-tuned models|❌|✅|✅| ➖ |
@@ -153,11 +153,11 @@ All the capabilities of Cognitive Services Contributor plus the ability to:
 |Make inference API calls with Microsoft Entra ID| ✅ | ✅ | ❌ |  ➖ | 
 ## Common Issues
 
-### Unable to view Azure Cognitive Search option in Azure OpenAI Studio
+### Unable to view Azure Cognitive Search option in Azure AI Studio
 
 **Issue:**
 
-When selecting an existing Azure Cognitive Search resource the search indices don't load, and the loading wheel spins continuously. In Azure OpenAI Studio, go to **Playground Chat** > **Add your data (preview)** under Assistant setup. Selecting **Add a data source** opens a modal that allows you to add a data source through either Azure Cognitive Search or Blob Storage. Selecting the Azure Cognitive Search option and an existing Azure Cognitive Search resource should load the available Azure Cognitive Search indices to select from.
+When selecting an existing Azure Cognitive Search resource the search indices don't load, and the loading wheel spins continuously. In Azure AI Studio, go to **Playground Chat** > **Add your data (preview)** under Assistant setup. Selecting **Add a data source** opens a modal that allows you to add a data source through either Azure Cognitive Search or Blob Storage. Selecting the Azure Cognitive Search option and an existing Azure Cognitive Search resource should load the available Azure Cognitive Search indices to select from.
 
 **Root cause** 
 
@@ -177,13 +177,13 @@ For this API call, you need a **subscription-level scope** role. You can use the
 
 - Use API keys for Azure Cognitive Search: If you only need to interact with the Azure Cognitive Search service, you can request the admin keys or query keys from the subscription owner. These keys allow you to make API calls directly to the search service without needing an Azure RBAC role. Keep in mind that using API keys will **bypass** the Azure RBAC access control, so use them cautiously and follow security best practices.
 
-### Unable to upload files in Azure OpenAI Studio for on your data
+### Unable to upload files in Azure AI Studio for on your data
 
-**Symptom:** Unable to access storage for the **on your data** feature using Azure OpenAI Studio.
+**Symptom:** Unable to access storage for the **on your data** feature using Azure AI Studio.
 
 **Root cause:**
 
-Insufficient subscription-level access for the user attempting to access the blob storage in Azure OpenAI Studio. The user may **not** have the necessary permissions to call the Azure Management API endpoint: ```https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/listAccountSas?api-version=2022-09-01```
+Insufficient subscription-level access for the user attempting to access the blob storage in Azure AI Studio. The user may **not** have the necessary permissions to call the Azure Management API endpoint: ```https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/listAccountSas?api-version=2022-09-01```
 
 Public access to the blob storage is disabled by the owner of the Azure subscription for security reasons.
 
@@ -199,7 +199,7 @@ Possible reasons why the user may **not** have permissions:
 **Solution options**
 
 - Verify and update access rights: Ensure the user has the appropriate subscription-level access, including the necessary permissions for the API call (Microsoft.Storage/storageAccounts/listAccountSas/action). If required, request the subscription owner or administrator to grant the necessary access rights.
-- Request assistance from the owner or admin: If the solution above is not feasible, consider asking the subscription owner or administrator to upload the data files on your behalf. This approach can help import the data into Azure OpenAI Studio without **user** requiring subscription-level access or public access to the blob storage.
+- Request assistance from the owner or admin: If the solution above is not feasible, consider asking the subscription owner or administrator to upload the data files on your behalf. This approach can help import the data into Azure AI Studio without **user** requiring subscription-level access or public access to the blob storage.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "役割ベースのアクセス制御に関する情報の更新"
}
```

### Explanation
この変更は、「role-based-access-control.md」ファイルに関する軽微な修正を行いました。主に、Azureに関連する用語とフレーズが「Azure OpenAI Studio」から「Azure AI Studio」に更新され、文書全体で18行の追加と削除が行われました。これにより、サービスの一貫性と最新性が保たれています。

具体的には、ユーザーがAzure AI Studioでリソースやモデル展開にアクセスできることに関する説明が含まれています。また、新たに追加された機能や役割に関しても詳述され、ユーザーが自身の役割の特権を明確に理解できるようになっています。

加えて、クラウド環境でのリソース管理に必要な認可や、特定の機能にアクセスするために必要な役割の詳細な一覧が提供されています。この情報は、AzureポータルやAzure AI Studio内でのパーミッション設定に役立つことでしょう。

全体として、このアップデートはAzureにおけるサービスの説明をより正確かつ一貫性のあるものにし、ユーザーが役割ベースのアクセス制御の利用方法を容易に理解できるように挙げられたことが強調されています。

## articles/ai-services/openai/how-to/working-with-models.md{#item-7ec098}

<details>
<summary>Diff</summary>
````diff
@@ -20,9 +20,9 @@ You can get a list of models that are available for both inference and fine-tuni
 
 ## Model updates
 
-Azure OpenAI now supports automatic updates for select model deployments. On models where automatic update support is available, a model version drop-down is visible in Azure OpenAI Studio under **Deployments** and **Edit**:
+Azure OpenAI now supports automatic updates for select model deployments. On models where automatic update support is available, a model version drop-down is visible in Azure AI Studio under **Deployments** and **Edit**:
 
-:::image type="content" source="../media/models/auto-update-new.png" alt-text="Screenshot of the deploy model UI of Azure OpenAI Studio." lightbox="../media/models/auto-update-new.png":::
+:::image type="content" source="../media/models/auto-update-new.png" alt-text="Screenshot of the deploy model UI of Azure AI Studio." lightbox="../media/models/auto-update-new.png":::
 
 You can learn more about Azure OpenAI model versions and how they work in the [Azure OpenAI model versions](../concepts/model-versions.md) article.
 
@@ -40,13 +40,13 @@ When you select a specific model version for a deployment, this version remains
 
 ## Viewing retirement dates
 
-For currently deployed models, from Azure OpenAI Studio select **Deployments**:
+For currently deployed models, from Azure AI Studio select **Deployments**:
 
-:::image type="content" source="../media/models/deployments-new.png" alt-text="Screenshot of the deployment UI of Azure OpenAI Studio." lightbox="../media/models/deployments-new.png":::
+:::image type="content" source="../media/models/deployments-new.png" alt-text="Screenshot of the deployment UI of Azure AI Studio." lightbox="../media/models/deployments-new.png":::
 
 ## Model deployment upgrade configuration
 
-You can check what model upgrade options are set for previously deployed models in [Azure OpenAI Studio](https://oai.azure.com). Select **Deployments** > Under the deployment name column select one of the deployment names that are highlighted in blue.
+You can check what model upgrade options are set for previously deployed models in [Azure AI Studio](https://oai.azure.com). Select **Deployments** > Under the deployment name column select one of the deployment names that are highlighted in blue.
 
 Selecting a deployment name opens the **Properties** for the model deployment. You can view what upgrade options are set for your deployment under **Version update policy**:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルによる作業に関する情報の更新"
}
```

### Explanation
この変更は、「working-with-models.md」ファイルに関する軽微な修正を行いました。主に、Azureに関連する用語やフレーズの一貫性を高めるために、「Azure OpenAI Studio」の表現が「Azure AI Studio」に変更されました。

具体的には、モデルの自動更新機能やモデルのデプロイに関する情報が更新されており、それに伴いUIのスクリーンショットや手順も一貫した表現に修正されています。これにより、ユーザーはAzure AI Studio内での操作に関して迷うことなく、必要な情報にアクセスできるようになります。

また、モデルのバージョン管理やデプロイのアップグレード設定に関する手順も一部修正されており、これによってユーザーがAzure AI Studioでモデルを管理する際の理解が深まることが期待されます。

全体として、これらの修正はAzureにおけるサービスの説明をより明確にし、ユーザーがモデル管理やデプロイに関連する作業をスムーズに行えるようにすることを目的としています。

## articles/ai-services/openai/includes/create-resource-portal.md{#item-cb2503}

<details>
<summary>Diff</summary>
````diff
@@ -93,11 +93,11 @@ As an option, you can add a private endpoint for access to your resource. Select
 
 ## Deploy a model
 
-Before you can generate text or inference, you need to deploy a model. You can select from one of several available models in Azure OpenAI Studio.
+Before you can generate text or inference, you need to deploy a model. You can select from one of several available models in Azure AI Studio.
 
 To deploy a model, follow these steps:
 
-1. Sign in to [Azure OpenAI Studio](https://oai.azure.com).
+1. Sign in to [Azure AI Studio](https://oai.azure.com).
 
 2. Choose the subscription and the Azure OpenAI resource to work with, and select **Use resource**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースポータルに関する情報の更新"
}
```

### Explanation
この変更は、「create-resource-portal.md」ファイルに関する軽微な修正を行いました。主に、「Azure OpenAI Studio」という言葉が「Azure AI Studio」に変更され、文書内での用語の一貫性が図られました。

具体的には、モデルのデプロイに関する説明の箇所で、モデルを利用する際の操作手順が更新され、ユーザーはAzure AI Studioにサインインしてモデルを選択する必要があるという点が強調されています。この変更により、ユーザーがリソースを管理する際に、正しい作業環境についての理解が深まることが期待されます。

全体として、このアップデートはAzureにおけるサービスの説明を最新の状態に保ち、ユーザーがモデルデプロイのプロセスをスムーズに進められるようにすることを目的としています。

## articles/ai-services/openai/includes/fine-tuning-studio.md{#item-439f1e}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: 'Customize a model with Azure OpenAI Service and Azure OpenAI Studio'
+title: 'Customize a model with Azure OpenAI Service and Azure AI Studio'
 titleSuffix: Azure OpenAI
-description: Learn how to create your own custom model with Azure OpenAI Service by using the Azure OpenAI Studio.
+description: Learn how to create your own custom model with Azure OpenAI Service by using the Azure AI Studio.
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
@@ -17,8 +17,7 @@ ms.author: mbullwin
 - An Azure subscription. <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
 - An Azure OpenAI resource that's located in a region that supports fine-tuning of the Azure OpenAI model. Check the [Model summary table and region availability](../concepts/models.md#fine-tuning-models) for the list of available models by region and supported functionality. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 - Fine-tuning access requires **Cognitive Services OpenAI Contributor**.
-- If you do not already have access to view quota, and deploy models in Azure OpenAI Studio you will require [additional permissions](../how-to/role-based-access-control.md).  
-
+- If you do not already have access to view quota, and deploy models in Azure AI Studio you will require [additional permissions](../how-to/role-based-access-control.md).  
 
 ## Models
 
@@ -41,12 +40,12 @@ Or you can fine tune a previously fine-tuned model, formatted as base-model.ft-{
 Consult the [models page](../concepts/models.md#fine-tuning-models) to check which regions currently support fine-tuning.
 
 
-## Review the workflow for Azure OpenAI Studio
+## Review the workflow for Azure AI Studio
 
-Take a moment to review the fine-tuning workflow for using Azure OpenAI Studio:
+Take a moment to review the fine-tuning workflow for using Azure AI Studio:
 
 1. Prepare your training and validation data.
-1. Use the **Create custom model** wizard in Azure OpenAI Studio to train your custom model.
+1. Use the **Create custom model** wizard in Azure AI Studio to train your custom model.
     1. [Select a base model](#select-the-base-model).
     1. [Choose your training data](#choose-your-training-data).
     1. Optionally, [choose your validation data](#choose-your-validation-data).
@@ -77,7 +76,7 @@ If you would like a step-by-step walk-through of fine-tuning a `gpt-4o-mini` (20
 {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
 ```
 
-## Multi-turn chat file format
+## Multi-turn chat file format Azure OpenAI 
 
 Multiple turns of a conversation in a single line of your jsonl training file is also supported. To skip fine-tuning on specific assistant messages add the optional `weight` key value pair. Currently `weight` can be set to 0 or 1.  
 
@@ -145,13 +144,13 @@ After it guides you through the process of implementing suggested changes, the t
 
 ## Use the Create custom model wizard
 
-Azure OpenAI Studio provides the **Create custom model** wizard, so you can interactively create and train a fine-tuned model for your Azure resource.
+Azure AI Studio provides the **Create custom model** wizard, so you can interactively create and train a fine-tuned model for your Azure resource.
 
-1. Open Azure OpenAI Studio at <a href="https://oai.azure.com/" target="_blank">https://oai.azure.com/</a> and sign in with credentials that have access to your Azure OpenAI resource. During the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
+1. Open Azure AI Studio at <a href="https://oai.azure.com/" target="_blank">https://oai.azure.com/</a> and sign in with credentials that have access to your Azure OpenAI resource. During the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
 
-1. In Azure OpenAI Studio, browse to the **Tools > Fine-tuning** pane, and select **Fine-tune model**.
+1. In Azure AI Studio, browse to the **Tools > Fine-tuning** pane, and select **Fine-tune model**.
 
-   :::image type="content" source="../media/fine-tuning/studio-create-custom-model.png" alt-text="Screenshot that shows how to access the Create custom model wizard in Azure OpenAI Studio." lightbox="../media/fine-tuning/studio-create-custom-model.png":::
+   :::image type="content" source="../media/fine-tuning/studio-create-custom-model.png" alt-text="Screenshot that shows how to access the Create custom model wizard in Azure AI Studio." lightbox="../media/fine-tuning/studio-create-custom-model.png":::
 
 The **Create custom model** wizard opens.
 
@@ -180,7 +179,7 @@ For more information about our base models that can be fine-tuned, see [Models](
 
 The next step is to either choose existing prepared training data or upload new prepared training data to use when customizing your model. The **Training data** pane displays any existing, previously uploaded datasets and also provides options to upload new training data.
 
-:::image type="content" source="../media/fine-tuning/studio-training-data.png" alt-text="Screenshot of the Training data pane for the Create custom model wizard in Azure OpenAI Studio." lightbox="../media/fine-tuning/studio-training-data.png":::
+:::image type="content" source="../media/fine-tuning/studio-training-data.png" alt-text="Screenshot of the Training data pane for the Create custom model wizard in Azure AI Studio." lightbox="../media/fine-tuning/studio-training-data.png":::
 
 - If your training data is already uploaded to the service, select **Files from Azure OpenAI Connection**.
 
@@ -229,7 +228,7 @@ The next step provides options to configure the model to use validation data in
 
 The **Validation data** pane displays any existing, previously uploaded training and validation datasets and provides options by which you can upload new validation data. 
 
-:::image type="content" source="../media/fine-tuning/studio-validation-data.png" alt-text="Screenshot of the Validation data pane for the Create custom model wizard in Azure OpenAI Studio." lightbox="../media/fine-tuning/studio-validation-data.png":::
+:::image type="content" source="../media/fine-tuning/studio-validation-data.png" alt-text="Screenshot of the Validation data pane for the Create custom model wizard in Azure AI Studio." lightbox="../media/fine-tuning/studio-validation-data.png":::
 
 - If your validation data is already uploaded to the service, select **Choose dataset**.
 
@@ -294,15 +293,15 @@ After you configure the advanced options, select **Next** to [review your choice
 
 The **Review** pane of the wizard displays information about your configuration choices.
 
-:::image type="content" source="../media/fine-tuning/studio-review.png" alt-text="Screenshot of the Review pane for the Create custom model wizard in Azure OpenAI Studio." lightbox="../media/fine-tuning/studio-review.png":::
+:::image type="content" source="../media/fine-tuning/studio-review.png" alt-text="Screenshot of the Review pane for the Create custom model wizard in Azure AI Studio." lightbox="../media/fine-tuning/studio-review.png":::
 
 If you're ready to train your model, select **Start Training job** to start the fine-tuning job and return to the **Models** pane.
 
 ## Check the status of your custom model
 
 The **Models** pane displays information about your custom model in the **Customized models** tab. The tab includes information about the status and job ID of the fine-tune job for your custom model. When the job completes, the tab displays the file ID of the result file. You might need to select **Refresh** in order to see an updated status for the model training job.
 
-:::image type="content" source="../media/fine-tuning/studio-models-job-running.png" alt-text="Screenshot of the Models pane from Azure OpenAI Studio, with a custom model displayed." lightbox="../media/fine-tuning/studio-models-job-running.png":::
+:::image type="content" source="../media/fine-tuning/studio-models-job-running.png" alt-text="Screenshot of the Models pane from Azure AI Studio, with a custom model displayed." lightbox="../media/fine-tuning/studio-models-job-running.png":::
 
 After you start a fine-tuning job, it can take some time to complete. Your job might be queued behind other jobs on the system. Training your model can take minutes or hours depending on the model and dataset size.
 
@@ -318,7 +317,7 @@ Here are some of the tasks you can do on the **Models** pane:
 
 - Select **Refresh** to update the information on the page.
 
-:::image type="content" source="../media/fine-tuning/studio-model-details.png" alt-text="Screenshot of the Models pane in Azure OpenAI Studio, with a custom model displayed." lightbox="../media/fine-tuning/studio-models-job-running.png":::
+:::image type="content" source="../media/fine-tuning/studio-model-details.png" alt-text="Screenshot of the Models pane in Azure AI Studio, with a custom model displayed." lightbox="../media/fine-tuning/studio-models-job-running.png":::
 
 ## Checkpoints
 
@@ -340,13 +339,13 @@ When the fine-tuning job succeeds, you can deploy the custom model from the **Mo
 
 To deploy your custom model, select the custom model to deploy, and then select **Deploy model**.
 
-:::image type="content" source="../media/fine-tuning/studio-models-deploy-model.png" alt-text="Screenshot that shows how to deploy a custom model in Azure OpenAI Studio." lightbox="../media/fine-tuning/studio-models-deploy-model.png":::
+:::image type="content" source="../media/fine-tuning/studio-models-deploy-model.png" alt-text="Screenshot that shows how to deploy a custom model in Azure AI Studio." lightbox="../media/fine-tuning/studio-models-deploy-model.png":::
 
 The **Deploy model** dialog box opens. In the dialog box, enter your **Deployment name** and then select **Create** to start the deployment of your custom model. 
 
-:::image type="content" source="../media/fine-tuning/studio-models-deploy.png" alt-text="Screenshot of the Deploy Model dialog in Azure OpenAI Studio." lightbox="../media/fine-tuning/studio-models-deploy.png":::
+:::image type="content" source="../media/fine-tuning/studio-models-deploy.png" alt-text="Screenshot of the Deploy Model dialog in Azure AI Studio." lightbox="../media/fine-tuning/studio-models-deploy.png":::
 
-You can monitor the progress of your deployment on the **Deployments** pane in Azure OpenAI Studio.
+You can monitor the progress of your deployment on the **Deployments** pane in Azure AI Studio.
 
 ### Cross region deployment
 
@@ -358,13 +357,13 @@ Cross subscription/region deployment can be accomplished via [Python](/azure/ai-
 
 ## Use a deployed custom model
 
-After your custom model deploys, you can use it like any other deployed model. You can use the **Playgrounds** in [Azure OpenAI Studio](https://oai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models. For fine-tuned `babbage-002` and `davinci-002` models you will use the Completions playground and the Completions API. For fine-tuned `gpt-35-turbo-0613` models you will use the Chat playground and the Chat completion API.
+After your custom model deploys, you can use it like any other deployed model. You can use the **Playgrounds** in [Azure AI Studio](https://oai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models. For fine-tuned `babbage-002` and `davinci-002` models you will use the Completions playground and the Completions API. For fine-tuned `gpt-35-turbo-0613` models you will use the Chat playground and the Chat completion API.
 
-:::image type="content" source="../media/quickstarts/playground-load-new.png" alt-text="Screenshot of the Playground pane in Azure OpenAI Studio, with sections highlighted." lightbox="../media/quickstarts/playground-load-new.png":::
+:::image type="content" source="../media/quickstarts/playground-load-new.png" alt-text="Screenshot of the Playground pane in Azure AI Studio, with sections highlighted." lightbox="../media/quickstarts/playground-load-new.png":::
 
 ## Analyze your custom model
 
-Azure OpenAI attaches a result file named _results.csv_ to each fine-tuning job after it completes. You can use the result file to analyze the training and validation performance of your custom model. The file ID for the result file is listed for each custom model in the **Result file Id** column on the **Models** pane for Azure OpenAI Studio. You can use the file ID to identify and download the result file from the **Data files** pane of Azure OpenAI Studio.
+Azure OpenAI attaches a result file named _results.csv_ to each fine-tuning job after it completes. You can use the result file to analyze the training and validation performance of your custom model. The file ID for the result file is listed for each custom model in the **Result file Id** column on the **Models** pane for Azure AI Studio. You can use the file ID to identify and download the result file from the **Data files** pane of Azure AI Studio.
 
 The result file is a CSV file that contains a header row and a row for each training step performed by the fine-tuning job. The result file contains the following columns:
 
@@ -378,7 +377,7 @@ The result file is a CSV file that contains a header row and a row for each trai
 | `full_valid_loss` | The validation loss calculated at the end of each epoch. When training goes well, loss should decrease. |
 |`full_valid_mean_token_accuracy` | The valid mean token accuracy calculated at the end of each epoch. When training is going well, token accuracy should increase. |
 
-You can also view the data in your results.csv file as plots in Azure OpenAI Studio. Select the link for your trained model, and you will see three charts: loss, mean token accuracy, and token accuracy. If you provided validation data, both datasets will appear on the same plot.
+You can also view the data in your results.csv file as plots in Azure AI Studio. Select the link for your trained model, and you will see three charts: loss, mean token accuracy, and token accuracy. If you provided validation data, both datasets will appear on the same plot.
 
 Look for your loss to decrease over time, and your accuracy to increase. If you see a divergence between your training and validation data, that may indicate that you are overfitting. Try training with fewer epochs, or a smaller learning rate multiplier.
 
@@ -390,18 +389,18 @@ When you're done with your custom model, you can delete the deployment and model
 
 [!INCLUDE [Fine-tuning deletion](fine-tune.md)]
 
-You can delete the deployment for your custom model on the **Deployments** pane in Azure OpenAI Studio. Select the deployment to delete, and then select **Delete** to delete the deployment.
+You can delete the deployment for your custom model on the **Deployments** pane in Azure AI Studio. Select the deployment to delete, and then select **Delete** to delete the deployment.
 
 ### Delete your custom model
 
-You can delete a custom model on the **Models** pane in Azure OpenAI Studio. Select the custom model to delete from the **Customized models** tab, and then select **Delete** to delete the custom model.
+You can delete a custom model on the **Models** pane in Azure AI Studio. Select the custom model to delete from the **Customized models** tab, and then select **Delete** to delete the custom model.
 
 > [!NOTE]
 > You can't delete a custom model if it has an existing deployment. You must first [delete your model deployment](#delete-your-model-deployment) before you can delete your custom model.
 
 ### Delete your training files
 
-You can optionally delete training and validation files that you uploaded for training, and result files generated during training, on the **Management** > **Data files** pane in Azure OpenAI Studio. Select the file to delete, and then select **Delete** to delete the file.
+You can optionally delete training and validation files that you uploaded for training, and result files generated during training, on the **Management** > **Data files** pane in Azure AI Studio. Select the file to delete, and then select **Delete** to delete the file.
 
 ## Continuous fine-tuning
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングスタジオに関する情報の更新"
}
```

### Explanation
この変更は、「fine-tuning-studio.md」ファイルに対する軽微な更新を行いました。主に、「Azure OpenAI Studio」という表現が「Azure AI Studio」に変更され、ドキュメント内での用語の一貫性が向上しました。

具体的な修正内容としては、モデルのファインチューニングに関連する手順や説明文のいくつかが更新されており、操作手順の各ステップで「Azure AI Studio」という名称が用いられている点が挙げられます。たとえば、カスタムモデルの作成や既存のモデルのデプロイに関する段落がすべて「Azure AI Studio」の文脈で記述されています。

さらに、ファインチューニングのワークフローや、モデルのトレーニングとバリデーションデータの設定など、操作手順がより明確に示されています。変更された内容は、ユーザーがファインチューニングプロセスを理解し、正しく操作できるようにすることを目的としています。

全体として、このアップデートはAzureの文書を最新の用語に整え、ユーザーがリソースを効果的に管理できるようにするためのものです。また、ユーザーが手順に従いやすくなることで、よりスムーズにモデルのファインチューニングを行うことができるようになります。

## articles/ai-services/openai/includes/fine-tuning-unified.md{#item-718336}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,24 @@
+---
+title: 'Customize a model with Azure OpenAI Service and Azure AI Studio'
+titleSuffix: Azure OpenAI
+description: Learn how to create your own custom model with Azure OpenAI Service by using the Azure AI Studio.
+#services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 11/11/2024
+author: mrbullwinkle    
+ms.author: mbullwin
+---
+
+There are two unique fine-tuning experiences in Azure AI Studio. Both allow you to fine-tune Azure OpenAI models, but only the Hub/Project view supports fine-tuning non Azure OpenAI models. If you are only using the Azure OpenAI fine-tuning experience which is available anytime you select a resource in a region where fine-tuning is supported.
+
+# [Azure OpenAI](#tab/azure-openai)
+
+[!INCLUDE [Azure AI Studio resource view fine-tuning](../includes/fine-tuning-studio.md)]
+
+# [Hub/Project](#tab/hub)
+
+[!INCLUDE [Azure AI Studio Hub/Project fine-tuning](../includes/fine-tuning-openai-in-ai-studio.md)]
+
+---
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファインチューニングの統一インクルードガイドの追加"
}
```

### Explanation
この変更は、「fine-tuning-unified.md」という新しいファイルを追加し、Azure OpenAIサービスとAzure AI Studioを使用したカスタムモデルの作成方法についての情報を含んでいます。このファイルは、ユーザーが異なるファインチューニングの体験に関する理解を深めるためのものです。

具体的には、Azure AI Studioには二つの異なるファインチューニング体験が存在し、一方はAzure OpenAIモデルのファインチューニングをサポートし、もう一方はHub/Projectビューで非Azure OpenAIモデルのファインチューニングを支援します。この選択肢により、ユーザーは自分のニーズに応じた適切なファインチューニング手法を利用できるようになります。

加えて、このドキュメントには、Azure AI Studio内でのファインチューニングのリソースビューとHub/Projectビューに関するリンクが含まれており、それぞれの体験についての詳細情報を含むインクルードファイルへのアクセスを提供しています。

全体として、この新しいファイルはAzureの文書を充実させ、ユーザーがファインチューニングプロセスに必要な情報を迅速に見つけやすくすることを目的としており、より効率的に機能を活用できるようにサポートする役割を果たします。

## articles/ai-services/openai/media/content-filters/studio.png{#item-343759}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルター画像の更新"
}
```

### Explanation
この変更は、「studio.png」という画像ファイルにおける軽微な更新を示していますが、具体的な内容に関しては、追加や削除、変更がないため、画像のファイル自体の内容は変わっていない可能性があります。

この変更により、画像ファイルは最新のリポジトリに保持されていますが、視覚的な変更や関連する文書への影響は確認できません。通常、このような画像の更新は、関連するドキュメントやコンテンツの一貫性を保つために重要です。

したがって、法的または技術的な理由から画像が変わっていない場合でも、更新が施されることは、情報の正確性やドキュメントの整合性を維持するために役立ちます。ユーザーはこの画像が含まれる文脈で使用される際、最新の状態で表示されることを期待することができます。

## articles/ai-services/openai/media/fine-tuning/error.png{#item-b79279}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エラーメッセージ画像の更新"
}
```

### Explanation
この変更は、「error.png」という画像ファイルに関する軽微な修正を示していますが、具体的な内容については追加、削除、変更は行われていないため、実質的には画像自体の内容は変わっていない可能性があります。

この更新は、関連する資料や文脈の整合性を維持するために重要です。更新された画像は、ユーザーがファインチューニングに関連するエラーメッセージを視覚的に理解する際に使用される可能性があります。ファイルが最新のリポジトリに保たれることで、文書利用時に期待される情報の正確性やアクセス可能性が向上します。

したがって、ユーザーはこの画像が必要なコンテキストで使用される場合に、最新の状態で表示されることを期待できます。これにより、全体的なユーザーエクスペリエンスの向上に寄与します。

## articles/ai-services/openai/media/fine-tuning/studio-create-custom-model.png{#item-973d92}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムモデル作成に関する画像の更新"
}
```

### Explanation
この変更は、「studio-create-custom-model.png」という画像ファイルの軽微な更新を示していますが、この変更に伴う具体的な内容は、追加、削除、もしくは変更が行われていないため、画像の内容自体は変わっていないと思われます。

更新された画像は、カスタムモデル作成に関連する情報をユーザーに提供する際に重要です。画像が最新の状態でリポジトリに保持されることで、ユーザーがこのプロセスを視覚的に理解するのに役立ちます。ドキュメントにおける画像の一貫性は、全体的なユーザーエクスペリエンスの向上に寄与します。

このような軽微な更新によって、関連する資料やコンテンツとの整合性が維持され、ユーザーが情報を正しく理解できるようになります。この変更により、ユーザーはカスタムモデルの作成手順に関する最新の情報を確認することができます。

## articles/ai-services/openai/media/how-to/working-with-models/update-policy-new.png{#item-c99209}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの更新ポリシーに関する画像の更新"
}
```

### Explanation
この変更は、「update-policy-new.png」という画像ファイルの軽微な更新を示していますが、実際には追加、削除、変更が行われていないため、画像の内容自体は変わっていないと考えられます。

この画像はモデルの更新ポリシーに関連する情報を提供するものであり、ユーザーがモデルの管理や運用に関する理解を深めるために使われます。画像を最新のリポジトリに保持することで、参考情報の一貫性が保たれ、ユーザーが各プロセスの手順を適切に把握できるようになります。

このような軽微な更新により、関連するコンテンツとの整合性が維持され、ユーザーは正確で信頼性のある情報を得ることができます。これにより、全体的なユーザーエクスペリエンスを向上させ、情報の把握を容易にする助けとなるでしょう。

## articles/ai-services/openai/media/quickstarts/chatgpt-playground-load-new.png{#item-8ad889}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ChatGPTプレイグラウンドのロードに関する画像の更新"
}
```

### Explanation
この変更は、「chatgpt-playground-load-new.png」という画像ファイルの軽微な更新を示していますが、具体的な内容に関しては追加、削除、変更が行われていないため、画像自体には変更はありません。

この画像はChatGPTプレイグラウンドの使用方法に関連した視覚情報を提供しており、ユーザーがプレイグラウンド内での操作を理解する手助けをします。画像が最新のリポジトリに保持されることで、ドキュメントの関連性が維持され、ユーザーが情報を正しく利用できるようになります。

軽微な更新を行うことで、全体的なコンテンツとの整合性が保たれ、利用者は信頼性の高い情報を得ることができるため、ユーザーエクスペリエンスの向上につながります。この改訂により、ChatGPTを効果的に利用するための情報が常に最新であることが保証されます。

## articles/ai-services/openai/media/quickstarts/playground-load-new.png{#item-9023ae}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレイグラウンドのロードに関する画像の更新"
}
```

### Explanation
この変更は、「playground-load-new.png」という画像ファイルの軽微な更新を示していますが、実際には追加、削除、変更が行われておらず、画像の内容自体に変化はありません。

この画像はAIサービスのプレイグラウンドの使用方法に関するビジュアル情報を提供しており、ユーザーがプレイグラウンドにアクセスし、機能を理解するのに役立ちます。画像を最新のリポジトリに保持することで、ドキュメントの一貫性が保たれ、情報が常に最新の状態に維持されます。

このような軽微な更新は、関連するコンテンツとの整合性を維持し、ユーザーが正確で信頼性の高い情報にアクセスできるようにするため重要です。結果として、ユーザーエクスペリエンスが向上し、AIサービスを効果的に活用できることが促進されます。

## articles/ai-services/openai/monitor-openai-reference.md{#item-8d8887}

<details>
<summary>Diff</summary>
````diff
@@ -32,6 +32,10 @@ Here are the most important metrics we think you should monitor for Azure OpenAI
 - Time to Response
 - Time Between Tokens
 
+- Time to Last Byte
+
+- Normalized Time to First Byte 
+
 You can also monitor Content Safety metrics that are used by other Azure AI services. 
 - Blocked Volume
 - Harmful Volume Detected
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OpenAIモニタリングリファレンスのメトリクス更新"
}
```

### Explanation
この変更は、「monitor-openai-reference.md」ファイルにおける軽微な更新を示しています。具体的には、監視すべき重要なメトリクスとして「Time to Last Byte」と「Normalized Time to First Byte」の2つが新たに追加されました。これにより、Azure OpenAIのパフォーマンスをより包括的に監視するための指標が強化されました。

追加された内容は以下の通りです：

- **Time to Last Byte**：これは、サーバーが最後のバイトを送信するまでの時間を測定する指標です。この情報は、全体的な応答速度を理解する上で重要です。
- **Normalized Time to First Byte**：これは、最初のバイトがクライアントに到達するまでの時間を正規化した指標で、リクエストに対する応答の迅速さを把握するのに役立ちます。

これらのメトリクスの追加により、利用者はAzure OpenAIサービスのパフォーマンスをより良く理解し、必要に応じてリソースを最適化するための有用な情報を得ることができます。このように、ドキュメントが更新されることで、ユーザーは最新の指標を基により効果的なモニタリングを行うことができるようになります。


