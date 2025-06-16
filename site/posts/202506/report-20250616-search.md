---
date: '2025-06-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0496181...MicrosoftDocs:b7d8d3a
summary: 新機能として、エージェント型検索のセットアップガイドが追加され、Azure AI Foundryへの移行に伴う大幅な更新が行われました。モデルは`gpt-4.1-mini`に変更され、ドキュメントの日付も最新の状態に保たれました。これにより、ユーザーは古くなった情報を使用せず、最新の技術とガイドラインに基づいてサービスを展開できるようになります。また、役割ベースのアクセス管理の詳細な設定手順も含まれています。古いOpenAIリソースからAzure
  AI Foundryリソースへの移行に伴い、古いリソースを利用するための手順は削除されました。全体として、これらの変更は、Azure AI Searchを活用するユーザーにとって、クラウドサービスにおける最新情報を基にした利便性を向上させることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0496181...MicrosoftDocs:b7d8d3a){target="_blank"}

# Highlights

- 新機能として、エージェント型検索のセットアップガイドが追加されました。
- Azure AI Foundryへの移行に伴う大幅な更新。
- 使用するモデルが`gpt-4.1-mini`へ変更。
- 日付の更新により、ドキュメントの最新性を維持。

## New features

- エージェント型検索のセットアップガイドが新たに追加。
- 役割ベースのアクセス管理の詳細な設定手順が含まれている。

## Breaking changes

- OpenAIリソースからAzure AI Foundryリソースへの移行が示され、古いリソースを使用する手順が削除。

## Other updates

- ドキュメントの日付が更新され、最新の状態に。
- 手順やコードスニペットが、より効率的で明確なものに改善。
- Visual Studio Codeでの設定方法がシンプルになり、HTTPリクエストのサンプルが追加。

# Insights

今回の変更は、Azure AI Searchを活用するユーザーに向けて、最新の技術とガイドラインを提供することを目的としたものです。まず、ドキュメントの日付更新は、一見地味ですが、ユーザーが古くなった情報を使用しないようにするための基本的なアップデートです。常に最新の情報に基づくことは特にクラウドサービスでは重要です。

新たに追加されたエージェント型検索のセットアップガイドは、Azure AI Foundry環境での作業を前提にした詳細な手順を提供しています。これにより、クラウド環境への理解が深まり、容易にサービスを展開できるようになっています。特に、役割ベースのアクセス管理などは、セキュリティ管理を簡便にする重要な機能です。

さらに、モデルの更新（`gpt-4o-mini`から`gpt-4.1-mini`への移行）は性能面での向上を期待でき、新しいアーキテクチャやパラメータをテストする良い機会を提供します。この種のアップデートは、AIサービスの向上に直結するため、開発効率の改善につながります。

