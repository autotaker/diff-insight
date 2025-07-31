---
date: '2025-07-31'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c2bb090...MicrosoftDocs:18e731f
summary: |-
  この報告書の要約は次の通りです。

  今回の修正では、新しい機能は追加されていないものの、既存の内容がより分かりやすく編集されました。互換性を損なう変更は行われておらず、ガイドの表現が簡潔に修正され、APIのサポート地域情報と新バージョン通知が追加されました。これにより、文書の理解が容易になり、ユーザーはAzure AI Document Intelligenceをより効果的に活用できるようになります。表現の改善によって、必要な情報に迅速にアクセスできるようになり、開発プロセスがスムーズになることが期待されます。また、表現の微調整は特定の言語での理解を助け、エラーのリスクを減少させる効果があります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c2bb090...MicrosoftDocs:18e731f){target="_blank"}

# Highlights

## 新しい機能
特に新しい機能は追加されていませんが、従来の内容が詳細にわかりやすく編集されています。

## 互換性を損ねる変更
本変更では互換性を損ねるような変更はありません。

## その他の更新
- ガイド内の表現や文言が簡潔かつ明瞭になるよう修正
- APIのサポート地域情報と新バージョン通知の追加
- 見出しの改善で情報の一貫性を向上

# Insights

今回の修正は、主にユーザーの文書理解を容易にし、複雑に見える内容を整理して利用しやすくすることを目的としています。このようなドキュメントインテリジェンスのガイドラインやクイックスタートの更新は、利用者が困惑することなくAzure AI Document Intelligenceを最適に活用できるようにする重要な努力の一環です。特にAPIの新バージョン発表と対応地域の明確化は、多国籍での利用を検討している開発者にとって非常に有益な情報です。

