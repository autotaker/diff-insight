---
date: '2025-04-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a9279bd...MicrosoftDocs:2873777
summary: 今回のコード変更では、Azure AI Search に関連する複数のドキュメントが更新されました。デバッグセッションやキャパシティプランニング、アップグレード手順、インデクサの機能についての最新情報が追加され、特に
  lightbox 機能により画像を詳細に確認できるようになりました。すべてのドキュメントの最終更新日が更新され、可読性向上のための構成調整も行われています。この修正は、ユーザー体験の向上を目指しており、特に技術者や開発者にとって役立つ情報が含まれています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a9279bd...MicrosoftDocs:2873777){target="_blank"}

# Highlights
今回のコード変更では、Azure AI Search に関連する複数のドキュメントが更新されました。ドキュメントの最終更新日が更新されただけでなく、デバッグセッションやキャパシティプランニング、アップグレード手順、インデクサの機能に関する最新情報が追加されています。特に視覚的支援を強化するために lightbox 機能が追加され、より詳細に画像を確認できるようになりました。

## New features
- デバッグセッションでは、カスタムスキルにおけるユーザー割り当てマネージド ID がサポートされていない点が追加されました。
- インデクサにおけるドキュメントクラッキングの詳細が追加され、画像抽出機能のオプションが説明されています。

## Breaking changes
特に記載はありませんが、一部重要な変更によってユーザーの理解と設定方法に影響を与える可能性があります。

## Other updates
- すべてのドキュメントの最終更新日が更新されました。
- ドキュメントの可読性向上や情報が明確になるような構成の調整が行われています。
- lightbox 機能の追加により、画像の拡大表示ができるようになりました。

# Insights
この更新は、Azure AI Search のドキュメントにおいて非常に重要なもので、特にユーザー体験の向上を目的としています。例えば、デバッグセッションでは、カスタムスキルを持つユーザーに重要な情報が追加され、ユーザー割り当てマネージド ID をどのように扱うべきかが明示されています。これにより、デバッグ中に直面する可能性がある問題に適切な対応が可能です。

また、キャパシティプランニングやアップグレード手順についても、lightbox 機能が追加されたことで、より視覚的に情報を補完しやすくなりました。このような変更は、テキストだけでは伝えきれない情報の補完に非常に有効です。

インデクサ関連では、ドキュメントクラッキングのプロセスが詳しく説明され、画像抽出についての新しいオプションが紹介されました。この更新は、特に多様な形式のデータを扱うユーザーにとって有用であり、検索機能の設定を効果的に行うためのガイダンスを提供します。

