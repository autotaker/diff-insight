---
date: '2026-04-29'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6f9c768...MicrosoftDocs:8ee4114
summary: |-
  このコードの変更により、検索インデックスに新しいフィルタリング機能が追加されました。主な新機能として、ODataフィルタを利用して検索結果を特定のドキュメントやフィールドに効果的に絞り込むことが可能になりました。また、フィルタ式を`filterAddOn`パラメータを通じて指定できるようになり、メタデータ、日付範囲、数値範囲、テキストマッチング、論理演算子などの多様なフィルタリングオプションが提供されています。

  ユーザーはこの新機能を活用することで、より関連性の高い検索結果を迅速かつ正確に得ることができるようになります。新しいフィルタリング機能は、情報取得の効率を向上させることを目的としており、直感的なフィルタ構文や具体的な実装例が提供されています。これにより、さまざまな開発環境でフィルタリング機能を容易に導入できることが期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6f9c768...MicrosoftDocs:8ee4114){target="_blank"}

# ハイライト
このコードの変更により、検索インデックスでのクエリ時に新しいフィルタリング機能が追加されました。主な新機能として、ODataフィルタを使用して検索結果を特定のドキュメントやフィールドに絞り込むことが可能になっています。

## 新機能
- ODataフィルタを利用した検索インデックス内の詳細なフィルタリング。
- `filterAddOn`パラメータを通じたフィルタ式の指定。
- 様々なフィルタリングオプションの提供（メタデータ、日付範囲、数値範囲、テキストマッチング、論理演算子）。

## ブレークチェンジ
- 特に記載なし。

## その他の更新
- フィルタの構文と使用例に関する新しいセクションを追加。
- C#、Python、REST APIでの具体的なフィルタリングの例を提供。

# インサイト
検索インデックスにおける新しいフィルタリング機能の追加は、ユーザーがより関連性の高い検索結果を迅速かつ正確に得るための大きな改善です。この変更の目的は、ユーザーが検索クエリをより詳細かつ特定の条件で絞り込むことを可能にし、これにより情報取得の効率を上げることにあります。

ODataフィルタの導入により、柔軟で強力な検索機能が実現されました。ユーザーは`filterAddOn`パラメータを使用してフィルタを指定でき、様々な条件でクエリを絞ることができます。これにより、単にキーワード検索するのではなく、具体的なフィールドやドキュメントに基づいて検索プロセスを改善できます。

また、提供されているフィルタの構文や例は、ユーザーが直感的にどのようにフィルタを活用できるかを示しており、プログラム言語に合わせた実装例としてのC#、Python、REST APIの具体的な例も、より幅広いユーザーがこの機能を利用可能にするものです。これにより、様々な開発環境での導入が容易になり、検索機能の普及を促進することが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-retrieve.md](#item-d739cf) | new feature | 検索インデックスでのクエリ時のフィルタリング機能の追加 | modified | 200 | 0 | 200 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-retrieve.md{#item-d739cf}

<details>
<summary>Diff</summary>
````diff
@@ -193,6 +193,206 @@ Authorization: Bearer {{accessToken}}
 
 :::zone-end
 
