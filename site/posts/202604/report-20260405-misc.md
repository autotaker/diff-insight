---
date: '2026-04-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dd1a03a...MicrosoftDocs:e462261
summary: Azure Languageサービスのデータ制限に関するドキュメントが更新され、「会話のPIIデータを赤actionする方法」についての情報が強化されました。データ制限の見出しが「Maximum
  value」に変更され、具体的な制限の詳細が明確化されています。これにより、ユーザーは機能の制約をより直感的に理解できるようになり、サービスの効率的な利用が期待されます。特に、会話のPIIデータに関する情報が整理され、API利用時の手続きや制限の理解が容易になりました。この更新は、全てのステークホルダーに透明性のあるシステム利用を提供し、大規模なテキスト分析を行うユーザーにとって重要な資産となります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dd1a03a...MicrosoftDocs:e462261){target="_blank"}

# Highlights
Azure Languageサービスのデータ制限に関するドキュメントと、「会話のPIIデータを赤actionする方法」ドキュメントがアップデートされました。データ制限の見出しがより具体的に「Maximum value」に変更され、制限の詳細が明確化されています。また、PIIデータの赤actionに関する情報が強化されて、API利用時の手続きや制限に関する理解が容易になっています。

## New features
- 会話のPIIデータドキュメントにおいて、API応答の保持時間や機能説明が追加。
- データ制限における「Maximum value」という明確な見出しの追加。

## Breaking changes
- 特に破壊的な変更はありませんが、すべてのユーザーに影響を与える可能性があるため、注意が必要です。

## Other updates
- 説明が整理され、読みやすさが向上。
- 箇条書きによる情報提供により、内容把握が容易。

# Insights
このドキュメント更新は、Azure Languageサービスのユーザーにとって、システムリミテーションの理解を大幅に向上させるものです。特にデータ制限の見出しが「Value」から「Maximum value」に変更された点は、各機能が持つ制約を直感的に理解する助けとなるでしょう。これにより、ユーザーは各機能の制限を事前に把握し、より効率的にサービスを利用することが可能になります。

一方、会話のPIIデータに関しては、非同期機能の応答保持期間や、各会話アイテムに関する制限が明記されており、APIを利用したプロセスの構築やトラブルシューティングが容易になります。赤action機能の詳細な記述は、セキュリティリスクの軽減に貢献するでしょう。

