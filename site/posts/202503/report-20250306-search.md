---
date: '2025-03-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:71adf7f...MicrosoftDocs:31c2d64
summary: このコード差分の主なポイントは、ドキュメントの小規模な更新と修正です。主な変更としては、暗号化キー管理に関する詳細なガイダンスが充実し、コードの可読性と整合性が改善されました。具体的には、引数名が明示化され、SAP
  HANAコネクタの最新のリンクが更新されました。また、`search-security-manage-encryption-keys.md`ファイルには、Azureポリシーの設定とCMKの使用に関する包括的なガイダンスが追加されました。この更新により、ユーザーは最新の情報を基にサービスの構成や管理をより効率的に行えるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:71adf7f...MicrosoftDocs:31c2d64){target="_blank"}

# Highlights
このコード差分の主なポイントは、ドキュメントの小規模な更新と修正です。以下の3つのファイルに変更が加えられています：

## 新しい機能
- 特に新機能の追加はありませんが、暗号化キー管理に関する詳細なガイダンスが充実しています。

## 大きな変更点
- 各引数名の明示化により、コードの可読性と整合性が改善されました。
- SAP HANAコネクタの最新リンクが更新されることで、正確な情報とアクセスが保証されます。

## その他の更新
- `search-security-manage-encryption-keys.md`ファイルでは、Azureポリシーの設定とCMKの使用に関する包括的なガイダンスが追加されました。

# Insights
このドキュメント更新は、可読性や整合性、情報の正確性を向上させることを目的としています。特に、キーレス接続やコネクタ情報、暗号化キー管理に関する詳細が精査され、ユーザーが必要な情報をより容易に取得できるようになっています。ユーザーはこれにより、最新のガイダンスに基づいて実際の構成や設定を進めることができ、その結果、サービスのセットアップや管理がより効率的になります。

