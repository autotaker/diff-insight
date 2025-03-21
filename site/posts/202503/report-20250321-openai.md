---
date: '2025-03-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:17e9a85...MicrosoftDocs:34ecec7
summary: このコード差分では、主に日付情報の更新やクライアントライブラリの新機能追加、TypeScriptコードの大幅な変更が行われています。新機能としては、JavaScriptクライアントライブラリのリアルタイムオーディオ処理方法が導入され、TypeScriptでは互換性のない変更が加えられました。また、日付情報の更新やAPIバージョン情報のアップデートも行われ、文書の正確性が保たれています。これらの変更は、ユーザビリティの向上と開発者が直感的に操作できるライブラリ利用方法の提供を目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:17e9a85...MicrosoftDocs:34ecec7){target="_blank"}

<format>
# ハイライト
このコード差分では、主に日付情報の更新、クライアントライブラリの新機能追加、およびTypeScriptコードの大幅な変更が行われています。新機能として、JavaScriptクライアントライブラリでの新しいリアルタイムオーディオ処理方法が追加され、TypeScriptでは互換性のない変更が導入されています。

## 新機能
- リアルタイムJavaScriptクライアントライブラリの大幅な更新で、新しいAPIの使用方針が導入されました。
- 各種イベントリスナーの追加により、リアルタイムでの応答処理がより強化されました。

## Breaking changes
- TypeScriptコードで「OpenAI client」への移行が行われ、旧版との互換性が失われました。
- 主要関数の再編成により、コードの使用方法が変更されています。

## その他の更新
- 複数の文書で日付情報が最新版に更新され、正確な情報提供を担保しています。
- APIバージョン情報が更新され、最新のリクエストURIに対応しています。

# インサイト
このコードの変更は、主にユーザビリティ向上と最新情報の正確な反映を目的としています。なかでもJavaScriptクライアントライブラリの更新は、開発者がより直感的にOpenAIのリアルタイムAPIを操作できるようにするもので、直感性と効率性を兼ね備えた新しいライブラリ利用方法が提供されています。さらに、更新されたTypeScriptセクションでは、コードの再構築による明確さの向上と、新しいWebSocketによるリアルタイム通信処理の追加があり、これらは今後の開発において重要な変更と考えられます。

