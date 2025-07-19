---
date: '2025-07-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d29c020...MicrosoftDocs:1217e71
summary: この変更は、AI関連の複数のサービスに関するドキュメントのマイナーアップデートを示しています。主な内容は、日付の更新やリンクの修正、技術的な表現の改善、手順の明確化です。新機能や破壊的変更はなく、文書の利便性と正確性が向上しました。具体的には、ドキュメントの日付が最新に更新され、技術用語の表現が調整され、リンクの整理が行われました。これにより、特に初心者がAPIやサービスを理解しやすくなることが期待されています。正確で明確な文書はユーザービリティの向上に寄与する重要な要素です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d29c020...MicrosoftDocs:1217e71){target="_blank"}

<format>
# Highlights
この変更は、AI関連の複数のサービスに関するドキュメントのマイナーアップデートが行われたことを示します。特に、日付の更新やリンクの修正、技術的な表現の改善、手順の明確化が中心です。新機能や破壊的変更はなく、文書の利便性と正確性を向上させいるのが特徴です。

## New features
新機能は特に追加されていません。

## Breaking changes
破壊的変更はありません。

## Other updates
- ドキュメントの日付が最新版に更新。
- cURLなどの技術用語の記述が調整。
- 特定の文書でリンクおよび内容の簡潔化と整理が実施。
- 手順やプロセスの説明文をより明確に修正。

# Insights
今回の更新では、ドキュメント全体にわたる日付の更新と細かい内容の微調整がされています。日付の変更は主に情報の新鮮さを保つ目的です。リンクの修正は、ユーザーが必要な情報にスムーズにアクセスできるようにするために行われたものです。例えば、言語サービスに関しては、責任あるAIの使用に関するリンクが更新され、ユーザーの利便性が向上しました。

cURLやコマンドに関する表現の改善や、技術的な手順が明確化されることにより、ユーザーが各サービスや機能をより理解しやすくなることが期待されます。これは特に、初心者がドキュメントを参照しつつAPIやサービスを使う際に高い効果を上げます。

