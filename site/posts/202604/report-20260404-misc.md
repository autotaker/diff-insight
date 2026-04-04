---
date: '2026-04-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0c9218b...MicrosoftDocs:dd1a03a
summary: この変更はAzure Languageサービスのドキュメントに重要な更新を加えるもので、データ制限やマイグレーションに関する内容の明確化、新しい画像の追加、個人情報の赤塗りに関する修正が含まれています。これにより、ユーザーは各機能をより理解しやすくなり、全体的な理解度が向上しています。新機能としては、質問と回答のペアインポートや同義語インポートに関する画像が追加されました。破壊的な変更はありません。また、文書の整備や視覚的資料の追加により、使いやすさと理解のしやすさが向上しています。これにより、特にデータ制限に関する情報が整理され、開発者や運用者がより効率的に機能を利用できるようサポートされています。全体として、Azure
  Languageサービスの情報環境が改善されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0c9218b...MicrosoftDocs:dd1a03a){target="_blank"}

<format>
# ハイライト
この変更はAzure Languageサービスの文書における数々の更新を含み、データ制限やマイグレーションに関する内容の明確化、インポート機能に関連する新しい画像の追加、個人情報の赤塗りに関する文書修正といった内容が含まれています。これにより、ユーザーが各機能をより把握しやすくなり、理解度が向上しています。

## 新機能
- 「質問と回答のペアインポート」に関する画像が新たに追加されました。
- 「同義語インポート」に関する画像が新たに追加されました。

## 破壊的な変更
- 特に破壊的な変更は報告されていません。

## その他の更新
- 「データ制限」文書の日付が更新され、情報が整理されました。
- 「マイグレーションスタジオからFoundryへの」手順の明確化が行われました。
- 「会話における個人情報の赤塗り」に関する文書が編集され、重要ではない情報が削除されました。

# インサイト
文書の整備や視覚的な資料の追加によって、Azure Languageサービスのドキュメントはより使いやすく、理解しやすくなっています。特にデータ制限に関する更新では、情報が整理され、明確になったことで、開発者や運用者が具体的な制限を理解しやすくなり、APIや機能の利用が効率的に行えるようになっています。また、新しい画像の追加は、特にビジュアルを頼りにするユーザーにとって操作手順を直感的に理解しやすくするため、使いやすさの向上に寄与しています。

