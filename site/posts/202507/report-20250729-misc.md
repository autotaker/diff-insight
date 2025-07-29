---
date: '2025-07-29'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c91b816...MicrosoftDocs:e0fd9e5
summary: この変更は、文書インテリジェンスサービスに関するドキュメントの誤植を修正するマイナーアップデートです。具体的には、"fist"を"first"に訂正することで、自動スケーリングの手順の理解が向上しました。新しい機能の追加はなく、破壊的な変更もありませんが、文書の正確性が向上しました。この変更はユーザーエクスペリエンスに大きな影響を与え、誤記が技術ドキュメントの信頼性を損なうことを防ぎます。小さな修正であっても、ユーザーがサービスをより正確に理解できるようになり、運用ミスが減少することが期待されます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c91b816...MicrosoftDocs:e0fd9e5){target="_blank"}


# ハイライト
この変更は、文書インテリジェンスサービス制限に関するドキュメントの誤植を修正するマイナーアップデートです。変更により、"fist"が"first"に訂正され、自動スケーリングの手順の理解が向上しました。

## 新機能
特に新機能追加はありませんが、ドキュメントの正確性が向上しました。

## 破壊的な変更
この更新には、破壊的な変更は含まれていません。

## その他の更新
文書内の誤記を1か所訂正しました。

# インサイト
このコード差分は、一目で些細な変更のように見えますが、実際にはユーザーエクスペリエンスに大きな影響を与える可能性があります。誤字脱字は、技術ドキュメントの信頼性を損ない、特に非英語圏のエンジニアには誤解を与えることがあります。例えば、"fist"と"first"は、つづりが似ているものの、全く異なる意味を持ちます。"fist"は「こぶし」を意味し、文脈にそぐわないため、修正が必要でした。このような小さな修正により、ユーザーはサービスをより正確に理解でき、自動スケーリングが適切に設定され、運用ミスを減らすことができます。この変更は小さく見えるかもしれませんが、技術文書の精度を保つための重要な一歩です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [service-limits.md](#item-5ceae5) | minor update | 文書インテリジェンスのサービス制限に関する誤植修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/service-limits.md{#item-5ceae5}

<details>
<summary>Diff</summary>
````diff
@@ -285,7 +285,7 @@ The next sections describe specific cases of adjusting quotas.
 
 By default the number of transactions per second is limited to 15 transactions per second for a Document Intelligence resource. For the Standard pricing tier, this amount can be increased. Before submitting the request, ensure you're familiar with the material in [this section](#detailed-description-quota-adjustment-and-best-practices) and aware of these [best practices](#example-of-a-workload-pattern-best-practice).
 
-The fist step would be to enable auto scaling. Follow this document to enable auto scaling on your resource * [enable auto scaling](../../ai-services/autoscale.md). With auto scaling enabled your resource can continue to accept requests over the TPS limits configured if there's capacity on the service. It can still result in request throttled. 
+The first step would be to enable auto scaling. Follow this document to enable auto scaling on your resource * [enable auto scaling](../../ai-services/autoscale.md). With auto scaling enabled your resource can continue to accept requests over the TPS limits configured if there's capacity on the service. It can still result in request throttled. 
 
 Increasing the Concurrent Request limit does **not** directly affect your costs. Document Intelligence service uses "Pay only for what you use" model. The limit defines how high the Service can scale before it starts throttle your requests.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書インテリジェンスのサービス制限に関する誤植修正"
}
```

### Explanation
この変更は、文書インテリジェンスのサービス制限に関するドキュメント内の誤植を修正するために行われました。具体的には、"fist"（最初）という誤った表記を"first"（最初）に修正しました。この修正は、ユーザーが自動スケーリングを有効にする手順を理解しやすくするためのものです。変更は1行が追加され、1行が削除され、合計2つの変更が記録されています。自動スケーリングの有効化に関するセクションの明確さが向上し、ユーザーがサービスの使用方法について誤解するリスクを減少させます。


