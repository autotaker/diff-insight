---
date: '2024-10-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d84fb33...MicrosoftDocs:a68723c
summary: この修正では、DALL·EおよびGPT-4 Turbo with Visionのクイックスタートガイドが大幅にアップデートされ、新しいTypeScript
  SDKセクションが追加されました。また、JavaScriptガイドも改訂されてより分かりやすくなりました。特に、Microsoft Entra IDを使用した認証方法の導入により、認証プロセスが強化されています。これによりセキュリティも向上し、開発者がこれらのツールをより効率的に活用できるようになります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d84fb33...MicrosoftDocs:a68723c){target="_blank"}

# Highlights
この修正では、DALL·EおよびGPT-4 Turbo with Visionのクイックスタートガイドに関する大幅な更新と追加が行われました。特に、TypeScript SDKの新しいセクションが導入され、JavaScriptガイドもより簡潔で明確な内容に刷新されました。さらに、Microsoft Entra IDを利用した認証方法が新たに含まれ、認証プロセスが強化されています。

## New features
- **TypeScriptクイックスタートガイドの追加**：DALL·EおよびGPT-4 Turbo with Visionのための新しいTypeScriptガイドが提供されました。これにより、TypeScriptユーザーは特定の環境でのクイックスタートをより迅速に行うことが可能です。

## Breaking changes
- **認証方法の変更**：従来のAPIキーを使用した認証方式から、Microsoft Entra IDを用いたキーレス認証にシフトされました。これにより、よりセキュアで最新の認証手法が採用されています。

## Other updates
- **ガイドの更新と改善**：DALL·EとGPT-4 Turbo with VisionのJavaScriptガイドで、環境設定や認証方法に関する説明が改善され、開発者がより簡単に理解できるようになっています。また、新しいビジョン対応モデルに関する詳細が更新されています。

# Insights
今回の変更は、Azure OpenAIの機能をより多様な開発環境で効率的に利用できるようにすることを目的としています。TypeScriptユーザーへの対応を含め、プログラミング言語の多様性が強化されています。特に、Microsoft Entra IDによるキーレス認証方式の導入は、セキュリティの向上と共にAPIの利用の容易さを念頭に置いたものであり、現代的な開発ニーズへの対応を示しています。

