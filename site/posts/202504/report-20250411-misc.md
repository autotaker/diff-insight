---
date: '2025-04-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a9279bd...MicrosoftDocs:2873777
summary: この差分は、Azure AI Language サービスの「whats-new.md」ファイルのマイナーアップデートに関するものであり、いくつかの重要な新機能と特定の機能の品質向上が含まれています。具体的には、インド、イギリス西部、カナダ東部の3つの新しい地域でのデプロイが可能となり、会話型PII除去サービスの性能が向上しました。また、特に破壊的な変更は見受けられませんが、いくつかのシステム設定に影響を与える可能性があります。全体として、この更新はグローバルな展開を促進し、より多くのユーザーに高精度なサービスを提供することを目指しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a9279bd...MicrosoftDocs:2873777){target="_blank"}

# ハイライト
この差分は、Azure AI Language サービスの「whats-new.md」ファイルに関するマイナーアップデートですが、いくつかの重要な新機能が追加され、特定の機能の品質と精度が向上しています。変更点には新しいデプロイ地域の追加とモデルインフラストラクチャの改善が含まれています。

## 新機能
- Azure AI Language リソースがインド、イギリス西部、カナダ東部の3つの新しい地域でデプロイ可能に。
- 会話型PII除去サービスが継続的にアップグレードされ、識別可能な情報の処理性能が向上。

## 破壊的変更
特に破壊的な変更は見受けられませんが、一部の変更によりシステムの設定や使用方法が変更される可能性があります。

## その他の更新
- 「whats-new.md」ファイルの日付が2025年3月24日から2025年4月10日に変更。
- 固有名詞認識（NER）とテキスト個人識別情報（PII）エンティティ認識モデルのバックエンドインフラストラクチャが更新されました。

# インサイト
この更新は、Azure AI Language サービスのグローバル展開を促進し、多様な地域のユーザーにより高精度なサービスを提供することを目的としています。特に、新しいデプロイ地域の追加は、地理的に分散したユーザー層へのアプローチを広げることを意味しています。これにより、地域特有の法規制やインフラストラクチャの問題を考慮しながら、より多くのユーザーがサービスを利用できるようになります。

また、モデルバックエンドの改善により、従来のモデルよりも高度な分析が可能になります。特に固有名詞認識（NER）や個人識別情報（PII）の認識において、より広範囲にわたるコンテキストを処理できるようになったため、これらのサービスの精度が向上します。

最後に、会話型PII除去サービスの継続的なアップグレードは、AIモデルが日々進化していることを示し、ユーザーが求める高水準のプライバシー保護を実現するための重要なステップです。このような更新により、個人データの漏洩リスクを最小限に抑えつつ、より信頼性の高いサービス提供が可能になります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [whats-new.md](#item-69b272) | minor update | 2025年の言語サービスの新機能と更新状況 | modified | 14 | 2 | 16 | 


# Modified Contents
## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: whats-new
-ms.date: 03/24/2025
+ms.date: 04/10/2025
 ms.author: jboback
 ---
 
@@ -16,7 +16,19 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
 
 ## March 2025
 
-* Our [Conversational PII redaction](personally-identifiable-information/how-to/redact-conversation-pii.md?tabs=client-libraries) service is now powered by an upgraded GA model. This updated 2024-02-01 version includes improved quality and accuracy in Credit card number entities and numeric identification entities, such as Social Security numbers, driver’s license numbers, policy numbers, Medicare Beneficiary Identifiers, and Financial account numbers.
+* Azure AI Language resource now can be deployed to 3 new regions, Jio India Central, UK West and Canada East, for the following capabilities: 
+ * Language detection 
+ * Sentiment analysis 
+ * Key phrase extraction 
+ * Named entity recognition (NER) 
+ * Personally identifiable information (PII) entity recognition 
+ * Entity linking 
+ * Text analytics for health 
+ * Extractive text summarization 
+
+* Back-end infrastructure for the Named entity recognition (NER) and Text Personally identifiable information (PII) entity recognition models is now updated with extended context window limits. 
+
+* Our [Conversational PII redaction](personally-identifiable-information/how-to/redact-conversation-pii.md?tabs=client-libraries) service is now powered by an upgraded GA model. This updated version includes improved quality and accuracy in Credit card number entities and Numeric identification entities, such as Social Security numbers, Driver’s license numbers, Policy numbers, Medicare Beneficiary Identifiers, and Financial account numbers.
 
 ## February 2025
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "2025年の言語サービスの新機能と更新状況"
}
```

### Explanation
この変更は、Azure AI Language サービスの「whats-new.md」ファイルに対する更新です。主な変更点は日付の修正と新機能の追加です。具体的には、日付が2025年3月24日から2025年4月10日に変更されました。

また、2025年3月のセクションにおいて、Azure AI Language リソースが新たにインドのジオ、イギリスの西部、およびカナダの東部の3つの新しい地域にデプロイできることが追加されました。これにより、言語検出、感情分析、重要フレーズ抽出、固有名詞認識（NER）、個人識別情報（PII）エンティティ認識、エンティティリンク、健康に関するテキスト分析、抽出的テキスト要約などの機能が利用可能になります。

さらに、固有名詞認識（NER）とテキスト個人識別情報（PII）エンティティ認識モデルのバックエンドインフラストラクチャも更新され、拡張されたコンテキストウィンドウの制限が適用されています。これにより、これらの機能の質と精度が向上します。

最後に、会話型PII除去サービスに関する情報も改訂され、継続的なモデルのアップグレードについての情報が含まれています。これにより、クレジットカード番号や社会保障番号、運転免許証番号などの識別可能なエンティティの品質と精度が向上したことが強調されています。


