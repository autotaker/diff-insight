---
date: '2025-01-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7840f69...MicrosoftDocs:058aad5
summary: 今回の差分では、ドキュメントインテリジェンス、マネージドネットワーク、モデルカタログに関する3つのドキュメントが軽微に更新されました。主な変更点は、カスタム抽出モデルの種類の削減と整理、WebSocketサーバー取得のためのリポジトリURLのアップデート、およびサーバーレスAPIエンドポイントに関する記述の修正です。新機能は追加されていませんが、情報の鮮度が高まり、古い情報との整合性に注意が必要です。これらの変更により、AzureのAIサービスに関するドキュメントはよりアクセスしやすくなり、ユーザーが効率的に利用できるよう支援しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7840f69...MicrosoftDocs:058aad5){target="_blank"}

# ハイライト
今回の差分では、ドキュメントインテリジェンス、マネージドネットワーク、モデルカタログに関する3つのドキュメントがそれぞれ軽微に更新されました。主な変更点として、カスタム抽出モデルのタイプの削減と整理、WebSocketサーバー取得用のリポジトリURLのアップデート、サーバーレスAPIのエンドポイントに関する記述の修正があります。

## 新機能
今回の変更において、新機能の追加はありませんでしたが、情報の鮮度が高まるように内容が更新されています。

## 破壊的変更
破壊的変更は特にありませんが、ドキュメントの情報元が改変されているため、古い情報との整合性に注意が必要です。

## その他の更新
- カスタム抽出モデルの種類に関する説明の簡略化と正確化。
- Visual Studio Code用AIツールのWebSocketサーバーリポジトリURLの最適化。
- モデルカタログ概要におけるサーバーレスAPIエンドポイント関連情報の明確化と一貫性の向上。

# 洞察
これらの変更は、AzureのAI関連ドキュメントの情報を最新の状態に保つためのものであり、エンドユーザーがサービスをより効率的に利用する手助けを狙っています。特にドキュメントインテリジェンスの記事では、カスタム抽出モデルの記述が簡素化されることで、利用者が混乱することなく適切な選択をできるようになっています。同様に、WebSocketサーバーのリポジトリURLの更新は、Visual Studio Codeクライアントとサーバの接続の信頼性を向上させるものです。また、モデルカタログにおけるサーバーレスAPIエンドポイントの変更は、ネットワーク設定と利用に関する視点をはっきりさせ、利用者が自身の要件に即した選択を適確に行う一助となるでしょう。これにより、AzureのAIサービスのドキュメントは、利用者にとってよりアクセスしやすく実用的なものとなっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-overview.md](#item-768c0d) | minor update | カスタム抽出モデルのタイプの更新 | modified | 1 | 1 | 2 | 
| [configure-managed-network.md](#item-dc9c50) | minor update | WebSocketサーバーのリポジトリURLの更新 | modified | 1 | 1 | 2 | 
| [model-catalog-overview.md](#item-278001) | minor update | サーバーレスAPIのエンドポイントに関する変更 | modified | 4 | 4 | 8 | 


# Modified Contents
## articles/ai-services/document-intelligence/model-overview.md{#item-768c0d}

<details>
<summary>Diff</summary>
````diff
@@ -373,7 +373,7 @@ Version v3.0 and later custom models support signature detection in custom templ
 
 :::image type="icon" source="media/studio/custom-extraction.png":::
 
-Custom extraction model can be one of three types, **custom template**, **custom neural**. To create a custom extraction model, label a dataset of documents with the values you want extracted and train the model on the labeled dataset. You only need five examples of the same form or document type to get started.
+Custom extraction model can be one of two types, **custom template**, **custom neural**. To create a custom extraction model, label a dataset of documents with the values you want extracted and train the model on the labeled dataset. You only need five examples of the same form or document type to get started.
 
 ***Sample custom extraction processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/customform/projects)***:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム抽出モデルのタイプの更新"
}
```

### Explanation
このコードの差分は、ドキュメントインテリジェンスに関する記事のカスタム抽出モデルの説明における軽微な更新を示しています。変更された内容は、カスタム抽出モデルのタイプが三種類から二種類に減ったことを反映しています。具体的には、以前は「カスタムテンプレート」、「カスタムニューラル」の他にもう一つのモデルタイプが存在していましたが、現在はこの二種類のみとなっています。この修正は、カスタム抽出モデルの作成方法に関する記述を簡素化し、より正確な情報提供を目的としています。

## articles/ai-studio/how-to/configure-managed-network.md{#item-dc9c50}

<details>
<summary>Diff</summary>
````diff
@@ -786,7 +786,7 @@ The hosts in this section are used to install Visual Studio Code packages to est
 | `code.visualstudio.com` | Required to download and install VS Code desktop. This host isn't required for VS Code Web. |
 | `update.code.visualstudio.com`<br>`*.vo.msecnd.net` | Used to retrieve VS Code server bits that are installed on the compute instance through a setup script. |
 | `marketplace.visualstudio.com`<br>`vscode.blob.core.windows.net`<br>`*.gallerycdn.vsassets.io` | Required to download and install VS Code extensions. These hosts enable the remote connection to compute instances. For more information, see [Get started with Azure AI Foundry projects in VS Code](./develop/vscode.md). |
-| `https://github.com/microsoft/vscode-tools-for-ai/tree/master/azureml_remote_websocket_server/*` | Used to retrieve websocket server bits that are installed on the compute instance. The websocket server is used to transmit requests from Visual Studio Code client (desktop application) to Visual Studio Code server running on the compute instance. |
+| `https://github.com/microsoft/vscode-tools-for-ai/tree/master/azureml_remote_websocket_server/*`<br>`raw.githubusercontent.com` | Used to retrieve websocket server bits that are installed on the compute instance. The websocket server is used to transmit requests from Visual Studio Code client (desktop application) to Visual Studio Code server running on the compute instance. |
 | `vscode.download.prss.microsoft.com` | Used for Visual Studio Code download CDN |
 
 #### Ports
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "WebSocketサーバーのリポジトリURLの更新"
}
```

### Explanation
このコードの差分は、マネージドネットワークの設定に関するドキュメントにおいて、WebSocketサーバーを取得するためのリポジトリのURLに関する軽微な更新を示しています。具体的には、元の記述では「`https://github.com/microsoft/vscode-tools-for-ai/tree/master/azureml_remote_websocket_server/*`」というURLが示されていましたが、変更後は「`raw.githubusercontent.com`」が追加され、より適切にリソースを取得できるようになっています。この修正により、Visual Studio Codeクライアントとサーバー間の接続が円滑になることが期待されます。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -165,7 +165,7 @@ Pay-per-token billing is available only to users whose Azure subscription belong
 
 ### Network isolation for models deployed via serverless APIs
 
