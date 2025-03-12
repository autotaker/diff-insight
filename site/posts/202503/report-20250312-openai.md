---
date: '2025-03-12'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f35ae63...MicrosoftDocs:3791c10
summary: |-
  今回の変更は、Azure OpenAIサービス関連のドキュメントに対するマイナーアップデートを行ったもので、特にモデルのリタイアメントやアップグレード日、セクションタイトルの修正、手順の具体化、認証手順の改善、プログラム名や日付の更新に焦点が当てられています。新機能としては、DALL-EやGPT-4 Turbo with Visionモデルの認証方法の改善や、テキスト読み上げ機能、Whisperモデルのサンプルコードの向上が含まれています。特に大きな破壊的変更はありませんが、古いファイル名での手順が通用しなくなる可能性があります。

  ドキュメント更新は、開発者がより正確で最新の情報に基づいてシステムを構築できるようにするためのもので、手順の明確化や具体化が施されています。これにより誤解や混乱を防ぎ、セキュリティ面ではパスワードレス認証が推奨されています。モデルのリリースやリタイアメントの日付が明確にされ、計画的なアップデートやメンテナンスが容易になり、ビジネスエンティティにとって効率的なリソース管理が可能となります。全体として、ユーザーに向けたエクスペリエンスが大幅に向上し、Azure OpenAIサービスがより利用しやすくなっています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f35ae63...MicrosoftDocs:3791c10){target="_blank"}

<format>
# Highlights
今回の変更は、Azure OpenAIサービス関連のドキュメントに対するいくつかのマイナーアップデートを行ったものです。特に、モデルのリタイアメントやアップグレード日、セクションタイトルの修正、手順の具体化、認証手順の改善、プログラム名や日付の更新に焦点が当てられています。

## New features
- DALL-EやGPT-4 Turbo with Visionモデルで推奨される認証方法に関する改善。
- テキスト読み上げ機能やWhisperモデルのサンプルコードの向上。
- セキュリティ対策の強化、特に Azure Key Vault の使用推奨。

## Breaking changes
- 特に大きな破壊的変更はありませんが、ファイル名の表記統一によって、古いファイル名での手順が通用しなくなる可能性があります。

## Other updates
- モデルのリタイアメント日やアップグレード開始日の変更。
- セクションタイトルの見直しによるコンテンツの焦点の明確化。
- サービス名や日付の一貫性を保つための修正。

# Insights
今回のドキュメント更新は、Azure OpenAIを利用する開発者がより正確で最新の情報に基づいてシステムを構築できるようにするためのものです。具体的には、手順の明確化や具体化により、ユーザーが手順を誤解したり、混乱したりすることを防ぐための工夫が施されています。

実際のコードや設定に関わる変更として、ファイル名の変更（`program.cs`から`Program.cs`）や、セクションタイトルの変更により、利用者の期待する内容に即したドキュメント構成に直されています。また、認証手続きのセキュリティ面での改善が行われ、パスワードレス認証が推奨されています。これはクラウドベースのセキュリティを強化し、ユーザーがリスクを最小限に抑えられるようにするための重要な改良です。

さらに、モデルのリリースやリタイアメントの日付が明確にされたことで、組織としての計画的なアップデートやメンテナンスが容易になります。これにより、ビジネスエンティティはより効率的にリソースを管理し、最先端のAI技術を活用しながら顧客に対するサービスの質を維持・向上させることが可能になります。

