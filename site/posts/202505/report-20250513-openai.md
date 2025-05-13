---
date: '2025-05-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d064b0a...MicrosoftDocs:6d3cef9
summary: Azure OpenAIサービスに関するドキュメントが大幅に更新され、新しい機能が追加され、重要な情報が改訂されました。新たにAzure OpenAIサービスのREST
  APIに関する作成プレビューリファレンスが追加され、API認証やリクエスト構造についてのガイダンスが提供されます。また、新しいモデルである`gpt-4.1-nano`が追加されたほか、コンテンツフィルターやAPIバージョン情報の更新も行われています。これにより、ユーザーはより精度の高い情報を基に作業を進めることが可能となり、開発者にとって有用なリファレンスとなります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d064b0a...MicrosoftDocs:6d3cef9){target="_blank"}

<format>
# Highlights
Azure OpenAIサービスに関するドキュメントに大規模な更新が行われ、新しい機能の追加や重要な情報の改訂がされています。特に、Azure OpenAIサービスのREST APIに関する新しい作成プレビューリファレンスが追加されたこと、ファインチューニングモデル情報に新しいモデルが追加されたこと、またAPIバージョン情報が最新化されたことが目立ちます。

## New features
- **Azure OpenAI サービス REST API 作成プレビューリファレンス**が新たに追加されました。これにより、APIの認証、リクエスト構造、レスポンス受信の方法についての重要なガイダンスが提供されています。
- **最新の著作権バージョンに関する新しいドキュメント**が追加され、APIの著作権に関する詳細な情報を新たに提供しています。

## Breaking changes
なし

## Other updates
- Azure OpenAIのコンテンツフィルター、ファインチューニングデプロイメント、APIサーフェスに関するドキュメントでの情報更新。
- 新しいモデル`gpt-4.1-nano`の追加。
- モデルマトリックスにおけるデータゾーンおよび標準グローバル情報の更新。
- 目次(`toc.yml`)に、著者用プレビュAPIリファレンスへのリンクを追加。

# Insights
Azure OpenAIサービスのドキュメントにおいて、新たな情報が大幅に追加されると共に、既存の内容が最新情報に基づいてアップデートされました。特に、新しいREST API作成プレビューリファレンスの追加は、開発者にとってAPIを利用する際の重要なリファレンスガイドとして機能します。この追加は、APIを通じたインタラクションをよりスムーズに進めるための手助けとなります。

また、コンテンツフィルターに関する情報更新は、特定のモデル（GPT-image-1モデル）での設定制限について明記することで、ユーザーがエラーを未然に防ぎ、より効果的にサービスを利用できるようにしています。さらに、APIバージョンの更新や、モデルマトリックスにおける地域によるモデルサポートの情報整備は、開発者が適切なリソースを選択・利用するための指針を提供します。

