---
date: '2025-05-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8fb6286...MicrosoftDocs:59073f6
summary: この変更は、Azure GovernmentでのOpenAIサービスに関するドキュメントの更新で、重要な日付の変更、データゾーンの説明の明確化、重要機能に関する通知の追加、冗長な内容の削除が含まれています。新機能に関する詳細は少ないものの、Provisioned
  Instanceの提供予定が示されています。破壊的な変更はなく、全体的に情報が整理され、ドキュメントが簡略化されました。これにより、Azure Governmentを利用する米国政府機関の理解が深まり、ユーザーエクスペリエンスが向上することを目指しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8fb6286...MicrosoftDocs:59073f6){target="_blank"}

# ハイライト
この変更は、Azure GovernmentでのOpenAIサービスに関連するドキュメントの更新を目的としています。主なポイントとして、重要な日付の変更、データゾーンの説明の明確化、重要機能に関する通知の追加、および冗長な内容の削除が含まれます。

## 新機能
特定の新機能に関する情報は詳細に記載されていませんが、Provisioned Instanceの提供に関する通知が追加され、これが2025年5月以降に具体化されることが示されています。

## 破壊的変更
この更新には、特に破壊的な変更や互換性の問題は無いようです。日付の変更や説明の改善がメインです。

## その他の更新
85行もの情報が削除されることで、ドキュメントが簡略化され、情報のアクセスがしやすくなりました。

# インサイト
このコードの変更は、Azure Governmentを利用する米国政府機関や関連組織に関連するもので、OpenAIサービスの利用に対する理解を深め、より明確で効率的にすることを目的としています。まず、ドキュメント内の日付が最新情報と合致するように更新されており、これは特定のサービスや機能の提供スケジュールに直結するため、非常に重要です。次に、データゾーンに関する説明が明確化されたことで、ユーザーはAzure Governmentインフラストラクチャの効果的な利用法を理解しやすくなりました。これにより、データが米国政府のデータセンター内でどのように最適にルーティングされるかが具体的になり、信頼性と効率性が向上します。

