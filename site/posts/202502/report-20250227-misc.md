---
date: '2025-02-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bc33227...MicrosoftDocs:42a07e4
summary: |-
  このコードの変更に関する要約は以下の通りです。

  Azure Document Intelligenceサービスのバッチ分析APIに関するドキュメントが更新され、特に「Phi-4-mini-instruct」という新しいモデルが追加されました。バッチ分析APIは一度のリクエストで最大10,000件のドキュメントを処理できるようになり、ユーザーにとって利便性が向上しています。また、具体的な手順や推奨事項が強化され、実際の使用時の理解が深められています。破壊的な変更はないものの、新しい機能に慣れる必要がある点に注意が必要です。ストレージコンテナへの認証方法やAPI応答解析についても詳細が更新され、ナビゲーションリンクの改善により、最新のドキュメントへのアクセスが容易になりました。全体として、ユーザーエクスペリエンスの向上が図られています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bc33227...MicrosoftDocs:42a07e4){target="_blank"}

<format>
# Highlights
このコードの変更では、主にAzureのDocument Intelligenceサービスのバッチ分析API、Phi-4ファミリーモデルのデプロイガイド、モデルカタログ、地域別可用性、およびナビゲーションリンクに関するドキュメントが更新されています。特に新しいモデル「Phi-4-mini-instruct」に関する情報が追加され、バッチ分析APIで処理可能なドキュメント数が10,000件に増加したことが注目されます。

## New features
- バッチ分析APIが最大10,000件のドキュメントを一度のリクエストで処理可能になりました。
- Phi-4ファミリーモデルに「Phi-4-mini-instruct」という新モデルが追加されました。
- 実際の利用シーンでの理解を深めるために、具体的手順や推奨事項が強化されました。

## Breaking changes
- 特に大きな破壊的変更はありませんが、新しい機能と情報の追加により、既存のユーザーは新しい環境や利用方法に慣れる必要があります。

## Other updates
- ストレージコンテナへの認証方法やAPI応答解析についての詳細が更新されました。
- 新たに更新された画像により、ドキュメントの視覚的情報が最新化されました。

