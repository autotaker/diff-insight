---
date: '2025-11-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:36ddb61...MicrosoftDocs:0ae942c
summary: このコード差分の変更点は、`prebuilt.md`ファイル内の質問応答APIサンプルへのリンクを更新したことです。古いリンクが新しいリンクに置き換えられ、ユーザーは最新のAPIドキュメンテーションにアクセスできるようになります。この変更は、既存の機能に影響を及ぼさず、破壊的な要素は含まれていません。具体的には、古いURLを削除し新しいURLを追加する変更が行われました。このメンテナンス作業は、ユーザーの利便性を向上させ、ドキュメントの品質を維持するために重要です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:36ddb61...MicrosoftDocs:0ae942c){target="_blank"}

# Highlights
このコード差分の変更点は、`prebuilt.md`ファイル内の質問応答APIサンプルへのリンク更新です。リンク先が「Language/stable」から「LanguageQuestionAnswering/stable」へと変更されており、ユーザーが最新のAPIドキュメンテーションにアクセスできるように改良されています。

## New features
変更は、既存のリンクを新しいリンクに置き換えることであり、新しいAPIサンプルのリファレンス先へのアクセスが可能になる点です。

## Breaking changes
この変更には重大な破壊的要素は含まれておらず、すでに存在するAPIの使用法や機能に影響を及ぼすものではありません。

## Other updates
1行の削除と1行の追加のみが行われ、合計2つの行が変更されました。具体的には、古いURLを削除して新しいURLを追加しています。

# Insights
今回の変更は、ユーザーの利便性を向上させるために、APIドキュメンテーションリンクを最新情報に即したものに更新するという小規模ながらも重要なメンテナンス作業です。このようなリンク先の変更は、古いリファレンスに基づいた誤った情報やデッドリンクによる混乱を避けるために必要です。質問応答サービスのAPIに関する利用者は、この変更により最新の公式ドキュメンテーションに直接アクセスできるため、開発プロセスが円滑に進むことが期待できます。この種のリンク更新は、ドキュメント品質を維持し、ユーザーエクスペリエンスを向上させる上での重要な一環です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [prebuilt.md](#item-a28843) | minor update | APIサンプルのリンクの更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/language-service/question-answering/how-to/prebuilt.md{#item-a28843}

<details>
<summary>Diff</summary>
````diff
@@ -221,4 +221,4 @@ Language code|Language
 
 ## Prebuilt API reference
 
-Visit the [full prebuilt API samples](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/Language/stable/2021-10-01/examples/questionanswering/SuccessfulQueryText.json) documentation to understand the input and output parameters required for calling the API.
+Visit the [full prebuilt API samples](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/LanguageQuestionAnswering/stable/2021-10-01/examples/questionanswering/SuccessfulQueryText.json) documentation to understand the input and output parameters required for calling the API.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIサンプルのリンクの更新"
}
```

### Explanation
この変更は、`prebuilt.md`ファイル内のAPIサンプルへのリンクを更新することに関するものです。具体的には、質問応答APIのサンプルへのURLが新しい場所に変更されています。変更された行は、以前のリンクから新しいリンクに替わり、リンク先は「Language/stable」から「LanguageQuestionAnswering/stable」へと修正されています。この変更により、ユーザーは最新のドキュメンテーションにアクセスしやすくなります。全体として、1行の追加と1行の削除があり、合計で2つの変更があります。


