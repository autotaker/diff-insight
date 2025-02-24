---
date: '2025-02-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b49c252...MicrosoftDocs:8c6e364
summary: 今回の更新では、複数の記事とメディアファイルに関する改訂や新機能の追加が行われました。特に、クラウド評価に関する新しい記事が追加され、Azure
  AI Projects SDKを用いた評価手順が詳しく解説されています。また、チャット出力定義に関連する画像も新たに導入されました。さらに、Evaluate SDKに関するドキュメントが大幅に改訂され、ローカル評価に注力されることとなり、一部の情報が削除されました。その他にも、リダイレクト設定の追加やドキュメントの可読性向上、画像処理に関する具体的なコード例の追加、目次構造の更新が行われています。これらの改訂を通じて、ユーザーの利便性が向上し、AIスタジオの活用が一層進むことが期待されます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b49c252...MicrosoftDocs:8c6e364){target="_blank"}

<format>
# Highlights
この差分では、複数の記事とメディアファイルに関する更新や新しい機能の追加が行われました。主な新機能として、クラウド評価に関する記事が新たに追加され、チャット出力定義に関する画像が初めて導入されました。また、Evaluate SDKに関するドキュメントの大幅な改訂も行われ、変更内容の中には破壊的変更があります。

## New features
- クラウド評価に関する新しい記事が追加され、Azure AI Projects SDKを利用した評価手順が詳細に解説されています。
- チャット出力定義に関連する新しい画像ファイルが導入され、チャットボットの実装などに視覚的に情報を伝えるサポートを提供します。

## Breaking changes
- 「Evaluate SDK」に関するドキュメントは完全に再構築され、ローカル評価に焦点が移されました。これにより、従来の構造やプロンプトフローSDKからの情報が大幅に削除されています。

## Other updates
- リダイレクト設定が追加され、ユーザーの遷移をスムーズにするための調整が行われました。
- トレースおよびメトリクス収集のドキュメントがマイナーに更新され、情報の可読性が向上しました。
- 画像処理に関するドキュメントでは、具体的なコード例が追加され、ユーザーが実践的に利用できる情報が増えました。
- 目次の構造もアップデートされ、新しい記事へのリンクが設定されています。

# Insights
今回のコード差分における最も大きな焦点は、Azure AI関連サービスの利用効率を高めるためのドキュメント強化と、新しい評価プロセスの説明にあります。特に、新しく追加されたクラウド評価に関する記事は、Azure AI Projects SDKの利用を具体的にする情報を提供し、開発者のニーズに応える内容となっています。このような情報の追加によって、ユーザーはクラウド環境での評価プロセスを容易に理解し、実行できるようになります。

また、Evaluate SDKに関するドキュメントの完全な見直しは、従来の情報を再構成し、より直接的かつ効率的にローカル環境での評価を行えるようになっています。この変更により、一部の情報が削除されることで、ユーザーはより焦点を絞った・必要な内容に直接アクセスできるようになり、ドキュメントの利用効率が向上しています。