このような一連のアップデートは、Azure AI ecosystemの一部として有機的に進化させる意図が見え、技術的な選択肢を広げ、エージェント型検索の導入を円滑に進めるための下地を整えるものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-python.md](#item-efee6a) | minor update | エージェント検索のクイックスタートガイドの更新 | modified | 58 | 91 | 149 | 
| [agentic-retrieval-rest.md](#item-3df373) | minor update | エージェント型検索のRESTクイックスタートガイドの更新 | modified | 17 | 84 | 101 | 
| [agentic-retrieval-setup.md](#item-e5e297) | new feature | エージェント型検索のセットアップガイドの追加 | added | 82 | 0 | 82 | 
| [search-get-started-agentic-retrieval.md](#item-4a40f4) | minor update | エージェント型検索クイックスタートガイドの日付更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 05/30/2025
+ms.date: 6/15/2025
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -21,101 +21,38 @@ This quickstart is based on the [Quickstart-Agentic-Retrieval](https://github.co
 
 + An [Azure AI Search service](../../search-create-service-portal.md) on the Basic tier or higher with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
 
-+ An [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource).
++ An [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects). You get an Azure AI Foundry resource (that's needed for model deployments) when you create an Azure AI Foundry project.
 
 + [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter package](https://pypi.org/project/jupyter/).
 
-## Deploy models
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-To run agentic retrieval, you must deploy the following models to your Azure OpenAI resource:
+[!INCLUDE [Setup](./agentic-retrieval-setup.md)]
 
-+ An LLM for query planning.
-
-+ An LLM for answer generation.
-
-+ (Optional) An embedding model for vector queries.
-
-Agentic retrieval [supports several models](../../search-agentic-retrieval-how-to-create.md#supported-models), but this quickstart assumes `gpt-4o-mini` for both LLMs and `text-embedding-3-large` for the embedding model.
-
-To deploy the Azure OpenAI models:
-
-1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and select your Azure OpenAI resource.
-
-1. From the left pane, select **Model catalog**.
-
-1. Select **gpt-4o-mini**, and then select **Use this model**.
-
-1. Specify a deployment name. To simplify your code, we recommend **gpt-4o-mini**.
-
-1. Accept the defaults.
-
-1. Select **Deploy**.
-
-1. Repeat the previous steps for **text-embedding-3-large**.
-
-## Configure role-based access
-
-Azure AI Search needs access to your Azure OpenAI models. For this task, you can use API keys or Microsoft Entra ID with role assignments. Keys are easier to start with, but roles are more secure. This quickstart assumes roles.
-
-To configure the recommended role-based access:
-
-1. Sign in to the [Azure portal](https://portal.azure.com/).
-
-1. [Enable role-based access](../../search-security-enable-roles.md) on your Azure AI Search service.
-
-1. [Create a system-assigned managed identity](../../search-howto-managed-identities-data-sources.md#create-a-system-managed-identity) on your Azure AI Search service.
-
-1. On your Azure AI Search service, [assign the following roles](../../search-security-rbac.md#how-to-assign-roles-in-the-azure-portal) to yourself.
-
-    + **Search Service Contributor**
-
-    + **Search Index Data Contributor**
-
-    + **Search Index Data Reader**
-
-1. On your Azure OpenAI resource, assign **Cognitive Services User** to the managed identity of your search service.
-
-## Get endpoints
-
-In your code, you specify the following endpoints to establish connections with Azure AI Search and Azure OpenAI. These steps assume that you configured role-based access in the previous section.
-
-To obtain your service endpoints:
-
-1. Sign in to the [Azure portal](https://portal.azure.com/).
-
-1. On your Azure AI Search service:
-
-    1. From the left pane, select **Overview**.
-
-    1. Copy the URL, which should be similar to `https://my-service.search.windows.net`.
-
-1. On your Azure OpenAI resource:
+## Connect from your local system
 
-    1. From the left pane, select **Resource Management** > **Keys and Endpoint**.
+You configured role-based access to interact with Azure AI Search and Azure OpenAI. 
 
-    1. Copy the URL, which should be similar to `https://my-resource.openai.azure.com`.
+To connect from your local system:
 
-## Connect from your local system
+1. Open a new terminal in Visual Studio Code and change to the directory where you want to save your files.
+1. Run the following Azure CLI command and sign in with your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Azure AI Foundry project.
 
-You configured role-based access to interact with Azure AI Search and Azure OpenAI. From the command line, use the Azure CLI to sign in to the same subscription and tenant for both services. For more information, see [Quickstart: Connect without keys](../../search-get-started-rbac.md).
-
-```azurecli
-az account show
+    ```azurecli
+    az login
+    ```
 
-az account set --subscription <PUT YOUR SUBSCRIPTION ID HERE>
-    
-az login --tenant <PUT YOUR TENANT ID HERE>
-```
+For more information, see [Quickstart: Connect without keys](../../search-get-started-rbac.md).
 
 ## Install packages and load connections
 
 Before you run any code, install Python packages and define credentials, endpoints, and deployment details for connections to Azure AI Search and Azure OpenAI. These values are used in subsequent operations.
 
 To install the packages and load the connections:
 
-1. In Visual Studio Code, create a `.ipynb` file.
+1. In Visual Studio Code, create a `.ipynb` file. For example, you can name the file `quickstart-agentic-retrieval.ipynb`.
 
-1. Install the following packages.
+1. In the first code cell, paste the following code to install the required packages. 
 
     ```Python
     ! pip install azure-search-documents==11.6.0b12 --quiet
@@ -126,7 +63,9 @@ To install the packages and load the connections:
     ! pip install requests --quiet
     ```
 
-1. In another code cell, paste the following import statements and variables.
+    You can run this cell by selecting the **Run Cell** button or pressing `Shift+Enter`.
+
+1. Add another code cell and paste the following import statements and variables.
 
     ```Python
     from azure.identity import DefaultAzureCredential, get_bearer_token_provider
@@ -135,26 +74,28 @@ To install the packages and load the connections:
     endpoint = "PUT YOUR SEARCH SERVICE ENDPOINT HERE"
     credential = DefaultAzureCredential()
     token_provider = get_bearer_token_provider(credential, "https://search.azure.com/.default")
-    azure_openai_endpoint = "PUT YOUR AZURE OPENAI ENDPOINT HERE"
-    azure_openai_gpt_deployment = "gpt-4o-mini"
-    azure_openai_gpt_model = "gpt-4o-mini"
+    azure_openai_endpoint = "PUT YOUR AZURE AI FOUNDRY ENDPOINT HERE"
+    azure_openai_gpt_deployment = "gpt-4.1-mini"
+    azure_openai_gpt_model = "gpt-4.1-mini"
     azure_openai_api_version = "2025-03-01-preview"
     azure_openai_embedding_deployment = "text-embedding-3-large"
     azure_openai_embedding_model = "text-embedding-3-large"
     index_name = "earth_at_night"
     agent_name = "earth-search-agent"
-    answer_model = "gpt-4o-mini"
+    answer_model = "gpt-4.1-mini"
     api_version = "2025-05-01-Preview"
     ```
 
-1. Replace `endpoint` and `azure_openai_endpoint` with the values you obtained in [Get endpoints](#get-endpoints).
+1. Set `endpoint` to your Azure AI Search endpoint, which looks like `https://<your-search-service-name>.search.windows.net.` Set `azure_openai_endpoint` to your Azure AI Foundry endpoint, which looks like `https://<your-foundry-resource-name>.openai.azure.com.` You obtained both values in the [Get endpoints](#get-endpoints) section. 
 
 1. To verify the variables, run the code cell.
 
 ## Create a search index
 
 In Azure AI Search, an index is a structured collection of data. The following code defines an index named `earth_at_night`, which you specified using the `index_name` variable in the previous section.
 
+Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+
 ```Python
 from azure.search.documents.indexes.models import SearchIndex, SearchField, VectorSearch, VectorSearchProfile, HnswAlgorithmConfiguration, AzureOpenAIVectorizer, AzureOpenAIVectorizerParameters, SemanticSearch, SemanticConfiguration, SemanticPrioritizedFields, SemanticField
 from azure.search.documents.indexes import SearchIndexClient
@@ -215,6 +156,8 @@ The index schema contains fields for document identification and page content, e
 
 Currently, the `earth_at_night` index is empty. Run the following code to populate the index with JSON documents from NASA's Earth at Night e-book. As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
 
+Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+
 ```Python
 from azure.search.documents import SearchIndexingBufferedSender
 import requests
@@ -230,10 +173,12 @@ print(f"Documents uploaded to index '{index_name}'")
 
 ## Create a knowledge agent
 
-To connect Azure AI Search to your `gpt-4o-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. The following code defines a knowledge agent named `earth-search-agent`, which you specified using the `agent_name` variable in a previous section.
+To connect Azure AI Search to your `gpt-4.1-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. The following code defines a knowledge agent named `earth-search-agent`, which you specified using the `agent_name` variable in a previous section.
 
 To ensure relevant and semantically meaningful responses, `default_reranker_threshold` is set to exclude responses with a reranker score of `2.5` or lower.
 
+Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+
 ```Python
 from azure.search.documents.indexes.models import KnowledgeAgent, KnowledgeAgentAzureOpenAIModel, KnowledgeAgentTargetIndex, KnowledgeAgentRequestLimits, AzureOpenAIVectorizerParameters
 
@@ -266,6 +211,8 @@ The next step is to define the knowledge agent instructions and conversation con
 
 For now, create the following assistant message, which instructs `earth-search-agent` to answer questions about the Earth at night, cite sources using their `ref_id`, and respond with "I don't know" when answers are unavailable.
 
+Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+
 ```Python
 instructions = """
 An Q&A agent that can answer questions about the Earth at night.
@@ -287,6 +234,8 @@ You're ready to initiate the agentic retrieval pipeline. The input for this pipe
 
 The following code sends a two-part user query to `earth-search-agent`, which deconstructs the query into subqueries, runs the subqueries against both text fields and vector embeddings in the `earth_at_night` index, and ranks and merges the results. The response is then appended to the `messages` array.
 
+Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+
 ```Python
 from azure.search.documents.agent import KnowledgeAgentRetrievalClient
 from azure.search.documents.agent.models import KnowledgeAgentRetrievalRequest, KnowledgeAgentMessage, KnowledgeAgentMessageTextContent, KnowledgeAgentIndexParams
@@ -315,7 +264,9 @@ messages.append({
 
 ### Review the response, activity, and results
 
-To output the response, activity, and results of the retrieval pipeline, run the following code.
+Now you want to display the response, activity, and results of the retrieval pipeline.
+
+Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
 
 ```Python
 import textwrap
@@ -335,7 +286,7 @@ The output should be similar to the following example, where:
 
 + `Response` provides a text string of the most relevant documents (or chunks) in the search index based on the user query. As shown later in this quickstart, you can pass this string to an LLM for answer generation.
 
-+ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4o-mini` deployment and the tokens used for query planning and execution.
++ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for query planning and execution.
 
 + `Results` lists the documents that contributed to the response, each one identified by their `doc_key`.
 
@@ -391,7 +342,9 @@ Results
 
 ## Create the Azure OpenAI client
 
-To extend the retrieval pipeline from answer *extraction* to answer *generation*, set up the Azure OpenAI client to interact with your `gpt-4o-mini` deployment, which you specified using the `answer_model` variable in a previous section.
+To extend the retrieval pipeline from answer *extraction* to answer *generation*, set up the Azure OpenAI client to interact with your `gpt-4.1-mini` deployment, which you specified using the `answer_model` variable in a previous section.
+
+Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
 
 ```Python
 from openai import AzureOpenAI
@@ -407,7 +360,9 @@ client = AzureOpenAI(
 
 ### Use the Responses API to generate an answer
 
-You can now use the Responses API to generate a detailed answer based on the indexed documents. The following code sends the `messages` array, which contains the conversation history, to your `gpt-4o-mini` deployment.
+You can now use the Responses API to generate a detailed answer based on the indexed documents. The following code sends the `messages` array, which contains the conversation history, to your `gpt-4.1-mini` deployment.
+
+Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
 
 ```Python
 response = client.responses.create(
@@ -419,7 +374,7 @@ wrapped = textwrap.fill(response.output_text, width=100)
 print(wrapped)
 ```
 
-The output should be similar to the following example, which uses the reasoning capabilities of `gpt-4o-mini` to provide contextually relevant answers.
+The output should be similar to the following example, which uses the reasoning capabilities of `gpt-4.1-mini` to provide contextually relevant answers.
 
 ```
 Suburban belts often exhibit larger December brightening than urban cores primarily because of the type of development and light distribution in those areas. Suburbs tend to have more uniform and expansive lighting, making them more visible in nighttime satellite images. In contrast, urban cores, although having higher absolute light levels, often contain dense building clusters that can cause light to be obscured or concentrated in smaller areas, leading to less visible brightening when viewed from space.  Regarding the visibility of the Phoenix nighttime street grid from space, it is attributed to the city's grid layout and the intensity of its street lighting. The grid pattern of the streets and the significant development around them create a stark contrast against less developed areas. Conversely, large stretches of interstate in the Midwest may remain dimmer due to fewer densely populated structures and less intensive street lighting, resulting in less illumination overall.  For more detailed insights, you can refer to the sources: [0] and [1].
@@ -429,6 +384,8 @@ Suburban belts often exhibit larger December brightening than urban cores primar
 
 Alternatively, you can use the Chat Completions API for answer generation.
 
+Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+
 ```Python
 response = client.chat.completions.create(
     model=answer_model,
@@ -449,6 +406,8 @@ Suburban belts tend to display larger December brightening than urban cores, des
 
 Continue the conversation by sending another user query to `earth-search-agent`. The following code reruns the retrieval pipeline, fetching relevant content from the `earth_at_night` index and appending the response to the `messages` array. However, unlike before, you can now use the Azure OpenAI client to generate an answer based on the retrieved content.
 
+Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+
 ```Python
 messages.append({
     "role": "user",
@@ -469,7 +428,9 @@ messages.append({
 
 ### Review the new response, activity, and results
 
-To output the latest response, activity, and results of the retrieval pipeline, run the following code.
+Now you want to display the response, activity, and results of the retrieval pipeline.
+
+Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
 
 ```Python
 import textwrap
@@ -489,6 +450,8 @@ print(json.dumps([r.as_dict() for r in retrieval_result.references], indent=2))
 
 Now that you've sent multiple user queries, use the Responses API to generate an answer based on the indexed documents and conversation history, which is captured in the `messages` array.
 
+Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+
 ```Python
 response = client.responses.create(
     model=answer_model,
@@ -513,6 +476,8 @@ In the Azure portal, you can find and manage resources by selecting **All resour
 
 ### Delete the knowledge agent
 
+Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+
 ```Python
 index_client = SearchIndexClient(endpoint=endpoint, credential=credential)
 index_client.delete_agent(agent_name)
@@ -521,6 +486,8 @@ print(f"Knowledge agent '{agent_name}' deleted successfully")
 
 ### Delete the search index
 
+Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+
 ```Python
 index_client = SearchIndexClient(endpoint=endpoint, credential=credential)
 index_client.delete_index(index_name)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索のクイックスタートガイドの更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchに関連するエージェント検索のクイックスタートガイドにおけるいくつかの更新を反映しています。主な変更点は以下の通りです。

1. 日付の更新 - ドキュメントの更新日が2025年5月30日から2025年6月15日に変更されました。
2. コンテンツの追加 - Azure AI Foundryプロジェクトの作成に関する情報が追加され、OpenAIリソースからAzure AI Foundryリソースへの移行が強調されました。
3. コードスニペットの変更 - 使用するモデルが`gpt-4o-mini`から`gpt-4.1-mini`に更新され、関連するコードチュートリアルも改善されました。
4. 説明の明確化 - 新しい手順が追加され、ユーザーが適切に設定や接続を行えるように支援する内容が強化されました。
5. セクションの整理 - 一連のコードセルの追加とともに、新しい操作のステップが具体的に示されています。

この変更は、特にAzure AI Foundryを通じたエージェントの展開やモデルの設定に対する指導をより明確にし、利用者が情報を取得しやすくすることを目的としています。

## articles/search/includes/quickstarts/agentic-retrieval-rest.md{#item-3df373}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 05/30/2025
+ms.date: 6/15/2025
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -22,94 +22,26 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 + An [Azure AI Search service](../../search-create-service-portal.md) on the Basic tier or higher with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
 
-+ An [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource).
++ An [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects). You get an Azure AI Foundry resource (that's needed for model deployments) when you create an Azure AI Foundry project.
 
 + [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
-## Deploy models
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-To run agentic retrieval, you must deploy the following models to your Azure OpenAI resource:
-
-+ An LLM for query planning.
-
-+ An LLM for answer generation.
-
-+ (Optional) An embedding model for vector queries.
-
-Agentic retrieval [supports several models](../../search-agentic-retrieval-how-to-create.md#supported-models), but this quickstart assumes `gpt-4o-mini` for the query-planning LLM and `text-embedding-3-large` for the embedding model. To use the answer-generating LLM, see the Python version of this quickstart.
-
-To deploy the Azure OpenAI models:
-
-1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and select your Azure OpenAI resource.
-
-1. From the left pane, select **Model catalog**.
-
-1. Select **gpt-4o-mini**, and then select **Use this model**.
-
-1. Specify a deployment name. To simplify your code, we recommend **gpt-4o-mini**.
-
-1. Accept the defaults.
-
-1. Select **Deploy**.
-
-1. Repeat the previous steps for **text-embedding-3-large**.
-
-## Configure role-based access
-
-Azure AI Search needs access to your Azure OpenAI models. For this task, you can use API keys or Microsoft Entra ID with role assignments. Keys are easier to start with, but roles are more secure. This quickstart assumes roles.
-
-To configure the recommended role-based access:
-
-1. Sign in to the [Azure portal](https://portal.azure.com/).
-
-1. [Enable role-based access](../../search-security-enable-roles.md) on your Azure AI Search service.
-
-1. [Create a system-assigned managed identity](../../search-howto-managed-identities-data-sources.md#create-a-system-managed-identity) on your Azure AI Search service.
-
-1. On your Azure AI Search service, [assign the following roles](../../search-security-rbac.md#how-to-assign-roles-in-the-azure-portal) to yourself.
-
-    + **Search Service Contributor**
-
-    + **Search Index Data Contributor**
-
-    + **Search Index Data Reader**
-
-1. On your Azure OpenAI resource, assign **Cognitive Services User** to the managed identity of your search service.
-
-## Get endpoints
-
-In your code, you specify the following endpoints to establish connections with Azure AI Search and Azure OpenAI. These steps assume that you configured role-based access in the previous section.
-
-To obtain your service endpoints:
-
-1. Sign in to the [Azure portal](https://portal.azure.com/).
-
-1. On your Azure AI Search service:
-
-    1. From the left pane, select **Overview**.
-
-    1. Copy the URL, which should be similar to `https://my-service.search.windows.net`.
-
-1. On your Azure OpenAI resource:
-
-    1. From the left pane, select **Resource Management** > **Keys and Endpoint**.
-
-    1. Copy the URL, which should be similar to `https://my-resource.openai.azure.com`.
+[!INCLUDE [Setup](./agentic-retrieval-setup.md)]
 
 ## Connect from your local system
 
 You configured role-based access to interact with Azure AI Search and Azure OpenAI. From the command line, use the Azure CLI to sign in to the same subscription and tenant for both services. For more information, see [Quickstart: Connect without keys](../../search-get-started-rbac.md).
 
 To connect from your local system:
 
-1. Run the following commands in sequence.
+1. Open a new terminal in Visual Studio Code and change to the directory where you want to save your files.
 
-    ```azurecli
-    az account show
+1. Run the following command and sign in with your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Azure AI Foundry project.
 
-    az account set --subscription <PUT YOUR SUBSCRIPTION ID HERE>
-    
-    az login --tenant <PUT YOUR TENANT ID HERE>
+    ```azurecli
+    az login
     ```
 
 1. To obtain your Microsoft Entra token, run the following command. You specify this value in the next section.
@@ -124,26 +56,27 @@ Before you send any requests, define credentials, endpoints, and deployment deta
 
 To load the connections:
 
-1. In Visual Studio Code, paste the following placeholders into a `.rest` or `.http` file.
+1. In Visual Studio Code create a `.rest` or `.http` file. For example, you can name the file `agentic-retrieval.rest`.
+1. Paste these placeholders into the new file:
 
     ```HTTP
     @baseUrl = PUT-YOUR-SEARCH-SERVICE-URL-HERE
     @token = PUT-YOUR-MICROSOFT-ENTRA-TOKEN-HERE
-    @aoaiBaseUrl = PUT-YOUR-AOAI-URL-HERE
-    @aoaiGptModel = gpt-4o-mini
-    @aoaiGptDeployment = gpt-4o-mini
+    @aoaiBaseUrl = PUT-YOUR-AI-FOUNDRY-URL-HERE
+    @aoaiGptModel = gpt-4.1-mini
+    @aoaiGptDeployment = gpt-4.1-mini
     @aoaiEmbeddingModel = text-embedding-3-large
     @aoaiEmbeddingDeployment = text-embedding-3-large
     @index-name = earth_at_night
     @agent-name = earth-search-agent
     @api-version = 2025-05-01-Preview
     ```
 
-1. Replace `@baseUrl` and `@aoaiBaseUrl` with the values you obtained in [Get endpoints](#get-endpoints).
+1. Set `@baseUrl` to your Azure AI Search endpoint, which looks like `https://<your-search-service-name>.search.windows.net.` Set `@aoaiBaseUrl` to your Azure AI Foundry endpoint, which looks like `https://<your-foundry-resource-name>.openai.azure.com.` You obtained both values in the [Get endpoints](#get-endpoints) section. 
 
 1. Replace `@token` with the Microsoft Entra token you obtained in [Connect from your local system](#connect-from-your-local-system).
 
-1. To verify the variables, send the following request.
+1. In the same file, enter and send the following HTTP request to verify that you can connect to Azure AI Search. The request lists existing indexes in your search service.
 
     ```HTTP
     ### List existing indexes by name
@@ -280,7 +213,7 @@ POST {{baseUrl}}/indexes/{{index-name}}/docs/index?api-version={{api-version}}
 
 ## Create a knowledge agent
 
-To connect Azure AI Search to your `gpt-4o-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. Use [Create Knowledge Agents](/rest/api/searchservice/knowledge-agents/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true) to define an agent named `earth-search-agent`, which you specified using the `@agent-name` variable in a previous section.
+To connect Azure AI Search to your `gpt-4.1-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. Use [Create Knowledge Agents](/rest/api/searchservice/knowledge-agents/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true) to define an agent named `earth-search-agent`, which you specified using the `@agent-name` variable in a previous section.
 
 To ensure relevant and semantically meaningful responses, `defaultRerankerThreshold` is set to exclude responses with a reranker score of `2.5` or lower.
 
@@ -346,7 +279,7 @@ The output should be similar to the following JSON, where:
 
 + `response` provides a text string of the most relevant documents (or chunks) in the search index based on the user query. You can pass this string to an LLM for use as grounding data in answer generation.
 
-+ `activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4o-mini` deployment and the tokens used for query planning and execution.
++ `activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for query planning and execution.
 
 + `references` lists the documents that contributed to the response, each one identified by their `docKey`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント型検索のRESTクイックスタートガイドの更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchに関連するエージェント型検索のRESTクイックスタートガイドにいくつかの重要な更新を含んでいます。以下が主な変更点です。

1. 日付の更新 - ドキュメントの日付が2025年5月30日から2025年6月15日に変更されました。
2. コンテンツの追加 - Azure AI Foundryプロジェクトに関する情報が追加され、OpenAIリソースからの移行が明確に示されています。また、必要なサービスやツールが補足されています。
3. 使用するモデルの変更 - `gpt-4o-mini`から新しいモデル`gpt-4.1-mini`に更新され、関連するコード例や手順もそれに基づいて修正されています。
4. 手順の簡素化 - 接続に関する手順が簡略化され、Visual Studio Codeでの設定方法が改善されました。特に、HTTPリクエストのサンプルが具体的に示されています。
5. 役割ベースのアクセス設定 - 役割ベースのアクセス管理に関する情報が集約され、ユーザーが簡単に設定できるように整理されています。

これらの変更により、ユーザーは新しい機能や設定についての理解を深めることができ、よりスムーズに実装を行うことができるようになります。

## articles/search/includes/quickstarts/agentic-retrieval-setup.md{#item-e5e297}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,82 @@
+---
+manager: nitinme
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 6/15/2025
+---
+
+## Configure role-based access
+
+You can use search service API keys or Microsoft Entra ID with role assignments. Keys are easier to start with, but roles are more secure. This quickstart assumes roles.
+
+To configure the recommended role-based access:
+
+1. Sign in to the [Azure portal](https://portal.azure.com/).
+
+1. [Enable role-based access](../../search-security-enable-roles.md) on your Azure AI Search service.
+
+1. On your Azure AI Search service, [assign the following roles](../../search-security-rbac.md#how-to-assign-roles-in-the-azure-portal) to yourself.
+
+    + **Search Service Contributor**
+
+    + **Search Index Data Contributor**
+
+    + **Search Index Data Reader**
+
+For agentic retrieval, Azure AI Search also needs access to your Azure OpenAI Foundry resource. 
+
+1. [Create a system-assigned managed identity](../../search-howto-managed-identities-data-sources.md#create-a-system-managed-identity) on your Azure AI Search service. Here's how to do it using the Azure CLI:
+
+   ```azurecli
+   az search service update --name YOUR-SEARCH-SERVICE-NAME --resource-group YOUR-RESOURCE-GROUP-NAME --identity-type SystemAssigned
+   ```
+   
+    If you already have a managed identity, you can skip this step.
+
+1. On your Azure AI Foundry resource, assign **Cognitive Services User** to the managed identity that you created for your search service. 
+
+## Deploy models
+
+To use agentic retrieval, you must deploy [one of the supported Azure OpenAI models](../../search-agentic-retrieval-how-to-create.md#supported-models) to your Azure AI Foundry resource:
+
++ A chat model for query planning and answer generation. We use `gpt-4.1-mini` in this quickstart. Optionally, you can use a different model for query planning and another for answer generation, but this quickstart uses the same model for simplicity.
+
++ An embedding model for vector queries. We use `text-embedding-3-large` in this quickstart, but you can use any embedding model that supports the `text-embedding` task.
+
+To deploy the Azure OpenAI models:
+
+1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and select your Azure AI Foundry resource.
+
+1. From the left pane, select **Model catalog**.
+
+1. Select **gpt-4.1-mini**, and then select **Use this model**.
+
+1. Specify a deployment name. To simplify your code, we recommend **gpt-4.1-mini**.
+
+1. Leave the default settings.
+
+1. Select **Deploy**.
+
+1. Repeat the previous steps, but this time deploy the **text-embedding-3-large** embedding model.
+
+## Get endpoints
+
+In your code, you specify the following endpoints to establish connections with you Azure AI Search service and Azure AI Foundry resource. These steps assume that you [configured role-based access as described previously](#configure-role-based-access). 
+
+To obtain your service endpoints:
+
+1. Sign in to the [Azure portal](https://portal.azure.com/).
+
+1. On your Azure AI Search service:
+
+    1. From the left pane, select **Overview**.
+
+    1. Copy the URL, which should be similar to `https://my-service.search.windows.net`. 
+
+1. On your Azure AI Foundry resource:
+
+    1. From the left pane, select **Resource Management** > **Keys and Endpoint**. 
+
+    1. Select the **OpenAI** tab and copy the URL that looks similar to `https://my-resource.openai.azure.com`.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "エージェント型検索のセットアップガイドの追加"
}
```

### Explanation
このコードの変更は、Azure AI Searchにおけるエージェント型検索のセットアップに関する新しいガイドを追加しました。このガイドには、以下の主要な内容が含まれています。

1. **役割ベースのアクセス管理の設定** - Azure AI Searchサービスにおける役割ベースのアクセス管理の設定方法が示されています。具体的には、システム割り当ての管理アイデンティティの作成や必要な役割の割り当てについて説明されています。

2. **モデルのデプロイ方法** - エージェント型検索を使用するために必要なAzure OpenAIモデルのデプロイ手順が詳細に記載されています。特に、`gpt-4.1-mini`や`text-embedding-3-large`といったモデルが使用されます。

3. **エンドポイントの取得** - コード内でAzure AI SearchサービスとAzure AI Foundryリソースの接続を確立するために必要なエンドポイントの取得方法が説明されています。この手順には、AzureポータルでのサインインやエンドポイントのURLのコピーが含まれます。

全体として、この新しいドキュメントはユーザーに対してエージェント型検索のセットアップを円滑に行うための具体的な手順を提供しており、さらに理解しやすく実用的な内容となっています。

## articles/search/search-get-started-agentic-retrieval.md{#item-4a40f4}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 05/29/2025
+ms.date: 6/15/2025
 zone_pivot_groups: search-get-started-agentic-retrieval
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント型検索クイックスタートガイドの日付更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchに関するエージェント型検索のクイックスタートガイドの日付を更新したものです。具体的には、以前の日付である2025年5月29日から2025年6月15日へと修正されています。このような日付の変更は、ドキュメントの最新性や信頼性を維持するために重要です。この更新により、ユーザーはより正確な情報に基づいて作業を進めることができます。


