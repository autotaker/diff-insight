---
date: '2025-06-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2e48ee2...MicrosoftDocs:1531236
summary: カスタムニューラルモデルのサポート状況に関するテーブルが更新され、全てのフィールドタイプに対応していることが示されました。新機能として、カスタムニューラルモデルが「✔️Supported」と表記され、これに対する重大な互換性の破壊はありません。テーブル内の記述も「Unsupported」から「✔️Supported」に変更され、ユーザーがより正確な情報を得られるようになっています。今回の更新により、カスタムラベル機能に関連するドキュメントの正確性と明瞭性が向上し、サービス利用者は最新の情報に基づいて、機能の設定や利用をより適切に行えるよう支援されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2e48ee2...MicrosoftDocs:1531236){target="_blank"}

<format>
# ハイライト
カスタムニューラルモデルのサポート状況に関するテーブルの内容が更新され、モデルが全てのフィールドタイプをサポートすることが示されました。

## 新機能
- カスタムニューラルモデルが「✔️Supported」と表記され、全フィールドタイプに対応していることが明示されています。

## 破壊的変更
- 今回の更新で重大な互換性の破壊は発生していません。

## その他の更新
- テーブル内の記述が「Unsupported」から「✔️Supported」に変更されました。

# 洞察
今回のテーブル更新は、カスタムラベル機能に関連するドキュメントの内容の正確性と明瞭性を向上させることを目的としています。特に、カスタムニューラルモデルに関する情報が誤解を招く可能性があったため、サポート状況を正確に表すように修正されました。ユーザーはこれによって、モデルが対応可能なフィールドタイプについての見解をより正確に得ることができます。

ドキュメントはユーザーが技術情報に基づいて適切な判断を下すための重要なリソースです。したがって、この更新は、サービス利用者が最新の情報に基づいて、カスタムラベル機能の設定や利用をより効果的に行うことを支援するものであると言えます。また、このような更新が続くことで、ドキュメントの信頼性が向上し、長期的にはユーザーとの信頼関係の構築にもつながることでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [custom-labels.md](#item-90435a) | minor update | カスタムラベルの表の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/train/custom-labels.md{#item-90435a}

<details>
<summary>Diff</summary>
````diff
@@ -82,7 +82,7 @@ Custom neural models currently only support key-value pairs, structured fields (
 
 | Model type | Form fields | Selection marks | Tabular fields | Signature | Region | Overlapping fields |
 |---|---|---|---|---|---|
-| Custom neural | ✔️Supported | ✔️Supported | ✔️Supported | Unsupported | ✔️Supported<sup>1</sup> | ✔️Supported<sup>2</sup> |
+| Custom neural | ✔️Supported | ✔️Supported | ✔️Supported | ✔️Supported | ✔️Supported<sup>1</sup> | ✔️Supported<sup>2</sup> |
 | Custom template | ✔️Supported| ✔️Supported | ✔️Supported | ✔️Supported | ✔️Supported | Unsupported |
 
 <sup>1</sup> Region labeling implementation differs between template and neural models. For template models, the training process injects synthetic data at training time if no text is found in the region labeled. With neural models, no synthetic text is injected and the recognized text is used as is.</br>
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムラベルの表の更新"
}
```

### Explanation
この変更は、カスタムラベルのセクションにおけるテーブルの一部を更新しています。具体的には、カスタムニューラルモデルに関する「Signature」の列の内容が修正され、サポート状況が「Unsupported」から「✔️Supported」に変更されました。これにより、カスタムニューラルモデルが全てのフィールドタイプをサポートすることが明確に示されています。この修正は、ドキュメントの正確性を向上させ、利用者がモデルの機能についてより正確な情報を得られるようにするためのものです。


