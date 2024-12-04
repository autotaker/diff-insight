---
date: '2024-12-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3b6e85f...MicrosoftDocs:2c6389f
summary: 今回の変更では、Azure OpenAIに関する文書が更新され、特にデータ設定やネットワークアクセスにおける透明性と一貫性が向上しました。新たに詳細な設定方法が追加され、ユーザーガイドの明瞭性も強化されています。しかし、SynapseMLとの統合に関する文書は完全に削除され、Azure
  OpenAIとの連携情報が失われています。また、他の更新としては、認証方法やクォータに関する文書の改善、目次やリンクの更新が行われています。この改訂は、ユーザーがより効果的にAzure
  OpenAIを利用するための重要なステップと評価されており、特にデータセキュリティに関する具体的なガイダンスが追加されました。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3b6e85f...MicrosoftDocs:2c6389f){target="_blank"}

# Highlights
今回の変更点は、Azure OpenAI関連の文書に対するさまざまな更新が含まれています。特に目立つのは、データ設定やネットワークアクセスに関する透明性と一貫性が強化され、ユーザーガイドの明瞭性が向上されたことです。また、SynapseMLとの統合に関するドキュメントが完全に削除されました。

## New features
- Azure OpenAIを通じたデータ構成とネットワークアクセスの詳細な設定方法が新たに追加されました。
- Provisioned Throughputに関する詳細説明が追加され、ユーザーがサービスを最大限に活用するためのガイダンスが強化されました。

## Breaking changes
- SynapseMLに関する統合シナリオを含むドキュメントが削除されました。これにより、Azure OpenAIサービスとSynapseMLの連携方法に関する情報が失われています。

## Other updates
- Weights & Biases統合に関する手順の改善。
- 認証方法に関する文書の仕様調整と更新。
- クォータと制限に関する文書の改善。
- Azure OpenAI関連文書の目次とリンクが更新され、情報の一貫性が保たれました。
- "What's new" のセクションで、データ管理に関する記事が最新の内容に更新されました。

# Insights
このドキュメント更新は、ユーザーがAzure OpenAIをより効果的に利用できるようにするための重要なステップといえます。特に、データセキュリティやネットワークアクセスについてのガイダンスが具体的かつ詳細に示されたことで、実際の環境設定に役立つ情報が充実しています。昨今のデータ保護とアクセス制御の重要性を背景に、仮想ネットワークやプライベートエンドポイントに関する詳しい説明が追加されており、これによりセキュリティリスクを最小化しつつ、効率的にデータを管理する方法を示していることが評価されます。

さらに、Provisioned Throughputの改訂は、ユーザーが使用するリソースに対してより柔軟に対応できることを示しています。この更新は、特に大規模データセットを扱うユーザーにとって重要であり、リソース管理の面での柔軟性を提供します。

一方で、SynapseMLとの統合記事が削除されたことは、Azure OpenAIの機能開発やドキュメントの構成における戦略的変更を示唆しています。今後、この統合機能がどう展開していくのか、不明瞭な部分も少なからずあります。そのためユーザーは、公式ドキュメントや関連するチャネルでの最新情報を追い続ける必要があります。

