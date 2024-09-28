---
date: '2024-09-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3b0d11e...MicrosoftDocs:804ee13
summary: この報告書では、Microsoft Docsに対するマイナーな更新と新機能が説明されています。主な変更点は、説明の明確化、特定情報の強調、新しい「安全なデータプレイグラウンド」の文書の追加、画像ファイルの更新を含みます。特に目立った重大な変更はありませんが、ユーザーの理解を深めるための重要な修正が行われています。また、文書全体の表現の一貫性を向上させ、不要な情報の整理も進められています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3b0d11e...MicrosoftDocs:804ee13){target="_blank"}

# ハイライト

ここでは、Microsoft Docsのさまざまな記事に対して行われたマイナーな更新と新機能について説明します。主な変更点には、説明の明確化、特定情報の強調、新規機能の追加、および画像ファイルの更新があります。

## 新機能
- 安全なデータプレイグラウンドの利用方法についての新しい文書
- 画像の追加：「AI検索マネージドアイデンティティ」、「AI検索プライベートエンドポイント」、「AI検索の公開アクセス無効化」、「AIサービスのマネージドアイデンティティ」、「AIサービスのプライベートエンドポイント」、「AIサービスのパブリックアクセス無効化」、「ハブのパブリックアクセス無効化」、「プライベートエンドポイント」、「検索APIのアクセス制御」、「ネットワーク隔離設定の選択」、「ストレージアカウントのパブリックアクセス無効化」、「ストレージのプライベートエンドポイント」
- 目次（`toc.yml`）に新しい項目「Secure playground chat」の追加

## ブレイキングチェンジ
- 特に重大な変更はなし。ただし、文書の更新によりユーザーの理解を深めるための重要な修正が行われています。

## その他の更新
- 記事内の表現の明確化や一貫性の向上
- 不要な情報の整理および削除
- 新しい画像ファイルのファイル名変更

# インサイト

このコード差分は、Microsoft Docsの多くの文書に対して行われた連続的なマイナーアップデートと、新しい機能の追加を示していますが、その目的と意図は明確です。以下にその目的を详しく説明します。

## 記事の明確化と一貫性向上

今回の変更では、多くの文書で内容の整理や表現の明確化が行われています。例えば、"configure-managed-network.md"におけるネットワーク隔離設定に関する整理や、「Jaisモデルのデプロイ」に関する文書の表現修正、また「Meta Llamaモデル」や「Mistral Nemoモデル」の出力フォーマットに関する警告文の明確化などです。

こうした変更は、ユーザーが文書を読む際により理解しやすくなることを目指しています。特に技術文書においては、曖昧な表現が誤解を招くことがあるため、正確かつ明瞭な説明が求められます。このような細かな修正が全体的なユーザー体験を向上させます。

## 新たなガイドラインの追加

「安全なデータプレイグラウンドの利用方法」という新しい文書は、大きな新機能として追加されています。224行に及ぶこの新しい記事は、Azure AI Studioのプレイグラウンドで安全にデータを扱うための詳細なガイドラインを提供しています。Microsoft Entra IDによる役割ベースのアクセス制御や、プライベートエンドポイントの使用など、安全なデータ管理の具体的な手法が紹介されています。

この新機能は、セキュリティ意識の高まりを背景にしており、ユーザーが安全にAzure AI Studioを利用できるようにするための重要なステップです。

## 画像ファイルの追加と更新

多くの新しい画像ファイルが追加され、既存の画像ファイル名が変更されています。この変更の意図は、文書内のビジュアルコンテンツを通じて情報をよりわかりやすく提供することです。

例えば、「AI検索マネージドアイデンティティ」、「AI検索プライベートエンドポイント」、「ネットワーク隔離設定の選択」などの画像は、具体的な手順や設定方法を視覚的に解説する目的で追加されています。これにより、ユーザーは文章だけでなく、視覚的なサポートを通じてより直感的に理解できるようになります。

