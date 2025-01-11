---
date: '2025-01-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1227d31...MicrosoftDocs:28bc1fd
summary: この差分には、Azure OpenAIに関連する複数のドキュメントの更新が含まれています。主なポイントとして、新しいAPIバージョンの実装やコードサンプルの改良があります。特に、C#のコードサンプルにおいて大規模な変更が行われています。ドキュメントは最新のAPIバージョンに更新され、REST
  APIのリクエストボディに新しいパラメータが追加されました。これにより、認証情報の取り扱いがより明確になり、PythonとC#のサンプルコードが更新され、利用の利便性が向上しています。全体として、これらの更新はAzure
  OpenAIサービスの利用を推進し、ユーザーにとっての価値を向上させることを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1227d31...MicrosoftDocs:28bc1fd){target="_blank"}

# ハイライト

この差分には、Azure OpenAIに関連する複数のドキュメントの更新が含まれています。主なポイントは、新規APIバージョンの実装やコードサンプルの改良など、いくつかの重要な変更です。特に、破壊的な変更として、C#のコードサンプルの大規模な更新があります。

## 新機能

- Azure OpenAI APIに関するドキュメントは、最新のAPIバージョン「2024-10-01-preview」と「2024-10-21」に更新され、ユーザーは最新の機能にアクセスできるようになりました。
- REST APIのリクエストボディに新しいパラメータが追加され、認証情報がより明確に取り扱われるようになりました。

## 破壊的変更

- C#のコードサンプルで大規模な変更が行われ、一部のライブラリのインポートや関数名が変更されました。これにより、非同期ストリーミング機能に影響があります。

## その他の更新

- Pythonコードサンプルは、出力形式の変更とAPIバージョンの更新が含まれ、ユーザー側での理解と利用が容易になっています。
- ドキュメントの日付情報の更新も複数行われ、ユーザーは新しい情報にアクセスしやすくなっています。

# 洞察

この差分は、Azure OpenAIのAPI利用をより円滑にするための多様な改良を反映しています。APIバージョンの更新は、新しい機能の利用を容易にし、最新のプレビューリリースへの追従を促進します。特に、データプレーン著作APIのバージョン更新により、ユーザーはAzureのAIサービスで提供される最先端の機能を探求しやすくなります。

PythonおよびC#のコードサンプルの更新は、開発者が最新のSDKに合わせてコードを適合させるための良いガイドを提供します。Pythonの例での出力形式変更は、JSONの扱いをより簡潔かつ明確にし、実際の開発での使用に直結する利便性を向上させています。

また、REST APIの更新は、認証情報の明確化を通じて、セキュリティの向上とAPIリクエストの簡略化に寄与しています。これにより、APIの利用がより直感的になり、ユーザー体験が向上する一助となっています。