ドキュメントインテリジェンスや言語サービスなどは、高度に技術的なAIサービスであり、これに関する正確でわかりやすい文書は、ユーザービリティの観点から非常に大切です。日本語環境向けにローカライズされたドキュメントが、さらに正確で明確になることは、サービスを実用的にする上での重要なステップです。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index.yml](#item-9c57d7) | minor update | 日付の更新とリンクの削除 | modified | 1 | 5 | 6 | 
| [rest-api.md](#item-9d952f) | minor update | 日付の更新とcURLの記述改善 | modified | 2 | 5 | 7 | 
| [use-containers.md](#item-77ab95) | minor update | 多数の文言変更と日付の修正 | modified | 24 | 27 | 51 | 
| [overview.md](#item-89c74f) | minor update | カスタムNERに関する情報の強化と日付更新 | modified | 19 | 17 | 36 | 
| [overview.md](#item-f138b4) | minor update | 言語サービスの透明性に関するリンクの修正 | modified | 4 | 4 | 8 | 
| [redact-document-pii.md](#item-5509ee) | minor update | PII文書の赤色処理手順に関する文書の修正 | modified | 2 | 7 | 9 | 
| [call-api.md](#item-c2ddb6) | minor update | 感情分析および意見マイニングに関する文書の更新 | modified | 13 | 13 | 26 | 
| [document-summarization.md](#item-da1a14) | minor update | 文書要約手順に関する文書の更新 | modified | 8 | 12 | 20 | 
| [call-api.md](#item-a1a7d7) | minor update | 医療向けテキスト分析API呼び出し手順の更新 | modified | 8 | 8 | 16 | 
| [use-containers.md](#item-9dddb4) | minor update | 医療向けテキスト分析コンテナの使用手順の更新 | modified | 34 | 34 | 68 | 


# Modified Contents
## articles/ai-services/document-intelligence/index.yml{#item-9c57d7}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ metadata:
   ms.topic: landing-page
   author: laujan
   ms.author: lajanuar
-  ms.date: 11/19/2024
+  ms.date: 07/17/2025
   monikerRange: '<=doc-intel-4.0.0'
 # linkListType: architecture | concept | deploy | download | get-started | how-to-guide | learn | overview | quickstart | reference | tutorial | video | whats-new
 # Limits: https://learn.learn.microsoft.com/help/contribute/contribute-how-to-write-landing-page?branch=main#limits
@@ -87,10 +87,6 @@ landingContent:
         links:
            - text: Transparency notes
              url: /azure/ai-foundry/responsible-ai/document-intelligence/transparency-note?toc=/azure/ai-services/document-intelligence/toc.json&bc=/azure/ai-services/document-intelligence/breadcrumb/toc.json
-           - text: Characteristics and limitations
-             url:  /azure/ai-foundry/responsible-ai/document-intelligence/characteristics-and-limitations?toc=/azure/ai-services/document-intelligence/toc.json&bc=/azure/ai-services/document-intelligence/breadcrumb/toc.json
-           - text: Guidance for integration and responsible use
-             url: /azure/ai-foundry/responsible-ai/document-intelligence/guidance-integration-responsible-use?toc=/azure/ai-services/document-intelligence/toc.json&bc=/azure/ai-services/document-intelligence/breadcrumb/toc.json
            - text: Data privacy, compliance, and security
              url: /azure/ai-foundry/responsible-ai/document-intelligence/data-privacy-security?toc=/azure/ai-services/document-intelligence/toc.json&bc=/azure/ai-services/document-intelligence/breadcrumb/toc.json#Card 5
    
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新とリンクの削除"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスに関連するYAMLファイルの修正で、主に日付の更新と特定のリンクが削除されています。具体的には、`ms.date` フィールドが2024年11月19日から2025年7月17日に変更され、いくつかのリンク（「特性と制限」、「統合と責任ある使用に関するガイダンス」）が削除されました。これにより、ドキュメントの内容が最新の情報を反映し、情報の整理が行われています。全体として、6か所の変更があり、ファイルの構築が改善されています。

## articles/ai-services/document-intelligence/quickstarts/includes/rest-api.md{#item-9d952f}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: include
-ms.date: 04/11/2025
+ms.date: 07/17/2025
 ms.author: lajanuar
 ---
 
@@ -30,10 +30,7 @@ In this quickstart, learn to use the Document Intelligence REST API to analyze a
 
 * Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services)
 
-* curl command line tool installed.
-
-  * [Windows](https://curl.haxx.se/windows/)
-  * [Mac or Linux](https://learn2torials.com/thread/how-to-install-curl-on-mac-or-linux-(ubuntu)-or-windows)
+* cURL command-line tool installed.
 
 * **PowerShell version 7.*+** (or a similar command-line application.):
   * [Windows](/powershell/scripting/install/installing-powershell-on-windows)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新とcURLの記述改善"
}
```

### Explanation
この変更は、Document Intelligenceのクイックスタートガイドに関連するMarkdownファイルの修正で、主に日付の更新とcURLツールに関する記述の改善が行われています。具体的には、`ms.date` フィールドが2025年4月11日から2025年7月17日に更新されました。また、cURLコマンドラインツールの説明が変更され、インストールに関する情報が簡略化されました。この修正により、ファイルが最新の情報を反映し、ユーザーに対する説明がより明確になります。合計で7か所の変更があり、その中で5行が削除され、2行が追加されています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/use-containers.md{#item-77ab95}

<details>
<summary>Diff</summary>
````diff
@@ -5,12 +5,9 @@ description: Use Docker containers for the conversational language understanding
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.custom:
-  - ignite-2024
 ms.topic: how-to
-ms.date: 04/29/2025
+ms.date: 07/17/2025
 ms.author: lajanuar
-keywords: on-premises, Docker, container
 ---
 
 # Install and run Conversational Language Understanding (CLU) containers
@@ -26,7 +23,7 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 
 You must meet the following prerequisites before using CLU containers.
 
-* If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/cognitive-services/).
+* An active Azure subscription. If you don't have one, create a [free account](https://azure.microsoft.com/free/cognitive-services/).
 * [Docker](https://docs.docker.com/) installed on a host computer. Docker must be configured to allow the containers to connect with and send billing data to Azure.
     * On Windows, Docker must also be configured to support Linux containers.
     * You should have a basic understanding of [Docker concepts](https://docs.docker.com/get-started/overview/).
@@ -40,17 +37,17 @@ You must meet the following prerequisites before using CLU containers.
 
 The following table describes the minimum and recommended specifications for the available container. Each CPU core must be at least 2.6 gigahertz (GHz) or faster.
 
-It's recommended to have a CPU with AVX-512 instruction set, for the best experience (performance and accuracy).
+We recommended that you have a CPU with AVX-512 instruction set, for the best experience (performance and accuracy).
 
 |     | Minimum host specs     | Recommended host specs |
 |---------------------|------------------------|------------------------|
-| **CLU**     | 1 core, 2 GB memory     | 4 cores, 8 GB memory    |
+| **CLU**     | `1 core`, `2-GB memory`     | `4 cores`, `8-GB memory`    |
 
 CPU core and memory correspond to the `--cpus` and `--memory` settings, which are used as part of the `docker run` command.
 
 ## Export your Conversational Language Understanding model
 
-Before you proceed with running the docker image, you need to export your own trained model to expose it to your container. Use the following command to extract your model and replace the placeholders below with your own values:
+Before you proceed with running the docker image, you need to export your own trained model to expose it to your container. Use the following command to extract your model and replace the placeholders with your own values:
 
 |Placeholder |Value|Format or example|
 |------------|-----|-----------------|
@@ -75,7 +72,7 @@ The CLU container image can be found on the `mcr.microsoft.com` container regist
 
  To use the latest version of the container, you can use the `latest` tag, which is for English. You can also find a full list of containers for supported languages using the [tags on the MCR](https://mcr.microsoft.com/product/azure-cognitive-services/language/clu/tags).
 
-The latest CLU container is available in several languages. To download the container for the English container, use the command below.
+The latest CLU container is available in several languages. To download the container for the English container, use the following command:
 
 ```
 docker pull mcr.microsoft.com/azure-cognitive-services/language/clu:latest
@@ -85,14 +82,14 @@ docker pull mcr.microsoft.com/azure-cognitive-services/language/clu:latest
 
 ## Run the container in download model mode
 
-After creating the exported model in the section above, users have to run the container in order to download the deployment package that was created specifically for their exported models.
+After the exported model is created, users have to run the container to download the deployment package that was created specifically for their exported models.
 
-| Placeholder| Value|Format or example  |
+| Placeholder| Value | Format or example  |
 |---|---|---|
-| **{API_KEY}**| The key for your Language resource. You can find it on your resource's **Key and endpoint** page, on the Azure portal. | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   | 
-| **{ENDPOINT_URI}**     | The endpoint for accessing the API. You can find it on your resource's **Key and endpoint** page, on the Azure portal. | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-| **{IMAGE_TAG}**   | The image tag representing the language of the container you want to run. Make sure this matches the `docker pull` command you used.  | latest|
-| **{LOCAL_CLU_PORT}**| Port number assigned for the container in local machine.| 5000 |
+| **{API_KEY}**| The key for your Language resource. You can find it on your resource's **Key and endpoint** page, on the Azure portal. | See Azure portal |
+| **{ENDPOINT_URI}** | The endpoint for accessing the API. You can find it on your resource's **Key and endpoint** page, on the Azure portal. | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
+| **{IMAGE_TAG}** | The image tag representing the language of the container you want to run. Make sure the tag matches the `docker pull` command you used.  | latest|
+| **{LOCAL_CLU_PORT}** | Port number assigned for the container in local machine.| 5000 |
 | **{LOCAL_MODEL_DIRECTORY}** | Absolute directory in host machine where exported models are saved in. | `C:\usr\local\myDeploymentPackage` |
 | **{PROJECT_NAME}**| Name of the project that the exported model belongs to  | myProject  |
 | **{EXPORTED_MODEL_NAME}**   | Exported model to be downloaded | myExportedModel   |
@@ -110,26 +107,26 @@ exportedModelName={EXPORTED_MODEL_NAME}
 
 DO NOT alter the downloaded files. Even altering the name or folder structure can affect the integrity of the container and might break it.
 
-Repeat those steps to download as many models as you'd like to test. They can belong to different projects and have different exported model names.
+Repeat those steps to download as many models as you'd like to test. Your models can belong to different projects and have different (exported) model names.
 
 ## Run the container with `docker run`
 
-Once the container is on the host computer, use the [docker run](https://docs.docker.com/engine/reference/commandline/run/) command to run the containers. The container continues to run until you stop it. Replace the placeholders below with your own values:
+Once the container is on the host computer, use the [docker run](https://docs.docker.com/engine/reference/commandline/run/) command to run the containers. The container continues to run until you stop it. Replace the placeholders with your own values:
 
 
 > [!IMPORTANT]
-> * The docker commands in the following sections use the back slash, `\`, as a line continuation character. Replace or remove this based on your host operating system's requirements.
-> * The `Eula`, `Billing`, and `ApiKey` options must be specified to run the container; otherwise, the container won't start.  For more information, see [Billing](#billing).
+> * The docker commands in the following sections use the back slash, `\`, as a line continuation character. Replace or remove the back slash based on your host operating system's requirements.
+> * The `Eula`, `Billing`, and `ApiKey` options must be specified to run the container; otherwise, the container doesn't start. For more information, see [Billing](#billing).
 
-To run the CLU container, execute the following `docker run` command. Replace the placeholders below with your own values:
+To run the CLU container, execute the following `docker run` command. Replace the placeholders with your own values:
 
 | Placeholder | Value | Format or example |
 |-------------|-------|---|
 | **{API_KEY}** | The key for your Language resource. You can find it on your resource's **Key and endpoint** page, on the Azure portal. |`xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`|
 | **{ENDPOINT_URI}** | The endpoint for accessing the API. You can find it on your resource's **Key and endpoint** page, on the Azure portal. | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-| **{IMAGE_TAG}** | The image tag representing the language of the container you want to run. Make sure this matches the `docker pull` command you used. | `latest` |
+| **{IMAGE_TAG}** | The image tag representing the language of the container you want to run. Make sure the tag matches the `docker pull` command you used. | `latest` |
 |**{LOCAL_CLU_PORT}** |Port number assigned for the container in local machine. |5000 |
-|**{LOCAL_NER_PORT}** |Port number of the NER container. See Run NER Container section below. |5001 (Has to be different that the above port number) |
+|**{LOCAL_NER_PORT}** |Port number of the `NER` container. See Run `NER` Container section. |5001 (Has to be different than the port number) |
 |**{LOCAL_LOGGING_DIRECTORY}** |Absolute directory in host machine where that logs are saved in. |`C:\usr\local\mylogs` |
 |**{LOCAL_MODEL_DIRECTORY}** |Absolute directory in host machine where exported models are saved in. |`C:\usr\local\myDeploymentPackage` |
 
@@ -145,13 +142,13 @@ This command:
 
 * Runs a *CLU* container from the container image
 * Allocates one CPU core and 8 gigabytes (GB) of memory
-* Exposes TCP port 5000 and allocates a pseudo-TTY for the container
+* Exposes `TCP` port 5000 and allocates a pseudo-TTY for the container
 * Automatically removes the container after it exits. The container image is still available on the host computer.
 
 [!INCLUDE [Running multiple containers on the same host](../../../includes/cognitive-services-containers-run-multiple-same-host.md)]
 
-## Running NER Container
-CLU relies on NER to handle prebuilt entities. The CLU container works properly without NER if users decide not to integrate it. NER billing is disabled when it's used through CLU, no extra charges are generated unless a call is made directly to NER's container.
+## Running named entity recognition (NER) Container
+CLU relies on NER to handle prebuilt entities. The CLU container works properly without NER if users decide not to integrate it. NER billing is turned off when accessed via CLU, so there are no added charges unless you make a direct call to the NER container.
 
 To set up NER in CLU container
 - Follow the [NER container documentation](../../named-entity-recognition/how-to/use-containers.md).
@@ -179,7 +176,7 @@ For information on how to call CLU see [our guide](call-api.md).
 
 ## Troubleshooting
 
-If you run the container with an output [mount](../../concepts/configure-containers.md#mount-settings) and logging enabled, the container generates log files that are helpful to troubleshoot issues that happen while starting or running the container.
+If you run the container with both an output [mount](../../concepts/configure-containers.md#mount-settings) and logging enabled, the container generates log files. The log files can help you troubleshoot any issues that occur during startup or while the container is running.
 
 [!INCLUDE [Azure AI services FAQ note](../../../containers/includes/cognitive-services-faq-note.md)]
 
@@ -201,7 +198,7 @@ In this article, you learned concepts and workflow for downloading, installing,
 * You must specify billing information when instantiating a container.
 
 > [!IMPORTANT]
-> Azure AI containers aren't licensed to run without being connected to Azure for metering. Customers need to enable the containers to communicate billing information with the metering service at all times. Azure AI containers don't send customer data (for example, text that is being analyzed) to Microsoft.
+> Azure AI containers aren't licensed to run without being connected to Azure for metering. Customers must enable containers to always communicate billing information to the metering service. Azure AI containers don't send customer data (for example, text that is being analyzed) to Microsoft.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "多数の文言変更と日付の修正"
}
```

### Explanation
この変更は、会話型言語理解に関連するDockerコンテナの使用方法についてのMarkdownファイルの修正です。主な内容としては、日付が2025年4月29日から2025年7月17日に更新され、文書内の多数の文言が改良されました。具体的には、前提条件の記述が明確になり、技術的な詳細が整理されました。また、モデルのエクスポートやコンテナの起動に関する手順がより一層分かりやすくなっています。合計で51か所の変更があり、27行が削除され、24行が追加されています。これにより、ユーザーがDockerコンテナを効果的に利用できるような情報が提供されています。

## articles/ai-services/language-service/custom-named-entity-recognition/overview.md{#item-89c74f}

<details>
<summary>Diff</summary>
````diff
@@ -6,17 +6,17 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 04/29/2025
+ms.date: 07/17/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-ner
 ---
 
 # What is custom named entity recognition?
 
-Custom NER is one of the custom features offered by [Azure AI Language](../overview.md). It is a cloud-based API service that applies machine-learning intelligence to enable you to build custom models for custom named entity recognition tasks.
+Custom named entity recognition (NER) is a cloud-based API service that uses machine learning to help you build models designed for your unique entity recognition requirements. It's one of the specialized features available through [Azure AI Language](../overview.md). With custom NER, you can create AI models that extract domain-specific entities from unstructured text, such as contracts or financial documents. When you start a Custom NER project, you can repeatedly label data, train and evaluate your model, and improve its performance before deploying it. The quality of your labeled data is essential, as it directly impacts the model's accuracy.
+
+To simplify building and customizing your model, the service offers a custom web portal that can be accessed through the [Language studio](https://aka.ms/languageStudio). You can easily get started with the service by following the steps in this [quickstart](quickstart.md).
 
-Custom NER enables users to build custom AI models to extract domain-specific entities from unstructured text, such as contracts or financial documents. By creating a Custom NER project, developers can iteratively label data, train, evaluate, and improve model performance before making it available for consumption. The quality of the labeled data greatly impacts model performance. To simplify building and customizing your model, the service offers a custom web portal that can be accessed through the [Language studio](https://aka.ms/languageStudio). You can easily get started with the service by following the steps in this [quickstart](quickstart.md). 
- 
 This documentation contains the following article types:
 
 * [Quickstarts](quickstart.md) are getting-started instructions to guide you through making requests to the service.
@@ -25,7 +25,7 @@ This documentation contains the following article types:
 
 ## Example usage scenarios
 
-Custom named entity recognition can be used in multiple scenarios across a variety of industries:
+Custom named entity recognition can be used in multiple scenarios across various industries:
 
 ### Information extraction
 
@@ -37,24 +37,26 @@ Search is foundational to any app that surfaces text content to users. Common sc
 
 ### Audit and compliance
 
-Instead of manually reviewing significantly long text files to audit and apply policies, IT departments in financial or legal enterprises can use custom NER to build automated solutions. These solutions can be helpful to enforce compliance policies, and set up necessary business rules based on knowledge mining pipelines that process structured and unstructured content.
+Instead of manually reviewing long text files to audit and apply policies, IT departments in financial or legal enterprises can use custom NER to build automated solutions. These solutions can be helpful to enforce compliance policies, and set up necessary business rules based on knowledge mining pipelines that process structured and unstructured content.
 
 ## Project development lifecycle
 
-Using custom NER typically involves several different steps. 
+Using custom NER typically involves several different steps.
 
 :::image type="content" source="media/development-lifecycle.png" alt-text="The development lifecycle" lightbox="media/development-lifecycle.png":::
 
 1. **Define your schema**: Know your data and identify the [entities](glossary.md#entity) you want extracted. Avoid ambiguity.
 
-2. **Label your data**: Labeling data is a key factor in determining model performance. Label precisely, consistently and completely.
-    1. **Label precisely**: Label each entity to its right type always. Only include what you want extracted, avoid unnecessary data in your labels.
-    2. **Label consistently**:  The same entity should have the same label across all the files.
-    3. **Label completely**: Label all the instances of the entity in all your files.
+1. **Label your data**: Labeling data is a key factor in determining model performance. Label precisely, consistently and completely.
+    * **Label precisely**: Label each entity to its right type always. Only include what you want extracted and avoid unnecessary data in your labels.
+    * **Label consistently**:  The same entity should have the same label across all the files.
+     **Label completely**: Label all the instances of the entity in all your files.
+
+1. **Train the model**: Your model starts learning from your labeled data.
+
+1. **View the model's performance**: After training, review evaluation results and analyze performance for improvement.
 
-3. **Train the model**: Your model starts learning from your labeled data.
 
-4. **View the model's performance**: After training is completed, view the model's evaluation details, its performance and guidance on how to improve it. 
 
 6. **Deploy the model**: Deploying a model makes it available for use via the [Analyze API](https://aka.ms/ct-runtime-swagger).
 
@@ -73,16 +75,16 @@ As you use custom NER, see the following reference documentation and samples for
 |JavaScript (Runtime)    | [JavaScript documentation](/javascript/api/overview/azure/ai-text-analytics-readme?view=azure-node-preview&preserve-view=true)        | [JavaScript samples](https://github.com/Azure/azure-sdk-for-js/blob/%40azure/ai-text-analytics_6.0.0-beta.1/sdk/textanalytics/ai-text-analytics/samples/v5/javascript/customText.js) |
 |Python (Runtime) | [Python documentation](/python/api/azure-ai-textanalytics/azure.ai.textanalytics?view=azure-python-preview&preserve-view=true)        | [Python samples](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/textanalytics/azure-ai-textanalytics/samples/sample_recognize_custom_entities.py) |
 
-## Responsible AI 
+## Responsible AI
 
-An AI system includes not only the technology, but also the people who will use it, the people who will be affected by it, and the environment in which it is deployed. Read the [transparency note for custom NER](/azure/ai-foundry/responsible-ai/language-service/cner-transparency-note) to learn about responsible AI use and deployment in your systems. You can also see the following articles for more information:
+An AI system includes not only the technology, but also the people who use it, the people affected by it, and the deployment environment. Read the [transparency note](/azure/ai-foundry/responsible-ai/language-service/transparency-note) to learn about responsible AI use and deployment in your systems. For more information, *see* the following articles:
 
 [!INCLUDE [Responsible AI links](../includes/overview-responsible-ai-links.md)]
 
 ## Next steps
 
-* Use the [quickstart article](quickstart.md) to start using custom named entity recognition.  
+* Use the [quickstart article](quickstart.md) to start using custom named entity recognition.
 
-* As you go through the project development lifecycle, review the [glossary](glossary.md) to learn more about the terms used throughout the documentation for this feature. 
+* As you go through the project development lifecycle, review the [glossary](glossary.md) to learn more about the terms used throughout the documentation for this feature.
 
 * Remember to view the [service limits](service-limits.md) for information such as [regional availability](service-limits.md#regional-availability).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムNERに関する情報の強化と日付更新"
}
```

### Explanation
この変更は、カスタム命名エンティティ認識（NER）に関する文書の更新で、主に情報の明確化と日付の修正が行われています。日付は2025年4月29日から2025年7月17日に変更され、カスタムNERの定義がより簡潔に記述され、その機能や提供される利点についての説明が強化されています。また、プロジェクト開発のライフサイクルに関するステップが整理され、モデルのトレーニングとパフォーマンス評価のプロセスについても明示的に言及されるようになりました。さらに、ドキュメントの中で関連する情報へのリンクが更新され、ユーザーが必要な情報にアクセスしやすくなっています。合計で36か所の変更があり、17行が削除され、19行が追加されています。

## articles/ai-services/language-service/overview.md{#item-f138b4}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 06/21/2025
+ms.date: 07/17/2025
 ms.author: lajanuar
 ---
 
@@ -248,6 +248,6 @@ Use Language service containers to deploy API features on-premises. These Docker
 
 An AI system includes not only the technology, but also the people who use it, the people affected by it, and the deployment environment. Read the following articles to learn about responsible AI use and deployment in your systems:
 
-* [Transparency note for the Language service](/azure/ai-foundry/responsible-ai/text-analytics/transparency-note)
-* [Integration and responsible use](/azure/ai-foundry/responsible-ai/text-analytics/guidance-integration-responsible-use)
-* [Data, privacy, and security](/azure/ai-foundry/responsible-ai/text-analytics/data-privacy)
+* [Transparency note for the Language service](/azure/ai-foundry/responsible-ai/language-service/transparency-note)
+* [Integration and responsible use](/azure/ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use)
+* [Data, privacy, and security](/azure/ai-foundry/responsible-ai/language-service/data-privacy)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サービスの透明性に関するリンクの修正"
}
```

### Explanation
この変更は、言語サービスに関する概要ページの修正です。主な変更点は、日付が2025年6月21日から2025年7月17日に更新されたことと、責任あるAIに関するリソースへのリンクが修正されたことです。具体的には、元々のリンクが対象となるサービスのコンテキストに沿った適切なパスに変更され、ユーザーがより正確な情報にアクセスできるようになっています。合計で8か所の変更があり、4行が追加され、4行が削除されています。これにより、責任あるAIの使用および展開に関する情報が整理され、ユーザーにとっての利便性が向上しています。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-document-pii.md{#item-5509ee}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 03/05/2025
+ms.date: 07/17/2025
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
@@ -57,19 +57,14 @@ A native document refers to the file format used to create the original document
 
 ***Let's get started:***
 
-* For this project, we use the cURL command line tool to make REST API calls.
+* For this project, we use the cURL command-line tool to make REST API calls.
 
     > [!NOTE]
     > The cURL package is preinstalled on most Windows 10 and Windows 11 and most macOS and Linux distributions. You can check the package version with the following commands:
     > Windows: `curl.exe -V`
     > macOS `curl -V`
     > Linux: `curl --version`
 
-* If cURL isn't installed, here are installation links for your platform:
-
-  * [Windows](https://curl.haxx.se/windows/).
-  * [Mac or Linux](https://learn2torials.com/thread/how-to-install-curl-on-mac-or-linux-(ubuntu)-or-windows).
-
 * An active [**Azure account**](https://azure.microsoft.com/free/cognitive-services/). If you don't have one, you can [**create a free account**](https://azure.microsoft.com/free/).
 
 * An [**Azure Blob Storage account**](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM). You also need to [create containers](#create-azure-blob-storage-containers) in your Azure Blob Storage account for your source and target files:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PII文書の赤色処理手順に関する文書の修正"
}
```

### Explanation
この変更は、「個人識別情報（PII）」の処理に関する文書の修正です。主な更新点は、日付が2025年3月5日から2025年7月17日に変更されたことと、cURLコマンドラインツールに関する表現の修正です。具体的には、「cURL command line tool」が「cURL command-line tool」という形に修正され、正確なハイフンの使い方が導入されています。そのほか、一部のステップが削除され、より明確な手順が強調されています。合計で9か所の変更があり、その中で7行が削除され、2行が追加されました。この更新により、手順が整理され、より分かりやすくなっています。

## articles/ai-services/language-service/sentiment-opinion-mining/how-to/call-api.md{#item-c2ddb6}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,12 @@
 ---
 title: How to perform sentiment analysis and opinion mining
 titleSuffix: Azure AI services
-description: This article will show you how to detect sentiment, and mine for opinions in text.
+description: This article shows you how to detect sentiment, and mine for opinions in text.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 05/23/2025
+ms.date: 07/17/2025
 ms.author: lajanuar
 ms.custom: language-service-sentiment-opinion-mining
 ---
@@ -19,7 +19,7 @@ Sentiment analysis and opinion mining are two ways of detecting positive and neg
 
 Sentiment Analysis applies sentiment labels to text, which are returned at a sentence and document level, with a confidence score for each. 
 
-The labels are *positive*, *negative*, and *neutral*. At the document level, the *mixed* sentiment label also can be returned. The sentiment of the document is determined below:
+The labels are *positive*, *negative*, and *neutral*. At the document level, the *mixed* sentiment label also can be returned. The sentiment of the document is determined as follows:
 
 | Sentence sentiment                                                                            | Returned document label |
 |-----------------------------------------------------------------------------------------------|-------------------------|
@@ -28,17 +28,17 @@ The labels are *positive*, *negative*, and *neutral*. At the document level, the
 | At least one `negative` sentence and at least one `positive` sentence are in the document.    | `mixed`                 |
 | All sentences in the document are `neutral`.                                                  | `neutral`               |
 
-Confidence scores range from 1 to 0. Scores closer to 1 indicate a higher confidence in the label's classification, while lower scores indicate lower confidence. For each document or each sentence, the predicted scores associated with the labels (positive, negative, and neutral) add up to 1. For more information, see the [Responsible AI transparency note](/azure/ai-foundry/responsible-ai/text-analytics/transparency-note). 
+Confidence scores range from 1 to 0. Scores closer to 1 indicate a higher confidence in the label's classification, while lower scores indicate lower confidence. For each document or each sentence, the predicted scores associated with the labels (positive, negative, and neutral) add up to 1. For more information, see the [Responsible AI transparency note](/azure/ai-foundry/responsible-ai/language-service/transparency-note). 
 
 ## Opinion Mining
 
-Opinion Mining is a feature of Sentiment Analysis. Also known as Aspect-based Sentiment Analysis in Natural Language Processing (NLP), this feature provides more granular information about the opinions related to attributes of products or services in text. The API surfaces opinions as a target (noun or verb) and an assessment (adjective).
+Opinion Mining is a feature of Sentiment Analysis. Also called Aspect-based Sentiment Analysis in Natural Language Processing (NLP), this feature provides more granular information about the opinions related to attributes of products or services in text. The API surfaces opinions as a target (noun or verb) and an assessment (adjective).
 
-For example, if a customer leaves feedback about a hotel such as "The room was great, but the staff was unfriendly.", Opinion Mining will locate targets (aspects) in the text, and their associated assessments (opinions) and sentiments. Sentiment Analysis might only report a negative sentiment.
+For example, if a customer leaves feedback about a hotel such as "The room was great, but the staff was unfriendly.", Opinion Mining locates targets (aspects) in the text, and their associated assessments (opinions) and sentiments. Sentiment Analysis might only report a negative sentiment.
 
 :::image type="content" source="../media/opinion-mining.png" alt-text="A diagram of the Opinion Mining example" lightbox="../media/opinion-mining.png":::
 
-If you're using the REST API, to get Opinion Mining in your results, you must include the `opinionMining=true` flag in a request for sentiment analysis. The Opinion Mining results will be included in the sentiment analysis response. Opinion mining is an extension of Sentiment Analysis and is included in your current [pricing tier](https://azure.microsoft.com/pricing/details/cognitive-services/text-analytics/).
+If you're using the REST API, to get Opinion Mining in your results, you must include the `opinionMining=true` flag in a request for sentiment analysis. The Opinion Mining results are included in the sentiment analysis response. Opinion mining is an extension of Sentiment Analysis and is included in your current [pricing tier](https://azure.microsoft.com/pricing/details/cognitive-services/text-analytics/).
 
 ## Development options
 
@@ -48,7 +48,7 @@ If you're using the REST API, to get Opinion Mining in your results, you must in
 
 ### Specify the sentiment analysis model
 
-By default, sentiment analysis will use the latest available AI model on your text. You can also configure your API requests to use a specific [model version](../../concepts/model-lifecycle.md).
+By default, sentiment analysis uses the latest available AI model on your text. You can also configure your API requests to use a specific [model version](../../concepts/model-lifecycle.md).
 
 <!--### Using a preview model version
 
@@ -75,16 +75,16 @@ See the reference documentation for more information.
 
 ### Input languages
 
-When you submit documents to be processed by sentiment analysis, you can specify which of [the supported languages](../language-support.md) they're written in. If you don't specify a language, sentiment analysis will default to English. The API may return offsets in the response to support different [multilingual and emoji encodings](../../concepts/multilingual-emoji-support.md). 
+When you submit documents for processing by sentiment analysis, you can specify which of [the supported languages](../language-support.md) they're written in. If you don't specify a language, sentiment analysis defaults to English. The API may return offsets in the response to support different [multilingual and emoji encodings](../../concepts/multilingual-emoji-support.md). 
 
 ## Submitting data
 
-Sentiment analysis and opinion mining produce a higher-quality result when you give it smaller amounts of text to work on. This is opposite from some features, like key phrase extraction which performs better on larger blocks of text. 
+Sentiment analysis and opinion mining produce a higher-quality result when you give it smaller amounts of text to work on. This process is opposite from some features, like key phrase extraction, that perform better on larger blocks of text. 
 
-To send an API request, you'll need your Language resource endpoint and key.
+To send an API request, you need your Language resource endpoint and key.
 
 > [!NOTE]
-> You can find the key and endpoint for your Language resource on the Azure portal. They will be located on the resource's **Key and endpoint** page, under **resource management**. 
+> You can find the key and endpoint for your Language resource on the Azure portal. They're located on the resource's **Key and endpoint** page, under **resource management**. 
 
 Analysis is performed upon receipt of the request. Using the sentiment analysis and opinion mining features synchronously is stateless. No data is stored in your account, and results are returned immediately in the response.
 
@@ -96,7 +96,7 @@ When you receive results from the API, the order of the returned key phrases is
 
 Sentiment analysis returns a sentiment label and confidence score for the entire document, and each sentence within it. Scores closer to 1 indicate a higher confidence in the label's classification, while lower scores indicate lower confidence. A document can have multiple sentences, and the confidence scores within each document or sentence add up to 1.
 
-Opinion Mining will locate targets (nouns or verbs) in the text, and their associated assessment (adjective). For example, the sentence "*The restaurant had great food and our server was friendly*" has two targets: *food* and *server*. Each target has an assessment. For example, the assessment for *food* would be *great*, and the assessment for *server* would be *friendly*.
+Opinion Mining locates targets (nouns or verbs) in the text, and their associated assessment (adjective). For example, the sentence "*The restaurant had great food and our server was friendly*" has two targets: *food* and *server*. Each target has an assessment. For example, the assessment for *food* would be *great*, and the assessment for *server* would be *friendly*.
 
 The API returns opinions as a target (noun or verb) and an assessment (adjective).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "感情分析および意見マイニングに関する文書の更新"
}
```

### Explanation
この変更は、感情分析および意見マイニングに関するAPIの呼び出し手順を記述した文書の更新です。主な改訂点は、日付が2025年5月23日から2025年7月17日に変更されたことと、文章中のいくつかの表現がより明確に修正されたことです。例えば、「this article will show you how」が「this article shows you how」に変更され、文の一貫性が向上しています。また、いくつかの文が細かく修正され、よりスムーズな読みやすさを意識した表現に調整されています。

さらに、リンク先が関連する情報をより正確に指すように更新されており、全体で26か所の変更が行われています。この更新により、ユーザーが感情分析や意見マイニングの機能をより正確に理解できるようになり、APIの利用時の手順が一層明確になっています。

## articles/ai-services/language-service/summarization/how-to/document-summarization.md{#item-da1a14}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 03/05/2025
+ms.date: 07/17/2025
 ms.author: lajanuar
 ms.custom:
   - language-service-summarization
@@ -52,19 +52,14 @@ Azure AI Language is a cloud-based service that applies Natural Language Process
 
 ***Let's get started:***
 
-* For this project, we use the cURL command line tool to make REST API calls.
+* For this project, we use the cURL command-line tool to make REST API calls.
 
     > [!NOTE]
     > The cURL package is preinstalled on most Windows 10 and Windows 11 and most macOS and Linux distributions. You can check the package version with the following commands:
     > Windows: `curl.exe -V`
     > macOS `curl -V`
     > Linux: `curl --version`
 
-* If cURL isn't installed, here are installation links for your platform:
-
-  * [Windows](https://curl.haxx.se/windows/).
-  * [Mac or Linux](https://learn2torials.com/thread/how-to-install-curl-on-mac-or-linux-(ubuntu)-or-windows).
-
 * An active [**Azure account**](https://azure.microsoft.com/free/cognitive-services/). If you don't have one, you can [**create a free account**](https://azure.microsoft.com/free/).
 
 * An [**Azure Blob Storage account**](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM). You also need to [create containers](#create-azure-blob-storage-containers) in your Azure Blob Storage account for your source and target files:
@@ -150,19 +145,20 @@ When you get results from language detection, you can stream the results to an a
 
 Here's an example of content you might submit for summarization, which is extracted using the Microsoft blog article [A holistic representation toward integrative AI](https://www.microsoft.com/research/blog/a-holistic-representation-toward-integrative-ai/). This article is only an example. The API can accept longer input text. For more information, *see* [data and service limits](../overview.md#input-requirements-and-service-limits).
  
-*"At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."*
+*"At Microsoft, we are on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."*
 
 The text summarization API request is processed upon receipt of the request by creating a job for the API backend. If the job succeeded, the output of the API is returned. The output is available for retrieval for 24 hours. After this time, the output is purged. Due to multilingual and emoji support, the response might contain text offsets. For more information, *see* [how to process offsets](../../concepts/multilingual-emoji-support.md).
 
 When you use the preceding example, the API might return these summarized sentences:
 
 **Extractive summarization**:
-- "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding."
-- "We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages."
-- "The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today."
+
+* "At Microsoft, we are on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding."
+* "We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages."
+* "The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today."
 
 **Abstractive summarization**:
-- "Microsoft is taking a more holistic, human-centric approach to learning and understanding. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. Over the past five years, we have achieved human performance on benchmarks in."
+- "Microsoft is taking a more holistic, human-centric approach to learning and understanding. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. Over the past five years, we achieved human performance on benchmarks in."
 
 ### Try text extractive summarization
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書要約手順に関する文書の更新"
}
```

### Explanation
この変更は、文書要約サービスに関する手順書の更新です。主な修正点は、日付が2025年3月5日から2025年7月17日に変更され、cURLコマンドラインツールの表現が「command line tool」から「command-line tool」に修正されています。さらに、いくつかの文章で表現が明確になり、読みやすさが向上しています。

特に、MicrosoftのAIの進歩に関する例文が更新されており、従来よりも自然な流れで表現されています。これにより、要約APIの使い方がより理解しやすくなっています。また、変更点は合計で20か所に及び、削除された行と追加された行の数はそれぞれ12行と8行です。この更新により、ユーザーは文書要約機能を利用する際の手順とその効果をさらに容易に把握できるようになりました。

## articles/ai-services/language-service/text-analytics-for-health/how-to/call-api.md{#item-a1a7d7}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 06/21/2025
+ms.date: 07/17/2025
 ms.author: lajanuar
 ms.custom: language-service-health
 ---
@@ -16,15 +16,15 @@ ms.custom: language-service-health
 
 [!INCLUDE [service notice](../includes/service-notice.md)]
 
-Text Analytics for health can be used to extract and label relevant medical information from unstructured texts such as doctors' notes, discharge summaries, clinical documents, and electronic health records. The service performs [named entity recognition](../concepts/health-entity-categories.md), [relation extraction](../concepts/relation-extraction.md), [entity linking](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/index.html), and [assertion detection](../concepts/assertion-detection.md) to uncover insights from the input text. For information  on the returned confidence scores, see the [transparency note](/azure/ai-foundry/responsible-ai/text-analytics/transparency-note#general-guidelines-to-understand-and-improve-performance).
+Text Analytics for health can be used to extract relevant medical information from unstructured texts. These texts may include doctors' notes, discharge summaries, clinical documents, and electronic health records. The tool can also label the extracted information for easier analysis and reference. The service performs [named entity recognition](../concepts/health-entity-categories.md), [relation extraction](../concepts/relation-extraction.md), [entity linking](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/index.html), and [assertion detection](../concepts/assertion-detection.md) to uncover insights from the input text. For information  on the returned confidence scores, see the [transparency note](/azure/ai-foundry/responsible-ai/language-service/transparency-note).
 
 > [!TIP]
 > If you want to test out the feature without writing any code, use [Azure AI Foundry](https://ai.azure.com/?cid=learnDocs).
 
-There are two ways to call the service: 
+There are two ways to call the service:
 
-* A [Docker container](use-containers.md) (synchronous)
-* Using the web-based API and client libraries (asynchronous) 
+* Using a [Docker container](use-containers.md) (synchronous).
+* Using the web-based API and client libraries (asynchronous).
 
 ## Development options
 
@@ -39,16 +39,16 @@ The Text Analytics for health supports English in addition to multiple languages
 To send an API request, you need your Language resource endpoint and key.
 
 > [!NOTE]
-> You can find the key and endpoint for your Language resource on the Azure portal. They are located on the resource's **Key and endpoint** page, under **resource management**. 
+> You can find the key and endpoint for your Language resource on the Azure portal. They're located on the resource's **Key and endpoint** page, under **resource management**.
 
-Analysis is performed upon receipt of the request. If you send a request using the REST API or client library, the results are returned asynchronously. If you're using the Docker container, they are returned synchronously.  
+Analysis is performed upon receipt of the request. If you send a request using the REST API or client library, the results are returned asynchronously. If you're using the Docker container, they're returned synchronously.
 
 [!INCLUDE [asynchronous-result-availability](../../includes/async-result-availability.md)]
 
 
 ## Submitting a Fast Healthcare Interoperability Resources (FHIR) request
 
-Fast Healthcare Interoperability Resources (FHIR) is the health industry communication standard developed by the Health Level Seven International (HL7) organization.  The standard defines the data formats (resources) and API structure for exchanging electronic healthcare data. To receive your result using the **FHIR** structure, you must send the FHIR version in the API request body. 
+Fast Healthcare Interoperability Resources (FHIR) is the health industry communication standard developed by the Health Level Seven International (HL7) organization. The standard defines the data formats (resources) and API structure for exchanging electronic healthcare data. To receive your result using the **FHIR** structure, you must send the FHIR version in the API request body.
 
 | Parameter Name  | Type |  Value |
 |--|--|--|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "医療向けテキスト分析API呼び出し手順の更新"
}
```

### Explanation
この変更は、医療向けテキスト分析サービスに関するAPI呼び出し手順を記述した文書の更新です。主な修正点として、文書の日付が2025年6月21日から2025年7月17日に変更され、引き続きをよりスムーズな言い回しに修正しています。

具体的には、医療情報を抽出する説明が「Relevant medical information from unstructured texts」として、より簡潔に整理されています。また、サービスが提供する機能の説明も改善され、情報がより明確に伝わるようになっています。呼び出し方法のリストも整理されて、整然とした形式で提供されています。

また、APIキーとエンドポイントの取得に関する説明において、従来の「They are located」を「They're located」とすることで、より親しみやすい表現に変更されています。変更点は合計16か所であり、削除された行と追加された行はそれぞれ8行ずつです。この更新により、ユーザーが医療向けテキスト分析APIを利用する際の手順が一層明確になることが期待されます。

## articles/ai-services/language-service/text-analytics-for-health/how-to/use-containers.md{#item-9dddb4}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 06/21/2025
+ms.date: 07/17/2025
 ms.author: lajanuar
 ms.custom: language-service-health, devx-track-azurecli
 ms.devlang: azurecli
@@ -23,9 +23,9 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 
 You must meet the following prerequisites before using Text Analytics for health containers. If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/cognitive-services/) before you begin.
 
-* [Docker](https://docs.docker.com/) installed on a host computer. Docker must be configured to allow the containers to connect with and send billing data to Azure. 
+* [Docker](https://docs.docker.com/) installed on a host computer. Docker must be configured to allow the containers to connect with and send billing data to Azure.
     * On Windows, Docker must also be configured to support Linux containers.
-    * You should have a basic understanding of [Docker concepts](https://docs.docker.com/get-started/overview/). 
+    * You should have a basic understanding of [Docker concepts](https://docs.docker.com/get-started/overview/).
 * A <a href="https://portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics"  title="Create a Language resource"  target="_blank">Language resource </a> with the free (F0) or standard (S) [pricing tier](https://azure.microsoft.com/pricing/details/cognitive-services/text-analytics/).
 
 [!INCLUDE [Gathering required parameters](../../../containers/includes/container-gathering-required-parameters.md)]
@@ -49,7 +49,7 @@ The Text Analytics for health container image can be found on the `mcr.microsoft
 
 To use the latest version of the container, you can use the `latest` tag. You can also find a full list of [tags on the MCR](https://mcr.microsoft.com/product/azure-cognitive-services/textanalytics/healthcare/tags).
 
-Use the [`docker pull`](https://docs.docker.com/engine/reference/commandline/pull/) command to download this container image from the Microsoft public container registry. You can find the featured tags on the  [Microsoft Container Registry](https://mcr.microsoft.com/product/azure-cognitive-services/textanalytics/healthcare/about)  
+Use the [`docker pull`](https://docs.docker.com/engine/reference/commandline/pull/) command to download this container image from the Microsoft public container registry. You can find the featured tags on the  [Microsoft Container Registry](https://mcr.microsoft.com/product/azure-cognitive-services/textanalytics/healthcare/about)
 
 ```
 docker pull mcr.microsoft.com/azure-cognitive-services/textanalytics/healthcare:<tag-name>
@@ -59,25 +59,25 @@ docker pull mcr.microsoft.com/azure-cognitive-services/textanalytics/healthcare:
 
 ## Run the container with `docker run`
 
-Once the container is on the host computer, use the [docker run](https://docs.docker.com/engine/reference/commandline/run/) command to run the containers. The container will continue to run until you stop it.
+Once the container is on the host computer, use the [docker run](https://docs.docker.com/engine/reference/commandline/run/) command and run the containers. The container continues to run until you stop it.
 
 > [!IMPORTANT]
-> * The docker commands in the following sections use the back slash, `\`, as a line continuation character. Replace or remove this based on your host operating system's requirements. 
-> * The `Eula`, `Billing`, and `ApiKey` options must be specified to run the container; otherwise, the container won't start.  For more information, see [Billing](#billing).
->   * The [responsible AI](/azure/ai-foundry/responsible-ai/text-analytics/transparency-note-health)  (RAI) acknowledgment must also be present with a value of `accept`.
+> * The docker commands in the following sections use the back slash, `\`, as a line continuation character. Replace or remove the back slash based on your host operating system's requirements.
+> * The `Eula`, `Billing`, and `ApiKey` options must be specified to run the container; otherwise, the container doesn't start. For more information, see [Billing](#billing).
+>   * The [responsible AI](/azure/ai-foundry/responsible-ai/language-service/transparency-note) (RAI) acknowledgment must also be present with a value of `accept`.
 > * The sentiment analysis and language detection containers use v3 of the API, and are generally available. The key phrase extraction container uses v2 of the API, and is in preview.
 
-There are multiple ways you can install and run the Text Analytics for health container. 
+There are multiple ways you can install and run the Text Analytics for health container.
 
 - Use the Azure portal to create a Language resource, and use Docker to get your container.
-- Use an Azure VM with Docker to run the container. 
+- Use an Azure virtual machine (VM) with Docker and run the container.
 - Use the following PowerShell and Azure CLI scripts to automate resource deployment and container configuration.
 
-When you use the Text Analytics for health container, the data contained in your API requests and responses is not visible to Microsoft, and is not used for training the model applied to your data. 
+When you use the Text Analytics for health container, the data contained in your API requests and responses isn't visible to Microsoft, and isn't used for training the model applied to your data.
 
 ### Run the container locally
 
-To run the container in your own environment after downloading the container image, execute the following `docker run` command. Replace the placeholders below with your own values:
+To run the container in your own environment after downloading the container image, execute the following `docker run` command. Replace the placeholders with your own values:
 
 | Placeholder | Value | Format or example |
 |-------------|-------|---|
@@ -90,26 +90,26 @@ mcr.microsoft.com/azure-cognitive-services/textanalytics/healthcare:<tag-name> \
 Eula=accept \
 rai_terms=accept \
 Billing={ENDPOINT_URI} \
-ApiKey={API_KEY} 
+ApiKey={API_KEY}
 ```
 
 This command:
 
 - Runs the Text Analytics for health container from the container image
 - Allocates 6 CPU core and 12 gigabytes (GB) of memory
-- Exposes TCP port 5000 and allocates a pseudo-TTY for the container
+- Exposes `TCP` port 5000 and allocates a pseudo-TTY for the container
 - Accepts the end user license agreement (EULA) and responsible AI (RAI) terms
 - Automatically removes the container after it exits. The container image is still available on the host computer.
 
 ### Demo UI to visualize output
 
-The container provides REST-based query prediction endpoint APIs.  We have also provided a visualization tool in the container that is accessible by appending `/demo` to the endpoint of the container. For example:
+The container provides REST-based query prediction endpoint APIs. We also provide a visualization tool in the container that is accessible by appending `/demo` to the endpoint of the container. For example:
 
 ```
 http://<serverURL>:5000/demo
 ```
 
-Use the example cURL request below to submit a query to the container you have deployed replacing the `serverURL` variable with the appropriate value.
+Use the following example cURL request to submit a query to the container you deployed by replacing the `serverURL` variable with the appropriate value.
 
 ```bash
 curl -X POST 'http://<serverURL>:5000/text/analytics/v3.1/entities/health' --header 'Content-Type: application/json' --header 'accept: application/json' --data-binary @example.json
@@ -118,10 +118,10 @@ curl -X POST 'http://<serverURL>:5000/text/analytics/v3.1/entities/health' --hea
 
 ### Install the container using Azure Web App for Containers
 
-Azure [Web App for Containers](https://azure.microsoft.com/services/app-service/containers/) is an Azure resource dedicated to running containers in the cloud. It brings out-of-the-box capabilities such as autoscaling, support for docker containers and docker compose, HTTPS support and much more.
+Azure [Web App for Containers](https://azure.microsoft.com/services/app-service/containers/) is an Azure resource dedicated to running containers in the cloud. It offers built-in features like autoscaling, support for Docker containers and Docker Compose, and HTTPS support.
 
 > [!NOTE]
-> Using Azure Web App you will automatically get a domain in the form of `<appservice_name>.azurewebsites.net`
+> With Azure Web App, you automatically get a domain in the form of `<appservice_name>.azurewebsites.net`
 
 Run this PowerShell script using the Azure CLI to create a Web App for Containers, using your subscription and the container image over HTTPS. Wait for the script to complete (approximately 25-30 minutes) before submitting the first request.
 
@@ -141,21 +141,21 @@ $DOCKER_IMAGE_NAME = "mcr.microsoft.com/azure-cognitive-services/textanalytics/h
 az login
 az account set -s $subscription_name
 az appservice plan create -n $appservice_plan_name -g $resource_group_name --is-linux -l $resources_location --sku P3V2
-az webapp create -g $resource_group_name -p $appservice_plan_name -n $appservice_name -i $DOCKER_IMAGE_NAME 
+az webapp create -g $resource_group_name -p $appservice_plan_name -n $appservice_name -i $DOCKER_IMAGE_NAME
 az webapp config appsettings set -g $resource_group_name -n $appservice_name --settings Eula=accept rai_terms=accept Billing=$TEXT_ANALYTICS_RESOURCE_API_ENDPOINT ApiKey=$TEXT_ANALYTICS_RESOURCE_API_KEY
 
 # Once deployment complete, the resource should be available at: https://<appservice_name>.azurewebsites.net
 ```
 
 ### Install the container using Azure Container Instance
 
-You can also use an Azure Container Instance (ACI) to make deployment easier. ACI is a resource that allows you to run Docker containers on-demand in a managed, serverless Azure environment. 
+You can also use an Azure Container Instance (ACI) to make deployment easier. ACI is a resource that allows you to run Docker containers on-demand in a managed, serverless Azure environment.
 
-See [How to use Azure Container Instances](../../../containers/azure-container-instance-recipe.md) for steps on deploying an ACI resource using the Azure portal. You can also use the below PowerShell script using Azure CLI, which will create an ACI on your subscription using the container image.  Wait for the script to complete (approximately 25-30 minutes) before submitting the first request.  Due to the limit on the maximum number of CPUs per ACI resource, do not select this option if you expect to submit more than 5 large documents (approximately 5000 characters each) per request.
-See the [ACI regional support](/azure/container-instances/container-instances-region-availability) article for availability information. 
+See [How to use Azure Container Instances](../../../containers/azure-container-instance-recipe.md) for steps on deploying an ACI resource using the Azure portal. You can also use the following PowerShell script using Azure CLI, which creates an ACI on your subscription using the container image. Wait for the script to complete (approximately 25-30 minutes) before submitting the first request. Due to the limit on the maximum number of CPUs per ACI resource, don't select this option if you expect to submit more than five large documents (approximately 5,000 characters each) per request.
+See the [ACI regional support](/azure/container-instances/container-instances-region-availability) article for availability information.
 
-> [!NOTE] 
-> Azure Container Instances don't include HTTPS support for the builtin domains. If you need HTTPS, you will need to manually configure it, including creating a certificate and registering a domain. You can find instructions to do this with NGINX below.
+> [!NOTE]
+> Azure Container Instances don't include HTTPS support for the builtin domains. If you need HTTPS, you need to manually configure it, including creating a certificate and registering a domain. You can find instructions with the following NGINX example:
 
 ```azurecli
 $subscription_name = ""                    # The name of the subscription you want you resource to be created on.
@@ -179,20 +179,20 @@ az container create --resource-group $resource_group_name --name $azure_containe
 
 ### Secure ACI connectivity
 
-By default there is no security provided when using ACI with container API. This is because typically containers will run as part of a pod which is protected from the outside by a network bridge. You can however modify a container with a front-facing component, keeping the container endpoint private. The following examples use [NGINX](https://www.nginx.com) as an ingress gateway to support HTTPS/SSL and client-certificate authentication.
+By default, ACI with the container API doesn't provide security—containers usually run inside a pod, and a network bridge isolates the pod from external access. You can, however, modify a container with a front-facing component, keeping the container endpoint private. The following examples use [NGINX](https://www.nginx.com) as an ingress gateway to support HTTPS/SSL and client-certificate authentication.
 
 > [!NOTE]
-> NGINX is an open-source, high-performance HTTP server and proxy. An NGINX container can be used to terminate a TLS connection for a single container. More complex NGINX ingress-based TLS termination solutions are also possible.
+> NGINX is an open-source, high-performance HTTP server, and proxy. An NGINX container can be used to terminate a `TLS` connection for a single container. More complex NGINX ingress-based `TLS` termination solutions are also possible.
 
 #### Set up NGINX as an ingress gateway
 
-NGINX uses [configuration files](https://docs.nginx.com/nginx/admin-guide/basic-functionality/managing-configuration-files/) to enable features at runtime. In order to enable TLS termination for another service, you must specify an SSL certificate to terminate the TLS connection and  `proxy_pass` to specify an address for the service. A sample is provided below.
+NGINX uses [configuration files](https://docs.nginx.com/nginx/admin-guide/basic-functionality/managing-configuration-files/) to enable features at runtime. In order to enable `TLS` termination for another service, you must specify an SSL certificate to terminate the `TLS` connection and  `proxy_pass` to specify an address for the service. A sample is provided:
 
 
 > [!NOTE]
 > `ssl_certificate` expects a path to be specified within the NGINX container's local filesystem. The address specified for `proxy_pass` must be available from within the NGINX container's network.
 
-The NGINX container will load all of the files in the `_.conf_` that are mounted under `/etc/nginx/conf.d/` into the HTTP configuration path.
+The NGINX container loads all of the files in the `_.conf_` that are mounted under `/etc/nginx/conf.d/` into the HTTP configuration path.
 
 ```nginx
 server {
@@ -213,9 +213,9 @@ server {
 }
 ```
 
-#### Example Docker compose file
+#### Compose file example
 
-The below example shows how a [docker compose](https://docs.docker.com/reference/cli/docker/compose/) file can be created to deploy NGINX and health containers:
+The following example shows how a [docker compose](https://docs.docker.com/reference/cli/docker/compose/) file can be created to deploy NGINX and health containers:
 
 ```yaml
 version: "3.7"
@@ -262,7 +262,7 @@ Use the host, `http://localhost:5000`, for container APIs.
 
 ### Structure the API request for the container
 
-You can use the [Visual Studio Code REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) or the example cURL request below to submit a query to the container you deployed, replacing the `serverURL` variable with the appropriate value.  Note the version of the API in the URL for the container is different than the hosted API.
+You can use the [Visual Studio Code REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) or the following example cURL request to submit a query to the container you deployed, replacing the `serverURL` variable with the appropriate value. Note the version of the API in the URL for the container is different than the hosted API.
 
 [!INCLUDE [Use APIs in container](../includes/container-request.md)]
 
@@ -289,13 +289,13 @@ var client = new TextAnalyticsClient("http://localhost:5000", "your-text-analyti
 
 ## Troubleshooting
 
-If you run the container with an output [mount](configure-containers.md#mount-settings) and logging enabled, the container generates log files that are helpful to troubleshoot issues that happen while starting or running the container.
+If you run the container with an output [mount](configure-containers.md#mount-settings) and logging enabled, the container generates log files. These log files are useful for troubleshooting issues that may occur while the container is starting or running.
 
 [!INCLUDE [Azure AI services FAQ note](../../../containers/includes/cognitive-services-faq-note.md)]
 
 ## Billing
 
-Text Analytics for health containers send billing information to Azure, using a _Language_ resource on your Azure account. 
+Text Analytics for health containers send billing information to Azure, using a _Language_ resource on your Azure account.
 
 [!INCLUDE [Container's Billing Settings](../../../includes/cognitive-services-containers-how-to-billing-info.md)]
 
@@ -310,7 +310,7 @@ In this article, you learned concepts and workflow for downloading, installing,
 * You must specify billing information when instantiating a container.
 
 > [!IMPORTANT]
-> Azure AI containers are not licensed to run without being connected to Azure for metering. Customers need to enable the containers to communicate billing information with the metering service at all times. Azure AI containers do not send customer data (e.g. text that is being analyzed) to Microsoft.
+> Azure AI containers aren't licensed to run without being connected to Azure for metering. Customers must ensure that the containers are always able to communicate billing information to the metering service. Azure AI containers don't send customer data (for example, text that is being analyzed) to Microsoft.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "医療向けテキスト分析コンテナの使用手順の更新"
}
```

### Explanation
この変更は、医療向けテキスト分析サービスのコンテナ使用に関する手順書の更新です。主な修正点は、文書の日付が2025年6月21日から2025年7月17日に変更され、全体的に文の明確さと一貫性が向上しています。

具体的には、テキスト分析のコンテナを使用するための前提条件が簡潔に整理され、特にDockerに関する注意事項が改善されています。また、`docker run`コマンドの説明においても、書き方が一貫性を持たせられ、何を指定する必要があるのかが明確に示されています。

さらに、登録後のリソースの管理やセキュリティに関するセクションでは、重要な注意点が強調され、利便性が向上しています。全体として、変更点は68か所に及び、削除された行と追加された行がそれぞれ34行ずつです。この更新により、医療向けテキスト分析コンテナの使用が一層スムーズに行えるようになりました。ユーザーは、手順を追いやすく、より明確にコンテナの管理と使用法を理解することができます。