新しいファインチューニングモデル`gpt-4.1-nano`の追加により、ユーザーはプロジェクトに応じて最適なモデルを選択する幅が広がり、より専門的なニーズに対応可能となります。これらの更新は全体として、Azure OpenAIサービスの利用者がより精度の高い情報を基に効率よく作業を進めることを意図しており、企業や開発者にとって非常に有用なアップデートです。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [authoring-reference-preview.md](#item-038539) | new feature | Azure OpenAI サービス REST API 作成プレビューリファレンスの追加 | added | 32 | 0 | 32 | 
| [content-filters.md](#item-6f0627) | minor update | コンテンツフィルターに関する情報の更新 | modified | 3 | 0 | 3 | 
| [fine-tuning-deploy.md](#item-286d57) | minor update | ファインチューニングデプロイメントに関する情報の更新 | modified | 8 | 61 | 69 | 
| [api-surface.md](#item-a25fa2) | minor update | APIサーフェスのバージョン情報の更新 | modified | 2 | 2 | 4 | 
| [latest-authoring.md](#item-f706af) | new feature | 最新の著作権バージョンに関する新しいドキュメントの追加 | added | 6392 | 0 | 6392 | 
| [fine-tune-models.md](#item-2aadea) | minor update | 新しいモデル `gpt-4.1-nano` の追加 | modified | 1 | 0 | 1 | 
| [datazone-standard.md](#item-188333) | minor update | データゾーンの標準に関するモデルマトリックスの更新 | modified | 15 | 15 | 30 | 
| [standard-global.md](#item-17a84b) | minor update | 標準グローバルモデルマトリックスの更新 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c945af) | minor update | 目次に著者用プレビュAPIのリファレンスを追加 | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/ai-services/openai/authoring-reference-preview.md{#item-038539}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,32 @@
+---
+title: Azure OpenAI Service REST API authoring preview reference
+titleSuffix: Azure OpenAI
+description: Learn how to use Azure OpenAI's latest authoring preview REST API. In this article, you learn about authorization options,  how to structure a request and receive a response.
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: conceptual
+ms.date: 03/25/2025
+author: mrbullwinkle
+ms.author: mbullwin
+recommendations: false
+ms.custom:
+---
+
+# Azure OpenAI Service authoring REST API preview reference
+
+This article provides details on the inference REST API endpoints for Azure OpenAI.
+
+[!INCLUDE [API surfaces](./includes/api-surface.md)]
+
+## Data plane authoring
+
+The rest of the article covers the latest preview release of the Azure OpenAI data plane inference specification, `2025-04-01-preview`.
+
+If you're looking for documentation on the latest GA API release, refer to the [latest GA data plane inference API](./reference.md)
+
+[!INCLUDE [API surfaces](./includes/api-versions/latest-authoring.md)]
+
+## Next steps
+
+Learn about [Models, and fine-tuning with the REST API](/rest/api/azureopenai/fine-tuning).
+Learn more about the [underlying models that power Azure OpenAI](./concepts/models.md).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAI サービス REST API 作成プレビューリファレンスの追加"
}
```

### Explanation
このコードの変更は、Azure OpenAI サービスの最新の作成プレビュー REST API に関する新しいドキュメントが追加されたことを示しています。追加された内容は32行で構成され、APIの認証オプション、リクエストの構造、レスポンスの受信方法について説明しています。

新しいドキュメントには、次の主要なセクションがあります：
- **データプレーン作成**: Azure OpenAI のデータプレーン推論仕様についての最新情報が記載されています。
- **推奨事項**: ユーザーが最新の GA API のリリースに関する情報を見つけるためのリンクが含まれています。
- **次のステップ**: モデルや REST API を使用したファインチューニングに関する学習資料へのリンクが提供されています。

この変更は、Azure OpenAI サービスに対する重要なリファレンスを提供し、ユーザーが新しい機能を利用できるようにすることを目的としています。

## articles/ai-services/openai/how-to/content-filters.md{#item-6f0627}

<details>
<summary>Diff</summary>
````diff
@@ -24,6 +24,9 @@ Jailbreak risk detection and protected text and code models are optional and on
 > [!NOTE]
 > All customers have the ability to modify the content filters and configure the severity thresholds (low, medium, high). Approval is required for turning the content filters partially or fully off. Managed customers only may apply for full content filtering control via this form: [Azure OpenAI Limited Access Review: Modified Content Filters](https://ncv.microsoft.com/uEfCgnITdR). At this time, it is not possible to become a managed customer.
 
+> [!IMPORTANT]
+> The GPT-image-1 model does not support content filtering configuration: only the default content filter is used.
+
 Content filters can be configured at the resource level. Once a new configuration is created, it can be associated with one or more deployments. For more information about model deployment, see the [resource deployment guide](create-resource.md).
 
 ## Prerequisites
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルターに関する情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAI のコンテンツフィルターに関するドキュメントに重要な注意事項を追加したことを示しています。具体的には、GPT-image-1モデルに関してはコンテンツフィルターの設定がサポートされておらず、デフォルトのコンテンツフィルターのみが使用されるという情報が明記されました。

変更点は次の通りです：
- コンテンツフィルターを使用する際のエクスプレスな重要性についての注意書きが追加されました。
- 他の記述はそのままで、コンテンツフィルターがリソースレベルで設定できる旨や新しい設定の作成後にデプロイメントに関連付けることができるという情報も保持されています。

この更新は、ユーザーが特定のモデルにおけるフィルター設定の制限を理解し、適切に利用するのに役立つことを目的としています。

## articles/ai-services/openai/how-to/fine-tuning-deploy.md{#item-286d57}

<details>
<summary>Diff</summary>
````diff
@@ -366,81 +366,28 @@ Azure OpenAI fine-tuning supports the following deployment types.
 |GPT-35-Turbo-1106-finetune|East US2, North Central US, Sweden Central, Switzerland West|
 |GPT-35-Turbo-0125-finetune|East US2, North Central US, Sweden Central, Switzerland West|
 
-### Global Standard (preview)
+### Global Standard
+
+[Global standard](./deployment-types.md#global-standard) fine-tuned deployments offer [cost savings](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/), but custom model weights may temporarily be stored outside the geography of your Azure OpenAI resource.
 
 | Models | Region |
 |--|--|
 |GPT-4.1-finetune|East US2, North Central US, and Sweden Central|
 |GPT-4.1-mini-finetune|East US2, North Central US, and Sweden Central|
+|GPT-4.1-nano-finetune|East US2, North Central US, and Sweden Central|
 |GPT-4o-finetune|East US2, North Central US, and Sweden Central|
 |GPT-4o-mini-finetune|East US2, North Central US, and Sweden Central|
 
-[Global standard](./deployment-types.md#global-standard) fine-tuned deployments offer [cost savings](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/), but custom model weights may temporarily be stored outside the geography of your Azure OpenAI resource.
-
 :::image type="content" source="../media/fine-tuning/global-standard.png" alt-text="Screenshot of the global standard deployment user experience with a fine-tuned model." lightbox="../media/fine-tuning/global-standard.png":::
 
-### Provisioned Managed (preview)
+### Provisioned Managed
 
 | Models | Region |
 |--|--|
-|GPT-4o-finetune|North Central US, Switzerland West|
-|GPT-4o-mini-finetune|North Central US, Switzerland West|
-
-- `gpt-4o-mini-2024-07-18`
-- `gpt-4o-2024-08-06`
-
-[Provisioned managed](./deployment-types.md#provisioned) fine-tuned deployments offer [predictable performance](../concepts/provisioned-throughput.md) for fine-tuned deployments. As part of public preview, provisioned managed deployments may be created regionally via the data-plane [REST API](../reference.md#data-plane-inference) version `2024-10-01` or newer. See below for examples.
-
-#### Creating a Provisioned Managed deployment
-
-To create a new deployment, make an HTTP PUT call via the [Deployments - Create or Update REST API](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true). The approach is similar to performing [cross region deployment](#cross-region-deployment) with the following exceptions:
-
-- You must provide a `sku` name of `ProvisionedManaged`.
-- The capacity must be declared in PTUs.
-- The `api-version` must be `2024-10-01` or newer.
-- The HTTP method should be `PUT`.
-
-For example, to deploy a gpt-4o-mini model:
-
-```bash
-curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-01" \
-  -H "Authorization: Bearer <TOKEN>" \
-  -H "Content-Type: application/json" \
-  -d '{
-    "sku": {"name": "ProvisionedManaged", "capacity": 25},
-    "properties": {
-        "model": {
-            "format": "OpenAI",
-            "name": "gpt-4omini-ft-model-name",
-            "version": "1",
-            "source": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/{SourceResourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{SourceAOAIAccountName}"
-        }
-    }
-  }'
-```
-
-#### Scaling a fine-tuned model on Provisioned Managed
+|GPT-4o-finetune|North Central US, Sweden Central|
+|GPT-4o-mini-finetune|North Central US, Sweden Central|
 
-To scale a fine-tuned provision managed deployment to increase or decrease PTU capacity, perform the same `PUT` REST API call as you did when [creating the deployment](#creating-a-provisioned-managed-deployment) and provide an updated `capacity` value for the `sku`. Keep in mind, provisioned deployments must scale in [minimum increments](../how-to/provisioned-throughput-onboarding.md#how-much-throughput-per-ptu-you-get-for-each-model).
-
-For example, to scale the model deployed in the previous section from 25 to 40 PTU, make another `PUT` call and increase the capacity:
-
-```bash
-curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-01" \
-  -H "Authorization: Bearer <TOKEN>" \
-  -H "Content-Type: application/json" \
-  -d '{
-    "sku": {"name": "ProvisionedManaged", "capacity": 40},
-    "properties": {
-        "model": {
-            "format": "OpenAI",
-            "name": "gpt-4omini-ft-model-name",
-            "version": "1",
-            "source": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/{SourceResourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{SourceAOAIAccountName}"
-        }
-    }
-  }'
-```
+[Provisioned managed](./deployment-types.md#provisioned) fine-tuned deployments offer [predictable performance](../concepts/provisioned-throughput.md) for latency-sensitive agents and applications. They use the same regional provisioned throughput (PTU) capacity as base models, so if you already have regional PTU quota you can deploy your fine-tuned model in support regions.
 
 ## Clean up your deployment
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングデプロイメントに関する情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのファインチューニングデプロイメントに関する文書の修正を反映しています。この更新では、既存の情報が整理され、新たに重要な適用方法やモデルの選択肢が強調されています。

主な変更点は次の通りです：
- "Global Standard" および "Provisioned Managed" セクションのタイトルが修正され、プレビューから本リリースへと変更されました。
- 各デプロイメントタイプに対応するモデルのリストが見直され、特定の地域における利用可能性が再確認されています。
- "Provisioned Managed" のデプロイメントが、レイテンシーに敏感なエージェントやアプリケーション用に予測可能なパフォーマンスを提供すると説明が追加されています。

これにより、ファインチューニングデプロイメントを利用する開発者が、選択肢や適用の手引きをより理解しやすくなっています。また、ドキュメントの冗長性が減少し、必要な情報が整理されているため、ユーザーにとって利便性が向上しています。

## articles/ai-services/openai/includes/api-surface.md{#item-a25fa2}

<details>
<summary>Diff</summary>
````diff
@@ -22,8 +22,8 @@ Each API surface/specification encapsulates a different set of Azure OpenAI capa
 | API | Latest preview release | Latest GA release | Specifications | Description |
 |:---|:----|:----|:----|:---|
 | **Control plane** | [`2024-06-01-preview`](/rest/api/aiservices/accountmanagement/operation-groups?view=rest-aiservices-accountmanagement-2024-06-01-preview&preserve-view=true) | [`2024-10-01`](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices) | Azure OpenAI shares a common control plane with all other Azure AI Services. The control plane API is used for things like [creating Azure OpenAI resources](/rest/api/aiservices/accountmanagement/accounts/create?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), [model deployment](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), and other higher level resource management tasks. The control plane also governs what is possible to do with capabilities like Azure Resource Manager, Bicep, Terraform, and Azure CLI.|
-| **Data plane - authoring** | `2025-03-01-preview` | `2024-10-21` | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
-| **Data plane - inference** | [`2025-03-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-10-21`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, audio, on your data, Dall-e, assistants, etc. |
+| **Data plane - authoring** | `2025-04-01-preview` | `2024-10-21` | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
+| **Data plane - inference** | [`2025-04-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-10-21`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, audio, on your data, Dall-e, assistants, etc. |
 
 ## Authentication
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIサーフェスのバージョン情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのAPIサーフェスに関するドキュメントにおけるバージョン情報の修正を示しています。具体的には、データプレーンの「著作権」および「推論」に関するAPIのプレビューおよびGA（一般提供）版の日付が更新されました。

主な変更点は次の通りです：
- **Data plane - authoring** のプレビュー版が `2025-03-01-preview` から `2025-04-01-preview` に変更されました。
- **Data plane - inference** のプレビュー版も同様に `2025-03-01-preview` から `2025-04-01-preview` に更新されています。

この修正により、ユーザーは最新のAPIバージョン情報にアクセスできるようになり、サービスの利用準備が整いやすくなります。また、全体的に文書が最新の情報に基づいて更新されることで、開発者が正確な情報をもとに作業を進められるよう支援しています。

## articles/ai-services/openai/includes/api-versions/latest-authoring.md{#item-f706af}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "最新の著作権バージョンに関する新しいドキュメントの追加"
}
```

### Explanation
このコードの変更は、Azure OpenAIの最新の著作権バージョンに関する新しいドキュメントファイルが追加されたことを示しています。追加されたファイルは、APIの著作権に関する詳細な情報を提供することを目的としており、合計で6392行の新しい内容が含まれています。

主なポイントは次の通りです：
- 新しいドキュメントは、著作権に関するAPI版本に関する完全な情報を集約しており、開発者にとって今後の開発に役立つリソースとなります。
- この追加により、ユーザーはAzure OpenAIの最新機能や、全体的なAPIの利用方法に関する詳細なガイダンスを得ることができます。

この新機能により、開発者は新しいAPIの機能を迅速に理解し、実装するための基盤が整います。また、ドキュメントが充実することで、ユーザーはより良いサポートとリソースへのアクセスが可能になります。

## articles/ai-services/openai/includes/fine-tune-models.md{#item-2aadea}

<details>
<summary>Diff</summary>
````diff
@@ -23,3 +23,4 @@ manager: nitinme
 | `gpt-4o` (2024-08-06) | East US2 <br> North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 65,536 | Oct 2023 | Text & Vision to Text |
 | `gpt-4.1` (2025-04-14) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384 <br> Training example context length: 65,536 | May 2024 | Text & Vision to Text |
 | `gpt-4.1-mini` (2025-04-14) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384 <br> Training example context length: 65,536 | May 2024 | Text to Text |
+| `gpt-4.1-nano` (2025-04-14) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384 <br> Training example context length: 32,768 | May 2024 | Text to Text |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいモデル `gpt-4.1-nano` の追加"
}
```

### Explanation
このコードの変更は、Azure OpenAIのファインチューニングモデルに関するドキュメントにおいて、新しいモデル `gpt-4.1-nano` の情報が追加されたことを示しています。この更新により、ユーザーは新しいモデルの仕様と利用可能なオプションについての知識を得ることができます。

具体的な変更内容は以下の通りです：
- `gpt-4.1-nano` モデルが追加され、その詳細な情報が表に含まれています。このモデルの入力サイズは128,000、出力サイズは16,384、トレーニング例のコンテキスト長は32,768 です。
- モデルのリリース日として2025年4月14日が指定されています。

この更新により、開発者は利用可能な新しいファインチューニングモデルを把握し、今後のプロジェクトに役立てることができるようになります。新しいモデルの追加は、ユーザーにとって機能の選択肢を広げ、特定のニーズに合わせた最適なモデルを選ぶ手助けとなります。

## articles/ai-services/openai/includes/model-matrix/datazone-standard.md{#item-188333}

<details>
<summary>Diff</summary>
````diff
@@ -9,18 +9,18 @@ ms.custom: references_regions
 ms.date: 04/02/2025
 ---
 
-| **Region**     | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-nano**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:---------------------------:|:--------------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
-| eastus             | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus2            | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| francecentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| italynorth         | ✅                        | ✅                             | ✅                        | ✅                   | -                      | -                      | ✅                       | ✅                            |
-| northcentralus     | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| polandcentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southcentralus     | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| spaincentral       | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westeurope         | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus             | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
+| **Region**     | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-nano**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:---------------------------:|:--------------------------------:|:--------------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
+| eastus             | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus2            | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                        | ✅                             | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                        | ✅                             | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| italynorth         | ✅                        | ✅                             | -                            | ✅                        | ✅                   | -                      | -                      | ✅                       | ✅                            |
+| northcentralus     | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                        | ✅                             | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                        | ✅                             | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                        | ✅                             | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                        | ✅                             | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                        | ✅                             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データゾーンの標準に関するモデルマトリックスの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのモデルマトリックスに関連するドキュメントで、データゾーンの標準に関する部分が更新されたことを示しています。具体的には、一部のモデルに関する情報が修正され、利用可能なリージョンに対するサポートが明確にされています。

主な更新点は以下の通りです：
- 表の列に `gpt-4.1-mini` モデルが追加されました。
- 一部のリージョンにおいて特定のモデルのサポート状況が変更されています。例えば、以前は対応していたモデルがいくつかのリージョンで非対応になっています（例: `francecentral` や `germanywestcentral` におけるいくつかのモデルの対応状況の変更）。
- 各リージョンで利用可能なモデルのリストは、開発者がどのモデルをどのリージョンで使用できるかを把握するための重要な情報であるため、この更新はユーザーにとって価値があります。

この変更により、ユーザーは最新のモデルのサポート状態を理解し、適切なリージョンでのモデルの選択ができるようになります。これは、開発環境を整える上で大変重要な更新です。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -35,4 +35,4 @@ ms.date: 04/17/2025
 | uksouth            | -                  | -                       | -                           | ✅                        | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | westeurope         | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | westus             | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| westus3            | -                  | -                       | ✅                            | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| westus3            | -                  | -                       | ✅                            | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準グローバルモデルマトリックスの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIの標準グローバルモデルマトリックスに関するドキュメントの更新を示しています。具体的には、`westus3` リージョンにおける特定のモデルのサポート状況が修正されました。

主な更新点は以下の通りです：
- `westus3` リージョンにおけるモデルの列において、ユーザーの利用状況を反映した小さな調整が行われています。
- この変更により、`westus3` リージョンでのモデルの利用可能状況が再確認され、情報が統一されました。

この修正は、開発者が特定のリージョンで利用可能なモデルについて正確な情報を得るために重要です。変更された表形式のデータは、どのモデルがどのリージョンで使えるかを確認する際の重要なリファレンスとなります。この更新により、ユーザーはより判断しやすくなり、ニーズに合ったモデルを選択できるようになります。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -314,6 +314,8 @@ items:
   items:
     - name: Inference GA API reference
       href: reference.md
+    - name: Authoring preview API reference
+      href: authoring-reference-preview.md
     - name: Inference preview API reference
       href: reference-preview.md
     - name: Assistants API Reference
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次に著者用プレビュAPIのリファレンスを追加"
}
```

### Explanation
このコードの変更は、Azure OpenAIの目次ファイル（`toc.yml`）において、著者用プレビュAPIリファレンスへのリンクを追加したことを示しています。具体的には、次の二つの行が追加されました：

1. `"Authoring preview API reference"`という名前の項目が追加され、そのリンクが`authoring-reference-preview.md`に設定されました。
2. これにより、目次内で著者用プレビュAPIリファレンスを簡単に参照できるようになりました。

この変更は、利用者に対して新しいコンテンツへのアクセスを提供し、特に開発者や著者がプレビュAPIの詳細を確認する際に役立ちます。目次の一部として追加されたこの情報は、ユーザーのナビゲーションを向上させ、リファレンス資料を見つけやすくする価値ある更新です。


