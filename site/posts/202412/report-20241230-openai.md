---
date: '2024-12-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dfca068...MicrosoftDocs:c18cb3f
summary: このコードの変更点では、Azure OpenAIサービスドキュメントに対する一連のマイナー更新と新機能の追加が含まれています。主な内容は、グローバルスタンダードのプレビュー表記の更新、新しい環境変数に関するインクルードファイルの追加、及びリアルタイムオーディオ用のモデルとアプリケーションのデプロイ手順の追加です。具体的には、環境変数に関する新しいリソースが提供され、`gpt-4o-realtime-preview`モデルを活用したリアルタイムオーディオアプリケーションのセットアップ手順が詳細に示されています。視覚的に際立つ破壊的変更はなく、全体としてはユーザーが新機能を効果的に活用できるようにサポートすることを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dfca068...MicrosoftDocs:c18cb3f){target="_blank"}

# Highlights

このコードの変更点では、Azure OpenAIサービスドキュメントに対する一連のマイナー更新と新機能の追加が含まれています。特に、グローバルスタンダードについてのプレビュー表記の更新、新しい環境変数に関するインクルードファイルの追加、リアルタイムオーディオ用のモデルとアプリケーションのデプロイ手順の追加が重要なポイントです。

## New features
- 環境変数に関する新しいインクルードファイルの追加。
- キーなしでの環境変数に関する情報の提供。
- `gpt-4o-realtime-preview`モデルを使ったリアルタイムオーディオアプリケーション（JavaScript、Python、TypeScript）のセットアップ手順の追加。
- リアルタイムオーディオ用モデルデプロイの手順を詳述。

## Breaking changes
- 特に視覚的に際立った破壊的変更はありません。

## Other updates
- リアルタイムオーディオクイックスタートのコンテンツ整理と更新。

# Insights

この一連のドキュメント更新は、主にAzure OpenAIサービスの新機能、特にリアルタイムオーディオ処理機能に焦点を当てている点が特徴的です。ユーザーが最新の機能を正しく理解し、利用できるように、詳細で手順にフォーカスした内容が追加されています。

最初のポイントは、グローバルスタンダードのプレビュー表記の更新が行われている点です。これはユーザーに新しいデプロイメントが2025年1月まで利用不可能であることを明示しています。これにより、デプロイメント準備をする際に誤解を避け、計画を適正に立てることができます。

次に、新しいインクルードファイルが追加され、環境変数の設定においてより具体的かつ役立つリソースを有しています。これによってユーザーは迅速に必要な設定を行い、試験や実運用に進めることが可能となります。

リアルタイムオーディオ処理に関しては、`gpt-4o-realtime-preview`モデルは、Azure AI Foundryポータルやリアルタイム音声プレイグラウンドなどと統合するための詳細な手順が含まれています。これにより、言語に依存しない実装を可能にし、さまざまなプラットフォームや言語環境で活用するためのガイドが用意されています。

