---
date: '2024-09-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5e7dab7...MicrosoftDocs:552467e
summary: この更新では、主にREST APIの暗号化設定に関する変更が行われました。具体的には、"enforcement"の値が"Disabled"から"Enabled"に変更され、暗号化の遵守状態に関する項目が削除されました。これらの変更は、暗号化設定の有効化と文書の明確さ向上を目的としています。また、暗号化設定はデフォルトで有効化されるようになり、システムや設定の再評価が必要な互換性の破壊的変更も含まれています。全体的に、セキュリティの強化を図りつつ、ユーザーが簡潔に暗号化状態を把握できる環境を提供することが意図されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5e7dab7...MicrosoftDocs:552467e){target="_blank"}

# ハイライト
この更新では、主にREST APIの暗号化設定に関する変更が行われました。
- "enforcement"の値は"Disabled"から"Enabled"に変更されました。
- 暗号化の遵守状態に関する項目が削除されました。

これらの変更は、暗号化設定の有効化と文書の明確さ向上を目的としています。

## 新機能
- 暗号化設定がデフォルトで有効化されるようになりました。

## 互換性の破壊的変更
- 暗号化の遵守状態に関する項目が削除されたため、これに依存していたシステムや設定は再評価が必要です。

## その他の更新
- ドキュメントの修正と明確化。

# 洞察
今回の変更は、REST APIおよび暗号化キー管理に関する設定を明確にし、暗号化がデフォルトで有効となるように改訂されたものです。

まず、`search-manage-rest.md`の変更について注目すると、"enforcement"の値が"Disabled"から"Enabled"に変更されました。これにより、デフォルトで暗号化が有効化されることが保証され、セキュリティの強化が図られます。さらに、暗号化の遵守状態に関する項目が削除されました。これは、特定の遵守状態に煩わされることなく、単純に暗号化を有効にするという意図が覗えます。

次に、`search-security-manage-encryption-keys.md`に同様の変更が適用されています。このファイルでも"enforcement"の設定が"Enabled"に固定され、"encryptionComplianceStatus"が削除されました。これにより、暗号化キーの管理における手順が一貫して簡潔になり、ユーザーはより明確に暗号化状態を把握できます。

これらの変更から、システム全体において暗号化設定の一貫性を高め、ユーザーが複雑な設定に迷わされることなくセキュリティの強化を行える環境を提供する意図が見て取れます。セキュリティ面の強化は、現代の情報システムにおいてますます重要性を増しており、このアップデートはそれを反映したものだと言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-manage-rest.md](#item-405ec7) | minor update | REST APIの暗号化設定の変更 | modified | 2 | 3 | 5 | 
| [search-security-manage-encryption-keys.md](#item-db3487) | minor update | 暗号化キー管理に関するセクションの修正 | modified | 1 | 2 | 3 | 


# Modified Contents
## articles/search/search-manage-rest.md{#item-405ec7}

<details>
<summary>Diff</summary>
````diff
@@ -221,9 +221,8 @@ PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegrou
      {
         "properties": {
             "encryptionWithCmk": {
-            "enforcement": "Disabled",
-            "encryptionComplianceStatus": "Compliant"
-            },
+                "enforcement": "Enabled"
+            }
         }
     }
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIの暗号化設定の変更"
}
```

### Explanation
この変更では、`search-manage-rest.md`ファイルにおけるREST APIの設定に関する部分が更新されました。具体的には、"enforcement"の値が"Disabled"から"Enabled"に変更され、暗号化の遵守状態に関する項目が削除されました。この変更は、暗号化設定の有効化を反映するものであり、全体的には文書の明確さを向上させる目的で行なわれました。

## articles/search/search-security-manage-encryption-keys.md{#item-db3487}

<details>
<summary>Diff</summary>
````diff
@@ -368,8 +368,7 @@ PATCH https://management.azure.com/subscriptions/<your-subscription-Id>/resource
 {
     "properties": {
         "encryptionWithCmk": {
-            "enforcement": "Enabled",
-            "encryptionComplianceStatus": "Compliant"
+            "enforcement": "Enabled"
         }
     }
 }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "暗号化キー管理に関するセクションの修正"
}
```

### Explanation
この変更は、`search-security-manage-encryption-keys.md`ファイルに対するものです。主に、暗号化設定に関するセクションが修正されました。"enforcement"の設定が"Enabled"に固定され、"encryptionComplianceStatus"が削除されました。この更新は、文書の簡潔さを向上させることを目的としており、暗号化キーの管理がより明確に理解できるようになります。


