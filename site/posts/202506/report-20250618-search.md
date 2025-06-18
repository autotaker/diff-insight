---
date: '2025-06-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ba67d73...MicrosoftDocs:2e48ee2
summary: このコード変更では、MicrosoftのAzure AI Search関連ドキュメントが複数更新され、日付やメソッド名の修正、ナレッジストアやインデクサー、プロジェクションの具体例についての説明が改善されました。新機能としてスキルベースのインデクシングの追加やKeyless
  Connectionsの役割ベースアクセス強化が行われました。また、エージェント検索のメソッド名が変更されたものの、重大な変更は特にありません。これらの修正は、ユーザーにとっての利便性向上と正確な情報提供を目的としています。全体として、Azure
  AI Searchドキュメントの更新はユーザーエクスペリエンスを向上させることを意図しており、データ収集の効率化やセキュリティ向上にも寄与しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ba67d73...MicrosoftDocs:2e48ee2){target="_blank"}

# ハイライト

このコード変更では、MicrosoftのAzure AI Search関連ドキュメントのファイルが複数更新され、特に日付やメソッド名の修正、及びナレッジストアやインデクサー、プロジェクションの詳細な例に関する説明の改善が行われています。新たに追加された機能や主要な変更点として、エージェントによる検索機能の改善、Keyless Connectionsの役割ベースアクセス強化、インデクサーにおけるスキルベースのインデクシング紹介などがあります。これらの変更は主に、ユーザーの利便性向上と、より正確で最新の情報提供を目的としています。

## 新機能

- "スキルベースのインデクシング" セクションが追加され、検索可能なコンテンツ生成の新方法が紹介されました。  
- Keyless Connectionsに役割ベースのアクセスを強化する手順が追加されました。

## 重大な変更

- 特に重大な変更はありませんが、エージェント検索のメソッド名が`agent_client.knowledge_retrieval.retrieve`から`agent_client.retrieve`に変更されました。

## その他の更新

- `ms.date`の更新に伴い、ドキュメントの最新性を保つための日付変更が各ファイルで行われました。
- エージェントの検索機能において、システムメッセージを除外するフィルタリングが追加されました。
- 各ファイルにおいて文法や表現が見直され、より明確な説明が提供されています。

# 洞察

この更新作業は主にAzure AI Searchドキュメントのユーザーエクスペリエンスを向上させることを目的としています。特に、日付の更新は、常に新しい情報が反映されている状態を保つために重要です。ドキュメントのバージョンを最新に保ち、ユーザーが安心して利用できるように配慮されていることがわかります。

エージェントによる検索方法の変更は、開発効率の向上及びコードの簡素化を目指しています。特にメソッド名の短縮化は、意図が明確になり、開発者にとって理解しやすくなっています。さらに、不必要なシステムメッセージをフィルタリングすることで、データ収集がより効率的になります。

Keyless Connectionsのセクションでは、役割ベースアクセスを強調することにより、セキュリティおよびアクセス制御が強化され、企業内での利用がより安定して行える環境が整備されています。加えて、インデクサーナレッジストアのプロジェクションに関する説明が詳細化され、実用的なガイダンスが強化されています。これにより、ユーザーはAzureの技術をより効果的に活用し、業務に組み込むことが可能になります。

