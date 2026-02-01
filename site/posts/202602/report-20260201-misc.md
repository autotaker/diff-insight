---
date: '2026-02-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3e5f42f...MicrosoftDocs:8ef275a
summary: 今回のコード差分では、ファイルに軽微な更新が行われ、サービス名やSDKのメソッド名の導入、APIの仕様修正が含まれています。これにより、ユーザーは最新の仕様に基づいて開発が可能になります。新たに「Content
  Understanding」機能が追加され、テキストや画像などの統合処理ができるようになりました。また、バッチAPIによる複数ドキュメントの同時処理もサポートされます。メソッド名の変更など、既存のコードに影響を与える可能性がありますが、更新はサービス内容の理解向上とAPI利用の最適化を目的としています。このような改良により、開発者はより効率的にデータ処理やアプリケーションのスケールアップが可能になります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3e5f42f...MicrosoftDocs:8ef275a){target="_blank"}

# Highlights

今回のコード差分では、一連のファイルにおいて軽微な更新が行われています。それぞれ、サービス名の明確化、新しいSDKのメソッド名の導入、そしてAPIの仕様修正が盛り込まれています。これにより、ユーザーは最新の仕様に基づいた開発が可能となります。また、最新情報では新機能のリリースについても触れています。

## 新機能

- 「Content Understanding」という新機能がリリースされ、テキスト、画像、音声、動画の統合された処理が可能になりました。
- バッチAPIによる複数ドキュメントの同時処理のサポートが追加。

## 破壊的変更

詳細な破壊的変更については記載がありませんが、SDKのメソッド名変更などが既存のコードに影響を与える可能性があります。

## その他の更新

- サービス名やメソッド名の変更が複数のSDK資料で修正され、認識の相違を防ぐための改善がされています。
- 各種サンプルコードやAPIの説明が最新の実装に合わせて更新されました。

# Insights

この更新の主な目的は、ユーザーがドキュメントインテリジェンスサービスの最新の機能を利用しやすくすることにあります。名称やメソッド名の変更は、ユーザーに対するサービスや機能の理解を向上させ、開発者が最新のSDKを使用する中での混乱を未然に防ぐためのものです。

また、新機能として追加された「Content Understanding」やバッチAPIの導入は、より高性能かつ柔軟なデータ処理を可能にします。これにより、開発者は複雑な解析機能を手軽に利用できるようになり、エンタープライズ向けアプリケーションのスケールアップを効率的に行えるでしょう。

