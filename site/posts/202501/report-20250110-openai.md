---
date: '2025-01-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6c9883f...MicrosoftDocs:1227d31
summary: 本変更は、Azure OpenAIの文書に関する多くの更新を含んでいます。特に、アシスタントの応答形式の詳細、新しい`o1`モデルに関する情報、モデルの廃止予定や更新日程に関する調整が行われました。これにより、ユーザーに正確で役立つ情報を提供し、開発者がプラットフォームの機能を最大限に活用できるようにすることを目指しています。特に、応答形式に関する情報の追加は、開発者が設計や統合を円滑に行うのに寄与し、ユーザーエクスペリエンスの向上につながります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6c9883f...MicrosoftDocs:1227d31){target="_blank"}

# Highlights
本変更は、Azure OpenAIの文書に対して、アシスタントの応答形式、モデルの廃止情報、モデルバージョン、モデルの説明、クォータおよび制限に関する情報などが更新されたことを含む、各種の細かい修正と更新が行われたものです。新機能として、アシスタントの応答形式の詳細や、新しい`o1`モデルの情報が追加されました。また、いくつかのモデルの廃止や更新の予定に関する情報が調整されました。これらの更新により、ユーザーに最新の、正確で役立つ情報が提供されることを目指しています。

## New features
- アシスタントの応答形式に関する詳細情報の追加。
- `o1`モデルに対する新しいリンクが追加され、関連情報へのアクセスが容易に。

## Breaking changes
- 特になし

## Other updates
- モデルの廃止予定や更新日程に関する情報が調整されました。
- クォータ管理と制限に関する文書が更新され、最新情報が反映されました。

# Insights
この一連の更新は、Azure OpenAIの様々な文書がより正確で使いやすいものとなることを目指しています。特に、アシスタントの応答形式に関する詳細や、モデルの廃止・更新情報をより明確にすることで、開発者やユーザーがプラットフォームの機能を最大限に活用できるよう支援することが狙いです。

具体的には、アシスタントの応答形式への詳細追加は、開発者が応答形式を適切に設計し、外部ツールとシームレスに統合するのに役立ちます。こうした情報が加わることで、開発者はエラーを減らし、ユーザーエクスペリエンスを向上させることが容易になります。

モデル関連では、廃止モデルの自動更新情報や新モデルの追加が行われ、それらのリリーススケジュールが調整されています。この微調整は、Azure OpenAIの使用において誤解や不便さを減らし、現行のインフラストラクチャーにスムーズに移行できるようにする意図があります。

