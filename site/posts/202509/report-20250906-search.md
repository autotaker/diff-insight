---
date: '2025-09-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:de1cf56...MicrosoftDocs:13753f1
summary: 主な変更点として、エージェントリトリーバルに関するクイックスタート文書に新しい情報が追加され、タイトルの修正が行われました。特に、REST APIのバージョンに関する注意事項が更新され、サポートされていない機能についての説明が加わりました。Pythonクイックスタートが大幅に更新され、新しい機能やベストプラクティスが導入されています。他の言語に関しても小規模な修正がなされました。この変更は、ユーザーが最適な開発選択をするのを助けるため、REST
  APIのバージョンによる機能の違いを明示しています。また、ユーザーにとって具体的な実装を行いやすくし、最新技術の理解を助けることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:de1cf56...MicrosoftDocs:13753f1){target="_blank"}

<format>
# Highlights

上記の差分における主な変更点として、エージェントリトリーバルに関するクイックスタート文書の新しい情報追加とタイトルの修正が行われました。特に、REST APIバージョンの注意事項が更新され、特定のバージョンがサポートしていない機能についての注意が明記されています。Pythonクイックスタートは大幅に更新され、最新機能やベストプラクティスが導入されています。その他の言語（C#, Java, JavaScript, TypeScript）に関連するドキュメントにも小規模な修正が加えられました。

## New features

- Pythonクイックスタートでは、Azure AI Foundryを用いた最新のエージェントリトリーバルの説明が追加されました。
- REST APIを介したエージェントリトリーバルの説明が、より具体的にAzure OpenAIの利用を強調しています。

## Breaking changes

- 2025-05-01-previewバージョンのREST APIでは、特定のエージェントリトリーバル機能がサポートされないことが明記されており、代替のバージョンの使用が推奨されています。

## Other updates

- 複数の言語のクイックスタートタイトルがより明確な表現に改められました。
- Azure AI Searchのサンプルドキュメントには、エージェントリトリーバル機能とその実装方法に焦点を当てた詳細が追加されています。

# Insights

この文書の変更は、エージェントリトリーバルの機能とその実装方法をユーザーに詳しく説明することを目的としています。特に、使用するREST APIのバージョンにより機能のサポートが異なることを明確に示すことで、ユーザーが最適な開発選択をするのを助けます。また、Pythonでの説明が大幅に更新されていることから、最新技術やベストプラクティスの採用に力を入れていることが伺えます。ユーザーが技術的背景を持たない場合でも、ドキュメントを頼りに具体的な実装を行うことを意図しています。