全体として、これらの更新は、Azure OpenAIサービスの利用を推進し、ユーザーにとっての価値を向上させます。今後の機能追加に備えるための基盤を整える重要なアップデートと言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [api-version-deprecation.md](#item-1cad50) | minor update | APIバージョンの更新と重要な情報の追加 | modified | 5 | 2 | 7 | 
| [api-surface.md](#item-a25fa2) | minor update | データプレーンの著作APIのバージョン更新 | modified | 1 | 1 | 2 | 
| [use-your-data-dotnet.md](#item-b811b8) | breaking change | コードサンプルの大幅な変更 | modified | 21 | 89 | 110 | 
| [use-your-data-python.md](#item-3dc5e2) | minor update | Pythonコードサンプルの更新 | modified | 4 | 3 | 7 | 
| [use-your-data-rest.md](#item-d1e071) | minor update | REST APIのコマンド更新 | modified | 9 | 5 | 14 | 
| [use-your-data-quickstart.md](#item-52c1f4) | minor update | クイックスタート日付の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/api-version-deprecation.md{#item-1cad50}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 01/08/2024
+ms.date: 01/10/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -25,7 +25,10 @@ This article is to help you understand the support lifecycle for the Azure OpenA
 Azure OpenAI API latest release:
 
 - Inference: [2024-12-01-preview](reference-preview.md)
-- Authoring: [2024-12-01-preview](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/2024-10-01-preview/azureopenai.json)
+- Authoring: [2024-10-01-preview](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/2024-10-01-preview/azureopenai.json)
+
+> [!IMPORTANT]
+> For features that are part of the dataplane authoring API such as batch, fine-tuning, and assistants files, continue to use API version `2024-10-01-preview` to take advantage of the latest preview features.
 
 This version contains support for the latest Azure OpenAI features including:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新と重要な情報の追加"
}
```

### Explanation
この修正は、Azure OpenAI APIに関するドキュメント「api-version-deprecation.md」の更新を含んでいます。主な変更点は、ドキュメントの日付が「2024年1月8日」から「2024年1月10日」に更新されたことと、新たに「重要な情報」セクションが追加されたことです。このセクションでは、データプレーンの著作APIに関連する機能、特にバッチ、ファインチューニング、アシスタントファイルについて、最新のプレビュー機能を利用するためにAPIバージョン「2024-10-01-preview」を使用することが強調されています。これにより、ユーザーは最新の機能を活用しやすくなることが期待されています。

## articles/ai-services/openai/includes/api-surface.md{#item-a25fa2}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ Each API surface/specification encapsulates a different set of Azure OpenAI capa
 | API | Latest preview release | Latest GA release | Specifications | Description |
 |:---|:----|:----|:----|:---|
 | **Control plane** | [`2024-06-01-preview`](/rest/api/aiservices/accountmanagement/operation-groups?view=rest-aiservices-accountmanagement-2024-06-01-preview&preserve-view=true) | [`2024-10-01`](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices) | Azure OpenAI shares a common control plane with all other Azure AI Services. The control plane API is used for things like [creating Azure OpenAI resources](/rest/api/aiservices/accountmanagement/accounts/create?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), [model deployment](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), and other higher level resource management tasks. The control plane also governs what is possible to do with capabilities like Azure Resource Manager, Bicep, Terraform, and Azure CLI.|
-| **Data plane - authoring** | `2024-12-01-preview` | `2024-10-21` | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
+| **Data plane - authoring** | `2024-10-01-preview` | `2024-10-21` | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
 | **Data plane - inference** | [`2024-12-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-10-21`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, speech/whisper, on your data, Dall-e, assistants, etc. |
 
 ## Authentication
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データプレーンの著作APIのバージョン更新"
}
```

### Explanation
この修正は、Azure OpenAIに関するドキュメント「api-surface.md」におけるデータプレーンの著作APIのバージョンの更新を反映しています。具体的には、「Data plane - authoring」の行で、最新のプレビューリリースが「2024-12-01-preview」から「2024-10-01-preview」に変更されました。この変更により、ユーザーはデータプレーンの著作APIを使用する際に、最新のプレビューバージョンを参照できるようになり、従来の情報がより正確性をもって維持されることが期待されます。この更新は、APIの利用者が新しい機能や更新を容易に把握できるようにするためのものです。

## articles/ai-services/openai/includes/use-your-data-dotnet.md{#item-b811b8}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: travisw
 ms.author: travisw
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 03/07/2024
+ms.date: 01/09/2025
 ---
 
 [!INCLUDE [Set up required variables](./use-your-data-common-variables.md)]
@@ -14,14 +14,12 @@ ms.date: 03/07/2024
 
 From the project directory, open the *Program.cs* file and replace its contents with the following code:
 
-### Without response streaming
-
 ```csharp
-using Azure;
+using System;
 using Azure.AI.OpenAI;
+using System.ClientModel;
 using Azure.AI.OpenAI.Chat;
 using OpenAI.Chat;
-using System.Text.Json;
 using static System.Environment;
 
 string azureOpenAIEndpoint = GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
@@ -31,36 +29,38 @@ string searchEndpoint = GetEnvironmentVariable("AZURE_AI_SEARCH_ENDPOINT");
 string searchKey = GetEnvironmentVariable("AZURE_AI_SEARCH_API_KEY");
 string searchIndex = GetEnvironmentVariable("AZURE_AI_SEARCH_INDEX");
 
-#pragma warning disable AOAI001
 AzureOpenAIClient azureClient = new(
-    new Uri(azureOpenAIEndpoint),
-    new AzureKeyCredential(azureOpenAIKey));
+			new Uri(azureOpenAIEndpoint),
+			new ApiKeyCredential(azureOpenAIKey));
 ChatClient chatClient = azureClient.GetChatClient(deploymentName);
 
+// Extension methods to use data sources with options are subject to SDK surface changes. Suppress the
+// warning to acknowledge and this and use the subject-to-change AddDataSource method.
+#pragma warning disable AOAI001
+
 ChatCompletionOptions options = new();
 options.AddDataSource(new AzureSearchChatDataSource()
 {
-    Endpoint = new Uri(searchEndpoint),
-    IndexName = searchIndex,
-    Authentication = DataSourceAuthentication.FromApiKey(searchKey),
+	Endpoint = new Uri(searchEndpoint),
+	IndexName = searchIndex,
+	Authentication = DataSourceAuthentication.FromApiKey(searchKey),
 });
 
 ChatCompletion completion = chatClient.CompleteChat(
-    [
-        new UserChatMessage("What are my available health plans?"),
-    ], options);
-
-Console.WriteLine(completion.Content[0].Text);
+	[
+		new UserChatMessage("What health plans are available?"),
+			],
+	options);
 
-AzureChatMessageContext onYourDataContext = completion.GetAzureMessageContext();
+ChatMessageContext onYourDataContext = completion.GetMessageContext();
 
 if (onYourDataContext?.Intent is not null)
 {
-    Console.WriteLine($"Intent: {onYourDataContext.Intent}");
+	Console.WriteLine($"Intent: {onYourDataContext.Intent}");
 }
-foreach (AzureChatCitation citation in onYourDataContext?.Citations ?? [])
+foreach (ChatCitation citation in onYourDataContext?.Citations ?? [])
 {
-    Console.WriteLine($"Citation: {citation.Content}");
+	Console.WriteLine($"Citation: {citation.Content}");
 }
 ```
 
@@ -86,72 +86,4 @@ Thank you for your interest in the Contoso electronics plan and benefit packages
 learn more about the various options available to you...// Omitted for brevity
 ```
 
-This will wait until the model has generated its entire response before printing the results. Alternatively, if you want to asynchronously stream the response and print the results, you can replace the contents of *Program.cs* with the code in the next example.
-
-### Async with streaming
-
-```csharp
-using Azure;
-using Azure.AI.OpenAI;
-using Azure.AI.OpenAI.Chat;
-using OpenAI.Chat;
-using static System.Environment;
-
-string azureOpenAIEndpoint = GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
-string azureOpenAIKey = GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
-string deploymentName = GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT_ID");
-string searchEndpoint = GetEnvironmentVariable("AZURE_AI_SEARCH_ENDPOINT");
-string searchKey = GetEnvironmentVariable("AZURE_AI_SEARCH_API_KEY");
-string searchIndex = GetEnvironmentVariable("AZURE_AI_SEARCH_INDEX");
-
-#pragma warning disable AOAI001
-
-AzureOpenAIClient azureClient = new(
-    new Uri(azureOpenAIEndpoint),
-    new AzureKeyCredential(azureOpenAIKey));
-ChatClient chatClient = azureClient.GetChatClient(deploymentName);
-
-ChatCompletionOptions options = new();
-options.AddDataSource(new AzureSearchChatDataSource()
-{
-    Endpoint = new Uri(searchEndpoint),
-    IndexName = searchIndex,
-    Authentication = DataSourceAuthentication.FromApiKey(searchKey),
-});
-
-var chatUpdates = chatClient.CompleteChatStreamingAsync(
-    [
-        new UserChatMessage("What are my available health plans?"),
-    ], options);
-
-AzureChatMessageContext onYourDataContext = null;
-await foreach (var chatUpdate in chatUpdates)
-{
-    if (chatUpdate.Role.HasValue)
-    {
-        Console.WriteLine($"{chatUpdate.Role}: ");
-    }
-
-    foreach (var contentPart in chatUpdate.ContentUpdate)
-    {
-        Console.Write(contentPart.Text);
-    }
-
-    if (onYourDataContext == null)
-    {
-        onYourDataContext = chatUpdate.GetAzureMessageContext();
-    }
-}
-
-Console.WriteLine();
-if (onYourDataContext?.Intent is not null)
-{
-    Console.WriteLine($"Intent: {onYourDataContext.Intent}");
-}
-foreach (AzureChatCitation citation in onYourDataContext?.Citations ?? [])
-{
-    Console.Write($"Citation: {citation.Content}");
-}
-```
-
-
+This will wait until the model has generated its entire response before printing the results.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "コードサンプルの大幅な変更"
}
```

### Explanation
この修正は、Azure OpenAIに関するドキュメント「use-your-data-dotnet.md」における主要な変更を示しています。主に、C#のコードサンプルが大幅に更新されたことが特徴です。具体的には、更新されたサンプルコードでは、いくつかのライブラリのインポートが変更され、`AzureOpenAIClient`のインスタンス化に使われるクレデンシャルが`ApiKeyCredential`に更新されました。さらに、関数やクラスの名前も変更され、一部の機能がサポートする形式にも変更が加えられています。

これに加えて、非同期ストリーミングに関する古いコードサンプルは、新しい例に置き換えられ、古い情報は削除されました。この変更により、ユーザーが最新のAPIを利用しやすくなり、また、より直感的なインターフェースが提供されることが期待されます。全体的に、コードサンプルは明確化され、最新のSDKに適応したものとなっています。

## articles/ai-services/openai/includes/use-your-data-python.md{#item-3dc5e2}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: mrbullwinkle #travisw
 ms.author: mbullwin #travisw
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 03/07/2024
+ms.date: 01/10/2025
 ---
 
 [!INCLUDE [Set up required variables](./use-your-data-common-variables.md)]
@@ -59,7 +59,7 @@ deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT_ID")
 client = openai.AzureOpenAI(
     azure_endpoint=endpoint,
     api_key=api_key,
-    api_version="2024-02-01",
+    api_version="2024-10-21",
 )
 
 completion = client.chat.completions.create(
@@ -87,7 +87,8 @@ completion = client.chat.completions.create(
     }
 )
 
-print(completion.model_dump_json(indent=2))
+print(f"{completion.choices[0].message.role}: {completion.choices[0].message.content}")
+
 ```
 
 # [OpenAI Python 0.28.1](#tab/python)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonコードサンプルの更新"
}
```

### Explanation
この修正は、Azure OpenAIに関するドキュメント「use-your-data-python.md」におけるPythonコードサンプルの更新を反映しています。主な変更点は、`api_version`の値が「2024-02-01」から「2024-10-21」に変更されたことです。この更新により、ユーザーは新しいAPIバージョンに基づいた機能を利用できるようになります。

また、コードの出力形式が変更され、`print`文が`completion.model_dump_json(indent=2)`から、`completion.choices[0].message.role`および`completion.choices[0].message.content`を用いて新しい形式で結果を表示するように修正されました。これにより、出力の内容がより明確で、ユーザーにとって理解しやすくなっています。この変更は、ドキュメントの整合性を高め、最新のAPI機能に適応するためのものです。

## articles/ai-services/openai/includes/use-your-data-rest.md{#item-d1e071}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: aahill
 ms.author: aahi
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 03/07/2024
+ms.date: 01/10/2025
 ---
 
 [!INCLUDE [Set up required variables](./use-your-data-common-variables.md)]
@@ -20,7 +20,7 @@ To trigger a response from the model, you should end with a user message indicat
 > There are several parameters you can use to change the model's response, such as `temperature` or `top_p`. See the [reference documentation](../reference.md#completions-extensions) for more information.
 
 ```bash
-curl -i -X POST $AZURE_OPENAI_ENDPOINT/openai/deployments/$AZURE_OPENAI_DEPLOYMENT_ID/chat/completions?api-version=2024-02-15-preview \
+curl -i -X POST $AZURE_OPENAI_ENDPOINT/openai/deployments/$AZURE_OPENAI_DEPLOYMENT_ID/chat/completions?api-version=2024-10-21 \
 -H "Content-Type: application/json" \
 -H "api-key: $AZURE_OPENAI_API_KEY" \
 -d \
@@ -31,8 +31,11 @@ curl -i -X POST $AZURE_OPENAI_ENDPOINT/openai/deployments/$AZURE_OPENAI_DEPLOYME
             "type": "azure_search",
             "parameters": {
                 "endpoint": "'$AZURE_AI_SEARCH_ENDPOINT'",
-                "key": "'$AZURE_AI_SEARCH_API_KEY'",
-                "index_name": "'$AZURE_AI_SEARCH_INDEX'"
+                "index_name": "'$AZURE_AI_SEARCH_INDEX'",
+                "authentication": {
+                    "type": "api_key",
+                    "key": "'$AZURE_AI_SEARCH_API_KEY'"
+                }
             }
         }
     ],
@@ -81,7 +84,8 @@ curl -i -X POST $AZURE_OPENAI_ENDPOINT/openai/deployments/$AZURE_OPENAI_DEPLOYME
         "prompt_tokens": 3779,
         "completion_tokens": 105,
         "total_tokens": 3884
-    }
+    },
+    "system_fingerprint": "fp_65792305e4"
 }
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIのコマンド更新"
}
```

### Explanation
この修正は、Azure OpenAIに関するドキュメント「use-your-data-rest.md」において、REST APIを使用するためのコマンドが更新された内容を反映しています。主な変更点は、APIバージョンの更新と、リクエストのボディ内での新しいパラメータの追加です。

具体的には、APIバージョンが「2024-02-15-preview」から「2024-10-21」に変更されました。また、リクエストの構造において、検索用の認証情報が`authentication`オブジェクトとして追加され、APIキーを含む新しいパラメータが導入されています。この変更により、ユーザーはより明確に認証情報を提供できるようになります。

さらに、レスポンスの例に新しいフィールド「system_fingerprint」が追加され、応答の詳細が充実しています。これらの更新は、最新のAPI仕様に対応するものであり、ドキュメントの内容が最新化されたことを示しています。

## articles/ai-services/openai/use-your-data-quickstart.md{#item-52c1f4}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom: devx-track-dotnet, devx-track-extended-java, devx-track-js, devx-trac
 ms.topic: quickstart
 author: aahill
 ms.author: aahi
-ms.date: 10/22/2024
+ms.date: 01/09/2025
 recommendations: false
 zone_pivot_groups: openai-use-your-data
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタート日付の更新"
}
```

### Explanation
この修正は、「use-your-data-quickstart.md」ドキュメントにおける変更を反映しています。主な変更点は、ドキュメントの最終更新日が「2024年10月22日」から「2025年1月9日」に変更されたことです。このアップデートにより、ユーザーは新しい情報や機能に基づいた最新のクイックスタートガイドを参照できるようになります。

具体的には、ドキュメントのメタデータに含まれる日付情報が修正されたことが影響しています。この変更は、ドキュメントの正確性を保ち、ユーザーに最新の見解を提供するために重要です。全体として、これはドキュメント改善に向けた軽微な更新であり、ユーザーの利便性向上を図っています。