こうした画像の追加は、特に技術的な設定や手順を説明する際に効果的です。視覚的な情報は理解を助け、操作ミスを

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [configure-managed-network.md](#item-dc9c50) | minor update | 管理ネットワークの構成に関する文書の変更 | modified | 1 | 18 | 19 | 
| [connections-add.md](#item-6f5a17) | minor update | Azure AI Studioでの接続追加の方法に関する文書の変更 | modified | 23 | 22 | 45 | 
| [deploy-models-jais.md](#item-0bd11f) | minor update | Jaisモデルのデプロイに関する文書の変更 | modified | 11 | 11 | 22 | 
| [deploy-models-llama.md](#item-6274a7) | minor update | Meta Llamaモデルのデプロイに関する文書の変更 | modified | 11 | 11 | 22 | 
| [deploy-models-mistral-nemo.md](#item-e7b729) | minor update | Mistral Nemoモデルのデプロイに関する文書の変更 | modified | 11 | 9 | 20 | 
| [deploy-models-mistral-open.md](#item-84e005) | minor update | Mistralモデルのデプロイに関する文書の変更 | modified | 20 | 20 | 40 | 
| [deploy-models-mistral.md](#item-487a41) | minor update | Mistralプレミアムチャットモデルのデプロイに関する文書の修正 | modified | 11 | 9 | 20 | 
| [deploy-models-phi-3-5-moe.md](#item-9af6ea) | minor update | Phi-3.5 MoEチャットモデルに関する文書の修正 | modified | 3 | 3 | 6 | 
| [deploy-models-phi-3-vision.md](#item-bd5aae) | minor update | Phi-3ビジョンチャットモデルに関する文書の修正 | modified | 3 | 3 | 6 | 
| [deploy-models-phi-3.md](#item-47e305) | minor update | Phi-3ファミリーのチャットモデルに関する文書の修正 | modified | 3 | 3 | 6 | 
| [fine-tune-model-llama.md](#item-2a42d8) | minor update | Llamaモデルのファインチューニングに関する文書の修正 | modified | 1 | 1 | 2 | 
| [secure-data-playground.md](#item-b7fa5e) | new feature | 安全なデータプレイグラウンドの利用方法に関する新しい文書 | added | 224 | 0 | 224 | 
| [connection-add-azure-ai-search-connect-entra-id.png](#item-3aff1d) | minor update | 画像ファイル名の変更: Azure AI Searchへの接続 | renamed | 0 | 0 | 0 | 
| [connections-all.png](#item-80f298) | minor update | 画像ファイル名の変更: 接続の概要 | renamed | 0 | 0 | 0 | 
| [ai-search-managed-identity.png](#item-9d42bb) | new feature | 新しい画像の追加: AI検索マネージドアイデンティティ | added | 0 | 0 | 0 | 
| [ai-search-private-endpoint.png](#item-f5e3ff) | new feature | 新しい画像の追加: AI検索プライベートエンドポイント | added | 0 | 0 | 0 | 
| [ai-search-public-access-disable.png](#item-086b7b) | new feature | 新しい画像の追加: AI検索の公開アクセス無効化 | added | 0 | 0 | 0 | 
| [ai-services-managed-identity.png](#item-fde1e6) | new feature | 新しい画像の追加: AIサービスのマネージドアイデンティティ | added | 0 | 0 | 0 | 
| [ai-services-private-endpoint.png](#item-c0ff55) | new feature | 新しい画像の追加: AIサービスのプライベートエンドポイント | added | 0 | 0 | 0 | 
| [ai-services-public-access-disable.png](#item-0bf186) | new feature | 新しい画像の追加: AIサービスのパブリックアクセスの無効化 | added | 0 | 0 | 0 | 
| [hub-public-access-disable.png](#item-2d67eb) | new feature | 新しい画像の追加: ハブのパブリックアクセスの無効化 | added | 0 | 0 | 0 | 
| [private-endpoints.png](#item-94033b) | new feature | 新しい画像の追加: プライベートエンドポイント | added | 0 | 0 | 0 | 
| [search-api-access-control.png](#item-a7279f) | new feature | 新しい画像の追加: 検索APIのアクセス制御 | added | 0 | 0 | 0 | 
| [select-network-isolation-configuration.png](#item-8f7f08) | new feature | 新しい画像の追加: ネットワーク隔離設定の選択 | added | 0 | 0 | 0 | 
| [storage-account-public-access-disable.png](#item-68fdda) | new feature | 新しい画像の追加: ストレージアカウントのパブリックアクセスを無効にする | added | 0 | 0 | 0 | 
| [storage-private-endpoint.png](#item-8ffe01) | new feature | 新しい画像の追加: ストレージのプライベートエンドポイント | added | 0 | 0 | 0 | 
| [toc.yml](#item-2745cd) | minor update | 目次に新しい項目を追加: セキュアなプレイグラウンドチャット | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/ai-studio/how-to/configure-managed-network.md{#item-dc9c50}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,6 @@ We have two network isolation aspects. One is the network isolation to access an
 You need to configure following network isolation configurations.
 
 - Choose network isolation mode. You have two options: allow internet outbound mode or allow only approved outbound mode.
-- Create private endpoint outbound rules to your private Azure resources. Private Azure AI Search isn't supported yet. 
 - If you use Visual Studio Code integration with allow only approved outbound mode, create FQDN outbound rules described in the [use Visual Studio Code](#scenario-use-visual-studio-code) section.
 - If you use HuggingFace models in Models with allow only approved outbound mode, create FQDN outbound rules described in the [use HuggingFace models](#scenario-use-huggingface-models) section.
 - If you use one of the open-source models with allow only approved outbound mode, create FQDN outbound rules described in the [curated by Azure AI](#scenario-curated-by-azure-ai) section.
@@ -44,10 +43,6 @@ There are three different configuration modes for outbound traffic from the mana
 <sup>1</sup> You can use outbound rules with _allow only approved outbound_ mode to achieve the same result as using allow internet outbound. The differences are:
 
 * Always use private endpoints to access Azure resources. 
-
-    > [!IMPORTANT]
-    > While you can create a private endpoint for Azure AI Search, the connected services must allow public networking. For more information, see [Connectivity to other services](#connectivity-to-other-services).
-
 * You must add rules for each outbound connection you need to allow.
 * Adding FQDN outbound rules __increase your costs__ as this rule type uses Azure Firewall. If you use outbound FQDN rules, charges for Azure Firewall are included in your billing. For more information, see [Pricing](#pricing).
 * The default rules for _allow only approved outbound_ are designed to minimize the risk of data exfiltration. Any outbound rules you add might increase your risk.
@@ -151,15 +146,6 @@ Before following the steps in this article, make sure you have the following pre
 * FQDN outbound rules only support ports 80 and 443.
 * When using a compute instance with a managed network, use the `az ml compute connect-ssh` command to connect to the compute using SSH.
 
-### Connectivity to other services
-
-* Azure AI Search should be public with your provisioned private Azure AI Studio hub.
-* The "Add your data" feature in the Azure AI Studio playground doesn't support using a virtual network or private endpoint on the following resources:
-    * Azure AI Search
-    * Azure OpenAI
-    * Storage resource
-
-
 ## Configure a managed virtual network to allow internet outbound
 
 > [!TIP]
@@ -808,7 +794,7 @@ If you plan to use __HuggingFace models__ with the hub, add outbound _FQDN_ rule
 
 ### Scenario: Curated by Azure AI
 
-These models involve dynamic installation of dependencies at runtime, and reequire outbound _FQDN_ rules to allow traffic to the following hosts:
+These models involve dynamic installation of dependencies at runtime, and require outbound _FQDN_ rules to allow traffic to the following hosts:
 
 *.anaconda.org
 *.anaconda.com
@@ -843,9 +829,6 @@ Private endpoints are currently supported for the following Azure services:
 * Azure Storage (all sub resource types)
 
 
-> [!IMPORTANT]
-> While you can create a private endpoint for Azure AI services and Azure AI Search, the connected services must allow public networking. For more information, see [Connectivity to other services](#connectivity-to-other-services).
-
 When you create a private endpoint, you provide the _resource type_ and _subresource_ that the endpoint connects to. Some resources have multiple types and subresources. For more information, see [what is a private endpoint](/azure/private-link/private-endpoint-overview).
 
 When you create a private endpoint for hub dependency resources, such as Azure Storage, Azure Container Registry, and Azure Key Vault, the resource can be in a different Azure subscription. However, the resource must be in the same tenant as the hub.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "管理ネットワークの構成に関する文書の変更"
}
```

### Explanation
この変更は、Microsoft Docsの「管理されたネットワークの構成」に関する記事に対して行われたマイナーな更新を反映しています。具体的には、18行が削除され、1行が追加され、全体の19行が変更されました。主な変更点は、ネットワーク隔離の設定に関するセクションの整理と不要な情報の削除です。また、重要な注意点が明確化されています。特に、「Azure AI Search」に関しては、プライベートエンドポイントを作成できるものの、接続されるサービスがパブリックネットワークを許可する必要があることを強調しています。この更新により、読者への情報提供がさらに明瞭で具体的になることを目的としています。詳細な更新内容はGitHubのリンクから確認できます。

## articles/ai-studio/how-to/connections-add.md{#item-6f5a17}

<details>
<summary>Diff</summary>
````diff
@@ -8,10 +8,11 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 09/13/2024
 ms.reviewer: larryfr
 ms.author: larryfr
 author: Blackmist
+# Customer Intent: As an admin or developer, I want to understand how to add new connections in Azure AI Studio.
 ---
 
 # How to add a new connection in Azure AI Studio
@@ -34,7 +35,7 @@ Here's a table of some of the available connection types in Azure AI Studio. The
 | Azure Content Safety | ✓ | Azure AI Content Safety is a service that detects potentially unsafe content in text, images, and videos. |
 | Azure OpenAI || Azure OpenAI is a service that provides access to the OpenAI GPT-3 model. |
 | Serverless Model | ✓ | Serverless Model connections allow you to [serverless API deployment](deploy-models-serverless.md). |
-| Microsoft OneLake | ✓ | Microsoft OneLake provides open access to all of your Fabric items through Azure Data Lake Storage (ADLS) Gen2 APIs and SDKs.<br/><br/>In Azure AI Studio you can set up a connection to your OneLake data using a OneLake URI. You can find the information that Azure AI Studio requires to construct a **OneLake Artifact URL** (workspace and item GUIDs) in the URL on the Fabric portal. For information about the URI syntax, see [Connecting to Microsoft OneLake](/fabric/onelake/onelake-access-api). |
+| Microsoft OneLake | ✓ | Microsoft OneLake provides open access to all of your Fabric items through Azure Data Lake Storage (ADLS) Gen2 APIs and SDKs.<br/><br/>In Azure AI Studio you can set up a connection to your OneLake data using a OneLake URI. You can find the information that Azure AI Studio requires to construct a __OneLake Artifact URL__ (workspace and item GUIDs) in the URL on the Fabric portal. For information about the URI syntax, see [Connecting to Microsoft OneLake](/fabric/onelake/onelake-access-api). |
 | API key || API Key connections handle authentication to your specified target on an individual basis. For example, you can use this connection with the SerpApi tool in prompt flow.  |
 | Custom || Custom connections allow you to securely store and access keys while storing related properties, such as targets and versions. Custom connections are useful when you have many targets that or cases where you wouldn't need a credential to access. LangChain scenarios are a good example where you would use custom service connections. Custom connections don't manage authentication, so you have to manage authentication on your own. |
 
@@ -43,54 +44,54 @@ Here's a table of some of the available connection types in Azure AI Studio. The
 Follow these steps to create a new connection that's only available for the current project.
 
 1. Go to your project in Azure AI Studio. If you don't have a project, [create a new project](./create-projects.md).
-1. Select **Settings** from the collapsible left menu. 
-1. Select **+ New connection** from the **Connected resources** section.
+1. Select __Settings__ from the collapsible left menu. 
+1. Select __+ New connection__ from the __Connected resources__ section.
 
     :::image type="content" source="../media/data-connections/connection-add.png" alt-text="Screenshot of the button to add a new connection." lightbox="../media/data-connections/connection-add.png":::
 
-1. Select the service you want to connect to from the list of available external resources. For example, select **Azure AI Search**.
+1. Select the service you want to connect to from the list of available external resources. For example, select __Azure AI Search__.
 
     :::image type="content" source="../media/data-connections/connection-add-browse-azure-ai-search.png" alt-text="Screenshot of the page to select Azure AI Search from a list of other resources." lightbox="../media/data-connections/connection-add-browse-azure-ai-search.png":::
 
-1. Browse for and select your Azure AI Search service from the list of available services and then select the type of __Authentication__ to use for the resource. Select **Add connection**.
+1. Browse for and select your Azure AI Search service from the list of available services and then select the type of __Authentication__ to use for the resource. Select __Add connection__.
 
     > [!TIP]
     > Different connection types support different authentication methods. Using Microsoft Entra ID may require specific Azure role-based access permissions for your developers. For more information, visit [Role-based access control](../concepts/rbac-ai-studio.md#scenario-connections-using-microsoft-entra-id-authentication).
     >
     > Microsoft Entra ID support with the Azure AI Search connection is currently in preview.
 
-    :::image type="content" source="../media/data-connections/connection-add-azure-ai-search-connect.png" alt-text="Screenshot of the page to select the Azure AI Search service that you want to connect to." lightbox="../media/data-connections/connection-add-azure-ai-search-connect.png":::
+    :::image type="content" source="../media/data-connections/connection-add-azure-ai-search-connect-entra-id.png" alt-text="Screenshot of the page to select the Azure AI Search service that you want to connect to." lightbox="../media/data-connections/connection-add-azure-ai-search-connect-entra-id.png":::
 
-1. After the service is connected, select **Close** to return to the **Settings** page.
-1. Select **Connected resources** > **View all** to view the new connection. You might need to refresh the page to see the new connection.
+1. After the service is connected, select __Close__ to return to the __Settings__ page.
+1. Select __Connected resources__ > __View all__ to view the new connection. You might need to refresh the page to see the new connection.
 
-    :::image type="content" source="../media/data-connections/connections-all-refreshed.png" alt-text="Screenshot of all connections after you add the Azure AI Search connection." lightbox="../media/data-connections/connections-all-refreshed.png":::
+    :::image type="content" source="../media/data-connections/connections-all.png" alt-text="Screenshot of all connections after you add the Azure AI Search connection." lightbox="../media/data-connections/connections-all.png":::
 
 ## Network isolation
 
-If your hub is configured for [network isolation](configure-managed-network.md), you might need to create an outbound private endpoint rule to connect to **Azure Blob Storage**, **Azure Data Lake Storage Gen2**, or **Microsoft OneLake**. A private endpoint rule is needed if one or both of the following are true:
+If your hub is configured for [network isolation](configure-managed-network.md), you might need to create an outbound private endpoint rule to connect to __Azure Blob Storage__, __Azure Data Lake Storage Gen2__, or __Microsoft OneLake__. A private endpoint rule is needed if one or both of the following are true:
 
 - The managed network for the hub is configured to [allow only approved outbound traffic](configure-managed-network.md#configure-a-managed-virtual-network-to-allow-only-approved-outbound). In this configuration, you must explicitly create outbound rules to allow traffic to other Azure resources.
 - The data source is configured to disallow public access. In this configuration, the data source can only be reached through secure methods, such as a private endpoint.
 
 To create an outbound private endpoint rule to the data source, use the following steps:
 
 1. Sign in to the [Azure portal](https://portal.azure.com), and select the Azure AI Studio hub.
-1. Select **Networking**, then **Workspace managed outbound access**.
-1. To add an outbound rule, select **Add user-defined outbound rules**. From the **Workspace outbound rules** sidebar, provide the following information:
+1. Select __Networking__, then __Workspace managed outbound access__.
+1. To add an outbound rule, select __Add user-defined outbound rules__. From the __Workspace outbound rules__ sidebar, provide the following information:
     
-    - **Rule name**: A name for the rule. The name must be unique for the AI Studio hub.
-    - **Destination type**: Private Endpoint.
-    - **Subscription**: The subscription that contains the Azure resource you want to connect to.
-    - **Resource type**: `Microsoft.Storage/storageAccounts`. This resource provider is used for Azure Storage, Azure Data Lake Storage Gen2, and Microsoft OneLake.
-    - **Resource name**: The name of the Azure resource (storage account).
-    - **Sub Resource**: The sub-resource of the Azure resource. Select `blob` in the case of Azure Blob storage. Select `dfs` for Azure Data Lake Storage Gen2 and Microsoft OneLake. 
+    - __Rule name__: A name for the rule. The name must be unique for the AI Studio hub.
+    - __Destination type__: Private Endpoint.
+    - __Subscription__: The subscription that contains the Azure resource you want to connect to.
+    - __Resource type__: `Microsoft.Storage/storageAccounts`. This resource provider is used for Azure Storage, Azure Data Lake Storage Gen2, and Microsoft OneLake.
+    - __Resource name__: The name of the Azure resource (storage account).
+    - __Sub Resource__: The sub-resource of the Azure resource. Select `blob` in the case of Azure Blob storage. Select `dfs` for Azure Data Lake Storage Gen2 and Microsoft OneLake. 
   
-1. Select **Save** to create the rule.
+1. Select __Save__ to create the rule.
 
-1. Select **Save** at the top of the page to save the changes to the managed network configuration.
+1. Select __Save__ at the top of the page to save the changes to the managed network configuration.
 
-## Next steps
+## Related content
 
 - [Connections in Azure AI Studio](../concepts/connections.md)
 - [How to create vector indexes](../how-to/index-add.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioでの接続追加の方法に関する文書の変更"
}
```

### Explanation
この変更は、Microsoft Docsの「Azure AI Studioでの接続の追加方法」に関する記事に対するマイナーな更新を表しています。合計で23行が追加され、22行が削除され、45行が修正されました。主な更新内容は、接続手順の明確化や必要な情報の追加です。

具体的には、接続の設定手順がより分かりやすく記述され、特にサービスの選択に際しての注意点やスクリプトの図示が強調されています。また、接続に関する注意事項や関連情報についても、新しい見出しが追加されています。これにより、ユーザーがAzure AI Studioでの新しい接続の追加をより簡単に理解し、適切に実行できるようにすることが意図されています。詳細はGitHubリンクで確認可能です。

## articles/ai-studio/how-to/deploy-models-jais.md{#item-0bd11f}

<details>
<summary>Diff</summary>
````diff
@@ -201,7 +201,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormat
+from azure.ai.inference.models import ChatCompletionsResponseFormatText
 
 response = client.complete(
     messages=[
@@ -214,12 +214,12 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
+    response_format=ChatCompletionsResponseFormatText(),
 )
 ```
 
 > [!WARNING]
-> Jais models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Jais doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -482,7 +482,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!WARNING]
-> Jais models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Jais doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -580,7 +580,7 @@ Deployment to a serverless API endpoint doesn't require quota from your subscrip
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -606,7 +606,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also uses the following namespaces but you may not always need them:
+This example also use the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -775,7 +775,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
 > [!WARNING]
-> Jais models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Jais doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1088,7 +1088,7 @@ Explore other parameters that you can specify in the inference client. For a ful
 ```
 
 > [!WARNING]
-> Jais models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Jais doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1165,14 +1165,14 @@ The following example shows how to handle events when the model detects harmful
 
 ## More inference examples
 
-For more examples of how to use Jais models, see the following examples and tutorials:
+For more examples of how to use Jais, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 
-## Cost and quota considerations for Jais models deployed as serverless API endpoints
+## Cost and quota considerations for Jais family of models deployed as serverless API endpoints
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
@@ -1189,4 +1189,4 @@ For more information on how to track costs, see [Monitor costs for models offere
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Jaisモデルのデプロイに関する文書の変更"
}
```

### Explanation
この変更は、Microsoft Docsの「Jaisモデルのデプロイに関する文書」に対するマイナーな更新を示しています。合計で11行が追加され、11行が削除され、22行が変更されました。主な変更点として、文書内での表現の一貫性と明確さが改善されています。

特に、Jaisモデルに関連する出力フォーマットの取り扱いについての表現が修正され、「JaisモデルではJSON出力フォーマットがサポートされていない」という警告がより読みやすくなっています。また、ソースコードの例において、インポートするクラスの名称が正確に変更されています。これにより、ユーザーはJaisモデルをより確実に使用できるようになり、クライアントライブラリの利用についての理解が深まることが意図されています。詳細についてはGitHubのリンクを参照することができます。

## articles/ai-studio/how-to/deploy-models-llama.md{#item-6274a7}

<details>
<summary>Diff</summary>
````diff
@@ -255,7 +255,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormat
+from azure.ai.inference.models import ChatCompletionsResponseFormatText
 
 response = client.complete(
     messages=[
@@ -268,12 +268,12 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
+    response_format=ChatCompletionsResponseFormatText(),
 )
 ```
 
 > [!WARNING]
-> Meta Llama models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Meta Llama doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -610,7 +610,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!WARNING]
-> Meta Llama models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Meta Llama doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -765,7 +765,7 @@ For deployment to a self-hosted managed compute, you must have enough quota in y
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -791,7 +791,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also uses the following namespaces but you may not always need them:
+This example also use the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -973,7 +973,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
 > [!WARNING]
-> Meta Llama models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Meta Llama doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1348,7 +1348,7 @@ Explore other parameters that you can specify in the inference client. For a ful
 ```
 
 > [!WARNING]
-> Meta Llama models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Meta Llama doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1441,7 +1441,7 @@ The following example shows how to handle events when the model detects harmful
 
 ## More inference examples
 
-For more examples of how to use Meta Llama models, see the following examples and tutorials:
+For more examples of how to use Meta Llama, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                             |
 |-------------------------------------------|-------------------|------------------------------------------------------------------- |
@@ -1453,7 +1453,7 @@ For more examples of how to use Meta Llama models, see the following examples an
 | LangChain                                 | Python            | [Link](https://aka.ms/meta-llama-3.1-405B-instruct-langchain)      |
 | LiteLLM                                   | Python            | [Link](https://aka.ms/meta-llama-3.1-405B-instruct-litellm)        | 
 
-## Cost and quota considerations for Meta Llama models deployed as serverless API endpoints
+## Cost and quota considerations for Meta Llama family of models deployed as serverless API endpoints
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
@@ -1463,7 +1463,7 @@ Each time a project subscribes to a given offer from the Azure Marketplace, a ne
 
 For more information on how to track costs, see [Monitor costs for models offered through the Azure Marketplace](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace).
 
-## Cost and quota considerations for Meta Llama models deployed to managed compute
+## Cost and quota considerations for Meta Llama family of models deployed to managed compute
 
 Meta Llama models deployed to managed compute are billed based on core hours of the associated compute instance. The cost of the compute instance is determined by the size of the instance, the number of instances running, and the run duration.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Meta Llamaモデルのデプロイに関する文書の変更"
}
```

### Explanation
この変更は、「Meta Llamaモデルのデプロイに関する文書」に対するマイナーな更新を反映しています。合計で11行が追加され、11行が削除され、22行の変更が行われました。主な内容としては、文書の表現の明確化と一貫性の向上が図られています。

具体的には、出力フォーマットに関する警告が一貫して改訂され、Meta LlamaモデルがJSON出力フォーマットをサポートしていない旨が強調されています。また、コード例内で使用されるクラス名などに変更があり、全体的な文面が一層洗練されています。これにより、ユーザーがMeta Llamaモデルを利用する際の理解が深まり、より正確な情報が提供されることが目的とされています。詳細についてはGitHubのリンクから確認できます。

## articles/ai-studio/how-to/deploy-models-mistral-nemo.md{#item-e7b729}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Mistral Nemo chat model with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 09/12/2024
+ms.date: 08/08/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -209,7 +209,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormat
+from azure.ai.inference.models import ChatCompletionsResponseFormatText
 
 response = client.complete(
     messages=[
@@ -222,7 +222,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
+    response_format=ChatCompletionsResponseFormatText(),
 )
 ```
 
@@ -234,13 +234,15 @@ Mistral Nemo chat model can create JSON outputs. Set `response_format` to `json_
 
 
 ```python
+from azure.ai.inference.models import ChatCompletionsResponseFormatJSON
+
 response = client.complete(
     messages=[
         SystemMessage(content="You are a helpful assistant that always generate responses in JSON format, using."
                       " the following format: { ""answer"": ""response"" }."),
         UserMessage(content="How many languages are in the world?"),
     ],
-    response_format={ "type": ChatCompletionsResponseFormat.JSON_OBJECT }
+    response_format=ChatCompletionsResponseFormatJSON()
 )
 ```
 
@@ -960,7 +962,7 @@ Deployment to a serverless API endpoint doesn't require quota from your subscrip
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -986,7 +988,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also uses the following namespaces but you may not always need them:
+This example also use the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -2008,7 +2010,7 @@ The following example shows how to handle events when the model detects harmful
 
 ## More inference examples
 
-For more examples of how to use Mistral models, see the following examples and tutorials:
+For more examples of how to use Mistral, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
@@ -2022,7 +2024,7 @@ For more examples of how to use Mistral models, see the following examples and t
 | LiteLLM                                   | Python            | [Link](https://aka.ms/mistral-large/litellm-sample)             | 
 
 
-## Cost and quota considerations for Mistral models deployed as serverless API endpoints
+## Cost and quota considerations for Mistral family of models deployed as serverless API endpoints
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
@@ -2039,4 +2041,4 @@ For more information on how to track costs, see [Monitor costs for models offere
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistral Nemoモデルのデプロイに関する文書の変更"
}
```

### Explanation
この変更は、「Mistral Nemoモデルのデプロイに関する文書」にマイナーな更新が行われたことを示しています。合計で11行が追加され、9行が削除され、20行の変更がありました。主な修正点は、文書内の情報の明確化や一貫性の向上です。

具体的には、クライアントからの応答をJSON形式で取得するために使用する必要のあるインポートが分かりやすく変更され、コード例も改善されています。また、使用するパラメータやインポートの名称がより正確に表現されています。これにより、ユーザーはMistral Nemoモデルを効果的に利用できるようになることが意図されています。文書の内容が最新の情報であることが確認でき、ユーザーは実際の使用時に役立つ具体的な指示を得ることができます。詳細はGitHubのリンクを通じて確認可能です。

## articles/ai-studio/how-to/deploy-models-mistral-open.md{#item-84e005}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Mistral-7B and Mixtral chat models with Azure AI S
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 09/12/2024
+ms.date: 08/08/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -63,8 +63,8 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling, enabling application development and tech stack modernization at scale
-* Precise information recall from large documents, due to its 64K tokens context window
+* Natively capable of function calling; along with the constrained output mode implemented on la Plateforme, this enables application development and tech stack modernization at scale
+* Pprecise information recall from large documents, due to its 64K tokens context window
 
 
 The following models are available:
@@ -257,7 +257,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormat
+from azure.ai.inference.models import ChatCompletionsResponseFormatText
 
 response = client.complete(
     messages=[
@@ -270,12 +270,12 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
+    response_format=ChatCompletionsResponseFormatText(),
 )
 ```
 
 > [!WARNING]
-> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -352,8 +352,8 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling, enabling application development and tech stack modernization at scale
-* Precise information recall from large documents, due to its 64K tokens context window
+* Natively capable of function calling; along with the constrained output mode implemented on la Plateforme, this enables application development and tech stack modernization at scale
+* Pprecise information recall from large documents, due to its 64K tokens context window
 
 
 The following models are available:
@@ -576,7 +576,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!WARNING]
-> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -658,8 +658,8 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling, enabling application development and tech stack modernization at scale
-* Precise information recall from large documents, due to its 64K tokens context window
+* Natively capable of function calling; along with the constrained output mode implemented on la Plateforme, this enables application development and tech stack modernization at scale
+* Pprecise information recall from large documents, due to its 64K tokens context window
 
 
 The following models are available:
@@ -689,7 +689,7 @@ For deployment to a self-hosted managed compute, you must have enough quota in y
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -715,7 +715,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also uses the following namespaces but you may not always need them:
+This example also use the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -897,7 +897,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
 > [!WARNING]
-> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -976,8 +976,8 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling, enabling application development and tech stack modernization at scale
-* Precise information recall from large documents, due to its 64K tokens context window
+* Natively capable of function calling; along with the constrained output mode implemented on la Plateforme, this enables application development and tech stack modernization at scale
+* Pprecise information recall from large documents, due to its 64K tokens context window
 
 
 The following models are available:
@@ -1230,7 +1230,7 @@ Explore other parameters that you can specify in the inference client. For a ful
 ```
 
 > [!WARNING]
-> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1279,7 +1279,7 @@ The following extra parameters can be passed to Mistral-7B and Mixtral chat mode
 
 ## More inference examples
 
-For more examples of how to use Mistral models, see the following examples and tutorials:
+For more examples of how to use Mistral, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
@@ -1293,7 +1293,7 @@ For more examples of how to use Mistral models, see the following examples and t
 | LiteLLM                                   | Python            | [Link](https://aka.ms/mistral-large/litellm-sample)             | 
 
 
-## Cost and quota considerations for Mistral models deployed to managed compute
+## Cost and quota considerations for Mistral family of models deployed to managed compute
 
 Mistral models deployed to managed compute are billed based on core hours of the associated compute instance. The cost of the compute instance is determined by the size of the instance, the number of instances running, and the run duration.
 
@@ -1306,4 +1306,4 @@ It is a good practice to start with a low number of instances and scale up as ne
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralモデルのデプロイに関する文書の変更"
}
```

### Explanation
この変更は、「Mistralモデルのデプロイに関する文書」に対して行われたマイナーな更新を示しています。合計で20行が追加され、20行が削除され、40行の修正が行われました。主な修正点は、文書内の内容の明確化と一貫性の向上です。

具体的には、MistralおよびMixtralモデルに関連する強みの記述が修正され、関数呼び出しが可能であることや、大きなドキュメントからの情報の正確なリコールといった特徴が強調されています。また、コード例内でのインポート名の変更や、JSON出力フォーマットのサポートに関する警告文の表現が一貫して整理されました。

さらに、文書の更新日が変更されたことも注目すべき点であり、これにより最新の情報が提供されていることが示されています。このような変更により、ユーザーはMistralモデルを利用する際に、より正確かつ明確な情報を得られるような工夫がなされています。詳細な変更内容はGitHubのリンクから確認できます。

## articles/ai-studio/how-to/deploy-models-mistral.md{#item-487a41}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Mistral premium chat models with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 09/12/2024
+ms.date: 08/08/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -239,7 +239,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormat
+from azure.ai.inference.models import ChatCompletionsResponseFormatText
 
 response = client.complete(
     messages=[
@@ -252,7 +252,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
+    response_format=ChatCompletionsResponseFormatText(),
 )
 ```
 
@@ -264,13 +264,15 @@ Mistral premium chat models can create JSON outputs. Set `response_format` to `j
 
 
 ```python
+from azure.ai.inference.models import ChatCompletionsResponseFormatJSON
+
 response = client.complete(
     messages=[
         SystemMessage(content="You are a helpful assistant that always generate responses in JSON format, using."
                       " the following format: { ""answer"": ""response"" }."),
         UserMessage(content="How many languages are in the world?"),
     ],
-    response_format={ "type": ChatCompletionsResponseFormat.JSON_OBJECT }
+    response_format=ChatCompletionsResponseFormatJSON()
 )
 ```
 
@@ -1050,7 +1052,7 @@ Deployment to a serverless API endpoint doesn't require quota from your subscrip
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -1076,7 +1078,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also uses the following namespaces but you may not always need them:
+This example also use the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -2128,7 +2130,7 @@ The following example shows how to handle events when the model detects harmful
 
 ## More inference examples
 
-For more examples of how to use Mistral models, see the following examples and tutorials:
+For more examples of how to use Mistral, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
@@ -2142,7 +2144,7 @@ For more examples of how to use Mistral models, see the following examples and t
 | LiteLLM                                   | Python            | [Link](https://aka.ms/mistral-large/litellm-sample)             | 
 
 
-## Cost and quota considerations for Mistral models deployed as serverless API endpoints
+## Cost and quota considerations for Mistral family of models deployed as serverless API endpoints
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
@@ -2159,4 +2161,4 @@ For more information on how to track costs, see [Monitor costs for models offere
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralプレミアムチャットモデルのデプロイに関する文書の修正"
}
```

### Explanation
このコードの変更は、「Mistralプレミアムチャットモデルのデプロイ」に関する文書に対するマイナーな更新を示しています。合計で11行が追加され、9行が削除され、20行にわたる修正が行われました。主な変更点は、情報の更新と文書の明確化です。

具体的に見ると、文書の更新日が変更され、最新の情報が提供されています。また、コードの例において、インポート名称が変更されており、特に`ChatCompletionsResponseFormat`から`ChatCompletionsResponseFormatText`への移行が見られます。さらに、JSON出力フォーマットに関する警告文が簡潔に整理され、ユーザーに明確な指示が与えられています。

文書内の記述も一部変更され、Mistralモデルの機能や使い方がより明確に説明されています。また、ナビゲーションのためのリンクや、推奨されるリソースのリストも更新されています。このような小さな変更が、ユーザーにとってより良い理解を助け、Mistralモデルの活用を促進することを目的としています。詳細はGitHubのリンクを通じて確認できます。

## articles/ai-studio/how-to/deploy-models-phi-3-5-moe.md{#item-9af6ea}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Phi-3.5 MoE chat model with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 09/12/2024
+ms.date: 08/19/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -219,7 +219,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormat
+from azure.ai.inference.models import ChatCompletionsResponseFormatText
 
 response = client.complete(
     messages=[
@@ -232,7 +232,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
+    response_format=ChatCompletionsResponseFormatText(),
 )
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3.5 MoEチャットモデルに関する文書の修正"
}
```

### Explanation
このコード変更は、「Phi-3.5 MoEチャットモデルのデプロイ」に関する文書に対するマイナーな更新を示しています。合計で3行が追加され、3行が削除され、6行の修正が行われました。主に文書の最新化と明確化が目的です。

具体的には、文書の更新日が変更され、情報が最新の状態に保たれています。また、コード例において、`ChatCompletionsResponseFormat`から`ChatCompletionsResponseFormatText`へのインポートの変更があり、これはより明確な命名規則に基づいています。そして、`response_format`の設定方法も更新され、より直感的な形式が適用されています。

これらの変更により、ユーザーはPhi-3.5 MoEモデルを使用する際に、より正確で効果的な情報を得ることが可能になります。文書のリファレンスも整備され、全体的にユーザビリティが向上しています。詳細な変更内容については、GitHubのリンクから確認できます。

## articles/ai-studio/how-to/deploy-models-phi-3-vision.md{#item-bd5aae}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Phi-3 chat model with vision with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 09/12/2024
+ms.date: 08/19/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -215,7 +215,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormat
+from azure.ai.inference.models import ChatCompletionsResponseFormatText
 
 response = client.complete(
     messages=[
@@ -228,7 +228,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
+    response_format=ChatCompletionsResponseFormatText(),
 )
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3ビジョンチャットモデルに関する文書の修正"
}
```

### Explanation
このコード変更は、「Phi-3ビジョンチャットモデルのデプロイ」に関する文書に対するマイナーな更新を示しています。合計で3行が追加され、3行が削除され、6行の修正が行われました。主に文書の最新化と明確化が目的です。

具体的には、文書の更新日が新しい日付に変更され、最新の情報が提供されています。また、コードの例において、`ChatCompletionsResponseFormat`から`ChatCompletionsResponseFormatText`へと変更が行われており、より分かりやすい命名が反映されています。さらに、`response_format`の設定も修正され、新たに指定された形式が適用されています。

これらの変更により、ユーザーはPhi-3ビジョンチャットモデルを使用する際に、より正確で効果的なガイダンスを受けられるようになります。文書のリファレンスも整えられ、全体的に利便性が向上しています。詳細については、GitHubのリンクから確認できます。

## articles/ai-studio/how-to/deploy-models-phi-3.md{#item-47e305}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Phi-3 family chat models with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 09/12/2024
+ms.date: 08/19/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -256,7 +256,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormat
+from azure.ai.inference.models import ChatCompletionsResponseFormatText
 
 response = client.complete(
     messages=[
@@ -269,7 +269,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
+    response_format=ChatCompletionsResponseFormatText(),
 )
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3ファミリーのチャットモデルに関する文書の修正"
}
```

### Explanation
このコード変更は、「Phi-3ファミリーのチャットモデルのデプロイ」に関する文書に対するマイナーな更新を示しています。合計で3行が追加され、3行が削除され、6行の修正が行われました。主に文書の最新化と明確化が目的です。

具体的には、文書の更新日が新しい日付に変更され、最新の情報が反映されています。また、コード例では、`ChatCompletionsResponseFormat`から`ChatCompletionsResponseFormatText`へと変更されており、より分かりやすい命名に改善されています。さらに、`response_format`の設定についても修正が行われ、指定の形式が新たに適用されています。

これにより、ユーザーはPhi-3ファミリーのチャットモデルを使用する際に、より正確で有用な情報を得ることができ、文書全体の利便性が向上しています。詳細な変更内容については、GitHubのリンクから確認できます。

## articles/ai-studio/how-to/fine-tune-model-llama.md{#item-2a42d8}

<details>
<summary>Diff</summary>
````diff
@@ -230,7 +230,7 @@ To fine-tune a Llama 2 model in an existing Azure AI Studio project, follow thes
 
     :::image type="content" source="../media/how-to/fine-tune/llama/llama-pay-as-you-go-overview.png" alt-text="Screenshot of pay-as-you-go marketplace overview." lightbox="../media/how-to/fine-tune/llama/llama-pay-as-you-go-overview.png":::
 
-1. Choose a base model to fine-tune and select **Confirm**. Your choice influences both the performance and [the cost of your model](./deploy-models-llama.md#cost-and-quota-considerations-for-meta-llama-models-deployed-as-serverless-api-endpoints).
+1. Choose a base model to fine-tune and select **Confirm**. Your choice influences both the performance and [the cost of your model](./deploy-models-llama.md#cost-and-quota-considerations-for-meta-llama-family-of-models-deployed-as-serverless-api-endpoints).
 
     :::image type="content" source="../media/how-to/fine-tune/llama/fine-tune-select-model.png" alt-text="Screenshot of option to select a model to fine-tune." lightbox="../media/how-to/fine-tune/llama/fine-tune-select-model.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Llamaモデルのファインチューニングに関する文書の修正"
}
```

### Explanation
このコード変更は、「Llamaモデルのファインチューニング」に関する文書に対するマイナーな更新を示しています。今回の更新では、1行が追加され、1行が削除され、合計で2行の修正が行われました。

具体的には、ファインチューニングの際に選択したベースモデルの影響についての説明の一部が修正されています。具体的には、モデルのコストに関連するリンクのテキストが「meta-llama models」から「meta-llama family of models」に変更されました。この修正により、より明確にモデルファミリーについての情報が伝わるようになります。

このような文書の更新は、ユーザーがLlamaモデルをファインチューニングする際に、正確で最新の情報を提供することに貢献しており、文書全体の理解を向上させることが目的です。詳細な変更内容については、GitHubのリンクから確認できます。

## articles/ai-studio/how-to/secure-data-playground.md{#item-b7fa5e}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,224 @@
+---
+title: Securely use playground chat
+titleSuffix: Azure AI Studio
+description: Learn how to securely use the Azure AI Studio playground chat on your own data. 
+manager: scottpolly
+ms.service: azure-ai-studio
+ms.topic: how-to
+ms.date: 09/13/2024
+ms.reviewer: meerakurup 
+ms.author: larryfr
+author: Blackmist
+zone_pivot_groups: azure-ai-studio-sdk-cli
+# Customer intent: As an administrator, I want to make sure that my data is handled securely when used in the playground chat.
+---
+
+# Use your data securely with the Azure AI Studio playground
+
+Use this article to learn how to securely use Azure AI Studio's playground chat on your data. The following sections provide our recommended configuration to protect your data and resources by using Microsoft Entra ID role-based access control, a managed network, and private endpoints. We recommend disabling public network access for Azure OpenAI resources, Azure AI Search resources, and storage accounts. Using selected networks with IP rules isn't supported because the services' IP addresses are dynamic.
+
+> [!NOTE]
+> AI Studio's managed virtual network settings apply only to AI Studio's managed compute resources, not platform as a service (PaaS) services like Azure OpenAI or Azure AI Search. When using PaaS services, there is no data exfiltration risk because the services are managed by Microsoft.
+
+The following table summarizes the changes made in this article:
+
+| Configurations | Default | Secure | Notes |
+| ----- | ----- | ----- | ----- |
+| Data sent between services | Sent over the public network | Sent through a private network | Data is sent encrypted using HTTPS even over the public network. |
+| Service authentication | API keys | Microsoft Entra ID | Anyone with the API key can authenticate to the service. Microsoft Entra ID provides more granular and robust authentication. |
+| Service permissions | API Keys | Role-based access control | API keys provide full access to the service. Role-based access control provides granular access to the service. |
+| Network access | Public | Private | Using a private network prevents entities outside the private network from accessing resources secured by it. |
+
+## Prerequisites
+
+Ensure that the AI Studio hub is deployed with the __Identity-based access__ setting for the Storage account. This configuration is required for the correct access control and security of your AI Studio Hub. You can verify this configuration using one of the following methods:
+
+- In the Azure portal, select the hub and then select __Settings__, __Properties__, and __Options__. At the bottom of the page, verify that __Storage account access type__ is set to __Identity-based access__.
+- If deploying using Azure Resource Manager or Bicep templates, include the `systemDatastoresAuthMode: 'identity'` property in your deployment template.
+
+
+## Configure Network Isolated AI Studio Hub
+
+If you're __creating a new Azure AI Studio hub__, use one of the following documents to create a hub with network isolation:
+
+- [Create a secure Azure AI Studio hub in Azure portal](create-secure-ai-hub.md)
+- [Create a secure Azure AI Studio hub using the Python SDK or Azure CLI](develop/create-hub-project-sdk.md)
+
+If you have an __existing Azure AI Studio hub__ that isn't configured to use a managed network, use the following steps to configure it to use one:
+
+1. From the Azure portal, select the hub, then select __Settings__, __Networking__, __Public access__.
+1. To disable public network access for the hub, set __Public network access__ to __Disabled__. Select __Save__ to apply the changes.
+
+    :::image type="content" source="../media/how-to/secure-playground-on-your-data/hub-public-access-disable.png" alt-text="Screenshot of Azure AI Studio hub settings with public access disabled.":::
+
+1. Select select __Workspace managed outbound access__ and then select either the __Allow Internet Outbound__ or __Allow Only Approved Outbound__ network isolation mode. Select __Save__ to apply the changes.
+
+    :::image type="content" source="../media/how-to/secure-playground-on-your-data/select-network-isolation-configuration.png" alt-text="Screenshot of the Azure AI Studio hub settings with allow internet outbound selected.":::
+
+## Configure Azure AI services Resource
+
+Depending on your configuration, you might use an Azure AI services resource that also includes Azure OpenAI or a standalone Azure OpenAI resource. The steps in this section configure an AI services resource. The same steps apply to an Azure OpenAI resource.
+
+1. If you don't have an existing Azure AI services resource for your Azure AI Studio hub, [create one](/azure/ai-services/openai/how-to/create-resource?pivots=web-portal).
+1. From the Azure portal, select the AI services resource, then select __Resource Management, __Identity__, and __System assigned__. 
+1. To create a managed identity for the AI services resource, set the __Status__ to __On__. Select __Save__ to apply the changes.
+
+    :::image type="content" source="../media/how-to/secure-playground-on-your-data/ai-services-managed-identity.png" alt-text="Screenshot of setting the status of managed identity to on.":::
+
+1. To disable public network access, select __Networking__, __Firewalls and virtual networks__, and then set __Allow access from__ to __Disabled__. Under __Exceptions__, make sure that __Allow Azure services on the trusted services list__ is enabled. Select __Save__ to apply the changes.
+
+    :::image type="content" source="../media/how-to/secure-playground-on-your-data/ai-services-public-access-disable.png" alt-text="Screenshot of AI services with public network access disabled.":::
+
+1. To create a private endpoint for the AI services resource, select __Networking__, __Private endpoint connections__, and then select __+ Private endpoint__. This private endpoint is used to allow clients in your Azure Virtual Network to securely communicate with the AI services resource. For more information on using private endpoints with Azure AI services, visit the [Use private endpoints](/azure/ai-services/cognitive-services-virtual-networks#use-private-endpoints) article.
+
+    :::image type="content" source="../media/how-to/secure-playground-on-your-data/ai-services-private-endpoint.png" alt-text="Screenshot of the private endpoint section for AI services.":::
+
+    1. From the __Basics__ tab, enter a unique name for the private endpoint, network interface, and select the region to create the private endpoint in.
+    1. From the __Resource__ tab, accept the target subresource of __account__.
+    1. From the __Virtual Network__ tab, select the _Azure Virtual Network_ that the private endpoint connects to. This network should be the same one that your clients connect to, and that the Azure AI Studio hub has a private endpoint connection to.
+    1. From the __DNS__ tab, select the defaults for the DNS settings.
+    1. Continue to the __Review + create__ tab, then select __Create__ to create the private endpoint.
+
+1. Currently you can't disable local (shared key) authentication to Azure AI services through the Azure portal. Instead, you can use the following [Azure PowerShell](/powershell/azure/what-is-azure-powershell) cmdlet:
+
+    ```azurepowershell
+    Set-AzCognitiveServicesAccount -resourceGroupName "resourceGroupName" -name "AIServicesAccountName" -disableLocalAuth $true
+    ```
+
+    For more information, visit the [Disable local authentication in Azure AI services](/azure/ai-services/disable-local-auth) article.
+
+## Configure Azure AI Search
+
+You might want to consider using an Azure AI Search index when you either want to: 
+ - Customize the index creation process. 
+ - Reuse an index created before by ingesting data from other data sources. 
+
+To use an existing index, it must have at least one searchable field. Ensure at least one valid vector column is mapped when using vector search. 
+
+> [!IMPORTANT]
+> The information in this section is only applicable for securing the Azure AI Search resource for use with Azure AI Studio. If you're using Azure AI Search for other purposes, you might need to configure additional settings. For related information on configuring Azure AI Search, visit the following articles:
+>
+> - [Configure network access and firewall rules](../../search/service-configure-firewall.md)
+> - [Enable or disable role-based access control](/azure/search/search-security-enable-roles)
+> - [Configure a search service to connect using a managed identity](/azure/search/search-howto-managed-identities-data-sources)
+
+1. If you don't have an existing Azure AI Search resource for your Azure AI Studio hub, [create one](/azure/search/search-create-service-portal).
+1. From the Azure portal, select the AI Search resource, then select __Settings__, __Identity__, and __System assigned__.
+1. To create a managed identity for the AI Search resource, set the __Status__ to __On__. Select __Save__ to apply the changes.
+
+    :::image type="content" source="../media/how-to/secure-playground-on-your-data/ai-search-managed-identity.png" alt-text="Screenshot of AI Search with a system-managed identity configuration.":::
+
+1. To disable public network access, select __Settings__, __Networking__, and __Firewalls and virtual networks__. Set __Public network access__ to __Disabled__. Under __Exceptions__, make sure that __Allow Azure services on the trusted services list__ is enabled. Select __Save__ to apply the changes.
+
+    :::image type="content" source="../media/how-to/secure-playground-on-your-data/ai-search-public-access-disable.png" alt-text="Screenshot of AI Search with public network access disabled.":::
+
+1. To create a private endpoint for the AI Search resource, select __Networking__, __Private endpoint connections__, and then select __+ Create a private endpoint__.
+
+    :::image type="content" source="../media/how-to/secure-playground-on-your-data/ai-search-private-endpoint.png" alt-text="Screenshot of the private endpoint section of AI Search.":::
+
+    1. From the __Basics__ tab, enter a unique name for the private endpoint, network interface, and select the region to create the private endpoint in.
+    1. From the __Resource__ tab, select the __Subscription__ that contains the resource, set the __Resource type__ to __Microsoft.Search/searchServices__, and select the Azure AI Search resource. The only available subresource is __searchService__.
+    1. From the __Virtual Network__ tab, select the _Azure Virtual Network_ that the private endpoint connects to. This network should be the same one that your clients connect to, and that the Azure AI Studio hub has a private endpoint connection to.
+    1. From the __DNS__ tab, select the defaults for the DNS settings.
+    1. Continue to the __Review + create__ tab, then select __Create__ to create the private endpoint.
+
+1. To enable API access based on role-based access controls, select __Settings__, __Keys__, and then set __API Access control__ to __Role-based access control__ or __Both__. Select __Yes_ to apply the changes.
+
+    > [!NOTE]
+    > Select __Both__ if you have other services that use a key to access the Azure AI Search. Select __Role-based access control__ to disable key-based access.
+
+    :::image type="content" source="../media/how-to/secure-playground-on-your-data/search-api-access-control.png" alt-text="Screenshot of AI Search with API access set to both.":::
+
+## Configure Azure Storage (ingestion-only)
+
+If you're using Azure Storage for the ingestion scenario with the Azure AI Studio playground, you need to configure your Azure Storage Account.
+
+1. Create a Storage Account resource 
+1. From the Azure portal, select the Storage Account resource, then select __Security + networking__, __Networking__, and __Firewalls and virtual networks__.
+1. To disable public network access and allow access from trusted services, set __Public network access__ to __Enabled from selected virtual networks and IP addresses__. Under __Exceptions__, make sure that __Allow Azure services on the trusted services list__ is enabled.
+
+    :::image type="content" source="../media/how-to/secure-playground-on-your-data/storage-account-public-access-disable.png" alt-text="Screenshot of storage account network configuration.":::
+
+1. Set __Public network access__ to __Disabled__ and then select __Save__ to apply the changes. The configuration to allow access from trusted services is still enabled.
+1. To create a private endpoint for Azure Storage, select __Networking__, __Private endpoint connections__, and then select __+ Private endpoint__.
+
+    :::image type="content" source="../media/how-to/secure-playground-on-your-data/storage-private-endpoint.png" alt-text="Screenshot of the private endpoint section for the storage account.":::
+
+    1. From the __Basics__ tab, enter a unique name for the private endpoint, network interface, and select the region to create the private endpoint in.
+    1. From the __Resource__ tab, set the __Target sub-resource__ to __blob__.
+    1. From the __Virtual Network__ tab, select the _Azure Virtual Network_ that the private endpoint connects to. This network should be the same one that your clients connect to, and that the Azure AI Studio hub has a private endpoint connection to.
+    1. From the __DNS__ tab, select the defaults for the DNS settings.
+    1. Continue to the __Review + create__ tab, then select __Create__ to create the private endpoint.
+
+1. Repeat the previous step to create a private endpoint, however this time set the __Target sub-resource__ to __file__. The previous private endpoint allows secure communication to blob storage, and this private endpoint allows secure communication to file storage.
+1. To disable local (shared key) authentication to storage, select __Configuration__, under __Settings__. Set __Allow storage account key access__ to __Disabled__, and then select __Save__ to apply the changes. For more information, visit the [Prevent authorization with shared key](/azure/storage/common/shared-key-authorization-prevent) article. 
+
+## Configure Azure Key Vault
+
+Azure AI Studio uses Azure Key Vault to securely store and manage secrets. To allow access to the key vault from trusted services, use the following steps.
+
+> [!NOTE]
+> These steps assume that the key vault has already been configured for network isolation when you created your Azure AI Studio Hub.
+
+1. From the Azure portal, select the Key Vault resource, then select __Settings__, __Networking__, and __Firewalls and virtual networks__.
+1. From the __Exception__ section of the page, make sure that __Allow trusted Microsoft services to bypass firewall__ is __enabled__.
+
+## Configure connections to use Microsoft Entra ID
+
+Connections from Azure AI Studio to Azure AI services and Azure AI Search should use Microsoft Entra ID for secure access. Connections are created from [Azure AI Studio](https://ai.azure.com) instead of the Azure portal.
+
+> [!IMPORTANT]
+> Using Microsoft Entra ID with Azure AI Search is currently a preview feature. For more information on connections, visit the [Add connections](connections-add.md#create-a-new-connection) article.
+
+1. from Azure AI Studio, select __Connections__. If you have existing connections to the resources, you can select the connection and then select the __pencil icon__ in the __Access details__ section to update the connection. Set the __Authentication__ field to __Microsoft Entra ID__, then select __Update__.
+1. To create a new connection, select __+ New connection__, then select the resource type. Browse for the resource or enter the required information, then set __Authentication__ to __Microsoft Entra ID__. Select __Add connection__ to create the connection.
+
+Repeat these steps for each resource that you want to connect to using Microsoft Entra ID.
+
+## Assign roles to resources and users
+
+The services need to authorize each other to access the connected resources. The admin performing the configuration needs to have the __Owner__ role on these resources to add role assignments. The following table lists the required role assignments for each resource. The __Assignee__ column refers to the system-assigned managed identity of the listed resource. The __Resource__ column refers to the resource that the assignee needs to access. For example, the Azure AI Search has a system-assigned managed identity that needs to be assigned the __Storage Blob Data Contributor__ role for the Azure Storage Account.
+
+| Resource | Role | Assignee | Description |
+|----------|------|----------|-------------|
+| Azure AI Search | Search Index Data Contributor | Azure AI services/OpenAI | Read-write access to content in indexes. Import, refresh, or query the documents collection of an index. Only used for ingestion and inference scenarios. |
+| Azure AI Search | Search Index Data Reader | Azure AI services/OpenAI | Inference service queries the data from the index. Only used for inference scenarios. |
+| Azure AI Search | Search Service Contributor | Azure AI services/OpenAI | Read-write access to object definitions (indexes, aliases, synonym maps, indexers, data sources, and skillsets). Inference service queries the index schema for auto fields mapping. Data ingestion service creates index, data sources, skill set, indexer, and queries the indexer status. |
+| Azure AI services/OpenAI | Cognitive Services OpenAI Contributor | Azure AI Search | Custom skill |
+| Azure OpenAI Resource for chat model | Cognitive Services OpenAI User | Azure OpenAI resource for embedding model | Required only if using two Azure OpenAI resources to communicate. |
+| Azure Storage Account | Storage Blob Data Contributor | Azure AI Search | Reads blob and writes knowledge store. |
+| Azure Storage Account | Storage Blob Data Contributor | Azure AI services/OpenAI | Reads from the input container, and writes the preprocess result to the output container. |
+
+> [!NOTE]
+> The Cognitive Services OpenAI User role is only required if you are using two Azure OpenAI resources: one for your chat model and one for your embedding model. If this applies, enable Trusted Services AND ensure the Connection for your embedding model Azure OpenAI resource has EntraID enabled.  
+
+To enable your developers to use these resources to build applications, add the developers' identity with the following role assignments to the listed resources.
+
+| Resource | Role | Description |
+|----------|------|-------------|
+| Azure AI Search | Contributor | List API-Keys to list indexes from Azure OpenAI Studio. |
+| Azure AI Search | Search Index Data Contributor | Required for the indexing scenario. |
+| Azure AI services/OpenAI | Cognitive Services OpenAI Contributor | Call public ingestion API from Azure OpenAI Studio. |
+| Azure AI services/OpenAI | Cognitive Services User | List API-Keys from Azure OpenAI Studio. |
+| Azure AI services/OpenAI | Contributor | Allows for calls to the control plane. |
+| Azure Storage Account | Contributor | List Account SAS to upload files from Azure OpenAI Studio. |
+| Azure Storage Account | Storage Blob Data Contributor | Needed for developers to read and write to blob storage. |
+| Azure Storage Account | Storage File Data PrivilegedContributorRoleId | Needed to Access File Share in Storage for Promptflow data. |
+| The resource group or Azure subscription where the developer need to deploy the web app to | Contributor | Deploy web app to the developer's Azure subscription. |
+
+## Use your data in AI Studio  
+
+Now, the data you add to AI Studio is secured to the isolated network provided by your Azure AI Studio hub and project. For an example of using data, visit the [build a question and answer copilot](../tutorials/deploy-copilot-ai-studio.md) tutorial.
+
+## Deploy web apps
+
+For information on configuring web app deployments, visit the [Use Azure OpenAI on your data securely](/azure/ai-services/openai/how-to/use-your-data-securely#web-app) article.
+
+## Limitations
+
+When using the Chat playground in Azure AI Studio, don't navigate to another tab within Studio. If you do navigate to another tab, when you return to the Chat tab you must remove your data and then add it back.
+
+## Related content
+
+- [Tutorial: Deploy an enterprise chat web app](../tutorials/deploy-chat-web-app.md)
+- [How to configure a managed network](configure-managed-network.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "安全なデータプレイグラウンドの利用方法に関する新しい文書"
}
```

### Explanation
このコード変更は、「安全なデータプレイグラウンドの利用方法」という新しい文書の追加を示しています。文書全体で224行の追加があり、内容はAzure AI Studioのプレイグラウンドでデータを安全に使用する方法について詳しく説明しています。

新しい文書では、Microsoft Entra IDによる役割ベースのアクセス制御、管理されたネットワーク、およびプライベートエンドポイントを使用してデータとリソースを保護するための推奨設定が提供されています。また、Azure OpenAIリソースやAzure AI Searchリソース、ストレージアカウントの公衆ネットワークアクセスを無効にすることが推奨されています。

文書内には、その設定を行うための手順、推奨される構成のまとめ、管理されたアイデンティティを使用したリソースアクセスの制御に関する詳細な説明や、開発者が必要とする権限の割り当てについての情報も含まれています。

この新しいガイドは、Azure AI Studioを通じてデータを安全に使用し、適切なセキュリティ対策を講じるための重要なリソースとなることを目的としています。詳細な内容については、GitHubのリンクから確認できます。

## articles/ai-studio/media/data-connections/connection-add-azure-ai-search-connect-entra-id.png{#item-3aff1d}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイル名の変更: Azure AI Searchへの接続"
}
```

### Explanation
このコード変更は、画像ファイル「connection-add-azure-ai-search-connect.png」の名前を「connection-add-azure-ai-search-connect-entra-id.png」に変更したことを示しています。この変更により、画像の内容が具体的にMicrosoft Entra IDへの接続を示すことが反映されています。

変更の影響は、画像ファイル名の更新によって、関連文書内での画像の識別がより明確になることです。また、これにより、ユーザーが画像を参照する際に、Microsoft Entra IDとの関連を理解しやすくなります。

ファイルの内容自体には変更がないため、主に文書の可読性や理解の向上を目的とした調整となります。詳細な内容については、GitHubのリンクから確認できます。

## articles/ai-studio/media/data-connections/connections-all.png{#item-80f298}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイル名の変更: 接続の概要"
}
```

### Explanation
このコード変更は、「connections-all-refreshed.png」という画像ファイルの名前を「connections-all.png」に変更したことを示しています。この変更により、画像がより一般的な接続の概要を示すものとして認識されるようになります。

変更後のファイル名は、画像の内容との一貫性を保ちながら、関連する文書内での画像の識別を向上させる目的があります。具体的な内容や更新内容は変更されていないため、主にファイル名の明確化に関連する微小な修正となります。

詳細な内容は、GitHubのリンクから確認できます。

## articles/ai-studio/media/how-to/secure-playground-on-your-data/ai-search-managed-identity.png{#item-9d42bb}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: AI検索マネージドアイデンティティ"
}
```

### Explanation
このコード変更は、新しい画像ファイル「ai-search-managed-identity.png」が追加されたことを示しています。この画像は、「データ上のプレイグラウンドを安全にする方法」についての文書に関連しており、特にAI検索機能におけるマネージドアイデンティティの概念を視覚的に示しています。

新たに追加されたこの画像は、ユーザーがAI検索のマネージドアイデンティティを理解する手助けとなり、実際の利用シナリオや設定方法に関する情報を提供する役割を担います。この変更により、関連するガイドラインやチュートリアルがより充実したものとなり、利用者の理解を深めることが期待されます。

詳細な内容は、GitHubのリンクから確認できます。

## articles/ai-studio/media/how-to/secure-playground-on-your-data/ai-search-private-endpoint.png{#item-f5e3ff}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: AI検索プライベートエンドポイント"
}
```

### Explanation
このコード変更は、新たに「ai-search-private-endpoint.png」という画像ファイルが追加されたことを示しています。この画像は、「データ上のプレイグラウンドを安全にする方法」に関する文書に関連しており、特にAI検索のプライベートエンドポイントの設定や利用に関する情報を視覚的に提供します。

追加された画像は、プライベートエンドポイントの概念を説明するのに役立ち、利用者がこの機能を理解し、実装する際の助けとなることが期待されます。この変更により、関連するガイドラインやチュートリアルがさらに充実し、ユーザーの理解促進につながります。

詳細な内容は、GitHubのリンクから確認できます。

## articles/ai-studio/media/how-to/secure-playground-on-your-data/ai-search-public-access-disable.png{#item-086b7b}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: AI検索の公開アクセス無効化"
}
```

### Explanation
このコード変更は、「ai-search-public-access-disable.png」という新しい画像ファイルが追加されたことを示しています。この画像は、「データ上のプレイグラウンドを安全にする方法」に関連する文書内で、特にAI検索における公開アクセスの無効化についての情報を視覚的に支援するものです。

追加された画像は、ユーザーがAI検索サービスの公開アクセスをどのように無効にするかを理解しやすくするために設計されており、実際の設定手順や理由を明確に説明する役割を果たします。この変更は、ユーザーにとって安全なデータ管理を促進するものであり、関連するガイドやチュートリアルの情報をより充実させることが期待されます。

詳細な内容は、GitHubのリンクから確認できます。

## articles/ai-studio/media/how-to/secure-playground-on-your-data/ai-services-managed-identity.png{#item-fde1e6}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: AIサービスのマネージドアイデンティティ"
}
```

### Explanation
このコード変更は、「ai-services-managed-identity.png」という新しい画像ファイルが追加されたことを示しています。この画像は、「データ上のプレイグラウンドを安全にする方法」に関連する文書の一環として、AIサービスのマネージドアイデンティティの概念を視覚的に示すものです。

追加された画像は、ユーザーがマネージドアイデンティティを利用する目的や方法を理解するのを助けることを意図しており、AIサービスが安全に認証を行うための仕組みを説明しています。この変更により、ユーザーが関連するセキュリティ機能をより容易に把握できるようになり、実際の実装や活用において重要な参考資料となることが期待されます。

詳細な内容は、GitHubのリンクから確認できます。

## articles/ai-studio/media/how-to/secure-playground-on-your-data/ai-services-private-endpoint.png{#item-c0ff55}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: AIサービスのプライベートエンドポイント"
}
```

### Explanation
このコード変更は、「ai-services-private-endpoint.png」という新しい画像ファイルが追加されたことを表示しています。この画像は、「データ上のプレイグラウンドを安全にする方法」の文書に関連しており、AIサービスのプライベートエンドポイントに関する情報を視覚的に補足するものです。

追加された画像は、プライベートエンドポイントがユーザーのデータをどのように保護し、AIサービスに安全に接続するかを示す役割を果たします。これにより、ユーザーはこの重要な概念を理解しやすくなり、プライバシーとセキュリティを強化するための実践的な手段を見つけやすくなります。

詳細な内容は、GitHubのリンクから確認できます。

## articles/ai-studio/media/how-to/secure-playground-on-your-data/ai-services-public-access-disable.png{#item-0bf186}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: AIサービスのパブリックアクセスの無効化"
}
```

### Explanation
このコード変更は、「ai-services-public-access-disable.png」という新しい画像ファイルが追加されたことを示しています。この画像は、「データ上のプレイグラウンドを安全にする方法」に関連しており、AIサービスにおけるパブリックアクセスを無効化するプロセスを視覚的に示しています。

追加された画像は、ユーザーに対してAIサービスのセキュリティ強化のための手順を理解させることを目的としており、パブリックアクセスの無効化がデータ保護においてどれほど重要であるかを強調します。この変更により、ユーザーは安全な環境を構築するための具体的なアクションを把握しやすくなると期待されます。

詳細な内容は、GitHubのリンクから確認できます。

## articles/ai-studio/media/how-to/secure-playground-on-your-data/hub-public-access-disable.png{#item-2d67eb}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: ハブのパブリックアクセスの無効化"
}
```

### Explanation
このコード変更は、「hub-public-access-disable.png」という新しい画像ファイルが追加されたことを示しています。この画像は、「データ上のプレイグラウンドを安全にする方法」に関連しており、ハブにおけるパブリックアクセスを無効化する方法を視覚的に説明しています。

追加された画像は、ユーザーがハブに対するアクセスを制御し、セキュリティを向上させるための具体的な手順を理解するのに役立ちます。この変更により、データとリソースを保護するための効果的な施策として、パブリックアクセスの無効化の重要性が強調されます。

詳細な内容は、GitHubのリンクから確認できます。

## articles/ai-studio/media/how-to/secure-playground-on-your-data/private-endpoints.png{#item-94033b}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: プライベートエンドポイント"
}
```

### Explanation
このコード変更は、「private-endpoints.png」という新しい画像ファイルが追加されたことを示しています。この画像は、「データ上のプレイグラウンドを安全にする方法」に関連しており、プライベートエンドポイントの設定方法を視覚的に説明しています。

追加された画像は、ユーザーがプライベートエンドポイントを利用してデータセキュリティを向上させ、外部からの不正アクセスを防ぐための具体的な手順を理解するのに役立ちます。この変更により、プレイグラウンドのセキュリティを強化するための効果的な施策として、プライベートエンドポイントの利用の重要性が強調されます。

詳細な内容は、GitHubのリンクから確認できます。

## articles/ai-studio/media/how-to/secure-playground-on-your-data/search-api-access-control.png{#item-a7279f}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: 検索APIのアクセス制御"
}
```

### Explanation
このコード変更は、「search-api-access-control.png」という新しい画像ファイルが追加されたことを示しています。この画像は、「データ上のプレイグラウンドを安全にする方法」に関連しており、検索APIへのアクセス制御の方法を視覚的に説明しています。

追加された画像は、ユーザーが検索APIに対するアクセス権限をどのように管理し、データのセキュリティを確保するかを理解するのに役立ちます。この変更により、検索APIのアクセス制御がデータの保護において重要であることが強調され、ユーザーはより安全にデータを扱うことができるようになります。

詳細な内容は、GitHubのリンクから確認できます。

## articles/ai-studio/media/how-to/secure-playground-on-your-data/select-network-isolation-configuration.png{#item-8f7f08}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: ネットワーク隔離設定の選択"
}
```

### Explanation
このコード変更は、「select-network-isolation-configuration.png」という新しい画像ファイルが追加されたことを示しています。この画像は、「データ上のプレイグラウンドを安全にする方法」に関連しており、ネットワーク隔離設定を選択する手順を視覚的に説明しています。

追加された画像は、ユーザーがネットワーク隔離の設定を正しく行うための情報を提供し、データのセキュリティを強化するための重要な要素を示しています。この変更により、ユーザーは適切なネットワーク構成を選択し、データへのアクセスをより安全に管理することができます。

詳細な内容は、GitHubのリンクから確認できます。

## articles/ai-studio/media/how-to/secure-playground-on-your-data/storage-account-public-access-disable.png{#item-68fdda}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: ストレージアカウントのパブリックアクセスを無効にする"
}
```

### Explanation
このコード変更は、「storage-account-public-access-disable.png」という新しい画像ファイルが追加されたことを示しています。この画像は、「データ上のプレイグラウンドを安全にする方法」に関連しており、ストレージアカウントのパブリックアクセスを無効にする手順を視覚的に説明しています。

追加された画像は、ユーザーがストレージアカウントのセキュリティを強化するために、パブリックアクセスを正しく無効にする方法を理解するのに役立ちます。この変更によって、ユーザーは個人データや機密情報を保護し、アクセス管理の重要性を認識することができます。

詳細な内容は、GitHubのリンクから確認できます。

## articles/ai-studio/media/how-to/secure-playground-on-your-data/storage-private-endpoint.png{#item-8ffe01}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: ストレージのプライベートエンドポイント"
}
```

### Explanation
このコード変更は、「storage-private-endpoint.png」という新しい画像ファイルが追加されたことを示しています。この画像は、「データ上のプレイグラウンドを安全にする方法」に関連しており、ストレージサービスのプライベートエンドポイントを設定する手順を視覚的に説明しています。

追加された画像は、ユーザーがプライベートエンドポイントを使用してストレージのセキュリティを向上させる方法を理解するのに役立ちます。この変更により、ユーザーはデータアクセスをより厳格に制御し、セキュリティリスクを低減するための重要な情報を得ることができます。

詳細な内容は、GitHubのリンクから確認できます。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -316,6 +316,8 @@ items:
         href: how-to/configure-private-link.md
       - name: Configure custom DNS
         href: /azure/machine-learning/how-to-custom-dns?context=/azure/ai-studio/context/context
+      - name: Secure playground chat
+        href: how-to/secure-data-playground.md
       - name: Troubleshoot secure project connectivity
         href: how-to/troubleshoot-secure-connection-project.md
     - name: Data protection & encryption
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次に新しい項目を追加: セキュアなプレイグラウンドチャット"
}
```

### Explanation
このコード変更は、`toc.yml`ファイルの修正を示しており、目次に「Secure playground chat」という新しい項目が追加されました。これにより、ユーザーはセキュアなデータプレイグラウンドに関する情報に簡単にアクセスできるようになります。

この変更は、ユーザーがAIスタジオの記事をよりナビゲートしやすくするために行われました。新しい項目は、「how-to/secure-data-playground.md」というリンクに関連しており、セキュアなプレイグラウンドチャットの設定や使用方法についてのガイドラインを提供しています。

詳細な内容は、GitHubのリンクから確認できます。


