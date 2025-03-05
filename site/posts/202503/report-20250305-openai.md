---
date: '2025-03-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bf9270b...MicrosoftDocs:71adf7f
summary: このコード差分は、Azure OpenAIの機能強化に関するものであり、新しいモデルと詳細なドキュメントが追加され、既存の文書も更新されています。特に、ファインチューニングや安全性、トラブルシューティングに関するセクションが充実しました。新たに追加されたドキュメントは、ユーザーがAzure
  OpenAIの機能を効果的に活用できるよう支援します。また、ファインチューニング用のPython SDKドキュメントが大幅に更新され、最新の実装にフォーカスされています。さらに、目次やリンクの修正も行われ、ユーザーが情報にアクセスしやすくなっています。全体として、この更新はAzure
  OpenAIサービスの利用を効果的かつ安全に行うための重要な変更です。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bf9270b...MicrosoftDocs:71adf7f){target="_blank"}

<format>
# ハイライト
このコード差分は、Azure OpenAIの機能強化と整備に焦点を当てており、新しいモデルとドキュメントの追加、既存文書の更新が行われています。特に、ファインチューニングと安全性、トラブルシューティング関連の新しいセクションが豊富に追加されています。

## 新機能
- **新しいドキュメントの追加**: ファインチューニングのデプロイ、ダイレクトプレファレンス最適化、安全性評価、トラブルシューティングなどに関する詳細なドキュメントが追加され、これによりユーザーはAzure OpenAIの機能をより効果的に活用できます。
- **モデル情報の拡充**: 新しい「o1」モデルや「o3-mini」モデルが追加され、各モデルに対するプロビジョニングされたスループットとリージョン提供状況が明確に示されました。

## 破壊的変更
- **ファインチューニング用Python SDKドキュメントの大規模更新**: 古いバージョンのPython SDKに関するセクションが削除され、最新の実装にフォーカスされています。

## その他のアップデート
- **マイナーな文書更新**: 日付変更、セクションタイトルの明確化、データセットに関する詳細説明の強化、および結果ファイルの分析手法の追加などが含まれます。
- **目次とリンクの修正**: 新しいファインチューニング関連のセクションの追加とリンクの修正で、ユーザーが迅速に必要な情報へアクセス可能となりました。

# 洞察
この変更は、Azure OpenAIサービスを使用するユーザーにとって非常に有益です。特に、新機能として追加されたドキュメントは、ファインチューニングプロセスの理解を深め、実装をスムーズにするために不可欠です。たとえば、「fine-tuning-deploy.md」の実装詳細や、「fine-tuning-troubleshoot.md」のトラブルシューティングガイドは、開発者に具体的な手順を提供し、実際の作業効率を高めます。

また、新たなモデルの追加は、ユーザーのニーズに応じた選択肢を増やし、プロビジョニングされたスループットやリージョンごとの利用可能性を明確にすることで、ユーザーが計画を立てやすくなります。特に「o1」および「o3-mini」モデルの紹介は、利用可能なリソースの最適化とスケーラビリティに貢献するでしょう。

加えて、Python SDKおよびREST APIに関するドキュメントの更新は、最新の機能やエンドポイントに対応しており、ユーザーが最新技術を利用するための貴重な指針を提供します。これにより、ユーザーが古いドキュメントに依存せず、最新の技術を活用できる環境が整えられています。

