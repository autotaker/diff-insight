---
date: '2025-06-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2e48ee2...MicrosoftDocs:1531236
summary: このコード変更では、AIサービスのOpenAIに関するドキュメンテーションが更新され、特にモデルの引退に関する詳細なテーブルが追加されたことで、ユーザーがモデルのライフサイクルを把握しやすくなりました。既存の記事も整理・更新され、情報が明確化されています。一部では、レガシーモデルに関する情報が大幅に整理され、古い情報が削除されたため、ユーザーに大きな影響を与えています。加えて、コンテンツストリーミングやフィルタリング設定についての情報が明確化され、ファインチューニングモデルの利用可能地域も拡張されました。これにより、ユーザー体験が向上し、サービス利用の効率が高まっています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2e48ee2...MicrosoftDocs:1531236){target="_blank"}

# Highlights
このコード変更では、AIサービスのOpenAIに関するいくつかのドキュメンテーションが更新されました。新機能として、モデルの引退に関する詳細なテーブルが追加され、より明確な情報提供が行われています。既存の記事も修正・更新され、情報の整理と明確化が図られています。一部、重大な破壊的変更が行われています。

## New features
- モデルの引退に関するテーブルの追加により、ユーザーはモデルのライフサイクルを把握しやすくなった。

## Breaking changes
- レガシーモデルとモデル引退に関する情報の大幅な整理により、古い情報が削除され、ユーザーへの影響が大きい。

## Other updates
- コンテンツストリーミングとコンテンツフィルタリング設定に関する情報が明確化された。
- ファインチューニングモデルの利用可能地域のリストが拡張された。

# Insights
今回のコード変更を通じて、Azure OpenAIサービスのドキュメンテーションが改善され、ユーザーの理解を助けるようになっています。特に、モデル引退に関するテーブルの追加により、重要な決定を行う際のガイドとしての役割が強化されました。このテーブルはモデル名、バージョン、引退日、代替モデルといった情報を整理し、ユーザーが容易にアクセスできるように構成されています。

さらに、レガシーモデルの情報を大幅に整理し、新しいモデルへとユーザーを促す設計がされています。実際に具体的な利用モデルが更新され、新しい展開を視覚化しやすくすることで切り替えをスムーズに行うことが期待されています。

コンテンツストリーミングでは、全ての顧客が対象となるように拡張されており、フィルタリング設定も明確化されました。これは、より多くの顧客にストリーミング機能を利用しやすくするための対応であると考えられます。合わせて、リクエスト時に画像入力に対するフィルタリング仕様の注意点が新たに追加されています。

ファインチューニングモデルは対応地域が増加したことで、利用可能な選択肢が広がり、特に新しい市場での展開が期待されます。ユーザーはこれにより、自社のサービスを効率的に計画することが容易にできます。

