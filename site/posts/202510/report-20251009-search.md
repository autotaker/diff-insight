---
date: '2025-10-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fa0a155...MicrosoftDocs:53e6b22
summary: |-
  現在の修正では、GPTモデルのバージョンを「gpt-4.1-mini」から「gpt-5-mini」へ更新することに注力しています。この変更は、さまざまなプログラミング言語において一貫して行われ、最新モデルの機能を活用することを目的としています。また、エージェント検索やBlobナレッジソースにおける設定や説明も改善されています。

  新機能として、クイックスタートガイドでのGPTモデルのアップグレードや、エージェント検索における「gpt-5」シリーズのサポート拡大があります。特に破壊的な変更はありませんが、最新モデルに依存する設定には調整が必要となります。

  文書全体にわたって説明文の改善、重複の削除、技術用語の一貫性などが図られています。これにより、Azureサービス利用者が最新技術をより効果的に活用できるようになります。全体として、このアップデートは、Azureの検索やエージェント技術の利用を一層進めることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fa0a155...MicrosoftDocs:53e6b22){target="_blank"}

# Highlights
現在の修正は、主に使用されるGPTモデルのバージョンを「gpt-4.1-mini」から「gpt-5-mini」に更新することに焦点を当てたものです。この変更は、さまざまなプログラミング言語（C#, Java, JavaScript, Python, REST, TypeScript）に渡り一貫して実施され、最新のモデルの機能と性能を活用するために行われました。また、エージェント検索やBlobナレッジソース、ベクトル検索などの設定や概念文書においても、モデルバージョンの更新や説明の改善が行われています。

## New features
- クイックスタートガイド全般でのGPTモデルのバージョンが「gpt-5-mini」にアップグレード。
- エージェント検索の設定や概念においても、サポートされるモデルが「gpt-5」シリーズに拡大。

## Breaking changes
特に破壊的な変更はありませんが、エージェントや検索パイプラインの設定が最新のモデルに依存するようになり、過去のモデルを使い続ける場合には調整が必要です。

## Other updates
- 文書全体での案内や説明文の改善。
- 重複文章の削除と情報の追加によるアップグレード手順の簡素化。
- 技術用語の一貫性と正確性の向上。

# Insights
この一連の修正は、新しいGPTモデルを活用するための全面的なアップデートとして捉えることができます。特に「gpt-5-mini」へのバージョン変更は、全体的なパフォーマンスと機能向上を意図しており、多くのプログラミング環境で対応済みです。

エージェント検索に使用されるモデルが最新バージョンに統一され、利便性と効果性の向上が期待されます。モデルの更新により、クエリプランニングや応答生成がより高度なものとなり、デプロイされたエージェントの質も向上するでしょう。

さらに、文書自体も整備され、重複や冗長性の削除、情報の追加によって、利用者がより直感的に理解できる内容になっています。これにより、Azureサービスの利用者はより簡潔で効果的に最新技術を活用できるでしょう。

加えて、技術用語や設定内容の明確化により、正確さと理解しやすさが向上しています。この変更は特にベクトル検索やナレッジソースにおけるモデル利用において、最新の状態が反映されることを可能にします。

