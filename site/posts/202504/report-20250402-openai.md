---
date: '2025-04-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:11d129c...MicrosoftDocs:63f4fcb
summary: この変更は、Azure OpenAIのAPIドキュメント内にあるストアオプションの記述を修正するもので、具体的にはJSONフォーマットの`"store"`キーに関連する値を`"True"`から`"true"`に小文字に修正しました。特に新機能の追加や破壊的変更はなく、ドキュメントの一貫性と正確性を高めることを目的としています。この修正により、開発者がドキュメントを基にコードを書く際の混乱やエラーを未然に防ぎ、技術的な精度が向上します。正確なドキュメントは、効率的な開発の基盤となる重要な要素です。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:11d129c...MicrosoftDocs:63f4fcb){target="_blank"}

# ハイライト
この変更は、Azure OpenAIのAPIドキュメント内にあるストアオプションの記述を修正するものです。具体的には、JSONフォーマット内の`"store"`キーに関連する値の記述において、`"True"`から`"true"`に小文字へ修正されました。

## 新機能
特に新機能の追加はありません。

## 破壊的変更
破壊的な変更はありません。この修正はドキュメントフォーマットの一貫性と正確性を目的としたものです。

## その他のアップデート
ドキュメントのJSON表記において、プログラマーが誤解しないよう、正確なフォーマットにするための記述変更が行われています。

# インサイト
今回の変更は些細に見えるかもしれませんが、プログラムやドキュメントにおいて、JSON形式のキーと値の記述は非常に重要です。`"store": True`という誤った記述から、JSON標準に従った正しい記述である小文字の`"store": true`にすることで、開発者がドキュメントを基にコードを記述する際の混乱やエラーを未然に防ぐことができます。JSONでは、ブール値は小文字で表記されるため、この変更は技術的な精度とドキュメント全体の品質向上に寄与します。このような微調整は、特に多数の開発者が関与するプロジェクトにおいて重要な役割を果たします。正確なドキュメントは、効率的な開発を支える基盤となるのです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [stored-completions.md](#item-ccc7e6) | minor update | ストアオプションの修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/openai/how-to/stored-completions.md{#item-ccc7e6}

<details>
<summary>Diff</summary>
````diff
@@ -115,7 +115,7 @@ curl $AZURE_OPENAI_ENDPOINT/openai/deployments/gpt-4o/chat/completions?api-versi
   -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" \
   -d '{
     "model": "gpt-4o",
-    "store": True,
+    "store": true,
     "messages": [
       {
         "role": "system",
@@ -137,7 +137,7 @@ curl $AZURE_OPENAI_ENDPOINT/openai/deployments/gpt-4o/chat/completions?api-versi
   -H "api-key: $AZURE_OPENAI_API_KEY" \
   -d '{
     "model": "gpt-4o",
-    "store": True,
+    "store": true,
     "messages": [
       {
         "role": "system",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ストアオプションの修正"
}
```

### Explanation
この変更は、Azure OpenAIのAPIドキュメントにおけるストアオプションの表記を修正するためのものです。具体的には、`stored-completions.md`ファイルで、`"store": True`と記述されていた部分を`"store": true`に変更しました。この変更により、プログラム上の一貫性が向上し、正しいJSON形式に適合するようになりました。変更の規模は小さく、同じ内容に対して大小文字を修正したのみですが、ドキュメントの正確性を高める重要なステップとなります。


