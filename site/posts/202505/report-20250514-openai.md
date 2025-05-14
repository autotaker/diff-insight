---
date: '2025-05-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6d3cef9...MicrosoftDocs:2a41314
summary: Azure OpenAI APIに関する文書に対する軽微な更新が行われました。主な変更内容は、APIバージョンの非推奨やプレビューリリースの日付の更新、新機能の追加です。具体的には、`GPT-image-1`や評価APIの機能が新たに加わり、最新の推論プレビューAPIバージョンに関する情報とガイダンスが強化されました。また、プレビューリリースの日付が2025年4月1日に更新され、Azure
  API ManagementとOpenAPI 3.1の互換性についての注意点も追加されています。今回の更新は、開発者がAPIをより効果的に活用するために重要な情報を提供しており、特に新しい機能やエンドポイントの理解を促進します。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6d3cef9...MicrosoftDocs:2a41314){target="_blank"}

# ハイライト
変更内容のハイライトは、Azure OpenAI API関連のドキュメントに対する軽微な更新であり、主にAPIバージョンの非推奨やプレビューリリースの日付の更新、新機能の追加について言及しています。また、非推奨バージョンのAPIの使い方に関連する情報も更新されています。

## 新機能
- `GPT-image-1`、評価API、`o3`および`o4-mini`の推論要約追加
- 最新推論プレビューAPIバージョンに関する詳細情報とガイダンスが強化されました

## 破壊的変更
特筆すべき破壊的変更はなし。

## その他の更新
- プレビューリリースの日付が`2025年4月1日`に更新
- Azure API ManagementとOpenAPI 3.1の互換性に関する注意点が追加
- APIサーフェスと使用可能なAPIの概要が最新の情報に基づいて修正

# インサイト
Azure OpenAIサービスに関する最新の情報を開発者に提供し、APIの使用に関して最新の機能と推奨事項を受け取ることで、開発者がより効果的に作業を進められるように配慮されています。

この更新は、特に最新推論プレビューにおけるAPIの進化を示すものであり、開発者にとって更新された機能やエンドポイントを理解し、活用するために重要です。新しいプレビューリリースでは、`GPT-image-1`や評価APIの機能が追加され、開発者がAzureのAI機能をより豊かに利用できるようになったことが示されています。

