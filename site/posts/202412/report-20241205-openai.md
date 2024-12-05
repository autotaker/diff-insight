---
date: '2024-12-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2c6389f...MicrosoftDocs:04e3114
summary: |-
  この報告の要約は以下の通りです。

  最近のドキュメント更新では、新しいビジュアル要素が追加され、視覚的理解を向上させました。特に、ビジネス継続性と災害復旧に関するガイドラインが強化され、高可用性の確保に必要な情報が充実しました。また、プロンプトキャッシングに関するドキュメントが微調整され、用語の正確性が向上しました。新たに追加された図により、災害復旧やスケーリングのプロセスの理解が深まり、ユーザーは効果的な災害復旧計画を立てやすくなっています。全体として、これらの更新は、Azure OpenAIサービスユーザーのビジネス継続性を強化し、信頼性の高いシステム運用をサポートすることを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2c6389f...MicrosoftDocs:04e3114){target="_blank"}

# Highlights

- **重大な更新**として複数の新しいビジュアル要素が追加され、ドキュメントの視覚的理解が向上しました。
- **ビジネス継続性と災害復旧**に関するガイドラインが強化され、Azure OpenAIサービスの高可用性確保についての情報がさらに充実しました。
- **プロンプトキャッシング**のドキュメントが微調整され、用語の正確性が向上しました。

## New features

- **災害復旧アーキテクチャの図**、**災害復旧プロセスの図**、および**スケーリングプロセスの図**が新たに追加され、ドキュメントの理解が促進されました。

## Breaking changes

- 破壊的な変更は特にありませんが、用語の変更（例: `prompt_tokens_details`）は注意が必要です。

## Other updates

- プロンプトキャッシングに関する属性名と説明が修正され、ドキュメントの一貫性と正確性が向上しました。

# Insights

Azure OpenAIサービスにおける「ビジネス継続性と災害復旧」のテーマは、この度のドキュメント更新において特に強調されています。企業がクラウドサービスを利用する際に最も懸念される点の一つが、サービスの中断やデータ損失です。このガイドの更新により、ユーザーは標準およびプロビジョニングされたデプロイメントの詳細を理解し、高可用性を保つための適切なインフラストラクチャ設計を行えるようになります。

また、視覚的な要素が多数追加されたことは特筆すべきです。技術的な概念はしばしば理解しにくいものであり、図を付け加えることにより、文章だけでは表現しにくいビジュアルな情報を提供することは、利用者が具体的な災害復旧計画を策定する際、重要な助けとなるでしょう。この図により、ユーザーは災害時のシステムスケーリングやリカバリー機能の役割をより直感的に把握することが可能になります。

さらに、プロンプトキャッシングのドキュメント調整は、細部へのこだわりが示されています。細かい属性名の変更は、システムエンジニアや開発チームがキャッシュ戦略を正確に理解するためには不可欠な情報です。今回の調整で、キャッシュの効果やシステム応答のパフォーマンスをより効率的に追跡しやすくなりました。

