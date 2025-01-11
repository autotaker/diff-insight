---
date: '2025-01-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1227d31...MicrosoftDocs:28bc1fd
summary: 今回の変更では、ドキュメントとサンプルコードに軽微な修正と追加が行われました。特にC#用のAzure AI推論パッケージに関する情報が多くのドキュメントに追加され、管理されたモデルデプロイメント向けの自動スケーリング設定が新たに導入されました。また、Azure
  CLIコマンドの設定についても明確化が図られ、関連するリンクタイトルも修正されています。これにより、特にC#開発者向けの情報が充実し、設定プロセスの理解を助け、ユーザーエクスペリエンスが向上することが期待されます。破壊的な変更は報告されていません。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1227d31...MicrosoftDocs:28bc1fd){target="_blank"}

<format>
# ハイライト
今回の変更は、ドキュメントおよびサンプルコードにおいて軽微な修正と追加が行われた内容です。特にC#用のAzure AI推論パッケージに関する情報が多くのドキュメントに追加されたことが特徴です。また、特定のAzure CLIコマンドの更新や自動スケーリングの設定セクションの追加なども含まれています。

## 新機能
- Cohere、Jais、Meta Llama、Mistral、Phi-3、Phi-4モデルにC#用Azure AI推論パッケージに関する情報を追加。
- 管理されたモデルデプロイメント用に自動スケーリングの設定方法について新しいセクションを追加。

## 破壊的変更
- 特に破壊的変更は報告されていません。

## その他の更新
- Azure CLIコマンドの`--provision-network-now`フラグ設定の明確化。
- "チャットアプリをAzureにデプロイする"リンクタイトルを"チャットアプリをAzureに評価する"に修正。

# 洞察
今回の変更により、Azure AI推論モデルのドキュメントが他のプログラミング言語との統一性を高め、より広範な開発者層への対応が強化されています。特にC#開発者向けの情報が充実し、各モデルの実装例がGitHubリンクを通じて明確に案内されています。これにより、C#言語を使用するユーザーが、適切なリソースに容易にアクセスできる環境が整います。

また、マネージドネットワークに関するCLIコマンドの明確化は、ユーザーにとって設定プロセスを自動化する際の正確な操作を支援します。これにより、プロビジョニングの誤解を避け、システムの円滑な運用を促進します。