一方、日付やAPIバージョン情報の更新は、主に文書の正確性を保持するためのものであり、これらの小さな変更は信頼性向上に寄与しています。大幅な変更と小規模な更新が混在するこの差分は、OpenAIのリアルタイムAPIを利用する開発者にとって、今後のプロジェクトで必須の情報を提供しています。適切なドキュメンテーションと例示されたコードは、迅速な適応を可能にし、開発者の利便性を最大化します。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [realtime-audio.md](#item-482ba3) | minor update | 更新された日付情報の修正 | modified | 1 | 1 | 2 | 
| [realtime-javascript.md](#item-3c125e) | new feature | リアルタイムJavaScriptクライアントライブラリの更新 | modified | 136 | 107 | 243 | 
| [realtime-portal.md](#item-1b81a2) | minor update | 日付情報の更新 | modified | 1 | 1 | 2 | 
| [realtime-python.md](#item-1291c0) | minor update | 日付情報の更新 | modified | 1 | 1 | 2 | 
| [realtime-typescript.md](#item-eacc9c) | breaking change | TypeScript コードの大幅な更新 | modified | 150 | 116 | 266 | 
| [realtime-audio-quickstart.md](#item-727df8) | minor update | ドキュメントのバージョン情報の更新 | modified | 2 | 2 | 4 | 
| [realtime-audio-reference.md](#item-276d51) | minor update | APIバージョン情報の修正 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/ai-services/openai/how-to/realtime-audio.md{#item-482ba3}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use the GPT-4o Realtime API for speech and audio with
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 12/20/2024
+ms.date: 3/20/2025
 author: eric-urban
 ms.author: eur
 ms.custom: references_regions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新された日付情報の修正"
}
```

### Explanation
この変更では、`realtime-audio.md`ファイルのメタデータにある日付情報が更新されました。具体的には、以前の更新日が「2024年12月20日」から「2025年3月20日」に変更され、ファイル全体の内容に重要なタイムスタンプの最新化が反映されています。この修正は、記事が最新の情報を提供していることを保証するための重要なマイナーアップデートです。変更は1行の追加と1行の削除で構成されており、全体で2つの変更が行われています。これにより、文書の正確性と信頼性が向上します。

## articles/ai-services/openai/includes/realtime-javascript.md{#item-3c125e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 1/21/2025
+ms.date: 3/20/2025
 ---
 
 ## Prerequisites
@@ -38,10 +38,10 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     npm init -y
     ```
 
-1. Install the real-time audio client library for JavaScript with:
+1. Install the OpenAI client library for JavaScript with:
 
     ```console
-    npm install https://github.com/Azure-Samples/aoai-realtime-audio-sdk/releases/download/js/v0.5.2/rt-client-0.5.2.tgz
+    npm install openai
     ```
 
 1. For the **recommended** keyless authentication with Microsoft Entra ID, install the `@azure/identity` package with:
@@ -50,6 +50,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     npm install @azure/identity
     ```
 
+
 ## Retrieve resource information
 
 [!INCLUDE [resource authentication](resource-authentication.md)]
@@ -64,55 +65,70 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create the `index.js` file with the following code:
 
     ```javascript 
-    import { DefaultAzureCredential } from "@azure/identity";
-    import { LowLevelRTClient } from "rt-client";
-    import dotenv from "dotenv";
-    dotenv.config();
-    async function text_in_audio_out() {
-        // Set environment variables or edit the corresponding values here.
-        const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "YourEndpoint";
-        const deployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini-realtime-preview";
-        if (!endpoint || !deployment) {
-            throw new Error("You didn't set the environment variables.");
-        }
-        const client = new LowLevelRTClient(new URL(endpoint), new DefaultAzureCredential(), { deployment: deployment });
-        try {
-            await client.send({
-                type: "response.create",
-                response: {
-                    modalities: ["audio", "text"],
-                    instructions: "Please assist the user."
-                }
+    import { OpenAIRealtimeWS } from "openai/beta/realtime/ws";
+    import { AzureOpenAI } from "openai/index.mjs";
+    import { DefaultAzureCredential, getBearerTokenProvider } from "@azure/identity";
+    async function main() {
+        // You will need to set these environment variables or edit the following values
+        const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
+        // Required Azure OpenAI deployment name and API version
+        const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini-realtime-preview";
+        const apiVersion = process.env.OPENAI_API_VERSION || "2024-10-01-preview";
+        // Keyless authentication 
+        const credential = new DefaultAzureCredential();
+        const scope = "https://cognitiveservices.azure.com/.default";
+        const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+        const azureOpenAIClient = new AzureOpenAI({
+            azureADTokenProvider,
+            apiVersion: apiVersion,
+            deployment: deploymentName,
+            endpoint: endpoint,
+        });
+        const realtimeClient = await OpenAIRealtimeWS.azure(azureOpenAIClient);
+        realtimeClient.socket.on("open", () => {
+            console.log("Connection opened!");
+            realtimeClient.send({
+                type: "session.update",
+                session: {
+                    modalities: ["text", "audio"],
+                    model: "gpt-4o-mini-realtime-preview",
+                },
+            });
+            realtimeClient.send({
+                type: "conversation.item.create",
+                item: {
+                    type: "message",
+                    role: "user",
+                    content: [{ type: "input_text", text: "Please assist the user" }],
+                },
             });
-            for await (const message of client.messages()) {
-                switch (message.type) {
-                    case "response.done": {
-                        break;
-                    }
-                    case "error": {
-                        console.error(message.error);
-                        break;
-                    }
-                    case "response.audio_transcript.delta": {
-                        console.log(`Received text delta: ${message.delta}`);
-                        break;
-                    }
-                    case "response.audio.delta": {
-                        const buffer = Buffer.from(message.delta, "base64");
-                        console.log(`Received ${buffer.length} bytes of audio data.`);
-                        break;
-                    }
-                }
-                if (message.type === "response.done" || message.type === "error") {
-                    break;
-                }
-            }
-        }
-        finally {
-            client.close();
-        }
+            realtimeClient.send({ type: "response.create" });
+        });
+        realtimeClient.on("error", (err) => {
+            // Instead of throwing the error, you can log it
+            // and continue processing events.
+            throw err;
+        });
+        realtimeClient.on("session.created", (event) => {
+            console.log("session created!", event.session);
+            console.log();
+        });
+        realtimeClient.on("response.text.delta", (event) => process.stdout.write(event.delta));
+        realtimeClient.on("response.audio.delta", (event) => {
+            const buffer = Buffer.from(event.delta, "base64");
+            console.log(`Received ${buffer.length} bytes of audio data.`);
+        });
+        realtimeClient.on("response.audio_transcript.delta", (event) => {
+            console.log(`Received text delta:${event.delta}.`);
+        });
+        realtimeClient.on("response.text.done", () => console.log());
+        realtimeClient.on("response.done", () => realtimeClient.close());
+        realtimeClient.socket.on("close", () => console.log("\nConnection closed!"));
     }
-    await text_in_audio_out();
+    main().catch((err) => {
+        console.error("The sample encountered an error:", err);
+    });
+    export { main };
     ```
 
 1. Sign in to Azure with the following command:
@@ -132,56 +148,66 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create the `index.js` file with the following code:
 
     ```javascript 
-    import { AzureKeyCredential } from "@azure/core-auth";
-    import { LowLevelRTClient } from "rt-client";
-    import dotenv from "dotenv";
-    dotenv.config();
-    async function text_in_audio_out() {
-        // Set environment variables or edit the corresponding values here.
+    import { OpenAIRealtimeWS } from "openai/beta/realtime/ws";
+    import { AzureOpenAI } from "openai/index.mjs";
+    async function main() {
+        // You will need to set these environment variables or edit the following values
+        const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
         const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
-        const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
-        const deployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini-realtime-preview";
-        if (!endpoint || !deployment) {
-            throw new Error("You didn't set the environment variables.");
-        }
-        const client = new LowLevelRTClient(new URL(endpoint), new AzureKeyCredential(apiKey), { deployment: deployment });
-        try {
-            await client.send({
-                type: "response.create",
-                response: {
-                    modalities: ["audio", "text"],
-                    instructions: "Please assist the user."
-                }
+        // Required Azure OpenAI deployment name and API version
+        const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini-realtime-preview";
+        const apiVersion = process.env.OPENAI_API_VERSION || "2024-10-01-preview";
+        const azureOpenAIClient = new AzureOpenAI({
+            apiKey: apiKey,
+            apiVersion: apiVersion,
+            deployment: deploymentName,
+            endpoint: endpoint,
+        });
+        const realtimeClient = await OpenAIRealtimeWS.azure(azureOpenAIClient);
+        realtimeClient.socket.on("open", () => {
+            console.log("Connection opened!");
+            realtimeClient.send({
+                type: "session.update",
+                session: {
+                    modalities: ["text", "audio"],
+                    model: "gpt-4o-mini-realtime-preview",
+                },
             });
-            for await (const message of client.messages()) {
-                switch (message.type) {
-                    case "response.done": {
-                        break;
-                    }
-                    case "error": {
-                        console.error(message.error);
-                        break;
-                    }
-                    case "response.audio_transcript.delta": {
-                        console.log(`Received text delta: ${message.delta}`);
-                        break;
-                    }
-                    case "response.audio.delta": {
-                        const buffer = Buffer.from(message.delta, "base64");
-                        console.log(`Received ${buffer.length} bytes of audio data.`);
-                        break;
-                    }
-                }
-                if (message.type === "response.done" || message.type === "error") {
-                    break;
-                }
-            }
-        }
-        finally {
-            client.close();
-        }
+            realtimeClient.send({
+                type: "conversation.item.create",
+                item: {
+                    type: "message",
+                    role: "user",
+                    content: [{ type: "input_text", text: "Please assist the user" }],
+                },
+            });
+            realtimeClient.send({ type: "response.create" });
+        });
+        realtimeClient.on("error", (err) => {
+            // Instead of throwing the error, you can log it
+            // and continue processing events.
+            throw err;
+        });
+        realtimeClient.on("session.created", (event) => {
+            console.log("session created!", event.session);
+            console.log();
+        });
+        realtimeClient.on("response.text.delta", (event) => process.stdout.write(event.delta));
+        realtimeClient.on("response.audio.delta", (event) => {
+            const buffer = Buffer.from(event.delta, "base64");
+            console.log(`Received ${buffer.length} bytes of audio data.`);
+        });
+        realtimeClient.on("response.audio_transcript.delta", (event) => {
+            console.log(`Received text delta:${event.delta}.`);
+        });
+        realtimeClient.on("response.text.done", () => console.log());
+        realtimeClient.on("response.done", () => realtimeClient.close());
+        realtimeClient.socket.on("close", () => console.log("\nConnection closed!"));
     }
-    await text_in_audio_out();
+    main().catch((err) => {
+        console.error("The sample encountered an error:", err);
+    });
+    export { main };
     ```
 
 1. Run the JavaScript file.
@@ -201,22 +227,25 @@ The script gets a response from the model and prints the transcript and audio da
 The output will look similar to the following:
 
 ```console
-Received text delta: Hello
-Received text delta: !
-Received text delta:  How
-Received text delta:  can
-Received text delta:  I
+Received text delta:Of.
+Received text delta: course.
+Received text delta:!.
+Received text delta: How.
+Received text delta: can.
 Received 4800 bytes of audio data.
 Received 7200 bytes of audio data.
-Received text delta:  help
+Received text delta: I.
 Received 12000 bytes of audio data.
-Received text delta:  you
-Received text delta:  today
-Received text delta: ?
+Received text delta: help.
+Received text delta: you.
+Received text delta: today.
+Received text delta:?.
 Received 12000 bytes of audio data.
 Received 12000 bytes of audio data.
 Received 12000 bytes of audio data.
-Received 24000 bytes of audio data.
+Received 26400 bytes of audio data.
+
+Connection closed!
 ```
 
 ## Web application sample
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "リアルタイムJavaScriptクライアントライブラリの更新"
}
```

### Explanation
この変更では、`realtime-javascript.md`ファイルに大幅な改訂が行われ、リアルタイムオーディオのクライアントライブラリの使い方が更新されました。特に、OpenAIクライアントライブラリを使用する方法に変更され、これに伴い多くの新しい機能が追加されました。

具体的には、以下のポイントが含まれています：
- 古いライブラリから新しい`OpenAIRealtimeWS`および`AzureOpenAI`を使用するようにコードが移行され、より直感的で効率的な方式でリアルタイムオーディオ処理が可能になります。
- 日付情報が更新され、記事は最新のAPI情報に基づいています。
- 環境変数の管理とエラーハンドリングが改善され、ユーザーにとってより使いやすい構成になっています。
- 各種のイベントリスナーが追加され、リアルタイムでの応答処理が強化されています。

これにより、開発者はJavaScriptを使用してOpenAIのリアルタイムAPIとよりスムーズに相互作用できるようになり、全体的なユーザー体験が向上しています。変更は実質的に243行に及ぶもので、追加136行、削除107行が反映されています。

## articles/ai-services/openai/includes/realtime-portal.md{#item-1b81a2}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 1/21/2025
+ms.date: 3/20/2025
 ---
 
 ## Deploy a model for real-time audio
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付情報の更新"
}
```

### Explanation
この変更では、`realtime-portal.md`ファイルの日付情報が更新されました。具体的には、記事の更新日が「2025年1月21日」から「2025年3月20日」に変更されています。この更新は記事の内容が最新であることを反映し、ユーザーに正確な情報を提供するために重要です。変更の規模は小さく、追加が1行、削除が1行の合計2行の変更です。このようなマイナーアップデートは、文書の信頼性を保つために重要です。

## articles/ai-services/openai/includes/realtime-python.md{#item-1291c0}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 1/21/2025
+ms.date: 3/20/2025
 ---
 
 ## Prerequisites
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付情報の更新"
}
```

### Explanation
この変更は、`realtime-python.md`ファイルに対するもので、文書の日付情報が更新されています。具体的には、前回の更新日が「2025年1月21日」から「2025年3月20日」へと変更されました。このマイナーアップデートは、ユーザーに最新の情報を提供するために重要です。全体的な変更はわずか2行で、1行の追加と1行の削除が含まれています。このような更新は、ドキュメントの正確性と信頼性を維持するための重要なステップです。

## articles/ai-services/openai/includes/realtime-typescript.md{#item-eacc9c}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 1/21/2025
+ms.date: 3/20/2025
 ---
 
 ## Prerequisites
@@ -46,10 +46,10 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     npm pkg set type=module
     ```
     
-1. Install the real-time audio client library for JavaScript with:
+1. Install the OpenAI client library for JavaScript with:
 
     ```console
-    npm install https://github.com/Azure-Samples/aoai-realtime-audio-sdk/releases/download/js/v0.5.2/rt-client-0.5.2.tgz
+    npm install openai
     ```
 
 1. For the **recommended** keyless authentication with Microsoft Entra ID, install the `@azure/identity` package with:
@@ -58,6 +58,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     npm install @azure/identity
     ```
 
+
 ## Retrieve resource information
 
 [!INCLUDE [resource authentication](resource-authentication.md)]
@@ -72,61 +73,79 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create the `index.ts` file with the following code:
 
     ```typescript
-    import { DefaultAzureCredential } from "@azure/identity";
-    import { LowLevelRTClient } from "rt-client";
-    import dotenv from "dotenv";
-    dotenv.config();
+    import { OpenAIRealtimeWS } from "openai/beta/realtime/ws";
+    import { AzureOpenAI } from "openai/index.mjs";
+    import { DefaultAzureCredential, getBearerTokenProvider } from "@azure/identity";
     
-    async function text_in_audio_out() {
-        // Set environment variables or edit the corresponding values here.
-        const endpoint: string = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
-        const deployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini-realtime-preview";
-        if (!endpoint || !deployment) {
-            throw new Error("You didn't set the environment variables.");
-        }
-        const client = new LowLevelRTClient(
-            new URL(endpoint), 
-            new DefaultAzureCredential(), 
-            {deployment: deployment}
-        );
-        try {
-            await client.send({
-                type: "response.create",
-                response: {
-                    modalities: ["audio", "text"],
-                    instructions: "Please assist the user."
-                }
-            });
+    async function main(): Promise<void> {
+    
+        // You will need to set these environment variables or edit the following values
+        const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
+        
+        // Required Azure OpenAI deployment name and API version
+        const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini-realtime-preview";
+        const apiVersion = process.env.OPENAI_API_VERSION || "2024-10-01-preview"; 
+    
+        // Keyless authentication 
+        const credential = new DefaultAzureCredential();
+        const scope = "https://cognitiveservices.azure.com/.default";
+        const azureADTokenProvider = getBearerTokenProvider(credential, scope);
     
-            for await (const message of client.messages()) {
-                switch (message.type) {
-                    case "response.done": {
-                        break;
-                    }
-                    case "error": {
-                        console.error(message.error);
-                        break;
-                    }
-                    case "response.audio_transcript.delta": {
-                        console.log(`Received text delta: ${message.delta}`);
-                        break;
-                    }
-                    case "response.audio.delta": {
-                        const buffer = Buffer.from(message.delta, "base64");
-                        console.log(`Received ${buffer.length} bytes of audio data.`);
-                        break;
-                    }
-                }
-                if (message.type === "response.done" || message.type === "error") {
-                    break;
-                }
-            }
-        } finally {
-            client.close();
-        }
+        const azureOpenAIClient = new AzureOpenAI({
+            azureADTokenProvider,
+            apiVersion: apiVersion,
+            deployment: deploymentName,
+            endpoint: endpoint,
+        });
+    
+        const realtimeClient = await OpenAIRealtimeWS.azure(azureOpenAIClient);
+    
+        realtimeClient.socket.on("open", () => {
+            console.log("Connection opened!");
+            realtimeClient.send({
+            type: "session.update",
+            session: {
+                modalities: ["text", "audio"],
+                model: "gpt-4o-mini-realtime-preview",
+            },
+            });
+            realtimeClient.send({
+            type: "conversation.item.create",
+            item: {
+                type: "message",
+                role: "user",
+                content: [{ type: "input_text", text: "Please assist the user" }],
+            },
+            });
+            realtimeClient.send({ type: "response.create" });
+        });
+        realtimeClient.on("error", (err) => {
+            // Instead of throwing the error, you can log it
+            // and continue processing events.
+            throw err;
+        });
+        realtimeClient.on("session.created", (event) => {
+            console.log("session created!", event.session);
+            console.log();
+        });
+        realtimeClient.on("response.text.delta", (event) => process.stdout.write(event.delta));
+        realtimeClient.on("response.audio.delta", (event) => {
+            const buffer = Buffer.from(event.delta, "base64");
+            console.log(`Received ${buffer.length} bytes of audio data.`);
+        });
+        realtimeClient.on("response.audio_transcript.delta", (event) => {
+            console.log(`Received text delta:${event.delta}.`);
+        });
+        realtimeClient.on("response.text.done", () => console.log());
+        realtimeClient.on("response.done", () => realtimeClient.close());
+        realtimeClient.socket.on("close", () => console.log("\nConnection closed!"));
     }
     
-    await text_in_audio_out();
+    main().catch((err) => {
+        console.error("The sample encountered an error:", err);
+    });
+    
+    export { main };
     ```
 
 1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
@@ -167,62 +186,74 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create the `index.ts` file with the following code:
 
     ```typescript
-    import { AzureKeyCredential } from "@azure/core-auth";
-    import { LowLevelRTClient } from "rt-client";
-    import dotenv from "dotenv";
-    dotenv.config();
+    import { OpenAIRealtimeWS } from "openai/beta/realtime/ws";
+    import { AzureOpenAI } from "openai/index.mjs";
     
-    async function text_in_audio_out() {
-        // Set environment variables or edit the corresponding values here.
-        const apiKey: string = process.env.AZURE_OPENAI_API_KEY || "Your API key";
-        const endpoint: string = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
-        const deployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini-realtime-preview";
-        if (!endpoint || !deployment) {
-            throw new Error("You didn't set the environment variables.");
-        }
-        const client = new LowLevelRTClient(
-            new URL(endpoint), 
-            new AzureKeyCredential(apiKey),
-            {deployment: deployment}
-        );
-        try {
-            await client.send({
-                type: "response.create",
-                response: {
-                    modalities: ["audio", "text"],
-                    instructions: "Please assist the user."
-                }
-            });
+    async function main(): Promise<void> {
+    
+        // You will need to set these environment variables or edit the following values
+        const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "AZURE_OPENAI_ENDPOINT";
+        const apiKey = process.env.AZURE_OPENAI_API_KEY || "Your API key";
+        
+        // Required Azure OpenAI deployment name and API version
+        const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT_NAME || "gpt-4o-mini-realtime-preview";
+        const apiVersion = process.env.OPENAI_API_VERSION || "2024-10-01-preview"; 
+        
+        const azureOpenAIClient = new AzureOpenAI({
+            apiKey: apiKey,
+            apiVersion: apiVersion,
+            deployment: deploymentName,
+            endpoint: endpoint,
+        });
+    
+        const realtimeClient = await OpenAIRealtimeWS.azure(azureOpenAIClient);
     
-            for await (const message of client.messages()) {
-                switch (message.type) {
-                    case "response.done": {
-                        break;
-                    }
-                    case "error": {
-                        console.error(message.error);
-                        break;
-                    }
-                    case "response.audio_transcript.delta": {
-                        console.log(`Received text delta: ${message.delta}`);
-                        break;
-                    }
-                    case "response.audio.delta": {
-                        const buffer = Buffer.from(message.delta, "base64");
-                        console.log(`Received ${buffer.length} bytes of audio data.`);
-                        break;
-                    }
-                }
-                if (message.type === "response.done" || message.type === "error") {
-                    break;
-                }
-            }
-        } finally {
-            client.close();
-        }
+        realtimeClient.socket.on("open", () => {
+            console.log("Connection opened!");
+            realtimeClient.send({
+            type: "session.update",
+            session: {
+                modalities: ["text", "audio"],
+                model: "gpt-4o-mini-realtime-preview",
+            },
+            });
+            realtimeClient.send({
+            type: "conversation.item.create",
+            item: {
+                type: "message",
+                role: "user",
+                content: [{ type: "input_text", text: "Please assist the user" }],
+            },
+            });
+            realtimeClient.send({ type: "response.create" });
+        });
+        realtimeClient.on("error", (err) => {
+            // Instead of throwing the error, you can log it
+            // and continue processing events.
+            throw err;
+        });
+        realtimeClient.on("session.created", (event) => {
+            console.log("session created!", event.session);
+            console.log();
+        });
+        realtimeClient.on("response.text.delta", (event) => process.stdout.write(event.delta));
+        realtimeClient.on("response.audio.delta", (event) => {
+            const buffer = Buffer.from(event.delta, "base64");
+            console.log(`Received ${buffer.length} bytes of audio data.`);
+        });
+        realtimeClient.on("response.audio_transcript.delta", (event) => {
+            console.log(`Received text delta:${event.delta}.`);
+        });
+        realtimeClient.on("response.text.done", () => console.log());
+        realtimeClient.on("response.done", () => realtimeClient.close());
+        realtimeClient.socket.on("close", () => console.log("\nConnection closed!"));
     }
     
-    await text_in_audio_out();
+    main().catch((err) => {
+        console.error("The sample encountered an error:", err);
+    });
+    
+    export { main };
     ```
 
 1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
@@ -263,20 +294,23 @@ The script gets a response from the model and prints the transcript and audio da
 The output will look similar to the following:
 
 ```console
-Received text delta: Hello
-Received text delta: !
-Received text delta:  How
-Received text delta:  can
-Received text delta:  I
+Received text delta:Of.
+Received text delta: course.
+Received text delta:!.
+Received text delta: How.
+Received text delta: can.
 Received 4800 bytes of audio data.
 Received 7200 bytes of audio data.
-Received text delta:  help
+Received text delta: I.
 Received 12000 bytes of audio data.
-Received text delta:  you
-Received text delta:  today
-Received text delta: ?
+Received text delta: help.
+Received text delta: you.
+Received text delta: today.
+Received text delta:?.
 Received 12000 bytes of audio data.
 Received 12000 bytes of audio data.
 Received 12000 bytes of audio data.
-Received 24000 bytes of audio data.
+Received 26400 bytes of audio data.
+
+Connection closed!
 ```
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "TypeScript コードの大幅な更新"
}
```

### Explanation
この変更は、`realtime-typescript.md`ファイルにおける大幅な更新を示しています。主な変更点は、TypeScriptコードの実装に関するもので、以下のような重要なポイントがあります：

1. **日付情報の更新**: 更新日が「2025年1月21日」から「2025年3月20日」に変更されました。

2. **クライアントライブラリの変更**: 旧版の「real-time audio client」から「OpenAI client」への移行が行われ、インストール手順や使用するパッケージ名が変更されています。

3. **関数の再構築**: 主要な機能が`text_in_audio_out`関数から`main`関数に移行され、コードの流れが改善されました。この変更により、環境変数の設定、エラー処理、WebSocket接続の管理がより明確になっています。

4. **新機能の追加**: 新しいWebSocketを用いたリアルタイムの通信処理が実装され、受信したメッセージの処理方法が強化されています。

全体として、追加と削除がそれぞれ150行と116行で、合計で266行の変更が行われています。この更新は、全体的な構造や機能性に大きな影響を与えるため、使用者は新しいインターフェース及び機能に適応する必要があります。

## articles/ai-services/openai/realtime-audio-quickstart.md{#item-727df8}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use GPT-4o Realtime API for speech and audio with Azur
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 2/7/2025
+ms.date: 3/20/2025
 author: eric-urban
 ms.author: eur
 ms.custom: references_regions, ignite-2024
@@ -32,7 +32,7 @@ See the [models and versions documentation](./concepts/models.md#gpt-4o-audio) f
 
 ## API support
 
-Support for the Realtime API was first added in API version `2024-10-01-preview`. Use the latest `2024-12-17` model version. 
+Support for the Realtime API was first added in API version `2024-10-01-preview`. Use version `2024-10-01-preview` to access the Realtime API. 
 
 ::: zone pivot="ai-foundry-portal"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントのバージョン情報の更新"
}
```

### Explanation
この変更は、`realtime-audio-quickstart.md`ファイルに対するもので、主にドキュメントの内容に関するマイナーな更新が行われました。以下に具体的な変更点を示します。

1. **日付情報の更新**: ドキュメントの更新日が「2025年2月7日」から「2025年3月20日」に変更されています。これは、最新の情報を反映するための通常の手続きです。

2. **APIサポートの説明の変更**: Realtime APIのサポートに関する記述が微調整され、最新のモデルバージョンを明確にするために、使用すべきAPIバージョンが「`2024-10-01-preview`」に変更されました。

この変更により、ユーザーが最新のAPIの使用方法を正確に把握するための情報が提供されています。全体として、追加と削除はそれぞれ2行で、わずか4行の変更が行われていますが、文書の正確性と関連性を維持するために重要な更新です。

## articles/ai-services/openai/realtime-audio-reference.md{#item-276d51}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use the Realtime API to interact with the Azure OpenAI
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 2/7/2025
+ms.date: 3/20/2025
 author: eric-urban
 ms.author: eur
 recommendations: false
@@ -31,13 +31,13 @@ You can construct a full request URI by concatenating:
 - The secure WebSocket (`wss://`) protocol.
 - Your Azure OpenAI resource endpoint hostname, for example, `my-aoai-resource.openai.azure.com`
 - The `openai/realtime` API path.
-- An `api-version` query string parameter for a supported API version such as `2024-12-17`
+- An `api-version` query string parameter for a supported API version such as `2024-10-01-preview`.
 - A `deployment` query string parameter with the name of your `gpt-4o-realtime-preview` or `gpt-4o-mini-realtime-preview` model deployment.
 
 The following example is a well-constructed `/realtime` request URI:
 
 ```http
-wss://my-eastus2-openai-resource.openai.azure.com/openai/realtime?api-version=2024-12-17&deployment=gpt-4o-realtime-preview
+wss://my-eastus2-openai-resource.openai.azure.com/openai/realtime?api-version=2024-10-01-preview&deployment=gpt-4o-realtime-preview
 ```
 
 ## Authentication
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョン情報の修正"
}
```

### Explanation
この変更は、`realtime-audio-reference.md`ファイルに対するもので、主にAPIバージョンに関するマイナーな更新が行われました。具体的な変更点は以下の通りです。

1. **日付情報の更新**: ドキュメントの更新日が「2025年2月7日」から「2025年3月20日」に変更されています。これにより、文書の最新性が保たれています。

2. **APIバージョンに関する記述の変更**: リクエストURIの生成に関する説明で、使用すべきAPIバージョンが「`2024-12-17`」から「`2024-10-01-preview`」に変更されました。これによって、ユーザーには正しいバージョンの使用を促す内容となっています。

3. **リクエストURIの例**: APIバージョンの変更に合わせて、URIの例も更新されています。具体的には、URIの`api-version`部分が上記の変更に従って修正されています。

変更の合計は、追加と削除がそれぞれ3行であり、全体で6行の微調整が行われています。これにより、ドキュメントの正確性が向上し、ユーザーがAPIを正しく使用するための情報が更新されています。


