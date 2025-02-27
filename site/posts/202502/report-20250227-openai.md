---
date: '2025-02-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bc33227...MicrosoftDocs:42a07e4
summary: |-
  この報告の要約は次のとおりです。

  Azure OpenAI Serviceのドキュメントに対して複数の更新が行われました。これには、新しいモデルの引退予定日、CLIに関する更新、タイプミスの修正、およびC#アシスタントのサンプルコードの改善が含まれています。具体的には、Azure Developer CLIに`gpt-4o-mini`モデルをデプロイするためのサンプルテンプレートが追加され、C#サンプルコードにおいて新しいライブラリの使用やAPIキーの取得方法についての説明が追加されました。特に破壊的な変更はないものの、モデルの引退日情報が強調されており、これによりユーザーはサービスの活用計画を立てやすくなります。また、文書の信頼性向上やセキュリティの強化にも寄与しています。全体として、これらの更新はユーザーエクスペリエンスを向上させ、技術エコシステムを強化しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bc33227...MicrosoftDocs:42a07e4){target="_blank"}

<format>
# ハイライト
この差分は、Azure OpenAI Serviceのドキュメントにおける複数の更新を含んでおり、新しいモデルの引退予定日やCLIの更新内容の追加、タイプミスの修正、そしてC#アシスタントのサンプルコードの改善が行われています。

## 新機能
- Azure Developer CLIにおいて、`gpt-4o-mini`モデルをデプロイするサンプルテンプレートが追加。
- C#サンプルコードに新しいライブラリの使用とKey VaultからのAPIキー取得方法の説明が追加。

## 破壊的変更
- 特に破壊的変更は含まれていませんが、引退予定のモデルに関する今後の使用に際する重要な日程情報が追加されました。

## その他の更新
- `stored-completions.md`ファイルのタイプミス修正。
- `gpt-4o-realtime-preview`モデルの引退予定日が2025年2月25日（非推奨）と2025年3月26日（引退）として記載。
- Azure Developer CLIの文書更新で日付変更およびGitHubリンクの追加。

# 洞察
このアップデートは、Azure OpenAI Serviceの利用者に対して、最新の情報とよりセキュアな開発環境を提供するためのものであり、特に以下の点で重要です。

モデルの引退日程が明確化されたことで、ユーザーは将来的な計画を立てる際の重要な判断材料を得ることができ、サービスの使用を継続的に最適化する手助けをします。CLIに関連する更新は、変化する技術スタックへの素早い適応を可能にし、ユーザーに最新のサンプルテンプレートを提供します。特に、`infra/main.bicep`ファイルの変数を編集することで異なるモデルをデプロイする柔軟性が強調されています。

`stored-completions.md`のタイプミス修正により、技術文書の信頼性が向上し、開発者が誤った情報によって混乱する可能性を減少させます。

C#アシスタントの更新では、ライブラリの選択やセキュリティ考慮を提供し、実装の正確性と安全性を実現します。このような改善は、単なるコードの更新にとどまらず、開発者が安心して使用できるフレームワークの強化に寄与します。特にKey Vaultの使用により、機密情報の適切な管理が促進され、クラウド開発におけるベストプラクティスの普及を促進します。

