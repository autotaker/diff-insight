---
date: '2025-07-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:db33d34...MicrosoftDocs:d29c020
summary: このアップデートでは、言語サービスのYAMLファイルに「Announced for Deprecation」という新しいセクションが追加され、ユーザーが非推奨のサービス情報にアクセスしやすくなっています。このセクションには「Language
  Understanding」と「QnA Maker」へリンクが含まれており、これらのサービスに関する最新の非推奨情報を提供します。重大な破壊的変更はありませんが、ユーザーエクスペリエンスが向上し、特にエンタープライズ環境でこれらのサービスを使用している開発者にとって重要な情報が提供されることで、プロジェクトの戦略を見直す助けとなります。この変更は、小さなアップデートに見えるかもしれませんが、開発者の意思決定をサポートする重要な要素となります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:db33d34...MicrosoftDocs:d29c020){target="_blank"}

# Highlights
このアップデートでは、言語サービスのYAMLファイルに非推奨項目を新たに追加しています。追加されたセクション「Announced for Deprecation」には「Language Understanding」と「QnA Maker」へのリンクが含まれており、これらサービスの最新の非推奨情報を提供しています。

## New features
- 「Announced for Deprecation」セクションが追加され、ユーザーが非推奨のサービス情報にアクセスしやすくなりました。

## Breaking changes
- 特筆すべき大きな機能の破壊的変更は含まれていません。

## Other updates
- 非推奨情報のリンクを通じ、ユーザー体験が向上しました。

# Insights
この変更は、そのままでは小さなアップデートに見えるかもしれませんが、ユーザーエクスペリエンスに大きな影響を与える可能性があります。特に、エンタープライズ環境でこれらのサービスに依存している開発者にとって、非推奨になる機能やサービスの情報は非常に重要です。新しいセクション「Announced for Deprecation」の追加により、開発者は非推奨情報に迅速にアクセスし、それに基づいて適切な対応を行うことができます。

また、「Language Understanding」や「QnA Maker」が非推奨になるという情報は、これらのサービスを使用しているプロジェクトに対して今後の戦略を再考させるトリガーとなり得ます。このアップデートにより、開発者やサービス利用者が非推奨に関する先見性を持ちやすくなり、結果としてプロジェクトの長期的な計画が立てやすくなる点が評価できます。

技術的には、YAMLファイルに新たなセクションとリンクを数行追加するだけですが、その影響はサービスのライフサイクル管理や機能更新計画にまで広がります。このように、情報提供の改善が開発者の意思決定プロセスを支える重要な要素となります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index.yml](#item-c9444f) | minor update | 言語サービスに非推奨項目を追加 | modified | 6 | 0 | 6 | 


# Modified Contents
## articles/ai-services/language-service/index.yml{#item-c9444f}

<details>
<summary>Diff</summary>
````diff
@@ -106,3 +106,9 @@ additionalContent:
         links:
         - text: Support and help
           url: ../cognitive-services-support-options.md?context=/azure/ai-services/speech-service/context/context
+      - title: Announced for Deprecation
+        links:
+        - text: Language Understanding
+          url: ../luis/index.yml
+        - text: QnA Maker
+          url: ../qnamaker/index.yml
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サービスに非推奨項目を追加"
}
```

### Explanation
この変更では、言語サービスに関するYAMLファイルが更新され、非推奨項目に関する情報が追加されました。具体的には、「Announced for Deprecation」というセクションが追加され、その中に「Language Understanding」と「QnA Maker」のリンクが設けられています。これにより、ユーザーは非推奨とされるサービスについての最新情報にアクセスしやすくなります。変更の総数は6件であり、元のファイルの106行目から新しい情報が挿入されていることが確認できます。


