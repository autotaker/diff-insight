---
date: '2026-02-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e20ff5a...MicrosoftDocs:8ae7459
summary: 今回の更新では、Azure AI SearchとCognitive Searchにおいて、主にセキュリティの強化と利便性の向上が図られました。エージェント的検索の認証方法が従来のAPIキーからより安全なBearerトークン形式へ変更され、これにより機密情報の管理が容易になります。また、GenAIプロンプトスキルの設定が複数のプロパティからJSON形式の一元化された文字列へと変更され、開発者にとっての理解と実装のしやすさが向上しました。これらの変更によって、Azureの検索ソリューションは信頼性と使いやすさが向上しました。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e20ff5a...MicrosoftDocs:8ae7459){target="_blank"}

# Highlights

## 新機能

- `エージェント的検索の認証方法`: Azure AI Searchにおける認証方法が、`api-key` からより安全なBearerトークン形式へと変更。これには「Search Index Data Reader」ロールが必要。
  
- `GenAIプロンプトスキルの定義`: Azure Cognitive Searchでのスキル定義が、個別のプロパティからJSON形式の文字列に一元化されたことで、読みやすく扱いやすくなった。

## 破壊的変更

- なし

## その他の更新

- `ms.date` の更新: 文書の日付が2025年10月23日から2026年2月12日に変更された。

# Insights

Azure AI SearchとCognitive Searchの機能における今回の更新は、特にセキュリティの強化と利便性の向上に重点を置いています。エージェント的検索の認証方法の変更では、Bearerトークンを採用することで、セキュリティが重要視されています。APIキーの管理はしばしばセキュリティの弱点となることが多いため、トークンベースの認証はより安全な方法と言えます。この変更により、アプリケーションの認証のために設定ファイルなどに機密情報を保存する必要がなくなる利点があります。

一方で、GenAIプロンプトスキルの更新は、スキルのプロパティをJSON形式で記述することで、開発者にとっての理解と実装のしやすさが向上しています。JSON形式による一元的なプロパティ定義は、設定の一貫性を保ち、後からの情報取得や確認が容易になります。これにより、スキルの拡張や管理が直感的に行えるようになるため、開発者にとっての生産性が高まり、エラーハンドリングも簡素化される可能性があります。

これらの更新により、Azureの検索ソリューションはセキュリティ面での信頼性が向上しつつ、開発者の操作性や使いやすさも同時に改善されました。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-retrieve.md](#item-d739cf) | minor update | エージェント的検索の認証方法を更新 | modified | 2 | 2 | 4 | 
| [cognitive-search-skill-genai-prompt.md](#item-384bf9) | minor update | GenAIプロンプトスキルの定義を更新 | modified | 2 | 14 | 16 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-retrieve.md{#item-d739cf}

<details>
<summary>Diff</summary>
````diff
@@ -106,9 +106,9 @@ https://<your-service-name>.search.windows.net/knowledgebases/<your-knowledge-ba
 
 The MCP endpoint requires authentication via custom headers. You have two options:
 
-+ Pass a query key (recommended) or an admin key in the `api-key` header. The key grants read-only access, so no role assignment is needed. For more information, see [Connect to Azure AI Search using API keys](search-security-api-keys.md).
++ **(Recommended)** Pass a bearer token in the `Authorization` header. The identity behind the token must have the **Search Index Data Reader** role assigned on the search service. This approach avoids storing keys in configuration files. For more information, see [Connect your app to Azure AI Search using identities](search-security-rbac-client-code.md).
 
-+ (Recommended) Pass a bearer token in the `Authorization` header. The identity behind the token must have the **Search Index Data Reader** role assigned on the search service. This approach avoids storing keys in configuration files. For more information, see [Connect your app to Azure AI Search using identities](search-security-rbac-client-code.md).
++ Pass a query key or an admin key in the `api-key` header. We recommend a query key for read-only access, which is sufficient for retrieval and the safer choice. An admin key provides full read-write access to the search service. For more information, see [Connect to Azure AI Search using API keys](search-security-api-keys.md).
 
 > [!TIP]
 > Each MCP client configures custom headers differently. For example:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント的検索の認証方法を更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchのエージェント的検索における認証方法に関する説明を更新したものです。具体的には、`api-key` ヘッダーを使用してクエリキーや管理者キーを渡す方法から、Bearerトークンを使用する方法に推奨事項を変更しました。新しい説明では、トークンを使用することが推奨されており、トークンの背後にあるアイデンティティには「Search Index Data Reader」ロールが必要であることが明示されています。また、Bearトークンを使うことで設定ファイルにキーを保管する必要がなくなる利点が強調されています。

この変更により、より安全で効率的な認証方法を選択するためのガイダンスが更新され、APIキーの使用に関する情報も整理されています。全体的には、セキュリティを強化し、開発者がAzure AI Searchを利用する際のガイドラインを改善する内容です。

## articles/search/cognitive-search-skill-genai-prompt.md{#item-384bf9}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2025
 ms.topic: reference
-ms.date: 10/23/2025
+ms.date: 02/12/2026
 ---
 
 # GenAI Prompt skill
@@ -183,19 +183,7 @@ The GenAI Prompt skill is available in the [latest preview REST API](/rest/api/s
       "strict": true,
       "schema": {
         "type": "object",
-        "properties": {
-          "facts": {
-            "type": "array",
-            "items": {
-              "type": "object",
-              "properties": {
-                "number": { "type": "number" },
-                "fact": { "type": "string" }
-              },
-              "required": [ "number", "fact" ]
-            }
-          }
-        },
+        "properties": "{\"facts\":{\"type\":\"array\",\"items\":{\"type\":\"object\",\"properties\":{\"number\":{\"type\":\"number\"},\"fact\":{\"type\":\"string\"}},\"required\":[\"number\",\"fact\"]}}}",
         "required": [ "facts" ],
         "additionalProperties": false
       }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GenAIプロンプトスキルの定義を更新"
}
```

### Explanation
このコードの変更は、Azure Cognitive SearchのGenAIプロンプトスキルに関する文書の修正を含みます。主に、スキルのメタデータの更新や、`ms.date` が2025年10月23日から2026年2月12日に変更されています。また、スキルのプロパティの定義方法にも変更があり、従来の個別のプロパティ定義から、JSON形式の文字列でまとめた形式へと整理されています。

具体的には、以前は各プロパティ（`facts`、`number`、`fact`）が個別に定義されていましたが、変更後は全体のスキーマが一つの文字列として記述され、読みやすさや扱いやすさが向上しています。この変更により、スキルの使用方法や構造が明確になり、開発者がGenAIプロンプトスキルを実装する際の理解が促進されます。


