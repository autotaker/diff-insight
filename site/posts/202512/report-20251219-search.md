---
date: '2025-12-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a2d235e...MicrosoftDocs:38e3c32
summary: この更新では、エージェント検索に関する多くの文書が最新情報に改訂されました。特に、用語の変更やAPIのバージョン更新に関連する修正が行われています。新機能として、エージェント検索のクイックスタートガイドが改善され、最新のAzure
  SDKに関する情報が強調されました。また、「知識エージェント」という用語が「知識ベース」に変更され、古いAPIバージョンに関する情報が削除されました。その他、2025-08-01-previewから2025-11-01-previewへの移行に関する注意書きが多くのドキュメントから削除され、情報の一貫性が向上しています。この更新は、エージェント検索機能の利用を促進し、ユーザーエクスペリエンスの向上を目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a2d235e...MicrosoftDocs:38e3c32){target="_blank"}

<format>
# ハイライト
この更新では、エージェント検索に関する多くの文書が最新の情報に合わせて修正され、特に用語の変更やAPIバージョンの更新に関連した修正が行われています。

## 新機能
- エージェント検索のクイックスタートガイドがより明確になり、新しいAPIバージョンを使用した手順が整理されました。
- 知識ベースに関するドキュメントが改訂され、最新のAzure SDKについての情報が強調されました。

## 破壊的変更
- 「知識エージェント」という用語が「知識ベース」に変更され、以前のAPIバージョンに関する情報が削除されました。

## その他の更新
- 多くのドキュメントで、2025-08-01-previewから2025-11-01-previewへの移行に関連する注意書きが削除され、最新の用語・情報で統一されました。

# インサイト
最新のAzure AI Searchやエージェント検索の機能を活用するために、既存のドキュメントが更新されました。特に、APIやSDKのバージョン変更に伴う用語の改訂が幾つか行われ、情報の統一性が図られています。これにより、ユーザーはより正確に新しいシステムと機能にアクセスしやすくなり、ドキュメントが提供する情報の信頼性が向上しました。

用語とAPIの進化により、Azureポータルとプログラム的なアプローチの両方が強化され、エージェント検索の設定や使用がより効率的で直感的になっています。特に、知識ベースとの接続が簡潔になり、最新のアクセス制御モデル（RBACとAPIキー）が奨励されている点は今後の開発作業において重要な更新です。

画像ファイルの更新は、視覚的なガイドとしての効果をより高め、ユーザーが最新のステップを視覚的に確認しやすくするための改良と考えられます。

