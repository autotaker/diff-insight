---
date: '2025-10-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0191f09...MicrosoftDocs:a6b6823
summary: ドキュメントの更新により、エージェント検索とRAGアプローチの説明が明確になりました。具体的には、新しい日付の設定、表現の具体化、デプロイメント手順の簡略化、用語の統一が行われています。エージェント検索の説明では、「任意の埋め込みモデル」が「任意の'text-embedding'モデル」と具体的に記載され、RAGアプローチに関連する用語も一貫性を持つように整理されています。これにより、ユーザーの理解が向上し、情報の取得がより迅速になることを目指しています。特に重大な変更はありませんが、全体的にユーザー体験の向上に寄与する内容です。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0191f09...MicrosoftDocs:a6b6823){target="_blank"}

# Highlights
ドキュメントの一部が更新され、エージェント検索とRAG（Retrieval-Augmented Generation）アプローチの説明が明確になりました。これには、新しい日付の設定、具体化された表現、簡略化されたデプロイメント手順および用語の統一が含まれます。

## New features
- 「agentic retrieval」セットアップに関する日付の更新と説明の明確化。
- RAGアプローチにおける用語の統一および説明の改善。

## Breaking changes
特に重大な変更はありませんが、ユーザーの理解がより明確になるような微調整が行われています。

## Other updates
- エージェント検索で使用する「任意の埋め込みモデル」が「任意の'text-embedding'モデル」と具体的に記載されるようになりました。
- デプロイメント手順が簡略化され、詳細な説明が他リンクへと誘導されるようになりました。

# Insights
今回の修正は、主にユーザー体験の向上と情報の明瞭化を目的としています。エージェント検索のセットアップに関するドキュメントでは、日付の更新が行われたほか、どのようなモデルが適切であるかをより明確にしています。この具体化によって、実装者は正確なモデルを選択しやすくなります。

また、RAGアプローチに関連するドキュメントでは、用語の統一がなされ、特に専門用語については一貫性が持たせられました。例えば、「LLM query planning」が「LLM for query planning」に修正されることで、読者はその概念の正確な用途を簡単に把握できるようになります。言葉の選び方によって、文章の明確さが改善され、ユーザーが情報をスムーズに得られることを目指しています。

これらの些細とも言える変更が積み重なることにより、最終的にはユーザーが求める情報をより速やかに取得できるようにするという大きな改善に繋がります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-setup.md](#item-e5e297) | minor update | エージェント検索のセットアップに関するドキュメントの更新 | modified | 4 | 18 | 22 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | RAGアプローチに関する用語の統一と説明の明確化 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/includes/quickstarts/agentic-retrieval-setup.md{#item-e5e297}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 08/26/2025
+ms.date: 10/16/2025
 ---
 
 ## Configure access
@@ -83,22 +83,8 @@ To get the endpoints for this quickstart, select both of the following tabs.
 
 To use agentic retrieval, you must deploy two Azure OpenAI models to your Azure AI Foundry resource:
 
-+ An embedding model for text-to-vector conversion. This quickstart uses `text-embedding-3-large`, but you can use any embedding model that supports the `text-embedding` task.
++ An embedding model for text-to-vector conversion. This quickstart uses `text-embedding-3-large`, but you can use any `text-embedding` model.
 
-+ A [supported chat completion model](../../agentic-retrieval-how-to-create-knowledge-base.md#supported-models) for query planning and answer generation. This quickstart uses `gpt-5-mini`. Optionally, you can use one model for query planning and another model for answer generation, but this quickstart uses the same model for simplicity.
++ An LLM for query planning and answer generation. This quickstart uses `gpt-5-mini`, but you can use any [supported LLM for agentic retrieval](../../agentic-retrieval-how-to-create-knowledge-base.md#supported-models).
 
-To deploy the Azure OpenAI models:
-
-1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and select your Azure AI Foundry resource.
-
-1. From the left pane, select **Model catalog**.
-
-1. Select **text-embedding-3-large**, and then select **Use this model**.
-
-1. Enter a deployment name. To simplify your code, we recommend **text-embedding-3-large**.
-
-1. Leave the default settings.
-
-1. Select **Deploy**.
-
-1. Repeat the previous steps, but this time, deploy **gpt-5-mini** from the model catalog.
+For deployment instructions, see [Deploy Azure OpenAI models with Azure AI Foundry](/azure/ai-foundry/how-to/deploy-models-openai).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索のセットアップに関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、`agentic-retrieval-setup.md`というファイルに対する修正であり、ドキュメントの更新を含んでいます。主な変更点としては、日付の更新と文言の簡略化が含まれています。具体的には、文書の日付が2025年8月26日から2025年10月16日に変更され、エージェント検索に必要なモデルの説明が明確化されました。以前は、「任意の埋め込みモデル」という表現が使われていましたが、現在は「任意の'text-embedding'モデル」と具体的に記載されています。また、デプロイメント手順が簡略化され、別のリンクにて詳細な説明を参照するように案内がされています。この変更は、ユーザーがエージェント検索を実装する際の理解を助けることを目的としています。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ You can choose between two approaches for RAG workloads: agentic retrieval, or t
 > [!NOTE]
 > New to copilot and RAG concepts? Watch [Vector search and state of the art retrieval for Generative AI apps](https://www.youtube.com/watch?v=lSzc1MJktAo).
 
-## Modern RAG with Agentic Retrieval
+## Modern RAG with agentic retrieval
 
 Azure AI Search now provides **agentic retrieval**, a specialized pipeline designed specifically for RAG patterns. This approach uses large language models to intelligently break down complex user queries into focused subqueries, executes them in parallel, and returns structured responses optimized for chat completion models.
 
@@ -53,7 +53,7 @@ For new RAG implementations, we recommend starting with [agentic retrieval](agen
 
 ## Classic RAG pattern for Azure AI Search
 
-A RAG solution can be implemented on Azure AI Search using the original query execution architecture. With this approach, your application sends a single query request to Azure AI Search, the search engine processes the request, and returns search results to the caller. There's no side trip to an LLM query planning or LLM integration in the query pipeline. There's no query execution details in the response, and citations are built into the response only if you have fields in your index that provide a parent document name or page. This approach is faster and simpler with fewer components. Depending on your application requirements, it can be the best choice. 
+A RAG solution can be implemented on Azure AI Search using the original query execution architecture. With this approach, your application sends a single query request to Azure AI Search, the search engine processes the request, and returns search results to the caller. There's no side trip to an LLM for query planning or answer formulation. There's no query execution details in the response, and citations are built into the response only if you have fields in your index that provide a parent document name or page. This approach is faster and simpler with fewer components. Depending on your application requirements, it could be the best choice. 
 
 A high-level summary of classic RAG pattern built on Azure AI Search looks like this:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGアプローチに関する用語の統一と説明の明確化"
}
```

### Explanation
このコードの変更は、`retrieval-augmented-generation-overview.md`ファイルの修正に関連しており、主に用語の統一といくつかの説明の改善が行われました。特に、「agentic retrieval」という表現が、見出しレベルの文脈で大文字から小文字に変更され、スタイルの一貫性が確保されています。また、古いRAGパターンの説明部分での文言が少し明確にされ、「LLM query planning」や「LLM integration」の表現が「LLM for query planning」や「answer formulation」に修正されました。これにより、読者は何に対して言及されているかをより明確に理解できるようになりました。全体として、これらの変更は情報の明瞭さを向上させ、ユーザー体験を改善することを意図しています。


