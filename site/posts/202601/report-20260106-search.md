---
date: '2026-01-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4c4d763...MicrosoftDocs:2159f0d
summary: このコードの差分では、ドキュメントの微細なテキスト更新と用語の調整が行われています。主に、文章のトーンやリンクの正確性、タイトルの明確さに焦点を当てた修正が含まれており、ドキュメントの読みやすさとユーザーのナビゲーション体験を向上させます。新機能や破壊的変更は含まれておらず、文章のトーン調整やリンクの修正が行われています。これにより、信頼性の高い情報提供が実現されることが期待されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4c4d763...MicrosoftDocs:2159f0d){target="_blank"}

# ハイライト
このコードの差分では、ドキュメントの微細なテキスト更新と用語の調整が行われています。特に、文章のトーンやリンクの正確性、タイトルの明確さに焦点を当てた修正が含まれます。このようなマイナーアップデートは、ドキュメントの読みやすさとユーザーのナビゲーション体験を向上させます。

## 新機能
今回の修正には新機能は含まれていません。

## 破壊的変更
破壊的変更はありません。

## その他の更新
- 文章のトーン調整（例："expect to" を "you are expected to" に変更）。
- タイトルとリンクの修正により情報の明確化を図りました。
- 用語とリンクの修正を通じて、適切なリソースへの案内を強化しました。

# 洞察
この更新は多くのマイナーな修正を含んでいますが、それはドキュメント全体の質と利用者の利便性を向上させる上で重要です。以下の点が特に強調できます：

1. **文章のトーンとスタイルの改善**: 細部の表現を洗練させることで、読者に対する情報提供がよりクリアでプロフェッショナルになります。このような調整は、特に技術文書において信頼性を高めます。

2. **リンクの正確性と整合性の向上**: ドキュメント内のリンクは、適切な情報源にユーザーを誘導するための重要なツールです。今回の修正により、リンク先の整合性が確認され、読者が誤って無関係なページに誘導される可能性が減少します。これによりユーザーエクスペリエンスが向上し、資料の信頼性がさらに増します。

3. **タイトルの明確化**: タイトルに説明的な要素を加えることで、ドキュメントのテーマを迅速に理解できるようになります。これは特に、検索結果から特定の情報を見つけ出す際に役立ちます。

4. **用語の一貫性の維持**: 用語やフレーズの一貫性は、読者に対するメッセージの明瞭さを保つだけでなく、ドキュメントの全体的なスタイルの一貫性にも寄与します。これは、特に大規模なドキュメントセットにおいて重要です。

