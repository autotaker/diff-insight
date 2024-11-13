---
date: '2024-11-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d63c476...MicrosoftDocs:51e566e
summary: このコード差分では、AI Studioにおけるモデルデプロイおよびファインチューニングに関する記事が強化され、新たなサンプルノートブックの追加が行われています。これにより、Phi-3やLLaMAモデルに対するファインチューニングの具体的な指針が提供されています。また、Phi-3モデルに関する細かな更新も含まれています。特に破壊的な変更は報告されておらず、ユーザーはより理解しやすく整理されたファインチューニングプロセスを通じて、モデルの最適化を行いやすくなります。全体として、AI開発者にとって有益なリソースとなる内容です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d63c476...MicrosoftDocs:51e566e){target="_blank"}

# Highlights
このコード差分では、AI Studioにおけるモデルデプロイおよびファインチューニングに関する主要な記事が強化されています。主な変更点としては、新たなサンプルノートブックの追加が複数記事にわたって行われており、特定のモデルに対してより充実したファインチューニングの指針が提供されています。また、Phi-3モデルのファインチューニングにおけるマイナーな更新も含まれています。

## New features
- **サンプルノートブックの追加**：Phi-3やLLaMAモデルのファインチューニングに新たなサンプルノートブックが追加され、データセットの選定、ファインチューニング、モデルデプロイまでの具体的な手順が示されています。
- **Azure AIコンテンツフィルターの紹介**：安心して生成タスクを行えるよう、コンテンツフィルタリング機能に関する情報が追加されました。

## Breaking changes
- 特に破壊的な変更は報告されていません。

## Other updates
- Phi-3モデルのファインチューニング記事が細分化され、より詳しいモデルバージョンの説明と性能向上に関する情報が追加されました。

# Insights
この差分は、AIモデルのデプロイメントとファインチューニングの実用的なガイドラインを提供するために重要なステップを示しています。まず、サンプルノートブックが新たに追加されたことによって、ユーザーは手を動かして具体的なタスクに取り組む際のフローを習得する上で大きな助けとなるでしょう。たとえば、Phi-3モデル用にはダイアログ要約に焦点を当てたファインチューニング手法が詳しく記載されており、LLaMAモデルでは特定のデータセットを使ったトレーニング方法が紹介されています。

さらに、それぞれの記事にはAzure AIを使ったサーバーレスデプロイメントの例も含まれており、モデルを本番環境でどのように利用できるかを実践的に示しています。また、セキュリティ面にも配慮し、Azure AIのコンテンツフィルタリングが説明されていることから、安心してAIモデルを利用するための指針も含まれます。

