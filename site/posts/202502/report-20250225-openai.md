---
date: '2025-02-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8c6e364...MicrosoftDocs:50dc684
summary: この更新では、複数のドキュメントに対して軽微な修正が行われ、新しい情報の追加、文言の強調、日付の更新が含まれています。大きな破壊的変更はないものの、文書の正確性とユーザー理解を向上させる改良が進められています。また、ストレージ完了機能に関する新セクションの追加やAPI使用時の明確化が行われています。この変更により、開発者がより効率的にプロジェクトを進められるようになり、Azure
  OpenAIサービスの利用が改善されることが期待されます。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8c6e364...MicrosoftDocs:50dc684){target="_blank"}

# ハイライト
このコードの差分では、複数のドキュメントに対する軽微な修正が行われました。主要な新機能としては、新しい情報の追加、文言の強調、日付の更新などがあります。大規模な破壊的変更はありませんが、ドキュメントの正確性とユーザーの理解を向上させるための改善が行われています。

## 新機能
- ストレージ完了機能に関する新しいセクションの追加。
- `purpose` パラメーターの文言強調によるAPI使用の明確化。
- メトリクスに関する最新情報への注意喚起。

## 破壊的変更
特に大きな破壊的変更はありません。

## その他の更新
- 日付情報の最新化。
- JavaのSDK関連コードの小さな修正。
- Azure OpenAI役割ベースのアクセス制御に関する説明の明確化。

# インサイト
この更新において、複数の技術文書が改善され、ユーザーに対する情報提供が強化されました。特に、明確な文言への修正や強調は、APIやSDKの利用時の誤解を減らし、開発者が効率的にプロジェクトを進められるようにサポートします。ストレージ完了機能への新情報の追加は、ユーザーへの機能の可用性の最新情報を提供し、意思決定を助ける役割を果たします。

また、メトリクス関連ドキュメントの更新は従量課金型（スタンダード）デプロイメントで使用できるメトリクスの制限を認識させ、監視やデプロイメント時のトラブルを未然に防ぐための重要なガイドとなります。Java SDKに関するコード修正は、見落としがちなコード内の小さなミスを排除し、コードの保守性と可読性を向上させます。

