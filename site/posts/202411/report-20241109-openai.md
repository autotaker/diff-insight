---
date: '2024-11-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6e04dd6...MicrosoftDocs:e12bec9
summary: |-
  以下の3つのドキュメントにマイナーな更新がありました。主な変更点は新しい情報や説明の追加です。

  まず、`use-your-data-securely.md` では、Azure AI Studioプロジェクトでのプライベートエンドポイント関連に「Reader」ロールが追加されました。これはBlobストレージからのデータ読み取りをセキュアにし、データセキュリティ管理に関する指針を提供します。

  次に、`global-batch.md` では、新たに「南インド」、「スイス北部」、「イギリス南部」の地域情報が更新され、GPTモデルの利用可能なバージョンが示されています。これにより、適切なモデル選択が可能になります。

  最後に、`overview.md` では画像処理機能に関する説明が明確化され、GPT-4oのトークン消費に関する違いが説明されています。これによりユーザーは効果的な利用ができるようになります。

  全体として、これらの更新により、Azure AIサービスをより安全で効果的に利用することが期待されます。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6e04dd6...MicrosoftDocs:e12bec9){target="_blank"}

<format>
# ハイライト
以下の3つのドキュメントに対するマイナーな更新が行われました。新しい情報や説明の追加が主な変更点です。

## 新機能
- `use-your-data-securely.md` において、Azure AI Studioプロジェクトでのプライベートエンドポイント関連の「Reader」ロールの追加。

## 破壊的変更
- 資料の更新による破壊的な変更はありません。
  
## その他の更新
- `global-batch.md` における、地域別で利用可能なGPTモデルのバージョン情報の更新。
- `overview.md` での画像処理機能に関するテキストの明確化。

# インサイト
このコード差分は、Azure AIサービスに関連するドキュメントにおいて、主に利用者の理解を深め、最新のサービス提供内容に情報をアップデートすることを目的としています。

最初に、`use-your-data-securely.md` において、Azure AI StudioでのBlobストレージに関連する新しい「Reader」ロールが文書中に追加されました。これにより、プロジェクト内でのBlobストレージからのデータ読み取りがセキュアになるとともに、ユーザーがどのようにデータセキュリティを管理するかについて、より明確な指針が示されることになります。

次に、`global-batch.md` では、新たに「南インド」、「スイス北部」、および「イギリス南部」という地域が追加され、それぞれのGPTモデルの利用可能なバージョンが示されました。このような更新は、グローバルバッチモデルの利用可能地域を把握したいユーザーにとって、非常に有益な情報です。更新された地域情報により、ビジネスニーズに合ったモデルを迅速に選択できることでしょう。

最後に、`overview.md` の画像処理機能に関する説明が明確化されました。特に、低詳細および高詳細モードにおけるGPT-4oのトークン消費の違いが明示され、これによりどちらのモードが特定の処理に適しているか判断する材料をユーザーに提供します。これにより、Azure OpenAIの画像処理機能を活用する際の選択肢を広げ、効果的な利用を促す狙いがあります。

