---
date: '2025-02-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:17e9068...MicrosoftDocs:f9aa01e
summary: このコード変更では、特定のドキュメントに軽微な更新が行われました。新しい機能は追加されておらず、大きな破壊的変更もありません。変更点としては、ワークスペース名の変更によるコードの可読性向上と、ドキュメントの日付および表現の修正が挙げられます。特に、ワークスペース名の変更はプロジェクト接続の正確性を高め、一貫性を保つことを目的としています。また、情報の最新性を保つための重要な更新が行われており、全体的なユーザー体験の向上が期待されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:17e9068...MicrosoftDocs:f9aa01e){target="_blank"}

# ハイライト
このコード変更では、`articles/ai-studio/how-to/develop/index-build-consume-sdk.md`と`articles/ai-studio/how-to/secure-data-playground.md`のドキュメントで軽微な更新が行われました。

## 新機能
特に新しい機能は追加されていません。

## 破壊的変更
大きな破壊的変更はありません。

## その他の更新
- ワークスペース名の変更により、プロジェクト接続に関するコードの可読性が向上しました。
- ドキュメントの日付と表現の修正により、情報の最新性と明確さが強化されました。

# 洞察
コードの更新により、特に「ワークスペース名の変更」が注目されます。`workspace_name` パラメーターの値が `<ai_studio_project_name>` から `<ai_foundry_project_name>` に変更されたことで、より正確なプロジェクトの接続をサポートすることが目的とされています。この変更は、コード内で複数回適用され、一貫性のある命名が保たれています。

また、ドキュメントにおける日付の更新や表現の修正は、ユーザが情報を最新の状態で正確に理解できるようにするための重要な更新です。特に日付の更新は、ドキュメントが古くなっているとの誤解を避けるために重要です。表現の修正もまた、多くの場合自然な言い回しを採用することで、可読性が向上し、ユーザーフレンドリーになっています。