これらの修正が積み重なることで、最終的には読者に対してより信頼性の高い情報提供が可能になると考えられます。また、技術文書の目的である「正確で迅速な情報の提供」という点でも、このような継続的な改善は意義深いものと言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-concept-intro.md](#item-bf9ed7) | minor update | 小さな文の変更: Cognitive Search の導入 | modified | 1 | 1 | 2 | 
| [cognitive-search-output-field-mapping.md](#item-31fe9c) | minor update | タイトルの明確化: 認知検索の出力フィールドマッピング | modified | 1 | 1 | 2 | 
| [cognitive-search-skill-azure-openai-embedding.md](#item-3eca57) | minor update | 用語の修正: Azure OpenAI 埋め込みスキル | modified | 1 | 1 | 2 | 
| [cognitive-search-skill-genai-prompt.md](#item-384bf9) | minor update | リンクの修正: GenAIプロンプトスキル | modified | 5 | 5 | 10 | 
| [search-blob-storage-integration.md](#item-bbdaa6) | minor update | 説明の明確化: Blobストレージ統合 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/cognitive-search-concept-intro.md{#item-bf9ed7}

<details>
<summary>Diff</summary>
````diff
@@ -62,7 +62,7 @@ Open-source, third-party, or first-party code can be integrated into the pipelin
 
 ### Use-cases for built-in skills
 
-Built-in skills are based on the Foundry Tools APIs: [Azure Vision](/azure/ai-services/computer-vision/) and [Azure Language](/azure/ai-services/language-service/overview). Unless your content input is small, expect to [attach a billable Microsoft Foundry resource](cognitive-search-attach-cognitive-services.md) to run larger workloads.
+Built-in skills are based on the Foundry Tools APIs: [Azure Vision](/azure/ai-services/computer-vision/) and [Azure Language](/azure/ai-services/language-service/overview). Unless your content input is small, you are expected to [attach a billable Microsoft Foundry resource](cognitive-search-attach-cognitive-services.md) to run larger workloads.
 
 A [skillset](cognitive-search-defining-skillset.md) that's assembled using built-in skills is well suited for the following application scenarios:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "小さな文の変更: Cognitive Search の導入"
}
```

### Explanation
このコードの変更は、`articles/search/cognitive-search-concept-intro.md`ファイル内の文章をわずかに修正するもので、具体的には「expect to」を「you are expected to」に置き換えています。この変更により、文章のトーンが少し洗練され、読者への伝え方が明確になります。このような修正は、文の流れや理解を助けるために重要です。変更された内容は、組み込みスキルを使用する場合にMicrosoft Foundryリソースが必要になることを説明しています。この文の改善は、ドキュメントの質を向上させるための一環です。

## articles/search/cognitive-search-output-field-mapping.md{#item-31fe9c}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.date: 04/14/2025
 ms.update-cycle: 365-days
 ---
 
-# Map enriched output to fields in a search index in Azure AI Search
+# Map enriched output to fields in a search index (output field mappings)
 
 :::image type="content" source="media/cognitive-search-output-field-mapping/indexer-stages-output-field-mapping.png" alt-text="Diagram of the Indexer Stages with Output Field Mappings highlighted.":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "タイトルの明確化: 認知検索の出力フィールドマッピング"
}
```

### Explanation
このコードの変更は、`articles/search/cognitive-search-output-field-mapping.md`ファイルのタイトルをわずかに修正しており、新しいタイトルは「Map enriched output to fields in a search index (output field mappings)」となっています。この修正は、タイトルに「(output field mappings)」というフレーズを追加することで、読者が文書の主題をより明確に理解できるようにしています。このような小さな変更は、文書のナビゲーションを改善し、テーマをよりはっきりと表現します。これは特に、検索インデックスにおける出力フィールドのマッピングに関して、より具体的な情報を提供することに寄与します。

## articles/search/cognitive-search-skill-azure-openai-embedding.md{#item-3eca57}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.date: 10/23/2025
 
 #	Azure OpenAI Embedding skill
 
-The **Azure OpenAI Embedding** skill connects to an embedding model deployed to your [Azure OpenAI in Foundry Models](/azure/ai-services/openai/overview) resource or [Microsoft Foundry](/azure/ai-foundry/what-is-azure-ai-foundry) project to generate embeddings during indexing. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed.
+The **Azure OpenAI Embedding** skill connects to an embedding model deployed to your [Azure OpenAI in Foundry Models](/azure/ai-services/openai/overview) resource or [Microsoft Foundry](/azure/ai-foundry/what-is-foundry) project to generate embeddings during indexing. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed.
 
 The [**Import data (new)** wizard](search-get-started-portal-import-vectors.md) in the Azure portal uses the Azure OpenAI Embedding skill to vectorize content. You can run the wizard and review the generated skillset to see how the wizard builds the skill for embedding models.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の修正: Azure OpenAI 埋め込みスキル"
}
```

### Explanation
このコードの変更は、`articles/search/cognitive-search-skill-azure-openai-embedding.md`ファイル内の文をわずかに修正しています。具体的には、"Microsoft Foundry"プロジェクトに関する表現が「[Microsoft Foundry](/azure/ai-foundry/what-is-azure-ai-foundry)」から「[Microsoft Foundry](/azure/ai-foundry/what-is-foundry)」に変更されています。この修正は、リンク先の正確性を向上させ、より適切な情報への導きを提供することを目的としています。なお、この埋め込みスキルがどのように機能するかを説明する部分に影響を与えるもので、ドキュメント全体の理解を助ける重要な修正です。

## articles/search/cognitive-search-skill-genai-prompt.md{#item-384bf9}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.date: 10/23/2025
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-The **GenAI (Generative AI) Prompt** skill executes a *chat completion* request against a large language model (LLM) deployed in [Azure OpenAI in Foundry Models](/azure/ai-services/openai/overview) or [Microsoft Foundry](/azure/ai-foundry/what-is-azure-ai-foundry). Use this skill to create new information that can be indexed and stored as searchable content.
+The **GenAI (Generative AI) Prompt** skill executes a *chat completion* request against a large language model (LLM) deployed in [Azure OpenAI in Foundry Models](/azure/ai-services/openai/overview) or [Microsoft Foundry](../ai-foundry/what-is-foundry.md). Use this skill to create new information that can be indexed and stored as searchable content.
 
 Here are some examples of how the GenAI prompt skill can help you create content:
 
@@ -35,7 +35,7 @@ The GenAI Prompt skill is available in the [latest preview REST API](/rest/api/s
 
 ## Supported models
 
-- You can use any [chat completion inference model](/azure/ai-foundry/model-inference/concepts/models) deployed in Foundry, such as GPT models, Deepseek R#, Llama-4-Mavericj, and Cohere-command-r. For GPT models specifically, only the chat completions API endpoints are supported. Endpoints using the Azure OpenAI Responses API (containing `/openai/responses` in the URI) aren't currently compatible.
+- You can use any [chat completion inference model](../ai-foundry/foundry-models/concepts/models.md) deployed in Foundry, such as GPT models, Deepseek R#, Llama-4-Mavericj, and Cohere-command-r. For GPT models specifically, only the chat completions API endpoints are supported. Endpoints using the Azure OpenAI Responses API (containing `/openai/responses` in the URI) aren't currently compatible.
 
 - For image verbalization, the model you use to analyze the image determines what image formats are supported.
 
@@ -49,7 +49,7 @@ The GenAI Prompt skill is available in the [latest preview REST API](/rest/api/s
 
 ## Prerequisites
 
-- An [Azure OpenAI in Foundry Models resource](/azure/ai-foundry/openai/how-to/create-resource) or [Foundry project](/azure/ai-foundry/how-to/create-projects).
+- An [Azure OpenAI in Foundry Models resource](../ai-foundry/openai/how-to/create-resource.md) or [Foundry project](../ai-foundry/how-to/create-projects.md).
 
 - A [supported model](#supported-models) deployed to your resource or project.
 
@@ -61,7 +61,7 @@ The GenAI Prompt skill is available in the [latest preview REST API](/rest/api/s
 
   - On Azure OpenAI, assign [**Cognitive Services OpenAI User**](/azure/ai-services/openai/how-to/role-based-access-control) to the managed identity.
 
-  - On Foundry, assign [**Azure AI User**](/azure/ai-foundry/concepts/rbac-azure-ai-foundry#azure-ai-user) to the managed identity.
+  - On Foundry, assign [**Azure AI User**](../ai-foundry/concepts/rbac-foundry.md#built-in-roles) to the managed identity.
 
 ## @odata.type  
 
@@ -249,5 +249,5 @@ The GenAI Prompt skill is available in the [latest preview REST API](/rest/api/s
 - [Azure AI Search built-in indexers](search-indexer-overview.md)
 - [Integrated vectorization](vector-search-integrated-vectorization.md)
 - [How to define a skillset](cognitive-search-defining-skillset.md)  
-- [How to generate chat completions with Azure AI model inference (Foundry)](/azure/ai-foundry/model-inference/how-to/use-chat-completions)  
+- [How to generate chat completions with Azure AI model inference (Foundry)](../ai-foundry/foundry-models/how-to/use-chat-completions.md)  
 - [Structured outputs in Azure OpenAI](/azure/ai-services/openai/how-to/structured-outputs)  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの修正: GenAIプロンプトスキル"
}
```

### Explanation
このコードの変更は、`articles/search/cognitive-search-skill-genai-prompt.md`ファイルにおいて複数のリンクのパスを修正しています。具体的には、"Microsoft Foundry"に関連するリンクや、他のリソースへのリンクが更新され、より正確な参照を提供するようになりました。この変更により、ユーザーは関連情報にアクセスしやすくなり、理解が深まることが期待されます。

変更点には具体的に、`/azure/ai-foundry/what-is-azure-ai-foundry`から`../ai-foundry/what-is-foundry.md`へのリンクの修正、また、サポートされているモデルや前提条件に関するリンクの更新が含まれます。これにより、ダイレクトに関連するリソースに接続でき、ドキュメント全体の整合性が向上します。

## articles/search/search-blob-storage-integration.md{#item-bbdaa6}

<details>
<summary>Diff</summary>
````diff
@@ -45,7 +45,7 @@ You can start directly in your Storage Account portal page.
 
 1. In the left navigation page under **Data management**, select **Azure AI Search** to select or create a search service. 
 
-1. Use an [import wizard](search-get-started-skillset.md) to extract and optionally create searchable content from your blobs. The workflow creates an indexer, data source, index, and option skillset on your Azure AI Search service.
+1. Use an [import wizard](search-get-started-skillset.md) to extract and optionally create searchable content from your blobs. The workflow creates an indexer, data source, index, and optional skillset on your Azure AI Search service.
 
    :::image type="content" source="media/search-blob-storage-integration/blob-blade.png" alt-text="Screenshot of the Azure AI Search wizard in the Azure Storage portal page." border="true":::
 
@@ -118,7 +118,7 @@ Add the following metadata properties and values to blobs in Blob Storage. When
 | Property name | Property value | Explanation |
 | ------------- | -------------- | ----------- |
 | "AzureSearch_Skip" |`"true"` |Instructs the blob indexer to completely skip the blob. Neither metadata nor content extraction is attempted. This is useful when a particular blob fails repeatedly and interrupts the indexing process. |
-| "AzureSearch_SkipContent" |`"true"` |This is equivalent to the `"dataToExtract" : "allMetadata"` setting described [above](#PartsOfBlobToIndex) scoped to a particular blob. | 
+| "AzureSearch_SkipContent" |`"true"` |This is equivalent to the `"dataToExtract": "allMetadata"` setting described [here](/rest/api/searchservice/indexers/create?#blobindexerdatatoextract) but just scoped to a particular blob. | 
 
 ### Indexing blob metadata
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "説明の明確化: Blobストレージ統合"
}
```

### Explanation
このコードの変更は、`articles/search/search-blob-storage-integration.md`ファイルの内容において、特定の情報の表現をクリアにするための修正です。具体的には、Blobストレージから検索可能なコンテンツを抽出するために使用する「インポートウィザード」に関する説明が若干の更新を受けました。

1つ目の変更では、インポートウィザードが作成する要素のリストにおける「option skillset」が「optional skillset」に修正されています。この変更により、表記に一貫性が生まれ、より理解しやすくなっています。

2つ目の変更では、Blobストレージ内のメタデータプロパティに関する説明が改善されています。「ここで説明されている」との表現が、「ここで」というリンク付きの説明に置き換えられ、ユーザーが具体的な参考資料を容易に見つけられるようになっています。これにより、関連情報へのアクセスが向上し、ドキュメントの理解がさらに進むことが期待されます。


