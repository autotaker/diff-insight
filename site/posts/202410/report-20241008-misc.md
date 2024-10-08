---
date: '2024-10-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:43a3b87...MicrosoftDocs:e9690f5
summary: この変更では、Azure AI Studioに関する文書のリンクや構造が更新され、新たに顧客管理キー（CMK）に関する詳細な文書が追加されました。これにより、利用者は自分の暗号化キーを管理できるようになり、データのセキュリティが強化されます。目次も更新され、関連リンクが調整されており、使いやすさが向上しています。特に破壊的な変更はありませんが、文書のリンクが変更されたため、新しいリンク先を確認する必要があります。この更新は、利用者が情報を迅速に取得できるようにし、Azure
  AI Studioの利用を促進することを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:43a3b87...MicrosoftDocs:e9690f5){target="_blank"}

# ハイライト
この変更では、Azure AI Studioに関する文書のリンクや構造が更新され、新しい機能として顧客管理キー（CMK）に関する詳細な文書が追加されました。これにより、利用者はデータのセキュリティ対策として自身の暗号化キーを管理できるようになりました。その他、目次（TOC）も更新され、関連リンクが調整されました。

## 新機能
- 「Azure AI Studioのための顧客管理キーに関する新しい文書」が追加。この文書では、顧客が自分の暗号化キーを管理する際の方法や手順について詳しく説明され、データセキュリティの強化が図られています。

## 破壊的変更
- 特に破壊的な変更は含まれていませんが、文書リンクの更新により、ユーザーは新しいリンク先を確認する必要があります。

## その他の更新
- アーキテクチャ関連文書内のリンク更新。
- 目次（TOC）のリンクが整理され、利用者が容易に情報を見つけられるように改良されました。

# インサイト
今回の更新は、Azure AI Studioの利用者に対する文書の改善と新しいセキュリティ機能の提供を目的としています。データ保護は現代のクラウドサービスにおいて極めて重要な要素となっており、特に企業利用者はその必要性を感じています。新たに提供された顧客管理キー（CMK）の文書は、そのニーズに応えるものとして評価されるでしょう。利用者は自社のセキュリティポリシーに基づき、鍵管理を自ら行うことで、データの保護に対する信頼性を高めることが可能となります。

さらに、リンクや目次の更新は、ユーザーエクスペリエンスの向上を意図しており、必要な情報を素早く取得するためのナビゲーションを改善することに寄与しています。これにより、Azure AI Studioを活用したプロジェクトが円滑に進められることが期待されます。

