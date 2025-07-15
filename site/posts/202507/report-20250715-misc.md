---
date: '2025-07-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bd40fd4...MicrosoftDocs:dbb4e58
summary: このコード差分は、Azure AIサービスにおけるドキュメントに対するマイナーな修正を含んでいます。主な更新内容は新機能の追加はないものの、既存の情報を明確に整理し、ユーザーにとって理解しやすくなっています。重大な変更は行われておらず、情報の精度と有用性が高められています。特に、Named
  Entity Recognition (NER)や個人情報検出、REST APIドキュメントにおいては、詳細な説明や具体例の追加が行われ、ユーザーエクスペリエンスの向上に貢献しています。これにより、Azure
  AIサービスの利用が促進されることが期待されます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bd40fd4...MicrosoftDocs:dbb4e58){target="_blank"}

# Highlights
このコード差分は、Azure AIサービスにおける複数のドキュメントについてのマイナーな修正を含んでいます。主な更新は以下の通りです：

## New features
特に新機能の導入は見られませんが、既存の情報をより明確にし、ユーザーにとって理解しやすいようにアップデートが行われています。

## Breaking changes
重大な変更や後方互換性を損なうような変更は含まれていません。

## Other updates
- Named Entity Recognition (NER) の概要がアップデートされ、責任あるAIに関する説明が詳しくなりました。
- 個人情報 (PII) 検出サポート言語に関する情報が、より明確に構造化され、最新版のモデルのサポート言語が追加されました。
- 感情分析のリソース割り当てとアンマウントに関するREST APIドキュメントのリソースIDの形式が更新され、具体的な例が示されました。

# Insights
この変更は、Azure AIサービスにおけるドキュメントの精度と有用性を高めるための小規模な修正を施しています。特に以下の点が注目されます：

NERに関するドキュメントでは、日付の更新に加えて、文体の修正や責任あるAIに関する記述が詳しく追加されたことにより、利用者にとっての情報価値が向上しています。これは、サービスを提供する際の信頼性向上やコンプライアンスの側面から重要な意味を持つと考えられます。

また、PII検出のドキュメントでは、言語サポートに関する箇条書き形式の導入により、情報がより一貫性を持って整理され、読みやすくなる努力が見られます。これにより、ユーザーは自身のニーズに応じた情報を迅速に取得できるようになり、実用的なサポートが強化されました。

