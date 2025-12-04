---
date: '2025-12-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8d736bf...MicrosoftDocs:cad893f
summary: 今回の変更では、特に新しい機能の追加はなく、名称の変更によりAIの利用分野を明確にする調整が行われています。破壊的変更は含まれておらず、既存の機能には影響を与えません。目次項目名称が「AI
  services」から「Foundry Tools」に変更され、関連文書内でも用語の置き換えが行われています。また、スペルミスの修正も含まれています。これらの変更は文書の精度や一貫性を向上させ、ユーザーがより効果的に情報を理解できるようにすることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8d736bf...MicrosoftDocs:cad893f){target="_blank"}

# Highlights

今回の変更では、以下の点が主に注目されます。

## 新機能
- 特に新しい機能の追加はありませんが、名称の変更によりAIの利用分野を示唆する情報がより正確になるよう調整されました。

## 破壊的変更
- 今回の変更には破壊的変更は含まれていません。名称の変更やスペル修正にとどまるため、既存の機能や動作に影響はありません。

## その他の更新
- `toc.yml` の目次項目名称が「AI services」から「Foundry Tools」に変更されました。
- `search-try-for-free.md`の中で、「AIサービス」という用語が「Foundry Tools」に置き換えられました。
- `tutorial-optimize-indexing-push-api.md`で「Programatically」のスペルが「Programmatically」に訂正されました。

# Insights

この変更は、ユーザーの理解を助けるためのマイナーアップデートですが、文書の精度と一貫性を保証する上で重要な役割を果たします。具体的な変更点として、「AI services」という言葉を「Foundry Tools」に変更したのは、より正確なツールの名称を提供することを目的としています。これは、ユーザーがドキュメントを読んで、どのツールが適用されているのかを瞬時に理解する手助けになります。

一方で、スペルミスの修正は、ドキュメントの品質を保つ基本的かつ重要な作業です。「Programatically」という誤ったスペルを「Programmatically」に変更することで、プロフェッショナルな文章に求められる信頼性を向上しています。

どれも小さな変更ですが、正確さとユーザビリティの向上に貢献しており、技術文書としての完成度を高めるための重要なステップです。ユーザーがドキュメントを使って効果的にタスクを遂行できるようにするための土台を築く意図が見られます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [toc.yml](#item-eeb848) | minor update | 目次項目の変更 | modified | 2 | 2 | 4 | 
| [search-try-for-free.md](#item-36e28d) | minor update | AIサービスの言及の変更 | modified | 1 | 1 | 2 | 
| [tutorial-optimize-indexing-push-api.md](#item-ef0e96) | minor update | プログラム的にのスペル修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/breadcrumb/toc.yml{#item-eeb848}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ items:
   items:
   - name: Search
     tocHref: /azure/reliability
-  - name: AI services
+  - name: Foundry Tools
     tocHref: /azure/ai-services/
     topicHref: /azure/ai-services/index
     items:
@@ -16,7 +16,7 @@ items:
   tocHref: /legal/
   topicHref: /azure/index
   items:
-  - name: AI services                # Original doc set name
+  - name: Foundry Tools                # Original doc set name
     tocHref: /legal/cognitive-services/    # Destination doc set route
     topicHref: /azure/ai-services/index    # Original doc set route
     items:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次項目の変更"
}
```

### Explanation
このコードの変更は、`toc.yml` ファイルにおける目次項目の名前を変更するマイナーアップデートです。具体的には、「AI services」という項目が「Foundry Tools」に変更されました。この変更により、関連するリンクや項目名が更新され、正確な方向性を提供することが目的です。内容としては、目次内の2つの行でそれぞれの名前が変更され、デリートとアディションが行われています。全体として、文書内の構造的情報が明確になると共に、ユーザーに適切な情報を提供するための改善がなされています。変更されたファイルは、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/blob/cad893f3a0d8b7c30ebc5c6c3a0a139ea7d95fa2/articles%2Fsearch%2Fbreadcrumb%2Ftoc.yml)から参照できます。

## articles/search/search-try-for-free.md{#item-36e28d}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ For a next step evaluation of [RAG scenarios](retrieval-augmented-generation-ove
 
 - Storing data
 - Deploying embedding and chat models (**Azure OpenAI**)
-- Applying AI services for creating AI-generated content during indexing (optional)
+- Applying Foundry Tools for creating AI-generated content during indexing (optional)
 - Adding information retrieval (**Azure AI Search**)
 - Adding a frontend app (optional)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIサービスの言及の変更"
}
```

### Explanation
このコードの変更は、`search-try-for-free.md` ファイル内で「AIサービス」に関する言及を更新するマイナーアップデートです。具体的には、「Applying AI services for creating AI-generated content during indexing」という行が「Applying Foundry Tools for creating AI-generated content during indexing」に変更されました。この変更は、より正確なツールの名称に基づいており、ユーザーが文書の内容を理解しやすくすることを目的としています。全体として、関連する情報の明確化が図られ、Pipelineの構成においてどのツールを使用するかの選択肢をユーザーに提供しています。変更されたファイルは、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/blob/cad893f3a0d8b7c30ebc5c6c3a0a139ea7d95fa2/articles%2Fsearch%2Fsearch-try-for-free.md)から参照できます。

## articles/search/tutorial-optimize-indexing-push-api.md{#item-ef0e96}

<details>
<summary>Diff</summary>
````diff
@@ -363,7 +363,7 @@ After the function finishes running, you can verify that all of the documents we
 
 After the program finishes running, you can explore the populated search index either programmatically or using the [Search explorer](search-explorer.md) in the Azure portal.
 
-### Programatically
+### Programmatically
 
 There are two main options for checking the number of documents in an index: the [Count Documents API](/rest/api/searchservice/documents/count) and the [Get Index Statistics API](/rest/api/searchservice/indexes/get-statistics). Both paths require time to process, so don't be alarmed if the number of documents returned is initially lower than you expect.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プログラム的にのスペル修正"
}
```

### Explanation
このコードの変更は、`tutorial-optimize-indexing-push-api.md` ファイルにおける「Programatically」という単語のスペルを修正するマイナーアップデートです。修正後の表記は「Programmatically」となっており、正しい英語表記に合わせています。この変更は、文書の正確性を高め、読み手に対する理解を深めることを目的としています。また、プログラムによる検索インデックスの検証方法に関する情報はそのまま維持されており、ユーザーがその後の手順をスムーズに進められるよう配慮されています。変更されたファイルは、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/blob/cad893f3a0d8b7c30ebc5c6c3a0a139ea7d95fa2/articles%2Fsearch%2Ftutorial-optimize-indexing-push-api.md)から参照できます。


