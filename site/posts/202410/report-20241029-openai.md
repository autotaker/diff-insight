---
date: '2024-10-29'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ceba2b5...MicrosoftDocs:d84fb33
summary: この変更は、`use-your-data-rest.md`ファイル内でのデータソースタイプ名が`"AzureCognitiveSearch"`から`"azure_search"`に変更されたことを示しています。変更の主な目的はAPIの整合性と一貫性を保ち、コードの可読性を向上させることです。特に影響があるのは、旧名称を使用している場合で、これを新名称に更新しなければなりません。この変更はAPI利用者にとって、データソースの指示をより正確に行えるようにするためのもので、将来的なメンテナンスの容易さにも寄与します。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ceba2b5...MicrosoftDocs:d84fb33){target="_blank"}

# ハイライト
この変更は、`use-your-data-rest.md`ファイル内で使用されるデータソースタイプの名称が、`"AzureCognitiveSearch"`から`"azure_search"`に変更されたことを示しています。この更新は、APIの整合性や一貫性を保つことを主な目的としており、特にAPIを利用する際のコードの可読性向上に寄与する小規模なアップデートです。

## 新しい機能
特筆すべき新機能はこの変更には含まれていません。

## 破壊的変更
- データソースタイプ名の変更により、旧名称`"AzureCognitiveSearch"`を使用している場合は、新名称`"azure_search"`に更新する必要があります。これにより、旧バージョンのコードが正常に動作しなくなる可能性があります。

## その他の更新
- API利用者が正確にデータソースを指定できるよう、Curlリクエストのデータソースタイプ名が更新されました。

# 洞察
今回の変更は、主にAPIの名称一貫性と可読性を向上させることを目的としています。特に、APIの利用者が複数の異なるデータソースタイプを扱う際に、統一された名称を使用することでコードの読みやすさや保守性が向上します。この変更は、国際的なAPI標準や業界のベストプラクティスに沿ったものであると考えられます。そのため、既存のAPI利用者は、変更がもたらす影響を最小限に抑えるためにドキュメントや既存コードの更新を行う必要があるでしょう。これにより、将来的なメンテナンスが容易になり、APIの持続的な改善が見込めます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [use-your-data-rest.md](#item-d1e071) | minor update | データソースタイプの名称変更 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/includes/use-your-data-rest.md{#item-d1e071}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ curl -i -X POST $AZURE_OPENAI_ENDPOINT/openai/deployments/$AZURE_OPENAI_DEPLOYME
 {
     "data_sources": [
         {
-            "type": "AzureCognitiveSearch",
+            "type": "azure_search",
             "parameters": {
                 "endpoint": "'$AZURE_AI_SEARCH_ENDPOINT'",
                 "key": "'$AZURE_AI_SEARCH_API_KEY'",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データソースタイプの名称変更"
}
```

### Explanation
この変更では、`use-your-data-rest.md`ファイル内のデータソースのタイプ名が`"AzureCognitiveSearch"`から`"azure_search"`に変更されました。この修正は、APIの整合性や一貫性を保つために行われたもので、特にコードの可読性を向上させるためのマイナーアップデートに分類されます。変更の内容は、Curlリクエストの一部に関連しており、API利用者がデータソースを正しく指定できるようにしています。


