---
date: '2025-06-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:92ff08a...MicrosoftDocs:a20162d
summary: この文書の更新では、Azure サービス関連のドキュメントに小規模な変更と改善が加えられました。主な内容としては、新しいエラー項目の追加、C# クイックスタートガイドの更新、誤字の修正、言語タグの訂正があります。特に、Azure
  SQL インデクサーに関するトラブルシューティング情報が強化され、C# のクイックスタートガイドも最新のコーディングプラクティスに合わせて改善されました。これにより、ユーザーエクスペリエンスの向上とより正確な情報提供が実現され、Azure
  サービスの使用効率が向上します。全体として、開発者コミュニティに対するサポートがさらに強化されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:92ff08a...MicrosoftDocs:a20162d){target="_blank"}

<format>
# ハイライト
この文書の更新では、Azure サービス関連のドキュメントにいくつかの小規模な変更と改善が加えられました。新しいエラー項目や警告の追加、C# クイックスタートガイドの更新、誤字の修正、および言語タグの訂正が行われました。

## 新機能
- `articles/search/cognitive-search-common-errors-warnings.md` に新しいエラーの説明が追加され、より具体的なトラブルシューティング情報が提供されました。

## 破壊的変更
特に破壊的な変更はありません。

## 他の更新
- C# クイックスタートガイドの一貫性と可読性の改善。
- アプリポータル作成ガイドの誤字修正。
- エージェント検索クイックスタートガイドの言語タグの正確性が向上。

# 洞察
この変更セットは、ドキュメントの改善を図るいくつかの小規模な改良が含まれています。

まず、一般的なエラードキュメントに新たに追加された警告とエラーの項目として、「データ型不一致によるエラー」が挙げられます。これにより、Azure SQL インデクサーの使用時に発生しやすい型不一致の問題に対するガイダンスが強化されました。この情報の追加は、ユーザーが問題をより迅速に特定し、Azure サービスの適切な使用法を確立する助けとなるでしょう。

次に、C# でのエージェント検索のクイックスタートガイドでは、最新の Azure OpenAI ライブラリの使用方法に関する更新が行われ、開発者が最新のコーディングプラクティスを学びやすくしました。ここでは、コード例の整形とコメントの追加により、初心者にもわかりやすいガイドになっています。また、エラーハンドリングやコードの最適化も行われ、より実践的なリソースとなっています。

さらに、ドキュメントにおける誤字の修正や言語タグの間違いも見逃せません。これらの修正は小さいですが、ドキュメントの正確性と信頼性を向上させ、ユーザーエクスペリエンスを改善する重要な役割を果たします。これにより、正確な情報がユーザーに伝わりやすくなります。