これにより、技術者だけでなく、サービスを計画/利用するすべてのステークホルダーにとって、より透明性のあるシステム利用が期待できます。更新されたドキュメントは、特に大規模なテキスト分析を行うユーザーにとって、計画的なリソース配分と効率化に繋がる重要な資産となるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [data-limits.md](#item-48b8af) | minor update | データ制限の更新: 記載方法の改善 | modified | 5 | 5 | 10 | 
| [redact-conversation-pii.md](#item-0d6332) | minor update | 会話のPIIデータの赤action方法に関する更新 | modified | 14 | 5 | 19 | 


# Modified Contents
## articles/ai-services/language-service/concepts/data-limits.md{#item-48b8af}

<details>
<summary>Diff</summary>
````diff
@@ -41,12 +41,12 @@ When using features of Azure Language, keep the following information in mind:
 
 | The following limit specifies the maximum number of characters that can be in a single document. |
 
-| Feature | Value |
+| Feature | Maximum value |
 | ------------------------ | --------------- |
-| Text Analytics for health | 125,000 characters as measured by [StringInfo.LengthInTextElements](/dotnet/api/system.globalization.stringinfo.lengthintextelements). |
-| Conversation PII | ≤ 1,000 characters as measured by the [**Analyze Conversations** API](/rest/api/language/analyze-conversations/analyze-conversations/analyze-conversations) default conversation item length. |
-| All other preconfigured features (synchronous) | 5,120 as measured by [StringInfo.LengthInTextElements](/dotnet/api/system.globalization.stringinfo.lengthintextelements). If you need to submit larger documents, consider using the feature asynchronously. |
-| All other preconfigured features ([asynchronous](use-asynchronously.md)) | 125,000 characters across all submitted documents, as measured by [StringInfo.LengthInTextElements](/dotnet/api/system.globalization.stringinfo.lengthintextelements) (maximum of 25 documents). |
+| **Text Analytics for health** | 125,000 characters as measured by [StringInfo.LengthInTextElements](/dotnet/api/system.globalization.stringinfo.lengthintextelements). |
+| **Conversation PII** | 1,000 characters as measured by [**Analyze Conversations** API](/rest/api/language/analyze-conversations/analyze-conversations/analyze-conversations). A conversation can have a list of conversation items (turns). 1,000 is the max limit for each conversation item (not for the entire conversation). The conversation PII API supports asynchronous requests only. |
+| **All other preconfigured features (synchronous)** | 5,120 as measured by [StringInfo.LengthInTextElements](/dotnet/api/system.globalization.stringinfo.lengthintextelements). If you need to submit larger documents, consider using the feature asynchronously. |
+| **All other preconfigured features ([asynchronous](use-asynchronously.md))** | 125,000 characters across all submitted documents, as measured by [StringInfo.LengthInTextElements](/dotnet/api/system.globalization.stringinfo.lengthintextelements) (maximum of 25 documents). |
 
 If a document exceeds the character limit, the API behaves differently depending on how you're sending requests.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ制限の更新: 記載方法の改善"
}
```

### Explanation
この変更では、Azure Languageサービスのドキュメントにおけるデータ制限に関する表記が改善されました。具体的には、制限の説明の見出しが「Value」から「Maximum value」に変更され、各機能に関する説明も明確化されています。特に、「Conversation PII」機能の説明が詳しくなり、会話アイテムごとの最大制限や非同期リクエストのサポートについて言及されています。

この変更により、読者が機能のデータ制限に関する理解を深めやすくなることを目的としています。変更された内容は、特にテキスト分析や非同期機能を利用する際の限界について、より明確に示されています。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-conversation-pii.md{#item-0d6332}

<details>
<summary>Diff</summary>
````diff
@@ -30,15 +30,24 @@ The conversational PII API supports all Azure regions supported by Azure Languag
 
 ## Submitting data
 
-You can submit the input to the API as list of conversation items. Analysis is performed upon receipt of the request. Because the API is asynchronous, there may be a delay between sending an API request, and receiving the results. For information on the size and number of requests you can send per minute and second, see the following data limits.
+* You can submit the input to the API as list of conversation items. Analysis is performed upon receipt of the request. Because the API is asynchronous, there may be a delay between sending an API request, and receiving the results. For information on the size and number of requests you can send per minute and second, see the following data limits.
 
-When you use the async feature, the API results are available for 24 hours from the time the request was ingested, and is indicated in the response. After this time period, the results are purged and are no longer available for retrieval.
+* When you use the async feature, the API results are available for 24 hours from the time the request was ingested, and is indicated in the response. After this time period, the results are purged and are no longer available for retrieval.
 
-When you submit data to conversational PII, you can send one conversation (chat or spoken) per request.
+* When you submit data to conversational PII, you can send one conversation (chat or spoken) per request.
 
-The API attempts to detect all the [defined entity categories](../concepts/conversations-entity-categories.md) for a given conversation input. If you want to specify which entities are detected and returned, use the optional `piiCategories` parameter with the appropriate entity categories.
+* The API attempts to detect all the [defined entity categories](../concepts/conversations-entity-categories.md) for a given conversation input. If you want to specify which entities are detected and returned, use the optional `piiCategories` parameter with the appropriate entity categories.
 
-For spoken transcripts, the entities detected are returned on the `redactionSource` parameter value provided. Currently, the supported values for `redactionSource` are `text`, `lexical`, `itn`, and `maskedItn` (which maps to Speech to text REST API's `display`\\`displayText`, `lexical`, `itn`, and `maskedItn` format respectively). Additionally, for the spoken transcript input, this API also provides audio timing information to empower audio redaction. For using the audioRedaction feature, use the optional `includeAudioRedaction` flag with `true` value. The audio redaction is performed based on the lexical input format.
+* For spoken transcripts, the entities detected are returned on the `redactionSource` parameter value provided. Currently, the supported values for `redactionSource` are `text`, `lexical`, `itn`, and `maskedItn` (which maps to Speech to text REST API's `display`\\`displayText`, `lexical`, `itn`, and `maskedItn` format respectively). Additionally, for the spoken transcript input, this API also provides audio timing information to empower audio redaction. For using the audioRedaction feature, use the optional `includeAudioRedaction` flag with `true` value. The audio redaction is performed based on the lexical input format.
+
+* A conversation can have a list of conversation items (turns). There's a 1000 max limit for each conversation item (not for the entire conversation):
+
+  * ***Multi-turn conversation example***<br><br>
+  
+     > [!div class="checklist"]
+     > * (conv item1) User: Hi! <br>
+     > * (conv item2) Bot: Hello, how can I help? <br>
+     > * (conv item3) User: What time does the next train leave for Paris? <br>
 
 ## Getting PII results
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話のPIIデータの赤action方法に関する更新"
}
```

### Explanation
この変更では、「会話のPIIデータを赤actionする方法」に関するドキュメントが更新され、情報が強化されています。具体的には、APIを通じて送信するデータの形式に関する記述が箇条書きになり、読みやすさが向上しました。また、会話アイテムのリストに関する新しい説明が追加され、各会話アイテムに最大1000の制限があることが明示されています。

さらに、「非同期機能」を使用している場合のAPIの応答が24時間保持されること、発話のトランスクリプトにおいて音声の赤action機能を使用する方法など、多くの具体的な情報が追加されています。この更新により、ユーザーがAPIを利用する際の手続きや制限について、より明確な理解を得られることを目的としています。


