---
date: '2026-01-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b8d6e71...MicrosoftDocs:a88a880
summary: このコードの変更では、ドキュメントの明確化やメタデータの更新、クイックスタートガイドの修正、さらには新しいドキュメント削除に関するガイドの追加が行われました。これにより、ドキュメントの整合性や最新性が向上し、ユーザーが情報にアクセスしやすくなります。特に、新たに追加されたガイドは、Azure
  AI Searchにおけるドキュメント削除手順を詳しく説明しており、データ管理の能力を強化します。一方、再インデックス作成のドキュメントには重要な変更があり、一部の情報が削除されているため、ユーザーにとっての影響が懸念されます。全体として、これらの更新はAzure
  AI Searchの機能理解を深め、開発者にとって有益な環境を提供することを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b8d6e71...MicrosoftDocs:a88a880){target="_blank"}

<format>
# ハイライト

このコードの変更では、複数のドキュメントにおける表現の明確化、メタデータの更新、多数のクイックスタートガイドの内容修正、及び新しいガイドの追加が行われました。これによって、ドキュメント全体の整合性、最新性、ユーザーが情報にアクセスしやすくなるような改善が図られています。特に、新しい機能として、ドキュメント削除に関する詳細なガイドが加わりました。

## 新機能
- `search-how-to-delete-documents.md`の追加: Azure AI Searchにおけるドキュメント削除手順に関する新しいガイドが提供されました。

## ブレイキングチェンジ
- `search-howto-reindex.md`の大幅なリファクタリング: 再インデックス作成に関する内容が整理され、一部のセクションが削除されました。

## その他のアップデート
- 複数ドキュメントにわたる表現の微調整。
- クイックスタートガイドの日付の更新とメタデータの追加。
- リンクの修正とナビゲーションの簡略化。

# インサイト

この一連の変更は、Azure AI Searchに関するドキュメントをより洗練された形にするためのものであり、利用者が情報に迅速かつ正確にアクセスすることを意図しています。特に日付の更新とメタデータの追加は、ドキュメントを常に最新の技術仕様に準拠させることを目的としており、これは開発者のユーザーエクスペリエンスの向上に貢献します。

新たに追加されたドキュメント削除のガイドは、Azureの検索インデックス管理における重要なイニシアチブであり、ユーザーがより効果的にデータを管理する能力を強化します。この詳細な手順の導入は、ユーザーが個別のユースケースでの削除を理解し、実装を容易にするための重大なステップです。

一方で、再インデックス作成のドキュメントに対するブレイキングチェンジは、特定の情報が削除されることで、特定のユーザーにとっては情報が不足する可能性があります。このような変更は、ユーザーが再インデックス作成に関する特定のユースケースを考慮する設計が必要であり、注意が必要です。

