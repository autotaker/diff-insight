---
date: '2025-07-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8cabf74...MicrosoftDocs:e9c44be
summary: このドキュメント更新は、「モデルライフサイクル」、「カスタム命名エンティティ認識」、「Azureリソース」、「カスタム質問応答の制限」に関する記事の文言を統一し、一貫性を高めることを目的としています。具体的な変更として、すべての日付を「07/22/2025」に統一し、一般的な表現を調整することで文書の品質を向上させました。新機能は追加されていませんが、情報の更新を通じて明瞭さが増しています。破壊的な変更はなく、これにより読者が情報をより直感的に理解しやすくなっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8cabf74...MicrosoftDocs:e9c44be){target="_blank"}


# ハイライト
このドキュメント更新は、様々な「モデルライフサイクル」、「カスタム命名エンティティ認識」、「Azureリソース」、「カスタム質問応答の制限」に関する記事内で、日付の更新、文言の統一、一貫性の改善を行ったものです。それぞれの修正は、最新情報を反映し、文書の明瞭性を高めています。

## 新機能
- 特に新機能の追加はありませんが、文言や情報の更新を通じて各文章の一貫性と明瞭性が向上しています。

## 破壊的変更
- 破壊的変更はありません。

## その他の更新
- 日付がすべて「07/22/2025」に統一され、最新のリリース情報を反映。
- 一貫性を高めるための表現の微調整。
- 箇条書き形式や指示文の明確化。

# 洞察
今回のドキュメント更新では、主に小さな文言の調整が行われ、全体としてドキュメントの品質向上が図られています。具体的な日付の更新を通じて、情報が最新であることを確認しつつ、文書全体におけるスタイルの一貫性を高めています。特に「カスタム質問応答の制限」などでは、具体的な数字（N-1やN-2）を用いることでさらに明瞭な理解を促しています。