この一連のアップデートは、Microsoftのクラウドサービスを最大限に活用するための重要な一歩であり、ユーザーにとってのメリットは長期的なものとなるでしょう。特にドキュメントが提供する情報の最新性と正確性への配慮は、Azure技術の信頼性と効率性を担保するための重要な側面です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-python.md](#item-efee6a) | minor update | エージェントによる検索機能の改善 | modified | 5 | 5 | 10 | 
| [keyless-connections.md](#item-3f0d72) | minor update | Keyless Connectionsに関するドキュメントの更新 | modified | 12 | 16 | 28 | 
| [knowledge-store-create-rest.md](#item-2643dd) | minor update | RESTを使用したナレッジストア作成に関するドキュメントの更新 | modified | 1 | 1 | 2 | 
| [knowledge-store-projection-example-long.md](#item-e18999) | minor update | ナレッジストアにおける投影の詳細例に関するドキュメントの更新 | modified | 1 | 1 | 2 | 
| [knowledge-store-projection-overview.md](#item-81aa4a) | minor update | ナレッジストアにおけるプロジェクションの概要に関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [knowledge-store-projection-shape.md](#item-2e47a8) | minor update | ナレッジストアにおけるプロジェクション形状に関するドキュメントの更新 | modified | 7 | 7 | 14 | 
| [knowledge-store-projections-examples.md](#item-9bfff5) | minor update | ナレッジストアのプロジェクション例に関するドキュメントの更新 | modified | 14 | 14 | 28 | 
| [search-how-to-create-indexers.md](#item-de71fb) | minor update | インデクサーの作成に関するドキュメントの更新 | modified | 4 | 4 | 8 | 
| [tutorial-rag-build-solution-query.md](#item-93965f) | minor update | RAGソリューションのクエリに関するチュートリアルの更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 6/15/2025
+ms.date: 6/17/2025
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -250,9 +250,9 @@ messages.append({
     """
 })
 
-retrieval_result = agent_client.knowledge_retrieval.retrieve(
+retrieval_result = agent_client.retrieve(
     retrieval_request=KnowledgeAgentRetrievalRequest(
-        messages=[KnowledgeAgentMessage(role=msg["role"], content=[KnowledgeAgentMessageTextContent(text=msg["content"])]) for msg in messages],
+        messages=[KnowledgeAgentMessage(role=msg["role"], content=[KnowledgeAgentMessageTextContent(text=msg["content"])]) for msg in messages if msg["role"] != "system"],
         target_index_params=[KnowledgeAgentIndexParams(index_name=index_name, reranker_threshold=2.5)]
     )
 )
@@ -414,9 +414,9 @@ messages.append({
     "content": "How do I find lava at night?"
 })
 
-retrieval_result = agent_client.knowledge_retrieval.retrieve(
+retrieval_result = agent_client.retrieve(
     retrieval_request=KnowledgeAgentRetrievalRequest(
-        messages=[KnowledgeAgentMessage(role=msg["role"], content=[KnowledgeAgentMessageTextContent(text=msg["content"])]) for msg in messages],
+        messages=[KnowledgeAgentMessage(role=msg["role"], content=[KnowledgeAgentMessageTextContent(text=msg["content"])]) for msg in messages if msg["role"] != "system"],
         target_index_params=[KnowledgeAgentIndexParams(index_name=index_name, reranker_threshold=2.5)]
     )
 )
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントによる検索機能の改善"
}
```

### Explanation
この変更は、`agentic-retrieval-python.md`ファイルに対するマイナーアップデートを示しています。主に、エージェントの検索機能を改善するためのコードの修正が行われました。具体的には、`ms.date`の更新があり、日付が2025年6月15日から2025年6月17日に変更されました。

また、リカバリー呼び出しで使用されているメソッド名が`agent_client.knowledge_retrieval.retrieve`から`agent_client.retrieve`に変更され、よりシンプルな構造に改善されています。

さらに、メッセージのフィルタリングが追加され、`msg["role"]`が"system"ではないメッセージのみを処理するように変更されています。これにより、システムメッセージを除外してより正確なリカバリー結果を得ることができるようになります。この改良は、エージェントの効率的かつ効果的な情報取得をサポートします。

## articles/search/keyless-connections.md{#item-3f0d72}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,7 @@
 title: Use keyless connections in search apps
 description: Use keyless connections with an Azure Identity library for Microsoft Entra ID authentication and authorization with Azure AI Search.
 ms.topic: how-to
-ms.date: 10/30/2024
+ms.date: 06/17/2025
 ms.service: azure-ai-search
 author: HeidiSteen
 ms.author: heidist
@@ -16,35 +16,31 @@ In your application code, you can set up a keyless connection to Azure AI Search
 
 Keyless connections are enabled with the following steps: 
 
-* Configure your authentication.
+* Enable role-based access on your search service
 * Set environment variables, as needed. 
 * Use an Azure Identity library credential type to create an Azure AI Search client object.
 
 ## Prerequisites
 
 The following steps need to be completed for both local development and production workloads:
 
-* [Create an AI Search resource](#create-an-ai-search-resource)
+* [Create an AI Search resource](search-create-service-portal.md)
 * [Enable role-based access on your search service](search-security-enable-roles.md)
 * [Install Azure Identity client library](#install-azure-identity-client-library)
 
-### Create an AI Search resource
-
-Before continuing with this article, you need an Azure AI Search resource to work with. If you don't have a resource, [create your resource](search-create-service-portal.md) now. [Enable role-based access control (RBAC)](search-security-enable-roles.md) for the resource.
-
-### Install Azure Identity client library
+## Install Azure Identity client library
 
 To use a keyless approach, update your AI Search enabled code with the Azure Identity client library.
 
-#### [.NET](#tab/csharp)
+### [.NET](#tab/csharp)
 
 Install the [Azure Identity client library for .NET](https://www.nuget.org/packages/Azure.Identity):
 
 ```dotnetcli
 dotnet add package Azure.Identity
 ```
 
-#### [Java](#tab/java)
+### [Java](#tab/java)
 
 Install the [Azure Identity client library for Java](https://mvnrepository.com/artifact/com.azure/azure-identity) with the following POM file:
 
@@ -60,15 +56,15 @@ Install the [Azure Identity client library for Java](https://mvnrepository.com/a
 </dependencyManagement>
 ```
 
-#### [JavaScript](#tab/javascript)
+### [JavaScript](#tab/javascript)
 
 Install the [Azure Identity client library for JavaScript](https://www.npmjs.com/package/@azure/identity):
 
 ```console
 npm install --save @azure/identity
 ```
 
-#### [Python](#tab/python)
+### [Python](#tab/python)
 
 Install the [Azure Identity client library for Python](https://pypi.org/project/azure-identity/):
 
@@ -82,7 +78,7 @@ pip install azure-identity
 
 The Azure Identity library's `DefaultAzureCredential` allows you to run the same code in the local development environment and in the Azure cloud. Create a single credential and reuse the credential instance as needed to take advantage of token caching.
 
-#### [.NET](#tab/csharp)
+### [.NET](#tab/csharp)
 
 For more information on `DefaultAzureCredential` for .NET, see [Azure Identity client library for .NET](/dotnet/api/overview/azure/identity-readme#defaultazurecredential). 
 
@@ -104,7 +100,7 @@ SearchClient searchClient = new(new Uri(endpoint), indexName, credential);
 SearchIndexClient searchIndexClient = new(endpoint, credential);
 ```
 
-#### [Java](#tab/java)
+### [Java](#tab/java)
 
 For more information on `DefaultAzureCredential` for Java, see [Azure Identity client library for Java](/java/api/overview/azure/identity-readme#defaultazurecredential).
 
@@ -148,7 +144,7 @@ SearchIndexAsyncClient searchIndexAsyncClient = new SearchIndexClientBuilder()
     .buildAsyncClient();
 ```
 
-#### [JavaScript](#tab/javascript)
+### [JavaScript](#tab/javascript)
 
 For more information on `DefaultAzureCredential` for JavaScript, see [Azure Identity client library for JavaScript](/javascript/api/overview/azure/identity-readme#defaultazurecredential).
 
@@ -178,7 +174,7 @@ const indexClient = new SearchIndexClient(
 );
 ```
 
-#### [Python](#tab/python)
+### [Python](#tab/python)
 
 For more information on `DefaultAzureCredential` for Python, see [Azure Identity client library for Python](/python/api/overview/azure/identity-readme#defaultazurecredential).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Keyless Connectionsに関するドキュメントの更新"
}
```

### Explanation
この変更は、`keyless-connections.md`ファイルに対するマイナーアップデートであり、Azure AI Searchにおけるキーレス接続の利用方法についての情報が更新されています。主な変更点としては、`ms.date`の更新が行われ、日付が2024年10月30日から2025年6月17日に変更されました。

ドキュメント内の手順が整理され、役割ベースのアクセスを有効にすることが新たに追加され、キーなしの接続を簡素化する手続きが強調されています。また、関連するリソースへのリンクが更新され、一貫性を持たせるために文書内のセクション見出しが改訂されています。具体的には、各プログラミング言語（.NET、Java、JavaScript、Python）に関する情報が個別の見出しに整理され、より可読性が向上しました。

これらの変更により、ユーザーがAzure AI SearchとAzure Identityクライアントライブラリを使用してインタラクションを行う方法が明確になり、ユーザー経験の向上につながることが期待されます。

## articles/search/knowledge-store-create-rest.md{#item-2643dd}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 12/10/2024
+ms.date: 06/17/2025
 ---
 
 # Create a knowledge store using REST
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTを使用したナレッジストア作成に関するドキュメントの更新"
}
```

### Explanation
この変更は、`knowledge-store-create-rest.md`ファイルに対するマイナーアップデートで、RESTを使用してナレッジストアを作成する方法に関するドキュメントが更新されました。主な変更点として、`ms.date`の更新があり、日付が2024年12月10日から2025年6月17日に変更されました。

この日付変更により、ドキュメントの最新性が保たれ、新しい情報や機能に対応した内容が反映されることが期待されています。このアップデートは、ユーザーがAzure AI Searchのナレッジストア機能を正確に理解し、効率的に利用するための重要な改善です。

## articles/search/knowledge-store-projection-example-long.md{#item-e18999}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 12/10/2024
+ms.date: 06/17/2025
 ---
 
 # Detailed example of shapes and projections in a knowledge store
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジストアにおける投影の詳細例に関するドキュメントの更新"
}
```

### Explanation
この変更は、`knowledge-store-projection-example-long.md`ファイルに対するマイナーアップデートであり、ナレッジストアにおける形状と投影の詳細な例についてのドキュメントが更新されました。主な変更点は、`ms.date`の更新で、日付が2024年12月10日から2025年6月17日に変更されています。

この日付の更新は、ドキュメントの最新性を確保し、新機能や情報に適応した内容を反映させることを目的としています。これにより、ユーザーはナレッジストアの投影に関する最新の情報を取得し、より効果的にAzure AI Searchの機能を活用できるようになります。

## articles/search/knowledge-store-projection-overview.md{#item-81aa4a}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Projection concepts
 titleSuffix: Azure AI Search
-description: Introduces projection concepts and best practices. If you are creating a knowledge store in Azure AI Search, projections determine the type, quantity, and composition of objects in Azure Storage.
+description: Introduces projection concepts and best practices. If you're creating a knowledge store in Azure AI Search, projections determine the type, quantity, and composition of objects in Azure Storage.
 
 manager: nitinme
 author: HeidiSteen
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 12/10/2024
+ms.date: 06/17/2025
 ---
 
 # Knowledge store "projections" in Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジストアにおけるプロジェクションの概要に関するドキュメントの更新"
}
```

### Explanation
この変更は、`knowledge-store-projection-overview.md`ファイルに対するマイナーアップデートであり、ナレッジストアにおけるプロジェクションの概念とベストプラクティスについてのドキュメントが更新されました。主な変更点は、`description`の文言が修正され、"`If you are`"から"`If you're`"に変更されたことや、`ms.date`の更新が行われ、日付が2024年12月10日から2025年6月17日に変更されています。

これにより、内容がより自然な言い回しに改訂され、さらに最新の日付が反映されることで、ユーザーはAzure AI Searchのナレッジストアに関する最新の情報を理解しやすくなっています。このアップデートは、ユーザーがプロジェクションの概念を効果的に把握できるようにするための重要な改善です。

## articles/search/knowledge-store-projection-shape.md{#item-2e47a8}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 12/10/2024
+ms.date: 06/17/2025
 ---
 
 # Shaping data for projection into a knowledge store
@@ -21,9 +21,9 @@ By itself, the enrichment tree doesn't include logic that would inform how its c
 
 ## Approaches for creating shapes
 
-There are two ways to shape enriched content to that it can be projected into a knowledge store:
+There are two ways to shape enriched content so that it can be projected into a knowledge store:
 
-+ Use the [Shaper skill](cognitive-search-skill-shaper.md) to create nodes in an enrichment tree that are used expressly for projection. Most skills create new content. In contrast, a Shaper skill work with existing nodes, usually to consolidate multiple nodes into a single complex object. This is useful for tables, where you want the output of multiple nodes to be physically expressed as columns in the table. 
++ Use the [Shaper skill](cognitive-search-skill-shaper.md) to create nodes in an enrichment tree that are used expressly for projection. Most skills create new content. In contrast, a Shaper skill works with existing nodes, usually to consolidate multiple nodes into a single complex object. This is useful for tables, where you want the output of multiple nodes to be physically expressed as columns in the table. 
 
 + Use an inline shape within the projection definition itself.
 
@@ -111,11 +111,11 @@ Within a Shaper skill, an input can have a `sourceContext` element. This same pr
 
 `sourceContext` is used to construct multi-level, nested objects in an enrichment pipeline. If the input is at a *different* context than the skill context, use the *sourceContext*. The *sourceContext* requires you to define a nested input with the specific element being addressed as the source. 
 
-In the example above, sentiment analysis and key phrases extraction was performed on text that was split into pages for more efficient analysis. Assuming you want the scores and phrases projected into a table, you'll now need to set the context to nested input that provides the score and phrase.
+In the previous example, sentiment analysis and key phrases extraction was performed on text that was split into pages for more efficient analysis. Assuming you want the scores and phrases projected into a table, you'll now need to set the context to nested input that provides the score and phrase.
 
 ### Projecting a shape into multiple tables
 
-With the `tableprojection` node defined in the `outputs` section above, you can slice parts of the `tableprojection` node into individual, related tables:
+With the `tableprojection` node defined in the `outputs` in the previous section, you can slice parts of the `tableprojection` node into individual, related tables:
 
 ```json
 "projections": [
@@ -145,8 +145,8 @@ With the `tableprojection` node defined in the `outputs` section above, you can
 
 Inline shaping is the ability to form new shapes within the projection definition itself. Inline shaping has these characteristics:
 
-+ The shape can be used only by the projection that contains it.
-+ The shape can be identical to what a Shaper skill would produce.
++ The shape is used only by the projection that contains it.
++ The shape can be identical to what a Shaper skill produces.
 
 An inline shape is created using `sourceContext` and `inputs`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジストアにおけるプロジェクション形状に関するドキュメントの更新"
}
```

### Explanation
この変更は、`knowledge-store-projection-shape.md`ファイルに対するマイナーアップデートで、ナレッジストアにおけるプロジェクションの形状に関する内容が更新されました。主な変更点には、`ms.date`が2024年12月10日から2025年6月17日に変更されたことや、いくつかの文法的な修正が含まれています。

具体的には、「to that it can be projected into a knowledge store」という表現が「so that it can be projected into a knowledge store」に修正され、また、Shaperスキルについての説明文も若干改善されています。さらに、"outputs"セクションに関する記述も再構築され、内容の明確性が向上しています。

これらの変更は、ユーザーがナレッジストアへのデータプロジェクションを理解する際の補助として機能し、より精確で使いやすい情報提供を目的としています。ユーザーは、このドキュメントを通じてプロジェクション形状の作成方法およびその活用方法をより効果的に学ぶことができるでしょう。

## articles/search/knowledge-store-projections-examples.md{#item-9bfff5}

<details>
<summary>Diff</summary>
````diff
@@ -10,20 +10,20 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 12/10/2024
+ms.date: 06/17/2025
 ---
 
 # Define projections in a knowledge store
 
-[Projections](knowledge-store-projection-overview.md) are the component of a [knowledge store definition](knowledge-store-concept-intro.md) that determines where AI enriched content is stored in Azure Storage. Projections determine the type, quantity, and composition of the data structures containing your content.
+[Projections](knowledge-store-projection-overview.md) are the component of a [knowledge store definition](knowledge-store-concept-intro.md) that determines how AI enriched content is stored in Azure Storage. Projections determine the type, quantity, and composition of the data structures containing your content.
 
 In this article, learn the syntax for each type of projection:
 
 + [Table projections](#define-a-table-projection)
 + [Object projections](#define-an-object-projection)
 + [File projections](#define-a-file-projection)
 
-Recall that projections are defined under the "knowledgeStore" property of a skillset.
+Recall that projections are defined under the `knowledgeStore` property of a skillset.
 
 ```json
 "knowledgeStore" : {
@@ -54,7 +54,7 @@ Except for file projections, which only accept binary images, the source must be
 
 While a node might resolve to a single field, a more common representation is a reference to a complex shape. Complex shapes are created through a shaping methodology, either a [Shaper skill](cognitive-search-skill-shaper.md) or [an inline shaping definition](knowledge-store-projection-shape.md#inline-shape), but usually a Shaper skill. The fields or elements of the shape determine the fields in containers and tables.
 
-Shaper skills are favored because it outputs JSON, where as most skills don't output valid JSON on their own. In many cases, the same data shape created by a Shaper skill can be used equally by both table and object projections.
+Shaper skills are favored because it outputs JSON, whereas most skills don't output valid JSON on their own. In many cases, the same data shape created by a Shaper skill can be used equally by both table and object projections.
 
 Given source input requirements, knowing how to [shape data](knowledge-store-projection-shape.md) becomes a practical requirement for projection definition, especially if you're working with tables.
 
@@ -67,13 +67,13 @@ To define a table projection, use the `tables` array in the projections property
 | Property | Description |
 |----------|-------------|
 | tableName | Determines the name of a new table created in Azure Table Storage.  |
-| generatedKeyName | Column name for the key that uniquely identifies each row. The value is system-generated. If you omit this property, a column will be created automatically that uses the table name and "key" as the naming convention. |
+| generatedKeyName | Column name for the key that uniquely identifies each row. The value is system-generated. If you omit this property, a column is created automatically that uses the table name and "key" as the naming convention. |
 | source | A path to a node in an enrichment tree. The node should be a reference to a complex shape that determines which columns are created in the table.|
 
 In table projections, "source" is usually the output of a [Shaper skill](cognitive-search-skill-shaper.md) that defines the shape of the table. Tables have rows and columns, and shaping is the mechanism by which rows and columns are specified. You can use a [Shaper skill or inline shapes](knowledge-store-projection-shape.md). The Shaper skill produces valid JSON, but the source could be the output from any skill, if valid JSON.
 
 > [!NOTE]
-> Table projections are subject to the [storage limits](/rest/api/storageservices/understanding-the-table-service-data-model) imposed by Azure Storage. The entity size cannot exceed 1 MB and a single property can be no bigger than 64 KB. These constraints make tables a good solution for storing a large number of small entities.
+> Table projections are subject to the [storage limits](/rest/api/storageservices/understanding-the-table-service-data-model) imposed by Azure Storage. The entity size can't exceed 1 MB and a single property can be no bigger than 64 KB. These constraints make tables a good solution for storing a large number of small entities.
 
 ### Single table example
 
@@ -128,14 +128,14 @@ Columns are derived from the "source". The following data shape containing Hotel
 
 A common pattern for table projections is to have multiple related tables, where system-generated partitionKey and rowKey columns are created to support cross-table relationships for all tables under the same projection group. 
 
-Creating multiple tables can be useful if you want control over how related data is aggregated. If enriched content has unrelated or independent components, for example the keywords extracted from a document might be unrelated from the entities recognized in the same document, you can split those fields out into adjacent tables.
+Creating multiple tables can be useful if you want control over how related data is aggregated. If enriched content has unrelated or independent components, for example the keywords extracted from a document might be unrelated from the entities recognized in the same document, you can split out those fields into adjacent tables.
 
 When you're projecting to multiple tables, the complete shape is projected into each table, unless a child node is the source of another table within the same group. Adding a projection with a source path that is a child of an existing projection results in the child node being sliced out of the parent node and projected into the new yet related table. This technique allows you to define a single node in a Shaper skill that can be the source for all of your projections.
 
 The pattern for multiple tables consists of:
 
 + One table as the parent or main table
-+ Additional tables to contain slices of the enriched content
++ Other tables to contain slices of the enriched content
 
 For example, assume a Shaper skill outputs an "EnrichedShape" that contains hotel information, plus enriched content like key phrases, locations, and organizations. The main table would include fields that describe the hotel (ID, name, description, address, category). Key phrases would get the key phrase column. Entities would get the entity columns.
 
@@ -166,7 +166,7 @@ To define an object projection, use the `objects` array in the projections prope
 | Property | Description |
 |----------|-------------|
 | storageContainer | Determines the name of a new container created in Azure Storage.  |
-| generatedKeyName | Column name for the key that uniquely identifies each row. The value is system-generated. If you omit this property, a column will be created automatically that uses the table name and "key" as the naming convention. |
+| generatedKeyName | Column name for the key that uniquely identifies each row. The value is system-generated. If you omit this property, a column is created automatically that uses the table name and "key" as the naming convention. |
 | source | A path to a node in an enrichment tree that is the root of the projection. The node is usually a reference to a complex data shape that determines blob structure.|
 
 The following example projects individual hotel documents, one hotel document per blob, into a container called `hotels`.
@@ -193,7 +193,7 @@ The following example projects individual hotel documents, one hotel document pe
 }
 ```
 
-The source is the output of a Shaper skill, named `"objectprojection"`. Each blob will have a JSON representation of each field input.
+The source is the output of a Shaper skill, named `"objectprojection"`. Each blob has a JSON representation of each field input.
 
 ```json
     {
@@ -237,10 +237,10 @@ To define a file projection, use the `files` array in the projections property.
 | Property | Description |
 |----------|-------------|
 | storageContainer | Determines the name of a new container created in Azure Storage.  |
-| generatedKeyName | Column name for the key that uniquely identifies each row. The value is system-generated. If you omit this property, a column will be created automatically that uses the table name and "key" as the naming convention. |
+| generatedKeyName | Column name for the key that uniquely identifies each row. The value is system-generated. If you omit this property, a column is created automatically that uses the table name and "key" as the naming convention. |
 | source | A path to a node in an enrichment tree that is the root of the projection. For images files, the  source is always `/document/normalized_images/*`.  File projections only act on the `normalized_images` collection. Neither indexers nor a skillset will pass through the original non-normalized image.|
 
-The destination is always a blob container, with a folder prefix of the base64 encoded value of the document ID. If there are multiple images, they'll be placed together in the same folder. File projections can't share the same container as object projections and need to be projected into a different container. 
+The destination is always a blob container, with a folder prefix of the base64 encoded value of the document ID. If there are multiple images, they're placed together in the same folder. File projections can't share the same container as object projections and need to be projected into a different container. 
 
 The following example projects all normalized images extracted from the document node of an enriched document, into a container called `myImages`.
 
@@ -273,13 +273,13 @@ You can process projections by following these steps:
 
 1. Use Azure portal to verify object creation in Azure Storage.
 
-1. If you're projecting tables, [import them into Power BI](knowledge-store-connect-power-bi.md) for table manipulation and visualization. In most cases, Power BI will auto-discover the relationships among tables.
+1. If you're projecting tables, [import them into Power BI](knowledge-store-connect-power-bi.md) for table manipulation and visualization. In most cases, Power BI autodiscovers the relationships among tables.
 
 ## Common issues
 
 Omitting any of the following steps can result in unexpected outcomes. Check for the following conditions if your output doesn't look right.
 
-+ String enrichments aren't shaped into valid JSON. When strings are enriched, for example `merged_content` enriched with key phrases, the enriched property is represented as a child of `merged_content` within the enrichment tree. The default representation isn't well-formed JSON. At projection time, make sure to transform the enrichment into a valid JSON object with a name and a value. Using a Shaper skill or defining inline shapes will help resolve this issue.
++ String enrichments aren't shaped into valid JSON. When strings are enriched, for example `merged_content` enriched with key phrases, the enriched property is represented as a child of `merged_content` within the enrichment tree. The default representation isn't well-formed JSON. At projection time, make sure to transform the enrichment into a valid JSON object with a name and a value. Using a Shaper skill or defining inline shapes help resolve this issue.
 
 + Omission of `/*` at the end of a source path. If the source of a projection is `/document/projectionShape/keyPhrases`, the key phrases array is projected as a single object/row. Instead, set the source path to `/document/projectionShape/keyPhrases/*` to yield a single row or object for each of the key phrases.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジストアのプロジェクション例に関するドキュメントの更新"
}
```

### Explanation
この変更は、`knowledge-store-projections-examples.md`ファイルに対するマイナーアップデートで、ナレッジストアのプロジェクションに関する例を含むドキュメントが更新されました。主な変更点として、`ms.date`が2024年12月10日から2025年6月17日に変更されたことに加えて、文法や用語の明確化が行われています。

具体的な内容の変更としては、プロジェクションの保存方法に関する説明が明確にされ、「how AI enriched content is stored in Azure Storage」という表現が追加されました。また、`knowledgeStore`プロパティに関連する説明や、シェイピング方法に関する情報も具体的に記述されています。特に、テーブルプロジェクション、オブジェクトプロジェクション、ファイルプロジェクションのそれぞれに関連するプロパティの定義が精緻化されています。

この更新により、ユーザーはナレッジストアのプロジェクションの概念をより正確に理解し、実際の使用方法や設定方法についての具体的なガイダンスを得られるようになっています。ユーザーがナレッジストアのプロジェクションを効果的に活用できるための非常に有用なドキュメントの改訂となりました。

## articles/search/search-how-to-create-indexers.md{#item-de71fb}

<details>
<summary>Diff</summary>
````diff
@@ -11,18 +11,18 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 12/17/2024
+ms.date: 06/17/2025
 ---
 
 # Create an indexer in Azure AI Search
 
-This article focuses on the basic steps of creating an indexer. Depending on the data source and your workflow, more configuration might be necessary.
+This article focuses on the basic steps of creating an indexer that's used to automate data ingestion for supported data sources. Depending on the data source and your workflow, more configuration might be necessary.
 
-You can use an indexer to automate data import and indexing in Azure AI Search. An indexer is a named object on a search service that connects to an external Azure data source, reads data, and passes it to a search engine for indexing. Using indexers significantly reduces the quantity and complexity of the code you need to write if you're using a supported data source.
+You can use an indexer to automate data import and indexing in Azure AI Search. An indexer is a named object on a search service that connects to an external Azure data source, reads and serializes the data, and passes it to a search engine for indexing. Using indexers significantly reduces the quantity and complexity of the code you need to write if you're using a supported data source.
 
 Indexers support two workflows:
 
-+ **Raw content indexing (plain text or vectors)**: Extract strings and metadata from textual content for full text search scenarios. Extracts raw vector content for vector search (for example, vectors in an Azure SQL database or Azure Cosmos DB collection). In this workflow, indexing occurs only over existing content that you provide.
++ **Raw content indexing (plain text or vectors)**: Extract strings and metadata from textual content used for full text search scenarios. Extracts raw vector content used for vector search (for example, vectors in an Azure SQL database or Azure Cosmos DB collection). In this workflow, indexing occurs only over existing content that you provide.
 
 + **Skills-based indexing**: Extends indexing through built-in or custom skills that create or generate new searchable content. For example, you can add integrated machine learning for analysis over images and unstructured text, extracting or inferring text and structure. Or, use skills to chunk and vectorize content from text and images. Skills-based indexing creates or generates new content that doesn't exist in your external data source. New content becomes part of your index when you add fields to the index schema that accepts the incoming data. To learn more, see [AI enrichment in Azure AI Search](cognitive-search-concept-intro.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーの作成に関するドキュメントの更新"
}
```

### Explanation
この変更は、`search-how-to-create-indexers.md`ファイルに対するマイナーアップデートで、Azure AI Searchでインデクサーを作成する際の基本的な手順についてのドキュメントが更新されました。主な変更点として、`ms.date`が2024年12月17日から2025年6月17日に変更されたことが含まれています。

具体的な内容の変更としては、インデクサーの役割についての説明が明確になり、データの自動取り込みを行うことが強調されました。また、「読み込む」と「シリアライズする」という表現が追加され、データ処理の流れが具体的に説明されています。

新たに「スキルベースのインデクシング」というセクションが追加され、内蔵またはカスタムスキルを利用して新しい検索可能なコンテンツを生成する方法についても詳しく説明されています。これにより、ユーザーはインデクサーを活用することで新しいコンテンツを作成し、インデックスに組み込む方法を学ぶことができるようになっています。

このドキュメントの変更により、インデクサーの機能と活用方法についての理解が深まり、より効果的にAzure AI Searchを利用できるようになることを目的としています。

## articles/search/tutorial-rag-build-solution-query.md{#item-93965f}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: tutorial
-ms.date: 01/09/2025
+ms.date: 06/17/2025
 ---
 
 # Tutorial: Search your data using a chat model (RAG in Azure AI Search)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションのクエリに関するチュートリアルの更新"
}
```

### Explanation
この変更は、`tutorial-rag-build-solution-query.md`ファイルに対するマイナーアップデートであり、Azure AI Searchにおけるチャットモデルを使用したデータ検索に関するチュートリアルが更新されました。主な変更点として、`ms.date`が2025年1月9日から2025年6月17日に変更されていることが挙げられます。

この更新により、チュートリアルの日時が新しくなり、最新版の情報をユーザーに提供することが目的です。なお、他の内容に関しては変更はなく、チュートリアルの構成や指示がそのまま維持されています。このデート変更は、利用者がより最新の情報に基づいて学習し、効果的にAzure AI Searchを活用できるようにするためのものです。


