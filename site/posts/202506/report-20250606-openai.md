---
date: '2025-06-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c6cc5fa...MicrosoftDocs:e10a743
summary: このコードの変更は、Azure OpenAI サービスにおける「プロビジョニングスループットオンボーディング」セクションに対するマイナーな更新です。情報がテーブル形式に整理され、トピックの明確化と可読性の向上が図られました。新機能は追加されていませんが、既存の情報のレイアウトが改善されています。この変更は破壊的な影響を及ぼさず、ユーザーにとっては情報のアクセスのしやすさとナビゲーションが向上しました。全体として、ユーザーがスムーズに情報を得られるようにし、Azure
  OpenAI サービスの利用体験を向上させることが目的です。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c6cc5fa...MicrosoftDocs:e10a743){target="_blank"}

<format>
# Highlights
このコードの変更は、Azure OpenAI サービスに関する文書の「プロビジョニングスループットオンボーディング」セクションに行われたマイナーな更新です。具体的には、情報がテーブル形式で整頓され、トピックの明確化とデータの組織化が改善されました。

## New features
特に新機能が追加されたわけではありませんが、既存の情報のレイアウトと表示方法の改善が行われています。

## Breaking changes
この変更がシステムやサービスにおける既存の運用を壊すものではなく、ユーザーに対する破壊的な影響はありません。

## Other updates
- トピックの再編: データの最小値やスケールの増分に関する情報が整理されました。
- 可読性の向上: 入力 TPM とレイテンシ目標値に関する情報がより読みやすくなりました。
- ナビゲーションの改善: 情報が整理されることで、ユーザーの文書内でのナビゲーションも改善されています。

# Insights
Azure OpenAI サービスの「プロビジョニングスループットオンボーディング」セクションは、サービスを利用するユーザーにとって重要な情報を含んでいます。この更新では、特に情報の可読性とアクセスのしやすさを重視して変更が加えられています。

テーブル形式で情報を整理することで、読者は提供されるデータを簡単に確認し、必要な情報を迅速に取得することができるようになりました。これは、サービスの初期設定や拡張を行う際に、ユーザーの意思決定を支援するためのものです。

また、データの最小値やスケールの増分、入力 TPM（Transaction Per Minute）およびレイテンシ目標値の情報が明確に整理されたことにより、エンドポイントのスループットを効率的に管理し、期待されるパフォーマンス目標を簡単に設定することが可能になります。これにより、ユーザーはより効率的にリソースを利用し、目的に合ったスループットパラメータを選択するサポートを受けられます。

これらの変更は、ユーザーがドキュメントを通してスムーズに情報を得られるようにすることで、Azure OpenAI サービスの利用における全体的な体験を向上させることを目的としています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | プロビジョニングスループットのオンボーディングに関する記事の更新 | modified | 8 | 8 | 16 | 


# Modified Contents
## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -77,14 +77,14 @@ The amount of throughput (measured in tokens per minute or TPM) a deployment get
 
 For example, for `gpt-4.1:2025-04-14`, 1 output token counts as 4 input tokens towards your utilization limit which matches the [pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). Older models use a different ratio and for a deeper understanding on how different ratios of input and output tokens impact the throughput your workload needs, see the [Azure AI Foundry PTU quota calculator](https://ai.azure.com/resource/calculator).
 
-|Topic| **o4-mini** | **gpt-4.1** | **gpt-4.1-mini** | **gpt-4.1-nano** | **o3** | **o3-mini** | **o1** | **gpt-4o** | **gpt-4o-mini** |  **DeepSeek-R1** | **DeepSeek-V3-0324** | **MAI-DS-R1** |
-| --- |  --- | --- |  --- |  --- | --- | --- | --- | --- | --- | --- | --- | --- |
-|Global & data zone provisioned minimum deployment| 15 | 15|15| 15 | 15 |15|15|15|15| 100|100|100|
-|Global & data zone provisioned scale increment| 5 | 5|5| 5 | 5 |5|5|5|5|  100|100|100|
-|Regional provisioned minimum deployment|25| 50|25| 25 |50 | 25|25|50|25| NA|NA|NA|
-|Regional provisioned scale increment|25| 50|25| 25 | 50 | 25|50|50|25|NA|NA|NA|
-|Input TPM per PTU|5,400 | 3,000|14,900| 59,400 | 600 | 2,500|230|2,500|37,000|4,000|4,000|4,000|
-|Latency Target Value| 66 Tokens Per Second | 40 Tokens Per Second|50 Tokens Per Second| 60 Tokens Per Second | 40 Tokens Per Second | 66 Tokens Per Second |25 Tokens Per Second|25 Tokens Per Second|33 Tokens Per Second|50 Tokens Per Second|50 Tokens Per Second|50 Tokens Per Second|
+|Topic| **o4-mini** | **gpt-4.1** | **gpt-4.1-mini** | **gpt-4.1-nano** | **o3** | **o3-mini** | **o1** | **gpt-4o** | **gpt-4o-mini** |  **DeepSeek-R1** | **DeepSeek-V3-0324** |
+| --- |  --- | --- |  --- |  --- | --- | --- | --- | --- | --- | --- | --- |
+|Global & data zone provisioned minimum deployment| 15 | 15|15| 15 | 15 |15|15|15|15| 100|100|
+|Global & data zone provisioned scale increment| 5 | 5|5| 5 | 5 |5|5|5|5|  100|100|
+|Regional provisioned minimum deployment|25| 50|25| 25 |50 | 25|25|50|25| NA|NA|
+|Regional provisioned scale increment|25| 50|25| 25 | 50 | 25|50|50|25|NA|NA|
+|Input TPM per PTU|5,400 | 3,000|14,900| 59,400 | 600 | 2,500|230|2,500|37,000|4,000|4,000|
+|Latency Target Value| 66 Tokens Per Second | 40 Tokens Per Second|50 Tokens Per Second| 60 Tokens Per Second | 40 Tokens Per Second | 66 Tokens Per Second |25 Tokens Per Second|25 Tokens Per Second|33 Tokens Per Second|50 Tokens Per Second|50 Tokens Per Second|
 
 
 For a full list, see the [Azure AI Foundry calculator](https://ai.azure.com/resource/calculator).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングスループットのオンボーディングに関する記事の更新"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関する文書の一部を更新しています。具体的には、「プロビジョニングスループットオンボーディング」に関するセクションにおいて、テーブル形式でのデータの表示が修正され、情報の整頓が行われました。

主な変更点としては、トピック、グローバルおよび地域別の展開に関する最小値やスケールの増分、入力 TPM とレイテンシ目標値などが含まれています。また、改訂により、明確なカラム構造が強調され、情報の可読性が向上しています。8行の追加と削除を伴う変更が行われており、合計で16の変更が加えられました。これは、ユーザーにとっての理解を助けるための改善を意図したものであり、全体のナビゲーションと情報取得を容易にしています。