全体として、この更新はエージェント検索機能の利用を促進し、ユーザーエクスペリエンスを向上させるために設計されており、開発者は更新されたAPIおよびSDKを用いてよりスムーズにシステムを利用することが可能になります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-answer-synthesis.md](#item-f44e99) | minor update | エージェント検索の回答合成を有効にする方法の更新 | modified | 1 | 4 | 5 | 
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | エージェント検索パイプライン作成手順の小規模更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-how-to-migrate.md](#item-9653ea) | minor update | エージェント検索の移行ガイドの更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-how-to-retrieve.md](#item-d739cf) | minor update | エージェント検索の取得方法に関する文書の更新 | modified | 0 | 3 | 3 | 
| [agentic-retrieval-overview.md](#item-d1f354) | minor update | エージェント検索の概要に関する文書の更新 | modified | 3 | 5 | 8 | 
| [get-started-portal-agentic-retrieval.md](#item-2bf1dc) | minor update | Azureポータルでのエージェント検索のクイックスタートガイドの更新 | modified | 42 | 31 | 73 | 
| [agentic-knowledge-source-how-to-blob-csharp.md](#item-b5f755) | minor update | Blob C#を使用したエージェント知識ソースの手順文書の修正 | modified | 0 | 3 | 3 | 
| [agentic-knowledge-source-how-to-blob-python.md](#item-029d03) | minor update | Blob Pythonを使用したエージェント知識ソースの手順文書の修正 | modified | 0 | 3 | 3 | 
| [agentic-knowledge-source-how-to-blob-rest.md](#item-b5ce57) | minor update | Blob RESTを使用したエージェント知識ソースの手順文書の修正 | modified | 0 | 3 | 3 | 
| [agentic-knowledge-source-how-to-search-index-csharp.md](#item-d3510c) | minor update | C#を使用したエージェント知識ソースの検索インデックス手順の修正 | modified | 0 | 3 | 3 | 
| [agentic-knowledge-source-how-to-search-index-python.md](#item-58056f) | minor update | Pythonを使用したエージェント知識ソースの検索インデックス手順の修正 | modified | 0 | 3 | 3 | 
| [agentic-knowledge-source-how-to-search-index-rest.md](#item-e95367) | minor update | RESTを使用したエージェント知識ソースの検索インデックス手順の修正 | modified | 0 | 3 | 3 | 
| [agentic-retrieval-how-to-create-knowledge-base-csharp.md](#item-4469a2) | minor update | C#を使用した知識ベースの作成手順の修正 | modified | 1 | 4 | 5 | 
| [agentic-retrieval-how-to-create-knowledge-base-python.md](#item-4e498f) | minor update | Pythonを使用した知識ベースの作成手順の修正 | modified | 1 | 4 | 5 | 
| [agentic-retrieval-how-to-create-knowledge-base-rest.md](#item-37851c) | minor update | RESTを使用した知識ベースの作成手順の修正 | modified | 1 | 4 | 5 | 
| [create-knowledge-base.png](#item-0c94b6) | minor update | 知識ベース作成のための画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [create-knowledge-source.png](#item-104c67) | minor update | 知識ソース作成のための画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [search-api-preview.md](#item-511f5d) | minor update | エージェント的検索機能に関する情報の修正 | modified | 1 | 1 | 2 | 
| [tutorial-adls-gen2-indexer-acls.md](#item-6881a0) | minor update | ACLsに関する構文の修正 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-fa71b4) | minor update | 2025年12月の更新情報追加 | modified | 7 | 1 | 8 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-answer-synthesis.md{#item-f44e99}

<details>
<summary>Diff</summary>
````diff
@@ -32,10 +32,7 @@ You can enable answer synthesis in two ways:
 
 + A knowledge base that uses the [2025-11-01-preview syntax](agentic-retrieval-how-to-migrate.md).
 
-+ [Visual Studio Code](https://code.visualstudio.com/) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) or a prerelease package of an Azure SDK that provides the knowledge base REST APIs.
-
-> [!NOTE]
-> Although you can use the Azure portal to configure answer synthesis, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](agentic-retrieval-how-to-migrate.md).
++ [Visual Studio Code](https://code.visualstudio.com/) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) or a preview Azure SDK package that provides the knowledge base REST APIs.
 
 ## Enable answer synthesis on a knowledge base
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索の回答合成を有効にする方法の更新"
}
```

### Explanation
この変更は、エージェント検索における回答合成を有効にする手段に関する文書の更新を含んでいます。具体的には、以下の調整が行われました：

1. **追加と削除**: 新しい情報が1行追加され、4行が削除されており、全体としては5つの変更が行われています。
2. **文言の修正**: 2025-11-01-preview構文を使用する知識ベースに関する情報が新たに追加されました。この情報は、回答合成の設定方法に関連する重要なコンテキストを提供します。
3. **旧情報の削除**: 変更によって、以前の「知識エージェント」用語を使用する2025-08-01-previewに関する情報が削除され、これに伴い、破壊的変更に関する注意喚起を示す部分も削除されています。これにより、ユーザーは最新の機能に基づいた正確な情報にアクセスできるようになります。

この更新は、ユーザーが回答合成の設定をより効率的に行えるようにするためのものであり、最新のAzure SDKに関する情報を反映させることを目的としています。

## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -312,7 +312,7 @@ index_client.delete_knowledge_base(base_name)
 print(f"Knowledge base '{base_name}' deleted successfully")
 
 # Delete the knowledge source
-index_client.delete_knowledge_source(knowledge_source=knowledge_source_name) # This is new feature in 2025-08-01-Preview api version
+index_client.delete_knowledge_source(knowledge_source=knowledge_source_name)
 print(f"Knowledge source '{knowledge_source_name}' deleted successfully.")
 
 # Delete the search index
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索パイプライン作成手順の小規模更新"
}
```

### Explanation
この変更は、エージェント検索のパイプラインを作成する手順に関するドキュメントの小規模な更新を示しています。具体的には、以下の修正が行われました：

1. **追加と削除**: 1行が新たに追加され、既存の1行が削除されており、計2つの変更が生じています。
2. **機能の説明**: `index_client.delete_knowledge_source` メソッドの説明が更新され、2025-08-01-preview APIバージョンに関連する機能の言及が削除されました。これにより、最新の機能が常に考慮されるようになっています。
3. **コードの一貫性**: 更新されたコードは、より簡潔で明瞭になり、引数の指定も整理されているため、可読性が向上しています。

全体的にこの変更は、最新の情報を反映し、ユーザーに対してエージェント検索パイプラインの作成手順をより明確に提示することを目的としています。

## articles/search/agentic-retrieval-how-to-migrate.md{#item-9653ea}

<details>
<summary>Diff</summary>
````diff
@@ -41,7 +41,7 @@ You can continue to run older code with no updates if you retain the API version
 
 ### [**2025-11-01-preview**](#tab/migrate-11-01)
 
-If you're migrating from [2025-08-01-preview](#2025-08-01-preview-1), *knowledge agent* is renamed to *knowledge base*, and multiple properties are relocated to different objects and levels within an object definition.
+If you're migrating from [2025-08-01-preview](#2025-08-01-preview-1), "knowledge agent" is renamed to "knowledge base," and multiple properties are relocated to different objects and levels within an object definition.
 
 1. [Update searchIndex knowledge sources](#update-a-searchindex-knowledge-source).
 1. [Update azureBlob knowledge sources](#update-an-azureblob-knowledge-source).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索の移行ガイドの更新"
}
```

### Explanation
この変更は、エージェント検索の移行ガイドに関する文書の小規模な更新を反映しています。具体的には、以下の修正が行われました：

1. **追加と削除**: 1行が新たに追加され、1行が削除されており、合計で2つの変更が行われています。
2. **用語の修正**: 「knowledge agent」が「knowledge base」に改名されたことを説明する文で、引用符を追加しました。これにより、用語が明確に強調され、読者が変更内容を理解しやすくなっています。
3. **一貫性の向上**: 用語の統一と引用符の使用により、文書全体の見やすさと一貫性が向上しました。

全体的に、この更新は、ユーザーが2025-08-01-previewからの移行を行う際に必要な情報をより明確に提供することを目的としています。

## articles/search/agentic-retrieval-how-to-retrieve.md{#item-d739cf}

<details>
<summary>Diff</summary>
````diff
@@ -40,9 +40,6 @@ You can also use optional [answer synthesis](agentic-retrieval-how-to-answer-syn
 
 To follow the steps in this guide, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending REST API calls to Azure AI Search.
 
-> [!NOTE]
-> Although you can use the Azure portal to retrieve data from knowledge bases, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](agentic-retrieval-how-to-migrate.md).
-
 ## Set up the retrieve action
 
 A retrieve action is specified on a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md). The knowledge base has one or more knowledge sources. Retrieval can return a synthesized answer in natural language or raw grounding chunks from the knowledge sources.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索の取得方法に関する文書の更新"
}
```

### Explanation
この変更は、エージェント検索の取得方法に関する文書の小規模な更新を示しています。以下の重要な修正が行われました：

1. **削除**: 3行が削除され、要点が簡潔にまとめられています。削除された部分は、Azureポータルに関する注意書きや、2025-08-01-previewでの用語関連の情報に関する記述です。
2. **情報のクリアランス**: Azureポータルに関する情報が削除されることで、混乱を避け、ユーザーに対して最新の情報を提供することに重点を置いています。
3. **文書の集中化**: 不要な情報を削除することにより、文書がより明確になり、ユーザーが必要な手順に集中できるようになっています。

全体として、この変更は、アクションや手順についての理解を容易にすることを目的としており、ユーザーがエージェント検索機能をより効果的に利用できるようにしています。

## articles/search/agentic-retrieval-overview.md{#item-d1f354}

<details>
<summary>Diff</summary>
````diff
@@ -98,16 +98,14 @@ Your application drives the pipeline by calling the knowledge base and handling
 
 ## How to get started
 
-To create an agentic retrieval solution, you must use a preview REST API version or a prerelease Azure SDK package that provides the functionality.
+To create an agentic retrieval solution, you can use the Azure portal, the latest preview REST APIs, or a preview Azure SDK package that provides the functionality.
 
-Currently, Azure portal support for agentic retrieval is limited to the 2025-08-01-preview. We recommend using a programmatic approach to access the latest features.
+Currently, the portal only supports the creation of search index and blob knowledge sources. We recommend using a programmatic approach to create other types of knowledge sources.
 
 ### [**Quickstarts**](#tab/quickstarts)
 
-+ [Quickstart: Use agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md)
-  + This quickstart supports C#, Java, JavaScript, Python, TypeScript, and REST.
 + [Quickstart: Use agentic retrieval in the Azure portal](get-started-portal-agentic-retrieval.md)
-  + The portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. Breaking changes apply to objects created in this quickstart.
++ [Quickstart: Use agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md) (C#, Java, JavaScript, Python, TypeScript, REST)
 
 ### [**How-to guides**](#tab/how-to-guides)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索の概要に関する文書の更新"
}
```

### Explanation
この変更は、エージェント検索の概要に関する文書に対する小規模な更新を示しています。以下の重要な変更点が含まれています：

1. **追加と削除**: 3行が追加され、5行が削除されており、計8つの変更が行われました。新しい情報に基づいて内容が整理され、最新の利用可能な機能に対応しています。
2. **Azureポータルの対応範囲の明確化**: エージェント検索ソリューションを作成するために、ユーザーはAzureポータルや最新のプレビューREST API、プレビューAzure SDKパッケージを使用できることが強調されています。また、ポータルの機能制限についても明確にされています。
3. **クイックスタートガイドの修正**: クイックスタートガイドのリンクが更新され、新しい情報が反映されています。特に、ポータルを使用したエージェント検索のクイックスタートガイドが追加され、言語の選択肢も同行しています。
4. **プログラム的アプローチの推奨**: 一部の機能はプログラム的なアプローチを通じてのみ利用可能であることが示されており、開発者が最適な方法で新機能にアクセスできるよう指導しています。

全体として、この更新はユーザーがエージェント検索機能を理解し、利用しやすくなることを目的としており、最新の手法と機能を強調しています。

## articles/search/get-started-portal-agentic-retrieval.md{#item-2bf1dc}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2025
 ms.topic: quickstart
-ms.date: 11/07/2025
+ms.date: 12/18/2025
 ---
 
 # Quickstart: Use agentic retrieval in the Azure portal
@@ -27,7 +27,7 @@ The portal guides you through the process of creating the following objects:
 Afterwards, you test the knowledge base by submitting a complex query that requires information from multiple documents and reviewing the synthesized answer.
 
 > [!IMPORTANT]
-> Because the portal uses the 2025-08-01-preview REST API version for agentic retrieval, the knowledge source and knowledge base created in this quickstart aren't compatible with the latest 2025-11-01-preview. For help with breaking changes, see [Migrate your agentic retrieval code](agentic-retrieval-how-to-migrate.md).
+> The portal now uses the 2025-11-01-preview REST APIs for knowledge sources and knowledge bases. If you previously created agentic retrieval objects in the portal, those objects use the 2025-08-01-preview and are subject to breaking changes. We recommend that you [migrate existing objects and code](agentic-retrieval-how-to-migrate.md) as soon as possible.
 
 ## Prerequisites
 
@@ -127,44 +127,41 @@ To create the knowledge source for this quickstart:
 
 1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
 
-1. From the left pane, select **Knowledge retrieval** > **Knowledge sources**.
+1. From the left pane, select **Agentic retrieval** > **Knowledge sources**.
 
 1. Select **Add knowledge source** > **Add knowledge source**.
 
-1. Enter **earth-at-night-ks** for the name.
+1. Select **Azure blob**.
 
-1. Select **Azure blob**, and then select your subscription, storage account, and container with the sample data.
+1. Enter **earth-at-night-ks** for the name, and then select your subscription, storage account, and container with the sample data.
 
 1. Select the **Authenticate using managed identity** checkbox. Leave the identity type as **System-assigned**.
 
 1. Select **Add vectorizer**.
 
 1. Select **Azure AI Foundry** for the kind, and then select your subscription, project, and embedding model deployment.
 
-1. Select **System managed identity** for the authentication type.
+1. Select **System assigned identity** for the authentication type.
 
 1. Create the knowledge source.
 
    :::image type="content" source="media/get-started-portal-agentic-retrieval/create-knowledge-source.png" alt-text="Screenshot of the knowledge source configuration for this quickstart." lightbox="media/get-started-portal-agentic-retrieval/create-knowledge-source.png" :::
 
 ## Create a knowledge base
 
-> [!NOTE]
-> The portal uses the 2025-08-01-preview, which refers to "knowledge bases" as "knowledge agents." Although the portal UI uses the latest terminology, the underlying REST API objects and JSON payloads still use "knowledge agents."
-
 A knowledge base uses your knowledge source and deployed LLM to orchestrate agentic retrieval. When a user submits a complex query, the LLM generates subqueries that are sent simultaneously to your knowledge source. Azure AI Search then semantically ranks the results for relevance and combines the best results into a single, unified response.
 
 The output mode determines how the knowledge base formulates answers. You can either use extractive data for verbatim content or [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md) for natural-language answer generation. By default, the portal uses answer synthesis.
 
 To create the knowledge base for this quickstart:
 
-1. From the left pane, select **Knowledge retrieval** > **Knowledge bases**.
+1. From the left pane, select **Agentic retrieval** > **Knowledge bases**.
 
 1. Select **Add knowledge base** > **Add knowledge base**.
 
 1. Enter **earth-at-night-kb** for the name.
 
-1. Under **Model deployment**, select **Add model deployment**.
+1. Under **Chat completion model**, select **Add model deployment**.
 
 1. Select **Azure AI Foundry** for the kind, and then select your subscription, project, and LLM deployment.
 
@@ -193,55 +190,69 @@ To query the knowledge base:
 1. Review the synthesized, citation-backed answer, which should be similar to the following example.
 
     ```
-    The suburban belts exhibit larger December brightening compared to urban cores due to the increased use of decorative and festive lighting in residential areas, which are more prevalent in suburban regions. In contrast, urban cores, despite having higher absolute light levels, experience less seasonal variation in lighting. The Phoenix nighttime street grid is sharply visible from space because of its regular grid layout and the extensive use of street lighting, which creates a consistent and bright pattern. Conversely, large stretches of interstate highways between Midwestern cities are less illuminated, as they primarily serve as transit routes with minimal lighting infrastructure, resulting in comparatively dim visibility from space.
+    Suburban belts show larger December brightening in satellite nighttime lights than urban cores mainly because of relative (percentage) change effects and differences in how light is used and distributed. Areas with lower baseline light (suburbs, residential streets) can increase lighting use or reflect more light in winter and so show a bigger percent change, while bright urban cores are already near sensor saturation so their relative increase is small. The retrieved material explains that brightest lights are generally the most urbanized but not necessarily the most populated, and that poor or low‑light areas can have large populations but low availability or use of electric lights; thus lower‑light suburbs can exhibit larger relative changes when seasonal lighting rises.
     ```
 
-1. Select the debug icon to review the activity log, which should be similar to the following example.
+1. Select the debug icon to review the activity log, which should be similar to the following JSON.
 
-    ```
+    ```JSON
     [
       {
         "type": "modelQueryPlanning",
         "id": 0,
-        "inputTokens": 2081,
-        "outputTokens": 128,
-        "elapsedMs": 1577
+        "inputTokens": 1518,
+        "outputTokens": 284,
+        "elapsedMs": 3001
       },
       {
         "type": "azureBlob",
         "id": 1,
         "knowledgeSourceName": "earth-at-night-ks",
-        "queryTime": "2025-11-03T15:09:28.172Z",
-        "count": 0,
-        "elapsedMs": 731,
+        "queryTime": "2025-12-12T18:54:28.792Z",
+        "count": 1,
+        "elapsedMs": 456,
         "azureBlobArguments": {
-          "search": "Why do suburban belts display larger December brightening than urban cores despite higher downtown light levels?"
+          "search": "causes of December brightening in satellite nighttime lights suburban vs urban cores"
         }
       },
       {
         "type": "azureBlob",
         "id": 2,
         "knowledgeSourceName": "earth-at-night-ks",
-        "queryTime": "2025-11-03T15:09:28.669Z",
+        "queryTime": "2025-12-12T18:54:29.389Z",
         "count": 3,
-        "elapsedMs": 497,
+        "elapsedMs": 596,
         "azureBlobArguments": {
-          "search": "Why is the Phoenix nighttime street grid sharply visible from space compared to dim interstates in the Midwest?"
+          "search": "factors affecting seasonal variation in nighttime lights December winter brightening suburban belts urban cores"
         }
       },
       {
-        "type": "semanticReranker",
+        "type": "azureBlob",
         "id": 3,
-        "inputTokens": 0
+        "knowledgeSourceName": "earth-at-night-ks",
+        "queryTime": "2025-12-12T18:54:29.862Z",
+        "count": 6,
+        "elapsedMs": 472,
+        "azureBlobArguments": {
+          "search": "why is Phoenix street grid highly visible at night from space compared to dim interstates in the Midwest reasons lighting patterns road lighting urban form"
+        }
       },
       {
-        "type": "modelAnswerSynthesis",
+        "type": "agenticReasoning",
         "id": 4,
-        "inputTokens": 3938,
-        "outputTokens": 136,
-        "elapsedMs": 1963
+        "retrievalReasoningEffort": {
+          "kind": "low"
+        },
+        "reasoningTokens": 111243
+      },
+      {
+        "type": "modelAnswerSynthesis",
+        "id": 5,
+        "inputTokens": 7514,
+        "outputTokens": 1058,
+        "elapsedMs": 12334
       }
-    ]   
+    ]
     ```
 
    The activity log offers insight into the steps taken during retrieval, including query planning and execution, semantic ranking, and answer synthesis. For more information, see [Review the activity array](agentic-retrieval-how-to-retrieve.md#review-the-activity-array).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureポータルでのエージェント検索のクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azureポータルでのエージェント検索に関するクイックスタートガイドの更新を示しています。主要な修正点は以下の通りです：

1. **APIバージョンの更新**: ポータルが2025-11-01-preview REST APIsを使用するようになり、これに関連する記述が新しくなっています。以前のAPIバージョンを使用して作成したオブジェクトについても、大きな変更があることが強調されています。
   
2. **手順の変更**: 各ステップの手順が整理され、以下の項目が変更されています：
   - 知識ソースや知識ベースを扱う際のメニュー名の変更（例：**Knowledge retrieval**から**Agentic retrieval**へ）。
   - モデルデプロイメントのセクション名が変更され、より明確な表現が用いられています。
   
3. **新しい構成要素の追加**: 新しい内容が追加され、特にAzure AI Foundryを用いた設定手順が強化され、ユーザーが迅速に作業を進められるようになっています。

4. **デバッグ情報の改善**: デバッグ情報の出力形式がJSONに変更され、出力例の具体性が増しています。これにより、ユーザーはアクティビティログを理解しやすくなります。

5. **引用の改善**: クイックスタートガイド内のコード例や情報が最新のデータに基づいて修正され、利用者にとって実用的な情報の提供が強化されています。

この更新により、ユーザーは最新の機能や手順を把握しやすくなり、エージェント検索の利用がよりスムーズになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-csharp.md{#item-b5f755}

<details>
<summary>Diff</summary>
````diff
@@ -33,9 +33,6 @@ Unlike a [search index knowledge source](../../agentic-knowledge-source-how-to-s
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
-> [!NOTE]
-> Although you can use the Azure portal to create blob knowledge sources, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](../../agentic-retrieval-how-to-migrate.md).
-
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources using C#](knowledge-source-check-csharp.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blob C#を使用したエージェント知識ソースの手順文書の修正"
}
```

### Explanation
この変更は、Blob C#を使用したエージェント知識ソースの手順に関する文書に対する小規模な修正を示しています。具体的な変更点は以下の通りです：

1. **不要なノートの削除**: AzureポータルにおけるBlob知識ソース作成に関する注意書きが削除されました。このガイドでは、古い「知識エージェント」という用語や、2025-08-01-preview APIの機能制限が述べられていましたが、これが明示的に表示されなくなりました。

2. **アクセス権についての強調**: Azure AI Searchでオブジェクトを作成し使用するための権限についての説明が追加され、ロールベースのアクセス制御（RBAC）を利用することが推奨される点が強調されています。また、APIキーを使用するオプションも記載されています。

3. **手順の簡略化**: 存在する知識ソースのチェックに関するセクションが簡略化されており、C#を使用したチェックに関するインクルード文がそのままにされています。

この更新により、ユーザーは最新の手順と推奨されるアクセス管理の方法をより明確に理解できるようになり、システムの使用が効率化されることを目的としています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-python.md{#item-029d03}

<details>
<summary>Diff</summary>
````diff
@@ -33,9 +33,6 @@ Unlike a [search index knowledge source](../../agentic-knowledge-source-how-to-s
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
-> [!NOTE]
-> Although you can use the Azure portal to create blob knowledge sources, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](../../agentic-retrieval-how-to-migrate.md).
-
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources using Python](knowledge-source-check-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blob Pythonを使用したエージェント知識ソースの手順文書の修正"
}
```

### Explanation
この変更は、Blob Pythonを使用したエージェント知識ソースの手順に関する文書の小規模な修正を示しています。具体的な変更点は以下の通りです：

1. **不要なノートの削除**: AzureポータルによるBlob知識ソース作成に関する注意書きが削除されました。このノートでは、古い「知識エージェント」用語や、2025-08-01-preview APIでの機能制限が説明されていましたが、これがなくなりました。

2. **アクセス権についての強調**: Azure AI Searchでオブジェクトを作成し使用するための権限に関する説明が追加され、ロールベースのアクセス制御（RBAC）を使用することが推奨されています。また、役割の割り当てが実行できない場合のAPIキーの使用についても言及されています。

3. **手順の簡略化**: 存在する知識ソースをチェックする手順に関するセクションが簡略化されており、Pythonを使用したチェックに関するインクルード文が維持されています。

この更新により、ユーザーは手順をより理解しやすくなり、Azure AI Searchの使用における権限管理についてもクリアな情報を得ることができるため、よりスムーズに操作を行えるようになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-rest.md{#item-b5ce57}

<details>
<summary>Diff</summary>
````diff
@@ -33,9 +33,6 @@ Unlike a [search index knowledge source](../../agentic-knowledge-source-how-to-s
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
-> [!NOTE]
-> Although you can use the Azure portal to create blob knowledge sources, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](../../agentic-retrieval-how-to-migrate.md).
-
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources using REST](knowledge-source-check-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blob RESTを使用したエージェント知識ソースの手順文書の修正"
}
```

### Explanation
この変更は、Blob RESTを使用したエージェント知識ソースの手順に関する文書に対する小規模な修正を示しています。具体的な変更点は以下の通りです：

1. **不要なノートの削除**: AzureポータルによるBlob知識ソース作成に関する注意書きが削除されました。このノートでは、古い「知識エージェント」という用語や、2025-08-01-preview APIの機能制限が述べられていましたが、これが削除されました。

2. **アクセス権についての強調**: Azure AI Searchでオブジェクトを作成し、使用するための権限に関する説明が追加され、ロールベースのアクセス制御（RBAC）を利用することが推奨されています。また、役割の割り当てが不可能な場合にはAPIキーの使用についても言及があります。

3. **手順の簡略化**: 存在する知識ソースのチェックに関するセクションが簡略化されており、RESTを使用したチェックに関するインクルード文がそのままにされています。

この更新により、ユーザーは手順をより明確に理解し、Azure AI Searchの利用に関して権限管理に関する重要な情報を得ることができるため、操作の効率が向上します。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-csharp.md{#item-d3510c}

<details>
<summary>Diff</summary>
````diff
@@ -21,9 +21,6 @@ A *search index knowledge source* specifies a connection to an Azure AI Search i
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
-> [!NOTE]
-> Although you can use the Azure portal to create search index knowledge sources, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](../../agentic-retrieval-how-to-migrate.md).
-
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources using C#](knowledge-source-check-csharp.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#を使用したエージェント知識ソースの検索インデックス手順の修正"
}
```

### Explanation
この変更は、C#を使用したエージェント知識ソースの検索インデックスに関する手順文書の小規模な修正を示しています。具体的な変更点は以下の通りです：

1. **不要なノートの削除**: Azureポータルを用いて検索インデックス知識ソースを作成する際の注意書きが削除されました。このノートでは、以前の「知識エージェント」という用語や、2025-08-01-previewのAPIが新しい機能をサポートしていない旨が触れられていましたが、これが削除されています。

2. **アクセス権についての強調**: Azure AI Searchでオブジェクトを作成および使用するための権限に関する説明が追加されました。ロールベースのアクセス制御（RBAC）が推奨されていますが、役割の割り当てが不可能な場合にはAPIキーの利用についても言及されています。

3. **手順の簡略化**: 既存の知識ソースをチェックする手順に関するセクションが簡略化され、C#を利用したチェックに関するインクルード文が維持されています。

この更新により、ユーザーは手順をより明確に理解することができ、Azure AI Searchの利用に際して権限管理に関する重要な情報を得ることで、操作がスムーズに行えるようになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-python.md{#item-58056f}

<details>
<summary>Diff</summary>
````diff
@@ -21,9 +21,6 @@ A *search index knowledge source* specifies a connection to an Azure AI Search i
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
-> [!NOTE]
-> Although you can use the Azure portal to create search index knowledge sources, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](../../agentic-retrieval-how-to-migrate.md).
-
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources using Python](knowledge-source-check-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonを使用したエージェント知識ソースの検索インデックス手順の修正"
}
```

### Explanation
この変更は、Pythonを使用したエージェント知識ソースの検索インデックスに関する手順文書に対する小規模な修正を示しています。具体的な変更点は以下の通りです：

1. **不要なノートの削除**: Azureポータルを利用して検索インデックス知識ソースを作成する際の注意書きが削除されました。このノートでは、「知識エージェント」という以前の用語と、2025-08-01-previewのAPIがすべての2025-11-01-preview機能をサポートしていないことについて述べられていましたが、これが削除されています。

2. **アクセス権についての強調**: Azure AI Searchでオブジェクトを作成し、使用するための権限に関する重要な説明が追加されました。ロールベースのアクセス制御（RBAC）が推奨されており、役割の割り当てができない場合にはAPIキーの使用についても言及されています。

3. **手順の簡略化**: 既存の知識ソースをチェックするセクションが簡略化されており、Pythonを使用したチェックに関するインクルード文がそのまま維持されています。

この更新により、ユーザーは手順をより直感的に理解でき、Azure AI Searchの利用において権限管理に関する重要な情報を効果的に活用できるようになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-rest.md{#item-e95367}

<details>
<summary>Diff</summary>
````diff
@@ -21,9 +21,6 @@ A *search index knowledge source* specifies a connection to an Azure AI Search i
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
-> [!NOTE]
-> Although you can use the Azure portal to create search index knowledge sources, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](../../agentic-retrieval-how-to-migrate.md).
-
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources using REST](knowledge-source-check-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTを使用したエージェント知識ソースの検索インデックス手順の修正"
}
```

### Explanation
この変更は、RESTを使用したエージェント知識ソースの検索インデックスに関する手順文書に小規模な修正を行ったことを示しています。具体的な変更点は以下の通りです：

1. **不要なノートの削除**: Azureポータルを利用して検索インデックス知識ソースを作成する際の注意書きが削除されました。このノートでは、2025-08-01-previewのAPIが以前の「知識エージェント」という用語を使用し、2025-11-01-previewの機能をすべてサポートしていないことが記載されていましたが、これが削除されています。

2. **アクセス権についての強調**: Azure AI Searchでオブジェクトを作成・使用するための権限に関する説明が追加されました。ロールベースのアクセス制御（RBAC）が推奨され、役割の割り当てが行えない場合にはAPIキーを使用する方法についても言及されています。

3. **手順の簡略化**: 既存の知識ソースをチェックする方法についてのセクションが簡略化され、RESTを使用したチェックに関するインクルード文がそのまま維持されています。

この更新により、ユーザーは手順をより明確に理解でき、Azure AI Searchを使用する際の権限管理に関して重要な情報を適切に活用することが可能になります。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-csharp.md{#item-4469a2}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ A knowledge base specifies:
 After you create a knowledge base, you can update its properties at any time. If the knowledge base is in use, updates take effect on the next retrieval.
 
 > [!IMPORTANT]
-> 2025-11-01-preview renames the 2025-08-01-preview *knowledge agent* to *knowledge base*. This is a breaking change. We recommend [migrating existing code](../../agentic-retrieval-how-to-migrate.md) to the new APIs as soon as possible.
+> 2025-11-01-preview renames the 2025-08-01-preview "knowledge agent" to "knowledge base." This is a breaking change. We recommend [migrating existing code](../../agentic-retrieval-how-to-migrate.md) to the new APIs as soon as possible.
 
 ## Prerequisites
 
@@ -35,9 +35,6 @@ After you create a knowledge base, you can update its properties at any time. If
 
 + The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
 
-> [!NOTE]
-> Although you can use the Azure portal to create knowledge bases, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](../../agentic-retrieval-how-to-migrate.md).
-
 ### Supported models
 
 Use one of the following LLMs from Azure OpenAI or an equivalent open-source model. For deployment instructions, see [Deploy Azure OpenAI models with Microsoft Foundry](/azure/ai-foundry/how-to/deploy-models-openai).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#を使用した知識ベースの作成手順の修正"
}
```

### Explanation
この変更は、C#を使用して知識ベースを作成する手順における小規模な修正を示しています。具体的な変更内容は以下の通りです：

1. **用語の統一**: 2025-11-01-previewにおいて、2025-08-01-previewの「知識エージェント」の用語が「知識ベース」に変更されたことについての説明が修正されました。この変更によって、用語が一貫して引用されるようになり、明確さが向上しています。

2. **重要な情報の強調**: 知識エージェントから知識ベースへの名称変更が破壊的変更であることを再確認し、既存のコードの新しいAPIへの移行を推奨する情報が維持されています。

3. **前提条件の追加**: Python用の最新のプレビュー版`azure-search-documents`クライアントライブラリが前提条件として新たに追加され、ユーザーに必要なツールについての情報が提供されています。

4. **ノートの削除**: Azureポータルを使用して知識ベースを作成する際に以前の「知識エージェント」用語を使うことについての注意書きが削除され、ユーザーが不要な情報に混乱することを防いでいます。

これらの変更により、ドキュメントはより正確で、利用者が知識ベースの作成に関して必要な情報を容易に得られるようになります。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-python.md{#item-4e498f}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ A knowledge base specifies:
 After you create a knowledge base, you can update its properties at any time. If the knowledge base is in use, updates take effect on the next retrieval.
 
 > [!IMPORTANT]
-> 2025-11-01-preview renames the 2025-08-01-preview *knowledge agent* to *knowledge base*. This is a breaking change. We recommend [migrating existing code](../../agentic-retrieval-how-to-migrate.md) to the new APIs as soon as possible.
+> 2025-11-01-preview renames the 2025-08-01-preview "knowledge agent" to "knowledge base." This is a breaking change. We recommend [migrating existing code](../../agentic-retrieval-how-to-migrate.md) to the new APIs as soon as possible.
 
 ## Prerequisites
 
@@ -35,9 +35,6 @@ After you create a knowledge base, you can update its properties at any time. If
 
 + The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
 
-> [!NOTE]
-> Although you can use the Azure portal to create knowledge bases, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](../../agentic-retrieval-how-to-migrate.md).
-
 ### Supported models
 
 Use one of the following LLMs from Azure OpenAI or an equivalent open-source model. For deployment instructions, see [Deploy Azure OpenAI models with Microsoft Foundry](/azure/ai-foundry/how-to/deploy-models-openai).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonを使用した知識ベースの作成手順の修正"
}
```

### Explanation
この変更は、Pythonを使用して知識ベースを作成する手順に関する小規模な修正を示しています。具体的な変更内容は以下の通りです：

1. **用語の統一**: 2025-11-01-previewにおいて、2025-08-01-previewの「知識エージェント」が「知識ベース」に変更されたことが、引用符を用いて正確に表現されています。この修正により、用語の使用が一貫し、文書の明瞭さが向上しました。

2. **重要な情報の強調**: 知識エージェントから知識ベースへの変更が破壊的なものであることが再確認され、既存のコードを新しいAPIに移行することを推奨する内容が維持されています。

3. **前提条件の追加**: Python用の最新のプレビュー版`azure-search-documents`クライアントライブラリが新たに前提条件としてリストに追加され、ユーザーが必要とするライブラリについての重要な情報が提供されています。

4. **ノートの削除**: Azureポータルを使用して知識ベースを作成する際に「知識エージェント」用語を使用することに関する注記が削除され、必要のない情報への混乱を避けています。

これらの変更により、ドキュメントはより正確で、利用者が知識ベースの作成に関して必要な情報を容易に得られるように改善されています。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-rest.md{#item-37851c}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ A knowledge base specifies:
 After you create a knowledge base, you can update its properties at any time. If the knowledge base is in use, updates take effect on the next retrieval.
 
 > [!IMPORTANT]
-> 2025-11-01-preview renames the 2025-08-01-preview *knowledge agent* to *knowledge base*. This is a breaking change. We recommend [migrating existing code](../../agentic-retrieval-how-to-migrate.md) to the new APIs as soon as possible.
+> 2025-11-01-preview renames the 2025-08-01-preview "knowledge agent" to "knowledge base." This is a breaking change. We recommend [migrating existing code](../../agentic-retrieval-how-to-migrate.md) to the new APIs as soon as possible.
 
 ## Prerequisites
 
@@ -35,9 +35,6 @@ After you create a knowledge base, you can update its properties at any time. If
 
 + The latest preview version of the [`Azure.Search.Documents` client library](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1) for the .NET SDK.
 
-> [!NOTE]
-> Although you can use the Azure portal to create knowledge bases, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](../../agentic-retrieval-how-to-migrate.md).
-
 ### Supported models
 
 Use one of the following LLMs from Azure OpenAI or an equivalent open-source model. For deployment instructions, see [Deploy Azure OpenAI models with Microsoft Foundry](/azure/ai-foundry/how-to/deploy-models-openai).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTを使用した知識ベースの作成手順の修正"
}
```

### Explanation
この変更は、RESTを使用して知識ベースを作成する手順に関する小規模な修正を示しています。具体的な変更内容は以下の通りです：

1. **用語の統一**: 2025-11-01-previewにおいて、2025-08-01-previewの「知識エージェント」が「知識ベース」に変更されたことが、正確な引用符を用いて表現されるようになりました。この変更により、用語が明確に統一され、ドキュメントの読みやすさが向上しています。

2. **重要情報の強調**: 知識エージェントから知識ベースへの名称変更が破壊的な変更であることが再度強調され、ユーザーに既存のコードを新しいAPIに移行することを推奨する内容が維持されています。

3. **前提条件の追加**: .NET SDK用の最新のプレビュー版`Azure.Search.Documents`クライアントライブラリが前提条件として新たに追加され、必要な情報が提供されています。

4. **ノートの削除**: Azureポータルを使用して知識ベースを作成する際に以前の「知識エージェント」用語を使うことについての注記が削除され、この情報が不要であることが考慮されています。

これらの修正により、ドキュメントはより正確で、利用者がREST APIを使用して知識ベースを作成するために必要な情報を容易に得られるように改善されています。

## articles/search/media/get-started-portal-agentic-retrieval/create-knowledge-base.png{#item-0c94b6}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ベース作成のための画像ファイルの更新"
}
```

### Explanation
この変更は、知識ベースを作成する際の画像ファイルに関するもので、実際のコンテンツの追加や削除は行われていません。ただし、ファイル自体が修正されたことを示しています。具体的には以下のポイントがあります：

- **画像ファイルの更新**: `create-knowledge-base.png`という画像ファイルが変更されたが、内容の追加や削除は行われていません。この変更により、ドキュメント内で画像が最新の情報や視覚表現に沿ったものに更新されている可能性があります。

この変更は、ユーザーが知識ベースを作成する際の視覚的な理解を向上させるためのものと考えられますが、具体的な変更内容については画像ファイルの直接の確認が必要です。

## articles/search/media/get-started-portal-agentic-retrieval/create-knowledge-source.png{#item-104c67}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ソース作成のための画像ファイルの更新"
}
```

### Explanation
この変更は、知識ソースを作成する際に使用される画像ファイルに関するもので、具体的なコンテンツの変更は行われていませんが、画像自体が更新されたことを示しています。以下が主なポイントです：

- **画像ファイルの変更**: `create-knowledge-source.png`という画像が修正されましたが、コンテンツの追加や削除はありません。この更新により、画像が最新の情報や視覚的な表現に適合している可能性があります。

この更新は、ユーザーが知識ソースを作成するための理解を深めるためにビジュアルを改善することが狙いであると考えられます。画像の具体的な内容を確認するには、画像ファイルへの直接のアクセスが必要です。

## articles/search/search-api-preview.md{#item-511f5d}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ Preview features are removed from this list if they're retired or transition to
 
 | Feature | Description | Availability |
 |--|--|--|
-| [**Agentic retrieval**](agentic-retrieval-overview.md) | Create a conversational search experience powered by large language models (LLMs). Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries simultaneously, reranks the results for relevance, and either extracts grounding data or synthesizes answers into natural language. To get started, see [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md).<p>The pipeline involves one or more [knowledge sources](agentic-knowledge-source-overview.md#supported-knowledge-sources) within a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), whose [response payload](agentic-retrieval-how-to-retrieve.md) provides full transparency into the query plan and reference data.<p>Knowledge sources and knowledge bases created in the Azure portal use the 2025-08-01-preview schema and aren't compatible with the latest 2025-11-01-preview. To get started, see [Quickstart: Agentic retrieval in the Azure portal](get-started-portal-agentic-retrieval.md). | [Knowledge Sources (preview)](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true), [Knowledge bases (preview)](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true), [Knowledge Retrieval (preview)](/rest/api/searchservice/knowledge-retrieval?view=rest-searchservice-2025-11-01-preview&preserve-view=true), and the Azure portal |
+| [**Agentic retrieval**](agentic-retrieval-overview.md) | Create a conversational search experience powered by large language models (LLMs). Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries simultaneously, reranks the results for relevance, and either extracts grounding data or synthesizes answers into natural language.<p>The pipeline involves one or more [knowledge sources](agentic-knowledge-source-overview.md#supported-knowledge-sources) within a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), whose [response payload](agentic-retrieval-how-to-retrieve.md) provides full transparency into the query plan and reference data.<p>To get started, see [Quickstart: Use agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md) (programmatic) or [Quickstart: Use agentic retrieval in the Azure portal](get-started-portal-agentic-retrieval.md). | [Knowledge Sources (preview)](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true), [Knowledge bases (preview)](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true), [Knowledge Retrieval (preview)](/rest/api/searchservice/knowledge-retrieval?view=rest-searchservice-2025-11-01-preview&preserve-view=true), and the Azure portal |
 | [**Purview index configuration**](search-indexer-sensitivity-labels.md) | Apply Microsoft Purview classifications and sensitivity labels to indexed content based on source metadata for enhanced data governance. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 | [**Scoring function aggregation**](index-add-scoring-profiles.md#example-function-aggregation) | Combine and aggregate multiple scoring functions, enabling more sophisticated relevance customization and weighted signal combination. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 | [**Facet aggregations**](search-faceted-navigation-examples.md#facet-aggregation-example) | Use sum, count, minimum, maximum, and other aggregate functions to provide enhanced analytics in faceted search experiences. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント的検索機能に関する情報の修正"
}
```

### Explanation
この変更は、`search-api-preview.md`というドキュメント内のエージェント的検索機能に関する情報が修正されたことに関するものです。具体的には、エージェント的検索機能に関する説明と関連するクイックスタートガイドへのリンクが更新されました。以下のポイントが含まれています：

- **追加と削除**: 総じて1つの文が追加され、1つの文が削除されました。これにより、情報の最新性が保たれています。
- **リンクの修正**: 機能の開始方法に関するクイックスタートガイドのリンクが具体的に更新され、プログラマティックな使用とAzureポータルでの使用の両方に対応する情報が含まれています。

この修正は、利用者に対してエージェント的検索機能の実装に関するより明確で整理された情報を提供することを目的としています。詳細な変更内容を確認するには、該当のドキュメントを直接見る必要があります。

## articles/search/tutorial-adls-gen2-indexer-acls.md{#item-6881a0}

<details>
<summary>Diff</summary>
````diff
@@ -79,7 +79,7 @@ As a best practice, use [`Group` sets](search-indexer-access-control-lists-and-r
 
 [Create an index](search-how-to-create-search-index.md#create-an-index) that contains fields for content and [permission metadata](search-indexer-access-control-lists-and-role-based-access.md#create-permission-fields-in-the-index).
 
-Be sure to use the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) or a prerelease Azure SDK that provides equivalent functionality. The permission filter properties are only available in the preview APIs.
+Be sure to use the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) or a preview Azure SDK package that provides equivalent functionality. The permission filter properties are only available in the preview APIs.
 
 For demo purposes, the permission field has `retrievable` enabled so that you can check the values from the index. In a production environment, you should disable `retrievable` to avoid leaking sensitive information.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ACLsに関する構文の修正"
}
```

### Explanation
この変更は、`tutorial-adls-gen2-indexer-acls.md`というチュートリアル文書内のアクセス制御リスト（ACLs）に関する情報についての軽微な修正を反映しています。具体的には、使用するAzure SDKパッケージに関する表現が修正されています。以下のポイントが含まれています：

- **文言の更新**: 「prerelease Azure SDK」という表現が「preview Azure SDK package」に変更され、より明確にプレビュー版のSDKパッケージを指すようになっています。
- **コンテキストの維持**: ACLの設定を利用する際に最新のプレビューREST APIや関連するSDKを使用することの重要性が強調されています。

この修正は、ユーザーに対して正確で最新の情報を提供し、ACLの設定に関する理解を助けることを目的としています。具体的な変更内容を確認するためには、該当のドキュメントを直接参照することが求められます。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Announcements of new and enhanced features, including a service ren
 author: haileytap
 ms.author: haileytapia
 manager: nitinme
-ms.date: 11/18/2025
+ms.date: 12/18/2025
 ms.service: azure-ai-search
 ms.topic: overview
 ms.custom:
@@ -20,6 +20,12 @@ Learn about the latest updates to Azure AI Search functionality, docs, and sampl
 > [!NOTE]
 > Preview features are announced here, but we also maintain a [preview features list](search-api-preview.md) so you can find them in one place.
 
+## December 2025
+
+| Item | Description |
+|--|--|
+| [2025-11-01-preview portal migration for agentic retrieval](get-started-portal-agentic-retrieval.md) | [Knowledge bases](agentic-retrieval-how-to-create-knowledge-base.md) and [knowledge sources](agentic-knowledge-source-overview.md) in the Azure portal have been updated to use the 2025-11-01-preview REST APIs instead of the 2025-08-01-preview. Portal-created knowledge bases now support the [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md), and query-time properties (maximum runtime and maximum output size) have been removed from the UI. The portal continues to support search index and blob knowledge sources only; other knowledge source types must be created programmatically.<p>If you previously created knowledge bases or knowledge sources in the portal, those objects still use the 2025-08-01-preview schema. For help with breaking changes, see [Migrate your agentic retrieval code](agentic-retrieval-how-to-migrate.md). |
+
 ## November 2025
 
 | Item | Description |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "2025年12月の更新情報追加"
}
```

### Explanation
この変更は、`whats-new.md`というドキュメントにおける最新の機能や改善点についての情報の更新を目的としています。具体的には、2025年12月に関する新しい項目が追加され、これに関連する詳細が記載されています。以下のポイントが含まれています：

- **日付の更新**: MS日付フィールドが「11/18/2025」から「12/18/2025」に変更され、最新の更新日を反映しています。
- **新しいセクションの追加**: 2025年12月に関連する新機能や変更内容が表形式で追加され、エージェント検索機能に対するREST APIの更新が説明されています。
- **詳細な説明**: 新しく追加された項目には、以前のバージョンとの互換性や移行に関する情報も含まれ、変更に対する理解を深めるためのリンクが提供されています。

この修正は、利用者に最新の機能やサービスの状態を正確に反映させるものであり、特にプレビュー機能についての詳細な情報を提供する役割も果たしています。具体的な更新内容を確認するには、該当のドキュメントを直接参照することが推奨されます。


