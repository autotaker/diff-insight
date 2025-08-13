---
date: '2025-08-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fd2e69f...MicrosoftDocs:ebf24ba
summary: この変更は、Azure AI Languageの個人を特定できる情報（PII）検出機能に関するドキュメントの小規模な更新です。主な内容として、日付の修正とエンティティ名の一部変更が行われています。新機能は特にありませんが、情報の更新が適用され、破壊的な変更も含まれていません。この更新は、ドキュメントの情報の正確性を高めることを目的としており、ユーザーにとって重要な情報が最新の状態に保たれています。エンティティ名の変更により、ユーザーがより正確な情報を元に操作を行えるようになり、ドキュメントの信頼性向上にも寄与します。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fd2e69f...MicrosoftDocs:ebf24ba){target="_blank"}

# Highlights
この変更は、Azure AI Languageの個人を特定できる情報（PII）検出機能に関するドキュメントの小規模な更新です。主要な変更として、日付の修正と、エンティティ名の一部変更があります。

## New features
特定された新機能はありませんが、情報の更新が適用されています。

## Breaking changes
特に破壊的な変更は含まれていません。

## Other updates
1. 日付が2025年3月24日から2025年8月11日、及び2025年5月15日から2025年8月1日に変更されました。
2. エンティティ名が「SortCard」から「SortCode」に変更されました。

# Insights
この更新は、Azure AI Languageのドキュメントにおける情報の正確性を高めるためのマイナーな修正となっています。特に、リリース及びプレビュー版の日付を最新の状態に保つことは、ユーザーが現在の製品バージョンに即した情報を得るために重要です。

また、エンティティ名の変更は、名称がより実情に即したものであることを示唆しています。これにより、ユーザーがドキュメントを参照した際に混乱せず、正確な情報を元に操作を行えるというメリットがあります。この種の変更は一見小さなものに見えるかもしれませんが、長期的にはドキュメントの信頼性向上に寄与します。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [overview.md](#item-8a6932) | minor update | 新しい情報の更新と日付の修正 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/ai-services/language-service/personally-identifiable-information/overview.md{#item-8a6932}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 03/24/2025
+ms.date: 08/11/2025
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
@@ -20,11 +20,11 @@ Azure AI Language Personally Identifiable Information (PII) detection is a featu
 
 ## What's new
 
-The 2025-05-15-preview introduces several new entities:
+The 2025-08-01-preview introduces several new entities:
 
 * [**DateOfBirth**](concepts/entity-categories.md#category-datetime) with English, French, German, Italian, Spanish, Portuguese, Brazilian Portuguese, and Dutch language support.
 * [**LicensePlate**](concepts/entity-categories.md#type-license-plate-) with English language support.
-* [**SortCard**](concepts/entity-categories.md#type-sort-code-) with English language support.
+* [**SortCode**](concepts/entity-categories.md#type-sort-code-) with English language support.
 
 
 The Text PII and Conversational PII detection preview API (version `2024-11-15-preview`) now supports the option to mask detected sensitive entities with a label beyond just redaction characters. Customers can specify if personal data content such as names and phone numbers, that is, `"John Doe received a call from 424-878-9192"`, are masked with a redaction character, that is, `"******** received a call from ************"`, or masked with an entity label, that is, `"[PERSON_1] received a call from [PHONENUMBER_1]"`. More on how to specify the redaction policy style for your outputs can be found in our [how-to guides](how-to-call.md). 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しい情報の更新と日付の修正"
}
```

### Explanation
この変更は、Azure AI Languageの個人を特定できる情報（PII）検出機能に関するドキュメントの小規模な更新を示しています。主に、併記されている日付が2025年3月24日から2025年8月11日に修正され、新しいプレビュー版の日付が2025年5月15日から2025年8月1日に変更されています。さらに、エンティティのリストも含まれており、「SortCard」が「SortCode」に名称変更され、適切なリンクが維持されています。

これにより、ドキュメントは最新のプロダクトリリースを正確に反映し、利用者に新機能に関する信頼性のある情報を提供できるようになっています。全体として、わずかな修正でありながら、情報の正確性を高める重要なアップデートとなります。


