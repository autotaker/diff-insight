---
date: '2025-04-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:869fffd...MicrosoftDocs:8f8bd66
summary: 今回のコード更新では、OpenAI関連のドキュメントに新機能が追加され、既存情報が微調整されました。主な変更点は、Azure OpenAIリソースを仮想ネットワーク内でプライベートエンドポイントを用いて保護する方法に関する新しいドキュメントの追加です。また、モデル情報やプロンプト変換に関する情報の更新も行われました。全体的に、ドキュメントの整合性やユーザーの理解を深めることを目的とした改訂がなされています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:869fffd...MicrosoftDocs:8f8bd66){target="_blank"}

<format>
# Highlights
今回のコード更新では、OpenAI関連のドキュメントにおいて様々な新機能の追加や既存情報の微調整が行われました。主要な新機能として、Azure OpenAIのリソースを仮想ネットワーク内でプライベートエンドポイントを利用して保護する方法に関する新しいドキュメントが追加され、複数の視覚資料も提供されています。また、モデル情報やプロンプト変換の適用範囲に関する情報の微調整が行われています。

## New features
- Azure OpenAIのリソースを仮想ネットワーク内でプライベートエンドポイントを用いて保護する新しいドキュメントの追加。
- プライベートエンドポイント、プライベートリンク、デプロイメント詳細、ネットワーク基礎などに関する新しい画像ファイルの追加。

## Breaking changes
特に重大な変更や互換性の問題を引き起こす変更は見られません。

## Other updates
- OpenAIのモデルにおける地域情報およびアクセス情報の微調整（例：「West US 2」から「West US 3」への変更）。
- プロンプト変換において、適用対象モデルを「DALL-E 3」のみに修正。
- ファインチューニングデプロイメントに新たに「GPT-4.1」ファインチューニングモデルの追加。
- 推論モデルのフットノート情報の修正。
- 画像編集APIの入力画像の説明を具体化。
- TOCにプライベートエンドポイント関連の新しい項目を追加。

# Insights
この一連の更新は、主にドキュメントの整合性とユーザーが利用する際の透明性と明確性を高めることを目的としています。新たなプライベートエンドポイント設定に関するガイダンスは、セキュリティを重視する企業や開発者にとって大きな利点を提供します。このドキュメントにより、リソースへのアクセス制御を強化し、セキュアなネットワーク構築を支援するための具体的な手順が示されています。視覚的な画像の追加は、複雑な設定手順の理解を助け、特に可視化によって学習したいユーザーにとって有用です。

