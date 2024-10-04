---
date: '2024-10-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:94dabc3...MicrosoftDocs:7d913a4
summary: Azure AI検索サービスに関する文書が更新され、いくつかの新機能が追加されました。主な内容としては、検索ユニットの詳細な説明、インデクサーのスケジューリングに関するFAQの追加、顧客管理キー（CMK）暗号化の設定と管理についての包括的な説明、RAGソリューションのためのクエリ技術の強化があります。破壊的変更はありません。さらに、用語の更新や文書の日付の修正も行われています。これらの更新は、ユーザーがAzure
  AI検索サービスをより効果的に理解し、活用できるようにするためのもので、特に運用やセキュリティ対策の向上に寄与します。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:94dabc3...MicrosoftDocs:7d913a4){target="_blank"}

# Highlights

## New features
- Detailed explanation of search units in the context of Azure AI Search service capacity planning.
- New FAQ section added to the indexer scheduling documentation.
- Comprehensive description of customer-managed key (CMK) encryption setup and management in the Azure AI Search service.
- Enhanced tutorial details on querying techniques for RAG solutions, focusing on hybrid query methods.

## Breaking changes
There are no breaking changes introduced in the updates.

## Other updates
- Terminology update in the indexer execution environment documentation from "search nodes" to "content processors."
- Date updates for several documents to reflect the most recent revisions.

# Insights

Azure AI検索サービスに関連する一連の文書の更新が行われました。これにより、サービスの運用に必要な重要事項がより明確に記載され、ユーザーが各機能を効果的に理解・活用できるようになっています。

まず、「検索サービスのキャパシティプランニング」の更新では、検索ユニットの定義がより詳細に説明されました。これは、検索サービスの基本単位に加え、レプリカやパーティションがユニットを消費することを理解することで、ユーザーの運用計画に役立つ情報を提供します。

次に、「インデクサーのリセット方法」では、用語の変更とともに、プライベート実行環境の詳細が整理され、特にコンテンツプロセッサーに重点が置かれています。全体として、Microsoft管理下でのマルチテナント環境の活用方法が強調されており、サービスの計算リソースを最適に利用できるようになっています。

また、新たに追加された「インデクサーのスケジュール方法」についてのFAQセクションでは、スケジューリングの具体例や挑戦点を列挙することで、ユーザーが効率的にインデクサーを管理するための知識を提供しています。特に、失敗が繰り返される状況に対する対策が実践的に説明されています。

加えて、「暗号鍵の管理方法」においては、CMKの設定と管理のプロセスが詳細に説明されています。これにより、ユーザーはセキュリティ対策としての暗号化手順をより明確に理解し、適用できるようになります。

最後に、「RAGソリューションのクエリ構築」のチュートリアルでは、検索手法におけるクエリのハイブリッド性が強調されています。この更新により、キーワード検索とベクトル検索の併用が具体的に説明され、ユーザーは実際の検索プロセスを効果的に実装するための理解が深まります。

