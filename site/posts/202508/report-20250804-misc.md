---
date: '2025-08-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5952713...MicrosoftDocs:c84ae83
summary: この更新では、カスタムテキスト分類のREST APIに関するドキュメントで、リソースのアンカウントに関する情報が修正されました。主な変更点は、サンプルJSON内のリソースIDパスが正しい形式に更新されたことです。新機能や破壊的変更はなく、リソースIDのパスが修正され、ユーザーが正確に操作できるようになりました。この修正により、ドキュメントの信頼性とアクセシビリティが向上し、ユーザーがリソースをスムーズに操作できるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5952713...MicrosoftDocs:c84ae83){target="_blank"}

<format>
# ハイライト
この更新では、カスタムテキスト分類のREST APIのリソースに関するドキュメントで、リソースのアンカウントに関する情報が修正されました。主な変更点は、サンプルJSON内のリソースIDパスが正しい形式に更新されたことです。

## 新機能
- 特に新機能の追加はありません。

## 破壊的変更
- 破壊的な変更はありません。この更新はドキュメントの修正に留まっています。

## その他の更新
- リソースIDのパスが正しい形式に修正され、ユーザーが誤りなく操作できるようになりました。

# 洞察
この更新は、Azureポータルのリソースプロパティタブに表示されるリソースIDのフィールドをもとに、ドキュメント内のJSONサンプルコードを修正したものです。以前のドキュメントでは、`assignedResourceIds`フィールドに指定されていたリソースIDが不正であったため、ユーザーが正しいリソースをアンカウントする際に混乱を招く可能性がありました。

正しいリソースID形式の使用は、ユーザーがミスなくリソースを操作できる手助けとなり、結果としてドキュメントの信頼性とアクセシビリティを向上させます。特に、技術ドキュメントは正確さが求められるため、このような小さな修正でも非常に重要です。今後もこのような小さなドキュメントの修正が、効率的な開発と運用を支える基盤となるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [unassign-resources.md](#item-e7c3f6) | minor update | リソースのアンカウントに関する情報を修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/language-service/custom-text-classification/includes/rest-api/unassign-resources.md{#item-e7c3f6}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ Use the following sample JSON as your body.
 
 |Key  |Placeholder  |Value  | Example |
 |---------|---------|----------|--|
-| `assignedResourceIds` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to unassign. Found in the Azure portal under the _Properties_ tab for the resource as the _Resource ID_ field. | `/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
+| `assignedResourceIds` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to unassign. Found in the Azure portal under the _Properties_ tab for the resource as the _Resource ID_ field. | `/subscriptions/a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
 
 ### Get unassign resource status
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースのアンカウントに関する情報を修正"
}
```

### Explanation
このコードの差分では、特定のリソースをアンカウントするためのサンプルJSONの例が修正されました。具体的には、`assignedResourceIds`の値に含まれるリソースIDパスが変更されています。以前は不正な形式のリソースIDが指定されていたのに対し、修正後は正しい形式に更新されています。この変更は、Azureポータル内のリソースのプロパティタブにおけるリソースIDのフィールドに基づいており、ユーザーが正しいリソースIDを参照できるようにするためのものです。全体的に、この修正は文書の正確性を向上させ、利用者が手順をより理解しやすくすることを目的としています。


