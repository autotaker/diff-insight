---
date: '2024-10-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:96dd444...MicrosoftDocs:bf31bc8
summary: 今回の変更では、主に新機能の追加と軽微な修正が行われました。特に注目すべきは、トラブルシューティングセクションが追加されたことで、ユーザーが適切な権限を設定するための明確なガイダンスを得られるようになった点です。大きな機能変更はないものの、リンクの修正やチュートリアルテキストの改善が行われ、ユーザーエクスペリエンスの向上が図られています。これにより、ユーザーは正確な情報へのアクセスが容易になり、文書の内容がより理解しやすくなっています。全体として、これらの更新はユーザーがサービスを最大限に活用するための基盤を強化しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:96dd444...MicrosoftDocs:bf31bc8){target="_blank"}

# Highlights

## New features
- `articles/ai-studio/concepts/rbac-ai-studio.md`: トラブルシューティングセクションが追加されました。これにより、特定のエラーメッセージに関する情報とその解決策が提供され、ユーザーは適切な権限を設定するための明確な指針を得ることができます。

## Breaking changes
- 特に大きな機能や仕様の根本的な変更はありません。

## Other updates
- `articles/ai-services/language-service/question-answering/tutorials/active-learning.md`: チュートリアルテキストの表現を改善し、内容の一貫性と可読性を向上させるための軽微な修正。
- `articles/ai-studio/concepts/encryption-keys-portal.md`: リンクの修正により、正確な情報へのアクセスが可能に。
- `articles/ai-studio/how-to/prompt-flow-tools/content-safety-tool.md` と `articles/ai-studio/how-to/prompt-flow-tools/serp-api-tool.md`: Azure AI Studioへのサインインリンクを修正し、ユーザーエクスペリエンスの向上を目指した軽微なアップデート。

# Insights

今回の変更では、軽微な修正から新機能の導入まで多岐にわたっています。特に目を引くのは、`rbac-ai-studio.md`ファイルへのトラブルシューティングセクションの追加です。この変更は、Azure AI Studioを利用する際の権限設定に関する困惑を緩和し、ユーザーが迅速に課題を解決できるようになるため、非常に有益です。エラーメッセージの具体的な原因と解決策を提示することは、日常のワークフローの効率化に寄与します。

その他の修正としては、リンクや表現の細かな改善が挙げられます。これらの変更はすべて、ユーザーエクスペリエンスを向上させることを目的としています。リンクの修正によって、ユーザーは正しい情報源に簡単にアクセスでき、業務を中断することなく進めることができます。また、文書の表現を改善することは、内容の正確さと信頼性を保つ上で重要な役割を果たします。

