---
date: '2025-11-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c655d26...MicrosoftDocs:57ab145
summary: AIサービスセクションの`toc.yml`ファイル内のリンクが正しく更新されました。これにより、情報の正確さが向上し、ユーザーが関連資料にアクセスしやすくなります。新しい機能は追加されていませんが、リンク修正によって操作性が改善されます。今回の修正は破壊的変更を伴わず、既存のユーザー体験を向上させる軽微な変更です。また、リンク構造が統一され、正しいパスが提供されるようになりました。これにより、ユーザーは必要な情報に簡単にアクセスできるようになります。細かな改善がユーザー体験の向上に寄与しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c655d26...MicrosoftDocs:57ab145){target="_blank"}

# ハイライト
「AIサービス」セクションの`toc.yml`ファイル内のリンクが正しく更新されました。これは情報の正確さを高め、ユーザーが関連資料にアクセスしやすくすることを目的としています。

## 新機能
特に新しい機能の追加はありませんが、リンク修正は全体の操作性を向上させます。

## 破壊的変更
今回の修正によって破壊的な変更はありません。既存のユーザー体験を改善するための軽微な変更です。

## その他の更新
リンク構造の一貫性を高め、正しいパスをユーザーに提供するように更新されました。

# 詳細
今回のコード変更は、AzureのAIサービスに関連した文書内のリンクを修正することによって、ユーザーが必要とする情報により簡単にアクセスできるようにすることが目的です。

具体的には、以下のことが行われました：

1. **リンクの修正**：不正確だったリンクが新しい正しいパスに更新されました。それにより、ユーザーは正しいリソースに迷うことなくアクセスできるようになりました。

2. **一貫性の向上**：セクションごとのリンク先パスが統一され、すべて「/azure/ai-foundry/responsible-ai」の形式を基にしています。これにより、ドキュメント内での参照が整理されました。

このような変更は一見小さなものですが、ドキュメントの質を高め、ユーザーの利便性を向上させる重要な役割を果たしています。ユーザーが資料に効率的にアクセスできるようになることで、AIサービスを活用する際の障壁が低くなり、サービス全体の価値向上にもつながります。このように、細かな改善を積み重ねることがユーザー体験の向上に直結します。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [toc.yml](#item-12f1f0) | minor update | 「AIサービス」セクションのリンク修正 | modified | 4 | 4 | 8 | 


# Modified Contents
## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -45,13 +45,13 @@ items:
     - name: Responsible use of AI
       items:
       - name: Transparency note for CLU
-        href: /legal/cognitive-services/language-service/clu-transparency-note?context=/azure/ai-services/language-service/context/context
+        href: /azure/ai-foundry/responsible-ai/clu/clu-transparency-note?context=/azure/ai-services/language-service/context/context
       - name: Integration and responsible use
-        href: /legal/cognitive-services/language-service/guidance-integration-responsible-use?context=/azure/ai-services/language-service/context/context
+        href: /azure/ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use?context=/azure/ai-services/language-service/context/context
       - name: Characteristics and limitations
-        href: /legal/cognitive-services/language-service/clu-characteristics-and-limitations?context=/azure/ai-services/language-service/context/context
+        href: /azure/ai-foundry/responsible-ai/clu/clu-characteristics-and-limitations?context=/azure/ai-services/language-service/context/context
       - name: Data, privacy, and security
-        href: /legal/cognitive-services/language-service/data-privacy?context=/azure/ai-services/language-service/context/context
+        href: /azure/ai-foundry/responsible-ai/clu/clu-data-privacy-security?context=/azure/ai-services/language-service/context/context
     - name: How-to guides
       items:
         - name: Use containers
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "「AIサービス」セクションのリンク修正"
}
```

### Explanation
今回の変更では、AIサービスに関する「toc.yml」ファイル内のいくつかのリンクが修正されました。具体的には、従来のリンクが新しい正しいパスに更新され、各項目のセクションが一貫性を保つ形へと変更されました。新しいリンクは「/azure/ai-foundry/responsible-ai」を基にしたものであり、これによりユーザーが関連するリソースにアクセスしやすくなっています。合計で4行の追加と削除があり、全体の変更数は8行です。このようなマイナーな更新は、情報の正確性とユーザー体験の向上に寄与します。