ドキュメントの形式や表現が改良されたことにより、利用者は必要な情報に迅速にアクセスでき、実際の開発プロセスがよりスムーズになるでしょう。また、細かながらも表現の修正は、特定言語における微妙なニュアンスを理解しやすくし、エラーが発生しやすいポイントを減らします。このように、少しの言い回しの変更が、ユーザーエクスペリエンス全体に大きく寄与することを考慮することが、文書の品質向上につながります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [build-a-custom-model.md](#item-4f2040) | minor update | カスタムモデルの構築に関するガイドの一部修正 | modified | 2 | 2 | 4 | 
| [overview.md](#item-4e36ba) | minor update | ドキュメントインテリジェンスの概要のテキスト修正 | modified | 1 | 1 | 2 | 
| [id-document.md](#item-bf45fa) | minor update | IDドキュメントモデルに関する概要の更新 | modified | 9 | 2 | 11 | 
| [studio-custom-project.md](#item-f52b95) | minor update | カスタムプロジェクトに関する前提条件の見出し修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/how-to-guides/build-a-custom-model.md{#item-4f2040}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ Once you gather a set of forms or documents for training, you need to upload it
 
 The Document Intelligence Studio provides and orchestrates all the API calls required to complete your dataset and train your model.
 
-1. Start by navigating to the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio). The first time you use the Studio, you need to [initialize your subscription, resource group, and resource](../studio-overview.md). Then, follow the [prerequisites for custom projects](../quickstarts/studio-custom-project.md#additional-prerequisites-for-custom-projects) to configure the Studio to access your training dataset.
+1. Start by navigating to the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio). The first time you use the Studio, you need to [initialize your subscription, resource group, and resource](../studio-overview.md). Then, follow the [prerequisites for custom projects](../quickstarts/studio-custom-project.md#prerequisites-for-custom-projects) to configure the Studio to access your training dataset.
 
 1. In the Studio, select the **Custom extraction model** tile and select the **Create a project** button.
 
@@ -60,7 +60,7 @@ The Document Intelligence Studio provides and orchestrates all the API calls req
     1. On the next step in the workflow, choose or create a Document Intelligence resource before you select continue.
 
     > [!IMPORTANT]
-    > Custom neural models are only available in a few regions. If you plan on training a neural model, please select or create a resource in one of [these supported regions](../train/custom-neural.md#supported-regions).
+    > Custom neural models are only available in a few regions. If you plan on training a neural model, select or create a resource in one of [these supported regions](../train/custom-neural.md#supported-regions).
 
     :::image type="content" source="../media/how-to/studio-custom-configure-resource.png" alt-text="Screenshot of Select the Document Intelligence resource.":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムモデルの構築に関するガイドの一部修正"
}
```

### Explanation
このコードの変更は、ドキュメントインテリジェンススタジオを使用してカスタムモデルを構築する方法に関するガイドのテキストに対する少しの修正を含んでいます。具体的には、既存の手順の表現がわずかに変更され、明確さが向上しています。 

1つ目の変更では、手順のリンク先について「追加の前提条件」という表現が、単に「前提条件」に修正され、読みやすさが改善されています。同様に、重要な注意事項に記載されている文言も簡潔に整理され、トレーニングのために選択または作成するリソースに関する指示が分かりやすくなっています。

これらの変更は、ユーザーが文書をより理解しやすくし、よりスムーズにカスタムモデルの構築を行えるようにすることを目的としています。

## articles/ai-services/document-intelligence/overview.md{#item-4e36ba}

<details>
<summary>Diff</summary>
````diff
@@ -41,7 +41,7 @@ monikerRange: '<=doc-intel-4.0.0'
 
 :::moniker-end
 
-Azure AI Document Intelligence is a cloud-based [Azure AI service](../../ai-services/index.yml) that enables you to build intelligent document processing solutions. Massive amounts of data, spanning a wide variety of data types, are stored in forms and documents. Document Intelligence enables you to effectively manage the velocity at which data is collected and processed and is key to improved operations, informed data-driven decisions, and enlightened innovation.</br></br>For information on region access, *see* Azure AI Services [Product Availability by Region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).</br></br>
+Azure AI Document Intelligence is a cloud-based [Azure AI service](../../ai-services/index.yml) that enables you to build intelligent document processing solutions. Massive amounts of data, spanning a wide variety of data types, are stored in forms and documents. Document Intelligence enables you to effectively manage the velocity at which data is collected and processed and is key to improved operations, informed data-driven decisions, and enlightened innovation. For information on region access, *see* Azure AI Services [Product Availability by Region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).</br></br>
 
 | ✔️ [**Document analysis models**](#document-analysis-models) | ✔️ [**Prebuilt models**](#prebuilt-models) | ✔️ [**Custom models**](#custom-model-overview) |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスの概要のテキスト修正"
}
```

### Explanation
この変更は、Azure AI Document Intelligenceに関する概要ドキュメントのテキストの一部を修正し、文の構造を改善しています。修正内容は、主に1文のテキストが再配置され、不要な改行タグが削除されました。

具体的には、テキストの最後の部分からブラケットで囲まれた改行タグが削除され、情報がより流れるように修正されています。これにより、テキストが一貫して読みやすくなり、ユーザーがドキュメントを通じてよりスムーズに情報を得られるようにしています。

このような小さな変更が、全体的なユーザーエクスペリエンスを向上させることに貢献します。

## articles/ai-services/document-intelligence/prebuilt/id-document.md{#item-bf45fa}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 02/10/2025
+ms.date: 07/29/2025
 ms.author: lajanuar
 ms.custom: references.regions
 ---
@@ -32,7 +32,14 @@ ms.custom: references.regions
 
 ::: moniker range=">=doc-intel-3.0.0"
 
-Document Intelligence Identity document (ID) model combines Optical Character Recognition (OCR) with deep learning models to analyze and extract key information from identity documents. The API analyzes identity documents (including the following) and returns a structured JSON data representation.
+> [!NOTE]
+>
+> Document Intelligence `v4.0 2024-11-30 (GA)` API for the prebuilt Identity document (ID) model now supports identification documents from all regions worldwide, including expanded coverage across the United States, Asia, Europe, Africa, and Oceania.
+>
+
+> [!NOTE]
+>
+> Document Intelligence Identity document (ID) model combines Optical Character Recognition (OCR) with deep learning models to analyze and extract key information from identity documents. The API analyzes identity documents (including the following) and returns a structured JSON data representation.
 
 | Region | Document types |
 |--------|----------------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "IDドキュメントモデルに関する概要の更新"
}
```

### Explanation
この変更は、Azure AI Document IntelligenceのIDドキュメントモデルに関するドキュメントの内容を更新し、特にAPIのサポートされる地域の情報を強調しています。具体的には、いくつかの重要な情報が追加されたことが特徴です。

1つ目の追加内容は、新しいバージョンのAPI (`v4.0 2024-11-30 (GA)`) に関する通知で、グローバルに展開されている身分証明書（ID）ドキュメントのサポートを含むことを明確にしています。これにより、ユーザーはどの地域の文書がサポートされているかを理解しやすくなっています。

さらに、従来の文についても、内容の開始部分にノートが追加され、モデルの機能についての理解を深める情報が補足されています。これにより、ドキュメントの全体的な情報提供の質が向上しています。

元のテキストの一部は整理され、理解を助ける形式で再構成されており、ユーザーがAPIの機能とサポートを把握しやすくしています。

## articles/ai-services/document-intelligence/quickstarts/studio-custom-project.md{#item-f52b95}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ monikerRange: '>=doc-intel-3.0.0'
 
 For details on subscription, resource, and authentication setup, *see* [Get started with Document Intelligence Studio](get-started-studio.md#prerequisites-for-new-users).
 
-## Additional prerequisites for custom projects
+## Prerequisites for custom projects
 
 In addition to the Azure account and a Document Intelligence or Azure AI Foundry resource, you need:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムプロジェクトに関する前提条件の見出し修正"
}
```

### Explanation
この変更は、Azure Document Intelligenceのクイックスタートガイドにおけるカスタムプロジェクトに関連するセクションの見出しを修正しています。具体的には、「Additional prerequisites for custom projects」という見出しが「Prerequisites for custom projects」に変更されました。

この修正は、見出しの表現を簡潔にし、情報の一貫性を高めることを目的としています。新しい見出しは、読者に対して必要な前提条件が何であるかを明確に示すものであり、内容全体の流れを良くしています。

変更前の表現は冗長的であった可能性があり、修正後は必要な情報にすぐにアクセスしやすくなっています。このような小さな更新が、ドキュメントの可読性を向上させ、ユーザーにとっての利便性を高める要因となります。


