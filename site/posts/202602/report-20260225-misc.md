---
date: '2026-02-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6a204e3...MicrosoftDocs:7d59142
summary: |-
  要約:
  この変更は、Azure Language Serviceに関連するドキュメントの整理と更新を目的としています。いくつかの重要な変更と軽微な更新があり、複数のドキュメントが削除され、特に手順の明確化が進められています。新たにKubernetesへのキーフレーズ抽出コンテナのデプロイ手順のセクションも追加され、ユーザー体験が向上することが期待されていますが、重要な手順や情報の削除に伴い、従来のユーザーは新しい作業フローに適応する必要があります。全体として、情報の整頓と視覚的改善が進み、ユーザーはより効率的にAzure環境を利用できるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6a204e3...MicrosoftDocs:7d59142){target="_blank"}

<format>
# ハイライト
このコード差分は、Azure Language Serviceに関連するドキュメントと手順の大幅な整理と更新を目的としたもので、いくつかの重大な変更と様々な軽微な更新を含んでいます。複数のドキュメントファイルが削除され、主に手順の明確化と情報の整理が促進されています。この結果、ユーザーはサポートドキュメントへの参照を調整する必要がある一方で、新しい手順書や手続きを利用する機会が提供されています。

## 新機能
- Kubernetesにキーフレーズ抽出コンテナをデプロイする手順が強化され、新しいセクションが追加されました。

## 破壊的変更
- 多数の手順ガイド文書が削除され、モデル削除、予測URL取得、SDKバージョン情報などに関する重要な情報が失われました。

## その他の更新
- API呼び出し手順やドキュメントの文字情報が整えられ、ユーザーがより簡単に情報を見つけられるように視覚的な改善が施されています。

# 洞察
この差分では、Azure Language Serviceに関連するドキュメントの改善と統合が主な目的とされています。多くの手順やガイドが削除された理由は、ドキュメントの集約や情報提供の効率化を図るためと考えられます。これにより、情報の冗長性が削減され、特定の手順が利用不可になったことで、従来のユーザーが新しい作業フローに適応する必要が生じます。

特に破壊的変更とされた「SDKターゲットバージョン情報」や「Azureポータルのキーとエンドポイントに関するページ」の削除は、SDKの互換性やAPIキー管理に関する重要情報が失われるため、関連する知識を持つユーザーにはかなりの影響を及ぼすでしょう。しかし、このような深刻な変化はドキュメントの統一と将来の更新の簡素化につながる可能性も秘めています。

さらに、Kubernetesへのキーフレーズ抽出コンテナのデプロイ手順の強化は、ユーザーがAzureサービスと連携する際のハードルを下げ、実装の際の準備がスムーズになるよう意図されています。この施策によって、Azure Kubernetes Serviceを用いたデプロイフローが改善され、ユーザーの開発体験が向上することが期待されます。