さらに、マイグレーションの手順やPIIに関する文書の明確化は、ユーザーが正確かつ効率的にサービスを使用するための重要なサポートとなり、特にシステム移行や個人情報の取り扱いにおける慎重さを求められる場面での信頼性を強化します。全体を通して、Azure Languageサービスが提供する機能を最大限に活用するための情報環境が改善されています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [data-limits.md](#item-48b8af) | minor update | データ制限に関する文書の更新 | modified | 19 | 16 | 35 | 
| [question-answer-pairs-import.png](#item-7dceb2) | new feature | 質問と回答のペアインポートに関する画像の追加 | added | 0 | 0 | 0 | 
| [synonyms-import.png](#item-f096d4) | new feature | 同義語インポートに関する画像の追加 | added | 0 | 0 | 0 | 
| [migration-studio-to-foundry.md](#item-12d575) | minor update | マイグレーションスタジオからFoundryへのドキュメントの修正 | modified | 16 | 15 | 31 | 
| [redact-conversation-pii.md](#item-0d6332) | minor update | 会話における個人情報の赤塗りに関するドキュメントの修正 | modified | 1 | 5 | 6 | 


# Modified Contents
## articles/ai-services/language-service/concepts/data-limits.md{#item-48b8af}

<details>
<summary>Diff</summary>
````diff
@@ -6,44 +6,47 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: limits-and-quotas
-ms.date: 11/18/2025
+ms.date: 04/03/2026
 ms.author: lajanuar
 ---
+<!-- markdownlint-disable MD025 -->
 # Service limits for Azure Language in Foundry Tools
 
 > [!NOTE]
 > This article only describes the limits for preconfigured features in Azure Language in Foundry Tools:
-> To see the service limits for customizable features, see the following articles: 
+> To see the service limits for customizable features, see the following articles:
+>
 > * [Custom classification](../custom-text-classification/service-limits.md)
 > * [Custom NER](../custom-named-entity-recognition/service-limits.md)
 > * [Conversational language understanding](../conversational-language-understanding/service-limits.md)
 > * [Question answering](../question-answering/concepts/limits.md)
 
-Use this article to find the limits for the size, and rates that you can send data to the following features of Azure Language. 
-* [Named Entity Recognition (NER)](../named-entity-recognition/overview.md) 
+Use this article to find the limits for the size, and rates that you can send data to the following features of Azure Language.
+>
+* [Named Entity Recognition (NER)](../named-entity-recognition/overview.md)
 * [Personally Identifiable Information (PII) detection](../personally-identifiable-information/overview.md)
-* [Key phrase extraction](../key-phrase-extraction/overview.md) 
-* [Entity linking](../entity-linking/overview.md)  
+* [Key phrase extraction](../key-phrase-extraction/overview.md)
+* [Entity linking](../entity-linking/overview.md)
 * [Text Analytics for health](../text-analytics-for-health/overview.md)
 * [Sentiment analysis and opinion mining](../sentiment-opinion-mining/overview.md)
 * [Language detection](../language-detection/overview.md)
 
 When using features of Azure Language, keep the following information in mind:
 
-* Pricing is independent of data or rate limits. Pricing is based on the number of text records you send to the API, and is subject to your Language resource's [pricing details](https://aka.ms/unifiedLanguagePricing).
-    * A text record is measured as 1000 characters. 
-* Data and rate limits are based on the number of documents you send to the API. If you need to analyze larger documents than the limit allows, you can break the text into smaller chunks of text before sending them to the API. 
-* A document is a single string of text characters.  
+* Pricing is independent of data or rate limits. Pricing is based on the number of text records you send to the API, and is subject to your Language resource's [pricing details](https://aka.ms/unifiedLanguagePricing). **A text record is measured as 1000 characters**.
+* Data and rate limits are based on the number of documents you send to the API. If you need to analyze larger documents than the limit allows, you can break the text into smaller chunks of text before sending them to the API.
+* A document is a single string of text characters.
 
 ## Maximum characters per document
 
-The following limit specifies the maximum number of characters that can be in a single document.
+| The following limit specifies the maximum number of characters that can be in a single document. |
 
 | Feature | Value |
-|------------------------|---------------|
-| Text Analytics for health | 125,000 characters as measured by [StringInfo.LengthInTextElements](/dotnet/api/system.globalization.stringinfo.lengthintextelements).  | 
+| ------------------------ | --------------- |
+| Text Analytics for health | 125,000 characters as measured by [StringInfo.LengthInTextElements](/dotnet/api/system.globalization.stringinfo.lengthintextelements). |
+| Conversation PII | ≤ 1,000 characters as measured by the [**Analyze Conversations** API](/rest/api/language/analyze-conversations/analyze-conversations/analyze-conversations) default conversation item length. |
 | All other preconfigured features (synchronous) | 5,120 as measured by [StringInfo.LengthInTextElements](/dotnet/api/system.globalization.stringinfo.lengthintextelements). If you need to submit larger documents, consider using the feature asynchronously. |
-| All other preconfigured features ([asynchronous](use-asynchronously.md))  | 125,000 characters across all submitted documents, as measured by [StringInfo.LengthInTextElements](/dotnet/api/system.globalization.stringinfo.lengthintextelements) (maximum of 25 documents). |
+| All other preconfigured features ([asynchronous](use-asynchronously.md)) | 125,000 characters across all submitted documents, as measured by [StringInfo.LengthInTextElements](/dotnet/api/system.globalization.stringinfo.lengthintextelements) (maximum of 25 documents). |
 
 If a document exceeds the character limit, the API behaves differently depending on how you're sending requests.
 
@@ -65,10 +68,10 @@ The following limit specifies the maximum size of documents contained in the ent
 
 Exceeding the following document limits generates an HTTP 400 error code.
 
-> [!NOTE] 
+> [!NOTE]
 > When sending asynchronous API requests, you can send a maximum of 25 documents per request.
 
-| Feature | Max Documents Per Request | 
+| Feature | Max Documents Per Request |
 |----------|-----------|
 | Conversation summarization | 1 |
 | Language Detection | 1000 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ制限に関する文書の更新"
}
```

### Explanation
この変更は、Azure Languageサービステクノロジーに関する文書の「データ制限」に関する情報を更新するもので、ファイル内の内容を整形し、情報を明確にするための修正が行われています。具体的には、文書の日付が2025年11月18日から2026年4月3日に更新され、プラットフォーム上でのサービスの限界に関する注意事項や説明が整理されています。また、特定の機能に関連するドキュメントリンクについても改善が図られ、期日を持った情報がより分かりやすくなっています。

変更点としては、文書の新しい日付に加え、いくつかの文が追加され、テーブル構造が一部修正されています。これにより、利用者はデータの制限について理解しやすくなり、各機能におけるリミットについての情報が視覚的に整理されています。また、特定の APIリクエストに関する制約がさらに明確になり、ユーザーは各機能の制限を意識して利用できるようになります。

## articles/ai-services/language-service/media/question-answer-pairs-import.png{#item-7dceb2}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "質問と回答のペアインポートに関する画像の追加"
}
```

### Explanation
この変更は、Azure Languageサービスにおける「質問と回答のペアインポート」に関連する新しい画像ファイルが追加されたことを示しています。この画像は、ユーザーが質問と回答のペアをインポートする際の手順やインターフェースを視覚的に理解するのに役立つものです。

ファイル名は「question-answer-pairs-import.png」であり、具体的にはドキュメント内の関連情報を補完するために利用されることが期待されます。新たに追加されたこの画像により、ユーザーは文書の説明をより直感的に理解できるようになり、具体的な操作方法や期待される結果を視覚的に確認できる利点があります。

画像の追加に伴い、文書全体の理解度が向上し、特にビジュアルコンテンツを重視するユーザーにとって、学習を促進する要素となります。これにより、より効果的な利用が可能になることが目指されています。

## articles/ai-services/language-service/media/synonyms-import.png{#item-f096d4}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "同義語インポートに関する画像の追加"
}
```

### Explanation
この変更は、Azure Languageサービスに関連する「同義語インポート」に関する新しい画像ファイルが追加されたことを示しています。この画像は、利用者が同義語をインポートするプロセスを視覚的に示すもので、ドキュメントにおける情報提供の一環として機能します。

ファイル名は「synonyms-import.png」で、関連する手順やインターフェースの説明を補完する目的で使用されます。この新しい画像によって、ユーザーは文書に記載された内容をより直感的に理解でき、具体的な操作方法や期待される結果を視覚的に確認できるようになります。

画像の追加は、特に視覚的な情報を好むユーザーにとって有益であり、学習や作業の効率を向上させることを目的としています。これにより、同義語のインポートに関する理解が深まり、使用体験が向上することが期待されています。

## articles/ai-services/language-service/migration-studio-to-foundry.md{#item-12d575}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: upgrade-and-migration-article
-ms.date: 02/05/2026
+ms.date: 04/03/2026
 ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD025 -->
@@ -39,12 +39,8 @@ You can migrate to Microsoft Foundry using one of two approaches:
 
 * **[Option II: Migrate to a new Foundry resource](#option-ii-migrate-to-a-new-foundry-resource)**. Export your projects from Language Studio and import them into a new Foundry resource. This approach consolidates your AI capabilities into a single resource and provides access to both Foundry classic and the new Foundry experiences.
 
-
-
 ---
 
-
-
 ## Option I: Start using Foundry with an existing Language resource
 
 If you have an existing Azure Language resource with custom projects, you can continue using it within Microsoft Foundry by creating a Foundry hub and connecting your resource. This approach preserves your current resource configuration and allows you to access your projects in Foundry without exporting or reimporting data.
@@ -166,17 +162,22 @@ You can now train and deploy your `CNER` project using the **Getting started** w
 
 #### Import a Custom Question Answering (CQA) project
 
-1. In Foundry, navigate to your project.
-1. Select **Fine-tuning** from the left navigation pane.
-1. From the main window, select the **AI Service fine-tuning** tab, and then select **+ Fine-tune**.
-1. In the **Create CQA fine-tuning task** window, select your connected Azure AI Search resource.
-1. Enter a **Name** for your project and select the **Language**.
-1. Optionally, update the **Default answer when no answer is returned** field (default is "No answer found").
-1. Select **Create**.
-1. From the **Getting started** menu, select **Manage sources**.
-1. Select **+ Add source**, and then select **Add Files** to upload your exported question-answer pairs.
+1. In Foundry, navigate to your AI foundry project.
+1. When you export a `CQA` project from Language Studio, you receive a `.zip` file containing your project data. Extract the contents of the `.zip` file to access the underlying files.
+1. In Foundry, select **Fine-tuning** from the left navigation pane.
+1. From the main window, select the **AI Service fine-tuning** tab, and then select your existing `CQA` project or select **+ Fine-tune** to create a new fine-tuning task.
+1. On your `CQA` project Getting started page, select **Edit knowledge base**.
+1. On the **Edit knowledge base** page, select the **Question Answer Pairs** tab then select **Import question and answers**.
+1. Browse for your extracted files then drag and drop the `.tsv` file to import your question-answer pairs (If you had any question-answer pairs in the original project).
+
+    :::image type="content" source="media/question-answer-pairs-import.png" alt-text="Screenshot of the import question-answer pairs dialogue box window.":::
+
+1. Next, select the **Synonyms** tab on the page.
+1. Select **Import Synonyms** and choose the extracted `Synonyms.tsv` file (If you had any synonyms in the original project).
+
+    :::image type="content" source="media/synonyms-import.png" alt-text="Screenshot of the import synonyms dialogue box window.":::
 
-After adding your source files, you can train and deploy the `CQA` project using the **Getting started** workflow in Foundry.
+1. After adding your source files, you can train and deploy the `CQA` project using the **Getting started** workflow in Foundry.
 
 #### Import a Conversational Language Understanding (CLU) project
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マイグレーションスタジオからFoundryへのドキュメントの修正"
}
```

### Explanation
この変更は、Azure Languageサービスにおける「マイグレーションスタジオからFoundryへの」ドキュメントの内容が修正されたことを示しています。主に、日付の更新や手順の明確化が行われており、特にユーザーがFoundryを利用する際の手順に関連するセクションが改善されています。

具体的には、言語リソースの使用に関する手順や、Foundryにおけるプロジェクトのインポート方法がより詳しく説明されています。また、ユーザーがプロジェクトデータをどのようにエクスポートしてインポートするかに関する新しい情報が追加され、特にカスタム質問応答（CQA）プロジェクトや同義語のインポートに関して視覚的な補助情報も含まれています。

新たに追加された画像は、ユーザーがインポートダイアログボックスを視覚的に理解できるようにし、操作をより容易にすることを目的としています。これにより、ユーザーがFoundryへスムーズに移行できるよう、全体的な文書の質と使いやすさが向上しています。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-conversation-pii.md{#item-0d6332}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/18/2025
+ms.date: 04/03/2026
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
@@ -40,10 +40,6 @@ The API attempts to detect all the [defined entity categories](../concepts/conve
 
 For spoken transcripts, the entities detected are returned on the `redactionSource` parameter value provided. Currently, the supported values for `redactionSource` are `text`, `lexical`, `itn`, and `maskedItn` (which maps to Speech to text REST API's `display`\\`displayText`, `lexical`, `itn`, and `maskedItn` format respectively). Additionally, for the spoken transcript input, this API also provides audio timing information to empower audio redaction. For using the audioRedaction feature, use the optional `includeAudioRedaction` flag with `true` value. The audio redaction is performed based on the lexical input format.
 
-> [!NOTE]
-> Conversation PII now supports 40,000 characters as document size.
-
-
 ## Getting PII results
 
 When you get results from PII detection, you can stream the results to an application or save the output to a file on the local system. The API response includes [recognized entities](../concepts/conversations-entity-categories.md), including their categories and subcategories, and confidence scores. The text string with the PII entities redacted is also returned.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話における個人情報の赤塗りに関するドキュメントの修正"
}
```

### Explanation
この変更は、「会話における個人情報（PII）の赤塗り」がどのように行われるかに関するドキュメントが修正されたことを示しています。主に、日付が更新され、不要な情報が削除されており、文書の全体的な明瞭さを向上させるための軽微な編集が行われました。

具体的には、会話PIIのサポートされる最大ドキュメントサイズに関する注意書きが削除されました。この変更により、情報がより簡潔に整理され、ユーザーが重要な点に集中できるようになります。また、APIの使用法や結果の処理についての説明はそのまま残されており、ユーザーがPII検出機能を利用する際の手引きとなる情報が保持されています。

この更新は、文書をより最新のものとし、ユーザーが適切にAPIを使用するための信頼性を高めることを目的としています。


