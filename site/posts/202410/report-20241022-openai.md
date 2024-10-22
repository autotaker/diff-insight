---
date: '2024-10-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:96dd444...MicrosoftDocs:bf31bc8
summary: この記事は、Azure OpenAIサービスに関するドキュメントの更新についての要約を提供しています。主な更新内容には、新しいモニタリング指標「Time
  Between Tokens」の追加、廃止された指標の置き換え、Azure Government AI Servicesのモデル可用性情報の更新、Provisioned
  Throughputの改善、およびバッチREST APIの使用例の強化が含まれています。これらの変更は、ユーザーエクスペリエンスを向上させ、Azure AIサービスの運用をより正確かつ効果的にすることを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:96dd444...MicrosoftDocs:bf31bc8){target="_blank"}

# Highlights
この記事は、複数のAzure OpenAIサービスに関連するドキュメントの更新について説明しています。これらの更新には、モデル提供状況、プロビジョニングスループット、バッチREST APIの使用例、そしてモニタリング指標に関するものが含まれています。

## New features
- モニタリング指標に「Time Between Tokens」が追加されました。

## Breaking changes
- 特に重大な変更は報告されていませんが、廃止された指標「Provisioned-managed Utilization」が「Provisioned-managed Utilization V2」に置き換えられています。

## Other updates
- 「Azure Government AI Services」のモデルの可用性に関する情報が更新されました。
- 「Provisioned Throughput」に関する文章が微修正され、正確性と明瞭性が改善されました。
- バッチREST APIの使用例が改善され、エラーメッセージの説明が追加され、API利用時のトラブルシューティングが容易になりました。

# Insights
これらの変更はユーザーエクスペリエンスの向上と、より正確で効果的なAzure AIサービスの運用をサポートすることを目指しています。例えば、Azure Government AI Servicesにおけるモデルの可用性情報の更新は、ユーザーがリアルタイムの可用性を正しく把握するために重要です。また、Provisioned Throughputの詳細情報の改善により、ユーザーはリソースをより効果的に管理・活用できます。