また、Azure API ManagementとOpenAPI 3.1の互換性に関する既知の問題に触れることで、開発者がAPI仕様を正しく理解し、適切に解析するための実践が促されています。これにより、実際のアプリケーションに新機能を組み込む際に役立つ情報が提供され、全体的にAzure OpenAIサービスの価値を高める役割を果たしていることがわかります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [api-version-deprecation.md](#item-1cad50) | minor update | APIバージョンの非推奨に関する更新 | modified | 12 | 3 | 15 | 
| [api-surface.md](#item-a25fa2) | minor update | APIサーフェスの更新 | modified | 1 | 1 | 2 | 
| [latest-inference-preview.md](#item-24bf0f) | minor update | 最新推論プレビューのAPIバージョン更新 | modified | 538 | 400 | 938 | 


# Modified Contents
## articles/ai-services/openai/api-version-deprecation.md{#item-1cad50}

<details>
<summary>Diff</summary>
````diff
@@ -18,17 +18,20 @@ This article is to help you understand the support lifecycle for the Azure OpenA
 
 
 > [!NOTE]
-> New API response objects may be added to the API response without version changes. We recommend you only parse the response objects you require. 
+> New API response objects may be added to the API response without version changes. We recommend you only parse the response objects you require.
+>
+> The latest Azure OpenAI spec uses OpenAPI 3.1. It is a known issue that this is currently not fully supported by [Azure API Management](/azure/api-management/api-management-key-concepts)
 
 ## Latest preview API releases
 
 Azure OpenAI API latest release:
 
-- Inference: [2025-03-01-preview](reference-preview.md)
-- Authoring: [2025-03-01-preview](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/)
+- Inference: [2025-04-01-preview](reference-preview.md)
+- Authoring: [2025-04-01-preview](authoring-reference-preview.md)
 
 This version contains support for the latest Azure OpenAI features including:
 
+- `GPT-image-1`, the evaluations API, reasoning summary with `o3` and `o4-mini` . [**Added in 2025-04-01-preview**]
 - [Responses API & support for `computer-use-preview` model](./how-to/responses.md) [**Added in 2025-03-01-preview**]
 - [Stored Completions (distillation) API](./how-to/stored-completions.md#stored-completions-api) [**Added in 2025-02-01-preview**]
 - [Predicted Outputs](./how-to/predicted-outputs.md) [**Added in 2025-01-01-preview**]
@@ -44,6 +47,12 @@ This version contains support for the latest Azure OpenAI features including:
 - [Function calling](./how-to/function-calling.md)  [**Added in 2023-07-01-preview**]
 - [Retrieval augmented generation with your data feature](./use-your-data-quickstart.md).  [**Added in 2023-06-01-preview**]
 
+## Changes between 2025-04-01-preview and 2025-03-01-preview
+
+- [`GPT-image-1` support](/azure/ai-services/openai/how-to/dall-e)
+- [Reasoning summary for `o3` and `o4-mini`](/azure/ai-services/openai/how-to/reasoning)
+- [Evaluation API](/azure/ai-services/openai/authoring-reference-preview#evaluation---create)
+
 ## Changes between 2025-03-01-preview and 2025-02-01-preview
 
 - [Responses API](./how-to/responses.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの非推奨に関する更新"
}
```

### Explanation
この変更は、「articles/ai-services/openai/api-version-deprecation.md」ファイルに対するもので、Azure OpenAI APIの最新のプレビューリリースに関する情報を更新しています。主な変更点は、プレビューリリースの日付の更新と、それに関連する新しい機能の追加についての詳細が含まれています。

具体的には、以前は2025年3月1日がリリースされた日時だったのが、2025年4月1日プレビューへの更新が行われました。また、`GPT-image-1`や評価API、`o3`および`o4-mini`の推論要約といった新機能が追加されたことが記述されています。

この変更は、Azure API Managementが現在、OpenAPI 3.1を完全にはサポートしていないという既知の問題にも言及しており、ユーザーがAPIの応答オブジェクトを適切に解析する際の推奨事項を強調しています。全体として、この更新はAPIのサポートライフサイクルに関する重要な情報を提供し、開発者が新機能を利用する際に有益な内容となっています。

## articles/ai-services/openai/includes/api-surface.md{#item-a25fa2}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ Each API surface/specification encapsulates a different set of Azure OpenAI capa
 | API | Latest preview release | Latest GA release | Specifications | Description |
 |:---|:----|:----|:----|:---|
 | **Control plane** | [`2024-06-01-preview`](/rest/api/aiservices/accountmanagement/operation-groups?view=rest-aiservices-accountmanagement-2024-06-01-preview&preserve-view=true) | [`2024-10-01`](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices) | Azure OpenAI shares a common control plane with all other Azure AI Services. The control plane API is used for things like [creating Azure OpenAI resources](/rest/api/aiservices/accountmanagement/accounts/create?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), [model deployment](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), and other higher level resource management tasks. The control plane also governs what is possible to do with capabilities like Azure Resource Manager, Bicep, Terraform, and Azure CLI.|
-| **Data plane - authoring** | `2025-04-01-preview` | `2024-10-21` | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
+| **Data plane - authoring** | [`2025-04-01-preview`](/azure/ai-services/openai/authoring-reference-preview) | `2024-10-21` | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
 | **Data plane - inference** | [`2025-04-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-10-21`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, audio, on your data, Dall-e, assistants, etc. |
 
 ## Authentication
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIサーフェスの更新"
}
```

### Explanation
この変更は、「articles/ai-services/openai/includes/api-surface.md」ファイルに対するもので、Azure OpenAIAPIに関する最新のプレビューリリース情報と使用可能なAPIの概要を更新しています。具体的には、「Data plane - authoring」セクションにおいて、プレビューリリースの日付を`2025-04-01-preview`に修正しました。

この変更に伴い、関連リンクも更新されており、ユーザーが新しいプレビューリリースにアクセスしやすくなっています。全体として、この更新はAzure OpenAI のAPIがどのように進化しているのかを反映しており、開発者が最新情報に基づいて作業できるようにするための重要な情報を提供しています。シンプルな修正ではありますが、API仕様や機能の正確な理解を助ける役割を果たしています。

## articles/ai-services/openai/includes/api-versions/latest-inference-preview.md{#item-24bf0f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新推論プレビューのAPIバージョン更新"
}
```

### Explanation
この変更は、「articles/ai-services/openai/includes/api-versions/latest-inference-preview.md」ファイルに対するもので、Azure OpenAIの最新の推論プレビューAPIバージョンに関する情報を大幅に更新しています。具体的には、538行が追加され、400行が削除され、合計で938行の変更が行われています。

この改訂では、最新のAPIの機能やエンドポイントに関する詳細情報が追加された結果、全体的な内容がより充実し、開発者が必要とする最新の技術情報にアクセスしやすくなっています。特に、APIの更新に伴う新しい機能や改善点が反映されており、開発者がその情報を活用して効果的に作業できるように設計されています。

全体として、この更新は、Azure OpenAIサービスにおける推論機能の進化を示す重要なものであり、開発者が新しい機能を正しく享受できるように最新情報を提供する役割を果たしています。


