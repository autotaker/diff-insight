---
date: '2026-08-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c0c7917...MicrosoftDocs:93ed0d0
summary: Azure Cognitive Searchに関連する多くの文書が更新され、セキュリティ機能の強化、新しいプロパティの追加、日付の更新が行われました。主に認証やセキュリティに関する改善があり、新たに追加された`authResourceId`プロパティにより、安全な設定を行うための指針が提供されています。特に大きな破壊的変更はなく、設定の見直しが必要になる可能性があるものの、ユーザーに対してセキュリティを強化する情報が提供されています。これにより、Azure
  Cognitive Searchの利用者はリスクを軽減しつつ、より安全にサービスを活用できるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c0c7917...MicrosoftDocs:93ed0d0){target="_blank"}

<format>
# Highlights
Azure Cognitive Searchに関連する複数の文書が更新され、それぞれのセキュリティ機能強化や新しいプロパティの追加、日付の更新が行われました。これらの更新は主に認証とセキュリティに関するもので、追加された`authResourceId`プロパティなどの新機能により、ユーザーにより安全で適切な設定を行うためのガイダンスを提供しています。

## New features
- `authResourceId`プロパティの追加により、アプリケーションの認証管理が強化されました。
- `ai-usage: ai-assisted`という新しいカスタムフィールドが各文書に追加され、使用目的が明確にされました。
- セキュリティ考慮事項の追加により、セキュアなエンドポイント指定やトークン検証の重要性が強調されました。

## Breaking changes
特に大きな破壊的変更はありませんが、追加の認証プロパティとセキュリティに関する強化された記述により、設定の見直しが必要となる可能性があります。

## Other updates
- 各ドキュメントの日付が最新の状態に更新されました。
- マネージド・アイデンティティ認証と関連するセキュリティプラクティスが詳述されています。

# Insights
今回の更新は、Azure Cognitive Searchのユーザーがセキュリティリスクを軽減しつつ、サービスを効果的に利用できるようにすることを目的としているようです。`authResourceId`やマネージド・アイデンティティ認証に関する情報の追加は、特にAzureサービスのコンプライアンスや認証を考慮する企業にとって有益です。

この変更により、カスタムスキルやAPIスキル、GenAIプロンプトスキル、Azure OpenAI関連のスキルを使用する際に、セキュリティが強化されます。各文書の更新版は、セキュアな設定を行うための詳細なガイドを提供しており、信頼できる振る舞いの確保やセキュリティ対策の最適化に役立ちます。さらに、最小特権の原則やベストプラクティスの適用が推奨されており、これらを遵守することでシステム全体のセキュリティをさらに高められます。

