---
date: '2024-12-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f98b838...MicrosoftDocs:dfca068
summary: この変更は、`cognitive-search-output-field-mapping.md`ドキュメントにおける説明文を更新するもので、特に「AOAI」という表現がより具体的な「Azure
  OpenAI Service」に変更されました。この更新は、Azure OpenAI Serviceに関する情報の明確化を目的としており、技術的な具体性が追加されています。互換性に影響を与える大きな変更はなく、一部の用語選択も調整されています。この変更は軽微ですが、正確な表現は技術ドキュメントの信頼性を維持し、読者が関連情報を検索する助けとなります。今後もこのような用語の見直しが継続されることが重要です。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f98b838...MicrosoftDocs:dfca068){target="_blank"}

# ハイライト
この変更は、`cognitive-search-output-field-mapping.md`ドキュメントにおける説明文の更新です。特に、"AOAI"と表現されていた部分が、より具体的で正確な"Azure OpenAI Service"に更新されました。この更新は、読者に対してAzure OpenAI Serviceに関する情報を明確に提供することを目的としており、新しい情報の追加や既存の情報の削除を伴います。

## 新機能
- Azure OpenAI Serviceの説明が明確化され、技術的に具体性が追加されました。

## 互換性に影響する変更
- 現時点では、特に互換性に直接的に影響を与える大きな変更はありません。

## その他の更新
- 一部の単語選択についての調整が行われ、ドキュメントの整合性を高めています。

# 洞察
この変更は単に用語を更新するだけの軽微なものでありますが、それが持つ重要性は無視できません。特に、Azure OpenAI Serviceは現在多くの技術者が注目しているテクノロジーです。このため、正確なサービス名を用いることは、技術ドキュメントの信頼性を維持する上で重要です。読者がサービスの特定や関連情報を検索する際に、正確な名前表記は誤解を避け、関連知識の向上に寄与します。また、技術系文章において正確さは、信頼性を確保するための基本とも言えます。今後もこのような用語の見直しは継続して行われるべきでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-output-field-mapping.md](#item-31fe9c) | minor update | Azure OpenAI Serviceの説明更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/cognitive-search-output-field-mapping.md{#item-31fe9c}

<details>
<summary>Diff</summary>
````diff
@@ -182,7 +182,7 @@ The source field path is skill output. In this example, the output is *text_vect
 ```json
 {
   "name": "test-vector-size-ss",  
-  "description": "Generate embeddings using AOAI",
+  "description": "Generate embeddings using Azure OpenAI Service",
   "skills": [
     {
       "@odata.type": "#Microsoft.Skills.Text.AzureOpenAIEmbeddingSkill",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI Serviceの説明更新"
}
```

### Explanation
この変更は、`cognitive-search-output-field-mapping.md`ファイルにおける単語の修正を含んでいます。具体的には、"Generate embeddings using AOAI" という説明が "Generate embeddings using Azure OpenAI Service" に更新されました。この修正は、Azure OpenAI Serviceについての説明を明確にし、読者に正確な情報を提供することを目的としています。ファイルの変更は、1行の追加と1行の削除を伴い、全体としては形式上の意味合いを持つ軽微な更新です。この修正により、文書の整合性が高まり、サービス名が明示的に表記されるようになっています。