この更新は、読者に対し、AIベースのサービスやモデルを活用する際に誤解が生じないように設計されています。日付の更新を通じて、情報が適時に更新されていることを保証し、一歩先んじた運用が可能になるでしょう。用語と表現の統一的な改善は、技術文書における非常に重要な点であり、このような改訂は常に評価されるべきです。細かな修正であっても、結果的には読者が情報を直感的に理解し、効率良く活用できるようにするために重要です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-lifecycle.md](#item-417f3f) | minor update | モデルライフサイクルの更新 | modified | 15 | 16 | 31 | 
| [quickstart.md](#item-abe5b8) | minor update | カスタム命名エンティティ認識のクイックスタートの更新 | modified | 8 | 9 | 17 | 
| [azure-resources.md](#item-34fc37) | minor update | Azureリソースに関する概念の更新 | modified | 14 | 13 | 27 | 
| [limits.md](#item-50708f) | minor update | カスタム質問応答の制限に関するドキュメントの更新 | modified | 20 | 16 | 36 | 


# Modified Contents
## articles/ai-services/language-service/concepts/model-lifecycle.md{#item-417f3f}

<details>
<summary>Diff</summary>
````diff
@@ -6,34 +6,34 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 01/31/2025
+ms.date: 07/22/2025
 ms.author: lajanuar
 ---
 
 # Model lifecycle
 
-Language service features utilize AI models. We update the language service with new model versions to improve accuracy, support, and quality. As models become older, they are retired. Use this article for information on that process, and what you can expect for your applications.
+Language service features utilize AI models. We update the language service with new model versions to improve accuracy, support, and quality. As models become older, they're retired. Use this article for information on that process, and what you can expect for your applications.
 
 ## Prebuilt features
 
-Our standard (not customized) language service features are built on AI models that we call pre-trained or prebuilt models.
+Our standard (not customized) language service features are built on AI models that we call pretrained or prebuilt models.
 
 We regularly update the language service with new model versions to improve model accuracy, support, and quality.
 
-By default, all API requests will use the latest Generally Available (GA) model.
+By default, all API requests use the latest Generally Available (GA) model.
 
 #### Choose the model-version used on your data
 
-We recommend using the `latest` model version to utilize the latest and highest quality models. As our models improve, it’s possible that some of your model results may change. Model versions may be deprecated, so we no longer accept specified GA model versions in your implementation. 
+We recommend using the `latest` model version to utilize the latest and highest quality models. As our models improve, it's possible that some of your model results may change. Model versions may be deprecated, so we no longer accept specified GA model versions in your implementation. 
 
-Preview models used for preview features do not maintain a minimum retirement period and may be deprecated at any time.
+Preview models used for preview features don't maintain a minimum retirement period and may be deprecated at any time.
 
-By default, API and SDK requests will use the latest Generally Available model. To use a model in preview, you can use an optional parameter `modelVersion` to select the preview version of the model to be used (not recommended for GA models).
+By default, API and SDK requests use the latest Generally Available model. To use a model in preview, you can use an optional parameter `modelVersion` to select the preview version of the model to be used (not recommended for GA models).
 
 > [!NOTE]
-> If you are using a model version that is not listed in the table, then it was subjected to the expiration policy.
+> If you're using a model version that isn't listed in the table, then it was subjected to the expiration policy.
 
-Use the table below to find which model versions are supported by each feature:
+Use the following table to find which model versions support each feature:
 
 | Feature                                             | Supported generally available (GA) version     | Latest supported preview versions           |
 |-----------------------------------------------------|------------------------------------------------|---------------------------------------------|
@@ -55,7 +55,7 @@ Use the table below to find which model versions are supported by each feature:
 
 For custom features, there are two key parts of the AI implementation: training and deployment. New configurations are released regularly with regular AI improvements, so older and less accurate configurations are retired. 
 
-Use the table below to find which model versions are supported by each feature:
+Use the following table to find which model versions support each feature:
 
 | Feature                                     | Supported Training Config Versions         | Training Config Expiration         | Deployment Expiration  |
 |---------------------------------------------|--------------------------------------------|------------------------------------|------------------------|
@@ -66,24 +66,23 @@ Use the table below to find which model versions are supported by each feature:
 
 ** *For latest training configuration versions, the posted expiration dates are subject to availability of a newer model version. If no newer model versions are available, the expiration date may be extended.*
 
-Training configurations are typically available for **six months** after its release. If you've assigned a trained configuration to a deployment, this deployment expires after **twelve months** from the training config expiration. If your models are about to expire, you can retrain and redeploy your models with the latest training configuration version. 
+Training configurations are typically available for **six months** after its release. If you assigned a trained configuration to a deployment, this deployment expires after **twelve months** from the training config expiration. If your models are about to expire, you can retrain and redeploy your models with the latest training configuration version. 
 
 > [!TIP]
-> It's recommended to use the latest supported configuration version.
+> We recommend that you use the latest supported configuration version.
 
 After the **training config expiration** date, you'll have to use another supported training configuration version to submit any training or deployment jobs. After the **deployment expiration** date, your deployed model will be unavailable to be used for prediction.
 
 After training config version expires, API calls will return an error when called or used if called with an expired configuration version. By default, training requests use the latest available training configuration version. To change the configuration version, use the `trainingConfigVersion` parameter when submitting a training job and assign the version you want.
 
 
-
 ## API versions
 
-When you're making API calls to the following features, you need to specify the `API-VERISON` you want to use to complete your request. It's recommended to use the latest available API versions.
+When you're making API calls to the following features, you need to specify the `API-VERISON` you want to use to complete your request. We recommend that you use the latest available API version.
 
-If you're using [Language Studio](https://aka.ms/languageStudio) for your projects, you'll use the latest API version available. Other API versions are only available through the REST APIs and client libraries.
+If you're using [Language Studio](https://aka.ms/languageStudio) for your projects, you use the latest API version available. Other API versions are only available through the REST APIs and client libraries.
 
-Use the following table to find which API versions are supported by each feature:
+Use the following table to find which API versions support each feature:
 
 |Feature                               |Supported versions                                                                   |Latest Generally Available version                           |Latest preview version|
 |--------------------------------------|-------------------------------------------------------------------------------------|----------------------------------|----------------------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルの更新"
}
```

### Explanation
このコードの変更では、ドキュメント「モデルライフサイクル」の内容が更新されました。具体的には、日付の修正、文言の軽微な変更、そして用語の統一が行われました。これにより、最新の情報を文書に反映させ、明確さと一貫性を向上させています。

変更点の一つとして、日付が「01/31/2025」から「07/22/2025」に更新されています Furthermore, 文中の「pre-trained」の表現が「pretrained」に統一されるなど、用語の一貫性が図られました。運用に関連するAPIやモデルの使用に関しても、利用を推奨するための文が「it's recommended that you use the latest supported configuration version」に変更され、より明確な指示が提供されています。

全体的に、この更新は文の流れと情報の明確性を高め、読者がモデルやAPIのバージョン管理に関する情報を理解しやすくすることを目的としています。

## articles/ai-services/language-service/custom-named-entity-recognition/quickstart.md{#item-abe5b8}

<details>
<summary>Diff</summary>
````diff
@@ -6,20 +6,21 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 01/31/2025
+ms.date: 07/22/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-ner, mode-other
 zone_pivot_groups: usage-custom-language-features
 ---
 
 # Quickstart: Custom named entity recognition
 
-Use this article to get started with creating a custom NER project where you can train custom models for custom entity recognition. A model is artificial intelligence software that's trained to do a certain task. For this system, the models extract named entities and are trained by learning from tagged data.
+Use this article to get started with creating a custom NER project where you can train custom models for custom entity recognition. A model artificial intelligence software trained to achieve a specific task. For this system, the models extract named entities and are trained by learning from tagged data.
+
+In this article, we use Language Studio to demonstrate key concepts of custom Named Entity Recognition (NER). As an example, let's build a custom NER model to extract the following relevant entities from loan agreements:
 
-In this article, we use Language Studio to demonstrate key concepts of custom Named Entity Recognition (NER). As an example we’ll build a custom NER model to extract relevant entities from loan agreements, such as the:
 * Date of the agreement
-* Borrower's name, address, city and state  
-* Lender's name, address, city and state  
+* Borrower's name, address, city, and state
+* Lender's name, address, city, and state
 * Loan and interest amounts
 
 ::: zone pivot="language-studio"
@@ -36,11 +37,9 @@ In this article, we use Language Studio to demonstrate key concepts of custom Na
 
 ## Next steps
 
-After you've created entity extraction model, you can:
-
-* [Use the runtime API to extract entities](how-to/call-api.md)
+After you create your entity extraction model, you can [use the runtime API to extract entities](how-to/call-api.md).
 
-When you start to create your own custom NER projects, use the how-to articles to learn more about tagging, training and consuming your model in greater detail:
+As you create your own custom NER projects, use our how-to articles to learn more about tagging, training, and consuming your model in greater detail:
 
 * [Data selection and schema design](how-to/design-schema.md)
 * [Tag data](how-to/tag-data.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム命名エンティティ認識のクイックスタートの更新"
}
```

### Explanation
このコードの変更では、ドキュメント「カスタム命名エンティティ認識のクイックスタート」が更新され、いくつかの軽微な修正が行われました。主な改訂内容には、日付の更新、文の構造改善、および箇条書きの項目間の明確化が含まれています。

具体的には、日付が「01/31/2025」から「07/22/2025」に更新され、最新の情報が反映されています。また、文の一部が修正され、よりスムーズな読解が可能となっています。例えば、「A model is artificial intelligence software that’s trained to do a certain task.」が「A model artificial intelligence software trained to achieve a specific task.」に変更され、文の構造が簡潔に整理されています。

さらに、箇条書きの形式も改善され、項目間の明確さが向上しています。特に、「Borrower's name, address, city and state」という表現の中の「,」の追加や、「the following relevant entities from loan agreements:」への適切なコンマの追加などが行われています。

全体として、この更新は文書の明確性を高め、読者がカスタムNERプロジェクトを作成する際のガイダンスをより理解しやすくすることを目的としています。

## articles/ai-services/language-service/question-answering/concepts/azure-resources.md{#item-34fc37}

<details>
<summary>Diff</summary>
````diff
@@ -1,24 +1,24 @@
 ---
 title: Azure resources - custom question answering
-description: Question answering uses several Azure sources, each with a different purpose. Understanding how they are used individually allows you to plan for and select the correct pricing tier or know when to change your pricing tier. Understanding how they are used in combination allows you to find and fix problems when they occur.
+description: Question answering uses several Azure sources, each with a different purpose. Understanding how they're used individually allows you to plan for and select the correct pricing tier or know when to change your pricing tier. Understanding how they're used in combination allows you to find and fix problems when they occur.
 ms.service: azure-ai-language
 ms.topic: conceptual
 author: laujan
 ms.author: lajanuar
-ms.date: 06/30/2025
+ms.date: 07/22/2025
 ms.custom: language-service-question-answering
 ---
 
 # Azure resources for custom question answering
 
-Custom question answering uses several Azure sources, each with a different purpose. Understanding how they are used individually allows you to plan for and select the correct pricing tier or know when to change your pricing tier. Understanding how resources are used _in combination_ allows you to find and fix problems when they occur.
+Custom question answering uses several Azure sources, each with a different purpose. Understanding how they're used individually allows you to plan for and select the correct pricing tier or know when to change your pricing tier. Understanding how resources are used _in combination_ allows you to find and fix problems when they occur.
 
 ## Resource planning
 
 > [!TIP]
 > "Knowledge base" and "project" are equivalent terms in custom question answering and can be used interchangeably.
 
-When you first develop a project, in the prototype phase, it is common to have a single resource for both testing and production.
+When you first develop a project, in the prototype phase, it's common to have a single resource for both testing and production.
 
 When you move into the development phase of the project, you should consider:
 
@@ -34,14 +34,15 @@ Typically there are three parameters you need to consider:
 
     * The throughput for custom question answering is currently capped at 10 text records per second for both management APIs and prediction APIs.
 
-    * This should also influence your **Azure AI Search** selection, see more details [here](/azure/search/search-sku-tier). Additionally, you might need to adjust Azure AI Search [capacity](/azure/search/search-capacity-planning) with replicas.
+    * The throughput cap should also influence your **Azure AI Search** selection. For more information, *see* [Azure AI Search](/azure/search/search-sku-tier). Additionally, you might need to adjust Azure AI Search [capacity](/azure/search/search-capacity-planning) with replicas.
 
 * **Size and the number of projects**: Choose the appropriate [Azure search SKU](https://azure.microsoft.com/pricing/details/search/) for your scenario. Typically, you decide the number of projects you need based on number of different subject domains. One subject domain (for a single language) should be in one project.
 
     With custom question answering, you have a choice to set up your language resource in a single language or multiple languages. You can make this selection when you create your first project in the [Language Studio](https://language.azure.com/).
 
     > [!IMPORTANT]
-    > You can publish N-1 projects of a single language or N/2 projects of different languages in a particular tier, where N is the maximum indexes allowed in the tier. Also check the maximum size and the number of documents allowed per tier.
+    > You can publish N-1 projects  with a single language resource or N-2 projects with multiple language resources in a single tier. The `N` notation is the maximum indexes allowed in the tier.
+    > Also, check the maximum size and the number of documents allowed per tier.
 
     For example, if your tier has 15 allowed indexes, you can publish 14 projects of the same language (one index per published project). The 15th index is used for all the projects for authoring and testing. If you choose to have projects in different languages, then you can only publish seven projects.
 
@@ -51,9 +52,9 @@ The following table gives you some high-level guidelines.
 
 |                            |Azure AI Search | Limitations                      |
 | -------------------------- |------------ | -------------------------------- |
-| **Experimentation**        |Free Tier    | Publish Up to 2 KBs, 50 MB size  |
-| **Dev/Test Environment**   |Basic        | Publish Up to 14 KBs, 2 GB size    |
-| **Production Environment** |Standard     | Publish Up to 49 KBs, 25 GB size |
+| **Experimentation**        |Free Tier    | Publish Up to 2-KBs, 50-MB size  |
+| **Dev/Test Environment**   |Basic        | Publish Up to 14-KBs, 2-GB size    |
+| **Production Environment** |Standard     | Publish Up to 49-KBs, 25-GB size |
 
 ## Recommended settings
 
@@ -63,14 +64,14 @@ The throughput for custom question answering is currently capped at 10 text reco
 
 ## Keys in custom question answering
 
-Your custom question answering feature deals with two kinds of keys: **authoring keys** and **Azure AI Search keys** used to access the service in the customer’s subscription.
+Your custom question answering feature deals with two kinds of keys: **authoring keys** and **Azure AI Search keys** used to access the service in the customer's subscription.
 
 Use these keys when making requests to the service through APIs.
 
 |Name|Location|Purpose|
 |--|--|--|
 |Authoring/Subscription key|[Azure portal](https://azure.microsoft.com/free/cognitive-services/)|These keys are used to access the Language service APIs). These APIs let you edit the questions and answers in your project, and publish your project. These keys are created when you create a new resource.<br><br>Find these keys on the **Azure AI services** resource on the **Keys and Endpoint** page.|
-|Azure AI Search Admin Key|[Azure portal](/azure/search/search-security-api-keys)|These keys are used to communicate with the Azure AI Search service deployed in the user’s Azure subscription. When you associate an Azure AI Search resource with the custom question answering feature, the admin key is automatically passed to custom question answering. <br><br>You can find these keys on the **Azure AI Search** resource on the **Keys** page.|
+|Azure AI Search Admin Key|[Azure portal](/azure/search/search-security-api-keys)|These keys are used to communicate with the Azure AI Search service deployed in the user's Azure subscription. When you associate an Azure AI Search resource with the custom question answering feature, the admin key is automatically passed to custom question answering. <br><br>You can find these keys on the **Azure AI Search** resource on the **Keys** page.|
 
 ### Find authoring keys in the Azure portal
 
@@ -94,12 +95,12 @@ In custom question answering, both the management and the prediction services ar
 
 Each Azure resource created with custom question answering feature has a specific purpose:
 
-* Language resource (Also referred to as a Text Analytics resource depending on the context of where you are evaluating the resource.)
+* Language resource (Also referred to as a Text Analytics resource depending on the context of where you're evaluating the resource.)
 * Azure AI Search resource
 
 ### Language resource
 
-The language resource with custom question answering feature provides access to the authoring and publishing APIs, hosts the ranking runtime as well as provides telemetry.
+The language resource with custom question answering feature provides access to the authoring and publishing APIs, hosts the ranking runtime and provides telemetry.
 
 ### Azure AI Search resource
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureリソースに関する概念の更新"
}
```

### Explanation
このコードの変更では、ドキュメント「Azureリソース - カスタム質問応答」の内容が更新されました。主な改訂により、いくつかの文の構造が改善され、情報の明確性が向上しています。

具体的には、日付が「06/30/2025」から「07/22/2025」に更新されました。また、文の表現が微調整され、特に一貫性が高められています。例えば、「they are used individually」から「they're used individually」に変更され、言い回しがより自然になっています。同様に、「when they occur」が「when they occur」と変更されるなど、文章の流れが一貫しています。

さらに、リソースの選定や制限に関する説明もより明確になっています。「The throughput cap should also influence your Azure AI Search selection.」のように指示が整理され、読者がより正確に理解できるようになっています。

全体として、この更新は文書の明確性と一貫性を向上させ、読者がカスタム質問応答に関連するAzureリソースをより容易に理解できるようにすることを目的としています。

## articles/ai-services/language-service/question-answering/concepts/limits.md{#item-50708f}

<details>
<summary>Diff</summary>
````diff
@@ -1,16 +1,16 @@
 ---
 title: Limits and boundaries - custom question answering
-description: Custom question answering has meta-limits for parts of the knowledge base and service. It is important to keep your knowledge base within those limits in order to test and publish.
+description: Custom question answering has meta-limits for parts of the knowledge base and service. It's important to keep your knowledge base within those limits in order to test and publish.
 ms.service: azure-ai-language
 author: laujan
 ms.author: lajanuar
 ms.topic: conceptual
-ms.date: 06/21/2025
+ms.date: 07/22/2025
 ---
 
 # Project limits and boundaries
 
-Custom question answering limits provided below are a combination of the [Azure AI Search pricing tier limits](/azure/search/search-limits-quotas-capacity) and custom question answering limits. Both sets of limits affect how many projects you can create per resource and how large each project can grow.
+The following custom question answering limits are a combination of the [Azure AI Search pricing tier limits](/azure/search/search-limits-quotas-capacity) and custom question answering limits. Both sets of limits affect how many projects you can create per resource and how large each project can grow.
 
 ## Projects
 
@@ -21,7 +21,8 @@ Choose the appropriate [Azure search SKU](https://azure.microsoft.com/pricing/de
 With custom question answering, you have a choice to set up your language resource in a single language or multiple languages. You can make this selection when you create your first project in the [Language Studio](https://language.azure.com/).
 
   > [!IMPORTANT]
-  > You can publish N-1 projects of a single language or N/2 projects of different languages in a particular tier, where N is the maximum indexes allowed in the tier. Also check the maximum size and the number of documents allowed per tier.
+  > You can publish N-1 projects with a single language resource or N-2 projects with multiple language resources in a single tier. The `N` notation is the maximum indexes allowed in the tier.
+  > Also check the maximum size and the number of documents allowed per tier.
 
 For example, if your tier has 15 allowed indexes, you can publish 14 projects of the same language (one index per published project). The 15th index is used for all the projects for authoring and testing. If you choose to have projects in different languages, then you can only publish seven projects.
 
@@ -32,7 +33,7 @@ For example, if your tier has 15 allowed indexes, you can publish 14 projects of
 
 File names may not include the following characters:
 
-|Do not use character|
+|Don't use character|
 |--|
 |Single quote `'`|
 |Double quote `"`|
@@ -51,17 +52,17 @@ File names may not include the following characters:
 
 > [!NOTE]
 > Custom question answering currently has no limits on the number of sources that can be added. Throughput is currently capped at 10 text records per second for both management APIs and prediction APIs.
-> When using the F0 tier, upload is limited to 3 files.
+> If you use the F0 tier, upload is limited to three files.
 
 ### Maximum number of deep-links from URL
 
 The maximum number of deep-links that can be crawled for extraction of question answer pairs from a URL page is **20**.
 
 ## Metadata limits
 
-Metadata is presented as a text-based `key:value` pair, such as `product:windows 10`. It is stored and compared in lower case. Maximum number of metadata fields is based on your **[Azure AI Search tier limits](/azure/search/search-limits-quotas-capacity)**.
+Metadata is presented as a text-based `key:value` pair, such as `product:windows 10`. Metadata is stored and compared in lower case. The maximum number of metadata fields is based on your **[Azure AI Search tier limits](/azure/search/search-limits-quotas-capacity)**.
 
-If you choose to projects with multiple languages in a single language resource, there is a dedicated test index per project. So the limit is applied per project in the language service.
+If you choose to projects with multiple languages in a single language resource, there's a dedicated test index per project. So the limit is applied per project in the language service.
 
 |**Azure AI Search tier** | **Free** | **Basic** |**S1** | **S2**| **S3** |**S3 HD**|
 |---|---|---|---|---|---|----|
@@ -99,7 +100,7 @@ Overall limits on the content in the project:
 
 ## Create project call limits:
 
-These represent the limits for each create project action; that is, selecting *Create new project* or calling the REST API to create a project.
+The limits for each create project action, that is, selecting *Create new project* or calling the REST API to create a project are as follows:
 
 * Recommended maximum number of alternate questions per answer: 300
 * Maximum number of URLs: 10
@@ -108,7 +109,8 @@ These represent the limits for each create project action; that is, selecting *C
 
 ## Update project call limits
 
-These represent the limits for each update action; that is, selecting *Save* or calling the REST API with an update request.
+The limits for each update action, that is, selecting *Save* or calling the REST API with an update request are as follows:
+
 * Length of each source name: 300
 * Recommended maximum number of alternate questions added or deleted: 300
 * Maximum number of metadata fields added or deleted: 10
@@ -118,19 +120,21 @@ These represent the limits for each update action; that is, selecting *Save* or
 ## Add unstructured file limits
 
 > [!NOTE]
-> * If you need to use larger files than the limit allows, you can break the file into smaller files before sending them to the API. 
+> * If you need to use larger files than the limit allows, you can break the file into smaller files before sending them to the API.
+
+The limits when unstructured files are used to *Create new project* or call the REST API to create a project are as follows:
 
-These represent the limits when unstructured files are used to *Create new project* or call the REST API to create a project:
-* Length of file: We will extract first 32000 characters
+* Length of file: The service extracts the first 32,000 characters.
 * Maximum three responses per file.
 
 ## Prebuilt custom question answering limits
 
 > [!NOTE]
-> * If you need to use larger documents than the limit allows, you can break the text into smaller chunks of text before sending them to the API. 
-> * A document is a single string of text characters.  
+> * A document is a single string of text characters.
+> * To use larger documents than the limit allows, you can break the text into smaller chunks before sending them to the API.
+
+The limits when the REST API is used to answer a question without having to create a project is as follows:
 
-These represent the limits when REST API is used to answer a question based without having to create a project:
 * Number of documents: 5
 * Maximum size of a single document:  5,120 characters
 * Maximum three responses per document.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム質問応答の制限に関するドキュメントの更新"
}
```

### Explanation
このコードの変更では、ドキュメント「カスタム質問応答の制限と境界」に関して、いくつかの軽微な修正が行われました。主な改訂には、文章の流れを改善し、情報の明確性を高めるための文言の調整が含まれています。

具体的な変更点として、日付が「06/21/2025」から「07/22/2025」に更新され、最新のリリース情報が反映されています。また、テキスト内の表現が若干変更され、より自然かつ一貫性のある表現になっています。たとえば、文中の「It's important to keep your knowledge base within those limits」が、「It's important to keep your knowledge base within those limits」と修正され、句読点や構文が見直されています。

さらに、プロジェクトの制限に関する内容も整理され、「You can publish N-1 projects with a single language resource or N-2 projects with multiple language resources in a single tier.」といった具体的な表現になりました。これにより、読み手が制限を理解しやすくなっています。

全体として、今回のアップデートは、ドキュメントの一貫性や理解しやすさを向上させ、読者がカスタム質問応答機能の利用における制限を適切に把握できるようにすることを目的としています。


