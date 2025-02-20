---
date: '2025-02-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f9aa01e...MicrosoftDocs:11dfa93
summary: 今回のドキュメントの変更では、Azure AIおよびOpenAIサービスに関連するいくつかの重要な改訂が行われました。主なポイントとして、データのアップロード方法に関するガイダンスが明確化され、JavaScriptクライアントの設定がより詳細に説明されました。また、監視指標が最新のもので更新され、「Tokens
  per Second」という新しい指標が追加され、パフォーマンス監視が強化されました。文書の日付も最新に更新され、ウェブアプリに関する注意事項やサポートセクションへのリンクも追加されています。この変更により、ユーザーはAzureサービスをより効果的に利用できるようになります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f9aa01e...MicrosoftDocs:11dfa93){target="_blank"}

# Highlights
このドキュメントの変更では、Azure AIおよびOpenAIサービスに関連する複数の部分が改訂されました。変更の主な特徴としては、データアップロード方法についてのガイダンスが明瞭になり、JavaScriptのクライアント構成が詳細に説明され、監視指標が最新のものとなり、公式の日時も更新されています。

## 新機能
- データアップロードと接続のベストプラクティスを示す新しいガイダンスが追加されました。
- Azure OpenAIのJavaScriptクライアントについて、`AzureClientOptions`オブジェクトを使用した構成の詳細が追加されました。
- モニタリング指標に「Tokens per Second」が新しく加わり、パフォーマンス監視が強化されました。

## 破壊的変更
現時点で、破壊的変更は特記されていません。ただし、削除された要素や仕様に変更が加えられた場合があります。

## その他の更新
- ウェブアプリに関する注意事項と、サポートセクションへのリンクが追加されました。
- 文書の日付が最新に更新されました。
- 「Time to Last Byte」という指標が削除され、単純化が図られました。

# Insights
今回の更新は、Azure AIおよびOpenAIサービスの使いやすさと実用性を向上させることを目的としています。特にデータのアップロードおよび接続に関するガイダンスは、ユーザーが正確かつ効率的にAzureサービスを利用するために不可欠です。また、JavaScriptクライアントの構成方法がより細かく説明され、ユーザーは設定の誤りを減少させることができます。

さらにモニタリング指標の更新により、開発者はより詳細にパフォーマンスを分析でき、必要に応じてシステムの調整が可能になりました。この変更は、特に大規模な運用環境で役立つでしょう。

