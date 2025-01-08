---
date: '2025-01-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7840f69...MicrosoftDocs:058aad5
summary: 新機能として、AIモデル情報の追加と地域情報の更新により、ユーザーはモデルの地域での可用性をより理解しやすくなりました。Breaking Changesでは、「Azure
  OpenAI Studio」が「Azure AI Foundry」に名称変更され、現行のサービス名に基づいた正確な情報が提供されます。その他の更新では、プロンプトキャッシングサポートモデルの更新と画像ファイルのメタデータ修正が行われ、最新の情報が反映されています。この変更は主にAzure
  AI関連のドキュメントの 正確性を向上させ、エンドユーザーが利用可能なモデルの理解を深めることを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7840f69...MicrosoftDocs:058aad5){target="_blank"}

# ハイライト

- **新機能**: AIモデル情報の追加と地域情報の更新により、ユーザーはモデルの地域での可用性についてより理解しやすくなっています。
- **Breaking Changes**: Azure OpenAI StudioからAzure AI Foundryへの移行に伴う名称変更。
- **その他の更新**: プロンプトキャッシングサポートモデルの更新と画像ファイルのメタデータ変更。

## 新機能
- モデルの地域可用性を示す表の改善により、ユーザーは特定の地域で使用できるモデルを簡単に把握できるようになりました。

## Breaking Changes
- ドキュメント内の「Azure OpenAI Studio」がすべて「Azure AI Foundry」に変更され、サービスの移行に伴う名称変更が行われています。これによりユーザーは現在使用可能なサービス名に基づいて正確な情報を得ることができます。

## その他の更新
- 古いモデルの削除と新しいモデルの追加により、プロンプトキャッシングサポートモデルのリストが最新の状態になっています。
- 画像ファイルのメタデータが微修正され、ドキュメント内での正確な使用がサポートされています。画像の表示そのものには変更はありません。

# インサイト

この変更は、主にAzure AI関連のドキュメントの正確さと現行のサービス名に即した更新を行うことを目的としています。特に、「Azure OpenAI Studio」という旧名称から「Azure AI Foundry」への切り替えは、クラウドサービスが進化する中で最新のプラットフォームを利用する際の混乱を避けるためになされています。これにより、ユーザーはAIサービス利用時により整合性の取れた情報を得られるでしょう。

技術的には、新しいAIモデルや地域サポートに関する情報の追加は、エンドユーザーがどのモデルをどこで使えるのかを理解するための重要な要素です。また、プロンプトキャッシングにおけるモデルの更新は、ユーザーが最適なパフォーマンスを引き出せるよう支援する内容といえます。これらの更新を通じて、ユーザーはAIサービスの機能を一層活用できるようになるでしょう。

