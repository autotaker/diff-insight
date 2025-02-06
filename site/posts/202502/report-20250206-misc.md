---
date: '2025-02-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d46a0e8...MicrosoftDocs:ea9b000
summary: このコードの差分は、Azure AIのドキュメントに関する小規模更新と新機能の追加を含んでいます。主に、ドキュメントの修正や情報の整理、リンクの更新が行われ、新たにサーバーレスAPIに関連するコンテンツ安全性に関する注記やセクションも追加されました。新機能としては、コンテンツ安全性と危険カテゴリについての詳細なセクションが新たに追加され、ユーザーがリスクを把握しやすくなっています。また、既存のリンクが変更されているため、その影響を確認する必要があります。全体的に、ドキュメントの可読性向上とユーザビリティの改善が図られています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d46a0e8...MicrosoftDocs:ea9b000){target="_blank"}

<format>
# ハイライト
このコードの差分は、Azure AIのドキュメントに関する一連の小規模更新と新機能の追加を示しています。主に、ドキュメントの修正、情報の整理、リンクの更新、そしてサーバーレスAPIに関連するコンテンツ安全性に関する新しい注記やセクションの追加が行われています。新機能としては、コンテンツの安全性と危険カテゴリについての詳細なセクションが追加されました。

## 新機能
- コンテンツ安全性と危険カテゴリに関する新しいセクションが追加されました。これにより、ユーザーは、さまざまな危険カテゴリに関連する詳細情報を取得しやすくなります。
- サーバーレスAPIに関するコンテンツ安全性の注記が新たに追加され、適用範囲が明確になりました。

## 破壊的変更
- 特に目立った破壊的変更はありませんが、リンクの更新によりアクセス方法が変更されているため、既存のリンクを参照している場合にその影響を確認する必要があります。

## その他の更新
- ドキュメント内の説明やテキストが見直され、より簡潔で明確な表現に統一されています。
- 目次ファイル（toc.yml）において、サーバーレスAPI関連の情報へのリンクが整理・追加されています。

# インサイト
このコードの修正は、Azure AIを利用するユーザーがより明確で簡潔な情報を取得できるようにすることを目的としています。主に、ドキュメント内の情報の可読性向上やアクセスしやすさ、そしてサーバーレスAPIによるモデルのコンテンツ安全性への理解を深めるための言及が含まれています。

多くの文書で共通して行われた変更は、冗長な情報の削除と`[!INCLUDE]`構文による情報の一元化です。これにより、ユーザーは重要な内容を素早く確認でき、全体の情報整理が進み、他のドキュメントとのコンシステンシーが高まりました。

新機能としては、コンテンツの安全性を強化し、ユーザーがよりコンテンツの使い方やリスクを把握できるような新しいセクションが追加されています。この新しいセクションは、特に危険カテゴリの理解を促進し、リスクの管理を容易にするための重要なリソースとして機能します。

