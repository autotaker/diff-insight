---
date: '2025-01-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:de17d62...MicrosoftDocs:36d0ff5
summary: 今回の報告では、Azure OpenAIアシスタントガイドとJavaScript用データ使用ガイドに関する更新が行われました。主な変更点は、プレビュー版の表記を削除し、シンプルな表記に修正したことや、依存関係のアップデート、APIバージョンの更新があります。破壊的変更は報告されていません。また、両ガイドの最終更新日も更新されており、最新のドキュメントとして整備されています。これにより、ユーザーは最新の環境でスムーズにサービスを利用できるようになっています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:de17d62...MicrosoftDocs:36d0ff5){target="_blank"}

# ハイライト

- **新機能**:
  - Azure OpenAIアシスタントガイドでは、プレビュー版の表記を削除して、より直線的でシンプルな表記に修正。
  - JavaScript用データ使用ガイドでは、依存関係のアップデートとAPIバージョンの更新が行われ、より最新の環境での使用に適した形に。
  
- **破壊的変更**:
  - なし。

- **その他の更新**:
  - 両ガイドについて、最終更新日が更新され、最新のドキュメントとして整備。
  
## 新機能

Azure OpenAIアシスタントのクイックスタートガイドとJavaScript用データ使用ガイドにおいて、最新の環境に適用できるように、細かな改善が行われました。特にプレビュー版とされた表記やAPIバージョンの更新など、より最新の情報を反映しています。

## 破壊的変更

今回の更新による破壊的変更は特に報告されていません。

## その他の更新

記事の最終更新日が新たに設定され、ドキュメントの最新性を保証しています。

# インサイト

今回のコード変更では、主にAzure OpenAIアシスタントおよびJavaScript用ガイドの更新が施されました。この変更の意図は、ユーザーがこれらのサービスを使用する際、最新の環境での利用を可能とし、スムーズな導入を支援することにあります。

Azure OpenAIアシスタントのガイドでは、プレビュー版の記載を削除することで、リリース版としての整備が確認でき、これにより、新規ユーザーに対し混乱を少なくし、導入段階での明快さを優先した作りになっていることが分かります。特に、用語の簡素化と明確化が意図されています。

一方、JavaScriptのガイドでは、依存関係で使用しているパッケージが最新のものにアップデートされ、インストールコマンドが変更されたことで、ユーザーが適切な設定を維持することが可能です。APIバージョンの更新は、Azure OpenAIサービスの機能強化と、それに対する適応の必要性を示していると見られます。このことで、開発者が新しいバージョンのAPIを使用する際にもスムーズに移行できるよう、準備が整っていることを示唆しています。

全体として、これらの更新はユーザーの開発体験を向上させ、最新のテクノロジーを利用できるようにするためのものであり、変更の頻度が重要であることを利用者に認識させる補助となります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [assistants-ai-studio.md](#item-1632e2) | minor update | Azure OpenAIアシスタントのクイックスタートガイドの更新 | modified | 2 | 2 | 4 | 
| [use-your-data-javascript.md](#item-786699) | minor update | JavaScript用のデータ使用ガイドの更新 | modified | 4 | 4 | 8 | 


# Modified Contents
## articles/ai-services/openai/includes/assistants-ai-studio.md{#item-1632e2}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Quickstart - getting started with Azure OpenAI assistants (preview) in Azure AI Foundry portal
 titleSuffix: Azure OpenAI
-description: Walkthrough on how to get started with Azure OpenAI assistants with new features like code interpreter in Azure AI Foundry portal (Preview).
+description: Walkthrough on how to get started with Azure OpenAI assistants with new features like code interpreter in Azure AI Foundry portal.
 manager: nitinme
 ms.service: azure-ai-studio
 ms.custom:
@@ -21,7 +21,7 @@ ms.author: aahi
 - An [Azure AI hub resource](../../../ai-studio/how-to/create-azure-ai-resource.md) with a model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 - An [Azure AI project](../../../ai-studio/how-to/create-projects.md) in Azure AI Foundry portal.
 
-## Go to the Azure AI Foundry portal (Preview)
+## Go to the Azure AI Foundry portal
 
 [Azure AI Foundry](https://ai.azure.com) lets you use Assistants v2 which provides several upgrades such as the [file search](../how-to/file-search.md) tool which is faster and supports more files.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIアシスタントのクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azure OpenAIアシスタントに関するクイックスタートガイドの内容を少し更新したものです。具体的には、次の点が修正されました：

1. **説明文の変更**: "code interpreter in Azure AI Foundry portal (Preview)"が削除され、ただの"code interpreter in Azure AI Foundry portal"に変更されました。これにより、文がより簡潔になりました。

2. **セクションタイトルの変更**: "Go to the Azure AI Foundry portal (Preview)"から"Go to the Azure AI Foundry portal"にタイトルが変更され、プレビュー版の表記が削除されました。

この変更は全体として、ガイドの内容をより明確にし、ユーザーがAzure AI Foundryポータルに移動する際の情報を整理する助けとなります。修正は、2行の追加と2行の削除により、合計で4つの行が変更されました。

## articles/ai-services/openai/includes/use-your-data-javascript.md{#item-786699}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: glharper
 ms.author: glharper
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 10/22/2024
+ms.date: 01/10/2025
 ---
 
 [!INCLUDE [Set up required variables](./use-your-data-common-variables.md)]
@@ -24,7 +24,7 @@ npm init
 Install the Azure OpenAI client and Azure Identity libraries for JavaScript with npm:
 
 ```console
-npm install @azure/openai @azure/identity
+npm install openai @azure/identity
 ```
 
 Your app's _package.json_ file will be updated with the dependencies.
@@ -51,7 +51,7 @@ Your app's _package.json_ file will be updated with the dependencies.
 
     // Required Azure OpenAI deployment name and API version
     const deploymentName = "gpt-4";
-    const apiVersion = "2024-07-01-preview";
+    const apiVersion = "2024-10-21";
     
     function getClient() {
       return new AzureOpenAI({
@@ -139,7 +139,7 @@ Your app's _package.json_ file will be updated with the dependencies.
     
     // Required Azure OpenAI deployment name and API version
     const deploymentName = "gpt-4";
-    const apiVersion = "2024-07-01-preview";
+    const apiVersion = "2024-10-21";
     
     function getClient() {
       return new AzureOpenAI({
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript用のデータ使用ガイドの更新"
}
```

### Explanation
この変更は、JavaScriptにおけるAzure OpenAIのデータ使用に関するガイドに対する軽微な更新を示しています。主な修正点は以下の通りです：

1. **日付の更新**: `ms.date`フィールドが「2024年10月22日」から「2025年1月10日」に変更され、文書の最終更新日が新しいものに更新されました。

2. **依存関係の変更**: JavaScriptのパッケージ管理システムであるnpmによる依存関係のインストール部分が変更されました。具体的には、`npm install @azure/openai @azure/identity`が`npm install openai @azure/identity`に変更され、パッケージ名が更新されました。

3. **APIバージョンの変更**: コード内のAPIバージョンも更新されました。`"2024-07-01-preview"`から`"2024-10-21"`に変更されたことで、最新のバージョンを指すようになりました。

これらの変更は、ユーザーが最新の設定や依存関係を使用できるようにするためのもので、全体で4行の追加と4行の削除が行われた結果、合計8箇所の変更が行われました。