全体として、これらの更新は Azure AI Search のドキュメントをよりユーザーフレンドリーにし、技術的な理解や実装手順を明確にする役割を果たしています。特に技術者や開発者にとって、最新の情報に基づいた適切な設定ができるようになることは大きなメリットです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-debug-session.md](#item-edf092) | minor update | コグニティブサーチデバッグセッションの更新 | modified | 3 | 1 | 4 | 
| [search-capacity-planning.md](#item-0dd6c9) | minor update | 検索サービスのキャパシティプランニングの更新 | modified | 8 | 8 | 16 | 
| [search-how-to-upgrade.md](#item-990225) | minor update | Azure AI Search サービスのアップグレード手順の更新 | modified | 5 | 5 | 10 | 
| [search-indexer-overview.md](#item-292796) | minor update | Azure AI Search インデクサの概要の更新 | modified | 7 | 2 | 9 | 


# Modified Contents
## articles/search/cognitive-search-debug-session.md{#item-edf092}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 12/03/2024
+ms.date: 04/10/2025
 ---
 
 # Debug Sessions in Azure AI Search
@@ -53,6 +53,8 @@ Debug Sessions work with all generally available [indexer data sources](search-d
 
 + For custom skills, a user-assigned managed identity isn't supported for a debug session connection to Azure Storage. As stated in the prerequisites, you can use a system managed identity, or specify a full access connection string that includes a key. For more information, see [Connect a search service to other Azure resources using a managed identity](search-howto-managed-identities-data-sources.md).
 
++ Data sources with encryption enabled via [customer managed keys (CMK)](search-security-manage-encryption-keys.md).
+  
 + Currently, the ability to select which document to debug is unavailable. This limitation isn't permanent and will be lifted soon. At this time, Debug Sessions selects the first document in the source data container or folder.
 
 ## How a debug session works
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブサーチデバッグセッションの更新"
}
```

### Explanation
この変更は、Azure AI Search に関する「コグニティブサーチデバッグセッション」のドキュメントを更新したものです。具体的には、最終更新日を「2024年12月3日」から「2025年4月10日」に変更しました。また、新たにデバッグセッションに関する2つの項目を追加しました。一つは、カスタムスキルにおけるユーザー割り当てマネージドIDが Azure ストレージとのデバッグセッションにサポートされていないことに関するもので、システム管理IDを使用するか、フルアクセス接続文字列を指定する必要があることが記載されています。もう一つは、暗号化が有効なデータソースに関する情報で、顧客管理キー（CMK）を介した暗号化のサポートについて言及されています。また、デバッグ対象としてどのドキュメントを選択するかの機能が現在は利用できないことが述べられ、その制限が一時的なものであることも説明されています。この変更により、ユーザーはデバッグセッションの制限や推奨設定についての最新情報を得ることができます。

## articles/search/search-capacity-planning.md{#item-0dd6c9}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: conceptual
-ms.date: 03/31/2025
+ms.date: 04/10/2025
 ---
 
 # Estimate and manage capacity of a search service
@@ -88,23 +88,23 @@ To increase or decrease the capacity of your service, you have two options:
 
    The following screenshot shows a Standard service provisioned with one replica and partition. The formula at the bottom indicates how many search units are being used (1). If the unit price was $100 (not a real price), the monthly cost of running this service would be $100 on average.
 
-   :::image type="content" source="media/search-capacity-planning/initial-values.png" alt-text="Screenshot of the Scale page showing the current replica and partition values." border="true":::
+   :::image type="content" source="media/search-capacity-planning/initial-values.png" alt-text="Screenshot of the Scale page showing the current replica and partition values." border="true" lightbox="media/search-capacity-planning/initial-values.png":::
 
 1. Use the slider to increase or decrease the number of partitions. Select **Save**.
 
    This example adds a second replica and partition. Notice the search unit count; it's now four because the billing formula is replicas multiplied by partitions (2 x 2). Doubling capacity more than doubles the cost of running the service. If the search unit cost was $100, the new monthly bill would now be $400.
 
    For the current per unit costs of each tier, visit the [pricing page](https://azure.microsoft.com/pricing/details/search/).
 
-   :::image type="content" source="media/search-capacity-planning/add-two-each.png" alt-text="Screenshot of the Scale page with added replicas and partitions." border="true":::
+   :::image type="content" source="media/search-capacity-planning/add-two-each.png" alt-text="Screenshot of the Scale page with added replicas and partitions." border="true" lightbox="media/search-capacity-planning/add-two-each.png":::
 
 1. Check your notifications to confirm that the operation started.
 
-   :::image type="content" source="media/search-capacity-planning/portal-notifications.png" alt-text="Screenshot of the notification of the scaling operation in the Azure portal." border="true":::
+   :::image type="content" source="media/search-capacity-planning/portal-notifications.png" alt-text="Screenshot of the notification of the scaling operation in the Azure portal." border="true" lightbox="media/search-capacity-planning/portal-notifications.png":::
 
    This operation can take several hours to complete. You can’t cancel the process after it starts, and there’s no real-time monitoring of replica and partition adjustments. However, the following message displays while changes are underway.
 
-   :::image type="content" source="media/search-capacity-planning/updating-message.png" alt-text="Screenshot of the Updating message in the Azure portal." border="true":::
+   :::image type="content" source="media/search-capacity-planning/updating-message.png" alt-text="Screenshot of the Updating message in the Azure portal." border="true" lightbox="media/search-capacity-planning/updating-message.png":::
 
 ### Change your pricing tier
 
@@ -134,17 +134,17 @@ To change your pricing tier:
 
 1. Under your current tier, select **Change Pricing Tier**.
 
-   :::image type="content" source="media/search-capacity-planning/change-pricing-tier.png" alt-text="Screenshot of the Change Pricing Tier button in the Azure portal." border="true":::
+   :::image type="content" source="media/search-capacity-planning/change-pricing-tier.png" alt-text="Screenshot of the Change Pricing Tier button in the Azure portal." border="true" lightbox="media/search-capacity-planning/change-pricing-tier.png":::
 
 1. On the **Select Pricing Tier** page, choose a higher tier from the list. Currently, you can only move up between Basic, S1, S2, and S3. Other pricing tiers are unavailable and appear dimmed.
 
 1. To switch to the higher tier, select **Select**.
 
-   :::image type="content" source="media/search-capacity-planning/pricing-tier-list.png" alt-text="Screenshot of the Select Pricing Tier page and the list of higher tiers in the Azure portal." border="true":::
+   :::image type="content" source="media/search-capacity-planning/pricing-tier-list.png" alt-text="Screenshot of the Select Pricing Tier page and the list of higher tiers in the Azure portal." border="true" lightbox="media/search-capacity-planning/pricing-tier-list.png":::
 
    This operation can take several hours to complete. You can’t cancel the process after it starts, and there’s no real-time monitoring of tier changes. However, on the **Overview** page, a **Provisioning** status indicates the operation is underway for your service.
 
-   :::image type="content" source="media/search-capacity-planning/provisioning-status.png" alt-text="Screenshot of the service Overview page with a Provisioning status." border="true":::
+   :::image type="content" source="media/search-capacity-planning/provisioning-status.png" alt-text="Screenshot of the service Overview page with a Provisioning status." border="true" lightbox="media/search-capacity-planning/provisioning-status.png":::
 
 ## How scale requests are handled
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスのキャパシティプランニングの更新"
}
```

### Explanation
この変更は、「検索キャパシティプランニング」に関するドキュメントを更新したもので、内容がより明確かつ視覚的にわかりやすくなるように修正されました。主な修正点は、画像のリファレンスに「lightbox」オプションが追加されたことです。これにより、ユーザーは画像をクリックして拡大表示することができ、より詳細に確認できます。また、最終更新日が「2025年3月31日」から「2025年4月10日」に変更されました。

具体的には、以下のスクリプト内で行われた変更が含まれています。

- 各画像のMarkdown記述が更新され、lightbox機能が追加されました。この変更により、複数の画像を含むセクションが強化され、ユーザーは視覚的に情報を得やすくなります。
- 文章全体が整理されており、情報の流れがスムーズです。キャパシティの増減方法についての説明や、価格階層の変更方法についても、わかりやすく記載されています。

この更新により、読者は検索サービスのキャパシティを管理するための手順をより効率的に理解できるようになります。

## articles/search/search-how-to-upgrade.md{#item-990225}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.custom: references_regions
-ms.date: 04/04/2025
+ms.date: 04/10/2025
 ---
 
 # Upgrade your Azure AI Search service in the Azure portal
@@ -73,7 +73,7 @@ For [eligible services](#upgrade-eligibility), the following table compares the
 
 On the **Overview** page, you can view various metadata about your search service, including the **Create date (UTC)** and **Upgrade date (UTC)**.
 
-:::image type="content" source="media/search-how-to-upgrade/service-creation-upgrade-metadata.png" alt-text="Screenshot of the service creation and service upgrade dates in the Azure portal." border="true":::
+:::image type="content" source="media/search-how-to-upgrade/service-creation-upgrade-metadata.png" alt-text="Screenshot of the service creation and service upgrade dates in the Azure portal." border="true" lightbox="media/search-how-to-upgrade/service-creation-upgrade-metadata.png":::
 
 The date you created your service partially determines its [upgrade eligibility](#upgrade-eligibility). If your service has never been upgraded, the **Upgrade date (UTC)** doesn't appear.
 
@@ -87,19 +87,19 @@ To upgrade your service:
 
 1. On the **Overview** page, select **Upgrade** from the command bar.
 
-   :::image type="content" source="media/search-how-to-upgrade/upgrade-button.png" alt-text="Screenshot of the Upgrade button on the command bar in the Azure portal." border="true":::
+   :::image type="content" source="media/search-how-to-upgrade/upgrade-button.png" alt-text="Screenshot of the Upgrade button on the command bar in the Azure portal." border="true" lightbox="media/search-how-to-upgrade/upgrade-button.png":::
 
    If this button appears dimmed, an upgrade isn’t available for your service. Your service either has the [latest upgrade](#check-your-service-creation-or-upgrade-date) or is in an [unsupported region](#upgrade-eligibility).
 
 1. Review the upgrade details for your service, and then select **Upgrade**.
 
-   :::image type="content" source="media/search-how-to-upgrade/upgrade-panel.png" alt-text="Screenshot of your service upgrade details in the Azure portal." border="true":::
+   :::image type="content" source="media/search-how-to-upgrade/upgrade-panel.png" alt-text="Screenshot of your service upgrade details in the Azure portal." border="true" lightbox="media/search-how-to-upgrade/upgrade-panel.png":::
 
    A confirmation appears reminding you that the upgrade can't be undone.
 
 1. To permanently upgrade your service, select **Upgrade**.
 
-   :::image type="content" source="media/search-how-to-upgrade/upgrade-confirmation.png" alt-text="Screenshot of the upgrade confirmation in the Azure portal." border="true":::
+   :::image type="content" source="media/search-how-to-upgrade/upgrade-confirmation.png" alt-text="Screenshot of the upgrade confirmation in the Azure portal." border="true" lightbox="media/search-how-to-upgrade/upgrade-confirmation.png":::
 
 1. Check your notifications to confirm that the operation started.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search サービスのアップグレード手順の更新"
}
```

### Explanation
この変更は、「Azure AI Search サービスのアップグレード方法」に関するドキュメントを更新したもので、ユーザーがアップグレードを行う際の手順および関連情報がより明確に示されています。主な修正点は、最終更新日が「2025年4月4日」から「2025年4月10日」に変更されたことと、画像の表示方法に「lightbox」オプションが追加された点です。この変更により、画像をクリックすることで拡大表示できるようになります。

具体的には、以下の部分が修正されました：

- Azureポータル内でのサービスの作成日とアップグレード日を表示するためのスクリーンショットへのリファレンスが更新され、lightbox機能が追加されました。
- アップグレード手順の各段階での指示がそのまま保持され、各ステップにおける画像の説明が明確に記載されています。

この更新により、読者はAzure AI Search サービスのアップグレード手順をよりスムーズに理解し、実行できるようになります。また、より良いユーザーエクスペリエンスを提供するために、視覚的なサポートが強化されています。

## articles/search/search-indexer-overview.md{#item-292796}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 12/19/2024
+ms.date: 04/09/2025
 ---
 
 # Indexers in Azure AI Search
@@ -81,7 +81,9 @@ For each document it receives, an indexer implements or coordinates multiple ste
 
 ### Stage 1: Document cracking
 
-Document cracking is the process of opening files and extracting content. Text-based content can be extracted from files on a service, rows in a table, or items in container or collection. If you add a skillset and [image skills](cognitive-search-concept-image-scenarios.md), document cracking can also extract images and queue them for image processing.
+Document cracking is the process of opening files and extracting content. Text-based content can be extracted from files on a service, rows in a table, or items in container or collection. 
+
+You can also enable image extraction during document cracking for an [extra fee](https://azure.microsoft.com/pricing/details/search/). This is disabled by default and can be enabled via the `imageAction` property in the [indexer parameters configuration](/rest/api/searchservice/indexers/create-or-update). Review some [image scenarios](cognitive-search-concept-image-scenarios.md) for indexer image handling.
 
 Depending on the data source, the indexer will try different operations to extract potentially indexable content:
 
@@ -91,6 +93,9 @@ Depending on the data source, the indexer will try different operations to extra
 
 + When the document is a record in [Azure Cosmos DB](search-howto-index-cosmosdb.md), the indexer will extract non-binary content from fields and subfields from the Azure Cosmos DB document.
 
+Note that the document cracking process can also be triggered later during the optional [skillset execution](cognitive-search-concept-intro.md) stage, using skillsets, for data transformation. Adding a skillset with [image skills](cognitive-search-concept-image-scenarios.md) allows document cracking to extract images and queue them for processing.
+
+
 ### Stage 2: Field mappings 
 
 An indexer extracts text from a source field and sends it to a destination field in an index or knowledge store. When field names and data types coincide, the path is clear. However, you might want different names or types in the output, in which case you need to tell the indexer how to map the field.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search インデクサの概要の更新"
}
```

### Explanation
この変更は、「Azure AI Search インデクサの概要」に関するドキュメントを更新したもので、インデクサの動作とオプションに関する重要な情報が追加されています。主な修正点として、最終更新日が「2024年12月19日」から「2025年4月9日」に変更されたことや、ドキュメントクラッキングに関する説明が拡充されたことが挙げられます。

具体的には、以下の点が修正されました：

- ドキュメントクラッキングのプロセスに関する説明が広がり、画像抽出を有効にすることが可能である旨が明記されました。この機能はデフォルトでは無効になっており、`imageAction`プロパティを使用してインデクサのパラメータ設定で有効化できることが記されています。
- インデクサがAzure Cosmos DBにおける非バイナリコンテンツの抽出方法についての説明が追加され、データ変換のためにスキルセット実行段階でもドキュメントクラッキングがトリガーされる可能性があることに言及されました。

これらの更新により、読者はAzure AI Searchのインデクサ機能について、より詳細かつ正確な情報を得られるようになり、特に画像処理に関するオプションが強調されています。