総じて、この改訂はAzure OpenAIのドキュメントにおける透明性と専門性を高めるものであり、利用者がサービスの機能を活用する際に役立つ具体的な指針を提供しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [use-your-data.md](#item-455d6e) | minor update | データを使用するためのAzure OpenAIの構成に関する更新 | modified | 6 | 6 | 12 | 
| [integrate-synapseml.md](#item-88e852) | breaking change | SynapseMLとの統合に関するドキュメントの削除 | removed | 0 | 351 | 351 | 
| [on-your-data-configuration.md](#item-4875d3) | minor update | データを使用するためのAzure OpenAI設定に関するドキュメントの更新 | renamed | 6 | 8 | 14 | 
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | Provisioned Throughput on Azure OpenAIに関する文書の改訂 | modified | 20 | 15 | 35 | 
| [weights-and-biases-integration.md](#item-8ae868) | minor update | Weights & Biases統合に関する文書の更新 | modified | 18 | 18 | 36 | 
| [on-your-data-authentication.md](#item-43fc01) | minor update | データ接続の認証方法に関する文書の更新 | modified | 2 | 2 | 4 | 
| [index.yml](#item-0adb87) | minor update | Azure OpenAIのデータにおけるネットワークとアクセス設定に関するリンクの更新 | modified | 2 | 2 | 4 | 
| [quotas-limits.md](#item-06c6f9) | minor update | Azure OpenAIのクォータおよび制限に関する文書の改善 | modified | 4 | 4 | 8 | 
| [toc.yml](#item-c945af) | minor update | Azure OpenAIトピックの目次の更新 | modified | 2 | 6 | 8 | 
| [whats-new.md](#item-53303b) | minor update | Azure OpenAIの新機能に関する文書の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/use-your-data.md{#item-455d6e}

<details>
<summary>Diff</summary>
````diff
@@ -43,7 +43,7 @@ To get started, [connect your data source](../use-your-data-quickstart.md) using
 
 ## Azure Role-based access controls (Azure RBAC) for adding data sources
 
-To use Azure OpenAI On Your Data fully, you need to set one or more Azure RBAC roles. See [Use Azure OpenAI On Your Data securely](../how-to/use-your-data-securely.md#role-assignments) for more information.
+To use Azure OpenAI On Your Data fully, you need to set one or more Azure RBAC roles. See [Azure OpenAI On Your Data configuration](../how-to/on-your-data-configuration.md#role-assignments) for more information.
 
 ## Data formats and file types
 
@@ -131,7 +131,7 @@ Azure OpenAI On Your Data has intelligent search enabled for your data. Semantic
 > [!NOTE] 
 > Document-level access control is supported when you select Azure AI Search as your data source.
 
-Azure OpenAI On Your Data lets you restrict the documents that can be used in responses for different users with Azure AI Search [security filters](/azure/search/search-security-trimming-for-azure-search-with-aad). When you enable document level access, the search results returned from Azure AI Search and used to generate a response are trimmed based on user Microsoft Entra group membership. You can only enable document-level access on existing Azure AI Search indexes See [Use Azure OpenAI On Your Data securely](../how-to/use-your-data-securely.md#document-level-access-control) for more information.
+Azure OpenAI On Your Data lets you restrict the documents that can be used in responses for different users with Azure AI Search [security filters](/azure/search/search-security-trimming-for-azure-search-with-aad). When you enable document level access, the search results returned from Azure AI Search and used to generate a response are trimmed based on user Microsoft Entra group membership. You can only enable document-level access on existing Azure AI Search indexes. See [Azure OpenAI On Your Data network and access configuration](../how-to/on-your-data-configuration.md#document-level-access-control) for more information.
 
 
 ### Index field mapping 
@@ -387,7 +387,7 @@ A Teams app lets you bring conversational experience to your users in Teams to i
 - Sign in to your [Microsoft 365 developer account](/microsoftteams/platform/concepts/build-and-test/prepare-your-o365-tenant) (using this link to get a test account: [Developer program](https://developer.microsoft.com/microsoft-365/dev-program)).
     - Enable **custom Teams apps** and turn on **custom app uploading** in your account (instructions [here](/microsoftteams/platform/concepts/build-and-test/prepare-your-o365-tenant#enable-custom-teams-apps-and-turn-on-custom-app-uploading))
 - [Azure command-line interface (CLI)](/cli/azure/install-azure-cli) installed. This is a cross-platform command-line tool to connect to Azure and execute administrative commands on Azure resources. For more information on setting up environment variables, see the [Azure SDK documentation](https://github.com/Azure/azure-sdk-for-go/wiki/Set-up-Your-Environment-for-Authentication).
-- Your Azure account has been assigned **Cognitive Services OpenAI user** or **Cognitive Services OpenAI Contributor** role of the Azure OpenAI resource you're using, allowing your account to make Azure OpenAI API calls. For more information, see [Using your data with Azure OpenAI securely](/azure/ai-services/openai/how-to/use-your-data-securely#using-the-api) and [Add role assignment to an Azure OpenAI resource](/azure/ai-services/openai/how-to/role-based-access-control#add-role-assignment-to-an-azure-openai-resource) for instructions on setting this role in the Azure portal. 
+- Your Azure account has been assigned **Cognitive Services OpenAI user** or **Cognitive Services OpenAI Contributor** role of the Azure OpenAI resource you're using, allowing your account to make Azure OpenAI API calls. For more information, see [Azure OpenAI On Your data configuration](../how-to/on-your-data-configuration.md#using-the-api) and [Add role assignment to an Azure OpenAI resource](/azure/ai-services/openai/how-to/role-based-access-control#add-role-assignment-to-an-azure-openai-resource) for instructions on setting this role in the Azure portal. 
 
 
 You can deploy to a standalone Teams app directly from Azure OpenAI Studio. Follow the steps below: 
@@ -433,9 +433,9 @@ Deploying to a standalone web app lets you and your users to interact with chat
 
 ---
 
-## Use Azure OpenAI On Your Data securely
+## Configure access and networking for Azure OpenAI On Your Data
 
-You can use Azure OpenAI On Your Data securely by protecting data and resources with Microsoft Entra ID role-based access control, virtual networks, and private endpoints. You can also restrict the documents that can be used in responses for different users with Azure AI Search security filters. See [Securely use Azure OpenAI On Your Data](../how-to/use-your-data-securely.md).
+You can use Azure OpenAI On Your Data and protect data and resources with Microsoft Entra ID role-based access control, virtual networks, and private endpoints. You can also restrict the documents that can be used in responses for different users with Azure AI Search security filters. See [Azure OpenAI On Your Data access and network configuration](../how-to/on-your-data-configuration.md).
 
 ## Best practices
 
@@ -743,6 +743,6 @@ If your Azure OpenAI resource is in another region, you won't be able to use Azu
 ## Next steps
 * [Get started using your data with Azure OpenAI](../use-your-data-quickstart.md)
 
-* [Securely use Azure OpenAI On Your Data](../how-to/use-your-data-securely.md)
+* [Azure OpenAI On Your Data network and access configuration](../how-to/on-your-data-configuration.md)
 
 * [Introduction to prompt engineering](./prompt-engineering.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データを使用するためのAzure OpenAIの構成に関する更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIにおけるデータ利用に関する文書の一部を更新しています。具体的には、役割ベースのアクセス制御（RBAC）の設定に関するリンクや文言が修正され、より明確にドキュメントが整備されました。また、ドキュメント全体の一貫性を保つために、用語の変更やセクションヘッダーが更新されています。

- 古い内容では、「安全にデータを使用する方法」に関するリンクが示されていましたが、これを「データ構成」に関する詳細なリンクに変更しました。
- 追加された情報として、ドキュメントレベルのアクセス制御の機能が強調され、ユーザーのMicrosoft Entraグループメンバーシップに基づいて結果が制限されることが説明されています。
- 新たに「アクセスとネットワークの構成」というセクションが設けられ、ユーザーがAzure OpenAIをどのように安全に利用できるかについての情報が提供されています。

これにより、ユーザーはAzure OpenAIを適切に設定し、安全に利用する方法を理解しやすくなります。

## articles/ai-services/openai/how-to/integrate-synapseml.md{#item-88e852}

<details>
<summary>Diff</summary>
````diff
@@ -1,351 +0,0 @@
----
-title: 'Use Azure OpenAI Service with large datasets'
-titleSuffix: Azure OpenAI
-description: Learn how to integrate Azure OpenAI Service with SynapseML and Apache Spark to apply large language models at a distributed scale.
-#services: cognitive-services
-manager: nitinme
-ms.service: azure-ai-openai
-ms.custom: build-2023, build-2023-dataai
-ms.topic: how-to
-ms.date: 09/01/2024
-author: mrbullwinkle
-ms.author: mbullwin
-recommendations: false
----
-
-# Use Azure OpenAI with large datasets
-
-Azure OpenAI can be used to solve a large number of natural language tasks through prompting the completion API. To make it easier to scale your prompting workflows from a few examples to large datasets of examples, Azure OpenAI Service is integrated with the distributed machine learning library [SynapseML](https://www.microsoft.com/research/blog/synapseml-a-simple-multilingual-and-massively-parallel-machine-learning-library/). This integration makes it easy to use the [Apache Spark](https://spark.apache.org/) distributed computing framework to process millions of prompts with Azure OpenAI Service.
-
-This tutorial shows how to apply large language models at a distributed scale by using Azure OpenAI and Azure Synapse Analytics.
-
-## Prerequisites
-
-- An Azure subscription. <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
-
-
-- An Azure OpenAI resource. [Create a resource](create-resource.md?pivots=web-portal#create-a-resource).
-
-- An Apache Spark cluster with SynapseML installed.
-
-   - Create a [serverless Apache Spark pool](/azure/synapse-analytics/get-started-analyze-spark#create-a-serverless-apache-spark-pool).
-   - To install SynapseML for your Apache Spark cluster, see [Install SynapseML](#install-synapseml).
-
-> [!NOTE]
-> The `OpenAICompletion()` transformer is designed to work with the [Azure OpenAI Service legacy models](/azure/ai-services/openai/concepts/legacy-models) like `Text-Davinci-003`, which supports prompt-based completions. Newer models like the current `GPT-3.5 Turbo` and `GPT-4` model series are designed to work with the new chat completion API that expects a specially formatted array of messages as input. If you working with embeddings or chat completion models, please check the [Chat Completion](#chat-completion) and [Generating Text Embeddings](#generating-text-embeddings) sections bellow.
-> 
-> The Azure OpenAI SynapseML integration supports the latest models via the [OpenAIChatCompletion()](https://github.com/microsoft/SynapseML/blob/0836e40efd9c48424e91aa10c8aa3fbf0de39f31/cognitive/src/main/scala/com/microsoft/azure/synapse/ml/cognitive/openai/OpenAIChatCompletion.scala#L24) transformer.
-
-We recommend that you [create an Azure Synapse workspace](/azure/synapse-analytics/get-started-create-workspace). However, you can also use Azure Databricks, Azure HDInsight, Spark on Kubernetes, or the Python environment with the `pyspark` package.
-
-## Use example code as a notebook
-
-To use the example code in this article with your Apache Spark cluster, complete the following steps:
-
-1. Prepare a new or existing notebook.
-
-1. Connect your Apache Spark cluster with your notebook.
-
-1. Install SynapseML for your Apache Spark cluster in your notebook.
-
-1. Configure the notebook to work with your Azure OpenAI service resource.
-
-### Prepare your notebook
-
-You can create a new notebook in your Apache Spark platform, or you can import an existing notebook. After you have a notebook in place, you can add each snippet of example code in this article as a new cell in your notebook.
-
-- To use a notebook in Azure Synapse Analytics, see [Create, develop, and maintain Synapse notebooks in Azure Synapse Analytics](/azure/synapse-analytics/spark/apache-spark-development-using-notebooks).
-
-- To use a notebook in Azure Databricks, see [Manage notebooks for Azure Databricks](/azure/databricks/notebooks/notebooks-manage).
-
-- (Optional) Download [this demonstration notebook](https://github.com/microsoft/SynapseML/blob/master/docs/Explore%20Algorithms/OpenAI/OpenAI.ipynb) and connect it with your workspace. During the download process, select **Raw**, and then save the file. 
-
-### Connect your cluster
-
-When you have a notebook ready, connect or _attach_ your notebook to an Apache Spark cluster.
-
-### Install SynapseML
-
-To run the exercises, you need to install SynapseML on your Apache Spark cluster. For more information, see [Install SynapseML](https://microsoft.github.io/SynapseML/docs/Get%20Started/Install%20SynapseML/) on the [SynapseML website](https://microsoft.github.io/SynapseML/).
-
-To install SynapseML, create a new cell at the top of your notebook and run the following code.
-
-- For a **Spark3.2 pool**, use the following code:
-
-   ```python
-   %%configure -f
-   {
-     "name": "synapseml",
-     "conf": {
-         "spark.jars.packages": "com.microsoft.azure:synapseml_2.12:0.11.2,org.apache.spark:spark-avro_2.12:3.3.1",
-         "spark.jars.repositories": "https://mmlspark.azureedge.net/maven",
-         "spark.jars.excludes": "org.scala-lang:scala-reflect,org.apache.spark:spark-tags_2.12,org.scalactic:scalactic_2.12,org.scalatest:scalatest_2.12,com.fasterxml.jackson.core:jackson-databind",
-         "spark.yarn.user.classpath.first": "true",
-         "spark.sql.parquet.enableVectorizedReader": "false",
-         "spark.sql.legacy.replaceDatabricksSparkAvro.enabled": "true"
-     }
-   }
-   ```
-
-- For a **Spark3.3 pool**, use the following code:
-
-   ```python
-   %%configure -f
-   {
-     "name": "synapseml",
-     "conf": {
-         "spark.jars.packages": "com.microsoft.azure:synapseml_2.12:0.11.2-spark3.3",
-         "spark.jars.repositories": "https://mmlspark.azureedge.net/maven",
-         "spark.jars.excludes": "org.scala-lang:scala-reflect,org.apache.spark:spark-tags_2.12,org.scalactic:scalactic_2.12,org.scalatest:scalatest_2.12,com.fasterxml.jackson.core:jackson-databind",
-         "spark.yarn.user.classpath.first": "true",
-         "spark.sql.parquet.enableVectorizedReader": "false"
-     }
-   }
-   ```
-
-The connection process can take several minutes.
-
-### Configure the notebook
-
-Create a new code cell and run the following code to configure the notebook for your service. Set the `resource_name`, `deployment_name`, `location`, and `key` variables to the corresponding values for your Azure OpenAI resource.
-
-```python
-import os
-
-# Replace the following values with your Azure OpenAI resource information
-resource_name = "<RESOURCE_NAME>"      # The name of your Azure OpenAI resource.
-deployment_name = "<DEPLOYMENT_NAME>"  # The name of your Azure OpenAI deployment.
-location = "<RESOURCE_LOCATION>"       # The location or region ID for your resource.
-key = "<RESOURCE_API_KEY>"             # The key for your resource.
-
-assert key is not None and resource_name is not None
-```
-
-Now you're ready to start running the example code.
-
-> [!IMPORTANT]
-> Remember to remove the key from your code when you're done, and never post it publicly. For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information, see [Azure AI services security](../../security-features.md).
-
-
-## Create a dataset of prompts
-
-The first step is to create a dataframe consisting of a series of rows, with one prompt per row.
-
-You can also load data directly from Azure Data Lake Storage or other databases. For more information about loading and preparing Spark dataframes, see the [Apache Spark Data Sources](https://spark.apache.org/docs/latest/sql-data-sources.html).
-
-```python
-df = spark.createDataFrame(
-    [
-        ("Hello my name is",),
-        ("The best code is code that's",),
-        ("SynapseML is ",),
-    ]
-).toDF("prompt")
-```
-
-## Create the OpenAICompletion Apache Spark client
-
-To apply Azure OpenAI Completion generation to the dataframe, create an `OpenAICompletion` object that serves as a distributed client. Parameters can be set either with a single value, or by a column of the dataframe with the appropriate setters on the `OpenAICompletion` object.
-
-In this example, you set the `maxTokens` parameter to 200. A token is around four characters, and this limit applies to the sum of the prompt and the result. You also set the `promptCol` parameter with the name of the prompt column in the dataframe, such as **prompt**.
-
-```python
-from synapse.ml.cognitive import OpenAICompletion
-
-completion = (
-    OpenAICompletion()
-    .setSubscriptionKey(key)
-    .setDeploymentName(deployment_name)
-    .setUrl("https://{}.openai.azure.com/".format(resource_name))
-    .setMaxTokens(200)
-    .setPromptCol("prompt")
-    .setErrorCol("error")
-    .setOutputCol("completions")
-)
-```
-
-## Transform the dataframe with the OpenAICompletion client
-
-After you have the dataframe and completion client, you can transform your input dataset and add a column called `completions` with all of the text generated from the Azure OpenAI completion API. In this example, select only the text for simplicity.
-
-```python
-from pyspark.sql.functions import col
-
-completed_df = completion.transform(df).cache()
-display(completed_df.select(
-  col("prompt"), col("error"), col("completions.choices.text").getItem(0).alias("text")))
-```
-
-The following image shows example output with completions in Azure Synapse Analytics Studio. Keep in mind that completions text can vary. Your output might look different.
-
-:::image type="content" source="../media/how-to/synapse-studio-transform-dataframe-output.png" alt-text="Screenshot that shows sample completions in Azure Synapse Analytics Studio." border="false":::
-
-## Explore other usage scenarios
-
-Here are some other use cases for working with Azure OpenAI Service and large datasets.
-
-### Generating Text Embeddings
-
-In addition to completing text, we can also embed text for use in downstream algorithms or vector retrieval architectures. Creating embeddings allows you to search and retrieve documents from large collections and can be used when prompt engineering isn't sufficient for the task. For more information on using [OpenAIEmbedding](https://mmlspark.blob.core.windows.net/docs/0.11.1/pyspark/_modules/synapse/ml/cognitive/openai/OpenAIEmbedding.html), see our [embedding guide](https://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/OpenAI/Quickstart%20-%20OpenAI%20Embedding/).
-
-from synapse.ml.services.openai import OpenAIEmbedding
-
-```python
-embedding = (
-    OpenAIEmbedding()
-    .setSubscriptionKey(key)
-    .setDeploymentName(deployment_name_embeddings)
-    .setCustomServiceName(service_name)
-    .setTextCol("prompt")
-    .setErrorCol("error")
-    .setOutputCol("embeddings")
-)
-
-display(embedding.transform(df))
-```
-
-### Chat Completion
-Models such as ChatGPT and GPT-4 are capable of understanding chats instead of single prompts. The [OpenAIChatCompletion](https://mmlspark.blob.core.windows.net/docs/0.11.1/pyspark/_modules/synapse/ml/cognitive/openai/OpenAIChatCompletion.html) transformer exposes this functionality at scale.
-
-```python
-from synapse.ml.services.openai import OpenAIChatCompletion
-from pyspark.sql import Row
-from pyspark.sql.types import *
-
-
-def make_message(role, content):
-    return Row(role=role, content=content, name=role)
-
-
-chat_df = spark.createDataFrame(
-    [
-        (
-            [
-                make_message(
-                    "system", "You are an AI chatbot with red as your favorite color"
-                ),
-                make_message("user", "Whats your favorite color"),
-            ],
-        ),
-        (
-            [
-                make_message("system", "You are very excited"),
-                make_message("user", "How are you today"),
-            ],
-        ),
-    ]
-).toDF("messages")
-
-chat_completion = (
-    OpenAIChatCompletion()
-    .setSubscriptionKey(key)
-    .setDeploymentName(deployment_name)
-    .setCustomServiceName(service_name)
-    .setMessagesCol("messages")
-    .setErrorCol("error")
-    .setOutputCol("chat_completions")
-)
-
-display(
-    chat_completion.transform(chat_df).select(
-        "messages", "chat_completions.choices.message.content"
-    )
-)
-```
-
-### Improve throughput with request batching from OpenAICompletion
-
-You can use Azure OpenAI Service with large datasets to improve throughput with request batching. In the previous example, you make several requests to the service, one for each prompt. To complete multiple prompts in a single request, you can use batch mode.
-
-In the [OpenAItCompletion](https://mmlspark.blob.core.windows.net/docs/0.11.1/pyspark/_modules/synapse/ml/cognitive/openai/OpenAICompletion.html) object definition, you specify the `"batchPrompt"` value to configure the dataframe to use a **batchPrompt** column. Create the dataframe with a list of prompts for each row.
-
-> [!NOTE]
-> There's currently a limit of 20 prompts in a single request and a limit of 2048 tokens, or approximately 1500 words.
-
-> [!NOTE]
-> Currently, request batching is not supported by the `OpenAIChatCompletion()` transformer.
-
-```python
-batch_df = spark.createDataFrame(
-    [
-        (["The time has come", "Pleased to", "Today stocks", "Here's to"],),
-        (["The only thing", "Ask not what", "Every litter", "I am"],),
-    ]
-).toDF("batchPrompt")
-```
-
-Next, create the `OpenAICompletion` object. If your column is of type `Array[String]`, set the `batchPromptCol` value for the column heading, rather than the `promptCol` value.
-
-```python
-batch_completion = (
-    OpenAICompletion()
-    .setSubscriptionKey(key)
-    .setDeploymentName(deployment_name)
-    .setUrl("https://{}.openai.azure.com/".format(resource_name))
-    .setMaxTokens(200)
-    .setBatchPromptCol("batchPrompt")
-    .setErrorCol("error")
-    .setOutputCol("completions")
-)
-```
-
-In the call to `transform`, one request is made per row. Because there are multiple prompts in a single row, each request is sent with all prompts in that row. The results contain a row for each row in the request.
-
-```python
-completed_batch_df = batch_completion.transform(batch_df).cache()
-display(completed_batch_df)
-```
-
-### Use an automatic mini-batcher
-
-You can use Azure OpenAI Service with large datasets to transpose the data format. If your data is in column format, you can transpose it to row format by using the SynapseML `FixedMiniBatcherTransformer` object.
-
-```python
-from pyspark.sql.types import StringType
-from synapse.ml.stages import FixedMiniBatchTransformer
-from synapse.ml.core.spark import FluentAPI
-
-completed_autobatch_df = (df
- .coalesce(1) # Force a single partition so your little 4-row dataframe makes a batch of size 4 - you can remove this step for large datasets.
- .mlTransform(FixedMiniBatchTransformer(batchSize=4))
- .withColumnRenamed("prompt", "batchPrompt") 
- .mlTransform(batch_completion))
-
-display(completed_autobatch_df)
-```
-
-### Prompt engineering for translation
-
-Azure OpenAI can solve many different natural language tasks through _prompt engineering_. For more information, see [Learn how to generate or manipulate text](completions.md). In this example, you can prompt for language translation:
-
-```python
-translate_df = spark.createDataFrame(
-    [
-        ("Japanese: Ookina hako \nEnglish: Big box \nJapanese: Midori tako\nEnglish:",),
-        ("French: Quelle heure est-il à Montréal? \nEnglish: What time is it in Montreal? \nFrench: Où est le poulet? \nEnglish:",),
-    ]
-).toDF("prompt")
-
-display(completion.transform(translate_df))
-```
-
-### Prompt for question answering
-
-Azure OpenAI also supports prompting the `Text-Davinci-003` model for general-knowledge question answering:
-
-```python
-qa_df = spark.createDataFrame(
-    [
-        (
-            "Q: Where is the Grand Canyon?\nA: The Grand Canyon is in Arizona.\n\nQ: What is the weight of the Burj Khalifa in kilograms?\nA:",
-        )
-    ]
-).toDF("prompt")
-
-display(completion.transform(qa_df))
-```
-
-## Next steps
-
-- Learn how to work with the [GPT-35 Turbo and GPT-4 models](/azure/ai-services/openai/how-to/chatgpt?pivots=programming-language-chat-completions).
-- Learn more about the [Azure OpenAI Service models](../concepts/models.md).
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "SynapseMLとの統合に関するドキュメントの削除"
}
```

### Explanation
このコード変更では、Azure OpenAIサービスとSynapseMLの統合に関するドキュメントが完全に削除されました。この変更により、351行の内容が削除され、関連情報は一切含まれなくなりました。ドキュメントには、Azure OpenAIを使用して大規模なデータセットを処理する方法や、Apache Sparkを通じての具体的な実装手順が含まれていました。

具体的には、以下のような内容が削除されています。

- Azure OpenAIサービスをSynapseMLと連携させて、大規模な言語モデルを分散処理する方法に関するチュートリアル。
- 使用するための前提条件や必要なリソースに関する詳細。
- Pythonを使用した具体的なコード例や使い方の手順。
- Azure Synapse Analyticsまたは他のプラットフォームでのデータフレーム操作についての情報。

このドキュメントの削除は、関連する情報が他の場所に移動されたか、または現在の機能が変更されたことを示している可能性があります。ユーザーは、Azure OpenAIを利用する他のリソースを参照する必要があります。

## articles/ai-services/openai/how-to/on-your-data-configuration.md{#item-4875d3}

<details>
<summary>Diff</summary>
````diff
@@ -1,27 +1,25 @@
 ---
-title: 'Using your data with Azure OpenAI securely'
+title: 'Network and access configuration for Azure OpenAI On Your Data'
 titleSuffix: Azure OpenAI
-description: Use this article to learn about securely using your data for text generation in Azure OpenAI.
+description: Use this article to learn about configuring Azure OpenAI when using your data for text generation.
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
 author: aahill
 ms.author: aahi
-ms.date: 09/24/2024
+ms.date: 12/03/2024
 recommendations: false
 ---
 
-# Securely use Azure OpenAI On Your Data
+# Network and access configuration for Azure OpenAI On Your Data
 
 > [!NOTE]
 > As of June 2024, the application form for the Microsoft managed private endpoint to Azure AI Search is no longer needed.
 >
 > The managed private endpoint will be deleted from the Microsoft managed virtual network at July 2025. If you have already provisioned a managed private endpoint through the application process before June 2024, enable [Azure AI Search trusted service](#enable-trusted-service-1) as early as possible to avoid service disruption. 
 
-Use this article to learn how to use Azure OpenAI On Your Data securely by protecting data and resources with Microsoft Entra ID role-based access control, virtual networks, and private endpoints.
-
-This article is only applicable when using [Azure OpenAI On Your Data with text](/azure/ai-services/openai/concepts/use-your-data). It does not apply to [Azure OpenAI On Your Data with images](/azure/ai-services/openai/concepts/use-your-image-data).
+Use this article to learn how to configure networking and access when using Azure OpenAI On Your Data with Microsoft Entra ID role-based access control, virtual networks, and private endpoints.
 
 ## Data ingestion architecture 
 
@@ -292,7 +290,7 @@ To enable the developers to use these resources to build applications, the admin
 | `Contributor` | Azure AI Search | List API-Keys to list indexes from Azure OpenAI Studio.|
 | `Contributor` | Storage Account | List Account SAS to upload files from Azure OpenAI Studio.|
 | `Contributor` | The resource group or Azure subscription where the developer need to deploy the web app to | Deploy web app to the developer's Azure subscription.|
-| `Role Based Access Control Administrator` | Azure OpenAI | Permission to configure the necessary role assignment on the Azure OpenAI resource. Enables the web app to call Azure Open AI. |
+| `Role Based Access Control Administrator` | Azure OpenAI | Permission to configure the necessary role assignment on the Azure OpenAI resource. Enables the web app to call Azure OpenAI. |
 
 ## Configure gateway and client
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データを使用するためのAzure OpenAI設定に関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIにおけるデータ使用に関する文書のタイトルと内容が更新され、ドキュメントの焦点が「安全な使用」から「ネットワークとアクセスの設定」に移行しました。具体的には、以下の変更が行われています。

- **タイトルの変更**: 元のタイトル「Using your data with Azure OpenAI securely」が「Network and access configuration for Azure OpenAI On Your Data」に変更され、セキュリティからネットワークとアクセスに重点が移されました。
- **説明の更新**: 説明文も変更され、「データを安全に使用する方法」から「データを使用する際のAzure OpenAIの設定方法」に改訂されました。
- **文書の適用範囲の明確化**: 文書の内容がAzure OpenAIを使用する際の設定に特化し、特にMicrosoft Entra IDによる役割ベースのアクセス制御、仮想ネットワーク、プライベートエンドポイントなどについて詳述しています。

また、最終更新日が2024年9月から2024年12月に変更され、新しい情報が反映されることが示唆されています。この変更により、ユーザーはAzure OpenAIのネットワーク設定とアクセス管理に関する現在のガイダンスをより良く理解できるようになります。

## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -29,7 +29,7 @@ You should consider switching from standard deployments to provisioned deploymen
 
 ## Sizing and estimation: provisioned deployments
 
-Determining the right amount of provisioned throughput, or PTUs, you require for your workload is an essential step to optimizing performance and cost. If you are not familiar with the different approaches available to estimate system level throughput, review the system level throughput estimation recommendations in our [performance and latency documentation](./latency.md). This section describes how to use Azure OpenAI capacity calculators to estimate the number of PTUs required to support a given workload.
+Determining the right amount of provisioned throughput, or PTUs, you require for your workload is an essential step to optimizing performance and cost. If you aren't familiar with the different approaches available to estimate system level throughput, review the system level throughput estimation recommendations in our [performance and latency documentation](./latency.md). This section describes how to use Azure OpenAI capacity calculators to estimate the number of PTUs required to support a given workload.
 
 ### Estimate provisioned throughput units and cost
 
@@ -52,7 +52,7 @@ The **Provisioned** option and the capacity planner are only available in certai
 | Version | Version of the model you plan to use, for example 0614 |
 | Peak calls per min | The number of calls per minute that are expected to be sent to the model |
 | Tokens in prompt call | The number of tokens in the prompt for each call to the model. Calls with larger prompts utilize more of the PTU deployment. Currently this calculator assumes a single prompt value so for workloads with wide variance. We recommend benchmarking your deployment on your traffic to determine the most accurate estimate of PTU needed for your deployment. |
-| Tokens in model response | The number of tokens generated from each call to the model. Calls with larger generation sizes will utilize more of the PTU deployment. Currently this calculator assumes a single prompt value so for workloads with wide variance. We recommend benchmarking your deployment on your traffic to determine the most accurate estimate of PTU needed for your deployment. |
+| Tokens in model response | The number of tokens generated from each call to the model. Calls with larger generation sizes utilize more of the PTU deployment. Currently this calculator assumes a single prompt value so for workloads with wide variance. We recommend benchmarking your deployment on your traffic to determine the most accurate estimate of PTU needed for your deployment. |
 
 After you fill in the required details, select **Calculate** button in the output column.
 
@@ -65,35 +65,35 @@ The values in the output column are the estimated value of PTU units required fo
 
 ## Understanding the provisioned throughput purchase model
 
-Azure OpenAI Provisioned and Global Provisioned are purchased on-demand at an hourly basis based on the number of deployed PTUs, with substantial term discount available via the purchase of Azure Reservations.   
+Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned are purchased on-demand at an hourly basis based on the number of deployed PTUs, with substantial term discount available via the purchase of Azure Reservations.   
 
-The hourly model is useful for short-term deployment needs, such as validating new models or acquiring capacity for a hackathon.  However, the discounts provided by the Azure Reservation for Azure OpenAI Provisioned and Global Provisioned are considerable and most customers with consistent long-term usage will find a reserved model to be a better value proposition. 
+The hourly model is useful for short-term deployment needs, such as validating new models or acquiring capacity for a hackathon.  However, the discounts provided by the Azure Reservation for Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned are considerable and most customers with consistent long-term usage will find a reserved model to be a better value proposition. 
 
 > [!NOTE]
-> Azure OpenAI Provisioned customers onboarded prior to the August self-service update use a purchase model called the Commitment model.  These customers can continue to use this older purchase model alongside the Hourly/reservation purchase model.  The Commitment model is not available for new customers.  For details on the Commitment purchase model and options for coexistence and migration, please see the [Azure OpenAI Provisioned August Update](../concepts/provisioned-migration.md).
+> Azure OpenAI Provisioned customers onboarded prior to the August self-service update use a purchase model called the Commitment model.  These customers can continue to use this older purchase model alongside the Hourly/reservation purchase model.  The Commitment model is not available for new customers or new models introduced after August 2024.  For details on the Commitment purchase model and options for coexistence and migration, please see the [Azure OpenAI Provisioned August Update](../concepts/provisioned-migration.md).
 ## Hourly usage
 
-Provisioned and Global Provisioned deployments are charged an hourly rate ($/PTU/hr) on the number of PTUs that have been deployed.  For example, a 300 PTU deployment will be charged the hourly rate times 300.  All Azure OpenAI pricing is available in the Azure Pricing Calculator. 
+Provisioned, Data Zone Provisioned, and Global Provisioned deployments are charged an hourly rate ($/PTU/hr) on the number of PTUs that have been deployed.  For example, a 300 PTU deployment will be charged the hourly rate times 300.  All Azure OpenAI pricing is available in the Azure Pricing Calculator. 
 
 If a deployment exists for a partial hour, it will receive a prorated charge based on the number of minutes it was deployed during the hour.  For example, a deployment that exists for 15 minutes during an hour will receive 1/4th the hourly charge.  
 
 If the deployment size is changed, the costs of the deployment will adjust to match the new number of PTUs.   
 
 :::image type="content" source="../media/provisioned/hourly-billing.png" alt-text="A diagram showing hourly billing." lightbox="../media/provisioned/hourly-billing.png":::
 
-Paying for provisioned and global provisioned deployments on an hourly basis is ideal for short-term deployment scenarios.  For example: Quality and performance benchmarking of new models, or temporarily increasing PTU capacity to cover an event such as a hackathon.  
+Paying for provisioned, data zoned provisioned, and global provisioned deployments on an hourly basis is ideal for short-term deployment scenarios.  For example: Quality and performance benchmarking of new models, or temporarily increasing PTU capacity to cover an event such as a hackathon.  
 
-Customers that require long-term usage of provisioned and global provisioned deployments, however, might pay significantly less per month by purchasing a term discount via an Azure Reservation as discussed in the next section. 
+Customers that require long-term usage of provisioned, data zoned provisioned, and global provisioned deployments, however, might pay significantly less per month by purchasing a term discount via Azure Reservations as discussed in the next section. 
 
 > [!NOTE]
 > It is not recommended to scale production deployments according to incoming traffic and pay for them purely on an hourly basis. There are two reasons for this:
-> * The cost savings achieved by purchasing an Azure Reservation for Azure OpenAI Provisioned are significant, and it will be less expensive in many cases to maintain a deployment sized for full production volume paid for via a reservation than it would be to scale the deployment with incoming traffic.
-> * Having unused provisioned quota (PTUs) does not guarentee that capacity will be available to support increasing the size of the deployment when required. Quota limits the maximum number of PTUs that can be deployed, but it is not a capacity guarantee. Provisioned capacity for each region and modal dynamically changes throughout the day and might not be available when required. As a result, it is recommended to maintain a permanant deployment to cover your traffic needs (paid for via a reservation).
+> * The cost savings achieved by purchasing Azure Reservations for Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned are significant, and it will be less expensive in many cases to maintain a deployment sized for full production volume paid for via a reservation than it would be to scale the deployment with incoming traffic.
+> * Having unused provisioned quota (PTUs) does not guarantee that capacity will be available to support an increase in the size of the deployment when required. Quota limits the maximum number of PTUs that can be deployed, but it is not a capacity guarantee. Provisioned capacity for each region and model dynamically changes throughout the day and might not be available when required. As a result, it is recommended to maintain a permanent deployment to cover your traffic needs (paid for via a reservation).
 > * Charges for deployments on a deleted resource will continue until the resource is purged.  To prevent this, delete a resource’s deployment before deleting the resource.  For more information, see [Recover or purge deleted Azure AI services resources](../../recover-purge-resources.md). 
 
 ## Azure Reservations for Azure OpenAI provisioned deployments
 
-Discounts on top of the hourly usage price can be obtained by purchasing an Azure Reservation for Azure OpenAI Provisioned and Global Provisioned. An Azure Reservation is a term-discounting mechanism shared by many Azure products. For example, Compute and Cosmos DB. For Azure OpenAI Provisioned and Global Provisioned, the reservation provides a discount for committing to payment for fixed number of PTUs for a one-month or one-year period.  
+Discounts on top of the hourly usage price can be obtained by purchasing an Azure Reservation for Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned. An Azure Reservation is a term-discounting mechanism shared by many Azure products. For example, Compute and Cosmos DB. For Azure OpenAI Provisioned, Data Zone Provisioned, and Global Provisioned, the reservation provides a discount in exchange for committing to payment for fixed number of PTUs for a one-month or one-year period.  
 
 * Azure Reservations are purchased via the Azure portal, not the Azure AI Foundry portal Link to Azure reservation portal.
 
@@ -107,11 +107,13 @@ Discounts on top of the hourly usage price can be obtained by purchasing an Azur
 
 * New reservations can be purchased to cover the same scope as existing reservations, to allow for discounting of new provisioned deployments.  The scope of existing reservations can also be updated at any time without penalty, for example to cover a new subscription. 
 
+* Reservations for Global, Data Zone, and Regional deployments aren't interchangeable. You need to purchase a separate reservation for each deployment type. 
+
 * Reservations can be canceled after purchase, but credits are limited.   
 
 * If the size of provisioned deployments within the scope of a reservation exceeds the amount of the reservation, the excess is charged at the hourly rate. For example, if deployments amounting to 250 PTUs exist within the scope of a 200 PTU reservation, 50 PTUs will be charged on an hourly basis until the deployment sizes are reduced to 200 PTUs, or a new reservation is created to cover the remaining 50. 
 
-* Reservations guarantee a discounted price for the selected term.  They do not reserve capacity on the service or guarantee that it will be available when a deployment is created.  It is highly recommended that customers create deployments prior to purchasing a reservation to prevent from over-purchasing a reservation. 
+* Reservations guarantee a discounted price for the selected term.  They don't reserve capacity on the service or guarantee that it will be available when a deployment is created. It's highly recommended that customers create deployments prior to purchasing a reservation to prevent from over-purchasing a reservation. 
 
 > [!IMPORTANT] 
 > * Capacity availability for model deployments is dynamic and changes frequently across regions and models.  To prevent you from purchasing a reservation for more PTUs than you can use, create deployments first, and then purchase the Azure Reservation to cover the PTUs you have deployed.  This best practice will ensure that you can take full advantage of the reservation discount and prevent you from purchasing a term commitment that you cannot use. 
@@ -120,17 +122,20 @@ Discounts on top of the hourly usage price can be obtained by purchasing an Azur
 
 ## Important: sizing Azure OpenAI provisioned reservations
 
-The PTU amounts in reservation purchases are independent of PTUs allocated in quota or used in deployments. It is possible to purchase a reservation for more PTUs than you have in quota, or can deploy for the desired region, model, or version.   Credits for over-purchasing a reservation are limited, and customers must take steps to ensure they maintain their reservation sizes in line with their deployed PTUs.  
+The PTU amounts in reservation purchases are independent of PTUs allocated in quota or used in deployments. It's possible to purchase a reservation for more PTUs than you have in quota, or can deploy for the desired region, model, or version.   Credits for over-purchasing a reservation are limited, and customers must take steps to ensure they maintain their reservation sizes in line with their deployed PTUs.  
  
-The best practice is to always purchase a reservation after deployments have been created.  This prevents purchasing a reservation and then finding out that the required capacity is not available for the desired region or model. 
+The best practice is to always purchase a reservation after deployments have been created.  This prevents purchasing a reservation and then finding out that the required capacity isn't available for the desired region or model. 
  
+
+Reservations for Global, Data Zone, and Regional deployments aren't interchangeable. You need to purchase a separate reservation for each deployment type.
+
 To assist customers with purchasing the correct reservation amounts. The total number of PTUs in a subscription and region that can be covered by a reservation are listed on the Quotas page of Azure AI Foundry. See the message "PTUs Available for reservation." 
 
 :::image type="content" source="../media/provisioned/available-quota.png" alt-text="A screenshot showing available PTU quota." lightbox="../media/provisioned/available-quota.png":::
 
 Managing Azure Reservations 
 
-After a reservation is created, it is a best practice monitor it to ensure it is receiving the usage you are expecting.  This can be done via the Azure Reservation Portal or Azure Monitor.  Details on these topics and others can be found here: 
+After a reservation is created, it is a best practice monitor it to ensure it is receiving the usage you're expecting.  This can be done via the Azure Reservation Portal or Azure Monitor.  Details on these articles and others can be found here: 
 
 * [View Azure reservation utilization](/azure/cost-management-billing/reservations/reservation-utilization) 
 * [View Azure Reservation purchase and refund transactions](/azure/cost-management-billing/reservations/view-purchase-refunds) 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Provisioned Throughput on Azure OpenAIに関する文書の改訂"
}
```

### Explanation
このコードの変更では、Azure OpenAIの「Provisioned Throughput」についての文書が改訂され、全体的に内容が更新されました。具体的には、以下の変更が行われています。

- **セクション内容の追加**: 新たに「Data Zone Provisioned」という用語が登場し、同様に「Provisioned」の説明が拡張されました。これにより、料金モデルや使用状況が具体的に概要されます。
- **更新された説明と文言の調整**: 一部の文が明確化され、言葉遣いが調整されました。特に、PTU（Provisioned Throughput Unit）に関連する記述が強化され、ユーザーが必要とする情報の理解を助けるようになっています。
- **注意事項の強化**: 注記の中で、旧モデルからの移行に関する詳細と、予約購入の際の注意点が明確にされました。特に、モデルの非互換性に関する情報が強調されており、予約購入後に展開されたPTU数に見合った購入が推奨されています。
- **ベストプラクティスの強調**: 予約作成の後にデプロイを確認し、必要なPTU数に応じて適切に調整することの重要性が再確認されています。

全体として、この改訂はAzure OpenAIの使用に関心を持つユーザーにとって有益で出所になり、具体的かつ分かりやすいガイダンスを提供しています。

## articles/ai-services/openai/how-to/weights-and-biases-integration.md{#item-8ae868}

<details>
<summary>Diff</summary>
````diff
@@ -21,80 +21,80 @@ Weights & Biases (W&B) is a powerful AI developer platform that enables machine
 ## Prerequisites
 
 - An Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). The resource should be in a [region that supports fine-tuning](../concepts/models.md#fine-tuning-models).
-- All users on your team who need to fine-tune models should have **Cognitive Services OpenAI Contributor** access assigned for the new Azure OpenAI resource.
+- Ensure all team members who need to fine-tune models have **Cognitive Services OpenAI Contributor** access assigned for the new Azure OpenAI resource.
 - A [Weights & Biases](https://wandb.ai) account and API key.
 - [Azure Key Vault](https://portal.azure.com/#create/Microsoft.KeyVault). For more information on creating a key vault, see the [Azure Key Vault quickstart](/azure/key-vault/general/quick-create-portal).
 
 ## Enable System Managed Identity
 
-First you will need to enable [System Managed Identity](/entra/identity/managed-identities-azure-resources/overview) for your Azure OpenAI resource.
+First, enable [System Managed Identity](/entra/identity/managed-identities-azure-resources/overview) for your Azure OpenAI resource.
 
-:::image type="content" source="../media/how-to/weights-and-biases/system-managed.png" alt-text="Screenshot of the system managed identity enabled user experience." lightbox="../media/how-to/weights-and-biases/system-managed.png":::
+:::image type="content" source="../media/how-to/weights-and-biases/system-managed.png" alt-text="Screenshot of the system managed identity interface." lightbox="../media/how-to/weights-and-biases/system-managed.png":::
 
 ## Retrieve Weights & Biases API key
 
-Sign in to [https://wandb.ai](https://wandb.ai) and go to [User Settings](https://wandb.ai/settings).
+Sign in to [https://wandb.ai](https://wandb.ai) and go to the [User Settings](https://wandb.ai/settings).
 
-Under **API Keys** select **Reveal** to access your key and copy to the clipboard.
+Under **API Keys**, select **Reveal** to access your key and copy it to the clipboard.
 
 :::image type="content" source="../media/how-to/weights-and-biases/reveal-key.png" alt-text="Screenshot of API keys section of User Settings user experience." lightbox="../media/how-to/weights-and-biases/reveal-key.png":::
 
-If you would like to create a new key use [https://wandb.ai/authorize](https://wandb.ai/authorize), and copy the key to add to your integration configuration later.
+If you would like to create a new key, use [https://wandb.ai/authorize](https://wandb.ai/authorize), and copy the key to add to your integration configuration later.
 
 ## Configure Azure Key Vault
 
-In order to securely, send data from Azure OpenAI to your Weights & Biases projects you'll need to use [Azure Key Vault](/azure/key-vault/general/overview).
+To securely send data from Azure OpenAI to your Weights & Biases projects, you'll need to use [Azure Key Vault](/azure/key-vault/general/overview).
 
 ### Add your Weights & Biases API key as a Secret to your Azure Key Vault
 
 1. Navigate to the Azure Key Vault you are planning to use.
-2. To read\write secrets to your Azure Key Vault, you must explicitly assign access.
-3. Go to Settings > Access configuration, under Permission model we recommend you select Azure role-based access control if this isn't already selected. Learn more about [Azure role-based access control](/azure/role-based-access-control/overview?WT.mc_id=Portal-Microsoft_Azure_KeyVault).
+2. To read and write secrets to your Azure Key Vault, you must explicitly assign access.
+3. Go to **Settings** > **Access** configuration. Under **Permission** model, we recommend you select Azure role-based access control if this isn't already selected. Learn more about [Azure role-based access control](/azure/role-based-access-control/overview?WT.mc_id=Portal-Microsoft_Azure_KeyVault).
 
     :::image type="content" source="../media/how-to/weights-and-biases/role-based-access-control.png" alt-text="Screenshot of key vault access configuration user interface." lightbox="../media/how-to/weights-and-biases/role-based-access-control.png":::
 
 ### Assign Key Vault Secrets Officer role
 
-Now that you set your permission model to Azure role-based access control, you can give yourself the **Key Vault Secrets Officer** role.
+Now that you have set your permission model to Azure role-based access control, you can give yourself the **Key Vault Secrets Officer** role.
 
 1. Go to **Access control (IAM)** and then **Add role assignment**
 
     :::image type="content" source="../media/how-to/weights-and-biases/access-control.png" alt-text="Screenshot of the access control add role assignment user experience." lightbox="../media/how-to/weights-and-biases/access-control.png":::
 
-2. Choose **Key Vault Secrets Officer** and add your account as a member and select **review & assign**.
+2. Choose **Key Vault Secrets Officer**, add your account as a member, and select **review & assign**.
 
     :::image type="content" source="../media/how-to/weights-and-biases/key-vault-secret-officer.png" alt-text="Screenshot of the key vault secret officer role assignment." lightbox="../media/how-to/weights-and-biases/key-vault-secret-officer.png":::
 
 ### Create secrets
 
-1. From within your key vault resource under **Objects** and select **Secrets** > **Generate/Import**.
+1. From within your key vault resource under **Objects**, select **Secrets** > **Generate/Import**.
 
     :::image type="content" source="../media/how-to/weights-and-biases/secrets.png" alt-text="Screenshot of the key vault secrets user interface." lightbox="../media/how-to/weights-and-biases/secrets.png":::
 
-2. Provide a name to your secret and save the generated API key from Weights & Biases to the **secret value**.
+2. Provide a name for your secret and save the generated Weights & Biases API key to the **secret value**.
 
     :::image type="content" source="../media/how-to/weights-and-biases/create-secret.png" alt-text="Screenshot of the key vault secrets creation user interface." lightbox="../media/how-to/weights-and-biases/create-secret.png":::
 
-3. Make sure to capture the secret name and key vault url. Key vault URL can be retrieved from **Overview** section of your key-vault.
+3. Make sure to capture the secret name and key vault URL. The key vault URL can be retrieved from **Overview** section of your key vault.
 
 ### Give your Key Vault permission on your Azure OpenAI account
 
-If you used vault access policy earlier to read/write secrets to your Azure Key Vault, you should use that again. Otherwise, continue to use Azure role-based access control. **We recommend Azure role-based access control, though if it does not work for you, please try Vault Access policy.**
+If you used a Vault Access policy earlier to read and write secrets to your Azure Key Vault, you should use that again. Otherwise, continue to use Azure role-based access control. **We recommend Azure role-based access control. However, if it does not work for you, please try Vault Access policy.**
 
 Give your Azure OpenAI resource the **Key Vault Secrets Officer** role.
 
 :::image type="content" source="../media/how-to/weights-and-biases/assign.png" alt-text="Screenshot of the assign managed identity user interface." lightbox="../media/how-to/weights-and-biases/assign.png":::
 
 ## Link Weights & Biases with Azure OpenAI
 
-1. Navigate to [AI Foundry portal](https://ai.azure.com) and select your Azure OpenAI fine-tuning resource.
+1. Navigate to the [AI Foundry portal](https://ai.azure.com) and select your Azure OpenAI fine-tuning resource.
 
     :::image type="content" source="../media/how-to/weights-and-biases/manage-integrations.png" alt-text="Screenshot of the manage integrations button." lightbox="../media/how-to/weights-and-biases/manage-integrations.png":::
 
-2. Add your key vault URL and secret > then select **Update**.
+2. Add your key vault URL and secret. Then, select **Update**.
 
     :::image type="content" source="../media/how-to/weights-and-biases/integration.png" alt-text="Screenshot of the manage integrations for Weights and Biases user experience." lightbox="../media/how-to/weights-and-biases/integration.png":::
 
-3. Now when you create new fine-tuning jobs you'll have the option to log data from the job to your Weights & Biases account.
+3. Now, when you create new fine-tuning jobs, you'll have the option to log data from the job to your Weights & Biases account.
 
     :::image type="content" source="../media/how-to/weights-and-biases/dashboards.png" alt-text="Screenshot of the weights and biases dashboards." lightbox="../media/how-to/weights-and-biases/dashboards.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Weights & Biases統合に関する文書の更新"
}
```

### Explanation
このコードの変更では、Weights & Biasesとの統合に関するAzure OpenAIの文書が改訂され、いくつかの表現や手順が明確化されました。主な変更点は以下の通りです。

- **手順の簡素化**: 各ステップでの説明が簡潔になり、文がより明確かつスムーズに読めるよう調整されています。具体的には、アクセス設定やAPIキー取得の手順が少し簡略化されており、ユーザーが理解しやすくなっています。
- **重要な役割の明確化**: Azure Key Vaultに関連する役割（Key Vault Secrets Officer）の設定手順がより明確に表現されており、必要な設定が分かりやすく示されています。
- **用語の整合性**: 「秘密」という用語が一貫性を持って使われるようになり、特に新しい秘密の作成に関する手順での用語が統一されました。
- **視覚的要素の強化**: スクリーンショットのキャプションが改善され、ユーザーが画面の内容を理解する助けとなるよう、説明がより具体的に記述されています。

このような改訂により、Weights & Biasesとの統合手順がより流暢でわかりやすくなり、ユーザーにとって有益な情報を提供する文書へと改善されています。

## articles/ai-services/openai/includes/on-your-data-authentication.md{#item-43fc01}

<details>
<summary>Diff</summary>
````diff
@@ -9,12 +9,12 @@ ms.date: 03/27/2024
 
 ## Data connection
 
-You need to select how you want to authenticate the connection from Azure OpenAI, Azure AI Search, and Azure blob storage. You can choose a *System assigned managed identity* or an *API key*. By selecting *API key* as the authentication type, the system will automatically populate the API key for you to connect with your Azure AI Search, Azure OpenAI, and Azure Blob Storage resources. By selecting *System assigned managed identity*, the authentication will be based on the [role assignment](../how-to/use-your-data-securely.md#role-assignments) you have. *System assigned managed identity* is selected by default for security. 
+You need to select how you want to authenticate the connection from Azure OpenAI, Azure AI Search, and Azure blob storage. You can choose a *System assigned managed identity* or an *API key*. By selecting *API key* as the authentication type, the system will automatically populate the API key for you to connect with your Azure AI Search, Azure OpenAI, and Azure Blob Storage resources. By selecting *System assigned managed identity*, the authentication will be based on the [role assignment](../how-to/on-your-data-configuration.md#role-assignments) you have. *System assigned managed identity* is selected by default for security. 
 
 
 :::image type="content" source="../media/use-your-data/data-connection-authentication.png" alt-text="A screenshot showing the managed identity option in Azure OpenAI Studio." lightbox="../media/use-your-data/data-connection-authentication.png":::
 
-Once you select the **next** button, it will automatically validate your setup to use the selected authentication method. If you encounter an error, see the [role assignments article](../how-to/use-your-data-securely.md#role-assignments) to update your setup.
+Once you select the **next** button, it will automatically validate your setup to use the selected authentication method. If you encounter an error, see the [role assignments article](../how-to/on-your-data-configuration.md#role-assignments) to update your setup.
 
 Once you have fixed the setup, select **next** again to validate and proceed. API users can also [configure authentication](../references/azure-search.md#api-key-authentication-options) with assigned managed identity and API keys.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ接続の認証方法に関する文書の更新"
}
```

### Explanation
このコードの変更では、Azure OpenAI、Azure AI Search、Azure Blob Storageへのデータ接続に関する文書が改訂され、一部の参照が更新されました。主な変更点は以下の通りです。

- **参照リンクの更新**: 認証方法の説明内での「role assignment」へのリンクが、旧参照から新しい参照（`on-your-data-configuration.md`）に変更されました。これにより、ユーザーが最新の設定情報にアクセスしやすくなっています。
- **表現の調整**: 認証メソッドの選択に関する説明が、一貫性を持った明確な表現に整えられました。特に、APIキーとシステム割り当てマネージドアイデンティティの選択に関する文章が、より流暢で理解しやすい形に改善されています。

全体として、この改訂はユーザーが実際にデータ接続を認証する際の手順をより明確に示し、必要な情報に容易にアクセスできるようにすることを目的としています。

## articles/ai-services/openai/index.yml{#item-0adb87}

<details>
<summary>Diff</summary>
````diff
@@ -102,8 +102,8 @@ landingContent:
                url:  ./how-to/gpt-with-vision.md
              - text: Provisioned Throughput Units (PTU) 
                url: ./how-to/provisioned-throughput-onboarding.md
-             - text: Securing Azure OpenAI on your data
-               url: ./how-to/use-your-data-securely.md
+             - text: Network and access configuration for Azure OpenAI on your data
+               url: ./how-to/on-your-data-configuration.md
              - text: Resource creation & deployment
                url: ./how-to/create-resource.md 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIのデータにおけるネットワークとアクセス設定に関するリンクの更新"
}
```

### Explanation
この変更では、Azure OpenAIに関連する文書のリンクが更新されました。具体的には、以下の点が改訂されています：

- **リンクのテキストとURLの変更**: 「Securing Azure OpenAI on your data」という項目が「Network and access configuration for Azure OpenAI on your data」に変更され、そのリンク先も旧ページ（`use-your-data-securely.md`）から新ページ（`on-your-data-configuration.md`）に置き換えられました。これは、ネットワークおよびアクセス設定に関する最新情報を提供するための更新です。

この変更により、ユーザーは最新の情報や手順に基づいてAzure OpenAIのデータ管理を行いやすくなります。文書が常に最新の内容を反映することは、ユーザーにとって重要なポイントです。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ The following sections provide you with a quick guide to the default quotas and
 
 | Limit Name | Limit Value |
 |--|--|
-| OpenAI resources per region per Azure subscription | 30 |
+| Azure OpenAI resources per region per Azure subscription | 30 |
 | Default DALL-E 2 quota limits | 2 concurrent requests |
 | Default DALL-E 3 quota limits| 2 capacity units (6 requests per minute)|
 | Default Whisper quota limits | 3 requests per minute |
@@ -44,8 +44,8 @@ The following sections provide you with a quick guide to the default quotas and
 | Max number of `/chat/completions` functions | 128 |
 | Max number of `/chat completions` tools | 128 |
 | Maximum number of Provisioned throughput units per deployment | 100,000 |
-| Max files per Assistant/thread | 10,000 when using the API or AI Foundry. 20 when using Azure OpenAI Studio.|
-| Max file size for Assistants & fine-tuning | 512 MB |
+| Max files per Assistant/thread | 10,000 when using the API or Azure AI Foundry portal. In Azure OpenAI Studio the limit was 20.|
+| Max file size for Assistants & fine-tuning | 512 MB<br/><br/>200 MB via Azure AI Foundry portal |
 | Max size for all uploaded files for Assistants |100 GB |
 | Assistants token limit | 2,000,000 token limit |
 | GPT-4o max images per request (# of images in the messages array/conversation history) | 50 |
@@ -181,7 +181,7 @@ To minimize issues related to rate limits, it's a good idea to use the following
 
 ### How to request increases to the default quotas and limits
 
-Quota increase requests can be submitted from the [Quotas](./how-to/quota.md) page of Azure AI Foundry. Due to high demand, quota increase requests are being accepted and will be filled in the order they're received. Priority is given to customers who generate traffic that consumes the existing quota allocation, and your request might be denied if this condition isn't met.
+Quota increase requests can be submitted from the [Quotas](./how-to/quota.md) page in the Azure AI Foundry portal. Due to high demand, quota increase requests are being accepted and will be filled in the order they're received. Priority is given to customers who generate traffic that consumes the existing quota allocation, and your request might be denied if this condition isn't met.
 
 For other rate limits, [submit a service request](../cognitive-services-support-options.md?context=/azure/ai-services/openai/context/context).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIのクォータおよび制限に関する文書の改善"
}
```

### Explanation
このコードの変更は、Azure OpenAIに関するクォータおよび制限に関する文書の内容を改善するためのものです。主な変更点は以下の通りです：

- **リソース名の修正**: リミット名が「OpenAI resources per region per Azure subscription」から「Azure OpenAI resources per region per Azure subscription」に変更され、より具体的にリソースを表すようになりました。
  
- **ファイル数制限の明確化**: 「Max files per Assistant/thread」に関する文が明確にされ、特にAzure OpenAI Studioにおける制限が詳細に説明されています。この変更により、ユーザーが異なるプラットフォームでのファイル制限を理解しやすくなります。

- **ファイルサイズの明確化**: 「Max file size for Assistants & fine-tuning」で、Azure AI Foundryポータルを介した場合のファイルサイズ制限が追加され、ユーザーにとって具体的な情報が提供されています。

- **クォータ増加リクエストの手順の修正**: クォータ増加リクエストの提出に関する説明が改善され、Azure AI Foundryポータル内の正確なページへの言及がされています。

これらの変更は、ユーザーがAzure OpenAIのリソース制限を理解し、必要に応じて適切に対応できるようにすることを目的としています。整体として、文書の透明性と利用者への情報提供が向上しています。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -138,8 +138,6 @@ items:
       href: ./how-to/structured-outputs.md
     - name: Work with code
       href: ./how-to/work-with-code.md
-    - name: Use with large datasets
-      href: ./how-to/integrate-synapseml.md
     - name: Deploy and use web apps
       href: ./how-to/use-web-app.md
     - name: Legacy
@@ -175,8 +173,8 @@ items:
       - name: Text data
         href: ./concepts/use-your-data.md
         displayName: use your data, on your data
-      - name: Use Azure OpenAI On Your Data securely
-        href: ./how-to/use-your-data-securely.md
+      - name: Network and access configuration
+        href: ./how-to/on-your-data-configuration.md
       - name: Deploy and use web apps
         href: ./how-to/use-web-app.md
       - name: Use the Azure Developer CLI
@@ -201,8 +199,6 @@ items:
         href: encrypt-data-at-rest.md
       - name: Managed identity
         href: ./how-to/managed-identity.md
-      - name: Use Azure OpenAI on your data securely
-        href: ./how-to/use-your-data-securely.md
   - name: Service management
     items:
       - name: Resource creation & model deployment
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIトピックの目次の更新"
}
```

### Explanation
この変更は、Azure OpenAIに関連する文書の目次（TOC）を更新するためのものです。主な改訂点は以下の通りです：

- **項目の削除**: 「Use with large datasets」という項目が目次から削除されました。この変更により、ユーザーは関連情報や手順に容易にアクセスできる他の項目に焦点を当てることができます。

- **項目名の変更**: 「Use Azure OpenAI On Your Data securely」が「Network and access configuration」に改名され、より明確で具体的な内容を示しています。また、リンク先も更新され、新しい情報を参照できるようになっています。

- **重複項目の削除**: 「Use Azure OpenAI on your data securely」の項目が重複していたため、1つが削除されました。これにより、目次が簡潔になり、ユーザーにとってのナビゲーションが向上します。

これらの変更は、文書の整合性を保ちながら、ユーザーが関連する情報にスムーズにアクセスできるように設計されています。目次の更新を通じて、Azure OpenAIに関するコンテンツの利用が一層効率的になります。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -555,7 +555,7 @@ You can now use Azure OpenAI On Your Data in the following Azure region:
 ### Azure OpenAI On Your Data
 
 - Full VPN and private endpoint support for Azure OpenAI On Your Data, including security support for: storage accounts, Azure OpenAI resources, and Azure AI Search service resources.   
-- New article for using [Azure OpenAI On Your Data securely](./how-to/use-your-data-securely.md) by protecting data with virtual networks and private endpoints.
+- New article for using [Azure OpenAI On Your Data configuration](./how-to/on-your-data-configuration.md) by protecting data with virtual networks and private endpoints.
 
 ### GPT-4 Turbo with Vision now available
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIの新機能に関する文書の更新"
}
```

### Explanation
この変更は、「Azure OpenAIの新機能」に関する文書の内容を更新するためのものです。具体的な変更点は以下の通りです：

- **新しい記事の参照先変更**: 「Azure OpenAI On Your Data securely」に関する記事のリンクが「Azure OpenAI On Your Data configuration」に変更されました。この変更により、データ保護の方法に関する情報が、より適切な記事へ誘導されるようになります。リンク先の記事は、仮想ネットワークやプライベートエンドポイントを使ったデータの保護について詳しく解説しています。

- **文言の調整**: 新記事のタイトルが更新されることで、利用者が情報の内容をより直感的に理解できるようになっています。

この変更は、Azure OpenAIに関する最新情報をユーザーに的確に伝えるためのもので、文書の精度と有用性を高める目的があります。利用者が必要な情報を迅速に見つけやすくすることを目指しています。