-Managed computes for models deployed as serverless APIs follow the public network access flag setting of the Azure AI Foundry hub that has the project in which the deployment exists. To help secure your managed compute, disable the public network access flag on your Azure AI Foundry hub. You can help secure inbound communication from a client to your managed compute by using a private endpoint for the hub.
+Endpoints for models deployed as serverless APIs follow the public network access flag setting of the Azure AI Foundry hub that has the project in which the deployment exists. To help secure your serverless API endpoint, disable the public network access flag on your Azure AI Foundry hub. You can help secure inbound communication from a client to your endpoint by using a private endpoint for the hub.
 
 To set the public network access flag for the Azure AI Foundry hub:
 
@@ -177,11 +177,11 @@ To set the public network access flag for the Azure AI Foundry hub:
 
 #### Limitations
 
-* If you have an Azure AI Foundry hub with a managed compute created before July 11, 2024, managed computes added to projects in this hub won't follow the networking configuration of the hub. Instead, you need to create a new managed compute for the hub and create new serverless API deployments in the project so that the new deployments can follow the hub's networking configuration.
+* If you have an Azure AI Foundry hub with a private endpoint created before July 11, 2024, serverless API endpoints added to projects in this hub won't follow the networking configuration of the hub. Instead, you need to create a new private endpoint for the hub and create new serverless API deployments in the project so that the new deployments can follow the hub's networking configuration.
 
-* If you have an Azure AI Foundry hub with MaaS deployments created before July 11, 2024, and you enable a managed compute on this hub, the existing MaaS deployments won't follow the hub's networking configuration. For serverless API deployments in the hub to follow the hub's networking configuration, you need to create the deployments again.
+* If you have an Azure AI Foundry hub with MaaS deployments created before July 11, 2024, and you enable a private endpoint on this hub, the existing serverless API deployments won't follow the hub's networking configuration. For serverless API deployments in the hub to follow the hub's networking configuration, you need to create the deployments again.
 
-* Currently, [Azure OpenAI On Your Data](/azure/ai-services/openai/concepts/use-your-data) support isn't available for MaaS deployments in private hubs, because private hubs have the public network access flag disabled.
+* Currently, [Azure OpenAI On Your Data](/azure/ai-services/openai/concepts/use-your-data) support isn't available for serverless API deployments in private hubs, because private hubs have the public network access flag disabled.
 
 * Any network configuration change (for example, enabling or disabling the public network access flag) might take up to five minutes to propagate.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスAPIのエンドポイントに関する変更"
}
```

### Explanation
このコードの差分は、モデルカタログの概要に関するドキュメントにおいて、サーバーレスAPIのエンドポイントに関する表現を軽微に更新したことを示しています。具体的には、「Managed computes」の部分が「Endpoints」に変更され、管理されたコンピュートに関連する言及がサーバーレスAPIエンドポイントに焦点を当てたものとなっています。また、プライベートエンドポイントや公のネットワークアクセスフラグに関する説明も修正され、情報がより明確かつ一貫性のあるものになっています。これにより、利用者はサーバーレスAPIがAzure AI Foundryハブの設定にどのように依存するかを理解しやすくなります。


