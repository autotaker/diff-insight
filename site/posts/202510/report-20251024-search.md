---
date: '2025-10-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a8cf2b8...MicrosoftDocs:782e48d
summary: この変更は、Azure Cognitive Searchに関連するドキュメントを更新し、スキルやAPIキー、GenAIプロンプト、データソースギャラリーに関する情報をより明確かつ最新のものにしました。特に、スキルの課金モデルやAPIの互換性についてのユーザーガイダンスが向上しています。新たにLogic
  Appsを利用したデータ取り込みに関する具体的な指示が追加され、破壊的な変更は含まれていません。また、APIセキュリティや「built-in skill」についての説明も強化されています。これにより、開発者はプロジェクトにより迅速に対応できるようになり、Azureプラットフォームを利用したAIソリューションの開発がスムーズになることが期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a8cf2b8...MicrosoftDocs:782e48d){target="_blank"}

<format>
# ハイライト
この変更は、Azure Cognitive Searchに関連するドキュメントを更新し、スキルやAPIキー、GenAIプロンプト、データソースギャラリーに関して情報をより明確かつ最新のものにしました。特に、スキルの課金モデルやAPIの互換性など重要な要素について、ユーザーガイダンスが向上しています。

## 新機能
- Logic Appsを利用したデータ取り込みの具体的な指示と事前構築されたワークフローの利用に関する説明。
  
## 破壊的変更
- 特に破壊的とされる変更は含まれていません。

## その他の更新
- Azure OpenAIに関する「built-in skill」の定義の明確化。
- Azure OpenAI Responses APIが互換性がないことの明記。
- APIキーに関するセキュリティと使用方法の詳細な情報強化。
- ドキュメント中の最新日付への更新。

# インサイト
今回の変更は、Azure Cognitive Searchを利用する開発者やエンジニアにとって、より明確で実践的な情報を提供するための重要なアップデートとなっています。それにより、以下の点が特に注目されています。

まず、「スキル」の定義がより明確になったことで、AzureにホストされたAIモデルや外部の容量を持ち込むスキルの使い分けが簡単になります。これにより、開発者はプロジェクトのニーズに合わせて適切なスキルを選択できるようになりました。

次に、GenAIプロンプトスキルの更新により、サポートされるAPIやモデルの詳細が追加され、ユーザーが利用可能なオプションを正確に把握できます。この情報は、特に新たにAPIを統合しようとする段階での摩擦を減らすのに役立ちます。

さらに、データソースギャラリーのLogic Apps関連の説明が強化されたことで、具体的な取り込み手順が分かりやすく紹介されています。これにより、Azure AI Searchへのデータインデックス作成の効率が高まり、開発者はより迅速に実装を進められます。

APIキーの利用に関するドキュメントの更新も重要です。セキュリティ面での注意喚起とキーの違いの明確化が進み、APIキーによる接続が行いやすくなり、より安全かつ効果的にAzure AI Searchを利用できます。

