---
date: '2026-08-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4f575cb...MicrosoftDocs:6ad6704
summary: 今回の更新では、いくつかのドキュメントがマイナーアップデートされ、日付の更新や内容の明確化、新しい情報の追加が行われました。特に、Azure AI
  Search機能に関する情報が改善され、エージェントリトリーバルのパイプライン作成における設定強制機能やサーバーレスコスト最適化の新たな推奨策が追加されました。重大な破壊的変更は報告されていません。画像分析スキルやサーバーレス開発者層、無料試用アカウントに関する情報も整理され、全体的な可読性が向上しました。これにより、新規および既存のユーザーが機能をより理解しやすくなり、Azureサービスの利用促進が図られています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4f575cb...MicrosoftDocs:6ad6704){target="_blank"}

<format>
# Highlights
いくつかのドキュメントに対するマイナーアップデートが実施され、これにより日付の更新、内容の明確化、新しい情報の追加などが行われました。特に、Azure AI Search機能に関する説明や料金モデル、セキュリティ設定、コスト最適化などに関する情報が改善されました。

## 新機能
- エージェントリトリーバルのパイプライン作成における設定強制機能の情報追加。
- サーバーレスコスト最適化のための新たな推奨策の提示。

## 破壊的変更
- 特に重大な破壊的変更は報告されていません。

## その他の更新
- 画像分析スキルのAPI関連の表現修正。
- サーバーレス開発者層の使用に関するプレビュー情報更新。
- 無料試用アカウントに関する情報の再構成。
- ベクトル検索におけるドキュメント処理に関する情報整理。

# Insights
今回の更新では、Azure AI Searchに関連するドキュメントの多くがわかりやすくなるように改善されました。これは、新しいユーザーに対して機能の概要を提供し、既存のユーザーが使用のベストプラクティスを容易に理解できるようにするためのものです。

「エージェントリトリーバルソリューションのパイプライン作成」では、新たにユーザーごとのアクセスポリシーを強制できるオプションが追加され、安全性を向上させるための措置が示されています。これにより、一層セキュアな情報取得が可能となります。

画像分析スキルのドキュメントでは、AI APIの導入方法についてより一貫性のある記述が行われ、それにより開発者が機能の実装方法を理路整然と理解できるようになっています。サーバーレス関連のドキュメントも、プレビュー段階にもかかわらず、サービスが有料化されるタイミングを明示し、利用者が意識してサービス利用を計画できるようにしています。

コスト最適化に関するガイドラインは、特に企業がリソースを効率的かつ費用対効果の高い方法で管理するために役立ち、運用のコストを削減するための具体的なアドバイスが提供されます。

