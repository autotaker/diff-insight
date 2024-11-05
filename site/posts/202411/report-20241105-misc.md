---
date: '2024-11-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8de853c...MicrosoftDocs:c2df9dc
summary: このドキュメントの更新では、Azure AIリソースの作成と利用に関する情報が強化され、ユーザーエクスペリエンスが向上しました。具体的には、新しい画像が追加され、SDK評価の構成が改善され、CLIの新しいログイン方法が導入されるなどの新機能があります。また、リソース作成後に資格情報の保管方法が変更できないことが明確化される破壊的変更も含まれています。この更新は、特に新しいユーザーや開発者にとって、手順の理解と実装を容易にし、Azureのストレージ資格情報の管理に関する重要な情報を提供します。全体として、ユーザーの理解度と効率の向上が期待されます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8de853c...MicrosoftDocs:c2df9dc){target="_blank"}

# ハイライト
このドキュメントの更新では、新機能と改善が行われ、ユーザーがAzure AIリソースを作成し利用する際に役立つ情報が提供されるようになりました。AzureリソースやSDK、CLIに関する手順の詳細が強化され、新しい画像が追加されるなど、ユーザーエクスペリエンスを向上させるための変更が加えられています。これには、ストレージ資格情報の管理、SDKの評価方法の明確化、CLIの柔軟なログインオプションが含まれます。

## 新機能
- Azure AIリソースに関する新しい画像の追加による視覚的説明の強化。
- SDK評価の際の「column_mapping」構成の改善。
- CLI用のデバイスコードを用いた新しいログイン方法の導入。

## 破壊的変更
- リソース作成後に資格情報の保管方法を変更できない点の明確化。

## その他の更新
- Azure AIモデル推論サービスに関するLlama Indexドキュメントの更新。
- Qualificationsの保管方法の選択肢の詳細な説明とその重要性の強調。

# インサイト
今回の更新は、多岐にわたるAzure AI関連のドキュメントに対するユーザビリティの向上を目的としており、特に新しいユーザーや開発者にとって、手順の理解と実装を容易にしています。具体的には、Azureのストレージ資格情報の管理方法と、その選択が後に変更できない点を利用者に明確に伝えることが重要です。これは、セキュリティと運用の両面で適切な選択を促すものであり、ユーザーが事前に慎重に決定を下すべきポイントです。

また、SDK評価において「column_mapping」を視覚的に整理したことにより、データの関連性をより直感的に把握でき、設定のミスを減らすことが期待されます。CLIに関しては、環境やセキュリティ状況に応じた柔軟なログイン方法を提供することで、ユーザーが直面する様々なシナリオに対応可能となりました。

