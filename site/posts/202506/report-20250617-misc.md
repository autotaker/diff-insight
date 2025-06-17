---
date: '2025-06-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b7d8d3a...MicrosoftDocs:ba67d73
summary: この変更の主なハイライトは、個人識別情報 (PII) ドキュメントの正規表現に関する情報へのリンクの形式を、直接のURLから相対パスに変更したことです。この変更により、ドキュメントの可読性とリンク管理の一貫性が向上しました。また、相対パスの使用により、異なる環境への移行時にリンクが壊れるリスクが軽減され、ユーザーが必要な情報に迅速にアクセスできるようになります。今回の更新はシンプルながら、ドキュメントの可用性と管理性の向上に寄与しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b7d8d3a...MicrosoftDocs:ba67d73){target="_blank"}

# ハイライト
この変更の主なハイライトは、個人識別情報 (PII) ドキュメントの正規表現に関する情報へのリンクの形式が変更された点です。直接のURLから相対パスに変更され、ドキュメントの可読性とリンク管理の一貫性が向上しました。

## 新機能
該当なし

## 重大な変更
該当なし

## その他の更新
- リンクの形式が直接のURLから相対パスに変更。
- 文書内の行数の調整による更新（1行削除、1行追加）。

# インサイト
この変更は、ドキュメント管理の観点から非常に実用的です。相対パスへの変更は、ドキュメントが異なる環境に移行した場合でもリンクが壊れるリスクを軽減します。たとえば、ドキュメントが別のドメインや新しいディレクトリ構造に移動した場合でも、相対パスによるリンクは引き続き機能します。これは、ドキュメントのメンテナンスを容易にし、将来のプラットフォーム変更に柔軟に対応できるようにする重要なステップです。また、ユーザーエクスペリエンスの向上にもつながります。リンクが常に正しい場所を参照することで、ユーザーは必要な情報に迅速にアクセスできます。

今回の更新はシンプルですが、ドキュメントの可用性と管理性の向上に貢献しています。これにより、ユーザーはPIIドキュメントの正規表現についての必要な情報にアクセスしやすくなるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [adapt-to-domain-pii.md](#item-62092f) | minor update | 情報へのリンクの更新: PII ドキュメントの正規表現に関する情報を改善 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/language-service/personally-identifiable-information/how-to/adapt-to-domain-pii.md{#item-62092f}

<details>
<summary>Diff</summary>
````diff
@@ -221,4 +221,4 @@ Logging:Console:LogLevel:Default=Debug
 - Rule names must begin with "CE_"  
 - Rule names must be unique. 
 - Rule names may only use alphanumeric characters and underscores ("_")
-- Regex patterns follow the .NET regular Expressions format. See [our documentation on .NET regular expressions](https://learn.microsoft.com/dotnet/standard/base-types/regular-expressions) for more information. 
\ No newline at end of file
+- Regex patterns follow the .NET regular Expressions format. See [our documentation on .NET regular expressions](/dotnet/standard/base-types/regular-expressions) for more information. 
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "情報へのリンクの更新: PII ドキュメントの正規表現に関する情報を改善"
}
```

### Explanation
今回の変更は、ドキュメント内の正規表現に関する外部リンクの内容を更新しました。具体的には、リンクの形式が変更され、直接の URL から相対パスに変更されました。これにより、より一貫性のあるリンクの管理が可能になり、ドキュメントの可読性が向上します。また、この変更に伴い、ドキュメント内の行数が1行削除され、1行が追加されたことを反映しています。この修正は、ユーザーがドキュメントの正規表現に関する情報をより容易に見つけられるようにするための改善です。