全体として、多くの小さな改善が積み重なることでユーザーに向けたエクスペリエンスが大幅に向上され、Azure OpenAIサービスがより利用しやすくなっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルのリタイアメントおよびアップグレードに関する日付の変更 | modified | 4 | 4 | 8 | 
| [assistants-csharp.md](#item-cc4697) | minor update | クイックスタートのセクションタイトルと日付の変更 | modified | 5 | 5 | 10 | 
| [chatgpt-dotnet.md](#item-2563fb) | minor update | クイックスタートに関するセクションタイトルと日付の変更 | modified | 9 | 8 | 17 | 
| [dall-e-dotnet.md](#item-755f0a) | minor update | DALL-EのC#サンプルコードの更新 | modified | 74 | 56 | 130 | 
| [dotnet.md](#item-aca852) | minor update | プログラムファイル名の表記の統一 | modified | 2 | 2 | 4 | 
| [gpt-v-dotnet.md](#item-120a68) | minor update | GPT-4 Turbo with Visionモデルに関するドキュメントの更新 | modified | 58 | 47 | 105 | 
| [text-to-speech-dotnet.md](#item-fea66a) | minor update | テキスト読み上げの設定方法に関するドキュメントの更新 | modified | 50 | 39 | 89 | 
| [use-your-data-dotnet.md](#item-b811b8) | minor update | データ使用に関する.NETドキュメントの更新 | modified | 2 | 2 | 4 | 
| [whisper-dotnet.md](#item-562a58) | minor update | Whisperモデルに関する.NETドキュメントの改訂 | modified | 64 | 50 | 114 | 
| [whisper-python.md](#item-e61179) | minor update | Whisperモデルに関するPythonドキュメントのサービス名更新 | modified | 1 | 1 | 2 | 
| [realtime-audio-reference.md](#item-276d51) | minor update | リアルタイム音声参照ドキュメントの入力トークンの詳細の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 02/28/2025
+ms.date: 03/11/2025
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -103,7 +103,7 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-4` | 1106-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than March 10, 2025 **<sup>1</sup>** <br>Retirement date: April 02, 2025  | `gpt-4o`|
 | `gpt-4` | 0125-preview |To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than March 10, 2025 **<sup>1</sup>** <br>Retirement date: April 02, 2025  | `gpt-4o` |
 | `gpt-4` | vision-preview | To be upgraded to **`gpt-4o` version: `2024-11-20`**, starting no sooner than March 10, 2025  **<sup>1</sup>** <br>Retirement date: April 02, 2025 | `gpt-4o`|
-| `gpt-4o` | 2024-05-13 | No earlier than May 20, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on February 13, 2025. | |
+| `gpt-4o` | 2024-05-13 | No earlier than June 30, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on March 17, 2025. | |
 | `gpt-4o` | 2024-08-06 | No earlier than August 6, 2025  | |
 | `gpt-4o` | 2024-11-20 | No earlier than November 20, 2025  | |
 | `gpt-4o-mini` | 2024-07-18 | No earlier than July 18, 2025  | |
@@ -113,8 +113,8 @@ These models are currently available for use in Azure OpenAI Service.
 | `o1` | 2024-12-17 | No earlier than December 17, 2025 | |
 | `text-embedding-ada-002` | 2 | No earlier than October 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
 | `text-embedding-ada-002` | 1 | No earlier than October 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
-| `text-embedding-3-small` | | No earlier than October 3, 2025 | |
-| `text-embedding-3-large` | | No earlier than October 3, 2025 | |
+| `text-embedding-3-small` | | No earlier than January 25, 2026 | |
+| `text-embedding-3-large` | | No earlier than January 25, 2026 | |
 
  **<sup>1</sup>** We'll notify all customers with these preview deployments at least 30 days before the start of the upgrades. We'll publish an upgrade schedule detailing the order of regions and model versions that we'll follow during the upgrades, and link to that schedule from here.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのリタイアメントおよびアップグレードに関する日付の変更"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるモデルのリタイアメントとアップグレードに関する日付を更新するものです。具体的には、いくつかのモデルのリタイアメントおよびアップグレードの開始日が変更されました。

1. **更新された日付**: `ms.date`フィールドが2025年2月28日から2025年3月11日に変更されています。これにより、文書の最新性が維持されます。
2. **モデルのアップグレード開始日**: `gpt-4o`モデルのアップグレード開始日が、2025年3月10日から2025年3月17日に変更されました。また、これに伴い、予定されていた自動アップデートの関連情報も更新されています。
3. **リタイアメント日**: `gpt-4`モデルとその関連モデルのリタイアメント日が、2025年4月2日として維持されています。
4. **テキスト埋め込みモデルの新しい日付**: `text-embedding-3-small`および`text-embedding-3-large`モデルのリタイアメント日が2025年10月3日から2026年1月25日に延長されています。

この更新は、ユーザーに対して最新のモデルの展開スケジュールを提供し、より良い計画と準備を可能にすることを目的としています。

## articles/ai-services/openai/includes/assistants-csharp.md{#item-cc4697}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: aapowell
 ms.author: aapowell
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 3/10/2025
+ms.date: 3/11/2025
 ---
 
 [Reference documentation](/dotnet/api/overview/azure/ai.openai.assistants-readme?context=/azure/ai-services/openai/context/context) |  [Source code](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/openai/Azure.AI.OpenAI/src) | [Package (NuGet)](https://www.nuget.org/packages/Azure.AI.OpenAI/)
@@ -62,9 +62,9 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 [!INCLUDE [resource authentication](resource-authentication.md)]
 
-## Create the assistant
+## Run the quickstart
 
-The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
+The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with an `AzureKeyCredential` object. 
 
 #### [Microsoft Entra ID](#tab/keyless)
 
@@ -79,9 +79,9 @@ AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new Az
 ```
 ---
 
-To create an assistant, you need to:
+To run the quickstart, follow these steps:
 
-1. Update the `Program.cs` file with the following code to create an assistant:
+1. Replace the contents of `Program.cs` with the following code and update the placeholder values with your own.
     
     ```csharp
     using Azure;
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートのセクションタイトルと日付の変更"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関する記事の一部、特にC#向けアシスタントのセクションを更新するものです。変更点は以下の通りです。

1. **日付の更新**: フィールド`ms.date`が2025年3月10日から2025年3月11日に変更され、文書の最新性が保たれています。
   
2. **セクションタイトルの変更**: セクションタイトルが「アシスタントを作成する」から「クイックスタートを実行する」に変更されました。この変更は、内容が実際にアシスタントの作成プロセスからクイックスタートの実行方法に焦点を移すことを反映しています。

3. **手順の更新**: 初期の手順が修正され、プログラムファイルを更新する際に、「アシスタントを作成する」という表現から、「プログラムの内容を置き換え、プレースホルダの値を自分のものに更新する」と具体的な指示に変更されています。これにより、ユーザーが手順をより理解しやすくなりました。

これらの変更は、ユーザーに対してより明確で最新の情報を提供し、クイックスタートプロセスの理解を深めることを目的としています。

## articles/ai-services/openai/includes/chatgpt-dotnet.md{#item-2563fb}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-openai
 ms.topic: include
 author: mrbullwinkle
 ms.author: mbullwin
-ms.date: 11/15/2023
+ms.date: 3/11/2025
 ---
 
 [Source code](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/openai/Azure.AI.OpenAI/src) | [Package (NuGet)](https://www.nuget.org/packages/Azure.AI.OpenAI/) | [Samples](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/openai/Azure.AI.OpenAI/tests/Samples)| [Retrieval Augmented Generation (RAG) enterprise chat template](/dotnet/ai/get-started-app-chat-template) |
@@ -60,9 +60,9 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 [!INCLUDE [resource authentication](resource-authentication.md)]
 
-## Add the code for chat completion
+## Run the quickstart
 
-The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
+The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with an `AzureKeyCredential` object. 
 
 #### [Microsoft Entra ID](#tab/keyless)
 
@@ -81,9 +81,9 @@ You can use streaming or non-streaming to get the chat completion. The following
 
 ### Without response streaming
 
-To use the non-streaming method:
+To run the quickstart, follow these steps:
 
-1. Update the `Program.cs` file with the following code:
+1. Replace the contents of `Program.cs` with the following code and update the placeholder values with your own.
 
     ```csharp
     using Azure;
@@ -127,12 +127,13 @@ To use the non-streaming method:
 Assistant: Arrr, ye be askin’ a fine question, matey! Aye, several Azure AI services support customer-managed keys (CMK)! This lets ye take the wheel and secure yer data with encryption keys stored in Azure Key Vault. Services such as Azure Machine Learning, Azure Cognitive Search, and others also offer CMK fer data protection. Always check the specific service's documentation fer the latest updates, as features tend to shift swifter than the tides, aye!
 ```
 
-This will wait until the model has generated its entire response before printing the results. Alternatively, if you want to asynchronously stream the response and print the results, you can replace the contents of *program.cs* with the code in the next example.
+This will wait until the model has generated its entire response before printing the results. Alternatively, if you want to asynchronously stream the response and print the results, you can replace the contents of *Program.cs* with the code in the next example.
 
 ### Async with streaming
 
-To use the streaming method:
-1. Update the `Program.cs` file with the following code:
+To run the quickstart, follow these steps:
+
+1. Replace the contents of `Program.cs` with the following code and update the placeholder values with your own.
 
     ```csharp
     using Azure;
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートに関するセクションタイトルと日付の変更"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるChatGPTのC#向けの実装に関するドキュメントを更新するものです。主な変更点は以下の通りです。

1. **日付の更新**: `ms.date`が2023年11月15日から2025年3月11日に変更され、ドキュメントの最新性が確保されています。

2. **セクションタイトルの変更**: セクションタイトルが「チャット完了のためのコードを追加」から「クイックスタートを実行する」に変更されており、内容の焦点をより明確に示しています。

3. **手順の具体化**: 手順が更新され、プログラムの内容を置き換え、プレースホルダの値を自分のものに更新するように促す具体的な指示が追加されています。

これらの変更は、ユーザーがクイックスタートをより理解しやすくするために、内容の明確性と最新の情報提供を図っています。また、ドキュメント全体の一貫性が保たれるように見直されています。

## articles/ai-services/openai/includes/dall-e-dotnet.md{#item-755f0a}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-openai
 ms.topic: include
 author: PatrickFarley
 ms.author: pafarley
-ms.date: 06/26/2024
+ms.date: 3/11/2025
 ---
 
 Use this guide to get started generating images with the Azure OpenAI SDK for C#.
@@ -21,83 +21,101 @@ Use this guide to get started generating images with the Azure OpenAI SDK for C#
 - The [.NET 7 SDK](https://dotnet.microsoft.com/download/dotnet/7.0)
 - An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
+### Microsoft Entra ID prerequisites
 
-## Setup
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-[!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
+## Set up
 
-[!INCLUDE [environment-variables](environment-variables.md)]
+1. Create a new folder `vision-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
+    ```shell
+    mkdir vision-quickstart && cd vision-quickstart
+    ```
 
-## Create a new .NET Core application
+1. Create a new console application with the following command:
 
-In a console window (such as cmd, PowerShell, or Bash), use the `dotnet new` command to create a new console app with the name `azure-openai-quickstart`. This command creates a simple "Hello World" project with a single C# source file: *Program.cs*.
+    ```shell
+    dotnet new console
+    ```
 
-```dotnetcli
-dotnet new console -n azure-openai-quickstart
-```
+3. Install the [OpenAI .NET client library](https://www.nuget.org/packages/Azure.AI.OpenAI/) with the [dotnet add package](/dotnet/core/tools/dotnet-add-package) command:
 
-Change your directory to the newly created app folder. You can build the application with:
+    ```console
+    dotnet add package Azure.AI.OpenAI --version 1.0.0-beta.6
+    ```
 
-```dotnetcli
-dotnet build
-```
+1. For the **recommended** keyless authentication with Microsoft Entra ID, install the [Azure.Identity](https://www.nuget.org/packages/Azure.Identity) package with:
 
-The build output should contain no warnings or errors.
+    ```console
+    dotnet add package Azure.Identity
+    ```
 
-```output
-...
-Build succeeded.
- 0 Warning(s)
- 0 Error(s)
-...
-```
+1. For the **recommended** keyless authentication with Microsoft Entra ID, sign in to Azure with the following command:
 
-## Install the OpenAI .NET SDK
+    ```console
+    az login
+    ```
 
-Install the client library with:
+## Retrieve resource information
 
-```dotnetcli
-dotnet add package Azure.AI.OpenAI --version 1.0.0-beta.6
-```
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
-## Generate images with DALL-E
+## Run the quickstart
 
-From the project directory, open the *program.cs* file and replace the contents with the following code:
+The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with an `AzureKeyCredential` object. 
+
+#### [Microsoft Entra ID](#tab/keyless)
 
 ```csharp
-using Azure;
-using Azure.AI.OpenAI;
-using OpenAI.Images;
-using static System.Environment;
-
-string endpoint = GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
-string key = GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
-
-AzureOpenAIClient openAIClient = new(
-    new Uri(endpoint),
-    new AzureKeyCredential(key));
-
-// This must match the custom deployment name you chose for your model
-ImageClient chatClient = openAIClient.GetImageClient("dalle-3");
-
-var imageGeneration = await chatClient.GenerateImageAsync(
-        "a happy monkey sitting in a tree, in watercolor",
-        new ImageGenerationOptions()
-        {
-            Size = GeneratedImageSize.W1024xH1024
-        }
-    );
-
-Console.WriteLine(imageGeneration.Value.ImageUri);
+AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new DefaultAzureCredential()); 
 ```
 
-Build and run the application from your application directory with these commands:
+#### [API key](#tab/api-key)
 
-```dotnet
-dotnet build
-dotnet run
+```csharp
+AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new AzureKeyCredential(key));
 ```
+---
+
+To run the quickstart, follow these steps:
+
+1. Replace the contents of `Program.cs` with the following code and update the placeholder values with your own.
+
+    ```csharp
+    using Azure;
+    using Azure.AI.OpenAI;
+    using OpenAI.Images;
+    using static System.Environment;
+    
+    string endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT") ?? "https://<your-resource-name>.openai.azure.com/";
+    string key = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY") ?? "<your-key>";
+    
+    // Use the recommended keyless credential instead of the AzureKeyCredential credential.
+    AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new DefaultAzureCredential()); 
+    //AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new AzureKeyCredential(key));
+    
+    // This must match the custom deployment name you chose for your model
+    ImageClient chatClient = openAIClient.GetImageClient("dalle-3");
+    
+    var imageGeneration = await chatClient.GenerateImageAsync(
+            "a happy monkey sitting in a tree, in watercolor",
+            new ImageGenerationOptions()
+            {
+                Size = GeneratedImageSize.W1024xH1024
+            }
+        );
+    
+    Console.WriteLine(imageGeneration.Value.ImageUri);
+    ```
+
+1. Run the application using the `dotnet run` command or the run button at the top of Visual Studio:
+
+    ```dotnetcli
+    dotnet run
+    ```
 
 ## Output
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL-EのC#サンプルコードの更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連つけられたDALL-EのC#プログラミングに関するガイドラインを更新するものです。主に以下の点が修正されています。

1. **日付の更新**: `ms.date`が2024年6月26日から2025年3月11日に変更されたことで、文書の最新性が維持されています。

2. **Microsoft Entra IDの認証情報**: 認証に関するセクションが追加され、Microsoft Entra IDでのキーレス認証に必要な手順が明確に示されています。

3. **手順の詳細化**: アプリケーションのセットアップ手順がより詳細に説明されており、新しいフォルダの作成、コンソールアプリケーションの生成、必要なパッケージのインストール方法が具体的に示されています。また、プログラムファイル`Program.cs`の内容を変更するための具体的なコード例が提供されています。

4. **サンプルコードの明確化**: DALL-Eを使用した画像生成のサンプルコードが更新され、環境変数を使用してエンドポイントやAPIキーを取得する方法が紹介されています。また、推奨されるキーレス認証とAPIキーの使用方法がそれぞれ明記されています。

これらの変更は、ユーザーがDALL-Eを利用する際のセットアップや実行プロセスをより理解しやすくするために行われたもので、全体としてガイドの明確性と実用性が向上しています。

## articles/ai-services/openai/includes/dotnet.md{#item-aca852}

<details>
<summary>Diff</summary>
````diff
@@ -62,7 +62,7 @@ dotnet add package Azure.AI.OpenAI --version 1.0.0-beta.17
 
 ## Create a sample application
 
-From the project directory, open the *program.cs* file and replace with the following code:
+From the project directory, open the *Program.cs* file and replace with the following code:
 
 ```csharp
 using Azure;
@@ -91,7 +91,7 @@ Console.WriteLine($"Chatbot: {completion}");
 > For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see the Azure AI services [security](../../security-features.md) article.
 
 ```cmd
-dotnet run program.cs
+dotnet run Program.cs
 ```
 
 ## Output
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プログラムファイル名の表記の統一"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスに関するC#のサンプルアプリケーションのドキュメントにおける minor update です。主に以下の点に関する修正が行われました。

1. **ファイル名の表記統一**: `program.cs`の表記が`Program.cs`に統一されました。この変更は、C#におけるファイル名の通常の命名規則に従ったもので、コードの可読性や一貫性を向上させることを目的としています。

2. **コマンドの修正**: コマンドラインの実行についても、同様に`program.cs`から`Program.cs`への修正が行われ、正確なファイル名が反映されています。

これらの変更により、ユーザーがサンプルアプリケーションを設定する際に正しいファイル名を使用しやすくなり、手順の明確さが向上しています。全体として、ドキュメントの整合性を高めるための重要な調整です。

## articles/ai-services/openai/includes/gpt-v-dotnet.md{#item-120a68}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 01/22/2024
+ms.date: 3/11/2025
 ---
 
 Use this article to get started using the Azure OpenAI .NET SDK to deploy and use the GPT-4 Turbo with Vision model. 
@@ -18,98 +18,109 @@ Use this article to get started using the Azure OpenAI .NET SDK to deploy and us
 - [The .NET 8.0 SDK](https://dotnet.microsoft.com/en-us/download)
 - An Azure OpenAI Service resource with a GPT-4 Turbo with Vision model deployed. See [GPT-4 and GPT-4 Turbo Preview model availability](../concepts/models.md#gpt-4-and-gpt-4-turbo-model-availability) for available regions. For more information about resource creation, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).
 
-## Set up
+### Microsoft Entra ID prerequisites
 
-### Retrieve key and endpoint
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-To successfully make a call against Azure OpenAI, you need an **endpoint** and a **key**.
+## Set up
 
-|Variable name | Value |
-|--------------------------|-------------|
-| `AZURE_OPENAI_ENDPOINT`               | The service endpoint can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the endpoint via the **Deployments** page in Azure AI Foundry portal. An example endpoint is: `https://docs-test-001.openai.azure.com/`. |
-| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+1. Create a new folder `vision-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+    ```shell
+    mkdir vision-quickstart && cd vision-quickstart
+    ```
 
-:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location highlighted." lightbox="../media/quickstarts/endpoint.png":::
+1. Create a new console application with the following command:
 
+    ```shell
+    dotnet new console
+    ```
 
-## Create the .NET app
+3. Install the [OpenAI .NET client library](https://www.nuget.org/packages/Azure.AI.OpenAI/) with the [dotnet add package](/dotnet/core/tools/dotnet-add-package) command:
 
-1. Create a .NET app using the `dotnet new` command:
+    ```console
+    dotnet add package Azure.AI.OpenAI
+    ```
 
-    ```dotnetcli
-    dotnet new console -n OpenAISpeech
+1. For the **recommended** keyless authentication with Microsoft Entra ID, install the [Azure.Identity](https://www.nuget.org/packages/Azure.Identity) package with:
+
+    ```console
+    dotnet add package Azure.Identity
     ```
 
-1. Change into the directory of the new app:
+1. For the **recommended** keyless authentication with Microsoft Entra ID, sign in to Azure with the following command:
 
-    ```dotnetcli
-    cd OpenAISpeech
+    ```console
+    az login
     ```
 
-## Install the client library
+## Retrieve resource information
 
-Install the [`Azure.OpenAI`](https://www.nuget.org/packages/Azure.AI.OpenAI/) client library:
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
-```dotnetcli
-dotnet add package Azure.AI.OpenAI
-```
+## Run the quickstart
 
-## Passwordless authentication is recommended
+The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with an `AzureKeyCredential` object. 
 
-Passwordless authentication is more secure than key-based alternatives and is the recommended approach for connecting to Azure services. If you choose to use Passwordless authentication, you'll need to complete the following:
+#### [Microsoft Entra ID](#tab/keyless)
 
-1. Add the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package.
+```csharp
+AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new DefaultAzureCredential()); 
+```
 
-    ```dotnetcli
-    dotnet add package Azure.Identity
-    ```
+#### [API key](#tab/api-key)
 
-1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal on your OpenAI resource under **Access control (IAM)** > **Add role assignment**.
-1. Sign-in to Azure using Visual Studio or the Azure CLI via `az login`.
+```csharp
+AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new AzureKeyCredential(key));
+```
+---
 
-## Update the app code
+To run the quickstart, follow these steps:
 
-1. Replace the contents of `program.cs` with the following code and update the placeholder values with your own.
+1. Replace the contents of `Program.cs` with the following code and update the placeholder values with your own.
 
     ```csharp
     using Azure;
     using Azure.AI.OpenAI;
     using Azure.Identity;
     using OpenAI.Chat; // Required for Passwordless auth
     
-    var endpoint = new Uri("YOUR_AZURE_OPENAI_ENDPOINT");
-    var credentials = new AzureKeyCredential("YOUR_AZURE_OPENAI_KEY");
-    // var credentials = new DefaultAzureCredential(); // Use this line for Passwordless auth
-    var deploymentName = "gpt-4"; // Default name, update with your own if needed
+    string deploymentName = "gpt-4";
     
-    AzureOpenAIClient openAIClient = new AzureOpenAIClient(endpoint, credentials);
+    string endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT") ?? "https://<your-resource-name>.openai.azure.com/";
+    string key = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY") ?? "<your-key>";
+    
+    // Use the recommended keyless credential instead of the AzureKeyCredential credential.
+    AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new DefaultAzureCredential()); 
+    //AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new AzureKeyCredential(key));
+
     var chatClient = openAIClient.GetChatClient(deploymentName);
     
     var imageUri = "YOUR_IMAGE_URL";
     
-    List<ChatMessage> messages = [
-        new UserChatMessage(
-            ChatMessageContentPart.CreateTextMessageContentPart("Please describe the following image:"),
-            ChatMessageContentPart.CreateImageMessageContentPart(new Uri(imageUri), "image/png"))
-    ];
-    
-    ChatCompletion chatCompletion = await chatClient.CompleteChatAsync(messages);
+    var chatMessages = new List<ChatMessage>
+    {
+        new SystemChatMessage("You are a helpful assistant."),
+        new UserChatMessage($"Describe this picture: {imageUrl}")
+    };
+        
+    ChatCompletion chatCompletion = await chatClient.CompleteChatAsync(chatMessages);
     
     Console.WriteLine($"[ASSISTANT]:");
     Console.WriteLine($"{chatCompletion.Content[0].Text}");
     ```
 
-[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv-expanded.md)]
-
 1. Run the application using the `dotnet run` command or the run button at the top of Visual Studio:
 
     ```dotnetcli
     dotnet run
     ```
 
-  The app generates an audio file at the location you specified for the `speechFilePath` variable. Play the file on your device to hear the generated audio.
+## Output
+
+The output of the application will be a description of the image you provided in the `imageUri` variable. The assistant will analyze the image and provide a detailed description based on its content.
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turbo with Visionモデルに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAI .NET SDKを使用してGPT-4 Turbo with Visionモデルをデプロイし利用するためのガイドを更新するものです。主な修正点は以下の通りです。

1. **日付の更新**: `ms.date` が2024年1月22日から2025年3月11日に変更され、文書の最新性が提供されています。

2. **認証手順の改善**: Microsoft Entra IDを使用したキーレス認証に関する情報がセクションとして整理されており、必須の手順や役割の割り当て方法について詳述されています。

3. **セットアップ手順の詳細化**: 新しいフォルダー作成やコンソールアプリケーションの生成手順が追加され、ユーザーがこれらの手順に従いやすくなっています。

4. **コードの具体性向上**: サンプルコードが更新され、エンドポイントやAPIキーの取得方法が環境変数を使用する形で示されています。また、従来の認証方法に加えて、推奨されるキーレス認証への切り替えについての明確な指示が含まれています。

5. **サンプル実行時の出力に関する情報の強化**: アプリケーションの出力として、提供された画像に対する説明が得られる旨が説明され、ユーザーに対してその目的が明示されています。

これらの変更は、ユーザーがGPT-4 Turbo with Visionモデルを理解し、設定する際の手助けをするために行われたものであり、全体としてドキュメントの明瞭さと実用性が向上しています。

## articles/ai-services/openai/includes/text-to-speech-dotnet.md{#item-fea66a}

<details>
<summary>Diff</summary>
````diff
@@ -2,11 +2,10 @@
 ms.topic: include
 manager: nitinme
 ms.service: azure-ai-openai
-ms.topic: include
-ms.date: 09/23/2024
-ms.reviewer: eur
-ms.author: alexwolf
-author: alexwolfmsft
+ms.date: 3/11/2025
+ms.reviewer: alexwolf
+ms.author: eur
+author: eric-urban
 recommendations: false
 ---
 
@@ -16,62 +15,72 @@ recommendations: false
 - An Azure OpenAI resource with a Whisper model deployed in a [supported region](../concepts/models.md#whisper-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 - [The .NET 8.0 SDK](https://dotnet.microsoft.com/en-us/download)
 
-## Create the .NET app
+### Microsoft Entra ID prerequisites
 
-1. Create a .NET app using the `dotnet new` command:
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-    ```dotnetcli
-    dotnet new console -n TextToSpeech
-    ```
+## Set up
 
-1. Change into the directory of the new app:
+1. Create a new folder `to-speech-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-    ```dotnetcli
-    cd OpenAISpeech
+    ```shell
+    mkdir to-speech-quickstart && cd to-speech-quickstart
     ```
 
-1. Install the [`Azure.OpenAI`](https://www.nuget.org/packages/Azure.AI.OpenAI/) client library:
-    
-    ```dotnetcli
-    dotnet add package Azure.AI.OpenAI
+1. Create a new console application with the following command:
+
+    ```shell
+    dotnet new console
     ```
 
-## Authenticate and connect to Azure OpenAI
+3. Install the [OpenAI .NET client library](https://www.nuget.org/packages/Azure.AI.OpenAI/) with the [dotnet add package](/dotnet/core/tools/dotnet-add-package) command:
 
-To make requests to your Azure OpenAI service, you need the service endpoint as well as authentication credentials via one of the following options:
+    ```console
+    dotnet add package Azure.AI.OpenAI
+    ```
 
-- [Microsoft Entra ID](/entra/fundamentals/whatis) is the recommended approach for authenticating to Azure services and is more secure than key-based alternatives. 
-- Access keys allow you to provide a secret key to connect to your resource.
+1. For the **recommended** keyless authentication with Microsoft Entra ID, install the [Azure.Identity](https://www.nuget.org/packages/Azure.Identity) package with:
 
-[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+    ```console
+    dotnet add package Azure.Identity
+    ```
 
-### Get the Azure OpenAI endpoint
+1. For the **recommended** keyless authentication with Microsoft Entra ID, sign in to Azure with the following command:
 
-The service endpoint can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the endpoint via the **Deployments** page in Azure AI Foundry portal. An example endpoint is: `https://docs-test-001.openai.azure.com/`.
+    ```console
+    az login
+    ```
 
-:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location highlighted." lightbox="../media/quickstarts/endpoint.png":::
+## Retrieve resource information
 
-### Authenticate using Microsoft Entra ID
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
-If you choose to use Microsoft Entra ID authentication, you'll need to complete the following:
+## Run the quickstart
 
-1. Add the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package.
+The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with an `AzureKeyCredential` object. 
 
-    ```dotnetcli
-    dotnet add package Azure.Identity
-    ```
+#### [Microsoft Entra ID](#tab/keyless)
 
-1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal on your OpenAI resource under **Access control (IAM)** > **Add role assignment**.
-1. Sign-in to Azure using Visual Studio or the Azure CLI via `az login`.
+```csharp
+AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new DefaultAzureCredential()); 
+```
 
-### Authenticate using keys
+#### [API key](#tab/api-key)
 
-The access key value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+```csharp
+AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new AzureKeyCredential(key));
+```
+---
 
-## Update the app code
+> [!NOTE]
+> You can get sample audio files, such as *wikipediaOcelot.wav*, from the [Azure AI Speech SDK repository at GitHub](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/sampledata/audiofiles).
 
-1. Replace the contents of `program.cs` with the following code and update the placeholder values with your own.
+To run the quickstart, follow these steps:
 
+1. Replace the contents of `Program.cs` with the following code and update the placeholder values with your own.
+    
     ```csharp
     using Azure;
     using Azure.AI.OpenAI;
@@ -89,7 +98,7 @@ The access key value can be found in the **Keys & Endpoint** section when examin
     var speechFilePath = "YOUR_AUDIO_FILE_PATH";
     
     AzureOpenAIClient openAIClient = new AzureOpenAIClient(endpoint, credentials);
-    var audioClient = openAIClient.GetAudioClient(deploymentName);
+    AudioClient = openAIClient.GetAudioClient(deploymentName);
     
     var result = await audioClient.GenerateSpeechAsync(
                     "the quick brown chicken jumped over the lazy dogs");
@@ -105,4 +114,6 @@ The access key value can be found in the **Keys & Endpoint** section when examin
     dotnet run
     ```
 
-    The app generates an audio file at the location you specified for the `speechFilePath` variable. Play the file on your device to hear the generated audio.
+## Output
+
+The application will generate an audio file at the location you specified for the `speechFilePath` variable. Play the file on your device to hear the generated audio.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト読み上げの設定方法に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるテキスト読み上げ機能を使用するための.NET SDKに関するガイドを改善するための minor update です。主な修正点は以下の通りです。

1. **日付と著者情報の更新**: `ms.date`が2024年9月23日から2025年3月11日に変更され、レビューアおよび著者の情報も新たに設定されています。

2. **手順の整理と明確化**: Microsoft Entra IDを使用したキーレス認証に関する必要な準備が明確に整理され、役割の割り当て方法とAzure CLIのインストールに関する指示が追加されています。

3. **アプリケーションのセットアップ手順の詳細化**: 新しいフォルダーを作成し、そのフォルダーでVisual Studio Codeを開く方法が説明され、ユーザーが簡単にアプリケーションを始められるようになっています。

4. **コードやコマンドの修正**: サンプルコードが更新され、新しいコンソールアプリケーションの生成方法や必要なライブラリのインストール方法が含まれるようになっています。

5. **出力情報の明確化**: アプリケーションが指定したファイルパスにオーディオファイルを生成することが記され、ユーザーは生成されたオーディオをデバイスで再生することができることが示されています。 

全体として、これらの変更は、ユーザーがAzure OpenAIを使用してテキストを効果的に音声に変換するための手助けをし、手順の平易性と明確さを向上させています。

## articles/ai-services/openai/includes/use-your-data-dotnet.md{#item-b811b8}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: travisw
 ms.author: travisw
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 01/09/2025
+ms.date: 3/11/2025
 ---
 
 [!INCLUDE [Set up required variables](./use-your-data-common-variables.md)]
@@ -66,7 +66,7 @@ foreach (ChatCitation citation in onYourDataContext?.Citations ?? [])
 > For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see the Azure AI services [security](../../security-features.md) article.
 
 ```cmd
-dotnet run program.cs
+dotnet run Program.cs
 ```
 
 ## Output
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ使用に関する.NETドキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるユーザーのデータを利用するための.NET SDKのドキュメントを更新するための minor update です。主な修正点は以下の通りです。

1. **日付の更新**: 文書の日付が2025年1月9日から2025年3月11日に変更され、最新性を反映しています。

2. **コマンドの修正**: コードスニペット内の`program.cs`が`Program.cs`に修正され、一貫性と正確性が向上しています。この小さな変更は、ユーザーが正しいファイル名を使用することでエラーを防ぐのに役立ちます。

3. **セキュリティに関する注意喚起**: Azure Key Vaultを使用した安全な資格情報の管理方法が強調されており、ユーザーがセキュリティ対策に注意を払うよう促されています。

これらの改訂により、ドキュメントの精度と信頼性が向上し、ユーザーがAzure OpenAIの機能を利用する際に安心感を持てるようになっています。

## articles/ai-services/openai/includes/whisper-dotnet.md{#item-562a58}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +1,10 @@
 ---
 services: ai-services
-author: mrbullwinkle
-ms.author: mbullwin
-ms.service: openai
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 3/19/2024
+ms.date: 3/11/2025
 ---
 
 ## Prerequisites
@@ -13,73 +13,88 @@ ms.date: 3/19/2024
 - An Azure OpenAI resource with a Whisper model deployed in a [supported region](../concepts/models.md#whisper-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 - [The .NET 8.0 SDK](https://dotnet.microsoft.com/en-us/download)
 
-## Set up
+### Microsoft Entra ID prerequisites
 
-### Retrieve key and endpoint
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-To successfully make a call against Azure OpenAI, you need an *endpoint* and a *key*.
+## Set up
 
-|Variable name | Value |
-|--------------------------|-------------|
-| `AZURE_OPENAI_ENDPOINT`               | The service endpoint can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the endpoint via the **Deployments** page in Azure AI Foundry portal. An example endpoint is: `https://docs-test-001.openai.azure.com/`.|
-| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+1. Create a new folder `whisper-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you'll need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+    ```shell
+    mkdir whisper-quickstart && cd whisper-quickstart
+    ```
 
-:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location circled in red." lightbox="../media/quickstarts/endpoint.png":::
+1. Create a new console application with the following command:
 
-## Create the .NET app
+    ```shell
+    dotnet new console
+    ```
 
-1. Create a .NET app using the `dotnet new` command:
+3. Install the [OpenAI .NET client library](https://www.nuget.org/packages/Azure.AI.OpenAI/) with the [dotnet add package](/dotnet/core/tools/dotnet-add-package) command:
 
-    ```dotnetcli
-    dotnet new console -n OpenAIWhisper
+    ```console
+    dotnet add package Azure.AI.OpenAI
     ```
 
-1. Change into the directory of the new app:
+1. For the **recommended** keyless authentication with Microsoft Entra ID, install the [Azure.Identity](https://www.nuget.org/packages/Azure.Identity) package with:
 
-    ```dotnetcli
-    cd OpenAIWhisper
+    ```console
+    dotnet add package Azure.Identity
     ```
 
-1. Install the [`Azure.OpenAI`](https://www.nuget.org/packages/Azure.AI.OpenAI/) client library:
+1. For the **recommended** keyless authentication with Microsoft Entra ID, sign in to Azure with the following command:
 
-    ```dotnetcli
-    dotnet add package Azure.AI.OpenAI
+    ```console
+    az login
     ```
 
-## Passwordless authentication is recommended
+## Retrieve resource information
 
-Passwordless authentication is more secure than key-based alternatives and is the recommended approach for connecting to Azure services. If you choose to use Passwordless authentication, you'll need to complete the following:
+[!INCLUDE [resource authentication](resource-authentication.md)]
 
-1. Add the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package.
+## Run the quickstart
 
-    ```dotnetcli
-    dotnet add package Azure.Identity
-    ```
+The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with an `AzureKeyCredential` object. 
+
+#### [Microsoft Entra ID](#tab/keyless)
+
+```csharp
+AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new DefaultAzureCredential()); 
+```
 
-1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal on your OpenAI resource under **Access control (IAM)** > **Add role assignment**.
-1. Sign-in to Azure using Visual Studio or the Azure CLI via `az login`.
+#### [API key](#tab/api-key)
 
-## Update the app code
+```csharp
+AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new AzureKeyCredential(key));
+```
+---
+
+> [!NOTE]
+> You can get sample audio files, such as *wikipediaOcelot.wav*, from the [Azure AI Speech SDK repository at GitHub](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/sampledata/audiofiles).
 
-1. Replace the contents of `program.cs` with the following code and update the placeholder values with your own.
+To run the quickstart, follow these steps:
 
-    > [!NOTE]
-    > You can get sample audio files, such as *wikipediaOcelot.wav*, from the [Azure AI Speech SDK repository at GitHub](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/sampledata/audiofiles).
+1. Replace the contents of `Program.cs` with the following code and update the placeholder values with your own.
     
     ```csharp
     using Azure;
     using Azure.AI.OpenAI;
     using Azure.Identity; // Required for Passwordless auth
     
-    var endpoint = new Uri("YOUR_OPENAI_ENDPOINT");
-    var credentials = new AzureKeyCredential("YOUR_OPENAI_KEY");
-    // var credentials = new DefaultAzureCredential(); // Use this line for Passwordless auth
-    var deploymentName = "whisper"; // Default deployment name, update with your own if necessary
-    var audioFilePath = "YOUR_AUDIO_FILE_PATH";
     
-    AzureOpenAIClient openAIClient = new AzureOpenAIClient(endpoint, credentials);
+    string deploymentName = "whisper";
+    
+    string endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT") ?? "https://<your-resource-name>.openai.azure.com/";
+    string key = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY") ?? "<your-key>";
+    
+    // Use the recommended keyless credential instead of the AzureKeyCredential credential.
+    AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new DefaultAzureCredential()); 
+    //AzureOpenAIClient openAIClient = new AzureOpenAIClient(new Uri(endpoint), new AzureKeyCredential(key));
+    
+    var audioFilePath = "<audio file path>"
     
     var audioClient = openAIClient.GetAudioClient(deploymentName);
     
@@ -92,19 +107,18 @@ Passwordless authentication is more secure than key-based alternatives and is th
     }
     ```
 
-[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
-
 1. Run the application using the `dotnet run` command or the run button at the top of Visual Studio:
 
     ```dotnetcli
     dotnet run
     ```
 
-    If you are using the sample audio file, you should see the following text printed out in the console:
+## Output
 
-    ```text
-    The ocelot, Lepardus paradalis, is a small wild cat native to the southwestern United States, 
-    Mexico, and Central and South America. This medium-sized cat is characterized by solid 
-    black spots and streaks on its coat, round ears...
-    ```
-    
\ No newline at end of file
+If you are using the sample audio file, you should see the following text printed out in the console:
+
+```text
+The ocelot, Lepardus paradalis, is a small wild cat native to the southwestern United States, 
+Mexico, and Central and South America. This medium-sized cat is characterized by solid 
+black spots and streaks on its coat, round ears...
+```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisperモデルに関する.NETドキュメントの改訂"
}
```

### Explanation
この変更は、Azure OpenAIサービスのWhisperモデルを使用するための.NET SDKのドキュメントを更新するための minor update です。主な修正点は以下の通りです。

1. **著者と日付の更新**: 著者情報が`eric-urban`に変更され、文書の日付が2024年3月19日から2025年3月11日に更新されました。これにより、文書が最新の情報を反映しています。

2. **手順の整理と明確化**: Microsoft Entra IDを利用したキーレス認証の準備手順が追加され、Azure CLIのインストールやユーザーアカウントへの役割の割り当てについて詳細に説明されています。

3. **コンソールアプリケーションの作成手順の詳細化**: 新しいフォルダーの作成や、Visual Studio Codeをそのフォルダーで開くための具体的なコマンドが追加され、ユーザーがアプリの開始の手順をより簡単に理解できるようになっています。

4. **サンプルコードの改善**: サンプルコードが更新され、環境変数を使用する方法が示されており、パスワードレス認証の推奨が強調されています。

5. **出力の明確化**: アプリケーションを実行した際に予想されるコンソール出力の例が提供され、ユーザーが期待できる結果を把握しやすくしています。

これらの変更は、ユーザーがWhisperモデルを効果的に利用できるようにするための情報を整理し、更新したものです。全体的に見て、ドキュメントはより明確かつ使いやすくなっています。

## articles/ai-services/openai/includes/whisper-python.md{#item-e61179}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,7 @@
 services: ai-services
 author: mrbullwinkle
 ms.author: mbullwin
-ms.service: openai
+ms.service: azure-ai-openai
 ms.topic: include
 ms.date: 3/19/2024
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisperモデルに関するPythonドキュメントのサービス名更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスのWhisperモデルを扱うPythonのドキュメントに関する minor update です。主な修正点は以下の通りです。

1. **サービス名の更新**: 文書内のサービス名が`openai`から`azure-ai-openai`に変更されました。この修正により、サービスのブランド名が統一され、整合性が保たれています。

2. **著者情報の維持と日付の更新**: 著者情報は変更されていませんが、日付が2024年3月19日として指定されており、最新の情報を反映しています。文書の正確性を確保するための重要な更新です。

この変更は、ユーザーがAzure OpenAIサービスに関連する情報を明確に理解できるようにするためのドキュメントの一貫性を保つものです。全体的に、この小さな修正はユーザーの混乱を避け、サービスの利用をスムーズにするための重要な改善です。

## articles/ai-services/openai/realtime-audio-reference.md{#item-276d51}

<details>
<summary>Diff</summary>
````diff
@@ -1293,7 +1293,7 @@ You use the `RealtimeRequestSession` object when you want to update the session
 | + total_tokens | integer | The total number of tokens in the Response including input and output text and audio tokens.<br><br>A property of the `usage` object. | 
 | + input_tokens | integer | The number of input tokens used in the response, including text and audio tokens.<br><br>A property of the `usage` object. |
 | + output_tokens | integer | The number of output tokens sent in the response, including text and audio tokens.<br><br>A property of the `usage` object. | 
-| + input_token_details | object | Details about the input tokens used in the response.<br><br>A property of the `usage` object.<br>br><br>See nested properties next.|
+| + input_token_details | object | Details about the input tokens used in the response.<br><br>A property of the `usage` object.<br><br>See nested properties next.|
 | + cached_tokens | integer | The number of cached tokens used in the response.<br><br>A property of the `input_token_details` object. | 
 | + text_tokens | integer | The number of text tokens used in the response.<br><br>A property of the `input_token_details` object. | 
 | + audio_tokens | integer | The number of audio tokens used in the response.<br><br>A property of the `input_token_details` object. | 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイム音声参照ドキュメントの入力トークンの詳細の修正"
}
```

### Explanation
この変更は、Azure OpenAIサービスのリアルタイム音声に関する参照ドキュメントに対する minor update です。主な修正点は以下の通りです。

1. **HTMLの修正**: 入力トークンの詳細に関する記述のHTML部分で、`<br>`タグが間違って表記されていたため修正されました。具体的には、`<br><br>`が`<br><br>`に修正され、表示の整合性が向上しました。この修正により、文書の可読性が改善され、ユーザーが情報をより簡単に理解できるようになります。

2. **文書の一貫性の向上**: この変更を通じて、入力トークンの詳細の説明が整備され、他のトークンに関する情報とも一貫した表現が維持されるようになりました。

このように、この微修正は文書の整合性とユーザビリティを向上させるための重要なステップです。全体として、文書はより使いやすく、正確な情報を提供するものになっています。


