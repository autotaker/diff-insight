---
date: '2024-11-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ef5a197...MicrosoftDocs:f59daa8
summary: 今回のドキュメントの更新では、Azure OpenAIに関するさまざまな情報が改訂され、新しいデータが追加されました。特に、2つの新しい画像が導入され、視覚的な理解が向上しました。また、レイテンシとスループットについての詳細情報が追加され、パフォーマンスの評価がしやすくなっています。サービス名や地域情報の改善も行われ、文書の正確性が向上しました。新しいAPIバージョンやモデル情報の更新により、ユーザーは最新の技術を活用できるようになります。全体として、これらの改訂はAzure
  OpenAIの機能を最大限に活用する手助けをすることを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ef5a197...MicrosoftDocs:f59daa8){target="_blank"}

# ハイライト
今回のドキュメント更新では、Azure OpenAIに関するさまざまな文書が微調整され、新しい情報が追加されています。特に、新しい画像の追加による視覚的支援や、レイテンシとスループットの理解を深めるための情報追加が注目されます。また、サービス名や地域情報の更新も含まれています。

## 新機能
- 新しい画像「processed-prompt-token-graph.png」と「deployment-ptu-capacity-calculator.png」の追加により、データの視覚化が向上しました。
- 構造化出力をサポートする新バージョンモデルの情報が追加され、APIバージョンも最新の状態に更新されています。

## 破壊的変更
- 特に大きな破壊的変更は報告されていませんが、新しい推奨APIバージョンへの変更など、開発者への影響がある可能性があります。

## その他の更新
- サービス名の一貫性向上や、用語の変更によりドキュメントの正確性が向上。
- 地域情報の更新により、利用可能なモデルのチェックが容易になりました。
- レイテンシとスループットに関する詳細なドキュメント更新が行われ、パフォーマンス評価を支援。

# インサイト
Azure OpenAIのサービスに関する文書の最新更新は、利用者がサービスのパフォーマンスをより効果的に評価し、最適化することを支援するものでした。ドキュメントでは、マイナーな内容の調整から始まり、新たな画像の挿入により視覚的理解を容易にする工夫が見受けられます。

特に、レイテンシやスループットに関する情報は、Azure OpenAIのユーザーが自らの環境でどのようにこれらのパフォーマンス指標を管理し、最適化するかを理解するのに重要です。トークン数の測定や推定方法の説明が追加され、ユーザーはより現実的な環境で評価を行うことができます。

また、APIやモデルの新バージョン情報の提供により、利用者は最新の技術に遅れずについていくことができ、より効率的なサービス利用が可能です。地域情報の更新により、特定の地域でのモデル利用可能性が明確化され、ビジネスへの影響を評価するのに役立ちます。