ガイドの更新により、DALL·EやGPT-4 Turbo with Visionを利用する際のハードルが低くなることが期待され、新しいモデル機能の紹介も踏まえ、技術の最新情報を反映した内容となっています。これらの改善により、開発者はより直感的にAzure OpenAIのサービスを活用し、それをビジネスや個人プロジェクトで応用する際の準備が整うことでしょう。多様な使用シナリオに対応するための資料の充実は、開発者間のエコシステム強化に寄与します。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [dall-e-quickstart.md](#item-fcd528) | minor update | DALL·E クイックスタートに TypeScript SDK のセクションを追加 | modified | 6 | 0 | 6 | 
| [gpt-v-quickstart.md](#item-2a6183) | minor update | GPT-4 Turbo クイックスタートの内容を更新 | modified | 10 | 3 | 13 | 
| [dall-e-javascript.md](#item-6cffcf) | minor update | DALL·E JavaScript ガイドの内容を更新 | modified | 23 | 28 | 51 | 
| [dall-e-typescript.md](#item-57b205) | new feature | DALL·E TypeScript クイックスタートガイドの追加 | added | 207 | 0 | 207 | 
| [gpt-v-javascript.md](#item-a128c9) | minor update | GPT-4 Turbo with VisionモデルのJavaScriptガイドの更新 | modified | 24 | 35 | 59 | 
| [gpt-v-typescript.md](#item-03ec34) | new feature | GPT-4 Turbo with VisionのTypeScriptクイックスタートガイドの追加 | added | 256 | 0 | 256 | 


# Modified Contents
## articles/ai-services/openai/dall-e-quickstart.md{#item-fcd528}

<details>
<summary>Diff</summary>
````diff
@@ -54,6 +54,12 @@ zone_pivot_groups: openai-quickstart-dall-e
 
 ::: zone-end
 
+::: zone pivot="programming-language-typescript"
+
+[!INCLUDE [TypeScript SDK quickstart](includes/dall-e-typescript.md)]
+
+::: zone-end
+
 ::: zone pivot="programming-language-go"
 
 [!INCLUDE [Go SDK quickstart](includes/dall-e-go.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL·E クイックスタートに TypeScript SDK のセクションを追加"
}
```

### Explanation
この変更は、DALL·E のクイックスタートガイドに TypeScript SDK に関連する新しいセクションを追加するもので、合計で6行が追加されました。この追加によって、プログラミング言語として TypeScript を使用するユーザーに対して、DALL·E の利用方法をより具体的に説明する内容が含まれています。具体的には、TypeScript 用の SDK クイックスタートを含むためのコードスニペットが挿入され、他のプログラミング言語の情報と同様に、関連ドキュメントへの参照が組み込まれています。これにより、ユーザーはより多様な開発環境で DALL·E を活用するための情報にアクセスしやすくなります。

## articles/ai-services/openai/gpt-v-quickstart.md{#item-2a6183}

<details>
<summary>Diff</summary>
````diff
@@ -17,9 +17,10 @@ zone_pivot_groups: openai-quickstart-gpt-v
 
 Get started using GPT-4 Turbo with images with the Azure OpenAI Service.
 
-## GPT-4 Turbo model upgrade
-
-[!INCLUDE [GPT-4 Turbo](./includes/gpt-4-turbo.md)]
+> [!NOTE]
+> **Model choice**
+>
+> The latest vision-capable models are `gpt-4o` and `gpt-4o mini`. These are in public preview. The latest available GA model is `gpt-4` version `turbo-2024-04-09`.
 
 ::: zone pivot="programming-language-studio"
 
@@ -45,6 +46,12 @@ Get started using GPT-4 Turbo with images with the Azure OpenAI Service.
 
 ::: zone-end
 
+::: zone pivot="programming-language-typescript"
+
+[!INCLUDE [TypeScript quickstart](includes/gpt-v-typescript.md)]
+
+::: zone-end
+
 ::: zone pivot="programming-language-dotnet"
 
 [!INCLUDE [.NET quickstart](includes/gpt-v-dotnet.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turbo クイックスタートの内容を更新"
}
```

### Explanation
この変更は、GPT-4 Turbo クイックスタートガイドの内容を更新するもので、合計で10行が追加され、3行が削除されました。主な変更点としては、モデル選択に関する重要な情報が新たに追加され、最新のビジョン対応モデルである `gpt-4o` と `gpt-4o mini` の情報が含まれています。これらは現在パブリックプレビュー中であり、商用利用可能な最新のモデルである `gpt-4` のバージョンが示されています。また、TypeScript 用のクイックスタートを追加する新しいセクションも導入され、ユーザーが多様なプログラミング言語で GPT-4 Turbo を使用する方法に関して、より有用なリソースを提供しています。これにより、ユーザーは最新のモデルと使い方をより簡単に理解できるようになります。

## articles/ai-services/openai/includes/dall-e-javascript.md{#item-6cffcf}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-openai
 ms.topic: include
 author: PatrickFarley
 ms.author: pafarley
-ms.date: 09/06/2024
+ms.date: 10/23/2024
 ---
 
 Use this guide to get started generating images with the Azure OpenAI SDK for JavaScript.
@@ -17,22 +17,13 @@ Use this guide to get started generating images with the Azure OpenAI SDK for Ja
 
 ## Prerequisites
 
-#### [TypeScript](#tab/typescript)
 
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
-- [TypeScript](https://www.typescriptlang.org/download/)
+- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 
-#### [JavaScript](#tab/javascript)
-
-- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
-- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
-- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
-
----
-
 ## Setup
 
 [!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
@@ -62,15 +53,19 @@ Your app's _package.json_ file will be updated with the dependencies.
 
 Create a new file named _ImageGeneration.js_ and open it in your preferred code editor. Copy the following code into the _ImageGeneration.js_ file:
 
-#### [TypeScript](#tab/typescript)
 
-```typescript
-import "dotenv/config";
-import { AzureOpenAI } from "openai";
+
+#### [Microsoft Entra ID](#tab/javascript-keyless)
+
+```javascript
+const { AzureOpenAI } = require("openai");
+const { 
+    DefaultAzureCredential, 
+    getBearerTokenProvider 
+} = require("@azure/identity");
 
 // You will need to set these environment variables or edit the following values
 const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
-const apiKey = process.env["AZURE_OPENAI_API_KEY"];
 
 // Required Azure OpenAI deployment name and API version
 const apiVersion = "2024-07-01";
@@ -80,10 +75,15 @@ const deploymentName = "dall-e-3";
 const prompt = "a monkey eating a banana";
 const numberOfImagesToGenerate = 1;
 
+// keyless authentication    
+const credential = new DefaultAzureCredential();
+const scope = "https://cognitiveservices.azure.com/.default";
+const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+
 function getClient(): AzureOpenAI {
   return new AzureOpenAI({
     endpoint,
-    apiKey,
+    azureADTokenProvider,
     apiVersion,
     deployment: deploymentName,
   });
@@ -111,23 +111,17 @@ main().catch((err) => {
 });
 ```
 
-1. Build the application with the following command:
-
-    ```console
-    tsc
-    ```
+Run the script with the following command:
 
-1. Run the application with the following command:
+```console
+node ImageGeneration.js
+```
 
-    ```console
-    node ImageGeneration.js
-    ```
 
 
-#### [JavaScript](#tab/javascript)
+#### [API key](#tab/javascript-key)
 
 ```javascript
-require("dotenv/config");
 const { AzureOpenAI } = require("openai");
 
 // You will need to set these environment variables or edit the following values
@@ -178,6 +172,7 @@ Run the script with the following command:
 ```console
 node ImageGeneration.js
 ```
+
 ---
 
 ## Output
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL·E JavaScript ガイドの内容を更新"
}
```

### Explanation
この変更は、DALL·E JavaScript ガイドの内容を更新し、合計で23行が追加され、28行が削除され、51行の変更が行われました。主な変更点には、日付の更新や、必須条件のセクションの簡略化があります。TypeScript に関する記述が削除され、暗号化された認証方法として Microsoft Entra ID を使用する新しい手法が追加されました。

さらに、API キーを使用する方法が追加され、JavaScript コードの例も刷新されました。特に、環境変数の設定、Azure OpenAI 設定の管理、およびアプリケーションの実行に向けた具体的な手順が明確に示されています。これにより、開発者がJavaScriptを用いて Azure OpenAI を使用する際の手順が一層分かりやすくなり、最新の認証方法に基づいた実装が可能になります。

## articles/ai-services/openai/includes/dall-e-typescript.md{#item-57b205}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,207 @@
+---
+title: 'Quickstart: Use Azure OpenAI Service with the JavaScript SDK to generate images'
+titleSuffix: Azure OpenAI
+description: Walkthrough on how to get started with Azure OpenAI and make your first image generation call with the JavaScript SDK. 
+#services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+author: PatrickFarley
+ms.author: pafarley
+ms.date: 10/23/2024
+---
+
+Use this guide to get started generating images with the Azure OpenAI SDK for JavaScript.
+
+[Reference documentation](https://platform.openai.com/docs/api-reference/images/create) | [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
+
+## Prerequisites
+
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [TypeScript](https://www.typescriptlang.org/download/)
+- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
+- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+
+
+
+## Setup
+
+[!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
+
+[!INCLUDE [environment-variables](environment-variables.md)]
+
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
+## Generate images with DALL-E
+
+Create a new file named _ImageGeneration.ts_ and open it in your preferred code editor. Copy the following code into the _ImageGeneration.ts_ file:
+
+#### [Microsoft Entra ID](#tab/typescript-keyless)
+
+```typescript
+import { AzureOpenAI } from "openai";
+import { 
+    DefaultAzureCredential, 
+    getBearerTokenProvider 
+} from "@azure/identity";
+
+// You will need to set these environment variables or edit the following values
+const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
+
+// Required Azure OpenAI deployment name and API version
+const apiVersion = "2024-07-01";
+const deploymentName = "dall-e-3";
+
+// keyless authentication    
+const credential = new DefaultAzureCredential();
+const scope = "https://cognitiveservices.azure.com/.default";
+const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+
+function getClient(): AzureOpenAI {
+  return new AzureOpenAI({
+    endpoint,
+    azureADTokenProvider,
+    apiVersion,
+    deployment: deploymentName,
+  });
+}
+async function main() {
+  console.log("== Image Generation ==");
+
+  const client = getClient();
+
+  const results = await client.images.generate({
+    prompt,
+    size: "1024x1024",
+    n: numberOfImagesToGenerate,
+    model: "",
+    style: "vivid", // or "natural"
+  });
+
+  for (const image of results.data) {
+    console.log(`Image generation result URL: ${image.url}`);
+  }
+}
+
+main().catch((err) => {
+  console.error("The sample encountered an error:", err);
+});
+```
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
+    node ImageGeneration.js
+    ```
+
+#### [API key](#tab/typescript-key)
+
+```typescript
+import { AzureOpenAI } from "openai";
+
+// You will need to set these environment variables or edit the following values
+const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
+const apiKey = process.env["AZURE_OPENAI_API_KEY"];
+
+// Required Azure OpenAI deployment name and API version
+const apiVersion = "2024-07-01";
+const deploymentName = "dall-e-3";
+
+// The prompt to generate images from
+const prompt = "a monkey eating a banana";
+const numberOfImagesToGenerate = 1;
+
+function getClient(): AzureOpenAI {
+  return new AzureOpenAI({
+    endpoint,
+    apiKey,
+    apiVersion,
+    deployment: deploymentName,
+  });
+}
+async function main() {
+  console.log("== Image Generation ==");
+
+  const client = getClient();
+
+  const results = await client.images.generate({
+    prompt,
+    size: "1024x1024",
+    n: numberOfImagesToGenerate,
+    model: "",
+    style: "vivid", // or "natural"
+  });
+
+  for (const image of results.data) {
+    console.log(`Image generation result URL: ${image.url}`);
+  }
+}
+
+main().catch((err) => {
+  console.error("The sample encountered an error:", err);
+});
+```
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
+    node ImageGeneration.js
+    ```
+
+---
+
+## Output
+
+The URL of the generated image is printed to the console.
+
+```console
+== Batch Image Generation ==
+Image generation result URL: https://dalleproduse.blob.core.windows.net/private/images/5e7536a9-a0b5-4260-8769-2d54106f2913/generated_00.png?se=2023-08-29T19%3A12%3A57Z&sig=655GkWajOZ9ALjFykZF%2FBMZRPQALRhf4UPDImWCQoGI%3D&ske=2023-09-02T18%3A53%3A23Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2023-08-26T18%3A53%3A23Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02
+Image generation result URL: https://dalleproduse.blob.core.windows.net/private/images/5e7536a9-a0b5-4260-8769-2d54106f2913/generated_01.png?se=2023-08-29T19%3A12%3A57Z&sig=B24ymPLSZ3HfG23uojOD9VlRFGxjvgcNmvFo4yPUbEc%3D&ske=2023-09-02T18%3A53%3A23Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2023-08-26T18%3A53%3A23Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02
+```
+
+> [!NOTE]
+> The image generation APIs come with a content moderation filter. If the service recognizes your prompt as harmful content, it won't return a generated image. For more information, see the [content filter](../concepts/content-filter.md) article.
+
+## Clean up resources
+
+If you want to clean up and remove an Azure OpenAI resource, you can delete the resource. Before deleting the resource, you must first delete any deployed models.
+
+- [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
+- [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
+
+## Next steps
+
+* Explore the image generation APIs in more depth with the [DALL-E how-to guide](../how-to/dall-e.md).
+* For more examples check out the [Azure OpenAI Samples GitHub repository](https://github.com/Azure/openai-samples).
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "DALL·E TypeScript クイックスタートガイドの追加"
}
```

### Explanation
この変更は、DALL·EのTypeScriptクイックスタートガイドが新たに追加されたもので、207行のコードが含まれています。このガイドでは、Azure OpenAI SDKを用いてJavaScriptで画像を生成するための手順が解説されています。利用に必要な条件として、Azureのサブスクリプション、Node.jsのLTSバージョン、TypeScript、Azure CLIなどが挙げられています。

ガイドでは、Nodeアプリケーションの作成、クライアントライブラリのインストール、実際にDALL·Eを使って画像を生成する方法について詳細に説明されています。また、Microsoft Entra IDを利用したキーレス認証の方法やAPIキーを用いた方法が示されており、それぞれ異なる認証手段に対する具体的なコード例も提供されています。

最後に、生成された画像のURLがコンソールに出力され、クリーンアップ手順や次のステップを案内するセクションも含まれています。これにより、開発者はDALL·Eを使って画像生成に迅速に取り組めるようになることを目的としています。

## articles/ai-services/openai/includes/gpt-v-javascript.md{#item-a128c9}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 09/06/2024
+ms.date: 10/23/2024
 ---
 
 Use this article to get started using the OpenAI JavaScript SDK to deploy and use the GPT-4 Turbo with Vision model. 
@@ -18,18 +18,9 @@ This SDK is provided by OpenAI with Azure specific types provided by Azure.
 
 ## Prerequisites
 
-## [**TypeScript**](#tab/typescript)
-
-- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
-- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
-- [TypeScript](https://www.typescriptlang.org/download/)
-- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
-
-
-## [**JavaScript**](#tab/javascript)
-
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 ---
@@ -65,36 +56,40 @@ Your app's _package.json_ file will be updated with the dependencies.
 
 Select an image from the [azure-samples/cognitive-services-sample-data-files](https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images) and set the URL for an image in the environment variables.
 
-## [**TypeScript**](#tab/typescript)
 
-1. Create a _quickstart.ts_ and paste in the following code. 
-    
-    ```typescript
-    import "dotenv/config";
-    import { AzureOpenAI } from "openai";
-    import type {
-      ChatCompletion,
-      ChatCompletionCreateParamsNonStreaming,
-    } from "openai/resources/index";
+## [Microsoft Entra ID](#tab/javascript-keyless)
+
+1. Replace the contents of _quickstart.js_ with the following code. 
     
+    ```javascript
+    const AzureOpenAI = require('openai').AzureOpenAI;
+    const { 
+        DefaultAzureCredential, 
+        getBearerTokenProvider 
+    } = require('@azure/identity');
+
     // You will need to set these environment variables or edit the following values
     const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
-    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
     const imageUrl = process.env["IMAGE_URL"] || "<image url>";
     
     // Required Azure OpenAI deployment name and API version
     const apiVersion = "2024-07-01-preview";
     const deploymentName = "gpt-4-with-turbo";
     
+    // keyless authentication    
+    const credential = new DefaultAzureCredential();
+    const scope = "https://cognitiveservices.azure.com/.default";
+    const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+
     function getClient(): AzureOpenAI {
       return new AzureOpenAI({
         endpoint,
-        apiKey,
+        azureADTokenProvider,
         apiVersion,
         deployment: deploymentName,
       });
     }
-    function createMessages(): ChatCompletionCreateParamsNonStreaming {
+    function createMessages() {
       return {
         messages: [
           { role: "system", content: "You are a helpful assistant." },
@@ -118,7 +113,7 @@ Select an image from the [azure-samples/cognitive-services-sample-data-files](ht
         max_tokens: 2000,
       };
     }
-    async function printChoices(completion: ChatCompletion): Promise<void> {
+    async function printChoices(completion) {
       for (const choice of completion.choices) {
         console.log(choice.message);
       }
@@ -136,32 +131,26 @@ Select an image from the [azure-samples/cognitive-services-sample-data-files](ht
       console.error("Error occurred:", err);
     });
     ```
+
 1. Make the following changes:
     1. Enter the name of your GPT-4 Turbo with Vision deployment in the appropriate field.
     1. Change the value of the `"url"` field to the URL of your image.
         > [!TIP]
         > You can also use a base 64 encoded image data instead of a URL. For more information, see the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-a-local-image).
-
-1. Build the application with the following command:
-
-    ```console
-    tsc
-    ```
-
 1. Run the application with the following command:
 
     ```console
     node quickstart.js
     ```
 
 
-## [**JavaScript**](#tab/javascript)
+
+## [API key](#tab/javascript-key)
 
 1. Replace the contents of _quickstart.js_ with the following code. 
     
     ```javascript
-    import "dotenv/config";
-    import { AzureOpenAI } from "openai";
+    const { AzureOpenAI } = require("openai");
     
     // You will need to set these environment variables or edit the following values
     const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turbo with VisionモデルのJavaScriptガイドの更新"
}
```

### Explanation
この変更は、GPT-4 Turbo with Visionモジュールに関するJavaScriptガイドを更新し、合計で24行が追加され、35行が削除され、59行の変更が行われました。主な更新内容には、日付の変更や、前提条件セクションの簡素化が含まれています。特に、TypeScriptからJavaScriptに焦点を当てた新しいセクションが導入され、Microsoft Entra IDを用いたキーレス認証方法が追加されました。

従来のAPIキーを用いた認証方法は削除され、新しく追加されたコード例は、ジャバスクリプト環境における認証手法を明確に示しています。さらに、画像生成に関するプロセスや、環境変数の設定方法について具体的な手順が記載されており、開発者がこのモデルを使用する際の理解を深めることができる内容となっています。また、生成されたメッセージをコンソールに出力するための機能や、URL以外にBase64エンコードされた画像データの使用に関するヒントも提供されています。この更新により、開発者がより容易にGPT-4 Turbo with Visionモデルを活用できるようになります。

## articles/ai-services/openai/includes/gpt-v-typescript.md{#item-03ec34}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,256 @@
+---
+title: 'Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the JavaScript SDK'
+titleSuffix: Azure OpenAI
+description: Get started using the OpenAI JavaScript SDK to deploy and use the GPT-4 Turbo with Vision model.
+services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.custom: references_regions
+ms.date: 10/23/2024
+---
+
+Use this article to get started using the OpenAI JavaScript SDK to deploy and use the GPT-4 Turbo with Vision model. 
+
+This SDK is provided by OpenAI with Azure specific types provided by Azure. 
+
+[Reference documentation](https://platform.openai.com/docs/api-reference/chat) | [Library source code](https://github.com/openai/openai-node?azure-portal=true) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
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
+> [!NOTE]
+> This library is maintained by OpenAI. Refer to the [release history](https://github.com/openai/openai-node/releases) to track the latest updates to the library.
+
+[!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
+
+[!INCLUDE [environment-variables](environment-variables.md)]
+
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
+## Create a new JavaScript application for image prompts
+
+Select an image from the [azure-samples/cognitive-services-sample-data-files](https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images) and set the URL for an image in the environment variables.
+
+
+## [Microsoft Entra ID](#tab/typescript-keyless)
+
+1. Create a _quickstart.ts_ and paste in the following code. 
+    
+    ```typescript
+    import { AzureOpenAI } from "openai";
+    import { 
+        DefaultAzureCredential, 
+        getBearerTokenProvider 
+    } from "@azure/identity";
+    import type {
+      ChatCompletion,
+      ChatCompletionCreateParamsNonStreaming,
+    } from "openai/resources/index";
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const imageUrl = process.env["IMAGE_URL"] || "<image url>";
+    
+    // Required Azure OpenAI deployment name and API version
+    const apiVersion = "2024-07-01-preview";
+    const deploymentName = "gpt-4-with-turbo";
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
+    function createMessages(): ChatCompletionCreateParamsNonStreaming {
+      return {
+        messages: [
+          { role: "system", content: "You are a helpful assistant." },
+          {
+            role: "user",
+            content: [
+              {
+                type: "text",
+                text: "Describe this picture:",
+              },
+              {
+                type: "image_url",
+                image_url: {
+                  url: imageUrl,
+                },
+              },
+            ],
+          },
+        ],
+        model: "",
+        max_tokens: 2000,
+      };
+    }
+    async function printChoices(completion: ChatCompletion): Promise<void> {
+      for (const choice of completion.choices) {
+        console.log(choice.message);
+      }
+    }
+    export async function main() {
+      console.log("== Get GPT-4 Turbo with vision Sample ==");
+    
+      const client = getClient();
+      const messages = createMessages();
+      const completion = await client.chat.completions.create(messages);
+      await printChoices(completion);
+    }
+    
+    main().catch((err) => {
+      console.error("Error occurred:", err);
+    });
+    ```
+1. Make the following changes:
+    1. Enter the name of your GPT-4 Turbo with Vision deployment in the appropriate field.
+    1. Change the value of the `"url"` field to the URL of your image.
+        > [!TIP]
+        > You can also use a base 64 encoded image data instead of a URL. For more information, see the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-a-local-image).
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
+    node quickstart.js
+    ```
+
+
+
+## [API key](#tab/typescript-key)
+
+1. Create a _quickstart.ts_ and paste in the following code. 
+    
+    ```typescript
+    import { AzureOpenAI } from "openai";
+    import type {
+      ChatCompletion,
+      ChatCompletionCreateParamsNonStreaming,
+    } from "openai/resources/index";
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+    const imageUrl = process.env["IMAGE_URL"] || "<image url>";
+    
+    // Required Azure OpenAI deployment name and API version
+    const apiVersion = "2024-07-01-preview";
+    const deploymentName = "gpt-4-with-turbo";
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    function createMessages(): ChatCompletionCreateParamsNonStreaming {
+      return {
+        messages: [
+          { role: "system", content: "You are a helpful assistant." },
+          {
+            role: "user",
+            content: [
+              {
+                type: "text",
+                text: "Describe this picture:",
+              },
+              {
+                type: "image_url",
+                image_url: {
+                  url: imageUrl,
+                },
+              },
+            ],
+          },
+        ],
+        model: "",
+        max_tokens: 2000,
+      };
+    }
+    async function printChoices(completion: ChatCompletion): Promise<void> {
+      for (const choice of completion.choices) {
+        console.log(choice.message);
+      }
+    }
+    export async function main() {
+      console.log("== Get GPT-4 Turbo with vision Sample ==");
+    
+      const client = getClient();
+      const messages = createMessages();
+      const completion = await client.chat.completions.create(messages);
+      await printChoices(completion);
+    }
+    
+    main().catch((err) => {
+      console.error("Error occurred:", err);
+    });
+    ```
+1. Make the following changes:
+    1. Enter the name of your GPT-4 Turbo with Vision deployment in the appropriate field.
+    1. Change the value of the `"url"` field to the URL of your image.
+        > [!TIP]
+        > You can also use a base 64 encoded image data instead of a URL. For more information, see the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-a-local-image).
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
+    node quickstart.js
+    ```
+
+
+
+---
+
+## Clean up resources
+
+If you want to clean up and remove an Azure OpenAI resource, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
+
+- [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
+- [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
+
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "GPT-4 Turbo with VisionのTypeScriptクイックスタートガイドの追加"
}
```

### Explanation
この変更は、GPT-4 Turbo with Visionモデルを使用するためのTypeScriptクイックスタートガイドが新たに追加されたもので、256行のコードが含まれています。この記事は、OpenAIのJavaScript SDKを使って画像や動画に対してGPT-4 Turbo with Visionモデルを導入し、利用する方法を示しています。

ガイドには、必要な前提条件として、Azureのサブスクリプション、LTSバージョンのNode.js、TypeScript、Azure CLIなどが含まれており、これらの環境を整えるためのリンクが提供されています。さらに、Microsoft Entra IDを用いたキーレス認証の方法が説明されており、環境変数のセットアップも指示されています。

次に、Nodeアプリケーションの作成、クライアントライブラリのインストール、画像プロンプトの新しいJavaScriptアプリケーションの構築に関する具体的な手順が示されています。コード例が含まれ、GPT-4 Turbo with Visionモデルに画像を渡し、その説明を得るための仕組みが詳述されています。すなわち、ユーザーが画像を指定し、その画像に関する説明を生成する一連のプロセスが手順として説明されています。

最後に、リソースのクリーンアップ方法についても言及されており、Azure OpenAIリソースまたはリソースグループを削除する方法が記載されています。これにより、開発者はGPT-4 Turbo with Visionモデルを迅速かつ効果的に利用開始できるようになります。


