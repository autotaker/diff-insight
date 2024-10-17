---
date: '2024-10-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9a3d20f...MicrosoftDocs:00d70d8
summary: このドキュメントの更新では、著者やレビュアー情報、最終更新日、前提条件などの新しい情報が追加され、カスタムサブドメインの必要性やAzure OpenAIサービス作成時の注意点が明確に説明されています。大きな破壊的変更はないものの、一部のパラメータ名やリンク形式が修正され、利便性が向上しています。また、文書の管理上、更新が行われ、利用者が正確な情報を得やすくなっています。今回の変更により、ユーザーはAzure
  OpenAIの特定機能を利用する際の準備を明確に理解でき、開発プロセスが円滑になります。全体的に、これらの改訂はユーザーの経験を向上させるための重要な取り組みです。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9a3d20f...MicrosoftDocs:00d70d8){target="_blank"}

# Highlights

## New features
- 著者およびレビュアーの情報、最終更新日、前提条件セクションなど、ドキュメントにいくつかの新しい情報が追加された。
- カスタムサブドメインの必要性とAzure OpenAIサービスの作成時の注意点が明確に説明されている。

## Breaking changes
- 大きな破壊的変更は見られないが、いくつかのパラメータ名やリンク形式の修正が行われ、ユーザーが同じ情報を利用する際の方法に変更が加えられている。

## Other updates
- 変更箇所には最終更新日や執筆者情報の更新が含まれており、これはドキュメント管理上の定期的なアップデートの一環であると考えられる。
- Azure OpenAIサービスリソースに関連する重要な情報がドキュメント内で明確にされ、利用者が正しい情報を取得しやすい状況が構築されている。

# Insights

このドキュメントの更新によって、Azure OpenAI関連のサービスとベクトライザー、インデックス作成のプロセスについてより具体的な指針が示されるようになりました。特筆すべきは、カスタムサブドメインが必要であることの明示です。これにより、ユーザーはAzure OpenAIの特定機能を利用する場合に必要な準備が明確になります。AI Studioで作成されたリソースがサポートされない点にも注意が必要です。これは、Azureポータルで作成されたリソースのみが現在のベストプラクティスに従うべきであることを示唆しています。

また、パラメータ名やフォーマットの一部変更など、ユーザーが既存ドキュメントを参照する際の誤解やトラブルを防ぐための全般的な修正が行われています。これらは一見小さなアップデートのように見えますが、利用者の経験を向上させるための重要な配慮がなされています。

