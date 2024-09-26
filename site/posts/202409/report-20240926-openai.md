---
date: '2024-09-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:beebdfc...MicrosoftDocs:5e7dab7
summary: 最近のドキュメント更新では、主要なマイナーアップデートと新機能が導入されました。新たに「コンテンツフィルター設定可能性」に関するガイドが追加され、メタ情報の更新、リンクの修正、ドキュメント内容の刷新も行われました。破壊的な変更はなく、これらの改良によって、ユーザーに最新で使いやすい情報が提供され、ドキュメントの保守性が向上しています。特に、セキュリティに関するガイドが強化されており、より安全なデータの使用が推奨されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:beebdfc...MicrosoftDocs:5e7dab7){target="_blank"}

# ハイライト

最近のドキュメント更新では、主要なマイナーアップデートと1つの新しい機能が導入されました。これには、メタ情報の更新から、リンクの修正、新しいガイドの追加、および使用ガイドの内容刷新が含まれます。

## 新機能
- `articles/ai-services/openai/includes/content-filter-configurability.md`ファイルの新規追加。これにより、Azure OpenAIサービスでのコンテンツフィルター設定可能性に関する詳細なガイドが提供されます。

## 破壊的変更
破壊的な変更はありません。

## その他の更新
- メタデータ更新: `assistants-reference-messages.md`, `gpt-with-vision.md`, `content-filters.md`, `use-your-data-securely.md`, `faq.yml`, `cosmos-db.md`
- ドキュメント内容の簡略化と更新: `content-filter.md`
- タイトルと説明文の刷新: `how-to/content-filters.md`

# インサイト

この差分の主な目的は、ドキュメントをより保守しやすく、ユーザーにとって使いやすく、最新の情報を提供することです。以下に具体的な変更点とその意義を詳述します。

## メタデータの更新

`assistants-reference-messages.md`、`gpt-with-vision.md`、`content-filters.md`、`use-your-data-securely.md`、`faq.yml`、`cosmos-db.md` では、日付や著者情報などのメタデータがアップデートされました。これは、ドキュメントが最新であることを示し、信頼性を維持するためです。特に著者情報の更新は、最新の責任者に関する情報を反映するために重要です。

## ドキュメント内容の簡略化とリンク修正

`content-filter.md` では、内容の一部が削除され、インクルードステートメントが追加されました。これにより、重複する情報を排除し、情報の一元管理が可能となっています。リンク修正では、ユーザーが正確な情報に迅速にアクセスできるようにしました。

## 新しいガイドの追加

新たに追加された`content-filter-configurability.md`ファイルは、Azure OpenAIサービスでのコンテンツフィルター設定に関するガイドを詳述しています。フィルターの設定方法を明確にし、ユーザーの理解と活用を促進しています。特にフィルターの細かな設定ができることは、企業政策に合わせた柔軟な対応が可能となるため、ユーザーにとって非常に価値があります。

## 使用ガイドの内容刷新

多くのファイルで、タイトルや内容が刷新され、より具体的で明確になりました。例えば、`how-to/content-filters.md` のタイトルと説明文が、実際の使用方法により焦点を当てたものに変更されました。また、`use-your-data-securely.md` では、データの安全な使用方法に関する具体的なガイドが追加されています。これにより、ユーザーが最良のプラクティスを理解しやすくなっています。

## データセキュリティの強調

特にセキュリティ面での改善が目立ちます。例えば、`cosmos-db.md` では、Azure Cosmos DBとAzure OpenAIサービスを使用する際のセキュアな接続方法が強調されており、ユーザーが最適なセキュリティ設定を行うためのガイドが追加されています。

このような一連の変更は、ユーザーに対して最新で正確な情報を提供し、ドキュメント全体の保守性と使いやすさを大幅に向上させます。



# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [assistants-reference-messages.md](#item-1c8daa) | minor update | 記事のメタ情報の更新 | modified | 3 | 3 | 6 | 
| [content-filter.md](#item-dfc7e7) | minor update | コンテンツフィルタリングに関する情報の調整 | modified | 1 | 23 | 24 | 
| [gpt-with-vision.md](#item-991388) | minor update | GPT-4 Turbo with Visionに関する記述の更新 | modified | 4 | 3 | 7 | 
| [faq.yml](#item-6deb71) | minor update | GPT-4 Turbo with Visionの制限に関するリンクの修正 | modified | 1 | 1 | 2 | 
| [content-filters.md](#item-6f0627) | minor update | Azure OpenAIサービスにおけるコンテンツフィルターの更新 | modified | 18 | 19 | 37 | 
| [use-your-data-securely.md](#item-76e120) | minor update | データを安全に使用するためのガイドの更新 | modified | 16 | 11 | 27 | 
| [content-filter-configurability.md](#item-11f064) | new feature | コンテンツフィルターの設定可能性に関する新しいガイド | added | 41 | 0 | 41 | 
| [cosmos-db.md](#item-d6e2e5) | minor update | Cosmos DBに関するドキュメントの更新 | modified | 6 | 2 | 8 | 


# Modified Contents
## articles/ai-services/openai/assistants-reference-messages.md{#item-1c8daa}

<details>
<summary>Diff</summary>
````diff
@@ -5,9 +5,9 @@ description: Learn how to use Azure OpenAI's Python & REST API messages with Ass
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 07/25/2024
-author: mrbullwinkle
-ms.author: mbullwin
+ms.date: 09/25/2024
+author: aahill
+ms.author: aahi
 recommendations: false
 ms.custom: devx-track-python
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事のメタ情報の更新"
}
```

### Explanation
この変更では、`assistants-reference-messages.md`ファイル内のメタデータが更新されました。具体的には、`ms.date`、`author`、および`ms.author`のフィールドが修正されています。`ms.date`フィールドの日付が2024年7月25日から2024年9月25日に変更され、著者情報が`mrbullwinkle`から`aahill`に、著者のユーザー名が`mbullwin`から`aahi`に更新されました。このような小規模な変更は、記事の更新情報を最新のものに保つために重要です。

## articles/ai-services/openai/concepts/content-filter.md{#item-dfc7e7}

<details>
<summary>Diff</summary>
````diff
@@ -81,31 +81,9 @@ Detecting indirect attacks requires using document delimiters when constructing
 
 ## Configurability
 
-Azure OpenAI Service includes default safety settings applied to all models, excluding Azure OpenAI Whisper. These configurations provide you with a responsible experience by default, including content filtering models, blocklists, prompt transformation, [content credentials](../concepts/content-credentials.md), and others. [Read more about it here](/azure/ai-services/openai/concepts/default-safety-policies). All customers can also configure content filters and create custom safety policies that are tailored to their use case requirements. The configurability feature allows customers to adjust the settings, separately for prompts and completions, to filter content for each content category at different severity levels as described in the table below: 
+[!INCLUDE [content-filter-configurability](../includes/content-filter-configurability.md)]
 
-| Severity filtered | Configurable for prompts | Configurable for completions | Descriptions |
-|-------------------|--------------------------|------------------------------|--------------|
-| Low, medium, high | Yes | Yes | Strictest filtering configuration. Content detected at severity levels low, medium, and high is filtered.|
-| Medium, high      | Yes | Yes | Content detected at severity level low isn't filtered, content at medium and high is filtered.|
-| High              | Yes| Yes | Content detected at severity levels low and medium isn't filtered. Only content at severity level high is filtered. |
-| No filters | If approved<sup>1</sup>| If approved<sup>1</sup>| No content is filtered regardless of severity level detected. Requires approval<sup>1</sup>.|
-|Annotate only | If approved<sup>1</sup>| If approved<sup>1</sup>| Disables the filter functionality, so content will not be blocked, but annotations are returned via API response. Requires approval<sup>1</sup>.|
 
-<sup>1</sup> For Azure OpenAI models, only customers who have been approved for modified content filtering have full content filtering control and can turn off content filters. Apply for modified content filters via this form: [Azure OpenAI Limited Access Review: Modified Content Filters](https://ncv.microsoft.com/uEfCgnITdR) For Azure Government customers, please apply for modified content filters via this form: [Azure Government - Request Modified Content Filtering for Azure OpenAI Service](https://aka.ms/AOAIGovModifyContentFilter).
-
-Configurable content filters for inputs (prompts) and outputs (completions) are available for the following Azure OpenAI models:
-
-* GPT model series
-* GPT-4 Turbo Vision GA<sup>*</sup> (turbo-2024-04-09)
-* GPT-4o
-* GPT-4o mini
-* DALL-E 2 and 3
-
-<sup>*</sup>Only available for GPT-4 Turbo Vision GA, does not apply to GPT-4 Turbo Vision preview 
-
-Content filtering configurations are created within a Resource in Azure AI Studio, and can be associated with Deployments. [Learn more about configurability here](../how-to/content-filters.md).  
-
-Customers are responsible for ensuring that applications integrating Azure OpenAI comply with the [Code of Conduct](/legal/cognitive-services/openai/code-of-conduct?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext). 
 
 ## Scenario details
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングに関する情報の調整"
}
```

### Explanation
この変更では、`content-filter.md`ファイルにおけるコンテンツフィルタリングに関する情報が簡略化されました。具体的には、削除された23行のテキストにより、コンテンツフィルタリングの構成可能性や、各モデルに対するフィルタリングの可用性に関する詳細が削除されましたが、代わりにインクルードステートメント`[!INCLUDE [content-filter-configurability](../includes/content-filter-configurability.md)]`が追加されました。このインクルードにより、フィルタリングの設定に関する情報が外部リンクから取得され、全体の内容が軽量化され、最新情報を一元化することができます。これにより、文書の可読性と保守性が向上します。

## articles/ai-services/openai/concepts/gpt-with-vision.md{#item-991388}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,12 @@
 ---
 title: GPT-4 Turbo with Vision concepts
 titleSuffix: Azure OpenAI
-description: Learn about vision chats enabled by GPT-4 Turbo with Vision.
+description: Learn concepts related to using images in your AI model chats, enabled through GPT-4 Turbo with Vision and other models.
 author: PatrickFarley
 ms.author: pafarley
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 01/02/2024
+ms.date: 09/24/2024
 manager: nitinme
 ---
 
@@ -36,6 +36,7 @@ See the [Tokens section of the overview](/azure/ai-services/openai/overview#toke
 
 
 ### Example image price calculation
+
 > [!IMPORTANT]
 > The following content is an example only, and prices are subject to change in the future.
 
@@ -68,7 +69,7 @@ For a typical use case, take a 3-minute video with a 100-token prompt input. The
 
 Additionally, there's a one-time indexing cost of $0.15 to generate the Video Retrieval index for this 3-minute video. This index can be reused across any number of Video Retrieval and GPT-4 Turbo with Vision API calls.
 
-## Limitations
+## Input limitations
 
 This section describes the limitations of GPT-4 Turbo with Vision.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turbo with Visionに関する記述の更新"
}
```

### Explanation
この変更では、`gpt-with-vision.md`ファイル内のいくつかの記述が変更され、内容が更新されました。まず、`description`フィールドが具体的に「AIモデルチャットでの画像使用に関連する概念」に関する内容に改訂されました。また、日付が2024年1月2日から2024年9月24日に変更され、最新の情報を反映しています。

さらに、「例の画像価格計算」のセクションに重要な注意事項としての情報が追加され、新しいヘッダー「入力の制限」に置き換えられることで、コンテンツが視覚的に整理され、わかりやすくなっています。この更新によって、利用者にとっての文書の内容がより明確になり、最新の使用条件が反映されるようになりました。

## articles/ai-services/openai/faq.yml{#item-6deb71}

<details>
<summary>Diff</summary>
````diff
@@ -227,7 +227,7 @@ sections:
       - question: |
           What are the known limitations of GPT-4 Turbo with Vision?
         answer: |
-          See the [limitations](./concepts/gpt-with-vision.md#limitations) section of the GPT-4 Turbo with Vision concepts guide.
+          See the [limitations](./concepts/gpt-with-vision.md#input-limitations) section of the GPT-4 Turbo with Vision concepts guide.
       - question: |
           I keep getting truncated responses when I use GPT-4 Turbo vision models. Why is this happening?
         answer:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turbo with Visionの制限に関するリンクの修正"
}
```

### Explanation
この変更では、`faq.yml`ファイル内のGPT-4 Turbo with Visionに関するFAQの一部が更新されました。具体的には、GPT-4 Turbo with Visionの制限に関する回答のリンクが修正され、`#limitations`から`#input-limitations`セクションへと変更されました。これにより、ユーザーがより正確な情報にアクセスできるようになり、内容が最新のドキュメント構造に合わせて調整されました。この修正は、利用者が必要な情報を迅速に見つけるための助けとなります。

## articles/ai-services/openai/how-to/content-filters.md{#item-6f0627}

<details>
<summary>Diff</summary>
````diff
@@ -1,40 +1,39 @@
 ---
-title: 'How to use content filters (preview) with Azure OpenAI Service'
+title: 'Use content filters (preview) with Azure OpenAI Service'
 titleSuffix: Azure OpenAI
-description: Learn how to use content filters (preview) with Azure OpenAI Service.
+description: Learn how to use and configure the content filters that come with Azure OpenAI Service, including getting approval for gated modifications.
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 04/16/2024
+ms.date: 09/25/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
+ms.custom: FY25Q1-Linter
+# customer intent: As a developer, I want to learn how to configure content filters with Azure OpenAI Service so that I can ensure that my applications comply with our Code of Conduct.
 ---
 
 # How to configure content filters with Azure OpenAI Service
 
+The content filtering system integrated into Azure OpenAI Service runs alongside the core models, including DALL-E image generation models. It uses an ensemble of multi-class classification models to detect four categories of harmful content (violence, hate, sexual, and self-harm) at four severity levels respectively (safe, low, medium, and high), and optional binary classifiers for detecting jailbreak risk, existing text, and code in public repositories. The default content filtering configuration is set to filter at the medium severity threshold for all four content harms categories for both prompts and completions. That means that content that is detected at severity level medium or high is filtered, while content detected at severity level low or safe is not filtered by the content filters. Learn more about content categories, severity levels, and the behavior of the content filtering system [here](../concepts/content-filter.md). Jailbreak risk detection and protected text and code models are optional and off by default. For jailbreak and protected material text and code models, the configurability feature allows all customers to turn the models on and off. The models are by default off and can be turned on per your scenario. Some models are required to be on for certain scenarios to retain coverage under the [Customer Copyright Commitment](/legal/cognitive-services/openai/customer-copyright-commitment?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext).
+
 > [!NOTE]
 > All customers have the ability to modify the content filters and configure the severity thresholds (low, medium, high). Approval is required for turning the content filters partially or fully off. Managed customers only may apply for full content filtering control via this form: [Azure OpenAI Limited Access Review: Modified Content Filters](https://ncv.microsoft.com/uEfCgnITdR). At this time, it is not possible to become a managed customer.
 
-The content filtering system integrated into Azure OpenAI Service runs alongside the core models, including DALL-E image generation models. It uses an ensemble of multi-class classification models to detect four categories of harmful content (violence, hate, sexual, and self-harm) at four severity levels respectively (safe, low, medium, and high), and optional binary classifiers for detecting jailbreak risk, existing text, and code in public repositories. The default content filtering configuration is set to filter at the medium severity threshold for all four content harms categories for both prompts and completions. That means that content that is detected at severity level medium or high is filtered, while content detected at severity level low or safe is not filtered by the content filters. Learn more about content categories, severity levels, and the behavior of the content filtering system [here](../concepts/content-filter.md). Jailbreak risk detection and protected text and code models are optional and off by default. For jailbreak and protected material text and code models, the configurability feature allows all customers to turn the models on and off. The models are by default off and can be turned on per your scenario. Some models are required to be on for certain scenarios to retain coverage under the [Customer Copyright Commitment](/legal/cognitive-services/openai/customer-copyright-commitment?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext).
-
-Content filters can be configured at resource level. Once a new configuration is created, it can be associated with one or more deployments. For more information about model deployment, see the [resource deployment guide](create-resource.md).
+Content filters can be configured at the resource level. Once a new configuration is created, it can be associated with one or more deployments. For more information about model deployment, see the [resource deployment guide](create-resource.md).
 
-The configurability feature allows customers to adjust the settings, separately for prompts and completions, to filter content for each content category at different severity levels as described in the table below. Content detected at the 'safe' severity level is labeled in annotations but is not subject to filtering and isn't configurable.
+## Prerequisites
 
-| Severity filtered | Configurable for prompts | Configurable for completions | Descriptions |
-|-------------------|--------------------------|------------------------------|--------------|
-| Low, medium, high | Yes | Yes | Strictest filtering configuration. Content detected at severity levels low, medium, and high is filtered. |
-| Medium, high      | Yes | Yes | Content detected at severity level low isn't filtered, content at medium and high is filtered. |
-| High              | Yes| Yes | Content detected at severity levels low and medium isn't filtered. Only content at severity level high is filtered. |
-| No filters | If approved<sup>\*</sup>| If approved<sup>\*</sup>| No content is filtered regardless of severity level detected. Requires approval<sup>\*</sup>.|
-|Annotate only | If approved<sup>\*</sup>| If approved<sup>\*</sup>| Disables the filter functionality, so content will not be blocked, but annotations are returned via API response. Requires approval<sup>\*</sup>|
+* You must have an Azure OpenAI resource and a large language model (LLM) deployment to configure content filters. Follow a [quickstart](/azure/ai-services/openai/chatgpt-quickstart?) to get started.
 
-<sup>\*</sup> Only approved customers have full content filtering control and can turn the content filters partially or fully off. Managed customers only can apply for full content filtering control via this form: [Azure OpenAI Limited Access Review: Modified Content Filters](https://ncv.microsoft.com/uEfCgnITdR). At this time, it is not possible to become a managed customer.
+## Understand content filter configurability
 
-Customers are responsible for ensuring that applications integrating Azure OpenAI comply with the [Code of Conduct](/legal/cognitive-services/openai/code-of-conduct?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext). 
+[!INCLUDE [content-filter-configurability](../includes/content-filter-configurability.md)]
+ 
+## Understand other filters
 
+You can configure the following filter categories in addition to the default harm category filters.
 
 |Filter category  |Status |Default setting  |Applied to prompt or completion?  |Description  |
 |---------|---------|---------|---------|
@@ -44,7 +43,7 @@ Customers are responsible for ensuring that applications integrating Azure OpenA
 | Protected material - text | GA| On | Completion | Identifies and blocks known text content from being displayed in the model output (for example, song lyrics, recipes, and selected web content).  |
 
 
-## Configuring content filters via Azure OpenAI Studio
+## Configure content filters via Azure OpenAI Studio
 
 The following steps show how to set up a customized content filtering configuration for your resource.
 
@@ -101,11 +100,11 @@ The following steps show how to set up a customized content filtering configurat
     > [!NOTE]
     > Before deleting a content filtering configuration, you will need to unassign it from any deployment in the Deployments tab.
 
-## Best practices
+## Follow best practices
 
 We recommend informing your content filtering configuration decisions through an iterative identification (for example, red team testing, stress-testing, and analysis) and measurement process to address the potential harms that are relevant for a specific model, application, and deployment scenario. After you implement mitigations such as content filtering, repeat measurement to test effectiveness. Recommendations and best practices for Responsible AI for Azure OpenAI, grounded in the [Microsoft Responsible AI Standard](https://aka.ms/RAI) can be found in the [Responsible AI Overview for Azure OpenAI](/legal/cognitive-services/openai/overview?context=/azure/ai-services/openai/context/context).
 
-## Next steps
+## Related content
 
 - Learn more about Responsible AI practices for Azure OpenAI: [Overview of Responsible AI practices for Azure OpenAI models](/legal/cognitive-services/openai/overview?context=/azure/ai-services/openai/context/context).
 - Read more about [content filtering categories and severity levels](../concepts/content-filter.md) with Azure OpenAI Service.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスにおけるコンテンツフィルターの更新"
}
```

### Explanation
この変更は、`content-filters.md`ファイルにおけるAzure OpenAIサービスのコンテンツフィルターに関する情報を更新したものです。タイトルが「How to use content filters (preview)」から「Use content filters (preview)」に変更され、説明文もより具体的に「Azure OpenAIサービスに付属するコンテンツフィルターの使用および設定方法を学ぶ」内容に変わりました。また、日付が2024年4月16日から2024年9月25日に変更されています。

内容の改訂に伴い、コンテンツフィルタリングシステムの動作や設定方法に関する詳細な説明が追加されました。特に、フィルターの設定やカテゴリに関する情報が整理され、新たに「理解する他のフィルター」や「フィルタリング設定をAzure OpenAI Studioで構成する」セクションが設けられ、利用者がより簡単に情報を得られるようになっています。この変更により、ユーザーがフィルター設定の重要性や利用方法を理解しやすくなっています。

## articles/ai-services/openai/how-to/use-your-data-securely.md{#item-76e120}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-openai
 ms.topic: how-to
 author: aahill
 ms.author: aahi
-ms.date: 07/15/2024
+ms.date: 09/24/2024
 recommendations: false
 ---
 
@@ -83,6 +83,11 @@ If you are using a published [web app](./use-web-app.md), you need to redeploy i
 
 When using the API, pass the `filter` parameter in each API request. For example:
 
+> [!IMPORTANT]
+> The following is for example only. If you use an API key, store it securely somewhere else, such as in [Azure Key Vault](/azure/key-vault/general/overview). Don't include the API key directly in your code, and never post it publicly.
+
+For more information about AI services security, see [Authenticate requests to Azure AI services](/azure/ai-services/authentication).
+
 ```json
 {
     "messages": [
@@ -91,13 +96,13 @@ When using the API, pass the `filter` parameter in each API request. For example
             "content": "who is my manager?"
         }
     ],
-    "dataSources": [
+    "data_sources": [
         {
-            "type": "AzureCognitiveSearch",
+            "type": "azure_search",
             "parameters": {
-                "endpoint": "'$AZURE_AI_SEARCH_ENDPOINT'",
-                "key": "'$AZURE_AI_SEARCH_API_KEY'",
-                "indexName": "'$AZURE_AI_SEARCH_INDEX'",
+                "endpoint": "<AZURE_AI_SEARCH_ENDPOINT>",
+                "key": "<AZURE_AI_SEARCH_API_KEY>",
+                "index_name": "<AZURE_AI_SEARCH_INDEX>",
                 "filter": "my_group_ids/any(g:search.in(g, 'group_id1, group_id2'))"
             }
         }
@@ -152,13 +157,13 @@ To set the managed identities via the management API, see [the management API re
 ```json
 
 "identity": {
-  "principalId": "12345678-abcd-1234-5678-abc123def",
-  "tenantId": "1234567-abcd-1234-1234-abcd1234",
+  "principalId": "<YOUR-PRINCIPAL-ID>",
+  "tenantId": "<YOUR-TENNANT-ID>",
   "type": "SystemAssigned, UserAssigned", 
   "userAssignedIdentities": {
-    "/subscriptions/1234-5678-abcd-1234-1234abcd/resourceGroups/my-resource-group",
-    "principalId": "12345678-abcd-1234-5678-abcdefg1234", 
-    "clientId": "12345678-abcd-efgh-1234-12345678"
+    "/subscriptions/<YOUR-SUBSCIRPTION-ID>/resourceGroups/my-resource-group",
+    "principalId": "<YOUR-PRINCIPAL-ID>", 
+    "clientId": "<YOUR-CLIENT-ID>"
   }
 }
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データを安全に使用するためのガイドの更新"
}
```

### Explanation
この変更では、`use-your-data-securely.md`ファイルの内容が更新され、Azure OpenAIサービスを安全に利用するための情報が強化されました。変更点の一部として、日付が2024年7月15日から2024年9月24日に更新され、文中に重要な注意点が追加されました。具体的には、APIキーを安全に保管するためにAzure Key Vaultを利用することに関する注意喚起が行われています。また、データソースの表記が「dataSources」から「data_sources」に変更され、その後のパラメータも小文字の形式に統一されました。

さらに、`principalId`や`tenantId`などのサンプル値が具体的な値からプレースホルダーに置き換えられ、ユーザーが自分の情報を簡単に挿入できるようになっています。この更新は、ユーザーに安全なプラクティスを促し、データの取り扱いに関するガイダンスをより明確にすることを目的としています。

## articles/ai-services/openai/includes/content-filter-configurability.md{#item-11f064}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,41 @@
+---
+titleSuffix: Azure OpenAI
+#services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+author: PatrickFarley
+ms.author: pafarley
+ms.date: 09/25/2024
+recommendations: false
+---
+
+
+
+Azure OpenAI Service includes default safety settings applied to all models, excluding Azure OpenAI Whisper. These configurations provide you with a responsible experience by default, including content filtering models, blocklists, prompt transformation, [content credentials](../concepts/content-credentials.md), and others. [Read more about it here](/azure/ai-services/openai/concepts/default-safety-policies). 
+
+All customers can also configure content filters and create custom safety policies that are tailored to their use case requirements. The configurability feature allows customers to adjust the settings, separately for prompts and completions, to filter content for each content category at different severity levels as described in the table below. Content detected at the 'safe' severity level is labeled in annotations but is not subject to filtering and isn't configurable.
+
+| Severity filtered | Configurable for prompts | Configurable for completions | Descriptions |
+|-------------------|--------------------------|------------------------------|--------------|
+| Low, medium, high | Yes | Yes | Strictest filtering configuration. Content detected at severity levels low, medium, and high is filtered.|
+| Medium, high      | Yes | Yes | Content detected at severity level low isn't filtered, content at medium and high is filtered.|
+| High              | Yes| Yes | Content detected at severity levels low and medium isn't filtered. Only content at severity level high is filtered. |
+| No filters | If approved<sup>1</sup>| If approved<sup>1</sup>| No content is filtered regardless of severity level detected. Requires approval<sup>1</sup>.|
+|Annotate only | If approved<sup>1</sup>| If approved<sup>1</sup>| Disables the filter functionality, so content will not be blocked, but annotations are returned via API response. Requires approval<sup>1</sup>.|
+
+<sup>1</sup> For Azure OpenAI models, only customers who have been approved for modified content filtering have full content filtering control and can turn off content filters. Apply for modified content filters via this form: [Azure OpenAI Limited Access Review: Modified Content Filters](https://ncv.microsoft.com/uEfCgnITdR) For Azure Government customers, apply for modified content filters via this form: [Azure Government - Request Modified Content Filtering for Azure OpenAI Service](https://aka.ms/AOAIGovModifyContentFilter).
+
+Configurable content filters for inputs (prompts) and outputs (completions) are available for the following Azure OpenAI models:
+
+* GPT model series
+* GPT-4 Turbo Vision GA<sup>*</sup> (`turbo-2024-04-09`)
+* GPT-4o
+* GPT-4o mini
+* DALL-E 2 and 3
+
+<sup>*</sup>Only available for GPT-4 Turbo Vision GA, does not apply to GPT-4 Turbo Vision preview 
+
+Content filtering configurations are created within a Resource in Azure AI Studio, and can be associated with Deployments. [Learn more about configurability here](../how-to/content-filters.md).  
+
+Customers are responsible for ensuring that applications integrating Azure OpenAI comply with the [Code of Conduct](/legal/cognitive-services/openai/code-of-conduct?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext). 
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "コンテンツフィルターの設定可能性に関する新しいガイド"
}
```

### Explanation
この変更は、`content-filter-configurability.md`という新しいファイルの追加を含んでおり、Azure OpenAIサービスにおけるコンテンツフィルターの設定可能性についての詳しい情報が提供されています。このファイルでは、デフォルトの安全設定やユーザーが独自の安全ポリシーを設定する方法が説明されています。

具体的には、フィルターの厳しさを「低、中、高」と分類し、各レベルごとにプロンプトやレスポンスの設定が調整可能であることが示されています。また、フィルタリングの各オプションに対する説明が表形式で整理されており、顧客が自身のニーズに合わせて設定を行えることが強調されています。

このガイドは、Azure OpenAIモデルのユーザーにとって重要なリソースであり、特にフィルターの構成やカスタマイズがどのように行われるかを明確に示すことで、ユーザーの理解と活用を促進しています。さらに、顧客がコンテンツフィルタリングを適切に利用し、Azure OpenAIのコードオブコンダクトに従うことが求められている旨が記載されています。

## articles/ai-services/openai/references/cosmos-db.md{#item-d6e2e5}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI on your Azure Cosmos DB data Python &
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 03/12/2024
+ms.date: 09/24/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -93,10 +93,14 @@ Prerequisites:
 * Configure the role assignments from the user to the Azure OpenAI resource. Required role: `Cognitive Services OpenAI User`.
 * Install [Az CLI](/cli/azure/install-azure-cli) and run `az login`.
 * Define the following environment variables: `AzureOpenAIEndpoint`, `ChatCompletionsDeploymentName`,`ConnectionString`, `Database`, `Container`, `Index`, `EmbeddingDeploymentName`.
+
+> [!NOTE]
+> The following is for example only. If you use a connection string, store it securely somewhere else, such as in [Azure Key Vault](/azure/key-vault/general/overview). Don't include the API key directly in your code, and never post it publicly.
+
 ```bash
 export AzureOpenAIEndpoint=https://example.openai.azure.com/
 export ChatCompletionsDeploymentName=turbo
-export ConnectionString='mongodb+srv://username:***@example.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000'
+export ConnectionString='<db-connection-string>'
 export Database=testdb
 export Container=testcontainer
 export Index=testindex
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cosmos DBに関するドキュメントの更新"
}
```

### Explanation
この変更では、`cosmos-db.md`ファイルが更新され、Azure OpenAIをAzure Cosmos DBデータとともに使用する際の情報が強化されました。主な変更点として、最終更新日が2024年3月12日から2024年9月24日に更新され、ドキュメントの最新性が保たれています。

具体的には、ユーザーがセキュアに接続情報を管理することを促すための注意書きが追加されました。この中で、接続文字列を安全に保管する方法としてAzure Key Vaultの利用が推奨されています。また、APIキーをコードに直接含めたり、公開したりしないように注意を促す文言も追加されています。

さらに、接続文字列の例として、個人情報を伏せた形式（`<db-connection-string>`）が提供され、ユーザーが自身の適切な値に置き換えやすくなっています。この更新は、ユーザーがセキュアにAzure OpenAIとAzure Cosmos DBを統合する際のベストプラクティスを強調しています。


