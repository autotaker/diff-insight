---
date: '2025-04-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b7568a1...MicrosoftDocs:b8a8182
summary: この更新には、Azure AI Searchに関連するドキュメントの軽微な更新と新機能の追加が含まれています。主な更新内容は、日付の更新、用語の変更、画像の追加および削除、そして文書の明確化です。特に新しい画像が追加され、視覚的に情報が補完されました。重大な破壊的変更はありませんが、全体的な精度と可読性を向上させることを目的とした内容の最新化と一貫性の向上が中心になっています。この一連の更新は、ユーザーにとってサービスの利用をより安心で効果的にするためのものです。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b7568a1...MicrosoftDocs:b8a8182){target="_blank"}

<format>
# Highlights
このdiffには、Azure AI Searchに関連するドキュメントのいくつかの部分に対する軽微な更新と新しい機能の追加が含まれています。更新の主な内容は、日付の更新、用語の変更、画像の追加および削除、そしてドキュメントの明確化です。

## New features
- `service-created-upgraded-metadata.png`: 新しい画像が追加され、アップグレードメタデータに関する内容が視覚的に補完されました。

## Breaking changes
- 特に重大な破壊的変更は含まれていません。

## Other updates
- 画像処理に関する記事の更新：日付の更新、画像処理の説明強化。
- サービスポータル関連: 用語の変更と日付の更新。
- Azure AI Searchサービスのアップグレードガイド: 日付の更新と説明の明確化。
- インデックス再構築文書: 日付の更新とわずかな文言修正。

# Insights
この一連の更新は、Azure AI Searchのドキュメントの精度と可読性を高めることを目的としています。具体的には、内容の最新化と一貫性の向上が中心に据えられています。

まず、新しい画像の追加は、ユーザーの理解をサポートするための有益なビジュアルリソースを提供し、どのようにデータが管理されるかを具体的に示すために役立ちます。特に、システムが複雑である場合や、手続きが多段階にわたる場合には、こうしたビジュアルの提供が重要です。

さらに、用語の変更や説明の明確化は、正確な理解を促進するための措置です。特に、`AIサービス統合`から`AIエンリッチメント`への変更は、実際の機能がユーザーにもたらす価値と一致した表現を目指しています。

日付の更新については、全てのドキュメントにわたって適用されており、これによりユーザーは情報が最新であることを確認でき、安心してサービスを利用する手助けとなります。

また、特定の画像の削除は、ドキュメンテーションのクリーンアップに起因しており、内容が焦点を絞って一貫性を持つことを意図しています。

