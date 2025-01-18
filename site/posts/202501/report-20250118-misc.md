---
date: '2025-01-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0fcd6d7...MicrosoftDocs:1d7cc3c
summary: このリポートでは、ドキュメントに対するマイナーなアップデートが行われ、利便性や理解の向上を目指しています。主な内容は、自分のトレーニングしたモデルをエクスポートする手順の追加や新しい環境変数の導入です。具体的な破壊的変更は報告されていませんが、ドキュメント内の表記の改善やDockerイメージの取得方法の更新などが行われています。これにより、ユーザーはより使いやすく、カスタマイズされたモデルを活用しやすくなり、AIスタジオのモデルカタログも今後のライフサイクルへの理解が深まります。全体として、この変更は技術者や開発者にとってより効率的な使用を促進する内容となっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0fcd6d7...MicrosoftDocs:1d7cc3c){target="_blank"}

# ハイライト

このリポートでは、異なるドキュメントに対するマイナーアップデートを通じて、使用する際の利便性や理解を向上させるための情報の更新が行われました。新しい機能の追加や、表記の修正などが主な焦点とされています。

## 新機能

- コンテナのドキュメントにおいて、自分のトレーニングしたモデルをエクスポートする手順の追加。
- 新しい環境変数の導入やNERコンテナ利用の設定方法の追加。

## 破壊的変更

- 特に報告されていません。

## その他の更新

- ドキュメント内の数字表記やホストスペックの表記形式の改善。
- Dockerイメージの取得方法の更新。
- AIスタジオのモデルカタログ概要の更新。
- プレイグラウンドガイドにおけるSDK名称の修正。

# インサイト

今回のコード変更には、ドキュメントの明確性と使いやすさを向上させるための微細な改善が数多く含まれています。特に、コンテナを用いた会話型言語理解（CLU）に関するドキュメントでは、ユーザーが実際に利用するうえで便利な情報が充実しています。

例えば、データ制限やホストスペックの記載が統一されており、ユーザーが該当する仕様を簡単に確認できるようになっています。また、自分のトレーニングしたモデルをエクスポートする手順が加わったことで、ユーザーはよりカスタマイズされたモデルを活用しやすくなりました。さらに、NERコンテナの利用に関する情報が追加されたことにより、エンティティの複雑な処理が可能になります。

一方で、AIスタジオのモデルカタログに関する更新では、モデルの廃止や退役の情報が追加され、今後のモデルのライフサイクルに対する理解が向上するとともに、常に最新の機能を活用できるように配慮されています。