ドキュメントの細部にわたる変更は、API利用法の標準化と最適化を進めており、開発者がAPIを効果的に活用できる環境を整えています。このような更新は、サービスの信頼性を高めるものであり、今後の技術革新においても柔軟に対応できるサービス基盤を提供する狙いがあります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [faq.yml](#item-7a051f) | minor update | FAQの文言変更: Document Intelligence Studioの名称変更 | modified | 1 | 1 | 2 | 
| [csharp-sdk.md](#item-ee69c7) | minor update | C# SDKのメソッド名変更と引数の修正 | modified | 10 | 5 | 15 | 
| [java-sdk.md](#item-166b2e) | minor update | Java SDKのメソッドとインポートの修正 | modified | 108 | 117 | 225 | 
| [javascript-sdk.md](#item-615fcd) | minor update | JavaScript SDKのバージョン更新とコード修正 | modified | 72 | 74 | 146 | 
| [python-sdk.md](#item-83c83f) | minor update | Python SDKのバージョン更新と出力修正 | modified | 3 | 4 | 7 | 
| [rest-api.md](#item-9d952f) | minor update | REST APIのサンプルドキュメントとcURLコマンドの修正 | modified | 5 | 3 | 8 | 
| [whats-new.md](#item-1ec8d3) | minor update | ドキュメントインテリジェンスの最新情報の更新 | modified | 48 | 31 | 79 | 


# Modified Contents
## articles/ai-services/document-intelligence/faq.yml{#item-7a051f}

<details>
<summary>Diff</summary>
````diff
@@ -71,7 +71,7 @@ sections:
 
           For more information, see [overview of RAG in Document Intelligence](concept/retrieval-augmented-generation.md)
 
-  - name: Document Intelligence Studio
+  - name: Document Intelligence/Content Understanding Studio
     questions:
       - question: |
           Do I need specific permissions to access Document Intelligence Studio?
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQの文言変更: Document Intelligence Studioの名称変更"
}
```

### Explanation
この変更は、`faq.yml`ファイル内の文言を微調整するものです。具体的には「Document Intelligence Studio」という項目名が「Document Intelligence/Content Understanding Studio」に変更されました。この更新により、名称がより明確になり、ユーザーに対するサービスの内容を正確に反映しています。この変更は1行の追加と1行の削除からなり、全体として内容の理解を深めることを目的としています。変更内容の詳細は、以下のリンクで確認できます: [コードの差分](https://github.com/MicrosoftDocs/azure-ai-docs/blob/8ef275a1d20d13feed3124dd4854ecb071048674/articles%2Fai-services%2Fdocument-intelligence%2Ffaq.yml)。

## articles/ai-services/document-intelligence/quickstarts/includes/csharp-sdk.md{#item-ee69c7}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: include
-ms.date: 11/18/2025
+ms.date: 01/30/2026
 ms.author: lajanuar
 monikerRange: ">=doc-intel-3.0.0"
 ---
@@ -190,7 +190,7 @@ Extract text, selection marks, text styles, table structures, and bounding regio
 >
 > * For this example, you'll need a **document file from a URI**. You can use our [sample document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf) for this quickstart.
 > * We've added the file URI value to the `Uri fileUri` variable at the top of the script.
-> * To extract the layout from a given file at a URI, use the `StartAnalyzeDocumentFromUri` method and pass `prebuilt-layout` as the model ID. The returned value is an `AnalyzeResult` object containing data from the submitted document.
+> * To extract the layout from a given file at a URI, use the `AnalyzeDocumentAsync` method and pass `prebuilt-layout` as the model ID. The returned value is an `AnalyzeResult` object containing data from the submitted document.
 
 :::moniker range="doc-intel-4.0.0"
 
@@ -625,7 +625,7 @@ Analyze and extract common fields from specific document types using a prebuilt
 >
 > * Analyze an invoice using the prebuilt-invoice model. You can use our [sample invoice document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf) for this quickstart.
 > * We've added the file URI value to the `Uri invoiceUri` variable at the top of the Program.cs file.
-> * To analyze a given file at a URI, use the `StartAnalyzeDocumentFromUri` method and pass `prebuilt-invoice` as the model ID. The returned value is an `AnalyzeResult` object containing data from the submitted document.
+> * To analyze a given file at a URI, use the `AnalyzeDocumentAsync` method and pass `prebuilt-invoice` as the model ID. The returned value is an `AnalyzeResult` object containing data from the submitted document.
 > * For simplicity, all the key-value pairs that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../prebuilt/invoice.md#field-extraction) concept page.
 
 :::moniker range="doc-intel-4.0.0"
@@ -644,9 +644,14 @@ AzureKeyCredential credential = new AzureKeyCredential(key);
 DocumentIntelligenceClient client = new DocumentIntelligenceClient(new Uri(endpoint), credential);
 
 //sample invoice document
-Uri uriSource = new Uri("https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf");
+Uri invoiceUri = new Uri("https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf");
 
-Operation<AnalyzeResult> operation = await client.AnalyzeDocumentAsync(WaitUntil.Completed, "prebuilt-invoice", uriSource);
+AnalyzeDocumentContent content = new AnalyzeDocumentContent()
+{
+    UrlSource = invoiceUri
+};
+
+Operation<AnalyzeResult> operation = await client.AnalyzeDocumentAsync(WaitUntil.Completed, "prebuilt-invoice", content);
 
 AnalyzeResult result = operation.Value;
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDKのメソッド名変更と引数の修正"
}
```

### Explanation
この変更は、`csharp-sdk.md`ファイルにおけるいくつかのメソッド名や引数の修正に関するものです。具体的には、`StartAnalyzeDocumentFromUri`メソッドが`AnalyzeDocumentAsync`メソッドに変更されており、引数として渡す内容も更新されています。この修正は、より最新のSDKに対応するためのものであり、正しいメソッドを使用してドキュメントを解析する手順を明確に示しています。

この更新では、合計10行が追加され、5行が削除されたことで、全体にわたる15行の変更が行われています。具体的な修正点には、引数の型や変数名の変更が含まれており、これはコードの機能を向上させ、ユーザーがSDKを利用する際の体験をよりスムーズにすることを目的としています。変更内容の詳細は、以下のリンクで確認できます: [コードの差分](https://github.com/MicrosoftDocs/azure-ai-docs/blob/8ef275a1d20d13feed3124dd4854ecb071048674/articles%2Fai-services%2Fdocument-intelligence%2Fquickstarts%2Fincludes%2Fcsharp-sdk.md)。

## articles/ai-services/document-intelligence/quickstarts/includes/java-sdk.md{#item-166b2e}

<details>
<summary>Diff</summary>
````diff
@@ -255,7 +255,7 @@ Extract text, selection marks, text styles, table structures, and bounding regio
 > [!div class="checklist"]
 >
 > * For this example, you'll need a **document file at a URI**. You can use our [sample document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf) for this quickstart.
-> * To analyze a given file at a URI, you'll use the `beginAnalyzeDocumentFromUrl` method and pass `prebuilt-layout` as the model Id. The returned value is an `AnalyzeResult` object containing data about the submitted document.
+> * To analyze a given file at a URI, you'll use the `beginAnalyzeDocument` method and pass `prebuilt-layout` as the model Id. The returned value is an `AnalyzeResult` object containing data about the submitted document.
 > * We've added the file URI value to the `documentUrl` variable in the main method.
 
 :::moniker range="doc-intel-4.0.0"
@@ -630,16 +630,17 @@ Analyze and extract common fields from specific document types using a prebuilt
 
 ```java
 
-import com.azure.ai.documentintelligence.models.AnalyzeDocumentRequest;
+import com.azure.ai.documentintelligence.DocumentIntelligenceClient;
+import com.azure.ai.documentintelligence.DocumentIntelligenceClientBuilder;
+import com.azure.ai.documentintelligence.models.AnalyzeDocumentOptions;
+import com.azure.ai.documentintelligence.models.AnalyzeOperationDetails;
 import com.azure.ai.documentintelligence.models.AnalyzeResult;
-import com.azure.ai.documentintelligence.models.AnalyzeResultOperation;
-import com.azure.ai.documentintelligence.models.Document;
+import com.azure.ai.documentintelligence.models.AnalyzedDocument;
 import com.azure.ai.documentintelligence.models.DocumentField;
 import com.azure.ai.documentintelligence.models.DocumentFieldType;
 import com.azure.core.credential.AzureKeyCredential;
 import com.azure.core.util.polling.SyncPoller;
 
-import java.io.IOException;
 import java.time.LocalDate;
 import java.util.List;
 import java.util.Map;
@@ -652,140 +653,130 @@ public class DocIntelligence {
 
   public static void main(String[] args) {
 
+    // create your `DocumentIntelligenceClient` instance and `AzureKeyCredential` variable
+    DocumentIntelligenceClient client = new DocumentIntelligenceClientBuilder()
+      .credential(new AzureKeyCredential(key))
+      .endpoint(endpoint)
+      .buildClient();
+
     // sample document
     String modelId = "prebuilt-invoice";
     String invoiceUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf";
 
-    public static void main(final String[] args) throws IOException {
-
-      // Instantiate a client that will be used to call the service.
-      DocumentIntelligenceClient client = new DocumentIntelligenceClientBuilder()
-        .credential(new AzureKeyCredential(key))
-        .endpoint(endpoint)
-        .buildClient();
-
-      SyncPoller<AnalyzeResultOperation, AnalyzeResultOperation > analyzeInvoicesPoller =
-        client.beginAnalyzeDocument(modelId, 
-            null,
-            null,
-            null,
-            null,
-            null,
-            null,
-            new AnalyzeDocumentRequest().setUrlSource(invoiceUrl));
-
-      AnalyzeResult analyzeInvoiceResult = analyzeInvoicesPoller.getFinalResult().getAnalyzeResult();
-
-      for (int i = 0; i < analyzeInvoiceResult.getDocuments().size(); i++) {
-        Document analyzedInvoice = analyzeInvoiceResult.getDocuments().get(i);
-        Map < String, DocumentField > invoiceFields = analyzedInvoice.getFields();
-        System.out.printf("----------- Analyzing invoice  %d -----------%n", i);
-        DocumentField vendorNameField = invoiceFields.get("VendorName");
-        if (vendorNameField != null) {
-          if (DocumentFieldType.STRING == vendorNameField.getType()) {
-            String merchantName = vendorNameField.getValueString();
-            System.out.printf("Vendor Name: %s, confidence: %.2f%n",
-              merchantName, vendorNameField.getConfidence());
-          }
+    SyncPoller<AnalyzeOperationDetails, AnalyzeResult> analyzeInvoicesPoller =
+      client.beginAnalyzeDocument(modelId, new AnalyzeDocumentOptions(invoiceUrl));
+
+    AnalyzeResult analyzeInvoiceResult = analyzeInvoicesPoller.getFinalResult();
+
+    for (int i = 0; i < analyzeInvoiceResult.getDocuments().size(); i++) {
+      AnalyzedDocument analyzedInvoice = analyzeInvoiceResult.getDocuments().get(i);
+      Map<String, DocumentField> invoiceFields = analyzedInvoice.getFields();
+      System.out.printf("----------- Analyzing invoice  %d -----------%n", i);
+      DocumentField vendorNameField = invoiceFields.get("VendorName");
+      if (vendorNameField != null) {
+        if (DocumentFieldType.STRING == vendorNameField.getType()) {
+          String merchantName = vendorNameField.getValueAsString();
+          System.out.printf("Vendor Name: %s, confidence: %.2f%n",
+            merchantName, vendorNameField.getConfidence());
         }
+      }
 
-        DocumentField vendorAddressField = invoiceFields.get("VendorAddress");
-        if (vendorAddressField != null) {
-          if (DocumentFieldType.STRING == vendorAddressField.getType()) {
-            String merchantAddress = vendorAddressField.getValueString();
-            System.out.printf("Vendor address: %s, confidence: %.2f%n",
-              merchantAddress, vendorAddressField.getConfidence());
-          }
+      DocumentField vendorAddressField = invoiceFields.get("VendorAddress");
+      if (vendorAddressField != null) {
+        if (DocumentFieldType.STRING == vendorAddressField.getType()) {
+          String merchantAddress = vendorAddressField.getValueAsString();
+          System.out.printf("Vendor address: %s, confidence: %.2f%n",
+            merchantAddress, vendorAddressField.getConfidence());
         }
+      }
 
-        DocumentField customerNameField = invoiceFields.get("CustomerName");
-        if (customerNameField != null) {
-          if (DocumentFieldType.STRING == customerNameField.getType()) {
-            String merchantAddress = customerNameField.getValueString();
-            System.out.printf("Customer Name: %s, confidence: %.2f%n",
-              merchantAddress, customerNameField.getConfidence());
-          }
+      DocumentField customerNameField = invoiceFields.get("CustomerName");
+      if (customerNameField != null) {
+        if (DocumentFieldType.STRING == customerNameField.getType()) {
+          String merchantAddress = customerNameField.getValueAsString();
+          System.out.printf("Customer Name: %s, confidence: %.2f%n",
+            merchantAddress, customerNameField.getConfidence());
         }
+      }
 
-        DocumentField customerAddressRecipientField = invoiceFields.get("CustomerAddressRecipient");
-        if (customerAddressRecipientField != null) {
-          if (DocumentFieldType.STRING == customerAddressRecipientField.getType()) {
-            String customerAddr = customerAddressRecipientField.getValueString();
-            System.out.printf("Customer Address Recipient: %s, confidence: %.2f%n",
-              customerAddr, customerAddressRecipientField.getConfidence());
-          }
+      DocumentField customerAddressRecipientField = invoiceFields.get("CustomerAddressRecipient");
+      if (customerAddressRecipientField != null) {
+        if (DocumentFieldType.STRING == customerAddressRecipientField.getType()) {
+          String customerAddr = customerAddressRecipientField.getValueAsString();
+          System.out.printf("Customer Address Recipient: %s, confidence: %.2f%n",
+            customerAddr, customerAddressRecipientField.getConfidence());
         }
+      }
 
-        DocumentField invoiceIdField = invoiceFields.get("InvoiceId");
-        if (invoiceIdField != null) {
-          if (DocumentFieldType.STRING == invoiceIdField.getType()) {
-            String invoiceId = invoiceIdField.getValueString();
-            System.out.printf("Invoice ID: %s, confidence: %.2f%n",
-              invoiceId, invoiceIdField.getConfidence());
-          }
+      DocumentField invoiceIdField = invoiceFields.get("InvoiceId");
+      if (invoiceIdField != null) {
+        if (DocumentFieldType.STRING == invoiceIdField.getType()) {
+          String invoiceId = invoiceIdField.getValueAsString();
+          System.out.printf("Invoice ID: %s, confidence: %.2f%n",
+            invoiceId, invoiceIdField.getConfidence());
         }
+      }
 
-        DocumentField invoiceDateField = invoiceFields.get("InvoiceDate");
-        if (customerNameField != null) {
-          if (DocumentFieldType.DATE == invoiceDateField.getType()) {
-            LocalDate invoiceDate = invoiceDateField.getValueDate();
-            System.out.printf("Invoice Date: %s, confidence: %.2f%n",
-              invoiceDate, invoiceDateField.getConfidence());
-          }
+      DocumentField invoiceDateField = invoiceFields.get("InvoiceDate");
+      if (invoiceDateField != null) {
+        if (DocumentFieldType.DATE == invoiceDateField.getType()) {
+          LocalDate invoiceDate = invoiceDateField.getValueAsDate();
+          System.out.printf("Invoice Date: %s, confidence: %.2f%n",
+            invoiceDate, invoiceDateField.getConfidence());
         }
+      }
 
-        DocumentField invoiceTotalField = invoiceFields.get("InvoiceTotal");
-        if (customerAddressRecipientField != null) {
-          if (DocumentFieldType.NUMBER == invoiceTotalField.getType()) {
-            Double invoiceTotal = invoiceTotalField.getValueNumber();
-            System.out.printf("Invoice Total: %.2f, confidence: %.2f%n",
-              invoiceTotal, invoiceTotalField.getConfidence());
-          }
+      DocumentField invoiceTotalField = invoiceFields.get("InvoiceTotal");
+      if (invoiceTotalField != null) {
+        if (DocumentFieldType.DOUBLE == invoiceTotalField.getType()) {
+          Double invoiceTotal = invoiceTotalField.getValueAsDouble();
+          System.out.printf("Invoice Total: %.2f, confidence: %.2f%n",
+            invoiceTotal, invoiceTotalField.getConfidence());
         }
+      }
 
-        DocumentField invoiceItemsField = invoiceFields.get("Items");
-        if (invoiceItemsField != null) {
-          System.out.printf("Invoice Items: %n");
-          if (DocumentFieldType.ARRAY == invoiceItemsField.getType()) {
-            List < DocumentField > invoiceItems = invoiceItemsField.getValueArray();
-            invoiceItems.stream()
-              .filter(invoiceItem -> DocumentFieldType.OBJECT == invoiceItem.getType())
-              .map(documentField -> documentField.getValueObject())
-              .forEach(documentFieldMap -> documentFieldMap.forEach((key, documentField) -> {
-
-                // See a full list of fields found on an invoice here:
-                // https://aka.ms/documentintelligence/invoicefields
-
-                if ("Description".equals(key)) {
-                  if (DocumentFieldType.STRING == documentField.getType()) {
-                    String name = documentField.getValueString();
-                    System.out.printf("Description: %s, confidence: %.2fs%n",
-                      name, documentField.getConfidence());
-                  }
+      DocumentField invoiceItemsField = invoiceFields.get("Items");
+      if (invoiceItemsField != null) {
+        System.out.printf("Invoice Items: %n");
+        if (DocumentFieldType.LIST == invoiceItemsField.getType()) {
+          List<DocumentField> invoiceItems = invoiceItemsField.getValueAsList();
+          invoiceItems.stream()
+            .filter(invoiceItem -> DocumentFieldType.MAP == invoiceItem.getType())
+            .map(documentField -> documentField.getValueAsMap())
+            .forEach(documentFieldMap -> documentFieldMap.forEach((key, documentField) -> {
+
+              // See a full list of fields found on an invoice here:
+              // https://aka.ms/documentintelligence/invoicefields
+
+              if ("Description".equals(key)) {
+                if (DocumentFieldType.STRING == documentField.getType()) {
+                  String name = documentField.getValueAsString();
+                  System.out.printf("Description: %s, confidence: %.2fs%n",
+                    name, documentField.getConfidence());
                 }
-                if ("Quantity".equals(key)) {
-                  if (DocumentFieldType.NUMBER == documentField.getType()) {
-                    Double quantity = documentField.getValueNumber();
-                    System.out.printf("Quantity: %f, confidence: %.2f%n",
-                      quantity, documentField.getConfidence());
-                  }
+              }
+              if ("Quantity".equals(key)) {
+                if (DocumentFieldType.DOUBLE == documentField.getType()) {
+                  Double quantity = documentField.getValueAsDouble();
+                  System.out.printf("Quantity: %f, confidence: %.2f%n",
+                    quantity, documentField.getConfidence());
                 }
-                if ("UnitPrice".equals(key)) {
-                  if (DocumentFieldType.NUMBER == documentField.getType()) {
-                    Double unitPrice = documentField.getValueNumber();
-                    System.out.printf("Unit Price: %f, confidence: %.2f%n",
-                      unitPrice, documentField.getConfidence());
-                  }
+              }
+              if ("UnitPrice".equals(key)) {
+                if (DocumentFieldType.DOUBLE == documentField.getType()) {
+                  Double unitPrice = documentField.getValueAsDouble();
+                  System.out.printf("Unit Price: %f, confidence: %.2f%n",
+                    unitPrice, documentField.getConfidence());
                 }
-                if ("ProductCode".equals(key)) {
-                  if (DocumentFieldType.NUMBER == documentField.getType()) {
-                    Double productCode = documentField.getValueNumber();
-                    System.out.printf("Product Code: %f, confidence: %.2f%n",
-                      productCode, documentField.getConfidence());
-                  }
+              }
+              if ("ProductCode".equals(key)) {
+                if (DocumentFieldType.DOUBLE == documentField.getType()) {
+                  Double productCode = documentField.getValueAsDouble();
+                  System.out.printf("Product Code: %f, confidence: %.2f%n",
+                    productCode, documentField.getConfidence());
                 }
-              }));
-          }
+              }
+            }));
         }
       }
     }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java SDKのメソッドとインポートの修正"
}
```

### Explanation
この変更は、`java-sdk.md`ファイルにおけるメソッド名やインポート文の修正を行うもので、Java SDKに関連するコードサンプルのために内容が大幅に更新されています。新しいメソッド名として `beginAnalyzeDocument` が導入され、過去の `beginAnalyzeDocumentFromUrl` メソッドは削除されました。これにより、APIの使用法が現行の仕様に合わせて改善されています。

さらに、インポート文や変数の型も変更されており、多くの部分で変数名が一貫性を持つ形に整理されています。また、解析結果の取得方法も刷新され、新しいAPIの利用法に従って改善されています。

この変更によって、全体で108行が追加され、117行が削除され、合計で225行の変更が行われました。これにより、Java SDKを使用する開発者が最新の機能を正確に活用できるようになり、所定のデータをより適切に管理することができるようになります。変更内容の詳細は、以下のリンクで確認できます: [コードの差分](https://github.com/MicrosoftDocs/azure-ai-docs/blob/8ef275a1d20d13feed3124dd4854ecb071048674/articles%2Fai-services%2Fdocument-intelligence%2Fquickstarts%2Fincludes%2Fjava-sdk.md)。

## articles/ai-services/document-intelligence/quickstarts/includes/javascript-sdk.md{#item-615fcd}

<details>
<summary>Diff</summary>
````diff
@@ -6,13 +6,13 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: include
-ms.date: 11/18/2025
+ms.date: 01/30/2026
 ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD025 -->
 
 :::moniker range="doc-intel-4.0.0"
-[Client library](/javascript/api/overview/azure/ai-document-intelligence-rest-readme?view=azure-node-latest&preserve-view=true) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package (npm)]( https://www.npmjs.com/package/@azure-rest/ai-document-intelligence/v/1.0.0) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest/samples/v1/javascript) |[Supported REST API version](../../sdk-overview-v4-0.md)
+[Client library](/javascript/api/overview/azure/ai-document-intelligence-rest-readme?view=azure-node-latest&preserve-view=true) | [REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package (npm)](https://www.npmjs.com/package/@azure-rest/ai-document-intelligence/v/1.1.0) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest/samples/v1/javascript) |[Supported REST API version](../../sdk-overview-v4-0.md)
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
@@ -73,7 +73,7 @@ In this quickstart, use the following features to analyze and extract data and v
  4. Install the `ai-document-intelligence` client library and `azure/identity` npm packages:
 
     ```console
-    npm i @azure-rest/ai-document-intelligence@1.0.0 @azure/core-auth
+    npm i @azure-rest/ai-document-intelligence@1.1.0
     ```
 
     Your app's `package.json` file is updated with the dependencies.
@@ -144,56 +144,64 @@ Extract text, selection marks, text styles, table structures, and bounding regio
 :::moniker range="doc-intel-4.0.0"
 
 ```javascript
-    const DocumentIntelligence = require("@azure-rest/ai-document-intelligence").default,
-  { getLongRunningPoller, isUnexpected } = require("@azure-rest/ai-document-intelligence");
-
-  const { AzureKeyCredential } = require("@azure/core-auth");
-
-    // set `<your-key>` and `<your-endpoint>` variables with the values from the Azure portal.
-    const key = "<your-key>";
-    const endpoint = "<your-endpoint>";
+const DocumentIntelligence = require("@azure-rest/ai-document-intelligence").default,
+{ getLongRunningPoller, isUnexpected } = require("@azure-rest/ai-document-intelligence");
 
-    // sample document
-    const formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"
+// set `<your-key>` and `<your-endpoint>` variables with the values from the Azure portal.
+const key = "<your-key>";
+const endpoint = "<your-endpoint>";
 
-   async function main() {
-    const client = DocumentIntelligence(endpoint, new AzureKeyCredential(key));
+// sample document
+const formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"
 
+async function main() {
+  const client = DocumentIntelligence(endpoint, { key });
 
-    const initialResponse = await client
-      .path("/documentModels/{modelId}:analyze", "prebuilt-layout")
-      .post({
-        contentType: "application/json",
-        body: {
-          urlSource: formUrl
-        },
-       });
+  const initialResponse = await client
+    .path("/documentModels/{modelId}:analyze", "prebuilt-layout")
+    .post({
+      contentType: "application/json",
+      body: {
+        urlSource: formUrl
+      },
+    });
 
-       if (isUnexpected(initialResponse)) {
-       throw initialResponse.body.error;
-     }
+  if (isUnexpected(initialResponse)) {
+    throw initialResponse.body.error;
+  }
 
-    const poller = await getLongRunningPoller(client, initialResponse);
-    const analyzeResult = (await poller.pollUntilDone()).body.analyzeResult;
+  const poller = getLongRunningPoller(client, initialResponse);
+  const analyzeResult = (await poller.pollUntilDone()).body.analyzeResult;
 
-    const documents = analyzeResult?.documents;
+  const pages = analyzeResult?.pages;
+  const tables = analyzeResult?.tables;
 
-    const document = documents && documents[0];
-    if (!document) {
-    throw new Error("Expected at least one document in the result.");
+  if (pages && pages.length > 0) {
+    console.log("Pages:");
+    for (const page of pages) {
+      console.log("- Page", page.pageNumber, `(unit: ${page.unit})`);
+      console.log(`  ${page.width}x${page.height}`);
+      console.log(`  ${page.lines?.length || 0} lines, ${page.words?.length || 0} words`);
     }
+  } else {
+    console.log("No pages were extracted from the document.");
+  }
 
-    console.log(
-    "Extracted document:",
-    document.docType,
-    `(confidence: ${document.confidence || "<undefined>"})`,
-    );
-    console.log("Fields:", document.fields);
+  if (tables && tables.length > 0) {
+    console.log("Tables:");
+    for (const table of tables) {
+      console.log(
+        `- Extracted table: ${table.columnCount} columns, ${table.rowCount} rows (${table.cells.length} cells)`
+      );
+    }
+  } else {
+    console.log("No tables were extracted from the document.");
+  }
 }
 
 main().catch((error) => {
-    console.error("An error occurred:", error);
-    process.exit(1);
+  console.error("An error occurred:", error);
+  process.exit(1);
 });
 
 ```
@@ -313,63 +321,53 @@ In this example, we analyze an invoice using the **prebuilt-invoice** model.
 :::moniker range="doc-intel-4.0.0"
 
 ```javascript
-
 const DocumentIntelligence = require("@azure-rest/ai-document-intelligence").default,
-  { getLongRunningPoller, isUnexpected } = require("@azure-rest/ai-document-intelligence");
-
-const { AzureKeyCredential } = require("@azure/core-auth");
+{ getLongRunningPoller, isUnexpected } = require("@azure-rest/ai-document-intelligence");
 
-    // set `<your-key>` and `<your-endpoint>` variables with the values from the Azure portal.
-    const key = "<your-key>";
-    const endpoint = "<your-endpoint>";
+// set `<your-key>` and `<your-endpoint>` variables with the values from the Azure portal.
+const key = "<your-key>";
+const endpoint = "<your-endpoint>";
 
-    // sample document
-    const invoiceUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf"
+// sample document
+const invoiceUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf"
 
 async function main() {
+  const client = DocumentIntelligence(endpoint, { key });
 
-    const client = DocumentIntelligence(endpoint, new AzureKeyCredential(key));
-
-    const initialResponse = await client
+  const initialResponse = await client
     .path("/documentModels/{modelId}:analyze", "prebuilt-invoice")
     .post({
       contentType: "application/json",
       body: {
-        // The Document Intelligence service will access the URL to the invoice image and extract data from it
         urlSource: invoiceUrl,
       },
     });
 
-    if (isUnexpected(initialResponse)) {
-       throw initialResponse.body.error;
-     }
-
-    const poller = await getLongRunningPoller(client, initialResponse);
+  if (isUnexpected(initialResponse)) {
+    throw initialResponse.body.error;
+  }
 
-    poller.onProgress((state) => console.log("Operation:", state.result, state.status));
-    const analyzeResult = (await poller.pollUntilDone()).body.analyzeResult;
+  const poller = getLongRunningPoller(client, initialResponse);
+  const analyzeResult = (await poller.pollUntilDone()).body.analyzeResult;
 
-    const documents = analyzeResult?.documents;
+  const documents = analyzeResult?.documents;
 
-    const result = documents && documents[0];
-    if (result) {
-      console.log(result.fields);
-    } else {
-      throw new Error("Expected at least one invoice in the result.");
-    }
+  const invoice = documents && documents[0];
+  if (!invoice) {
+    throw new Error("Expected at least one invoice in the result.");
+  }
 
-console.log(
+  console.log(
     "Extracted invoice:",
-    document.docType,
-    `(confidence: ${document.confidence || "<undefined>"})`,
+    invoice.docType,
+    `(confidence: ${invoice.confidence || "<undefined>"})`
   );
-  console.log("Fields:", document.fields);
+  console.log("Fields:", invoice.fields);
 }
 
-
 main().catch((error) => {
-    console.error("An error occurred:", error);
-    process.exit(1);
+  console.error("An error occurred:", error);
+  process.exit(1);
 });
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKのバージョン更新とコード修正"
}
```

### Explanation
この変更は、`javascript-sdk.md`ファイルにおいてJavaScript SDKのバージョンを1.0.0から1.1.0に更新し、いくつかのコードの修正を行うものです。全体で72行が追加され、74行が削除され、合計146行の更新が行われています。

コード内では、`AzureKeyCredential`が削除され、新しい認証方式が`{ key }`として統合されています。また、初期レスポンスの処理や出力内容も改善され、ページやテーブルの情報を出力する部分が追加されています。これにより、ユーザーはドキュメントから抽出したデータをより詳しく確認できるようになります。

更新内容には、関数の呼び出しやエラーハンドリングが含まれており、特にSDKの使用に関して、より直感的で効率的なコードに仕上がっています。変更に関する詳細な情報は、以下のリンクから確認可能です: [コードの差分](https://github.com/MicrosoftDocs/azure-ai-docs/blob/8ef275a1d20d13feed3124dd4854ecb071048674/articles%2Fai-services%2Fdocument-intelligence%2Fquickstarts%2Fincludes%2Fjavascript-sdk.md)。

## articles/ai-services/document-intelligence/quickstarts/includes/python-sdk.md{#item-83c83f}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.author: lajanuar
 <!-- markdownlint-disable MD025 -->
 
 :::moniker range="doc-intel-4.0.0"
-[Client library](/python/api/overview/azure/ai-documentintelligence-readme?view=azure-python-preview&preserve-view=true) |[REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package (PyPi)](https://pypi.org/project/azure-ai-documentintelligence/1.0.0b4/) | [Samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/documentintelligence/azure-ai-documentintelligence/samples) | [Supported REST API version](../../sdk-overview-v4-0.md#supported-programming-languages)
+[Client library](/python/api/overview/azure/ai-documentintelligence-readme?view=azure-python&preserve-view=true) |[REST API reference](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) | [Package (PyPi)](https://pypi.org/project/azure-ai-documentintelligence/1.0.2/) | [Samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/documentintelligence/azure-ai-documentintelligence/samples) | [Supported REST API version](../../sdk-overview-v4-0.md#supported-programming-languages)
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
@@ -55,7 +55,7 @@ Open a terminal window in your local environment and install the Azure Document
 :::moniker range="doc-intel-4.0.0"
 
 ```console
-pip install azure-ai-documentintelligence==1.0.0b4
+pip install azure-ai-documentintelligence==1.0.2
 
 ```
 
@@ -751,8 +751,7 @@ def analyze_invoice():
                     f"Remittance Address Recipient: {remittance_address_recipient.get('content')} has confidence: {remittance_address_recipient.get('confidence')}"
                 )
 
-
-          print("----------------------------------------")
+            print("----------------------------------------")
 
 
 if __name__ == "__main__":
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python SDKのバージョン更新と出力修正"
}
```

### Explanation
この変更は、`python-sdk.md`ファイルにおいて、Python SDKのバージョンを1.0.0b4から1.0.2に更新し、いくつかの出力メッセージの修正を行うもので、全体で3行が追加され、4行が削除され、合計7行の変更が行われています。

具体的には、クライアントライブラリのリンク先が新しいバージョンに更新され、Pythonパッケージのインストール手順も最新のバージョンに対応するように変更されています。これにより、開発者はより新しい機能やバグ修正を持つSDKを使用できるようになります。また、出力部分においては、余分な行を削除する形でコードが整えられています。

この変更によって、ユーザーは最新のSDKを簡単にインストールし、解析結果をより明確に表示できるようになるため、ドキュメントの利用価値が向上します。詳細な変更内容については、以下のリンクで確認できます: [コードの差分](https://github.com/MicrosoftDocs/azure-ai-docs/blob/8ef275a1d20d13feed3124dd4854ecb071048674/articles%2Fai-services%2Fdocument-intelligence%2Fquickstarts%2Fincludes%2Fpython-sdk.md)。

## articles/ai-services/document-intelligence/quickstarts/includes/rest-api.md{#item-9d952f}

<details>
<summary>Diff</summary>
````diff
@@ -79,14 +79,15 @@ Before you run the cURL command, make the following changes to the [post request
 | **Invoice**  | `prebuilt-invoice` | `https://github.com/Azure-Samples/cognitive-services-REST-api-samples/raw/master/curl/form-recognizer/rest-api/invoice.pdf` |
 | **Receipt**  | `prebuilt-receipt` | `https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/receipt.png` |
 | **ID document**  | `prebuilt-idDocument` | `https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/identity_documents.png` |
+
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
 
 **Sample documents**
 
 | **Feature**   | **{modelID}**   | **{your-document-url}** |
-| --- | --- |--|
+| --- | --- | --- |
 | **General Document** | `prebuilt-document` | `https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf` |
 | **Read** | `prebuilt-read` | `https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/read.png` |
 | **Layout** | `prebuilt-layout` | `https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/layout.png` |
@@ -96,6 +97,7 @@ Before you run the cURL command, make the following changes to the [post request
 | **Receipt**  | `prebuilt-receipt` | `https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/receipt.png` |
 | **ID document**  | `prebuilt-idDocument` | `https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/identity_documents.png` |
 | **Business card**  | `prebuilt-businessCard` | `https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/de5e0d8982ab754823c54de47a47e8e499351523/curl/form-recognizer/rest-api/business_card.jpg` |
+
 :::moniker-end
 
 > [!IMPORTANT]
@@ -106,7 +108,7 @@ Before you run the cURL command, make the following changes to the [post request
 :::moniker range="doc-intel-4.0.0"
 
 ```bash
-curl -v -i POST "{endpoint}/documentintelligence/documentModels/{modelId}:analyze?api-version=2024-11-30" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: {key}" --data-ascii "{'urlSource': '{your-document-url}'}"
+curl -v -i -X POST "{endpoint}/documentintelligence/documentModels/{modelId}:analyze?api-version=2024-11-30" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: {key}" --data-ascii "{'urlSource': '{your-document-url}'}"
 ```
 
 :::moniker-end
@@ -137,7 +139,7 @@ You receive a `202 (Success)` response that includes a read-only **Operation-Loc
 
 :::moniker range="doc-intel-4.0.0"
 
-After you call the [`Analyze document`](/rest/api/aiservices/operation-groups) API, call the [**Get analyze result**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)&preserve-view=true&tabs=HTTP) API to get the status of the operation and the extracted data. Before you run the command, make these changes:
+After you call the [`Analyze document`](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) API, call the [**Get analyze result**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) API to get the status of the operation and the extracted data. Before you run the command, make these changes:
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIのサンプルドキュメントとcURLコマンドの修正"
}
```

### Explanation
この変更は、`rest-api.md`ファイルにおいて、REST APIのサンプルドキュメントやcURLコマンドの記述に関する数点のマイナーな更新を行うものです。全体で5行が追加され、3行が削除され、合計8行の変更が行われています。

具体的には、サンプルドキュメントに関する表のフォーマットが改良され、`{your-document-url}`の定義部分がより一貫性のある形式に整えられています。また、cURLコマンドの説明には、HTTPメソッドを明示的に指定するオプション（`-X POST`）が追加され、より正確なリクエスト形式が提示されるようになっています。

さらに、APIリファレンスに関する説明文もわずかに修正されました。これにより、利用者がAPIを理解しやすくなり、具体的なサンプルをもとに簡単にリクエストを実行できるように配慮されています。変更に関する詳細は、以下のリンクで確認できます: [コードの差分](https://github.com/MicrosoftDocs/azure-ai-docs/blob/8ef275a1d20d13feed3124dd4854ecb071048674/articles%2Fai-services%2Fdocument-intelligence%2Fquickstarts%2Fincludes%2Frest-api.md)。

## articles/ai-services/document-intelligence/whats-new.md{#item-1ec8d3}

<details>
<summary>Diff</summary>
````diff
@@ -27,47 +27,64 @@ Document Intelligence service is updated on an ongoing basis. Bookmark this page
 > [!IMPORTANT]
 > Preview API versions are retired once the GA API is released. The 2023-02-28-preview API version is retiring. If you're still using the preview API or the associated SDK versions, update your code to target the latest API version `2024-11-30 (GA)`. </br>
 
+## Latest updates
+
+**Content Understanding: The Next Step Forward for Document Intelligence**
+</br>
+In November 2025, the GA version of **Content Understanding** was released (**2025-11-01** API version). Content Understanding is an evolution of Document Intelligence that expands multimodal processing capabilities to support text, images, audio, and video content types.
+
+Key features include:
+
+* **Multimodal content analysis**. Process and extract insights from text, images, audio, and video within a unified API framework.
+* **Enhanced AI integration**. Seamlessly integrate with Azure AI services for intelligent content processing and decision-making workflows.
+* **Flexible deployment options**. Build applications, automate document workflows, or enable AI-driven analytics with scalable cloud infrastructure.
+* **Unified content extraction**. Utilize a single service to handle diverse content types, reducing complexity and improving operational efficiency.
+
 ## June 2025
+
 **Document Intelligence v4.0 Read container is now available!**
-<br>
+</br>
 This container image includes highly requested Read features like searchable PDF! For more information, *see:*
+
 * [Install and run containers](containers/install-run.md?view=doc-intel-4.0.0&preserve-view=true)
 * [Container image tags](containers/image-tags.md?view=doc-intel-4.0.0&preserve-view=true)
 
 ## April 2025
+
 **Document Intelligence v4.0 Layout container is now available!**
-<br>
+</br>
 For more information, *see:*
+
 * [Install and run containers](containers/install-run.md?view=doc-intel-4.0.0&preserve-view=true)
 * [Container image tags](containers/image-tags.md?view=doc-intel-4.0.0&preserve-view=true)
 
 ## December 2024
 
-**Document Intelligence v4.0 programming language SDKs are now generally available (GA)**! <br><br>The latest client libraries default to the [**2024-11-30 REST API (GA)**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) version of the service.<br><br>
+**Document Intelligence v4.0 programming language SDKs are now generally available (GA)**! </br></br>The latest client libraries default to the [**2024-11-30 REST API (GA)**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) version of the service.</br></br>
 For more information, *see* client libraries for the following supported programming languages:
 
-* [🆕 .NET (C#)](versioning/changelog-release-history.md?view=doc-intel-4.0.0&tabs=csharp&preserve-view=true)
+* [.NET (C#)](versioning/changelog-release-history.md?view=doc-intel-4.0.0&tabs=csharp&preserve-view=true)
 
-* [🆕 Java](versioning/changelog-release-history.md?view=doc-intel-4.0.0&tabs=java&preserve-view=true)
+* [Java](versioning/changelog-release-history.md?view=doc-intel-4.0.0&tabs=java&preserve-view=true)
 
-* [🆕 JavaScript](versioning/changelog-release-history.md?view=doc-intel-4.0.0&tabs=javascript&preserve-view=true)
+* [JavaScript](versioning/changelog-release-history.md?view=doc-intel-4.0.0&tabs=javascript&preserve-view=true)
 
-* [🆕 Python](versioning/changelog-release-history.md?view=doc-intel-4.0.0&tabs=python&preserve-view=true)
+* [Python](versioning/changelog-release-history.md?view=doc-intel-4.0.0&tabs=python&preserve-view=true)
 
 ## November 2024
 
 **Document Intelligence REST API v4.0: [**2024-11-30 REST API (GA)**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true) is now generally available (GA)**! The v4.0 REST API includes the following changes:
 
-* [🆕 Batch API](concept-batch-analysis.md)
+* [Batch API](concept-batch-analysis.md)
   * Batch API now supports all models, including all read, layout, prebuilt verticals, and custom models.
   * Batch API supports LIST function to allow users to list batch jobs within past seven days.
   * Batch API supports DELETE function to explicitly delete batch job for GDPR and privacy compliance.
   * GetAnalyzeBatchResult supports resultId in response to LIST all resultIds.
- 
-* 🆕 Searchable PDF. The [prebuilt read](prebuilt/read.md) model now supports images formats (JPEG/JPG, PNG, BMP, TIFF, HEIF)  and language expansion to include Chinese, Japanese, and Korean for  [PDF output](prebuilt/read.md#searchable-pdf).
- 
+
+* Searchable PDF. The [prebuilt read](prebuilt/read.md) model now supports images formats (JPEG/JPG, PNG, BMP, TIFF, HEIF)  and language expansion to include Chinese, Japanese, and Korean for  [PDF output](prebuilt/read.md#searchable-pdf).
+
 * [Custom classification model](train/custom-model.md#custom-classification-model)
-  * Custom classification model supports incremental training. You can add new samples to existing classes or add new classes by referencing an existing classifier. 
+  * Custom classification model supports incremental training. You can add new samples to existing classes or add new classes by referencing an existing classifier.
   * With v4.0, custom classification model doesn't split documents by default during analysis. You need to explicitly set 'splitMode' property to auto to preserve the older behavior.
   * Custom classification model now supports 25,000 pages as new training page limit.
 
@@ -85,18 +102,18 @@ For more information, *see* client libraries for the following supported program
   * Mortgage model now supports signature detection for  forms 1003, 1004, 1005 and closing disclosure.
 
 * [Receipt Model](concept-receipt.md)
-  * Receipt Model now supports more fields including ReceiptType, Tax rate, CountryRegion, net amount and description. 
- 
-*  [🆕 US Tax model](prebuilt/tax-document.md)
-   *  New prebuilt tax models added for 1095A, 1095C, 1099SSA, and W4.
+  * Receipt Model now supports more fields including ReceiptType, Tax rate, CountryRegion, net amount and description.
+
+* [US Tax model](prebuilt/tax-document.md)
+  * New prebuilt tax models added for `1095A`, `1095C`, `1099SSA`, and `W4`.
 
 * [Delete analyze response](/rest/api/aiservices/document-models/delete-analyze-result?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true&tabs=HTTP)
-  * Analyze response is stored for 24 hours from when the operation completes for retrieval. For scenarios where you want to delete the response sooner, use the delete analyze response API to delete the response.  
+  * Analyze response is stored for 24 hours from when the operation completes for retrieval. For scenarios where you want to delete the response sooner, use the delete analyze response API to delete the response.
 
 * The v4.0 API includes cumulative updates from preview releases as listed:
   * [August 2024](#august-2024)
   * [May 2024](#may-2024)
-  * [Feb 2024](#february-2024) 
+  * [Feb 2024](#february-2024)
 
 ## August 2024
 
@@ -109,26 +126,26 @@ The Document Intelligence [**2024-07-31-preview**](/rest/api/aiservices/document
 * **West Europe**
 * **North Central US**
 
-* [🆕 Model compose with custom classifiers](train/composed-models.md)
+* [Model compose with custom classifiers](train/composed-models.md)
   * Document Intelligence now adds support for composing model with an explicit custom classification model. [Learn more about the benefits](train/composed-models.md) of using the new compose capability.
 * [Custom classification model](train/custom-model.md#custom-classification-model)
   * Custom classification model now supports updating the model in-place as well.
   * Custom classification model adds support for model copy operation to enable backup and disaster recovery.
   * Custom classification model now supports explicitly specifying pages to be classified from an input document.
-* [🆕 Mortgage documents model](concept-mortgage-documents.md)
+* [Mortgage documents model](concept-mortgage-documents.md)
   * Extract information from Appraisal (Form 1004).
   * Extract information from Validation of Employment (Form 1005).
-* [🆕 Check model](concept-bank-check.md)
+* [Check model](concept-bank-check.md)
   * Extract payee, amount, date, and other relevant information from checks.​
-* [🆕 Pay Stub model](concept-pay-stub.md)
+* [Pay Stub model](concept-pay-stub.md)
   * New prebuilt to process pay stubs to extract wages, hours, deductions, net pay and more.​
-* [🆕 Bank statement model](concept-bank-statement.md)
+* [Bank statement model](concept-bank-statement.md)
   * New prebuilt to extract account information including beginning and ending balances, transaction details from bank statements.​
-* [🆕 US Tax model](prebuilt/tax-document.md)
+* [US Tax model](prebuilt/tax-document.md)
   * New unified US tax model that can extract from forms such as W-2, 1098, 1099, and 1040.
-* 🆕 Searchable PDF. The [prebuilt read](prebuilt/read.md) model now supports [PDF output](prebuilt/read.md#searchable-pdf)  to download PDFs with embedded text from extraction results, allowing for PDF to be utilized in scenarios such as search copy of contents.
-* [Layout model](prebuilt/layout.md) now supports improved [figure detection](prebuilt/layout.md#figures) where figures from documents can now be downloaded as an image file to be used for further figure understanding. The layout model also features improvements to the OCR model for scanned text targeting improvements for single characters, boxed text, and dense text documents.
-* [🆕 Batch API](concept-batch-analysis.md)
+* Searchable PDF. The [prebuilt read](prebuilt/read.md) model now supports [PDF output](prebuilt/read.md#searchable-pdf)  to download PDFs with embedded text from extraction results, allowing for PDF to be utilized in scenarios such as search copy of contents.
+* [Layout model](prebuilt/layout.md) now supports improved [figure detection](prebuilt/layout.md#figures) where figures from documents can now be downloaded as an image file to be used for further figure understanding. The layout model also features improvements to the `OCR` model for scanned text targeting improvements for single characters, boxed text, and dense text documents.
+* [Batch API](concept-batch-analysis.md)
   * Document Intelligence now adds support for batch analysis operation to support analyzing a set of documents to simplify developer experience and improve efficiency.
 * [Add-on capabilities](concept-add-on-capabilities.md)
   * [Query fields](concept-add-on-capabilities.md#query-fields) AI quality of extraction is improved with the latest model.
@@ -188,14 +205,14 @@ The Document Intelligence [**2024-07-31-preview**](/rest/api/aiservices/document
   * Tax items support expansion for Germany (`de`), Spain (`es`), Portugal (`pt`), English Canada `en-CA`.
 
 * [ID model](prebuilt/id-document.md)
-  * [Expanded field support](prebuilt/id-document.md#supported-document-types) for European Union IDs and driver license.
-* [🆕 Mortgage documents](concept-mortgage-documents.md)
+  * [Expanded field support](prebuilt/id-document.md#supported-document-types) for European Union identification cards and driver licenses.
+* [Mortgage documents](concept-mortgage-documents.md)
   * Extract information from Uniform Residential Loan Application (Form 1003).
   * Extract information from Uniform Underwriting and Transmittal Summary or Form 1008.
   * Extract information from mortgage closing disclosure.
-* [🆕 Credit/Debit card model](concept-credit-card.md)
+* [Credit/Debit card model](concept-credit-card.md)
   * Extract information from bank cards.
-* [🆕 Marriage certificate](concept-marriage-certificate.md)
+* [Marriage certificate](concept-marriage-certificate.md)
   * New prebuilt to extract information from marriage certificates.
 
 ## December 2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスの最新情報の更新"
}
```

### Explanation
この変更は、`whats-new.md`ファイルにおいて、ドキュメントインテリジェンスサービスの最新情報を包括的に更新するものです。合計で48行が追加され、31行が削除され、全体で79行の変更が行われています。

主な変更点としては、2025年11月には新しい機能である「Content Understanding」がリリースされたことが追加されており、この機能はテキスト、画像、音声、動画の処理能力を統合するものです。これにより、利用者はより多様なコンテンツからインサイトを抽出できるようになります。また、複数の新機能や拡張機能に関する具体的な説明が更新されており、たとえば「バッチAPI」とは、一度に複数のドキュメントを処理するための新しいサポートが追加されていることが挙げられます。

さらに、各種モデルのサポート状況も詳しく記されており、例えばレシートモデルのフィールド拡張や、米国税モデルの追加機能に関する情報も更新されています。これにより、開発者は常に新しいAPI機能やモデルにアクセスし、最新の利用ケースに対応できるようになっています。

このアップデートにより、ユーザーはドキュメントインテリジェンスの最新機能を把握し、効率的に利用できるための重要な情報源となっています。具体的な変更内容の詳細については、以下のリンクで確認できます: [コードの差分](https://github.com/MicrosoftDocs/azure-ai-docs/blob/8ef275a1d20d13feed3124dd4854ecb071048674/articles%2Fai-services%2Fdocument-intelligence%2Fwhats-new.md)。


