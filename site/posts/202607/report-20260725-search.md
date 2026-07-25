---
date: '2026-07-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2b2f71f...MicrosoftDocs:7f76ef9
summary: この変更は、Azure AI SearchのMCPエンドポイントの認証方法の更新、ナビゲーショントピック名とリンクの修正、画像の更新および削除、SharePoint
  Onlineのインデックス作成手順の具体化を含んでいます。具体的には、C#およびPythonにおける認証方法のコード例が追加され、ナビゲーションが整理され、インデックス作成手順が最新情報に基づいて更新されています。さらに、不要な画像が削除され、視覚情報や権限設定の手順が刷新されました。今回の変更は、ユーザビリティやセキュリティの向上を目指しており、開発者やエンドユーザーにとってより効率的で安全な体験を提供します。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2b2f71f...MicrosoftDocs:7f76ef9){target="_blank"}

<format>
# Highlights
この変更は、Azure AI SearchのMCPエンドポイントの認証方法の更新、ナビゲーショントピック名とリンクの修正、いくつかの画像の更新および削除、そしてSharePoint Onlineインデックス作成手順の具体化を含むものでした。

## New features
- Azure AI SearchのMCPエンドポイントにおける認証方法について、C#およびPythonでのコード例が追加された。
- ナビゲーションが整理され、トピック名とリンクが明確化された。
- SharePoint Onlineのインデックス作成手順が最新の情報に基づいて更新された。

## Breaking changes
- `aad-app-authentication-configuration.png`という画像が削除されたが、具体的なドキュメント上の動作に影響する変更はなし。

## Other updates
- 画像ファイルの改訂により、視覚情報や権限設定の手順が刷新された。
- 不要または古くなった画像とその関連情報が整理された。

# Insights
今回の変更は、主にAzure AI SearchのMCPエンドポイントの認証に関連する更新と、SharePoint Onlineのインデックス作成手順の改善に焦点を当てています。まず、MCPエンドポイントに関しては、認証方法の明確化が行われており、ベアラートークンの使用が推奨される点と、セキュリティに関する注意事項が強調されています。この更新は、セキュリティを強化し、開発者が正確にAPIを利用できるよう支援するものです。

トピックナビゲーションの変更では、「Search」という一般的な名称を「Azure AI Search」に変更することで、ユーザーの混乱を避ける狙いが感じられます。また、ナビゲーションリンクが整理されており、これによって関連情報の検索がより直感的になっています。

画像の更新では、API権限の手続きに関する画像の内容が最新情報に基づいてアップデートされているため、視覚的な情報伝達が効果的に行われます。これにより、ユーザーは権限設定に関する具体的なイメージを持ちやすくなり、インデックス作成手順の理解が促進されます。

SharePoint Onlineのインデックス作成手順は、最新の日付と、ユーザーインターフェースの変更に基づく詳しい操作ガイドに刷新されています。このことで、ユーザーが手順をスムーズに進められるだけでなく、権限付与の必要性についての理解も深まります。

