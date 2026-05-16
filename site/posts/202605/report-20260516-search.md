---
date: '2026-05-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ca3a955...MicrosoftDocs:6fafdc8
summary: この変更では、いくつかの文書における役割名が更新され、「Azure AI User」と「Azure AI Project Manager」がそれぞれ「Foundry
  User」と「Foundry Project Manager」に変更されました。この変更は、ユーザーが正確な役割名を基に作業を進められるようにすることを目的とし、関連する補足情報も追加されています。破壊的な変更はなく、すべての関連文書が新しい役割名に基づいて調整されています。この一連の更新は、Foundryプラットフォームにおける役割管理の明確化と統一を図り、ユーザーの混乱を避けつつ、操作性を向上させることを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ca3a955...MicrosoftDocs:6fafdc8){target="_blank"}

<format>
# Highlights
この変更では、いくつかの文書における役割名が更新されました。具体的には、「Azure AI User」と「Azure AI Project Manager」が「Foundry User」と「Foundry Project Manager」に変更され、これにより役割に関する指示や補足情報が更新されています。これらの変更は、文書を最新の情報に保ち、ユーザーが正確な役割名を基に作業を進められるようにすることを目的としています。

## New features
該当する新機能はありませんが、役割名の更新に伴い、関連する補足情報が追加されています。

## Breaking changes
破壊的な変更は含まれていません。すべての変更は情報の更新であり、システムの動作には影響を及ぼしません。

## Other updates
すべての関連文書が新しい役割名に基づいて一致するように調整されています。

# Insights
この一連の文書更新は、Microsoftが提供するFoundryプラットフォームにおける役割管理の明確化と統一を意図したものです。特に「Azure AI User」や「Azure AI Project Manager」といった旧役割が、「Foundry User」や「Foundry Project Manager」と置き換えられています。この変更は、ユーザーが様々なプロジェクトやデプロイメントで適切な役割を選択しやすくするための努力の一環と見ることができます。

役割名が変わることで、技術文書もこれに即応する形で更新されており、文書の一貫性と正確性が確保されています。この種の更新は、ユーザーにとっての混乱を避け、操作性の向上と学習曲線の緩和を目指しています。補足情報が追加されたことで、ユーザーは新しい役割名についてより深く理解することができ、Microsoftのサービスを効果的に利用する助けとなります。