# Insights
このドキュメントの更新は、Azure Document IntelligenceとAI Studioを利用するユーザーにとって、非常に価値のある情報を提供します。特に、バッチ分析APIの処理能力の拡大は、大量のドキュメントを迅速に処理する必要があるユーザーにとって有益です。ドキュメントでの詳細な手順と推奨事項の導入は、実際の運用時のトラブルを減少させ、ユーザーエクスペリエンスを向上させます。一方、Phi-4ファミリーに新しく追加された「Phi-4-mini-instruct」モデルは、軽量でありながら高い性能を持つとして紹介されており、特に指示遵守における強化が図られているため、さまざまなAI活用シーンで重宝されるでしょう。また、ドキュメントにおいて明確化されたストレージコンテナ認証方法やAPIの応答解析は、開発者がより深くサービスを理解し、効率的に利用できる助けになります。ナビゲーションリンクの更新により、ユーザーが最新のドキュメントにアクセスする際の体験が向上し、全体的な品質改善がなされています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [batch-analysis.md](#item-9fb3da) | minor update | バッチ分析のAPIに関するドキュメントの更新 | modified | 169 | 145 | 314 | 
| [deploy-models-phi-4.md](#item-c40212) | minor update | Phi-4モデルに関するデプロイガイドの更新 | modified | 96 | 28 | 124 | 
| [model-catalog-overview.md](#item-278001) | minor update | Phiファミリーモデルに関する情報の更新 | modified | 1 | 1 | 2 | 
| [region-availability-maas.md](#item-35d79c) | minor update | モデルの可用性情報の更新 | modified | 1 | 1 | 2 | 
| [fine-tune-azure-ai-services.png](#item-794ba3) | minor update | 画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [toc.yml](#item-2745cd) | minor update | ナビゲーションリンクの更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/prebuilt/batch-analysis.md{#item-9fb3da}

<details>
<summary>Diff</summary>
````diff
@@ -1,119 +1,140 @@
 ---
 title: "Batch analysis and processing"
 titleSuffix: Azure AI services
-description: Learn about the Document Intelligence Batch analysis API 
+description: Learn about the Document Intelligence Batch analysis API
 author: laujan
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 02/07/2025
+ms.date: 02/25/2025
 ms.author: lajanuar
 monikerRange: '>=doc-intel-4.0.0'
 ---
 
-# Document Intelligence batch analysis 
+# Document Intelligence batch analysis
 
-The batch analysis API allows you to bulk process multiple documents using one asynchronous request. Rather than having to submit documents individually and track multiple request IDs, you can analyze a collection of documents like invoices, a series of loan documents, or a group of custom documents simultaneously. The batch API supports reading the documents from Azure blob storage and writing the results to blob storage.
+The batch analysis API allows you to bulk process up to 10,000 documents using one request. Instead of analyzing documents one by one and keeping track of their respective request IDs, you can simultaneously analyze a collection of documents like invoices, loan papers, or custom documents. The input documents must be stored in an Azure blob storage container. Once the documents are processed, the API writes the results to a specified storage container.
 
-* To utilize batch analysis, you need an Azure Blob storage account with specific containers for both your source documents and the processed outputs.
-* Upon completion, the batch operation result lists all of the individual documents processed with their status, such as `succeeded`, `skipped`, or `failed`.
-* The Batch API preview version is available via pay-as-you-go pricing.
+## Batch analysis limits
 
-## Batch analysis guidance
+* The maximum number of document files that can be in a single batch request is 10,000.
+* Batch operation results are retained for 24 hours after completion. The batch operation status is no longer available 24 hours after batch processing is completed. The input documents and respective result files remain in the storage containers provided.
 
-* The maximum number of documents processed per single batch analyze request (including skipped documents) is 10,000.
+## Prerequisites
 
-* Operation results are retained for 24 hours after completion. The documents and results are in the storage account provided, but operation status is no longer available 24 hours after completion.
+* An active Azure subscription. If you don't have an Azure subscription, you can [create one for free](https://azure.microsoft.com/free/cognitive-services/).
 
-Ready to get started?
+*  A [Document Intelligence Azure Resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer): once you have your Azure subscription, create a Document Intelligence resource in the Azure portal. You can use the free pricing tier (F0) to try the service. After your resource is deployed, select **"Go to resource"** to retrieve your **key** and **endpoint**. You need the resource key and endpoint to connect your application to the Document Intelligence service. You can also find these values on the **Keys and Endpoint** page in Azure portal.
 
-## Prerequisites
+*  An [Azure Blob Storage account](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM). [Create two containers](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container) in your Azure Blob Storage account for your source and result files:
 
-* You need an active Azure subscription. If you don't have an Azure subscription, you can [create one for free](https://azure.microsoft.com/free/cognitive-services/).
+     * **Source container**: This container is where you upload document files for analysis.
+     * **Result container**: This container is where results from the batch analysis API are stored.
 
-* Once you have your Azure subscription A [Document Intelligence](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) instance in the Azure portal. You can use the free pricing tier (`F0`) to try the service.
+### Storage container authorization
 
-* After your resource deploys, select **Go to resource** and retrieve your key and endpoint.
+To allow the API to process documents and write results in your Azure storage containers, you must authorize using one of the following two options:
 
-  * You need the key and endpoint from the resource to connect your application to the Document Intelligence service. You paste your key and endpoint into the code later in the quickstart. You can find these values on the Azure portal **Keys and Endpoint** page.
 
-* An [**Azure Blob Storage account**](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM). You'll [**create containers**](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container) in your Azure Blob Storage account for your source and result files:
+**✔️ Managed Identity**. A managed identity is a service principal that creates a Microsoft Entra identity and specific permissions for an Azure managed resource. Managed identities enable you to run your Document Intelligence application without having to embed credentials in your code, a safer way to grant access to storage data without including access signature tokens (SAS) in your code.
 
-  * **Source container**. This container is where you upload your files for analysis (required).
-  * **Result container**. This container is where your processed files are stored (optional).
+Review [Managed identities for Document Intelligence](../authentication/managed-identities.md) to learn how to enable a managed identity for your resource and grant it access to your storage container.
 
-You can designate the same Azure Blob Storage container for source and processed documents. However, to minimize potential chances of accidentally overwriting data, we recommend choosing separate containers.
+> [!IMPORTANT]
+>
+> When using managed identities, don't include a SAS token URL with your HTTP requests. Using managed identities replaces the requirement for you to include shared access signature tokens (SAS).
 
-### Storage container authorization
 
-You can choose one of the following options to authorize access to your Document resource.
+**✔️ Shared Access Signature (SAS)**. A shared access signature is a URL that grants restricted access to your storage container. To use this method, create Shared Access Signature (SAS) tokens for your source and result containers. Go to the storage container in Azure portal and select **"Shared access tokens"** to generate SAS token and URL.
 
-**✔️ Managed Identity**. A managed identity is a service principal that creates a Microsoft Entra identity and specific permissions for an Azure managed resource. Managed identities enable you to run your Document Intelligence application without having to embed credentials in your code. Managed identities are a safer way to grant access to storage data and replace the requirement for you to include shared access signature tokens (SAS) with your source and result URLs.
+* Your **source** container or blob must designate **read**, **write**, **list**, and **delete** permissions.
+* Your **result** container or blob must designate **write**, **list**, **delete** permissions.
 
-To learn more, *see* [Managed identities for Document Intelligence](../authentication/managed-identities.md).
+:::image type="content" source="../media/sas-tokens/sas-permissions.png" alt-text="Screenshot that shows the SAS permission fields in the Azure portal.":::
 
-  :::image type="content" source="../media/managed-identities/rbac-flow.png" alt-text="Screenshot of managed identity flow (role-based access control).":::
+Review [**Create SAS tokens**](../authentication/create-sas-tokens.md) to learn more about generating SAS tokens and how they work.
 
-> [!IMPORTANT]
->
-> * When using managed identities, don't include a SAS token URL with your HTTP requests—your requests will fail. Using managed identities replaces the requirement for you to include shared access signature tokens (SAS).
+## Calling the batch analysis API
 
-**✔️ Shared Access Signature (SAS)**. A shared access signature is a URL that grants restricted access for a specified period of time to your Document Intelligence service. To use this method, you need to create Shared Access Signature (SAS) tokens for your source and result containers. The source and result containers must include a Shared Access Signature (SAS) token, appended as a query string. The token can be assigned to your container or specific blobs.
+### 1. Specify the input files
 
-:::image type="content" source="../media/sas-tokens/sas-url-token.png" alt-text="Screenshot of storage URI with SAS token appended.":::
+The batch API supports two options for specifying the files to be processed.
 
-* Your **source** container or blob must designate **read**, **write**, **list**, and **delete** access.
-* Your **result** container or blob must designate **write**, **list**, **delete** access.
+* If you want to process all the files in a container or a folder, and the number of files is less than the 10000 limit, use the ```azureBlobSource``` object in your request.
 
-To learn more, *see* [**Create SAS tokens**](../authentication/create-sas-tokens.md).
+    ```bash
+    POST /documentModels/{modelId}:analyzeBatch
 
-## Calling the batch analysis API
+    {
+      "azureBlobSource": {
+        "containerUrl": "https://myStorageAccount.blob.core.windows.net/myContainer?mySasToken",
+        ...
+      },
+     ...
+    }
 
-* Specify the Azure Blob Storage container URL for your source document set within the `azureBlobSource` or `azureBlobFileListSource` objects.
+    ```
 
-### Specify the input files
+* If you don't want to process all the files in a container or folder, but rather specific files in that container or folder, use the ```azureBlobFileListSource``` object. This operation requires a File List JSONL file which lists the files to be processed. Store the JSONL file in the root folder of the container. Here's an example JSONL file with two files listed:
 
-The batch API supports two options for specifying the files to be processed. If you need all files in a container or folder processed, and the number of files is less than the 10000 limit for a single batch request, use the ```azureBlobSource``` container. 
+  ```json
+  {"file": "Adatum Corporation.pdf"}
+  {"file": "Best For You Organics Company.pdf"}
+  ```
 
-If you have specific files in the container or folder to process or the number of files to be processed is over the max limit for a single batch, use the ```azureBlobFileListSource```. Split the dataset into multiple batches and add a file with the list of files to be processed in a JSONL format in the root folder of the container. An example of the file list format is.
+Use a file list `JSONL` file with the following conditions:
 
-```JSON
-{"file": "Adatum Corporation.pdf"}
-{"file": "Best For You Organics Company.pdf"}
-```
-### Specify the results location
+  * When you need to process specific files instead of all files in a container;
+  * When the total number of files in the input container or folder exceeds the 10,000 file batch processing limit;
+  * When you want more control over which files get processed in each batch request;
+
+   ```bash
+   POST /documentModels/{modelId}:analyzeBatch
+
+   {
+     "azureBlobFileListSource": {
+       "containerUrl": "https://myStorageAccount.blob.core.windows.net/myContainer?mySasToken",
+       "fileList": "myFileList.jsonl"
+       ...
+     },
+     ...
+   }
+
+   ```
+
+A container URL or a container SAS URL is required in both options. Use container URL if using managed Identity to access your storage container. If you're using Shared Access Signature (SAS), use a SAS URL.
 
-Specify the Azure Blob Storage container URL for your batch analysis results using `resultContainerUrl`. To avoid accidental overwriting, we recommend using separate containers for source and processed documents.
 
-Set the ```overwriteExisting``` boolean property to false if you don't want any existing results with the same file names overwritten. This setting doesn't affect the billing and only prevents results from being overwritten after the input file is processed.
+### 2. Specify the results location
 
-Set the ```resultPrefix``` to namespace the results from this run of the batch API. 
+* Specify the Azure Blob Storage container URL (or container SAS URL) for where you want your results to be stored using `resultContainerURL` parameter. We recommend using separate containers for source and results to prevent accidental overwriting.
 
-  * If you plan to use the same container for both input and output, set `resultContainerUrl` and `resultPrefix` to match your input `azureBlobSource`.
-  * When using the same container, you can include the `overwriteExisting` field to decide whether to overwrite any files with the analysis result files.
+* Set the `overwriteExisting` Boolean property to `False` and prevent overwriting any existing results for the same document. If you'd like to overwrite any existing results, set the Boolean to `True`. You're still billed for processing the document even if any existing results aren't overwritten.
 
-## Build and run the POST request
+* Use `resultPrefix` to group and store results in a specific container folder.
 
-Before you run the POST request, replace {your-source-container-SAS-URL} and {your-result-container-SAS-URL} with the values from your Azure Blob storage container instances.
 
-The following sample shows how to add the ```azureBlobSource``` property to the request:
+### 3. Build and run the POST request
 
-**Allow only one either `azureBlobSource` or `azureBlobFileListSource`.**
+Remember to replace the following sample container URL values with real values from your Azure Blob storage containers.
 
+This example shows a POST request with `azureBlobSource` input
 ```bash
 POST /documentModels/{modelId}:analyzeBatch
 
 {
   "azureBlobSource": {
     "containerUrl": "https://myStorageAccount.blob.core.windows.net/myContainer?mySasToken",
-    "prefix": "trainingDocs/"
+    "prefix": "inputDocs/"
   },
   "resultContainerUrl": "https://myStorageAccount.blob.core.windows.net/myOutputContainer?mySasToken",
-  "resultPrefix": "layoutresult/",
+  "resultPrefix": "batchResults/",
   "overwriteExisting": true
 }
 
 ```
-The following sample shows how to add the ```azureBlobFileListSource``` property to the request:
+
+This example shows a POST request with `azureBlobFileListSource` and a file list input
+
 
 ```bash
 POST /documentModels/{modelId}:analyzeBatch
@@ -124,22 +145,23 @@ POST /documentModels/{modelId}:analyzeBatch
       "fileList": "myFileList.jsonl"
     },
   "resultContainerUrl": "https://myStorageAccount.blob.core.windows.net/myOutputContainer?mySasToken",
-  "resultPrefix": "customresult/",
+  "resultPrefix": "batchResults/",
   "overwriteExisting": true
 }
 
 ```
 
-***Successful response***
+Here's an example **successful** response
 
 ```bash
 202 Accepted
 Operation-Location: /documentModels/{modelId}/analyzeBatchResults/{resultId}
 ```
 
-## Retrieve batch analysis API results
+### 4. Retrieve API results
+
+Use the `GET` operation to retrieve batch analysis results after the POST operation is executed. The GET operation fetches status information, batch completion percentage, and operation creation and update date/time. This information is **only retained for 24 hours** after the batch analysis is completed.
 
-After the Batch API operation is executed, you can retrieve the batch analysis results using the`GET` operation. This operation fetches operation status information, operation completion percentage, and operation creation and update date/time.
 
 ```bash
 GET /documentModels/{modelId}/analyzeBatchResults/{resultId}
@@ -154,99 +176,101 @@ GET /documentModels/{modelId}/analyzeBatchResults/{resultId}
 }
 ```
 
-## Interpreting status messages
+### 5. Interpret status messages
 
-For each document a set, there a status is assigned, either `succeeded`, `failed`, or `skipped`. For each document, there are two URLs provided to validate the results: `sourceUrl`, which is the source blob storage container for your succeeded input document, and `resultUrl`, which is constructed by combining `resultContainerUrl` and`resultPrefix` to create the relative path for the source file and `.ocr.json`.
+For each document processed, a status is assigned, either `succeeded`, `failed`, `running`, `notStarted`, or `skipped`. A source URL, which is the source blob storage container for the input document, is provided.
 
 * Status `notStarted` or `running`. The batch analysis operation isn't initiated or isn't completed. Wait until the operation is completed for all documents.
 
 * Status `completed`. The batch analysis operation is finished.
 
-* Status `failed`. The batch operation failed. This response usually occurs if there are overall issues with the request. Failures on individual files are returned in the batch report response, even if all the files failed. For example, storage errors don't halt the batch operation as a whole, so that you can access partial results via the batch report response.
-
-Only files that have a `succeeded` status have the property `resultUrl` generated in the response. This enables model training to detect file names that end with `.ocr.json` and identify them as the only files that can be used for training.
-
-Example of a `succeeded` status response:
-
-```bash
-[
-  "result": {
-    "succeededCount": 0,
-    "failedCount": 2,
-    "skippedCount": 2,
-    "details": [
-      {
-        "sourceUrl": "https://{your-source-container}/myContainer/trainingDocs/file2.jpg",
-        "status": "failed",
-        "error": {
-          "code": "InvalidArgument",
-          "message": "Invalid argument.",
-          "innererror": {
-            "code": "InvalidSasToken",
-            "message": "The shared access signature (SAS) is invalid: {details}"
-                   }
-               }
-          }
-      ]
-   }
-]
-...
-```
-
-Example of a `failed` status response:
-
-* This error is only returned if there are errors in the overall batch request.
-* Once the batch analysis operation is started, individual document operation status doesn't affect the status of the overall batch job, even if all the files have the status `failed`.
-
-```bash
-[
-    "result": {
-    "succeededCount": 0,
-    "failedCount": 2,
-    "skippedCount": 2,
-    "details": [
-        "sourceUrl": "https://{your-source-container}/myContainer/trainingDocs/file2.jpg",
-        "status": "failed",
-        "error": {
-            "code": "InvalidArgument",
-            "message": "Invalid argument.",
-            "innererror": {
-              "code": "InvalidSasToken",
-              "message": "The shared access signature (SAS) is invalid: {details}"
+* Status `succeeded`. The batch operation was successful, and input document was processed. The results are available at `resultUrl`, which is created by combining `resultContainerUrl`, `resultPrefix`, `input filename`, and `.ocr.json` extension. **Only files that have succeeded have the property `resultUrl`**.
+
+  Example of a `succeeded` status response:
+
+
+  ```bash
+  {
+      "resultId": "myresultId-",
+      "status": "succeeded",
+      "percentCompleted": 100,
+      "createdDateTime": "2025-01-01T00:00:000",
+      "lastUpdatedDateTime": "2025-01-01T00:00:000",
+      "result": {
+          "succeededCount": 10,000,
+          "failedCount": 0,
+          "skippedCount": 0,
+          "details": [
+              {
+                  "sourceUrl": "https://{your-source-container}/inputFolder/document1.pdf",
+                  "resultUrl": "https://{your-result-container}/resultsFolder/document1.pdf.ocr.json",
+                  "status": "succeeded"
+              },
+            ...
+              {
+                  "sourceUrl": "https://{your-source-container}/inputFolder/document10000.pdf",
+                  "resultUrl": "https://{your-result-container}/resultsFolder/document10000.pdf.ocr.json",
+                  "status": "succeeded"
+              }
+         ]
+
+       }
+  }
+  ```
+
+* Status `failed`. This error is only returned if there are errors in the overall batch request. Once the batch analysis operation starts, the individual document operation status doesn't affect the status of the overall batch job, even if all the files have the status `failed`.
+
+    Example of a `failed` status response:
+
+    ```bash
+    [
+        "result": {
+        "succeededCount": 0,
+        "failedCount": 2,
+        "skippedCount": 0,
+        "details": [
+            "sourceUrl": "https://{your-source-container}/inputFolder/document1.jpg",
+            "status": "failed",
+            "error": {
+                "code": "InvalidArgument",
+                "message": "Invalid argument.",
+                "innererror": {
+                  "code": "InvalidSasToken",
+                  "message": "The shared access signature (SAS) is invalid: {details}"
+                    }
                 }
-            }
-        ]
-    }
-]
-...
-```
-
-Example of `skipped` status response:
-
-```bash
-[
-    "result": {
-    "succeededCount": 3,
-    "failedCount": 0,
-    "skippedCount": 2,
-    "details": [
-        ...
-        "sourceUrl": "https://myStorageAccount.blob.core.windows.net/myContainer/trainingDocs/file4.jpg",
-        "status": "skipped",
-        "error": {
-            "code": "OutputExists",
-            "message": "Analysis skipped because result file {path} already exists."
-             }
-        ]
-    }
-]
-...
-```
-
-The batch analysis results help you identify which files are successfully analyzed and validate the analysis results by comparing the file in the `resultUrl` with the output file in the `resultContainerUrl`.
-
-> [!NOTE]
-> Analysis results aren't returned for individual files until the entire document set batch analysis is completed. To track detailed progress beyond `percentCompleted`, you can monitor `*.ocr.json` files as they are written into the `resultContainerUrl`.
+            ]
+        }
+    ]
+    ...
+    ```
+
+* Status `skipped`: Typically, this status happens when output for the document is already present in the specified output folder and the `overwriteExisting` Boolean property is set to `false`.
+
+  Example of `skipped` status response:
+
+   ```bash
+   [
+       "result": {
+       "succeededCount": 3,
+       "failedCount": 0,
+       "skippedCount": 2,
+       "details": [
+           ...
+           "sourceUrl": "https://{your-source-container}/inputFolder/document1.pdf",
+           "status": "skipped",
+           "error": {
+               "code": "OutputExists",
+               "message": "Analysis skipped because result file https://{your-result-container}/resultsFolder/document1.pdf.ocr.json already exists."
+                }
+           ]
+       }
+   ]
+   ...
+   ```
+
+  > [!NOTE]
+  > Analysis results aren't returned for individual files until analysis for the entire batch is completed. To track detailed progress beyond `percentCompleted`, you can monitor `*.ocr.json` files as they're written into the    `resultContainerUrl`.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ分析のAPIに関するドキュメントの更新"
}
```

### Explanation
この変更は、AzureのDocument Intelligenceのバッチ分析APIに関するドキュメントを改訂したものです。主な更新内容には、バッチリクエストで処理できるドキュメントの数が最大10,000件に増加したこと、利用者に対する具体的な手順や推奨事項が追加されたこと、改善された説明が含まれます。さらに、ドキュメントの保持期間、ストレージコンテナの承認方法、POSTリクエストの構築手順、およびAPIの応答の解析についての詳細も強調されています。

変更された内容は以下の通りです：

1. バッチ分析APIを使用すると、一度のリクエストで最大10,000件のドキュメントを処理できるようになりました。
2. プリフィックスや結果を保存する場所に関する設定がわかりやすく説明され、新しい要件が示されています。
3. ストレージコンテナへの認証方法として、Managed IdentityやShared Access Signature (SAS) の詳細が明記されています。
4. APIの応答やドキュメントの状態（成功、失敗、スキップなど）についての説明が明確化されています。

これにより、開発者やユーザーはバッチ分析をより効果的に利用できるようになります。また、新しい例や注意点も含まれており、実際の利用シーンでの理解を深めるために役立ちます。

## articles/ai-studio/how-to/deploy-models-phi-4.md{#item-c40212}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Phi-4 family chat models with Azure AI Foundry.
 ms.service: azure-ai-foundry
 manager: scottpolly
 ms.topic: how-to
-ms.date: 01/09/2025
+ms.date: 02/25/2025
 ms.reviewer: v-vkonjarla
 reviewer: VindyaKonjarla
 ms.author: mopeakande
@@ -27,18 +27,35 @@ The Phi-4 family of small language models (SLMs) is a collection of instruction-
 
 ## Phi-4 family chat models
 
+The Phi-4 family chat models include the following models:
+
+# [Phi-4-mini-instruct](#tab/phi-4-mini-instruct)
+
+Phi-4-mini-instruct is a lightweight open model built upon synthetic data and filtered publicly available websites - with a focus on high-quality, reasoning dense data. The model belongs to the Phi-4 model family and supports 128K token context length. The model underwent an enhancement process, incorporating both supervised fine-tuning and direct preference optimization to support precise instruction adherence and robust safety measures. 
+
+The Phi-4-mini-instruct model comes in the following variant with a 128K token length.
+
+
+The following models are available:
+
+* [Phi-4-mini-instruct](https://aka.ms/azureai/landing/Phi-4-mini-instruct)
+
+
+# [Phi-4](#tab/phi-4)
+
 Phi-4 is a state-of-the-art open model built upon a blend of synthetic datasets, data from filtered public domain websites, and acquired academic books and Q&A datasets. The goal of this approach was to ensure that small capable models were trained with data focused on high quality and advanced reasoning.
 
 Phi-4 underwent a rigorous enhancement and alignment process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures.
+The Phi-4 model comes in the following variant with a 16K token length.
 
-The Phi-4 models come in the following variants with a 16K tokens length.
 
-
-You can learn more about the models in their respective model card:
+The following models are available:
 
 * [Phi-4](https://aka.ms/azureai/landing/Phi-4)
 
 
+---
+
 ## Prerequisites
 
 To use Phi-4 family chat models with Azure AI Foundry, you need the following prerequisites:
@@ -138,7 +155,7 @@ print("Model provider name:", model_info.model_provider_name)
 ```
 
 ```console
-Model name: Phi-4
+Model name: Phi-4-mini-instruct
 Model type: chat-completions
 Model provider name: Microsoft
 ```
@@ -159,7 +176,7 @@ response = client.complete(
 ```
 
 > [!NOTE]
-> Phi-4 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> Phi-4-mini-instruct and Phi-4 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -175,7 +192,7 @@ print("\tCompletion tokens:", response.usage.completion_tokens)
 
 ```console
 Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
-Model: Phi-4
+Model: Phi-4-mini-instruct
 Usage: 
   Prompt tokens: 19
   Total tokens: 91
@@ -322,18 +339,35 @@ except HttpResponseError as ex:
 
 ## Phi-4 family chat models
 
+The Phi-4 family chat models include the following models:
+
+# [Phi-4-mini-instruct](#tab/phi-4-mini-instruct)
+
+Phi-4-mini-instruct is a lightweight open model built upon synthetic data and filtered publicly available websites - with a focus on high-quality, reasoning dense data. The model belongs to the Phi-4 model family and supports 128K token context length. The model underwent an enhancement process, incorporating both supervised fine-tuning and direct preference optimization to support precise instruction adherence and robust safety measures. 
+
+The Phi-4-mini-instruct model comes in the following variant with a 128K token length.
+
+
+The following models are available:
+
+* [Phi-4-mini-instruct](https://aka.ms/azureai/landing/Phi-4-mini-instruct)
+
+
+# [Phi-4](#tab/phi-4)
+
 Phi-4 is a state-of-the-art open model built upon a blend of synthetic datasets, data from filtered public domain websites, and acquired academic books and Q&A datasets. The goal of this approach was to ensure that small capable models were trained with data focused on high quality and advanced reasoning.
 
 Phi-4 underwent a rigorous enhancement and alignment process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures.
+The Phi-4 model comes in the following variant with a 16K token length.
 
-The Phi-4 models come in the following variants with a 16K tokens length.
 
-
-You can learn more about the models in their respective model card:
+The following models are available:
 
 * [Phi-4](https://aka.ms/azureai/landing/Phi-4)
 
 
+---
+
 ## Prerequisites
 
 To use Phi-4 family chat models with Azure AI Foundry, you need the following prerequisites:
@@ -431,7 +465,7 @@ console.log("Model provider name: ", model_info.body.model_provider_name)
 ```
 
 ```console
-Model name: Phi-4
+Model name: Phi-4-mini-instruct
 Model type: chat-completions
 Model provider name: Microsoft
 ```
@@ -454,7 +488,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!NOTE]
-> Phi-4 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> Phi-4-mini-instruct and Phi-4 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -474,7 +508,7 @@ console.log("\tCompletion tokens:", response.body.usage.completion_tokens);
 
 ```console
 Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
-Model: Phi-4
+Model: Phi-4-mini-instruct
 Usage: 
   Prompt tokens: 19
   Total tokens: 91
@@ -640,18 +674,35 @@ catch (error) {
 
 ## Phi-4 family chat models
 
+The Phi-4 family chat models include the following models:
+
+# [Phi-4-mini-instruct](#tab/phi-4-mini-instruct)
+
+Phi-4-mini-instruct is a lightweight open model built upon synthetic data and filtered publicly available websites - with a focus on high-quality, reasoning dense data. The model belongs to the Phi-4 model family and supports 128K token context length. The model underwent an enhancement process, incorporating both supervised fine-tuning and direct preference optimization to support precise instruction adherence and robust safety measures. 
+
+The Phi-4-mini-instruct model comes in the following variant with a 128K token length.
+
+
+The following models are available:
+
+* [Phi-4-mini-instruct](https://aka.ms/azureai/landing/Phi-4-mini-instruct)
+
+
+# [Phi-4](#tab/phi-4)
+
 Phi-4 is a state-of-the-art open model built upon a blend of synthetic datasets, data from filtered public domain websites, and acquired academic books and Q&A datasets. The goal of this approach was to ensure that small capable models were trained with data focused on high quality and advanced reasoning.
 
 Phi-4 underwent a rigorous enhancement and alignment process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures.
+The Phi-4 model comes in the following variant with a 16K token length.
 
-The Phi-4 models come in the following variants with a 16K tokens length.
 
-
-You can learn more about the models in their respective model card:
+The following models are available:
 
 * [Phi-4](https://aka.ms/azureai/landing/Phi-4)
 
 
+---
+
 ## Prerequisites
 
 To use Phi-4 family chat models with Azure AI Foundry, you need the following prerequisites:
@@ -764,7 +815,7 @@ Console.WriteLine($"Model provider name: {modelInfo.Value.ModelProviderName}");
 ```
 
 ```console
-Model name: Phi-4
+Model name: Phi-4-mini-instruct
 Model type: chat-completions
 Model provider name: Microsoft
 ```
@@ -786,7 +837,7 @@ Response<ChatCompletions> response = client.Complete(requestOptions);
 ```
 
 > [!NOTE]
-> Phi-4 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> Phi-4-mini-instruct and Phi-4 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -802,7 +853,7 @@ Console.WriteLine($"\tCompletion tokens: {response.Value.Usage.CompletionTokens}
 
 ```console
 Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
-Model: Phi-4
+Model: Phi-4-mini-instruct
 Usage: 
   Prompt tokens: 19
   Total tokens: 91
@@ -970,18 +1021,35 @@ catch (RequestFailedException ex)
 
 ## Phi-4 family chat models
 
+The Phi-4 family chat models include the following models:
+
+# [Phi-4-mini-instruct](#tab/phi-4-mini-instruct)
+
+Phi-4-mini-instruct is a lightweight open model built upon synthetic data and filtered publicly available websites - with a focus on high-quality, reasoning dense data. The model belongs to the Phi-4 model family and supports 128K token context length. The model underwent an enhancement process, incorporating both supervised fine-tuning and direct preference optimization to support precise instruction adherence and robust safety measures. 
+
+The Phi-4-mini-instruct model comes in the following variant with a 128K token length.
+
+
+The following models are available:
+
+* [Phi-4-mini-instruct](https://aka.ms/azureai/landing/Phi-4-mini-instruct)
+
+
+# [Phi-4](#tab/phi-4)
+
 Phi-4 is a state-of-the-art open model built upon a blend of synthetic datasets, data from filtered public domain websites, and acquired academic books and Q&A datasets. The goal of this approach was to ensure that small capable models were trained with data focused on high quality and advanced reasoning.
 
 Phi-4 underwent a rigorous enhancement and alignment process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures.
+The Phi-4 model comes in the following variant with a 16K token length.
 
-The Phi-4 models come in the following variants with a 16K tokens length.
 
-
-You can learn more about the models in their respective model card:
+The following models are available:
 
 * [Phi-4](https://aka.ms/azureai/landing/Phi-4)
 
 
+---
+
 ## Prerequisites
 
 To use Phi-4 family chat models with Azure AI Foundry, you need the following prerequisites:
@@ -1045,7 +1113,7 @@ The response is as follows:
 
 ```json
 {
-    "model_name": "Phi-4",
+    "model_name": "Phi-4-mini-instruct",
     "model_type": "chat-completions",
     "model_provider_name": "Microsoft"
 }
@@ -1071,7 +1139,7 @@ The following example shows how you can create a basic chat completions request
 ```
 
 > [!NOTE]
-> Phi-4 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> Phi-4-mini-instruct and Phi-4 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -1081,7 +1149,7 @@ The response is as follows, where you can see the model's usage statistics:
     "id": "0a1234b5de6789f01gh2i345j6789klm",
     "object": "chat.completion",
     "created": 1718726686,
-    "model": "Phi-4",
+    "model": "Phi-4-mini-instruct",
     "choices": [
         {
             "index": 0,
@@ -1138,7 +1206,7 @@ You can visualize how streaming generates content:
     "id": "23b54589eba14564ad8a2e6978775a39",
     "object": "chat.completion.chunk",
     "created": 1718726371,
-    "model": "Phi-4",
+    "model": "Phi-4-mini-instruct",
     "choices": [
         {
             "index": 0,
@@ -1161,7 +1229,7 @@ The last message in the stream has `finish_reason` set, indicating the reason fo
     "id": "23b54589eba14564ad8a2e6978775a39",
     "object": "chat.completion.chunk",
     "created": 1718726371,
-    "model": "Phi-4",
+    "model": "Phi-4-mini-instruct",
     "choices": [
         {
             "index": 0,
@@ -1212,7 +1280,7 @@ Explore other parameters that you can specify in the inference client. For a ful
     "id": "0a1234b5de6789f01gh2i345j6789klm",
     "object": "chat.completion",
     "created": 1718726686,
-    "model": "Phi-4",
+    "model": "Phi-4-mini-instruct",
     "choices": [
         {
             "index": 0,
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-4モデルに関するデプロイガイドの更新"
}
```

### Explanation
この変更は、Azure AI FoundryにおけるPhi-4ファミリーのチャットモデルに関するデプロイメントガイドの文書を更新したものです。主な更新点には、「Phi-4-mini-instruct」という新しいモデルに関する詳細の追加が含まれています。

- **モデルの説明更新**: Phi-4モデルファミリーに新たに追加された「Phi-4-mini-instruct」モデルについて、軽量でありながら高品質なデータに基づいた設計であることが強調されています。このモデルは128Kのトークンコンテキストをサポートし、指示への厳密な遵守を助けるために強化プロセスを経たことが説明されています。

- **モデルリストの拡張**: Phi-4ファミリーに含まれるモデルとして「Phi-4-mini-instruct」と「Phi-4」が紹介され、それぞれの特性や用途について具体的なリンクが提供されています。Phi-4モデルも引き続き文書に記載されており、その特性と利点が解説されています。

- **ノートの内容の明確化**: どちらのモデルもシステムメッセージ（`role="system"`）をサポートしないことに関する注意書きが強化され、ユーザーに対して注意が必要であることが再確認されています。

- **プログラムコード内の名称変更**: いくつかのコードスニペットが「Phi-4」から「Phi-4-mini-instruct」へと変更され、これによりドキュメント全体に一貫したモデル名の使用が保証されています。

この変更により、ユーザーは新しいモデルの機能とそれに伴う利用方法をより理解しやすくなり、AIモデルのデプロイメントに関する全体的な質が向上しています。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -84,7 +84,7 @@ Gretel | Not available | Gretel-Navigator
 Healthcare AI family Models | MedImageParse<BR>  MedImageInsight<BR>  CxrReportGen<BR>  Virchow<BR>  Virchow2<BR>  Prism<BR>  BiomedCLIP-PubMedBERT<BR>  microsoft-llava-med-v1.5<BR>  m42-health-llama3-med4<BR>  biomistral-biomistral-7b<BR>  microsoft-biogpt-large-pub<BR>  microsoft-biomednlp-pub<BR>  stanford-crfm-biomedlm<BR>  medicalai-clinicalbert<BR>  microsoft-biogpt<BR>  microsoft-biogpt-large<BR>  microsoft-biomednlp-pub<BR> | Not Available
 JAIS | Not available | jais-30b-chat
 Meta Llama family models | Llama-3.3-70B-Instruct<BR> Llama-3.2-3B-Instruct<BR>  Llama-3.2-1B-Instruct<BR>  Llama-3.2-1B<BR>  Llama-3.2-90B-Vision-Instruct<BR>  Llama-3.2-11B-Vision-Instruct<BR>  Llama-3.1-8B-Instruct<BR>  Llama-3.1-8B<BR>  Llama-3.1-70B-Instruct<BR>  Llama-3.1-70B<BR>  Llama-3-8B-Instruct<BR>  Llama-3-70B<BR>  Llama-3-8B<BR>  Llama-Guard-3-1B<BR>  Llama-Guard-3-8B<BR>  Llama-Guard-3-11B-Vision<BR>  Llama-2-7b<BR>  Llama-2-70b<BR>  Llama-2-7b-chat<BR>  Llama-2-13b-chat<BR>  CodeLlama-7b-hf<BR>  CodeLlama-7b-Instruct-hf<BR>  CodeLlama-34b-hf<BR>  CodeLlama-34b-Python-hf<BR>  CodeLlama-34b-Instruct-hf<BR>  CodeLlama-13b-Instruct-hf<BR>  CodeLlama-13b-Python-hf<BR>  Prompt-Guard-86M<BR>  CodeLlama-70b-hf<BR> | Llama-3.3-70B-Instruct<BR> Llama-3.2-90B-Vision-Instruct<br>  Llama-3.2-11B-Vision-Instruct<br>  Llama-3.1-8B-Instruct<br>  Llama-3.1-70B-Instruct<br>  Llama-3.1-405B-Instruct<br>  Llama-3-8B-Instruct<br>  Llama-3-70B-Instruct<br>  Llama-2-7b<br>  Llama-2-7b-chat<br>  Llama-2-70b<br>  Llama-2-70b-chat<br>  Llama-2-13b<br>  Llama-2-13b-chat<br>
-Microsoft Phi family models | Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> Phi-3-vision-128k-Instruct <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct <br> Phi-4| Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct <br> Phi-4
+Microsoft Phi family models | Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> Phi-3-vision-128k-Instruct <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct <br> Phi-4 <br> Phi-4-mini-instruct | Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct <br> Phi-4 <br> Phi-4-mini-instruct
 Mistral family models | mistralai-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x22B-Instruct-v0-1 <br> mistral-community-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x7B-v01 <br> mistralai-Mistral-7B-Instruct-v0-2 <br> mistralai-Mistral-7B-v01 <br> mistralai-Mixtral-8x7B-Instruct-v01 <br> mistralai-Mistral-7B-Instruct-v01 | Mistral-large (2402) <br> Mistral-large (2407) <br> Mistral-small <br> Ministral-3B <br> Mistral-NeMo
 Nixtla | Not available | TimeGEN-1
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phiファミリーモデルに関する情報の更新"
}
```

### Explanation
この変更は、Azure AI Studioのモデルカタログに関する概要ドキュメントに関するもので、特にMicrosoft Phiファミリーモデルのリストに「Phi-4-mini-instruct」が追加されています。この追加により、ユーザーはPhi-4ファミリーが持つモデルの幅広い選択肢を把握しやすくなります。

具体的な変更点は以下の通りです：

- **モデルの追加**: Microsoft Phiファミリーモデルのリストに「Phi-4-mini-instruct」が追加され、全体の構成が更新されました。このモデルは、Phiファミリーの一部として、以前のモデルと共に提供されます。

- **リストの整合性向上**: この変更により、ファミリー内のモデルの可用性や種類がより明確に示され、利用者が求める情報にアクセスしやすくなっています。

新たに追加された「Phi-4-mini-instruct」は、Phiファミリー内の他のモデルと同様に、ユーザーが選択できるオプションの一つとして位置付けられています。この更新は、Azureユーザーに対する情報提供の質を向上させるものです。

## articles/ai-studio/includes/region-availability-maas.md{#item-35d79c}

<details>
<summary>Diff</summary>
````diff
@@ -61,7 +61,7 @@ Llama 3.1 405B Instruct  | [Microsoft Managed countries/regions](/partner-center
 
 | Model | Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
-Phi-4                       | Not applicable | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available       |
+Phi-4 <br>  Phi-4-mini-instruct    | Not applicable | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available       |
 Phi-3.5-vision-Instruct     | Not applicable | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available       |
 Phi-3.5-MoE-Instruct     | Not applicable | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | East US 2       |
 Phi-3.5-Mini-Instruct     | Not applicable | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | East US 2  | East US 2       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの可用性情報の更新"
}
```

### Explanation
この変更は、Azure AI Studioの地域別可用性に関するドキュメントにおいて、モデルに関する情報が更新されたものです。主な変更点は、Phiファミリーに新たに追加された「Phi-4-mini-instruct」の可用性情報の統合です。

- **モデルの統合**: Phi-4とPhi-4-mini-instructが同時にリストされるようになりました。これにより、ユーザーはPhiファミリー内の両方のモデルについての情報を一目で把握できるようになります。

- **可用性の明確化**: 両モデルのデプロイメント地域とファインチューニング地域の情報は同じままですが、追加された行により、両モデルが同じ地域で利用可能であることが明示されています。

この更新は、利用者がAzureの各モデルの地域別可用性を確認しやすくし、決定をサポートするための情報を強化することを目的としています。全体として、モデルの選択肢が明確に示され、利用者にとっての利便性が向上しています。

## articles/ai-studio/media/ai-services/fine-tune-azure-ai-services.png{#item-794ba3}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの更新"
}
```

### Explanation
この変更は、Azure AI Studioの「fine-tune-azure-ai-services.png」という画像ファイルに関するもので、具体的な変更内容は記載されていないものの、ファイル自体が更新されたことを示しています。追加や削除はなく、画像の内容や形式に対する変更が行われた可能性があります。

- **画像の更新**: 画像ファイルのメタデータや内容が改訂された可能性がありますが、具体的な変更内容の詳細が示されていないため、ユーザーは新しい画像を確認する必要があります。

- **ドキュメントへの影響**: 画像はAIサービスのファインチューニングに関する情報を視覚的に伝える重要な要素です。この更新により、最新の情報や手法を反映した画像が提供されることで、ドキュメントの品質が向上することが期待されます。

全体として、この画像の更新は、Azure AI Studioの視覚的な点を最新の状態に保つためのものです。ユーザーは、最新情報に基づく支援を受けることができるようになります。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -294,7 +294,7 @@ items:
       - name: Hear and speak with chat in the playground
         href: quickstarts/hear-speak-playground.md
       - name: Custom speech fine-tuning
-        href: ../ai-services/speech-service/custom-speech-ai-foundry-portal.md?context=/azure/ai-studio/context/context
+        href: ../ai-services/speech-service/how-to-custom-speech-create-project.md?context=/azure/ai-studio/context/context
     - name:  Translator
       items:
       - name: What is Azure AI Translator?
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナビゲーションリンクの更新"
}
```

### Explanation
この変更は、Azure AI Studioの目次ファイル（toc.yml）の更新であり、特定のナビゲーションリンクが修正されました。具体的には、カスタムスピーチのファインチューニングに関連するリンクが新しいページに変更されています。

- **リンクの変更**: 以前のリンク「custom-speech-ai-foundry-portal.md」から、「how-to-custom-speech-create-project.md」へと変更されました。この変更により、ユーザーがカスタムスピーチプロジェクトの作成方法に関する最新のガイダンスにアクセスしやすくなります。

- **ユーザー体験の向上**: 新しいリンクは、ユーザーが必要とする情報に迅速にアクセスできるように設計されているため、学習や作業の効率を高めることが期待されます。

全体として、この小さな更新は大きな影響を持つ可能性があり、利用者が Azure AI Studioを使用する際のナビゲーション体験を向上させる役割を果たしています。


