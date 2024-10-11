---
date: '2024-10-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7341d04...MicrosoftDocs:576156f
summary: このドキュメントの更新では、Azure OpenAIに関連するいくつかのセクションでの小規模な修正や新機能の追加が行われました。主な内容として、新しい地域でのモデルサポート情報の充実、環境変数キーに関するドキュメントの追加が挙げられます。また、用語やクォータ情報の修正、JavaScript用アシスタントの実装ガイドの改訂も行われ、これらはユーザーがサービスをより効率的に利用できるようにするためのものです。全体として、開発者やエンドユーザーがAzure
  OpenAI技術を効果的に活用できるようなサポートを目指しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7341d04...MicrosoftDocs:576156f){target="_blank"}

# Highlights
このドキュメントの差分では、Azure OpenAIに関連するいくつかのセクションで小規模な更新と新機能の追加が行われました。特に、新しい地域でのモデルサポートに関する情報の拡充や、環境変数キーに関するドキュメントの追加がなされました。また、用語とクォータ情報の修正、JavaScript用アシスタントの実装ガイドが更新されています。これらの変更は、ユーザーがより効率的にサービスを利用できるようにするものです。

## New features
- アシスタント用の環境変数キーに関するドキュメントが追加されました。
- キーなしでのアシスタント用環境変数に関する新しいドキュメントが追加されました。

## Breaking changes
特に重大な変更はありませんが、表現やリンクの修正が複数行われており、ユーザーインターフェースの一貫性と精度が向上しています。

## Other updates
- モデルの最新情報を反映するため、地域リストが拡張されました。
- 展開タイプに関する用語が整理され、表現の明確化が行われました。
- JavaScript用アシスタントのガイドが更新され、新しいサンプルを含むセットアップ手順が強化されました。
- クォータと制限が最新の使用状況とパフォーマンスに合わせて更新されました。
- 新しいドキュメントの統合により目次の更新が行われ、リアルタイムオーディオクイックスタートのガイドが改善されました。

# Insights
この差分は、ユーザーがAzure OpenAIサービスを使用する際に直面する可能性のある問題を予測し、解決するためのものです。特に、地域の拡張と新たにサポートされたモデルが追加されたことで、ユーザーはより多くのオプションを持ち、自分のニーズに合った地域でモデルを展開する能力が高まりました。

また、新しい環境変数キーに関するドキュメントは、開発者がサービスを統合する際のハードルを下げ、Azureポータルでの設定を簡素化します。環境変数の詳細や設定方法に関する情報が強化されているため、新規導入者やエクスペリエンスレベルの異なるユーザーに配慮された内容となっており、設定の一貫性が保たれます。

さらには、リアルタイムオーディオクイックスタートガイドの更新によって、新しいファイル構造が導入され、情報の一貫性が改善されました。このことで、ユーザーが最新の情報にアクセスしやすくなり、機能への迅速なアクセスが提供されます。特に、日本語を含めた多言語サポートがあることで、非英語圏のユーザーにも理解しやすい改善が図られています。

