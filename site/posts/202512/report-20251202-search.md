---
date: '2025-12-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5867053...MicrosoftDocs:02f798d
summary: Azure AI Searchに関するドキュメントが更新され、複数のセクションで新しい情報や機能が追加されました。主な更新内容には、スコアリング・プロファイルの説明の改良、インデックス作成ガイドの明確化、およびセキュリティ関連の画像が含まれます。新機能として、ネットワーク設定やアクセス管理を視覚的に理解できる新しい画像が追加されました。破壊的な変更は特になく、機能の正確性と理解のしやすさが向上しています。さらに、APIキー関連のセキュリティプラクティスが詳述されており、全体的にユーザーがAzure
  AI Searchをより効果的に活用できるような改善が行われています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5867053...MicrosoftDocs:02f798d){target="_blank"}

# ハイライト
ドキュメントの更新および新機能として、複数のセクションでAzure AI Searchに関する情報が刷新され、いくつかの新しい機能が追加されました。主要な更新としては、スコアリング・プロファイルの説明の改良、インデックス作成についてのガイドの明確化、そしてセキュリティに関連する画像の追加と更新があります。また、トラステッドサービス例外やACLおよびRBACのドキュメントもより理解しやすく改善されています。

## 新機能
- セレクトネットワークを有効にするためおよびネットワークアクセス管理用の新しい画像が追加され、ユーザーはネットワーク設定やアクセス管理を視覚的に理解できるようになりました。

## 破壊的変更
特に破壊的な変更はありませんが、ドキュメントの更新により情報の正確性や理解のしやすさが向上しています。

## その他の更新
- エージェント取得とスコアリング・プロファイルに関するガイドがより明確に修正され、ブースト設定の影響や日付フレッシュネス関数の効果が整理されています。
- トラステッドサービス例外およびACLやRBACに関するドキュメントの更新により、セキュリティの詳細が強調され、ユーザーの理解が深まりました。
- APIキー関連のドキュメントが更新され、セキュリティプラクティスの推奨事項がより詳細に記述されています。

# インサイト
この一連の変更を通じて、Azure AI Searchのドキュメントはより豊富で、ユーザーフレンドリーなものに進化しています。特に、ネットワークセキュリティに関する新しい画像の追加や、重要なセキュリティ機能の明確化は、ユーザーが自身の環境をより安全に管理する助けになります。更新されたスコアリング・プロファイルの内容は、開発者がAzure Searchの検索結果をより効果的に最適化するための重要な情報を提供しています。

インデックス作成やトラステッドサービス例外の文書の改訂により、ユーザーはプロジェクトの管理と設定を効率的に行いやすくなり、開発時間の削減につながります。APIキーの更新情報は、セキュリティリスクを軽減するためのベストプラクティスを提示し、Azureサービスを利用する際のガイドラインとして有用です。