バッチREST APIの文書化での改善は、特に初心者にとってAPIインタフェースの理解を助け、より効率的な実装を可能にします。さらに、「Time Between Tokens」のような新しいモニタリング指標の追加により、Azure OpenAIのパフォーマンスをリアルタイムで把握し、迅速な問題解決が可能になります。これにより、サービスの効率的な利用が推進されます。このように、文書への細やかな修正と指標の追加が、Azureサービスの包括的な利用性を段階的に向上させています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-government.md](#item-a47549) | minor update | Azure Government AI Servicesのモデル提供状況の更新 | modified | 1 | 1 | 2 | 
| [provisioned-throughput.md](#item-022e0c) | minor update | Provisioned Throughputに関するドキュメントの小規模な修正 | modified | 2 | 2 | 4 | 
| [batch-rest.md](#item-bcccd9) | minor update | バッチREST APIの使用例に関する修正 | modified | 4 | 5 | 9 | 
| [monitor-openai-reference.md](#item-8d8887) | minor update | モニタリング指標に関する小規模な追加 | modified | 1 | 0 | 1 | 


# Modified Contents
## articles/ai-services/openai/azure-government.md{#item-a47549}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ The following sections show model availability by region and deployment type.
 
 |   **Region**  | **gpt-35-turbo**, **1106** | **gpt-35-turbo**, **0125** | **gpt-4**, **1106-Preview** | **gpt-4o**, **2024-05-13** | **text-embedding-ada-002** |
 |:--------------|:--------------------------:|:--------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|
-| usgovarizona  | ✅ | ✅ | ✅ | ✅ | ✅ |
+| usgovarizona  | - | ✅ | ✅ | ✅ | ✅ |
 | usgovvirginia | ✅ | ✅ | ✅ | - | ✅ |
 
 To request quota increases for the pay-as-you-go consumption model, apply at [https://aka.ms/AOAIGovQuota](https://aka.ms/AOAIGovQuota)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Government AI Servicesのモデル提供状況の更新"
}
```

### Explanation
この変更は、Azure GovernmentにおけるAIサービスのモデル提供状況を示すテーブルの一部を更新しています。具体的には、"usgovarizona"リージョンの行で、**gpt-35-turbo**, **1106**モデルの可用性が「✅」から「-」に変更されました。これは、モデルの利用可能性に関する情報を反映させるための更新であり、他のリージョンについては引き続き「✅」や「-」のマークが表示されています。この変更は、AIモデルの利用可能性を示す重要な情報を更新することを目的としています。

## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model.
 | Estimating size | Provided calculator in the studio & benchmarking script. |
 
 
-## How much thoughput per PTU you get for each model
+## How much throughput per PTU you get for each model
 The amount of throughput (tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in the minute. Generating output tokens requires more processing than input tokens and so the more output tokens generated the lower your overall TPM. The service dynamically balances the input & output costs, so users do not have to set specific input and output limits. This approach means your deployment is resilient to fluctuations in the workload shape. 
 
 To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the `gpt-4o` and `gpt-4o-mini` models
@@ -109,7 +109,7 @@ Azure OpenAI is a highly sought-after service where customer demand might exceed
 
 To find the capacity needed for their deployments, use the capacity  API or the Studio deployment experience to provide real-time information on capacity availability.
 
-In Azure OpenAI Studio, the deployment experience identifies when a region lacks the capacity needed to deploy the model. This looks at the desired model, version and number of PTUs. If cpacity is unavailable, the experience direct  users to a select an alternative region.
+In Azure OpenAI Studio, the deployment experience identifies when a region lacks the capacity needed to deploy the model. This looks at the desired model, version and number of PTUs. If capacity is unavailable, the experience direct  users to a select an alternative region.
 
 Details on the new deployment experience can be found in the Azure OpenAI [Provisioned get started guide](../how-to/provisioned-get-started.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Provisioned Throughputに関するドキュメントの小規模な修正"
}
```

### Explanation
この変更は、Azure OpenAIの「Provisioned Throughput」に関するドキュメントの内容を一部修正しています。主な変更点としては、見出し「How much throughput per PTU you get for each model」の表記が微修正され、綴りの誤りが修正されています。また、Azure OpenAI Studioにおけるデプロイメント体験に関する説明も明瞭さを向上させるために軽微な文言が修正されています。これらの変更は、情報の正確性と明確さを向上させることを目的としたもので、ユーザーがサービスの利用時に得られる情報をより理解しやすくする役割を果たします。

## articles/ai-services/openai/includes/batch/batch-rest.md{#item-bcccd9}

<details>
<summary>Diff</summary>
````diff
@@ -258,9 +258,8 @@ curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024
 Use the REST API to list all batch jobs with additional sorting/filtering options.
 
 ```http
-curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/batches?api-version=2024-10-01-preview \
-  -H "api-key: $AZURE_OPENAI_API_KEY" \
-  -H "filter: 'created_at gt 1728773533 and created_at lt 1729032733 and status eq 'Completed''" \
-  -H "orderby: created_at asc"
-
+curl "YOUR_RESOURCE_NAME.openai.azure.com/batches?api-version=2024-10-01-preview&$filter=created_at%20gt%201728773533%20and%20created_at%20lt%201729032733%20and%20status%20eq%20'Completed'&$orderby=created_at%20asc" \
+  -H "api-key: $AZURE_OPENAI_API_KEY""
 ```
+
+To avoid the error `URL rejected: Malformed input to a URL function` spaces are replaced with `%20`.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチREST APIの使用例に関する修正"
}
```

### Explanation
この変更は、Azure OpenAIのバッチREST APIに関するドキュメントの使用例を更新しています。具体的には、APIリクエストの形式が改善され、より明確に記述されています。元のサンプルコードではヘッダー情報が個別に指定されていましたが、新しい形式ではURL内にフィルタリング、ソートオプションが組み込まれ、より簡潔で使いやすくなっています。また、エラーメッセージについての説明が追加され、ユーザーがURL内の空白文字を`%20`に置き換える必要があることが明記されています。これにより、API利用時のトラブルシューティングが容易になることを目的としています。

## articles/ai-services/openai/monitor-openai-reference.md{#item-8d8887}

<details>
<summary>Diff</summary>
````diff
@@ -30,6 +30,7 @@ Here are the most important metrics we think you should monitor for Azure OpenAI
 - Provisioned-managed Utilization V2
 - Prompt Token Cache Match Rate
 - Time to Response
+- Time Between Tokens 
 
 > [!NOTE]
 > The **Provisioned-managed Utilization** metric is now deprecated and is no longer recommended. This metric has been replaced by the **Provisioned-managed Utilization V2** metric.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モニタリング指標に関する小規模な追加"
}
```

### Explanation
この変更は、Azure OpenAIのモニタリングに関するドキュメントに新しい指標「Time Between Tokens」を追加しています。この指標は、Azure OpenAIサービスのパフォーマンスを監視する上で重要な要素の一つとされています。他の指標とともに、ユーザーがサービスの応答時間やリソースの利用状況をより正確に把握できるようにすることを目的としています。また、関連する注意書きも含まれており、従来の指標である「Provisioned-managed Utilization」が廃止され「Provisioned-managed Utilization V2」に置き換えられる旨が明記されています。これにより、最新のメトリックに基づいた監視が推奨されることが強調されています。


