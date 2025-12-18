---
date: '2025-12-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a67f1c9...MicrosoftDocs:a2d235e
summary: 今回の変更では、ドキュメントのアップデートと削除が行われ、特にいくつかのチュートリアルとガイドが削除されました。これにより、ユーザーは具体的な手順や参考情報を得るためのリソースを一部失いました。一方で、モデルデータのロードとエクスポートに関する新しい手順が追加され、REST
  API を利用した操作が強化されました。この変更は、Azure の AI サービスに関するドキュメントの最新化を図り、ユーザーの利便性向上を目指していますが、特に
  Language Studio に関する情報の削除が目立ち、REST API への移行が重要なフェーズとなっています。柔軟なドキュメント作成が求められており、プログラム
  API の使用方法を含む新しいガイドラインが期待されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a67f1c9...MicrosoftDocs:a2d235e){target="_blank"}

<format>
# ハイライト
今回の変更では、ドキュメントのアップデートおよび削除が多岐にわたっています。特に重要なのは、複数のチュートリアルとガイドが削除されたことで、ユーザーが具体的な手順や参考情報を得るためのリソースが一部失われる点です。また、新機能としてモデルデータのロードとエクスポートに関する手順が追加されるなど、REST API を中心としたアプローチへの移行が進んでいます。

## 新機能
- モデルデータのロードとエクスポート手順が新たに追加され、REST API を用いた操作が強化されました。

## 破壊的変更
- 多くのチュートリアル（例えば、FAQボット作成、ガイド付き会話、複数言語の対応等）が削除されたため、従来の手順に基づく情報を利用していたユーザーには影響が大きいです。
- Language Studio 絡みのプロジェクト作成やデプロイ手順の削除は、REST API を主体とした新たなガイドラインへのシフトを印象づけています。

## その他の更新
- ドキュメントのメタデータが更新され、最新の情報を反映する形となっていますが、意図的な簡略化も行われています。
- 一部のリンクや表現が最新のプラットフォーム名に合わせて修正されています。

# 洞察
これらの変更は、Azure の AI サービスに関するドキュメントをより最新化し、利用者にとって利便性を高めるための透明性ある情報提供を目指しているものです。しかし、具体的な削除が多く見られ、特に Language Studio を中心とした手順が欠落しているため、今後は REST API を中心にアプローチを切り替えるユーザーにとって重要なフェーズとなります。

技術的背景としては、サービスが より API 指向に移行していることが予測され、ユーザーがこの新しいワークフローに順応できるための代替ガイドラインの構築が必要です。例えば、プログラム的なスキルがないユーザーに向けた新しいドキュメントやソフトなガイドが提供されることが期待されます。

