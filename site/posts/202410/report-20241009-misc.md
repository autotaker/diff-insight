---
date: '2024-10-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e9690f5...MicrosoftDocs:eb045a9
summary: このコード更新は、Azure AIサービスのドキュメントで多数のファイルが対象であり、新機能の追加や著者情報の更新が中心です。特筆すべき点は、言語サービスにPII検出機能が追加されたこと、著者やレビュー担当者の情報の更新により信頼性向上、不要な機能プレビュータグの削除による文書の簡潔化です。全体的に、ユーザビリティと効率性を向上させるための重要なステップを反映しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e9690f5...MicrosoftDocs:eb045a9){target="_blank"}

# ハイライト
このコード更新は、Azure AIサービスのドキュメントに関する多数のファイルを対象に行われ、主に新機能の追加や著者情報の更新を含んでいます。特に、以下の点が重要です。

- 言語サービスにおける個人を特定できる情報（PII）検出の機能がコンテナ設定に追加されました。
- 著者やレビュー担当者の情報が多数のファイルで更新され、これにより信頼性や透明性が向上しました。
- 不要な機能プレビューのタグが複数のファイルから削除され、内容が簡潔に。

## 新機能
- Azure AIサービスのコンテナ設定におけるPII検出機能の追加

## ブレイキングチェンジ
- 特に重大な互換性の問題を引き起こす変更は見られません。

## その他の更新
- 大多数の文書で著者とレビュー担当者情報の更新
- 不要なインクルードタグの削除による文書の簡素化
- 古いメディアファイルの削除

# インサイト
この一連の変更は、Azure AIサービスのユーザビリティと効率性を向上させるための重要なステップを示しています。特に、言語サービスの設定にPII検出の機能追加は、エンタープライズ環境におけるセキュリティやコンプライアンスの強化に直結します。この機能は、企業が法令遵守や社内ポリシーの遵守を容易にするための強力なツールとなるでしょう。

また、大規模な著者情報の更新と不要な機能プレビューの削除は、書類作成の効率を向上し、レビューやユーザーフィードバックがより正確に行えるようにするためのものです。これにより、ユーザーは常に最新で信頼性のある情報にアクセスでき、これが大規模なシステムインテグレーションや継続的な改善プロセスにおいて重要な役割を果たします。