全体として、これらの更新はいずれもユーザーエクスペリエンスの向上と、Azure OpenAI Serviceを取り巻く技術エコシステムの強化に貢献しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルの引退についての更新 | modified | 2 | 1 | 3 | 
| [azure-developer-cli.md](#item-3d4cfb) | minor update | Azure Developer CLIに関する更新 | modified | 4 | 3 | 7 | 
| [stored-completions.md](#item-ccc7e6) | bug fix | タイプミスの修正 | modified | 1 | 1 | 2 | 
| [assistants-csharp.md](#item-cc4697) | minor update | C#アシスタントのサンプルコードの更新 | modified | 41 | 12 | 53 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -107,7 +107,7 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-4o` | 2024-08-06 | No earlier than August 6, 2025  | |
 | `gpt-4o` | 2024-11-20 | No earlier than November 20, 2025  | |
 | `gpt-4o-mini` | 2024-07-18 | No earlier than July 18, 2025  | |
-| `gpt-4o-realtime-preview` | 2024-10-01 | No earlier than September 30, 2025  | `gpt-4o-realtime-preview` (version 2024-12-17) or `gpt-4o-mini-realtime-preview` (version 2024-12-17) |
+| `gpt-4o-realtime-preview` | 2024-10-01 | **Deprecated:** February 25, 2025<br>**Retirement:** No earlier than March 26, 2025 | `gpt-4o-realtime-preview` (version 2024-12-17) or `gpt-4o-mini-realtime-preview` (version 2024-12-17) |
 | `gpt-3.5-turbo-instruct` | 0914 | No earlier than May 31, 2025 |  |
 | `o1-preview` | 2024-09-12 | No earlier than April 2, 2025 | `o1` |
 | `o1` | 2024-12-17 | No earlier than December 17, 2025 | |
@@ -174,6 +174,7 @@ If you're an existing customer looking for information about these models, see [
 ## February 25, 2025
 
 -  `dalle-3` updated to no earlier than June 30, 2025.
+- `gpt-4o-realtime-preview` (2024-10-01) No earlier than March 26, 2025.
 
 ## February 20, 2025
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの引退についての更新"
}
```

### Explanation
このコードの変更は、Azure OpenAI Serviceにおけるモデルの引退情報を更新することを目的としています。具体的には、`gpt-4o-realtime-preview`モデルに関する引退予定日が明確に記載され、2025年2月25日に非推奨、2025年3月26日に引退することが追加されました。この修正により、利用者はこのモデルを使用する際の重要な日程についての最新情報を得ることができます。また、変更は2行追加され、1行が削除されています。この更新は、ユーザーが模型の可用性とその将来の計画を理解する手助けになります。

## articles/ai-services/openai/how-to/azure-developer-cli.md{#item-3d4cfb}

<details>
<summary>Diff</summary>
````diff
@@ -7,13 +7,13 @@ ms.service: azure-ai-openai
 ms.topic: quickstart
 author: aahill
 ms.author: aahi
-ms.date: 04/09/2024
+ms.date: 02/25/2025
 recommendations: false
 ---
 
 # Use the Azure Developer CLI to deploy resources for Azure OpenAI On Your Data 
 
-Use this article to learn how to automate resource deployment for Azure OpenAI Service On Your Data. The Azure Developer CLI (`azd`) is an open-source command-line tool that streamlines provisioning and deploying resources to Azure by using a template system. The template contains infrastructure files to provision the necessary Azure OpenAI resources and configurations. It also includes the completed sample app code.
+Use this article to learn how to automate resource deployment for Azure OpenAI Service On Your Data. The Azure Developer CLI (`azd`) is an open-source command-line tool that streamlines provisioning and deploying resources to Azure by using a template system. The template contains infrastructure files to provision the necessary Azure OpenAI resources and configurations. The source code for the template can be found on [GitHub](https://github.com/Azure-Samples/openai-chat-your-own-data/tree/main).
 
 ## Prerequisites
 
@@ -55,7 +55,8 @@ Use this article to learn how to automate resource deployment for Azure OpenAI S
     - `Location`: The Azure region where your resources are deployed.
 
     > [!NOTE]
-    > The sample `azd` template uses the `gpt-35-turbo-16k` model. A recommended region for this template is East US, because different Azure regions support different OpenAI models. For more details about model support by region, go to the [Azure OpenAI Service Models](/azure/ai-services/openai/concepts/models) support page.
+    > * The sample `azd` template deploys a `gpt-4o-mini` model. A recommended region for this template is East US, because different Azure regions support different OpenAI models. For more details about model support by region, go to the [Azure OpenAI Service Models](/azure/ai-services/openai/concepts/models) support page.
+    > * If you want to deploy a different model, you can edit the variables in the `infra/main.bicep` file.
 
     The provisioning process might take several minutes. Wait for the task to finish before you proceed to the next steps.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Developer CLIに関する更新"
}
```

### Explanation
このコードの変更は、Azure Developer CLIに関する文書の内容を更新することを目的としています。具体的には、日付が2024年4月9日から2025年2月25日に変更され、使用するサンプルテンプレートに関連する情報が追加されました。新しい情報では、サンプルテンプレートが`gpt-4o-mini`モデルをデプロイすることが明記され、異なるモデルをデプロイするためには`infra/main.bicep`ファイルの変数を編集する必要があることが説明されています。また、GitHubへのリンクも追加され、テンプレートのソースコードが確認できるようになっています。この修正により、ユーザーは最新のモデルやリソースデプロイのための手順に関する重要な情報を得ることができます。

## articles/ai-services/openai/how-to/stored-completions.md{#item-ccc7e6}

<details>
<summary>Diff</summary>
````diff
@@ -88,7 +88,7 @@ client = AzureOpenAI(
     azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
     )
 
-ompletion = client.chat.completions.create(
+completion = client.chat.completions.create(
     
     model="gpt-4o", # replace with model deployment name
     store= True,
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "タイプミスの修正"
}
```

### Explanation
このコードの変更は、`stored-completions.md`ファイル内でのタイプミスを修正することを目的としています。特に、`ompletion`という誤った変数名が`completion`に修正されました。この修正により、コードの正確性が向上し、ユーザーが正しく機能するスクリプトを参照できるようになります。変更は、1行の追加と1行の削除からなりますが、全体としてはコードの可読性と動作に重要な影響を与えます。

## articles/ai-services/openai/includes/assistants-csharp.md{#item-cc4697}

<details>
<summary>Diff</summary>
````diff
@@ -71,24 +71,35 @@ Passwordless authentication is more secure than key-based alternatives and is th
 
 ### Create the assistant
 
+>[!Note]
+> For this sample, the following libraries were used:
+>- Azure.AI.OpenAI(2.1.0-beta2)
+>- Azure.AI.OpenAI.Assistants(1.0.0-beta4)
+
 Update the `Program.cs` file with the following code to create an assistant:
 
 ```csharp
 using Azure;
-using Azure.AI.OpenAI.Assistants;
+using Azure.AI.OpenAI;
+using Azure.Identity;
+using Azure.Security.KeyVault.Secrets;
+using OpenAI.Assistants;
+using OpenAI.Files;
+using System.ClientModel;
 
 // Assistants is a beta API and subject to change
 // Acknowledge its experimental status by suppressing the matching warning.
 string endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
 string key = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
+string deploymentName = "<Replace with Deployment Name>"
 
 var openAIClient = new AzureOpenAIClient(new Uri(endpoint), new AzureKeyCredential(key));
 
 // Use for passwordless auth
 //var openAIClient = new AzureOpenAIClient(new Uri(endpoint), new DefaultAzureCredential()); 
 
-FileClient fileClient = openAIClient.GetFileClient();
-AssistantClient assistantClient = openAIClient.GetAssistantClient();
+OpenAIFileClient fileClient = azureClient.GetOpenAIFileClient();
+AssistantClient assistantClient = azureClient.GetAssistantClient();
 
 // First, let's contrive a document we'll use retrieval with and upload it.
 using Stream document = BinaryData.FromString("""
@@ -120,13 +131,13 @@ using Stream document = BinaryData.FromString("""
             }
             """).ToStream();
 
-OpenAIFileInfo salesFile = await fileClient.UploadFileAsync(
+OpenAI.Files.OpenAIFile salesFile = await fileClient.UploadFileAsync(
     document,
     "monthly_sales.json",
     FileUploadPurpose.Assistants);
 
 // Now, we'll create a client intended to help with that data
-AssistantCreationOptions assistantOptions = new()
+OpenAI.Assistants.AssistantCreationOptions assistantOptions = new()
 {
     Name = "Example: Contoso sales RAG",
     Instructions =
@@ -136,7 +147,7 @@ AssistantCreationOptions assistantOptions = new()
     Tools =
             {
                 new FileSearchToolDefinition(),
-                new CodeInterpreterToolDefinition(),
+                new OpenAI.Assistants.CodeInterpreterToolDefinition(),
             },
     ToolResources = new()
     {
@@ -158,7 +169,9 @@ ThreadCreationOptions threadOptions = new()
     InitialMessages = { "How well did product 113045 sell in February? Graph its trend over time." }
 };
 
-ThreadRun threadRun = await assistantClient.CreateThreadAndRunAsync(assistant.Id, threadOptions);
+var initialMessage = new OpenAI.Assistants.ThreadInitializationMessage(OpenAI.Assistants.MessageRole.User, ["hi"]);
+
+ThreadRun threadRun = await assistantClient.CreateThreadAndRunAsync(assistant.Value.Id, threadOptions);
 
 // Check back to see when the run is done
 do
@@ -168,15 +181,15 @@ do
 } while (!threadRun.Status.IsTerminal);
 
 // Finally, we'll print out the full history for the thread that includes the augmented generation
-AsyncCollectionResult<ThreadMessage> messages
+AsyncCollectionResult<OpenAI.Assistants.ThreadMessage> messages
     = assistantClient.GetMessagesAsync(
         threadRun.ThreadId,
         new MessageCollectionOptions() { Order = MessageCollectionOrder.Ascending });
 
-await foreach (ThreadMessage message in messages)
+await foreach (OpenAI.Assistants.ThreadMessage message in messages)
 {
     Console.Write($"[{message.Role.ToString().ToUpper()}]: ");
-    foreach (MessageContent contentItem in message.Content)
+    foreach (OpenAI.Assistants.MessageContent contentItem in message.Content)
     {
         if (!string.IsNullOrEmpty(contentItem.Text))
         {
@@ -202,9 +215,9 @@ await foreach (ThreadMessage message in messages)
         }
         if (!string.IsNullOrEmpty(contentItem.ImageFileId))
         {
-            OpenAIFileInfo imageInfo = await fileClient.GetFileAsync(contentItem.ImageFileId);
+            OpenAI.Files.OpenAIFile imageFile = await fileClient.GetFileAsync(contentItem.ImageFileId);
             BinaryData imageBytes = await fileClient.DownloadFileAsync(contentItem.ImageFileId);
-            using FileStream stream = File.OpenWrite($"{imageInfo.Filename}.png");
+            using FileStream stream = File.OpenWrite($"{imageFile.Filename}.png");
             imageBytes.ToStream().CopyTo(stream);
 
             Console.WriteLine($"<image: {imageInfo.Filename}.png>");
@@ -214,6 +227,22 @@ await foreach (ThreadMessage message in messages)
 }
 ```
 
+It is recommended that you store the API Key in a secure location, such as a Key Vault. The following code snippet can replace the 
+```GetEnvironmentVariable``` lines to retrieve the Azure OpenAI API Key from your Key Vault instance:
+
+```csharp
+string keyVaultName = "<Replace with Key Vault Name>";
+var kvUri = $"https://{keyVaultName}.vault.azure.net/";
+
+var client = new SecretClient(new Uri(kvUri), new DefaultAzureCredential());
+
+KeyVaultSecret endpointSecret = await client.GetSecretAsync("AZURE-OPENAI-ENDPOINT");
+KeyVaultSecret apiKeySecret = await client.GetSecretAsync("AZURE-OPENAI-API-KEY");
+
+string endpoint = endpointSecret.Value;
+string key = apiKeySecret.Value;
+```
+
 Run the app using the [`dotnet run`](/dotnet/core/tools/dotnet-run) command:
 
 ```csharp
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#アシスタントのサンプルコードの更新"
}
```

### Explanation
このコードの変更は、C#アシスタントに関するサンプルコードを更新することを目的としています。変更には新しいライブラリの追加、コードのリファクタリング、およびコメントの追加が含まれています。主な加筆部分では、使用するライブラリと対象のアシスタントを明確にするための情報が含まれています。また、APIキーを安全に保管する方法についても新たに説明が加わり、Key VaultからAPIキーを取得するためのコードスニペットが提供されています。これにより、ユーザーはより安全にAzure OpenAIの設定を行うことができるようになります。全体として、コードの可読性と安全性が向上するための重要な変更が含まれています。


