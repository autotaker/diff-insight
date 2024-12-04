---
date: '2024-12-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3b6e85f...MicrosoftDocs:2c6389f
summary: このコード変更は、Azure AI 検索の関連ドキュメントに対するいくつかのマイナーな更新を含んでおり、内容の明確化を図っています。主な変更点は、新しい情報の追加、セキュリティの強調、認証方法の更新、文書表現の明確化です。破壊的な変更はありませんが、ユーザーの設定に影響を与える可能性のある新しい認証方法への言及が追加されています。また、各ドキュメントの日付を最新に更新し、手順の簡略化も行われています。特に、APIキーからMicrosoft
  Entra ID認証への切り替えを強調し、名称を「Keyless authentication」から「Connect without keys」に変更することで、ユーザーの理解を深める工夫がなされています。全体として、この変更はユーザー体験の向上に寄与することを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3b6e85f...MicrosoftDocs:2c6389f){target="_blank"}

# ハイライト

このコード変更は、Azure AI 検索の関連ドキュメントに対するいくつかのマイナーな更新を含んでおり、最新の情報に基づいた内容の明確化を旨としています。主なハイライトとして、新しい情報の追加、セキュリティの強調、認証方法の更新、および文書の表現の明確化などがあります。

## 新機能

- 特に言及すべき新機能はありませんが、文書の改訂を通じてユーザーの理解を深めるための改善が行われています。

## 破壊的変更

- 破壊的な変更はありません。ただし、新しい認証方法への言及が追加され、ユーザーの設定に関する変更が促される可能性があります。

## その他の更新

- 各ドキュメントにおける日付が最新のものに更新されています。
- チュートリアルやガイドでは、表現の明確化や手順の簡略化がされています。
- 認証方法に関して、APIキーからアクセストークンへの切り替えを強調した記述が追加されています。

# インサイト

このコードの変更は、Azure AI 検索のドキュメントにおいて、より具体的で直感的な利用ガイドを提供するための重要な調整を行っています。ユーザーが新しい情報に迅速にアクセスできるようにし、最新のセキュリティ対策や設定が適用されることを目的として、内容の鮮度と整合性を保つためのアプローチが見受けられます。

特に、APIキーの代替としてのMicrosoft Entra ID認証を通じた接続の強調は、セキュリティを重視する現代的なアプローチを反映しています。この変更は、多くのユーザーにとってより安全で管理しやすい認証手段に移行させるポジティブな動機付けとなるでしょう。