加えて、各サンプルの説明文の修正を通じて、ユーザーに対してより明確な目的と達成方法を提供し、Azure AI Searchの最新機能を効果的に活用できるように訴求しています。ユーザーはこれにより、柔軟なクエリ計画や回答生成を可能とする最新の技術をより理解しやすくなっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-csharp.md](#item-f93ed3) | minor update | エージェントリトリーバルに関するC#クイックスタートの更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-java.md](#item-4e2c55) | minor update | エージェントリトリーバルに関するJavaクイックスタートの更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-javascript.md](#item-715283) | minor update | エージェントリトリーバルに関するJavaScriptクイックスタートの更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-python.md](#item-efee6a) | minor update | エージェントリトリーバルに関するPythonクイックスタートの大幅な更新 | modified | 227 | 249 | 476 | 
| [agentic-retrieval-rest.md](#item-3df373) | minor update | エージェントリトリーバルに関するRESTクイックスタートの更新 | modified | 9 | 7 | 16 | 
| [agentic-retrieval-typescript.md](#item-e6370b) | minor update | エージェントリトリーバルに関するTypeScriptクイックスタートの更新 | modified | 1 | 1 | 2 | 
| [search-get-started-rbac-python.md](#item-de7760) | minor update | PythonによるRBACを使用した検索クイックスタートの更新 | modified | 1 | 1 | 2 | 
| [search-get-started-rbac-rest.md](#item-fd8ef4) | minor update | RESTを使用したRBACに関する検索クイックスタートの更新 | modified | 1 | 1 | 2 | 
| [samples-dotnet.md](#item-12f3fa) | minor update | Azure AI Searchのエージェントリトリーバルに関するクイックスタートの内容更新 | modified | 1 | 1 | 2 | 
| [samples-python.md](#item-d2bf09) | minor update | Pythonサンプルのエージェントリトリーバルに関するクイックスタートの内容更新 | modified | 1 | 1 | 2 | 
| [samples-rest.md](#item-198ebc) | minor update | RESTサンプルのエージェントリトリーバルに関するクイックスタートの内容更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/includes/quickstarts/agentic-retrieval-csharp.md{#item-f93ed3}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 To get started with a Jupyter notebook instead, see the [Azure-Samples/azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) repository on GitHub.
 
 > [!TIP]
-> The C# version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST version of this quickstart.
+> The C# version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST or Python version.
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するC#クイックスタートの更新"
}
```

### Explanation
この更新は、C#クイックスタートのドキュメントにおける小規模な修正を反映しています。具体的には、REST APIのバージョンに関する注意事項が更新され、2025-05-01-previewバージョンが知識ソースやその他のエージェントリトリーバル機能をサポートしていないことを明記しています。変更後の文では、機能を使用したい場合に、RESTまたはPythonバージョンを参照するように指示されています。この修正は、ユーザーに対してより正確な情報を提供することを目的としています。

## articles/search/includes/quickstarts/agentic-retrieval-java.md{#item-4e2c55}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-c
 Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
 > [!TIP]
-> The Java version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST version of this quickstart.
+> The Java version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST or Python version.
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するJavaクイックスタートの更新"
}
```

### Explanation
この変更は、Javaクイックスタートのドキュメントにおいて、小規模な修正を行ったものです。具体的には、使用されているREST APIのバージョンについての注意書きが更新され、2025-05-01-previewバージョンが知識ソースや他のエージェントリトリーバル機能をサポートしていないことが強調されています。修正後の文では、これらの機能を利用するにはRESTまたはPythonバージョンを参照するように誘導しています。この更新は、ユーザーに対してより明確で正確な情報を提供することを目的としています。

## articles/search/includes/quickstarts/agentic-retrieval-javascript.md{#item-715283}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-c
 Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
 > [!TIP]
-> The JavaScript version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST version of this quickstart.
+> The JavaScript version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST or Python version.
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するJavaScriptクイックスタートの更新"
}
```

### Explanation
この変更は、JavaScriptクイックスタートのドキュメントに対する小規模な修正を示しています。具体的には、使用中のREST APIバージョンについての説明が改訂され、2025-05-01-previewバージョンが知識ソースやその他のエージェントリトリーバル機能をサポートしていないことが明示されています。修正後の文では、これらの機能を利用するためにRESTまたはPythonバージョンを参照するように案内しています。この更新は、ユーザーに対してより正確でわかりやすい情報を提供することを目的としています。

## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -4,105 +4,108 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 08/28/2025
+ms.date: 09/05/2025
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
 
-In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-concept.md) to create a conversational search experience powered by large language models (LLMs) and your proprietary data. Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries in parallel, and extracts grounding data from documents indexed in Azure AI Search. The output is intended for integration with agentic and custom chat solutions.
+In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-concept.md) to create a conversational search experience powered by documents indexed in Azure AI Search and large language models (LLMs) from Azure OpenAI in Azure AI Foundry Models.
 
-Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
+A *knowledge agent* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the agent outputs raw content from your sources, but this quickstart uses the answer synthesis modality for natural-language answer generation.
 
-This quickstart is based on the [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval) Jupyter notebook on GitHub.
+Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
 > [!TIP]
-> The Python version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST version of this quickstart.
+> Want to get started right away? See the [azure-search-python-samples](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval) repository on GitHub.
 
 ## Prerequisites
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
 + An [Azure AI Search service](../../search-create-service-portal.md) on the Basic tier or higher with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
 
-+ An [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects). You get an Azure AI Foundry resource (that you need for model deployments) when you create an Azure AI Foundry project.
-
-+ [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter package](https://pypi.org/project/jupyter/).
++ An [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects) and Azure AI Foundry resource. When you create a project, the resource is automatically created.
 
 + The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
++ [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter package](https://pypi.org/project/jupyter/).
+
 [!INCLUDE [Setup](./agentic-retrieval-setup.md)]
 
 ## Connect from your local system
 
-You configured role-based access to interact with Azure AI Search and Azure OpenAI. 
+You configured role-based access to interact with Azure AI Search and Azure OpenAI in Azure AI Foundry. Use the Azure CLI to sign in to the same subscription and tenant for both resources. For more information, see [Quickstart: Connect without keys](../../search-get-started-rbac.md).
 
 To connect from your local system:
 
-1. Open a new terminal in Visual Studio Code and change to the directory where you want to save your files.
-1. Run the following Azure CLI command and sign in with your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Azure AI Foundry project.
+1. In Visual Studio Code, open the folder where you want to save your files.
+
+1. Select **Terminal** > **New Terminal**.
+
+1. Run the following command to sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Azure AI Foundry project.
 
     ```azurecli
     az login
     ```
 
-For more information, see [Quickstart: Connect without keys](../../search-get-started-rbac.md).
-
 ## Install packages and load connections
 
-Before you run any code, install Python packages and define credentials, endpoints, and deployment details for connections to Azure AI Search and Azure OpenAI. These values are used in subsequent operations.
+Before you run any code, install Python packages and define endpoints, credentials, and deployment details for connections to Azure AI Search and Azure OpenAI in Azure AI Foundry. These values are used in the following sections.
 
 To install the packages and load the connections:
 
-1. In Visual Studio Code, create a `.ipynb` file. For example, you can name the file `quickstart-agentic-retrieval.ipynb`.
+1. In the same folder in Visual Studio Code, create a file named `quickstart-agentic-retrieval.ipynb`.
 
-1. In the first code cell, paste the following code to install the required packages. 
+1. Add a code cell, and then paste the following `pip install` commands.
 
-    ```Python
-    ! pip install azure-search-documents==11.6.0b12 --quiet
+    ```python
+    ! pip install azure-search-documents==11.7.0b1 --quiet
     ! pip install azure-identity --quiet
     ! pip install openai --quiet
     ! pip install aiohttp --quiet
     ! pip install ipykernel --quiet
     ! pip install requests --quiet
     ```
 
-    You can run this cell by selecting the **Run Cell** button or pressing `Shift+Enter`.
+1. Select **Execute Cell** to install the packages.
 
-1. Add another code cell and paste the following import statements and variables.
+1. Add another code cell, and then paste the following import statements and variables.
 
-    ```Python
+    ```python
     from azure.identity import DefaultAzureCredential, get_bearer_token_provider
     import os
 
-    endpoint = "PUT YOUR SEARCH SERVICE ENDPOINT HERE"
+    search_endpoint = "PUT-YOUR-SEARCH-SERVICE-URL-HERE"
     credential = DefaultAzureCredential()
     token_provider = get_bearer_token_provider(credential, "https://search.azure.com/.default")
-    azure_openai_endpoint = "PUT YOUR AZURE AI FOUNDRY ENDPOINT HERE"
-    azure_openai_gpt_deployment = "gpt-4.1-mini"
-    azure_openai_gpt_model = "gpt-4.1-mini"
-    azure_openai_api_version = "2025-03-01-preview"
-    azure_openai_embedding_deployment = "text-embedding-3-large"
-    azure_openai_embedding_model = "text-embedding-3-large"
-    index_name = "earth_at_night"
-    agent_name = "earth-search-agent"
-    answer_model = "gpt-4.1-mini"
-    api_version = "2025-05-01-Preview"
+    aoai_endpoint = "PUT-YOUR-AOAI-FOUNDRY-URL-HERE"
+    aoai_embedding_model = "text-embedding-3-large"
+    aoai_embedding_deployment = "text-embedding-3-large"
+    aoai_gpt_model = "gpt-4.1-mini"
+    aoai_gpt_deployment = "gpt-4.1-mini"
+    index_name = "earth-at-night"
+    knowledge_source_name = "earth-knowledge-source"
+    knowledge_agent_name = "earth-knowledge-agent"
+    search_api_version = "2025-08-01-preview"
     ```
 
-1. Set `endpoint` to your Azure AI Search endpoint, which looks like `https://<your-search-service-name>.search.windows.net.` Set `azure_openai_endpoint` to your Azure AI Foundry endpoint, which looks like `https://<your-foundry-resource-name>.openai.azure.com.` You obtained both values in the [Get endpoints](#get-endpoints) section. 
+1. Set `search_endpoint` and `aoai_endpoint` to the values you obtained in [Get endpoints](#get-endpoints).
 
-1. To verify the variables, run the code cell.
+1. Select **Execute Cell** to load the variables.
 
 ## Create a search index
 
-In Azure AI Search, an index is a structured collection of data. The following code defines an index named `earth_at_night`, which you specified using the `index_name` variable in the previous section.
+In Azure AI Search, an index is a structured collection of data. Add and run a code cell with the following code to define an index named `earth-at-night`, which you previously specified using the `index_name` variable.
 
-Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+The index schema contains fields for document identification and page content, embeddings, and numbers. The schema also includes configurations for semantic ranking and vector search, which uses your `text-embedding-3-large` deployment to vectorize text and match documents based on semantic similarity.
 
-```Python
+```python
 from azure.search.documents.indexes.models import SearchIndex, SearchField, VectorSearch, VectorSearchProfile, HnswAlgorithmConfiguration, AzureOpenAIVectorizer, AzureOpenAIVectorizerParameters, SemanticSearch, SemanticConfiguration, SemanticPrioritizedFields, SemanticField
 from azure.search.documents.indexes import SearchIndexClient
+from openai import AzureOpenAI
+from azure.identity import get_bearer_token_provider
 
+azure_openai_token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")
 index = SearchIndex(
     name=index_name,
     fields=[
@@ -118,9 +121,9 @@ index = SearchIndex(
             AzureOpenAIVectorizer(
                 vectorizer_name="azure_openai_text_3_large",
                 parameters=AzureOpenAIVectorizerParameters(
-                    resource_url=azure_openai_endpoint,
-                    deployment_name=azure_openai_embedding_deployment,
-                    model_name=azure_openai_embedding_model
+                    resource_url=aoai_endpoint,
+                    deployment_name=aoai_embedding_deployment,
+                    model_name=aoai_embedding_model
                 )
             )
         ]
@@ -140,351 +143,326 @@ index = SearchIndex(
     )
 )
 
-index_client = SearchIndexClient(endpoint=endpoint, credential=credential)
+index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
 index_client.create_or_update_index(index)
-print(f"Index '{index_name}' created or updated successfully")
+print(f"Index '{index_name}' created or updated successfully.")
 ```
 
-The index schema contains fields for document identification and page content, embeddings, and numbers. It also includes configurations for semantic ranking and vector queries, which use the `text-embedding-3-large` model you previously deployed.
-
 ## Upload documents to the index
 
-Currently, the `earth_at_night` index is empty. Run the following code to populate the index with JSON documents from [NASA's Earth at Night e-book](https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json). As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
-
-Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+Currently, the `earth-at-night` index is empty. Add and run a code cell with the following code to populate the index with JSON documents from [NASA's Earth at Night e-book](https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json). As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
 
-```Python
-from azure.search.documents import SearchIndexingBufferedSender
+```python
 import requests
+from azure.search.documents import SearchIndexingBufferedSender
 
 url = "https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json"
 documents = requests.get(url).json()
 
-with SearchIndexingBufferedSender(endpoint=endpoint, index_name=index_name, credential=credential) as client:
+with SearchIndexingBufferedSender(endpoint=search_endpoint, index_name=index_name, credential=credential) as client:
     client.upload_documents(documents=documents)
 
-print(f"Documents uploaded to index '{index_name}'")
+print(f"Documents uploaded to index '{index_name}' successfully.")
+```
+
+## Create a knowledge source
+
+A knowledge source is a reusable reference to your source data. Add and run a code cell with the following code to define a knowledge source named `earth-knowledge-source` that targets the `earth-at-night` index.
+
+`source_data_select` specifies which index fields are accessible for retrieval and citations. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+
+```python
+from azure.search.documents.indexes.models import SearchIndexKnowledgeSource, SearchIndexKnowledgeSourceParameters
+from azure.search.documents.indexes import SearchIndexClient
+
+ks = SearchIndexKnowledgeSource(
+    name=knowledge_source_name,
+    description="Knowledge source for Earth at night data",
+    search_index_parameters=SearchIndexKnowledgeSourceParameters(
+        search_index_name=index_name,
+        source_data_select="id,page_chunk,page_number",
+    ),
+)
+
+index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
+index_client.create_or_update_knowledge_source(knowledge_source=ks, api_version=search_api_version)
+print(f"Knowledge source '{knowledge_source_name}' created or updated successfully.")
 ```
 
 ## Create a knowledge agent
 
-To connect Azure AI Search to your `gpt-4.1-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. The following code defines a knowledge agent named `earth-search-agent`, which you specified using the `agent_name` variable in a previous section.
+To target `earth-knowledge-source` and your `gpt-4.1-mini` deployment at query time, you need a knowledge agent. Add and run a code cell with the following code to define a knowledge agent named `earth-knowledge-agent`, which you previously specified using the `knowledge_agent_name` variable.
 
-To ensure relevant and semantically meaningful responses, `default_reranker_threshold` is set to exclude responses with a reranker score of `2.5` or lower.
+`reranker_threshold` ensures semantic relevance by excluding responses with a reranker score of `2.5` or lower. Meanwhile, `modality` is set to `ANSWER_SYNTHESIS`, enabling natural-language answers that cite the retrieved documents.
 
-Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+```python
+from azure.search.documents.indexes.models import KnowledgeAgent, KnowledgeAgentAzureOpenAIModel, KnowledgeSourceReference, AzureOpenAIVectorizerParameters, KnowledgeAgentOutputConfiguration, KnowledgeAgentOutputConfigurationModality
+from azure.search.documents.indexes import SearchIndexClient
 
-```Python
-from azure.search.documents.indexes.models import KnowledgeAgent, KnowledgeAgentAzureOpenAIModel, KnowledgeAgentTargetIndex, KnowledgeAgentRequestLimits, AzureOpenAIVectorizerParameters
+aoai_params = AzureOpenAIVectorizerParameters(
+    resource_url=aoai_endpoint,
+    deployment_name=aoai_gpt_deployment,
+    model_name=aoai_gpt_model,
+)
+
+output_cfg = KnowledgeAgentOutputConfiguration(
+    modality=KnowledgeAgentOutputConfigurationModality.ANSWER_SYNTHESIS,
+    include_activity=True,
+)
 
 agent = KnowledgeAgent(
-    name=agent_name,
-    models=[
-        KnowledgeAgentAzureOpenAIModel(
-            azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
-                resource_url=azure_openai_endpoint,
-                deployment_name=azure_openai_gpt_deployment,
-                model_name=azure_openai_gpt_model
-            )
-        )
-    ],
-    target_indexes=[
-        KnowledgeAgentTargetIndex(
-            index_name=index_name,
-            default_reranker_threshold=2.5
+    name=knowledge_agent_name,
+    models=[KnowledgeAgentAzureOpenAIModel(azure_open_ai_parameters=aoai_params)],
+    knowledge_sources=[
+        KnowledgeSourceReference(
+            name=knowledge_source_name,
+            reranker_threshold=2.5,
         )
     ],
+    output_configuration=output_cfg,
 )
 
-index_client.create_or_update_agent(agent)
-print(f"Knowledge agent '{agent_name}' created or updated successfully")
+index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
+index_client.create_or_update_agent(agent, api_version=search_api_version)
+print(f"Knowledge agent '{knowledge_agent_name}' created or updated successfully.")
 ```
 
 ## Set up messages
 
-The next step is to define the knowledge agent instructions and conversation context using the `messages` array. Each message includes a `role`, such as `user` or `assistant`, and `content` in natural language. A user message represents the query to be processed, while an assistant message guides the knowledge agent on how to respond. During the retrieval process, these messages are sent to an LLM to extract relevant responses from indexed documents.
-
-For now, create the following assistant message, which instructs `earth-search-agent` to answer questions about the Earth at night, cite sources using their `ref_id`, and respond with "I don't know" when answers are unavailable.
+Messages are the input for the retrieval route and contain the conversation history. Each message includes a role that indicates its origin, such as `system` or `user`, and content in natural language. The LLM you use determines which roles are valid.
 
-Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+Add and run a code cell with the following code to create a system message, which instructs `earth-knowledge-agent` to answer questions about the Earth at night and respond with "I don't know" when answers are unavailable.
 
-```Python
+```python
 instructions = """
-An Q&A agent that can answer questions about the Earth at night.
-Sources have a JSON format with a ref_id that must be cited in the answer.
-If you do not have the answer, respond with "I don't know".
+A Q&A agent that can answer questions about the Earth at night.
+If you don't have the answer, respond with "I don't know".
 """
 
 messages = [
     {
-        "role": "assistant",
+        "role": "system",
         "content": instructions
     }
 ]
 ```
 
 ## Run the retrieval pipeline
 
-You're ready to initiate the agentic retrieval pipeline. The input for this pipeline is the `messages` array, whose conversation history includes the instructions you previously provided and user queries. Additionally, `target_index_params` specifies the index to query and other configurations, such as the semantic ranker threshold.
+You're ready to run agentic retrieval. Add and run a code cell with the following code to send a two-part user query to `earth-knowledge-agent`.
 
-The following code sends a two-part user query to `earth-search-agent`, which deconstructs the query into subqueries, runs the subqueries against both text fields and vector embeddings in the `earth_at_night` index, and ranks and merges the results. The response is then appended to the `messages` array.
+Given the conversation history and retrieval parameters, the agent:
 
-Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+1. Analyzes the entire conversation to infer the user's information need.
+1. Decomposes the compound query into focused subqueries.
+1. Runs the subqueries concurrently against your knowledge source.
+1. Uses semantic ranker to rerank and filter the results.
+1. Synthesizes the top results into a natural-language answer.
 
-```Python
+```python
 from azure.search.documents.agent import KnowledgeAgentRetrievalClient
-from azure.search.documents.agent.models import KnowledgeAgentRetrievalRequest, KnowledgeAgentMessage, KnowledgeAgentMessageTextContent, KnowledgeAgentIndexParams
+from azure.search.documents.agent.models import KnowledgeAgentRetrievalRequest, KnowledgeAgentMessage, KnowledgeAgentMessageTextContent, SearchIndexKnowledgeSourceParams
 
-agent_client = KnowledgeAgentRetrievalClient(endpoint=endpoint, agent_name=agent_name, credential=credential)
-
-messages.append({
-    "role": "user",
-    "content": """
+agent_client = KnowledgeAgentRetrievalClient(endpoint=search_endpoint, agent_name=knowledge_agent_name, credential=credential)
+query_1 = """
     Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown?
     Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?
     """
-})
 
-retrieval_result = agent_client.retrieve(
-    retrieval_request=KnowledgeAgentRetrievalRequest(
-        messages=[KnowledgeAgentMessage(role=msg["role"], content=[KnowledgeAgentMessageTextContent(text=msg["content"])]) for msg in messages if msg["role"] != "system"],
-        target_index_params=[KnowledgeAgentIndexParams(index_name=index_name, reranker_threshold=2.5)]
-    )
-)
 messages.append({
-    "role": "assistant",
-    "content": retrieval_result.response[0].content[0].text
+    "role": "user",
+    "content": query_1
 })
+
+req = KnowledgeAgentRetrievalRequest(
+    messages=[
+        KnowledgeAgentMessage(
+            role=m["role"],
+            content=[KnowledgeAgentMessageTextContent(text=m["content"])]
+        ) for m in messages if m["role"] != "system"
+    ],
+    knowledge_source_params=[
+        SearchIndexKnowledgeSourceParams(
+            knowledge_source_name=knowledge_source_name,
+            kind="searchIndex"
+        )
+    ]
+)
+
+result = agent_client.retrieve(retrieval_request=req, api_version=search_api_version)
+print(f"Retrieved content from '{knowledge_source_name}' successfully.")
 ```
 
 ### Review the response, activity, and results
 
-Now you want to display the response, activity, and results of the retrieval pipeline.
-
-Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+Add and run a code cell with the following code to display the response, activity, and results of the retrieval pipeline.
 
-```Python
+```python
 import textwrap
 import json
 
 print("Response")
-print(textwrap.fill(retrieval_result.response[0].content[0].text, width=120))
+print(textwrap.fill(result.response[0].content[0].text, width=120))
 
 print("Activity")
-print(json.dumps([a.as_dict() for a in retrieval_result.activity], indent=2))
+print(json.dumps([a.as_dict() for a in result.activity], indent=2))
 
 print("Results")
-print(json.dumps([r.as_dict() for r in retrieval_result.references], indent=2))
+print(json.dumps([r.as_dict() for r in result.references], indent=2))
 ```
 
 The output should be similar to the following example, where:
 
-+ `Response` provides a text string of the most relevant documents (or chunks) in the search index based on the user query. As shown later in this quickstart, you can pass this string to an LLM for answer generation.
++ `Response` provides a synthesized, LLM-generated answer to the query that cites the retrieved documents. When answer synthesis isn't enabled, this section contains content extracted directly from the documents.
 
-+ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for query planning and execution.
++ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for semantic ranking, query planning, and answer synthesis.
 
 + `Results` lists the documents that contributed to the response, each one identified by their `doc_key`.
 
 ```
 Response
-[{"ref_id":1,"content":"# Urban Structure\n\n## March 16, 2013\n\n### Phoenix Metropolitan Area at Night\n\nThis figure presents a nighttime satellite view of the Phoenix metropolitan area, highlighting urban structure and transport corridors. City lights illuminate the layout of several cities and major thoroughfares.\n\n**Labeled Urban Features:**\n\n- **Phoenix:** Central and brightest area in the right-center of the image.\n- **Glendale:** Located to the west of Phoenix, this city is also brightly lit.\n- **Peoria:** Further northwest, this area is labeled and its illuminated grid is seen.\n- **Grand Avenue:** Clearly visible as a diagonal, brightly lit thoroughfare running from Phoenix through Glendale and Peoria.\n- **Salt River Channel:** Identified in the southeast portion, running through illuminated sections.\n- **Phoenix Mountains:** Dark, undeveloped region to the northeast of Phoenix.\n- **Agricultural Fields:** Southwestern corner of the image, grid patterns are visible but with much less illumination, indicating agricultural land use.\n\n**Additional Notes:**\n\n- The overall pattern shows a grid-like urban development typical of western U.S. cities, with scattered bright nodes at major intersections or city centers.\n- There is a clear transition from dense urban development to sparsely populated or agricultural land, particularly evident towards the bottom and left of the image.\n- The illuminated areas follow the existing road and street grids, showcasing the extensive spread of the metropolitan area.\n\n**Figure Description:**  \nA satellite nighttime image captured on March 16, 2013, showing Phoenix and surrounding areas (including Glendale and Peoria). Major landscape and infrastructural features, such as the Phoenix Mountains, Grand Avenue, the Salt River Channel, and agricultural fields, are labeled. The image reveals the extent of urbanization and the characteristic street grid illuminated by city lights.\n\n---\n\nPage 89"},{"ref_id":0,"content":"<!-- PageHeader=\"Urban Structure\" -->\n\n### Location of Phoenix, Arizona\n\nThe image depicts a globe highlighting the location of Phoenix, Arizona, in the southwestern United States, marked with a blue pinpoint on the map of North America. Phoenix is situated in the central part of Arizona, which is in the southwestern region of the United States.\n\n---\n\n### Grid of City Blocks-Phoenix, Arizona\n\nLike many large urban areas of the central and western United States, the Phoenix metropolitan area is laid out along a regular grid of city blocks and streets. While visible during the day, this grid is most evident at night, when the pattern of street lighting is clearly visible from the low-Earth-orbit vantage point of the ISS.\n\nThis astronaut photograph, taken on March 16, ... highlighted in this image is urbanized, there are several noticeably dark areas. The Phoenix Mountains are largely public parks and recreational land. To the west, agricultural fields provide a sharp contrast to the lit streets of residential developments. The Salt River channel appears as a dark ribbon within the urban grid.\n\n\n<!-- PageFooter=\"Earth at Night\" -->\n<!-- PageNumber=\"88\" -->"}]
+Suburban belts display larger December brightening than urban cores despite higher absolute light levels downtown
+because the urban grid encourages outward growth along city borders, fueled by widespread personal automobile use,
+leading to extensive suburban and residential municipalities linked by surface streets and freeways. This expansion
+results in increased lighting in suburban areas during December, reflecting growth and development patterns rather than
+just absolute light intensity downtown [ref_id:0].  The Phoenix nighttime street grid is sharply visible from space
+because the metropolitan area is laid out along a regular grid of city blocks and streets, with major street lighting
+clearly visible from low-Earth orbit. The grid pattern is especially evident at night due to street lighting, and major
+transportation corridors like Grand Avenue and brightly lit commercial properties enhance this visibility. In contrast,
+large stretches of interstate highways between Midwestern cities remain comparatively dim because, although the United
+States has extensive road networks, the lighting along interstate highways is less intense and continuous than the dense
+urban street grids. Additionally, navigable rivers and less urbanized areas show less light, indicating that lighting
+intensity correlates with urban density and development patterns rather than just the presence of transportation
+corridors [ref_id:0][ref_id:1][ref_id:2].
 Activity
 [
   {
     "id": 0,
-    "type": "ModelQueryPlanning",
-    "input_tokens": 1407,
-    "output_tokens": 309
+    "type": "modelQueryPlanning",
+    "elapsed_ms": 4572,
+    "input_tokens": 2071,
+    "output_tokens": 166
   },
   {
     "id": 1,
-    "type": "AzureSearchQuery",
-    "target_index": "earth_at_night",
-    "query": {
-      "search": "suburban belts December brightening urban cores light levels"
-    },
-    "query_time": "2025-05-06T20:47:01.814Z",
-    "elapsed_ms": 714
+    "type": "searchIndex",
+    "elapsed_ms": 608,
+    "knowledge_source_name": "earth-knowledge-source",
+    "query_time": "2025-09-05T17:38:49.330Z",
+    "count": 0,
+    "search_index_arguments": {
+      "search": "Reasons for larger December brightening in suburban belts compared to urban cores despite higher downtown light levels"
+    }
+  },
+    ... // Trimmed for brevity
+  {
+    "id": 4,
+    "type": "semanticReranker",
+    "input_tokens": 68989
   },
   {
-    "id": 2,
-    "type": "AzureSearchQuery",
-    "target_index": "earth_at_night",
-    "query": {
-      "search": "Phoenix nighttime street grid visibility from space"
-    },
-    "query_time": "2025-05-06T20:47:02.230Z",
-    "count": 2,
-    "elapsed_ms": 416
+    "id": 5,
+    "type": "modelAnswerSynthesis",
+    "elapsed_ms": 5619,
+    "input_tokens": 3931,
+    "output_tokens": 249
   }
 ]
 Results
 [
   {
-    "type": "AzureSearchDoc",
+    "type": "searchIndex",
     "id": "0",
     "activity_source": 2,
+    "reranker_score": 2.6642752,
     "doc_key": "earth_at_night_508_page_104_verbalized"
   },
-  {
-    "type": "AzureSearchDoc",
-    "id": "1",
-    "activity_source": 2,
-    "doc_key": "earth_at_night_508_page_105_verbalized"
-  }
+  ... // Trimmed for brevity
 ]
 ```
 
-## Create the Azure OpenAI client
-
-To extend the retrieval pipeline from answer *extraction* to answer *generation*, set up the Azure OpenAI client to interact with your `gpt-4.1-mini` deployment, which you specified using the `answer_model` variable in a previous section.
-
-Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
-
-```Python
-from openai import AzureOpenAI
-from azure.identity import get_bearer_token_provider
-
-azure_openai_token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")
-client = AzureOpenAI(
-    azure_endpoint=azure_openai_endpoint,
-    azure_ad_token_provider=azure_openai_token_provider,
-    api_version=azure_openai_api_version
-)
-```
-
-### Use the Responses API to generate an answer
-
-You can now use the Responses API to generate a detailed answer based on the indexed documents. The following code sends the `messages` array, which contains the conversation history, to your `gpt-4.1-mini` deployment.
-
-Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
-
-```Python
-response = client.responses.create(
-    model=answer_model,
-    input=messages
-)
-
-wrapped = textwrap.fill(response.output_text, width=100)
-print(wrapped)
-```
-
-The output should be similar to the following example, which uses the reasoning capabilities of `gpt-4.1-mini` to provide contextually relevant answers.
-
-```
-Suburban belts often exhibit larger December brightening than urban cores primarily because of the type of development and light distribution in those areas. Suburbs tend to have more uniform and expansive lighting, making them more visible in nighttime satellite images. In contrast, urban cores, although having higher absolute light levels, often contain dense building clusters that can cause light to be obscured or concentrated in smaller areas, leading to less visible brightening when viewed from space.  Regarding the visibility of the Phoenix nighttime street grid from space, it is attributed to the city's grid layout and the intensity of its street lighting. The grid pattern of the streets and the significant development around them create a stark contrast against less developed areas. Conversely, large stretches of interstate in the Midwest may remain dimmer due to fewer densely populated structures and less intensive street lighting, resulting in less illumination overall.  For more detailed insights, you can refer to the sources: [0] and [1].
-```
-
-### Use the Chat Completions API to generate an answer
-
-Alternatively, you can use the Chat Completions API for answer generation.
-
-Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
-
-```Python
-response = client.chat.completions.create(
-    model=answer_model,
-    messages=messages
-)
-
-wrapped = textwrap.fill(response.choices[0].message.content, width=100)
-print(wrapped)
-```
-
-The output should be similar to the following example.
-
-```
-Suburban belts tend to display larger December brightening than urban cores, despite the absolute light levels being higher in downtown areas, due to the differing density of light sources and how light scatters. In urban cores, the intense concentration of lights may result in a more uniform light distribution that can obscure the brightening effect, whereas suburban areas, with their lower density of lights and more open spaces, allow for clearer visibility of atmospheric light scattering, thus enhancing the brightening effect in those regions.  As for why the Phoenix nighttime street grid is sharply visible from space compared to the dim stretches of the interstate between Midwestern cities, it primarily relates to urban planning and development patterns. The Phoenix metropolitan area is laid out along a regular grid of city blocks that include extensive street lighting, making the urban structure distinctly visible from space. In contrast, the interstates between Midwestern cities often traverse areas with less concentrated development and fewer bright lighting sources, leading to these sections appearing dimmer in nighttime imagery [1; ref_id:1].
-```
-
 ## Continue the conversation
 
-Continue the conversation by sending another user query to `earth-search-agent`. The following code reruns the retrieval pipeline, fetching relevant content from the `earth_at_night` index and appending the response to the `messages` array. However, unlike before, you can now use the Azure OpenAI client to generate an answer based on the retrieved content.
-
-Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+Add and run a code cell with the following code to continue the conversation with `earth-knowledge-agent`. After you send this user query, the agent fetches relevant content from `earth-knowledge-source` and appends the response to the `messages` list.
 
-```Python
+```python
+query_2 = "How do I find lava at night?"
 messages.append({
     "role": "user",
-    "content": "How do I find lava at night?"
+    "content": query_2
 })
 
-retrieval_result = agent_client.retrieve(
-    retrieval_request=KnowledgeAgentRetrievalRequest(
-        messages=[KnowledgeAgentMessage(role=msg["role"], content=[KnowledgeAgentMessageTextContent(text=msg["content"])]) for msg in messages if msg["role"] != "system"],
-        target_index_params=[KnowledgeAgentIndexParams(index_name=index_name, reranker_threshold=2.5)]
-    )
+req = KnowledgeAgentRetrievalRequest(
+    messages=[
+        KnowledgeAgentMessage(
+            role=m["role"],
+            content=[KnowledgeAgentMessageTextContent(text=m["content"])]
+        ) for m in messages if m["role"] != "system"
+    ],
+    knowledge_source_params=[
+        SearchIndexKnowledgeSourceParams(
+            knowledge_source_name=knowledge_source_name,
+            kind="searchIndex"
+        )
+    ]
 )
-messages.append({
-    "role": "assistant",
-    "content": retrieval_result.response[0].content[0].text
-})
+
+result = agent_client.retrieve(retrieval_request=req, api_version=search_api_version)
+print(f"Retrieved content from '{knowledge_source_name}' successfully.")
 ```
 
 ### Review the new response, activity, and results
 
-Now you want to display the response, activity, and results of the retrieval pipeline.
-
-Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+Add and run a code cell with the following code to display the new response, activity, and results of the retrieval pipeline.
 
-```Python
+```python
 import textwrap
 import json
 
 print("Response")
-print(textwrap.fill(retrieval_result.response[0].content[0].text, width=120))
+print(textwrap.fill(result.response[0].content[0].text, width=120))
 
 print("Activity")
-print(json.dumps([a.as_dict() for a in retrieval_result.activity], indent=2))
+print(json.dumps([a.as_dict() for a in result.activity], indent=2))
 
 print("Results")
-print(json.dumps([r.as_dict() for r in retrieval_result.references], indent=2))
+print(json.dumps([r.as_dict() for r in result.references], indent=2))
 ```
 
-## Generate an LLM-powered answer
+## Clean up resources
 
-Now that you sent multiple user queries, use the Responses API to generate an answer based on the indexed documents and conversation history, which is captured in the `messages` array.
+When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
 
-Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+In the [Azure portal](https://portal.azure.com/), you can manage your Azure AI Search and Azure AI Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
 
-```Python
-response = client.responses.create(
-    model=answer_model,
-    input=messages
-)
+Otherwise, add and run code cells with the following code to delete the objects you created in this quickstart.
 
-wrapped = textwrap.fill(response.output_text, width=100)
-print(wrapped)
-```
+### Delete the knowledge agent
 
-The output should be similar to the following example.
+```python
+from azure.search.documents.indexes import SearchIndexClient
 
-```
-To find lava at night, you can look for the following signs:  1. **Active Volcanoes**: Research volcanoes that are currently active. Notable examples include Mount Etna in Italy and Kilauea in Hawaii. Both have had significant eruptions that can be observed at night due to the glow of lava. 2. **Satellite Imagery**: Use satellite imagery, especially those from sources like VIIRS (Visible Infrared Imaging Radiometer Suite) on the Suomi NPP satellite, which captures nighttime images of active lava flows. During eruptions, lava glows brightly in thermal infrared images, making it detectable from space.  3. **Safe Viewing Locations**: If you’re near an active volcano, find designated viewing areas for safety. Many national parks with volcanoes offer nighttime lava viewing experiences.  4. **Moonlight**: The presence of moonlight can enhance visibility, allowing you to spot lava flows more easily against the backdrop of the dark landscape.  5. **Monitoring Reports**: Follow updates from geological services or local authorities that monitor volcanic activity, which often provide real-time information about eruptions and visible lava flows at night.  6. **Photography**: If you're an enthusiast, consider using long-exposure photography techniques to capture the glow of lava flows at night.  For more information on observing volcanic activity, satellite imagery can provide vital data for detecting lava flows and volcanic eruptions.
+index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
+index_client.delete_agent(knowledge_agent_name)
+print(f"Knowledge agent '{knowledge_agent_name}' deleted successfully.")
 ```
 
-## Clean up resources
+### Delete the knowledge source
 
-When working in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money. You can delete resources individually, or you can delete the resource group to delete the entire set of resources.
-
-In the Azure portal, you can find and manage resources by selecting **All resources** or **Resource groups** from the left pane. You can also run the following code to delete the objects you created in this quickstart.
-
-### Delete the knowledge agent
-
-Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+```python
+from azure.search.documents.indexes import SearchIndexClient
 
-```Python
-index_client = SearchIndexClient(endpoint=endpoint, credential=credential)
-index_client.delete_agent(agent_name)
-print(f"Knowledge agent '{agent_name}' deleted successfully")
+index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
+index_client.delete_knowledge_source(knowledge_source=knowledge_source_name)
+print(f"Knowledge source '{knowledge_source_name}' deleted successfully.")
 ```
 
 ### Delete the search index
 
-Add and run a new code cell in the `quickstart-agentic-retrieval.ipynb` notebook with the following code:
+```python
+from azure.search.documents.indexes import SearchIndexClient
 
-```Python
-index_client = SearchIndexClient(endpoint=endpoint, credential=credential)
+index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
 index_client.delete_index(index_name)
-print(f"Index '{index_name}' deleted successfully")
+print(f"Index '{index_name}' deleted successfully.")
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するPythonクイックスタートの大幅な更新"
}
```

### Explanation
この変更は、Pythonクイックスタートのドキュメントに対する大規模な修正を示しています。主な変更点は、エージェントリトリーバルを用いた会話型検索体験を作成する方法についての説明が更新されたことです。具体的には、Azure AI Foundryでの大規模言語モデル（LLM）を使用した知識エージェントの導入、そしてREST APIのバージョンや依存関係の更新が含まれています。また、ドキュメントの構成や手順が整理され、ユーザーが必要とする設定や準備についての情報がより明確になっています。新しいコード例やリンクの追加により、ユーザーがすぐに作業を始められるよう配慮されています。このアップデートは、ユーザーに最新の機能と最善の実践を提供することを目的としています。

## articles/search/includes/quickstarts/agentic-retrieval-rest.md{#item-3df373}

<details>
<summary>Diff</summary>
````diff
@@ -9,9 +9,9 @@ ms.date: 08/26/2025
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
 
-In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-concept.md) to create a conversational search experience powered by documents indexed in Azure AI Search and large language models (LLMs) from Azure AI Foundry Models.
+In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-concept.md) to create a conversational search experience powered by documents indexed in Azure AI Search and large language models (LLMs) from Azure OpenAI in Azure AI Foundry Models.
 
-A *knowledge agent* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the agent outputs raw content from your sources, but this quickstart passes the output to an LLM for natural-language answer generation.
+A *knowledge agent* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the agent outputs raw content from your sources, but this quickstart uses the answer synthesis modality for natural-language answer generation.
 
 Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
@@ -34,7 +34,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 ## Connect from your local system
 
-You configured role-based access to interact with Azure AI Search and Azure AI Foundry. From the command line, use the Azure CLI to sign in to the same subscription and tenant for both resources. For more information, see [Quickstart: Connect without keys](../../search-get-started-rbac.md).
+You configured role-based access to interact with Azure AI Search and Azure OpenAI in Azure AI Foundry. From the command line, use the Azure CLI to sign in to the same subscription and tenant for both resources. For more information, see [Quickstart: Connect without keys](../../search-get-started-rbac.md).
 
 To connect from your local system:
 
@@ -56,7 +56,7 @@ To connect from your local system:
 
 ## Load connections
 
-Before you send any requests, define endpoints, credentials, and deployment details for connections to Azure AI Search and Azure AI Foundry. These values are used in the following sections.
+Before you send any requests, define endpoints, credentials, and deployment details for connections to Azure AI Search and Azure OpenAI in Azure AI Foundry. These values are used in the following sections.
 
 To load the connections:
 
@@ -95,7 +95,7 @@ To load the connections:
 
 In Azure AI Search, an index is a structured collection of data. Use [Indexes - Create (REST API)](/rest/api/searchservice/indexes/create) to define an index named `earth-at-night`, which you previously specified using the `@index-name` variable.
 
-The index schema contains fields for document identification and page content, embeddings, and numbers. The schema also includes configurations for semantic ranking and vector search, which uses your `text-embedding-3-large` deployment to vectorize text and match documents based on semantic or conceptual similarity.
+The index schema contains fields for document identification and page content, embeddings, and numbers. The schema also includes configurations for semantic ranking and vector search, which uses your `text-embedding-3-large` deployment to vectorize text and match documents based on semantic similarity.
 
 ```HTTP
 ### Create an index
@@ -299,7 +299,7 @@ POST {{search-url}}/agents('{{knowledge-agent-name}}')/retrieve?api-version={{ap
 
 The output should be similar to the following JSON, where:
 
-+ `response` provides a synthesized, LLM-generated answer to the query based on the retrieved documents. When answer synthesis isn't enabled, this section contains content extracted directly from the documents.
++ `response` provides a synthesized, LLM-generated answer to the query that cites the retrieved documents. When answer synthesis isn't enabled, this section contains content extracted directly from the documents.
 
 + `activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for semantic ranking, query planning, and answer synthesis.
 
@@ -399,7 +399,9 @@ The output should be similar to the following JSON, where:
 
 When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
 
-Run the following code to delete the objects you created in this quickstart.
+In the [Azure portal](https://portal.azure.com/), you can manage your Azure AI Search and Azure AI Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
+
+Otherwise, run the following code to delete the objects you created in this quickstart.
 
 <!-- You can delete resources individually or delete the entire resource group.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するRESTクイックスタートの更新"
}
```

### Explanation
この変更は、RESTクイックスタートの文書に対する小規模な修正を示しています。主な内容として、Azure AI Foundryからの大規模言語モデル（LLM）を使用したエージェントリトリーバルに関する説明が更新され、より具体的にAzure OpenAIが言及されています。また、知識エージェントの自然言語応答生成において、出力が合成されることが強調されています。さらに、リソースの管理に関する情報が更新され、Azureポータルでリソースを管理する方法についての見出しが追加されました。全体として、ユーザーに対する明確で関連性のある情報が提供されています。

## articles/search/includes/quickstarts/agentic-retrieval-typescript.md{#item-e6370b}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-c
 Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
 > [!TIP]
-> The TypeScript version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST version of this quickstart.
+> The TypeScript version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST or Python version.
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するTypeScriptクイックスタートの更新"
}
```

### Explanation
この変更は、TypeScriptクイックスタートのドキュメントに対する小さな修正を示しています。主な修正点は、TIPセクションの内容に関するもので、使用しているREST APIバージョンに関する情報が更新されました。具体的には、2025-05-01-previewのREST APIバージョンでは知識ソースや他のエージェントリトリーバル機能がサポートされていないことに加え、これらの機能を使用するためにはRESTまたはPythonバージョンに目を通すように案内されています。この変更により、ユーザーは機能の対比と適用可能なバージョンをより簡単に理解できるようになっています。

## articles/search/includes/quickstarts/search-get-started-rbac-python.md{#item-de7760}

<details>
<summary>Diff</summary>
````diff
@@ -42,7 +42,7 @@ To sign in:
 ## Connect to Azure AI Search
 
 > [!NOTE]
-> This section illustrates the basic Python pattern for keyless connections. For comprehensive guidance, see a specific quickstart or tutorial, such as [Quickstart: Run agentic retrieval in Azure AI Search](../../search-get-started-agentic-retrieval.md).
+> This section illustrates the basic Python pattern for keyless connections. For comprehensive guidance, see a specific quickstart or tutorial, such as [Quickstart: Use agentic retrieval in Azure AI Search](../../search-get-started-agentic-retrieval.md).
 
 You can use Python notebooks in Visual Studio Code to send requests to your Azure AI Search service. For request authentication, use the `DefaultAzureCredential` class from the Azure Identity library.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PythonによるRBACを使用した検索クイックスタートの更新"
}
```

### Explanation
この変更は、Pythonを使用したRBACに基づく検索クイックスタートの文書に対する小規模な修正を示しています。主な修正点は、ノートセクションにおける表現の変更です。特に、「エージェントリトリーバルに関するクイックスタート」のタイトルが「エージェントリトリーバルを使用したクイックスタート」と修正され、より正確なタイトルが提供されるようになりました。この変更により、ユーザーは該当するリソースに対してより適切にアクセスできるようになり、明確な指示での案内が強化されています。

## articles/search/includes/quickstarts/search-get-started-rbac-rest.md{#item-fd8ef4}

<details>
<summary>Diff</summary>
````diff
@@ -58,7 +58,7 @@ To get your token:
 ## Connect to Azure AI Search
 
 > [!NOTE]
-> This section illustrates the basic REST pattern for keyless connections. For comprehensive guidance, see a specific quickstart or tutorial, such as [Quickstart: Run agentic retrieval in Azure AI Search](../../search-get-started-agentic-retrieval.md).
+> This section illustrates the basic REST pattern for keyless connections. For comprehensive guidance, see a specific quickstart or tutorial, such as [Quickstart: Use agentic retrieval in Azure AI Search](../../search-get-started-agentic-retrieval.md).
 
 You can use the REST Client extension in Visual Studio Code to send requests to your Azure AI Search service. For request authentication, include an `Authorization` header with the Microsoft Entra ID token you previously generated.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTを使用したRBACに関する検索クイックスタートの更新"
}
```

### Explanation
この変更は、RESTを使用したRBACに基づく検索クイックスタートの文書に対する小規模な修正を示しています。具体的には、ノートセクションの内容が修正されており、「エージェントリトリーバルに関するクイックスタート」のタイトルが「エージェントリトリーバルを使用したクイックスタート」に改められ、より明確に表現されています。この修正により、ユーザーは該当する情報源に対して適切にアクセスでき、導入する際の指針がより分かりやすくなっています。

## articles/search/samples-dotnet.md{#item-12f3fa}

<details>
<summary>Diff</summary>
````diff
@@ -52,7 +52,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. A
 |-------------|------------------|---------|
 | [create-mvc-app](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/create-mvc-app) |  [Tutorial: Add search to an ASP.NET Core (MVC) app](tutorial-csharp-create-mvc-app.md) | While most samples are console applications, this MVC sample uses a web page to front the sample Hotels index, demonstrating basic search, pagination, and other server-side behaviors.|
 | [quickstart](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/AzureSearchQuickstart) | [Quickstart: Full-text search](search-get-started-text.md) | Covers the basic workflow for creating, loading, and querying a search index in C# using sample data. |
-| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) | [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md) | Creates a knowledge agent in Azure AI Search to integrate LLM reasoning into query planning. |
+| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) | [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md) | Creates a retrieval pipeline that integrates semantic ranking in Azure AI Search with LLM-powered query planning and answer generation. |
 | [quickstart-rag](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-rag) | [Quickstart: Generative search (RAG)](search-get-started-rag.md) | Uses grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
 | [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-search/) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Shows the index schema and query request for invoking semantic ranker. |
 | [quickstart-vector-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-vector-search) | [Quickstart: Vector search](search-get-started-vector.md) | Covers the basic workflow for indexing and querying vector data. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのエージェントリトリーバルに関するクイックスタートの内容更新"
}
```

### Explanation
この変更は、Azure AI Searchに関するサンプルコードを紹介する文書の一部を更新しています。具体的には、「エージェントリトリーバルに関するクイックスタート」の説明が変更され、エージェントリトリーバルが「LLM駆動のクエリ計画と回答生成を統合するリトリーバルパイプラインを作成する」ことを強調する内容に修正されました。この更新により、ユーザーはエージェントリトリーバルの機能についてより正確な理解を得ることができ、その構築方法を容易に把握できるようになります。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. M
 | Samples | Article |
 |---------|---------|
 | [Quickstart](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart) | Source code for the Python portion of [Quickstart: Full-text search](search-get-started-text.md). This sample covers the basic workflow for creating, loading, and querying a search index using sample data. |
-| [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval) | Source code for the Python portion of [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md). |
+| [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval) | Source code for the Python portion of [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md). This sample creates a retrieval pipeline that integrates semantic ranking in Azure AI Search with LLM-powered query planning and answer generation. |
 | [Quickstart-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-RAG) | Source code for the Python portion of [Quickstart: Generative search (RAG) with grounding data from Azure AI Search](search-get-started-rag.md). |
 | [Quickstart-Semantic-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) | Source code for the Python portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). This sample shows the index schema and query request for invoking semantic ranker. |
 | [Quickstart-Vector-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Vector-Search) | Source code for the Python portion of [Quickstart: Vector search](search-get-started-vector.md). Covers the basic workflow for indexing and querying vector data. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonサンプルのエージェントリトリーバルに関するクイックスタートの内容更新"
}
```

### Explanation
この変更は、Azure AI Searchに関するPythonサンプルの文書に対する小規模な修正を表示しています。具体的には、「エージェントリトリーバルに関するクイックスタート」の説明が修正され、サンプルが「Azure AI SearchにおけるセマンティックランキングとLLM駆動のクエリ計画および回答生成を統合するリトリーバルパイプラインを作成する」ことに焦点を当てた内容に改められています。この更新により、ユーザーはサンプルの目的とその機能についてより明確に理解でき、実装手順をより効果的に把握できるようになっています。

## articles/search/samples-rest.md{#item-198ebc}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. M
 |---------|---------|
 | [quickstart](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart) | Source code for the REST portion of [Quickstart: Full-text search](search-get-started-text.md). This sample covers the basic workflow for creating, loading, and querying a search index using sample data. |
 | [quickstart-vectors](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) | Source code for [Quickstart: Vector search using REST APIs](search-get-started-vector.md). This sample covers the basic workflow for indexing and querying vector data. |
-| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-agentic-retrieval) | Source code for the REST portion of [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md). This sample shows you how to create a knowledge agent in Azure AI Search to integrate LLM reasoning into query planning. |
+| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-agentic-retrieval) | Source code for the REST portion of [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md). This sample creates a retrieval pipeline that integrates semantic ranking in Azure AI Search with LLM-powered query planning and answer generation. |
 | [skillset-tutorial](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skillset-tutorial) | Source code for [Tutorial: Use REST and AI to generate searchable content from Azure blobs](tutorial-skillset.md). This sample shows you how to create a skillset that iterates over Azure blobs to extract information and infer structure.|
 | [skill examples](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skill-examples) | Skillset examples in indexer pipelines that include indexes and indexers so that you can follow field mappings, output field mappings, and source paths. |
 | [debug-sessions](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Debug-sessions) | Source code for [Tutorial: Diagnose, repair, and commit changes to your skillset](cognitive-search-tutorial-debug-sessions.md). This sample shows you how to use a skillset debug session in the Azure portal. REST is used to create the objects used during debug.|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTサンプルのエージェントリトリーバルに関するクイックスタートの内容更新"
}
```

### Explanation
この変更は、Azure AI SearchにおけるREST APIサンプルの文書に対する小さな修正です。具体的には、「エージェントリトリーバルに関するクイックスタート」の説明が更新され、サンプルが「Azure AI SearchにおけるセマンティックランキングとLLM駆動のクエリ計画および回答生成を統合するリトリーバルパイプラインを作成する」という内容に変更されました。この修正により、ユーザーはこのサンプルがどのように新しい技術と統合されているかを理解しやすくなり、実装の目的がより明確になります。


