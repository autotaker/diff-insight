---
date: '2024-09-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:89cdcc6...MicrosoftDocs:e3ea9cd
summary: "このコードの主な変更点は、画像表示にライトボックス機能を追加し、APIペイロード制限に関する情報を更新したことです。 \n\n具体的には、`search-sku-tier.md`\
  \ と `vector-search-index-size.md` にライトボックス機能が導入され、ユーザーは画像をクリックして拡大表示できるようになります。また、`tutorial-rag-build-solution-pipeline.md`\
  \ には、APIペイロード制限に関する情報とAIエンリッチメントデータの制限についての情報も追加されています。\n\nこれらの変更は、ユーザーの知識獲得を促進し、ドキュメントの使いやすさと情報の正確性を向上させることを目的としています。"
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:89cdcc6...MicrosoftDocs:e3ea9cd){target="_blank"}

# ハイライト
このコードの差分の主な変更点は以下の通りです。
- 新機能として、画像表示にライトボックス機能を追加。
- APIペイロード制限についての情報を追加。

## 新機能
1. `search-sku-tier.md` および `vector-search-index-size.md` において、画像表示にライトボックス機能が追加されました。これにより、画像をクリックすることで拡大表示できます。
   
## その他の更新
1. `tutorial-rag-build-solution-pipeline.md` では、日付の変更とともに、APIペイロード制限に加え、AIエンリッチメントデータの制限に関する情報も追加されました。

# インサイト
この更新は、主にドキュメントのユーザビリティと情報の正確性を向上させることを目的としています。具体的には、以下のようなポイントに重点を置いています。

## ライトボックス機能の追加
### 目的
ライトボックス機能を導入することで、画像が小さく表示されている場合でも、ユーザーがクリックすることで拡大表示して詳細を確認しやすくすることを目的としています。画像の詳細な部分が確認しやすくなるため、ユーザーの情報把握能力が向上します。

### 効果
ユーザーは画像をクリックするだけで拡大して見ることができるため、情報の視認性が劇的に向上。特に技術的なドキュメントにおいて、図表やスクリーンショットの細かい部分まで確認したい場合に有用です。

## APIペイロード制限情報の追加
### 目的
APIのペイロード制限に関する情報を追加することで、ユーザーがシステムの制約をより詳細に理解できるようにします。これにより、ユーザーはAPI使用時に予期せぬ制限に直面することを避けることができ、スムーズにシステムを利用できます。

### 効果
APIペイロード制限に加え、AIエンリッチメントデータの制限についての情報が追加されることで、ユーザーが全体の制約をより包括的に理解できるようになります。これにより、ユーザーはより正確な情報に基づいて業務やプロジェクトを進行できます。

