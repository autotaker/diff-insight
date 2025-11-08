---
date: '2025-11-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f0d677f...MicrosoftDocs:886d965
summary: この変更点では、ポータル画像検索のクイックスタートガイドが更新され、日付情報やモデル、提供者に関する情報が刷新されました。特に、Azure OpenAIモデルリソース及びAzure
  AI Foundryプロジェクトの最新情報が追加されました。この更新により、ユーザーは最新の技術にアクセスしやすくなり、適切なモデル選びが促進されます。また、日付情報の更新によって文書の整合性が向上し、Azureエコシステムを使用するユーザーエクスペリエンスが改善されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f0d677f...MicrosoftDocs:886d965){target="_blank"}

# ハイライト
この変更点では、ポータル画像検索のクイックスタートガイドにおいて日付の更新が行われ、サポートされるモデルと提供者に関する情報が刷新されました。特に、Azure OpenAIモデルリソースやAzure AI Foundryプロジェクトの最新情報が含まれています。

## 新機能
- Azure OpenAIモデルリソースとAzure AI Foundryプロジェクトに関する最新のモデル一覧が追加されました。

## 破壊的変更
- 特定の破壊的変更はありませんが、日付情報が更新され、情報の整合性が向上しました。

## その他の更新
- ドキュメント内の日付情報が、2025年10月8日から2025年10月24日に更新されました。
- サポートされるプロバイダーとモデルを示すテーブルが改定され、より詳細な提供者情報が追加されました。

# インサイト
この更新は、ユーザーがAzureの画像検索サービスを使用する際の導入部分でつまずかないようにするための重要なステップです。特に、日付情報の更新は、ドキュメントが新鮮で最新の情報を提供していることを保証する重要な役割を果たしています。また、新しく改定されたモデル情報は、ユーザーがどのプロバイダーのどのモデルを選ぶべきかの指針を提供し、より適切な選択を助けるものです。

Azure OpenAIモデルリソースとAzure AI Foundryプロジェクトの最新情報は、クラウドベースのAIソリューションを活用している開発者やデータサイエンティストにとって非常に重要であり、有効です。この更新により、ユーザーは最新の技術にアクセスしやすくなり、ビジネスニーズに応じて迅速にモデルを適用できるようになるでしょう。

全体として、この更新はAzureエコシステムを使用するユーザーエクスペリエンスを向上させ、迅速かつ効率的に画像検索を開始できるように設計されています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | ポータル画像検索のクイックスタートガイドの更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 10/08/2025
+ms.date: 10/24/2025
 ms.custom:
   - references_regions
 ---
@@ -57,7 +57,7 @@ The following table lists the supported providers and models for each method. De
 | Provider | Models for image verbalization | Models for multimodal embeddings |
 |--|--|--|
 | [Azure OpenAI in Azure AI Foundry Models resource](/azure/ai-services/openai/how-to/create-resource) <sup>1, 2</sup> | LLMs:<br>gpt-4o<br>gpt-4o-mini<br>gpt-5<br>gpt-5-mini<br>gpt-5-nano<br><br>Embedding models:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large | |
-| [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects) | Embedding models:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large | |
+| [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects) | LLMs:<br>phi-4<br>gpt-4o<br>gpt-4o-mini<br>gpt-5<br>gpt-5-mini<br>gpt-5-nano<br><br>Embedding models:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large | |
 | [Azure AI Foundry hub-based project](/azure/ai-foundry/how-to/hub-create-projects) | LLMs:<br>phi-4<br>gpt-4o<br>gpt-4o-mini<br>gpt-5<br>gpt-5-mini<br>gpt-5-nano<br><br>Embedding models:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large<br>Cohere-embed-v3-english <sup>3</sup><br>Cohere-embed-v3-multilingual <sup>3</sup> | Cohere-embed-v3-english <sup>3</sup><br>Cohere-embed-v3-multilingual <sup>3</sup> |
 | [Azure AI services multi-service resource](/azure/ai-services/multi-service-resource#azure-ai-multi-services-resource-for-azure-ai-search-skills) <sup>4</sup> | Embedding model: [Azure AI Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) <sup>5</sup> | [Azure AI Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) <sup>5</sup> |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータル画像検索のクイックスタートガイドの更新"
}
```

### Explanation
この変更は、ポータルの画像検索に関するクイックスタートガイドの一部を更新するものです。具体的には、ドキュメント内の日付情報が更新され、具体的な提供者とモデルに関するテーブルが修正されました。修正された内容には、Azure OpenAIモデルリソースとAzure AI Foundryプロジェクトのモデル一覧が含まれています。

- 変更前の日付は2025年10月8日でしたが、変更後は2025年10月24日となりました。
- サポートされるプロバイダーとモデルを示すテーブルの内容も更新され、いくつかのモデルが追加または変更され、提供者の情報がより充実しました。

この変更により、ドキュメントの最新性が保たれ、利用者にとっての有用性が向上しています。