全体的に、これらの更新は、Azure AI Searchの機能とその利用における理解を深めさせ、開発者が効率よく作業を進めるための環境を提供することを目指しています。また、このようなドキュメントの進化はサービスの有用性を高め、開発者にとっても大きな利益となるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | ドキュメントの表現を微調整 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-csharp.md](#item-f93ed3) | minor update | C# クイックスタート文書の更新 | modified | 17 | 68 | 85 | 
| [agentic-retrieval-java.md](#item-4e2c55) | minor update | Java クイックスタート文書の表現修正 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-javascript.md](#item-715283) | minor update | JavaScript クイックスタート文書の更新 | modified | 15 | 15 | 30 | 
| [agentic-retrieval-python.md](#item-efee6a) | minor update | Python クイックスタート文書の内容整理 | modified | 17 | 113 | 130 | 
| [agentic-retrieval-rest.md](#item-3df373) | minor update | REST API クイックスタート文書の更新 | modified | 20 | 9 | 29 | 
| [agentic-retrieval-typescript.md](#item-e6370b) | minor update | TypeScript クイックスタートドキュメントの更新 | modified | 15 | 15 | 30 | 
| [search-get-started-vector-dotnet.md](#item-8f2f1b) | minor update | ベクトル検索の .NET クイックスタートドキュメントの更新 | modified | 203 | 189 | 392 | 
| [search-get-started-vector-java.md](#item-a3db97) | minor update | Java用ベクトル検索クイックスタートのドキュメント更新 | modified | 84 | 56 | 140 | 
| [search-get-started-vector-javascript.md](#item-d0387c) | minor update | JavaScript用ベクトル検索のクイックスタートドキュメントの更新 | modified | 93 | 64 | 157 | 
| [search-get-started-vector-python.md](#item-53085f) | minor update | Python用ベクトル検索のクイックスタートドキュメントの更新 | modified | 105 | 101 | 206 | 
| [search-get-started-vector-rest.md](#item-c7d261) | minor update | REST APIを用いたベクトル検索のクイックスタートドキュメントの更新 | modified | 206 | 193 | 399 | 
| [search-get-started-vector-typescript.md](#item-9b3bc8) | minor update | TypeScriptを使用したベクトル検索のクイックスタートドキュメントの更新 | modified | 98 | 66 | 164 | 
| [semantic-ranker-java.md](#item-93a05a) | minor update | Javaを使用したセマンティックランキングのクイックスタートドキュメントの更新 | modified | 7 | 7 | 14 | 
| [search-get-started-agentic-retrieval.md](#item-4a40f4) | minor update | エージェントリトリーバルのクイックスタートドキュメントの更新 | modified | 4 | 2 | 6 | 
| [search-get-started-vector.md](#item-4984d9) | minor update | ベクター検索のクイックスタートドキュメントの更新 | modified | 3 | 1 | 4 | 
| [search-how-to-delete-documents.md](#item-556879) | new feature | ドキュメント削除に関する新しいガイドの追加 | added | 308 | 0 | 308 | 
| [search-how-to-index-azure-blob-one-to-many.md](#item-30a1f9) | minor update | Azure Blob インデックスの多対多マッピングに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [search-how-to-index-logic-apps.md](#item-e25907) | minor update | Logic Apps インデックスに関するドキュメントの更新 | modified | 1 | 1 | 2 | 
| [search-how-to-index-sql-database.md](#item-86d873) | minor update | SQLデータベースインデックスに関するドキュメントの更新 | modified | 1 | 1 | 2 | 
| [search-how-to-load-search-index.md](#item-a72573) | minor update | 検索インデックスのデータ読み込みに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [search-howto-reindex.md](#item-46738a) | breaking change | 再インデックス作成に関するドキュメントの大幅なリファクタリング | modified | 2 | 38 | 40 | 
| [search-howto-run-reset-indexers.md](#item-fb10c8) | minor update | インデックスリセットに関するドキュメントの修正 | modified | 2 | 2 | 4 | 
| [search-query-access-control-rbac-enforcement.md](#item-d24df7) | minor update | クエリアクセス制御とRBAC施行に関するドキュメントの修正 | modified | 5 | 4 | 9 | 
| [search-security-rbac.md](#item-a5d129) | minor update | RBACに関するドキュメントの更新 | modified | 8 | 2 | 10 | 
| [toc.yml](#item-c4768f) | minor update | 目次ファイルの更新 | modified | 3 | 1 | 4 | 
| [vector-search-how-to-create-index.md](#item-97c769) | minor update | ベクトルインデックス作成に関するドキュメントの改善 | modified | 24 | 24 | 48 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -265,7 +265,7 @@ print(f"Documents uploaded to index '{index_name}'")
 
 A knowledge source is a reusable reference to source data. The following code creates a knowledge source that targets the index you previously created.
 
-`source_data_fields` specifies which index fields are included in citation references. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+`source_data_fields` specifies which index fields are included in citation references. This example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
 
 For more information about this step, see [Create a search index knowledge source](agentic-knowledge-source-how-to-search-index.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントの表現を微調整"
}
```

### Explanation
このコードの変更において、`agentic-retrieval-how-to-create-pipeline.md` ファイルの一部が修正されました。具体的には、`source_data_fields` に関する説明文が若干変更されました。元の文では「Our example includes only human-readable fields...」という表現が使われていましたが、新しい文では「This example includes only human-readable fields...」と書き換えられています。この変更は、文をより一般的な形にし、特定の例ではなく、より広範な内容を示すようにしています。この修正により、ドキュメントの明確さと一貫性が向上しています。

## articles/search/includes/quickstarts/agentic-retrieval-csharp.md{#item-f93ed3}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,9 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/14/2025
+ms.date: 01/14/2026
+ms.custom: dev-focus
+ai-usage: ai-assisted
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -486,70 +488,7 @@ Reference Type: KnowledgeBaseSearchIndexReference
   "SourceData": {},
   "RerankerScore": 2.6344998
 }
-Reference Type: KnowledgeBaseSearchIndexReference
-{
-  "DocKey": "earth_at_night_508_page_194_verbalized",
-  "Id": "1",
-  "ActivitySource": 3,
-  "SourceData": {},
-  "RerankerScore": 2.630955
-}
-Reference Type: KnowledgeBaseSearchIndexReference
-{
-  "DocKey": "earth_at_night_508_page_105_verbalized",
-  "Id": "3",
-  "ActivitySource": 2,
-  "SourceData": {},
-  "RerankerScore": 2.5884187
-}
-Reference Type: KnowledgeBaseSearchIndexReference
-{
-  "DocKey": "earth_at_night_508_page_189_verbalized",
-  "Id": "4",
-  "ActivitySource": 3,
-  "SourceData": {},
-  "RerankerScore": 2.465418
-}
-Reference Type: KnowledgeBaseSearchIndexReference
-{
-  "DocKey": "earth_at_night_508_page_193_verbalized",
-  "Id": "6",
-  "ActivitySource": 3,
-  "SourceData": {},
-  "RerankerScore": 2.4560246
-}
-Reference Type: KnowledgeBaseSearchIndexReference
-{
-  "DocKey": "earth_at_night_508_page_174_verbalized",
-  "Id": "2",
-  "ActivitySource": 1,
-  "SourceData": {},
-  "RerankerScore": 2.3254027
-}
-Reference Type: KnowledgeBaseSearchIndexReference
-{
-  "DocKey": "earth_at_night_508_page_176_verbalized",
-  "Id": "5",
-  "ActivitySource": 1,
-  "SourceData": {},
-  "RerankerScore": 2.257256
-}
-Reference Type: KnowledgeBaseSearchIndexReference
-{
-  "DocKey": "earth_at_night_508_page_177_verbalized",
-  "Id": "7",
-  "ActivitySource": 1,
-  "SourceData": {},
-  "RerankerScore": 2.1968744
-}
-Reference Type: KnowledgeBaseSearchIndexReference
-{
-  "DocKey": "earth_at_night_508_page_125_verbalized",
-  "Id": "8",
-  "ActivitySource": 2,
-  "SourceData": {},
-  "RerankerScore": 2.086579
-}
+... // Trimmed for brevity
 Response:
 ... // Trimmed for brevity
 Activity:
@@ -575,7 +514,7 @@ Now that you've run the code, let's break down the key steps:
 
 ### Create a search index
 
-In Azure AI Search, an index is a structured collection of data. The following code defines an index named `earth-at-night`, which you previously specified using the `indexName` variable.
+In Azure AI Search, an index is a structured collection of data. The following code defines an index named `earth-at-night`.
 
 The index schema contains fields for document identification and page content, embeddings, and numbers. The schema also includes configurations for semantic ranking and vector search, which uses your `text-embedding-3-large` deployment to vectorize text and match documents based on semantic or conceptual similarity.
 
@@ -652,6 +591,8 @@ await indexClient.CreateOrUpdateIndexAsync(index);
 Console.WriteLine($"Index '{indexName}' created or updated successfully.");
 ```
 
+Reference: [SearchField](/dotnet/api/azure.search.documents.indexes.models.searchfield), [SimpleField](/dotnet/api/azure.search.documents.indexes.models.simplefield), [VectorSearch](/dotnet/api/azure.search.documents.indexes.models.vectorsearch), [SemanticSearch](/dotnet/api/azure.search.documents.indexes.models.semanticsearch), [SearchIndex](/dotnet/api/azure.search.documents.indexes.models.searchindex), [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient)
+
 ### Upload documents to the index
 
 Currently, the `earth-at-night` index is empty. The following code populates the index with JSON documents from [NASA's Earth at Night e-book](https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json). As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
@@ -678,11 +619,13 @@ await searchIndexingBufferedSender.FlushAsync();
 Console.WriteLine($"Documents uploaded to index '{indexName}' successfully.");
 ```
 
+Reference: [SearchClient](/dotnet/api/azure.search.documents.searchclient), [SearchIndexingBufferedSender](/dotnet/api/azure.search.documents.searchindexingbufferedsender-1)
+
 ### Create a knowledge source
 
 A knowledge source is a reusable reference to source data. The following code defines a knowledge source named `earth-knowledge-source` that targets the `earth-at-night` index.
 
-`SourceDataFields` specifies which index fields are included in citation references. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+`SourceDataFields` specifies which index fields are included in citation references. This example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
 
 ```csharp
 // Create a knowledge source
@@ -698,9 +641,11 @@ await indexClient.CreateOrUpdateKnowledgeSourceAsync(indexKnowledgeSource);
 Console.WriteLine($"Knowledge source '{knowledgeSourceName}' created or updated successfully.");
 ```
 
+Reference: [SearchIndexKnowledgeSource](/dotnet/api/azure.search.documents.indexes.models.searchindexknowledgesource)
+
 ### Create a knowledge base
 
-To target `earth-knowledge-source` and your `gpt-5-mini` deployment at query time, you need a knowledge base. The following code defines a knowledge base named `earth-knowledge-base`, which you previously specified using the `knowledgeBaseName` variable.
+To target `earth-knowledge-source` and your `gpt-5-mini` deployment at query time, you need a knowledge base. The following code defines a knowledge base named `earth-knowledge-base`.
 
 `OutputMode` is set to `AnswerSynthesis`, enabling natural-language answers that cite the retrieved documents and follow the provided `AnswerInstructions`.
 
@@ -730,6 +675,8 @@ await indexClient.CreateOrUpdateKnowledgeBaseAsync(knowledgeBase);
 Console.WriteLine($"Knowledge base '{knowledgeBaseName}' created or updated successfully.");
 ```
 
+Reference: [KnowledgeBaseAzureOpenAIModel](/dotnet/api/azure.search.documents.indexes.models.knowledgebaseazureopenaimodel), [KnowledgeBase](/dotnet/api/azure.search.documents.indexes.models.knowledgebase)
+
 ### Set up messages
 
 Messages are the input for the retrieval route and contain the conversation history. Each message includes a role that indicates its origin, such as `system` or `user`, and content in natural language. The LLM you use determines which roles are valid.
@@ -791,6 +738,8 @@ messages.Add(new Dictionary<string, string>
 });
 ```
 
+Reference: [KnowledgeBaseRetrievalClient](/dotnet/api/azure.search.documents.knowledgebases.knowledgebaseretrievalclient?view=azure-dotnet-preview&preserve-view=true), [KnowledgeBaseRetrievalRequest](/dotnet/api/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest?view=azure-dotnet-preview&preserve-view=true)
+
 #### Review the response, activity, and references
 
 The following code displays the response, activity, and references from the retrieval pipeline, where:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# クイックスタート文書の更新"
}
```

### Explanation
このコードの変更は、`agentic-retrieval-csharp.md` ファイルにおける重要な修正を含んでいます。主な変更点は、文書の更新日が「11/14/2025」から「01/14/2026」に変更されたこと、および新たに `ms.custom` と `ai-usage` のメタデータが追加されたことです。これにより、文書が最新の情報を反映する形になり、開発者向けのカスタム情報やAIの利用に関する指針が明確になります。

また、たくさんの行が削除され、コードスニペットが簡略化されています。具体的には、いくつかの冗長な例が排除され、主要なコードやコンセプトが強調されています。これにより、ドキュメントの読みやすさが向上し、ユーザーにとって必要な情報により迅速にアクセスできるようになっています。新しい参照リンクも追加され、ユーザーが関連情報にアクセスするのが容易になりました。全体的に、構造と内容の精緻化が図られ、開発者がより効果的に情報を活用できるよう意図されています。

## articles/search/includes/quickstarts/agentic-retrieval-java.md{#item-4e2c55}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.date: 11/05/2025
 
 In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview.md) to create a conversational search experience powered by large language models (LLMs) and your proprietary data. Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries in parallel, and extracts grounding data from documents indexed in Azure AI Search. The output is intended for integration with agentic and custom chat solutions.
 
-Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
+Although you can use your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
 > [!TIP]
 > The Java version of this quickstart uses the 2025-05-01-preview REST API version, which uses the previous "knowledge agent" terminology and doesn't support the latest features available in the 2025-11-01-preview. To use these features, see the C#, Python, or REST version.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java クイックスタート文書の表現修正"
}
```

### Explanation
このコードの変更は、`agentic-retrieval-java.md` ファイルにおいて、文書内の表現を若干調整することを目的としています。具体的には、「provide your own data」という表現が「use your own data」に変更されています。この変更は、ユーザーに対してより親しみやすく、使いやすい印象を与えるためのものです。

全体の文脈は変わっていませんが、表現の改善により、ユーザーが自身のデータを使用することが促進されています。この種の微調整は文書の可読性を向上させ、ユーザーがコンテンツをより良く理解できるようにするための重要な要素です。文書でも含まれている推薦情報（TIP）では、Java バージョンが古い REST API バージョンを使用していることに言及し、最新の機能を利用するには他の言語バージョンを参照するように指示しています。

## articles/search/includes/quickstarts/agentic-retrieval-javascript.md{#item-715283}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,9 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 12/19/2025
+ms.date: 01/14/2026
+ms.custom: dev-focus
+ai-usage: ai-assisted
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -539,19 +541,7 @@ Reference Type: searchIndex
   "rerankerScore": 2.6692379,
   "docKey": "earth_at_night_508_page_174_verbalized"
 }
-Reference Type: searchIndex
-{
-  "type": "searchIndex",
-  "id": "1",
-  "activitySource": 3,
-  "sourceData": {
-    "id": "earth_at_night_508_page_186_verbalized",
-    "page_chunk": "## Appendix A\n\n### NASA's Black Marble Product Suite\n\nNASA's Black Marble product suite provides estimates of daily nighttime lights and other intrinsic surface optical properties of Earth at night. The product is based on the Day/Night Band (DNB) sensor of the Visible Infrared Imaging Radiometer Suite (VIIRS) instrument onboard the Suomi National Polar-orbiting Partnership (NPP) satellite. The VIIRS DNB is a highly sensitive, low-light sensor capable of measuring daily global nighttime light emissions and reflections, allowing users to identify sources and intensities of these artificial lights, and monitor changes over a period of time. Like any optical sensor, the principal challenge in using VIIRS DNB data is to account for variations in light captured by the sensor. Certainly, there are variations in the sources and intensity of anthropogenic light due to changing human processes like urbanization, oil and gas production, nighttime commercial fishing, and infrastructure development. However, these processes can only be studied when other naturally-occurring factors that influence nighttime lights are removed. For example, variations in lunar lighting due to consistent changes in Moon phase cause fluctuations in the amount of light shining on Earth. Similarly, land-cover dynamics (e.g., seasonal vegetation, snow and ice cover), as well as atmospheric conditions (e.g., clouds, aerosols, airglow, and auroras), influence the intensity of the light captured by the sensor as it travels over various parts of the world.\n\nTo realize the full potential of the VIIRS DNB time series record for nighttime lights applications, NASA's Black Marble product suite was developed, building on a history of 20 years of research on how light changes when it reflects off of surfaces with different angular and spectral properties. Through complex modeling, scientists can now predict how moonlight, snow, vegetation, terrain, and clouds impact the lights we see from space, allowing for more accurate assessments of human and environmental activity at night.\n\n<!-- PageFooter=\"170 Earth at Night\" -->",
-    "page_number": 186
-  },
-  "rerankerScore": 2.5997617,
-  "docKey": "earth_at_night_508_page_186_verbalized"
-}
+... // Trimmed for brevity
 
 ❓ Follow-up question: How do I find lava at night?
 
@@ -676,6 +666,8 @@ const searchClient = new SearchClient(process.env.AZURE_SEARCH_ENDPOINT, 'earth_
 await searchIndexClient.createOrUpdateIndex(index);
 ```
 
+Reference: [SearchField](/javascript/api/@azure/search-documents/searchfield), [VectorSearch](/javascript/api/@azure/search-documents/vectorsearch), [SemanticSearch](/javascript/api/@azure/search-documents/semanticsearch), [SearchIndex](/javascript/api/@azure/search-documents/searchindex), [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient), [SearchClient](/javascript/api/@azure/search-documents/searchclient), [DefaultAzureCredential](/javascript/api/@azure/identity/defaultazurecredential)
+
 ### Upload documents to the index
 
 Currently, the `earth-at-night` index is empty. The following code populates the index with JSON documents from [NASA's Earth at Night e-book](https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json). As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
@@ -716,11 +708,13 @@ while (count !== documents.length) {
 console.log(`✓ All ${documents.length} documents indexed successfully!`);
 ```
 
+Reference: [SearchIndexingBufferedSender](/javascript/api/@azure/search-documents/searchindexingbufferedsender)
+
 ### Create a knowledge source
 
 A knowledge source is a reusable reference to source data. The following code defines a knowledge source named `earth-knowledge-source` that targets the `earth-at-night` index.
 
-`source_data_fields` specifies which index fields are included in citation references. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+`source_data_fields` specifies which index fields are included in citation references. This example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
 
 ```javascript
 await searchIndexClient.createKnowledgeSource({
@@ -739,6 +733,8 @@ await searchIndexClient.createKnowledgeSource({
 console.log(`✅ Knowledge source 'earth-knowledge-source' created successfully.`);
 ```
 
+Reference: [SearchIndexKnowledgeSource](/javascript/api/@azure/search-documents/searchindexknowledgesource)
+
 ### Create a knowledge base
 
 To target `earth-knowledge-source` and your `gpt-5-mini` deployment at query time, you need a knowledge base. The following code defines a knowledge base named `earth-knowledge-base`.
@@ -770,6 +766,8 @@ await searchIndexClient.createKnowledgeBase({
 console.log(`✅ Knowledge base 'earth-knowledge-base' created successfully.`);
 ```
 
+Reference: [KnowledgeBase](/javascript/api/@azure/search-documents/knowledgebase)
+
 ### Run the retrieval pipeline
 
 You're ready to run agentic retrieval. The following code sends a two-part user query to `earth-knowledge-base`, which:
@@ -818,6 +816,8 @@ const retrievalRequest = {
 const result = await knowledgeRetrievalClient.retrieveKnowledge(retrievalRequest);
 ```
 
+Reference: [KnowledgeRetrievalClient](/javascript/api/@azure/search-documents/knowledgeretrievalclient), [KnowledgeBaseRetrievalRequest](/javascript/api/@azure/search-documents/knowledgebaseretrievalrequest)
+
 ### Review the response, activity, and references
 
 The following code displays the response, activity, and references from the retrieval pipeline, where:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript クイックスタート文書の更新"
}
```

### Explanation
この変更は、`agentic-retrieval-javascript.md` ファイルの文書において、いくつかの重要な更新が行われたことを示しています。主な変更内容として、文書の更新日が「12/19/2025」から「01/14/2026」に変更され、さらに新しいメタデータとして `ms.custom` と `ai-usage` が追加されました。これにより、文書がより現代的かつ開発者向けの情報を反映するようになります。

コードセクションでは、特定の詳細や冗長な情報が削除され、情報の要点を強調するために整理されています。具体的には、いくつかのコード例に関連する説明が簡略化され、読者が素早く理解できるようになっています。新しい参照リンクが追加され、ユーザーが関連する API ドキュメントに簡単にアクセスできるようになったのも特徴です。

これらの修正により、ユーザーは JavaScript を使用したエージェント検索体験について、より効率的に学び、実装を進められるよう配慮されています。また、内容の整頓とリンクの追加によって、リソースのナビゲーションが向上し、開発者が洞察を得やすくなることが期待されています。

## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,9 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/10/2025
+ms.date: 01/14/2026
+ms.custom: dev-focus
+ai-usage: ai-assisted
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -428,115 +430,7 @@ references_content:
     "reranker_score": 2.722408,
     "doc_key": "earth_at_night_508_page_105_verbalized"
   },
-  {
-    "type": "searchIndex",
-    "id": "3",
-    "activity_source": 2,
-    "source_data": {
-      "id": "earth_at_night_508_page_104_verbalized",
-      "page_chunk": "<!-- PageHeader=\"Urban Structure\" -->\n\n### Location of Phoenix, Arizona\n\nThe image depicts a globe highlighting the location of Phoenix, Arizona, in the southwestern United States, marked with a blue pinpoint on the map of North America. Phoenix is situated in the central part of Arizona, which is in the southwestern region of the United States.\n\n---\n\n### Grid of City Blocks-Phoenix, Arizona\n\nLike many large urban areas of the central and western United States, the Phoenix metropolitan area is laid out along a regular grid of city blocks and streets. While visible during the day, this grid is most evident at night, when the pattern of street lighting is clearly visible from the low-Earth-orbit vantage point of the ISS.\n\nThis astronaut photograph, taken on March 16, 2013, includes parts of several cities in the metropolitan area, including Phoenix (image right), Glendale (center), and Peoria (left). While the major street grid is oriented north-south, the northwest-southeast oriented Grand Avenue cuts across the three cities at image center. Grand Avenue is a major transportation corridor through the western metropolitan area; the lighting patterns of large industrial and commercial properties are visible along its length. Other brightly lit properties include large shopping centers, strip malls, and gas stations, which tend to be located at the intersections of north-south and east-west trending streets.\n\nThe urban grid encourages growth outwards along a city's borders by providing optimal access to new real estate. Fueled by the adoption of widespread personal automobile use during the twentieth century, the Phoenix metropolitan area today includes 25 other municipalities (many of them largely suburban and residential) linked by a network of surface streets and freeways.\n\nWhile much of the land area highlighted in this image is urbanized, there are several noticeably dark areas. The Phoenix Mountains are largely public parks and recreational land. To the west, agricultural fields provide a sharp contrast to the lit streets of residential developments. The Salt River channel appears as a dark ribbon within the urban grid.\n\n\n<!-- PageFooter=\"Earth at Night\" -->\n<!-- PageNumber=\"88\" -->",
-      "page_number": 104
-    },
-    "reranker_score": 2.6451337,
-    "doc_key": "earth_at_night_508_page_104_verbalized"
-  },
-  {
-    "type": "searchIndex",
-    "id": "1",
-    "activity_source": 1,
-    "source_data": {
-      "id": "earth_at_night_508_page_174_verbalized",
-      "page_chunk": "<!-- PageHeader=\"Holiday Lights\" -->\n\n## Holiday Lights\n\n### Bursting with Holiday Energy-United States\n\nNASA researchers found that nighttime lights in the United States shine 20 to 50 percent brighter in December due to holiday light displays and other activities during Christmas and New Year's when compared to light output during the rest of the year.\n\nThe next five maps (see also pages 161-163), created using data from the VIIRS DNB on the Suomi NPP satellite, show changes in lighting intensity and location around many major cities, comparing the nighttime light signals from December 2012 and beyond.\n\n---\n\n#### Figure 1. Location Overview\n\nA map of the western hemisphere with a marker indicating the mid-Atlantic region of the eastern United States, where the study of holiday lighting intensity was focused.\n\n---\n\n#### Figure 2. Holiday Lighting Intensity: Mid-Atlantic United States (2012\u20132014)\n\nA map showing Maryland, New Jersey, Delaware, Virginia, West Virginia, Ohio, Kentucky, Tennessee, North Carolina, South Carolina, and surrounding areas. Major cities labeled include Washington, D.C., Richmond, Norfolk, and Raleigh.\n\nThe map uses colors to indicate changes in holiday nighttime lighting intensity between 2012 and 2014:\n\n- **Green/bright areas**: More holiday lighting (areas shining 20\u201350% brighter in December).\n- **Yellow areas**: No change in lighting.\n- **Dim/grey areas**: Less holiday lighting.\n\nKey observations from the map:\n\n- The Washington, D.C. metropolitan area shows significant increases in lighting during the holidays, extending into Maryland and Virginia.\n- Urban centers such as Richmond (Virginia), Norfolk (Virginia), Raleigh (North Carolina), and clusters in Tennessee and South Carolina also experience notable increases in light intensity during December.\n- Rural areas and the interiors of West Virginia, Kentucky, and North Carolina show little change or less holiday lighting, corresponding to population density and urbanization.\n\n**Legend:**\n\n| Holiday Lighting Change | Color on Map   |\n|------------------------|---------------|\n| More                   | Green/bright  |\n| No Change              | Yellow        |\n| Less         
-          | Dim/grey      |\n\n_The scale bar indicates a distance of 100 km for reference._\n\n---\n\n<!-- PageFooter=\"158 Earth at Night\" -->",
-      "page_number": 174
-    },
-    "reranker_score": 2.476761,
-    "doc_key": "earth_at_night_508_page_174_verbalized"
-  },
-  {
-    "type": "searchIndex",
-    "id": "2",
-    "activity_source": 3,
-    "source_data": {
-      "id": "earth_at_night_508_page_124_verbalized",
-      "page_chunk": "# Urban Development\n\n## Figure: Location Highlight on Globe\n\nThis figure depicts a globe focused on North America, with a marker pinpointing the central region of the United States. The highlighted location represents the geographical focus of the text discussion on US urban development and transportation networks.\n\n---\n\n## Urban Development\n\n### Lighting Paths\u2014Across the United States\n\nThe United States has more miles of roads than any other nation in the world\u20144.1 million miles (6.6 million kilometers) to be precise, which is roughly 40 percent more than second-ranked India. About 47,000 miles (75,639 kilometers) of those roads are part of the Interstate Highway System, established by President Dwight Eisenhower in the 1950s. The country/region also has 127,000 miles (204,000 kilometers) of railroad tracks and about 25,000 miles (40,000 kilometers) of navigable rivers and canals (not including the Great Lakes). The imprint of that transportation web becomes easy to see at night.\n\nThe VIIRS DNB on the Suomi NPP satellite acquired this nighttime view (top image, right) of the continental United States on October 1, 2013. The roadway map (bottom image, right) traces the path of the major interstate highways, railroads, and rivers of the United States. Comparing the two images, you quickly see how the cities and settlements align with the transportation corridors. In the early days of the republic, post roads and toll roads for horse-drawn carts and carriages were built to connect eastern cities like Boston, New York, Baltimore, and Philadelphia, though relatively few travelers made the long, unlit journeys. Railroads became the dominant transportation method for people and cargo in the middle of the nineteenth century, establishing longer links across the Nation and waypoints across the Midwest, the Great Plains, and the Rockies. Had nighttime satellite images existed in that era, they probably would show only dim pearls of light around major cities in the east and scattered across the country/region; the strands of steel tracks and cobbled roads that connected them would be invisible from space.\n\nEventually, cars and trucks became the dominant form of transportation in the United States. Drivers then needed roads and lighting to keep them safe on those roads. As the Nation grew in the twentieth century, the development of new cities and suburbs often conformed to the path of the interstate highways, adding light along the paths between the cities.\n\nOver the years, the length of navigable rivers has been a constant, as is their relative lack of light. Even today the only light seems to be the occasional port cities along riverbanks and the light of ships themselves.\n\n---\n\n**Table: Summary of U.S. Transportation Infrastructure**\n\n| Infrastructure Type     | Total Mileage (mi) | Total Mileage (km) |\n|------------------------|--------------------|--------------------|\n| Roads (All)            | 4,100,000          | 6,600,000          |\n| Interstate Highways    | 47,000             | 75,639             |\n| Railroads              | 127,000            | 204,000            |\n| Navigable Rivers/Canals| 25,000             | 40,000             |\n\n---\n\n<!-- PageFooter=\"108 Earth at Night\" -->",
-      "page_number": 124
-    },
-    "reranker_score": 2.466304,
-    "doc_key": "earth_at_night_508_page_124_verbalized"
-  },
-  {
-    "type": "searchIndex",
-    "id": "4",
-    "activity_source": 1,
-    "source_data": {
-      "id": "earth_at_night_508_page_176_verbalized",
-      "page_chunk": "# Holiday Lights\n\n## Figure 1: Location Marker on Globe\n\n**Description:**  \nA world map focused on the Western Hemisphere, with a marker placed in the eastern United States. This image serves to indicate the geographic focus of the following data and discussion about holiday lighting patterns, particularly those observed in the United States.\n\n---\n\nHoliday lights increase most dramatically in the suburbs and outskirts of major cities, where there is more yard space and a prevalence of single-family homes. Central urban areas do not see as large an increase in lighting, but they still experience a brightening of 20 to 30 percent during the holidays. This pattern holds true across the U.S., which remains ethnically and religiously diverse but participates in a nationally shared tradition of increased holiday lighting during holiday seasons.\n\nBeyond the cultural implications, this trend has significant consequences for energy consumption. The availability of a daily, global dynamic dataset of nighttime lights offers new insights into the broad societal forces influencing energy decisions. As noted by the Intergovernmental Panel on Climate Change, improvements in energy efficiency and conservation are essential to reducing greenhouse gas emissions. Examining daily nightlight data provides a valuable perspective on urban and suburban life, helping to reveal the underlying patterns and drivers of energy use.\n\n*(Images continue on pages 161-163)*\n\n---\n\n*Page 160 Earth at Night*",
-      "page_number": 176
-    },
-    "reranker_score": 2.3416197,
-    "doc_key": "earth_at_night_508_page_176_verbalized"
-  },
-  {
-    "type": "searchIndex",
-    "id": "6",
-    "activity_source": 1,
-    "source_data": {
-      "id": "earth_at_night_508_page_175_verbalized",
-      "page_chunk": "# Holiday Lights\n\nFrom 2013 to the average light output for the rest of 2012 to 2014, the change in light usage is subtle on any given night. However, when averaged over days and weeks, the pattern becomes more perceptible. Areas where light usage increased in December are marked in green, areas with little change are marked in yellow, and areas where less light was used are marked in red.\n\nThe light output from 70 U.S. cities was examined as a first step toward determining patterns in urban energy use. Researchers found that light intensity increased by 30 to 50 percent in December in many areas, which may be related to holiday lighting.\n\n---\n\n## Figure 1: Location Reference\n\nA globe highlights the southeastern region of the United States, pinpointing the area of interest for the study of holiday light usage, focusing on states like Tennessee, North Carolina, South Carolina, Georgia, and Alabama.\n\n---\n\n## Figure 2: Holiday Lighting Patterns in the Southeastern United States (2012\u20132014)\n\nThis map highlights several cities in the southeastern United States, including Nashville, Charlotte, Columbia, Birmingham, and Atlanta. The states of Tennessee, North Carolina, South Carolina, Alabama, and Georgia are outlined, along with the Atlantic Ocean to the east.\n\n### Key Observations:\n- The most significant concentrations of nighttime lighting are seen in major metropolitan areas, with Atlanta having the largest and most intense area of light.\n- Other notable clusters of increased light output are visible in Nashville, Charlotte, Birmingham, and Columbia.\n- The map reflects changes in light usage during December of 2012\u20132014, with \u201cmore\u201d lighting (green shading) concentrated around urban areas, indicating an increase due to holiday lighting displays.\n\n**Map Details:**\n- Time frame: 2012\u20132014\n- Locations marked: Nashville (Tennessee), Charlotte (North Carolina), Columbia (South Carolina), Birmingham (Alabama), Atlanta (Georgia)\n- Scale: 100 km bar provided\n- North directional arrow included\n\n---\n\n### Legend:\n- **Green Shading**: Areas where light usage increased in December (likely due to holiday lights)\n- **Yellow Shading**: Areas with little change in light usage\n- **Red Shading**: Areas where less light was used\n\n---\n\n#### Page Footer: \u201cno change\u201d\n#### Page Number: 159",
-      "page_number": 175
-    },
-    "reranker_score": 2.3052866,
-    "doc_key": "earth_at_night_508_page_175_verbalized"
-  },
-  {
-    "type": "searchIndex",
-    "id": "9",
-    "activity_source": 1,
-    "source_data": {
-      "id": "earth_at_night_508_page_177_verbalized",
-      "page_chunk": "# Holiday Lights\n\n## Holiday Lighting in Florida (2012\u20132014)\n\nThis figure presents a nighttime satellite map of Florida, highlighting changes in holiday lighting between 2012 and 2014. The map covers major urban areas including Jacksonville, Orlando, Tampa Bay, and Miami, with the Gulf of Mexico to the west.\n\nKey observations from the figure:\n- The map displays areas of increased, decreased, or unchanged outdoor lighting intensity during the holiday season.\n- Major metropolitan regions such as Miami, Tampa Bay, Orlando, and Jacksonville show noticeable concentrations of holiday lighting, with many surrounding areas experiencing changes in brightness compared to the non-holiday period.\n- Color coding (not described in the image but referenced):  \n  - **Less**: Areas where holiday lighting decreased  \n  - **No change**: Areas where lighting remained stable  \n  - **More**: Areas where holiday lighting increased\n\n**Legend:**\n- The figure includes a scale bar indicating a span of 100 km for distance estimation.\n- The map is oriented with north at the top.\n\n**Geographic Labels:**\n- Jacksonville (northeast Florida)\n- Orlando (central Florida)\n- Tampa Bay (west-central Florida)\n- Miami (southeast Florida)\n- The Gulf of Mexico (to the west of the peninsula)\n\n**Takeaway:**\nThe map visualizes spatial patterns in holiday lighting, indicating that urban and suburban areas in Florida experience substantial increases in nighttime brightness during the holiday period, particularly in and around major cities.\n\n<!-- PageNumber=\"161\" -->",
-      "page_number": 177
-    },
-    "reranker_score": 2.2241132,
-    "doc_key": "earth_at_night_508_page_177_verbalized"
-  },
-  {
-    "type": "searchIndex",
-    "id": "5",
-    "activity_source": 3,
-    "source_data": {
-      "id": "earth_at_night_508_page_12_verbalized",
-      "page_chunk": "## Preface\n\nTo keen observers, the nocturnal Earth is not pitch black, featureless, or static. The stars and the Moon provide illumination that differs from, and complements, daylight. Natural Earth processes such as volcanic eruptions, auroras, lightning, and meteors entering the atmosphere generate localized visible light on timescales ranging from subsecond (lightning), to days, weeks (forest fires), and months (volcanic eruptions).\n\nMost interesting and unique (as far as we know) to Earth, is the nighttime visible illumination emitted from our planet that is associated with human activities. Whether purposefully designed to banish darkness (such as lighting for safety, industrial activities, commerce, and transportation) or a secondary result of (such as gas flares associated with mining and hydrocarbon extraction activities, or nocturnal commercial fishing), anthropogenic sources of nighttime light are often broadly distributed in space and sustained in time\u2014over years and even decades. Because these light sources are inextricably tied to human activities and societies, extensive and long-term measurement and monitoring of Earth's anthropogenic nocturnal lights can provide valuable insights into the spatial distribution of our species and the ways in which society is changing\u2014and is changed by\u2014the environment on a wide range of time scales.\n\nOver the past four decades, sensitive imaging instruments have been operated on low-Earth-orbiting satellites to measure natural and human-caused visible nocturnal illumination, both reflected and Earth-generated. The satellite sensors provide unique imagery: global coverage yet with high spatial resolution, and frequent measurements over long periods of time.\n\nThe combined, multisatellite global nocturnal illumination dataset contains a treasure trove of unique information about our planet and our species\u2014and the",
-      "page_number": 12
-    },
-    "reranker_score": 2.128052,
-    "doc_key": "earth_at_night_508_page_12_verbalized"
-  },
-  {
-    "type": "searchIndex",
-    "id": "7",
-    "activity_source": 3,
-    "source_data": {
-      "id": "earth_at_night_508_page_125_verbalized",
-      "page_chunk": "# Urban Development\n\n**Date:** October 1, 2013\n\n---\n\n## Figure: Urban Development and Infrastructure in the United States\n\nThis figure comprises two maps of the continental United States, highlighting the patterns of urban development and infrastructure.\n\n### Top Panel: Nighttime Lights Map (October 1, 2013)\n\nThis map displays the United States as seen from space at night on October 1, 2013. Major observations include:\n\n- A dense concentration of bright spots representing urban and suburban areas with prominent lighting, especially along the east coast, the Midwest (notably around Chicago), Texas, and California.\n- The west and central parts of the country/region, such as the Rocky Mountains and deserts, appear much darker, indicating sparse population and fewer urban centers.\n- The boundaries of the United States are outlined for reference.\n- Major urban corridors are clearly visible, including the heavily lit regions running from Boston through New York City, Philadelphia, Baltimore, D.C., Atlanta, and further south, as well as the line of cities from Los Angeles through southern California.\n\n### Bottom Panel: Major Transport and River Networks\n\nThis map outlines the primary interstate highways, railroad lines, and major river systems in the continental United States, using different colors to distinguish among them:\n\n| Feature    | Color       | Description                                                                       |\n|------------|-------------|-----------------------------------------------------------------------------------|\n| Interstate | Red         | Key high-speed roadways, forming a vast national network and connecting cities     |\n| Railroad   | Green       | Major rail lines paralleling some highway routes, providing freight and passenger service |\n| River      | Blue        | Major river systems used historically for transport, industry, and urban siting    |\n\n- The locations of interstate highways closely follow the distribution of nighttime lights, as seen in the top panel.\n- Railroad networks are especially dense in the Midwest and northeast, regions with both high population density and industrial activity.\n- Major rivers, such as the Mississippi, Missouri, and Ohio, are marked in blue, reflecting their importance for historical urban development.\n\n**Scale:** Both maps include a scale bar representing 500 km and a North arrow for orientation.\n\n---\n\n**Summary:**  \nThe figure visually demonstrates the relationship between urban development (as observed through nighttime satellite imagery) and the underlying networks of interstates, railroads, and rivers that have historically influenced the growth and connectivity of American cities. Most urbanized and densely lit areas correspond to nodes and crossroads within this transportation and river network.\n\n---\n\n**Page 109**",
-      "page_number": 125
-    },
-    "reranker_score": 2.108246,
-    "doc_key": "earth_at_night_508_page_125_verbalized"
-  },
-  {
-    "type": "searchIndex",
-    "id": "8",
-    "activity_source": 2,
-    "source_data": {
-      "id": "earth_at_night_508_page_179_verbalized",
-      "page_chunk": "# Holiday Lights\n\n## Figure 1: Geographic Context of Holiday Lighting Study\n\nThis figure shows a map of the globe focused on North America, with a blue marker pointing to the region in the southwestern United States. This highlighted area includes parts of California, Nevada, and Arizona, encompassing the cities of Los Angeles, San Diego, Las Vegas, and Phoenix. This is the region of the study of holiday lighting.\n\n---\n\n## Figure 2: Changes in Holiday Lighting (2012\u20132014)\n\nThis figure is a satellite map of the southwestern United States and northwestern Mexico, annotated with state and city names:\n\n- **California** (including Los Angeles and San Diego)\n- **Nevada** (including Las Vegas)\n- **Arizona** (including Phoenix)\n- **Mexico** (including Tijuana)\n\nThe map shows holiday lighting patterns, using color to indicate change in light intensity during the holiday period (presumably Christmas season) between 2012 and 2014.\n\n### Map Legend\n\n| Color      | Meaning                     |\n|------------|-----------------------------|\n| Greenish   | More holiday lighting       |\n| Yellow     | No change in lighting       |\n| Red        | Less holiday lighting       |\n\n### Observations\n\n- Major urban areas such as Los Angeles, San Diego, Las Vegas, and Phoenix show increased lighting during the holiday period (marked primarily in green).\n- Some areas show no significant change, especially in less densely populated zones.\n- A few small areas may show a decrease in holiday lighting (if red is present).\n\n- The scale of the map includes a reference bar showing 50 km for distance.\n\n---\n\n### Holiday Lighting Change Key\n\n- **Less** (Red)\n- **No change** (Yellow)\n- **More** (Green)\n\n---\n\n<!-- PageNumber=\"163\" -->",
-      "page_number": 179
-    },
-    "reranker_score": 2.1016884,
-    "doc_key": "earth_at_night_508_page_179_verbalized"
-  }
+  ... // Trimmed for brevity
 ]
 Retrieved content from 'earth-knowledge-base' successfully.
 response_content:
@@ -570,7 +464,7 @@ Now that you've run the code, let's break down the key steps:
 
 ### Create a search index
 
-In Azure AI Search, an index is a structured collection of data. The following code defines an index named `earth-at-night`, which you previously specified using the `index_name` variable.
+In Azure AI Search, an index is a structured collection of data. The following code defines an index named `earth-at-night`.
 
 The index schema contains fields for document identification and page content, embeddings, and numbers. The schema also includes configurations for semantic ranking and vector search, which uses your `text-embedding-3-large` deployment to vectorize text and match documents based on semantic similarity.
 
@@ -620,6 +514,8 @@ index_client.create_or_update_index(index)
 print(f"Index '{index_name}' created or updated successfully.")
 ```
 
+Reference: [SearchField](/python/api/azure-search-documents/azure.search.documents.indexes.models.searchfield), [VectorSearch](/python/api/azure-search-documents/azure.search.documents.indexes.models.vectorsearch), [SemanticSearch](/python/api/azure-search-documents/azure.search.documents.indexes.models.semanticsearch), [SearchIndex](/python/api/azure-search-documents/azure.search.documents.indexes.models.searchindex), [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient)
+
 ### Upload documents to the index
 
 Currently, the `earth-at-night` index is empty. The following code populates the index with JSON documents from [NASA's Earth at Night e-book](https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json). As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
@@ -635,11 +531,13 @@ with SearchIndexingBufferedSender(endpoint=search_endpoint, index_name=index_nam
 print(f"Documents uploaded to index '{index_name}' successfully.")
 ```
 
+Reference: [SearchIndexingBufferedSender](/python/api/azure-search-documents/azure.search.documents.searchindexingbufferedsender)
+
 ### Create a knowledge source
 
 A knowledge source is a reusable reference to source data. The following code defines a knowledge source named `earth-knowledge-source` that targets the `earth-at-night` index.
 
-`source_data_fields` specifies which index fields are included in citation references. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+`source_data_fields` specifies which index fields are included in citation references. This example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
 
 ```python
 # Create a knowledge source
@@ -657,9 +555,11 @@ index_client.create_or_update_knowledge_source(knowledge_source=ks)
 print(f"Knowledge source '{knowledge_source_name}' created or updated successfully.")
 ```
 
+Reference: [SearchIndexKnowledgeSource](/python/api/azure-search-documents/azure.search.documents.indexes.models.searchindexknowledgesource)
+
 ### Create a knowledge base
 
-To target `earth-knowledge-source` and your `gpt-5-mini` deployment at query time, you need a knowledge base. The following code defines a knowledge base named `earth-knowledge-base`, which you previously specified using the `knowledge_base_name` variable.
+To target `earth-knowledge-source` and your `gpt-5-mini` deployment at query time, you need a knowledge base. The following code defines a knowledge base named `earth-knowledge-base`.
 
 `output_mode` is set to `ANSWER_SYNTHESIS`, enabling natural-language answers that cite the retrieved documents and follow the provided `answer_instructions`.
 
@@ -688,6 +588,8 @@ index_client.create_or_update_knowledge_base(knowledge_base)
 print(f"Knowledge base '{knowledge_base_name}' created or updated successfully.")
 ```
 
+Reference: [KnowledgeBase](/python/api/azure-search-documents/azure.search.documents.indexes.models.knowledgebase)
+
 ### Set up messages
 
 Messages are the input for the retrieval route and contain the conversation history. Each message includes a role that indicates its origin, such as `system` or `user`, and content in natural language. The LLM you use determines which roles are valid.
@@ -755,6 +657,8 @@ result = agent_client.retrieve(retrieval_request=req)
 print(f"Retrieved content from '{knowledge_base_name}' successfully.")
 ```
 
+Reference: [KnowledgeBaseRetrievalClient](/python/api/azure-search-documents/azure.search.documents.knowledgebases.knowledgebaseretrievalclient), [KnowledgeBaseRetrievalRequest](/python/api/azure-search-documents/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest)
+
 #### Review the response, activity, and references
 
 The following code displays the response, activity, and references from the retrieval pipeline, where:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python クイックスタート文書の内容整理"
}
```

### Explanation
この変更は、`agentic-retrieval-python.md` ファイルにおける大幅な改訂を示しており、文書全体の読みやすさと情報の整理が目的です。最も顕著な変更点として、更新日が「11/10/2025」から「01/14/2026」に更新され、新たに `ms.custom` と `ai-usage` のメタデータが追加されています。

内容の修正では、多くの古い情報が削除され、代わりに要点を強調するために新しい構成要素が追加されました。例えば、コードスニペットの請求や詳しい情報が、簡潔さを保ちつつ有用性を向上させる形で見直されています。また、各セクションに関連する API 参照リンクが増加しており、開発者が必要な情報に迅速にアクセスできるようになっています。

このような大幅な削除と整理は、読者が Python を使用してエージェント検索を実装する際に、無駄な情報に惑わされることなく、重要なポイントに集中できるようにするためのものであると考えられます。これにより、ユーザーは文書内の内容を効果的に理解し、プロジェクトの実装に活かすことができるようになります。

## articles/search/includes/quickstarts/agentic-retrieval-rest.md{#item-3df373}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,9 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 12/05/2025
+ms.date: 01/14/2026
+ms.custom: dev-focus
+ai-usage: ai-assisted
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -13,7 +15,7 @@ In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview
 
 A *knowledge base* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the knowledge base outputs raw content from your sources, but this quickstart uses the answer synthesis output mode for natural-language answer generation.
 
-Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
+Although you can use your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
 > [!TIP]
 > Want to get started right away? See the [azure-search-rest-samples](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-agentic-retrieval) GitHub repository.
@@ -387,7 +389,7 @@ Now that you've run the code, let's break down the key steps:
 
 ### Create a search index
 
-In Azure AI Search, an index is a structured collection of data. The following code uses [Indexes - Create (REST API)](/rest/api/searchservice/indexes/create) to define an index named `earth-at-night`, which you previously specified using the `@index-name` variable.
+In Azure AI Search, an index is a structured collection of data. The following code defines an index named `earth-at-night`.
 
 The index schema contains fields for document identification and page content, embeddings, and numbers. The schema also includes configurations for semantic ranking and vector search, which uses your `text-embedding-3-large` deployment to vectorize text and match documents based on semantic similarity.
 
@@ -467,12 +469,13 @@ Authorization: Bearer {{token}}
 }
 ```
 
+Reference: [Indexes - Create](/rest/api/searchservice/indexes/create)
+
 ### Upload documents to the index
 
-Currently, the `earth-at-night` index is empty. The following code uses [Documents - Index (REST API)](/rest/api/searchservice/documents/index) to populate the index with JSON documents from NASA's Earth at Night e-book. As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
+Currently, the `earth-at-night` index is empty. The following code populates the index with JSON documents from NASA's Earth at Night e-book. As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
 
 ```HTTP
-
 ### Upload documents
 POST {{search-url}}/indexes/{{index-name}}/docs/index?api-version={{api-version}}  HTTP/1.1
 Content-Type: application/json
@@ -502,11 +505,13 @@ Authorization: Bearer {{token}}
 }
 ```
 
+Reference: [Documents - Index](/rest/api/searchservice/documents/index)
+
 ### Create a knowledge source
 
-A knowledge source is a reusable reference to source data. The following code uses [Knowledge Sources - Create (REST API)](/rest/api/searchservice/knowledge-sources/create?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to define a knowledge source named `earth-knowledge-source` that targets the `earth-at-night` index.
+A knowledge source is a reusable reference to source data. The following code defines a knowledge source named `earth-knowledge-source` that targets the `earth-at-night` index.
 
-`sourceDataFields` specifies which index fields are included in citation references. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+`sourceDataFields` specifies which index fields are included in citation references. This example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
 
 ```HTTP
 ### Create a knowledge source
@@ -529,9 +534,11 @@ Authorization: Bearer {{token}}
 }
 ```
 
+Reference: [Knowledge Sources - Create](/rest/api/searchservice/knowledge-sources/create?view=rest-searchservice-2025-11-01-preview&preserve-view=true)
+
 ### Create a knowledge base
 
-To target your `earth-knowledge-source` and `gpt-5-mini` deployment at query time, you need a knowledge base. The following code uses [Knowledge Bases - Create (REST API)](/rest/api/searchservice/knowledge-bases/create?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to define a base named `earth-knowledge-base`, which you previously specified using the `@knowledge-base-name` variable.
+To target your `earth-knowledge-source` and `gpt-5-mini` deployment at query time, you need a knowledge base. The following code defines a base named `earth-knowledge-base`.
 
 `outputMode` is set to `answerSynthesis`, enabling natural-language answers that cite the retrieved documents and follow the provided `answerInstructions`.
 
@@ -563,9 +570,11 @@ Authorization: Bearer {{token}}
 }
 ```
 
+Reference: [Knowledge Bases - Create](/rest/api/searchservice/knowledge-bases/create?view=rest-searchservice-2025-11-01-preview&preserve-view=true)
+
 ### Run the retrieval pipeline
 
-You're ready to run agentic retrieval. The following code uses [Knowledge Retrieval - Retrieve (REST API)](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to send a two-part user query to `earth-knowledge-base`, which:
+You're ready to run agentic retrieval. The following code sends a two-part user query to `earth-knowledge-base`, which:
 
 1. Analyzes the entire conversation to infer the user's information need.
 1. Decomposes the compound query into focused subqueries.
@@ -606,6 +615,8 @@ Authorization: Bearer {{token}}
 }
 ```
 
+Reference: [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true)
+
 The output should contain the following components:
 
 + `response` provides a synthesized, LLM-generated answer to the query that cites the retrieved documents. When answer synthesis isn't enabled, this section contains content extracted directly from the documents.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST API クイックスタート文書の更新"
}
```

### Explanation
この変更は、`agentic-retrieval-rest.md` ファイルにおける文書の重要な更新を示しています。主に、ドキュメントの日付が「12/05/2025」から「01/14/2026」に変更され、新たに `ms.custom` と `ai-usage` のメタデータが追加されたことで、内容がより最新の技術トレンドに反映されています。

文書のオーバーホールにより、いくつかのセクションで文言が改善され、ユーザーが自分のデータを使用できることが明記されています。また、元の文書に比べて、各コードスニペットに関連する REST API のリンクが新たに追加されたことで、開発者が具体的なリファレンスにすぐにアクセスできるように工夫されています。

具体的には、インデックスや知識ソースの作成、ドキュメントのアップロード、知識ベースの設定といった基本的なステップに関する説明が簡潔に整理され、それぞれのセクションに関連する具体的な API を指すリンクが設けられています。これにより、ユーザーは読みやすさと情報の的確さを享受しながら、迅速に導入を進められるようになります。

全体的に、この更新は実用的な情報とリファレンスを強化し、ユーザーがエージェント検索の機能を効果的に利用できるようにすることを目的としています。

## articles/search/includes/quickstarts/agentic-retrieval-typescript.md{#item-e6370b}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,9 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 12/19/2025
+ms.date: 01/14/2026
+ms.custom: dev-focus
+ai-usage: ai-assisted
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -598,19 +600,7 @@ Reference Type: searchIndex
   "rerankerScore": 2.6692379,
   "docKey": "earth_at_night_508_page_174_verbalized"
 }
-Reference Type: searchIndex
-{
-  "type": "searchIndex",
-  "id": "1",
-  "activitySource": 3,
-  "sourceData": {
-    "id": "earth_at_night_508_page_186_verbalized",
-    "page_chunk": "## Appendix A\n\n### NASA's Black Marble Product Suite\n\nNASA's Black Marble product suite provides estimates of daily nighttime lights and other intrinsic surface optical properties of Earth at night. The product is based on the Day/Night Band (DNB) sensor of the Visible Infrared Imaging Radiometer Suite (VIIRS) instrument onboard the Suomi National Polar-orbiting Partnership (NPP) satellite. The VIIRS DNB is a highly sensitive, low-light sensor capable of measuring daily global nighttime light emissions and reflections, allowing users to identify sources and intensities of these artificial lights, and monitor changes over a period of time. Like any optical sensor, the principal challenge in using VIIRS DNB data is to account for variations in light captured by the sensor. Certainly, there are variations in the sources and intensity of anthropogenic light due to changing human processes like urbanization, oil and gas production, nighttime commercial fishing, and infrastructure development. However, these processes can only be studied when other naturally-occurring factors that influence nighttime lights are removed. For example, variations in lunar lighting due to consistent changes in Moon phase cause fluctuations in the amount of light shining on Earth. Similarly, land-cover dynamics (e.g., seasonal vegetation, snow and ice cover), as well as atmospheric conditions (e.g., clouds, aerosols, airglow, and auroras), influence the intensity of the light captured by the sensor as it travels over various parts of the world.\n\nTo realize the full potential of the VIIRS DNB time series record for nighttime lights applications, NASA's Black Marble product suite was developed, building on a history of 20 years of research on how light changes when it reflects off of surfaces with different angular and spectral properties. Through complex modeling, scientists can now predict how moonlight, snow, vegetation, terrain, and clouds impact the lights we see from space, allowing for more accurate assessments of human and environmental activity at night.\n\n<!-- PageFooter=\"170 Earth at Night\" -->",
-    "page_number": 186
-  },
-  "rerankerScore": 2.5997617,
-  "docKey": "earth_at_night_508_page_186_verbalized"
-}
+... // Trimmed for brevity
 
 ❓ Follow-up question: How do I find lava at night?
 
@@ -735,6 +725,8 @@ const searchClient = new SearchClient<EarthAtNightDocument>(process.env.AZURE_SE
 await searchIndexClient.createOrUpdateIndex(index);
 ```
 
+Reference: [SearchField](/javascript/api/@azure/search-documents/searchfield), [VectorSearch](/javascript/api/@azure/search-documents/vectorsearch), [SemanticSearch](/javascript/api/@azure/search-documents/semanticsearch), [SearchIndex](/javascript/api/@azure/search-documents/searchindex), [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient), [SearchClient](/javascript/api/@azure/search-documents/searchclient), [DefaultAzureCredential](/javascript/api/@azure/identity/defaultazurecredential)
+
 ### Upload documents to the index
 
 Currently, the `earth-at-night` index is empty. The following code populates the index with JSON documents from [NASA's Earth at Night e-book](https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json). As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
@@ -775,11 +767,13 @@ while (count !== documents.length) {
 console.log(`✓ All ${documents.length} documents indexed successfully!`);
 ```
 
+Reference: [SearchIndexingBufferedSender](/javascript/api/@azure/search-documents/searchindexingbufferedsender)
+
 ### Create a knowledge source
 
 A knowledge source is a reusable reference to source data. The following code defines a knowledge source named `earth-knowledge-source` that targets the `earth-at-night` index.
 
-`source_data_fields` specifies which index fields are included in citation references. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+`source_data_fields` specifies which index fields are included in citation references. This example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
 
 ```typescript
 await searchIndexClient.createKnowledgeSource({
@@ -798,6 +792,8 @@ await searchIndexClient.createKnowledgeSource({
 console.log(`✅ Knowledge source 'earth-knowledge-source' created successfully.`);
 ```
 
+Reference: [SearchIndexKnowledgeSource](/javascript/api/@azure/search-documents/searchindexknowledgesource)
+
 ### Create a knowledge base
 
 To target `earth-knowledge-source` and your `gpt-5-mini` deployment at query time, you need a knowledge base. The following code defines a knowledge base named `earth-knowledge-base`.
@@ -829,6 +825,8 @@ await searchIndexClient.createKnowledgeBase({
 console.log(`✅ Knowledge base 'earth-knowledge-base' created successfully.`); 
 ```
 
+Reference: [KnowledgeBase](/javascript/api/@azure/search-documents/knowledgebase)
+
 ### Run the retrieval pipeline
 
 You're ready to run agentic retrieval. The following code sends a two-part user query to `earth-knowledge-base`, which:
@@ -877,6 +875,8 @@ const retrievalRequest = {
 const result = await knowledgeRetrievalClient.retrieveKnowledge(retrievalRequest);
 ```
 
+Reference: [KnowledgeRetrievalClient](/javascript/api/@azure/search-documents/knowledgeretrievalclient), [KnowledgeBaseRetrievalRequest](/javascript/api/@azure/search-documents/knowledgebaseretrievalrequest)
+
 ### Review the response, activity, and references
 
 The following code displays the response, activity, and references from the retrieval pipeline, where:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScript クイックスタートドキュメントの更新"
}
```

### Explanation
この変更は、`agentic-retrieval-typescript.md` ファイルにおける文書の全体的な更新を反映しています。主なポイントとして、文書の日付が「12/19/2025」から「01/14/2026」に変更され、新たに `ms.custom` と `ai-usage` のメタデータが追加されています。これにより、最新の技術動向に沿った内容となっています。

また、文中ではサンプルコードのセクションに関連するリンクが増加しており、特に Azure 機能に関連する API リファレンスが追加されています。これにより、開発者は必要な情報をすぐに取得でき、実際のコードにアクセスがしやすくなっております。具体的には、検索クライアント、インデックス、知識ソース、知識ベース、及びリトリーバルパイプラインに関する具体的な API リファレンスリンクが設けられています。

さらに、一部の冗長な情報が削除され、全体的に文書が簡潔になったことで、ユーザーがエージェント検索の実装方法をより理解しやすくなっています。これにより、ユーザーは容易に導入を進め、効果的に Azure の機能を活用できるようになります。

## articles/search/includes/quickstarts/search-get-started-vector-dotnet.md{#item-8f2f1b}

<details>
<summary>Diff</summary>
````diff
@@ -4,122 +4,126 @@ author: rotabor
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 01/14/2026
+ms.custom: dev-focus
+ai-usage: ai-assisted
 ---
 
-In this quickstart, you work with a .NET app to create, populate, and query vectors. The code examples perform these operations by using the [Azure AI Search client library](/dotnet/api/overview/azure/search). The library provides an abstraction over the REST API for access to index operations such as data ingestion, search operations, and index management operations.
+In this quickstart, you use a .NET app to create, load, and query a [vector index](../../vector-store.md). The code performs these operations by using the [Azure AI Search client library for .NET](/dotnet/api/overview/azure/search), which provides an abstraction over the REST APIs to access index operations.
 
-In Azure AI Search, a [vector store](../../vector-store.md) has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. The [Create Index](/rest/api/searchservice/indexes/create-or-update) REST API creates the vector store.
+In Azure AI Search, a vector index has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. [Indexes - Create or Update](/rest/api/searchservice/indexes/create-or-update) (REST API) creates the vector index.
 
 > [!NOTE]
 > This quickstart omits the vectorization step and provides inline embeddings. If you want to add [built-in data chunking and vectorization](../../vector-search-integrated-vectorization.md) over your own content, try the [**Import data (new)** wizard](../../search-get-started-portal-import-vectors.md) for an end-to-end walkthrough.
 
 ## Prerequisites
 
-- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch) in your current subscription.
-    - You can use a free search service for most of this quickstart, but we recommend the Basic tier or higher for larger data files.
-    - To run the query example that invokes [semantic reranking](../../semantic-search-overview.md), your search service must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
++ An [Azure AI Search service](../../search-create-service-portal.md).
 
-- [Visual Studio Code](https://code.visualstudio.com/download) or [Visual Studio](https://visualstudio.com).
+    + You can use the Free tier for most of this quickstart, but we recommend Basic or higher for larger data files.
 
-- [Git](https://git-scm.com/downloads) to clone the sample repo.
+    + For [keyless authentication](../../search-get-started-rbac.md) with Microsoft Entra ID, assign the **Search Index Data Contributor role** to your user account.
+    
+    + To run the semantic hybrid query, you must [enable semantic ranker](../../semantic-how-to-enable-disable.md).
+
++ [Visual Studio Code](https://code.visualstudio.com/download) or [Visual Studio](https://visualstudio.com) to run the code.
+
++ [Git](https://git-scm.com/downloads) to clone the sample repo.
 
 ## Get service information
 
-Requests to the search endpoint must be authenticated and authorized. While it's possible to use API keys or roles for this task, we recommend [using a keyless connection via Microsoft Entra ID](../../search-get-started-rbac.md).
+Requests to the search endpoint must be authenticated and authorized. While it's possible to use API keys for this task, we recommend [using a keyless connection via Microsoft Entra ID](../../search-get-started-rbac.md).
 
-This quickstart uses `DefaultAzureCredential`, which simplifies authentication in both development and production scenarios. However, for production scenarios, you might have more advanced requirements that require a different approach. See [Authenticate .NET apps to Azure services by using the Azure SDK for .NET](/dotnet/azure/sdk/authentication/) to understand all of your options.
+This quickstart uses `DefaultAzureCredential`, which simplifies authentication in both development and production scenarios. However, for production scenarios, you might have more advanced requirements that require a different approach. To understand all of your options, see [Authenticate .NET apps to Azure services by using the Azure SDK for .NET](/dotnet/azure/sdk/authentication/).
 
 ## Clone the code and setup environment
 
-1. Clone the repo containing the code for this quickstart. 
+1. Clone the repo containing the code for this quickstart.
 
    ```bash
    git clone https://github.com/Azure-Samples/azure-search-dotnet-samples
    ```
-  
-   This repo has .NET code examples for several articles each in a separate subfolder.
 
-1. Open the subfolder `quickstart-Vector-Search` in Visual Studio Code, or double click the `.sln` file to open the solution in Visual Studio.
+1. Open the `quickstart-vector-search` folder in Visual Studio Code or double-click the `VectorSearchQuickstart.sln` file to open the solution in Visual Studio.
+
+1. Open `appsettings.json` in both `VectorSearchCreatePopulateIndex` and `VectorSearchExamples` folders. 
 
-1. Open the `appsettings.json` files in the `VectorSearchExamples` and `VectorSearchCreatePopulateIndex` folders. Update the following values: 
+1. Set `Endpoint` to your search service URL, which should be similar to `https://mydemo.search.windows.net`.
 
-   - `AZURE_SEARCH_ENDPOINT`: Find the url of your Azure AI Search service in the [Azure portal](https://portal.azure.com). On the **Overview** page of your search resource, look for the URL field. An example endpoint might look like `https://mydemo.search.windows.net`. 
-   - `AZURE_SEARCH_INDEX_NAME`: Leave the default value provided in the file or enter your own index name.
+1. Set `IndexName` to a unique name for your index. You can also use the default `hotels-vector-quickstart` name.
 
-## Create the vector index and upload documents
+## Create a vector index and upload documents
 
-To run search queries against the Azure AI Search service, you first need to create a search index and upload documents to the service.
+To run search queries against your Azure AI Search service, you must first create a search index and upload documents to the index.
 
-1. Open a new terminal in the `VectorSearchCreatePopulateIndex` folder.
+To create and populate the index:
 
-1. Run the project using the `dotnet run` command:
+1. Open a terminal in the `VectorSearchCreatePopulateIndex` folder.
+
+1. Use the `dotnet run` command to run the project.
 
     ```dotnetcli
     dotnet run
     ```
 
-The following code executes to create an index:
-
-:::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchcreatepopulateindex/program.cs" id="CreateSearchindex":::
-
-The following code uploads the JSON formatted documents in the `hotel-samples.json` file to the Azure AI Search service:
-
-:::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchcreatepopulateindex/program.cs" id="UploadDocs":::
-
-After you run the project, the following output is printed:
-
-```output
-Key: 1, Succeeded: True
-Key: 2, Succeeded: True
-Key: 3, Succeeded: True
-Key: 4, Succeeded: True
-Key: 48, Succeeded: True
-Key: 49, Succeeded: True
-Key: 13, Succeeded: True
-```
-
-Key takeaways:
-
-- Your code interacts with a specific search index hosted in your Azure AI Search service through the `SearchClient`, which is the main object provided by the `azure-search-documents` package. The `SearchClient` provides access to index operations such as:
+    The following code executes to create an index:
+    
+    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchcreatepopulateindex/program.cs" id="CreateSearchindex":::
+    
+    The following code uploads JSON-formatted documents in the `hotel-samples.json` file to your search service.
+    
+    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchcreatepopulateindex/program.cs" id="UploadDocs":::
+    
+    After you run the project, the following output is printed.
+    
+    ```output
+    Key: 1, Succeeded: True
+    Key: 2, Succeeded: True
+    Key: 3, Succeeded: True
+    Key: 4, Succeeded: True
+    Key: 48, Succeeded: True
+    Key: 49, Succeeded: True
+    Key: 13, Succeeded: True
+    ```
+    
+    Key takeaways:
 
-    - **Data ingestion**: `UploadDocuments()`, `MergeDocuments()`, `DeleteDocuments()`
-    - **Search operations**: `Search()`, `Autocomplete()`, `Suggest()`
-    - **Index management operations**: `CreateOrUpdateIndex()`
+    + Your code interacts with a specific search index hosted in your Azure AI Search service through the SearchClient, which is the main object provided by the azure-search-documents package. The SearchClient provides access to index operations, such as:
 
-- Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 4096 floating point values each. This size of embeddings generated by the Azure OpenAI **text-embedding-3-small** model for this quickstart is 1536.
+        + Data ingestion: `UploadDocuments()`, `MergeDocuments()`, `DeleteDocuments()`
 
-## Run search queries
+        + Search operations: `Search()`, `Autocomplete()`, `Suggest()`
+        
+        + Index management operations: `CreateOrUpdateIndex()`
+    
+    + Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 4096 floating point values each. This quickstart sets the dimensions attribute to 1,536 because that's the size of embeddings generated by the `text-embedding-ada-002` model.
 
-After the index is created and documents are loaded, you can issue vector queries against them by calling `SearchAsync()` with various parameters.
+## Run queries
 
-1. In the `VectorSearchExamples` folder, open the `Program.cs` file.
-1. Open a new terminal in the `VectorSearchExamples` folder.
+To issue the vector queries in this section, open `Program.cs` in the `VectorSearchExamples` folder, and then open a terminal in the `VectorSearchExamples` folder.
 
-In the following sections, you run queries against the `hotels-vector-quickstart` index. The queries include:
+Queries in this section:
 
-- [Single vector search](#single-vector-search)
-- [Single vector search with filter](#single-vector-search-with-filter)
-- [Hybrid search](#hybrid-search)
-- [Semantic hybrid search with filter](#semantic-hybrid-search-with-a-filter)
++ [Single vector search](#single-vector-search)
++ [Single vector search with filter](#single-vector-search-with-filter)
++ [Hybrid search](#hybrid-search)
++ [Semantic hybrid search with filter](#semantic-hybrid-search-with-a-filter)
 
 ### Single vector search
 
-The first example demonstrates a basic scenario where you want to find document descriptions that closely match the search string.
+The first query demonstrates a basic scenario where you want to find document descriptions that closely match the search string.
 
-1. In the `Program.cs` file of the `VectorSearchExamples` folder, uncomment the method call `SearchExamples.SearchSingleVector(searchClient, vectorizedResult);`. This method executes the following search function in the `SearchExamples.cs` class:
+To create a single vector search:
 
-    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchexamples/SearchExamples.cs" id="SearchSingleVector":::
+1. In the `Program.cs` file of the `VectorSearchExamples` folder, uncomment the `SearchExamples.SearchSingleVector(searchClient, vectorizedResult);` method call.
 
-1. Run the project using the `dotnet run` command:
+    This method executes the following search function in the `SearchExamples.cs` class.
 
-    ```dotnetcli
-    dotnet run
-    ```
+    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchexamples/SearchExamples.cs" id="SearchSingleVector":::
 
-    After you run the project, the search results are printed in the output window:
+1. Run `dotnet run` to execute the query, which returns the following results.
     
     ```output
     Single Vector Search Results:
@@ -132,29 +136,31 @@ The first example demonstrates a basic scenario where you want to find document
 
 ### Single vector search with filter
 
-You can add filters, but the filters are applied to the nonvector content in your index. In this example, the filter applies to the `Tags` field to filter out any hotels that don't provide free Wi-Fi.
+In Azure AI Search, [filters](../../vector-search-filters.md) apply to nonvector fields in an index. This example filters on the `Tags` field to filter out any hotels that don't provide free Wi-Fi.
+
+To create a single vector search with a filter:
+
+1. In the `Program.cs` file of the `VectorSearchExamples` folder, uncomment the `SearchExamples.SearchSingleVectorWithFilter(searchClient, vectorizedResult);` method call.
 
-1. In the `Program.cs` file of the `VectorSearchExamples` folder, uncomment the method call `SearchExamples.SearchSingleVectorWithFilter(searchClient, vectorizedResult);`. This method executes the following search function in the `SearchExamples.cs` class:
+    This method executes the following search function in the `SearchExamples.cs` class.
 
     :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchexamples/SearchExamples.cs" id="SearchSingleVectorWithFilter":::
 
-1.  Run the project again, and the status of each document is printed below it:
+1.  Run `dotnet run` to execute the query, which returns only hotels that provide free Wi-Fi. 
     
        ```output
         Single Vector Search With Filter Results:
         Score: 0.6605852, HotelId: 48, HotelName: Nordick's Valley Motel, Tags: continental breakfastair conditioningfree wifi
         Score: 0.57902366, HotelId: 2, HotelName: Old Century Hotel, Tags: poolfree wifiair conditioningconcierge
        ```
 
-       The query was the same as the previous [single vector search example](#single-vector-search), but it includes a post-processing exclusion filter and returns only the two hotels that have free Wi-Fi.
+1. For a geo filter, uncomment `SearchExamples.SingleSearchWithGeoFilter(searchClient, vectorizedResult);` in `Program.cs`.
 
-1. The next filter example uses a **geo filter**. In the `Program.cs` file of the `VectorSearchExamples` folder, uncomment the method call `SearchExamples.SingleSearchWithGeoFilter(searchClient, vectorizedResult);`. This method executes the following search function in the `SearchExamples.cs` class:
+    This method executes the following search function in the `SearchExamples.cs` class.
 
     :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchexamples/SearchExamples.cs" id="SingleSearchWithGeoFilter":::
-   
-   The query was the same as the previous [single vector search example](#single-vector-search), but it includes a post-processing exclusion filter and returns only the two hotels within 300 kilometers.
 
-1.  Run the project again, and the status of each document is printed below it:
+1.  Run `dotnet run` to execute the query, which returns only hotels within 300 kilometers.
    
     ```output
     Vector query with a geo filter:
@@ -173,16 +179,20 @@ You can add filters, but the filters are applied to the nonvector content in you
 
 ### Hybrid search
 
-Hybrid search consists of keyword queries and vector queries in a single search request. This example runs the vector query and full-text search concurrently:
+[Hybrid search](../../hybrid-search-overview.md) combines keyword and vector queries in one request. This example runs the following full-text and vector query strings concurrently:
+
++ Search string: `historic hotel walk to restaurants and shopping`
++ Vector query string: `quintessential lodging near running trails, eateries, retail` (vectorized into a mathematical representation)
 
-- **Search string**: `historic hotel walk to restaurants and shopping`
-- **Vector query string** (vectorized into a mathematical representation): `Quintessential lodging near running trails, eateries, retail`
+To create a hybrid search:
 
-1. In the `Program.cs` file of the `VectorSearchExamples` folder, uncomment the method call `SearchExamples.SearchHybridVectorAndText(searchClient, vectorizedResult);`. This method executes the following search function in the `SearchExamples.cs` class:
+1. In the `Program.cs` file, uncomment the `SearchExamples.SearchHybridVectorAndText(searchClient, vectorizedResult);` method call.
+
+    This method executes the following search function in the `SearchExamples.cs` class.
 
     :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchexamples/SearchExamples.cs" id="SearchHybridVectorAndText":::
 
-1.  Run the project again, and the status of each document is printed below it:
+1.  Run `dotnet run` to execute the query, which returns the following results.
 
        ```output
        Hybrid search results:
@@ -222,136 +232,140 @@ Hybrid search consists of keyword queries and vector queries in a single search
        Tags: poolfree wifiair conditioningconcierge
        ```
     
-Because Reciprocal Rank Fusion (RRF) merges results, it helps to review the inputs. The following results are from only the full-text query. The top two results are Sublime Palace Hotel and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
-
-```json
-{
-    "@search.score": 2.2626662,
-    "HotelName": "Sublime Palace Hotel",
-    "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace."
-},
-{
-    "@search.score": 0.86421645,
-    "HotelName": "Luxury Lion Resort",
-    "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort"
-},
-```
-
-In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to fourth position. Luxury Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
-
-```json
-"value": [
-    {
-        "@search.score": 0.857736,
-        "HotelId": "48",
-        "HotelName": "Nordick's Valley Motel",
-        "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
-        "Category": "Boutique"
-    },
-    {
-        "@search.score": 0.8399129,
-        "HotelId": "49",
-        "HotelName": "Swirling Currents Hotel",
-        "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center.",
-        "Category": "Luxury"
-    },
-    {
-        "@search.score": 0.8383954,
-        "HotelId": "13",
-        "HotelName": "Luxury Lion Resort",
-        "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort",
-        "Category": "Resort and Spa"
-    },
+    Because Reciprocal Rank Fusion (RRF) merges results, it helps to review the inputs. The following results are from the full-text query only. The top two results are Sublime Palace Hotel and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
+
+    ```json
     {
-        "@search.score": 0.8254346,
-        "HotelId": "4",
+        "@search.score": 2.2626662,
         "HotelName": "Sublime Palace Hotel",
-        "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.",
-        "Category": "Boutique"
+        "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace."
     },
     {
-        "@search.score": 0.82380056,
-        "HotelId": "1",
-        "HotelName": "Stay-Kay City Hotel",
-        "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York.",
-        "Category": "Boutique"
-    },
-    {
-        "@search.score": 0.81514084,
-        "HotelId": "2",
-        "HotelName": "Old Century Hotel",
-        "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
-        "Category": "Boutique"
+        "@search.score": 0.86421645,
+        "HotelName": "Luxury Lion Resort",
+        "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort"
     },
-    {
-        "@search.score": 0.8133763,
-        "HotelId": "3",
-        "HotelName": "Gastronomic Landscape Hotel",
-        "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
-        "Category": "Resort and Spa"
-    }
-]
-```
+    ```
+
+    In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to the fourth position. Luxury Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
+
+    ```json
+    "value": [
+        {
+            "@search.score": 0.857736,
+            "HotelId": "48",
+            "HotelName": "Nordick's Valley Motel",
+            "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer.  Hiking? Wine Tasting? Exploring the caverns?  It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley.",
+            "Category": "Boutique"
+        },
+        {
+            "@search.score": 0.8399129,
+            "HotelId": "49",
+            "HotelName": "Swirling Currents Hotel",
+            "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center.",
+            "Category": "Luxury"
+        },
+        {
+            "@search.score": 0.8383954,
+            "HotelId": "13",
+            "HotelName": "Luxury Lion Resort",
+            "Description": "Unmatched Luxury.  Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium, we feature the best in comfort",
+            "Category": "Resort and Spa"
+        },
+        {
+            "@search.score": 0.8254346,
+            "HotelId": "4",
+            "HotelName": "Sublime Palace Hotel",
+            "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.",
+            "Category": "Boutique"
+        },
+        {
+            "@search.score": 0.82380056,
+            "HotelId": "1",
+            "HotelName": "Stay-Kay City Hotel",
+            "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York.",
+            "Category": "Boutique"
+        },
+        {
+            "@search.score": 0.81514084,
+            "HotelId": "2",
+            "HotelName": "Old Century Hotel",
+            "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
+            "Category": "Boutique"
+        },
+        {
+            "@search.score": 0.8133763,
+            "HotelId": "3",
+            "HotelName": "Gastronomic Landscape Hotel",
+            "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
+            "Category": "Resort and Spa"
+        }
+    ]
+    ```
 
 ### Semantic hybrid search with a filter
 
-The hybrid query with semantic ranking is filtered to show only the hotels within a 500-kilometer radius of Washington D.C.
+Add [semantic ranking](../../semantic-search-overview.md) to rerank results based on language understanding.
 
-1. In the `Program.cs` file of the `VectorSearchExamples` folder, uncomment the method call `SearchExamples.SearchHybridVectoryAndSemantic(searchClient, vectorizedResult);`. This method executes the following search function in the `SearchExamples.cs` class:
+To create a semantic hybrid search with a filter:
 
-    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchexamples/SearchExamples.cs" id="SearchHybridVectorAndSemantic":::
+1. In the `Program.cs` file, uncomment `SearchExamples.SearchHybridVectorAndSemantic(searchClient, vectorizedResult);` method call.
 
-1.  Run the project again, and review the output below the cell. The response is three hotels, which are filtered by location and faceted by `StateProvince` and semantically reranked to promote results that are closest to the search string query (`historic hotel walk to restaurants and shopping`).
+    This method executes the following search function in the `SearchExamples.cs` class.
 
-       The Swirling Currents Hotel now moves into the top spot. Without semantic ranking, Nordick's Valley Motel is number one. With semantic ranking, the machine comprehension models recognize that `historic` applies to "hotel, within walking distance to dining (restaurants) and shopping."
-    
-       ```output
-       Total semantic hybrid results: 7
-       - Score: 0.0317460335791111
-         Re-ranker Score: 2.6550590991973877
-         HotelId: 49
-         HotelName: Swirling Currents Hotel
-         Description: Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary Wi-Fi and flat-screen TVs.
-         Category: Suite
-       - Score: 0.03279569745063782
-         Re-ranker Score: 2.599761724472046
-         HotelId: 4
-         HotelName: Sublime Palace Hotel
-         Description: Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.
-         Category: Boutique
-       - Score: 0.03125
-         Re-ranker Score: 2.3480887413024902
-         HotelId: 2
-         HotelName: Old Century Hotel
-         Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
-         Category: Boutique
-       - Score: 0.016393441706895828
-         Re-ranker Score: 2.2718777656555176
-         HotelId: 1
-         HotelName: Stay-Kay City Hotel
-         Description: This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic center of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.
-         Category: Boutique
-       - Score: 0.01515151560306549
-         Re-ranker Score: 2.0582215785980225
-         HotelId: 3
-         HotelName: Gastronomic Landscape Hotel
-         Description: The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.
-         Category: Suite
-       ```
+    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-vector-search/vectorsearchexamples/SearchExamples.cs" id="SearchHybridVectorAndSemantic":::
 
-Key takeaways:
+1. Run `dotnet run` to execute the query, which returns the following hotels. The hotels are filtered by location, faceted by `StateProvince`, and semantically reranked to promote results that are closest to the search string query (`historic hotel walk to restaurants and shopping`).
 
-- In a hybrid search, you can integrate vector search with full-text search over keywords. Filters, spell check, and semantic ranking apply to textual content only, and not vectors. In this final query, there's no semantic `answer` because the system didn't produce one that was sufficiently strong.
+    The Swirling Currents Hotel now moves to the top spot. Without semantic ranking, Nordick's Valley Motel is number one. With semantic ranking, the machine comprehension models recognize that `historic` applies to "hotel within walking distance to dining (restaurants) and shopping."
+    
+    ```output
+    Total semantic hybrid results: 7
+    - Score: 0.0317460335791111
+      Re-ranker Score: 2.6550590991973877
+      HotelId: 49
+      HotelName: Swirling Currents Hotel
+      Description: Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary Wi-Fi and flat-screen TVs.
+      Category: Suite
+    - Score: 0.03279569745063782
+      Re-ranker Score: 2.599761724472046
+      HotelId: 4
+      HotelName: Sublime Palace Hotel
+      Description: Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.
+      Category: Boutique
+    - Score: 0.03125
+      Re-ranker Score: 2.3480887413024902
+      HotelId: 2
+      HotelName: Old Century Hotel
+      Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
+      Category: Boutique
+    - Score: 0.016393441706895828
+      Re-ranker Score: 2.2718777656555176
+      HotelId: 1
+      HotelName: Stay-Kay City Hotel
+      Description: This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic center of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.
+      Category: Boutique
+    - Score: 0.01515151560306549
+      Re-ranker Score: 2.0582215785980225
+      HotelId: 3
+      HotelName: Gastronomic Landscape Hotel
+      Description: The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel's restaurant services.
+      Category: Suite
+    ```
+    
+    Key takeaways:
 
-- Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
+    + In a hybrid search, you can integrate vector search with full-text search over keywords. Filters, spell check, and semantic ranking apply to textual content only, and not vectors. In this final query, there's no semantic `answer` because the system didn't produce one that was sufficiently strong.
+    
+    + Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
 
-## Clean up
+## Clean up resources
 
 When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
 
 You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
 
 ## Next steps
 
-- Review the repository of code samples for vector search capabilities in Azure AI Search for [.NET](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet)
-- Review the other .NET and Azure AI Search code samples in the [azure-search-dotnet-samples repo](https://github.com/Azure-Samples/azure-search-dotnet-samples)
\ No newline at end of file
++ Review the repository of code samples for vector search capabilities in Azure AI Search for [.NET](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet).
++ Review the other .NET and Azure AI Search code samples in the [azure-search-dotnet-samples repo](https://github.com/Azure-Samples/azure-search-dotnet-samples).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索の .NET クイックスタートドキュメントの更新"
}
```

### Explanation
このコードの変更は、`search-get-started-vector-dotnet.md` ファイルの大規模な更新を反映しています。主な変更点は、文書の日付が「11/20/2025」から「01/14/2026」に変更され、新たに `ms.custom` と `ai-usage` のメタデータが追加されたことです。これにより、最新の情報と技術トレンドを反映した内容へと進化しています。

文書の冒頭から始まり、.NET アプリを使用してベクトルインデックスを作成、ロード、クエリする方法が改善されています。特に、AWS AI Search クライアントライブラリに関する説明が新たに明確化され、ユーザーが REST API の抽象化された操作にアクセスするための情報が整えられています。

さらに、文書の内容全体が簡潔でわかりやすくなり、コードの例を追加したり、セマンティックランキングやフィルタリングの利用に関する部分が強化されています。特に、クエリの実行手順や、使用するコードの例が詳細に説明されており、読者は各機能を実装する方法をより理解しやすくなっています。

最終的に、サンプルコードや使用法に関連するリンクが増加し、ユーザーが迅速に適切な情報にアクセスできるよう配慮されており、全体として、より直感的で実用的なクイックスタートガイドに仕上がっています。

## articles/search/includes/quickstarts/search-get-started-vector-java.md{#item-a3db97}

<details>
<summary>Diff</summary>
````diff
@@ -2,36 +2,41 @@
 author: KarlErickson
 ms.author: karler
 ms.service: azure-ai-search
-ms.custom: devx-track-java
+ms.custom: devx-track-java, dev-focus
 ms.topic: include
-ms.date: 12/15/2025
+ms.date: 01/14/2026
 ai-usage: ai-assisted
 ---
 
-In this quickstart, you use Java to create, load, and query vectors. The code examples perform these operations by using the [Azure AI Search client library](/java/api/overview/azure/search-documents-readme). The library provides an abstraction over the REST API for access to index operations such as data ingestion, search operations, and index management operations.
+In this quickstart, you use Java to create, load, and query a [vector index](../../vector-store.md). The code performs these operations by using the [Azure AI Search client library for Java](/java/api/overview/azure/search-documents-readme), which provides an abstraction over the REST APIs to access index operations.
 
-In Azure AI Search, a [vector store](../../vector-store.md) has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. The [Create Index](/rest/api/searchservice/indexes/create-or-update) REST API creates the vector store.
+In Azure AI Search, a vector index has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. [Indexes - Create or Update](/rest/api/searchservice/indexes/create-or-update) (REST API) creates the vector index.
 
 > [!NOTE]
 > This quickstart omits the vectorization step and provides inline embeddings. If you want to add [built-in data chunking and vectorization](../../vector-search-integrated-vectorization.md) over your own content, try the [**Import data (new)** wizard](../../search-get-started-portal-import-vectors.md) for an end-to-end walkthrough.
 
 ## Prerequisites
 
-- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch) in your current subscription.
-    - The `Search Index Data Contributor` role assigned at the scope of the service.
-    - You can use a free search service for most of this quickstart, but we recommend the Basic tier or higher for larger data files.
-    - To run the query example that invokes [semantic reranking](../../semantic-search-overview.md), your search service must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
++ An [Azure AI Search service](../../search-create-service-portal.md).
 
-- [Java 21 (LTS)](/java/openjdk/install).
+    + You can use the Free tier for most of this quickstart, but we recommend Basic or higher for larger data files.
 
-- [Maven](https://maven.apache.org/download.cgi).
+    + For [keyless authentication](../../search-get-started-rbac.md) with Microsoft Entra ID, assign the **Search Index Data Contributor role** to your user account.
+    
+    + To run the semantic hybrid query, you must [enable semantic ranker](../../semantic-how-to-enable-disable.md).
+
++ [Java 21 (LTS)](/java/openjdk/install).
+
++ [Maven](https://maven.apache.org/download.cgi).
 
-## Get service endpoints
+## Get service information
 
 In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints so that you can provide them as variables in your code.
 
+To get the service endpoint:
+
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
 1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
@@ -48,7 +53,7 @@ In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Sea
 
 1. Create a `pom.xml` file with required dependencies.
 
-   :::code language="xml" source="~/azure-search-java-samples/vector-quickstart/pom.xml" :::
+   :::code language="xml" source="~/azure-search-java-samples/quickstart-vector-search/pom.xml" :::
 
 1. Compile the project to resolve the dependencies.
 
@@ -86,25 +91,27 @@ az login --tenant <PUT YOUR TENANT ID HERE>
 
 You should now be logged in to Azure from your local device.
 
-## Create the vector index
+## Create a vector index
 
 In this section, you create a vector index in Azure AI Search with [SearchIndexClient](/java/api/com.azure.search.documents.indexes.searchindexclient).[createOrUpdateIndex](/java/api/com.azure.search.documents.indexes.searchindexclient#com-azure-search-documents-indexes-searchindexclient-createorupdateindex(com-azure-search-documents-indexes-models-searchindex)). The index schema defines the fields, including the vector field `DescriptionVector`.
 
-1. Create a `CreateIndex.java` file in the the `src/main/java/com/example/search` directory.
+To create a vector index:
+
+1. Create a `CreateIndex.java` file in the `src/main/java/com/example/search` directory.
 
 1. Copy the following code into the file.
 
-   :::code language="java" source="~/azure-search-java-samples/vector-quickstart/src/main/java/com/example/search/CreateIndex.java" :::
+   :::code language="java" source="~/azure-search-java-samples/quickstart-vector-search/src/main/java/com/example/search/CreateIndex.java" :::
 
-   The code file creates the index and defines the index schema, including the vector field `DescriptionVector`.
+   The code file creates the index and defines the index schema, including the `DescriptionVector` vector field.
 
 1. Run the file.
 
     ```bash
     mvn compile exec:java -Dexec.mainClass="com.example.search.CreateIndex"
     ```
 
-1. The output of this code shows that the index is created successfully:
+    The output of this code shows that the index is created successfully.
 
     ```output
     Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -113,29 +120,37 @@ In this section, you create a vector index in Azure AI Search with [SearchIndexC
     hotels-vector-quickstart created
     ```
 
-   Key takeaways when creating vector index with the `azure-search-documents` library:
+   Key takeaways:
+
+   + You define an index by creating a list of fields.
+
+   + This particular index supports multiple search capabilities, such as:
+
+      + Full-text keyword search (`setSearchable`)
+
+      + Vector search (enables hybrid search by collocating vector and nonvector fields) fields (`DescriptionVector` with `setVectorSearchProfileName`)
+      
+      + Semantic search 
+
+      + Faceted search (`SearchSuggester`)
 
-   - You define an index by creating a list of fields.
+      + Geo-spatial search (`Location` field with `SearchFieldDataType.GEOGRAPHY_POINT`)
 
-   - This particular index supports multiple search capabilities, such as:
-      - Full-text keyword search (`setSearchable`)
-      - Vector search (enables hybrid search by collocating vector and nonvector fields) fields (`DescriptionVector` with `setVectorSearchProfileName`)
-      - Semantic search 
-      - Faceted search (`SearchSuggester`)
-      - Geo-spatial search (`Location` field with `SearchFieldDataType.GEOGRAPHY_POINT`)
-      - Filtering, sorting (Many fields marked filterable and sortable)
+      + Filtering, sorting (many fields marked filterable and sortable)
 
 ## Upload documents to the index
 
-Creating and loading the index are separate steps. You created the index schema in the [previous step](#create-the-vector-index). Now you need to load documents into the index with [SearchClient](/java/api/com.azure.search.documents.searchclient).[uploadDocuments](/java/api/com.azure.search.documents.searchclient#com-azure-search-documents-searchclient-uploaddocuments(java-lang-iterable(-))). The documents contain the vectorized version of the article's description, which enables similarity search based on meaning rather than exact keywords.
+Creating and loading the index are separate steps. You created the index schema in the previous step. You now need to load documents into the index with [SearchClient](/java/api/com.azure.search.documents.searchclient).[uploadDocuments](/java/api/com.azure.search.documents.searchclient#com-azure-search-documents-searchclient-uploaddocuments(java-lang-iterable(-))). The documents contain the vectorized version of the article's description, which enables similarity search based on meaning rather than exact keywords.
 
 In Azure AI Search, the index stores all searchable content, while the search engine executes queries against that index.
 
+To upload documents to the index:
+
 1. Create an `UploadDocuments.java` file in the `src/main/java/com/example/search` directory.
 
 1. Copy the following code into the file.
 
-   :::code language="java" source="~/azure-search-java-samples/vector-quickstart/src/main/java/com/example/search/UploadDocuments.java" :::
+   :::code language="java" source="~/azure-search-java-samples/quickstart-vector-search/src/main/java/com/example/search/UploadDocuments.java" :::
 
     This code loads a collection of documents. Each document includes the vectorized version of the article's `Description`. This vector enables similarity search, where matching is based on meaning rather than exact keywords.
 
@@ -147,7 +162,7 @@ In Azure AI Search, the index stores all searchable content, while the search en
     mvn compile exec:java -Dexec.mainClass="com.example.search.UploadDocuments"
     ```
 
-1. The output of this code shows that the documents are indexed and ready for search:
+    The output of this code shows that the documents are indexed and ready for search.
 
     ```output
     Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -164,37 +179,42 @@ In Azure AI Search, the index stores all searchable content, while the search en
     All documents indexed successfully.
     ```
 
-    Key takeaways about the `uploadDocuments` method and this example:
+    Key takeaways:
 
     * Your code interacts with a specific search index hosted in your Azure AI Search service through the `SearchClient`. The `SearchClient` provides access to operations such as:
-        * Data ingestion - `uploadDocuments`, `mergeDocuments`, `deleteDocuments`, and so on.
-        * Search operations - `search`, `autocomplete`, `suggest`
-    * Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 4096 floating point values each. This quickstart sets the dimensions attribute to 1,536 because that's the size of embeddings generated by the Azure OpenAI `text-embedding-ada-002` model.
+
+        * Data ingestion: `uploadDocuments`, `mergeDocuments`, `deleteDocuments`, and so on.
+
+        * Search operations: `search`, `autocomplete`, `suggest`
+
+    * Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 4096 floating point values each. This quickstart sets the dimensions attribute to 1,536 because that's the size of embeddings generated by the `text-embedding-ada-002` model.
 
 ## Create the query as a vector
 
 The example vector queries are based on two strings:
 
-- **Search string**: `historic hotel walk to restaurants and shopping`
-- **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
++ Search string: `historic hotel walk to restaurants and shopping`
++ Vector query string: `quintessential lodging near running trails, eateries, retail` (vectorized into a mathematical representation)
 
 The vector query string is semantically similar to the search string, but it includes terms that don't exist in the search index. If you do a keyword search for `quintessential lodging near running trails, eateries, retail`, results are zero. We use this example to show how you can get relevant results even if there are no matching terms.
 
 Create a `QueryVector.java` file in the `src/main/java/com/example/search` directory and add the code to create the query vector.
 
-:::code language="java" source="~/azure-search-java-samples/vector-quickstart/src/main/java/com/example/search/QueryVector.java" :::
+:::code language="java" source="~/azure-search-java-samples/quickstart-vector-search/src/main/java/com/example/search/QueryVector.java" :::
 
 This code is used in the following sections to perform vector searches. The query vector is created using an embedding model from Azure OpenAI.
 
 ## Create a single vector search
 
 The first example demonstrates a basic scenario where you want to find document descriptions that closely match the search string using the [SearchClient](/java/api/com.azure.search.documents.searchclient).[search](/java/api/com.azure.search.documents.searchasyncclient#com-azure-search-documents-searchasyncclient-search(java-lang-string)) and the [VectorQuery](/java/api/com.azure.search.documents.models.vectorquery) and [SearchOptions](/java/api/com.azure.search.documents.models.searchoptions).
 
+To create a single vector search:
+
 1. Create a `SearchSingle.java` file in the `src/main/java/com/example/search` directory.
 
 1. Copy the following code into the file.
 
-    :::code language="java" source="~/azure-search-java-samples/vector-quickstart/src/main/java/com/example/search/SearchSingle.java" :::
+    :::code language="java" source="~/azure-search-java-samples/quickstart-vector-search/src/main/java/com/example/search/SearchSingle.java" :::
 
     The `vectorQuery` contains the configuration of the vectorized query including the vectorized text of the query input as retrieved through `QueryVector.getVectorList`. `setFields` determines which vector fields are searched and `setKNearestNeighborsCount` specifies the number of nearest neighbors to return.
 
@@ -206,7 +226,7 @@ The first example demonstrates a basic scenario where you want to find document
     mvn compile exec:java -Dexec.mainClass="com.example.search.SearchSingle"
     ```
 
-1. The output of this code shows the relevant docs for the query `quintessential lodging near running trails, eateries, retail`.
+    The output of this code shows the relevant docs for the query `quintessential lodging near running trails, eateries, retail`.
 
     ```output
     Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -226,11 +246,13 @@ The first example demonstrates a basic scenario where you want to find document
 
 You can add filters, but the filters are applied to the nonvector content in your index. In this example, the filter applies to the `Tags` field to filter out any hotels that don't provide free Wi-Fi. This search uses [SearchClient](/java/api/com.azure.search.documents.searchclient).[SearchClient](/java/api/com.azure.search.documents.searchclient) and [SearchOptions](/java/api/com.azure.search.documents.models.searchoptions). 
 
+To create a single vector search with a filter:
+
 1. Create a `SearchSingleWithFilter.java` file in the `src/main/java/com/example/search` directory.
 
 1. Copy the following code into the file.
 
-    :::code language="java" source="~/azure-search-java-samples/vector-quickstart/src/main/java/com/example/search/SearchSingleWithFilter.java" :::
+    :::code language="java" source="~/azure-search-java-samples/quickstart-vector-search/src/main/java/com/example/search/SearchSingleWithFilter.java" :::
 
     This code has the same search functionality as the previous search, but it adds a post-processing exclusion filter for hotels with `free wifi`.
 
@@ -240,7 +262,7 @@ You can add filters, but the filters are applied to the nonvector content in you
     mvn compile exec:java -Dexec.mainClass="com.example.search.SearchSingleWithFilter"
     ```
 
-1. The output of this code shows the relevant documents for the query with the filter for `free wifi` applied:
+    The output of this code shows the relevant documents for the query with the filter for `free wifi` applied.
 
     ```output
     Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -255,19 +277,21 @@ You can add filters, but the filters are applied to the nonvector content in you
 
 You can specify a geospatial filter to limit results to a specific geographic area. In this example, the filter limits results to hotels within 300 kilometers of Washington D.C. (coordinates: `-77.03241 38.90166`). Geospatial distances are always in kilometers. This search uses [SearchClient](/java/api/com.azure.search.documents.searchclient).[SearchClient](/java/api/com.azure.search.documents.searchclient) and [SearchOptions](/java/api/com.azure.search.documents.models.searchoptions).
 
+To create a single vector search with a geospatial filter:
+
 1. Create a `SearchSingleWithFilterGeo.java` file in the `src/main/java/com/example/search` directory.
 
 1. Copy the following code into the file.
 
-    :::code language="java" source="~/azure-search-java-samples/vector-quickstart/src/main/java/com/example/search/SearchSingleWithFilterGeo.java" :::
+    :::code language="java" source="~/azure-search-java-samples/quickstart-vector-search/src/main/java/com/example/search/SearchSingleWithFilterGeo.java" :::
 
 1. Build and run the file.
 
     ```bash
     mvn compile exec:java -Dexec.mainClass="com.example.search.SearchSingleWithFilterGeo"
     ```
 
-1. The output of this code shows the relevant documents for the query with the geospatial post-processing exclusion filter applied.
+    The output of this code shows the relevant documents for the query with the geospatial post-processing exclusion filter applied.
 
     ```output
     Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -280,26 +304,28 @@ You can specify a geospatial filter to limit results to a specific geographic ar
 
 ## Create a hybrid search
 
-Hybrid search consists of keyword queries and vector queries in a single search request. This example runs the vector query and full-text search concurrently:
+[Hybrid search](../../hybrid-search-overview.md) combines keyword and vector queries in one request. This example runs the following full-text and vector query strings concurrently:
 
-- **Search string**: `historic hotel walk to restaurants and shopping`
-- **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
++ Search string: `historic hotel walk to restaurants and shopping`
++ Vector query string: `quintessential lodging near running trails, eateries, retail` (vectorized into a mathematical representation)
 
 This search uses [SearchClient](/java/api/com.azure.search.documents.searchclient).[SearchClient](/java/api/com.azure.search.documents.searchclient) and [SearchOptions](/java/api/com.azure.search.documents.models.searchoptions).
 
+Tp create a hybrid search:
+
 1. Create a `SearchHybrid.java` file in the `src/main/java/com/example/search` directory.
 
 1. Copy the following code into the file.
 
-    :::code language="java" source="~/azure-search-java-samples/vector-quickstart/src/main/java/com/example/search/SearchHybrid.java" :::
+    :::code language="java" source="~/azure-search-java-samples/quickstart-vector-search/src/main/java/com/example/search/SearchHybrid.java" :::
 
 1. Build and run the file.
 
     ```bash
     mvn compile exec:java -Dexec.mainClass="com.example.search.SearchHybrid"
     ```
 
-1. The output of this code shows the relevant documents for the hybrid search.
+    The output of this code shows the relevant documents for the hybrid search.
 
     ```output
     Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -342,7 +368,7 @@ This search uses [SearchClient](/java/api/com.azure.search.documents.searchclien
       Tags: ["pool","free wifi","air conditioning","concierge"]
     ```
 
-    Because Reciprocal Rank Fusion (RRF) merges results, it helps to review the inputs. The following results are from only the full-text query. The top two results are Sublime Palace Hotel and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
+    Because Reciprocal Rank Fusion (RRF) merges results, it helps to review the inputs. The following results are from the full-text query only. The top two results are Sublime Palace Hotel and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
 
     ```json
        {
@@ -357,7 +383,7 @@ This search uses [SearchClient](/java/api/com.azure.search.documents.searchclien
        },
     ```
 
-    In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to fourth position. Luxury Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
+    In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to the fourth position. Luxury Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
 
    ```json
    "value": [
@@ -419,19 +445,21 @@ Here's the last query in the collection to extend the semantic hybrid search wit
 
 This search uses [SearchClient](/java/api/com.azure.search.documents.searchclient).[SearchClient](/java/api/com.azure.search.documents.searchclient) and [SearchOptions](/java/api/com.azure.search.documents.models.searchoptions). 
 
+To create a semantic hybrid search:
+
 1. Create a `SearchSemanticHybrid.java` file in the `src/main/java/com/example/search` directory.
 
 1. Copy the following code into the file.
 
-    :::code language="java" source="~/azure-search-java-samples/vector-quickstart/src/main/java/com/example/search/SearchSemanticHybrid.java" :::
+    :::code language="java" source="~/azure-search-java-samples/quickstart-vector-search/src/main/java/com/example/search/SearchSemanticHybrid.java" :::
 
 1. Build and run the file.
 
     ```bash
     mvn compile exec:java -Dexec.mainClass="com.example.search.SearchSemanticHybrid"
     ```
 
-1. The output of this code shows the relevant documents for the semantic hybrid search.
+    The output of this code shows the relevant documents for the semantic hybrid search.
 
     ```output
     Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -484,19 +512,19 @@ This search uses [SearchClient](/java/api/com.azure.search.documents.searchclien
 
     - Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
 
-## Clean up
+## Clean up resources
 
 When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
 
 You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
 
-If you want to keep your search service but delete the index and its documents, you can delete the index programmatically.
+Alternatively, to delete the vector index you created in this quickstart programmatically:
 
 1. Create a `DeleteIndex.java` file in the `src/main/java/com/example/search` directory.
 
 1. Add the following code to the file.
 
-    :::code language="java" source="~/azure-search-java-samples/vector-quickstart/src/main/java/com/example/search/DeleteIndex.java" :::
+    :::code language="java" source="~/azure-search-java-samples/quickstart-vector-search/src/main/java/com/example/search/DeleteIndex.java" :::
 
 1. Build and run the file.
 
@@ -506,4 +534,4 @@ If you want to keep your search service but delete the index and its documents,
 
 ## Next steps
 
-- Review the repository of code samples for vector search capabilities in Azure AI Search for [Java](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-java)
++ Review the repository of code samples for vector search capabilities in Azure AI Search for [Java](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-java).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java用ベクトル検索クイックスタートのドキュメント更新"
}
```

### Explanation
この変更は、`search-get-started-vector-java.md` ファイルにおいて、Javaを使用したベクトルインデックスの作成、読み込み、検索に関する情報を更新するものです。主な変更点としては、文書の日付が「12/15/2025」から「01/14/2026」に変更され、`ms.custom` メタデータに `dev-focus` が追加されています。これにより、本ドキュメントの目的とコンテキストがより明確になりました。

内容の詳細については、Azure AI Search クライアントライブラリを使用して、どのようにベクトルインデックスを操作するかの説明が改善されています。特に、インデックススキーマ、ベクトルフィールドの設定、データのアップロード方法について、コード例とともに詳しく述べられています。また、事前に必要な環境設定やAPIエンドポイントの取得方法もわかりやすく更新されました。

新たに追加された手順には、ドキュメントのアップロードや検索の実行に関する明確な指示が含まれており、特にフィルターやジオスペーシャル検索の使用について説明が強化されています。これにより、開発者は検索機能を活かしたアプリケーションをより簡単に実装できるようになります。

最後に、ドキュメントは全体的に読みやすさを考慮して整理されており、使用するコードとその実行方法が一貫して提供されているため、ユーザーがスムーズに理解しやすくなっています。

## articles/search/includes/quickstarts/search-get-started-vector-javascript.md{#item-d0387c}

<details>
<summary>Diff</summary>
````diff
@@ -4,44 +4,48 @@ author: diberry
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 01/14/2026
+ms.custom: dev-focus
+ai-usage: ai-assisted
 ---
 
-In this quickstart, you use JavaScript to create, load, and query vectors. The code examples perform these operations by using the [Azure AI Search client library](/javascript/api/overview/azure/search-documents-readme). The library provides an abstraction over the REST API for access to index operations such as data ingestion, search operations, and index management operations.
+In this quickstart, you use JavaScript to create, load, and query a [vector index](../../vector-store.md). The code performs these operations by using the [Azure AI Search client library for JavaScript](/javascript/api/overview/azure/search-documents-readme), which provides an abstraction over the REST APIs to access index operations.
 
-In Azure AI Search, a [vector store](../../vector-store.md) has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. The [Create Index](/rest/api/searchservice/indexes/create-or-update) REST API creates the vector store.
+In Azure AI Search, a vector index has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. [Indexes - Create or Update](/rest/api/searchservice/indexes/create-or-update) (REST API) creates the vector index.
 
 > [!NOTE]
 > This quickstart omits the vectorization step and provides inline embeddings. If you want to add [built-in data chunking and vectorization](../../vector-search-integrated-vectorization.md) over your own content, try the [**Import data (new)** wizard](../../search-get-started-portal-import-vectors.md) for an end-to-end walkthrough.
 
 ## Prerequisites
 
-- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch) in your current subscription.
-    - The `Search Index Data Contributor` role assigned at the scope of the service.
-    - You can use a free search service for most of this quickstart, but we recommend the Basic tier or higher for larger data files.
-    - To run the query example that invokes [semantic reranking](../../semantic-search-overview.md), your search service must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
++ An [Azure AI Search service](../../search-create-service-portal.md).
 
-- [Visual Studio Code](https://code.visualstudio.com/download).
+    + You can use the Free tier for most of this quickstart, but we recommend Basic or higher for larger data files.
 
-- [Node.JS with LTS](https://nodejs.org/en/download/).
+    + For [keyless authentication](../../search-get-started-rbac.md) with Microsoft Entra ID, assign the **Search Index Data Contributor role** to your user account.
+    
+    + To run the semantic hybrid query, you must [enable semantic ranker](../../semantic-how-to-enable-disable.md).
+
++ [Visual Studio Code](https://code.visualstudio.com/download).
+
++ [Node.JS with LTS](https://nodejs.org/en/download/).
 
 ## Get service endpoints
 
 In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints so that you can provide them as variables in your code.
 
+To get the service endpoint:
+
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
 1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
 
-1. On the **Overview** home page, copy the URL. An example endpoint might look like `https://example.search.windows.net`. 
-
+1. On the **Overview** home page, copy the URL. An example endpoint might look like `https://example.search.windows.net`.
 
 ## Set up the Node.JS project
 
-Set up project with Visual Studio Code and JavaScript.
-
 1. Start Visual Studio Code in a new directory.
 
    ```bash
@@ -57,8 +61,7 @@ Set up project with Visual Studio Code and JavaScript.
 
    This creates a `package.json` file with default values.
 
-
-1. Install the following npm packages.
+1. Install the following `npm` packages.
 
    ```bash
    npm install @azure/identity @azure/search-documents dotenv
@@ -73,6 +76,7 @@ Set up project with Visual Studio Code and JavaScript.
 ## Set up environment variables for local development
 
 1. Create a `.env` file in your `vector-quickstart` project directory.
+
 1. Add the following environment variables to the `.env` file, replacing the values with your own service endpoints and keys.
 
    ```plaintext
@@ -95,11 +99,12 @@ az login --tenant <PUT YOUR TENANT ID HERE>
 
 You should now be logged in to Azure from your local device.
 
-
-## Create the vector index 
+## Create a vector index
 
 In this section, you create a vector index in Azure AI Search with [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient).[createOrUpdateIndex](/javascript/api/@azure/search-documents/searchindexclient#@azure-search-documents-searchindexclient-createorupdateindex). The index schema defines the fields, including the vector field `DescriptionVector`. 
 
+To create a vector index:
+
 1. Create a `createIndex.js` file in the `src` directory.
 
 1. Copy the following code into the file. 
@@ -108,12 +113,13 @@ In this section, you create a vector index in Azure AI Search with [SearchIndexC
 
     The code file adds the dependencies, environment variables, and JavaScript type for `HotelDocument` to the top of the file. Add the `createIndex` function to create the index. The function defines the index schema, including the vector field `DescriptionVector`.
 
-1. Run the file:
+1. Run the file.
 
     ```bash
     node -r dotenv/config src/createIndex.js
     ```
-1. The output of this code shows that the index is created successfully:
+
+   The output of this code shows that the index is created successfully.
 
     ```output
     Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -122,25 +128,32 @@ In this section, you create a vector index in Azure AI Search with [SearchIndexC
     hotels-vector-quickstart created
     ```
 
-   Key takeaways when creating vector index with the `@azure/search-documents` library:
+   Key takeaways:
+
+   + You define an index by creating a list of fields. 
+
+   + This particular index supports multiple search capabilities, such as:
 
-   - You define an index by creating a list of fields. 
+      + Full-text keyword search (`searchable`)
 
-   - This particular index supports multiple search capabilities, such as:
-      - Full-text keyword search (`searchable`)
-      - Vector search (enables hybrid search by collocating vector and nonvector fields) fields (`DescriptionVector` with `vectorSearchProfileName`)
-      - Semantic search 
-      - Faceted search (`searchSuggester`)
-      - Geo-spatial search (`Location` field with `geo.distance`)
-      - Filtering, sorting (Many fields marked filterable and sortable)
+      + Vector search (enables hybrid search by collocating vector and nonvector fields) fields (`DescriptionVector` with `vectorSearchProfileName`)
 
+      + Semantic search 
+
+      + Faceted search (`searchSuggester`)
+
+      + Geo-spatial search (`Location` field with `geo.distance`)
+
+      + Filtering, sorting (many fields marked filterable and sortable)
 
 ## Upload documents to the index
 
-Creating and loading the index are separate steps. You created the index schema in the [previous step](#create-the-vector-index). Now you need to load documents into the index with [SearchClient](/javascript/api/@azure/search-documents/searchclient).[uploadDocuments](/javascript/api/%40azure/search-documents/searchclient#@azure-search-documents-searchclient-uploaddocuments). The documents contain the vectorized version of the article's description, which enables similarity search based on meaning rather than exact keywords.
+Creating and loading the index are separate steps. You created the index schema in the previous step. You now need to load documents into the index with [SearchClient](/javascript/api/@azure/search-documents/searchclient).[uploadDocuments](/javascript/api/%40azure/search-documents/searchclient#@azure-search-documents-searchclient-uploaddocuments). The documents contain the vectorized version of the article's description, which enables similarity search based on meaning rather than exact keywords.
 
 In Azure AI Search, the index stores all searchable content, while the search engine executes queries against that index.
 
+To upload documents to the index:
+
 1. Create an `uploadDocuments.js` file in the `src` directory.
 1. Copy the following code into the file.
 
@@ -150,12 +163,13 @@ In Azure AI Search, the index stores all searchable content, while the search en
 
     Because this quickstart article searches the index immediately, the `waitUntilIndexed` function waits until the index is ready for search operations. This is important because the index needs to be fully populated with documents before you can perform searches.
 
-1. Build and run the file:
+1. Build and run the file.
 
     ```bash
     node -r dotenv/config src/uploadDocuments.js
     ```
-1. The output of this code shows that the documents are indexed and ready for search:
+
+   The output of this code shows that the documents are indexed and ready for search.
 
     ```output
     Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -172,34 +186,39 @@ In Azure AI Search, the index stores all searchable content, while the search en
     All documents indexed successfully.
     ```
 
-    Key takeaways about the uploadDocuments() method and this example:
-    
-    * Your code interacts with a specific search index hosted in your Azure AI Search service through the SearchClient, which is the main object provided by the @azure/search-documents package. The SearchClient provides access to index operations such as:
-        * Data ingestion - uploadDocuments(), mergeDocuments(), deleteDocuments(), etc.
-        * Search operations - search(), autocomplete(), suggest()
-        * Index management operations such as createIndex(), deleteIndex(), getIndex(), etc.
-    * Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 4096 floating point values each. This quickstart sets the dimensions attribute to 1,536 because that's the size of embeddings generated by the Azure OpenAI text-embedding-ada-002 model.
+    Key takeaways:
+
+    * Your code interacts with a specific search index hosted in your Azure AI Search service through the `SearchClient`, which is the main object provided by the @azure/search-documents package. The `SearchClient` provides access to index operations, such as:
+
+        * Data ingestion: `uploadDocuments`, `mergeDocuments`, `deleteDocuments`, and so on.
+
+        * Search operations: `search`, `autocomplete`, `suggest`
+
+        * Index management operations: `createIndex`, `deleteIndex`, `getIndex`, and so on.
+
+    * Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 4096 floating point values each. This quickstart sets the dimensions attribute to 1,536 because that's the size of embeddings generated by the `text-embedding-ada-002` model.
 
 ## Create the query as a vector
 
 The example vector queries are based on two strings:
 
-- **Search string**: `historic hotel walk to restaurants and shopping`
-- **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
++ Search string: `historic hotel walk to restaurants and shopping`
++ Vector query string: `quintessential lodging near running trails, eateries, retail` (vectorized into a mathematical representation)
 
 The vector query string is semantically similar to the search string, but it includes terms that don't exist in the search index. If you do a keyword search for `quintessential lodging near running trails, eateries, retail`, results are zero. We use this example to show how you can get relevant results even if there are no matching terms.
 
-1. Create a `queryVector.js` file in the `src` directory and add the code to create the query vector.
+Create a `queryVector.js` file in the `src` directory and add the code to create the query vector.
 
-    :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/queryVector.js" :::
-
-1. This code is used in the following sections to perform vector searches. The query vector is created using an embedding model from Azure OpenAI.
+:::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/queryVector.js" :::
 
+This code is used in the following sections to perform vector searches. The query vector is created using an embedding model from Azure OpenAI.
 
 ## Create a single vector search
 
 The first example demonstrates a basic scenario where you want to find document descriptions that closely match the search string using the [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions).
 
+To create a single vector search:
+
 1. Create a `searchSingle.js` file in the `src` directory.
 
 1. Copy the following code into the file.
@@ -210,13 +229,13 @@ The first example demonstrates a basic scenario where you want to find document
 
     The vector query string is `quintessential lodging near running trails, eateries, retail`, which is vectorized into 1,536 embeddings for this query.
 
-1. Build and run the file:
+1. Build and run the file.
 
     ```bash
     node -r dotenv/config src/searchSingle.js
     ```
 
-1. The output of this code shows the relevant docs for the query `quintessential lodging near running trails, eateries, retail`. 
+   The output of this code shows the relevant docs for the query `quintessential lodging near running trails, eateries, retail`.
 
     ```output
     Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -238,6 +257,8 @@ The first example demonstrates a basic scenario where you want to find document
 
 You can add filters, but the filters are applied to the nonvector content in your index. In this example, the filter applies to the `Tags` field to filter out any hotels that don't provide free Wi-Fi. This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
 
+To create a single vector search with a filter:
+
 1. Create a `searchSingleWithFilter.js` file in the `src` directory.
 
 1. Copy the following code into the file.
@@ -246,12 +267,13 @@ You can add filters, but the filters are applied to the nonvector content in you
 
     Add the dependencies, environment variables, and the same search functionality as the previous search with a post-processing exclusion filter added for hotels with `free wifi`.
 
-1. Build and run the file:
+1. Build and run the file.
 
     ```bash
     node -r dotenv/config src/searchSingleWithFilter.js
     ```
-1. The output of this code shows the relevant documents for the query with the filter for `free wifi` applied:
+
+   The output of this code shows the relevant documents for the query with the filter for `free wifi` applied.
 
     ```output
     Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -267,18 +289,20 @@ You can add filters, but the filters are applied to the nonvector content in you
 
 You can specify a geospatial filter to limit results to a specific geographic area. In this example, the filter limits results to hotels within 300 kilometers of Washington D.C. (coordinates: `-77.03241 38.90166`). Geospatial distances are always in kilometers. This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
 
+To create a search with a geospatial filter:
+
 1. Create a `searchSingleWithFilterGeo.js` file in the `src` directory.
 
 1. Copy the following code into the file.
 
     :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/searchSingleWithFilterGeo.js" :::
-1. Build and run the file:
+1. Build and run the file.
 
     ```bash
     node -r dotenv/config src/searchSingleWithFilterGeo.js
     ```
 
-1. The output of this code shows the relevant documents for the query with the geospatial post-processing exclusion filter applied:
+   The output of this code shows the relevant documents for the query with the geospatial post-processing exclusion filter applied.
 
     ```output
     Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -290,26 +314,28 @@ You can specify a geospatial filter to limit results to a specific geographic ar
     - HotelId: 49, HotelName: Swirling Currents Hotel, Tags: N/A, Score 0.602634072303772
     ```
 
-
 ## Create a hybrid search
 
 Hybrid search consists of keyword queries and vector queries in a single search request. This example runs the vector query and full-text search concurrently:
 
-- **Search string**: `historic hotel walk to restaurants and shopping`
-- **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
++ Search string: `historic hotel walk to restaurants and shopping`
++ Vector query string: `quintessential lodging near running trails, eateries, retail` (vectorized into a mathematical representation)
 
 This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
 
+To create a hybrid search:
+
 1. Create a `searchHybrid.js` file in the `src` directory.
 1. Copy the following code into the file.
 
     :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/searchHybrid.js" :::
-1. Build and run the file:
+1. Build and run the file.
 
     ```bash
     node -r dotenv/config src/searchHybrid.js
     ```
-1. The output of this code shows the relevant documents for the hybrid search:
+
+   The output of this code shows the relevant documents for the hybrid search.
 
     ```output
     Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -353,7 +379,7 @@ This search uses [SearchClient](/javascript/api/@azure/search-documents/searchcl
       Tags: ["pool","free wifi","air conditioning","concierge"]
     ```
 
-    Because Reciprocal Rank Fusion (RRF) merges results, it helps to review the inputs. The following results are from only the full-text query. The top two results are Sublime Palace Hotel and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
+    Because Reciprocal Rank Fusion (RRF) merges results, it helps to review the inputs. The following results are from the full-text query only. The top two results are Sublime Palace Hotel and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
 
     ```json
        {
@@ -368,7 +394,7 @@ This search uses [SearchClient](/javascript/api/@azure/search-documents/searchcl
        },
     ```
 
-    In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to fourth position. Luxury Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
+    In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to the fourth position. Luxury Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
    
    ```json
    "value": [
@@ -430,18 +456,21 @@ Here's the last query in the collection to extend the semantic hybrid search wit
 
 This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
 
+To create a semantic hybrid search:
+
 1. Create a `searchSemanticHybrid.js` file in the `src` directory.
+
 1. Copy the following code into the file.
 
     :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/searchSemanticHybrid.js" :::
 
-1. Build and run the file:
+1. Build and run the file.
 
     ```bash
     node -r dotenv/config src/searchSemanticHybrid.js
     ```
 
-1. The output of this code shows the relevant documents for the semantic hybrid search:
+   The output of this code shows the relevant documents for the semantic hybrid search.
 
     ```output
     Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -495,25 +524,25 @@ This search uses [SearchClient](/javascript/api/@azure/search-documents/searchcl
 
     - Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
 
-## Clean up
+## Clean up resources
 
 When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
 
 You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
 
-If you want to keep your search service but delete the index and its documents, you can delete the index programmatically.
+Alternatively, to delete the vector index you created in this quickstart programmatically:
 
 1. Create a `deleteIndex.js` file in the `src` directory.
 1. Add the dependencies, environment variables, and code to delete the index.
 
     :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/deleteIndex.js" :::
 
-1. Build and run the file:
+1. Build and run the file.
 
     ```bash
     node -r dotenv/config src/deleteIndex.js
     ```
 
 ## Next steps
 
-- Review the repository of code samples for vector search capabilities in Azure AI Search for [JavaScript](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript)
\ No newline at end of file
++ Review the repository of code samples for vector search capabilities in Azure AI Search for [JavaScript](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript用ベクトル検索のクイックスタートドキュメントの更新"
}
```

### Explanation
この変更は、`search-get-started-vector-javascript.md` ファイルに対する改訂を示しており、JavaScriptを用いたベクトルインデックスの作成、読み込み、検索に関連する情報を最新化しています。主な変更には、文書の日付を「11/20/2025」から「01/14/2026」に変更し、新しいメタデータ `ms.custom` と `ai-usage` を追加した点が含まれています。

内容に関しては、Azure AI Search クライアントライブラリを使用してベクトルインデックスを作成する方法についての説明が強化されており、設計したインデックススキーマ、ベクトルフィールド、それぞれのフィールドの操作に関する詳しい情報が加わっています。また、環境設定やAPIエンドポイントの取得方法がクリアに示されており、ユーザーがスタートアッププロジェクトを簡単にセットアップできるようになっています。

ナビゲーションやプロジェクト設定手順が改善され、特にnpmパッケージのインストール手順や環境変数の設定が明示的に述べられています。文書の全体構成はより整理され、実行する際の出力例を通して得られる情報が強調されているため、開発者がコードを実装する際の理解が深まるよう工夫されています。

新たに追加された操作や検索機能に関する手順が詳細で、特にフィルターやジオスペーシャル検索のセクションがより明確になっています。これにより、開発者は実際のシナリオに即した形でより効果的にベクトル検索を実施しやすくなっています。全体として、使用する際の利便性と理解のしやすさが向上したクイックスタートガイドとなっています。

## articles/search/includes/quickstarts/search-get-started-vector-python.md{#item-53085f}

<details>
<summary>Diff</summary>
````diff
@@ -4,35 +4,40 @@ author: rotabor
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 01/14/2026
+ms.custom: dev-focus
+ai-usage: ai-assisted
 ---
 
-In this quickstart, you use a Jupyter notebook to create, load, and query vectors. The code examples perform these operations by using the [Azure AI Search client library](/python/api/overview/azure/search-documents-readme). The library provides an abstraction over the REST API for access to index operations such as data ingestion, search operations, and index management operations.
+In this quickstart, you use a Jupyter notebook to create, load, and query a [vector index](../../vector-store.md). The code performs these operations by using the [Azure AI Search client library for Python](/python/api/overview/azure/search-documents-readme), which provides an abstraction over the REST APIs to access index operations.
 
-In Azure AI Search, a [vector store](../../vector-store.md) has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. The [Create Index](/rest/api/searchservice/indexes/create-or-update) REST API creates the vector store.
+In Azure AI Search, a vector index has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. [Indexes - Create or Update](/rest/api/searchservice/indexes/create-or-update) (REST API) creates the vector index.
 
 > [!NOTE]
 > This quickstart omits the vectorization step and provides inline embeddings. If you want to add [built-in data chunking and vectorization](../../vector-search-integrated-vectorization.md) over your own content, try the [**Import data (new)** wizard](../../search-get-started-portal-import-vectors.md) for an end-to-end walkthrough.
 
 ## Prerequisites
 
-- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch) in your current subscription.
-    - You can use a free search service for most of this quickstart, but we recommend the Basic tier or higher for larger data files.
-    - To run the query example that invokes [semantic reranking](../../semantic-search-overview.md), your search service must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
++ An [Azure AI Search service](../../search-create-service-portal.md).
 
-- [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter package](https://pypi.org/project/jupyter/).
+    + You can use the Free tier for most of this quickstart, but we recommend Basic or higher for larger data files.
 
-- [Git](https://git-scm.com/downloads) to clone the repo containing the Jupyter notebook and other related files.
+    + For [keyless authentication](../../search-get-started-rbac.md) with Microsoft Entra ID, assign the **Search Index Data Contributor role** to your user account.
+    
+    + To run the semantic hybrid query, you must [enable semantic ranker](../../semantic-how-to-enable-disable.md).
+
++ [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter package](https://pypi.org/project/jupyter/).
+
++ [Git](https://git-scm.com/downloads) to clone the sample repo.
 
 ## Get service information
 
-Requests to the search endpoint must be authenticated and authorized. While it's possible to use API keys or roles for this task, we recommend [using a keyless connection via Microsoft Entra ID](../../search-get-started-rbac.md).
+Requests to the search endpoint must be authenticated and authorized. While it's possible to use API keys for this task, we recommend [using a keyless connection via Microsoft Entra ID](../../search-get-started-rbac.md).
 
 This quickstart uses `DefaultAzureCredential`, which simplifies authentication in both development and production scenarios. However, for production scenarios, you might have more advanced requirements that require a different approach. See [Authenticate Python apps to Azure services by using the Azure SDK for Python](/azure/developer/python/sdk/authentication/overview) to understand all of your options.
 
-
 ## Clone the code and setup environment
 
 1. Clone the repo containing the code for this quickstart. 
@@ -41,25 +46,15 @@ This quickstart uses `DefaultAzureCredential`, which simplifies authentication i
    git clone https://github.com/Azure-Samples/azure-search-python-samples
    ```
   
-   This repo has Python code examples for several articles each in a separate subfolder.
-
-1. In Visual Studio Code, open the subfolder `Quickstart-Vector-Search`.
+1. In Visual Studio Code, open the `Quickstart-Vector-Search` folder.
 
-   There are three files in this folder:
+1. Rename the `sample.env` file to `.env`.
 
-   - `vector-search-quickstart.ipynb`
-   - `requirements.txt`
-   - `sample.env`
-
-1. Rename the `sample.env` file to `.env` and modify the values in the `.env` file. 
-
-   Use the search service URL as the `AZURE_SEARCH_ENDPOINT`. You can find the url in the [Azure portal](https://portal.azure.com). Go to your Azure AI Search service, on the **Overview** page, look for the URL field. An example endpoint might look like `https://mydemo.search.windows.net`. 
-   
-   Finally, choose a new `AZURE_SEARCH_INDEX_NAME` name, or use the one provided in the file.
+1. Set `AZURE_SEARCH_ENDPOINT` to your search service URL, which should be similar to `https://mydemo.search.windows.net`.
 
-1. In Visual Studio Code, work in an environment. On the **View** menu, select **Terminal...**, or select <kbd>Ctrl</kbd>+<kbd>`</kbd>.
+1. Set `AZURE_SEARCH_INDEX_NAME` to a unique name for your index. You can also use the default `vector-search-quickstart` name.
 
-1. Run the following commands in the terminal:
+1. Select **View** > **New Terminal**, and then run the following commands to create and activate a virtual environment.
 
    ```bash
    python -m venv .venv
@@ -68,25 +63,21 @@ This quickstart uses `DefaultAzureCredential`, which simplifies authentication i
    ```
    
    > [!Note] 
-   > This assumes you're using Git Bash in your Terminal, and you're running on Windows. If you're using a different shell and/or a different operating system, adjust these instructions for your specific environment.
+   > + This step assumes you're using Git Bash in your terminal and running on Windows. If you're using a different shell and/or operating system, adjust these instructions to your specific environment.
+   >
+   > + The `where python` command validates that you're working from the virtual environment by listing `python.exe` in the `Quickstart-Vector-Search\.venv\` folder and other locations from your machine's directory.
 
-   If prompted, allow Visual Studio Code to use the new environment.
+1. If prompted, allow Visual Studio Code to use the new environment.
 
-   The `where python` command validates that you're working from the virtual environment by listing `python.exe` in the `Quickstart-Vector-Search\.venv\` folder, and other locations from your machine's directory.
-
-1. Install the required libraries by running the following command:
+1. Install the required libraries.
 
    ```bash
    pip install requirements.txt
    ```
 
-1. In Visual Studio Code, open the `vector-search-quickstart.ipynb`.
-
-   > [!Note]
-   > If this is the first time you have used a Jupyter Notebook (.ipynb) in Visual Studio Code, you will be prompted to install the Jupyter Notebook kernel and possibly other tools. Choose to install the suggested tools to continue with this quickstart.
+1. Open the `vector-search-quickstart.ipynb` file.
 
-
-1. Find the cell below section titled "Install packages and set variables" and select the **Execute Cell (Ctrl + Alt + Enter)** button (which looks like a typical run button) to the left of the cell. Executing the cell loads the environment variables, creates the DefaultAzureCredential, and prints values to the output to confirm that the notebook's dependencies and `.env` are set up correctly.
+1. Run the `Install packages and set variables` code cell to load the environment variables.
 
    ```python
    # Load environment variables from .env file
@@ -105,7 +96,7 @@ This quickstart uses `DefaultAzureCredential`, which simplifies authentication i
    print(f"Using Azure Search index: {index_name}")
    !pip list 
    ```
-   Executing this cell produces the following output.
+   The output includes some of the installed packages.
 
    ```output
    Using Azure Search endpoint: https://<search-service-name>.search.windows.net
@@ -127,14 +118,13 @@ This quickstart uses `DefaultAzureCredential`, which simplifies authentication i
    ...
    ```
   
-   There are many more packages that you can view in a scrollable element (see the message below the cell results).
-
+## Create a vector index
 
-## Create the vector index
+The code in `vector-search-quickstart.ipynb` uses several methods from the `azure.search.documents` library to create the vector index and searchable fields.
 
-The code in the `vector-search-quickstart.ipynb` uses several methods from the `azure.search.documents` library to create the vector index and searchable fields.
+To create the vector index:
 
-1. Find the cell below section titled "Create an index" and execute the cell to create the index.
+1. Run the `Create an index` code cell.
 
    ```python
    from azure.search.documents.indexes import SearchIndexClient
@@ -218,33 +208,39 @@ The code in the `vector-search-quickstart.ipynb` uses several methods from the `
    print(f' {result.name} created')
    ```
 
-   If the index is created successfully, you see the following result below the cell:
+   If the index is created successfully, the following output is displayed below the code cell.
 
    ```output
    vector-search-quickstart created
    ```
 
-   Key takeaways when creating vector index with the `azure.search.documents`:
+   Key takeaways:
+
+   + You define an index by creating a list of fields. Each field is created using a helper method that defines the field type and its settings.
+
+   + This particular index supports multiple search capabilities, such as:
+
+      + Full-text keyword search (`SearchableField(name="HotelName", ...)`, `SearchableField(name="Description", ...)`)
 
-   - You define an index by creating a list of fields. Each field is created using a helper method that defines the field type and its settings.
+      + Vector search (enables hybrid search by collocating vector and nonvector fields) fields (`DescriptionVector`)
 
-   - This particular index supports multiple search capabilities, such as:
-      - Full-text keyword search (`SearchableField(name="HotelName", ...)`, `SearchableField(name="Description", ...)`)
-      - Vector search (enables hybrid search by collocating vector and nonvector fields) fields (`DescriptionVector`)
-      - Semantic search (`semantic_search=SemanticSearch(configurations=[semantic_config])`)
-      - Faceted search (`facetable=True`)
-      - Semantic search (`semantic_search=SemanticSearch(configurations=[semantic_config])`)
-      - Geo-spatial search (`Location` field is `GeographyPoint`)
-      - Filtering, sorting (Many fields marked filterable and sortable)
+      + Semantic search (`semantic_search=SemanticSearch(configurations=[semantic_config])`)
 
+      + Faceted search (`facetable=True`)
 
-## Upload documents
+      + Geo-spatial search (`Location` field is `GeographyPoint`)
 
-Creating and loading the index are separate steps. You created the index schema [in the previous step](#create-a-vector-index). Now you need to load documents into the index.
+      + Filtering, sorting (many fields marked filterable and sortable)
+
+## Upload documents to the index
+
+Creating and loading the index are separate steps. You created the index schema in the previous step. You now need to load documents into the index.
  
 In Azure AI Search, the index stores all searchable content, while the search engine executes queries against that index.
 
-1. Find the cell below section titled "Create documents payload" and execute the cell. This cell contains the following code (truncated for brevity):
+To upload documents to the index:
+
+1. Run the `Create documents payload` code cell.
 
    ```python
       # Create a documents payload
@@ -290,7 +286,7 @@ In Azure AI Search, the index stores all searchable content, while the search en
    > [!IMPORTANT]
    > The code in this example isn't runnable. Several characters or lines are removed for brevity. Instead, run the code in the Jupyter notebook.
    
-1. Find the cell below section titled "Upload the documents" and execute the cell. This cell contains the following code (truncated for brevity):
+1. Run the `Upload the documents` code cell.
 
    ```python
    # Upload documents to the index
@@ -308,9 +304,9 @@ In Azure AI Search, the index stores all searchable content, while the search en
    index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
    ```
 
-   This creates an instance of the search client by calling the `SearchClient()` constructor, then calls the `upload_documents()` method on the object. 
+   This creates an instance of the search client by calling the `SearchClient()` constructor and then calling the `upload_documents()` method on the object. 
 
-   After you run the cell, the status of each document is printed below it:
+   After you run the cell, the status of each document is printed below it.
 
    ```output
    Key: 1, Succeeded: True, ErrorMessage: None
@@ -322,43 +318,45 @@ In Azure AI Search, the index stores all searchable content, while the search en
    Key: 13, Succeeded: True, ErrorMessage: None
    ```
 
-   Key takeaways about the `upload_documents()` method and this example:
+   Key takeaways:
 
-   - Your code interacts with a specific search index hosted in your Azure AI Search service through the `SearchClient`, which is the main object provided by the `azure-search-documents` package. The `SearchClient` provides access to index operations such as:
+   + Your code interacts with a specific search index hosted in your Azure AI Search service through the `SearchClient`, which is the main object provided by the `azure-search-documents` package. The `SearchClient` provides access to index operations, such as:
 
-      - **Data ingestion** - `upload_documents()`, `merge_documents()`, `delete_documents()`, etc.
-      - **Search operations** - `search()`, `autocomplete()`, `suggest()`
-      - **Index management operations** 
+      + Data ingestion: `upload_documents()`, `merge_documents()`, `delete_documents()`, etc.
+      
+      + Search operations: `search()`, `autocomplete()`, `suggest()`
 
-   - Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 4096 floating point values each. This quickstart sets the dimensions attribute to 1,536 because that's the size of embeddings generated by the Azure OpenAI **text-embedding-ada-002** model.
+      + Index management operations: `get_index_statistics()`, `get_document_count()`
+
+   + Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 4096 floating point values each. This quickstart sets the dimensions attribute to 1,536 because that's the size of embeddings generated by the `text-embedding-ada-002` model.
 
 ## Run queries
 
-Now that documents are loaded, you can issue vector queries against them by calling `search_client.search()` and passing in a VectorizedQuery object, the fields you want returned, the number of results, and so on.
+Now that documents are loaded, you can issue vector queries against them by calling `search_client.search()` and passing in a `VectorizedQuery` object, the fields you want returned, the number of results, and so on.
 
-In the next sections, we run queries against the `hotels-vector-quickstart` index. The queries include:
+Queries in this section:
 
-- [Single vector search](#single-vector-search)
-- [Single vector search with filter](#single-vector-search-with-filter)
-- [Hybrid search](#hybrid-search)
-- [Semantic hybrid search](#semantic-hybrid-search)
++ [Single vector search](#single-vector-search)
++ [Single vector search with filter](#single-vector-search-with-filter)
++ [Hybrid search](#hybrid-search)
++ [Semantic hybrid search](#semantic-hybrid-search)
 
 ### Create the vector query string
 
 The example vector queries are based on two strings:
 
-- **Search string**: `historic hotel walk to restaurants and shopping`
-- **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
++ Search string: `historic hotel walk to restaurants and shopping`
++ Vector query string: `quintessential lodging near running trails, eateries, retail` (vectorized into a mathematical representation)
 
 The vector query string is semantically similar to the search string, but it includes terms that don't exist in the search index. If you do a keyword search for `quintessential lodging near running trails, eateries, retail`, results are zero. We use this example to show how you can get relevant results even if there are no matching terms.
 
-- Find the cell below section titled "Create the vector query string" and execute the cell. This loads the `vector` variable with the vectorized query data required to run all of the searches in the next sections.
+1. Run the `Create the vector query string` code cell. This loads the `vector` variable with the vectorized query data required to run all of the searches in the next sections.
 
 ### Single vector search
 
 The first example demonstrates a basic scenario where you want to find document descriptions that closely match the search string.
 
-- Find the cell below section titled "Single vector search" and execute the cell. This block contains the request to query the search index.
+1. Run the `Single vector search` code cell. This block contains the request to query the search index.
 
    ```python
    # IMPORTANT: Before you run this code, make sure the documents were successfully
@@ -402,7 +400,7 @@ The first example demonstrates a basic scenario where you want to find document
 
    `search_client.search()` returns a dict-like object. Each result provides a search score, which can be accessed using `score = result.get("@search.score", "N/A")`. While not displayed in this example, in a similarity search, the response always includes `k` results ordered by the value similarity score.
 
-   After you run the cell, the status of each document is printed below it:
+   After you run the cell, the status of each document is printed below it.
 
    ```output
    Total results: 5
@@ -417,7 +415,9 @@ The first example demonstrates a basic scenario where you want to find document
 
 You can add filters, but the filters are applied to the nonvector content in your index. In this example, the filter applies to the `Tags` field to filter out any hotels that don't provide free Wi-Fi.
 
-1. Find the cell below section titled "Single vector search with filter" and execute the cell. This cell contains the request to query the search index.
+To create a single vector search with a filter:
+
+1. Run the `Single vector search with filter` code cell. This cell contains the request to query the search index.
 
     ```python
    if vector:
@@ -458,7 +458,7 @@ You can add filters, but the filters are applied to the nonvector content in you
 
    The query was the same as the previous [single vector search example](#single-vector-search), but it includes a post-processing exclusion filter and returns only the two hotels that have free Wi-Fi.
 
-1. The next filter example uses a **geo filter**. Run the cell in the section titled "Vector query with a geo filter". This block contains the request to query the search index.
+1. The next filter example uses a geo filter. Run the `Vector query with a geo filter` code cell. This block contains the request to query the search index.
 
    ```python
    if vector:
@@ -520,10 +520,12 @@ You can add filters, but the filters are applied to the nonvector content in you
 
 Hybrid search consists of keyword queries and vector queries in a single search request. This example runs the vector query and full-text search concurrently:
 
-- **Search string**: `historic hotel walk to restaurants and shopping`
-- **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
++ Search string: `historic hotel walk to restaurants and shopping`
++ Vector query string: `quintessential lodging near running trails, eateries, retail` (vectorized into a mathematical representation)
 
-- Find the cell below section titled "Hybrid search" and execute the cell. This block contains the request to query the search index.
+To create a hybrid search:
+
+1. Run the `Hybrid search` code cell. This block contains the request to query the search index.
 
    ```python
    if vector:
@@ -561,7 +563,7 @@ Hybrid search consists of keyword queries and vector queries in a single search
       print("No vector loaded, skipping search.")    
    ```
 
-   Review the response:
+1. Review the output below the cell.
 
    ```output
    Total hybrid results: 7
@@ -601,7 +603,7 @@ Hybrid search consists of keyword queries and vector queries in a single search
      Tags: ['pool', 'free wifi', 'air conditioning', 'concierge']
    ```
 
-   Because Reciprocal Rank Fusion (RRF) merges results, it helps to review the inputs. The following results are from only the full-text query. The top two results are Sublime Palace Hotel and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
+   Because Reciprocal Rank Fusion (RRF) merges results, it helps to review the inputs. The following results are from the full-text query only. The top two results are Sublime Palace Hotel and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
 
    ```json
    {
@@ -616,7 +618,7 @@ Hybrid search consists of keyword queries and vector queries in a single search
    },
    ```
 
-   In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to fourth position. Luxury Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
+   In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to the fourth position. Luxury Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
    
    ```json
    "value": [
@@ -676,7 +678,9 @@ Hybrid search consists of keyword queries and vector queries in a single search
 
 Here's the last query in the collection. This hybrid query specifies the semantic query type and a semantic configuration, demonstrating that you can build a hybrid query that uses semantic reranking.
 
-- Find the cell below section titled "Semantic hybrid search" and execute the cell. This code block contains the request to query the search index.
+To create a semantic hybrid search:
+
+1. Run the `Semantic hybrid search` code cell. This code block contains the request to query the search index.
 
    ```python
    if semantic_hybrid_query_vector:
@@ -719,9 +723,9 @@ Here's the last query in the collection. This hybrid query specifies the semanti
       print("No vector loaded, skipping search.")
    ```
 
-   Review the output below the cell.
+1. Review the output below the cell.
 
-   With semantic ranking, the Swirling Currents Hotel now moves into the top spot. W
+   With semantic ranking, the Swirling Currents Hotel now moves into the top spot.
 
    ```output
    Total semantic hybrid results: 7
@@ -757,23 +761,23 @@ Here's the last query in the collection. This hybrid query specifies the semanti
      Category: Suite
    ```
 
-You can think of the semantic ranking as a way to improve the relevance of search results by understanding the meaning behind the words in the query and the content of the documents. In this case, the semantic ranking helps to identify hotels that are not only relevant to the keywords but also match the intent of the query:
-
-Key takeaways:
-
-- Vector search is specified through the `vectors.value` property. Keyword search is specified through the `search` property.
-
-- In a hybrid search, you can integrate vector search with full-text search over keywords. Filters, spell check, and semantic ranking apply to textual content only, and not vectors. In this final query, there's no semantic `answer` because the system didn't produce one that was sufficiently strong.
-
-- Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
+    You can think of the semantic ranking as a way to improve the relevance of search results by understanding the meaning behind the words in the query and the content of the documents. In this case, the semantic ranking helps to identify hotels that are not only relevant to the keywords but also match the intent of the query:
+    
+    Key takeaways:
+    
+    + Vector search is specified through the `vectors.value` property. Keyword search is specified through the `search` property.
+    
+    + In a hybrid search, you can integrate vector search with full-text search over keywords. Filters, spell check, and semantic ranking apply to textual content only, and not vectors. In this final query, there's no semantic `answer` because the system didn't produce one that was sufficiently strong.
+    
+    + Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
 
-## Clean up
+## Clean up resources
 
 When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
 
 You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
 
-If you want to keep the search service, but delete the index and documents, you can use the `SearchIndexClient` object's `delete_index()` method. Find the cell below section titled "Clean up" and execute the cell if you want to delete the `hotels-vector-quickstart` index:
+Alternatively, you can run the `Clean up` code cell to delete the vector index created in this quickstart.
 
 ```python
 index_client.delete_index(index_name)
@@ -782,5 +786,5 @@ print(f"Index '{index_name}' deleted successfully.")
 
 ## Next steps
 
-- Review the repository of code samples for vector search capabilities in Azure AI Search for [Python](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python)
-- Review the other Python and Azure AI Search code samples in the [azure-search-python-samples repo](https://github.com/Azure-Samples/azure-search-python-samples)
\ No newline at end of file
++ Review the repository of code samples for vector search capabilities in Azure AI Search for [Python](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python).
++ Review the other Python and Azure AI Search code samples in the [azure-search-python-samples repo](https://github.com/Azure-Samples/azure-search-python-samples).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python用ベクトル検索のクイックスタートドキュメントの更新"
}
```

### Explanation
この変更は、`search-get-started-vector-python.md` ファイルにおける更新を示しており、Jupyterノートブックを使用してPythonでベクトルインデックスを作成、読み込み、検索する際の手順が最新化されています。主な変更点には、文書の日付が「11/20/2025」から「01/14/2026」に変更され、新たに `ms.custom` と `ai-usage` メタデータが追加されています。

内容については、Azure AI Searchのクライアントライブラリを使用してコード例を通じてベクトルインデックスを作成する方法が詳述されており、特に関与するインデックススキーマや検索操作に関する情報が強化されています。また、環境の構成手順が明確に示されており、必要なツールやサービスについての推奨事項も含まれています。

更新された手順により、Gitリポジトリをクローンし、Jupyterノートブックを実行する際のステップが整理されており、ユーザーがスムーズに作業を進められるようになっています。特に、環境変数の設定やパッケージのインストールに関する具体的な指示が増え、開発者が必要な準備を迅速に行うことができるよう配慮されています。

また、文書の詳細部分には、ベクトル検索、単一ベクトル検索、ハイブリッド検索などの具体的なコード例が示され、それぞれの実行結果が明確に出力として表示されるようになっています。この改善により、読者は期待される結果を簡単に確認しながら実装を進められます。

全体として、このドキュメント更新によってPythonを使用したベクトル検索のクイックスタートが、より分かりやすく、実践的な内容になっています。

## articles/search/includes/quickstarts/search-get-started-vector-rest.md{#item-c7d261}

<details>
<summary>Diff</summary>
````diff
@@ -4,25 +4,29 @@ author: haileytapia
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 01/14/2026
+ms.custom: dev-focus
+ai-usage: ai-assisted
 ---
 
-In this quickstart, you use the [Azure AI Search REST APIs](/rest/api/searchservice) to create, load, and query vectors.
+In this quickstart, you use the [Azure AI Search REST APIs](/rest/api/searchservice) to create, load, and query a [vector index](../../vector-store.md).
 
-In Azure AI Search, a [vector store](../../vector-store.md) has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. The [Create Index](/rest/api/searchservice/indexes/create-or-update) REST API creates the vector store.
+In Azure AI Search, a vector index has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. [Indexes - Create or Update](/rest/api/searchservice/indexes/create-or-update) (REST API) creates the vector index.
 
 > [!NOTE]
 > This quickstart omits the vectorization step and provides inline embeddings. If you want to add [built-in data chunking and vectorization](../../vector-search-integrated-vectorization.md) over your own content, try the [**Import data (new)** wizard](../../search-get-started-portal-import-vectors.md) for an end-to-end walkthrough.
 
 ## Prerequisites
 
-- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch) in your current subscription.
-    - You can use a free search service for most of this quickstart, but we recommend the Basic tier or higher for larger data files.
-    - To run the query example that invokes [semantic reranking](../../semantic-search-overview.md), your search service must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
++ An [Azure AI Search service](../../search-create-service-portal.md).
 
-- [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
+    + You can use the Free tier for most of this quickstart, but we recommend Basic or higher for larger data files.
+    
+    + To run the semantic hybrid query, you must [enable semantic ranker](../../semantic-how-to-enable-disable.md).
+
++ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
 ## Get service information
 
@@ -48,7 +52,6 @@ Select the tab that corresponds to your preferred authentication method. Use the
 
 #### [API key](#tab/api-key)
 
-
 1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch).
 
 1. On the **Overview** home page, find the URL. An example endpoint might look like `https://mydemo.search.windows.net`. 
@@ -65,39 +68,42 @@ Select the tab that corresponds to your preferred authentication method. Use the
 
 You use one `.rest` or `.http` file to run all the requests in this quickstart. You can download the REST file that contains the code for this quickstart, or you can create a new file in Visual Studio Code and copy the code into it.
 
-1. In Visual Studio Code, create a new file with a `.rest` or `.http` file extension. For example, `az-search-vector-quickstart.rest`. Copy and paste the raw contents of the [Azure-Samples/azure-search-rest-samples/blob/main/Quickstart-vectors/az-search-vector-quickstart.rest](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) file into this new file. 
+To create the code file:
 
-1. At the top of the file, replace the placeholder value for `@baseUrl` with your search service URL. See the [Get service information](#get-service-information) section for instructions on how to find your search service URL.
+1. In Visual Studio Code, create a file with a `.rest` or `.http` file extension, such as `az-search-vector-quickstart.rest`.
 
+1. Copy and paste the raw contents of the [az-search-vector-quickstart.rest](https://github.com/Azure-Samples/azure-search-rest-samples/blob/main/Quickstart-vectors/az-search-quickstart-vectors.rest) file into the new file. 
 
    ```http
    @baseUrl = PUT-YOUR-SEARCH-SERVICE-URL-HERE
    ```
 
-1. At the top of the file, replace the placeholder value for authentication. See the [Get service information](#get-service-information) section for instructions on how to get your Microsoft Entra token or API key.
+1. Set `@baseUrl` to the endpoint you obtained in [Get service information](#get-service-information).
 
-    For the **recommended** keyless authentication via Microsoft Entra ID, you need to replace `@apiKey` with the `@token` variable.
-
-   ```http
-   @token = PUT-YOUR-MICROSOFT-ENTRA-TOKEN-HERE
-   ```
+1. Set the key or token for authentication. You obtained this value in [Get service information](#get-service-information).
 
-    If you prefer to use an API key, replace `@apiKey` with the key you copied from the Azure portal.
+   + For the **recommended** keyless authentication with Microsoft Entra ID, replace `@apiKey` with the `@token` variable.
 
-    ```http
-    @apiKey = PUT-YOUR-ADMIN-KEY-HERE
-    ```
+        ```http
+        @token = PUT-YOUR-MICROSOFT-ENTRA-TOKEN-HERE
+        ```
 
-1. For the **recommended** keyless authentication via Microsoft Entra ID, you need to replace `api-key: {{apiKey}}` with `Authorization: Bearer {{token}}` in the request headers. Replace all instances of `api-key: {{apiKey}}` that you find in the file.
+    + If you prefer to use an API key, replace `@apiKey` with the key you copied from the Azure portal.
 
+        ```http
+        @apiKey = PUT-YOUR-ADMIN-KEY-HERE
+        ```
 
+1. For the **recommended** keyless authentication with Microsoft Entra ID, replace all instances of `api-key: {{apiKey}}` with `Authorization: Bearer {{token}}` in the request headers.
 
 ## Create a vector index
 
-You use the [Create Index](/rest/api/searchservice/indexes/create) REST API to create a vector index and set up the physical data structures on your search service.
+You use [Indexes - Create](/rest/api/searchservice/indexes/create) (REST API) to create a vector index and set up the physical data structures on your search service.
 
 The index schema in this example is organized around hotel content. Sample data consists of vector and nonvector descriptions of fictitious hotels. This schema includes configurations for vector indexing and queries, and for semantic ranking.
 
+To create a vector index:
+
 1. In Visual Studio Code, open the `az-search-vector-quickstart.rest` file you [created earlier](#create-or-download-the-code-file).
 
 1. Find the `### Create a new index` code block in the file. This block contains the request to create the `hotels-vector-quickstart` index on your search service. 
@@ -378,21 +384,23 @@ The index schema in this example is organized around hotel content. Sample data
     }
     ```
 
-Key takeaways about the [Create Index](/rest/api/searchservice/indexes/create) REST API:
-
-- The `fields` collection includes a required key field and text and vector fields (such as `Description` and `DescriptionVector`) for text and vector search. Colocating vector and nonvector fields in the same index enables hybrid queries. For instance, you can combine filters, text search with semantic ranking, and vectors into a single query operation.
-
-- Vector fields must be one of the [EDM data types used for vectors](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields), such as `type: Collection(Edm.Single)`. Vector fields also have `dimensions` and `vectorSearchProfile` properties.
-
-- The `vectorSearch` section is an array of Approximate Nearest Neighbor (ANN) algorithm configurations and profiles. Supported algorithms include Hierarchical Navigable Small World and exhaustive K-Nearest Neighbor. For more information, see [Relevance scoring in vector search](../../vector-search-ranking.md).
-
-- The (optional) `semantic` configuration enables reranking of search results. You can rerank results in queries of type `semantic` for string fields that are specified in the configuration. To learn more, see [Semantic ranking overview](../../semantic-search-overview.md).
+    Key takeaways:
+    
+    + The `fields` collection includes a required key field and text and vector fields (such as `Description` and `DescriptionVector`) for text and vector search. Colocating vector and nonvector fields in the same index enables hybrid queries. For instance, you can combine filters, text search with semantic ranking, and vectors into a single query operation.
+    
+    + Vector fields must be one of the [EDM data types used for vectors](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields), such as `type: Collection(Edm.Single)`. Vector fields also have `dimensions` and `vectorSearchProfile` properties.
+    
+    + The `vectorSearch` section is an array of Approximate Nearest Neighbor (ANN) algorithm configurations and profiles. Supported algorithms include Hierarchical Navigable Small World and exhaustive K-Nearest Neighbor. For more information, see [Relevance scoring in vector search](../../vector-search-ranking.md).
+    
+    + The (optional) `semantic` configuration enables reranking of search results. You can rerank results in queries of type `semantic` for string fields that are specified in the configuration. To learn more, see [Semantic ranking overview](../../semantic-search-overview.md).
 
-## Upload documents
+## Upload documents to the index
 
-Creating and loading the index are separate steps. You created the index schema [in the previous step](#create-a-vector-index). Now you need to load documents into the index.
+Creating and loading the index are separate steps. You created the index schema in the previous step. You now need to load documents into the index.
  
-In Azure AI Search, the index contains all searchable data and queries run on the search service. For REST calls, the data is provided as JSON documents. Use [Documents- Index REST API](/rest/api/searchservice/documents/) for this task. The URI is extended to include the `docs` collection and the `index` operation.
+In Azure AI Search, the index contains all searchable data and queries run on the search service. For REST calls, the data is provided as JSON documents. Use [Documents - Index](/rest/api/searchservice/documents/) (REST API) for this task. The URI is extended to include the `docs` collection and the `index` operation.
+
+To upload documents to the index:
 
 1. Formulate an upload documents request to upload documents to the `hotels-vector-quickstart` index on your search service.
 
@@ -639,32 +647,34 @@ In Azure AI Search, the index contains all searchable data and queries run on th
 
 1. Select **Send Request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search documents.
 
-Key takeaways about the [Documents - Index REST API](/rest/api/searchservice/documents/) request:
-
-- Documents in the payload consist of fields defined in the index schema.
-
-- Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of `4096` floating point values each. This quickstart sets the dimensions attribute to 1,536 because that's the size of embeddings generated by the Azure OpenAI **text-embedding-3-small** model.
+    Key takeaways:
+    
+    + Documents in the payload consist of fields defined in the index schema.
+    
+    + Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 4096 floating point values each. This quickstart sets the dimensions attribute to 1,536 because that's the size of embeddings generated by the `text-embedding-ada-002` model.
 
 ## Run queries
 
-Now that documents are loaded, you can run vector queries against them by using [Documents - Search Post (REST)](/rest/api/searchservice/documents/search-post).
+Now that documents are loaded, you can run vector queries against them by using [Documents - Search Post](/rest/api/searchservice/documents/search-post) (REST API).
 
-In the next sections, we run queries against the `hotels-vector-quickstart` index. The queries include:
+Queries in this section:
 
-- [Single vector search](#single-vector-search)
-- [Single vector search with filter](#single-vector-search-with-filter)
-- [Hybrid search](#hybrid-search)
-- [Semantic hybrid search](#semantic-hybrid-search)
++ [Single vector search](#single-vector-search)
++ [Single vector search with filter](#single-vector-search-with-filter)
++ [Hybrid search](#hybrid-search)
++ [Semantic hybrid search](#semantic-hybrid-search)
 
 The example queries are based on two strings:
 
-- **Search string**: `historic hotel walk to restaurants and shopping`
-- **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
++ Search string: `historic hotel walk to restaurants and shopping`
++ Vector query string: `quintessential lodging near running trails, eateries, retail` (vectorized into a mathematical representation)
 
 The vector query string is semantically similar to the search string, but it includes terms that don't exist in the search index. If you do a keyword search for `quintessential lodging near running trails, eateries, retail`, results are zero in a pure keyword search without semantic ranking. We use this example to show how you can get relevant results using vectors, even if there are no matching terms.
 
 ### Single vector search
 
+To create a single vector search:
+
 1. Formulate the request. The query is a 1536 float representation of *quintessential lodging near running trails, eateries, retail*. The query is searching `DescriptionVector` and returning k-5 results. It's using the "exhaustive" override parameter to perform a full scan of the index instead of ANN. An exhaustive search is useful for small indexes.
 
     ```http
@@ -688,7 +698,7 @@ The vector query string is semantically similar to the search string, but it inc
         }
     ```
 
-   Key takeaways about the [Documents - Search Post](/rest/api/searchservice/documents/search-post) REST API:
+    Key takeaways about [Documents - Search Post](/rest/api/searchservice/documents/search-post) (REST API):
 
     + The `vectorQueries.vector` is the vector query string. It's a vector representation of *quintessential lodging near running trails, eateries, retail*, which is vectorized into 1,536 embeddings for this query.
 
@@ -776,6 +786,8 @@ The vector query string is semantically similar to the search string, but it inc
 
 You can add filters, but the filters are applied to the nonvector content in your index. In this example, the filter applies to the `Tags` field to filter out any hotels that don't provide free Wi-Fi.
 
+To create a single vector search with a filter:
+
 1. Formulate the request. This is the same request as the previous one, with an extra filter and filter mode parameter.
 
     ```http
@@ -906,8 +918,10 @@ You can add filters, but the filters are applied to the nonvector content in you
 
 Hybrid search consists of keyword queries and vector queries in a single search request. This example runs the vector query and full text search concurrently:
 
-- **Search string**: `historic hotel walk to restaurants and shopping`
-- **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
++ Search string: `historic hotel walk to restaurants and shopping`
++ Vector query string: `quintessential lodging near running trails, eateries, retail` (vectorized into a mathematical representation)
+
+To create a hybrid search:
 
 1. Formulate the hybrid query.
 
@@ -936,95 +950,97 @@ Hybrid search consists of keyword queries and vector queries in a single search
 
 1. Select **Send Request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
 
-Because this is a hybrid query, results are [ranked by Reciprocal Rank Fusion (RRF)](../../hybrid-search-ranking.md#scores-in-a-hybrid-search-results). Notice that `@search.score` values have a different basis and are uniformly smaller values. RRF evaluates search scores of multiple search results, takes the inverse, and then merges and sorts the combined results. The `top` number of results are returned.
-
-Review the response, consisting of the top k-5 matches out of 7 matching documents in the index:
-
-```json
-{
-  "@odata.count": 7,
-  "value": [
-    {
-      "@search.score": 0.03279569745063782,
-      "HotelName": "Sublime Palace Hotel",
-      "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience."
-    },
-    {
-      "@search.score": 0.032522473484277725,
-      "HotelName": "Luxury Lion Resort",
-      "Description": "Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort."
-    },
-    {
-      "@search.score": 0.03205128386616707,
-      "HotelName": "Nordick's Valley Motel",
-      "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley."
-    },
-    {
-      "@search.score": 0.0317460335791111,
-      "HotelName": "Swirling Currents Hotel",
-      "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary Wi-Fi and flat-screen TVs."
-    },
+    Because this is a hybrid query, results are [ranked by Reciprocal Rank Fusion (RRF)](../../hybrid-search-ranking.md#scores-in-a-hybrid-search-results). Notice that `@search.score` values have a different basis and are uniformly smaller values. RRF evaluates search scores of multiple search results, takes the inverse, and then merges and sorts the combined results. The `top` number of results are returned.
+    
+    Review the response, consisting of the top k-5 matches out of 7 matching documents in the index:
+    
+    ```json
     {
-      "@search.score": 0.03125,
-      "HotelName": "Old Century Hotel",
-      "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music."
+      "@odata.count": 7,
+      "value": [
+        {
+          "@search.score": 0.03279569745063782,
+          "HotelName": "Sublime Palace Hotel",
+          "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience."
+        },
+        {
+          "@search.score": 0.032522473484277725,
+          "HotelName": "Luxury Lion Resort",
+          "Description": "Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort."
+        },
+        {
+          "@search.score": 0.03205128386616707,
+          "HotelName": "Nordick's Valley Motel",
+          "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley."
+        },
+        {
+          "@search.score": 0.0317460335791111,
+          "HotelName": "Swirling Currents Hotel",
+          "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary Wi-Fi and flat-screen TVs."
+        },
+        {
+          "@search.score": 0.03125,
+          "HotelName": "Old Century Hotel",
+          "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music."
+        }
+      ]
     }
-  ]
-}
-```
-
-Because RRF merges results, it helps to review the inputs individually. 
-
-The following results are from the full-text portion of the query: *historic hotel walk to restaurants and shopping*. In the full text query, the top three results are Sublime Palace Hotel, Stay-Kay City Hotel, and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score. In the fused query, only two of these matches are in the top 3, and the second match (Stay-Kay City Hotel) doesn't appear in the top 5 at all.
-
-```json
-  "value": [
-    {
-      "@search.score": 1.4868739,
-      "HotelName": "Sublime Palace Hotel",
-      "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience."
-    },
-    {
-      "@search.score": 1.2699215,
-      "HotelName": "Stay-Kay City Hotel",
-      "Description": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities."
-    },
-    {
-      "@search.score": 1.2456272,
-      "HotelName": "Luxury Lion Resort",
-      "Description": "Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort."
-    },
-    ...
-  ]
-```
-
-In the vector portion query (*quintessential lodging near running trails, eateries, retail*) is a different string so we should expect different results. This query returns Nordick's Valley Motel, Luxury Lion Resort, and Sublime Palace Hotel as the top three matches. In the fused query, these results are in the top 3, but in reverse order.
-
-```json
-  "value": [
-    {
-      "@search.score": 0.6605852,
-      "HotelName": "Nordick's Valley Motel",
-      "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley."
-    },
-    {
-      "@search.score": 0.6333684,
-      "HotelName": "Luxury Lion Resort",
-      "Description": "Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort."
-    },
-    {
-      "@search.score": 0.605672,
-      "HotelName": "Sublime Palace Hotel",
-      "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience."
-    },
-   ...
-  ]
-```
+    ```
+    
+    Because RRF merges results, it helps to review the inputs individually. 
+    
+    The following results are from the full-text portion of the query: *historic hotel walk to restaurants and shopping*. In the full text query, the top three results are Sublime Palace Hotel, Stay-Kay City Hotel, and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score. In the fused query, only two of these matches are in the top 3, and the second match (Stay-Kay City Hotel) doesn't appear in the top 5 at all.
+    
+    ```json
+      "value": [
+        {
+          "@search.score": 1.4868739,
+          "HotelName": "Sublime Palace Hotel",
+          "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience."
+        },
+        {
+          "@search.score": 1.2699215,
+          "HotelName": "Stay-Kay City Hotel",
+          "Description": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities."
+        },
+        {
+          "@search.score": 1.2456272,
+          "HotelName": "Luxury Lion Resort",
+          "Description": "Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort."
+        },
+        ...
+      ]
+    ```
+    
+    In the vector portion query (*quintessential lodging near running trails, eateries, retail*) is a different string so we should expect different results. This query returns Nordick's Valley Motel, Luxury Lion Resort, and Sublime Palace Hotel as the top three matches. In the fused query, these results are in the top 3, but in reverse order.
+    
+    ```json
+      "value": [
+        {
+          "@search.score": 0.6605852,
+          "HotelName": "Nordick's Valley Motel",
+          "Description": "Only 90 miles (about 2 hours) from the nation's capital and nearby most everything the historic valley has to offer. Hiking? Wine Tasting? Exploring the caverns? It's all nearby and we have specially priced packages to help make our B&B your home base for fun while visiting the valley."
+        },
+        {
+          "@search.score": 0.6333684,
+          "HotelName": "Luxury Lion Resort",
+          "Description": "Unmatched Luxury. Visit our downtown hotel to indulge in luxury accommodations. Moments from the stadium and transportation hubs, we feature the best in convenience and comfort."
+        },
+        {
+          "@search.score": 0.605672,
+          "HotelName": "Sublime Palace Hotel",
+          "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience."
+        },
+       ...
+      ]
+    ```
 
 ### Semantic hybrid search
 
 Here's the last query in the collection. This hybrid query adds L2 semantic ranking that applies machine reading comprehension over the L1-ranked results, promoting more relevant matches to the top.
 
+To create a semantic hybrid search:
+
 1. Formulate the request. 
 
     ```http
@@ -1054,72 +1070,71 @@ Here's the last query in the collection. This hybrid query adds L2 semantic rank
 
 1. Select **Send Request**. You should have an `HTTP/1.1 200 OK` response. The response body should include the JSON representation of the search results.
 
-Review the response, consisting of a semantic reranking of the RRF-ranked results of the hybrid query. Semantic ranking works off of text inputs. In a text or hybrid query, this input is the text portion of the query (*historic hotel walk to restaurants and shopping*). To use semantic ranking on a pure vector query, such as the first example, or to explicitly control the text used for semantic ranking, [provide a semanticQuery string](../../semantic-how-to-query-request.md#set-up-the-query).
-
-After semantic reranking, Swirling Currents Hotel with its reference to *walking access to shopping, dining, entertainment and the city center* moves into the top spot. The machine comprehension model promotes *walking access to shopping and dining* as a closer match to *walk to restaurants and shopping*.
-
-Before semantic reranking, Sublime Palace, with its reference to *walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments* was number one.  
-
-```json
-{
-  "@odata.count": 7,
-  "@search.answers": [],
-  "value": [
-    {
-      "@search.score": 0.0317460335791111,
-      "@search.rerankerScore": 2.6550590991973877,
-      "HotelId": "49",
-      "HotelName": "Swirling Currents Hotel",
-      "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary Wi-Fi and flat-screen TVs.",
-      "Category": "Suite"
-    },
-    {
-      "@search.score": 0.03279569745063782,
-      "@search.rerankerScore": 2.599761724472046,
-      "HotelId": "4",
-      "HotelName": "Sublime Palace Hotel",
-      "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.",
-      "Category": "Boutique"
-    },
-    {
-      "@search.score": 0.03125,
-      "@search.rerankerScore": 2.3480887413024902,
-      "HotelId": "2",
-      "HotelName": "Old Century Hotel",
-      "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
-      "Category": "Boutique"
-    },
-    {
-      "@search.score": 0.03154495730996132,
-      "@search.rerankerScore": 2.2718777656555176,
-      "HotelId": "1",
-      "HotelName": "Stay-Kay City Hotel",
-      "Description": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic center of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
-      "Category": "Boutique"
-    },
+    Review the response, consisting of a semantic reranking of the RRF-ranked results of the hybrid query. Semantic ranking works off of text inputs. In a text or hybrid query, this input is the text portion of the query (*historic hotel walk to restaurants and shopping*). To use semantic ranking on a pure vector query, such as the first example, or to explicitly control the text used for semantic ranking, [provide a semanticQuery string](../../semantic-how-to-query-request.md#set-up-the-query).
+    
+    After semantic reranking, Swirling Currents Hotel with its reference to *walking access to shopping, dining, entertainment and the city center* moves into the top spot. The machine comprehension model promotes *walking access to shopping and dining* as a closer match to *walk to restaurants and shopping*.
+    
+    Before semantic reranking, Sublime Palace, with its reference to *walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments* was number one.  
+    
+    ```json
     {
-      "@search.score": 0.03053613007068634,
-      "@search.rerankerScore": 2.0582215785980225,
-      "HotelId": "3",
-      "HotelName": "Gastronomic Landscape Hotel",
-      "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel\u2019s restaurant services.",
-      "Category": "Suite"
+      "@odata.count": 7,
+      "@search.answers": [],
+      "value": [
+        {
+          "@search.score": 0.0317460335791111,
+          "@search.rerankerScore": 2.6550590991973877,
+          "HotelId": "49",
+          "HotelName": "Swirling Currents Hotel",
+          "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary Wi-Fi and flat-screen TVs.",
+          "Category": "Suite"
+        },
+        {
+          "@search.score": 0.03279569745063782,
+          "@search.rerankerScore": 2.599761724472046,
+          "HotelId": "4",
+          "HotelName": "Sublime Palace Hotel",
+          "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.",
+          "Category": "Boutique"
+        },
+        {
+          "@search.score": 0.03125,
+          "@search.rerankerScore": 2.3480887413024902,
+          "HotelId": "2",
+          "HotelName": "Old Century Hotel",
+          "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.",
+          "Category": "Boutique"
+        },
+        {
+          "@search.score": 0.03154495730996132,
+          "@search.rerankerScore": 2.2718777656555176,
+          "HotelId": "1",
+          "HotelName": "Stay-Kay City Hotel",
+          "Description": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic center of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
+          "Category": "Boutique"
+        },
+        {
+          "@search.score": 0.03053613007068634,
+          "@search.rerankerScore": 2.0582215785980225,
+          "HotelId": "3",
+          "HotelName": "Gastronomic Landscape Hotel",
+          "Description": "The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel\u2019s restaurant services.",
+          "Category": "Suite"
+        }
+      ]
     }
-  ]
-}
-```
+    ```
 
-> [!TIP]
->Semantically ranked results can include more detail, including semantic answers, captions, and highlights. Adding more parameters to the request produces the extra detail. For more information, see [Set up a semantic query](../../semantic-how-to-query-request.md?tabs=rest-query#set-up-the-query).
->
+    > [!TIP]
+    > Semantically ranked results can include more detail, including semantic answers, captions, and highlights. Adding more parameters to the request produces the extra detail. For more information, see [Set up a semantic query](../../semantic-how-to-query-request.md?tabs=rest-query#set-up-the-query).
 
-## Clean up
+## Clean up resources
 
 When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
 
 You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
 
-If you want to keep the search service, but delete the index and documents, you can use the `DELETE` command in the REST client. This command (at the end of your `az-search-vector-quickstart.rest` file) deletes the `hotels-vector-quickstart` index:
+Alternatively, you can send the following request to delete the vector index created in this quickstart.
 
 ```http
 ### Delete an index
@@ -1130,6 +1145,4 @@ DELETE  {{baseUrl}}/indexes/hotels-vector-quickstart?api-version=2025-09-01 HTTP
 
 ## Next steps
 
-As a next step, we recommend learning how to invoke REST API calls [without API keys](../../search-get-started-rbac.md).
-
-You might also want to review the demo code for [Python](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python), [C#](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet), or [JavaScript](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript).
++ Learn how to invoke REST API calls [without API keys](../../search-get-started-rbac.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIを用いたベクトル検索のクイックスタートドキュメントの更新"
}
```

### Explanation
この変更は、`search-get-started-vector-rest.md` ファイルの更新を示しており、Azure AI Search REST APIを利用してベクトルインデックスを作成、読み込み、検索する手順が最新化されています。主な変更点は、文書の日付が「11/20/2025」から「01/14/2026」に変更され、新たに `ms.custom` と `ai-usage`のメタデータが追加されたことです。

内容に関連して、クイックスタートガイドは、ベクトルインデックスの概念を明確にし、ユーザーがREST APIを使って操作を行う方法を詳細に説明しています。特に、インデックスの作成やドキュメントのアップロードに焦点を当てており、必要なAPIエンドポイントや認証情報を得る手順が詳述されています。

ドキュメントでは、従来のAPIキーによる認証方法に加え、Microsoft Entraによるキーレス認証を選択することも推奨されており、その手順が具体的に示されています。これにより、開発者がセキュアにAPIを操作するための柔軟性が向上しています。

また、各リクエストに対する事例が含まれ、複雑なクエリの作成や、検索の結果を確認する目安として、出力例も豊富に提供されています。特にハイブリッド検索やセマンティック検索の具体的な使用法に関する例が強調されており、これによりユーザーは複雑な検索クエリを構築する際の理解を深めることができます。

全体として、このドキュメントの更新により、AzureのREST APIを用いたベクトル検索がより理解しやすく、効果的なリソースとなっています。

## articles/search/includes/quickstarts/search-get-started-vector-typescript.md{#item-9b3bc8}

<details>
<summary>Diff</summary>
````diff
@@ -4,50 +4,53 @@ author: diberry
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 01/14/2026
+ms.custom: dev-focus
+ai-usage: ai-assisted
 ---
 
-In this quickstart, you use TypeScript to create, load, and query vectors. The code examples perform these operations by using the [Azure AI Search client library](/javascript/api/overview/azure/search-documents-readme). The library provides an abstraction over the REST API for access to index operations such as data ingestion, search operations, and index management operations.
+In this quickstart, you use TypeScript to create, load, and query a [vector index](../../vector-store.md). The code performs these operations by using the [Azure AI Search client library for TypeScript](/javascript/api/overview/azure/search-documents-readme), which provides an abstraction over the REST APIs to access index operations.
 
-In Azure AI Search, a [vector store](../../vector-store.md) has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. The [Create Index](/rest/api/searchservice/indexes/create-or-update) REST API creates the vector store.
+In Azure AI Search, a vector index has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. [Indexes - Create or Update](/rest/api/searchservice/indexes/create-or-update) (REST API) creates the vector index.
 
 > [!NOTE]
 > This quickstart omits the vectorization step and provides inline embeddings. If you want to add [built-in data chunking and vectorization](../../vector-search-integrated-vectorization.md) over your own content, try the [**Import data (new)** wizard](../../search-get-started-portal-import-vectors.md) for an end-to-end walkthrough.
 
 ## Prerequisites
 
-- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch) in your current subscription.
-    - The `Search Index Data Contributor` role assigned at the scope of the service.
-    - You can use a free search service for most of this quickstart, but we recommend the Basic tier or higher for larger data files.
-    - To run the query example that invokes [semantic reranking](../../semantic-search-overview.md), your search service must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
++ An [Azure AI Search service](../../search-create-service-portal.md).
 
-- [Visual Studio Code](https://code.visualstudio.com/download).
+    + You can use the Free tier for most of this quickstart, but we recommend Basic or higher for larger data files.
 
-- [Node.JS with LTS](https://nodejs.org/en/download/).
-- [TypeScript](https://www.typescriptlang.org/download). You can globally install TypeScript using npm:
+    + For [keyless authentication](../../search-get-started-rbac.md) with Microsoft Entra ID, assign the **Search Index Data Contributor role** to your user account.
+    
+    + To run the semantic hybrid query, you must [enable semantic ranker](../../semantic-how-to-enable-disable.md).
+
++ [Visual Studio Code](https://code.visualstudio.com/download).
+
++ [Node.JS with LTS](https://nodejs.org/en/download/).
++ [TypeScript](https://www.typescriptlang.org/download). You can globally install TypeScript using npm:
 
    ```bash
    npm install -g typescript
    ```
 
-## Get service endpoints
+## Get service information
 
 In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints so that you can provide them as variables in your code.
 
+To get the service endpoint:
+
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
 1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
 
 1. On the **Overview** home page, copy the URL. An example endpoint might look like `https://example.search.windows.net`. 
 
-
-
 ## Set up the Node.JS project
 
-Set up project with Visual Studio Code and TypeScript.
-
 1. Start Visual Studio Code in a new directory.
 
    ```bash
@@ -63,7 +66,7 @@ Set up project with Visual Studio Code and TypeScript.
 
    This creates a `package.json` file with default values.
 
-1. Edit `package.json` to include a build script. Add the following line to the `scripts` section:
+1. Edit `package.json` to include a build script. Add the following line to the `scripts` section.
 
    ```json
    "build": "tsc"
@@ -134,10 +137,12 @@ az login --tenant <PUT YOUR TENANT ID HERE>
 You should now be logged in to Azure from your local device.
 
 
-## Create the vector index 
+## Create a vector index
 
 In this section, you create a vector index in Azure AI Search with [SearchIndexClient](/javascript/api/@azure/search-documents/searchindexclient).[createOrUpdateIndex](/javascript/api/@azure/search-documents/searchindexclient#@azure-search-documents-searchindexclient-createorupdateindex). The index schema defines the fields, including the vector field `DescriptionVector`. Once the index is created, you upload documents to the index. The documents contain the vectorized version of the article's description, which enables similarity search based on meaning rather than exact keywords.
 
+To create the vector index:
+
 1. Create a `createIndex.ts` file in the `src` directory.
 
 1. Copy the following code into the file. 
@@ -146,12 +151,12 @@ In this section, you create a vector index in Azure AI Search with [SearchIndexC
 
     The code file adds the dependencies, environment variables, and JavaScript type for `HotelDocument` to the top of the file. Add the `createIndex` function to create the index. The function defines the index schema, including the vector field `DescriptionVector`.
 
-1. Build and run the file:
+1. Build and run the file.
 
     ```console
     npm run build && node -r dotenv/config dist/createIndex.js
     ```
-1. The output of this code shows that the index is created successfully:
+    The output of this code shows that the index is created successfully.
 
     ```console
     Using Azure Search endpoint: https://my-service.search.windows.net
@@ -160,40 +165,48 @@ In this section, you create a vector index in Azure AI Search with [SearchIndexC
     hotels-vector-quickstart created
     ```
 
-   Key takeaways when creating vector index with the `@azure/search-documents` library:
+   Key takeaways:
+
+   + You define an index by creating a list of fields. 
+
+   + This particular index supports multiple search capabilities, such as:
 
-   - You define an index by creating a list of fields. 
+      + Full-text keyword search (`searchable`)
 
-   - This particular index supports multiple search capabilities, such as:
-      - Full-text keyword search (`searchable`)
-      - Vector search (enables hybrid search by collocating vector and nonvector fields) fields (`DescriptionVector` with `vectorSearchProfileName`)
-      - Semantic search 
-      - Faceted search (`searchSuggester`)
-      - Geo-spatial search (`Location` field with `geo.distance`)
-      - Filtering, sorting (Many fields marked filterable and sortable)
+      + Vector search (enables hybrid search by collocating vector and nonvector fields) fields (`DescriptionVector` with `vectorSearchProfileName`)
+
+      + Semantic search 
+
+      + Faceted search (`searchSuggester`)
+
+      + Geo-spatial search (`Location` field with `geo.distance`)
+
+      + Filtering, sorting (many fields marked filterable and sortable)
 
 
 ## Upload documents to the index
 
-Creating and loading the index are separate steps. You created the index schema in the [previous step](#create-the-vector-index). Now you need to load documents into the index with [SearchClient](/javascript/api/@azure/search-documents/searchclient).[uploadDocuments](/javascript/api/%40azure/search-documents/searchclient#@azure-search-documents-searchclient-uploaddocuments).
+Creating and loading the index are separate steps. You created the index schema in the previous step. You now need to load documents into the index with [SearchClient](/javascript/api/@azure/search-documents/searchclient).[uploadDocuments](/javascript/api/%40azure/search-documents/searchclient#@azure-search-documents-searchclient-uploaddocuments). The documents contain the vectorized version of the article's description, which enables similarity search based on meaning rather than exact keywords.
 
 In Azure AI Search, the index stores all searchable content, while the search engine executes queries against that index.
 
+To upload documents to the index:
+
 1. Create a `uploadDocuments.ts` file in the `src` directory.
 1. Copy the following code into the file.
 
     :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/uploadDocuments.ts" :::
 
-    This code loads a variable documents with a JSON object describing each document, along with the vectorized version of the article's description. This vector enables similarity search, where matching is based on meaning rather than exact keywords.
+    This code loads variable documents with a JSON object describing each document, along with the vectorized version of the article's description. This vector enables similarity search, where matching is based on meaning rather than exact keywords.
 
     Because this quickstart article searches the index immediately, the `waitUntilIndexed` function waits until the index is ready for search operations. This is important because the index needs to be fully populated with documents before you can perform searches.
 
-1. Build and run the file:
+1. Build and run the file.
 
     ```console
     npm run build && node -r dotenv/config dist/uploadDocuments.js
     ```
-1. The output of this code shows that the documents are indexed and ready for search:
+    The output of this code shows that the documents are indexed and ready for search.
 
     ```console
     Uploading documents...
@@ -208,34 +221,39 @@ In Azure AI Search, the index stores all searchable content, while the search en
     All documents indexed successfully.
     ```
 
-    Key takeaways about the upload_documents() method and this example:
-    
-    * Your code interacts with a specific search index hosted in your Azure AI Search service through the SearchClient, which is the main object provided by the @azure/search-documents package. The SearchClient provides access to index operations such as:
-        * Data ingestion - uploadDocuments(), mergeDocuments(), deleteDocuments(), etc.
-        * Search operations - search(), autocomplete(), suggest()
-        * Index management operations such as createIndex(), deleteIndex(), getIndex(), etc.
-    * Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 4096 floating point values each. This quickstart sets the dimensions attribute to 1,536 because that's the size of embeddings generated by the Azure OpenAI text-embedding-ada-002 model.
+    Key takeaways:
+
+    * Your code interacts with a specific search index hosted in your Azure AI Search service through the `SearchClient`, which is the main object provided by the @azure/search-documents package. The `SearchClient` provides access to index operations, such as:
+
+        * Data ingestion: `uploadDocuments`, `mergeDocuments`, `deleteDocuments`, and so on.
+
+        * Search operations: `search`, `autocomplete`, `suggest`
+
+        * Index management operations: `createIndex`, `deleteIndex`, `getIndex`, and so on.
+
+    * Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 4096 floating point values each. This quickstart sets the dimensions attribute to 1,536 because that's the size of embeddings generated by the `text-embedding-ada-002` model.
 
 ## Create the query as a vector
 
 The example vector queries are based on two strings:
 
-- **Search string**: `historic hotel walk to restaurants and shopping`
-- **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
++ Search string: `historic hotel walk to restaurants and shopping`
++ Vector query string: `quintessential lodging near running trails, eateries, retail` (vectorized into a mathematical representation)
 
 The vector query string is semantically similar to the search string, but it includes terms that don't exist in the search index. If you do a keyword search for `quintessential lodging near running trails, eateries, retail`, results are zero. We use this example to show how you can get relevant results even if there are no matching terms.
 
-1. Create a `queryVector.ts` file in the `src` directory and add the code to create the query vector.
-
-    :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/queryVector.ts" :::
+Create a `queryVector.ts` file in the `src` directory and add the code to create the query vector.
 
-1. This code is used in the following sections to perform vector searches. The query vector is created using an embedding model from Azure OpenAI.
+:::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/queryVector.ts" :::
 
+This code is used in the following sections to perform vector searches. The query vector is created using an embedding model from Azure OpenAI.
 
 ## Create a single vector search
 
 The first example demonstrates a basic scenario where you want to find document descriptions that closely match the search string using the [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions).
 
+To create a single vector search:
+
 1. Create a `searchSingle.ts` file in the `src` directory.
 
 1. Copy the following code into the file.
@@ -246,13 +264,13 @@ The first example demonstrates a basic scenario where you want to find document
 
     The vector query string is `quintessential lodging near running trails, eateries, retail`, which is vectorized into 1,536 embeddings for this query.
 
-1. Build and run the file:
+1. Build and run the file.
 
     ```console
     npm run build && node -r dotenv/config dist/searchSingle.js
     ```
 
-1. The output of this code shows the relevant docs for the query `quintessential lodging near running trails, eateries, retail`. 
+    The output of this code shows the relevant docs for the query `quintessential lodging near running trails, eateries, retail`. 
 
     ```console
     Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
@@ -269,11 +287,12 @@ The first example demonstrates a basic scenario where you want to find document
 
     The response for the vector equivalent of `quintessential lodging near running trails, eateries, retail` consists of 5 results with only the fields specified by the select returned.
 
-
 ## Create a single vector search with a filter
 
 You can add filters, but the filters are applied to the nonvector content in your index. In this example, the filter applies to the `Tags` field to filter out any hotels that don't provide free Wi-Fi. This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
 
+To create a single vector search with a filter:
+
 1. Create a `searchSingleWithFilter.ts` file in the `src` directory.
 
 1. Copy the following code into the file.
@@ -282,12 +301,13 @@ You can add filters, but the filters are applied to the nonvector content in you
 
     Add the dependencies, environment variables, and the same search functionality as the previous search with a post-processing exclusion filter added for hotels with `free wifi`.
 
-1. Build and run the file:
+1. Build and run the file.
 
     ```console
     npm run build && node -r dotenv/config dist/searchSingleWithFilter.js
     ```
-1. The output of this code shows the relevant documents for the query with the filter for `free wifi` applied:
+
+    The output of this code shows the relevant documents for the query with the filter for `free wifi` applied:
 
     ```console
     Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
@@ -303,18 +323,21 @@ You can add filters, but the filters are applied to the nonvector content in you
 
 You can specify a geospatial filter to limit results to a specific geographic area. In this example, the filter limits results to hotels within 300 kilometers of Washington D.C. (coordinates: `-77.03241 38.90166`). Geospatial distances are always in kilometers. This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
 
+To create a search with a geospatial filter:
+
 1. Create a `searchSingleWithFilterGeo.ts` file in the `src` directory.
 
 1. Copy the following code into the file.
 
     :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/searchSingleWithFilterGeo.ts" :::
-1. Build and run the file:
+
+1. Build and run the file.
 
     ```console
     npm run build && node -r dotenv/config dist/searchSingleWithFilterGeo.js
     ```
 
-1. The output of this code shows the relevant documents for the query with the geospatial post-processing exclusion filter applied:
+    The output of this code shows the relevant documents for the query with the geospatial post-processing exclusion filter applied.
 
     ```console
     Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
@@ -326,26 +349,30 @@ You can specify a geospatial filter to limit results to a specific geographic ar
     - HotelId: 49, HotelName: Swirling Currents Hotel, Tags: N/A, Score 0.602634072303772
     ```
 
-
 ## Create a hybrid search
 
 Hybrid search consists of keyword queries and vector queries in a single search request. This example runs the vector query and full-text search concurrently:
 
-- **Search string**: `historic hotel walk to restaurants and shopping`
-- **Vector query string** (vectorized into a mathematical representation): `quintessential lodging near running trails, eateries, retail`
++ Search string: `historic hotel walk to restaurants and shopping`
++ Vector query string: `quintessential lodging near running trails, eateries, retail` (vectorized into a mathematical representation)
 
 This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
 
+To create a hybrid search:
+
 1. Create a `searchHybrid.ts` file in the `src` directory.
+
 1. Copy the following code into the file.
 
     :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/searchHybrid.ts" :::
-1. Build and run the file:
+
+1. Build and run the file.
 
     ```console
     npm run build && node -r dotenv/config dist/searchHybrid.js
     ```
-1. The output of this code shows the relevant documents for the hybrid search:
+
+    The output of this code shows the relevant documents for the hybrid search:
 
     ```console
     Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
@@ -389,7 +416,7 @@ This search uses [SearchClient](/javascript/api/@azure/search-documents/searchcl
       Tags: ["pool","free wifi","air conditioning","concierge"]
     ```
 
-    Because Reciprocal Rank Fusion (RRF) merges results, it helps to review the inputs. The following results are from only the full-text query. The top two results are Sublime Palace Hotel and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
+    Because Reciprocal Rank Fusion (RRF) merges results, it helps to review the inputs. The following results are from the full-text query only. The top two results are Sublime Palace Hotel and Luxury Lion Resort. The Sublime Palace Hotel has a stronger BM25 relevance score.
 
     ```json
        {
@@ -404,7 +431,7 @@ This search uses [SearchClient](/javascript/api/@azure/search-documents/searchcl
        },
     ```
 
-    In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to fourth position. Luxury Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
+    In the vector-only query, which uses HNSW for finding matches, the Sublime Palace Hotel drops to the fourth position. Luxury Lion, which was second in the full-text search and third in the vector search, doesn't experience the same range of fluctuation, so it appears as a top match in a homogenized result set.
    
    ```json
    "value": [
@@ -466,18 +493,21 @@ Here's the last query in the collection to extend the semantic hybrid search wit
 
 This search uses [SearchClient](/javascript/api/@azure/search-documents/searchclient).[search](/javascript/api/@azure/search-documents/searchclient#@azure-search-documents-searchclient-search) and the [VectorQuery](/javascript/api/@azure/search-documents/vectorquery) and [SearchOptions](/javascript/api/@azure/search-documents/searchoptions). 
 
+To create a semantic hybrid search:
+
 1. Create a `searchSemanticHybrid.ts` file in the `src` directory.
+
 1. Copy the following code into the file.
 
     :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/searchSemanticHybrid.ts" :::
 
-1. Build and run the file:
+1. Build and run the file.
 
     ```console
     npm run build && node -r dotenv/config dist/searchSemanticHybrid.js
     ```
 
-1. The output of this code shows the relevant documents for the semantic hybrid search:
+    The output of this code shows the relevant documents for the semantic hybrid search.
 
     ```console
     Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
@@ -531,24 +561,26 @@ This search uses [SearchClient](/javascript/api/@azure/search-documents/searchcl
 
     - Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
 
-## Clean up
+## Clean up resources
 
 When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
 
 You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
 
-If you want to keep your search service but delete the index and its documents, you can delete the index programmatically.
+Alternatively, to delete the vector index you created in this quickstart programmatically:
 
 1. Create a `deleteIndex.ts` file in the `src` directory.
+
 1. Add the dependencies, environment variables, and code to delete the index.
 
     :::code language="typescript" source="~/azure-search-javascript-samples/quickstart-vector-ts/src/deleteIndex.ts" :::
-1. Build and run the file:
+
+1. Build and run the file.
 
     ```console
     npm run build && node -r dotenv/config dist/deleteIndex.js
     ```
 
 ## Next steps
 
-- Review the repository of code samples for vector search capabilities in Azure AI Search for [JavaScript](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript)
\ No newline at end of file
++ Review the repository of code samples for vector search capabilities in Azure AI Search for [JavaScript](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptを使用したベクトル検索のクイックスタートドキュメントの更新"
}
```

### Explanation
この変更は、`search-get-started-vector-typescript.md` ファイルの更新を示しており、TypeScriptを使用してAzure AI Searchでベクトルを作成、読み込み、クエリする手順が最新化されています。主な変更点は、文書の日付が「11/20/2025」から「01/14/2026」に変更されたことと、新たに `ms.custom` と `ai-usage` のメタデータが追加されたことです。

クイックスタートの内容は、TypeScriptを使用してベクトルインデックスを作成するプロセスに重点を置いており、特にインデックススキーマの定義やドキュメントのアップロード方法に関する具体的な指示が含まれています。各手順の説明が詳細に記述されており、ユーザーが簡単に設定を行えるようになっています。

特に、新しいファイルの作成、依存関係の追加、および環境変数の設定に関する手順が整理されており、Visual Studio Codeを使ったプロジェクトの構築が明確に説明されています。さまざまな検索例（単一のベクトル検索、フィルタ付き検索、ハイブリッド検索など）が含まれており、各検索シナリオでの具体的なコード例と結果が示されています。

さらに、クイックスタート記事では、Microsoft Entraを使用したキーのない認証の推奨方法が取り入れられており、セキュリティと利便性が向上しています。

全体的に、このドキュメントの更新により、Azure AI SearchのTypeScriptにおけるベクトル検索の実装が容易に理解できるようになっています。これにより、開発者はより効果的に検索機能を実装し、有用なデータを効率的に取得する方法を学べます。

## articles/search/includes/quickstarts/semantic-ranker-java.md{#item-93a05a}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,7 @@ The quickstart assumes the following is available on your computer:
 
 1. Create a `pom.xml` file with required dependencies.
 
-   :::code language="xml" source="~/azure-search-java-samples/semantic-ranking-quickstart/pom.xml" :::
+   :::code language="xml" source="~/azure-search-java-samples/quickstart-semantic-ranking/pom.xml" :::
 
 1. Compile the project to resolve the dependencies.
 
@@ -61,15 +61,15 @@ If you signed in to the [Azure portal](https://portal.azure.com), you're signed
 
 Create a `SearchConfig.java` file in the `src/main/java/com/azure/search/quickstart` directory to read the properties file and hold the configuration values and authentication credential.
 
-:::code language="java" source="~/azure-search-java-samples/semantic-ranking-quickstart/src/main/java/com/azure/search/quickstart/SearchConfig.java" :::
+:::code language="java" source="~/azure-search-java-samples/quickstart-semantic-ranking/src/main/java/com/azure/search/quickstart/SearchConfig.java" :::
 
 ## Get the index schema
 
 In this section, you get settings for the existing `hotels-sample-index` index on your search service.
 
 1. Create a `GetIndexSettings.java` file in the `src/main/java/com/azure/search/quickstart` directory.
 
-   :::code language="java" source="~/azure-search-java-samples/semantic-ranking-quickstart/src/main/java/com/azure/search/quickstart/GetIndexSettings.java" :::
+   :::code language="java" source="~/azure-search-java-samples/quickstart-semantic-ranking/src/main/java/com/azure/search/quickstart/GetIndexSettings.java" :::
 
 1. Compile and run the code.
 
@@ -83,7 +83,7 @@ In this section, you get settings for the existing `hotels-sample-index` index o
 
 1. Create an `UpdateIndexSettings.java` file in the `src/main/java/com/azure/search/quickstart` directory to add a semantic configuration to the existing `hotels-sample-index` index on your search service.
 
-   :::code language="java" source="~/azure-search-java-samples/semantic-ranking-quickstart/src/main/java/com/azure/search/quickstart/UpdateIndexSettings.java" :::
+   :::code language="java" source="~/azure-search-java-samples/quickstart-semantic-ranking/src/main/java/com/azure/search/quickstart/UpdateIndexSettings.java" :::
 
 1. Compile and run the code.
 
@@ -99,7 +99,7 @@ After the `hotels-sample-index` index has a semantic configuration, you can run
 
 1. Create a `SemanticQuery.java` file in the `src/main/java/com/azure/search/quickstart` directory to create a semantic query of the index.
 
-   :::code language="java" source="~/azure-search-java-samples/semantic-ranking-quickstart/src/main/java/com/azure/search/quickstart/SemanticQuery.java" :::
+   :::code language="java" source="~/azure-search-java-samples/quickstart-semantic-ranking/src/main/java/com/azure/search/quickstart/SemanticQuery.java" :::
 
 1. Compile and run the code.
 
@@ -115,7 +115,7 @@ Optionally, you can add captions to extract portions of the text and apply hit h
 
 1. Create a `SemanticQueryWithCaptions.java` file in the `src/main/java/com/azure/search/quickstart` directory.
 
-   :::code language="java" source="~/azure-search-java-samples/semantic-ranking-quickstart/src/main/java/com/azure/search/quickstart/SemanticQueryWithCaptions.java" :::
+   :::code language="java" source="~/azure-search-java-samples/quickstart-semantic-ranking/src/main/java/com/azure/search/quickstart/SemanticQueryWithCaptions.java" :::
 
 1. Compile and run the code.
 
@@ -144,7 +144,7 @@ To produce a semantic answer, the question and answer must be closely aligned, a
 
 1. Create a `SemanticAnswer.java` file in the `src/main/java/com/azure/search/quickstart` directory.
 
-   :::code language="java" source="~/azure-search-java-samples/semantic-ranking-quickstart/src/main/java/com/azure/search/quickstart/SemanticAnswer.java" :::
+   :::code language="java" source="~/azure-search-java-samples/quickstart-semantic-ranking/src/main/java/com/azure/search/quickstart/SemanticAnswer.java" :::
 
 1. Compile and run the code.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaを使用したセマンティックランキングのクイックスタートドキュメントの更新"
}
```

### Explanation
この変更は、`semantic-ranker-java.md` ファイルの更新を示しており、Azure AI SearchにおけるセマンティックランキングをJavaで実装するための手順が最新化されています。具体的には、サンプルコードのパスが新しいディレクトリ構成に合わせて修正されました。この修正により、各サンプルファイルが適切な場所から参照されるようになり、ユーザーが必要な依存関係やコードを簡単に見つけられるようになります。

過去の文書と比較して、`pom.xml`、`SearchConfig.java`、`GetIndexSettings.java`、`UpdateIndexSettings.java`、`SemanticQuery.java`、`SemanticQueryWithCaptions.java`、`SemanticAnswer.java` の各ファイルパスが新たに指定されたディレクトリへと変更されており、ファイルの構成が整理されています。

これにより、ユーザーはコードの読み込みや実行をよりスムーズに行えるようになり、クイックスタートガイドの全体的な明瞭さと使いやすさが向上しました。また、このドキュメントはセマンティックランキングに関連するコードのサンプルを通じて、ユーザーがAzure AI Searchの機能を効果的に試験する手助けをしています。

この更新は、特に新規の開発者にとって、セマンティックランキングを利用した検索機能を理解し、実装する際の重要なリソースとなるでしょう。

## articles/search/search-get-started-agentic-retrieval.md{#item-4a40f4}

<details>
<summary>Diff</summary>
````diff
@@ -6,9 +6,11 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 10/21/2025
+ms.date: 01/14/2026
+ms.custom: dev-focus
+ai-usage: ai-assisted
 zone_pivot_groups: search-get-started-agentic-retrieval
-# Customer intent: I want to learn how to use agentic retrieval to create a knowledge base that processes multi-turn conversations. The knowledge base should retrieve relevant information from a knowledge source that points to an Azure AI Search index and use an Azure OpenAI chat completion model to synthesize answers.
+# Customer intent: I want to learn how to use agentic retrieval to create a knowledge base that processes multi-turn conversations. The knowledge base should retrieve relevant information from a knowledge source that points to an Azure AI Search index and use an Azure OpenAI LLM to synthesize answers.
 ---
 
 # Quickstart: Use agentic retrieval in Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルのクイックスタートドキュメントの更新"
}
```

### Explanation
この変更は、`search-get-started-agentic-retrieval.md` ファイルの更新を示しており、Azure AI Searchを利用したエージェントリトリーバルのクイックスタートガイドに関する内容が最新化されています。主な修正内容は、ドキュメントの日付が「10/21/2025」から「01/14/2026」に変更されたことに加え、`ms.custom` と `ai-usage` のメタデータが新しく追加されています。

さらに、ドキュメント内の顧客の意図に関する記述も修正されており、"Azure OpenAI chat completion model" から "Azure OpenAI LLM" に変更されています。この変更は、エージェントリトリーバルの知識ベースが情報を取得するために使用するAIモデルの表現をより一般的にし、可読性と理解のしやすさを向上させています。

全体として、この更新により、クイックスタートガイドが最新の情報を反映し、読者がAzure AI Searchにおけるエージェントリトリーバルの利用方法を迅速に理解できるようになっています。これにより、開発者はマルチターンの会話を処理する知識ベースの構築が容易になると期待されます。

## articles/search/search-get-started-vector.md{#item-4984d9}

<details>
<summary>Diff</summary>
````diff
@@ -7,8 +7,10 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
+  - dev-focus
 ms.topic: quickstart
-ms.date: 11/20/2025
+ms.date: 01/14/2026
+ai-usage: ai-assisted
 zone_pivot_groups: search-get-started-vector-search
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクター検索のクイックスタートドキュメントの更新"
}
```

### Explanation
この変更は、`search-get-started-vector.md` ファイルの更新を示しており、Azure AI Searchにおけるベクター検索に関するクイックスタートガイドが最新化されています。主な修正内容には、ドキュメントの日付が「11/20/2025」から「01/14/2026」に変更されたこと、そして新たに `dev-focus` と `ai-usage` のメタデータが追加されたことが含まれています。

これにより、ドキュメントが現行の開発者向けの焦点を明確に反映することとなり、AIの使用に関する指針が示されるようになっています。さらに、こうした変更は、ベクター検索機能を活用する開発者に対して、最新のテクノロジー及びその利活用に関する必要な情報を提供することを目的としています。

以上の更新内容により、読者はAzure AI Searchを使用してベクター検索を実施するための手順を、より効果的に学ぶことができ、よりスムーズに実装を行うことが期待されます。このように、ドキュメントの明瞭さと情報の新しさが向上することで、ユーザーエクスペリエンスが改善されています。

## articles/search/search-how-to-delete-documents.md{#item-556879}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,308 @@
+---
+title: Delete Documents
+titleSuffix: Azure AI Search
+description: Learn how to delete documents in a search index using the REST APIs or an Azure SDK.
+manager: nitinme
+author: HeidiSteen
+ms.author: heidist
+ms.service: azure-ai-search
+ms.update-cycle: 180-days
+ms.topic: how-to
+ms.date: 01/15/2026
+---
+
+# Delete documents in a search index
+
+This article explains how to delete whole documents from a search index on Azure AI Search. 
+
+It covers these tasks:
+
++ Understand when manual deletion is required
++ Identify specific documents to delete
++ Get document counts and storage metrics
++ Delete a single or orphaned document
++ Delete documents in bulk
++ Confirm deletion
+
+You can use the REST APIs or an Azure SDK client library to delete documents. There's currently no support for document deletion in the Azure portal.
+
+For more information about deleting or updating a *specific field* within a document, see [Update or rebuild an index](search-howto-reindex.md).
+
+## Prerequisites
+
++ To delete documents, you must have 
+`Microsoft.Search/searchServices/indexes/documents/delete` or **Search Index Data Contributor** permissions.
+
+## Understand when manual deletion is required
+
+Manual document deletion is necessary when you use the [push mode approach to indexing](search-what-is-data-import.md#pushing-data-to-an-index), where application code handles data import and drives indexing.
+
+You also need manual document deletion if you use [Logic Apps to load an index (preview)](search-how-to-index-logic-apps.md#limitations).
+
+You might also need manual document deletion in indexer-driven workloads if search documents become "orphaned" from source documents. An important benefit of indexers is automated content retrieval and synchronization via the change and deletion detection features of the target data source. All of the supported data sources provide some level of detection. But in some cases, synchronized deletion is predicated on a soft-delete strategy where you flag a source document (or record) for deletion, run the indexer to delete the indexed content, and only after the index is updated do you physically delete the source content. If source content is deleted first, you have *orphan documents* in the search index. You must manually delete orphan documents in your index to re-establish parity between source and indexed content.
+
+The following links provide more information about change and deletion detection for each data source in indexer-driven workloads.
+
++ [Azure Storage](search-how-to-index-azure-blob-changed-deleted.md)
++ [Azure SQL](search-how-to-index-sql-database.md#indexing-new-changed-and-deleted-rows)
++ [Azure Cosmos DB](search-how-to-index-cosmosdb-sql.md#indexing-deleted-documents)
++ [Azure Database for MySQL (preview)](search-how-to-index-mysql.md#indexing-deleted-rows)
++ [SharePoint indexer](search-how-to-index-sharepoint-online.md)
++ [OneLake indexer](search-how-to-index-onelake-files.md#supported-tasks)
+
+## Identify specific documents for deletion
+
+All documents are uniquely identified by a [document key](search-how-to-create-search-index.md#document-keys) in a search index. To delete a document, you must identify which field is the document key and provide the key on the deletion request.
+
+In the Azure portal, you can view the fields of each index. Document keys are string fields and are denoted with a key icon to make them easier to spot.
+
+### Find the document key
+
+Once you know which field is the document key, you can get the key value by running a query that returns the key field in the search results.
+
+In this example, the search string is used to find the document in the index, and the select statement determines what fields are in the results. The "HotelId" is the document key in this example. 
+
+```http
+POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+{
+    "search": "this query has terms that pertain to the document I want to delete",
+    "select": "HotelName, HotelId",
+    "count": true
+}
+```
+
+Results for this keyword search are the top 50 by default. If the document you want to delete satisfies the search criteria, you should see it (and it's key) in the results. Make sure the query includes a descriptive field that helps you confirm you have the correct document.
+
+```json
+{
+  "@odata.count": 50,
+  "value": [
+    {
+      "@search.score": 4.5116634,
+      "HotelId": "18",
+      "HotelName": "Ocean Water Resort & Spa"
+    }
+   ...
+  ]
+}
+```
+
+A simple string is straightforward, but if the index uses a base-64 encoded field, or if search documents were generated from a `parsingMode` setting, you might be working with values that you aren't familiar with. If you're working with chunked documents create by an indexer, the document key is often a generated "chunked_id" composed of a long sequence of numbers and letters.
+
+## Look up a specific document
+
+Now that you have the document key, run a [look up query](/rest/api/searchservice/documents/get) that retrieves the entire document. If the document is a chunk, you should see the ID of the parent document. The document key is included as a query parameter.
+
+The first example returns the hotel having a document key value of `18`.
+
+```http
+GET https://[service name].search.windows.net/indexes/hotels-sample-index/docs('18')&api-version=2025-09-01
+```
+
+The second example returns a chunk document. The "chunk_id" is the document key.
+
+```http
+GET https://[service name].search.windows.net/indexes/chunking-example-index/docs('aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb')&api-version=2025-09-01
+```
+
+The response from the second example includes all fields, which you should review to ensure you know what you're deleting. Fields that include parent information are useful if you need to manually reindex a single parent document into constituent chunked documents in the search index.
+
+```json
+{
+  "chunk_id": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
+  "parent_id": "bbbbbbbb-1111-2222-3333-cccccccccccc",
+  "chunk": "Unpopulated Slopes of an Active Volcano\u2014Naples, Italy ... 90\n\nDazzling Coastlines\u2014Italy ... .92\n\nLiving on Fertile Land\u2014Nile River, Egypt  ... 94\n\n\n\n vii",
+  "title": "earth_at_night_508.pdf",
+  "text_vector": [ <omitted> ]
+}
+```
+
+> [!TIP]
+> Use a [REST client](search-get-started-text.md?tabs=keyless%2Cwindows&pivots=rest#query-the-index), an Azure SDK client library, or a [command line tool](search-get-started-text.md?tabs=keyless%2Cwindows&pivots=powershell#query-the-index) to run a lookup query. The Azure portal doesn't support GET requests for a query.
+
+## Get document counts and storage metrics
+
+Before you delete documents, get initial metrics for the index document count and storage so that you can confirm deletion later.
+
+You can get document counts and index storage using:
+
++ The Azure portal, under **Search management** > **Indexes**.
++ The [Indexes - Get Statistics](/rest/api/searchservice/indexes/get-statistics) REST API
+
+Here's an example response:
+
+```json
+{
+  "documentCount": 12,
+  "storageSize": 123456,
+  "vectorIndexSize": 123456
+}
+```
+
+## Delete a single document
+
+### [**REST**](#tab/rest)
+
+1. Use the [Documents - Index](/rest/api/searchservice/documents) REST API with a delete `@search.action` to remove it from the search index. Formulate a POST call specifying the index name and the `docs/index` endpoint. Make sure the body of the request includes the key of the document you want to delete.
+
+    ```http
+    POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/index?api-version=2025-09-01
+    Content-Type: application/json   
+    api-key: [admin key]
+    
+    {  
+      "value": [  
+        {  
+          "@search.action": "delete",  
+          "id": "18"  
+        }  
+      ]  
+    }
+    ```
+
+1. Send the request.
+
+   The following table explains the various per-document [status codes](/rest/api/searchservice/http-status-codes) that can be returned in the response. Some status codes indicate problems with the request itself, while others indicate temporary error conditions. The latter you should retry after a delay.
+
+   |Status code|Meaning|Retryable|Notes|
+   |-----------|-------|---------|-----| 
+   |200|Document was successfully deleted.|n/a|Delete operations are [idempotent](https://en.wikipedia.org/wiki/Idempotence). That is, even if a document key doesn't exist in the index, attempting a delete operation with that key results in a 200 status code.|
+   |400|There was an error in the document that prevented it from being deleted.|No|The error message in the response provides details.|
+   |422|The index is temporarily unavailable because it was updated with the 'allowIndexDowntime' flag set to 'true'.|Yes|
+   |503|Your search service is temporarily unavailable, possibly due to heavy load.|Yes|Your code should wait before retrying in this case or you risk prolonging the service unavailability.|
+
+   > [!NOTE]  
+   > If your client code frequently encounters a 207 response, one possible reason is that the system is under load. You can confirm this by checking the `statusCode` property for 503. If so, we recommend throttling indexing requests. Otherwise, if indexing traffic doesn't subside, the system could start rejecting all requests with 503 errors.  
+
+1. You can resend the [Lookup query](/rest/api/searchservice/documents/get) to confirm the deletion. You should get a 404 document not found message. 
+
+    ```http
+    GET https://[service name].search.windows.net/indexes/hotel-sample-index/docs/18?api-version=2025-09-01
+    ```
+
+### [**.NET**](#tab/sdk-dotnet)
+
+The Azure SDK for .NET provides the following APIs for simple and bulk document uploads into an index:
+
++ [IndexDocumentsAsync](/dotnet/api/azure.search.documents.searchclient.indexdocumentsasync)
++ [SearchIndexingBufferedSender](/dotnet/api/azure.search.documents.searchindexingbufferedsender-1)
+
+### [**Python**](#tab/sdk-python)
+
+The Azure SDK for Python provides the following APIs for simple and bulk document uploads into an index:
+
++ [IndexDocumentsBatch](/python/api/azure-search-documents/azure.search.documents.indexdocumentsbatch)
++ [SearchIndexingBufferedSender](/python/api/azure-search-documents/azure.search.documents.searchindexingbufferedsender)
+
+Code sample:
+
++ [sample_crud_operations.py](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/samples/sample_crud_operations.py)
+
+### [**JavaScript**](#tab/sdk-javascript)
+
+The Azure SDK for JavaScript/TypeScript provides the following APIs for simple and bulk document uploads into an index:
+
++ [IndexDocumentsBath](/javascript/api/%40azure/search-documents/indexdocumentsbatch)
++ [SearchIndexingBufferedSender](/javascript/api/%40azure/search-documents/searchindexingbufferedsender)
+
+### [**Java**](#tab/sdk-java)
+
+The Azure SDK for Java provides the following APIs for simple and bulk document uploads into an index:
+
++ [indexactiontype enumerator](/java/api/com.azure.search.documents.models.indexactiontype)
++ [SearchIndexingBufferedSender](/java/api/com.azure.search.documents.searchclientbuilder.searchindexingbufferedsenderbuilder)
+
+Code sample:
+
++ [IndexContentManagementExample.java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/IndexContentManagementExample.java)
+
+---
+
+## Delete documents in bulk
+
+### [**REST**](#tab/rest)
+
+1. Use the [Documents - Index](/rest/api/searchservice/documents) REST API with a delete `@search.action` to remove it from the search index. Formulate a POST call specifying the index name and the `docs/index` endpoint. Make sure the body of the request includes the keys of all of the documents you want to delete.
+
+    ```http
+    POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/index?api-version=2025-09-01
+    Content-Type: application/json   
+    api-key: [admin key]
+    
+    {
+      "value": [
+        {
+          "@search.action": "delete",
+          "id": "doc1"
+        },
+        {
+          "@search.action": "delete",
+          "id": "doc2"
+        }
+      ]
+    }
+    ```
+
++ **Batch limits**: It is recommended to limit batches to 1,000 documents or roughly 16 MB per request to ensure optimal performance.
+
++ **Idempotency**: Deletion is idempotent; if you attempt to delete a document ID that does not exist, the API will still return a 200 OK status.
+
++ **Latency**: Documents are not always removed instantly from storage. A background process performs the physical deletion every few minutes.
+
++ **Vector storage**: Deleting documents does not immediately free up vector storage quotas. It takes several minutes for physical deletion. For immediate reclamation of vector space, you may need to drop and rebuild the index.
+
+### [**.NET**](#tab/sdk-dotnet)
+
+The Azure SDK for .NET provides the following APIs for simple and bulk document uploads into an index:
+
++ [IndexDocumentsAsync](/dotnet/api/azure.search.documents.searchclient.indexdocumentsasync)
++ [SearchIndexingBufferedSender](/dotnet/api/azure.search.documents.searchindexingbufferedsender-1)
+
+### [**Python**](#tab/sdk-python)
+
+The Azure SDK for Python provides the following APIs for simple and bulk document uploads into an index:
+
++ [IndexDocumentsBatch](/python/api/azure-search-documents/azure.search.documents.indexdocumentsbatch)
++ [SearchIndexingBufferedSender](/python/api/azure-search-documents/azure.search.documents.searchindexingbufferedsender)
+
+Code sample:
+
++ [sample_crud_operations.py](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/samples/sample_crud_operations.py)
+
+### [**JavaScript**](#tab/sdk-javascript)
+
+The Azure SDK for JavaScript/TypeScript provides the following APIs for simple and bulk document uploads into an index:
+
++ [IndexDocumentsBath](/javascript/api/%40azure/search-documents/indexdocumentsbatch)
++ [SearchIndexingBufferedSender](/javascript/api/%40azure/search-documents/searchindexingbufferedsender)
+
+### [**Java**](#tab/sdk-java)
+
+The Azure SDK for Java provides the following APIs for simple and bulk document uploads into an index:
+
++ [indexactiontype enumerator](/java/api/com.azure.search.documents.models.indexactiontype)
++ [SearchIndexingBufferedSender](/java/api/com.azure.search.documents.searchclientbuilder.searchindexingbufferedsenderbuilder)
+
+Code sample:
+
++ [IndexContentManagementExample.java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/IndexContentManagementExample.java)
+
+---
+
+## Confirm document deletion
+
+You can find metrics about document counts and index storage using:
+
++ The Azure portal, under **Search management** > **Indexes**.
++ The [Indexes - Get Statistics](/rest/api/searchservice/indexes/get-statistics) REST API
+
+Get Statistics is the mechanism for retrieving index metrics. The portal calls Get Statistics to populate the index metrics in the portal pages.
+
+Deleting a document doesn't immediately free up space in the index. Every few minutes, a background process performs the physical deletion. Whether you use the Azure portal or the Get Statistics API to return index statistics, you can expect a small delay before the deletion is reflected in the Azure portal and API metrics.
+
+## See also
+
++ [Search indexes overview](search-what-is-an-index.md)
++ [Data import overview](search-what-is-data-import.md)
++ [Import data wizard overview](search-import-data-portal.md)
++ [Indexers overview](search-indexer-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ドキュメント削除に関する新しいガイドの追加"
}
```

### Explanation
この変更は、`search-how-to-delete-documents.md` という新しいファイルが追加されたことを示しており、Azure AI Searchでのドキュメントの削除方法に関する詳細な手順を提供しています。このガイドは、REST APIやAzure SDKを使用して、検索インデックスからドキュメントを削除する方法を学ぶことができます。ファイルは308行にわたる内容で構成されており、以下の主要なポイントがカバーされています。

1. **手作業による削除の必要性** - いつ手動でドキュメントを削除する必要があるかを理解することを説明し、アプリケーションコードがデータインポートを処理するプッシュモードのアプローチを使用している場合や、ロジックアプリを使用してインデックスをロードしている場合などのシナリオについて述べています。

2. **特定のドキュメントの特定** - ドキュメントは一意に識別される「ドキュメントキー」によって特定されることを解説し、その取得方法や、行うべきリクエスト形式を示しています。

3. **ドキュメント削除のメトリクス取得** - 削除を行う前に、インデックス内のドキュメント数やストレージのメトリクスを取得する方法を説明しています。

4. **単一およびバルクでの削除** - ドキュメントを単体または一括で削除するための具体的な手順を、REST APIの使用方法を含めて示しています。

5. **削除の確認** - 削除後にドキュメントが本当に削除されたかを確認する方法を提供し、AzureポータルやAPIを通じてインデックスのメトリクスを取得する手法を紹介しています。

これにより、Azure AI Searchにおいてドキュメントを効果的に管理できる能力が向上し、ユーザーは新しい機能の使用法について幅広く学ぶことができるようになります。この新しいガイドによって、開発者とユーザーにとって、 Azure AI Searchの利活用がさらに進むことが期待されます。

## articles/search/search-how-to-index-azure-blob-one-to-many.md{#item-30a1f9}

<details>
<summary>Diff</summary>
````diff
@@ -9,15 +9,15 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 05/19/2025
+ms.date: 01/14/2026
 ms.update-cycle: 365-days
 ---
 
 # Indexing blobs and files to produce multiple search documents
 
 **Applies to**: [Blob indexers](search-how-to-index-azure-blob-storage.md), [File indexers](search-file-storage-integration.md)
 
-By default, an indexer treats the contents of a blob or file as a single search document. If you want a more granular representation in a search index, you can set **parsingMode** values to create multiple search documents from one blob or file. The **parsingMode** values that result in many search documents include `delimitedText` (for [CSV](search-how-to-index-azure-blob-csv.md)), and `jsonArray` or `jsonLines` (for [JSON](search-how-to-index-azure-blob-json.md)).
+By default, an indexer treats the contents of a blob or file as a single search document. If you want a more granular representation in a search index, you can set **parsingMode** values to create multiple search documents from one blob or file. The **parsingMode** values that result in many search documents include `delimitedText` (for [CSV](search-how-to-index-azure-blob-csv.md)), `jsonArray` or `jsonLines` (for [JSON](search-how-to-index-azure-blob-json.md)), or `markdown` with sub-mode `oneToMany` for [markdown](search-how-to-index-azure-blob-markdown.md).
 
 When you use any of these parsing modes, the new search documents that emerge must have unique document keys, and a problem arises in determining where that value comes from. The parent blob has at least one unique value in the form of `metadata_storage_path property`, but if it contributes that value to more than one search document, the key is no longer unique in the index.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Blob インデックスの多対多マッピングに関するドキュメントの更新"
}
```

### Explanation
この変更は、`search-how-to-index-azure-blob-one-to-many.md` ファイルの更新を示しており、Azure Blobやファイルをインデックス化する方法と、それによって生成される検索ドキュメントに関する情報が改善されています。主な内容の変更は以下の通りです。

- ドキュメントの日付が「05/19/2025」から「01/14/2026」に変更され、最新の情報を反映しています。
- **parsingMode** に関する説明が拡充され、1つのBlobまたはファイルから複数の検索ドキュメントを作成するための新しいオプションとして、「markdown」とそのサブモード「oneToMany」が追加されました。これにより、Markdown形式のデータも複数の検索ドキュメントに変換することが可能となることが示されています。

この変更により、ユーザーはAzure Blobインデックスに関して、より詳細で多様なドキュメント作成の方法を学ぶことができ、特にマークダウン形式のデータを扱う際の柔軟性が向上しました。また、インデックスのドキュメントキーが一意である必要がある問題に対する理解も深まるため、ユーザーは適切な方法でドキュメントを管理できるようになります。このような更新は、Azure AI Searchの利便性向上に寄与します。

## articles/search/search-how-to-index-logic-apps.md{#item-e25907}

<details>
<summary>Diff</summary>
````diff
@@ -127,7 +127,7 @@ It also supports the following query actions:
 
 + The search index is generated using a fixed schema (document ID, content, and vectorized content), with text extraction only. You can [modify the index](#modify-existing-objects) as long as the update doesn't affect existing fields.
 + Vectorization supports text embedding only.
-+ Deletion detection isn't supported. You must manually [delete orphaned documents](search-howto-reindex.md#delete-orphan-documents) from the index.
++ Deletion detection isn't supported. You must manually [delete orphaned documents](search-how-to-delete-documents.md#delete-a-single-document) from the index.
 + Duplicate documents in the search index are a known issue in this preview. Consider deleting objects and starting over if this becomes an issue.
 + No support for private endpoints in the logic app workflow created by the portal wizard. The workflow is hosted using the [**Consumption** hosting option](/azure/logic-apps/single-tenant-overview-compare) and is subject to its constraints. To use the **Standard** hosting option, use a programmatic approach to creating the workflow.
 + All actions are generally available except for 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Logic Apps インデックスに関するドキュメントの更新"
}
```

### Explanation
この変更は、`search-how-to-index-logic-apps.md` ファイルの更新を示しており、Logic Appsに関連するインデックス作成手順に関する情報が若干修正されました。主な内容の変更は以下の通りです。

- **削除されたドキュメント**に関する注意点が更新されました。具体的には、元々のリンクが「search-howto-reindex.md#delete-orphan-documents」から、「search-how-to-delete-documents.md#delete-a-single-document」に変更されました。これにより、オーファンドキュメント（孤立したドキュメント）を削除するための手順が、別のドキュメント参照に切り替わっています。

- 他の部分では、検索インデックスの生成方法（固定スキーマ、コンテンツの抽出）、ベクトル化のサポート（テキスト埋め込みのみ）、および重複ドキュメントに関する注意点が残されたままとなっており、変更はこの特定の文に限られています。

この修正により、オーファンドキュメントの取り扱いについてのガイダンスがより明確になり、ユーザーはドキュメント管理をより効果的に行うことができるようになります。また、他の関連情報は維持されているため、Document Storageの理解を深めるための参考になります。

## articles/search/search-how-to-index-sql-database.md{#item-86d873}

<details>
<summary>Diff</summary>
````diff
@@ -377,7 +377,7 @@ Database requirements:
 + Database must have [change tracking enabled](/sql/relational-databases/track-changes/enable-and-disable-change-tracking-sql-server)
 + Tables only (no views).
 + Tables can't be clustered. To meet this requirement, drop the clustered index and recreate it as non-clustered index. This workaround often degrades performance. Duplicating content in a second table that's dedicated to indexer processing can be a helpful mitigation. 
-+ Tables can't be empty. If you use TRUNCATE TABLE to clear rows, a reset and rerun of the indexer won't remove the corresponding search documents. To remove orphaned search documents, you must [index them with a delete action](search-howto-reindex.md#delete-orphan-documents).
++ Tables can't be empty. If you use TRUNCATE TABLE to clear rows, a reset and rerun of the indexer won't remove the corresponding search documents. To remove orphaned search documents, you must [index them with a delete action](search-how-to-delete-documents.md#delete-a-single-document).
 + Primary key can't be a compound key (containing more than one column).
 + Primary key must be non-clustered if you want deletion detection.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SQLデータベースインデックスに関するドキュメントの更新"
}
```

### Explanation
この変更は、`search-how-to-index-sql-database.md` ファイルの更新を示し、SQLデータベースをインデックス化するための要件に関する情報が修正されています。主な内容の変更は以下の通りです。

- データベースの空でないテーブルに関する注意点が更新されました。具体的には、オーファンドキュメントを削除するためのアクションに関する参照が「search-howto-reindex.md#delete-orphan-documents」から「search-how-to-delete-documents.md#delete-a-single-document」に変更されました。この修正により、孤立した検索ドキュメントを削除するための手順が、適切なドキュメントにリンクされるようになっています。

- 他の条件（変更追跡の有効化、ビューの非対応、テーブルがクラスター化されていないこと、主キーに関する要件など）は変更されておらず、そのまま維持されています。

この変更により、SQLデータベースのインデックス作成に関するガイダンスがより具体的かつ効果的になり、ユーザーはオーファンドキュメントの管理方法を正確に理解できるようになります。全体として、SQLデータベースを利用した検索機能の有効性を高めるための重要な情報を提供しています。

## articles/search/search-how-to-load-search-index.md{#item-a72573}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: how-to
-ms.date: 10/02/2025
+ms.date: 01/13/2026
 ---
 
 # Load data into a search index in Azure AI Search
@@ -93,7 +93,7 @@ REST APIs are useful for initial proof-of-concept testing, where you can test in
    | upload | Similar to an "upsert" where the document is inserted if it's new, and updated or replaced if it exists. If the document is missing values that the index requires, the document field's value is set to null. |
    | merge | Updates a document that already exists, and fails a document that can't be found. Merge replaces existing values. For this reason, be sure to check for collection fields that contain multiple values, such as fields of type `Collection(Edm.String)`. For example, if a `tags` field starts with a value of `["budget"]` and you execute a merge with `["economy", "pool"]`, the final value of the `tags` field is `["economy", "pool"]`. It isn't `["budget", "economy", "pool"]`. |
    | mergeOrUpload | Behaves like merge if the document exists, and upload if the document is new. This is the most common action for incremental updates. |
-   | delete | Delete removes the specified document from the index. Any field you specify in a delete operation, other than the key field, is ignored. If you want to remove an individual field from a document, use merge instead and set the field explicitly to null.|
+   | delete | Delete removes the specified document from the index. Any field you specify in a delete operation, other than the key field, is ignored. If you want to remove an individual field from a document, use merge instead and set the field explicitly to null. For more information, see [Delete documents in a search index](search-how-to-delete-documents.md).|
 
    There are no ordering guarantees for which action in the request body is executed first. It's not recommended to have multiple "merge" actions associated with the same document in a single request body. If there are multiple "merge" actions required for the same document, perform the merging client-side before updating the document in the search index.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスのデータ読み込みに関するドキュメントの更新"
}
```

### Explanation
この変更は、`search-how-to-load-search-index.md` ファイルの更新を示しており、Azure AI Searchにおける検索インデックスへのデータの読み込み方法に関する情報が修正されています。主な内容の変更は以下の通りです。

- **日付の更新**: ドキュメントの日付が「10/02/2025」から「01/13/2026」に変更されました。これにより、最新の情報に基づいていることが示されています。

- **削除操作に関する説明の追加**: 削除操作の説明に「[Delete documents in a search index](search-how-to-delete-documents.md)」へのリンクが追加され、ユーザーがドキュメントを削除する際の追加情報を参照できるようになっています。元の記述では、この詳細な情報へのリンクがありませんでした。

これらの変更により、ユーザーは検索インデックスに関する最新のデータ読み込み手法を理解しやすくなり、特にドキュメント削除に関する手続きについての詳細情報にアクセスしやすくなりました。全体として、この修正はユーザーエクスペリエンスの向上と、情報のアップデートを目的としています。

## articles/search/search-howto-reindex.md{#item-46738a}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 09/28/2025
+ms.date: 01/13/2026
 ms.update-cycle: 180-days
 ---
 
@@ -53,7 +53,7 @@ The body of the request contains one or more documents to be indexed. Within the
 
    | Action | Effect |
    |--------|--------|
-   | delete | Removes the entire document from the index. If you want to remove an individual field, use merge instead, setting the field in question to null. Deleted documents and fields don't immediately free up space in the index. Every few minutes, a background process performs the physical deletion. Whether you use the Azure portal or an API to return index statistics, you can expect a small delay before the deletion is reflected in the Azure portal and through APIs. |
+   | delete | Removes the entire document from the index. If you want to remove an individual field, use merge instead, setting the field in question to null. Deleted documents and fields don't immediately free up space in the index. Every few minutes, a background process performs the physical deletion. Whether you use the Azure portal or an API to return index statistics, you can expect a small delay before the deletion is reflected in the Azure portal and through APIs. For more information, see [Delete documents in a search index](search-how-to-delete-documents.md).|
    | merge | Updates a document that already exists, and fails a document that can't be found. Merge replaces existing values. For this reason, be sure to check for collection fields that contain multiple values, such as fields of type `Collection(Edm.String)`. For example, if a `tags` field starts with a value of `["budget"]` and you execute a merge with `["economy", "pool"]`, the final value of the `tags` field is `["economy", "pool"]`. It won't be `["budget", "economy", "pool"]`. <br><br>The same behavior applies to complex collections. If the document contains a complex collection field named Rooms with a value of `[{ "Type": "Budget Room", "BaseRate": 75.0 }]`, and you execute a merge with a value of `[{ "Type": "Standard Room" }, { "Type": "Budget Room", "BaseRate": 60.5 }]`, the final value of the Rooms field will be `[{ "Type": "Standard Room" }, { "Type": "Budget Room", "BaseRate": 60.5 }]`. It won't append or merge new and existing values. |
    | mergeOrUpload | Behaves like merge if the document exists, and upload if the document is new. This is the most common action for incremental updates. |
    | upload | Similar to an "upsert" where the document is inserted if it's new, and updated or replaced if it exists. If the document is missing values that the index requires, the document field's value is set to null. |
@@ -316,42 +316,6 @@ If you added or renamed a field, use [select](search-query-odata-select.md) to r
 
 The Azure portal provides index size and vector index size. You can check these values after updating an index, but remember to expect a small delay as the service processes the change and to account for portal refresh rates, which can be a few minutes.
 
-## Delete orphan documents
-
-Azure AI Search supports document-level operations so that you can look up, update, and delete a specific document in isolation. The following example shows how to delete a document. 
-
-Deleting a document doesn't immediately free up space in the index. Every few minutes, a background process performs the physical deletion. Whether you use the Azure portal or an API to return index statistics, you can expect a small delay before the deletion is reflected in the Azure portal and API metrics.
-
-1. Identify which field is the document key. In the Azure portal, you can view the fields of each index. Document keys are string fields and are denoted with a key icon to make them easier to spot.
-
-1. Check the values of the document key field: `search=*&$select=HotelId`. A simple string is straightforward, but if the index uses a base-64 encoded field, or if search documents were generated from a `parsingMode` setting, you might be working with values that you aren't familiar with.
-
-1. [Look up the document](/rest/api/searchservice/documents/get) to verify the value of the document ID and to review its content before deleting it. Specify the key or document ID in the request. The following examples illustrate a simple string for the [Hotels sample index](search-get-started-portal.md) and a base-64 encoded string for the metadata_storage_path key of the [cog-search-demo index](tutorial-skillset.md).
-
-    ```http
-    GET https://[service name].search.windows.net/indexes/hotel-sample-index/docs/1111?api-version=2025-09-01
-    ```
-
-    ```http
-    GET https://[service name].search.windows.net/indexes/cog-search-demo/docs/aHR0cHM6Ly9oZWlkaWJsb2JzdG9yYWdlMi5ibG9iLmNvcmUud2luZG93cy5uZXQvY29nLXNlYXJjaC1kZW1vL2d1dGhyaWUuanBn0?api-version=2025-09-01
-    ```
-
-1. [Delete the document](/rest/api/searchservice/documents) using a delete `@search.action` to remove it from the search index.
-
-    ```http
-    POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/index?api-version=2025-09-01
-    Content-Type: application/json   
-    api-key: [admin key] 
-    {  
-      "value": [  
-        {  
-          "@search.action": "delete",  
-          "id": "1111"  
-        }  
-      ]  
-    }
-    ```
-
 ## See also
 
 + [Indexer overview](search-indexer-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "再インデックス作成に関するドキュメントの大幅なリファクタリング"
}
```

### Explanation
この変更は、`search-howto-reindex.md` ファイルの大幅なリファクタリングを示しており、Azure AI Searchにおける再インデックス作成に関する説明が根本的に変更されています。主な内容の詳細は以下の通りです。

- **日付の更新**: ドキュメントの日付が「09/28/2025」から「01/13/2026」に変更され、最新性が強調されています。

- **削除活動の簡素化**: 「delete」と「merge」といったアクションに関する説明が整理され、一部の文が削除されました。この部分では、削除がインデックス内のドキュメントからすぐに空きスペースを解放しないことについての情報が維持されていますが、全体の記述は簡略化され、冗長な部分がなくなっています。

- **孤立したドキュメントの削除に関するセクションの削除**: 「Delete orphan documents」と題されたセクションが完全に削除されました。このセクションでは、孤立したドキュメントの特定、確認、削除手順について詳しく説明がされていましたが、全体的に洗練された内容にするために取り除かれました。

このリファクタリングにより、再インデックス作成のプロセスがより簡潔かつ明確になり、ユーザーが情報をより迅速に理解できるようになっています。しかし、一部の重要な情報が削除されたため、特定のユースケース（孤立したドキュメントの処理）に関する情報は不足している可能性があります。全体として、文書はメンテナンス性と読みやすさを向上させることを目的としていますが、注意が必要です。

## articles/search/search-howto-run-reset-indexers.md{#item-fb10c8}

<details>
<summary>Diff</summary>
````diff
@@ -94,10 +94,10 @@ If you need to rebuild all or part of an index, use Reset APIs available at decr
 + [Reset Documents (preview)](#reset-docs) reindexes a specific document or list of documents
 + [Reset Skills (preview)](#reset-skills) invokes skill processing for a specific skill
 
-After reset, follow with a Run command to reprocess new and existing documents. Orphaned search documents having no counterpart in the data source can't be removed through reset/run. If you need to delete documents, see [Documents - Index](/rest/api/searchservice/documents) instead.
+After reset, follow with a Run command to reprocess new and existing documents. Orphaned search documents having no counterpart in the data source can't be removed through reset/run. If you need to delete specific documents, see [Delete documents in a search index](search-how-to-delete-documents.md) or [Documents - Index](/rest/api/searchservice/documents) instead.
 
 > [!NOTE]
-> Tables can't be empty. If you use TRUNCATE TABLE to clear rows, a reset and rerun of the indexer won't remove the corresponding search documents. To remove orphaned search documents, you must [index them with a delete action](search-howto-reindex.md#delete-orphan-documents).
+> Tables can't be empty. If you use TRUNCATE TABLE to clear rows, a reset and rerun of the indexer won't remove the corresponding search documents. To remove orphaned search documents, you must [index them with a delete action](search-how-to-delete-documents.md#delete-a-single-document).
 
 <a name="reset-indexers"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスリセットに関するドキュメントの修正"
}
```

### Explanation
この変更は、`search-howto-run-reset-indexers.md` ファイルの更新を示しており、Azure AI Searchにおけるインデックスリセットのプロセスに関する情報が改善されています。主な変更点は以下の通りです。

- **文言の修正**: 「特定のドキュメントを削除する必要がある場合、ドキュメントを削除するインデックスの方法を参照してください」という文がより具体的なリンクに更新されました。「[Documents - Index](/rest/api/searchservice/documents)」に加えて、「[Delete documents in a search index](search-how-to-delete-documents.md)」への参考文献が追加され、ユーザーはドキュメント削除の手続きにアクセスしやすくなっています。

- **注釈のリンク変更**: 注釈の部分で、「孤立した検索ドキュメントを削除するには、削除アクションでインデックスする必要があります」というセクションのリンクが「[search-howto-reindex.md#delete-orphan-documents]」から「[search-how-to-delete-documents.md#delete-a-single-document]」に修正されています。これにより、ユーザーは特定のドキュメントを削除するための最新の情報にアクセスできるようになっています。

この修正は、情報の明確さとアクセスビリティを向上させ、ユーザーが必要な手続きを迅速に見つけられるように配慮されています。全体として、この変更はユーザーの理解を助け、エラーを防ぐための重要な要素と位置付けられます。

## articles/search/search-query-access-control-rbac-enforcement.md{#item-d24df7}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn how query-time ACL and RBAC enforcement ensures secure document retrieval in Azure AI Search for indexes containing permission filters from data sources such as Azure Data Lake Storage (ADLS) Gen2 and SharePoint in Microsoft 365.  
 ms.service: azure-ai-search  
 ms.topic: article  
-ms.date: 12/01/2025  
+ms.date: 01/15/2026  
 author: mattgotteiner  
 ms.author: magottei 
 ---  
@@ -115,11 +115,13 @@ You can accomplish these tasks by adding a custom header, `x-ms-enable-elevated-
 
 ### Permissions for elevated-read requests
 
-Currently, you must [create a custom role](search-security-rbac.md#create-a-custom-role) to run queries with elevated permissions. Add the `Microsoft.Search/searchServices/indexes/contentSecurity/elevatedOperations/read` permission to run the queries.
+You must have [Search Index Data Contributor](search-security-rbac.md#built-in-roles-used-in-search) permissions or a [custom role](search-security-rbac.md#create-a-custom-role) that includes the Elevate Read permission.
+
+Queries are a data plane operation, so the custom role can only consist of atomic data plane permissions. For a custom role, add the `Microsoft.Search/searchServices/indexes/contentSecurity/elevatedOperations/read` permission.
 
 ### Add an elevated-read header to a query
 
-The following example is a query request against a search index.
+After you set up permissions, you can run the query. The following example is a query request against a search index.
 
 ```http
 POST {endpoint}/indexes('{indexName}')/search.post.search?api-version=2025-11-01-preview
@@ -137,7 +139,6 @@ x-ms-enable-elevated-read: true
 > [!IMPORTANT]
 > The `x-ms-enable-elevated-read` header only works on Search POST actions. You can't perform an elevated read query on a [knowledge base retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) action.
 
-
 ### Important ACL functionality behavior change in specific preview API versions
 
 Before REST API version `2025-11-01-preview`, earlier preview versions `2025-05-01-preview` and `2025-08-01-preview` returned all documents when using a service API key or authorized Entra roles, even if no user token was provided. Applications that didn’t validate the presence of a user token could inadvertently expose results to end users if not implemented correctly or following best practices.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリアクセス制御とRBAC施行に関するドキュメントの修正"
}
```

### Explanation
この変更は、`search-query-access-control-rbac-enforcement.md` ファイルに対する更新を示しており、Azure AI Searchにおけるクエリタイムのアクセス制御（ACL）と役割ベースのアクセス制御（RBAC）についての情報が改善されています。主な変更点は以下の通りです。

- **日付の更新**: 文書の日付が「12/01/2025」から「01/15/2026」に更新され、最新の情報であることが示されています。

- **権限に関する説明の明確化**: 「elevated permissions」を使用してクエリを実行するには、「Search Index Data Contributor」権限または「引き上げられた読み取り権限」を含むカスタムロールが必要であることが明記されました。これにより、必要な権限がより明確に理解できるようになっています。

- **クエリ実行の文言修正**: 「権限を設定した後、クエリを実行できます」という文が追加され、権限設定とクエリ実行の流れがわかりやすくなっています。

- **機能変更に関する重要な記述**: 過去のAPIバージョンに関する情報が保持されており、ユーザーがアクセス制御の実装におけるリスクを理解できるようにされていますが、新しい方針に基づくセキュリティの強化が示唆されます。

これらの変更は、ユーザーがクエリアクセス制御の遂行を理解しやすくし、今後の実装に対する注意を促す狙いがあります。全体として、文書はより明確で一貫性のある内容になっており、ユーザーの利用が促進されることが期待されます。

## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Use Azure role-based access control for granular permissions on ser
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 11/21/2025
+ms.date: 01/15/2026
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: how-to
@@ -76,7 +76,7 @@ The following roles are built in. If these roles are insufficient, [create a cus
 | [Contributor](/azure/role-based-access-control/built-in-roles#contributor) | Control & Data |  Same level of control plane access as Owner, minus the ability to assign roles or change authentication options. </br></br>On the data plane, this role has the same access as the Search Service Contributor role. It includes access to all data plane actions except the ability to query or index documents.|
 | [Reader](/azure/role-based-access-control/built-in-roles#reader) | Control & Data | Read access across the entire service, including search metrics, content metrics (storage consumed, number of objects), and the object definitions of data plane resources (indexes, indexers, and so on). However, it can't read API keys or read content within indexes. |
 | [Search Service Contributor](/azure/role-based-access-control/built-in-roles#search-service-contributor) | Control & Data | Read-write access to object definitions (indexes, aliases, synonym maps, indexers, data sources, and skillsets). This role is for developers who create objects, and for administrators who manage a search service and its objects, but without access to index content. Use this role to create, delete, and list indexes, get index definitions, get service information (statistics and quotas), test analyzers, create and manage synonym maps, indexers, data sources, and skillsets. See [`Microsoft.Search/searchServices/*`](/azure/role-based-access-control/resource-provider-operations#microsoftsearch) for the permissions list. |
-| [Search Index Data Contributor](/azure/role-based-access-control/built-in-roles#search-index-data-contributor) | Data | Read-write access to content in indexes. This role is for developers or index owners who need to import, refresh, or query the documents collection of an index. This role doesn't support index creation or management. By default, this role is for all indexes on a search service. See [Grant access to a single index](#grant-access-to-a-single-index) to narrow the scope.  |
+| [Search Index Data Contributor](/azure/role-based-access-control/built-in-roles#search-index-data-contributor) | Data | Read-write access to content in indexes. This role is for developers or index owners who need to import, refresh, or query the documents collection of an index. This role doesn't support index creation, updates, or deletion. By default, this role applies to all indexes on a search service. See [Grant access to a single index](#grant-access-to-a-single-index) to narrow the scope.  |
 | [Search Index Data Reader](/azure/role-based-access-control/built-in-roles#search-index-data-reader) | Data |  Read-only access for querying search indexes. This role is for apps and users who run queries. This role doesn't support read access to object definitions. For example, you can't read a search index definition or get search service statistics. By default, this role is for all indexes on a search service. See [Grant access to a single index](#grant-access-to-a-single-index) to narrow the scope.  |
 
 Combine these roles to get sufficient permissions for your use case.
@@ -94,6 +94,7 @@ Combine these roles to get sufficient permissions for your use case.
 |Access quotas and service statistics |❌|❌|✅|✅|❌|
 |Read/query an index |✅|✅|❌|❌|❌|
 |Upload data for indexing <sup>1</sup>|❌|✅|❌|❌|❌|
+|Elevated read regardless of permission filters <sup>2</sup>|❌|✅|❌|❌|❌|
 |Create or edit indexes/aliases |❌|❌|✅|✅|❌|
 |Create, edit and run indexers/data sources/skillsets |❌|❌|✅|✅|❌|
 |Create or edit synonym maps |❌|❌|✅|✅|❌|
@@ -108,6 +109,8 @@ Combine these roles to get sufficient permissions for your use case.
 
 <sup>1</sup> In the Azure portal, an Owner or Contributor can run the Import data wizards that create and load indexes, even though they can't upload documents in other clients. Data connections in the wizard are made by the search service itself and not individual users. The wizards have the `Microsoft.Search/searchServices/indexes/documents/*` permission necessary for completing this task.
 
+<sup>2</sup> Elevated read is used for debugging queries that obtain results using the identity of the called. For more information, see [Investigate incorrect query results](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results).
+
 Owners and Contributors grant the same permissions, except that only Owners can assign roles.
 
 ## Assign roles
@@ -211,6 +214,9 @@ This is a very specific role. It grants [GET or POST access](/rest/api/searchser
 
 This section provides basic steps for setting up the role assignment and is here for completeness, but we recommend [Use Azure AI Search without keys ](keyless-connections.md) for comprehensive instructions on configuring your app for role-based access.
 
+> [!NOTE]
+> As a developer, if you need to debug queries that are predicated on a Microsoft identity, you should use Search Index Data Contributor or create a custom role that gives you [elevated permissions for debug purposes](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results).
+
 #### [**Azure portal**](#tab/roles-portal-query)
 
 1. Sign in to the [Azure portal](https://portal.azure.com).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACに関するドキュメントの更新"
}
```

### Explanation
この変更は、`search-security-rbac.md` ファイルに関連する更新を示しており、Azureの役割ベースのアクセス制御（RBAC）に関する情報が強化されています。主な変更点は次の通りです。

- **日付の更新**: 更新の日付が「11/21/2025」から「01/15/2026」に変更され、文書の最新性が強調されています。

- **役割に関する説明の修正**: 「Search Index Data Contributor」ロールの説明が明確にされ、インデックスの作成、更新、削除がサポートされないことが強調されています。また、この役割がデフォルトですべてのインデックスに適用されることを明記しています。

- **新しい機能の追加**: 「Elevated read regardless of permission filters」という新しい権限項目が追加され、特定の条件下での読み取り権限について説明しています。これにより、クエリデバッグのために必要な権限が明確化されています。

- **注意書きの追加**: 注意事項として、開発者がMicrosoft IDに基づくクエリのデバッグを行う必要がある場合には、「Search Index Data Contributor」ロールまたはカスタムロールの作成を推奨する記述が加わりました。

これらの変更は、ユーザーがRBACを利用して文書にアクセスする方法をより適切に理解できるように設計されており、アクセス制御の実装や役割の組み合わせに関するガイダンスが強化されています。全体として、ドキュメントがより包括的で実用的な情報を提供する形に改善されています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -122,6 +122,8 @@ items:
         href: search-how-to-load-search-index.md
       - name: Import large data sets
         href: search-how-to-large-index.md
+      - name: Delete documents
+        href: search-how-to-delete-documents.md
       - name: Manage an index
         href: search-how-to-manage-index.md
       - name: Update or rebuild an index
@@ -243,7 +245,7 @@ items:
         - name: Index plain text
           href: search-how-to-index-azure-blob-plaintext.md
         - name: Index CSV
-          href: search-how-to-index-azure-blob-changed-deleted.md
+          href: search-how-to-index-azure-blob-csv.md
         - name: Index JSON
           href: search-how-to-index-azure-blob-json.md
         - name: Index Markdown
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次ファイルの更新"
}
```

### Explanation
この変更は、`toc.yml` ファイルに対する修正を示しており、Azureの検索に関連する文書の目次が更新されています。主な変更点は以下の通りです。

- **新しい項目の追加**: 「Delete documents」という新しいセクションが追加され、それに対応するリンク「search-how-to-delete-documents.md」が文書に組み込まれました。これにより、ユーザーがドキュメント削除に関する情報を簡単にアクセスできるようになっています。

- **変更されたリンク**: 「Index CSV」という項目のリンクが「search-how-to-index-azure-blob-changed-deleted.md」から「search-how-to-index-azure-blob-csv.md」に更新されており、より正確で具体的な情報を得られるようになっています。

これらの変更は、ユーザーが必要な情報を見つけやすくすることを目的としており、ドキュメントのナビゲーションが向上しています。全体的に、目次がより直感的で使いやすくなっている点が特筆されます。

## articles/search/vector-search-how-to-create-index.md{#item-97c769}

<details>
<summary>Diff</summary>
````diff
@@ -1,51 +1,51 @@
 ---
-title: Create a vector index
+title: Create a Vector Index
 titleSuffix: Azure AI Search
-description: Create or update a search index to include vector fields.
+description: Learn how to create or update a search index to include vector fields.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
+  - dev-focus
+ai-usage: ai-assisted
 ms.topic: how-to
-ms.date: 09/28/2025
+ms.date: 01/14/2026
 ---
 
-# Create a vector index
+# Create a vector index in Azure AI Search
 
-In Azure AI Search, you can use [Create or Update Index (REST API)](/rest/api/searchservice/indexes/create-or-update) to store vectors in a search index. A vector index is defined by an index schema that has vector fields, nonvector fields, and a vector configuration section.
+In Azure AI Search, you can store and query vectors in a search index. A *vector index* is defined by an index schema that has vector fields, nonvector fields, and a vector configuration section.
 
-When you create a vector index, you implicitly create an *embedding space* that serves as the corpus for vector queries. The embedding space consists of all vector fields populated with embeddings from the same embedding model. At query time, the system compares the vector query to the indexed vectors, returning results based on semantic similarity.
+Creating a vector index implicitly creates an *embedding space* that serves as the corpus for vector queries. The embedding space consists of all vector fields populated with embeddings from the same embedding model. At query time, the system compares the vector query to the indexed vectors and returns results based on semantic similarity.
 
-To index vectors in Azure AI Search, follow these steps:
+This article uses REST to explain how to create a vector index, which includes the following steps:
 
 > [!div class="checklist"]
-> + Start with a basic schema definition.
-> + Add vector algorithms and optional compression.
-> + Add vector field definitions.
-> + Load prevectorized data as a [separate step](#load-vector-data-for-indexing) or use [integrated vectorization](vector-search-integrated-vectorization.md) for data chunking and embedding during indexing.
+> + Start with a basic schema definition
+> + Add vector algorithms and optional compression
+> + Add vector field definitions
+> + Load prevectorized data as a [separate step](#load-vector-data-for-indexing) or use [integrated vectorization](vector-search-integrated-vectorization.md) to chunk and embed data during indexing
 
-This article uses REST for illustration. After you understand the basic workflow, continue with the Azure SDK code samples in the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) repo, which provides guidance on using vectors in test and production code.
-
-> [!TIP]
-> You can also use the Azure portal to [create a vector index](search-get-started-portal-import-vectors.md) and try out integrated data chunking and vectorization.
+After you understand the basic workflow, try the Azure SDK samples in the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) GitHub repo for guidance on using vectors in test and production code. You can also use the Azure portal to [create a vector index](search-get-started-portal-import-vectors.md) via integrated vectorization.
 
 ## Prerequisites
 
-+ An [Azure AI Search service](search-create-service-portal.md) in any region and on any tier. If you plan to use [integrated vectorization](vector-search-integrated-vectorization.md) with Azure AI skills and vectorizers, Azure AI Search must be in the same region as the embedding models hosted on Azure Vision in Foundry Tools.
++ An [Azure AI Search service](search-create-service-portal.md) in any region and on any tier. If you plan to use [integrated vectorization](vector-search-integrated-vectorization.md) with the Azure Vision skill and vectorizer, Azure AI Search must be in the same region as the embedding models hosted on Azure Vision in Foundry Tools.
 
-+ Your source documents must have [vector embeddings](vector-search-how-to-generate-embeddings.md) to upload to the index. You can also use [integrated vectorization](vector-search-integrated-vectorization.md) for this step.
++ For the recommended [keyless authentication](search-security-rbac.md), assign the **Search Service Contributor** and **Search Index Data Contributor** roles to your user account, managed identity, or service principal. For the less secure [key-based authentication](search-security-api-keys.md), obtain an admin API key.
 
-+ You should know the dimensions limit of the model that creates the embeddings so that you can assign that limit to the vector field. For **text-embedding-ada-002**, dimensions are fixed at 1536. For **text-embedding-3-small** or **text-embedding-3-large**, dimensions range from 1 to 1536 and from 1 to 3072, respectively.
++ Source documents with [vector embeddings](vector-search-how-to-generate-embeddings.md) to upload to the index. You can also use [integrated vectorization](vector-search-integrated-vectorization.md) for this task.
 
-+ You should know what similarity metric to use. For embedding models on Azure OpenAI, similarity is computed using [`cosine`](/azure/ai-services/openai/concepts/understand-embeddings#cosine-similarity).
++ The dimensions limit of your embedding model. `text-embedding-ada-002` is fixed at 1536, `text-embedding-3-small` ranges from 1 to 1536, and `text-embedding-3-large` ranges from 1 to 3072.
 
-+ You should know how to [create an index](search-how-to-create-search-index.md). A schema always includes a field for the document key, fields for search or filters, and other configurations for behaviors needed during indexing and queries.
++ The similarity metric for your embedding model. Azure OpenAI models use [`cosine`](/azure/ai-services/openai/concepts/understand-embeddings#cosine-similarity).
 
-## Limitations
++ Familiarity with [creating an index](search-how-to-create-search-index.md).  A schema always includes a field for the document key, fields for search or filters, and other configurations for behaviors needed during indexing and queries.
 
-Some search services created before January 2019 can't create a vector index. If this applies to you, create a new service to use vectors.
+> [!NOTE]
+> Some search services created before January 2019 can't create a vector index. If applicable, create a new service to use vectors.
 
 ## Prepare documents for indexing
 
@@ -61,7 +61,7 @@ Make sure your source documents provide the following content:
 
 Your search index should include fields and content for all of the query scenarios you want to support. Suppose you want to search or filter over product names, versions, metadata, or addresses. In this case, vector similarity search isn't especially helpful. Keyword search, geo-search, or filters that iterate over verbatim content would be a better choice. A search index that's inclusive of both vector and nonvector fields provides maximum flexibility for query construction and response composition.
 
-For a short example of a documents payload that includes vector and nonvector fields, see the [load vector data](#load-vector-data-for-indexing) section of this article.
+For a documents payload example, see the [Load vector data for indexing](#load-vector-data-for-indexing) section.
 
 ## Start with a basic index
 
@@ -384,7 +384,7 @@ If you're familiar with indexers and skillsets:
 
 ---
 
-## Query your index for vector content
+## Query an index for vector content
 
 For validation purposes, you can query the index using Search Explorer in the Azure portal or a REST API call. Because Azure AI Search can't convert a vector to human-readable text, try to return fields from the same document that provide evidence of the match. For example, if the vector query targets the `titleVector` field, you could select `title` for the search results.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルインデックス作成に関するドキュメントの改善"
}
```

### Explanation
この変更は、`vector-search-how-to-create-index.md` ファイルに対する修正を示しており、Azureのベクトルインデックス作成方法に関する文書が改善されています。主な変更点は以下の通りです。

- **タイトルと説明の更新**: ドキュメントのタイトルが「Create a vector index」から「Create a Vector Index」に変更され、より目を引く形式になっています。また、説明文も「Create or update a search index to include vector fields.」から「Learn how to create or update a search index to include vector fields.」に変更され、学習内容に焦点が当たるようになりました。

- **文章の明確化**: 文書の構成や内容が整理され、情報の流れが向上しています。例えば、ベクトルインデックスの定義や作成プロセスについての説明が簡潔で分かりやすくなっています。

- **手順の整理**: ベクトルインデックス作成に必要な手順が段階的に列挙され、各手順が明確に説明されています。具体的な手順内容が番号付きリストとして強調され、ユーザーが実際の操作に移りやすくなっています。

- **注意喚起の追加**: 古い検索サービスについての注意書きが追加され、2019年1月以前に作成されたサービスではベクトルインデックスが作成できないことが明記されています。具体的な対応として新しいサービスの作成が推奨されています。

- **用語の統一**: 文中で使用される用語や表現が統一され、読みやすさが増しています。特に「create a vector index」と「Create a vector index in Azure AI Search」など、表現の一貫性が保たれています。

全体として、これらの更新は文書のクオリティと明瞭性を向上させ、利用者がベクトルインデックスの作成プロセスを理解しやすくするための重要な改善となっています。