全体的に、これらの更新はAzure AI検索サービスにおける重要な機能やプロセスをさらに明確化し、ユーザーのソリューション設計や運用をより効果的にサポートすることを目的としています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-capacity-planning.md](#item-0dd6c9) | minor update | 検索サービスのキャパシティプランニングに関する内容の更新 | modified | 2 | 2 | 4 | 
| [search-howto-run-reset-indexers.md](#item-fb10c8) | minor update | インデクサーの実行環境に関する情報の更新 | modified | 2 | 2 | 4 | 
| [search-howto-schedule-indexers.md](#item-d57e7b) | minor update | インデクサーのスケジューリング動作に関するFAQの追加 | modified | 17 | 8 | 25 | 
| [search-security-manage-encryption-keys.md](#item-db3487) | minor update | 暗号鍵管理のプロセス手順の更新と整理 | modified | 226 | 250 | 476 | 
| [tutorial-rag-build-solution-query.md](#item-93965f) | minor update | RAGソリューションクエリのチュートリアルの更新 | modified | 5 | 2 | 7 | 


# Modified Contents
## articles/search/search-capacity-planning.md{#item-0dd6c9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 06/19/2024
+ms.date: 10/02/2024
 ---
 
 # Estimate and manage capacity of a search service
@@ -37,7 +37,7 @@ Capacity is expressed in *search units* that can be allocated in combinations of
 
 | Concept  | Definition|
 |----------|-----------|
-|*Search unit* | A single increment of total available capacity (36 units). It's also the billing unit for an Azure AI Search service. A minimum of one unit is required to run the service.|
+|*Search unit* | A single increment of total available capacity (36 units). A minimum of one unit is required to run the service. The first replica and partition pair is the first search unit. However, each extra instance of a replica *or* a partition consumes an extra search unit. For example, you start with one replica and partition (one search unit), add a second replica, you are now consuming two search units. A search unit is also the billing unit for an Azure AI Search service. |
 |*Replica* | Instances of the search service, used primarily to load balance query operations. Each replica hosts one copy of an index. If you allocate three replicas, you have three copies of an index available for servicing query requests.|
 |*Partition* | Physical storage and I/O for read/write operations (for example, when rebuilding or refreshing an index). Each partition has a slice of the total index. If you allocate three partitions, your index is divided into thirds. |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスのキャパシティプランニングに関する内容の更新"
}
```

### Explanation
このコードの差分は、Azure AI 検索サービスに関する文書「検索サービスのキャパシティプランニング」に対する軽微な更新を示しています。主な変更点は、日付の更新（2024年6月19日から2024年10月2日へ）と、検索ユニットの定義に関する内容を詳しく説明した部分です。具体的には、検索ユニットは、基本的にサービスを運営するために必要な最小一つの単位を示すだけでなく、それに加えて追加のレプリカやパーティションが検索ユニットを消費することについても触れています。これにより、ユーザーは検索ユニットの運用方法をより明確に理解できるでしょう。

## articles/search/search-howto-run-reset-indexers.md{#item-fb10c8}

<details>
<summary>Diff</summary>
````diff
@@ -42,7 +42,7 @@ An indexer job runs in a managed execution environment. Currently, there are two
 
 Indexer execution environments include:
 
-+ A private execution environment that runs on search nodes, specific to your search service.
++ A private execution environment that runs on content processors that are specific to your search service.
 
 + A multitenant environment with content processors, managed and secured by Microsoft at no extra cost. This environment is used to offload computationally intensive processing, leaving service-specific resources available for routine operations. Whenever possible, most indexer jobs are executed in the multitenant environment.
 
@@ -51,7 +51,7 @@ Indexer limits vary for each environment:
 | Workload | Maximum duration | Maximum jobs | Execution environment |
 |----------|------------------|---------------------|-----------------------------|
 | Private execution | 24 hours | One indexer job per [search unit](search-capacity-planning.md#concepts-search-units-replicas-partitions) <sup>1</sup>.  | Indexing doesn't run in the background. Instead, the search service will balance all indexing jobs against ongoing queries and object management actions (such as creating or updating indexes). When running indexers, you should expect to see [some query latency](search-performance-analysis.md#impact-of-indexing-on-queries) if indexing volumes are large. |
-| Multitenant| 2 hours <sup>2</sup> | Indeterminate <sup>3</sup> | Because the content processing cluster is multitenant, nodes are added to meet demand. If you experience a delay in on-demand or scheduled execution, it's probably because the system is either adding nodes or waiting for one to become available.|
+| Multitenant| 2 hours <sup>2</sup> | Indeterminate <sup>3</sup> | Because the content processing cluster is multitenant, content processors are added to meet demand. If you experience a delay in on-demand or scheduled execution, it's probably because the system is either adding processors or waiting for one to become available.|
 
 <sup>1</sup> Search units can be [flexible combinations](search-capacity-planning.md#partition-and-replica-combinations) of partitions and replicas, but indexer jobs aren't tied to one or the other. In other words, if you have 12 units, you can have 12 indexer jobs running concurrently in private execution, no matter how the search units are deployed.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーの実行環境に関する情報の更新"
}
```

### Explanation
このコードの差分は、Azure AI 検索サービスにおけるインデクサーの実行環境に関する文書「インデクサーのリセット方法」への軽微な更新を示しています。主な変更点としては、プライベート実行環境の説明において「search nodes」から「content processors」へ表現が修正され、具体的な内容が明確化されました。また、新たにマルチテナント環境についての説明が追加され、Microsoftによって管理されるコンテンツプロセッサーが、計算負荷の高い処理をオフロードし、サービス特有のリソースを通常の操作に利用できるようにしていることが強調されています。これにより、インデクサーの実行環境に対する理解が深まり、特定の制限や期待値についての理解も向上します。

## articles/search/search-howto-schedule-indexers.md{#item-d57e7b}

<details>
<summary>Diff</summary>
````diff
@@ -103,27 +103,36 @@ await indexerClient.CreateOrUpdateIndexerAsync(indexer);
 
 ---
 
-## Scheduling behavior
+## Scheduling behavior FAQ
 
-+ For text-based indexing, the scheduler can kick off as many indexer jobs as the search service supports, which is determined by the number of search units. For example, if the service has three replicas and four partitions, you can have 12 indexer jobs in active execution, whether initiated on demand or on a schedule.
+**Can I run multiple indexer jobs in parallel?**
 
-+ Skills-based indexers run in a different [execution environment](search-howto-run-reset-indexers.md#indexer-execution). For this reason, the number of service units has no bearing on the number of skills-based indexer jobs you can run. Multiple skills-based indexers can run in parallel, but doing so depends on node availability within the execution environment.
+You can run multiple indexers simultaneously, but each indexer is single instance. You can't run two copies of the same indexer concurrently. 
 
-+ Although multiple indexers can run simultaneously, a given indexer is single instance. You can't run two copies of the same indexer concurrently. If an indexer happens to still be running when its next scheduled execution is set to start, the pending execution is postponed until the next scheduled occurrence, allowing the current job to finish.
+For text-based indexing, the scheduler can kick off as many indexer jobs as the search service supports, which is determined by the number of [search units](search-capacity-planning.md#concepts-search-units-replicas-partitions). For example, if the service has three replicas and four partitions, you can have 12 indexer jobs in active execution, whether initiated on demand or on a schedule.
 
-+ If an indexer is set to a certain schedule but repeatedly fails on the same document each time, the indexer will begin running on a less frequent interval (up to the maximum interval of at least once every 2 hours or 24 hours, depending on different implementation factors) until it successfully makes progress again. If you believe you have fixed whatever the underlying issue, you can [run the indexer manually](search-howto-run-reset-indexers.md), and if indexing succeeds, the indexer will return to its regular schedule.
+For skills-based indexing, indexers run in a specific [execution environment](search-howto-run-reset-indexers.md#indexer-execution). For this reason, the number of service units has no bearing on the number of skills-based indexer jobs you can run. Multiple skills-based indexers can run in parallel, but doing so depends on content processor availability within the execution environment.
 
-+ Indexer processes can be queued up and may not start exactly at the time posted, depending on the processing workload and other factors. Based on this, If there is a strict business need tied to the exact time indexing is performed, you should consider using the [Push model](search-what-is-data-import.md#pushing-data-to-an-index) so you can control the indexing pipeline directly.
+**Do scheduled jobs always start at the designated time?**
+
+Indexer processes can be queued up and might not start exactly at the time posted, depending on the processing workload and other factors. For example, if an indexer happens to still be running when its next scheduled execution is set to start, the pending execution is postponed until the next scheduled occurrence, allowing the current job to finish.
 
 Let’s consider an example to make this more concrete. Suppose we configure an indexer schedule with an interval of hourly and a start time of January 1, 2024 at 8:00:00 AM UTC. Here's what could happen when an indexer run takes longer than an hour:
 
 1. The first indexer execution starts at or around January 1, 2024 at 8:00 AM UTC. Assume this execution takes 20 minutes (or any amount of time that's less than 1 hour).
 
-1. The second execution starts at or around January 1, 2022 9:00 AM UTC. Suppose that this execution takes 70 minutes - more than an hour – and it will not complete until 10:10 AM UTC.
+1. The second execution starts at or around January 1, 2024 9:00 AM UTC. Suppose that this execution takes 70 minutes - more than an hour – and it will not complete until 10:10 AM UTC.
 
 1. The third execution is scheduled to start at 10:00 AM UTC, but at that time the previous execution is still running. This scheduled execution is then skipped. The next execution of the indexer won't start until 11:00 AM UTC.
-  
 
+> [!NOTE]
+> If you have strict indexer execution requirements that are time-sensitive, you should consider using the [push API model](search-what-is-data-import.md#pushing-data-to-an-index) so you can control the indexing pipeline directly.
+
+<!-- + Although multiple indexers can run simultaneously, a given indexer is single instance. You can't run two copies of the same indexer concurrently. If an indexer happens to still be running when its next scheduled execution is set to start, the pending execution is postponed until the next scheduled occurrence, allowing the current job to finish. -->
+
+**What happens if indexing fails repeatedly on the same document?**
+
+If an indexer is set to a certain schedule but repeatedly fails on the same document each time, the indexer will begin running on a less frequent interval (up to the maximum interval of at least once every 2 hours or 24 hours, depending on different implementation factors) until it successfully makes progress again. If you believe you have fixed the underlying issue, you can [run the indexer manually](search-howto-run-reset-indexers.md), and if indexing succeeds, the indexer will return to its regular schedule.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーのスケジューリング動作に関するFAQの追加"
}
```

### Explanation
このコードの差分は、Azure AI 検索サービスにおけるインデクサーのスケジューリングに関する文書「インデクサーのスケジュール方法」に対する軽微な更新を示しています。主な変更点は、スケジューリング動作に関するFAQのセクションが追加されたことです。このセクションでは、インデクサーを並行して実行することに関する詳細や、スケジュールされたジョブが指定された時間に必ず開始されるわけではないこと、また複数のインデクサーが動作を続けていると次の予定実行が延期される可能性があることなどが説明されています。

具体的には、テキストベースのインデクサーやスキルベースのインデクサーに関する情報が見直され、各インデクサーの実行環境の違いや、キューイングされる可能性についての例が挙げられています。また、失敗を繰り返した場合の対処法として手動実行が提案され、インデクサーの効率的な管理に向けた具体的なアドバイスも含まれています。この更新によって、ユーザーはインデクサーのスケジューリングに関する理解を深めることができるでしょう。

## articles/search/search-security-manage-encryption-keys.md{#item-db3487}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: how-to
-ms.date: 09/23/2024
+ms.date: 10/02/2024
 ms.custom:
   - references_regions
   - ignite-2023
@@ -18,34 +18,30 @@ ms.custom:
 
 Azure AI Search automatically encrypts data at rest with [service-managed keys](/azure/security/fundamentals/encryption-atrest#azure-encryption-at-rest-components). If more protection is needed, you can supplement default encryption with another encryption layer using keys that you create and manage in Azure Key Vault. 
 
-This article walks you through the steps of setting up customer-managed key (CMK) or "bring-your-own-key" (BYOK) encryption. Here are some points to keep in mind:
-
-+ CMK encryption is enacted on individual objects. If you require CMK across your search service, [set an enforcement policy](#encryption-enforcement-policy).
-
-+ CMK encryption depends on [Azure Key Vault](/azure/key-vault/general/overview). You can create your own encryption keys and store them in a key vault, or you can use Azure Key Vault APIs to generate encryption keys. Azure Key Vault must be in the same subscription and tenant as Azure AI Search. Azure AI Search retrieves your managed key by connecting through a system or user-managed identity. This behavior requires both services to share the same tenant.
-
-+ CMK encryption becomes operational when an object is created. You can't encrypt objects that already exist. CMK encryption occurs whenever an object is saved to disk, either data at rest for long-term storage or temporary data for short-term storage. With CMK, the disk never sees unencrypted data.
+This article walks you through the steps of setting up customer-managed key (CMK) or "bring-your-own-key" (BYOK) encryption.
 
 > [!NOTE]
 > If an index is CMK encrypted, it is only accessible if the search service has access to the key. If access is revoked, the index is unusable and the service cannot be scaled until the index is deleted or access to the key is restored.
 
 ## CMK encrypted objects
 
+CMK encryption is enacted on individual objects. If you require CMK across your search service, [set an enforcement policy](#set-up-a-policy-to-enforce-cmk-compliance).
+
+CMK encryption becomes operational when an object is created. You can't encrypt objects that already exist. CMK encryption occurs whenever an object is saved to disk, either data at rest for long-term storage or temporary data for short-term storage. With CMK, the disk never sees unencrypted data.
+
 Objects that can be encrypted include indexes, synonym lists, indexers, data sources, and skillsets. Encryption is computationally expensive to decrypt so only sensitive content is encrypted.
 
 Encryption is performed over the following content:
 
-+ All content within indexes and synonym lists, including descriptions.
-
-+ For indexers, data sources, and skillsets, only those fields that store connection strings, descriptions, identities, keys, and user inputs are encrypted. For example, skillsets have Azure AI services keys, and some skills accept user inputs, such as custom entities. In both cases, keys and user inputs into skills are encrypted. Any references to external resources (such as Azure data sources or Azure OpenAI models) are also encrypted.
++ All content within indexes and synonym lists.
 
-+ For vectorizer definitions used by queries, fields that store connection details or credential are encrypted.
++ Sensitive content in indexers, data sources, skillsets, and vectorizers. This content consists of only those fields that store connection strings, descriptions, identities, keys, and user inputs. For example, skillsets have Azure AI services keys, and some skills accept user inputs, such as custom entities. In both cases, keys and user inputs into skills are encrypted. Any references to external resources (such as Azure data sources or Azure OpenAI models) are also encrypted.
 
 ## Full double encryption
 
 When you introduce CMK encryption, you're encrypting content twice. For the objects and fields noted in the previous section, content is first encrypted with your CMK, and secondly with the Microsoft-managed key. Content is doubly encrypted on data disks for long-term storage, and on temporary disks used for short-term storage.
 
-Enabling CMK encryption increases index size and degrades query performance. Based on observations to date, you can expect to see an increase of 30-60 percent in query times, although actual performance varies depending on the index definition and types of queries. Because performance is diminished, we recommend that you only enable this feature on indexes that really require it.
+Enabling CMK encryption increases index size and degrades query performance. Based on observations to date, you can expect to see an increase of 30-60 percent in query times, although actual performance varies depending on the index definition and types of queries. Because performance is diminished, we recommend that you only enable this feature on objects that really require it.
 
 Although double encryption is now available in all regions, support was rolled out in two phases:
 
@@ -59,149 +55,102 @@ Although double encryption is now available in all regions, support was rolled o
 
 + The second rollout on May 13, 2021 added encryption for temporary disks and extended CMK encryption to [all supported regions](search-region-support.md).
 
-  If you're using CMK from a service created during the first rollout and you also want CMK encryption over temporary disks, you need to create a new search service in your region of choice and redeploy your content.
+  If you're using CMK from a service created during the first rollout and you also want CMK encryption over temporary disks, you need to create a new search service in your region of choice and redeploy your content. To determine your service creation date, see [How to check service creation date](vector-search-index-size.md#how-to-check-service-creation-date).
 
 ## Prerequisites
 
-The following tools and services are used in this scenario.
-
 + [Azure AI Search](search-create-service-portal.md) on a [billable tier](search-sku-tier.md#tier-descriptions) (Basic or above, in any region).
 
-+ [Azure Key Vault](/azure/key-vault/general/overview), you can [create a key vault using the Azure portal](/azure/key-vault/general/quick-create-portal), [Azure CLI](/azure/key-vault/general/quick-create-cli), or [Azure PowerShell](/azure/key-vault/general/quick-create-powershell). Create the resource in the same subscription as Azure AI Search. The key vault must have **soft-delete** and **purge protection** enabled.
-
-+ [Microsoft Entra ID](/azure/active-directory/fundamentals/active-directory-whatis). If you don't have one, [set up a new tenant](/azure/active-directory/develop/quickstart-create-new-tenant).
-
-You should have a search client that can create the encrypted object. Into this code, you reference a key vault key and application registration information. This code could be a working app, or prototype code such as the [C# code sample DotNetHowToEncryptionUsingCMK](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToEncryptionUsingCMK).
-
-> [!TIP]
-> You can use a [REST client](search-get-started-rest.md) or [Azure PowerShell](search-get-started-powershell.md) to create indexes and synonym maps that include an encryption key parameter. You can also use Azure SDKs. Portal support for adding a key to indexes or synonym maps isn't supported.
-
-## Key Vault tips
-
-If you're new to Azure Key Vault, review this quickstart to learn about basic tasks: [Set and retrieve a secret from Azure Key Vault using PowerShell](/azure/key-vault/secrets/quick-create-powershell). Here are some tips for using Key Vault:
++ [Azure Key Vault](/azure/key-vault/general/overview) in the same subscription as Azure AI Search. You can [create a key vault using the Azure portal](/azure/key-vault/general/quick-create-portal), [Azure CLI](/azure/key-vault/general/quick-create-cli), or [Azure PowerShell](/azure/key-vault/general/quick-create-powershell). The key vault must have **soft-delete** and **purge protection** enabled. 
 
-+ Use as many key vaults as you need. Managed keys can be in different key vaults. A search service can have multiple encrypted objects, each one encrypted with a different customer-managed encryption key, stored in different key vaults.
-
-+ [Enable logging](/azure/key-vault/general/logging) on Key Vault so that you can monitor key usage.
-
-+ Remember to follow strict procedures during routine rotation of key vault keys and Active Directory application secrets and registration. Always update all [encrypted content](search-security-get-encryption-keys.md) to use new secrets and keys before deleting the old ones. If you miss this step, your content can't be decrypted.
-
-## 1 - Enable purge protection
++ A search client that can create an encrypted object, such as a [REST client](search-get-started-rest.md), [Azure PowerShell](search-get-started-powershell.md), or an Azure SDK (Python, .NET, Java, JavaScript). 
 
-As a first step, make sure [soft-delete](/azure/key-vault/general/soft-delete-overview) and [purge protection](/azure/key-vault/general/soft-delete-overview#purge-protection) are enabled on the key vault. Due to the nature of encryption with customer-managed keys, no one can retrieve your data if your Azure Key Vault key is deleted. 
+## Limitations
 
-To prevent data loss caused by accidental Key Vault key deletions, soft-delete and purge protection must be enabled on the key vault. Soft-delete is enabled by default, so you'll only encounter issues if you purposely disabled it. Purge protection isn't enabled by default, but it's required for customer-managed key encryption in Azure AI Search. 
++ No support for Azure Key Vault Managed Hardware Security Model (HSM).
 
-You can set both properties using the portal, PowerShell, or Azure CLI commands.
-
-### [**Azure portal**](#tab/portal-pp)
-
-1. Sign in to the [Azure portal](https://portal.azure.com) and open your key vault overview page.
++ No support for adding encryption keys in the Azure portal.
 
-1. On the **Overview** page under **Essentials**, enable **Soft-delete** and **Purge protection**.
++ No cross-subscription support. Azure Key Vault and Azure AI Search must be in the same subscription.
 
-### [**Using PowerShell**](#tab/ps-pp)
-
-1. Run `Connect-AzAccount` to  set up your Azure credentials.
-
-1. Run the following command to connect to your key vault, replacing `<vault_name>` with a valid name:
-
-   ```powershell
-   $resource = Get-AzResource -ResourceId (Get-AzKeyVault -VaultName "<vault_name>").ResourceId
-   ```
-
-1. Azure Key Vault is created with soft-delete enabled. If it's disabled on your vault, run  the following command:
+## Key Vault tips
 
-   ```powershell
-   $resource.Properties | Add-Member -MemberType NoteProperty -Name "enableSoftDelete" -Value 'true'
-   ```
+If you're new to Azure Key Vault, review this quickstart to learn about basic tasks: [Set and retrieve a secret from Azure Key Vault using PowerShell](/azure/key-vault/secrets/quick-create-powershell). 
 
-1. Enable purge protection:
+Here are some tips for using Key Vault:
 
-   ```powershell
-   $resource.Properties | Add-Member -MemberType NoteProperty -Name "enablePurgeProtection" -Value 'true'
-   ```
++ Use as many key vaults as you need. Managed keys can be in different key vaults. A search service can have multiple encrypted objects, each one encrypted with a different customer-managed encryption key, stored in different key vaults.
 
-1. Save your updates:
++ Use the same tenant so that you can retrieve your managed key by connecting through a system or user-managed identity. This behavior requires both services to share the same tenant. For more information about creating a tenant, see [Set up a new tenant](/azure/active-directory/develop/quickstart-create-new-tenant).
 
-   ```powershell
-   Set-AzResource -resourceid $resource.ResourceId -Properties $resource.Properties
-   ```
++ [Enable purge protection](/azure/key-vault/general/soft-delete-overview#purge-protection) and [soft-delete](/azure/key-vault/general/soft-delete-overview). Due to the nature of encryption with customer-managed keys, no one can retrieve your data if your Azure Key Vault key is deleted. To prevent data loss caused by accidental Key Vault key deletions, soft-delete and purge protection must be enabled on the key vault. Soft-delete is enabled by default, so you'll only encounter issues if you purposely disable it. Purge protection isn't enabled by default, but it's required for customer-managed key encryption in Azure AI Search.
 
-### [**Using Azure CLI**](#tab/cli-pp)
++ [Enable logging](/azure/key-vault/general/logging) on the key vault so that you can monitor key usage.
 
-+ If you have an [installation of Azure CLI](/cli/azure/install-azure-cli), you can run the following command to enable the required properties.
++ [Enable autorotation of keys](/azure/key-vault/keys/how-to-configure-key-rotation) or follow strict procedures during routine rotation of key vault keys and application secrets and registration. Always update all [encrypted content](search-security-get-encryption-keys.md) to use new secrets and keys before deleting the old ones. If you miss this step, your content can't be decrypted.
 
-   ```azurecli-interactive
-   az keyvault update -n <vault_name> -g <resource_group> --enable-soft-delete --enable-purge-protection
-   ```
+## Step 1: Create a key in Key Vault
 
----
+Skip key generation if you already have a key in Azure Key Vault that you want to use, but collect the key identifier. You need this information when creating an encrypted object.
 
-## 2 - Create a key in Key Vault
+Before you add the key, make sure that you have assigned to yourself the **Key Vault Crypto Officer** role.
 
-Skip key generation if you already have a key in Azure Key Vault that you want to use, but collect the key identifier. You need this information when creating an encrypted object.
+Azure AI Search encryption supports RSA keys of sizes 2048, 3072 and 4096. For more information about supported key types, see [About keys](/azure/key-vault/keys/about-keys).
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and open your key vault overview page.
 
-1. Select **Keys** on the left, and then select **+ Generate/Import**.
+1. Select **Objects** > **Keys** on the left, and then select **Generate/Import**.
+
+1. In the **Create a key** pane, from the list of **Options**, choose **Generate** to create a new key.
 
-1. In the **Create a key** pane, from the list of **Options**, choose the method that you want to use to create a key. You can **Generate** a new key, **Upload** an existing key, or use **Restore Backup** to select a backup of a key.
+1. Enter a **Name** for your key, and accept the defaults for other key properties.
 
-1. Enter a **Name** for your key, and optionally select other key properties.
+1. Optionally, set a key rotation policy to [enable auto rotation](/azure/key-vault/keys/how-to-configure-key-rotation).
 
 1. Select **Create** to start the deployment.
 
 1. Select the key, select the current version, and then make a note of the key identifier. It's composed of the **key value Uri**, the **key name**, and the **key version**. You need the identifier to define an encrypted index in Azure AI Search.
 
    :::image type="content" source="media/search-manage-encryption-keys/cmk-key-identifier.png" alt-text="Create a new key vault key" border="true":::
 
-## 3 - Create a security principal
+## Step 2: Create a security principal
 
-You have several options for accessing the encryption key at run time. The simplest approach is to retrieve the key using the managed identity and permissions of your search service. You can use either a system or user-managed identity. Doing so allows you to omit the steps for application registration and application secrets, and simplifies the encryption key definition.
+You have several options for setting up Azure AI Search access to the encryption key at run time. The simplest approach is to retrieve the key using the managed identity of your search service. You can use either a system or user-managed identity. Doing so allows you to omit the steps for application registration and application secrets. Alternatively, you can create and register a Microsoft Entra application and have the search service provide the application ID on requests.
 
-Alternatively, you can create and register a Microsoft Entra application. The search service provides the application ID on requests.
-
-A managed identity enables your search service to authenticate to Azure Key Vault without storing credentials (ApplicationID or ApplicationSecret) in code. The lifecycle of this type of managed identity is tied to the lifecycle of your search service, which can only have one managed identity. For more information about how managed identities work, see [What are managed identities for Azure resources](/azure/active-directory/managed-identities-azure-resources/overview).
+We recommend using a managed identity. A managed identity enables your search service to authenticate to Azure Key Vault without storing credentials (ApplicationID or ApplicationSecret) in code. The lifecycle of this type of managed identity is tied to the lifecycle of your search service, which can only have one system assigned managed identity. For more information about how managed identities work, see [What are managed identities for Azure resources](/azure/active-directory/managed-identities-azure-resources/overview).
 
 ### [**System-managed identity**](#tab/managed-id-sys)
 
-1. Make your search service a trusted service.
-
-   ![Turn on system assigned managed identity](./media/search-managed-identities/turn-on-system-assigned-identity.png "Turn on system assigned managed identity")
-
-Conditions that prevent you from adopting this approach include:
+Enable the system assigned managed identity for your search service.
 
-+ You can't directly grant your search service access permissions to the key vault (for example, if the search service is in a different Microsoft Entra ID tenant than the Azure Key Vault).
-
-+ A single search service is required to host multiple encrypted indexes or synonym maps, each using a different key from a different key vault, where each key vault must use **a different identity** for authentication. Because a search service can only have one managed identity, a requirement for multiple identities rules out the simplified approach for your scenario.  
+![Screenshot of turn on system assigned managed identity.](./media/search-managed-identities/turn-on-system-assigned-identity.png "Screenshot showing how to turn on the system-assigned managed identity.")
 
 ### [**User-managed identity (preview)**](#tab/managed-id-user)
 
 > [!IMPORTANT] 
-> User-managed identity support is in public preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> User-managed identity support for CMK is in public preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 > 
 > 2021-04-01-Preview of the [Management REST API](/rest/api/searchmanagement/) introduced this feature.
 
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
-1. Select **+ Create a new resource**.
+1. Select **Create a new resource**.
 
 1. In the "Search services and marketplace" search bar, search for "User Assigned Managed Identity" and then select **Create**.
 
 1. Give the identity a descriptive name.
 
-1. Next, assign the user-managed identity to the search service. This can be done using the latest preview [2024-06-01-preview](/rest/api/searchmanagement/management-api-versions) management API.
+1. Next, assign the user-managed identity to the search service. This can be done using the latest preview [2024-06-01-preview](/rest/api/searchmanagement/management-api-versions) management API or the previous preview.
 
     The identity property takes a type and one or more fully qualified user-assigned identities:
-    
+  
     * **type** is the type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes both an identity created by the system and a set of user assigned identities. The type 'None' removes all identities from the service.
     * **userAssignedIdentities** includes the details of the user-managed identity.
         * User-managed identity format: 
             * /subscriptions/**subscription ID**/resourcegroups/**resource group name**/providers/Microsoft.ManagedIdentity/userAssignedIdentities/**managed identity name**
-    
+  
     Example of how to assign a user-managed identity to a search service:
-    
+  
     ```http
     PUT https://management.azure.com/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Search/searchServices/[search service name]?api-version=2024-06-01-preview
     Content-Type: application/json
@@ -265,49 +214,39 @@ Conditions that prevent you from adopting this approach include:
 
 ---
 
-## 4 - Grant permissions
-
-In this step, you create an access policy in Key Vault. This policy gives the application you registered with Microsoft Entra ID permission to use your customer-managed key.
-
-Access permissions could be revoked at any given time. Once revoked, any search service index or synonym map that uses that key vault become unusable. Restoring key vault access permissions at a later time restores index and synonym map access. For more information, see [Secure access to a key vault](/azure/key-vault/general/security-features).
+## Step 3: Grant permissions
 
-1. Still in the Azure portal, open your key vault **Overview** page. 
+Azure Key Vault supports authorization using role-based access controls. We recommend this approach over key vault access policies. For more information, see [Provide access to Key Vault keys, certificates, and secrets using Azure roles](/azure/key-vault/general/rbac-guide).
 
-1. Select the **Access policies** on the left, and select **+ Create** to start the **Create an access policy** wizard.
+In this step, assign the **Key Vault Crypto Service Encryption User** role to your search service. If you're testing locally, assign this role to yourself as well.
 
-   :::image type="content" source="media/search-manage-encryption-keys/cmk-add-access-policy.png" alt-text="Create an access policy." border="true":::
+1. Sign in to the [Azure portal](https://portal.azure.com) and find your key vault.
 
-1. On the **Permissions** page, select *Get* for **Key permissions**, **Secret permissions**, and **Certificate Permissions**. Select *Unwrap Key* and *Wrap Key* for ** cryptographic operations on the key.
+1. Select **Access control (IAM)** and select **Add role assignment**.
 
-   :::image type="content" source="media/search-manage-encryption-keys/cmk-access-policy-permissions.png" alt-text="Select permissions in the Permissions page." border="true":::
+1. Select **Key Vault Crypto Service Encryption User** and then select **Next**.
 
-1. Select **Next**.
+1. Select managed identities, select members, and then select the managed identity of your search service.
 
-1. On the **Principle** page, find and select the security principal used by the search service to access the encryption key. This will either be the system-managed or user-managed identity of the search service, or the registered application.
-
-1. Select **Next** and **Create**.
-
-> [!Important]
-> Encrypted content in Azure AI Search is configured to use a specific Azure Key Vault key with a specific **version**. If you change the key or version, the index or synonym map must be updated to use it **before** you delete the previous one. 
-> Failing to do so will render the index or synonym map unusable. You won't be able to decrypt the content if the key is lost.
+1. Select **Review + Assign**.
 
-<a name="encrypt-content"></a>
+Wait a few minutes for the role assignment to become operational.
 
-## 5 - Encrypt content
+## Step 4: Encrypt content
 
-Encryption keys are added when you create an object. To add a customer-managed key on an index, synonym map, indexer, data source, or skillset, use the [Search REST API](/rest/api/searchservice/) or an Azure SDK to create an object that has encryption enabled. The portal doesn't allow encryption properties on object creation. 
+Encryption keys are added when you create an object. To add a customer-managed key on an index, synonym map, indexer, data source, or skillset, use the [Search REST API](/rest/api/searchservice/) or an Azure SDK to create an object that has encryption enabled. To add encryption using the Azure SDK, see the [Python example](#python-example-of-an-encryption-key-configuration) in this article.
 
-1. Call the Create APIs to specify the **encryptionKey** property:
+1. Call the creation APIs to specify the **encryptionKey** property:
 
    + [Create Index](/rest/api/searchservice/indexes/create)
    + [Create Synonym Map](/rest/api/searchservice/synonym-maps/create)
    + [Create Indexer](/rest/api/searchservice/indexers/create)
    + [Create Data Source](/rest/api/searchservice/data-sources/create)
    + [Create Skillset](/rest/api/searchservice/skillsets/create)
 
-1. Insert the encryptionKey construct into the object definition. This property is a first-level property, on the same level as name and description. The following [REST examples](#rest-examples) show property placement. If you're using the same vault, key, and version, you can paste in the same "encryptionKey" construct into each object definition.
+1. Insert the encryptionKey construct into the object definition. This property is a first-level property, on the same level as name and description. If you're using the same vault, key, and version, you can paste in the same encryptionKey construct into each object definition.
 
-   The first example shows an "encryptionKey" for a search service that connects using a managed identity:
+   The first example shows an encryptionKey for a search service that connects using a managed identity:
 
     ```json
     {
@@ -319,7 +258,7 @@ Encryption keys are added when you create an object. To add a customer-managed k
     }
     ```
 
-    The second example includes "accessCredentials", necessary if you registered an application in Microsoft Entra ID:
+    The second example includes accessCredentials, necessary if you registered an application in Microsoft Entra ID:
 
     ```json
     {
@@ -335,14 +274,46 @@ Encryption keys are added when you create an object. To add a customer-managed k
     }
     ```
 
+1. Verify the encryption key exists by issuing a GET on the object.
+
+   + [GET Index](/rest/api/searchservice/indexes/get)
+   + [GET Synonym Map](/rest/api/searchservice/synonym-maps/get)
+   + [GET Indexer](/rest/api/searchservice/indexers/get)
+   + [GET Data Source](/rest/api/searchservice/data-sources/get)
+   + [GET Skillset](/rest/api/searchservice/skillsets/get)
+
+1. Verify the object is operational by performing a task, such as query an index that's been encrypted.
+
 Once you create the encrypted object on the search service, you can use it as you would any other object of its type. Encryption is transparent to the user and developer.
 
-> [!Note]
-> None of these key vault details are considered secret and could be easily retrieved by browsing to the relevant Azure Key Vault page in Azure portal.
+None of these key vault details are considered secret and could be easily retrieved by browsing to the relevant Azure Key Vault page in Azure portal.
+
+> [!Important]
+> Encrypted content in Azure AI Search is configured to use a specific Azure Key Vault key with a specific *version*. If you change the key or version, the object must be updated to use it **before** you delete the previous one. Failing to do so renders the object unusable. You won't be able to decrypt the content if the key is lost.
+
+## Step 5: Test encryption
+
+To verify encryption is working, revoke the encryption key, query the index (it should be unusable), and then reinstate the encryption key.
+
+Use the Azure portal for this task.
+
+1. On the Azure Key Vault page, select **Objects** > **Keys**.
+
+1. Select the key you just created, and then select **Delete**.
+
+1. On the Azure AI Search page, select **Search management** > **Indexes**.
+
+1. Select your index and use Search Explorer to run a query. You should get an error.
+
+1. Return to the Azure Key Vault **Objects** > **Keys** page.
 
-<a name="encryption-enforcement-policy"></a>
+1. Select **Manage deleted keys**.
 
-## 6 - Set up policy
+1. Select your key, and then select **Recover**. 
+
+1. Return to your index in Azure AI Search and rerun the query. You should see search results. If you don't see immediate results, wait a minute and try again.
+
+## Set up a policy to enforce CMK compliance
 
 Azure policies help to enforce organizational standards and to assess compliance at-scale. Azure AI Search has an optional [built-in policy for service-wide CMK enforcement](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F76a56461-9dc0-40f0-82f5-2453283afa2f).
 
@@ -374,161 +345,166 @@ PATCH https://management.azure.com/subscriptions/<your-subscription-Id>/resource
 }
 ```
 
-## REST examples
+## Rotate or update encryption keys
 
-This section shows the JSON for several objects so that you can see where to locate "encryptionKey" in an object definition.
+We recommend using the [autorotation capabilities of Azure Key Vault](/azure/key-vault/keys/how-to-configure-key-rotation), but you can also rotate keys manually.
 
-### Index encryption
+When you change a key or its version, any object that uses the key must first be updated to use the new values **before** you delete the old values. Otherwise, the object becomes unusable because it can't be decrypted. 
 
-The details of creating a new index via the REST API could be found at [Create Index (REST API)](/rest/api/searchservice/indexes/create), where the only difference is specifying the encryption key details as part of the index definition:
+1. [Determine the key used by an index or synonym map](search-security-get-encryption-keys.md).
 
-```json
-{
- "name": "hotels",
- "fields": [
-  {"name": "HotelId", "type": "Edm.String", "key": true, "filterable": true},
-  {"name": "HotelName", "type": "Edm.String", "searchable": true, "filterable": false, "sortable": true, "facetable": false},
-  {"name": "Description", "type": "Edm.String", "searchable": true, "filterable": false, "sortable": false, "facetable": false, "analyzer": "en.lucene"},
-  {"name": "Description_fr", "type": "Edm.String", "searchable": true, "filterable": false, "sortable": false, "facetable": false, "analyzer": "fr.lucene"},
-  {"name": "Category", "type": "Edm.String", "searchable": true, "filterable": true, "sortable": true, "facetable": true},
-  {"name": "Tags", "type": "Collection(Edm.String)", "searchable": true, "filterable": true, "sortable": false, "facetable": true},
-  {"name": "ParkingIncluded", "type": "Edm.Boolean", "filterable": true, "sortable": true, "facetable": true},
-  {"name": "LastRenovationDate", "type": "Edm.DateTimeOffset", "filterable": true, "sortable": true, "facetable": true},
-  {"name": "Rating", "type": "Edm.Double", "filterable": true, "sortable": true, "facetable": true},
-  {"name": "Location", "type": "Edm.GeographyPoint", "filterable": true, "sortable": true}
- ],
-  "encryptionKey": {
-    "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
-    "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
-    "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
-    "accessCredentials": {
-      "applicationId": "<YOUR-APPLICATION-ID>",
-      "applicationSecret": "<YOUR-APPLICATION-SECRET>"
-    }
-  }
-}
-```
+1. [Create a new key in key vault](/azure/key-vault/keys/quick-create-portal), but leave the original key available.
 
-You can now send the index creation request, and then start using the index normally.
+1. [Update the encryptionKey properties](/rest/api/searchservice/indexes/create-or-update) on an index or synonym map to use the new values. Only objects that were originally created with this property can be updated to use a different value.
 
-### Synonym map encryption
+1. Disable or delete the previous key in the key vault. Monitor key access to verify the new key is being used.
 
-Create an encrypted synonym map using the [Create Synonym Map Azure AI Search REST API](/rest/api/searchservice/synonym-maps/create). Use the "encryptionKey" property to specify which encryption key to use.
+For performance reasons, the search service caches the key for up to several hours. If you disable or delete the key without providing a new one, queries continue to work on a temporary basis until the cache expires. However, once the search service can no longer decrypt content, you get this message: "Access forbidden. The query key used might have been revoked - please retry." 
 
-```json
-{
-  "name" : "synonymmap1",
-  "format" : "solr",
-  "synonyms" : "United States, United States of America, USA\n
-  Washington, Wash. => WA",
-  "encryptionKey": {
-    "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
-    "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
-    "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
-    "accessCredentials": {
-      "applicationId": "<YOUR-APPLICATION-ID>",
-      "applicationSecret": "<YOUR-APPLICATION-SECRET>"
-    }
-  }
-}
-```
+## Work with encrypted content
 
-You can now send the synonym map creation request, and then start using it normally.
+With customer-managed key encryption, you might notice latency for both indexing and queries due to the extra encrypt/decrypt work. Azure AI Search doesn't log encryption activity, but you can monitor key access through key vault logging. 
 
-### Data source encryption
+We recommend that you [enable logging](/azure/key-vault/general/logging) as part of key vault configuration.
 
-Create an encrypted data source using the [Create Data Source (REST API)](/rest/api/searchservice/data-sources/create). Use the "encryptionKey" property to specify which encryption key to use.
+1. [Create a log analytics workspace](/azure/azure-monitor/logs/quick-create-workspace).
 
-```json
-{
-  "name" : "datasource1",
-  "type" : "azureblob",
-  "credentials" :
-  { "connectionString" : "DefaultEndpointsProtocol=https;AccountName=datasource;AccountKey=accountkey;EndpointSuffix=core.windows.net"
-  },
-  "container" : { "name" : "containername" },
-  "encryptionKey": {
-    "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
-    "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
-    "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
-    "accessCredentials": {
-      "applicationId": "<YOUR-APPLICATION-ID>",
-      "applicationSecret": "<YOUR-APPLICATION-SECRET>"
-    }
-  }
-}
-```
+1. [Add a diagnostic setting in key vault](/azure/key-vault/general/howto-logging) that uses the workspace for data retention. 
 
-You can now send the data source creation request, and then start using it normally.
+1. Select **audit** or **allLogs** for the category, give the diagnostic setting a name, and then save it.
 
-### Skillset encryption
+## Python example of an encryption key configuration
 
-Create an encrypted skillset using the [Create Skillset REST API](/rest/api/searchservice/skillsets/create). Use the "encryptionKey" property to specify which encryption key to use.
+This section shows the Python representation of an `encryptionKey` in an object definition. The same definition applies to indexes, data sources, skillets, indexers, and synonym maps. To try this example on your search service and key vault, download the notebook from [azure-search-python-samples](https://github.com/Azure-Samples/azure-search-python-samples).
 
-```json
-{
-    "name": "skillset1",
-    "skills":  [ omitted for brevity ],
-    "cognitiveServices": { omitted for brevity },
-      "knowledgeStore":  { omitted for brevity  },
-    "encryptionKey": (optional) { 
-        "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
-        "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
-        "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
-        "accessCredentials": {
-          "applicationId": "<YOUR-APPLICATION-ID>",
-          "applicationSecret": "<YOUR-APPLICATION-SECRET>"
-    }
-}
+Install some packages.
+
+```python
+! pip install python-dotenv
+! pip install azure-core
+! pip install azure-search-documents==11.5.1
+! pip install azure-identity
 ```
 
-You can now send the skillset creation request, and then start using it normally.
+Create an index that has an encryption key.
+
+```python
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import (
+    SimpleField,
+    SearchFieldDataType,
+    SearchableField,
+    SearchIndex,
+    SearchResourceEncryptionKey
+)
+from azure.identity import DefaultAzureCredential
+
+endpoint="<PUT YOUR AZURE SEARCH SERVICE ENDPOINT HERE>"
+credential = DefaultAzureCredential()
+
+index_name = "test-cmk-index"
+index_client = SearchIndexClient(endpoint=endpoint, credential=credential)  
+fields = [
+        SimpleField(name="Id", type=SearchFieldDataType.String, key=True),
+        SearchableField(name="Description", type=SearchFieldDataType.String)
+    ]
+
+scoring_profiles = []
+suggester = []
+encryption_key = SearchResourceEncryptionKey(
+    key_name="<PUT YOUR KEY VAULT NAME HERE>",
+    key_version="<PUT YOUR ALPHANUMERIC KEY VERSION HERE>",
+    vault_uri="<PUT YOUR KEY VAULT ENDPOINT HERE>"
+)
+
+index = SearchIndex(name=index_name, fields=fields, encryption_key=encryption_key)
+result = index_client.create_or_update_index(index)
+print(f' {result.name} created')
+```
 
-### Indexer encryption
+Get the index definition to verify encryption key configuration exists.
 
-Create an encrypted indexer using the [Create Indexer REST API](/rest/api/searchservice/indexers/create). Use the "encryptionKey" property to specify which encryption key to use.
+```python
+index_name = "test-cmk-index-qs"
+index_client = SearchIndexClient(endpoint=AZURE_SEARCH_SERVICE, credential=credential)  
 
-```json
-{
-  "name": "indexer1",
-  "dataSourceName": "datasource1",
-  "skillsetName": "skillset1",
-  "parameters": {
-      "configuration": {
-          "imageAction": "generateNormalizedImages"
-      }
-  },
-  "encryptionKey": {
-    "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
-    "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
-    "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
-    "accessCredentials": {
-      "applicationId": "<YOUR-APPLICATION-ID>",
-      "applicationSecret": "<YOUR-APPLICATION-SECRET>"
-    }
-  }
-}
+result = index_client.get_index(index_name)  
+print(f"{result}")  
 ```
 
-You can now send the indexer creation request, and then start using it normally.
+Load the index with a few documents. All field content is considered sensitive and is encrypted on disk using your customer managed key.
 
->[!Important]
-> While "encryptionKey" can't be added to existing search indexes or synonym maps, it may be updated by providing different values for any of the three key vault details (for example, updating the key version). 
-> When changing to a new Key Vault key or a new key version, any search index or synonym map that uses the key must first be updated to use the new key\version **before** deleting the previous key\version. 
-> Failing to do so will render the index or synonym map unusable, as it won't be able to decrypt the content once key access is lost. Although restoring key vault access permissions at a later time will restore content access.
+```python
+from azure.search.documents import SearchClient
 
-## Work with encrypted content
+# Create a documents payload
+documents = [
+    {
+    "@search.action": "upload",
+    "Id": "1",
+    "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities."
+    },
+    {
+    "@search.action": "upload",
+    "Id": "2",
+    "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts."
+    },
+    {
+    "@search.action": "upload",
+    "Id": "3",
+    "Description": "The hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel's restaurant services."
+    },
+    {
+    "@search.action": "upload",
+    "Id": "4",
+    "Description": "The hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 1800 palace."
+    }
+]
 
-With customer-managed key encryption, you might notice latency for both indexing and queries due to the extra encrypt/decrypt work. Azure AI Search doesn't log encryption activity, but you can monitor key access through key vault logging. We recommend that you [enable logging](/azure/key-vault/general/logging) as part of key vault configuration.
+search_client = SearchClient(endpoint=AZURE_SEARCH_SERVICE, index_name=index_name, credential=credential)
+try:
+    result = search_client.upload_documents(documents=documents)
+    print("Upload of new document succeeded: {}".format(result[0].succeeded))
+except Exception as ex:
+    print (ex.message)
 
-Key rotation is expected to occur over time. Whenever you rotate keys, it's important to follow this sequence:
+    index_client = SearchClient(endpoint=AZURE_SEARCH_SERVICE, credential=credential)
+```
 
-1. [Determine the key used by an index or synonym map](search-security-get-encryption-keys.md).
-1. [Create a new key in key vault](/azure/key-vault/keys/quick-create-portal), but leave the original key available.
-1. [Update the encryptionKey properties](/rest/api/searchservice/indexes/create-or-update) on an index or synonym map to use the new values. Only objects that were originally created with this property can be updated to use a different value.
-1. Disable or delete the previous key in the key vault. Monitor key access to verify the new key is being used.
+Run a query to confirm the index is operational.
+
+```python
+from azure.search.documents import SearchClient
+
+query = "historic"  
+
+search_client = SearchClient(endpoint=AZURE_SEARCH_SERVICE, credential=credential, index_name=index_name)
+  
+results = search_client.search(  
+    query_type='simple',
+    search_text=query, 
+    select=["Id", "Description"],
+    include_total_count=True
+    )
+  
+for result in results:  
+    print(f"Score: {result['@search.score']}")
+    print(f"Id: {result['Id']}")
+    print(f"Description: {result['Description']}")
+```
 
-For performance reasons, the search service caches the key for up to several hours. If you disable or delete the key without providing a new one, queries continue to work on a temporary basis until the cache expires. However, once the search service can no longer decrypt content, you get this message: "Access forbidden. The query key used might have been revoked - please retry." 
+Output from the query should produce results similar to the following example.
+
+```
+Score: 0.6130029
+Id: 4
+Description: The hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 1800 palace.
+Score: 0.26286605
+Id: 1
+Description: The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.
+```
+
+Since encrypted content is decrypted prior to data refresh or queries, you won't see visual evidence of encryption. To verify encryption is working, check the resource logs.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "暗号鍵管理のプロセス手順の更新と整理"
}
```

### Explanation
このコードの差分は、Azure AI 検索サービスにおける暗号鍵の管理に関する文書「暗号鍵の管理方法」に対する大幅な更新と整理を示しています。主な変更点として、顧客管理鍵（CMK）または「持ち込み鍵」（BYOK）暗号化を設定する手順が詳細に記述され、プロセスが段階的に整理されました。これにより、ユーザーは暗号鍵の管理と利用に関する手順をより明確に理解できるようになっています。

特に、CMKの設定方法、適用対象、暗号化の効果、およびAzure Key Vaultの役割に関する情報が追加されており、具体的な手順や注意喚起、制限事項が詳細に示されています。また、暗号化のパフォーマンスに関する考慮事項も含まれており、プロセス中に直面する可能性のある問題やそれに対する推奨事項も整理されています。

この更新により、ユーザーは鍵の生成、アクセス制御の設定、CMKを使用したオブジェクトの暗号化、鍵のローテーションや更新方法の理解を深めることができ、特にセキュリティを重視するシナリオにおいて適切な対策を講じることが可能になります。

## articles/search/tutorial-rag-build-solution-query.md{#item-93965f}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: tutorial
-ms.date: 10/01/2024
+ms.date: 10/03/2024
 
 ---
 
@@ -90,14 +90,17 @@ Sources:\n{sources}
 """
 
 # Provide the query. Notice it's sent to both the search engine and the LLM.
+# The query sent to the search engine is hybrid. Keyword search on "query". Text-to-vector conversion for vector search.
 query="how much of earth is covered by water"
+vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=1, fields="text_vector", exhaustive=True)
 
 # Set up the search results and the chat thread.
 # Retrieve the selected fields from the search index related to the question.
 search_results = search_client.search(
     search_text=query,
+    vector_queries= [vector_query],
+    select="title, chunk, locations",
     top=1,
-    select="title, chunk, locations"
 )
 sources_formatted = "\n".join([f'{document["title"]}:{document["chunk"]}:{document["locations"]}' for document in search_results])
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションクエリのチュートリアルの更新"
}
```

### Explanation
このコードの差分は、「RAGソリューションのクエリ構築」に関するチュートリアルの軽微な更新を示しています。主な変更点は、日付の修正に加え、検索エンジンと大規模言語モデル（LLM）へのクエリの送信方法についての詳細が追加された点です。

具体的には、クエリがどのように検索エンジンとLLMに送信されるかについての説明が強調され、クエリはハイブリッドであることが明記されています。これにより、キーワード検索とベクトル検索を併用する方法が明示され、ユーザーはどのように検索を実行するかをより深く理解できるようになっています。

また、テキストからベクトルへの変換を行うために`VectorizableTextQuery`が使用されていることも記載されており、これにより検索プロセスの具体的な手法が示されています。全体を通じて、更新された内容は、ユーザーがRAGソリューションの実装をより効果的に行えるようにするための重要な情報を提供しています。