このような更新は、Azureサービスとの統合プロセスを円滑にするものであり、ユーザーにとっての明確なガイダンス提供のための継続的な取り組みの一環です。これにより、開発者やエンジニアは、新しい機能をスムーズに取り入れ、自分たちのアプリケーションを効果的に開発することができるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-azure-openai-embedding.md](#item-3eca57) | minor update | Azure OpenAI Embedding スキルに関する情報が更新されました | modified | 7 | 2 | 9 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | Azure ポータルによるベクトル化のクイックスタートに関する情報が更新されました | modified | 5 | 2 | 7 | 
| [search-index-azure-sql-managed-instance-with-managed-identity.md](#item-a4ec86) | minor update | Azure SQL マネージドインスタンスのインデックス作成に関する情報が更新されました | modified | 1 | 1 | 2 | 
| [search-indexer-how-to-access-private-sql.md](#item-1bd4cc) | minor update | プライベート SQL インスタンスへのアクセスに関する手順が更新されました | modified | 6 | 7 | 13 | 
| [vector-search-vectorizer-azure-open-ai.md](#item-e75cee) | minor update | Azure OpenAI ベクトライザーに関する情報が更新されました | modified | 10 | 4 | 14 | 


# Modified Contents
## articles/search/cognitive-search-skill-azure-openai-embedding.md{#item-3eca57}

<details>
<summary>Diff</summary>
````diff
@@ -9,18 +9,23 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: reference
-ms.date: 08/05/2024
+ms.date: 10/16/2024
 ---
 
 #	Azure OpenAI Embedding skill
 
 The **Azure OpenAI Embedding** skill connects to a deployed embedding model on your [Azure OpenAI](/azure/ai-services/openai/overview) resource to generate embeddings during indexing. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed. 
 
+## Prerequisites
+
+Your Azure OpenAI Service must have an associated [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains). If the service was created through the Azure portal, this subdomain is automatically generated as part of your service setup. Ensure that your service includes a custom subdomain before using it with the Azure AI Search integration.
+
+Azure OpenAI Service resources (with access to embedding models) that were created in AI Studio aren't supported. Only the Azure OpenAI Service resources created in the Azure portal are compatible with the **Azure OpenAI Embedding** skill integration.
+
 The [Import and vectorize data wizard](search-get-started-portal-import-vectors.md) in the Azure portal uses the **Azure OpenAI Embedding** skill to vectorize content. You can run the wizard and review the generated skillset to see how the wizard builds the skill for embedding models. 
 
 > [!NOTE]
 > This skill is bound to Azure OpenAI and is charged at the existing [Azure OpenAI pay-as-you go price](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing).
->
 
 ## @odata.type  
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI Embedding スキルに関する情報が更新されました"
}
```

### Explanation
この変更は、Azure OpenAI Embedding スキルに関するドキュメントの更新を示しています。具体的には、前提条件セクションが追加され、Azure OpenAI サービスを使用する際のカスタムサブドメインについての情報が含まれています。また、AI Studio で作成された Azure OpenAI サービスリソースはサポートされず、Azure ポータルで作成されたリソースのみが適合することが明記されています。さらに、最終更新日が2024年8月5日から2024年10月16日に変更されました。この更新により、ユーザーはAzure OpenAI Embedding スキルの必要要件を理解しやすくなり、正しいサービスの利用を促進できます。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -2,14 +2,13 @@
 title: "Quickstart: Vectorize text and images by using the Azure portal"
 titleSuffix: Azure AI Search
 description: Use a wizard to automate data chunking and vectorization in a search index.
-
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: quickstart
-ms.date: 08/13/2024
+ms.date: 10/16/2024
 ---
 
 # Quickstart: Vectorize text and images by using the Azure portal
@@ -47,6 +46,10 @@ Key points about the wizard:
   | [Azure AI Studio model catalog](/azure/ai-studio/what-is-ai-studio) |  Azure, Cohere, and Facebook embedding models. |
   | [Azure AI services multiservice account](/azure/ai-services/multi-service-resource) | [Azure AI Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) for image and text vectorization. Azure AI Vision multimodal is available in selected regions. [Check the documentation](/azure/ai-services/computer-vision/how-to/image-retrieval?tabs=csharp) for an updated list. **To use this resource, the account must be in an available region and in the same region as Azure AI Search**. |
 
+If using the Azure OpenAI Service, it must have an associated [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains). If the service was created through the Azure portal, this subdomain is automatically generated as part of your service setup. Ensure that your service includes a custom subdomain before using it with the Azure AI Search integration.
+
+Azure OpenAI Service resources (with access to embedding models) that were created in AI Studio aren't supported. Only the Azure OpenAI Service resources created in the Azure portal are compatible with the **Azure OpenAI Embedding** skill integration.
+
 ### Public endpoint requirements
 
 All of the preceding resources must have public access enabled so that the portal nodes can access them. Otherwise, the wizard fails. After the wizard runs, you can enable firewalls and private endpoints on the integration components for security. For more information, see [Secure connections in the import wizards](search-import-data-portal.md#secure-connections).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure ポータルによるベクトル化のクイックスタートに関する情報が更新されました"
}
```

### Explanation
この変更は、Azure ポータルを使用したテキストおよび画像のベクトル化に関するクイックスタートガイドの更新を示しています。主な改訂点として、最終更新日が2024年8月13日から2024年10月16日に変更されました。また、Azure OpenAI サービスを使用する場合には、カスタムサブドメインが必要であることが強調されています。さらに、AI Studio で作成された Azure OpenAI サービスリソースはサポートされず、Azure ポータルで作成されたリソースのみがこのベクトル化プロセスと互換性があることが明確にされています。この更新により、ユーザーはAzure AI Searchとの統合に向けた要件を理解しやすくなり、正しいサービスの利用を促進します。また、パブリックエンドポイントの要件やセキュリティに関する情報も追加されています。

## articles/search/search-index-azure-sql-managed-instance-with-managed-identity.md{#item-a4ec86}

<details>
<summary>Diff</summary>
````diff
@@ -94,7 +94,7 @@ Create the data source and provide a system-assigned managed identity.
 
 ### System-assigned managed identity
 
-The [REST API](//rest/api/searchservice/data-sources/create), Azure portal, and the [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) support system-assigned managed identity. 
+The [REST API](/rest/api/searchservice/data-sources/create), Azure portal, and the [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) support system-assigned managed identity. 
 
 When you're connecting with a system-assigned managed identity, the only change to the data source definition is the format of the "credentials" property. You'll provide an Initial Catalog or Database name and a `ResourceId` that has no account key or password. The `ResourceId` must include the subscription ID of SQL Managed Instance, the resource group of SQL Managed instance, and the name of the SQL database. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure SQL マネージドインスタンスのインデックス作成に関する情報が更新されました"
}
```

### Explanation
この変更は、Azure SQL マネージドインスタンスでのインデックス作成に関連するドキュメントにおける軽微な修正を示しています。具体的には、システム割り当てマネージドIDに関する説明の中で、REST API のリンク部分が修正され、正しいリンク形式が適用されました。この更新により、ドキュメントの正確性が向上し、ユーザーはシステム割り当てマネージドIDに関連するリソースをよりスムーズに参照できるようになります。その他の内容は変更されていませんが、全体の情報が引き続き有効であることが確認されます。また、データソース定義における「credentials」プロパティのフォーマットに関する説明は変わっていないため、利用者には一貫したサポートが提供されます。

## articles/search/search-indexer-how-to-access-private-sql.md{#item-1bd4cc}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.date: 05/23/2024
 
 This article explains how to configure an indexer in Azure AI Search for a private connection to a SQL managed instance that runs within a virtual network. The private connection is through a [shared private link](search-indexer-howto-access-private.md) and Azure Private Link.
 
-On a private connection to a managed instance, the fully qualified domain name (FQDN) of the instance must include the [DNS Zone](/azure/azure-sql/managed-instance/connectivity-architecture-overview#virtual-cluster-connectivity-architecture). Currently, only the Azure AI Search Management REST API provides a `resourceRegion` parameter for accepting the DNS zone specification.
+On a private connection to a managed instance, the fully qualified domain name (FQDN) of the instance must include the [DNS Zone](/azure/azure-sql/managed-instance/connectivity-architecture-overview#virtual-cluster-connectivity-architecture). Currently, only the Azure AI Search Management REST API provides a `dnsZonePrefix` parameter for accepting the DNS zone specification.
 
 Although you can call the Management REST API directly, it's easier to use the Azure CLI `az rest` module to send Management REST API calls from a command line. This article uses the Azure CLI with REST to set up the private link.
 
@@ -57,7 +57,7 @@ For more information about connection properties, see [Create an Azure SQL Manag
        "name": "{{shared-private-link-name}}",
        "properties": {
            "privateLinkResourceId": "/subscriptions/{{target-resource-subscription-ID}}/resourceGroups/{{target-resource-rg}}/providers/Microsoft.Sql/managedInstances/{{target-resource-name}}",
-           "resourceRegion": "a1b22c333d44",
+           "dnsZonePrefix": "a1b22c333d44",
            "groupId": "managedInstance",
            "requestMessage": "please approve",
        }
@@ -66,7 +66,7 @@ For more information about connection properties, see [Create an Azure SQL Manag
 
 1. Provide a meaningful name for the shared private link. The shared private link appears alongside other private endpoints. A name like "shared-private-link-for-search" can remind you how it's used.
 
-1. Paste in the DNS zone name in "resourceRegion" that you retrieved in an earlier step.
+1. Paste in the DNS zone name in "dnsZonePrefix" that you retrieved in an earlier step.
 
 1. Edit the "privateLinkResourceId" to reflect the private endpoint of your managed instance. Provide the subscription ID, resource group name, and object name of the managed instance.
 
@@ -128,7 +128,7 @@ This article assumes a [REST client](search-get-started-rest.md) and uses the RE
 
 1. [Create the data source definition](search-howto-connecting-azure-sql-database-to-azure-search-using-indexers.md) as you would normally for Azure SQL. The format of the connection string is slightly different for a managed instance, but other properties are the same as if you were configuring a data source connection to Azure SQL database.
 
-    Provide the connection string that you copied earlier.
+    Provide the connection string that you copied earlier with an Initial Catalog specified.
 
     ```http
     POST https://myservice.search.windows.net/datasources?api-version=2024-07-01
@@ -139,16 +139,15 @@ This article assumes a [REST client](search-get-started-rest.md) and uses the RE
          "description" : "A database for testing Azure AI Search indexes.",
          "type" : "azuresql",
          "credentials" : { 
-             "connectionString" : "Server=tcp:contoso.public.0000000000.database.windows.net,1433; Persist Security Info=false; User ID=<your user name>; Password=<your password>;MultipleActiveResultsSets=False; Encrypt=True;Connection Timeout=30;" 
+             "connectionString" : "Server=tcp:contoso.public.0000000000.database.windows.net,1433;Persist Security Info=false; User ID=<your user name>; Password=<your password>;MultipleActiveResultsSets=False; Encrypt=True;Connection Timeout=30;Initial Catalog=<your database name>"
             },
          "container" : { 
              "name" : "Name of table or view to index",
              "query" : null (not supported in the Azure SQL indexer)
              },
          "dataChangeDetectionPolicy": null,
          "dataDeletionDetectionPolicy": null,
-         "encryptionKey": null,
-         "identity": null
+         "encryptionKey": null
      }
     ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベート SQL インスタンスへのアクセスに関する手順が更新されました"
}
```

### Explanation
この変更は、Azure AI Search のプライベート SQL インスタンスへの接続に関するドキュメントの内容を更新しています。主な修正点は、DNS ゾーン仕様を受け取るパラメータ名が `resourceRegion` から `dnsZonePrefix` に変更されたことです。この変更により、ユーザーがプライベート接続の設定を行う際に、正確なパラメータ名を使用することができるようになります。

さらに、接続文字列の指定方法にも更新があり、接続に使用するデータベース名を含める必要があることが明示されています。これにより、ユーザーはAzure SQL マネージドインスタンスに対して適切に接続を設定できるようになります。全体として、この更新は、ユーザー体験を向上させるため、より明確で一貫した情報を提供しています。

## articles/search/vector-search-vectorizer-azure-open-ai.md{#item-e75cee}

<details>
<summary>Diff</summary>
````diff
@@ -2,13 +2,14 @@
 title: Azure OpenAI vectorizer
 titleSuffix: Azure AI Search
 description: Connects to a deployed model on your Azure OpenAI resource at query time.
-author: careyjmac
-ms.author: chalton
+author: HeidiSteen
+ms.author: heidist
+ms.reviewer: chalton
 ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: reference
-ms.date: 08/05/2024
+ms.date: 10/16/2024
 ---
 
 # Azure OpenAI vectorizer
@@ -23,7 +24,12 @@ Vectorizers are used at query time, but specified in index definitions, and refe
 
 > [!NOTE]
 > This vectorizer is bound to Azure OpenAI and is charged at the existing [Azure OpenAI pay-as-you go price](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing).
->
+
+## Prerequisites
+
+Your Azure OpenAI Service must have an associated [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains). If the service was created through the Azure portal, this subdomain is automatically generated as part of your service setup. Ensure that your service includes a custom subdomain before using it with the Azure AI Search integration.
+
+Azure OpenAI Service resources (with access to embedding models) that were created in AI Studio aren't supported. Only the Azure OpenAI Service resources created in the Azure portal are compatible with the **Azure OpenAI Embedding** skill integration. 
 
 ## Vectorizer parameters
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI ベクトライザーに関する情報が更新されました"
}
```

### Explanation
この変更は、Azure OpenAI ベクトライザーに関するドキュメントの更新を示しています。主な修正点には、著者およびレビュアーの情報が変更され、最終更新日が2024年10月16日に変更されました。また、ユーザーがAzure AI Searchとの統合を使用する前に確認するべき前提条件が新たに追加されました。この前提条件では、Azure OpenAI サービスに関連付けられたカスタムサブドメインが必要であることが明記されており、サービスがAzureポータルを介して作成された場合、このサブドメインが自動的に生成されることが説明されています。

さらに、AIスタジオで作成されたAzure OpenAIサービスリソースは、埋め込みモデルへのアクセスがないため、**Azure OpenAI Embedding** スキル統合とは互換性がないことも追記されています。これにより、ユーザーは適切な環境でサービスを利用するための情報を得ることができ、全体としてより明確なガイダンスが提供されることとなります。