さらに、画像ファイルの微細なメタデータ更新は、ドキュメントの正確性および整合性を保つ上で重要です。特に、視覚要素が多く含まれる技術文書においては、画像の適切な使用が情報伝達の鍵となります。このような些細な更新でも、全体の品質を維持するために重要です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | AIモデルの更新と地域情報の改善 | modified | 19 | 12 | 31 | 
| [assistants-logic-apps.md](#item-57ae37) | minor update | Azure AI Foundryへの移行に関する詳細更新 | modified | 11 | 14 | 25 | 
| [prompt-caching.md](#item-1631df) | minor update | プロンプトキャッシングのサポートモデル更新 | modified | 1 | 1 | 2 | 
| [assistants-playground-add-function.png](#item-65f602) | minor update | 画像ファイルのメタデータ更新 | modified | 0 | 0 | 0 | 
| [import-logic-apps.png](#item-2c6611) | minor update | 画像ファイルのメタデータ更新 | modified | 0 | 0 | 0 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -347,18 +347,25 @@ These models can only be used with Embedding API requests.
 
 For Assistants you need a combination of a supported model, and a supported region. Certain tools and capabilities require the latest models. The following models are available in the Assistants API, SDK, and Azure AI Foundry. The following table is for pay-as-you-go. For information on Provisioned Throughput Unit (PTU) availability, see [provisioned throughput](./provisioned-throughput.md). The listed models and regions can be used with both Assistants v1 and v2. You can use [global standard models](#global-standard-model-availability) if they are supported in the regions listed below. 
 
-| Region | `gpt-35-turbo (0613)` | `gpt-35-turbo (1106)`| `fine tuned gpt-3.5-turbo-0125` | `gpt-4 (0613)` | `gpt-4 (1106)` | `gpt-4 (0125)` | `gpt-4o (2024-05-13)` | `gpt-4o-mini (2024-07-18)` |
-|-----|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
-| Australia East | ✅ | ✅ | | ✅ |✅ | | | |
-| East US  | ✅ | | | | | ✅ | ✅ |✅|
-| East US 2 | ✅ |  | ✅ | ✅ |✅ | |✅| |
-| France Central  | ✅ | ✅ | | ✅ |✅ |  | | |
-| Japan East | ✅ |  | | | | | | |
-| Norway East | |  | | | ✅ |  | | |
-| Sweden Central | ✅ |✅ | ✅ |✅ |✅| |✅| |
-| UK South | ✅  | ✅ | | | ✅ | ✅ |  | |
-| West US |  | ✅ | | | ✅ | |✅| |
-| West US 3 |  |  | | |✅ | |✅| |
+
+| **Region**   |  **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**    | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**  | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   | **gpt-35-turbo-16k**, **0613**   |
+|:-----------------|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:------------------------------:|
+| australiaeast    | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                           | ✅                    | ✅                       | ✅                       | ✅                       | ✅                           |
+| canadaeast       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                           | ✅                    | ✅                       | ✅                       | ✅                       | ✅                           |
+| eastus           | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        |  ✅                            | -                   | ✅                       | -                      | ✅                       | ✅                           |
+| eastus2          | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      | ✅                       | ✅                           |
+| francecentral    | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                           | ✅                    | ✅                       | ✅                       | -                      | ✅                           |
+| japaneast        | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | ✅                       | -                      | ✅                       | ✅                           |
+| northcentralus   | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | ✅                            | -                   | ✅                       | -                      | ✅                       | ✅                           |
+| norwayeast       | -                      | -                      | -                           | -               | ✅                        | -                       |  -                           | -                   | -                      | -                      | -                      | -                          |
+| southcentralus   | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                       | ✅                            | -                   | -                      | -                      | ✅                       | -                          |
+| southindia       | -                      | -                      | -                           | -               | ✅                        | -                       | -                           | -                   | -                      | ✅                       | ✅                       | -                          |
+| swedencentral    | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                            | ✅                    | ✅                       | ✅                       | -                      | ✅                           |
+| switzerlandnorth | -                      | -                      | -                           | ✅                | -                       | -                       |  -                           | ✅                    | ✅                       | -                      | ✅                       | ✅                           |
+| uksouth          | -                      | -                      | -                           | -               | ✅                        | ✅                        | -                           | -                   | ✅                       | ✅                       | ✅                       | ✅                           |
+| westeurope       | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | -                      | -                      | -                      | -                          |
+| westus           | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       |✅                            | -                   | -                      | ✅                       | ✅                       | -                          |
+| westus3          | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | ✅                            | -                   | -                      | -                      | ✅                       | -                          |
 
 ## Model retirement
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIモデルの更新と地域情報の改善"
}
```

### Explanation
この変更は、「models.md」ドキュメントに対して行われた軽微な更新を示しています。具体的には、さまざまなAIモデルとその利用可能な地域に関する情報が追加され、表の構成が改善されました。新しいモデルやそのバージョンが、さまざまな地域でどのようにサポートされるかを視覚的に示すために、表の内容が更新されています。

追加された内容には、新しいモデル名やバージョン情報が含まれ、それぞれの地域におけるサポート状況が詳細に記載されています。これにより、ユーザーが必要なモデルを特定の地域で簡単に利用できるかどうかを理解しやすくなります。

また、モデルの引退に関するセクションも新たに追加されており、どのモデルが使用できなくなるかの情報も提供されることで、ユーザーが将来的な計画を立てる際に役立つよう配慮されています。この変更は、文書全体の理解を助け、新技術に適応できるようにすることを目的としています。

## articles/ai-services/openai/how-to/assistants-logic-apps.md{#item-57ae37}

<details>
<summary>Diff</summary>
````diff
@@ -14,9 +14,6 @@ recommendations: false
 
 # Call Azure Logic apps as functions using Azure OpenAI Assistants 
 
-> [!NOTE]
-> This functionality is currently only available in Azure OpenAI Studio.
-
 [Azure Logic Apps](https://azure.microsoft.com/products/logic-apps) is an integration platform in Azure that allows you to build applications and automation workflows with low code tools enabling developer productivity and faster time to market. By using the visual designer and selecting from hundreds of prebuilt connectors, you can quickly build a workflow that integrates and manages your apps, data, services, and systems.
 
 Azure Logic Apps is fully managed by Microsoft Azure, which frees you from worrying about hosting, scaling, managing, monitoring, and maintaining solutions built with these services. When you use these capabilities to create [serverless](/azure/logic-apps/logic-apps-overview) apps and solutions, you can just focus on the business logic and functionality. These services automatically scale to meet your needs, make automation workflows faster, and help you build robust cloud apps using little to no code.
@@ -31,7 +28,7 @@ The Assistants playground enumerates and lists all the workflows in your subscri
 * [Request trigger](/azure/connectors/connectors-native-reqres?tabs=consumption): Function calling requires a REST-based API. Logic Apps with a request trigger provides a REST endpoint. Therefore only workflows with a request trigger are supported for function calling.
 * Schema: The workflows you want to use for function calling should have a JSON schema describing the inputs and expected outputs. Using Logic Apps you can streamline and provide schema in the trigger, which would be automatically imported as a function definition.
 
-If you already have workflows with above three requirements, you should be able to use them in Azure OpenAI Studio  and invoke them via user prompts.
+If you already have workflows with above three requirements, you should be able to use them in Azure AI Foundry and invoke them via user prompts.
 If you do not have existing workflows, you can follow the steps in this article to create them. There are two primary steps:
 1. [Create a Logic App on Azure portal](#create-logic-apps-workflows-for-function-calling).
 2. [Import your Logic Apps workflows as a function in the Assistants Playground](#import-your-logic-apps-workflows-as-functions).
@@ -50,7 +47,7 @@ Here are the steps to create a new Logic Apps workflow for function calling.
 1. After Azure successfully deploys your logic app resource, select **Go to resource**. Or, find and select your logic app resource by typing the name in the Azure search box.
 1. Open the Logic Apps workflow in designer. Select Development Tools + Logic app designer. This opens your empty workflow in designer. Or you select Blank Logic App from templates
 1. Now you're ready to add one more step in the workflow. A workflow always starts with a single trigger, which specifies the condition to meet before running any subsequent actions in the workflow.
-1. Your workflow is required to have a Request trigger to generate a REST endpoint, and a response action to return the response to Azure OpenAI Studio  when this workflow is invoked.
+1. Your workflow is required to have a Request trigger to generate a REST endpoint, and a response action to return the response to Azure AI Foundry when this workflow is invoked.
 1. Add a trigger [(Request)](/azure/connectors/connectors-native-reqres?tabs=consumption)
 
     Select **Add a trigger** and then search for request trigger. Select the **When a HTTP request is received** operation.
@@ -61,7 +58,7 @@ Here are the steps to create a new Logic Apps workflow for function calling.
 
     :::image type="content" source="..\media\how-to\assistants\logic-apps\create-logic-app-2.png" alt-text="A screenshot showing the option to provide a JSON schema." lightbox="..\media\how-to\assistants\logic-apps\create-logic-app-2.png":::
 
-    Here is an example of the request schema. You can add a description for your workflow in the comment box. This is imported by Azure OpenAI Studio  as the function description.
+    Here is an example of the request schema. You can add a description for your workflow in the comment box. This is imported by Azure AI Foundry as the function description.
     
     :::image type="content" source="..\media\how-to\assistants\logic-apps\create-logic-app-3.png" alt-text="A screenshot showing an example request schema." lightbox="..\media\how-to\assistants\logic-apps\create-logic-app-3.png":::
 
@@ -77,22 +74,22 @@ Here are the steps to create a new Logic Apps workflow for function calling.
 
     :::image type="content" source="..\media\how-to\assistants\logic-apps\create-logic-app-6.png" alt-text="A screenshot showing the location property." lightbox="..\media\how-to\assistants\logic-apps\create-logic-app-6.png":::
 
-1. Configure the [response](/azure/connectors/connectors-native-reqres#add-a-response-action). The workflow needs to return the response back to Azure OpenAI Studio. This is done using Response action.
+1. Configure the [response](/azure/connectors/connectors-native-reqres#add-a-response-action). The workflow needs to return the response back to Azure AI Foundry. This is done using Response action.
 
     :::image type="content" source="..\media\how-to\assistants\logic-apps\create-logic-app-7.png" alt-text="A screenshot showing the response action." lightbox="..\media\how-to\assistants\logic-apps\create-logic-app-7.png":::
 
      In the response action, you can pick the output from any of the prior steps. You can optionally also provide a JSON schema if you want to return the output in a specific format.
     
     :::image type="content" source="..\media\how-to\assistants\logic-apps\create-logic-app-7.png" alt-text="A screenshot showing the comment box to specify a JSON schema." lightbox="..\media\how-to\assistants\logic-apps\create-logic-app-7.png":::
 
-1. The workflow is now ready. In Azure OpenAI Studio, you can import this function using the **Add function** feature in the Assistants playground.
+1. The workflow is now ready. In Azure AI Foundry, you can import this function using the **Add function** feature in the Assistants playground.
 
 
 ## Import your Logic Apps workflows as functions
 
-Here are the steps to import your Logic Apps workflows as function in the Assistants playground in Azure OpenAI Studio:
+Here are the steps to import your Logic Apps workflows as function in the Assistants playground in Azure AI Foundry:
 
-1. In Azure OpenAI Studio, select **Assistants**. Select an existing Assistant or create a new one. After you have configured the assistant with a name and instructions, you are ready to add a function. Select **+ Add function**. 
+1. In Azure AI Foundry, select **Playgrounds** from the left navigation menu, and then **Assistants playground**. Select an existing Assistant or create a new one. After you have configured the assistant with a name and instructions, you are ready to add a function. Select **+ Add function**. 
 
     :::image type="content" source="..\media\how-to\assistants\logic-apps\assistants-playground-add-function.png" alt-text="A screenshot showing the Assistant playground with the add function button." lightbox="..\media\how-to\assistants\logic-apps\assistants-playground-add-function.png":::
 
@@ -123,11 +120,11 @@ You can confirm the invocation by looking at the logs as well as your [workflow
 
 Azure Logic Apps has connectors to hundreds of line-of-business (LOB) applications and databases including but not limited to: SAP, Salesforce, Oracle, SQL, and more. You can also connect to SaaS applications or your in-house applications hosted in virtual networks. These out of box connectors provide operations to send and receive data in multiple formats. Leveraging these capabilities with Azure OpenAI assistants, you should be able to quickly bring your data for Intelligent Insights powered by Azure OpenAI.
 
-**What happens when a Logic Apps is imported in Azure OpenAI Studio  and invoked**
+**What happens when a Logic Apps is imported in Azure AI Foundry  and invoked**
 
-The Logic Apps swagger file is used to populate function definitions. Azure Logic App publishes an OpenAPI 2.0 definition (swagger) for workflows with a request trigger based on [annotations on the workflow](/rest/api/logic/workflows/list-swagger). Users are able to modify the content of this swagger by updating their workflow. Azure OpenAI Studio  uses this to generate the function definitions that the Assistant requires.  
+The Logic Apps swagger file is used to populate function definitions. Azure Logic App publishes an OpenAPI 2.0 definition (swagger) for workflows with a request trigger based on [annotations on the workflow](/rest/api/logic/workflows/list-swagger). Users are able to modify the content of this swagger by updating their workflow. Azure AI Foundry uses this to generate the function definitions that the Assistant requires.  
 
-**How does authentication from Azure OpenAI Studio  to Logic Apps work?**
+**How does authentication from Azure AI Foundry to Logic Apps work?**
 
 Logic Apps supports two primary types of authentications to invoke a request trigger.
 
@@ -139,7 +136,7 @@ Logic Apps supports two primary types of authentications to invoke a request tri
 
     Logic Apps also supports authentication trigger invocations with Microsoft Entra ID OAuth, where you can specify authentication policies to be used in validating OAuth tokens. For more information, see the [Logic Apps documentation](/azure/logic-apps/logic-apps-securing-a-logic-app#generate-shared-access-signatures-sas).
 
-When Azure OpenAI Assistants require invoking a Logic App as part of function calling, Azure OpenAI Studio  will retrieve the callback URL with the SAS to invoke the workflow. 
+When Azure OpenAI Assistants require invoking a Logic App as part of function calling, Azure AI Foundry will retrieve the callback URL with the SAS to invoke the workflow. 
 
 ## See also
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryへの移行に関する詳細更新"
}
```

### Explanation
この変更は、「assistants-logic-apps.md」ドキュメントに対して行われた軽微な更新を示しています。主な変更は、Azure OpenAI StudioからAzure AI Foundryへの移行に関連する情報の更新です。各所で「Azure OpenAI Studio」という表現が「Azure AI Foundry」に変更され、内容が調整されました。

変更点には、Azure Logic Appsとその利用方法に関する情報が含まれています。具体的には、Logic Appsの作成手順や、ユーザーが持っているワークフローをAzure AI Foundry内でどのように操作できるかに関して説明が更新されています。また、Azureでのサーバーレスアプリケーション作成時に必要な要件についても明示されています。

これにより、ユーザーは新しいプラットフォームでの機能の呼び出し方や、Azure AI Foundryにおけるワークフローの取り扱いについてより正確な情報を得ることができるようになります。全体として、文書は最新のプラットフォームに即した内容となり、利用者の理解を深めやすくなることを目指しています。

## articles/ai-services/openai/how-to/prompt-caching.md{#item-1631df}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ Currently only the following models support prompt caching with Azure OpenAI:
 - `o1-2024-12-17`
 - `o1-preview-2024-09-12`
 - `o1-mini-2024-09-12`
-- `gpt-4o-2024-05-13`
+- `gpt-4o-2024-11-20`
 - `gpt-4o-2024-08-06`
 - `gpt-4o-mini-2024-07-18`
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトキャッシングのサポートモデル更新"
}
```

### Explanation
この変更は、「prompt-caching.md」ドキュメントに対して行われた軽微な更新を示しています。具体的には、Azure OpenAIによるプロンプトキャッシングをサポートしているモデルに関する情報が更新されました。

変更内容としては、プロンプトキャッシングをサポートするモデルのリストから、古いモデル「gpt-4o-2024-05-13」が削除され、新しいモデル「gpt-4o-2024-11-20」が追加されました。これにより、ユーザーは最新のモデルを利用したプロンプトキャッシングの使用が可能であることが明確に示されています。

この更新は、利用者がどのモデルを使用できるかを正確に把握できるようにするためのもので、最新の情報に基づいて機能を最大限に活用することを支援します。

## articles/ai-services/openai/media/how-to/assistants/logic-apps/assistants-playground-add-function.png{#item-65f602}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルのメタデータ更新"
}
```

### Explanation
この変更は、「assistants-playground-add-function.png」という画像ファイルに関する更新を示しています。具体的には、画像ファイル自体には追加や削除は行われていないものの、ファイルのメタデータや関連情報が何らかの形で更新された可能性があります。

変更内容には、画像が含まれる文脈や使用される文書内での取り扱いが影響される可能性がありますが、具体的な内容は記載されていないため、ユーザーにとっては直接的な変更には至っていないと考えられます。このような更新は、画像の正確な表示や関連するドキュメントとの整合性を保持するために行われることがあります。

## articles/ai-services/openai/media/how-to/assistants/logic-apps/import-logic-apps.png{#item-2c6611}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルのメタデータ更新"
}
```

### Explanation
この変更は、「import-logic-apps.png」という画像ファイルに関するもので、ファイル自体に対する具体的な追加や削除はありませんでしたが、何らかの形式でメタデータが更新された可能性があります。画像ファイルの変更状態は「modified」とされていますが、実際のコンテンツには影響を与えない変更内容です。

このような更新は、ドキュメントや関連資料内での画像の正確な使用を助けるために行われることがあり、今回の更新も画像を使用する文書との整合性を保つためのものであると考えられます。ユーザーにとっては、直接的な視覚的変更は無いものの、使用されるコンテキストにおいて重要な役割を果たす可能性があります。