全体として、このドキュメントの変更は、ユーザーがサービスを最適に活用するための手がかりを提供し、よりスムーズな開発と運用を可能にしています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [use-your-data.md](#item-455d6e) | minor update | データのアップロードおよび接続に関する新たなガイダンスの追加 | modified | 3 | 1 | 4 | 
| [use-web-app.md](#item-802413) | minor update | ウェブアプリに関する注意事項と日付の更新 | modified | 4 | 2 | 6 | 
| [javascript.md](#item-50536a) | minor update | JavaScript用Azure OpenAIクライアントの構成と機能の更新 | modified | 38 | 12 | 50 | 
| [monitor-openai-reference.md](#item-8d8887) | minor update | Azure OpenAIのモニタリング指標の更新 | modified | 2 | 3 | 5 | 


# Modified Contents
## articles/ai-services/openai/concepts/use-your-data.md{#item-455d6e}

<details>
<summary>Diff</summary>
````diff
@@ -82,6 +82,8 @@ For some data sources such as uploading files from your local machine (preview)
 |URL/Web address (preview)        | Web content from the URLs is stored in Azure Blob Storage.         |
 |Azure Blob Storage (preview) | Upload files from Azure Blob Storage to be ingested into an Azure AI Search index.         |
 
+If you choose to upload files or connect Azure Blob Storage, your data should be unstructured text for best results. If you have non-textual semi-structured or structured data consider converting it to text. If your files have special formatting, such as tables and columns, or bullet points, prepare your data with the data preparation script available on [GitHub](https://github.com/microsoft/sample-app-aoai-chatGPT/tree/main/scripts#optional-crack-pdfs-to-text).
+
 :::image type="content" source="../media/use-your-data/azure-databases-and-ai-search.png" lightbox="../media/use-your-data/azure-databases-and-ai-search.png" alt-text="Diagram of vector indexing services.":::
 
 # [Azure AI Search](#tab/ai-search)
@@ -93,7 +95,7 @@ You might want to consider using an Azure AI Search index when you either want t
 > [!NOTE]
 > * To use an existing index, it must have at least one searchable field.
 > * Set the CORS **Allow Origin Type** option to `all` and the **Allowed origins** option to `*`. 
-
+> * You cannot have complex fields in your search index. 
 
 ### Search types
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データのアップロードおよび接続に関する新たなガイダンスの追加"
}
```

### Explanation
このコードの変更では、Azure AIサービスにおけるデータのアップロードや接続の方法に関する情報が更新されました。具体的には、ファイルをアップロードする際やAzure Blob Storageに接続する場合は、最適な結果を得るためにデータが非構造テキストであるべきという指針が追加されています。また、特殊なフォーマットを持つファイル、例えば表や列、箇条書きが含まれるデータの事前準備についても、GitHub上にあるデータ準備スクリプトを利用するように促されています。

さらに、画像を使った図によって、ベクターインデックスサービスの視覚的な説明が加えられています。最後に、検索インデックスにおける制約に関しても新たな注意事項が追加されています。全体として、ユーザーに対する明確なガイダンスを提供し、データ準備に関する理解を深める内容となっています。

## articles/ai-services/openai/how-to/use-web-app.md{#item-802413}

<details>
<summary>Diff</summary>
````diff
@@ -7,19 +7,21 @@ ms.service: azure-ai-openai
 ms.topic: how-to
 author: aahill
 ms.author: aahi
-ms.date: 01/08/2025
+ms.date: 02/19/2025
 recommendations: false
 ---
 
 
 # Use the Azure OpenAI web app
 
+> [!NOTE]
+> The web app and its [source code](https://github.com/microsoft/sample-app-aoai-chatGPT) are provided "as is" and as a sample only. Customers are responsible for all customization and implementation of their web apps. See the support section for the web app on [GitHub](https://github.com/microsoft/sample-app-aoai-chatGPT/blob/main/SUPPORT.md) for more information.
+
 Along with Azure AI Foundry portal, APIs, and SDKs, you can use the customizable standalone web app to interact with Azure OpenAI models by using a graphical user interface. Key features include:
 * Connectivity with multiple data sources to support rich querying and retrieval-augmented generation, including Azure AI Search, Prompt Flow, and more.
 * Conversation history and user feedback collection through Cosmos DB.
 * Authentication with role-based access control via Microsoft Entra ID.
 * Customization of the user interface, data sources, and features using environment variables (no-code via Azure portal).
-* Sample source code for the web app is available on [GitHub](https://github.com/microsoft/sample-app-aoai-chatGPT). Source code is provided "as is" and as a sample only. Customers are responsible for all customization and implementation of their web apps.
 
 You can deploy the app via the [Azure AI Foundry portal](/azure/ai-studio/tutorials/deploy-chat-web-app), the [Azure portal](https://portal.azure.com), or the Azure Developer CLI via your local machine [(instructions available at the repository here)](https://github.com/microsoft/sample-app-aoai-chatGPT). Depending on your deployment channel, you can preload a data source to chat with via the web application, but this can be changed after deployment. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ウェブアプリに関する注意事項と日付の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIウェブアプリに関するドキュメントの更新を含んでいます。主な変更点は、ウェブアプリおよびそのソースコードに関する新たな注意書きが追加されたことです。この注意書きでは、提供されるウェブアプリが「現状のまま」であること、顧客が全てのカスタマイズおよび実装に責任を持つことが明記されています。また、GitHub上のサポートセクションへのリンクも含まれています。

さらに、文書の日付が2025年1月8日から2025年2月19日に更新されています。これにより、情報の鮮度が保たれています。全体として、ユーザーにとって重要なカスタマイズの責任についてのガイダンスが強化され、実用的な情報が提供されている内容となっています。

## articles/ai-services/openai/includes/language-overview/javascript.md{#item-50536a}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Azure OpenAI JavaScript support
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 11/18/2024
+ms.date: 02/13/2025
 ---
 
 [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Reference](../../reference.md) |
@@ -36,7 +36,7 @@ import { DefaultAzureCredential } from "@azure/identity";
 const credential = new DefaultAzureCredential();
 ```
 
-This object is then passed to the second argument of the `OpenAIClient` and `AssistantsClient` client constructors.
+This object is then passed as part of the [`AzureClientOptions`](#configuration) object to the `AzureOpenAI` and `AssistantsClient` client constructors.
 
 In order to authenticate the `AzureOpenAI` client, however, we need to use the `getBearerTokenProvider` function from the `@azure/identity` package. This function creates a token provider that `AzureOpenAI` uses internally to obtain tokens for each request. The token provider is created as follows:
 
@@ -48,38 +48,64 @@ const endpoint = "https://your-azure-openai-resource.com";
 const apiVersion = "2024-10-21"
 const scope = "https://cognitiveservices.azure.com/.default";
 const azureADTokenProvider = getBearerTokenProvider(credential, scope);
-
+const deployment = "gpt-35-turbo";
 
 const client = new AzureOpenAI({ 
     endpoint, 
-    apiVersions,
+    apiVersion,
+    deployment,
     azureADTokenProvider
-     });
+});
 ```
 
 For more information about Azure OpenAI keyless authentication, see the "[Get started with the Azure OpenAI security building block](/azure/developer/ai/get-started-securing-your-ai-app?tabs=github-codespaces&pivots=typescript)" QuickStart article. 
 
-# [API Key](#tab/api-key)
 
-API Key
+### Configuration
+
+The `AzureClientOptions` object extends the OpenAI `ClientOptions` object. This Azure-specific client object is used to configure the connection and behavior of the Azure OpenAI client. It includes properties for specifying the properties unique to Azure.
 
-API keys are not recommended for production use because they are less secure than other authentication methods. 
+| Property | Details |
+|--|--|
+| apiVersion: `string` | Specifies the API version to use. |
+| azureADTokenProvider: `(() => Promise<string>)` | A function that returns an access token for Microsoft Entra (formerly known as Azure Active Directory), invoked on every request.|
+| deployment: `string` | A model deployment. If provided, sets the base client URL to include `/deployments/{deployment}`. Non-deployment endpoints can't be used (not supported with Assistants APIs).|
+| endpoint: `string` | Your Azure OpenAI endpoint with the following format: `https://RESOURCE-NAME.azure.openai.com/`.|
+
+# [API Key](#tab/api-key)
+
+API keys aren't recommended for production use because they're less secure than other authentication methods. 
 
 ```typescript
 import { AzureKeyCredential } from "@azure/openai";
 const apiKey = new AzureKeyCredential("your API key");
-const endpoint = "https://your-azure-openai-resource.com";0
+const endpoint = "https://your-azure-openai-resource.com";
 const apiVersion = "2024-10-21"
+const deployment = "gpt-35-turbo";
 
-const client = new AzureOpenAI({ apiKey, endpoint, apiVersion });
+const client = new AzureOpenAI({ 
+    apiKey, 
+    endpoint, 
+    apiVersion, 
+    deployment 
+});
 ```
 
-`AzureOpenAI` can be authenticated with an API key by setting the `AZURE_OPENAI_API_KEY` environment variable or by setting the `apiKey` string property in the options object when creating the `AzureOpenAI` client.
+### Configuration
 
-[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+The `AzureClientOptions` object extends the OpenAI `ClientOptions` object. This Azure-specific client object is used to configure the connection and behavior of the Azure OpenAI client. It includes properties for specifying the properties unique to Azure.
 
+| Property | Details |
+|--|--|
+| apiKey: `string` | Your API key for authenticating requests. |
+| apiVersion: `string` | Specifies the API version to use. |
+| deployment: `string` | A model deployment. If provided, sets the base client URL to include `/deployments/{deployment}`. Non-deployment endpoints can't be used (not supported with Assistants APIs).|
+| endpoint: `string` | Your Azure OpenAI endpoint with the following format: `https://RESOURCE-NAME.azure.openai.com/`.|
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 ---
 
+
 ## Audio
 
 ### Transcription
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript用Azure OpenAIクライアントの構成と機能の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのJavaScriptサポートに関するドキュメントの更新です。主な更新点は、クライアント構成に関する指示がより詳細になり、`AzureClientOptions`オブジェクトに関する情報が追加されたことです。このオブジェクトでは、Azure特有のプロパティを使用して接続や動作を構成できます。また、`apiKey`、`apiVersion`、`deployment`、`endpoint`の各プロパティの詳細がテーブル形式で整理され、明確に説明されています。

さらに、クライアントの認証方法に関する記述が改訂され、`getBearerTokenProvider`関数を使用してBearerトークンプロバイダーを作成する方法が示されています。この改善により、Azure OpenAIクライアントの使用時にユーザーが直面する可能性のある問題が軽減されます。

ドキュメントの全体的な構造も変更され、不要な情報が削除されたり、新しい注意事項が追加されたりしています。これにより、より一貫したユーザーフレンドリーな体験が提供されるようになっています。また、日付も2024年11月18日から2025年2月13日に更新されており、情報の新しさを保っています。

## articles/ai-services/openai/monitor-openai-reference.md{#item-8d8887}

<details>
<summary>Diff</summary>
````diff
@@ -31,10 +31,9 @@ Here are the most important metrics we think you should monitor for Azure OpenAI
 - Prompt Token Cache Match Rate
 - Time to Response
 - Time Between Tokens
-
 - Time to Last Byte
-
-- Normalized Time to First Byte 
+- Normalized Time to First Byte
+- Tokens per Second
 
 You can also monitor Content Safety metrics that are used by other Azure AI services. 
 - Blocked Volume
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIのモニタリング指標の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのモニタリング指標に関するドキュメントの更新を含んでいます。具体的には、監視すべき重要なメトリクスのリストが見直され、いくつかの指標が修正されました。新たに「Tokens per Second」という指標が追加され、これによりパフォーマンスの監視がより詳細化されています。

一方で、「Time to Last Byte」という指標が文書から削除され、これによりリストが簡潔になりました。その他の指標はそのまま残されており、ユーザーがAzure OpenAIのパフォーマンスを効率的に監視できるようになっています。全体として、これらの変更は、ドキュメントの明確性を向上させ、必要な情報に容易にアクセスできるようにする目的があります。