+## Filter at query time (Search index)
+
+When retrieving from a search index knowledge source, you can apply an [OData filter](search-query-odata-filter.md) at query time to narrow the results to specific documents or fields. The filter expression uses OData syntax and is passed via the `filterAddOn` parameter.
+
+### Filter syntax and examples
+
+The `filterAddOn` parameter accepts OData filter expressions. Example patterns include:
+
+- **Metadata fields**: `city eq 'Phoenix'`, `status eq 'active'`
+- **Date ranges**: `publishDate ge 2024-01-01 and publishDate le 2024-12-31`
+- **Numeric ranges**: `price ge 100 and price le 5000`
+- **Text matching**: `substringof('climate', description)`, `indexof(title, 'urgent') ge 0`
+- **Logical operators**: `(category eq 'News' or category eq 'Analysis') and status eq 'published'`
+
+**Example filter expressions:**
+
+- `status eq 'published'`
+- `created ge 2025-01-01`
+- `city eq 'Redmond' and department eq 'Engineering'`
+- `(priority eq 'High' or priority eq 'Critical') and resolved eq false`
+
+### Examples by language
+
+:::zone pivot="csharp"
+
+```csharp
+using Azure.Identity;
+using Azure.Search.Documents.KnowledgeBases;
+using Azure.Search.Documents.KnowledgeBases.Models;
+
+var kbClient = new KnowledgeBaseRetrievalClient(
+    endpoint: new Uri("<YOUR SEARCH SERVICE URL>"),
+    knowledgeBaseName: "<YOUR KNOWLEDGE BASE NAME>",
+    tokenCredential: new DefaultAzureCredential()
+);
+
+var retrievalRequest = new KnowledgeBaseRetrievalRequest();
+
+retrievalRequest.Messages.Add(
+    new KnowledgeBaseMessage(
+        content: new[] {
+            new KnowledgeBaseMessageTextContent(
+                "You are a support agent. Answer questions based on published documentation. "
+                + "If you don't know the answer, say so."
+            )
+        }
+    ) { Role = "assistant" }
+);
+
+retrievalRequest.Messages.Add(
+    new KnowledgeBaseMessage(
+        content: new[] {
+            new KnowledgeBaseMessageTextContent(
+                "What is the process for submitting an expense report?"
+            )
+        }
+    ) { Role = "user" }
+);
+
+// Apply a filter to search only published documents
+var searchIndexParams = new SearchIndexKnowledgeSourceParams(
+    knowledgeSourceName: "internal-documentation-ks"
+);
+searchIndexParams.FilterAddOn = "status eq 'published'";
+
+retrievalRequest.KnowledgeSourceParams.Add(searchIndexParams);
+
+var result = await kbClient.RetrieveAsync(retrievalRequest);
+Console.WriteLine(
+    (result.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text
+);
+```
+
+:::zone-end
+
+:::zone pivot="python"
+
+```python
+from azure.identity import DefaultAzureCredential
+from azure.search.documents.knowledgebases import KnowledgeBaseRetrievalClient
+from azure.search.documents.knowledgebases.models import (
+    KnowledgeBaseMessage,
+    KnowledgeBaseMessageTextContent,
+    KnowledgeBaseRetrievalRequest,
+    SearchIndexKnowledgeSourceParams,
+)
+
+kb_client = KnowledgeBaseRetrievalClient(
+    endpoint="<YOUR SEARCH SERVICE URL>",
+    knowledge_base_name="<YOUR KNOWLEDGE BASE NAME>",
+    credential=DefaultAzureCredential(),
+)
+
+request = KnowledgeBaseRetrievalRequest(
+    messages=[
+        KnowledgeBaseMessage(
+            role="assistant",
+            content=[
+                KnowledgeBaseMessageTextContent(
+                    text="You are a support agent. Answer questions based on published documentation. "
+                    "If you don't know the answer, say so."
+                )
+            ],
+        ),
+        KnowledgeBaseMessage(
+            role="user",
+            content=[
+                KnowledgeBaseMessageTextContent(
+                    text="What is the process for submitting an expense report?"
+                )
+            ],
+        ),
+    ],
+    knowledge_source_params=[
+        SearchIndexKnowledgeSourceParams(
+            knowledge_source_name="internal-documentation-ks",
+            # Apply a filter to search only published documents
+            filter_add_on="status eq 'published'",
+        )
+    ],
+)
+
+result = kb_client.retrieve(retrieval_request=request)
+print(result.response[0].content[0].text)
+```
+
+:::zone-end
+
+:::zone pivot="rest"
+
+```http
+POST https://<YOUR SEARCH SERVICE>.search.windows.net/knowledgebases/<YOUR KNOWLEDGE BASE NAME>/retrieve?api-version=2025-11-01-preview
+Content-Type: application/json
+Authorization: Bearer <YOUR ACCESS TOKEN>
+
+{
+    "messages": [
+        {
+            "role": "assistant",
+            "content": [
+                {
+                    "type": "text",
+                    "text": "You are a support agent. Answer questions based on published documentation. If you don't know the answer, say so."
+                }
+            ]
+        },
+        {
+            "role": "user",
+            "content": [
+                {
+                    "type": "text",
+                    "text": "What is the process for submitting an expense report?"
+                }
+            ]
+        }
+    ],
+    "knowledgeSourceParams": [
+        {
+            "knowledgeSourceName": "internal-documentation-ks",
+            "kind": "searchIndex",
+            "filterAddOn": "status eq 'published'"
+        }
+    ]
+}
+```
+
+:::zone-end
+
+### Multi-filter example
+
+You can combine multiple filters to refine results further:
+
+:::zone pivot="csharp"
+
+```csharp
+searchIndexParams.FilterAddOn = "(status eq 'published' or status eq 'internal') and created ge 2025-01-01";
+```
+
+:::zone-end
+
+:::zone pivot="python"
+
+```python
+filter_add_on="(status eq 'published' or status eq 'internal') and created ge 2025-01-01"
+```
+
+:::zone-end
+
+:::zone pivot="rest"
+
+```json
+{
+    "knowledgeSourceName": "internal-documentation-ks",
+    "kind": "searchIndex",
+    "filterAddOn": "(status eq 'published' or status eq 'internal') and created ge 2025-01-01"
+}
+```
+
+:::zone-end
+
 ### Request parameters
 
 Pass the following parameters to call the retrieve action.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "検索インデックスでのクエリ時のフィルタリング機能の追加"
}
```

### Explanation
この変更は、検索インデックスから情報を取得する際に使用できる新しいフィルタリング機能を追加するものです。具体的には、ODataフィルタを使用して検索結果を特定のドキュメントやフィールドに絞り込むことが可能になりました。ユーザーは、`filterAddOn`パラメータを介してフィルター式を指定でき、これによりより具体的で関連性の高い検索結果を取得できます。

新しいセクションでは、フィルタの構文とその使用例が詳しく説明されており、メタデータフィールド、日付範囲、数値範囲、テキストマッチング、論理演算子など、様々なフィルタリングオプションが提供されています。また、C#、Python、REST APIの各言語での具体的なフィルタリングの例も示されており、ユーザーは自身のニーズに応じたフィルタを簡単に実装できるようになっています。この変更により、ユーザーは検索機能をより強力に活用できるようになります。