結果として、これらの更新はAzure Cognitive Searchユーザーのセキュリティ認識を高め、より安全な環境でサービスを利用できるようになるための重要なステップであると考えられます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-custom-skill-interface.md](#item-4cb17d) | minor update | 認証リソースIDのプロパティの追加と日付の更新 | modified | 4 | 1 | 5 | 
| [cognitive-search-custom-skill-web-api.md](#item-5d1065) | minor update | カスタムWeb APIスキルの認証とセキュリティの強化 | modified | 57 | 2 | 59 | 
| [cognitive-search-skill-azure-openai-embedding.md](#item-3eca57) | minor update | Azure OpenAI Embeddingスキルのセキュリティ強化と日付の更新 | modified | 35 | 3 | 38 | 
| [cognitive-search-skill-genai-prompt.md](#item-384bf9) | minor update | GenAIプロンプトスキルのセキュリティ考慮事項の追加 | modified | 36 | 3 | 39 | 
| [vector-search-vectorizer-azure-open-ai.md](#item-e75cee) | minor update | Azure OpenAIベクトライザーのセキュリティ強化と日付の更新 | modified | 37 | 4 | 41 | 


# Modified Contents
## articles/search/cognitive-search-custom-skill-interface.md{#item-4cb17d}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,9 @@ ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
+ai-usage: ai-assisted
 ms.topic: how-to
-ms.date: 07/07/2026
+ms.date: 07/28/2026
 ms.update-cycle: 365-days
 ---
 
@@ -46,6 +47,8 @@ If your function or app uses Azure managed identities and Azure roles for authen
 
 + Your [custom skill definition](cognitive-search-custom-skill-web-api.md) must include an `authResourceId` property. This property takes an application (client) ID, in a [supported format](/azure/active-directory/develop/security-best-practices-for-app-registration#application-id-uri): `api://<appId>`.
 
+Ensure that `uri` points to the endpoint of the application identified by `authResourceId`. Mismatched values can cause authentication failures or requests being sent to an unintended endpoint. For security guidance, recommended practices, and steps to verify your configuration, see [Security considerations for managed identity authentication](cognitive-search-custom-skill-web-api.md#security-considerations-for-managed-identity-authentication).
+
 By default, the connection to the endpoint times out if a response isn't returned within a 30-second window (`PT30S`). The indexing pipeline is synchronous, and indexing produces a timeout error if a response isn't received in that time frame. You can increase the interval to a maximum value of 230 seconds by setting the `timeout` parameter (`PT230S`).
 
 ## Format web API inputs
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "認証リソースIDのプロパティの追加と日付の更新"
}
```

### Explanation
このコードの変更は、Azure Cognitive Searchのカスタムスキルインターフェースに関する文書を更新するもので、主に以下の点が修正されています。まず、`ms.date`のフィールドが2026年7月7日から2026年7月28日に変更されました。また、新たに`ai-usage: ai-assisted`というカスタムフィールドが追加されました。

さらに、カスタムスキル定義についての重要な情報が2つ追加されました。1つは、`authResourceId`プロパティが必須であり、このプロパティにはアプリケーション（クライアント）IDが必要であることです。もう1つは、`uri`が`authResourceId`で識別されたアプリケーションのエンドポイントを指していることを確認する重要性で、ミスマッチが発生すると認証エラーや不正なエンドポイントへのリクエストを引き起こす可能性があることが強調されています。

この変更により、ユーザーはカスタムスキルをより適切に設定し、安全に使用するためのガイダンスが提供されます。

## articles/search/cognitive-search-custom-skill-web-api.md{#item-5d1065}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,9 @@ ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
+ai-usage: ai-assisted
 ms.topic: reference
-ms.date: 04/14/2025
+ms.date: 07/28/2026
 ms.update-cycle: 365-days
 ---
 
@@ -35,14 +36,44 @@ Parameters are case sensitive.
 | Parameter name	 | Description |
 |--------------------|-------------|
 | `uri` | The URI of the Web API to which the JSON payload is sent. Only the **https** URI scheme is allowed. When you retrieve the skillset with GET, the service returns the `?code=` query parameter value as `?code=<redacted>` to prevent exposure of function keys. To update the skill without changing the stored URI, set `uri` to `<unchanged>`. |
-| `authResourceId` | (Optional) A string that if set, indicates that this skill should use a system managed identity on the connection to the function or app hosting the code. This property takes an application (client) ID or app's registration in Microsoft Entra ID, in any of these formats: `api://<appId>`, `<appId>/.default`, `api://<appId>/.default`. This value is used to scope the authentication token retrieved by the indexer, and is sent along with the custom Web skill API request to the function or app. Setting this property requires that your search service is [configured for managed identity](search-how-to-managed-identities.md) and your Azure function app is [configured for a Microsoft Entra sign in](/azure/app-service/configure-authentication-provider-aad). To use this parameter, call the API with `api-version=2023-10-01-Preview`. |
+| `authResourceId` | (Optional) A string that, when set, indicates that this skill should use a system managed identity on the connection to the function or app hosting the code. This property takes an application (client) ID or an app's registration in Microsoft Entra ID in any of these formats: `api://<appId>`, `<appId>/.default`, or `api://<appId>/.default`. This value is used to scope the authentication token retrieved by the indexer and is sent along with the Custom Web API skill request to the function or app. Setting this property requires that your search service is [configured for managed identity](search-how-to-managed-identities.md) and your Azure function app is [configured for a Microsoft Entra sign in](/azure/app-service/configure-authentication-provider-aad). To use this parameter, call the API with `api-version=2023-10-01-preview` or later. For guidance on choosing the correct value, see [Understand the `authResourceId` value](#understand-the-authresourceid-value). |
 | `authIdentity`   | (Optional) A user-managed identity used by the search service for connecting to the function or app hosting the code. You can use either a [system or user managed identity](search-how-to-managed-identities.md). To use a system managed identity, leave `authIdentity` blank. |
 | `httpMethod` | The method to use while sending the payload. Allowed methods are `PUT` or `POST` |
 | `httpHeaders` | A collection of key-value pairs where the keys represent header names and values represent header values that are sent to your Web API along with the payload. The following headers are prohibited from being in this collection: `Accept`, `Accept-Charset`, `Accept-Encoding`, `Content-Length`, `Content-Type`, `Cookie`, `Host`, `TE`, `Upgrade`, `Via`. When you retrieve the skillset with GET, the service returns `<redacted>` for all header values to prevent exposure of credentials such as bearer tokens and API keys. To update the skill without changing stored header values, set each value to `<unchanged>`. The service restores the original stored value. |
 | `timeout` | (Optional) When specified, indicates the timeout for the http client making the API call. It must be formatted as an XSD "dayTimeDuration" value (a restricted subset of an [ISO 8601 duration](https://www.w3.org/TR/xmlschema11-2/#dayTimeDuration) value). For example, `PT60S` for 60 seconds. If not set, a default value of 30 seconds is chosen. The timeout can be set to a maximum of 230 seconds and a minimum of 1 second. |
 | `batchSize` | (Optional) Indicates how many "data records" (see JSON payload structure below) is sent per API call. If not set, a default of 1000 is chosen. Use this parameter to achieve a suitable tradeoff between indexing throughput and load on your API. |
 | `degreeOfParallelism` | (Optional) When specified, indicates the number of calls the indexer makes in parallel to the endpoint you provide. You can decrease this value if your endpoint is failing under pressure, or raise it if your endpoint can handle the load. If not set, a default value of 5 is used. The `degreeOfParallelism` can be set to a maximum of 10 and a minimum of 1. |
 
+### Understand the `authResourceId` value
+
+When a Custom Web API skill uses managed identity authentication, Azure AI Search obtains a Microsoft Entra access token and sends it to the custom skill endpoint. The `authResourceId` property specifies the resource identifier, also known as the audience or Application ID URI, for which the token is requested. The value must match what the target application expects during token validation. Otherwise, authentication fails with a `401 Unauthorized` response.
+
+The `authResourceId` value identifies the application hosting your custom skill. It isn't the URL of your search service or indexer.
+
+The following table shows common formats:
+
+| Target application | `authResourceId` value |
+|---|---|
+| Microsoft Entra protected web application | `api://<application-client-id>` |
+| Application configured with a custom Application ID URI | Custom Application ID URI, such as `api://contoso-customskill` |
+| Azure Function protected by Microsoft Entra ID | Application ID URI configured for the function app's app registration, such as `api://contoso-funcapp` |
+
+The property accepts formats with and without the `.default` scope suffix. Use `api://<appId>` to match the Application ID URI directly. If you include a `.default` suffix, such as `api://<appId>/.default`, the access token's `aud` claim contains the base Application ID URI without the suffix.
+
+For steps to configure Microsoft Entra authentication for an Azure Function and set `authResourceId`, see [Use a search service managed identity to connect to an Azure Function app](search-howto-managed-identities-azure-functions.md).
+
+**Example: Azure Function protected by Microsoft Entra ID**
+
+In this example, Azure AI Search acquires an access token for the audience specified by `authResourceId` and includes the token when invoking the custom skill endpoint.
+
+```json
+{
+  "@odata.type": "#Microsoft.Skills.Custom.WebApiSkill",
+  "uri": "https://contoso-function.azurewebsites.net/api/enrich",
+  "authResourceId": "api://contoso-customskill"
+}
+```
+
 ## Skill inputs
 
 This skill has no predefined inputs. The inputs are any existing field, or any [node in the enrichment tree](cognitive-search-working-with-skillsets.md#enrichment-tree) that you want to pass to your custom skill.
@@ -245,6 +276,30 @@ In addition to your Web API being unavailable or sending non-successful status c
 
 For cases when the Web API is unavailable or returns an HTTP error, the indexer execution history includes a friendly error with any available details about the HTTP error.
 
+## Security considerations for managed identity authentication
+
+When using managed identity authentication with a Custom Web API skill, Azure AI Search obtains a Microsoft Entra access token for the application identified by `authResourceId` and includes that token in requests sent to the endpoint specified by `uri`. The endpoint referenced by `uri` is typically your Azure Function, Azure App Service, Azure API Management endpoint, or another Microsoft Entra-protected application. You're responsible for configuring and maintaining the relationship between the endpoint and the application identified by `authResourceId`.
+
+### Recommended security practices
+
+To help maintain a secure deployment, follow these practices:
+
+- Configure the `uri` property to point only to trusted endpoints that are intended to receive requests from Azure AI Search.
+- Configure `authResourceId` to identify the Microsoft Entra application that is expected to receive and validate the access token.
+- Ensure that the application receiving requests validates standard token claims, including audience (`aud`), issuer (`iss`), tenant (`tid`), and any required application roles or permissions, before processing requests.
+- Apply the principle of least privilege when granting permissions to the Azure AI Search managed identity.
+- Periodically review Custom Web API skill definitions, Microsoft Entra application registrations, and app role assignments and permissions granted to Azure AI Search managed identities. Review configuration changes through your established change-management and security-review processes.
+- Periodically review endpoint configurations for Azure Functions, App Services, APIs, and API gateways.
+- Monitor application sign-in logs, authentication events, and API access logs for unexpected or unauthorized activity.
+- Remove unused endpoints, permissions, application registrations, and role assignments that are no longer required.
+
+### Restrict access to skillset configuration
+
+Users who can create, modify, or run skillsets can control both the destination endpoint and the authentication configuration used by a Custom Web API skill. Restrict these permissions to trusted administrators and follow your standard change-management and security review processes when configuring managed identity-enabled custom skills.
+
+> [!IMPORTANT]
+> The `authResourceId` value identifies the intended recipient application for the access token. Ensure that the endpoint specified in `uri` is the endpoint that is expected to receive and validate tokens for that application. Incorrect configuration can result in authentication failures or requests being sent to an unintended endpoint.
+
 ## See also
 
 + [Define a skillset](cognitive-search-defining-skillset.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムWeb APIスキルの認証とセキュリティの強化"
}
```

### Explanation
この変更は、Azure Cognitive SearchにおけるカスタムWeb APIスキルの文書に関するものです。主に以下の修正が行われました。

1. **日付の更新**: `ms.date`のフィールドが2025年4月14日から2026年7月28日に変更されました。

2. **新しいカスタムフィールドの追加**: `ai-usage: ai-assisted`というフィールドが追加され、文書の情報量が増加しました。

3. **`authResourceId`の詳細な説明**: `authResourceId`パラメータについての説明が強化され、Microsoft Entra IDを使用した認証プロセスや、期待される形式に関する情報が追加されました。このプロパティは、アクセス・トークンの取得に必要であり、トークン検証中にターゲットアプリケーションが期待する値と一致しなければならないことが説明されています。

4. **セキュリティに関する考慮事項**: マネージド・アイデンティティ認証を使用する際のセキュリティに関する章が新たに追加され、信頼できるエンドポイントを指定することや、必要なトークンの検証を行うことの重要性が強調されています。

これにより、ユーザーはカスタムWeb APIスキルをより安全にかつ適切に構成するための詳細なガイダンスを得ることができます。また、認証構成に関するベストプラクティスが示されることで、セキュリティリスクを軽減するための助けとなる情報が提供されています。

## articles/search/cognitive-search-skill-azure-openai-embedding.md{#item-3eca57}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,8 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: reference
-ms.date: 07/10/2025
+ms.date: 07/28/2026
+ai-usage: ai-assisted
 ---
 
 #	Azure OpenAI Embedding skill
@@ -45,7 +46,7 @@ Parameters are case sensitive.
 
 | Inputs | Description |
 |---------------------|-------------|
-| `resourceUri` | (Required) The URI of the model provider. Supported domains are:<p><ul><li>`openai.azure.com`</li><li>`services.ai.azure.com`</li><li>`cognitiveservices.azure.com`</li></ul><p>This field is required if your resource is deployed behind a private endpoint or uses virtual network (VNet) integration. [Azure API Management](/azure/api-management/api-management-key-concepts) endpoints are also supported, , except for API Management custom domains. For setup, including authentication, RBAC, and optional private connectivity, see [Use Azure API Management with Azure OpenAI skills and vectorizers](search-how-to-configure-azure-openai-api-management.md). |
+| `resourceUri` | (Required) The URI of the model provider. Supported domains are:<p><ul><li>`openai.azure.com`</li><li>`services.ai.azure.com`</li><li>`cognitiveservices.azure.com`</li></ul><p>This field is required if your resource is deployed behind a private endpoint or uses virtual network (VNet) integration. [Azure API Management](/azure/api-management/api-management-key-concepts) endpoints are also supported, except for API Management custom domains. For setup, including authentication, RBAC, and optional private connectivity, see [Use Azure API Management with Azure OpenAI skills and vectorizers](search-how-to-configure-azure-openai-api-management.md). |
 | `apiKey`   |  The secret key used to access the model. If you provide a key, leave `authIdentity` empty. If you set both `apiKey` and `authIdentity`, the `apiKey` is used on the connection. |
 | `deploymentId`   | (Required) The ID of the deployed Azure OpenAI embedding model. This is the deployment name you specified when you deployed the model. |
 | `authIdentity`   | A user-managed identity used by the search service for the connection. You can use either a [system- or user-managed identity](search-how-to-managed-identities.md). To use a system-managed identity, leave `apiKey` and `authIdentity` blank. The system-managed identity is used automatically. A managed identity must have [Cognitive Services OpenAI User](/azure/ai-services/openai/how-to/role-based-access-control#azure-openai-roles) permissions to send text to Azure OpenAI. |
@@ -144,7 +145,7 @@ The following are some best practices you need to consider when utilizing this s
 
 - Your Azure OpenAI instance should be in the same region or at least geographically close to the region where your AI Search service is hosted. This reduces latency and improves the speed of data transfer between the services.
 
-- To avoid experiencing 429 error codes often, consider implementing load balancing via [API Management](/azure/api-management/) by implementing a gateway [/azure/architecture/ai-ml/guide/azure-openai-gateway-multi-backend] in front of multiple Azure OpenAI embedding model deployments.
+- To avoid experiencing 429 error codes often, consider implementing load balancing via [API Management](/azure/api-management/) by implementing a [gateway](/azure/architecture/ai-ml/guide/azure-openai-gateway-multi-backend) in front of multiple Azure OpenAI embedding model deployments.
 
 -	If you have a larger than default Azure OpenAI TPM (Tokens per minute) limit as published in [quotas and limits](/azure/ai-services/openai/quotas-limits) documentation, open a [support case](/azure/azure-portal/supportability/how-to-create-azure-support-request) with the Azure AI Search team, so this can be adjusted accordingly. This helps your indexing process not being unnecessarily slowed down by the documented default TPM limit, if you have higher limits.
 
@@ -163,6 +164,37 @@ The following are some best practices you need to consider when utilizing this s
 | Text is empty | Warning |
 | Text is larger than 8,000 tokens | Error |
 
+## Security considerations for managed identity authentication
+
+When the Azure OpenAI Embedding skill uses managed identity authentication, Azure AI Search obtains a Microsoft Entra access token for the Foundry Tools audience (`https://cognitiveservices.azure.com`) and includes it in requests sent to the endpoint specified by `resourceUri`. Managed identity authentication applies when `authIdentity` is set, or when both `apiKey` and `authIdentity` are empty and the service uses the system-assigned identity.
+
+The endpoint referenced by `resourceUri` is expected to be your own Azure OpenAI or Foundry Tools resource. Supported domains are:
+
+- `openai.azure.com`
+- `cognitiveservices.azure.com`
+- `services.ai.azure.com`
+
+[Azure API Management (APIM)](/azure/api-management/api-management-key-concepts) endpoints (`*.azure-api.net`) are also supported. Because an APIM hostname can't be verified from its name alone, Azure AI Search validates these endpoints with a live connectivity check at configuration time rather than by domain matching. You're responsible for configuring and maintaining the relationship between the APIM endpoint and the Azure OpenAI or Foundry Tools resource behind it.
+
+A managed identity token issued for the Foundry Tools audience is valid against any Foundry Tools or Azure OpenAI resource the identity is authorized on. **Sending it to an untrusted endpoint could expose the token.**
+
+### Recommended security practices
+
+To help maintain a secure deployment, follow these practices:
+
+- Set `resourceUri` only to endpoints you own and trust. Prefer the Foundry Tools domains listed earlier. If you use an APIM endpoint, confirm it fronts your own resource before enabling managed identity. A trusted-looking hostname isn't proof of ownership.
+- Apply the principle of least privilege to the managed identity used by the search service. The Azure OpenAI Embedding skill requires only the **Cognitive Services OpenAI User** role on the target resource. Avoid granting broader roles.
+- Use [Network Security Perimeter (NSP)](search-security-network-security-perimeter.md) and private endpoints or VNet integration to restrict which endpoints the search service can reach and which sources the target resource accepts requests from.
+- If you use an APIM endpoint, ensure the gateway validates inbound requests and forwards them only to the intended backend. You should also review its access policies periodically.
+- Prefer managed identity over `apiKey`. If you use `apiKey`, store and rotate it securely and don't embed it in source control. The service rejects configurations that set both `apiKey` and `authIdentity`.
+- Periodically review skillset definitions, managed identity role assignments, and APIM configurations to confirm that `resourceUri` values, access controls, and identity permissions remain current and appropriate. Review configuration changes through your established change-management and security-review processes.
+- Monitor Azure OpenAI and Foundry Tools sign-in logs, authentication events, and access logs for unexpected or unauthorized activity.
+- Remove unused skills, endpoints, role assignments, and API keys that are no longer required.
+
+### Restrict access to skillset configuration
+
+Users who can create, modify, or run skillsets control both the destination endpoint (`resourceUri`) and the authentication configuration used by the skill. Because the skill sends a managed identity token for the Foundry Tools audience to that endpoint, restrict these permissions to trusted administrators and follow your standard change-management and security-review processes when configuring managed identity–enabled skills.
+
 ## See also
 
 + [Built-in skills](cognitive-search-predefined-skills.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI Embeddingスキルのセキュリティ強化と日付の更新"
}
```

### Explanation
この変更は、Azure Cognitive SearchにおけるAzure OpenAI Embeddingスキルに関する文書を更新したもので、主に以下のポイントが含まれています。

1. **日付の更新**: ドキュメントの最終更新日が2025年7月10日から2026年7月28日に変更されました。

2. **新しいカスタムフィールドの追加**: 新たに`ai-usage: ai-assisted`というフィールドが追加され、利用目的が明確になりました。

3. **`resourceUri`フィールドの詳細説明**: `resourceUri`のフィールドに関する説明が強化され、特にAPI Managementエンドポイントについての注意点が明確化されました。

4. **セキュリティに関する考慮事項**: マネージドアイデンティティ認証を使用する場合のセキュリティ考慮事項が新たに追加され、Azure OpenAI EmbeddingスキルがMicrosoft Entraアクセス・トークンを取得し、指定されたエンドポイントに送信する方法が詳述されています。このセクションでは、信頼できるエンドポイントのみを使用すること、最小特権の原則を適用すること、及び定期的なレビューの重要性が強調されています。

これにより、ユーザーはセキュリティを考慮した形でAzure OpenAI Embeddingスキルを利用できるようになり、信頼性の高いエンドポイントとの接続方法や認証のベストプラクティスについてのガイダンスが得られます。

## articles/search/cognitive-search-skill-genai-prompt.md{#item-384bf9}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2025
 ms.topic: reference
-ms.date: 04/22/2026
+ms.date: 07/28/2026
 ai-usage: ai-assisted
 ---
 
@@ -231,10 +231,43 @@ The GenAI Prompt skill is generally available in the [2026-04-01 Search Service
 | Both `apiKey` and `authIdentity` supplied | **Error** |
 | Unsupported model for multimodal prompt | **Error** |
 | Input exceeds model token limit | **Error** |
-| Model returns invalid JSON for `json_schema` | **Warning** – raw string returned in `response` |
+| Model returns invalid JSON for `json_schema` | **Warning**: Raw string returned in `response` |
 
+## Security considerations for managed identity authentication
 
-### See also
+When the GenAI Prompt skill uses managed identity authentication, Azure AI Search obtains a Microsoft Entra access token for the Foundry Tools audience (`https://cognitiveservices.azure.com`) and includes it in requests sent to the endpoint specified by `uri`. Managed identity authentication applies when `authIdentity` is set, or when both `apiKey` and `authIdentity` are empty and the service uses the system-assigned identity.
+
+The endpoint referenced by `uri` is expected to be your own Azure OpenAI or Foundry resource. Supported domains are:
+
+- `openai.azure.com`
+- `cognitiveservices.azure.com`
+- `services.ai.azure.com`
+
+[Azure API Management (APIM)](/azure/api-management/api-management-key-concepts) endpoints (`*.azure-api.net`) and custom domains that front these resources are also supported. Because a custom domain or APIM hostname can't be verified from its name alone, Azure AI Search validates these endpoints with a live connectivity check at configuration time rather than by domain matching. You're responsible for configuring and maintaining the relationship between the endpoint and the Azure OpenAI or Foundry resource behind it.
+
+> [!NOTE]
+> A managed identity token issued for the Foundry Tools audience is valid against any Foundry Tools or Azure OpenAI resource the identity is authorized on. Sending it to an untrusted endpoint could expose the token.
+
+### Recommended security practices
+
+To help maintain a secure deployment, follow these practices:
+
+- Set `uri` only to endpoints you own and trust. Prefer the Foundry Tools domains listed earlier. If you use an APIM or custom-domain endpoint, confirm it fronts your own resource before enabling managed identity. A trusted-looking hostname isn't proof of ownership.
+- Apply the principle of least privilege to the managed identity used by the search service:
+  - On Azure OpenAI, assign only **Cognitive Services OpenAI User**.
+  - On Foundry, assign only **Foundry User**. Avoid granting broader roles.
+- Use [Network Security Perimeter (NSP)](search-security-network-security-perimeter.md) and private endpoints or VNet integration to restrict which endpoints the search service can reach and which sources the target resource accepts requests from.
+- If you use an APIM or custom-domain endpoint, ensure the gateway validates inbound requests and forwards them only to the intended backend. You should also review its access policies periodically.
+- Prefer managed identity over `apiKey`. If you use `apiKey`, store and rotate it securely and don't embed it in source control. The service rejects configurations that set both `apiKey` and `authIdentity`.
+- Periodically review skillset definitions, managed identity role assignments, and APIM and custom-domain configurations to confirm that `uri` values, access controls, and identity permissions remain current and appropriate. Review configuration changes through your established change-management and security-review processes.
+- Monitor Azure OpenAI, Foundry Tools, and Foundry sign-in logs, authentication events, and access logs for unexpected or unauthorized activity.
+- Remove unused skills, endpoints, role assignments, and API keys that are no longer required.
+
+### Restrict access to skillset configuration
+
+Users who can create, modify, or run skillsets control both the destination endpoint (`uri`) and the authentication configuration used by the skill. Because the skill sends a managed identity token for the Foundry Tools audience to that endpoint, restrict these permissions to trusted administrators and follow your standard change-management and security-review processes when configuring managed identity–enabled skills.
+
+## See also
 
 - [Azure AI Search built-in indexers](search-indexer-overview.md)
 - [Integrated vectorization](vector-search-integrated-vectorization.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GenAIプロンプトスキルのセキュリティ考慮事項の追加"
}
```

### Explanation
この変更は、Azure Cognitive SearchにおけるGenAIプロンプトスキルに関する文書を更新したもので、以下の主要な変更点が含まれています。

1. **日付の更新**: ドキュメントの最終更新日が2026年4月22日から2026年7月28日に変更されました。

2. **セキュリティに関する考慮事項の追加**: マネージド・アイデンティティ認証を使用する場合のセキュリティ考慮事項が新たに追加され、Azure AI SearchがMicrosoft Entraアクセス・トークンを取得し、指定されたエンドポイントに送信する方法について説明されています。このセクションでは、信頼できるエンドポイントのみを使用することの重要性や、適切な役割の割り当てのための最小特権の原則が強調されています。

3. **推奨されるセキュリティプラクティス**: セキュリティの維持に役立つ複数の推奨プラクティスが追加され、特にエンドポイントの信頼性やアクセス制御に関して詳細な指針が提供されています。

4. **APIキーに関する注意喚起**: マネージド・アイデンティティを使用することが推奨され、APIキーの安全な管理に関する注意点が示されています。

これにより、ユーザーはGenAIプロンプトスキルを使用する際に必要なセキュリティ対策を講じることができ、より安全な構成を確保するための具体的な手法を学ぶことができます。

## articles/search/vector-search-vectorizer-azure-open-ai.md{#item-e75cee}

<details>
<summary>Diff</summary>
````diff
@@ -5,15 +5,16 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: concept-article
-ms.date: 07/10/2026
+ms.date: 07/28/2026
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Azure OpenAI vectorizer
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-The **Azure OpenAI** vectorizer connects to an embedding model deployed to your [Azure OpenAI in Foundry Models](/azure/ai-services/openai/overview) resource or [Microsoft Foundry](/azure/ai-foundry/what-is-azure-ai-foundry) project to generate embeddings at query time. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed.
+The **Azure OpenAI** vectorizer connects to an embedding model deployed to your [Azure OpenAI in Foundry Models](/azure/ai-services/openai/overview) resource or [Microsoft Foundry](/azure/ai-foundry/what-is-foundry) project to generate embeddings at query time. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed.
 
 Although vectorizers are used at query time, you specify them in index definitions and reference them on vector fields through a vector profile. For more information, see [Configure a vectorizer in a search index](vector-search-how-to-configure-vectorizer.md).
 
@@ -76,7 +77,7 @@ The expected field dimensions for a field configured with an Azure OpenAI vector
 ]
 ```
 
-## Best practices
+## Performance best practices
 
 The following are some best practices you need to consider when utilizing this vectorizer:
 
@@ -86,11 +87,43 @@ The following are some best practices you need to consider when utilizing this v
 
 - Your Azure OpenAI instance should be in the same region or at least geographically close to the region where your AI Search service is hosted. This reduces latency and improves the speed of data transfer between the services.
 
-- To avoid experiencing 429 error codes often, consider implementing load balancing via [API Management](/azure/api-management/) by implementing a gateway [/azure/architecture/ai-ml/guide/azure-openai-gateway-multi-backend] in front of multiple Azure OpenAI embedding model deployments.
+- To avoid frequent 429 error codes, consider implementing load balancing through [API Management](/azure/api-management/) by implementing a [load-balancing gateway](/azure/architecture/ai-ml/guide/azure-openai-gateway-multi-backend) in front of multiple Azure OpenAI embedding model deployments.
 
 -	If you have a larger than default Azure OpenAI TPM (Tokens per minute) limit as published in [quotas and limits](/azure/ai-services/openai/quotas-limits) documentation, open a [support case](/azure/azure-portal/supportability/how-to-create-azure-support-request) with the Azure AI Search team, so this can be adjusted accordingly. This helps your indexing process not being unnecessarily slowed down by the documented default TPM limit, if you have higher limits.
 
 
+## Security considerations for managed identity authentication
+
+When the Azure OpenAI vectorizer uses managed identity authentication, Azure AI Search obtains a Microsoft Entra access token for the Foundry Tools audience (`https://cognitiveservices.azure.com`) and includes it in requests sent to the endpoint specified by `resourceUri`. Managed identity authentication applies when you set `authIdentity`, or when both `apiKey` and `authIdentity` are empty and the service uses the system-assigned identity.
+
+The endpoint referenced by `resourceUri` is expected to be your own Azure OpenAI or Foundry Tools resource. Supported domains are:
+
+- `openai.azure.com`
+- `cognitiveservices.azure.com`
+- `services.ai.azure.com`
+
+[Azure API Management (APIM)](/azure/api-management/api-management-key-concepts) endpoints (`*.azure-api.net`) are also supported. Because an APIM hostname can't be verified from its name alone, Azure AI Search validates these endpoints with a live connectivity check at configuration time rather than by domain matching. You're responsible for configuring and maintaining the relationship between the APIM endpoint and the Azure OpenAI or Foundry Tools resource behind it.
+
+> [!NOTE]
+> A managed identity token issued for the Foundry Tools audience is valid against any Foundry Tools or Azure OpenAI resource the identity is authorized on. Sending it to an untrusted endpoint could expose the token.
+
+### Recommended security practices
+
+To help maintain a secure deployment, follow these practices:
+
+- Set `resourceUri` only to endpoints you own and trust. Prefer the Foundry Tools domains listed earlier. If you use an APIM endpoint, confirm it fronts your own resource before enabling managed identity. A trusted-looking hostname isn't proof of ownership.
+- Apply the principle of least privilege to the managed identity used by the search service. The Azure OpenAI vectorizer requires only the **Cognitive Services OpenAI User** role on the target resource. Avoid granting broader roles.
+- Use [Network Security Perimeter (NSP)](search-security-network-security-perimeter.md) and private endpoints or VNet integration to restrict which endpoints the search service can reach and which sources the target resource accepts requests from.
+- If you use an APIM endpoint, ensure the gateway validates inbound requests and forwards them only to the intended backend. You should also review its access policies periodically.
+- Prefer managed identity over `apiKey`. If you use `apiKey`, store and rotate it securely and don't embed it in source control. The service rejects configurations that set both `apiKey` and `authIdentity`.
+- Periodically review index definitions, managed identity role assignments, and APIM configurations to confirm that `resourceUri` values, access controls, and identity permissions remain current and appropriate. Review configuration changes through your established change-management and security-review processes.
+- Monitor Azure OpenAI and Foundry Tools sign-in logs, authentication events, and access logs for unexpected or unauthorized activity.
+- Remove unused vectorizers, endpoints, role assignments, and API keys that are no longer required.
+
+### Restrict access to index and vectorizer configuration
+
+Users who can create or modify index definitions control both the destination endpoint (`resourceUri`) and the authentication configuration used by the vectorizer. Because the vectorizer sends a managed identity token for the Foundry Tools audience to that endpoint, restrict these permissions to trusted administrators and follow your standard change-management and security-review processes when configuring managed identity–enabled vectorizers.
+
 ## See also
 
 + [Integrated vectorization](vector-search-integrated-vectorization.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIベクトライザーのセキュリティ強化と日付の更新"
}
```

### Explanation
この変更は、Azure Cognitive SearchにおけるAzure OpenAIベクトライザーに関する文書を更新したもので、以下の主要な変更点が含まれています。

1. **日付の更新**: ドキュメントの最終更新日が2026年7月10日から2026年7月28日に変更されました。

2. **新しいカスタムフィールドの追加**: 文書に`ai-usage: ai-assisted`フィールドが追加され、Azure OpenAIベクトライザーの使用目的が明確になりました。

3. **セキュリティに関する考慮事項の追加**: マネージド・アイデンティティ認証の使用に関するセキュリティ考慮事項が新たに追加され、Azure AI SearchがMicrosoft Entraアクセス・トークンを取得し、指定されたエンドポイントに送信する方法について詳述されています。

4. **推奨されるセキュリティプラクティス**: 文書に複数の推奨セキュリティプラクティスが追加され、ユーザーが信頼できるエンドポイントの設定や、最小特権の原則の適用を行うことが求められています。

5. **パフォーマンスに関するベストプラクティスの強調**: ベストプラクティスのセクションが「パフォーマンスベストプラクティス」へと変更され、より明確な指針が提供されています。

これにより、ユーザーはAzure OpenAIベクトライザーを利用する際に必要なセキュリティ対策を講じ、パフォーマンス向上に必要な設定を理解することができます。