これらの更新により、ドキュメンテーションが最新の情報を提供し、ユーザーの利便性を向上させるものとなっています。特にトラブルシューティングセクションの追加は、今後のアップデートにおける新たな方向性を示唆しており、より包括的かつユーザーフレンドリーなドキュメント作成の一環と見受けられます。いずれも、ユーザーがサービスを最大限に活用するための基盤を強化するアップデートとなっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [active-learning.md](#item-e8486d) | minor update | チュートリアルのテキストの修正 | modified | 2 | 2 | 4 | 
| [encryption-keys-portal.md](#item-95428d) | minor update | リンクの修正 | modified | 1 | 1 | 2 | 
| [rbac-ai-studio.md](#item-c2a11a) | new feature | トラブルシューティングセクションの追加 | modified | 23 | 0 | 23 | 
| [content-safety-tool.md](#item-09b048) | minor update | Azure AI Studioのリンク修正 | modified | 1 | 1 | 2 | 
| [serp-api-tool.md](#item-144ed7) | minor update | Azure AI Studioのリンク修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/language-service/question-answering/tutorials/active-learning.md{#item-e8486d}

<details>
<summary>Diff</summary>
````diff
@@ -20,9 +20,9 @@ In this tutorial, you learn how to:
 > * Accept/reject active learning suggestions
 > * Add alternate questions
 
-This tutorial shows you how to enhance your custom question answering project with active learning. If you notice that customers are asking questions, which are not part of your project. There are often variations of questions that are paraphrased differently.
+This tutorial shows you how to enhance your custom question answering project with active learning. If you notice that customers are asking questions that are not covered in your project, they may be paraphrased variations of questions.
 
-These variations when added as alternate questions to the relevant question answer pair, help to optimize the project to answer real world user queries. You can manually add alternate questions to question answer pairs through the editor. At the same time, you can also use the active learning feature to generate active learning suggestions based on user queries. The active learning feature, however, requires that the project receives regular user traffic to generate suggestions.
+These variations, when added as alternate questions to the relevant question answer pair, help to optimize the project to answer real world user queries. You can manually add alternate questions to question answer pairs through the editor. At the same time, you can also use the active learning feature to generate active learning suggestions based on user queries. The active learning feature, however, requires that the project receives regular user traffic to generate suggestions.
 
 ## Use active learning
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルのテキストの修正"
}
```

### Explanation
このコードの変更は、`active-learning.md`ファイルの内容を軽微に更新したもので、特に文の表現を改善するための修正が行われました。具体的には、質問がプロジェクトに含まれていない場合に関する説明がより明確になり、言い回しが改良されています。これにより、読者がアクティブラーニングの提案についての理解を深めることができるようになります。全体として、内容の一貫性と可読性を高めるための微調整です。変更が行われた具体的な例として、表現を調整した部分がありますが、機能の追加や仕様に関する根本的な変更は含まれていません。

## articles/ai-studio/concepts/encryption-keys-portal.md{#item-95428d}

<details>
<summary>Diff</summary>
````diff
@@ -87,7 +87,7 @@ Customer-managed key encryption is configured via Azure portal in a similar way
 
 Alternatively, use infrastructure-as-code options for automation. Example Bicep templates for Azure AI Studio are available on the Azure Quickstart repo:
 1. [CMK encryption for hub](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aistudio-cmk).
-1. [Service-side CMK encryption preview for hub](https://github.com/azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-cmk-service-side-encryption).
+1. [Service-side CMK encryption preview for hub](https://github.com/azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aistudio-cmk-service-side-encryption).
 
 ## Limitations
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの修正"
}
```

### Explanation
このコードの変更は、`encryption-keys-portal.md`ファイル内のリンクを修正するための軽微なアップデートです。具体的には、サービスサイドの顧客管理キー（CMK）暗号化に関するリンクが更新され、新しいURLに変更されています。この変更により、読者は正確な情報にアクセスできるようになり、マニュアルの内容がより信頼性のあるものとなります。全体として、この修正は文書のメンテナンスの一環として行われており、機能や仕様に関する大きな変更はありません。

## articles/ai-studio/concepts/rbac-ai-studio.md{#item-c2a11a}

<details>
<summary>Diff</summary>
````diff
@@ -384,6 +384,29 @@ The following example defines a role for a developer using [Azure OpenAI Assista
 }
 ```
 
+## Troubleshooting
+
+### Error: Principal does not have access to API/Operation
+
+#### Symptoms
+
+When using the Azure AI Studio chat playground, you receive an error message stating "Principal does not have access to API/Operation". The error may also include an "Apim-request-id".
+
+#### Cause
+
+The user or service principal used to authenticate requests to Azure OpenAI or Azure AI Search does not have the required permissions to access the resource.
+
+#### Solution
+
+Assign the following roles to the user or service principal. The role you assign depends on the services you are using and the level of access the user or service principal requires:
+
+| Service being accessed | Role | Description |
+| --- | --- | --- |
+| Azure OpenAI | Cognitive Services OpenAI Contributor | Call public ingestion API from Azure AI Studio. |
+| Azure OpenAI | Cognitive Services User | List API-Keys from Azure AI Studio. |
+| Azure AI Search | Search Index Data Contributor | Required for indexing scenarios. |
+| Azure AI Search| Search Index Data Reader | Inference service queries the data from the index. Only used for inference scenarios. |
+
 ## Next steps
 
 - [How to create an Azure AI Studio hub](../how-to/create-azure-ai-resource.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "トラブルシューティングセクションの追加"
}
```

### Explanation
このコードの変更は、`rbac-ai-studio.md`ファイルにトラブルシューティングのセクションを新たに追加したものです。このセクションでは、「Principal does not have access to API/Operation」というエラーメッセージに関する情報が提供されています。具体的には、エラーの症状、原因、および解決策が詳述されています。

解決策には、ユーザーまたはサービスプリンシパルに必要な役割を割り当てることが提案され、Azure OpenAIおよびAzure AI Searchに関連するさまざまな役割とその説明が表形式で示されています。これにより、ユーザーは適切な権限を設定するための明確な指針を得ることができ、エラーの解決に役立てることができます。この変更は、Azure AI Studioの利用者にとって重要な情報源を提供するものであり、利用者のエクスペリエンスを向上させるための新しい機能です。

## articles/ai-studio/how-to/prompt-flow-tools/content-safety-tool.md{#item-09b048}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ Azure AI Content Safety is a content moderation service that helps detect harmfu
 
 To create an Azure Content Safety connection:
 
-1. Sign in to [Azure AI Studio](https://ai.azure.com/).
+1. Sign in to [Azure AI Studio](https://ml.azure.com/).
 1. Go to **Project settings** > **Connections**.
 1. Select **+ New connection**.
 1. Complete all steps in the **Create a new connection** dialog. You can use an Azure AI Studio hub or Azure AI Content Safety resource. We recommend that you use a hub that supports multiple Azure AI services.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのリンク修正"
}
```

### Explanation
このコードの変更は、`content-safety-tool.md`ファイルにおいて、Azure AI Studioへのサインインリンクを修正するための軽微なアップデートです。具体的には、元のリンクが `https://ai.azure.com/` から `https://ml.azure.com/` に変更されています。この修正により、ユーザーは最新の正しいURLを通じてAzure AI Studioにアクセスできるようになり、コンテンツの安全性ツールを使用する際によりスムーズな体験が得られます。これは文書の信頼性を向上させる重要な調整であり、ユーザーエクスペリエンスの向上に寄与するものであります。

## articles/ai-studio/how-to/prompt-flow-tools/serp-api-tool.md{#item-144ed7}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ Sign up on the [Serp API home page](https://serpapi.com/).
 
 To create a Serp connection:
 
-1. Sign in to [Azure AI Studio](https://ai.azure.com/).
+1. Sign in to [Azure AI Studio](https://ml.azure.com/).
 1. Go to **Project settings** > **Connections**.
 1. Select **+ New connection**.
 1. Add the following custom keys to the connection:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのリンク修正"
}
```

### Explanation
このコードの変更は、`serp-api-tool.md`ファイルにおけるAzure AI Studioへのサインインリンクを修正するための軽微なアップデートです。具体的には、元のリンクが `https://ai.azure.com/` から新しいリンク `https://ml.azure.com/` に変更されています。このリンクの修正により、ユーザーは正しいURLを使用してAzure AI Studioにアクセスでき、Serp APIツールを利用する際の使い勝手が向上します。この変更はドキュメントの正確性を確保し、ユーザーが適切なリソースにアクセスできるようにするために重要です。


