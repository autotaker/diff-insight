---
date: '2026-08-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:19bbfea...MicrosoftDocs:2cb7c3b
summary: このコード差分では、`articles/ai-services/document-intelligence/toc.yml` ファイルがマイナーに更新され、ユーザーの利便性が向上しています。目次に「地域サポート」と「コンプライアンスと認証」の項目が新たに追加され、ユーザーが必要な情報をより簡単に見つけやすくなりました。特に破壊的な変更はないものの、目次の構造がわずかに変更されています。全体で12箇所の変更があり、5行が追加され、7行が削除されています。この更新により、ドキュメントの情報へのアクセス性が向上し、特にビジネスユーザーにとって重要な情報がより直感的に利用できるようになりました。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:19bbfea...MicrosoftDocs:2cb7c3b){target="_blank"}

# Highlights
このコード差分では、`articles/ai-services/document-intelligence/toc.yml` ファイルのマイナーな更新が行われ、ユーザーの利便性が向上しています。新しい特徴として、「地域サポート」と「コンプライアンスと認証」に関する項目が追加されています。

## New features
- 「地域サポート」と「コンプライアンスと認証」の項目が目次に追加されました。

## Breaking changes
- 特に破壊的な変更はありませんが、目次の整理により構造がわずかに変更されています。

## Other updates
- 5行が新たに追加され、7行が削除されました。
- コード全体で12箇所の変更が行われています。

# Insights
この更新は、`toc.yml` ファイル、つまり目次ファイルの内容を改良することで、ユーザーがドキュメント内で必要な情報を迅速に取得できるようにすることを目的としています。具体的には、目次に「地域サポート」や「コンプライアンスと認証」の項目が新設され、ユーザーはこれまで以上に容易に該当の情報を探し出せるようになりました。

これにより、ドキュメントが提供する情報のアクセス性が向上し、ユーザーエクスペリエンスがより直感的になることが期待されます。特に「コンプライアンスと認証」というデータは、信頼性の高いサービスを求めるビジネスユーザーにとって非常に重要であり、こうした情報が目次から即座にアクセスできることは、資料としての価値をさらに高めます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [toc.yml](#item-81aa7b) | minor update | 目次ファイルの更新 | modified | 5 | 7 | 12 | 


# Modified Contents
## articles/ai-services/document-intelligence/toc.yml{#item-81aa7b}

<details>
<summary>Diff</summary>
````diff
@@ -29,6 +29,8 @@ items:
       - name: Custom models
         displayName: locale, handwritten, handwriting, text, detect, detection, printed
         href: language-support/custom.md
+  - name: Region support
+    href: https://go.microsoft.com/fwlink/?linkid=2087185      
   - name: Pricing
     displayName: cost, free, F0, tiers, standard, S0
     href: https://azure.microsoft.com/pricing/details/form-recognizer/
@@ -366,17 +368,13 @@ items:
 
 - name: Resources
   items:
-  - name: Enterprise readiness
-    items:
-    - name: Region support
-      href: https://go.microsoft.com/fwlink/?linkid=2087185
-    - name: Compliance and certification
-      href: https://azure.microsoft.com/support/legal/cognitive-services-compliance-and-privacy/
   - name: Known issues and troubleshooting
     href: reference/known-issues.md
+  - name: Compliance and certification
+    href: https://azure.microsoft.com/support/legal/cognitive-services-compliance-and-privacy/
   - name: Support and help options
     href: ../../ai-services/cognitive-services-support-options.md?context=/azure/ai-services/document-intelligence/context/context
   - name: Privacy and cookies
     href: https://privacy.microsoft.com/en-US/privacystatement
   - name: Document Intelligence release history
-    href: reference/release-history.md
\ No newline at end of file
+    href: reference/release-history.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次ファイルの更新"
}
```

### Explanation
この変更は、`articles/ai-services/document-intelligence/toc.yml` ファイルに対する小規模な更新です。主に、以下の2つの新しい項目が追加されました：1つは「地域サポート」で、もう1つは「コンプライアンスと認証」です。これにより、ユーザーは新たに提供されるリソースや情報へのアクセスが容易になります。

具体的な変更内容としては、5行が追加され、7行が削除されています。また、コード全体において12の変更が行われています。これにより、目次がより整理され、関連情報へのリンクが強化されています。

全体として、これらの変更はドキュメンテーションの利便性を向上させ、ユーザーが求める情報を迅速に見つける手助けをすることを目的としています。


