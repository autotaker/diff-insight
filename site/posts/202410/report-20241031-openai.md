---
date: '2024-10-31'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a68723c...MicrosoftDocs:b16ebe2
summary: このコード変更は、Azure OpenAIサービスを利用したテキスト読み上げと音声認識機能の実装を容易にするために、JavaScriptおよびTypeScript向けのドキュメントを改善し、新たに追加したものです。主な改善点には、認証方法の見直し（APIキーからAzure
  Active Directoryへの変更）や新しい言語サポート（TypeScript用のテキスト読み上げおよびWhisper APIのドキュメントの追加）が含まれています。また、クイックスタートドキュメントにもTypeScriptセクションが追加され、認証方法の理解が深まるように改善されています。これにより、開発者はよりセキュアで効率的にAzureのサービスを利用できるようになります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a68723c...MicrosoftDocs:b16ebe2){target="_blank"}

# Highlights
このコード変更は、Azure OpenAIサービスを用いたテキスト読み上げおよび音声認識機能の実装をより簡単にするためのJavaScriptおよびTypeScript向けドキュメントの改善と追加を行ったものです。主要な改善点としては、認証方法の見直しや新しい言語サポートの追加が含まれています。

## New features
- TypeScript用のテキスト読み上げドキュメントの新規追加。
- Whisper API用のTypeScriptドキュメントの新規追加。

## Breaking changes
- Azure OpenAI APIの認証方法がAPIキーからAzure Active Directory利用へと変わりました。

## Other updates
- Whisper APIおよびテキスト読み上げ機能のクイックスタートにTypeScriptセクションが追加されました。
- JavaScriptドキュメントにおける認証方法の改善。

# Insights
このドキュメント更新では、Azure OpenAIサービスを活用する開発者にとって非常に重要な認証方法の見直しが行われています。従来のAPIキーによる認証方法はセキュリティ面での懸念を払拭するため、Azure Active Directoryを利用したパスワードレス認証に変更されました。これにより、開発者はよりセキュアな環境でサービスを利用することができます。また、`DefaultAzureCredential`を用いることで、開発プロセスにおける認証管理が簡素化されました。

さらに、TypeScriptを用いる開発者の要望に応えるため、新たにテキスト読み上げとWhisper APIのサポートが追加されました。これにより、JavaScriptと同様の機能をTypeScriptプロジェクトに迅速に組み込むことが可能です。クイックスタートドキュメントにもそれぞれ対応するセクションが追加されており、導入が容易になっています。

