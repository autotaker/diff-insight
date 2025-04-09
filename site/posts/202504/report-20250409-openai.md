---
date: '2025-04-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6c8ccfa...MicrosoftDocs:24b31df
summary: この記事では、Azure GovernmentとAzure AIサービスに関する文書の更新について説明します。この更新には、文書の日付とポータルの更新、デプロイメントに関するSKU名の変更、クォータと制限のドキュメントの強化が含まれています。新たに「Key
  Portals」に「AI Foundry Portal」を追加し、クォータ制限の詳細やAPI使用例を含む文書も更新されました。重要な破壊的変更はありませんが、SKU名が「ProvisionedStandard」から「ProvisionedManaged」に変更され、新しいクォータテーブルも追加されました。これらの変更は、ユーザーの体験を向上させることを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6c8ccfa...MicrosoftDocs:24b31df){target="_blank"}

# Highlights
この記事では、Azure GovernmentとAzure AIサービスに関連する文書の更新について説明します。特に、Azure Government文書の日付とポータルの更新、デプロイメントに関するSKU名の変更、およびクォータと制限のドキュメント拡充が含まれています。

## New features
- 「Key Portals」セクションへの「AI Foundry Portal」の追加。
- 「quotas-limits.md」におけるクォータ制限の詳細とAPI使用例の追加。

## Breaking changes
特に破壊的な変更はありません。

## Other updates
- 文書の日付更新により、最新情報を提供。
- SKU名「ProvisionedStandard」から「ProvisionedManaged」への名称変更。
- クォータ割り当てに関する新しいテーブルの追加。

# Insights
Azure Governmentの文書における小規模な更新は、最新情報を保持し、ユーザビリティを向上させることを目的としています。特に日付の更新により、情報の新鮮さを維持し、「Key Portals」セクションでの順序変更と「AI Foundry Portal」の追加は、利用者が必要なツールに簡単にアクセスできるようにするための措置です。

デプロイメント関連の文書では、SKU名の変更が重要な修正点です。これにより、利用者が最新のSKU名を使用してAPIリクエストを正しく実行できるようになります。名称変更は管理の一元化や統一性を図るためと考えられます。

クォータと制限に関するドキュメントでは、特にトークンの使用制限やAPI使用例の追加がユーザーの実践的な理解を助け、リソースの管理を効果的に行うことができるようになります。また、新しいテーブルが追加され、ユーザーが自身のサブスクリプションのクォータIDを容易に理解し、より適切なリソースの使用計画を立てることができるようになっています。