全体として、このドキュメントの変更は、開発者やエンドユーザーがAzure OpenAI技術をより効率的に、かつ効果的に活用できるようサポートするために設計されています。モデルのサポート地域や環境設定における新情報は、将来的なサービス拡張や改良を視野に入れた重要なアップデートです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | モデルに関する情報の更新 | modified | 3 | 3 | 6 | 
| [deployment-types.md](#item-210814) | minor update | 展開タイプに関する用語の修正 | modified | 2 | 2 | 4 | 
| [assistants-env-var-key.md](#item-670ce2) | new feature | アシスタント用の環境変数キーに関するドキュメントの追加 | added | 17 | 0 | 17 | 
| [assistants-env-var-without-key.md](#item-039e55) | new feature | キーなしでのアシスタント用環境変数に関するドキュメントの追加 | added | 16 | 0 | 16 | 
| [assistants-javascript.md](#item-ad3627) | minor update | JavaScript用アシスタントの実装ガイドの更新 | modified | 485 | 45 | 530 | 
| [quota.md](#item-389aa1) | minor update | クォータ情報の更新 | modified | 7 | 7 | 14 | 
| [standard-global.md](#item-17a84b) | minor update | モデルの標準グローバルマトリックスの更新 | modified | 5 | 5 | 10 | 
| [standard-models.md](#item-af04c4) | minor update | 標準モデルのマトリックスの更新 | modified | 6 | 5 | 11 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータと制限の更新 | modified | 4 | 4 | 8 | 
| [realtime-audio-quickstart.md](#item-727df8) | minor update | リアルタイムオーディオクイックスタートの名前変更 | renamed | 7 | 7 | 14 | 
| [toc.yml](#item-c945af) | minor update | 目次の更新 | modified | 2 | 2 | 4 | 
| [whats-new.md](#item-53303b) | minor update | 新しいリアルタイムオーディオドキュメントへのリンク更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 10/01/2024
+ms.date: 10/09/2024
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -221,15 +221,15 @@ print(response.model_dump_json(indent=2))
 
 ### Region availability
 
-Available for standard and global standard deployment in East US2 and Sweden Central for approved customers.
+Available for standard and global standard deployment in East US, East US2, North Central US, South Central US, Sweden Central, West US, and West US3 for approved customers.
 
 ## GPT-4o audio
 
 The `gpt-4o-realtime-preview` model is part of the GPT-4o model family and supports low-latency, "speech in, speech out" conversational interactions. GPT-4o audio is designed to handle real-time, low-latency conversational interactions, making it a great fit for support agents, assistants, translators, and other use cases that need highly responsive back-and-forth with a user.
 
 GPT-4o audio is available in the East US 2 (`eastus2`) and Sweden Central (`swedencentral`) regions. To use GPT-4o audio, you need to [create](../how-to/create-resource.md) or use an existing resource in one of the supported regions.
 
-When your resource is created, you can [deploy](../how-to/create-resource.md#deploy-a-model) the GPT-4o audio model. If you are performing a programmatic deployment, the **model** name is `gpt-4o-realtime-preview`. For more information on how to use GPT-4o audio, see the [GPT-4o audio documentation](../how-to/audio-real-time.md).
+When your resource is created, you can [deploy](../how-to/create-resource.md#deploy-a-model) the GPT-4o audio model. If you are performing a programmatic deployment, the **model** name is `gpt-4o-realtime-preview`. For more information on how to use GPT-4o audio, see the [GPT-4o audio documentation](../realtime-audio-quickstart.md).
 
 Details about maximum request tokens and training data are available in the following table.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルに関する情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのモデルに関するドキュメントの更新を含んでいます。具体的には、2つの主な修正が行われました。まず、ドキュメントの最終更新日が「2024年10月1日」から「2024年10月9日」に変更されました。次に、利用可能な地域のリストが拡張されました。具体的には、East US2およびSweden Central地域に加えて、East US、North Central US、South Central US、West US、およびWest US3が新たに追加されました。この変更は、モデルの展開に関する情報の正確性を向上させ、ユーザーに対して最新の地域情報を提供することを目的としています。また、GPT-4o音声モデルのドキュメントへのリンクも更新され、ユーザーが必要なリソースを見つけやすくするための改善がなされています。

## articles/ai-services/openai/how-to/deployment-types.md{#item-210814}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.author: mbullwin
 
 Azure OpenAI provides customers with choices on the hosting structure that fits their business and usage patterns. The service offers two main types of deployment: **standard** and **provisioned**. Standard is offered with a global deployment option, routing traffic globally to provide higher throughput. Provisioned is also offered with a global deployment option, allowing customers to purchase and deploy provisioned throughput units across Azure global infrastructure. All deployments can perform the exact same inference operations, however the billing, scale and performance are substantially different. As part of your solution design, you will need to make two key decisions:
 
-- **Data residency needs**: global vs. regional resources  
+- **Data processing needs**: global vs. regional resources  
 - **Call volume**: standard vs. provisioned
 
 ## Global versus regional deployment types
@@ -32,7 +32,7 @@ Azure OpenAI offers three types of deployments. These provide a varied level of
 
 | **Offering** | **Global-Batch** | **Global-Standard**|  **Global-Provisioned**  | **Standard** | **Provisioned**  |
 |---|:---|:---| -------- |:---|:---|
-| **Best suited for**      | Offline scoring <br><br> Workloads that are not latency sensitive and can be completed in hours.<br><br> For use cases that do not have data processing residency requirements.|Recommended starting place for customers. <br><br>Global-Standard will have the higher default quota and larger number of models available than Standard. |Real-time scoring for large consistent volume. Includes the highest commitments and limits.                                                                                               For use cases that do not have data residency requirements.| For customers with data residency requirements. Optimized for low to medium volume. |Real-time scoring for large consistent volume. Includes the highest commitments and limits.                                                                                          For use cases with data residency requirements|
+| **Best suited for**      | Offline scoring <br><br> Workloads that are not latency sensitive and can be completed in hours.<br><br>|Recommended starting place for customers. <br><br>Global-Standard will have the higher default quota and larger number of models available than Standard. |Real-time scoring for large consistent volume. Includes the highest commitments and limits.                                                                                             | For customers with data residency requirements. Optimized for low to medium volume. |Real-time scoring for large consistent volume. Includes the highest commitments and limits.                                                                                          For use cases with data residency requirements|
 | **How it works**         | Offline processing via files |Traffic may be routed anywhere in the world |Traffic may be routed anywhere in the world| | |
 | **Getting started**      | [Global-Batch](./batch.md) | [Model deployment](./create-resource.md) |[Provisioned onboarding](/azure/ai-services/openai/how-to/provisioned-throughput-onboarding)| [Model deployment](./create-resource.md) | [Provisioned onboarding](./provisioned-throughput-onboarding.md) |
 | **Cost**                 | [Least expensive option](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> 50% less cost compared to Global Standard prices. Access to all new models with larger quota allocations.  | [Global deployment pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) |May experience cost savings for consistent usage|  [Regional pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) |May experience cost savings for consistent usage |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "展開タイプに関する用語の修正"
}
```

### Explanation
このコードの変更は、Azure OpenAIの展開タイプに関するドキュメントの用語の更新を目的としています。具体的には、データ処理の要件に関連する表現が修正されました。「データ居住のニーズ」から「データ処理のニーズ」への変更が行われ、表現がより明確に、現在の文脈にふさわしいものとなりました。

さらに、テーブル内での最適な使用例についてもわずかな修正が行われ、情報の正確性と一貫性が向上しました。これにより、ユーザーは異なる展開タイプの利用状況と要件に関する理解を深め、適切な選択を行いやすくなります。この変更は、全体的な文書のユーザビリティ向上に寄与するものです。

## articles/ai-services/openai/includes/assistants-env-var-key.md{#item-670ce2}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,17 @@
+---
+manager: nitinme
+author: mrbullwinkle
+ms.author: mbullwin
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 10/09/2024
+ms.custom: devex-track-js, devex-track-typescript
+---
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. |
+| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+| `AZURE_OPENAI_DEPLOYMENT_NAME` | This value will correspond to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Model Deployments** in the Azure portal.|
+| `OPENAI_API_VERSION`|Learn more about [API Versions](/azure/ai-services/openai/api-version-deprecation).|
+
+Learn more about [finding API keys](/azure/ai-services/cognitive-services-environment-variables) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "アシスタント用の環境変数キーに関するドキュメントの追加"
}
```

### Explanation
このコードの変更は、Azure OpenAIにおけるアシスタント用の環境変数キーに関する新しいドキュメントを追加することを目的としています。この新しいファイルには、環境変数名とその値に関する情報が表形式で記載されています。具体的には、`AZURE_OPENAI_ENDPOINT`、`AZURE_OPENAI_API_KEY`、`AZURE_OPENAI_DEPLOYMENT_NAME`、および`OPENAI_API_VERSION`の各環境変数についての詳細が含まれています。

各環境変数の値は、Azureポータル内のリソースの「Keys and Endpoint」セクションや、「Resource Management」内の「Model Deployments」から確認できることが明記されています。また、APIバージョンに関する情報や環境変数の設定方法にリンクが提供されており、ユーザーが容易に必要な情報にアクセスできるようになっています。この変更により、Azure OpenAIを使用する際の設定手順が明確にされ、開発者やユーザーに対するサポートが向上します。

## articles/ai-services/openai/includes/assistants-env-var-without-key.md{#item-039e55}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,16 @@
+---
+manager: nitinme
+author: mrbullwinkle
+ms.author: mbullwin
+ms.service: azure-ai-openai
+ms.topic: include
+ms.date: 10/0//2024
+ms.custom: devex-track-js, devex-track-typescript
+---
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
    "modification_title": "キーなしでのアシスタント用環境変数に関するドキュメントの追加"
}
```

### Explanation
このコードの変更は、キーなしでのアシスタント用環境変数に関する新しいドキュメントを追加することを目的としています。新しく追加されたファイルには、アシスタントが必要とする環境変数の名前とその値に関する情報が表形式で記載されています。

具体的には、`AZURE_OPENAI_ENDPOINT`と`AZURE_OPENAI_DEPLOYMENT_NAME`、および`OPENAI_API_VERSION`の変数が含まれています。これらの変数の値は、Azureポータルの「Keys and Endpoint」セクションや、「Resource Management」内の「Model Deployments」から確認することができると説明されています。

また、キーなし認証や環境変数の設定方法についてのリンクも提供されており、ユーザーが必要な情報に簡単にアクセスできるようになっています。この変更によって、Azure OpenAIを利用する際の設定に関する理解が深まり、特にキーを使わずに利用する方法に関する説明が強化されている点が特徴です。

## articles/ai-services/openai/includes/assistants-javascript.md{#item-ad3627}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: mrbullwinkle
 ms.author: mbullwin
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 05/30/2024
+ms.date: 10/09/2024
 ms.custom: passwordless-js, devex-track-javascript
 ---
 
@@ -16,7 +16,8 @@ ms.custom: passwordless-js, devex-track-javascript
 ## Prerequisites
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
-- <a href="https://nodejs.org/" target="_blank">Node.js LTS with TypeScript or ESM support.</a>
+- <a href="https://nodejs.org/" target="_blank">Node.js LTS or ESM support.</a>
+- [TypeScript](https://www.typescriptlang.org/download/) installed globally
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI. 
 - An Azure OpenAI resource with a [compatible model in a supported region](../concepts/models.md#assistants-preview).
 - We recommend reviewing the [Responsible AI transparency note](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=text) and other [Responsible AI resources](/legal/cognitive-services/openai/overview?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext) to familiarize yourself with the capabilities and limitations of the Azure OpenAI Service.
@@ -32,64 +33,71 @@ For passwordless authentication, you need to
 
 ## Set up
 
+1. Create a new folder `assistants-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
+
+    ```shell
+    mkdir assistants-quickstart && code assistants-quickstart
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
+
 1. Install the OpenAI Assistants client library for JavaScript with:
 
     ```console
     npm install openai
     ```
 
-2. For the **recommended** passwordless authentication:
+1. For the **recommended** passwordless authentication:
 
     ```console
     npm install @azure/identity
     ```
 
-## Retrieve key and endpoint
+## Retrieve resource information
 
-To successfully make a call against the Azure OpenAI service, you'll need the following:
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
-|Variable name | Value |
-|--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in **Azure OpenAI Studio** > **Playground** > **View code**. An example endpoint is: `https://docs-test-001.openai.azure.com/`.|
-| `API-KEY` | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
-| `DEPLOYMENT-NAME` | This value will correspond to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Model Deployments** in the Azure portal or alternatively under **Management** > **Deployments** in Azure OpenAI Studio.|
+#### [TypeScript keyless (Recommended)](#tab/typescript-keyless)
 
-Go to your resource in the Azure portal. The **Keys and Endpoint** can be found in the **Resource Management** section. Copy your endpoint and access key as you'll need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
+[!INCLUDE [assistants-keyless-environment-variables](assistants-env-var-without-key.md)]
 
-:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview blade for an OpenAI Resource in the Azure portal with the endpoint & access keys location circled in red." lightbox="../media/quickstarts/endpoint.png":::
 
-[!INCLUDE [environment-variables](environment-variables.md)]
+#### [TypeScript with API key](#tab/typescript-key)
 
-Add additional environment variables for the deployment name and API version: 
-* `AZURE_OPENAI_DEPLOYMENT_NAME`: Your deployment name as shown in the Azure portal.
-* `OPENAI_API_VERSION`: Learn more about [API Versions](/azure/ai-services/openai/concepts/model-versions).
+[!INCLUDE [assistants-key-environment-variables](assistants-env-var-key.md)]
 
-# [Command Line](#tab/command-line)
 
-```cmd
-setx AZURE_OPENAI_DEPLOYMENT_NAME "REPLACE_WITH_YOUR_DEPLOYMENT_NAME" 
-setx OPENAI_API_VERSION "REPLACE_WITH_YOUR_API_VERSION" 
-```
+#### [JavaScript keyless](#tab/javascript-keyless)
 
-# [PowerShell](#tab/powershell)
+[!INCLUDE [assistants-keyless-environment-variables](assistants-env-var-without-key.md)]
 
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_DEPLOYMENT_NAME', 'REPLACE_WITH_YOUR_DEPLOYMENT_NAME', 'User')
-[System.Environment]::SetEnvironmentVariable('OPENAI_API_VERSION', 'REPLACE_WITH_YOUR_API_VERSION', 'User')
-```
 
-# [Bash](#tab/bash)
+#### [JavaScript with API key](#tab/javascript-key)
 
-```bash
-export AZURE_OPENAI_DEPLOYMENT_NAME="REPLACE_WITH_YOUR_DEPLOYMENT_NAME"
-export OPENAI_API_VERSION="REPLACE_WITH_YOUR_API_VERSION"
-```
+[!INCLUDE [assistants-key-environment-variables](assistants-env-var-key.md)]
 
 ---
 
+> [!CAUTION]
+> Don't set `AZURE_OPENAI_API_KEY` when using keyless authentication.
+
+
 ## Create an assistant
 
-In our code we are going to specify the following values:
+In our code we're going to specify the following values:
 
 | **Name** | **Description** |
 |:---|:---|
@@ -100,30 +108,460 @@ In our code we are going to specify the following values:
 
 ### Tools
 
-An individual assistant can access up to 128 tools including `code interpreter`, as well as any custom tools you create via [functions](../how-to/assistant-functions.md).
+An individual assistant can access up to 128 tools including `code interpreter`, and any custom tools you create via [functions](../how-to/assistant-functions.md).
+
+#### [TypeScript keyless (Recommended)](#tab/typescript-keyless)
+
+1. Create the `index.ts` file with the following code:
+
+    ```typescript
+    import { AzureOpenAI } from "openai";
+    import {
+      Assistant,
+      AssistantCreateParams,
+      AssistantTool,
+    } from "openai/resources/beta/assistants";
+    import { Message, MessagesPage } from "openai/resources/beta/threads/messages";
+    import { Run } from "openai/resources/beta/threads/runs/runs";
+    import { Thread } from "openai/resources/beta/threads/threads";
+    
+    // Add `Cognitive Services User` to identity for Azure OpenAI resource
+    import {
+      DefaultAzureCredential,
+      getBearerTokenProvider,
+    } from "@azure/identity";
+    
+    // Get environment variables
+    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT as string;
+    const azureOpenAIDeployment = process.env
+      .AZURE_OPENAI_DEPLOYMENT_NAME as string;
+    const openAIVersion = process.env.OPENAI_API_VERSION as string;
+    
+    // Check env variables
+    if (!azureOpenAIEndpoint || !azureOpenAIDeployment || !openAIVersion) {
+      throw new Error(
+        "Please ensure to set AZURE_OPENAI_DEPLOYMENT_NAME and AZURE_OPENAI_ENDPOINT in your environment variables."
+      );
+    }
+    
+    // Get Azure SDK client
+    const getClient = (): AzureOpenAI => {
+      const credential = new DefaultAzureCredential();
+      const scope = "https://cognitiveservices.azure.com/.default";
+      const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+      const assistantsClient = new AzureOpenAI({
+        endpoint: azureOpenAIEndpoint,
+        apiVersion: openAIVersion,
+        azureADTokenProvider,
+      });
+      return assistantsClient;
+    };
+    
+    const assistantsClient = getClient();
+    
+    const options: AssistantCreateParams = {
+      model: azureOpenAIDeployment, // Deployment name seen in Azure AI Studio
+      name: "Math Tutor",
+      instructions:
+        "You are a personal math tutor. Write and run JavaScript code to answer math questions.",
+      tools: [{ type: "code_interpreter" } as AssistantTool],
+    };
+    const role = "user";
+    const message = "I need to solve the equation `3x + 11 = 14`. Can you help me?";
+    
+    // Create an assistant
+    const assistantResponse: Assistant =
+      await assistantsClient.beta.assistants.create(options);
+    console.log(`Assistant created: ${JSON.stringify(assistantResponse)}`);
+    
+    // Create a thread
+    const assistantThread: Thread = await assistantsClient.beta.threads.create({});
+    console.log(`Thread created: ${JSON.stringify(assistantThread)}`);
+    
+    // Add a user question to the thread
+    const threadResponse: Message =
+      await assistantsClient.beta.threads.messages.create(assistantThread.id, {
+        role,
+        content: message,
+      });
+    console.log(`Message created:  ${JSON.stringify(threadResponse)}`);
+    
+    // Run the thread and poll it until it is in a terminal state
+    const runResponse: Run = await assistantsClient.beta.threads.runs.createAndPoll(
+      assistantThread.id,
+      {
+        assistant_id: assistantResponse.id,
+      },
+      { pollIntervalMs: 500 }
+    );
+    console.log(`Run created:  ${JSON.stringify(runResponse)}`);
+    
+    // Get the messages
+    const runMessages: MessagesPage =
+      await assistantsClient.beta.threads.messages.list(assistantThread.id);
+    for await (const runMessageDatum of runMessages) {
+      for (const item of runMessageDatum.content) {
+        // types are: "image_file" or "text"
+        if (item.type === "text") {
+          console.log(`Message content: ${JSON.stringify(item.text?.value)}`);
+        }
+      }
+    }
+    ```
+    
+
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
 
-#### [TypeScript](#tab/typescript)
+1. Run the code with the following command:
 
-Sign in to Azure with `az login` then create and run an assistant with the following **recommended** passwordless TypeScript module (index.ts):
+    ```shell
+    node index.js
+    ```
 
-:::code language="typescript" source="~/azure-typescript-e2e-apps/quickstarts/azure-openai-assistants/ts/src/index.ts" :::
+#### [TypeScript with API key](#tab/typescript-key)
+
+1. Create the `index.ts` file with the following code:
+
+    ```typescript
+    import { AzureOpenAI } from "openai";
+    import {
+      Assistant,
+      AssistantCreateParams,
+      AssistantTool,
+    } from "openai/resources/beta/assistants";
+    import { Message, MessagesPage } from "openai/resources/beta/threads/messages";
+    import { Run } from "openai/resources/beta/threads/runs/runs";
+    import { Thread } from "openai/resources/beta/threads/threads";
+    
+    // Get environment variables
+    const azureOpenAIKey = process.env.AZURE_OPENAI_KEY as string;
+    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT as string;
+    const azureOpenAIDeployment = process.env
+      .AZURE_OPENAI_DEPLOYMENT_NAME as string;
+    const openAIVersion = process.env.OPENAI_API_VERSION as string;
+    
+    // Check env variables
+    if (!azureOpenAIKey || !azureOpenAIEndpoint || !azureOpenAIDeployment || !openAIVersion) {
+      throw new Error(
+        "Please set AZURE_OPENAI_KEY and AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_DEPLOYMENT_NAME in your environment variables."
+      );
+    }
+    
+    // Get Azure SDK client
+    const getClient = (): AzureOpenAI => {
+      const assistantsClient = new AzureOpenAI({
+        endpoint: azureOpenAIEndpoint,
+        apiVersion: openAIVersion,
+        apiKey: azureOpenAIKey,
+      });
+      return assistantsClient;
+    };
+    
+    const assistantsClient = getClient();
+    
+    const options: AssistantCreateParams = {
+      model: azureOpenAIDeployment, // Deployment name seen in Azure AI Studio
+      name: "Math Tutor",
+      instructions:
+        "You are a personal math tutor. Write and run JavaScript code to answer math questions.",
+      tools: [{ type: "code_interpreter" } as AssistantTool],
+    };
+    const role = "user";
+    const message = "I need to solve the equation `3x + 11 = 14`. Can you help me?";
+    
+    // Create an assistant
+    const assistantResponse: Assistant =
+      await assistantsClient.beta.assistants.create(options);
+    console.log(`Assistant created: ${JSON.stringify(assistantResponse)}`);
+    
+    // Create a thread
+    const assistantThread: Thread = await assistantsClient.beta.threads.create({});
+    console.log(`Thread created: ${JSON.stringify(assistantThread)}`);
+    
+    // Add a user question to the thread
+    const threadResponse: Message =
+      await assistantsClient.beta.threads.messages.create(assistantThread.id, {
+        role,
+        content: message,
+      });
+    console.log(`Message created:  ${JSON.stringify(threadResponse)}`);
+    
+    // Run the thread and poll it until it is in a terminal state
+    const runResponse: Run = await assistantsClient.beta.threads.runs.createAndPoll(
+      assistantThread.id,
+      {
+        assistant_id: assistantResponse.id,
+      },
+      { pollIntervalMs: 500 }
+    );
+    console.log(`Run created:  ${JSON.stringify(runResponse)}`);
+    
+    // Get the messages
+    const runMessages: MessagesPage =
+      await assistantsClient.beta.threads.messages.list(assistantThread.id);
+    for await (const runMessageDatum of runMessages) {
+      for (const item of runMessageDatum.content) {
+        // types are: "image_file" or "text"
+        if (item.type === "text") {
+          console.log(`Message content: ${JSON.stringify(item.text?.value)}`);
+        }
+      }
+    }
+    ```
+    
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
 
-To use the service key for authentication, you can create and run an assistant with the following TypeScript module (index.ts):
+1. Transpile from TypeScript to JavaScript.
 
-:::code language="typescript" source="~/azure-typescript-e2e-apps/quickstarts/azure-openai-assistants/ts/src/index-using-password.ts" :::
+    ```shell
+    tsc
+    ```
 
-#### [JavaScript](#tab/javascript)
+1. Run the code with the following command:
 
-Sign in to Azure with `az login` then create and run an assistant with the following **recommended** passwordless JavaScript module (index.mjs):
+    ```shell
+    node index.js
+    ```
 
-:::code language="javascript" source="~/azure-typescript-e2e-apps/quickstarts/azure-openai-assistants/js/src/index.mjs" :::
+#### [JavaScript keyless](#tab/javascript-keyless)
+
+1. Create the `index.js` file with the following code:
+
+    ```nodejs
+    import { AzureOpenAI } from "openai";
+    
+    // Add `Cognitive Services User` to identity for Azure OpenAI resource
+    import {
+      DefaultAzureCredential,
+      getBearerTokenProvider,
+    } from "@azure/identity";
+    
+    // Get environment variables
+    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT;
+    const azureOpenAIDeployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME;
+    const azureOpenAIVersion = process.env.OPENAI_API_VERSION;
+    
+    // Check env variables
+    if (!azureOpenAIEndpoint || !azureOpenAIDeployment || !azureOpenAIVersion) {
+      throw new Error(
+        "Please ensure to set AZURE_OPENAI_DEPLOYMENT_NAME and AZURE_OPENAI_ENDPOINT in your environment variables."
+      );
+    }
+    
+    // Get Azure SDK client
+    const getClient = () => {
+      const credential = new DefaultAzureCredential();
+      const scope = "https://cognitiveservices.azure.com/.default";
+      const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+      const assistantsClient = new AzureOpenAI({
+        endpoint: azureOpenAIEndpoint,
+        apiVersion: azureOpenAIVersion,
+        azureADTokenProvider,
+      });
+      return assistantsClient;
+    };
+    
+    const assistantsClient = getClient();
+    
+    const options = {
+      model: azureOpenAIDeployment, // Deployment name seen in Azure AI Studio
+      name: "Math Tutor",
+      instructions:
+        "You are a personal math tutor. Write and run JavaScript code to answer math questions.",
+      tools: [{ type: "code_interpreter" }],
+    };
+    const role = "user";
+    const message = "I need to solve the equation `3x + 11 = 14`. Can you help me?";
+    
+    // Create an assistant
+    const assistantResponse = await assistantsClient.beta.assistants.create(
+      options
+    );
+    console.log(`Assistant created: ${JSON.stringify(assistantResponse)}`);
+    
+    // Create a thread
+    const assistantThread = await assistantsClient.beta.threads.create({});
+    console.log(`Thread created: ${JSON.stringify(assistantThread)}`);
+    
+    // Add a user question to the thread
+    const threadResponse = await assistantsClient.beta.threads.messages.create(
+      assistantThread.id,
+      {
+        role,
+        content: message,
+      }
+    );
+    console.log(`Message created:  ${JSON.stringify(threadResponse)}`);
+    
+    // Run the thread and poll it until it is in a terminal state
+    const runResponse = await assistantsClient.beta.threads.runs.createAndPoll(
+      assistantThread.id,
+      {
+        assistant_id: assistantResponse.id,
+      },
+      { pollIntervalMs: 500 }
+    );
+    console.log(`Run created:  ${JSON.stringify(runResponse)}`);
+    
+    // Get the messages
+    const runMessages = await assistantsClient.beta.threads.messages.list(
+      assistantThread.id
+    );
+    for await (const runMessageDatum of runMessages) {
+      for (const item of runMessageDatum.content) {
+        // types are: "image_file" or "text"
+        if (item.type === "text") {
+          console.log(`Message content: ${JSON.stringify(item.text?.value)}`);
+        }
+      }
+    }
+    ```
 
-To use the service key for authentication, you can create and run an assistant with the following JavaScript module (index.mjs):
+1. Sign in to Azure with the following command:
 
-:::code language="javascript" source="~/azure-typescript-e2e-apps/quickstarts/azure-openai-assistants/js/src/index-using-password.mjs" :::
+    ```shell
+    az login
+    ```
 
+1. Run the JavaScript file.
 
---- 
+    ```shell
+    node index.js
+    ```
+
+#### [JavaScript with API key](#tab/javascript-key)
+
+1. Create the `index.js` file with the following code:
+
+    ```nodejs
+    import { AzureOpenAI } from "openai";
+    
+    // Get environment variables
+    const azureOpenAIKey = process.env.AZURE_OPENAI_KEY;
+    const azureOpenAIEndpoint = process.env.AZURE_OPENAI_ENDPOINT;
+    const azureOpenAIDeployment = process.env.AZURE_OPENAI_DEPLOYMENT_NAME;
+    const azureOpenAIVersion = process.env.OPENAI_API_VERSION;
+    
+    // Check env variables
+    if (!azureOpenAIKey || !azureOpenAIEndpoint || !azureOpenAIDeployment || !azureOpenAIVersion) {
+      throw new Error(
+        "Please set AZURE_OPENAI_KEY and AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_DEPLOYMENT_NAME in your environment variables."
+      );
+    }
+    
+    // Get Azure SDK client
+    const getClient = () => {
+      const assistantsClient = new AzureOpenAI({
+        endpoint: azureOpenAIEndpoint,
+        apiVersion: azureOpenAIVersion,
+        apiKey: azureOpenAIKey,
+      });
+      return assistantsClient;
+    };
+    
+    const assistantsClient = getClient();
+    
+    const options = {
+      model: azureOpenAIDeployment, // Deployment name seen in Azure AI Studio
+      name: "Math Tutor",
+      instructions:
+        "You are a personal math tutor. Write and run JavaScript code to answer math questions.",
+      tools: [{ type: "code_interpreter" }],
+    };
+    const role = "user";
+    const message = "I need to solve the equation `3x + 11 = 14`. Can you help me?";
+    
+    // Create an assistant
+    const assistantResponse = await assistantsClient.beta.assistants.create(
+      options
+    );
+    console.log(`Assistant created: ${JSON.stringify(assistantResponse)}`);
+    
+    // Create a thread
+    const assistantThread = await assistantsClient.beta.threads.create({});
+    console.log(`Thread created: ${JSON.stringify(assistantThread)}`);
+    
+    // Add a user question to the thread
+    const threadResponse = await assistantsClient.beta.threads.messages.create(
+      assistantThread.id,
+      {
+        role,
+        content: message,
+      }
+    );
+    console.log(`Message created:  ${JSON.stringify(threadResponse)}`);
+    
+    // Run the thread and poll it until it is in a terminal state
+    const runResponse = await assistantsClient.beta.threads.runs.createAndPoll(
+      assistantThread.id,
+      {
+        assistant_id: assistantResponse.id,
+      },
+      { pollIntervalMs: 500 }
+    );
+    console.log(`Run created:  ${JSON.stringify(runResponse)}`);
+    
+    // Get the messages
+    const runMessages = await assistantsClient.beta.threads.messages.list(
+      assistantThread.id
+    );
+    for await (const runMessageDatum of runMessages) {
+      for (const item of runMessageDatum.content) {
+        // types are: "image_file" or "text"
+        if (item.type === "text") {
+          console.log(`Message content: ${JSON.stringify(item.text?.value)}`);
+        }
+      }
+    }
+    ```
+
+1. Run the JavaScript file.
+
+    ```shell
+    node index.js
+    ```
+
+```
 
 ## Output
 
@@ -138,7 +576,9 @@ Message content: "Yes, of course! To solve the equation \\( 3x + 11 = 14 \\), we
 Message content: "I need to solve the equation `3x + 11 = 14`. Can you help me?"
 ```
 
-It is important to remember that while the code interpreter gives the model the capability to respond to more complex queries by converting the questions into code and running that code iteratively in JavaScript until it reaches a solution, you still need to validate the response to confirm that the model correctly translated your question into a valid representation in code.
+It's important to remember that while the code interpreter gives the model the capability to respond to more complex queries by converting the questions into code and running that code iteratively in JavaScript until it reaches a solution, you still need to validate the response to confirm that the model correctly translated your question into a valid representation in code.
+
+---
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript用アシスタントの実装ガイドの更新"
}
```

### Explanation
このコードの変更は、JavaScript用アシスタントの実装ガイドを更新する目的で行われました。主な変更点には、日付の更新、環境変数に関する情報の追加、アシスタントのセットアップ手順の詳細化が含まれています。特に、パスワードレス認証の推奨手順と、エクスポートされた環境変数の設定方法に関するガイドが強化されています。

具体的には、Node.jsおよびTypeScriptの設定手順が詳述されており、新しいフォルダの作成、`package.json`の作成と更新のコマンドが追加されています。また、`index.ts`と`index.js`のサンプルコードが新たに含まれ、アシスタントの作成方法やスレッドの実行に関する手順が整理されています。

これにより、開発者がAzure OpenAIのアシスタントをJavaScriptで利用する際の手順が明確になり、従来のドキュメント内容が最新の情報に基づいて更新されています。ユーザーはこの変更を通じて、必要な環境設定やコーディング手順をスムーズに遵守できるようになります。

## articles/ai-services/openai/includes/model-matrix/quota.md{#item-389aa1}

<details>
<summary>Diff</summary>
````diff
@@ -14,23 +14,23 @@ ms.date: 10/04/2024
 | australiaeast      | -         | -     | 40 K    | 80 K        | 80 K          | 30 K            | -        | -             | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | brazilsouth        | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | canadaeast         | -         | -     | 40 K    | 80 K        | 80 K          | -               | -        | -             | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| eastus             | -         | -     | -       | -           | 80 K          | -               | 1 M      | 2 M           | 240 K          | 240 K                   | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 240 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| eastus2            | 1 M       | 600 K | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | 50 M                       | 15 M                  | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | 250 K               | -                        | -                  | -             | -                        | -             | -                        | 250 K                     | 250 K                          | 250 K                          |
+| eastus             | 1 M       | 600 K | -       | -           | 80 K          | -               | 1 M      | 2 M           | 240 K          | 240 K                   | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 240 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| eastus2            | 1 M       | 600 K | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | 250 K               | -                        | -                  | -             | -                        | -             | -                        | 250 K                     | 250 K                          | 250 K                          |
 | francecentral      | -         | -     | 20 K    | 60 K        | 80 K          | -               | -        | -             | 240 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | germanywestcentral | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | japaneast          | -         | -     | -       | -           | -             | 30 K            | -        | -             | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | 350 K                    | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | koreacentral       | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| northcentralus     | -         | -     | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
+| northcentralus     | 1 M       | 600 K | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
 | norwayeast         | -         | -     | -       | -           | 150 K         | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | polandcentral      | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | southafricanorth   | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| southcentralus     | -         | -     | -       | -           | 80 K          | -               | 1 M      | 2 M           | 240 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| southcentralus     | 1 M       | 600 K | -       | -           | 80 K          | -               | 1 M      | 2 M           | 240 K          | -                       | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | southindia         | -         | -     | -       | -           | 150 K         | -               | -        | -             | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | spaincentral       | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| swedencentral      | 1 M       | 600 K | 40 K    | 80 K        | 150 K         | 30 K            | 1 M      | 2 M           | 300 K          | 240 K                   | 50 M                       | 15 M                  | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | 350 K                    | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
+| swedencentral      | 1 M       | 600 K | 40 K    | 80 K        | 150 K         | 30 K            | 1 M      | 2 M           | 300 K          | 240 K                   | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | 350 K                    | 250 K               | 500 K                    | 100 K              | 240 K         | 250 K                    | 240 K         | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
 | switzerlandnorth   | -         | -     | 40 K    | 80 K        | -             | 30 K            | -        | -             | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | switzerlandwest    | -         | -     | -       | -           | -             | -               | -        | -             | -              | -                       | -                          | -                     | -                         | -                              | -                              | -                       | -                            | -                      | -                            | -                             | -                        | -                        | -                        | -                   | -                        | -                  | -             | 250 K                    | -             | 250 K                    | 250 K                     | 250 K                          | 250 K                          |
 | uksouth            | -         | -     | -       | -           | 80 K          | -               | -        | -             | 240 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
 | westeurope         | -         | -     | -       | -           | -             | -               | -        | -             | 240 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 240 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| westus             | -         | -     | -       | -           | 80 K          | 30 K            | 1 M      | 2 M           | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
-| westus3            | -         | -     | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | -                          | -                     | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| westus             | 1 M       | 600 K | -       | -           | 80 K          | 30 K            | 1 M      | 2 M           | 300 K          | -                       | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | 5 B                     | 5 B                          | 150 M                  | 300 M                        | 10 B                          | 350 K                    | -                        | -                        | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
+| westus3            | 1 M       | 600 K | -       | -           | 80 K          | -               | 1 M      | 2 M           | 300 K          | -                       | 50 M                       | 30 M                  | 30 M                      | 50 M                           | 2 M                            | -                       | -                            | -                      | -                            | -                             | 350 K                    | -                        | 350 K                    | -                   | -                        | -                  | -             | -                        | -             | -                        | -                         | -                              | -                              |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータ情報の更新"
}
```

### Explanation
このコードの変更は、OpenAIのモデルに関するクォータ情報を更新するためのもので、特に地域ごとの制限や使用可能なリソースに関するデータが修正されています。具体的には、クォータの値に関して、いくつかの地域でのキャパシティ値が変更されており、これは解析や実行時に影響を与える可能性があるため重要です。

変更されたセクションでは、使用月間、同時実行数、リクエスト数、特定のパラメータなどが含まれており、以下のような更新がありました：
- `eastus`や`eastus2`、`northcentralus`などの各地域におけるキャパシティ値の具体的な数値が追加または修正されています。
- これにより、利用者は特定の地域において期待されるパフォーマンスを正確に把握できるようになります。

この変更は、ユーザーがリソースを計画し、適切な地域を選択する際の参考情報として役立つもので、Azure OpenAIサービスの利用をより効果的に行うことを促進します。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -13,22 +13,22 @@ ms.date: 10/03/2024
 | australiaeast      | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
 | brazilsouth        | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
 | canadaeast         | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| eastus             | -                          | -                       | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
+| eastus             | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
 | eastus2            | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                                        |
 | francecentral      | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
 | germanywestcentral | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
 | japaneast          | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
 | koreacentral       | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| northcentralus     | -                          | -                       | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
+| northcentralus     | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
 | norwayeast         | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
 | polandcentral      | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
 | southafricanorth   | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| southcentralus     | -                          | -                       | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
+| southcentralus     | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
 | southindia         | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
 | spaincentral       | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
 | swedencentral      | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                                        |
 | switzerlandnorth   | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
 | uksouth            | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
 | westeurope         | -                          | -                       | ✅                            | ✅                       | -                      | ✅                            | -                                       |
-| westus             | -                          | -                       | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
-| westus3            | -                          | -                       | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
+| westus             | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
+| westus3            | ✅                           | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | -                                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの標準グローバルマトリックスの更新"
}
```

### Explanation
このコードの変更は、OpenAIのモデルに関する標準グローバルマトリックスを更新するためのもので、特に各地域のモデルサポート状況が見直されています。変更された内容は、特定の地域におけるサポートの可否を示すチェックマークの追加または削除に関連しています。

具体的には、以下の地域に対してチェックマークが追加されました：
- `eastus`: 以前は未サポートとされていましたが、今回の変更によりサポートされることになりました。
- `northcentralus`, `southcentralus`, `westus`, `westus3`: これらの地域でも同様に、サポートが明示的に確認され、チェックマークが追加されました。

この変更により、ユーザーは各地域におけるモデルの利用可能性についての最新情報を得ることができ、サービスの計画や設定に役立つことが期待されます。また、すべての更新は、ドキュメントがより正確で有用な情報を提供することを目指しています。

## articles/ai-services/openai/includes/model-matrix/standard-models.md{#item-af04c4}

<details>
<summary>Diff</summary>
````diff
@@ -13,18 +13,19 @@ ms.date: 10/04/2024
 | australiaeast    | -                          | -                       | ✅                | ✅                        | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | ✅                  | -                  | -                  | -            | -               | -                |
 | brazilsouth      | -                          | -                       | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
 | canadaeast       | -                          | -                       | ✅                | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| eastus           | -                          | -                       | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | ✅                  | -                  | -                  | -            | -               | -                |
+| eastus           | ✅                           | ✅                        | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | ✅                  | -                  | -                  | -            | -               | -                |
 | eastus2          | ✅                           | ✅                        | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | francecentral    | -                          | -                       | ✅                | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | ✅                    | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
 | japaneast        | -                          | -                       | -               | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | -                   | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| northcentralus   | -                          | -                       | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
+| northcentralus   | ✅                           | ✅                        | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
 | norwayeast       | -                          | -                       | -               | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | southafricanorth | -                          | -                       | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
-| southcentralus   | -                          | -                       | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | ✅                       | -                      | -                      | ✅                       | -                          | -                               | ✅                              | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
+| southcentralus   | ✅                           | ✅                        | -               | -                       | ✅                        | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | ✅                       | -                      | -                      | ✅                       | -                          | -                               | ✅                              | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
 | southindia       | -                          | -                       | -               | ✅                        | -                       | -                         | -                           | -                      | -                      | -                           | -                   | -                      | -                      | ✅                       | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | swedencentral    | ✅                           | ✅                        | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           | ✅                                | -                             | ✅                              | -                             | ✅                              | -                 | ✅                  | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
 | switzerlandnorth | -                          | -                       | ✅                | -                       | -                       | ✅                          | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       | -                      | -                      | ✅                           | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
 | uksouth          | -                          | -                       | -               | ✅                        | ✅                        | -                         | -                           | -                      | -                      | -                           | -                   | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
 | westeurope       | -                          | -                       | -               | -                       | -                       | -                         | -                           | -                      | -                      | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| westus           | -                          | -                       | -               | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
-| westus3          | -                          | -                       | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| westus           | ✅                           | ✅                        | -               | ✅                        | -                       | ✅                          | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
+| westus3          | ✅                           | ✅                        | -               | ✅                        | -                       | -                         | ✅                            | ✅                       | ✅                       | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準モデルのマトリックスの更新"
}
```

### Explanation
このコードの変更は、OpenAIの標準モデルに関するマトリックスを更新するためのもので、特にモデルのサポート状況や設定内容に関して、いくつかの地域に対する情報が修正されています。

具体的な変更点は以下の通りです：
- 各地域におけるモデルの利用状況に対して、チェックマークが追加または削除されており、特に`eastus`、`northcentralus`、`southcentralus`、`westus`、`westus3`の各地域で新たにサポートが確立されたことが示されています。
- これにより、以前はサポートされていなかったモデルが、これらの地域で使用可能になったことを示しています。

この変更は、ユーザーが利用可能なモデルを計画し、適切な地域でリソースを展開する際に役立つ重要な情報を提供します。また、ドキュメンテーションが刷新され、最新の状態を反映していることを示します。これにより、ユーザーは自分のニーズに合ったモデルをより効果的に選択できるようになります。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 08/21/2024
+ms.date: 10/10/2024
 ms.author: mbullwin
 ---
 
@@ -66,10 +66,10 @@ The following sections provide you with a quick guide to the default quotas and
 
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
 |---|---|:---:|:---:|
-| `o1-preview` | Enterprise agreement | 15 M | 2.5 K |
+| `o1-preview` | Enterprise agreement | 30 M | 5 K |
 | `o1-mini`| Enterprise agreement | 50 M | 5 K |
-| `o1-preview` | Default | 1.5 M | 250 |
-| `o1-mini`| Default | 1 M | 100 |
+| `o1-preview` | Default | 3 M | 500 |
+| `o1-mini`| Default | 5 M | 500 |
 
 ### o1-preview & o1-mini standard
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータと制限の更新"
}
```

### Explanation
このコードの変更は、OpenAIのクォータと制限に関するドキュメントを更新するためのもので、特にモデルに対する制限が見直されています。変更された内容は、モデルごとのトークンおよびリクエストの制限を明確に示しています。

具体的には、以下の点が更新されました：
- `o1-preview`モデルの「エンタープライズ契約」におけるトークン制限が15百万から30百万に引き上げられ、リクエスト制限も2,500から5,000に増加しています。
- `o1-preview`モデルの「デフォルト」におけるトークン制限は1.5百万から3百万に、リクエスト制限は250から500にそれぞれ増加しました。
- また、`o1-mini`モデルに関しても、デフォルトのトークン制限が1百万から5百万に増加し、リクエスト制限が100から500に引き上げられました。

これらの変更により、ユーザーは各モデルの利用可能なリソースと制約について、より正確で最新の情報を得られるようになります。特に、大規模なリクエストを行うユーザーにとっては、より柔軟な使用が可能となることが期待されます。また、最終更新日も2024年10月に更新されています。

## articles/ai-services/openai/realtime-audio-quickstart.md{#item-727df8}

<details>
<summary>Diff</summary>
````diff
@@ -23,7 +23,7 @@ Most users of the Realtime API need to deliver and receive audio from an end-use
 
 Currently only `gpt-4o-realtime-preview` version: `2024-10-01-preview` supports real-time audio.
 
-The `gpt-4o-realtime-preview` model is available for global deployments in [East US 2 and Sweden Central regions](../concepts/models.md#global-standard-model-availability).
+The `gpt-4o-realtime-preview` model is available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability).
 
 > [!IMPORTANT]
 > The system stores your prompts and completions as described in the "Data Use and Access for Abuse Monitoring" section of the service-specific Product Terms for Azure OpenAI Service, except that the Limited Exception does not apply. Abuse monitoring will be turned on for use of the `gpt-4o-realtime-preview` API even for customers who otherwise are approved for modified abuse monitoring.
@@ -38,13 +38,13 @@ Support for the Realtime API was first added in API version `2024-10-01-preview`
 ## Prerequisites
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
-- An Azure OpenAI resource created in a [supported region](#supported-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+- An Azure OpenAI resource created in a [supported region](#supported-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](./how-to/create-resource.md).
 
 ## Deploy a model for real-time audio
 
 Before you can use GPT-4o real-time audio, you need a deployment of the `gpt-4o-realtime-preview` model in a supported region as described in the [supported models](#supported-models) section.
 
-You can deploy the model from the [Azure AI Studio model catalog](../../../ai-studio/how-to/model-catalog-overview.md) or from your project in AI Studio. Follow these steps to deploy a `gpt-4o-realtime-preview` model from the model catalog:
+You can deploy the model from the [Azure AI Studio model catalog](../../ai-studio/how-to/model-catalog-overview.md) or from your project in AI Studio. Follow these steps to deploy a `gpt-4o-realtime-preview` model from the model catalog:
 
 1. Sign in to [AI Studio](https://ai.azure.com) and go to the **Home** page.
 1. Select **Model catalog** from the left sidebar.
@@ -71,13 +71,13 @@ To chat with your deployed `gpt-4o-realtime-preview` model in the [Azure AI Stud
 1. Select your deployed `gpt-4o-realtime-preview` model from the **Deployment** dropdown. 
 1. Select **Enable microphone** to allow the browser to access your microphone. If you already granted permission, you can skip this step.
 
-    :::image type="content" source="../media/how-to/real-time/real-time-playground.png" alt-text="Screenshot of the real-time audio playground with the deployed model selected." lightbox="../media/how-to/real-time/real-time-playground.png":::
+    :::image type="content" source="./media/how-to/real-time/real-time-playground.png" alt-text="Screenshot of the real-time audio playground with the deployed model selected." lightbox="./media/how-to/real-time/real-time-playground.png":::
 
 1. Optionally you can edit contents in the **Give the model instructions and context** text box. Give the model instructions about how it should behave and any context it should reference when generating a response. You can describe the assistant's personality, tell it what it should and shouldn't answer, and tell it how to format responses.
 1. Optionally, change settings such as threshold, prefix padding, and silence duration.
 1. Select **Start listening** to start the session. You can speak into the microphone to start a chat.
 
-    :::image type="content" source="../media/how-to/real-time/real-time-playground-start-listening.png" alt-text="Screenshot of the real-time audio playground with the start listening button and microphone access enabled." lightbox="../media/how-to/real-time/real-time-playground-start-listening.png":::
+    :::image type="content" source="./media/how-to/real-time/real-time-playground-start-listening.png" alt-text="Screenshot of the real-time audio playground with the start listening button and microphone access enabled." lightbox="./media/how-to/real-time/real-time-playground-start-listening.png":::
 
 1. You can interrupt the chat at any time by speaking. You can end the chat by selecting the **Stop listening** button.
 
@@ -129,5 +129,5 @@ You can run the sample code locally on your machine by following these steps. Re
 
 ## Related content
 
-* Learn more about Azure OpenAI [deployment types](./deployment-types.md)
-* Learn more about Azure OpenAI [quotas and limits](../quotas-limits.md)
+* Learn more about Azure OpenAI [deployment types](./how-to/deployment-types.md)
+* Learn more about Azure OpenAI [quotas and limits](quotas-limits.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオクイックスタートの名前変更"
}
```

### Explanation
このコードの変更は、OpenAIのリアルタイムオーディオ機能に関するクイックスタートガイドのファイル名を変更し、いくつかのリンクを更新するために行われました。元のファイル名は`audio-real-time.md`から`realtime-audio-quickstart.md`に変更されました。

具体的な変更点は以下の通りです：
- ファイル内のリンクが適切な相対パスに更新され、ドキュメント内での参照が正しく機能するように修正されています。これにより、ユーザーは関連情報にスムーズにアクセスできるようになります。
- 特に、`gpt-4o-realtime-preview`モデルに関して、利用可能な地域の情報やリアルタイムオーディオのデプロイ手順が引き続き提供されていますが、その情報へのリンクのパスが統一されています。

この変更により、ドキュメントの整合性が向上し、ユーザーがリアルタイムオーディオAPIを効果的に利用するための情報がより見やすくなっています。また、関連するリソースへのアクセスが改善され、使用するモデルやクォータについてよりわかりやすく案内されています。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -38,6 +38,8 @@ items:
       href: dall-e-quickstart.md
     - name: Use your data
       href: use-your-data-quickstart.md
+    - name: Realtime API for speech and audio (preview)
+      href: realtime-audio-quickstart.md
     - name: Whisper model
       href: whisper-quickstart.md
     - name: Text to speech (preview)
@@ -162,8 +164,6 @@ items:
       - name: Function calling
         href: ./how-to/fine-tuning-functions.md
         displayName: fine-tuning, finetuning
-  - name: Realtime API for speech and audio (Preview)
-    href: ./how-to/audio-real-time.md
   - name: Use your data
     items:
       - name: Text data
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新"
}
```

### Explanation
このコードの変更は、OpenAIに関連するドキュメントの目次ファイル（toc.yml）の更新に関するもので、特にリアルタイムAPIに関する情報が反映されています。

具体的な変更点は以下の通りです：
- 目次に「Realtime API for speech and audio (preview)」という新しい項目が追加され、これに関連するクイックスタートガイドへのリンク（`realtime-audio-quickstart.md`）が設けられました。これにより、ユーザーはリアルタイムAPIに関する情報に迅速にアクセスできるようになります。
- 以前の目次項目であった「Realtime API for speech and audio (Preview)」が削除され、そのリンクが新しいガイドに統合されています。この変更により、重複を避けると共に、目次が整理されました。

全体として、この変更はドキュメントの可読性を向上させ、ユーザーが必要な情報を効果的に見つけるための手助けとなります。また、最新の機能に関する情報が強調され、ユーザーがリアルタイムオーディオAPIについての理解を深めやすくなっています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -44,7 +44,7 @@ Azure OpenAI GPT-4o audio is part of the GPT-4o model family that supports low-l
 
 The `gpt-4o-realtime-preview` model is available for global deployments in [East US 2 and Sweden Central regions](./concepts/models.md#global-standard-model-availability).
 
-For more information, see the [GPT-4o real-time audio documentation](./how-to/audio-real-time.md).
+For more information, see the [GPT-4o real-time audio documentation](realtime-audio-quickstart.md).
 
 ### Global batch support updates
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいリアルタイムオーディオドキュメントへのリンク更新"
}
```

### Explanation
このコードの変更は、OpenAIの新着情報を記載したドキュメント（whats-new.md）の更新に関連しています。具体的には、リアルタイムオーディオに関するドキュメントへのリンクが修正されました。

具体的な変更点は以下の通りです：
- リアルタイムオーディオに関する情報へのリンクが「./how-to/audio-real-time.md」から「realtime-audio-quickstart.md」に更新されました。この変更により、ユーザーが直接新しいクイックスタートガイドにアクセスできるようになります。
- 変更は1行の追加と1行の削除を伴い、全体的な情報の構造が整理されました。

この更新は、ユーザーが最新の情報に簡単にアクセスできるようにするためのもので、リアルタイムオーディオの理解を深める助けになります。