一方で、Phi-3モデル関連の記事の更新では、モデル選択やバージョンに関する新たな情報が加わり、全体的にファインチューニングプロセスが整理され、理解しやすくなっています。このような更新により、ユーザーは多様なニーズに応じたモデル最適化を行いやすくなるでしょう。全体として、この差分はAI Studioを利用したAI開発者にとって非常に有益なリソースとなると考えられます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [deploy-models-phi-3.md](#item-47e305) | new feature | サンプルノートブックの追加 | modified | 4 | 0 | 4 | 
| [fine-tune-model-llama.md](#item-2a42d8) | new feature | サンプルノートブックの追加 | modified | 4 | 0 | 4 | 
| [fine-tune-phi-3.md](#item-5b722a) | minor update | Phi-3モデルのファインチューニングに関する更新 | modified | 55 | 21 | 76 | 


# Modified Contents
## articles/ai-studio/how-to/deploy-models-phi-3.md{#item-47e305}

<details>
<summary>Diff</summary>
````diff
@@ -1476,6 +1476,10 @@ Phi-3 family models deployed to managed compute are billed based on core hours o
 
 It is a good practice to start with a low number of instances and scale up as needed. You can monitor the cost of the compute instance in the Azure portal.
 
+## Sample notebook
+
+You can use this [sample notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/finetuning/standalone/chat-completion/chat_completion_with_model_as_service.ipynb)  to create a standalone fine-tuning job to enhance a model's ability to summarize dialogues between two people using the Samsum dataset. The training data utilized is the ultrachat_200k dataset, which is divided into four splits suitable for supervised fine-tuning (sft) and generation ranking (gen). The notebook employs the available Azure AI models for the chat-completion task (If you would like to use a different model than what's used in the notebook, you can replace the model name). The notebook includes setting up prerequisites, selecting a model to fine-tune, creating training and validation datasets, configuring and submitting the fine-tuning job, and finally, creating a serverless deployment using the fine-tuned model for sample inference.
+
 ## Related content
 
 
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "サンプルノートブックの追加"
}
```

### Explanation
この変更では、AI StudioにおけるPhi-3モデルのデプロイ方法に関する記事に、新しいサンプルノートブックが追加されました。追加された内容には、モデルを強化するためのスタンドアロンのファインチューニングジョブを作成する手順が含まれており、具体的にはSamsumデータセットを使ったダイアログの要約に関するものです。ノートブックでは、Azure AIモデルを使用したチャット完了タスクのためのファインチューニング、データセットの作成、ジョブの設定と提出、ならびにファインチューニングされたモデルを用いたサーバーレスデプロイメントの作成がガイドされています。この更新により、ユーザーは特定のニーズに応じてモデルのファインチューニングを行いやすくなります。また、関連するコンテンツへのリンクも追加され、より深く学ぶためのリソースが提供されています。

## articles/ai-studio/how-to/fine-tune-model-llama.md{#item-2a42d8}

<details>
<summary>Diff</summary>
````diff
@@ -269,6 +269,10 @@ Each time a project subscribes to a given offer from the Azure Marketplace, a ne
 
 For more information on how to track costs, see [monitor costs for models offered throughout the Azure Marketplace](./costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace).
 
+## Sample notebook
+
+You can use this [sample notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/finetuning/standalone/chat-completion/chat_completion_with_model_as_service.ipynb)  to create a standalone fine-tuning job to enhance a model's ability to summarize dialogues between two people using the Samsum dataset. The training data utilized is the ultrachat_200k dataset, which is divided into four splits suitable for supervised fine-tuning (sft) and generation ranking (gen). The notebook employs the available Azure AI models for the chat-completion task (If you would like to use a different model than what's used in the notebook, you can replace the model name). The notebook includes setting up prerequisites, selecting a model to fine-tune, creating training and validation datasets, configuring and submitting the fine-tuning job, and finally, creating a serverless deployment using the fine-tuned model for sample inference.
+
 ## Content filtering
 
 Models deployed as a service with pay-as-you-go billing are protected by Azure AI Content Safety. When deployed to real-time endpoints, you can opt out of this capability. With Azure AI content safety enabled, both the prompt and completion pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions. Learn more about [Azure AI Content Safety](../concepts/content-filtering.md).
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "サンプルノートブックの追加"
}
```

### Explanation
この変更では、LLaMAモデルのファインチューニングに関する記事に、新たなサンプルノートブックが追加されました。このノートブックは、Samsumデータセットを使用して、二人の間のダイアログを要約する能力を向上させるためのスタンドアロンのファインチューニングジョブを作成する手順を導入しています。使用されるトレーニングデータはultrachat_200kデータセットであり、これは監視付きファインチューニング（SFT）と生成ランキング（GEN）に適した四つの分割があります。また、ノートブックには、ファインチューニングするモデルの選択、トレーニングと検証データセットの作成、ファインチューニングジョブの設定と提出、最終的にはファインチューニングされたモデルを使用したサーバーレスデプロイメントによる推論のサンプルが含まれています。さらに、Azure AIが提供するコンテンツフィルタリング機能についての情報も追加され、安心してサービスを利用できることが強調されています。これは、ユーザーが有害なコンテンツの出力を防ぐ仕組みを理解する手助けとなります。

## articles/ai-studio/how-to/fine-tune-phi-3.md{#item-5b722a}

<details>
<summary>Diff</summary>
````diff
@@ -21,46 +21,39 @@ The Phi-3 family of SLMs is a collection of instruction-tuned generative text mo
 
 [!INCLUDE [models-preview](../includes/models-preview.md)]
 
-## [Phi-3-mini](#tab/phi-3-mini)
+# [Phi-3-mini](#tab/phi-3-mini)
 
 Phi-3 Mini is a 3.8B parameters, lightweight, state-of-the-art open model built upon datasets used for Phi-2 - synthetic data and filtered websites - with a focus on high-quality, reasoning dense data. The model belongs to the Phi-3 model family, and the Mini version comes in two variants 4K and 128K which is the context length (in tokens) it can support.
 
-- [Phi-3-mini-4k-Instruct](https://ai.azure.com/explore/models/Phi-3-mini-4k-instruct/version/4/registry/azureml)
-- [Phi-3-mini-128k-Instruct](https://ai.azure.com/explore/models/Phi-3-mini-128k-instruct/version/4/registry/azureml)
+- [Phi-3-mini-4k-Instruct](https://ai.azure.com/explore/models/Phi-3-mini-4k-instruct/version/4/registry/azureml) (preview)
+- [Phi-3-mini-128k-Instruct](https://ai.azure.com/explore/models/Phi-3-mini-128k-instruct/version/4/registry/azureml) (preview)
 
 The model underwent a rigorous enhancement process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures. When assessed against benchmarks testing common sense, language understanding, math, code, long context and logical reasoning, Phi-3 Mini-4K-Instruct and Phi-3 Mini-128K-Instruct showcased a robust and state-of-the-art performance among models with less than 13 billion parameters.
 
 
-## [Phi-3-medium](#tab/phi-3-medium)
+# [Phi-3-medium](#tab/phi-3-medium)
 Phi-3 Medium is a 14B parameters, lightweight, state-of-the-art open model. Phi-3-Medium was trained with Phi-3 datasets that include both synthetic data and the filtered, publicly available websites data, with a focus on high quality and reasoning-dense properties.
 
 The model belongs to the Phi-3 model family, and the Medium version comes in two variants, 4K and 128K, which denote the context length (in tokens) that each model variant can support.
 
-- Phi-3-medium-4k-Instruct
-- Phi-3-medium-128k-Instruct
+- Phi-3-medium-4k-Instruct (preview)
+- Phi-3-medium-128k-Instruct (preview)
 
 The model underwent a rigorous enhancement process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures. When assessed against benchmarks that test common sense, language understanding, math, code, long context and logical reasoning, Phi-3-Medium-4k-Instruct and Phi-3-Medium-128k-Instruct showcased a robust and state-of-the-art performance among models with less than 13 billion parameters.
 
----
-
-
-## [Phi-3-mini](#tab/phi-3-mini)
 
-The following models are available in Azure AI Studio for Phi 3 when fine-tuning as a service with pay-as-you-go:
+# [Phi-3.5](#tab/phi-3-5)
 
-- `Phi-3-mini-4k-instruct` (preview)
-- `Phi-3-mini-128k-instruct` (preview)
 
-Fine-tuning of Phi-3 models is currently supported in projects located in East US 2.
+Phi-3.5-mini-Instruct is a 3.8B parameter model enhances multi-lingual support, reasoning capability, and offers an extended context length of 128K tokens
 
-## [Phi-3-medium](#tab/phi-3-medium)
+Phi-3.5-MoE-Instruct. Featuring 16 experts and 6.6B active parameters, this model delivers high performance, reduced latency, multi-lingual support, and robust safety measures, surpassing the capabilities of larger models while maintaining the efficacy of the Phi models.
 
-The following models are available in Azure AI Studio for Phi 3 when fine-tuning as a service with pay-as-you-go:
+- Phi-3.5-mini-Instruct (preview)
+- Phi-3.5-MoE-Instruct (preview)
 
-- `Phi-3-medium-4k-instruct` (preview)
-- `Phi-3-medium-128k-instruct` (preview)
+The models underwent a rigorous enhancement process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures. When assessed against benchmarks that test common sense, language understanding, math, code, long context and logical reasoning, Phi-3.5-mini-Instruct and Phi-3.5-MoE-Instruct showcased a robust and state-of-the-art performance among models with less than 13 billion parameters.
 
-Fine-tuning of Phi-3 models is currently supported in projects located in East US 2.
 
 ---
 
@@ -163,7 +156,45 @@ To fine-tune a Phi-3 model:
 1. If this is your first time fine-tuning the model in the project, you have to subscribe your project for the particular offering (for example, Phi-3-medium-128k-instruct) from Azure AI Studio. This step requires that your account has the Azure subscription permissions and resource group permissions listed in the prerequisites. Each project has its own subscription to the particular Azure AI Studio offering, which allows you to control and monitor spending. Select **Subscribe and fine-tune**.
 
     > [!NOTE]
-    > Subscribing a project to a particular Azure AI Studio offering (in this case, Phi-3-mini-128k-instruct) requires that your account has **Contributor** or **Owner** access at the subscription level where the project is created. Alternatively, your user account can be assigned a custom role that has the Azure subscription permissions and resource group permissions listed in the [prerequisites](#prerequisites).
+    > Subscribing a project to a particular Azure AI Studio offering (in this case, Phi-3-medium-128k-instruct) requires that your account has **Contributor** or **Owner** access at the subscription level where the project is created. Alternatively, your user account can be assigned a custom role that has the Azure subscription permissions and resource group permissions listed in the [prerequisites](#prerequisites).
+
+1. Once you sign up the project for the particular Azure AI Studio offering, subsequent fine-tuning of the _same_ offering in the _same_ project don't require subscribing again. Therefore, you don't need to have the subscription-level permissions for subsequent fine-tune jobs. If this scenario applies to you, select **Continue to fine-tune**.
+
+1. Enter a name for your fine-tuned model and the optional tags and description.
+1. Select training data to fine-tune your model. See [data preparation](#data-preparation) for more information.
+
+    > [!NOTE]
+    > If you have your training/validation files in a credential less datastore, you will need to allow workspace managed identity access to your datastore in order to proceed with MaaS finetuning with a credential less storage. On the "Datastore" page, after clicking "Update authentication" > Select the following option: 
+    
+    ![Use workspace managed identity for data preview and profiling in Azure Machine Learning Studio.](../media/how-to/fine-tune/phi-3/credentials.png)
+
+    Make sure all your training examples follow the expected format for inference. To fine-tune models effectively, ensure a balanced and diverse dataset. This involves maintaining data balance, including various scenarios, and periodically refining training data to align with real-world expectations, ultimately leading to more accurate and balanced model responses.
+    - The batch size to use for training. When set to -1, batch_size is calculated as 0.2% of examples in training set and the max is 256.
+    - The fine-tuning learning rate is the original learning rate used for pretraining multiplied by this multiplier. We recommend experimenting with values between 0.5 and 2. Empirically, we've found that larger learning rates often perform better with larger batch sizes. Must be between 0.0 and 5.0.
+    - Number of training epochs. An epoch refers to one full cycle through the data set.
+
+1. Task parameters are an optional step and an advanced option- Tuning hyperparameter is essential for optimizing large language models (LLMs) in real-world applications. It allows for improved performance and efficient resource usage. Users can choose to keep the default settings or advanced users can customize parameters like epochs or learning rate.
+
+1. Review your selections and proceed to train your model.
+
+Once your model is fine-tuned, you can deploy the model and can use it in your own application, in the playground, or in prompt flow. For more information, see [How to deploy Phi-3 family of large language models with Azure AI Studio](./deploy-models-phi-3.md).
+
+
+# [Phi-3.5](#tab/phi-3-5)
+
+To fine-tune a Phi-3.5 model:
+
+1. Sign in to [Azure AI Studio](https://ai.azure.com).
+1. Choose the model you want to fine-tune from the Azure AI Studio [model catalog](https://ai.azure.com/explore/models). 
+
+1. On the model's **Details** page, select **fine-tune**.
+
+1. Select the project in which you want to fine-tune your models. To use the pay-as-you-go model fine-tune offering, your workspace must belong to the **East US 2** region.
+1. On the fine-tune wizard, select the link to **Azure AI Studio Terms** to learn more about the terms of use. You can also select the **Azure AI Studio offer details** tab to learn about pricing for the selected model.
+1. If this is your first time fine-tuning the model in the project, you have to subscribe your project for the particular offering (for example, Phi-3.5-mini-instruct) from Azure AI Studio. This step requires that your account has the Azure subscription permissions and resource group permissions listed in the prerequisites. Each project has its own subscription to the particular Azure AI Studio offering, which allows you to control and monitor spending. Select **Subscribe and fine-tune**.
+
+    > [!NOTE]
+    > Subscribing a project to a particular Azure AI Studio offering (in this case, Phi-3.5-mini-instruct) requires that your account has **Contributor** or **Owner** access at the subscription level where the project is created. Alternatively, your user account can be assigned a custom role that has the Azure subscription permissions and resource group permissions listed in the [prerequisites](#prerequisites).
 
 1. Once you sign up the project for the particular Azure AI Studio offering, subsequent fine-tuning of the _same_ offering in the _same_ project don't require subscribing again. Therefore, you don't need to have the subscription-level permissions for subsequent fine-tune jobs. If this scenario applies to you, select **Continue to fine-tune**.
 
@@ -197,10 +228,13 @@ You can delete a fine-tuned model from the fine-tuning model list in [Azure AI S
 
 ## Cost and quotas
 
-### Cost and quota considerations for Phi-3 models fine-tuned as a service
+### Cost and quota considerations for Phi models fine-tuned as a service
 
 Phi models fine-tuned as a service are offered by Microsoft and integrated with Azure AI Studio for use. You can find the pricing when [deploying](./deploy-models-phi-3.md) or fine-tuning the models under the Pricing and terms tab on deployment wizard.
 
+## Sample notebook
+
+You can use this [sample notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/finetuning/standalone/chat-completion/chat_completion_with_model_as_service.ipynb)  to create a standalone fine-tuning job to enhance a model's ability to summarize dialogues between two people using the Samsum dataset. The training data utilized is the ultrachat_200k dataset, which is divided into four splits suitable for supervised fine-tuning (sft) and generation ranking (gen). The notebook employs the available Azure AI models for the chat-completion task (If you would like to use a different model than what's used in the notebook, you can replace the model name). The notebook includes setting up prerequisites, selecting a model to fine-tune, creating training and validation datasets, configuring and submitting the fine-tuning job, and finally, creating a serverless deployment using the fine-tuned model for sample inference.
 
 ## Content filtering
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3モデルのファインチューニングに関する更新"
}
```

### Explanation
この変更は、Phi-3モデルのファインチューニングに関するドキュメントの更新を含んでおり、文書全体にわたり56行が追加され、21行が削除されました。更新内容には、Phi-3モデルのバージョンに関する詳細な説明が含まれ、特に新しいPhi-3.5モデルの導入や、モデルの性能向上に関連する情報が追加されています。加えて、ファインチューニングプロセスの手順が整理され、より明確に説明されています。また、関連するサンプルノートブックへのリンクが追加され、ユーザーが実際にファインチューニングを行う際の支援となるリソースが提供されています。これにより、ユーザーはPhi-3モデルを効果的に利用するための具体的なガイドラインを得られるようになりました。全体として、記事はより包括的で、利用者が異なるモデルを選択し、ファインチューニングを実行する際の理解を深めるのに役立つ内容となっています。


