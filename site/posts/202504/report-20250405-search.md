---
date: '2025-04-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a4ad9b8...MicrosoftDocs:f85abdf
summary: この更新では、Azure AI Foundryのモデルカタログへのリンクのテキストが修正され、情報の正確性が向上しました。特に新機能や互換性を壊す変更はありませんが、文言の微調整がユーザーエクスペリエンスに良い影響を与えることが期待されています。正確な情報を提供することで、全体のドキュメントの一貫性と信頼性が保たれ、最終的にはユーザーの信頼を高める役割を果たしています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a4ad9b8...MicrosoftDocs:f85abdf){target="_blank"}

# ハイライト
この更新では、ドキュメント「search-get-started-portal-import-vectors.md」でAzure AI Foundryのモデルカタログへのリンクのテキストが修正されました。具体的な変更はフレーズの訂正であり、情報の正確性を向上することを目指しています。

## 新機能
特に新機能は追加されていません。

## 互換性を壊す変更
今回の更新には互換性を壊す変更はありません。

## その他の更新
「Azure AI Foundryモデルカタログ」というフレーズが、「Azure AI Foundry」に置き換えられました。

# 洞察
このドキュメントの更新は、テキストの微調整であるものの、非常に重要な役割を果たしています。特に、ユーザーがリンクを利用する際に正しい情報源やリソースにたどり着けるかどうかは、ユーザーエクスペリエンスと製品の利用効率に大きく影響します。誤ったリンクや不正確な名称は誤解を生みやすく、結果としてユーザーの信頼を損ねる可能性があります。したがって、このような小さな変更でも、全体のドキュメントの一貫性と信頼性をサポートするためには重要です。

この変更が特に小規模なものであり、技術的な機能の追加や削除ではないものの、「正確な情報提供」という観点から全体的なユーザーサポートと製品価値の向上に寄与していると言えるでしょう。小さな改善が積み重なって、より良いユーザーエクスペリエンスを実現することができるという好例です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | AI Foundryのリファレンスリンクの修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -47,7 +47,7 @@ Use an embedding model on an Azure AI platform in the [same region as Azure AI S
 | Provider | Supported models |
 |---|---|
 | [Azure OpenAI Service](https://aka.ms/oai/access) | text-embedding-ada-002 <br>text-embedding-3-large <br>text-embedding-3-small |
-| [Azure AI Foundry model catalog](/azure/ai-foundry/what-is-ai-foundry) | For text: <br>Cohere-embed-v3-english <br>Cohere-embed-v3-multilingual <br>For images: <br>Facebook-DinoV2-Image-Embeddings-ViT-Base <br>Facebook-DinoV2-Image-Embeddings-ViT-Giant |
+| [Azure AI Foundry model catalog](/azure/ai-foundry/what-is-azure-ai-foundry) | For text: <br>Cohere-embed-v3-english <br>Cohere-embed-v3-multilingual <br>For images: <br>Facebook-DinoV2-Image-Embeddings-ViT-Base <br>Facebook-DinoV2-Image-Embeddings-ViT-Giant |
 | [Azure AI services multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills) | [Azure AI Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) for image and text vectorization, [available in selected regions](/azure/ai-services/computer-vision/how-to/image-retrieval?tabs=csharp). Depending on how you [attach the multi-service resource](cognitive-search-attach-cognitive-services.md), the multi-service account might need to be in the same region as Azure AI Search. |
 
 If you use the Azure OpenAI Service, the endpoint must have an associated [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains). A custom subdomain is an endpoint that includes a unique name (for example, `https://hereismyuniquename.cognitiveservices.azure.com`). If the service was created through the Azure portal, this subdomain is automatically generated as part of your service setup. Ensure that your service includes a custom subdomain before using it with the Azure AI Search integration.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryのリファレンスリンクの修正"
}
```

### Explanation
この変更は、ドキュメント「search-get-started-portal-import-vectors.md」において、Azure AI Foundryのモデルカタログへのリンクのテキストを修正するという、小規模な更新です。具体的には、「Azure AI Foundryモデルカタログ」というフレーズが修正され、正確な名称「Azure AI Foundry」に置き換えられています。この変更は、情報の正確性を向上させ、ユーザーが正しいリソースにアクセスできるようにすることを目的としています。