また、提供予定の新機能に関する注意喚起が含まれていることは、ユーザーが今後の計画を立てる上で役立ちます。最後に、不必要な情報の削除によってドキュメントが洗練され、必要な情報が探しやすくなり、全体としてユーザーエクスペリエンスが向上します。これらの修正は、Azure Governmentの顧客がOpenAIサービスをより効果的に活用できるようにするための重要なステップです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-government.md](#item-a47549) | minor update | Azure Government版のOpenAIサービスに関する更新: 日付とデプロイメントの変更 | modified | 4 | 85 | 89 | 


# Modified Contents
## articles/ai-services/openai/azure-government.md{#item-a47549}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: challenp
 ms.service: azure-ai-openai
 ms.topic: how-to
 ms.custom: references_regions, azuregovernment
-ms.date: 4/7/2025
+ms.date: 5/1/2025
 recommendations: false
 ---
 
@@ -33,9 +33,7 @@ The following sections show model availability by region and deployment type. Mo
 * Data stored at rest remains in the designated Azure region of the resource.
 * Data may be processed for inferencing in either of the two Azure Government regions. 
 
-SKU name in code: DataZoneStandard
-
-Data zone standard deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. Data zone standard provides higher default quotas than our Azure geography-based deployment types.
+Data zone standard deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure Government infrastructure to dynamically route traffic to the data center within the USGov data zone with the best availability for each request.
 
 To request quota increases for these models, submit a request at [https://aka.ms/AOAIGovQuota](https://aka.ms/AOAIGovQuota). Note the following maximum quota limits allowed via that form:
 
@@ -51,8 +49,8 @@ To request quota increases for these models, submit a request at [https://aka.ms
 | usgovarizona  | ✅ | - | - | ✅ | - |
 | usgovvirginia | ✅ | - | - | ✅ | - |
 
-[NOTE]
-> Provisioned Throughput Units (PTUs) are different from standard quota in Azure OpenAI and are not available by default in Azure Government. To learn more about this offering contact your Microsoft Account Team.
+> [!IMPORTANT]
+> Reserved Instance Provisioned Deployments are now available in Azure Government as of May 2025. Refer to [Provisioned Managed Offering in Azure Government](./concepts/gov-provisioned.md) for more details.
 
 <br>
 
@@ -62,8 +60,6 @@ The following feature differences exist when comparing Azure OpenAI in Azure Gov
 
 |Feature|Description|
 |--------|--------|
-| Structured Outputs | Not currently supported. |
-| Reservation Based Purchases | Not currently supported. |
 | Batch Deployments | Not currently supported. |
 | Connect your data | Virtual network and private links are supported. Deployment to a web app or a copilot in Copilot Studio is not supported. |
 | Abuse Monitoring | Not all features of Abuse Monitoring are enabled for Azure OpenAI in Azure Government. You are responsible for implementing reasonable technical and operational measures to detect and mitigate any use of the service in violation of the Product Terms. [Automated Content Classification and Filtering](./concepts/content-filter.md) remains enabled by default for Azure Government. If modified content filters are required, apply at [https://aka.ms/AOAIGovModifyContentFilter](https://aka.ms/AOAIGovModifyContentFilter)|
@@ -72,80 +68,3 @@ The following feature differences exist when comparing Azure OpenAI in Azure Gov
 | Service Endpoints | openai.azure.us |
 | Key Portals | <ul><li>AI Foundry Portal - ai.azure.us</li><li>Azure OpenAI Studio - aoai.azure.us</li><li>Azure portal - portal.azure.us</li></ul> |
 
-<br>
-
-## Provisioned deployments in Azure Government
-
-The following guide walks you through setting up a provisioned deployment with your Azure OpenAI Service resource in Azure Government. 
-
-### Prerequisites
-
-- An Azure Government subscription
-- An Azure OpenAI resource
-- An approved quota for a provisioned deployment and purchased a commitment
-
-### Managing provisioned throughput commitments
-
-For Azure OpenAI in Azure Government, provisioned throughput deployments require prepurchased commitments created and managed from the **Manage Commitments** view in Azure OpenAI Studio. You can navigate to this view by selecting **Manage Commitments** from the Quota pane.
-
-From the Manage Commitments view, you can do several things:
-* Purchase new commitments or edit existing commitments.
-* Monitor all commitments in your subscription.
-* Identify and take action on commitments that might cause unexpected billing.
-
-| Setting | Notes |
-|---------|-------|
-| **Select a resource** | Choose the resource where you create the provisioned deployment. Once you have purchased the commitment, you are unable to use the quota on another resource until the current commitment expires. |
-| **Select a commitment type** | Select Provisioned. (Provisioned is equivalent to Provisioned Managed) |
-| **Current uncommitted provisioned quota** | The number of PTUs currently available for you to commit to this resource. | 
-| **Amount to commit (PTU)** | Choose the number of PTUs you're committing to. **This number can be increased during the commitment term, but can't be decreased**. Enter values in increments of 50 for the commitment type Provisioned. |
-| **Commitment tier for current period** | The commitment period is set to one month. |
-| **Renewal settings** | Autorenew at current PTUs <br> Autorenew at lower PTUs <br> Do not autorenew |
-
-> [!IMPORTANT]
-> A new commitment is billed up-front for the entire term. If the renewal settings are set to auto-renew, then you will be billed again on each renewal date based on the renewal settings.
-
-> [!IMPORTANT]
-> When you add PTUs to a commitment, they will be billed immediately, at a pro-rated amount from the current date to the end of the existing commitment term. Adding PTUs does not reset the commitment term.
-
-### Changing renewal settings
-
-Commitment renewal settings can be changed at any time before the expiration date of your commitment.
-
-> [!IMPORTANT]
-> If you allow a commitment to expire or decrease in size such that the deployments under the resource require more PTUs than you have in your resource commitment, you will receive hourly overage charges for any excess PTUs.  For example, a resource that has deployments that total 500 PTUs and a commitment for 300 PTUs will generate hourly overage charges for 200 PTUs.
-
-### Common commitment management scenarios
-
-**Discontinue use of provisioned throughput**
-
-To end use of provisioned throughput and prevent hourly overage charges after commitment expiration, two steps must be taken:
-
-1. Set the renewal policy on all commitments to *Don't autorenew*.
-2. Delete the provisioned deployments using the quota.
-
-**Move a commitment/deployment to a new resource in the same subscription/region**
-
-It isn't possible in Azure OpenAI Studio to directly *move* a deployment or a commitment to a new resource. Instead, a new deployment needs to be created on the target resource and traffic moved to it. This process requires a new commitment purchase on the new resource. Because commitments are charged up-front for a 30-day period, it's necessary to time this move with the expiration of the original commitment to minimize overlap with the new commitment and “double-billing” during the overlap.
-
-There are two approaches that can be taken to implement this transition.
-
-**Option 1: No-Overlap Switchover**
-
-This option requires some downtime, but requires no extra quota and generates no extra costs.
-
-| Steps | Notes |
-|-------|-------|
-|Set the renewal policy on the existing commitment to expire| This action prevents the commitment from renewing and generating further charges |
-|Before expiration of the existing commitment, delete its deployment | Downtime starts at this point and will last until the new deployment is created and traffic is moved. You can minimize the duration by timing the deletion to happen as close to the expiration date/time as possible.|
-|After expiration of the existing commitment, create the commitment on the new resource|Minimize downtime by executing this step and the next step as soon after expiration as possible.|
-|Create the deployment on the new resource and move traffic to it||
-
-**Option 2: Overlapped Switchover**
-
-This option has no downtime by having both existing and new deployments live at the same time. This method also requires having quota available to create the new deployment and  generates extra costs during the overlapped deployments.
-
-| Steps | Notes |
-|-------|-------|
-|Set the renewal policy on the existing commitment to expire| Doing so prevents the commitment from renewing and generating further charges.|
-|Before expiration of the existing commitment:<br>1. Create the commitment on the new resource.<br>2. Create the new deployment.<br>3. Switch traffic<br>4.	Delete existing deployment| Ensure you leave enough time for all steps before the existing commitment expires, otherwise overage charges will be generated (see next section) for options. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Government版のOpenAIサービスに関する更新: 日付とデプロイメントの変更"
}
```

### Explanation
このコードの変更は、Azure GovernmentにおけるOpenAIサービスに関するドキュメントの更新を示しています。この更新では、主に以下の点が改訂されています：

1. **日付の変更**: ドキュメント内の日付が2025年4月7日から2025年5月1日に変更されました。この変更は、特定の機能やサービスの提供に関連する重要な日付を反映しています。

2. **データゾーンに関する説明の明確化**: 「Data Zone Standard」デプロイメントの説明が改善され、Azure Governmentインフラストラクチャを活用してトラフィックを動的にルーティングする方法が具体的に述べられています。これにより、米国政府データゾーン内のデータセンターに問い合わせを最適化することが強調されました。

3. **重要な情報の強調**: Provisioned Instanceの提供に関する重要な通知が追加され、2025年5月以降にAzure Governmentで利用できるようになる新しい機能についての注意喚起が行われています。

4. **不必要な項目の削除**: 85行もの内容が削除され、文書が簡略化されました。これにより、情報がより明確になり、ユーザーが必要とする情報に容易にアクセスできるようになっています。

この修正は、Azure GovernmentのユーザーがOpenAIサービスを利用する際の理解をより深めるために役立つでしょう。