さらに、画像の更新や追加は、視覚的なサポートを提供し、ユーザーが情報を直感的に理解するための助けとなります。これらは、AIスタジオの全体的なユーザー体験を改善し、新機能の提供や既存機能の理解をサポートする重要な役割を果たしています。全体として、これらの更新は、利用者がより効果的にAIスタジオを活用し、自分のプロジェクトを進めるための巨大な一歩であると言えます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [.openpublishing.redirection.ai-studio.json](#item-c75c21) | minor update | リダイレクト設定の追加 | modified | 10 | 0 | 10 | 
| [cloud-evaluation.md](#item-07f28c) | new feature | クラウド評価に関する新しい記事の追加 | added | 284 | 0 | 284 | 
| [evaluate-sdk.md](#item-9d5197) | breaking change | Evaluate SDKの大幅な改訂 | modified | 27 | 298 | 325 | 
| [trace-production-sdk.md](#item-8d5b4c) | minor update | トレースおよびメトリクス収集に関するドキュメントの改善 | modified | 17 | 16 | 33 | 
| [flow-process-image.md](#item-1476f6) | minor update | 画像処理に関するドキュメントの更新 | modified | 43 | 11 | 54 | 
| [online-evaluation.md](#item-d9591b) | minor update | オンライン評価に関するドキュメントの更新 | modified | 3 | 3 | 6 | 
| [batch-run-data-selection.png](#item-10bd03) | minor update | 画像処理に関するバッチ実行データ選択の画像更新 | modified | 0 | 0 | 0 | 
| [chat-input-definition.png](#item-943c2b) | minor update | チャット入力定義に関する画像の更新 | modified | 0 | 0 | 0 | 
| [chat-output-definition.png](#item-a18f8c) | new feature | チャット出力定義に関する画像の追加 | added | 0 | 0 | 0 | 
| [gpt-4v-tool-in-chatflow.png](#item-eac13e) | minor update | GPT-4Vツールに関する画像の更新 | modified | 0 | 0 | 0 | 
| [gpt-4v-tool.png](#item-ff092c) | minor update | GPT-4Vツールに関する画像の更新 | modified | 0 | 0 | 0 | 
| [toc.yml](#item-2745cd) | minor update | AIスタジオの目次に関する更新 | modified | 3 | 1 | 4 | 


# Modified Contents
## articles/ai-studio/.openpublishing.redirection.ai-studio.json{#item-c75c21}

<details>
<summary>Diff</summary>
````diff
@@ -289,6 +289,16 @@
             "source_path_from_root": "/articles/ai-studio/concepts/related-content.md",
             "redirect_url": "/azure/ai-studio/concepts/what-are-ai-services",
             "redirect_document_id": false
+          },
+          {
+            "source_path_from_root": "/articles/ai-studio/how-to/develop/evaluate-sdk.md#cloud-evaluation-preview-on-test-datasets",
+            "redirect_url": "/azure/ai-studio/how-to/develop/cloud-evaluation",
+            "redirect_document_id": false
+          },
+          {
+            "source_path_from_root": "/articles/ai-studio/how-to/develop/evaluate-sdk.md#cloud-evaluation-on-test-datasets",
+            "redirect_url": "/azure/ai-studio/how-to/develop/cloud-evaluation",
+            "redirect_document_id": false
           }
     ]
 }
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リダイレクト設定の追加"
}
```

### Explanation
このコードの変更では、AIスタジオに関連するリダイレクト設定が追加されました。具体的には、記事「evaluate-sdk.md」から新たに2つのリダイレクト項目が追加され、これにより、特定のセクションからの遷移がスムーズになります。この更新によって、ユーザーはより関連性の高いコンテンツに直接アクセスできるようになります。リダイレクト先のURLも指定されており、これにより情報のナビゲーションが向上しています。全体として、10行の変更が行われ、ファイルの内容が改善されています。

## articles/ai-studio/how-to/develop/cloud-evaluation.md{#item-07f28c}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,284 @@
+---
+title: Cloud evaluation with Azure AI Projects SDK
+titleSuffix: Azure AI Foundry
+description: This article provides instructions on how to evaluate a Generative AI application on the cloud.
+manager: scottpolly
+ms.service: azure-ai-foundry
+ms.custom:
+  - references_regions
+  - ignite-2024
+ms.topic: how-to
+ms.date: 02/21/2025
+ms.reviewer: changliu2
+ms.author: lagayhar
+author: lgayhardt
+---
+# Evaluate your Generative AI application on the cloud with Azure AI Projects SDK (preview)
+
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
+
+While Azure AI Evaluation SDK client supports running evaluations locally on your own machine, you might want to delegate the job remotely to the cloud. For example, after you ran local evaluations on small test data to help assess your generative AI application prototypes, now you move into pre-deployment testing and need run evaluations on a large dataset. Cloud evaluation frees you from managing your local compute infrastructure, and enables you to integrate evaluations as tests into your CI/CD pipelines. After deployment, you might want to [continuously evaluate](../online-evaluation.md) your applications for post-deployment monitoring.
+
+In this article, you learn how to run cloud evaluation (preview) in pre-deployment testing on a test dataset. Using the Azure AI Projects SDK, you'll have evaluation results automatically logged into your Azure AI project for better observability. This feature supports all Microsoft curated [built-in evaluators](./evaluate-sdk.md#built-in-evaluators) and your own [custom evaluators](./evaluate-sdk.md#custom-evaluators) which can be located in the [Evaluator library](../evaluate-generative-ai-app.md#view-and-manage-the-evaluators-in-the-evaluator-library) and have the same project-scope RBAC.
+
+## Prerequisites
+
+- Azure AI project in the same [regions](./evaluate-sdk.md#region-support) as risk and safety evaluators (preview). If you don't have an existing project, follow the guide [How to create Azure AI project](../create-projects.md?tabs=ai-studio) to create one.
+
+- Azure OpenAI Deployment with GPT model supporting `chat completion`, for example `gpt-4`.
+- `Connection String` for Azure AI project to easily create `AIProjectClient` object. You can get the **Project connection string** under **Project details** from the project's **Overview** page.
+- Make sure you're first logged into your Azure subscription by running `az login`.
+
+### Installation Instructions
+
+1. Create a **virtual Python environment of you choice**. To create one using conda, run the following command:
+
+    ```bash
+    conda create -n cloud-evaluation
+    conda activate cloud-evaluation
+    ```
+
+2. Install the required packages by running the following command:
+
+    ```bash
+   pip install azure-identity azure-ai-projects azure-ai-ml
+    ```
+
+    Optionally you can use `pip install azure-ai-evaluation` if you want a code-first experience to fetch evaluator ID for built-in evaluators in code.
+
+Now you can define a client and a deployment which will be used to run your evaluations in the cloud:
+
+```python
+
+import os, time
+from azure.ai.projects import AIProjectClient
+from azure.identity import DefaultAzureCredential
+from azure.ai.projects.models import Evaluation, Dataset, EvaluatorConfiguration, ConnectionType
+from azure.ai.evaluation import F1ScoreEvaluator, RelevanceEvaluator, ViolenceEvaluator
+
+# Load your Azure OpenAI config
+deployment_name = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
+api_version = os.environ.get("AZURE_OPENAI_API_VERSION")
+
+# Create an Azure AI Client from a connection string. Available on Azure AI project Overview page.
+project_client = AIProjectClient.from_connection_string(
+    credential=DefaultAzureCredential(),
+    conn_str="<connection_string>"
+)
+```
+
+## Uploading evaluation data
+
+We provide two ways to register your data in Azure AI project required for evaluations in the cloud:
+
+1. **From SDK**: Upload new data from your local directory to your Azure AI project in the SDK, and fetch the dataset ID as a result:
+
+```python
+data_id, _ = project_client.upload_file("./evaluate_test_data.jsonl")
+```
+
+**From UI**: Alternatively, you can upload new data or update existing data versions by following the UI walkthrough under the **Data** tab of your Azure AI project.
+
+2. Given existing datasets uploaded to your Project:
+
+- **From SDK**: if you already know the dataset name you created, construct the dataset ID in this format: `/subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.MachineLearningServices/workspaces/<project-name>/data/<dataset-name>/versions/<version-number>`
+
+- **From UI**: If you don't know the dataset name, locate it under the **Data** tab of your Azure AI project and construct the dataset ID as in the format previously.
+
+## Specifying evaluators from Evaluator library
+
+We provide a list of built-in evaluators registered in the [Evaluator library](../evaluate-generative-ai-app.md#view-and-manage-the-evaluators-in-the-evaluator-library) under **Evaluation** tab of your Azure AI project. You can also register custom evaluators and use them for Cloud evaluation. We provide two ways to specify registered evaluators:
+
+### Specifying built-in evaluators
+
+- **From SDK**: Use built-in evaluator `id` property supported by `azure-ai-evaluation` SDK:
+
+```python
+from azure.ai.evaluation import F1ScoreEvaluator, RelevanceEvaluator, ViolenceEvaluator
+print("F1 Score evaluator id:", F1ScoreEvaluator.id)
+```
+
+- **From UI**: Follows these steps to fetch evaluator IDs after they're registered to your project:
+  - Select **Evaluation** tab in your Azure AI project;
+  - Select Evaluator library;
+  - Select your evaluators of choice by comparing the descriptions;
+  - Copy its "Asset ID" which will be your evaluator ID, for example, `azureml://registries/azureml/models/Groundedness-Evaluator/versions/1`.
+
+### Specifying custom evaluators
+
+- For code-based custom evaluators, register them to your Azure AI project and fetch the evaluator IDs as in this example:
+
+```python
+from azure.ai.ml import MLClient
+from azure.ai.ml.entities import Model
+from promptflow.client import PFClient
+
+
+# Define ml_client to register custom evaluator
+ml_client = MLClient(
+       subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"],
+       resource_group_name=os.environ["AZURE_RESOURCE_GROUP"],
+       workspace_name=os.environ["AZURE_PROJECT_NAME"],
+       credential=DefaultAzureCredential()
+)
+
+
+# Load evaluator from module
+from answer_len.answer_length import AnswerLengthEvaluator
+
+# Then we convert it to evaluation flow and save it locally
+pf_client = PFClient()
+local_path = "answer_len_local"
+pf_client.flows.save(entry=AnswerLengthEvaluator, path=local_path)
+
+# Specify evaluator name to appear in the Evaluator library
+evaluator_name = "AnswerLenEvaluator"
+
+# Finally register the evaluator to the Evaluator library
+custom_evaluator = Model(
+    path=local_path,
+    name=evaluator_name,
+    description="Evaluator calculating answer length.",
+)
+registered_evaluator = ml_client.evaluators.create_or_update(custom_evaluator)
+print("Registered evaluator id:", registered_evaluator.id)
+# Registered evaluators have versioning. You can always reference any version available.
+versioned_evaluator = ml_client.evaluators.get(evaluator_name, version=1)
+print("Versioned evaluator id:", registered_evaluator.id)
+```
+
+After registering your custom evaluator to your Azure AI project, you can view it in your [Evaluator library](../evaluate-generative-ai-app.md#view-and-manage-the-evaluators-in-the-evaluator-library) under **Evaluation** tab in your Azure AI project.
+
+- For prompt-based custom evaluators, use this snippet to register them. For example, let's register our `FriendlinessEvaluator` built as described in [Prompt-based evaluators](./evaluate-sdk.md#prompt-based-evaluators):
+
+```python
+# Import your prompt-based custom evaluator
+from friendliness.friend import FriendlinessEvaluator
+
+# Define your deployment 
+model_config = dict(
+    azure_endpoint=os.environ.get("AZURE_ENDPOINT"),
+    azure_deployment=os.environ.get("AZURE_DEPLOYMENT_NAME"),
+    api_version=os.environ.get("AZURE_API_VERSION"),
+    api_key=os.environ.get("AZURE_API_KEY"), 
+    type="azure_openai"
+)
+
+# Define ml_client to register custom evaluator
+ml_client = MLClient(
+       subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"],
+       resource_group_name=os.environ["AZURE_RESOURCE_GROUP"],
+       workspace_name=os.environ["AZURE_PROJECT_NAME"],
+       credential=DefaultAzureCredential()
+)
+
+# # Convert evaluator to evaluation flow and save it locally
+local_path = "friendliness_local"
+pf_client = PFClient()
+pf_client.flows.save(entry=FriendlinessEvaluator, path=local_path) 
+
+# Specify evaluator name to appear in the Evaluator library
+evaluator_name = "FriendlinessEvaluator"
+
+# Register the evaluator to the Evaluator library
+custom_evaluator = Model(
+    path=local_path,
+    name=evaluator_name,
+    description="prompt-based evaluator measuring response friendliness.",
+)
+registered_evaluator = ml_client.evaluators.create_or_update(custom_evaluator)
+print("Registered evaluator id:", registered_evaluator.id)
+# Registered evaluators have versioning. You can always reference any version available.
+versioned_evaluator = ml_client.evaluators.get(evaluator_name, version=1)
+print("Versioned evaluator id:", registered_evaluator.id)
+```
+
+After logging your custom evaluator to your Azure AI project, you can view it in your [Evaluator library](../evaluate-generative-ai-app.md#view-and-manage-the-evaluators-in-the-evaluator-library) under **Evaluation** tab of your Azure AI project.
+
+## Cloud evaluation (preview) with Azure AI Projects SDK
+
+You can now submit a cloud evaluation with Azure AI Projects SDK via a Python API. See the following example specifying an NLP evaluator (F1 score), AI-assisted quality and safety evaluator (Relevance and Violence), and a custom evaluator (Friendliness) with their [evaluator IDs](#specifying-evaluators-from-evaluator-library):
+
+```python
+import os, time
+from azure.ai.projects import AIProjectClient
+from azure.identity import DefaultAzureCredential
+from azure.ai.projects.models import Evaluation, Dataset, EvaluatorConfiguration, ConnectionType
+from azure.ai.evaluation import F1ScoreEvaluator, RelevanceEvaluator, ViolenceEvaluator
+
+# Load your Azure OpenAI config
+deployment_name = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
+api_version = os.environ.get("AZURE_OPENAI_API_VERSION")
+
+# Create an Azure AI Client from a connection string. Avaiable on project overview page on Azure AI project UI.
+project_client = AIProjectClient.from_connection_string(
+    credential=DefaultAzureCredential(),
+    conn_str="<connection_string>"
+)
+
+# Construct dataset ID per the instruction
+data_id = "<dataset-id>"
+
+default_connection = project_client.connections.get_default(connection_type=ConnectionType.AZURE_OPEN_AI)
+
+# Use the same model_config for your evaluator (or use different ones if needed)
+model_config = default_connection.to_evaluator_model_config(deployment_name=deployment_name, api_version=api_version)
+
+# Create an evaluation
+evaluation = Evaluation(
+    display_name="Cloud evaluation",
+    description="Evaluation of dataset",
+    data=Dataset(id=data_id),
+    evaluators={
+        # Note the evaluator configuration key must follow a naming convention
+        # the string must start with a letter with only alphanumeric characters 
+        # and underscores. Take "f1_score" as example: "f1score" or "f1_evaluator" 
+        # will also be acceptable, but "f1-score-eval" or "1score" will result in errors.
+        "f1_score": EvaluatorConfiguration(
+            id=F1ScoreEvaluator.id,
+        ),
+        "relevance": EvaluatorConfiguration(
+            id=RelevanceEvaluator.id,
+            init_params={
+                "model_config": model_config
+            },
+        ),
+        "violence": EvaluatorConfiguration(
+            id=ViolenceEvaluator.id,
+            init_params={
+                "azure_ai_project": project_client.scope
+            },
+        ),
+        "friendliness": EvaluatorConfiguration(
+            id="<custom_evaluator_id>",
+            init_params={
+                "model_config": model_config
+            }
+        )
+    },
+)
+
+# Create evaluation
+evaluation_response = project_client.evaluations.create(
+    evaluation=evaluation,
+)
+
+# Get evaluation
+get_evaluation_response = project_client.evaluations.get(evaluation_response.id)
+
+print("----------------------------------------------------------------")
+print("Created evaluation, evaluation ID: ", get_evaluation_response.id)
+print("Evaluation status: ", get_evaluation_response.status)
+print("AI project URI: ", get_evaluation_response.properties["AiStudioEvaluationUri"])
+print("----------------------------------------------------------------")
+```
+Now you can use the URI to view your evaluation results in your Azure AI project, in order to better assess the quality and safety performance of your applications.
+
+## Related content
+
+- [Evaluate your Generative AI applications locally](./evaluate-sdk.md)
+- [Evaluate your Generative AI applications online](https://aka.ms/GenAIMonitoringDoc)
+- [Learn more about simulating test datasets for evaluation](./simulator-interaction-data.md)
+- [View your evaluation results in Azure AI project](../../how-to/evaluate-results.md)
+- [Get started building a chat app using the Azure AI Foundry SDK](../../quickstarts/get-started-code.md)
+- [Get started with evaluation samples](https://aka.ms/aistudio/eval-samples)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "クラウド評価に関する新しい記事の追加"
}
```

### Explanation
このコードの変更では、Azure AIプロジェクトSDKを使用したクラウド評価に関する新しい記事が追加されました。この新しいコンテンツには、生成AIアプリケーションを評価するための手順やベストプラクティスが詳しく説明されています。284行の情報が追加され、クラウドで評価を実行するための前提条件、インストール手順、評価データのアップロード方法、評価者の指定方法などが包括的に扱われています。

記事は主に、開発者がローカルのリソースを管理することなく、クラウドでの評価を利用するための手助けをすることを目的としています。利用者は、SDKを使った明確な手順を通じて、評価データセットのアップロードや評価者の選択を行い、結果をAzureのプロジェクトで確認することができます。この新機能により、AIスタジオのユーザーは、プロトタイプの評価から本番前のテストまで、すべてを弾力的に処理できるようになります。

## articles/ai-studio/how-to/develop/evaluate-sdk.md{#item-9d5197}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
-title: Evaluate your Generative AI application with the Azure AI Evaluation SDK
-titleSuffix: Azure AI project
+title: Local Evaluation with Azure AI Evaluation SDK
+titleSuffix: Azure AI Foundry
 description: This article provides instructions on how to evaluate a Generative AI application with the Azure AI Evaluation SDK.
 manager: scottpolly
 ms.service: azure-ai-foundry
@@ -9,17 +9,17 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: how-to
-ms.date: 12/18/2024
+ms.date: 02/21/2025
 ms.reviewer: minthigpen
 ms.author: lagayhar
 author: lgayhardt
 ---
-# Evaluate your Generative AI application with the Azure AI Evaluation SDK
+# Evaluate your Generative AI application locally with the Azure AI Evaluation SDK
 
 [!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 > [!NOTE]
-> Evaluation with the prompt flow SDK has been retired and replaced with Azure AI Evaluation SDK.
+> Evaluation with the prompt flow SDK has been retired and replaced with Azure AI Evaluation SDK client library for Python. For more information about input data requirements, see the [API Reference Documentation](https://aka.ms/azureaieval-python-ref).
 
 To thoroughly assess the performance of your generative AI application when applied to a substantial dataset, you can evaluate a Generative AI application in your development environment with the Azure AI evaluation SDK. Given either a test dataset or a target, your generative AI application generations are quantitatively measured with both mathematical based metrics and AI-assisted quality and safety evaluators. Built-in or custom evaluators can provide you with comprehensive insights into the application's capabilities and limitations.
 
@@ -51,9 +51,6 @@ For more in-depth information on each evaluator definition and how it's calculat
 
 Built-in quality and safety metrics take in query and response pairs, along with additional information for specific evaluators.
 
-> [!TIP]
-> For more information about inputs and outputs, see the [Azure Python reference documentation](https://aka.ms/azureaieval-python-ref).
-
 ### Data requirements for built-in evaluators
 
 Built-in evaluators can accept *either* query and response pairs or a list of conversations:
@@ -64,7 +61,7 @@ Built-in evaluators can accept *either* query and response pairs or a list of co
 | Evaluator       | `query`      | `response`      | `context`       | `ground_truth`  | `conversation` |
 |----------------|---------------|---------------|---------------|---------------|-----------|
 |`GroundednessEvaluator`   | Optional: String | Required: String | Required: String | N/A  | Supported for text |
-| `GroundednessProEvaluator`   | Required: String | Required: String | Required: String | N/A  | Supported for text |
+| `GroundednessProEvaluator`  | Required: String | Required: String | Required: String | N/A  | Supported for text |
 | `RetrievalEvaluator`        | Required: String | N/A | Required: String         | N/A           | Supported for text |
 | `RelevanceEvaluator`      | Required: String | Required: String | N/A | N/A           | Supported for text |
 | `CoherenceEvaluator`      | Required: String | Required: String | N/A           | N/A           |Supported for text |
@@ -82,7 +79,7 @@ Built-in evaluators can accept *either* query and response pairs or a list of co
 | `IndirectAttackEvaluator`      | Required: String | Required: String | Required: String | N/A           |Supported for text |
 | `ProtectedMaterialEvaluator`  | Required: String | Required: String | N/A           | N/A           |Supported for text and image |
 | `QAEvaluator`      | Required: String | Required: String | Required: String | Required: String           | Not supported |
-| `ContentSafetyEvaluator`      | Required: String | Required: String |  N/A  | N/A           | Supported for text and image |
+| `ContentSafetyEvaluator`     | Required: String | Required: String |  N/A  | N/A           | Supported for text and image |
 
 - Query: the query sent in to the generative AI application
 - Response: the response to the query generated by the generative AI application
@@ -91,7 +88,7 @@ Built-in evaluators can accept *either* query and response pairs or a list of co
 - Conversation: a list of messages of user and assistant turns. See more in the next section.
 
 > [!NOTE]
-> AI-assisted quality evaluators except for `SimilarityEvaluator` come with a reason field. They employ techniques including chain-of-thought reasoning to generate an explanation for the score. Therefore they will consume more token usage in generation as a result of improved evaluation quality. Specifically, `max_token` for evaluator generation has been set to 800 for all AI-assisted evaluators (and 1600 for `RetrievalEvaluator` to accommodate for longer inputs.)
+> AI-assisted quality evaluators except for `SimilarityEvaluator` come with a reason field. They employ techniques including chain-of-thought reasoning to generate an explanation for the score. Therefore they'll consume more token usage in generation as a result of improved evaluation quality. Specifically, `max_token` for evaluator generation has been set to 800 for all AI-assisted evaluators (and 1600 for `RetrievalEvaluator` to accommodate for longer inputs.)
 
 #### Conversation support for text
 
@@ -126,7 +123,7 @@ For evaluators that support conversations for text, you can provide `conversatio
 Our evaluators understand that the first turn of the conversation provides valid `query` from `user`, `context` from `assistant`,  and `response` from `assistant` in the query-response format. Conversations are then evaluated per turn and results are aggregated over all turns for a conversation score.
 
 > [!NOTE]
-> Note that in the second turn, even if `context` is `null` or a missing key, it will be interpreted as an empty string instead of erroring out, which might lead to misleading results. We strongly recommend that you validate your evaluation data to comply with the data requirements.
+> In the second turn, even if `context` is `null` or a missing key, it will be interpreted as an empty string instead of erroring out, which might lead to misleading results. We strongly recommend that you validate your evaluation data to comply with the data requirements.
 
 #### Conversation support for images and multi-modal text and image
 
@@ -201,9 +198,9 @@ safety_score = safety_evaluator(conversation=conversation_image_url)
 
 Currently the image and multi-modal evaluators support:
 
-- Single turn only (a conversation can have only 1 user message and 1 assistant message)
-- Conversation can have only 1 system message
-- Conversation payload should be less than 10MB size (including images)
+- Single turn only (a conversation can have only one user message and one assistant message)
+- Conversation can have only one system message
+- Conversation payload should be less than 10-MB size (including images)
 - Absolute URLs and Base64 encoded images
 - Multiple images in a single turn
 - JPG/JPEG, PNG, GIF file formats
@@ -214,12 +211,14 @@ You can use our built-in AI-assisted and NLP quality evaluators to assess the pe
 
 #### Set up
 
-1. For AI-assisted quality evaluators except for `GroundednessProEvaluator`, you must specify a GPT model to act as a judge to score the evaluation data. Choose a deployment with either GPT-3.5, GPT-4, GPT-4o or GPT-4-mini model for your calculations and set it as your `model_config`. We support both Azure OpenAI or OpenAI model configuration schema. We recommend using GPT models that don't have the `(preview)` suffix for the best performance and parseable responses with our evaluators.
+1. For AI-assisted quality evaluators except for `GroundednessProEvaluator` (preview), you must specify a GPT model (`gpt-35-turbo`, `gpt-4`, `gpt-4-turbo`, `gpt-4o`, or `gpt-4o-mini`) in your `model_config` to act as a judge to score the evaluation data. We support both Azure OpenAI or OpenAI model configuration schema. We recommend using GPT models that aren't in preview for the best performance and parseable responses with our evaluators.
 
 > [!NOTE]
-> Make sure the you have at least `Cognitive Services OpenAI User` role for the Azure OpenAI resource to make inference calls with API key. For more permissions, learn more about [permissioning for Azure OpenAI resource](../../../ai-services/openai/how-to/role-based-access-control.md#summary).  
+> It's strongly recommended that `gpt-3.5-turbo` should be replaced by `gpt-4o-mini` for your evaluator model, as the latter is cheaper, more capable, and just as fast according to [OpenAI](https://platform.openai.com/docs/models/gpt-4#gpt-3-5-turbo).
+>
+> Make sure the you have at least `Cognitive Services OpenAI User` role for the Azure OpenAI resource to make inference calls with API key. To learn more about permissions, see [permissions for Azure OpenAI resource](../../../ai-services/openai/how-to/role-based-access-control.md#summary).  
 
-2. For `GroundednessProEvaluator`, instead of a GPT deployment in `model_config`, you must provide your `azure_ai_project` information. This accesses the backend evaluation service of your Azure AI project.
+2. For `GroundednessProEvaluator` (preview), instead of a GPT deployment in `model_config`, you must provide your `azure_ai_project` information. This accesses the backend evaluation service of your Azure AI project.
 
 #### Performance and quality evaluator usage
 
@@ -253,7 +252,7 @@ groundedness_pro_eval = GroundednessProEvaluator(azure_ai_project=azure_ai_proje
 
 query_response = dict(
     query="Which tent is the most waterproof?",
-    context="The Alpine Explorer Tent is the most water-proof of all tents available.",
+    context="The Alpine Explorer Tent is the second most water-proof of all tents available.",
     response="The Alpine Explorer Tent is the most waterproof."
 )
 
@@ -296,13 +295,15 @@ The result of the AI-assisted quality evaluators for a query and response pair i
 - `{metric_name}_label` provides a binary label.
 - `{metric_name}_reason` explains why a certain score or label was given for each data point.
 
+#### Comparing quality and custom evaluators
+
 For NLP evaluators, only a score is given in the `{metric_name}` key.
 
-Like 6 other AI-assisted evaluators, `GroundednessEvaluator` is a prompt-based evaluator that outputs a score on a 5-point scale (the higher the score, the more grounded the result is). On the other hand, `GroundednessProEvaluator` invokes our backend evaluation service powered by Azure AI Content Safety and outputs `True` if all content is grounded, or `False` if any ungrounded content is detected.
+Like six other AI-assisted evaluators, `GroundednessEvaluator` is a prompt-based evaluator that outputs a score on a 5-point scale (the higher the score, the more grounded the result is). On the other hand, `GroundednessProEvaluator` (preview) invokes our backend evaluation service powered by Azure AI Content Safety and outputs `True` if all content is grounded, or `False` if any ungrounded content is detected.
 
-We open-source the prompts of our quality evaluators except for `GroundednessProEvaluator` (powered by Azure AI Content Safety) for transparency. These prompts serve as instructions for a language model to perform their evaluation task, which requires a human-friendly definition of the metric and its associated scoring rubrics (what the 5 levels of quality mean for the metric). We highly recommend that users customize the definitions and grading rubrics to their scenario specifics. See details in [Custom Evaluators](#custom-evaluators).
+We open-source the prompts of our quality evaluators except for `GroundednessProEvaluator` (powered by Azure AI Content Safety) for transparency. These prompts serve as instructions for a language model to perform their evaluation task, which requires a human-friendly definition of the metric and its associated scoring rubrics (what the five levels of quality mean for the metric). We highly recommend that users customize the definitions and grading rubrics to their scenario specifics. See details in [Custom Evaluators](#custom-evaluators).
 
-For conversation mode, here is an example for `GroundednessEvaluator`:
+For conversation mode, here's an example for `GroundednessEvaluator`:
 
 ```python
 # Conversation mode
@@ -391,7 +392,7 @@ print(violence_conv_score)
 
 The result of the content safety evaluators for a query and response pair is a dictionary containing:
 
-- `{metric_name}` provides a severity label for that content risk ranging from Very low, Low, Medium, and High. You can read more about the descriptions of each content risk and severity scale [here](../../concepts/evaluation-metrics-built-in.md).
+- `{metric_name}` provides a severity label for that content risk ranging from Very low, Low, Medium, and High. To learn more about the descriptions of each content risk and severity scale, see [Evaluation and monitoring metrics for generative AI](../../concepts/evaluation-metrics-built-in.md).
 - `{metric_name}_score` has a range between 0 and 7 severity level that maps to a severity label given in `{metric_name}`.
 - `{metric_name}_reason` explains why a certain severity score was given for each data point.
 
@@ -738,284 +739,12 @@ result = evaluate(
 
 ```
 
-## Cloud evaluation (preview) on test datasets
-
-After local evaluations of your generative AI applications, you might want to run evaluations in the cloud for pre-deployment testing, and [continuously evaluate](https://aka.ms/GenAIMonitoringDoc) your applications for post-deployment monitoring. Azure AI Projects SDK offers such capabilities via a Python API and supports almost all of the features available in local evaluations. Follow the steps below to submit your evaluation to the cloud on your data using built-in or custom evaluators.
-
-### Prerequisites
-
-- Azure AI project in the same [regions](#region-support) as risk and safety evaluators (preview). If you don't have an existing project, follow the guide [How to create Azure AI project](../create-projects.md?tabs=ai-studio) to create one.
-
-> [!NOTE]
-> Cloud evaluations do not support `ContentSafetyEvaluator`, and `QAEvaluator`.
-
-- Azure OpenAI Deployment with GPT model supporting `chat completion`, for example `gpt-4`.
-- `Connection String` for Azure AI project to easily create `AIProjectClient` object. You can get the **Project connection string** under **Project details** from the project's **Overview** page.
-- Make sure you're first logged into your Azure subscription by running `az login`.
-
-### Installation Instructions
-
-1. Create a **virtual Python environment of you choice**. To create one using conda, run the following command:
-
-    ```bash
-    conda create -n cloud-evaluation
-    conda activate cloud-evaluation
-    ```
-
-2. Install the required packages by running the following command:
-
-    ```bash
-   pip install azure-identity azure-ai-projects azure-ai-ml
-    ```
-
-    Optionally you can `pip install azure-ai-evaluation` if you want a code-first experience to fetch evaluator ID for built-in evaluators in code.
-
-Now you can define a client and a deployment which will be used to run your evaluations in the cloud:
-
-```python
-
-import os, time
-from azure.ai.projects import AIProjectClient
-from azure.identity import DefaultAzureCredential
-from azure.ai.projects.models import Evaluation, Dataset, EvaluatorConfiguration, ConnectionType
-from azure.ai.evaluation import F1ScoreEvaluator, RelevanceEvaluator, ViolenceEvaluator
-
-# Load your Azure OpenAI config
-deployment_name = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
-api_version = os.environ.get("AZURE_OPENAI_API_VERSION")
-
-# Create an Azure AI Client from a connection string. Avaiable on Azure AI project Overview page.
-project_client = AIProjectClient.from_connection_string(
-    credential=DefaultAzureCredential(),
-    conn_str="<connection_string>"
-)
-```
-
-### Uploading evaluation data
-
-We provide two ways to register your data in Azure AI project required for evaluations in the cloud:
-
-1. **From SDK**: Upload new data from your local directory to your Azure AI project in the SDK, and fetch the dataset ID as a result:
-
-```python
-data_id, _ = project_client.upload_file("./evaluate_test_data.jsonl")
-```
-
-**From UI**: Alternatively, you can upload new data or update existing data versions by following the UI walkthrough under the **Data** tab of your Azure AI project.
-
-2. Given existing datasets uploaded to your Project:
-
-- **From SDK**: if you already know the dataset name you created, construct the dataset ID in this format: `/subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.MachineLearningServices/workspaces/<project-name>/data/<dataset-name>/versions/<version-number>`
-
-- **From UI**: If you don't know the dataset name, locate it under the **Data** tab of your Azure AI project and construct the dataset ID as in the format above.
-
-### Specifying evaluators from Evaluator library
-
-We provide a list of built-in evaluators registered in the [Evaluator library](../evaluate-generative-ai-app.md#view-and-manage-the-evaluators-in-the-evaluator-library) under **Evaluation** tab of your Azure AI project. You can also register custom evaluators and use them for Cloud evaluation. We provide two ways to specify registered evaluators:
-
-#### Specifying built-in evaluators
-
-- **From SDK**: Use built-in evaluator `id` property supported by `azure-ai-evaluation` SDK:
-
-```python
-from azure.ai.evaluation import F1ScoreEvaluator, RelevanceEvaluator, ViolenceEvaluator
-print("F1 Score evaluator id:", F1ScoreEvaluator.id)
-```
-
-- **From UI**: Follows these steps to fetch evaluator ids after they're registered to your project:
-  - Select **Evaluation** tab in your Azure AI project;
-  - Select Evaluator library;
-  - Select your evaluators of choice by comparing the descriptions;
-  - Copy its "Asset ID" which will be your evaluator id, for example, `azureml://registries/azureml/models/Groundedness-Evaluator/versions/1`.
-
-#### Specifying custom evaluators
-
-- For code-based custom evaluators, register them to your Azure AI project and fetch the evaluator ids with the following:
-
-```python
-from azure.ai.ml import MLClient
-from azure.ai.ml.entities import Model
-from promptflow.client import PFClient
-
-
-# Define ml_client to register custom evaluator
-ml_client = MLClient(
-       subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"],
-       resource_group_name=os.environ["AZURE_RESOURCE_GROUP"],
-       workspace_name=os.environ["AZURE_PROJECT_NAME"],
-       credential=DefaultAzureCredential()
-)
-
-
-# Load evaluator from module
-from answer_len.answer_length import AnswerLengthEvaluator
-
-# Then we convert it to evaluation flow and save it locally
-pf_client = PFClient()
-local_path = "answer_len_local"
-pf_client.flows.save(entry=AnswerLengthEvaluator, path=local_path)
-
-# Specify evaluator name to appear in the Evaluator library
-evaluator_name = "AnswerLenEvaluator"
-
-# Finally register the evaluator to the Evaluator library
-custom_evaluator = Model(
-    path=local_path,
-    name=evaluator_name,
-    description="Evaluator calculating answer length.",
-)
-registered_evaluator = ml_client.evaluators.create_or_update(custom_evaluator)
-print("Registered evaluator id:", registered_evaluator.id)
-# Registered evaluators have versioning. You can always reference any version available.
-versioned_evaluator = ml_client.evaluators.get(evaluator_name, version=1)
-print("Versioned evaluator id:", registered_evaluator.id)
-```
-
-After registering your custom evaluator to your Azure AI project, you can view it in your [Evaluator library](../evaluate-generative-ai-app.md#view-and-manage-the-evaluators-in-the-evaluator-library) under **Evaluation** tab in your Azure AI project.
-
-- For prompt-based custom evaluators, use this snippet to register them. For example, let's register our `FriendlinessEvaluator` built as described in [Prompt-based evaluators](#prompt-based-evaluators):
-
-```python
-# Import your prompt-based custom evaluator
-from friendliness.friend import FriendlinessEvaluator
-
-# Define your deployment 
-model_config = dict(
-    azure_endpoint=os.environ.get("AZURE_ENDPOINT"),
-    azure_deployment=os.environ.get("AZURE_DEPLOYMENT_NAME"),
-    api_version=os.environ.get("AZURE_API_VERSION"),
-    api_key=os.environ.get("AZURE_API_KEY"), 
-    type="azure_openai"
-)
-
-# Define ml_client to register custom evaluator
-ml_client = MLClient(
-       subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"],
-       resource_group_name=os.environ["AZURE_RESOURCE_GROUP"],
-       workspace_name=os.environ["AZURE_PROJECT_NAME"],
-       credential=DefaultAzureCredential()
-)
-
-# # Convert evaluator to evaluation flow and save it locally
-local_path = "friendliness_local"
-pf_client = PFClient()
-pf_client.flows.save(entry=FriendlinessEvaluator, path=local_path) 
-
-# Specify evaluator name to appear in the Evaluator library
-evaluator_name = "FriendlinessEvaluator"
-
-# Register the evaluator to the Evaluator library
-custom_evaluator = Model(
-    path=local_path,
-    name=evaluator_name,
-    description="prompt-based evaluator measuring response friendliness.",
-)
-registered_evaluator = ml_client.evaluators.create_or_update(custom_evaluator)
-print("Registered evaluator id:", registered_evaluator.id)
-# Registered evaluators have versioning. You can always reference any version available.
-versioned_evaluator = ml_client.evaluators.get(evaluator_name, version=1)
-print("Versioned evaluator id:", registered_evaluator.id)
-```
-
-After logging your custom evaluator to your Azure AI project, you can view it in your [Evaluator library](../evaluate-generative-ai-app.md#view-and-manage-the-evaluators-in-the-evaluator-library) under **Evaluation** tab of your Azure AI project.
-
-### Cloud evaluation (preview) with Azure AI Projects SDK
-
-You can submit a cloud evaluation with Azure AI Projects SDK via a Python API. See the following example to submit a cloud evaluation of your dataset using an NLP evaluator (F1 score), an AI-assisted quality evaluator (Relevance), a safety evaluator (Violence) and a custom evaluator. Putting it altogether:
-
-```python
-import os, time
-from azure.ai.projects import AIProjectClient
-from azure.identity import DefaultAzureCredential
-from azure.ai.projects.models import Evaluation, Dataset, EvaluatorConfiguration, ConnectionType
-from azure.ai.evaluation import F1ScoreEvaluator, RelevanceEvaluator, ViolenceEvaluator
-
-# Load your Azure OpenAI config
-deployment_name = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
-api_version = os.environ.get("AZURE_OPENAI_API_VERSION")
-
-# Create an Azure AI Client from a connection string. Available on project overview page on Azure AI project UI.
-project_client = AIProjectClient.from_connection_string(
-    credential=DefaultAzureCredential(),
-    conn_str="<connection_string>"
-)
-
-# Construct dataset ID per the instruction
-data_id = "<dataset-id>"
-
-default_connection = project_client.connections.get_default(connection_type=ConnectionType.AZURE_OPEN_AI)
-
-# Use the same model_config for your evaluator (or use different ones if needed)
-model_config = default_connection.to_evaluator_model_config(deployment_name=deployment_name, api_version=api_version)
-
-# Create an evaluation
-evaluation = Evaluation(
-    display_name="Cloud evaluation",
-    description="Evaluation of dataset",
-    data=Dataset(id=data_id),
-    evaluators={
-        # Note the evaluator configuration key must follow a naming convention
-        # the string must start with a letter with only alphanumeric characters 
-        # and underscores. Take "f1_score" as example: "f1score" or "f1_evaluator" 
-        # will also be acceptable, but "f1-score-eval" or "1score" will result in errors.
-        "f1_score": EvaluatorConfiguration(
-            id=F1ScoreEvaluator.id,
-        ),
-        "relevance": EvaluatorConfiguration(
-            id=RelevanceEvaluator.id,
-            init_params={
-                "model_config": model_config
-            },
-        ),
-        "violence": EvaluatorConfiguration(
-            id=ViolenceEvaluator.id,
-            init_params={
-                "azure_ai_project": project_client.scope
-            },
-        ),
-        "friendliness": EvaluatorConfiguration(
-            id="<custom_evaluator_id>",
-            init_params={
-                "model_config": model_config
-            }
-        )
-    },
-)
-
-# Create evaluation
-evaluation_response = project_client.evaluations.create(
-    evaluation=evaluation,
-)
-
-# Get evaluation
-get_evaluation_response = project_client.evaluations.get(evaluation_response.id)
-
-print("----------------------------------------------------------------")
-print("Created evaluation, evaluation ID: ", get_evaluation_response.id)
-print("Evaluation status: ", get_evaluation_response.status)
-print("AI project URI: ", get_evaluation_response.properties["AiStudioEvaluationUri"])
-print("----------------------------------------------------------------")
-```
-
-Now we can run the cloud evaluation we just instantiated above.
-
-```python
-evaluation = client.evaluations.create(
-    evaluation=evaluation,
-    subscription_id=subscription_id,
-    resource_group_name=resource_group_name,
-    workspace_name=workspace_name,
-    headers={
-        "x-azureml-token": DefaultAzureCredential().get_token("https://ml.azure.com/.default").token,
-    }
-)
-```
-
 ## Related content
 
-- [Azure Python reference documentation](https://aka.ms/azureaieval-python-ref)
-- [Azure AI Evaluation SDK Troubleshooting guide](https://aka.ms/azureaieval-tsg)
+- [Azure AI Evaluation Python SDK client reference documentation](https://aka.ms/azureaieval-python-ref)
+- [Azure AI Evaluation SDK client Troubleshooting guide](https://aka.ms/azureaieval-tsg)
 - [Learn more about the evaluation metrics](../../concepts/evaluation-metrics-built-in.md)
+- [Evaluate your Generative AI applications remotely on the cloud](./cloud-evaluation.md)
 - [Learn more about simulating test datasets for evaluation](./simulator-interaction-data.md)
 - [View your evaluation results in Azure AI project](../../how-to/evaluate-results.md)
 - [Get started building a chat app using the Azure AI Foundry SDK](../../quickstarts/get-started-code.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Evaluate SDKの大幅な改訂"
}
```

### Explanation
このコードの変更は、Azure AI Evaluation SDKに関連するドキュメントの大幅な改訂を示しています。変更内容には、記事のタイトルやサブタイトルの修正、日付の更新、内容の構造変更が含まれています。特に、298行の削除と27行の追加が行われており、全体として325行が変更されました。

主な変更点として、ドキュメントの焦点が「ローカル評価」にシフトし、リダイレクトされた内容や不必要な情報が削除されました。また、プロンプトフローSDKからの移行に関する詳細説明が更新され、Azure AI Evaluation SDKのクライアントライブラリに関する情報が強調されています。

この改訂により、ユーザーは生成AIアプリケーションの評価を行う手順や、そのための必要なデータ要件をより明確に理解できるようになっています。特に、評価者やメトリクスの詳細、データ要件に関する情報が整理され、実際の評価の実施に直結する内容が中心になっています。全体として、ドキュメントは効率的でわかりやすくなり、ユーザーのニーズに応えた内容の更新が行われています。

## articles/ai-studio/how-to/develop/trace-production-sdk.md{#item-8d5b4c}

<details>
<summary>Diff</summary>
````diff
@@ -7,8 +7,8 @@ ms.service: azure-ai-foundry
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 5/21/2024
-ms.reviewer: keli19
+ms.date: 02/14/2025
+ms.reviewer: none
 ms.author: lagayhar
 author: lgayhardt
 ---
@@ -38,13 +38,13 @@ After you test your flow properly, either a flex flow or a DAG flow, you can dep
 You can also [deploy to other platforms, such as Docker container, Kubernetes cluster, and more](https://microsoft.github.io/promptflow/how-to-guides/deploy-a-flow/index.html).
 
 > [!NOTE]
-> You need to use the latest prompt flow base image to deploy the flow, so that it support the tracing and feedback collection API.
+> You need to use the latest prompt flow base image to deploy the flow, so that it supports the tracing and feedback collection API.
 
 ## Enable trace and collect system metrics for your deployment
 
-If you're using Azure AI Foundry portal to deploy, then you can turn-on **Application Insights diagnostics** in **Advanced settings** > **Deployment** step in the deployment wizard, in which way the tracing data and system metrics are collected to the project linked to Application Insights.
+If you're using Azure AI Foundry portal to deploy, you can turn on **Application Insights diagnostics** in the **Advanced settings** > **Deployment** step in the deployment wizard, in which way the tracing data and system metrics are collected to the project linked to Application Insights.
 
-If you're using SDK or CLI, you can by adding a property `app_insights_enabled: true` in the deployment yaml file that collects data to the project linked to application insights. 
+If you're using the SDK or CLI, you can add a property `app_insights_enabled: true` in the deployment yaml file that collects data to the project linked to application insights.
 
 ```yaml
 app_insights_enabled: true
@@ -58,30 +58,31 @@ environment_variables:
 ```
 
 > [!NOTE]
-> If you only set `app_insights_enabled: true` but your project doesn't have a linked Application Insights resource, your deployment will not fail but there will be no data collected.
+> If you only set `app_insights_enabled: true` but your project doesn't have a linked Application Insights resource, your deployment won't fail but there will be no data collected.
 >
-> If you specify both `app_insights_enabled: true` and the above environment variable at the same time, the tracing data and metrics will be sent to the project linked to application insights. Hence, if you want to specify a different Application Insights, you only need to keep the environment variable.
+> If you specify both `app_insights_enabled: true` and the previous environment variable at the same time, the tracing data and metrics will be sent to the project linked to application insights. Hence, if you want to specify a different Application Insights, you only need to keep the environment variable.
 > 
-> If you deploy to other platforms, you can also use the environment variable `APPLICATIONINSIGHTS_CONNECTION_STRING: <connection_string>` to collect trace data and metrics to speicifed Application Insights.
+> If you deploy to other platforms, you can also use the environment variable `APPLICATIONINSIGHTS_CONNECTION_STRING: <connection_string>` to collect trace data and metrics to specified Application Insights.
+
 ## View tracing data in Application Insights
 
 Traces record specific events or the state of an application during execution. It can include data about function calls, variable values, system events and more. Traces help breakdown an application's components into discrete inputs and outputs, which is crucial for debugging and understanding an application. You can learn more from [here](https://opentelemetry.io/docs/concepts/signals/traces/) on traces. The trace data follows [OpenTelemetry specification](https://opentelemetry.io/docs/specs/otel/).
 
 You can view the detailed trace in the specified Application Insights. The following screenshot shows an example of an event of a deployed flow containing multiple nodes. In Application Insights -> Investigate -> Transaction search, and you can select each node to view its detailed trace. 
 
-The **Dependency** type events record calls from your deployments. The name of that event is the name of flow folder. Learn more about [Transaction search and diagnostics in Application Insights](/azure/azure-monitor/app/transaction-search-and-diagnostics).
+The **Dependency** type events record calls from your deployments. The name of that event is the name of the flow folder. Learn more about [Transaction search and diagnostics in Application Insights](/azure/azure-monitor/app/transaction-search-and-diagnostics).
 
 ## View system metrics in Application Insights
 
 | Metrics Name                         | Type      | Dimensions                                | Description                                                                     |
 |--------------------------------------|-----------|-------------------------------------------|---------------------------------------------------------------------------------|
-| token_consumption                    | counter   | - flow <br> - node<br> - llm_engine<br> - token_type:  `prompt_tokens`: LLM API input tokens;  `completion_tokens`: LLM API response tokens ; `total_tokens` = `prompt_tokens + completion tokens`          | OpenAI token consumption metrics                                                |
-| flow_latency                         | histogram | flow,response_code,streaming,response_type| request execution cost, response_type means whether it's full/firstbyte/lastbyte|
-| flow_request                         | counter   | flow,response_code,exception,streaming    | flow request count                                                              |
-| node_latency                         | histogram | flow,node,run_status                      | node execution cost                                                             |
-| node_request                         | counter   | flow,node,exception,run_status            | node execution count                                                    |
-| rpc_latency                          | histogram | flow,node,api_call                        | rpc cost                                                                        |
-| rpc_request                          | counter   | flow,node,api_call,exception              | rpc count                                                                       |
+| token_consumption                    | counter   | - flow <br> - node<br> - llm_engine<br> - token_type:  `prompt_tokens`: LLM API input tokens;  `completion_tokens`: LLM API response tokens; `total_tokens` = `prompt_tokens + completion tokens`          | OpenAI token consumption metrics                                                |
+| flow_latency                         | histogram | flow, response_code, streaming, response_type | request execution cost, response_type means whether it's full/firstbyte/lastbyte|
+| flow_request                         | counter   | flow, response_code, exception, streaming    | flow request count                                                              |
+| node_latency                         | histogram | flow, node, run_status                      | node execution cost                                                             |
+| node_request                         | counter   | flow, node, exception, run_status            | node execution count                                                    |
+| rpc_latency                          | histogram | flow, node, api_call                        | rpc cost                                                                        |
+| rpc_request                          | counter   | flow, node, api_call, exception              | rpc count                                                                       |
 | flow_streaming_response_duration     | histogram | flow                                      | streaming response sending cost, from sending first byte to sending last byte   |
 
 You can find the workspace default Application Insights in your workspace overview page in Azure portal.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トレースおよびメトリクス収集に関するドキュメントの改善"
}
```

### Explanation
このコードの変更は、Azure AI Studioに関するトレースおよびメトリクス収集のドキュメントのマイナーな更新を示しています。17行が追加され、16行が削除され、全体として33行が変更されました。この修正には、日付の更新、レビュー担当の明記の削除、表現の改善が含まれています。

主な変更点として、アプリケーションインサイトを使用してデプロイする際の設定方法や注意点が明確化されました。例えば、アプリケーションインサイトの診断を有効にする手順がわかりやすくまとめられています。また、トレースデータの収集に関する注意事項や環境変数の設定についても情報が更新され、ユーザーにとっての利便性が向上しました。

さらに、トレースデータとシステムメトリクスの表示方法についての説明が追加され、アプリケーションインサイトでのデータの確認方法が具体的に示されています。全体として、ドキュメントはより親しみやすく、利用者がトレース機能やメトリクスを利用する際の参考になる内容に改善されています。

## articles/ai-studio/how-to/flow-process-image.md{#item-1476f6}

<details>
<summary>Diff</summary>
````diff
@@ -7,8 +7,8 @@ ms.service: azure-ai-foundry
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 5/21/2024
-ms.reviewer: jinzhong
+ms.date: 02/14/2025
+ms.reviewer: none
 ms.author: lagayhar
 author: lgayhardt
 ---
@@ -39,14 +39,44 @@ To use image data in prompt flow authoring page:
    :::image type="content" source="../media/prompt-flow/how-to-process-image/flow-input-image-preview.png" alt-text="Screenshot of flow authoring page showing image preview flow input." lightbox = "../media/prompt-flow/how-to-process-image/flow-input-image-preview.png":::
 3. You might want to preprocess the image using the [Python tool](./prompt-flow-tools/python-tool.md) before feeding it to the LLM. For example, you can resize or crop the image to a smaller size.
    :::image type="content" source="../media/prompt-flow/how-to-process-image/process-image-using-python.png" alt-text="Screenshot of using python tool to do image preprocessing." lightbox = "../media/prompt-flow/how-to-process-image/process-image-using-python.png":::
+
+    ```python
+    from promptflow import tool
+    from promptflow.contracts.multimedia import Image as PFImage 
+    from PIL import Image as Image 
+    import io
+    
+    @tool
+    def process_image(input_image: PFImage) -> PFImage:
+        # convert the input image data to a BytesIO object
+        data_byteIO = io.BytesIO(input_image)
+    
+        # Open the image data as a PIL Image object
+        image = Image.open(data_byteIO)
+    
+        # crop image
+        cropped_image = image.crop((100, 100, 900, 900))
+    
+        # Convert the cropped image back to BytesIO
+        byte_arr = io.BytesIO()
+        cropped_image.save(byte_arr, format = 'JPEG')
+    
+        # Create a new prompt flow Image object with the cropped image data
+        # This image is now ready to be returned
+        cropped_PF_image = PFImage(byte_arr.getvalue(), mime_type = "image/jpeg")
+    
+        return cropped_PF_image
+       ```
+    
     > [!IMPORTANT]
     > To process images using a Python function, you need to use the `Image` class that you import from the `promptflow.contracts.multimedia` package. The `Image` class is used to represent an `Image` type within prompt flow. It is designed to work with image data in byte format, which is convenient when you need to handle or manipulate the image data directly.
     >
     > To return the processed image data, you need to use the `Image` class to wrap the image data. Create an `Image` object by providing the image data in bytes and the [MIME type](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types) `mime_type`. The MIME type lets the system understand the format of the image data, or it can be `*` for unknown type.
 
 4. Run the Python node and check the output. In this example, the Python function returns the processed Image object. Select the image output to preview the image.
    :::image type="content" source="../media/prompt-flow/how-to-process-image/python-node-image-output.png" alt-text="Screenshot of Python node's image output." lightbox = "../media/prompt-flow/how-to-process-image/python-node-image-output.png"::: 
-If the Image object from Python node is set as the flow output, you can preview the image in the flow output page as well.
+
+    If the Image object from Python node is set as the flow output, you can preview the image in the flow output page as well.
 
 ## Use GPT-4V tool
 
@@ -56,32 +86,34 @@ Add the [Azure OpenAI GPT-4 Turbo with Vision tool](./prompt-flow-tools/azure-op
 
 :::image type="content" source="../media/prompt-flow/how-to-process-image/gpt-4v-tool.png" alt-text="Screenshot of GPT-4V tool." lightbox = "../media/prompt-flow/how-to-process-image/gpt-4v-tool.png":::
 
-The Jinja template for composing prompts in the GPT-4V tool follows a similar structure to the chat API in the LLM tool. To represent an image input within your prompt, you can use the syntax `![image]({{INPUT NAME}})`. Image input can be passed in the `user`, `system` and `assistant` messages.
+The Jinja template for composing prompts in the GPT-4V tool follows a similar structure to the chat API in the LLM tool. To represent an image input within your prompt, you can use the syntax `![image]({{INPUT NAME}})`. Image input can be passed in the `user`, `system`, and `assistant` messages.
 
 Once you've composed the prompt, select the **Validate and parse input** button to parse the input placeholders. The image input represented by `![image]({{INPUT NAME}})` will be parsed as image type with the input name as INPUT NAME.
 
 You can assign a value to the image input through the following ways:
 
 - Reference from the flow input of Image type.
 - Reference from other node's output of Image type.
-- Upload, drag, or paste an image, or specify an image URL or the relative image path.
+- Upload, drag, paste an image, or specify an image URL or the relative image path.
 
 ## Build a chatbot to process images
 
 In this section, you learn how to build a chatbot that can process image and text inputs.
 
-Assume you want to build a chatbot that can answer any questions about the image and text together. You can achieve this by following the steps below:
+Assume you want to build a chatbot that can answer any questions about the image and text together. You can achieve this by following the steps in this section.
 
 1. Create a **chat flow**.
-1. Add a **chat input**, select the data type as **"list"**. In the chat box, user can input a mixed sequence of texts and images, and prompt flow service will transform that into a list.
+1. In *Inputs*, select the data type as **"list"**. In the chat box, user can input a mixed sequence of texts and images, and prompt flow service will transform that into a list.
    :::image type="content" source="../media/prompt-flow/how-to-process-image/chat-input-definition.png" alt-text="Screenshot of chat input type configuration." lightbox = "../media/prompt-flow/how-to-process-image/chat-input-definition.png":::  
-1. Add **GPT-4V** tool to the flow.
+1. Add **GPT-4V** tool to the flow. You can copy the prompt from the default LLM tool chat and paste it into the GPT 4V tool. Then you delete the default LLM tool chat from the flow.
     :::image type="content" source="../media/prompt-flow/how-to-process-image/gpt-4v-tool-in-chatflow.png" alt-text=" Screenshot of GPT-4V tool in chat flow." lightbox = "../media/prompt-flow/how-to-process-image/gpt-4v-tool-in-chatflow.png":::  
 
     In this example, `{{question}}` refers to the chat input, which is a list of texts and images.
+1. In *Outputs*, change the value of "answer" to the name of your vision tool's output, for example, `${gpt_vision.output}`.
+    :::image type="content" source="../media/prompt-flow/how-to-process-image/chat-output-definition.png" alt-text="Screenshot of chat output type configuration." lightbox = "../media/prompt-flow/how-to-process-image/chat-output-definition.png":::  
 1. (Optional) You can add any custom logic to the flow to process the GPT-4V output. For example, you can add content safety tool to detect if the answer contains any inappropriate content, and return a final answer to the user.
     :::image type="content" source="../media/prompt-flow/how-to-process-image/chat-flow-postprocess.png" alt-text="Screenshot of processing gpt-4v output with content safety tool." lightbox = "../media/prompt-flow/how-to-process-image/chat-flow-postprocess.png":::
-1. Now you can **test the chatbot**.  Open the chat window, and input any questions with images. The chatbot will answer the questions based on the image and text inputs. The chat input value is automatically backfilled from the input in the chat window. You can find the texts with images in the chat box which is translated into a list of texts and images.
+1. Now you can **test the chatbot**. Open the chat window, and input any questions with images. The chatbot will answer the questions based on the image and text inputs. The chat input value is automatically backfilled from the input in the chat window. You can find the texts with images in the chat box which is translated into a list of texts and images.
     :::image type="content" source="../media/prompt-flow/how-to-process-image/chatbot-test.png" alt-text="Screenshot of chatbot interaction with images." lightbox = "../media/prompt-flow/how-to-process-image/chatbot-test.png":::
 
 > [!NOTE]
@@ -98,7 +130,7 @@ A batch run allows you to test the flow with an extensive dataset. There are thr
 - **Public image URL:** You can also reference the image URL in the entry file using this format: `{"data:<mime type>;url": "<image URL>"}`. For example, `{"data:image/png;url": "https://www.example.com/images/1.png"}`.
 - **Base64 string:** A Base64 string can be referenced in the entry file using this format: `{"data:<mime type>;base64": "<base64 string>"}`. For example, `{"data:image/png;base64": "iVBORw0KGgoAAAANSUhEUgAAAGQAAABLAQMAAAC81rD0AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABlBMVEUAAP7////DYP5JAAAAAWJLR0QB/wIt3gAAAAlwSFlzAAALEgAACxIB0t1+/AAAAAd0SU1FB+QIGBcKN7/nP/UAAAASSURBVDjLY2AYBaNgFIwCdAAABBoAAaNglfsAAAAZdEVYdGNvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVDnr0DLAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIwLTA4LTI0VDIzOjEwOjU1KzAzOjAwkHdeuQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMC0wOC0yNFQyMzoxMDo1NSswMzowMOEq5gUAAAAASUVORK5CYII="}`.
 
-In summary, prompt flow uses a unique dictionary format to represent an image, which is `{"data:<mime type>;<representation>": "<value>"}`. Here, `<mime type>` refers to HTML standard [MIME](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types) image types, and `<representation>` refers to the supported image representations: `path`,`url` and `base64`.
+In summary, prompt flow uses a unique dictionary format to represent an image, which is `{"data:<mime type>;<representation>": "<value>"}`. Here, `<mime type>` refers to HTML standard [MIME](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types) image types, and `<representation>` refers to the supported image representations: `path`,`url`, and `base64`.
 
 ### Create a batch run
 
@@ -125,7 +157,7 @@ For now, you can test the endpoint by sending request including image inputs.
 
 To consume the online endpoint with image input, you should represent the image by using the format `{"data:<mime type>;<representation>": "<value>"}`. In this case, `<representation>` can either be `url` or `base64`.
 
-If the flow generates image output, it is returned with `base64` format, for example, `{"data:<mime type>;base64": "<base64 string>"}`.
+If the flow generates image output, it's returned with `base64` format, for example, `{"data:<mime type>;base64": "<base64 string>"}`.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像処理に関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、画像データを処理する流れに関するドキュメントのマイナーな更新を示しています。43行が追加され、11行が削除された結果、合計54行が変更されました。主な変更は、Pythonツールを使用して画像を前処理するためのコード例が追加されたことです。このコードは、入力画像をトリミングし、JPEG形式で画像を保存する機能を示しています。

また、レビュー担当者の情報が削除され、日付が更新され、ユーザーにとっての可読性が向上しています。画像入力に関連する部分も強化され、ユーザーが画像データをどのように操作し、どのように機能を実装するかを具体的に理解できるようになりました。

具体的な手順や重要な注意点が明示されており、GPT-4Vツールを使用した画像処理のフローやチャットボットの構築に関する説明が改善されています。全体を通じて、画像処理を利用したプロンプトフローの使い方がより明確に説明され、実践的なアプローチが強調されています。

## articles/ai-studio/how-to/online-evaluation.md{#item-d9591b}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom:
   - build-2024
 ms.topic: how-to
 ms.date: 01/16/2025
-ms.reviewer: alehughes
+ms.reviewer: mesameki
 ms.author: lagayhar  
 author: lgayhardt
 ---
@@ -92,7 +92,7 @@ pip install azure-identity azure-ai-projects azure-ai-ml
 ```
 
 > [!TIP]
-> Optionally, you can use `pip install azure-ai-evaluation` if you want a code-first experience to fetch evaluator ID for built-in evaluators in code. To learn how to do this, see [Specifying evaluators from evaluator library](./develop/evaluate-sdk.md#specifying-evaluators-from-evaluator-library).
+> Optionally, you can use `pip install azure-ai-evaluation` if you want a code-first experience to fetch evaluator ID for built-in evaluators in code. To learn how to do this, see [Specifying evaluators from evaluator library](./develop/cloud-evaluation.md#specifying-evaluators-from-evaluator-library).
 
 ### Set up tracing for your generative AI application
 
@@ -165,7 +165,7 @@ Optionally, you can use the [sample operator](/kusto/query/sample-operator?view=
 
 ### Set up online evaluation with Azure AI Project SDK
 
-You can submit an online evaluation scheduled job with the Azure AI Project SDK via a Python API. See the below script to learn how to set up online evaluation with performance and quality (AI-assisted) evaluators. To view a comprehensive list of supported evaluators, see [Evaluate with the Azure AI Evaluation SDK](./develop/evaluate-sdk.md). To learn how to use custom evaluators, see [custom evaluators](./develop/evaluate-sdk.md#specifying-custom-evaluators).
+You can submit an online evaluation scheduled job with the Azure AI Project SDK via a Python API. See the below script to learn how to set up online evaluation with performance and quality (AI-assisted) evaluators. To view a comprehensive list of supported evaluators, see [Evaluate with the Azure AI Evaluation SDK](./develop/evaluate-sdk.md). To learn how to use custom evaluators, see [custom evaluators](./develop/cloud-evaluation.md#specifying-custom-evaluators).
 
 Start by importing the required packages and configuring the required variables:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オンライン評価に関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、オンライン評価に関するドキュメントのマイナーな更新を示しています。3行が追加され、3行が削除された結果、合計6行が変更されました。主な変更点は、レビュー担当者の情報の更新と、特定のドキュメントへのリンクの修正です。

具体的には、`pip install azure-ai-evaluation`に関連する説明のリンク先が変更され、`cloud-evaluation.md`に接続するようになりました。また、オンライン評価のセットアップに関する章では、Azure AIプロジェクトSDKを使用してオンライン評価のスケジュールジョブを提出する方法についての記述が明確に保たれていますが、リファレンスリンクが適切な新しいリソースに更新されています。

これにより、ユーザーは最新の情報に基づいた手順にアクセスしやすくなり、使いやすさが向上しています。全体として、本更新は情報の正確性を保つための重要な修正を含んでいます。

## articles/ai-studio/media/prompt-flow/how-to-process-image/batch-run-data-selection.png{#item-10bd03}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像処理に関するバッチ実行データ選択の画像更新"
}
```

### Explanation
このコードの変更は、画像処理に関するバッチ実行データ選択を示す画像の変更を示しています。具体的には、実際の変更内容はありませんが、対象の画像ファイルが更新されたことが示されています。画像のリンクは、GitHubリポジトリの最新の場所を参照しており、ユーザーが使用する際の視覚的な情報を提供しています。

この更新は、画像の改善または最適化を目的としている可能性があり、視覚的な要素としての役割を果たします。全体として、この変更は情報の視覚的な表現を向上させるためのものであり、コンテンツのアクセシビリティを高める要素として重要です。

## articles/ai-studio/media/prompt-flow/how-to-process-image/chat-input-definition.png{#item-943c2b}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャット入力定義に関する画像の更新"
}
```

### Explanation
このコードの変更は、チャット入力定義に関する画像の更新を示しています。具体的には、このファイルは変更されたが、追加や削除は行われておらず、実際の変更内容はありません。しかし、画像の参照が最新の状態に保たれていることが示されています。

提示されたリンクは、GitHubリポジトリ内の画像ファイルへのアクセスを提供し、ユーザーが視覚的情報に基づいて理解を深める手助けをします。この更新は、情報の視覚における一貫性を維持するために重要であり、関連する内容の視覚的な表現を向上させる役割を果たします。全体として、この変更は細かい調整を行うことで、コンテンツの質を高める目的があります。

## articles/ai-studio/media/prompt-flow/how-to-process-image/chat-output-definition.png{#item-a18f8c}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "チャット出力定義に関する画像の追加"
}
```

### Explanation
このコードの変更は、チャット出力定義に関連する新しい画像ファイルの追加を示しています。このファイルは新しく追加されたもので、他のファイルに対する追加や削除はありません。

この変更により、ユーザーはチャット出力に関する視覚的な情報を手に入れることができ、学習や実践に役立てることができます。提供されたリンクを通じて、この画像にアクセスし、詳細な情報を視覚的に理解することが可能となります。この新機能は、情報をより明確に伝えるための重要な要素となり、コンテンツ全体の質を向上させることに寄与します。

## articles/ai-studio/media/prompt-flow/how-to-process-image/gpt-4v-tool-in-chatflow.png{#item-eac13e}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4Vツールに関する画像の更新"
}
```

### Explanation
このコードの変更は、GPT-4Vツールに関する画像の更新を示しています。このファイルは変更されたものの、実際には追加や削除は行われておらず、変更内容はありません。これは、画像の内容や表示方法が最新の情報に基づいていることを示している可能性があります。

提供されたリンクを通じて、ユーザーは最新の情報にアクセスでき、この画像がどのようにGPT-4Vツールをチャットフローで活用できるかを視覚的に理解する手助けとなります。この更新は、コンテンツの一貫性を保つために重要であり、情報の正確性を向上させる一助となります。全体として、これは品質を高めるための小さな調整ですが、重要な役割を果たします。

## articles/ai-studio/media/prompt-flow/how-to-process-image/gpt-4v-tool.png{#item-ff092c}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4Vツールに関する画像の更新"
}
```

### Explanation
このコードの変更は、GPT-4Vツールに関連する画像の更新を示しています。この変更では、追加や削除は行われていませんが、画像自体が更新されたことを意味しています。具体的には、内容や表示に関するマイナーな調整があった可能性があります。

更新された画像は、ユーザーがGPT-4Vツールの機能や使用方法を理解するのに役立ちます。提供されたリンクを通じて、ユーザーは最新のビジュアル情報にアクセスし、どのようにこのツールを効果的に使用できるかを視覚的に確認することができます。このような小さな更新は、情報の一貫性と正確性を維持するために重要であり、全体的なユーザー体験の向上に寄与します。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -410,9 +410,11 @@ items:
       href: how-to/evaluate-prompts-playground.md
     - name: Generate synthetic and simulated data for evaluation
       href: how-to/develop/simulator-interaction-data.md
-    - name: Evaluate with the Azure AI Evaluation SDK
+    - name: Local evaluation with Azure AI Evaluation SDK
       href: how-to/develop/evaluate-sdk.md
       displayName: code,accuracy,metrics
+    - name: Cloud evaluation with Azure AI Projects SDK
+      href: how-to/develop/cloud-evaluation.md
     - name: Run evaluations from the portal
       href: how-to/evaluate-generative-ai-app.md
     - name: View evaluation results in the portal
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIスタジオの目次に関する更新"
}
```

### Explanation
このコードの変更は、AIスタジオの目次（TOC）の更新を示しています。具体的には、3つの新しい項目が追加され、1つの項目が削除されました。更新内容の概要は以下の通りです。

1. **項目名の変更**: 「Evaluate with the Azure AI Evaluation SDK」という項目が「Local evaluation with Azure AI Evaluation SDK」に変更されました。
2. **新しい項目の追加**: 「Cloud evaluation with Azure AI Projects SDK」という新しい項目が追加され、対応するリンクも設定されました。

これにより、ユーザーはローカル評価とクラウド評価の両方の手法について明確に理解できるようになります。目次の変更は、コンテンツの構成やユーザーのナビゲーションを改善するためのものです。提供されたリンクを通じて、関連するドキュメントへのアクセスも容易になります。この更新は、AIスタジオにおけるユーザー体験を向上させる重要な役割を果たします。