全体として、この更新はAzure OpenAIサービスの利用における最新かつ最適な方法をユーザーに提示し、技術的要求に応えたものとなっています。ユーザーはこれを活用することで、安全かつ効率的にファインチューニングを行うことができるようになります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [provisioned-throughput.md](#item-022e0c) | minor update | プロビジョニングされたスループットに関するアップデート | modified | 8 | 8 | 16 | 
| [fine-tuning-deploy.md](#item-286d57) | new feature | ファインチューニングモデルのデプロイに関する新しいドキュメント | added | 470 | 0 | 470 | 
| [fine-tuning-direct-preference-optimization.md](#item-384724) | new feature | ダイレクトプレファレンス最適化に関する新しいドキュメント | added | 74 | 0 | 74 | 
| [fine-tuning-safety-evaluation.md](#item-782ce3) | new feature | ファインチューニングの安全評価に関する新しいドキュメント | added | 60 | 0 | 60 | 
| [fine-tuning-troubleshoot.md](#item-a32e1f) | new feature | Azure OpenAIファインチューニングのトラブルシューティングに関する新しいドキュメント | added | 80 | 0 | 80 | 
| [fine-tuning-vision.md](#item-d37669) | new feature | 画像入力によるモデルのファインチューニングに関する新しいドキュメント | added | 82 | 0 | 82 | 
| [fine-tuning.md](#item-5c0e85) | minor update | ファインチューニングドキュメントの更新 | modified | 1 | 257 | 258 | 
| [fine-tuning-openai-in-ai-studio.md](#item-723c8d) | minor update | Azure AIスタジオにおけるファインチューニングドキュメントの更新 | modified | 17 | 33 | 50 | 
| [fine-tuning-python.md](#item-976f58) | breaking change | ファインチューニング用Python SDKドキュメントの大規模更新 | modified | 58 | 336 | 394 | 
| [fine-tuning-rest.md](#item-9add3e) | minor update | REST APIを使用したファインチューニングドキュメントの更新 | modified | 56 | 155 | 211 | 
| [fine-tuning-studio.md](#item-439f1e) | minor update | ファインチューニングスタジオに関するドキュメントの更新 | modified | 42 | 144 | 186 | 
| [provisioned-global.md](#item-340884) | minor update | モデル行列におけるプロビジョニングされたグローバルリージョンの更新 | modified | 30 | 28 | 58 | 
| [deploy-dialogue.png](#item-7a5d8d) | new feature | デプロイダイアログの画像を追加 | added | 0 | 0 | 0 | 
| [quotas-limits.md](#item-06c6f9) | minor update | オープンAIのクォータと制限の更新 | modified | 9 | 1 | 10 | 
| [toc.yml](#item-c945af) | minor update | 目次の更新とファインチューニングセクションの改善 | modified | 17 | 1 | 18 | 
| [whats-new.md](#item-53303b) | minor update | DPOリファレンスのリンク修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -48,14 +48,14 @@ The amount of throughput (tokens per minute or TPM) a deployment gets per PTU is
 
 To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the specified models. To understand the impact of output tokens on the TPM per PTU limit, use the 3 input token to 1 output token ratio. For a detailed understanding of how different ratios of input and output tokens impact the throughput your workload needs, see the [Azure OpenAI capacity calculator](https://oai.azure.com/portal/calculator). The table also shows Service Level Agreement (SLA) Latency Target Values per model.  For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
 
-|Topic| **gpt-4o**   | **gpt-4o-mini**   |
-| --- | --- | --- |
-|Global & data zone provisioned minimum deployment|15|15|
-|Global & data zone provisioned scale increment|5|5|
-|Regional provisioned minimum deployment | 50 | 25|
-|Regional provisioned scale increment|50|25|
-|Input TPM per PTU | 2,500 | 37,000  |
-|Latency Target Value |25 Tokens Per Second|33 Tokens Per Second|
+|Topic| **gpt-4o**   | **gpt-4o-mini**  | **o1**|
+| --- | --- | --- | --- |
+|Global & data zone provisioned minimum deployment|15|15|15|
+|Global & data zone provisioned scale increment|5|5|5|
+|Regional provisioned minimum deployment|50|25|50|
+|Regional provisioned scale increment|50|25|50|
+|Input TPM per PTU |2,500|37,000|230|
+|Latency Target Value |25 Tokens Per Second|33 Tokens Per Second|25 Tokens Per Second|
 
 For a full list see the [Azure OpenAI Service in Azure AI Foundry portal calculator](https://oai.azure.com/portal/calculator).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされたスループットに関するアップデート"
}
```

### Explanation
今回の変更は、`provisioned-throughput.md`というファイルで行われました。この変更では、表に新しい列が追加され、各モデルのプロビジョニングされたスループットに関する情報が更新されています。具体的には、GPT-4o-miniに加え、新たにo1モデルが追加され、各モデルに対するスループットやレイテンシターゲット値が明確に示されています。また、従来の情報が整理され、プロビジョニングされた最小デプロイメントやスケールインクリメントに関する数値も更新されています。この更新により、ユーザーは新しいo1モデルの性能を適切に理解し、利用するための参考情報を得ることができます。

## articles/ai-services/openai/how-to/fine-tuning-deploy.md{#item-286d57}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,470 @@
+---
+title: 'Deploy a fine-tuned model'
+titleSuffix: Azure OpenAI
+description: Learn how to deploy your fine-tuned model with Azure OpenAI Service by using Python, the REST APIs, or Azure AI Foundry portal.
+#services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.custom: build-2023, build-2023-dataai, devx-track-python, references_regions
+ms.topic: how-to
+ms.date: 02/24/2025
+author: mrbullwinkle
+ms.author: mbullwin
+---
+
+# Deploy a fine-tuned model for inferencing
+
+Once your model is fine-tuned, you can deploy the model and can use it in your own application.
+
+When you deploy the model, you make the model available for inferencing, and that incurs an hourly hosting charge. Fine-tuned models, however, can be stored in Azure AI Foundry at no cost until you're ready to use them.
+
+Azure OpenAI provides choices of deployment types for fine-tuned models on the hosting structure that fits different business and usage patterns: **Standard**, **Global Standard** (preview) and **Provisioned Managed** (preview). Learn more about [deployment types for fine-tuned models](#deployment-types) and the [concepts of all deployment types](./deployment-types.md).
+
+## Deploy your fine-tuned model
+
+## [Portal](#tab/portal)
+
+To deploy your custom model, select the custom model to deploy, and then select **Deploy**.
+
+The **Deploy model** dialog box opens. In the dialog box, enter your **Deployment name** and then select **Create** to start the deployment of your custom model.
+
+:::image type="content" source="../media/fine-tuning/fine-tuning-deploy/deploy-dialogue.png" alt-text="Screenshot that shows how to deploy a custom model in Azure AI Foundry portal." lightbox="../media/fine-tuning/fine-tuning-deploy/deploy-dialogue.png":::
+
+You can monitor the progress of your deployment on the **Deployments** pane in Azure AI Foundry portal.
+
+The UI does not support cross region deployment, while Python SDK or REST supports.
+
+## [Python](#tab/python)
+
+
+```python
+import json
+import os
+import requests
+
+token = os.getenv("<TOKEN>") 
+subscription = "<YOUR_SUBSCRIPTION_ID>"  
+resource_group = "<YOUR_RESOURCE_GROUP_NAME>"
+resource_name = "<YOUR_AZURE_OPENAI_RESOURCE_NAME>"
+model_deployment_name = "gpt-35-turbo-ft" # custom deployment name that you will use to reference the model when making inference calls.
+
+deploy_params = {'api-version': "2024-10-21"} 
+deploy_headers = {'Authorization': 'Bearer {}'.format(token), 'Content-Type': 'application/json'}
+
+deploy_data = {
+    "sku": {"name": "standard", "capacity": 1}, 
+    "properties": {
+        "model": {
+            "format": "OpenAI",
+            "name": <"fine_tuned_model">, #retrieve this value from the previous call, it will look like gpt-35-turbo-0613.ft-b044a9d3cf9c4228b5d393567f693b83
+            "version": "1"
+        }
+    }
+}
+deploy_data = json.dumps(deploy_data)
+
+request_url = f'https://management.azure.com/subscriptions/{subscription}/resourceGroups/{resource_group}/providers/Microsoft.CognitiveServices/accounts/{resource_name}/deployments/{model_deployment_name}'
+
+print('Creating a new deployment...')
+
+r = requests.put(request_url, params=deploy_params, headers=deploy_headers, data=deploy_data)
+
+print(r)
+print(r.reason)
+print(r.json())
+
+```
+
+|variable      | Definition|
+|--------------|-----------|
+| token        | There are multiple ways to generate an authorization token. The easiest method for initial testing is to launch the Cloud Shell from the [Azure portal](https://portal.azure.com). Then run [`az account get-access-token`](/cli/azure/account#az-account-get-access-token()). You can use this token as your temporary authorization token for API testing. We recommend storing this in a new environment variable. |
+| subscription | The subscription ID for the associated Azure OpenAI resource. |
+| resource_group | The resource group name for your Azure OpenAI resource. |
+| resource_name | The Azure OpenAI resource name. |
+| model_deployment_name | The custom name for your new fine-tuned model deployment. This is the name that will be referenced in your code when making chat completion calls. |
+| fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It will look like `gpt-35-turbo-0613.ft-b044a9d3cf9c4228b5d393567f693b83`. You will need to add that value to the deploy_data json. Alternatively you can also deploy a checkpoint, by passing the checkpoint ID which will appear in the format `ftchkpt-e559c011ecc04fc68eaa339d8227d02d` |
+
+### Cross region deployment
+
+Fine-tuning supports deploying a fine-tuned model to a different region than where the model was originally fine-tuned. You can also deploy to a different subscription/region.
+
+The only limitations are that the new region must also support fine-tuning and when deploying cross subscription the account generating the authorization token for the deployment must have access to both the source and destination subscriptions.
+
+Below is an example of deploying a model that was fine-tuned in one subscription/region to another.
+
+```python
+import json
+import os
+import requests
+
+token= os.getenv("<TOKEN>") 
+
+subscription = "<DESTINATION_SUBSCRIPTION_ID>"  
+resource_group = "<DESTINATION_RESOURCE_GROUP_NAME>"
+resource_name = "<DESTINATION_AZURE_OPENAI_RESOURCE_NAME>"
+
+source_subscription = "<SOURCE_SUBSCRIPTION_ID>"
+source_resource_group = "<SOURCE_RESOURCE_GROUP>"
+source_resource = "<SOURCE_RESOURCE>"
+
+
+source = f'/subscriptions/{source_subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.CognitiveServices/accounts/{source_resource}'
+
+model_deployment_name = "gpt-35-turbo-ft" # custom deployment name that you will use to reference the model when making inference calls.
+
+deploy_params = {'api-version': "2024-10-21"} 
+deploy_headers = {'Authorization': 'Bearer {}'.format(token), 'Content-Type': 'application/json'}
+
+
+
+deploy_data = {
+    "sku": {"name": "standard", "capacity": 1}, 
+    "properties": {
+        "model": {
+            "format": "OpenAI",
+            "name": <"FINE_TUNED_MODEL_NAME">, # This value will look like gpt-35-turbo-0613.ft-0ab3f80e4f2242929258fff45b56a9ce 
+            "version": "1",
+            "source": source
+        }
+    }
+}
+deploy_data = json.dumps(deploy_data)
+
+request_url = f'https://management.azure.com/subscriptions/{subscription}/resourceGroups/{resource_group}/providers/Microsoft.CognitiveServices/accounts/{resource_name}/deployments/{model_deployment_name}'
+
+print('Creating a new deployment...')
+
+r = requests.put(request_url, params=deploy_params, headers=deploy_headers, data=deploy_data)
+
+print(r)
+print(r.reason)
+print(r.json())
+```
+
+To deploy between the same subscription, but different regions you would just have subscription and resource groups be identical for both source and destination variables and only the source and destination resource names would need to be unique.
+
+### Cross tenant deployment
+
+The account used to generate access tokens with `az account get-access-token --tenant` should have Cognitive Services OpenAI Contributor permissions to both the source and destination Azure OpenAI resources. You will need to generate two different tokens, one for the source tenant and one for the destination tenant.
+
+```python
+import requests
+
+subscription = "DESTINATION-SUBSCRIPTION-ID"
+resource_group = "DESTINATION-RESOURCE-GROUP"
+resource_name = "DESTINATION-AZURE-OPENAI-RESOURCE-NAME"
+model_deployment_name = "DESTINATION-MODEL-DEPLOYMENT-NAME"
+fine_tuned_model = "gpt-4o-mini-2024-07-18.ft-f8838e7c6d4a4cbe882a002815758510" #source fine-tuned model id example id provided
+source_subscription_id = "SOURCE-SUBSCRIPTION-ID"
+source_resource_group = "SOURCE-RESOURCE-GROUP" 
+source_account = "SOURCE-AZURE-OPENAI-RESOURCE-NAME"
+
+dest_token = "DESTINATION-ACCESS-TOKEN" # az account get-access-token --tenant DESTINATION-TENANT-ID
+source_token = "SOURCE-ACCESS-TOKEN"  # az account get-access-token --tenant SOURCE-TENANT-ID
+
+headers = {
+    "Authorization": f"Bearer {dest_token}", 
+    "x-ms-authorization-auxiliary": f"Bearer {source_token}", 
+    "Content-Type": "application/json"
+}
+
+url = f"https://management.azure.com/subscriptions/{subscription}/resourceGroups/{resource_group}/providers/Microsoft.CognitiveServices/accounts/{resource_name}/deployments/{model_deployment_name}?api-version=2024-10-01"
+
+payload = {
+    "sku": {
+        "name": "standard",
+        "capacity": 1
+    },
+    "properties": {
+        "model": {
+            "format": "OpenAI",
+            "name": fine_tuned_model,
+            "version": "1",
+            "sourceAccount": f"/subscriptions/{source_subscription_id}/resourceGroups/{source_resource_group}/providers/Microsoft.CognitiveServices/accounts/{source_account}"
+        }
+    }
+}
+
+response = requests.put(url, headers=headers, json=payload)
+
+# Check response
+print(f"Status Code: {response.status_code}")
+print(f"Response: {response.json()}")
+```
+
+## [REST](#tab/rest)
+
+The following example shows how to use the REST API to create a model deployment for your customized model. The REST API generates a name for the deployment of your customized model.
+
+
+```bash
+curl -X POST "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-21" \
+  -H "Authorization: Bearer <TOKEN>" \
+  -H "Content-Type: application/json" \
+  -d '{
+    "sku": {"name": "standard", "capacity": 1},
+    "properties": {
+        "model": {
+            "format": "OpenAI",
+            "name": "<FINE_TUNED_MODEL>",
+            "version": "1"
+        }
+    }
+}'
+```
+
+|variable      | Definition|
+|--------------|-----------|
+| token        | There are multiple ways to generate an authorization token. The easiest method for initial testing is to launch the Cloud Shell from the [Azure portal](https://portal.azure.com). Then run [`az account get-access-token`](/cli/azure/account#az-account-get-access-token()). You can use this token as your temporary authorization token for API testing. We recommend storing this in a new environment variable. |
+| subscription | The subscription ID for the associated Azure OpenAI resource. |
+| resource_group | The resource group name for your Azure OpenAI resource. |
+| resource_name | The Azure OpenAI resource name. |
+| model_deployment_name | The custom name for your new fine-tuned model deployment. This is the name that will be referenced in your code when making chat completion calls. |
+| fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It will look like `gpt-35-turbo-0613.ft-b044a9d3cf9c4228b5d393567f693b83`. You'll need to add that value to the deploy_data json. Alternatively you can also deploy a checkpoint, by passing the checkpoint ID which will appear in the format `ftchkpt-e559c011ecc04fc68eaa339d8227d02d` |
+
+
+### Cross region deployment
+
+Fine-tuning supports deploying a fine-tuned model to a different region than where the model was originally fine-tuned. You can also deploy to a different subscription/region.
+
+The only limitations are that the new region must also support fine-tuning and when deploying cross subscription the account generating the authorization token for the deployment must have access to both the source and destination subscriptions. 
+
+Below is an example of deploying a model that was fine-tuned in one subscription/region to another.
+
+```bash
+curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-21" \
+  -H "Authorization: Bearer <TOKEN>" \
+  -H "Content-Type: application/json" \
+  -d '{
+    "sku": {"name": "standard", "capacity": 1},
+    "properties": {
+        "model": {
+            "format": "OpenAI",
+            "name": "<FINE_TUNED_MODEL>", 
+            "version": "1",
+            "source": "/subscriptions/{sourceSubscriptionID}/resourceGroups/{sourceResourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{sourceAccount}" 
+        }
+    }
+}'
+```
+
+To deploy between the same subscription, but different regions, you would just have subscription and resource groups be identical for both source and destination variables and only the source and destination resource names would need to be unique.
+
+### Cross tenant deployment
+
+The account used to generate access tokens with `az account get-access-token --tenant` should have Cognitive Services OpenAI Contributor permissions to both the source and destination Azure OpenAI resources. You will need to generate two different tokens, one for the source tenant and one for the destination tenant.
+
+
+```bash
+curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>?api-version=2024-10-01" \
+  -H "Authorization: Bearer <DESTINATION TOKEN>" \
+  -H "x-ms-authorization-auxiliary: Bearer <SOURCE TOKEN>" \
+  -H "Content-Type: application/json" \
+  -d '{
+    "sku": {"name": "standard", "capacity": 1},
+    "properties": {
+        "model": {
+            "format": "OpenAI",
+            "name": "<FINE_TUNED_MODEL>", 
+            "version": "1",
+            "sourceAccount": "/subscriptions/{sourceSubscriptionID}/resourceGroups/{sourceResourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{sourceAccount}" 
+        }
+    }
+}'
+```
+
+### Deploy a model with Azure CLI
+
+The following example shows how to use the Azure CLI to deploy your customized model. With the Azure CLI, you must specify a name for the deployment of your customized model. For more information about how to use the Azure CLI to deploy customized models, see [`az cognitiveservices account deployment`](/cli/azure/cognitiveservices/account/deployment).
+
+To run this Azure CLI command in a console window, you must replace the following _\<placeholders>_ with the corresponding values for your customized model:
+
+| Placeholder | Value |
+| --- | --- |
+| _\<YOUR_AZURE_SUBSCRIPTION>_ | The name or ID of your Azure subscription. |
+| _\<YOUR_RESOURCE_GROUP>_ | The name of your Azure resource group. |
+| _\<YOUR_RESOURCE_NAME>_ | The name of your Azure OpenAI resource. |
+| _\<YOUR_DEPLOYMENT_NAME>_ | The name you want to use for your model deployment. |
+| _\<YOUR_FINE_TUNED_MODEL_ID>_ | The name of your customized model. |
+
+```azurecli
+az cognitiveservices account deployment create 
+    --resource-group <YOUR_RESOURCE_GROUP>
+    --name <YOUR_RESOURCE_NAME>  
+    --deployment-name <YOUR_DEPLOYMENT_NAME>
+    --model-name <YOUR_FINE_TUNED_MODEL_ID>
+    --model-version "1" 
+    --model-format OpenAI 
+    --sku-capacity "1" 
+    --sku-name "Standard"
+```
+---
+
+[!INCLUDE [Fine-tuning deletion](../includes/fine-tune.md)]
+
+## Use your deployed fine-tuned model
+
+## [Portal](#tab/portal)
+
+After your custom model deploys, you can use it like any other deployed model. You can use the **Playgrounds** in [Azure AI Foundry portal](https://oai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models.
+
+:::image type="content" source="../media/quickstarts/playground-load-new.png" alt-text="Screenshot of the Playground pane in Azure AI Foundry portal, with sections highlighted." lightbox="../media/quickstarts/playground-load-new.png":::
+
+
+## [Python](#tab/python)
+
+```python
+import os
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
+  api_version="2024-02-01"
+)
+
+response = client.chat.completions.create(
+    model="gpt-35-turbo-ft", # model = "Custom deployment name you chose for your fine-tuning model"
+    messages=[
+        {"role": "system", "content": "You are a helpful assistant."},
+        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
+        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
+        {"role": "user", "content": "Do other Azure AI services support this too?"}
+    ]
+)
+
+print(response.choices[0].message.content)
+```
+
+## [REST](#tab/rest)
+
+```bash
+curl $AZURE_OPENAI_ENDPOINT/openai/deployments/<deployment_name>/chat/completions?api-version=2024-10-21 \
+  -H "Content-Type: application/json" \
+  -H "api-key: $AZURE_OPENAI_API_KEY" \
+  -d '{"messages":[{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},{"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},{"role": "user", "content": "Do other Azure AI services support this too?"}]}'
+```
+---
+
+### Prompt caching
+
+Azure OpenAI fine-tuning supports prompt caching with select models. Prompt caching allows you to reduce overall request latency and cost for longer prompts that have identical content at the beginning of the prompt. To learn more about prompt caching, see [getting started with prompt caching](./prompt-caching.md).
+
+## Deployment Types
+
+Azure OpenAI fine-tuning supports the following deployment types.
+
+### Standard
+
+[Standard deployments](./deployment-types.md#standard) provides a pay-per-call billing model, and the model available in each region as well as throughput may be limited.
+
+| Models | Region |
+|--|--|
+|GPT-4o-finetune|East US2, North Central US, Sweden Central|
+|gpt-4o-mini-2024-07-18|North Central US, Sweden Central|
+|GPT-4-finetune|North Central US, Sweden Central|
+|GPT-35-Turbo-finetune|East US2, North Central US, Sweden Central, Switzerland West|
+|GPT-35-Turbo-1106-finetune|East US2, North Central US, Sweden Central, Switzerland West|
+|GPT-35-Turbo-0125-finetune|East US2, North Central US, Sweden Central, Switzerland West|
+
+### Global Standard (preview)
+
+| Models | Region |
+|--|--|
+|GPT-4o-finetune|East US2, North Central US, and Sweden Central|
+|GPT-4o-mini-finetune|East US2, North Central US, and Sweden Central|
+
+[Global standard](./deployment-types.md#global-standard) fine-tuned deployments offer [cost savings](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/), but custom model weights may temporarily be stored outside the geography of your Azure OpenAI resource.
+
+:::image type="content" source="../media/fine-tuning/global-standard.png" alt-text="Screenshot of the global standard deployment user experience with a fine-tuned model." lightbox="../media/fine-tuning/global-standard.png":::
+
+Global Standard fine-tuned deployments currently support structured outputs only on GPT-4o.
+
+### Provisioned Managed (preview)
+
+| Models | Region |
+|--|--|
+|GPT-4o-finetune|North Central US, Switzerland West|
+|GPT-4o-mini-finetune|North Central US, Switzerland West|
+
+- `gpt-4o-mini-2024-07-18`
+- `gpt-4o-2024-08-06`
+
+[Provisioned managed](./deployment-types.md#provisioned) fine-tuned deployments offer [predictable performance](../concepts/provisioned-throughput.md#what-do-the-provisioned-deployment-types-provide) for fine-tuned deployments. As part of public preview, provisioned managed deployments may be created regionally via the data-plane [REST API](../reference.md#data-plane-inference) version `2024-10-01` or newer. See below for examples.
+
+Provisioned Managed fine-tuned deployments currently support structured outputs only on GPT-4o.
+
+#### Creating a Provisioned Managed deployment
+
+To create a new deployment, make an HTTP PUT call via the [Deployments - Create or Update REST API](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true). The approach is similar to performing [cross region deployment](#cross-region-deployment) with the following exceptions:
+
+- You must provide a `sku` name of `ProvisionedStandard`.
+- The capacity must be declared in PTUs.
+- The `api-version` must be `2024-10-01` or newer.
+- The HTTP method should be `PUT`.
+
+For example, to deploy a gpt-4o-mini model:
+
+```bash
+curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-01" \
+  -H "Authorization: Bearer <TOKEN>" \
+  -H "Content-Type: application/json" \
+  -d '{
+    "sku": {"name": "ProvisionedStandard", "capacity": 25},
+    "properties": {
+        "model": {
+            "format": "OpenAI",
+            "name": "gpt-4omini-ft-model-name",
+            "version": "1",
+            "source": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/{SourceResourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{SourceAOAIAccountName}"
+        }
+    }
+  }'
+```
+
+#### Scaling a fine-tuned model on Provisioned Managed
+
+To scale a fine-tuned provision managed deployment to increase or decrease PTU capacity, perform the same `PUT` REST API call as you did when [creating the deployment](#creating-a-provisioned-managed-deployment) and provide an updated `capacity` value for the `sku`. Keep in mind, provisioned deployments must scale in [minimum increments](../concepts/provisioned-throughput.md#how-much-throughput-per-ptu-you-get-for-each-model).
+
+For example, to scale the model deployed in the previous section from 25 to 40 PTU, make another `PUT` call and increase the capacity:
+
+```bash
+curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-01" \
+  -H "Authorization: Bearer <TOKEN>" \
+  -H "Content-Type: application/json" \
+  -d '{
+    "sku": {"name": "ProvisionedStandard", "capacity": 40},
+    "properties": {
+        "model": {
+            "format": "OpenAI",
+            "name": "gpt-4omini-ft-model-name",
+            "version": "1",
+            "source": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/{SourceResourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{SourceAOAIAccountName}"
+        }
+    }
+  }'
+```
+
+## Clean up your deployment
+
+To delete a deployment, use the [Deployments - Delete REST API](/rest/api/aiservices/accountmanagement/deployments/delete?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true) and send an HTTP DELETE to the deployment resource. Like with creating deployments, you must include the following parameters:
+
+- Azure subscription ID
+- Azure resource group name
+- Azure OpenAI resource name
+- Name of the deployment to delete
+
+Below is the REST API example to delete a deployment:
+
+```bash
+curl -X DELETE "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-21" \
+  -H "Authorization: Bearer <TOKEN>"
+```
+
+You can also delete a deployment in Azure AI Foundry portal, or use [Azure CLI](/cli/azure/cognitiveservices/account/deployment?preserve-view=true#az-cognitiveservices-account-deployment-delete).
+
+
+## Next steps
+
+- [Azure OpenAI Quotas & limits](./quota.md)
+- [Azure OpenAI deployment types](./deployment-types.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファインチューニングモデルのデプロイに関する新しいドキュメント"
}
```

### Explanation
この変更では、新しいドキュメント「fine-tuning-deploy.md」が追加されました。このドキュメントでは、Azure OpenAIサービスを使用してファインチューニングされたモデルをデプロイする方法について詳細に説明しています。内容は470行にわたり、モデルデプロイメントの手順、使用するAPIやPythonコードの例、およびリソースの設定に関する情報が含まれています。

具体的には、デプロイメントの種類やプロセスの概要、必要な環境変数の設定、REST APIやAzure CLIを使用したデプロイの手法など、多岐にわたる情報が記載されています。また、異なるサブスクリプションやリージョンにデプロイするための指示、ファインチューニング後のモデルのクリーンアップ方法も説明されています。

この新しいドキュメントは、ユーザーがファインチューニングされたモデルを効率的にデプロイし、その後使い始める際の貴重なリソースとなります。特にPython SDKやREST APIを介した実装例が豊富に提供されているため、開発者は具体的なコードを参考にしながら作業を進めることができます。

## articles/ai-services/openai/how-to/fine-tuning-direct-preference-optimization.md{#item-384724}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,74 @@
+---
+title: 'Direct preference optimization'
+titleSuffix: Azure OpenAI
+description: Learn how to use direct preference optimization technique to fine-tune Azure OpenAI models.
+#services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.custom: build-2023, build-2023-dataai, devx-track-python, references_regions
+ms.topic: how-to
+ms.date: 02/24/2025
+author: mrbullwinkle
+ms.author: mbullwin
+---
+
+# Direct preference optimization (preview)
+
+Direct preference optimization (DPO) is an alignment technique for large language models, used to adjust model weights based on human preferences. It differs from reinforcement learning from human feedback (RLHF) in that it does not require fitting a reward model and uses simpler binary data preferences for training. It is computationally lighter weight and faster than RLHF, while being equally effective at alignment.
+
+## Why is DPO useful?
+
+DPO is especially useful in scenarios where there's no clear-cut correct answer, and subjective elements like tone, style, or specific content preferences are important. This approach also enables the model to learn from both positive examples (what's considered correct or ideal) and negative examples (what's less desired or incorrect).
+
+DPO is believed to be a technique that will make it easier for customers to generate high-quality training data sets. While many customers struggle to generate sufficient large data sets for supervised fine-tuning, they often have preference data already collected based on user logs, A/B tests, or smaller manual annotation efforts.
+
+## Direct preference optimization dataset format
+
+Direct preference optimization files have a different format than supervised fine-tuning. Customers provide a "conversation" containing the system message and the initial user message, and then "completions" with paired preference data. Users can only provide two completions.
+
+Three top-level fields: `input`, `preferred_output` and `non_preferred_output`
+
+- Each element in the preferred_output/non_preferred_output must contain at least one assistant message
+- Each element in the preferred_output/non_preferred_output can only have roles in (assistant, tool)
+
+```json
+{  
+  "input": {  
+    "messages": {"role": "system", "content": ...},  
+    "tools": [...],  
+    "parallel_tool_calls": true  
+  },  
+  "preferred_output": [{"role": "assistant", "content": ...}],  
+  "non_preferred_output": [{"role": "assistant", "content": ...}]  
+}  
+```
+
+Training datasets must be in `jsonl` format:
+
+```jsonl
+{{"input": {"messages": [{"role": "system", "content": "You are a chatbot assistant. Given a user question with multiple choice answers, provide the correct answer."}, {"role": "user", "content": "Question: Janette conducts an investigation to see which foods make her feel more fatigued. She eats one of four different foods each day at the same time for four days and then records how she feels. She asks her friend Carmen to do the same investigation to see if she gets similar results. Which would make the investigation most difficult to replicate? Answer choices: A: measuring the amount of fatigue, B: making sure the same foods are eaten, C: recording observations in the same chart, D: making sure the foods are at the same temperature"}]}, "preferred_output": [{"role": "assistant", "content": "A: Measuring The Amount Of Fatigue"}], "non_preferred_output": [{"role": "assistant", "content": "D: making sure the foods are at the same temperature"}]}
+}
+```
+
+## Direct preference optimization model support
+
+- `gpt-4o-2024-08-06` supports direct preference optimization in its respective fine-tuning regions. Latest region availability is updated in the [models page](../concepts/models.md#fine-tuning-models)
+
+Users can use preference fine tuning with base models as well as models that have already been fine-tuned using supervised fine-tuning as long as they are of a supported model/version.
+
+## How to use direct preference optimization fine-tuning
+
+   :::image type="content" border="true" source="/azure/ai-services/openai/media/fine-tuning/preference-optimization.gif" alt-text="GIF of preference optimization fine-tuning steps.":::
+
+1. Prepare `jsonl` datasets in the [preference format](#direct-preference-optimization-dataset-format).
+2. Select the model and then select the method of customization **Direct Preference Optimization**.
+3. Upload datasets – training and validation. Preview as needed.
+4. Select hyperparameters, defaults are recommended for initial experimentation.
+5. Review the selections and create a fine tuning job.
+
+
+## Next steps
+
+- Explore the fine-tuning capabilities in the [Azure OpenAI fine-tuning tutorial](../tutorials/fine-tune.md).
+- Review fine-tuning [model regional availability](../concepts/models.md#fine-tuning-models)
+- Learn more about [Azure OpenAI quotas](../quotas-limits.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ダイレクトプレファレンス最適化に関する新しいドキュメント"
}
```

### Explanation
今回の変更により、「fine-tuning-direct-preference-optimization.md」という新しいドキュメントが追加されました。このドキュメントでは、Azure OpenAIモデルをファインチューニングするためのダイレクトプレファレンス最適化（DPO）技術について説明しています。DPOは、モデルの重みを人間の好みに基づいて調整するためのアライメント技術であり、強化学習（RLHF）とは異なり、報酬モデルをフィッティングする必要がなく、バイナリデータの嗜好を用いた訓練が可能です。

ドキュメントにはDPOがどのように役立つか、特に正解が明確でない状況で価値があることや、ポジティブおよびネガティブな例から学べることが述べられています。また、DPOのデータセットの形式、サポートされるモデル、ファインチューニングの手順なども詳細に説明されています。

具体的には、DPO用のデータセットは特定の形式（`jsonl`）で提供する必要があり、訓練データと検証データをアップロードする流れや、カスタマイズ方法としてDPOを選択する手順も示されています。この新しい情報は、ユーザーが高品質なトレーニングデータセットを生成する手助けとなることを目的としています。

## articles/ai-services/openai/how-to/fine-tuning-safety-evaluation.md{#item-782ce3}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,60 @@
+---
+title: 'Safety evaluation for fine-tuning (preview)'
+titleSuffix: Azure OpenAI
+description: Learn how the safety evaluation works for Azure OpenAI fine-tuning.
+#services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.custom: build-2023, build-2023-dataai, devx-track-python, references_regions
+ms.topic: how-to
+ms.date: 02/24/2025
+author: mrbullwinkle
+ms.author: mbullwin
+---
+
+# Safety evaluation for fine-tuning (preview)
+
+GPT-4o, GPT-4o-mini, and GPT-4 are our most advanced models that can be fine-tuned to your needs. As with Azure OpenAI models generally, the advanced capabilities of fine-tuned models come with increased responsible AI challenges related to harmful content, manipulation, human-like behavior, privacy issues, and more. Learn more about risks, capabilities, and limitations in the [Overview of Responsible AI practices](/legal/cognitive-services/openai/overview?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext) and [Transparency Note](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fcognitive-services%2Fopenai%2Fcontext%2Fcontext&tabs=text). To help mitigate the risks associated with advanced fine-tuned models, we have implemented additional evaluation steps to help detect and prevent harmful content in the training and outputs of fine-tuned models. These steps are grounded in the [Microsoft Responsible AI Standard](https://www.microsoft.com/ai/responsible-ai) and [Azure OpenAI Service content filtering](/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cpython-new).
+
+- Evaluations are conducted in dedicated, customer specific, private workspaces;
+- Evaluation endpoints are in the same geography as the Azure OpenAI resource;
+- Training data is not stored in connection with performing evaluations; only the final model assessment (deployable or not deployable) is persisted; and
+
+GPT-4o, GPT-4o-mini, and GPT-4 fine-tuned model evaluation filters are set to predefined thresholds and cannot be modified by customers; they aren't tied to any custom content filtering configuration you might have created.
+
+## Data evaluation
+
+Before training starts, your data is evaluated for potentially harmful content (violence, sexual, hate, and fairness, self-harm – see category definitions [here](/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cpython-new#risk-categories)). If harmful content is detected above the specified severity level, your training job will fail, and you'll receive a message informing you of the categories of failure.
+
+**Sample message:**
+
+```output
+The provided training data failed RAI checks for harm types: [hate_fairness, self_harm, violence]. Please fix the data and try again.
+```
+
+Your training data is evaluated automatically within your data import job as part of providing the fine-tuning capability.
+
+If the fine-tuning job fails due to the detection of harmful content in training data, you won't be charged.
+
+## Model evaluation
+
+After training completes but before the fine-tuned model is available for deployment, the resulting model is evaluated for potentially harmful responses using Azure’s built-in [risk and safety metrics](/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=warning#risk-and-safety-metrics). Using the same approach to testing that we use for the base large language models, our evaluation capability simulates a conversation with your fine-tuned model to assess the potential to output harmful content, again using specified harmful content [categories](/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cpython-new#risk-categories) (violence, sexual, hate, and fairness, self-harm).  
+
+If a model is found to generate output containing content detected as harmful at above an acceptable rate, you'll be informed that your model isn't available for deployment, with information about the specific categories of harm detected:
+
+**Sample Message**:
+
+```output
+This model is unable to be deployed. Model evaluation identified that this fine tuned model scores above acceptable thresholds for [Violence, Self Harm]. Please review your training data set and resubmit the job.
+```
+
+   :::image type="content" source="../media/fine-tuning/failure.png" alt-text="Screenshot of a failed fine-tuning job due to safety evaluation." lightbox="../media/fine-tuning/failure.png":::
+
+As with data evaluation, the model is evaluated automatically within your fine-tuning job as part of providing the fine-tuning capability. Only the resulting assessment (deployable or not deployable) is logged by the service. If deployment of the fine-tuned model fails due to the detection of harmful content in model outputs, you won't be charged for the training run.
+
+
+## Next steps
+
+- Explore the fine-tuning capabilities in the [Azure OpenAI fine-tuning tutorial](../tutorials/fine-tune.md).
+- Review fine-tuning [model regional availability](../concepts/models.md#fine-tuning-models)
+- Learn more about [Azure OpenAI quotas](../quotas-limits.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファインチューニングの安全評価に関する新しいドキュメント"
}
```

### Explanation
新しいドキュメント「fine-tuning-safety-evaluation.md」が追加されました。このドキュメントでは、Azure OpenAIにおけるファインチューニングモデルの安全評価について詳しく説明しています。GPT-4o、GPT-4o-mini、GPT-4といった最先端のモデルに適用されるこの評価は、危害を及ぼすコンテンツ、人間のような振る舞い、プライバシーの問題などに関連する責任あるAIの課題に対処するための重要な手続きです。

ドキュメントには、安全評価のプロセスに関する情報が含まれており、具体的には、モデルとトレーニングデータがどのように評価されるかについて詳述されています。トレーニングデータは有害コンテンツが含まれているかどうか自動的に評価され、基準を超えた場合はトレーニングが失敗し、その理由が通知されます。

また、トレーニング完了後、ファインチューニングされたモデルは有害な応答について評価され、許容範囲を超える有害コンテンツを出力する場合は、デプロイできない旨が通知される仕組みになっています。これにより、ユーザーはモデルの安全性を確保し、責任を持って使用できるようになります。ドキュメントは、Azure OpenAIのファインチューニング機能を利用する際の重要なリソースとなるでしょう。

## articles/ai-services/openai/how-to/fine-tuning-troubleshoot.md{#item-a32e1f}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,80 @@
+---
+title: 'Troubleshooting for Azure OpenAI fine-tuning'
+titleSuffix: Azure OpenAI
+description: Learn how to troubleshoot Azure OpenAI Service fine-tuning.
+#services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.custom: build-2023, build-2023-dataai, devx-track-python, references_regions
+ms.topic: how-to
+ms.date: 02/24/2025
+author: mrbullwinkle
+ms.author: mbullwin
+---
+
+# Troubleshooting for Azure OpenAI fine-tuning
+
+## How do I enable fine-tuning?
+
+In order to successfully access fine-tuning, you need **Cognitive Services OpenAI Contributor assigned**. Even someone with high-level Service Administrator permissions would still need this account explicitly set in order to access fine-tuning. For more information, please review the [role-based access control guidance](/azure/ai-services/openai/how-to/role-based-access-control#cognitive-services-openai-contributor).
+
+## Why did my upload fail?
+
+If your file upload fails in Azure AI Foundry portal, you can view the error message under **Data files** in Azure AI Foundry portal. Hover your mouse over where it says **error** (under the status column) and an explanation of the failure will be displayed.
+
+:::image type="content" source="../media/fine-tuning/error.png" alt-text="Screenshot of fine-tuning error message." lightbox="../media/fine-tuning/error.png":::
+
+## My fine-tuned model doesn't seem to have improved
+
+- **Missing system message:** You need to provide a system message when you fine tune; you'll want to provide that same system message when you use the fine-tuned model. If you provide a different system message, you may see different results than what you fine-tuned for.
+
+- **Not enough data:** while 10 is the minimum for the pipeline to run, you need hundreds to thousands of data points to teach the model a new skill. Too few data points risks overfitting and poor generalization. Your fine-tuned model may perform well on the training data, but poorly on other data because it has memorized the training examples instead of learning patterns. For best results, plan to prepare a data set with hundreds or thousands of data points.
+
+- **Bad data:** A poorly curated or unrepresentative dataset will produce a low-quality model. Your model may learn inaccurate or biased patterns from your dataset. For example, if you're training a chatbot for customer service, but only provide training data for one scenario (e.g. item returns) it will not know how to respond to other scenarios. Or, if your training data is bad (contains incorrect responses), your model will learn to provide incorrect results.
+
+## Fine-tuning with vision
+
+**What to do if your images get skipped**
+
+Your images can get skipped for the following reasons:
+
+- contains CAPTCHAs
+- contains people
+- contains faces
+
+Remove the image. For now, we can't fine-tune models with images containing these entities.
+
+**Common issues**
+
+|Issue| Reason/Solution|
+|:----|:-----|
+|**Images skipped**| Images can get skipped for the following reasons: contains CAPTCHAs, people, or faces.<br><br> Remove the image. For now, we can't fine-tune models with images containing these entities.|
+|**Inaccessible URL**| Check that the image URL is publicly accessible.|
+|**Image too large**| Check that your images fall within our dataset size limits.|
+|**Invalid image format**| Check that your images fall within our dataset format.|
+
+**How to upload large files**
+
+Your training files might get quite large. You can upload files up to 8 GB in multiple parts using the [Uploads API](/rest/api/azureopenai/upload-file?view=rest-azureopenai-2024-10-21&preserve-view=true) as opposed to the Files API, which only allows file uploads of up to 512 MB.
+
+**Reducing training cost**
+
+If you set the detail parameter for an image to low, the image is resized to 512 by 512 pixels and is only represented by 85 tokens regardless of its size. This will reduce the cost of training.
+
+```json
+{ 
+    "type": "image_url", 
+
+    "image_url": { 
+
+        "url": "https://raw.githubusercontent.com/MicrosoftDocs/azure-ai-docs/main/articles/ai-services/openai/media/how-to/generated-seattle.png", 
+
+        "detail": "low" 
+
+    } 
+} 
+```
+
+**Other considerations for vision fine-tuning**
+
+To control the fidelity of image understanding, set the detail parameter of `image_url` to `low`, `high`, or `auto` for each image. This will also affect the number of tokens per image that the model sees during training time and will affect the cost of training.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIファインチューニングのトラブルシューティングに関する新しいドキュメント"
}
```

### Explanation
新たに「fine-tuning-troubleshoot.md」というドキュメントが追加され、Azure OpenAIのファインチューニングに関するトラブルシューティングの方法が記されています。このドキュメントは、ユーザーがファインチューニングを正しく行うための指針を提供しており、問題が発生した際の解決策を明示しています。

主な内容には、ファインチューニングを有効にするための要件として「Cognitive Services OpenAI Contributor」の設定について説明し、アップロード失敗のエラーメッセージの確認方法も示されています。また、ファインチューニング後のモデルが期待通りに改善しない理由をいくつか挙げており、適切なシステムメッセージの提供、十分なデータポイントの確保、データの品質などが重要であるとしています。

さらに、画像を使用したファインチューニングに関する特有の問題や、画像のアップロードに関するガイドライン、コスト削減のためのアプローチについても触れています。これにより、ユーザーはファインチューニングのプロセスをスムーズに実行できるようになります。この新しいドキュメントは、Azure OpenAIのファインチューニングを行う際に役立つ重要なリソースです。

## articles/ai-services/openai/how-to/fine-tuning-vision.md{#item-d37669}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,82 @@
+---
+title: 'Vision customization'
+titleSuffix: Azure OpenAI
+description: Learn how to fine-tune a model with image inputs.
+#services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.custom: build-2023, build-2023-dataai, devx-track-python, references_regions
+ms.topic: how-to
+ms.date: 02/24/2025
+author: mrbullwinkle
+ms.author: mbullwin
+---
+
+# Vision fine-tuning
+
+Fine-tuning is also possible with images in your JSONL files. Just as you can send one or many image inputs to chat completions, you can include those same message types within your training data. Images can be provided either as publicly accessible URLs or data URIs containing [base64 encoded images](/azure/ai-services/openai/how-to/gpt-with-vision?tabs=rest#call-the-chat-completion-apis). 
+
+## Model support
+
+Vision fine-tuning is supported for `gpt-4o` version `2024-08-06` models only.
+
+## Image dataset requirements
+
+- Your training file can contain a maximum of 50,000 examples that contain images (not including text examples).
+- Each example can have at most 64 images.
+- Each image can be at most 10 MB.
+
+## Format
+
+Images must be:
+
+- JPEG
+- PNG
+- WEBP
+
+Images must be in the RGB or RGBA image mode.
+
+You cannot include images as output from messages with the assistant role.
+
+As with all fine-tuning training your example file requires at least 10 examples.
+
+### Example file format
+
+```json
+{
+  "messages": [
+    { "role": "system", "content": "You are a helpful AI assistant." },
+    { "role": "user", "content": "Describe the image?" },
+    { "role": "user", "content": [
+        {
+          "type": "image_url",
+          "image_url": {
+            "url": "https://raw.githubusercontent.com/MicrosoftDocs/azure-ai-docs/main/articles/ai-services/openai/media/how-to/generated-seattle.png"
+          }
+        }
+      ]
+    },
+    { "role": "assistant", "content": "The image appears to be a watercolor painting of a city skyline, featuring tall buildings and a recognizable structure often associated with Seattle, like the Space Needle. The artwork uses soft colors and brushstrokes to create a somewhat abstract and artistic representation of the cityscape" }
+  ]
+}
+```
+
+
+## Content moderation policy
+
+We scan your images before training to ensure that they comply with our usage policy [Transparency Note](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=text). This may introduce latency in file validation before fine tuning begins.
+
+Images containing the following will be excluded from your dataset and not used for training:
+
+- People
+- Faces
+- CAPTCHAs
+
+> [!IMPORTANT]
+>For vision fine tuning face screening process: We screen for faces/people to skip those images from training the model. The screening capability leverages face detection **WITHOUT** Face identification which means we don't create facial templates or measure specific facial geometry, and the technology used to screen for faces is incapable of uniquely identifying the individuals. To know more about data and Privacy for face refer to - [Data and privacy for Face - Azure AI services | Microsoft Learn](/legal/cognitive-services/computer-vision/imageanalysis-data-privacy-security?context=%2Fazure%2Fai-services%2Fcomputer-vision%2Fcontext%2Fcontext).
+
+## Next steps
+
+- [Deploy a finetuned model](fine-tuning-deploy.md).
+- Review fine-tuning [model regional availability](../concepts/models.md#fine-tuning-models)
+- Learn more about [Azure OpenAI quotas](../quotas-limits.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "画像入力によるモデルのファインチューニングに関する新しいドキュメント"
}
```

### Explanation
新しく追加された「fine-tuning-vision.md」ドキュメントでは、画像を使用したAzure OpenAIモデルのファインチューニングについて解説しています。このドキュメントは、ユーザーがJSONLファイル内に画像を含むトレーニングデータを使用してファインチューニングを行う方法を提供しています。

具体的な内容としては、サポートされているモデル（`gpt-4o`バージョン `2024-08-06`）や画像のデータセット要件について触れています。トレーニングファイルには最大50,000の例を含めることができ、各画像のサイズは最大10 MBでなければなりません。また、使用可能な画像フォーマット（JPEG, PNG, WEBP）や、画像がRGBまたはRGBAモードである必要があることも記載されています。

さらに、ファインチューニングに関する例ファイルのフォーマットや、トレーニング前に画像が使用ポリシーに準拠しているかを確認するためのコンテンツのモデレーション方針についても説明されています。特定の要素（人、顔、CAPTCHA）が含まれる画像はトレーニングデータから除外されるため、ユーザーはこれらのポリシーを理解する必要があります。

このドキュメントは、画像入力を用いたファインチューニングのプロセスを支援するための重要なリソースとして機能します。

## articles/ai-services/openai/how-to/fine-tuning.md{#item-5c0e85}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: build-2023, build-2023-dataai, devx-track-python, references_regions
 ms.topic: how-to
-ms.date: 12/13/2024
+ms.date: 02/27/2025
 author: mrbullwinkle
 ms.author: mbullwin
 zone_pivot_groups: openai-fine-tuning
@@ -44,262 +44,6 @@ We use LoRA, or low rank approximation, to fine-tune models in a way that reduce
 
 ::: zone-end
 
-## Other Deployment Types
-
-Azure OpenAI fine-tuning supports [global standard deployments](./deployment-types.md#global-standard) in East US2, North Central US, and Sweden Central for:
-
-- `gpt-4o-mini-2024-07-18`
-- `gpt-4o-2024-08-06`
-
-And supports [regional provisioned managed](./deployment-types.md#provisioned) in North Central US and Switzerland West for:
-
-- `gpt-4o-mini-2024-07-18`
-- `gpt-4o-2024-08-06`
-
-### Global Standard (preview)
-
-Global standard fine-tuned deployments offer [cost savings](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/), but custom model weights may temporarily be stored outside the geography of your Azure OpenAI resource.
-
-:::image type="content" source="../media/fine-tuning/global-standard.png" alt-text="Screenshot of the global standard deployment user experience with a fine-tuned model." lightbox="../media/fine-tuning/global-standard.png":::
-
-Global Standard fine-tuning deployments currently do not support vision and structured outputs.
-
-### Provisioned Managed (preview)
-
-Provisioned managed fine-tuned deployments offer [predictable performance](../concepts/provisioned-throughput.md#what-do-the-provisioned-deployment-types-provide) for fine-tuned deployments. As part of public preview, provisioned managed deployments may be created regionally via the data-plane [REST API](../reference.md#data-plane-inference) version `2024-10-01` or newer. See below for examples.
-
-Provisioned Managed fine-tuning deployments currently do not support vision and structured outputs.
-
-#### Creating a Provisioned Managed deployment
-
-To create a new deployment, make an HTTP PUT call via the [Deployments - Create or Update REST API](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true). The approach is similar to performing [cross region deployment](#cross-region-deployment) with the following exceptions:
-
-- You must provide a sku name of `ProvisionedStandard`.
-- The capacity must be declared in PTUs.
-- The `api-version` must be `2024-10-01` or newer.
-- The HTTP method should be `PUT`.
-
-For example, to deploy a gpt-4o-mini model:
-
-```bash
-curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-01" \
-  -H "Authorization: Bearer <TOKEN>" \
-  -H "Content-Type: application/json" \
-  -d '{
-    "sku": {"name": "ProvisionedStandard", "capacity": 25},
-    "properties": {
-        "model": {
-            "format": "OpenAI",
-            "name": "gpt-4omini-ft-model-name",
-            "version": "1",
-            "source": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/{SourceResourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{SourceAOAIAccountName}"
-        }
-    }
-  }'
-```
-
-#### Scaling a fine-tuned model on Provisioned Managed
-
-To scale a fine-tuned provision managed deployment to increase or decrease PTU capacity, perform the same `PUT` REST API call as you did when [creating the deployment](#creating-a-provisioned-managed-deployment) and provide an updated `capacity` value for the `sku`. Keep in mind, provisioned deployments must scale in [minimum increments](../concepts/provisioned-throughput.md#how-much-throughput-per-ptu-you-get-for-each-model).
-
-For example, to scale the model deployed in the previous section from 25 to 40 PTU, make another `PUT` call and increase the capacity:
-
-```bash
-curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-01" \
-  -H "Authorization: Bearer <TOKEN>" \
-  -H "Content-Type: application/json" \
-  -d '{
-    "sku": {"name": "ProvisionedStandard", "capacity": 40},
-    "properties": {
-        "model": {
-            "format": "OpenAI",
-            "name": "gpt-4omini-ft-model-name",
-            "version": "1",
-            "source": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/{SourceResourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{SourceAOAIAccountName}"
-        }
-    }
-  }'
-```
-
-#### Deleting a Provisioned Managed deployment
-
-To delete a deployment, use the [Deployments - Delete REST API](/rest/api/aiservices/accountmanagement/deployments/delete?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true) and send an HTTP DELETE to the deployment resource. Like with creating deployments, you must include the following parameters:
-
-
-- Azure subscription id
-- Azure resource group name
-- Azure OpenAI resource name
-- Name of the PTU deployment to delete
-
-For example, to delete the model created and modified in the previous sections:
-
-```bash
-curl -X DELETE "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-01" \
-  -H "Authorization: Bearer <TOKEN>"
-```
-
-## Vision fine-tuning
-
-Fine-tuning is also possible with images in your JSONL files. Just as you can send one or many image inputs to chat completions, you can include those same message types within your training data. Images can be provided either as publicly accessible URLs or data URIs containing [base64 encoded images](/azure/ai-services/openai/how-to/gpt-with-vision?tabs=rest#call-the-chat-completion-apis). 
-
-### Image dataset requirements
-
-- Your training file can contain a maximum of 50,000 examples that contain images (not including text examples).
-- Each example can have at most 64 images.
-- Each image can be at most 10 MB.
-
-### Format
-
-Images must be:
-
-- JPEG
-- PNG
-- WEBP
-
-Images must be in the RGB or RGBA image mode.
-
-You cannot include images as output from messages with the assistant role.
-
-### Content moderation policy
-
-We scan your images before training to ensure that they comply with our usage policy [Transparency Note](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=text). This may introduce latency in file validation before fine tuning begins.
-
-Images containing the following will be excluded from your dataset and not used for training:
-
-- People
-- Faces
-- CAPTCHAs
-
-> [!IMPORTANT]
->For  vision fine tuning face screening process: We screen for faces/people to skip those images from training the model. The screening capability leverages face detection **WITHOUT** Face identification which means we don't create facial templates or measure specific facial geometry, and the technology used to screen for faces is incapable of uniquely identifying the individuals. To know more about data and Privacy for face refer to - [Data and privacy for Face - Azure AI services | Microsoft Learn](/legal/cognitive-services/computer-vision/imageanalysis-data-privacy-security?context=%2Fazure%2Fai-services%2Fcomputer-vision%2Fcontext%2Fcontext).
-
-## Prompt caching
-
-Azure OpenAI fine-tuning supports prompt caching with select models. Prompt caching allows you to reduce overall request latency and cost for longer prompts that have identical content at the beginning of the prompt. To learn more about prompt caching, see [getting started with prompt caching](./prompt-caching.md).
-
-## Direct preference optimization (DPO) (preview)
-
-Direct preference optimization (DPO) is an alignment technique for large language models, used to adjust model weights based on human preferences. It differs from reinforcement learning from human feedback (RLHF) in that it does not require fitting a reward model and uses simpler binary data preferences for training. It is computationally lighter weight and faster than RLHF, while being equally effective at alignment.
-
-### Why is DPO useful?
-
-DPO is especially useful in scenarios where there's no clear-cut correct answer, and subjective elements like tone, style, or specific content preferences are important. This approach also enables the model to learn from both positive examples (what's considered correct or ideal) and negative examples (what's less desired or incorrect).
-
-DPO is believed to be a technique that will make it easier for customers to generate high-quality training data sets. While many customers struggle to generate sufficient large data sets for supervised fine-tuning, they often have preference data already collected based on user logs, A/B tests, or smaller manual annotation efforts.
-
-### Direct preference optimization dataset format
-
-Direct preference optimization files have a different format than supervised fine-tuning. Customers provide a "conversation" containing the system message and the initial user message, and then "completions" with paired preference data. Users can only provide two completions.
-
-Three top-level fields: `input`, `preferred_output` and `non_preferred_output`
-
-- Each element in the preferred_output/non_preferred_output must contain at least one assistant message
-- Each element in the preferred_output/non_preferred_output can only have roles in (assistant, tool)
-
-```json
-{  
-  "input": {  
-    "messages": {"role": "system", "content": ...},  
-    "tools": [...],  
-    "parallel_tool_calls": true  
-  },  
-  "preferred_output": [{"role": "assistant", "content": ...}],  
-  "non_preferred_output": [{"role": "assistant", "content": ...}]  
-}  
-```
-
-Training datasets must be in `jsonl` format:
-
-```jsonl
-{{"input": {"messages": [{"role": "system", "content": "You are a chatbot assistant. Given a user question with multiple choice answers, provide the correct answer."}, {"role": "user", "content": "Question: Janette conducts an investigation to see which foods make her feel more fatigued. She eats one of four different foods each day at the same time for four days and then records how she feels. She asks her friend Carmen to do the same investigation to see if she gets similar results. Which would make the investigation most difficult to replicate? Answer choices: A: measuring the amount of fatigue, B: making sure the same foods are eaten, C: recording observations in the same chart, D: making sure the foods are at the same temperature"}]}, "preferred_output": [{"role": "assistant", "content": "A: Measuring The Amount Of Fatigue"}], "non_preferred_output": [{"role": "assistant", "content": "D: making sure the foods are at the same temperature"}]}
-}
-```
-
-### Direct preference optimization model support
-
-- `gpt-4o-2024-08-06` supports direct preference optimization in its respective fine-tuning regions. Latest region availability is updated in the [models page](../concepts/models.md#fine-tuning-models)
-
-Users can use preference fine tuning with base models as well as models that have already been fine-tuned using supervised fine-tuning as long as they are of a supported model/version.
-
-### How to use direct preference optimization fine-tuning?
-
-   :::image type="content" border="true" source="/azure/ai-services/openai/media/fine-tuning/preference-optimization.gif" alt-text="GIF of preference optimization fine-tuning steps.":::
-
-1. Prepare `jsonl` datasets in the [preference format](#direct-preference-optimization-dataset-format).
-2. Select the model and then select the method of customization **Direct Preference Optimization**.
-3. Upload datasets – training and validation. Preview as needed.
-4. Select hyperparameters, defaults are recommended for initial experimentation.
-5. Review the selections and create a fine tuning job.
-
-## Troubleshooting
-
-### How do I enable fine-tuning?
-
-In order to successfully access fine-tuning, you need **Cognitive Services OpenAI Contributor assigned**. Even someone with high-level Service Administrator permissions would still need this account explicitly set in order to access fine-tuning. For more information, please review the [role-based access control guidance](/azure/ai-services/openai/how-to/role-based-access-control#cognitive-services-openai-contributor).
-
-### Why did my upload fail?
-
-If your file upload fails in [Azure AI Foundry portal](https://ai.azure.com/), you can view the error message under **Data files** in [Azure AI Foundry portal](https://ai.azure.com/). Hover your mouse over where it says “error” (under the status column) and an explanation of the failure will be displayed.
-
-:::image type="content" source="../media/fine-tuning/error.png" alt-text="Screenshot of fine-tuning error message." lightbox="../media/fine-tuning/error.png":::
-
-### My fine-tuned model does not seem to have improved
-
-- **Missing system message:** You need to provide a system message when you fine tune; you will want to provide that same system message when you use the fine-tuned model. If you provide a different system message, you may see different results than what you fine-tuned for.
-
-- **Not enough data:** while 10 is the minimum for the pipeline to run, you need hundreds to thousands of data points to teach the model a new skill. Too few data points risks overfitting and poor generalization. Your fine-tuned model may perform well on the training data, but poorly on other data because it has memorized the training examples instead of learning patterns. For best results, plan to prepare a data set with hundreds or thousands of data points.
-
-- **Bad data:** A poorly curated or unrepresentative dataset will produce a low-quality model. Your model may learn inaccurate or biased patterns from your dataset. For example, if you are training a chatbot for customer service, but only provide training data for one scenario (e.g. item returns) it will not know how to respond to other scenarios. Or, if your training data is bad (contains incorrect responses), your model will learn to provide incorrect results.
-
-### Fine-tuning with vision
-
-**What to do if your images get skipped**
-
-Your images can get skipped for the following reasons:
-
-- contains CAPTCHAs
-- contains people
-- contains faces
-
-Remove the image. For now, we cannot fine-tune models with images containing these entities.
-
-**Common issues**
-
-|Issue| Reason/Solution|
-|:----|:-----|
-|**Images skipped**| Images can get skipped for the following reasons: contains CAPTCHAs, people, or faces.<br><br> Remove the image. For now, we cannot fine-tune models with images containing these entities.|
-|**Inaccessible URL**| Check that the image URL is publicly accessible.|
-|**Image too large**| Check that your images fall within our dataset size limits.|
-|**Invalid image format**| Check that your images fall within our dataset format.|
-
-**How to upload large files**
-
-Your training files might get quite large. You can upload files up to 8 GB in multiple parts using the [Uploads API](/rest/api/azureopenai/upload-file?view=rest-azureopenai-2024-10-21&preserve-view=true) as opposed to the Files API, which only allows file uploads of up to 512 MB.
-
-**Reducing training cost**
-
-If you set the detail parameter for an image to low, the image is resized to 512 by 512 pixels and is only represented by 85 tokens regardless of its size. This will reduce the cost of training.
-
-```json
-{ 
-
-    "type": "image_url", 
-
-    "image_url": { 
-
-        "url": "https://raw.githubusercontent.com/MicrosoftDocs/azure-ai-docs/main/articles/ai-services/openai/media/how-to/generated-seattle.png", 
-
-        "detail": "low" 
-
-    } 
-
-} 
-```
-
-**Other considerations for vision fine-tuning**
-
-To control the fidelity of image understanding, set the detail parameter of `image_url` to `low`, `high`, or `auto` for each image. This will also affect the number of tokens per image that the model sees during training time and will affect the cost of training.
-
 ## Next steps
 
 - Explore the fine-tuning capabilities in the [Azure OpenAI fine-tuning tutorial](../tutorials/fine-tune.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングドキュメントの更新"
}
```

### Explanation
「fine-tuning.md」というドキュメントが更新され、主な改訂点として日付が更新されたほか、一部の内容が削除されています。具体的には、以下のような変更が行われています。

- **日付の更新**: ドキュメントの日付が2024年12月13日から2025年2月27日に変更されています。
- **コンテンツの削除**: 「他のデプロイタイプ」として細分化されたセクションが完全に削除され、これにはグローバル標準デプロイやプロビジョニング済み管理デプロイに関する詳細情報が含まれていました。これにより、該当セクションが258行分のテキストを削除し、現在のドキュメントはよりコンパクトでシンプルな内容に修正されています。

この更新により、ファインチューニングに関する情報がより最新のものとなり、特にリリース日やサポートされる機能に関する情報が正確であることが保証されています。ユーザーは、この改訂を通じて、Azure OpenAIのファインチューニング機能をより正確に理解できるようになります。

## articles/ai-services/openai/includes/fine-tuning-openai-in-ai-studio.md{#item-723c8d}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@
  ms.author: mbullwin
  ms.service: azure-ai-foundry
  ms.topic: include
- ms.date: 05/03/2024
+ ms.date: 02/27/2025
 ms.custom: include, build-2024
 ---
 
@@ -24,7 +24,7 @@ ms.custom: include, build-2024
 - Fine-tuning access requires **Cognitive Services OpenAI Contributor** role on the Azure OpenAI resource.
 - If you don't already have access to view quota and deploy models in Azure AI Foundry portal you need [more permissions](../how-to/role-based-access-control.md).
 
-## Models
+### Supported models
 
 The following models support fine-tuning:
 
@@ -47,7 +47,7 @@ Take a moment to review the fine-tuning workflow for using Azure AI Foundry:
 
 1. Prepare your training and validation data.
 1. Use the **Fine-tune model** wizard in Azure AI Foundry portal to train your custom model.
-    1. [Select a model](#select-the-base-model).
+    1. Select a model to finetune.
     1. [Choose your training data](#choose-your-training-data).
     1. Optionally, [choose your validation data](#choose-your-validation-data).
     1. Optionally, [configure your parameters](#configure-your-parameters) for your fine-tuning job.
@@ -64,7 +64,7 @@ Your training data and validation data sets consist of input and output examples
 
 The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document. For `gpt-35-turbo-0613` the fine-tuning dataset must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
 
-If you would like a step-by-step walk-through of fine-tuning a `gpt-4o-mini-2024-07-18` model please refer to the [Azure OpenAI fine-tuning tutorial.](../tutorials/fine-tune.md)
+It's generally recommended to use the instructions and prompts that you found worked best in every training example. This will help you get the best results, especially if you have fewer than a hundred examples.
 
 ### Example file format
 
@@ -99,9 +99,9 @@ Multiple turns of a conversation in a single line of your jsonl training file is
 
 In addition to the JSONL format, training and validation data files must be encoded in UTF-8 and include a byte-order mark (BOM). The file must be less than 512 MB in size.
 
-### Create your training and validation datasets
+### Datasets size consideration
 
-The more training examples you have, the better. Fine tuning jobs will not proceed without at least 10 training examples, but such a small number is not enough to noticeably influence model responses. It is best practice to provide hundreds, if not thousands, of training examples to be successful.
+The more training examples you have, the better. Fine tuning jobs will not proceed without at least 10 training examples, but such a small number isn't enough to noticeably influence model responses. It is best practice to provide hundreds, if not thousands, of training examples to be successful. It's recommended to start with 50 well-crafted training data.
 
 In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively impact performance. If you train the model on a large amount of internal data, without first pruning the dataset for only the highest quality examples you could end up with a model that performs much worse than expected.
 
@@ -115,12 +115,8 @@ To fine-tune an Azure OpenAI model in an existing Azure AI Foundry project, foll
 
     :::image type="content" source="../media/fine-tuning/ai-studio/fine-tune-new.png" alt-text="Screenshot of the option to start creating a new fine-tuned model." lightbox="../media/fine-tuning/ai-studio/fine-tune-new.png":::
 
-### Select the base model
-
 1. Select a base model to fine-tune. Your choice influences both the performance and the cost of your model. In this example, we are choosing the `gpt-35-turbo` model. Then select **Confirm**.
 
-    :::image type="content" source="../media/fine-tuning/ai-studio/fine-tune-gpt-35-turbo.png" alt-text="Screenshot of option to select a model to fine-tune." lightbox="../media/fine-tuning/ai-studio/fine-tune-gpt-35-turbo.png":::
-
 1. For `gpt-35-turbo` we have different versions available for fine-tuning, so please choose which version you'd like to fine-tune. We will choose (0301). 
 
 1. We also recommend including the `suffix` parameter to make it easier to distinguish between different iterations of your fine-tuned model. `suffix` takes a string, and is set to identify the fine-tuned model. With the OpenAI Python API a string of up to 18 characters is supported that will be added to your fine-tuned model name.
@@ -136,11 +132,11 @@ The next step is to either choose existing prepared training data or upload new
 
 :::image type="content" source="../media/fine-tuning/ai-studio/fine-tune-training-data-local.png" alt-text="Screenshot of the Training data pane for the Fine-tune model wizard in Azure AI Foundry portal." lightbox="../media/fine-tuning/ai-studio/fine-tune-training-data-local.png":::
 
-- If your training data is already in your project, select **Data in Azure AI Foundry portal**.
+- If your training data is already in your project, select **Data in Azure AI Foundry**.
 
    - Select the file from the list shown in the **Training data** pane.
 
-- If your training data is already uploaded to the Azure OpenAI service, select your Azure OpenAI connection under **Azure OpenAI Connection**.
+- If your training data is already uploaded to the Azure OpenAI service, select your Azure OpenAI connection under **Connected AI resource**.
 
 - To upload training data to fine-tune your model, select **Upload data** and then select **Upload file**.  
    - Make sure all your training examples follow the expected format for inference. To fine-tune models effectively, ensure a balanced and diverse dataset. This involves maintaining data balance, including various scenarios, and periodically refining training data to align with real-world expectations, ultimately leading to more accurate and balanced model responses. See [data preparation](#prepare-your-training-and-validation-data) for more information.
@@ -149,8 +145,6 @@ The next step is to either choose existing prepared training data or upload new
 > [!NOTE]
 > Training data files must be formatted as JSONL files, encoded in UTF-8 with a byte-order mark (BOM). The file must be less than 512 MB in size.
 
-:::image type="content" source="../media/fine-tuning/ai-studio/fine-tune-training-data-preview.png" alt-text="Screenshot of option to upload training data locally." lightbox="../media/fine-tuning/ai-studio/fine-tune-training-data-preview.png":::
-
 After uploading files, you will see a preview of your training data. Select **Next** to continue.
 
 :::image type="content" source="../media/fine-tuning/ai-studio/fine-tune-training-data-preview.png" alt-text="Screenshot of the training data preview." lightbox="../media/fine-tuning/ai-studio/fine-tune-training-data-preview.png":::
@@ -184,10 +178,16 @@ Review your choices and select **Submit** to start training your new fine-tuned
 
 ## Check the status of your fine-tuned model
 
-After you submit your fine-tuning job, you see a page with details about your fine-tuned model. You can find the status and more information about your fine-tuned model on the **Fine-tuning** > **Models** page in Azure AI Foundry portal.
+After you submit your fine-tuning job, you see a page with details about your fine-tuned model. You can find the status and more information about your fine-tuned model on the **Fine-tuning** page in Azure AI Foundry portal.
 
 Your job might be queued behind other jobs on the system. Training your model can take minutes or hours depending on the model and dataset size.
 
+## Checkpoints
+
+When each training epoch completes a checkpoint is generated. A checkpoint is a fully functional version of a model which can both be deployed and used as the target model for subsequent fine-tuning jobs. Checkpoints can be particularly useful, as they may provide snapshots prior to overfitting. When a fine-tuning job completes you will have the three most recent versions of the model available to deploy.
+
+:::image type="content" source="../media/fine-tuning/checkpoints.png" alt-text="Screenshot of checkpoints UI." lightbox="../media/fine-tuning/checkpoints.png":::
+
 ## Analyze your fine-tuned model
 
 After fine-tuning is successfully completed, you can download a result file named _results.csv_ from the fine-tuned model page under the **Details** tab. You can use the result file to analyze the training and validation performance of your custom model. 
@@ -210,30 +210,18 @@ You can also view the data in your results.csv file as plots in Azure AI Foundry
 
 Look for your loss to decrease over time, and your accuracy to increase. If you see a divergence between your training and validation data that may indicate that you are overfitting. Try training with fewer epochs, or a smaller learning rate multiplier.
 
-## Checkpoints
-
-When each training epoch completes a checkpoint is generated. A checkpoint is a fully functional version of a model which can both be deployed and used as the target model for subsequent fine-tuning jobs. Checkpoints can be particularly useful, as they can provide a snapshot of your model prior to overfitting having occurred. When a fine-tuning job completes you will have the three most recent versions of the model available to deploy.
-
-:::image type="content" source="../media/fine-tuning/checkpoints.png" alt-text="Screenshot of checkpoints UI." lightbox="../media/fine-tuning/checkpoints.png":::
-
-## Safety evaluation GPT-4, GPT-4o, GPT-4o-mini fine-tuning - public preview
-
-[!INCLUDE [Safety evaluation](../includes/safety-evaluation.md)]
 
 ## Deploy a fine-tuned model
 
-Once your model is fine-tuned, you can deploy the model and can use it in your own application. You can't deploy a fine-tuned model from the deployments page or the playground page in Azure AI Foundry portal. The only way, currently, to deploy a fine-tuned model is from the model details page for that model.
+Once your model is fine-tuned, you can deploy the model and can use it in your own application.
 
 When you deploy the model, you make the model available for inferencing, and that incurs an hourly hosting charge. Fine-tuned models, however, can be stored in Azure AI Foundry portal at no cost until you're ready to use them.
 
 [!INCLUDE [Fine-tuning deletion](../../../ai-services/openai/includes/fine-tune.md)]
 
-> [!NOTE]
-> Only one deployment is permitted for a fine-tuned model. An error message is displayed if you select an already-deployed fine-tuned model.
-
 You can monitor the progress of your deployment on the **Deployments** page in Azure AI Foundry portal.
 
-## Use a deployed fine-tuned model
+### Use a deployed fine-tuned model
 
 After your fine-tuned model deploys, you can use it like any other deployed model. You can use the **Playground** in [Azure AI Foundry](https://ai.azure.com) to experiment with your new deployment. You can also use the REST API to call your fine-tuned model from your own application. You can even begin to use this new fine-tuned model in your prompt flow to build your generative AI application.
 
@@ -256,7 +244,3 @@ You can delete a fine-tuned model on the **Fine-tuning** page in Azure AI Foundr
 
 > [!NOTE]
 > You can't delete a fine-tuned model if it has an existing deployment. You must first [delete your model deployment](#delete-your-fine-tuned-model-deployment) before you can delete your fine-tuned model.
-
-### Delete your training files
-
-You can optionally delete training and validation files that you uploaded for training, and result files generated during training. For this you need to go to Azure AI Foundry portal and navigate to the **Management** > **Data + indexes** pane. Select the file to delete, and then select **Delete** to delete the file.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AIスタジオにおけるファインチューニングドキュメントの更新"
}
```

### Explanation
「fine-tuning-openai-in-ai-studio.md」ドキュメントが更新され、いくつかの重要な変更が加えられました。この改訂には、以下の要素が含まれています。

- **日付の更新**: ドキュメントの日付が2024年5月3日から2025年2月27日に変更されました。
- **セクションタイトルの変更**: 「モデル」セクションが「サポートされるモデル」へと変更され、内容の明確化が図られました。
- **細かな文言の調整**: 一部の文言がより明確に、また読みやすくなるよう修正されています。例えば、「Select a model to finetune」という表現に変更され、ユーザーに対して具体的なアクションが求められる形となりました。

- **データセットに関する詳細の強調**: 訓練データおよび検証データに関する説明が改訂され、特に質の良い訓練データの重要性が強調されています。訓練データの「数」は少なくとも10例は必要ですが、質の高い訓練データを持つことがモデルの性能を大きく向上させることが記述されています。

- **チェックポイントに関する情報の追加**: 各トレーニングエポックの完了時に生成されるチェックポイントの重要性に関する情報が新たに追加されました。これにより、過剰適合を防ぐための戦略が示されています。

この改訂によって、ユーザーはAzure AIスタジオでのファインチューニングプロセスをより効果的に理解し、活用できるようになります。詳細な手順や注意すべき点が改善され、特に初心者や実施経験の浅いユーザーにとって、より利用しやすい内容となっています。

## articles/ai-services/openai/includes/fine-tuning-python.md{#item-976f58}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ description: Learn how to create your own customized model with Azure OpenAI Ser
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 03/06/2024
+ms.date: 02/27/2025
 author: mrbullwinkle
 ms.author: mbullwin
 ---
@@ -22,7 +22,7 @@ ms.author: mbullwin
 - If you do not already have access to view quota, and deploy models in Azure AI Foundry portal you will require [additional permissions](../how-to/role-based-access-control.md).  
 
 
-## Models
+### Supported models
 
 The following models support fine-tuning:
 
@@ -37,7 +37,6 @@ The following models support fine-tuning:
 
 Or you can fine tune a previously fine-tuned model, formatted as `base-model.ft-{jobid}`.
 
-:::image type="content" source="../media/fine-tuning/models.png" alt-text="Screenshot of model options with a custom fine-tuned model." lightbox="../media/fine-tuning/models.png":::
 
 Consult the [models page](../concepts/models.md#fine-tuning-models) to check which regions currently support fine-tuning.
 
@@ -126,7 +125,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-05-01-preview"  # This API version or later is required to access seed/events/checkpoint capabilities
+  api_version="2024-10-21"  # This API version or later is required to access seed/events/checkpoint capabilities
 )
 
 training_file_name = 'training_set.jsonl'
@@ -191,8 +190,6 @@ After you upload your training and validation files, you're ready to start the f
 
 The following Python code shows an example of how to create a new fine-tune job with the Python SDK:
 
-# [OpenAI Python 1.x](#tab/python-new)
-
 In this example we are also passing the seed parameter. The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases. If a seed isn't specified, one will be generated for you.
 
 ```python
@@ -212,28 +209,6 @@ print("Job ID:", response.id)
 print("Status:", response.id)
 print(response.model_dump_json(indent=2))
 ```
-
-# [OpenAI Python 0.28.1](#tab/python)
-
-```python
-
-response = openai.FineTuningJob.create(
-    training_file=training_file_id,
-    validation_file=validation_file_id,
-    model="gpt-35-turbo-0613",
-)
-
-job_id = response["id"]
-
-# You can use the job ID to monitor the status of the fine-tuning job.
-# The fine-tuning job will take some time to start and complete.
-
-print("Job ID:", response["id"])
-print("Status:", response["status"])
-print(response)
-
-```
-
 ---
 
 You can also pass additional optional parameters like hyperparameters to take greater control of the fine-tuning process. For initial training we recommend using the automatic defaults that are present without specifying these parameters. 
@@ -269,85 +244,80 @@ client.fine_tuning.jobs.create(
 
 ## Check fine-tuning job status
 
-# [OpenAI Python 1.x](#tab/python-new)
-
 ```python
 response = client.fine_tuning.jobs.retrieve(job_id)
 
 print("Job ID:", response.id)
 print("Status:", response.status)
 print(response.model_dump_json(indent=2))
 ```
+---
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-```python
-#Retrieve training job ID
+### List fine-tuning events
 
-response = openai.FineTuningJob.retrieve(job_id)
+To examine the individual fine-tuning events that were generated during training, you might need to upgrade your OpenAI client library to the latest version with `pip install openai --upgrade` to run this command.
 
-print("Job ID:", response["id"])
-print("Status:", response["status"])
-print(response)
+```python
+response = client.fine_tuning.jobs.list_events(fine_tuning_job_id=job_id, limit=10)
+print(response.model_dump_json(indent=2))
 ```
 
----
-
-## List fine-tuning events
-
-To examine the individual fine-tuning events that were generated during training:
+## Checkpoints
 
-# [OpenAI Python 1.x](#tab/python-new)
+When each training epoch completes a checkpoint is generated. A checkpoint is a fully functional version of a model which can both be deployed and used as the target model for subsequent fine-tuning jobs. Checkpoints can be particularly useful, as they may provide snapshots prior to overfitting. When a fine-tuning job completes you will have the three most recent versions of the model available to deploy. The final epoch will be represented by your fine-tuned model, the previous two epochs will be available as checkpoints.
 
-You might need to upgrade your OpenAI client library to the latest version with `pip install openai --upgrade` to run this command.
+You can run the list checkpoints command to retrieve the list of checkpoints associated with an individual fine-tuning job. You might need to upgrade your OpenAI client library to the latest version with `pip install openai --upgrade` to run this command.
 
 ```python
 response = client.fine_tuning.jobs.list_events(fine_tuning_job_id=job_id, limit=10)
 print(response.model_dump_json(indent=2))
 ```
 
-# [OpenAI Python 0.28.1](#tab/python)
-
-This command isn't available in the 0.28.1 OpenAI Python library. Upgrade to the latest release.
-
 ---
 
-## Checkpoints
+## Analyze your customized model
 
-When each training epoch completes a checkpoint is generated. A checkpoint is a fully functional version of a model which can both be deployed and used as the target model for subsequent fine-tuning jobs. Checkpoints can be particularly useful, as they can provide a snapshot of your model prior to overfitting having occurred. When a fine-tuning job completes you will have the three most recent versions of the model available to deploy. The final epoch will be represented by your fine-tuned model, the previous two epochs will be available as checkpoints.
+Azure OpenAI attaches a result file named _results.csv_ to each fine-tune job after it completes. You can use the result file to analyze the training and validation performance of your customized model. The file ID for the result file is listed for each customized model, and you can use the Python SDK to retrieve the file ID and download the result file for analysis.
 
-You can run the list checkpoints command to retrieve the list of checkpoints associated with an individual fine-tuning job:
+The following Python example retrieves the file ID of the first result file attached to the fine-tuning job for your customized model, and then uses the Python SDK to download the file to your working directory for analysis.
 
-# [OpenAI Python 1.x](#tab/python-new)
+```python
+# Retrieve the file ID of the first result file from the fine-tuning job
+# for the customized model.
+response = client.fine_tuning.jobs.retrieve(job_id)
+if response.status == 'succeeded':
+    result_file_id = response.result_files[0]
 
-You might need to upgrade your OpenAI client library to the latest version with `pip install openai --upgrade` to run this command.
+retrieve = client.files.retrieve(result_file_id)
 
-```python
-response = client.fine_tuning.jobs.list_events(fine_tuning_job_id=job_id, limit=10)
-print(response.model_dump_json(indent=2))
-```
+# Download the result file.
+print(f'Downloading result file: {result_file_id}')
 
-# [OpenAI Python 0.28.1](#tab/python)
+with open(retrieve.filename, "wb") as file:
+    result = client.files.content(result_file_id).read()
+    file.write(result)
+```
 
-This command isn't available in the 0.28.1 OpenAI Python library. Upgrade to the latest release.
+The result file is a CSV file that contains a header row and a row for each training step performed by the fine-tuning job. The result file contains the following columns:
 
----
+| Column name | Description |
+| --- | --- |
+| `step` | The number of the training step. A training step represents a single pass, forward and backward, on a batch of training data. |
+| `train_loss` | The loss for the training batch. |
+| `train_mean_token_accuracy` | The percentage of tokens in the training batch correctly predicted by the model.<br>For example, if the batch size is set to 3 and your data contains completions `[[1, 2], [0, 5], [4, 2]]`, this value is set to 0.83 (5 of 6) if the model predicted `[[1, 1], [0, 5], [4, 2]]`. |
+| `valid_loss` | The loss for the validation batch. |
+| `validation_mean_token_accuracy` | The percentage of tokens in the validation batch correctly predicted by the model.<br>For example, if the batch size is set to 3 and your data contains completions `[[1, 2], [0, 5], [4, 2]]`, this value is set to 0.83 (5 of 6) if the model predicted `[[1, 1], [0, 5], [4, 2]]`. |
+| `full_valid_loss` | The validation loss calculated at the end of each epoch. When training goes well, loss should decrease. |
+|`full_valid_mean_token_accuracy` | The valid mean token accuracy calculated at the end of each epoch. When training is going well, token accuracy should increase. |
 
-## Safety evaluation GPT-4, GPT-4o, GPT-4o-mini fine-tuning - public preview
+You can also view the data in your results.csv file as plots in Azure AI Foundry portal. Select the link for your trained model, and you will see three charts: loss, mean token accuracy, and token accuracy. If you provided validation data, both datasets will appear on the same plot.
 
-[!INCLUDE [Safety evaluation](../includes/safety-evaluation.md)]
+Look for your loss to decrease over time, and your accuracy to increase. If you see a divergence between your training and validation data that can indicate that you are overfitting. Try training with fewer epochs, or a smaller learning rate multiplier.
 
 ## Deploy a fine-tuned model
 
 When the fine-tuning job succeeds, the value of the `fine_tuned_model` variable in the response body is set to the name of your customized model. Your model is now also available for discovery from the [list Models API](/rest/api/azureopenai/models/list). However, you can't issue completion calls to your customized model until your customized model is deployed. You must deploy your customized model to make it available for use with completion calls.
 
-[!INCLUDE [Fine-tuning deletion](fine-tune.md)]
-
-You can also use [Azure AI Foundry](/azure/ai-services/openai/how-to/fine-tuning?tabs=turbo%2Cpython-new&pivots=ai-foundry-portal#deploy-a-fine-tuned-model) or the [Azure CLI](#deploy-a-model-with-azure-cli) to deploy your customized model.
-
-> [!NOTE]
-> Only one deployment is permitted for a customized model. An error occurs if you select an already-deployed customized model.
-
 Unlike the previous SDK commands, deployment must be done using the control plane API which requires separate authorization, a different API path, and a different API version.
 
 |variable      | Definition|
@@ -370,7 +340,7 @@ resource_group = "<YOUR_RESOURCE_GROUP_NAME>"
 resource_name = "<YOUR_AZURE_OPENAI_RESOURCE_NAME>"
 model_deployment_name ="gpt-35-turbo-ft" # custom deployment name that you will use to reference the model when making inference calls.
 
-deploy_params = {'api-version': "2023-05-01"} 
+deploy_params = {'api-version': "2024-10-21"} 
 deploy_headers = {'Authorization': 'Bearer {}'.format(token), 'Content-Type': 'application/json'}
 
 deploy_data = {
@@ -397,256 +367,44 @@ print(r.json())
 
 ```
 
-### Cross region deployment
-
-Fine-tuning supports deploying a fine-tuned model to a different region than where the model was originally fine-tuned. You can also deploy to a different subscription/region.
-
-The only limitations are that the new region must also support fine-tuning and when deploying cross subscription the account generating the authorization token for the deployment must have access to both the source and destination subscriptions.
-
-Below is an example of deploying a model that was fine-tuned in one subscription/region to another.
-
-```python
-import json
-import os
-import requests
-
-token= os.getenv("<TOKEN>") 
-
-subscription = "<DESTINATION_SUBSCRIPTION_ID>"  
-resource_group = "<DESTINATION_RESOURCE_GROUP_NAME>"
-resource_name = "<DESTINATION_AZURE_OPENAI_RESOURCE_NAME>"
-
-source_subscription = "<SOURCE_SUBSCRIPTION_ID>"
-source_resource_group = "<SOURCE_RESOURCE_GROUP>"
-source_resource = "<SOURCE_RESOURCE>"
-
-
-source = f'/subscriptions/{source_subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.CognitiveServices/accounts/{source_resource}'
-
-model_deployment_name ="gpt-35-turbo-ft" # custom deployment name that you will use to reference the model when making inference calls.
-
-deploy_params = {'api-version': "2023-05-01"} 
-deploy_headers = {'Authorization': 'Bearer {}'.format(token), 'Content-Type': 'application/json'}
-
-
-
-deploy_data = {
-    "sku": {"name": "standard", "capacity": 1}, 
-    "properties": {
-        "model": {
-            "format": "OpenAI",
-            "name": <"FINE_TUNED_MODEL_NAME">, # This value will look like gpt-35-turbo-0613.ft-0ab3f80e4f2242929258fff45b56a9ce 
-            "version": "1",
-            "source": source
-        }
-    }
-}
-deploy_data = json.dumps(deploy_data)
-
-request_url = f'https://management.azure.com/subscriptions/{subscription}/resourceGroups/{resource_group}/providers/Microsoft.CognitiveServices/accounts/{resource_name}/deployments/{model_deployment_name}'
-
-print('Creating a new deployment...')
-
-r = requests.put(request_url, params=deploy_params, headers=deploy_headers, data=deploy_data)
-
-print(r)
-print(r.reason)
-print(r.json())
-```
-
-To deploy between the same subscription, but different regions you would just have subscription and resource groups be identical for both source and destination variables and only the source and destination resource names would need to be unique.
-
-### Cross tenant deployment
-
-The account used to generate access tokens with `az account get-access-token --tenant` should have Cognitive Services OpenAI Contributor permissions to both the source and destination Azure OpenAI resources. You will need to generate two different tokens, one for the source tenant and one for the destination tenant.
-
-```python
-import requests
-
-subscription = "DESTINATION-SUBSCRIPTION-ID"
-resource_group = "DESTINATION-RESOURCE-GROUP"
-resource_name = "DESTINATION-AZURE-OPENAI-RESOURCE-NAME"
-model_deployment_name = "DESTINATION-MODEL-DEPLOYMENT-NAME"
-fine_tuned_model = "gpt-4o-mini-2024-07-18.ft-f8838e7c6d4a4cbe882a002815758510" #source fine-tuned model id example id provided
-source_subscription_id = "SOURCE-SUBSCRIPTION-ID"
-source_resource_group = "SOURCE-RESOURCE-GROUP" 
-source_account = "SOURCE-AZURE-OPENAI-RESOURCE-NAME"
-
-dest_token = "DESTINATION-ACCESS-TOKEN" # az account get-access-token --tenant DESTINATION-TENANT-ID
-source_token = "SOURCE-ACCESS-TOKEN"  # az account get-access-token --tenant SOURCE-TENANT-ID
-
-headers = {
-    "Authorization": f"Bearer {dest_token}", 
-    "x-ms-authorization-auxiliary": f"Bearer {source_token}", 
-    "Content-Type": "application/json"
-}
-
-url = f"https://management.azure.com/subscriptions/{subscription}/resourceGroups/{resource_group}/providers/Microsoft.CognitiveServices/accounts/{resource_name}/deployments/{model_deployment_name}?api-version=2024-10-01"
-
-payload = {
-    "sku": {
-        "name": "standard",
-        "capacity": 1
-    },
-    "properties": {
-        "model": {
-            "format": "OpenAI",
-            "name": fine_tuned_model,
-            "version": "1",
-            "sourceAccount": f"/subscriptions/{source_subscription_id}/resourceGroups/{source_resource_group}/providers/Microsoft.CognitiveServices/accounts/{source_account}"
-        }
-    }
-}
-
-response = requests.put(url, headers=headers, json=payload)
-
-# Check response
-print(f"Status Code: {response.status_code}")
-print(f"Response: {response.json()}")
-```
-
-### Deploy a model with Azure CLI
-
-The following example shows how to use the Azure CLI to deploy your customized model. With the Azure CLI, you must specify a name for the deployment of your customized model. For more information about how to use the Azure CLI to deploy customized models, see [`az cognitiveservices account deployment`](/cli/azure/cognitiveservices/account/deployment).
-
-To run this Azure CLI command in a console window, you must replace the following _\<placeholders>_ with the corresponding values for your customized model:
+Learn more about cross region deployment and use the deployed model [here](../how-to/fine-tuning-deploy.md#use-your-deployed-fine-tuned-model).
 
-| Placeholder | Value |
-| --- | --- |
-| _\<YOUR_AZURE_SUBSCRIPTION>_ | The name or ID of your Azure subscription. |
-| _\<YOUR_RESOURCE_GROUP>_ | The name of your Azure resource group. |
-| _\<YOUR_RESOURCE_NAME>_ | The name of your Azure OpenAI resource. |
-| _\<YOUR_DEPLOYMENT_NAME>_ | The name you want to use for your model deployment. |
-| _\<YOUR_FINE_TUNED_MODEL_ID>_ | The name of your customized model. |
-
-```azurecli
-az cognitiveservices account deployment create 
-    --resource-group <YOUR_RESOURCE_GROUP>
-    --name <YOUR_RESOURCE_NAME>  
-    --deployment-name <YOUR_DEPLOYMENT_NAME>
-    --model-name <YOUR_FINE_TUNED_MODEL_ID>
-    --model-version "1" 
-    --model-format OpenAI 
-    --sku-capacity "1" 
-    --sku-name "Standard"
-```
 
-## Use a deployed customized model
+## Continuous fine-tuning
 
-After your custom model deploys, you can use it like any other deployed model. You can use the **Chat Playground** in [Azure AI Foundry](https://ai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models.
+Once you have created a fine-tuned model you might want to continue to refine the model over time through further fine-tuning. Continuous fine-tuning is the iterative process of selecting an already fine-tuned model as a base model and fine-tuning it further on new sets of training examples.
 
-# [OpenAI Python 1.x](#tab/python-new)
+To perform fine-tuning on a model that you have previously fine-tuned you would use the same process as described in [create a customized model](#create-a-customized-model) but instead of specifying the name of a generic base model you would specify your already fine-tuned model's ID. The fine-tuned model ID looks like `gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7`
 
 ```python
-import os
 from openai import AzureOpenAI
 
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-02-01"
-)
-
-response = client.chat.completions.create(
-    model="gpt-35-turbo-ft", # model = "Custom deployment name you chose for your fine-tuning model"
-    messages=[
-        {"role": "system", "content": "You are a helpful assistant."},
-        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
-        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
-        {"role": "user", "content": "Do other Azure AI services support this too?"}
-    ]
+  api_version="2024-02-01"  
 )
 
-print(response.choices[0].message.content)
-```
-
-# [OpenAI Python 0.28.1](#tab/python)
-
-```python
-import os
-import openai
-openai.api_type = "azure"
-openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") 
-openai.api_version = "2024-02-01"
-openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
-
-response = openai.ChatCompletion.create(
-    engine="gpt-35-turbo-ft", # engine = "Custom deployment name you chose for your fine-tuning model"
-    messages=[
-        {"role": "system", "content": "You are a helpful assistant."},
-        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
-        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
-        {"role": "user", "content": "Do other Azure AI services support this too?"}
-    ]
+response = client.fine_tuning.jobs.create(
+    training_file=training_file_id,
+    validation_file=validation_file_id,
+    model="gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7" # Enter base model name. Note that in Azure OpenAI the model name contains dashes and cannot contain dot/period characters. 
 )
 
-print(response)
-print(response['choices'][0]['message']['content'])
-```
-
----
-
-## Analyze your customized model
-
-Azure OpenAI attaches a result file named _results.csv_ to each fine-tune job after it completes. You can use the result file to analyze the training and validation performance of your customized model. The file ID for the result file is listed for each customized model, and you can use the Python SDK to retrieve the file ID and download the result file for analysis.
-
-The following Python example retrieves the file ID of the first result file attached to the fine-tuning job for your customized model, and then uses the Python SDK to download the file to your working directory for analysis.
-
-# [OpenAI Python 1.x](#tab/python-new)
-
-```python
-# Retrieve the file ID of the first result file from the fine-tuning job
-# for the customized model.
-response = client.fine_tuning.jobs.retrieve(job_id)
-if response.status == 'succeeded':
-    result_file_id = response.result_files[0]
-
-retrieve = client.files.retrieve(result_file_id)
-
-# Download the result file.
-print(f'Downloading result file: {result_file_id}')
-
-with open(retrieve.filename, "wb") as file:
-    result = client.files.content(result_file_id).read()
-    file.write(result)
-```
+job_id = response.id
 
-# [OpenAI Python 0.28.1](#tab/python)
+# You can use the job ID to monitor the status of the fine-tuning job.
+# The fine-tuning job will take some time to start and complete.
 
-```python
-# Retrieve the file ID of the first result file from the fine-tune job
-# for the customized model.
-response = openai.FineTuningJob.retrieve(job_id)
-if response["status"] == 'succeeded':
-    result_file_id = response.result_files[0].id
-    result_file_name = response.result_files[0].filename
+print("Job ID:", response.id)
+print("Status:", response.id)
+print(response.model_dump_json(indent=2))
 
-# Download the result file.
-print(f'Downloading result file: {result_file_id}')
-# Write the byte array returned by the File.download() method to 
-# a local file in the working directory.
-with open(result_file_name, "wb") as file:
-    result = openai.File.download(id=result_file_id)
-    file.write(result)
 ```
 
----
-
-The result file is a CSV file that contains a header row and a row for each training step performed by the fine-tuning job. The result file contains the following columns:
-
-| Column name | Description |
-| --- | --- |
-| `step` | The number of the training step. A training step represents a single pass, forward and backward, on a batch of training data. |
-| `train_loss` | The loss for the training batch. |
-| `train_mean_token_accuracy` | The percentage of tokens in the training batch correctly predicted by the model.<br>For example, if the batch size is set to 3 and your data contains completions `[[1, 2], [0, 5], [4, 2]]`, this value is set to 0.83 (5 of 6) if the model predicted `[[1, 1], [0, 5], [4, 2]]`. |
-| `valid_loss` | The loss for the validation batch. |
-| `validation_mean_token_accuracy` | The percentage of tokens in the validation batch correctly predicted by the model.<br>For example, if the batch size is set to 3 and your data contains completions `[[1, 2], [0, 5], [4, 2]]`, this value is set to 0.83 (5 of 6) if the model predicted `[[1, 1], [0, 5], [4, 2]]`. |
-| `full_valid_loss` | The validation loss calculated at the end of each epoch. When training goes well, loss should decrease. |
-|`full_valid_mean_token_accuracy` | The valid mean token accuracy calculated at the end of each epoch. When training is going well, token accuracy should increase. |
-
-You can also view the data in your results.csv file as plots in Azure AI Foundry portal. Select the link for your trained model, and you will see three charts: loss, mean token accuracy, and token accuracy. If you provided validation data, both datasets will appear on the same plot.
+We also recommend including the `suffix` parameter to make it easier to distinguish between different iterations of your fine-tuned model. `suffix` takes a string, and is set to identify the fine-tuned model. With the OpenAI Python API a string of up to 18 characters is supported that will be added to your fine-tuned model name.
 
-Look for your loss to decrease over time, and your accuracy to increase. If you see a divergence between your training and validation data that can indicate that you are overfitting. Try training with fewer epochs, or a smaller learning rate multiplier.
+If you are unsure of the ID of your existing fine-tuned model this information can be found in the **Models** page of Azure AI Foundry, or you can generate a [list of models](/rest/api/azureopenai/models/list?view=rest-azureopenai-2023-12-01-preview&tabs=HTTP&preserve-view=true) for a given Azure OpenAI resource using the REST API.
 
 ## Clean up your deployments, customized models, and training files
 
@@ -701,39 +459,3 @@ print(f'Deleting already uploaded files.')
 for id in results:
     openai.File.delete(sid = id)
 ```
-
-## Continuous fine-tuning
-
-Once you have created a fine-tuned model you might want to continue to refine the model over time through further fine-tuning. Continuous fine-tuning is the iterative process of selecting an already fine-tuned model as a base model and fine-tuning it further on new sets of training examples.
-
-To perform fine-tuning on a model that you have previously fine-tuned you would use the same process as described in [create a customized model](#create-a-customized-model) but instead of specifying the name of a generic base model you would specify your already fine-tuned model's ID. The fine-tuned model ID looks like `gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7`
-
-```python
-from openai import AzureOpenAI
-
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
-  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-02-01"  
-)
-
-response = client.fine_tuning.jobs.create(
-    training_file=training_file_id,
-    validation_file=validation_file_id,
-    model="gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7" # Enter base model name. Note that in Azure OpenAI the model name contains dashes and cannot contain dot/period characters. 
-)
-
-job_id = response.id
-
-# You can use the job ID to monitor the status of the fine-tuning job.
-# The fine-tuning job will take some time to start and complete.
-
-print("Job ID:", response.id)
-print("Status:", response.id)
-print(response.model_dump_json(indent=2))
-
-```
-
-We also recommend including the `suffix` parameter to make it easier to distinguish between different iterations of your fine-tuned model. `suffix` takes a string, and is set to identify the fine-tuned model. With the OpenAI Python API a string of up to 18 characters is supported that will be added to your fine-tuned model name.
-
-If you are unsure of the ID of your existing fine-tuned model this information can be found in the **Models** page of Azure AI Foundry, or you can generate a [list of models](/rest/api/azureopenai/models/list?view=rest-azureopenai-2023-12-01-preview&tabs=HTTP&preserve-view=true) for a given Azure OpenAI resource using the REST API.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "ファインチューニング用Python SDKドキュメントの大規模更新"
}
```

### Explanation
「fine-tuning-python.md」というドキュメントが大規模に更新され、多くの重要な変更が加えられました。この改訂では、以下の主要な内容が盛り込まれています。

- **日付の更新**: ドキュメントの日付が2024年3月6日から2025年2月27日に変更されました。
- **セクションタイトルの変更**: 「モデル」セクションが「サポートされるモデル」に改名され、内容の明確化がなされています。
- **実装例の修正**: Python SDKの使用例が更新され、`api_version`が「2024-05-01」から「2024-10-21」に変更されました。これは、新しいAPI機能やエンドポイントに対応するためです。

- **不要なコンテンツの削除**: 古いバージョンのPython SDKに関する例やセクションが削除され、最新の実装にフォーカスが当てられています。この変更により、情報が整理され、ユーザーが最新の方法でファインチューニングを行うための指針が強化されています。

- **結果ファイル分析の強化**: 完了したファインチューニング作業に関連する結果ファイルの取得と分析に関する新しい情報が追加されました。ユーザーは結果ファイルを用いて、モデルのトレーニングと検証のパフォーマンスを詳細に確認できるようになっています。

- **継続的ファインチューニングの追加**: ファインチューニングしたモデルを継続的に改善するためのプロセスが明記され、新たにファインチューニングを行う際の手法についても触れられています。

このような変更により、従来の内容が一新され、ユーザーはAzure OpenAIにおけるファインチューニングの最新かつ最適な方法を学ぶことができるようになります。また、ステップバイステップの手順が強化され、初心者や経験の浅いユーザーが取り組みやすい内容となっています。

## articles/ai-services/openai/includes/fine-tuning-rest.md{#item-9add3e}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ description: Learn how to create your own customized model with Azure OpenAI Ser
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 08/02/2024
+ms.date: 02/27/2025
 author: mrbullwinkle
 ms.author: mbullwin
 ---
@@ -21,7 +21,7 @@ ms.author: mbullwin
 
 
 
-## Models
+### Supported models
 
 The following models support fine-tuning:
 
@@ -53,7 +53,7 @@ Take a moment to review the fine-tuning workflow for using the REST APIS and Pyt
 1. Use your customized model.
 1. Optionally, analyze your customized model for performance and fit.
 
-### Prepare your training and validation data
+## Prepare your training and validation data
 
 Your training data and validation data sets consist of input and output examples for how you would like the model to perform.
 
@@ -101,19 +101,7 @@ The more training examples you have, the better. Fine tuning jobs will not proce
 
 In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively impact performance. If you train the model on a large amount of internal data without first pruning the dataset for only the highest quality examples, you could end up with a model that performs much worse than expected.
 
-### Select the base model
-
-The first step in creating a custom model is to choose a base model. The **Base model** pane lets you choose a base model to use for your custom model. Your choice influences both the performance and the cost of your model.
-
-Select the base model from the **Base model type** dropdown, and then select **Next** to continue.
-
-Or you can fine tune a previously fine-tuned model, formatted as base-model.ft-{jobid}.
-
-:::image type="content" source="../media/fine-tuning/models.png" alt-text="Screenshot of model options with a custom fine-tuned model." lightbox="../media/fine-tuning/models.png":::
-
-For more information about our base models that can be fine-tuned, see [Models](../concepts/models.md).
-
-## Upload your training data
+### Upload your training data
 
 The next step is to either choose existing prepared training data or upload new prepared training data to use when fine-tuning your model. After you prepare your training data, you can upload your files to the service. There are two ways to upload training data:
 
@@ -149,7 +137,7 @@ After you uploaded your training and validation files, you're ready to start the
 In this example we are also passing the seed parameter. The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but can differ in rare cases. If a seed is not specified, one will be generated for you.
 
 ```bash
-curl -X POST $AZURE_OPENAI_ENDPOINT/openai/fine_tuning/jobs?api-version=2024-05-01-preview \
+curl -X POST $AZURE_OPENAI_ENDPOINT/openai/fine_tuning/jobs?api-version=2024-10-21 \
   -H "Content-Type: application/json" \
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -d '{
@@ -176,41 +164,71 @@ The current supported hyperparameters for fine-tuning are:
 After you start a fine-tune job, it can take some time to complete. Your job might be queued behind other jobs in the system. Training your model can take minutes or hours depending on the model and dataset size. The following example uses the REST API to check the status of your fine-tuning job. The example retrieves information about your job by using the job ID returned from the previous example:
 
 ```bash
-curl -X GET $AZURE_OPENAI_ENDPOINT/openai/fine_tuning/jobs/<YOUR-JOB-ID>?api-version=2024-05-01-preview \
+curl -X GET $AZURE_OPENAI_ENDPOINT/openai/fine_tuning/jobs/<YOUR-JOB-ID>?api-version=2024-10-21 \
   -H "api-key: $AZURE_OPENAI_API_KEY"
 ```
 
-## List fine-tuning events
+### List fine-tuning events
 
 To examine the individual fine-tuning events that were generated during training:
 
 ```bash
-curl -X POST $AZURE_OPENAI_ENDPOINT/openai/fine_tuning/jobs/{fine_tuning_job_id}/events?api-version=2024-05-01-preview \
+curl -X POST $AZURE_OPENAI_ENDPOINT/openai/fine_tuning/jobs/{fine_tuning_job_id}/events?api-version=2024-10-21 \
   -H "Content-Type: application/json" \
   -H "api-key: $AZURE_OPENAI_API_KEY" 
 ```
 
 ## Checkpoints
 
-When each training epoch completes a checkpoint is generated. A checkpoint is a fully functional version of a model which can both be deployed and used as the target model for subsequent fine-tuning jobs. Checkpoints can be particularly useful, as they can provide a snapshot of your model prior to overfitting having occurred. When a fine-tuning job completes you will have the three most recent versions of the model available to deploy. The final epoch will be represented by your fine-tuned model, the previous two epochs will be available as checkpoints.
+When each training epoch completes a checkpoint is generated. A checkpoint is a fully functional version of a model which can both be deployed and used as the target model for subsequent fine-tuning jobs. Checkpoints can be particularly useful, as they may provide snapshots prior to overfitting. When a fine-tuning job completes you will have the three most recent versions of the model available to deploy. The final epoch will be represented by your fine-tuned model, the previous two epochs will be available as checkpoints.
 
 You can run the list checkpoints command to retrieve the list of checkpoints associated with an individual fine-tuning job:
 
 ```bash
-curl -X POST $AZURE_OPENAI_ENDPOINT/openai/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints?api-version=2024-05-01-preview \
+curl -X POST $AZURE_OPENAI_ENDPOINT/openai/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints?api-version=2024-10-21 \
   -H "Content-Type: application/json" \
   -H "api-key: $AZURE_OPENAI_API_KEY" 
 ```
 
-## Safety evaluation GPT-4, GPT-4o, GPT-4o-mini fine-tuning - public preview
+## Analyze your customized model
+
+Azure OpenAI attaches a result file named _results.csv_ to each fine-tune job after it completes. You can use the result file to analyze the training and validation performance of your customized model. The file ID for the result file is listed for each customized model, and you can use the REST API to retrieve the file ID and download the result file for analysis.
+
+The following Python example uses the REST API to retrieve the file ID of the first result file attached to the fine-tuning job for your customized model, and then downloads the file to your working directory for analysis.
+
+```bash
+curl -X GET "$AZURE_OPENAI_ENDPOINT/openai/fine_tuning/jobs/<JOB_ID>?api-version=2023-12-01-preview" \
+  -H "api-key: $AZURE_OPENAI_API_KEY")
+```
+
+```bash
+curl -X GET "$AZURE_OPENAI_ENDPOINT/openai/files/<RESULT_FILE_ID>/content?api-version=2023-12-01-preview" \
+    -H "api-key: $AZURE_OPENAI_API_KEY" > <RESULT_FILENAME>
+```
+
+The result file is a CSV file that contains a header row and a row for each training step performed by the fine-tuning job. The result file contains the following columns:
+
+| Column name | Description |
+| --- | --- |
+| `step` | The number of the training step. A training step represents a single pass, forward and backward, on a batch of training data. |
+| `train_loss` | The loss for the training batch. |
+| `train_mean_token_accuracy` | The percentage of tokens in the training batch correctly predicted by the model.<br>For example, if the batch size is set to 3 and your data contains completions `[[1, 2], [0, 5], [4, 2]]`, this value is set to 0.83 (5 of 6) if the model predicted `[[1, 1], [0, 5], [4, 2]]`. |
+| `valid_loss` | The loss for the validation batch. |
+| `validation_mean_token_accuracy` | The percentage of tokens in the validation batch correctly predicted by the model.<br>For example, if the batch size is set to 3 and your data contains completions `[[1, 2], [0, 5], [4, 2]]`, this value is set to 0.83 (5 of 6) if the model predicted `[[1, 1], [0, 5], [4, 2]]`. |
+| `full_valid_loss` | The validation loss calculated at the end of each epoch. When training goes well, loss should decrease. |
+|`full_valid_mean_token_accuracy` | The valid mean token accuracy calculated at the end of each epoch. When training is going well, token accuracy should increase. |
+
+You can also view the data in your results.csv file as plots in Azure AI Foundry portal. Select the link for your trained model, and you will see three charts: loss, mean token accuracy, and token accuracy. If you provided validation data, both datasets will appear on the same plot.
+
+Look for your loss to decrease over time, and your accuracy to increase. If you see a divergence between your training and validation data that may indicate that you are overfitting. Try training with fewer epochs, or a smaller learning rate multiplier.
+
 
-[!INCLUDE [Safety evaluation](../includes/safety-evaluation.md)]
 
 ## Deploy a fine-tuned model
 
 [!INCLUDE [Fine-tuning deletion](fine-tune.md)]
 
-The following Python example shows how to use the REST API to create a model deployment for your customized model. The REST API generates a name for the deployment of your customized model.
+The following example shows how to use the REST API to create a model deployment for your customized model. The REST API generates a name for the deployment of your customized model.
 
 |variable      | Definition|
 |--------------|-----------|
@@ -222,7 +240,7 @@ The following Python example shows how to use the REST API to create a model dep
 | fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It will look like `gpt-35-turbo-0613.ft-b044a9d3cf9c4228b5d393567f693b83`. You'll need to add that value to the deploy_data json. Alternatively you can also deploy a checkpoint, by passing the checkpoint ID which will appear in the format `ftchkpt-e559c011ecc04fc68eaa339d8227d02d` |
 
 ```bash
-curl -X POST "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2023-05-01" \
+curl -X POST "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-21" \
   -H "Authorization: Bearer <TOKEN>" \
   -H "Content-Type: application/json" \
   -d '{
@@ -237,125 +255,30 @@ curl -X POST "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resource
 }'
 ```
 
-### Cross region deployment
-
-Fine-tuning supports deploying a fine-tuned model to a different region than where the model was originally fine-tuned. You can also deploy to a different subscription/region.
-
-The only limitations are that the new region must also support fine-tuning and when deploying cross subscription the account generating the authorization token for the deployment must have access to both the source and destination subscriptions. 
-
-Below is an example of deploying a model that was fine-tuned in one subscription/region to another.
-
-```bash
-curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2023-05-01" \
-  -H "Authorization: Bearer <TOKEN>" \
-  -H "Content-Type: application/json" \
-  -d '{
-    "sku": {"name": "standard", "capacity": 1},
-    "properties": {
-        "model": {
-            "format": "OpenAI",
-            "name": "<FINE_TUNED_MODEL>", 
-            "version": "1",
-            "source": "/subscriptions/{sourceSubscriptionID}/resourceGroups/{sourceResourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{sourceAccount}" 
-        }
-    }
-}'
-```
+Learn more about cross region deployment and use the deployed model [here](../how-to/fine-tuning-deploy.md#use-your-deployed-fine-tuned-model).
 
-To deploy between the same subscription, but different regions, you would just have subscription and resource groups be identical for both source and destination variables and only the source and destination resource names would need to be unique.
 
-### Cross tenant deployment
+## Continuous fine-tuning
 
-The account used to generate access tokens with `az account get-access-token --tenant` should have Cognitive Services OpenAI Contributor permissions to both the source and destination Azure OpenAI resources. You will need to generate two different tokens, one for the source tenant and one for the destination tenant.
+Once you have created a fine-tuned model, you might want to continue to refine the model over time through further fine-tuning. Continuous fine-tuning is the iterative process of selecting an already fine-tuned model as a base model and fine-tuning it further on new sets of training examples.
 
+To perform fine-tuning on a model that you have previously fine-tuned, you would use the same process as described in [create a customized model](#create-a-customized-model) but instead of specifying the name of a generic base model you would specify your already fine-tuned model's ID. The fine-tuned model ID looks like `gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7`
 
 ```bash
-curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>?api-version=2024-10-01" \
-  -H "Authorization: Bearer <DESTINATION TOKEN>" \
-  -H "x-ms-authorization-auxiliary: Bearer <SOURCE TOKEN>" \
+curl -X POST $AZURE_OPENAI_ENDPOINT/openai/fine_tuning/jobs?api-version=2023-12-01-preview \
   -H "Content-Type: application/json" \
+  -H "api-key: $AZURE_OPENAI_API_KEY" \
   -d '{
-    "sku": {"name": "standard", "capacity": 1},
-    "properties": {
-        "model": {
-            "format": "OpenAI",
-            "name": "<FINE_TUNED_MODEL>", 
-            "version": "1",
-            "sourceAccount": "/subscriptions/{sourceSubscriptionID}/resourceGroups/{sourceResourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{sourceAccount}" 
-        }
-    }
+    "model": "gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7", 
+    "training_file": "<TRAINING_FILE_ID>", 
+    "validation_file": "<VALIDATION_FILE_ID>",
+    "suffix": "<additional text used to help identify fine-tuned models>"
 }'
 ```
 
-### Deploy a model with Azure CLI
-
-The following example shows how to use the Azure CLI to deploy your customized model. With the Azure CLI, you must specify a name for the deployment of your customized model. For more information about how to use the Azure CLI to deploy customized models, see [`az cognitiveservices account deployment`](/cli/azure/cognitiveservices/account/deployment).
-
-To run this Azure CLI command in a console window, you must replace the following _\<placeholders>_ with the corresponding values for your customized model:
-
-| Placeholder | Value |
-| --- | --- |
-| _\<YOUR_AZURE_SUBSCRIPTION>_ | The name or ID of your Azure subscription. |
-| _\<YOUR_RESOURCE_GROUP>_ | The name of your Azure resource group. |
-| _\<YOUR_RESOURCE_NAME>_ | The name of your Azure OpenAI resource. |
-| _\<YOUR_DEPLOYMENT_NAME>_ | The name you want to use for your model deployment. |
-| _\<YOUR_FINE_TUNED_MODEL_ID>_ | The name of your customized model. |
-
-```azurecli
-az cognitiveservices account deployment create 
-    --resource-group <YOUR_RESOURCE_GROUP>
-    --name <YOUR_RESOURCE_NAME>  
-    --deployment-name <YOUR_DEPLOYMENT_NAME>
-    --model-name <YOUR_FINE_TUNED_MODEL_ID>
-    --model-version "1" 
-    --model-format OpenAI 
-    --sku-capacity "1" 
-    --sku-name "Standard"
-```
-
-## Use a deployed customized model
-
-After your custom model deploys, you can use it like any other deployed model. You can use the **Chat Playgrounds** in [Azure AI Foundry](https://ai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models.
-
-```bash
-curl $AZURE_OPENAI_ENDPOINT/openai/deployments/<deployment_name>/chat/completions?api-version=2023-05-15 \
-  -H "Content-Type: application/json" \
-  -H "api-key: $AZURE_OPENAI_API_KEY" \
-  -d '{"messages":[{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},{"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},{"role": "user", "content": "Do other Azure AI services support this too?"}]}'
-```
-
-## Analyze your customized model
-
-Azure OpenAI attaches a result file named _results.csv_ to each fine-tune job after it completes. You can use the result file to analyze the training and validation performance of your customized model. The file ID for the result file is listed for each customized model, and you can use the REST API to retrieve the file ID and download the result file for analysis.
-
-The following Python example uses the REST API to retrieve the file ID of the first result file attached to the fine-tuning job for your customized model, and then downloads the file to your working directory for analysis.
-
-```bash
-curl -X GET "$AZURE_OPENAI_ENDPOINT/openai/fine_tuning/jobs/<JOB_ID>?api-version=2023-12-01-preview" \
-  -H "api-key: $AZURE_OPENAI_API_KEY")
-```
-
-```bash
-curl -X GET "$AZURE_OPENAI_ENDPOINT/openai/files/<RESULT_FILE_ID>/content?api-version=2023-12-01-preview" \
-    -H "api-key: $AZURE_OPENAI_API_KEY" > <RESULT_FILENAME>
-```
-
-The result file is a CSV file that contains a header row and a row for each training step performed by the fine-tuning job. The result file contains the following columns:
-
-| Column name | Description |
-| --- | --- |
-| `step` | The number of the training step. A training step represents a single pass, forward and backward, on a batch of training data. |
-| `train_loss` | The loss for the training batch. |
-| `train_mean_token_accuracy` | The percentage of tokens in the training batch correctly predicted by the model.<br>For example, if the batch size is set to 3 and your data contains completions `[[1, 2], [0, 5], [4, 2]]`, this value is set to 0.83 (5 of 6) if the model predicted `[[1, 1], [0, 5], [4, 2]]`. |
-| `valid_loss` | The loss for the validation batch. |
-| `validation_mean_token_accuracy` | The percentage of tokens in the validation batch correctly predicted by the model.<br>For example, if the batch size is set to 3 and your data contains completions `[[1, 2], [0, 5], [4, 2]]`, this value is set to 0.83 (5 of 6) if the model predicted `[[1, 1], [0, 5], [4, 2]]`. |
-| `full_valid_loss` | The validation loss calculated at the end of each epoch. When training goes well, loss should decrease. |
-|`full_valid_mean_token_accuracy` | The valid mean token accuracy calculated at the end of each epoch. When training is going well, token accuracy should increase. |
-
-You can also view the data in your results.csv file as plots in Azure AI Foundry portal. Select the link for your trained model, and you will see three charts: loss, mean token accuracy, and token accuracy. If you provided validation data, both datasets will appear on the same plot.
-
-Look for your loss to decrease over time, and your accuracy to increase. If you see a divergence between your training and validation data that may indicate that you are overfitting. Try training with fewer epochs, or a smaller learning rate multiplier.
+We also recommend including the `suffix` parameter to make it easier to distinguish between different iterations of your fine-tuned model. `suffix` takes a string, and is set to identify the fine-tuned model. The suffix can contain up to 40 characters (a-z, A-Z, 0-9,- and _) that will be added to your fine-tuned model name.
 
+If you're unsure of the ID of your fine-tuned model this information can be found in the **Models** page of Azure AI Foundry, or you can generate a [list of models](/rest/api/azureopenai/models/list?view=rest-azureopenai-2023-12-01-preview&tabs=HTTP&preserve-view=true) for a given Azure OpenAI resource using the REST API.
 
 ## Clean up your deployments, customized models, and training files
 
@@ -382,25 +305,3 @@ Similarly, you can use various methods to delete your customized model:
 You can optionally delete training and validation files that you uploaded for training, and result files generated during training, from your Azure OpenAI subscription. You can use the following methods to delete your training, validation, and result files:
 
 - [Azure AI Foundry](../how-to/fine-tuning.md?pivots=ai-foundry-portal#delete-your-training-files)
-
-## Continuous fine-tuning
-
-Once you have created a fine-tuned model, you might want to continue to refine the model over time through further fine-tuning. Continuous fine-tuning is the iterative process of selecting an already fine-tuned model as a base model and fine-tuning it further on new sets of training examples.
-
-To perform fine-tuning on a model that you have previously fine-tuned, you would use the same process as described in [create a customized model](#create-a-customized-model) but instead of specifying the name of a generic base model you would specify your already fine-tuned model's ID. The fine-tuned model ID looks like `gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7`
-
-```bash
-curl -X POST $AZURE_OPENAI_ENDPOINT/openai/fine_tuning/jobs?api-version=2023-12-01-preview \
-  -H "Content-Type: application/json" \
-  -H "api-key: $AZURE_OPENAI_API_KEY" \
-  -d '{
-    "model": "gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7", 
-    "training_file": "<TRAINING_FILE_ID>", 
-    "validation_file": "<VALIDATION_FILE_ID>",
-    "suffix": "<additional text used to help identify fine-tuned models>"
-}'
-```
-
-We also recommend including the `suffix` parameter to make it easier to distinguish between different iterations of your fine-tuned model. `suffix` takes a string, and is set to identify the fine-tuned model. The suffix can contain up to 40 characters (a-z, A-Z, 0-9,- and _) that will be added to your fine-tuned model name.
-
-If you're unsure of the ID of your fine-tuned model this information can be found in the **Models** page of Azure AI Foundry, or you can generate a [list of models](/rest/api/azureopenai/models/list?view=rest-azureopenai-2023-12-01-preview&tabs=HTTP&preserve-view=true) for a given Azure OpenAI resource using the REST API.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIを使用したファインチューニングドキュメントの更新"
}
```

### Explanation
「fine-tuning-rest.md」ドキュメントが更新され、いくつかの重要な変更が加えられました。以下にその概要を示します。

- **日付の更新**: ドキュメントの日付が2024年8月2日から2025年2月27日に変更されました。
- **セクションタイトルの変更**: 「モデル」というセクションが「サポートされるモデル」に改称され、内容が明確化されています。

- **APIバージョンの更新**: REST APIを呼び出す際の`api-version`が「2024-05-01-preview」から「2024-10-21」に更新され、最新の機能にアクセスできるようになります。

- **新しい手順の追加**: 訓練データのアップロードとファインチューニングジョブの開始に関する手順が整理され、簡潔に説明されています。また、ファインチューニングの結果ファイルの取得方法が追加され、分析に役立てることができるようになっています。

- **モデルのチェックポイントに関する詳細の追加**: 各トレーニングエポックの完了時に生成されるチェックポイントについての説明が強化されています。これにより、モデルの過剰適合を防ぐ方法が具体化され、利用者が自分のモデルの状態を把握しやすくなります。

- **ファインチューニングモデルの識別のためのサフィックスの推奨**: モデルのバージョンを識別するために使用できるサフィックスパラメータの導入が推奨され、最大40文字の文字列を使用してファインチューニングされたモデルを識別できるようになります。

これらの変更により、ユーザーはREST APIを介してのファインチューニングプロセスをよりスムーズに行えるようになります。また、文書全体が最新の情報に基づいて整理され、明確になっています。これにより、初心者や経験の浅いユーザーがAzure OpenAIを利用しやすくなっています。

## articles/ai-services/openai/includes/fine-tuning-studio.md{#item-439f1e}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ description: Learn how to create your own custom model with Azure OpenAI Service
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 10/03/2024
+ms.date: 02/27/2025
 author: mrbullwinkle    
 ms.author: mbullwin
 ---
@@ -19,7 +19,7 @@ ms.author: mbullwin
 - Fine-tuning access requires **Cognitive Services OpenAI Contributor**.
 - If you do not already have access to view quota, and deploy models in Azure AI Foundry portal you will require [additional permissions](../how-to/role-based-access-control.md).  
 
-## Models
+### Supported models
 
 The following models support fine-tuning:
 
@@ -43,7 +43,7 @@ Take a moment to review the fine-tuning workflow for using Azure AI Foundry port
 
 1. Prepare your training and validation data.
 1. Use the **Create custom model** wizard in Azure AI Foundry portal to train your custom model.
-    1. [Select a base model](#select-the-base-model).
+    1. Select a base model.
     1. [Choose your training data](#choose-your-training-data).
     1. Optionally, [choose your validation data](#choose-your-validation-data).
     1. Optionally, [configure task parameters](#configure-task-parameters) for your fine-tuning job.
@@ -59,7 +59,8 @@ Your training data and validation data sets consist of input and output examples
 
 The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document. For `gpt-35-turbo` (all versions), `gpt-4`, `gpt-4o`, and `gpt-4o-mini`, the fine-tuning dataset must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
 
-If you would like a step-by-step walk-through of fine-tuning a `gpt-4o-mini` (2024-07-18) model please refer to the [Azure OpenAI fine-tuning tutorial.](../tutorials/fine-tune.md)
+It's generally recommended to use the instructions and prompts that you found worked best in every training example. This will help you get the best results, especially if you have fewer than a hundred examples.
+
 
 ### Example file format
 
@@ -94,9 +95,9 @@ Multiple turns of a conversation in a single line of your jsonl training file is
 
 In addition to the JSONL format, training and validation data files must be encoded in UTF-8 and include a byte-order mark (BOM). The file must be less than 512 MB in size.
 
-### Create your training and validation datasets
+### Datasets size consideration
 
-The more training examples you have, the better. Fine tuning jobs will not proceed without at least 10 training examples, but such a small number isn't enough to noticeably influence model responses. It is best practice to provide hundreds, if not thousands, of training examples to be successful.
+The more training examples you have, the better. Fine-tuning jobs will not proceed without at least 10 training examples, but such a small number isn't enough to noticeably influence model responses. It is best practice to provide hundreds, if not thousands, of training examples to be successful. It's recommended to start with 50 well-crafted training data.
 
 In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively impact performance. If you train the model on a large amount of internal data, without first pruning the dataset for only the highest quality examples you could end up with a model that performs much worse than expected.
 
@@ -110,19 +111,7 @@ Azure AI Foundry portal provides the **Create custom model** wizard, so you can
 
    :::image type="content" source="../media/fine-tuning/studio-create-custom-model.png" alt-text="Screenshot that shows how to access the Create custom model wizard in Azure AI Foundry portal." lightbox="../media/fine-tuning/studio-create-custom-model.png":::
 
-The **Create custom model** wizard opens.
-
-### Select the base model
-
-The first step in creating a custom model is to choose a base model. The **Base model** pane lets you choose a base model to use for your custom model. Your choice influences both the performance and the cost of your model.
-
-Select the base model from the **Base model type** dropdown, and then select **Next** to continue.
-
-- Or you can fine tune a previously fine-tuned model, formatted as base-model.ft-{jobid}.
-
-:::image type="content" source="../media/fine-tuning/models.png" alt-text="Screenshot of model options with a custom fine-tuned model." lightbox="../media/fine-tuning/models.png":::
-
-For more information about our base models that can be fine-tuned, see [Models](../concepts/models.md#fine-tuning-models).
+1. Select a base model to fine-tune, and then select **Next** to continue.
 
 ### Choose your training data
 
@@ -136,41 +125,15 @@ The next step is to either choose existing prepared training data or upload new
 
 - To upload new training data, use one of the following options:
 
-   - Select **Local file** to [upload training data from a local file](#upload-training-data-from-local-file).
+   - Select **Local file** to upload training data from a local file.
 
-   - Select **Azure blob or other shared web locations** to [import training data from Azure Blob or another shared web location](#import-training-data-from-azure-blob-store).
+   - Select **Azure blob or other shared web locations** to import training data from Azure Blob or another shared web location.
 
 For large data files, we recommend that you import from an Azure Blob store. Large files can become unstable when uploaded through multipart forms because the requests are atomic and can't be retried or resumed. For more information about Azure Blob Storage, see [What is Azure Blob Storage](/azure/storage/blobs/storage-blobs-overview)?
 
 > [!NOTE]
 > Training data files must be formatted as JSONL files, encoded in UTF-8 with a byte-order mark (BOM). The file must be less than 512 MB in size.
 
-#### Upload training data from local file
-
-You can upload a new training dataset to the service from a local file by using one of the following methods:
-
-- Drag and drop the file into the client area of the **Training data** pane, and then select **Upload file**.
-
-- Select **Browse for a file** from the client area of the **Training data** pane, choose the file to upload from the **Open** dialog, and then select **Upload file**.
-
-After you select and upload the training dataset, select **Next** to continue.
-
-:::image type="content" source="../media/fine-tuning/studio-training-data-local.png" alt-text="Screenshot of the Training data pane for the Create custom model wizard, with local file options." lightbox="../media/fine-tuning/studio-training-data-local.png":::
-
-#### Import training data from Azure Blob store
-
-You can import a training dataset from Azure Blob or another shared web location by providing the name and location of the file.
-
-1. Enter the **File name** for the file.
-
-1. For the **File location**, provide the Azure Blob URL, the Azure Storage shared access signature (SAS), or other link to an accessible shared web location.
-
-1. Select **Import** to import the training dataset to the service.
-
-After you select and upload the training dataset, select **Next** to continue.
-
-:::image type="content" source="../media/fine-tuning/studio-training-data-blob.png" alt-text="Screenshot of the Training data pane for the Create custom model wizard, with Azure Blob and shared web location options." lightbox="../media/fine-tuning/studio-training-data-blob.png":::
-
 ### Choose your validation data
 
 The next step provides options to configure the model to use validation data in the training process. If you don't want to use validation data, you can choose **Next** to continue to the advanced options for the model. Otherwise, if you have a validation dataset, you can either choose existing prepared validation data or upload new prepared validation data to use when customizing your model.
@@ -185,41 +148,15 @@ The **Validation data** pane displays any existing, previously uploaded training
 
 - To upload new validation data, use one of the following options:
 
-   - Select **Local file** to [upload validation data from a local file](#upload-validation-data-from-local-file).
+   - Select **Local file** to upload validation data from a local file.
    
-   - Select **Azure blob or other shared web locations** to [import validation data from Azure Blob or another shared web location](#import-validation-data-from-azure-blob-store).
+   - Select **Azure blob or other shared web locations** to import validation data from Azure Blob or another shared web location.
 
 For large data files, we recommend that you import from an Azure Blob store. Large files can become unstable when uploaded through multipart forms because the requests are atomic and can't be retried or resumed.
 
 > [!NOTE]
 > Similar to training data files, validation data files must be formatted as JSONL files, encoded in UTF-8 with a byte-order mark (BOM). The file must be less than 512 MB in size.
 
-#### Upload validation data from local file
-
-You can upload a new validation dataset to the service from a local file by using one of the following methods:
-
-- Drag and drop the file into the client area of the **Validation data** pane, and then select **Upload file**.
-
-- Select **Browse for a file** from the client area of the **Validation data** pane, choose the file to upload from the **Open** dialog, and then select **Upload file**.
-
-After you select and upload the validation dataset, select **Next** to continue.
-
-:::image type="content" source="../media/fine-tuning/studio-validation-data-local.png" alt-text="Screenshot of the Validation data pane for the Create custom model wizard, with local file options." lightbox="../media/fine-tuning/studio-validation-data-local.png":::
-
-#### Import validation data from Azure Blob store
-
-You can import a validation dataset from Azure Blob or another shared web location by providing the name and location of the file.
-
-1. Enter the **File name** for the file.
-
-1. For the **File location**, provide the Azure Blob URL, the Azure Storage shared access signature (SAS), or other link to an accessible shared web location.
-
-1. Select **Import** to import the training dataset to the service.
-
-After you select and upload the validation dataset, select **Next** to continue.
-
-:::image type="content" source="../media/fine-tuning/studio-validation-data-blob.png" alt-text="Screenshot of the Validation data pane for the Create custom model wizard, with Azure Blob and shared web location options." lightbox="../media/fine-tuning/studio-validation-data-blob.png":::
-
 ### Configure task parameters
 
 The **Create custom model** wizard shows the parameters for training your fine-tuned model on the **Task parameters** pane. The following parameters are available:
@@ -243,95 +180,66 @@ After you configure the advanced options, select **Next** to [review your choice
 
 ### Review your choices and train your model
 
-The **Review** pane of the wizard displays information about your configuration choices.
-
-:::image type="content" source="../media/fine-tuning/studio-review.png" alt-text="Screenshot of the Review pane for the Create custom model wizard in Azure AI Foundry portal." lightbox="../media/fine-tuning/studio-review.png":::
-
-If you're ready to train your model, select **Start Training job** to start the fine-tuning job and return to the **Models** pane.
+Review your choices and select **Submit** to start training your new fine-tuned model.
 
 ## Check the status of your custom model
 
-The **Models** pane displays information about your custom model in the **Customized models** tab. The tab includes information about the status and job ID of the fine-tune job for your custom model. When the job completes, the tab displays the file ID of the result file. You might need to select **Refresh** in order to see an updated status for the model training job.
-
-:::image type="content" source="../media/fine-tuning/studio-models-job-running.png" alt-text="Screenshot of the Models pane from Azure AI Foundry portal, with a custom model displayed." lightbox="../media/fine-tuning/studio-models-job-running.png":::
+After you submit your fine-tuning job, you will see a page with details about your fine-tuned model. You can find the status and more information about your fine-tuned model on the **Fine-tuning** page in Azure AI Foundry portal.
 
-After you start a fine-tuning job, it can take some time to complete. Your job might be queued behind other jobs on the system. Training your model can take minutes or hours depending on the model and dataset size.
+Your job might be queued behind other jobs on the system. Training your model can take minutes or hours depending on the model and dataset size.
 
-Here are some of the tasks you can do on the **Models** pane:
-
-- Check the status of the fine-tuning job for your custom model in the **Status** column of the **Customized models** tab.
-
-- In the **Model name** column, select the model name to view more information about the custom model. You can see the status of the fine-tuning job, training results, training events, and hyperparameters used in the job.
-
-- Select **Download training file** to download the training data you used for the model.
-
-- Select **Download results** to download the result file attached to the fine-tuning job for your model and [analyze your custom model](#analyze-your-custom-model) for training and validation performance.
+## Checkpoints
 
-- Select **Refresh** to update the information on the page.
+When each training epoch completes a checkpoint is generated. A checkpoint is a fully functional version of a model which can both be deployed and used as the target model for subsequent fine-tuning jobs. Checkpoints can be particularly useful, as they may provide snapshots prior to overfitting. When a fine-tuning job completes you will have the three most recent versions of the model available to deploy.
 
-:::image type="content" source="../media/fine-tuning/studio-model-details.png" alt-text="Screenshot of the Models pane in Azure AI Foundry portal, with a custom model displayed." lightbox="../media/fine-tuning/studio-models-job-running.png":::
+## Analyze your custom model
 
-## Checkpoints
+Azure OpenAI attaches a result file named _results.csv_ to each fine-tuning job after it completes. You can use the result file to analyze the training and validation performance of your custom model. The file ID for the result file is listed for each custom model in the **Result file Id** column on the **Models** pane for Azure AI Foundry portal. You can use the file ID to identify and download the result file from the **Data files** pane of Azure AI Foundry portal.
 
-When each training epoch completes a checkpoint is generated. A checkpoint is a fully functional version of a model which can both be deployed and used as the target model for subsequent fine-tuning jobs. Checkpoints can be particularly useful, as they can provide a snapshot of your model prior to overfitting having occurred. When a fine-tuning job completes you will have the three most recent versions of the model available to deploy. 
+The result file is a CSV file that contains a header row and a row for each training step performed by the fine-tuning job. The result file contains the following columns:
 
+| Column name | Description |
+| --- | --- |
+| `step` | The number of the training step. A training step represents a single pass, forward and backward, on a batch of training data. |
+| `train_loss` | The loss for the training batch. |
+| `train_mean_token_accuracy` | The percentage of tokens in the training batch correctly predicted by the model.<br>For example, if the batch size is set to 3 and your data contains completions `[[1, 2], [0, 5], [4, 2]]`, this value is set to 0.83 (5 of 6) if the model predicted `[[1, 1], [0, 5], [4, 2]]`. |
+| `valid_loss` | The loss for the validation batch. |
+| `validation_mean_token_accuracy` | The percentage of tokens in the validation batch correctly predicted by the model.<br>For example, if the batch size is set to 3 and your data contains completions `[[1, 2], [0, 5], [4, 2]]`, this value is set to 0.83 (5 of 6) if the model predicted `[[1, 1], [0, 5], [4, 2]]`. |
+| `full_valid_loss` | The validation loss calculated at the end of each epoch. When training goes well, loss should decrease. |
+|`full_valid_mean_token_accuracy` | The valid mean token accuracy calculated at the end of each epoch. When training is going well, token accuracy should increase. |
 
-## Safety evaluation GPT-4, GPT-4o, and GPT-4o-mini fine-tuning - public preview
+You can also view the data in your results.csv file as plots in Azure AI Foundry portal. Select the link for your trained model, and you will see three charts: loss, mean token accuracy, and token accuracy. If you provided validation data, both datasets will appear on the same plot.
 
-[!INCLUDE [Safety evaluation](../includes/safety-evaluation.md)]
+Look for your loss to decrease over time, and your accuracy to increase. If you see a divergence between your training and validation data, that may indicate that you are overfitting. Try training with fewer epochs, or a smaller learning rate multiplier. 
 
 ## Deploy a fine-tuned model
 
 When the fine-tuning job succeeds, you can deploy the custom model from the **Models** pane. You must deploy your custom model to make it available for use with completion calls.
 
 [!INCLUDE [Fine-tuning deletion](fine-tune.md)]
 
-> [!NOTE]
-> Only one deployment is permitted for a custom model. An error message is displayed if you select an already-deployed custom model.
-
-To deploy your custom model, select the custom model to deploy, and then select **Deploy model**.
-
-:::image type="content" source="../media/fine-tuning/studio-models-deploy-model.png" alt-text="Screenshot that shows how to deploy a custom model in Azure AI Foundry portal." lightbox="../media/fine-tuning/studio-models-deploy-model.png":::
-
-The **Deploy model** dialog box opens. In the dialog box, enter your **Deployment name** and then select **Create** to start the deployment of your custom model. 
+To deploy your custom model, select the custom model to deploy, and then select **Deploy**.
 
-:::image type="content" source="../media/fine-tuning/studio-models-deploy.png" alt-text="Screenshot of the Deploy Model dialog in Azure AI Foundry portal." lightbox="../media/fine-tuning/studio-models-deploy.png":::
+The **Deploy model** dialog box opens. In the dialog box, enter your **Deployment name** and then select **Create** to start the deployment of your custom model.
 
 You can monitor the progress of your deployment on the **Deployments** pane in Azure AI Foundry portal.
 
-### Cross region deployment
+### Use a deployed fine-tuned model
 
-Fine-tuning supports deploying a fine-tuned model to a different region than where the model was originally fine-tuned. You can also deploy to a different subscription/region.
+After your fine-tuned model deploys, you can use it like any other deployed model. You can use the **Playground** in [Azure AI Foundry](https://ai.azure.com) to experiment with your new deployment. You can also use the REST API to call your fine-tuned model from your own application. You can even begin to use this new fine-tuned model in your prompt flow to build your generative AI application.
 
-The only limitations are that the new region must also support fine-tuning and when deploying cross subscription the account generating the authorization token for the deployment must have access to both the source and destination subscriptions.
-
-Cross subscription/region deployment can be accomplished via [Python](/azure/ai-services/openai/how-to/fine-tuning?tabs=turbo%2Cpython-new&pivots=programming-language-python#cross-region-deployment) or [REST](/azure/ai-services/openai/how-to/fine-tuning?tabs=turbo%2Cpython-new&pivots=rest-api#cross-region-deployment).
-
-## Use a deployed custom model
-
-After your custom model deploys, you can use it like any other deployed model. You can use the **Playgrounds** in [Azure AI Foundry portal](https://oai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models.
-
-:::image type="content" source="../media/quickstarts/playground-load-new.png" alt-text="Screenshot of the Playground pane in Azure AI Foundry portal, with sections highlighted." lightbox="../media/quickstarts/playground-load-new.png":::
-
-## Analyze your custom model
+> [!NOTE]
+> For chat models, the [system message that you use to guide your fine-tuned model](../concepts/system-message.md) (whether it's deployed or available for testing in the playground) must be the same as the system message you used for training. If you use a different system message, the model might not perform as expected.
 
-Azure OpenAI attaches a result file named _results.csv_ to each fine-tuning job after it completes. You can use the result file to analyze the training and validation performance of your custom model. The file ID for the result file is listed for each custom model in the **Result file Id** column on the **Models** pane for Azure AI Foundry portal. You can use the file ID to identify and download the result file from the **Data files** pane of Azure AI Foundry portal.
+## Continuous fine-tuning
 
-The result file is a CSV file that contains a header row and a row for each training step performed by the fine-tuning job. The result file contains the following columns:
+Once you have created a fine-tuned model you may wish to continue to refine the model over time through further fine-tuning. Continuous fine-tuning is the iterative process of selecting an already fine-tuned model as a base model and fine-tuning it further on new sets of training examples.
 
-| Column name | Description |
-| --- | --- |
-| `step` | The number of the training step. A training step represents a single pass, forward and backward, on a batch of training data. |
-| `train_loss` | The loss for the training batch. |
-| `train_mean_token_accuracy` | The percentage of tokens in the training batch correctly predicted by the model.<br>For example, if the batch size is set to 3 and your data contains completions `[[1, 2], [0, 5], [4, 2]]`, this value is set to 0.83 (5 of 6) if the model predicted `[[1, 1], [0, 5], [4, 2]]`. |
-| `valid_loss` | The loss for the validation batch. |
-| `validation_mean_token_accuracy` | The percentage of tokens in the validation batch correctly predicted by the model.<br>For example, if the batch size is set to 3 and your data contains completions `[[1, 2], [0, 5], [4, 2]]`, this value is set to 0.83 (5 of 6) if the model predicted `[[1, 1], [0, 5], [4, 2]]`. |
-| `full_valid_loss` | The validation loss calculated at the end of each epoch. When training goes well, loss should decrease. |
-|`full_valid_mean_token_accuracy` | The valid mean token accuracy calculated at the end of each epoch. When training is going well, token accuracy should increase. |
+To perform fine-tuning on a model that you have previously fine-tuned you would use the same process as described in [create a customized model](#use-the-create-custom-model-wizard) but instead of specifying the name of a generic base model you would specify your already fine-tuned model. A custom fine-tuned model would look like `gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7`
 
-You can also view the data in your results.csv file as plots in Azure AI Foundry portal. Select the link for your trained model, and you will see three charts: loss, mean token accuracy, and token accuracy. If you provided validation data, both datasets will appear on the same plot.
+:::image type="content" source="../media/fine-tuning/studio-continuous.png" alt-text="Screenshot of the Create a custom model UI with a fine-tuned model highlighted." lightbox="../media/fine-tuning/studio-continuous.png":::
 
-Look for your loss to decrease over time, and your accuracy to increase. If you see a divergence between your training and validation data, that may indicate that you are overfitting. Try training with fewer epochs, or a smaller learning rate multiplier.
+We also recommend including the `suffix` parameter to make it easier to distinguish between different iterations of your fine-tuned model. `suffix` takes a string, and is set to identify the fine-tuned model. With the OpenAI Python API a string of up to 18 characters is supported that will be added to your fine-tuned model name.
 
 ## Clean up your deployments, custom models, and training files
 
@@ -354,13 +262,3 @@ You can delete a custom model on the **Models** pane in Azure AI Foundry portal.
 
 You can optionally delete training and validation files that you uploaded for training, and result files generated during training, on the **Management** > **Data + indexes** pane in Azure AI Foundry portal. Select the file to delete, and then select **Delete** to delete the file.
 
-## Continuous fine-tuning
-
-Once you have created a fine-tuned model you may wish to continue to refine the model over time through further fine-tuning. Continuous fine-tuning is the iterative process of selecting an already fine-tuned model as a base model and fine-tuning it further on new sets of training examples.
-
-To perform fine-tuning on a model that you have previously fine-tuned you would use the same process as described in [create a customized model](#use-the-create-custom-model-wizard) but instead of specifying the name of a generic base model you would specify your already fine-tuned model. A custom fine-tuned model would look like `gpt-35-turbo-0613.ft-5fd1918ee65d4cd38a5dcf6835066ed7`
-
-:::image type="content" source="../media/fine-tuning/studio-continuous.png" alt-text="Screenshot of the Create a custom model UI with a fine-tuned model highlighted." lightbox="../media/fine-tuning/studio-continuous.png":::
-
-We also recommend including the `suffix` parameter to make it easier to distinguish between different iterations of your fine-tuned model. `suffix` takes a string, and is set to identify the fine-tuned model. With the OpenAI Python API a string of up to 18 characters is supported that will be added to your fine-tuned model name.
-
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングスタジオに関するドキュメントの更新"
}
```

### Explanation
「fine-tuning-studio.md」ドキュメントが更新され、以下の重要な変更が加えられました：

- **日付の更新**: ドキュメントの日付が2024年10月3日から2025年2月27日に変更されました。
- **セクションタイトルの変更**: 「モデル」というセクションが「サポートされるモデル」に改名され、内容がより規範的になっています。

- **ファインチューニングの手順の整理**: カスタムモデルの作成プロセスが段階ごとに明確に説明され、ユーザーが追いやすくなりました。特に、基礎モデルの選択やトレーニングデータの選択に関するステップが簡素化されています。

- **データセットに関する詳細の強化**: トレーニングと検証データセットに必要な条件が強調され、例えば、トレーニングデータの数が最低10例必要であること、及び高品質なサンプルが必要であることが強調されています。

- **結果ファイルの解析の強化**: 結果ファイル（_results.csv_）がファインチューニングジョブに関連づけられ、カスタムモデルのトレーニングと検証パフォーマンスを詳しく分析する方法が示されています。

- **サフィックスの使用推奨**: 複数のファインチューニングモデルの管理を容易にするために、`suffix`パラメータを導入し、モデル名に追加することが推奨されています。

- **ページの視覚的情報追加**: スクリーンショットや図が多く使用され、ユーザーがプロセスを視覚的に理解しやすくなっています。

これらの変更により、ドキュメントはユーザーがAzure AI Foundryを使用してファインチューニング機能をより効率的に利用できるように増強されています。全体として、大幅に整理されており、特に初心者や新しいユーザーにとって、理解と実行が容易になるよう配慮されています。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -6,33 +6,35 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 02/06/2025
+ms.date: 03/04/2025
 ---
 
-| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
-| australiaeast      | ✅                       | ✅                       | ✅                       | ✅                            |
-| brazilsouth        | ✅                       | ✅                       | ✅                       | ✅                            |
-| canadacentral      | ✅                       | ✅                       | ✅                       | ✅                            |
-| canadaeast         | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus             | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus2            | ✅                       | ✅                       | ✅                       | ✅                            |
-| francecentral      | ✅                       | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | ✅                       | ✅                       | ✅                       | ✅                            |
-| japaneast          | ✅                       | ✅                       | ✅                       | ✅                            |
-| koreacentral       | ✅                       | ✅                       | ✅                       | ✅                            |
-| northcentralus     | ✅                       | ✅                       | ✅                       | ✅                            |
-| norwayeast         | ✅                       | ✅                       | ✅                       | ✅                            |
-| polandcentral      | ✅                       | ✅                       | ✅                       | ✅                            |
-| southafricanorth   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southcentralus     | ✅                       | ✅                       | ✅                       | ✅                            |
-| southeastasia      | ✅                       | ✅                       | ✅                       | ✅                            |
-| southindia         | ✅                       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandnorth   | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandwest    | ✅                       | ✅                       | ✅                       | ✅                            |
-| uaenorth           | ✅                       | ✅                       | ✅                       | ✅                            |
-| uksouth            | ✅                       | ✅                       | ✅                       | ✅                            |
-| westeurope         | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus             | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                       | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
+| **Region**     | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
+| australiaeast      | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
+| brazilsouth        | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
+| canadacentral      | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
+| canadaeast         | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus             | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus2            | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
+| italynorth         | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
+| japaneast          | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
+| koreacentral       | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
+| northcentralus     | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
+| norwayeast         | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
+| polandcentral      | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
+| southafricanorth   | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southeastasia      | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
+| southindia         | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandnorth   | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandwest    | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| uaenorth           | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
+| uksouth            | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル行列におけるプロビジョニングされたグローバルリージョンの更新"
}
```

### Explanation
「provisioned-global.md」ドキュメントの更新が行われ、以下の変更が加えられました：

- **日付の更新**: ドキュメントの日付が2025年2月6日から2025年3月4日に変更されました。

- **新しいモデル列の追加**: 表のフォーマットが更新され、新たに「o1」というモデルが追加されました。このモデルは、2024年12月17日からの利用が可能です。既存のモデル（gpt-4oやgpt-4o-mini）の情報と共に、どのリージョンで利用できるかを示しています。

- **リージョンごとの提供状況の更新**: 各リージョンにおける新しいモデルの対応状況が追加され、一部のリージョンではo1モデルが不可であることが示されています。また、多くのリージョンで既存のgpt-4oモデルの利用状況も引き続き確認できます。

- **列の構造の改善**: 表中のモデルリストが整理され、異なるモデルバージョンごとの提供状況が一目で確認できるように改善されました。

この更新により、usersが利用可能なモデルの詳細やどのリージョンでどのモデルが利用できるかを容易に理解できる情報が提供され、全体的な可読性が向上しています。また、モデルの日付と供給状況の変化を追跡するのが容易になりました。

## articles/ai-services/openai/media/fine-tuning/fine-tuning-deploy/deploy-dialogue.png{#item-7a5d8d}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "デプロイダイアログの画像を追加"
}
```

### Explanation
ドキュメントに新たに「deploy-dialogue.png」という画像が追加されました。この画像は、ファインチューニング機能のデプロイに関連するダイアログを視覚的に示しています。

- **ファイルの場所**: 画像は「articles/ai-services/openai/media/fine-tuning/fine-tuning-deploy/」ディレクトリに保存されています。

- **ビジュアルリソースの提供**: この画像は、ユーザーがデプロイプロセスをより理解しやすくするための補足として機能します。操作手順やインターフェースが視覚的に示されることで、利用者がファインチューニングモデルをデプロイする際の参考となります。

- **ドキュメントの充実**: 画像の追加により、文書の視覚的な情報が強化され、特にビジュアル学習者にとって、プロセスの理解が容易になります。また、操作時に見かける画面がどのようなものかを事前に知ることができ、ユーザー体験を向上させることに寄与しています。

この変更により、ファインチューニングのデプロイに関連する情報が分かりやすくなり、ユーザーが想定する操作を行いやすくするための重要なリソースが提供されました。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 2/27/2025
+ms.date: 3/04/2025
 ms.author: mbullwin
 ---
 
@@ -94,6 +94,14 @@ The following sections provide you with a quick guide to the default quotas and
 | `o1` & `o1-preview` | Default | 3 M | 500 |
 | `o1-mini`| Default | 5 M | 500 |
 
+### `o3-mini` data zone standard
+
+| Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
+|---|---|:---:|:---:|
+| `o3-mini` | Enterprise agreement | 20 M | 2 K  |
+| `o3-mini` | Default | 2 M | 200 |
+
+
 ### o1-preview & o1-mini standard
 
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オープンAIのクォータと制限の更新"
}
```

### Explanation
「quotas-limits.md」ドキュメントにおいて、以下の変更が行われました：

- **日付の更新**: ドキュメントの日付が2025年2月27日から2025年3月4日に修正されました。

- **新しいモデル情報の追加**: 新たに「o3-mini」モデルに関する情報が追加されました。このモデルには以下のクォータとリクエスト制限が設定されています：
  - **エンタープライズ契約**: 1分あたりのトークン制限は20M、リクエスト数は2K。
  - **デフォルト**: 1分あたりのトークン制限は2M、リクエスト数は200。

- **既存の情報との統合**: 新しい「o3-mini」モデルの情報は、既存の「o1-preview」および「o1-mini」モデルの情報とともに整理され、よりわかりやすく示されています。これにより、ユーザーは異なるモデルのクォータを比較しやすくなります。

この更新により、最新のモデルとその制限が反映されており、ユーザーが自分に適したプランを選択する際の参考となる情報が提供されています。新しいモデルが追加されたことで、クオータに関する理解が深まり、OpenAIのサービスを利用する際の計画が容易になります。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -170,12 +170,28 @@ items:
     items:
       - name: Fine-tuning your model
         href: ./how-to/fine-tuning.md
-        displayName: finetuning 
+        displayName: finetuning, fine-tuning 
+      - name: Deploy your fine-tuned model
+        href: ./how-to/fine-tuning-deploy.md 
+        displayName: finetuning, fine-tuning  
+      - name: Vision fine-tuning
+        href: ./how-to/fine-tuning-vision.md
+        displayName: finetuning, fine-tuning  
+      - name: Preference fine-tuning
+        href: ./how-to/fine-tuning-direct-preference-optimization.md
+        displayName: finetuning, fine-tuning  
+      - name: Safety evaluation
+        href: ./how-to/fine-tuning-safety-evaluation.md
+        displayName: finetuning, fine-tuning  
       - name: Tool calling
         href: ./how-to/fine-tuning-functions.md
         displayName: fine-tuning, finetuning, function calling
       - name: Weights & Biases integration (preview)
         href: ./how-to/weights-and-biases-integration.md
+        displayName: finetuning, fine-tuning  
+      - name: Troubleshooting guidance
+        href: ./how-to/fine-tuning-troubleshoot.md
+        displayName: finetuning, fine-tuning  
   - name: Stored completions
     href: ./how-to/stored-completions.md
   - name: Use your data
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新とファインチューニングセクションの改善"
}
```

### Explanation
「toc.yml」ファイルに対する次の変更が行われました：

- **新しい項目の追加**: ファインチューニングに関連する複数の新しいセクションが追加されました。具体的には以下の内容です：
  - **チューニングされたモデルのデプロイ**
  - **ビジョンファインチューニング**
  - **プリファレンスファインチューニング**
  - **安全性評価**
  - **トラブルシューティングガイダンス**

- **表示名の統一性**: 一部の項目の表示名が「finetuning」と「fine-tuning」の両方を含むように修正され、表現の一貫性が向上しました。

- **リンクの整理**: 各項目に対するリンクが更新され、ユーザーが関連するリソースに迅速にアクセスできるように改善されました。

この更新により、目次がより包括的になり、ファインチューニングに関する情報へのアクセスが容易になりました。新しい項目の追加は、ユーザーがファインチューニングのプロセスを学ぶ上での参考となるリソースを提供し、全体的なユーザーエクスペリエンスの向上に寄与しています。表示名の改善も、情報の明確性を高めるための重要なステップです。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -92,7 +92,7 @@ To learn more about the advanced `o1` series models see, [getting started with o
 
 ### Preference fine-tuning (preview)
 
-[Direct preference optimization (DPO)](./how-to/fine-tuning.md#direct-preference-optimization-dpo-preview) is a new alignment technique for large language models, designed to adjust model weights based on human preferences. Unlike reinforcement learning from human feedback (RLHF), DPO does not require fitting a reward model and uses simpler data (binary preferences) for training. This method is computationally lighter and faster, making it equally effective at alignment while being more efficient. DPO is especially useful in scenarios where subjective elements like tone, style, or specific content preferences are important. We’re excited to announce the public preview of DPO in Azure OpenAI Service, starting with the `gpt-4o-2024-08-06` model.
+[Direct preference optimization (DPO)](./how-to/fine-tuning-direct-preference-optimization.md) is a new alignment technique for large language models, designed to adjust model weights based on human preferences. Unlike reinforcement learning from human feedback (RLHF), DPO does not require fitting a reward model and uses simpler data (binary preferences) for training. This method is computationally lighter and faster, making it equally effective at alignment while being more efficient. DPO is especially useful in scenarios where subjective elements like tone, style, or specific content preferences are important. We’re excited to announce the public preview of DPO in Azure OpenAI Service, starting with the `gpt-4o-2024-08-06` model.
 
 For fine-tuning model region availability, see the [models page](./concepts/models.md#fine-tuning-models).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DPOリファレンスのリンク修正"
}
```

### Explanation
「whats-new.md」ファイルにおいて、以下の変更が行われました：

- **リンクの修正**: 「Direct preference optimization (DPO)」についての説明文中に含まれていた参照リンクが、以前の「fine-tuning.md」から新しい「fine-tuning-direct-preference-optimization.md」に変更されました。この修正により、DPOに関する情報への直接的なアクセスが可能になっています。

- **内容の一貫性**: DPOの説明内容自体には変更がないため、技術的な詳細やその意義は引き続き同じで、ユーザーは新しいリンクを通じて最新情報を得ることができます。

この更新は、ユーザーがDPOの手法についての正確なリソースに容易にアクセスできるようにするためのものであり、情報の整合性を保つ上で重要です。新しいリンクは、DPOのプレビューに関する情報をより迅速に参照するために役立ちます。


