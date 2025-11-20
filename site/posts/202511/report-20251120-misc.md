---
date: '2025-11-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:877b82c...MicrosoftDocs:05b2bb7
summary: この変更は、YAMLファイルに記載された環境変数のインデントを7スペースから8スペースに修正するマイナーアップデートです。新しい機能は追加されておらず、破壊的な変更もありません。インデントの修正により、YAMLの可読性と構文の整合性が向上し、開発者が設定ファイルをより理解しやすくなります。この修正は、特にコンテナの設定を行う際に、文書の整然さが重要であるため、ミスを防ぐ効果を期待されます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:877b82c...MicrosoftDocs:05b2bb7){target="_blank"}

# ハイライト
この変更は、YAMLファイルに記載された環境変数のインデントを修正するマイナーアップデートです。

## 新機能
特に新しい機能は追加されていません。

## 破壊的変更
破壊的変更はありません。この変更は既存の機能の可読性と構文の整合性を改善するものです。

## その他の更新
環境変数のインデントを従来の7スペースから8スペースに修正しました。

# 見識
この変更は地味に見えるかもしれませんが、YAMLファイルにおいてインデントは非常に重要です。YAMLはスペースによるインデントで階層を管理するため、間違ったインデントは構文エラーを引き起こす可能性があります。今回の修正は、`EULA=accept`という環境変数のインデントを1スペース追加することで、YAMLの一貫性と可読性を向上させました。開発者が設定ファイルをより理解しやすく、ミスを防ぎやすくなります。特に、ドキュメントを通してコンテナの設定を行う場合、見た目の整った正確な文書が重要です。この修正により、ユーザーは安心して文書を基に設定を進められるでしょう。_SETTINGSファイルの階層構造が視覚的に明瞭になるため、設定ミスによる不具合を未然に防ぐ効果が期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [install-run.md](#item-e32e11) | minor update | 環境変数のインデント修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/document-intelligence/containers/install-run.md{#item-e32e11}

<details>
<summary>Diff</summary>
````diff
@@ -283,7 +283,7 @@ services:
     container_name: azure-cognitive-service-read
     image: mcr.microsoft.com/azure-cognitive-services/form-recognizer/read-3.1
     environment:
-      - EULA=accept
+        - EULA=accept
         - billing={FORM_RECOGNIZER_ENDPOINT_URI}
         - apiKey={FORM_RECOGNIZER_KEY}
 ```
@@ -671,7 +671,7 @@ services:
     container_name: azure-cognitive-service-read
     image: mcr.microsoft.com/azure-cognitive-services/form-recognizer/read-3.1
     environment:
-      - EULA=accept
+        - EULA=accept
         - billing={FORM_RECOGNIZER_ENDPOINT_URI}
         - apiKey={FORM_RECOGNIZER_KEY}
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "環境変数のインデント修正"
}
```

### Explanation
この変更は、`install-run.md`ファイル内の環境変数のインデントを修正するためのものです。具体的には、`EULA=accept`という行のインデントが、従来の7スペースから8スペースに変更されました。この修正により、YAML構文の整合性が向上し、可読性が向上します。同様の修正が他の行にも適用されています。この変更は、ドキュメントの整合性を保ち、開発者がコンテナを適切に設定できるようにするためのものです。また、問題のある行が視覚的に明確になり、設定ミスを防ぐ手助けとなります。