自動スケーリングセクションの追加は、リソース使用の最適化に関する情報を提供し、ユーザーがパフォーマンスを維持しつつ経済的にサービスを運用する助けとなります。変更においては、ユーザーがドキュメントの内容をより理解しやすくするために、リンクの表現をより適切なものに修正するなど、細部にも注意が払われています。これらの調整は、ユーザーエクスペリエンスの向上につながるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [configure-managed-network.md](#item-dc9c50) | minor update | マネージドネットワークの構成方法に関するコマンドの更新 | modified | 2 | 2 | 4 | 
| [deploy-models-cohere-command.md](#item-3e97f4) | minor update | C#用のAzure AI推論パッケージに関する情報の追加 | modified | 1 | 0 | 1 | 
| [deploy-models-cohere-embed.md](#item-eab662) | minor update | C#用のAzure AI推論パッケージに関する情報の追加 | modified | 1 | 0 | 1 | 
| [deploy-models-jais.md](#item-0bd11f) | minor update | C#用のAzure AI推論パッケージに関する情報の追加 | modified | 1 | 0 | 1 | 
| [deploy-models-llama.md](#item-6274a7) | minor update | C#用のAzure AI推論パッケージに関する情報の追加 | modified | 1 | 0 | 1 | 
| [deploy-models-managed.md](#item-3ddb5f) | minor update | 自動スケーリングの設定に関するセクションの追加 | modified | 4 | 0 | 4 | 
| [deploy-models-mistral-nemo.md](#item-e7b729) | minor update | C#用のAzure AI推論パッケージに関する情報の追加 | modified | 1 | 0 | 1 | 
| [deploy-models-mistral-open.md](#item-84e005) | minor update | C#用のAzure AI推論パッケージに関する情報の追加 | modified | 1 | 0 | 1 | 
| [deploy-models-mistral.md](#item-487a41) | minor update | C#用のAzure AI推論パッケージに関する情報の追加 | modified | 1 | 0 | 1 | 
| [deploy-models-phi-3-5-vision.md](#item-8d6d7d) | minor update | C#用のAzure AI推論パッケージに関する情報の追加 | modified | 1 | 0 | 1 | 
| [deploy-models-phi-3-vision.md](#item-bd5aae) | minor update | C#用のAzure AI推論パッケージに関する情報の追加 | modified | 1 | 0 | 1 | 
| [deploy-models-phi-3.md](#item-47e305) | minor update | C#用のAzure AI推論パッケージに関する情報の追加 | modified | 1 | 0 | 1 | 
| [deploy-models-phi-4.md](#item-c40212) | minor update | C#用のAzure AI推論パッケージに関する情報の追加 | modified | 1 | 0 | 1 | 
| [copilot-sdk-build-rag.md](#item-b77dba) | minor update | リンクタイトルの変更 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-studio/how-to/configure-managed-network.md{#item-dc9c50}

<details>
<summary>Diff</summary>
````diff
@@ -634,7 +634,7 @@ During hub creation, select __Provision managed network proactively at creation_
 The following example shows how to provision a managed virtual network during hub creation. The `--provision-network-now` flag is in preview.
     
 ```azurecli
-az ml workspace create -n myworkspace -g my_resource_group --kind hub --managed-network AllowInternetOutbound --provision-network-now
+az ml workspace create -n myworkspace -g my_resource_group --kind hub --managed-network AllowInternetOutbound --provision-network-now true
 ```
 
 The following example shows how to provision a managed virtual network.
@@ -654,7 +654,7 @@ az ml workspace show -n my_ai_hub_name -g my_resource_group --query managed_netw
 The following example shows how to provision a managed virtual network during hub creation. The `--provision-network-now` flag is in preview.
     
 ```azurecli
-az ml workspace create -n myworkspace -g my_resource_group --managed-network AllowInternetOutbound --provision-network-now
+az ml workspace create -n myworkspace -g my_resource_group --managed-network AllowInternetOutbound --provision-network-now true
 ```
 
 The following example shows how to provision a managed virtual network:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージドネットワークの構成方法に関するコマンドの更新"
}
```

### Explanation
この変更は、マネージドネットワークを構成する際のAzure CLIコマンドの一部に修正が行われたものです。具体的には、`--provision-network-now` フラグが `true` に設定されるように、コマンドの書き方が更新されています。この変更により、コマンドの動作が明確になり、利用者にはより正確な実行が要求されることとなります。ファイル内では、コマンドの二箇所でこの修正が適用されており、全体の変更行数は4行に及びます。この更新は、文書に対して少しの改善をもたらすマイナーなアップデートとして位置付けられています。

## articles/ai-studio/how-to/deploy-models-cohere-command.md{#item-3e97f4}

<details>
<summary>Diff</summary>
````diff
@@ -2129,6 +2129,7 @@ For more examples of how to use Cohere models, see the following examples and tu
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | Web requests                              | Bash              | [Command-R](https://aka.ms/samples/cohere-command-r/webrequests) - [Command-R+](https://aka.ms/samples/cohere-command-r-plus/webrequests) |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
 | Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)      |
 | OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/samples/cohere-command/openaisdk)             |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#用のAzure AI推論パッケージに関する情報の追加"
}
```

### Explanation
この変更は、Cohereモデルの使用方法に関するドキュメントにC#用のAzure AI推論パッケージを追加したものです。具体的には、表の中にC#における推論パッケージについての説明とそのリンクが追加されました。このリンクは、C#のサンプルが GitHub にある Azure SDK の中に含まれていることを示しています。全体として、これはマイナーな更新であり、他のプログラミング言語での推論パッケージの情報と同様に、C#に関連するリソースを読者に提供することを目的としています。今回の変更により、Cohereモデルを利用する際の情報がさらに充実し、利用者にとって便利なリソースが提供されています。

## articles/ai-studio/how-to/deploy-models-cohere-embed.md{#item-eab662}

<details>
<summary>Diff</summary>
````diff
@@ -631,6 +631,7 @@ Cohere Embed V3 models can optimize the embeddings based on its use case.
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | Web requests                              | Bash              | [cohere-embed.ipynb](https://aka.ms/samples/embed-v3/webrequests) |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
 | Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)      |
 | OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/samples/cohere-embed/openaisdk)             |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#用のAzure AI推論パッケージに関する情報の追加"
}
```

### Explanation
この変更は、Cohere Embed V3モデルの使用に関するドキュメントにおいて、C#用のAzure AI推論パッケージについての情報を追加したものです。具体的には、推論パッケージの説明と、そのサンプルへのリンクが歓迎されています。このリンクは、C#のサンプルが GitHub 上の Azure SDK 内にあることを示しています。この更新は、他のプログラミング言語におけるリソースと同様に、C#に関連するサンプルを提供することで、ユーザーがCohere Embedモデルを活用する際の便宜を図ることを目的としています。このようにして、利用者は様々な言語に対する情報を容易に得ることができるようになります。

## articles/ai-studio/how-to/deploy-models-jais.md{#item-0bd11f}

<details>
<summary>Diff</summary>
````diff
@@ -1169,6 +1169,7 @@ For more examples of how to use Jais models, see the following examples and tuto
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
 | Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#用のAzure AI推論パッケージに関する情報の追加"
}
```

### Explanation
この変更は、Jaisモデルの使用方法に関するドキュメントで、C#用のAzure AI推論パッケージについての情報を新たに追加したものです。具体的には、Jaisモデルを利用する際に役立つリソースを示す表に、C#向けの関連リンクが挿入されています。このリンクは、C#のサンプルが GitHub の Azure SDK に存在することを示しています。このマイナーな更新により、ユーザーはJaisモデルを活用する際の参考情報をより豊富に得ることができ、様々なプログラミング言語での推論パッケージのリソースにアクセスしやすくなります。

## articles/ai-studio/how-to/deploy-models-llama.md{#item-6274a7}

<details>
<summary>Diff</summary>
````diff
@@ -1464,6 +1464,7 @@ For more examples of how to use Meta Llama models, see the following examples an
 | Description                               | Language          | Sample                                                             |
 |-------------------------------------------|-------------------|------------------------------------------------------------------- |
 | CURL request                              | Bash              | [Link](https://aka.ms/meta-llama-3.1-405B-instruct-webrequests)    |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
 | Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azureml-examples/blob/main/sdk/typescript/README.md) |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)     |
 | Python web requests                       | Python            | [Link](https://aka.ms/meta-llama-3.1-405B-instruct-webrequests)    |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#用のAzure AI推論パッケージに関する情報の追加"
}
```

### Explanation
この変更は、Meta Llamaモデルを使用するためのドキュメントにおいて、C#用のAzure AI推論パッケージに関する情報を新たに追加したものです。具体的には、モデルの利用例やチュートリアルを示すテーブルに、C#向けのリンクが挿入されています。このリンクは、C#のサンプルが GitHub の Azure SDK 内に存在することを示しています。この更新により、ユーザーはMeta Llamaモデルを効率的に活用するためのリソースをより多く得ることができ、様々なプログラミング言語にわたる情報へのアクセスが容易になります。

## articles/ai-studio/how-to/deploy-models-managed.md{#item-3ddb5f}

<details>
<summary>Diff</summary>
````diff
@@ -151,6 +151,10 @@ response_json = json.loads(response)
 print(json.dumps(response_json, indent=2))
 ```
 
+## Configure Autoscaling
+
+To configure autoscaling for deployments, you can go to Azure Portal, locate the Azure resource typed `Machine learning online deployment` in the resource group of the AI project, and use Scaling menu under Setting. For more information on autoscaling, see [Autoscale online endpoints](/azure/machine-learning/how-to-autoscale-endpoints) in the Azure Machine Learning documentation. 
+
 ## Delete the deployment endpoint
 
 To delete deployments in Azure AI Foundry portal, select the **Delete** button on the top panel of the deployment details page.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "自動スケーリングの設定に関するセクションの追加"
}
```

### Explanation
この変更は、管理されたモデルのデプロイメントに関するドキュメントに自動スケーリングの設定に関するセクションを新たに追加したものです。具体的には、Azureポータルを使用してAIプロジェクトのリソースグループ内にある「機械学習オンラインデプロイメント」リソースを見つけ、設定の下にあるスケーリングメニューを使用して自動スケーリングを構成する方法が説明されています。また、自動スケーリングに関する詳細情報へのリンクも提供されています。この更新により、ユーザーはデプロイメントのパフォーマンスを最適化するための重要な手段である自動スケーリングの実装を理解しやすくなります。

## articles/ai-studio/how-to/deploy-models-mistral-nemo.md{#item-e7b729}

<details>
<summary>Diff</summary>
````diff
@@ -2016,6 +2016,7 @@ For more examples of how to use Mistral models, see the following examples and t
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | CURL request                              | Bash              | [Link](https://aka.ms/mistral-large/webrequests-sample)         |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
 | Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 | Python web requests                       | Python            | [Link](https://aka.ms/mistral-large/webrequests-sample)         |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#用のAzure AI推論パッケージに関する情報の追加"
}
```

### Explanation
この変更は、Mistralモデルを使用するためのドキュメントにおいて、C#用のAzure AI推論パッケージに関する情報を新たに追加したものです。変更された部分には、モデルの利用例を示すテーブルにC#のサンプルリンクが挿入されています。具体的には、C#向けのパッケージをGitHub上で確認できるリンクが提供されています。この更新によって、ユーザーはMistralモデルを活用できるプログラミング言語の選択肢が広がり、C#の開発者が特定のサンプルを参考にしやすくなります。

## articles/ai-studio/how-to/deploy-models-mistral-open.md{#item-84e005}

<details>
<summary>Diff</summary>
````diff
@@ -1285,6 +1285,7 @@ For more examples of how to use Mistral models, see the following examples and t
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | CURL request                              | Bash              | [Link](https://aka.ms/mistral-large/webrequests-sample)         |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
 | Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 | Python web requests                       | Python            | [Link](https://aka.ms/mistral-large/webrequests-sample)         |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#用のAzure AI推論パッケージに関する情報の追加"
}
```

### Explanation
この変更は、Mistralモデルを活用する方法に関するドキュメントにC#用のAzure AI推論パッケージについての情報を新たに追加したものです。具体的には、モデルの利用例を示すテーブルにC#言語のサンプルへのリンクが追加されています。これにより、C#開発者はAzureのAI推論パッケージをどのように利用できるかを理解しやすくなり、より多様なプログラミング言語での実装例が手に入るようになります。この更新は、Mistralモデルを使用する際の参考情報を強化するものです。

## articles/ai-studio/how-to/deploy-models-mistral.md{#item-487a41}

<details>
<summary>Diff</summary>
````diff
@@ -2216,6 +2216,7 @@ For more examples of how to use Mistral models, see the following examples and t
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | CURL request                              | Bash              | [Link](https://aka.ms/mistral-large/webrequests-sample)         |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
 | Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 | Python web requests                       | Python            | [Link](https://aka.ms/mistral-large/webrequests-sample)         |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#用のAzure AI推論パッケージに関する情報の追加"
}
```

### Explanation
この変更は、Mistralモデルに関するドキュメント内にC#用のAzure AI推論パッケージに関する新しい情報を追加したものです。具体的には、Mistralモデルを使用するための具体例を示したテーブルに、C#プログラミング言語のサンプルリンクが新たに挿入されています。この追加により、C#の開発者はAzure AI推論パッケージの利用方法を理解しやすくなり、より多くのプログラミング言語に対応したリソースを活用できるようになります。この更新は、Mistralモデルに関するユーザーガイドを強化するものです。

## articles/ai-studio/how-to/deploy-models-phi-3-5-vision.md{#item-8d6d7d}

<details>
<summary>Diff</summary>
````diff
@@ -1614,6 +1614,7 @@ For more examples of how to use Phi-3 family models, see the following examples
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | CURL request                              | Bash              | [Link](https://aka.ms/phi-3/webrequests-sample)         |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
 | Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 | Python web requests                       | Python            | [Link](https://aka.ms/phi-3/webrequests-sample)         |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#用のAzure AI推論パッケージに関する情報の追加"
}
```

### Explanation
この変更は、Phi-3ファミリーのモデルを利用する方法に関するドキュメントにC#用のAzure AI推論パッケージに関する情報を追加したものです。具体的には、利用例を示すテーブルにC#のサンプルへのリンクが新たに加えられています。この追加により、C#開発者はPhi-3モデルを効果的に利用するためのリソースをより簡単に見つけることができ、より多様なプログラミング環境での実装をサポートする内容となっています。この更新は、Phi-3モデルに関連するユーザー向けの情報を拡充する役割を果たしています。

## articles/ai-studio/how-to/deploy-models-phi-3-vision.md{#item-bd5aae}

<details>
<summary>Diff</summary>
````diff
@@ -1405,6 +1405,7 @@ For more examples of how to use Phi-3 family models, see the following examples
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | CURL request                              | Bash              | [Link](https://aka.ms/phi-3/webrequests-sample)         |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
 | Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 | Python web requests                       | Python            | [Link](https://aka.ms/phi-3/webrequests-sample)         |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#用のAzure AI推論パッケージに関する情報の追加"
}
```

### Explanation
この変更は、Phi-3ファミリーのモデルを利用する方法に関するドキュメントにC#用のAzure AI推論パッケージの情報を追加したものです。具体的には、サンプルのテーブルにC#プログラミング言語に関するリンクが新たに追加され、C#開発者がMistralモデルを使用する際の具体例が示されています。この更新により、C#を使用するユーザーは、Azure AI推論パッケージの利用方法をよりよく理解し、リソースにアクセスできるようになります。この変更は、Phi-3モデルに関連する開発者向け情報を充実させるための重要な更新です。

## articles/ai-studio/how-to/deploy-models-phi-3.md{#item-47e305}

<details>
<summary>Diff</summary>
````diff
@@ -1458,6 +1458,7 @@ For more examples of how to use Phi-3 family models, see the following examples
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | CURL request                              | Bash              | [Link](https://aka.ms/phi-3/webrequests-sample)         |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
 | Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 | Python web requests                       | Python            | [Link](https://aka.ms/phi-3/webrequests-sample)         |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#用のAzure AI推論パッケージに関する情報の追加"
}
```

### Explanation
この変更は、Phi-3ファミリーのモデルを利用する方法に関するドキュメントにおいて、C#用のAzure AI推論パッケージに関する情報を追加したものです。具体的には、使用例をまとめたテーブルにC#に関連するリンクが新たに組み込まれました。これにより、C#開発者は、Azure AI推論パッケージを活用してモデルを実装する方法をより簡単に理解し、関連するリソースにアクセスすることができます。この更新は、Phi-3モデルの利用を多様なプログラミング環境でサポートするための重要な一歩です。

## articles/ai-studio/how-to/deploy-models-phi-4.md{#item-c40212}

<details>
<summary>Diff</summary>
````diff
@@ -1117,6 +1117,7 @@ For more examples of how to use Phi-4 family models, see the following examples
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | CURL request                              | Bash              | [Link](https://aka.ms/phi-3/webrequests-sample)         |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)   |  
 | Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 | Python web requests                       | Python            | [Link](https://aka.ms/phi-3/webrequests-sample)         |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#用のAzure AI推論パッケージに関する情報の追加"
}
```

### Explanation
この変更は、Phi-4ファミリーのモデルの使用例に関するドキュメントにC#用のAzure AI推論パッケージの情報を追加したものです。具体的には、使用例のテーブルにC#に関するリソースリンクが新たに加えられ、C#開発者がAIモデルを用いる際の具体的な参考情報を得られるようになっています。この更新により、C#を利用するユーザーは、Phi-4モデルを実装する手助けとなる資料にアクセスしやすくなり、より多様なプログラミング環境への対応を図ることができます。これはPhi-4モデルの利用における重要なアップデートです。

## articles/ai-studio/tutorials/copilot-sdk-build-rag.md{#item-b77dba}

<details>
<summary>Diff</summary>
````diff
@@ -186,4 +186,4 @@ But don't delete them yet, if you want to deploy your chat app to Azure in [the
 ## Next step
 
 > [!div class="nextstepaction"]
-> [Part 3: Evaluate and deploy your chat app to Azure](copilot-sdk-evaluate-deploy.md)
+> [Part 3: Evaluate your chat app to Azure](copilot-sdk-evaluate-deploy.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクタイトルの変更"
}
```

### Explanation
この変更は、Copilot SDKを使用してRAG（Retrieval-Augmented Generation）システムを構築するためのチュートリアルにおいて、次のステップとしてのリンクタイトルを修正したものです。具体的には、「チャットアプリをAzureにデプロイする」という表現から「チャットアプリをAzureに評価する」という表現に変更されました。この修正により、次のステップの内容がより明確に示され、ユーザーが期待するアクションに対する理解が深まることを意図しています。このような細かな修正は、ドキュメントの正確性を向上させるために重要です。


