---
date: '2025-03-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:31c2d64...MicrosoftDocs:4d90f76
summary: |-
  このコードの変更では、Azureの検索サービスに関連する2つの主要なドキュメントが更新されました。一つは検索制限やキャパシティに関するもので、プライベートエンドポイントやAI処理能力に関する情報が強化されました。もう一つは暗号化キー管理に関するドキュメントで、カスタマーマネージドキーのポリシーやAzure CLIを使った新規サービスの作成に関する情報が改訂されました。

  新機能として、検索制限とキャパシティの文書にスキルセットや埋め込みモデルに関する情報が追加され、暗号化キー管理文書にはCMKの設定やAzure CLIのコマンドが加わりました。また、破壊的変更として、プライベート接続が低いティアでのAI機能が無効化される可能性が明記され、新しい制限が4月3日以降に適用されることが示されています。

  全体的に情報が明確化され、特にリソースグループポリシーを考慮にいれた手順が強化されました。この変更は、Azureの検索サービスを使用する開発者にとって、システムの理解を容易にし、AI機能の実装やセキュリティポリシーの遵守を助けることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:31c2d64...MicrosoftDocs:4d90f76){target="_blank"}

# ハイライト

このコードの変更において、Azureの検索サービスに関連する2つの主要なドキュメントが更新されました。
- 一つは、検索制限、クォータ、およびキャパシティに関するものであり、特にプライベートエンドポイントとAI処理能力に関する情報が強化されました。
- もう一つは、暗号化キー管理に関するドキュメントで、特にカスタマーマネージドキー（CMK）のポリシーおよびAzure CLIを使用した新規サービスの作成に関する情報が改訂されました。

## 新機能
- 検索制限とキャパシティの文書に、スキルセットと埋め込みモデルについての新しい情報が追加されました。
- 暗号化キー管理において、CMKの設定と新規検索サービスの作成に関するAzure CLIの具体的なコマンドが追加されました。

## 破壊的変更
- プライベート接続が低いティアでのAI機能によって無効化される可能性があることが明記され、4月3日以降のサービスに新しい制限が適用されることが明確化されました。

## その他の更新
- 文書全体で情報の明確化が図られています。特に、リソースグループポリシーを考慮に入れた上での手順がユーザーにとって実行可能に強化されています。

# インサイト

この変更は、Azureの検索サービスを使用する開発者に対して、より多くの情報を提供しながら、彼らのシステムがどのように動作するのかを理解しやすくするために行われました。これによりユーザーは、プライベートエンドポイントやAI処理能力がサービスの使用にどのように影響するかをより良く理解することができます。

特に、新しいスキルセットと埋め込みモデルに関する情報が追加されたことで、開発者は自らのサービスにAI機能を組み込む際に、具体的な制限を理解し、効率的に設計を行うことができるようになりました。2024年以降に新たに作成されるサービスに対する制限についての記載が追加されることで、今後導入を考えているユーザーへの警告にもなっています。