このように、今回の変更は主に利便性と信頼性の向上を図っており、Azure AI Studioの採用を促進する要因となるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [architecture.md](#item-22ed18) | minor update | アーキテクチャに関する文書のリンクを更新 | modified | 1 | 1 | 2 | 
| [encryption-keys-portal.md](#item-95428d) | new feature | Azure AI Studioのための顧客管理キーに関する新しい文書の追加 | added | 103 | 0 | 103 | 
| [toc.yml](#item-2745cd) | minor update | TOCのリンク更新と新規追加 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-studio/concepts/architecture.md{#item-22ed18}

<details>
<summary>Diff</summary>
````diff
@@ -74,7 +74,7 @@ While most of the resources used by Azure AI Studio live in your Azure subscript
 - **Metadata storage**: Provided by Azure Storage resources in the Microsoft subscription.  
 
     > [!NOTE]
-    > If you use customer-managed keys, the metadata storage resources are created in your subscription. For more information, see [Customer-managed keys](../../ai-services/encryption/cognitive-services-encryption-keys-portal.md?context=/azure/ai-studio/context/context).
+    > If you use customer-managed keys, the metadata storage resources are created in your subscription. For more information, see [Customer-managed keys](encryption-keys-portal.md).
 
 Managed compute resources and managed virtual networks exist in the Microsoft subscription, but you manage them. For example, you control which VM sizes are used for compute resources, and which outbound rules are configured for the managed virtual network.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アーキテクチャに関する文書のリンクを更新"
}
```

### Explanation
この変更では、Azure AI Studioのアーキテクチャに関する文書の内容が少し変更され、顧客管理キーに関する情報のリンクが更新されました。具体的には、元のリンクから新しいリンクに修正されています。これにより、より適切な参照先が提供され、利用者が必要な情報にアクセスしやすくなります。この修正は、文書の質を向上させるための小さな更新と見なされます。

## articles/ai-studio/concepts/encryption-keys-portal.md{#item-95428d}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,103 @@
+---
+title: Customer-Managed Keys for Azure AI Studio
+titleSuffix: Azure AI Studio
+description: Learn about using customer-managed keys for encryption to improve data security with Azure AI Studio.
+author: Blackmist
+ms.author: larryfr
+ms.service: azure-ai-services
+ms.custom:
+  - ignite-2023
+ms.topic: concept-article
+ms.date: 10/7/2024
+ms.reviewer: deeikele
+# Customer intent: As an admin, I want to understand how I can use my own encryption keys with Azure AI Studio.
+---
+
+# Customer-managed keys for encryption with Azure AI Studio
+
+Customer-managed keys (CMKs) in Azure AI Studio provide enhanced control over the encryption of your data. By using CMKs, you can manage your own encryption keys to add an extra layer of protection and meet compliance requirements more effectively.
+
+## About encryption in Azure AI Studio
+
+Azure AI Studio layers on top of Azure Machine Learning and Azure AI services. By default, these services use Microsoft-managed encryption keys. 
+
+Hub and project resources are implementations of the Azure Machine Learning workspace and encrypt data in transit and at rest. For details, see [Data encryption with Azure Machine Learning](../../machine-learning/concept-data-encryption.md).
+
+Azure AI services data is encrypted and decrypted using [FIPS 140-2](https://en.wikipedia.org/wiki/FIPS_140-2) compliant [256-bit AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) encryption. Encryption and decryption are transparent, meaning encryption and access are managed for you. Your data is secure by default and you don't need to modify your code or applications to take advantage of encryption.
+
+## Data storage in your subscription when using customer-managed keys
+
+Hub resources store metadata in your Azure subscription when using customer-managed keys. Data is stored in a Microsoft-managed resource group that includes an Azure Storage account, Azure Cosmos DB resource and Azure AI Search. 
+
+> [!IMPORTANT]
+> When using a customer-managed key, the costs for your subscription will be higher because encrypted data is stored in your subscription. To estimate the cost, use the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/).
+
+The encryption key you provide when creating a hub is used to encrypt data that is stored on Microsoft-managed resources. All projects using the same hub store data on the resources in a managed resource group identified by the name `azureml-rg-hubworkspacename_GUID`. Projects use Microsoft Entra ID authentication when interacting with these resources. If your hub has a private link endpoint, network access to the managed resources is restricted. The managed resource group is deleted, when the hub is deleted. 
+
+The following data is stored on the managed resources.
+
+|Service|What it's used for|Example|
+|-----|-----|-----|
+|Azure Cosmos DB|Stores metadata for your Azure AI projects and tools|Index names, tags; Flow creation timestamps; deployment tags; evaluation metrics|
+|Azure AI Search|Stores indices that are used to help query your AI studio content.|An index based off your model deployment names|
+|Azure Storage Account|Stores instructions for how customization tasks are orchestrated|JSON representation of flows you create in AI Studio|
+
+>[!IMPORTANT]
+> Azure AI Studio uses Azure compute that is managed in the Microsoft subscription, for example when you fine-tune models or or build flows. Its disks are encrypted with Microsoft-managed keys. Compute is ephemeral, meaning after a task is completed the virtual machine is deprovisioned, and the OS disk is deleted. Compute instance machines used for 'Code' experiences are persistant. Azure Disk Encryption isn't supported for the OS disk. 
+
+## (Preview) Service-side storage of encrypted data when using customer-managed keys
+
+A new architecture for customer-managed key encryption with hubs is available in preview, which resolves the dependency on the managed resource group. In this new model, encrypted data is stored service-side on Microsoft-managed resources instead of in managed resources in your subscription. Metadata is stored in multitenant resources using document-level CMK encryption. An Azure AI Search instance is hosted on the Microsoft-side per customer, and for each hub. Due to its dedicated resource model, its Azure cost is charged in your subscription via the hub resource.
+
+> [!NOTE]
+> During this preview key rotation and user-assigned identity capabilities are not supported. Server-side encryption is currently not supported in reference to an Azure Key Vault for storing your encryption key that has public network access disabled.
+
+## Use customer-managed keys with Azure Key Vault
+
+You must use Azure Key Vault to store your customer-managed keys. You can either create your own keys and store them in a key vault, or you can use the Azure Key Vault APIs to generate keys. The Azure AI services resource and the key vault must be in the same region and in the same Microsoft Entra tenant, but they can be in different subscriptions. For more information about Azure Key Vault, see [What is Azure Key Vault?](/azure/key-vault/general/overview).
+
+To enable customer-managed keys, the key vault containing your keys must meet these requirements:
+
+- You must enable both the **Soft Delete** and **Do Not Purge** properties on the key vault.
+- If you use the [Key Vault firewall](/azure/key-vault/general/access-behind-firewall), you must allow trusted Microsoft services to access the key vault.
+- You must grant your hub's and Azure AI Services resource's system-assigned managed identity the following permissions on your key vault: *get key*, *wrap key*, *unwrap key*.
+
+The following limitations hold for Azure AI Services:
+- Only Azure Key Vault with [legacy access policies](/azure/key-vault/general/assign-access-policy) are supported.
+- Only RSA and RSA-HSM keys of size 2048 are supported with Azure AI services encryption. For more information about keys, see **Key Vault keys** in [About Azure Key Vault keys, secrets, and certificates](/azure/key-vault/general/about-keys-secrets-certificates).
+
+### Enable your Azure AI Services resource's managed identity
+
+If connecting with Azure AI Services, or variants of Azure AI Services such as Azure OpenAI, you need to enable managed identity as a prerequisite for using customer-managed keys.
+
+1. Go to your Azure AI services resource.
+1. On the left, under **Resource Management**, select **Identity**.
+1. Switch the system-assigned managed identity status to **On**.
+1. Save your changes, and confirm that you want to enable the system-assigned managed identity.
+
+## Enable customer-managed keys
+
+Azure AI studio builds on hub as implementation of Azure Machine Learning workspace, Azure AI Services, and lets you connect with other resources in Azure. You must set encryption specifically on each resource.
+
+Customer-managed key encryption is configured via Azure portal in a similar way for each Azure resource:
+1. Create a new Azure resource in Azure portal.
+1. Under the encryption tab, select your encryption key.
+
+:::image type="content" source="../../machine-learning/media/concept-customer-managed-keys/cmk-service-side-encryption.png" alt-text="Screenshot of the encryption tab with the option for server side encryption selected." lightbox="../../machine-learning/media/concept-customer-managed-keys/cmk-service-side-encryption.png":::
+
+Alternatively, use infrastructure-as-code options for automation. Example Bicep templates for Azure AI Studio are available on the Azure Quickstart repo:
+1. [CMK encryption for hub](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aistudio-cmk).
+1. [Service-side CMK encryption preview for hub](https://github.com/azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-cmk-service-side-encryption).
+
+## Limitations
+
+* The customer-managed key for encryption can only be updated to keys in the same Azure Key Vault instance.
+* After deployment, hubs can't switch from Microsoft-managed keys to Customer-managed keys or vice versa.
+* [Azure AI services Customer-Managed Key Request Form](https://aka.ms/cogsvc-cmk) is required to use customer-managed keys in combination with Azure Speech and Content Moderator capabilities.
+* At the time of creation, you can't provide or modify resources that are created in the Microsoft-managed Azure resource group in your subscription.
+* You can't delete Microsoft-managed resources used for customer-managed keys without also deleting your hub.
+* [Azure AI services Customer-Managed Key Request Form](https://aka.ms/cogsvc-cmk) is still required for Speech and Content Moderator.
+
+## Related content
+
+* [What is Azure Key Vault](/azure/key-vault/general/overview)?
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Studioのための顧客管理キーに関する新しい文書の追加"
}
```

### Explanation
この変更では、Azure AI Studioにおける顧客管理キー（CMK）を使用した暗号化に関する新しい文書が追加されました。この文書は、データのセキュリティを向上させるためにCMKを使う方法について詳しく説明しており、顧客が自分の暗号化キーを管理することで、より高い制御を得られることを強調しています。

文書では、暗号化の基本、顧客管理キーを使用する際のデータストレージ、Azure Key Vaultの利用方法、ならびに使用上の制限事項について包括的に説明されています。また、顧客管理キーの有効化手順や、その設定方法についても具体的に案内されています。この新しい機能は、Azure AI Studioを利用するユーザーにとって重要な情報源となります。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -324,10 +324,10 @@ items:
         href: how-to/troubleshoot-secure-connection-project.md
     - name: Data protection & encryption
       items:
+      - name: Configure customer-managed keys
+        href: concepts/encryption-keys-portal.md
       - name: Rotate keys
         href: ../ai-services/rotate-keys.md?context=/azure/ai-studio/context/context
-      - name: Configure customer-managed keys
-        href: ../ai-services/encryption/cognitive-services-encryption-keys-portal.md?context=/azure/ai-studio/context/context
     - name: Vulnerability management
       href: concepts/vulnerability-management.md
     - name: Disaster recovery
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCのリンク更新と新規追加"
}
```

### Explanation
この変更では、Azure AI Studioに関する目次（TOC）が更新され、リンクの追加と編集が行われました。具体的には、顧客管理キーの設定に関連する文書へのリンクが新たに追加され、以前のリンクが削除されています。新しいリンクは「概念 / 暗号化キーのポータル」へのもので、より具体的な情報を提供することを目的としています。また、リンクの整理により、ユーザーがリソースを見つけやすくなっています。この修正は、文書の利便性を向上させるための小さな更新と見なされます。


