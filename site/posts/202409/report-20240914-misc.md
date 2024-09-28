---
date: '2024-09-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:022de22...MicrosoftDocs:3b0d11e
summary: この記事では、Microsoft Azure AIサービスに関するドキュメントのマイナーな更新について詳述しています。主なポイントとして、新機能では文書要約APIに新しい`summaryLength`や`query`フィールドが追加され、中部アメリカおよび南部中心アメリカに対する地域別サポートが強化されました。また、Microsoft
  Entra IDを利用した新たな認証シナリオも導入されています。ブレイキング変更は特になく、文言の明確化や画像、日付の更新も行われています。これらの変更は、ユーザーの利便性向上とドキュメントの明確さを目指したものです。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:022de22...MicrosoftDocs:3b0d11e){target="_blank"}

# ハイライト
この記事では、Microsoft Azure AI サービスの関連ドキュメントへの一連のマイナーな更新に関して、主な変更点を詳細に説明します。以下が更新のハイライトです：
- **新しい機能の追加**：文書要約のAPIに`summaryLength`や新しい`query`フィールドの追加説明、地域別サポート情報の拡充、Microsoft Entra ID 認証のシナリオ追加など。
- **ブレイキング変更**：特に目立ったブレイキング変更はなし。
- **その他の更新**：複数のファイルとドキュメントの文言の修正と明確化、API形式の統一、日付の更新、画像の更新などが含まれます。

## 新しい機能
- **文書要約APIの修正**：`sentenceCount`パラメータに対する`summaryLength`の導入と新しい`query`フィールドの追加。
- **地域別サポート追加**：中部アメリカと南部中心アメリカに新しい要約機能サポートの追加。
- **RBACとMicrosoft Entra ID認証シナリオ**：Microsoft Entra IDを用いた新しい接続シナリオ。

## ブレイキング変更
- 今回の更新において、広範な機能変更や、既存の機能の互換性を著しく損なう変更は特に見受けられませんでした。

## その他の更新
- **文言修正と明確化**：複数のファイルで混乱を避けるための表現修正が行われました。
- **画像ファイルの更新**：接続手順や関連情報を示す画像ファイルの更新。
- **日付の更新**：ドキュメントの日付の更新により最新情報が反映。
- **メソッド名の変更**：接続作成に関するメソッド名の変更。
- **誤字修正**：誤記された用語の修正（例：Content Safeaty → Content Safety）。

# インサイト
これらの変更は、ユーザーがMicrosoft Azure AIサービスを利用する際の利便性を向上させ、ドキュメントの明確性を高めるためのものです。以下に各変更の背景とその意義について具体的に解説します：

### 1. **要約APIの改訂**
文書要約APIに関する変更点がいくつか見られます。具体的には、要約の長さを指定するパラメータに`summaryLength`が導入され、`sentenceCount`の代わりに使用されます。この変更はより直感的であり、要約の出力を制御しやすくする意図があります。また、新たに追加された`query`フィールドは、クエリベースの要約を行う際の柔軟性を高め、ユーザーの要約ニーズに応じたカスタマイズを可能にします。

### 2. **地域別サポート情報の拡充**
新しい地域（中部アメリカと南部中心アメリカ）でのサポートが追加されたことは、Azure AI サービスの利用範囲を広げる重要な更新です。これにより、より多くの地域で要約機能が利用可能となり、ユーザーの地理的制約を減少させることが期待されます。

### 3. **RBACとMicrosoft Entra IDの認証**
Microsoft Entra IDを利用した新しい認証シナリオが追加されました。これにより、セキュリティが強化されると同時に、認証手順が詳細に説明されたことで、開発者が役割ベースのアクセス制御（RBAC）を適切に実装しやすくなります。