また、暗号化キー管理に関するドキュメントの変更により、開発者はセキュリティポリシーに基づいた具体的な手順を踏むことが可能となり、Azure CLIを活用して新しいリソースを作成する際の透明性が高まりました。この改訂が、サービスのセットアッププロセス全体の理解を助け、エラーを減少させるサポートとなるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索制限、クォータ、キャパシティに関する記事の更新 | modified | 5 | 5 | 10 | 
| [search-security-manage-encryption-keys.md](#item-db3487) | minor update | 暗号化キー管理に関するドキュメントの更新 | modified | 8 | 8 | 16 | 


# Modified Contents
## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -145,14 +145,14 @@ Indexers can access other Azure resources [over private endpoints](search-indexe
 | Resource | Free | Basic | S1 | S2 | S3 | S3 HD | L1 | L2 |
 |----------|------|-------|----|----|----|-------|----|----|
 | Private endpoint indexer support | No | Yes | Yes | Yes | Yes | No | Yes | Yes |
-| Private endpoint support for indexers with a skillset<sup>1</sup> | No | No | No | Yes | Yes | No | Yes | Yes |
-| Private endpoint support for indexers with a skillset and integrated vectorization <sup>2</sup> | No | Yes | Yes | Yes | Yes | No | Yes | Yes |
+| Private endpoint support for indexers with a skillset <sup>1</sup> | No | No | Yes | Yes | Yes | No | Yes | Yes |
+| Private endpoint support for skillsets with an embedding skill <sup>2</sup> | No | Yes | Yes | Yes | Yes | No | Yes | Yes |
 | Maximum private endpoints | N/A | 10 or 30 | 100 | 400 | 400 | N/A | 20 | 20 |
-| Maximum distinct resource types<sup>3</sup> | N/A | 4 | 7 | 15 | 15 | N/A | 4 | 4 |
+| Maximum distinct resource types <sup>3</sup> | N/A | 4 | 7 | 15 | 15 | N/A | 4 | 4 |
 
-<sup>1</sup> AI enrichment and image analysis are computationally intensive and consume disproportionate amounts of available processing power. For this reason, private connections are disabled on lower tiers to ensure the performance and stability of the search service itself.
+<sup>1</sup> AI enrichment and image analysis are computationally intensive and consume disproportionate amounts of available processing power. For this reason, private connections are disabled on lower tiers to ensure the performance and stability of the search service itself. On basic services, private connections to an Azure AI multi-service resource are unsupported to preserve service stability. For the S1 tier, make sure the service was created with [higher limits](search-limits-quotas-capacity.md#partition-storage-gb) after April 3, 2024. 
 
-<sup>2</sup> High-capacity services created after April 3, 2024 in the regions listed under [Partition Storage](search-limits-quotas-capacity.md#partition-storage-gb) and running [integrated vectorization](vector-search-integrated-vectorization.md) workloads at indexing time support shared private links in paid tiers. The system must detect at least a skill that is embedding data.
+<sup>2</sup> Private connections to an embedding model are supported on basic and S1 high-capacity search services created after April 3, 2024, with the [higher limits](search-limits-quotas-capacity.md#partition-storage-gb) for storage and computational processing. 
 
 <sup>3</sup> The number of distinct resource types are computed as the number of unique `groupId` values used across all shared private link resources for a given search service, irrespective of the status of the resource.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索制限、クォータ、キャパシティに関する記事の更新"
}
```

### Explanation
この変更は、Azureの検索サービスに関するドキュメントにおいていくつかの小さな更新を含んでいます。具体的には、プライベートエンドポイントに関するサポート情報が見直され、スキルセットや埋め込みモデルに関連する新しい情報が追記されています。また、AIの強化や画像分析が処理能力を大きく消費するため、低いティアでのプライベート接続の無効化についての説明も強化されています。加えて、2024年4月3日以降に作成されたサービスに対して高い制限が適用されることが明記され、ユーザーに対してより明確なガイドラインが提供されています。この変更は、全体的にサービスの安定性を維持し、正確な利用情報を提供することを目的としています。

## articles/search/search-security-manage-encryption-keys.md{#item-db3487}

<details>
<summary>Diff</summary>
````diff
@@ -347,7 +347,7 @@ A policy that's assigned to a resource group in your subscription is effective i
 
 For new search services, create them with [SearchEncryptionWithCmk](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2023-11-01&tabs=HTTP#searchencryptionwithcmk&preserve-view=true) set to `Enabled`. 
 
-Neither the Azure portal nor the command line tools (the Azure CLI and Azure PowerShell) provide this property natively, but you can use [Management REST API](/rest/api/searchmanagement/services/create-or-update) to provision a search service with a CMK policy definition. You can also use the Azure CLI `az resource create` or `update` command to set properties as name-value pairs.
+Neither the Azure portal nor the command line tools (the Azure CLI and Azure PowerShell) provide this property natively, but you can use [Management REST API](/rest/api/searchmanagement/services/create-or-update) to provision a search service with a CMK policy definition.
 
 ### [**Management REST API**](#tab/mgmt-rest-create)
 
@@ -376,22 +376,22 @@ PUT https://management.azure.com/subscriptions/{{subscriptionId}}/resourceGroups
       }
     }
 ```
-
+<!-- 
 ### [**Azure CLI**](#tab/azure-cli-create)
 
-1. Create your search service using the examples in [Manage your Azure AI Search service with the Azure CLI](search-manage-azure-cli.md).
+These instructions assume you have a Deny policy defined for the resource group into which you're deploying a new search service.
 
-1. Patch your service using the update command, substituting valid values for an existing search service and resource group.
+Run the following [`az resource`](/cli/azure/resource) command to create a new search service with CMK enforcement enabled. Substitute valid values for the name of the new search service and name of the existing resource group. The command includes eastus for a region so that you can see how regions are specified (lower case, no spaces).
 
-   ```azurecli
-   az resource update --name SEARCH-SERVICE-PLACEHOLDER --resource-group RESOURCE-GROUP-PLACEHOLDER --resource-type searchServices --namespace Microsoft.Search --set properties.encryptionWithCmk.enforcement=Enabled
-   ```
+```azurecli
+az resource create --name SEARCH-SERVICE-PLACEHOLDER --location eastus --resource-group RESOURCE-GROUP-PLACEHOLDER --resource-type searchServices --namespace Microsoft.Search --set properties.encryptionWithCmk.enforcement=Enabled
+``` -->
 
 ---
 
 #### Update an existing search service
 
-For existing search services that are now non-compliant, patch them using [Services - Update API](/rest/api/searchmanagement/services/update). Patching the services restores the ability to update search service properties.
+For existing search services that are now non-compliant, patch them using [Services - Update API](/rest/api/searchmanagement/services/update) or the Azure CLI [az resource update](/cli/azure/resource?view=azure-cli-latest#az-resource-update&preserve-view=true) command. Patching the services restores the ability to update search service properties.
 
 ### [**Management REST API**](#tab/mgmt-rest-update)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "暗号化キー管理に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azureの検索サービスにおける暗号化キーの管理についてのドキュメントを改訂したものです。主に、カスタマーマネージドキー（CMK）のポリシーに関連する手順を明確化し、Azure CLIを用いて新しい検索サービスを作成する方法を更新しました。特に、CMKの強制を有効にして新しい検索サービスを作成するための具体的なコマンドが示され、従来のパッチ方法から新しいリソースの作成に切り替えられたことが反映されています。また、リソースグループのポリシーを考慮した上での手順が強調されており、利用者にはより具体的で実行可能なガイダンスが提供されています。全体として、利用者が検索サービスの設定を行う際の明瞭さが向上しています。