総じて、このアップデートは、Azureの検索およびエージェント技術のより高度な使用を支援するものと言えます。特にデプロイと設定に関わる開発者やエンジニアにとって、最新のガイドラインに基づいたより効果的な実装が可能になります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-csharp.md](#item-f93ed3) | minor update | コードの更新: モデルのバージョンをgpt-4.1-miniからgpt-5-miniに変更 | modified | 4 | 4 | 8 | 
| [agentic-retrieval-java.md](#item-4e2c55) | minor update | コードの更新: モデルのバージョンをgpt-4.1-miniからgpt-5-miniに変更 | modified | 6 | 6 | 12 | 
| [agentic-retrieval-javascript.md](#item-715283) | minor update | コードの更新: モデルのバージョンをgpt-4.1-miniからgpt-5-miniに変更 | modified | 6 | 6 | 12 | 
| [agentic-retrieval-python.md](#item-efee6a) | minor update | コードの更新: モデルのバージョンをgpt-4.1-miniからgpt-5-miniに変更 | modified | 4 | 4 | 8 | 
| [agentic-retrieval-rest.md](#item-3df373) | minor update | コードの更新: モデルのバージョンをgpt-4.1-miniからgpt-5-miniに変更 | modified | 4 | 4 | 8 | 
| [agentic-retrieval-setup.md](#item-e5e297) | minor update | コードの更新: モデルのバージョンをgpt-4.1-miniからgpt-5-miniに変更 | modified | 2 | 2 | 4 | 
| [agentic-retrieval-typescript.md](#item-e6370b) | minor update | コードの更新: モデルのバージョンをgpt-4.1-miniからgpt-5-miniに変更 | modified | 6 | 6 | 12 | 
| [search-agentic-retrieval-concept.md](#item-797a22) | minor update | エージェント検索概念の更新: モデルサポートの変更 | modified | 2 | 2 | 4 | 
| [search-agentic-retrieval-how-to-create.md](#item-310fbe) | minor update | エージェント作成手順の更新: モデルの変更と説明の改善 | modified | 4 | 4 | 8 | 
| [search-how-to-upgrade.md](#item-990225) | minor update | サービスアップグレード手順の簡素化と用語の修正 | modified | 3 | 3 | 6 | 
| [search-knowledge-source-how-to-blob.md](#item-58d84a) | minor update | Blobナレッジソースのモデルバージョン更新 | modified | 4 | 4 | 8 | 
| [vector-search-how-to-truncate-dimensions.md](#item-8350a3) | minor update | ベクトル検索の設定に関する用語の修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/includes/quickstarts/agentic-retrieval-csharp.md{#item-f93ed3}

<details>
<summary>Diff</summary>
````diff
@@ -113,8 +113,8 @@ To create and run the agentic retrieval pipeline:
     
                 string aoaiEmbeddingModel = "text-embedding-3-large";
                 string aoaiEmbeddingDeployment = "text-embedding-3-large";
-                string aoaiGptModel = "gpt-4.1-mini";
-                string aoaiGptDeployment = "gpt-4.1-mini";
+                string aoaiGptModel = "gpt-5-mini";
+                string aoaiGptDeployment = "gpt-5-mini";
     
                 string indexName = "earth-at-night";
                 string knowledgeSourceName = "earth-knowledge-source";
@@ -723,7 +723,7 @@ Console.WriteLine($"Knowledge source '{knowledgeSourceName}' created or updated
 
 ### Create a knowledge agent
 
-To target `earth-knowledge-source` and your `gpt-4.1-mini` deployment at query time, you need a knowledge agent. Add and run a code cell with the following code to define a knowledge agent named `earth-knowledge-agent`, which you previously specified using the `knowledgeAgentName` variable.
+To target `earth-knowledge-source` and your `gpt-5-mini` deployment at query time, you need a knowledge agent. Add and run a code cell with the following code to define a knowledge agent named `earth-knowledge-agent`, which you previously specified using the `knowledgeAgentName` variable.
 
 `RerankerThreshold` ensures semantic relevance by excluding responses with a reranker score of `2.5` or lower. Meanwhile, `Modality` is set to `AnswerSynthesis`, enabling natural-language answers that cite the retrieved documents.
 
@@ -832,7 +832,7 @@ The following code displays the response, activity, and results of the retrieval
 
 + `Response` provides a synthesized, LLM-generated answer to the query that cites the retrieved documents. When answer synthesis isn't enabled, this section contains content extracted directly from the documents.
 
-+ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for semantic ranking, query planning, and answer synthesis.
++ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-5-mini` deployment and the tokens used for semantic ranking, query planning, and answer synthesis.
 
 + `Results` lists the documents that contributed to the response, each one identified by their `DocKey`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コードの更新: モデルのバージョンをgpt-4.1-miniからgpt-5-miniに変更"
}
```

### Explanation
この修正は、C#によるエージェント検索パイプラインのクイックスタートガイドにおいて、使用するGPTモデルのバージョンを更新したものです。具体的には、元々のコードでは「gpt-4.1-mini」というモデルが指定されていましたが、新しいバージョンである「gpt-5-mini」に変更されました。

主な変更点は以下の通りです：
- 変数`aoaiGptModel`と`aoaiGptDeployment`の値が「gpt-4.1-mini」から「gpt-5-mini」に変更されました。
- 知識エージェントの定義においても、ターゲットとするデプロイメントが「gpt-5-mini」に更新されています。
- 出力に関連する文言も同様に修正され、活動トラッキングでのデプロイメント表記が新しいモデルに適応されています。

これにより、新しいGPTモデルの機能を活用することができ、ドキュメントに記載されたコードも最新の技術に対応することが可能になります。

## articles/search/includes/quickstarts/agentic-retrieval-java.md{#item-4e2c55}

<details>
<summary>Diff</summary>
````diff
@@ -117,7 +117,7 @@ The sample in this quickstart works with the Java Runtime. Install a Java Develo
 
     ```plaintext
     AZURE_OPENAI_ENDPOINT=https://<your-ai-foundry-resource-name>.openai.azure.com/
-    AZURE_OPENAI_GPT_DEPLOYMENT=gpt-4.1-mini
+    AZURE_OPENAI_GPT_DEPLOYMENT=gpt-5-mini
     AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-large
     AZURE_SEARCH_ENDPOINT=https://<your-search-service-name>.search.windows.net
     AZURE_SEARCH_INDEX_NAME=agentic-retrieval-sample
@@ -167,7 +167,7 @@ The sample in this quickstart works with the Java Runtime. Install a Java Develo
         private static final String SEARCH_ENDPOINT;
         private static final String AZURE_OPENAI_ENDPOINT;
         private static final String AZURE_OPENAI_GPT_DEPLOYMENT;
-        private static final String AZURE_OPENAI_GPT_MODEL = "gpt-4.1-mini";
+        private static final String AZURE_OPENAI_GPT_MODEL = "gpt-5-mini";
         private static final String AZURE_OPENAI_EMBEDDING_DEPLOYMENT;
         private static final String AZURE_OPENAI_EMBEDDING_MODEL = "text-embedding-3-large";
         private static final String INDEX_NAME = "earth_at_night";
@@ -182,7 +182,7 @@ The sample in this quickstart works with the Java Runtime. Install a Java Develo
                 "https://contoso-agentic-search-service.search.windows.net");
             AZURE_OPENAI_ENDPOINT = getEnvVar(dotenv, "AZURE_OPENAI_ENDPOINT",
                 "https://contoso-proj-agentic-foundry-res.openai.azure.com/");
-            AZURE_OPENAI_GPT_DEPLOYMENT = getEnvVar(dotenv, "AZURE_OPENAI_GPT_DEPLOYMENT", "gpt-4.1-mini");
+            AZURE_OPENAI_GPT_DEPLOYMENT = getEnvVar(dotenv, "AZURE_OPENAI_GPT_DEPLOYMENT", "gpt-5-mini");
             AZURE_OPENAI_EMBEDDING_DEPLOYMENT = getEnvVar(dotenv, "AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-large");
         }
         
@@ -1150,7 +1150,7 @@ try {
 
 ### Create a knowledge agent
 
-To connect Azure AI Search to your `gpt-4.1-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. The following code defines a knowledge agent named `earth-search-agent` that uses the agent definition to process queries and retrieve relevant documents from the `earth_at_night` index.
+To connect Azure AI Search to your `gpt-5-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. The following code defines a knowledge agent named `earth-search-agent` that uses the agent definition to process queries and retrieve relevant documents from the `earth_at_night` index.
 
 To ensure relevant and semantically meaningful responses, `defaultRerankerThreshold` is set to exclude responses with a reranker score of `2.5` or lower.
 
@@ -1324,13 +1324,13 @@ The output should include:
 
 + `Response` provides a text string of the most relevant documents (or chunks) in the search index based on the user query. As shown later in this quickstart, you can pass this string to an LLM for answer generation.
 
-+ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for query planning and execution.
++ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-5-mini` deployment and the tokens used for query planning and execution.
 
 + `Results` lists the documents that contributed to the response, each one identified by their `DocKey`.
 
 ### Create the Azure OpenAI client
 
-To extend the retrieval pipeline from answer *extraction* to answer *generation*, set up the Azure OpenAI client to interact with your `gpt-4.1-mini` deployment.
+To extend the retrieval pipeline from answer *extraction* to answer *generation*, set up the Azure OpenAI client to interact with your `gpt-5-mini` deployment.
 
 ```java
 OpenAIAsyncClient openAIClient = new OpenAIClientBuilder()
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コードの更新: モデルのバージョンをgpt-4.1-miniからgpt-5-miniに変更"
}
```

### Explanation
この修正では、Javaでのエージェント検索パイプラインに関するクイックスタートガイドにおいて、使用しているGPTモデルを「gpt-4.1-mini」から「gpt-5-mini」にアップデートしました。これにより、新しいモデルの機能と性能を活用することが可能になります。

主な変更点は次の通りです：
- 環境変数として設定されている`AZURE_OPENAI_GPT_DEPLOYMENT`の値が更新され、新しいデプロイメント「gpt-5-mini」が指定されました。
- コード内のモデルの定義を示す変数`AZURE_OPENAI_GPT_MODEL`も「gpt-5-mini」に変更され、全体で一貫性が保たれています。
- 知識エージェントの定義や処理に関する部分でも、使用するデプロイメントが「gpt-5-mini」に変更されています。
- 出力内容においても、アクティビティと結果に関連するセクションが更新され、新しいモデルを反映するように修正されています。

これによって、ユーザーは最新の技術を反映したガイドラインに従って、より効果的にエージェント検索パイプラインを構築することができるようになります。

## articles/search/includes/quickstarts/agentic-retrieval-javascript.md{#item-715283}

<details>
<summary>Diff</summary>
````diff
@@ -71,7 +71,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
     ```plaintext
     AZURE_OPENAI_ENDPOINT=https://<your-ai-foundry-resource-name>.openai.azure.com/
-    AZURE_OPENAI_GPT_DEPLOYMENT=gpt-4.1-mini
+    AZURE_OPENAI_GPT_DEPLOYMENT=gpt-5-mini
     AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-large
     AZURE_SEARCH_ENDPOINT=https://<your-search-service-name>.search.windows.net
     AZURE_SEARCH_INDEX_NAME=agentic-retrieval-sample
@@ -92,8 +92,8 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
     const config = {
         searchEndpoint: process.env.AZURE_SEARCH_ENDPOINT || "https://your-search-service.search.windows.net",
         azureOpenAIEndpoint: process.env.AZURE_OPENAI_ENDPOINT || "https://your-ai-foundry-resource.openai.azure.com/",
-        azureOpenAIGptDeployment: process.env.AZURE_OPENAI_GPT_DEPLOYMENT || "gpt-4.1-mini",
-        azureOpenAIGptModel: "gpt-4.1-mini",
+        azureOpenAIGptDeployment: process.env.AZURE_OPENAI_GPT_DEPLOYMENT || "gpt-5-mini",
+        azureOpenAIGptModel: "gpt-5-mini",
         azureOpenAIApiVersion: process.env.OPENAI_API_VERSION || "2025-03-01-preview",
         azureOpenAIEmbeddingDeployment: process.env.AZURE_OPENAI_EMBEDDING_DEPLOYMENT || "text-embedding-3-large",
         azureOpenAIEmbeddingModel: "text-embedding-3-large",
@@ -878,7 +878,7 @@ try {
 
 ### Create a knowledge agent
 
-To connect Azure AI Search to your `gpt-4.1-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. The following code defines a knowledge agent named `earth-search-agent` that uses the agent definition to process queries and retrieve relevant documents from the `earth_at_night` index.
+To connect Azure AI Search to your `gpt-5-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. The following code defines a knowledge agent named `earth-search-agent` that uses the agent definition to process queries and retrieve relevant documents from the `earth_at_night` index.
 
 To ensure relevant and semantically meaningful responses, `defaultRerankerThreshold` is set to exclude responses with a reranker score of `2.5` or lower.
 
@@ -1011,13 +1011,13 @@ The output should include:
 
 + `Response` provides a text string of the most relevant documents (or chunks) in the search index based on the user query. As shown later in this quickstart, you can pass this string to an LLM for answer generation.
 
-+ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for query planning and execution.
++ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-5-mini` deployment and the tokens used for query planning and execution.
 
 + `Results` lists the documents that contributed to the response, each one identified by their `DocKey`.
 
 ### Create the Azure OpenAI client
 
-To extend the retrieval pipeline from answer *extraction* to answer *generation*, set up the Azure OpenAI client to interact with your `gpt-4.1-mini` deployment.
+To extend the retrieval pipeline from answer *extraction* to answer *generation*, set up the Azure OpenAI client to interact with your `gpt-5-mini` deployment.
 
 ```javascript
 const scope = "https://cognitiveservices.azure.com/.default";
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コードの更新: モデルのバージョンをgpt-4.1-miniからgpt-5-miniに変更"
}
```

### Explanation
この修正では、JavaScriptによるエージェント検索パイプラインのクイックスタートガイドにおいて、使用されるGPTモデルが「gpt-4.1-mini」から「gpt-5-mini」に更新されました。この変更により、最新の機能と向上した性能を活用することが可能になります。

修正された具体的な点は以下の通りです：
- 環境変数`AZURE_OPENAI_GPT_DEPLOYMENT`のデフォルト値が「gpt-5-mini」に変更され、コード内で使用されるモデル名も同様に更新されました。
- 知識エージェントの定義においても、ターゲットデプロイメントが新しい「gpt-5-mini」に変更されています。
- 出力に関する説明の中では、アクティビティや結果のトラッキングも新しいモデル名を反映するように修正されました。
- Azure OpenAIクライアントのセクションも「gpt-5-mini」に適応するように変更されています。

これにより、最新技術を使用した実用的なガイドラインが提供され、ユーザーは新しいモジュールの利点を最大限に引き出すことができるようになります。

## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -81,8 +81,8 @@ To install the packages and load the connections:
     aoai_endpoint = "PUT-YOUR-AOAI-FOUNDRY-URL-HERE"
     aoai_embedding_model = "text-embedding-3-large"
     aoai_embedding_deployment = "text-embedding-3-large"
-    aoai_gpt_model = "gpt-4.1-mini"
-    aoai_gpt_deployment = "gpt-4.1-mini"
+    aoai_gpt_model = "gpt-5-mini"
+    aoai_gpt_deployment = "gpt-5-mini"
     index_name = "earth-at-night"
     knowledge_source_name = "earth-knowledge-source"
     knowledge_agent_name = "earth-knowledge-agent"
@@ -191,7 +191,7 @@ print(f"Knowledge source '{knowledge_source_name}' created or updated successful
 
 ## Create a knowledge agent
 
-To target `earth-knowledge-source` and your `gpt-4.1-mini` deployment at query time, you need a knowledge agent. Add and run a code cell with the following code to define a knowledge agent named `earth-knowledge-agent`, which you previously specified using the `knowledge_agent_name` variable.
+To target `earth-knowledge-source` and your `gpt-5-mini` deployment at query time, you need a knowledge agent. Add and run a code cell with the following code to define a knowledge agent named `earth-knowledge-agent`, which you previously specified using the `knowledge_agent_name` variable.
 
 `reranker_threshold` ensures semantic relevance by excluding responses with a reranker score of `2.5` or lower. Meanwhile, `modality` is set to `ANSWER_SYNTHESIS`, enabling natural-language answers that cite the retrieved documents.
 
@@ -315,7 +315,7 @@ The output should be similar to the following example, where:
 
 + `Response` provides a synthesized, LLM-generated answer to the query that cites the retrieved documents. When answer synthesis isn't enabled, this section contains content extracted directly from the documents.
 
-+ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for semantic ranking, query planning, and answer synthesis.
++ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-5-mini` deployment and the tokens used for semantic ranking, query planning, and answer synthesis.
 
 + `Results` lists the documents that contributed to the response, each one identified by their `doc_key`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コードの更新: モデルのバージョンをgpt-4.1-miniからgpt-5-miniに変更"
}
```

### Explanation
この修正は、Python用のエージェント検索パイプラインに関するクイックスタートガイドにおいて、使用されるGPTモデルを「gpt-4.1-mini」から「gpt-5-mini」に更新する内容です。この変更により、最新の機能とパフォーマンスを利用することができるようになります。

主な変更点は以下の通りです：
- 環境変数として設定されている`aoai_gpt_model`および`aoai_gpt_deployment`の値が、両方とも「gpt-5-mini」に更新されました。
- 知識エージェントの定義において、新しいモデル「gpt-5-mini」を利用する旨が明記されました。このエージェントは、`earth-knowledge-source`をターゲットとし、クエリ処理を行います。
- 出力に関連するセクションでは、アクティビティのトラッキングが最新のモデルを反映するように修正され、モデル名が更新されています。

これにより、ユーザーは新しいモデルがもたらす性能向上を活用しながら、効率的にエージェント検索パイプラインを構築することができるようになります。

## articles/search/includes/quickstarts/agentic-retrieval-rest.md{#item-3df373}

<details>
<summary>Diff</summary>
````diff
@@ -70,8 +70,8 @@ To load the connections:
     @aoai-url = PUT-YOUR-AOAI-FOUNDRY-URL-HERE
     @aoai-embedding-model = text-embedding-3-large
     @aoai-embedding-deployment = text-embedding-3-large
-    @aoai-gpt-model = gpt-4.1-mini
-    @aoai-gpt-deployment = gpt-4.1-mini
+    @aoai-gpt-model = gpt-5-mini
+    @aoai-gpt-deployment = gpt-5-mini
     @index-name = earth-at-night
     @knowledge-source-name = earth-knowledge-source
     @knowledge-agent-name = earth-knowledge-agent
@@ -232,7 +232,7 @@ POST {{search-url}}/knowledgesources?api-version={{api-version}}  HTTP/1.1
 
 ## Create a knowledge agent
 
-To target your `earth-knowledge-source` and `gpt-4.1-mini` deployment at query time, you need a knowledge agent. Use [Knowledge Agents - Create (REST API)](/rest/api/searchservice/knowledge-agents/create?view=rest-searchservice-2025-08-01-preview&preserve-view=true) to define an agent named `earth-knowledge-agent`, which you previously specified using the `@knowledge-agent-name` variable.
+To target your `earth-knowledge-source` and `gpt-5-mini` deployment at query time, you need a knowledge agent. Use [Knowledge Agents - Create (REST API)](/rest/api/searchservice/knowledge-agents/create?view=rest-searchservice-2025-08-01-preview&preserve-view=true) to define an agent named `earth-knowledge-agent`, which you previously specified using the `@knowledge-agent-name` variable.
 
 `knowledgeSources.rerankerThreshold` ensures semantic relevance by excluding responses with a reranker score of `2.5` or lower. Meanwhile, `outputConfiguration.modality` is set to `answerSynthesis`, enabling natural-language answers that cite the retrieved documents.
 
@@ -301,7 +301,7 @@ The output should be similar to the following JSON, where:
 
 + `response` provides a synthesized, LLM-generated answer to the query that cites the retrieved documents. When answer synthesis isn't enabled, this section contains content extracted directly from the documents.
 
-+ `activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for semantic ranking, query planning, and answer synthesis.
++ `activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-5-mini` deployment and the tokens used for semantic ranking, query planning, and answer synthesis.
 
 + `references` lists the documents that contributed to the response, each one identified by their `docKey`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コードの更新: モデルのバージョンをgpt-4.1-miniからgpt-5-miniに変更"
}
```

### Explanation
この修正は、REST APIを使用したエージェント検索パイプラインに関するクイックスタートガイドにおいて、使用されるGPTモデルが「gpt-4.1-mini」から「gpt-5-mini」に更新される内容です。この変更により、新しいモデルの利点が活用できるようになります。

主な変更点は以下の通りです：
- 環境変数として設定されている`@aoai-gpt-model`と`@aoai-gpt-deployment`の値が更新され、「gpt-5-mini」が使用されるようになりました。
- 知識エージェントの定義部分では、ターゲットデプロイメントとして新しいモデル「gpt-5-mini」が指定されています。このエージェントは、クエリ処理の際に`earth-knowledge-source`をターゲットにします。
- 出力に関するセクションでは、アクティビティのトラッキングが更新され、最新のモデル名が反映されました。

この修正により、ユーザーは最新のモデルが提供する性能向上を利用し、エージェント検索パイプラインの構築と運用をより効率的に行うことができるようになります。

## articles/search/includes/quickstarts/agentic-retrieval-setup.md{#item-e5e297}

<details>
<summary>Diff</summary>
````diff
@@ -85,7 +85,7 @@ To use agentic retrieval, you must deploy two Azure OpenAI models to your Azure
 
 + An embedding model for text-to-vector conversion. This quickstart uses `text-embedding-3-large`, but you can use any embedding model that supports the `text-embedding` task.
 
-+ A [supported chat completion model](../../search-agentic-retrieval-how-to-create.md#supported-models) for query planning and answer generation. This quickstart uses `gpt-4.1-mini`. Optionally, you can use one model for query planning and another model for answer generation, but this quickstart uses the same model for simplicity.
++ A [supported chat completion model](../../search-agentic-retrieval-how-to-create.md#supported-models) for query planning and answer generation. This quickstart uses `gpt-5-mini`. Optionally, you can use one model for query planning and another model for answer generation, but this quickstart uses the same model for simplicity.
 
 To deploy the Azure OpenAI models:
 
@@ -101,4 +101,4 @@ To deploy the Azure OpenAI models:
 
 1. Select **Deploy**.
 
-1. Repeat the previous steps, but this time, deploy **gpt-4.1-mini** from the model catalog.
+1. Repeat the previous steps, but this time, deploy **gpt-5-mini** from the model catalog.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コードの更新: モデルのバージョンをgpt-4.1-miniからgpt-5-miniに変更"
}
```

### Explanation
この修正は、エージェント検索の設定に関するクイックスタートガイドにおいて、使用されるチャット完了モデルのバージョンを「gpt-4.1-mini」から「gpt-5-mini」に更新する内容です。この変更により、最新モデルの機能と性能を活用することができるようになります。

主な変更点は以下の通りです：
- エンベディングモデルとして使用されるモデルの説明に追加があり、`text-embedding-3-large`が引き続き推奨されています。
- チャット完了モデルに関する説明が更新され、クイックスタートでは「gpt-5-mini」が使用されると明記されています。このモデルは、クエリプランニングと回答生成の両方に使用されます。
- デプロイメント手順についても、最初のモデルのデプロイ後に「gpt-5-mini」をデプロイするように指示が変更されています。

これにより、ユーザーは最新の生成モデルを利用し、エージェント検索の効果を最大限に引き出すことができるようになります。

## articles/search/includes/quickstarts/agentic-retrieval-typescript.md{#item-e6370b}

<details>
<summary>Diff</summary>
````diff
@@ -77,7 +77,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
     ```plaintext
     AZURE_OPENAI_ENDPOINT=https://<your-ai-foundry-resource-name>.openai.azure.com/
-    AZURE_OPENAI_GPT_DEPLOYMENT=gpt-4.1-mini
+    AZURE_OPENAI_GPT_DEPLOYMENT=gpt-5-mini
     AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-large
     AZURE_SEARCH_ENDPOINT=https://<your-search-service-name>.search.windows.net
     AZURE_SEARCH_INDEX_NAME=agentic-retrieval-sample
@@ -114,8 +114,8 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
     const config = {
         searchEndpoint: process.env.AZURE_SEARCH_ENDPOINT || "https://your-search-service.search.windows.net",
         azureOpenAIEndpoint: process.env.AZURE_OPENAI_ENDPOINT || "https://your-ai-foundry-resource.openai.azure.com/",
-        azureOpenAIGptDeployment: process.env.AZURE_OPENAI_GPT_DEPLOYMENT || "gpt-4.1-mini",
-        azureOpenAIGptModel: "gpt-4.1-mini",
+        azureOpenAIGptDeployment: process.env.AZURE_OPENAI_GPT_DEPLOYMENT || "gpt-5-mini",
+        azureOpenAIGptModel: "gpt-5-mini",
         azureOpenAIApiVersion: process.env.OPENAI_API_VERSION || "2025-03-01-preview",
         azureOpenAIEmbeddingDeployment: process.env.AZURE_OPENAI_EMBEDDING_DEPLOYMENT || "text-embedding-3-large",
         azureOpenAIEmbeddingModel: "text-embedding-3-large",
@@ -1079,7 +1079,7 @@ try {
 
 ### Create a knowledge agent
 
-To connect Azure AI Search to your `gpt-4.1-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. The following code defines a knowledge agent named `earth-search-agent` that uses the agent definition to process queries and retrieve relevant documents from the `earth_at_night` index.
+To connect Azure AI Search to your `gpt-5-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. The following code defines a knowledge agent named `earth-search-agent` that uses the agent definition to process queries and retrieve relevant documents from the `earth_at_night` index.
 
 To ensure relevant and semantically meaningful responses, `defaultRerankerThreshold` is set to exclude responses with a reranker score of `2.5` or lower.
 
@@ -1220,13 +1220,13 @@ The output should include:
 
 + `Response` provides a text string of the most relevant documents (or chunks) in the search index based on the user query. As shown later in this quickstart, you can pass this string to an LLM for answer generation.
 
-+ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for query planning and execution.
++ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-5-mini` deployment and the tokens used for query planning and execution.
 
 + `Results` lists the documents that contributed to the response, each one identified by their `DocKey`.
 
 ### Create the Azure OpenAI client
 
-To extend the retrieval pipeline from answer *extraction* to answer *generation*, set up the Azure OpenAI client to interact with your `gpt-4.1-mini` deployment.
+To extend the retrieval pipeline from answer *extraction* to answer *generation*, set up the Azure OpenAI client to interact with your `gpt-5-mini` deployment.
 
 ```typescript
 const scope = "https://cognitiveservices.azure.com/.default";
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コードの更新: モデルのバージョンをgpt-4.1-miniからgpt-5-miniに変更"
}
```

### Explanation
この修正は、TypeScriptを使用したエージェント検索のクイックスタートガイドにおいて、使用されるGPTモデルのバージョンを「gpt-4.1-mini」から「gpt-5-mini」に更新する内容です。この変更により、最新のモデルを利用した機能強化が期待できます。

主な変更点は以下の通りです：
- 環境変数の設定が更新され、モデルデプロイメントの値が「gpt-5-mini」に変更されました。この環境変数は、Azure OpenAIのGPTモデルのデプロイメントを指定します。
- コード内での直接的なモデルの指定も更新され、`azureOpenAIGptDeployment`と`azureOpenAIGptModel`の値が「gpt-5-mini」に変更されています。
- 知識エージェントを定義する部分でも、接続されるモデル名が更新され、`gpt-5-mini`と明記されています。
- レスポンスに関するセクションも更新され、取得プロセス中に生成されるサブクエリやトークンが新しいモデルに基づいていることが反映されています。

この修正により、ユーザーは最新のGPTモデルを活用した、より効果的なエージェント検索機能を実装できるようになります。

## articles/search/search-agentic-retrieval-concept.md{#item-797a22}

<details>
<summary>Diff</summary>
````diff
@@ -65,7 +65,7 @@ Agentic retrieval is designed for conversational search experiences that use an
 
 The agentic retrieval process follows three main phases:
 
-1. **Query planning**: A knowledge agent sends your query and conversation history to an LLM (gpt-4o or gpt-4.1 series), which analyzes the context and breaks down complex questions into focused subqueries. This step is automated and not customizable. The number of subqueries depends on what the LLM decides and whether the `maxDocsForReranker` parameter is higher than 50. A new subquery is defined for each 50-document batch sent to semantic ranker.
+1. **Query planning**: A knowledge agent sends your query and conversation history to an LLM (gpt-4o, gpt-4.1, and gpt-5 series), which analyzes the context and breaks down complex questions into focused subqueries. This step is automated and not customizable. The number of subqueries depends on what the LLM decides and whether the `maxDocsForReranker` parameter is higher than 50. A new subquery is defined for each 50-document batch sent to semantic ranker.
 
 2. **Query execution**: All subqueries run simultaneously against your knowledge sources, using keyword, vector, and hybrid search. Each subquery undergoes semantic reranking to find the most relevant matches. References are extracted and retained for citation purposes.
 
@@ -88,7 +88,7 @@ Your search index determines query execution and any optimizations that occur du
 Your application drives the pipeline by calling the knowledge agent and handling the response. The pipeline returns grounding data that you pass to an LLM for answer generation in your conversation interface. For implementation details, see [Build an agent-to-agent retrieval solution](search-agentic-retrieval-how-to-pipeline.md).
 
 > [!NOTE]
-> Only gpt-4o and gpt-4.1 series models are supported for query planning. You can use any model for final answer generation.
+> Only gpt-4o, gpt-4.1, and gpt-5 series models are supported for query planning. You can use any model for final answer generation.
 
 ## How to get started
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索概念の更新: モデルサポートの変更"
}
```

### Explanation
この修正は、エージェント検索の概念に関する文書で、クエリプランニングに使用できるLLM（大規模言語モデル）のサポートされるバージョンを更新したものです。具体的には、「gpt-4o」と「gpt-4.1」シリーズに加えて、「gpt-5」シリーズが新たにサポートされることが明記されています。

主な変更点は以下の通りです：
- クエリプランニングプロセスの説明において、LLMのサポートが「gpt-4o」および「gpt-4.1」シリーズから「gpt-5」シリーズを含むように拡張されました。これにより、最新のモデルを利用してより高度なクエリプランニングが行えることが示されています。
- ノート部分でも、サポートされるモデルについての情報が更新され、クエリプランニングには「gpt-4o」、「gpt-4.1」、および「gpt-5」シリーズのモデルが必要であると明記されています。最終的な回答生成には、いずれのモデルも使用可能です。

このような変更により、ユーザーは最新の言語モデルを利用したエージェント検索機能を強化することができます。

## articles/search/search-agentic-retrieval-how-to-create.md{#item-310fbe}

<details>
<summary>Diff</summary>
````diff
@@ -57,7 +57,7 @@ Make sure you have a supported model that Azure AI Search can access. The follow
 
 ### Supported models
 
-Use Azure OpenAI or an equivalent open source model:
+Use Azure OpenAI or an equivalent open-source model:
 
 + `gpt-4o`
 + `gpt-4o-mini`
@@ -307,8 +307,8 @@ PUT {{search-url}}/agents/{{agent-name}}?api-version=2025-08-01-preview
             "azureOpenAIParameters": {
                 "resourceUri": "{{model-provider-url}}",
                 "apiKey": "{{model-api-key}}",
-                "deploymentId": "gpt-4o-mini",
-                "modelName": "gpt-4o-mini"
+                "deploymentId": "gpt-5-mini",
+                "modelName": "gpt-5-mini"
             }
         }
     ],
@@ -345,7 +345,7 @@ PUT {{search-url}}/agents/{{agent-name}}?api-version=2025-08-01-preview
 
     + `rerankerThreshold` is the minimum semantic reranker score that's acceptable for inclusion in a response. [Reranker scores](semantic-search-overview.md#how-results-are-scored) range from 1 to 4. Plan on revising this value based on testing and what works for your content.
 
-+ `models` specifies one or more connections to an existing gpt-4o or gpt-4o-mini model. Currently in this preview release, models can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Azure AI Foundry portal or from a command line request. You can use role-based access control instead of API keys for the Azure AI Search connection to the model. For more information, see [How to deploy Azure OpenAI models with Azure AI Foundry](/azure/ai-foundry/how-to/deploy-models-openai).
++ `models` specifies a connection to a [supported chat completion model](#supported-models). In this preview, `models` can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Azure AI Foundry portal or from a command line request. You can use role-based access control instead of API keys for the Azure AI Search connection to the model. For more information, see [How to deploy Azure OpenAI models with Azure AI Foundry](/azure/ai-foundry/how-to/deploy-models-openai).
 
 + `outputConfiguration` gives you control over query execution logic and output.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント作成手順の更新: モデルの変更と説明の改善"
}
```

### Explanation
この修正は、エージェント作成に関する手順文書において、サポートされるモデルの更新と書き方の改善を行ったものです。主に、使用するモデルのバージョンが「gpt-4o-mini」から「gpt-5-mini」に変更され、モデルに関する説明が明確に強化されています。

主な変更点は以下の通りです：
- **モデル名の変更**: サポートされるモデルリストにおいて、従来の「gpt-4o-mini」の代わりに「gpt-5-mini」が使用されるように更新されました。
- **説明の改善**: `models`に関する説明が更新され、「gpt-4o」および「gpt-4o-mini」から「サポートされているチャット完了モデル」へと修正され、より包括的な説明が提供されています。
- **一般的な表現の修正**: 表現が一貫性のある形に改善され、分かりやすさが向上しました。具体的には、「open source model」が「open-source model」に修正されています。
- **新たな設定項目**: `outputConfiguration`という新しい項目が導入され、クエリ実行ロジックと出力制御についての情報が提供されている点も重要です。

以上の変更により、ユーザーは最新のモデルを使用したエージェント作成方法をより良く理解できるようになり、実装に役立つ情報が整理されて提供されています。

## articles/search/search-how-to-upgrade.md{#item-990225}

<details>
<summary>Diff</summary>
````diff
@@ -16,13 +16,13 @@ ms.update-cycle: 180-days
 
 An upgrade brings older search services to the capabilities of new services created in the same region. Specifically, it upgrades the computing power of the underlying service. This one-time operation doesn't introduce breaking changes to your application, and you shouldn't need to change any code.
 
-For [eligible services](#upgrade-eligibility), an upgrade increases the [partition storage](#higher-storage-limits) and [vector index size](#higher-vector-limits) on the same tier at no extra cost.
+For [eligible services](#upgrade-eligibility), an upgrade increases the [partition storage](#higher-storage-limits) and [vector index size](#higher-vector-limits) on the same pricing tier at no extra cost.
+
+This article describes how to upgrade your service in the [Azure portal](https://portal.azure.com/). Alternatively, you can use the [Search Management REST APIs](/rest/api/searchmanagement/) to upgrade your service programmatically. For more information, see [Manage your search service using REST](search-manage-rest.md#upgrade-a-service).
 
 > [!TIP]
 > Looking to [change your pricing tier](search-capacity-planning.md#change-your-pricing-tier)? You can switch between Basic and Standard (S1, S2, and S3) tiers.
 
-This article describes how to upgrade your service in the [Azure portal](https://portal.azure.com/). Alternatively, you can use the [Search Management REST APIs](/rest/api/searchmanagement/) to upgrade your service programmatically. For more information, see [Manage your search service using REST](search-manage-rest.md#upgrade-a-service).
-
 ## About service upgrades
 
 In April 2024, Azure AI Search increased the [storage capacity](search-limits-quotas-capacity.md#service-limits) of newly created search services. Services created before April 2024 saw no capacity changes, so if you wanted larger and faster partitions, you had to create a new service. However, some older services can now be upgraded to benefit from the higher-capacity partitions.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービスアップグレード手順の簡素化と用語の修正"
}
```

### Explanation
この修正は、Azureの検索サービスのアップグレード方法に関する文書に対して行われたもので、内容の明確化と用語の一貫性を図るための変更が含まれています。

主な変更点は以下の通りです：
- **用語の修正**: 「same tier」が「same pricing tier」に修正されており、この変更により、料金階層に関する情報が明確になっています。
- **重複文章の削除**: 以前、サービスのアップグレード手順が2回記載されていましたが、こちらの冗長性が解消され、文章が簡潔になりました。
- **情報の追加**: アップグレード手段に関する情報が追加され、Azureポータルを使用する方法だけでなく、Search Management REST APIを利用したプログラムによるアップグレードについても触れられています。これにより、読者に選択肢が提供されています。
- **TIPセクションの強調**: 料金階層の変更に関するTIPが強調されており、BasicとStandard（S1, S2, S3）の間の切り替えが可能であることが明示されています。

全体として、この修正は文書の可読性を向上させ、アップグレードに関する手順をより明確に示しています。利用者が必要な情報を迅速に得られるように配慮されています。

## articles/search/search-knowledge-source-how-to-blob.md{#item-58d84a}

<details>
<summary>Diff</summary>
````diff
@@ -91,9 +91,9 @@ A response for blob knowledge source might look like the following example.
       "kind": "azureOpenAI",
       "azureOpenAIParameters": {
         "resourceUri": "<REDACTED>",
-        "deploymentId": "gpt-4o-mini",
+        "deploymentId": "gpt-5-mini",
         "apiKey": "<REDACTED>",
-        "modelName": "gpt-4o-mini",
+        "modelName": "gpt-5-mini",
         "authIdentity": null
       }
     },
@@ -177,9 +177,9 @@ A blob knowledge source can include an `ingestionSchedule` that adds scheduling
           "kind": "azureOpenAI",
           "azureOpenAIParameters": {
             "resourceUri": "{{aoai-endpoint}}",
-            "deploymentId": "gpt-4o-mini",
+            "deploymentId": "gpt-5-mini",
             "apiKey": "{{aoai-key}}",
-            "modelName": "gpt-4o-mini",
+            "modelName": "gpt-5-mini",
             "authIdentity": null
           }
         },
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blobナレッジソースのモデルバージョン更新"
}
```

### Explanation
この修正は、Blobナレッジソースに関する文書で、使用されるモデルのバージョンが更新されたことを反映したものです。主な変更点は、すべての関連する箇所で「gpt-4o-mini」から「gpt-5-mini」への変更が行われています。

具体的な変更内容は以下の通りです：
- **モデルIDの更新**: Blobナレッジソースからのレスポンス例や、スケジュール設定のセクションで使用されている「deploymentId」と「modelName」が「gpt-5-mini」に変更されました。これは、最新のモデルを利用することにより、性能や機能の向上を図るためのものです。
- **一貫性の確保**: 同一の情報が複数の箇所で一貫して更新されており、ドキュメント全体での情報の整合性が保たれています。

この変更により、利用者は最新の技術に基づいた正確な情報を得ることができ、AzureのBlobナレッジソースの利用においてより効果的な結果を期待できるようになります。

## articles/search/vector-search-how-to-truncate-dimensions.md{#item-8350a3}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 09/28/2025
+ms.date: 10/08/2025
 ---
 
 # Truncate dimensions using MRL compression
@@ -94,7 +94,7 @@ The following example illustrates a vector search configuration that meets the r
     "compressions": [ 
       { 
         "name": "use-mrl", 
-        "kind": "truncation", 
+        "kind": "binaryQuantization", 
         "rescoringOptions": {
             "enableRescoring": true,
             "defaultOversampling": 10,
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索の設定に関する用語の修正"
}
```

### Explanation
この修正は、ベクトル検索時の次元の切り捨てに関する文書に対するもので、主に日付の更新と用語の変更が含まれています。

具体的な変更内容は以下の通りです：
- **日付の更新**: ドキュメントの最終更新日が「09/28/2025」から「10/08/2025」に変更されました。これは最新の情報を反映するためのもので、文書が最新であることを示しています。
- **用語の修正**: ベクトル検索設定の例において、圧縮タイプの指定が「truncation」から「binaryQuantization」に変更されました。この変更により、より正確な技術用語が使用されており、文書の正確性が向上しています。

全体として、この修正により、文書はより現代的かつ正確な情報を提供するものへと改善されており、利用者が具体的な設定や情報を理解しやすくなっています。


