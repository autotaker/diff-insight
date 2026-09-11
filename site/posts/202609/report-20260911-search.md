---
date: '2026-09-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0d6f6ab...MicrosoftDocs:54bcca9
summary: この変更は、Azure AI Searchの光学文字認識（OCR）スキルに関する記事にマイナーなアップデートが行われたことを示しています。新しいAI使用に関する情報が追加され、OCRスキルが利用するAPIのバージョンに関するリンクが更新されました。重大な変更やブレイキングチェンジは報告されておらず、一部の表現が明確化されました。この更新により、ユーザーは最新の情報に基づいてOCRスキルを適切に利用できるようになり、全体的なドキュメントの有用性とわかりやすさが向上しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0d6f6ab...MicrosoftDocs:54bcca9){target="_blank"}

# Highlights
この変更は、Azure AI Search の光学文字認識（OCR）スキルに関する記事に対するマイナーアップデートが行われたことを示しています。新しい情報の追加と一部リンクの修正が主なポイントです。

## New features
- AI の使用に関する情報が追加されました。
- OCRスキルが利用するAPIのバージョンに関する最新のリンクが更新されました。

## Breaking changes
- 特に重大な変更や breaking change は報告されていません。

## Other updates
- ドキュメント内の表現が一部明確化されました。

# Insights
この更新は、Azure AI Search の光学文字認識（OCR）スキルに関連するドキュメントに小さな調整を加え、ユーザーが最新の情報を基にOCRスキルを適切に使用できるようにしたものです。特に、APIバージョンに関するリンクが最新のものに更新されているため、これによりユーザーは最新の技術に基づいてサービスを利用することが可能になります。また、AI 使用に関する新しい情報の追加により、ユーザーはAIテクノロジーの利用方法や利点をより深く理解することが期待されます。これらの変更は、全体的にドキュメントの有用性とわかりやすさを向上させ、ユーザーエクスペリエンスを良くすることを目的としています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-ocr.md](#item-259256) | minor update | OCRスキルに関する記事の更新 | modified | 5 | 3 | 8 | 


# Modified Contents
## articles/search/cognitive-search-skill-ocr.md{#item-259256}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +1,12 @@
 ---
 title: OCR Skill
 description: Extract text from image files using optical character recognition (OCR) in an enrichment pipeline in Azure AI Search.
+ai-usage: ai-assisted
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
+  - doc-kit-assisted
 ms.topic: reference
 ms.date: 01/07/2026
 ms.update-cycle: 365-days
@@ -15,11 +17,11 @@ ms.update-cycle: 365-days
 
 The **optical character recognition (OCR)** skill recognizes printed and handwritten text in image files. This article is the reference documentation for the OCR skill. See [Extract text from images](cognitive-search-concept-image-scenarios.md) for usage instructions.
 
-The **OCR** skill uses the machine learning models provided by [Azure Vision in Foundry Tools](/azure/ai-services/computer-vision/overview) API [v3.2](https://westus.dev.cognitive.microsoft.com/docs/services/computer-vision-v3-2/operations/5d986960601faab4bf452005). The **OCR** skill maps to the following functionality:
+The **OCR** skill uses the machine learning models provided by [Azure Vision in Foundry Tools](/azure/ai-services/computer-vision/overview) API [v3.2](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/ComputerVision/stable/v3.2). The **OCR** skill maps to the following functionality:
 
 + For the languages listed under [Azure Vision language support](/azure/ai-services/computer-vision/language-support#optical-character-recognition-ocr), the [Read API](/azure/ai-services/computer-vision/overview-ocr) is used.
 
-+ For Greek and Serbian Cyrillic, the legacy [OCR in version 3.2](https://github.com/Azure/azure-rest-api-specs/tree/master/specification/cognitiveservices/data-plane/ComputerVision/stable/v3.2) API is used.
++ For Greek and Serbian Cyrillic, the legacy [OCR in version 3.2](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/ComputerVision/stable/v3.2) API is used.
 
 The **OCR** skill extracts text from image files and embedded images. Supported file formats include:
 
@@ -42,7 +44,7 @@ Parameters are case sensitive.
 
 | Parameter name     | Description |
 |--------------------|-------------|
-| `detectOrientation`    | Detects image orientation. Valid values are `true` or `false`. </p>This parameter only applies if the [legacy OCR version 3.2](https://github.com/Azure/azure-rest-api-specs/tree/master/specification/cognitiveservices/data-plane/ComputerVision/stable/v3.2) API is used.  |
+| `detectOrientation`    | Detects image orientation. Valid values are `true` or `false`. </p>This parameter only applies if the [legacy OCR version 3.2](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/ComputerVision/stable/v3.2) API is used.  |
 | `defaultLanguageCode` | Language code of the input text. Supported languages include all of the [generally available languages](/azure/ai-services/computer-vision/language-support#analyze-image) of Azure Vision. You can also specify `unk` (Unknown). </p>If the language code is unspecified or null, the language is set to English. If the language is explicitly set to `unk`, all languages found are auto-detected and returned.|
 | `lineEnding` | The value to use as a line separator. Possible values: "Space", "CarriageReturn", "LineFeed".  The default is "Space". |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OCRスキルに関する記事の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける光学文字認識（OCR）スキルに関するドキュメントファイル`cognitive-search-skill-ocr.md`に対するマイナーアップデートです。具体的には、ファイルが5行追加され、3行が削除され、合計で8行の変更が行われました。主な変更点には、AIの使用に関する情報の追加とリンクの修正が含まれています。特に、OCRスキルが利用するAPIのバージョンに関するリンクが更新され、ドキュメント内の一部の表現が明確化されました。これにより、ユーザーは最新の情報に基づいてOCRスキルをより正確に理解し、使用することができます。