全体として、この更新はAzure AI Searchの利便性とユーザーエクスペリエンスを向上させるための重要なステップであると言えます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-concept-image-scenarios.md](#item-606953) | minor update | 画像処理に関する記事の更新 | modified | 4 | 2 | 6 | 
| [service-created-upgraded-metadata.png](#item-72b496) | new feature | 新しい画像の追加 | added | 0 | 0 | 0 | 
| [service-creation-upgrade-metadata.png](#item-d1251d) | minor update | 画像の削除 | removed | 0 | 0 | 0 | 
| [search-create-service-portal.md](#item-f90159) | minor update | サービスポータルに関する文書の修正 | modified | 3 | 3 | 6 | 
| [search-how-to-upgrade.md](#item-990225) | minor update | Azure AI Searchサービスのアップグレードガイドの修正 | modified | 11 | 14 | 25 | 
| [search-howto-reindex.md](#item-46738a) | minor update | インデックスの再構築に関する文書の修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/cognitive-search-concept-image-scenarios.md{#item-606953}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 04/14/2025
+ms.date: 04/28/2025
 ms.custom:
   - devx-track-csharp
   - ignite-2023
@@ -58,7 +58,9 @@ Azure Blob Storage is the most frequently used storage for image processing in A
 After the source files are set up, enable image normalization by setting the `imageAction` parameter in indexer configuration. Image normalization helps make images more uniform for downstream processing. Image normalization includes the following operations:
 
 + Large images are resized to a maximum height and width to make them uniform.
-+ For images that have metadata that specifies orientation, image rotation is adjusted for vertical loading.  
++ For images that have metadata that specifies orientation, image rotation is adjusted for vertical loading.
+
+Note that enabling `imageAction` (setting this parameter to other than `none`) will incur an additional charge for image extraction according to [Azure AI Search pricing](https://azure.microsoft.com/pricing/details/search/).
 
 Metadata adjustments are captured in a complex type created for each image. You can't opt out of the image normalization requirement. Skills that iterate over images, such as OCR and image analysis, expect normalized images.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像処理に関する記事の更新"
}
```

### Explanation
この変更は、Azure AI Search に関するドキュメント内の画像処理の概念を扱った記事に対する少 minor update です。主な修正点は日付の更新と画像正規化プロセスに関する説明の強化です。具体的には、元の更新日（04/14/2025）が新しい日付（04/28/2025）に置き換えられました。また、画像処理における画像正規化機能についての追加情報が含まれており、画像の最大サイズの調整や、メタデータによる回転調整の重要性について詳しく説明されています。最後に、`imageAction`パラメータの設定が追加料金を伴うことも明記されるようになりました。これにより、ユーザーは画像処理の効果やコストについてより明確に理解できるようになります。

## articles/search/media/search-how-to-upgrade/service-created-upgraded-metadata.png{#item-72b496}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加"
}
```

### Explanation
この変更は、Azure AI Search に関するドキュメントに新しい画像ファイルが追加されたことを示しています。具体的には、`service-created-upgraded-metadata.png` という名前の画像が、サービスによって作成されたアップグレードメタデータに関連するコンテンツを視覚的に補完する目的で追加されました。この追加により、ユーザーがアップグレードプロセスの理解を深めるためのビジュアルリソースが提供され、文書の内容がより豊かになることが期待されます。画像は、検索方法や構成手順の説明に役立つことでしょう。

## articles/search/media/search-how-to-upgrade/service-creation-upgrade-metadata.png{#item-d1251d}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像の削除"
}
```

### Explanation
この変更は、Azure AI Search に関する記事から特定の画像ファイルが削除されたことを示しています。具体的には、`service-creation-upgrade-metadata.png` という名前の画像が削除されました。この削除は、コンテンツの品質向上や、関連性の低いビジュアルリソースの整理を目的としている可能性があります。画像が除去されることで、ユーザーに提供される情報がより一貫性を持ち、必要な内容に焦点が当てられることが期待されます。この変更により、文書全体の明瞭さが向上することが見込まれます。

## articles/search/search-create-service-portal.md{#item-f90159}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Create a search service in the Azure portal'
+title: 'Create a Search Service in the Azure Portal'
 titleSuffix: Azure AI Search
 description: Learn how to set up an Azure AI Search resource in the Azure portal. Choose resource groups, regions, and a pricing tier.
 
@@ -11,7 +11,7 @@ ms.custom:
   - references_regions
   - build-2024
 ms.topic: how-to
-ms.date: 03/21/2025
+ms.date: 04/28/2025
 ---
 
 # Create an Azure AI Search service in the Azure portal
@@ -120,7 +120,7 @@ In most cases, choose a region near you, unless any of the following apply:
 
    + Start with [Azure OpenAI regions](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability) because they have the most variability. Azure OpenAI provides embedding models and chat models for RAG and integrated vectorization.
 
-   + Check [Azure AI Search regions](search-region-support.md#azure-public-regions) for a match to your Azure OpenAI region. If you're using OCR, entity recognition, or other skills backed by Azure AI, the **AI service integration** column indicates whether Azure AI services multi-service and Azure AI Search are in the same region.
+   + Check [Azure AI Search regions](search-region-support.md#azure-public-regions) for a match to your Azure OpenAI region. If you're using OCR, entity recognition, or other skills backed by Azure AI, the **AI enrichment** column indicates whether Azure AI services multi-service and Azure AI Search are in the same region.
 
    + Check [multimodal embedding regions](/azure/ai-services/computer-vision/overview-image-analysis#region-availability) for multimodal APIs and image search. This API is accessed through an Azure AI services multi-service account, but in general, it's available in fewer regions than Azure AI services multi-service.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービスポータルに関する文書の修正"
}
```

### Explanation
この変更は、Azure AI Search に関連する「サービスポータルでの検索サービスの作成」という文書が修正されたことを示しています。具体的には、以下の点が変更されました：

1. タイトルが「Create a search service in the Azure portal」から「Create a Search Service in the Azure Portal」に変更され、大文字が適用されました。
2. 日付が「03/21/2025」から「04/28/2025」に更新され、最新の情報が反映されています。
3. 特定のセクション内において、「AIサービス統合」から「AIエンリッチメント」への用語変更が行われ、内容の正確性を向上させています。

これらの修正は、文書の表現の一貫性を高め、ユーザーが適切な情報を取得できるようにすることを目的としています。全体として、内容が明確化され、最新情報が反映されたことで、読者にとって有用なリソースとなるでしょう。

## articles/search/search-how-to-upgrade.md{#item-990225}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.custom: references_regions
-ms.date: 04/10/2025
+ms.date: 04/29/2025
 ---
 
 # Upgrade your Azure AI Search service in the Azure portal
@@ -26,7 +26,7 @@ This article describes how to upgrade your service in the [Azure portal](https:/
 
 ## About service upgrades
 
-In April 2024, Azure AI Search increased the [storage capacity](search-limits-quotas-capacity.md#service-limits) of newly created search services. Services created before April 2024 saw no capacity changes, so if you wanted larger and faster partitions, you had to create a new service. However, some older services can now be upgraded to benefit from the higher capacity partitions.
+In April 2024, Azure AI Search increased the [storage capacity](search-limits-quotas-capacity.md#service-limits) of newly created search services. Services created before April 2024 saw no capacity changes, so if you wanted larger and faster partitions, you had to create a new service. However, some older services can now be upgraded to benefit from the higher-capacity partitions.
 
 In this preview, an upgrade only increases the [storage limit](#higher-storage-limits) and [vector index size](#higher-vector-limits) of [eligible services](#upgrade-eligibility).
 
@@ -35,15 +35,12 @@ In this preview, an upgrade only increases the [storage limit](#higher-storage-l
 To qualify for an upgrade, your service:
 
 > [!div class="checklist"]
-> + Must have been created before April 2024. Services created after April 2024 should already have higher capacity. To see when you created your service, [check your service creation date](#check-your-service-creation-or-upgrade-date).
-> + Must be in a region where higher capacity is enabled.
-> + Must be in one of the following regions:
->   + East US
->   + North Central US
->   + West Central US
->   + UK South
+> + Must have been [created before April 3, 2024](#check-your-service-creation-or-upgrade-date). Services created after this date should already have higher capacity.
+> + Must be in a [region where higher capacity is enabled](search-region-support.md). Most regions provide higher-capacity partitions. Exceptions are noted in the footnotes of each table.
 
-<!-- Check the footnotes in the [list of supported regions](search-region-support.md). -->
+> [!IMPORTANT]
+> + Some search services created before January 1, 2019 don't support upgrades. In this situation, you must create a new service in a high-capacity region to get increased storage and vector limits.
+> + Upgrades are subject to [capacity constraints](search-region-support.md). If regional capacity is constrained for your pricing tier, your service can't be upgraded.
 
 ### Higher storage limits
 
@@ -71,11 +68,11 @@ For [eligible services](#upgrade-eligibility), the following table compares the
 
 ## Check your service creation or upgrade date
 
-On the **Overview** page, you can view various metadata about your search service, including the **Create date (UTC)** and **Upgrade date (UTC)**.
+On the **Overview** page, you can view various metadata about your search service, including **Date created** and **Date upgraded**.
 
-:::image type="content" source="media/search-how-to-upgrade/service-creation-upgrade-metadata.png" alt-text="Screenshot of the service creation and service upgrade dates in the Azure portal." border="true" lightbox="media/search-how-to-upgrade/service-creation-upgrade-metadata.png":::
+:::image type="content" source="media/search-how-to-upgrade/service-created-upgraded-metadata.png" alt-text="Screenshot of the service creation and service upgrade dates in the Azure portal." border="true" lightbox="media/search-how-to-upgrade/service-created-upgraded-metadata.png":::
 
-The date you created your service partially determines its [upgrade eligibility](#upgrade-eligibility). If your service has never been upgraded, the **Upgrade date (UTC)** doesn't appear.
+The date you created your service partially determines its [upgrade eligibility](#upgrade-eligibility). If your service has never been upgraded, **Date upgraded** doesn't appear.
 
 ## Upgrade your service
 
@@ -89,7 +86,7 @@ To upgrade your service:
 
    :::image type="content" source="media/search-how-to-upgrade/upgrade-button.png" alt-text="Screenshot of the Upgrade button on the command bar in the Azure portal." border="true" lightbox="media/search-how-to-upgrade/upgrade-button.png":::
 
-   If this button appears dimmed, an upgrade isn’t available for your service. Your service either has the [latest upgrade](#check-your-service-creation-or-upgrade-date) or is in an [unsupported region](#upgrade-eligibility).
+   If this button appears dimmed, an upgrade isn’t available for your service. Your service either [has the latest upgrade](#check-your-service-creation-or-upgrade-date) or [doesn't qualify for an upgrade](#upgrade-eligibility).
 
 1. Review the upgrade details for your service, and then select **Upgrade**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchサービスのアップグレードガイドの修正"
}
```

### Explanation
この変更は、Azure AI Search サービスのアップグレードに関する文書が修正されたことを示しています。具体的には、以下の点が変更されました：

1. 日付が「04/10/2025」から「04/29/2025」に更新され、最新の情報が反映されています。
2. アップグレードの条件についての説明が明確化され、具体的な文言が修正されました。
3. 一部の条件について、サービスの作成日や地域の情報に基づいて、より正確なガイドラインが提供されていることが強調されています。
4. 画像のソース名が更新され、サービスの作成およびアップグレード日を示すスクリーンショットに関する情報も修正されています。

これらの変更により、文書の正確性が向上し、ユーザーにとってより利用しやすいリソースとなっています。また、サービスのアップグレードプロセスに関する重要な情報が強調されているため、利用者は自身のサービスを効果的に管理できるようになります。

## articles/search/search-howto-reindex.md{#item-46738a}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 04/22/2025
+ms.date: 04/28/2025
 ---
 
 # Update or rebuild an index in Azure AI Search
@@ -233,7 +233,7 @@ Some modifications require an index drop and rebuild, replacing a current index
 | Assign an analyzer to a field | [Analyzers](search-analyzers.md) are defined in an index, assigned to fields, and then invoked during indexing to inform how tokens are created. You can add a new analyzer definition to an index at any time, but you can only *assign* an analyzer when the field is created. This is true for both the **analyzer** and **indexAnalyzer** properties. The **searchAnalyzer** property is an exception (you can assign this property to an existing field). |
 | Update or delete an analyzer definition in an index | You can't delete or change an existing analyzer configuration (analyzer, tokenizer, token filter, or char filter) in the index unless you rebuild the entire index. |
 | Add a field to a suggester | If a field already exists and you want to add it to a [Suggesters](index-add-suggesters.md) construct, rebuild the index. |
-| Upgrade your service or tier | If you need more capacity, check if you can [upgrade your service](search-how-to-upgrade.md) or [switch to a higher service tier](search-capacity-planning.md#change-your-pricing-tier). If not, you must create a new service and rebuild your indexes from scratch. To help automate this process, you can use a code sample that backs up your index to a series of JSON files. You can then recreate the index in a search service you specify. |
+| Upgrade your service or tier | If you need more capacity, check if you can [upgrade your service](search-how-to-upgrade.md) or [switch to a higher pricing tier](search-capacity-planning.md#change-your-pricing-tier). If not, you must create a new service and rebuild your indexes from scratch. To help automate this process, you can use a code sample that backs up your index to a series of JSON files. You can then recreate the index in a search service you specify. |
 
 The order of operations is:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスの再構築に関する文書の修正"
}
```

### Explanation
この変更は、Azure AI Search におけるインデックスの更新または再構築に関する文書が修正されたことを示しています。具体的には、以下の点が変更されました：

1. 日付が「04/22/2025」から「04/28/2025」に更新され、最新の情報が反映されています。
2. サービスのアップグレードやティアの変更に関する説明の文言が微修正され、明確化されていますが、元の内容の意味は保たれています。

これらの修正によって、文書の正確さと可読性が向上し、利用者がインデックスに関する手続きや変更を理解しやすくなっています。この更新は、読者にとってより有益なガイドとなることを目的としており、特にサービスのアップグレードやインデックスの管理に関心のあるユーザーに役立つ内容です。


