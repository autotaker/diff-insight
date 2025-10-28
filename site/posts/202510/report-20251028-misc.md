---
date: '2025-10-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4ad1de1...MicrosoftDocs:631f16c
summary: この変更では、ドキュメントインテリジェンスに関するサービス制限文書が更新され、標準プライシング層における1秒当たりの取引数（TPS）の制限が詳細に説明されています。新たに、TPS制限が15であることに加え、増加要求が可能であることが追加されました。特に破壊的な変更はなく、ユーザーに対し、サービスをより柔軟に利用できる機会が提供されています。この更新は、ユーザーがサービスをより理解し、ビジネスニーズに応じた取引数の要求が可能であることを強調しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4ad1de1...MicrosoftDocs:631f16c){target="_blank"}

<format>
# ハイライト
この変更では、ドキュメントインテリジェンスに関するサービス制限文書が更新され、標準プライシング層における1秒当たりの取引数（TPS）の制限に関する情報が詳細に記載されています。

## 新しい機能
- 標準プライシング層におけるTPS制限が15であることに加え、増加要求ができる旨が追加。

## 破壊的変更
- 特に破壊的な変更はありません。

## その他の更新
- TPSの増加要求が可能であることや、それに関する追加の説明が更新され、ユーザーがより柔軟にサービスを利用できる機会を提供。

# 考察
この文書の更新は、ユーザーがサービスに対する理解を深めるための重要な役割を果たしています。特に、取引数の制限緩和要求を行うことが可能であるとの情報は、利用者のビジネスニーズをサポートする上で非常に意義深いです。これにより、ユーザーはより高いオペレーションニーズを持つ場合も、公式に認められたプロセスを通じてシステムの限界を超えるリクエストを行うことができるようになります。

また、この変更はユーザーに、日々の使用パターンやベストプラクティスの遵守がいかに重要であるかを再確認させます。これは、サービスを継続的に最適化し、安全で効果的な運用を維持するために非常に重要です。オペレーションの柔軟性をさらに高める一方で、システムの安全性とパフォーマンスを確保することを目的とした今回の文書更新は、サービスの長期的な信頼性の向上に寄与するでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [service-limits.md](#item-5ceae5) | minor update | サービス制限の文書の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/service-limits.md{#item-5ceae5}

<details>
<summary>Diff</summary>
````diff
@@ -283,7 +283,7 @@ The next sections describe specific cases of adjusting quotas.
 
 ### Increasing transactions per second request limit
 
-By default the number of transactions per second is limited to 15 transactions per second for a Document Intelligence resource. For the Standard pricing tier, this amount can be increased. Before submitting the request, ensure you're familiar with the material in [this section](#detailed-description-quota-adjustment-and-best-practices) and aware of these [best practices](#example-of-a-workload-pattern-best-practice).
+By default the number of transactions per second is limited to 15 transactions per second for a Document Intelligence resource. For the Standard pricing tier, TPS increase requests can be submitted, but whether they can be approved and at what TPS level adjustment will depend on the daily usage patterns and the best practices that are being followed. Before submitting the request, ensure you're familiar with the material in [this section](#detailed-description-quota-adjustment-and-best-practices) and aware of these [best practices](#example-of-a-workload-pattern-best-practice).
 
 The first step would be to enable auto scaling. Follow this document to enable auto scaling on your resource * [enable auto scaling](../../ai-services/autoscale.md). With auto scaling enabled your resource can continue to accept requests over the TPS limits configured if there's capacity on the service. It can still result in request throttled. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス制限の文書の更新"
}
```

### Explanation
この変更では、ドキュメントインテリジェンスリソースの取引制限に関するテキストの一部が更新されました。具体的には、標準プライシング層における1秒当たりの取引数（TPS）の増加要求についての説明が追加されました。変更前の内容では、TPSは15に制限されていることを述べていましたが、更新後の内容では、増加要求が提出可能であること、承認されるかどうかや調整が行われるTPSレベルは、日々の使用パターンや遵守されているベストプラクティスに依存することが明記されています。この更新は、利用者がサービスを適切に利用するための重要な情報を提供するものです。