クォータに関する文書更新では、利用者が現在の制限を理解し要件を満たすために必要な手続きをより迅速に行えるようにするための改善がなされています。この総合的なドキュメントの更新は、全体としてAzure OpenAIサービスの採用と運用をより円滑にする一助となっています。こうした更新活動は、ユーザーが最新の情報にアクセスし、Azureプラットフォームを効果的に利用する上で非常に重要です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [assistants-reference.md](#item-52344f) | minor update | アシスタントの応答形式とツールリソースに関する詳細の追加 | modified | 56 | 0 | 56 | 
| [model-retirements.md](#item-03fc2e) | minor update | モデルの廃止と更新に関する情報の調整 | modified | 10 | 3 | 13 | 
| [model-versions.md](#item-304d14) | minor update | モデルバージョンに関する情報の更新 | modified | 12 | 4 | 16 | 
| [models.md](#item-db2c37) | minor update | o1モデルの説明に対するリンクの追加 | modified | 1 | 1 | 2 | 
| [quota.md](#item-9440c2) | minor update | クォータに関するガイドラインの更新 | modified | 18 | 14 | 32 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータおよび制限に関する文書の更新 | modified | 11 | 11 | 22 | 


# Modified Contents
## articles/ai-services/openai/assistants-reference.md{#item-52344f}

<details>
<summary>Diff</summary>
````diff
@@ -42,6 +42,62 @@ Create an assistant with a model and instructions.
 | response_format | string or object | Optional | Specifies the format that the model must output. Compatible with GPT-4 Turbo and all GPT-3.5 Turbo models since gpt-3.5-turbo-1106. Setting this parameter to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON. Importantly, when using JSON mode, you must also instruct the model to produce JSON yourself using a system or user message. Without this instruction, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Additionally, the message content may be partially cut off if you use `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length. |
 | tool_resources | object | Optional | A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs. |
 
+### response_format types
+
+**string**
+
+`auto` is the default value.
+
+**object**
+
+Possible `type` values: `text`, `json_object`, `json_schema`.
+
+***json_schema***
+
+| Name | Type | Description | Default | Required/Optional |
+|---  |---   |---       |--- |--- |
+| `description` | string | A description of what the response format is for, used by the model to determine how to respond in the format. |  | Optional |
+| `name` | string | The name of the response format. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. |  | Required |
+| `schema` | object | The schema for the response format, described as a JSON Schema object. |  | Optional |
+| `strict` | boolean or null | Whether to enable strict schema adherence when generating the output. If set to true, the model will always follow the exact schema defined in the `schema` field. Only a subset of JSON Schema is supported when `strict` is `true`. | false | Optional |
+
+### tool_resources properties
+
+**code_interpreter**
+
+| Name | Type | Description | Default |
+|---  |---   |---       |--- |
+| `file_ids` | array | A list of file IDs made available to the code_interpreter tool. There can be a maximum of 20 files associated with the tool. | `[]` |
+
+**file_search**
+
+| Name | Type | Description | Required/Optional |
+|---  |---   |---       |--- |
+| `vector_store_ids` | array | The vector store attached to this thread. There can be a maximum of 1 vector store attached to the thread. | Optional | 
+| `vector_stores` | array | A helper to create a vector store with file_ids and attach it to this thread. There can be a maximum of 1 vector store attached to the thread. | Optional |
+
+***vector_stores***
+
+| Name | Type | Description | Required/Optional |
+|---  |---   |---       |--- |
+| `file_ids` | array | A list of file IDs to add to the vector store. There can be a maximum of 10000 files in a vector store. | Optional | 
+| `chunking_strategy` | object | The chunking strategy used to chunk the file(s). If not set, will use the auto strategy. | Optional |
+| `metadata` | map | Set of 16 key-value pairs that can be attached to a vector store. This can be useful for storing additional information about the vector store in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long. | Optional |
+
+***chunking_strategy***
+
+| Name | Type | Description | Required/optional | 
+|---  |---   |---       |---|
+| `Auto Chunking Strategy` | object | The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`. `type` is always `auto` | Required |
+| `Static Chunking Strategy` | object | `type` Always `static`  | Required |
+
+***Static Chunking Strategy***
+
+| Name | Type | Description | Required/Optional |
+|---  |---   |---       |--- |
+| `max_chunk_size_tokens` | integer | The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`. | Required |
+| `chunk_overlap_tokens` | integer | The number of tokens that overlap between chunks. The default value is `400`. Note that the overlap must not exceed half of `max_chunk_size_tokens`. | Required |
+
 ### Returns
 
 An [assistant](#assistant-object) object.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アシスタントの応答形式とツールリソースに関する詳細の追加"
}
```

### Explanation
この変更は、アシスタントの応答形式とツールリソースに関する情報を明確化するために、`assistants-reference.md`文書に対して行われました。具体的には、応答形式の種類に関する詳細やツールリソースのプロパティに関するセクションが新たに追加されました。これにより、利用者がアシスタントを作成する際の設定やオプションを理解しやすくなります。加えて、JSONスキーマに基づく厳密な応答構造や、それに対するさまざまな設定オプションに関する具体的な情報が提供され、開発者がアシスタントを活用する際の利便性が向上しました。この変更は56行の追加を含むもので、0行の削除があり、全体の変更は56行です。

## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 12/02/2024
+ms.date: 01/09/2025
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -98,15 +98,16 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-35-turbo` | 0301 | February 13, 2025<br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025.   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
 | `gpt-35-turbo`<br>`gpt-35-turbo-16k` | 0613 | February 13, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025.  | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
 | `gpt-35-turbo` | 1106 | No earlier than March 31, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
-| `gpt-35-turbo` | 0125 | No earlier than March 31, 2025 | `gpt-4o-mini` |
+| `gpt-35-turbo` | 0125 | No earlier than May 31, 2025 | `gpt-4o-mini` |
 | `gpt-4`<br>`gpt-4-32k` | 0314 | June 6, 2025 | `gpt-4o` |
 | `gpt-4`<br>`gpt-4-32k` | 0613 | June 6, 2025 | `gpt-4o` |
 | `gpt-4` | 1106-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025 **<sup>1</sup>** | `gpt-4o`|
 | `gpt-4` | 0125-preview |To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025 **<sup>1</sup>**  | `gpt-4o` |
 | `gpt-4` | vision-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025  **<sup>1</sup>** | `gpt-4o`|
 | `gpt-4o` | 2024-05-13 | No earlier than May 20, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on February 13, 2025. | |
 | `gpt-4o-mini` | 2024-07-18 | No earlier than July 18, 2025  | |
-| `gpt-3.5-turbo-instruct` | 0914 | No earlier than February 1, 2025 |  |
+| `gpt-3.5-turbo-instruct` | 0914 | No earlier than April 1, 2025 |  |
+| `o1` | 2024-12-17 | No earlier than December 17, 2025 | |
 | `text-embedding-ada-002` | 2 | No earlier than October 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
 | `text-embedding-ada-002` | 1 | No earlier than October 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
 | `text-embedding-3-small` | | No earlier than October 3, 2025 | |
@@ -162,6 +163,12 @@ If you're an existing customer looking for information about these models, see [
 
 ## Retirement and deprecation history
 
+## January 9, 2025
+
+- `o1` added.
+- `gpt-35-turbo instruct` updated to no earlier than April 1, 2025.
+- `gpt-35-turbo` (0125) updated to no earlier than May 31, 2025.
+
 ## December 11, 2024
 
 Embeddings models updated to no earlier than October 3, 2025.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの廃止と更新に関する情報の調整"
}
```

### Explanation
この変更は、`model-retirements.md`文書において、Azure OpenAIに関連するモデルの廃止や更新日程に関する情報を調整するために行われました。具体的には、いくつかのモデルのデフォルトの自動アップデートが行われる日時が変更され、さらに新たに`o1`モデルが追加されました。また、`gpt-35-turbo`のバージョン0125の更新予定も、従来の日時から2025年5月31日以降に変更されました。この変更には、10行の追加と3行の削除が含まれており、合計で13行の変更が行われています。このように、文書の内容を最新の状況に合わせて更新することで、ユーザーに正確で信頼性のある情報を提供することを目的としています。

## articles/ai-services/openai/concepts/model-versions.md{#item-304d14}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about model versions in Azure OpenAI. 
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 09/20/2024
+ms.date: 01/09/2025
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
 ms.author: mbullwin #chrhoder
@@ -17,7 +17,7 @@ Azure OpenAI Service is committed to providing the best generative AI models for
 
 ## How model versions work
 
-We want to make it easy for customers to stay up to date as models improve.  Customers can choose to start with a particular version and to automatically update as new versions are released.
+We want to make it easy for customers to stay up to date as models improve. Customers can choose to start with a particular version and to automatically update as new versions are released.
 
 When you deploy a model you can choose an update policy, which can include the following options:
 
@@ -27,17 +27,25 @@ When you deploy a model you can choose an update policy, which can include the f
 
 ## How Azure updates OpenAI models
 
-Azure works closely with OpenAI to release new model versions.  When a new version of a model is released, a customer can immediately test it in new deployments.  Azure publishes when new versions of models are released, and notifies customers at least two weeks before a new version becomes the default version of the model.   Azure also maintains the previous major version of the model until its retirement date, so customers can switch back to it if desired.
+Azure works closely with OpenAI to release new model versions. When a new version of a model is released, a customer can immediately test it in new deployments. Azure publishes when new versions of models are released, and notifies customers at least two weeks before a new version becomes the default version of the model.   Azure also maintains the previous major version of the model until its retirement date, so customers can switch back to it if desired.
 
 ## What you need to know about Azure OpenAI model version upgrades
 
-As a customer of Azure OpenAI models, you might notice some changes in the model behavior and compatibility after a version upgrade.  These changes might affect your applications and workflows that rely on the models.  Here are some tips to help you prepare for version upgrades and minimize the impact:
+As a customer of Azure OpenAI models, you might notice some changes in the model behavior and compatibility after a version upgrade. These changes might affect your applications and workflows that rely on the models. Here are some tips to help you prepare for version upgrades:
 
 * Read [what’s new](../whats-new.md) and [models](../concepts/models.md) to understand the changes and new features.
 * Read the documentation on [model deployments](../how-to/create-resource.md) and [version upgrades](../how-to/working-with-models.md) to understand how to work with model versions.
 * Test your applications and workflows with the new model version after release.
 * Update your code and configuration to use the new features and capabilities of the new model version.
 
+### Will a model upgrade happen if the new model version is not yet available in that region?
+
+Yes, even in cases where the latest model version is not yet available in a region, we will automatically 
+upgrade deployments during the scheduled upgrade window. Our engineering team will begin rollout of the new model version starting on the announced 
+upgrade date. For example, if `gpt-35-turbo-0125` is not yet available in Japan East, we will deploy it to Japan East to upgrade older model 
+versions as part of the default model version upgrade process. 
+
+
 ## Next Steps
 
 - [Learn more about working with Azure OpenAI models](../how-to/working-with-models.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルバージョンに関する情報の更新"
}
```

### Explanation
この変更は、`model-versions.md`文書に対して行われ、Azure OpenAIにおけるモデルバージョンに関する最新情報を反映するためのものです。主な更新内容には、最終更新日が2024年9月20日から2025年1月9日に変更されたことが含まれています。また、モデルのアップデートポリシーや、Azureが新しいモデルバージョンをリリースする際のプロセスに関する説明が改訂されました。そして、新たに「地域で新しいモデルバージョンが利用できない場合のアップグレード」についての情報が追加され、モデルの自動アップグレードに関する詳細が提供されました。これにより、ユーザーがモデルのバージョン管理とアップデートの仕組みをより理解しやすくなることを目指しています。この変更には12行の追加と4行の削除があり、合計で16行の変更が行われています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ The Azure OpenAI `o1` and `o1-mini` models are specifically designed to tackle r
 
 |  Model ID  | Description | Max Request (tokens) | Training Data (up to)  |
 |  --- |  :--- |:--- |:---: |
-| `o1` (2024-12-17) | The most capable model in the o1 series, offering enhanced reasoning abilities. <br> **Request access: [limited access model application](https://aka.ms/OAI/o1access)** <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools <br> | Input: 200,000 <br> Output: 100,000 | |  
+| `o1` (2024-12-17) | The most capable model in the o1 series, offering [enhanced reasoning abilities](../how-to/reasoning.md). <br> - Structured outputs<br> - Text, image processing <br> - Functions/Tools <br> <br> **Request access: [limited access model application](https://aka.ms/OAI/o1access)** | Input: 200,000 <br> Output: 100,000 | Oct 2023 |  
 |`o1-preview` (2024-09-12) | Older preview version | Input: 128,000  <br> Output: 32,768 | Oct 2023 |
 | `o1-mini` (2024-09-12) | A faster and more cost-efficient option in the o1 series, ideal for coding tasks requiring speed and lower resource consumption.| Input: 128,000  <br> Output: 65,536 | Oct 2023 |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "o1モデルの説明に対するリンクの追加"
}
```

### Explanation
この変更は、`models.md`文書において、Azure OpenAIの`o1`モデルの説明を更新するために行われました。具体的には、`o1`モデルに関する説明に「[強化された推論能力](../how-to/reasoning.md)」へのリンクが追加され、読者がこの機能についてより詳しく理解できるようになっています。また、同時にモデルの説明の形式が若干変更され、情報が整理されました。この修正により、利用者は`o1`モデルの特性をより明確に把握でき、関連情報へのアクセスが容易になります。この変更には1行の追加と1行の削除が含まれ、合計で2行の変更が行われています。

## articles/ai-services/openai/how-to/quota.md{#item-9440c2}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: mrbullwinkle
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 11/04/2024
+ms.date: 01/09/2025
 ms.author: mbullwin
 ---
 
@@ -18,18 +18,18 @@ Quota provides the flexibility to actively manage the allocation of rate limits
 ## Prerequisites
 
 > [!IMPORTANT]
-> For any task that requires viewing available quota we recommend using the **Cognitive Services Usages Reader** role. This role provides the minimal access necessary to view quota usage across an Azure subscription. To learn more about this role and the other roles you will need to access Azure OpenAI, consult our [Azure role-based access (Azure RBAC) guide](./role-based-access-control.md). 
+> For any task that requires viewing available quota we recommend using the **Cognitive Services Usages Reader** role. This role provides the minimal access necessary to view quota usage across an Azure subscription. To learn more about this role and the other roles you will need to access Azure OpenAI, consult our [Azure role-based access control guide](./role-based-access-control.md). 
 >
-> This role can be found in the Azure portal under **Subscriptions** > **Access control (IAM)** > **Add role assignment** > search for **Cognitive Services Usages Reader**.This role **must be applied at the subscription level**, it does not exist at the resource level.
+> This role can be found in the Azure portal under **Subscriptions** > **Access control (IAM)** > **Add role assignment** > search for **Cognitive Services Usages Reader**. This role **must be applied at the subscription level**, it does not exist at the resource level.
 >
 > If you do not wish to use this role, the subscription **Reader** role will provide equivalent access, but it will also grant read access beyond the scope of what is needed for viewing quota and model deployment.
 
 ## Introduction to quota
 
-Azure OpenAI's quota feature enables assignment of rate limits to your deployments, up-to a global limit called your “quota.”  Quota is assigned to your subscription on a per-region, per-model basis in units of **Tokens-per-Minute (TPM)**. When you onboard a subscription to Azure OpenAI, you'll receive default quota for most available models. Then, you'll assign TPM to each deployment as it is created, and the available quota for that model will be reduced by that amount. You can continue to create deployments and assign them TPM until you reach your quota limit. Once that happens, you can only create new deployments of that model by reducing the TPM assigned to other deployments of the same model (thus freeing TPM for use), or by requesting and being approved for a model quota increase in the desired region.
+Azure OpenAI's quota feature enables assignment of rate limits to your deployments, up-to a global limit called your *quota*. Quota is assigned to your subscription on a per-region, per-model basis in units of **Tokens-per-Minute (TPM)**. When you onboard a subscription to Azure OpenAI, you'll receive default quota for most available models. Then, you'll assign TPM to each deployment as it is created, and the available quota for that model will be reduced by that amount. You can continue to create deployments and assign them TPM until you reach your quota limit. Once that happens, you can only create new deployments of that model by reducing the TPM assigned to other deployments of the same model (thus freeing TPM for use), or by requesting and being approved for a model quota increase in the desired region.
 
 > [!NOTE]
-> With a quota of 240,000 TPM for GPT-35-Turbo in East US, a customer can create a single deployment of 240K TPM, 2 deployments of 120K TPM each, or any number of deployments in one or multiple Azure OpenAI resources as long as their TPM adds up to less than 240K total in that region.
+> With a quota of 240,000 TPM for GPT-35-Turbo in East US, a customer can create a single deployment of 240 K TPM, 2 deployments of 120 K TPM each, or any number of deployments in one or multiple Azure OpenAI resources as long as their TPM adds up to less than 240 K total in that region.
 
 When a deployment is created, the assigned TPM will directly map to the tokens-per-minute rate limit enforced on its inferencing requests. A **Requests-Per-Minute (RPM)** rate limit will also be enforced whose value is set proportionally to the TPM assignment using the following ratio:
 
@@ -53,6 +53,10 @@ Post deployment you can adjust your TPM allocation by selecting and editing your
 > [!IMPORTANT]
 > Quotas and limits are subject to change, for the most up-date-information consult our [quotas and limits article](../quotas-limits.md).
 
+## Request more quota
+
+Quota increase requests can be submitted via the [quota increase request form](https://aka.ms/oai/stuquotarequest). Due to high demand, quota increase requests are being accepted and will be filled in the order they're received. Priority is given to customers who generate traffic that consumes the existing quota allocation, and your request might be denied if this condition isn't met.
+
 ## Model specific settings
 
 Different model deployments, also called model classes have unique max TPM values that you're now able to control. **This represents the maximum amount of TPM that can be allocated to that type of model deployment in a given region.** 
@@ -71,7 +75,7 @@ For an all up view of your quota allocations across deployments in a given regio
 - **Deployment**: Model deployments divided by model class.
 - **Quota type**: There's one quota value per region for each model type. The quota covers all versions of that model.  
 - **Quota allocation**: For the quota name, this shows how much quota is used by deployments and the total quota approved for this subscription and region. This amount of quota used is also represented in the bar graph.
-- **Request Quota**: The icon navigates to a form where requests to increase quota can be submitted.
+- **Request Quota**: The icon navigates to [this form](https://aka.ms/oai/stuquotarequest) where requests to increase quota can be submitted.
 
 ## Migrating existing deployments
 
@@ -92,7 +96,7 @@ As requests come into the deployment endpoint, the estimated max-processed-token
 > [!IMPORTANT]
 > The token count used in the rate limit calculation is an estimate based in part on the character count of the API request. The rate limit token estimate is not the same as the token calculation that is used for billing/determining that a request is below a model's input token limit. Due to the approximate nature of the rate limit token calculation, it is expected behavior that a rate limit can be triggered prior to what might be expected in comparison to an exact token count measurement for each request.  
 
-RPM rate limits are based on the number of requests received over time. The rate limit expects that requests be evenly distributed over a one-minute period. If this average flow isn't maintained, then requests may receive a 429 response even though the limit isn't met when measured over the course of a minute. To implement this behavior, Azure OpenAI Service evaluates the rate of incoming requests over a small period of time, typically 1 or 10 seconds. If the number of requests received during that time exceeds what would be expected at the set RPM limit, then new requests will receive a 429 response code until the next evaluation period. For example, if Azure OpenAI is monitoring request rate on 1-second intervals, then rate limiting will occur for a 600-RPM deployment if more than 10 requests are received during each 1-second period (600 requests per minute = 10 requests per second).
+RPM rate limits are based on the number of requests received over time. The rate limit expects that requests be evenly distributed over a one-minute period. If this average flow isn't maintained, then requests might receive a 429 response even though the limit isn't met when measured over the course of a minute. To implement this behavior, Azure OpenAI Service evaluates the rate of incoming requests over a small period of time, typically 1 or 10 seconds. If the number of requests received during that time exceeds what would be expected at the set RPM limit, then new requests will receive a 429 response code until the next evaluation period. For example, if Azure OpenAI is monitoring request rate on 1-second intervals, then rate limiting will occur for a 600-RPM deployment if more than 10 requests are received during each 1-second period (600 requests per minute = 10 requests per second).
 
 ### Rate limit best practices
 
@@ -106,7 +110,7 @@ To minimize issues related to rate limits, it's a good idea to use the following
 
 ## Automate deployment
 
-This section contains brief example templates to help get you started programmatically creating deployments that use quota to set TPM rate limits. With the introduction of quota you must use API version `2023-05-01` for resource management related activities. This API version is only for managing your resources, and does not impact the API version used for inferencing calls like completions, chat completions, embedding, image generation etc.
+This section contains brief example templates to help get you started programmatically creating deployments that use quota to set TPM rate limits. With the introduction of quota you must use API version `2023-05-01` for resource management related activities. This API version is only for managing your resources, and does not impact the API version used for inferencing calls like completions, chat completions, embedding, image generation, etc.
 
 # [REST](#tab/rest)
 
@@ -151,7 +155,7 @@ curl -X PUT https://management.azure.com/subscriptions/00000000-0000-0000-0000-0
 > [!NOTE]
 > There are multiple ways to generate an authorization token. The easiest method for initial testing is to launch the Cloud Shell from the [Azure portal](https://portal.azure.com). Then run [`az account get-access-token`](/cli/azure/account?view=azure-cli-latest#az-account-get-access-token&preserve-view=true). You can use this token as your temporary authorization token for API testing.
 
-For more information, refer to the REST API reference documentation for [usages](/rest/api/aiservices/accountmanagement/usages/list?branch=main&tabs=HTTP) and [deployment](/rest/api/aiservices/accountmanagement/deployments/create-or-update).
+For more information, see the REST API reference documentation for [usages](/rest/api/aiservices/accountmanagement/usages/list?branch=main&tabs=HTTP) and [deployment](/rest/api/aiservices/accountmanagement/deployments/create-or-update).
 
 ### Usage
 
@@ -201,7 +205,7 @@ az cognitiveservices account deployment create --model-format
                                                [--sku]
 ```
 
-To sign into your local installation of the CLI, run the [az login](/cli/azure/reference-index#az-login) command:
+To sign into your local installation of the CLI, run the [`az login`](/cli/azure/reference-index#az-login) command:
 
 ```azurecli
 az login
@@ -231,7 +235,7 @@ az cognitiveservices usage list -l eastus
 
 This command runs in the context of the currently active subscription for Azure CLI. Use `az-account-set --subscription` to [modify the active subscription](/cli/azure/manage-azure-subscriptions-azure-cli#change-the-active-subscription).
 
-For more details on `az cognitiveservices account` and `az cognitivesservices usage` consult the [Azure CLI reference documentation](/cli/azure/cognitiveservices/account/deployment?view=azure-cli-latest&preserve-view=true)
+For more information, see the [Azure CLI reference documentation](/cli/azure/cognitiveservices/account/deployment?view=azure-cli-latest&preserve-view=true)
 
 # [Azure PowerShell](#tab/powershell)
 
@@ -328,7 +332,7 @@ For more details on `New-AzCognitiveServicesAccountDeployment` and `Get-AzCognit
 }
 ```
 
-For more details, consult the [full Azure Resource Manager reference documentation](/azure/templates/microsoft.cognitiveservices/accounts/deployments?pivots=deployment-language-arm-template).
+For more information, see the [full Azure Resource Manager reference documentation](/azure/templates/microsoft.cognitiveservices/accounts/deployments?pivots=deployment-language-arm-template).
 
 # [Bicep](#tab/bicep)
 
@@ -354,7 +358,7 @@ resource arm_je_std_deployment 'Microsoft.CognitiveServices/accounts/deployments
 }
 ```
 
-For more details consult the [full Bicep reference documentation](/azure/templates/microsoft.cognitiveservices/accounts/deployments?pivots=deployment-language-bicep).
+For more information, see the [full Bicep reference documentation](/azure/templates/microsoft.cognitiveservices/accounts/deployments?pivots=deployment-language-bicep).
 
 # [Terraform](#tab/terraform)
 
@@ -430,7 +434,7 @@ resource "azapi_resource" "TERRAFORM-AOAI-STD-DEPLOYMENT" {
 }
 ```
 
-For more details consult the [full Terraform reference documentation](/azure/templates/microsoft.cognitiveservices/accounts/deployments?pivots=deployment-language-terraform).
+For more information, see the [full Terraform reference documentation](/azure/templates/microsoft.cognitiveservices/accounts/deployments?pivots=deployment-language-terraform).
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータに関するガイドラインの更新"
}
```

### Explanation
この変更は、`quota.md`文書において、Azure OpenAIのクォータに関する情報を更新するために行われました。主な更新点は、最終更新日が2024年11月4日から2025年1月9日に変更されたことと、いくつかの文言や表現の整理が行われたことです。特に、クォータ関連の役割の説明や、クォータの増加要求を提出するためのリンクが追加され、利用者が情報にアクセスしやすくなっています。また、いくつかの注意点や重要な情報を強調するために内容が改善されました。これにより、利用者はより明確にAzure OpenAIのクォータ管理について理解できるようになります。この変更は、合計で18行の追加と14行の削除があり、32行の修正が行われています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 11/11/2024
+ms.date: 01/09/2025
 ms.author: mbullwin
 ---
 
@@ -61,26 +61,26 @@ The following sections provide you with a quick guide to the default quotas and
 
 [!INCLUDE [Quota](./includes/global-batch-limits.md)]
 
-## o1-preview & o1-mini rate limits
+## o1 & o1-mini rate limits
 
 > [!IMPORTANT]
 > The ratio of RPM/TPM for quota with o1-series models works differently than older chat completions models:
 >
 > - **Older chat models:** 1 unit of capacity = 6 RPM and 1,000 TPM.
-> - **o1-preview:** 1 unit of capacity = 1 RPM and 6,000 TPM.
+> - **o1 & o1-preview:** 1 unit of capacity = 1 RPM and 6,000 TPM.
 > - **o1-mini:** 1 unit of capacity = 1 RPM per 10,000 TPM.
 >
 > This is particularly important for programmatic model deployment as this change in RPM/TPM ratio can result in accidental under allocation of quota if one is still assuming the 1:1000 ratio followed by older chat completion models.
 >
-> There is a known issue with the [quota/usages API](/rest/api/aiservices/accountmanagement/usages/list?view=rest-aiservices-accountmanagement-2024-06-01-preview&tabs=HTTP&preserve-view=true) where it assumes the old ratio applies to the new o1-series models. The API returns the correct base capacity number, but does not apply the correct ratio for the accurate calculation of TPM.
+> There is a known issue with the [quota/usages API](/rest/api/aiservices/accountmanagement/usages/list?view=rest-aiservices-accountmanagement-2024-06-01-preview&tabs=HTTP&preserve-view=true) where it assumes the old ratio applies to the new o1-series models. The API returns the correct base capacity number, but doesn't apply the correct ratio for the accurate calculation of TPM.
 
-### o1-preview & o1-mini global standard
+### o1 & o1-mini global standard
 
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
 |---|---|:---:|:---:|
-| `o1-preview` | Enterprise agreement | 30 M | 5 K |
+| `o1` & `o1-preview` | Enterprise agreement | 30 M | 5 K |
 | `o1-mini`| Enterprise agreement | 50 M | 5 K |
-| `o1-preview` | Default | 3 M | 500 |
+| `o1` & `o1-preview` | Default | 3 M | 500 |
 | `o1-mini`| Default | 5 M | 500 |
 
 ### o1-preview & o1-mini standard
@@ -134,12 +134,12 @@ M = million | K = thousand
 
 #### Usage tiers
 
-Global standard deployments use Azure's global infrastructure, dynamically routing customer traffic to the data center with best availability for the customer’s inference requests. Similarly, Data zone standard deployments allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. This enables more consistent latency for customers with low to medium levels of traffic. Customers with high sustained levels of usage might see more variability in response latency.
+Global standard deployments use Azure's global infrastructure, dynamically routing customer traffic to the data center with best availability for the customer’s inference requests. Similarly, Data zone standard deployments allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. This enables more consistent latency for customers with low to medium levels of traffic. Customers with high sustained levels of usage might see greater variability in response latency.
 
 The Usage Limit determines the level of usage above which customers might see larger variability in response latency. A customer’s usage is defined per model and is the total tokens consumed across all deployments in all subscriptions in all regions for a given tenant.
 
 > [!NOTE]
-> Usage tiers only apply to standard, data zone standard, and global standard deployment types. Usage tiers do not apply to global batch and provisioned throughput deployments.
+> Usage tiers only apply to standard, data zone standard, and global standard deployment types. Usage tiers don't apply to global batch and provisioned throughput deployments.
 
 #### GPT-4o global standard, data zone standard, & standard
 
@@ -179,9 +179,9 @@ To minimize issues related to rate limits, it's a good idea to use the following
 - Test different load increase patterns.
 - Increase the quota assigned to your deployment. Move quota from another deployment, if necessary.
 
-### How to request increases to the default quotas and limits
+## How to request quota increases
 
-Quota increase requests can be submitted from the [Quotas](./how-to/quota.md) page in the Azure AI Foundry portal. Due to high demand, quota increase requests are being accepted and will be filled in the order they're received. Priority is given to customers who generate traffic that consumes the existing quota allocation, and your request might be denied if this condition isn't met.
+Quota increase requests can be submitted via the [quota increase request form](https://aka.ms/oai/stuquotarequest). Due to high demand, quota increase requests are being accepted and will be filled in the order they're received. Priority is given to customers who generate traffic that consumes the existing quota allocation, and your request might be denied if this condition isn't met.
 
 For other rate limits, [submit a service request](../cognitive-services-support-options.md?context=/azure/ai-services/openai/context/context).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータおよび制限に関する文書の更新"
}
```

### Explanation
この変更は、`quotas-limits.md`文書において、Azure OpenAIのクォータ及び制限に関する情報を更新および整理しました。主な更新点として、`o1-preview`の名称が`o1`に変更され、両者のレート制限に関する情報が統合されています。また、日付が2024年11月11日から2025年1月9日に変更され、最新の情報を反映しています。

さらに、クォータとレート制限の詳細がわかりやすく整理され、リクエスト数やトークン数に関する具体的な制限が明示されています。クォータ増加要求を提出するための手続きも改善され、専用のリンクが追加されました。これにより、ユーザーは必要な情報により迅速にアクセスできるようになり、全体的な文書の可読性と実用性が向上しています。変更は合計で11行の追加と11行の削除があり、合計22行の修正が行われています。


