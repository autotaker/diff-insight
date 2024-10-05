---
date: '2024-10-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7d913a4...MicrosoftDocs:1b56c27
summary: この更新は、AIサービスのリリースノートとAIスタジオのモデル推論情報に関するマイナーな変更を含んでいます。具体的には、リリースノートに2024年8月の更新情報が追加され、Conversational
  Language Understanding (CLU) の発話制限の引き上げや新しいトレーニング設定バージョンが記載されました。また、Conversational
  PII検出サービスが2024年7月に一般提供されることが言及されています。破壊的変更はなく、リリースノートの日付が1930年から2024年10月4日に修正された他、AIスタジオの項目名のフォーマットがアンダースコアからハイフン形式に統一されました。これらの変更はユーザー体験の向上を目指しており、特に開発者やデータサイエンティストにとって有益です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7d913a4...MicrosoftDocs:1b56c27){target="_blank"}

# ハイライト
この更新は、AIサービスのリリースノートとAIスタジオのモデル推論情報に関するマイナーな変更を含んでいます。

## 新機能
- リリースノートに2024年8月の更新情報が追加され、Conversational Language Understanding (CLU) の発話制限の引き上げや新しいトレーニング設定バージョンについて記載。
- Conversational PII検出サービスの一般提供（GA）が2024年7月に言及されている。

## 破壊的変更
- なし。

## その他の更新
- リリースノートの日付が1930年ではなく、2024年10月4日に修正された。
- AIスタジオの「モデル推論情報」文書における項目名のフォーマットがアンダースコアからハイフン形式に統一。

# インサイト
AIサービスのリリースノートにおける更新は、ユーザーが新しい機能や改善を利用できるようにするための重要な情報提供を目的としています。特に、Conversational Language Understandingにおける発話制限の緩和や、最新のトレーニング設定への言及は、開発者やデータサイエンティストにとって有益です。これらの更新により、より多くのデータを扱えるようになり、モデルの訓練における柔軟性を向上させます。

また、AIスタジオの「モデル推論情報」でのフォーマット修正は、文書を一貫性のあるものにし、項目名の読みやすさを向上させています。この修正は、セットアップやパイプラインの設定時にエラーを防ぎ、ユーザーが異なるAPIやライブラリを使用する際の一貫性を確保します。特に、異なるツール間での作業が必要なプロジェクトでは、このような細かなフォーマットの統一が重要です。

これらの変更は、全体的なユーザー体験の向上を目指しており、新しい技術やサービスの適応を促進します。リリースノートの更新やフォーマットの統一は地味ながらも、長期的には大きな影響を与えることがあります。ユーザーにとっての利便性向上を意識した更新です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [whats-new.md](#item-69b272) | minor update | リリースノートの更新 | modified | 5 | 1 | 6 | 
| [reference-model-inference-info.md](#item-e465b4) | minor update | モデル推論情報の項目形式の修正 | modified | 5 | 5 | 10 | 


# Modified Contents
## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: whats-new
-ms.date: 08/22/2024
+ms.date: 10/04/2024
 ms.author: jboback
 ---
 
@@ -19,6 +19,10 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
 
 * Custom Summarization has been discontinued and is no longer available in the Studio and documentation.
 
+## August 2024
+* [CLU utterance limit in a project](conversational-language-understanding/service-limits.md#data-limits) increased from 25,000 to 50,000.
+* [CLU new version of training configuration, version 2024-08-01-preview, is available now](conversational-language-understanding/concepts/best-practices.md#address-out-of-domain-utterances), which improves the quality of intent identification for out of domain utterances.
+
 ## July 2024
 
 * [Conversational PII redaction](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/announcing-conversational-pii-detection-service-s-general/ba-p/4162881) service in English-language contexts is now Generally Available (GA).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リリースノートの更新"
}
```

### Explanation
この変更は、AI言語サービスに関するリリースノートを更新するもので、主に日付の修正と新機能の追加が含まれています。具体的には、1930年8月22日の日付が2024年10月4日に変更され、2024年8月に関する重要な更新内容が新たに追加されました。これには、Conversational Language Understanding (CLU) の発話制限の引き上げや、最新のトレーニング設定バージョンの提供に関する情報が含まれています。また、2024年7月のConversational PII検出サービスの一般提供（GA）についても言及されています。これにより、ユーザーは最新のサービスや機能に関する情報を得ることができます。

## articles/ai-studio/reference/reference-model-inference-info.md{#item-e465b4}

<details>
<summary>Diff</summary>
````diff
@@ -115,9 +115,9 @@ The inference task associated with the mode.
 
 | Name | Type | Description |
 | --- | --- | --- |
-| audio\_generation | string | A text-to-audio generative model.  |
-| chat_completion | string | A model capable of taking chat-formatted messages and generate responses.    |
+| audio-generation | string | A text-to-audio generative model.  |
+| chat-completions | string | A model capable of taking chat-formatted messages and generate responses.    |
 | embeddings | string | A model capable of generating embeddings from a text.    |
-| image\_embeddings | string | A model capable of generating embeddings from an image and text description.  |
-| image\_generation | string | A model capable of generating images from an image and text description.  |
-| text\_generation | string | A text generation model.    |
+| image-embeddings | string | A model capable of generating embeddings from an image and text description.  |
+| image-generation | string | A model capable of generating images from an image and text description.  |
+| text-generation | string | A text generation model.    |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル推論情報の項目形式の修正"
}
```

### Explanation
この変更は、AIスタジオの「モデル推論情報」文書におけるテーブルのフォーマットを修正するもので、主にパイプラインで使用される項目名のハイフン形式への変更が含まれています。具体的には、項目名がアンダースコア（_）からハイフン（-）に変更され、より一貫性のある形式となりました。これには、`audio_generation` が `audio-generation`、`chat_completion` が `chat-completions`、`image_embeddings` が `image-embeddings`、`image_generation` が `image-generation`、そして `text_generation` が `text-generation` といった変更が含まれています。これにより、文書の可読性が向上し、ユーザーが項目をより簡単に理解できるようになります。


