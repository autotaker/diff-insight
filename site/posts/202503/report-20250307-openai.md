---
date: '2025-03-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:31c2d64...MicrosoftDocs:4d90f76
summary: 今回のドキュメント更新では、Azure OpenAIサービスに新機能が追加され、技術的な修正も行われました。新機能として、リクエストごとにカスタムコンテンツフィルタリングを設定できるリクエストヘッダーが導入され、使用方法がより理解しやすくなるようドキュメントが詳細化されました。また、JavaScriptサンプルコードのスペルミスが修正され、コードの信頼性が向上しました。その他、バッチ処理のUTF-8エンコーディングに関する制約が明記され、地域情報の更新や最新リリース情報が反映されました。全体として、ユーザーの利便性向上を目指した重要な変更が行われています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:31c2d64...MicrosoftDocs:4d90f76){target="_blank"}

# ハイライト

今回のドキュメント更新では、新機能の追加と共に技術的な修正が行われました。主な新機能としては、Azure OpenAIサービスでのリクエストごとにカスタムコンテンツフィルタリング設定を指定できるリクエストヘッダーが導入されました。また、バッチ処理やモデルマトリックスに関する情報の調整も含まれています。重要な修正点としては、JavaScriptサンプルコードのスペルミスが改善され、コードの信頼性が向上しています。

## 新機能
- リクエストごとにカスタムコンテンツフィルタリングが設定可能になりました。
- コンテンツフィルタリングに関するドキュメントの詳細化とエラーメッセージ情報の追加によって、使用方法の理解が深まりました。

## 破壊的変更

## その他の更新
- バッチ処理に関するUTF-8エンコーディングの制約が明記されました。
- カナダ中央リージョンに関するモデル情報が削除・更新されました。
- JavaScriptサンプルコードのスペルミスが修正されました。
- Azure OpenAIサービスの最新リリース情報が明確にされました。

# 洞察

今回の変更は、Azure OpenAIの機能とそのドキュメントの質を向上させるための重要な更新です。バッチ処理のエンコーディング制約追加によって、ユーザーはファイルの準備においてより適切な対応が求められるようになりました。これはシステム全体の効率性向上を意図していると考えられます。

コンテンツフィルタリング関連では、新しいリクエストヘッダー機能が導入されたことにより、ユーザーはより精密なリクエスト管理が可能となりました。API呼び出し時に特定のフィルタ設定を適用できるため、多様な業務ニーズに対応しやすくなります。この柔軟性は、セキュリティとカスタマイズ性が重視されるビジネスシーンで特に価値があります。