また、「Keyless authentication」から「Connect without keys」への名称変更は、意図的に分かりやすさを追求したものであり、ユーザーが必要とする具体的な操作を明示する上で重要な役割を果たします。こうした調整は、技術の利用者がよりスムーズにサービスを活用できるようにすることを目的としており、ユーザー体験の向上に寄与します。全体として、この一連の変更は、ユーザーにとっての利便性を優先した戦略的な文書改善と位置づけることができます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-debug-session.md](#item-edf092) | minor update | コグニティブ検索デバッグセッションの更新 | modified | 5 | 5 | 10 | 
| [cognitive-search-how-to-debug-skillset.md](#item-31db42) | minor update | コグニティブ検索スキルセットのデバッグ方法に関する更新 | modified | 13 | 25 | 38 | 
| [cognitive-search-tutorial-debug-sessions.md](#item-7e10e9) | minor update | デバッグセッションを使用したスキルセット修正のチュートリアル更新 | modified | 1 | 1 | 2 | 
| [search-get-started-rbac.md](#item-9d96c1) | minor update | RBACを使用したAzure AI検索のクイックスタート文書の更新 | modified | 12 | 14 | 26 | 
| [search-get-started-vector.md](#item-4984d9) | minor update | ベクトル検索のクイックスタート文書の改訂 | modified | 37 | 99 | 136 | 
| [toc.yml](#item-c4768f) | minor update | 目次における認証方法の名称変更 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/cognitive-search-debug-session.md{#item-edf092}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 10/01/2024
+ms.date: 12/03/2024
 ---
 
 # Debug Sessions in Azure AI Search
@@ -29,13 +29,13 @@ Use Debug Sessions to investigate and resolve problems with:
 
 + Custom skills used to integrate external processing that you provide.
 
-Compare the following debug session images for the first two scenarios. For both scenarios, the surface area shows the progression of skills that generate or transform content en route from the source document to the search index. The flow includes index mapping options, and you can trace the arrows to follow the processing trail. The details pane to the right is context-sensitive. It shows a representation of the enriched document, or the details of a skill or mapping.
+Compare the following debug session images for the first two scenarios. For both scenarios, the surface area shows the progression of skills that generate or transform content en route from the source document to the search index. The flow includes index mapping options, and you can trace the arrows to follow the processing trail. The details pane to the right is context-sensitive. It shows a representation of the enriched document that's created by the pipeline, or the details of a skill or mapping.
 
-The first image shows a pattern for applied AI enrichment. Skills can run sequentially or in parallel if there are no dependencies. Output field mappings send enriched or generated content from in-memory data structures to fields in an index. 
+The first image shows a pattern for applied AI enrichment (no vectors). Skills can run sequentially or in parallel if there are no dependencies. Index mappings show how enriched or generated content travels from in-memory data structures to fields in an index. Enriched document shows the data structure that the skillset creates.
 
 :::image type="content" source="media/cognitive-search-debug/debug-session-flow-applied-ai.png" alt-text="Screenshot of a debug session for OCR and image analysis." lightbox="media/cognitive-search-debug/debug-session-flow-applied-ai.png":::
 
-The second image shows a typical pattern for integrated vectorization. Skills for integrated vectorization usually includes Text Split and an embedding skill. A Text Split skill chunks a document into pages. An embedding skills provides vectorization. Projection mappings control how chunks of content are index. This particular skillset skips the parent index and creates an index of just chunked content, using metadata to identify the source of the chunk.
+The second image shows a typical pattern for integrated vectorization. Skills for integrated vectorization usually include a Text Split skill and an embedding skill. A Text Split skill divides a document into chunks. An embedding skill calls an embedding API to vectorize those chunks. This particular skillset chunks content into an array of "pages". For integrated vectorization, projection mappings control how chunks are mapped to fields in the index.
 
 :::image type="content" source="media/cognitive-search-debug/debug-session-flow-integrated-vectorization.png" alt-text="Screenshot of a debug session for integrated vectorization." lightbox="media/cognitive-search-debug/debug-session-flow-integrated-vectorization.png":::
 
@@ -53,7 +53,7 @@ Debug Sessions work with all generally available [indexer data sources](search-d
 
 + For custom skills, a user-assigned managed identity isn't supported for a debug session connection to Azure Storage. As stated in the prerequisites, you can use a system managed identity, or specify a full access connection string that includes a key. For more information, see [Connect a search service to other Azure resources using a managed identity](search-howto-managed-identities-data-sources.md).
 
-+ Currently, the ability to select which document to debug is unavailable. This limitation is not permanent and will be lifted soon. At this time, Debug Sessions selects the first document in the source data container or folder.
++ Currently, the ability to select which document to debug is unavailable. This limitation isn't permanent and will be lifted soon. At this time, Debug Sessions selects the first document in the source data container or folder.
 
 ## How a debug session works
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブ検索デバッグセッションの更新"
}
```

### Explanation
この変更は、Azure AI 検索におけるデバッグセッションに関するドキュメントの修正を反映しています。主な修正点は、日付の更新といくつかの表現の明確化です。具体的には、最初の修正では`ms.date`が2024年10月1日から2024年12月3日に変更され、デバッグセッションに関連する情報が洗練されています。これにより、読者に対してより明確で正確な内容が提供されます。また、文中のいくつかのフレーズが修正され、特に「生成された文書」に関連する説明が強化されています。このような変更は、ユーザーがドキュメントの内容をよりよく理解し、利用できるようにするための重要なステップです。

## articles/search/cognitive-search-how-to-debug-skillset.md{#item-31db42}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 10/01/2024
+ms.date: 12/03/2024
 ---
 
 # Debug an Azure AI Search skillset in Azure portal
@@ -23,17 +23,15 @@ For background on how a debug session works, see [Debug sessions in Azure AI Sea
 
 ## Prerequisites
 
-+ An Azure AI Search service. We recommend using a system-assigned managed identity and role assignments that allow Azure AI Search to write to Azure Storage and call the Azure AI resources used in the skillset.
++ An Azure AI Search service, any region or tier.
 
 + An Azure Storage account, used to save session state.
 
 + An existing enrichment pipeline, including a data source, a skillset, an indexer, and an index. 
 
-+ For role assignments, the search service identity must have:
+## Security and permissions
 
-  + **Cognitive Services User** permissions on the Azure AI multiservice account used by the skillset.
-
-  + **Storage Blob Data Contributor** permissions on Azure Storage. Otherwise, plan on using a full access connection string for the debug session connection to Azure Storage.
++ To save a debug session to Azure storage, the search service identity must have **Storage Blob Data Contributor** permissions on Azure Storage. Otherwise, plan on choosing a full access connection string for the debug session connection to Azure Storage.
 
 + If the Azure Storage account is behind a firewall, configure it to [allow search service access](search-indexer-howto-access-ip-restricted.md).
 
@@ -51,8 +49,6 @@ Debug sessions work with all generally available [indexer data sources](search-d
 
 + For custom skills, a user-assigned managed identity isn't supported for a debug session connection to Azure Storage. As stated in the prerequisites, you can use a system managed identity, or specify a full access connection string that includes a key. For more information, see [Connect a search service to other Azure resources using a managed identity](search-howto-managed-identities-data-sources.md).
 
-+ Currently, the ability to select which document to debug is unavailable. This limitation is not permanent and will be lifted soon. At this time, Debug Sessions selects the first document in the source data container or folder.
-
 ## Create a debug session
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
@@ -67,33 +63,25 @@ Debug sessions work with all generally available [indexer data sources](search-d
 
 1. In **Indexer template**, select the indexer that drives the skillset you want to debug. Copies of both the indexer and skillset are used to initialize the session.
 
-1. In **Storage account**, find a general-purpose storage account for caching the debug session.
+1. In **Document to debug**, choose the first document in the index or select a specific document. If you select a specific document, depending on the data source, you're asked for a URI or a row ID.
+
+   If your specific document is a blob, provide the blob URI. You can find the URI in the blob property page in the portal.
 
-1. Select **Authenticate using managed identity** if you previously assigned **Storage Blob Data Contributor** permissions to the search service system-managed identity.
+   :::image type="content" source="media/cognitive-search-debug/copy-blob-url.png" lightbox="media/cognitive-search-debug/copy-blob-url.png" alt-text="Screenshot of the URI property in blob storage." border="true":::
+
+1. In **Storage account**, choose a general-purpose storage account for caching the debug session.
+
+1. Select **Authenticate using managed identity** if you previously assigned **Storage Blob Data Contributor** permissions to the search service system-managed identity. If you don't check this box, the search service connects using a full access connection string.
 
 1. Select **Save**.
 
    + Azure AI Search creates a blob container on Azure Storage named *ms-az-cognitive-search-debugsession*.
    + Within that container, it creates a folder using the name you provided for the session name.
    + It starts your debug session.
 
-1. A debug session opens to the settings page. You can make modifications to the initial configuration and override any defaults.
-
-1. In **Storage connection string**, you can specify the connection string or change the storage account. 
-
-   <!-- 1. In **Document to debug**, choose the first document in the index or select a specific document. If you select a specific document, depending on the data source, you're asked for a URI or a row ID.
-
-   If your specific document is a blob, provide the blob URI. You can find the URI in the blob property page in the portal.
-
-   :::image type="content" source="media/cognitive-search-debug/copy-blob-url.png" lightbox="media/cognitive-search-debug/copy-blob-url.png" alt-text="Screenshot of the URI property in blob storage." border="true"::: -->
-
-1. Optionally, in **Indexer settings**, specify any [indexer execution settings](search-howto-indexing-azure-blob-storage.md) used to create the session. The settings should mirror the settings used by the actual indexer. Any indexer options that you specify in a debug session have no effect on the indexer itself.
-
-1. If you made changes, select **Save session**, followed by **Run**.
-
 The debug session begins by executing the indexer and skillset on the selected document. The document's content and metadata are visible and available in the session.
 
-A debug session can be canceled while it's executing using the **Cancel** button. If you hit the **Cancel** button you should be able to analyze partial results.
+A debug session can be canceled while it's executing. If you hit the **Cancel** button you should be able to analyze partial results.
 
 It's expected for a debug session to take longer to execute than the indexer since it goes through extra processing. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブ検索スキルセットのデバッグ方法に関する更新"
}
```

### Explanation
この変更は、Azure ポータルにおけるコグニティブ検索スキルセットのデバッグ方法に関するドキュメントを更新したものです。主な修正点は、日付の変更（2024年10月1日から2024年12月3日へ）と、デバッグセッションを実行するための要件の明確化です。具体的には、Azure AI 検索サービスや Azure ストレージアカウントに関する情報が簡略化され、必要な権限や設定が整理されています。

特に、セキュリティと権限セクションが追加され、デバッグセッションを Azure ストレージに保存するために必要な「Storage Blob Data Contributor」権限について詳細が記載されています。加えて、特定の文書をデバッグするための手順が更新され、ユーザーが文書を選択する際の流れがより明確になっています。

このような改善により、ユーザーはデバッグセッションを効果的に設定し、実行できるようになります。また、ユーザーが直面する可能性のある制限や選択肢についても詳しい情報が提供されており、利便性が向上しています。

## articles/search/cognitive-search-tutorial-debug-sessions.md{#item-7e10e9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: tutorial
-ms.date: 08/20/2024
+ms.date: 12/03/2024
 ---
 
 # Tutorial: Fix a skillset using Debug Sessions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デバッグセッションを使用したスキルセット修正のチュートリアル更新"
}
```

### Explanation
この変更は、デバッグセッションを使用してスキルセットを修正するためのチュートリアルにおいて、日付の更新を行ったものです。具体的には、`ms.date`が2024年8月20日から2024年12月3日に変更されました。この更新により、チュートリアルが最新の情報に合わせて調整され、利用者にとって関連性の高い内容となります。全体として、ドキュメントの内容は安定しており、ユーザーがチュートリアルにアクセスする際の参考となる情報が提供されています。

## articles/search/search-get-started-rbac.md{#item-9d96c1}

<details>
<summary>Diff</summary>
````diff
@@ -7,12 +7,12 @@ ms.author: heidist
 ms.service: azure-ai-search
 
 ms.topic: quickstart
-ms.date: 11/29/2024
+ms.date: 12/03/2024
 ---
 
 # Quickstart: Connect without keys
 
-Configure Azure AI Search to use Microsoft Entra ID authentication and role-based access control (RBAC) so that you can connect from your local system with your personal identity, using Jupyter notebooks or a REST client to interact with your search service.
+Configure Azure AI Search to use Microsoft Entra ID authentication and role-based access control (RBAC) so that you can connect from your local system without API keys, using Jupyter notebooks or a REST client to interact with your search service.
 
 If you stepped through other quickstarts that connect using API keys, this quickstart shows you how to switch to identity-based authentication so that you can avoid hard-coded keys in your example code.
 
@@ -34,7 +34,7 @@ You need this step if you have more than one subscription or tenant.
 
    1. Notice the subscription name and ID in **Overview** > **Essentials**.
 
-   1. Now select the subscription name to confirm the parent management group (tenant ID) on the next page.
+   1. Now select the subscription name to show the parent management group (tenant ID) on the next page.
 
       :::image type="content" source="media/search-get-started-rbac/select-subscription-name.png" lightbox="media/search-get-started-rbac/select-subscription-name.png" alt-text="Screenshot of the portal page providing the subscription name":::
 
@@ -52,12 +52,6 @@ You need this step if you have more than one subscription or tenant.
     az login --tenant <your-tenant-id>
    ```
 
-1. Verify your tenant ID:
-
-   ```azurecli
-   az account show --query tenantId --output tsv
-   ```
-
 ## Step 2: Configure Azure AI Search for RBAC
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and navigate to your Azure AI Search service.
@@ -122,19 +116,21 @@ az login
 
 ### Using a REST client
 
-[Several quickstarts](search-get-started-vector.md) and tutorials use a REST client, such as Visual Studio Code with the REST extension. Here's how you connect to Azure AI Search from Visual Studio Code.
+Several quickstarts and tutorials use a REST client, such as Visual Studio Code with the REST extension. Here's how you connect to Azure AI Search from Visual Studio Code.
+
+You should have a `.rest` or `.http` file, similar to the one described in [Quickstart: Vector search](search-get-started-vector.md).
 
-1. Get a personal identity token:
+1. Get an access token:
 
    ```azurecli
    az account get-access-token --scope https://search.azure.com/.default --query accessToken --output tsv
    ```
 
-1. Set variables used for the connection, pasting the full search service endpoint and the token you got in the previous step. Make sure neither value is quote-enclosed.
+1. At the top of your file, set variables used for the connection, pasting the full search service endpoint and the access token you got in the previous step. Your variables should look similar to the following example. Notice the values aren't quote-enclosed.
 
     ```REST
-    @baseUrl = PUT-YOUR-SEARCH-SERVICE-URL-HERE
-    @token = PUT-YOUR-PERSONAL-IDENTITY-TOKEN-HERE
+    @baseUrl = https://contoso.search.search.windows.net
+    @token = <a long GUID>
     ```
 
 1. Specify the authorization bearer token in a REST call:
@@ -153,6 +149,8 @@ az login
          }
    ```
 
+If the call fails, revisit the previous steps to make sure you didn't skip any. You might also want to restart your device.
+
 ## Additional configuration
 
 Configure a managed identity for outbound connections:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACを使用したAzure AI検索のクイックスタート文書の更新"
}
```

### Explanation
このコードの変更は、Azure AI検索サービスのロールベースのアクセス制御（RBAC）を使用したクイックスタートチュートリアルの文書を更新したものです。主な変更点は日付の更新（2024年11月29日から2024年12月3日へ）と、接続方法に関する記述の修正です。特に、APIキーを使用せずにMicrosoft Entra ID認証を通じて接続することの強調が追加されました。

内容については、Azure AI検索に接続するための手順が簡略化され、一部の説明がより明確になっています。具体的には、「個人IDトークン」を「アクセストークン」に変更し、必要なトークンを取得する手順が具体的に示されています。また、接続に使用する変数の設定についても、より具体的な例が提供されています。

これにより、ユーザーはAzure AI検索サービスによりスムーズに接続できる情報が得られ、チュートリアルの実用性が向上しています。加えて、エラーハンドリングについても注意を促す文言が追加され、ユーザーが手順を漏れなく確認できるよう配慮されています。

## articles/search/search-get-started-vector.md{#item-4984d9}

<details>
<summary>Diff</summary>
````diff
@@ -8,14 +8,14 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: quickstart
-ms.date: 10/31/2024
+ms.date: 12/03/2024
 ---
 
 # Quickstart: Vector search by using REST
 
 Learn how to use the [Search REST APIs](/rest/api/searchservice) to create, load, and query vectors in Azure AI Search.
 
-In Azure AI Search, a [vector store](vector-store.md) has an index schema that defines vector and nonvector fields, a vector configuration for algorithms that create the embedding space, and settings on vector field definitions that are used in query requests. The [Create Index](/rest/api/searchservice/indexes/create-or-update) API creates the vector store.
+In Azure AI Search, a [vector store](vector-store.md) has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. The [Create Index](/rest/api/searchservice/indexes/create-or-update) REST API creates the vector store.
 
 If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
 
@@ -24,106 +24,49 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 
 ## Prerequisites
 
-- [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client). If you need help with getting started, see [Quickstart: Text search using REST](search-get-started-rest.md).
+- [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
 - [Azure AI Search](search-what-is-azure-search.md), in any region and on any tier. You can use the Free tier for this quickstart, but Basic or higher is recommended for larger data files. [Create](search-create-service-portal.md) or [find an existing Azure AI Search resource](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) under your current subscription.
 
   Most existing services support vector search. For a small subset of services created prior to January 2019, an index that contains vector fields fails on creation. In this situation, a new service must be created.
 
 - Optionally, to run the query example that invokes [semantic reranking](semantic-search-overview.md), your search service must be the Basic tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
-- Optionally, an [Azure OpenAI](https://aka.ms/oai/access) resource with a deployment of `text-embedding-ada-002`. The source `.rest` file includes an optional step for generating new text embeddings, but we provide pregenerated embeddings so that you can omit this dependency.
-
 ## Download files
 
 [Download a REST sample](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) from GitHub to send the requests in this quickstart. For more information, see [Downloading files from GitHub](https://docs.github.com/get-started/start-your-journey/downloading-files-from-github).
 
 You can also start a new file on your local system and create requests manually by using the instructions in this article.
 
-## Get a search service endpoint
+## Get a search endpoint and an API key
+
+You can find the search service endpoint and API keys in the Azure portal. You're pasting these values into a `.rest` or `.http` file in the next step.
 
-You can find the search service endpoint in the Azure portal.
+Requests to the search endpoint must be authenticated and authorized. You can use API keys or roles for this task. Keys are easier to start with, but roles are more secure. Although we use API keys for this quickstart, we recommend [switching to a keyless connection](search-get-started-rbac.md).
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
 
 1. On the **Overview** home page, find the URL. An example endpoint might look like `https://mydemo.search.windows.net`. 
 
    :::image type="content" source="media/search-get-started-rest/get-endpoint.png" lightbox="media/search-get-started-rest/get-endpoint.png" alt-text="Screenshot of the URL property on the overview page.":::
 
-You're pasting this endpoint into the `.rest` or `.http` file in a later step.
-
-## Configure access
-
-Requests to the search endpoint must be authenticated and authorized. You can use API keys or roles for this task. Keys are easier to start with, but roles are more secure.
-
-For a role-based connection, the following instructions have you connecting to Azure AI Search under your identity, not the identity of a client app.
-
-### Option 1: Use keys
-
-Select **Settings** > **Keys** and then copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one. For more information, see [Connect to Azure AI Search using key authentication](search-security-api-keys.md).
-
-:::image type="content" source="media/search-get-started-rest/get-api-key.png" lightbox="media/search-get-started-rest/get-api-key.png" alt-text="Screenshot that shows the API keys in the Azure portal.":::
-
-You're pasting this key into the `.rest` or `.http` file in a later step.
-
-### Option 2: Use roles
-
-Make sure your search service is [configured for role-based access](search-security-enable-roles.md). You must have preconfigured [role-assignments for developer access](search-security-rbac.md#assign-roles-for-development). Your role assignments must grant permission to create, load, and query a search index. 
-
-In this section, obtain your personal identity token using either the Azure CLI, Azure PowerShell, or the Azure portal. 
-
-#### [Azure CLI](#tab/azure-cli)
-
-1. Sign in to Azure CLI.
-
-    ```azurecli
-    az login
-    ```
-
-1. Get your personal identity token.
-
-    ```azurecli
-    az account get-access-token --scope https://search.azure.com/.default
-    ```
-
-#### [Azure PowerShell](#tab/azure-powershell)
-
-1. Sign in with PowerShell.
-
-    ```azurepowershell
-    Connect-AzAccount
-    ```
-
-1. Get your personal identity token.
-
-    ```azurepowershell
-    Get-AzAccessToken -ResourceUrl https://search.azure.com
-    ```
-
-#### [Azure portal](#tab/portal)
+1. Select **Settings** > **Keys**. Either **API keys** or **Both** must be enabled. [Admin API keys](search-security-api-keys.md) are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
 
-Use the steps found here: [find the user object ID](/partner-center/find-ids-and-domain-names#find-the-user-object-id) in the Azure portal.
-
----
-
-You're pasting your personal identity token into the `.rest` or `.http` file in a later step.
-
-> [!NOTE]
-> This section assumes you're using a local client that connects to Azure AI Search on your behalf. An alternative approach is [getting a token for the client app](/entra/identity-platform/v2-oauth2-client-creds-grant-flow), assuming your application is [registered](/entra/identity-platform/quickstart-register-app) with Microsoft Entra ID.
+   :::image type="content" source="media/search-get-started-rest/get-api-key.png" lightbox="media/search-get-started-rest/get-api-key.png" alt-text="Screenshot that shows the API keys in the Azure portal.":::
 
 ## Create a vector index
 
 [Create Index (REST)](/rest/api/searchservice/indexes/create) creates a vector index and sets up the physical data structures on your search service.
 
 The index schema is organized around hotel content. Sample data consists of vector and nonvector names and descriptions of seven fictitious hotels. This schema includes configurations for vector indexing and queries, and for semantic ranking.
 
-1. Open a new text file in Visual Studio Code.
+1. Create a new text file in Visual Studio Code.
 
-1. Set variables to the values you collected earlier. This example uses a personal identity token.
+1. At the top of the file, add variables for the values you collected earlier.
 
    ```http
    @baseUrl = PUT-YOUR-SEARCH-SERVICE-URL-HERE
-   @token = PUT-YOUR-PERSONAL-IDENTITY-TOKEN-HERE
+   @apiKey = PUT-YOUR-ADMIN-KEY-HERE
    ```
 
 1. Save the file with a `.rest` or `.http` file extension.
@@ -134,7 +77,7 @@ The index schema is organized around hotel content. Sample data consists of vect
     ### Create a new index
     POST {{baseUrl}}/indexes?api-version=2023-11-01  HTTP/1.1
         Content-Type: application/json
-        Authorization: Bearer {{token}}
+        api-key: {{apiKey}}
     
     {
         "name": "hotels-vector-quickstart",
@@ -237,23 +180,6 @@ The index schema is organized around hotel content. Sample data consists of vect
                         "efSearch": 500,
                         "metric": "cosine"
                     }
-                },
-                {
-                    "name": "my-hnsw-vector-config-2",
-                    "kind": "hnsw",
-                    "hnswParameters": 
-                    {
-                        "m": 4,
-                        "metric": "euclidean"
-                    }
-                },
-                {
-                    "name": "my-eknn-vector-config",
-                    "kind": "exhaustiveKnn",
-                    "exhaustiveKnnParameters": 
-                    {
-                        "metric": "cosine"
-                    }
                 }
             ],
             "profiles": [      
@@ -284,13 +210,16 @@ The index schema is organized around hotel content. Sample data consists of vect
     }
     ```
 
-1. Select **Send request**. Recall that you need the REST client to send requests. You should have an `HTTP/1.1 201 Created` response. The response body should include the JSON representation of the index schema.
+1. Save the file again, and then select **Send request**. You should have an `HTTP/1.1 201 Created` response. The response body should include the JSON representation of the index schema.
 
-    Key points:
+    Key takeaways about this REST API:
 
     - The `fields` collection includes a required key field and text and vector fields (such as `Description` and `DescriptionVector`) for text and vector search. Colocating vector and nonvector fields in the same index enables hybrid queries. For instance, you can combine filters, text search with semantic ranking, and vectors into a single query operation.
+
     - Vector fields must be `type: Collection(Edm.Single)` with `dimensions` and `vectorSearchProfile` properties.
+
     - The `vectorSearch` section is an array of approximate nearest neighbor algorithm configurations and profiles. Supported algorithms include hierarchical navigable small world and exhaustive k-nearest neighbor. For more information, see [Relevance scoring in vector search](vector-search-ranking.md).
+
     - [Optional]: The `semantic` configuration enables reranking of search results. You can rerank results in queries of type `semantic` for string fields that are specified in the configuration. To learn more, see [Semantic ranking overview](semantic-search-overview.md).
 
 ## Upload documents
@@ -302,11 +231,15 @@ The URI is extended to include the `docs` collection and the `index` operation.
 > [!IMPORTANT]
 > The following example isn't runnable code. For readability, we excluded vector values because each one contains 1,536 embeddings, which is too long for this article. If you want to try this step, copy runnable code from the [sample on GitHub](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors).
 
+1. Paste in a valid request that uploads documents, similar to the example below.
+
+1. Save the file, and then select **Send request**. You should have an `HTTP/1.1 201 Created` response. The response body should include the JSON representation of the search documents.
+
 ```http
 ### Upload documents
 POST {{baseUrl}}/indexes/hotels-quickstart-vectors/docs/index?api-version=2023-11-01  HTTP/1.1
 Content-Type: application/json
-Authorization: Bearer {{token}}
+api-key: {{apiKey}}
 
 {
     "value": [
@@ -434,9 +367,10 @@ Authorization: Bearer {{token}}
 }
 ```
 
-Key points:
+Key takeaways about this REST API:
 
 - Documents in the payload consist of fields defined in the index schema.
+
 - Vector fields contain floating point values. The dimensions attribute has a minimum of 2 and a maximum of 3,072 floating point values each. This quickstart sets the dimensions attribute to 1,536 because that's the size of embeddings generated by the Azure OpenAI **text-embedding-ada-002** model.
 
 ## Run queries
@@ -462,13 +396,13 @@ The vector query string is semantically similar to the search string, but it inc
 
 ### Single vector search
 
-1. Paste in a POST request to query the search index. Then select **Send request**. The URI is extended to include the `/docs/search` operator.
+1. Paste in a POST request to query the search index. Save the file. Then select **Send request**. The URI is extended to include the `/docs/search` operator.
 
     ```http
     ### Run a query
     POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2023-11-01  HTTP/1.1
         Content-Type: application/json
-        Authorization: Bearer {{token}}
+        api-key: {{apiKey}}
         
         {
             "count": true,
@@ -547,7 +481,7 @@ You can add filters, but the filters are applied to the nonvector content in you
     ### Run a vector query with a filter
     POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2023-11-01  HTTP/1.1
         Content-Type: application/json
-        Authorization: Bearer {{token}}
+        api-key: {{apiKey}}
     
         {
             "count": true,
@@ -620,7 +554,7 @@ Hybrid search consists of keyword queries and vector queries in a single search
     ### Run a hybrid query
     POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2023-11-01  HTTP/1.1
         Content-Type: application/json
-        Authorization: Bearer {{token}}
+        api-key: {{apiKey}}
         
     {
         "count": true,
@@ -767,7 +701,7 @@ Here's the last query in the collection. This hybrid query with semantic ranking
     ### Run a hybrid query
     POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2023-11-01  HTTP/1.1
         Content-Type: application/json
-        Authorization: Bearer {{token}}
+        api-key: {{apiKey}}
 
     {
         "count": true,
@@ -854,10 +788,12 @@ Here's the last query in the collection. This hybrid query with semantic ranking
     }
     ```
 
-    Key points:
+    Key takeaways about this REST API:
 
     - Vector search is specified through the `vectors.value` property. Keyword search is specified through the `search` property.
+
     - In a hybrid search, you can integrate vector search with full-text search over keywords. Filters, spell check, and semantic ranking apply to textual content only, and not vectors. In this final query, there's no semantic `answer` because the system didn't produce one that was sufficiently strong.
+
     - Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
 
 ## Clean up
@@ -872,9 +808,11 @@ You can also try this `DELETE` command:
 ### Delete an index
 DELETE  {{baseUrl}}/indexes/hotels-vector-quickstart?api-version=2023-11-01 HTTP/1.1
     Content-Type: application/json
-    Authorization: Bearer {{token}}
+    api-key: {{apiKey}}
 ```
 
 ## Next steps
 
-As a next step, we recommend that you review the demo code for [Python](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python), [C#](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet), or [JavaScript](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript).
+As a next step, we recommend learning how to invoke REST API calls [without API keys](search-get-started-rbac.md).
+
+You might also want to review the demo code for [Python](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python), [C#](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet), or [JavaScript](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のクイックスタート文書の改訂"
}
```

### Explanation
この変更は、Azure AI検索におけるベクトル検索のクイックスタートガイドのアップデートを反映しています。主な修正点としては、日付の更新（2024年10月31日から2024年12月3日への変更）が含まれており、文中のいくつかの表現も明確化されています。

具体的には、ベクトル検索の構成やリクエストの形式、新たな手順が追加されています。特に「アクセストークン」から「APIキー」に変更され、APIリクエストの認証方法に関する整合性が向上しています。他にも、ベクトルインデックスの作成やドキュメントのアップロード手順が簡略化され、ユーザーがより直感的に理解できるように情報が整理されています。

また、APIリクエストの例が整理され、関連する重要なポイントや注意事項も詳しく説明されているため、実際の作業を行う際の指針が得やすくなっています。最後に、次のステップとして、APIキー以外の方法での接続についてのリンクが提供されているため、よりセキュアなアクセス方法の導入も促されています。全体的に、ユーザーが迅速かつ効果的にAzure AI検索のベクトル機能を活用できるように配慮された更新といえます。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ items:
     href: search-get-started-semantic.md
   - name: Chat with your data 
     href: /azure/ai-services/openai/use-your-data-quickstart?context=/azure/search/context/context
-  - name: Keyless authentication
+  - name: Connect without keys
     href: search-get-started-rbac.md
   - name: Portal
     items:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次における認証方法の名称変更"
}
```

### Explanation
この変更は、Azure AI検索の目次ファイル（toc.yml）における項目の名前を更新しています。具体的には、「Keyless authentication」というタイトルが「Connect without keys」に変更されました。この変更は、キーを使用しない接続方法を明確にし、ユーザーに理解しやすい用語を用いることを目的としています。

変更の内容は、ごくわずかながら重要な意味を持っています。新しい名称は、アクセストークンなどを利用する代替手段での接続を示唆し、ユーザーに対してよりセキュアまたは現代的な認証手法を示すものとして機能します。このような修正は、ドキュメントの整合性を高め、利用者が求める情報へと円滑に誘導するのに寄与します。全体として、この変更はユーザーの体験を向上させることを目的とした小さなが、意義深い調整です。