今回の一連の更新は、Azure OpenAIサービスユーザーのビジネス継続性を強化し、より堅牢で信頼性の高いシステム運用をサポートするものとなっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [business-continuity-disaster-recovery.md](#item-0d0259) | minor update | ビジネス継続性と災害復旧に関するガイドの更新 | modified | 54 | 17 | 71 | 
| [disaster-recovery-diagram.jpg](#item-6c769d) | new feature | 災害復旧アーキテクチャの図の追加 | added | 0 | 0 | 0 | 
| [recovery.png](#item-1bcb58) | new feature | 災害復旧プロセスの図の追加 | added | 0 | 0 | 0 | 
| [scaling.jpg](#item-1431c7) | new feature | スケーリングプロセスの図の追加 | added | 0 | 0 | 0 | 
| [prompt-caching.md](#item-1631df) | minor update | プロンプトキャッシングに関するドキュメントの修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/openai/how-to/business-continuity-disaster-recovery.md{#item-0d0259}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ description: Considerations for implementing Business Continuity and Disaster Re
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 9/05/2024
+ms.date: 12/03/2024
 author: mrbullwinkle    
 ms.author: mbullwin
 recommendations: false
@@ -19,32 +19,69 @@ Azure OpenAI is available in multiple regions. When you create an Azure OpenAI r
 
 It's rare, but not impossible, to encounter a network issue that hits an entire region. If your service needs to always be available, then you should design it to either failover into another region or split the workload between two or more regions. Both approaches require at least two Azure OpenAI resources in different regions. This article provides general recommendations for how to implement Business Continuity and Disaster Recovery (BCDR) for your Azure OpenAI applications.
 
-## BCDR requires custom code
+By default, the Azure OpenAI service provides a [default SLA](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1). While the default resiliency may be sufficient for many applications, applications requiring high degrees of resiliency and business continuity should take additional steps to further strengthen their model infrastructure.
 
-Today customers will call the endpoint provided during deployment for inferencing. Inferencing operations are stateless, so no data is lost if a region becomes unavailable.
+## Standard Deployments
 
-If a region is nonoperational customers must take steps to ensure service continuity.
+> [!NOTE]
+> If you can use Global Standard deployments, you should use these instead. Data Zone deployments are the next best option for organizations requiring data processing to happen entirely within a geographic boundary.
 
-## BCDR for base model & customized model
+1. For Standard Deployments default to Data Zone deployment (US/EU options).
 
-If you're using the base models, you should configure your client code to monitor errors, and if the errors persist, be prepared to redirect to another region of your choice where you have an Azure OpenAI subscription.
+1. You should deploy two Azure OpenAI Service resources in the Azure Subscription. One resource should be deployed in your preferred region and the other should be deployed in your secondary/failover region. The Azure OpenAI service allocates quota at the subscription + region level, so they can live in the same subscription with no impact on quota.
+1. You should have one deployment for each model you plan to use deployed to the Azure OpenAI Service resource in your preferred Azure region and you should duplicate these model deployments in the secondary/failover region. Allocate the full quota available in your Standard deployment to each of these endpoints. This provides the highest throughput rate when compared to splitting quota across multiple deployments.
+1. Select the deployment region based on your network topology. You can deploy an Azure OpenAI Service resource to any supported region and then create a Private Endpoint for that resource in your preferred region.
+    - Once within the Azure OpenAI Service boundary, the Azure OpenAI Service optimizes routing and processing across available compute in the data zone. 
+    - Using data zones is more efficient and simpler than self-managed load balancing across multiple regional deployments.
+1. If there's a regional outage where the deployment is in an unusable state, you can use the other deployment in the secondary/passive region within the same subscription.
+    - Because both the primary and secondary deployments are Zone deployments, they draw from the same Zone capacity pool which draws from all available regions in the Zone. The secondary deployment is protecting against the primary Azure OpenAI endpoint being unreachable.     
+    - Use a Generative AI Gateway that supports load balancing and circuit breaker pattern such as API Management in front of the Azure OpenAI Service endpoints so disruption during a regional outage is minimized to consuming applications.
+    - If the quota within a given subscription is exhausted, a new subscription can be deployed in the same manner as above and its endpoint deployed behind the Generative AI Gateway.
 
-Follow these steps to configure your client to monitor errors:
+## Provisioned Deployments
 
-1. Use the [models](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability) page to choose the datacenters and regions that are right for you.
+### Create an Enterprise PTU Pool
 
-2. Select a primary and one (or more) secondary/backup regions from the list.
+1. For provisioned deployments, we recommend having a single Data Zone PTU deployment (available 12/04/2024) that serves as an enterprise pool of PTU. You can use API Management to manage traffic from multiple applications to set throughput limits, logging, priority, and failover logic.     
+    - Think of this Enterprise PTU Pool as a “Private pay-as-you-go  ” resource that protects against the noisy-neighbors problem that can occur on Standard deployments when service demand is high. Your organization will have guaranteed, dedicated access to a pool of capacity that is only available to you and therefore independent of demand spikes from other customers. 
+    - This gives you control over which applications experience increases in latency first, allowing you to prioritize traffic to your mission critical applications.
+    - Provisioned Deployments are backed by latency SLAs that make them preferable to Standard  (pay-as-you-go) deployments for latency sensitive workloads.
+    - Enterprise PTU Deployment also enables higher utilization rates as traffic is smoothed out across application workloads, whereas individual workloads tend to be more prone to spikes.
+1. Your primary Enterprise PTU  deployment should be in a different region than your primary Standard Zone deployment. This is so that if there's a regional outage, you don't lose access to both your PTU deployment and Standard Zone deployment at the same time.
 
-3. Create Azure OpenAI resources for each region(s) selected.
+### Workload Dedicated PTU Deployment
 
-4. For the primary region and any backup regions your code will need to know:
+1. Certain workloads may need to have their own dedicated provisioned deployment. If so, you can create a dedicated PTU deployment for that application.
+1. The workload and enterprise PTU pool deployments should protect against regional failures. You could do this by placing the workload PTU pool in Region A and the enterprise PTU pool in Region B.    
+1. This deployment should fail over first to the Enterprise PTU Pool and then to the Standard deployment. This implies that when utilization of the workload PTU deployment exceeds 100%, requests would still be serviced by PTU endpoints, enabling a higher latency SLA for that application.
 
-    - Base URI for the resource
-    - Regional access key or Microsoft Entra ID access
+:::image type="content" source="../how-to/media/disaster-recovery/disaster-recovery-diagram.jpg" alt-text="Disaster recovery architectural diagram." lightbox="../how-to/media/disaster-recovery/disaster-recovery-diagram.jpg":::
 
-5. Configure your code so that you monitor connectivity errors (typically connection timeouts and service unavailability errors).
+The additional benefit of this architecture is that it allows you to stack Standard deployments with Provisioned Deployments so that you can dial in your preferred level of performance and resiliency. This allows you to use PTU for your baseline demand across workloads and leverage pay-as-you-go for spikes in traffic.
 
-    - Given that networks yield transient errors, for single connectivity issue occurrences, the suggestion is to retry.
-    - For persistent connectivity issues, redirect traffic to the backup resource in the region(s) you've created.
+:::image type="content" source="../how-to/media/disaster-recovery/scaling.jpg" alt-text="Provisioned scaling diagram." lightbox="../how-to/media/disaster-recovery/scaling.jpg":::
 
-If you have fine-tuned a model in your primary region, you will need to retrain the base model in the secondary region(s) using the same training data. And then follow the above steps.
+
+## Supporting Infrastructure
+
+The infrastructure that supports the Azure OpenAI architecture needs to be considered in designs. The infrastructure components involved in the architecture vary depending on if the applications consume the Azure OpenAI service over the Internet or over a private network. The architecture discussed in this article assumes the organization has implemented a [Generative AI Gateway](/ai/playbook/technology-guidance/generative-ai/dev-starters/genai-gateway/). Organizations with a mature Azure footprint and hybrid connectivity should consume the service through a private network while organizations without hybrid connectivity, or with applications in another cloud such as GCP or AWS, will consume the service through the Microsoft public backbone.
+
+### Designing for consumption through the Microsoft public backbone
+
+Organizations consuming the service through the Microsoft public backbone should consider the following design elements:
+
+1. The Generative AI Gateway should be deployed in manner that ensures it's available in the event of an Azure regional outage. If using APIM (Azure API Management), this can be done by deploying separate APIM instances in multiple regions or using the [multi-region gateway feature of APIM](/azure/api-management/api-management-howto-deploy-multi-region).
+
+1. A public global server load balancer should be used to load balance across the multiple Generative AI Gateway instances in either an active/active or active/passive manner. [Azure FrontDoor](/azure/traffic-manager/traffic-manager-routing-methods) can be used to fulfill this role depending on the organization’s requirements.
+
+:::image type="content" source="../how-to/media/disaster-recovery/recovery.png" alt-text="Failover architectural diagram." lightbox="../how-to/media/disaster-recovery/recovery.png":::
+
+
+### Designing for consumption through the private networking
+
+Organizations consuming the service through a private network should consider the following design elements:
+
+1. Hybrid connectivity should be deployed in a way that it protects against the failure of an Azure region. The underlining components supporting hybrid connectivity consist of the organization’s on-premises network infrastructure and [Microsoft ExpressRoute](/azure/expressroute/designing-for-high-availability-with-expressroute) or [VPN](/azure/vpn-gateway/vpn-gateway-highlyavailable). 
+1. The Generative AI Gateway should be deployed in manner that ensures it's available in the event of an Azure regional outage. If using APIM (Azure API Management), this can be done by deploying separate APIM instances in multiple regions or using the [multi-region gateway feature of APIM](/azure/api-management/api-management-howto-deploy-multi-region).
+1. Azure Private Link Private Endpoints should be deployed for each Azure OpenAI Service instance in each Azure region. For Azure Private DNS, a split-brain DNS approach can be used if all application access to the Azure OpenAI Service is done through the Generative AI Gateway to provide for additional protection against a regional failure. If not, Private DNS records will need to be manually modified in the event of a loss of an Azure region. 
+1. A private global server load balancer should be used to load balance across the multiple Generative AI Gateway instances in either an active/active or active/passive manner. Azure doesn't have a native service for global server load balancer for workloads that require private DNS resolution. For additional background on this topic you can refer to this unofficial guide: https://github.com/adstuart/azure-crossregion-private-lb. In lieu of a global server load balancer, organizations can achieve an active/passive pattern through toggling the DNS record for the Generative AI Gateway.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ビジネス継続性と災害復旧に関するガイドの更新"
}
```

### Explanation
このコードの差分は、「ビジネス継続性と災害復旧」に関するガイドを更新したものであり、Azure OpenAIサービスの利用における継続的な可用性を確保するための推奨事項が強化されています。具体的には、Azure OpenAIの標準デプロイメントとプロビジョニングされたデプロイメントについて追加の情報を提供し、それぞれのシナリオにおける運用上の考慮点を明示しました。

主な変更点として、デプロイメントの推奨構成や、サービスの冗長性を確保するために必要なリソースの配置に関する具体的な指導が追加されました。また、日付が2024年9月5日から2024年12月3日に更新され、最新の情報に基づいたコンテンツとしていました。

この更新により、ユーザーは都合に応じた最適なデプロイメント戦略を策定できるようになり、特に高可用性とビジネス継続性を必要とするアプリケーションに向けた新しいアプローチを備えることができます。さらに、Azure OpenAIサービスの構成におけるインフラストラクチャの重要性も強調されています。

## articles/ai-services/openai/how-to/media/disaster-recovery/disaster-recovery-diagram.jpg{#item-6c769d}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "災害復旧アーキテクチャの図の追加"
}
```

### Explanation
このコードの差分は、「災害復旧アーキテクチャ」を示す図を新たに追加したことを示しています。この画像は、Azure OpenAIサービスに関する文章におけるビジュアルコンテンツとして機能し、ユーザーが災害復旧戦略を理解する手助けをすることを目的としています。

具体的には、追加された画像は、復旧時におけるシステムの構造や流れを視覚的に示しており、文書内のテキストの説明を補完する役割を果たします。この図は、Azureの効果的なバックアップおよびリカバリー手法を実現するための設計要素を理解するために役立ちます。

このような視覚的要素の追加により、ユーザーが関連する情報をより迅速かつ効果的に grasp できるようになり、災害対策やビジネス継続計画の重要性を強調する一助となります。

## articles/ai-services/openai/how-to/media/disaster-recovery/recovery.png{#item-1bcb58}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "災害復旧プロセスの図の追加"
}
```

### Explanation
このコードの差分は、「災害復旧プロセス」を視覚的に示す新しい画像を追加したことを示しています。この画像は、Azure OpenAIサービスに関連する文書において、災害復旧の流れや手順を明確に理解するための補助資料として利用されます。

追加された「recovery.png」ファイルは、災害からの復旧に際し考慮すべき重要な要素やプロセスを視覚的に表現しており、テキストの説明を補完します。このような視覚的情報は、ユーザーが災害復旧の戦略をより具体的に把握しやすくするために重要です。

図を通じて、ユーザーは複雑な復旧手順を理解しやすくなり、効果的な災害対策を講じることが可能となります。これにより、ドキュメント全体の有用性が向上し、災害復旧に対する理解が深まることを目的としています。

## articles/ai-services/openai/how-to/media/disaster-recovery/scaling.jpg{#item-1431c7}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "スケーリングプロセスの図の追加"
}
```

### Explanation
このコードの差分は、災害復旧に関連した「スケーリングプロセス」を示す新しい画像ファイルを追加したことを示しています。この画像は、Azure OpenAIサービスに関する文書の一部として、システムがスケールアップまたはスケールダウンする過程を視覚的に表現しています。

追加された「scaling.jpg」は、災害時におけるリソースの拡張や縮小の手順を視覚的に示すもので、利用者にプロセスの理解を促す役割を果たします。この画像によって、ユーザーは、スケーリングがどのように行われるか、またその際の重要な要素について直感的に理解することが容易になります。

視覚的情報の追加は、テキストだけでは伝えきれない複雑な概念を理解するために非常に有用であり、特に技術的な文脈においては、利用者が具体的なアクションプランを策定する際に役立ちます。これにより、災害復旧の計画全体の質が向上することを目指しています。

## articles/ai-services/openai/how-to/prompt-caching.md{#item-1631df}

<details>
<summary>Diff</summary>
````diff
@@ -39,7 +39,7 @@ For a request to take advantage of prompt caching the request must be both:
 - A minimum of 1,024 tokens in length.
 - The first 1,024 tokens in the prompt must be identical.
 
-When a match is found between the token computations in a prompt and the current content of the prompt cache, it's referred to as a cache hit. Cache hits will show up as [`cached_tokens`](/azure/ai-services/openai/reference-preview#cached_tokens) under [`prompt_token_details`](/azure/ai-services/openai/reference-preview#properties-for-prompt_tokens_details) in the chat completions response.
+When a match is found between the token computations in a prompt and the current content of the prompt cache, it's referred to as a cache hit. Cache hits will show up as [`cached_tokens`](/azure/ai-services/openai/reference-preview#cached_tokens) under [`prompt_tokens_details`](/azure/ai-services/openai/reference-preview#properties-for-prompt_tokens_details) in the chat completions response.
 
 ```json
 {
@@ -85,4 +85,4 @@ To improve the likelihood of cache hits occurring, you should structure your req
 
 ## Can I disable prompt caching?
 
-Prompt caching is enabled by default for all supported models. There is no opt-out support for prompt caching. 
\ No newline at end of file
+Prompt caching is enabled by default for all supported models. There is no opt-out support for prompt caching. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトキャッシングに関するドキュメントの修正"
}
```

### Explanation
このコードの差分は、「プロンプトキャッシング」に関するドキュメントにおいて、いくつかの文言を修正したことを示しています。具体的には、プロンプトキャッシュのヒット数に関する情報やキャッシュのトークンに関連する記述が更新されています。

主な変更点として、プロンプトキャッシュのヒットを示す属性名が「`prompt_token_details`」から「`prompt_tokens_details`」に修正されました。この変更により、ユーザーが正確な情報にアクセスできるようになり、システムの応答におけるキャッシュヒットの表示が明確になります。

また、キャッシュヒットの説明の構造を維持しつつ、全体として情報が整合性を持たせる形で見直されています。これにより、ユーザーがプロンプトキャッシングの効果的な利用方法をより理解しやすくなり、技術的な仕様が一層明確化されます。全体として、この修正はドキュメントの信頼性と可読性を向上させることを目的としています。


