---
date: '2025-01-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:985f323...MicrosoftDocs:fee2fd2
summary: この変更の主なハイライトとして、新しい記事と視覚的なコンテンツの追加、および更新された注意事項が含まれています。新しい画像ファイルが複数追加され、技術的な概念をより直感的に理解できるようになりました。また、`ms.date`の更新や注意事項の追加により、文書の最新性と利用者の理解が高められています。特に、Azure
  Functionsに関する新しい記事では、カスタムWeb APIのホスティング手順やMicrosoft Entra IDを用いた認証の設定について詳細が説明されています。これにより、ユーザーはAzure
  Functionsの認証と接続に関する技術的課題を簡単に解決できるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:985f323...MicrosoftDocs:fee2fd2){target="_blank"}

# Highlights
この変更の主なハイライトとして、新しい記事と視覚的なコンテンツの追加、および更新された注意事項が含まれます。新しい画像ファイルが複数追加され、ユーザーが技術的な概念をより直感的に理解できるようになりました。また、`ms.date`の更新や注意事項の追加により、文書の最新性と利用者の理解が高められています。

## New features
- 「Managed Identities for Azure Functions」に関する新しい記事が追加され、Azure Functionsへのインデクサ接続設定に関する詳細な説明が提供されました。
- Azure Functionsに関連する複数の新しい画像が追加され、パーミッションや認証などのプロセスが視覚的に説明されています。

## Breaking changes
なし

## Other updates
- `ms.date`の日付が2025年1月9日から1月22日に更新されました。
- Azure AIリソースのプライベートエンドポイント設定に関する注意事項が追加されました。
- ドキュメント目次（`toc.yml`）が更新され、Azure Functionsへの接続に関する項目が追加されました。

# Insights
この変更は、Azure Functionsとその関連する認証、設定プロセスに対する理解を深めるのに役立つ内容が大幅に強化されています。新しい記事では、Azure Functionsを利用したカスタムWeb APIのホスティングに必要な手順が詳細に説明されており、特にMicrosoft Entra IDを用いた認証の設定が明記されています。

追加された画像による視覚的説明は、技術的プロセスを概念的に捉えるのを容易にし、特に初心者にとって有用です。ユーザーは、具体的な設定やAPIの使用方法を視覚的に把握できるため、効率的に作業を進めることができます。

また、ドキュメント内の情報の最新性を保つために、更新された注意事項や日付の修正は重要です。特にプライベートエンドポイント設定に関する注意事項の更新は、セキュリティの観点から重要で、ユーザーが最新のセキュリティ要件を誰にでもわかりやすく理解できるようにしています。