これらの変更は、継続的なドキュメンテーション改善の一環として、開発者および管理者がより正確で信頼できる情報に基づいて、Azure OpenAIサービスを活用できるようにするための積極的な取り組みを示しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [assistant.md](#item-b12c67) | minor update | ファイルアップロードエンドポイントに関する文言の修正 | modified | 1 | 1 | 2 | 
| [role-based-access-control.md](#item-4b9817) | minor update | Azure OpenAIに関する役割ベースのアクセス制御の更新 | modified | 5 | 5 | 10 | 
| [stored-completions.md](#item-ccc7e6) | minor update | ストレージ完了に関する情報の追加と日付の更新 | modified | 5 | 1 | 6 | 
| [java.md](#item-827a02) | minor update | Java SDKの環境変数取得方法の修正 | modified | 2 | 2 | 4 | 
| [monitor-openai-reference.md](#item-8d8887) | minor update | Azure OpenAIメトリクスに関する情報更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/openai/how-to/assistant.md{#item-b12c67}

<details>
<summary>Diff</summary>
````diff
@@ -67,7 +67,7 @@ An individual assistant can access up to 128 tools including [code interpreter](
 
 ### Files
 
-Files can be uploaded via Studio, or programmatically. The `file_ids` parameter is required to give tools like `code_interpreter` access to files. When using the File upload endpoint, you must have the `purpose` set to assistants to be used with the Assistants API.
+Files can be uploaded via Studio, or programmatically. The `file_ids` parameter is required to give tools like `code_interpreter` access to files. When using the File upload endpoint, you must have the `purpose` set to `assistants` to be used with the Assistants API.
 
 ## Assistants playground
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイルアップロードエンドポイントに関する文言の修正"
}
```

### Explanation
この変更は、ドキュメント内のファイルアップロードに関するパラメーターの説明に対する軽微な修正です。具体的には、`purpose` パラメーターの値が「assistants」となっている箇所を強調するため、バッククォートを使用して修正しました。この文言の変更は、ドキュメントの正確性を向上させ、APIの使用に関する明確な指示を提供するために行われました。変更内容は、明確に理解できるようになり、開発者が正しくこの機能を利用できるようサポートします。

## articles/ai-services/openai/how-to/role-based-access-control.md{#item-4b9817}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: mrbullwinkle
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 08/29/2024
+ms.date: 02/24/2025
 ms.author: mbullwin
 recommendations: false
 ---
@@ -74,15 +74,16 @@ This role has all the permissions of Cognitive Services OpenAI User and is also
 ✅ Create custom fine-tuned models <br>
 ✅ Upload datasets for fine-tuning <br>
 ✅ View, query, filter Stored completions data <br>
-✅ Create new model deployments or edit existing model deployments **[Added Fall 2023]**
+✅ Create new model deployments or edit existing model deployments **[Added Fall 2023]** <br>
+✅ Add data sources to Azure OpenAI On Your Data. **You must also have the [Cognitive Services Contributor](#cognitive-services-contributor) role as well**.
 
 A user with only this role assigned would be unable to:
 
 ❌ Create new Azure OpenAI resources <br>
 ❌ View/Copy/Regenerate keys under **Keys and Endpoint** <br>
 ❌ Access quota <br>
 ❌ Create customized content filters <br>
-❌ Add a data source for the use your data feature
+❌ Add a data source for Azure OpenAI On Your Data
 
 ### Cognitive Services Contributor
 
@@ -95,14 +96,13 @@ This role is typically granted access at the resource group level for a user in
 ✅ Ability to view what models are available for deployment in Azure AI Foundry portal <br>
 ✅ Use the Chat, Completions, and DALL-E (preview) playground experiences to generate text and images with any models that have already been deployed to this Azure OpenAI resource <br>
 ✅ Create customized content filters <br>
-✅ Add a data source for the use your data feature <br>
+✅ Add data sources to Azure OpenAI On Your Data. **You must also have the [Cognitive Services OpenAI Contributor](#cognitive-services-openai-contributor) role as well**.
 ✅ Create new model deployments or edit existing model deployments (via API) <br>
 ✅ Create custom fine-tuned models **[Added Fall 2023]**<br>
 ✅ Upload datasets for fine-tuning **[Added Fall 2023]**<br>
 ✅ Create new model deployments or edit existing model deployments (via Azure AI Foundry) **[Added Fall 2023]**<br>
 ✅ View, query, filter Stored completions data <br>
 
-
 A user with only this role assigned would be unable to:
 
 ❌ Access quota <br>
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIに関する役割ベースのアクセス制御の更新"
}
```

### Explanation
この変更は、Azure OpenAIにおける役割ベースのアクセス制御に関するドキュメントの内容を更新したものです。特に、2つの主要な役割に関連する機能の説明を明確化し、一部の文言をより正確にしました。具体的には、新しいデータソースの追加に関する条件や、役割の権限に関する詳細が強調されています。また、日付の変更（08/29/2024から02/24/2025）も反映されています。このアップデートは、利用者が役割に基づく機能を正確に理解する助けになるよう意図されています。全体として、ユーザーが役割に適したアクセス権を理解し、正確な情報に基づいてシステムを使用できるように改善されています。

## articles/ai-services/openai/how-to/stored-completions.md{#item-ccc7e6}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
 ms.custom: references_regions
-ms.date: 01/29/2025
+ms.date: 02/24/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -22,6 +22,10 @@ Stored completions allow you to capture the conversation history from chat compl
 
 Support first added in `2024-10-01-preview`
 
+### Deployment type
+
+Currently only `Standard` model deployments support stored completions.
+
 ### Model & region availability
 
 | **Region**     | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-05-13**  | **gpt-4o-mini**, **2024-07-18**   |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ストレージ完了に関する情報の追加と日付の更新"
}
```

### Explanation
この変更は、ストレージされた完了に関するドキュメントの内容を更新したもので、いくつかの新しい情報の追加と日付の更新が含まれています。具体的には、「現在、`Standard` モデルのデプロイメントのみがストレージ完了をサポートします」という新しいセクションが追加され、ストレージ機能の対応状況を明確にしています。また、文書の日付が「01/29/2025」から「02/24/2025」に更新されています。これにより、ユーザーは対応する機能やモデルの可用性について最新の情報を得ることができ、より良い理解を促進することが狙いです。全体として、この更新はストレージ完了機能に関連する情報を強化し、ユーザーにとっての有用性を高めています。

## articles/ai-services/openai/includes/java.md{#item-827a02}

<details>
<summary>Diff</summary>
````diff
@@ -103,8 +103,8 @@ dependencies {
     public class GetCompletionsSample {
     
         public static void main(String[] args) {
-            String azureOpenaiKey = System.getenv("AZURE_OPENAI_API_KEY");;
-            String endpoint = System.getenv("AZURE_OPENAI_ENDPOINT");;
+            String azureOpenaiKey = System.getenv("AZURE_OPENAI_API_KEY");
+            String endpoint = System.getenv("AZURE_OPENAI_ENDPOINT");
             String deploymentOrModelId = "gpt-35-turbo-instruct";
     
             OpenAIClient client = new OpenAIClientBuilder()
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java SDKの環境変数取得方法の修正"
}
```

### Explanation
この変更は、JavaのSDKにおける環境変数の取得方法に関する小さな修正です。具体的には、コード内で環境変数を取得する際に、不要なセミコロンが削除されています。この修正により、プログラムの可読性が向上し、コードの正確性が保たれます。変更内容は、`String azureOpenaiKey = System.getenv("AZURE_OPENAI_API_KEY");` と `String endpoint = System.getenv("AZURE_OPENAI_ENDPOINT");` という行に見られます。この修正は、Javaのコードのクリーンさを保ち、開発者が理解しやすい形にするための取り組みとして重要です。全体として、ユーザーがこのコードを使用する際の混乱を避け、正しい実装を導く手助けとなります。

## articles/ai-services/openai/monitor-openai-reference.md{#item-8d8887}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,7 @@ See [Monitor Azure OpenAI](./how-to/monitor-openai.md) for details on the data y
 
 ### Supported metrics for Microsoft.CognitiveServices/accounts
 
-Here are the most important metrics we think you should monitor for Azure OpenAI. Later in this article is a longer list of all available Azure AI services metrics which contains more details on metrics in this shorter list.
+Here are the most important metrics we think you should monitor for Azure OpenAI. Later in this article is a longer list of all available Azure AI services metrics which contains more details on metrics in this shorter list. _Please see below list for most up to date information. We're working on refreshing the tables in the following sections._
 
 - Azure OpenAI Requests
 - Active Tokens
@@ -42,9 +42,9 @@ You can also monitor Content Safety metrics that are used by other Azure AI serv
 - Safety System Event
 - Total Volume Sent for Safety Check 
 
-
 > [!NOTE]
 > The **Provisioned-managed Utilization** metric is now deprecated and is no longer recommended. This metric has been replaced by the **Provisioned-managed Utilization V2** metric.
+> Tokens per Second, Time to Response, Time Between Tokens are currently not available for pay-as-you-go (Standard) deployments. 
 
 Cognitive Services metrics have the category **Cognitive Services - HTTP Requests** in the following table. These metrics are legacy metrics that are common to all Azure AI Services resources. Microsoft no longer recommends that you use these metrics with Azure OpenAI.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIメトリクスに関する情報更新"
}
```

### Explanation
この変更は、Azure OpenAIのメトリクスに関する文書の一部を更新したもので、より最新の情報を提供することを目的としています。具体的には、重要なメトリクスを監視する必要があることを説明する文に、新たに「最新の情報については以下のリストをご覧ください。以下のセクションの表を更新中です。」という注意喚起の文が追加されています。この文の追加により、読者は文書の情報が現時点での最新ではないかもしれないことを理解し、最新情報を求める意識が高まります。

また、注記として「トークン毎秒、応答までの時間、トークン間の時間は、従量課金型（スタンダード）デプロイメントでは現在使用できません。」という重要な情報も含まれています。これにより、ユーザーは利用可能なメトリクスの制限について理解し、監視を行う際に注意が必要であることを認識できるようになります。全体として、この更新は文書の信頼性を高め、ユーザーの理解を深めるための重要な措置です。


