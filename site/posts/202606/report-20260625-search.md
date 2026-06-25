---
date: '2026-06-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7d98215...MicrosoftDocs:8ac646c
summary: この記事の更新では、Azure AI Searchの知識ベース作成に重要な新手順が追加され、「ロールベースのアクセス制御を有効にする」機能が導入されました。これにより、ユーザーはアクセス権限を詳細に管理できるようになり、セキュリティが強化されます。また、C#、Python、RESTの各プラットフォームに新しい手順も追加されています。この更新は、Azure
  AI Searchのユーザビリティを向上させると同時に、セキュリティ面でも管理が容易になることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7d98215...MicrosoftDocs:8ac646c){target="_blank"}

# Highlights
この記事の更新では、Azure AI Searchの知識ベースを作成する際に重要な新しい手順が追加されました。この新しい手順は、「ロールベースのアクセス制御を有効にする」機能を指しています。この追加により、Azure AI Searchのセキュリティ管理が強化されます。

## 新機能
- Azure AI Searchの知識ベース作成において、「ロールベースのアクセス制御を有効にする」手順が追加されました。これにより、ユーザーはアクセス権限をより細かく管理できるようになりました。

## 互換性を破る変更
- なし

## その他の更新
- C#、Python、およびRESTの各プラットフォーム用の手順に新しいステップが追加されました。

# Insights
この更新は、Azure AI Searchの知識ベース管理においてセキュリティを重視した内容と言えます。ロールベースのアクセス制御は、業務において重要なデータや機能へのアクセスを制限するための一般的な手法であり、多くのエンタープライズ環境で利用されています。今回の文書の更新は、Azure AI Searchのユーザビリティを向上させると同時に、セキュリティ面での管理がしやすくなることを意図しています。具体的なプログラミング言語（C#、Python、REST）のセクション毎にこの重要なステップが追加されていることは、対象を使い慣れた開発者にとっても有用な情報となるでしょう。セキュリティ強化が求められる現代において、このような更新は今後ますます重要になっていくと考えられます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-knowledge-base.md](#item-7df0e2) | minor update | 知識ベースの作成方法に関する更新 | modified | 6 | 0 | 6 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-knowledge-base.md{#item-7df0e2}

<details>
<summary>Diff</summary>
````diff
@@ -109,6 +109,8 @@ Azure AI Search needs access to the LLM from Azure OpenAI in Foundry Models. We
 
 ::: zone pivot="csharp"
 
+1. [Enable role-based access control on Azure AI Search](search-security-enable-roles.md).
+
 1. [Configure Azure AI Search to use a managed identity](search-how-to-managed-identities.md).
 
 1. On your model provider, assign **Cognitive Services User** to the managed identity of your search service. If you're testing locally, assign the same role to your user account.
@@ -127,6 +129,8 @@ Azure AI Search needs access to the LLM from Azure OpenAI in Foundry Models. We
 
 ::: zone pivot="python"
 
+1. [Enable role-based access control on Azure AI Search](search-security-enable-roles.md).
+
 1. [Configure Azure AI Search to use a managed identity](search-how-to-managed-identities.md).
 
 1. On your model provider, assign **Cognitive Services User** to the managed identity of your search service. If you're testing locally, assign the same role to your user account.
@@ -143,6 +147,8 @@ Azure AI Search needs access to the LLM from Azure OpenAI in Foundry Models. We
 
 ::: zone pivot="rest"
 
+1. [Enable role-based access control on Azure AI Search](search-security-enable-roles.md).
+
 1. [Configure Azure AI Search to use a managed identity](search-how-to-managed-identities.md).
 
 1. On your model provider, assign **Cognitive Services User** to the managed identity of your search service. If you're testing locally, assign the same role to your user account.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ベースの作成方法に関する更新"
}
```

### Explanation
この変更は、Azure AI Searchの知識ベースを作成する方法に関する文書の更新です。具体的には、ロールベースのアクセス制御を有効にする手順を追加しました。変更は、C#、Python、およびRESTの各プラットフォームに適用され、各セクションの手順に「Azure AI Searchでのロールベースのアクセス制御を有効にする」という新しいステップが挿入されています。これにより、ユーザーはAzure AI Searchが適切に管理され、セキュリティが強化されることが強調されています。全体で6行の変更がありましたが、削除された内容はありません。


