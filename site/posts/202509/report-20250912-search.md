---
date: '2025-09-12'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5c4a3e6...MicrosoftDocs:b436d14
summary: 今回の変更では、ドキュメントが微細に更新され、特に「提案者（suggesters）」設定の削除や調整が行われたことが際立っています。また、エージェントリトリーバルソリューションに関連した新しい説明やリンクの追加により、ユーザーの利便性が向上しています。全体としては小規模な更新ですが、ドキュメント全体の整理とユーザー体験の改善に寄与しています。新機能にはAzure
  AI Searchにおけるリンクの追加やコードスニペットの提供が含まれ、ユーザーがサービスを効果的に利用しやすくなっています。重大な破壊的変更はないものの、「suggesters」設定の削除には注意が必要です。今回の更新は、エンジニアや開発者が技術をより簡潔に理解し、サービスの実装に集中できるように設計されています。全体的に、ユーザーのAzureサービス体験が向上することが期待されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5c4a3e6...MicrosoftDocs:b436d14){target="_blank"}

# Highlights
今回の変更においては、多くのドキュメントが微細に更新され、特に「提案者（suggesters）」設定の削除や調整が行われたことが注目されます。また、エージェントリトリーバルソリューションに関連した説明の追加や明確化、リンクの追加によりユーザーの利便性向上も図られています。これらの変更はすべて小規模な更新として分類されますが、ドキュメント全体の整理整頓とユーザー体験の向上に寄与しています。

## New features
- Azure AI Searchにおける新しいリンクの追加。
- 新しいコードスニペットを通じたエージェントリトリーバル実装の理解促進。

## Breaking changes
- 特に重大な破壊的変更はないが、「suggesters」設定が削除され、期待されるドキュメントの使用方法に注意が必要。

## Other updates
- 「suggesters」セクションの設定が単純化され、空配列になったことでドキュメントの簡素化。
- 検索キャパシティ計画での検索ユニットの説明更新。

# Insights
今回の変更は、Azure AI Searchを利用する開発者やエンジニアが、より効果的にサービスを活用できるように設計されています。特に、ドキュメントが簡潔で明瞭になるように意識されており、「suggesters」設定の削除は、その一例です。これにより、不要な設定や情報を取り除き、ユーザーが実装に集中できる環境を提供しています。

また、エージェントリトリーバルに関する更新では、技術的背景や実装例に関する情報が充実しており、初学者から既存のユーザーまで、幅広い層が参考にできるようになっています。リンクやサンプルコードが追加されたのは、実際の構築や設計におけるリソースとして役立つことを目的としています。

さらに、検索キャパシティの計画については、具体的な計算方法が提示されるようになりました。これにより、ユーザーは自身のサービスのスケーリングに関して、より根拠ある決定を下せるようになります。

