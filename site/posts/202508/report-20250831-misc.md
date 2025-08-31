---
date: '2025-08-31'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d642c49...MicrosoftDocs:6863762
summary: このドキュメントの修正は、ドキュメントインテリジェンスのバッチ分析APIに関するマイナーなアップデートで、新しいAPIエンドポイントとパラメータが追加され、文言が修正されました。今回の変更には破壊的な変更はなく、主に新機能の追加と文書の更新が行われています。また、文書の著者や日付情報が更新され、APIの呼び出し方法もより明確になりました。この変更は、ユーザーに最新の仕様に基づいた正確な利用ガイドラインを提供し、APIの利用における一貫性を確保することを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d642c49...MicrosoftDocs:6863762){target="_blank"}

# ハイライト
このドキュメントの修正は、ドキュメントインテリジェンスのバッチ分析APIに関するマイナーアップデートで、新しいAPIエンドポイントやパラメータ追加と共に、文言の修正が行われました。

## 新機能
- 新しいAPIエンドポイントとパラメータが追加されました。

## 破壊的変更
- なし（今回の変更は主に新しい機能の追加と文書の更新に留まる）

## その他の更新
- 文書の著者や日付情報が更新されています。
- バッチ分析APIの呼び出し方法がより明確になりました。

# インサイト
このドキュメント変更は、ドキュメントインテリジェンスサービスを使用するユーザーに対して、最新仕様に基づく正確な利用ガイドラインを提供することを目的としています。具体的には、APIエンドポイントが最新のものに改訂され、POSTリクエストにおける呼び出し方法がより明確になるように修正されています。これにより、ユーザーは最新の形式に則って正確かつ効率的にAPIを活用できるようになります。

更新によってエンドポイントとリクエストフォーマットに変更が加えられたことは、APIの利用における一貫性を確保し、開発者がサービスを正しく構築するための助けとなります。また、文言の修正により、技術文書がよりユーザーフレンドリーになることが期待されます。アップデートされた文書は、今後のAPI利用において信頼性のあるサポートとなるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [batch-analysis.md](#item-9fb3da) | minor update | バッチ分析APIの更新と修正 | modified | 17 | 12 | 29 | 


# Modified Contents
## articles/ai-services/document-intelligence/prebuilt/batch-analysis.md{#item-9fb3da}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about the Document Intelligence Batch analysis API
 author: laujan
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 02/25/2025
+ms.date: 08/28/2025
 ms.author: lajanuar
 monikerRange: '>=doc-intel-4.0.0'
 ---
@@ -53,7 +53,7 @@ Review [Managed identities for Document Intelligence](../authentication/managed-
 
 Review [**Create SAS tokens**](../authentication/create-sas-tokens.md) to learn more about generating SAS tokens and how they work.
 
-## Calling the batch analysis API
+## Call the batch analysis API
 
 ### 1. Specify the input files
 
@@ -62,16 +62,19 @@ The batch API supports two options for specifying the files to be processed.
 * If you want to process all the files in a container or a folder, and the number of files is less than the 10000 limit, use the ```azureBlobSource``` object in your request.
 
     ```bash
-    POST /documentModels/{modelId}:analyzeBatch
+    POST {endpoint}/documentintelligence/documentModels/{modelId}:analyzeBatch?api-version=2024-11-30
 
     {
       "azureBlobSource": {
-        "containerUrl": "https://myStorageAccount.blob.core.windows.net/myContainer?mySasToken",
-        ...
-      },
-     ...
+        "containerUrl": "https://myStorageAccount.blob.core.windows.net/myContainer?mySasToken"
+      
+    },
+    {
+       "resultContainerUrl": "https://myStorageAccount.blob.core.windows.net/myOutputContainer?mySasToken",
+       "resultPrefix": "trainingDocsResult/"
     }
 
+
     ```
 
 * If you don't want to process all the files in a container or folder, but rather specific files in that container or folder, use the ```azureBlobFileListSource``` object. This operation requires a File List JSONL file which lists the files to be processed. Store the JSONL file in the root folder of the container. Here's an example JSONL file with two files listed:
@@ -88,7 +91,7 @@ Use a file list `JSONL` file with the following conditions:
   * When you want more control over which files get processed in each batch request;
 
    ```bash
-   POST /documentModels/{modelId}:analyzeBatch
+   POST {endpoint}/documentintelligence/documentModels/{modelId}:analyzeBatch?api-version=2024-11-30
 
    {
      "azureBlobFileListSource": {
@@ -119,13 +122,14 @@ Remember to replace the following sample container URL values with real values f
 
 This example shows a POST request with `azureBlobSource` input
 ```bash
-POST /documentModels/{modelId}:analyzeBatch
+POST {endpoint}/documentintelligence/documentModels/{modelId}:analyzeBatch?api-version=2024-11-30
 
 {
   "azureBlobSource": {
     "containerUrl": "https://myStorageAccount.blob.core.windows.net/myContainer?mySasToken",
     "prefix": "inputDocs/"
   },
+  {
   "resultContainerUrl": "https://myStorageAccount.blob.core.windows.net/myOutputContainer?mySasToken",
   "resultPrefix": "batchResults/",
   "overwriteExisting": true
@@ -137,13 +141,14 @@ This example shows a POST request with `azureBlobFileListSource` and a file list
 
 
 ```bash
-POST /documentModels/{modelId}:analyzeBatch
+POST {endpoint}/documentintelligence/documentModels/{modelId}:analyzeBatch?api-version=2024-11-30
 
 {
    "azureBlobFileListSource": {
       "containerUrl": "https://myStorageAccount.blob.core.windows.net/myContainer?mySasToken",
       "fileList": "myFileList.jsonl"
     },
+{
   "resultContainerUrl": "https://myStorageAccount.blob.core.windows.net/myOutputContainer?mySasToken",
   "resultPrefix": "batchResults/",
   "overwriteExisting": true
@@ -155,7 +160,7 @@ Here's an example **successful** response
 
 ```bash
 202 Accepted
-Operation-Location: /documentModels/{modelId}/analyzeBatchResults/{resultId}
+Operation-Location: /documentintelligence/documentModels/{modelId}/analyzeBatchResults/{resultId}?api-version=2024-11-30
 ```
 
 ### 4. Retrieve API results
@@ -164,7 +169,7 @@ Use the `GET` operation to retrieve batch analysis results after the POST operat
 
 
 ```bash
-GET /documentModels/{modelId}/analyzeBatchResults/{resultId}
+GET {endpoint}/documentintelligence/documentModels/{modelId}/analyzeBatchResults/{resultId}?api-version=2024-11-30
 200 OK
 
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ分析APIの更新と修正"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスのバッチ分析APIに関する文書の更新を包含しています。具体的には、いくつかのセクションで文言の修正が行われ、新しいAPIエンドポイントとパラメータが追加されました。また、文書の著者や日付の情報も更新されています。

主な変更点には、バッチ分析APIの呼び出し方法に関する説明が含まれています。具体的には、POSTリクエストにおいて新しいエンドポイントを指定する必要があることを明確にするために、APIのエンドポイントが修正されこれに伴い、リクエストフォーマットにも調整が加えられています。旧バージョンのエンドポイントから新しい形式に変更されたことが、対応する場所でのコード行の修正によって示されています。

この変更は、ユーザーに最新の使い方を案内するために必要な更新であり、将来的なAPIの利用において信頼性と一貫性を提供することを目的としています。