今回の変更によって、JavaScriptおよびTypeScriptのそれぞれで音声合成・音声認識を行う際の設定手順が整理され、開発者はAzureのサービスを活用してより豊かな機能を提供することが期待されます。これらの改善は、Time-to-Marketの短縮やセキュリティの向上に寄与するものといえます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [text-to-speech-javascript.md](#item-e9b653) | minor update | テキスト読み上げのJavaScriptコードの改善 | modified | 24 | 44 | 68 | 
| [text-to-speech-typescript.md](#item-1335d5) | new feature | TypeScriptによるテキスト読み上げのドキュメント追加 | added | 247 | 0 | 247 | 
| [whisper-javascript.md](#item-3ee990) | minor update | Whisper APIのJavaScript仕様書のアップデート | modified | 16 | 24 | 40 | 
| [whisper-typescript.md](#item-eafedb) | new feature | TypeScriptによるWhisper APIのドキュメント追加 | added | 228 | 0 | 228 | 
| [text-to-speech-quickstart.md](#item-c344ad) | minor update | テキスト読み上げのクイックスタートドキュメントのTypeScriptセクションの追加 | modified | 6 | 0 | 6 | 
| [whisper-quickstart.md](#item-4cae3d) | minor update | WhisperクイックスタートドキュメントのTypeScriptセクションの追加 | modified | 6 | 0 | 6 | 


# Modified Contents
## articles/ai-services/openai/includes/text-to-speech-javascript.md{#item-e9b653}

<details>
<summary>Diff</summary>
````diff
@@ -14,24 +14,12 @@ recommendations: false
 
 ## Prerequisites
 
-#### [JavaScript](#tab/javascript)
-
-- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
-- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
-- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
-
-
-#### [TypeScript](#tab/typescript)
-
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
-- [TypeScript](https://www.typescriptlang.org/download/)
+- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 
-
----
-
 ## Set up
 
 ### Retrieve key and endpoint
@@ -104,32 +92,35 @@ Your app's _package.json_ file will be updated with the dependencies.
 
 ## Create a speech file
 
+    
 
-
-#### [JavaScript](#tab/javascript)
+#### [Microsoft Entra ID](#tab/javascript-keyless)
 
 1. Create a new file named _Text-to-speech.js_ and open it in your preferred code editor. Copy the following code into the _Text-to-speech.js_ file:
 
     ```javascript
-    require("dotenv/config");
     const { writeFile } = require("fs/promises");
     const { AzureOpenAI } = require("openai");
+    const { DefaultAzureCredential, getBearerTokenProvider } = require("@azure/identity");
     require("openai/shims/node");
     
     // You will need to set these environment variables or edit the following values
     const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
-    const speechFilePath =
-      process.env["SPEECH_FILE_PATH"] || "<path to save the speech file>";
+    const speechFilePath = "<path to save the speech file>";
     
     // Required Azure OpenAI deployment name and API version
     const deploymentName = "tts";
     const apiVersion = "2024-08-01-preview";
     
+    // keyless authentication    
+    const credential = new DefaultAzureCredential();
+    const scope = "https://cognitiveservices.azure.com/.default";
+    const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+
     function getClient() {
       return new AzureOpenAI({
         endpoint,
-        apiKey,
+        azureADTokenProvider,
         apiVersion,
         deployment: deploymentName,
       });
@@ -169,30 +160,26 @@ Your app's _package.json_ file will be updated with the dependencies.
     ```console
     node Text-to-speech.js
     ```
-    
 
-#### [TypeScript](#tab/typescript)
+#### [API key](#tab/javascript-key)
 
-1. Create a new file named _Text-to-speech.ts_ and open it in your preferred code editor. Copy the following code into the _Text-to-speech.ts_ file:
+1. Create a new file named _Text-to-speech.js_ and open it in your preferred code editor. Copy the following code into the _Text-to-speech.js_ file:
 
-    ```typescript
-    import "dotenv/config";
-    import { writeFile } from "fs/promises";
-    import { AzureOpenAI } from "openai";
-    import type { SpeechCreateParams } from "openai/resources/audio/speech";
-    import "openai/shims/node";
+    ```javascript
+    const { writeFile } = require("fs/promises");
+    const { AzureOpenAI } = require("openai");
+    require("openai/shims/node");
     
     // You will need to set these environment variables or edit the following values
     const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
     const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
-    const speechFilePath =
-      process.env["SPEECH_FILE_PATH"] || "<path to save the speech file>";
+    const speechFilePath = "<path to save the speech file>";
     
     // Required Azure OpenAI deployment name and API version
     const deploymentName = "tts";
     const apiVersion = "2024-08-01-preview";
     
-    function getClient(): AzureOpenAI {
+    function getClient() {
       return new AzureOpenAI({
         endpoint,
         apiKey,
@@ -202,9 +189,9 @@ Your app's _package.json_ file will be updated with the dependencies.
     }
     
     async function generateAudioStream(
-      client: AzureOpenAI,
-      params: SpeechCreateParams
-    ): Promise<NodeJS.ReadableStream> {
+      client,
+      params
+    ) {
       const response = await client.audio.speech.create(params);
       if (response.ok) return response.body;
       throw new Error(`Failed to generate audio stream: ${response.statusText}`);
@@ -229,19 +216,12 @@ Your app's _package.json_ file will be updated with the dependencies.
     });
     
     ```
-    
-   The import of `"openai/shims/node"` is necessary when running the code in a Node.js environment. It ensures that the output type of the `client.audio.speech.create` method is correctly set to `NodeJS.ReadableStream`.
-
-1. Build the application with the following command:
-
-    ```console
-    tsc
-    ```
 
-1. Run the application with the following command:
+1. Run the script with the following command:
 
     ```console
     node Text-to-speech.js
     ```
+    
 
 ---
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト読み上げのJavaScriptコードの改善"
}
```

### Explanation
このコードの変更は、JavaScriptを用いたテキスト読み上げの機能に関連する文書を更新したものです。主な改善点としては、JavaScriptおよびTypeScriptの設定手順が簡素化され、特にAzure CLIを使ったパスワードレス認証の追加が目立ちます。また、Azure OpenAI APIの認証方法がAPIキーからAzure Active Directoryを利用した方法に変更されました。

具体的には、次の点が修正されました：
- 不要な環境変数の設定が削除され、代わりに`DefaultAzureCredential`が使用されるようになった。
- 複数の手順が整理され、Microsoft Entra IDによる認証手順が導入された。
- コード例が更新され、Node.js環境での適切な設定が強調されました。

この変更により、利用者はより安全で便利にテキスト読み上げ機能を実装できるようになりました。

## articles/ai-services/openai/includes/text-to-speech-typescript.md{#item-1335d5}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,247 @@
+---
+ms.topic: include
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 09/12/2024
+ms.reviewer: v-baolianzou
+ms.author: eur
+author: eric-urban
+recommendations: false
+---
+
+[Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
+
+## Prerequisites
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [TypeScript](https://www.typescriptlang.org/download/)
+- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
+- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+
+
+## Set up
+
+### Retrieve key and endpoint
+
+To successfully make a call against Azure OpenAI, you need an **endpoint** and a **key**.
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.|
+| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+
+Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+
+:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location highlighted." lightbox="../media/quickstarts/endpoint.png":::
+
+### Environment variables
+
+Create and assign persistent environment variables for your key and endpoint.
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+
+# [Command Line](#tab/command-line)
+
+```CMD
+setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
+```
+
+```CMD
+setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
+```
+
+# [PowerShell](#tab/powershell)
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_KEY_VALUE_HERE', 'User')
+```
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_ENDPOINT_HERE', 'User')
+```
+
+# [Bash](#tab/bash)
+
+```Bash
+echo export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE" >> /etc/environment && source /etc/environment
+```
+
+```Bash
+echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/environment && source /etc/environment
+```
+---
+
+## Create a Node application
+
+In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+
+```console
+npm init
+```
+
+## Install the client library
+
+Install the client libraries with:
+
+```console
+npm install openai @azure/identity
+```
+
+Your app's _package.json_ file will be updated with the dependencies.
+
+## Create a speech file
+
+    
+
+#### [Microsoft Entra ID](#tab/typescript-keyless)
+
+1. Create a new file named _Text-to-speech.ts_ and open it in your preferred code editor. Copy the following code into the _Text-to-speech.ts_ file:
+
+    ```typescript
+    import { writeFile } from "fs/promises";
+    import { AzureOpenAI } from "openai";
+    import { DefaultAzureCredential, getBearerTokenProvider } from "@azure/identity";
+    import type { SpeechCreateParams } from "openai/resources/audio/speech";
+    import "openai/shims/node";
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const speechFilePath = "<path to save the speech file>";
+    
+    // Required Azure OpenAI deployment name and API version
+    const deploymentName = "tts";
+    const apiVersion = "2024-08-01-preview";
+
+    // keyless authentication    
+    const credential = new DefaultAzureCredential();
+    const scope = "https://cognitiveservices.azure.com/.default";
+    const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        azureADTokenProvider,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    
+    async function generateAudioStream(
+      client: AzureOpenAI,
+      params: SpeechCreateParams
+    ): Promise<NodeJS.ReadableStream> {
+      const response = await client.audio.speech.create(params);
+      if (response.ok) return response.body;
+      throw new Error(`Failed to generate audio stream: ${response.statusText}`);
+    }
+    export async function main() {
+      console.log("== Text to Speech Sample ==");
+    
+      const client = getClient();
+      const streamToRead = await generateAudioStream(client, {
+        model: deploymentName,
+        voice: "alloy",
+        input: "the quick brown chicken jumped over the lazy dogs",
+      });
+    
+      console.log(`Streaming response to ${speechFilePath}`);
+      await writeFile(speechFilePath, streamToRead);
+      console.log("Finished streaming");
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
+    
+    ```
+    
+   The import of `"openai/shims/node"` is necessary when running the code in a Node.js environment. It ensures that the output type of the `client.audio.speech.create` method is correctly set to `NodeJS.ReadableStream`.
+
+1. Build the application with the following command:
+
+    ```console
+    tsc
+    ```
+
+1. Run the application with the following command:
+
+    ```console
+    node Text-to-speech.js
+    ```
+
+
+#### [API key](#tab/typescript-key)
+
+1. Create a new file named _Text-to-speech.ts_ and open it in your preferred code editor. Copy the following code into the _Text-to-speech.ts_ file:
+
+    ```typescript
+    import { writeFile } from "fs/promises";
+    import { AzureOpenAI } from "openai";
+    import type { SpeechCreateParams } from "openai/resources/audio/speech";
+    import "openai/shims/node";
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = "<endpoint>";
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+    const speechFilePath =
+      process.env["SPEECH_FILE_PATH"] || "<path to save the speech file>";
+    
+    // Required Azure OpenAI deployment name and API version
+    const deploymentName = "tts";
+    const apiVersion = "2024-08-01-preview";
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    
+    async function generateAudioStream(
+      client: AzureOpenAI,
+      params: SpeechCreateParams
+    ): Promise<NodeJS.ReadableStream> {
+      const response = await client.audio.speech.create(params);
+      if (response.ok) return response.body;
+      throw new Error(`Failed to generate audio stream: ${response.statusText}`);
+    }
+    export async function main() {
+      console.log("== Text to Speech Sample ==");
+    
+      const client = getClient();
+      const streamToRead = await generateAudioStream(client, {
+        model: deploymentName,
+        voice: "alloy",
+        input: "the quick brown chicken jumped over the lazy dogs",
+      });
+    
+      console.log(`Streaming response to ${speechFilePath}`);
+      await writeFile(speechFilePath, streamToRead);
+      console.log("Finished streaming");
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
+    
+    ```
+    
+   The import of `"openai/shims/node"` is necessary when running the code in a Node.js environment. It ensures that the output type of the `client.audio.speech.create` method is correctly set to `NodeJS.ReadableStream`.
+
+1. Build the application with the following command:
+
+    ```console
+    tsc
+    ```
+
+1. Run the application with the following command:
+
+    ```console
+    node Text-to-speech.js
+    ```
+
+---
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "TypeScriptによるテキスト読み上げのドキュメント追加"
}
```

### Explanation
この変更は、TypeScriptを用いたテキスト読み上げに関する新しいドキュメントを追加したものです。主な内容としては、Azure OpenAIサービスを利用したテキスト読み上げのための設定手順やサンプルコードが含まれています。

具体的には、以下の内容が含まれています：
- **前提条件**: AzureのサブスクリプションやNode.js、TypeScript、Azure CLIなど必要な環境を設定するための情報が提供されています。
- **セットアップ手順**: Azure OpenAIのエンドポイントとキーの取得方法が詳しく説明されており、環境変数の設定手順も記載されています。
- **Nodeアプリケーションの作成**: 新しいNodeアプリケーションを作成し、必要なクライアントライブラリ（OpenAIとAzure Identity）をインストールする方法が案内されています。
- **例コード**: TypeScriptでのテキスト読み上げ機能を実装するためのサンプルコードが２種類示されており、一つはMicrosoft Entra IDを用いた認証、もう一つはAPIキーによる認証が含まれています。両方のサンプルは、特定のテキストを音声ファイルに変換し、指定したパスに保存する方法を示しています。

この新しいドキュメントにより、開発者はAzure OpenAIサービスを利用したテキスト読み上げ機能をTypeScriptで簡単に実装することができるようになります。

## articles/ai-services/openai/includes/whisper-javascript.md{#item-3ee990}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ ms.topic: include
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 9/12/2024
+ms.date: 10/22/2024
 ms.reviewer: v-baolianzou
 ms.author: eur
 author: eric-urban
@@ -13,25 +13,14 @@ author: eric-urban
 
 ## Prerequisites
 
-#### [JavaScript](#tab/javascript)
 
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 
 
-#### [TypeScript](#tab/typescript)
-
-- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
-- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
-- [TypeScript](https://www.typescriptlang.org/download/)
-- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
-
-
----
-
-
 ## Set up
 
 ### Retrieve key and endpoint
@@ -84,7 +73,7 @@ echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/envi
 ```
 ---
 
-## Passwordless authentication is recommended
+## Microsoft Entra ID authentication is recommended
 
 For passwordless authentication, you need to 
 
@@ -113,29 +102,32 @@ Your app's _package.json_ file will be updated with the dependencies.
 
 ## Create a sample application
 
-
-#### [JavaScript](#tab/javascript)
+#### [Microsoft Entra ID](#tab/javascript-keyless)
 
 1. Create a new file named _Whisper.js_ and open it in your preferred code editor. Copy the following code into the _Whisper.js_ file:
 
     ```javascript
-    require("dotenv/config");
     const { createReadStream } = require("fs");
     const { AzureOpenAI } = require("openai");
+    const { DefaultAzureCredential, getBearerTokenProvider } = require("@azure/identity");
     
     // You will need to set these environment variables or edit the following values
-    const audioFilePath = process.env["AUDIO_FILE_PATH"] || "<audio file path>";
+    const audioFilePath = "<audio file path>";
     const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
     
     // Required Azure OpenAI deployment name and API version
     const apiVersion = "2024-08-01-preview";
     const deploymentName = "whisper";
     
+    // keyless authentication    
+    const credential = new DefaultAzureCredential();
+    const scope = "https://cognitiveservices.azure.com/.default";
+    const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+
     function getClient() {
       return new AzureOpenAI({
         endpoint,
-        apiKey,
+        azureADTokenProvider,
         apiVersion,
         deployment: deploymentName,
       });
@@ -165,17 +157,17 @@ Your app's _package.json_ file will be updated with the dependencies.
     ```
 
 
-#### [TypeScript](#tab/typescript)
+
+#### [API key](#tab/typescript-key)
 
 1. Create a new file named _Whisper.js_ and open it in your preferred code editor. Copy the following code into the _Whisper.js_ file:
     
-    ```typescript
-    import "dotenv/config";
+    ```javascript
     import { createReadStream } from "fs";
     import { AzureOpenAI } from "openai";
     
     // You will need to set these environment variables or edit the following values
-    const audioFilePath = process.env["AUDIO_FILE_PATH"] || "<audio file path>";
+    const audioFilePath = "<audio file path>";
     const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
     const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisper APIのJavaScript仕様書のアップデート"
}
```

### Explanation
この変更は、Whisper APIに対するJavaScriptの仕様書を更新したものです。主に、パスワードレス認証からMicrosoft Entra IDを使用した認証方法への移行が行われ、設定手順やサンプルコードが改訂されました。

具体的な変更点は次の通りです：
- **日付の更新**: ドキュメントの日付が2024年9月12日から2024年10月22日に変更されました。
- **前提条件**: AzureのサブスクリプションやNode.js、Azure CLIなどの前提条件が整理され、特にAzure CLIを用いたパスワードレス認証のセクションが強調されました。
- **認証の変更**: パスワードレス認証の推奨がMicrosoft Entra ID認証の推奨に置き換えられ、実装における手順が具体化されました。また、サンプルコードでは、Azure IDの持つ機能を利用するために`DefaultAzureCredential`を用いた新しい認証方法が追加されました。
- **コードの整理**: 提供されるコード例の中で環境変数の設定や必要な値の指定が簡素化され、APIキーの使用がオプションとして扱われるようになりました。

この更新により、開発者は最新のセキュリティ標準に従った簡便な認証方法を利用し、Whisper APIをより安全かつ効率的に扱うことができるようになります。

## articles/ai-services/openai/includes/whisper-typescript.md{#item-eafedb}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,228 @@
+---
+ms.topic: include
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 10/22/2024
+ms.reviewer: v-baolianzou
+ms.author: eur
+author: eric-urban
+---
+
+[Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
+
+## Prerequisites
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [TypeScript](https://www.typescriptlang.org/download/)
+- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
+- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+
+## Set up
+
+### Retrieve key and endpoint
+
+To successfully make a call against Azure OpenAI, you need an *endpoint* and a *key*.
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.|
+| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+
+Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you'll need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+
+:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location circled in red." lightbox="../media/quickstarts/endpoint.png":::
+
+### Environment variables
+
+Create and assign persistent environment variables for your key and endpoint.
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+
+# [Command Line](#tab/command-line)
+
+```CMD
+setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
+```
+
+```CMD
+setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
+```
+
+# [PowerShell](#tab/powershell)
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_KEY_VALUE_HERE', 'User')
+```
+
+```powershell
+[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_ENDPOINT_HERE', 'User')
+```
+
+# [Bash](#tab/bash)
+
+```Bash
+echo export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE" >> /etc/environment && source /etc/environment
+```
+
+```Bash
+echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/environment && source /etc/environment
+```
+---
+
+## Microsoft Entra ID authentication is recommended
+
+For passwordless authentication, you need to 
+
+1. Use the `@azure/identity` package.
+1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal under **Access control (IAM)** > **Add role assignment**.
+1. Sign in with the Azure CLI such as `az login`.
+
+## Create a Node application
+
+In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+
+```console
+npm init
+```
+
+## Install the client library
+
+Install the client libraries with:
+
+```console
+npm install openai @azure/identity
+```
+
+Your app's _package.json_ file will be updated with the dependencies.
+
+## Create a sample application
+
+#### [Microsoft Entra ID](#tab/typescript-keyless)
+
+1. Create a new file named _Whisper.ts_ and open it in your preferred code editor. Copy the following code into the _Whisper.ts_ file:
+    
+    ```typescript
+    import { createReadStream } from "fs";
+    import { AzureOpenAI } from "openai";
+    import { DefaultAzureCredential, getBearerTokenProvider } from "@azure/identity";
+
+    // You will need to set these environment variables or edit the following values
+    const audioFilePath = "<audio file path>";
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    
+    // Required Azure OpenAI deployment name and API version
+    const apiVersion = "2024-08-01-preview";
+    const deploymentName = "whisper";
+
+    // keyless authentication    
+    const credential = new DefaultAzureCredential();
+    const scope = "https://cognitiveservices.azure.com/.default";
+    const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        azureADTokenProvider,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    
+    export async function main() {
+      console.log("== Transcribe Audio Sample ==");
+    
+      const client = getClient();
+      const result = await client.audio.transcriptions.create({
+        model: "",
+        file: createReadStream(audioFilePath),
+      });
+    
+      console.log(`Transcription: ${result.text}`);
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
+    ```
+
+1. Build the application with the following command:
+
+    ```console
+    tsc
+    ```
+
+1. Run the application with the following command:
+
+    ```console
+    node Whisper.js
+    ```
+
+#### [API key](#tab/typescript-key)
+
+1. Create a new file named _Whisper.ts_ and open it in your preferred code editor. Copy the following code into the _Whisper.ts_ file:
+    
+    ```typescript
+    import { createReadStream } from "fs";
+    import { AzureOpenAI } from "openai";
+    
+    // You will need to set these environment variables or edit the following values
+    const audioFilePath = "<audio file path>";
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+    
+    // Required Azure OpenAI deployment name and API version
+    const apiVersion = "2024-08-01-preview";
+    const deploymentName = "whisper";
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    
+    export async function main() {
+      console.log("== Transcribe Audio Sample ==");
+    
+      const client = getClient();
+      const result = await client.audio.transcriptions.create({
+        model: "",
+        file: createReadStream(audioFilePath),
+      });
+    
+      console.log(`Transcription: ${result.text}`);
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
+    ```
+
+1. Build the application with the following command:
+
+    ```console
+    tsc
+    ```
+
+1. Run the application with the following command:
+
+    ```console
+    node Whisper.js
+    ```
+
+---
+
+You can get sample audio files, such as *wikipediaOcelot.wav*, from the [Azure AI Speech SDK repository at GitHub](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/sampledata/audiofiles).
+
+> [!IMPORTANT]
+> For production, store and access your credentials using a secure method, such as [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see [Azure AI services security](../../security-features.md).
+
+## Output
+
+```json
+{"text":"The ocelot, Lepardus paradalis, is a small wild cat native to the southwestern United States, Mexico, and Central and South America. This medium-sized cat is characterized by solid black spots and streaks on its coat, round ears, and white neck and undersides. It weighs between 8 and 15.5 kilograms, 18 and 34 pounds, and reaches 40 to 50 centimeters 16 to 20 inches at the shoulders. It was first described by Carl Linnaeus in 1758. Two subspecies are recognized, L. p. paradalis and L. p. mitis. Typically active during twilight and at night, the ocelot tends to be solitary and territorial. It is efficient at climbing, leaping, and swimming. It preys on small terrestrial mammals such as armadillo, opossum, and lagomorphs."}
+```
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "TypeScriptによるWhisper APIのドキュメント追加"
}
```

### Explanation
この変更は、Whisper APIを使ったTypeScriptによる音声認識機能の新しいドキュメントを追加したものです。このドキュメントには、SDKの使用方法やサンプルコードが含まれており、開発者がAzure OpenAIサービスとのインタラクションを容易に行えるよう支持されています。

具体的には、以下の内容が含まれています：
- **前提条件**: AzureのサブスクリプションやLTS版のNode.js、TypeScript、Azure CLIが必要であることが明記されています。また、これらのリソースを設定する手順が説明されています。
- **セットアップ手順**: Azure OpenAIを利用するために必要なエンドポイントとAPIキーの取得方法が記載されています。環境変数を作成し、クライアントを設定するための具体的なコマンドも提供されています。
- **Microsoft Entra IDによる認証**: パスワードレス認証としてMicrosoft Entra IDを推奨し、そのための手順が詳述されています。
- **サンプルアプリケーションの作成**: TypeScriptでのサンプルアプリケーションを作成する具体的な手順が477行のコードを通じて提供されており、音声ファイルを読み込み、認識結果を表示する方法が示されています。
- **セキュリティに関する注意**: プロダクション環境では、Azure Key Vaultなどの安全な方法でクレデンシャルを管理するよう警告されています。

このドキュメントにより、開発者はAzureのWhisper APIを使用して音声をテキストに変換する機能を簡便に実装することができ、より安全で効率的な開発が可能になります。

## articles/ai-services/openai/text-to-speech-quickstart.md{#item-c344ad}

<details>
<summary>Diff</summary>
````diff
@@ -31,6 +31,12 @@ The available voices are: `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer
 
 ::: zone-end
 
+::: zone pivot="programming-language-typescript"
+
+[!INCLUDE [TypeScript quickstart](includes/text-to-speech-typescript.md)]
+
+::: zone-end
+
 ::: zone pivot="programming-language-dotnet"
 
 [!INCLUDE [.NET quickstart](includes/text-to-speech-dotnet.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト読み上げのクイックスタートドキュメントのTypeScriptセクションの追加"
}
```

### Explanation
この変更は、テキスト読み上げ機能に関するクイックスタートドキュメントの更新で、TypeScriptに関するセクションが新たに追加されました。

具体的な変更点は以下の通りです：
- **TypeScriptセクションの追加**: ドキュメント内にTypeScript用のクイックスタートが新たに追加され、関連する内容は`includes/text-to-speech-typescript.md`ファイルからインクルードされています。これにより、TypeScriptを使用してテキスト読み上げ機能を実装する際のサポートが強化されています。

この追加により、開発者は異なるプログラミング言語（ここではTypeScript）を用いて、テキストを音声に変換する機能を迅速に利用できるようになり、より広範なプラットフォームでの開発が促進されます。

## articles/ai-services/openai/whisper-quickstart.md{#item-4cae3d}

<details>
<summary>Diff</summary>
````diff
@@ -44,6 +44,12 @@ The file size limit for the Whisper model is 25 MB. If you need to transcribe a
 
 ::: zone-end
 
+::: zone pivot="programming-language-typescript"
+
+[!INCLUDE [JavaScript quickstart](includes/whisper-typescript.md)]
+
+::: zone-end
+
 ::: zone pivot="programming-language-powershell"
 
 [!INCLUDE [PowerShell quickstart](includes/whisper-powershell.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "WhisperクイックスタートドキュメントのTypeScriptセクションの追加"
}
```

### Explanation
この変更は、Whisper APIに関するクイックスタートドキュメントの更新で、新たにTypeScriptに関するセクションが追加されました。

具体的な変更内容は以下の通りです：
- **TypeScriptセクションの追加**: ドキュメントにTypeScript用のクイックスタートが新たに挿入され、関連情報は`includes/whisper-typescript.md`ファイルからインクルードされています。これにより、TypeScriptを使用したWhisper APIの利用方法が開発者に対して提供され、利便性が向上します。

この追加によって、Whisper APIを使用する際にJavaScriptの選択肢が強化され、開発者はTypeScriptでの音声認識機能の実装をより簡単に行うことができるようになります。