具体的には、`SearchClient`の引数名の変更によりコードの意味が明確になり、SAP HANAコネクタのリンク更新で最新情報へのアクセスが可能になりました。また、`search-security-manage-encryption-keys.md`に関しては、新たなポリシー設定とAPIコマンドの具体例が追加されることで、実際の運用や管理に役立つ実用的なステップが提示されています。これにより、企業はコンプライアンス要件を一貫して満たし続けることができるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [keyless-connections.md](#item-3f0d72) | minor update | キーレス接続に関するドキュメントの更新 | modified | 1 | 1 | 2 | 
| [search-data-sources-gallery.md](#item-18727f) | minor update | SAP HANAコネクタに関するリンクの更新 | modified | 1 | 1 | 2 | 
| [search-security-manage-encryption-keys.md](#item-db3487) | minor update | 暗号化キー管理に関するドキュメントの更新 | modified | 87 | 13 | 100 | 


# Modified Contents
## articles/search/keyless-connections.md{#item-3f0d72}

<details>
<summary>Diff</summary>
````diff
@@ -196,7 +196,7 @@ credential = DefaultAzureCredential(authority=authority)
 
 search_client = SearchClient(
     endpoint=service_endpoint, 
-    index=index_name, 
+    index_name=index_name, 
     credential=credential, 
     audience=audience)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "キーレス接続に関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、`articles/search/keyless-connections.md`ファイル内の内容に対する小規模な更新を示しています。具体的には、`SearchClient`を呼び出す際の引数の順序が変更され、`index`から`index_name`に引数の名前が明示的に修正されています。この変更は、コードの可読性を向上させることを目的としており、ユーザーがどの引数が何を指しているのかをより明確に理解できるようになります。全体として、この変更は動作には影響を与えず、ドキュメント内の整合性を改善するためのものです。

## articles/search/search-data-sources-gallery.md{#item-18727f}

<details>
<summary>Diff</summary>
````diff
@@ -2327,7 +2327,7 @@ By [BA Insight](https://www.bainsight.com/)
 
 The SAP HANA Connector honors the security of the source database and provides both full and incremental crawls, so users always have the latest information available to them. It indexes content from SAP HANA into Azure AI Search, surfacing it through BA Insight's SmartHub to provide users with integrated search results.
 
-[More details](https://www.bainsight.com/connectors/sap-hana-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.bainsight.com/connectors/connector-sap-hana-cloud-version/)
 
 :::column-end:::
 :::column span="":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SAP HANAコネクタに関するリンクの更新"
}
```

### Explanation
このコードの変更は、`articles/search/search-data-sources-gallery.md`ファイル内で行われた小規模な修正を反映しています。具体的には、SAP HANAコネクタに関するリンクが更新され、新しいリンクを参照するようになりました。この更新により、ユーザーは最新の情報にアクセスすることができ、コネクタの機能や特長についての詳細を確認しやすくなります。全体として、この変更は情報の正確性を保つためのものであり、ユーザー体験を向上させることに寄与します。

## articles/search/search-security-manage-encryption-keys.md{#item-db3487}

<details>
<summary>Diff</summary>
````diff
@@ -320,17 +320,19 @@ Azure policies help to enforce organizational standards and to assess compliance
 
 | Effect | Effect if enabled|
 |--------|------------------|
-| [**AuditIfNotExists**](/azure/governance/policy/concepts/effect-audit-if-not-exists) | Checks for compliance: do objects have a customer-managed key defined, and is the content encrypted. This effect applies to existing services with content. It's evaluated each time an object is created or updated, or [per the evaluation schedule](/azure/governance/policy/overview#understand-evaluation-outcomes). [Learn more...](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F356da939-f20a-4bb9-86f8-5db445b0e354) |
+| [**AuditIfNotExists**](/azure/governance/policy/concepts/effect-audit-if-not-exists) | Checks for policy compliance: do objects have a customer-managed key defined, and is the content encrypted. This effect applies to existing services with content. It's evaluated each time an object is created or updated, or [per the evaluation schedule](/azure/governance/policy/overview#understand-evaluation-outcomes). [Learn more...](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F356da939-f20a-4bb9-86f8-5db445b0e354) |
 | [**Deny**](/azure/governance/policy/concepts/effect-deny) | Checks for policy enforcement: does the search service have [SearchEncryptionWithCmk](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2023-11-01&tabs=HTTP#searchencryptionwithcmk&preserve-view=true) set to `Enabled`. This effect applies to new services only, which must be created with encryption enabled. Existing services remain operational but you can't update them unless you patch the service. None of the tools used for provisioning services expose this property, so be aware that setting the policy limits you to [programmatic set up](#enable-cmk-policy-enforcement).|
 
 ### Assign a policy
 
-1. Navigate to a built-in policy and then select **Assign**.
+1. In the Azure portal, navigate to a built-in policy and then select **Assign**.
 
    + [AuditIfExists](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F76a56461-9dc0-40f0-82f5-2453283afa2f)
 
    + [Deny](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F356da939-f20a-4bb9-86f8-5db445b0e354)
 
+   Here's an example of the **AuditIfExists** policy in the Azure portal:
+
    :::image type="content" source="media/search-security-manage-encryption-keys/assign-policy.png" alt-text="Screenshot of assigning built-in CMK policy." border="true":::
 
 1. Set [policy scope](/azure/governance/policy/concepts/scope) by selecting the subscription and resource group. Exclude any search services for which the policy shouldn't apply.
@@ -339,22 +341,94 @@ Azure policies help to enforce organizational standards and to assess compliance
 
 ### Enable CMK policy enforcement
 
-+ For new search services, create them with [SearchEncryptionWithCmk](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2023-11-01&tabs=HTTP#searchencryptionwithcmk&preserve-view=true) set to `Enabled`. Neither the Azure portal nor the command line tools (the Azure CLI and Azure PowerShell) provide this property, but you can use [Management REST API](/rest/api/searchmanagement/services/create-or-update) to provision a search service with a CMK policy definition.
+A policy that's assigned to a resource group in your subscription is effective immediately. Audit policies flag non-compliant resources, but Deny policies prevent the creation and update of non-compliant search services. This section explains how to create a compliant search service or update a service to make it compliant. To bring objects into compliance, start at [step one](#step-1-create-an-encryption-key) of this article.
 
-+ For existing search services, patch them using [Services - Update API](/rest/api/searchmanagement/services/update).
+#### Create a compliant search service
 
-   ```http
-   PATCH https://management.azure.com/subscriptions/<your-subscription-Id>/resourceGroups/<your-resource-group-name>/providers/Microsoft.Search/searchServices/<your-search-service-name>?api-version=2023-11-01
-  
-   {
-      "properties": {
-          "encryptionWithCmk": {
-              "enforcement": "Enabled"
-          }
+For new search services, create them with [SearchEncryptionWithCmk](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2023-11-01&tabs=HTTP#searchencryptionwithcmk&preserve-view=true) set to `Enabled`. 
+
+Neither the Azure portal nor the command line tools (the Azure CLI and Azure PowerShell) provide this property natively, but you can use [Management REST API](/rest/api/searchmanagement/services/create-or-update) to provision a search service with a CMK policy definition. You can also use the Azure CLI `az resource create` or `update` command to set properties as name-value pairs.
+
+### [**Management REST API**](#tab/mgmt-rest-create)
+
+This example is from [Manage your Azure AI Search service with REST APIs](search-manage-rest.md), modified to include the [SearchEncryptionWithCmk](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2023-11-01&tabs=HTTP#searchencryptionwithcmk&preserve-view=true) property.
+
+```rest
+### Create a search service (provide an existing resource group)
+@resource-group = my-rg
+@search-service-name = my-search
+PUT https://management.azure.com/subscriptions/{{subscriptionId}}/resourceGroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2023-11-01 HTTP/1.1
+     Content-type: application/json
+     Authorization: Bearer {{token}}
+
+    {
+        "location": "North Central US",
+        "sku": {
+            "name": "basic"
+        },
+        "properties": {
+            "replicaCount": 1,
+            "partitionCount": 1,
+            "hostingMode": "default",
+            "encryptionWithCmk": {
+                "enforcement": "Enabled"
+        }
       }
-   }
+    }
+```
+
+### [**Azure CLI**](#tab/azure-cli-create)
+
+1. Create your search service using the examples in [Manage your Azure AI Search service with the Azure CLI](search-manage-azure-cli.md).
+
+1. Patch your service using the update command, substituting valid values for an existing search service and resource group.
+
+   ```azurecli
+   az resource update --name SEARCH-SERVICE-PLACEHOLDER --resource-group RESOURCE-GROUP-PLACEHOLDER --resource-type searchServices --namespace Microsoft.Search --set properties.encryptionWithCmk.enforcement=Enabled
    ```
 
+---
+
+#### Update an existing search service
+
+For existing search services that are now non-compliant, patch them using [Services - Update API](/rest/api/searchmanagement/services/update). Patching the services restores the ability to update search service properties.
+
+### [**Management REST API**](#tab/mgmt-rest-update)
+
+```http
+PATCH https://management.azure.com/subscriptions/<your-subscription-Id>/resourceGroups/<your-resource-group-name>/providers/Microsoft.Search/searchServices/<your-search-service-name>?api-version=2023-11-01
+
+{
+  "properties": {
+      "encryptionWithCmk": {
+          "enforcement": "Enabled"
+      }
+  }
+}
+```
+
+### [**Azure CLI**](#tab/azure-cli-update)
+
+Run the following command, substituting valid values for the search service and resource group.
+
+```azurecli
+az resource update --name SEARCH-SERVICE-PLACEHOLDER --resource-group RESOURCE-GROUP-PLACEHOLDER --resource-type searchServices --namespace Microsoft.Search --set properties.encryptionWithCmk.enforcement=Enabled
+```
+
+The response should include the following statement:
+
+```bash
+"encryptionWithCmk": {
+      "encryptionComplianceStatus": "NonCompliant",
+      "enforcement": "Enabled"
+    }
+...
+```
+
+"Non-compliant" means the search service has existing objects that aren't CMK encrypted. To achieve compliance, recreate each object, specifying an encryption key.
+
+---
+
 ## Rotate or update encryption keys
 
 Use the following instructions to rotate keys or to migrate from Azure Key Vault to the Hardware Security Model (HSM). 
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
このコードの変更は、`articles/search/search-security-manage-encryption-keys.md`ファイルの内容に対する大規模な修正を含んでいます。主に、Azureポリシーの適用や、顧客管理キー（CMK）を使用した暗号化の設定に関する詳細なガイダンスが追加されました。また、ポリシーの適用方法や、サービスの作成・更新に関する具体的な手順が強化され、管理REST APIやAzure CLIを利用した具体的なコマンド例も新たに含まれています。

この更新により、ユーザーはいかにして新しい検索サービスでCMKポリシーを有効にし、既存のサービスをコンプライアンス状態に戻すかのプロセスをより明確に理解できるようになります。全体として、ドキュメントの内容が充実し、具体的な使用例を通じて実行可能な手順が提供されています。