これらの更新はドキュメント全体の可読性を高め、新しい機能や既存機能の最適な利用方法を明確にするものです。ユーザーエクスペリエンスの向上を通じてAzureサービスの使用を促進する意図が見受けられます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | エージェントリトリーバルソリューションのパイプライン作成方法のチュートリアルの更新 | modified | 43 | 26 | 69 | 
| [cognitive-search-skill-image-analysis.md](#item-07daa8) | minor update | 画像分析スキルに関するドキュメントの修正 | modified | 1 | 2 | 3 | 
| [preview-serverless.md](#item-bbbf72) | minor update | サーバーレス開発者層のプレビュー情報の更新 | modified | 2 | 2 | 4 | 
| [search-try-for-free.md](#item-36e28d) | minor update | 無料試用アカウントの料金モデルとティアに関する情報の更新 | modified | 4 | 4 | 8 | 
| [serverless-cost-optimization.md](#item-8dc21e) | minor update | サーバーレスコスト最適化に関する情報の更新 | modified | 44 | 10 | 54 | 
| [vector-search-how-to-chunk-documents.md](#item-b79133) | minor update | ベクトル検索のドキュメントチャンクの扱いに関する情報の整理 | modified | 0 | 4 | 4 | 
| [vector-search-vectorizer-custom-web-api.md](#item-d7c2f9) | minor update | カスタムWeb APIに関する関連リンクの整理 | modified | 0 | 1 | 1 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: 'Tutorial: Build an Agentic Retrieval Solution'
 description: Build an agentic retrieval solution that connects Azure AI Search to Foundry Agent Service via MCP. Follow this tutorial to create a knowledge base and agent.
-ms.date: 07/20/2026
+ms.date: 08/06/2026
 ms.service: azure-ai-search
 ms.topic: tutorial
 ms.custom:
@@ -437,56 +437,73 @@ agent = project_client.agents.create_version(
 print(f"AI agent '{agent_name}' created or updated successfully")
 ```
 
-#### (Optional) Connect to a remote SharePoint knowledge source
+#### (Optional) Enforce permissions with per-request headers
 
-[!INCLUDE [foundry-iq-limitation](../foundry/includes/foundry-iq-limitation.md)]
+If any of your knowledge sources contain permission-protected content, the retrieval engine can filter results so that each user sees only the documents they're authorized to access. To enable this filtering, forward the signed-in user's identity token in the `x-ms-query-source-authorization` header of the MCP tool connection. Without the token, permission-enabled sources return results unfiltered. For more information, see [Enforce permissions at query time (preview)](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time-preview).
 
-Optionally, if your knowledge base includes a remote SharePoint knowledge source, you must also include the `x-ms-query-source-authorization` header in the MCP tool connection. For more information, see [Enforce permissions at query time (preview)](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time-preview).
+[!INCLUDE [vary-mcp-headers-per-request](../foundry/includes/vary-mcp-headers-per-request.md)]
 
-```python
-from azure.search.documents.indexes.models import RemoteSharePointKnowledgeSource, KnowledgeSourceReference
-from azure.search.documents.indexes import SearchIndexClient
-from azure.identity import get_bearer_token_provider
-
-remote_sp_ks = RemoteSharePointKnowledgeSource(
-    name="remote-sharepoint",
-    description="SharePoint knowledge source"
-)
-
-index_client = SearchIndexClient(endpoint=endpoint, credential=credential)
-index_client.create_or_update_knowledge_source(knowledge_source=remote_sp_ks)
-print(f"Knowledge source '{remote_sp_ks.name}' created or updated successfully.")
-
-knowledge_base.knowledge_sources = [
-    KnowledgeSourceReference(name=remote_sp_ks.name), KnowledgeSourceReference(name=knowledge_source_name)
-]
+The following code updates the agent from the previous step so the MCP tool reads its authorization header from a structured input.
 
-index_client.create_or_update_knowledge_base(knowledge_base=knowledge_base)
-print(f"Knowledge base '{base_name}' updated with new knowledge source successfully")
+```python
+from azure.ai.projects.models import StructuredInputDefinition
 
+# Reference the token as a placeholder in the header
 mcp_kb_tool = MCPTool(
     server_label="knowledge-base",
     server_url=mcp_endpoint,
     require_approval="never",
     allowed_tools=["knowledge_base_retrieve"],
     project_connection_id=project_connection_name,
     headers={
-        "x-ms-query-source-authorization": get_bearer_token_provider(credential, "https://search.azure.com/.default")()
+        "x-ms-query-source-authorization": "{{search_auth_token}}"
     }
 )
 
+# Declare the structured input so the caller can supply the token per request
 agent = project_client.agents.create_version(
     agent_name=agent_name,
     definition=PromptAgentDefinition(
         model=agent_model,
         instructions=instructions,
-        tools=[mcp_kb_tool]
+        tools=[mcp_kb_tool],
+        structured_inputs={
+            "search_auth_token": StructuredInputDefinition(
+                description="Per-user Azure AI Search bearer token",
+                required=True,
+                schema={"type": "string"},
+            )
+        }
     )
 )
 
 print(f"AI agent '{agent_name}' created or updated successfully")
 ```
 
+When you invoke the agent, supply an Azure AI Search token in `structured_inputs`. This example resolves a token from the current `credential`. For a multi-user app, pass the token of each signed-in user instead. For example, use a token obtained through an on-behalf-of flow so the retrieval engine can filter results for that user.
+
+```python
+# Resolve an Azure AI Search token from the current credential (use a per-user token in production)
+from azure.identity import get_bearer_token_provider
+
+search_token = get_bearer_token_provider(credential, "https://search.azure.com/.default")()
+
+openai_client = project_client.get_openai_client()
+conversation = openai_client.conversations.create()
+
+response = openai_client.responses.create(
+    conversation=conversation.id,
+    tool_choice="required",
+    input="{user_query}",
+    extra_body={
+        "agent_reference": {"name": agent.name, "type": "agent_reference"},
+        "structured_inputs": {"search_auth_token": search_token},
+    },
+)
+
+print(f"Response: {response.output_text}")
+```
+
 ### Chat with the agent
 
 Your client app uses the Conversations and [Responses](/azure/ai-foundry/openai/how-to/responses) APIs from Azure OpenAI to interact with the agent.
@@ -507,7 +524,7 @@ response = openai_client.responses.create(
         Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown?
         Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?
     """,
-    extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
+    extra_body={"agent_reference": {"name": agent.name, "type": "agent_reference"}},
 )
 
 print(f"Response: {response.output_text}")
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルソリューションのパイプライン作成方法のチュートリアルの更新"
}
```

### Explanation
この変更は、エージェントリトリーバルソリューションのパイプライン作成方法に関するチュートリアルを更新しました。主な変更内容には、ドキュメントの日付更新、機能の説明の改善、およびリクエストごとの権限の強制に関する新しい情報の追加が含まれています。

具体的には、ドキュメントの最初にあるメタ情報として、"ms.date" が2026年7月20日から2026年8月6日に更新されています。また、元のセクション「(Optional) Connect to a remote SharePoint knowledge source」が「(Optional) Enforce permissions with per-request headers」に改名され、言語が明確化されました。

新しい部分では、権限で保護されたコンテンツを含む知識ソースの場合、各ユーザーがアクセスを許可された文書のみを表示できるようにするために、`x-ms-query-source-authorization` ヘッダーにサインインユーザーのアイデンティティトークンを転送する必要があると説明されています。また、MCPツールの接続における承認を構造化された入力から読み取る方法も示されており、具体的なPythonコード例がいくつか新たに追加されています。

これにより、ユーザーはアプリケーションを通じてエージェントとより効果的にインタラクションできるようになります。全体として、エージェントの作成や知識源の更新のプロセスが改善され、セキュリティとユーザーエクスペリエンスが強化されました。

## articles/search/cognitive-search-skill-image-analysis.md{#item-07daa8}

<details>
<summary>Diff</summary>
````diff
@@ -23,8 +23,7 @@ This skill uses the machine learning models provided by [Azure Vision in Foundry
 
 Supported data sources for OCR and image analysis are blobs in Azure Blob Storage and Azure Data Lake Storage (ADLS) Gen2, and image content in Microsoft OneLake. Images can be standalone files or embedded images in a PDF or other files.
 
-This skill is implemented using the [AI Image Analysis API](/azure/ai-services/computer-vision/overview-image-analysis) version 3.2. If your solution requires calling a newer version of that service API (such as version 4.0), consider implementing through [Web API custom skill](cognitive-search-custom-skill-web-api.md) or use the [ImageAnalysisV4 power skill](https://github.com/Azure-Samples/azure-search-power-skills/blob/main/Vision/ImageAnalysisV4/README.md).
-
+This skill is implemented using the [AI Image Analysis API](/azure/ai-services/computer-vision/overview-image-analysis) version 3.2. If your solution requires calling a newer version of that service API, such as version 4.0, consider implementing through the [Custom Web API skill](cognitive-search-custom-skill-web-api.md).
 > [!NOTE]
 > This skill is bound to Foundry Tools and requires [a billable resource](cognitive-search-attach-cognitive-services.md) for transactions that exceed 20 documents per indexer per day. Execution of built-in skills is charged at the existing [Foundry Tools Standard price](https://azure.microsoft.com/pricing/details/cognitive-services/).
 >
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像分析スキルに関するドキュメントの修正"
}
```

### Explanation
この変更は、「画像分析」スキルに関するドキュメントに関する小規模な更新を行いました。主にテキストの編集が施され、いくつかの用語や文言が明確化されました。

具体的には、AI画像分析APIがバージョン3.2で実装されていることに関するセクションが修正されました。以前は「Web APIカスタムスキルを通じて実装することを検討してください」と記載されていた部分が、「Custom Web API skillにより実装することを検討してください」と変更され、表現が一貫性を持つように整えられています。また、バージョン4.0を呼び出す必要がある場合の案内が簡潔になり、情報の明瞭さが向上しています。

このように、テキストの整備によってユーザーがAPIのバージョンに関する指針を理解しやすくなっていますが、内容全般についての大きな変更は行われていないため、文書全体の整合性向上を目的としたマイナーな修正となっています。

## articles/search/includes/previews/preview-serverless.md{#item-bbbf72}

<details>
<summary>Diff</summary>
````diff
@@ -5,11 +5,11 @@ ms.topic: include
 ms.service: azure-ai-search
 author: mattwojo
 ms.author: mattwoj
-ms.date: 06/02/2026
+ms.date: 08/10/2026
 ---
 
 > [!IMPORTANT]
 > The Serverless Developer tier is currently in preview. This preview is provided without a service-level agreement and isn't recommended for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).<br><br>
-> Billing for the Serverless Developer tier isn't yet enabled during the preview. Estimated costs for your usage are available in the Azure portal and telemetry, but that usage won't appear on your Azure bill during this initial period. Microsoft will provide at least 30 days notice before billing begins. The deferral of billing during this preview is temporary. Serverless Developer is a paid tier and you'll be responsible for any charges accrued once billing begins.<br><br>
+> Billing for the Serverless Developer tier begins on September 13, 2026. Charges for usage on or after that date appear on your Azure bill. You aren't charged for usage before September 13, 2026. Serverless Developer is a paid tier once billing begins.
 > The Serverless Developer tier doesn't support migration to or from other pricing tiers and some features available on other tiers aren't supported during Public Preview. Service limits, supported features, and pricing details may change before general availability.<br><br>
 > The preview is currently only available in West Central US, Switzerland North, and Japan East.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレス開発者層のプレビュー情報の更新"
}
```

### Explanation
この変更は、「サーバーレス開発者層」に関するプレビュー情報の内容を更新しました。主に日付と請求に関する情報が修正されています。

具体的には、「ms.date」が2026年6月2日から2026年8月10日に更新されました。また、サーバーレス開発者層の請求が開始される日付が明確に示され、2026年9月13日から請求が発生することが明記されています。この変更により、ユーザーはその日以降の使用料がAzureの請求書に表示されることを理解しやすくなり、2026年9月13日以前の使用に対しては請求されないことが強調されています。

さらに、請求が開始された後は、この層が有料であることも明記され、ユーザーに対して注意を促しています。他の料金層との移行やサポートされる機能に関する情報は引き続き含まれており、プレビューの現在地として「西中央米国、スイス北部、日本東部」とも記載されています。これにより、サーバーレス開発者層の使用に関する重要な情報がより明確になり、ユーザーにとって利便性が向上しています。

## articles/search/search-try-for-free.md{#item-36e28d}

<details>
<summary>Diff</summary>
````diff
@@ -43,13 +43,13 @@ Before you create resources for a key-based connection, confirm regional support
 
 ## Choose a pricing model and tier
 
-Azure AI Search offers two pricing models: Dedicated and Serverless (Preview). For a free-trial account, you can evaluate Dedicated Free and Basic tiers, and you can also try the Serverless Developer tier at no charge during the initial preview period while reviewing estimated usage costs. Microsoft provides at least 30 days notice before Serverless Developer billing begins.
+Azure AI Search offers two pricing models: Dedicated and Serverless (Preview).
 
-+ **Free** doesn't consume credits and provides 50 MB of storage. You can have one free search service per Azure subscription. This tier is always free and doesn't expire, even after your 30-day trial ends. However, it doesn't support semantic ranking or managed identities for Microsoft Entra ID authentication and authorization, which are commonly used in quickstarts.
+- **Dedicated pricing model** - **Free tier** doesn't consume credits and provides 50 MB of storage. You can have one free search service per Azure subscription. This tier is always free and doesn't expire, even after your 30-day trial ends. However, it doesn't support semantic ranking or managed identities for Microsoft Entra ID authentication and authorization, which are commonly used in quickstarts.
 
-+ **Basic** (recommended) is in the Dedicated pricing model, consumes about one-third of your USD200 credits over 30 days, and provides 15 GB of storage in most regions. This tier supports all features, including semantic ranking and managed identities, and runs on dedicated infrastructure for consistent performance.
+- **Dedicated pricing model** - **Basic tier** (recommended) consumes about one-third of your USD200 credits over 30 days, and provides 15 GB of storage in most regions. This tier supports all features, including semantic ranking and managed identities, and runs on dedicated infrastructure for consistent performance.
 
-+ **Serverless Developer** (Preview) is in the Serverless pricing model and uses consumption-based pricing. During the initial preview period, you can evaluate estimated usage costs without billing. Microsoft provides at least 30 days notice before billing begins.
+- **Serverless pricing model** - **Serverless Developer tier** (Preview) uses consumption-based pricing. To evaluate usage costs in this tier, visit the [Azure portal](https://portal.azure.com) where you can view charges accrued once the billing period begins in the **Scale + Cost** tab.
 
 [!INCLUDE [Serverless preview](./includes/previews/preview-serverless.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "無料試用アカウントの料金モデルとティアに関する情報の更新"
}
```

### Explanation
この変更は、「無料試用アカウントの料金モデルとティア」に関する情報を整理し、より明確にすることを目的とした更新です。具体的には、料金モデルの説明が簡潔に記載されるように再編成されています。

まず、Azure AI Searchが提供する2つの料金モデル、すなわち「Dedicated（専用）」と「Serverless（サーバーレス）」に関する情報が明確に分離され、個々のモデルについての詳細な説明が提供されます。特に、各ティア（無料ティア、基本ティア、サーバーレス開発者ティア）の特長が強調され、どのような条件でそれぞれが利用できるかが明示されました。

例えば、無料ティアについては、クレジットを消費せず、50 MBのストレージを提供すること、さらには1つのAzureサブスクリプションにつき1つの無料検索サービスが利用可能であることが記載されています。基本ティアは推奨されているオプションとして位置づけられ、機能の幅が広いことや、一貫したパフォーマンスを提供する専用インフラを使用していることが強調されています。

サーバーレス開発者ティアについては、初期プレビュー期間中には請求が行われないことと、請求が開始する前にMicrosoftが少なくとも30日前に通知を行うことが強調されています。また、Azureポータルでの使用料の確認方法も明記され、ユーザーが利用状況を簡単に把握できるようになっています。

全体的に、この変更は情報の構成を見直すことで、ユーザーが各料金モデルとティアの違いや特長を理解しやすくなることを目指しています。

## articles/search/serverless-cost-optimization.md{#item-8dc21e}

<details>
<summary>Diff</summary>
````diff
@@ -29,8 +29,24 @@ For more information about pricing model and service tier differences, see [Choo
 In the Serverless model, **performance optimization directly affects cost**. Cost is directly tied to workload execution:
 
 - Queries and indexing consume compute, measured in Compute Units per hour (CU/h).
-- Storage is billed separately based on index size on disk.
-- When the service is idle with no active queries or indexing, compute usage is zero. There's no reserved or minimum capacity charge.
+- Active indexes consume compute based on their resource usage and how long they remain active.
+- An index stays active for 10 minutes after its last query or indexing request before it goes inactive.
+- Inactive indexes have no minimum or reserved compute charge. The compute usage for inactive indexes scales to zero. There's no minimum compute charge when an index is inactive.
+- Storage is billed separately based on index size on disk and continues whether or not an index is in use.
+- Agentic retrieval consumes compute for each query executed against knowledge sources backed by Azure AI Search indexes, plus a separate orchestration charge for generating those queries and merging the results into a single response.
+
+Storage charges stop only when you delete the index.
+
+### How index size affects compute usage
+
+While an index is active, Azure AI Search evaluates two finite resources to determine its compute usage:
+
+- **Total index size**: The total space that the index occupies on disk, including text, metadata, and vectors.
+- **Vector index size**: The memory used by the [vector index](vector-search-index-size.md). Memory is more resource intensive than disk, so vector index size has a higher weighting when converted to CUs.
+
+Azure AI Search doesn't add the two resulting CU amounts together. Compute usage is based on whichever amount is higher. For example, vector index size can determine compute usage even when the total index size on disk is relatively small.
+
+To reduce active-index compute usage, identify which resource produces the higher CU amount. Then reduce total index size, vector index size, or both. Indexed storage remains a separate per-GB/month charge.
 
 The Serverless pricing model is most cost-effective for workloads with variable, intermittent, or unpredictable traffic, where provisioned capacity would be underutilized.
 
@@ -57,17 +73,17 @@ Different operations have different cost profiles:
 
 ### Monitor compute usage
 
-Monitoring compute consumption helps you identify expensive operations, optimize query patterns, and estimate costs. The Compute Unit (CU) cost of every request is returned in the `x-ms-request-charge` HTTP response header as a floating-point number. Use this header to identify expensive operations and optimize query patterns. You can track the CU cost of every request by inspecting the HTTP response headers and operation events in Azure Monitor. For more guidance on the types of monitoring data available and methods for analyzing that data, see [Monitor Azure AI Search](/azure/azure-monitor/fundamentals/overview).
+Monitoring compute consumption helps you identify expensive operations, optimize query patterns, and estimate costs. The Compute Unit (CU) cost of every request is returned in the `x-ms-azs-compute-units-consumed` HTTP response header as a floating-point number. Use this header to identify expensive operations and optimize query patterns. You can track the CU cost of every request by inspecting the HTTP response headers and operation events in Azure Monitor. For more guidance on the types of monitoring data available and methods for analyzing that data, see [Monitor Azure AI Search](/azure/azure-monitor/fundamentals/overview).
 
-- **Header**: `x-ms-request-charge: <value>`
+- **Header**: `x-ms-azs-compute-units-consumed: <value>`
 - **Value**: A floating-point number representing the CUs consumed.
 
 Example:
 
 ```http
 Status: 200 OK
 Content-Type: application/json
-x-ms-request-charge: 12.45
+x-ms-azs-compute-units-consumed: 12.45
 ```
 
 In this example, the request consumed 12.45 compute units. You can use this value to identify high-cost operations and compare the relative cost of different query patterns.
@@ -107,16 +123,20 @@ To estimate serverless costs:
 
 1. Index representative sample data.
 1. Run typical indexing and query workloads.
-1. Record the `x-ms-request-charge` value returned for each operation.
+1. Record the `x-ms-azs-compute-units-consumed` value returned for each operation.
 1. Use Azure Monitor metrics to measure aggregate usage over time.
 1. Extrapolate costs based on expected production traffic.
 
+Use the **Scale + Cost** tab in the Azure portal to see your current usage and estimate costs.
+
 Because the same request executed against the same data generally produces similar compute consumption, representative workloads can provide a reliable basis for cost estimation.
 
 Serverless usage is measured continuously and aggregated for billing. Compute consumption is tracked throughout each minute and emitted only when compute resources are used.
 
 When estimating costs, use request charge values to understand the cost of individual operations and Azure Monitor metrics to understand overall service consumption patterns.
 
+Use both data sources together to understand costs: per-request charge data helps you evaluate individual operations, while Azure Monitor metrics help you understand aggregate service consumption over time. For a complete cost picture, also account for features that are billed separately from Compute Units.
+
 Billing is based on aggregate compute usage rather than individual requests. Usage is measured in one-minute intervals and rounded up to the nearest 0.25 CU per minute. These one-minute usage intervals accumulate over the course of an hour to determine the billable CU/hour amount. Internally, usage aggregates from milli-compute units (mCU) to compute units (CU) and converts into the hourly usage reported for billing.
 
 Different operations consume different amounts of compute. In general:
@@ -150,16 +170,28 @@ How you send data to the index affects both cost and throughput:
 
 - **Index only new or changed data**: Avoid full reindexing when possible. Sending only additions and updates reduces the number of documents processed, lowering compute cost and improving ingestion speed.
 
-- **Use change detection for incremental indexing**: Detect what changed before you reprocess content. Incremental indexing avoids repeated work on unchanged documents and keeps reprocessing costs down.
-
 - **Skip image extraction unless you need it**: Image extraction adds extra processing work and can become a separate cost driver. Turn it on only for documents or workflows that actually need image content.
 
-- **Target skills to relevant fields and documents**: Scope enrichment skills to the specific fields or documents they need. Avoid running skills across content that doesn't need enrichment, especially when the outputs aren't used downstream.
-
 - **Account for index size growth**: Where possible, create smaller indexes. As an index grows, indexing costs increase because more data must be stored and maintained, and operations require more compute. For very large datasets, consider partitioning data across multiple indexes to help manage performance and costs. Although costs rise with index size, the increase is sublinear. Larger indexes cost more per operation, but not proportionally more.
 
 For more guidance, see [Tips for better performance in Azure AI Search](./search-performance-tips.md).
 
+### Optimize indexer operations
+
+Serverless indexer compute usage depends on the work performed during each indexer run. For row-oriented sources, use the number of documents processed as an indicator of workload volume. For file-based sources such as Azure Blob Storage and Azure Data Lake Storage Gen2, monitor the amount of source data processed. Actual compute usage also depends on document payloads, index structure, enrichment, and other processing performed during the run.
+
+To reduce indexer compute usage:
+
+- **Use change detection and incremental indexing**: Process only new or changed data instead of repeatedly indexing the full data source.
+
+- **Right-size indexer schedules**: Choose a schedule that meets your data freshness requirements. Use Compute Unit telemetry to evaluate the effect of schedule frequency.
+
+- **Reduce unnecessary document content**: Remove content that doesn't need to be indexed, and exclude files or file types that aren't required.
+
+- **Scope enrichment skills carefully**: Run skills only on fields and documents that require enrichment, and avoid generating outputs that aren't used downstream. Billable skills can incur separate transaction charges.
+
+- **Monitor failed and repeated runs**: An indexer can consume compute for work completed before it fails. Review execution history and Compute Unit usage to identify recurring failures and retry patterns.
+
 ### Optimize your queries
 
 Query design is a primary driver of variable cost:
@@ -208,6 +240,8 @@ Vector queries are compute-intensive because they require similarity calculation
 
 - **Use hybrid search selectively**: Hybrid queries run both keyword and vector retrieval. Use only when necessary for relevance.
 
+- **Tune `maxTextRecallSize` for hybrid queries**: Set `hybridSearch.maxTextRecallSize` to control how many BM25-ranked text results are available to Reciprocal Rank Fusion (RRF). The default is 1,000, and the supported range is 1 through 10,000. Lowering the value can reduce text retrieval and result-fusion work, which can reduce resource utilization and latency. However, it can exclude relevant keyword results, including exact terms, IDs, and acronyms that vector search might miss. Test representative queries, and compare relevance, latency, and the `x-ms-azs-compute-units-consumed` response header before selecting a value. Control vector candidates separately by setting `k` on each vector query.
+
 - **Apply filters before vector queries**: Narrow the candidate set before vector search to reduce the amount of data processed. See [How filtering works in vector queries](./vector-search-filters.md#how-filtering-works-in-vector-queries).
 
 ## Reduce costs by minimizing usage
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスコスト最適化に関する情報の更新"
}
```

### Explanation
この変更は、「サーバーレスコスト最適化」に関する文書の内容を更新し、情報をより明確に、かつ詳細にすることを目的としています。主な変更点として、サーバーレスモデルにおけるコストの最適化に関する情報が新たに追加され、文の構造が整理されました。

具体的には、インデックスのサイズが計算使用量に与える影響に関するセクションが新設され、推奨される課題解決の手法が詳述されています。アクティブなインデックスのリソース使用状況や、非アクティブインデックスに対する料金が明記され、条件に応じて課金が行われないことが強調されています。また、ストレージやクエリの実行に関する詳細情報が追加され、それぞれの課金モデルについての説明が改善されています。

さらに、Compute Unit (CU) の消費量をモニタリングする重要性も強調され、個々のリクエストに対するCU消費量を追跡する方法が具体的に示されています。これは、コストの予測や運用の最適化において役立ちます。

新出のセクションには、インデクサーの操作の最適化やクエリの利用法についての指針も含まれており、サーバーレスインデクサーの計算使用量を削減するための具体的な提案が行われています。また、特定のクエリ設計やハイブリッド検索の利用に関するアドバイスも提供され、コストを削減し、リソースの利用を効率化するための方法が解説されています。

全体的に、この変更は、コストの最適化に関する知識を提供し、ユーザーがAzure AI Searchのサーバーレス料金モデルを理解し、最適に利用できるようにすることを目的としています。

## articles/search/vector-search-how-to-chunk-documents.md{#item-b79133}

<details>
<summary>Diff</summary>
````diff
@@ -185,10 +185,6 @@ Output for two consecutive chunks shows the text from the first chunk overlappin
 
 `'**Darkness is not void of illumination. It is the contrast, the area between light and **\ndark, that is often the most illustrative. Darkness reminds me of where I came from and where I am now-from a small town in the mountains, to the unique vantage point of the Nation's capital. Darkness is where dreamers and learners of all ages peer into the universe and think of questions about themselves and their space in the cosmos. Light is where they work, where they gather, and take time together.\nNASA's spacefaring satellites have compiled an unprecedented record of our \nEarth, and its luminescence in darkness, to captivate and spark curiosity. These missions see the contrast between dark and light through the lenses of scientific instruments. Our home planet is full of complex and dynamic cycles and processes. These soaring observers show us new ways to discern the nuances of light created by natural and human-made sources, such as auroras, wildfires, cities, phytoplankton, and volcanoes.' metadata={'source': './data/earth_at_night_508.pdf', 'page': 9}`
 
-### Custom skill
-
-A [fixed-sized chunking and embedding generation sample](https://github.com/Azure-Samples/azure-search-power-skills/blob/main/Vector/EmbeddingGenerator/README.md) demonstrates both chunking and vector embedding generation using [Azure OpenAI](/azure/ai-services/openai/) embedding models. This sample uses an [Azure AI Search custom skill](cognitive-search-custom-skill-web-api.md) in the [Power Skills repo](https://github.com/Azure-Samples/azure-search-power-skills/tree/main#readme) to wrap the chunking step.
-
 ## Related content
 
 - [Understand embeddings in Azure OpenAI in Foundry Models](/azure/ai-services/openai/concepts/understand-embeddings)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のドキュメントチャンクの扱いに関する情報の整理"
}
```

### Explanation
この変更は、「ベクトル検索におけるドキュメントのチャンク処理」に関する情報を整理し、文書の冗長性を減少させることを目的としています。具体的には、既存の情報から一部のセクションが削除され、内容が簡潔になるように調整されています。

変更された部分では、カスタムスキルに関する詳細が削除されました。これにより、具体的な実装例やサンプルコードへの参照がなくなり、文書がより流動的にところどころで一貫性を持つようになります。特に「固定サイズのチャンク生成」と「ベクトル埋め込み生成」に関連する情報が削除されましたが、これによってユーザーが必要な情報により早くアクセスできるようになると考えられます。

加えて、関連コンテンツへのリンクも削除されましたが、これにより文書の焦点がより明確になり、主題に対する理解を深めることができます。この変更は、ユーザーが必要とする情報を迅速に得られるようにし、全体の可読性を向上させるためのものであるといえます。

全体として、文書はよりシンプルで、一貫したメッセージを持つようになっており、ユーザーにとって利便性が高まったといえます。

## articles/search/vector-search-vectorizer-custom-web-api.md{#item-d7c2f9}

<details>
<summary>Diff</summary>
````diff
@@ -157,4 +157,3 @@ Keep the following considerations in mind when implementing a web API endpoint f
 + [Integrated vectorization](vector-search-integrated-vectorization.md)
 + [How to configure a vectorizer in a search index](vector-search-how-to-configure-vectorizer.md)
 + [Custom Web API skill](cognitive-search-custom-skill-web-api.md)
-+ [Hugging Face Embeddings Generator power skill (can be used for a custom web API vectorizer as well)](https://github.com/Azure-Samples/azure-search-power-skills/tree/main/Vector/EmbeddingGenerator)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムWeb APIに関する関連リンクの整理"
}
```

### Explanation
この変更は、「ベクトル検索のベクトライザーに関するカスタムWeb API」の文書の一部を更新し、関連リンクの整理を目的としています。具体的には、参照されているリンクの中から1つが削除されています。

削除されたリンクは、「Hugging Face Embeddings Generator power skill」に関するもので、このリンクはカスタムWeb APIベクトライザーとしても使用できることが示されていました。この変更により、文書内の情報がよりシンプルで明確になり、利用者に混乱を招く可能性のある情報が除かれています。

更新されたリンクは、統合ベクトル化、ベクトライザーの設定方法、カスタムWeb APIスキルに関するものであり、これによりユーザーが関連する情報を簡単に見つけられるようになります。全体として、この変更は文書の可読性を向上させるとともに、利用者に提供する情報の一貫性を保つことを意図しています。


