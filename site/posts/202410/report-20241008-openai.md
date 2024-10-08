---
date: '2024-10-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:43a3b87...MicrosoftDocs:e9690f5
summary: この変更は、OpenAIサービスに関するドキュメントの二つのセクションで小規模な更新を行ったものです。埋め込み機能に関しては最新の情報を反映し、Azure
  AI Searchを推奨システムとして明示しました。バッチ処理に関しては、用語を修正し、一貫性を持たせることでパフォーマンスの推奨を強化しました。新機能はありませんが、情報の更新によりユーザーは最新の技術や適切なソリューションへの理解を深めやすくなっています。破壊的な変更はなく、全体的に情報の信頼性と正確さを高めることを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:43a3b87...MicrosoftDocs:e9690f5){target="_blank"}

# ハイライト

この変更は、OpenAIサービスに関連するドキュメントの二つのセクションにおいて行われた小規模な更新です：

- **埋め込み機能と推奨システムの更新**：「埋め込み」技術への理解を補い、最新の日付を反映し、Azure AI Search を推奨されるシステムとして明示しました。
- **バッチ処理に関するパフォーマンス推奨の更新**：用語の修正を行い、バッチ処理に関するパフォーマンスの推奨の一貫性を強化しました。

## 新機能

特に新機能は含まれていませんが、埋め込み技術の使用例としてAzure AI Searchが明確に推奨されました。

## 破壊的変更

破壊的な変更は特にありません。

## その他の更新

- 埋め込み機能に関する説明の情報が新しい日付に更新され、情報の信頼性が高まりました。
- 「patch processing」という誤った用語を「batch processing」に修正し、一貫性を持たせました。

# 洞察

このドキュメントの更新は、情報の鮮度と正確さを高めることを目的としています。埋め込み機能に関する変更では、最新の日付を明記することでユーザーに対して現在の技術や推奨システムに関する最新情報を提供するようになっています。特に、Azure AI Searchが埋め込みリトリーバルシステムとして明確に推奨されることで、ユーザーが適切なソリューションを選択しやすくなります。

一方、バッチ処理に関するドキュメントの変更は、用語の不一致を解消し、ユーザーが効率的なバッチ処理の方法をより理解できるようにサポートしています。特に、パフォーマンス向上を目的としたファイルのサイズ管理についてのアドバイスは、ユーザーがより明確な指針に従う助けとなるでしょう。

このように、ドキュメントのアップデートは、技術的な理解と実践における明確さを向上させるものであり、ユーザーにとって価値のある情報提供を実現しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [understand-embeddings.md](#item-736ec2) | minor update | 埋め込み機能と推奨システムの更新 | modified | 2 | 2 | 4 | 
| [batch.md](#item-a131d5) | minor update | バッチ処理に関するパフォーマンス推奨の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/understand-embeddings.md{#item-736ec2}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ description: Learn more about how the Azure OpenAI embeddings API uses cosine si
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: tutorial
-ms.date: 09/05/2024
+ms.date: 10/6/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -15,7 +15,7 @@ ms.custom:
 
 # Understand embeddings in Azure OpenAI Service
 
-An embedding is a special format of data representation that machine learning models and algorithms can easily use. The embedding is an information dense representation of the semantic meaning of a piece of text. Each embedding is a vector of floating-point numbers, such that the distance between two embeddings in the vector space is correlated with semantic similarity between two inputs in the original format. For example, if two texts are similar, then their vector representations should also be similar. Embeddings power vector similarity search in Azure Databases such as [Azure Cosmos DB for MongoDB vCore](/azure/cosmos-db/mongodb/vcore/vector-search) ,  [Azure SQL Database](/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications?view=azuresql&preserve-view=true#vector-search) or [Azure Database for PostgreSQL - Flexible Server](/azure/postgresql/flexible-server/how-to-use-pgvector).
+An embedding is a special format of data representation that machine learning models and algorithms can easily use. The embedding is an information dense representation of the semantic meaning of a piece of text. Each embedding is a vector of floating-point numbers, such that the distance between two embeddings in the vector space is correlated with semantic similarity between two inputs in the original format. For example, if two texts are similar, then their vector representations should also be similar. Embeddings power vector similarity search in retrieval systems such as [Azure AI Search](/azure/search) (recommended) and in Azure databases such as [Azure Cosmos DB for MongoDB vCore](/azure/cosmos-db/mongodb/vcore/vector-search) ,  [Azure SQL Database](/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications?view=azuresql&preserve-view=true#vector-search), and [Azure Database for PostgreSQL - Flexible Server](/azure/postgresql/flexible-server/how-to-use-pgvector).
 
 ## Embedding models
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "埋め込み機能と推奨システムの更新"
}
```

### Explanation
この変更は、ドキュメント内の埋め込み機能に関連する説明を更新するものであり、主に二つのポイントで構成されています。まず、日付が「09/05/2024」から「10/6/2024」に変更され、文書の最新性が反映されています。次に、埋め込み技術が使用されるシステムの紹介が更新され、Azure AI Searchが推奨されるリトリーバルシステムとして明記されました。この変更により、ユーザーは最新の情報を得ることができ、埋め込みの使用例もより明確に理解できるようになります。

## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -85,7 +85,7 @@ In the Studio UI the deployment type will appear as `Global-Batch`.
 > [!TIP]
 > Each line of your input file for batch processing has a `model` attribute that requires a global batch **deployment name**. For a given input file, all names must be the same deployment name. This is different from OpenAI where the concept of model deployments does not exist. 
 >
-> For the best performance we recommend submitting large files for patch processing, rather than a large number of small files with only a few lines in each file.
+> For the best performance we recommend submitting large files for batch processing, rather than a large number of small files with only a few lines in each file.
 
 ::: zone pivot="programming-language-ai-studio"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理に関するパフォーマンス推奨の更新"
}
```

### Explanation
この変更は、バッチ処理に関するドキュメント内のパフォーマンス推奨を明確にするためのもので、一部の表現が修正されています。具体的には、「patch processing」という用語が「batch processing」に修正されています。この修正は、用語の一貫性を確保し、読者に正確な情報を提供することを目的としています。バッチ処理の推奨については、大きなファイルを提出することが推奨され、小さなファイルを多数送り込むことの非効率性が強調されています。これにより、ユーザーは最適なパフォーマンスを得るための方法をより明確に理解できるようになります。