一方で特定の情報がリンク形式からプレーンテキストの形式に変更された例もあり、情報の取り出しが容易になるような配慮がなされています。全体として、ドキュメントの統合と簡潔化が進められており、ユーザーはより洗練されたインターフェースを通じて情報へアクセスし、Azure環境の利用を効率的に進められることが目指されています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [call-api.md](#item-30dce9) | minor update | API呼び出しの手順を更新 | modified | 5 | 1 | 6 | 
| [key-endpoint-page.png](#item-be4fc8) | minor update | 画像ファイルの名前を変更 | renamed | 0 | 0 | 0 | 
| [create-text-analytics-resource.md](#item-9ad318) | breaking change | テキスト分析リソース作成ガイドの削除 | removed | 0 | 33 | 33 | 
| [delete-model-language-studio.md](#item-d249ac) | breaking change | Language Studioからのモデル削除手順の削除 | removed | 0 | 15 | 15 | 
| [delete-model-rest-api.md](#item-4e3628) | breaking change | REST APIによるモデル削除手順の削除 | removed | 0 | 34 | 34 | 
| [get-prediction-url.md](#item-bfe66f) | breaking change | 予測URL取得手順の削除 | removed | 0 | 30 | 30 | 
| [load-export-model-language-studio.md](#item-468a0f) | breaking change | モデルデータのロードおよびエクスポート手順の削除 | removed | 0 | 23 | 23 | 
| [load-export-model-rest-api.md](#item-718ea8) | breaking change | モデルデータのロードとエクスポート手順の削除 | removed | 0 | 80 | 80 | 
| [model-evaluation-language-studio.md](#item-741c45) | breaking change | モデル評価手順の削除 | removed | 0 | 80 | 80 | 
| [project-details.md](#item-3a6d16) | breaking change | プロジェクト詳細情報の手順の削除 | removed | 0 | 20 | 20 | 
| [resource-creation-language-studio.md](#item-bd3ca8) | breaking change | リソース作成手順の削除 | removed | 0 | 28 | 28 | 
| [roles-for-resource-and-storage.md](#item-d4eac6) | minor update | 役割設定手順の更新 | modified | 2 | 2 | 4 | 
| [use-pre-existing-resource.md](#item-a883ba) | minor update | 既存のリソース使用手順の更新 | modified | 15 | 27 | 42 | 
| [key-endpoint-page-azure-portal.md](#item-fec9be) | breaking change | Azureポータルのキーとエンドポイントに関するページの削除 | removed | 0 | 13 | 13 | 
| [sdk-target-versions.md](#item-59b6f8) | breaking change | SDKターゲットバージョン情報の削除 | removed | 0 | 19 | 19 | 
| [best-practices.md](#item-f97daf) | minor update | ベストプラクティスにおけるチャットパーソナリティ情報の改善 | modified | 5 | 5 | 10 | 
| [document-format-guidelines.md](#item-fb0489) | minor update | 文書形式ガイドラインの例文修正 | modified | 1 | 1 | 2 | 
| [use-kubernetes-service.md](#item-986931) | minor update | Kubernetesサービスへのキー フレーズ抽出コンテナのデプロイ手順の更新 | modified | 25 | 4 | 29 | 


# Modified Contents
## articles/ai-services/language-service/custom-text-classification/how-to/call-api.md{#item-30dce9}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,11 @@ You can query the deployment programmatically [Prediction API](/rest/api/languag
 
 First you need to get your resource key and endpoint:
 
-[!INCLUDE [Get keys and endpoint Azure portal](../../includes/key-endpoint-page-azure-portal.md)]
+1. Go to your resource overview page in the [Azure portal](https://portal.azure.com/#home)
+
+1. From the menu on the left side, select **Keys and Endpoint**. You use the endpoint and key for the API requests.
+
+    :::image type="content" source="../media/key-endpoint-page.png" alt-text="A screenshot showing the key and endpoint page in the Azure portal." lightbox="../media/key-endpoint-page.png":::
 
 ### Submit a custom text classification task
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "API呼び出しの手順を更新"
}
```

### Explanation
この変更は、Azureポータルからリソースのキーとエンドポイントを取得する手順を明確にするためのもので、API呼び出しに関するドキュメントが更新されました。具体的には、手順が段階的に書かれ、ユーザーがAzureポータルでキーとエンドポイントを見つけるための具体的なナビゲーションの指示が追加されました。また、関連する画像が挿入されて、視覚的に理解しやすくなっています。これにより、ユーザーが自分のAPIリクエストに必要な情報を迅速に把握できるようになります。

## articles/ai-services/language-service/custom-text-classification/media/key-endpoint-page.png{#item-be4fc8}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの名前を変更"
}
```

### Explanation
この変更は、`key-endpoint-page.png`という画像ファイルの場所が変更されたことを示しています。元々のパスは`articles/ai-services/language-service/media/key-endpoint-page.png`でしたが、新しいパスは`articles/ai-services/language-service/custom-text-classification/media/key-endpoint-page.png`です。この変更は、ドキュメントの構成を改善し、関連するコンテンツの整理を目的としています。具体的な内容や構造には変更はありませんが、ファイル名の変更によって、より明確で整理された管理が可能になります。

## articles/ai-services/language-service/includes/containers/create-text-analytics-resource.md{#item-9ad318}

<details>
<summary>Diff</summary>
````diff
@@ -1,33 +0,0 @@
----
-title: Create an Azure Language in Foundry Tools resource
-titleSuffix: Foundry Tools
-description: Learn how to create an Azure Language in Foundry Tools resource.
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-## Create an Azure Language in Foundry Tools resource
-
-1. Sign in to the [Azure portal](https://portal.azure.com).
-1. Select **Create a resource**, and then go to **AI + Machine Learning** > **Language**.
-   Or, go to [Create a Language resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics).
-1. Enter all the required settings:
-
-    |Setting|Value|
-    |--|--|
-    |Name|Enter a name (2-64 characters).|
-    |Subscription|Select the appropriate subscription.|
-    |Location|Select a nearby location.|
-    |Pricing tier| Enter **S**, the standard pricing tier.|
-    |Resource group|Select an available resource group.|
-
-1. Select **Create**, and wait for the resource to be created. Your browser automatically redirects to the newly created resource page.
-1. Collect the configured `endpoint` and an API key:
-
-    |Resource tab in portal|Setting|Value|
-    |--|--|--|
-    |**Overview**|Endpoint|Copy the endpoint. It appears similar to `https://my-resource.cognitiveservices.azure.com/text/analytics/v3.0`.|
-    |**Keys**|API Key|Copy one of the two keys. It's a 32-character alphanumeric string with no spaces or dashes: <`xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`>.|
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "テキスト分析リソース作成ガイドの削除"
}
```

### Explanation
この変更は、`create-text-analytics-resource.md`というファイルが完全に削除されたことを示しています。このファイルには、Azure Language in Foundry Toolsリソースを作成する手順が詳細に記載されていました。具体的には、Azureポータルへのサインインから始まり、必要な設定を入力するためのステップバイステップのガイドラインや、APIキーとエンドポイントの収集方法が説明されていました。この削除は、ドキュメントの整理や重複の解消に目的があった可能性があり、結果として、ユーザーは他の資料や手順に基づいてリソースを作成する必要があります。

## articles/ai-services/language-service/includes/custom/delete-model-language-studio.md{#item-d249ac}

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
    "modification_title": "Language Studioからのモデル削除手順の削除"
}
```

### Explanation
この変更は、`delete-model-language-studio.md`というファイルが削除されたことを示しています。このファイルには、Language Studio内でモデルを削除する手順が記載されていました。具体的には、モデルパフォーマンスを選択し、削除したいモデル名を選択してから、確認メッセージでOKをクリックするという流れが説明されていました。この削除により、ユーザーはモデル削除の手順を他のリソースや文書を参照する必要があり、情報の一貫性や整理を図る目的があったと考えられます。

## articles/ai-services/language-service/includes/custom/delete-model-rest-api.md{#item-4e3628}

<details>
<summary>Diff</summary>
````diff
@@ -1,34 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-Create a **DELETE** request using the following URL, headers, and JSON body to delete a trained model.
-
-
-### Request URL
-
-```rest
-{Endpoint}/language/authoring/analyze-text/projects/{PROJECT-NAME}/models/{trainedModelLabel}?api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `myProject` |
-|`{trainedModelLabel}`     | The name for your model name. This value is case-sensitive.   | `model1` |
-|`{API-VERSION}`     | The version of the API you're calling. The value referenced is for the latest version released. See [Model lifecycle](../../concepts/model-lifecycle.md) to learn more about other available API versions.  | `2022-05-01` |
-
-### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-
-Once you send your API request, you receive a `204` response indicating success, which means your trained model is deleted.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "REST APIによるモデル削除手順の削除"
}
```

### Explanation
この変更は、`delete-model-rest-api.md`というファイルが削除されたことを示しています。このファイルには、トレーニング済みモデルを削除するためのREST APIを用いた手順が詳細に記述されていました。具体的には、DELETEリクエストを送信するためのURL、必要なヘッダー、およびJSONボディの構成が説明されており、APIリクエストの認証方法や成功時の応答についても触れられていました。この削除により、ユーザーはモデル削除に関する文書を別の場所で探す必要があり、システムの整合性やドキュメントの整理を目的として行われた可能性があります。

## articles/ai-services/language-service/includes/custom/get-prediction-url.md{#item-bfe66f}

<details>
<summary>Diff</summary>
````diff
@@ -1,30 +0,0 @@
----
-titleSuffix: Foundry Tools
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. After the deployment job is completed successfully, select the deployment you want to use and from the top menu select **Get prediction URL**.
-
-    :::image type="content" source="../../media/custom/get-prediction-url-1.png" alt-text="A screenshot showing the button to get a prediction URL." lightbox="../../media/custom/get-prediction-url-1.png":::
-
-2. In the window that appears, under the **Submit** pivot, copy the sample request URL and body into your command line.
-
-3. Replace `<YOUR_DOCUMENT_HERE>` with the actual text you want to extract entities from.
-
-    :::image type="content" source="../../media/custom/get-prediction-url-2.png" alt-text="A screenshot showing the example request." lightbox="../../media/custom/get-prediction-url-2.png":::
-
-4. Submit the `POST` cURL request in your terminal or command prompt. You receive a 202 response with the API results if the request was successful.
-
-5. In the response header you receive extract `{JOB-ID}` from `operation-location`, which has the format: `{ENDPOINT}/text/analytics/v3.2-preview.2/analyze/jobs/<JOB-ID}>`
-
-6. Back to Language Studio; select **Retrieve** pivot from the same window you got the example request you got earlier and copy the sample request into a text editor. 
-
-    :::image type="content" source="../../media/custom/get-prediction-url-3.png" alt-text="A screenshot showing the example retrieval request." lightbox="../../media/custom/get-prediction-url-3.png":::
-
-7. Replace `<JOB-ID>` with the `{JOB-ID}` you extracted from the previous step. 
-
-8. Submit the `GET` cURL request in your terminal or command prompt.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "予測URL取得手順の削除"
}
```

### Explanation
この変更は、`get-prediction-url.md`というファイルが削除されたことを示しています。このファイルには、デプロイメントが成功した後に予測URLを取得するための手順が詳細に記述されていました。具体的には、Language Studioのインターフェースを使用して予測URLを取得し、そのURLを使って実際のテキストからエンティティを抽出する手順が段階的に説明されていました。ユーザーはcURLリクエストを送信し、成功した場合にはAPI結果を取得することができるという流れが含まれていました。この削除により、関連する情報が他の文書に移行された可能性があり、ユーザーは新たなリソースを参照する必要が出てきます。これにより、ドキュメントの整理や情報の一貫性を図ることが目的とされた可能性があります。

## articles/ai-services/language-service/includes/custom/load-export-model-language-studio.md{#item-468a0f}

<details>
<summary>Diff</summary>
````diff
@@ -1,23 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To **load** your model data:
-
-1. Select any model in the **model evaluation** page.
-
-2. Select the **Load model data** button. 
-
-3. Confirm that you do not have any unsaved changes you need to capture in window that appears, and select **Load data**. 
-
-4. Wait until your model data finishes loading back into your project. On completion, you'll be redirected back to the **Schema design** page. 
-
-To **export** your model data:
-
-1. Select any model in the **model evaluation** page.
-
-2.  Select the **Export model data** button. Wait for the JSON snapshot of your model to be downloaded locally. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルデータのロードおよびエクスポート手順の削除"
}
```

### Explanation
この変更は、`load-export-model-language-studio.md`というファイルが削除されたことを示しています。このファイルには、Language Studioを使用してモデルデータをロードおよびエクスポートするための具体的な手順が記述されていました。手順には、モデル評価ページでモデルを選択し、ロードまたはエクスポートボタンを押すこと、確認ダイアログでの確認、プロジェクトへのモデルデータのロード完了後のリダイレクトについての説明が含まれていました。この削除により、ユーザーはモデルデータの管理に関する情報を他のリソースから探さなければならなくなります。ドキュメントの整備や更新が意図されている可能性があります。

## articles/ai-services/language-service/includes/custom/load-export-model-rest-api.md{#item-718ea8}

<details>
<summary>Diff</summary>
````diff
@@ -1,80 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-### Load model data 
-
-Create a **POST** request using the following URL, headers, and JSON body to load your model data to your project.
-
-### Request URL
-
-Use the following URL when creating your API request. Replace the placeholder values with your own values. 
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/models/{MODEL-NAME}:load-snapshot?stringIndexType=Utf16CodeUnit&api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `EmailApp` |
-|`{API-VERSION}`     | The version of the API you're calling. | `2022-10-01-preview` |
-|`{MODEL-NAME}`       | The name of your model. This value is case-sensitive. | `v1` |
-
-### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-
-Once you send your API request, you receive a `202` response indicating success. In the response headers, extract the `operation-location` value formatted like this: 
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/models/{MODEL-NAME}/jobs/{JOB-ID}?api-version={API-VERSION}
-``` 
-
-`JOB-ID` is used to identify your request, since this operation is asynchronous. Use this URL to get the status of your model data loading, using the same authentication method.
-
-
-### Export model data
-
-Create a **POST** request using the following URL, headers, and JSON body to export your model data.
-
-### Request URL
-
-Use the following URL when creating your API request. Replace the placeholder values with your own values. 
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/:export?stringIndexType=Utf16CodeUnit&api-version={API-VERSION}&trainedModelLabel={MODEL-NAME}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `EmailApp` |
-|`{API-VERSION}`     | The version of the API you're calling. | `2022-10-01-preview` |
-|`{MODEL-NAME}`       | The name of your model. This value is case-sensitive. | `v1` |
-
-### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-
-Once you send your API request, you receive a `202` response indicating success. In the response headers, extract the `operation-location` value formatted like this: 
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/jobs/{JOB-ID}?api-version={API-VERSION}
-``` 
-
-`JOB-ID` is used to identify your request, since this operation is asynchronous. Use this URL to get the exported project JSON, using the same authentication method.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルデータのロードとエクスポート手順の削除"
}
```

### Explanation
この変更により、`load-export-model-rest-api.md`というファイルが削除されました。このファイルには、REST APIを使用してモデルデータをロードおよびエクスポートするための詳細な手順が記載されていました。具体的には、APIリクエストの作成方法、必要なリクエストURLとそのプレースホルダの説明、認証ヘッダーの指定、APIリクエストを送信した際のレスポンスの処理方法などが含まれていました。リクエストの成功を示すための`202`レスポンスについても触れられており、非同期処理のための`JOB-ID`の使用方法も説明されていました。この削除によって、ユーザーはモデルデータの管理に関する情報を他のリソースから探し直す必要が生じ、ドキュメントの整理や更新が意図されている可能性があります。

## articles/ai-services/language-service/includes/custom/model-evaluation-language-studio.md{#item-741c45}

<details>
<summary>Diff</summary>
````diff
@@ -1,80 +0,0 @@
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
-3. On this page, you can only view the successfully trained models, F1 score for each model and [model expiration date](../../concepts/model-lifecycle.md). You can select on the model name for more details about its performance.
-
-> [!NOTE]
-> * Entities that aren't labeled or predicted in the test set will not be part of the displayed results.
-
-### [Overview](#tab/overview)
-
-* In this tab you can view the model's details such as: F1 score, precision, recall, date and time for the training job, total training time and number of training and testing documents included in this training job.  
-
-    :::image type="content" source="../../media/custom/overview.png" alt-text="A screenshot that shows the overview page for model evaluation." lightbox="../../media/custom/overview.png":::
-
-* You'll also see guidance on how to improve the model. When you select *view details*,  a side panel will open to give more guidance on how to improve the model. In this example, *BorrowerAddress* and *BorrowerName* entities are confused with *$none* entity. Selecting the confused entities opens the data labeling page to label more data with the correct entity.
-
-    :::image type="content" source="../../media/custom/overview-guidance.png" alt-text="A screenshot that shows the guidance page for model evaluation." lightbox="../../media/custom/overview-guidance.png":::
-    
-### [Entity type performance](#tab/entity-performance)
-
-* This is a snapshot of how your model performed during testing. The metrics here are static and tied to your model, so they won’t update until you train again.
-
-* You can see for each entity, precision, recall, F1 score, number of training and testing labels.
-
-
-    :::image type="content" source="../../media/custom/entity-type-performace.png" alt-text="A screenshot of entity performance." lightbox="../../media/custom/entity-type-performace.png":::
-
-### [Test set details](#tab/test-set)
-
-* Here you can see the documents included in the **test set** and the result entity type for each document. You can use the *Show mismatches only* toggle to show only documents with mismatches, or unselect the toggle to view all document in the test set.
-
-* For each document, you can view: labeled text, its respective labeled entity type and what entity it was predicted with. Also, you can see whether it's a true positive, false positive or false negative. 
-
-    :::image type="content" source="../../media/custom/test-set.png" alt-text="A screenshot of test set details." lightbox="../../media/custom/test-set.png":::
-    
-
-### [Dataset distribution](#tab/dataset-distribution) 
-
-This snapshot shows how entities are distributed across your training and testing sets. This data is static and tied to your model, so it won’t update until you train again.
-
-* You can view the dataset distribution in *graph* or *table* view.
-
-**Graph view**
-
-* *Documents with at least one label*: This view shows for each entity, the number of occurrences for this entity across the training and testing sets.
-
-* *Total instances throughout documents*: This view shows for each entity, the labeled occurrences across training and testing sets.
-
-  :::image type="content" source="../../media/custom/dataset-graph.png" alt-text="A screenshot showing distribution in graph view." lightbox="../../media/custom/dataset-graph.png":::
-
-**Table view**
-
-For each *entity*, you can view: tags per entity in training set, tagged documents in training set, tags per entity in testing set, tagged documents in testing set, tags per entity total and tagged documents total.
-
-  :::image type="content" source="../../media/custom/dataset-table.png" alt-text="A screenshot showing distribution in table view." lightbox="../../media/custom/dataset-table.png":::
-
-### [Confusion matrix](#tab/confusion-matrix) 
-
-A confusion matrix is an N x N matrix used for evaluating the performance of a classification model, where N is the number of target entities. The matrix compares the actual target values with those values predicted by the machine learning model to show how well the extraction model is performing and what kinds of errors it's making.
-
-You can view the confusion matrix in *normalized* or *raw count* view.
-
-  :::image type="content" source="../../media/custom/confusion.png" alt-text="A screenshot of a confusion matrix in Language Studio." lightbox="../../media/custom/confusion.png":::
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
この変更は、`model-evaluation-language-studio.md`というファイルが削除されたことを示しています。このファイルには、Language Studioにおけるモデル評価のための手順や説明が詳述されていました。具体的には、プロジェクトページへの移動方法、モデルのパフォーマンスの確認、F1スコア、エンティティタイプのパフォーマンス、テストセットの詳細、データセットの分布、混同行列の表示方法などが含まれていました。また、ユーザーがモデルの改善方法を見つけられるようなガイダンスも提供されていました。この削除により、ユーザーはモデル評価に関する重要な情報を他のドキュメントから探さなければならなくなり、ドキュメントの整理や更新が意図されている可能性があります。

## articles/ai-services/language-service/includes/custom/project-details.md{#item-3a6d16}

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
    "modification_title": "プロジェクト詳細情報の手順の削除"
}
```

### Explanation
この変更により、`project-details.md`というファイルが削除されました。このファイルには、Language Studioでのプロジェクト設定に関する手順が記載されていました。具体的には、プロジェクト設定ページへの移動方法、プロジェクトの詳細情報の確認、プロジェクトの説明の更新、マルチリンガルデータセットの有効化または無効化の手順、接続されたストレージアカウントおよびコンテナの表示、主要リソースキーの取得方法などが含まれていました。この情報の削除により、ユーザーはプロジェクト設定に関する重要な情報を別の場所から探す必要が生じ、ドキュメントの整合性や最新情報を維持するための変更が行われた可能性があります。

## articles/ai-services/language-service/includes/custom/resource-creation-language-studio.md{#item-bd3ca8}

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
-|Location | The region      |
-|Pricing tier     | The pricing tier of your Language resource.        |
-
-> [!IMPORTANT]
-> * Make sure to enable **Managed Identity** when you create a Language resource. 
-> * Read and confirm Responsible AI notice
-
-To use this service, you'll need to [create an Azure storage account](/azure/storage/common/storage-account-create) if you don't have one already. 
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
この変更により、`resource-creation-language-studio.md`というファイルが削除されました。このファイルには、Language Studioを使用して新しい言語リソースを作成するための手順が詳しく記載されていました。具体的には、初回ログイン時に表示されるウィンドウで既存のリソースを選択する方法、新規リソース作成を行うためのメニュー経路、リソース作成に必要な詳細（Azureサブスクリプション、リソースグループ、リソース名、地域、価格階層など）が含まれていました。さらに、リソース作成時には「Managed Identity」の有効化やResponsible AIに関する確認が必要であることも強調されていました。この情報の削除により、ユーザーはリソース作成の手順を他の場所で探さなければならず、関連ドキュメントの整合性への影響が考えられます。

## articles/ai-services/language-service/includes/custom/roles-for-resource-and-storage.md{#item-d4eac6}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 11/18/2025
+ms.date: 02/23/2026
 ms.author: lajanuar
 ---
 Use the following steps to set the required roles for your Language resource and storage account.
@@ -19,7 +19,7 @@ Use the following steps to set the required roles for your Language resource and
 2. Select **Access Control (IAM)** in the left pane.
 3. Select **Add** to **Add Role Assignments**, and choose the appropriate role for your account.
 
-    You should have the **owner** or **contributor** role assigned on your Language resource.
+    * You should have the **owner** or **contributor** role assigned on your Language resource.
 
 4. Within **Assign access to**, select **User, group, or service principal**
 5. Select **Select members**
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "役割設定手順の更新"
}
```

### Explanation
この変更では、`roles-for-resource-and-storage.md`というファイルが修正され、以下の2点が更新されました。まず、ドキュメントの日付が「2025年11月18日」から「2026年2月23日」に変更されました。次に、ユーザーが言語リソースに対して「owner」または「contributor」役割が割り当てられる必要がある旨の説明が、リスト形式に整形され強調されました。これにより、手順がより明確になり、ユーザーが役割の設定に関する情報を理解しやすくすることが意図されています。転記された手順そのものは変わっておらず、主に視覚的な改善が行われていると言えます。

## articles/ai-services/language-service/includes/custom/use-pre-existing-resource.md{#item-a883ba}

<details>
<summary>Diff</summary>
````diff
@@ -5,46 +5,34 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 11/18/2025
+ms.date: 02/23/2026
 ms.author: lajanuar
 ---
-|Requirement  |Description  |
-|---------|---------|
-|Regions     |  If you don't have a resource, you need to create a new one in a supported region.        |
-|Pricing tier     | pricing tier for your resource.       |
-|Managed identity     | Make sure that the resource's managed identity setting is enabled. Otherwise, read the next section. |
+| Requirement | Description |
+| --- | --- |
+| Regions | If you don't have a resource, you need to create a new one in a supported region. |
+| Pricing tier | pricing tier for your resource. |
+| Managed identity | Make sure that the resource's managed identity setting is enabled. Otherwise, read the next section. |
 
-To use this service, you'll need to [create an Azure storage account](/azure/storage/common/storage-account-create) if you don't have one already. 
+To use this service, you'll need to [create an Azure storage account](/azure/storage/common/storage-account-create) if you don't have one already.
 
-## Enable identity management for your resource
-
-# [Azure portal](#tab/azure-portal)
+## Enable identity management using Azure portal
 
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
 
 ### Enable the custom feature for your resource
 
 Make sure to enable this service's custom feature from Azure portal.
 
 1. Go to your Language resource in [Azure portal](https://portal.azure.com/)
-2. From the left side menu, under **Resource Management** section, select **Features**
-3. Enable this service's custom feature
-4. Connect your storage account
-5. Select **Apply**
+1. From the left side menu, under **Resource Management** section, select **Features**
+1. Enable this service's custom feature
+1. Connect your storage account
+1. Select **Apply**
 
 > [!IMPORTANT]
 > Make sure that your **Language resource** has **storage blob data contributor** role assigned on the storage account you're connecting.
@@ -55,7 +43,7 @@ Make sure to enable this service's custom feature from Azure portal.
 
 ### Enable CORS for your storage account
 
-Make sure to allow (**GET, PUT, DELETE**) methods when enabling Cross-Origin Resource Sharing (CORS). 
+Make sure to allow (**GET, PUT, DELETE**) methods when enabling Cross-Origin Resource Sharing (CORS).
 Set allowed origins field to `https://language.cognitive.azure.com`. Allow all header by adding `*` to the allowed header values, and set the maximum age to `500`.
 
 :::image type="content" source="../../custom-named-entity-recognition/media/cors.png" alt-text="A screenshot showing how to use CORS for storage accounts." lightbox="../../custom-named-entity-recognition/media/cors.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "既存のリソース使用手順の更新"
}
```

### Explanation
この変更では、`use-pre-existing-resource.md`ファイルが修正され、いくつかの内容が更新されました。まず、ドキュメントの日付が「2025年11月18日」から「2026年2月23日」に変更されています。また、いくつかのセクションがフォーマットされ、特に「Requirements」と「Enable identity management」の項目が視覚的に整理されています。

具体的には、表が適切に書式設定され、項目の説明が読みやすくなりました。そして、アイデンティティ管理を有効にする手順も整理され、番号が統一されて明確化されています。他に、CORS設定についての指示は維持されており、必要なHTTPメソッドや設定値が具体的に記載されています。このように、手順と指示がより明確に表現されるよう整えられたことで、読者が手順を理解しやすくなることを意図しています。

## articles/ai-services/language-service/includes/key-endpoint-page-azure-portal.md{#item-fec9be}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Go to your resource overview page in the [Azure portal](https://portal.azure.com/#home)
-
-2. From the menu on the left side, select **Keys and Endpoint**. You use the endpoint and key for the API requests 
-
-    :::image type="content" source="../media/key-endpoint-page.png" alt-text="A screenshot showing the key and endpoint page in the Azure portal." lightbox="../media/key-endpoint-page.png":::
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azureポータルのキーとエンドポイントに関するページの削除"
}
```

### Explanation
この変更では、`key-endpoint-page-azure-portal.md`ファイルが完全に削除されました。このファイルには、Azureポータルでのリソースの概要ページにアクセスし、「Keys and Endpoint」セクションを選択する手順が記載されていました。また、APIリクエストに必要なキーとエンドポイントを示すスクリーンショットも含まれていました。

この削除により、ユーザーはこの特定の手順にアクセスできなくなりますので、関連する他のドキュメントやリソースで情報を確認する必要があります。作業フローや参照ガイドに大きな影響を与える可能性があるため、変更は「breaking change」として扱われます。これは、キーやエンドポイントの取得方法を知りたいユーザーにとって不便さをもたらすためです。

## articles/ai-services/language-service/includes/sdk-target-versions.md{#item-59b6f8}

<details>
<summary>Diff</summary>
````diff
@@ -1,19 +0,0 @@
----
- title: include file
- description: include file
- #services: cognitive-services
- author: laujan
- ms.service: azure-ai-language
- ms.topic: include
- ms.date: 11/05/2025
- ms.author: lajanuar
- ms.custom: include
----
-This table shows the relationship between SDK versions and supported API versions of the service:
-
-|SDK version  |Supported API version of service  |
-|---------|---------|
-|5.2-beta.x     | 3.0, 3.1, 3.2-preview.x (default)       |
-|5.1.X     | 3.0, 3.1 (default)       |
-|5.0.0    | 3.0       |
-|1.0.X    | 3.0      |
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "SDKターゲットバージョン情報の削除"
}
```

### Explanation
この変更では、`sdk-target-versions.md`ファイルが完全に削除されました。このファイルには、SDKバージョンとサービスのサポートされるAPIバージョンとの関係を示すテーブルが含まれており、具体的にはSDKのバージョンに対するAPIバージョンの対応が記載されていました。これにより、ユーザーは特定のSDKバージョンがどのAPIバージョンに対応しているかを簡単に確認できました。

この削除は、ユーザーにとって重要な情報源が失われることを意味し、特にSDKとの互換性を考慮する際に混乱を引き起こす可能性があります。したがって、この変更は「breaking change」として扱われ、従来のドキュメントを参照していたユーザーにとっては不便さをもたらします。判断材料として、ユーザーは他のリソースやドキュメントから情報を探る必要があるため、影響が大きい改訂となります。

## articles/ai-services/language-service/question-answering/concepts/best-practices.md{#item-f97daf}

<details>
<summary>Diff</summary>
````diff
@@ -102,11 +102,11 @@ Chit-chat is supported for several predefined personalities:
 
 |Personality |Custom question answering dataset file |
 |---------|-----|
-|Professional |[qna_chitchat_professional.tsv](https://qnamakerstore.blob.core.windows.net/qnamakerdata/editorial/qna_chitchat_professional.tsv) |
-|Friendly |[qna_chitchat_friendly.tsv](https://qnamakerstore.blob.core.windows.net/qnamakerdata/editorial/qna_chitchat_friendly.tsv) |
-|Witty |[qna_chitchat_witty.tsv](https://qnamakerstore.blob.core.windows.net/qnamakerdata/editorial/qna_chitchat_witty.tsv) |
-|Caring |[qna_chitchat_caring.tsv](https://qnamakerstore.blob.core.windows.net/qnamakerdata/editorial/qna_chitchat_caring.tsv) |
-|Enthusiastic |[qna_chitchat_enthusiastic.tsv](https://qnamakerstore.blob.core.windows.net/qnamakerdata/editorial/qna_chitchat_enthusiastic.tsv) |
+|Professional | qna_chitchat_professional.tsv |
+|Friendly | qna_chitchat_friendly.tsv |
+|Witty | qna_chitchat_witty.tsv |
+|Caring | qna_chitchat_caring.tsv |
+|Enthusiastic | qna_chitchat_enthusiastic.tsv |
 
 The responses range from formal to informal and irreverent. You should select the personality that is closest aligned with the tone you want for your bot. You can view the datasets, and choose one that serves as a base for your bot, and then customize the responses.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベストプラクティスにおけるチャットパーソナリティ情報の改善"
}
```

### Explanation
この変更では、`best-practices.md`ファイルの内容が更新され、チャットボットのパーソナリティに関する情報が改善されました。具体的には、5つの異なるパーソナリティ（Professional、Friendly、Witty、Caring、Enthusiastic）のそれぞれに対するカスタム質問応答データセットのファイル名が、リンク形式からプレーンテキストの形式に変更されました。

この更新は、情報の明瞭性を高め、ユーザーが必要なデータセットを簡単に識別できるようにすることを目的としています。具体的なファイル名が直接表示されることにより、ユーザーはリソースへのアクセスをより容易にし、適切なデータセットを選択する際の手間を軽減できます。この変更はあくまで「minor update」として位置づけられ、ユーザー体験の改善に寄与するものです。

## articles/ai-services/language-service/question-answering/reference/document-format-guidelines.md{#item-fb0489}

<details>
<summary>Diff</summary>
````diff
@@ -43,7 +43,7 @@ To follow is an example of a manual with an index page, and hierarchical content
 
 ### Brochures, guidelines, papers, and other files
 
-Many other types of documents can also be processed to generate question answer pairs, provided they have a clear structure and layout. These documents include: Brochures, guidelines, reports, white papers, scientific papers, policies, books, etc. See an example [here](https://qnamakerstore.blob.core.windows.net/qnamakerdata/docs/Manage%20Azure%20Blob%20Storage.docx).
+Many other types of documents can also be processed to generate question answer pairs, provided they have a clear structure and layout. These documents include: Brochures, guidelines, reports, white papers, scientific papers, policies, books, etc.
 
 To follow is an example of a semi-structured doc, without an index:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書形式ガイドラインの例文修正"
}
```

### Explanation
この変更では、`document-format-guidelines.md`ファイルの内容が修正され、文書形式に関する説明の一部が簡略化されました。具体的には、さまざまな種類の文書が質問応答ペアを生成するために処理できることを述べる文が更新され、具体的な例として挙げられていたリンク（Azure Blob Storageに関する文書へのリンク）が削除されました。

この変更は、文書の説明をより簡潔にすることを目的としており、特定の外部リソースへの依存を減らすことで、読み手がガイドラインを理解する際の障害を取り除いています。リンクの削除により、情報が一貫して保持されるため、ユーザーは他のリソースを探す手間を省くことができ、全体的な内容の明瞭性が向上します。この修正は「minor update」として位置づけられ、文書の使いやすさを向上させる効果があります。

## articles/ai-services/language-service/tutorials/use-kubernetes-service.md{#item-986931}

<details>
<summary>Diff</summary>
````diff
@@ -10,6 +10,7 @@ ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: cogserv-non-critical-language
 ---
+
 # Deploy a key phrase extraction container to Azure Kubernetes Service
 
 Learn how to deploy a [key phrase extraction Docker container](../key-phrase-extraction/how-to/use-containers.md) image to Azure Kubernetes Service (AKS). This procedure shows how to create a Language resource, how to associate a container image, and how to exercise this orchestration of the two from a browser. Using containers can shift your attention away from managing infrastructure to instead focusing on application development. While this article uses the key phrase extraction container as an example, you can use this process for other containers offered by Azure Language in Foundry Tools
@@ -23,13 +24,33 @@ This procedure requires several tools that must be installed and run locally. Do
 * The [Azure CLI](/cli/azure/install-azure-cli) installed.
 * The [Kubernetes CLI](https://kubernetes.io/docs/tasks/tools/install-kubectl/) installed.
 * An Azure resource with the correct pricing tier. Not all pricing tiers work with this container:
-    * **Language** resource with F0 or standard pricing tiers only.
-    * **Foundry Tools** resource with the S0 pricing tier.
+  * **Language** resource with F0 or standard pricing tiers only.
+  * **Foundry Tools** resource with the S0 pricing tier.
 
-[!INCLUDE [Create a Language resource](../includes/containers/create-text-analytics-resource.md)]
+## Create an Azure Language in Foundry Tools resource
 
-[!INCLUDE [Create a language container on Azure Kubernetes Service (AKS)](../../containers/includes/create-aks-resource.md)]
+1. Sign in to the [Azure portal](https://portal.azure.com).
+1. Select **Create a resource**, and then go to **AI + Machine Learning** > **Language**.
+   Or, go to [Create a Language resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics).
+1. Enter all the required settings:
+
+    |Setting|Value|
+    |--|--|
+    |Name|Enter a name (2-64 characters).|
+    |Subscription|Select the appropriate subscription.|
+    |Location|Select a nearby location.|
+    |Pricing tier| Enter **S**, the standard pricing tier.|
+    |Resource group|Select an available resource group.|
 
+1. Select **Create**, and wait for the resource to be created. Your browser automatically redirects to the newly created resource page.
+1. Collect the configured `endpoint` and an API key:
+
+    |Resource tab in portal|Setting|Value|
+    |--|--|--|
+    |**Overview**|Endpoint|Copy the endpoint. It appears similar to `https://my-resource.cognitiveservices.azure.com/text/analytics/v3.0`.|
+    |**Keys**|API Key|Copy one of the two keys. It's a 32-character alphanumeric string with no spaces or dashes: <`xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`>.|
+
+[!INCLUDE [Create a language container on Azure Kubernetes Service (AKS)](../../containers/includes/create-aks-resource.md)]
 
 ## Deploy the Key Phrase Extraction container to an AKS cluster
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Kubernetesサービスへのキー フレーズ抽出コンテナのデプロイ手順の更新"
}
```

### Explanation
この変更は、`use-kubernetes-service.md`ファイルにおける手順の更新を反映しています。新たに「Azure Kubernetes Serviceにキー フレーズ抽出コンテナをデプロイする」セクションが追加され、コンテナのデプロイに関する具体的な手順や詳細が強化されました。

追加された内容には、Azureポータルにサインインし、リソースを作成する手順が含まれており、リソースの設定に関するテーブルも追加されています。これにより、ユーザーは必要な設定項目（名前、サブスクリプション、ロケーション、価格帯、リソースグループなど）を理解しやすくなっています。

この更新は、手順のわかりやすさを向上させ、ユーザーがAzureサービスを利用してコンテナをデプロイする際の体験を改善することを目的としています。また、いくつかのインクルードコマンドの順序も見直され、全体的な流れがスムーズになりました。全体として、この修正は「minor update」として位置づけられ、ドキュメントの実用性を高めています。