このように、ドキュメントの改善と新機能の追加により、Azure AI Searchのユーザーは最新の情報とツールを活用してより効果的なシステムの設計と実施が行えるようになります。これらの更新は、セキュリティに対する重要性を高めるだけでなく、サービスの総合的な使用経験を向上させるために不可欠なステップです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-index.md](#item-3fbd2e) | minor update | エージェント取得インデックス作成に関するガイドの修正 | modified | 1 | 1 | 2 | 
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | スコアリング・プロファイルに関するガイドの修正 | modified | 3 | 3 | 6 | 
| [enable-selected-networks.png](#item-85dc7b) | new feature | セレクトネットワークを有効にするための画像追加 | added | 0 | 0 | 0 | 
| [exception.png](#item-be28c5) | minor update | 例外画像の更新 | modified | 0 | 0 | 0 | 
| [manage-network-access.png](#item-afc28a) | new feature | ネットワークアクセス管理用画像の追加 | added | 0 | 0 | 0 | 
| [system-assigned-identity-object-id.png](#item-eac4a5) | minor update | システム割り当てIDの画像更新 | modified | 0 | 0 | 0 | 
| [search-indexer-howto-access-trusted-service-exception.md](#item-e19826) | minor update | トラステッドサービス例外に関するドキュメントの更新 | modified | 23 | 17 | 40 | 
| [search-query-access-control-rbac-enforcement.md](#item-d24df7) | minor update | クエリ時のACLとRBACの強制に関するドキュメントの更新 | modified | 15 | 2 | 17 | 
| [search-security-api-keys.md](#item-d8c908) | minor update | APIキーを使用した接続に関するドキュメントの更新 | modified | 107 | 92 | 199 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-index.md{#item-3fbd2e}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ In Azure AI Search, agentic retrieval uses context and user questions to generat
 
 + An *existing index* containing searchable content. You can make an existing index available to agentic retrieval through a [search index knowledge source](agentic-knowledge-source-how-to-search-index.md) definition.
 
-+ A *generated index* created from an indexed [knowledge source](agentic-knowledge-source-overview.md). Indexed knowledge sources create a copy of an external data source inside a search index using a full indexer pipeline (data source, skillset, indexer, and index) for agentic retrieval. Indexed knowledge sources create a copy of an external data source inside a search index using a full indexer pipeline (data source, skillset, indexer, and index) for agentic retrievalMultiple knowledge sources can generate an indexer pipeline that results in a searchable index. These include:
++ A *generated index* created from an indexed [knowledge source](agentic-knowledge-source-overview.md). Indexed knowledge sources create a copy of an external data source inside a search index using a full indexer pipeline (data source, skillset, indexer, and index) for agentic retrieval. Multiple knowledge sources can generate an indexer pipeline that results in a searchable index. These include:
 
   + [Azure blobs](agentic-knowledge-source-how-to-blob.md)
   + [Microsoft OneLake](agentic-knowledge-source-how-to-onelake.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント取得インデックス作成に関するガイドの修正"
}
```

### Explanation
この変更は、Azure AI Searchに関連する文書に対するマイナーな更新です。具体的には、エージェント取得のコンテキストにおいて、インデックスの生成に関する説明が明確化されました。文中で、既存のインデックスと生成されたインデックスの定義が新たに加わりました。この更新は、他の情報源やデータソースとの関係を明確にし、ユーザーがエージェント取得プロセスをより理解しやすくすることを目的としています。変更点は、1行の追加と1行の削除で、全体の内容が整理され、理解しやすさが向上しています。

## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -233,9 +233,9 @@ For more examples, see [XML Schema: Datatypes (W3.org web site)](https://www.w3.
 
 ## Example: boosting by freshness or distance
 
-When using the freshness function, if you want the boost to have a more dramatic effect on more recent dates, and taper off for older dates, choose a quadratic interpolation. Quadratic amplifies the effect of near recent dates. This same logic applies to distance boosting, where farther locations yield larger magnitudes.
+The shape of the boost curve (constant, linear, logarithmic, quadratic) affects how aggressively scores change across the range. 
 
-The shape of the boost curve (constant, linear, logarithmic, quadratic) affects how aggressively scores change across the range. A quadratic curve tapers off more slowly for older dates, while a logarithmic curve shifts more sharply at the far end.
+When using the freshness function, if you want the boost to have a more dramatic effect on more recent dates, choose a quadratic interpolation. Quadratic amplifies the effect of near recent dates and closer locations and tapers off more slowly at the far end of the range. In contrast, a logarithmic curve shifts more sharply at the far end.
 
 Here's an example scoring profile that demonstrates how to boost by freshness.
 
@@ -361,7 +361,7 @@ The `boostGenre` profile uses weighted text fields, boosting matches found in al
 }  
 ```
 
-## Example: function aggregation 
+## Example: function aggregation
 
 > [!NOTE]
 > This capability is currently in preview, available through the [2025-11-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) and in Azure SDK preview packages that provide the feature.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリング・プロファイルに関するガイドの修正"
}
```

### Explanation
このコードの変更は、スコアリング・プロファイルに関するドキュメントの内容に対するマイナーな更新です。特に、スコアリングのブースト曲線の形状による影響の説明が整理され、より明確になりました。変更点では、フレッシュネス関数の説明の順序が入れ替わり、より効果的な表現になっています。具体的には、より新しい日付に対するブーストの効果を強調し、ロジスティック曲線の動作がより詳しく説明されています。また、例として示されたスコアリング・プロファイルについての情報も整理され、読みやすさが向上しています。全体として、内容の流れと理解の促進に寄与する更新です。

## articles/search/media/search-indexer-howto-secure-access/enable-selected-networks.png{#item-85dc7b}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "セレクトネットワークを有効にするための画像追加"
}
```

### Explanation
この変更は、Azure AI Searchに関するドキュメントに対して新しい画像ファイルが追加されたことを示しています。具体的には、「セレクトネットワークを有効にする」手順を視覚的に説明するための画像が新たに追加されました。この画像は、ユーザーがネットワーク設定を理解し、適切に構成する助けとなることを目的としています。追加された画像は、関連する手順を補完し、学習や実践における理解を深める効果が期待されます。

## articles/search/media/search-indexer-howto-secure-access/exception.png{#item-be28c5}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "例外画像の更新"
}
```

### Explanation
この変更は、Azure AI Searchに関連するドキュメント内の「例外」を示す画像が更新されたことを示しています。この画像の変更は、特定のエラーや例外の理解を助けるために、より明確または最新の情報を提供する目的で行われました。具体的な変更内容は表示されていませんが、画像の更新により、ユーザーが問題のトラブルシューティングや解決策を見つけやすくなることが期待されます。このマイナーな変更は、全体的なドキュメントの質を向上させる効果があります。

## articles/search/media/search-indexer-howto-secure-access/manage-network-access.png{#item-afc28a}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ネットワークアクセス管理用画像の追加"
}
```

### Explanation
この変更は、Azure AI Searchに関するドキュメントに新しい画像ファイルが追加されたことを示しています。具体的には、「ネットワークアクセスを管理する」ためのプロセスを視覚的に説明する目的でこの画像が追加されました。この追加により、ユーザーはネットワークアクセスの設定や管理についての理解を深めることができるようになります。新しい画像は、手順や設定を視覚的に示すことにより、利用者に対してよりわかりやすく、実用的な情報を提供する役割を果たします。

## articles/search/media/search-managed-identities/system-assigned-identity-object-id.png{#item-eac4a5}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "システム割り当てIDの画像更新"
}
```

### Explanation
この変更は、Azureのマネージドアイデンティティに関連する「システム割り当てアイデンティティのオブジェクトID」を示す画像が更新されたことを示しています。この画像の更新は、ユーザーがシステム割り当てアイデンティティに関する情報をより正確に理解できるようにするために行われました。具体的な変更点は見られませんが、画像の改良により、ドキュメント全体の視覚的な一貫性や理解を向上させることを目的としています。更新された画像は、特に新しいユーザーやこの機能に不慣れなユーザーに対して、より効果的に情報を伝える役割を果たすと Expectされます。

## articles/search/search-indexer-howto-access-trusted-service-exception.md{#item-e19826}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +1,13 @@
 ---
-title: Connect as trusted service
+title: Connect as Trusted Service
 titleSuffix: Azure AI Search
-description: Enable secure data access to Azure Storage from an indexer in Azure AI Search 
+description: Learn how to enable secure data access to Azure Storage from an indexer in Azure AI Search.
 manager: nitinme
 author: arv100kri
 ms.author: arjagann
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/04/2025
+ms.date: 12/01/2025
 ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
@@ -23,44 +23,50 @@ In Azure AI Search, indexers that access Azure blobs can use the [trusted servic
 
 ## Prerequisites
 
-+ A search service with a system-assigned managed identity ([see check service identity](#check-service-identity)).
++ A search service with a system-assigned managed identity. See [Check service identity](#check-service-identity).
 
-+ A storage account with the **Allow trusted Microsoft services to access this storage account** network option ([see check network settings](#check-network-settings)).
++ A storage account with the **Allow trusted Microsoft services to access this storage account** network option. See [Check network settings](#check-network-settings).
 
-+ An Azure role assignment in Azure Storage that grants permissions to the search service system-assigned managed identity ([see check permissions](#check-permissions)).
++ An Azure role assignment in Azure Storage that grants permissions to the search service system-assigned managed identity. See [Check permissions](#check-permissions).
 
 > [!NOTE]
 > In Azure AI Search, a trusted service connection is limited to blobs and ADLS Gen2 on Azure Storage. It's unsupported for indexer connections to Azure Table Storage and Azure Files.
 >
-> A trusted service connection must use a system managed identity. A user-assigned managed identity isn't currently supported for this scenario.
+> A trusted service connection must use a system-assigned managed identity. A user-assigned managed identity isn't currently supported for this scenario.
 
 ## Check service identity
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
 
-1. On the **Identity** page, make sure that a [system assigned identity is enabled](search-how-to-managed-identities.md). Remember that user-assigned managed identities won't work for a trusted service connection.
+1. From the left pane, select **Settings** > **Identity**.
+
+1. [Enable a system-assigned identity](search-how-to-managed-identities.md). Remember that user-assigned managed identities don't work for a trusted service connection.
 
    :::image type="content" source="media/search-managed-identities/system-assigned-identity-object-id.png" alt-text="Screenshot of a system identity object identifier." border="true":::
 
 ## Check network settings
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and [find your storage account](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Storage%2storageAccounts/).
 
-1. In the left pane under **Security + networking**, select **Networking**.
+1. From the left pane, select **Security + networking** > **Networking**.
 
-1. On the **Firewalls and virtual networks** tab, allow access from **Selected networks**.
+1. On the **Public access** tab, select **Manage**.
 
-1. Scroll down to the **Exceptions** section.
+   :::image type="content" source="media\search-indexer-howto-secure-access\manage-network-access.png" alt-text="Screenshot of the button to manage public network access in the Azure portal." border="true":::
 
-   :::image type="content" source="media\search-indexer-howto-secure-access\exception.png" alt-text="Screenshot of the firewall and networking page for Azure Storage in the Azure portal." border="true":::
+1. Under **Public network access scope**, select **Enable from selected networks**.
+
+   :::image type="content" source="media\search-indexer-howto-secure-access\enable-selected-networks.png" alt-text="Screenshot of the option to enable access from selected networks in the Azure portal." border="true":::
 
-1. Make sure the checkbox is selected for **Allow Azure services on the trusted services list to access this storage account**.
+1. Under **Exceptions**, select **Allow trusted Microsoft services to access this resource**.
+
+   :::image type="content" source="media\search-indexer-howto-secure-access\exception.png" alt-text="Screenshot of the firewall and networking page for Azure Storage in the Azure portal." border="true":::
 
    Assuming your search service has role-based access to the storage account, it can access data even when connections to Azure Storage are secured by IP firewall rules.
 
 ## Check permissions
 
-A system managed identity is a Microsoft Entra service principal. The assignment needs **Storage Blob Data Reader** at a minimum.
+A system-assigned managed identity is a Microsoft Entra service principal. The assignment needs **Storage Blob Data Reader** at a minimum.
 
 1. In the left pane under **Access Control**, view all role assignments and make sure that **Storage Blob Data Reader** is assigned to the search service system identity.
 
@@ -70,15 +76,15 @@ A system managed identity is a Microsoft Entra service principal. The assignment
 
 ## Set up and test the connection
 
-The easiest way to test the connection is by running the Import data wizard.
+The easiest way to test the connection is by running the **Import data** wizard.
 
-1. Start the Import data wizard, selecting the Azure Blob Storage or Azure Data Lake Storage Gen2. 
+1. Start the **Import data** wizard, selecting Azure Blob Storage or Azure Data Lake Storage Gen2.
 
 1. Choose a connection to your storage account, and then select **System-assigned**. Select **Next** to invoke a connection. If the index schema is detected, the connection succeeded.
 
    :::image type="content" source="media\search-indexer-howto-secure-access\test-system-identity.png" alt-text="Screenshot of the Import data wizard data source connection page." border="true":::
 
-## See also
+## Related content
 
 + [Connect to other Azure resources using a managed identity](search-how-to-managed-identities.md)
 + [Azure blob indexer](search-how-to-index-azure-blob-storage.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トラステッドサービス例外に関するドキュメントの更新"
}
```

### Explanation
この変更は、「トラステッドサービス例外にアクセスする方法」についてのドキュメントが修正されたことを示しています。主な変更点は、文法の修正、説明の明確化、日付の更新が含まれています。具体的には、タイトルの「trusted service」が「Trusted Service」に変更され、説明文がより明確に改善されています。また、システム管理されたアイデンティティに関する条件が強調され、必要なロールの追加情報が整理されています。これにより、ユーザーがトラステッドサービスの接続を設定し、必要な手順を理解する上での利便性が向上しています。全体的に、より使いやすく、情報がわかりやすい形に進化しています。

## articles/search/search-query-access-control-rbac-enforcement.md{#item-d24df7}

<details>
<summary>Diff</summary>
````diff
@@ -3,8 +3,8 @@ title: Query-Time ACL and RBAC Enforcement
 titleSuffix: Azure AI Search  
 description: Learn how query-time ACL and RBAC enforcement ensures secure document retrieval in Azure AI Search for indexes containing permission filters from data sources such as Azure Data Lake Storage (ADLS) Gen2 and SharePoint in Microsoft 365.  
 ms.service: azure-ai-search  
-ms.topic: conceptual  
-ms.date: 11/10/2025  
+ms.topic: article  
+ms.date: 12/01/2025  
 author: mattgotteiner  
 ms.author: magottei 
 ---  
@@ -137,6 +137,19 @@ x-ms-enable-elevated-read: true
 > [!IMPORTANT]
 > The `x-ms-enable-elevated-read` header only works on Search POST actions. You can't perform an elevated read query on a [knowledge base retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true) action.
 
+
+### Important ACL functionality behavior change in specific preview API versions
+
+Before REST API version `2025-11-01-preview`, earlier preview versions `2025-05-01-preview` and `2025-08-01-preview` returned all documents when using a service API key or authorized Entra roles, even if no user token was provided. Applications that didn’t validate the presence of a user token could inadvertently expose results to end users if not implemented correctly or following best practices.
+
+Starting in November 2025, this behavior changed:
+
+- ACL permission filters now apply even when using only service API keys or Entra authentication across all versions that support ACL.
+- If the user token is omitted, ACL-protected content isn't returned.
+- To view all documents for troubleshooting, you must explicitly include the elevated-read header when using REST API version `2025-11-01-preview`.
+
+This update helps keep content protected when applications don’t enforce best practices for token validation.
+
 ## See also
 
 - [Tutorial: Index ADLS Gen2 permission metadata](tutorial-adls-gen2-indexer-acls.md) 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリ時のACLとRBACの強制に関するドキュメントの更新"
}
```

### Explanation
この変更は、「クエリ時のACLおよびRBACの強制」に関するドキュメントの更新を示しています。主な修正点は、ドキュメントのメタデータの更新、特にトピックの変更と日付の更新です。また、重要なACL機能の動作の変更についての新たなセクションが追加され、特定のプレビューバージョンのREST APIにおける動作に関する情報が提供されています。この変更により、サービスAPIキーまたはEntra認証を使用している場合でも、ユーザートークンが提供されていない場合にはACLによる制限が適用されることが明示されました。この更新は、トークンの検証に関するベストプラクティスが適切に実装されていない場合でも、コンテンツが保護されるのに役立ちます。全体として、ユーザーがセキュリティの重要性を理解し、誤った実装による情報漏洩を防ぐための認識を高めることを目的としています。

## articles/search/search-security-api-keys.md{#item-d8c908}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Connect using API keys
+title: Connect Using API keys
 titleSuffix: Azure AI Search
 description: Learn how to use an admin or query API key for inbound access to an Azure AI Search service endpoint.
 manager: nitinme
@@ -9,42 +9,122 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 10/22/2025
+ms.date: 12/01/2025
 ms.update-cycle: 365-days
 #customer intent: I want to learn how to connect to Azure AI Search using API keys so that I can authenticate inbound requests to my search service.
 ---
 
 # Connect to Azure AI Search using keys
 
-Azure AI Search supports both identity-based and key-based authentication for connections to your search service. An API key is a unique string composed of 52 randomly generated numbers and letters. In your source code, you can specify it in a request header, or as an [environment variable](/azure/ai-services/cognitive-services-environment-variables) or app setting in your project, and then reference the variable on the request.
+Azure AI Search supports both identity-based and key-based authentication for connections to your search service. An API key is a unique string composed of 52 randomly generated numbers and letters.
+
+In your source code, you can directly specify the API key in a request header. Alternatively, you can store it as an [environment variable](/azure/ai-services/cognitive-services-environment-variables) or app setting in your project and then reference the variable in the request.
 
 > [!IMPORTANT]
 > When you create a search service, key-based authentication is the default, but it's not the most secure option. We recommend that you replace it with [role-based access](search-security-enable-roles.md).
 
 ## Enabled by default
 
-Key-based authentication is the default on new search services. A request made to a search service endpoint is accepted if both the request and the API key are valid, and your search service is configured to allow API keys on a request. In the Azure portal, authentication is specified on the **Keys** page under **Settings**. Either **API keys** or **Both** provide key support.
+Key-based authentication is the default for new search services. A request made to a search service endpoint is accepted if both the request and the API key are valid and if the search service is configured to allow API keys on a request.
+
+In the Azure portal, you specify authentication on the **Settings** > **Keys** page. Either **API keys** or **Both** provides key support.
 
 :::image type="content" source="media/search-security-overview/api-keys-enabled.png" alt-text="Screenshot of the Keys page in the Azure portal.":::
 
-## Types of API keys
+## Types of keys
 
 There are two kinds of keys used for authenticating a request:
 
-| Type | Permission level | Maximum | How created|
+| Type | Permission level | How it's created | Maximum |
 |------|------------------|---------|---------|
-| Admin | Full access (read-write) for all content operations | 2 <sup>1</sup>| Two admin keys, referred to as *primary* and *secondary* keys in the Azure portal, are generated when the service is created and can be individually regenerated on demand. |
-| Query | Read-only access, scoped to the documents collection of a search index | 50 | One query key is generated with the service. More can be created on demand by a search service administrator. |
+| Admin | Full access (read-write) for all content operations | Two admin keys, referred to as *primary* and *secondary* keys in the Azure portal, are generated when the service is created and can be individually regenerated on demand. | 2 <sup>1</sup> |
+| Query | Read-only access, scoped to the documents collection of a search index | One query key is generated with the service. More can be created on demand by a search service administrator. | 50 |
 
 <sup>1</sup> Having two allows you to roll over one key while using the second key for continued access to the service.
 
 Visually, there's no distinction between an admin key or query key. Both keys are strings composed of 52 randomly generated alpha-numeric characters. If you lose track of what type of key is specified in your application, you can [check the key values in the Azure portal](#find-existing-keys).
 
-## Use API keys on connections
+### Key-to-role mapping
+
+This article is about API keys. However, if you want to transition to role-based access, it's helpful to understand how keys map to [built-in roles in Azure AI Search](search-security-rbac.md#built-in-roles-used-in-search):
+
++ An admin key corresponds to the **Search Service Contributor** and **Search Index Data Contributor** roles.
++ A query key corresponds to the **Search Index Data Reader** role.
+
+## Permissions to view or manage keys
+
+Permissions for viewing and managing API keys are conveyed through [role assignments](search-security-rbac.md). Members of the following roles can view and regenerate keys:
+
++ Owner
++ Contributor
++ [Search Service Contributor](/azure/role-based-access-control/built-in-roles#search-service-contributor)
++ Administrator and co-administrator (classic)
+
+The following roles don't have access to API keys:
+
++ Reader
++ Search Index Data Contributor
++ Search Index Data Reader
+
+## Find existing keys
+
+You can view and manage API keys using the [Azure portal](https://portal.azure.com), [PowerShell](/powershell/module/az.search), [Azure CLI](/cli/azure/search), or [REST API](/rest/api/searchmanagement/).
+
+### [**Portal**](#tab/portal-find)
+
+1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
+
+1. From the left pane, select **Settings** > **Keys** to view admin and query keys.
+
+:::image type="content" source="media/search-manage/azure-search-view-keys.png" alt-text="Screenshot of a portal page showing API keys." border="true":::
+
+### [**PowerShell**](#tab/azure-ps-find)
+
+1. Install the `Az.Search` module:
+
+   ```azurepowershell
+   Install-Module Az.Search
+   ```
+
+1. Return admin keys:
+
+   ```azurepowershell
+   Get-AzSearchAdminKeyPair -ResourceGroupName <resource-group-name> -ServiceName <search-service-name>
+   ```
+
+1. Return query keys:
+
+   ```azurepowershell
+   Get-AzSearchQueryKey -ResourceGroupName <resource-group-name> -ServiceName <search-service-name>
+   ```
+
+### [**Azure CLI**](#tab/azure-cli-find)
+
+Use the following commands to return admin and query API keys, respectively:
+
+```azurecli
+az search admin-key show --resource-group <myresourcegroup> --service-name <myservice>
+
+az search query-key list --resource-group <myresourcegroup> --service-name <myservice>
+```
+
+### [**REST API**](#tab/rest-find)
+
+Use [List Admin Keys](/rest/api/searchmanagement/admin-keys/get) or [List Query Keys](/rest/api/searchmanagement/query-keys/list-by-search-service) in the Management REST API to return API keys.
+
+You must have a [valid role assignment](#permissions-to-view-or-manage-keys) to return or update API keys. See [Manage your Azure AI Search service with REST APIs](search-manage-rest.md) for guidance on meeting role requirements using the REST APIs.
+
+```rest
+POST https://management.azure.com/subscriptions/{{subscriptionId}}/resourceGroups/{{resource-group}}/providers//Microsoft.Search/searchServices/{{search-service-name}}/listAdminKeys?api-version=2025-05-01
+```
+
+---
+
+## Use keys on connections
 
-API keys are used for data plane (content) requests, such as creating or accessing an index or, any other request that's represented in the [Search REST APIs](/rest/api/searchservice/). 
+API keys are used for data plane (content) requests, such as creating or accessing an index or any other request that's represented in the [Search Service REST APIs](/rest/api/searchservice/).
 
-You can use either an API key or [Azure roles](search-security-rbac.md) for control plane (service) requests. When you use an API key:
+You can use either an API key or [roles](search-security-rbac.md) for control plane (service) requests. When you use an API key:
 
 - Admin keys are used for creating, modifying, or deleting objects. Admin keys are also used to GET object definitions and system information, such as [LIST Indexes](/rest/api/searchservice/indexes/list) or [GET Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics).
 
@@ -146,81 +226,12 @@ More script examples for other operations can be found at [Quickstart: Create an
 
 ### [**Portal**](#tab/portal-use)
 
-Recall that key authentication is enabled by default and supports data plane operations such as indexing and queries. 
+Recall that key authentication is enabled by default and supports data plane operations such as indexing and queries.
 
 However, if you [disable API keys](search-security-enable-roles.md#disable-api-key-authentication) and set up role assignments, the Azure portal uses role assignments instead.
 
 ---
 
-## Permissions to view or manage API keys
-
-Permissions for viewing and managing API keys are conveyed through [role assignments](search-security-rbac.md). Members of the following roles can view and regenerate keys:
-
-+ Owner
-+ Contributor
-+ [Search Service Contributor](/azure/role-based-access-control/built-in-roles#search-service-contributor)
-+ Administrator and co-administrator (classic)
-
-The following roles don't have access to API keys:
-
-+ Reader
-+ Search Index Data Contributor
-+ Search Index Data Reader
-
-## Find existing keys
-
-You can view and manage API keys in the [Azure portal](https://portal.azure.com), or through [PowerShell](/powershell/module/az.search), [Azure CLI](/cli/azure/search), or [REST API](/rest/api/searchmanagement/).
-
-### [**Portal**](#tab/portal-find)
-
-1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
-
-1. Under **Settings**, select **Keys** to view admin and query keys.
-
-:::image type="content" source="media/search-manage/azure-search-view-keys.png" alt-text="Screenshot of a portal page showing API keys." border="true":::
-
-### [**PowerShell**](#tab/azure-ps-find)
-
-1. Install the `Az.Search` module:
-
-   ```azurepowershell
-   Install-Module Az.Search
-   ```
-
-1. Return admin keys:
-
-   ```azurepowershell
-   Get-AzSearchAdminKeyPair -ResourceGroupName <resource-group-name> -ServiceName <search-service-name>
-   ```
-
-1. Return query keys:
-
-   ```azurepowershell
-   Get-AzSearchQueryKey -ResourceGroupName <resource-group-name> -ServiceName <search-service-name>
-   ```
-
-### [**Azure CLI**](#tab/azure-cli-find)
-
-Use the following commands to return admin and query API keys, respectively:
-
-```azurecli
-az search admin-key show --resource-group <myresourcegroup> --service-name <myservice>
-
-az search query-key list --resource-group <myresourcegroup> --service-name <myservice>
-```
-
-### [**REST API**](#tab/rest-find)
-
-Use [List Admin Keys](/rest/api/searchmanagement/admin-keys/get) or [List Query Keys](/rest/api/searchmanagement/query-keys/list-by-search-service) in the Management REST API to return API keys.
-
-You must have a [valid role assignment](#permissions-to-view-or-manage-api-keys) to return or update API keys. See [Manage your Azure AI Search service with REST APIs](search-manage-rest.md) for guidance on meeting role requirements using the REST APIs.
-
-```rest
-POST https://management.azure.com/subscriptions/{{subscriptionId}}/resourceGroups/{{resource-group}}/providers//Microsoft.Search/searchServices/{{search-service-name}}/listAdminKeys?api-version=2025-05-01
-```
-
----
-
 ## Create query keys
 
 Query keys are used for read-only access to documents within an index for operations targeting a documents collection. Search, filter, and suggestion queries are all operations that take a query key. Any read-only operation that returns system data or object definitions, such as an index definition or indexer status, requires an admin key.
@@ -231,7 +242,7 @@ Restricting access and operations in client apps is essential to safeguarding th
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
 
-1. Under **Settings**, select **Keys** to view API keys.
+1. From the left pane, select **Settings** > **Keys** to view API keys.
 
 1. Under **Manage query keys**, use the query key already generated for your service, or create new query keys. The default query key isn't named, but other generated query keys can be named for manageability.
 
@@ -249,7 +260,7 @@ A script example showing query key usage can be found at [Create or delete query
 
 Use [Create Query Keys](/rest/api/searchmanagement/query-keys/create) in the Management REST API.
 
-You must have a [valid role assignment](#permissions-to-view-or-manage-api-keys) to create or manage API keys. See [Manage your Azure AI Search service with REST APIs](search-manage-rest.md) for guidance on meeting role requirements using the REST APIs.
+You must have a [valid role assignment](#permissions-to-view-or-manage-keys) to create or manage API keys. See [Manage your Azure AI Search service with REST APIs](search-manage-rest.md) for guidance on meeting role requirements using the REST APIs.
 
 ```rest
 POST https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}/createQueryKey/{name}?api-version=2025-05-01
@@ -263,45 +274,49 @@ POST https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/
 
 Two admin keys are created for each service so that you can rotate a primary key while using the secondary key for business continuity.
 
-1. Under **Settings**, select **Keys**, then copy the secondary key.
+1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
+
+1. From the left pane, select **Settings** > **Keys**.
+
+1. Copy the secondary key.
 
 1. For all applications, update the API key settings to use the secondary key.
 
 1. Regenerate the primary key.
 
 1. Update all applications to use the new primary key.
 
-If you inadvertently regenerate both keys at the same time, all client requests using those keys will fail with HTTP 403 Forbidden. However, content isn't deleted and you aren't locked out permanently. 
+If you inadvertently regenerate both keys at the same time, all client requests using those keys will fail with HTTP 403 Forbidden. However, content isn't deleted and you aren't locked out permanently.
 
-You can still access the service through the Azure portal or programmatically. Management functions are operative through a subscription ID not a service API key, and are thus still available even if your API keys aren't. 
+You can still access the service through the Azure portal or programmatically. Management functions are operative through a subscription ID not a service API key, and are thus still available even if your API keys aren't.
 
 After you create new keys via portal or management layer, access is restored to your content (indexes, indexers, data sources, synonym maps) once you provide those keys on requests.
 
-## Secure API keys
+## Secure keys
 
 Use role assignments to restrict access to API keys.
 
 It's not possible to use [customer-managed key encryption](search-security-manage-encryption-keys.md) to encrypt API keys. Only sensitive data within the search service itself (for example, index content or connection strings in data source object definitions) can be CMK-encrypted.
 
-1. Navigate to your search service page in Azure portal.
+1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
 
-1. On the left pane, select **Access control (IAM)**, and then select the **Role assignments** tab.
+1. From the left pane, select **Access control (IAM)**, and then select the **Role assignments** tab.
 
 1. In the **Role** filter, select the roles that have permission to view or manage keys (Owner, Contributor, Search Service Contributor). The resulting security principals assigned to those roles have key permissions on your search service.
 
 1. As a precaution, also check the **Classic administrators** tab to determine whether administrators and co-administrators have access.
 
 ## Best practices
 
-+ For production workloads, switch to [Microsoft Entra ID and role-based access](keyless-connections.md). Or, if you want to continue using API keys, be sure to always monitor [who has access to your API keys](#secure-api-keys) and [regenerate API keys](#regenerate-admin-keys) on a regular cadence.
++ For production workloads, switch to [Microsoft Entra ID and role-based access](keyless-connections.md). Alternatively, if you want to continue using API keys, be sure to always monitor [who has access to your API keys](#secure-keys) and [regenerate API keys](#regenerate-admin-keys) on a regular cadence.
 
-+ Only use API keys if data disclosure isn't a risk (for example, when using sample data) and if you're operating behind a firewall. Exposure of API keys is a risk to both data and to unauthorized use of your search service. 
++ Only use API keys if data disclosure isn't a risk (for example, when using sample data) and if you're operating behind a firewall. Exposing API keys puts both your data and your search service at risk of unauthorized use.
 
 + If you use an API key, store it securely somewhere else, such as in [Azure Key Vault](/azure/key-vault/general/overview). Don't include the API key directly in your code, and never post it publicly.
 
 + Always check code, samples, and training material before publishing to make sure you don't inadvertently expose an API key.
 
-## See also
+## Related content
 
 + [Security in Azure AI Search](search-security-overview.md)
 + [Azure role-based access control in Azure AI Search](search-security-rbac.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIキーを使用した接続に関するドキュメントの更新"
}
```

### Explanation
この変更は、APIキーを使用してAzure AI Searchに接続する方法に関するドキュメントに大幅な更新が加えられたことを示しています。主要な更新内容には、ドキュメントのメタデータや構成の変更、暗号化オプションに関する情報の追加が含まれています。

具体的には、APIキーの定義や使用法についての詳細が改善され、認証方法としての役割ベースのアクセスに移行する際の考慮事項や推奨されるセキュリティプラクティスが追加されました。また、APIキーの管理や確認方法に関する部分がより詳細になり、管理の利便性が向上しています。

特に、キーの使用や管理に関するロールマッピングが強調されており、ユーザーがどのキーがどのような権限に関連しているかを理解しやすくなっています。これにより、ユーザがAPIキーを安全に管理し、誤った情報漏洩を防ぐためのガイダンスが強化されています。

全体として、この更新はユーザーがAPIキーを使用する際のセキュリティリスクを低減し、Azure AI Searchサービスの安全な利用を促進することを目的としています。