### 4. **文字と画像の修正**
各所の文言修正やJSON応答形式の統一、NuGetの正しい表記の適用が行われました。これにより、コードや説明文がより一貫性を持って記述され、可読性が向上します。また、画像ファイルの更新は視覚的な支援を強化し、ユーザーが手順

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [document-summarization.md](#item-da1a14) | minor update | 文書要約のAPI変更についての更新 | modified | 82 | 15 | 97 | 
| [region-support.md](#item-d74574) | minor update | 地域別サポートの追加情報 | modified | 5 | 2 | 7 | 
| [rbac-ai-studio.md](#item-c2a11a) | minor update | AI StudioにおけるRBACとMicrosoft Entra IDの認証のシナリオ追加 | modified | 28 | 3 | 31 | 
| [connections-add.md](#item-6f5a17) | minor update | Azure AI Searchの接続手順の更新と認証方法の追加 | modified | 6 | 1 | 7 | 
| [deploy-models-jais.md](#item-0bd11f) | minor update | Jaisモデルのデプロイ手順に関する文言修正と明確化 | modified | 11 | 11 | 22 | 
| [deploy-models-llama.md](#item-6274a7) | minor update | Meta Llamaモデルのデプロイ手順に関する文言修正と明確化 | modified | 11 | 11 | 22 | 
| [deploy-models-mistral-nemo.md](#item-e7b729) | minor update | Mistral Nemoモデルのデプロイ手順に関する文言修正と明確化 | modified | 9 | 11 | 20 | 
| [deploy-models-mistral-open.md](#item-84e005) | minor update | Mistralモデルのデプロイ手順に関する文言修正と明確化 | modified | 20 | 20 | 40 | 
| [deploy-models-mistral.md](#item-487a41) | minor update | Mistralプレミアムチャットモデルのデプロイ手順に関する文言修正 | modified | 9 | 11 | 20 | 
| [deploy-models-phi-3-5-moe.md](#item-9af6ea) | minor update | Phi-3.5 MoEモデルのデプロイ手順に関する文言修正 | modified | 3 | 3 | 6 | 
| [deploy-models-phi-3-vision.md](#item-bd5aae) | minor update | Phi-3ビジョンモデルのデプロイ手順に関する文言修正 | modified | 3 | 3 | 6 | 
| [deploy-models-phi-3.md](#item-47e305) | minor update | Phi-3モデルのデプロイ手順に関する文言修正 | modified | 3 | 3 | 6 | 
| [deploy-models-serverless-connect.md](#item-4faded) | minor update | サーバーレス接続の作成手順に関する文言修正 | modified | 1 | 1 | 2 | 
| [connections-add-sdk.md](#item-14b519) | minor update | AI Studioにおける接続の追加手順に関する更新 | modified | 37 | 11 | 48 | 
| [fine-tune-model-llama.md](#item-2a42d8) | minor update | Llamaモデルのファインチューニング手順の文言修正 | modified | 1 | 1 | 2 | 
| [connection-add-azure-ai-search-connect.png](#item-95a11f) | minor update | Azure AI Search接続に関する画像の更新 | modified | 0 | 0 | 0 | 
| [connections-all-refreshed.png](#item-a17762) | minor update | データ接続の全てが更新された画像の更新 | modified | 0 | 0 | 0 | 
| [reference-model-inference-api.md](#item-9fe240) | minor update | モデル推論APIドキュメントのマイナー修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/language-service/summarization/how-to/document-summarization.md{#item-da1a14}

<details>
<summary>Diff</summary>
````diff
@@ -122,22 +122,11 @@ curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/
     {
       "kind": "AbstractiveSummarization",
       "taskName": "Text Abstractive Summarization Task 1",
-      "parameters": {
-        "summaryLength": "short"
-      }
     }
   ]
 }
 '
 ```
-If you don't specify `summaryLength`, the model determines the summary length.
-
-### Using the summaryLength parameter
-For the `summaryLength` parameter, three values are accepted:
-* oneSentence: Generates a summary of mostly 1 sentence, with around 80 tokens.
-* short: Generates a summary of mostly 2-3 sentences, with around 120 tokens.
-* medium: Generates a summary of mostly 4-6 sentences, with around 170 tokens.
-* long: Generates a summary of mostly over 7 sentences, with around 210 tokens.
 
 2. Make the following changes in the command where needed:
     - Replace the value `your-language-resource-key` with your key.
@@ -222,7 +211,14 @@ The following cURL commands are executed from a BASH shell. Edit these commands
 
 The query-based text summarization API is an extension to the existing text summarization API.
 
-The biggest difference is a new `query` field in the request body (under `tasks` > `parameters` > `query`). Additionally, there's a new way to specify the preferred `summaryLength` in "buckets" of short/medium/long, which we recommend using instead of `sentenceCount`, especially when using abstractive. Below is an example request:
+The biggest difference is a new `query` field in the request body (under `tasks` > `parameters` > `query`).
+
+> [!TIP]
+> Query based summarization has some differentiation in the utilization of length control based on the type of query based summarization you're using:
+> - Query based extractive summarization supports length control by specifying sentenceCount.
+> - Query based abstractive summarization doesn't support length control.
+
+Below is an example request:
 
 ```bash
 curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/jobs?api-version=2023-11-15-preview \
@@ -253,22 +249,93 @@ curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/
       "kind": "ExtractiveSummarization",
       "taskName": "Query_based Extractive Summarization",
       "parameters": {
-          "query": "XYZ-code",
-          "sentenceCount": 3
+          "query": "XYZ-code"
       }
     }
   ]
 }
 '
 ```
 
-### Using the summaryLength parameter
+### Summary length control
+
+#### Using the summaryLength parameter in abstractive summarization
+
+If you don't specify `summaryLength`, the model determines the summary length.
+
 For the `summaryLength` parameter, three values are accepted:
 * oneSentence: Generates a summary of mostly 1 sentence, with around 80 tokens.
 * short: Generates a summary of mostly 2-3 sentences, with around 120 tokens.
 * medium: Generates a summary of mostly 4-6 sentences, with around 170 tokens.
 * long: Generates a summary of mostly over 7 sentences, with around 210 tokens.
 
+Below is an example request:
+
+```bash
+curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/jobs?api-version=2023-04-01 \
+-H "Content-Type: application/json" \
+-H "Ocp-Apim-Subscription-Key: <your-language-resource-key>" \
+-d \
+' 
+{
+  "displayName": "Text Abstractive Summarization Task Example",
+  "analysisInput": {
+    "documents": [
+      {
+        "id": "1",
+        "language": "en",
+        "text": "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there’s magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
+      }
+    ]
+  },
+  "tasks": [
+    {
+      "kind": "AbstractiveSummarization",
+      "taskName": "Length controlled Abstractive Summarization",
+          "parameters": {
+          "sentenceLength": "short"
+      }
+    }
+  ]
+}
+'
+```
+
+#### Using the sentenceCount parameter in extractive summarization
+For the `sentenceCount` parameter, you can input a value 1-20 to indicate the desired number of output sentences.
+
+Below is an example request:
+
+```bash
+curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/jobs?api-version=2023-11-15-preview \
+-H "Content-Type: application/json" \
+-H "Ocp-Apim-Subscription-Key: <your-language-resource-key>" \
+-d \
+' 
+{
+  "displayName": "Text Extractive Summarization Task Example",
+  "analysisInput": {
+    "documents": [
+      {
+        "id": "1",
+        "language": "en",
+        "text": "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there’s magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
+      }
+    ]
+  },
+"tasks": [
+    {
+      "kind": "ExtractiveSummarization",
+      "taskName": "Length controlled Extractive Summarization",
+      "parameters": {
+          "sentenceCount": "5"
+      }
+    }
+  ]
+}
+'
+```
+
 ## Service and data limits
 
 [!INCLUDE [service limits article](../../includes/service-limits-link.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書要約のAPI変更についての更新"
}
```

### Explanation
このコードの変更は、Microsoft Azure AIの文書要約APIに関連したドキュメントの更新を含んでいます。主に、要約の長さに関するパラメータとクエリベースの要約処理に関する情報が追加されており、文書の理解を深める内容になっています。

編集された内容では、以下の重要な変更が見られます：

1. **要約長さの指定方法の変更**:
   - 要約の長さを指定する際に、`sentenceCount`の代わりに、`summaryLength`という新しい方法が導入され、これに関する詳細がドキュメントに追加されました。

2. **新しいクエリフィールドの追加**:
   - リクエストボディ内に新たに`query`フィールドが導入され、クエリベースの要約における利用方法の違いが説明されています。

3. **具体例の追加**:
   - 新しいAPI呼び出しの具体例が追加され、ユーザーが新しい構文や要求パラメータを簡単に理解できるようにしています。

これにより、ユーザーは要約生成APIをより効率的に活用できるようになり、特に異なる要約のスタイルに応じた長さの制御が可能になっています。変更は文書の明確化と機能の強化を目的としています。

## articles/ai-services/language-service/summarization/region-support.md{#item-d74574}

<details>
<summary>Diff</summary>
````diff
@@ -25,11 +25,14 @@ Some summarization features are only available in limited regions. More regions
 |North Europe      |&#9989;                           |&#9989;                                        |&#10060;            |
 |East US           |&#9989;                           |&#9989;                                        |&#9989;             |
 |East US 2         |&#9989;                           |&#9989;                                        |&#10060;            |
+|Central US        |&#9989;                           |&#9989;                                        |&#10060;            |
+|South Central US  |&#9989;                           |&#9989;                                        |&#10060;            |
 |West US           |&#9989;                           |&#9989;                                        |&#10060;            |
-|USNat West        |&#9989;                           |&#9989;                                        |&#10060;            |
+|West US 2         |&#9989;                           |&#9989;                                        |&#10060;            |
 |USNat East        |&#9989;                           |&#9989;                                        |&#10060;            |
-|USSec West        |&#9989;                           |&#9989;                                        |&#10060;            |
+|USNat West        |&#9989;                           |&#9989;                                        |&#10060;            |
 |USSec East        |&#9989;                           |&#9989;                                        |&#10060;            |
+|USSec West        |&#9989;                           |&#9989;                                        |&#10060;            |
 |South UK          |&#9989;                           |&#9989;                                        |&#10060;            |
 |Southeast Asia    |&#9989;                           |&#9989;                                        |&#10060;            |
 |Australia East    |&#9989;                           |&#9989;                                        |&#10060;            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域別サポートの追加情報"
}
```

### Explanation
このコードの変更は、Microsoft Azure AIの要約サービスに関連する地域別のサポート情報の更新を含んでいます。特に、特定の要約機能が利用可能な地域に関する情報が拡充されています。

具体的な変更内容としては以下の点が挙げられます：

1. **新しい地域の追加**:
   - 中部アメリカ（Central US）と南部中心アメリカ（South Central US）における要約機能のサポートが追加されました。これにより、具体的にどの地域でどの要約機能が利用可能かを明確に示しています。

2. **地域名の変更**:
   - 一部の地域名が更新され、正確な情報が提供されています。これには、西部アメリカ（West US 2）と南西アメリカ（USSec West）も含まれており、情報の整合性が向上しています。

3. **全体の整備**:
   - テーブル全体の内容が見直され、地域別の要約機能のサポート状況が一目で分かるように整理されています。

これにより、ユーザーはAzure AIの要約サービスがどの地域で利用可能であるかを簡単に確認できるようになり、サービスの利用範囲を理解する助けとなります。変更は、ユーザーフレンドリーな情報提供を目的としています。

## articles/ai-studio/concepts/rbac-ai-studio.md{#item-c2a11a}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: conceptual
-ms.date: 5/21/2024
+ms.date: 9/12/2024
 ms.reviewer: deeikele
 ms.author: larryfr
 author: Blackmist
@@ -214,6 +214,31 @@ If your AI Studio hub is configured with a **user-assigned managed identity**, t
 
 Within the key vault, the user or service principal must have the create, get, delete, and purge access to the key through a key vault access policy. For more information, see [Azure Key Vault security](/azure/key-vault/general/security-features#controlling-access-to-key-vault-data).
 
+## Scenario: Connections using Microsoft Entra ID authentication
+
+When you create a connection that uses Microsoft Entra ID authentication, you must assign roles to your developers so they can access the resource.
+
+| Resource connection | Role | Description |
+|----------|------|-------------|
+| Azure AI Search | Contributor | List API-Keys to list indexes from Azure AI Studio. |
+| Azure AI Search | Search Index Data Contributor | Required for indexing scenarios |
+| Azure AI services / Azure OpenAI | Cognitive Services OpenAI Contributor | Call public ingestion API from Azure AI Studio. |
+| Azure AI services / Azure OpenAI | Cognitive Services User | List API-Keys from Azure AI Studio. |
+| Azure AI services / Azure OpenAI | Contributor | Allows for calls to the control plane. |
+
+When using Microsoft Entra ID authenticated connections in the chat playground, the services need to authorize each other to access the required resources. The admin performing the configuration needs to have the __Owner__ role on these resources to add role assignments. The following table lists the required role assignments for each resource. The __Assignee__ column refers to the system-assigned managed identity of the listed resource. The __Resource__ column refers to the resource that the assignee needs to access. For example, Azure OpenAI has a system-assigned managed identity that needs to be assigned the __Search Index Data Reader__ role for the Azure AI Search resource.
+
+| Role | Assignee | Resource | Description |
+|------|----------|----------|-------------|
+| Search Index Data Reader | Azure AI services / Azure OpenAI | Azure AI Search | Inference service queries the data from the index. Only used for inference scenarios. |
+| Search Index Data Contributor | Azure AI services / Azure OpenAI | Azure AI Search | Read-write access to content in indexes. Import, refresh, or query the documents collection of an index. Only used for ingestion and inference scenarios. |
+| Search Service Contributor | Azure AI services / Azure OpenAI | Azure AI Search | Read-write access to object definitions (indexes, aliases, synonym maps, indexers, data sources, and skillsets). Inference service queries the index schema for auto fields mapping. Data ingestion service creates index, data sources, skill set, indexer, and queries the indexer status. |
+| Cognitive Services OpenAI Contributor | Azure AI Search | Azure AI services / Azure OpenAI | Custom skill |
+| Cognitive Services OpenAI User | Azure OpenAI Resource for chat model | Azure OpenAI resource for embedding model | Required only if using two Azure OpenAI resources to communicate. |
+
+> [!NOTE]
+> The __Cognitive Services OpenAI User__ role is only required if you are using two Azure OpenAI resources: one for your chat model and one for your embedding model. If this applies, enable Trusted Services AND ensure the connection for your embedding model Azure OpenAI resource has Microsoft Entra ID enabled.  
+
 ## Scenario: Use an existing Azure OpenAI resource
 
 When you create a connection to an existing Azure OpenAI resource, you must also assign roles to your users so they can access the resource. You should assign either the **Cognitive Services OpenAI User** or **Cognitive Services OpenAI Contributor** role, depending on the tasks they need to perform. For information on these roles and the tasks they enable, see [Azure OpenAI roles](/azure/ai-services/openai/how-to/role-based-access-control#azure-openai-roles).
@@ -291,8 +316,8 @@ The following example defines a role for a developer using [Azure OpenAI Assista
 {
     "id": "",
     "properties": {
-        "roleName": "CognitiveServices OpenAI Assistants API Developer",
-        "description": "Custom role to work with AOAI Assistants API",
+        "roleName": "Azure OpenAI Assistants API Developer",
+        "description": "Custom role to work with Azure OpenAI Assistants API",
         "assignableScopes": [
             "<your-scope>"
         ],
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI StudioにおけるRBACとMicrosoft Entra IDの認証のシナリオ追加"
}
```

### Explanation
このコードの変更は、Microsoft Azure AI StudioのRBAC（ロールベースのアクセス制御）に関するドキュメントの更新を含んでいます。特に、Microsoft Entra ID認証を使用した接続に関する新しいシナリオが追加され、開発者がリソースにアクセスするために必要なロール分配の詳細が強化されています。

主な変更点は以下の通りです：

1. **Microsoft Entra ID認証に関する新しいセクション**:
   - Microsoft Entra IDを使用して接続を作成する場合、開発者にリソースへのアクセス権を付与するために必要なロールの情報が新たに追加されました。

2. **新しい役割の詳細**:
   - Azure AI SearchやCognitive Services OpenAIに関連する異なるロールやそれらの説明が表形式で整理され、どのロールがどのリソースに必要であるかが明確に示されています。

3. **重要な注意事項の追加**:
   - 異なるAzure OpenAIリソース間の接続の際に必要なロールの詳細と、それに伴う設定に関する注意事項が強調されています。

4. **既存のAzure OpenAIリソースの使用に関するガイダンス**:
   - 既存のAzure OpenAIリソースに接続するために必要な意図が述べられ、関連するロールの説明もされています。

5. **カスタムロールの名称変更**:
   - カスタムロールの名称が更新され、明確な識別が可能になっています。

これにより、ユーザーはAI Studio内でのRBACの管理やMicrosoft Entra IDを用いた認証についての理解が深まり、適切なロールを割り当てるための具体的な手順を把握しやすくなります。変更は、ユーザーがサービスをより効果的に利用できるようにしたことを目的としています。

## articles/ai-studio/how-to/connections-add.md{#item-6f5a17}

<details>
<summary>Diff</summary>
````diff
@@ -52,7 +52,12 @@ Follow these steps to create a new connection that's only available for the curr
 
     :::image type="content" source="../media/data-connections/connection-add-browse-azure-ai-search.png" alt-text="Screenshot of the page to select Azure AI Search from a list of other resources." lightbox="../media/data-connections/connection-add-browse-azure-ai-search.png":::
 
-1. Browse for and select your Azure AI Search service from the list of available services. Select **Add connection**.
+1. Browse for and select your Azure AI Search service from the list of available services and then select the type of __Authentication__ to use for the resource. Select **Add connection**.
+
+    > [!TIP]
+    > Different connection types support different authentication methods. Using Microsoft Entra ID may require specific Azure role-based access permissions for your developers. For more information, visit [Role-based access control](../concepts/rbac-ai-studio.md#scenario-connections-using-microsoft-entra-id-authentication).
+    >
+    > Microsoft Entra ID support with the Azure AI Search connection is currently in preview.
 
     :::image type="content" source="../media/data-connections/connection-add-azure-ai-search-connect.png" alt-text="Screenshot of the page to select the Azure AI Search service that you want to connect to." lightbox="../media/data-connections/connection-add-azure-ai-search-connect.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchの接続手順の更新と認証方法の追加"
}
```

### Explanation
このコードの変更は、Azure AI StudioにおけるAzure AI Searchサービスへの接続手順に関連するドキュメントの更新を反映しています。具体的には、接続を作成する際の認証方法に関する情報が追加されています。

主な変更点は以下の通りです：

1. **接続手順の一部改善**:
   - Azure AI Searchサービスを選択する際に、リソースに使用する認証の種類を選択することが明記されました。この変更により、ユーザーは接続時に適切な認証方法を選ぶことができます。

2. **ヒントの追加**:
   - 異なる接続タイプが異なる認証方法をサポートすることに関するヒントが追加され、特にMicrosoft Entra IDを使用する場合には、開発者に特定のAzureのロールベースのアクセス権限が必要であることが説明されています。これにより、ユーザーがアクセス権の管理をより理解できるようになります。

3. **プレビュー告知の追加**:
   - Azure AI Search接続に対するMicrosoft Entra IDのサポートが現在プレビュー段階である旨の注意書きが追加され、ユーザーに最新の情報を提供しています。

これにより、ユーザーが接続を作成する際に必要な手順を理解しやすくなり、認証方法に関する重要な情報が提供されることで、エラーを減らし、スムーズな利用体験を促進することを目指しています。変更は、ユーザーの利便性向上のために行われています。

## articles/ai-studio/how-to/deploy-models-jais.md{#item-0bd11f}

<details>
<summary>Diff</summary>
````diff
@@ -201,7 +201,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormatText
+from azure.ai.inference.models import ChatCompletionsResponseFormat
 
 response = client.complete(
     messages=[
@@ -214,12 +214,12 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
 )
 ```
 
 > [!WARNING]
-> Jais doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Jais models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -482,7 +482,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!WARNING]
-> Jais doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Jais models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -580,7 +580,7 @@ Deployment to a serverless API endpoint doesn't require quota from your subscrip
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -606,7 +606,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also use the following namespaces but you may not always need them:
+This example also uses the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -775,7 +775,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
 > [!WARNING]
-> Jais doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Jais models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1088,7 +1088,7 @@ Explore other parameters that you can specify in the inference client. For a ful
 ```
 
 > [!WARNING]
-> Jais doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Jais models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1165,14 +1165,14 @@ The following example shows how to handle events when the model detects harmful
 
 ## More inference examples
 
-For more examples of how to use Jais, see the following examples and tutorials:
+For more examples of how to use Jais models, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 
-## Cost and quota considerations for Jais family of models deployed as serverless API endpoints
+## Cost and quota considerations for Jais models deployed as serverless API endpoints
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
@@ -1189,4 +1189,4 @@ For more information on how to track costs, see [Monitor costs for models offere
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Jaisモデルのデプロイ手順に関する文言修正と明確化"
}
```

### Explanation
このコードの変更は、Azure AI StudioにおけるJaisモデルのデプロイ手順に関連するドキュメントの改訂を示しています。変更は、主に文言の修正といくつかの技術的な説明の明確化を含んでいます。

主な変更点は以下の通りです：

1. **インポート文の修正**:
   - `ChatCompletionsResponseFormatText`というクラス名が`ChatCompletionsResponseFormat`に変更され、応答フォーマットの指定が新しい形式に統一されました。

2. **応答フォーマットに関する警告の明確化**:
   - JaisモデルがJSON出力フォーマットをサポートしていないことを明確に示すため、警告文が変更されました。これにより、ユーザーがモデルの出力に対する期待を明確に理解できるようになります。

3. **パラメータのパス方法について**:
   - サポートされていないパラメータが必要な場合に、どのようにしてそれをモデルに渡すかに関する説明が一貫性を持って提供されています。

4. **依存関係の記述修正**:
   - NuGetパッケージに関する説明が更新され、正確なパッケージ名が使用されています（"NuGet"と大文字で記載）。

5. **文の明確化**:
   - Jaisモデルに関するいくつかの説明文が修正され、より明確で正確な表現に統一されています。特にモデルの使用例やコストについてのセクションが洗練されています。

これにより、ユーザーはJaisモデルをより効果的にデプロイし、使用するための具体的かつ正確な情報を得ることができます。変更は、利用者が適切な理解を持って操作できるようにすることを目的としています。

## articles/ai-studio/how-to/deploy-models-llama.md{#item-6274a7}

<details>
<summary>Diff</summary>
````diff
@@ -255,7 +255,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormatText
+from azure.ai.inference.models import ChatCompletionsResponseFormat
 
 response = client.complete(
     messages=[
@@ -268,12 +268,12 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
 )
 ```
 
 > [!WARNING]
-> Meta Llama doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Meta Llama models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -610,7 +610,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!WARNING]
-> Meta Llama doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Meta Llama models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -765,7 +765,7 @@ For deployment to a self-hosted managed compute, you must have enough quota in y
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -791,7 +791,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also use the following namespaces but you may not always need them:
+This example also uses the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -973,7 +973,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
 > [!WARNING]
-> Meta Llama doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Meta Llama models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1348,7 +1348,7 @@ Explore other parameters that you can specify in the inference client. For a ful
 ```
 
 > [!WARNING]
-> Meta Llama doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Meta Llama models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1441,7 +1441,7 @@ The following example shows how to handle events when the model detects harmful
 
 ## More inference examples
 
-For more examples of how to use Meta Llama, see the following examples and tutorials:
+For more examples of how to use Meta Llama models, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                             |
 |-------------------------------------------|-------------------|------------------------------------------------------------------- |
@@ -1453,7 +1453,7 @@ For more examples of how to use Meta Llama, see the following examples and tutor
 | LangChain                                 | Python            | [Link](https://aka.ms/meta-llama-3.1-405B-instruct-langchain)      |
 | LiteLLM                                   | Python            | [Link](https://aka.ms/meta-llama-3.1-405B-instruct-litellm)        | 
 
-## Cost and quota considerations for Meta Llama family of models deployed as serverless API endpoints
+## Cost and quota considerations for Meta Llama models deployed as serverless API endpoints
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
@@ -1463,7 +1463,7 @@ Each time a project subscribes to a given offer from the Azure Marketplace, a ne
 
 For more information on how to track costs, see [Monitor costs for models offered through the Azure Marketplace](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace).
 
-## Cost and quota considerations for Meta Llama family of models deployed to managed compute
+## Cost and quota considerations for Meta Llama models deployed to managed compute
 
 Meta Llama models deployed to managed compute are billed based on core hours of the associated compute instance. The cost of the compute instance is determined by the size of the instance, the number of instances running, and the run duration.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Meta Llamaモデルのデプロイ手順に関する文言修正と明確化"
}
```

### Explanation
このコードの変更は、Azure AI StudioにおけるMeta Llamaモデルのデプロイ手順に関するドキュメントを更新するもので、主に文言の調整と説明の明確化が含まれています。

主な変更点は以下の通りです：

1. **インポート文の修正**:
   - `ChatCompletionsResponseFormatText`というクラス名が`ChatCompletionsResponseFormat`に変更され、応答フォーマットが更新されました。これによりAPIの整合性が保たれました。

2. **JSON出力に関する警告の明確化**:
   - Meta LlamaモデルがJSON出力フォーマットをサポートしていない点についての説明が強化され、ユーザーが期待する出力形式に関して誤解を避けるための修正が行われました。

3. **パラメータのパス方法に関する説明**:
   - サポートされていないパラメータをモデルに渡す方法についての説明が効果的に整理され、ユーザーが必要な情報を簡単に見つけられるようになっています。

4. **NuGetの表記統一**:
   - `Nuget`が`NuGet`に修正され、正式な名称が使用されています。

5. **文の明確化**:
   - "Meta Llama"関連の説明文がいくつか修正され、より明確で一貫した表現になりました。特にモデルの使用例やコスト・制限に関する部分が改善されています。

これにより、ユーザーはMeta Llamaモデルをより効果的にデプロイし活用するための具体的かつ正確な情報にアクセス可能になり、文書が全体的に改善されています。変更は、利用者が情報を正確に理解し、適切に操作できるようにするために行われました。

## articles/ai-studio/how-to/deploy-models-mistral-nemo.md{#item-e7b729}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Mistral Nemo chat model with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 08/08/2024
+ms.date: 09/12/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -209,7 +209,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormatText
+from azure.ai.inference.models import ChatCompletionsResponseFormat
 
 response = client.complete(
     messages=[
@@ -222,7 +222,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
 )
 ```
 
@@ -234,15 +234,13 @@ Mistral Nemo chat model can create JSON outputs. Set `response_format` to `json_
 
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormatJSON
-
 response = client.complete(
     messages=[
         SystemMessage(content="You are a helpful assistant that always generate responses in JSON format, using."
                       " the following format: { ""answer"": ""response"" }."),
         UserMessage(content="How many languages are in the world?"),
     ],
-    response_format=ChatCompletionsResponseFormatJSON()
+    response_format={ "type": ChatCompletionsResponseFormat.JSON_OBJECT }
 )
 ```
 
@@ -962,7 +960,7 @@ Deployment to a serverless API endpoint doesn't require quota from your subscrip
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -988,7 +986,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also use the following namespaces but you may not always need them:
+This example also uses the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -2010,7 +2008,7 @@ The following example shows how to handle events when the model detects harmful
 
 ## More inference examples
 
-For more examples of how to use Mistral, see the following examples and tutorials:
+For more examples of how to use Mistral models, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
@@ -2024,7 +2022,7 @@ For more examples of how to use Mistral, see the following examples and tutorial
 | LiteLLM                                   | Python            | [Link](https://aka.ms/mistral-large/litellm-sample)             | 
 
 
-## Cost and quota considerations for Mistral family of models deployed as serverless API endpoints
+## Cost and quota considerations for Mistral models deployed as serverless API endpoints
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
@@ -2041,4 +2039,4 @@ For more information on how to track costs, see [Monitor costs for models offere
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistral Nemoモデルのデプロイ手順に関する文言修正と明確化"
}
```

### Explanation
このコードの変更は、Azure AI StudioにおけるMistral Nemoモデルのデプロイ手順に関連するドキュメントを更新するもので、主に文言の修正と説明の明確化が含まれています。

主な変更点は以下の通りです：

1. **日付の更新**:
   - ドキュメントの日付が`08/08/2024`から`09/12/2024`に変更され、最新の情報を反映しています。

2. **インポート文の修正**:
   - `ChatCompletionsResponseFormatText`が`ChatCompletionsResponseFormat`に変更され、APIの一貫性が保たれました。

3. **応答フォーマットに関する修正**:
   - JSON形式の応答を生成する方法が更新され、`response_format`の指定が新しい形式で定義されています。これにより、コードの可読性と理解が向上しています。

4. **年も含めた表記の統一**:
   - `Nuget`が`NuGet`に修正され、正式な名称で統一されています。

5. **文の明確化**:
   - "Mistral"や"サーバーレスAPIエンドポイント"に関する説明文が修正され、より明確で一貫した表現になっています。特にモデルの使用例やコストに関するセクションが洗練されています。

この変更は、ユーザーがMistral Nemoモデルをより効果的にデプロイし、活用するための最新かつ正確な情報を提供することを目的としています。全体として、内容が整備され、ユーザーが情報を正確に理解できるよう努力されています。

## articles/ai-studio/how-to/deploy-models-mistral-open.md{#item-84e005}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Mistral-7B and Mixtral chat models with Azure AI S
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 08/08/2024
+ms.date: 09/12/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -63,8 +63,8 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling; along with the constrained output mode implemented on la Plateforme, this enables application development and tech stack modernization at scale
-* Pprecise information recall from large documents, due to its 64K tokens context window
+* Natively capable of function calling, enabling application development and tech stack modernization at scale
+* Precise information recall from large documents, due to its 64K tokens context window
 
 
 The following models are available:
@@ -257,7 +257,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormatText
+from azure.ai.inference.models import ChatCompletionsResponseFormat
 
 response = client.complete(
     messages=[
@@ -270,12 +270,12 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
 )
 ```
 
 > [!WARNING]
-> Mistral doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -352,8 +352,8 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling; along with the constrained output mode implemented on la Plateforme, this enables application development and tech stack modernization at scale
-* Pprecise information recall from large documents, due to its 64K tokens context window
+* Natively capable of function calling, enabling application development and tech stack modernization at scale
+* Precise information recall from large documents, due to its 64K tokens context window
 
 
 The following models are available:
@@ -576,7 +576,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!WARNING]
-> Mistral doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -658,8 +658,8 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling; along with the constrained output mode implemented on la Plateforme, this enables application development and tech stack modernization at scale
-* Pprecise information recall from large documents, due to its 64K tokens context window
+* Natively capable of function calling, enabling application development and tech stack modernization at scale
+* Precise information recall from large documents, due to its 64K tokens context window
 
 
 The following models are available:
@@ -689,7 +689,7 @@ For deployment to a self-hosted managed compute, you must have enough quota in y
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -715,7 +715,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also use the following namespaces but you may not always need them:
+This example also uses the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -897,7 +897,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
 > [!WARNING]
-> Mistral doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -976,8 +976,8 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling; along with the constrained output mode implemented on la Plateforme, this enables application development and tech stack modernization at scale
-* Pprecise information recall from large documents, due to its 64K tokens context window
+* Natively capable of function calling, enabling application development and tech stack modernization at scale
+* Precise information recall from large documents, due to its 64K tokens context window
 
 
 The following models are available:
@@ -1230,7 +1230,7 @@ Explore other parameters that you can specify in the inference client. For a ful
 ```
 
 > [!WARNING]
-> Mistral doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1279,7 +1279,7 @@ The following extra parameters can be passed to Mistral-7B and Mixtral chat mode
 
 ## More inference examples
 
-For more examples of how to use Mistral, see the following examples and tutorials:
+For more examples of how to use Mistral models, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
@@ -1293,7 +1293,7 @@ For more examples of how to use Mistral, see the following examples and tutorial
 | LiteLLM                                   | Python            | [Link](https://aka.ms/mistral-large/litellm-sample)             | 
 
 
-## Cost and quota considerations for Mistral family of models deployed to managed compute
+## Cost and quota considerations for Mistral models deployed to managed compute
 
 Mistral models deployed to managed compute are billed based on core hours of the associated compute instance. The cost of the compute instance is determined by the size of the instance, the number of instances running, and the run duration.
 
@@ -1306,4 +1306,4 @@ It is a good practice to start with a low number of instances and scale up as ne
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralモデルのデプロイ手順に関する文言修正と明確化"
}
```

### Explanation
このコードの変更は、Azure AI StudioにおけるMistralモデルのデプロイ手順に関するドキュメントを更新するもので、主に文言の修正と説明の整備が含まれています。

主な変更点は以下の通りです：

1. **日付の更新**:
   - ドキュメントの日付が`08/08/2024`から`09/12/2024`に変更され、情報の新しさを反映しています。

2. **機能説明の修正**:
   - Mixtralモデルの強みを説明する文から冗長な部分が削除され、内容が簡潔になりました。特に、`function calling`の説明が明確化され、よりシンプルに表現されています。

3. **インポート文の変更**:
   - モデル応答形式のインポートに関する表記が更新され、`ChatCompletionsResponseFormatText`から`ChatCompletionsResponseFormat`に変更され、コードが統一されました。

4. **JSON出力に関する注意書きの修正**:
   - MistralモデルがJSON出力フォーマットをサポートしていないという警告がより明示的になり、ユーザーへの情報が明確に伝わるようになっています。

5. **NuGetの表記統一**:
   - `Nuget`が`NuGet`に修正され、正式名称が使用されています。

6. **文の明確化**:
   - "Mistral"に関する記述が更新され、モデルの使用例やコストに関する情報が一貫性を持った表現に整えられています。

これらの変更は、ユーザーがMistralモデルを効率的にデプロイし活用するための最新かつ正確な情報を提供することを目的としています。全体的に、ドキュメントの整備が行われており、ユーザーが情報を適切に理解しやすくなっています。

## articles/ai-studio/how-to/deploy-models-mistral.md{#item-487a41}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Mistral premium chat models with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 08/08/2024
+ms.date: 09/12/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -239,7 +239,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormatText
+from azure.ai.inference.models import ChatCompletionsResponseFormat
 
 response = client.complete(
     messages=[
@@ -252,7 +252,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
 )
 ```
 
@@ -264,15 +264,13 @@ Mistral premium chat models can create JSON outputs. Set `response_format` to `j
 
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormatJSON
-
 response = client.complete(
     messages=[
         SystemMessage(content="You are a helpful assistant that always generate responses in JSON format, using."
                       " the following format: { ""answer"": ""response"" }."),
         UserMessage(content="How many languages are in the world?"),
     ],
-    response_format=ChatCompletionsResponseFormatJSON()
+    response_format={ "type": ChatCompletionsResponseFormat.JSON_OBJECT }
 )
 ```
 
@@ -1052,7 +1050,7 @@ Deployment to a serverless API endpoint doesn't require quota from your subscrip
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -1078,7 +1076,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also use the following namespaces but you may not always need them:
+This example also uses the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -2130,7 +2128,7 @@ The following example shows how to handle events when the model detects harmful
 
 ## More inference examples
 
-For more examples of how to use Mistral, see the following examples and tutorials:
+For more examples of how to use Mistral models, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
@@ -2144,7 +2142,7 @@ For more examples of how to use Mistral, see the following examples and tutorial
 | LiteLLM                                   | Python            | [Link](https://aka.ms/mistral-large/litellm-sample)             | 
 
 
-## Cost and quota considerations for Mistral family of models deployed as serverless API endpoints
+## Cost and quota considerations for Mistral models deployed as serverless API endpoints
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
@@ -2161,4 +2159,4 @@ For more information on how to track costs, see [Monitor costs for models offere
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralプレミアムチャットモデルのデプロイ手順に関する文言修正"
}
```

### Explanation
このコードの変更は、Azure AI StudioにおけるMistralプレミアムチャットモデルのデプロイ手順に関するドキュメントの更新で、主に文言の修正が行われています。

主な変更点は以下の通りです：

1. **日付の更新**:
   - ドキュメントの日付が`08/08/2024`から`09/12/2024`に変更され、最新の情報を反映しています。

2. **インポート文の変更**:
   - `ChatCompletionsResponseFormatText`から`ChatCompletionsResponseFormat`に変更され、APIの一貫性が保たれました。

3. **応答形式の記述修正**:
   - モデルが生成するJSON出力の応答形式の指定が、従来の`ChatCompletionsResponseFormatJSON`から新しい形式`{ "type": ChatCompletionsResponseFormat.JSON_OBJECT }`に更新され、コードの可読性が向上しました。

4. **NuGetの表記統一**:
   - `Nuget`が`NuGet`に修正され、正しい名称が使われるようになりました。

5. **文の明確化**:
   - Mistralモデルに関する説明の一貫性を高めるために、冗長な表現が削除され、内容が整理されました。

6. **コストとクォータに関する文言の改善**:
   - Mistralモデルのコスト管理に関する説明が明確にされ、サーバーレスAPIエンドポイントにデプロイされた場合の管理情報が整理されています。

これらの変更は、ユーザーがMistralモデルをより効果的にデプロイおよび活用できるよう、最新かつ正確な情報を提供することを目的としています。全体として、情報が整理されており、ユーザーが理解しやすい形に改善されています。

## articles/ai-studio/how-to/deploy-models-phi-3-5-moe.md{#item-9af6ea}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Phi-3.5 MoE chat model with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 08/19/2024
+ms.date: 09/12/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -219,7 +219,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormatText
+from azure.ai.inference.models import ChatCompletionsResponseFormat
 
 response = client.complete(
     messages=[
@@ -232,7 +232,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
 )
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3.5 MoEモデルのデプロイ手順に関する文言修正"
}
```

### Explanation
このコードの変更は、Azure AI StudioにおけるPhi-3.5 MoEチャットモデルのデプロイ手順に関するドキュメントの更新を目的としています。主に文言の修正が行われています。

主な変更点は以下の通りです：

1. **日付の更新**:
   - ドキュメントの日付が`08/19/2024`から`09/12/2024`に変更され、情報が最新のものとなりました。

2. **インポート文の変更**:
   - `ChatCompletionsResponseFormatText`から`ChatCompletionsResponseFormat`に更新され、APIの一貫性が向上しました。

3. **応答形式の指定修正**:
   - モデルの応答形式指定が、`ChatCompletionsResponseFormatText()`から新しい形式である`{ "type": ChatCompletionsResponseFormat.TEXT }`に変更され、コードの可読性が向上しています。

これらの変更は、ユーザーがPhi-3.5 MoEモデルを効果的にデプロイし使用するための最新情報を提供することを目的としており、情報が整理され、理解しやすくなっています。全体として、ドキュメントの整備が進められており、ユーザーにとって価値あるリソースとなるよう改善されています。

## articles/ai-studio/how-to/deploy-models-phi-3-vision.md{#item-bd5aae}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Phi-3 chat model with vision with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 08/19/2024
+ms.date: 09/12/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -215,7 +215,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormatText
+from azure.ai.inference.models import ChatCompletionsResponseFormat
 
 response = client.complete(
     messages=[
@@ -228,7 +228,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
 )
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3ビジョンモデルのデプロイ手順に関する文言修正"
}
```

### Explanation
このコードの変更は、Azure AI StudioにおけるPhi-3チャットモデル（ビジョン付き）のデプロイ手順に関するドキュメントの更新です。主として文言の修正が行われています。

主な変更点は以下の通りです：

1. **日付の更新**:
   - ドキュメントの日付が`08/19/2024`から`09/12/2024`に変更され、最新の情報が反映されるようになりました。

2. **インポート文の修正**:
   - `ChatCompletionsResponseFormatText`から`ChatCompletionsResponseFormat`に変更され、APIの名称が統一されました。

3. **応答形式の指定の修正**:
   - `response_format`の指定が、従来の形式である`ChatCompletionsResponseFormatText()`から新しい形式`{ "type": ChatCompletionsResponseFormat.TEXT }`に変更され、明示的な記述に改善されています。

これらの変更は、Phi-3チャットモデル（ビジョン付き）を利用するユーザーが正確で最新な情報を得られるようにすることを目指しています。特に、コードの可読性と整合性が向上されており、ユーザーの理解を助けるための改善がなされています。全体として、ドキュメントが整理され、より効果的な情報提供を実現しています。

## articles/ai-studio/how-to/deploy-models-phi-3.md{#item-47e305}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Phi-3 family chat models with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 08/19/2024
+ms.date: 09/12/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -256,7 +256,7 @@ print_stream(result)
 Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
 
 ```python
-from azure.ai.inference.models import ChatCompletionsResponseFormatText
+from azure.ai.inference.models import ChatCompletionsResponseFormat
 
 response = client.complete(
     messages=[
@@ -269,7 +269,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormat.TEXT },
 )
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3モデルのデプロイ手順に関する文言修正"
}
```

### Explanation
このコードの変更は、Azure AI StudioにおけるPhi-3ファミリーのチャットモデルのデプロイ手順に関するドキュメントの更新を示しています。主に文言の修正が行われ、情報が最新になっています。

主な変更点は以下の通りです：

1. **日付の更新**:
   - ドキュメントの日付が`08/19/2024`から`09/12/2024`に変更され、最新の作成日が反映されています。

2. **インポート文の変更**:
   - `ChatCompletionsResponseFormatText`から`ChatCompletionsResponseFormat`に修正され、モデルに対するインポートの正確性を高めています。

3. **応答形式の指定の修正**:
   - `response_format`の設定が、`ChatCompletionsResponseFormatText()`から新しい形式である`{ "type": ChatCompletionsResponseFormat.TEXT }`に変更され、より明確で一貫性のある表現になりました。

これらの修正は、Phi-3モデルの使用を促進するための重要なステップであり、ユーザーが正確で詳細な情報を得ることができるようにしています。全体として、コードの可読性が向上し、ドキュメントの内容が整理され、より使いやすくなっています。

## articles/ai-studio/how-to/deploy-models-serverless-connect.md{#item-4faded}

<details>
<summary>Diff</summary>
````diff
@@ -202,7 +202,7 @@ Follow these steps to create a connection:
     # [Python SDK](#tab/python)
 
     ```python
-    client.connections.create(ServerlessConnection(
+    client.connections.create_or_update(ServerlessConnection(
         name="meta-llama3-8b-connection",
         endpoint="https://meta-llama3-8b-qwerty-serverless.inference.ai.azure.com",
         api_key="1234567890qwertyuiop"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレス接続の作成手順に関する文言修正"
}
```

### Explanation
このコードの変更は、Azure AI Studioにおけるサーバーレス接続のデプロイ手順に関するドキュメントの更新を示しています。主に、APIのメソッド名が変更され、より適切な表現に更新されています。

主な変更点は以下の通りです：

1. **メソッド名の修正**:
   - `client.connections.create(ServerlessConnection(...`が`client.connections.create_or_update(ServerlessConnection(...`に変更され、接続の作成および更新が可能であることを明示的に示しています。この変更により、ユーザーは既存の接続がある場合でも新たに作成する方法についての理解が深まります。

この変更は、サーバーレス接続を作成する際の手順を明確にし、より柔軟な操作を可能にするための重要なアップデートとなっています。全体として、ドキュメントが改善され、ユーザーエクスペリエンスが向上することを目的としています。

## articles/ai-studio/how-to/develop/connections-add-sdk.md{#item-14b519}

<details>
<summary>Diff</summary>
````diff
@@ -2,12 +2,12 @@
 title: How to add a new connection in AI Studio using the Azure Machine Learning SDK
 titleSuffix: Azure AI Studio
 description: This article provides instructions on how to add connections to other resources using the Azure Machine Learning SDK.
-manager: nitinme
+manager: scottpolly
 ms.service: azure-ai-studio
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 9/12/2024
 ms.reviewer: dantaylo
 ms.author: larryfr
 author: Blackmist
@@ -31,6 +31,16 @@ Connections are a way to authenticate and consume both Microsoft and other resou
 
 [!INCLUDE [SDK setup](../../includes/development-environment-config.md)]
 
+## Authenticating with Microsoft Entra ID
+
+There are various authentication methods for the different connection types. When you use Microsoft Entra ID, in addition to creating the connection you might also need to grant Azure role-based access control permissions before the connection can be used. For more information, visit [Role-based access control](../../concepts/rbac-ai-studio.md#scenario-connections-using-microsoft-entra-id-authentication).
+
+> [!IMPORTANT]
+> We recommend Microsoft Entra ID authentication with [managed identities for Azure resources](/azure/active-directory/managed-identities-azure-resources/overview) to avoid storing credentials with your applications that run in the cloud.
+>
+> If you use an API key, store it securely somewhere else, such as in [Azure Key Vault](/azure/key-vault/general/overview). Don't include the API key directly in your code, and never post it publicly.
+
+
 ## Azure OpenAI Service
 
 The following example creates an Azure OpenAI Service connection.
@@ -44,14 +54,20 @@ from azure.ai.ml.entities import UsernamePasswordConfiguration
 
 name = "XXXXXXXXX"
 
-target = "https://XXXXXXXXX.cognitiveservices.azure"
-api_key= "my-key"
+target = "https://XXXXXXXXX.cognitiveservices.azure.com/"
+
 resource_id= "Azure-resource-id"
 
+# Microsoft Entra ID
+credentials = None
+# Uncomment the following if you need to use API key instead
+# api_key= "my-key"
+# credentials = ApiKeyConfiguration(key=api_key)
+
 wps_connection = AzureOpenAIConnection(
     name=name,
     azure_endpoint=target,
-    credentials=ApiKeyConfiguration(key=api_key),
+    credentials=credentials,
     resource_id = resource_id,
     is_shared=False
 )
@@ -70,12 +86,17 @@ name = "my-ai-services"
 
 target = "https://XXXXXXXXX.cognitiveservices.azure.com/"
 resource_id=""
-api_key="XXXXXXXXX"
+
+# Microsoft Entra ID
+credentials = None
+# Uncomment the following if you need to use API key instead
+# api_key= "my-key"
+# credentials = ApiKeyConfiguration(key=api_key)
 
 wps_connection = AzureAIServicesConnection(
     name=name,
     endpoint=target,
-    credentials=ApiKeyConfiguration(key=api_key),
+    credentials=credentials,
     ai_services_resource_id=resource_id,
 )
 ml_client.connections.create_or_update(wps_connection)
@@ -90,13 +111,18 @@ from azure.ai.ml.entities import AzureAISearchConnection, ApiKeyConfiguration
 from azure.ai.ml.entities import UsernamePasswordConfiguration
 
 name = "my_aisearch_demo_connection"
-
 target = "https://XXXXXXXXX.search.windows.net"
-api_key="XXXXXXXXX"
+
+# Microsoft Entra ID
+credentials = None
+# Uncomment the following if you need to use API key instead
+# api_key= "my-key"
+# credentials = ApiKeyConfiguration(key=api_key)
+
 wps_connection = AzureAISearchConnection(
     name=name,
     endpoint=target,
-    credentials=ApiKeyConfiguration(key=api_key),
+    credentials=credentials,
 )
 ml_client.connections.create_or_update(wps_connection)
 ```
@@ -132,7 +158,7 @@ from azure.ai.ml.entities import ServerlessConnection
 
 name = "my_maas_apk"
 
-endpoint = "https://XXXXXXXXX.eastus2.inference.ai.azure.com"
+endpoint = "https://XXXXXXXXX.eastus2.inference.ai.azure.com/"
 api_key = "XXXXXXXXX"
 wps_connection = ServerlessConnection(
     name=name,
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Studioにおける接続の追加手順に関する更新"
}
```

### Explanation
このコードの変更は、Azure AI Studioでの接続を追加する手順に関するドキュメントの更新を示しています。変更の主要点は、接続の認証方法と新たな設定手順に関する情報が追加されたことです。

主な変更点は以下の通りです：

1. **記事の詳細な更新**:
   - 記事の管理者が`nitinme`から`scottpolly`に変更され、管理体制が見直されています。
   - 作成日も`5/21/2024`から`9/12/2024`に更新され、より最新の情報が反映されています。

2. **認証方法の追加**:
   - Microsoft Entra IDによる認証方法が新たに追加され、接続を作成する際に考慮すべき役割ベースのアクセス制御についての説明が含まれています。また、エンタープライズ環境での安全な認証方法を推奨し、アプリケーションの信頼性を向上させるためのベストプラクティスが提示されています。

3. **コード例の改良**:
   - 認証情報を格納するための`credentials`変数が導入され、APIキーの使用がオプションとして説明されるようになりました。これにより、より安全に接続を作成できる方法が強調されています。
   - 具体的なコード例においても、APIキーの直接的な使用を避けるためのコメントが追加され、その結果、コードの可読性とセキュリティが向上しています。

これらの変更は、Azure AI Studioを使用する開発者に対して、最新の機能とベストプラクティスを提供することを目的としており、ドキュメントの有用性を高めています。全体として、ユーザーが接続を追加する際の手順が明確化され、よりスムーズな実装が可能となっています。

## articles/ai-studio/how-to/fine-tune-model-llama.md{#item-2a42d8}

<details>
<summary>Diff</summary>
````diff
@@ -230,7 +230,7 @@ To fine-tune a Llama 2 model in an existing Azure AI Studio project, follow thes
 
     :::image type="content" source="../media/how-to/fine-tune/llama/llama-pay-as-you-go-overview.png" alt-text="Screenshot of pay-as-you-go marketplace overview." lightbox="../media/how-to/fine-tune/llama/llama-pay-as-you-go-overview.png":::
 
-1. Choose a base model to fine-tune and select **Confirm**. Your choice influences both the performance and [the cost of your model](./deploy-models-llama.md#cost-and-quota-considerations-for-meta-llama-family-of-models-deployed-as-serverless-api-endpoints).
+1. Choose a base model to fine-tune and select **Confirm**. Your choice influences both the performance and [the cost of your model](./deploy-models-llama.md#cost-and-quota-considerations-for-meta-llama-models-deployed-as-serverless-api-endpoints).
 
     :::image type="content" source="../media/how-to/fine-tune/llama/fine-tune-select-model.png" alt-text="Screenshot of option to select a model to fine-tune." lightbox="../media/how-to/fine-tune/llama/fine-tune-select-model.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Llamaモデルのファインチューニング手順の文言修正"
}
```

### Explanation
このコードの変更は、Azure AI StudioにおけるLlamaモデルのファインチューニング手順に関するドキュメントの更新を示しています。具体的には、手順内のリンク先の文言の修正が行われています。

主な変更点は以下の通りです：

1. **文言の修正**:
   - 「Meta Llama family of models deployed as serverless API endpoints」という表現が「Meta Llama models deployed as serverless API endpoints」に修正されました。この変更により、文脈がより明確になり、ユーザーが対象とするモデルファミリーが明示されました。

この変更は、特にファインチューニングを行う際のユーザーの理解を深め、関連情報にアクセスしやすくすることを目的としています。また、ドキュメント全体の一貫性が保たれ、ユーザーが必要とする情報をより迅速に取得できるよう支援しています。全体として、文書の正確性と明確さが向上することを目指したマイナーな更新です。

## articles/ai-studio/media/data-connections/connection-add-azure-ai-search-connect.png{#item-95a11f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search接続に関する画像の更新"
}
```

### Explanation
このコードの変更は、Azure AI Studioのデータ接続に関連する画像ファイルの更新を示しています。具体的には、`connection-add-azure-ai-search-connect.png`という画像が変更されていますが、変更の詳細は示されていません。

主なポイントは以下の通りです：

1. **画像の更新**:
   - 今回の変更では、画像自体の内容や形式についての具体的な追加や削除は行われていないものの、画像ファイルが新しいバージョンに置き換えられた可能性があります。これにより、ドキュメントにおけるビジュアルコンテンツの整合性や最新性が保たれることが期待されます。

この変更は、Azure AI Studioを使用するユーザーに対して、より正確で最新の情報を提供するためのものであり、視覚的なサポートが充実することで、ユーザーが接続手順を理解しやすくなることを目的としています。全体として、画像の保守管理を強化するためのマイナーな更新と言えるでしょう。

## articles/ai-studio/media/data-connections/connections-all-refreshed.png{#item-a17762}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ接続の全てが更新された画像の更新"
}
```

### Explanation
このコードの変更は、Azure AI Studioのデータ接続に関する画像ファイル`connections-all-refreshed.png`の更新を示しています。変更内容に追加や削除がなく、画像自体が新しいバージョンに置き換えられた可能性があります。

主なポイントは以下の通りです：

1. **画像の更新**:
   - 画像の表現や内容に関する具体的な変更は記載されていませんが、ファイルが新しいバージョンに置き換わることで、最新の情報やビジュアルコンテンツに改善が図られることが期待されます。

この変更は、ユーザーがAzure AI Studioのデータ接続についての理解を深めるための視覚的な支援を提供することを目的としており、ドキュメントの質を高めるために重要です。全体として、画像の信頼性と関連性を維持するためのマイナーな更新となっています。

## articles/ai-studio/reference/reference-model-inference-api.md{#item-9fe240}

<details>
<summary>Diff</summary>
````diff
@@ -539,7 +539,7 @@ catch (RequestFailedException ex)
 {
     if (ex.ErrorCode == "content_filter")
     {
-        Console.WriteLine($"Your query has trigger Azure Content Safeaty: {ex.Message}");
+        Console.WriteLine($"Your query has trigger Azure Content Safety: {ex.Message}");
     }
     else
     {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル推論APIドキュメントのマイナー修正"
}
```

### Explanation
このコードの変更は、`reference-model-inference-api.md`というドキュメントに対するマイナーな修正を示しています。この変更では、1つの行が修正されており、具体的には「Content Safeaty」という表記が「Content Safety」に訂正されています。

主なポイントは以下の通りです：

1. **誤記の修正**:
   - 元の文では「Content Safeaty」と誤って表記されていた部分が、正しい表記である「Content Safety」に修正されました。この修正により、ドキュメントの正確性と信頼性が向上します。

この変更は、テキストの明確さと正確性の向上を目的としたものであり、ユーザーが情報を正確に理解できるようにするための重要なステップです。全体としては、ドキュメントの内容を誤解を招かないようにするための小さな更新ですが、ユーザーにとっては図るべき重要な改善と言えます。


