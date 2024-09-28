---
date: '2024-09-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:022de22...MicrosoftDocs:3b0d11e
summary: このコードの変更は、Azure AI Searchにおける管理対象アイデンティティを使用したデータソース接続方法に関する更新です。新たに「Azure
  OpenAI」や「Azure AI Studio」、「Azure Functions」との接続情報が統合され、利便性が向上しました。特に破壊的な変更はなく、最終更新日も最新の情報に反映されています。この変更により、ユーザーは接続オプションをより簡単に理解でき、効率的に作業できるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:022de22...MicrosoftDocs:3b0d11e){target="_blank"}

# ハイライト
このコードの変更は、Azure AI Searchのドキュメントにおける管理対象アイデンティティを使用したデータソース接続方法に関する更新です。

## 新機能
- 新たに「Azure OpenAI」と「Azure AI Studio」および「Azure Functions」との接続情報が統合された。

## 破壊的変更
- 特に破壊的な変更はありません。

## その他の更新
- ドキュメントの最終更新日が2024年7月25日から2024年9月11日に変更されました。
- 接続方法に関する表の内容が具体的に調整されました。

# インサイト
この変更は、Azure AI Searchを利用する際の利便性とドキュメントの一貫性を改善することを目的としています。以下のポイントに注目してください。

1. **管理対象アイデンティティ**: 管理対象アイデンティティを使用することで、ユーザーは接続情報を手動で管理する必要がなくなり、セキュリティが向上します。この更新により、ユーザーが新しい接続オプションを利用しやすくなった点は大きな進歩です。

2. **ドキュメントの明確化**: 「Azure OpenAI」および「Azure AI Studio」と「Azure Functions」を通じた接続情報がより明確に統合されました。これにより、ユーザーが異なる接続オプションを把握しやすくなり、適切な方法を選択する際の混乱が減少します。

3. **最終更新日**: ドキュメントの最終更新日が変更されたことは、ユーザーにとって信頼性の指標となります。最新の情報が反映されていることを確認できるため、ユーザーは常に最新かつ正確なガイダンスを受け取ることができます。

この変更は、特にAzure AI Searchを利用する開発者や管理者にとって、作業の効率化と理解のしやすさを提供するものです。接続オプションが明確になることで、選択肢を比較して最適な方法を選ぶ際の参考になります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-howto-managed-identities-data-sources.md](#item-edf98d) | minor update | 検索サービスにおける管理対象アイデンティティのデータソースに関する変更 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/search/search-howto-managed-identities-data-sources.md{#item-edf98d}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: how-to
-ms.date: 07/25/2024
+ms.date: 09/11/2024
 ---
 
 # Configure a search service to connect using a managed identity in Azure AI Search
@@ -48,13 +48,13 @@ A search service uses Azure Storage as an indexer data source and as a data sink
 | [Debug sessions (hosted in Azure Storage)](cognitive-search-debug-session.md)	<sup>1</sup> | Yes | No |
 | [Enrichment cache (hosted in Azure Storage)](search-howto-incremental-index.md) <sup>1,</sup> <sup>2</sup> | Yes | Yes |
 | [Knowledge Store (hosted in Azure Storage)](knowledge-store-create-rest.md) <sup>1</sup>| Yes | Yes |
-| Connections to Azure OpenAI or Azure AI <sup>3</sup> | Yes | Yes |
+| Connections to Azure OpenAI, Azure AI Studio and Azure Functions via skills/vectorizers <sup>3</sup> | Yes | Yes |
 
 <sup>1</sup> For connectivity between search and storage, your network security configuration imposes constraints on which type of managed identity you can use. Only a system managed identity can be used for a same-region connection to storage via the trusted service exception or resource instance rule. See [Access to a network-protected storage account](search-indexer-securing-resources.md#access-to-a-network-protected-storage-account) for details.
 
 <sup>2</sup> AI search service currently can't connect to tables on a storage account that has [shared key access turned off](/azure/storage/common/shared-key-authorization-prevent).
 
-<sup>3</sup> Connections to Azure OpenAI or Azure AI include: [Custom skill](cognitive-search-custom-skill-interface.md), [Custom vectorizer](vector-search-vectorizer-custom-web-api.md), [Azure OpenAI embedding skill](cognitive-search-skill-azure-openai-embedding.md), [Azure OpenAI vectorizer](vector-search-how-to-configure-vectorizer.md), [AML skill](cognitive-search-aml-skill.md), [Azure AI Studio model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md), [Azure AI Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md), [Azure AI Vision vectorizer](vector-search-vectorizer-ai-services-vision.md).
+<sup>3</sup> Connections to Azure OpenAI,  Azure AI Studio and Azure Functions via skills/vectorizers include: [Custom skill](cognitive-search-custom-skill-interface.md), [Custom vectorizer](vector-search-vectorizer-custom-web-api.md), [Azure OpenAI embedding skill](cognitive-search-skill-azure-openai-embedding.md), [Azure OpenAI vectorizer](vector-search-how-to-configure-vectorizer.md), [AML skill](cognitive-search-aml-skill.md) and [Azure AI Studio model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md).
 
 ## Create a system managed identity
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスにおける管理対象アイデンティティのデータソースに関する変更"
}
```

### Explanation
この変更は、Azure AI Searchでの管理対象アイデンティティを用いた検索サービスの接続に関するドキュメントを更新しました。具体的には、最終更新日が2024年7月25日から2024年9月11日に変更され、接続方法に関する表の内容が調整されました。新しい表では、「Azure OpenAI」および「Azure AI Studio」と「Azure Functions」を通じた接続に関する情報が統合され、より明確な説明を提供しています。これにより、ユーザーがこれらの接続オプションを理解しやすくなり、ドキュメントの一貫性が向上しました。