全体として、これらの変更はユーザー体験を向上させ、サービス利用の効率を大幅に高めるための重要な更新となっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [content-streaming.md](#item-f10e15) | minor update | コンテンツストリーミングに関する情報の更新 | modified | 2 | 2 | 4 | 
| [legacy-models.md](#item-f6918a) | breaking change | レガシーモデルに関する情報の削除と更新 | modified | 48 | 121 | 169 | 
| [model-retirements.md](#item-03fc2e) | breaking change | モデル引退に関する情報の大幅整理 | modified | 19 | 254 | 273 | 
| [content-filters.md](#item-6f0627) | minor update | コンテンツフィルタリング設定に関する更新 | modified | 7 | 2 | 9 | 
| [fine-tune-models.md](#item-2aadea) | minor update | ファインチューニングモデルの利用可能地域の更新 | modified | 6 | 1 | 7 | 
| [models.md](#item-5cd5bf) | new feature | モデルの引退に関するテーブルの追加 | added | 112 | 0 | 112 | 


# Modified Contents
## articles/ai-services/openai/concepts/content-streaming.md{#item-f10e15}

<details>
<summary>Diff</summary>
````diff
@@ -37,8 +37,8 @@ To enable Asynchronous Filter in [Azure AI Foundry portal](https://ai.azure.com/
 | Compare | Streaming - Default | Streaming - Asynchronous Filter |
 |---|---|---|
 |Status |GA |Public Preview |
-| Eligibility |All customers |Customers approved for modified content filtering |
-| How to enable | Enabled by default, no action needed |Customers approved for modified content filtering can configure it directly in [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) (as part of a content filtering configuration, applied at the deployment level) |
+| Eligibility |All customers |All customers |
+| How to enable | Enabled by default, no action needed |Customers can configure it directly in [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) (as part of a content filtering configuration, applied at the deployment level) |
 |Modality and availability |Text; all GPT models |Text; all GPT models |
 |Streaming experience |Content is buffered and returned in chunks |Zero latency (no buffering, filters run asynchronously) |
 |Content filtering signal |Immediate filtering signal |Delayed filtering signal (in up to ~1,000-character increments) |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツストリーミングに関する情報の更新"
}
```

### Explanation
このコードの変更は、「articles/ai-services/openai/concepts/content-streaming.md」ファイルにおいて、コンテンツストリーミング機能に関する情報を更新したものです。具体的には、ストリーミングの資格と有効化方法に関するセクションが修正されました。 

元のテキストでは、修正されたコンテンツフィルタリングの設定を行うには承認された顧客のみが対象であったのに対し、更新後はすべての顧客が対象となっています。また、有効化方法についても、原則としてデフォルトで有効である旨は変わらないものの、更新された情報が明確に示されています。この変更は、ストリーミング機能の使用をより広範囲の顧客に便宜を図るものとなっています。

## articles/ai-services/openai/concepts/legacy-models.md{#item-f6918a}

<details>
<summary>Diff</summary>
````diff
@@ -1,133 +1,60 @@
 ---
-title: Azure OpenAI in Azure AI Foundry Models deprecated models
+title: Azure OpenAI in Azure AI Foundry Models retired models
 titleSuffix: Azure OpenAI
 description: Learn about the deprecated models in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 04/30/2025
+ms.date: 06/18/2025
 ms.custom: references_regions, build-2023, build-2023-dataai
 manager: nitinme
 author: mrbullwinkle 
 ms.author: mbullwin 
 recommendations: false
 ---
 
-# Azure OpenAI in Azure AI Foundry Models deprecated models
-
-Azure OpenAI offers a variety of models for different use cases. The following models were deprecated on July 6, 2023 and will be retired on June 14, 2024.  These models are no longer available for new deployments. Deployments created prior to July 6, 2023 remain available to customers until June 14, 2024. We recommend customers migrate their applications to deployments of replacement models prior to the June 14, 2024 retirement.
-
-At the time of retirement, deployments of these models will stop returning valid API responses.
-
-## GPT-3.5
-
-The impacted GPT-3.5 models are the following. The replacement for the GPT-3.5 models is GPT-3.5 Turbo Instruct when that model becomes available.
-
-- `text-davinci-002`
-- `text-davinci-003`
-- `code-davinci-002`
-
-## GPT-3 
-
-The impacted GPT-3 models are the following. The replacement for the GPT-3 models is GPT-3.5 Turbo Instruct when that model becomes available.
-
-- `text-ada-001`
-- `text-babbage-001`
-- `text-curie-001`
-- `text-davinci-001`
-- `code-cushman-001`
-
-## Embedding models
-
-The embedding models below will be retired effective June 14, 2024. Customers should migrate to `text-embedding-ada-002` (version 2).
-
-- [Similarity](#similarity-embedding)
-- [Text search](#text-search-embedding)
-- [Code search](#code-search-embedding)
-
-Each family includes models across a range of capability. The following list indicates the length of the numerical vector returned by the service, based on model capability:
-
-|  Base Model  |  Model(s)  |  Dimensions  |
-|---|---|---|
-| Ada | | 1,024 |
-| Babbage |  | 2,048 |
-| Curie |  | 4,096 |
-| Davinci |  | 12,288 |
-
-
-### Similarity embedding
-
-These models are good at capturing semantic similarity between two or more pieces of text.
-
-| Use cases | Models |
-|---|---|
-| Clustering, regression, anomaly detection, visualization | `text-similarity-ada-001` <br> `text-similarity-babbage-001` <br> `text-similarity-curie-001` <br> `text-similarity-davinci-001` <br>|
-
-### Text search embedding
-
-These models help measure whether long documents are relevant to a short search query. There are two input types supported by this family: `doc`, for embedding the documents to be retrieved, and `query`, for embedding the search query.
-
-| Use cases | Models |
-|---|---|
-| Search, context relevance, information retrieval | `text-search-ada-doc-001` <br> `text-search-ada-query-001` <br> `text-search-babbage-doc-001` <br> `text-search-babbage-query-001` <br> `text-search-curie-doc-001` <br> `text-search-curie-query-001` <br> `text-search-davinci-doc-001` <br> `text-search-davinci-query-001` <br> |
-
-### Code search embedding
-
-Similar to text search embedding models, there are two input types supported by this family: `code`, for embedding code snippets to be retrieved, and `text`, for embedding natural language search queries.
-
-| Use cases | Models |
-|---|---|
-| Code search and relevance | `code-search-ada-code-001` <br> `code-search-ada-text-001` <br> `code-search-babbage-code-001` <br> `code-search-babbage-text-001` |
-
-## Model summary table and region availability
-
-Region availability is for customers with deployments of the models prior to July 6, 2023.
-
-### GPT-3.5 models
-
-|  Model ID  |   Base model Regions   | Fine-Tuning Regions | Max Request (tokens) | Training Data (up to)  |
-|  --------- |  --------------------- | ------------------- | -------------------- | ---------------------- |
-| text-davinci-002 | East US, South Central US, West Europe | N/A | 4,097 | Jun 2021 |
-| text-davinci-003 | East US, West Europe | N/A | 4,097 | Jun 2021 |
-| code-davinci-002 | East US,  West Europe |  N/A | 8,001 | Jun 2021 |
-
-### GPT-3 models
-
-
-|  Model ID  |   Base model Regions   | Fine-Tuning Regions | Max Request (tokens) | Training Data (up to)  |
-|  --------- |  --------------------- | ------------------- | -------------------- | ---------------------- |
-| ada        |	N/A	                  | N/A | 2,049 | Oct 2019|
-| text-ada-001 | East US, South Central US, West Europe | N/A | 2,049 | Oct 2019|
-| babbage | N/A | N/A | 2,049 | Oct 2019 |
-| text-babbage-001 | East US, South Central US, West Europe | N/A | 2,049 | Oct 2019 |
-| curie | N/A | N/A | 2,049 | Oct 2019 |
-| text-curie-001  | East US, South Central US, West Europe | N/A | 2,049 | Oct 2019 |
-| davinci | N/A | N/A | 2,049 | Oct 2019|
-| text-davinci-001 | South Central US, West Europe | N/A |  |  |
-
-
-### Codex models
-
-|  Model ID  | Base model Regions   | Fine-Tuning Regions | Max Request (tokens) | Training Data (up to)  |
-|  --- |  --- | --- | --- | --- |
-| code-cushman-001 | South Central US, West Europe | N/A | 2,048 | |
-
-### Embedding models
-
-|  Model ID  |  Base model Regions   | Fine-Tuning Regions | Max Request (tokens) | Training Data (up to)  |
-|  --- | --- | --- | --- | --- |
-| text-similarity-ada-001| East US, South Central US, West Europe | N/A | 2,046 | Aug 2020 |
-| text-similarity-babbage-001  | South Central US, West Europe | N/A | 2,046 | Aug 2020 |
-| text-similarity-curie-001 | East US, South Central US, West Europe | N/A |  2,046 | Aug 2020 |
-| text-similarity-davinci-001  | South Central US, West Europe | N/A | 2,046 | Aug 2020 |
-| text-search-ada-doc-001 | South Central US, West Europe | N/A | 2,046 | Aug 2020 |
-| text-search-ada-query-001 | South Central US, West Europe | N/A | 2,046 | Aug 2020 |
-| text-search-babbage-doc-001  | South Central US, West Europe | N/A | 2,046 | Aug 2020 |
-| text-search-babbage-query-001  | South Central US, West Europe | N/A | 2,046 | Aug 2020 |
-| text-search-curie-doc-001  | South Central US, West Europe | N/A | 2,046 | Aug 2020 |
-| text-search-curie-query-001 | South Central US, West Europe | N/A | 2,046 | Aug 2020 |
-| text-search-davinci-doc-001 | South Central US, West Europe | N/A | 2,046 | Aug 2020 |
-| text-search-davinci-query-001  | South Central US, West Europe | N/A | 2,046 | Aug 2020 |
-| code-search-ada-code-001  | South Central US, West Europe | N/A | 2,046 | Aug 2020 |
-| code-search-ada-text-001  | South Central US, West Europe | N/A | 2,046 | Aug 2020 |
-| code-search-babbage-code-001 | South Central US, West Europe | N/A | 2,046 | Aug 2020 |
-| code-search-babbage-text-001 | South Central US, West Europe | N/A | 2,046 | Aug 2020 |
+# Azure OpenAI in Azure AI Foundry Models retired models
+
+Azure OpenAI offers a variety of models for different use cases. The following models are no longer available for deployment.
+
+## Retired models
+
+ These models are no longer available for new deployments.
+
+| Model | Deprecation date | Retirement date | Suggested replacement |
+| --------- | --------------------- | ------------------- | -------------------- |
+| `gpt-4o-realtime-preview` - 2024-10-01 | February 25, 2025 | March 26, 2025 | `gpt-4o-realtime-preview` (version 2024-12-17) or `gpt-4o-mini-realtime-preview` (version 2024-12-17) |
+| `gpt-35-turbo` - 0301 | | February 13, 2025   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
+| `gpt-35-turbo` - 0613 | | February 13, 2025 | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
+| `gpt-4`<br>`gpt-4-32k` - 0314 |         | June 6, 2025                       | `gpt-4o` version: `2024-11-20`       |
+| `gpt-4`<br>`gpt-4-32k` - 0613 |         | June 6, 2025                       | `gpt-4o` version: `2024-11-20`       |
+| `gpt-35-turbo-16k`     - 0613 |         | April  30, 2025                    | `gpt-4.1-mini` version: `2025-04-14` |
+| `babbage-002` | | January 27, 2025 |  |
+| `davinci-002` | | January 27, 2025 | |
+| `dall-e-2`|  | January 27, 2025 | dalle-3 |
+| `ada` | July 6, 2023 | June 14, 2024 |  |
+| `babbage` | July 6, 2023 | June 14, 2024 |  |
+| `curie` | July 6, 2023 | June 14, 2024 | |
+| `davinci` | July 6, 2023 | June 14, 2024 |  |
+| `text-ada-001` | July 6, 2023 | June 14, 2024 | gpt-35-turbo-instruct |
+| `text-babbage-001` | July 6, 2023 | June 14, 2024 | gpt-35-turbo-instruct |
+| `text-curie-001` | July 6, 2023 | June 14, 2024 | gpt-35-turbo-instruct |
+| `text-davinci-002` | July 6, 2023 | June 14, 2024 | gpt-35-turbo-instruct |
+| `text-davinci-003` | July 6, 2023 | June 14, 2024 | gpt-35-turbo-instruct |
+| `code-cushman-001` | July 6, 2023 | June 14, 2024 | gpt-35-turbo-instruct |
+| `code-davinci-002` | July 6, 2023 | June 14, 2024 | gpt-35-turbo-instruct |
+| `text-similarity-ada-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `text-similarity-babbage-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `text-similarity-curie-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `text-similarity-davinci-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `text-search-ada-doc-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `text-search-ada-query-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `text-search-babbage-doc-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `text-search-babbage-query-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `text-search-curie-doc-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `text-search-curie-query-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `text-search-davinci-doc-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `text-search-davinci-query-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `code-search-ada-code-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `code-search-ada-text-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `code-search-babbage-code-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
+| `code-search-babbage-text-001` | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "レガシーモデルに関する情報の削除と更新"
}
```

### Explanation
このコード変更は、「articles/ai-services/openai/concepts/legacy-models.md」ファイルにおける内容の大規模な更新を示しています。主に、レガシーモデルに関連する情報が整理され、古い情報が削除され、新しい情報が追加されました。変更の主なポイントは以下の通りです。

1. **レガシーモデルのタイトルの更新**: ページのタイトルが「deprecated models」から「retired models」に変更されており、これによりモデルの状態がより明確に示されています。

2. **モデルの廃止に関する詳細の簡略化**: 多くの旧モデルに関する詳細が削除され、新しいモデルの有効化についての情報が更新されています。例えば、`gpt-3.5`や`gpt-3`に関連する多くの具体的なモデルが挙げられていた部分が簡潔なリストにまとめられています。

3. **新しい代替モデルの紹介**: 新しく廃止されるモデルの代替品が詳細に示されており、顧客が新たに導入すべきモデルについての情報も更新されています。

変更の結果、古い情報が大幅に削除されたため、ユーザーにとっては重要な情報がより明確に、かつ簡潔に提示されています。この更新は、将来のモデルに関する戦略を理解するために必要な情報を提供することを目的としています。

## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -29,11 +29,22 @@ Azure OpenAI models are continually refreshed with newer and more capable models
 
 Azure OpenAI notifies customers of active Azure OpenAI deployments for models with upcoming retirements. We notify customers of upcoming retirements as follows for each deployment:
 
-1. At model launch, we programmatically designate a "not sooner than" retirement date (typically one year out).
+1. At model launch, we programmatically designate a "not sooner than" retirement date (for preview models this is between 90-120 days from launch, for generally available (GA) models this is 365 days from launch).
 2. At least 60 days notice before model retirement for Generally Available (GA) models.
-3. At least 30 days notice before preview model version upgrades.  
+3. At least 30 days notice before preview model version upgrades.
 
-Retirements are done on a rolling basis, region by region. Notifications are sent from an unmonitored mailbox, `azure-noreply@microsoft.com`.
+Retirements are done on a rolling basis, region by region. There is no schedule for when a specific region, or SKU will be upgraded.
+
+## Current models
+
+> [!NOTE]
+> Not all models go through a deprecation period prior to retirement. Some models/versions only have a retirement date.
+>
+> **Fine-tuned models** are subject to a [different](#fine-tuned-models) deprecation and retirement schedule from their equivalent base model.
+
+These models are currently available for use in Azure OpenAI.
+
+[!INCLUDE [Model retirement table](../includes/retirement/models.md)]
 
 ## Model availability
 
@@ -64,13 +75,11 @@ Be aware of the following:
 
 ### Who is notified of upcoming retirements
 
-Azure OpenAI notifies those who are members of the following roles for each subscription with a deployment of a model with an upcoming retirement.
+Azure OpenAI notifies customers via two methods:
+- **Azure Resource Health** - Anyone with reader permissions or above can see Azure health alerts, as well as configure personalized alerts via email, SMS, etc. See [Create Service Health Alerts](/azure/service-health/alerts-activity-log-service-notifications-portal)
+- **Email** - email notifications are automatically sent to subscription owners. Any individual with reader permissions may however configure their own alerts by following the guidance above.
+
 
-* Owner
-* Contributor
-* Reader
-* Monitoring contributor
-* Monitoring reader
 
 ## How to get ready for model retirements and version upgrades
 
@@ -82,250 +91,6 @@ For information on the model upgrade process, see [How to upgrade to a new model
 
 For more information on how to manage model upgrades and migrations for provisioned deployments, see [Managing models on provisioned deployment types](../how-to/working-with-models.md#managing-models-on-provisioned-deployment-types)
 
-## Current models
-
-> [!NOTE]
-> Not all models go through a deprecation period prior to retirement. Some models/versions only have a retirement date.
->
-> **Fine-tuned models** are subject to a [different](#fine-tuned-models) deprecation and retirement schedule from their equivalent base model.
-
-These models are currently available for use in Azure OpenAI.
-
-| Model                     | Version         | Retirement date                    | Replacement model                    |
-| --------------------------|-----------------|------------------------------------|--------------------------------------|
-| `computer-use-preview`    | 2025-03-11      | No earlier than September 1, 2025  |                                      |
-| `dall-e-3`                | 3               | No earlier than June 30, 2025      |                                      |
-| `gpt-35-turbo-16k`        | 0613            | April  30, 2025                    | `gpt-4.1-mini` version: `2025-04-14` |
-| `gpt-35-turbo`            | 1106            | No earlier than July 16, 2025      | `gpt-4.1-mini` version: `2025-04-14` |
-| `gpt-35-turbo`            | 0125            | No earlier than July 16, 2025      | `gpt-4.1-mini` version: `2025-04-14` |
-| `gpt-4`<br>`gpt-4-32k`    | 0314            | June 6, 2025                       | `gpt-4o` version: `2024-11-20`       |
-| `gpt-4`<br>`gpt-4-32k`    | 0613            | June 6, 2025                       | `gpt-4o` version: `2024-11-20`       |
-| `gpt-4`                   | turbo-2024-04-09| No earlier than June 6, 2025       | `gpt-4o` version: `2024-11-20`       |
-| `gpt-4`                   | 1106-preview    | May 1, 2025                        | `gpt-4o` version: `2024-11-20`       |
-| `gpt-4`                   | 0125-preview    | May 1, 2025                        | `gpt-4o` version: `2024-11-20`        |
-| `gpt-4`                   | vision-preview  | May 15, 2025                       | `gpt-4o` version: `2024-11-20`       |
-| `gpt-4.5-preview`         | 2025-02-27      | No Auto-upgrades <br>July 14, 2025 | `gpt-4.1` version: `2025-04-14`      |
-| `gpt-4.1`                 | 2025-04-14      | No earlier than April 11, 2026     |                                      |
-| `gpt-4.1-mini`            | 2025-04-14      | No earlier than April 11, 2026     |                                      |
-| `gpt-4.1-nano`            | 2025-04-14      | No earlier than April 11, 2026     |                                      |
-| `gpt-4o`                  | 2024-05-13      | No earlier than June 30, 2025      | `gpt-4.1` version: `2025-04-14`      |
-| `gpt-4o`                  | 2024-08-06      | No earlier than August 6, 2025     | `gpt-4.1` version: `2025-04-14`      |
-| `gpt-4o`                  | 2024-11-20      | No earlier than March 1, 2026      | `gpt-4.1` version: `2025-04-14`      |
-| `gpt-4o-mini`             | 2024-07-18      | No earlier than August 16, 2025    | `gpt-4.1-mini` version: `2025-04-14` |
-| `gpt-3.5-turbo-instruct`  | 0914            | No earlier than May 31, 2025       |                                      |
-| `gpt-image-1`             | 2025-04-15      | No earlier than August 01, 2025    |                                      |
-| `o1-preview`              | 2024-09-12      | May 29, 2025                       | `o1`                                 |
-| `o1`                      | 2024-12-17      | No earlier than December 17, 2025  |                                      |
-| `o4-mini`                 | 2025-04-16      | No earlier than April 11, 2026     |                                      |
-| `o3`                      | 2025-04-16      | No earlier than April 11, 2026     |                                      |
-| `o3-mini`                 | 2025-01-31      | No earlier than February 1, 2026   |                                      |
-| `text-embedding-ada-002`  | 2               | No earlier than April 30, 2026     | `text-embedding-3-small` or `text-embedding-3-large` |
-| `text-embedding-ada-002`  | 1               | No earlier than April 30, 2026     | `text-embedding-3-small` or `text-embedding-3-large` |
-| `text-embedding-3-small`  |                 | No earlier than April 30, 2026     |                                      |
-| `text-embedding-3-large`  |                 | No earlier than April 30, 2026     |                                      |
-
-
-We'll notify all customers with these preview deployments at least 30 days before the start of the upgrades. We'll publish an upgrade schedule detailing the order of regions and model versions that we'll follow during the upgrades, and link to that schedule from here.
-
-> [!TIP]
-> **Will a model upgrade happen if the new model version is not yet available in that region?**
->
-> Yes, even in cases where the latest model version is not yet available in a region, we'll automatically upgrade deployments during the scheduled upgrade window. For more information, see [Azure OpenAI model versions](/azure/ai-services/openai/concepts/model-versions#will-a-model-upgrade-happen-if-the-new-model-version-is-not-yet-available-in-that-region).
-
-> [!IMPORTANT]
-> Vision enhancements preview features including Optical Character Recognition (OCR), object grounding, video prompts will be retired and no longer available once `gpt-4` Version: `vision-preview` is upgraded to `turbo-2024-04-09`. If you're currently relying on any of these preview features, this automatic model upgrade will be a breaking change.
-
-## Fine-tuned models
-
-Fine-tuned models retire in two phases: training and deployment.
-
-All fine-tuned models follow their equivalent base model for **training** retirement. Once retired, a given model is no longer available for fine tuning.
-
-For fine-tuned models made generally available since `gpt-4o-2024-08-06`, **deployment** retirement occurs 1 year after **training** retirement. At deployment retirement, inference and deployment returns error responses.
-
-| Model            | Version     | Training retirement date  | Deployment retirement date       |
-| -----------------|-------------|---------------------------|----------------------------------|
-| `gpt-35-turbo`   | 1106        | At base model retirement  | At training retirement           |
-| `gpt-35-turbo`   | 0125        | At base model retirement  | At training retirement           |
-| `gpt-4o`         | 2024-08-06  | At base model retirement  | One year after training retirement |
-| `gpt-4o-mini`    | 2024-07-18  | At base model retirement  | One year after training retirement |
-| `gpt-4.1`        | 2025-04-14  | At base model retirement  | One year after training retirement |
-| `gpt-4.1-mini`   | 2025-04-14  | At base model retirement  | One year after training retirement |
-| `gpt-4.1-nano`   | 2025-04-14  | At base model retirement  | One year after training retirement |
-| `o4-mini`        | 2025-04-16  | At base model retirement  | One year after training retirement |
-
-## Default model versions
-
-| Model | Current default version | New default version | Default upgrade date |
-|---|---|---|---|
-| `gpt-35-turbo` | 0301 | 0125 | Deployments of versions `0301`, `0613`, and `1106` set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 21, 2025.|
-|  `gpt-4o` | 2024-08-06 | - | - |
-
-## Deprecated models
-
- These models are no longer available for new deployments.
-
-If you're an existing customer looking for information about these models, see [Legacy models](./legacy-models.md).
-
-| Model | Deprecation date | Retirement date | Suggested replacement |
-| --------- | --------------------- | ------------------- | -------------------- |
-| `gpt-4o-realtime-preview` - 2024-10-01 | February 25, 2025 | March 26, 2025 | `gpt-4o-realtime-preview` (version 2024-12-17) or `gpt-4o-mini-realtime-preview` (version 2024-12-17) |
-| `gpt-35-turbo` - 0301 | | February 13, 2025   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
-| `gpt-35-turbo` - 0613 | | February 13, 2025 | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
-| babbage-002 | | January 27, 2025 |  |
-| davinci-002 | | January 27, 2025 | |
-| dall-e-2|  | January 27, 2025 | dalle-3 |
-| ada | July 6, 2023 | June 14, 2024 |  |
-| babbage | July 6, 2023 | June 14, 2024 |  |
-| curie | July 6, 2023 | June 14, 2024 | |
-| davinci | July 6, 2023 | June 14, 2024 |  |
-| text-ada-001 | July 6, 2023 | June 14, 2024 | gpt-35-turbo-instruct |
-| text-babbage-001 | July 6, 2023 | June 14, 2024 | gpt-35-turbo-instruct |
-| text-curie-001 | July 6, 2023 | June 14, 2024 | gpt-35-turbo-instruct |
-| text-davinci-002 | July 6, 2023 | June 14, 2024 | gpt-35-turbo-instruct |
-| text-davinci-003 | July 6, 2023 | June 14, 2024 | gpt-35-turbo-instruct |
-| code-cushman-001 | July 6, 2023 | June 14, 2024 | gpt-35-turbo-instruct |
-| code-davinci-002 | July 6, 2023 | June 14, 2024 | gpt-35-turbo-instruct |
-| text-similarity-ada-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| text-similarity-babbage-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| text-similarity-curie-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| text-similarity-davinci-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| text-search-ada-doc-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| text-search-ada-query-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| text-search-babbage-doc-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| text-search-babbage-query-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| text-search-curie-doc-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| text-search-curie-query-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| text-search-davinci-doc-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| text-search-davinci-query-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| code-search-ada-code-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| code-search-ada-text-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| code-search-babbage-code-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-| code-search-babbage-text-001 | July 6, 2023 | June 14, 2024 | text-embedding-3-small |
-
 ## Retirement and deprecation history
 
-## April 15, 2025
-
-To track further individual updates to this article refer to the [Git History](https://github.com/MicrosoftDocs/azure-ai-docs/commits/main/articles/ai-services/openai/concepts/model-retirements.md)
-
-## March 18, 2025
-
-GPT-4 preview models retirement date updated to date: May 1, 2025.
-
-## February 28, 2025
-
-- Updated `gpt-4` versions `1106-preview`, `0125-preview`, `vision-preview` to be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than March 10, 2025.
-
-## February 25, 2025
-
--  `dalle-3` updated to no earlier than June 30, 2025.
-- `gpt-4o-realtime-preview` (2024-10-01) No earlier than March 26, 2025.
-
-## February 20, 2025
-
-- `o1-preview` updated to no earlier than April 2, 2025.
-
-## February 12, 2025
-
-- Updates to `gpt-35-turbo-16k` (0613), (1106), `gpt-35-turbo-instruct`, `gpt-4` (turbo-2024-04-09)
-
-## February 6, 2025
-
-- Updates to `gpt-35-turbo`, `gpt-4` preview models, and `gpt-4o` models.
-
-## January 9, 2025
-
-- `o1` added.
-- `gpt-35-turbo instruct` updated to no earlier than April 1, 2025.
-- `gpt-35-turbo` (0125) updated to no earlier than May 31, 2025.
-
-## December 11, 2024
-
-Embeddings models updated to no earlier than October 3, 2025.
-
-## December 2, 2024
-
-`gpt-3.5-turbo-instruct` updated to no earlier than February 1, 2025.
-
-## November 22, 2024
-
-`gpt-35-turbo` 1106 retirement date updated to no earlier than March 31, 2025.
-
-## November 11, 2024
-
-Updates to:
-
-- `babbage-002`, `davinci-002`.
-- `gpt-35-turbo` DEFAULT model version update date.
-- `gpt-35-turbo` 0301, 0613 retirement date.
-- `gpt-35-turbo` 0125 retirement date.
-- `gpt-4o` DEFAULT model update date.
-- `text-embeddings-3-small` & `text-embedding-3-large` retirement date.
-
-## October 25, 2024
-
-* `babbage-002` & `davinci-002` deprecation date: November 15, 2024  and retirement date: January 27, 2025.
-
-## September 12, 2024
-
-* `gpt-35-turbo` (0301), (0613), (1106) and `gpt-35-turbo-16k` (0613) auto-update to default upgrade date updated to November 13, 2024.
-
-## September 9, 2024
-
-* `gpt-35-turbo` (0301) and (0613) retirement changed to January 27, 2025.
-* `gpt-4` preview model upgrade date changed to starting no sooner than January 27, 2025.
-
-## September 3, 2024
-
-* Updated tables to include information on `gpt-35-turbo` default version upgrades. Deployments of versions `0301`, `0613`, and `1106` set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 15, 2024.|
-
-### August 22, 2024
-
-* Updated `gpt-35-turbo` (0301) retirement date to no earlier than November 1, 2024.
-* Updated `gpt4` and `gpt-4-32k` (0314 and 0613) deprecation date to November 1, 2024.
-
-### August 8, 2024
-
-* Updated `gpt-35-turbo` & `gpt-35-turbo-16k` (0613) model's retirement date to November 1, 2024.
-
-### July 30, 2024
-
-* Updated `gpt-4` preview model upgrade date to November 15, 2024 or later for the following versions:
-  * 1106-preview
-  * 0125-preview
-  * vision-preview (Vision enhancements feature will no longer be supported once this model is retired/upgraded.)
-
-### July 18, 2024
-
-* Updated `gpt-4` 0613  deprecation date to October 1, 2024 and the retirement date to June 6, 2025.
-
-### June 19, 2024
-
-* Updated `gpt-35-turbo` 0301 retirement date to no earlier than October 1, 2024.
-* Updated `gpt-35-turbo` & `gpt-35-turbo-16k`0613 retirement date to October 1, 2024.
-* Updated `gpt-4` & `gpt-4-32k` 0314 deprecation date to October 1, 2024, and retirement date to June 6, 2025.  
-
-### June 4, 2024
-
-Retirement date for legacy models updated by one month.
-
-### April 24, 2024
-
-Earliest retirement date for `gpt-35-turbo` 0301 and 0613 has been updated to August 1, 2024.
-
-### March 13, 2024
-
-We published this document to provide information about the current models, deprecated models, and upcoming retirements.
-
-### February 23, 2024
-
-We announced the upcoming in-place upgrade of `gpt-4` version `1106-preview` to `0125-preview` to start no earlier than March 8, 2024.
-
-### November 30, 2023
-
-The default version of `gpt-4` and `gpt-3-32k` was updated from `0314` to `0613` starting on November 30, 2023. The upgrade of `0314` deployments set for autoupgrade to `0613` was completed on December 3, 2023.
-
-### July 6, 2023
-
-We announced the deprecation of models with upcoming retirement on July 5, 2024.
+To track individual updates to this article refer to the [Git History](https://github.com/MicrosoftDocs/azure-ai-docs/commits/main/articles/ai-services/openai/includes/retirement/models.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデル引退に関する情報の大幅整理"
}
```

### Explanation
このコード変更は、「articles/ai-services/openai/concepts/model-retirements.md」ファイルの内容を大幅に整理したことを示しています。この変更には、モデルの引退やバージョンアップに関する通知方法、現在利用可能なモデル、およびそれらの取り扱いに関する新しい情報が含まれています。

主な変更点は以下の通りです：

1. **通知方法の更新**: モデルの引退予定に関する通知が、プレビューおよび一般提供（GA）モデルに対してそれぞれ異なる告知期間を持つことが明示されました。特に、プレビューモデルは90〜120日後、GAモデルは365日後に引退予定日が設定されることが記載されています。

2. **現在のモデルリストの追加**: 現在利用可能なモデルに関するセクションが追加され、ユーザーが今使えるモデルを簡単に確認できるようになりました。

3. **通知方法の具体化**: Azure OpenAIの通知がどのように行われるかが具体的に述べられ、Azure Resource Healthを通じたアラートやメール通知の仕組みが紹介されています。

4. **不必要な詳細の削除**: 以前のバージョンでは詳細にリストアップされていた特定のモデルの退役予定や置き換えモデルについての情報が大幅に削減され、簡潔な形式にまとまりました。

この整理により、ユーザーはモデル引退に関する情報をより迅速かつ効率的に把握しやすくなっています。特に、新しいモデルの使用開始や引退モデルの管理において、重要なポイントが明確に示されています。

## articles/ai-services/openai/how-to/content-filters.md{#item-6f0627}

<details>
<summary>Diff</summary>
````diff
@@ -53,7 +53,7 @@ You can configure the following filter categories in addition to the default har
 
 ## Specify a content filtering configuration at request time (preview)
 
-In addition to the deployment-level content filtering configuration, we also provide a request header that allows you specify your custom configuration at request time for every API call. 
+In addition to the deployment-level content filtering configuration, we also provide a request header that allows you specify your custom configuration at request time for each API call. 
 
 ```bash
 curl --request POST \ 
@@ -75,7 +75,12 @@ curl --request POST \
     }' 
 ```
 
-The request-level content filtering configuration will override the deployment-level configuration, for the specific API call. If a configuration is specified that does not exist, the following error message will be returned. 
+The request-level content filtering configuration will override the deployment-level configuration, for the specific API call. 
+
+> [!IMPORTANT]
+> Content filter specification at request time is not available for image input (chat with images) scenarios. In those cases the default content filter will be used.
+
+If a configuration is specified that does not exist, the following error message will be returned. 
 
 ```json
 { 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリング設定に関する更新"
}
```

### Explanation
このコード変更は、「articles/ai-services/openai/how-to/content-filters.md」ファイルの内容を更新したもので、主にコンテンツフィルタリング設定に関連する情報が調整されました。具体的には、内容の明確化と重要な注意点が追加されています。

主な変更点は以下の通りです：

1. **文言の修正**: 「every API call」から「each API call」に変更されました。これにより、表現が一貫性を持ち、ユーザーにとって理解しやすくなっています。

2. **新しい警告の追加**: リクエスト時にコンテンツフィルタを指定する際の制限事項についての重要な注意点が追加されました。この注意点では、画像入力（画像を含むチャット）シナリオにおいてはリクエスト時のフィルタリング仕様が利用できず、デフォルトのコンテンツフィルタが使用されることが強調されています。

3. **構造の整理**: 既存の内容のフォーマットが整理され、重要な情報が目立つように配置されています。

この更新により、ユーザーがコンテンツフィルタリングを設定する際の条件や制限が明確になり、より適切な利用が促進されることが期待されます。

## articles/ai-services/openai/includes/fine-tune-models.md{#item-2aadea}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,8 @@ ms.custom:
 > **Global** training (in Public Preview) provides [more affordable](https://aka.ms/aoai-pricing) training per-token, but does not offer [data residency](https://aka.ms/data-residency). It is currently available to Azure OpenAI resources in the following regions, with more regions coming soon:
 >- Australia East
 >- Brazil South
->- EastUS2
+>- East US
+>- East US2
 >- France Central
 >- Germany West Central
 >- Italy North
@@ -47,3 +48,7 @@ ms.custom:
 >- Spain Central
 >- Sweden Central
 >- Switzerland West
+>- Switzerland North
+>- UK South
+>- West US
+>- West US3
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングモデルの利用可能地域の更新"
}
```

### Explanation
このコード変更は、「articles/ai-services/openai/includes/fine-tune-models.md」ファイルの内容を更新したもので、ファインチューニングモデルの利用可能地域に関する情報が追加されています。主に、新しい地域がリストに加えられたことが特徴です。

主な変更点は以下の通りです：

1. **地域名の修正**: 「EastUS2」という表記が「East US」に修正され、より明確な地域名が使用されています。

2. **新しい地域の追加**: 利用可能地域のリストにいくつかの新しい地域が加わりました：
   - **Switzerland North**
   - **UK South**
   - **West US**
   - **West US3**

3. **フォーマットの一貫性**: 追加された地域が他の地域名と同様のフォーマットで記載されており、リスト全体の整合性が保たれています。

この更新により、ユーザーはファインチューニングモデルの利用可能な地域をより包括的に理解できるようになり、サービス利用の計画がしやすくなります。

## articles/ai-services/openai/includes/retirement/models.md{#item-5cd5bf}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,112 @@
+---
+title: Model retirement table 
+titleSuffix: Azure OpenAI in Azure AI Foundry Models
+description: Model retirement table for  Azure OpenAI in Azure AI Foundry Models
+manager: nitinme
+ms.date: 06/18/2025
+ms.service: azure-ai-openai
+ms.topic: include
+ms.custom: references_regions, build-2025
+---
+
+
+# [Text generation](#tab/text)
+
+### Text generation
+
+| Model                     | Version         | Retirement date                    | Replacement model                    |
+| --------------------------|-----------------|------------------------------------|--------------------------------------|
+| `gpt-4.5-preview`         | 2025-02-27      | No Auto-upgrades <br>July 14, 2025 | `gpt-4.1` version: `2025-04-14`      |
+| `gpt-3.5-turbo-instruct`  | 0914            | No earlier than July 16, 2025      |                                      |
+| `o1-preview`              | 2024-09-12      | July 28, 2025                      | `o1`                                 |
+| `computer-use-preview`    | 2025-03-11      | No earlier than September 1, 2025  |                                      |
+| `gpt-35-turbo`            | 1106            | No earlier than September 1, 2025  | `gpt-4.1-mini` version: `2025-04-14` |
+| `gpt-35-turbo`            | 0125            | No earlier than September 1, 2025  | `gpt-4.1-mini` version: `2025-04-14` |
+| `gpt-4`                   | turbo-2024-04-09| No earlier than September 1, 2025  | `gpt-4o` version: `2024-11-20`       |
+| `model router`            | 2025-05-19      | No earlier than September 1, 2025  |                                      |
+| `gpt-4o`                  | 2024-05-13      | No earlier than September 15, 2025 | `gpt-4.1` version: `2025-04-14`      |
+| `gpt-4o-mini`             | 2024-07-18      | No earlier than September 15, 2025 | `gpt-4.1-mini` version: `2025-04-14` |
+| `o1-mini`                 | 2024-09-12      | No earlier than September 26, 2025 |                                      |
+| `gpt-4o`                  | 2024-08-06      | No earlier than October 15, 2025   | `gpt-4.1` version: `2025-04-14`      |
+| `o1`                      | 2024-12-17      | No earlier than December 17, 2025  |                                      |
+| `o3-mini`                 | 2025-01-31      | No earlier than February 1, 2026   |                                      |
+| `gpt-4o`                  | 2024-11-20      | No earlier than March 1, 2026      | `gpt-4.1` version: `2025-04-14`      |
+| `gpt-4.1`                 | 2025-04-14      | No earlier than April 11, 2026     |                                      |
+| `gpt-4.1-mini`            | 2025-04-14      | No earlier than April 11, 2026     |                                      |
+| `gpt-4.1-nano`            | 2025-04-14      | No earlier than April 11, 2026     |                                      |
+| `o4-mini`                 | 2025-04-16      | No earlier than April 11, 2026     |                                      |
+| `o3`                      | 2025-04-16      | No earlier than April 11, 2026     |                                      |
+
+# [Audio](#tab/audio)
+
+### Audio
+
+| Model                          | Version         | Retirement date                    | Replacement model                    |
+| -------------------------------|-----------------|------------------------------------|--------------------------------------|
+| `gpt-4o-mini-realtime-preview` | 2024-12-17      | No earlier than July 2, 2025       |                                      |
+| `gpt-4o-realtime-preview`      | 2024-12-17      | No earlier than July 2, 2025       |                                      |
+| `gpt-4o-audio-preview`         | 2024-12-17      | No earlier than July 2, 2025       |                                      |
+| `gpt-4o-audio-preview`         | 2024-12-17      | No earlier than July 2, 2025       |                                      |
+| `gpt-4o-transcribe`            | 2025-03-20      | No earlier than August 11, 2025    |                                      |
+| `gpt-4o-mini-tts`              | 2025-03-20      | No earlier than August 11, 2025    |                                      |
+| `gpt-4o-mini-transcribe`       | 2025-03-20      | No earlier than August 11, 2025    |                                      |
+| `tts`                          | 001             | No earlier than February 1, 2026   |                                      |
+| `tts-hd`                       | 001             | No earlier than February 1, 2026   |                                      |
+| `whisper`                      | 001             | No earlier than February 1, 2026   |                                      |
+
+# [Image & Video](#tab/image)
+
+### Image & video
+
+| Model                          | Version         | Retirement date                    | Replacement model                    |
+| -------------------------------|-----------------|------------------------------------|--------------------------------------|
+| `gpt-image-1`                  | 2025-04-15      | No earlier than August 1, 2025     |                                      |
+| `sora`                         | 2025-05-02      | No earlier than September 15, 2025 |                                      |
+| `dalle-3`                      | 3               | No earlier than September 15, 2025 |                                      |
+
+
+# [Embedding](#tab/embedding)
+
+### Embedding
+
+| Model                          | Version         | Retirement date                    | Replacement model                                    |
+| -------------------------------|-----------------|------------------------------------|------------------------------------------------------|
+| `text-embedding-ada-002`       | 2               | No earlier than April 30, 2026     | `text-embedding-3-small` or `text-embedding-3-large` |
+| `text-embedding-ada-002`       | 1               | No earlier than April 30, 2026     | `text-embedding-3-small` or `text-embedding-3-large` |
+| `text-embedding-3-small`       |                 | No earlier than April 30, 2026     |                                                      |
+| `text-embedding-3-large`       |                 | No earlier than April 30, 2026     |                                                      |
+
+---
+
+We notify all customers with these preview deployments at least 30 days before the start of the upgrades. We publish an upgrade schedule detailing the order of regions and model versions that we follow during the upgrades, and link to that schedule from here.
+
+> [!TIP]
+> **Will a model upgrade happen if the new model version is not yet available in that region?**
+>
+> Yes, even in cases where the latest model version is not yet available in a region, we automatically upgrade deployments during the scheduled upgrade window. For more information, see [Azure OpenAI model versions](/azure/ai-services/openai/concepts/model-versions#will-a-model-upgrade-happen-if-the-new-model-version-is-not-yet-available-in-that-region).
+
+## Fine-tuned models
+
+Fine-tuned models retire in two phases: training and deployment.
+
+All fine-tuned models follow their equivalent base model for **training** retirement. Once retired, a given model is no longer available for fine tuning.
+
+For fine-tuned models made generally available since `gpt-4o-2024-08-06`, **deployment** retirement occurs 1 year after **training** retirement. At deployment retirement, inference and deployment returns error responses.
+
+| Model            | Version     | Training retirement date  | Deployment retirement date       |
+| -----------------|-------------|---------------------------|----------------------------------|
+| `gpt-35-turbo`   | 1106        | At base model retirement  | At training retirement           |
+| `gpt-35-turbo`   | 0125        | At base model retirement  | At training retirement           |
+| `gpt-4o`         | 2024-08-06  | At base model retirement  | One year after training retirement |
+| `gpt-4o-mini`    | 2024-07-18  | At base model retirement  | One year after training retirement |
+| `gpt-4.1`        | 2025-04-14  | At base model retirement  | One year after training retirement |
+| `gpt-4.1-mini`   | 2025-04-14  | At base model retirement  | One year after training retirement |
+| `gpt-4.1-nano`   | 2025-04-14  | At base model retirement  | One year after training retirement |
+| `o4-mini`        | 2025-04-16  | At base model retirement  | One year after training retirement |
+
+## Default model versions
+
+| Model | Current default version | New default version | Default upgrade date |
+|---|---|---|---|
+| `gpt-35-turbo` | 0301 | 0125 | Deployments of versions `0301`, `0613`, and `1106` set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 21, 2025.|
+|  `gpt-4o` | 2024-08-06 | - | - |
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "モデルの引退に関するテーブルの追加"
}
```

### Explanation
このコード変更は、「articles/ai-services/openai/includes/retirement/models.md」ファイルを新たに追加したもので、Azure OpenAIにおけるモデルの引退に関する詳細な情報を提供するテーブルが含まれています。これにより、ユーザーはモデルの引退日や代替モデルについての重要な情報を一目で確認できるようになります。

主な変更点は以下の通りです：

1. **内容の追加**: 112行の情報が新しく追加され、テーブル形式で各モデルの引退に関する詳細が整理されています。これには、モデル名、バージョン、引退日、代替モデルが含まれます。

2. **テーブルセクション**: モデルはテキスト生成、音声、画像・動画、埋め込みといったカテゴリに分かれており、それぞれに関連するモデルの情報がきちんと区分けされています。

3. **引退プロセスの説明**: ファインチューニングされたモデルは、トレーニング引退とデプロイメント引退の2つのフェーズで退役することが説明されています。これにより、ユーザーはモデルが退役する前にどのような対応をするべきか理解しやすくなります。

4. **自動アップグレードの情報**: 新しいモデルバージョンが利用可能でない地域であっても、自動的にアップグレードが行われることが強調されています。

この新機能により、ユーザーはAzure OpenAIで利用されるモデルのライフサイクルをより理解し、引退に向けた計画を立てやすくなると期待されます。