さらには、モデルマトリックスの地域情報更新やJSサンプルコードの修正など、小さなながらもユーザーの利便性を追求した改善が見受けられます。このような細部への注意は、開発者コミュニティとの信頼関係を深め、Azure OpenAIサービスの活用をより促進するものと言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [batch.md](#item-a131d5) | minor update | バッチ処理に関する制約の追加 | modified | 2 | 0 | 2 | 
| [content-filters.md](#item-6f0627) | minor update | コンテンツフィルタの使用に関する情報の強化 | modified | 41 | 4 | 45 | 
| [provisioned-global.md](#item-340884) | minor update | プロビジョニングされたグローバルモデルマトリックスの更新 | modified | 0 | 1 | 1 | 
| [provisioned-models.md](#item-8ee639) | minor update | プロビジョニングされたモデルの情報の更新 | modified | 0 | 1 | 1 | 
| [use-your-data-javascript.md](#item-786699) | bug fix | JavaScriptサンプルコードの修正 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-53303b) | minor update | Azure OpenAIサービスの最新リリース情報の追加 | modified | 7 | 1 | 8 | 


# Modified Contents
## articles/ai-services/openai/how-to/batch.md{#item-a131d5}

<details>
<summary>Diff</summary>
````diff
@@ -240,6 +240,8 @@ When a job failure occurs, you'll find details about the failure in the `errors`
 
 - Resources deployed with Azure CLI won't work out-of-box with Azure OpenAI global batch. This is due to an issue where resources deployed using this method have endpoint subdomains that don't follow the `https://your-resource-name.openai.azure.com` pattern. A workaround for this issue is to deploy a new Azure OpenAI resource using one of the other common deployment methods which will properly handle the subdomain setup as part of the deployment process.
 
+- UTF-8-BOM encoded `jsonl` files are not supported. JSON lines files should be encoded using UTF-8. Use of Byte-Order-Mark (BOM) encoded files is not officially supported by the JSON RFC spec, and Azure OpenAI will currently treat BOM encoded files as invalid. A UTF-8-BOM encoded file will currently return the generic error message: "Validation failed: A valid model deployment name could not be extracted from the input file. Please ensure that each row in the input file has a valid deployment name specified in the 'model' field, and that the deployment name is consistent across all rows."
+
 ## See also
 
 * Learn more about Azure OpenAI [deployment types](./deployment-types.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ処理に関する制約の追加"
}
```

### Explanation
この変更では、Azure OpenAIにおけるバッチ処理に関する重要な情報が文書に追加されました。具体的には、UTF-8-BOMエンコードされた`jsonl`ファイルがサポートされていない旨が明記され、JSON Lines ファイルはUTF-8でエンコードされるべきであることが説明されています。BOMエンコードされたファイルは、Azure OpenAIによって無効と見なされ、使用した場合には一般的なエラーメッセージが返されることが記載されています。この更新は、利用者が適切にファイルを準備し、エラーを回避できるように支援することを目的としています。また、関連するデプロイタイプについてのリンクも提供されています。

## articles/ai-services/openai/how-to/content-filters.md{#item-6f0627}

<details>
<summary>Diff</summary>
````diff
@@ -1,20 +1,20 @@
 ---
-title: 'Use content filters (preview) with Azure AI Foundry'
+title: 'Use content filters (preview)'
 titleSuffix: Azure OpenAI
 description: Learn how to use and configure the content filters that come with Azure AI Foundry, including getting approval for gated modifications.
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 12/05/2024
+ms.date: 03/05/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
 ms.custom: FY25Q1-Linter
 # customer intent: As a developer, I want to learn how to configure content filters with Azure AI Foundry so that I can ensure that my applications comply with our Code of Conduct.
 ---
 
-# How to configure content filters with Azure AI Foundry
+# How to configure content filters
 
 The content filtering system integrated into Azure AI Foundry runs alongside the core models, including DALL-E image generation models. It uses an ensemble of multi-class classification models to detect four categories of harmful content (violence, hate, sexual, and self-harm) at four severity levels respectively (safe, low, medium, and high), and optional binary classifiers for detecting jailbreak risk, existing text, and code in public repositories. 
 
@@ -45,10 +45,46 @@ You can configure the following filter categories in addition to the default har
 |Prompt Shields for indirect attacks  | GA| Off | User prompt | Filter / annotate Indirect Attacks, also referred to as Indirect Prompt Attacks or Cross-Domain Prompt Injection Attacks, a potential vulnerability where third parties place malicious instructions inside of documents that the generative AI system can access and process. Requires: [Document embedding and formatting](/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cuser-prompt%2Cpython-new#embedding-documents-in-your-prompt). |
 | Protected material - code |GA| On | Completion | Filters protected code or gets the example citation and license information in annotations for code snippets that match any public code sources, powered by GitHub Copilot. For more information about consuming annotations, see the [content filtering concepts guide](/azure/ai-services/openai/concepts/content-filter#annotations-preview) |
 | Protected material - text | GA| On | Completion | Identifies and blocks known text content from being displayed in the model output (for example, song lyrics, recipes, and selected web content).  |
-| Groundedness* | Preview |Off | Completion |Detects whether the text responses of large language models (LLMs) are grounded in the source materials provided by the users. Ungroundedness refers to instances where the LLMs produce information that is non-factual or inaccurate from what was present in the source materials. Requires: [Document embedding and formatting](/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cuser-prompt%2Cpython-new#embedding-documents-in-your-prompt).|
+| Groundedness | Preview |Off | Completion |Detects whether the text responses of large language models (LLMs) are grounded in the source materials provided by the users. Ungroundedness refers to instances where the LLMs produce information that is non-factual or inaccurate from what was present in the source materials. Requires: [Document embedding and formatting](/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cuser-prompt%2Cpython-new#embedding-documents-in-your-prompt).|
 
 [!INCLUDE [create-content-filter](../../../ai-foundry/includes/create-content-filter.md)]
 
+## Specify a content filtering configuration at request time (preview)
+
+In addition to the deployment-level content filtering configuration, we also provide a request header that allows you specify your custom configuration at request time for every API call. 
+
+```bash
+curl --request POST \ 
+    --url 'URL' \ 
+    --header 'Content-Type: application/json' \ 
+    --header 'api-key: API_KEY' \ 
+    --header 'x-policy-id: CUSTOM_CONTENT_FILTER_NAME' \ 
+    --data '{ 
+        "messages": [ 
+            { 
+                "role": "system", 
+                "content": "You are a creative assistant." 
+            }, 
+            { 
+                "role": "user", 
+                "content": "Write a poem about the beauty of nature." 
+            } 
+        ] 
+    }' 
+```
+
+The request-level content filtering configuration will override the deployment-level configuration, for the specific API call. If a configuration is specified that does not exist, the following error message will be returned. 
+
+```json
+{ 
+    "error": 
+        { 
+            "code": "InvalidContentFilterPolicy", 
+            "message": "Your request contains invalid content filter policy. Please provide a valid policy." 
+        } 
+} 
+```
+
 ## Report content filtering feedback
 
 If you are encountering a content filtering issue, select the **Filters Feedback** button at the top of the playground. This is enabled in the **Images, Chat, and Completions** playground once you submit a prompt. 
@@ -66,3 +102,4 @@ We recommend informing your content filtering configuration decisions through an
 - Learn more about Responsible AI practices for Azure OpenAI: [Overview of Responsible AI practices for Azure OpenAI models](/legal/cognitive-services/openai/overview?context=/azure/ai-services/openai/context/context).
 - Read more about [content filtering categories and severity levels](../concepts/content-filter.md) with Azure AI Foundry.
 - Learn more about red teaming from our: [Introduction to red teaming large language models (LLMs) article](../concepts/red-teaming.md).
+- Learn how to [configure content filters using the API](/rest/api/aiservices/accountmanagement/rai-policies/create-or-update)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタの使用に関する情報の強化"
}
```

### Explanation
この変更では、Azure AI Foundryにおけるコンテンツフィルタの使用方法についての文書が大幅に更新されました。主な変更点として、記事のタイトルが「Azure AI Foundryでのコンテンツフィルタの使用（プレビュー）」から「コンテンツフィルタの使用（プレビュー）」に変更され、日付が2024年12月5日から2025年3月5日に更新されました。

内容面では、コンテンツフィルタリングのシステムの詳細が強化され、フィルタのカテゴリや設定方法、さらにはリクエスト時にカスタム構成を指定する方法が新たに追加されました。特に、API呼び出しのたびに特定のフィルタ設定を指定できるリクエストヘッダーの使用に関する具体的な例が記載されています。また、新しいエラーメッセージの情報も含まれており、無効なコンテンツフィルタポリシーに対する返答がどうなるかも示されています。

さらに、コンテンツフィルタのフィードバックを報告する方法や、責任あるAIプラクティスに関するリソースへのリンクも新たに追加されています。この更新は、ユーザーがコンテンツフィルタを効果的に使用し、設定を行いやすくすることを目的としています。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,6 @@ ms.date: 03/04/2025
 |:-------------------|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
 | australiaeast      | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
 | brazilsouth        | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
-| canadacentral      | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
 | canadaeast         | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
 | eastus             | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
 | eastus2            | -                  | ✅                       | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされたグローバルモデルマトリックスの更新"
}
```

### Explanation
この変更では、Azure OpenAIのプロビジョニングされたグローバルモデルマトリックスに関するドキュメントが修正されました。具体的には、カナダの中央リージョン（canadacentral）の行が削除されました。これにより、全体のモデル利用可能性に関する情報が更新され、カナダの中央リージョンで利用できるサービスが視覚的に表示されなくなりました。この修正は、公式の文書におけるモデルの可用性情報を正確かつ最新のものに保つことを目的としています。

## articles/ai-services/openai/includes/model-matrix/provisioned-models.md{#item-8ee639}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,6 @@ ms.date: 02/28/2025
 |:-------------------|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|
 | australiaeast      | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | brazilsouth        | ✅                       | -                      | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | -                      |
-| canadacentral      | ✅                       | -                      | -                      | -                           | ✅                | -                       | -                       | -                           | ✅                    | -                      | ✅                       |
 | canadaeast         | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      |
 | eastus             | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
 | eastus2            | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされたモデルの情報の更新"
}
```

### Explanation
この変更では、Azure OpenAIにおけるプロビジョニングされたモデルの情報を含むドキュメントが更新されました。具体的には、カナダの中央リージョン（canadacentral）に関する行が削除されました。この削除により、カナダの中央リージョンにおける利用可能なサービスの可用性情報が更新され、正確性が保たれました。

この修正は、ユーザーがAzure OpenAIのモデルを利用する際に、正確な地域情報を把握できるようにすることを目指しています。このようなマトリックスの情報は、各リージョンでどのモデルがサポートされているかを把握するのに重要です。

## articles/ai-services/openai/includes/use-your-data-javascript.md{#item-786699}

<details>
<summary>Diff</summary>
````diff
@@ -48,7 +48,7 @@ ms.date: 01/10/2025
     
     // Set the Azure and AI Search values from environment variables
     const endpoint = process.env.AZURE_OPENAI_ENDPOINT || "Your endpoint";
-    const searchEndpoint = process.enV.AZURE_AI_SEARCH_ENDPOINT || "Your search endpoint";
+    const searchEndpoint = process.env.AZURE_AI_SEARCH_ENDPOINT || "Your search endpoint";
     const searchIndex = process.env.AZURE_AI_SEARCH_INDEX || "Your search index";
 
     // keyless authentication    
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "JavaScriptサンプルコードの修正"
}
```

### Explanation
この変更では、Azure OpenAIのデータ使用に関するJavaScriptサンプルコードが修正されました。具体的には、環境変数からAI Searchのエンドポイントを取得する際のコードにおけるスペルの誤りが修正されました。旧コードでは「process.enV」と表記されていましたが、正しい書き方は「process.env」です。この修正により、環境変数から正しくエンドポイントを取得できるようになり、コードの機能性が向上しました。

この変更は、ユーザーが提供されているサンプルコードを利用する際に、誤った記述によって発生するエラーを防ぐ重要な修正です。結果として、JavaScriptを使用した環境設定がスムーズに行えるようになります。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -11,14 +11,20 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: whats-new
-ms.date: 2/27/2025
+ms.date: 03/05/2025
 recommendations: false
 ---
 
 # What's new in Azure OpenAI Service
 
 This article provides a summary of the latest releases and major documentation updates for Azure OpenAI Service.
 
+## March 2025
+
+### Specify content filtering configurations 
+
+In addition to the deployment-level content filtering configuration, we now also provide a request header that allows you specify your custom configuration at request time for every API call. For more information, see [Use content filters (preview)](./how-to/content-filters.md#specify-a-content-filtering-configuration-at-request-time-preview).
+
 ## February 2025
 
 ### GPT-4.5 Preview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスの最新リリース情報の追加"
}
```

### Explanation
この変更では、Azure OpenAIサービスに関する「What's New」記事が更新され、最新のリリース情報と主要なドキュメントの更新が追加されました。具体的には、2025年3月に新たに導入された機能として、リクエストごとにカスタムのコンテンツフィルタリング設定を指定できるリクエストヘッダーが提供されることが紹介されています。この機能により、ユーザーはAPI呼び出しの際に、より詳細なコンテンツフィルタリングが可能になります。

また、記事の日付が2025年2月27日から2025年3月5日に変更され、最新の情報が反映されています。この更新は、Azure OpenAIサービスの使い方や新機能を理解するために重要なものであり、利用者が最新の機能を把握しやすくする助けとなります。