これらの修正は全体として、Azureプラットフォームの利用者の体験を向上させるものであり、より効果的かつ正確な情報提供を目指しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-government.md](#item-a47549) | minor update | Azure Government 文書の日付とポータルの更新 | modified | 2 | 2 | 4 | 
| [fine-tuning-deploy.md](#item-286d57) | minor update | デプロイメントのSKU名変更 | modified | 3 | 3 | 6 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータと制限のドキュメントの拡充 | modified | 54 | 5 | 59 | 


# Modified Contents
## articles/ai-services/openai/azure-government.md{#item-a47549}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: challenp
 ms.service: azure-ai-openai
 ms.topic: how-to
 ms.custom: references_regions, azuregovernment
-ms.date: 1/29/2025
+ms.date: 4/7/2025
 recommendations: false
 ---
 
@@ -62,7 +62,7 @@ The following feature differences exist when comparing Azure OpenAI in Azure Gov
 | Data Storage | In Azure Government, there are no Azure OpenAI features currently enabled that store customer data at rest. However, Customer Managed Keys (CMK) can still be enabled in Azure Government to support use of the same policies in Azure Government as in Public cloud. Note also that if Azure OpenAI features that store customer data are enabled in Azure Government in the future, any existing CMK deployment would be applied to that data at that time. Learn more at [Azure OpenAI Data Privacy](/../legal/cognitive-services/openai/data-privacy).|
 | Compliance | View the current status of Azure OpenAI compliance in Azure Government at [Azure Government Services Audit Scope](/azure/azure-government/compliance/azure-services-in-fedramp-auditscope?branch=pr-en-us-76518#azure-government-services-by-audit-scope)|
 | Service Endpoints | openai.azure.us |
-| Key Portals | <ul></li><li>Azure OpenAI Studio - aoai.azure.us</li><li>Azure portal - portal.azure.us</li></ul> |
+| Key Portals | <ul><li>AI Foundry Portal - ai.azure.us</li><li>Azure OpenAI Studio - aoai.azure.us</li><li>Azure portal - portal.azure.us</li></ul> |
 
 <br>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Government 文書の日付とポータルの更新"
}
```

### Explanation
この変更では、「azure-government.md」ファイルにおけるいくつかの小規模な更新が行われました。具体的には、以下のポイントが変更されています。

1. **日付の更新**: 文書内の日付が「2025年1月29日」から「2025年4月7日」に変更されました。これは、最新の情報を反映させるための更新です。

2. **Key Portalsの修正**: 「Key Portals」セクションが更新され、「Azure OpenAI Studio」および「Azure portal」のリンクの順序が変わり、「AI Foundry Portal」が新たに追加されました。この変更により、利用可能なポータルのリストが最新の状態に保たれ、ユーザーが必要なリソースにアクセスしやすくなります。

これらの変更は、文書の正確性とユーザビリティの向上を目指したものであり、Azure Governmentに関する情報の適切な伝達を支援します。

## articles/ai-services/openai/how-to/fine-tuning-deploy.md{#item-286d57}

<details>
<summary>Diff</summary>
````diff
@@ -397,7 +397,7 @@ Provisioned Managed fine-tuned deployments currently support structured outputs
 
 To create a new deployment, make an HTTP PUT call via the [Deployments - Create or Update REST API](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true). The approach is similar to performing [cross region deployment](#cross-region-deployment) with the following exceptions:
 
-- You must provide a `sku` name of `ProvisionedStandard`.
+- You must provide a `sku` name of `ProvisionedManaged`.
 - The capacity must be declared in PTUs.
 - The `api-version` must be `2024-10-01` or newer.
 - The HTTP method should be `PUT`.
@@ -409,7 +409,7 @@ curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceG
   -H "Authorization: Bearer <TOKEN>" \
   -H "Content-Type: application/json" \
   -d '{
-    "sku": {"name": "ProvisionedStandard", "capacity": 25},
+    "sku": {"name": "ProvisionedManaged", "capacity": 25},
     "properties": {
         "model": {
             "format": "OpenAI",
@@ -432,7 +432,7 @@ curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceG
   -H "Authorization: Bearer <TOKEN>" \
   -H "Content-Type: application/json" \
   -d '{
-    "sku": {"name": "ProvisionedStandard", "capacity": 40},
+    "sku": {"name": "ProvisionedManaged", "capacity": 40},
     "properties": {
         "model": {
             "format": "OpenAI",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントのSKU名変更"
}
```

### Explanation
この変更は、「fine-tuning-deploy.md」ファイルにおけるいくつかの小規模な更新を反映しています。主な内容は次の通りです。

1. **SKU名の変更**: ドキュメントのいくつかのセクションで、デプロイメントに必要なSKU名が「ProvisionedStandard」から「ProvisionedManaged」に変更されました。これにより、最新のSKU名を適切に使用していることが確認されます。

2. **API使用に関する明記**: 新しいSKU名に伴い、関連するAPI呼び出しのコード スニペットも更新されています。これにより、ユーザーは正しいSKU名を使用したAPIリクエストができるようになります。

これらの修正は、Azureのデプロイメントに関する情報を最新のものに保ち、ユーザーが正確な手順を理解しやすくするためのものです。変更は主にコードスニペットとドキュメントのテキストに関連しており、具体的な利用方法を正確に示しています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 4/04/2025
+ms.date: 4/08/2025
 ms.author: mbullwin
 ---
 
@@ -199,16 +199,65 @@ The Usage Limit determines the level of usage above which customers might see la
 
 If your Azure subscription is linked to certain [offer types](https://azure.microsoft.com/support/legal/offer-details/) your max quota values are lower than the values indicated in the above tables.
 
-
 |Tier| Quota Limit in tokens per minute (TPM) |
 |---|:---|
 |Azure for Students, Free Trials | 1 K (all models) <br>Exception o-series & GPT 4.5 Preview: 0|
 | MSDN | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br>computer-use-preview: 30 K <br> gpt-4o-realtime-preview: 1 K <br> o-series: 0 <br> GPT 4.5 Preview: 0  |
-| Monthly credit card based subscriptions <sup>1</sup> | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br>computer-use-preview: 30 K <br> o-series: 0 <br> GPT 4.5 Preview: 0   |
+|Pay-as-you-go | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br>computer-use-preview: 30 K <br> o-series: 0 <br> GPT 4.5 Preview: 0   |
+| CSP Dev Test<sup>*</sup> | All models: 0 |
+
+<sup>*</sup>This only applies to a small number of dev/test CSP subscriptions. Use the query below to determine what `quotaId` is associated with your subscription.
+
+To determine the offer type that is associated with your subscription you can check your `quotaId`. If your `quotaId` is not listed in this table your subscription qualifies for default quota.
+
+# [REST](#tab/REST)
+
+[API reference](/rest/api/subscription/subscriptions/get)
 
-<sup>1</sup> This currently applies to [offer type 0003P](https://azure.microsoft.com/support/legal/offer-details/)
+```bash
+az login
+access_token=$(az account get-access-token --query accessToken -o tsv)
+```
+
+```bash
+curl -X GET "https://management.azure.com/subscriptions/{subscriptionId}?api-version=2020-01-01" \
+  -H "Authorization: Bearer $access_token" \
+  -H "Content-Type: application/json"
+```
+
+# [CLI](#tab/CLI)
+
+```azurecli
+az rest --method GET --uri "https://management.azure.com/subscriptions/{sub-id}?api-version=2020-01-01"
+```
+---
 
-In the Azure portal you can view what offer type is associated with your subscription by navigating to your subscription and checking the subscriptions overview pane. Offer type corresponds to the plan field in the subscription overview.
+### Output
+
+```json
+{
+  "authorizationSource": "Legacy",
+  "displayName": "Pay-As-You-Go",
+  "id": "/subscriptions/aaaaaa-bbbbb-cccc-ddddd-eeeeee",
+  "state": "Enabled",
+  "subscriptionId": "aaaaaa-bbbbb-cccc-ddddd-eeeeee",
+  "subscriptionPolicies": {
+    "locationPlacementId": "Public_2014-09-01",
+    "quotaId": "PayAsYouGo_2014-09-01",
+    "spendingLimit": "Off"
+  }
+}
+```
+
+| Quota allocation | Subscription quota ID |
+|:---|:----|
+| Enterprise | `EnterpriseAgreement_2014-09-01` |
+| Pay-as-you-go | `PayAsYouGo_2014-09-01`|
+| MSDN | `MSDN_2014-09-01` |
+| CSP Dev/Test | `CSPDEVTEST_2018-05-01` |
+| Azure for Students | `AzureForStudents_2018-01-01` |
+| Free Trial | `FreeTrial_2014-09-01` |
+| Default | Any quota ID not listed in this table  |
 
 ### General best practices to remain within rate limits
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータと制限のドキュメントの拡充"
}
```

### Explanation
この変更は、「quotas-limits.md」ファイルにおける大規模な更新を反映しています。主な内容は以下の通りです。

1. **日付の更新**: 文書の日付が「2025年4月4日」から「2025年4月8日」に更新され、最新のリリース情報を反映しています。

2. **クォータに関する詳細の追加**: 新たに「Pay-as-you-go」プランや「CSP Dev Test」といったクォータ制限に関する詳細が追加され、各プランにおけるトークンの使用制限が明示されています。

3. **API使用例の追加**: REST APIおよびCLIから情報を取得する際の具体的なコードスニペットが追加され、ユーザーが自身のサブスクリプションに関連するクォータ情報を容易に取得できるようになっています。

4. **クォータ割り当てのテーブルの追加**: 各サブスクリプションのクォータIDに関する新しいテーブルが追加され、ユーザーがそれぞれのプランに関連するクォータIDを理解しやすくしています。

これらの更新は、Azureユーザーが自らのサブスクリプションのクォータの理解を深めるために役立つ情報を提供し、より良いリソース管理と利用を促進することを目的としています。