これらの変更は、全体的なユーザー体験を向上させることを目指しており、コードとドキュメントの品質向上に寄与しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index-build-consume-sdk.md](#item-2ee880) | minor update | ワークスペース名の変更 | modified | 3 | 3 | 6 | 
| [secure-data-playground.md](#item-b7fa5e) | minor update | 日付と表現の修正 | modified | 6 | 6 | 12 | 


# Modified Contents
## articles/ai-studio/how-to/develop/index-build-consume-sdk.md{#item-2ee880}

<details>
<summary>Diff</summary>
````diff
@@ -98,7 +98,7 @@ from promptflow.rag.config import ConnectionConfig
 my_connection_config=ConnectionConfig(
     subscription_id="<subscription_id>",
     resource_group_name="<resource_group_name>",
-    workspace_name="<ai_studio_project_name>",
+    workspace_name="<ai_foundry_project_name>",
     connection_name="<serverless_connection_name>"
     )
 ```
@@ -157,7 +157,7 @@ client=MLClient(
     DefaultAzureCredential(), 
     subscription_id="<subscription_id>",
     resource_group_name="<resource_group_name>",
-    workspace_name="<ai_studio_project_name>"
+    workspace_name="<ai_foundry_project_name>"
     )
 ```
 The `subscription`, `resource_group` and `workspace` in the above code refers to the project you want to connect to.
@@ -210,7 +210,7 @@ client=MLClient(
     DefaultAzureCredential(), 
     subscription_id="<subscription_id>",
     resource_group_name="<resource_group_name>",
-    workspace_name="<ai_studio_project_name>"
+    workspace_name="<ai_foundry_project_name>"
     )
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ワークスペース名の変更"
}
```

### Explanation
この変更では、コード内の `workspace_name` パラメーターの値が `<ai_studio_project_name>` から `<ai_foundry_project_name>` に更新されました。この変更により、接続するプロジェクトの名前がより適切に反映されるようになっています。具体的には、以下の3つの箇所で同様の変更が行われました：

1. `my_connection_config` の設定部分
2. `client` の初期化部分（2回）

全体として、このマイナーな更新は、コードの可読性と明確さを高め、誤解を避けるために重要です。ユーザーが正しいプロジェクトに接続できるようになることを目的としています。

## articles/ai-studio/how-to/secure-data-playground.md{#item-b7fa5e}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to securely use the Azure AI Foundry portal playground ch
 manager: scottpolly
 ms.service: azure-ai-foundry
 ms.topic: how-to
-ms.date: 11/21/2024
+ms.date: 02/18/2025
 ms.reviewer: meerakurup 
 ms.author: larryfr
 author: Blackmist
@@ -18,7 +18,7 @@ zone_pivot_groups: azure-ai-studio-sdk-cli
 Use this article to learn how to securely use Azure AI Foundry's playground chat on your data. The following sections provide our recommended configuration to protect your data and resources by using Microsoft Entra ID role-based access control, a managed network, and private endpoints. We recommend disabling public network access for Azure OpenAI resources, Azure AI Search resources, and storage accounts. Using selected networks with IP rules isn't supported because the services' IP addresses are dynamic.
 
 > [!NOTE]
-> Azure AI Foundry's managed virtual network settings apply only to Azure AI Foundry's managed compute resources, not platform as a service (PaaS) services like Azure OpenAI or Azure AI Search. When using PaaS services, there is no data exfiltration risk because the services are managed by Microsoft.
+> Azure AI Foundry's managed virtual network settings apply only to Azure AI Foundry's managed compute resources, not platform as a service (PaaS) services like Azure OpenAI or Azure AI Search. When using PaaS services, there's no data exfiltration risk because the services are managed by Microsoft.
 
 The following table summarizes the changes made in this article:
 
@@ -51,7 +51,7 @@ If you have an __existing Azure AI Foundry hub__ that isn't configured to use a
 
     :::image type="content" source="../media/how-to/secure-playground-on-your-data/hub-public-access-disable.png" alt-text="Screenshot of Azure AI Foundry hub settings with public access disabled.":::
 
-1. Select select __Workspace managed outbound access__ and then select either the __Allow Internet Outbound__ or __Allow Only Approved Outbound__ network isolation mode. Select __Save__ to apply the changes.
+1. Select __Workspace managed outbound access__ and then select either the __Allow Internet Outbound__ or __Allow Only Approved Outbound__ network isolation mode. Select __Save__ to apply the changes.
 
     :::image type="content" source="../media/how-to/secure-playground-on-your-data/select-network-isolation-configuration.png" alt-text="Screenshot of the Azure AI Foundry hub settings with allow internet outbound selected.":::
 
@@ -96,7 +96,7 @@ You might want to consider using an Azure AI Search index when you either want t
 To use an existing index, it must have at least one searchable field. Ensure at least one valid vector column is mapped when using vector search. 
 
 > [!IMPORTANT]
-> The information in this section is only applicable for securing the Azure AI Search resource for use with Azure AI Foundry. If you're using Azure AI Search for other purposes, you might need to configure additional settings. For related information on configuring Azure AI Search, visit the following articles:
+> The information in this section is only applicable for securing the Azure AI Search resource for use with Azure AI Foundry. If you're using Azure AI Search for other purposes, you might need to configure other settings. For related information on configuring Azure AI Search, visit the following articles:
 >
 > - [Configure network access and firewall rules](../../search/service-configure-firewall.md)
 > - [Enable or disable role-based access control](/azure/search/search-security-enable-roles)
@@ -187,14 +187,14 @@ For more information on assigning roles, see [Tutorial: Grant a user access to r
 | Azure AI Search | Search Index Data Reader | Azure AI services/OpenAI | Inference service queries the data from the index. Only used for inference scenarios. |
 | Azure AI Search | Search Service Contributor | Azure AI services/OpenAI | Read-write access to object definitions (indexes, aliases, synonym maps, indexers, data sources, and skillsets). Inference service queries the index schema for auto fields mapping. Data ingestion service creates index, data sources, skill set, indexer, and queries the indexer status. |
 | Azure AI services/OpenAI | Cognitive Services Contributor | Azure AI Search | Allow Search to create, read, and update AI Services resource. |
-| Azure AI services/OpenAI | Cognitive Services OpenAI Contributor | Azure AI Search | Allow Search the ability to fine-tune, deploy and generate text |
+| Azure AI services/OpenAI | Cognitive Services OpenAI Contributor | Azure AI Search | Allow Search the ability to fine-tune, deploy, and generate text |
 | Azure Storage Account | Storage Blob Data Contributor | Azure AI Search | Reads blob and writes knowledge store. |
 | Azure Storage Account | Storage Blob Data Contributor | Azure AI services/OpenAI | Reads from the input container, and writes the preprocess result to the output container. |
 | Azure Blob Storage private endpoint | Reader | Azure AI Foundry project | For your Azure AI Foundry project with managed network enabled to access Blob storage in a network restricted environment |
 | Azure OpenAI Resource for chat model | Cognitive Services OpenAI User | Azure OpenAI resource for embedding model | [Optional] Required only if using two Azure OpenAI resources to communicate. |
 
 > [!NOTE]
-> The Cognitive Services OpenAI User role is only required if you are using two Azure OpenAI resources: one for your chat model and one for your embedding model. If this applies, enable Trusted Services AND ensure the Connection for your embedding model Azure OpenAI resource has EntraID enabled.  
+> The Cognitive Services OpenAI User role is only required if you're using two Azure OpenAI resources: one for your chat model and one for your embedding model. If this applies, enable Trusted Services AND ensure the Connection for your embedding model Azure OpenAI resource has EntraID enabled.  
 
 ### Assign roles to developers
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付と表現の修正"
}
```

### Explanation
この変更では、`secure-data-playground.md` ドキュメント内のいくつかの箇所でマイナーな更新が行われました。主な変更点は以下の通りです：

1. **日付の更新**: `ms.date` フィールドの値が `11/21/2024` から `02/18/2025` に変更され、ドキュメントの最新性が反映されています。

2. **表現の修正**: 特定の文の構造が改善され、可読性が向上しました。例えば、注意書きの文中で「there's」が使用されるように修正され、より自然な表現となっています。

3. **リストアイテムの改訂**: リスト内の項目が少し調整されましたが、主な内容には影響を与えません。

これらの変更は、ドキュメントの明確さと正確性を高めることを目的としており、ユーザーが情報をよりスムーズに理解できるよう改善されています。


