---
date: '2025-10-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2b0d8aa...MicrosoftDocs:09a6487
summary: この記事の変更は、エンティティ認識（NER）に関するMarkdownファイルに対して施されたもので、新しい「言語サポート」セクションが追加され、NERが対応する言語についての情報が提供されています。見出しの表現が統一され、既存のコンテンツのフォーマットが改善されました。これにより、ドキュメントのユーザビリティと可読性が向上し、特に開発者にとってNERの機能や利用可能言語を理解する手助けとなっています。この小さな変更が、エンドユーザーにとって重要な改善であり、サービスの利用を促進する目的があります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2b0d8aa...MicrosoftDocs:09a6487){target="_blank"}

# ハイライト
この記事の変更は、エンティティ認識（NER）に関する情報を含むMarkdownファイルに対するもので、新しいセクションの追加と既存の内容の改善が施されています。特に、サポートされる言語に関する情報が新しく追加されました。

## 新機能
- 「## 言語サポート」セクションが追加され、NERが対応する言語について説明しています。

## 破壊的変更
- 破壊的な変更は特にありませんが、見出し等の表現が統一されました。

## その他の更新
- 既存の見出し「Supported API versions」が「## Supported API versions:」に変更されることで、フォーマットの一貫性が向上しています。

# 洞察
この変更は、エンティティ認識に関するドキュメントのユーザビリティと可読性を改善するためのものです。特に、新しく追加された「言語サポート」セクションは、NERがどの言語で利用可能かを明示しており、実際にサービスを利用したい開発者にとって非常に有用な情報を提供しています。

既存のコンテンツについても、見出しや表現が統一されることで、文書全体がよりプロフェッショナルで一貫した印象を与えるようになっています。これにより、読者はNERの機能とその適用可能性について、より迅速かつ正確に理解する助けとなります。 

技術文書におけるこうした更新は、一見すると小さな変更に感じられますが、エンドユーザーにとっては重要な改善であり、結果的にはそのサービスの利用を促進させる効果があります。NERに関連する技術やサービスを使用するための導入ハードルを下げ、多言語サポートの情報を明確にすることが、今回の更新の主たる目的と言えます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [named-entity-categories.md](#item-a4a7f1) | minor update | エンティティカテゴリに関する記事の更新 | modified | 3 | 2 | 5 | 


# Modified Contents
## articles/ai-services/language-service/named-entity-recognition/concepts/named-entity-categories.md{#item-a4a7f1}

<details>
<summary>Diff</summary>
````diff
@@ -19,12 +19,13 @@ Named Entity Recognition (NER) is a computational linguistic process within natu
 
 * **Entity Types** provide more detailed distinctions within the broader categories, allowing for more granularity and flexibility.
 
-This article provides a list of entity categories identified and returned by the Named Entity Recognition (NER) process.## Language Support
+This article provides a list of entity categories identified and returned by the Named Entity Recognition (NER) process.
 
+## Language Support
 
 The [NER language support](../language-support.md) page lists all languages available for the named entities in this article. Any exceptions are noted for specific named entities.
 
-Supported API versions:
+## Supported API versions:
 
 * [**Preview: 2025-05-15-preview**](/rest/api/language/text-analysis-runtime/analyze-text?view=rest-language-2025-05-15-preview&preserve-view=true&tabs=HTTP#entitycategory)
 * [**Stable: Generally Available (GA)**](/rest/api/language/text-analysis-runtime/analyze-text?view=rest-language-2024-11-01&preserve-view=truetabs=HTTP#entitycategory)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティカテゴリに関する記事の更新"
}
```

### Explanation
このコードの変更は、エンティティ認識（NER）プロセスに関する記事内のMarkdownファイルに対するマイナーな更新を示しています。具体的には、いくつかのセクションが追加され、既存のコンテンツの表現が若干変更されています。

変更内容の中には、既存の情報の整理と新しいセクション見出しの追加が含まれています。特に「## 言語サポート」セクションが新たに追加され、NERにおけるサポート対象言語に関する情報が強調されています。また、既存の見出し「Supported API versions」も「## Supported API versions:」と修正されており、より一貫したフォーマットになっています。

このような変更は、文書の可読性や情報の明確性を向上させるために重要です。このマイナーな更新によって、読者がエンティティ認識の機能とそのサポート言語についてより簡単に理解できるようになっています。


