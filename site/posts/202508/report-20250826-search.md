---
date: '2025-08-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:37d9399...MicrosoftDocs:2ab3d6c
summary: この更新では新機能は導入されず、重大な変更もありませんでしたが、いくつかの改善が行われました。コードスニペットの参照先が更新され、ユーザーが必要なサンプルコードにアクセスしやすくなりました。また、ビジネス継続性と災害復旧（BCDR）要件に関するガイダンスが改善され、サービスの高可用性と災害復旧能力の向上が図られました。さらに、ユーザーが独自のマルチリージョン戦略を実装する必要が強調され、関連資料も追加されました。これにより、Azure
  Searchユーザーはより信頼性の高いサービスを利用できるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:37d9399...MicrosoftDocs:2ab3d6c){target="_blank"}

<format>
# Highlights

## New features
- No new features were introduced in this update.

## Breaking changes
- No breaking changes were identified.

## Other updates
- 更新されたコードスニペットの参照先により、必要なサンプルコードにユーザーがアクセスしやすくなる。
- ビジネス継続性と災害復旧（BCDR）要件に関する説明が更新され、堅牢なシステム設計のためのガイダンスが改善された。

# Insights

この変更は、ユーザーに対してより正確で最新の情報を提供することを目的としています。まず、コードスニペットのパスが微調整されました。新しいパスで示されたコードスニペットが、より適切な文脈や使用法を持っている可能性があります。したがって、参照が最新になり、ユーザビリティが向上しました。この種の更新は、開発者が最新のベストプラクティスとコードを追従できるようにするために重要です。

また、BCDR要件に関する情報も更新されました。従来は地域ペアリングに依存していたアプローチが、異なるAzureリージョンでのマルチインスタンス、かつレプリカの分散を推奨する内容に変更されています。この変更は、サービスの高可用性と災害復旧能力を進化させ、フルリージョン障害にも耐えうるシステムを構築するための重要なステップです。

加えて、ユーザーが独自のマルチリージョン戦略を実装する必要があることも明記され、Azureの提供するサービスだけを頼るのではなく、ユーザー自身の計画も必要であることを強調しています。このサポート資料として「マルチリージョン展開」に関するリンクが追加されている点も見逃せません。

これらの更新により、Azure Searchユーザーは信頼性が高く、安定したサービスを提供し続けるためのより強固な基盤を得ることができます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | コードスニペットの参照先を更新 | modified | 1 | 1 | 2 | 
| [search-create-service-portal.md](#item-f90159) | minor update | BCDR要件に関する説明の更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -180,7 +180,7 @@ Content-Type: application/json
 
 ### [**.NET SDK**](#tab/cogkey-csharp)
 
-The following code snippet is from [azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/tutorial-ai-enrichment/v11/Program.cs), trimmed for brevity.
+The following code snippet is from [azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/tutorial-ai-enrichment/tutorial-ai-enrichment/Program.cs), trimmed for brevity.
 
 ```csharp
 IConfigurationBuilder builder = new ConfigurationBuilder().AddJsonFile("appsettings.json");
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コードスニペットの参照先を更新"
}
```

### Explanation
この変更では、ドキュメント内のコードスニペットの参照元を更新しました。具体的には、コードスニペットが以前のパスから新しいパスに変更されました。変更前のパスは`azure-search-dotnet-samples/blob/main/tutorial-ai-enrichment/v11/Program.cs`でしたが、変更後のパスは`azure-search-dotnet-samples/blob/main/tutorial-ai-enrichment/tutorial-ai-enrichment/Program.cs`です。この更新により、より正確で最新の情報に基づいた参照が提供され、ユーザーが必要なサンプルコードにアクセスしやすくなります。

## articles/search/search-create-service-portal.md{#item-f90159}

<details>
<summary>Diff</summary>
````diff
@@ -115,7 +115,7 @@ In most cases, choose a region near you, unless any of the following apply:
 
 1. Do you have a specific tier in mind? Check [region availability by tier](search-sku-tier.md#region-availability-by-tier).
 
-1. Do you have business continuity and disaster recovery (BCDR) requirements? Create two or more search services in [regional pairs](/azure/reliability/cross-region-replication-azure#azure-paired-regions), each with two or more replicas for [availability zones](/azure/reliability/reliability-ai-search#availability-zone-support). For example, if you're operating in North America, you might choose East US and West US, or North Central US and South Central US, for each search service.
+1. Do you have business continuity and disaster recovery (BCDR) requirements? Create two or more search services in different Azure regions, each with two or more replicas so that they can be spread across multiple [availability zones](/azure/reliability/reliability-ai-search#availability-zone-support). For example, if you're operating in North America, you might choose East US and West US, or North Central US and South Central US, for each search service. For more information, see [Multi-region deployments in Azure AI Search](search-multi-region.md).
 
 1. Do you need [AI enrichment](cognitive-search-concept-intro.md), [integrated data chunking and vectorization](vector-search-integrated-vectorization.md), or [multimodal search](multimodal-search-overview.md)? For [billing purposes](cognitive-search-attach-cognitive-services.md), Azure AI Search and Azure AI services multi-service must coexist in the same region.
 
@@ -190,7 +190,7 @@ Most customers use a single search service at a tier [sufficient for the expecte
 
 However, you might need a second service for the following operational requirements:
 
-+ [Business continuity and disaster recovery (BCDR)](/azure/reliability/cross-region-replication-azure). If there's an outage, Azure AI Search won't provide instant failover.
++ Region outages. In the unlikely event of a full region outage, Azure AI Search doesn't provide instant failover. You must implement your own multi-region solution and failover approach. For more information, see [Multi-region deployments in Azure AI Search](search-multi-region.md).
 + [Multitenant architectures](search-modeling-multitenant-saas-applications.md) that require two or more services.
 + Globally deployed applications that require services in each geography to minimize latency.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "BCDR要件に関する説明の更新"
}
```

### Explanation
この変更では、ビジネス継続性と災害復旧（BCDR）要件に関するセクションが更新されました。具体的には、検索サービスを作成する際に地域のペアを選択する代わりに、異なるAzureリージョンで2つ以上の検索サービスを作成し、それぞれに2つ以上のレプリカを持たせることが推奨されています。この変更は、可用性ゾーンに分散させることを含んでおり、より堅牢なシステム設計を促進します。また、フルリージョン障害が発生した場合の対策として、ユーザーが独自のマルチリージョンソリューションおよびフェイルオーバーアプローチを実装する必要があることが明記されています。さらに、Azure AI Searchに関する追加情報として「マルチリージョン展開」のリンクも追加されています。


