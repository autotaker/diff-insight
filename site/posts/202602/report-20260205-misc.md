---
date: '2026-02-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:800bcb1...MicrosoftDocs:f5997cf
summary: クエリフィールドに関する情報が軽微に更新され、特定のプレビルトモデルの名称が変更されました。新しい機能の追加や重大な変更はありません。主な更新内容は「UX.Taxのプレビルトモデル」が「契約のプレビルトモデル」に変更されたことです。この修正はユーザーへの情報提供の正確性を向上させるためのものであり、契約文書の処理に対してより明確なガイダンスを提供します。ユーザーは適切な機能をより理解しやすくなり、サービスの品質向上が図られています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:800bcb1...MicrosoftDocs:f5997cf){target="_blank"}

# Highlights
クエリフィールドに関する情報が軽微に更新されました。特に、特定のプレビルトモデルの名称が変更されています。

## New features
特に新しい機能の追加はありません。

## Breaking changes
既存の機能に重大な変更はありません。

## Other updates
「UX.Taxのプレビルトモデル」が「契約のプレビルトモデル」に変更された点が主な更新内容です。

# Insights
今回の更新は、ユーザーへの情報提供の正確性を向上させるための軽微な修正に過ぎません。ドキュメントインテリジェンス機能では、プレビルトモデルとして提供される機能が、その目的ごとに異なる場合があります。たとえば、特定の業務用途に合わせたモデルが用意されていることが一般的で、ユーザーがこれらを選択する際の利便性が求められます。

本修正では、ユーザーがどのプレビルトモデルが適切かを識別する手助けをするために、文中の一部用語を明瞭かつ正確に訂正しています。特にビジネスドメインにおいて求められる契約文書の処理にあたり、「契約のプレビルトモデル」という表現が、より直接的で明解なガイダンスを提供します。この変更により、ユーザーはツールの利用可能な範囲を正しく理解しやすくなり、適切な機能を選択しやすくなると期待されます。

基本的には内容の本質に影響を与えることはなく、情報の精度を上げるための調整といえますので、ユーザーに対する直接的な影響も少ないと考えられます。このように改訂作業を通して、サービス全体としての品質向上が図られています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [query-fields.md](#item-c58523) | minor update | クエリフィールドに関する情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/concept/query-fields.md{#item-c58523}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ monikerRange: 'doc-intel-4.0.0'
 Document Intelligence now supports query field to extend the schema of any prebuilt model to extract the specific fields you need. Query fields can also be added to layout to extract fields in addition to structure from forms or documents.
 > [!NOTE]
 >
-> Document Intelligence Studio query field extraction is currently available with layout and prebuilt models, excluding the UX.Tax prebuilt models.
+> Document Intelligence Studio query field extraction is currently available with layout and prebuilt models, excluding the Contract prebuilt model.
 
 ## Query fields or key value pairs
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリフィールドに関する情報の更新"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスにおけるクエリフィールドの説明を微修正したものです。特に、文中の「UX.Taxのプレビルトモデル」を「契約のプレビルトモデル」に変更しています。これは、ユーザーに対してプレビルトモデルの除外についての正確な情報を提供するための修正です。この更新により、ユーザーが利用できる機能の範囲が明確になります。その他の部分は変更されていないため、内容は基本的に維持されています。