全体として、Azure AIのドキュメントはより整然となり、技術的な習得や応用をスムーズに進められるよう支援しています。今後のアップデートでもこの流れが継続されることで、ユーザーのAzureサービス体験がさらに向上することが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [semantic-ranker-rest.md](#item-d74861) | minor update | 提案者の設定の削除 | modified | 1 | 7 | 8 | 
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | 提案者の設定の削除 | modified | 1 | 8 | 9 | 
| [index-add-suggesters.md](#item-28ed57) | minor update | 提案者に関する文書の修正 | modified | 12 | 12 | 24 | 
| [search-agentic-retrieval-how-to-pipeline.md](#item-1ad1c3) | minor update | エージェントリトリーバルソリューションに関する文書の強化 | modified | 68 | 18 | 86 | 
| [search-agentic-retrieval-how-to-retrieve.md](#item-5f7fc0) | minor update | エージェントリトリーバルの取得方法に関する文書の修正 | modified | 4 | 2 | 6 | 
| [search-agentic-retrieval-how-to-synthesize.md](#item-18668b) | minor update | エージェントリトリーバルの合成方法に関する文書の追加 | modified | 2 | 0 | 2 | 
| [search-capacity-planning.md](#item-0dd6c9) | minor update | 検索キャパシティ計画に関する文書の更新 | modified | 1 | 1 | 2 | 
| [search-knowledge-source-how-to-blob.md](#item-58d84a) | minor update | Blob知識ソースに関する文書の関連リンクの追加 | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/search/includes/quickstarts/semantic-ranker-rest.md{#item-d74861}

<details>
<summary>Diff</summary>
````diff
@@ -99,13 +99,7 @@ To update an index using the REST API, you must provide the entire schema, plus
            { "name": "id", "type": "Edm.String", "searchable": false, "filterable": false, "retrievable": false, "stored": true, "sortable": false, "facetable": false },
            { "name": "rid", "type": "Edm.String", "searchable": false, "filterable": false, "retrievable": false, "stored": true, "sortable": false, "facetable": false }],
       "scoringProfiles": [],
-      "suggesters": [
-        {
-          "name": "sg",
-          "searchMode": "analyzingInfixMatching",
-          "sourceFields": ["Address/City", "Address/Country", "Rooms/Type", "Rooms/Tags"]
-        }
-      ],
+      "suggesters": [],
       "analyzers": [],
       "normalizers": [],
       "tokenizers": [],
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "提案者の設定の削除"
}
```

### Explanation
この変更は、REST APIを使用してインデックスを更新するためのドキュメントの一部を修正したもので、特に「suggesters」セクションに関連しています。具体的には、提案者の設定が以前は定義されていましたが、これが削除され、現在は空の配列に変更されました。この修正により、提案者に関する具体的な設定がなくなり、インデックスの定義が簡略化されました。この変更は全体的なインデックス設定を整えるための小さな更新として位置づけられます。

## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -340,13 +340,6 @@ The `boostGenre` profile uses weighted text fields, boosting matches found in al
         }  
       ]  
     }  
-  ],  
-  "suggesters": [  
-    {  
-      "name": "sg",  
-      "searchMode": "analyzingInfixMatching",  
-      "sourceFields": [ "albumTitle", "artistName" ]  
-    }  
-  ]   
+  ]
 }  
 ```  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "提案者の設定の削除"
}
```

### Explanation
この変更は、スコアリングプロファイルに関するドキュメントの内容を修正したもので、特に「suggesters」セクションに関連しています。具体的には、以前は定義されていた提案者（suggesters）の設定が完全に削除されました。これにより、提案者の情報がなくなり、リファレンスが簡素化され、文書全体の明瞭性が向上します。この変更は、スコアリングプロファイルの設定を強化し、ドキュメントの構造を整えるための小さな更新として位置づけられます。

## articles/search/index-add-suggesters.md{#item-28ed57}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 04/14/2025
+ms.date: 09/11/2025
 ms.update-cycle: 365-days
 ms.custom:
   - devx-track-csharp
@@ -21,9 +21,9 @@ In Azure AI Search, typeahead or "search-as-you-type" is enabled by using a *sug
 
 Matches on partial terms can be either an autocompleted query or a suggested match. The same suggester supports both experiences.
 
-## Typeahead experiences in Azure AI Search
+## Typeahead experiences
 
-Typeahead can be either *autocomplete*, which completes a partial input for a whole term query, or *suggestions* that invite click through to a particular match. Autocomplete produces a query. Suggestions produce a matching document.
+Typeahead  in Azure AI Search can be either *autocomplete*, which completes a partial input for a whole term query, or *suggestions* that invite click through to a particular match. Autocomplete produces a query. Suggestions produce a matching document.
 
 The following screenshot illustrates both. Autocomplete anticipates a potential term, finishing *tw* with *in*. Suggestions are mini search results, where a field like `hotel name` represents a matching hotel search document from the index. For suggestions, you can surface any field that provides descriptive information.
 
@@ -45,7 +45,7 @@ To create a suggester, add one to an [index definition](/rest/api/searchservice/
 
 + If the string field is part of a complex type (for example, a City field within Address), include the parent in the field path: `"Address/City"` (REST, C#, and Python), or `["Address"]["City"]` (JavaScript).
 
-+ Use the default standard Lucene analyzer (`"analyzer": null`) or a [language analyzer](index-add-language-analyzers.md) (for example, `"analyzer": "en.Microsoft"`) on the field.
++ Use the default standard Lucene analyzer (`"analyzer": null`) or a [language analyzer](index-add-language-analyzers.md) (for example, `"analyzer": "fr.microsoft"`) on the field.
 
 If you try to create a suggester using preexisting fields, the API disallows it. Prefixes are generated during indexing, when partial terms in two or more character combinations are tokenized alongside whole terms. Given that existing fields are already tokenized, you have to rebuild the index if you want to add them to a suggester. For more information, see [Update or rebuild an index in Azure AI Search](search-howto-reindex.md).
 
@@ -68,21 +68,21 @@ When evaluating analyzers, consider using the [Analyze Text API](/rest/api/searc
 Fields that use [custom analyzers](index-add-custom-analyzers.md) or [built-in analyzers](index-add-custom-analyzers.md#built-in-analyzers), (except for standard Lucene) are explicitly disallowed to prevent poor outcomes.
 
 > [!NOTE]
-> If you need to work around the analyzer constraint, for example if you need a keyword or ngram analyzer for certain query scenarios, you should use two separate fields for the same content. This allows one of the fields to have a suggester, while the other can be set up with a custom analyzer configuration.
+> If you need to work around the analyzer constraint, for example if you need a keyword or ngram analyzer for certain query scenarios, you should use two separate fields for the same content. This allows one of the fields to have a suggester, while the other can be set up with a custom analyzer configuration. If you're using an indexer, you can map a source field to two different index fields to support multiple configuations.
 
 ## Create using the Azure portal
 
-When using **Add Index** or the **Import data** wizard to create an index, you have the option of enabling a suggester:
+In the Azure portal, you can specify a suggester when you select **Add index**.
 
-1. In the index definition, enter a name for the suggester.
-
-1. In each field definition for new fields, select a checkbox in the **Suggester** column. A checkbox is available on string fields only. 
-
-As previously noted, analyzer choice impacts tokenization and prefixing. Consider the entire field definition when enabling suggesters. 
+1. Select **Add index** and add a string field.
+1. Set field attribution to **Searchable**.
+1. Select an analyzer.
+1. Once fields are defined, select **Autocomplete settings**.
+1. Select the searchable string fields for which you want to enable an autocomplete experience.
 
 ## Create using REST
 
-In the REST API, add suggesters by using [Create Index](/rest/api/searchservice/indexes/create) or [Update Index](/rest/api/searchservice/indexes/create-or-update). 
+In the REST API, add suggesters by using [Create Index](/rest/api/searchservice/indexes/create). 
 
   ```json
   {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "提案者に関する文書の修正"
}
```

### Explanation
この変更は、Azure AI Searchにおける提案者（suggesters）に関連するドキュメントの内容を修正しました。主な変更点として、提案者の説明が簡潔にされ、具体的な例や手順も改善されています。また、提案者を作成するための過程における指示がより明確になり、特にAzureポータルでの操作手順が整理され、読みやすくなっています。加えて、分析器に関する部分も更新され、使用する分析器の例が異なるものに変更されました。これにより、ユーザーは提案者をより効果的に利用できるようになります。この更新は、ドキュメントの整合性を高め、ユーザー体験を向上させることを目的とした小規模な改善です。

## articles/search/search-agentic-retrieval-how-to-pipeline.md{#item-1ad1c3}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,11 @@
 ---
 title: Build an agentic retrieval solution
 titleSuffix: Azure AI Search
-description: Learn how to design and build a custom agentic retrieval solution where Azure AI Search handles data retrieval for your custom agents.
+description: Learn how to design and build a custom agentic retrieval solution where Azure AI Search handles data retrieval for your custom agents in AI Foundry.
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 08/29/2025
+ms.date: 09/10/2025
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.custom:
@@ -53,9 +53,9 @@ Use one of the following chat completion models with your AI agent:
 Use a package version that provides preview functionality. See the [`requirements.txt`](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/agentic-retrieval-pipeline-example/requirements.txt) file for more packages used in the example solution.
 
 ```
-azure-ai-projects==1.0.0b11
-azure-ai-agents==1.0.0
-azure-search-documents==11.6.0b12
+azure-ai-projects==1.1.0b3
+azure-ai-agents==1.2.0b3
+azure-search-documents==11.7.0b1
 ```
 
 ### Configure access
@@ -100,9 +100,17 @@ Azure OpenAI hosts the models used by the agentic retrieval pipeline. Configure
 
 Development tasks on the Azure AI Search side include:
 
-+ Create a knowledge agent on Azure AI Search that maps to your deployed model in Azure AI Foundry Model.
-+ Call the retriever and provide a query, conversation, and override parameters.
-+ Parse the response for the parts you want to include in your chat application. For many scenarios, just the content portion of the response is sufficient. 
++ [Create a knowledge source](search-knowledge-source-overview.md) that maps to a [searchable index](search-agentic-retrieval-how-to-index.md).
++ [Create a knowledge agent](search-agentic-retrieval-how-to-create.md) on Azure AI Search that maps to your deployed model in Azure AI Foundry Model.
++ [Call the retriever](search-agentic-retrieval-how-to-retrieve.md) and provide a query, conversation, and override parameters.
++ Parse the response for the parts you want to include in your chat application. For many scenarios, just the content portion of the response is sufficient. You can also try [answer synthesis](search-agentic-retrieval-how-to-synthesize.md) for a simpler workflow.
+
+Developments on the Azure AI Agent side include:
+
++ Set up the AI project client and an AI agent.
++ Add a tool to coordinate calls from the AI agent to the retriever and knowledge agent.
+
+Query processing is initiated by user interaction in a client app, such as a chat bot, that calls an AI agent. The AI agent is configured to use a tool that orchestrates the requests and directs the responses. When the chat bot calls the agent, the tool calls the [retriever](search-agentic-retrieval-how-to-retrieve.md) on Azure AI Search, waits for the response, and then sends the response back to the AI agent and chat bot. In Azure AI Search, you can use [answer synthesis](search-agentic-retrieval-how-to-synthesize.md) to obtain an LLM-generated response from within the query pipeline, or you can call an LLM in your code if you want more control over answer generation.
 
 ## Components of the solution
 
@@ -169,20 +177,20 @@ print(f"AI agent '{agent_name}' created or updated successfully")
 
 ### Add an agentic retrieval tool to AI Agent
 
-An end-to-end pipeline needs an orchestration mechanism for coordinating calls to the retriever and knowledge agent. You can use a [tool](/azure/ai-services/agents/how-to/tools/function-calling) for this task. The tool calls the Azure AI Search knowledge retrieval client and the Azure AI agent, and it drives the conversations with the user.
+An end-to-end pipeline needs an orchestration mechanism for coordinating calls to the retriever and knowledge agent on Azure AI Search. You can use a [tool](/azure/ai-services/agents/how-to/tools/function-calling) for this task. The tool is configured in the AI agent and it calls the Azure AI Search knowledge retrieval client and sends back responses that drive the conversation with the user.
 
 ```python
 from azure.ai.agents.models import FunctionTool, ToolSet, ListSortOrder
 
 from azure.search.documents.agent import KnowledgeAgentRetrievalClient
-from azure.search.documents.agent.models import KnowledgeAgentRetrievalRequest, KnowledgeAgentMessage, KnowledgeAgentMessageTextContent, KnowledgeAgentIndexParams
+from azure.search.documents.agent.models import KnowledgeAgentRetrievalRequest, KnowledgeAgentMessage, KnowledgeAgentMessageTextContent
 
 agent_client = KnowledgeAgentRetrievalClient(endpoint=endpoint, agent_name=agent_name, credential=credential)
 
 thread = project_client.agents.threads.create()
 retrieval_results = {}
 
-# AGENTIC RETRIEVAL DEFINITION DEFERRED TO NEXT SECTION
+# AGENTIC RETRIEVAL DEFINITION "LIFTED AND SHIFTED" TO NEXT SECTION
 
 functions = FunctionTool({ agentic_retrieval })
 toolset = ToolSet()
@@ -194,32 +202,68 @@ project_client.agents.enable_auto_function_calls(toolset)
 
 The messages sent to the agent tool include instructions for chat history and using the results obtained from [knowledge retrieval](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true) on Azure AI Search. The response is passed as a large single string with no serialization or structure.
 
+This code snippet is the agentic retrieval definition mentioned in the previous code snippet.
+
 ```python
 def agentic_retrieval() -> str:
     """
         Searches a NASA e-book about images of Earth at night and other science related facts.
         The returned string is in a JSON format that contains the reference id.
         Be sure to use the same format in your agent's response
+        You must refer to references by id number
     """
     # Take the last 5 messages in the conversation
     messages = project_client.agents.messages.list(thread.id, limit=5, order=ListSortOrder.DESCENDING)
     # Reverse the order so the most recent message is last
-    messages.data.reverse()
-    retrieval_result = retrieval_result = agent_client.retrieve(
+    messages = list(messages)
+    messages.reverse()
+    retrieval_result = agent_client.retrieve(
         retrieval_request=KnowledgeAgentRetrievalRequest(
-            messages=[KnowledgeAgentMessage(role=msg["role"], content=[KnowledgeAgentMessageTextContent(text=msg.content[0].text)]) for msg in messages.data],
-            target_index_params=[KnowledgeAgentIndexParams(index_name=index_name, reranker_threshold=2.5)]
+            messages=[
+                    KnowledgeAgentMessage(
+                        role=m["role"],
+                        content=[KnowledgeAgentMessageTextContent(text=m["content"])]
+                    ) for m in messages if m["role"] != "system"
+            ]
         )
     )
 
     # Associate the retrieval results with the last message in the conversation
-    last_message = messages.data[-1]
+    last_message = messages[-1]
     retrieval_results[last_message.id] = retrieval_result
 
     # Return the grounding response to the agent
     return retrieval_result.response[0].content[0].text
 ```
 
+## How to start the conversation
+
+To start the chat, use the standard Azure AI agent tool calling APIs. Send the message with questions, and the agent decides when to retrieve knowledge from your search index using agentic retrieval.
+
+```python
+from azure.ai.agents.models import AgentsNamedToolChoice, AgentsNamedToolChoiceType, FunctionName
+
+message = project_client.agents.messages.create(
+    thread_id=thread.id,
+    role="user",
+    content="""
+        Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown?
+        Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?
+    """
+)
+
+run = project_client.agents.runs.create_and_process(
+    thread_id=thread.id,
+    agent_id=agent.id,
+    tool_choice=AgentsNamedToolChoice(type=AgentsNamedToolChoiceType.FUNCTION, function=FunctionName(name="agentic_retrieval")),
+    toolset=toolset)
+if run.status == "failed":
+    raise RuntimeError(f"Run failed: {run.last_error}")
+output = project_client.agents.messages.get_last_message_text_by_role(thread_id=thread.id, role="assistant").text.value
+
+print("Agent response:", output.replace(".", "\n"))
+```
+
 ## How to improve data quality
 
 Search results are consolidated into a large unified string that you can pass to a chat completion model for a grounded answer. The following indexing and relevance tuning features in Azure AI Search are available to help you generate high quality results. You can implement these features in the search index, and the improvements in search relevance are evident in the quality of the response returned during retrieval.
@@ -240,11 +284,17 @@ The LLM determines the quantity of subqueries based on these factors:
 + Chat history
 + Semantic ranker input constraints
 
-As the developer, the best way to control the number of subqueries is by setting the `defaultMaxDocsForReranker` in either the knowledge agent definition or as an override on the retrieve action. 
+As the developer, the best way to control the number of subqueries is by setting the [maxSubQueries](/rest/api/searchservice/knowledge-agents/create-or-update?view=rest-searchservice-2025-08-01-preview#knowledgesourcereference&preserve-view=true) property in a knowledge agent. 
+
+The semantic ranker processes up to 50 documents as an input, and the system creates subqueries to accommodate all of the inputs to semantic ranker. For example, if you only wanted two subqueries, you could set `maxSubQueries` to 100 to accommodate all documents in two batches.
+
+The [semantic configuration](semantic-how-to-configure.md) in the index determines whether the input is 50 or not. If the value is less, the query plan specifies however many subqueries are necessary to meet the smaller input size. 
+
+<!-- As the developer, the best way to control the number of subqueries is by setting the `defaultMaxDocsForReranker` in either the knowledge agent definition or as an override on the retrieve action. 
 
 The semantic ranker processes up to 50 documents as an input, and the system creates subqueries to accommodate all of the inputs to semantic ranker. For example, if you only wanted two subqueries, you could set `defaultMaxDocsForReranker` to 100 to accommodate all documents in two batches.
 
-The [semantic configuration](semantic-how-to-configure.md) in the index determines whether the input is 50 or not. If the value is less, the query plan specifies however many subqueries are necessary to meet the `defaultMaxDocsForReranker` threshold.
+The [semantic configuration](semantic-how-to-configure.md) in the index determines whether the input is 50 or not. If the value is less, the query plan specifies however many subqueries are necessary to meet the `defaultMaxDocsForReranker` threshold. -->
 
 ## Control the number of threads in chat history
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルソリューションに関する文書の強化"
}
```

### Explanation
この変更は、Azure AI Searchにおけるエージェントリトリーバルソリューションに関するドキュメントの更新であり、特に設計と実装に焦点を当てています。大きな変更点は、文章の明確さと流れを改善するための追加および修正です。具体的には、AI Foundryとの統合に関する説明が追加され、使用するパッケージのバージョンが更新されました。

また、知識エージェントの作成やデータ取得のプロセスに関する詳細な手順が整理され、エージェントがどのようにユーザーの入力を処理し、知識を取得するかの流れが明示されました。さらには、エージェントリトリーバル定義に関する新しいコードスニペットが追加され、ユーザーが実際の実装を理解しやすくなっています。

この更新により、ユーザーはAzure AI Searchを活用したエージェントリトリーバルの実装手順をよりスムーズに理解できるようになります。全体的に見て、ドキュメントは機能的で使いやすいものになっており、より良いユーザーエクスペリエンスを提供することを目指しています。

## articles/search/search-agentic-retrieval-how-to-retrieve.md{#item-5f7fc0}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.date: 08/29/2025
 
 In Azure AI Search, *agentic retrieval* is a new parallel query architecture that uses a large language model (LLM) for query planning. It generates subqueries that broaden the scope of what's searchable and relevant. It incorporates chat history for context. The LLM studies the query and subdivides it into more targeted queries, using different phrases and terminology for subquery composition.
 
-This article explains how to use the [**retrieve method**](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true) that invokes a knowledge agent and parallel query processing. It's updated for the new 2025-08-01-preview, which introduces breaking changes from the 2025-05-01-preview. For help with breaking changes, see [Migrate your agentic retrieval code](search-agentic-retrieval-how-to-migrate.md).
+This article explains how to use the [**retrieve action**](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true) that invokes a knowledge agent and parallel query processing. It's updated for the new 2025-08-01-preview, which introduces breaking changes from the 2025-05-01-preview. For help with breaking changes, see [Migrate your agentic retrieval code](search-agentic-retrieval-how-to-migrate.md).
 
 This article also explains the three components of the retrieval response: 
 
@@ -27,7 +27,9 @@ This article also explains the three components of the retrieval response:
 The retrieve request can include instructions for query processing that override the defaults set on the knowledge agent.
 
 > [!NOTE]
-> By default, there's no model-generated "answer" in the response and you should pass the extracted response to an LLM so that it can ground its answer based on the search results. For an end-to-end example that includes this step, see [Build an agent-to-agent retrieval solution ](search-agentic-retrieval-how-to-pipeline.md) or [Azure OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo). Alternatively, you can use [answer synthesis](search-agentic-retrieval-how-to-synthesize.md) to bring answer formulation into the agentic pipeline. In this workflow, the knowledge agent output consists of LLM-formulated answers instead of the raw search results.
+> By default, there's no model-generated "answer" in the response and you should pass the extracted response to an LLM so that it can ground its answer based on the search results. For an end-to-end example that includes this step, see [Build an agent-to-agent retrieval solution ](search-agentic-retrieval-how-to-pipeline.md) or [Azure OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo).
+>
+>Alternatively, you can use [answer synthesis](search-agentic-retrieval-how-to-synthesize.md) to bring answer formulation into the agentic pipeline. In this workflow, the retriever response consists of LLM-formulated answers instead of the raw search results.
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルの取得方法に関する文書の修正"
}
```

### Explanation
このコードの変更は、Azure AI Searchにおけるエージェントリトリーバルの取得方法に関する文書を更新したものです。主な変更点は、「retrieve method」という表現が「retrieve action」に変更されたことです。この修正により、用語がより正確で、APIのアクションに即したものになりました。

また、ドキュメント内の注意喚起の部分では、回答の生成に関する情報が明確に整理されました。特に、デフォルトの応答にはモデル生成の「回答」がないことが説明され、それを処理するためにLLMを通じて抽出された応答を渡す必要があることが強調されています。さらに、「answer synthesis」への言及が明確化され、エージェントリトリーバルパイプラインにおいて、LLMによって生成された回答を使用する方法が示されています。

このような更新により、ユーザーはエージェントリトリーバルの使用方法について、特に取得アクションに関連する変更点や新しい機能をより容易に理解できるようになります。全体的に、文書の明確さと正確性が向上し、ユーザーの体験が向上することを目的としています。

## articles/search/search-agentic-retrieval-how-to-synthesize.md{#item-18668b}

<details>
<summary>Diff</summary>
````diff
@@ -144,6 +144,8 @@ Depending on your agent's configuration, the response might include other inform
 
 ## Related content
 
++ [Quickstart: Agentic retrieval in Azure AI Search (uses answer synthesis)](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Agentic-Retrieval/quickstart-agentic-retrieval.ipynb)
++ [Azure AI Search Blob knowledge source Python sample (uses answer synthesis)](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/knowledge/blob-knowledge-source.ipynb)
 + [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
 + [Create a knowledge agent](search-agentic-retrieval-how-to-create.md)
 + [Create a search index knowledge source](search-knowledge-source-how-to-index.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルの合成方法に関する文書の追加"
}
```

### Explanation
この変更は、Azure AI Searchにおけるエージェントリトリーバルの合成方法に関する文書に関連しています。具体的には、関連コンテンツセクションに新しいリンクが追加されました。これにより、ユーザーはエージェントリトリーバルと回答合成に関連する具体的なサンプルやクイックスタートガイドに簡単にアクセスできるようになります。

追加されたリンクは、以下の2つです：

1. **Quickstart: Agentic retrieval in Azure AI Search (uses answer synthesis)** - これはエージェントリトリーバルを使用したクイックスタートガイドで、具体的な実装方法を示しています。
2. **Azure AI Search Blob knowledge source Python sample (uses answer synthesis)** - こちらは、Blob knowledge sourceを利用したPythonのサンプルコードです。

これらの追加により、ドキュメントの実用性が向上し、ユーザーがエージェントリトリーバルの応用方法をより深く理解するためのリソースが提供されるようになっています。この更新は、学習や実装を進めるための有益な情報源を強化することを目的としています。

## articles/search/search-capacity-planning.md{#item-0dd6c9}

<details>
<summary>Diff</summary>
````diff
@@ -38,7 +38,7 @@ Capacity is expressed in *search units* that can be allocated in combinations of
 
 | Concept  | Definition|
 |----------|-----------|
-|*Search unit* | A single increment of total available capacity (36 units). A minimum of one unit is required to run the service. The first replica and partition pair is the first search unit. However, each extra instance of a replica *or* a partition consumes an extra search unit. For example, you start with one replica and partition (one search unit), add a second replica, you're now consuming two search units. A search unit is also the billing unit for an Azure AI Search service. |
+|*Search unit* | A single increment of total available capacity. A minimum of one search unit is required to run the service. Depending on your pricing tier, the maximum ranges from one to 36 units.<br><br>The number of search units equals the number of replicas multiplied by the number of partitions: R × P = SU. Each service starts with one replica and one partition, which consumes one unit: 1 × 1 = 1. Adding a second replica consumes two units: 2 × 1 = 2.<br><br>A search unit is also the billing unit for a search service. |
 |*Replica* | Instances of the search service, used primarily to load balance query operations. Each replica hosts one copy of an index. If you allocate three replicas, you have three copies of an index available for servicing query requests.|
 |*Partition* | Physical storage and I/O for read/write operations (for example, when rebuilding or refreshing an index). Each partition has a slice of the total index. If you allocate three partitions, your index is divided into thirds. |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索キャパシティ計画に関する文書の更新"
}
```

### Explanation
この変更は、検索キャパシティ計画に関する文書の内容に関するもので、特に「検索ユニット」についての定義が更新されました。具体的には、検索ユニットの説明がより明確になり、構成要素（レプリカとパーティション）の計算方法が導入されています。

調整された点は以下の通りです：

- 検索ユニットの最小要件が「サービスを実行するために1つの検索ユニットが必要」とされ、料金プランに応じた最大数（1から36）の範囲が示されるようになりました。
- 検索ユニットの数を計算する式「R × P = SU」（レプリカ数 × パーティション数 = 検索ユニット数）が追加され、この計算を利用して検索ユニット数を具体的に示しました。
- 検索ユニットが請求単位であることも明言されています。

このような修正により、文書は特に検索ユニットの役割や計算に関してユーザーにとってより理解しやすくなり、実際にサービスを構成する際のガイダンスが向上しました。全体的に、文書の内容が具体的で明確になったことで、ユーザーのニーズに応じた情報が提供されています。

## articles/search/search-knowledge-source-how-to-blob.md{#item-58d84a}

<details>
<summary>Diff</summary>
````diff
@@ -235,6 +235,8 @@ api-key: {{api-key}}
 
 ## Learn more
 
++ [Azure AI Search Blob knowledge source Python sample](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/knowledge/blob-knowledge-source.ipynb)
+
 + [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
 
 + [Agentic RAG: build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blob知識ソースに関する文書の関連リンクの追加"
}
```

### Explanation
この変更は、「Blob知識ソースの利用方法」に関する文書に関連するもので、主に関連リンクが2つ追加されました。これにより、ユーザーがBlob知識ソースの具体的な使用例や関連コンテンツに簡単にアクセスできるようになります。

追加されたリンクは以下の通りです：

1. **Azure AI Search Blob knowledge source Python sample** - これは、Blob知識ソースを利用したPythonのサンプルコードです。このリソースは、ユーザーが具体的な実装方法を学ぶのに役立ちます。
   
2. **Agentic retrieval in Azure AI Search** - Azure AI Searchにおけるエージェントリトリーバルについての文書へのリンクです。このリンクを通じて、ユーザーはエージェントリトリーバルの概念や実装についてさらに掘り下げることができます。

また、YouTubeのリンクも追加されており、Agentic RAGについてのビデオが紹介されています。

これらの変更により、文書はユーザーにとってより包括的で、豊富な情報源となるよう設計されています。新しいリンクの追加は、Blob知識ソースおよび関連する技術への理解を深めるための有益なリソースを提供し、学習体験を向上させることを目的としています。