これらの変更は、Azure AIを活用する開発者やユーザーにとって、コンテンツ安全性の確保やナビゲーションのしやすさを大いに改善するものであり、全体のユーザビリティを向上させることに大きく寄与しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [whats-new.md](#item-1ec8d3) | minor update | ドキュメントインテリジェンスの更新情報の修正 | modified | 3 | 3 | 6 | 
| [content-safety-overview.md](#item-2c67e3) | minor update | コンテンツ安全の概要に関する文書の修正 | modified | 3 | 21 | 24 | 
| [content-filtering.md](#item-91b372) | minor update | コンテンツフィルタリングに関する文書の修正 | modified | 1 | 1 | 2 | 
| [model-catalog-content-safety.md](#item-0d1e57) | new feature | サーバーレスAPIを使用したモデルのためのコンテンツ安全性 | added | 49 | 0 | 49 | 
| [deploy-models-cohere-command.md](#item-3e97f4) | minor update | Azure AIコンテンツ安全設定の情報更新 | modified | 8 | 8 | 16 | 
| [deploy-models-deepseek.md](#item-7c33de) | minor update | Azure AIコンテンツ安全設定に関する情報更新 | modified | 8 | 8 | 16 | 
| [deploy-models-gretel-navigator.md](#item-2e9806) | minor update | Azure AIコンテンツ安全設定に関するノートの更新 | modified | 4 | 4 | 8 | 
| [deploy-models-jais.md](#item-0bd11f) | minor update | Azure AIコンテンツ安全設定に関する情報の更新 | modified | 7 | 8 | 15 | 
| [deploy-models-llama.md](#item-6274a7) | minor update | ニューラルネットワークモデルデプロイメントに関するコンテンツの更新 | modified | 4 | 16 | 20 | 
| [deploy-models-mistral-codestral.md](#item-83ba03) | minor update | MistralとCodestalモデルデプロイメントに関するコンテンツの更新 | modified | 8 | 8 | 16 | 
| [deploy-models-mistral-nemo.md](#item-e7b729) | minor update | MistralとNemoモデルデプロイメントに関するコンテンツの更新 | modified | 8 | 8 | 16 | 
| [deploy-models-mistral.md](#item-487a41) | minor update | Mistralモデルデプロイメントに関するコンテンツの更新 | modified | 7 | 8 | 15 | 
| [deploy-models-phi-3-5-vision.md](#item-8d6d7d) | minor update | Phi 3.5 Visionモデルデプロイメントに関するコンテンツの更新 | modified | 4 | 16 | 20 | 
| [deploy-models-phi-3.md](#item-47e305) | minor update | Phi 3モデルデプロイメントに関するコンテンツの更新 | modified | 4 | 17 | 21 | 
| [deploy-models-phi-4.md](#item-c40212) | minor update | Phi 4モデルデプロイメントに関するコンテンツの更新 | modified | 4 | 16 | 20 | 
| [deploy-models-tsuzumi.md](#item-d3fd51) | minor update | Tsuzumiモデルデプロイメントに関するコンテンツの更新 | modified | 7 | 8 | 15 | 
| [deploy-cxrreportgen.md](#item-377d15) | minor update | CXRReportGenモデルに関する文書の簡略化 | modified | 0 | 2 | 2 | 
| [deploy-medimageinsight.md](#item-e9ab9e) | minor update | MedImageInsightモデルに関する文書の簡略化 | modified | 0 | 2 | 2 | 
| [deploy-medimageparse.md](#item-611e84) | minor update | MedImageParseモデルに関する文書の簡略化 | modified | 0 | 2 | 2 | 
| [healthcare-ai-models.md](#item-12fcfc) | minor update | ヘルスケアAIモデルに関する文書の簡略化 | modified | 0 | 2 | 2 | 
| [model-catalog-overview.md](#item-278001) | minor update | モデルカタログの表現の改善 | modified | 2 | 2 | 4 | 
| [content-safety-harm-categories.md](#item-8ef139) | new feature | コンテンツ安全性および危険カテゴリの理解 | added | 29 | 0 | 29 | 
| [content-safety-serverless-apis-note.md](#item-779e7e) | new feature | サーバーレスAPIに関するコンテンツ安全性の注記 | added | 13 | 0 | 13 | 
| [content-safety-serverless-models.md](#item-8fe192) | minor update | サーバーレスモデルにおけるコンテンツ安全性のリンク更新 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-2745cd) | minor update | サーバーレスAPIモデルのコンテンツ安全性に関するリンク追加 | modified | 6 | 2 | 8 | 


# Modified Contents
## articles/ai-services/document-intelligence/whats-new.md{#item-1ec8d3}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: whats-new
-ms.date: 01/14/2025
+ms.date: 02/05/2025
 ms.author: lajanuar
 ms.custom:
   - references_regions
@@ -29,7 +29,7 @@ Document Intelligence service is updated on an ongoing basis. Bookmark this page
 
 ## December 2024
 
-**Document Intelligence v4.0 programming language SDKs are now generally available (GA)**! <br><br>The latest client libraries default to the [**2024-11-30 REST API (GA)**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30&preserve-view=true) version of the service.<br><br>
+**Document Intelligence v4.0 programming language SDKs are now generally available (GA)**! <br><br>The latest client libraries default to the [**2024-11-30 REST API (GA)**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) version of the service.<br><br>
 For more information, *see* client libraries for the following supported programming languages:
 
 * [🆕 .NET (C#)](versioning/changelog-release-history.md?view=doc-intel-4.0.0&tabs=csharp&preserve-view=true)
@@ -76,7 +76,7 @@ For more information, *see* client libraries for the following supported program
 *  [🆕 US Tax model](prebuilt/tax-document.md)
    *  New prebuilt tax models added for 1095A, 1095C, 1099SSA, and W4.
 
-* [Delete analyze response](https://learn.microsoft.com/rest/api/aiservices/document-models/delete-analyze-result?view=rest-aiservices-v4.0%20(2024-11-30)&tabs=HTTP)
+* [Delete analyze response](/rest/api/aiservices/document-models/delete-analyze-result?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true&tabs=HTTP)
   * Analyze response is stored for 24 hours from when the operation completes for retrieval. For scenarios where you want to delete the response sooner, use the delete analyze response API to delete the response.  
 
 * The v4.0 API includes cumulative updates from preview releases as listed:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスの更新情報の修正"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスサービスに関する「更新情報」ドキュメントの小規模な修正を含んでいます。具体的には、いくつかの日付やリンクの修正が行われています。

1. **日付の更新**: `ms.date` が「01/14/2025」から「02/05/2025」に変更され、最新の日付が反映されています。
2. **リンクの修正**: SDKが一般提供（GA）されたときのREST APIリンクが修正され、正しいURL形式が確保されています。これにより、ユーザーは最新のサービスバージョンにアクセスしやすくなります。例えば、古いリンク形式 (`/rest/api/...`) から、新しい形式に修正されています。
3. **テキストの整合性**: リストの内容において、対象のAPIエンドポイントに関しても更新が行われており、ユーザーが正確な情報にアクセスできるように配慮されています。

全体として、この差分は変更前と後で計6箇所（追加3、削除3）の変更があり、ユーザーにとってより有用な情報が提供されるようになっています。

## articles/ai-studio/ai-services/content-safety-overview.md{#item-2c67e3}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.author: pafarley
 author: PatrickFarley
 ---
 
-# Content Safety in Azure AI Foundry portal
+# Content safety in the Azure AI Foundry portal
 
 Azure AI Content Safety is an AI service that detects harmful user-generated and AI-generated content in applications and services. Azure AI Content Safety includes various APIs that allow you to detect and prevent the output of harmful content. The interactive Content Safety **try out** page in Azure AI Foundry portal allows you to view, explore, and try out sample code for detecting harmful content across different modalities. 
 
@@ -23,7 +23,7 @@ You can use Azure AI Content Safety for many scenarios:
 **Text content**: 
 - Moderate text content: This feature scans and moderates text content, identifying and categorizing it based on different levels of severity to ensure appropriate responses. 
 - Groundedness detection: This filter determines if the AI's responses are based on trusted, user-provided sources, ensuring that the answers are "grounded" in the intended material. Groundedness detection is helpful for improving the reliability and factual accuracy of responses. 
-- Protected material detection for text: This feature identifies protected text material, such as known song lyrics, articles, or other content, ensuring that the AI doesn’t output this content without permission. 
+- Protected material detection for text: This feature identifies protected text material, such as known song lyrics, articles, or other content, ensuring that the AI doesn't output this content without permission. 
 - Protected material detection for code: Detects code segments in the model's output that match known code from public repositories, helping to prevent uncredited or unauthorized reproduction of source code. 
 - Prompt shields: This feature provides a unified API to address "Jailbreak" and "Indirect Attacks": 
     - Jailbreak Attacks: Attempts by users to manipulate the AI into bypassing its safety protocols or ethical guidelines. Examples include prompts designed to trick the AI into giving inappropriate responses or performing tasks it was programmed to avoid. 
@@ -37,25 +37,7 @@ You can use Azure AI Content Safety for many scenarios:
 - Custom categories: Allows users to define specific categories for moderating and filtering content, tailoring safety protocols to unique needs. 
 - Safety system message: Provides a method for setting up a "System Message" to instruct the AI on desired behavior and limitations, reinforcing safety boundaries and helping prevent unwanted outputs. 
 
-## Understand harm categories
-
-### Harm categories
-
-| Category  | Description         |API term |
-| --------- | ------------------- | --- |
-| Hate and Fairness      | Hate and fairness harms refer to any content that attacks or uses discriminatory language with reference to a person or identity group based on certain differentiating attributes of these groups. <br><br>This includes, but is not limited to:<ul><li>Race, ethnicity, nationality</li><li>Gender identity groups and expression</li><li>Sexual orientation</li><li>Religion</li><li>Personal appearance and body size</li><li>Disability status</li><li>Harassment and bullying</li></ul> | `Hate` |
-| Sexual  | Sexual describes language related to anatomical organs and genitals, romantic relationships and sexual acts, acts portrayed in erotic or affectionate terms, including those portrayed as an assault or a forced sexual violent act against one’s will. <br><br> This includes but is not limited to:<ul><li>Vulgar content</li><li>Prostitution</li><li>Nudity and Pornography</li><li>Abuse</li><li>Child exploitation, child abuse, child grooming</li></ul>   | `Sexual` |
-| Violence  | Violence describes language related to physical actions intended to hurt, injure, damage, or kill someone or something; describes weapons, guns, and related entities. <br><br>This includes, but isn't limited to:  <ul><li>Weapons</li><li>Bullying and intimidation</li><li>Terrorist and violent extremism</li><li>Stalking</li></ul>  | `Violence` |
-| Self-Harm  | Self-harm describes language related to physical actions intended to purposely hurt, injure, damage one’s body or kill oneself. <br><br> This includes, but isn't limited to: <ul><li>Eating Disorders</li><li>Bullying and intimidation</li></ul>  | `SelfHarm` |
-
-### Severity levels 
-
-| Level | Description |
-| --- | ---|
-|Safe |Content might be related to violence, self-harm, sexual, or hate categories but the terms are used in general, journalistic, scientific, medical, and similar professional contexts, which are appropriate for most audiences. |
-|Low |Content that expresses prejudiced, judgmental, or opinionated views, includes offensive use of language, stereotyping, use cases exploring a fictional world (for example, gaming, literature) and depictions at low intensity.| 
-|Medium |Content that uses offensive, insulting, mocking, intimidating, or demeaning language towards specific identity groups, includes depictions of seeking and executing harmful instructions, fantasies, glorification, promotion of harm at medium intensity. |
-|High |Content that displays explicit and severe harmful instructions, actions, damage, or abuse; includes endorsement, glorification, or promotion of severe harmful acts, extreme or illegal forms of harm, radicalization, or nonconsensual power exchange or abuse. |
+[!INCLUDE [content-safety-harm-categories](../includes/content-safety-harm-categories.md)]
 
 ## Limitations
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツ安全の概要に関する文書の修正"
}
```

### Explanation
この変更は、Azure AI Foundryポータルにおけるコンテンツの安全性に関する文書の小規模な修正です。具体的には、タイトルの変更といくつかのセクションの削除を含んでいます。

1. **タイトルの修正**: ドキュメントのタイトルが「Content Safety in Azure AI Foundry portal」から「Content safety in the Azure AI Foundry portal」へと微調整され、文書全体の一貫性が向上しています。
2. **セクションの削除**: 「危害カテゴリ」や「深刻度レベル」に関する詳細な説明が削除され、より簡潔な内容に再構成されています。これにより、ページの可読性が向上し、重要な情報に焦点を合わせることができるようになっています。
3. **情報の簡素化**: 削除された部分は重要な内容ではありますが、全体としての情報量が減少し、ユーザーにとって必要な情報をすばやく見つけやすくなっています。

この変更により、コンテンツ安全に関する概要がより洗練され、ユーザーが迅速に理解しやすくなることを目的としています。

## articles/ai-studio/concepts/content-filtering.md{#item-91b372}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ Azure AI Foundry includes a content filtering system that works alongside core m
 
 This content filtering system is powered by [Azure AI Content Safety](../../ai-services/content-safety/overview.md), and it works by running both the prompt input and completion output through an ensemble of classification models aimed at detecting and preventing the output of harmful content. Variations in API configurations and application design might affect completions and thus filtering behavior.
 
-With Azure OpenAI model deployments, you can use the default content filter or create your own content filter (described later on). The default content filter is also available for other text models curated by Azure AI in the [model catalog](../how-to/model-catalog.md), but custom content filters aren't yet available for those models. Models available through **Models as a Service** have content filtering enabled by default and can't be configured.
+With Azure OpenAI model deployments, you can use the default content filter or create your own content filter (described later on).  Models available through **serverless APIs** have content filtering enabled by default. To learn more about the default content filter enabled for serverless APIs, see [Content safety for models curated by Azure AI in the model catalog](model-catalog-content-safety.md).
 
 ## Language support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングに関する文書の修正"
}
```

### Explanation
この変更は、Azure AI Foundryにおけるコンテンツフィルタリングに関する文書の小規模な修正を含んでいます。主な変更点は以下の通りです。

1. **文言の調整**: 「Models as a Service」という表現から「serverless APIs」という表現に変更され、提供されるサービスの種類をより正確に反映しています。この変更により、読者にとって理解しやすくなっています。
2. **情報の追加**: 新たに「serverless APIs」に関連するコンテンツフィルタリングの詳細が追加され、デフォルトのコンテンツフィルタに関する情報へリンクが示されています。具体的には、「コンテンツカタログ内のAzure AIによってキュレーションされたモデルのコンテンツ安全に関する情報」が新たに参照されています。

全体として、この修正はコンテンツフィルタリングの機能に関する文書をより明確にし、特定のサービスに対する情報を強調することを目的としています。

## articles/ai-studio/concepts/model-catalog-content-safety.md{#item-0d1e57}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,49 @@
+---
+title: Content safety for models curated by Azure AI in the model catalog
+titleSuffix: Azure AI Foundry
+description: Learn about content safety for models deployed using serverless APIs, using Azure AI Foundry.
+manager: scottpolly
+ms.service: azure-ai-foundry
+ms.topic: conceptual
+ms.date: 02/04/2025
+ms.author: mopeakande 
+author: msakande
+ms.reviewer: ositanachi
+reviewer: ositanachi
+ms.custom: 
+---
+
+# Content safety for models curated by Azure AI in the model catalog
+
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
+
+In this article, learn about content safety capabilities for models from the model catalog deployed using serverless APIs.
+
+
+## Content filter defaults
+
+Azure AI uses a default configuration of [Azure AI Content Safety](/azure/ai-services/content-safety/overview) content filters to detect harmful content across four categories including hate and fairness, self-harm, sexual, and violence for models deployed via serverless APIs. To learn more about content filtering (preview), see [Understand harm categories](#understand-harm-categories).
+
+The default content filtering configuration for text models is set to filter at the medium severity threshold, filtering any detected content at this level or higher. For image models, the default content filtering configuration is set at the low configuration threshold, filtering at this level or higher. For models deployed using the [Azure AI model inference service](../../ai-foundry/model-inference/how-to/configure-content-filters.md), you can create configurable filters by selecting the **Content filters** tab within the **Safety + security** page of the Azure AI Foundry portal.
+
+> [!TIP]
+> Content filtering (preview) isn't available for certain model types that are deployed via serverless APIs. These model types include embedding models and time series models.
+
+Content filtering (preview) occurs synchronously as the service processes prompts to generate content. You might be billed separately according to [Azure AI Content Safety pricing](https://azure.microsoft.com/pricing/details/cognitive-services/content-safety/) for such use. You can disable content filtering (preview) for individual serverless endpoints either:
+
+- When you first deploy a language model
+- Later, by selecting the content filtering toggle on the deployment details page
+
+Suppose you decide to use an API other than the [Azure AI Model Inference API](/azure/ai-studio/reference/reference-model-inference-api) to work with a model that is deployed via a serverless API. In such a situation, content filtering (preview) isn't enabled unless you implement it separately by using Azure AI Content Safety. To get started with Azure AI Content Safety, see [Quickstart: Analyze text content](/azure/ai-services/content-safety/quickstart-text). You run a higher risk of exposing users to harmful content if you don't use content filtering (preview) when working with models that are deployed via serverless APIs.
+
+[!INCLUDE [content-safety-harm-categories](../includes/content-safety-harm-categories.md)]
+
+## How charges are calculated
+
+Pricing details are viewable at [Azure AI Content Safety pricing](https://azure.microsoft.com/pricing/details/cognitive-services/content-safety/). Charges are incurred when the Azure AI Content Safety validates the prompt or completion. If Azure AI Content Safety blocks the prompt or completion, you're charged for both the evaluation of the content and the inference calls.
+
+## Related content
+
+- [How to configure content filters (preview) for models in Azure AI services](../../ai-foundry/model-inference/how-to/configure-content-filters.md)
+- [What is Azure AI Content Safety?](../../ai-services/content-safety/overview.md)
+- [Model catalog and collections in Azure AI Foundry portal](../how-to/model-catalog-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "サーバーレスAPIを使用したモデルのためのコンテンツ安全性"
}
```

### Explanation
この変更は、Azure AI Foundryにおける新しい文書「サーバーレスAPIを使用したモデルのためのコンテンツ安全性」の追加を含んでいます。この新しい文書は、以下の内容を提供しています。

1. **目的の明確化**: 本記事では、Azure AIのモデルカタログから提供されたモデルにおけるコンテンツ安全性の機能について説明されています。特に、サーバーレスAPIを使用したモデルに関する内容が中心です。
   
2. **デフォルトのコンテンツフィルタ**: Azure AIが用いるデフォルトのコンテンツフィルタの設定、フィルタリングの基準や、テキストモデル及び画像モデルそれぞれのフィルタリング設定についての詳細が示されています。

3. **利用上の注意**: コンテンツフィルタリングが利用できないモデルタイプ（埋め込みモデルや時系列モデルなど）に関する注意喚起や、サーバーレスエンドポイントにおけるフィルタリングの無効化方法が説明されています。

4. **料金計算の仕組み**: Azure AI Content Safetyがプロンプトやコンテンツを評価する際の課金方法についても詳しく説明されています。

5. **関連コンテンツのリンク**: ユーザーは、設定手順や他の関連情報へのリンクを通じて、さらに深い理解を得ることができます。

この文書は、Azure AIを活用する開発者にとって、コンテンツの安全性を確保し、リスクを管理するための重要なリソースとなり得るものです。

## articles/ai-studio/how-to/deploy-models-cohere-command.md{#item-3e97f4}

<details>
<summary>Diff</summary>
````diff
@@ -490,8 +490,8 @@ except HttpResponseError as ex:
     raise
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -977,8 +977,8 @@ catch (error) {
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -1489,8 +1489,8 @@ catch (RequestFailedException ex)
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -2117,8 +2117,8 @@ The following example shows how to handle events when the model detects harmful
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AIコンテンツ安全設定の情報更新"
}
```

### Explanation
この変更は、「Cohereコマンドを使用してモデルをデプロイする方法」に関する文書の小規模な修正を含んでいます。主な変更点は以下の通りです。

1. **内容の更新**: 文章内の特定の位置から、Azure AIコンテンツ安全設定に関するチップが削除され、代わりに`[!INCLUDE]`構文が追加され、別のノートがインクルードされる形になりました。このノートは、サーバーレスAPIに関連する内容で、コンテンツ安全に関する情報を提供する目的で使用されています。

2. **一貫性の向上**: 新しい文書構造が導入されたことにより、ナビゲーションと情報の一貫性が保証され、読者が必要な情報を見つけやすくなっています。

この修正は、ユーザーがAzure AIのコンテンツ安全性設定をより効果的に理解し、活用する手助けとなる内容を提供しています。

## articles/ai-studio/how-to/deploy-models-deepseek.md{#item-7c33de}

<details>
<summary>Diff</summary>
````diff
@@ -269,8 +269,8 @@ except HttpResponseError as ex:
     raise
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -542,8 +542,8 @@ catch (error) {
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -835,8 +835,8 @@ catch (RequestFailedException ex)
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -1121,8 +1121,8 @@ The following example shows how to handle events when the model detects harmful
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AIコンテンツ安全設定に関する情報更新"
}
```

### Explanation
この変更は、「DeepSeekモデルのデプロイ方法」に関する文書に対する小規模な修正を含んでいます。主要な変更点は以下の通りです。

1. **情報のアップデート**: 文書内の特定のセクションから、Azure AIコンテンツ安全設定に関するヒントが削除され、新たに`[!INCLUDE]`構文を使用して、外部ノートを追加しました。このノートは、サーバーレスAPIに関連するコンテンツ安全性についての情報を提供します。

2. **一貫性の向上**: 読者が必要な情報をより簡単に見つけられるように、情報の構造が改善されました。これにより、他の関連ドキュメントとの整合性も保たれます。

この修正は、Azure AIにおけるコンテンツ安全性の設定をよりよく理解し、効果的に活用するための手助けを行っています。

## articles/ai-studio/how-to/deploy-models-gretel-navigator.md{#item-2e9806}

<details>
<summary>Diff</summary>
````diff
@@ -266,8 +266,8 @@ except HttpResponseError as ex:
 
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -509,8 +509,8 @@ The following example shows how to handle events when the model detects harmful
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AIコンテンツ安全設定に関するノートの更新"
}
```

### Explanation
この変更は、「Gretel Navigatorを使用したモデルのデプロイ方法」に関する文書において、少数の修正を伴う更新です。主な変更点は以下の通りです。

1. **情報の更新**: 改訂されたセクションにおいて、Azure AIコンテンツ安全設定に関するチップが削除され、新たに`[!INCLUDE]`構文を使用して、外部ノートが追加されました。このノートは、特にサーバーレスAPIに関連する内容で、ユーザーにコンテンツ安全性の設定に関する情報を提供します。

2. **構造の改善**: 修正により、文書の整合性が見直され、情報の流れがよりスムーズになりました。これにより、読者が必要な情報を容易に見つけられるようになります。

この更新は、Azure AIの利用者に対し、コンテンツ安全性に関する最新の情報を提供するものであり、ドキュメントの価値を高める効果があります。

## articles/ai-studio/how-to/deploy-models-jais.md{#item-0bd11f}

<details>
<summary>Diff</summary>
````diff
@@ -272,8 +272,7 @@ except HttpResponseError as ex:
     raise
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
 ::: zone-end
 
@@ -546,8 +545,8 @@ catch (error) {
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -836,8 +835,8 @@ catch (RequestFailedException ex)
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -1158,8 +1157,8 @@ The following example shows how to handle events when the model detects harmful
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AIコンテンツ安全設定に関する情報の更新"
}
```

### Explanation
この変更は、「JAISを使用したモデルのデプロイ方法」に関する文書における小さな修正を伴う更新です。主な変更点は以下の通りです。

1. **情報の更新**: 文書中の特定のセクションで、Azure AIコンテンツ安全設定に関するヒントが削除され、代わりに新たに`[!INCLUDE]`構文を使用して外部のノートが追加されました。このノートは、サーバーレスAPIに関するコンテンツ安全性の情報を提供します。

2. **構造の改善**: 修正により、文書の情報が整理され、流れがより明確になりました。また、インクルード形式により、各セクションの整合性が向上しました。

この更新は、Azure AIに関心を持つユーザーに対し、コンテンツ安全性に関する最新の情報を効果的に提供することを目的としています。情報の明確さと一貫性を高めることに寄与しています。

## articles/ai-studio/how-to/deploy-models-llama.md{#item-6274a7}

<details>
<summary>Diff</summary>
````diff
@@ -357,11 +357,8 @@ except HttpResponseError as ex:
     raise
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ::: zone-end
 
@@ -705,11 +702,8 @@ catch (error) {
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ::: zone-end
 
@@ -1065,11 +1059,8 @@ catch (RequestFailedException ex)
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ::: zone-end
 
@@ -1449,11 +1440,8 @@ The following example shows how to handle events when the model detects harmful
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ニューラルネットワークモデルデプロイメントに関するコンテンツの更新"
}
```

### Explanation
この変更は、「Llamaを用いたモデルのデプロイ方法」に関する文書の小さな修正を伴う更新です。主な変更点は以下の通りです。

1. **情報の整理**: 文書内のヒントと注記が見直され、`[!TIP]`と`[!NOTE]`が削除され、代わりに`[!INCLUDE]`構文を用いて、サーバーレスAPIに関する注意事項が一つのノートとして統合されました。この変更により、情報が一か所に集中し、ユーザーが理解しやすくなっています。

2. **冗長な情報の削除**: サーバーレスAPIに関連するAzure AIのコンテンツ安全性に関する情報が簡潔に整理され、読みやすさと流れが改善されています。具体的には、同じ情報が繰り返されることを避け、よりスムーズに文書が進行するようになっています。

この更新は、Azure AIの利用者が重要な情報をより簡単に見つけられるようにするため、ドキュメントの構成を改善することを目的としています。また、サーバーレスAPIでのコンテンツ安全性への理解を強化するためのものです。

## articles/ai-studio/how-to/deploy-models-mistral-codestral.md{#item-83ba03}

<details>
<summary>Diff</summary>
````diff
@@ -466,8 +466,8 @@ except HttpResponseError as ex:
     raise
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -929,8 +929,8 @@ catch (error) {
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -1414,8 +1414,8 @@ catch (RequestFailedException ex)
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -2025,8 +2025,8 @@ The following example shows how to handle events when the model detects harmful
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MistralとCodestalモデルデプロイメントに関するコンテンツの更新"
}
```

### Explanation
この変更は、「MistralとCodestalを用いたモデルのデプロイ方法」に関する文書の小規模な修正を伴う更新です。主な変更点は以下の通りです。

1. **情報の整理と統合**: 文書内で安定性と安全性に関連する情報が見直され、複数の`[!TIP]`のセクションが削除されています。その代わりに、`[!INCLUDE]`構文が追加され、サーバーレスAPIに関する注記が統合されました。この変更により、ユーザーは関連情報を一つの場所から取得できるようになり、文書全体の流れがスムーズになっています。

2. **冗長な情報の削除**: 各セクションにおける情報が簡潔になり、異なる場所に分散していた同様のメッセージが一か所にまとめられました。これにより、ユーザーはAzure AIコンテンツ安全性に関する重要な情報を簡単に見つけることができます。

この更新は、ユーザーがAzure AIに関するコンテンツ安全性の設定を理解し、実行するために必要な情報をより効率的に提供することを目的としています。文書の一貫性を向上させ、情報の可読性を高めています。

## articles/ai-studio/how-to/deploy-models-mistral-nemo.md{#item-e7b729}

<details>
<summary>Diff</summary>
````diff
@@ -461,8 +461,8 @@ except HttpResponseError as ex:
     raise
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -920,8 +920,8 @@ catch (error) {
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -1401,8 +1401,8 @@ catch (RequestFailedException ex)
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -2008,8 +2008,8 @@ The following example shows how to handle events when the model detects harmful
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MistralとNemoモデルデプロイメントに関するコンテンツの更新"
}
```

### Explanation
この変更は、「MistralとNemoを用いたモデルのデプロイ方法」に関する文書の小規模な修正を伴う更新です。以下が主な変更点です。

1. **情報の整理**: 文書内での安定性と安全性に関する説明が改善され、以前の複数の`[!TIP]`セクションが削除され、`[!INCLUDE]`構文を用いて、サーバーレスAPIに関連する重要な情報が一貫して追加されました。この統合により、ユーザーは関連情報をより簡単に見つけることができるようになります。

2. **冗長な情報の削除**: 同じ安全性に関する情報が繰り返し表示されるのを避け、文書の中で一度の注記にまとめられることにより、視覚的な明瞭性と理解のしやすさが向上しました。

この更新は、Azure AIを利用するユーザーがコンテンツ安全性に関する情報を効率的に取得できるようにし、文書全体のクオリティを向上させることを目的としています。また、文書の可読性を高めることで、より迅速な情報取得を可能にしています。

## articles/ai-studio/how-to/deploy-models-mistral.md{#item-487a41}

<details>
<summary>Diff</summary>
````diff
@@ -510,8 +510,8 @@ except HttpResponseError as ex:
     raise
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -1019,8 +1019,8 @@ catch (error) {
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -1550,8 +1550,8 @@ catch (RequestFailedException ex)
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -2207,8 +2207,7 @@ The following example shows how to handle events when the model detects harmful
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralモデルデプロイメントに関するコンテンツの更新"
}
```

### Explanation
この変更は、「Mistralモデルのデプロイ方法」に関する文書における小規模な修正を伴う更新です。以下は主な変更点です。

1. **情報の統合**: 安全性に関する情報が一貫して整理され、以前の複数の`[!TIP]`セクションが削除されています。その代わりに、`[!INCLUDE]`構文を用いて、サーバーレスAPIに関連する重要な情報を一か所に集約しました。これにより、ユーザーは必要な情報をより簡単に見つけることができるようになります。

2. **冗長性の軽減**: 各セクションで同じ内容の情報が繰り返されることを防ぎ、視覚的な明瞭性が向上しました。複数の場所に分散していた重要な情報が整理され、より一貫したメッセージが提供されています。

この更新は、Azure AIの利用者がコンテンツ安全性の設定の理解を深め、文書全体のクオリティと可読性を向上させることを目的としています。ユーザーが求める情報にスムーズにアクセスできるよう配慮されています。

## articles/ai-studio/how-to/deploy-models-phi-3-5-vision.md{#item-8d6d7d}

<details>
<summary>Diff</summary>
````diff
@@ -308,11 +308,8 @@ except HttpResponseError as ex:
     raise
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ## Use chat completions with images
 
@@ -699,11 +696,8 @@ catch (error) {
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ## Use chat completions with images
 
@@ -1108,11 +1102,8 @@ catch (RequestFailedException ex)
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ## Use chat completions with images
 
@@ -1526,11 +1517,8 @@ The following example shows how to handle events when the model detects harmful
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ## Use chat completions with images
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi 3.5 Visionモデルデプロイメントに関するコンテンツの更新"
}
```

### Explanation
この変更は、「Phi 3.5 Visionモデルのデプロイ方法」に関する文書の小規模な修正を伴う更新です。以下は主要な変更点です。

1. **情報の一元化**: 安全性に関する情報を整理し、複数の`[!TIP]`及び`[!NOTE]`セクションを削除し、`[!INCLUDE]`構文を使用してサーバーレスAPIに関連する重要な情報を一か所にまとめました。これにより、ユーザーが必要な情報に容易にアクセスできるようになります。

2. **冗長性の削減**: 同様の内容が繰り返し表示されることを避け、文書の可読性が向上しました。また、不要な情報を削除することで、内容がより明確になり、利用者にとっての理解を助ける構造になっています。

3. **構造の整備**: 不要な文を排除することで、文書の流れが改善され、全体的なクオリティが向上しました。この更新により、読者が最も重要な情報に焦点を合わせられるよう配慮されています。

この小規模な更新は、Azure AIを利用するユーザーがコンテンツ安全性についての理解を深め、人材育成に役立つ情報を簡単に取得できるようになることを目的としております。

## articles/ai-studio/how-to/deploy-models-phi-3.md{#item-47e305}

<details>
<summary>Diff</summary>
````diff
@@ -342,11 +342,7 @@ except HttpResponseError as ex:
     raise
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
-
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
 ::: zone-end
 
@@ -693,11 +689,8 @@ catch (error) {
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ::: zone-end
 
@@ -1056,11 +1049,8 @@ catch (RequestFailedException ex)
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ::: zone-end
 
@@ -1443,11 +1433,8 @@ The following example shows how to handle events when the model detects harmful
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi 3モデルデプロイメントに関するコンテンツの更新"
}
```

### Explanation
この変更は、「Phi 3モデルのデプロイ方法」に関する文書における小規模な修正を伴う更新です。主な変更点は以下の通りです。

1. **情報の一元化と集約**: コンテンツ安全性に関する情報が整理され、冗長な`[!TIP]`および`[!NOTE]`セクションが削除されました。その代わりに、`[!INCLUDE]`構文を使用して、サーバーレスAPIに関連する重要な情報を一つの場所に集約しました。これにより、ユーザーは必要な情報をより容易に見つけられるようになります。

2. **テキストの削減**: 不要な記述が削除され、文書がより簡潔で明確になりました。これにより、読者が内容を素早く理解しやすくなる効果があります。具体的には、コンテンツの重複を排除し、かつ言及を一度に統一しました。

3. **文書の流れの改善**: 情報の整理により、文書全体の流れが円滑になり、可読性が向上しました。この変更は、ユーザーが重要な情報をすぐに確認できるようにするためのもので、ドキュメントのクオリティを向上させることを目的としています。

この更新は、Azure AIの利用者がコンテンツ安全性の理解を深め、実践的な情報を効率的に取得できるようにするためのもので、全体的なユーザビリティを向上させています。

## articles/ai-studio/how-to/deploy-models-phi-4.md{#item-c40212}

<details>
<summary>Diff</summary>
````diff
@@ -312,11 +312,8 @@ except HttpResponseError as ex:
     raise
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ::: zone-end
 
@@ -633,11 +630,8 @@ catch (error) {
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ::: zone-end
 
@@ -966,11 +960,8 @@ catch (RequestFailedException ex)
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ::: zone-end
 
@@ -1323,11 +1314,8 @@ The following example shows how to handle events when the model detects harmful
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
-> [!NOTE]
-> Azure AI content safety is only available for models deployed as serverless API endpoints.
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi 4モデルデプロイメントに関するコンテンツの更新"
}
```

### Explanation
この変更は、「Phi 4モデルのデプロイ方法」に関する文書の小規模な修正を伴う更新です。主な変更点は次の通りです。

1. **情報の集約**: コンテンツ安全性に関する情報が整理され、複数の`[!TIP]`および`[!NOTE]`セクションが削除されました。代わりに、`[!INCLUDE]`構文が使用され、サーバーレスAPIに関連する重要な情報が1つの場所にまとめられました。これにより、ユーザーは必要な情報をより簡単に見つけることができます。

2. **冗長性の削減**: 同じ内容が何度も繰り返されることを避け、文書の読みやすさを向上させました。特に、コンテンツにおける重複表現を排除することで、情報の伝達がより効率的になります。

3. **文書の整合性向上**: 不要な文が排除され、全体の文書の流れが良くなりました。これにより、読者が重要な情報を迅速に把握できるように工夫されています。

この更新は、Azure AIを使用するユーザーがコンテンツ安全性についての理解を深めつつ、実践的な情報にアクセスしやすくすることを目的としており、文書の全体的なクオリティを高めています。

## articles/ai-studio/how-to/deploy-models-tsuzumi.md{#item-d3fd51}

<details>
<summary>Diff</summary>
````diff
@@ -266,8 +266,8 @@ except HttpResponseError as ex:
     raise
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -583,8 +583,8 @@ catch (error) {
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
@@ -917,8 +917,7 @@ catch (RequestFailedException ex)
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
 
 ::: zone-end
 
@@ -1317,8 +1316,8 @@ The following example shows how to handle events when the model detects harmful
 }
 ```
 
-> [!TIP]
-> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+[!INCLUDE [content-safety-serverless-apis-note](../includes/content-safety-serverless-apis-note.md)]
+
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Tsuzumiモデルデプロイメントに関するコンテンツの更新"
}
```

### Explanation
この変更は、「Tsuzumiモデルのデプロイ方法」に関する文書に対する小規模な修正を含む更新です。主な変更点は以下の通りです。

1. **情報の集約**: 各セクションに繰り返し記載されていた内容が削除され、代わりに`[!INCLUDE]`構文が導入されました。これにより、サーバーレスAPIに関するコンテンツ安全性の重要な情報が一つの場所にまとめられ、文書の整理が進められました。ユーザーは関連情報をより効率的に確認できるようになっています。

2. **冗長性の排除**: 複数回記載されていた情報が削除され、文書全体が簡潔に保たれています。これにより、読みやすさが向上し、情報が迅速に把握できるようになっています。

3. **文書全体の流れの改善**: 不要なテキストが削除されることで、全体の文書の流れがスムーズになりました。読者は、重要な情報にすぐにアクセスできるようになり、文書の使用感が向上しています。

この更新は、Azure AIを利用するユーザーがコンテンツ安全性に関する理解を深化させ、効果的に情報を得ることを目的としており、文書の質を向上させるためのものです。

## articles/ai-studio/how-to/healthcare-ai/deploy-cxrreportgen.md{#item-377d15}

<details>
<summary>Diff</summary>
````diff
@@ -16,8 +16,6 @@ author: msakande
 
 # How to use CXRReportGen Healthcare AI model to generate grounded findings
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
-
 [!INCLUDE [health-ai-models-meddev-disclaimer](../../includes/health-ai-models-meddev-disclaimer.md)]
 
 In this article, you learn how to deploy CXRReportGen as an online endpoint for real-time inference and issue a basic call to the API. The steps you take are:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "CXRReportGenモデルに関する文書の簡略化"
}
```

### Explanation
この変更は、「CXRReportGen Healthcare AIモデルのデプロイ方法」に関する文書の小規模な修正を伴う更新です。具体的には、以下の点が変更されました。

1. **不要な行の削除**: 文章中の冗長な内容として、`[!INCLUDE]`コンテンツが2行削除されました。これにより、文書の流れがスムーズになり、重要な情報に対するフォーカスが高まりました。

2. **文書の簡潔化**: 必要のない情報が省かれることで、読者はより重要な内容に集中しやすくなります。特に、機能プレビューに関する情報が削除されたことにより、内容が明確になっています。

この更新は、CXRReportGenモデルを使用するユーザーが必要な情報を迅速に得られるように配慮されており、文書全体の品質を向上させることを目的としています。

## articles/ai-studio/how-to/healthcare-ai/deploy-medimageinsight.md{#item-e9ab9e}

<details>
<summary>Diff</summary>
````diff
@@ -16,8 +16,6 @@ author: msakande
 
 # How to use MedImageInsight healthcare AI model for medical image embedding generation
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
-
 [!INCLUDE [health-ai-models-meddev-disclaimer](../../includes/health-ai-models-meddev-disclaimer.md)]
 
 In this article, you learn how to deploy MedImageInsight from the model catalog as an online endpoint for real-time inference. You also learn to issue a basic call to the API. The steps you take are:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MedImageInsightモデルに関する文書の簡略化"
}
```

### Explanation
この変更は、「MedImageInsight Healthcare AIモデルのデプロイ方法」に関する文書に対する小規模な修正を含んでいます。具体的な変更内容は以下の通りです。

1. **冗長なコンテンツの削除**: 文書から`[!INCLUDE]`構文に関連する2行が削除されました。これにより、文章が簡潔になり、内容の明瞭さが向上しました。

2. **文書の流れの改善**: 不要な情報を削除することで、ユーザーは関心のある重要な情報により迅速にアクセスできるようになりました。

この更新は、MedImageInsightモデルを使用する際の情報の明確さを目的としており、従来の内容に対する不要な情報を排除することで、利用者が必要な知識をより効率的に得られるように配慮されています。

## articles/ai-studio/how-to/healthcare-ai/deploy-medimageparse.md{#item-611e84}

<details>
<summary>Diff</summary>
````diff
@@ -16,8 +16,6 @@ author: msakande
 
 # How to use MedImageParse healthcare AI model for segmentation of medical images
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
-
 [!INCLUDE [health-ai-models-meddev-disclaimer](../../includes/health-ai-models-meddev-disclaimer.md)]
 
 In this article, you learn how to deploy MedImageParse as an online endpoint for real-time inference and issue a basic call to the API. The steps you take are:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MedImageParseモデルに関する文書の簡略化"
}
```

### Explanation
この変更は、「MedImageParse Healthcare AIモデルのデプロイ方法」に関する文書に対する小規模な修正を含んでいます。具体的には次の内容が含まれています。

1. **冗長な行の削除**: 文書から`[!INCLUDE]`の構文が2行削除されました。これにより、文書が簡潔になり、読者にとって理解しやすくなりました。

2. **情報の明確化**: 不要な情報が省かれることで、ユーザーはより重要な内容に焦点を当てやすくなります。この変更により、ユーザーがMedImageParseモデルを使用する際に必要な直接的な情報が強調されています。

この更新は、医療画像のセグメンテーションのためにMedImageParseモデルを活用しようとするユーザーにとって、必要な情報へのアクセスを迅速に可能にすることを目的としています。

## articles/ai-studio/how-to/healthcare-ai/healthcare-ai-models.md{#item-12fcfc}

<details>
<summary>Diff</summary>
````diff
@@ -16,8 +16,6 @@ author: msakande
 
 # Foundation models for healthcare AI
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
-
 [!INCLUDE [health-ai-models-meddev-disclaimer](../../includes/health-ai-models-meddev-disclaimer.md)]
 
 In this article, you learn about Microsoft's catalog of multimodal healthcare foundation models. The models were developed in collaboration with Microsoft Research, strategic partners, and leading healthcare institutions for healthcare organizations. Healthcare organizations can use the models to rapidly build and deploy AI solutions tailored to their specific needs, while minimizing the extensive compute and data requirements typically associated with building multimodal models from scratch. The intention isn't for these models to serve as standalone products; rather, they're designed for developers to use as a foundation to build upon. With these healthcare AI models, professionals have the tools they need to harness the full potential of AI to enhance biomedical research, clinical workflows, and ultimately care delivery.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ヘルスケアAIモデルに関する文書の簡略化"
}
```

### Explanation
この変更は、「ヘルスケアAIモデル」に関する文書に対する小規模な修正を含んでいます。具体的には以下の内容です。

1. **冗長な行の削除**: 文書から`[!INCLUDE]`による構文が2行削除されました。この修正により、内容が簡潔になり、読者にとって情報が明確に伝わるよう改善されました。

2. **情報の活用性向上**: 不要な要素を取り除くことで、ユーザーはより核心的な情報に集中しやすくなりました。これは、ヘルスケアAIモデルについての理解を深め、実際の利用に役立つでしょう。

この更新は、Microsoftのマルチモーダルヘルスケアファウンデーションモデルの利用を促進し、開発者が自らのニーズに応じたAIソリューションを迅速に構築し展開できることを目指しています。全体的に、文書の流れが改善され、ユーザーが必要とする重要な情報によりアクセスしやすくなっています。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -27,7 +27,7 @@ The model catalog in Azure AI Foundry portal is the hub to discover and use a wi
 The model catalog organizes models into different collections:
 
 
-* **Curated by Azure AI**: The most popular non-Microsoft open-weight and proprietary models packaged and optimized to work seamlessly on the Azure AI platform. Use of these models is subject to the model providers' license terms. When you deploy these models in Azure AI Foundry portal, their availability is subject to the applicable [Azure service-level agreement (SLA)](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services), and Microsoft provides support for deployment problems.
+* **Curated by Azure AI**: The most popular partner models (open-weight and proprietary) packaged and optimized to work seamlessly on the Azure AI platform. Use of these models is subject to the model providers' license terms. When you deploy these models in Azure AI Foundry portal, their availability is subject to the applicable [Azure service-level agreement (SLA)](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services), and Microsoft provides support for deployment problems.
 
   Models from partners such as Meta, NVIDIA, and Mistral AI are examples of models available in this collection on the catalog. You can identify these models by looking for a green checkmark on the model tiles in the catalog. Or you can filter by the **Curated by Azure AI** collection.
 
@@ -97,7 +97,7 @@ Nixtla | Not available | TimeGEN-1
 AI models evolve fast, and when a new version or a new model with updated capabilities in the same model family become available, older models may be retired in the AI Foundry model catalog. To allow for a smooth transition to a newer model version, some models provide users with the option to enable automatic updates. To learn more about the model lifecycle of different models, upcoming model retirement dates, and suggested replacement models and versions, see:
 
 - [Azure OpenAI Service model deprecations and retirements](../../ai-services/openai/concepts/model-retirements.md)
-- [Severless API model deprecations and retirements](../../ai-studio/concepts/model-lifecycle-retirement.md)
+- [Serverless API model deprecations and retirements](../../ai-studio/concepts/model-lifecycle-retirement.md)
 
 ## Managed compute
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルカタログの表現の改善"
}
```

### Explanation
この変更は、「モデルカタログの概要」に関する文書に対する小規模な修正を含んでいます。主な修正点は以下の通りです。

1. **表現の改善**: 「Curated by Azure AI」という項目の説明が更新されました。元の文書では「非マイクロソフトのオープンウェイトおよびプロプライエタリモデル」と表現されていましたが、修正後は「パートナーモデル（オープンウェイトおよびプロプライエタリ）」とされています。この変更により、より広範囲なパートナーシップを反映した表現となり、読者の理解を助けます。

2. **軽微なテキスト修正**: 別の部分では、「Severless API model deprecations and retirements」の表記が「Serverless API model deprecations and retirements」に修正され、正確なスペルに直されています。

このような変更は、ドキュメントの正確性と可読性を向上させ、ユーザーがAzure AIのモデルカタログをよりよく理解できるようにすることを目的としています。全体として、文書の内容が明確化され、関連情報へのアクセスが向上しています。

## articles/ai-studio/includes/content-safety-harm-categories.md{#item-8ef139}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,29 @@
+---
+title: include file
+description: include file
+ms.author: pafarley
+ms.service: azure-ai-studio
+ms.topic: include
+ms.date: 01/28/2025
+ms.custom: include
+---
+
+## Understand harm categories
+
+### Harm categories
+
+| Category  | Description         |API term |
+| --------- | ------------------- | --- |
+| Hate and Fairness      | Hate and fairness harms refer to any content that attacks or uses discriminatory language with reference to a person or identity group based on certain differentiating attributes of these groups. <br><br>This includes, but isn't limited to:<ul><li>Race, ethnicity, nationality</li><li>Gender identity groups and expression</li><li>Sexual orientation</li><li>Religion</li><li>Personal appearance and body size</li><li>Disability status</li><li>Harassment and bullying</li></ul> | `Hate` |
+| Sexual  | Sexual describes language related to anatomical organs and genitals, romantic relationships and sexual acts, acts portrayed in erotic or affectionate terms, including those portrayed as an assault or a forced sexual violent act against one's will. <br><br> This includes but isn't limited to:<ul><li>Vulgar content</li><li>Prostitution</li><li>Nudity and Pornography</li><li>Abuse</li><li>Child exploitation, child abuse, child grooming</li></ul>   | `Sexual` |
+| Violence  | Violence describes language related to physical actions intended to hurt, injure, damage, or kill someone or something; describes weapons, guns, and related entities. <br><br>This includes, but isn't limited to:  <ul><li>Weapons</li><li>Bullying and intimidation</li><li>Terrorist and violent extremism</li><li>Stalking</li></ul>  | `Violence` |
+| Self-Harm  | Self-harm describes language related to physical actions intended to purposely hurt, injure, damage one's body or kill oneself. <br><br> This includes, but isn't limited to: <ul><li>Eating Disorders</li><li>Bullying and intimidation</li></ul>  | `SelfHarm` |
+
+### Severity levels 
+
+| Level | Description |
+| --- | ---|
+|Safe |Content might be related to violence, self-harm, sexual, or hate categories. However, the terms are used in general, journalistic, scientific, medical, and similar professional contexts, which are appropriate for most audiences. |
+|Low |Content that expresses prejudiced, judgmental, or opinionated views, includes offensive use of language, stereotyping, use-cases exploring a fictional world (for example, gaming, literature) and depictions at low intensity.| 
+|Medium |Content that uses offensive, insulting, mocking, intimidating, or demeaning language towards specific identity groups, includes depictions of seeking and executing harmful instructions, fantasies, glorification, promotion of harm at medium intensity. |
+|High |Content that displays explicit and severe harmful instructions, actions, damage, or abuse; includes endorsement, glorification, or promotion of severe harmful acts, extreme or illegal forms of harm, radicalization, or nonconsensual power exchange or abuse. |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "コンテンツ安全性および危険カテゴリの理解"
}
```

### Explanation
この変更は、コンテンツの安全性と関連する危険カテゴリについての新しいセクションを追加するものです。この追加により、内容は29行が新しく挿入され、具体的には以下の要素が含まれています。

1. **危険カテゴリの説明**: 新しい文書には、差別的な言語や暴力、セクシャリティ、自己傷害といったさまざまな危険カテゴリの詳細な説明が含まれています。これにより、各カテゴリに関連する具体的な行動や言語のタイプを理解できるようになります。

2. **カテゴリ別の詳細**: 各危険カテゴリには、具体的な説明や関連する用語、あるいはそれに該当する具体例が挙げられています。たとえば、ヘイトや公平性のカテゴリでは、人種や性別、宗教に基づく攻撃的な言語が含まれることが説明されています。

3. **深刻度レベルの定義**: コンテンツの深刻度レベルについての表も追加され、安全（Safe）、低（Low）、中（Medium）、高（High）といった分類が行われています。これにより、ユーザーはコンテンツのリスクを評価しやすくなります。

この新しいセクションは、ユーザーがコンテンツ安全性の重要性を理解し、適切に危険カテゴリに対応できるようにするための貴重なリソースとなります。全体として、この改訂はAzure AI Studioにおけるコンテンツの安全性を強化することを目的としています。

## articles/ai-studio/includes/content-safety-serverless-apis-note.md{#item-779e7e}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,13 @@
+---
+title: include file
+description: include file
+author: msakande
+ms.author: mopeakande
+ms.service: azure-ai-studio
+ms.topic: include
+ms.date: 02/04/2025
+ms.custom: include file
+---
+
+> [!NOTE]
+> Azure AI content safety is currently available for models deployed as serverless API endpoints, but not to models deployed via managed compute. To learn more about Azure AI content safety for models deployed as serverless APIs, see [Content safety for models curated by Azure AI in the model catalog](../concepts/model-catalog-content-safety.md).
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "サーバーレスAPIに関するコンテンツ安全性の注記"
}
```

### Explanation
このコードの変更は、Azure AI StudioにおけるサーバーレスAPIに関連するコンテンツ安全性についての新しい注記を追加するものです。この変更には、合計で13行の新しい内容が含まれています。

1. **注記の追加**: 新たに挿入された部分では、Azure AIコンテンツ安全性がサーバーレスAPIエンドポイントとしてデプロイされたモデルに利用可能であることが記載されています。一方、管理されたコンピューティングを通じてデプロイされたモデルにはこの機能が適用されないことが明確にされています。

2. **コンテンツ安全性についての情報提供**: さらに、サーバーレスAPIとしてデプロイされたモデルに関連するコンテンツ安全性についての詳細情報を提供するリンクが含まれています。このリンクは、ユーザーがモデルカタログ内でキュレーションされたAzure AIのモデルに関するコンテンツ安全性について学ぶためのもので、重要なリソースとなります。

この新しい文書は、Azure AIにおけるコンテンツの安全性とその適用範囲をユーザーに理解させることを目的としており、特にサーバーレスAPIの利用者にとっての重要なガイドラインを提供しています。全体的に、この変更はユーザーへの情報提供を強化し、Azure AIの利用における安全性の理解を深めることに寄与します。

## articles/ai-studio/includes/content-safety-serverless-models.md{#item-8fe192}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ ms.custom: include file
 # Also used in Azure Machine Learning documentation
 ---
 
-For language models deployed via serverless APIs, Azure AI implements a default configuration of [Azure AI Content Safety](/azure/ai-services/content-safety/overview) text moderation filters that detect harmful content such as hate, self-harm, sexual, and violent content. To learn more about content filtering (preview), see [Harm categories in Azure AI Content Safety](/azure/ai-services/content-safety/concepts/harm-categories).
+For language models deployed via serverless APIs, Azure AI implements a default configuration of [Azure AI Content Safety](../../ai-services/content-safety/overview.md) text moderation filters that detect harmful content such as hate, self-harm, sexual, and violent content. To learn more about content filtering (preview), see [Content safety for models curated by Azure AI in the model catalog](../concepts/model-catalog-content-safety.md). 
 
 > [!TIP]
 > Content filtering (preview) is not available for certain model types that are deployed via serverless APIs. These model types include embedding models and time series models.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスモデルにおけるコンテンツ安全性のリンク更新"
}
```

### Explanation
このコードの変更は、サーバーレスモデルに関するコンテンツ安全性のドキュメント内におけるリンクの更新を目的としたものです。具体的には、合計で2行が変更されており、1行が追加され、1行が削除されています。

1. **リンクの更新**: 旧バージョンでは、Azure AIコンテンツ安全性に関するリンクが特定のドキュメントを指していましたが、新しいバージョンでは相対パスが調整されています。これにより、より正確に関連文書へのアクセスが可能になっています。具体的には、コンテンツフィルタリングに関する詳細についてのリンクが更新され、サーバーレスAPI用に構築されたモデルに関する情報を提供する代替のリンクが指定されています。

2. **コンテンツフィルタリングについての注意事項**: 変更はコンテンツフィルタリングの機能についての情報を明確にする助けとなり、サーバーレスAPIでデプロイされた特定のモデルタイプ（埋め込みモデルや時系列モデルなど）に関してはそのフィルタリングが利用できないことも再確認されています。

この更新により、関連情報へのアクセスが向上し、ユーザーがサーバーレスモデルのコンテンツ安全性に関する理解を深められるようサポートしています。全体として、これは情報鮮度を保ち、ユーザーにとっての利便性を高めるための重要な改訂です。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -200,6 +200,8 @@ items:
         - name: Consume serverless API models from a different project or hub
           href: how-to/deploy-models-serverless-connect.md
           displayName: maas, paygo, models-as-a-service
+        - name: Content safety for models deployed with serverless APIs
+          href: concepts/model-catalog-content-safety.md
         - name: Model and region availability for Serverless API deployments
           href: how-to/deploy-models-serverless-availability.md
       - name: Managed compute
@@ -416,8 +418,10 @@ items:
     href: responsible-use-of-ai-overview.md
   - name: What is Azure AI Content Safety?
     href: ai-services/content-safety-overview.md
-  - name: Use Azure AI Content Safety in the portal
-    href: ai-services/how-to/content-safety.md
+  - name: Content safety for models deployed with serverless APIs
+    href: concepts/model-catalog-content-safety.md
+  - name: Use Azure AI content safety in the portal
+    href: ../ai-services/content-safety/how-to/foundry.md?context=/azure/ai-studio/context/context
   - name: Content filtering
     href: concepts/content-filtering.md
   - name: Use blocklists
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスAPIモデルのコンテンツ安全性に関するリンク追加"
}
```

### Explanation
このコードの変更は、Azure AI Studioの目次ファイル（toc.yml）の更新を通じて、サーバーレスAPIでデプロイされたモデルのコンテンツ安全性に関するリンクを追加したものです。この変更には合計8箇所の変更があり、6行が追加され、2行が削除されています。

1. **新しいリンクの追加**: 目次に新たに「サーバーレスAPIでデプロイされたモデルのコンテンツ安全性」という項目が追加され、そのリンクとして「concepts/model-catalog-content-safety.md」が指定されています。これにより、ユーザーはサーバーレスAPI利用時のモデルにおけるコンテンツ安全性に関する情報を容易にアクセスできるようになります。

2. **他のリンクの整理**: 一部のリンクが更新または削除されており、特にAzure AIコンテンツ安全性に関する情報が一貫性を持つように整備されています。これにより、目次がより明確で整然としたものになり、ユーザーが必要な情報にスムーズにアクセスできるよう配慮されています。

この変更は、ユーザーがAzure AI Studioを利用する際に、サーバーレスAPIに関するコンテンツ安全性についての理解を深める手助けをし、情報の整理を図ることを目的としています。また、関連情報への導線を強化することで、ユーザビリティを向上させる重要な更新となっています。


