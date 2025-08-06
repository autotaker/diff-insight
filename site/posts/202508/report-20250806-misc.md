---
date: '2025-08-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:88b6cf1...MicrosoftDocs:10d2435
summary: この差分では、IDドキュメントモデルにおける地域カバレッジの表現が更新され、Document Intelligence APIがサポートする地域が明確に示されました。新機能の追加はなく、文書の内容が具体的になり、ユーザーの理解を助けています。互換性が壊れる変更もなく、地域カバレッジに関する文が修正され、行数の調整も行われました。この変更は、APIの地理的範囲を包括的に表現し、ユーザーが地域を正しく理解できるようにすることを目的としています。結果として、情報の正確性と信頼性が向上しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:88b6cf1...MicrosoftDocs:10d2435){target="_blank"}

# ハイライト
この差分では、IDドキュメントモデルにおける地域カバレッジの表現が更新され、Document Intelligence APIがサポートする地域がより明確に示されるようになりました。

## 新機能
特に新しい機能の追加はありませんが、文書の内容がより具体的になり、ユーザーの理解を助ける目的が達成されています。

## 互換性が壊れる変更
互換性が壊れる変更はありません。

## その他の更新
- 地域カバレッジに関する文の修正。
- 合計7行が削除され、3行が追加されました。

# インサイト
この更新の背景には、Document Intelligence APIの地域サポートに関する誤解を避ける目的があります。今回の変更により、APIが対象とする地理的範囲がより包括的なものとして表現され、ユーザーが利用可能な地域を正しく理解できるようになりました。以前の文書では「アメリカ合衆国を含む」という表現が用いられていましたが、これが「北アメリカ、南アメリカを含む」に変わり、サービスが幅広い地域を対象としていることが明確になっています。

これは、グローバル市場において身分証明認識サービスの使用範囲を広げたいという戦略的意図があると考えられ、結果として、ユーザーに対する情報提供がより正確で信頼できるものになります。また、削除された内容については、冗長性を省きつつも、新たに追加された具体的な表現により文書の質が向上していることが伺えます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [id-document.md](#item-bf45fa) | minor update | IDドキュメントモデルの地域カバレッジの更新 | modified | 3 | 7 | 10 | 


# Modified Contents
## articles/ai-services/document-intelligence/prebuilt/id-document.md{#item-bf45fa}

<details>
<summary>Diff</summary>
````diff
@@ -34,21 +34,17 @@ ms.custom: references.regions
 
 > [!NOTE]
 >
-> Document Intelligence `v4.0 2024-11-30 (GA)` API for the prebuilt Identity document (ID) model now supports identification documents from all regions worldwide, including expanded coverage across the United States, Asia, Europe, Africa, and Oceania.
->
+> Document Intelligence `v4.0 2024-11-30 (GA)` API for the prebuilt Identity document (ID) model now supports identification documents from all regions worldwide, including expanded coverage across North America, South America, Asia, Europe, Africa, and Oceania.
 
-> [!NOTE]
->
-> Document Intelligence Identity document (ID) model combines Optical Character Recognition (OCR) with deep learning models to analyze and extract key information from identity documents. The API analyzes identity documents (including the following) and returns a structured JSON data representation.
+Document Intelligence Identity document (ID) model combines Optical Character Recognition (OCR) with deep learning models to analyze and extract key information from identity documents. The API analyzes identity documents (including the following) and returns a structured JSON data representation.
 
 | Region | Document types |
 |--------|----------------|
 |Worldwide|Passport Book, Passport Card|
 |United States|Driver License, Identification Card, Residency Permit (Green card), Social Security Card, Military ID|
-|Europe|Driver License, Identification Card, Residency Permit|
 |India|Driver License, PAN Card, Aadhaar Card|
-|Canada|Driver License, Identification Card, Residency Permit (Maple Card)|
 |Australia|Driver License, Photo Card, Key-pass ID (including digital version)|
+|Other|Driver License, Identification Card, Residency Permit|
 
 ::: moniker-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "IDドキュメントモデルの地域カバレッジの更新"
}
```

### Explanation
この差分では、IDドキュメントモデルに関する文書に minor update が実施されました。主な変更点は、Document Intelligence APIが全世界の身分証明書をサポートすることを明確にするために、地域カバレッジに関する表現の調整が行われたことです。

具体的には、「アメリカ合衆国を含む」から「北アメリカ、南アメリカを含む」という記載に変更され、地域のカバレッジがより正確に反映されています。この更新により、二つの地域名が明記され、推奨される文書内の情報がより具体的かつ包括的な内容になっています。

また、7行の削除と3行の追加がありましたが、内容の一部が削除される一方で重要な情報が明確化されたことで、ドキュメントの質が向上しています。この変更は、ユーザーがDocument Intelligence APIを利用する際の理解をより助けることを目的としています。


