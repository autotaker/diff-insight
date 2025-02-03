---
date: '2025-02-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5c1bed9...MicrosoftDocs:83a6833
summary: このコードの変更では、AzureのOpenAIに関するドキュメントが更新され、新機能の追加と重要な変更が行われました。新機能として、FAQに「GPT-4がどのように自分のモデルを識別するか」や「特定の言語で応答を得る方法」についての質問と回答が追加されました。一方、Azure
  Machine Learningに関連する資料が削除され、「azure-machine-learning.md」が完全に排除され、目次からのリンクや関連するインデックスの参照も削除されました。また、一部のFAQが整理され、表現が改善されています。この更新は、ユーザーに対してより明確で役立つ情報を提供することを目指しています。特に、Azure
  OpenAIにおけるデータソースの選び方に影響を与えるため、ユーザーには最新情報の追跡が重要です。全体として、Azureのサービスの有効性とユーザー体験の向上が期待されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5c1bed9...MicrosoftDocs:83a6833){target="_blank"}

# ハイライト

このコードの変更では、AzureのOpenAIに関するドキュメントに複数の更新が加えられています。新機能の追加と、いくつかの主要な変更点を以下に示します。

## 新機能

- FAQに、新たに「GPT-4がどのように自分のモデルを識別するか」や「特定の言語で応答を得る方法」についての質問と回答が追加されました。

## 重要な変更

- Azure Machine Learningに関連する資料が削除され、これは重大な変更とされています。具体的には、「azure-machine-learning.md」が完全に削除され、対応する目次からのリンクも削除。Azure Machine Learningインデックスの参照も削除され、他のデータソースに移行する必要があります。

## その他の更新

- 一部のFAQの質問が整理され、表現が改善されています。

# インサイト

このドキュメント更新は、AzureのオープンAIサービス利用者に対して、より明確で役立つ情報を提供することを目的としています。

FAQの更新では、新しい質問の追加により、ユーザーが直面する可能性のある具体的な疑問点に対する対応が強化されています。特に、特定の言語での応答やモデルの識別方法に関する詳細な情報の提供が含まれており、言語処理に重点を置いた更新といえます。

Azure Machine Learningに関連した資料の削除は、Azureがこちらのサービスを別の方向に再編する動きの一環だと考えられます。この変更はドキュメント全体の整合性を保つと同時に、ユーザーに対する最新のサポートを保証するために必須であるといえます。削除されたコンテンツは、これまでユーザーに特定の手順やコードサンプルを提供していたものであり、その情報が他のドキュメントに移行している可能性があるため、最新の情報を追跡することが重要です。

