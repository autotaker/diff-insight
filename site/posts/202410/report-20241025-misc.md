---
date: '2024-10-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f8a58ce...MicrosoftDocs:edd8070
summary: この変更は、Azure AI Studioがオンプレミスリソースにアクセスする方法を明確にするための新しい文書を追加することに焦点を当てています。この文書では、アプリケーションゲートウェイを介して非Azureリソースに安全にアクセスするためのガイドラインが提供されています。また、新しい画像ファイルと目次の更新も行われています。破壊的な変更はありません。このアップデートにより、ユーザーはオンプレミスリソースへのアクセスを効率的に処理できるようになり、Azure
  AI Studioの機能が強化されました。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f8a58ce...MicrosoftDocs:edd8070){target="_blank"}

# ハイライト

このコード変更は、Azure AI Studioがオンプレミスリソースにアクセスする方法を明確にするための新しい文書「オンプレミスリソースへのアクセス方法」を追加することを中心としたアップデートです。この文書では、アプリケーションゲートウェイを介して非Azureリソースに安全にアクセスするガイドラインを提供しています。また、それに関連して新しい画像ファイルが追加され、目次ファイルにも新しい項目が追加されました。

## 新機能

1. **新しい文書の追加**: Azure AI Studioからオンプレミスリソースにアクセスするための方法を詳述した文書が新たに追加されました。これには、アプリケーションゲートウェイを設定する手順や、サポートされているリソース・制限事項に関する情報が含まれています。

2. **視覚素材の追加**: Azure AI Studioでのアプリケーションゲートウェイの使用方法を示す新しい画像が追加されました。これは、文書内での理解を補助することを目的としています。

## 破壊的変更

特に破壊的な変更は行われていません。すべての変更は新機能追加であり、既存の機能に対する影響はありません。

## その他の更新

1. **目次の更新**: 「オンプレミスリソースへの安全なアクセス」という新しい項目が目次に追加され、関連する文書にアクセスしやすくなりました。

# 洞察

この差分は、Azure AI Studioユーザーがオンプレミスリソースに対するアクセスを効率的に処理するためのクリティカルな追加として設計されています。クラウドベースのプラットフォームからオンプレミスリソースにアクセスすることは、多くの企業において不可欠な要件となっていますが、この新しい文書によって、そのプロセスが明確且つ安全に行えるようになります。

アプリケーションゲートウェイの利用は、オンプレミス環境のセキュリティを強化しつつ、クラウド環境との連携を可能にするため、システムアーキテクチャの重要な部分を占めます。文書は、ゲートウェイの設定方法から可能な制限やトラブルシューティングまでを包括的にカバーしており、ユーザーの理解を助ける視覚的な図も追加されているため、技術者にとって貴重なリソースとなるでしょう。