したがって、これからのドキュメンテーションは、旧来の GUI ベースの操作説明からプログラム API の使用方法までを包括的にカバーする範囲を持つことがますます重要になります。ユーザーは変化に対応しつつ、新たなドキュメントのツールを活かし、効果的に作業を進める必要があります。</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [multi-region-deployment.md](#item-a7351d) | minor update | マルチリージョンデプロイメントのドキュメントの修正 | modified | 2 | 2 | 4 | 
| [project-versioning.md](#item-ea8b01) | minor update | プロジェクトバージョニングに関するドキュメントの修正 | modified | 1 | 1 | 2 | 
| [developer-guide.md](#item-003b09) | minor update | 開発者ガイドのドキュメント修正 | modified | 4 | 4 | 8 | 
| [data-formats.md](#item-8bec0b) | minor update | カスタムNERのデータフォーマットに関するドキュメント修正 | modified | 4 | 4 | 8 | 
| [create-project.md](#item-092612) | minor update | カスタムNERプロジェクト作成に関する手順の修正 | modified | 5 | 39 | 44 | 
| [design-schema.md](#item-f4e4b1) | minor update | テストセットの定義に関する文書修正 | modified | 1 | 1 | 2 | 
| [tag-data.md](#item-3806db) | minor update | データインポート関連リンクの更新 | modified | 1 | 1 | 2 | 
| [train-model.md](#item-5e8f97) | minor update | トレーニングモデルセクションのREST API専用の修正 | modified | 5 | 16 | 21 | 
| [view-model-evaluation.md](#item-1d51d8) | minor update | モデル評価セクションの修正とREST APIの強調 | modified | 6 | 30 | 36 | 
| [cancel-training.md](#item-79482e) | breaking change | トレーニングキャンセルの手順の削除 | removed | 0 | 9 | 9 | 
| [create-project.md](#item-781e28) | breaking change | プロジェクト作成手順の削除 | removed | 0 | 36 | 36 | 
| [delete-deployment.md](#item-7a474b) | breaking change | デプロイメント削除手順の削除 | removed | 0 | 10 | 10 | 
| [delete-model.md](#item-03f8d0) | breaking change | モデル削除手順の削除 | removed | 0 | 15 | 15 | 
| [delete-project.md](#item-33d276) | breaking change | プロジェクト削除手順の削除 | removed | 0 | 10 | 10 | 
| [deploy-model.md](#item-86f8f0) | breaking change | モデルデプロイ手順の削除 | removed | 0 | 26 | 26 | 
| [import-project.md](#item-f8acb5) | breaking change | プロジェクトインポート手順の削除 | removed | 0 | 42 | 42 | 
| [model-evaluation.md](#item-cbdc16) | breaking change | モデル評価手順の削除 | removed | 0 | 82 | 82 | 
| [project-details.md](#item-8fb72c) | breaking change | プロジェクト詳細手順の削除 | removed | 0 | 20 | 20 | 
| [resource-creation-language-studio.md](#item-50fe52) | breaking change | リソース作成手順の削除 | removed | 0 | 28 | 28 | 
| [swap-deployment.md](#item-5e9d44) | breaking change | デプロイメントのスワップ手順の削除 | removed | 0 | 14 | 14 | 
| [train-model.md](#item-0551aa) | breaking change | モデルトレーニング手順の削除 | removed | 0 | 28 | 28 | 
| [load-export-model.md](#item-97a5ef) | new feature | モデルデータのロードとエクスポートの手順追加 | added | 81 | 0 | 81 | 
| [data-formats.md](#item-1e7da5) | minor update | データ形式に関する文書の修正 | modified | 5 | 5 | 10 | 
| [evaluation-metrics.md](#item-3803bc) | minor update | 評価指標に関する文書の修正 | modified | 1 | 2 | 3 | 
| [fail-over.md](#item-3ec67b) | minor update | フェイルオーバーに関する文書の日付更新 | modified | 1 | 1 | 2 | 
| [faq.md](#item-038891) | minor update | FAQ文書内のサービス名の更新 | modified | 1 | 1 | 2 | 
| [glossary.md](#item-ed0857) | minor update | 用語集のトピックタイプの更新 | modified | 1 | 1 | 2 | 
| [call-api.md](#item-30dce9) | minor update | API呼び出し方法に関する文書の更新 | modified | 14 | 35 | 49 | 
| [create-project.md](#item-648436) | minor update | カスタムテキスト分類プロジェクト作成手順の更新 | modified | 6 | 39 | 45 | 
| [deploy-model.md](#item-20d1af) | minor update | モデル展開手順の更新 | modified | 6 | 47 | 53 | 
| [design-schema.md](#item-991baa) | minor update | テキスト分類スキーマ設計手順の更新 | modified | 6 | 8 | 14 | 
| [tag-data.md](#item-e70f6f) | minor update | データタグ付け手順に関する更新 | modified | 4 | 4 | 8 | 
| [train-model.md](#item-2c59cc) | minor update | モデル訓練手順の更新 | modified | 2 | 15 | 17 | 
| [view-model-evaluation.md](#item-6afd37) | minor update | モデル評価ビューに関する更新 | modified | 4 | 29 | 33 | 
| [blob-storage-upload.md](#item-72f02e) | minor update | Blobストレージへのアップロード手順の更新 | modified | 7 | 5 | 12 | 
| [rest-api.md](#item-c7e987) | minor update | REST APIに関する簡潔な指示の整理 | modified | 5 | 5 | 10 | 
| [load-export-model.md](#item-f1827f) | minor update | モデルデータの読み込みに関するメタデータの修正 | modified | 1 | 1 | 2 | 
| [use-pre-existing-resource.md](#item-7bcdd8) | minor update | リソースのアイデンティティ管理手順の簡素化 | modified | 2 | 14 | 16 | 
| [language-support.md](#item-35327f) | minor update | 言語サポート情報の更新とメタデータの修正 | modified | 3 | 3 | 6 | 
| [overview.md](#item-ebc28d) | minor update | カスタムテキスト分類の説明文の更新 | modified | 2 | 2 | 4 | 
| [quickstart.md](#item-29d53a) | minor update | クイックスタートガイドのタイトルと内容の修正 | modified | 2 | 13 | 15 | 
| [service-limits.md](#item-6df7a9) | minor update | サービス制限に関するトピックの更新 | modified | 1 | 1 | 2 | 
| [triage-email.md](#item-47cadc) | minor update | メールのトリアージに関するチュートリアルの日付更新 | modified | 1 | 1 | 2 | 
| [azure-machine-learning-labeling.md](#item-d2e0c8) | breaking change | Azure Machine Learningラベリングに関する文書の削除 | removed | 0 | 130 | 130 | 
| [bot-service.md](#item-f8e773) | breaking change | FAQボット作成チュートリアルの削除 | removed | 0 | 86 | 86 | 
| [guided-conversations.md](#item-a43dd4) | breaking change | ガイド付き会話チュートリアルの削除 | removed | 0 | 90 | 90 | 
| [multiple-languages.md](#item-1966cb) | breaking change | 複数言語プロジェクト作成チュートリアルの削除 | removed | 0 | 86 | 86 | 
| [power-virtual-agents.md](#item-aec51d) | breaking change | Power Virtual Agentsへのカスタム質問応答プロジェクト追加チュートリアルの削除 | removed | 0 | 214 | 214 | 
| [toc.yml](#item-12f1f0) | minor update | 言語サービスの目次ファイルの更新 | modified | 0 | 16 | 16 | 


# Modified Contents
## articles/ai-services/language-service/concepts/custom-features/multi-region-deployment.md{#item-a7351d}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about how to deploy your custom language projects to multiple
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 12/05/2025
 ms.author: lajanuar
 ms.custom: language-service-clu, ignite-2024
@@ -43,7 +43,7 @@ The same request body to each of those different URLs serves the exact same resp
 
 ## Validations and requirements
 
-Assigning deployment resources requires Microsoft Entra authentication. Microsoft Entra ID is used to confirm that you have access to the resources that you want to assign to your project for multiregion deployment. In Language Studio, you can automatically [enable Microsoft Entra authentication](https://aka.ms/rbac-language) by assigning yourself the Azure Cognitive Services Language Owner role to your original resource. To programmatically use Microsoft Entra authentication, learn more from the [Foundry Tools documentation](../../../authentication.md?source=docs&tabs=powershell&tryIt=true#authenticate-with-azure-active-directory).
+Assigning deployment resources requires Microsoft Entra authentication. Microsoft Entra ID is used to confirm that you have access to the resources that you want to assign to your project for multiregion deployment. In Microsoft Foundry, you can automatically [enable Microsoft Entra authentication](https://aka.ms/rbac-language) by assigning yourself the Azure Cognitive Services Language Owner role to your original resource. To programmatically use Microsoft Entra authentication, learn more from the [Foundry Tools documentation](../../../authentication.md?source=docs&tabs=powershell&tryIt=true#authenticate-with-azure-active-directory).
 
 Your project name and resource are used as its main identifiers. A Language resource can only have a specific project name in each resource. Any other projects with the same name can't be deployed to that resource.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチリージョンデプロイメントのドキュメントの修正"
}
```

### Explanation
この修正では、マルチリージョンデプロイメントに関するドキュメントにおいて、いくつかの用語や関連情報が更新されました。具体的には、`ms.topic`フィールドの値が「conceptual」から「concept-article」に変更され、内容をより明確にしました。また、Microsoft Entraに関連する説明部分で、「Language Studio」という表現が「Microsoft Foundry」に置き換えられ、最新のサービス名称に合わせた修正が行われています。この修正により、ドキュメントの情報が正確で最新の状態となり、利用者にとっての理解が促進されることを目的としています。

## articles/ai-services/language-service/concepts/custom-features/project-versioning.md{#item-ea8b01}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ ms.reviewer: haelhamm
 
 Building your project typically happens in increments. You may add, remove, or edit intents, entities, labels, and data at each stage. Every time you train, a snapshot of your current project state is taken to produce a model. That model saves the snapshot to be loaded back at any time. Every model acts as its own version of the project.
 
-For example, if your project has 10 intents and/or entities, with 50 training documents or utterances, it can be trained to create a model named **v1**. Afterwards, you might make changes to the project to alter the numbers of training data. The project can be trained again to create a new model named **v2**. If you don't like the changes you made in **v2** and would like to continue from where you left off in model **v1**, then you would just need to load the model data from **v1** back into the project. Loading a model's data is possible through both Azure Language Studio and API. Once complete, the project has the original amount and types of training data.
+For example, if your project has 10 intents and/or entities, with 50 training documents or utterances, it can be trained to create a model named **v1**. Afterwards, you might make changes to the project to alter the numbers of training data. The project can be trained again to create a new model named **v2**. If you don't like the changes you made in **v2** and would like to continue from where you left off in model **v1**, then you would just need to load the model data from **v1** back into the project. Loading a model's data is possible through both Microsoft Foundry and API. Once complete, the project has the original amount and types of training data.
 
 If the project data isn't saved in a trained model, it can be lost. For example, if you loaded model **v1**, your project now has the data that was used to train it. If you then made changes, didn't train, and loaded model **v2**, you would lose those changes as they weren't saved to any specific snapshot.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクトバージョニングに関するドキュメントの修正"
}
```

### Explanation
この修正では、プロジェクトバージョニングに関するドキュメントの一部が更新されました。主な変更点は、「Azure Language Studio」という表現が「Microsoft Foundry」に変更された点です。この修正により、最新のサービス名称が反映され、利用者がドキュメントを参照する際に混乱が避けられます。全体として、この更新はプロジェクトのトレーニングモデルの管理についての理解を助けるものであり、ユーザーが異なるモデルバージョンを扱う際に重要な情報を提供しています。

## articles/ai-services/language-service/concepts/developer-guide.md{#item-003b09}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about how to integrate Azure Language service SDK and REST AP
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.author: lajanuar
 ---
@@ -40,7 +40,7 @@ The Language provides three namespaces for using the available features. Dependi
 The `Azure.AI.TextAnalytics` namespace enables you to use the following Language features. Use the following links for articles to help you send API requests using the SDK.
 
 * [Custom named entity recognition](../custom-named-entity-recognition/how-to/call-api.md?tabs=client)
-* [Custom text classification](../custom-text-classification/how-to/call-api.md?tabs=client-libraries#send-a-text-classification-request-to-your-model)
+* [Custom text classification](../custom-text-classification/how-to/call-api.md#send-a-text-classification-request-to-your-model-rest-api)
 * [Document summarization](../summarization/quickstart.md)
 * [Entity linking](../entity-linking/quickstart.md)
 * [Key phrase extraction](../key-phrase-extraction/quickstart.md)
@@ -107,7 +107,7 @@ The conversation analysis authoring API enables you to author custom models and
 * [Conversational language understanding](../conversational-language-understanding/quickstart.md?pivots=rest-api)
 * [Orchestration workflow](../orchestration-workflow/quickstart.md?pivots=rest-api)
 
-For more information, *see* the [reference documentation](/rest/api/language/2023-04-01/conversational-analysis-authoring).
+For more information, *see* the [reference documentation](/rest/api/language/).
 
 ### Conversation analysis runtime API
 
@@ -128,7 +128,7 @@ The text analysis authoring API enables you to author custom models and create/m
 * [Custom named entity recognition](../custom-named-entity-recognition/quickstart.md?pivots=rest-api)
 * [Custom text classification](../custom-text-classification/quickstart.md?pivots=rest-api)
 
-For more information, *see* the [reference documentation](/rest/api/language/2023-04-01/text-analysis-authoring).
+For more information, *see* the [reference documentation](/rest/api/language/).
 ### Text analysis runtime API
 
 The text analysis runtime API enables you to send requests to custom models you create for the following features:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "開発者ガイドのドキュメント修正"
}
```

### Explanation
この修正では、開発者ガイドに関するドキュメントにいくつかの重要な変更が加えられました。まず、`ms.topic`フィールドの値が「conceptual」から「concept-article」に変更され、情報の分類が明確になりました。また、いくつかのリンクが更新され、REST APIに関する情報へのアクセスが改善されました。具体的には、カスタムテキスト分類のリンクが変更され、より直接的な参照先が設定されています。さらに、複数のAPIに関連するリファレンスドキュメントのURLが一般的なものに修正され、ユーザーが必要な情報を見つけやすくなっています。これらの変更は、開発者がAzure Language サービスをより効果的に利用できるようにするための改善を目的としています。

## articles/ai-services/language-service/custom-named-entity-recognition/concepts/data-formats.md{#item-8bec0b}

<details>
<summary>Diff</summary>
````diff
@@ -5,18 +5,18 @@ description: Learn about the data formats accepted by custom NER.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-ner
 ---
 # Accepted custom NER data formats
 
-If you're trying to [import your data](../how-to/create-project.md#import-project) into custom NER, it has to follow a specific format. If you don't have data to import, you can [create your project](../how-to/create-project.md) and use [Microsoft Foundry](https://ai.azure.com/) to label your documents.
+If you're trying to [import your data](../how-to/create-project.md#import-project-rest-api) into custom NER, it has to follow a specific format. If you don't have data to import, you can [create your project](../how-to/create-project.md) and use [Microsoft Foundry](https://ai.azure.com/) to label your documents.
 
 ## Labels file format
 
-Your Labels file should be in `json` format for use in [importing](../how-to/create-project.md#import-project) your labels into a project.
+Your Labels file should be in `json` format for use in [importing](../how-to/create-project.md#import-project-rest-api) your labels into a project.
 
 ```json
 {
@@ -108,5 +108,5 @@ Your Labels file should be in `json` format for use in [importing](../how-to/cre
 
 
 ## Next steps
-* You can import your labeled data into your project directly. Learn how to [import project](../how-to/create-project.md#import-project)
+* You can import your labeled data into your project directly. Learn how to [import project](../how-to/create-project.md#import-project-rest-api)
 * See the [how-to article](../how-to/tag-data.md)  more information about labeling your data. When you're done labeling your data, you can [train your model](../how-to/train-model.md).  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムNERのデータフォーマットに関するドキュメント修正"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識（NER）のデータフォーマットに関するドキュメントが更新されました。主な変更点は、データのインポートに関するリンクが改訂され、特にREST APIに関連する情報が強調されました。具体的には、「import-project」というリンクが「import-project-rest-api」に変更され、情報の正確性が向上しています。また、各セクション内のラベルファイル形式に関連する部分にも同様のリンク修正が行われています。この更新によって、ユーザーはカスタムNERプロジェクトにデータを正しくインポートするための手順をより明確に理解できるようになり、関連する情報の参照が改善されます。

## articles/ai-services/language-service/custom-named-entity-recognition/how-to/create-project.md{#item-092612}

<details>
<summary>Diff</summary>
````diff
@@ -42,8 +42,6 @@ You can create a resource in the following ways:
 
 [!INCLUDE [create a new resource from the Azure portal](../includes/resource-creation-azure-portal.md)]
 
-[!INCLUDE [create a new resource from Language Studio](../includes/language-studio/resource-creation-language-studio.md)]
-
 [!INCLUDE [create a new resource with Azure PowerShell](../includes/resource-creation-powershell.md)]
 
 
@@ -55,58 +53,26 @@ You can create a resource in the following ways:
 
 [!INCLUDE [use an existing resource](../includes/use-pre-existing-resource.md)]
 
-## Create a custom named entity recognition project
-
-Once your resource and storage container are configured, create a new custom NER project. A project is a work area for building your custom AI models based on your data. Only you can access your project along with others who have access to the Azure resource being used. If you labeled data, you can use it to get started by [importing a project](#import-project).
-
-### [Language Studio](#tab/language-studio)
+## Create a custom named entity recognition project (REST API)
 
-[!INCLUDE [Language Studio project creation](../includes/language-studio/create-project.md)]
-
-### [REST APIs](#tab/rest-api)
+Once your resource and storage container are configured, create a new custom NER project. A project is a work area for building your custom AI models based on your data. Only you can access your project along with others who have access to the Azure resource being used. If you labeled data, you can use it to get started by [importing a project](#import-project-rest-api).
 
 [!INCLUDE [REST APIs project creation](../includes/rest-api/create-project.md)]
 
----
-
-## Import project
+## Import project (REST API)
 
 If you already labeled data, you can use it to get started with the service. Make sure that your labeled data follows the [accepted data formats](../concepts/data-formats.md).
 
-### [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Import project](../includes/language-studio/import-project.md)]
-
-### [REST APIs](#tab/rest-api)
-
 [!INCLUDE [Import project](../includes/rest-api/import-project.md)]
 
----
-
-## Get project details
-
-### [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Language Studio project details](../includes/language-studio/project-details.md)]
-
-### [REST APIs](#tab/rest-api)
+## Get project details (REST API)
 
 [!INCLUDE [REST APIs project details](../includes/rest-api/project-details.md)]
 
----
-
-## Delete project
-
-### [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Delete project using Language studio](../includes/language-studio/delete-project.md)]
-
-### [REST APIs](#tab/rest-api)
+## Delete project (REST API)
 
 [!INCLUDE [Delete project using the REST API](../includes/rest-api/delete-project.md)]
 
----
-
 ## Next steps
 
 * You should have an idea of the [project schema](design-schema.md) you use to label your data.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムNERプロジェクト作成に関する手順の修正"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識（NER）プロジェクトを作成する手順に関連するドキュメントが更新されました。主な変更点として、プロジェクト作成のセクションがREST APIに焦点を当てるように修正され、関連する情報や手順が整理されています。具体的には、プロジェクト作成やデータのインポートに関する部分が、Language StudioとREST APIの両方の文脈からの記述が統一され、REST APIに関する手順が紹介されるようになりました。

また、一部の講読やセクションが削除され、言語スタジオに関する内容が簡素化されたため、文書全体がより明瞭かつ簡潔になっています。これにより、ユーザーはカスタムNERプロジェクトを効率的に作成できるようになります。関連する手順や情報の一貫性が向上し、ユーザーが必要な情報をすぐに見つけやすくなっています。

## articles/ai-services/language-service/custom-named-entity-recognition/how-to/design-schema.md{#item-f4e4b1}

<details>
<summary>Diff</summary>
````diff
@@ -64,7 +64,7 @@ You can upload an annotated dataset, or you can upload an unannotated one and la
  
 ## Test set
 
-When defining the testing set, make sure to include example documents that aren't present in the training set. Defining the testing set is an important step to calculate the [model performance](view-model-evaluation.md#model-details). Also, make sure that the testing set include documents that represent all entities used in your project.
+When defining the testing set, make sure to include example documents that aren't present in the training set. Defining the testing set is an important step to calculating the [model performance](view-model-evaluation.md#model-details-rest-api). Also, make sure that the testing set includes documents that represent all entities used in your project.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テストセットの定義に関する文書修正"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識（NER）のデザインスキーマに関するドキュメントが更新されました。具体的には、テストセットを定義する際の内容がわずかに修正されており、文法的な改善が行われています。変更された部分では、「model performance」に関連するリンクが改訂され、静的な情報からREST APIに特化した情報に更新されました。また、テストセットに関する説明の文が若干修正され、正確性が増しています。

これにより、ユーザーはテストセットの定義に関する情報をより明確に理解でき、モデルのパフォーマンスを計算する際に必要な要点を把握しやすくなっています。全体として、この変更は文書の精度向上に寄与しており、ユーザーがETLプロセスを通じてより良いデータ品質を得るための手助けとなります。

## articles/ai-services/language-service/custom-named-entity-recognition/how-to/tag-data.md{#item-3806db}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.custom: language-service-custom-ner
 ---
 # Label your data in Azure Language in Foundry Tools Studio
 
-Before training your model, you need to label your documents with the custom entities you want to extract. Data labeling is a crucial step in development lifecycle. You can create the entity types you want to extract from your data and label these entities within your documents. This data is used in the next step when training your model so that your model can learn from the labeled data. If you already labeled data, you can directly [import](create-project.md#import-project) it into your project, but you need to make sure that your data follows the [accepted data format](../concepts/data-formats.md). See [create project](create-project.md#import-project) to learn more about importing labeled data into your project.
+Before training your model, you need to label your documents with the custom entities you want to extract. Data labeling is a crucial step in development lifecycle. You can create the entity types you want to extract from your data and label these entities within your documents. This data is used in the next step when training your model so that your model can learn from the labeled data. If you already labeled data, you can directly [import](create-project.md#import-project-rest-api) it into your project, but you need to make sure that your data follows the [accepted data format](../concepts/data-formats.md). See [create project](create-project.md#import-project-rest-api) to learn more about importing labeled data into your project.
 
 Before creating a custom NER model, you first need to label your data. If your data isn't labeled already, you can label it in the [Language Studio](https://aka.ms/languageStudio). Labeled data informs the model how to interpret text, and is used for training and evaluation.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データインポート関連リンクの更新"
}
```

### Explanation
この修正では、Azure Language Serviceを用いたカスタムネーミングエンティティ認識（NER）のためのデータラベリングに関する文書が更新されました。具体的には、ラベル付けされたデータをプロジェクトにインポートするためのリンクがREST APIに関連するリンクに更新されています。この変更により、ユーザーはインポート手順を参照する際に、より正確な情報を得られるようになりました。

また、文全体の構成は維持されており、データラベリングが開発ライフサイクルにおいて重要なステップであることや、ラベル付けされたデータがモデルのトレーニングに使用されることが強調されています。このような小規模な修正でも、文書の正確性と一貫性が向上しており、ユーザーがプロジェクトに必要なデータを正しく取り扱うための助けとなります。

## articles/ai-services/language-service/custom-named-entity-recognition/how-to/train-model.md{#item-5e8f97}

<details>
<summary>Diff</summary>
````diff
@@ -44,38 +44,27 @@ Custom NER supports two methods for data splitting:
 
 * **Use a manual split of training and testing data**: This method enables users to define which labeled documents should belong to which set. This step is only enabled if you added documents to your testing set during [data labeling](tag-data.md).
 
-## Train model
+## Train model (REST API)
 
-# [Language studio](#tab/Language-studio)
-
-[!INCLUDE [Train model](../includes/language-studio/train-model.md)]
-
-# [REST APIs](#tab/REST-APIs)
+Once you have labeled your data and configured your data split settings, you can start training your custom NER model using the REST API. The training process involves submitting a training job request and monitoring its progress until completion. This section provides the API calls needed to initiate training and check the status of your training job.
 
 ### Start training job
 
 [!INCLUDE [train model](../includes/rest-api/train-model.md)]
 
-### Get training job status
+### Get training job status (REST API)
 
 Training can take some time, depending on the size of your training data and complexity of your schema. You can use the following request to keep polling the status of the training job until successful completion.
 
  [!INCLUDE [get training model status](../includes/rest-api/get-training-status.md)]
 
----
-
-### Cancel training job
 
-# [Language Studio](#tab/language-studio)
+### Cancel training job (REST API)
 
-[!INCLUDE [Cancel training](../includes/language-studio/cancel-training.md)]
-
-# [REST APIs](#tab/rest-api)
+If you need to stop a training job that's currently in progress, you can cancel it using the REST API. Canceling a training job is useful when you discover an issue with your data or configuration and want to make corrections before restarting the training process.
 
 [!INCLUDE [Cancel training](../includes/rest-api/cancel-training.md)]
 
----
-
 ## Next steps
 
 After training is completed, you'll be able to view [model performance](view-model-evaluation.md) to optionally improve your model if needed. Once you're satisfied with your model, you can deploy it, making it available to use for [extracting entities](call-api.md) from text.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トレーニングモデルセクションのREST API専用の修正"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識（NER）のモデルをトレーニングする方法に関するドキュメントが更新されました。主な変更点は、「トレインモデル」というセクションがREST APIに特化した内容に改訂されたことです。これにより、ユーザーはデータをラベル付けし、データ分割の設定を行った後、REST APIを使用してカスタムNERモデルのトレーニングを開始できることが明確に示されています。

具体的には、トレーニングジョブを申請するためのAPI呼び出しや、トレーニングジョブの進行状況をモニタリングするためのリクエストについての説明が追加されています。また、トレーニングジョブをキャンセルする方法に関する情報もREST APIに特化した内容に更新され、データや設定に問題がある場合にトレーニングプロセスを修正できる手段が提供されています。

全体として、この変更により、ユーザーがREST APIを使用してトレーニングプロセスを効率的に管理できるようになり、文書の整合性と実用性が向上しました。

## articles/ai-services/language-service/custom-named-entity-recognition/how-to/view-model-evaluation.md{#item-1d51d8}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.custom: language-service-custom-ner
 ---
 # View the custom NER model's evaluation and details
 
-After your model has finished training, you can view the model performance and see the extracted entities for the documents in the test set. 
+After your model finishes training, you can view the model performance and see the extracted entities for the documents in the test set. 
 
 > [!NOTE]
 > Using the **Automatically split the testing set from training data** option may result in different model evaluation result every time you [train a new model](train-model.md), as the test set is selected randomly from the data. To make sure that the evaluation is calculated on the same test set every time you train a model, make sure to use the **Use a manual split of training and testing data** option when starting a training job and define your **Test** documents when [labeling data](tag-data.md).
@@ -26,45 +26,21 @@ Before viewing model evaluation, you need:
 * [Labeled data](tag-data.md)
 * A [successfully trained model](train-model.md)
 
-See the [project development lifecycle](../overview.md#project-development-lifecycle) for more information.
+For more information, *see* the [project development lifecycle](../overview.md#project-development-lifecycle).
 
-## Model details
-
-### [Language studio](#tab/language-studio)
-
-[!INCLUDE [View model evaluation using Language Studio](../includes/language-studio/model-evaluation.md)]
-
-### [REST APIs](#tab/rest-api)
+## Model details (REST API)
 
 [!INCLUDE [Model evaluation](../includes/rest-api/model-evaluation.md)]
 
----
-
-## Load or export model data
-
-### [Language studio](#tab/Language-studio)
 
-[!INCLUDE [Load export model](../../conversational-language-understanding/includes/language-studio/load-export-model.md)]
+## Load or export model data (REST API)
 
+[!INCLUDE [Load export model](../includes/rest-api/load-export-model.md)]
 
-### [REST APIs](#tab/REST-APIs)
-
-[!INCLUDE [Load export model](../../custom-text-classification/includes/rest-api/load-export-model.md)]
-
----
-
-## Delete model
-
-### [Language studio](#tab/language-studio)
-
-[!INCLUDE [Delete model](../includes/language-studio/delete-model.md)]
-
-### [REST APIs](#tab/rest-api)
+## Delete model (REST API)
 
 [!INCLUDE [Delete model](../includes/rest-api/delete-model.md)]
 
----
-
 ## Next steps
 
 * [Deploy your model](deploy-model.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル評価セクションの修正とREST APIの強調"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識（NER）のモデル評価に関するドキュメントが更新され、内容が整備されました。主な変更点には、文章の表現を簡潔にするための文言の修正と、REST APIに関連する情報を強調するためのセクション修正が含まれています。

具体的には、モデルがトレーニングを終えた後の性能評価についての説明が見直され、「自動的にテストセットをトレーニングデータから分割する」というオプションの使用によって、テストセットが毎回異なる可能性があることが指摘されています。これにより、一貫した評価を行うために手動でテストドキュメントを定義するべきであると明記されています。

また、従来は「Language Studio」と「REST APIs」の両方が別々のセクションに記載されていた部分が、REST APIに特化したセクションに整理され、APIを利用することでモデル評価やデータの読み込み・エクスポート、モデル削除の手順が明確化されています。

これらの変更により、ユーザーはモデル評価に必要なステップや手段についての理解が深まるとともに、REST APIの利用を促進する内容へと進化しています。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/language-studio/cancel-training.md{#item-79482e}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To cancel a training job from within [Language Studio](https://aka.ms/languageStudio), go to the **Training jobs** page. Select the training job you want to cancel and select **Cancel** from the top menu. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "トレーニングキャンセルの手順の削除"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識（NER）のドキュメント内にあった「トレーニングキャンセル」セクションが削除されました。このセクションには、Language Studioからトレーニングジョブをキャンセルするための具体的な手順が説明されていました。

具体的には、ユーザーが「トレーニングジョブ」ページにアクセスし、キャンセルしたいトレーニングジョブを選択して「キャンセル」ボタンをクリックするというフローが記載されていました。しかし、この内容が削除されたことで、ユーザーはトレーニングジョブのキャンセル方法に関する情報を失うことになります。

この変更により、ユーザーがトレーニングキャンセルの手段について指示を受ける場がなくなり、今後の使用に際しての注意が必要です。このような重大な変更は、ユーザーが今後の操作を行う際に影響を及ぼす可能性があるため、ドキュメントの他の部分で代替の情報を提供する必要があります。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/language-studio/create-project.md{#item-781e28}

<details>
<summary>Diff</summary>
````diff
@@ -1,36 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Sign into the [Language Studio](https://aka.ms/languageStudio). A window appears to let you select your subscription and Language resource. Select Azure Language resource you created in the previous step. 
-
-2. Under the **Extract information** section of Language Studio, select **Custom named entity recognition**.
-
-    :::image type="content" source="../../media/select-custom-ner.png" alt-text="A screenshot showing the location of custom named entity recognition (NER) in Azure Language Studio landing page." lightbox="../../media/select-custom-ner.png":::
-
-3. Select **Create new project** from the top menu in your projects page. Creating a project lets you tag data, train, evaluate, improve, and deploy your models. 
-
-    :::image type="content" source="../../media/create-project.png" alt-text="A screenshot of the project creation page." lightbox="../../media/create-project.png":::
-
-4.  After you select, **Create new project**, a window appears to let you connect your storage account. If you already connected a storage account, the connected storage accounted appears in the window. If not, choose your storage account from the dropdown that appears and select **Connect storage account**; this sets the required roles for your storage account. This step can return an error if you aren't assigned as **owner** on the storage account.
-
-    >[!NOTE]
-    > * You only need to do this step once for each new resource you use. 
-    > * This process is irreversible, if you connect a storage account to your Language resource you can't disconnect it later.
-    > * You can only connect your Language resource to one storage account.
-    
-    :::image type="content" source="../../media/connect-storage.png" alt-text="A screenshot showing the storage connection screen." lightbox="../../media/connect-storage.png":::
-
-5. Enter the project information, including a name, description, and the language of the files in your project. If you're using the [example dataset](https://go.microsoft.com/fwlink/?linkid=2175226), select **English**. You can't change the name of your project later. Select **Next**
-
-    > [!TIP]
-    > Your dataset doesn't have to be entirely in the same language. You can have multiple documents, each with different supported languages. If your dataset contains documents of different languages or if you expect text from different languages during runtime, select **enable multi-lingual dataset** option when you enter the basic information for your project. This option can be enabled later from the **Project settings** page.
-
-6. Select the container where you uploaded your dataset. 
-If you already labeled data make sure it follows the [supported format](../../concepts/data-formats.md) and select **Yes, my files are already labeled and I have formatted JSON labels file** and select the labels file from the drop-down menu. Select **Next**.
-
-7. Review the data you entered and select **Create Project**.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト作成手順の削除"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識（NER）に関するドキュメントの「プロジェクト作成」に関するセクションが削除されました。このセクションは、Language Studioで新しいプロジェクトを作成するためのステップバイステップの手順を詳細に説明しており、具体的には以下のような内容が含まれていました。

1. Language Studioへのサインイン方法
2. カスタムネーミングエンティティ認識の選択方法
3. 新しいプロジェクトの作成手順
4. ストレージアカウントの接続手順
5. プロジェクト情報の入力方法
6. データセットが保存されているコンテナの選択
7. プロジェクトの作成確認と実行手順

これらの重要な情報が削除されたことにより、ユーザーはプロジェクト作成の具体的な手順を参照することができなくなります。この変更は、新規ユーザーにとって非常に大きな影響を及ぼす可能性があり、プロジェクト作成の際に戸惑うことが考えられます。新しい情報や代替のリソースについての指示が必要とされる状況です。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/language-studio/delete-deployment.md{#item-7a474b}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +0,0 @@
----
-titleSuffix: Foundry Tools
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To delete a deployment from within [Language Studio](https://aka.ms/laguageStudio), go to the **Deploying a model** page. Select the deployment you want to delete and select **Delete deployment** from the top menu. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "デプロイメント削除手順の削除"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識に関するドキュメント内の「デプロイメント削除」に関するセクションが削除されました。このセクションには、Language Studio内でデプロイメントを削除するための手順が記載されており、ユーザーが特定のデプロイメントを選択し、メニューから「デプロイメント削除」を選択する流れが説明されていました。

この重要な情報が削除されることで、ユーザーはデプロイメントを削除する具体的な手順を失います。これにより、誤ってデプロイメントを削除する手段を失ったり、必要な場合にデプロイメントを削除する方法を見つけるのが難しくなる可能性があります。特に、デプロイメント管理に関する明確な指示が欲しいユーザーにとって、この変更は大きな影響を及ぼすことが考えられます。したがって、代替の情報や指示が必要です。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/language-studio/delete-model.md{#item-03f8d0}

<details>
<summary>Diff</summary>
````diff
@@ -1,15 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To delete your model from within the [Language Studio](https://aka.ms/LanguageStudio):
-
-1. Select **Model performance** from the left side menu.
-
-2. Select the **model name** you want to delete and select **Delete** from the top menu.
-
-3. In the window that appears, select **OK** to delete the model. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデル削除手順の削除"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識に関連するドキュメントの「モデル削除」に関するセクションが削除されました。このセクションは、Language Studio内でモデルを削除するための具体的な手順を提供していました。具体的には、次のような手順が含まれていました。

1. 左側のメニューから「モデルパフォーマンス」を選択すること。
2. 削除したいモデル名を選び、トップメニューから「削除」を選択すること。
3. 表示されるウィンドウで「OK」を選択し、モデルを削除すること。

この内容の削除により、ユーザーはモデルを適切に削除する方法についての情報を失います。その結果、モデルの管理や誤った削除のリスクが増大し、特に新規ユーザーにとっては、必要な情報を見つけるのが困難になる可能性があります。この変更は、モデル管理に関する具体的な指示を必要とするユーザーに対して大きな影響を与えるでしょう。したがって、代替の情報やガイダンスを提供する必要があります。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/language-studio/delete-project.md{#item-33d276}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
-ms.custom: language-service-custom-classification
----
-When you don't need your project anymore, you can delete your project using [Language Studio](https://aka.ms/custom-extraction). Select **Custom named entity recognition (NER)** from the top, select the project you want to delete, and then select **Delete** from the top menu.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト削除手順の削除"
}
```

### Explanation
この修正により、カスタムネーミングエンティティ認識に関するドキュメントの中で、プロジェクトを削除する方法に関するセクションが削除されました。削除されていた内容には、プロジェクトを削除するための具体的な手順が記載されており、次のような流れが含まれていました：

- Language Studioにアクセスして、プロジェクトが不要になった場合に行うべき手順を説明。
- 画面上部から「カスタムネーミングエンティティ認識（NER）」を選択し、削除したいプロジェクトを選択すること。
- トップメニューから「削除」を選択することでプロジェクトを削除できる旨が指示されていました。

この手順の削除により、ユーザーはプロジェクトを管理し、不要なものを削除するための具体的な情報を失うことになります。特に、プラットフォームを初めて使用するユーザーにとっては、プロジェクト管理のプロセスが不明瞭になり、意図しない混乱を招く可能性があります。この変更は、ユーザーがプロジェクトを適切に管理する上での重要な指示を欠くことから、注意が必要です。今後、代替の指示やガイダンスを提供することが望まれます。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/language-studio/deploy-model.md{#item-86f8f0}

<details>
<summary>Diff</summary>
````diff
@@ -1,26 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To deploy your model from within the [Language Studio](https://aka.ms/LanguageStudio):
-
-1. Select **Deploying a model** from the left side menu.
-
-2. Select **Add deployment** to start a new deployment job.
-
-    :::image type="content" source="../../media/deploy-model.png" alt-text="A screenshot showing the deployment button" lightbox="../../media/deploy-model.png":::
-
-3. Select **Create new deployment** to create a new deployment and assign a trained model from the dropdown. You can also **Overwrite an existing deployment** by selecting this option and select the trained model you want to assign to it from the dropdown.
-
-    > [!NOTE]
-    > Overwriting an existing deployment doesn't require changes to your [prediction API](https://aka.ms/ct-runtime-swagger) call but the results you get are based on the newly assigned model.
-    
-   :::image type="content" source="../../media/add-deployment.png" alt-text="A screenshot showing the deployment screen" lightbox="../../media/add-deployment.png":::
-     
-4. Select **Deploy** to start the deployment job.
-
-5. After deployment is successful, an expiration date will appear next to it. [Deployment expiration](../../../concepts/model-lifecycle.md#expiration-timeline) is when your deployed model will be unavailable to be used for prediction, which typically happens **twelve** months after a training configuration expires.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルデプロイ手順の削除"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識に関するドキュメントの「モデルデプロイ」に関するセクションが削除されました。このセクションは、Language Studio内でモデルをデプロイするための具体的な手順を詳細に説明していました。削除されていた内容には、次のようなステップが含まれていました：

1. 左側のメニューから「モデルのデプロイ」を選択すること。
2. 「デプロイメントの追加」を選択して新しいデプロイメントジョブを開始すること。
3. 新しいデプロイを作成し、ドロップダウンからトレーニング済みのモデルを割り当てること。また、既存のデプロイを上書きするオプションも提供。
4. 「デプロイ」を選択し、デプロイメントジョブを開始すること。
5. デプロイメントが成功した後に、モデルの有効期限が表示されること。

これらの手順の削除により、ユーザーはモデルをデプロイする方法を知らなくなり、特に初めてこのシステムを使用するユーザーにとっては大きな混乱を引き起こす可能性があります。また、デプロイされたモデルの有効期限に関する重要な情報も失われます。この変更は、ユーザーがモデルをデプロイし、そこから予測を行うための重要なガイダンスを欠いていることから、事前に代替の指示やサポートを提供することが望まれます。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/language-studio/import-project.md{#item-f8acb5}

<details>
<summary>Diff</summary>
````diff
@@ -1,42 +0,0 @@
----
-titleSuffix: Foundry Tools
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Sign into the [Language Studio](https://aka.ms/languageStudio). A window appears to let you select your subscription and Language resource. Select your Language resource. 
-
-2. Under the **Extract information** section of Language Studio, select **Custom named entity recognition**.
-
-    :::image type="content" source="../../media/select-custom-ner.png" alt-text="A screenshot showing the location of the custom `NER` feature in Azure Language Studio landing page." lightbox="../../media/select-custom-ner.png":::
-        
-
-3. Select **Create new project** from the top menu in your projects page. Creating a project lets you tag data, train, evaluate, improve, and deploy your models. 
-
-    :::image type="content" source="../../media/create-project.png" alt-text="A screenshot of the project creation page." lightbox="../../media/create-project.png":::
-
-
-4.  After you select **Create new project**, a screen will appear to let you connect your storage account. If you can't find your storage account, make sure you created a resource using the recommended steps. If you've already connected a storage account to your Language resource, you can see your storage account connected.
-
-    >[!NOTE]
-    > * You only need to do this step once for each new language resource you use. 
-    > * This process is irreversible, if you connect a storage account to your Language resource you can't disconnect it later.
-    > * You can only connect your Language resource to one storage account.
-
-    :::image type="content" source="../../media/connect-storage.png" alt-text="A screenshot of the storage connection screen for new projects." lightbox="../../media/connect-storage.png":::
-
-4. Enter the project information, including a name, description, and the language of the files in your project. You can't change the name of your project later. Select **Next**.
-       
-    >[!TIP]
-    > Your dataset doesn't have to be entirely in the same language. You can have multiple documents, each with different supported languages. If your dataset contains documents of different languages or if you expect text from different languages during runtime, select **enable multi-lingual dataset** option when you enter the basic information for your project. This option can be enabled later from the **Project settings** page.
-
-5. Select the container where you uploaded your dataset. 
-
-7. Select **Yes, my files are already labeled and I have formatted JSON labels file** and select the labels file from the drop-down menu to import your JSON labels file. Make sure it follows the [supported format](../../concepts/data-formats.md).
-
-8.   Select **Next**.
-
-9. Review the data you entered and select **Create Project**.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクトインポート手順の削除"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識に関するドキュメントの「プロジェクトインポート」に関するセクションが削除されました。このセクションは、Language Studio内でプロジェクトをインポートするための具体的な手順を詳細に説明していました。削除された内容には、次のようなステップが含まれていました：

1. Language Studioにサインインし、サブスクリプションとLanguageリソースを選択すること。
2. 「情報を抽出」セクションから「カスタムネーミングエンティティ認識」を選択すること。
3. プロジェクトページのトップメニューから「新しいプロジェクトを作成」を選択し、データにタグ付け、モデルのトレーニング、評価、改善、デプロイを行うこと。
4. ストレージアカウントに接続する画面が表示され、その接続手順を行うこと（このプロセスは不可逆であり、注意が必要）。
5. プロジェクト情報（名前、説明、ファイルの言語など）を入力し、必要に応じてマルチリンガルデータセットを有効にすること。
6. アップロードしたデータセットのコンテナを選択し、JSONラベルファイルをインポートすること。
7. データの確認後、「プロジェクトを作成」を選択すること。

この手順の削除により、ユーザーはプロジェクトをインポートする方法についての指示を失い、特に初心者にとっては大きな混乱を引き起こす可能性があります。データセットの取扱いやストレージアカウントの接続に関する重要な情報も失われ、今後どのようにプロジェクトを作成する合ったのかを理解することが難しくなります。この変更は、ユーザー体験を大きく損なう要因となるため、代替のガイダンスを提供することが望まれます。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/language-studio/model-evaluation.md{#item-cbdc16}

<details>
<summary>Diff</summary>
````diff
@@ -1,82 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Go to your project page in [Language Studio](https://aka.ms/languageStudio).
-
-2. Select **Model performance** from the menu on the left side of the screen.
-
-3. On this page, you can only view the successfully trained models, F1 score for each model and [model expiration date](../../../concepts/model-lifecycle.md). You can select the model name for more details about its performance.
-
-> [!NOTE]
-> Entities that aren't labeled or predicted in the test set aren't part of the displayed results.
-
-### [Overview](#tab/overview)
-
-* In this tab you can view the model's details such as: F1 score, precision, recall, date, and time for the training job, total training time, and number of training and testing documents included in this training job.
-
-    :::image type="content" source="../../media/overview.png" alt-text="A screenshot that shows the overview page for model evaluation." lightbox="../../media/overview.png":::
-
-* You can also see [guidance](../../concepts/evaluation-metrics.md#guidance) on how to improve the model. When you select *view details*, a side panel opens to give more guidance on how to improve the model. In this example, *BorrowerAddress* and *BorrowerName* entities are confused with *$none* entity. By selecting the confused entities, you're taken to the [data labeling](../../how-to/tag-data.md) page to label more data with the correct entity.
-
-    :::image type="content" source="../../media/overview-guidance.png" alt-text="A screenshot that shows the guidance page for model evaluation." lightbox="../../media/overview-guidance.png":::
-
-    Learn more about model guidance and confusion matrix in [model performance](../../concepts/evaluation-metrics.md) concepts.
-
-### [Entity type performance](#tab/entity-performance)
-
-* This view is a snapshot of how your model performed during testing. The metrics here are static and tied to your model, so they don't update until you train again.
-
-* You can see for each entity, precision, recall, F1 score, number of training and testing labels.
-
-
-    :::image type="content" source="../../media/entity-type-performace.png" alt-text="A screenshot of entity performance." lightbox="../../media/entity-type-performace.png":::
-
-### [Test set details](#tab/test-set)
-
-* Here you can see the documents included in the **test set** and the result entity type for each document. You can use the *Show mismatches only* toggle to show only documents with mismatches, or unselect the toggle to view all document in the test set.
-
-* For each document, you can view: labeled text, its respective labeled entity type and what entity it was predicted with. Also, you can see whether it's a [true positive](../../concepts/evaluation-metrics.md), [false positive](../../concepts/evaluation-metrics.md), or [false negative](../../concepts/evaluation-metrics.md).
-
-    :::image type="content" source="../../media/test-set.png" alt-text="A screenshot of test set details." lightbox="../../media/test-set.png":::
-
-
-### [Dataset distribution](#tab/dataset-distribution)
-
-This snapshot shows how entities are distributed across your training and testing sets. This data is static and tied to your model, so it doesn't update until you train again.
-
-* You can view the dataset distribution in *graph* or *table* view.
-
-**Graph view**
-
-* *Documents with at least one label*: This view shows for each entity, the number of occurrences for this entity across the training and testing sets.
-
-* *Total instances throughout documents*: This view shows for each entity, the labeled occurrences across training and testing sets.
-
-  :::image type="content" source="../../media/dataset-graph.png" alt-text="A screenshot showing distribution in graph view." lightbox="../../media/dataset-graph.png":::
-
-**Table view**
-
-For each *entity*, you can view: tags per entity in training set; tagged documents in training set; tags per entity in testing set; tagged documents in testing set; tags per entity total; and tagged documents total.
-
-  :::image type="content" source="../../media/dataset-table.png" alt-text="A screenshot showing distribution in table view." lightbox="../../media/dataset-table.png":::
-
-### [Confusion matrix](#tab/confusion-matrix)
-
-A [confusion matrix](../../concepts/evaluation-metrics.md#confusion-matrix) is an N x N matrix used for evaluating the performance of a classification model, where N is the number of target entities. The matrix compares the actual target values with those values predicted by the machine learning model to show how well the extraction model is performing and what kinds of errors it's making.
-
-You can view the confusion matrix in *normalized* or *raw count* view.
-
-  :::image type="content" source="../../media/confusion.png" alt-text="A screenshot of a confusion matrix in Language Studio." lightbox="../../media/confusion.png":::
-
-* All values: Shows the confusion matrix for all entities.
-
-* Only errors: Shows the confusion matrix for entities with errors only.
-
-* Only matches: Shows the confusion matrix for entities with correct predictions only.
-
----
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデル評価手順の削除"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識に関するドキュメントの「モデル評価」セクションが削除されました。このセクションは、Language Studio内でモデルのパフォーマンスを評価するための具体的な手順を詳細に説明していました。削除された内容には、次のような情報が含まれていました：

1. プロジェクトページに移動し、「モデルパフォーマンス」を選択する方法。
2. トレーニングに成功したモデルのF1スコアやモデルの有効期限などの情報を確認すること。
3. モデルの詳細（F1スコア、精度、再現率、トレーニング時間、トレーニングおよびテストドキュメントの数など）を表示できる「概要」タブの説明。
4. モデル改善に関するガイダンスを表示する方法、および混同行列の情報。
5. 各エンティティのパフォーマンスを示す「エンティティタイプパフォーマンス」タブがあり、モデルのテスト中のパフォーマンスを確認することができる。
6. テストセット内のドキュメントと結果エンティティタイプを表示する「テストセットの詳細」タブ。
7. データセットの分布を視覚的に表示する「データセット分布」タブ。
8. モデルのパフォーマンスを評価するための混同行列の説明。

この手順の削除により、ユーザーはモデルの評価方法についての指示を失い、特に初心者に成功したトレーニングモデルのパフォーマンスを理解する機会を奪われることになります。この変更は、ユーザーがエンティティ認識モデルを効果的に評価し、改善するために必要な洞察をも欠くことを意味し、全体的なユーザー体験を損なう可能性があります。適切な情報提供によって、ユーザーが直面する可能性のある混乱を最小限に抑えることが重要です。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/language-studio/project-details.md{#item-8fb72c}

<details>
<summary>Diff</summary>
````diff
@@ -1,20 +0,0 @@
----
-titleSuffix: Foundry Tools
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Go to your **project settings** page in [Language Studio](https://aka.ms/languageStudio).
-
-2. You can see project details.
-
-3. On this page, you can update project description and enable/disable Multi-lingual dataset in project settings.
-
-4. You can also view the connected storage account and container to your Language resource.
-
-5. You can also retrieve your primary resource key from this page.
-
-    :::image type="content" source="../../media/project-details.png" alt-text="A screenshot of the project settings page in Language Studio." lightbox="../../media/project-details.png":::
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト詳細手順の削除"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識に関するドキュメントの「プロジェクト詳細」セクションが削除されました。このセクションは、Language Studioのプロジェクト設定ページでプロジェクトの詳細を確認および更新するための手順を説明していました。削除された内容には、次のような重要な手順が含まれていました：

1. Language Studioでプロジェクト設定ページに移動する方法。
2. プロジェクト詳細を確認する方法。
3. プロジェクトの説明を更新し、マルチリンガルデータセットを有効または無効にする方法。
4. Languageリソースに接続されているストレージアカウントとコンテナを表示する方法。
5. プロジェクト詳細ページから主要リソースキーを取得する方法。

この手順の削除により、ユーザーはプロジェクトの設定を管理するための具体的な手順を失い、特にプロジェクトの構成やストレージアカウントについての重要な情報にアクセスできなくなります。この変更は、プロジェクトの設定を確実に行いたいユーザーにとって、大きな混乱を招く可能性があります。特に初心者にとっては、プロジェクトの管理や設定を適切に行うための支援が不足し、全体的な体験を損なう結果となるでしょう。代替のガイダンスを提供することが望まれます。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/language-studio/resource-creation-language-studio.md{#item-50fe52}

<details>
<summary>Diff</summary>
````diff
@@ -1,28 +0,0 @@
----
-titleSuffix: Foundry Tools
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-### Create a new Language resource from Language Studio
-
-If it's your first time logging in, you'll see a window in [Language Studio](https://aka.ms/languageStudio) that lets you choose an existing Language resource or create a new one. You can also create a resource by clicking the settings icon in the top-right corner, selecting **Resources**, then clicking **Create a new resource**.
-
-Create a Language resource with following details.
-
-|Instance detail  |Required value  |
-|---------|---------|
-|Azure subscription| **Your Azure subscription**|
-|Azure resource group| **Your Azure resource group**|
-|Azure resource name| **Your Azure resource name**|
-|Location | The [region](../../service-limits.md#regional-availability) of your Language resource.      |
-|Pricing tier     | The [pricing tier](../../service-limits.md#language-resource-limits) of your Language resource.        |
-
-> [!IMPORTANT]
-> * Make sure to enable **Managed Identity** when you create a Language resource. 
-> * Read and confirm Responsible AI notice
-
-To use custom named entity recognition, you need to [create an Azure storage account](/azure/storage/common/storage-account-create) if you don't have one already. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "リソース作成手順の削除"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識に関するドキュメントの「Language Studioでのリソース作成」セクションが削除されました。このセクションは、Language Studioから新しい言語リソースを作成する際の具体的な手順を説明していました。削除された内容には、以下の重要な情報が含まれていました：

1. Language Studioに初めてログインした際に、既存の言語リソースを選択するか新しいリソースを作成するためのウィンドウが表示されること。
2. 設定アイコンをクリックして「リソース」を選択し、「新しいリソースを作成」をクリックしてリソースを作成する方法。
3. 言語リソースを作成するための必要な詳細情報についての表：
   - Azureサブスクリプション
   - Azureリソースグループ
   - Azureリソース名
   - リソースの場所
   - 料金プラン
4. 言語リソース作成時に「マネージドアイデンティティ」を有効にする重要な注意事項。
5. カスタムネーミングエンティティ認識を使用するためにAzureストレージアカウントを作成する必要があること。

この手順の削除により、新しいユーザーは言語リソースの作成方法に関する指示を失い、特にAzureを初めて使用する際に重要な情報を得ることができなくなります。この変更は、リソースの設定と管理に関してユーザーの混乱を招く可能性が高く、特に初心者にとっては大きなハードルとなります。ユーザーが正しくリソースを作成できるように、代替の情報提供やガイダンスが必要です。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/language-studio/swap-deployment.md{#item-5e9d44}

<details>
<summary>Diff</summary>
````diff
@@ -1,14 +0,0 @@
----
-titleSuffix: Foundry Tools
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To swap deployments from within [Language Studio](https://aka.ms/laguageStudio):
-
-1. In the **Deploying a model** page, select the two deployments you want to swap and select **Swap deployments** from the top menu. 
-
-2. From the window that appears, select the names of the deployments you want to swap.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "デプロイメントのスワップ手順の削除"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識に関するドキュメントの「Language Studioにおけるデプロイメントのスワップ」セクションが削除されました。このセクションは、Language Studio内でデプロイメントをスワップするための具体的な手順を詳しく説明していました。削除された内容には、以下の重要なポイントが含まれていました：

1. **モデルのデプロイページ**でスワップしたいデプロイメントを選択し、上部メニューから「デプロイメントをスワップ」を選択する手順。
2. 表示されるウィンドウから、スワップしたいデプロイメントの名前を選択する方法。

この手順の削除により、ユーザーはLanguage Studio内でデプロイメントをスワップする操作に関するガイダンスを失い、特にデプロイ作業を行う際に困難を感じる可能性があります。デプロイメントの管理は、AIモデルの運用において非常に重要であり、この削除は特に初心者や新しいユーザーに不便をもたらすでしょう。ユーザーがスムーズにデプロイメントを管理できるように、代替の情報提供やサポートが必要とされます。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/language-studio/train-model.md{#item-0551aa}

<details>
<summary>Diff</summary>
````diff
@@ -1,28 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To start training your model from within the [Language Studio](https://aka.ms/LanguageStudio):
-
-1. Select **Training jobs** from the left side menu.
-
-2. Select **Start a training job** from the top menu.
-
-3. Select **Train a new model** and type in the model name in the text box. You can also **overwrite an existing model** by selecting this option and choosing the model you want to overwrite from the dropdown menu. Overwriting a trained model is irreversible, but it doesn't affect your deployed models until you deploy the new model.
-
-    :::image type="content" source="../../media/train-model.png" alt-text="Create a new training job" lightbox="../../media/train-model.png":::
-    
-4. Select data splitting method. You can choose **Automatically splitting the testing set from training data** where the system splits your labeled data between the training and testing sets, according to the specified percentages. Or you can **Use a manual split of training and testing data**, this option is only enabled if you added documents to your testing set during [data labeling](../../how-to/tag-data.md). See [How to train a model](../../how-to/train-model.md#data-splitting) for information about data splitting.
-
-4. Select the **Train** button.
-
-5. If you select the Training Job ID from the list, a side pane appears where you can check the **Training progress**, **Job status**, and other details for this job.
-
-    > [!NOTE]
-    > * Only successfully completed training jobs generate models.
-    > * Training can take some time between a couple of minutes and several hours based on the size of your labeled data.
-    > * You can only have one training job running at a time. You can't start other training job within the same project until the running job is completed.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルトレーニング手順の削除"
}
```

### Explanation
この修正では、カスタムネーミングエンティティ認識に関するドキュメントの「Language Studioにおけるモデルのトレーニング」セクションが削除されました。このセクションは、Language Studio内で新しいモデルをトレーニングするための具体的な手順を詳細に説明していました。削除された内容には以下の重要な手順が含まれていました：

1. **トレーニングジョブ**のメニューから新しいトレーニングジョブを開始する方法。
2. 新しいモデルの名前を入力し、既存のモデルを上書きするオプションについての説明。このオプションを選択すると、上書きされるモデルをドロップダウンメニューから選ぶことができる。
3. データ分割方法の選択肢に関する情報。このセクションでは、自動でデータを分割するオプションや手動分割の選択肢が提示されていました。
4. トレーニングプロセスの進捗状況を確認するためのサイドペインの使用方法。
5. トレーニングジョブ及びその成功条件についての注意事項。

このセクションが削除された結果、ユーザーはLanguage Studio内でのモデルトレーニングに関する重要なガイダンスを失い、特に新しいAIモデルを構築したいユーザーにとっては大きな不便が生じます。モデルトレーニングはAI開発の重要なフェーズであり、この削除は特に初心者ユーザーに影響を及ぼす可能性があります。適切なトレーニング手順を知るための代替案やサポートが必要となるでしょう。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/rest-api/load-export-model.md{#item-97a5ef}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,81 @@
+---
+author: laujan
+manager: nitinme
+ms.service: azure-ai-language
+ms.topic: include
+ms.date: 11/18/2025
+ms.author: lajanuar
+
+---
+### Load model data 
+
+Create a **POST** request using the following URL, headers, and JSON body to load your model data to your project.
+
+### Request URL
+
+Use the following URL when creating your API request. Replace the placeholder values with your own values. 
+
+```rest
+{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/models/{MODEL-NAME}:load-snapshot?stringIndexType=Utf16CodeUnit&api-version={API-VERSION}
+```
+
+|Placeholder  |Value  | Example |
+|---------|---------|---------|
+|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
+|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `EmailApp` |
+|`{API-VERSION}`     | The version of the API you're calling. | `2022-10-01-preview` |
+|`{MODEL-NAME}`       | The name of your model. This value is case-sensitive. | `v1` |
+
+### Headers
+
+Use the following header to authenticate your request. 
+
+|Key|Value|
+|--|--|
+|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
+
+
+Once you send your API request, you receive a `202` response indicating success. In the response headers, extract the `operation-location` value formatted like this: 
+
+```rest
+{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/models/{MODEL-NAME}/jobs/{JOB-ID}?api-version={API-VERSION}
+``` 
+
+`JOB-ID` is used to identify your request, since this operation is asynchronous. Use this URL to get the status of your model data loading, using the same authentication method.
+
+
+### Export model data
+
+Create a **POST** request using the following URL, headers, and JSON body to export your model data.
+
+### Request URL
+
+Use the following URL when creating your API request. Replace the placeholder values with your own values. 
+
+```rest
+{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/:export?stringIndexType=Utf16CodeUnit&api-version={API-VERSION}&trainedModelLabel={MODEL-NAME}
+```
+
+|Placeholder  |Value  | Example |
+|---------|---------|---------|
+|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
+|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `EmailApp` |
+|`{API-VERSION}`     | The version of the API you're calling. | `2022-10-01-preview` |
+|`{MODEL-NAME}`       | The name of your model. This value is case-sensitive. | `v1` |
+
+### Headers
+
+Use the following header to authenticate your request. 
+
+|Key|Value|
+|--|--|
+|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
+
+
+Once you send your API request, you receive a `202` response indicating success. In the response headers, extract the `operation-location` value formatted like this: 
+
+```rest
+{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/jobs/{JOB-ID}?api-version={API-VERSION}
+``` 
+
+`JOB-ID` is used to identify your request, since this operation is asynchronous. Use this URL to get the exported project JSON, using the same authentication method.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "モデルデータのロードとエクスポートの手順追加"
}
```

### Explanation
この修正では、新しいセクションとして「モデルデータのロードとエクスポート」が追加されました。このセクションは、APIを使用してAIモデルデータをプロジェクトにロードおよびエクスポートする手順を提供します。

**モデルデータをロードする手順**:
- **POSTリクエスト**を作成するための具体的なURL、ヘッダー、JSONボディの構成が記載されています。この手順に従って、モデルデータを指定されたプロジェクトにロードします。
- リクエストURLは、エンドポイントやプロジェクト名、モデル名、APIバージョンのプレースホルダーを用いて提供され、実際の値で置き換える必要があります。
- リクエストに必要なヘッダー情報が含まれており、特にAPIリクエストを認証するためのサブスクリプションキーが指定されています。
- APIリクエストを送信した後、成功を示す`202`レスポンスが返され、レスポンスヘッダーから`operation-location`値を抽出する方法が説明されています。この値は非同期操作のリクエストを識別するために使用され、モデルデータロードのステータスを確認するために利用されます。

**モデルデータをエクスポートする手順**:
- 同様に、モデルデータをエクスポートするためのPOSTリクエストの情報が提供されています。リクエストURL、ヘッダー、JSONボディの構成が詳述されており、特定のプレースホルダーが使用されています。
- エクスポート要求が成功すると、同様に`202`レスポンスが得られ、`operation-location`を使用してエクスポートされたプロジェクトJSONを取得するためのURLが説明されています。

この新機能により、ユーザーはAPIを使用してモデルデータのロードおよびエクスポートをシームレスに行うことができ、AIモデルの運用が一層簡便になります。

## articles/ai-services/language-service/custom-text-classification/concepts/data-formats.md{#item-1e7da5}

<details>
<summary>Diff</summary>
````diff
@@ -6,18 +6,18 @@ description: Learn about the data formats accepted by custom text classification
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
-ms.date: 11/18/2025
+ms.topic: concept-article
+ms.date: 12/15/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification
 ---
 # Accepted data formats
 
-If you're trying to import your data into custom text classification, it has to follow a specific format. If you don't have data to import, you can [create your project](../how-to/create-project.md) and use Language Studio to [label your documents](../how-to/tag-data.md).
+If you're trying to import your data into custom text classification, it has to follow a specific format. If you don't have data to import, you can [create your project](../how-to/create-project.md) and use Microsoft Foundry to [label your documents](../how-to/tag-data.md).
 
 ## Labels file format
 
-Your Labels file should be in the `json` format to enable you to [import](../how-to/create-project.md#import-a-custom-text-classification-project) your labels into a project.
+Your Labels file should be in the `json` format to enable you to [import](../how-to/create-project.md#import-a-custom-text-classification-project-rest-api) your labels into a project.
 
 # [Multi label classification](#tab/multi-classification)
 
@@ -135,5 +135,5 @@ Your Labels file should be in the `json` format to enable you to [import](../how
 
 ## Next steps
 
-* You can import your labeled data into your project directly. See [How to create a project](../how-to/create-project.md#import-a-custom-text-classification-project) to learn more about importing projects.
+* You can import your labeled data into your project directly. See [How to create a project](../how-to/create-project.md#import-a-custom-text-classification-project-rest-api) to learn more about importing projects.
 * See the [how-to article](../how-to/tag-data.md) more information about labeling your data. When you're done labeling your data, you can [train your model](../how-to/train-model.md).  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ形式に関する文書の修正"
}
```

### Explanation
この修正では、「カスタムテキスト分類」に関するデータ形式の文書が更新され、いくつかの文言が変更されました。具体的な変更点は以下の通りです：

1. **メタデータの変更**:
   - `ms.topic`の値が「conceptual」から「concept-article」に変更されました。
   - `ms.date`も更新され、作成日が「11/18/2025」から「12/15/2025」に変更されました。

2. **文中の表現の変更**:
   - 「Language Studio」を「Microsoft Foundry」に置き換えることで、ユーザーがドキュメントにデータをラベル付けする際に使用するツールの名称が最新情報に更新されました。
   - リンクの文言も一部変更され、「import」する際の手順を紹介するリンクの説明が具体的なREST APIの内容に更新されました。

3. **関連リンクの更新**:
   - 複数箇所で、「プロジェクトをインポート」するためのリンクが従来の内容からREST APIに基づいた情報へと変更されました。

これらの変更により、文書は最新の情報を反映し、ユーザーがカスタムテキスト分類に関するデータを効果的に取り扱うための情報がより正確になりました。また、具体的な手順や使用するツールに関する情報が改善され、ユーザビリティが向上しています。

## articles/ai-services/language-service/custom-text-classification/concepts/evaluation-metrics.md{#item-3803bc}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ description: Learn about evaluation metrics in custom text classification.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification
@@ -151,5 +151,4 @@ Similarly,
 
 ## Next steps
 
-* [View a model's performance in Language Studio](../how-to/view-model-evaluation.md)
 * [Train a model](../how-to/train-model.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価指標に関する文書の修正"
}
```

### Explanation
この修正では、「カスタムテキスト分類」における評価指標に関する文書が更新され、一部の文言が変更されました。主な変更点は以下の通りです：

1. **メタデータの変更**:
   - `ms.topic`の値が「conceptual」から「concept-article」に変更され、文書のカテゴリが明確に示されるようになりました。

2. **文中の表現の変更**:
   - 文書内で次のステップを示す部分において、「Language Studioでモデルのパフォーマンスを表示する」というリンクがこの変更に伴い削除されました。これは，現在の文書構造において統一性を持たせるための修正と見られます。

これにより、文書はより一貫性のある情報を提供し、読者にとっての明瞭さが向上されています。データサイエンスや機械学習のプロジェクトにおいて評価指標を理解するための重要な情報が引き続き保証されています。

## articles/ai-services/language-service/custom-text-classification/fail-over.md{#item-3ec67b}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/18/2025
+ms.date: 12/15/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フェイルオーバーに関する文書の日付更新"
}
```

### Explanation
この変更では、「カスタムテキスト分類」におけるフェイルオーバーに関する文書のメタデータが更新されました。具体的には、文書の日付が以下のように変更されています：

- `ms.date`の値が「11/18/2025」から「12/15/2025」に変更され、更新された日付を反映しています。

この修正によって、文書は最新の情報を提供し、ユーザーに対して正確な日時を示すことができます。これにより、読者は文書がいつ更新されたのかを理解しやすくなり、情報の鮮度に対する信頼性が向上します。

## articles/ai-services/language-service/custom-text-classification/faq.md{#item-038891}

<details>
<summary>Diff</summary>
````diff
@@ -43,7 +43,7 @@ When you're ready to start [using your model to make predictions](#how-do-i-use-
 
 ## What is the recommended CI/CD process?
 
-You can train multiple models on the same dataset within the same project. After you train your model successfully, you can [view its evaluation](how-to/view-model-evaluation.md). You can [deploy and test](quickstart.md#deploy-your-model) your model within [Language studio](https://aka.ms/languageStudio). You can add or remove tags from your data and train a **new** model and test it as well. View [service limits](service-limits.md)to learn about maximum number of trained models with the same project. When you [tag your data](how-to/tag-data.md#label-your-data), you can determine how your dataset is split into training and testing sets.
+You can train multiple models on the same dataset within the same project. After you train your model successfully, you can [view its evaluation](how-to/view-model-evaluation.md). You can [deploy and test](quickstart.md#deploy-your-model) your model within [Microsoft Foundry](https://ai.azure.com/). You can add or remove tags from your data and train a **new** model and test it as well. View [service limits](service-limits.md)to learn about maximum number of trained models with the same project. When you [tag your data](how-to/tag-data.md#label-your-data), you can determine how your dataset is split into training and testing sets.
 
 ## Does a low or high model score guarantee bad or good performance in production?
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQ文書内のサービス名の更新"
}
```

### Explanation
この修正では、「カスタムテキスト分類」に関連するFAQ文書が更新され、特定のサービス名が変更されました。主な変更点は以下の通りです：

- 文中の「Language studio」という表現が「Microsoft Foundry」に変更され、これにより、使用するプラットフォーム名が最新のものに更新されました。

この修正により、読者は現在のプラットフォームに関する正確な情報を得ることができ、関連する手続きを正しく理解するのに役立ちます。適切なサービス名の使用は、ドキュメントの精度と信頼性を向上させる重要な要素です。

## articles/ai-services/language-service/custom-text-classification/glossary.md{#item-ed0857}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ description: Learn about definitions used in custom text classification.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: glossary
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語集のトピックタイプの更新"
}
```

### Explanation
この変更では、「カスタムテキスト分類」に関する用語集ドキュメントのメタデータが更新されました。具体的には、`ms.topic`の値が「conceptual」から「glossary」に変更されました。この修正により、ドキュメントが「用語集」としての性質を明確に示すようになります。

この更新は、読み手に対して文書の目的や内容を正確に伝え、用語の定義や説明を探しているユーザーが必要な情報を容易に見つける手助けとなります。また、適切なトピックタイプの指定は、コンテンツの整理や検索の効率を向上させる重要な要素です。

## articles/ai-services/language-service/custom-text-classification/how-to/call-api.md{#item-30dce9}

<details>
<summary>Diff</summary>
````diff
@@ -16,81 +16,60 @@ ms.custom: language-service-clu
 # Send text classification requests to your model
 
 After you successfully deploy a model, you can query the deployment to classify text based on the model you assigned to the deployment.
-You can query the deployment programmatically [Prediction API](/rest/api/language/analyze-text/analyze-text/analyze-text?view=rest-language-analyze-text-2025-11-01&tabs=HTTP&preserve-view=true) or through the client libraries (Azure SDK). 
+You can query the deployment programmatically [Prediction API](/rest/api/language/analyze-text/analyze-text/analyze-text?view=rest-language-analyze-text-2025-11-01&tabs=HTTP&preserve-view=true) or through the client libraries (Azure SDK).
 
-## Test deployed model
-
-You can use Language Studio to submit the custom text classification task and visualize the results. 
-
-[!INCLUDE [Test model](../../includes/custom/language-studio/test-model.md)]
-
-
-:::image type="content" source="../media/test-model-results.png" alt-text="A screenshot showing model test results for a single label classification project." lightbox="../media/test-model-results.png":::
-
-
-## Send a text classification request to your model
-
-> [!TIP]
-> You can [test your model in Language Studio](../quickstart.md?pivots=language-studio#test-your-model) by sending sample text to classify it.
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Get prediction URL](../../includes/custom/language-studio/get-prediction-url.md)]
-
-
-# [REST API](#tab/rest-api)
+## Send a text classification request to your model (REST API)
 
 First you need to get your resource key and endpoint:
 
 [!INCLUDE [Get keys and endpoint Azure portal](../../includes/key-endpoint-page-azure-portal.md)]
 
-
-
 ### Submit a custom text classification task
 
 [!INCLUDE [submit a text classification task using the REST API](../includes/rest-api/submit-task.md)]
 
 
-### Get task results
+### Get task results (Azure SDK)
 
 [!INCLUDE [get custom NER task results](../includes/rest-api/get-results.md)]
 
-# [Client libraries (Azure SDK)](#tab/client-libraries)
 
 First you need to get your resource key and endpoint:
 
+
+
 [!INCLUDE [Get keys and endpoint Azure portal](../includes/get-keys-endpoint-azure.md)]
 
-3. Download and install the client library package for your language of choice:
-    
+1. Download and install the client library package for your language of choice:
+
     |Language  |Package version  |
     |---------|---------|
     |.NET     | [5.2.0-beta.3](https://www.nuget.org/packages/Azure.AI.TextAnalytics/5.2.0-beta.3)        |
     |Java     | [5.2.0-beta.3](https://mvnrepository.com/artifact/com.azure/azure-ai-textanalytics/5.2.0-beta.3)        |
     |JavaScript     |  [6.0.0-beta.1](https://www.npmjs.com/package/@azure/ai-text-analytics/v/6.0.0-beta.1)       |
     |Python     | [5.2.0b4](https://pypi.org/project/azure-ai-textanalytics/5.2.0b4/)         |
-    
-4. After you install the client library, use the following samples on GitHub to start calling the API.
-    
+
+1. After you install the client library, use the following samples on GitHub to start calling the API.
+
     Single label classification:
     * [C#](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/textanalytics/Azure.AI.TextAnalytics/samples/Sample9_SingleLabelClassify.md)
     * [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/textanalytics/azure-ai-textanalytics/src/samples/java/com/azure/ai/textanalytics/lro/SingleLabelClassifyDocument.java)
     * [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/%40azure/ai-text-analytics_6.0.0-beta.1/sdk/textanalytics/ai-text-analytics/samples/v5/javascript/customText.js)
     * [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/textanalytics/azure-ai-textanalytics/samples/sample_single_label_classify.py)
-    
+
     Multi label classification:
     * [C#](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/textanalytics/Azure.AI.TextAnalytics/samples/Sample10_MultiLabelClassify.md)
     * [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/textanalytics/azure-ai-textanalytics/src/samples/java/com/azure/ai/textanalytics/lro/MultiLabelClassifyDocument.java)
     * [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/%40azure/ai-text-analytics_6.0.0-beta.1/sdk/textanalytics/ai-text-analytics/samples/v5/javascript/customText.js)
     * [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/textanalytics/azure-ai-textanalytics/samples/sample_multi_label_classify.py)
 
-5. See the following reference documentation on the client, and return object:
-    
+1. See the following reference documentation on the client, and return object:
+
     * [C#](/dotnet/api/azure.ai.textanalytics?view=azure-dotnet-preview&preserve-view=true)
     * [Java](/java/api/overview/azure/ai-textanalytics-readme?view=azure-java-preview&preserve-view=true)
     * [JavaScript](/javascript/api/overview/azure/ai-text-analytics-readme?view=azure-node-preview&preserve-view=true)
     * [Python](/python/api/azure-ai-textanalytics/azure.ai.textanalytics?view=azure-python-preview&preserve-view=true)
----
+
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "API呼び出し方法に関する文書の更新"
}
```

### Explanation
この変更では、カスタムテキスト分類に関するAPI呼び出しの手順を説明する文書が更新されました。以下の主要な変更点があります：

- 既存のセクションが整理され、余分なテキストが削除され、より簡潔に必要な情報が提供されるようになりました。特に、「Language Studio」を使ってモデルをテストする方法の説明が削除され、APIによる呼び出しに関する内容が強調されました。
- 文書内での「REST API」セクションが新設され、リソースキーとエンドポイントの取得方法についての指示が明確化されました。
- API呼び出しのサンプルコードや関連リンクの構造も整理され、読みやすさが向上し、ユーザーが異なるプログラミング言語でサンプルをすぐに見つけられるようになりました。

この修正により、ユーザーはAPIを通じたカスタムテキスト分類モデルの呼び出しに関する情報に簡単にアクセスでき、実装を迅速に行いやすくなります。

## articles/ai-services/language-service/custom-text-classification/how-to/create-project.md{#item-648436}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/18/2025
+ms.date: 12/18/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification, references_regions
 ---
@@ -41,10 +41,6 @@ You also need an Azure storage account where to upload your `.txt` documents tha
 
 [!INCLUDE [create a new resource from the Azure portal](../includes/resource-creation-azure-portal.md)]
 
-### [Using Language Studio](#tab/language-studio)
-
-[!INCLUDE [create a new resource from Language Studio](../includes/language-studio/resource-creation-language-studio.md)]
-
 ### [Using Azure PowerShell](#tab/azure-powershell)
 
 [!INCLUDE [create a new resource with Azure PowerShell](../includes/resource-creation-powershell.md)]
@@ -60,58 +56,29 @@ You also need an Azure storage account where to upload your `.txt` documents tha
 [!INCLUDE [use an existing resource](../includes/use-pre-existing-resource.md)]
 
 
-## Create a custom text classification project
-
-Once your resource and storage container are configured, create a new custom text classification project. A project is a work area for building your custom AI models based on your data. Your project is only accessible by you and others who have access to the Azure resource being used. If you labeled data, you can [import it](#import-a-custom-text-classification-project) to get started.
-
-### [Language Studio](#tab/studio)
-
-[!INCLUDE [Language Studio project creation](../includes/language-studio/create-project.md)]
+## Create a custom text classification project (REST API)
 
+Once your resource and storage container are configured, create a new custom text classification project. A project is a work area for building your custom AI models based on your data. Your project is only accessible by you and others who have access to the Azure resource being used. If you labeled data, you can [import it](#import-a-custom-text-classification-project-rest-api) to get started.
 
-### [REST APIs](#tab/apis)
 
 [!INCLUDE [REST APIs project creation](../includes/rest-api/create-project.md)]
 
----
 
-## Import a custom text classification project
+## Import a custom text classification project (REST API)
 
 If you already labeled data, you can use it to get started with the service. Make sure that your labeled data follows the [accepted data formats](../concepts/data-formats.md).
 
-### [Language Studio](#tab/studio)
-
-[!INCLUDE [Import project](../includes/language-studio/import-project.md)]
-
-### [REST APIs](#tab/apis)
-
 [!INCLUDE [Import project](../includes/rest-api/import-project.md)]
 
----
-
-## Get project details
-
-### [Language Studio](#tab/studio)
-
-[!INCLUDE [Language Studio project details](../includes/language-studio/project-details.md)]
-
-### [REST APIs](#tab/apis)
+## Get project details (REST API)
 
 [!INCLUDE [REST API project details](../includes/rest-api/project-details.md)]
 
----
+## Delete project (REST API)
 
-## Delete project
-
-### [Language Studio](#tab/studio)
-
-[!INCLUDE [Delete project using Language Studio](../includes/language-studio/delete-project.md)]
-
-### [REST APIs](#tab/apis)
 
 [!INCLUDE [Delete project using the REST API](../includes/rest-api/delete-project.md)]
 
----
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムテキスト分類プロジェクト作成手順の更新"
}
```

### Explanation
この変更では、カスタムテキスト分類プロジェクトの作成手順を説明する文書が更新されました。以下のポイントが主な変更点です：

- `ms.date`の更新が行われ、文書の日付が2025年11月18日から2025年12月18日に変更されました。
- 「Language Studio」を使用したリソース作成に関するセクションが削除され、REST APIを利用してプロジェクトを作成する方法が強調されました。
- 新しいセクションが追加され、REST APIを使用してカスタムテキスト分類プロジェクトを作成、インポート、プロジェクトの詳細を取得、プロジェクトを削除する方法が詳述されました。

これにより、ユーザーはカスタムテキスト分類プロジェクトを設定するための手順をより明確に理解でき、主にREST APIに焦点を当てた情報が提供されるようになりました。この更新は、開発者がプロジェクトを迅速に開始できるようにするための重要な改善となっています。

## articles/ai-services/language-service/custom-text-classification/how-to/deploy-model.md{#item-20d1af}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/18/2025
+ms.date: 12/15/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification
 ---
@@ -24,16 +24,10 @@ Once you're satisfied with how your model performs, it's ready to be deployed; a
 
 See the [project development lifecycle](../overview.md#project-development-lifecycle).
 
-## Deploy model
+## Deploy model (REST API)
 
 After you review your model's performance and decided it can be used in your environment, you need to assign it to a deployment to be able to query it. Assigning the model to a deployment makes it available for use through the [prediction API](https://aka.ms/ct-runtime-swagger). We recommend that you create a deployment named `production` to which you assign the best model you built so far and use it in your system. You can create another deployment called `staging` to which you can assign the model you're currently working on to be able to test it. You can have a maximum on 10 deployments in your project.
 
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Deploy a model using Language Studio](../includes/language-studio/deploy-model.md)]
-
-# [REST APIs](#tab/rest-api)
-
 ### Submit deployment job
 
 [!INCLUDE [deploy model](../includes/rest-api/deploy-model.md)]
@@ -42,63 +36,28 @@ After you review your model's performance and decided it can be used in your env
 
 [!INCLUDE [get deployment status](../includes/rest-api/get-deployment-status.md)]
 
----
-
-## Swap deployments
+## Swap deployments (REST API)
 
 You can swap deployments after testing a model assigned to one deployment, and want to assign it to another. Swapping deployments involves taking the model assigned to the first deployment, and assigning it to the second deployment. Then taking the model assigned to second deployment and assign it to the first deployment. This step could be used to swap your `production` and `staging` deployments when you want to take the model assigned to `staging` and assign it to `production`.
 
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Swap deployments](../includes/language-studio/swap-deployment.md)]
-
-# [REST APIs](#tab/rest-api)
-
 [!INCLUDE [Swap deployments](../includes/rest-api/swap-deployment.md)]
 
----
-
-
-## Delete deployment
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Delete deployment](../includes/language-studio/delete-deployment.md)]
-
-# [REST APIs](#tab/rest-api)
+## Delete deployment (REST API)
 
 [!INCLUDE [Delete deployment](../includes/rest-api/delete-deployment.md)]
 
----
-
-## Assign deployment resources
+## Assign deployment resources (REST API)
 
 You can [deploy your project to multiple regions](../../concepts/custom-features/multi-region-deployment.md) by assigning different Language resources that exist in different regions.
 
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Assign resource](../../conversational-language-understanding/includes/language-studio/assign-resources.md)]
-
-# [REST APIs](#tab/rest-api)
-
 [!INCLUDE [Assign resource](../includes/rest-api/assign-resources.md)]
 
----
-
-## Unassign deployment resources
+## Unassign deployment resources (REST API)
 
 When you unassign or remove a deployment resource from a project, you also delete all the deployments previously deployed to that resource region.
 
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Unassign resource](../../conversational-language-understanding/includes/language-studio/unassign-resources.md)]
-
-# [REST APIs](#tab/rest-api)
-
 [!INCLUDE [Unassign resource](../includes/rest-api/unassign-resources.md)]
 
----
-
 ## Next steps
 
 * Use [prediction API to query your model](call-api.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル展開手順の更新"
}
```

### Explanation
この変更では、カスタムテキスト分類モデルの展開手順に関する文書が更新されました。主な変更点は以下の通りです：

- `ms.date`が2025年11月18日から2025年12月15日に更新され、最新の情報を反映させました。
- 「モデルを展開」セクションのタイトルが「Deploy model」から「Deploy model (REST API)」に変更され、REST APIを利用した方法に重点が置かれました。
- 言語スタジオでモデルを展開する手順が削除され、逆にREST API経由での展開やスワップの手法が強調されるように整理されました。
- 新しいセクションとして、REST APIを使用したデプロイメントリソースの割り当てや解除の手順が追加され、これによりユーザーはAPIを使用した管理が簡単に行えるようになりました。

この更新により、ユーザーがモデルを効率的に展開および管理するための手順が明確に示され、主にREST APIを活用した方法に焦点が当てられるようになっています。

## articles/ai-services/language-service/custom-text-classification/how-to/design-schema.md{#item-991baa}

<details>
<summary>Diff</summary>
````diff
@@ -13,15 +13,15 @@ ms.custom: language-service-custom-classification
 ---
 # How to prepare data and define a text classification schema
 
-In order to create a custom text classification model, you will need quality data to train it. This article covers how you should select and prepare your data, along with defining a schema. Defining the schema is the first step in [project development lifecycle](../overview.md#project-development-lifecycle), and it defines the classes that you need your model to classify your text into at runtime.
+In order to create a custom text classification model, you need quality data to train it. This article covers how you should select and prepare your data, along with defining a schema. Defining the schema is the first step in [project development lifecycle](../overview.md#project-development-lifecycle), and it defines the classes that you need your model to classify your text into at runtime.
 
 ## Schema design
 
 The schema defines the classes that you need your model to classify your text into at runtime.
 
 * **Review and identify**: Review documents in your dataset to be familiar with their structure and content, then identify how you want to classify your data. 
 
-    For example, if you're classifying support tickets, you might need the following classes: *login issue*, *hardware issue*, *connectivity issue*, and *new equipment request*.
+    For example, if you're classifying support tickets, you might need the following classes: *Sign in issue*, *hardware issue*, *connectivity issue*, and *new equipment request*.
 
 * **Avoid ambiguity in classes**: Ambiguity arises when the classes you specify share similar meaning to one another. The more ambiguous your schema is, the more labeled data you might need to differentiate between different classes.
 
@@ -34,7 +34,7 @@ The schema defines the classes that you need your model to classify your text in
 
 The quality of data you train your model with affects model performance greatly.
 
-* Use real-life data that reflects your domain's problem space to effectively train your model. You can use synthetic data to accelerate the initial model training process, but it will likely differ from your real-life data and make your model less effective when used.
+* Use real-life data that reflects your domain's problem space to effectively train your model. You can use synthetic data to accelerate the initial model training process, but it likely differs from your real-life data and make your model less effective when used.
 
 * Balance your data distribution as much as possible without deviating far from the distribution in real-life.
 
@@ -54,14 +54,12 @@ As a prerequisite for creating a custom text classification project, your traini
 * [Create and upload documents from Azure](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container)
 * [Create and upload documents using Azure Storage Explorer](/azure/vs-azure-tools-storage-explorer-blobs)
 
-You can only use `.txt`. documents for custom text. If your data is in other format, you can use [CLUtils parse command](https://github.com/microsoft/CognitiveServicesLanguageUtilities/blob/main/CustomTextAnalytics.CLUtils/Solution/CogSLanguageUtilities.ViewLayer.CliCommands/Commands/ParseCommand/README.md) to change your file format.
-
- You can upload an annotated dataset, or you can upload an unannotated one and [label your data](../how-to/tag-data.md) in Language studio. 
+You can only use `.txt` documents for custom text. If your data is in other format, you can use [CLUtils parse command](https://github.com/microsoft/CognitiveServicesLanguageUtilities/blob/main/CustomTextAnalytics.CLUtils/Solution/CogSLanguageUtilities.ViewLayer.CliCommands/Commands/ParseCommand/README.md) to change your file format.
 
 ## Test set
 
-When defining the testing set, make sure to include example documents that are not present in the training set. Defining the testing set is an important step to calculate the [model performance](view-model-evaluation.md#model-details). Also, make sure that the testing set include documents that represent all classes used in your project.
+When defining the testing set, make sure to include example documents that aren't present in the training set. Defining the testing set is an important step to calculate the [model performance](view-model-evaluation.md#model-details-rest-api). Also, make sure that the testing set includes documents that represent all classes used in your project.
 
 ## Next steps
 
-If you haven't already, create a custom text classification project. If it's your first time using custom text classification, consider following the [quickstart](../quickstart.md) to create an example project. You can also see the [project requirements](../how-to/create-project.md) for more details on what you need to create a project.
+If you haven't already, create a custom text classification project. If it's your first time using custom text classification, consider following the [quickstart](../quickstart.md) to create an example project. For more information, *see* [project requirements](../how-to/create-project.md).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト分類スキーマ設計手順の更新"
}
```

### Explanation
この変更では、カスタムテキスト分類モデルのスキーマ設計に関する文書が更新されました。主な変更点は以下の通りです：

- `ms.date`が更新され、最新の日付が反映されました。
- スキーマ設計の説明がわかりやすく整理され、特にクラス名の例が「login issue」から「Sign in issue」に変更されるなど、表現の一貫性が保たれました。
- リアルデータに基づくモデルのトレーニングに関する部分が微修正され、テキストの流れが改善されました。
- テストセットの定義に関する説明が明確化され、「in」で表現されていた部分が「aren't」に変更されることで文法的な正確さが向上しました。

これらの更新により、ユーザーはスキーマ設計やデータ準備に関するガイダンスをより理解しやすくなり、カスタムテキスト分類プロジェクトを作成する際の手順が洗練されました。

## articles/ai-services/language-service/custom-text-classification/how-to/tag-data.md{#item-e70f6f}

<details>
<summary>Diff</summary>
````diff
@@ -7,15 +7,15 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/18/2025
+ms.date: 12/15/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification
 ---
 # Label text data for training your model 
 
 Before training your model, you need to label your documents with the classes you want to categorize them into. Data labeling  is a crucial step in development lifecycle; in this step you can create the classes you want to categorize your data into and label your documents with these classes. This data is used in the next step when training your model so that your model can learn from the labeled data. If you already labeled your data, you can directly [import](create-project.md) it into your project but you need to make sure that your data follows the [accepted data format](../concepts/data-formats.md).
 
-Before creating a custom text classification model, you need to have labeled data first. If your data isn't labeled already, you can label it in the [Language Studio](https://aka.ms/languageStudio). Labeled data informs the model how to interpret text, and is used for training and evaluation.
+Before creating a custom text classification model, you need to have labeled data first. If your data isn't labeled already, you can label it in the [Microsoft Foundry](https://ai.azure.com/). Labeled data informs the model how to interpret text, and is used for training and evaluation.
 
 ## Prerequisites
 
@@ -28,7 +28,7 @@ See the [project development lifecycle](../overview.md#project-development-lifec
 
 ## Data labeling guidelines
 
-After [preparing your data, designing your schema](design-schema.md) and [creating your project](create-project.md), you need to label your data. Labeling your data is important so your model knows which documents will be associated with the classes you need. When you label your data in [Language Studio](https://aka.ms/languageStudio) (or import labeled data), these labels are stored in the JSON file in your storage container that you've connected to this project. 
+After [preparing your data, designing your schema](design-schema.md) and [creating your project](create-project.md), you need to label your data. Labeling your data is important so your model knows which documents will be associated with the classes you need. When you label your data or import labeled data, these labels are stored in the JSON file in your storage container that you've connected to this project. 
 
 As you label your data, keep in mind:
 
@@ -40,7 +40,7 @@ As you label your data, keep in mind:
 
 Use the following steps to label your data:
 
-1. Go to your project page in [Language Studio](https://aka.ms/languageStudio).
+1. Go to your project page in [Microsoft Foundry](https://ai.azure.com/).
 
 2. From the left side menu, select **Data labeling**. You can find a list of all documents in your storage container. See the image below.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データタグ付け手順に関する更新"
}
```

### Explanation
この変更では、カスタムテキスト分類モデル用のデータタグ付けに関する文書が更新されました。主な変更点は以下の通りです：

- `ms.date`が2025年11月18日から2025年12月15日に変更され、最新の日付が反映されました。
- ラベルデータを作成するためのツールが「Language Studio」から「Microsoft Foundry」に変更され、最新のプラットフォームが明示されました。この変更は、ユーザーがデータのラベル付けを行う際のリソースの正確性を高めます。
- データにラベルを付けるプロセスに関する一部の文が簡略化され、具体的な手順がまとめられました。
- データのラベル付けに関するガイドラインの説明が明確化され、ラベルがJSONファイルに保存される旨がより具体的に記述されました。

これらの更新により、ユーザーはカスタムテキスト分類モデルを作成するためのデータラベリングプロセスをより理解しやすくなり、最新のツールを使用して効率的に作業できるようになります。

## articles/ai-services/language-service/custom-text-classification/how-to/train-model.md{#item-2c59cc}

<details>
<summary>Diff</summary>
````diff
@@ -48,13 +48,8 @@ Custom text classification supports two methods for data splitting:
 
 * **Use a manual split of training and testing data**: This method enables users to define which labeled documents should belong to which set. This step is only enabled if you added documents to your testing set during [data labeling](tag-data.md).
 
-## Train model
+## Train model with REST API
 
-# [Language studio](#tab/Language-studio)
-
-[!INCLUDE [Train model](../includes/language-studio/train-model.md)]
-
-# [REST APIs](#tab/REST-APIs)
 
 ### Start training job
 
@@ -66,19 +61,11 @@ Training could take sometime depending on the size of your training data and com
 
  [!INCLUDE [get training model status](../includes/rest-api/get-training-status.md)]
 
----
-
-### Cancel training job
 
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Cancel training](../includes/language-studio/cancel-training.md)]
-
-# [REST APIs](#tab/rest-api)
+### Cancel training job with REST API
 
 [!INCLUDE [Cancel training](../includes/rest-api/cancel-training.md)]
 
----
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル訓練手順の更新"
}
```

### Explanation
この変更では、カスタムテキスト分類モデルの訓練に関する文書が更新されました。主な変更点は以下の通りです：

- モデル訓練セクションのタイトルが「Train model」から「Train model with REST API」に変更され、REST APIを使用した訓練プロセスに焦点が当てられるようになりました。
- 訓練に関する手順から「Language Studio」に関連する情報が削除され、REST APIに関連する情報が強調されました。これにより、ユーザーがREST APIを利用する際のガイダンスが明確になります。
- 訓練ジョブのキャンセルに関するセクションが「Cancel training job」から「Cancel training job with REST API」に変更され、REST APIを通じたキャンセル方法が主に説明される形になりました。
- 不要な文が削除され、全体として文書が簡潔に整理されました。

この更新により、ユーザーはREST APIを介してモデルを訓練し、ジョブをキャンセルする方法をより明確に理解できるようになります。

## articles/ai-services/language-service/custom-text-classification/how-to/view-model-evaluation.md{#item-6afd37}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/18/2025
+ms.date: 12/15/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification
 ---
@@ -29,13 +29,7 @@ Before viewing model evaluation you need:
 
 See the [project development lifecycle](../overview.md#project-development-lifecycle).
 
-## Model details
-
-### [Language studio](#tab/language-studio)
-
-[!INCLUDE [View model details](../includes/language-studio/model-evaluation.md)]
-
-### [REST APIs](#tab/rest-api)
+## Model details (REST API)
 
 ### Single label classification
 [!INCLUDE [Model evaluation](../includes/rest-api/model-evaluation-single-label.md)]
@@ -44,35 +38,16 @@ See the [project development lifecycle](../overview.md#project-development-lifec
 
 [!INCLUDE [Model evaluation](../includes/rest-api/model-evaluation-multi-label.md)]
 
----
-
-## Load or export model data
-
-### [Language studio](#tab/Language-studio)
-
-[!INCLUDE [Load export model](../../conversational-language-understanding/includes/language-studio/load-export-model.md)]
-
 
-### [REST APIs](#tab/REST-APIs)
+## Load or export model data (REST API)
 
 [!INCLUDE [Load export model](../includes/rest-api/load-export-model.md)]
 
----
-
-## Delete model
-
-### [Language studio](#tab/language-studio)
-
-[!INCLUDE [Delete model](../includes/language-studio/delete-model.md)]
 
-
-### [REST APIs](#tab/rest-api)
+## Delete model (REST API)
 
 [!INCLUDE [Delete model](../includes/rest-api/delete-model.md)]
 
-
----
-
 ## Next steps
 
 As you review your how your model performs, learn about the [evaluation metrics](../concepts/evaluation-metrics.md) that are used. Once you know whether your model performance needs to improve, you can begin improving the model.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル評価ビューに関する更新"
}
```

### Explanation
この変更では、カスタムテキスト分類モデルの評価ビューに関する文書が更新されました。主な変更点は以下の通りです：

- `ms.date`が2025年11月18日から2025年12月15日に変更され、文書の日付が最新のものに更新されました。
- モデルの詳細に関するセクションが「Language Studio」と「REST APIs」からの情報を統合し、単一ラベルと多ラベル分類に関するREST APIの使用に重点を置いた新しいタイトル「Model details (REST API)」を持つセクションに変更されました。
- 「Load or export model data」および「Delete model」に関するセクションもそれぞれ「Load or export model data (REST API)」、「Delete model (REST API)」とタイトルが変更され、REST APIを通じた操作に注目が置かれるようになりました。
- 不要な文が削除されて全体がシンプルになり、重要な情報が際立つように整理されました。

これらの更新により、ユーザーはREST APIを使用してモデル評価やデータの読み込み・エクスポート、削除を行うプロセスをより明確に理解できるようになります。

## articles/ai-services/language-service/custom-text-classification/includes/quickstarts/blob-storage-upload.md{#item-72f02e}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ After you create an Azure storage account and connected it to your Language reso
 
 1. [Download the sample dataset for multi label classification projects](https://github.com/Azure-Samples/cognitive-services-sample-data-files/raw/master/language-service/Custom%20text%20classification/Custom%20multi%20classification%20-%20movies%20summary.zip).
 
-2. Open the .zip file, and extract the folder containing the documents. 
+1. Open the .zip file, and extract the folder containing the documents. 
 
 The provided sample dataset contains about 200 documents,  each of which is a summary for a movie. Each document belongs to one or more of the following classes: 
 * "Mystery"
@@ -26,7 +26,7 @@ The provided sample dataset contains about 200 documents,  each of which is a su
 
 1. [Download the sample dataset for single label classification projects](https://github.com/Azure-Samples/cognitive-services-sample-data-files/raw/master/language-service/Custom%20text%20classification/Custom%20single%20classification%20-%20WebOfScience.zip). 
 
-2. Open the .zip file, and extract the folder containing the documents. 
+1. Open the .zip file, and extract the folder containing the documents. 
 
 The provided sample dataset contains about 210 documents, each of which is an abstract of a scientific paper. Each document is labeled with only one class of the following classes: 
 * "Computer_science"
@@ -39,14 +39,16 @@ The provided sample dataset contains about 210 documents, each of which is an ab
 
 ---
 
-2. In the [Azure portal](https://portal.azure.com), navigate to the storage account you created, and select it by selecting **Storage accounts** and typing your storage account name into **Filter for any field**.
+### Azure portal
+
+1. In the [Azure portal](https://portal.azure.com), navigate to the storage account you created, and select it by selecting **Storage accounts** and typing your storage account name into **Filter for any field**.
 
     if your resource group doesn't show up, make sure the **Subscription equals** filter is set to **All**.
 
-3. In your storage account, select **Containers** from the left menu, located below **Data storage**. On the screen that appears, select **+ Container**. Give the container the name **example-data** and leave the default **Public access level**.
+1. In your storage account, select **Containers** from the left menu, located below **Data storage**. On the screen that appears, select **+ Container**. Give the container the name **example-data** and leave the default **Public access level**.
 
     :::image type="content" source="../../media/storage-screen.png" alt-text="A screenshot showing the main page for a storage account." lightbox="../../media/storage-screen.png":::
 
-4. After your container is created, select it. Then select **Upload** button to select the `.txt` and `.json` files you downloaded earlier. 
+1. After your container is created, select it. Then select **Upload** button to select the `.txt` and `.json` files you downloaded earlier. 
 
     :::image type="content" source="../../media/file-upload-screen.png" alt-text="A screenshot showing the button for uploading files to the storage account." lightbox="../../media/file-upload-screen.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blobストレージへのアップロード手順の更新"
}
```

### Explanation
この変更では、カスタムテキスト分類モデルのためのBlobストレージへのファイルアップロード手順が更新されました。主な変更点は以下の通りです：

- 手順の番号が整理され、特にサンプルデータセットのダウンロードや解凍に関する指示が「1.」から始まるように改訂されました。これにより、ユーザーは手順の流れをより簡単に追跡できるようになっています。
- Azureポータルにログインして作成したストレージアカウントにアクセスする手順が「### Azure portal」という新しい見出しの下に整理され、より明確に手順が構成されています。
- 各手順の説明が明確にされたため、ユーザーが特定のアクション（例えば、コンテナーの作成やファイルのアップロード）を実行する際の理解が深まりました。
- 不必要な説明が削除され、全体的に文書が簡潔で関連性の高い内容になっています。

これらの更新により、Blobストレージにデータをアップロードする手順がより直感的に理解できるようになり、ユーザーの利便性が向上します。

## articles/ai-services/language-service/custom-text-classification/includes/quickstarts/rest-api.md{#item-c7e987}

<details>
<summary>Diff</summary>
````diff
@@ -23,26 +23,26 @@ Before you can use custom text classification, you'll need to create a Language
 > If you have a [pre-existing resource](../../how-to/create-project.md#using-a-preexisting-language-resource) that you'd like to use, you need to connect it to storage account.
 
 [!INCLUDE [create a new resource from the Azure portal](../resource-creation-azure-portal.md)]
-    
+
 
 
 ## Upload sample data to blob container
 
 [!INCLUDE [Uploading sample data for custom tex classification](blob-storage-upload.md)]
-    
+
 
 
 ### Get your resource keys and endpoint
 
 [!INCLUDE [Get keys and endpoint Azure portal](../get-keys-endpoint-azure.md)]
-    
+
 
 
 ## Create a custom text classification project
 
 Once your resource and storage container are configured, create a new custom text classification project. A project is a work area for building your custom ML models based on your data. Your project can only be accessed by you and others who have access to Azure Language resource being used.
 
-### Trigger import project job 
+### Trigger import project job
 
 [!INCLUDE [Import a project using the REST API](../rest-api/import-project.md)]
 
@@ -60,7 +60,7 @@ Typically after you create a project, you go ahead and start [tagging the docume
 
 ### Start training your model
 
-After your project has been imported, you can start training your model. 
+After your project has been imported, you can start training your model.
 
 [!INCLUDE [train model](../rest-api/train-model.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIに関する簡潔な指示の整理"
}
```

### Explanation
この変更では、カスタムテキスト分類用REST APIに関連する文書の内容が整理され、明確化されています。主な変更点は以下の通りです：

- 特に "Upload sample data to blob container"、"Get your resource keys and endpoint" などのセクションにおいて、見出しがより読みやすく、整然としたレイアウトに変更されました。
- 不要な空行が削除され、セクション間の整合性が向上しました。これにより、文書全体がすっきりとした印象を与え、読みやすさが向上しています。
- "Trigger import project job"の見出しが微調整され、スムーズなフローを保ちながら、関連するコンテンツへのリンクが一貫して含まれています。
- コンテンツが各手順の実行に有益であることを反映するため、要約の形で情報が提示されています。

これらの更新により、ユーザーはREST APIを使ったカスタムテキスト分類のプロセスを効率的に理解し、実行することができるようになります。

## articles/ai-services/language-service/custom-text-classification/includes/rest-api/load-export-model.md{#item-f1827f}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,11 @@
 ---
-#services: cognitive-services
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: include
 ms.date: 11/18/2025
 ms.author: lajanuar
+
 ---
 ### Load model data 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルデータの読み込みに関するメタデータの修正"
}
```

### Explanation
この変更では、カスタムテキスト分類のモデルデータを読み込む際の文書に関するメタデータが修正されました。以下に主な変更点を示します：

- 文書の冒頭に記載されているメタデータにおいて、1行が追加され、一部が削除されました。この変更により、文書の構造がより明確になると同時に、関連情報の整理が行われました。
- 具体的には、`#services: cognitive-services`の行が削除され、文書の内容には影響を与えないメタ情報が更新されています。
- メタデータの整理によって、この文書がどのサービスに関連しているかの情報が簡潔に表現され、ユーザーが必要な情報に素早くアクセスできるようになります。

これらの更新により、文書の可読性が向上し、ユーザーはモデルデータの読み込み手順に関する情報をより効果的に利用できるようになります。

## articles/ai-services/language-service/custom-text-classification/includes/use-pre-existing-resource.md{#item-7bcdd8}

<details>
<summary>Diff</summary>
````diff
@@ -20,23 +20,11 @@ To use custom text classification, you'll need to [create an Azure storage accou
 
 ## Enable identity management for your resource
 
-# [Azure portal](#tab/azure-portal)
-
 Your Language resource must have identity management, to enable it using [Azure portal](https://portal.azure.com/):
 
 1. Go to your Language resource
-2. From left hand menu, under **Resource Management** section, select **Identity**
-3. From **System assigned** tab, make sure to set **Status** to **On**
-
-# [Language Studio](#tab/language-studio)
-
-Your Language resource must have identity management, to enable it using [Language Studio](https://aka.ms/languageStudio):
-
-1. Select the settings icon in the top right corner of the screen
-2. Select **Resources**
-3. Select the check box **Managed Identity** for your Azure Language in Foundry Tools resource.
-
----
+1. From left hand menu, under **Resource Management** section, select **Identity**
+1. From **System assigned** tab, make sure to set **Status** to **On**
 
 ### Enable custom text classification feature
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースのアイデンティティ管理手順の簡素化"
}
```

### Explanation
この変更では、既存のリソースを使用する際のアイデンティティ管理に関する手順が簡素化されました。主な変更内容は次の通りです：

- 文書内の手順が整理され、一部が削除されて簡潔になりました。特に、AzureポータルとLanguage Studioの両方でリソースのアイデンティティを有効にする方法についての情報が1つの手順に統合され、明確さが向上しました。
- 不要なセクションが削除され、手順の数が削減されたため、ユーザーがリソースのアイデンティティ管理をより簡単に理解できるように配慮されています。
- 新たに追加された手順は必要なアクションを直接示しており、読者が必要な設定を迅速に実行できるようになっています。

これらの更新によって、ユーザーはアイデンティティ管理のプロセスをスムーズに進めることができ、カスタムテキスト分類機能を利用する準備を簡潔に整えることができます。

## articles/ai-services/language-service/custom-text-classification/language-support.md{#item-35327f}

<details>
<summary>Diff</summary>
````diff
@@ -6,8 +6,8 @@ description: Learn about which languages are supported by custom text classifica
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
-ms.date: 11/18/2025
+ms.topic: concept-article
+ms.date: 12/15/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification
 ---
@@ -22,7 +22,7 @@ With custom text classification, you can train a model in one language and use t
 You can train your project entirely with English documents, and query it in: French, German, Mandarin, Japanese, Korean, and others. Custom text classification
 makes it easy for you to scale your projects to multiple languages by using multilingual technology to train your models.
 
-Whenever you identify that a particular language is not performing as well as other languages, you can add more documents for that language in your project. In the [data labeling](how-to/tag-data.md) page in Language Studio, you can select the language of the document you're adding. When you introduce more documents for that language to the model, it is introduced to more of the syntax of that language, and learns to predict it better.
+Whenever you identify that a particular language is not performing as well as other languages, you can add more documents for that language in your project. When you introduce more documents for that language to the model, it is introduced to more of the syntax of that language, and learns to predict it better.
 
 You aren't expected to add the same number of documents for every language. You should build the majority of your project in one language, and only add a few documents in languages you observe aren't performing well. If you create a project that is primarily in English, and start testing it in French, German, and Spanish, you might observe that German doesn't perform as well as the other two languages. In that case, consider adding 5% of your original English documents in German, train a new model and test in German again. You should see better results for German queries. The more labeled documents you add, the more likely the results are going to get better. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サポート情報の更新とメタデータの修正"
}
```

### Explanation
この変更では、カスタムテキスト分類の言語サポートに関する文書が更新され、いくつかのメタデータが修正されました。主な変更内容は以下の通りです：

- メタデータにおける`ms.topic`の値が`concept-article`に変更され、ドキュメントの種類がより具体的に示されるようになりました。また、`ms.date`が`12/15/2025`に更新され、情報の新しさが反映されています。
- 文書内の内容において、特定の言語性能に関する説明が簡潔化されました。具体的には、引用されていたリンクが削除され、説明自体はスムーズに流れるように編集されています。これにより、必要な情報がより明確に伝わるようになりました。
- カスタムテキスト分類のモデルへの文書追加に関するアドバイスが強調され、ユーザーが言語間のパフォーマンスを最適化するためにどのように文書を管理すべきかが具体的に示されています。

これらの更新により、ユーザーはカスタムテキスト分類機能を利用する際の言語サポートに関する理解を深めることができ、より効果的にプロジェクトを管理できるようになります。

## articles/ai-services/language-service/custom-text-classification/overview.md{#item-ebc28d}

<details>
<summary>Diff</summary>
````diff
@@ -7,15 +7,15 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 11/18/2025
+ms.date: 12/15/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification
 ---
 # What is custom text classification?
 
 Custom text classification is one of the custom features offered by [Azure Language in Foundry Tools](../overview.md). It's a cloud-based API service that applies machine-learning intelligence to enable you to build custom models for text classification tasks. 
 
-Custom text classification enables users to build custom AI models to classify text into custom classes predefined by the user. By creating a custom text classification project, developers can iteratively label data, train, evaluate, and improve model performance before making it available for consumption. The quality of the labeled data greatly impacts model performance. To simplify building and customizing your model, the service offers a custom web portal that can be accessed through the [Language studio](https://aka.ms/languageStudio). You can easily get started with the service by following the steps in this [quickstart](quickstart.md). 
+Custom text classification enables users to build custom AI models to classify text into custom classes predefined by the user. By creating a custom text classification project, developers can iteratively label data, train, evaluate, and improve model performance before making it available for consumption. The quality of the labeled data greatly impacts model performance. To simplify building and customizing your model, the service offers a unified platform for building, managing, and deploying AI solutions that can be accessed through the [Microsoft Foundry](https://ai.azure.com/). You can easily get started with the service by following the steps in this [quickstart](quickstart.md). 
 
 Custom text classification supports two types of projects: 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムテキスト分類の説明文の更新"
}
```

### Explanation
この変更では、カスタムテキスト分類に関する文書の一部が更新され、特にサービスの提供方法やプラットフォームが変更されています。主な変更点は以下の通りです：

- メタデータである`ms.date`が`12/15/2025`に更新され、情報の新しさが保証されています。
- カスタムテキスト分類の機能説明の中で、ユーザーが利用できるプラットフォームが`[Language studio](https://aka.ms/languageStudio)`から`[Microsoft Foundry](https://ai.azure.com/)`に変更されました。この変更により、プロジェクトのビルド、管理、およびデプロイに関する一元化されたプラットフォームの重要性が強調されています。
- 説明文の表現が若干調整され、ユーザーがAIソリューションの構築プロセスをより理解しやすくなっています。

これらの変更によって、カスタムテキスト分類の利用者は、最新のプラットフォーム情報を元により効率的にプロジェクトを進めるための手順を理解しやすくなり、サービスを効果的に活用できるようになります。

## articles/ai-services/language-service/custom-text-classification/quickstart.md{#item-29d53a}

<details>
<summary>Diff</summary>
````diff
@@ -7,12 +7,11 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 12/05/2025
+ms.date: 12/15/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification, mode-other
-zone_pivot_groups: usage-custom-language-features
 ---
-# Quickstart: Custom text classification
+# Quickstart: Custom text classification REST API
 
 Use this article to get started with creating a custom text classification project where you can train custom models for text classification. A model is AI software trained to do a certain task. For this system, the models classify text, and are trained by learning from tagged data.
 
@@ -24,18 +23,8 @@ Custom text classification supports two types of projects:
 In this quickstart, you can use the sample datasets provided to build a multi label classification to classify movie scripts into one or more categories. Alternatively, you can use single label classification dataset to classify abstracts of scientific papers into one of the defined domains.
 
 
-::: zone pivot="language-studio"
-
-[!INCLUDE [Language Studio quickstart](includes/quickstarts/language-studio.md)]
-
-::: zone-end
-
-::: zone pivot="rest-api"
-
 [!INCLUDE [REST API quickstart](includes/quickstarts/rest-api.md)]
 
-::: zone-end
-
 ## Next steps
 
 After you create a custom text classification model, you can:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートガイドのタイトルと内容の修正"
}
```

### Explanation
この変更では、カスタムテキスト分類に関するクイックスタートガイドが更新され、特にタイトルと一部の内容が修正されています。主な変更点は以下の通りです：

- `ms.date`が`12/15/2025`に更新され、文書の最新性が保たれています。
- ガイドのタイトルが「Quickstart: Custom text classification」から「Quickstart: Custom text classification REST API」に変更され、REST APIに焦点を当てた内容であることが明示されています。
- プロジェクト作成に関する説明は引き続き提供されていますが、特定の内容が簡素化され、一部のゾーン構造が削除されました。この変更により、情報がよりコンパクトになり、ユーザーが必要な手順に迅速にアクセスできるようになります。

これらの変更によって、運用者はカスタムテキスト分類のREST APIを使用してモデルを構築するための手順を理解しやすくなり、プロジェクトの立ち上げが円滑に進むことが期待されます。

## articles/ai-services/language-service/custom-text-classification/service-limits.md{#item-6df7a9}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: laujan
 manager: nitinme
 ms.date: 11/18/2025
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: limits-and-quotas
 ms.author: lajanuar
 ms.custom: language-service-custom-classification, references_regions
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス制限に関するトピックの更新"
}
```

### Explanation
この変更では、カスタムテキスト分類に関する「サービス制限」文書のトピックが更新されています。具体的には、以下の変更が行われました：

- メタデータ内の`ms.topic`が「conceptual」から「limits-and-quotas」に変更され、文書の焦点がサービスの制限とクォータに関するものだと明確になりました。この変更は、ユーザーが期待する情報により正確にアクセスできるようにするためのものです。
- その他のメタデータや内容は、従来通り保たれています。

これにより、ユーザーはカスタムテキスト分類サービスの制限に関する文書において、より明確に目的や内容を理解でき、必要な情報を迅速に見つけることができるようになります。

## articles/ai-services/language-service/custom-text-classification/tutorials/triage-email.md{#item-47cadc}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: tutorial
-ms.date: 11/18/2025
+ms.date: 12/15/2025
 ms.author: lajanuar
 ---
 # Tutorial: Triage incoming emails with Power Automate
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メールのトリアージに関するチュートリアルの日付更新"
}
```

### Explanation
この変更では、カスタムテキスト分類に関する「メールのトリアージ」チュートリアルが更新されました。主な改訂点は以下の通りです：

- メタデータ内の`ms.date`が`11/18/2025`から`12/15/2025`に変更されています。これにより、チュートリアルの最新性が確保され、ユーザーが提供される情報が新しいものであることが示されます。
- その他のメタデータやチュートリアルの内容は保持されており、ユーザーが必要な情報にアクセスできる形になっています。

この日付の更新により、ユーザーは新しい情報に基づいてチュートリアルを利用でき、より効果的にメールのトリアージを行うための手法を学ぶことができるようになります。

## articles/ai-services/language-service/custom/azure-machine-learning-labeling.md{#item-d2e0c8}

<details>
<summary>Diff</summary>
````diff
@@ -1,130 +0,0 @@
----
-title: Use Azure Machine Learning labeling in Language Studio
-description: Learn how to label your data in Azure Machine Learning, and import it for use in Azure Language service.
-titleSuffix: Foundry Tools
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-# Use Azure Machine Learning labeling in Language Studio
-
-Labeling data is an important part of preparing your dataset. Using the labeling experience in Azure Machine Learning, you can experience easier collaboration, more flexibility, and the ability to [outsource labeling tasks](/azure/machine-learning/how-to-outsource-data-labeling) to external labeling vendors from the [Azure Marketplace](https://azuremarketplace.microsoft.com/marketplace/consulting-services?search=AzureMLVend). You can use Azure Machine Learning labeling for:
-* [custom text classification](../custom-text-classification/overview.md)
-* [custom named entity recognition](../custom-named-entity-recognition/overview.md)
-
-## Prerequisites
-
-Before you can connect your labeling project to Azure Machine Learning, you need:
-* A successfully created Language Studio project with a configured Azure blob storage account.
-* Text data that is uploaded to your storage account.
-* At least:
-    * One entity label for custom named entity recognition, or
-    * Two class labels for custom text classification projects.
-* An [Azure Machine Learning workspace](/azure/machine-learning/how-to-manage-workspace) that is [connected](/azure/machine-learning/v1/how-to-connect-data-ui?tabs=credential#create-datastores) to the same Azure blob storage account that your Language Studio account using.
-
-## Limitations
-
-* Connecting your labeling project to Azure Machine Learning is a one-to-one connection. If you disconnect your project, you can't connect your project back to the same Azure Machine Learning project
-* You can't label in Azure Language Studio and Azure Machine Learning simultaneously. The labeling experience is enabled in one studio at a time.
-* The testing and training files in the labeling experience you switch away from is ignored when training your model.
-* Only Azure Machine Learning's JSONL file format can be imported into Language Studio.
-* Projects with the multi-lingual option enabled can't be connected to Azure Machine Learning, and not all languages are supported.
-    * Language support is provided by the Azure Machine Learning [TextDNNLanguages Class](/python/api/azureml-automl-core/azureml.automl.core.constants.textdnnlanguages?view=azure-ml-py&preserve-view=true&branch=main#azureml-automl-core-constants-textdnnlanguages-supported).
-* The Azure Machine Learning workspace you're connecting to must be assigned to the same Azure Storage account that Language Studio is connected to. Be sure that the Azure Machine Learning workspace has the storage blob data reader permission on the storage account. The workspace needs to link to the storage account during the [creation process in the Azure portal](https://portal.azure.com/#create/Microsoft.MachineLearningServices).
-* Switching between the two labeling experiences isn't instantaneous. It may take time to successfully complete the operation.
-
-## Import your Azure Machine Learning labels into Language Studio
-
-Language Studio supports the JSONL file format used by Azure Machine Learning. If you've been labeling data on Azure Machine Learning, you can import your up-to-date labels in a new custom project to utilize the features of both studios.
-
-1.    Start by creating a new project for custom text classification or custom named entity recognition.
-
-1. In the **Create a project** screen that appears, follow the prompts to connect your storage account, and enter the basic information about your project. Be sure that the Azure resource you're using doesn't have another storage account already connected.
-
-1. In the **Choose container** section, choose the option indicating that you already have a correctly formatted file. Then select your most recent Azure Machine Learning labels file.
-
-    :::image type="content" source="./media/select-label-file.png" alt-text="A screenshot showing the selection for a label file in Language Studio." lightbox="./media/select-label-file.png":::
-
-## Connect to Azure Machine Learning
-
-Before you connect to Azure Machine Learning, you need an Azure Machine Learning account with a pricing plan that can accommodate the compute needs of your project. See the [prerequisites section](#prerequisites) to make sure that you successfully completed all the requirements to start connecting your Language Studio project to Azure Machine Learning.
-
-1. Use the [Azure portal](https://portal.azure.com) to navigate to the Azure Blob Storage account connected to your language resource.
-1. Ensure that the *Storage Blob Data Contributor* role is assigned to your AML workspace within the role assignments for your Azure Blob Storage account.
-1. Navigate to your project in [Language Studio](https://language.azure.com/). From the left pane of your project, select **Data labeling**.
-1. Select **use Azure Machine Learning to label** in either the **Data labeling** description, or under the **Activity pane**.
-
-    :::image type="content" source="./media/azure-machine-learning-selection.png" alt-text="A screenshot showing the location of the Azure Machine Learning link." lightbox="./media/azure-machine-learning-selection.png":::
-
-1. Select **Connect to Azure Machine Learning** to start the connection process.
-
-    :::image type="content" source="./media/activity-pane.png" alt-text="A screenshot showing the Azure Machine Learning connection button in Language Studio." lightbox="./media/activity-pane.png":::
-
-1. In the window that appears, follow the prompts. Select the Azure Machine Learning workspace you created previously under the same Azure subscription. Enter a name for the new Azure Machine Learning project that is created to enable labeling in Azure Machine Learning.
-
-    >[!TIP]
-    > Make sure your workspace is linked to the same Azure Blob Storage account and Language resource before continuing. You can create a new workspace and [link to your storage account using the Azure portal](https://portal.azure.com/#create/Microsoft.MachineLearningServices). Ensure that the storage account is properly linked to the workspace.
-
-1. (Optional) Turn on the vendor labeling toggle to use labeling vendor companies. Before choosing the vendor labeling companies, contact the vendor labeling companies on the [Azure Marketplace](https://azuremarketplace.microsoft.com/marketplace/consulting-services?search=AzureMLVend) to finalize a contract with them. For more information about working with vendor companies, see [How to outsource data labeling](/azure/machine-learning/how-to-outsource-data-labeling).
-
-  * You can also leave labeling instructions for the human labelers that help you in the labeling process.
-  * These instructions can help them understand the task by leaving clear definitions of the labels and including examples for better results.
-
-1. Review the settings for your connection to Azure Machine Learning and make changes if needed.
-
-    > [!IMPORTANT]
-    > Finalizing the connection **is permanent**. Attempting to disconnect your established connection at any point in time can permanently disable your Language Studio project from connecting to the same Azure Machine Learning project.
-
-1. After the connection is initiated, your ability to label data in Language Studio will be disabled for a few minutes to prepare the new connection.
-
-## Switch to labeling with Azure Machine Learning from Language Studio
-
-Once the connection is established, you can switch to Azure Machine Learning through the **Activity pane** in Language Studio at any time.
-
-:::image type="content" source="./media/switch-labeling-activity.png" alt-text="A screenshot showing the button to switch to labeling using Azure Machine Learning." lightbox="./media/switch-labeling-activity.png":::
-
-When you switch, your ability to label data in Language Studio is disabled, and you're able to label data in Azure Machine Learning. You can switch back to labeling in Language Studio at any time through Azure Machine Learning.
-
-For information on how to label the text, see [Azure Machine Learning how to label](/azure/machine-learning/how-to-label-data#label-text). For information about managing and tracking the text labeling project, *see* [Azure Machine Learning set up and manage a text labeling project](/azure/machine-learning/how-to-create-text-labeling-projects).
-
-## Train your model using labels from Azure Machine Learning
-
-When you switch to labeling using Azure Machine Learning, you can still train, evaluate, and deploy your model in Language Studio. To train your model using updated labels from Azure Machine Learning:
-
-1. Select **Training jobs** from the navigation menu on the left of Azure Language studio screen for your project.
-
-1. Select **Import latest labels from Azure Machine Learning** from the **Choose label origin** section in the training page. This step synchronizes the labels from Azure Machine Learning before starting the training job.
-
-    :::image type="content" source="./media/azure-machine-learning-label-origin.png" alt-text="A screenshot showing the selector for using labels from Azure Machine Learning." lightbox="./media/azure-machine-learning-label-origin.png":::
-
-## Switch to labeling with Language Studio from Azure Machine Learning
-
-After you switch to labeling with Azure Machine Learning, You can switch back to labeling with Language Studio project at any time.
-
-> [!NOTE]
-> * Only users with the [correct roles](/azure/machine-learning/how-to-add-users) in Azure Machine Learning have the ability to switch labeling.
-> * When you switch to using Language Studio, labeling on Azure Machine Learning is disabled.
-
-To switch back to labeling with Language Studio:
-
-1. Navigate to your project in Azure Machine Learning and select **Data labeling** from the left pane.
-1. Select the **Language Studio** tab and select **Switch to Language Studio**.
-
-    :::image type="content" source="./media/azure-machine-learning-studio.png" alt-text="A screenshot showing the selector for using labels from Language Studio." lightbox="./media/azure-machine-learning-studio.png":::
-
-3. The process takes a few minutes to complete, and your ability to label in Azure Machine Learning is disabled until switched back from Language Studio.
-
-## Disconnecting from Azure Machine Learning
-
-Disconnecting your project from Azure Machine Learning is a permanent, irreversible process and can't be undone. You can no longer be able to access your labels in Azure Machine Learning, and you won't be able to reconnect the Azure Machine Learning project to any Language Studio project in the future. To disconnect from Azure Machine Learning:
-
-1. Ensure that any updated labels you want to maintain are synchronized with Azure Machine Learning by switching the labeling experience back to Azure Language Studio.
-1. Select **Project settings** from the navigation menu on the left in Language Studio.
-1. Select the **Disconnect from Azure Machine Learning** button from the **Manage Azure Machine Learning connections** section.
-
-## Next steps
-Learn more about labeling your data for [Custom Text Classification](../custom-text-classification/how-to/tag-data.md) and [Custom Named Entity Recognition](../custom-named-entity-recognition/how-to/tag-data.md).
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azure Machine Learningラベリングに関する文書の削除"
}
```

### Explanation
この変更では、「Azure Machine Learningラベリングに関する文書」が完全に削除されました。具体的には、130行もの内容が削除され、Azure Machine Learningのラベリング機能をLanguage Studioで利用する方法に関する詳細なガイドが失われました。

文書には、ラベリングの手順、前提条件、制限、接続方法、ラベルのインポートおよびエクスポートの手続き、ならびにプロジェクトの管理方法についての情報が含まれていました。この情報の削除は、関連する内容が他の文書に統合されたか、もしくはサービスの提供形態の変更を反映している可能性があります。

このような重要な情報が削除されることは、ユーザーにとっての利用手順や理解に大きな影響を与えるため、注意が必要です。ユーザーは代替の資料を参照し、新たなガイドラインに従って作業を行う必要があります。

## articles/ai-services/language-service/question-answering/tutorials/bot-service.md{#item-f8e773}

<details>
<summary>Diff</summary>
````diff
@@ -1,86 +0,0 @@
----
-title: "Tutorial: Create an FAQ bot with custom question answering and Azure AI Bot Service"
-description: In this tutorial, create a no code FAQ Bot with custom question answering and Azure AI Bot Service.
-ms.service: azure-ai-language
-ms.topic: tutorial
-author: laujan
-ms.author: lajanuar
-ms.date: 11/18/2025
-ms.custom:
-  - language-service-question-answering
-  - cogserv-non-critical-language
-  - sfi-image-nochange
----
-# Tutorial: Create an FAQ bot
-
-Create an FAQ Bot with custom question answering and Azure [Bot Service](https://azure.microsoft.com/services/bot-service/) with no code.
-
-In this tutorial, you learn how to:
-
-<!-- green checkmark -->
-> [!div class="checklist"]
-> * Link a custom question answering project to an Azure AI Bot Service
-> * Deploy a Bot
-> * Chat with the Bot in web chat
-> * Enable the Bot in supported channels
-
-## Create and publish a project
-
-Follow the [getting started article](../how-to/create-test-deploy.md). Once the project has been successfully deployed, you will be ready to start this article.
-
-## Create a bot
-
-After deploying your project, you can create a bot from the **Deploy project** page:
-
-* You can create several bots quickly, all pointing to the same project for different regions or pricing plans for the individual bots.
-
-* When you make changes to the project and redeploy, you don't need to take further action with the bot. It's already configured to work with the project, and works with all future changes to the project. Every time you publish a project, all the bots connected to it are automatically updated.
-
-1. In [Language Studio](https://language.azure.com/), on the custom question answering **Deploy project** page, select the **Create a bot** button.
-
-    > [!div class="mx-imgBorder"]
-    > ![Screenshot of UI with option to create a bot in Azure.](../media/bot-service/create-bot-in-azure.png)
-
-1. A new browser tab opens for the Azure portal, with the Azure AI Bot Service's creation page. Configure the Azure AI Bot Service and hit the **Create** button.
-
-    |Setting |Value|
-    |----------|---------|
-    | Bot handle| Unique identifier for your bot. This value needs to be distinct from your App name |
-    | Subscription | Select your subscription |
-    | Resource group | Select an existing resource group or create a new one |
-    | Location | Select your desired location |
-    | Pricing tier | Choose pricing tier |
-    |App name | App service name for your bot |
-    |SDK language | C# or Node.js. Once the bot is created, you can download the code to your local development environment and continue the development process. |
-    | Language Resource Key  | This key is automatically populated deployed custom question answering project |
-    | App service plan/Location | This value is automatically populated, do not change this value |
-
-1. After the bot is created, open the **Bot service** resource.
-1. Under **Settings**, select **Test in Web Chat**.
-
-    > [!div class="mx-imgBorder"]
-    > ![Screenshot of Azure AI Bot Service UI button that reads "Test web chat".](../media/bot-service/test-in-web-chat.png)
-
-1. At the chat prompt of **Type your message**, enter:
-
-    `How do I setup my surface book?`
-
-    The chat bot responds with an answer from your project.
-
-    > [!div class="mx-imgBorder"]
-    > ![Screenshot of bot test chat response containing a question and bot generated answer.](../media/bot-service/bot-chat.png)
-
-## Integrate the bot with channels
-
-Select **Channels** in the Bot service resource that you create. You can activate the Bot in additional [supported channels](/azure/bot-service/bot-service-manage-channels).
-
-   >[!div class="mx-imgBorder"]
-   >![Screenshot of integration with teams with product icons.](../media/bot-service/channels.png)
-
-## Clean up resources
-
-If you're not going to continue to use this application, delete the associate custom question answering and bot service resources.
-
-## Next steps
-
-Advance to the next article to learn how to customize your FAQ bot with multi-turn prompts.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "FAQボット作成チュートリアルの削除"
}
```

### Explanation
この変更では、「カスタム質問応答とAzure AIボットサービスを使用したFAQボットの作成に関するチュートリアル」が削除されました。合計86行の内容が削除されたことで、ユーザーはこの特定のプロセスに関する情報を失うことになります。

削除されたセクションには、FAQボットの作成手順、プロジェクトのデプロイ方法、ボットの設定やチャネルとの統合に関する具体的な手順が含まれていました。この情報は、特にコーディングの知識がないユーザーにとって有益であり、ノーコードでボットを構築する際の手助けとなっていました。

このドキュメントの削除は、ボットの作成や質問応答のカスタマイズに関するリソースへのアクセスを制限し、ユーザーが必要とする情報を他の場所で見つける必要があることを意味します。この変更により、ボットサービスを利用するユーザーは新たなガイドラインや資料を探さなければならなくなります。

## articles/ai-services/language-service/question-answering/tutorials/guided-conversations.md{#item-a43dd4}

<details>
<summary>Diff</summary>
````diff
@@ -1,90 +0,0 @@
----
-title: Add guided conversations with multi-turn prompts
-description: In this tutorial, learn how to make guided conversations with multi-turn prompts.
-ms.service: azure-ai-language
-ms.topic: tutorial
-author: laujan
-ms.author: lajanuar
-ms.date: 11/18/2025
-ms.custom: language-service-question-answering
----
-# Add guided conversations with multi-turn prompts
-
-In this tutorial, you learn how to:
-
-> [!div class="checklist"]
-> * Add new question and answer pairs to your existing project
-> * Add follow-up prompts to create guided conversations
-> * Test your multi-turn prompts
-
-## Prerequisites
-
- In this tutorial, we use [Surface Pen FAQ](https://support.microsoft.com/surface/how-to-use-your-surface-pen-8a403519-cd1f-15b2-c9df-faa5aa924e98) to create a project.
-
-If you have never created a custom question answering project before we recommend starting with the [getting started](../how-to/create-test-deploy.md) article, which will take you step-by-step through the process.
-
-## View question answer pair context
-
-For this example, let's assume that users are asking for additional details about the Surface Pen product, particularly how to troubleshoot their Surface Pen, but they are not getting the correct answers. So, we add more prompts to support additional scenarios and guide the users to the correct answers using multi-turn prompts.
-
-Multi-turn prompts that are associated with question and answer pairs, can be viewed by selecting **Show columns** > **Context**. By default this should already be enabled on the **Edit project** page in Azure Language Studio custom question answering interface.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of show columns UI with context highlighted in red]( ../media/guided-conversations/context.png) ]( ../media/guided-conversations/context.png#lightbox)
-
-This displays the context tree where all follow-up prompts linked to a QnA pair are shown: 
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of Surface Pen FAQ page with answers to common questions]( ../media/guided-conversations/surface-source.png) ]( ../media/guided-conversations/surface-source.png#lightbox)
-
-## Add question pair with follow-up prompts
-
-To help users solve issues with their Surface Pen, we add follow-up prompts:
-
-- Add a new question pair with two follow-up prompts
-- Add a follow-up prompt to one of the newly added prompts
-
-1. Add a new QnA pair with two follow-up prompts **Check compatibility** and **Check Pen Settings**
-Using the editor, we add a new QnA pair with a follow-up prompt by selecting **Add question pair**
-
-    > [!div class="mx-imgBorder"]
-    > ![Screenshot of UI with "Add question pair" highlighted in a red box]( ../media/guided-conversations/add-question.png)
-    
-    A new row in **Editorial** is created where we enter the question answer pair as shown below:
-    
-    |Field|Value|
-    |-----|----|
-    |Questions | Fix problems with Surface |
-    |Answers and prompts | Here are some things to try first if your Surface Pen won't write, open apps, or connect to Bluetooth.|
-    
-2. We then add a follow-up prompt to the newly created question pair by choosing **Add follow-up prompts**. Fill the details for the prompt as shown:
-    
-    > [!div class="mx-imgBorder"]
-    > [ ![Screenshot of UI with "add a follow-up prompt" highlighted in a red box]( ../media/guided-conversations/add-prompts.png) ]( ../media/guided-conversations/add-prompts.png#lightbox)
-    
-    We provide **Check Compatibility** as the "Display text" for the prompt and try to link it to a QnA. Since, no related QnA pair is available to link to the prompt, when we search “Check your Surface Pen Compatibility”, we create a new question pair by selecting **Create link to new pair** and select **Done**. Then select **Save changes**.
-    
-    > [!div class="mx-imgBorder"]
-    > [ ![Screenshot of a question and answer about checking your surface pen compatibility]( ../media/guided-conversations/compatability-check.png) ]( ../media/guided-conversations/compatability-check.png#lightbox)
-    
-3. Similarly, we add another prompt **Check Pen Settings** to help the user troubleshoot the Surface Pen and add question pair to it.
-    
-    > [!div class="mx-imgBorder"]
-    > [ ![Screenshot of a question and answer about checking your surface pen settings]( ../media/guided-conversations/pen-settings.png) ]( ../media/guided-conversations/check-pen-settings.png#lightbox)
-
-4. Add another follow-up prompt to the newly created prompt. We now add “Replace Pen tips’ as a follow-up prompt to the previously created prompt “Check Pen Settings”.
-
-    > [!div class="mx-imgBorder"]
-    > [ ![Screenshot of a question and answer about creating a follow-up prompt for replacing pen tips]( ../media/guided-conversations/replace-pen.png) ]( ../media/guided-conversations/replace-pen.png#lightbox)
-    
-5. Finally, save the changes and test these prompts in the **Test** pane:
-    
-    > [!div class="mx-imgBorder"]
-    > [ ![Screenshot of question answer UI with save changes highlighted in a red box]( ../media/guided-conversations/save-changes.png) ]( ../media/guided-conversations/save-changes.png#lightbox)
-    
-    For a user query **Issues with Surface Pen**, the system returns an answer and presents the newly added prompts to the user. The user then selects one of the prompts **Check Pen Settings** and the related answer is returned to the user with another prompt **Replace Pen Tips**, which when selected further provides the user with more information. So, multi-turn is used to help and guide the user to the desired answer.
-    
-    > [!div class="mx-imgBorder"]
-    > [ ![Screenshot of chat test UI]( ../media/guided-conversations/test.png) ]( ../media/guided-conversations/test.png#lightbox)
-
-## Next steps
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "ガイド付き会話チュートリアルの削除"
}
```

### Explanation
この変更では、「ガイド付き会話とマルチターンプロンプトの作成に関するチュートリアル」が削除されました。合計90行が削除されたことで、ユーザーは特定のチュートリアルに沿ったガイドを失うことになります。

削除されたセクションには、マルチターンプロンプトを使用してユーザーにガイド付き会話を提供する方法、具体的な質問と回答のペアを追加する方法、プロンプトをテストする方法が含まれていました。特に、Surface Penに関するFAQを活用して、ユーザーが問い合わせに効果的に応答できるように設計されたこのチュートリアルは、実践的な手順と視覚的なサポートを提供していました。

このドキュメントの削除は、特に新たにカスタム質問応答プロジェクトを作成しようとするユーザーにとって、大きな影響を与える可能性があります。ユーザーは代替リソースを探す必要があり、このフレームワークを通じて効果的な対話型ボットを構築するための手助けが減少します。

## articles/ai-services/language-service/question-answering/tutorials/multiple-languages.md{#item-1966cb}

<details>
<summary>Diff</summary>
````diff
@@ -1,86 +0,0 @@
----
-title: Create projects in multiple languages - custom question answering
-description: In this tutorial, learn how to create projects with multiple languages.
-ms.service: azure-ai-language
-ms.topic: tutorial
-author: laujan
-ms.author: lajanuar
-ms.date: 11/18/2025
-ms.custom: language-service-question-answering
----
-# Create projects in multiple languages
-
-In this tutorial, you learn how to:
-
-<!-- green checkmark -->
-> [!div class="checklist"]
-> * Create a project that supports English
-> * Create a project that supports German
-
-This tutorial walks you through the process of creating projects in multiple languages. We use the [Surface Pen FAQ](https://support.microsoft.com/surface/how-to-use-your-surface-pen-8a403519-cd1f-15b2-c9df-faa5aa924e98) URL to create projects in German and English. We then deploy the project and use the custom question answering REST API to query and get answers to FAQs in the desired language.
-
-## Create project in German
-
-To be able to create a project in more than one language, the multiple language setting must be set at the creation of the first project that is associated with the language resource.
-
-> [!div class="mx-imgBorder"]
-> [![Screenshot of UI for create project with I want to select the language when I create a project in this resource selected.](../media/multiple-languages/multiple-languages.png)](../media/multiple-languages/multiple-languages.png#lightbox)
-
-1. From the [Language Studio](https://aka.ms/languageStudio) home page, select open custom question answering. Select **Create new project** > **I want to select the language when I create a project in this resource** > **Next**.
-
-2. Fill out enter basic information page and select **Next** > **Create project**.
-
-    |Setting| Value|
-    |---|----|
-    |Name | Unique name for your project|
-    |Description | Unique description to help identify the project |
-    |Source language | For this tutorial, select German |
-    |Default answer | Default answer when no answer is returned |
-
-    > [!div class="mx-imgBorder"]
-    > [![Screenshot of UI for create project with the German language selected.](../media/multiple-languages/choose-german.png)](../media/multiple-languages/choose-german.png#lightbox)
-
-3. **Add source** > **URLs** > **Add url** > **Add all**.
-
-    |Setting| Value |
-    |----|------|
-    | Url Name | Surface Pen German |
-    | URL | https://support.microsoft.com/de-de/surface/how-to-use-your-surface-pen-8a403519-cd1f-15b2-c9df-faa5aa924e98 |
-    | Classify file structure | Autodetect |
-    
-    Custom question answering reads the document and extracts question answer pairs from the source URL to create the project in the German language. If you select the link to the source, the project page opens where we can edit the contents.
-    
-    > [!div class="mx-imgBorder"]
-    > [![Screenshot of UI with German questions and answers](../media/multiple-languages/german-language.png)](../media/multiple-languages/german-language.png#lightbox)
-    
-## Create project in English
-
-We now repeat the above steps from before but this time we select English and an English URL as a source.
-
-1. From the [Language Studio](https://aka.ms/languageStudio), open the custom question answering page > **Create new project**.
-
-1. Fill out enter basic information page and select **Next** > **Create project**.
-
-    |Setting| Value|
-    |---|----|
-    |Name | Unique name for your project|
-    |Description | Unique description to help identify the project |
-    |Source language | For this tutorial, select English |
-    |Default answer | Default answer when no answer is returned |
-
-1. **Add source** > **URLs** > **Add url** > **Add all**.
-
-    |Setting| Value |
-    |-----|-----|
-    | Url Name | Surface Pen German |
-    | URL | https://support.microsoft.com/en-us/surface/how-to-use-your-surface-pen-8a403519-cd1f-15b2-c9df-faa5aa924e98 |
-    | Classify file structure | Autodetect |
-
-## Deploy and query project
-
-We're now ready to deploy the two projects and query them in the desired language using the custom question answering REST API. Once a project is deployed, the following page is shown which provides details to query the project.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of UI with English questions and answers](../media/multiple-languages/get-prediction-url.png) ](../media/multiple-languages/get-prediction-url.png#lightbox)
-
-The language for the incoming user query can be detected with the [Language Detection API](../../language-detection/how-to/call-api.md) and the user can call the appropriate endpoint and project depending on the detected language.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "複数言語プロジェクト作成チュートリアルの削除"
}
```

### Explanation
この変更では、「複数言語でプロジェクトを作成する方法に関するチュートリアル」が削除されました。合計86行の内容が削除されたため、ユーザーはこの部分に関連する情報を失うことになります。

削除されたセクションには、英語とドイツ語をサポートするプロジェクトの作成手順と、カスタム質問応答APIを使用して特定の言語でFAQに対してクエリを実行する方法が含まれていました。具体的には、Surface Penに関するサポート情報を元に、言語を選択してプロジェクトを設定し、必要なURLを追加する流れを詳細に説明していました。

このドキュメントの削除により、多言語対応のプロジェクトを構築しようとしていたユーザーは、適切なリソースを見つけるのが難しくなる可能性があります。また、マルチランゲージ設定によるカスタム質問応答の実装方法についての理解が失われるため、これに関連する機能を利用するには他のガイドや資料を探す必要があります。

## articles/ai-services/language-service/question-answering/tutorials/power-virtual-agents.md{#item-aec51d}

<details>
<summary>Diff</summary>
````diff
@@ -1,214 +0,0 @@
----
-title: "Tutorial: Add your custom question answering project to Power Virtual Agents"
-description: In this tutorial, you will learn how to add your custom question answering project to Power Virtual Agents.
-ms.service: azure-ai-language
-ms.topic: tutorial
-author: laujan
-ms.author: lajanuar
-ms.date: 11/18/2025
-ms.custom: language-service-question-answering
----
-# Add your custom question answering project to Power Virtual Agents
-
-Create and extend a [Power Virtual Agents](https://powervirtualagents.microsoft.com/) bot to provide answers from your project. 
-
-> [!NOTE]
-> The integration demonstrated in this tutorial is in preview and is not intended for deployment to production environments. 
-
-In this tutorial, you learn how to: 
-> [!div class="checklist"]
-> * Create a Power Virtual Agents bot 
-> * Create a system fallback topic
-> * Add custom question answering as an action to a topic as a Power Automate flow
-> * Create a Power Automate solution
-> * Add a Power Automate flow to your solution
-> * Publish Power Virtual Agents
-> * Test Power Virtual Agents, and receive an answer from your custom question answering project
-
-> [!NOTE]
-> The QnA Maker service is being retired on the 31st of March, 2025. A newer version of the question and answering capability is now available as part of [Azure Language in Foundry Tools](../../index.yml). For custom question answering capabilities within Azure Language, see [custom question answering](../overview.md). Starting 1st October, 2022 you won’t be able to create new QnA Maker resources. For information on migrating existing QnA Maker knowledge bases to custom question answering, consult the [migration guide](../how-to/migrate-qnamaker.md).
-
-## Create and publish a project
-1. Follow the [quickstart](../quickstart/sdk.md?pivots=studio) to create a custom question answering project. Once you have deployed your project.
-2. After deploying your project from Language Studio, select “Get Prediction URL”. 
-3. Get your Site URL from the hostname of Prediction URL and your Account key which would be the Ocp-Apim-Subscription-Key.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of how to obtain the prediction URL and subscription key displayed.]( ../media/power-virtual-agents/get-prediction-url.png) ]( ../media/power-virtual-agents/get-prediction-url.png#lightbox)
-
-4. Create a custom question answering connector: Follow the [connector documentation](/connectors/languagequestionansw/) to create a connection to question answering.
-5. Use this tutorial to create a Bot with Power Virtual Agents instead of creating a bot from Language Studio.
-
-## Create a bot in Power Virtual Agents
-[Power Virtual Agents](https://powervirtualagents.microsoft.com/) allows teams to create powerful bots by using a guided, no-code graphical interface. You don't need data scientists or developers.
-
-Create a bot by following the steps in [Create and delete Power Virtual Agents bots](/power-virtual-agents/authoring-first-bot).
-
-## Create the system fallback topic
-In Power Virtual Agents, you create a bot with a series of topics (subject areas), in order to answer user questions by performing actions.
-
-Although the bot can connect to your project from any topic, this tutorial uses the system fallback topic. The fallback topic is used when the bot can't find an answer. The bot passes the user's text to custom question answering Query knowledgebase API, receives the answer from your project, and displays it to the user as a message.
-
-Create a fallback topic by following the steps in [Configure the system fallback topic in Power Virtual Agents](/power-virtual-agents/authoring-system-fallback-topic).
-
-## Use the authoring canvas to add an action
-Use the Power Virtual Agents authoring canvas to connect the fallback topic to your project. The topic starts with the unrecognized user text. Add an action that passes that text to custom question answering, and then shows the answer as a message. The last step of displaying an answer is handled as a [separate step](../../../QnAMaker/Tutorials/integrate-with-power-virtual-assistant-fallback-topic.md), later in this tutorial.
-
-This section creates the fallback topic conversation flow.
-
-The new fallback action might already have conversation flow elements. Delete the **Escalate** item by selecting the **Options** menu.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of how to delete existing conversation flow elements.]( ../media/power-virtual-agents/delete-action.png) ]( ../media/power-virtual-agents/delete-action.png#lightbox)
-
-Below the *Message* node, select the (**+**) icon, then select **Call an action**.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of how select the Call an action feature.]( ../media/power-virtual-agents/trigger-action-for-power-automate.png) ]( ../media/power-virtual-agents/trigger-action-for-power-automate.png#lightbox)
-
-Select **Create a flow**. This takes you to the Power Automate portal.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of where to find the Create a flow action.]( ../media/power-virtual-agents/create-flow.png) ]( ../media/power-virtual-agents/create-flow.png#lightbox)
-
-Power Automate opens a new template as shown below.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of the default Power Automate template.]( ../media/power-virtual-agents/power-automate-actions.png) ]( ../media/power-virtual-agents/power-automate-actions.png#lightbox)
-**Do not use the template shown above.**
-
-Instead you need to follow the steps below that creates a Power Automate flow. This flow:
-- Takes the incoming user text as a question, and sends it to custom question answering.
-- Returns the top response back to your bot.
-
-select **Create** in the left panel, then click "OK" to leave the page.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of the Create action in the left panel and a confirmation message for navigating away from the page.]( ../media/power-virtual-agents/power-automate-create-new.png) ]( ../media/power-virtual-agents/power-automate-create-new.png#lightbox)
-
-Select "Instant Cloud flow"
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of the Instant cloud flow selection box.]( ../media/power-virtual-agents/create-instant-cloud-flow.png) ]( ../media/power-virtual-agents/create-instant-cloud-flow.png#lightbox)
-
-For testing this connector, you can select “When PowerVirtual Agents calls a flow” and select **Create**.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of the When Power Virtual Agents calls a flow selection in the Choose how to trigger this flow list.]( ../media/power-virtual-agents/create-trigger.png) ]( ../media/power-virtual-agents/create-trigger.png#lightbox)
-
-Select "New Step" and search for "Power Virtual Agents". Choose "Add an input" and select text. Next, provide the keyword and the value.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of the Add an input option.]( ../media/power-virtual-agents/flow-step-1.png) ]( ../media/power-virtual-agents/flow-step-1.png#lightbox)
-
-Select "New Step" and search "Language - custom question answering" and choose "Generate answer from Project" from the three actions.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of the Generate answer from Project selection in the Action list.]( ../media/power-virtual-agents/flow-step-2.png) ]( ../media/power-virtual-agents/flow-step-2.png#lightbox)
-
-This option helps in answering the specified question using your project. Type in the project name, deployment name and API version and select the question from the previous step.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of fields for the Generate answer from Project action.]( ../media/power-virtual-agents/flow-step-3.png) ]( ../media/power-virtual-agents/flow-step-3.png#lightbox)
-
-Select "New Step" and search for "Initialize variable". Choose a name for your variable, and select the "String" type.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of the Initialize variable action fields.]( ../media/power-virtual-agents/flow-step-4.png) ]( ../media/power-virtual-agents/flow-step-4.png#lightbox)
-
-Select "New Step" again, and search for "Apply to each", then select the output from the previous steps and add an action of "Set variable" and select the connector action.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of the Set variable action within the Apply to each step.]( ../media/power-virtual-agents/flow-step-5.png) ]( ../media/power-virtual-agents/flow-step-5.png#lightbox)
-
-Select "New Step" and search for "Return value(s) to Power Virtual Agents" and type in a keyword, then choose the previous variable name in the answer.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of the Return value(s) to Power Virtual Agents step, containing the previous variable.]( ../media/power-virtual-agents/flow-step-6.png) ]( ../media/power-virtual-agents/flow-step-6.png#lightbox)
-
-The list of completed steps should look like this.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of the full list of completed steps within Power Virtual Agents.]( ../media/power-virtual-agents/flow-step-7.png) ]( ../media/power-virtual-agents/flow-step-7.png#lightbox)
-
-Select **Save** to save the flow.
-
-## Create a solution and add the flow
-
-For the bot to find and connect to the flow, the flow must be included in a Power Automate solution.
-
-1. While still in the Power Automate portal, select Solutions from the left-side navigation.
-2. Select **+ New solution**.
-3. Enter a display name. The list of solutions includes every solution in your organization or school. Choose a naming convention that helps you filter to just your solutions. For example, you might prefix your email to your solution name: jondoe-power-virtual-agent-question-answering-fallback.
-4. Select your publisher from the list of choices.
-5. Accept the default values for the name and version.
-6. Select **Create** to finish the process.
-
-**Add your flow to the solution**
-
-1. In the list of solutions, select the solution you just created. It should be at the top of the list. If it isn't, search by your email name, which is part of the solution name.
-2. In the solution, select **+ Add existing**, and then select Flow from the list.
-3. Find your flow from the **Outside solutions** list, and then select Add to finish the process. If there are many flows, look at the **Modified** column to find the most recent flow.
-
-## Add your solution's flow to Power Virtual Agents
-
-1. Return to the browser tab with your bot in Power Virtual Agents. The authoring canvas should still be open.
-2. To insert a new step in the flow, above the **Message** action box, select the plus (+) icon. Then select **Call an action**.
-3. From the **Flow** pop-up window, select the new flow named **Generate answers using Question Answering Project...**. The new action appears in the flow.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of the Call an action using the Generate answers using Question Answering Project flow.]( ../media/power-virtual-agents/flow-step-8.png) ]( ../media/power-virtual-agents/flow-step-8.png#lightbox)
-
-4. To correctly set the input variable to the QnA Maker action, select **Select a variable**, then select **bot.UnrecognizedTriggerPhrase**.
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of the selected bot.UnrecognizedTriggerPhrase variable within the action call.]( ../media/power-virtual-agents/flow-step-9.png) ]( ../media/power-virtual-agents/flow-step-9.png#lightbox)
-
-5. To correctly set the output variable to the custom Question Answering action, in the **Message** action, select **UnrecognizedTriggerPhrase**, then select the icon to insert a variable, {x}, then select **FinalAnswer**.
-6. From the context toolbar, select **Save**, to save the authoring canvas details for the topic.
-
-Here's what the final bot canvas looks like:
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of the completed bot canvas.]( ../media/power-virtual-agents/flow-step-10.png) ]( ../media/power-virtual-agents/flow-step-10.png#lightbox)
-
-## Test the bot
-
-As you design your bot in Power Virtual Agents, you can use the [Test bot pane](/power-virtual-agents/authoring-test-bot) to see how the bot leads a customer through the bot conversation.
-
-1. In the test pane, toggle **Track between topics**. This allows you to watch the progression between topics, as well as within a single topic.
-2. Test the bot by entering the user text in the following order. The authoring canvas reports the successful steps with a green check mark.
-
-|**Question order**|**Test questions**                                                 |**Purpose**                                                                                                                           |
-|------------------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
-|1                 |Hello                                                              |Begin conversation                                                                                                                          |
-|2                 |Store hours                                                        |Sample topic. This is configured for you without any additional work on your part.                                                                                                                            |
-|3                 |Yes                                                                |In reply to "Did that answer your question?"                                                                                                                                     |
-|4                 |Excellent                                                          |In reply to "Please rate your experience."                                                                                                                                     |
-|5                 |Yes                                                                |In reply to "Can I help with anything else?"                                                                                                                                     |
-|6                 |How can I improve the throughput performance for query predictions?|This question triggers the fallback action, which sends the text to your project to answer. Then the answer is shown. the green check marks for the individual actions indicate success for each action.|
-
-> [!div class="mx-imgBorder"]
-> [ ![Screenshot of the completd test bot running alongside the tutorial flow.]( ../media/power-virtual-agents/flow-step-11.png) ]( ../media/power-virtual-agents/flow-step-11.png#lightbox)
-
-## Publish your bot
-
-To make the bot available to all members of your organization, you need to publish it.
-
-Publish your bot by following the steps in [Publish your bot](/power-virtual-agents/publication-fundamentals-publish-channels).
-
-## Share your bot
-
-To make your bot available to others, you first need to publish it to a channel. For this tutorial we'll use the demo website.
-
-Configure the demo website by following the steps in [Configure a chatbot for a live or demo website](/power-virtual-agents/publication-connect-bot-to-web-channels).
-
-Then you can share your website URL with your school or organization members.
-
-## Clean up resources
-
-When you're done with the project, remove the QnA Maker resources in the Azure portal.
-
-## See also
-
-* [Tutorial: Create an FAQ bot](../tutorials/bot-service.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Power Virtual Agentsへのカスタム質問応答プロジェクト追加チュートリアルの削除"
}
```

### Explanation
この変更では、「Power Virtual Agentsにカスタム質問応答プロジェクトを追加する方法に関するチュートリアル」が削除されました。このセクションは214行もあり、ユーザーはPower Virtual Agentsとカスタム質問応答機能を統合する方法についての詳細を失うことになります。

削除されたチュートリアルは、Power Virtual Agentsボットを作成し、質問応答プロジェクトを統合してFAQに対する応答を提供する手順を説明していました。具体的には、システムフォールバックトピックの作成、Power Automateを使用したカスタム質問応答の追加、プロジェクトのデプロイ方法などが含まれていました。また、QnA Makerサービスの引退と、その代替としてのカスタム質問応答機能についての重要な情報も提供されていました。

このドキュメントの削除により、Power Virtual Agentsでのプロジェクトの設定や運用に関心のあるユーザーは、必要なリソースや手順を見つけることが難しくなる可能性があります。特に、新規のボット開発を行う開発者やチームには影響が大きく、何らかの代替資料を探す必要があります。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -226,22 +226,12 @@ items:
         href: conversational-language-understanding/concepts/app-architecture.md
     - name: Tutorials
       items:
-      - name: Create an FAQ Bot
-        href: question-answering/tutorials/bot-service.md
-        displayName: bot framework, chatbot
-      - name: Guided conversations
-        href: question-answering/tutorials/guided-conversations.md
       - name: Active learning
         href: question-answering/tutorials/active-learning.md
       - name: Adding synonyms
         href: question-answering/tutorials/adding-synonyms.md
-      - name: Multiple languages
-        href: question-answering/tutorials/multiple-languages.md
       - name: Multiple domains
         href: question-answering/tutorials/multiple-domains.md
-      - name: Add your custom question answering project to Microsoft Copilot Studios
-        href: question-answering/tutorials/power-virtual-agents.md
-        displayName: power virtual agents, pva integration, chatbot, virtual assistant
     - name: Reference
       items:
       - name: General
@@ -290,12 +280,6 @@ items:
       - name: Label data
         href: custom-text-classification/how-to/tag-data.md
         displayName: tag data, annotate text, training data
-      - name: Auto label your data (preview)
-        href: custom-text-classification/how-to/use-autolabeling.md
-        displayName: automatic annotation, smart labeling, ai assisted labeling
-      - name: Label data with Azure Machine Learning
-        href: custom/azure-machine-learning-labeling.md
-        displayName: azure ml labeling, aml annotation
       - name: Train a model
         href: custom-text-classification/how-to/train-model.md
         displayName: training, classifier, build model
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サービスの目次ファイルの更新"
}
```

### Explanation
この変更は、言語サービスに関する目次ファイル（toc.yml）の修正です。合計16行が削除され、いくつかのチュートリアルのリンクが目次から除外されました。

具体的には、以下のチュートリアルが目次から削除されました:
- FAQボットの作成
- ガイド付き会話
- 複数言語に関するチュートリアル
- Power Virtual Agentsへのカスタム質問応答プロジェクトの追加

これにより、目次からこれらのトピックにアクセスできなくなります。残りのチュートリアルとして、アクティブ学習や同義語の追加、複数のドメインに関する内容は引き続き利用可能です。また、今後の内容更新や新たなチュートリアルが追加される場合、ユーザーはこれらの削除されたトピックについての情報を他の場所で探す必要があります。この変更は、特に新しいユーザーやボット開発に関心のあるチームに影響を与える可能性があります。