全体として、この更新は Azure サービスを使用する際の効率性と正確性を向上させ、開発者コミュニティにより良いサポートを提供するものです。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-common-errors-warnings.md](#item-a5c854) | minor update | 一般的なエラーと警告に関する情報の更新 | modified | 9 | 0 | 9 | 
| [agentic-retrieval-csharp.md](#item-f93ed3) | minor update | C# におけるエージェント検索のクイックスタートガイドの更新 | modified | 79 | 71 | 150 | 
| [search-create-app-portal.md](#item-19ab44) | minor update | アプリポータル作成ガイドの誤字修正 | modified | 1 | 1 | 2 | 
| [search-get-started-agentic-retrieval.md](#item-4a40f4) | minor update | エージェント検索のクイックスタートガイドの言語タグ修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/cognitive-search-common-errors-warnings.md{#item-a5c854}

<details>
<summary>Diff</summary>
````diff
@@ -414,3 +414,12 @@ This warning is passed from the Language service of Azure AI services. In some c
 ## `Error: Cannot write more bytes to the buffer than the configured maximum buffer size`
 
 Indexers have [document size limits](search-limits-quotas-capacity.md#indexer-limits). Make sure that the documents in your data source are smaller than the supported size limit, as documented for your service tier. 
+
+<a name="error-failed-to-compare-type-value"></a>
+## `Error: Failed to compare value 'X' of type M to value 'Y' of type N.`
+
+This error usually happens in Azure SQL indexers when the source column type used for [`dataChangeDetectionPolicy`](search-how-to-index-sql-database.md#high-water-mark-change-detection-policy) doesn’t match what the indexer expects, especially if [`convertHighWaterMarkToRowVersion`](search-how-to-index-sql-database.md#converthighwatermarktorowversion) is turned on.
+
+For example, if the column used for change detection is of type datetime, but the indexer expects a rowversion type because convertHighWaterMarkToRowVersion is enabled, the mismatch will cause an error.
+
+Check the data type for the 'High Water Mark' column in the source and update the indexer configuration accordingly. Once verified and updated, reset and rerun the indexer to process the column values.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "一般的なエラーと警告に関する情報の更新"
}
```

### Explanation
この変更は、Azure AI サービスの言語サービスからの警告メッセージに関する文書に新しいエラーの項目を追加しました。具体的には、`Error: Failed to compare value 'X' of type M to value 'Y' of type N.`というエラーについての説明を含めています。このエラーは、Azure SQL インデクサーがデータ変更検出ポリシー用に使用するソースカラムの型と、インデクサーが期待する型が一致しない場合に発生することが詳細に説明されています。

追加された内容では、`dataChangeDetectionPolicy`に関連する設定や、`convertHighWaterMarkToRowVersion`が有効になっている場合の注意点について具体的な例を挙げて説明しています。また、'High Water Mark'カラムのデータ型を確認し、インデクサー構成を適切に更新する手順が示されています。この変更により、ユーザーが直面する可能性のあるエラーをより理解しやすくなり、適切な対処ができるようサポートしています。

## articles/search/includes/quickstarts/agentic-retrieval-csharp.md{#item-f93ed3}

<details>
<summary>Diff</summary>
````diff
@@ -48,7 +48,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
     dotnet add package Azure.Search.Documents --version 11.7.0-beta.4
     ```
 
-1. Install the Azure OpenAI client library ([Azure.AI.OpenAI](/dotnet/api/overview/azure.ai.openai-readme)) for .NET with:
+1. Install the Azure OpenAI client library ([Azure.AI.OpenAI](/dotnet/api/azure.ai.openai)) for .NET with:
 
     ```console
     dotnet add package Azure.AI.OpenAI --version 2.1.0
@@ -103,18 +103,21 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
     using OpenAI.Chat;
     
     namespace AzureSearch.Quickstart
-    {    class Program
+    {
+        class Program
         {
             static async Task Main(string[] args)
-            {            
+            {
                 // Load environment variables from .env file
                 // Ensure you have a .env file in the same directory with the required variables.
                 DotEnv.Load();
     
                 string endpoint = Environment.GetEnvironmentVariable("AZURE_SEARCH_ENDPOINT") 
                     ?? throw new InvalidOperationException("AZURE_SEARCH_ENDPOINT is not set.");
                 string azureOpenAIEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT") 
-                    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");            string azureOpenAIGptDeployment = "gpt-4.1-mini";
+                    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
+                
+                string azureOpenAIGptDeployment = "gpt-4.1-mini";
                 string azureOpenAIGptModel = "gpt-4.1-mini";
                 string azureOpenAIEmbeddingDeployment = "text-embedding-3-large";
                 string azureOpenAIEmbeddingModel = "text-embedding-3-large";
@@ -123,15 +126,35 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
                 string agentName = "earth-search-agent";
     
                 var credential = new DefaultAzureCredential();            
+                
                 // Define the fields for the index
                 var fields = new List<SearchField>
                 {
-                    new SimpleField("id", SearchFieldDataType.String) { IsKey = true, IsFilterable = true, IsSortable = true, IsFacetable = true },
-                    new SearchField("page_chunk", SearchFieldDataType.String) { IsFilterable = false, IsSortable = false, IsFacetable = false },
-                    new SearchField("page_embedding_text_3_large", SearchFieldDataType.Collection(SearchFieldDataType.Single)) { VectorSearchDimensions = 3072, VectorSearchProfileName = "hnsw_text_3_large" },
-                    new SimpleField("page_number", SearchFieldDataType.Int32) { IsFilterable = true, IsSortable = true, IsFacetable = true }
-                };            
-                // Define the vectorizer
+                    new SimpleField("id", SearchFieldDataType.String) 
+                    { 
+                        IsKey = true, 
+                        IsFilterable = true, 
+                        IsSortable = true, 
+                        IsFacetable = true 
+                    },
+                    new SearchField("page_chunk", SearchFieldDataType.String) 
+                    { 
+                        IsFilterable = false, 
+                        IsSortable = false, 
+                        IsFacetable = false 
+                    },
+                    new SearchField("page_embedding_text_3_large", SearchFieldDataType.Collection(SearchFieldDataType.Single)) 
+                    { 
+                        VectorSearchDimensions = 3072, 
+                        VectorSearchProfileName = "hnsw_text_3_large" 
+                    },
+                    new SimpleField("page_number", SearchFieldDataType.Int32) 
+                    { 
+                        IsFilterable = true, 
+                        IsSortable = true, 
+                        IsFacetable = true 
+                    }
+                };// Define the vectorizer
                 var vectorizer = new AzureOpenAIVectorizer(vectorizerName: "azure_openai_text_3_large")
                 {
                     Parameters = new AzureOpenAIVectorizerParameters
@@ -191,7 +214,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
                     SemanticSearch = semanticSearch
                 };
     
-                // Create the index client and delete the index if it exists, then create it
+                // Create the index client. Delete the index if it exists and then recreate it.
                 var indexClient = new SearchIndexClient(new Uri(endpoint), credential);
                 try
                 {
@@ -201,9 +224,8 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
                 catch (Exception ex)
                 {
                     Console.WriteLine($"Index '{indexName}' could not be deleted or did not exist: {ex.Message}");
-                }
+                }            
                 await indexClient.CreateOrUpdateIndexAsync(index);
-    
                 Console.WriteLine($"Index '{indexName}' created or updated successfully");
     
                 // Download the documents from the GitHub URL
@@ -221,13 +243,11 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
                     {
                         KeyFieldAccessor = doc => doc["id"].ToString(),
                     }
-                );
-    
+                );            
                 await searchIndexingBufferedSender.UploadDocumentsAsync(documents);
                 await searchIndexingBufferedSender.FlushAsync();
+                Console.WriteLine($"Documents uploaded to index '{indexName}'");
     
-                Console.WriteLine($"Documents uploaded to index '{indexName}'");            
-
                 var openAiParameters = new AzureOpenAIVectorizerParameters
                 {
                     ResourceUri = new Uri(azureOpenAIEndpoint),
@@ -240,8 +260,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
                 var targetIndex = new KnowledgeAgentTargetIndex(indexName)
                 {
                     DefaultRerankerThreshold = 2.5f
-                };
-    
+                };            
                 // Create the knowledge agent
                 var agent = new KnowledgeAgent(
                     name: agentName,
@@ -250,7 +269,6 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
                 await indexClient.CreateOrUpdateKnowledgeAgentAsync(agent);
                 Console.WriteLine($"Search agent '{agentName}' created or updated successfully");
     
-    
                 string instructions = @"
                 A Q&A agent that can answer questions about the Earth at night.
                 Sources have a JSON format with a ref_id that must be cited in the answer.
@@ -264,46 +282,42 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
                         { "role", "system" },
                         { "content", instructions }
                     }
-                };
-    
+                };            
                 var agentClient = new KnowledgeAgentRetrievalClient(
                     endpoint: new Uri(endpoint),
                     agentName: agentName,
                     tokenCredential: new DefaultAzureCredential()
-                );            
-
+                );
+    
                 messages.Add(new Dictionary<string, object>
                 {
                     { "role", "user" },
                     { "content", @"
-                Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown?
-                Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?
-                " }
-                });
-    
+                    Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown?
+                    Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?
+                    " }
+                });            
                 var retrievalResult = await agentClient.RetrieveAsync(
                     retrievalRequest: new KnowledgeAgentRetrievalRequest(
-                            messages: messages
-                                .Where(message => message["role"].ToString() != "system")
-                                .Select(
-                                message => new KnowledgeAgentMessage(
-                                    role: message["role"].ToString(),
-                                    content: new[] { new KnowledgeAgentMessageTextContent(message["content"].ToString()) }))
-                                .ToList()
-                            )
-                        {
-                            TargetIndexParams = { new KnowledgeAgentIndexParams { IndexName = indexName, RerankerThreshold = 2.5f } }
-                        }
-                    );
-    
+                        messages: messages
+                            .Where(message => message["role"].ToString() != "system")
+                            .Select(message => new KnowledgeAgentMessage(
+                                role: message["role"].ToString(),
+                                content: new[] { new KnowledgeAgentMessageTextContent(message["content"].ToString()) }))
+                            .ToList()
+                    )
+                    {
+                        TargetIndexParams = { new KnowledgeAgentIndexParams { IndexName = indexName, RerankerThreshold = 2.5f } }
+                    }
+                );            
                 messages.Add(new Dictionary<string, object>
                 {
                     { "role", "assistant" },
                     { "content", (retrievalResult.Value.Response[0].Content[0] as KnowledgeAgentMessageTextContent).Text }
                 });
     
-                // Print 
-                Console.WriteLine((retrievalResult.Value.Response[0].Content[0] as KnowledgeAgentMessageTextContent).Text);            
+                Console.WriteLine((retrievalResult.Value.Response[0].Content[0] as KnowledgeAgentMessageTextContent).Text);
+    
                 Console.WriteLine("Activities:");
                 foreach (var activity in retrievalResult.Value.Activity)
                 {
@@ -325,50 +339,46 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
                         reference.GetType(),
                         new JsonSerializerOptions { WriteIndented = true }
                     );
-                    Console.WriteLine(referenceJson);
-                }
-    
+                    Console.WriteLine(referenceJson);            }
     
                 AzureOpenAIClient azureClient = new(
                     new Uri(azureOpenAIEndpoint),
                     new DefaultAzureCredential());
-                ChatClient chatClient = azureClient.GetChatClient(azureOpenAIGptDeployment);            
+                ChatClient chatClient = azureClient.GetChatClient(azureOpenAIGptDeployment);
+    
                 List<ChatMessage> chatMessages = messages
                     .Select<Dictionary<string, object>, ChatMessage>(m => m["role"].ToString() switch
                     {
                         "user" => new UserChatMessage(m["content"].ToString()),
                         "assistant" => new AssistantChatMessage(m["content"].ToString()),
                         "system" => new SystemChatMessage(m["content"].ToString()),
                         _ => null
-                    })
+                    })                
                     .Where(m => m != null)
                     .ToList();
     
-    
                 var result = await chatClient.CompleteChatAsync(chatMessages);
-    
                 Console.WriteLine($"[ASSISTANT]: {result.Value.Content[0].Text.Replace(".", "\n")}");
     
                 messages.Add(new Dictionary<string, object>
                 {
                     { "role", "user" },
-                    { "content", "How do I find lava at night?" }
+                    { "content", "How do I find lava at night?" }            
                 });
     
                 var retrievalResult2 = await agentClient.RetrieveAsync(
                     retrievalRequest: new KnowledgeAgentRetrievalRequest(
-                            messages: messages
-                                .Where(message => message["role"].ToString() != "system")
-                                .Select(
-                                message => new KnowledgeAgentMessage(
-                                    role: message["role"].ToString(),
-                                    content: new[] { new KnowledgeAgentMessageTextContent(message["content"].ToString()) }))
-                                .ToList()
-                            )
-                        {
-                            TargetIndexParams = { new KnowledgeAgentIndexParams { IndexName = indexName, RerankerThreshold = 2.5f } }
-                        }
-                    );
+                        messages: messages
+                            .Where(message => message["role"].ToString() != "system")
+                            .Select(message => new KnowledgeAgentMessage(
+                                role: message["role"].ToString(),
+                                content: new[] { new KnowledgeAgentMessageTextContent(message["content"].ToString()) }))
+                            .ToList()
+                    )
+                    {
+                        TargetIndexParams = { new KnowledgeAgentIndexParams { IndexName = indexName, RerankerThreshold = 2.5f } }
+                    }
+                );
     
                 messages.Add(new Dictionary<string, object>
                 {
@@ -400,29 +410,27 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
                         new JsonSerializerOptions { WriteIndented = true }
                     );
                     Console.WriteLine(referenceJson2);
-                }            List<ChatMessage> chatMessages2 = messages
+                }
+    
+                List<ChatMessage> chatMessages2 = messages
                     .Select<Dictionary<string, object>, ChatMessage>(m => m["role"].ToString() switch
                     {
                         "user" => new UserChatMessage(m["content"].ToString()),
                         "assistant" => new AssistantChatMessage(m["content"].ToString()),
                         "system" => new SystemChatMessage(m["content"].ToString()),
                         _ => null
-                    })
+                    })                
                     .Where(m => m != null)
                     .ToList();
     
-    
                 var result2 = await chatClient.CompleteChatAsync(chatMessages2);
-    
                 Console.WriteLine($"[ASSISTANT]: {result2.Value.Content[0].Text.Replace(".", "\n")}");
     
                 await indexClient.DeleteKnowledgeAgentAsync(agentName);
                 System.Console.WriteLine($"Search agent '{agentName}' deleted successfully");
     
-                await indexClient.DeleteIndexAsync(indexName);
+                await indexClient.DeleteIndexAsync(indexName);            
                 System.Console.WriteLine($"Index '{indexName}' deleted successfully");
-    
-    
             }
         }
     }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# におけるエージェント検索のクイックスタートガイドの更新"
}
```

### Explanation
この変更は、C# によるエージェント検索のクイックスタートガイドの内容を大幅に更新したものです。主な変更点としては、Azure OpenAI クライアントライブラリのバージョンの修正、コード内のコメントの改善、およびコーディングスタイルの一貫性が挙げられます。

具体的には、以下のような更新が行われました：
- Azure OpenAI のクライアントライブラリのリンクが修正され、新しいバージョン `2.1.0` に変更されました。
- コードブロックのインデントや整形が行われ、可読性が向上しました。例えば、クラスとメソッドのブロックの開始、終了の位置を整えています。
- いくつかのコメントがより詳細になり、コードの意図が明確に示されています（例えば、インデックスクライアントの作成時のコメントがより明確になりました）。
- エラー処理に関するコードの微調整や、メッセージ生成のロジックが簡略化されて、最適化された形に変更されました。

この変更により、クイックスタートガイドは、初心者でも理解しやすい形式で API 使用法を示すと共に、実際の使用シナリオに基づいた具体的なコード例が提供されています。これにより、開発者はより効率的にクイックスタートを利用できるようになります。

## articles/search/search-create-app-portal.md{#item-19ab44}

<details>
<summary>Diff</summary>
````diff
@@ -53,7 +53,7 @@ When the index is ready to use, move on to the next step.
 
 The wizard provides a basic layout for rendered search results that includes space for a thumbnail image, a title, and description. Backing each of these elements is a field in your index that provides the data.
 
-1. Skip **Thumbnail** because this index doesn't have images, but if you have an index field that's populated with URLs resolving to publically available images, you should specify that field for the thumbnail area. If your index doesn't have image URLs, leave this field blank.
+1. Skip **Thumbnail** because this index doesn't have images, but if you have an index field that's populated with URLs resolving to publicly available images, you should specify that field for the thumbnail area. If your index doesn't have image URLs, leave this field blank.
 
 1. In Title, choose a field that conveys the uniqueness of each document. In this sample, the Hotel Name is a reasonable selection.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アプリポータル作成ガイドの誤字修正"
}
```

### Explanation
この変更は、アプリポータルを作成するガイドにおいて、サンプルテキスト内の誤字を修正するものです。具体的には、`"publically available images"`というフレーズが`"publicly available images"`に訂正されました。この現象は、一般的な英語の文法ミスであり、正しい単語は「publicly」です。

この修正により、テキストの正確性が向上し、ユーザーがコンテンツをより適切に理解できるようになります。他の部分は変更されておらず、全体の流れや説明はそのまま維持されています。このような誤字の訂正は、ドキュメントの信頼性を高めるために重要です。

## articles/search/search-get-started-agentic-retrieval.md{#item-4a40f4}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ zone_pivot_groups: search-get-started-agentic-retrieval
 
 ::: zone pivot="programming-language-csharp"
 
-[!INCLUDE [Python quickstart](includes/quickstarts/agentic-retrieval-csharp.md)]
+[!INCLUDE [C# quickstart](includes/quickstarts/agentic-retrieval-csharp.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索のクイックスタートガイドの言語タグ修正"
}
```

### Explanation
この変更は、エージェント検索に関するクイックスタートガイドの言語タグを修正したものです。具体的には、Markdown ドキュメント内のリファレンスを示す部分が更新され、Python から C# に変更されました。

修正内容は以下の通りです：
- 元の記述 `[!INCLUDE [Python quickstart](includes/quickstarts/agentic-retrieval-csharp.md)]` が `[!INCLUDE [C# quickstart](includes/quickstarts/agentic-retrieval-csharp.md)]` に更新されました。

この修正により、ユーザーに正しいプログラミング言語の導入ガイドを提供することが可能になり、ドキュメントの正確性が向上します。これにより、C# を使用する開発者が適切なリソースにアクセスできるようになります。


