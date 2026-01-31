---
date: '2026-01-31'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d1b059c...MicrosoftDocs:3e5f42f
summary: このドキュメント更新には、Azure言語サービスに関する3つの主要なマイナーアップデートが含まれています。まず、モデルライフサイクル文書の情報が強化され、次にC#
  SDKの更新日付が修正されました。最後に、PII検出のクイックスタートガイドが用語の一貫性と内容の明確さを向上させる形で更新されました。これらの変更は、特にサービスの新しいユーザーや開発者に対する有用なガイドとなり、Azure言語サービスの利用をより効果的にすることを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d1b059c...MicrosoftDocs:3e5f42f){target="_blank"}

# Highlights
このドキュメント更新には、3つの主要なマイナーアップデートが含まれます。最初に、Azure言語サービスの「モデルライフサイクル」文書の情報が強化されました。次に、C# SDK関連のドキュメントで更新日付の修正が行われました。そして最後に、個人を特定できる情報（PII）検出のクイックスタートガイドが更新され、用語の一貫性と内容の明確さが向上しました。

## 新機能
- Azure言語サービスにおけるモデルライフサイクルのポリシーや機能に関する追加情報。

## 破壊的変更
- なし

## その他の更新
- C# SDKおよびPII検出クイックスタートガイドにおいて、更新日付の修正。
- PII検出ガイドの用語変更および説明の改良。

# Insights
このアップデートは、Azure言語サービス、特にモデルライフサイクルの文書に関する細部を強化し、ユーザーがサービスの運用管理をより一層効果的に行えるようにすることを目的としています。例えば、新しいモデルバージョンのリリースや古いモデルの非推奨、退職に関するガイドラインが追加され、ユーザーがモデルのライフサイクルを適切に管理できるようになりました。

C# SDKに関しては、日付情報が矛盾している場合ユーザーが混乱を招く可能性があるため、これを修正したことは情報の正確性を保つ上で重要です。同様に、PII検出のクイックスタートガイドの用語変更と内容改訂は、一貫性を保ちつつ、内容をより分かりやすくすることを目指しています。