全体として、これらの変更はAzure AI Searchとその応用におけるユーザビリティの向上を図っており、開発者およびエンドユーザーに対してより安全で効率的な体験を提供するものと評価できます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-retrieve.md](#item-d739cf) | minor update | エンドポイントの認証方法の更新 | modified | 205 | 12 | 217 | 
| [toc.yml](#item-eeb848) | minor update | トピック名とリンクの更新 | modified | 8 | 15 | 23 | 
| [aad-app-authentication-configuration.png](#item-56d8b1) | minor update | 画像ファイルの削除 | removed | 0 | 0 | 0 | 
| [application-api-permissions.png](#item-8199de) | minor update | 画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [delegated-api-permissions.png](#item-9ba39b) | minor update | 画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [search-how-to-index-sharepoint-online.md](#item-8c099c) | minor update | SharePoint Onlineインデックス作成手順の更新 | modified | 29 | 20 | 49 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-retrieve.md{#item-d739cf}

<details>
<summary>Diff</summary>
````diff
@@ -41,6 +41,12 @@ To set up a pipeline that connects Azure AI Search to Foundry Agent Service via
 
 ::: zone pivot="csharp"
 
++ If you [call the MCP endpoint through the Azure OpenAI Responses API](#authenticate-to-the-mcp-endpoint), you need:
+
+  + A deployed LLM and the **Cognitive Services OpenAI User** role (or an API key) on the Foundry resource. You can reuse the LLM and resource specified in your knowledge base, if applicable.
+
+  + The [`Azure.AI.OpenAI`](https://www.nuget.org/packages/Azure.AI.OpenAI) and [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) packages.
+
 + Required [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) package:
 
   + For 2026-05-01-preview features, the latest preview package: `dotnet add package Azure.Search.Documents --prerelease`
@@ -51,6 +57,12 @@ To set up a pipeline that connects Azure AI Search to Foundry Agent Service via
 
 ::: zone pivot="python"
 
++ If you [call the MCP endpoint through the Azure OpenAI Responses API](#authenticate-to-the-mcp-endpoint), you need:
+
+  + A deployed LLM and the **Cognitive Services OpenAI User** role (or an API key) on the Foundry resource. You can reuse the LLM and resource specified in your knowledge base, if applicable.
+
+  + The [`openai`](https://pypi.org/project/openai/) and [`azure-identity`](https://pypi.org/project/azure-identity/) packages.
+
 + Required [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) package:
 
   + For 2026-05-01-preview features, the latest preview package: `pip install --pre azure-search-documents`
@@ -1744,30 +1756,211 @@ To avoid this behavior, index large source documents as smaller chunks with stab
 
 In Azure AI Search, each knowledge base is a standalone MCP server that exposes the `knowledge_base_retrieve` tool. Any MCP-compatible client, including [Foundry Agent Service](/azure/ai-foundry/agents/overview), [GitHub Copilot](https://github.com/features/copilot), [Claude](https://claude.ai), and [Cursor](https://cursor.com), can invoke this tool to query the knowledge base.
 
-### MCP endpoint format
+### Authenticate to the MCP endpoint
 
-Each knowledge base has an MCP endpoint at the following URL.
+Each knowledge base has an MCP endpoint at the following URL:
 
 ```
-https://<your-service-name>.search.windows.net/knowledgebases/<your-knowledge-base-name>/mcp?api-version=<api-version>
+https://<your-search-service>.search.windows.net/knowledgebases/<your-knowledge-base>/mcp?api-version=<api-version>
 ```
 
 The API version you specify determines what the connection returns. With `2026-05-01-preview`, the knowledge base can return synthesized answers when the underlying knowledge base is configured with an LLM and a compatible reasoning effort. With `2026-04-01`, retrieval is always minimal and extractive, and the connection returns grounding data only.
 
-### Authenticate to the MCP endpoint
+How you authenticate to this endpoint depends on your MCP client. When you use the Azure OpenAI Responses API with the `knowledge_base_retrieve` MCP tool, you authenticate both the Responses API call to Azure OpenAI and the MCP request to Azure AI Search. If your MCP client calls this endpoint directly, you authenticate only to Azure AI Search.
+
+For Azure AI Search authentication, use one of the following methods:
+
++ [Pass a bearer token](#use-a-bearer-token-for-mcp-authentication) in the `Authorization` header (recommended)
++ [Pass an admin key](#use-an-admin-key-for-mcp-authentication) in the `api-key` header
+
+> [!NOTE]
+> MCP clients configure custom headers differently. For example, [Foundry Agent Service](/azure/ai-foundry/agents/how-to/foundry-iq-connect) injects headers through project connections, while clients such as [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp) require headers in MCP server JSON.
+
+### Use a bearer token for MCP authentication
+
+The recommended method for MCP authentication is a bearer token, which avoids storing sensitive keys in configuration files. The identity behind the token must have the **Search Index Data Reader** role assigned on the search service. For more information, see [Connect your app to Azure AI Search using identities](search-security-rbac-client-code.md).
+
+:::zone pivot="csharp"
+
+```csharp
+#pragma warning disable OPENAI001
+
+using Azure.AI.OpenAI;
+using Azure.Core;
+using Azure.Identity;
+using OpenAI.Responses;
+using System;
+using System.Collections.Generic;
+
+string openAiEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")!; // Example: https://<your-resource-name>.openai.azure.com
+string mcpServerUrl = Environment.GetEnvironmentVariable("AZURE_SEARCH_MCP_ENDPOINT")!; // Example: https://<your-search-service>.search.windows.net/knowledgebases/<your-knowledge-base>/mcp?api-version=<api-version>
+DefaultAzureCredential credential = new();
+
+// Create the Azure OpenAI Responses client
+AzureOpenAIClient azureClient = new(new Uri(openAiEndpoint), credential);
+ResponsesClient openAIClient = azureClient.GetResponsesClient();
+
+// Get a bearer token for Azure AI Search
+string searchToken = credential.GetToken(
+    new TokenRequestContext(new[] { "https://search.azure.com/.default" })
+).Token;
+
+// Configure the MCP tool for knowledge base retrieval
+McpTool mcpTool = ResponseTool.CreateMcpTool(
+    serverLabel: "search_kb",
+    serverUri: new Uri(mcpServerUrl),
+    headers: new Dictionary<string, string>
+    {
+        ["Authorization"] = $"Bearer {searchToken}",
+    },
+    allowedTools: new McpToolFilter { ToolNames = { "knowledge_base_retrieve" } },
+    toolCallApprovalPolicy: new McpToolCallApprovalPolicy(
+        GlobalMcpToolCallApprovalPolicy.NeverRequireApproval)
+);
+
+// Build the response request with the MCP tool attached
+CreateResponseOptions options = new()
+{
+    Model = "MODEL_NAME",
+    InputItems =
+    {
+        ResponseItem.CreateUserMessageItem(
+            "What causes the strongest nighttime brightness patterns in this dataset?")
+    },
+    Tools = { mcpTool }
+};
+
+ResponseResult response = await openAIClient.CreateResponseAsync(options);
+Console.WriteLine(response.GetOutputText());
+```
+
+**Reference:** [Use the Azure OpenAI Responses API](/azure/foundry/openai/how-to/responses?tabs=csharp#authentication)
+
+:::zone-end
+
+:::zone pivot="python"
+
+```python
+import os
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+from openai import AzureOpenAI
+
+openai_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"] # Example: https://<your-resource-name>.openai.azure.com
+mcp_server_url = os.environ["AZURE_SEARCH_MCP_ENDPOINT"] # Example: https://<your-search-service>.search.windows.net/knowledgebases/<your-knowledge-base>/mcp?api-version=<api-version>
+credential = DefaultAzureCredential()
+
+# Create token providers for Azure OpenAI and Azure AI Search
+openai_token_provider = get_bearer_token_provider(
+    credential, "https://cognitiveservices.azure.com/.default"
+)
+search_token_provider = get_bearer_token_provider(
+    credential, "https://search.azure.com/.default"
+)
+
+# Create the Azure OpenAI client
+client = AzureOpenAI(
+    azure_endpoint=openai_endpoint,
+    azure_ad_token_provider=openai_token_provider,
+    api_version=os.environ["OPENAI_API_VERSION"], # Example: 2025-04-01-preview
+)
+
+# Create a response using the MCP tool configuration
+response = client.responses.create(
+    model="MODEL_NAME",
+    input="What causes the strongest nighttime brightness patterns in this dataset?",
+    tools=[
+        {
+            "type": "mcp",
+            "server_label": "search_kb",
+            "server_url": mcp_server_url,
+            "allowed_tools": ["knowledge_base_retrieve"],
+            "headers": {
+                "Authorization": f"Bearer {search_token_provider()}"
+            },
+            "require_approval": "never",
+        }
+    ],
+)
+
+print(response.output_text)
+```
+
+**Reference:** [Use the Azure OpenAI Responses API](/azure/foundry/openai/how-to/responses?tabs=python#authentication)
+
+:::zone-end
+
+:::zone pivot="rest"
+
+```http
+// This code snippet is currently unavailable.
+```
 
-The MCP endpoint requires authentication through custom headers. You have two options:
+:::zone-end
 
-+ **(Recommended)** Pass a bearer token in the `Authorization` header. The identity behind the token must have the **Search Index Data Reader** role assigned on the search service. This approach avoids storing keys in configuration files. For more information, see [Connect your app to Azure AI Search using identities](search-security-rbac-client-code.md).
+### Use an admin key for MCP authentication
 
-+ Pass an admin key in the `api-key` header. An admin key provides full read-write access to the search service, so use it with caution. For more information, see [Connect to Azure AI Search using API keys](search-security-api-keys.md).
+An admin key grants full read-write access to the search service, so use it only in development environments or when a bearer token isn't available. For more information, see [Connect to Azure AI Search using API keys](search-security-api-keys.md).
 
 > [!TIP]
-> Each MCP client configures custom headers differently. For example:
->
-> + In [Foundry Agent Service](/azure/ai-foundry/agents/how-to/foundry-iq-connect), you configure authentication through a project connection and add the MCP tool to an agent. The service automatically injects the required headers on MCP requests.
->
-> + In [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp) and similar clients, you configure headers in the MCP server JSON, such as `mcp.json`.
+> The following example shows only the header that differs from the bearer token example. For the full setup, see [Use a bearer token for MCP authentication](#use-a-bearer-token-for-mcp-authentication).
+
+:::zone pivot="csharp"
+
+```csharp
+#pragma warning disable OPENAI001
+
+using OpenAI.Responses;
+using System;
+using System.Collections.Generic;
+
+string mcpServerUrl = Environment.GetEnvironmentVariable("AZURE_SEARCH_MCP_ENDPOINT")!; // Example: https://<your-search-service>.search.windows.net/knowledgebases/<your-knowledge-base>/mcp?api-version=<api-version>
+string searchAdminKey = Environment.GetEnvironmentVariable("AZURE_SEARCH_ADMIN_KEY")!; // Example: <your-search-admin-key>
+
+McpTool mcpTool = ResponseTool.CreateMcpTool(
+    serverLabel: "search_kb",
+    serverUri: new Uri(mcpServerUrl),
+    headers: new Dictionary<string, string> { ["api-key"] = searchAdminKey },
+    allowedTools: new McpToolFilter { ToolNames = { "knowledge_base_retrieve" } },
+    toolCallApprovalPolicy: new McpToolCallApprovalPolicy(
+        GlobalMcpToolCallApprovalPolicy.NeverRequireApproval)
+);
+```
+
+**Reference:** [Use the Azure OpenAI Responses API](/azure/foundry/openai/how-to/responses?tabs=csharp#authentication)
+
+:::zone-end
+
+:::zone pivot="python"
+
+```python
+import os
+
+mcp_server_url = os.environ["AZURE_SEARCH_MCP_ENDPOINT"] # Example: https://<your-search-service>.search.windows.net/knowledgebases/<your-knowledge-base>/mcp?api-version=<api-version>
+search_admin_key = os.environ["AZURE_SEARCH_ADMIN_KEY"] # Example: <your-search-admin-key>
+
+tools = [
+    {
+        "type": "mcp",
+        "server_label": "search_kb",
+        "server_url": mcp_server_url,
+        "allowed_tools": ["knowledge_base_retrieve"],
+        "headers": {"api-key": search_admin_key},
+        "require_approval": "never",
+    }
+]
+```
+
+**Reference:** [Use the Azure OpenAI Responses API](/azure/foundry/openai/how-to/responses?tabs=python#authentication)
+
+:::zone-end
+
+:::zone pivot="rest"
+
+```http
+// This code snippet is currently unavailable.
+```
+
+:::zone-end
 
 ## Review the MCP response
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンドポイントの認証方法の更新"
}
```

### Explanation
この変更は、Azure AI SearchのMCPエンドポイントにおける認証方法を更新する内容です。主にコード内のドキュメンテーションを改訂し、Azure OpenAI Responses APIを利用する際の必要条件について詳しく説明しています。

具体的には、認証に必要な要素（デプロイされたLLMと役割、必要なNuGetパッケージなど）が追加され、C#およびPythonのコードスニペットが新たに含まれています。また、MCPクライアントからのエンドポイントへのアクセス方法に関する注意事項も強調されています。変更点には以下が含まれます：

1. **認証要件の明確化**: Azure OpenAI Responses APIを介してMCPエンドポイントを呼び出すための要件が追加されました。具体的には、デプロイされた大規模言語モデル（LLM）や必要な役割が記述されています。
   
2. **コード例の追加**: C#およびPythonでのコード例が含まれ、MCPエンドポイントにアクセスする際の実装方法が具体的に示されています。これは、開発者が実際に利用する際の手助けとなります。

3. **セキュリティと認証方法の推奨**: ベアラートークンを使用した認証の推奨と、APIキーを使用する場合の注意点が記述され、ユーザーに対するガイダンスが強化されました。

これらの変更により、Azure AI Searchを利用する開発者にとって、MCPエンドポイントとのインタラクションがより明確で安全なものとなります。

## articles/search/breadcrumb/toc.yml{#item-eeb848}

<details>
<summary>Diff</summary>
````diff
@@ -3,23 +3,16 @@ items:
   tocHref: /azure/
   topicHref: /azure/index
   items:
-  - name: Search
+  - name: Azure AI Search
+    tocHref: /azure/search/             # show this crumb on pages whose URL starts with this tocHref
+    topicHref: /azure/search/index      # page that opens when you select this crumb
+  - name: Azure AI Search
     tocHref: /azure/reliability
-  - name: Foundry Tools
-    tocHref: /azure/ai-services/
-    topicHref: /azure/ai-services/index
-    items:
-    - name: Azure AI Search
-      tocHref: /azure/search/
-      topicHref: /azure/search/index
+    topicHref: /azure/search/index
 - name: Azure
   tocHref: /legal/
   topicHref: /azure/index
   items:
-  - name: Foundry Tools                # Original doc set name
-    tocHref: /legal/cognitive-services/    # Destination doc set route
-    topicHref: /azure/ai-services/index    # Original doc set route
-    items:
-    - name: Azure AI Search                  # Original doc set name
-      tocHref: /legal/search/    # Destination doc set route
-      topicHref: /azure/search/index      # Original doc set route
+  - name: Azure AI Search
+    tocHref: /legal/search/
+    topicHref: /azure/search/index 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピック名とリンクの更新"
}
```

### Explanation
この変更は、`toc.yml`ファイルにおけるトピック名と関連リンクの更新に関するものです。具体的には、Azure AI Searchのセクションに対して、名称やリンクの修正が行われました。変更点の概要は以下のとおりです。

1. **トピック名の明確化**: 「Search」という元の名称が「Azure AI Search」に変更され、トピックがより具体的でわかりやすくなっています。

2. **ナビゲーションの整理**: Azure AI Searchに関連するリンク（`tocHref`および`topicHref`）が更新され、それに応じて新しい階層が整理されました。特に、ナビゲーションの整理により、関連する情報にアクセスしやすくなっています。この変更により、ユーザーは文書のナビゲーション時に発見しやすくなるでしょう。

3. **不要なエントリの削除**: 「Foundry Tools」とその関連ドキュメントのエントリが削除され、新しい構造に不要な情報が省かれています。これにより、ユーザーが利用する際に混乱を避け、情報の一貫性が保たれています。

このように、全体として、変更はトピックの明確化とナビゲーションの効率化を目指したものであり、ユーザー体験の向上に寄与しています。

## articles/search/media/search-howto-index-sharepoint-online/aad-app-authentication-configuration.png{#item-56d8b1}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの削除"
}
```

### Explanation
この変更は、`aad-app-authentication-configuration.png`という画像ファイルが削除されたことに関するものです。この画像は、Azure AI SearchでSharePoint Onlineをインデックスする手順に関連していた可能性があります。

削除の理由として考えられるのは、以下の点です：

1. **内容の更新または置き換え**: 画像が古くなったため、新しい画像や異なる形式の資料に置き換えられた可能性があります。

2. **ドキュメントの整理**: 不要な画像や情報の整理の一環として、この画像が削除された可能性があります。これにより、ドキュメントがより明確で一貫性のあるものになることが期待されます。

3. **情報の集中化**: 画像が不必要になった、または別の部分で同様の情報が提供されている場合、その重複を避けるために削除された可能性があります。

この削除により、ユーザーはより正確で整理された情報にアクセスできるようになります。全体として、この変更はドキュメントの品質向上につながるものと考えられます。

## articles/search/media/search-howto-index-sharepoint-online/application-api-permissions.png{#item-8199de}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの更新"
}
```

### Explanation
この変更は、`application-api-permissions.png`という画像ファイルが修正されたことに関するものです。この画像は、Azure AI SearchにおけるSharePoint Onlineのインデックス作成手順に関連している可能性があります。

変更の詳細は以下のとおりです：

1. **画像の内容の更新**: この画像内の情報が最新のAPI権限設定や手順に適応するように更新された可能性があります。これにより、ユーザーは新しいインターフェースや要件に合った、正確な情報を得ることができます。

2. **視覚的クオリティの向上**: 画像の解像度やデザインが向上している可能性があり、これによりユーザーの理解が容易になることが期待されます。

3. **整合性の確保**: 他の関連するドキュメントや画像とも整合性を持たせるために、内容やスタイルが調整されたことが考えられます。

この変更により、ユーザーはより効果的に必要な情報にアクセスでき、SharePoint Onlineのインデックス作成の理解が深まることでしょう。全体として、画像の改善はドキュメントの全体的な品質を向上させるものと考えられます。

## articles/search/media/search-howto-index-sharepoint-online/delegated-api-permissions.png{#item-9ba39b}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの更新"
}
```

### Explanation
この変更は、`delegated-api-permissions.png`という画像ファイルが修正されたことに関連しています。この画像は、SharePoint Onlineのインデックス作成における委任API権限の設定に関するものです。

変更の内容として考えられるのは以下の点です：

1. **内容の新規性**: 画像内の情報が最新の権限設定や手順に沿うよう更新され、ユーザーが正確なプロセスを理解できるようになっています。

2. **視覚的改善**: 画像のデザインや解像度が改善され、より明確で理解しやすいものになった可能性があります。これにより、視覚的な情報の伝達が効果的になります。

3. **ドキュメントの一貫性**: 他のコレポンディング画像や関連ドキュメントと整合性を持たせるために、スタイルや内容が調整されたかもしれません。

この変更により、ユーザーは委任API権限の設定プロセスをより容易に理解できるようになり、SharePoint Onlineのインデックス作成に関する知識が深まることが期待されます。全体として、画像の改良は、ドキュメントの品質とユーザーエクスペリエンスを向上させるものと考えられます。

## articles/search/search-how-to-index-sharepoint-online.md{#item-8c099c}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Set up a SharePoint in Microsoft 365 indexer to automate indexing o
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/07/2026
+ms.date: 07/23/2026
 ai-usage: ai-assisted
 ms.custom:
   - ignite-2025
@@ -148,48 +148,57 @@ The SharePoint in Microsoft 365 indexer uses a Microsoft Entra application for a
 
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
-1. Search for or navigate to **Microsoft Entra ID**, and then select **Add** > **App registration**. 
+1. Search for or navigate to **Microsoft Entra ID**.
+
+1. On the **Overview** page, select **+ Add** > **App registration**.
 
-1. Select **+ New registration**:
     1. Enter a name for your app.
-    1. Select **Single tenant**.
-    1. Skip the URI designation step. No redirect URI required.
+    1. Select **Single tenant only - *tenant name***.
+    1. Skip the URI designation step. No redirect URI is required.
     1. Select **Register**.
 
-1. On the navigation pane under **Manage**, select **API permissions**, and then **Add a permission**. Select **Microsoft Graph**.
+1. From the left pane, select **Manage** > **API permissions**.
+
+1. Select **+ Add a permission**, and then select **Microsoft Graph**.
+
+    + If your indexer uses application API permissions, select **Application permissions**.
 
-    + If your indexer uses application API permissions, choose **Application** permissions.
-      - For standard indexing, select:
-        - `Files.Read.All`
-        - `Sites.Read.All`
+      + For standard indexing, select:
+
+        + `Files.Read.All`
+        + `Sites.Read.All`
         
         :::image type="content" source="media/search-howto-index-sharepoint-online/application-api-permissions.png" alt-text="Screenshot of application API permissions." lightbox="media/search-howto-index-sharepoint-online/application-api-permissions.png":::
 
-      - If you're enabling [ACL ingestion (preview)](search-indexer-sharepoint-access-control-lists.md), the required permissions depend on which item types (document library files, list items, ASPX pages) and group types (Microsoft Entra vs. SharePoint site groups) you index. See [Permissions by ACL scenario](search-indexer-sharepoint-access-control-lists.md#permissions-by-acl-scenario) before completing this step. For the cross-scenario summary, see [Choose your permissions setup](#choose-your-permissions-setup).
+      + If you're enabling [ACL ingestion (preview)](search-indexer-sharepoint-access-control-lists.md), the required permissions depend on which item types (document library files, list items, ASPX pages) and group types (Microsoft Entra vs. SharePoint site groups) you index. Before you complete this step, see [Permissions by ACL scenario](search-indexer-sharepoint-access-control-lists.md#permissions-by-acl-scenario). For the cross-scenario summary, see [Choose your permissions setup](#choose-your-permissions-setup).
 
-          Using application permissions means that the indexer accesses the SharePoint site in a service context. So when you run the indexer, it has access to all content in the SharePoint tenant, which requires tenant admin approval. A client secret or secretless configuration is also required for authentication. Setting up the authentication mechanism is described later in this article under [authentication modes for application API permissions only](#available-authentication-methods-for-application-api-permissions-only).
+        Using application permissions means the indexer accesses the SharePoint site in a service context. Therefore, when you run the indexer, it has access to all content in the SharePoint tenant, which requires tenant admin approval. A client secret or secretless configuration is also required for authentication. Setting up the authentication mechanism is described later in this article under [Available authentication methods for application API permissions only](#available-authentication-methods-for-application-api-permissions-only).
 
-    + If the indexer uses delegated API permissions, select **Delegated permissions** and then select `Delegated - Files.Read.All`, `Delegated - Sites.Read.All`, and `Delegated - User.Read`.
+    + If your indexer uses delegated API permissions, select **Delegated permissions**, and then select:
 
+      + `Files.Read.All`
+      + `Sites.Read.All`
+      + `User.Read`
 
       :::image type="content" source="media/search-howto-index-sharepoint-online/delegated-api-permissions.png" alt-text="Screenshot showing delegated API permissions." lightbox="media/search-howto-index-sharepoint-online/delegated-api-permissions.png":::
 
       Delegated permissions allow the search client to connect to SharePoint under the security identity of the current user.
 
-1. Give admin consent.
-
-    Tenant admin consent is required when using application API permissions. Some tenants are locked down in such a way that tenant admin consent is required for delegated API permissions as well. If either of these conditions apply, you need to have a tenant admin grant consent for this Microsoft Entra application before creating the indexer.
+1. Select **Grant admin consent for *tenant name***.
 
+    Tenant admin consent is required when using application API permissions. Some tenants are locked down in such a way that tenant admin consent is also required for delegated API permissions. If either condition applies, a tenant administrator must grant consent for this Microsoft Entra application before creating the indexer.
 
     :::image type="content" source="media/search-howto-index-sharepoint-online/aad-app-grant-admin-consent.png" alt-text="Screenshot showing Microsoft Entra app grant admin consent." lightbox="media/search-howto-index-sharepoint-online/aad-app-grant-admin-consent.png":::
 
-1. Select the **Authentication** tab.
+1. From the left pane, select **Manage** > **Authentication (Preview)**.
 
-1. Set **Allow public client flows** to **Yes**, and then select **Save**.
+1. On the **Redirect URI configuration** tab, select **+ Add Redirect URI**.
 
-1. Select **+ Add a platform**, and then **Mobile and desktop applications**. Check `https://login.microsoftonline.com/common/oauth2/nativeclient`, and then select **Configure**.
+    1. Select **Mobile and desktop applications**.
+    1. Select the `https://login.microsoftonline.com/common/oauth2/nativeclient` redirect URI.
+    1. Select **Configure**.
 
-    :::image type="content" source="media/search-howto-index-sharepoint-online/aad-app-authentication-configuration.png" alt-text="Screenshot showing Microsoft Entra app authentication configuration." lightbox="media/search-howto-index-sharepoint-online/aad-app-authentication-configuration.png" :::
+1. On the **Settings** tab, enable the **Allow public client flows** toggle, and then select **Save**.
 
 1. Configure the indexer [authentication method](#available-authentication-methods-for-application-api-permissions-only) according to your solution needs.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint Onlineインデックス作成手順の更新"
}
```

### Explanation
この変更は、`search-how-to-index-sharepoint-online.md`というMarkdownドキュメントに対するもので、主にSharePoint Onlineのインデックス作成に関する手順を更新しています。具体的には、29行が追加され、20行が削除された結果、全体で49行の変更が行われています。

変更内容は以下のように要約できます：

1. **日付の更新**: ドキュメントの日付が2026年7月7日から2026年7月23日に更新され、最新情報を反映しています。

2. **手順の明確化**: 手順が整理され、新しいサブスクリプションやメニュー項目の構造に合わせて操作内容が詳述されています。例えば、アプリケーションの登録手順において、UIの変更に基づいて指示が更新されています。

3. **API権限設定の具体化**: 「アプリケーション権限」や「委任された権限」の設定方法が明確に説明されており、どの権限を選択するかに関する具体的な情報が追加されています。

4. **視覚情報の追加**: 手順に関連する画像への参照が保持され、ユーザーが視覚的により理解しやすいように構成されています。

5. **権限付与の重要性についての注意喚起**: テナント管理者の同意が必要な条件についての説明が強調され、ユーザーが注意すべき点が明確になっています。

このような変更により、ユーザーはSharePoint Onlineにおけるインデックス作成の設定手順をよりスムーズに理解し実行できるようになるため、ドキュメント全体の品質が向上しています。全体的に、手順の更新はユーザーエクスペリエンスの向上につながる重要な改善と言えるでしょう。


