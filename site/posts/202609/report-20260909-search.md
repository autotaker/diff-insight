---
date: '2026-09-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5d64e7f...MicrosoftDocs:e6b3e61
summary: このコードの変更は、Azure検索インデックスのサジェスターに関するドキュメントの修正に焦点を当てています。新しい機能や破壊的変更はなく、異なる設定をサポートするためのフィールド使用についての説明が改善されました。この変更により、ユーザーはアナライザーの制約を考慮しながら、異なるインデックスフィールドに同じ内容をマッピングする方法をより明確に理解できるようになります。結果として、システムの効果的な利用が促進されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5d64e7f...MicrosoftDocs:e6b3e61){target="_blank"}

# ハイライト
このコードの変更は、Azure検索インデックスのサジェスターに関するドキュメントの修正に焦点を当てています。新しい機能や破壊的変更は特にありませんが、ユーザーが異なる設定をサポートするためフィールドをどのように使用するかについての説明が調整されました。このことにより、アナライザーの制約を考慮しながら、異なるインデックスフィールドに同じコンテンツをマッピングするための情報がクリアになり、ユーザーがシステムをより効果的に利用できるようになります。

## 新機能
新機能に関しては特に明示されていません。

## 破壊的変更
破壊的な変更は含まれていません。

## その他の更新
- ドキュメントの一部テキストを更新。
- 異なる設定をサポートするためのフィールド使用に関する説明の改善。

# 洞察
この変更によって、Azure検索インデックスにサジェスターを追加する際の設定方法に関する理解が改善されました。文書の修正は、ユーザーがアナライザーの制約を回避しつつ、効率的にインデックスフィールドを設定できるようになることを目的としています。

サジェスターは、多くの検索シナリオで重要な役割を果たし、ユーザーが検索エクスペリエンスを自然に促進できる機能です。そのため、正確な設定情報を持つことはシステムの効果的な利用につながります。特に異なるインデックスフィールドへの同一コンテンツのマッピング方法に関する強調は、柔軟な設定を可能にし、多様なニーズに応える手段を提供します。

このようなドキュメント更新は、技術者が新しい設定や機能を困難なく活用できるようにするために重要です。同時に、既存システムに新しい構成を統合する際の混乱を防ぐ役割も果たします。したがって、今回の修正は、システムの持続可能な運用とユーザーの利便性向上に寄与するものといえるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index-add-suggesters.md](#item-28ed57) | minor update | 検索インデックスのサジェスターの追加に関するドキュメントの修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/index-add-suggesters.md{#item-28ed57}

<details>
<summary>Diff</summary>
````diff
@@ -66,7 +66,7 @@ When evaluating analyzers, consider using the [Analyze Text API](/rest/api/searc
 Fields that use [custom analyzers](index-add-custom-analyzers.md) or [built-in analyzers](index-add-custom-analyzers.md#built-in-analyzers), (except for standard Lucene) are explicitly disallowed to prevent poor outcomes.
 
 > [!NOTE]
-> If you need to work around the analyzer constraint, for example if you need a keyword or ngram analyzer for certain query scenarios, you should use two separate fields for the same content. This allows one of the fields to have a suggester, while the other can be set up with a custom analyzer configuration. If you're using an indexer, you can map a source field to two different index fields to support multiple configuations.
+> If you need to work around the analyzer constraint, for example if you need a keyword or ngram analyzer for certain query scenarios, you should use two separate fields for the same content. This allows one of the fields to have a suggester, while the other can be set up with a custom analyzer configuration. If you're using an indexer, you can map a source field to two different index fields to support multiple configurations.
 
 ## Create using the Azure portal
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスのサジェスターの追加に関するドキュメントの修正"
}
```

### Explanation
この変更は、Azureの検索インデックスにおけるサジェスターの追加に関するドキュメントの修正です。具体的には、文中の一部のテキストが更新され、異なる設定をサポートするためのフィールドの使用についての説明が調整されました。この修正により、ユーザーがアナライザーの制約を回避するためにどのようにフィールドを設定するかについての情報が明確になります。特に、異なるインデックスフィールドに同じコンテンツをマッピングする方法が強調され、ユーザーがシステムをより効果的に活用できるようになります。