また、モデル情報やプロンプト変換の情報が更新されたことで、ユーザーはサービスの最新の状態をより的確に把握し、自身のプロジェクトに適切な選択を行えるようになります。このような詳細情報のアップデートは、ドキュメント全体の信頼性を高め、ユーザーが安心してサービスを活用できる基盤を提供します。今後も、新たな機能や仕様変更に応じたドキュメントの更新が期待され、ユーザーの経験向上に努める姿勢が見受けられます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | モデル情報の更新 | modified | 2 | 2 | 4 | 
| [prompt-transformation.md](#item-21e047) | minor update | プロンプト変換に関する情報の修正 | modified | 2 | 2 | 4 | 
| [fine-tuning-deploy.md](#item-286d57) | minor update | ファインチューニングデプロイメントにおけるモデルリストの更新 | modified | 2 | 4 | 6 | 
| [network.md](#item-b0098f) | new feature | Azure OpenAIを仮想ネットワーク内でプライベートエンドポイントを使用して保護する方法 | added | 140 | 0 | 140 | 
| [reasoning.md](#item-a54b2f) | minor update | 推論モデルに関する情報の修正 | modified | 2 | 2 | 4 | 
| [latest-inference-preview.md](#item-24bf0f) | minor update | 画像編集APIの説明修正 | modified | 2 | 2 | 4 | 
| [fine-tune-models.md](#item-2aadea) | minor update | 微調モデルに関する情報の拡充 | modified | 8 | 6 | 14 | 
| [create-private-endpoint.png](#item-d35524) | new feature | プライベートエンドポイント作成手順の画像追加 | added | 0 | 0 | 0 | 
| [create-private-link.png](#item-eb2661) | new feature | プライベートリンク作成手順の画像追加 | added | 0 | 0 | 0 | 
| [deployment-details.png](#item-48a407) | new feature | デプロイメント詳細の画像追加 | added | 0 | 0 | 0 | 
| [network-basics.png](#item-5d467d) | new feature | ネットワーク基礎の画像追加 | added | 0 | 0 | 0 | 
| [network-disabled.png](#item-c8d3f3) | new feature | ネットワーク無効の画像追加 | added | 0 | 0 | 0 | 
| [private-endpoint.png](#item-d404da) | new feature | プライベートエンドポイントの画像追加 | added | 0 | 0 | 0 | 
| [toc.yml](#item-c945af) | minor update | TOCへの新しい項目の追加 | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -228,7 +228,7 @@ The image generation models generate images from text prompts that the user prov
 
 **For access to `gpt-image-1` registration is required, and access will be granted based on Microsoft's eligibility criteria**. Customers who have access to other limited access models will still need to request access for this model.
 
-Request access: [`computer-use-preview` limited access model application](https://aka.ms/oai/gptimage1access)
+Request access: [`gpt-image-1` limited access model application](https://aka.ms/oai/gptimage1access)
 
 Once access has been granted, you will need to create a deployment for the model.
 
@@ -237,7 +237,7 @@ Once access has been granted, you will need to create a deployment for the model
 | Model | Region |
 |---|---|
 |`dall-e-3` | East US<br>Australia East<br>Sweden Central|
-|`gpt-image-1` | West US 2 (Global Standard) <br> UAE North (Global Standard) |
+|`gpt-image-1` | West US 3 (Global Standard) <br> UAE North (Global Standard) |
 
 ## Audio models
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル情報の更新"
}
```

### Explanation
この変更は、OpenAIのモデルに関するドキュメントのマイナーな更新を含んでいます。具体的には、`gpt-image-1`モデルへのアクセスに関する情報が更新されました。元々の文では、モデルが「West US 2」と記載されていましたが、改訂後は「West US 3」と変更されました。また、`gpt-image-1`にアクセスするための申請セクションで、モデル名が明確に反映されるように修正されました。これにより、ユーザーが必要な情報をより理解しやすくなることを目的としています。全体として、文書の正確性と明確性を向上させるための微調整が行われました。

## articles/ai-services/openai/concepts/prompt-transformation.md{#item-21e047}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ manager: nitinme
 
 # What is prompt transformation?
 
-Prompt transformation is a process included in the DALL-E 3 and GPT-image-1 (preview) models that applies a safety and quality system message to your original prompt. It uses a large language model (LLM) call to add the message before sending your prompt to the model for image generation. This system message enriches your original prompt with the goal of generating more diverse and higher-quality images while maintaining intent. 
+Prompt transformation is a process included in the DALL-E 3 models that applies a safety and quality system message to your original prompt. It uses a large language model (LLM) call to add the message before sending your prompt to the model for image generation. This system message enriches your original prompt with the goal of generating more diverse and higher-quality images while maintaining intent. 
 
 After prompt transformation is applied to the original prompt, content filtering is applied as a secondary step before image generation; for more information, see [Content filtering](./content-filter.md).
 
@@ -34,7 +34,7 @@ Default prompt transformation contains safety enhancements that steer the model
 
 ## How do I use prompt transformation?
 
-Prompt transformation is applied by default to all Azure OpenAI DALL-E 3 and GPT-image-1 requests. No extra setup is required to benefit from prompt transformation enhancements.
+Prompt transformation is applied by default to all Azure OpenAI DALL-E 3 requests. No extra setup is required to benefit from prompt transformation enhancements.
 
 Like image generation, prompt transformation is non-deterministic due to the nature of large language models. A single original prompt may lead to many image variants.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプト変換に関する情報の修正"
}
```

### Explanation
この変更は、プロンプト変換に関するドキュメントのマイナーな更新を含みます。具体的には、プロンプト変換が適用されるモデルが更新されました。以前の記述では「DALL-E 3およびGPT-image-1（プレビュー）」モデルが言及されていましたが、これが「DALL-E 3」モデルのみに修正されました。この変更により、ユーザーがプロンプト変換の適用対象をより明確に理解できるようになります。他の内容は変更されておらず、プロンプト変換の目的や利用方法については引き続き同様の説明が提供されています。全体として、情報の正確性を向上させるための微調整が行われました。

## articles/ai-services/openai/how-to/fine-tuning-deploy.md{#item-286d57}

<details>
<summary>Diff</summary>
````diff
@@ -370,15 +370,15 @@ Azure OpenAI fine-tuning supports the following deployment types.
 
 | Models | Region |
 |--|--|
+|GPT-4.1-finetune|East US2, North Central US, and Sweden Central|
+|GPT-4.1-mini-finetune|East US2, North Central US, and Sweden Central|
 |GPT-4o-finetune|East US2, North Central US, and Sweden Central|
 |GPT-4o-mini-finetune|East US2, North Central US, and Sweden Central|
 
 [Global standard](./deployment-types.md#global-standard) fine-tuned deployments offer [cost savings](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/), but custom model weights may temporarily be stored outside the geography of your Azure OpenAI resource.
 
 :::image type="content" source="../media/fine-tuning/global-standard.png" alt-text="Screenshot of the global standard deployment user experience with a fine-tuned model." lightbox="../media/fine-tuning/global-standard.png":::
 
-Global Standard fine-tuned deployments currently support structured outputs only on GPT-4o.
-
 ### Provisioned Managed (preview)
 
 | Models | Region |
@@ -391,8 +391,6 @@ Global Standard fine-tuned deployments currently support structured outputs only
 
 [Provisioned managed](./deployment-types.md#provisioned) fine-tuned deployments offer [predictable performance](../concepts/provisioned-throughput.md) for fine-tuned deployments. As part of public preview, provisioned managed deployments may be created regionally via the data-plane [REST API](../reference.md#data-plane-inference) version `2024-10-01` or newer. See below for examples.
 
-Provisioned Managed fine-tuned deployments currently support structured outputs only on GPT-4o.
-
 #### Creating a Provisioned Managed deployment
 
 To create a new deployment, make an HTTP PUT call via the [Deployments - Create or Update REST API](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true). The approach is similar to performing [cross region deployment](#cross-region-deployment) with the following exceptions:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングデプロイメントにおけるモデルリストの更新"
}
```

### Explanation
この変更は、Azure OpenAIのファインチューニングデプロイメントに関するドキュメントの更新を含んでいます。主な変更点は、GPT-4.1ファインチューニングおよびGPT-4.1-miniファインチューニングモデルが新たに追加されたことです。これにより、ユーザーは利用可能なモデルの選択肢をより多く持つことになります。また、グローバルスタンダードのファインチューニングデプロイメントに関する情報が若干整理され、サポート対象モデルが明確に示されるようになりました。具体的には、Provisioned Managedタイプのデプロイメントに関する情報が削除され、より明確にファインチューニングに関する情報が整理されています。全体として、文書の内容を整理し、情報の透明性を向上させるための微調整が行われました。

## articles/ai-services/openai/how-to/network.md{#item-b0098f}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,140 @@
+---
+title: 'Securing Azure OpenAI inside a virtual network with private endpoints'
+titleSuffix: Azure OpenAI
+description: How to secure your Azure OpenAI resource inside a virtual network with private endpoints
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: how-to
+ms.date: 04/25/2025
+author: mrbullwinkle
+ms.author: mbullwin
+recommendations: false
+---
+
+# Configure Azure OpenAI networking
+
+In this article, learn how to create and connect to a secure Azure OpenAI resource. The steps in this article use an Azure Virtual Network to create a security boundary for your Azure OpenAI resource.
+
+After completing this article, you'll have the following architecture:
+
+- An Azure Virtual Network, with a subnet where your Azure OpenAI resource will reside.
+- An Azure OpenAI resource that uses a private endpoint to communicate using the virtual network.
+- Azure Bastion, which allows you to use your browser to securely communicate with the jump box VM inside the virtual network.
+- An Azure Virtual Machine that you can remotely connect to and access resources secured inside the virtual network.
+
+## Prerequisites
+
+Familiarity with Azure Virtual Networks and IP networking. If you aren't familiar, try the [Fundamentals of computer networking module](/training/modules/network-fundamentals/).  
+
+For more on networking in Azure AI Services resource, see [Configure Virtual Networks for Azure AI services](/azure/ai-services/cognitive-services-virtual-networks).
+
+## Create a virtual network
+
+To create a virtual network, use the following steps:
+
+1. In the [Azure portal](https://portal.azure.com), select the portal menu in the upper left corner. From the menu, select **+ Create a resource** and then enter **Virtual Network** in the search field. Select the Virtual Network entry, and then select **Create**.
+2. From the **Basics** tab, select the Azure subscription to use for this resource and then select or create a new resource group. Under Instance details, enter a friendly name for your virtual network and select the region to create it in.
+
+    :::image type="content" source="../media/how-to/network/network-basics.png" alt-text="Screenshot of virtual network setup." lightbox="../media/how-to/network/network-basics.png":::
+
+1. Accept the default settings for **Security** and IP **addresses**. A subnet titled "default" will be created for your virtual network. Best practice is to create another subnet to delegate all private endpoints.
+1. Select **Review + create**.
+1. Verify that the information is correct, and then select **Create**.
+
+## Create an Azure OpenAI resource
+
+1. In the Azure portal, select the portal menu in the upper left corner. From the menu, select **+ Create a resource** and then enter **Azure OpenAI**. Select the Azure OpenAI entry, and then select **Create**.
+2. From the Basics tab, select the Azure subscription to use for this resource and then select or create a new resource group. Under Instance details, enter a friendly name for your resource and select the region to create it in. The Azure OpenAI resource does not to be in the same region as your virtual network.
+3. Select **Review + create**.
+
+## Create a private endpoint and private DNS zone
+
+1. In the Azure portal, select the Azure OpenAI resource you created. In Resource Management, navigate to the Networking tab.
+2. Under Allow access from, select Disabled. Disabled ensures no networks can access this resource. Private endpoint connections will be the exclusive way to access this resource. Select Save to save the settings.
+
+    :::image type="content" source="../media/how-to/network/network-disabled.png" alt-text="Screenshot of resource network disabled UX." lightbox="../media/how-to/network/network-disabled.png":::
+
+1. Navigate to the Private endpoint connections tab and select **+ Private endpoint**. 
+
+    :::image type="content" source="../media/how-to/network/private-endpoint.png" alt-text="Screenshot of private endpoint connections tab." lightbox="../media/how-to/network/private-endpoint.png":::
+
+1. From the Basics tab, select the Azure subscription to use for this resource and then select or create a new resource group. Under Instance details, enter a name for your resource and select the region to create it in. The region you create the private network in must be the same as the region you chose to create your virtual network in. The network interface name will automatically use the name and will add "-nic".
+
+    :::image type="content" source="../media/how-to/network/create-private-endpoint.png" alt-text="Screenshot of create private endpoint." lightbox="../media/how-to/network/create-private-endpoint.png":::
+
+1. From the Resource tab, the Resource type should be `Microsoft.CognitiveServices/accounts`. For Target sub-resource, select **account**.
+
+1. From the Virtual Network tab, use the following values:
+   - Virtual network: The virtual network you created earlier.
+   - Subnet: default
+
+1. From the DNS tab, use the following values if you would like to use Azure Private DNS instead of custom DNS: 
+   - Integrate with private DNS zone: Yes
+   - Configurations name: privatelink-openai-azure-com
+   - Subscription: The same Azure subscription that contains the previous resources.
+   - Resource group: The same Azure resource group that contains the previous resources.
+
+    :::image type="content" source="../media/how-to/network/create-private-link.png" alt-text="Screenshot of create private link DNS tab." lightbox="../media/how-to/network/create-private-link.png":::
+
+1. Select **Review + create**. Verify that the information is correct, and then select **Create**.
+
+1. Once the private endpoint is created, you should see your private endpoint connection name, state, and description. You can select the link to the private endpoint and view further details on its DNS configuration.
+
+    
+    :::image type="content" source="../media/how-to/network/deployment-details.png" alt-text="Screenshot of deployment details post private link and endpoint deployment." lightbox="../media/how-to/network/deployment-details.png":::
+
+## Configure gateway and client for local network access
+
+To access the Azure OpenAI Service from your local or on-premises client machines, there are two approaches. One approach is to configure a virtual machine deployed in the same virtual network. Another approach is to configure Azure VPN Gateway and Azure VPN Client.
+
+For guidelines to set up a virtual network gateway for your virtual network, see [Tutorial – Create & manage a VPN gateway](/azure/vpn-gateway/tutorial-create-gateway-portal#VNetGateway). To add point-to-site configuration, and enable Microsoft Entra ID based authentication, see [Configure a VPN gateway for Microsoft Entra ID](/azure/vpn-gateway/openvpn-azure-ad-tenant#enable-authentication) authentication. Download the Azure VPN Client profile configuration package, unzip, and import the AzureVPN/azurevpnconfig.xml file to your Azure VPN client.
+
+Configure your local machine hosts file to point your resources host names to the private IPs in your virtual network. The hosts file is located at C:\Windows\System32\drivers\etc for Windows, and at /etc/hosts on Linux. Example: 10.0.0.5 contoso.openai.azure.com
+
+## Configure access through another hub and spoke architecture
+
+A common networking architecture adopted by enterprises is the Hub-spoke network topology. In this networking topology, the hub virtual network is the central network zone to control all ingress and egress traffic to the Internet while the spoke virtual network are host different types of workloads. Then, the hub and spoke virtual networks are peered. Peering is a networking feature that allows seamless connectivity between two Azure Virtual Networks in the same region or across different regions. Peering facilitates the sharing of resources, data, and services between virtual networks, enhancing application deployment flexibility and streamlining network architecture.
+
+To set up a basic hub and spoke architecture:
+
+1. Create a second virtual network in your Azure Subscription, your spoke virtual network. This virtual network does not need to be in the same region.
+2. In Settings, navigate to the **Peerings** tab. Select **+ Add**.
+3. Under Remote virtual network summary, provide a Peering Link Name and select the virtual network you will peer, in this case the Hub virtual network. Ensure `"Allow <hub virtual network name> to access <spoke virtual network name>"` is selected.
+4. Under Local virtual network summary, provide a Peering Link Name and ensure `"Allow <hub virtual network name> to access <spoke virtual network name>"` is selected. Then select Add. 
+
+## Configure your Network Security Group (NSG)
+
+Network Security Groups are used to control inbound and outbound traffic to network interfaces (NIC), VMs and subnets. You will need to configure NSG to allow traffic to and from Azure OpenAI. For more on configuring NSGs, see [Azure network security groups overview](/azure/virtual-network/network-security-groups-overview).
+
+## Testing your configuration
+
+You can test the network connection to Azure OpenAI using the Test-NetConnection cmdlet in PowerShell. This cmdlet allows you to test the network connection between your machine and another machine. It's a useful tool for network troubleshooting and debugging.
+
+1. Resolve the IP Address: Use the nslookup command to resolve the IP address of your Azure OpenAI endpoint. For example:
+
+   ```cmd
+   nslookup my-openai-instance.openai.azure.com
+   ```
+
+   This will return both public and private IP addresses associated with your Azure OpenAI instance. Your private IP address should be the same as the private IP seen in the DNS configuration of your private endpoint. 
+
+2. Test Private Endpoint: Next, test the network connection to the private IP address on port 443. For example:
+
+   ```powershell
+   Test-NetConnection 10.0.0.4 -Port 443
+   ```
+
+This command should succeed only from a machine that is on the same private network as your Azure OpenAI instance. If this command fails, it means there is a networking issue. Here are some possible causes:
+
+- DNS Issue: The Domain Name System (DNS) is responsible for translating domain names into IP addresses. If there's an issue with the DNS, it might not be able to correctly resolve the domain name of your Azure OpenAI instance to its IP address.
+
+- Machine Not on Private Network: If the machine you're running the command on is not on the same private network as your Azure OpenAI instance, the command will fail because it won't be able to reach the private IP address. Make sure that the machine is connected to the correct private network.
+
+- Customer Firewall Blocking: If there's a custom firewall set up between the machine and the Azure OpenAI instance, it might be blocking the connection. Firewalls are security measures that control incoming and outgoing network traffic based on predetermined security rules. You will need to check your firewall settings and make sure that traffic on port 443 is allowed.
+
+## Next steps
+
+- Explore the [Azure security baseline for Azure OpenAI](/security/benchmark/azure/baselines/azure-openai-security-baseline#virtual-network-integration)
+- Explore the various [Azure AI Services](/azure/ai-services/what-are-ai-services)
+- Learn how to [Configure Virtual Networks for Azure AI services](/azure/ai-services/cognitive-services-virtual-networks?tabs=portal)
+- [Azure OpenAI Private Endpoints: Connecting Across VNETs | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/azurearchitectureblog/azure-openai-private-endpoints-connecting-across-vnet%E2%80%99s/3913325)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIを仮想ネットワーク内でプライベートエンドポイントを使用して保護する方法"
}
```

### Explanation
この変更は、Azure OpenAIのリソースを仮想ネットワーク内でプライベートエンドポイントを使用して保護する方法を解説する新しいドキュメントを追加したものです。このドキュメントでは、Azure OpenAIリソースのセキュリティを確保するための手順が詳述されています。

主な内容としては、以下の項目が含まれています：

- Azure Virtual Networkの作成と接続に関する手順。
- Azure OpenAIリソースをプライベートエンドポイントを使用して設定する方法。
- ネットワークセキュリティグループ (NSG) を使用して、Azure OpenAIへのトラフィックを制御する方法。
- ローカルネットワークアクセス用のゲートウェイおよびクライアントの構成手順。
- ハブとスポークアーキテクチャにおけるネットワーク構成方法。

この新しい記事は、Azure OpenAIを使用する企業や開発者が、そのリソースを安全に管理し、アクセスするための貴重な情報を提供しています。全体として、このドキュメントはセキュアなネットワーク設定の重要性を強調し、実際の実装手順を明確に示しています。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -58,9 +58,9 @@ Azure OpenAI `o-series` models are designed to tackle reasoning and problem-solv
 
 <sup>2</sup> The latest o<sup>&#42;</sup> series model support system messages to make migration easier. When you use a system message with `o4-mini`, `o3`, `o3-mini`, and `o1` it will be treated as a developer message. You should not use both a developer message and a system message in the same API request.
 
-<sup>3</sup> Access to the chain-of-thought reasoning summary is limited access only for `o4-mini`.
+<sup>3</sup> Access to the chain-of-thought reasoning summary is limited access only for `o3` & `o4-mini`.
 
-<sup>4</sup> Streaming for `o3` is currently only supported for Enterprise subscriptions.
+<sup>4</sup> Streaming for `o3` is limited access only.
 
 ### Not Supported
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "推論モデルに関する情報の修正"
}
```

### Explanation
この変更は、Azure OpenAIの推論モデルに関する文書の一部を修正したものです。具体的には、いくつかのフットノートの内容が更新され、モデルのアクセス条件や機能に関連する情報が明確にされています。

主な変更点は以下の通りです：

- フットノートの表記が更新され、`o4-mini`モデルに加えて`o3`モデルでも「思考の連鎖推論」の要約にアクセスできるようになったことが示されました。
- `o3`モデルのストリーミング機能についての表記が修正され、従来は「エンタープライズサブスクリプションのみ」と書かれていたものが「制限付きアクセス」のみとされ、より正確な情報が提供されています。

これらの変更により、ユーザーは異なるモデルのアクセス制限や機能について、より正確に理解できるようになります。全体として、推論に関する情報はアップデートされ、ドキュメントの一貫性が向上しました。

## articles/ai-services/openai/includes/api-versions/latest-inference-preview.md{#item-24bf0f}

<details>
<summary>Diff</summary>
````diff
@@ -1357,7 +1357,7 @@ Generates an image based on an input image and text prompt instructions. Require
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| image | file | The input image to edit. Must be a valid image URL or base64-encoded image. tbd | Yes |  |
+| image | file | The input image to edit. Must be a valid image URL or base64-encoded image. | Yes |  |
 | n | integer | The number of images to generate. | No | 1 |
 | prompt | string | A text description of how the input image should be edited. The maximum length is 4000 characters. | Yes |  |
 | mask | file | A mask image to define the area of the input image that the model should edit, using fully transparent pixels (alpha of zero) in those areas. Must be a valid image URL or base64-encoded image. | No |  |
@@ -6195,7 +6195,7 @@ The style of the generated images.
 
 | Name | Type | Description | Required | Default |
 |------|------|-------------|----------|---------|
-| image | file | The input image to edit. Must be a valid image URL or base64-encoded image. tbd | Yes |  |
+| image | file | The input image to edit. Must be a valid image URL or base64-encoded image. | Yes |  |
 | n | integer | The number of images to generate. | No | 1 |
 | prompt | string | A text description of how the input image should be edited. The maximum length is 4000 characters. | Yes |  |
 | mask | file | A mask image to define the area of the input image that the model should edit, using fully transparent pixels (alpha of zero) in those areas. Must be a valid image URL or base64-encoded image. | No |  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像編集APIの説明修正"
}
```

### Explanation
この変更は、画像編集APIに関連するドキュメントの記述を修正したもので、特に入力画像に関する説明が明確化されました。具体的には、`image`フィールドの説明から「tbd」という表現が削除され、情報が整理されました。

主な変更点は以下の通りです：

- `image`フィールドの説明から「tbd」という不明な表現が除かれており、「有効な画像URLまたはbase64エンコードされた画像である必要があります」と言う具体的な説明が残されています。これにより、開発者が正確な入力形式を理解しやすくなります。

この修正により、APIユーザーは適切に画像を提供するための要件をより簡潔に把握できるようになり、ドキュメントの明瞭性が向上しています。全体として、APIの利用者にとって重要な情報がより正確に伝えられることになります。

## articles/ai-services/openai/includes/fine-tune-models.md{#item-2aadea}

<details>
<summary>Diff</summary>
````diff
@@ -15,9 +15,11 @@ manager: nitinme
 >
 > The supported regions for fine-tuning might vary if you use Azure OpenAI models in an Azure AI Foundry project versus outside a project.
 
-|  Model ID  | Fine-tuning regions | Max request (tokens) | Training Data (up to) |
-|  --- | --- | :---: | :---: |
-| `gpt-35-turbo` (1106) | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | Input: 16,385<br> Output: 4,096 |  Sep 2021|
-| `gpt-35-turbo` (0125)  | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | 16,385 | Sep 2021 |
-| `gpt-4o-mini` (2024-07-18) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 64,536 | Oct 2023 |
-| `gpt-4o` (2024-08-06) | East US2 <br> North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 64,536 | Oct 2023 | 
+|  Model ID  | Fine-tuning regions | Max request (tokens) | Training Data (up to) | Modality |
+|  --- | --- | :---: | :---: | --- |
+| `gpt-35-turbo` (1106) | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | Input: 16,385<br> Output: 4,096 |  Sep 2021 | Text to Text |
+| `gpt-35-turbo` (0125)  | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | 16,385 | Sep 2021 | Text to Text |
+| `gpt-4o-mini` (2024-07-18) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 65,536 | Oct 2023 | Text to Text |
+| `gpt-4o` (2024-08-06) | East US2 <br> North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 65,536 | Oct 2023 | Text & Vision to Text |
+| `gpt-4.1` (2025-04-14) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384 <br> Training example context length: 65,536 | May 2024 | Text to Text |
+| `gpt-4.1-mini` (2025-04-14) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384 <br> Training example context length: 65,536 | May 2024 | Text to Text |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "微調モデルに関する情報の拡充"
}
```

### Explanation
この変更は、微調整モデルに関するドキュメントを更新し、追加情報を提供することによって内容を拡充したものです。具体的には、微調整に関するテーブルに新しい列が追加され、各モデルの「モダリティ」に関する情報が含まれるようになりました。

主な変更点は以下の通りです：

- テーブルの構造が変更され、新たに「モダリティ」列が追加されました。これにより、各モデルがどのような形式のデータを処理するか（例：テキストからテキスト、テキストとビジョンからテキストなど）を明示しています。
- 新しいモデル`gpt-4.1`と`gpt-4.1-mini`が追加され、これらのモデルに関する微調整地域やリクエストの最大トークン数、トレーニングデータの情報が提供されています。

この更新によって、ユーザーは各モデルの特徴や利用可能な地域、モダリティについて、より包括的な理解を得られるようになり、ドキュメントの有用性が向上します。

## articles/ai-services/openai/media/how-to/network/create-private-endpoint.png{#item-d35524}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "プライベートエンドポイント作成手順の画像追加"
}
```

### Explanation
この変更は、プライベートエンドポイントを作成する手順に関連する新たな画像ファイルをドキュメントに追加したものです。ファイル名は「create-private-endpoint.png」で、ユーザーにビジュアルガイドを提供するためのものです。

主なポイントは以下の通りです：

- 画像が追加されたことにより、ユーザーはプライベートエンドポイントの作成プロセスを視覚的に理解しやすくなります。
- 画像のリンクは、GitHubリポジトリ内の該当フォルダーにあり、ダイレクトにプレビューが可能です。

この追加により、特に視覚的な情報を好むユーザーにとって、ドキュメントの利用価値が向上し、自学自習を助けるものとなります。

## articles/ai-services/openai/media/how-to/network/create-private-link.png{#item-eb2661}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "プライベートリンク作成手順の画像追加"
}
```

### Explanation
この変更は、プライベートリンクを作成する手順に関する新しい画像ファイルをドキュメントに追加したものです。ファイル名は「create-private-link.png」であり、ビジュアルガイドを提供することを目的としています。

主なポイントは以下の通りです：

- この画像が追加されたことにより、ユーザーはプライベートリンク作成のプロセスをより容易に理解できるようになり、複雑な手順を視覚的にサポートします。
- 画像のリンクは、GitHubのリポジトリ内にあり、ユーザーは必要に応じてアクセスしてプレビューすることが可能です。

これにより、特に視覚的な情報に依存する学習者にとって、ドキュメントの使い勝手が向上し、手順の明確さが増すことになります。

## articles/ai-services/openai/media/how-to/network/deployment-details.png{#item-48a407}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "デプロイメント詳細の画像追加"
}
```

### Explanation
この変更は、デプロイメントの詳細に関連する新しい画像ファイルをドキュメントに追加したものです。ファイル名は「deployment-details.png」であり、ユーザーに対して視覚的な情報を提供する目的があります。

主なポイントは以下の通りです：

- この画像の追加により、デプロイメントプロセスに関する理解が深まるとともに、特に複雑な設定や手順を視覚的に示すことで、ユーザーにとっての利便性が向上します。
- 画像はGitHubのリポジトリ内にホストされており、ユーザーは必要に応じて簡単にアクセスしてプレビューすることができます。

この変更により、ユーザーはデプロイメントに関する手順をより具体的に理解しやすくなり、全体的なドキュメントの質が向上することが期待されます。

## articles/ai-services/openai/media/how-to/network/network-basics.png{#item-5d467d}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ネットワーク基礎の画像追加"
}
```

### Explanation
この変更は、ネットワークの基礎に関連する新しい画像ファイルをドキュメントに追加したものです。ファイル名は「network-basics.png」であり、ユーザーに基礎的な概念を視覚的に示すことを目的としています。

主なポイントは以下の通りです：

- 新しい画像の追加により、ネットワークの基本的な概念を理解するためのビジュアルサポートが提供されます。これにより、特に初心者のユーザーが内容を把握しやすくなります。
- 画像はGitHubのリポジトリに保存されており、ユーザーは容易にアクセスし、プレビューすることができます。

この変更により、ドキュメントの教育的価値が向上し、ユーザーがネットワークに関する知識を効果的に習得できるようになります。

## articles/ai-services/openai/media/how-to/network/network-disabled.png{#item-c8d3f3}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ネットワーク無効の画像追加"
}
```

### Explanation
この変更は、ネットワークが無効である状態を示す新しい画像ファイルをドキュメントに追加したものです。ファイル名は「network-disabled.png」であり、特定の状況下でのネットワーク状態を明示的に説明することを目的としています。

主なポイントは以下の通りです：

- 新しく追加された画像により、ユーザーはネットワークが無効な状態について視覚的な理解を得ることができ、特にトラブルシューティングや設定に役立つ情報が提供されます。
- 画像は、GitHubリポジトリにホストされているため、ユーザーは容易にアクセスでき、必要に応じて確認することができます。

この変更は、ユーザーがネットワークの状態をより明確に理解し、適切に対処できるよう支援することを目的としています。

## articles/ai-services/openai/media/how-to/network/private-endpoint.png{#item-d404da}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "プライベートエンドポイントの画像追加"
}
```

### Explanation
この変更は、プライベートエンドポイントに関連する新しい画像ファイルをドキュメントに追加したものです。ファイル名は「private-endpoint.png」であり、プライベートエンドポイントの概念を視覚的に示すことを目的としています。

主なポイントは以下の通りです：

- 新しく追加された画像は、プライベートエンドポイントの設定や動作に関する理解を深めるためのビジュアルサポートを提供します。これにより、ユーザーはこの特定のネットワーク構造をよりよく理解できるようになります。
- 画像は、GitHubのリポジトリに保存されており、ユーザーは簡単にアクセス可能で、必要に応じて詳細を確認することができます。

この変更によって、ドキュメントの教育的価値が向上し、特にプライベートエンドポイントについての知識を得たいユーザーにとって有益な情報が提供されます。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -223,6 +223,8 @@ items:
     items:
       - name: Use virtual networks
         href: ../cognitive-services-virtual-networks.md?context=/azure/ai-services/openai/context/context
+      - name: Virtual networks with private endpoints
+        href: ./how-to/network.md        
       - name: Encryption of data at rest
         href: encrypt-data-at-rest.md
       - name: Managed identity
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCへの新しい項目の追加"
}
```

### Explanation
この変更は、TOC（目次）ファイル「toc.yml」に新しい項目を追加したもので、特にプライベートエンドポイントを使用した仮想ネットワークに関連する内容を含んでいます。具体的には、以下の2つの追加が行われています。

- 「Virtual networks with private endpoints」という名称の項目が新たに追加されました。この項目は、プライベートエンドポイントを使用した仮想ネットワークに関する情報へナビゲートするためのリンクです。
- これにより、ユーザーは関連するドキュメントを簡単に見つけることができ、プライベートエンドポイントに関連する設定や利用方法についての理解を深める手助けとなります。

この変更は、特定のトピックに関する情報を目次に加えることで、ユーザーが必要な情報にアクセスしやすくするためのマイナーな更新です。