これらの変更は、すべての技術的ドキュメントをより使いやすく、情報を分かりやすく提供するための重要なステップです。ユーザーエクスペリエンスを向上させるための取り組みとして、非常に価値のある更新と言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-sku-tier.md](#item-7686b8) | minor update | 画像表示のライトボックス機能の追加 | modified | 1 | 1 | 2 | 
| [tutorial-rag-build-solution-pipeline.md](#item-25ce01) | minor update | APIペイロード制限に関する情報の追加 | modified | 2 | 2 | 4 | 
| [vector-search-index-size.md](#item-bb2846) | minor update | 画像表示のライトボックス機能の追加 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ Billing rates are shown in the portal's **Select Pricing Tier** page. You can ch
 
 Tiers include **Free**, **Basic**, **Standard**, and **Storage Optimized**. Standard and Storage Optimized are available with several configurations and capacities. The following screenshot from Azure portal shows the available tiers, minus pricing (which you can find in the portal and on the [pricing page](https://azure.microsoft.com/pricing/details/search/)). 
 
-:::image type="content" source="media/search-sku-tier/tiers.png" alt-text="Pricing tier chart" border="true":::
+:::image type="content" source="media/search-sku-tier/tiers.png" lightbox="media/search-sku-tier/tiers.png" alt-text="Pricing tier chart" border="true":::
 
 **Free** creates a [limited search service](search-limits-quotas-capacity.md#subscription-limits) for smaller projects, like running tutorials and code samples. Internally, system resources are shared among multiple subscribers. You can't scale a free service, run significant workloads, and some premium features aren't available. You can only have one free search service per Azure subscription.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像表示のライトボックス機能の追加"
}
```

### Explanation
この変更は、文書「search-sku-tier.md」において、コンテンツ内の画像表示に関連するマークアップを更新しました。具体的には、画像タグに `lightbox` 属性が追加され、画像がクリックされた際に拡大表示できるようになりました。これにより、ユーザーは画像をより大きなサイズで確認することができ、情報の把握がしやすくなります。この変更は、ビジュアルコンテンツの表示方法を改善し、ユーザーエクスペリエンスを向上させることを目的としています。

## articles/search/tutorial-rag-build-solution-pipeline.md{#item-25ce01}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: tutorial
-ms.date: 09/12/2024
+ms.date: 09/23/2024
 
 ---
 
@@ -99,7 +99,7 @@ print(f"{result.name} created")
 
 In this step, set up the sample data and a connection to Azure Blob Storage. The indexer retrieves PDFs from a container. You create the container and upload files in this step.
 
-The original ebook is large, over 100 pages and 35 MB in size. We broke it up into smaller PDFs, one per page of text, to stay under the REST API payload limit of 16 MB per API call. For simplicity, we omit image vectorization for this exercise.
+The original ebook is large, over 100 pages and 35 MB in size. We broke it up into smaller PDFs, one per page of text, to stay under the [API payload limit](search-limits-quotas-capacity.md#api-request-limits) of 16 MB per API call and also the [AI enrichment data limits](search-limits-quotas-capacity.md#data-limits-ai-enrichment). For simplicity, we omit image vectorization for this exercise.
 
 1. Sign in to the Azure portal and find your Azure Storage account.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIペイロード制限に関する情報の追加"
}
```

### Explanation
この変更は、「tutorial-rag-build-solution-pipeline.md」という文書に対する更新です。具体的には、ドキュメント内の日付が「09/12/2024」とから「09/23/2024」に変更されました。そして、元の電子書籍に関する説明文に、APIペイロードの制限以外にも「AIエンリッチメントデータの制限」についてのリンクが追加されました。この修正は、ユーザーがAPIの使用に関する重要な制限事項をより明確に理解できるようにするためのものです。これにより、ドキュメントの情報がより正確で役立つものとなっています。

## articles/search/vector-search-index-size.md{#item-bb2846}

<details>
<summary>Diff</summary>
````diff
@@ -52,11 +52,11 @@ Newer services created after April 3, 2024 offer five to ten times more vector s
 
 1. Select the deployment. If you have more than one, click through to see if it resolves to your search service.
 
-    :::image type="content" source="media/vector-search-index-size/resource-group-deployments.png" alt-text="Screenshot of a filtered deployments list.":::
+    :::image type="content" source="media/vector-search-index-size/resource-group-deployments.png" lightbox="media/vector-search-index-size/resource-group-deployments.png" alt-text="Screenshot of a filtered deployments list.":::
 
 1. Expand deployment details. You should see *Created* and the creation date.
 
-   :::image type="content" source="media/vector-search-index-size/deployment-details.png" alt-text="Screenshot of the deployment details showing creation date.":::
+   :::image type="content" source="media/vector-search-index-size/deployment-details.png" lightbox="media/vector-search-index-size/deployment-details.png" alt-text="Screenshot of the deployment details showing creation date.":::
 
 1. Now that you know the age of your search service, review the vector quota limits based on service creation: [Vector index size limits](search-limits-quotas-capacity.md#vector-index-size-limits).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像表示のライトボックス機能の追加"
}
```

### Explanation
この変更は、「vector-search-index-size.md」というドキュメント内での画像表示に関する更新です。具体的には、二つの画像に `lightbox` 属性が追加され、ユーザーが画像をクリックすることで拡大表示できるようになりました。これにより、情報の視認性が向上し、ユーザーは画像をより詳細に確認することができます。この修正は、ドキュメントのビジュアルコンテンツの利用体験を改善することを目指しています。