全体を通して、この更新によってユーザーはAzure AIサービスをより安全に、かつ効果的に利用することが可能となります。各ドキュメントの最新情報により、ユーザーエクスペリエンスの向上が期待される変更です。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [use-your-data-securely.md](#item-76e120) | minor update | データセキュリティに関する情報の追加 | modified | 1 | 0 | 1 | 
| [global-batch.md](#item-929e6a) | minor update | グローバルバッチモデルの地域別対応の更新 | modified | 6 | 2 | 8 | 
| [overview.md](#item-97d507) | minor update | 画像処理機能に関する説明の明確化 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/ai-services/openai/how-to/use-your-data-securely.md{#item-76e120}

<details>
<summary>Diff</summary>
````diff
@@ -273,6 +273,7 @@ So far you have already setup each resource work independently. Next you need to
 | `Storage Blob Data Contributor` | Azure OpenAI | Storage Account | Reads from the input container, and writes the preprocessed result to the output container. |
 | `Cognitive Services OpenAI Contributor` | Azure AI Search | Azure OpenAI | Custom skill. |
 | `Storage Blob Data Reader` | Azure AI Search | Storage Account | Reads document blobs and chunk blobs. |
+| `Reader` | Azure AI Studio Project | Azure Storage Private Endpoints (Blob & File) | Read search indexes created in blob storage within an AI Studio Project. |
 | `Cognitive Services OpenAI User` | Web app | Azure OpenAI | Inference. |
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データセキュリティに関する情報の追加"
}
```

### Explanation
この変更では、`use-your-data-securely.md`ドキュメントに新しい情報が追加されました。具体的には、Azure AI StudioプロジェクトでのBlobおよびファイルのプライベートエンドポイントに関連する「Reader」ロールが追加され、これによりAIスタジオプロジェクト内のBlobストレージに作成された検索インデックスを読み取ることができることが明示されています。この修正は、Azureのセキュリティ設定に関する理解を深め、データを安全に利用するためのステップを提供します。

## articles/ai-services/openai/includes/model-matrix/global-batch.md{#item-929e6a}

<details>
<summary>Diff</summary>
````diff
@@ -5,16 +5,20 @@ description: Regional availability for Global Batch models
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 10/31/2024
+ms.date: 11/07/2024
 ---
 
 | **Region**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
 |:-----------------|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
+| australiaeast    | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | canadaeast       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | eastus           | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | eastus2          | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | northcentralus   | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | southcentralus   | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southindia       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | swedencentral    | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| switzerlandnorth | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| uksouth          | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
 | westus           | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westus3          | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westus3          | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルバッチモデルの地域別対応の更新"
}
```

### Explanation
この変更では、`global-batch.md`ドキュメントに地域別の利用可能性に関する情報が更新されました。具体的には、シートに新しい地域（南インド、スイス北部、イギリス南部）が追加され、それぞれの地域で利用可能なGPTモデルのバージョンが示されています。また、ドキュメントの最終更新日が2024年10月31日から2024年11月7日に変更されました。この更新は、ユーザーが利用可能なモデルや地域を容易に確認できるようにするものです。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -93,9 +93,9 @@ Azure OpenAI's image processing capabilities with GPT-4o, GPT-4o mini, and GPT-4
   - Low detail allows the API to return faster responses for scenarios that don't require high image resolution analysis. The tokens consumed for low detail images are:
     - **GPT-4o and GPT-4 Turbo with Vision**: Flat rate of **85 tokens per image**, regardless of size.
     - **GPT-4o mini**: Flat rate of **2833 tokens per image**, regardless of size.
-  - **Example: 4096 x 8192 image (low detail)**: The cost is a fixed 85 tokens, because it's a low detail image, and the size doesn't affect the cost in this mode.
+  - **Example: 4096 x 8192 image (low detail)**: The cost is a fixed 85 tokens with GPT-4o, because it's a low detail image, and the size doesn't affect the cost in this mode.
 - **High resolution mode**
-  - Low detail allows the API to analyze images in more detail. Image tokens are calculated based on the image's dimensions. The calculation involves the following steps:
+  - High detail allows the API to analyze images in more detail. Image tokens are calculated based on the image's dimensions. The calculation involves the following steps:
     1. **Image resizing**: The image is resized to fit within a 2048 x 2048 pixel square. If the shortest side is larger than 768 pixels, the image is further resized so that the shortest side is 768 pixels long. The aspect ratio is preserved during resizing.
     1. **Tile calculation**: Once resized, the image is divided into 512 x 512 pixel tiles. Any partial tiles are rounded up to a full tile. The number of tiles determines the total token cost.
     1. **Token calculation**:
@@ -139,4 +139,4 @@ Learn more about each model on our [models concept page](./concepts/models.md).
 
 ## Next steps
 
-Learn more about the [underlying models that power Azure OpenAI](./concepts/models.md).
\ No newline at end of file
+Learn more about the [underlying models that power Azure OpenAI](./concepts/models.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像処理機能に関する説明の明確化"
}
```

### Explanation
この変更では、`overview.md`ドキュメント内でAzure OpenAIの画像処理機能に関するテキストが修正されました。具体的には、低詳細および高詳細モードの説明が明確にされ、低詳細モードにおけるGPT-4oのトークン消費が正確に記載されています。また、低詳細と高詳細の説明が正確に置き換えられ、各モードの役割が明確になっています。この修正は、ユーザーがAzure OpenAIの画像処理機能をより理解しやすくすることを目的としています。