Azure OpenAIにおけるデータソースの選択肢がより限られるようになったことで、ユーザーがサポートされるデータソースを選定する際に見直しが必要となるでしょう。これらの変更により、Azure全体としてのサービスの有効性とユーザー体験が向上することが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [faq.yml](#item-6deb71) | minor update | FAQの更新と質問の追加 | modified | 28 | 18 | 46 | 
| [azure-machine-learning.md](#item-940a2b) | breaking change | Azure Machine Learningに関するドキュメントの削除 | removed | 0 | 167 | 167 | 
| [on-your-data.md](#item-c35b1e) | minor update | Azure Machine Learningインデックス参照の削除 | modified | 1 | 2 | 3 | 
| [toc.yml](#item-c945af) | minor update | Azure Machine Learningインデックスに関するリンクの削除 | modified | 0 | 2 | 2 | 


# Modified Contents
## articles/ai-services/openai/faq.yml{#item-6deb71}

<details>
<summary>Diff</summary>
````diff
@@ -64,22 +64,7 @@ sections:
           Where can I read about better ways to use Azure OpenAI to get the responses I want from the service?
         answer: | 
           Check out our [introduction to prompt engineering](./concepts/prompt-engineering.md). While these models are powerful, their behavior is also very sensitive to the prompts they receive from the user. This makes prompt construction an important skill to develop. After you've completed the introduction, check out our article on [system messages](./concepts/advanced-prompt-engineering.md).
-      - question: |
-          My guest account has been given access to an Azure OpenAI resource, but I'm unable to access that resource in the Azure AI Foundry portal. How do I enable access?
-        answer: | 
-          This is expected behavior when using the default sign-in experience for the [Azure AI Foundry](https://ai.azure.com).
-          
-          To access Azure AI Foundry from a guest account that has been granted access to an Azure OpenAI resource:
-          
-          1. Open a private browser session and then navigate to [https://ai.azure.com](https://ai.azure.com).
-          2. Rather than immediately entering your guest account credentials instead select `Sign-in options` 
-          3. Now select **Sign in to an organization** 
-          4. Enter the domain name of the organization that granted your guest account access to the Azure OpenAI resource. 
-          5. Now sign-in with your guest account credentials. 
-          
-          You should now be able to access the resource via the Azure AI Foundry portal.
-          
-          Alternatively if you're signed into the [Azure portal](https://portal.azure.com) from the Azure OpenAI resource's Overview pane you can select **Go to Azure AI Foundry** to automatically sign in with the appropriate organizational context.   
+      
       - question: |
           When I ask GPT-4 which model it's running, it tells me it's running GPT-3. Why does this happen?
         answer: | 
@@ -95,6 +80,15 @@ sections:
 
           To learn more about how GPT models are trained and work we recommend watching [Andrej Karpathy's talk from Build 2023 on the state of GPT](https://www.youtube.com/watch?v=bZQun8Y4L2A).
       
+      - question: |
+          How can I get the model to respond in a specific language?
+        answer: | 
+          Ensure that your prompt is clear and specific about the language requirement. If the issue persists, consider adding more context or rephrasing the prompt to reinforce the language instruction.
+
+          Example prompts:
+          * "Please respond in English and only in English."
+          * "Answer the following question in English: What is the weather like in Fresno?"
+          
       - question: |
           I asked the model when its knowledge cutoff is and it gave me a different answer than what is on the Azure OpenAI model's page. Why does this happen?
         answer:
@@ -121,7 +115,7 @@ sections:
           We noticed charges associated with API calls that failed to complete with status code 400. Why are failed API calls generating a charge? 
         answer:
           If the service performs processing, you will be charged even if the status code is not successful (not 200).
-          Common examples of this are, a 400 error due to a content filter or input limit, or a 408 error due to a timeout. Charges will also occur when a `status 200` is received with a `finish_reason` of `content_filter`.
+          Common examples of this are, a 400 error due to a content filter or input limit, or a 408 error due to a time-out. Charges will also occur when a `status 200` is received with a `finish_reason` of `content_filter`.
           In this case the prompt did not have any issues, but the completion generated by the model was detected to violate the content filtering rules, which result in the completion being filtered. 
 
           If the service doesn't perform processing, you won't be charged.
@@ -132,7 +126,23 @@ sections:
           How do I get access to Azure OpenAI? 
         answer: |
           A Limited Access registration form is not required to access most Azure OpenAI models. Learn more on the [Azure OpenAI Limited Access page](/legal/cognitive-services/openai/limited-access?context=/azure/ai-services/openai/context/context).
-
+      - question: |
+          My guest account has been given access to an Azure OpenAI resource, but I'm unable to access that resource in the Azure AI Foundry portal. How do I enable access?
+        answer: | 
+          This is expected behavior when using the default sign-in experience for the [Azure AI Foundry](https://ai.azure.com).
+          
+          To access Azure AI Foundry from a guest account that has been granted access to an Azure OpenAI resource:
+          
+          1. Open a private browser session and then navigate to [https://ai.azure.com](https://ai.azure.com).
+          2. Rather than immediately entering your guest account credentials instead select `Sign-in options` 
+          3. Now select **Sign in to an organization** 
+          4. Enter the domain name of the organization that granted your guest account access to the Azure OpenAI resource. 
+          5. Now sign-in with your guest account credentials. 
+          
+          You should now be able to access the resource via the Azure AI Foundry portal.
+          
+          Alternatively if you're signed into the [Azure portal](https://portal.azure.com) from the Azure OpenAI resource's Overview pane you can select **Go to Azure AI Foundry** to automatically sign in with the appropriate organizational context.   
+  
   - name: Learning more and where to ask questions
     questions:
       - question: |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQの更新と質問の追加"
}
```

### Explanation
このコードの変更は、OpenAIに関するFAQ（よくある質問）のYAMLファイルを更新するものであり、いくつかの新しい質問と回答の追加がなされています。追加された内容には、モデルがどのように特定の言語で応答できるかについての情報と、ゲストアカウントがAzure AI Foundryポータルへのアクセスを有効にする方法が含まれています。また、いくつかの既存の質問が整理され、回答の表現が改善されています。

具体的には、以下の内容が変更されています：
1. 「GPT-4がどのように自分のモデルを識別するか」に関する新しい質問が追加されました。
2. 「特定の言語で応答を得る方法」に関する明確なガイダンスが提供され、具体的な例も示されています。
3. ゲストアカウントのアクセスに関する手順が改訂され、一部の文が修正されています。

この更新は、ユーザーがAzure OpenAIサービスの利用に関してよりよく理解し、サポートを受けやすくするために行われました。

## articles/ai-services/openai/references/azure-machine-learning.md{#item-940a2b}

<details>
<summary>Diff</summary>
````diff
@@ -1,167 +0,0 @@
----
-title: Azure OpenAI on your Azure Machine Learning index data Python & REST API reference
-titleSuffix: Azure OpenAI
-description: Learn how to use Azure OpenAI on your Azure Machine Learning index data Python & REST API.
-manager: nitinme
-ms.service: azure-ai-openai
-ms.topic: conceptual
-ms.date: 01/28/2025
-author: aahill
-ms.author: aahi
-recommendations: false
-ms.custom: devx-track-python
----
-
-# Data source - Azure Machine Learning index (preview)
-
-The configurable options of Azure Machine Learning index when using Azure OpenAI On Your Data. This data source is supported in API version `2024-02-15-preview`.
-
-|Name | Type | Required | Description |
-|--- | --- | --- | --- |
-|`parameters`| [Parameters](#parameters)| True| The parameters to use when configuring Azure Machine Learning index.|
-| `type`| string| True | Must be `azure_ml_index`. |
-
-## Parameters
-
-|Name | Type | Required | Description |
-|--- | --- | --- | --- |
-| `project_resource_id` | string | True | The resource ID of the Azure Machine Learning project.|
-| `name` | string | True | The Azure Machine Learning index name.|
-| `version` | string | True | The version of the Azure Machine Learning index.|
-| `authentication`| One of [AccessTokenAuthenticationOptions](#access-token-authentication-options), [SystemAssignedManagedIdentityAuthenticationOptions](#system-assigned-managed-identity-authentication-options), [UserAssignedManagedIdentityAuthenticationOptions](#user-assigned-managed-identity-authentication-options) | True | The authentication method to use when accessing the defined data source. |
-| `in_scope` | boolean | False | Whether queries should be restricted to use of indexed data. Default is `True`.| 
-| `role_information`| string | False | Give the model instructions about how it should behave and any context it should reference when generating a response. You can describe the assistant's personality and tell it how to format responses.|
-| `strictness` | integer | False | The configured strictness of the search relevance filtering. The higher of strictness, the higher of the precision but lower recall of the answer. Default is `3`.| 
-| `top_n_documents` | integer | False | The configured top number of documents to feature for the configured query. Default is `5`. |
-| `filter`| string | False | Search filter. Only supported if the Azure Machine Learning index is of type Azure Search.|
-
-
-## Access token authentication options
-
-The authentication options for Azure OpenAI On Your Data when using access token.
-
-|Name | Type | Required | Description |
-|--- | --- | --- | --- |
-| `access_token`|string|True|The access token to use for authentication.|
-| `type`|string|True| Must be `access_token`.|
-
-## System assigned managed identity authentication options
-
-The authentication options for Azure OpenAI On Your Data when using a system-assigned managed identity.
-
-|Name | Type | Required | Description |
-|--- | --- | --- | --- |
-| `type`|string|True| Must be `system_assigned_managed_identity`.|
-
-## User assigned managed identity authentication options
-
-The authentication options for Azure OpenAI On Your Data when using a user-assigned managed identity.
-
-|Name | Type | Required | Description |
-|--- | --- | --- | --- |
-| `managed_identity_resource_id`|string|True|The resource ID of the user-assigned managed identity to use for authentication.|
-| `type`|string|True| Must be `user_assigned_managed_identity`.|
-
-## Examples
-
-Prerequisites:
-* Configure the role assignments from Azure OpenAI system assigned managed identity to Azure Machine Learning workspace resource. Required role: `AzureML Data Scientist`.
-* Configure the role assignments from the user to the Azure OpenAI resource. Required role: `Cognitive Services OpenAI User`.
-* Install [Az CLI](/cli/azure/install-azure-cli) and run `az login`.
-* Define the following environment variables: `AzureOpenAIEndpoint`, `ChatCompletionsDeploymentName`, `ProjectResourceId`, `IndexName`, `IndexVersion`.
-* Run `export MSYS_NO_PATHCONV=1` if you're using MINGW.
-```bash
-export AzureOpenAIEndpoint=https://example.openai.azure.com/
-export ChatCompletionsDeploymentName=turbo
-export ProjectResourceId='/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace-id}'
-export IndexName=testamlindex
-export IndexVersion=2
-```
-
-# [Python 1.x](#tab/python)
-
-Install the latest pip packages `openai`, `azure-identity`.
-
-```python
-import os
-from openai import AzureOpenAI
-from azure.identity import DefaultAzureCredential, get_bearer_token_provider
-
-endpoint = os.environ.get("AzureOpenAIEndpoint")
-deployment = os.environ.get("ChatCompletionsDeploymentName")
-project_resource_id = os.environ.get("ProjectResourceId")
-index_name = os.environ.get("IndexName")
-index_version = os.environ.get("IndexVersion")
-
-token_provider = get_bearer_token_provider(
-    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")
-
-client = AzureOpenAI(
-    azure_endpoint=endpoint,
-    azure_ad_token_provider=token_provider,
-    api_version="2024-02-15-preview",
-)
-
-completion = client.chat.completions.create(
-    model=deployment,
-    messages=[
-        {
-            "role": "user",
-            "content": "Who is DRI?",
-        },
-    ],
-    extra_body={
-        "data_sources": [
-            {
-                "type": "azure_ml_index",
-                "parameters": {
-                    "project_resource_id": project_resource_id,
-                    "name": index_name,
-                    "version": index_version,
-                    "authentication": {
-                        "type": "system_assigned_managed_identity"
-                    },
-                }
-            }
-        ]
-    }
-)
-
-print(completion.model_dump_json(indent=2))
-
-```
-
-# [REST](#tab/rest)
-
-```bash
-
-az rest --method POST \
- --uri $AzureOpenAIEndpoint/openai/deployments/$ChatCompletionsDeploymentName/chat/completions?api-version=2024-02-15-preview \
- --resource https://cognitiveservices.azure.com/ \
- --body \
-'
-{
-    "data_sources": [
-      {
-        "type": "azure_ml_index",
-        "parameters": {
-          "project_resource_id": "'$ProjectResourceId'",
-          "name": "'$IndexName'",
-          "version": "'$IndexVersion'",
-          "authentication": {
-            "type": "system_assigned_managed_identity"
-          },
-        }
-      }
-    ],
-    "messages": [
-      {
-        "role": "user",
-        "content": "Who is DRI?"
-      }
-    ]
-}
-'
-```
-
----
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azure Machine Learningに関するドキュメントの削除"
}
```

### Explanation
この変更は、Azure Machine Learningに関するドキュメントファイル（`azure-machine-learning.md`）を完全に削除するもので、内容としては、Azure OpenAIをAzure Machine Learningのインデックスデータに関連付けるためのPythonおよびREST APIのリファレンスが含まれていました。このドキュメントは167行が削除されており、実際の情報や例がすべて失われています。

具体的な内容としては、次のポイントが含まれていました：
- Azure Machine Learningインデックスを使用する際の設定オプションや必要な認証情報、APIの使い方についての詳細説明。
- あらゆる構成パラメータや認証方法の種類（システム割り当てられたマネージドアイデンティティやユーザー割り当てられたマネージドアイデンティティなど）の説明。
- サンプルコードの提供（PythonおよびREST APIの使用例）も含まれていました。

この削除は、Azureのドキュメンテーションの整理や内容の更新の一環として行われた可能性があり、利用者には特に影響を及ぼす重要な変更となります。他の場所に情報が統合または移動された場合、利用者は最新の情報を他の関連するドキュメントで確認する必要があります。

## articles/ai-services/openai/references/on-your-data.md{#item-c35b1e}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ POST {endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version=
 * `2024-05-01-preview` [Swagger spec](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2024-05-01-preview)
 
 > [!NOTE]
-> [Azure Machine learning indexes](./azure-machine-learning.md), [Pinecone](./pinecone.md), and [Elasticsearch](./elasticsearch.md) are supported as a preview.
+> [Pinecone](./pinecone.md), and [Elasticsearch](./elasticsearch.md) are supported as a preview.
 
 ## URI parameters
 
@@ -97,7 +97,6 @@ This list shows the supported data sources.
 
 * [Azure AI Search](./azure-search.md)
 * [Azure Cosmos DB for MongoDB vCore](./cosmos-db.md)
-* [Azure Machine Learning index (preview)](./azure-machine-learning.md)
 * [Elasticsearch (preview)](./elasticsearch.md)
 * [Pinecone (preview)](./pinecone.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Machine Learningインデックス参照の削除"
}
```

### Explanation
この変更は、Azure OpenAIに関するドキュメントである「on-your-data.md」を更新し、Azure Machine Learningインデックスの参照を削除します。具体的には、ドキュメント内の重要な注記から「Azure Machine Learningインデックス」の言及が削除され、他のデータソース（PineconeおよびElasticsearch）だけがプレビューとしてサポートされていることが示されるようになりました。

変更の詳細は以下の通りです：
- 注記セクションから「Azure Machine Learningインデックス」の記述が削除され、残りはPineconeおよびElasticsearchのみとなります。
- サポートされるデータソースのリストからも「Azure Machine Learningインデックス」の行が削除されました。

この変更は、Azure OpenAIのデータソースとしてAzure Machine Learningインデックスを使用することが廃止されたか、またはプレビューから除外されたことを示しており、ユーザーは他のリソースに移行する必要があるかもしれません。このように、ドキュメントが更新されることにより、ユーザーに最新のサポート情報を提供することができます。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -310,8 +310,6 @@ items:
           href: ./references/azure-search.md
         - name: Data source - Azure Cosmos DB for MongoDB vCore
           href: ./references/cosmos-db.md
-        - name: Data source - Azure Machine Learning index (preview)
-          href: ./references/azure-machine-learning.md
         - name: Data source - Elasticsearch (preview)
           href: ./references/elasticsearch.md
         - name: Data source - Pinecone (preview)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Machine Learningインデックスに関するリンクの削除"
}
```

### Explanation
この変更は、Azure OpenAIに関連するドキュメントの目次ファイル（`toc.yml`）を更新し、Azure Machine Learningインデックスに関する項目を削除します。具体的には、目次リストから「Data source - Azure Machine Learning index (preview)」の項目が取り除かれています。

この変更により、目次に表示されるデータソースのリンクが次のように更新されました：
- Azure Machine Learningインデックスの情報が削除され、ユーザーはもはやこのリソースを目次から直接探すことができません。
- 他のリソース、例えばAzure Cosmos DBやElasticsearch、Pineconeに関する項目は残り、引き続き利用可能です。

この更新は、Azure Machine Learningインデックスの関連情報がドキュメントから除外されたことを反映しており、ユーザーが最新のリソースやサポート情報を確認するうえで役立つことを目的としています。


