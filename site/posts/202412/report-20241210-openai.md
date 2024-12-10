---
date: '2024-12-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d135a3a...MicrosoftDocs:e69b8c6
summary: この変更では、APIのバージョンが最新のものに更新され、ブロックリストに関連する説明が改訂されました。主な新機能としては、ユーザーからの入力に対するブロックリスト設定がより柔軟に行えるように、"completionBlocklists"の名称を"promptBlocklists"に変更するオプションが追加されました。これにより、AIモデルの応答だけでなく、ユーザーの入力自体にもブロックリストを適用できるようになります。APIのバージョン更新に伴う潜在的な影響についての確認が必要ですが、主にユーザーエクスペリエンスの向上が目的とされています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d135a3a...MicrosoftDocs:e69b8c6){target="_blank"}

# ハイライト
この変更では、APIバージョンが最新のものに更新され、ブロックリストに関連するいくつかの説明が改訂されました。主な新機能としては、ユーザーからの入力に対するブロックリスト設定がより柔軟に行えるよう、"completionBlocklists"のタイトルを"promptBlocklists"に変更できるようになったことです。これにより、AIモデルの応答だけでなく、ユーザーの入力自体にもブロックリストを適用できるようになります。

## 新機能
- APIのバージョンが"2024-03-01-preview"から"2024-04-01-preview"に変更され、新しい機能や改善点が反映されています。
- プロンプトに適用されるブロックリストをより柔軟に扱えるように、"completionBlocklists"という名称を"promptBlocklists"に変更するオプションが追加されました。

## 破壊的変更
特に破壊的な変更は見当たりませんが、APIバージョンの更新に伴い、既存の実装に影響を与える可能性があるため、確認が必要です。

## その他の更新
- ブロックリスト名に関するガイドラインが明確化され、許可される文字が列挙されるようになりました。

# インサイト
この変更は、主にユーザーエクスペリエンスの向上と誤解を減らすことを目的としています。APIバージョンの更新は、通常、新機能や改善された機能を含みますが、具体的な機能の改良についてはここで明示されていません。しかしながら、バージョンの更新に伴う対応を行うことで、APIを利用する開発者はより効率的で効果的な開発が可能になるでしょう。

また、ブロックリストの名称変更オプションにより、ユーザーはコンテンツフィルタリングをより柔軟に管理できるようになります。これにより、特にスパムや不適切なコンテンツをプロンプトレベルで事前に防止することが容易になります。ブロックリスト名称に関するガイドラインの明確化も、APIの設定時に不必要なエラーを防ぎ、スムーズな利用を促進するものです。これらの変更は、開発者にとってのハードルを下げ、API利用の利便性を向上させます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [use-blocklists.md](#item-e99db7) | minor update | APIバージョンの更新とブロックリストの説明の変更 | modified | 5 | 4 | 9 | 


# Modified Contents
## articles/ai-services/openai/how-to/use-blocklists.md{#item-e99db7}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ Copy the cURL command below to a text editor and make the following changes:
 1. Optionally replace the value of the "description" field with a custom description.
 
 ```bash
-curl --location --request PUT 'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/raiBlocklists/{raiBlocklistName}?api-version=2024-03-01-preview' \ 
+curl --location --request PUT 'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/raiBlocklists/{raiBlocklistName}?api-version=2024-04-01-preview' \ 
 --header 'Authorization: Bearer {token}' \ 
 --header 'Content-Type: application/json' \ 
 --data-raw '{ 
@@ -72,10 +72,11 @@ To apply a **completion** blocklist to a content filter, use the following cURL
 1. Replace {accountName} with your resource name. 
 1. Replace {raiPolicyName} with the name of your Content Filter 
 1. Replace {token} with the token you got from the "Get your token" step above. 
-1. Replace "raiBlocklistName" in the body with a custom name for your list. Allowed characters: `0-9, A-Z, a-z, - . _ ~`. 
+1. Optionally change the `"completionBlocklists"` title to `"promptBlocklists"` if you want the blocklist to apply to user prompts instead of AI model completions.
+1. Replace `"raiBlocklistName"` in the body with a custom name for your list. Allowed characters: `0-9, A-Z, a-z, - . _ ~`. 
 
 ```bash
-curl --location --request PUT 'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/raiPolicies/{raiPolicyName}?api-version=2024-03-01-preview' \ 
+curl --location --request PUT 'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/raiPolicies/{raiPolicyName}?api-version=2024-04-01-preview' \ 
 --header 'Authorization: Bearer {token}' \ 
 --header 'Content-Type: application/json' \ 
 --data-raw '{ 
@@ -105,7 +106,7 @@ Copy the cURL command below to a text editor and make the following changes:
 1. Replace the value of the `"blocking pattern"` field with the item you'd like to add to your blocklist. The maximum length of a blockItem is 1000 characters. Also specify whether the pattern is regex or exact match. 
 
 ```bash
-curl --location --request PUT 'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/raiBlocklists/{raiBlocklistName}/raiBlocklistItems/{raiBlocklistItemName}?api-version=2024-03-01-preview' \ 
+curl --location --request PUT 'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/raiBlocklists/{raiBlocklistName}/raiBlocklistItems/{raiBlocklistItemName}?api-version=2024-04-01-preview' \ 
 --header 'Authorization: Bearer {token}' \ 
 --header 'Content-Type: application/json' \ 
 --data-raw '{  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新とブロックリストの説明の変更"
}
```

### Explanation
この変更は、APIバージョンのアップデートと、ブロックリストに関連するいくつかの説明の修正を含んでいます。具体的には、いくつかのcURLコマンドで使用されているAPIバージョンが、"2024-03-01-preview"から"2024-04-01-preview"に変更されました。また、ユーザーがプロンプトに適用されるブロックリストをより柔軟に扱えるように、"completionBlocklists"のタイトルを"promptBlocklists"に変更するオプションが追加されました。これにより、利用者はAIモデルの回答ではなく、ユーザーからの入力に対してブロックリストを設定できるようになります。

さらに、ブロックリスト名に関するガイドラインの説明が明確化され、ブロックリスト名には使用できる許可された文字が列挙されています。これらの改訂は、ユーザーがAPIを利用する際の使いやすさを向上させ、誤解を減らすことを目的としています。