全体として、これらの改訂は、Azure Cognitive Searchを利用する際に、ユーザーがより正確な情報を手に入れ、プロジェクトに迅速に応用できるようサポートすることを目的としています。これにより、Azureプラットフォームを利用したAIソリューションの開発がスムーズに進むことが期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-predefined-skills.md](#item-81d522) | minor update | 記事の更新 - スキルに関する情報の明確化 | modified | 4 | 4 | 8 | 
| [cognitive-search-skill-genai-prompt.md](#item-384bf9) | minor update | GenAIプロンプトスキルに関する情報の更新 | modified | 2 | 2 | 4 | 
| [api-keys-enabled.png](#item-5ff7fd) | minor update | 画像の更新 - APIキーの有効化に関するビジュアル | modified | 0 | 0 | 0 | 
| [search-data-sources-gallery.md](#item-18727f) | minor update | データソースギャラリーの情報更新 | modified | 2 | 2 | 4 | 
| [search-security-api-keys.md](#item-d8c908) | minor update | APIキーによるAzure AI Search接続に関する情報の強化 | modified | 59 | 13 | 72 | 


# Modified Contents
## articles/search/cognitive-search-predefined-skills.md{#item-81d522}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: concept-article
-ms.date: 10/06/2025
+ms.date: 10/23/2025
 ms.update-cycle: 365-days
 ---
 
@@ -22,7 +22,7 @@ A *skill* is an atomic operation that transforms content in some way. Often, it'
 
 Skills are organized into the following categories:
 
-* A *built-in skill* wraps API calls to an Azure AI resource, where the inputs, outputs, and processing steps are well understood. For skills that call an Azure AI resource, the connection is made over the internal network. For skills that call Azure OpenAI, you provide the connection information that the search service uses to connect to the resource. A small quantity of processing is nonbillable, but at larger volumes, processing is billable. Built-in skills are based on pretrained models from Microsoft, which means you can't train the model using your own training data.
+* A *built-in skill* wraps API calls to an Azure AI resource, where the inputs, outputs, and processing steps are well understood. For skills that call an Azure AI resource, the connection is made over the internal network. For skills that run AI workloads on your own Azure-hosted models or services, you provide the connection information that the search service uses to connect to the resource. A small quantity of processing is nonbillable, but at larger volumes, processing is billable. Built-in skills are based on pretrained models from Microsoft, which means you can't train the model using your own training data.
 
 * A *custom skill* provides custom code that executes externally to the search service. It's accessed through a URI. Custom code is often made available through an Azure function app. To attach an open-source or third-party vectorization model, use a custom skill.
 
@@ -47,9 +47,9 @@ Skills that call Azure AI are billed at the Standard rate when you [attach an Az
 | [Microsoft.Skills.Vision.VectorizeSkill](cognitive-search-skill-vision-vectorize.md) | Multimodal image and text vectorization. | Azure AI services ([pricing](https://azure.microsoft.com/pricing/details/cognitive-services/)) |
 | [Microsoft.Skills.Util.DocumentIntelligenceLayoutSkill](cognitive-search-skill-document-intelligence-layout.md) | Accelerate information extraction from documents. | Azure AI services ([pricing](https://azure.microsoft.com/pricing/details/cognitive-services/)) |
 
-## Azure OpenAI skills
+## "Bring your own capacity" skills
 
-Skills that call models deployed on Azure OpenAI are billed at the Standard rate.
+Skills that run AI workloads on your own Azure-hosted models or services are billed at the Standard rate.
 
 | OData type  | Description | Metered by |
 |-------|-------------|-------------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事の更新 - スキルに関する情報の明確化"
}
```

### Explanation
この変更は、Azure Cognitive Searchに関する記事の一部を改善し、情報を最新のものに更新することを目的としています。具体的には、スキルカテゴリの説明が修正され、特に「デフォルトスキル」と「カスタムスキル」の定義とそれに関連する情報が明確化されています。

主な変更点は、"built-in skill"の定義で、Azureがホストするモデルやサービス上で実行されるAIワークロードに関する情報が更新されています。元の文ではAzure OpenAIに関連する接続情報を提供するという表現があったのに対し、新しい文では「自分のAzureホストモデルまたはサービスで実行されるAIワークロード」という言葉に置き換えられ、より明確になっています。

また、スキルの課金についてのセクション見出しが「Azure OpenAI skills」から「Bring your own capacity skills」へ変更され、これにより使用されるモデルが利用者の所有するものになることを強調しています。この変更は、文章の流れや内容の正確さを向上させるために行われています。

## articles/search/cognitive-search-skill-genai-prompt.md{#item-384bf9}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2025
 ms.topic: reference
-ms.date: 09/18/2025
+ms.date: 10/23/2025
 ---
 
 # GenAI Prompt skill
@@ -35,7 +35,7 @@ The GenAI Prompt skill is available in the [latest preview REST API](/rest/api/s
 
 ## Supported models
 
-- You can use any [chat completion inference model](/azure/ai-foundry/model-inference/concepts/models) deployed in AI Foundry, such as GPT models, Deepseek R#, Llama-4-Mavericj, Cohere-command-r, and so forth.
+- You can use any [chat completion inference model](/azure/ai-foundry/model-inference/concepts/models) deployed in AI Foundry, such as GPT models, Deepseek R#, Llama-4-Mavericj, Cohere-command-r, and so forth. For GPT models specifically, only the chat completions API endpoints are supported. Endpoints using the Azure OpenAI Responses API (containing `/openai/responses` as part of the URI) are not currently compatible.
 
 - For image verbalization, the model you use to analyze the image determines what image formats are supported.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GenAIプロンプトスキルに関する情報の更新"
}
```

### Explanation
この変更は、GenAIプロンプトスキルに関するドキュメントを更新し、特に使用可能なモデルやAPIの互換性に関する重要な情報を追加しています。具体的には、GPTモデルに関する制限が明確にされ、チャット補完APIエンドポイントのみがサポートされることが記載されています。

変更内容の一部として、新しい文が挿入され、「Azure OpenAI Responses API（URIに`/openai/responses`を含む）を使用したエンドポイントは現在は互換性がない」と明記されることで、ユーザーが適切なAPIを選択するためのガイダンスが提供されています。また、文中の日付が更新され、ドキュメントの最新性が保たれています。

これにより、ユーザーがGenAIプロンプトスキルを利用する際に、どのモデルがサポートされているか、またそれに関わるAPIの使用に関する制限を理解しやすくなるとともに、より明確な情報が提供されています。

## articles/search/media/search-security-overview/api-keys-enabled.png{#item-5ff7fd}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像の更新 - APIキーの有効化に関するビジュアル"
}
```

### Explanation
この変更は、APIキーが有効化された状況を示す画像ファイルに対して行われましたが、実際の変更内容には追加や削除はありませんでした。画像ファイル自体は、セキュリティに関する概要を示すために使用され、APIキーの管理や利用の重要性を説明する文脈において重要な役割を果たしています。

今回の変更によって、画像は以前のバージョンからの変更がなかったため、内容の更新はなく、既存のビジュアルが引き続き使用されることを示しています。これは、仕様や文書の整合性を保つために既存のリソースを活用し続ける一環と言えるでしょう。

## articles/search/search-data-sources-gallery.md{#item-18727f}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 09/28/2025
+ms.date: 10/21/2025
 ---
 
 # Data sources gallery
@@ -141,7 +141,7 @@ Connect to a OneLake lakehouse to extract supported files content from a hierarc
 
 ## Logic app connectors
 
-Pull in content [using logic app workflows](search-how-to-index-logic-apps.md) and the following supported data sources.
+Pull in content [using logic app workflows](search-how-to-index-logic-apps.md) and the following supported data sources. Note that the Logic Apps artifacts mentioned below, they have a pre-built workflow, however, you can use [any connectors listed under Logic Apps](/connectors/connector-reference/connector-reference-logicapps-connectors) that pull data from sources and create your own indexing pipeline workflow that pushes data to [Azure AI Search via a Logic App connector](/azure/logic-apps/connectors/azure-ai#azure-ai-search).
 
 :::row:::
 :::column span="":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データソースギャラリーの情報更新"
}
```

### Explanation
この変更は、「データソースギャラリー」に関するドキュメントにおいて情報が更新され、特にLogic Appsに関連する内容が強化されています。主な変更点には、日付の更新に加え、Logic Appsを利用してデータを取り込む際の具体的な指示が追加されています。

更新前の文は、Logic Appsワークフローを使用することについて簡単に触れていただけでしたが、変更後は、事前に構築されたワークフローが利用できること、さらにはLogic Appsのコネクタを使って自分自身のインデックスパイプラインを構築できる旨が記載され、より具体的で実用的な情報が提供されています。

これにより、ユーザーはLogic Appsを通じてAzure AI Searchにデータを送信する方法をより理解しやすくなり、効率的にデータインデックスを行うためのガイダンスが強化されています。

## articles/search/search-security-api-keys.md{#item-d8c908}

<details>
<summary>Diff</summary>
````diff
@@ -9,14 +9,14 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 07/31/2025
+ms.date: 10/22/2025
 ms.update-cycle: 365-days
 #customer intent: I want to learn how to connect to Azure AI Search using API keys so that I can authenticate inbound requests to my search service.
 ---
 
 # Connect to Azure AI Search using keys
 
-Azure AI Search supports both identity-based and key-based authentication for connections to your search service. An API key is a unique string composed of 52 randomly generated numbers and letters. In your source code, you can specify it in a request header, or as an [environment variable](/azure/ai-services/cognitive-services-environment-variables) or as an app setting in your project, and then reference the variable on the request.
+Azure AI Search supports both identity-based and key-based authentication for connections to your search service. An API key is a unique string composed of 52 randomly generated numbers and letters. In your source code, you can specify it in a request header, or as an [environment variable](/azure/ai-services/cognitive-services-environment-variables) or app setting in your project, and then reference the variable on the request.
 
 > [!IMPORTANT]
 > When you create a search service, key-based authentication is the default, but it's not the most secure option. We recommend that you replace it with [role-based access](search-security-enable-roles.md).
@@ -45,18 +45,21 @@ Visually, there's no distinction between an admin key or query key. Both keys ar
 API keys are used for data plane (content) requests, such as creating or accessing an index or, any other request that's represented in the [Search REST APIs](/rest/api/searchservice/). 
 
 You can use either an API key or [Azure roles](search-security-rbac.md) for control plane (service) requests. When you use an API key:
-- Admin keys are used for creating, modifying, or deleting objects. Admin keys are also used to GET object definitions and system information.
+
+- Admin keys are used for creating, modifying, or deleting objects. Admin keys are also used to GET object definitions and system information, such as [LIST Indexes](/rest/api/searchservice/indexes/list) or [GET Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics).
+
 - Query keys are typically distributed to client applications that issue queries.
 
 ### [**REST API**](#tab/rest-use)
 
-**How API keys are used in REST calls**:
-
-Set an admin key in the request header. You can't pass admin keys on the URI or in the body of the request. Admin keys are used for create-read-update-delete operation and on requests issued to the search service itself, such as [LIST Indexes](/rest/api/searchservice/indexes/list) or [GET Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics).
+Set an admin key in the request header. You can't pass admin keys on the URI or in the body of the request.
 
 Here's an example of admin API key usage on a create index request:
 
 ```http
+@baseUrl=https://my-demo-search-service.search.windows.net
+@adminApiKey=aaaabbbb-0000-cccc-1111-dddd2222eeee
+
 ### Create an index
 POST {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
@@ -71,7 +74,7 @@ POST {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
    }
 ```
 
-Set a query key in a request header for POST, or on the URI for GET. Query keys are used for operations that target the `index/docs` collection: [Search Documents](/rest/api/searchservice/documents/search-get), [Autocomplete](/rest/api/searchservice/documents/autocomplete-get), [Suggest](/rest/api/searchservice/documents/suggest-get), or [GET Document](/rest/api/searchservice/documents/get). 
+Set a query key in a request header for POST, or on the URI for GET. Query keys are used for operations that target the `index/docs` collection: [Search Documents](/rest/api/searchservice/documents/search-get), [Autocomplete](/rest/api/searchservice/documents/autocomplete-get), [Suggest](/rest/api/searchservice/documents/suggest-get), or [GET Document](/rest/api/searchservice/documents/get).
 
 Here's an example of query API key usage on a Search Documents (GET) request:
 
@@ -83,26 +86,69 @@ GET /indexes/my-new-index/docs?search=*&api-version=2025-09-01&api-key={{queryAp
 > [!NOTE]  
 > It's considered a poor security practice to pass sensitive data such as an `api-key` in the request URI. For this reason, Azure AI Search only accepts a query key as an `api-key` in the query string. As a general rule, we recommend passing your `api-key` as a request header.
 
-### [**PowerShell**](#tab/azure-ps-use)
+### [**Python**](#tab/python-use)
+
+It's a best practice to set the API key as an environment variable, but for simplicity, this example shows it as a string. The example uses a query API key for a query operation.
+
+```python
+# Import libraries
+from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential, AzureAuthorityHosts
+
+# Variables for endpoint, keys, index
+search_endpoint: str = "https://<Put your search service NAME here>.search.windows.net/"
+credential = AzureKeyCredential("Your search service query key")
+index_name: str = "hotels-quickstart-python"
+
+# Set up the client
+search_client = SearchClient(endpoint=search_endpoint,
+                      index_name=index_name,
+                      credential=credential)
+
+# Run the query
+results =  search_client.search(query_type='simple',
+    search_text="*" ,
+    select='HotelName,Description,Tags',
+    include_total_count=True)
+
+print ('Total Documents Matching Query:', results.get_count())
+for result in results:
+    print(result["@search.score"])
+    print(result["HotelName"])
+    print(result["Tags"])
+    print(f"Description: {result['Description']}")
+```
 
-**How API keys are used in PowerShell**:
+### [**PowerShell**](#tab/azure-ps-use)
 
 Set API keys in the request header using the following syntax:
 
-```azurepowershell
+```powershell
 $headers = @{
 'api-key' = '<YOUR-ADMIN-OR-QUERY-API-KEY>'
 'Content-Type' = 'application/json' 
 'Accept' = 'application/json' }
 ```
 
-A script example showing API key usage for various operations can be found at [Quickstart: Create an Azure AI Search index in PowerShell using REST APIs](search-get-started-text.md).
+Use a variable to contain the fully qualified query:
+
+```powershell
+$url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2025-09-01&search=attached restaurant&searchFields=Description,Tags&$select=HotelId,HotelName,Tags,Description&$count=true'
+```
+
+Send the request to the search service:
+
+```powershell
+Invoke-RestMethod -Uri $url -Headers $headers | ConvertTo-Json
+```
+
+More script examples for other operations can be found at [Quickstart: Create an Azure AI Search index in PowerShell using REST APIs](search-get-started-text.md).
 
 ### [**Portal**](#tab/portal-use)
 
-**How API keys are used in the Azure portal**:
+Recall that key authentication is enabled by default and supports data plane operations such as indexing and queries. 
 
-Key authentication applies to data plane operations such as indexing and queries. It's enabled by default. However, if you [disable API keys](search-security-enable-roles.md#disable-api-key-authentication) and set up role assignments, the Azure portal uses role assignments instead.
+However, if you [disable API keys](search-security-enable-roles.md#disable-api-key-authentication) and set up role assignments, the Azure portal uses role assignments instead.
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIキーによるAzure AI Search接続に関する情報の強化"
}
```

### Explanation
この変更は、「APIキーを使用してAzure AI Searchに接続する方法」に関するドキュメントを更新し、特にコンテンツの明瞭さと実用性を向上させるために情報が強化されています。主な更新点は、文中に追加されたAPIキーの使用に関する詳細および実際のコーディング例です。

具体的には、以下のポイントが重要です：
- APIキーの作成と使用についての情報を更新し、特に管理キーとクエリーキーの違いが明確になりました。
- REST APIやPython、PowerShellを使用したAPIキーの具体的な使用方法に関するコード例が追加され、開発者にとっての実用性が向上しています。
- セキュリティに関する注意事項が強調され、ユーザーがこれらの情報を適切に理解し、利用できるようになっています。

このように、文書全体が刷新され、Azure AI Searchをより安全かつ効果的に利用するための指針が強化されています。