これらの更新により、技術者や開発者がAzureのAIツールをより効率的に使用でき、ビジネスニーズに合った適切な設定を行うためのガイドラインが提供されています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [use-containers.md](#item-77ab95) | minor update | コンテナの使用に関するドキュメントのアップデート | modified | 70 | 9 | 79 | 
| [model-catalog-overview.md](#item-278001) | minor update | モデルライフサイクルに関する情報の追加 | modified | 6 | 0 | 6 | 
| [get-started-playground.md](#item-e4d7fb) | minor update | 関連コンテンツの表記修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/language-service/conversational-language-understanding/how-to/use-containers.md{#item-77ab95}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ keywords: on-premises, Docker, container
 # Install and run Conversational Language Understanding (CLU) containers
 
 > [!NOTE]
-> The data limits in a single synchronous API call for the CLU container are 5120 characters per document and up to 10 documents per call.
+> The data limits in a single synchronous API call for the CLU container are 5,120 characters per document and up to 10 documents per call.
 
 Containers enable you to host the CLU API on your own infrastructure. If you have security or data governance requirements that can't be fulfilled by calling CLU remotely, then containers might be a good option.
 
@@ -41,31 +41,81 @@ You must meet the following prerequisites before using CLU containers.
 
 The following table describes the minimum and recommended specifications for the available container. Each CPU core must be at least 2.6 gigahertz (GHz) or faster.
 
-It is recommended to have a CPU with AVX-512 instruction set, for the best experience (performance and accuracy).
+It's recommended to have a CPU with AVX-512 instruction set, for the best experience (performance and accuracy).
 
 |                     | Minimum host specs     | Recommended host specs |
 |---------------------|------------------------|------------------------|
-| **CLU**   | 1 core, 2GB memory     | 4 cores, 8GB memory    |
+| **CLU**             | 1 core, 2 GB memory     | 4 cores, 8 GB memory    |
 
 CPU core and memory correspond to the `--cpus` and `--memory` settings, which are used as part of the `docker run` command.
 
+## Export your Conversational Language Understanding model 
+
+Before you proceed with running the docker image, you need to export your own trained model to expose it to your container. Use the following command to extract your model and replace the placeholders below with your own values: 
+
+|Placeholder |Value|Format or example|
+|------------|-----|-----------------|
+|**{API_KEY}** |The key for your Language resource. You can find it on your resource's **Key and endpoint** page, on the Azure portal.|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|
+|**{ENDPOINT_URI}**|The endpoint for accessing the Conversational Language Understanding API. You can find it on your resource's **Key and endpoint** page, on the Azure portal.|`https://<your-custom-subdomain>.cognitiveservices.azure.com`|
+|**{PROJECT_NAME}**|The name of the project containing the model that you want to export. You can find it on your projects tab in the Language Studio portal.|myProject|
+|**{TRAINED_MODEL_NAME}** |The name of the trained model you want to export. You can find your trained models on your model evaluation tab under your project in the Language Studio portal|myTrainedModel 
+|**{EXPORTED_MODEL_NAME}** |The name to assign for the new exported model created.|myExportedModel |
+
+```bash
+curl --location --request PUT '{ENDPOINT_URI}/language/authoring/analyze-conversations/projects/{PROJECT_NAME}/exported-models/{EXPORTED_MODEL_NAME}?api-version=2024-11-15-preview' \ 
+--header 'Ocp-Apim-Subscription-Key: {API_KEY}' \ 
+--header 'Content-Type: application/json' \ 
+--data-raw '{ 
+    "TrainedModelLabel": "{TRAINED_MODEL_NAME}" 
+}' 
+```
+
 ## Get the container image with `docker pull`
 
-The CLU container image can be found on the `mcr.microsoft.com` container registry syndicate. It resides within the `azure-cognitive-services/textanalytics/` repository and is named `clu`. The fully qualified container image name is, `mcr.microsoft.com/azure-cognitive-services/textanalytics/clu`
+The CLU container image can be found on the `mcr.microsoft.com` container registry syndicate. It resides within the `azure-cognitive-services/language/` repository and is named `clu`. The fully qualified container image name is, `mcr.microsoft.com/azure-cognitive-services/language/clu`
 
- To use the latest version of the container, you can use the `latest` tag, which is for English. You can also find a full list of containers for supported languages using the [tags on the MCR](https://mcr.microsoft.com/product/azure-cognitive-services/textanalytics/clu/tags).
+ To use the latest version of the container, you can use the `latest` tag, which is for English. You can also find a full list of containers for supported languages using the [tags on the MCR](https://mcr.microsoft.com/product/azure-cognitive-services/language/clu/tags).
 
 The latest CLU container is available in several languages. To download the container for the English container, use the command below. 
 
 ```
-docker pull mcr.microsoft.com/azure-cognitive-services/textanalytics/clu:latest
+docker pull mcr.microsoft.com/azure-cognitive-services/language/clu:latest
 ```
 
 [!INCLUDE [Tip for using docker list](../../../includes/cognitive-services-containers-docker-list-tip.md)]
 
+## Run the container in download model mode 
+
+After creating the exported model in the section above, users have to run the container in order to download the deployment package that was created specifically for their exported models. 
+
+| Placeholder                 | Value                                                                                                                                 |Format or example                                              |
+|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
+| **{API_KEY}**               | The key for your Language resource. You can find it on your resource's **Key and endpoint** page, on the Azure portal.                | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                              |  
+| **{ENDPOINT_URI}**          | The endpoint for accessing the API. You can find it on your resource's **Key and endpoint** page, on the Azure portal.                | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
+| **{IMAGE_TAG}**             | The image tag representing the language of the container you want to run. Make sure this matches the `docker pull` command you used.  | latest                                                        |
+| **{LOCAL_CLU_PORT}**        | Port number assigned for the container in local machine.                                                                              | 5000                                                          |
+| **{LOCAL_MODEL_DIRECTORY}** | Absolute directory in host machine where exported models are saved in.                                                            | `C:\usr\local\myDeploymentPackage`                            |
+| **{PROJECT_NAME}**          | Name of the project that the exported model belongs to                                                                                | myProject                                                     |
+| **{EXPORTED_MODEL_NAME}**   | Exported model to be downloaded                                                                                                       | myExportedModel                                               |
+
+```bash
+docker run --rm -it -p {LOCAL_CLU_PORT}:80 \ 
+mcr.microsoft.com/azure-cognitive-services/language/clu:{IMAGE_TAG} \   
+-v {LOCAL_MODEL_DIRECTORY}:/DeploymentPackage \ 
+Billing={ENDPOINT_URI} \   
+ApiKey={API_KEY} \ 
+downloadmodel \ 
+projectName={PROJECT_NAME} \ 
+exportedModelName={EXPORTED_MODEL_NAME} 
+```
+
+DO NOT alter the downloaded files. Even altering the name or folder structure can affect the integrity of the container and might break it. 
+
+Repeat those steps to download as many models as you'd like to test. They can belong to different projects and have different exported model names. 
+
 ## Run the container with `docker run`
 
-Once the container is on the host computer, use the [docker run](https://docs.docker.com/engine/reference/commandline/run/) command to run the containers. The container will continue to run until you stop it. Replace the placeholders below with your own values:
+Once the container is on the host computer, use the [docker run](https://docs.docker.com/engine/reference/commandline/run/) command to run the containers. The container continues to run until you stop it. Replace the placeholders below with your own values:
 
 
 > [!IMPORTANT]
@@ -79,10 +129,14 @@ To run the CLU container, execute the following `docker run` command. Replace th
 | **{API_KEY}** | The key for your Language resource. You can find it on your resource's **Key and endpoint** page, on the Azure portal. |`xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`|
 | **{ENDPOINT_URI}** | The endpoint for accessing the API. You can find it on your resource's **Key and endpoint** page, on the Azure portal. | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
 | **{IMAGE_TAG}** | The image tag representing the language of the container you want to run. Make sure this matches the `docker pull` command you used. | `latest` |
+|**{LOCAL_CLU_PORT}** |Port number assigned for the container in local machine. |5000 |
+|**{LOCAL_NER_PORT}** |Port number of the NER container. See Run NER Container section below. |5001 (Has to be different that the above port number) |
+|**{LOCAL_LOGGING_DIRECTORY}** |Absolute directory in host machine where that logs are saved in. |`C:\usr\local\mylogs` |
+|**{LOCAL_MODEL_DIRECTORY}** |Absolute directory in host machine where exported models are saved in. |`C:\usr\local\myDeploymentPackage` |
 
 ```bash
 docker run --rm -it -p 5000:5000 --memory 8g --cpus 1 \
-mcr.microsoft.com/azure-cognitive-services/textanalytics/clu:{IMAGE_TAG} \
+mcr.microsoft.com/azure-cognitive-services/language/clu:{IMAGE_TAG} \
 Eula=accept \
 Billing={ENDPOINT_URI} \
 ApiKey={API_KEY}
@@ -97,6 +151,13 @@ This command:
 
 [!INCLUDE [Running multiple containers on the same host](../../../includes/cognitive-services-containers-run-multiple-same-host.md)]
 
+## Running NER Container 
+CLU relies on NER to handle prebuilt entities. The CLU container works properly without NER if users decide not to integrate it. NER billing is disabled when it’s used through CLU, no extra charges are generated unless a call is made directly to NER’s container. 
+ 
+To set up NER in CLU container 
+- Follow the [NER container documentation](../../named-entity-recognition/how-to/use-containers.md). 
+- When running CLU container, make sure to set the parameter `Ner_Url `so that `Ner_Url=http://host.docker.internal:{LOCAL_NER_PORT}` 
+
 ## Query the container's prediction endpoint
 
 The container provides REST-based query prediction endpoint APIs.
@@ -141,7 +202,7 @@ In this article, you learned concepts and workflow for downloading, installing,
 * You must specify billing information when instantiating a container.
 
 > [!IMPORTANT]
-> Azure AI containers are not licensed to run without being connected to Azure for metering. Customers need to enable the containers to communicate billing information with the metering service at all times. Azure AI containers do not send customer data (e.g. text that is being analyzed) to Microsoft.
+> Azure AI containers aren't licensed to run without being connected to Azure for metering. Customers need to enable the containers to communicate billing information with the metering service at all times. Azure AI containers don't send customer data (for example, text that is being analyzed) to Microsoft.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテナの使用に関するドキュメントのアップデート"
}
```

### Explanation
この変更では、コンテナを用いた会話型言語理解（CLU）に関するドキュメントが更新され、主に以下のポイントが追加・修正されました：

1. **データ制限に関する改善**: ドキュメント内の数字の表記が統一され、数字が5,120と記述されるように修正されました。

2. **ホストスペックの改善**: 最小および推奨ホストスペックの表において、メモリの表記形式が変更され（2GBから2 GBに）、より明確になりました。

3. **新機能の追加**: 自分のトレーニングされたモデルをエクスポートする手順が新たに追加され、ユーザーがコンテナにモデルを提供できるようになりました。

4. **Dockerイメージの取得方法の更新**: CLUコンテナイメージのリポジトリ名が変更され、より正確なリポジトリにリンクが更新されました。

5. **新しい環境変数の導入**: ローカルポートやモデルの保存ディレクトリなど、Docker実行時に使用する新しい環境変数が追加され、ユーザーが設定を行いやすくなっています。

6. **NERコンテナの利用に関する情報**: CLUと一緒にNERコンテナを使用するための設定方法が追加され、これによりユーザーは複雑なエンティティの処理を行うことができます。

これらの更新により、ユーザーはCLUコンテナをより効果的に使用し、ローカルの要件に応じた設定を行うことができるようになります。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -92,6 +92,12 @@ Nixtla | Not available | TimeGEN-1
 
 :::image type="content" source="../media/explore/platform-service-cycle.png" alt-text="Diagram that shows models as a service and the service cycle of managed computes." lightbox="../media/explore/platform-service-cycle.png":::
 
+## Model lifecycle: deprecation and retirement
+AI models evolve fast, and when a new version or a new model with updated capabilities in the same model family become available, older models may be retired in the AI Foundry model catalog. To allow for a smooth transition to a newer model version, some models provide users with the option to enable automatic updates. To learn more about the model lifecycle of different models, upcoming model retirement dates, and suggested replacement models and versions, see:
+
+- [Azure OpenAI Service model deprecations and retirements](../../ai-services/openai/concepts/model-retirements.md)
+- [Severless API model deprecations and retirements](../../ai-studio/concepts/model-lifecycle-retirement.md)
+
 ## Managed compute
 
 The capability to deploy models as managed compute builds on platform capabilities of Azure Machine Learning to enable seamless integration of the wide collection of models in the model catalog across the entire life cycle of large language model (LLM) operations.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルに関する情報の追加"
}
```

### Explanation
この変更では、AIスタジオにおけるモデルカタログの概要に関するドキュメントが更新され、新たにモデルのライフサイクルに関する情報が追加されました。具体的には以下の内容が含まれています：

1. **モデルの廃止と退役**: AIモデルは迅速に進化するため、新しいバージョンや改良された機能を持つモデルが利用可能になると、古いモデルがAIファウンドリのモデルカタログから退役することがあります。

2. **自動更新のオプション**: ユーザーが新しいモデルバージョンへのスムーズな移行を可能にするため、いくつかのモデルには自動更新を有効にするオプションが提供されていることが明示されました。

3. **モデルライフサイクルの詳細な情報へのリンク**: モデルのライフサイクル、今後のモデル退役日、および推奨される代替モデルやバージョンについての詳細情報にアクセスできるリンクが追加されました。具体的にはAzure OpenAIサービスおよびサーバーレスAPIに関連する情報です。

これらの更新により、ユーザーはモデルの進化とその管理についてより深く理解できるようになります。

## articles/ai-studio/quickstarts/get-started-playground.md{#item-e4d7fb}

<details>
<summary>Diff</summary>
````diff
@@ -63,5 +63,5 @@ Next, you can add your data to the model to help it answer questions about your
 
 ## Related content
 
-- [Build a custom chat app in Python using the prompt flow SDK](./get-started-code.md).
+- [Build a custom chat app in Python using the Azure AI Foundry SDK](./get-started-code.md).
 - [Deploy an enterprise chat web app](../tutorials/deploy-chat-web-app.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "関連コンテンツの表記修正"
}
```

### Explanation
この変更では、AIスタジオの「プレイグラウンドを始める」クイックスタートガイドにおいて、関連コンテンツの表記が修正されました。具体的には以下の点が更新されています：

1. **SDKの名称修正**: "using the prompt flow SDK" から "using the Azure AI Foundry SDK" に変更され、正確な名称が使用されるようになりました。これにより、ユーザーが参照する際の混乱を避けられます。

この修正により、関連コンテンツの紹介がより正確かつ明確になり、ユーザーにとっての利便性が向上しています。


