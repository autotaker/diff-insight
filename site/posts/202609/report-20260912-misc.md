---
date: '2026-09-12'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:54bcca9...MicrosoftDocs:dd4af48
summary: このコード変更の主なポイントは、REST APIコマンドをシンプルで明確にするためのマイナーアップデートです。具体的には、`analyze?_overload=analyzeDocument`のパラメータが削除され、APIエンドポイントの構造が見直されました。この結果、開発者のAPI利用時の可読性と使いやすさが向上しました。また、APIバージョンは2024-11-30に設定され、最新の機能との互換性が確保されています。特に重大な破壊的変更はありませんが、廃止されたパラメータによってリクエスト形式に変更が必要になる場合があります。これらの改善により、開発者はより効率的にシステム間のインテグレーションやドキュメント処理を行うことができ、迅速な開発サイクルが実現します。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:54bcca9...MicrosoftDocs:dd4af48){target="_blank"}

# Highlights
このコード変更の主なポイントは、REST APIコマンドをよりシンプルかつ明確にするためのマイナーアップデートです。具体的には、`analyze?_overload=analyzeDocument`のパラメータが削除され、APIエンドポイントの構造が見直されました。これにより、開発者がAPIを利用する際の可読性と使いやすさが向上しました。APIバージョンは2024-11-30に設定され、最新の機能との互換性が確保されています。

## New features
- REST APIコマンドが簡素化され、エンドポイントに直接アクセスしやすくなりました。

## Breaking changes
- 特に重大な破壊的変更はありませんが、`analyze?_overload=analyzeDocument`パラメータは廃止されています。これにより、APIのリクエスト形式の変更が必要になる可能性があります。

## Other updates
- APIバージョンは2024-11-30に設定され、最新の仕様に合わせて更新されています。

# Insights
この変更は、REST APIの使いやすさと開発者の生産性向上を目指したものです。かつてのAPI呼び出しに含まれていた余計なクエリパラメータの削除により、エンドポイントに対するリクエストがより直感的かつ明確になります。この結果、開発者はシステム間のインテグレーションやドキュメント処理をより効率よく行うことができ、組み込みのプロセスが簡素化されます。

また、APIのバージョンが新しくなったことで、最新の機能やセキュリティ修正を取り入れた利用が可能です。こうした改善は、特に迅速な開発サイクルと持続可能なソリューションを追求する組織にとって価値があると言えるでしょう。APIの更新により、今後も一貫して最新の技術スタックを採用することが可能となります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [rest-api.md](#item-222da8) | minor update | REST API コマンドの修正 | modified | 1 | 1 | 2 | 
| [read.md](#item-06f32f) | minor update | REST API コマンドの簡略化 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/how-to-guides/includes/v4-0/rest-api.md{#item-222da8}

<details>
<summary>Diff</summary>
````diff
@@ -63,7 +63,7 @@ Use the following table as a reference. Replace *\<modelId>* and *\<document-url
 Open a bash window and run the following cURL command. The commands include the endpoint and key environment variables previously created in the set environment variables section. Replace those variables if your variable names differ. Remember to replace the *\<modelId>* and *\<document-url>* parameters.
 
 ```bash
-curl -i -X POST "POST {endpoint}/documentintelligence/documentModels/{modelId}:analyze?_overload=analyzeDocument&api-version=2024-11-30" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: {DI_KEY}" --data-ascii "{'urlSource': '<document-url>'}"
+curl -i -X POST "{endpoint}/documentintelligence/documentModels/{modelId}:analyze?api-version=2024-11-30" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: {DI_KEY}" --data-ascii "{'urlSource': '<document-url>'}"
 ```
 
 To enable add-on capabilities, use the `features` query parameter in the POST request. There are four add-on capabilities available with the `2023-07-31` (GA) and later releases: *ocr.highResolution*, *ocr.formula*, *ocr.font*, and *queryFields.premium*. To learn more about each of the capabilities, see [Custom models](../../../concept/accuracy-confidence.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST API コマンドの修正"
}
```

### Explanation
この変更は、特定のREST APIコマンドの形式を修正するために行われました。具体的には、cURLコマンドのエンドポイントURLの形式が更新され、`analyze?_overload=analyzeDocument`のパラメータが削除されました。新しいコマンドは、前回のバージョンと比較してよりシンプルな形になっており、開発者が利用する際の明瞭さが向上しています。また、APIバージョンは2024-11-30に設定されています。この変更により、ユーザーはドキュメント分析を行う際の手順がより簡素化され、使いやすくなっています。

## articles/ai-services/document-intelligence/prebuilt/read.md{#item-06f32f}

<details>
<summary>Diff</summary>
````diff
@@ -104,7 +104,7 @@ To use searchable PDF, make a `POST` request using the `Analyze` operation and s
 
 ```bash
 
-     POST {endpoint}/documentintelligence/documentModels/prebuilt-read:analyze?_overload=analyzeDocument&api-version=2024-11-30&output=pdf
+     POST {endpoint}/documentintelligence/documentModels/prebuilt-read:analyze?api-version=2024-11-30&output=pdf
      {...}
      202
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST API コマンドの簡略化"
}
```

### Explanation
この変更は、REST APIコマンドの一部を簡略化することを目的としています。具体的には、`analyze?_overload=analyzeDocument`というクエリパラメータが削除され、よりシンプルな形になりました。この修正により、新しいAPIコマンドは、サポートされるエンドポイントに直接アクセスする際の可読性と使いやすさが向上します。APIのバージョンは2024-11-30に設定されており、ユーザーはこの簡略化されたリクエストを使用して、検索可能なPDFを生成することができます。