加えて、新しい画像がドキュメントに追加されたことで、特定の操作手順が視覚的に説明され、特に視覚的な情報を好むユーザーに対する利便性が向上しました。これらの改良により、Azure AIリソースやサービスの利用において、ユーザーの理解度と効率が大きく向上することが見込まれます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [create-azure-ai-resource.md](#item-998abe) | minor update | Azure AIリソースの作成方法に関する更新 | modified | 18 | 10 | 28 | 
| [evaluate-sdk.md](#item-9d5197) | minor update | SDK評価に関するドキュメントの更新 | modified | 4 | 4 | 8 | 
| [llama-index.md](#item-613372) | minor update | Llama Indexに関するドキュメントの更新 | modified | 26 | 9 | 35 | 
| [install-cli.md](#item-868060) | minor update | Azure CLIのインストール手順の更新 | modified | 5 | 0 | 5 | 
| [resource-create-resources.png](#item-a5c0ba) | new feature | リソース作成に関する新しい画像の追加 | added | 0 | 0 | 0 | 
| [studio-delete-hub.png](#item-9efef7) | new feature | ハブ削除に関する新しい画像の追加 | added | 0 | 0 | 0 | 


# Modified Contents
## articles/ai-studio/how-to/create-azure-ai-resource.md{#item-998abe}

<details>
<summary>Diff</summary>
````diff
@@ -40,9 +40,9 @@ If your organization is using [Azure Policy](/azure/governance/policy/overview),
     
     :::image type="content" source="~/reusable-content/ce-skilling/azure/media/ai-studio/resource-create-basics.png" alt-text="Screenshot of the option to set hub basic information." lightbox="~/reusable-content/ce-skilling/azure/media/ai-studio/resource-create-basics.png":::
 
-1. Select the **Storage** tab to specify storage account settings.
+1. Select the **Storage** tab to specify storage account settings. For storing credentials, either provide your Azure Key Vault or use the [Microsoft-managed credential store (preview)](#choose-how-credentials-are-stored).
 
-    :::image type="content" source="~/reusable-content/ce-skilling/azure/media/ai-studio/resource-create-resources.png" alt-text="Screenshot of the Create a hub with the option to set storage resource information." lightbox="~/reusable-content/ce-skilling/azure/media/ai-studio/resource-create-resources.png"::: 
+    :::image type="content" source="../media/how-to/hubs/resource-create-resources.png" alt-text="Screenshot of the Create a hub with the option to set storage resource information." lightbox="../media/how-to/hubs/resource-create-resources.png"::: 
 
 1. Select the **Networking** tab to set up Network isolation. Read more on [network isolation](configure-managed-network.md). For a walkthrough of creating a secure hub, see [Create a secure hub](create-secure-ai-hub.md).
 
@@ -90,7 +90,7 @@ Hub networking settings can be set during resource creation or changed in the **
 
 At hub creation, select between the networking isolation modes: **Public**, **Private with Internet Outbound**, and **Private with Approved Outbound**. To secure your resource, select either **Private with Internet Outbound** or **Private with Approved Outbound** for your networking needs. For the private isolation modes, a private endpoint should be created for inbound access. For more information on network isolation, see [Managed virtual network isolation](configure-managed-network.md). To create a secure hub, see [Create a secure hub](create-secure-ai-hub.md). 
 
-At hub creation in the Azure portal, creation of associated Azure AI services, Storage account, Key vault, Application insights, and Container registry is given. These resources are found on the Resources tab during creation. 
+At hub creation in the Azure portal, creation of associated Azure AI services, Storage account, Key vault (optional), Application insights (optional), and Container registry (optional) is given. These resources are found on the Resources tab during creation. 
 
 To connect to Azure AI services (Azure OpenAI, Azure AI Search, and Azure AI Content Safety) or storage accounts in Azure AI Studio, create a private endpoint in your virtual network. Ensure the public network access (PNA) flag is disabled when creating the private endpoint connection. For more about Azure AI services connections, follow documentation [here](../../ai-services/cognitive-services-virtual-networks.md). You can optionally bring your own (BYO) search, but this requires a private endpoint connection from your virtual network.
 
@@ -143,20 +143,28 @@ az ml workspace update -n "myexamplehub" -g "{MY_RESOURCE_GROUP}" -a "APPLICATIO
 ```
 ---
 
-## Delete an Azure AI Studio hub
+### Choose how credentials are stored
+
+Select scenarios in AI Studio store credentials on your behalf. For example when you create a connection in AI Studio to access an Azure Storage account with stored account key, access Azure Container Registry with admin password, or when you create a compute instance with enabled SSH keys. No credentials are stored with connections when you choose EntraID identity-based authentication.
 
-To delete a hub, use the [Azure portal](https://portal.azure.com). To quickly get to the Azure portal from the Azure AI Studio, go to the **Hub overview** for your hub and then select **Manage in Azure portal**.
+You can choose where credentials are stored:
 
-:::image type="content" source="../media/how-to/hubs/manage-hub-azure-portal.png" alt-text="Screenshot of the manage in Azure portal link in Azure AI Studio.":::
+1. **Your Azure Key Vault**: This requires you to manage your own Azure Key Vault instance and configure it per hub. It gives you additional control over secret lifecycle e.g. to set expiry policies. You can also share stored secrets with other applications in Azure.
+   
+1. **Microsoft-managed credential store (preview)**: In this variant Microsoft manages an Azure Key Vault instance on your behalf per hub. No resource management is needed on your side and the vault does not show in your Azure subscription. Secret data lifecycle follows the resource lifecycle of your hubs and projects. For example, when a project's storage connection is deleted, its stored secret is deleted as well.
 
-From the portal page for your hub, select **Overview** along the left side of the page and then select **Delete** from the top of the page.
+After your hub is created, it is not possible to switch between Your Azure Key Vault and using a Microsoft-managed credential store.
+
+## Delete an Azure AI Studio hub
 
-:::image type="content" source="../media/how-to/hubs/delete-hub-button.png" alt-text="Screenshot of the delete button for the Azure AI Studio hub in the Azure portal.":::
+To delete a hub from Azure AI Studio, select the hub and then select **Delete hub** from the **Hub properties** section of the page.
 
-You can also find your hub in the Azure portal by entering the hub name in the search field at the top of the Azure portal. Select the hub from the **Resources** list to navigate to the **Overview** page for the hub.
+:::image type="content" source="../media/how-to/hubs/studio-delete-hub.png" alt-text="Screenshot of the delete hub link in hub properties." lightbox="../media/how-to/hubs/studio-delete-hub.png":::
 
-:::image type="content" source="../media/how-to/hubs/search-in-portal.png" alt-text="Screenshot of using the search field in the Azure portal to find a hub.":::
+> [!NOTE]
+> You can also delete the hub from the Azure portal.
 
+Deleting a hub deletes all associated projects. When a project is deleted, all nested endpoints for the project are also deleted. You can optionally delete connected resources; however, make sure that no other applications are using this connection. For example, another Azure AI Studio deployment might be using it.
 
 
 ## Related content
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AIリソースの作成方法に関する更新"
}
```

### Explanation
この更新では、Azure AIリソースの作成に関するドキュメントが修正され、いくつかの情報が追加されました。具体的には、ストレージアカウントの資格情報の管理方法に関する詳細が追加され、AzureのKey Vault利用の選択肢について言及されています。また、リソース作成時に関連付けられるAzure AIサービスやオプションのリソース（Key Vault、Application Insights、Container Registry）の説明も強化されました。

具体的には、以下のポイントが新たに盛り込まれています。
- 資格情報を保管する方法として、ユーザーのAzure Key Vaultを利用するか、Microsoftによって管理される資格情報ストアを選択できることを明確にしました。
- リソース作成後に資格情報の保管方法を変更できない旨を説明し、選択が重要であることが強調されました。
- Hubを削除した際の影響について明確にし、関連するすべてのプロジェクトや接続されたリソースがどのように影響を受けるかを示しました。

この変更により、ユーザーはAzure AIリソースの作成時に必要な情報や手順をより理解しやすくなっています。

## articles/ai-studio/how-to/develop/evaluate-sdk.md{#item-9d5197}

<details>
<summary>Diff</summary>
````diff
@@ -432,8 +432,8 @@ result = evaluate(
     },
     # column mapping
     evaluator_config={
-        "column_mapping": {
-            "relevance": {
+        "relevance": {
+            "column_mapping": {
                 "query": "${data.queries}"
                 "ground_truth": "${data.ground_truth}"
                 "response": "${outputs.response}"
@@ -560,8 +560,8 @@ result = evaluate(
         "relevance": relevance_eval
     },
     evaluator_config={
-        "column_mapping": {
-            "default": {
+        "default": {
+            "column_mapping": {
                 "query": "${data.queries}"
                 "context": "${outputs.context}"
                 "response": "${outputs.response}"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SDK評価に関するドキュメントの更新"
}
```

### Explanation
この修正では、SDKの評価に関するドキュメントが更新され、評価設定の構成が明確化されました。具体的には、評価関数の設定において「column_mapping」構造が改善され、読みやすさが向上しました。

主な変更点は以下の通りです：
- 「evaluator_config」の中で「relevance」と「default」のそれぞれの設定において、"column_mapping"の位置を修正し、それによってデータマッピングの構造が視覚的に整理されました。
- コード内のインデントや構文が調整され、データのクエリ、真実のデータ、応答に関するマッピングがより明確に区別されるようになりました。

これにより、ユーザーはSDK評価を行う際に、設定の正確な構造と意味をより容易に理解できるようになっています。

## articles/ai-studio/how-to/develop/llama-index.md{#item-613372}

<details>
<summary>Diff</summary>
````diff
@@ -45,7 +45,10 @@ To run this tutorial, you need:
     ```bash
     pip install -U llama-index-llms-azure-inference
     pip install -U llama-index-embeddings-azure-inference
-    ``` 
+    ```
+
+    > [!IMPORTANT]
+    > Using the [Azure AI model inference service](https://aka.ms/aiservices/inference) requires version `0.2.4` for `llama-index-llms-azure-inference` or `llama-index-embeddings-azure-inference`.
 
 ## Configure the environment
 
@@ -67,7 +70,7 @@ export AZURE_INFERENCE_ENDPOINT="<your-model-endpoint-goes-here>"
 export AZURE_INFERENCE_CREDENTIAL="<your-key-goes-here>"
 ```
 
-Once configured, create a client to connect to the endpoint. The parameter `model_name` in the constructor is not required for endpoints serving a single model, like serverless endpoints.
+Once configured, create a client to connect to the endpoint.
 
 ```python
 import os
@@ -80,7 +83,20 @@ llm = AzureAICompletionsModel(
 ```
 
 > [!TIP]
-> If your model is an OpenAI model deployed to Azure OpenAI service or AI services resource, configure the client as indicated at [Azure OpenAI models](#azure-openai-models).
+> If your model is an OpenAI model deployed to Azure OpenAI service or AI services resource, configure the client as indicated at [Azure OpenAI models and Azure AI model inference service](#azure-openai-models-and-azure-ai-model-infernece-service).
+
+If your endpoint is serving more than one model, like with the [Azure AI model inference service](../../ai-services/model-inference.md) or [GitHub Models](https://github.com/marketplace/models), you have to indicate `model_name` parameter:
+
+```python
+import os
+from llama_index.llms.azure_inference import AzureAICompletionsModel
+
+llm = AzureAICompletionsModel(
+    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
+    model_name="mistral-large-2407",
+)
+```
 
 Alternatively, if your endpoint support Microsoft Entra ID, you can use the following code to create the client:
 
@@ -112,22 +128,23 @@ llm = AzureAICompletionsModel(
 )
 ```
 
-### Azure OpenAI models
+### Azure OpenAI models and Azure AI model infernece service
 
-If you are using Azure OpenAI models with key-based authentication, you need to pass the authentication key in the header `api-key`, which is the one expected in the Azure OpenAI service and in Azure AI Services. This configuration is not required if you are using Microsoft Entra ID (formerly known as Azure AD). The following example shows how to configure the client:
+If you are using Azure OpenAI models or [Azure AI model inference service](../../ai-services/model-inference.md), ensure you have at least version `0.2.4` of the LlamaIndex integration. Use `api_version` parameter in case you need to select a specific `api_version`. For the [Azure AI model inference service](../../ai-services/model-inference.md), you need to pass `model_name` parameter:
 
 ```python
-import os
 from llama_index.llms.azure_inference import AzureAICompletionsModel
 
 llm = AzureAICompletionsModel(
     endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
-    credential="",
-    client_kwargs={"headers" : { "api-key": os.environ["AZURE_INFERENCE_CREDENTIAL"] } }
+    credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
+    model_name="gpt-4o",
+    api_version="2024-05-01-preview",
 )
 ```
 
-Notice that `credentials` is still being passed with an empty value since it's a required parameter.
+> [!TIP]
+> Using a wrong `api_version` or one not supported by the model results in a `ResourceNotFound` exception.
 
 ### Inference parameters
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Llama Indexに関するドキュメントの更新"
}
```

### Explanation
この変更では、Llama Indexに関するドキュメントが更新され、Azure AIモデル推論サービスに関連する重要な情報が追加されました。ユーザーがAzure AIモデルを利用する際の設定や要件がより明確になりました。

主な変更点は以下の通りです：
- ユーザーが必要なパッケージのインストール手順に加え、Azure AIモデル推論サービスを使用するために必要な特定のバージョン（`0.2.4`）についての注意喚起が追加されました。
- 複数のモデルを提供しているエンドポイントを使用する場合、`model_name` パラメータを指定する必要があることが明記され、その具体的なコード例も示されました。
- Azure OpenAIモデルやAzure AIモデル推論サービスについてのセクション名が更新され、情報が集約されました。
- APIバージョンの指定に関する注意事項が追加され、誤ったバージョンを使用した場合に発生する可能性のある例外に関する説明が含まれています。

これにより、ユーザーはLlama Indexを使用した開発において、Azureのサービスとその利用要件をより良く理解し、適切に設定を行うことができるようになります。

## articles/ai-studio/includes/install-cli.md{#item-868060}

<details>
<summary>Diff</summary>
````diff
@@ -38,4 +38,9 @@ You can follow instructions [How to install the Azure CLI](/cli/azure/install-az
 After you install the Azure CLI, sign in using the ``az login`` command and sign-in using the browser:
 ```
 az login
+
+```
+Alternatively, you can log in manually via the browser with a device code.
+```
+az login --use-device-code
 ```
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure CLIのインストール手順の更新"
}
```

### Explanation
この修正では、Azure CLIのインストールに関するドキュメントが更新され、ログイン方法に関する情報が追加されました。具体的には、ブラウザを使用した通常のログイン方法に加えて、デバイスコードを使用した手動ログインの手順が記載されました。

主な変更点は以下の通りです：
- `az login` コマンドを使用したブラウザでのサインイン手順が説明された後、デバイスコードを使用する代替のログイン方法が新たに追加されました。
- 新しいログインコマンド `az login --use-device-code` が追加され、ユーザーはこのコマンドを使用して手動でログインできる方法が示されています。

これにより、ユーザーはAzure CLIを使用する際に、より柔軟なログインオプションを持つことができ、環境や状況に応じて選択できる利便性が向上しました。

## articles/ai-studio/media/how-to/hubs/resource-create-resources.png{#item-a5c0ba}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "リソース作成に関する新しい画像の追加"
}
```

### Explanation
この変更では、リソース作成に関連する新しい画像ファイルが追加されました。この画像は、Azure AI Studioの「ハブ」セクション内でのリソース作成の手順を視覚的に説明するために用いられることを目的としています。

主なポイントは以下の通りです：
- 新たに追加された画像ファイルの名前は `resource-create-resources.png` であり、具体的な手順やインターフェースを示すために活用される可能性があります。
- 画像の追加により、ドキュメントがより視覚的で理解しやすくなり、ユーザーがリソースを作成する際の手助けとなることが期待されます。

この変更は、ユーザーにとっての情報の受け取りやすさを向上させ、手順の理解を深めるため大いに貢献するでしょう。

## articles/ai-studio/media/how-to/hubs/studio-delete-hub.png{#item-9efef7}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ハブ削除に関する新しい画像の追加"
}
```

### Explanation
この変更では、ハブを削除する方法に関する新しい画像ファイルが追加されました。この画像は、Azure AI Studioの「ハブ」セクションでのハブ削除の手順を視覚的に示すために使用されることを目的としています。

主なポイントは以下の通りです：
- 新たに追加された画像ファイルの名前は `studio-delete-hub.png` で、ユーザーがハブを削除する際の具体的な操作手順を視覚的に説明していると考えられます。
- 画像が加わることで、ドキュメントはより視覚的で分かりやすくなり、ユーザーがハブ削除の手順を容易に理解できるようになることが期待されます。

この変更は、ユーザーが手順を追いやすくし、操作の理解を深めるために大いに役立つでしょう。