さらに、REST API関連のドキュメントにおいては、リソースIDの具体的な例が示されることで、実際の実装においてユーザーが直面するであろう疑問を解決し、開発者の利便性を向上させる意図が明確です。これらの修正は、ユーザーエクスペリエンスの向上に寄与し、結果的にAzure AIサービスの利用拡大を支援するものと見られます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [overview.md](#item-c2e78b) | minor update | named-entity-recognitionの概要の更新 | modified | 9 | 11 | 20 | 
| [language-support.md](#item-d332b1) | minor update | 個人情報（PII）検出言語サポートの更新 | modified | 18 | 4 | 22 | 
| [assign-resources.md](#item-5d6080) | minor update | リソースIDの例を更新 | modified | 1 | 1 | 2 | 
| [unassign-resources.md](#item-05bc52) | minor update | リソースIDの例を更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/language-service/named-entity-recognition/overview.md{#item-c2e78b}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 02/15/2025
+ms.date: 07/14/2025
 ms.author: lajanuar
 ms.custom: language-service-ner
 ---
@@ -19,31 +19,29 @@ Named Entity Recognition (NER) is one of the features offered by [Azure AI Langu
 * [**How-to guides**](how-to-call.md) contain instructions for using the service in more specific or customized ways.
 * The [**conceptual articles**](concepts/named-entity-categories.md) provide in-depth explanations of the service's functionality and features.
 
-> [!NOTE]
-> [Entity Resolution](concepts/entity-resolutions.md) was upgraded to the [Entity Metadata](concepts/entity-metadata.md) starting in API version 2023-04-15-preview. If you're calling the preview version of the API equal or newer than 2023-04-15-preview, check out the [Entity Metadata](concepts/entity-metadata.md) article to use the resolution feature.
-
 [!INCLUDE [Typical workflow for pre-configured language features](../includes/overview-typical-workflow.md)]
 
 ## Get started with named entity recognition
 
 [!INCLUDE [development options](./includes/development-options.md)]
 
-[!INCLUDE [Developer reference](../includes/reference-samples-text-analytics.md)] 
+[!INCLUDE [Developer reference](../includes/reference-samples-text-analytics.md)]
 
-## Responsible AI 
+## Responsible AI
 
-An AI system includes not only the technology, but also the people who use it, the people who are affected by it, and the environment in which it's deployed. Read the [transparency note for NER](/azure/ai-foundry/responsible-ai/language-service/transparency-note-named-entity-recognition) to learn about responsible AI use and deployment in your systems. You can also see the following articles for more information:
+An AI system consists of more than just its core technology. It also includes the people who operate it, the people its use affects, and the broader deployment context.
+All these interconnected elements shape the effectiveness and outcomes of AI. Read the [transparency note for NER](/azure/ai-foundry/responsible-ai/language-service/transparency-note-named-entity-recognition) to learn about responsible AI use and deployment in your systems. For more information, *see* the following articles:
 
 [!INCLUDE [Responsible AI links](../includes/overview-responsible-ai-links.md)]
 
 ## Scenarios
 
-*	Enhance search capabilities and search indexing - Customers can build knowledge graphs based on entities detected in documents to enhance document search as tags.
-*	Automate business processes - For example, when reviewing insurance claims, recognized entities like name and location could be highlighted to facilitate the review. Or a support ticket could be generated with a customer's name and company automatically from an email.
-*	Customer analysis – Determine the most popular information conveyed by customers in reviews, emails, and calls to determine the most relevant topics that get brought up and determine trends over time. 
+* **Enhance search capabilities and search indexing**. Customers can build knowledge graphs based on entities detected in documents to enhance document search as tags.
+* **Automate business processes** - Insurance claims, recognized entities like name and location can be highlighted to facilitate review. Support tickets can be automatically generated with customer name and company from an email.
+* **In-depth customer analysis**. Determine the most popular information conveyed by customers in reviews, emails, and calls to determine relevant topics and trends over time.
 
 ## Next steps
 
 There are two ways to get started using the Named Entity Recognition (NER) feature:
 * [Azure AI Foundry](../../../ai-foundry/what-is-azure-ai-foundry.md) is a web-based platform that lets you use several Language service features without needing to write code.
-* The [quickstart article](quickstart.md) for instructions on making requests to the service using the REST API and client library SDK.  
+* The [quickstart article](quickstart.md) for instructions on making requests to the service using the REST API and client library SDK.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "named-entity-recognitionの概要の更新"
}
```

### Explanation
この変更は、AIサービスにおけるNamed Entity Recognition（NER）の概要記事に対するマイナーな更新です。主な変更点として、日付の更新（2025年2月15日から2025年7月14日へ）が含まれ、新たに内容が追加されている部分もあります。特に、責任あるAIに関する説明がより詳細に記述され、シナリオの項目では具体的な機能説明が文体を整えられ、見やすくなりました。また、一部の文が簡潔に再構成され、情報の伝達がより効果的になっています。

全体として、変更は記事を理解しやすくし、利用者にとっての価値を高めることを目的としています。リンクやリファレンスの項目も見直され、ユーザーが必要な情報に迅速にアクセスできるよう配慮されています。

## articles/ai-services/language-service/personally-identifiable-information/language-support.md{#item-d332b1}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Personally Identifiable Information (PII) detection language support
 titleSuffix: Azure AI services
-description: This article explains which natural languages are supported by the PII detection feature of Azure AI Language.
+description: This article explains which natural languages the PII detection feature supports of Azure AI Language.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
@@ -11,9 +11,10 @@ ms.author: lajanuar
 ms.custom: language-service-pii, build-2024
 ---
 
-# Personally Identifiable Information (PII) detection language support 
+# Personally Identifiable Information (PII) detection language support
+
+Use this article to learn which natural languages text PII, document PII, and conversation PII features support.
 
-Use this article to learn which natural languages are supported by the text PII, document PII, and conversation PII features of Azure AI Language Service.
 # [Text PII](#tab/text)
 
 ## Text PII language support
@@ -190,7 +191,20 @@ Use this article to learn which natural languages are supported by the text PII,
 
 ## PII language support
 
-The Generally Available Conversational PII service currently supports English. Preview model version `2023-04-15-preview` supports English, German, Spanish, and French. 
+PII conversation preview version `2023-04-15-preview` supports the following languages:
+
+* English
+* French
+* German
+* Spanish
+
+
+PII conversation generally available (GA) version currently supports the following languages:
+
+* English
+* French
+* Spanish
+
 
 
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人情報（PII）検出言語サポートの更新"
}
```

### Explanation
この変更は、Azure AI Languageの個人情報（PII）検出機能に関連する言語サポートを示す記事のマイナーアップデートです。主な変更点には、説明文の若干の文言修正が含まれ、「文書PII、会話PII、テキストPII」がサポートされる言語についてより明確な表現がされています。

また、PII検出の会話機能に関する情報を明確にするために、サポートされる言語のリストが箇条書き形式で整理され、利用者にとって理解しやすく構造化されました。具体的には、最新版（2023年4月15日）のモデルについて支援される言語の詳細が追加され、ユーザーが利用可能な機能をより簡単に把握できるよう工夫されています。

このアップデートにより、読者がPII検出機能の言語サポートに関する情報を容易に理解できるようになり、Azure AIサービスの利用を促進することを目的としています。

## articles/ai-services/language-service/sentiment-opinion-mining/includes/custom/rest-api/assign-resources.md{#item-5d6080}

<details>
<summary>Diff</summary>
````diff
@@ -50,7 +50,7 @@ Use the following sample JSON as your body.
 
 |Key  |Placeholder  |Value  | Example |
 |---------|---------|----------|--|
-| `azureResourceId` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to assign. Found in the Azure portal under the **Properties** tab for the resource, in the **Resource ID** field. | `/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
+| `azureResourceId` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to assign. Found in the Azure portal under the **Properties** tab for the resource, in the **Resource ID** field. | `/subscriptions/a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
 | `customDomain` | `{CUSTOM-DOMAIN}` | The custom subdomain of the resource you want to assign. Found in the Azure portal under the **Keys and Endpoint** tab for the resource, as the **Endpoint** field in the URL `https://<your-custom-subdomain>.cognitiveservices.azure.com/` | `contosoresource`  |
 | `region` | `{REGION-CODE}` |  A region code specifying the region of the resource you want to assign. Found in the Azure portal under the **Keys and Endpoint** tab for the resource, in the **Location/Region** field. |`eastus`|
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースIDの例を更新"
}
```

### Explanation
この変更は、Azure AIの感情分析機能に関連するREST APIリソース割り当てのドキュメントにおけるマイナーな更新です。具体的には、`azureResourceId`の例として示されているリソースIDが新しい形式に更新され、より正確な情報が提供されています。

以前はplaceholderとして表示されていたリソースIDの部分が、特定のサブスクリプションに基づいた新しいリソースIDに更新されました。この変更は、ユーザーがリソースを正確に割り当てる際により具体的で実用的な例を提供することを目指しています。

全体として、この修正はファイル内の情報を最新のものにすることで、利用者に対して分かりやすく、役立つガイドラインを提示することに貢献しています。

## articles/ai-services/language-service/sentiment-opinion-mining/includes/custom/rest-api/unassign-resources.md{#item-05bc52}

<details>
<summary>Diff</summary>
````diff
@@ -48,7 +48,7 @@ Use the following sample JSON as your body.
 
 |Key  |Placeholder  |Value  | Example |
 |---------|---------|----------|--|
-| `assignedResourceIds` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to unassign. Found in the Azure portal under the _Properties_ tab for the resource as the _Resource ID_ field. | `/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
+| `assignedResourceIds` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to unassign. Found in the Azure portal under the _Properties_ tab for the resource as the _Resource ID_ field. | `/subscriptions/a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
 
 ### Get unassign resource status
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースIDの例を更新"
}
```

### Explanation
この変更は、Azure AIの感情分析機能に関連するREST APIリソースのアンマウントに関するドキュメントに対するマイナーな更新です。具体的には、`assignedResourceIds`フィールドに示されるリソースIDの例が新しい形式に修正されました。

変更前の例はプレースホルダーとして表記されていましたが、更新後の例では特定のサブスクリプションに基づいた新しいリソースIDが提供され、使用する際の明確性が向上しています。この修正により、ユーザーはリソースをアンマウントする際に必要な正しい情報をより容易に理解できるようになります。

全体として、この修正はファイル内の情報の正確性を高めることを目的としており、利用者がAzureポータルで必要なリソースを正しく扱えるように支援しています。