これらの追加と更新により、Azureの技術的ドキュメントがより理解しやすく、実用的なものになっています。ユーザーは、これを通じてAzure Functionsの認証と接続における技術的課題を簡単に解決できるようになるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | 変更された日付と注意事項の更新 | modified | 2 | 2 | 4 | 
| [api-permissions.png](#item-3018f7) | new feature | API Permissionsの画像追加 | added | 0 | 0 | 0 | 
| [app-registration-overview.png](#item-88e2aa) | new feature | アプリ登録の概要の画像追加 | added | 0 | 0 | 0 | 
| [authentication-supported-account.png](#item-ad13b9) | new feature | 認証サポートアカウントの画像追加 | added | 0 | 0 | 0 | 
| [client-secret.png](#item-72069e) | new feature | クライアントシークレットの画像追加 | added | 0 | 0 | 0 | 
| [expose-api-user-impersonation.png](#item-2eab03) | new feature | APIユーザーなりすましの画像追加 | added | 0 | 0 | 0 | 
| [function-app-authentication.png](#item-b5bfe7) | new feature | Function App認証の画像追加 | added | 0 | 0 | 0 | 
| [identity-provider.png](#item-36d458) | new feature | アイデンティティプロバイダーの画像追加 | added | 0 | 0 | 0 | 
| [search-identity-entra.png](#item-c30fea) | new feature | Search Identity Entraの画像追加 | added | 0 | 0 | 0 | 
| [search-service-identity.png](#item-e7e1bd) | new feature | サービス アイデンティティの画像追加 | added | 0 | 0 | 0 | 
| [search-howto-managed-identities-azure-functions.md](#item-2f13c4) | new feature | Azure Functionsへのインデクサ接続設定に関する新しい記事の追加 | added | 139 | 0 | 139 | 
| [toc.yml](#item-c4768f) | minor update | Azure Functionsへの接続に関する項目の追加 | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: how-to
-ms.date: 01/09/2025
+ms.date: 01/22/2025
 ---
 
 # Attach an Azure AI multi-service resource to a skillset in Azure AI Search
@@ -37,7 +37,7 @@ To attach an Azure AI multi-resource, you must provide connection information in
 + Connectivity over a public endpoint, unless your search service meets the creation date, tier, and region requirements for private connections to an Azure AI multi-service account.
 
 > [!NOTE]
-> If your Azure AI resource is configured to use a private endpoint, Azure AI Search can connect [using a shared private link](search-indexer-howto-access-private.md) if the search service was created after April 3, 2024 and is in a region that provides higher capacity computing power and is on a supported tier. For more information, see the requirements for using shared private links.
+> If your Azure AI resource is configured to use a private endpoint, Azure AI Search can connect [using a shared private link](search-indexer-howto-access-private.md) For more information, see the [requirements and limits for using shared private links](search-limits-quotas-capacity.md#shared-private-link-resource-limits).
 
 ## Bill through a keyless connection
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "変更された日付と注意事項の更新"
}
```

### Explanation
この変更では、文書「Cognitive SearchでのCognitive Servicesの接続」において、更新された日付と注意事項に関する情報が調整されました。具体的には、`ms.date`の値が2025年1月9日から2025年1月22日に変更されました。また、注記の部分では、Azure AIリソースがプライベートエンドポイントを使用するように設定されている場合の接続方法に関する情報が追加され、共有プライベートリンクの使用に関する要件のリンクが更新されました。これにより、ユーザーは最新の条件や制限についてより明確に理解できるようになります。

## articles/search/media/search-howto-managed-identities-azure-functions/api-permissions.png{#item-3018f7}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "API Permissionsの画像追加"
}
```

### Explanation
この変更では、記事「Managed Identities for Azure Functionsでの検索」に関連する新しい画像ファイル `api-permissions.png` が追加されました。この画像は、Azure FunctionsにおけるAPIの権限設定に関する視覚的な情報を提供することを目的としています。画像の追加により、ユーザーはリソースの設定やパーミッションの管理を理解しやすくなります。これは、今後のユーザー体験を向上させる新機能の一環として位置付けられます。

## articles/search/media/search-howto-managed-identities-azure-functions/app-registration-overview.png{#item-88e2aa}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "アプリ登録の概要の画像追加"
}
```

### Explanation
この変更では、記事「Managed Identities for Azure Functionsでの検索」に対して新しい画像ファイル `app-registration-overview.png` が追加されました。この画像は、Azure Functionsにおけるアプリ登録の概要を視覚的に示すことを目的としています。画像の追加により、ユーザーはアプリの登録プロセスや関連する設定をより理解しやすくなります。これは、ユーザーの理解を深めるための有用なリソースとして機能します。

## articles/search/media/search-howto-managed-identities-azure-functions/authentication-supported-account.png{#item-ad13b9}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "認証サポートアカウントの画像追加"
}
```

### Explanation
この変更では、記事「Managed Identities for Azure Functionsでの検索」に新しい画像ファイル `authentication-supported-account.png` が追加されました。この画像は、Azure Functionsにおいてサポートされる認証アカウントの種類を視覚的に示すものです。画像の導入によって、ユーザーは異なる認証オプションやその使用方法をより明確に理解できるようになります。これにより、各認証方法の適用シナリオを理解する助けとなり、全体的なユーザー体験の向上に寄与します。

## articles/search/media/search-howto-managed-identities-azure-functions/client-secret.png{#item-72069e}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "クライアントシークレットの画像追加"
}
```

### Explanation
この変更では、記事「Managed Identities for Azure Functionsでの検索」に新たに画像ファイル `client-secret.png` が追加されました。この画像は、Azure Functionsでのクライアントシークレットの概念を視覚的に示すために作成されました。ユーザーはこの画像を通じて、クライアントシークレットの設定や管理方法をより効果的に理解できるようになります。結果として、画像による視覚的な情報提供が、特定の技術的なプロセスの理解を容易にし、全体的な文書の質を向上させる役割を果たします。

## articles/search/media/search-howto-managed-identities-azure-functions/expose-api-user-impersonation.png{#item-2eab03}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "APIユーザーなりすましの画像追加"
}
```

### Explanation
この変更では、記事「Managed Identities for Azure Functionsでの検索」に新しく画像ファイル `expose-api-user-impersonation.png` が追加されました。この画像は、APIユーザーなりすましの概念を視覚的に説明するために設計されています。ユーザーはこの画像によって、APIの利用におけるユーザーなりすましの方法や関連する設定を理解しやすくなります。この視覚資料の追加は、技術的な内容をより明確にし、ドキュメント全体の有用性を向上させます。

## articles/search/media/search-howto-managed-identities-azure-functions/function-app-authentication.png{#item-b5bfe7}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Function App認証の画像追加"
}
```

### Explanation
この変更により、記事「Managed Identities for Azure Functionsでの検索」に新たに画像ファイル `function-app-authentication.png` が追加されました。この画像は、Function Appの認証に関するプロセスを視覚的に説明するために作成されています。ユーザーはこの視覚資料を通じて、Function Appの認証メカニズムをより直感的に理解できるようになります。画像の追加は、技術的な概念をよりわかりやすく伝える手助けをし、全体的なドキュメントの価値を向上させるものです。

## articles/search/media/search-howto-managed-identities-azure-functions/identity-provider.png{#item-36d458}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "アイデンティティプロバイダーの画像追加"
}
```

### Explanation
この変更では、記事「Managed Identities for Azure Functionsでの検索」にアイデンティティプロバイダーを示す新しい画像ファイル `identity-provider.png` が追加されました。この画像は、アイデンティティプロバイダーの役割と機能を視覚的に示すことを目的としています。ユーザーはこのビジュアルを利用することで、アイデンティティプロバイダーの重要性と、それがAzure Functionsにおける認証とアクセス制御にどのように寄与するかをより容易に理解できるようになります。この追加により、ドキュメントの説明が強化され、技術的な内容がさらに明確になっています。

## articles/search/media/search-howto-managed-identities-azure-functions/search-identity-entra.png{#item-c30fea}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Search Identity Entraの画像追加"
}
```

### Explanation
この変更により、記事「Managed Identities for Azure Functionsでの検索」に新たに画像ファイル `search-identity-entra.png` が追加されました。この画像は、Search Identity Entraの概念や機能を視覚的に説明するために使用されます。ユーザーは、この画像を通じてSearch Identity EntraがAzure Functions内でどのように機能するのかをより深く理解できるようになります。この新しいビジュアルの追加は、ドキュメントにおける技術的な説明を補完し、内容の理解を促進する効果があります。

## articles/search/media/search-howto-managed-identities-azure-functions/search-service-identity.png{#item-e7e1bd}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "サービス アイデンティティの画像追加"
}
```

### Explanation
この変更では、記事「Managed Identities for Azure Functionsでの検索」に対して新しい画像ファイル `search-service-identity.png` が追加されました。この画像は、サービス アイデンティティの役割とその機能を視覚的に説明するために設計されています。ユーザーはこのビジュアルを利用することで、サービス アイデンティティがAzure Functionsにおける認証やアクセス管理の中でどのように機能するかを理解しやすくなります。この追加により、ドキュメント全体の理解を助け、技術的な内容をより明確にする役割を果たします。

## articles/search/search-howto-managed-identities-azure-functions.md{#item-2f13c4}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,139 @@
+---
+title: Set up an indexer connection to Azure functions using "Easy Auth"
+titleSuffix: Azure AI Search
+description: Learn how to set up an indexer connection to an Azure Function using built-in authentication also known as "Easy Auth".
+author: arv100kri
+ms.author: arjagann
+
+ms.service: azure-ai-search
+ms.topic: how-to
+ms.date: 01/20/2025
+ms.custom:
+  - subject-rbac-steps
+---
+
+# Authenticate to Azure Function App using "Easy Auth" (Azure AI Search)
+
+This article explains how to set up an indexer connection to an Azure Function app using the [built-in authentication capabilities of App services](/azure/app-service/overview-authentication-authorization), also known as "Easy Auth". Azure Function apps are a great solution for hosting Custom Web APIs that an Azure AI Search service can use either to enrich content ingested during an indexer run, or to vectorize content in a search query if you're using a custom embedding model for [integrated vectorization](vector-search-integrated-vectorization.md).
+
+You can use either a system-assigned or a user-assigned identity of the search service to authenticate against the Azure Function app. This approach requires setting up a Microsoft Entra ID application registration to use as the authentication provider for the Azure Function app, as explained in this article.
+
+## Prerequisites
+
+* [Create a managed identity](search-howto-managed-identities-data-sources.md) for your search service.
+
+## Configure Microsoft Entra ID application to use as authentication provider
+
+To use Microsoft Entra ID as an authentication provider to the Azure Function app, an application registration must be created. There are 2 options to do so - either creating one automatically via the Azure Function app itself, or using an already created existing application. To learn more about these steps follow [Azure App services' documentation](/azure/app-service/configure-authentication-provider-aad?tabs=workforce-configuration#choose-the-app-registration.md).
+
+Regardless of either option, ensure that the app registration is configured per the following steps to ensure it being compatible with Azure AI Search.
+
+### Ensure the app registration has application ID URI configured
+
+The app registration should be configured with an application ID URI, which can then be used as the token audience with Azure Function apps and Azure AI Search. Configure it in the format `api://<applicationId>`. This can be done by navigating to the **Overview** section of the app registration and setting the **Application ID URI** field.
+
+[ ![Screenshot of an app registration configured with application ID URI.](./media/search-howto-managed-identities-azure-functions/app-registration-overview.png) ](./media/search-howto-managed-identities-azure-functions/app-registration-overview.png#lightbox)
+
+### Set supported account types for authentication
+
+Navigate to the **Authentication** section of the app registration and configure the **supported account types** so that only accounts in the same organization directory as the app registration can utilize it for authentication.
+
+[ ![Screenshot of an app registration with supported account types configured.](./media/search-howto-managed-identities-azure-functions/authentication-supported-account.png) ](./media/search-howto-managed-identities-azure-functions/authentication-supported-account.png#lightbox)
+
+### (Optional) Configure a client secret
+
+App services recommend utilizing a client secret for the authentication provider application. Authentication still works without client secret, as long as the delegated permissions are set up. To set up a client secret, navigate to the **Certificates & secrets** section of the app registration, and add a **New client secret** as explained [in this article](/entra/identity-platform/quickstart-register-app?tabs=client-secret#add-credentials).
+
+[ ![Screenshot of an app registration with option to configure client secret.](./media/search-howto-managed-identities-azure-functions/client-secret.png) ](./media/search-howto-managed-identities-azure-functions/client-secret.png#lightbox)
+
+### Add a scope to delegate permissions
+
+Navigate to the section **Expose an API** and configure the app registration to have a scope that delegates admin and user permissions to it, to ensure that it's compatible with the indexer's authentication flow.
+
+[ ![Screenshot of an app registration that delegates permission scope.](./media/search-howto-managed-identities-azure-functions/expose-api-user-impersonation.png) ](./media/search-howto-managed-identities-azure-functions/expose-api-user-impersonation.png#lightbox)
+
+Once the delegated permissions scope is set up, you should notice in the **API permissions** section of the app registration that the **User.Read** API on Microsoft.Graph is set.
+
+[ ![Screenshot of an app registration with delegated permissions.](./media/search-howto-managed-identities-azure-functions/api-permissions.png) ](./media/search-howto-managed-identities-azure-functions/api-permissions.png#lightbox)
+
+## Configure Microsoft Entra ID authentication provider in Azure Function app
+
+With the client application registered with the exact specifications above, Microsoft Entra ID authentication for the Azure Function app can be set up by following the [guide from App Services](/azure/app-service/configure-authentication-provider-aad). Navigate to the **Authentication** section of the Azure Function app to set up the authentication details.
+
+Ensure the following settings are configured to ensure that Azure AI Search can successfully authenticate to the Azure Function app.
+
+### Configure authentication settings
+
+* Ensure that **App Service authentication** is **Enabled**
+* Restrict access to the Azure Function app to **Require authentication**
+* For **Unauthenticated requests** prefer **HTTP 401: Unauthorized**
+
+The following screenshot highlights these specific settings for a sample Azure Function app.
+
+[ ![Screenshot of an Azure Function app that has configured authentication settings.](./media/search-howto-managed-identities-azure-functions/function-app-authentication.png) ](./media/search-howto-managed-identities-azure-functions/function-app-authentication.png#lightbox)
+
+### Add Microsoft Entra ID authentication provider
+
+* Add Microsoft Entra ID as the authentication provider for the Azure Function app.
+* Either create a new app registration or choose a previously configured app registration. Ensure that it's configured according to the guidelines in the previous section of this document.
+* Ensure that in the **Allowed token audiences** section, the application ID URI of the app registration is specified. It should be in the `api://<applicationId>` format, matching what was configured with the app registration created earlier.
+* If you desire, you can configure additional checks to restrict access specifically to the indexer. 
+
+[ ![Screenshot of an Azure Function app with Microsoft Entra ID Authentication provider.](./media/search-howto-managed-identities-azure-functions/identity-provider.png) ](./media/search-howto-managed-identities-azure-functions/identity-provider.png#lightbox)
+
+### Configure additional checks
+
+* Ensure that the **Object (principal) ID** of the specific Azure AI Search service's identity is specified as the **Identity requirement**, by checking the option **Allow requests from specific identities** and entering the **Object (principal) ID** in the identity section.
+
+[ ![Screenshot of the identity section for an Azure AI Search service.](./media/search-howto-managed-identities-azure-functions/search-service-identity.png) ](./media/search-howto-managed-identities-azure-functions/search-service-identity.png#lightbox)
+
+* In **Client application requirement** select the option **Allow requests from specific client application**. You need to look up the Client ID for the Azure AI Search service's identity. To do this, copy over the Object (principal) ID from the previous step and look up in your Microsoft Entra ID tenant. There should be a matching enterprise application whose overview page lists an **Application ID**, which is the GUID that needs to be specified as the client application requirement.
+
+[ ![Screenshot of the enterprise application details of an Azure AI Search service's identity.](./media/search-howto-managed-identities-azure-functions/search-identity-entra.png) ](./media/search-howto-managed-identities-azure-functions/search-identity-entra.png#lightbox)
+
+
+>[!NOTE]
+> This step is the most important configuration on the Azure Function app and doing it wrongly can result in the indexer being forbidden from accessing the Azure Function app. Ensure that you perform the lookup of the identity's enterprise application details correctly, and you specify the **Application ID** and **Object (principal) ID** in the right places.
+
+* For the **Tenant requirement**, choose any of the options that aligns with your security posture. Check out the [Azure App service documentation](/azure/app-service/configure-authentication-provider-aad) for more details.
+
+## Setting up a connection to the Azure Function app
+
+Depending on whether the connection to the Azure Function app needs to be made in a Custom Web API skill or a Custom Web API vectorizer, the JSON definition is slightly different. In both cases, ensure that you specify the correct URI to the Azure Function app and set the `authResourceId` to be the same value as the **Allowed token audience** configured for the authentication provider. 
+
+Depending on whether you choose to connect using a system assigned identity or a user assigned identity, details required will be slightly different. 
+
+### Using system assigned identity
+Here's an example to call into a function named `test` for the sample Azure Function app, where the system assigned identity of the search service is allowed to authenticate via "Easy Auth".
+
+```json
+"uri": "https://contoso-function-app.azurewebsites.net/api/test?",
+"authResourceId": "api://00000000-0000-0000-0000-000000000000"
+```
+
+### Using user assigned identity
+
+Here's an example to call into the same function, where the specific user assigned identity is allowed to authenticate via "Easy Auth". You're expected to specify the resource ID of the exact user assigned identity to use in the `identity` property of the configuration.
+
+```json
+"uri": "https://contoso-function-app.azurewebsites.net/api/test?",
+"authResourceId": "api://00000000-0000-0000-0000-000000000000",
+"identity" : { 
+        "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
+        "userAssignedIdentity": "/subscriptions/[subscription-id]/resourcegroups/[rg-name]/providers/Microsoft.ManagedIdentity/userAssignedIdentities/[my-user-managed-identity-name]" 
+    }
+```
+
+>[!NOTE]
+> This user assigned identity should actually be assigned to the Azure AI Search service for it to be specified in the Custom Web skill/vectorizer definition.
+
+## Run the indexer/vectorizer to verify permissions
+
+For Custom Web API skills, permissions are validated during indexer run-time. For vectorizer, they're validated when a vector query is issued utilizing the Custom Web API vectorizer. To rule out any specific issues with authentication, you can test by disabling the authentication provider on the Azure Function app and ensuring that calls from indexer/vectorizer succeed.
+
+* If authentication issues persist, ensure that the right identity information - namely Application ID, Object (principal) ID for the Azure AI Search service's identity is specified in the Azure Function app's authentication provider.
+
+## See also
+
+* [Custom Web API skill](cognitive-search-custom-skill-web-api.md)
+* [Custom Web API vectorizer](vector-search-vectorizer-custom-web-api.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure Functionsへのインデクサ接続設定に関する新しい記事の追加"
}
```

### Explanation
この変更では、「Managed Identities for Azure Functions」に関する新しい記事が追加されました。この文書は、Azure Functionsとのインデクサ接続を設定するための手順を詳述しており、特に「Easy Auth」として知られる組み込みの認証機能を用いた認証の設定に焦点を当てています。内容には、Microsoft Entra IDアプリケーションの設定、必要な前提条件、Azure Function appの認証プロバイダーとしてのMicrosoft Entra IDの構成方法が含まれています。

新しく追加された139行の内容は、Azure Functionsを使用してカスタムWeb APIをホスティングし、Azure AI Searchサービスがインデクサを介してコンテンツを取り込むために必要な詳細な手順と構成オプションを提供します。また、具体的な設定のためのスクリーンショットや注意事項も付属しており、ユーザーが適切に構成を行えるようにサポートしています。この追加により、関連するAzureサービス間の統合が強化され、技術的な作業の効率が向上します。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -470,6 +470,8 @@ items:
           href: search-howto-managed-identities-sql.md
         - name: SQL Managed Instance
           href: search-index-azure-sql-managed-instance-with-managed-identity.md
+        - name: Connect to an Azure function
+          href: search-howto-managed-identities-azure-functions.md
       - name: Connect through a firewall
         href: search-indexer-howto-access-ip-restricted.md
       - name: Connect using Network Security Perimeter
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Functionsへの接続に関する項目の追加"
}
```

### Explanation
この変更では、ドキュメント目次ファイル `toc.yml` が修正され、Azure Functionsへの接続に関する項目が追加されました。具体的には、「Connect to an Azure function」という名前の項目が追加され、そのリンク先として `search-howto-managed-identities-azure-functions.md` が指定されています。この更新により、ユーザーはAzure Functionsとの接続方法に関する新しいリソースに簡単にアクセスできるようになり、関連する情報が明確に整理されました。また、既存の内容と連携が強化され、ユーザーが特定のトピックを見つけやすくなっています。これは、Azure-managed identities を利用した接続を求めるユーザーにとって有益です。


