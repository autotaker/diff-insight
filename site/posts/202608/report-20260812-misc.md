---
date: '2026-08-12'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:90a93ce...MicrosoftDocs:4bb9e7f
summary: この変更は、ドキュメントインテリジェンスの移行ガイドに対するマイナーな更新です。具体的には、特定のREST APIバージョンのサポート終了日に関する新たな情報が追加され、日付が「2026年5月21日」から「2026年8月11日」に変更されました。この更新により、ユーザーはAPIのサポート終了に備えた計画的な移行が促進されます。特に重大な変更はありませんが、サポート終了に関する注意喚起が行われています。全体として、ユーザーがスムーズに移行できるよう支援する内容となっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:90a93ce...MicrosoftDocs:4bb9e7f){target="_blank"}

<format>
# ハイライト

この変更は、ドキュメントインテリジェンスの移行ガイドに対するマイナーな更新です。具体的には、日付の変更と、新たに追加された重要な情報が含まれます。この情報により、特定のREST APIバージョンのサポート終了日が明示され、移行の推奨がされています。

## 新機能

- 特定のREST APIバージョンのサポート終了日が追加されました。これにより、ユーザーはAPIのサポート終了に備え、適切な移行を計画することが可能となります。

## 重大な変更

- 特に重大な変更は存在しませんが、サポートが終了するAPIについての注意喚起が追加されているため、ユーザーはその情報に基づいてアクションを取る必要があります。

## その他の更新

- 日付の変更：「2026年5月21日」から「2026年8月11日」に更新されました。移行ガイドとしての正確性が向上しました。

# 洞察

今回の更新は、ユーザーがドキュメントインテリジェンスの提供するAPIのバージョンをスムーズに移行するための支援を目的としています。APIのサポート終了日は、システム運用における重要なマイルストーンであり、これをユーザーに周知することで、計画的な移行を促進しています。多くの企業はサーバーサイドでREST APIを利用しているため、サポート期間内に新しいバージョンに移行することは、ビジネスの継続性に関して重要な要素となります。

今回の日付の更新は、特にドキュメントやプロジェクトマネジメントにおいて、期限が迫るものとしての認識を持つ助けとなり、ユーザーが準備を始めやすくなるように設計されています。また、移行推奨の追加情報は、ユーザーに対する注意喚起の役割も果たし、技術的負債を未然に防ぐための有益なガイドとなります。このような変更は、サービス利用者のスムーズな体験を保障し、予期せぬ問題を回避する上で非常に有用です。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [migration-guide-overview.md](#item-49f49c) | minor update | 移行ガイドの更新 | modified | 2 | 1 | 3 | 


# Modified Contents
## articles/ai-services/document-intelligence/versioning/migration-guide-overview.md{#item-49f49c}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: mcleans
 ms.service: azure-document-intelligence-foundry-tools
 ms.topic: how-to
-ms.date: 05/21/2026
+ms.date: 08/11/2026
 ms.author: lajanuar
 monikerRange: '<=doc-intel-4.0.0'
 ai-usage: ai-assisted
@@ -18,6 +18,7 @@ ai-usage: ai-assisted
 
 > [!IMPORTANT]
 >
+> * **Document Intelligence REST preview API versions (2024-07-31-preview, 2024-02-29-preview, 2023-10-31-preview)** reach end of support on **June 30, 2026**.
 > * **Document Intelligence REST API v2.1** reaches end of support on **September 15, 2027**.
 > * **Document Intelligence REST API 2022-08-31 v3.0** reaches end of support on **March 30, 2029**. 
 > * To avoid production disruption, use this migration guide to move to **Azure Document Intelligence 2024-11-30 v4.0** before these dates.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "移行ガイドの更新"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスの移行ガイドに関連するマイナーアップデートです。具体的には、 1つの行の日付が「2026年5月21日」から「2026年8月11日」に変更されたことと、新たに重要な情報が追加されています。この重要な情報では、特定のREST APIバージョンのサポート終了日が明記されており、生産環境での問題を避けるための移行の推奨が行われています。この更新により、ユーザーはAPIのサポート終了日を把握し、適切に移行するためのガイダンスを受けることができます。