これらの更新は、Azure言語サービスのユーザーが正確で最新の情報に基づいてサービスを利用するための重要な基盤を提供し、特にサービスの新しいユーザーや開発者に対する有用なガイドとなります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-lifecycle.md](#item-417f3f) | minor update | モデルライフサイクルに関する更新 | modified | 70 | 54 | 124 | 
| [csharp-sdk.md](#item-67858f) | minor update | C# SDKの更新日付修正 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-94affd) | minor update | PII検出クイックスタートの更新 | modified | 5 | 6 | 11 | 


# Modified Contents
## articles/ai-services/language-service/concepts/model-lifecycle.md{#item-417f3f}

<details>
<summary>Diff</summary>
````diff
@@ -1,99 +1,115 @@
 ---
-title: Model Lifecycle of Language service models
+title: Model Lifecycle for Azure Language service models
 titleSuffix: Foundry Tools
 description: This article describes the timelines for models and model versions used by Language service features.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: concept-article
-ms.date: 01/26/2026
+ms.date: 01/30/2026
 ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD025 -->
 # Model lifecycle
 
-Language features utilize AI models. We update Azure Language with new model versions to improve accuracy, support, and quality. As models become older, they're retired. Use this article for information on that process, and what you can expect for your applications.
+Azure Language features are powered by machine learning models that undergo continuous improvement and refinement. New model versions are released regularly to enhance prediction accuracy, expand language support, and improve overall output quality.
 
-## Prebuilt features
+As part of this iterative development process, older model versions are deprecated and eventually retired according to a defined lifecycle policy. This article provides detailed information about model versioning, deprecation timelines, and retirement procedures to help you plan for updates and maintain compatibility in your production applications.
 
-Our standard (not customized) Language features are built on AI models that we call pretrained or prebuilt models.
+## Prebuilt features
 
-We regularly update Azure Language with new model versions to improve model accuracy, support, and quality.
+Prebuilt (also referred to as pretrained) features in Azure Language are powered by models trained on large datasets and are ready to use without added customization. These models provide out-of-the-box natural language processing capabilities for common scenarios.
 
-By default, all API requests use the latest Generally Available (GA) model.
+Prebuilt models are updated continuously to improve prediction accuracy, expand language coverage, and enhance output quality. By default, all API requests are automatically routed to the latest Generally Available (GA) model version.
 
-#### Choose the model-version used on your data
+### Choose the model version used on your data
 
-We recommend using the `latest` model version to utilize the latest and highest quality models. As our models improve, it's possible that some of your model results may change. Model versions may be deprecated, so we no longer accept specified GA model versions in your implementation.
+We recommend using the **latest** model version to ensure optimal accuracy and access to the most recent improvements. However, as models evolve, prediction outputs may change between versions. Deprecated model versions are no longer accepted in API requests after their retirement date.
 
-Preview models used for preview features don't maintain a minimum retirement period and may be deprecated at any time.
+> [!IMPORTANT]
+> Preview model versions don't maintain a minimum retirement period and may be deprecated at any time without advance notice.
 
-By default, API and SDK requests use the latest Generally Available model. To use a model in preview, you can use an optional parameter `modelVersion` to select the preview version of the model to be used (not recommended for GA models).
+By default, API and SDK requests are processed using the latest Generally Available model version. To specify an alternative version, use the optional **modelVersion** parameter in your request. Specifying a preview model version for production workloads isn't recommended.
 
 > [!NOTE]
-> If you're using a model version that isn't listed in the table, then it was subjected to the expiration policy.
+> If you're using a model version that isn't listed in the following table, that version is retired according to the expiration policy.
 
 ## Model versions
 
-Use the following table to find which model versions support each feature:
-
-| Feature | Supported generally available (GA) version | Latest supported preview versions | Other supported version |
-| ---- | ---- | ---- | ---- |
-| Sentiment Analysis and opinion mining | `latest` | | |
-| Language Detection | `latest` | | |
-| Entity Linking| `latest` | | |
-| Named Entity Recognition (NER) | `latest` | `2025-08-01-preview` | `2025-04-15-preview` |
-| Personally Identifiable Information (PII) detection | `latest` | `2025-08-01-preview` | `2025-04-15-preview` |
-| PII detection for conversations | `latest` | `2024-11-01-preview` | `2023-04-15-preview` |
-| Question answering | `latest` | | |
-| Text Analytics for health | `latest` | `2023-04-15-preview` | |
-| Key phrase extraction | `latest` | | |
-| Summarization | `latest`. **Note**: `2025-06-10` is only available for `issue` and `resolution` aspects in conversation summarization. | | |
+The following table provides a comprehensive reference of supported model versions for each prebuilt feature, including Generally Available (GA), preview, and deprecated versions:
+
+| Feature | Supported generally available (GA) version | Latest supported preview versions | Other supported versions | Deprecated versions |
+| --- | --- | --- | --- | --- |
+| **Sentiment Analysis and opinion mining** | **latest** | | | |
+| **Language Detection** | **latest** | | | |
+| **Entity Linking** | **latest** | | | |
+| **Named Entity Recognition (NER)** | **2025-11-01** (latest) | **2025-11-15-preview** | &bullet; **2025-02-01**</br>&bullet; **2023-09-01** | &bullet; **2025-08-01-preview**</br>&bullet; **2024-05-01** |
+| **Personally Identifiable Information (PII) detection** | **2025-11-01** (latest) | **2025-11-15-preview** | &bullet; **2025-02-01**</br>&bullet; **2023-09-01** | &bullet; **2025-08-01-preview**</br>&bullet; **2024-05-01** |
+| **PII detection for conversations** | **2025-02-01** (latest) | **2025-11-01-preview** | &bullet; **2022-05-15**</br>&bullet; **2022-05-15-preview** | &bullet; **2024-11-01-preview**</br>&bullet; **2023-04-15-preview** |
+| **Question answering** | **latest** | | | |
+| **Text Analytics for health** | **latest** | **2023-04-15-preview** | | |
+| **Key phrase extraction** | **latest** | | | |
+| **Summarization** | **latest**. **Note**: **2025-06-10** is only available for **issue** and **resolution** aspects in conversation summarization. | | | |
 
 ## Custom features
 
-### Expiration timeline
+Custom features in Azure Language involve two distinct lifecycle phases: **training** and **deployment**. Each phase has its own configuration version and expiration timeline. New training configurations are released periodically to incorporate AI improvements, and older configurations are retired according to a defined schedule.
 
-For custom features, there are two key parts of the AI implementation: training and deployment. New configurations are released regularly with regular AI improvements, so older and less accurate configurations are retired.
+### Expiration timeline
 
-Use the following table to find which model versions support each feature:
+The following table lists the supported training configuration versions and their corresponding expiration dates for each custom feature:
 
-| Feature                                     | Supported Training Config Versions         | Training Config Expiration         | Deployment Expiration  |
-|---------------------------------------------|--------------------------------------------|------------------------------------|------------------------|
-| Conversational language understanding       | `2022-09-01` (latest)**                    | August 26, 2025                    | August 26, 2026        |
-| Orchestration workflow                      | `2022-09-01` (latest)**                    | October 22, 2025                   | October 22, 2026       |
-| Custom named entity recognition             | `2022-05-01` (latest)**                    | October 22, 2025                   | October 22, 2026       |
-| Custom text classification                  | `2022-05-01` (latest)**                    | October 22, 2025                   | October 22, 2026       |
+| Feature | Supported Training Config Versions | Training Config Expiration | Deployment Expiration |
+| --- | --- | --- | --- |
+| Conversational language understanding | **2022-09-01** (latest) | August 26, 2025 | August 26, 2026 |
+| Orchestration workflow | **2022-09-01** (latest) | October 22, 2025 | October 22, 2026 |
+| Custom named entity recognition | **2022-05-01** (latest) | October 22, 2025 | October 22, 2026 |
+| Custom text classification | **2022-05-01** (latest) | October 22, 2025 | October 22, 2026 |
 
-** *For latest training configuration versions, the posted expiration dates are subject to availability of a newer model version. If no newer model versions are available, the expiration date may be extended.*
+***For the latest training configuration versions, posted expiration dates are subject to the availability of a newer model version. If no newer model versions are released, the expiration date may be extended.***
 
-Training configurations are typically available for **six months** after its release. If you assigned a trained configuration to a deployment, this deployment expires after **twelve months** from the training config expiration. If your models are about to expire, you can retrain and redeploy your models with the latest training configuration version.
+Training configurations are typically supported for **six months** following their release date. Deployments created using a specific training configuration remain active for **twelve months** after the training configuration expiration date. To avoid service disruption, retrain and redeploy your models using the latest training configuration version before the expiration date.
 
 > [!TIP]
-> We recommend that you use the latest supported configuration version.
+> We recommend using the latest supported training configuration version to ensure optimal model performance and extended support.
 
-After the **training config expiration** date, you have to use another supported training configuration version to submit any training or deployment jobs. After the **deployment expiration** date, your deployed model is unavailable to be used for prediction.
+**Training configuration expiration**: After the training configuration expiration date, you must use a supported configuration version to submit training or deployment jobs. Requests specifying an expired configuration version return an error.
 
-After training config version expires, API calls returns an error when called or used if called with an expired configuration version. By default, training requests use the latest available training configuration version. To change the configuration version, use the `trainingConfigVersion` parameter when submitting a training job and assign the version you want.
+**Deployment expiration**: After the deployment expiration date, the deployed model is no longer available for prediction requests.
+
+By default, training requests use the latest available training configuration version. To specify a different version, include the **trainingConfigVersion** parameter in your training job request.
 
 ## API versions
 
-When you're making API calls to the following features, you need to specify the `API-VERISON` you want to use to complete your request. We recommend that you use the latest available API version.
+For detailed information about request parameters and response schemas, see the [**Azure AI Language REST API reference**](/rest/api/language/).
+
+When making API calls to Azure Language features, you must specify the **API-VERSION** parameter in your request. We recommend using the latest available API version to access the most recent features and improvements.
+
+The following table lists the supported API versions for each feature:
+
+| Feature | Supported versions | Latest Generally Available version | Latest preview version |
+| --- | --- | --- | --- |
+| Custom text </br>classification | &bullet; **2022-05-01**</br>&bullet; **2022-10-01-preview**</br>&bullet; **2023-04-01** | **2022-05-01** | **2022-10-01-preview** |
+| Conversational language </br>understanding | &bullet; **2022-05-01**</br>&bullet; **2022-10-01-preview**</br>&bullet; **2023-04-01** | **2023-04-01** | **2022-10-01-preview** |
+| Custom named entity </br>recognition | &bullet; **2022-05-01**</br>&bullet; **2022-10-01-preview**</br>&bullet; **2023-04-01**</br>&bullet; **2023-04-15**</br>&bullet; **2023-04-15-preview** | **2023-04-15** | **2023-04-15-preview** |
+| Orchestration </br>workflow | &bullet; **2022-05-01**</br>&bullet; **2022-10-01-preview**</br>&bullet; **2023-04-01** | **2023-04-01** | **2022-10-01-preview** |
+| Named Entity</br>Recognition | &bullet; **2025-05-15-preview**</br>&bullet; **2024-11-01 (GA)**</br>&bullet; **2024-11-15-preview** | **2024-11-01 (GA)** | **2025-05-15-preview** |
+| `PII` detection </br>for text | &bullet; **2025-05-15-preview**</br>&bullet; **2024-11-01 (GA)**</br>&bullet; **2024-11-15-preview** | **2024-11-01 (GA)** | **2025-05-15-preview** |
+| `PII` detection </br>for conversations | &bullet; **2025-05-15-preview**</br>&bullet; **2024-11-01 (GA)**</br>&bullet; **2024-11-15-preview** | **2024-11-01 (GA)** | **2025-05-15-preview** |
 
-If you're using [Language Studio](https://aka.ms/languageStudio) for your projects, you use the latest API version available. Other API versions are only available through the REST APIs and client libraries.
+### Model version and API version comparison
 
-Use the following table to find which API versions support each feature:
+Understanding the distinction between model versions and API versions is essential for managing your Azure Language implementations effectively.
 
-|Feature                               |Supported versions                                                                   |Latest Generally Available version                           |Latest preview version|
-|--------------------------------------|-------------------------------------------------------------------------------------|----------------------------------|----------------------|
-| Custom text classification           |`2022-05-01`, `2022-10-01-preview`, `2023-04-01`                                     |`2022-05-01`                      |`2022-10-01-preview`  |
-| Conversational language understanding| `2022-05-01`, `2022-10-01-preview`, `2023-04-01`                                    |`2023-04-01`                      |`2022-10-01-preview`  |
-| Custom named entity recognition      | `2022-05-01`, `2022-10-01-preview`, `2023-04-01`, `2023-04-15`, `2023-04-15-preview`|`2023-04-15`                      |`2023-04-15-preview`  |
-| Orchestration workflow               | `2022-05-01`, `2022-10-01-preview`, `2023-04-01`                                    |`2023-04-01`                      |`2022-10-01-preview`  |
-| Named Entity Recognition (NER) | `2025-05-15-preview`, `2024-11-01 (GA)`,`2024-11-15-preview` | `2024-11-01 (GA)` | `2025-05-15-preview` |
-| Personally Identifiable Information (PII) detection  | `2025-05-15-preview`,`2024-11-01 (GA)`,`2024-11-15-preview` | `2024-11-01 (GA)` | `2025-05-15-preview` |
-| PII detection for conversations  | `2025-05-15-preview`,`2024-11-01 (GA)`,`2024-11-15-preview` | `2024-11-01 (GA)` | `2025-05-15-preview` |
+| Aspect | API version | Model version |
+| --- | --- | --- |
+| **Definition** | Defines the service endpoint contract, including request/response schemas and available operations. | Specifies the underlying machine learning algorithm and trained weights used for predictions. |
+| **REST call location** | Required `api-version` query parameter in the request URL. | Optional `modelVersion` parameter in the request body. |
+| **Update frequency** | Released when interface changes or new features are introduced. | Released regularly to improve prediction accuracy and language coverage. |
+| **Update impact** | Breaking changes require a new API version to maintain backward compatibility. | Updates typically enhance results without requiring API version changes. |
+| **Default behavior** | Must be explicitly specified; SDK/client libraries default to a specific supported version. | Automatically defaults to the latest GA model version if not specified. |
 
-## Next steps
+## Related content
 
-[Azure Language in Foundry Tools overview](../overview.md)
+* [Azure Language overview](../overview.md)
+* [Regional support for Azure Language](regional-support.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルに関する更新"
}
```

### Explanation
この変更は「モデルライフサイクル」という文書に対するマイナーアップデートです。内容が更新され、特にAzure言語サービスのモデルライフサイクルに関する情報が強化されました。追加された情報には、モデルの更新の重要性、非推奨および退職モデルの取り扱い、ならびに新しいトレーニング構成のバージョンとその有効期限についての詳細が含まれています。

主な変更点は次のとおりです：

- モデルのライフサイクルポリシーの明確化：新しいモデルバージョンのリリース、古いモデルの非推奨と退職に関するガイドラインが具体的に示されています。
- プリビルト機能に関する説明の改善：従来の記述からの言い回しが改訂され、より分かりやすくなりました。
- トレーニングとデプロイメントに関する新しいセクションが追加されました。これにより、カスタム機能の有効期限やリリーススケジュールについてより明確な情報が提供されるようになりました。
- APIおよびモデルバージョンの区別を理解するための新しいテーブルが追加されました。

全体として、この変更はAzure言語サービスにおけるモデルの管理タスクをより効果的にするための情報の更新と整理を目的としています。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/csharp-sdk.md{#item-67858f}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,7 @@
 author: laujan
 ms.author: lajanuar
 manager: nitinme
-ms.date: 12/11/2025
+ms.date: 01/30/2026
 ms.service: azure-ai-language
 ms.topic: include
 ms.custom:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDKの更新日付修正"
}
```

### Explanation
この変更はC# SDKに関連するドキュメントの更新です。特に、更新日付が2025年12月11日から2026年1月30日に修正されました。この変更は、情報の正確性を保証し、読者に最新の日時を提供することを目的としています。全体として、内容には他に大きな変更はなく、主にメタデータの調整に留まっています。

## articles/ai-services/language-service/personally-identifiable-information/quickstart.md{#item-94affd}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,12 @@
 ---
 title: "Quickstart: Detect personally identifiable information (PII) in text"
 titleSuffix: Foundry Tools
-description: Detect and redact personally identifiable information (PII) in text using SDKs, the REST API, or the Microsoft Foundry portal.
+description: Detect and redact personally identifiable information (PII) in text using client libraries, the REST API, or the Microsoft Foundry portal.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 01/21/2026
+ms.date: 01/30/2026
 ms.author: lajanuar
 ms.devlang: csharp
 # ms.devlang: csharp, java, javascript, python
@@ -23,9 +23,10 @@ ai-usage: ai-assisted
 ---
 
 # Quickstart: Detect personally identifiable information (PII)
+<!-- markdownlint-disable MD025 -->
 
 > [!NOTE]
-> This quickstart guides you through identifying personally identifiable information (PII) in documents. To detect PII in conversations, see [How to detect and redact PII in conversations](how-to/redact-conversation-pii.md). To detect PII in text, see [How to detect and redact PII in text](how-to/redact-text-pii.md).
+> This quickstart guides you through the process of locating personally identifiable information (PII) in documents. To detect PII in conversations, see [How to detect and redact PII in conversations](how-to/redact-conversation-pii.md). To detect PII in text, see [How to detect and redact PII in text](how-to/redact-text-pii.md).
 
 ::: zone pivot="programming-language-csharp"
 
@@ -66,7 +67,7 @@ ai-usage: ai-assisted
 ## Troubleshooting
 
 | Issue | Resolution |
-|---|---|
+| --- | --- |
 | You get a `401` or `403` error when calling the API. | Confirm your key and endpoint are correct for the same Azure AI resource. If you recently changed role assignments, wait a few minutes and try again. |
 | You get an error about missing environment variables. | Confirm `LANGUAGE_KEY` and `LANGUAGE_ENDPOINT` are set in your environment before you run the sample. |
 | The Foundry experience doesn't match the steps. | In the Foundry portal, use the version toggle to switch between Foundry (classic) and Foundry (new), then follow the matching tab in the Foundry section. |
@@ -78,8 +79,6 @@ To clean up and remove an Azure AI resource, you can delete either the individua
 * [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
 * [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
 
-
-
 ## Next steps
 
 * [PII overview](overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PII検出クイックスタートの更新"
}
```

### Explanation
この変更は「個人を特定できる情報（PII）の検出」についてのクイックスタートガイドに対するマイナーアップデートです。主な変更点は次の通りです：

- 文書の説明部分が改訂され、SDKsから「クライアントライブラリ」へと用語が変更されました。これにより、より一般的に用いられる言葉に置き換えられています。
- 更新日付が2026年1月21日から2026年1月30日に修正され、最新の情報が反映されています。
- 注意事項が若干改訂され、内容がより明確に表現されています。「個人を特定できる情報（PII）の位置を特定するプロセスについて」記載を強調した記述に変更されました。

全体として、この変更はクイックスタートガイドの内容を最新のものに保ちつつ、用語の一貫性と明確さを向上させることを目的としています。