これにより、ユーザーは新しいセクションを活用して、Azure AI Studioをビジネスニーズに合わせて効率的にカスタマイズし、非Azure環境とシームレスに統合することができるようになりました。このアップデートは、Azure AI Studioの機能を大幅に強化するものであり、多様なIT環境における適用を見据えた戦略的改善と言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [access-on-premises-resources.md](#item-8e3926) | new feature | オンプレミスリソースへのアクセス方法 | added | 112 | 0 | 112 | 
| [ai-studio-app-gateway.png](#item-5525c3) | new feature | Azure AI Studio アプリゲートウェイの図 | added | 0 | 0 | 0 | 
| [toc.yml](#item-2745cd) | minor update | 目次への新しい項目の追加 | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/ai-studio/how-to/access-on-premises-resources.md{#item-8e3926}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,112 @@
+---
+title: How to access on-premises resources
+titleSuffix: Azure AI Studio
+description: Learn how to configure an Azure AI Studio managed network to securely allow access to your on-premises resources.
+manager: scottpolly
+ms.service: azure-ai-studio
+ms.topic: how-to
+ms.date: 10/24/2024
+ms.reviewer: meerakurup 
+ms.author: larryfr
+author: Blackmist
+# Customer intent: As an admin, I want to allow my developers to securely access on-premises resources from Azure AI Studio.
+---
+
+# Access on-premises resources from your Azure AI Studio's managed network (preview)
+
+To access your non-Azure resources located in a different virtual network or located entirely on-premises from your Azure AI Studio's managed virtual network, an Application Gateway must be configured. Through this Application Gateway, full end to end access can be configured to your resources.
+
+Azure Application Gateway is a load balancer that makes routing decisions based on the URL of an HTTPS request. Azure Machine Learning supports using an application gateway to securely communicate with non-Azure resources. For more on Application Gateway, see [What is Azure Application Gateway](/azure/application-gateway/overview).
+
+To access on-premises or custom virtual network resources from the managed virtual network, you configure an Application Gateway on your Azure virtual network. The application gateway is used for inbound access to the AI Studio's hub. Once configured, you then create a private endpoint from the Azure AI Studio hub's managed virtual network to the Application Gateway. With the private endpoint, the full end to end path is secured and not routed through the Internet.
+
+:::image type="content" source="../media/how-to/network/ai-studio-app-gateway.png" alt-text="Diagram of a managed network using Application Gateway to communicate with on-premises resources." lightbox="../media/how-to/network/ai-studio-app-gateway.png":::
+
+## Prerequisites
+
+- Read the [How an application gateway works](/azure/application-gateway/how-application-gateway-works) article to understand how the Application Gateway can secure the connection to your non-Azure resources. 
+- Set up your Azure AI Studio hub's managed virtual network and select your isolation mode, either Allow Internet Outbound or Allow Only Approved Outbound. For more information, see [Managed virtual network isolation](configure-managed-network.md).
+- Get the private HTTP(S) endpoint of the resource to access.
+
+## Supported resources
+
+Application Gateway supports any backend target resource that uses HTTP or HTTPS protocol. Connections to the following resources from the managed virtual network are verified:
+- Jfrog Artifactory
+- Snowflake Database
+- Private APIs
+
+## Configure Azure Application Gateway
+
+Follow the [Quickstart: Direct web traffic using the portal](/azure/application-gateway/quick-create-portal). To correctly set up your Application Gateway for use with Azure Machine Learning, use the following guidance when creating the Application Gateway:
+
+1. From the __Basics__ tab:
+
+    - Ensure your Application Gateway is in the same region as the selected Azure Virtual Network.
+    - Azure AI Studio only supports IPv4 for Application Gateway.
+    - With your Azure Virtual Network, select one dedicated subnet for your Application Gateway. No other resources can be deployed in this subnet.
+
+1. From the __Frontends__ tab, Application Gateway doesn’t support private Frontend IP address only so Public IP addresses need to be selected or a new one created. Private IP addresses for the resources that the gateway connects to can be added within the range of the subnet you selected on the Basics tab.
+
+1. From the __Backends__ tab, you can add your backend target to a backend pool. You can manage your backend targets by creating different backend pools. Request routing is based on the pools. You can add backend targets such as a Snowflake database. 
+
+1. From the __Configuration__ tab, you configure how requests are received with the frontend IPs and routed to the backend. 
+
+    - In the __Listener__ section:
+        - You can create a listener with either HTTP or HTTPS protocol and specify the port you want it to listen to. If you want two listeners listening on the same front-end IP address and routing to different backend pools, you need to choose different ports. Incoming requests are differentiated based on ports.
+        - If you want end-to-end TLS encryption, select HTTPS listener and upload your own certificate for Application Gateway to decrypt request received by listener. For more information, see [Enabling end to end TLS on Azure Application Gateway](/azure/application-gateway/ssl-overview#end-to-end-tls-encryption).
+        - If you want a fully private backend target without any public network access, DO NOT setup a listener on the public frontend IP address and its associated routing rule. Application Gateway only forwards requests that listeners receive at the specific port. If you want to avoid adding public frontend IP listener by mistake, see [Network security rules](/azure/application-gateway/configuration-infrastructure#network-security-groups) to fully lock down public network access.
+
+    - In the __Backend targets__ section, if you want to use HTTPS and Backend server’s certificate is NOT issued by a well-known CA, you must upload the Root certificate (.CER) of the backend server. For more on configuring with a root certificate, see [Configure end-to-end TLS encryption using the portal](/azure/application-gateway/end-to-end-ssl-portal).
+
+1. Once the Application Gateway resource is created, navigate to the new Application Gateway resource in the Azure portal. Under __Settings__, select, __Private link__ to enable a virtual network to privately access the Application Gateway through a private endpoint connection. The Private link configuration isn't created by default. 
+
+    - Select __+ Add__ to add the Private Link configuration, and then use the following values to create the configuration:
+        - Name: Provide a name for your private link configuration
+        - Private link subnet: Select a subnet in your virtual network. 
+        - Frontend IP Configuration: `appGwPrivateFrontendIpIPv4`
+    - To verify the Private link is set up correctly, navigate to the __Private endpoint connections__ tab and select __+ Private endpoint__. On the __Resource__ tab, the __Target sub-resource__ should be the name of your private Frontend IP configuration, `appGwPrivateFrontendIpIPv4`. If no value appears in the __Target sub-resource__, then the Application Gateway listener wasn't configured correctly. 
+
+## Configure private link
+
+1. Now that your Application Gateway’s front-end IP and backend pools are created, you can now configure the private endpoint from the managed virtual network to your Application Gateway. in the [Azure portal](https://portal.azure.com), navigate to your Azure AI Studio hub's __Networking__ tab. Select __Workspace managed outbound access__, __+ Add user-defined outbound rules__. 
+1. In the __Workspace Outbound rules__ form, select the following to create your private endpoint:
+
+    - Rule name: Provide a name for your private endpoint to Application Gateway.
+    - Destination Type: Private Endpoint
+    - Subscription and Resource Group: Select the Subscription and Resource Group where your Application Gateway is deployed
+    - Resource Type: `Microsoft.Network/applicationGateways`
+    - Resource name: The name of your Application Gateway resource.
+    - Sub resource: `appGwPrivateFrontendIpIPv4` 
+    - FQDNs: These FQDNs are the aliases that you want to use inside the Azure AI Studio. They're resolved to the managed private endpoint’s private IP address targeting Application Gateway. You might include multiple FQDNs depending on how many resources you would like to connect to with the Application Gateway.
+
+    > [!NOTE]
+    > - If you are using HTTPS listener with certificate uploaded, make sure the FQDN alias matches with the certificate's CN (Common Name) or SAN (Subject Alternative Name) otherwise HTTPS call will fail with SNI (Server Name Indication).
+    > - The provided FQDNs must have at least three labels in the name to properly create the private DNS zone of thee private endpoint for Application Gateway.
+    > - The FQDNs field is editable after the private endpoint creation through SDK or CLI. The field is not editable in the Azure portal.
+    > - Dyname sub-resource naming is not supported for the private Frontend IP configuration. The Frontend IP name must be `appGwPrivateFrontendIpIPv4`.
+
+### Configure using Python SDK and Azure CLI
+
+To create a private endpoint to Application Gateway with SDK, see [Azure SDK for Python](/python/api/azure-ai-ml/azure.ai.ml.entities.privateendpointdestination).
+
+To create a private endpoint to Application Gateway with the Azure CLI, use the `az ml workspace outbound-rule set` command. Set properties as needed for your configuration. For more information, see [Configure a managed network](configure-managed-network.md?tabs=azure-cli).
+
+## Limitations
+
+- Application Gateway supports only HTTP(s) endpoints in the Backend pool. There's no support for non-HTTP(s) network traffic. Ensure your resources support HTTP(S) protocol.
+- To connect to Snowflake using the Application Gateway, you should add your own FQDN outbound rules to enable package/driver download and OCSP validation.
+  - The Snowflake JDBC driver uses HTTPS calls, but different drivers might have different implementations. Check if your resource uses HTTP(S) protocol or not.
+- For more information on limitations, see [Frequently asked questions about Application Gateway](/azure/application-gateway/application-gateway-faq).
+
+## Application Gateway Errors
+
+For errors related to the Application Gateway connection to your backend resources, follow the existing Application Gateway documentation based on the errors you receive:
+
+- [Troubleshoot backend health issues in Application Gateway](/azure/application-gateway/application-gateway-backend-health-troubleshooting)
+- [Troubleshooting bad gateway errors in Application Gateway](/azure/application-gateway/application-gateway-troubleshooting-502)
+- [HTTP response codes in Application Gateway](/azure/application-gateway/http-response-codes)
+- [Understanding disabled listeners](/azure/application-gateway/disabled-listeners)
+
+## Related content
+
+- [Managed virtual network isolation](configure-managed-network.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "オンプレミスリソースへのアクセス方法"
}
```

### Explanation
この変更は、Azure AI Studioにおけるオンプレミスリソースへのアクセス方法について詳述した新しい文書の追加を示しています。文書は、アプリケーションゲートウェイを使用して非Azureリソースに安全にアクセスする方法に関するガイドラインを提供しています。

文書の主な内容には、以下のセクションが含まれています：
- **概要**: Azure AI Studioの管理ネットワークからオンプレミスリソースにアクセスするために、アプリケーションゲートウェイを設定する必要があることなどを説明しています。
- **前提条件**: アプリケーションゲートウェイの機能や、Azure AI Studioの管理仮想ネットワークの設定方法についての情報を提供しています。
- **サポートされるリソース**: HTTPまたはHTTPSプロトコルを使用するバックエンドターゲットリソースをリストアップしています。
- **Azureアプリケーションゲートウェイの構成**: アプリケーションゲートウェイの作成と設定のための手順を詳述しています。
- **制限事項**: サポートされている機能や制約について説明しています。
- **アプリケーションゲートウェイのエラー対応**: エラーに対するトラブルシューティングリンクを提供し、問題解決に役立つ情報を提供しています。

この新しい文書は、ユーザーがAzure AI Studioを使用して効率的にオンプレミスリソースにアクセスできるようにするための重要なリソースとなります。

## articles/ai-studio/media/how-to/network/ai-studio-app-gateway.png{#item-5525c3}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Studio アプリゲートウェイの図"
}
```

### Explanation
この変更は、Azure AI Studioのアプリケーションゲートウェイに関する新しい画像ファイルを追加したことを示しています。この画像は、Azure AI Studioの管理ネットワークがオンプレミスリソースとどのように通信するかを視覚的に示したもので、ドキュメント内での使用を目的としています。

画像は、以下の情報を含む可能性があります：
- アプリケーションゲートウェイの構成
- オンプレミスリソースとの接続の流れ
- セキュアな通信を実現するためのネットワークトポロジー

このビジュアルは、ユーザーがアプリケーションゲートウェイの利用方法を理解する際に役立つリソースとなり、ドキュメントの情報を補完する重要な要素です。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -331,6 +331,8 @@ items:
       href: how-to/configure-private-link.md
     - name: Secure playground chat
       href: how-to/secure-data-playground.md
+    - name: Securely access on-premises resources
+      href: how-to/access-on-premises-resources.md
     - name: Troubleshoot secure project connectivity
       href: how-to/troubleshoot-secure-connection-project.md
   - name: Data protection & encryption
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次への新しい項目の追加"
}
```

### Explanation
この変更は、Azure AI Studioに関する目次ファイル（toc.yml）に新しい項目を追加したことを示しています。この更新により、「オンプレミスリソースへの安全なアクセス」というトピックが目次に追加され、関連するドキュメントがより簡単に見つけられるようになりました。

具体的には、次のような変更が加わりました：
- 「オンプレミスリソースへの安全なアクセス」という新しいセクションが追加され、そのリンク先が「how-to/access-on-premises-resources.md」に設定されています。

この更新は、ユーザーに対してオンプレミスリソースへのアクセス方法に関する情報を強調し、Azure AI Studioの利用をより円滑にするための重要な改善です。


