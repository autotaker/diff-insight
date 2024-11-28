---
date: '2024-11-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:796b906...MicrosoftDocs:744c16a
summary: このコード変更は、用語の整合性を高めるために"AI Foundry"を"AI Foundry portal"に修正し、関連リンクを更新する小規模な修正です。新機能の追加はありませんが、特にカスタムスピーチ関連のリンクが更新され、情報へのアクセスが改善されます。破壊的な変更もなく、ユーザーが一貫した体験を得られるようになっています。この変更により、ドキュメントの情報が分かりやすくなり、ユーザーエクスペリエンスの向上につながるでしょう。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:796b906...MicrosoftDocs:744c16a){target="_blank"}

# Highlights
このコード変更には、"AI Foundry"という用語を"AI Foundry portal"に修正することによってリンクの整合性を高める小規模な修正が含まれています。また、toc.ymlファイルでは、カスタムスピーチに関連するリンクの更新が行われ、関連情報へのアクセスが改善されています。

## New features
- 特に新機能は追加されていませんが、情報の整合性を高めるためのリンクの更新が行われています。

## Breaking changes
- 特に破壊的な変更はありません。

## Other updates
- "AI Foundry"から"AI Foundry portal"への用語修正。
- `toc.yml`でのカスタムスピーチ関連リンクを新しいポータルへのリンクとして更新。

# Insights
このコード変更は、ユーザーがAI関連のドキュメントを参照する際に、より一貫した体験を提供するものです。"AI Foundry"から"AI Foundry portal"へ用語が統一されることにより、ポータルの役割や位置を明確にし、ユーザーの混乱を減らす狙いがあります。このように一貫性を持たせることにより、ユーザーが情報を検索しやすくなるだけでなく、文章内部での情報の齟齬を防ぐ効果も期待できます。

特に、`toc.yml`でのリンク修正は、カスタムスピーチ機能のユーザーにとって重要なもので、これにより最新情報へのアクセスが保証されます。ポータルやリソースへのリンクが正確であることは、ユーザーエクスペリエンスを向上させ、サポートへの問い合わせを減少させる効果もあるでしょう。このような細かい調整が、全体のユーザビリティに大きく貢献することになります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [studio-overview.md](#item-db8fa3) | minor update | AI Foundryポータルへのリンク修正 | modified | 3 | 3 | 6 | 
| [toc.yml](#item-2745cd) | minor update | カスタムスピーチ用AIファウンドリポータルへのリンク修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/studio-overview.md{#item-db8fa3}

<details>
<summary>Diff</summary>
````diff
@@ -27,7 +27,7 @@ The studio is an online tool to visually explore, understand, train, and integra
 * Train custom extraction models to extract fields from documents.
 * Get sample code for the language specific `SDKs` to integrate into your applications.
 
-Currently, we're undergoing the migration of features from the [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio) to the new [AI Foundry](https://ai.azure.com/explore/aiservices/vision). There are some differences in the offerings for the two studios, which determine the correct studio for your use case.
+Currently, we're undergoing the migration of features from the [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio) to the new [AI Foundry portal](https://ai.azure.com/explore/aiservices/vision). There are some differences in the offerings for the two studios, which determine the correct studio for your use case.
 
 ## Choosing the correct studio experience
 
@@ -37,7 +37,7 @@ There are currently two studios, the [Azure AI Foundry](https://ai.azure.com/exp
 
 Document Intelligence Studio is the legacy experience that contains all features released on or before July 2024. For any of the v2.1, v3.0, v3.1 features, continue to use the Document Intelligence Studio. Studios provide a visual experience for labeling, training, and validating custom models. For custom document field extraction models, use the Document Intelligence Studio for template and neural models. Custom classification models can only be trained and used on Document Intelligence Studio. Use Document Intelligence Studio if you want to try out GA versions of the models from version 2.1, v3.0 and v3.1.
 
-### When to use [AI Foundry](https://ai.azure.com/explore/aiservices/vision)
+### When to use [AI Foundry portal](https://ai.azure.com/explore/aiservices/vision)
 
 Start with the new Azure AI Foundry and try any of the prebuilt document models from `2024-02-29-preview` version including general extraction models like Read or Layout. If you want to build and test a new [Document Field Extraction](https://ai.azure.com/explore/aiservices/vision/document/extraction) model, try our generative AI model, only available in the new AI Foundry.
 
@@ -210,5 +210,5 @@ Learn how to [connect your AI services hub](../../ai-studio/ai-services/how-to/c
 ## Next steps
 
 * Visit [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
-* Visit [AI Foundry](https://ai.azure.com/explore/aiservices/vision).
+* Visit [AI Foundry portal](https://ai.azure.com/explore/aiservices/vision).
 * Get started with [Document Intelligence Studio quickstart](quickstarts/try-document-intelligence-studio.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryポータルへのリンク修正"
}
```

### Explanation
この修正は、文書の中で「AI Foundry」という用語の表現を「AI Foundry portal」に変更する内容です。具体的には、いくつかの箇所で「AI Foundry」と記載されていた部分が「AI Foundry portal」に修正され、ドキュメントの整合性が向上しました。この変更は、ユーザーに対して正確な情報を提供し、関連するリンクを明確にすることを目的としています。また、リンク先の表現が一貫性が増し、ユーザーが新しいポータルをより容易に認識できるようになります。修正が行われた行数は合わせて6行で、追加された行数と削除された行数はそれぞれ3です。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -84,7 +84,7 @@ items:
       - name: Hear and speak with chat in the playground
         href: quickstarts/hear-speak-playground.md
       - name: Fine-tune in AI Foundry portal for custom speech
-        href: ../ai-services/speech-service/custom-speech-ai-studio.md?context=/azure/ai-studio/context/context
+        href: ../ai-services/speech-service/custom-speech-ai-foundry-portal.md?context=/azure/ai-studio/context/context
   - name: Explore and select AI models
     items:
     - name: Model catalog
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムスピーチ用AIファウンドリポータルへのリンク修正"
}
```

### Explanation
この修正は、`toc.yml`ファイル内のカスタムスピーチに関連するリンクを更新する内容です。「AI Foundry portal」に関するリンクが、以前の「custom-speech-ai-studio.md」から「custom-speech-ai-foundry-portal.md」へと変更されました。この変更により、リンクは新しいポータルに正しく移動するようになり、ユーザーがカスタムスピーチ機能に関する最新の情報を得ることができるようになります。全体として、変更によりリンクの整合性が向上し、リソースへのアクセスが促進されます。変更行数は2行で、1行追加され、1行が削除されています。