さらに、古いメディアファイルを削除することによって、ドキュメントリポジトリのコンテンツ管理がさらに効率的になり、ユーザーが必要な情報を迅速に見つけられるようになります。このような小さな変更が積み重なって、最終的にはユーザーエクスペリエンス全体の向上につながると考えられます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [configure-containers.md](#item-6f87ab) | minor update | コンテナの設定にPII検出を追加 | modified | 1 | 0 | 1 | 
| [use-containers.md](#item-8c61d4) | new feature | 新しいコンテナ使用法に関するドキュメントの追加 | added | 147 | 0 | 147 | 
| [toc.yml](#item-12f1f0) | minor update | 目次にコンテナ使用に関する項目を追加 | modified | 12 | 0 | 12 | 
| [connect-ai-services.md](#item-3f7954) | minor update | AIサービス接続に関する文書から不要な要素を削除 | modified | 0 | 2 | 2 | 
| [get-started.md](#item-8378f4) | minor update | AIサービス入門文書から不要な要素を削除 | modified | 0 | 2 | 2 | 
| [connections.md](#item-01b26a) | minor update | 接続に関する文書の著者情報とレビュー担当者を更新 | modified | 3 | 5 | 8 | 
| [content-filtering.md](#item-91b372) | minor update | コンテンツフィルター文書から不要な要素を削除 | modified | 0 | 2 | 2 | 
| [fine-tuning-overview.md](#item-31b07b) | minor update | ファインチューニングの概要における著者情報とレビュー担当者の更新 | modified | 3 | 3 | 6 | 
| [retrieval-augmented-generation.md](#item-c98880) | minor update | 情報更新と不要な要素の削除 | modified | 3 | 5 | 8 | 
| [faq.yml](#item-e7baa2) | minor update | FAQファイルの著者情報とレビュー担当者の更新 | modified | 3 | 3 | 6 | 
| [connections-add.md](#item-6f5a17) | minor update | Azure OpenAIサービスの説明のアップデート | modified | 1 | 1 | 2 | 
| [data-image-add.md](#item-a1f038) | minor update | データ画像追加ガイドのレビュー担当者の更新 | modified | 1 | 1 | 2 | 
| [ai-template-get-started.md](#item-d71b59) | minor update | AIテンプレートの開始方法ガイドの著者情報の更新 | modified | 2 | 2 | 4 | 
| [create-hub-project-sdk.md](#item-8c3e99) | minor update | ハブプロジェクト作成ガイドの著者情報の更新 | modified | 2 | 2 | 4 | 
| [index-build-consume-sdk.md](#item-2ee880) | minor update | インデックスの構築と利用に関するガイドの著者情報の更新 | modified | 2 | 2 | 4 | 
| [llama-index.md](#item-613372) | minor update | LlamaIndexとAzure AI Studioを使用したアプリケーション開発ガイドの著者情報の更新 | modified | 2 | 2 | 4 | 
| [sdk-overview.md](#item-d3ab19) | minor update | Azure AI SDKの概要ガイドの著者情報の更新 | modified | 2 | 2 | 4 | 
| [trace-local-sdk.md](#item-f7dfb5) | minor update | Prompt Flow SDKを使用したアプリケーションのトレースガイドの著者情報の更新 | modified | 2 | 2 | 4 | 
| [model-benchmarks.md](#item-82de8e) | minor update | Azure AI Studioにおけるモデルベンチマークガイドの著者情報の更新 | modified | 2 | 2 | 4 | 
| [chat-with-data.md](#item-0c0cfc) | minor update | データとのチャットに関するインクルードファイルの著者情報の更新 | modified | 3 | 3 | 6 | 
| [chat-without-data.md](#item-9fb83d) | minor update | データなしのチャットに関するインクルードファイルの著者情報の更新 | modified | 3 | 3 | 6 | 
| [create-hub.md](#item-9df177) | minor update | ハブの作成に関するインクルードファイルの著者情報の更新 | modified | 3 | 3 | 6 | 
| [create-projects.md](#item-676667) | minor update | プロジェクト作成に関するインクルードファイルの著者情報の更新 | modified | 3 | 3 | 6 | 
| [deploy-chat-model.md](#item-3cd743) | minor update | チャットモデルのデプロイに関するインクルードファイルの著者情報の更新 | modified | 3 | 3 | 6 | 
| [development-environment-config.md](#item-e347fe) | minor update | 開発環境設定に関するインクルードファイルの著者情報の更新 | modified | 2 | 2 | 4 | 
| [install-cli.md](#item-868060) | minor update | CLIインストールに関するインクルードファイルの著者情報の修正 | modified | 1 | 1 | 2 | 
| [install-python.md](#item-f5f09e) | minor update | Pythonインストールに関するインクルードファイルの著者情報の修正 | modified | 1 | 1 | 2 | 
| [index.yml](#item-68b5b4) | minor update | AIスタジオのインデックスファイルの著者情報とレビュアー情報の更新 | modified | 3 | 3 | 6 | 
| [command-r-deploy-start-from-project.png](#item-845a79) | minor update | デプロイ監視のメディアファイルの削除 | removed | 0 | 0 | 0 | 
| [breadcrumb-navigation.gif](#item-e9b43a) | minor update | パンくずナビゲーションGIFファイルの削除 | removed | 0 | 0 | 0 | 
| [get-started-code.md](#item-8a5082) | minor update | クイックスタートのコードにおける著者情報の更新 | modified | 2 | 2 | 4 | 
| [get-started-playground.md](#item-e4d7fb) | minor update | チャットプレイグラウンドガイドの著者情報の更新 | modified | 3 | 3 | 6 | 
| [region-support.md](#item-d402e1) | minor update | リージョンサポートガイドの著者情報の更新 | modified | 2 | 2 | 4 | 
| [deploy-chat-web-app.md](#item-987845) | minor update | チャットウェブアプリデプロイガイドのレビュー担当者の更新 | modified | 1 | 1 | 2 | 
| [screen-reader.md](#item-4dc029) | minor update | スクリーンリーダーガイドの著者情報の更新 | modified | 2 | 2 | 4 | 
| [what-is-ai-studio.md](#item-3ab62e) | minor update | AI Studioガイドのレビューおよび著者情報の更新 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/ai-services/language-service/concepts/configure-containers.md{#item-6f87ab}

<details>
<summary>Diff</summary>
````diff
@@ -23,6 +23,7 @@ Language service provides each container with a common configuration framework,
 * Text Analytics for Health
 * Summarization
 * Named Entity Recognition (NER)
+* Personally Identifiable (PII) detection
 
 ## Configuration settings
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテナの設定にPII検出を追加"
}
```

### Explanation
この修正は、Azure AIサービスに関するドキュメントの「configure-containers.md」ファイルに対して行われました。特に、言語サービスの設定に新しい機能が追加されています。具体的には、以前のリストに「個人を特定できる情報（PII）検出」が追加されました。この変更は、コンテナの設定についての情報を更新し、ユーザーがPIIの検出機能を利用できることを明示しています。今回の修正は、テキスト分析サービスの強化に寄与するものです。

## articles/ai-services/language-service/personally-identifiable-information/how-to/use-containers.md{#item-8c61d4}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,147 @@
+---
+title: Use personally identifiable information Docker containers on-premises
+titleSuffix: Azure AI services
+description: Use Docker containers for the Personally Identifiable Information API to determine the language of written text, on-premises.
+#services: cognitive-services
+author: jboback
+manager: nitinme
+ms.service: azure-ai-language
+ms.custom:
+ms.topic: how-to
+ms.date: 10/07/2024
+ms.author: jboback
+keywords: on-premises, Docker, container
+---
+
+# Install and run Personally Identifiable Information (PII) Detection containers
+
+> [!NOTE]
+> The data limits for the PII container are 5120 characters and 10 documents max.
+
+Containers enable you to host the PII detection API on your own infrastructure. If you have security or data governance requirements that can't be fulfilled by calling PII detection remotely, then containers might be a good option.
+
+If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/cognitive-services/) before you begin.
+
+## Prerequisites
+
+You must meet the following prerequisites before using PII detection containers. 
+
+* If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/cognitive-services/).
+* [Docker](https://docs.docker.com/) installed on a host computer. Docker must be configured to allow the containers to connect with and send billing data to Azure. 
+    * On Windows, Docker must also be configured to support Linux containers.
+    * You should have a basic understanding of [Docker concepts](https://docs.docker.com/get-started/overview/). 
+* A <a href="https://portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics"  title="Create a Language resource"  target="_blank">Language resource </a>
+
+[!INCLUDE [Gathering required parameters](../../../containers/includes/container-gathering-required-parameters.md)]
+
+## Host computer requirements and recommendations
+
+[!INCLUDE [Host Computer requirements](../../../includes/cognitive-services-containers-host-computer.md)]
+
+The following table describes the minimum and recommended specifications for the available container. Each CPU core must be at least 2.6 gigahertz (GHz) or faster.
+
+It is recommended to have a CPU with AVX-512 instruction set, for the best experience (performance and accuracy).
+
+|                     | Minimum host specs     | Recommended host specs |
+|---------------------|------------------------|------------------------|
+| **PII detection**   | 1 core, 2GB memory     | 4 cores, 8GB memory    |
+
+CPU core and memory correspond to the `--cpus` and `--memory` settings, which are used as part of the `docker run` command.
+
+## Get the container image with `docker pull`
+
+The PII detection container image can be found on the `mcr.microsoft.com` container registry syndicate. It resides within the `azure-cognitive-services/textanalytics/` repository and is named `pii`. The fully qualified container image name is, `mcr.microsoft.com/azure-cognitive-services/textanalytics/pii`
+
+ To use the latest version of the container, you can use the `latest` tag, which is for English. You can also find a full list of containers for supported languages using the [tags on the MCR](https://mcr.microsoft.com/product/azure-cognitive-services/textanalytics/pii/tags).
+
+The latest PII detection container is available in several languages. To download the container for the English container, use the command below. 
+
+```
+docker pull mcr.microsoft.com/azure-cognitive-services/textanalytics/pii:latest
+```
+
+[!INCLUDE [Tip for using docker list](../../../includes/cognitive-services-containers-docker-list-tip.md)]
+
+## Run the container with `docker run`
+
+Once the container is on the host computer, use the [docker run](https://docs.docker.com/engine/reference/commandline/run/) command to run the containers. The container will continue to run until you stop it. Replace the placeholders below with your own values:
+
+
+> [!IMPORTANT]
+> * The docker commands in the following sections use the back slash, `\`, as a line continuation character. Replace or remove this based on your host operating system's requirements. 
+> * The `Eula`, `Billing`, and `ApiKey` options must be specified to run the container; otherwise, the container won't start.  For more information, see [Billing](#billing).
+
+To run the PII detection container, execute the following `docker run` command. Replace the placeholders below with your own values:
+
+| Placeholder | Value | Format or example |
+|-------------|-------|---|
+| **{API_KEY}** | The key for your Language resource. You can find it on your resource's **Key and endpoint** page, on the Azure portal. |`xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`|
+| **{ENDPOINT_URI}** | The endpoint for accessing the API. You can find it on your resource's **Key and endpoint** page, on the Azure portal. | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
+| **{IMAGE_TAG}** | The image tag representing the language of the container you want to run. Make sure this matches the `docker pull` command you used. | `latest` |
+
+```bash
+docker run --rm -it -p 5000:5000 --memory 8g --cpus 1 \
+mcr.microsoft.com/azure-cognitive-services/textanalytics/pii:{IMAGE_TAG} \
+Eula=accept \
+Billing={ENDPOINT_URI} \
+ApiKey={API_KEY}
+```
+
+This command:
+
+* Runs a *PII detection* container from the container image
+* Allocates one CPU core and 8 gigabytes (GB) of memory
+* Exposes TCP port 5000 and allocates a pseudo-TTY for the container
+* Automatically removes the container after it exits. The container image is still available on the host computer.
+
+[!INCLUDE [Running multiple containers on the same host](../../../includes/cognitive-services-containers-run-multiple-same-host.md)]
+
+## Query the container's prediction endpoint
+
+The container provides REST-based query prediction endpoint APIs.
+
+Use the host, `http://localhost:5000`, for container APIs.
+
+<!-- ## Validate container is running -->
+
+[!INCLUDE [Container's API documentation](../../../includes/cognitive-services-containers-api-documentation.md)]
+
+For information on how to call PII see [our guide](../how-to-call.md).
+
+## Run the container disconnected from the internet
+
+[!INCLUDE [configure-disconnected-container](../../../containers/includes/configure-disconnected-container.md)]
+
+## Stop the container
+
+[!INCLUDE [How to stop the container](../../../includes/cognitive-services-containers-stop.md)]
+
+## Troubleshooting
+
+If you run the container with an output [mount](../../concepts/configure-containers.md#mount-settings) and logging enabled, the container generates log files that are helpful to troubleshoot issues that happen while starting or running the container.
+
+[!INCLUDE [Azure AI services FAQ note](../../../containers/includes/cognitive-services-faq-note.md)]
+
+## Billing
+
+The PII detection containers send billing information to Azure, using a _Language_ resource on your Azure account.
+
+[!INCLUDE [Container's Billing Settings](../../../includes/cognitive-services-containers-how-to-billing-info.md)]
+
+For more information about these options, see [Configure containers](../../concepts/configure-containers.md).
+
+## Summary
+
+In this article, you learned concepts and workflow for downloading, installing, and running PII detection containers. In summary:
+
+* PII detection provides Linux containers for Docker
+* Container images are downloaded from the Microsoft Container Registry (MCR).
+* Container images run in Docker.
+* You must specify billing information when instantiating a container.
+
+> [!IMPORTANT]
+> Azure AI containers are not licensed to run without being connected to Azure for metering. Customers need to enable the containers to communicate billing information with the metering service at all times. Azure AI containers do not send customer data (e.g. text that is being analyzed) to Microsoft.
+
+## Next steps
+
+* See [Configure containers](../../concepts/configure-containers.md) for configuration settings.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しいコンテナ使用法に関するドキュメントの追加"
}
```

### Explanation
この修正は、Azure AIサービスにおける個人を特定できる情報（PII）に関する新しいドキュメントファイル「use-containers.md」の追加を含みます。このドキュメントは、オンプレミス環境でのPII検出APIをホストするためのDockerコンテナの使用に関する詳細な手順を提供します。

新たに追加されたドキュメントには、Dockerコンテナのインストール、実行、ホストコンピュータの要件、コンテナイメージの取得方法、コンテナの実行方法、APIエンドポイントへのクエリ方法、トラブルシューティング、及び請求に関する情報が含まれています。特に、セキュリティやデータガバナンスの要件を満たすために、リモートでPII検出を呼び出すことができないユーザーに対して、ローカルでのコンテナ使用のオプションが強調されています。この修正は、エンドユーザーが自身のインフラでPII検出機能を享受できるようにする重要な一歩です。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -424,6 +424,18 @@ items:
         href: personally-identifiable-information/how-to-call.md
       - name: Call PII for conversations
         href: personally-identifiable-information/how-to-call-for-conversations.md
+      - name: Use containers
+        items:
+          - name: Use Docker containers
+            href: personally-identifiable-information/how-to/use-containers.md
+          - name: Configure containers
+            href: concepts/configure-containers.md
+          - name: Use container instances
+            href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
+          - name: Use containers in disconnected environments
+            href: ../containers/disconnected-containers.md
+          - name: Azure AI containers overview
+            href: ../cognitive-services-container-support.md
     - name: Concepts
       items:
       - name: Recognized entity categories
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次にコンテナ使用に関する項目を追加"
}
```

### Explanation
この修正では、Azure AIサービスに関する「toc.yml」ファイルが更新され、個人を特定できる情報（PII）に関連する新しいセクションが追加されました。具体的には、「Use containers」という項目が追加され、その中に「Use Docker containers」、「Configure containers」、「Use container instances」、「Use containers in disconnected environments」、および「Azure AI containers overview」という5つのサブ項目が含まれています。

この変更は、ユーザーがコンテナを使用する際に必要な情報を容易に見つけられるようにすることを目的としており、ドキュメント内のナビゲーションの向上につながります。これにより、ユーザーは個人を特定できる情報を扱うためのガイドラインや設定についての理解を深めることができます。

## articles/ai-studio/ai-services/connect-ai-services.md{#item-3f7954}

<details>
<summary>Diff</summary>
````diff
@@ -16,8 +16,6 @@ author: eric-urban
 
 # Connect AI services to your hub in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
-
 You can try out AI services for free in Azure AI Studio as described in the [getting started with AI services](get-started.md) article. This article describes how to use AI services connections to do more via Azure AI Studio, SDKs, and APIs. 
 
 After you create a hub with AI services, you can use the AI services connection via the AI Studio UI, APIs, and SDKs. For example, you can try out AI services via **Home** > **AI Services** in the AI Studio UI as shown here.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIサービス接続に関する文書から不要な要素を削除"
}
```

### Explanation
この修正では、「connect-ai-services.md」ファイルから2行のコンテンツが削除されました。具体的には、記事の冒頭にあった「Feature preview」のインクルードタグが削除され、これにより文書がよりシンプルになっています。

削除されたこの要素は、AIサービスの機能プレビューの情報へのリンクを提供していましたが、著者の判断により、現在の文脈では不要とされ、より明確で読みやすい内容にするための更新と考えられます。この変更は、ユーザーがAIサービスとの接続についての情報をスムーズに理解できるようにすることを目的としています。

## articles/ai-studio/ai-services/get-started.md{#item-8378f4}

<details>
<summary>Diff</summary>
````diff
@@ -15,8 +15,6 @@ author: eric-urban
 
 # Get started with AI services in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
-
 This article describes how to get started with AI services in [Azure AI Studio](https://ai.azure.com). You can connect to AI services in Azure AI Studio to use AI capabilities such as Azure OpenAI, Speech, Language, Translator, Vision, Document Intelligence, and Content Safety.
 
 Go to the **Home** page and then select **AI Services** from the left pane to explore these services.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIサービス入門文書から不要な要素を削除"
}
```

### Explanation
この修正では、「get-started.md」ファイルから2行のコンテンツが削除されました。具体的には、記事の冒頭にあった「Feature preview」のインクルードタグが削除され、文書がより簡潔になっています。

削除されたこの要素は、AIサービスの機能プレビューに関する情報を読者に提供していましたが、著者の判断により、現在の内容には不必要とされました。この変更により、記事の内容はより明確で、読者がAzure AI StudioでAIサービスを利用する方法についての情報を効果的に理解できるようになっています。

## articles/ai-studio/concepts/connections.md{#item-01b26a}

<details>
<summary>Diff</summary>
````diff
@@ -9,15 +9,13 @@ ms.custom:
   - build-2024
 ms.topic: conceptual
 ms.date: 5/21/2024
-ms.reviewer: eur
-ms.author: eur
-author: eric-urban
+ms.reviewer: sgilley
+ms.author: sgilley
+author: sdgilley
 ---
 
 # Connections in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
-
 Connections in Azure AI Studio are a way to authenticate and consume both Microsoft and non-Microsoft resources within your AI Studio projects. For example, connections can be used for prompt flow, training data, and deployments. [Connections can be created](../how-to/connections-add.md) exclusively for one project or shared with all projects in the same hub. 
 
 ## Connections to Azure AI services
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "接続に関する文書の著者情報とレビュー担当者を更新"
}
```

### Explanation
この修正では、「connections.md」ファイルのメタデータと本文が変更されました。具体的には、著者とレビュー担当者の情報が更新され、もともと「eric-urban」だった著者が「sdgilley」に変更され、レビュー担当者も「eur」から「sgilley」に更新されました。

また、記事の冒頭にあった「Feature preview」のインクルードタグが削除され、文章がより簡潔になっています。これにより、文書の焦点がより明確になり、Azure AI Studioにおける接続の重要性や機能についての説明が強調されています。この変更は、更新された担当者が文書に関与していることを反映し、最新の情報を提供することを目的としています。

## articles/ai-studio/concepts/content-filtering.md{#item-91b372}

<details>
<summary>Diff</summary>
````diff
@@ -16,8 +16,6 @@ author: PatrickFarley
 
 # Content filtering in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
-
 Azure AI Studio includes a content filtering system that works alongside core models and DALL-E image generation models.
 
 > [!IMPORTANT]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルター文書から不要な要素を削除"
}
```

### Explanation
この修正では、「content-filtering.md」ファイルから2行のコンテンツが削除されました。具体的には、記事の冒頭にあった「Feature preview」のインクルードタグが削除され、文章がよりシンプルになっています。

この変更は、Azure AI Studioにおけるコンテンツフィルタリングシステムの説明に焦点を当てることを目的としており、あまり重要でない要素を取り除くことで、文書の流れを改善しています。結果として、読み手はAzure AI Studioのコンテンツフィルタリング機能について、より明瞭に理解できるようになります。

## articles/ai-studio/concepts/fine-tuning-overview.md{#item-31b07b}

<details>
<summary>Diff</summary>
````diff
@@ -8,9 +8,9 @@ ms.custom:
   - build-2024
 ms.topic: conceptual
 ms.date: 5/29/2024
-ms.reviewer: eur
-ms.author: eur
-author: eric-urban
+ms.reviewer: sgilley
+ms.author: sgilley
+author: sdgilley
 ---
 
 # Fine-tune models in Azure AI Studio
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングの概要における著者情報とレビュー担当者の更新"
}
```

### Explanation
この修正では、「fine-tuning-overview.md」ファイルのメタデータが変更されました。具体的には、著者とレビュー担当者の情報が更新され、もともとは「eric-urban」と記載されていた著者が「sdgilley」に変更され、レビュー担当者も「eur」から「sgilley」に変更されました。

これにより、文書は新しい担当者に関連付けられ、最新の情報が反映されています。この更新は、Azure AI Studioにおけるファインチューニングモデルの使用に関する信頼性を向上させ、担当者が適切な情報を提供できるようにするためのものです。この変更は、文書の整合性を保ちつつ、最新の著者情報を確実にすることを目的としています。

## articles/ai-studio/concepts/retrieval-augmented-generation.md{#item-c98880}

<details>
<summary>Diff</summary>
````diff
@@ -9,15 +9,13 @@ ms.custom:
   - build-2024
 ms.topic: conceptual
 ms.date: 5/21/2024
-ms.reviewer: eur
-ms.author: eur
-author: eric-urban
+ms.reviewer: sgilley
+ms.author: sgilley
+author: sdgilley
 ---
 
 # Retrieval augmented generation and indexes
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
-
 This article talks about the importance and need for Retrieval Augmented Generation (RAG) and index in generative AI. 
 
 ## What is RAG?
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "情報更新と不要な要素の削除"
}
```

### Explanation
この修正では、「retrieval-augmented-generation.md」ファイルのメタデータと内容が一部変更されました。具体的には、著者およびレビュー担当者の情報が更新され、元の著者「eric-urban」が「sdgilley」に変更され、レビュー担当者も「eur」から「sgilley」に代わりました。

さらに、記事の冒頭にあった「Feature preview」のインクルードタグが削除され、他に2行のテキストが削除されることで、内容が簡略化されています。この変更は、文書を最新の担当者情報に適合させつつ、情報の流れを改善し、読者にとってより明瞭な内容を提供する目的があります。結果的に、記事はRetrieval Augmented Generation（RAG）やインデックスに関する重要性についての明確な説明がより強調されています。

## articles/ai-studio/faq.yml{#item-e7baa2}

<details>
<summary>Diff</summary>
````diff
@@ -9,9 +9,9 @@ metadata:
     - build-2024
   ms.topic: faq
   ms.date: 5/21/2024
-  ms.reviewer: eur
-  ms.author: eur
-  author: eric-urban
+  ms.reviewer: sgilley
+  ms.author: sgilley
+  author: sdgilley
 title: Azure AI frequently asked questions
 summary: |
   If you can't find answers to your questions in this document, and still need help check the [Azure AI services support options guide](../ai-services/cognitive-services-support-options.md?context=/azure/ai-services/openai/context/context). Azure OpenAI is part of Azure AI services.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQファイルの著者情報とレビュー担当者の更新"
}
```

### Explanation
この修正では、「faq.yml」ファイルのメタデータが更新されました。具体的には、著者およびレビュー担当者の情報が変更され、以前は「eric-urban」と記載されていた著者が「sdgilley」に、レビュー担当者は「eur」から「sgilley」に変更されました。

これにより、文書の管理や責任が最新の担当者に適切に反映されるようになります。この更新は、Azure AIに関連するFAQの信頼性を高め、情報を提供する際の一貫性を保つために重要です。また、文書全体のユーザーフィードバックに基づいて、必要なサポートオプションへのリンクも保持されており、引き続きユーザーが必要な情報にアクセスしやすい状態が維持されています。

## articles/ai-studio/how-to/connections-add.md{#item-6f5a17}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ Here's a table of some of the available connection types in Azure AI Studio. The
 | Azure Blob Storage | ✓ | Azure Blob Storage is a cloud storage solution for storing unstructured data like documents, images, videos, and application installers. |
 | Azure Data Lake Storage Gen 2 | ✓ | Azure Data Lake Storage Gen2 is a set of capabilities dedicated to big data analytics, built on Azure Blob storage. |
 | Azure Content Safety | ✓ | Azure AI Content Safety is a service that detects potentially unsafe content in text, images, and videos. |
-| Azure OpenAI || Azure OpenAI is a service that provides access to the OpenAI GPT-3 model. |
+| Azure OpenAI || Azure OpenAI is a service that provides access to OpenAI's models including the GPT-4o, GPT-4o mini, GPT-4, GPT-4 Turbo with Vision, GPT-3.5-Turbo, DALLE-3 and Embeddings model series with the security and enterprise capabilities of Azure. |
 | Serverless Model | ✓ | Serverless Model connections allow you to [serverless API deployment](deploy-models-serverless.md). |
 | Microsoft OneLake | ✓ | Microsoft OneLake provides open access to all of your Fabric items through Azure Data Lake Storage (ADLS) Gen2 APIs and SDKs.<br/><br/>In Azure AI Studio you can set up a connection to your OneLake data using a OneLake URI. You can find the information that Azure AI Studio requires to construct a __OneLake Artifact URL__ (workspace and item GUIDs) in the URL on the Fabric portal. For information about the URI syntax, see [Connecting to Microsoft OneLake](/fabric/onelake/onelake-access-api). |
 | API key || API Key connections handle authentication to your specified target on an individual basis. For example, you can use this connection with the SerpApi tool in prompt flow.  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスの説明のアップデート"
}
```

### Explanation
この修正では、「connections-add.md」ファイル内のAzure OpenAIサービスに関する説明が更新されました。具体的には、Azure OpenAIに関する記述が強化され、従来の説明に加えて、提供されるモデルの多様性を詳細に説明しています。

以前は、Azure OpenAIは「OpenAI GPT-3モデルへのアクセスを提供するサービス」と記載されていましたが、更新後は「OpenAIのモデル（GPT-4o、GPT-4o mini、GPT-4、GPT-4 Turbo with Vision、GPT-3.5-Turbo、DALLE-3、Embeddingsモデルシリーズ）を含むサービス」となり、Azureのセキュリティとエンタープライズ機能も強調されています。

この変更により、ユーザーはAzure OpenAIが提供する機能の幅広さをよりよく理解できるようになり、実際の利用においての選択肢が明確になります。これは、ユーザーがAzure AI Studioでのデータ接続を効果的に活用するのに役立つ情報の提供を目指しています。

## articles/ai-studio/how-to/data-image-add.md{#item-a1f038}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom:
   - build-2024
 ms.topic: how-to
 ms.date: 5/21/2024
-ms.reviewer: eur
+ms.reviewer: sgilley
 ms.author: pafarley
 author: PatrickFarley
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ画像追加ガイドのレビュー担当者の更新"
}
```

### Explanation
この修正では、「data-image-add.md」ファイルのメタデータにおいてレビュー担当者が更新されました。具体的には、以前は「eur」というユーザーがレビュー担当者として指定されていましたが、更新後は「sgilley」に変更されています。

この変更は、文書のレビューと承認プロセスにおいて、新しい担当者による確認を反映させることを目的としています。文書の品質と正確性を維持するために重要な更新であり、今後の検討やフィードバックにより、ユーザーに対してより信頼性の高い情報を提供するための基盤となります。

## articles/ai-studio/how-to/develop/ai-template-get-started.md{#item-d71b59}

<details>
<summary>Diff</summary>
````diff
@@ -7,8 +7,8 @@ ms.service: azure-ai-studio
 ms.topic: how-to
 ms.date: 5/21/2024
 ms.reviewer: dantaylo
-ms.author: eur
-author: eric-urban
+ms.author: sgilley
+author: sdgilley
 ---
 
 # How to get started with an AI template
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIテンプレートの開始方法ガイドの著者情報の更新"
}
```

### Explanation
この修正では、「ai-template-get-started.md」ファイルのメタデータにおいて著者情報が更新されました。以前は「eur」というユーザー名が著者として指定されていましたが、変更後は「sgilley」という名前に更新されています。また、著者のフィールドも「eric-urban」から「sdgilley」に変更されました。

これらの変更は、文書の執筆者情報の正確性を保つことを目的としており、ユーザーが文書の信頼性や関連性を評価する際に重要な要素となります。この更新によって、ガイドにアクセスする人々は、現在の著者が誰であるかを正確に把握できるようになり、近時の情報を受け取ることができるようになります。

## articles/ai-studio/how-to/develop/create-hub-project-sdk.md{#item-8c3e99}

<details>
<summary>Diff</summary>
````diff
@@ -8,8 +8,8 @@ ms.custom: build-2024, devx-track-azurecli
 ms.topic: how-to
 ms.date: 5/21/2024
 ms.reviewer: dantaylo
-ms.author: eur
-author: eric-urban
+ms.author: sgilley
+author: sdgilley
 ---
 
 # Create a hub using the Azure Machine Learning SDK and CLI
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハブプロジェクト作成ガイドの著者情報の更新"
}
```

### Explanation
この修正では、「create-hub-project-sdk.md」ファイルのメタデータにおいて著者情報が更新されました。具体的には、以前の著者「eur」が「sgilley」に変更され、著者名も「eric-urban」から「sdgilley」に更新されています。

この変更は、文書の執筆者情報を最新のものにすることを目的としており、ユーザーがガイドの内容に対する信頼性を評価するために重要です。適切な著者情報が提供されることにより、ユーザーは文書に対するフィードバックや問い合わせを行う際に、正しい担当者と連絡を取ることができるようになります。

## articles/ai-studio/how-to/develop/index-build-consume-sdk.md{#item-2ee880}

<details>
<summary>Diff</summary>
````diff
@@ -9,8 +9,8 @@ ms.custom:
 ms.topic: how-to
 ms.date: 5/21/2024
 ms.reviewer: dantaylo
-ms.author: eur
-author: eric-urban
+ms.author: sgilley
+author: sdgilley
 ---
 
 # How to build and consume an index using code
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスの構築と利用に関するガイドの著者情報の更新"
}
```

### Explanation
この修正は、「index-build-consume-sdk.md」ファイルにおいて、著者情報が更新されたことを示しています。具体的には、以前は「eur」というユーザー名が使用されていましたが、変更後は「sgilley」に、また著者名も「eric-urban」から「sdgilley」に更新されています。

この更新は文書の著者情報を正確に保つことを目的としており、ユーザーがその内容の信頼性を検証するのに重要です。著者情報が明記されることで、利用者は文書に関するフィードバックや質問を行う際に、正しい執筆者にアプローチできるようになります。このような情報の透明性は、文書の利用価値を向上させる要素となります。

## articles/ai-studio/how-to/develop/llama-index.md{#item-613372}

<details>
<summary>Diff</summary>
````diff
@@ -7,8 +7,8 @@ ms.service: azure-ai-studio
 ms.topic: how-to
 ms.date: 9/14/2024
 ms.reviewer: fasantia
-ms.author: eur
-author: eric-urban
+ms.author: sgilley
+author: sdgilley
 ---
 
 # Develop applications with LlamaIndex and Azure AI studio
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "LlamaIndexとAzure AI Studioを使用したアプリケーション開発ガイドの著者情報の更新"
}
```

### Explanation
この修正では、「llama-index.md」ファイルにおいて著者情報が更新されています。具体的には、以前の著者「eur」が「sgilley」に変更され、著者名も「eric-urban」から「sdgilley」に更新されています。

この変更は、文書の著者情報を最新のものに保つために行われました。適切な著者情報が記載されることにより、ユーザーはガイドの内容に対する信頼性を評価しやすくなり、フィードバックや質問を行う際に正しい宛先に連絡できるようになります。文書の透明性と信頼性を向上させるため、著者情報の更新は重要な施策です。

## articles/ai-studio/how-to/develop/sdk-overview.md{#item-d3ab19}

<details>
<summary>Diff</summary>
````diff
@@ -9,8 +9,8 @@ ms.custom:
 ms.topic: overview
 ms.date: 8/9/2024
 ms.reviewer: dantaylo
-ms.author: eur
-author: eric-urban
+ms.author: sgilley
+author: sdgilley
 ---
 
 # Overview of the Azure AI SDKs
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI SDKの概要ガイドの著者情報の更新"
}
```

### Explanation
この修正は、「sdk-overview.md」ファイルにおける著者情報の更新を示しています。具体的には、以前の著者「eur」が「sgilley」に変更され、著者名も「eric-urban」から「sdgilley」に変更されました。

著者情報を最新のものに更新することは、文書の透明性を維持し、利用者がその情報の信頼性を評価するのに役立ちます。利用者は、文書に関する質問やフィードバックを行う際に、適切な担当者に連絡を取ることができるようになります。このような更新は、文書の内容を正確に反映させ、全体的な利用価値を向上させるために重要です。

## articles/ai-studio/how-to/develop/trace-local-sdk.md{#item-f7dfb5}

<details>
<summary>Diff</summary>
````diff
@@ -9,8 +9,8 @@ ms.custom:
 ms.topic: how-to
 ms.date: 5/21/2024
 ms.reviewer: chenlujiao
-ms.author: eur
-author: eric-urban
+ms.author: sgilley
+author: sdgilley
 ---
 
 # How to trace your application with prompt flow SDK | Azure AI Studio
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Prompt Flow SDKを使用したアプリケーションのトレースガイドの著者情報の更新"
}
```

### Explanation
この修正は、「trace-local-sdk.md」ファイル内での著者情報の更新を示しています。変更内容としては、以前の著者「eur」が「sgilley」に改訂され、著者名も「eric-urban」から「sdgilley」に変更されています。

著者情報の更新は、文書の信頼性や透明性を確保するために重要です。正確な著者情報を提供することで、利用者は適切な担当者にコンタクトしやすくなり、ガイドの内容に対する信頼感を高めます。このようなマイナーアップデートは、文書の整合性を維持し、ユーザーが重要な情報にアクセスできるようにするために役立ちます。

## articles/ai-studio/how-to/model-benchmarks.md{#item-82de8e}

<details>
<summary>Diff</summary>
````diff
@@ -9,8 +9,8 @@ ms.custom:
 ms.topic: how-to
 ms.date: 5/21/2024
 ms.reviewer: jcioffi
-ms.author: eur
-author: eric-urban
+ms.author: sgilley
+author: sdgilley
 ---
 
 # Model benchmarks in Azure AI Studio
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioにおけるモデルベンチマークガイドの著者情報の更新"
}
```

### Explanation
この修正は、「model-benchmarks.md」ファイル内での著者情報の更新を示しています。具体的には、著者情報が変更され、以前の著者「eur」が「sgilley」に改訂され、著者名も「eric-urban」から「sdgilley」に更新されています。

著者情報の更新は、ドキュメントの信頼性を高めるために不可欠です。利用者が文書の作成者を把握することで、質問やフィードバックを行う際に適切な連絡先に到達しやすくなります。このようなマイナーな変更ですが、情報の正確性を保ち、利用者の信頼を得るために重要です。

## articles/ai-studio/includes/chat-with-data.md{#item-0c0cfc}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +1,9 @@
 ---
 title: include file
 description: include file
-author: eur
-ms.reviewer: eur
-ms.author: eric-urban
+author: sdgilley
+ms.reviewer: sgilley
+ms.author: sgilley
 ms.service: azure-ai-studio
 ms.topic: include
 ms.date: 5/21/2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データとのチャットに関するインクルードファイルの著者情報の更新"
}
```

### Explanation
この修正は、「chat-with-data.md」ファイル内での著者情報の更新を反映しています。具体的には、著者名が「eur」から「sdgilley」に変更され、レビューアも「eur」から「sgilley」に更新されています。また、著者に関するマークアップが一貫性を持つように調整されています。

著者やレビューアの情報を正確に記載することは、文書の信頼性と透明性を保つ上で重要です。ユーザーが適切な担当者にアクセスできるようにすることで、フィードバックや問い合わせを円滑に行えるようになります。このようなマイナーな変更は、文書の整合性を強化し、使用する上での利便性を向上させるものとなります。

## articles/ai-studio/includes/chat-without-data.md{#item-9fb83d}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +1,9 @@
 ---
 title: include file
 description: include file
-author: eur
-ms.reviewer: eur
-ms.author: eric-urban
+author: sdgilley
+ms.reviewer: sgilley
+ms.author: sgilley
 ms.service: azure-ai-studio
 ms.topic: include
 ms.date: 5/21/2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データなしのチャットに関するインクルードファイルの著者情報の更新"
}
```

### Explanation
この修正は、「chat-without-data.md」ファイルの著者情報を更新した内容です。具体的には、著者名が「eur」から「sdgilley」に変更され、レビューア名も「eur」から「sgilley」に修正されています。これにより、著者とレビューアの情報が一貫性を持つようになっています。

著者やレビューアの情報を明確にすることは、文書の信頼性を維持し、ユーザーが適切な連絡先にアクセスしてフィードバックを行うために重要です。このようなマイナーな変更は、ドキュメントの整合性を保ち、利用者の利便性を向上させる役割を果たします。

## articles/ai-studio/includes/create-hub.md{#item-9df177}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +1,9 @@
 ---
 title: include file
 description: include file
-author: eur
-ms.reviewer: eur
-ms.author: eric-urban
+author: sdgilley
+ms.reviewer: sgilley
+ms.author: sgilley
 ms.service: azure-ai-studio
 ms.topic: include
 ms.date: 5/21/2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハブの作成に関するインクルードファイルの著者情報の更新"
}
```

### Explanation
この修正では、「create-hub.md」ファイル内の著者情報が更新されました。具体的には、著者名が「eur」から「sdgilley」に変更され、レビューアおよび著者に関する情報もそれぞれ「eur」と「eric-urban」から「sgilley」に修正されています。これにより、文書内の著者に関する情報が適切で一貫性のあるものになります。

著者とレビューア名を正確に記載することは、文書の透明性や信頼性を高め、ユーザーが適切な連絡先にアプローチできるようにするために重要です。このようなマイナーな更新は、ドキュメントの品質を向上させ、利用者にとっての利便性を促進します。

## articles/ai-studio/includes/create-projects.md{#item-676667}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +1,9 @@
 ---
 title: include file
 description: include file
-author: eur
-ms.reviewer: eur
-ms.author: eric-urban
+author: sdgilley
+ms.reviewer: sgilley
+ms.author: sgilley
 ms.service: azure-ai-studio
 ms.topic: include
 ms.date: 5/21/2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクト作成に関するインクルードファイルの著者情報の更新"
}
```

### Explanation
この修正では、「create-projects.md」ファイルの著者情報が更新されました。具体的な変更内容として、著者名が「eur」から「sdgilley」に、レビューアおよび著者に記載されている情報も同様に「eur」と「eric-urban」から「sgilley」に変更されています。これにより、文書内の著者やレビューアに関する情報が正確で一貫性を持つようになります。

正確な著者情報を記載することで、読む人に信頼性を提供し、フィードバックや問い合わせが行いやすくなります。このようなマイナーな更新は、文書の品質を向上させ、ユーザーエクスペリエンスをより良いものにする重要な要素です。

## articles/ai-studio/includes/deploy-chat-model.md{#item-3cd743}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +1,9 @@
 ---
 title: include file
 description: include file
-author: eur
-ms.reviewer: eur
-ms.author: eric-urban
+author: sdgilley
+ms.reviewer: sgilley
+ms.author: sgilley
 ms.service: azure-ai-studio
 ms.topic: include
 ms.date: 8/8/2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットモデルのデプロイに関するインクルードファイルの著者情報の更新"
}
```

### Explanation
この修正では、「deploy-chat-model.md」ファイル内の著者情報が更新されました。変更内容としては、著者が「eur」から「sdgilley」に、レビューアおよび他の著者情報がそれぞれ「eur」と「eric-urban」から「sgilley」に変更されています。これにより、文書内の著者に関する情報が最新かつ正確なものになります。

著者情報の正確な記載は、ドキュメントの品質と信頼性を高め、ユーザーが必要な場合に適切な連絡先にアプローチしやすくするために重要です。このようなマイナーな更新を行うことで、全体的な文書の整合性と透明性が向上し、ユーザーエクスペリエンスの向上に寄与します。

## articles/ai-studio/includes/development-environment-config.md{#item-e347fe}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,11 @@
 ---
 title: include file
 description: include file
-author: eric-urban
+author: sdgilley
 ms.service: azure-ai-studio
 ms.topic: include
 ms.date: 5/21/2024
-ms.author: eur
+ms.author: sgilley
 ms.custom: include file, build-2024
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "開発環境設定に関するインクルードファイルの著者情報の更新"
}
```

### Explanation
この修正では、「development-environment-config.md」ファイルの著者情報が更新されています。具体的な変更内容には、著者が「eric-urban」から「sdgilley」に変わり、著者に関する情報も「eur」から「sgilley」に更新されています。これにより、文書内の著者の記載が最新のものとなります。

著者情報の正確な更新は、ドキュメントの信頼性を強化し、ユーザーが必要な情報を得るために適切な連絡を取れるようにします。このようなマイナーな変更は、ドキュメント全体の品質を向上させ、ユーザーエクスペリエンスをさらに良いものにする重要なステップです。

## articles/ai-studio/includes/install-cli.md{#item-868060}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: include file
 description: include file
 author: sdgilley
 ms.reviewer: sgilley
-ms.author: esgiley
+ms.author: sgilley
 ms.service: azure-ai-studio
 ms.topic: include
 ms.date: 08/29/2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "CLIインストールに関するインクルードファイルの著者情報の修正"
}
```

### Explanation
この修正では、「install-cli.md」ファイル内の著者情報が調整されています。具体的には、元の「ms.author」が「esgiley」であったのが「sgilley」に変更されました。この小さな修正により、著者情報が正確に更新され、ドキュメントの信頼性が向上します。

著者情報の正確な表示は、ユーザーが文書の作成者に適切にコンタクトできるようにするため重要です。このようなマイナーな変更は、文書全体の整合性や透明性を向上させ、ユーザーエクスペリエンスを向上させる役割を果たします。

## articles/ai-studio/includes/install-python.md{#item-f5f09e}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: include file
 description: include file
 author: sdgilley
 ms.reviewer: sgilley
-ms.author: esgiley
+ms.author: sgilley
 ms.service: azure-ai-studio
 ms.topic: include
 ms.date: 08/29/2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonインストールに関するインクルードファイルの著者情報の修正"
}
```

### Explanation
この修正は「install-python.md」ファイルに関連しており、著者情報が更新されています。具体的には、「ms.author」の情報が「esgiley」から「sgilley」に変更されました。この変更により、著者情報が正確で最新のものとして提供されるようになります。

著者の正確な表示は、文書の信頼性を向上させ、特にユーザーが適切な情報源や連絡先にアクセスできるようにするために重要です。この程度のマイナーな変更でも、ドキュメントの整合性と透明性に寄与し、全体的なユーザーエクスペリエンスを向上させる効果があります。

## articles/ai-studio/index.yml{#item-68b5b4}

<details>
<summary>Diff</summary>
````diff
@@ -10,9 +10,9 @@ metadata:
     - build-2024
     - copilot-learning-hub
   ms.topic: landing-page
-  ms.reviewer: eur
-  ms.author: eur
-  author: eric-urban
+  ms.reviewer: sgilley
+  ms.author: sgilley
+  author: sdgilley
   ms.date: 5/21/2024
 # linkListType: architecture | concept | deploy | download | get-started | how-to-guide | learn | overview | quickstart | reference | tutorial | video | whats-new
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIスタジオのインデックスファイルの著者情報とレビュアー情報の更新"
}
```

### Explanation
この変更では、「index.yml」ファイルにおける著者とレビュアーの情報が更新されています。具体的には、「ms.reviewer」、「ms.author」、および「author」の各フィールドが変更されました。元々「eur」となっていたレビュアー情報は「sgilley」に変更され、著者情報は「eur」から「sgilley」に、また「eric-urban」から「sdgilley」に更新されています。

これらの変更により、文書の作成に関与した人々の情報が最新となり、ユーザーが信頼できる情報源を識別しやすくなります。正確な著者情報とレビュアー情報は、ドキュメントの信頼性を高め、より良いユーザーエクスペリエンスを提供するために重要です。

## articles/ai-studio/media/deploy-monitor/cohere-command/command-r-deploy-start-from-project.png{#item-845a79}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイ監視のメディアファイルの削除"
}
```

### Explanation
この変更は、AIスタジオのデプロイ監視に関連するメディアファイル「command-r-deploy-start-from-project.png」の削除を示しています。このファイルはもはやリポジトリに存在せず、今後のドキュメントには表示されません。

ファイルの削除は、内容の更新や整理を目的として行われることがあります。場合によっては、古くなった、または重複したコンテンツをクリーンアップするために必要です。この変更により、視覚素材や情報を効率的に管理し、ユーザーにとっての文書の関連性が保たれることが期待されます。

## articles/ai-studio/media/explore/breadcrumb-navigation.gif{#item-e9b43a}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "パンくずナビゲーションGIFファイルの削除"
}
```

### Explanation
この変更は、「breadcrumb-navigation.gif」というGIFファイルの削除を表しています。このファイルは、AIスタジオのナビゲーションに関連していたメディア素材です。しかし、現在のリポジトリには存在しません。

ファイルの削除は、ドキュメントの整理や視覚素材の更新の一環として行われることがあり、古い情報や重複したコンテンツを排除することで、ユーザーにとっての関連性が向上することが期待されます。この変更により、ドキュメントの品質が保たれ、読み手が必要とする情報をより簡潔に得られるようになります。

## articles/ai-studio/quickstarts/get-started-code.md{#item-8a5082}

<details>
<summary>Diff</summary>
````diff
@@ -8,8 +8,8 @@ ms.custom: build-2024, devx-track-azurecli, devx-track-python
 ms.topic: how-to
 ms.date: 8/6/2024
 ms.reviewer: dantaylo
-ms.author: eur
-author: eric-urban
+ms.author: sgilley
+author: sdgilley
 ---
 
 # Build a custom chat app in Python using the prompt flow SDK
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートのコードにおける著者情報の更新"
}
```

### Explanation
この変更は、「get-started-code.md」ファイルの修正を示しており、著者情報が更新されています。特に、著者の名前が「eur」から「sgilley」に変更され、また「eric-urban」という名前が「sdgilley」に修正されています。この変更は、ドキュメントの執筆者を正確に反映させるために行われました。

追加された行数は2行、削除された行数も2行で、合計で4箇所の変更が行われています。これにより、ドキュメントが最新の情報に更新され、関連する著者の認知度が向上します。この修正は、特にコラボレーションやレビューの過程で重要な文書の透明性を保つために必要です。

## articles/ai-studio/quickstarts/get-started-playground.md{#item-e4d7fb}

<details>
<summary>Diff</summary>
````diff
@@ -8,9 +8,9 @@ ms.custom:
   - build-2024
 ms.topic: tutorial
 ms.date: 5/21/2024
-ms.reviewer: eur
-ms.author: eur
-author: eric-urban
+ms.reviewer: sgilley
+ms.author: sgilley
+author: sdgilley
 ---
 
 # Quickstart: Create a project and use the chat playground in Azure AI Studio
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットプレイグラウンドガイドの著者情報の更新"
}
```

### Explanation
この変更は、「get-started-playground.md」ファイルの修正を示し、著者及びレビュー担当者の情報が更新されています。具体的には、レビュー担当者が「eur」から「sgilley」に変更され、著者も同様に「eur」から「sgilley」、さらに「eric-urban」から「sdgilley」に修正されています。

追加された行数は3行、削除された行数も3行で、合計で6箇所の変更が行われています。この修正により、ドキュメントは最新の情報を反映し、正しい著者が表示されるようになります。これにより、クリアな責任の明確化がなされ、コラボレーションやレビューのプロセスが一層透明になります。これらの変更は、ユーザーがドキュメントの創作者を容易に認識できるようにすることを目的としています。

## articles/ai-studio/reference/region-support.md{#item-d402e1}

<details>
<summary>Diff</summary>
````diff
@@ -7,8 +7,8 @@ ms.service: azure-ai-studio
 ms.topic: conceptual
 ms.date: 5/21/2024
 ms.reviewer: deeikele
-ms.author: eur
-author: eric-urban
+ms.author: sgilley
+author: sdgilley
 ms.custom: references_regions, build-2024
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リージョンサポートガイドの著者情報の更新"
}
```

### Explanation
この変更は、「region-support.md」ファイルの修正を示しており、著者情報が更新されています。具体的には、著者の名前が「eur」から「sgilley」に変更され、また「eric-urban」という名前が「sdgilley」に修正されています。

今回の修正では、追加された行数が2行、削除された行数も2行で、合計で4箇所の変更が行われています。この更新により、ドキュメントは最新の著者情報を反映し、ユーザーが正確な情報を得られるように配慮されています。著者情報の明確化は、ドキュメントの信頼性を高め、関連するコンテンツにおける責任と透明性を向上させる重要な要素です。

## articles/ai-studio/tutorials/deploy-chat-web-app.md{#item-987845}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
 ms.topic: tutorial
 ms.date: 5/21/2024
-ms.reviewer: eur
+ms.reviewer: sgilley
 ms.author: aahi
 author: aahill
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットウェブアプリデプロイガイドのレビュー担当者の更新"
}
```

### Explanation
この変更は、「deploy-chat-web-app.md」ファイルの修正を示しており、レビュー担当者の情報が更新されています。具体的には、レビュー担当者が「eur」から「sgilley」に変更されています。

変更の内容としては、追加された行数が1行、削除された行数も1行で、合計で2箇所の変更が行われています。この更新により、ドキュメントには最新のレビュー担当者が反映され、利用者にとって信頼性の高い情報を提供できるようになっています。適切なレビュー担当者の明示は、ドキュメントの品質を向上させることにつながり、利用者が有益なリソースを得られるようにするために重要です。

## articles/ai-studio/tutorials/screen-reader.md{#item-4dc029}

<details>
<summary>Diff</summary>
````diff
@@ -10,8 +10,8 @@ ms.custom:
 ms.topic: quickstart
 ms.date: 8/9/2024
 ms.reviewer: ailsaleen
-ms.author: eur
-author: eric-urban
+ms.author: sgilley
+author: sdgilley
 ---
 
 # QuickStart: Get started using AI Studio with a screen reader
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スクリーンリーダーガイドの著者情報の更新"
}
```

### Explanation
この変更は、「screen-reader.md」ファイルの修正を示しており、著者情報が更新されています。具体的には、著者の名前が「eur」から「sgilley」に変更され、また「eric-urban」という名前が「sdgilley」に修正されています。

この修正では、追加された行数は2行、削除された行数も2行で、合計で4箇所の変更が行われています。この更新により、ドキュメントには最新の著者情報が反映され、ユーザーが正確な情報を得られるように配慮されています。著者情報の明確化は、ドキュメントの信頼性を高め、コンテンツに対するユーザーの信頼感を向上させる重要な要素となります。

## articles/ai-studio/what-is-ai-studio.md{#item-3ab62e}

<details>
<summary>Diff</summary>
````diff
@@ -7,9 +7,9 @@ keywords: Azure AI services, cognitive
 ms.service: azure-ai-studio
 ms.topic: overview
 ms.date: 5/21/2024
-ms.reviewer: eur
-ms.author: eur
-author: eric-urban
+ms.reviewer: sgilley
+ms.author: sgilley
+author: sdgilley
 ms.custom: ignite-2023, build-2024
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Studioガイドのレビューおよび著者情報の更新"
}
```

### Explanation
この変更は、「what-is-ai-studio.md」ファイルの修正を示しており、レビューおよび著者の情報が更新されています。具体的には、レビュー担当者が「eur」から「sgilley」に変更され、著者も「eur」から「sgilley」に、さらに別の著者名が「eric-urban」から「sdgilley」に修正されています。

この更新は、追加された行数が3行で、削除された行数も3行、合計で6箇所の変更が行われています。著者やレビュー担当者の情報が最新の内容に更新されることで、利用者はより正確で信頼性のある情報を得ることができ、コンテンツの品質向上につながります。このような著者情報の明確化は、ドキュメントの公信力を高め、ユーザー体験の向上に寄与します。