全体として、これらの変更はドキュメントの正確性と有用性を高め、利用者がAzure OpenAIの機能を最大限に活用できるよう支援することを目的としています。このようなドキュメントの更新は、技術サポートだけでなく、エンドユーザーに価値を提供するためにも非常に重要です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [provisioned-migration.md](#item-68e143) | minor update | マイナー更新: プロビジョニングされた移行に関する内容の調整 | modified | 1 | 1 | 2 | 
| [deployment-types.md](#item-210814) | minor update | マイナー更新: デプロイメントタイプに関する情報の調整 | modified | 1 | 1 | 2 | 
| [latency.md](#item-80eeec) | minor update | マイナー更新: レイテンシに関する情報の追加と整理 | modified | 43 | 11 | 54 | 
| [processed-prompt-token-graph.png](#item-284c3f) | new feature | 新規追加: プロセスされたプロンプトトークンのグラフ画像 | added | 0 | 0 | 0 | 
| [deployment-ptu-capacity-calculator.png](#item-8f1ba6) | new feature | 新規追加: デプロイメントPTU容量計算機の画像 | added | 0 | 0 | 0 | 
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | マニュアル修正: プロビジョニングされたスループットオンボーディングの内容更新 | modified | 19 | 10 | 29 | 
| [structured-outputs.md](#item-cc2557) | minor update | 更新: 構造化出力に関するドキュメントの修正 | modified | 10 | 9 | 19 | 
| [ai-search-ingestion.md](#item-60c204) | minor update | サービス名の修正: AI検索インジェスチョンのドキュメント | modified | 1 | 1 | 2 | 
| [global-batch.md](#item-929e6a) | minor update | モデルマトリックスの地域情報の追加 | modified | 6 | 0 | 6 | 


# Modified Contents
## articles/ai-services/openai/concepts/provisioned-migration.md{#item-68e143}

<details>
<summary>Diff</summary>
````diff
@@ -79,7 +79,7 @@ We also recommend that customers using commitments now create their deployments
 See the following links for more information. The guidance for reservations and commitments is the same:
 
 * [Capacity Transparency](#self-service-migration)
-* [Sizing reservations](../how-to/provisioned-throughput-onboarding.md#important-sizing-azure-openai-provisioned--global-provisioned-reservations)
+* [Sizing reservations](../how-to/provisioned-throughput-onboarding.md#important-sizing-azure-openai-provisioned-reservations)
 
 ## New hourly reservation payment model
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マイナー更新: プロビジョニングされた移行に関する内容の調整"
}
```

### Explanation
この変更は、ドキュメント「プロビジョニング移行」における内容のマイナー更新を示しています。具体的には、79行目のリスト内にあった一つの行が加えられたり削除されたりしています。元の行と新しい行の間で実質的な内容の変更はありませんが、フォーマットの調整と内容の明確化を目的とした次元での調整が行われました。この更新は、利用者がプロビジョニングされた予約に関連する情報をよりスムーズに取得できるようにすることを意図しています。

## articles/ai-services/openai/how-to/deployment-types.md{#item-210814}

<details>
<summary>Diff</summary>
````diff
@@ -43,7 +43,7 @@ Azure OpenAI offers three types of deployments. These provide a varied level of
 | **How it works**         | Offline processing via files |Traffic may be routed anywhere in the world |Traffic may be routed anywhere in the world| | |
 | **Getting started**      | [Global-Batch](./batch.md) | [Model deployment](./create-resource.md) |[Provisioned onboarding](/azure/ai-services/openai/how-to/provisioned-throughput-onboarding)| [Model deployment](./create-resource.md) | [Provisioned onboarding](./provisioned-throughput-onboarding.md) |
 | **Cost**                 | [Least expensive option](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> 50% less cost compared to Global Standard prices. Access to all new models with larger quota allocations.  | [Global deployment pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) |May experience cost savings for consistent usage|  [Regional pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) |May experience cost savings for consistent usage |
-| **What you get**         |[Significant discount compared to Global Standard](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) | Easy access to all new models with highest default pay-per-call limits.<br><br> Customers with high volume usage may see higher latency variability |Access to high & predictable throughput across Azure global infrastructure. Determine throughput per PTU using the provided [capacity calculator](/azure/ai-services/openai/how-to/provisioned-throughput-onboarding). | Easy access with [SLA on availability](https://azure.microsoft.com/support/legal/sla/). Optimized for low to medium volume workloads with high burstiness. <br><br>Customers with high consistent volume may experience greater latency variability. | Regional access with very high & predictable throughput. Determine throughput per PTU using the provided [capacity calculator](./provisioned-throughput-onboarding.md#estimate-provisioned-throughput-and-cost) |
+| **What you get**         |[Significant discount compared to Global Standard](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) | Easy access to all new models with the highest default pay-per-call limits.<br><br> Customers with high volume usage may see higher latency variability |Access to high & predictable throughput across Azure global infrastructure. Determine throughput per PTU using the provided [capacity calculator](/azure/ai-services/openai/how-to/provisioned-throughput-onboarding). |  [SLA on availability](https://azure.microsoft.com/support/legal/sla/). Optimized for low to medium volume workloads with high burstiness. <br><br>Customers with high consistent volume may experience greater latency variability. | Regional access with very high & predictable throughput. Determine throughput per PTU using the provided [capacity calculator](./provisioned-throughput-onboarding.md) |
 | **What you don’t get**   |❌Real-time call performance <br><br>❌Data processing guarantee<br> <br> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/)  |❌Data processing guarantee<br> <br> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) |❌Pay-per-call flexibility <br> <br>❌Data processing guarantee<br> <br> Data stored at rest remains in the designated Azure geography, while data may be processed for inferencing in any Azure OpenAI location. [Learn more about data residency](https://azure.microsoft.com/explore/global-infrastructure/data-residency/)| ❌High volume w/consistent low latency | ❌Pay-per-call flexibility |
 | **Per-call Latency**     | Not Applicable (file based async process) | Optimized for real-time calling & low to medium volume usage. Customers with high volume usage may see higher latency variability. Threshold set per model |Optimized for real-time calling & high-volume usage. | Optimized for real-time calling & low to medium volume usage. Customers with high volume usage may see higher latency variability. Threshold set per model |Optimized for real-time calling & high-volume usage.|
 | **Sku Name in code**     |  `GlobalBatch` |   `GlobalStandard`               |`GlobalProvisionedManaged`| `Standard`   |      `ProvisionedManaged`       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マイナー更新: デプロイメントタイプに関する情報の調整"
}
```

### Explanation
この変更は、「デプロイメントタイプ」に関する記事の内容をマイナーに更新したものです。具体的には、表形式での情報更新が行われ、一部の内容が再フォーマットされました。特に、「What you get」の行の説明が明確にされ、ユーザーに対する情報の見やすさが向上しています。この更新により、Azure OpenAIのさまざまなデプロイメントオプションがより理解しやすくなり、顧客が各オプションの特長を比較しやすくなります。変更の数は少ないものの、情報の整理と表現の向上が図られています。

## articles/ai-services/openai/how-to/latency.md{#item-80eeec}

<details>
<summary>Diff</summary>
````diff
@@ -17,29 +17,61 @@ ms.custom:
 This article provides you with background around how latency and throughput works with Azure OpenAI and how to optimize your environment to improve performance.
 
 ## Understanding throughput vs latency
-There are two key concepts to think about when sizing an application: (1) System level throughput and (2) Per-call response times (also known as Latency). 
+There are two key concepts to think about when sizing an application: (1) System level throughput measured in tokens per minute (TPM) and (2) Per-call response times (also known as latency). 
 
 ### System level throughput
 This looks at the overall capacity of your deployment – how many requests per minute and total tokens that can be processed.
 
 For a standard deployment, the quota assigned to your deployment partially determines the amount of throughput you can achieve. However, quota only determines the admission logic for calls to the deployment and isn't directly enforcing throughput. Due to per-call latency variations, you might not be able to achieve throughput as high as your quota. [Learn more on managing quota](./quota.md).
 
-In a provisioned deployment, A set amount of model processing capacity is allocated to your endpoint. The amount of throughput that you can achieve on the endpoint is a factor of the input size, output size, call rate and cache match rate. The number of concurrent calls and total tokens processed can vary based on these values. The following steps walk through how to assess the throughput you can get a given workload in a provisioned deployment:
+In a provisioned deployment, a set amount of model processing capacity is allocated to your endpoint. The amount of throughput that you can achieve on the endpoint is a factor of the workload shape including input token amount, output amount, call rate and cache match rate. The number of concurrent calls and total tokens processed can vary based on these values. 
 
-1.	Use the Capacity calculator for a sizing estimate. 
+For all deployment types, understanding system level throughput is a key component of optimizing performance. It is important to consider system level throughput for a given model, version, and workload combination as the throughput will vary across these factors. 
 
-2.	Benchmark the load using real traffic workload. Measure the utilization & tokens processed metrics from Azure Monitor. Run for an extended period. The [Azure OpenAI Benchmarking repository](https://aka.ms/aoai/benchmarking) contains code for running the benchmark. Finally, the most accurate approach is to run a  test with your own data and workload characteristics.
+#### Estimating system level throughput 
 
-Here are a few examples for GPT-4 0613 model:
+##### Estimating TPM with Azure Monitor metrics
 
-| Prompt  Size (tokens) |	Generation size (tokens) |	Calls per minute |	PTUs required |
-|--|--|--|--|
-| 800	 | 150 |	30 |	100 |
-| 1000 |	50 |	300	| 700 |
-| 5000 |	100 | 	50 |	600 |
+One approach to estimating system level throughput for a given workload is using historical token usage data. For Azure OpenAI workloads, all historical usage data can be accessed and visualized with the native monitoring capabilities offered within Azure OpenAI. Two metrics are needed to estimate system level throughput for Azure OpenAI workloads: (1) **Processed Prompt Tokens** and (2) **Generated Completion Tokens**. 
 
-The number of PTUs scales roughly linearly with call rate (might be sublinear) when the workload distribution remains constant.
+When combined, the **Processed Prompt Tokens** (input TPM) and **Generated Completion Tokens** (output TPM) metrics provide an estimated view of system level throughput based on actual workload traffic. This approach does not account for benefits from prompt caching, so it will be a conservative system throughput estimate. These metrics can be analyzed using minimum, average, and maximum aggregation over 1-minute windows across a multi-week time horizon. It is recommended to analyze this data over a multi-week time horizon to ensure there are enough data points to assess. The following screenshot shows an example of the **Processed Prompt Tokens** metric visualized in Azure Monitor, which is available directly through the Azure portal. 
 
+![Screenshot of Azure Monitor graph showcasing the Processed Prompt Tokens metric split by model and version.](media/latency/processed-prompt-token-graph.png)
+
+##### Estimating TPM from request data
+
+A second approach to estimated system level throughput involves collecting token usage information from API request data. This method provides a more granular approach to understanding workload shape per request. Combining per request token usage information with request volume, measured in requests per minute (RPM), provides an estimate for system level throughput. It is important to note that any assumptions made for consistency of token usage information across requests and request volume will impact the system throughput estimate. The token usage output data can be found in the API response details for a given Azure OpenAI Service chat completions request.
+
+```json
+{
+  "body": {
+    "id": "chatcmpl-7R1nGnsXO8n4oi9UPz2f3UHdgAYMn",
+    "created": 1686676106,
+    "choices": [...],
+    "usage": {
+      "completion_tokens": 557,
+      "prompt_tokens": 33,
+      "total_tokens": 590
+    }
+  }
+}
+```
+Assuming all requests for a given workload are uniform, the prompt tokens and completion tokens from the API response data can each be multiplied by the estimated RPM to identify the input and output TPM for the given workload. 
+
+##### How to use system level throughput estimates
+
+
+Once system level throughput has been estimated for a given workload, these estimates can be used to size Standard and Provisioned deployments. For Standard deployments, the input and output TPM values can be combined to estimate the total TPM to be assigned to a given deployment. For Provisioned deployments, the request token usage data or input and output TPM values can be used to estimate the number of PTUs required to support a given workload with the deployment capacity calculator experience. 
+
+Here are a few examples for the GPT-4o mini model:
+
+| Prompt  Size (tokens) |Generation size (tokens) |Requests per minute |Input TPM|Output TPM|Total TPM|PTUs required |
+|--|--|--| -------- | -------- | -------- |--|
+|800	 |150 |30 |24,000|4,500|28,500|15|
+|5,000 |50 |1,000|5,000,000|50,000|5,050,000|140|
+|1,000 |300 | 500 |500,000|150,000|650,000|30|
+
+The number of PTUs scales roughly linearly with call rate when the workload distribution remains constant.
 
 ### Latency: The per-call response times 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マイナー更新: レイテンシに関する情報の追加と整理"
}
```

### Explanation
この変更は、ドキュメント「レイテンシ」に関する内容を大幅に更新したもので、特にシステムレベルのスループットに関する情報が追加・整理されています。従来の情報に加え、スループットとレイテンシの基本概念についての詳細な説明が含まれ、Azure OpenAIのパフォーマンス最適化を図るための具体的な手法が示されています。

具体的には、以下の点が強調されています：

- システムレベルのスループットについて、トークン数（TPM）による測定方法が追加され、レイテンシとの関連性が示されています。
- スループットを推定するための新たなアプローチが導入され、Azure MonitorやAPIリクエストデータを使用した具体的な手法が説明されています。
- 入力トークン数や生成トークン数を基にしたスループットの推定方法が具体的に示され、実際の使用例や表が追加されています。

これにより、利用者はAzure OpenAIの導入時におけるスループットの見積もりやレイテンシの評価をより効果的に行うことができるようになります。全体的に、この更新は利用者にとって有益な情報を提供し、パフォーマンスの最適化に役立つ内容となっています。

## articles/ai-services/openai/how-to/media/latency/processed-prompt-token-graph.png{#item-284c3f}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新規追加: プロセスされたプロンプトトークンのグラフ画像"
}
```

### Explanation
この変更は、新しい画像ファイル「processed-prompt-token-graph.png」が追加されたもので、Azure OpenAIのドキュメント内でのデータ可視化をサポートする目的があります。この画像は、プロセスされたプロンプトトークンに関する情報を視覚的に示すもので、読者がスループットやレイテンシの理解を深める手助けをするために利用されます。

具体的には、このグラフは、レイテンシやスループットのパラメータを分析する際の重要な視覚的リソースとして機能します。これにより、情報の伝達が一層効果的になり、利用者は実データに基づく洞察を得やすくなります。この新規追加は、ドキュメントの教育的価値を向上させるものであり、利用者の体験を豊かにするための重要な要素となるでしょう。

## articles/ai-services/openai/how-to/media/provisioned-throughput-onboarding/deployment-ptu-capacity-calculator.png{#item-8f1ba6}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新規追加: デプロイメントPTU容量計算機の画像"
}
```

### Explanation
この変更は、新しい画像ファイル「deployment-ptu-capacity-calculator.png」が追加されたもので、Azure OpenAIのドキュメントにおけるプロビジョニングされたスループットの設定を補強する目的があります。この画像は、デプロイメントのPTU（プロセスされたトークンユニット）容量計算機のビジュアルガイドとして機能します。

具体的には、この画像は、PTU計算機の使い方や機能を示し、利用者が自分のデプロイメントに必要なスループットを効果的に評価するのを助けます。この視覚的なリソースにより、情報がより直感的に理解されるようになり、利用者は計算機の操作や結果の解釈において、より自信を持てるようになるでしょう。また、文書内の手順や説明に対して視覚的な支援を提供することで、読者の理解を深めることにも寄与します。

## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ This article walks you through the process of onboarding to [Provisioned Through
 
 ## When to use provisioned throughput units (PTU)
 
-You should consider switching from pay-as-you-go to provisioned throughput when you have well-defined, predictable throughput requirements. Typically, this occurs when the application is ready for production or has already been deployed in production and there's an understanding of the expected traffic. This allows users to accurately forecast the required capacity and avoid unexpected billing. 
+You should consider switching from standard deployments to provisioned deployments when you have well-defined, predictable throughput and latency requirements. Typically, this occurs when the application is ready for production or has already been deployed in production and there's an understanding of the expected traffic. This allows users to accurately forecast the required capacity and avoid unexpected billing. 
 
 ### Typical PTU scenarios
 
@@ -27,13 +27,22 @@ You should consider switching from pay-as-you-go to provisioned throughput when
 > [!NOTE]
 > In function calling and agent use cases, token usage can be variable. You should understand your expected Tokens Per Minute (TPM) usage in detail prior to migrating workloads to PTU.
 
-## Sizing and estimation: provisioned and global provisioned
+## Sizing and estimation: provisioned deployments
 
-Determining the right amount of provisioned throughput, or PTUs, you require for your workload is an essential step to optimizing performance and cost. This section describes how to use the Azure OpenAI capacity planning tool. The tool provides you with an estimate of the required PTU to meet the needs of your workload.
+Determining the right amount of provisioned throughput, or PTUs, you require for your workload is an essential step to optimizing performance and cost. If you are not familiar with the different approaches available to estimate system level throughput, review the system level throughput estimation recommendations in our [performance and latency documentation](./latency.md). This section describes how to use Azure OpenAI capacity calculators to estimate the number of PTUs required to support a given workload.
 
-### Estimate provisioned throughput and cost
+### Estimate provisioned throughput units and cost
 
-To get a quick estimate for your workload, open the capacity planner in the [Azure AI Studio](https://ai.azure.com). The capacity calculator is under **Shared resources** > **Model Quota** > **Azure OpenAI Provisioned**.
+To get a quick estimate for your workload using input and output TPM, leverage the built-in capacity planner in the deployment details section of the deployment dialogue screen. The built-in capacity planner is part of the deployment workflow to help streamline the sizing and allocation of quota to a PTU deployment for a given workload. For more information on how to identify and estimate TPM data, review the recommendations in our [performance and latency documentation](./latency.md). 
+
+After filling out the input and output TPM data in the built-in capacity calculator, select the **Calculate** button to view your PTU allocation recommendation. 
+
+![Screenshot of deployment workflow PTU capacity calculator.](media/provisioned-throughput-onboarding/deployment-ptu-capacity-calculator.png)
+
+
+
+
+To estimate provisioned capacity using request level data, open the capacity planner in the [Azure AI Studio](https://ai.azure.com). The capacity calculator is under **Shared resources** > **Model Quota** > **Azure OpenAI Provisioned**.
 
 The **Provisioned** option and the capacity planner are only available in certain regions within the Quota pane, if you don't see this option setting the quota region to *Sweden Central* will make this option available. Enter the following parameters based on your workload.
 
@@ -52,17 +61,17 @@ The values in the output column are the estimated value of PTU units required fo
 :::image type="content" source="../media/how-to/provisioned-onboarding/capacity-calculator.png" alt-text="Screenshot of the capacity calculator" lightbox="../media/how-to/provisioned-onboarding/capacity-calculator.png":::
 
 > [!NOTE]
-> The capacity calculator provides an estimate based on simple input criteria. The most accurate way to determine your capacity is to benchmark a deployment with a representational workload for your use case.
+> The capacity calculators provide an estimate based on simple input criteria. The most accurate way to determine your capacity is to benchmark a deployment with a representational workload for your use case.
 
-## Understanding the Provisioned Throughput Purchase Model 
+## Understanding the provisioned throughput purchase model
 
 Azure OpenAI Provisioned and Global Provisioned are purchased on-demand at an hourly basis based on the number of deployed PTUs, with substantial term discount available via the purchase of Azure Reservations.   
 
 The hourly model is useful for short-term deployment needs, such as validating new models or acquiring capacity for a hackathon.  However, the discounts provided by the Azure Reservation for Azure OpenAI Provisioned and Global Provisioned are considerable and most customers with consistent long-term usage will find a reserved model to be a better value proposition. 
 
 > [!NOTE]
 > Azure OpenAI Provisioned customers onboarded prior to the August self-service update use a purchase model called the Commitment model.  These customers can continue to use this older purchase model alongside the Hourly/reservation purchase model.  The Commitment model is not available for new customers.  For details on the Commitment purchase model and options for coexistence and migration, please see the [Azure OpenAI Provisioned August Update](../concepts/provisioned-migration.md).
-## Hourly Usage  
+## Hourly usage
 
 Provisioned and Global Provisioned deployments are charged an hourly rate ($/PTU/hr) on the number of PTUs that have been deployed.  For example, a 300 PTU deployment will be charged the hourly rate times 300.  All Azure OpenAI pricing is available in the Azure Pricing Calculator. 
 
@@ -82,7 +91,7 @@ Customers that require long-term usage of provisioned and global provisioned dep
 > * Having unused provisioned quota (PTUs) does not guarentee that capacity will be available to support increasing the size of the deployment when required. Quota limits the maximum number of PTUs that can be deployed, but it is not a capacity guarantee. Provisioned capacity for each region and modal dynamically changes throughout the day and might not be available when required. As a result, it is recommended to maintain a permanant deployment to cover your traffic needs (paid for via a reservation).
 > * Charges for deployments on a deleted resource will continue until the resource is purged.  To prevent this, delete a resource’s deployment before deleting the resource.  For more information, see [Recover or purge deleted Azure AI services resources](../../recover-purge-resources.md). 
 
-## Azure Reservations for Azure OpenAI Provisioned and Global Provisioned
+## Azure Reservations for Azure OpenAI provisioned deployments
 
 Discounts on top of the hourly usage price can be obtained by purchasing an Azure Reservation for Azure OpenAI Provisioned and Global Provisioned. An Azure Reservation is a term-discounting mechanism shared by many Azure products. For example, Compute and Cosmos DB. For Azure OpenAI Provisioned and Global Provisioned, the reservation provides a discount for committing to payment for fixed number of PTUs for a one-month or one-year period.  
 
@@ -109,7 +118,7 @@ Discounts on top of the hourly usage price can be obtained by purchasing an Azur
 >
 > * The Azure role and tenant policy requirements to purchase a reservation are different than those required to create a deployment or Azure OpenAI resource.  Verify authorization to purchase reservations in advance of needing to do so. See Azure OpenAI [Provisioned reservation documentation](https://aka.ms/oai/docs/ptum-reservations) for more details.
 
-## Important: Sizing Azure OpenAI Provisioned & Global Provisioned Reservations
+## Important: sizing Azure OpenAI provisioned reservations
 
 The PTU amounts in reservation purchases are independent of PTUs allocated in quota or used in deployments. It is possible to purchase a reservation for more PTUs than you have in quota, or can deploy for the desired region, model, or version.   Credits for over-purchasing a reservation are limited, and customers must take steps to ensure they maintain their reservation sizes in line with their deployed PTUs.  
  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マニュアル修正: プロビジョニングされたスループットオンボーディングの内容更新"
}
```

### Explanation
この変更は、プロビジョニングされたスループットのオンボーディングに関するドキュメント「provisioned-throughput-onboarding.md」に対する修正を行ったものです。主な変更点は、用語の一貫性と明確性の向上を目的に、いくつかのセクションが更新され、具体的には「pay-as-you-go」から「standard deployments」といった用語の変更や、内容の追加・修正が行われています。

特に、プロビジョニングされたスループット（PTU）の推定に関する情報が明確化され、ユーザーが実際のワークロードに基づいた要求を正確に評価できるようになっています。また、Azure AI Studio内での容量計算機の利用方法や、入力と出力のTPM（トークン毎分）のデータ入力を通じて、リソースの割り当てに関する新しい手順が追加されています。

この修正により、利用者はシステムのスループットをより正確に把握できるようになり、デプロイメントのニーズに応じたPTUの計画と評価が効率化されます。また、プロビジョニングモデルの理解を助けるために、重要な情報が整理され、明確に示されています。これにより、ドキュメント全体の質が向上し、ユーザー体験が更に充実します。

## articles/ai-services/openai/how-to/structured-outputs.md{#item-cc2557}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 08/28/2024
+ms.date: 11/20/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -23,11 +23,12 @@ Structured outputs make a model follow a [JSON Schema](https://json-schema.org/o
 
 ## Supported models
 
-Currently only `gpt-4o` version: `2024-08-06` supports structured outputs.
+- `gpt-4o-mini` version: `2024-07-18`
+- `gpt-4o` version: `2024-08-06`
 
 ## API support
 
-Support for structured outputs was first added in API version `2024-08-01-preview`.
+Support for structured outputs was first added in API version `2024-08-01-preview`. It is available in the latest preview APIs as well as the latest GA API: `2024-10-21`.
 
 ## Getting started
 
@@ -53,7 +54,7 @@ token_provider = get_bearer_token_provider(
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   azure_ad_token_provider=token_provider,
-  api_version="2024-08-01-preview"
+  api_version="2024-10-21"
 )
 
 
@@ -133,7 +134,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-08-01-preview"
+  api_version="2024-10-21"
 )
 
 
@@ -203,7 +204,7 @@ name='Science Fair' date='Friday' participants=['Alice', 'Bob']
 `response_format` is set to `json_schema` with `strict: true` set.
 
 ```bash
-curl -X POST  https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_MODEL_DEPLOYMENT_NAME/chat/completions?api-version=2024-08-01-preview \
+curl -X POST  https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_MODEL_DEPLOYMENT_NAME/chat/completions?api-version=2024-10-21 \
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -H "Content-Type: application/json" \
     -d '{
@@ -294,7 +295,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-08-01-preview"
+  api_version="2024-10-21"
 )
 
 
@@ -329,7 +330,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-08-01-preview"
+  api_version="2024-10-21"
 )
 
 class GetDeliveryDate(BaseModel):
@@ -354,7 +355,7 @@ print(response.model_dump_json(indent=2))
 # [REST](#tab/rest)
 
 ```bash
-curl -X POST  https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_MODEL_DEPLOYMENT_NAME/chat/completions?api-version=2024-08-01-preview \
+curl -X POST  https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_MODEL_DEPLOYMENT_NAME/chat/completions?api-version=2024-10-21 \
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -H "Content-Type: application/json" \
   -d '{
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新: 構造化出力に関するドキュメントの修正"
}
```

### Explanation
この変更は、「structured-outputs.md」の内容を更新し、主に新しいAPIバージョンの情報を反映させることを目的としています。具体的には、構造化出力をサポートするモデルとAPIのバージョンが更新され、最新の情報が提供されています。

変更点としては、次のことが含まれます。まず、構造化出力をサポートするモデルとして「gpt-4o-mini」バージョン「2024-07-18」が追加され、「gpt-4o」バージョン「2024-08-06」も引き続きサポートされています。また、APIのサポートセクションでは、構造化出力が最初に追加されたAPIバージョンが「2024-08-01-preview」であることが明記され、最新のGA APIである「2024-10-21」も含められました。

さらに、コードサンプルにおいて、APIバージョンを「2024-08-01-preview」から「2024-10-21」へ変更することが推奨されています。これにより、ユーザーは最新のAPIを使用して構造化出力を適切に利用できるようになります。全体的には、利用者が最新の機能やサポート体制を正しく理解し、活用できるようにするための重要な更新です。

## articles/ai-services/openai/includes/ai-search-ingestion.md{#item-60c204}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
 manager: nitinme
-ms.service: azure-ai-studio
+ms.service: azure-ai-services
 ms.custom:
 ms.topic: include
 ms.date: 10/08/2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス名の修正: AI検索インジェスチョンのドキュメント"
}
```

### Explanation
この変更は、「ai-search-ingestion.md」ファイルに対して行われた小規模な修正です。この修正では、`ms.service`の項目の値が「azure-ai-studio」から「azure-ai-services」へと変更されています。この変更により、ドキュメントが正確にサービスのダイナミクスを反映するようになります。

この修正は、サービス名の正確性を確保することで、開発者や利用者がドキュメントを参照する際に混乱を避けることを目的としています。全体として、ドキュメントの一貫性と正確性を向上させるための重要なステップです。

## articles/ai-services/openai/includes/model-matrix/global-batch.md{#item-929e6a}

<details>
<summary>Diff</summary>
````diff
@@ -8,17 +8,23 @@ ms.topic: include
 ms.date: 11/07/2024
 ---
 
+
 | **Region**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
 |:-----------------|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
 | australiaeast    | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | canadaeast       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | eastus           | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | eastus2          | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| francecentral    | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| japaneast        | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| koreacentral     | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | northcentralus   | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| norwayeast       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | southcentralus   | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | southindia       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | swedencentral    | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | switzerlandnorth | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | uksouth          | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westeurope       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | westus           | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | westus3          | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルマトリックスの地域情報の追加"
}
```

### Explanation
この変更は、「global-batch.md」ファイルにおいて、さまざまなモデルの対応地域に関する情報を更新したものです。この修正では、新たにいくつかの地域が追加され、特定のAIモデルがそれらの地域で利用可能であることが示されています。

具体的には、以下の地域が追加されました：
- フランス中部 (francecentral)
- 日本東部 (japaneast)
- 韓国中央 (koreacentral)
- ノルウェー東部 (norwayeast)
- 西ヨーロッパ (westeurope)

これらの地域において、複数のAIモデル（gpt-4o、gpt-4o-mini、gpt-4など）が全て対応可能であることが確認でき、利用者が特定の地域で利用できるモデルについての理解を深められます。この変更により、モデルの地域適応性に関する情報がより明確になり、クライアントや開発者にとって有益な更新となっています。