全体的に、このドキュメント更新はリアルタイム処理のニーズに応えるために開発者やユーザーをサポートすることを目的とし、実用的な技術ガイドを提供しています。その結果、ユーザーはよりスムーズにAzure OpenAIの新機能を使いこなせるようになります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [fine-tuning.md](#item-5c0e85) | minor update | グローバルスタンダードのプレビューを追加 | modified | 2 | 2 | 4 | 
| [env-var-key.md](#item-331f16) | new feature | 環境変数に関する新しいインクルードファイルの追加 | added | 18 | 0 | 18 | 
| [env-var-without-key.md](#item-56a8e2) | new feature | キーなしでの環境変数に関する新しいインクルードファイルの追加 | added | 15 | 0 | 15 | 
| [realtime-deploy-model.md](#item-21f911) | new feature | gpt-4oリアルタイムプレビューモデルのデプロイ手順の追加 | added | 18 | 0 | 18 | 
| [realtime-javascript.md](#item-3c125e) | new feature | リアルタイムJavaScriptアプリケーションのセットアップとデプロイ手順の追加 | added | 278 | 0 | 278 | 
| [realtime-portal.md](#item-1b81a2) | new feature | リアルタイムオーディオ用のモデルデプロイ手順の追加 | added | 31 | 0 | 31 | 
| [realtime-python.md](#item-1291c0) | new feature | リアルタイムオーディオ用Pythonアプリケーションのセットアップ手順の追加 | added | 247 | 0 | 247 | 
| [realtime-typescript.md](#item-eacc9c) | new feature | リアルタイムオーディオ用TypeScriptアプリケーションのセットアップ手順の追加 | added | 290 | 0 | 290 | 
| [realtime-audio-quickstart.md](#item-727df8) | minor update | リアルタイムオーディオクイックスタートの内容の更新 | modified | 10 | 74 | 84 | 


# Modified Contents
## articles/ai-services/openai/how-to/fine-tuning.md{#item-5c0e85}

<details>
<summary>Diff</summary>
````diff
@@ -44,12 +44,12 @@ We use LoRA, or low rank approximation, to fine-tune models in a way that reduce
 
 ::: zone-end
 
-## Global Standard
+## Global Standard (preview)
 
 Azure OpenAI fine-tuning supports [global standard deployments](./deployment-types.md#global-standard) in East US2, North Central US, and Sweden Central for:
 
-- `gpt-4o-2024-08-06`
 - `gpt-4o-mini-2024-07-18`
+- `gpt-4o-2024-08-06` (New deployments aren't available until January 2025)
 
 Global standard fine-tuned deployments offer [cost savings](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/), but custom model weights may temporarily be stored outside the geography of your Azure OpenAI resource.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルスタンダードのプレビューを追加"
}
```

### Explanation
このコードの変更は、「fine-tuning.md」ファイルにおけるマイナーアップデートであり、グローバルスタンダードの説明がプレビューであることを明示するために見出しを修正しました。また、特定のモデルのデプロイメントタイミングについての注意書きも追加されています。この更新により、Azure OpenAIの機能に関する最新情報が提供され、ユーザーの理解を助けることが目的とされています。具体的には、「Global Standard」という見出しが「Global Standard (preview)」に変更され、「新しいデプロイメントは2025年1月まで利用できない」という注釈が追加されています。これにより、ユーザーは新しいデプロイメントの可用性についての重要な情報を得ることができます。

## articles/ai-services/openai/includes/env-var-key.md{#item-331f16}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,18 @@
+---
+author: eric-urban 
+ms.author: eur 
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 12/27/2024
+---
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. |
+| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+| `AZURE_OPENAI_DEPLOYMENT_NAME` | This value will correspond to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Model Deployments** in the Azure portal.|
+| `OPENAI_API_VERSION`|Learn more about [API Versions](/azure/ai-services/openai/api-version-deprecation).|
+
+Learn more about [finding API keys](/azure/ai-services/cognitive-services-environment-variables) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "環境変数に関する新しいインクルードファイルの追加"
}
```

### Explanation
このコードの変更は、新しいファイル「env-var-key.md」が加わったことを示しており、Azure OpenAIサービスの環境変数に関する詳細情報を提供するためのものです。このファイルには、重要な環境変数の名前とその値に関する表が含まれています。特に、`AZURE_OPENAI_ENDPOINT`、`AZURE_OPENAI_API_KEY`、`AZURE_OPENAI_DEPLOYMENT_NAME`、および`OPENAI_API_VERSION`の各環境変数について具体的な説明が記載されています。また、APIキーの見つけ方や環境変数の設定方法に関するリンクも含まれており、ユーザーが必要な情報へ簡単にアクセスできるように配慮がされています。この変更により、Azure OpenAIを使用する際の設定に関するガイダンスが強化されています。

## articles/ai-services/openai/includes/env-var-without-key.md{#item-56a8e2}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,15 @@
+---
+author: eric-urban 
+ms.author: eur 
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 12/27/2024
+---
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. |
+| `AZURE_OPENAI_DEPLOYMENT_NAME` | This value will correspond to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Model Deployments** in the Azure portal.|
+| `OPENAI_API_VERSION`|Learn more about [API Versions](/azure/ai-services/openai/api-version-deprecation).|
+
+Learn more about [keyless authentication](/azure/ai-services/authentication) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "キーなしでの環境変数に関する新しいインクルードファイルの追加"
}
```

### Explanation
このコードの変更は、新しいファイル「env-var-without-key.md」が追加されたことを反映しており、Azure OpenAIサービスにおけるキーなしでの環境変数の設定に関する情報を提供します。このファイルには、`AZURE_OPENAI_ENDPOINT`、`AZURE_OPENAI_DEPLOYMENT_NAME`、および`OPENAI_API_VERSION`の各環境変数に関する詳細な説明が含まれており、特にAzureポータルでの設定方法についてのガイダンスがあります。また、「キーなし認証」や「環境変数の設定」に関連する情報へのリンクも含まれており、ユーザーが必要なリソースに容易にアクセスできるようになっています。この変更は、キーなしでの認証を選択したユーザーに対して、設定手順を明確化するためのものです。

## articles/ai-services/openai/includes/realtime-deploy-model.md{#item-21f911}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,18 @@
+---
+manager: nitinme
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 12/26/2024
+---
+
+To deploy the `gpt-4o-realtime-preview` model in the Azure AI Foundry portal:
+1. Go to the [Azure AI Foundry portal](https://ai.azure.com) and make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource (with or without model deployments.)
+1. Select the **Real-time audio** playground from under **Playgrounds** in the left pane.
+1. Select **Create new deployment** to open the deployment window. 
+1. Search for and select the `gpt-4o-realtime-preview` model and then select **Confirm**.
+1. In the deployment wizard, make sure to select the `2024-10-01` model version.
+1. Follow the wizard to finish deploying the model.
+
+Now that you have a deployment of the `gpt-4o-realtime-preview` model, you can interact with it in real time in the Azure AI Foundry portal **Real-time audio** playground or Realtime API.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "gpt-4oリアルタイムプレビューモデルのデプロイ手順の追加"
}
```

### Explanation
このコードの変更は、新しいファイル「realtime-deploy-model.md」が追加されたことを反映しており、Azure AI Foundryポータルにおける`gpt-4o-realtime-preview`モデルのデプロイ手順を説明しています。このファイルでは、ユーザーがAzure AI Foundryポータルにサインインし、リアルタイム音声プレイグラウンドからモデルをデプロイするための具体的なステップが詳述されています。手順には、モデルの選択、デプロイメントウィンドウの操作、モデルバージョンの選択などが含まれており、ユーザーがスムーズにモデルをデプロイできるように配慮されています。デプロイメントが完了すると、ユーザーはAzure AI Foundryポータルのリアルタイム音声プレイグラウンドやリアルタイムAPIを介して、デプロイしたモデルとリアルタイムでインタラクションできることを強調しています。この変更は、リアルタイムモデルの利用に関する情報を提供し、ユーザーの操作をサポートすることを目的としています。

## articles/ai-services/openai/includes/realtime-javascript.md{#item-3c125e}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,278 @@
+---
+manager: nitinme
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 12/26/2024
+---
+
+## Prerequisites
+
+- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
+- <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
+- An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- Then, you need to deploy a `gpt-4o-realtime-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
+
+## Microsoft Entra ID prerequisites
+
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
+
+## Deploy a model for real-time audio
+
+[!INCLUDE [Deploy model](realtime-deploy-model.md)]
+
+## Set up
+
+1. Create a new folder `realtime-audio-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
+
+    ```shell
+    mkdir realtime-audio-quickstart && code realtime-audio-quickstart
+    ```
+    
+1. Create the `package.json` with the following command:
+
+    ```shell
+    npm init -y
+    ```
+
+1. Update the `package.json` to ECMAScript with the following command: 
+
+    ```shell
+    npm pkg set type=module
+    ```
+    
+
+1. Install the real-time audio client library for JavaScript with:
+
+    ```console
+    npm install https://github.com/Azure-Samples/aoai-realtime-audio-sdk/releases/download/js/v0.5.2/rt-client-0.5.2.tgz
+    ```
+
+1. For the **recommended** keyless authentication with Microsoft Entra ID, install the `@azure/identity` package with:
+
+    ```console
+    npm install @azure/identity
+    ```
+
+## Retrieve resource information
+
+#### [Microsoft Entra ID](#tab/javascript-keyless)
+
+[!INCLUDE [keyless-environment-variables](env-var-without-key.md)]
+
+#### [API key](#tab/javascript-key)
+
+[!INCLUDE [key-environment-variables](env-var-key.md)]
+
+---
+
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+
+## Text in audio out
+
+#### [Microsoft Entra ID](#tab/javascript-keyless)
+
+1. Create the `text-in-audio-out.js` file with the following code:
+
+    ```javascript 
+    import { DefaultAzureCredential } from "@azure/identity";
+    import { LowLevelRTClient } from "rt-client";
+    import dotenv from "dotenv";
+    dotenv.config();
+    async function text_in_audio_out() {
+        // Set environment variables or edit the corresponding values here.
+        const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "yourEndpoint";
+        const deployment = "gpt-4o-realtime-preview";
+        if (!endpoint || !deployment) {
+            throw new Error("You didn't set the environment variables.");
+        }
+        const client = new LowLevelRTClient(new URL(endpoint), new DefaultAzureCredential(), { deployment: deployment });
+        try {
+            await client.send({
+                type: "response.create",
+                response: {
+                    modalities: ["audio", "text"],
+                    instructions: "Please assist the user."
+                }
+            });
+            for await (const message of client.messages()) {
+                switch (message.type) {
+                    case "response.done": {
+                        break;
+                    }
+                    case "error": {
+                        console.error(message.error);
+                        break;
+                    }
+                    case "response.audio_transcript.delta": {
+                        console.log(`Received text delta: ${message.delta}`);
+                        break;
+                    }
+                    case "response.audio.delta": {
+                        const buffer = Buffer.from(message.delta, "base64");
+                        console.log(`Received ${buffer.length} bytes of audio data.`);
+                        break;
+                    }
+                }
+                if (message.type === "response.done" || message.type === "error") {
+                    break;
+                }
+            }
+        }
+        finally {
+            client.close();
+        }
+    }
+    await text_in_audio_out();
+    ```
+
+1. Sign in to Azure with the following command:
+
+    ```shell
+    az login
+    ```
+
+1. Run the JavaScript file.
+
+    ```shell
+    node text-in-audio-out.js
+    ```
+
+
+#### [API key](#tab/javascript-key)
+
+1. Create the `text-in-audio-out.js` file with the following code:
+
+    ```javascript 
+    import { AzureKeyCredential } from "@azure/core-auth";
+    import { LowLevelRTClient } from "rt-client";
+    import dotenv from "dotenv";
+    dotenv.config();
+    async function text_in_audio_out() {
+        // Set environment variables or edit the corresponding values here.
+        const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "yourKey";
+        const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "yourEndpoint";
+        const deployment = "gpt-4o-realtime-preview";
+        if (!endpoint || !deployment) {
+            throw new Error("You didn't set the environment variables.");
+        }
+        const client = new LowLevelRTClient(new URL(endpoint), new AzureKeyCredential(apiKey), { deployment: deployment });
+        try {
+            await client.send({
+                type: "response.create",
+                response: {
+                    modalities: ["audio", "text"],
+                    instructions: "Please assist the user."
+                }
+            });
+            for await (const message of client.messages()) {
+                switch (message.type) {
+                    case "response.done": {
+                        break;
+                    }
+                    case "error": {
+                        console.error(message.error);
+                        break;
+                    }
+                    case "response.audio_transcript.delta": {
+                        console.log(`Received text delta: ${message.delta}`);
+                        break;
+                    }
+                    case "response.audio.delta": {
+                        const buffer = Buffer.from(message.delta, "base64");
+                        console.log(`Received ${buffer.length} bytes of audio data.`);
+                        break;
+                    }
+                }
+                if (message.type === "response.done" || message.type === "error") {
+                    break;
+                }
+            }
+        }
+        finally {
+            client.close();
+        }
+    }
+    await text_in_audio_out();
+    ```
+
+1. Run the JavaScript file.
+
+    ```shell
+    node text-in-audio-out.js
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+## Output
+
+The script gets a response from the model and prints the transcript and audio data received.
+
+The output will look similar to the following:
+
+```console
+Received text delta: Hello
+Received text delta: !
+Received text delta:  How
+Received text delta:  can
+Received text delta:  I
+Received 4800 bytes of audio data.
+Received 7200 bytes of audio data.
+Received text delta:  help
+Received 12000 bytes of audio data.
+Received text delta:  you
+Received text delta:  today
+Received text delta: ?
+Received 12000 bytes of audio data.
+Received 12000 bytes of audio data.
+Received 12000 bytes of audio data.
+Received 24000 bytes of audio data.
+```
+
+## Web application sample
+
+Our JavaScript web sample [on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk) demonstrates how to use the GPT-4o Realtime API to interact with the model in real time. The sample code includes a simple web interface that captures audio from the user's microphone and sends it to the model for processing. The model responds with text and audio, which the sample code renders in the web interface.
+
+You can run the sample code locally on your machine by following these steps. Refer to the [repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk) for the most up-to-date instructions.
+1. If you don't have Node.js installed, download and install the [LTS version of Node.js](https://nodejs.org/).
+
+1. Clone the repository to your local machine:
+    
+    ```bash
+    git clone https://github.com/Azure-Samples/aoai-realtime-audio-sdk.git
+    ```
+
+1. Go to the `javascript/samples/web` folder in your preferred code editor.
+
+    ```bash
+    cd ./javascript/samples
+    ```
+
+1. Run `download-pkg.ps1` or `download-pkg.sh` to download the required packages. 
+
+1. Go to the `web` folder from the `./javascript/samples` folder.
+
+    ```bash
+    cd ./web
+    ```
+
+1. Run `npm install` to install package dependencies.
+
+1. Run `npm run dev` to start the web server, navigating any firewall permissions prompts as needed.
+1. Go to any of the provided URIs from the console output (such as `http://localhost:5173/`) in a browser.
+1. Enter the following information in the web interface:
+    - **Endpoint**: The resource endpoint of an Azure OpenAI resource. You don't need to append the `/realtime` path. An example structure might be `https://my-azure-openai-resource-from-portal.openai.azure.com`.
+    - **API Key**: A corresponding API key for the Azure OpenAI resource.
+    - **Deployment**: The name of the `gpt-4o-realtime-preview` model that [you deployed in the previous section](#deploy-a-model-for-real-time-audio).
+    - **System Message**: Optionally, you can provide a system message such as "You always talk like a friendly pirate."
+    - **Temperature**: Optionally, you can provide a custom temperature.
+    - **Voice**: Optionally, you can select a voice.
+1. Select the **Record** button to start the session. Accept permissions to use your microphone if prompted.
+1. You should see a `<< Session Started >>` message in the main output. Then you can speak into the microphone to start a chat.
+1. You can interrupt the chat at any time by speaking. You can end the chat by selecting the **Stop** button.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "リアルタイムJavaScriptアプリケーションのセットアップとデプロイ手順の追加"
}
```

### Explanation
このコードの変更は、新しいファイル「realtime-javascript.md」が追加されたことを反映しており、Azure OpenAIサービスを利用したリアルタイムなオーディオ処理のためのJavaScriptアプリケーションに関する詳細な手順を提供しています。このファイルでは、必要な前提条件、Microsoft Entra IDを使用したキーなし認証、モデルのデプロイメント手順などが明確に記載されています。

手順には、Node.js環境の設定、アプリケーションフォルダの作成、必要なパッケージのインストールが含まれています。また、`text-in-audio-out.js`というJavaScriptファイルを作成し、Azure OpenAIサービスにアクセスするためのコードサンプルが詳細に説明されています。ユーザーは、このスクリプトを実行することで、モデルとのインタラクションをリアルタイムで楽しむことができます。

さらに、Webアプリケーションのサンプルについても触れられており、GitHub上のリポジトリにリンクが提供され、そこで実行する方法に関する手順が示されています。この変更は、開発者がAzure OpenAIサービスの機能を活用し、リアルタイムでの音声処理機能を実装できるようにサポートすることを目的としています。

## articles/ai-services/openai/includes/realtime-portal.md{#item-1b81a2}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,31 @@
+---
+manager: nitinme
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 12/26/2024
+---
+
+## Deploy a model for real-time audio
+
+[!INCLUDE [Deploy model](realtime-deploy-model.md)]
+
+## Use the GPT-4o real-time audio
+
+To chat with your deployed `gpt-4o-realtime-preview` model in the [Azure AI Foundry](https://ai.azure.com) **Real-time audio** playground, follow these steps:
+
+1. Go to the [Azure OpenAI Service page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource and the deployed `gpt-4o-realtime-preview` model.
+1. Select the **Real-time audio** playground from under **Playgrounds** in the left pane.
+1. Select your deployed `gpt-4o-realtime-preview` model from the **Deployment** dropdown. 
+1. Select **Enable microphone** to allow the browser to access your microphone. If you already granted permission, you can skip this step.
+
+    :::image type="content" source="../media/how-to/real-time/real-time-playground.png" alt-text="Screenshot of the real-time audio playground with the deployed model selected." lightbox="../media/how-to/real-time/real-time-playground.png":::
+
+1. Optionally, you can edit contents in the **Give the model instructions and context** text box. Give the model instructions about how it should behave and any context it should reference when generating a response. You can describe the assistant's personality, tell it what it should and shouldn't answer, and tell it how to format responses.
+1. Optionally, change settings such as threshold, prefix padding, and silence duration.
+1. Select **Start listening** to start the session. You can speak into the microphone to start a chat.
+
+    :::image type="content" source="../media/how-to/real-time/real-time-playground-start-listening.png" alt-text="Screenshot of the real-time audio playground with the start listening button and microphone access enabled." lightbox="../media/how-to/real-time/real-time-playground-start-listening.png":::
+
+1. You can interrupt the chat at any time by speaking. You can end the chat by selecting the **Stop listening** button.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "リアルタイムオーディオ用のモデルデプロイ手順の追加"
}
```

### Explanation
このコードの変更は、新しいファイル「realtime-portal.md」の追加を示しており、Azure AI Foundryポータルでの`gpt-4o-realtime-preview`モデルを使用したリアルタイムオーディオの利用手順を説明しています。このドキュメントでは、ユーザーがモデルをデプロイし、リアルタイムオーディオプレイグラウンドでのチャットを開始するための具体的なステップが記載されています。

手順には、Azure AI Foundryポータルへのサインイン、展開されたモデルの選択、マイクへのアクセス許可の付与などが含まれています。また、ユーザーがモデルに指示やコンテキストを提供するためのオプションとしてのテキストボックスの編集や、設定の変更が可能であることも示されています。最終的には、ユーザーがマイクで話しかけてチャットセッションを開始する手順が説明されており、これによりリアルタイムでモデルと対話できるようになります。

この変更は、Azure AI Foundryを活用したリアルタイムオーディオ体験を提供し、開発者やユーザーが簡単にモデルとやり取りできるようサポートすることを目的としています。

## articles/ai-services/openai/includes/realtime-python.md{#item-1291c0}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,247 @@
+---
+manager: nitinme
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 12/26/2024
+---
+
+## Prerequisites
+
+- An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
+- <a href="https://www.python.org/" target="_blank">Python 3.8 or later version</a>. We recommend using Python 3.10 or later, but having at least Python 3.8 is required. If you don't have a suitable version of Python installed, you can follow the instructions in the [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter) for the easiest way of installing Python on your operating system.
+- An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- Then, you need to deploy a `gpt-4o-realtime-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+
+## Microsoft Entra ID prerequisites
+
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
+
+## Deploy a model for real-time audio
+
+[!INCLUDE [Deploy model](realtime-deploy-model.md)]
+
+## Set up
+
+1. Create a new folder `realtime-audio-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
+
+    ```shell
+    mkdir realtime-audio-quickstart && code realtime-audio-quickstart
+    ```
+    
+1. Create a virtual environment. If you already have Python 3.10 or higher installed, you can create a virtual environment using the following commands:
+    
+    # [Windows](#tab/windows)
+    
+    ```bash
+    py -3 -m venv .venv
+    .venv\scripts\activate
+    ```
+    
+    # [Linux](#tab/linux)
+    
+    ```bash
+    python3 -m venv .venv
+    source .venv/bin/activate
+    ```
+    
+    # [macOS](#tab/macos)
+    
+    ```bash
+    python3 -m venv .venv
+    source .venv/bin/activate
+    ```
+    
+    ---
+    
+    Activating the Python environment means that when you run ```python``` or ```pip``` from the command line, you then use the Python interpreter contained in the ```.venv``` folder of your application. You can use the ```deactivate``` command to exit the python virtual environment, and can later reactivate it when needed.
+
+    > [!TIP]
+    > We recommend that you create and activate a new Python environment to use to install the packages you need for this tutorial. Don't install packages into your global python installation. You should always use a virtual or conda environment when installing python packages, otherwise you can break your global installation of Python.
+
+1. Install the real-time audio client library for Python with:
+
+    ```console
+    pip install "https://github.com/Azure-Samples/aoai-realtime-audio-sdk/releases/download/py%2Fv0.5.3/rtclient-0.5.3.tar.gz"
+    ```
+
+1. For the **recommended** keyless authentication with Microsoft Entra ID, install the `azure-identity` package with:
+
+    ```console
+    pip install azure-identity
+    ```
+
+## Retrieve resource information
+
+#### [Microsoft Entra ID](#tab/javascript-keyless)
+
+[!INCLUDE [keyless-environment-variables](env-var-without-key.md)]
+
+#### [API key](#tab/javascript-key)
+
+[!INCLUDE [key-environment-variables](env-var-key.md)]
+
+---
+
+## Text in audio out
+
+## [Microsoft Entra ID](#tab/javascript-keyless)
+
+1. Create the `text-in-audio-out.py` file with the following code:
+
+    ```python
+    import base64
+    import asyncio
+    from azure.identity.aio import DefaultAzureCredential
+    from rtclient import (
+        ResponseCreateMessage,
+        RTLowLevelClient,
+        ResponseCreateParams
+    )
+    
+    # Set environment variables or edit the corresponding values here.
+    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
+    deployment = "gpt-4o-realtime-preview"
+    
+    async def text_in_audio_out():
+        async with RTLowLevelClient(
+            url=endpoint,
+            azure_deployment=deployment,
+            token_credential=DefaultAzureCredential(),
+        ) as client:
+            await client.send(
+                ResponseCreateMessage(
+                    response=ResponseCreateParams(
+                        modalities={"audio", "text"}, 
+                        instructions="Please assist the user."
+                    )
+                )
+            )
+            done = False
+            while not done:
+                message = await client.recv()
+                match message.type:
+                    case "response.done":
+                        done = True
+                    case "error":
+                        done = True
+                        print(message.error)
+                    case "response.audio_transcript.delta":
+                        print(f"Received text delta: {message.delta}")
+                    case "response.audio.delta":
+                        buffer = base64.b64decode(message.delta)
+                        print(f"Received {len(buffer)} bytes of audio data.")
+                    case _:
+                        pass
+    
+    async def main():
+        await text_in_audio_out()
+    
+    asyncio.run(main())
+    ```
+
+1. Run the Python file.
+
+    ```shell
+    python text-in-audio-out.py
+    ```
+
+## [API key](#tab/javascript-key)
+
+1. Create the `text-in-audio-out.py` file with the following code:
+
+    ```python
+    import base64
+    import asyncio
+    from azure.core.credentials import AzureKeyCredential
+    from rtclient import (
+        ResponseCreateMessage,
+        RTLowLevelClient,
+        ResponseCreateParams
+    )
+    
+    # Set environment variables or edit the corresponding values here.
+    api_key = os.environ["AZURE_OPENAI_API_KEY"]    
+    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
+    deployment = "gpt-4o-realtime-preview"
+    
+    async def text_in_audio_out():
+        async with RTLowLevelClient(
+            url=endpoint,
+            azure_deployment=deployment,
+            key_credential=AzureKeyCredential(api_key) 
+        ) as client:
+            await client.send(
+                ResponseCreateMessage(
+                    response=ResponseCreateParams(
+                        modalities={"audio", "text"}, 
+                        instructions="Please assist the user."
+                    )
+                )
+            )
+            done = False
+            while not done:
+                message = await client.recv()
+                match message.type:
+                    case "response.done":
+                        done = True
+                    case "error":
+                        done = True
+                        print(message.error)
+                    case "response.audio_transcript.delta":
+                        print(f"Received text delta: {message.delta}")
+                    case "response.audio.delta":
+                        buffer = base64.b64decode(message.delta)
+                        print(f"Received {len(buffer)} bytes of audio data.")
+                    case _:
+                        pass
+    
+    async def main():
+        await text_in_audio_out()
+    
+    asyncio.run(main())
+    ```
+
+1. Run the Python file.
+
+    ```shell
+    python text-in-audio-out.py
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+## Output
+
+The script gets a response from the model and prints the transcript and audio data received.
+
+The output will look similar to the following:
+
+```console
+Received text delta: Hello
+Received text delta: !
+Received text delta:  How
+Received 4800 bytes of audio data.
+Received 7200 bytes of audio data.
+Received text delta:  can
+Received 12000 bytes of audio data.
+Received text delta:  I
+Received text delta:  assist
+Received text delta:  you
+Received 12000 bytes of audio data.
+Received 12000 bytes of audio data.
+Received text delta:  today
+Received text delta: ?
+Received 12000 bytes of audio data.
+Received 12000 bytes of audio data.
+Received 12000 bytes of audio data.
+Received 12000 bytes of audio data.
+Received 28800 bytes of audio data.
+```
+
+
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "リアルタイムオーディオ用Pythonアプリケーションのセットアップ手順の追加"
}
```

### Explanation
このコードの変更は、新しいファイル「realtime-python.md」を追加したもので、Azure OpenAIサービスを使用したリアルタイムオーディオ機能のためのPythonアプリケーションのセットアップ手順を提供しています。このドキュメントでは、必要な前提条件、Microsoft Entra IDを使用したキーなし認証、モデルのデプロイ手順、実際のコードサンプルが詳述されています。

手順には、Azureサブスクリプションの作成、Pythonのバージョン確認、Azure OpenAIリソースの作成、および`gpt-4o-realtime-preview`モデルのデプロイが含まれています。また、Pyhton仮想環境の作成や必要なパッケージのインストール方法が示され、実際にモデルと音声でインタラクションするためのサンプルコード（`text-in-audio-out.py`）が提供されています。このコードは、オーディオデータの生成とテキストの取得を行う非同期処理を行います。

さらに、ユーザーがスクリプトを実行し、どのような出力が期待されるかについても説明しています。この変更により、開発者はAzure OpenAIの機能を利用してリアルタイム音声クロスコミュニケーションを構築できるようになります。

## articles/ai-services/openai/includes/realtime-typescript.md{#item-eacc9c}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,290 @@
+---
+manager: nitinme
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 12/26/2024
+---
+
+## Prerequisites
+
+- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
+- <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
+- [TypeScript](https://www.typescriptlang.org/download/) installed globally.
+- An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- Then, you need to deploy a `gpt-4o-realtime-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
+
+## Microsoft Entra ID prerequisites
+
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
+
+## Deploy a model for real-time audio
+
+[!INCLUDE [Deploy model](realtime-deploy-model.md)]
+
+## Set up
+
+1. Create a new folder `realtime-audio-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
+
+    ```shell
+    mkdir realtime-audio-quickstart && code realtime-audio-quickstart
+    ```
+    
+
+1. Create the `package.json` with the following command:
+
+    ```shell
+    npm init -y
+    ```
+
+1. Update the `package.json` to ECMAScript with the following command: 
+
+    ```shell
+    npm pkg set type=module
+    ```
+    
+1. Install the real-time audio client library for JavaScript with:
+
+    ```console
+    npm install https://github.com/Azure-Samples/aoai-realtime-audio-sdk/releases/download/js/v0.5.2/rt-client-0.5.2.tgz
+    ```
+
+1. For the **recommended** keyless authentication with Microsoft Entra ID, install the `@azure/identity` package with:
+
+    ```console
+    npm install @azure/identity
+    ```
+
+## Retrieve resource information
+
+#### [Microsoft Entra ID](#tab/javascript-keyless)
+
+[!INCLUDE [keyless-environment-variables](env-var-without-key.md)]
+
+#### [API key](#tab/javascript-key)
+
+[!INCLUDE [key-environment-variables](env-var-key.md)]
+
+---
+
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
+    
+## Text in audio out
+
+#### [Microsoft Entra ID](#tab/typescript-keyless)
+
+1. Create the `text-in-audio-out.ts` file with the following code:
+
+    ```typescript
+    import { DefaultAzureCredential } from "@azure/identity";
+    import { LowLevelRTClient } from "rt-client";
+    import dotenv from "dotenv";
+    dotenv.config();
+    
+    async function text_in_audio_out() {
+        // Set environment variables or edit the corresponding values here.
+        const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "yourEndpoint";
+        const deployment = "gpt-4o-realtime-preview";
+        if (!endpoint || !deployment) {
+            throw new Error("You didn't set the environment variables.");
+        }
+        const client = new LowLevelRTClient(
+            new URL(endpoint), 
+            new DefaultAzureCredential(), 
+            {deployment: deployment}
+        );
+        try {
+            await client.send({
+                type: "response.create",
+                response: {
+                    modalities: ["audio", "text"],
+                    instructions: "Please assist the user."
+                }
+            });
+    
+            for await (const message of client.messages()) {
+                switch (message.type) {
+                    case "response.done": {
+                        break;
+                    }
+                    case "error": {
+                        console.error(message.error);
+                        break;
+                    }
+                    case "response.audio_transcript.delta": {
+                        console.log(`Received text delta: ${message.delta}`);
+                        break;
+                    }
+                    case "response.audio.delta": {
+                        const buffer = Buffer.from(message.delta, "base64");
+                        console.log(`Received ${buffer.length} bytes of audio data.`);
+                        break;
+                    }
+                }
+                if (message.type === "response.done" || message.type === "error") {
+                    break;
+                }
+            }
+        } finally {
+            client.close();
+        }
+    }
+    
+    await text_in_audio_out();
+    ```
+
+1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
+
+    ```json
+    {
+        "compilerOptions": {
+          "module": "NodeNext",
+          "target": "ES2022", // Supports top-level await
+          "moduleResolution": "NodeNext",
+          "skipLibCheck": true, // Avoid type errors from node_modules
+          "strict": true // Enable strict type-checking options
+        },
+        "include": ["*.ts"]
+    }
+    ```
+
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
+    tsc
+    ```
+    
+1. Sign in to Azure with the following command:
+
+    ```shell
+    az login
+    ```
+
+1. Run the code with the following command:
+
+    ```shell
+    node text-in-audio-out.js
+    ```
+
+#### [API key](#tab/typescript-key)
+
+1. Create the `text-in-audio-out.ts` file with the following code:
+
+    ```typescript
+    import { AzureKeyCredential } from "@azure/core-auth";
+    import { LowLevelRTClient } from "rt-client";
+    import dotenv from "dotenv";
+    dotenv.config();
+    
+    async function text_in_audio_out() {
+        // Set environment variables or edit the corresponding values here.
+        const apiKey: string = process.env["AZURE_OPENAI_API_KEY"] || "yourKey";
+        const endpoint: string = process.env["AZURE_OPENAI_ENDPOINT"] || "yourEndpoint";
+        const deployment = "gpt-4o-realtime-preview";
+        if (!endpoint || !deployment) {
+            throw new Error("You didn't set the environment variables.");
+        }
+        const client = new LowLevelRTClient(
+            new URL(endpoint), 
+            new AzureKeyCredential(apiKey),
+            {deployment: deployment}
+        );
+        try {
+            await client.send({
+                type: "response.create",
+                response: {
+                    modalities: ["audio", "text"],
+                    instructions: "Please assist the user."
+                }
+            });
+    
+            for await (const message of client.messages()) {
+                switch (message.type) {
+                    case "response.done": {
+                        break;
+                    }
+                    case "error": {
+                        console.error(message.error);
+                        break;
+                    }
+                    case "response.audio_transcript.delta": {
+                        console.log(`Received text delta: ${message.delta}`);
+                        break;
+                    }
+                    case "response.audio.delta": {
+                        const buffer = Buffer.from(message.delta, "base64");
+                        console.log(`Received ${buffer.length} bytes of audio data.`);
+                        break;
+                    }
+                }
+                if (message.type === "response.done" || message.type === "error") {
+                    break;
+                }
+            }
+        } finally {
+            client.close();
+        }
+    }
+    
+    await text_in_audio_out();
+    ```
+
+1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
+
+    ```json
+    {
+        "compilerOptions": {
+          "module": "NodeNext",
+          "target": "ES2022", // Supports top-level await
+          "moduleResolution": "NodeNext",
+          "skipLibCheck": true, // Avoid type errors from node_modules
+          "strict": true // Enable strict type-checking options
+        },
+        "include": ["*.ts"]
+    }
+    ```
+
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
+    tsc
+    ```
+
+1. Run the code with the following command:
+
+    ```shell
+    node text-in-audio-out.js
+    ```
+
+---
+
+Wait a few moments to get the response.
+
+## Output
+
+The script gets a response from the model and prints the transcript and audio data received.
+
+The output will look similar to the following:
+
+```console
+Received text delta: Hello
+Received text delta: !
+Received text delta:  How
+Received text delta:  can
+Received text delta:  I
+Received 4800 bytes of audio data.
+Received 7200 bytes of audio data.
+Received text delta:  help
+Received 12000 bytes of audio data.
+Received text delta:  you
+Received text delta:  today
+Received text delta: ?
+Received 12000 bytes of audio data.
+Received 12000 bytes of audio data.
+Received 12000 bytes of audio data.
+Received 24000 bytes of audio data.
+```
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "リアルタイムオーディオ用TypeScriptアプリケーションのセットアップ手順の追加"
}
```

### Explanation
このコードの変更は、新しいファイル「realtime-typescript.md」を追加したもので、Azure OpenAIサービスを使用したリアルタイムオーディオ機能のためのTypeScriptアプリケーションのセットアップ手順を提供しています。このドキュメントでは、必要な前提条件、Microsoft Entra IDを利用したキーなし認証、モデルのデプロイ手順、実際のTypeScriptサンプルコードが詳しく説明されています。

手順には、Azureサブスクリプションの作成、Node.jsおよびTypeScriptのインストール、Azure OpenAIリソースの作成、そして`gpt-4o-realtime-preview`モデルのデプロイが含まれています。また、TypeScriptコードの雛形や必要なパッケージのインストール方法が提供され、リアルタイムオーディオ機能とのインタラクションを実現するための実用的なコード例が示されています。

さらに、ユーザーがスクリプトを実行し、期待される出力結果についても説明されています。この変更は、開発者がAzure OpenAIのリアルタイムオーディオ機能を利用して、アプリケーションに簡単に統合できるよう支援するものです。

## articles/ai-services/openai/realtime-audio-quickstart.md{#item-727df8}

<details>
<summary>Diff</summary>
````diff
@@ -5,11 +5,11 @@ description: Learn how to use GPT-4o Realtime API for speech and audio with Azur
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 12/11/2024
+ms.date: 12/26/2024
 author: eric-urban
 ms.author: eur
 ms.custom: references_regions, ignite-2024
-zone_pivot_groups: openai-portal-js
+zone_pivot_groups: openai-portal-js-python-ts
 recommendations: false
 ---
 
@@ -37,91 +37,27 @@ Support for the Realtime API was first added in API version `2024-10-01-preview`
 > [!NOTE]
 > For more information about the API and architecture, see the [Azure OpenAI GPT-4o real-time audio repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk).
 
-## Prerequisites
-
-- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
-- An Azure OpenAI resource created in a [supported region](#supported-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](./how-to/create-resource.md).
-
-## Deploy a model for real-time audio
-
-Before you can use GPT-4o real-time audio, you need a deployment of the `gpt-4o-realtime-preview` model in a supported region as described in the [supported models](#supported-models) section.
-
-1. Go to the [Azure AI Foundry home page](https://ai.azure.com) and make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource (with or without model deployments.)
-1. Select the **Real-time audio** playground from under **Resource playground** in the left pane.
-1. Select **+ Create a deployment** to open the deployment window. 
-1. Search for and select the `gpt-4o-realtime-preview` model and then select **Confirm**.
-1. In the deployment wizard, make sure to select the `2024-10-01` model version.
-1. Follow the wizard to deploy the model.
-
-Now that you have a deployment of the `gpt-4o-realtime-preview` model, you can interact with it in real time in the Azure AI Foundry portal **Real-time audio** playground or Realtime API.
-
-## Use the GPT-4o real-time audio
-
-> [!TIP]
-> Right now, the fastest way to get started development with the GPT-4o Realtime API is to download the sample code from the [Azure OpenAI GPT-4o real-time audio repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk).
-
 ::: zone pivot="ai-foundry-portal"
 
-To chat with your deployed `gpt-4o-realtime-preview` model in the [Azure AI Foundry](https://ai.azure.com) **Real-time audio** playground, follow these steps:
-
-1. the [Azure OpenAI Service page](https://ai.azure.com/resource/overview) in Azure AI Foundry portal. Make sure you're signed in with the Azure subscription that has your Azure OpenAI Service resource and the deployed `gpt-4o-realtime-preview` model.
-1. Select the **Real-time audio** playground from under **Resource playground** in the left pane.
-1. Select your deployed `gpt-4o-realtime-preview` model from the **Deployment** dropdown. 
-1. Select **Enable microphone** to allow the browser to access your microphone. If you already granted permission, you can skip this step.
-
-    :::image type="content" source="./media/how-to/real-time/real-time-playground.png" alt-text="Screenshot of the real-time audio playground with the deployed model selected." lightbox="./media/how-to/real-time/real-time-playground.png":::
-
-1. Optionally you can edit contents in the **Give the model instructions and context** text box. Give the model instructions about how it should behave and any context it should reference when generating a response. You can describe the assistant's personality, tell it what it should and shouldn't answer, and tell it how to format responses.
-1. Optionally, change settings such as threshold, prefix padding, and silence duration.
-1. Select **Start listening** to start the session. You can speak into the microphone to start a chat.
-
-    :::image type="content" source="./media/how-to/real-time/real-time-playground-start-listening.png" alt-text="Screenshot of the real-time audio playground with the start listening button and microphone access enabled." lightbox="./media/how-to/real-time/real-time-playground-start-listening.png":::
-
-1. You can interrupt the chat at any time by speaking. You can end the chat by selecting the **Stop listening** button.
+[!INCLUDE [Azure AI Foundry portal quickstart](includes/realtime-portal.md)]
 
 ::: zone-end
 
 ::: zone pivot="programming-language-javascript"
 
-The JavaScript web sample demonstrates how to use the GPT-4o Realtime API to interact with the model in real time. The sample code includes a simple web interface that captures audio from the user's microphone and sends it to the model for processing. The model responds with text and audio, which the sample code renders in the web interface.
-
-You can run the sample code locally on your machine by following these steps. Refer to the [repository on GitHub](https://github.com/azure-samples/aoai-realtime-audio-sdk) for the most up-to-date instructions.
-1. If you don't have Node.js installed, download and install the [LTS version of Node.js](https://nodejs.org/).
+[!INCLUDE [JavaScript quickstart](includes/realtime-javascript.md)]
 
-1. Clone the repository to your local machine:
-    
-    ```bash
-    git clone https://github.com/Azure-Samples/aoai-realtime-audio-sdk.git
-    ```
-
-1. Go to the `javascript/samples/web` folder in your preferred code editor.
-
-    ```bash
-    cd ./javascript/samples
-    ```
+::: zone-end
 
-1. Run `download-pkg.ps1` or `download-pkg.sh` to download the required packages. 
+::: zone pivot="programming-language-python"
 
-1. Go to the `web` folder from the `./javascript/samples` folder.
+[!INCLUDE [Python quickstart](includes/realtime-python.md)]
 
-    ```bash
-    cd ./web
-    ```
+::: zone-end
 
-1. Run `npm install` to install package dependencies.
+::: zone pivot="programming-language-typescript"
 
-1. Run `npm run dev` to start the web server, navigating any firewall permissions prompts as needed.
-1. Go to any of the provided URIs from the console output (such as `http://localhost:5173/`) in a browser.
-1. Enter the following information in the web interface:
-    - **Endpoint**: The resource endpoint of an Azure OpenAI resource. You don't need to append the `/realtime` path. An example structure might be `https://my-azure-openai-resource-from-portal.openai.azure.com`.
-    - **API Key**: A corresponding API key for the Azure OpenAI resource.
-    - **Deployment**: The name of the `gpt-4o-realtime-preview` model that [you deployed in the previous section](#deploy-a-model-for-real-time-audio).
-    - **System Message**: Optionally, you can provide a system message such as "You always talk like a friendly pirate."
-    - **Temperature**: Optionally, you can provide a custom temperature.
-    - **Voice**: Optionally, you can select a voice.
-1. Select the **Record** button to start the session. Accept permissions to use your microphone if prompted.
-1. You should see a `<< Session Started >>` message in the main output. Then you can speak into the microphone to start a chat.
-1. You can interrupt the chat at any time by speaking. You can end the chat by selecting the **Stop** button.
+[!INCLUDE [TypeScript quickstart](includes/realtime-typescript.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオクイックスタートの内容の更新"
}
```

### Explanation
このコードの変更は、「realtime-audio-quickstart.md」ファイルに加えられたもので、主にコンテンツの整理と更新を行っています。特に、不要な情報の削除と新しい参照の追加が行われ、ファイル全体の構造がより明確になりました。

変更点には、Azure OpenAIサービスのクイックスタートガイドに関連する情報の更新や、日付や著者情報の修正が含まれています。また、リアルタイムオーディオの使用に必要な手順のリンクを新しく含め、プログラミング言語別にそれぞれのクイックスタートガイドを指し示すインクルード文を追加しました。例えば、JavaScript、Python、TypeScript用のクイックスタートガイドへのリンクが新たに追加され、利用者が各プラットフォームでの実装を簡単に参照できるようになっています。

この更新により、ユーザーは最新の情報をもとにしながら、Azureのリアルタイムオーディオ機能を効果的に利用できるようになります。