役割名の変更は、組織内での役割分担やアクセス権管理の見直しを示唆するものであり、この変化に伴い必要な調整を行うことで、ユーザーは最新の状態を維持しつつ業務を続行することができます。これにより、よりスムーズで効率的なプロジェクト運営が可能となります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | エージェント検索パイプラインの設定に関する文書更新 | modified | 4 | 2 | 6 | 
| [cognitive-search-skill-genai-prompt.md](#item-384bf9) | minor update | GenAI Promptスキルに関する文書の役割名の更新 | modified | 3 | 1 | 4 | 
| [resource-authentication-identity.md](#item-bcdb0d) | minor update | リソース認証アイデンティティに関する文書の役割名の更新 | modified | 3 | 1 | 4 | 
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | 画像検索の開始に関する文書の役割名の更新 | modified | 3 | 1 | 4 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | ベクトルインポートの開始に関する文書の役割名の更新 | modified | 3 | 1 | 4 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -82,10 +82,12 @@ To configure access for this solution:
 
     | Role | Assignee | Purpose |
     |------|----------|---------|
-    | Azure AI User | Your user account | Access model deployments and create agents |
-    | Azure AI Project Manager | Your user account | Create project connection and use MCP tool in agents |
+    | Foundry User | Your user account | Access model deployments and create agents |
+    | Foundry Project Manager | Your user account | Create project connection and use MCP tool in agents |
     | Cognitive Services User | Search service managed identity | Access knowledge base |
 
+[!INCLUDE [role-rename-note](../foundry/includes/role-rename-note.md)]
+
 ## Set up your environment
 
 1. Create a folder named `tutorial-agentic-retrieval` on your local system.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索パイプラインの設定に関する文書更新"
}
```

### Explanation
この変更は、文書「エージェント検索パイプラインの作成方法」における役割の名称を更新するためのマイナーな修正です。具体的には、以下の点が改訂されました：

- 役割「Azure AI User」と「Azure AI Project Manager」が「Foundry User」と「Foundry Project Manager」にそれぞれ変更されました。これにより、ユーザーがアクセスできるモードのデプロイメントやエージェントの作成、プロジェクト接続の作成、およびMCPツールの使用に関するガイダンスが最新の情報に基づいて更新されました。
- さらに、役割名称の変更に関する補足情報が含まれるようになりました（[!INCLUDE [role-rename-note](../foundry/includes/role-rename-note.md)]）。

全体として、これらの変更は、ユーザーが必要な役割をより明確に理解できるようにし、文書の一貫性を保持します。

## articles/search/cognitive-search-skill-genai-prompt.md{#item-384bf9}

<details>
<summary>Diff</summary>
````diff
@@ -53,7 +53,9 @@ The GenAI Prompt skill is generally available in the [2026-04-01 Search Service
 
   - On Azure OpenAI, assign [**Cognitive Services OpenAI User**](/azure/ai-services/openai/how-to/role-based-access-control) to the managed identity.
 
-  - On Foundry, assign [**Azure AI User**](../ai-foundry/concepts/rbac-foundry.md#built-in-roles) to the managed identity.
+  - On Foundry, assign [**Foundry User**](../ai-foundry/concepts/rbac-foundry.md#built-in-roles) to the managed identity.
+
+    [!INCLUDE [role-rename-note](../foundry/includes/role-rename-note.md)]
 
 ## @odata.type  
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GenAI Promptスキルに関する文書の役割名の更新"
}
```

### Explanation
この変更は、「GenAI Promptスキル」に関する文書の一部を更新するためのマイナーな修正です。主要な変更点は以下の通りです：

- Foundryにおける役割の名称が「Azure AI User」から「Foundry User」に変更されました。この更新により、ユーザーがFoundryの管理対象IDに割り当てるべき正しい役割が反映されました。
- また、役割名称の変更に関連する補足情報が追加され（[!INCLUDE [role-rename-note](../foundry/includes/role-rename-note.md)]）、ユーザーは新しい役割名に関する重要な情報を得られるようになっています。

これらの修正は、文書の正確さと一貫性を保ち、ユーザーが正しい情報に基づいて作業できるようにするためのものです。

## articles/search/includes/resource-authentication-identity.md{#item-bcdb0d}

<details>
<summary>Diff</summary>
````diff
@@ -20,6 +20,8 @@ To configure the recommended role-based access:
     | GPT-4/5 & text-embedding-3 | Cognitive Services OpenAI User | Azure OpenAI Resource |
     | Azure AI Vision multimodal 4.0 | Cognitive Services User | Azure AI Multi-service Resource |
     | Content Understanding  | Cognitive Services User | Microsoft Foundry Resource |
-    | Foundry Model Orchestration | Azure AI User | Foundry Project |
+    | Foundry Model Orchestration | Foundry User | Foundry Project |
+
+[!INCLUDE [role-rename-note](../../foundry/includes/role-rename-note.md)]
 
 1. Choose **Managed identity** and then assign your [search service managed identity](search-how-to-managed-identities.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソース認証アイデンティティに関する文書の役割名の更新"
}
```

### Explanation
この変更は、「リソース認証アイデンティティ」に関する文書の役割名を更新するためのマイナーな修正です。以下が主な変更点です：

- 役割「Azure AI User」が「Foundry User」に変更されました。これにより、Foundryモデルオーケストレーションに関する情報が最新の役割名に基づいて更新されています。
- また、役割名称の変更についての補足情報が追加され（[!INCLUDE [role-rename-note](../../foundry/includes/role-rename-note.md)]）、ユーザーが新しい役割名に関する重要な情報を得られます。

この修正は、利用者が正確な役割情報を基にアクションを実行できるようにするために、文書の正確さと一貫性を確保することを目的としています。

## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -132,7 +132,9 @@ The Microsoft Foundry model catalog provides LLMs for image verbalization and em
 
 On the parent resource of your Microsoft Foundry project:
 
-+ Assign **Azure AI Project Manager** to the managed identity of your search service.
++ Assign **Foundry Project Manager** to the managed identity of your search service.
+
+  [!INCLUDE [role-rename-note](../foundry/includes/role-rename-note.md)]
 
 ### [**Azure OpenAI**](#tab/openai)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像検索の開始に関する文書の役割名の更新"
}
```

### Explanation
この変更は、「画像検索の開始」に関する文書における役割名を更新するためのマイナーな修正です。主な変更点は以下の通りです：

- 役割「Azure AI Project Manager」が「Foundry Project Manager」に変更されました。これは、Microsoft Foundryプロジェクトに関連する管理対象IDの設定において、正確な役割名を反映するための更新です。
- また、役割名称の変更に関する補足情報が追加され（[!INCLUDE [role-rename-note](../foundry/includes/role-rename-note.md)]）、ユーザーが新しい役割名に関して重要な情報を得られるようになっています。

この修正は、ユーザーが正確な情報に基づいて設定を行い、プロジェクトを円滑に進められるようにすることを目的としています。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -134,7 +134,9 @@ The Microsoft Foundry model catalog provides embedding models for text vectoriza
 
 On the parent resource of your Microsoft Foundry project:
 
-+ Assign **Azure AI Project Manager** to the managed identity of your search service.
++ Assign **Foundry Project Manager** to the managed identity of your search service.
+
+  [!INCLUDE [role-rename-note](../foundry/includes/role-rename-note.md)]
 
 ### [**Azure AI multi-service**](#tab/vision-access)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルインポートの開始に関する文書の役割名の更新"
}
```

### Explanation
この変更は、「ベクトルインポートの開始」に関する文書で使用されている役割名を更新するためのマイナーな修正です。具体的には、次の変更が行われています：

- 役割「Azure AI Project Manager」が「Foundry Project Manager」に変更されました。この変更は、Microsoft Foundryプロジェクトの管理対象IDに関連する設定が、最新の役割に基づいて行われるようにするためです。
- また、役割の名称変更に関する補足情報が文書に追加され（[!INCLUDE [role-rename-note](../foundry/includes/role-rename-note.md)]）、ユーザーが新しい役割名に関する必要な情報を取得できるようになっています。

この修正は、文書を最新の状態に保ち、ユーザーが適切な役割に基づいて設定を行うことができるようにすることを目的としています。


