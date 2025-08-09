---
date: '2025-08-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ba81df5...MicrosoftDocs:fad6b8c
summary: このコード差分は、Azure AIサービスに関連するドキュメントの軽微なアップデートを含んでおり、明確性向上と最新情報の反映に焦点を当てています。新しく追加されたPII検出機能のエンティティや更新されたAPIやSDKの操作手順が特徴です。また、主な変更として破壊的な点はないものの、APIエンドポイントの更新には注意が必要です。全体として、文書の可読性が向上し、ユーザー体験の向上に寄与する内容となっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ba81df5...MicrosoftDocs:fad6b8c){target="_blank"}

# Highlights
このコード差分は、複数のAzure AIサービスに関連するドキュメントの軽微なアップデートを含んでおり、明確性向上と最新情報の反映に焦点を当てています。特に、APIやSDK関連のエンドポイントと例の更新、エンティティの追加、新機能情報の明確化が行われています。

## New features
- PII検出機能における新しいエンティティとして、生年月日やナンバープレートなどが追加。
- プリビルトAPIとカスタム質問応答システムにおける操作手順やサポートされる言語コードの更新。

## Breaking changes
特に破壊的な変更は見られないが、APIエンドポイントの更新は影響を与える可能性があるため、注意が必要。

## Other updates
- Java、C#、Python SDKに関する文書が更に明確にされ、可読性が向上。
- モデルライフサイクルや質問応答システムにおける日付や例の調整。
- 全体の文書内容が最新情報を反映し、簡潔な表現に整理。

# Insights
Azure AIサービスのドキュメントは、ユーザー体験を向上させ、開発者がより効率的に作業できるように改善されています。この度の更新では、エンドポイントの変更やエンティティの拡充がなされている点が重要です。特にAPIやSDKのエンドポイントが最新の形式に変更されたことで、ユーザーは正確な接続情報を使用することができ、サービスの利用における技術的障害が軽減されるでしょう。

さらに、PII検出に関する新しいエンティティが追加されたことで、より多様なデータを扱うことが可能になり、安全で具体的なデータ管理が促進されます。質問応答システムやプリビルトAPIの手順がクリアになったことは、開発者がシステムの構築や運用をスムーズに進めるために大いに役立ちます。

全体として、今回のドキュメントのアップデートは、技術的な正確さだけでなく、ユーザービリティの向上にも重点が置かれており、Azureサービスを利用する開発者にとって価値ある改善と言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [java-sdk.md](#item-166b2e) | minor update | Java SDKのドキュメント更新 | modified | 11 | 17 | 28 | 
| [model-lifecycle.md](#item-417f3f) | minor update | モデルライフサイクルに関する日付および機能サポートの更新 | modified | 13 | 13 | 26 | 
| [named-entity-recognition.png](#item-2d7ba0) | minor update | 命名エンティティ認識の画像更新 | modified | 0 | 0 | 0 | 
| [entity-categories.md](#item-ba2623) | minor update | 個人識別情報のエンティティカテゴリに関する情報更新 | modified | 89 | 4 | 93 | 
| [adapt-to-domain-pii.md](#item-62092f) | minor update | ドメインベースの個人識別情報（PII）適応に関するガイドの更新 | modified | 152 | 156 | 308 | 
| [overview.md](#item-8a6932) | minor update | 個人識別情報（PII）検出に関する新しいエンティティの追加 | modified | 7 | 0 | 7 | 
| [authoring.md](#item-855d84) | minor update | 質問応答システムの著作権に関するドキュメントの更新 | modified | 74 | 74 | 148 | 
| [export-import-refresh.md](#item-2d1b56) | minor update | カスタム質問応答におけるエクスポート・インポート手順の更新 | modified | 15 | 15 | 30 | 
| [prebuilt.md](#item-a28843) | minor update | プリビルトAPIに関するドキュメントの更新 | modified | 100 | 100 | 200 | 
| [rest.md](#item-e6e1b0) | minor update | REST APIに関するドキュメントの更新 | modified | 12 | 12 | 24 | 
| [sdk-csharp.md](#item-af9649) | minor update | C# SDKに関するドキュメントの更新 | modified | 19 | 19 | 38 | 
| [sdk-python.md](#item-33436a) | minor update | Python SDKに関するドキュメントの更新 | modified | 15 | 15 | 30 | 
| [multiple-domains.md](#item-323a1c) | minor update | 複数のドメインを持つFAQボット作成に関するチュートリアルの更新 | modified | 13 | 13 | 26 | 
| [toc.yml](#item-12f1f0) | minor update | PIIに関するTOCの更新 | modified | 3 | 3 | 6 | 
| [whats-new.md](#item-69b272) | minor update | 新機能に関するドキュメントの更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/quickstarts/includes/java-sdk.md{#item-166b2e}

<details>
<summary>Diff</summary>
````diff
@@ -264,9 +264,11 @@ Extract text, selection marks, text styles, table structures, and bounding regio
 
 ```java
 
-import com.azure.ai.documentintelligence.models.AnalyzeDocumentRequest;
+import com.azure.ai.documentintelligence.DocumentIntelligenceClient;
+import com.azure.ai.documentintelligence.DocumentIntelligenceClientBuilder;
+import com.azure.ai.documentintelligence.models.AnalyzeDocumentOptions;
+import com.azure.ai.documentintelligence.models.AnalyzeOperationDetails;
 import com.azure.ai.documentintelligence.models.AnalyzeResult;
-import com.azure.ai.documentintelligence.models.AnalyzeResultOperation;
 import com.azure.ai.documentintelligence.models.DocumentTable;
 import com.azure.core.credential.AzureKeyCredential;
 import com.azure.core.util.polling.SyncPoller;
@@ -291,17 +293,11 @@ public class DocIntelligence {
     String modelId = "prebuilt-layout";
     String documentUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf";
 
-    SyncPoller <AnalyzeResultOperation, AnalyzeResultOperation> analyzeLayoutPoller =
-      client.beginAnalyzeDocument(modelId,
-          null,
-          null,
-          null,
-          null,
-          null,
-          null,
-          new AnalyzeDocumentRequest().setUrlSource(documentUrl));
+    AnalyzeDocumentOptions options = new AnalyzeDocumentOptions(documentUrl);
 
-    AnalyzeResult analyzeLayoutResult = analyzeLayoutPoller.getFinalResult().getAnalyzeResult();
+    SyncPoller<AnalyzeOperationDetails, AnalyzeResult> analyzeLayoutPoller = client.beginAnalyzeDocument(modelId, options);
+
+    AnalyzeResult analyzeLayoutResult = analyzeLayoutPoller.getFinalResult();
 
     // pages
     analyzeLayoutResult.getPages().forEach(documentPage -> {
@@ -336,16 +332,14 @@ public class DocIntelligence {
       DocumentTable documentTable = tables.get(i);
       System.out.printf("Table %d has %d rows and %d columns.%n", i, documentTable.getRowCount(),
         documentTable.getColumnCount());
-      documentTable.getCells().forEach(documentTableCell -> {
+      documentTable.getCells().forEach(documentTableCell ->
         System.out.printf("Cell '%s', has row index %d and column index %d.%n", documentTableCell.getContent(),
-          documentTableCell.getRowIndex(), documentTableCell.getColumnIndex());
-      });
+          documentTableCell.getRowIndex(), documentTableCell.getColumnIndex()));
       System.out.println();
     }
 
     // styles
-    analyzeLayoutResult.getStyles().forEach(documentStyle -
-      > System.out.printf("Document is handwritten %s.%n", documentStyle.isHandwritten()));
+    analyzeLayoutResult.getStyles().forEach(documentStyle -> System.out.printf("Document is handwritten %s.%n", documentStyle.isHandwritten()));
   }
 }
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java SDKのドキュメント更新"
}
```

### Explanation
このコードの変更は、Java SDKのドキュメントに関するもので、記述の明確化や構文の改善が含まれています。具体的には、クラスメソッドの使用例が更新され、いくつかのインポート文が追加されたり修正されたりしました。

主な変更点には、以下の内容が含まれています：
- `AnalyzeDocumentRequest` から `AnalyzeDocumentOptions` への移行。この変更により、文書のURLを直接 `AnalyzeDocumentOptions` オブジェクトに渡すことで、コードが簡潔になりました。
- `SyncPoller` とその戻り値の型が明確に指定され、より適切に更新されました。
- ドキュメント内のスタイル情報の取得に関するコードが修正され、ラムダ式の表現が簡潔になりました。

これにより、Java SDKを使用する開発者にとって、より理解しやすく、使いやすいコード例となっています。

## articles/ai-services/language-service/concepts/model-lifecycle.md{#item-417f3f}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 07/22/2025
+ms.date: 08/07/2025
 ms.author: lajanuar
 ---
 
@@ -35,18 +35,18 @@ By default, API and SDK requests use the latest Generally Available model. To us
 
 Use the following table to find which model versions support each feature:
 
-| Feature                                             | Supported generally available (GA) version     | Latest supported preview versions           |
-|-----------------------------------------------------|------------------------------------------------|---------------------------------------------|
-| Sentiment Analysis and opinion mining               | `latest`                                      |                                              |
-| Language Detection                                  | `latest`                                      |                                              |
-| Entity Linking                                      | `latest`                                      |                                              |
-| Named Entity Recognition (NER)                      | `latest`                                      | `2025-05-15-preview`                         |
-| Personally Identifiable Information (PII) detection | `latest`                                      | `2025-05-15-preview`                         | 
-| PII detection for conversations                     | `latest`                                      | `2024-11-01-preview`                         |
-| Question answering                                  | `latest`                                      |                                              |
-| Text Analytics for health                           | `latest`                                      | `2023-04-15-preview`                         |
-| Key phrase extraction                               | `latest`                                      |                                              | 
-| Summarization                                       | `latest`                                      | `2025-06-10-preview` (only available for `issue` and `resolution` aspects in conversation summarization)  |
+| Feature | Supported generally available (GA) version | Latest supported preview versions |
+|--|--|--|
+| Sentiment Analysis and opinion mining | `latest` |  |
+| Language Detection | `latest` |  |
+| Entity Linking | `latest` |  |
+| Named Entity Recognition (NER) | `latest` | `2025-08-01-preview` |
+| Personally Identifiable Information (PII) detection | `latest` | `2025-08-01-preview` |
+| PII detection for conversations | `latest` | `2024-11-01-preview` |
+| Question answering | `latest` |  |
+| Text Analytics for health | `latest` | `2023-04-15-preview` |
+| Key phrase extraction | `latest` |  |
+| Summarization | `latest` | `2025-06-10-preview` (only available for `issue` and `resolution` aspects in conversation summarization) |
 
 
 ## Custom features
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルに関する日付および機能サポートの更新"
}
```

### Explanation
この変更は、モデルライフサイクルに関するドキュメントの内容を更新したもので、主に日付の修正と機能サポートに関する情報の整理が含まれています。

具体的な変更内容は次の通りです：
- `ms.date` の値が2025年7月22日から2025年8月7日へと変更されています。これにより、ドキュメントの更新日が正確になります。
- 機能サポートのテーブルが再フォーマットされ、可読性を向上させています。新しいテーブルでは、機能名、サポートされている一般公開（GA）バージョン、最新のプレビュー版がより明確に示されています。
- 特に、いくつかの機能について、プレビュー版のバージョンが更新されており（例えば、NERおよびPII検出）、最新の情報が反映されています。

これにより、このドキュメントを利用するユーザーにとって、最新のバージョン情報や機能サポートの状態が分かりやすくなっています。

## articles/ai-services/language-service/media/overview/named-entity-recognition.png{#item-2d7ba0}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "命名エンティティ認識の画像更新"
}
```

### Explanation
この変更は、命名エンティティ認識に関連する画像ファイルの更新です。具体的には、ファイルの内容は変更されていないものの、ファイルのメタデータや表示方法が修正された可能性があります。ただし、画像自体には追加や削除、または変更はありません。

この更新により、命名エンティティ認識に関するドキュメント内での画像の表示がより適切または最新の状態に保たれることになります。これにより、ユーザーが関連情報をよりスムーズに理解できるようになります。

## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories.md{#item-ba2623}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 06/04/2025
+ms.date: 08/07/2025
 ms.author: lajanuar
 ms.custom:
   - language-service-pii
@@ -85,6 +85,7 @@ This category contains the following entity:
 
    :::column-end:::
 :::row-end:::
+
 ---
 
 # [Preview API](#tab/preview-api)
@@ -146,11 +147,89 @@ This category contains the following entity:
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
 
+   :::column-end:::
+ :::row-end:::
+
+---
+
+# [Preview API](#tab/preview-api)
+
+## Type: License Plate 🆕
+
+This type contains the following entity:
+
+
+:::row:::
+    :::column span="":::
+        **Entity**
+
+        LicensePlate
+
+    :::column-end:::
+    :::column span="2":::
+        **Details**
+
+        License Plate is an alphanumeric code assigned to a vehicle by a state's Department of Licensing (or the equivalent).
+
+        To get this entity category, add `LicensePlate` to the `piiCategories` parameter. `LicensePlate` is returned in the API response if detected.
+
+    :::column-end:::
+
+    :::column span="":::
+      **Supported languages**
+
+      `en`
+
+   :::column-end:::
+:::row-end:::
+
+# [GA API](#tab/ga-api)
+
+## License Plate
+
+The **LicensePlate** entity isn't available with the current GA version.
+
+---
+
+# [Preview API](#tab/preview-api)
+
+## Type: Sort Code 🆕
+
+This type contains the following entity:
+
+:::row:::
+    :::column span="":::
+            **Entity**
+
+            SortCode
+
+        :::column-end:::
+        :::column span="2":::
+            **Details**
+
+            `SortCode` entity is a 6-digit number used in the UK to identify a specific bank and branch where a bank account is held.
+
+            To get this entity category, add `SortCode` to the `piiCategories` parameter. `SortCode` is returned in the API response if detected.
+
+        :::column-end:::
+
+        :::column span="":::
+          **Supported languages**
+
+          `en`
+
    :::column-end:::
 :::row-end:::
 
+# [GA API](#tab/ga-api)
+
+## Sort Code
+
+The **SortCode** entity isn't available with the current GA version.
+
 ---
 
+
 # [Preview API](#tab/preview-api)
 
 ## Type: PhoneNumber
@@ -212,6 +291,7 @@ This category contains the following entity:
    :::column-end:::
 
 :::row-end:::
+
 ---
 
 # [Preview API](#tab/preview-api)
@@ -607,6 +687,7 @@ This category contains the following entity:
     :::column-end:::
 
 :::row-end:::
+
 ---
 
 # [Preview API](#tab/preview-api)
@@ -775,7 +856,7 @@ The PII service supports the Age subtype within the broader Quantity type (since
    :::column-end:::
 :::row-end:::
 
-#### Subtype: DateOfBirth
+#### Subtype: DateOfBirth 🆕
 
 :::row:::
     :::column span="":::
@@ -789,13 +870,13 @@ The PII service supports the Age subtype within the broader Quantity type (since
 
       Date
 
-      To get this entity type, add `DateOfBirth` to the `piiCategories` parameter. `DateOfBirth` is returned in the API response if detected. 
+      To get this entity type, add `DateOfBirth` to the `piiCategories` parameter. `DateOfBirth` is returned in the API response if detected.
 
     :::column-end:::
     :::column span="2":::
       **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `nl`
 
    :::column-end:::
 :::row-end:::
@@ -829,6 +910,10 @@ This category contains the following entities:
    :::column-end:::
 :::row-end:::
 
+### Subtypes
+
+The subtype `DateOFBirth` isn't available in the current GA version.
+
 ### Subcategories
 
 The entity in this category can have the following subcategory:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人識別情報のエンティティカテゴリに関する情報更新"
}
```

### Explanation
この変更は、個人識別情報に関するドキュメントの「エンティティカテゴリ」に関する情報を更新したものです。主な変更点は以下の通りです：

- ドキュメントの日付が2025年6月4日から2025年8月7日へと更新され、最新の情報が反映されています。
- 新しいエンティティタイプ（例：ライセンスプレートやソートコード）が追加され、それぞれのエンティティに関する詳細な説明や取得方法、サポートされている言語が記載されています。このことにより、ユーザーがAPIを通じて新しいエンティティをどのように扱うかを理解しやすくなっています。
- その他のエンティティカテゴリ情報も更新され、特に「DateOfBirth」サブタイプのアップデートが加えられ、今後のGAバージョンでの利用に関する通知が含まれています。

この更新により、利用者は新たに追加されたエンティティやその利用方法についての理解を深め、より効果的なAPI運用が可能になります。

## articles/ai-services/language-service/personally-identifiable-information/how-to/adapt-to-domain-pii.md{#item-62092f}

<details>
<summary>Diff</summary>
````diff
@@ -6,219 +6,215 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 04/29/2025
+ms.date: 08/08/2025
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
 
-# Adapting Personally Identifying Information (PII) to your domain
+# Adapt Personally Identifying Information (PII) to your domain
 
-## Overview
+To support using your own terminology to identify entities (also known as *context*), the `entitySynonyms` feature enables you to define custom synonyms for specific entity types. This feature helps the system detect entities that appear in your inputs using terms or vocabulary that the model doesn't recognize by default. Aligning your specific terms with standard entities allows the model to accurately recognize and link these terms during entity detection.
 
-To accommodate and adapt to a customer’s custom vocabulary used to identify entities (also known as the "context"), the `entitySynonyms` feature allows customers to define their own synonyms for specific entity types. The goal of this feature is to help detect entities in contexts that the model isn't familiar with but are used in the customer’s inputs by ensuring that the customer’s unique terms are recognized and correctly associated during the detection process. 
+This custom vocabulary support enhances the prebuilt PII (Personally Identifiable Information) detection service, which is originally trained on general language and may not understand specialized or informal vocabulary—such as using *BAN* instead of *InternationalBankAccountNumber*. As a result, PII detection is capable of recognizing sensitive information even when it appears in slang, abbreviations, or informal language. This detection enhancement strengthens the system's ability to safeguard privacy in everyday, real-world scenarios.
 
-This adapts the prebuilt PII service which is trained to detect entities based on general domain text which may not match a customer’s custom input vocabulary, such as writing "BAN" instead of "InternationalBankAccountNumber". 
+We strongly recommend that you first test the accuracy of the entity detection feature without adding synonyms. Then only introduce custom synonyms if the model doesn't perform well with the default settings. For instance, if the model already recognizes *Org* as *organization*, there's no need to add it as a synonym.
 
-This means PII detection can catch sensitive information even when it’s written in different styles, slang, or casual language. That makes the system better at protecting privacy in real-world situations. 
+Once you test the service with your own data, you can use `entitySynonyms` to:
 
-We strongly recommend that customers first test the quality of predictions without introducing synonyms and only use them if the model isn't performing well. For example, "Org" may be something that the model already understands as "organization" and there's no need to use the Synonym feature. 
-
-After testing the service on their data, customers can use `entitySynonyms` to:
-
-* Specify particular [entities within the prebuilt service](../concepts/entity-categories.md) for which there are custom synonym context words in their input vocabulary.
-* List the custom synonyms.
+* Identify specific [entities within the prebuilt service](../concepts/entity-categories.md) that require custom synonym context words from your input vocabulary.
+* Provide a list of custom synonyms for context entities.
 * Specify the language of each synonym.
 
-## API Schema for the 'entitySynoyms' parameter
+## API Schema for the 'entitySynonyms' parameter
 
 ```json
-{ 
-    "parameter":  
-    "entitySynonyms": [  
-        { 
-            "entityType": "InternationalBankAccountNumber", 
-            "synonyms": [ {"synonym": "BAN", "language": "en"} ] 
-        } 
+{
+    "parameter":
+    "entitySynonyms": [
+        {
+            "entityType": "InternationalBankAccountNumber",
+            "synonyms": [ {"synonym": "BAN", "language": "en"} ]
+        }
     ]
-} 
+}
 ```
 
 ## Usage guidelines
 
-1. Synonyms must be restricted to phrases that directly refer to the type, and preserve semantic correctness. For example, for the entity type `InternationalBankAccountNumber`, a valid synonym could be "Financial Account Number" or "FAN". But, the word "deposit" though may be associated with type, as it doesn't directly have a meaning of a bank account number and therefore shouldn't be used. 
-1. Synonyms should be country agnostic. For example, "German passport" wouldn't be helpful to include.
+1. Synonyms must be restricted to phrases that directly refer to the type, and preserve semantic correctness. For example, for the entity type `InternationalBankAccountNumber`, a valid synonym could be "Financial Account Number" or *FAN*. But, the word *deposit* though may be associated with type, as it doesn't directly have a meaning of a bank account number and therefore shouldn't be used.
+1. Synonyms should be country agnostic. For example, *German passport* wouldn't be helpful to include.
 1. Synonyms can't be reused for more than one entity type.
 1. This synonym recognition feature only accepts a subset of entity types supported by the service. The supported entity types and example synonyms include:
 
-| Supported entity type             | Entity Type                       | Example synonyms                                                                         |
-|-----------------------------------|-----------------------------------|------------------------------------------------------------------------------------------|
-| ABA Routing Number                | ABARoutingNumber                  | Routing transit number (RTN)                                                             |
-| Address                           | Address                           | My place is                                                                              |
-| Age                               | Age                               | Years old, age in years, current age, person’s age, biological age                       |
-| Bank Account Number               | BankAccountNumber                 | Bank acct no., savings account number, checking account number, financial account number |
-| Credit Card Number                | CreditCardNumber                  | Cc number, payment card number, credit acct no.                                          |
-| Date                              | DateTime                          | Given date, specified date                                                               |
-| Date of Birth                     | DateOfBirth                       | Birthday, DOB, birthdate                                                                 |
-| International Bank Account Number | InternationalBankingAccountNumber | IBAN, intl bank acct no.                                                                 |
-| Organization                      | Organization                      | company, business, firm, corporation, agency, group, institution, entity, legal entity, party, respondent, plaintiff, defendant, jurisdiction, partner, provider, facility, practice, network, institution, enterprise, LLC, Inc, LLP, incorporated, employer, brand, subsidiary |
-| Person                            | Person                            | Name, individual, account holder |
-| Person Type                       | PersonType                        | Role, title, position |
-| Phone number                      | PhoneNumber                       | Landline, cell, mobile |
-| Swift Code                        | SWIFTCode                         | SWIFT code, BIC (Bank Identifier Code), SWIFT Identifier |
+|Supported entity type|Entity Type|Example synonyms|
+|--|--|--|
+|ABA Routing Number|ABARoutingNumber|Routing transit number (RTN)|
+|Address|Address|My place is|
+|Age|Age|Years old, age in years, current age, person's age, biological age|
+|Bank Account Number|BankAccountNumber|Bank acct no., savings account number, checking account number, financial account number|
+|Credit Card Number|CreditCardNumber|Cc number, payment card number, credit acct no.|
+|Date|DateTime|Given date, specified date|
+|Date of Birth|DateOfBirth|Birthday, DOB, birthdate|
+|International Bank Account Number|InternationalBankingAccountNumber|IBAN, intl bank acct no.|
+|Organization|Organization|company, business, firm, corporation, agency, group, institution, entity, legal entity, party, respondent, plaintiff, defendant, jurisdiction, partner, provider, facility, practice, network, institution, enterprise, LLC, Inc, LLP, incorporated, employer, brand, subsidiary|
+|Person|Person|Name, individual, account holder|
+|Person Type|PersonType|Role, title, position|
+|Phone number|PhoneNumber|Landline, cell, mobile|
+|Swift Code|SWIFTCode|SWIFT code, BIC (Bank Identifier Code), SWIFT Identifier|
 
 ## Customizing PII output by specifying values to exclude
 
-The `valueExclusionPolicy` option allows customers to adapt the PII service for scenarios where customers prefer certain terms be undetected and redacted even if those terms fall into a PII category they're interested in detected. For example, a police department might want personal identifiers redacted in most cases except for terms like "police officer", "suspect", and "witness".  
+The `valueExclusionPolicy` option allows you to adapt the PII service for scenarios where certain preferred terms can be undetected and redacted even if those terms fall into a PII category you're interested in detecting. For example, a police department might want personal identifiers redacted in most cases except for terms like *police officer*, *suspect*, and *witness*.
 
-In the following example, customers can use the `valueExclusionPolicy` option to specify a list of values which they wouldn't like to be detected or redacted from the input text. In the example below, if the user specifies the value "1 Microsoft Way, Redmond, WA 98052, US", even if the Address entity is turned-on, this value isn't redacted or listed in the returned API payload output. 
+In the following example, you can use the `valueExclusionPolicy` option to specify a list of values that you wouldn't like to be detected or redacted from the input text. In the next example, if the user enters the value *1 Microsoft Way, Redmond, WA 98052, US*, this value isn't redacted. It also isn't included in the returned API payload output, even if the `Address` entity is enabled.
 
-A subset of the specified excluded value, such as "1 Microsoft Way" isn't excluded.
+A subset of the specified excluded value, such as *One Microsoft Way* isn't excluded.
 
 ### Input
 ```json
-{ 
-  "kind": "PiiEntityRecognition", 
-  "parameters": { 
-    "modelVersion": "latest", 
-    "redactionPolicy": { 
-      "policyKind": "characterMask", 
-      "redactionCharacter": "-" 
-    }, 
-    "valueExclusionPolicy": { 
-      "caseSensitive": false, 
-      "excludedValues": { 
-        "1 Microsoft Way, Redmond, WA 98052", 
-        "1045 La Avenida St, Mountain View, CA 94043" 
-      } 
-    } 
-  }, 
-  "analysisInput": { 
-    "documents": [ 
-      { 
-        "id": "1", 
-        "text": "The police and John Doe inspected the storage garages located at 123 Main St, 1 Microsoft Way, Redmond, WA 98052, 456 Washington Blvd, Portland, OR, and 1045 La Avenida St, Mountain View, CA 94043" 
-      } 
-    ] 
-  } 
-} 
+{
+  "kind": "PiiEntityRecognition",
+  "parameters": {
+    "modelVersion": "latest",
+    "redactionPolicy": {
+      "policyKind": "characterMask",
+      "redactionCharacter": "-"
+    },
+    "valueExclusionPolicy": {
+      "caseSensitive": false,
+      "excludedValues": {
+        "1 Microsoft Way, Redmond, WA 98052",
+        "1045 La Avenida St, Mountain View, CA 94043"
+      }
+    }
+  },
+  "analysisInput": {
+    "documents": [
+      {
+        "id": "1",
+        "text": "The police and John Doe inspected the storage garages located at 123 Main St, 1 Microsoft Way, Redmond, WA 98052, 456 Washington Blvd, Portland, OR, and 1045 La Avenida St, Mountain View, CA 94043"
+      }
+    ]
+  }
+}
 ```
 
 ### Output
 ```json
-{ 
-    "kind": "PiiEntityRecognitionResults", 
-    "results": { 
-        "documents": [ 
-            { 
-                "redactedText": "The police and John Doe inspected the storage garages located at **********, 1 Microsoft Way, Redmond, WA 98052, ********************************, and 1045 La Avenida St, Mountain View, CA 94043" 
-                "id": "1", 
-                "entities": [ 
-                    { 
-                        "text": "John Doe", 
-                        "category": "Person", 
-                        "offset": 16, 
-                        "length": 5, 
-                        "confidenceScore": 0.98 
-                    } 
-                ], 
-                "warnings": [] 
-            } 
-        ], 
-        "errors": [], 
-        "modelVersion": "2021-01-15" 
-    } 
-} 
+{
+    "kind": "PiiEntityRecognitionResults",
+    "results": {
+        "documents": [
+            {
+                "redactedText": "The police and John Doe inspected the storage garages located at **********, 1 Microsoft Way, Redmond, WA 98052, ********************************, and 1045 La Avenida St, Mountain View, CA 94043"
+                "id": "1",
+                "entities": [
+                    {
+                        "text": "John Doe",
+                        "category": "Person",
+                        "offset": 16,
+                        "length": 5,
+                        "confidenceScore": 0.98
+                    }
+                ],
+                "warnings": []
+            }
+        ],
+        "errors": [],
+        "modelVersion": "2021-01-15"
+    }
+}
 ```
 ## Customizing PII detection using your own regex (only available for Text PII container)
 
-Customers can now adapt the PII service’s detecting by specifying their own regex using a regex recognition configuration file. See our [container how-to guides](../concepts/entity-categories.md) for a tutorial on how to install and run Personally Identifiable Information (PII) Detection containers.
+You can now adapt the PII service's detecting by specifying your own regex using a regex recognition configuration file. See our [container how-to guides](../concepts/entity-categories.md) for a tutorial on how to install and run Personally Identifiable Information (PII) Detection containers.
 
 > [!NOTE]
-> This only available for the Text PII container
+> Regex specification is only available for the Text PII container.
 
 ```bash
-docker run --rm -it -p 5000:5000 --memory 8g --cpus 1 \ 
-mcr.microsoft.com/azure-cognitive-services/textanalytics/pii:{IMAGE_TAG} \ 
-Eula=accept \ 
-Billing={ENDPOINT_URI} \ 
-ApiKey={API_KEY} \ 
-UserRegexRuleFilePath={REGEX_RULE_FILE_PATH} 
+docker run --rm -it -p 5000:5000 --memory 8g --cpus 1 \
+mcr.microsoft.com/azure-cognitive-services/textanalytics/pii:{IMAGE_TAG} \
+Eula=accept \
+Billing={ENDPOINT_URI} \
+ApiKey={API_KEY} \
+UserRegexRuleFilePath={REGEX_RULE_FILE_PATH}
 ```
 
 `UserRegexRuleFilePath` is the file path of the user defined regex rules.
 
 ### Regex recognition file format
 ```json
-[ 
-    { 
-      "name": "USSocialSecurityNumber", // category, type and tag to be returned. This name must be unique 
-      "description": "Rule to identify USSocialSecurityNumber in text", // used to describe the category 
-      "regexPatterns": [ // list of regex patterns to identify the entities 
-        { 
-          "id": "StrongSSNPattern", // id for the regex pattern 
-          "pattern": "(?<!\\d)([0-9]{3}-[0-9]{2}-[0-9]{4}|[0-9]{3} [0-9]{2} [0-9]{4}|[0-9]{3}.[0-9]{2}.[0-9]{4})(?!\\d)", // regex pattern to provide matches 
-          "matchScore": 0.65, // score to assign if the regex matches 
-          "locales": [ // list of languages valid for this regex 
-            "en" 
-         ] 
-        }, 
-        { 
-          "id": "WeakSSNPattern", 
-          "pattern": "(?<!\\d)([0-9]{9})(?!\\d)", 
-          "matchScore": 0.55, 
-          "locales": [ 
-            "en" 
-          ] 
-        } 
-      ], 
-      "matchContext": { // patterns to give matches context 
-        "hints": [ 
-          { 
-            "hintText": "ssa(\\s*)number", // regex pattern to find to give a match context. 
-            "boostingScore": 0.2, // score to boost match confidence if hint is found 
-            "locales": [ // list of languages valid for this context 
-              "en" 
-            ] 
-          }, 
-          { 
-            "hintText": "social(\\s*)security(\\s*)(#*)", 
-            "boostingScore": 0.2, 
-            "locales": [ 
-              "en" 
-            ] 
-          } 
-        ], 
-      } 
-    } 
-] 
+[
+    {
+      "name": "USSocialSecurityNumber", // category, type and tag to be returned. This name must be unique
+      "description": "Rule to identify USSocialSecurityNumber in text", // used to describe the category
+      "regexPatterns": [ // list of regex patterns to identify the entities
+        {
+          "id": "StrongSSNPattern", // id for the regex pattern
+          "pattern": "(?<!\\d)([0-9]{3}-[0-9]{2}-[0-9]{4}|[0-9]{3} [0-9]{2} [0-9]{4}|[0-9]{3}.[0-9]{2}.[0-9]{4})(?!\\d)", // regex pattern to provide matches
+          "matchScore": 0.65, // score to assign if the regex matches
+          "locales": [ // list of languages valid for this regex
+            "en"
+         ]
+        },
+        {
+          "id": "WeakSSNPattern",
+          "pattern": "(?<!\\d)([0-9]{9})(?!\\d)",
+          "matchScore": 0.55,
+          "locales": [
+            "en"
+          ]
+        }
+      ],
+      "matchContext": { // patterns to give matches context
+        "hints": [
+          {
+            "hintText": "ssa(\\s*)number", // regex pattern to find to give a match context.
+            "boostingScore": 0.2, // score to boost match confidence if hint is found
+            "locales": [ // list of languages valid for this context
+              "en"
+            ]
+          },
+          {
+            "hintText": "social(\\s*)security(\\s*)(#*)",
+            "boostingScore": 0.2,
+            "locales": [
+              "en"
+            ]
+          }
+        ],
+      }
+    }
+]
 ```
 
 ### Overview of each regex recognition file parameter
 
-| Parameter       | Subparameters and Descriptions                                                 |
+|Parameter      |Subparameters and Descriptions                                                |
 |-----------------|-------------------------------------------------------------|
-| `name`          | Category, type, and tag to return if there's a regex match. |
-| `decription`    | (optional) User-readable rule description.                  |
-| `regexPatterns` | List of regex patterns used to find entities.<br>- `id`: Identifier of the regex pattern.<br>- `matchScore`: Confidence score for regex matches.<br>- `locales`: Languages valid for the regex pattern.|
-| `matchcontext`  | Regex patterns providing context to matched entities. Context matching is a bidirectional search from the matched entity that increases confidence score in case it's found.  If multiple hints are supporting a match the hint with the highest score is used.<br>- `hints`: List of regex patterns giving context to matched entities.<br>    - `hintText`: Regex pattern providing context to matched entities.<br>    - `boostingScore`: (optional) Score added to confidence score from a matched entity.<br>    - `locales`: Language valid for hintText.<br>- `contextLimit`: (optional) Distance from the matched entity to search for context. |
+|`name`         |Category, type, and tag to return if there's a regex match.|
+|`decription`   |(optional) User-readable rule description.                 |
+|`regexPatterns`|List of regex patterns used to find entities.<br>* `id`: Identifier of the regex pattern.<br>- `matchScore`: Confidence score for regex matches.<br>* `locales`: Languages valid for the regex pattern.|
+|`matchcontext` |Regex patterns providing context to matched entities. Context matching is a bidirectional search from the matched entity that increases confidence score in when found. If multiple hints support a match, the hint with the highest score is used.<br>* `hints`: List of regex patterns giving context to matched entities.<br>* `hintText`: Regex pattern providing context to matched entities.<br>* `boostingScore`: (optional) Score added to confidence score from a matched entity.<br>* `locales`: Language valid for hintText.<br>* `contextLimit`: (optional) Distance from the matched entity to search for context.|
 
 ### Logging
 
 To display information about the running `regexRules`, add the following property to enable debug logging: `Logging:Console:LogLevel:Default=Debug`
 
 ```bash
-docker run --rm -it -p 5000:5000 --memory 8g --cpus 1 \ 
-mcr.microsoft.com/azure-cognitive-services/textanalytics/pii:{IMAGE_TAG} \ 
-Eula=accept \ 
-Billing={ENDPOINT_URI} \ 
-ApiKey={API_KEY} \ 
-UserRegexRuleFilePath={REGEX_RULE_FILE_PATH} \ 
-Logging:Console:LogLevel:Default=Debug 
+docker run --rm -it -p 5000:5000 --memory 8g --cpus 1 \
+mcr.microsoft.com/azure-cognitive-services/textanalytics/pii:{IMAGE_TAG} \
+Eula=accept \
+Billing={ENDPOINT_URI} \
+ApiKey={API_KEY} \
+UserRegexRuleFilePath={REGEX_RULE_FILE_PATH} \
+Logging:Console:LogLevel:Default=Debug
 ```
- 
+
 ### Regex rule constraints
 
-- Rule names must begin with "CE_"  
-- Rule names must be unique. 
-- Rule names may only use alphanumeric characters and underscores ("_")
-- Regex patterns follow the .NET regular Expressions format. See [our documentation on .NET regular expressions](/dotnet/standard/base-types/regular-expressions) for more information. 
\ No newline at end of file
+- Rule names must begin with *CE_*
+- Rule names must be unique.
+- Rule names may only use alphanumeric characters and underscores (*_*)
+- Regex patterns follow the .NET regular Expressions format. For more information, see [our documentation on .NET regular expressions](/dotnet/standard/base-types/regular-expressions).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドメインベースの個人識別情報（PII）適応に関するガイドの更新"
}
```

### Explanation
この変更は、ドメインベースの個人識別情報（PII）を適応させる方法に関するガイドを大幅に更新したものです。主な変更点は以下の通りです：

- ドキュメントの日付が2025年4月29日から2025年8月8日へ更新され、最新の情報が反映されています。
- タイトルが「Adapting Personally Identifying Information (PII) to your domain」から「Adapt Personally Identifying Information (PII) to your domain」に変更され、より直接的な表現となっています。
- `entitySynonyms`機能についての説明が簡潔かつ明確になり、ユーザー自身の用語を使用してエンティティを識別できる仕組みが強調されています。この機能により、カスタマイズされた語彙に応じてエンティティの認識精度が向上します。
- `valueExclusionPolicy`オプションが修正され、特定の用語を検出および除外する方法の具体例が示されています。例えば、警察署が特定の個人識別子を除外する方法についての説明が加えられています。
- 正規表現を使用してPII検出をカスタマイズする際の手順と注意点が強調され、デバッグログの有効化の方法も説明されています。

この更新により、ユーザーはPIIサービスの利用方法をより明確に理解でき、特定のビジネスニーズに合わせた設定を行うことが簡素化されます。

## articles/ai-services/language-service/personally-identifiable-information/overview.md{#item-8a6932}

<details>
<summary>Diff</summary>
````diff
@@ -20,6 +20,13 @@ Azure AI Language Personally Identifiable Information (PII) detection is a featu
 
 ## What's new
 
+The 2025-05-15-preview introduces several new entities:
+
+* [**DateOfBirth**](concepts/entity-categories.md#category-datetime) with English, French, German, Italian, Spanish, Portuguese, Brazilian Portuguese, and Dutch language support.
+* [**LicensePlate**](concepts/entity-categories.md#type-license-plate-) with English language support.
+* [**SortCard**](concepts/entity-categories.md#type-sort-code-) with English language support.
+
+
 The Text PII and Conversational PII detection preview API (version `2024-11-15-preview`) now supports the option to mask detected sensitive entities with a label beyond just redaction characters. Customers can specify if personal data content such as names and phone numbers, that is, `"John Doe received a call from 424-878-9192"`, are masked with a redaction character, that is, `"******** received a call from ************"`, or masked with an entity label, that is, `"[PERSON_1] received a call from [PHONENUMBER_1]"`. More on how to specify the redaction policy style for your outputs can be found in our [how-to guides](how-to-call.md). 
 
 The Conversational PII detection models (both version `2024-11-01-preview` and `GA`) are updated to provide enhanced AI quality and accuracy. The numeric identifier entity type now also includes Drivers License and Medicare Beneficiary Identifier.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人識別情報（PII）検出に関する新しいエンティティの追加"
}
```

### Explanation
この変更は、個人識別情報（PII）検出機能に関するドキュメントの「概要」セクションを更新し、新たに導入されたエンティティを追加したものです。主な変更点は以下の通りです：

- 2025年5月15日プレビュー版に関する情報が新たに追加され、いくつかの新しいエンティティについての説明が盛り込まれています。
  - **DateOfBirth**（生年月日）：英語、フランス語、ドイツ語、イタリア語、スペイン語、ポルトガル語、ブラジルポルトガル語、オランダ語に対応。
  - **LicensePlate**（ナンバープレート）：英語に対応。
  - **SortCard**（ソートコード）：英語に対応。
  
- テキストPIIと会話PII検出のプレビューAPI（バージョン`2024-11-15-preview`）は、検出された敏感なエンティティを単にマスキング文字で隠すのではなく、ラベルでマスキングするオプションもサポートしています。これにより、個人データの内容をより具体的に表現することが可能になります。

- また、会話PII検出モデル（バージョン`2024-11-01-preview`とGA）がAIの品質と精度を向上させるために更新され、数値識別子エンティティタイプには運転免許証やメディケア被保険者識別子が含まれるようになりました。

これらの変更により、ユーザーは新しいエンティティの利用可能性と、個人データのマスキング方法に関する情報にアクセスでき、PII検出機能の利便性が向上します。

## articles/ai-services/language-service/question-answering/how-to/authoring.md{#item-855d84}

<details>
<summary>Diff</summary>
````diff
@@ -6,32 +6,32 @@ ms.service: azure-ai-language
 author: laujan
 ms.author: lajanuar
 ms.topic: how-to
-ms.date: 06/30/2025
+ms.date: 08/07/2025
 ---
 
 # Authoring API
 
-The custom question answering Authoring API is used to automate common tasks like adding new question answer pairs, as well as creating, publishing, and maintaining projects. 
+The custom question answering Authoring API is used to automate common tasks like adding new question answer pairs, and creating, publishing, and maintaining projects. 
 
 > [!NOTE]
-> Authoring functionality is available via the REST API and [Authoring SDK (preview)](/dotnet/api/overview/azure/ai.language.questionanswering-readme). This article provides examples of using the REST API with cURL. For full documentation of all parameters and functionality available consult the [REST API reference content](/rest/api/questionanswering/question-answering-projects).
+> Authoring functionality is available via the REST API and [Authoring SDK (preview)](/dotnet/api/overview/azure/ai.language.questionanswering-readme). This article provides examples of using the REST API with cURL. For full documentation of all parameters and functionality available, consult the [REST API reference content](/rest/api/questionanswering/question-answering-projects).
 
 ## Prerequisites
 
 * The current version of [cURL](https://curl.haxx.se/). Several command-line switches are used in this article, which are noted in the [cURL documentation](https://curl.haxx.se/docs/manpage.html).
-* The commands in this article are designed to be executed in a Bash shell. These commands will not always work in a Windows command prompt or in PowerShell without modification. If you do not have a Bash shell installed locally, you can use the [Azure Cloud Shell's bash environment](/azure/cloud-shell/overview).
+* The commands in this article are executed in a Bash shell. These commands don't always work in a Windows command prompt or in PowerShell without modification. If you don't have a Bash shell installed locally, you can use the [Azure Cloud Shell's bash environment](/azure/cloud-shell/overview).
 
 ## Create a project
 
 To create a project programmatically:
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If the prior example was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/`. If the prior example was your endpoint in the following code sample, you would only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively, you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `NEW-PROJECT-NAME` | The name for your new custom question answering project.|
 
-You can also adjust additional values like the project language, the default answer given when no answer can be found that meets or exceeds the confidence threshold, and whether this language resource will support multiple languages.
+You can also adjust more values, such as the project language. Another option is to set the default answer that is provided when no response meets or exceeds the confidence threshold. In addition, you can specify whether this language resource supports multiple languages.
 
 ### Example query
 
@@ -44,7 +44,7 @@ curl -X PATCH -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applic
       },
       "multilingualResource": true
     }
-  }'  'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{NEW-PROJECT-NAME}?api-version=2021-10-01'
+  }'  'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{NEW-PROJECT-NAME}?api-version=2021-10-01'
 ```
 
 ### Example response
@@ -75,32 +75,32 @@ To delete a project programmatically:
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If the prior example was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/`. If the prior example was your endpoint in the following code sample, you would only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to delete.|
 
 ### Example query
 
 ```bash
-curl -X DELETE -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -i 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}?api-version=2021-10-01'
+curl -X DELETE -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -i 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}?api-version=2021-10-01'
 ```
 
-A successful call to delete a project results in an `Operation-Location` header being returned, which can be used to check the status of the delete project job. In most our examples, we haven't needed to look at the response headers and thus haven't been displaying them. To retrieve the response headers our curl command uses `-i`. Without this parameter prior to the endpoint address, the response to this command would appear empty as if no response occurred.
+A successful call to delete a project results in an `Operation-Location` header being returned, which can be used to check the status of the deleted project job. In most our examples, we don't view the response headers. To retrieve the response headers our curl command uses `-i`. Without this parameter preceding the endpoint address, the response to this command would appear empty as if no response occurred.
 
 ### Example response
 
 ```bash
 HTTP/2 202
 content-length: 0
-operation-location: https://southcentralus.api.cognitive.microsoft.com:443/language/query-knowledgebases/projects/sample-proj1/deletion-jobs/{JOB-ID-GUID}
+operation-location: https://southcentralus.cognitiveservices.azure.com:443/language/query-knowledgebases/projects/sample-proj1/deletion-jobs/{JOB-ID-GUID}
 x-envoy-upstream-service-time: 324
 apim-request-id:
 strict-transport-security: max-age=31536000; includeSubDomains; preload
 x-content-type-options: nosniff
 date: Tue, 23 Nov 2021 20:56:18 GMT
 ```
 
-If the project was already deleted or could not be found, you would receive a message like:
+If the project was already deleted or couldn't be found, you would receive a message like:
 
 ```json
 {
@@ -123,15 +123,15 @@ To check on the status of your delete project request:
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to check on the deployment status for.|
-| `JOB-ID` | When you delete a project programmatically, a `JOB-ID` is generated as part of the `operation-location` response header to the deletion request. The `JOB-ID` is the guid at the end of the `operation-location`. For example: `operation-location: https://southcentralus.api.cognitive.microsoft.com:443/language/query-knowledgebases/projects/sample-proj1/deletion-jobs/{THIS GUID IS YOUR JOB ID}` |
+| `JOB-ID` | When you delete a project programmatically, a `JOB-ID` is generated as part of the `operation-location` response header to the deletion request. The `JOB-ID` is the guid at the end of the `operation-location`. For example: `operation-location: https://southcentralus.cognitiveservices.azure.com:443/language/query-knowledgebases/projects/sample-proj1/deletion-jobs/{THIS GUID IS YOUR JOB ID}` |
 
 ### Example query
 
 ```bash
-curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/deletion-jobs/{JOB-ID}?api-version=2021-10-01'
+curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/deletion-jobs/{JOB-ID}?api-version=2021-10-01'
 ```
 
 ### Example response
@@ -148,19 +148,19 @@ curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applicat
 
 ## Get project settings
 
-To retrieve information about a given project, update the following values in the query below:
+To retrieve information about a given project, update the following values in the query:
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to retrieve information about.|
 
 ### Example query
 
 ```bash
 
-curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}?api-version=2021-10-01'
+curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}?api-version=2021-10-01'
 ```
 
 ### Example response
@@ -186,18 +186,18 @@ curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applicat
 
 ## Get question answer pairs
 
-To retrieve question answer pairs and related information for a given project, update the following values in the query below:
+To retrieve question answer pairs and related information for a given project, update the following values in the query:
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to retrieve all the question answer pairs for.|
 
 ### Example query
 
 ```bash
-curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}/qnas?api-version=2021-10-01'
+curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}/qnas?api-version=2021-10-01'
 
 ```
 
@@ -256,18 +256,18 @@ curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applicat
 
 ## Get sources
 
-To retrieve the sources and related information for a given project, update the following values in the query below:
+To retrieve the sources and related information for a given project, update the following values in the query:
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to retrieve all the source information for.|
 
 ### Example query
 
 ```bash
-curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT_NAME}/sources?api-version=2021-10-01'
+curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT_NAME}/sources?api-version=2021-10-01'
 ```
 
 ### Example response
@@ -299,19 +299,19 @@ curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applicat
 
 ## Get synonyms
 
-To retrieve synonyms and related information for a given project, update the following values in the query below:
+To retrieve synonyms and related information for a given project, update the following values in the query:
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to retrieve synonym information for.|
 
 ### Example query
 
 ```bash
 
-curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}/synonyms?api-version=2021-10-01'
+curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}/synonyms?api-version=2021-10-01'
 ```
 
 ### Example response
@@ -342,28 +342,28 @@ curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applicat
 
 ## Deploy project
 
-To deploy a project to production, update the following values in the query below:
+To deploy a project to production, update the following values in the query:
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to deploy to production.|
 
 ### Example query
 
 ```bash
-curl -X PUT -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' -i 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}/deployments/production?api-version=2021-10-01'  
+curl -X PUT -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' -i 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}/deployments/production?api-version=2021-10-01'  
 ```
 
-A successful call to deploy a project results in an `Operation-Location` header being returned which can be used to check the status of the deployment job. In most our examples, we haven't needed to look at the response headers and thus haven't been displaying them. To retrieve the response headers our curl command uses `-i`. Without this parameter prior to the endpoint address, the response to this command would appear empty as if no response occurred.
+A successful call to deploy a project results in an `Operation-Location` header being returned which can be used to check the status of the deployment job. In most our examples, we don't view the response headers. To retrieve the response headers our curl command uses `-i`. Without this parameter preceding the endpoint address, the response to this command would appear empty as if no response occurred.
 
 ### Example response
 
 ```bash
 0HTTP/2 202
 content-length: 0
-operation-location: https://southcentralus.api.cognitive.microsoft.com:443/language/query-knowledgebases/projects/sample-proj1/deployments/production/jobs/{JOB-ID-GUID}
+operation-location: https://southcentralus.cognitiveservices.azure.com:443/language/query-knowledgebases/projects/sample-proj1/deployments/production/jobs/{JOB-ID-GUID}
 x-envoy-upstream-service-time: 31
 apim-request-id:
 strict-transport-security: max-age=31536000; includeSubDomains; preload
@@ -375,15 +375,15 @@ date: Tue, 23 Nov 2021 20:35:00 GMT
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to check on the deployment status for.|
-| `JOB-ID` | When you deploy a project programmatically, a `JOB-ID` is generated as part of the `operation-location` response header to the deployment request. The `JOB-ID` is the guid at the end of the `operation-location`. For example: `operation-location: https://southcentralus.api.cognitive.microsoft.com:443/language/query-knowledgebases/projects/sample-proj1/deployments/production/jobs/{THIS GUID IS YOUR JOB ID}` |
+| `JOB-ID` | When you deploy a project programmatically, a `JOB-ID` is generated as part of the `operation-location` response header to the deployment request. The `JOB-ID` is the guid at the end of the `operation-location`. For example: `operation-location: https://southcentralus.cognitiveservices.azure.com:443/language/query-knowledgebases/projects/sample-proj1/deployments/production/jobs/{THIS GUID IS YOUR JOB ID}` |
 
 ### Example query
 
 ```bash
-curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}/deployments/production/jobs/{JOB-ID}?api-version=2021-10-01' 
+curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}/deployments/production/jobs/{JOB-ID}?api-version=2021-10-01' 
 ```
 
 ### Example response
@@ -408,22 +408,22 @@ curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applicat
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to export.|
 
 ### Example query
 
 ```bash
-curl -X POST -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '{exportAssetTypes": ["qnas","synonyms"]}' -i 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}/:export?api-version=2021-10-01&format=tsv'
+curl -X POST -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '{exportAssetTypes": ["qnas","synonyms"]}' -i 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}/:export?api-version=2021-10-01&format=tsv'
 ```
 
 ### Example response
 
 ```bash
 HTTP/2 202
 content-length: 0
-operation-location: https://southcentralus.api.cognitive.microsoft.com:443/language/query-knowledgebases/projects/Sample-project/export/jobs/{JOB-ID_GUID}
+operation-location: https://southcentralus.cognitiveservices.azure.com:443/language/query-knowledgebases/projects/Sample-project/export/jobs/{JOB-ID_GUID}
 x-envoy-upstream-service-time: 214
 apim-request-id:
 strict-transport-security: max-age=31536000; includeSubDomains; preload
@@ -435,15 +435,15 @@ date: Tue, 23 Nov 2021 21:24:03 GMT
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to check on the export status for.|
-| `JOB-ID` | When you export a project programmatically, a `JOB-ID` is generated as part of the `operation-location` response header to the export request. The `JOB-ID` is the guid at the end of the `operation-location`. For example: `operation-location: https://southcentralus.api.cognitive.microsoft.com/language/query-knowledgebases/projects/sample-proj1/export/jobs/{THIS GUID IS YOUR JOB ID}` |
+| `JOB-ID` | When you export a project programmatically, a `JOB-ID` is generated as part of the `operation-location` response header to the export request. The `JOB-ID` is the guid at the end of the `operation-location`. For example: `operation-location: https://southcentralus.cognitiveservices.azure.com/language/query-knowledgebases/projects/sample-proj1/export/jobs/{THIS GUID IS YOUR JOB ID}` |
 
 ### Example query
 
 ```bash
-curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/sample-proj1/export/jobs/{JOB-ID}?api-version=2021-10-01' 
+curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/sample-proj1/export/jobs/{JOB-ID}?api-version=2021-10-01' 
 ```
 
 ### Example response
@@ -455,37 +455,37 @@ curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applicat
   "jobId": "JOB-ID-GUID",
   "lastUpdatedDateTime": "2021-11-23T21:24:08+00:00",
   "status": "succeeded",
-  "resultUrl": "https://southcentralus.api.cognitive.microsoft.com:443/language/query-knowledgebases/projects/sample-proj1/export/jobs/{JOB-ID_GUID}/result"
+  "resultUrl": "https://southcentralus.cognitiveservices.azure.com:443/language/query-knowledgebases/projects/sample-proj1/export/jobs/{JOB-ID_GUID}/result"
 }
 ```
 
-If you try to access the resultUrl directly, you will get a 404 error. You must append `?api-version=2021-10-01` to the path to make it accessible by an authenticated request: `https://southcentralus.api.cognitive.microsoft.com:443/language/query-knowledgebases/projects/sample-proj1/export/jobs/{JOB-ID_GUID}/result?api-version=2021-10-01`
+If you try to access the resultUrl directly, you get a 404 error. You must append `?api-version=2021-10-01` to the path to make it accessible by an authenticated request: `https://southcentralus.cognitiveservices.azure.com:443/language/query-knowledgebases/projects/sample-proj1/export/jobs/{JOB-ID_GUID}/result?api-version=2021-10-01`
 
 ## Import project
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you would only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to be the destination for the import.|
-| `FILE-URI-PATH` | When you export a project programmatically, and then check the status the export a `resultUrl` is generated as part of the response. For example: `"resultUrl": "https://southcentralus.api.cognitive.microsoft.com:443/language/query-knowledgebases/projects/sample-proj1/export/jobs/{JOB-ID_GUID}/result"` you can use the resultUrl with the API version appended as a source file to import a project from: `https://southcentralus.api.cognitive.microsoft.com:443/language/query-knowledgebases/projects/sample-proj1/export/jobs/{JOB-ID_GUID}/result?api-version=2021-10-01`.|
+| `FILE-URI-PATH` | When you export a project programmatically, and then check the status the export a `resultUrl` is generated as part of the response. For example: `"resultUrl": "https://southcentralus.cognitiveservices.azure.com:443/language/query-knowledgebases/projects/sample-proj1/export/jobs/{JOB-ID_GUID}/result"` you can use the resultUrl with the API version appended as a source file to import a project from: `https://southcentralus.cognitiveservices.azure.com:443/language/query-knowledgebases/projects/sample-proj1/export/jobs/{JOB-ID_GUID}/result?api-version=2021-10-01`.|
 
 ### Example query
 
 ```bash
 curl -X POST -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '{
       "fileUri": "FILE-URI-PATH"
-  }' -i 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}/:import?api-version=2021-10-01&format=tsv'
+  }' -i 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}/:import?api-version=2021-10-01&format=tsv'
 ```
 
-A successful call to import a project results in an `Operation-Location` header being returned, which can be used to check the status of the import job. In many of our examples, we haven't needed to look at the response headers and thus haven't been displaying them. To retrieve the response headers our curl command uses `-i`. Without this additional parameter prior to the endpoint address, the response to this command would appear empty as if no response occurred.
+A successful call to import a project results in an `Operation-Location` header being returned, which can be used to check the status of the import job. In many of our examples, we view the response headers. To retrieve the response headers our curl command uses `-i`. Without this added parameter preceding the endpoint address, the response to this command would appear empty as if no response occurred.
 
 ### Example response
 
 ```bash
 HTTP/2 202
 content-length: 0
-operation-location: https://southcentralus.api.cognitive.microsoft.com:443/language/query-knowledgebases/projects/sample-proj1/import/jobs/{JOB-ID-GUID}
+operation-location: https://southcentralus.cognitiveservices.azure.com:443/language/query-knowledgebases/projects/sample-proj1/import/jobs/{JOB-ID-GUID}
 x-envoy-upstream-service-time: 417
 apim-request-id: 
 strict-transport-security: max-age=31536000; includeSubDomains; preload
@@ -497,15 +497,15 @@ date: Wed, 24 Nov 2021 00:35:11 GMT
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to be the destination for the import.|
-| `JOB-ID` | When you import a project programmatically, a `JOB-ID` is generated as part of the `operation-location` response header to the export request. The `JOB-ID` is the GUID at the end of the `operation-location`. For example: `operation-location: https://southcentralus.api.cognitive.microsoft.com/language/query-knowledgebases/projects/sample-proj1/import/jobs/{THIS GUID IS YOUR JOB ID}` |
+| `JOB-ID` | When you import a project programmatically, a `JOB-ID` is generated as part of the `operation-location` response header to the export request. The `JOB-ID` is the GUID at the end of the `operation-location`. For example: `operation-location: https://southcentralus.cognitiveservices.azure.com/language/query-knowledgebases/projects/sample-proj1/import/jobs/{THIS GUID IS YOUR JOB ID}` |
 
 ### Example query
 
 ```bash
-curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' 'https://southcentralus.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME/import/jobs/{JOB-ID-GUID}?api-version=2021-10-01' 
+curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' 'https://southcentralus.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME/import/jobs/{JOB-ID-GUID}?api-version=2021-10-01' 
 ```
 
 ### Example query response
@@ -525,14 +525,14 @@ curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applicat
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to generate a deployment list for.|
 
 ### Example query
 
 ```bash
-curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}/deployments?api-version=2021-10-01' 
+curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}/deployments?api-version=2021-10-01' 
 ```
 
 ### Example response
@@ -552,13 +552,13 @@ Retrieve a list of all question answering projects your account has access to.
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 
 ### Example query
 
 ```bash
-curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects?api-version=2021-10-01' 
+curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects?api-version=2021-10-01' 
 ```
 
 ### Example response
@@ -584,11 +584,11 @@ curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applicat
 
 ## Update sources
 
-In this example, we will add a new source to an existing project. You can also replace and delete existing sources with this command depending on what kind of operations you pass as part of your query body.
+In this example, we add a new source to an existing project. You can also replace and delete existing sources with this command depending on what kind of operations you pass as part of your query body.
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project where you would like to update sources.|
 |`METHOD`| PATCH |
@@ -609,14 +609,14 @@ curl -X PATCH -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applic
 ]'  -i '{LanguageServiceName}.cognitiveservices.azure.com//language/query-knowledgebases/projects/{projectName}/sources?api-version=2021-10-01'
 ```
 
-A successful call to update a source results in an `Operation-Location` header being returned which can be used to check the status of the import job. In many of our examples, we haven't needed to look at the response headers and thus haven't always been displaying them. To retrieve the response headers our curl command uses `-i`. Without this parameter prior to the endpoint address, the response to this command would appear empty as if no response occurred.
+A successful call to update a source results in an `Operation-Location` header being returned which can be used to check the status of the import job. In many of our examples, we don't view the response headers. To retrieve the response headers our curl command uses `-i`. Without this parameter preceding the endpoint address, the response to this command would appear empty as if no response occurred.
 
 ### Example response
 
 ```bash
 HTTP/2 202
 content-length: 0
-operation-location: https://southcentralus.api.cognitive.microsoft.com:443/language/query-knowledgebases/projects/Sample-project/sources/jobs/{JOB_ID_GUID}
+operation-location: https://southcentralus.cognitiveservices.azure.com:443/language/query-knowledgebases/projects/Sample-project/sources/jobs/{JOB_ID_GUID}
 x-envoy-upstream-service-time: 412
 apim-request-id: dda23d2b-f110-4645-8bce-1a6f8d504b33
 strict-transport-security: max-age=31536000; includeSubDomains; preload
@@ -628,15 +628,15 @@ date: Wed, 24 Nov 2021 02:47:53 GMT
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to be the destination for the import.|
-| `JOB-ID` | When you update a source programmatically, a `JOB-ID` is generated as part of the `operation-location` response header to the update source request. The `JOB-ID` is the GUID at the end of the `operation-location`. For example: `operation-location: https://southcentralus.api.cognitive.microsoft.com/language/query-knowledgebases/projects/sample-proj1/sources/jobs/{THIS GUID IS YOUR JOB ID}` |
+| `JOB-ID` | When you update a source programmatically, a `JOB-ID` is generated as part of the `operation-location` response header to the update source request. The `JOB-ID` is the GUID at the end of the `operation-location`. For example: `operation-location: https://southcentralus.cognitiveservices.azure.com/language/query-knowledgebases/projects/sample-proj1/sources/jobs/{THIS GUID IS YOUR JOB ID}` |
 
 ### Example query
 
 ```bash
-curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}/sources/jobs/{JOB-ID}?api-version=2021-10-01' 
+curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}/sources/jobs/{JOB-ID}?api-version=2021-10-01' 
 ```
 
 ### Example response
@@ -655,11 +655,11 @@ curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applicat
 
 ## Update question and answer pairs
 
-In this example, we will add a question answer pair to an existing source. You can also modify, or delete existing question answer pairs with this query depending on what operation you pass in the query body. If you don't have a source named `source5`, this example query will fail. You can adjust the source value in the body of the query to a source that exists for your target project.
+In this example, we add a question answer pair to an existing source. You can also modify, or delete existing question answer pairs with this query depending on what operation you pass in the query body. If you don't have a source named `source5`, this example query fails. You can adjust the source value in the body of the query to a source that exists for your target project.
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to be the destination for the import.|
 
@@ -681,17 +681,17 @@ curl -X PATCH -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applic
             }
         }
     }
-]'  -i 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}/qnas?api-version=2021-10-01'
+]'  -i 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}/qnas?api-version=2021-10-01'
 ```
 
-A successful call to update a question answer pair results in an `Operation-Location` header being returned which can be used to check the status of the update job. In many of our examples, we haven't needed to look at the response headers and thus haven't always been displaying them. To retrieve the response headers our curl command uses `-i`. Without this parameter prior to the endpoint address, the response to this command would appear empty as if no response occurred.
+A successful call to update a question answer pair results in an `Operation-Location` header being returned which can be used to check the status of the update job. In many of our examples, we don't view the response headers. To retrieve the response headers our curl command uses `-i`. Without this parameter preceding the endpoint address, the response to this command would appear empty as if no response occurred.
 
 ### Example response
 
 ```bash
 HTTP/2 202
 content-length: 0
-operation-location: https://southcentralus.api.cognitive.microsoft.com:443/language/query-knowledgebases/projects/Sample-project/qnas/jobs/{JOB-ID-GUID}
+operation-location: https://southcentralus.cognitiveservices.azure.com:443/language/query-knowledgebases/projects/Sample-project/qnas/jobs/{JOB-ID-GUID}
 x-envoy-upstream-service-time: 507
 apim-request-id: 
 strict-transport-security: max-age=31536000; includeSubDomains; preload
@@ -703,15 +703,15 @@ date: Wed, 24 Nov 2021 03:16:01 GMT
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to be the destination for the question answer pairs updates.|
-| `JOB-ID` | When you update a question answer pair programmatically, a `JOB-ID` is generated as part of the `operation-location` response header to the update request. The `JOB-ID` is the GUID at the end of the `operation-location`. For example: `operation-location: https://southcentralus.api.cognitive.microsoft.com/language/query-knowledgebases/projects/sample-proj1/qnas/jobs/{THIS GUID IS YOUR JOB ID}` |
+| `JOB-ID` | When you update a question answer pair programmatically, a `JOB-ID` is generated as part of the `operation-location` response header to the update request. The `JOB-ID` is the GUID at the end of the `operation-location`. For example: `operation-location: https://southcentralus.cognitiveservices.azure.com/language/query-knowledgebases/projects/sample-proj1/qnas/jobs/{THIS GUID IS YOUR JOB ID}` |
 
 ### Example query
 
 ```bash
-curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' 'https://southcentralus.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}/qnas/jobs/{JOB-ID}?api-version=2021-10-01' 
+curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: application/json" -d '' 'https://southcentralus.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}/qnas/jobs/{JOB-ID}?api-version=2021-10-01' 
 ```
 
 ### Example response
@@ -729,7 +729,7 @@ curl -X GET -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applicat
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to add synonyms.|
 
@@ -751,7 +751,7 @@ curl -X PUT -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applicat
       ]
     }
   ]
-}' -i 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}/synonyms?api-version=2021-10-01'
+}' -i 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}/synonyms?api-version=2021-10-01'
 ```
 
 ### Example response
@@ -775,7 +775,7 @@ date: Wed, 24 Nov 2021 03:59:09 GMT
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the code sample below, you would only need to add the region specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region specific portion of `southcentral`. The rest of the endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project you would like to be the destination for the active learning feedback updates.|
 
@@ -795,7 +795,7 @@ records": [
       "qnaId": 2
     }
   ]
-}' -i 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}/feedback?api-version=2021-10-01' 
+}' -i 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}/feedback?api-version=2021-10-01' 
 ```
 
 ### Example response
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "質問応答システムの著作権に関するドキュメントの更新"
}
```

### Explanation
この変更は、質問応答システムのための著作権APIに関するドキュメントが改訂されたことを示しています。具体的な変更点は以下の通りです：

- 更新日が2025年6月30日から2025年8月7日に変更され、最新の情報が反映されています。
- 一部の文言がわかりやすく整理され、冗長な表現が削除されました。例えば、「新しい質問回答ペアを追加する」ことに関する説明が簡潔に改訂されました。
- エンドポイントの例において、基盤となるサービスのURLが更新され、`southcentralus.api.cognitive.microsoft.com`から`southcentralus.cognitiveservices.azure.com`に変更されています。これにより、ユーザーは正しいエンドポイントを利用できるようになります。
- cURLコマンドの使い方に関する説明が強化され、特にAPIのレスポンスヘッダーの取得方法についての説明が調整されています。これにより、ユーザーがAPI呼び出しの結果を確認する際に直面するかもしれない問題が解決されます。

この更新により、ユーザーは質問応答システムの設定やAPIの利用方法についてより理解しやすくなり、適切なエンドポイントの利用が促進されます。

## articles/ai-services/language-service/question-answering/how-to/export-import-refresh.md{#item-2d1b56}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.topic: how-to
 author: laujan
 ms.author: lajanuar
 recommendations: false
-ms.date: 06/21/2025
+ms.date: 08/07/2025
 ---
 # Export-import-refresh in custom question answering
 
@@ -19,7 +19,7 @@ You might want to create a copy of your custom question answering project or rel
 
 ## Prerequisites
 
-* If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/cognitive-services/) before you begin.
+* An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services/) before you begin.
 * A [language resource](https://aka.ms/create-language-resource) with the custom question answering feature enabled. Remember your Microsoft Entra ID, Subscription, language resource name you selected when you created the resource.
 
 ## Export a project
@@ -28,9 +28,9 @@ You might want to create a copy of your custom question answering project or rel
 
 2. Scroll down to the **Answer questions** section and select **Open custom question answering**.
 
-3. Select the project you wish to export > Select **Export** > You’ll have the option to export as an **Excel** or **TSV** file.
+3. Select the project you wish to export > Select **Export** > You can export the project as an **Excel** or **TSV** file.
 
-4. You’ll be prompted to save your exported file locally as a zip file.
+4. You're prompted to save your exported file locally as a zip file.
 
 ### Export a project programmatically
 
@@ -46,9 +46,9 @@ To automate the export process, use the [export functionality of the authoring A
 
 4. Select Choose File and browse to the local zipped copy of your project that you exported previously.
 
-5. Provide a unique name for the project you’re importing.
+5. Provide a unique name for the project you're importing.
 
-6. Remember that a project that has only been imported still needs to be deployed/published if you want it to be live.
+6. Remember that a project that is only imported still needs to be deployed/published if you want it to be live.
 
 ### Import a project programmatically
 
@@ -62,7 +62,7 @@ To automate the import process, use the [import functionality of the authoring A
 
 3. Select the project that contains the source you want to refresh > select manage sources.
 
-4. We recommend having a backup of your project/question answer pairs prior to running each refresh so that you can always roll-back if needed.
+4. We recommend having a backup of your project/question answer pairs before running each refresh so that you can always roll back if needed.
 
 5. Select a URL-based source to refresh > Select **Refresh URL**.
 6. Only one URL can be refreshed at a time.
@@ -75,7 +75,7 @@ The update sources example in the [Authoring API docs](./authoring.md#update-sou
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`. If this was your endpoint in the following code sample, you would only need to add the region-specific portion of `southcentral` as the rest of the endpoint path is already present.|
+| `ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/` and you only need to add the region-specific portion of `southcentral`. The endpoint path is already present.|
 | `API-KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys allows for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `PROJECT-NAME` | The name of project where you would like to update sources.|
 
@@ -90,12 +90,12 @@ curl -X PATCH -H "Ocp-Apim-Subscription-Key: {API-KEY}" -H "Content-Type: applic
       "refresh": "true"
     }
   }
-]'  -i 'https://{ENDPOINT}.api.cognitive.microsoft.com/language/query-knowledgebases/projects/{PROJECT-NAME}/sources?api-version=2021-10-01'
+]'  -i 'https://{ENDPOINT}.cognitiveservices.azure.com/language/query-knowledgebases/projects/{PROJECT-NAME}/sources?api-version=2021-10-01'
 ```
 
 ## Export questions and answers
 
-It’s also possible to export/import a specific project of question and answers rather than the entire custom question answering project.
+It's also possible to export/import a specific project of question and answers rather than the entire custom question answering project.
 
 1. Sign in to the [Language Studio](https://language.azure.com/) with your Azure credentials.
 
@@ -105,16 +105,16 @@ It’s also possible to export/import a specific project of question and answers
 
 4. Select **Edit project**.
 
-5. To the right of show columns are `...` an ellipsis button. > Select the `...` > a dropdown will reveal the option to export/import questions and answers.
+5. To the right of show columns are `...` an ellipsis button. > Select the `...` > a dropdown reveals the option to export/import questions and answers.
 
-    Depending on the size of your web browser, you may experience the UI differently. Smaller browsers will see two separate ellipsis buttons.
+    Depending on the size of your web browser, you may experience the UI differently. Smaller browsers see two separate ellipsis buttons.
 
     > [!div class="mx-imgBorder"]
     > ![Screenshot of selecting multiple UI ellipsis buttons to get to import/export question and answer pair option](../media/export-import-refresh/export-questions.png)
 
 ## Import questions and answers
 
-It’s also possible to export/import a specific project of question and answers rather than the entire custom question answering project.
+It's also possible to export/import a specific project of question and answers rather than the entire custom question answering project.
 
 1. Sign in to the [Language Studio](https://language.azure.com/) with your Azure credentials.
 
@@ -124,9 +124,9 @@ It’s also possible to export/import a specific project of question and answers
 
 4. Select **Edit project**.
 
-5. To the right of show columns are `...` an ellipsis button. > Select the `...` > a dropdown will reveal the option to export/import questions and answers.
+5. To the right of show columns are `...` an ellipsis button. > Select the `...` > a dropdown reveals the option to export/import questions and answers.
 
-    Depending on the size of your web browser, you may experience the UI differently. Smaller browsers will see two separate ellipsis buttons.
+    Depending on the size of your web browser, you may experience the UI differently. Smaller browsers see two separate ellipsis buttons.
 
     > [!div class="mx-imgBorder"]
     > ![Screenshot of selecting multiple UI ellipsis buttons to get to import/export question and answer pair option](../media/export-import-refresh/export-questions.png)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム質問応答におけるエクスポート・インポート手順の更新"
}
```

### Explanation
この変更は、カスタム質問応答システムにおけるエクスポートおよびインポートに関する手順を更新したものです。主な改訂点は以下の通りです：

- 最終更新日が2025年6月21日から2025年8月7日に変更され、最新の情報が反映されています。
- 前提条件での表現が改善され、ユーザーがAzureサブスクリプションを無料で作成できることを明確に示しました。
- プロジェクトのエクスポート手順において、手順の記述がスムーズに整理され、冗長な表現が削除されています。例えば、ファイルの保存に関する表現が簡潔になりました。
- インポートやエクスポートに関連するミニマルな言い回しが修正され、一貫性が保たれました。
- APIエンドポイントのURLが改善され、より正確な情報が提供されています。
- 質問と回答のエクスポートおよびインポートに関する手順も改良され、ユーザーがよりわかりやすく手順を理解できるようになっています。

この変更により、ユーザーはカスタム質問応答プロジェクトのエクスポートおよびインポートをスムーズに行うことができるようになります。また、ドキュメントが一貫性を持ち、理解しやすくなっています。

## articles/ai-services/language-service/question-answering/how-to/prebuilt.md{#item-a28843}

<details>
<summary>Diff</summary>
````diff
@@ -6,31 +6,31 @@ ms.service: azure-ai-language
 author: laujan
 ms.author: lajanuar
 ms.topic: how-to
-ms.date: 06/21/2025
+ms.date: 08/07/2025
 ---
 
 # Prebuilt API
 
-The custom question answering **prebuilt API** provides you the capability to answer questions based on a passage of text without having to create projects, maintain question and answer pairs, or incurring costs for underutilized infrastructure. This functionality is provided as an API and can be used to meet question and answering needs without having to learn the details about custom question answering.
+The custom question answering **prebuilt API** provides you with the capability to answer questions based on a passage of text without having to create projects, maintain question and answer pairs, or incurring costs for underutilized infrastructure. This functionality is provided as an API and can be used to meet question and answering needs without having to learn the details about custom question answering.
 
-Given a user query and a block of text/passage the API will return an answer and precise answer (if available).
+Given a user query and a block of text/passage the API returns an answer and precise answer (if available).
 
 ## Example API usage
 
-Imagine that you have one or more blocks of text from which you would like to get answers for a given question. Normally you would have had to create as many sources as the number of blocks of text. However, now with the prebuilt API you can query the blocks of text without having to define content sources in a project.
+Imagine that you have one or more blocks of text from which you would like to get answers for a given question. Normally you have to create as many sources as the number of blocks of text. However, now with the prebuilt API you can query the blocks of text without having to define content sources in a project.
 
 Some other scenarios where this API can be used are:
 
-* You are developing an ebook reader app for end users, which allows them to highlight text, enter a question and find answers over a highlighted passage of text.
+* You're developing an ebook reader app for end users, which allows them to highlight text, enter a question and find answers over a highlighted passage of text.
 * A browser extension that allows users to ask a question over the content being currently displayed on the browser page.
 * A health bot that takes queries from users and provides answers based on the medical content that the bot identifies as most relevant to the user query.
 
-Below is an example of a sample request:
+Here's an example of a sample request:
 
 ## Sample request
 
 ```
-POST https://{Unique-to-your-endpoint}.api.cognitive.microsoft.com/language/:query-text
+POST https://{Unique-to-your-endpoint}.cognitiveservices.azure.com/language/:query-text
 ```
 
 ### Sample query over a single block of text
@@ -50,7 +50,7 @@ Request Body
       "records": [
         {
           "id": "1",
-          "text": "Power and charging. It takes two to four hours to charge the Surface Pro 4 battery fully from an empty state. It can take longer if you’re using your Surface for power-intensive activities like gaming or video streaming while you’re charging it."
+          "text": "Power and charging. It takes two to four hours to charge the Surface Pro 4 battery fully from an empty state. It can take longer if you're using your Surface for power-intensive activities like gaming or video streaming while you're charging it."
         },
         {
           "id": "2",
@@ -65,7 +65,7 @@ Request Body
 
 ## Sample response
 
-In the above request body, we query over a single block of text. A sample response received for the above query is shown below,
+In the request body, we query over a single block of text. Here's a sample response received for the query:
 
 ```json
 {
@@ -75,7 +75,7 @@ In the above request body, we query over a single block of text. A sample respon
       "body": {
         "answers": [
           {
-            "answer": "Power and charging. It takes two to four hours to charge the Surface Pro 4 battery fully from an empty state. It can take longer if you’re using your Surface for power-intensive activities like gaming or video streaming while you’re charging it.",
+            "answer": "Power and charging. It takes two to four hours to charge the Surface Pro 4 battery fully from an empty state. It can take longer if you're using your Surface for power-intensive activities like gaming or video streaming while you're charging it.",
             "confidenceScore": 0.93,
             "id": "1",
             "answerSpan": {
@@ -88,7 +88,7 @@ In the above request body, we query over a single block of text. A sample respon
             "length": 224
           },
           {
-            "answer": "It takes two to four hours to charge the Surface Pro 4 battery fully from an empty state. It can take longer if you’re using your Surface for power-intensive activities like gaming or video streaming while you’re charging it.",
+            "answer": "It takes two to four hours to charge the Surface Pro 4 battery fully from an empty state. It can take longer if you're using your Surface for power-intensive activities like gaming or video streaming while you're charging it.",
             "confidenceScore": 0.92,
             "id": "1",
             "answerSpan": {
@@ -101,7 +101,7 @@ In the above request body, we query over a single block of text. A sample respon
             "length": 224
           },
           {
-            "answer": "It can take longer if you’re using your Surface for power-intensive activities like gaming or video streaming while you’re charging it.",
+            "answer": "It can take longer if you're using your Surface for power-intensive activities like gaming or video streaming while you're charging it.",
             "confidenceScore": 0.05,
             "id": "1",
             "answerSpan": null,
@@ -128,97 +128,97 @@ These numbers represent the **per individual API call limits**:
 * Maximum three responses per document.
 
 ### Language codes supported
-The following language codes are supported by Prebuilt API. These language codes are in accordance to the [ISO 639-1 codes standard](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
+The following language codes support the Prebuilt API. These language codes are in accordance to the [ISO 639-1 codes standard](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
 
 Language code|Language
 ----|----
-af|Afrikaans
-am|Amharic
-ar|Arabic
-as|Assamese
-az|Azerbaijani
-ba|Bashkir
-be|Belarusian
-bg|Bulgarian
-bn|Bengali
-ca|Catalan, Valencian
-ckb|Central Kurdish
-cs|Czech
-cy|Welsh
-da|Danish
-de|German
-el|Greek, Modern (1453–)
-en|English
-eo|Esperanto
-es|Spanish, Castilian
-et|Estonian
-eu|Basque
-fa|Persian
-fi|Finnish
-fr|French
-ga|Irish
-gl|Galician
-gu|Gujarati
-he|Hebrew
-hi|Hindi
-hr|Croatian
-hu|Hungarian
-hy|Armenian
-id|Indonesian
-is|Icelandic
-it|Italian
-ja|Japanese
-ka|Georgian
-kk|Kazakh
-km|Central Khmer
-kn|Kannada
-ko|Korean
-ky|Kirghiz, Kyrgyz
-la|Latin
-lo|Lao
-lt|Lithuanian
-lv|Latvian
-mk|Macedonian
-ml|Malayalam
-mn|Mongolian
-mr|Marathi
-ms|Malay
-mt|Maltese
-my|Burmese
-ne|Nepali
-nl|Dutch, Flemish
-nn|Norwegian Nynorsk
-no|Norwegian
-or|Odia
-pa|Punjabi, Panjabi
-pl|Polish
-ps|Pashto, Pushto
-pt|Portuguese
-ro|Romanian
-ru|Russian
-sa|Sanskrit
-sd|Sindhi
-si|Sinhala, Sinhalese
-sk|Slovak
-sl|Slovenian
-sq|Albanian
-sr|Serbian
-sv|Swedish
-sw|Swahili
-ta|Tamil
-te|Telugu
-tg|Tajik
-th|Thai
-tl|Tagalog
-tr|Turkish
-tt|Tatar
-ug|Uighur, Uyghur
-uk|Ukrainian
-ur|Urdu
-uz|Uzbek
-vi|Vietnamese
-yi|Yiddish
-zh|Chinese
+`af`|Afrikaans
+`am`|Amharic
+`ar`|Arabic
+`as`|Assamese
+`az`|Azerbaijani
+`ba`|Bashkir
+`be`|Belarusian
+`bg`|Bulgarian
+`bn`|Bengali
+`ca`|Catalan
+`ckb`|Central Kurdish
+`cs`|Czech
+`cy`|Welsh
+`da`|Danish
+`de`|German
+`el`|Greek, Modern (1453–)
+`en`|English
+`eo`|Esperanto
+`es`|Spanish, Castilian
+`et`|Estonian
+`eu`|Basque
+`fa`|Persian
+`fi`|Finnish
+`fr`|French
+`ga`|Irish
+`gl`|Galician
+`gu`|Gujarati
+`he`|Hebrew
+`hi`|Hindi
+`hr`|Croatian
+`hu`|Hungarian
+`hy`|Armenian
+`id`|Indonesian
+`is`|Icelandic
+`it`|Italian
+`ja`|Japanese
+`ka`|Georgian
+`kk`|Kazakh
+`km`|Central Khmer
+`kn`|Kannada
+`ko`|Korean
+`ky`|Kirghiz, Kyrgyz
+`la`|Latin
+`lo`|Lao
+`lt`|Lithuanian
+`lv`|Latvian
+`mk`|Macedonian
+`ml`|Malayalam
+`mn`|Mongolian
+`mr`|Marathi
+`ms`|Malay
+`mt`|Maltese
+`my`|Burmese
+`ne`|Nepali
+`nl`|Dutch, Flemish
+`nn`|Norwegian Nynorsk
+`no`|Norwegian
+`or`|Odia
+`pa`|Punjabi, Punjabi
+`pl`|Polish
+`ps`|Pashto, Pushto
+`pt`|Portuguese
+`ro`|Romanian
+`ru`|Russian
+`sa`|Sanskrit
+`sd`|Sindhi
+`si`|Sinhala, Singhalese
+`sk`|Slovak
+`sl`|Slovenian
+`sq`|Albanian
+`sr`|Serbian
+`sv`|Swedish
+`sw`|Swahili
+`ta`|Tamil
+`te`|Telugu
+`tg`|Tajik
+`th`|Thai
+`tl`|Tagalog
+`tr`|Turkish
+`tt`|Tatar
+`ug`|Uighur, Uyghur
+`uk`|Ukrainian
+`ur`|Urdu
+`uz`|Uzbek
+`vi`|Vietnamese
+`yi`|Yiddish
+`zh`|Chinese
 
 ## Prebuilt API reference
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プリビルトAPIに関するドキュメントの更新"
}
```

### Explanation
この変更は、プリビルトAPIに関するドキュメントの内容を更新したものです。主な改訂点は以下の通りです：

- 最終更新日が2025年6月21日から2025年8月7日に変更され、最新の情報が反映されています。
- プリビルトAPIの機能説明が少し改善され、使用要件が明確に示されています。特に「APIを使用して質問を回答する能力がある」との説明が、ユーザーにとって分かりやすくなっています。
- エクスポートとインポートの手順において、文言が簡潔になり、冗長な表現が省かれました。特に手順の表現が明確化されています。
- サンプルリクエストやサンプル応答のセクションでは、フォーマットが統一され、読みやすく、理解しやすくなっています。
- プリビルトAPIでサポートされる言語コードの一覧が更新され、各言語コードの表記がいくつか訂正されました。これにより、ユーザーが簡単に言語コードを確認できるようになります。

この変更により、プリビルトAPIに関する情報が明確で、ユーザーが容易に利用方法や機能を理解できるようになっています。全体として、ドキュメントの可読性と一貫性が向上しています。

## articles/ai-services/language-service/question-answering/includes/rest.md{#item-e6e1b0}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: "Quickstart: Use cURL & REST to manage project - custom question answering"
 description: This quickstart shows you how to create, publish, and query your project using the REST APIs.
-ms.date: 06/30/2025
+ms.date: 08/07/2025
 ms.topic: include
 author: laujan
 ms.author: lajanuar
@@ -12,8 +12,8 @@ ms.author: lajanuar
 * The current version of [cURL](https://curl.haxx.se/). Several command-line switches are used in the quickstarts, which are noted in the [cURL documentation](https://curl.haxx.se/docs/manpage.html).
 * Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services)
 * Custom question answering requires a [Language resource](https://portal.azure.com/?quickstart=true#create/Microsoft.CognitiveServicesTextAnalytics) with the custom question answering feature enabled to generate an API key and endpoint.
-    * After your Language resource deploys, select **Go to resource**. You will need the key and endpoint from the resource you create to connect to the API. Paste your key and endpoint into the code below later in the quickstart.
-* To create a Language resource with [Azure CLI](../../../multi-service-resource.md?pivots=azcli) provide the following additional properties: `--api-properties qnaAzureSearchEndpointId=/subscriptions/<azure-subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.Search/searchServices/<azure-search-service-name> qnaAzureSearchEndpointKey=<azure-search-service-auth-key>`
+    * After your Language resource deploys, select **Go to resource**. You need the key and endpoint from the resource you create to connect to the API. Paste your key and endpoint into the code later in the quickstart.
+* Create a Language resource with [Azure CLI](../../../multi-service-resource.md?pivots=azcli) and provide the following properties: `--api-properties qnaAzureSearchEndpointId=/subscriptions/<azure-subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.Search/searchServices/<azure-search-service-name> qnaAzureSearchEndpointKey=<azure-search-service-auth-key>`
 * An existing project to query. If you have not setup a project, you can follow the instructions in the [**Language Studio quickstart**](../quickstart/sdk.md). Or add a project that uses this [Surface User Guide URL](https://download.microsoft.com/download/7/B/1/7B10C82E-F520-4080-8516-5CF0D803EEE0/surface-book-user-guide-EN.pdf) as a data source.
 
 
@@ -32,20 +32,20 @@ To [query a custom question answering project](/rest/api/questionanswering/quest
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `Endpoint`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`|
+| `Endpoint`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/`|
 | `API-Key` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys always for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `Project` | The name of your custom question answering project.|
-| `Deployment`             | There are two possible values: `test`, and `production`. `production` is dependent on you having deployed your project from **Language Studio** > **question answering** > **Deploy project**.|
+| `Deployment`             | There are two possible values: `test`, and `production`. `production` is dependent on you deploying your project from **Language Studio** > **question answering** > **Deploy project**.|
 
 The cURL command is executed from a BASH shell. Edit this command with your own resource name, resource key, and JSON values and size of JSON.
 
 ```bash
 curl -X POST -H "Ocp-Apim-Subscription-Key: $LANGUAGE_KEY" -H "Content-Type: application/json" -d '{
   "question": "How much battery life do I have left?"
-  }'  '$LANGUAGE_ENDPOINT.api.cognitive.microsoft.com/language/:query-knowledgebases?projectName={YOUR_PROJECT_NAME}&api-version=2021-10-01&deploymentName={DEPLOYMENT_NAME}'
+  }'  '$LANGUAGE_ENDPOINT.cognitiveservices.azure.com/language/:query-knowledgebases?projectName={YOUR_PROJECT_NAME}&api-version=2021-10-01&deploymentName={DEPLOYMENT_NAME}'
 ```
 
-When you run the code above, if you are using the data source from the prerequisites you will get an answer that looks as follows:
+When you run the code, if you're using the data source from the prerequisites you get an answer that looks as follows:
 
 ```json
 {
@@ -68,18 +68,18 @@ When you run the code above, if you are using the data source from the prerequis
 }
 ```
 
-The `confidenceScore` returns a value between 0 and 1. You can think of this like a percentage and multiply by 100 so a confidence score of 0.9185 means custom question answering is 91.85% confident this is the correct answer to the question based on the project.
+The `confidenceScore` returns a value between 0 and 1. Consider the confidence score as a percentage by multiplying it by 100. For example, a confidence score of 0.9185 indicates that the custom question-answering system is 91.85% confident that its response is correct based on the project information.
 
 If you want to exclude answers where the confidence score falls below a certain threshold, you can add the `confidenceScoreThreshold` parameter.
 
 ```bash
 curl -X POST -H "Ocp-Apim-Subscription-Key: $LANGUAGE_KEY" -H "Content-Type: application/json" -d '{
   "question": "How much battery life do I have left?",
   "confidenceScoreThreshold": "0.95",
-  }'  '$LANGUAGE_ENDPOINT.api.cognitive.microsoft.com//language/:query-knowledgebases?projectName=Sample-project&api-version=2021-10-01&deploymentName={DEPLOYMENT_NAME}'
+  }'  '$LANGUAGE_ENDPOINT.cognitiveservices.azure.com//language/:query-knowledgebases?projectName=Sample-project&api-version=2021-10-01&deploymentName={DEPLOYMENT_NAME}'
 ```
 
-Since we know from our previous execution of the code that our confidence score is: `.9185` setting the threshold to `.95` will result in the [default answer](../how-to/change-default-answer.md) being returned.
+Since we know from our previous execution of the code that our confidence score is: `.9185` setting the threshold to `.95` results in the [default answer](../how-to/change-default-answer.md) being returned.
 
 ```json
 {
@@ -111,10 +111,10 @@ curl -X POST -H "Ocp-Apim-Subscription-Key: $LANGUAGE_KEY" -H "Content-Type: app
 {"id":"doc2","text":"You can use the USB port on your Surface Pro 4 power supply to charge other devices, like a phone, while your Surface charges. The USB port on the power supply is only for charging, not for data transfer. If you want to use a USB device, plug it into the USB port on your Surface."}],
 "language":"en",
 "stringIndexType":"Utf16CodeUnit"
-}'  '$LANGUAGE_ENDPOINT.api.cognitive.microsoft.com/language/:query-text?&api-version=2021-10-01'
+}'  '$LANGUAGE_ENDPOINT.cognitiveservices.azure.com/language/:query-text?&api-version=2021-10-01'
 ```
 
-This example will return a result of:
+This example returns a result of:
 
 ```json
 {  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIに関するドキュメントの更新"
}
```

### Explanation
この変更は、REST APIに関するドキュメントを更新したもので、いくつかの修正が行われています。主な改訂点は以下の通りです：

- 最終更新日が2025年6月30日から2025年8月7日に変更され、最新の情報が提供されています。
- Azureの言語リソースの接続に関する記述が簡潔になり、必要なキーやエンドポイントの重要性が強調されています。
- cURLコマンド内で指定されるエンドポイントのURLが更新され、`api.cognitive.microsoft.com`から`cognitiveservices.azure.com`に変更され、最新のサービスと整合性が取れています。
- `confidenceScore`の説明がより明確にされ、スコアの解釈が具体的に示されています。これにより、ユーザーがスコアの意味を理解しやすくなっています。
- いくつかの文言が改善され、読みやすさが向上しています。具体的には、文末や表現が整理され、冗長なフレーズが削除されました。

全体として、この改訂はREST APIの利用に関する情報を一層明確にし、ユーザーが実際の操作や設定を行う際に役立つように整えられています。

## articles/ai-services/language-service/question-answering/includes/sdk-csharp.md{#item-af9649}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: This quickstart shows how to get started with the custom question a
 author: laujan
 ms.author: lajanuar
 ms.topic: include
-ms.date: 06/30/2025
+ms.date: 08/07/2025
 ---
 
 Use this quickstart for the custom question answering client library for .NET to:
@@ -13,7 +13,7 @@ Use this quickstart for the custom question answering client library for .NET to
 * Get an answer from a body of text that you send along with your question.
 * Get the confidence score for the answer to your question.
 
- [Reference documentation][questionanswering_refdocs] | [Package (NuGet)][questionanswering_nuget_package]  | [Additional samples][questionanswering_samples] | [Library source code][questionanswering_client_src]
+ [Reference documentation][questionanswering_refdocs] | [Package (NuGet)][questionanswering_nuget_package]  | [Samples][questionanswering_samples] | [Library source code][questionanswering_client_src]
 
 [questionanswering_nuget_package]: https://www.nuget.org/packages/Azure.AI.Language.QuestionAnswering/
 [questionanswering_refdocs]: /dotnet/api/Azure.AI.Language.QuestionAnswering/
@@ -25,9 +25,9 @@ Use this quickstart for the custom question answering client library for .NET to
 * Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services)
 * The [Visual Studio IDE](https://visualstudio.microsoft.com/vs/) or current version of [.NET Core](https://dotnet.microsoft.com/download/dotnet-core).
 * Custom question answering requires a [Language resource](https://portal.azure.com/?quickstart=true#create/Microsoft.CognitiveServicesTextAnalytics) with the custom question answering feature enabled to generate an API key and endpoint. 
-    * After your Language resource deploys, select **Go to resource**. You will need the key and endpoint from the resource you create to connect to the API. Paste your key and endpoint into the code below later in the quickstart.
-* To create a Language resource with [Azure CLI](../../../multi-service-resource.md?pivots=azcli) provide the following additional properties: `--api-properties qnaAzureSearchEndpointId=/subscriptions/<azure-subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.Search/searchServices/<azure-search-service-name> qnaAzureSearchEndpointKey=<azure-search-service-auth-key>`
-* An existing project to query. If you have not set up a project, you can follow the instructions in the [**Language Studio quickstart**](../quickstart/sdk.md). Or add a project that uses this [Surface User Guide URL](https://download.microsoft.com/download/7/B/1/7B10C82E-F520-4080-8516-5CF0D803EEE0/surface-book-user-guide-EN.pdf) as a data source.
+    * After your Language resource deploys, select **Go to resource**. You need the key and endpoint from the resource you create to connect to the API. Paste your key and endpoint into the code later in the quickstart.
+* Create a Language resource with [Azure CLI](../../../multi-service-resource.md?pivots=azcli) and provide the following properties: `--api-properties qnaAzureSearchEndpointId=/subscriptions/<azure-subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.Search/searchServices/<azure-search-service-name> qnaAzureSearchEndpointKey=<azure-search-service-auth-key>`
+* An existing project to query. If you don't have a project, you can follow the instructions in the [**Language Studio quickstart**](../quickstart/sdk.md). Or add a project that uses this [Surface User Guide URL](https://download.microsoft.com/download/7/B/1/7B10C82E-F520-4080-8516-5CF0D803EEE0/surface-book-user-guide-EN.pdf) as a data source.
 
 
 
@@ -73,19 +73,19 @@ dotnet add package Azure.AI.Language.QuestionAnswering
 
 #### Generate an answer from a project
 
-The example below will allow you to query a project using `GetAnswers` to get an answer to your question.
+The following example allows you to query a project using `GetAnswers` to get an answer to your question.
 
-You will need to update the code below and provide your own values for the following variables.
+You need to update the code and provide your own values for the following variables:
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `endpoint`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`|
+| `endpoint`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/`|
 | `credential` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys always for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `projectName` | The name of your custom question answering project.|
-| `deploymentName`             | There are two possible values: `test`, and `production`. `production` is dependent on you having deployed your project from **Language Studio** > **question answering** > **Deploy project**.|
+| `deploymentName`             | There are two possible values: `test`, and `production`. `production` is dependent on you deployed your project from **Language Studio** > **question answering** > **Deploy project**.|
 
 > [!IMPORTANT]
-> Remember to remove the key from your code when you're done, and never post it publicly. For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). See the Azure AI services [security](../../../security-features.md) article for more information.
+> Remember to remove the key from your code when you're done, and never post it publicly. For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information, see [Azure AI services security](../../../security-features.md).
 
 From the project directory, open the *program.cs* file and replace with the following code:
 
@@ -124,38 +124,38 @@ namespace question_answering
 }
 ```
 
-While we are hard coding the variables for our example. For production, consider using a secure way of storing and accessing your credentials. For example, [Azure key vault](/azure/key-vault/general/overview) provides secure key storage.
+While we're hard coding the variables for our example. For production, consider using a secure way of storing and accessing your credentials. For example, [Azure key vault](/azure/key-vault/general/overview) provides secure key storage.
 
-After updating `Program.cs` with the code above and substituting in the correct variable values. Run the application with the `dotnet run` command from your application directory.
+After updating `Program.cs` and substituting in the correct variable values. Run the application with the `dotnet run` command from your application directory.
 
 ```console
 dotnet run
 ```
 
-The response will look as follows:
+The response looks as follows:
 
 ```console
 Q: How much battery life do I have left?
 A: If you want to see how much battery you have left, go to **Start  **> **Settings  **> **Devices  **> **Bluetooth & other devices  **, then find your pen. The current battery level will appear under the battery icon.
 ```
 
-For information on how confident custom question answering is that this is the correct response add an additional print statement underneath the existing print statements:
+For information on confidence scores, add the following print statement underneath the existing print statements:
 
 ```csharp
 Console.WriteLine($"Q:{question}");
 Console.WriteLine($"A:{answer.Answer}");
 Console.WriteLine($"({answer.Confidence})"); // add this line
 ```
 
-If you execute `dotnet run` again, you will now receive a result with a confidence score:
+If you execute `dotnet run` again, you now receive a result with a confidence score:
 
 ```console
 Q:How much battery life do I have left?
 A:If you want to see how much battery you have left, go to **Start  **> **Settings  **> **Devices  **> **Bluetooth & other devices  **, then find your pen. The current battery level will appear under the battery icon.
 (0.9185)
 ```
 
-The confidence score returns a value between 0 and 1. You can think of this like a percentage and multiply by 100 so a confidence score of 0.9185 means custom question answering is 91.85% confident this is the correct answer to the question based on the project.
+Consider the confidence score as a percentage by multiplying it by 100. For example, a confidence score of 0.9185 indicates that the custom question-answering system is 91.85% confident that its response is correct based on the project information.
 
 If you want to exclude answers where the confidence score falls below a certain threshold, you use  `AnswerOptions` to add the `ConfidenceScoreThreshold` property.
 
@@ -168,7 +168,7 @@ options.ConfidenceThreshold = 0.95; //Add this line
 Response<AnswersResult> response = client.GetAnswers(question, project, options); //Add the additional options parameter
 ```
 
-Since we know from our previous execution of the code that our confidence score is: `.9185` setting the threshold to `.95` will result in the [default answer](../how-to/change-default-answer.md) being returned.
+Since we know from our previous execution of the code that our confidence score is: `.9185` setting the threshold to `.95` results in the [default answer](../how-to/change-default-answer.md) being returned.
 
 ```console
 Q:How much battery life do I have left?
@@ -198,7 +198,7 @@ namespace questionansweringcsharp
         static void Main(string[] args)
         {
 
-            Uri endpoint = new Uri("https://{YOUR-ENDPOINT}.api.cognitive.microsoft.com/");
+            Uri endpoint = new Uri("https://{YOUR-ENDPOINT}.cognitiveservices.azure.com/");
             AzureKeyCredential credential = new AzureKeyCredential("YOUR-LANGUAGE-RESOURCE-KEY");
             QuestionAnsweringClient client = new QuestionAnsweringClient(endpoint, credential);
 
@@ -237,7 +237,7 @@ namespace questionansweringcsharp
 }
 ```
 
-To run the code above, replace the `Program.cs` with the contents of the script block above and modify the `endpoint` and `credential` variables to correspond to the language resource you created as part of the prerequisites.
+To run the code, replace the `Program.cs` with the contents of the script block and modify the `endpoint` and `credential` variables to correspond to the language resource you created as part of the prerequisites.
 
 In this case, we iterate through all responses and only return the response with the highest confidence score that is greater than 0.9. To understand more about the options available with `GetAnswersFromText`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDKに関するドキュメントの更新"
}
```

### Explanation
この変更は、C# SDKに関するドキュメントを更新したもので、以下の主要なポイントが含まれています：

- 最終更新日が2025年6月30日から2025年8月7日に変更されており、情報が最新のものに更新されています。
- APIエンドポイントのURLが`api.cognitive.microsoft.com`から`cognitiveservices.azure.com`に変更され、現在のAzureサービスへ適合しています。
- ドキュメント内の表現が改善され、全体の読みやすさが向上しています。特に手順ごとの指示が明確になり、ユーザーが必要なアクションを理解しやすくなっています。
- 信頼度スコアの説明が明確化され、スコアの解釈が具体的になっています。ユーザーは信頼度スコアを理解しやすく、適切に利用できるようになっています。
- 一部のセクションで文言の整理が行われ、冗長な表現が削除されています。たとえば、記述がより直接的で、無駄が省かれています。

この更新により、C# SDKを使用してカスタム質問応答システムを構築する際のガイダンスが強化され、利用者はよりスムーズに手続きを進めることができるようになります。全体として、ドキュメントはより明確で、実用的な情報が提供されています。

## articles/ai-services/language-service/question-answering/includes/sdk-python.md{#item-33436a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: This quickstart shows how to get started with the custom question a
 ms.topic: include
 author: laujan
 ms.author: lajanuar
-ms.date: 06/30/2025
+ms.date: 08/07/2025
 ---
 
 Use this quickstart for the custom question answering client library for Python to:
@@ -13,7 +13,7 @@ Use this quickstart for the custom question answering client library for Python
 * Get an answer from a body of text that you send along with your question.
 * Get the confidence score for the answer to your question.
 
-[Package (PyPI)][questionanswering_pypi_package] | [Additional samples][questionanswering_samples] | [Library source code][questionanswering_client_src] 
+[Package (PyPI)][questionanswering_pypi_package] | [Samples][questionanswering_samples] | [Library source code][questionanswering_client_src] 
 
 [questionanswering_client_src]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/cognitivelanguage/azure-ai-language-questionanswering/
 [questionanswering_pypi_package]: https://pypi.org/project/azure-ai-language-questionanswering/
@@ -24,9 +24,9 @@ Use this quickstart for the custom question answering client library for Python
 * Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services)
 * [Python 3.x](https://www.python.org/)
 * Custom question answering requires a [Language resource](https://portal.azure.com/?quickstart=true#create/Microsoft.CognitiveServicesTextAnalytics) with the custom question answering feature enabled to generate an API key and endpoint.
-	* After your Language resource deploys, select **Go to resource**. You need the key and endpoint from the resource you create to connect to the API. Paste your key and endpoint into the code below later in the quickstart.
-* To create a Language resource with [Azure CLI](../../../multi-service-resource.md?pivots=azcli) provide the following other properties: `--api-properties qnaAzureSearchEndpointId=/subscriptions/<azure-subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.Search/searchServices/<azure-search-service-name> qnaAzureSearchEndpointKey=<azure-search-service-auth-key>`
-* An existing project to query. If you have not set up a project, you can follow the instructions in the [**Language Studio quickstart**](../quickstart/sdk.md). Or add a project that uses this [Surface User Guide URL](https://download.microsoft.com/download/7/B/1/7B10C82E-F520-4080-8516-5CF0D803EEE0/surface-book-user-guide-EN.pdf) as a data source.
+    * After your Language resource deploys, select **Go to resource**. You need the key and endpoint from the resource you create to connect to the API. Paste your key and endpoint into the code later in the quickstart.
+* Create a Language resource with [Azure CLI](../../../multi-service-resource.md?pivots=azcli) and provide the following properties: `--api-properties qnaAzureSearchEndpointId=/subscriptions/<azure-subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.Search/searchServices/<azure-search-service-name> qnaAzureSearchEndpointKey=<azure-search-service-auth-key>`
+* An existing project to query. If you don't have a project, you can follow the instructions in the [**Language Studio quickstart**](../quickstart/sdk.md). Or add a project that uses this [Surface User Guide URL](https://download.microsoft.com/download/7/B/1/7B10C82E-F520-4080-8516-5CF0D803EEE0/surface-book-user-guide-EN.pdf) as a data source.
 
 
 
@@ -46,16 +46,16 @@ pip install azure-ai-language-questionanswering
 
 ### Generate an answer from a project
 
-The example below will allow you to query a project using get_answers to get an answer to your question. You can copy this code into a dedicated .py file or into a cell in [Jupyter Notebook/Lab](https://jupyter.org/).
+The example allows you to query a project using get_answers to get an answer to your question. You can copy this code into a dedicated .py file or into a cell in [Jupyter Notebook/Lab](https://jupyter.org/).
 
-You need to update the code below and provide your own values for the following variables.
+You need to update the code and provide your own values for the following variables.
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `endpoint`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.api.cognitive.microsoft.com/`|
+| `endpoint`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. An example endpoint is: `https://southcentralus.cognitiveservices.azure.com/`|
 | `credential` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either Key1 or Key2. Always having two valid keys always for secure key rotation with zero downtime. Alternatively you can find the value in **Language Studio** > **question answering** > **Deploy project** > **Get prediction URL**. The key value is part of the sample request.|
 | `knowledge_base_project` | The name of your question answering project.|
-| `deployment`             | There are two possible values: `test`, and `production`. `production` is dependent on you having deployed your project from **Language Studio** > **question answering** > **Deploy project**.|
+| `deployment`             | There are two possible values: `test`, and `production`. `production`.|
 
 > [!IMPORTANT]
 > Remember to remove the key from your code when you're done, and never post it publicly. For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information, see the Azure AI services [security article](../../../security-features.md).
@@ -64,7 +64,7 @@ You need to update the code below and provide your own values for the following
 from azure.core.credentials import AzureKeyCredential
 from azure.ai.language.questionanswering import QuestionAnsweringClient
 
-endpoint = "https://{YOUR-ENDPOINT}.api.cognitive.microsoft.com/"
+endpoint = "https://{YOUR-ENDPOINT}.cognitiveservices.azure.com/"
 credential = AzureKeyCredential("{YOUR-LANGUAGE-RESOURCE-KEY}")
 knowledge_base_project = "{YOUR-PROJECT-NAME}"
 deployment = "production"
@@ -87,30 +87,30 @@ if __name__ == '__main__':
 
 While we're hard coding the variables for our example. For production, consider using a secure way of storing and accessing your credentials. For example, [Azure key vault](/azure/key-vault/general/overview) provides secure key storage.
 
-When you run the code above, if you're using the data source from the prerequisites you get an answer that looks as follows:
+When you run the code, if you're using the data source from the prerequisites you get an answer that looks as follows:
 
 ```
 Q: How much battery life do I have left?
 A: If you want to see how much battery you have left, go to **Start  **> **Settings  **> **Devices  **> **Bluetooth & other devices  **, then find your pen. The current battery level will appear under the battery icon.
 ```
 
-For information on how confident custom question answering is that this is the correct response add another print statement underneath the existing print statements:
+For information on confident scores add the following print statements:
 
 ```python
 print("Q: {}".format(question))
 print("A: {}".format(output.answers[0].answer))
 print("Confidence Score: {}".format(output.answers[0].confidence)) # add this line 
 ```
 
-You'll now receive a result with a confidence score:
+You receive a result with a confidence score:
 
 ```
 Q: How much battery life do I have left?
 A: If you want to see how much battery you have left, go to **Start  **> **Settings  **> **Devices  **> **Bluetooth & other devices  **, then find your pen. The current battery level will appear under the battery icon.
 Confidence Score: 0.9185
 ```
 
-The confidence score returns a value between 0 and 1. You can think of this like a percentage and multiply by 100 so a confidence score of 0.9185 means custom question answering is 91.85% confident this is the correct answer to the question based on the project.
+Consider the confidence score as a percentage by multiplying it by 100. For example, a confidence score of 0.9185 indicates that the custom question-answering system is 91.85% confident that its response is correct based on the project information.
 
 If you want to exclude answers where the confidence score falls below a certain threshold, you can modify the AnswerOptions to add the `confidence_threshold` parameter.
 
@@ -145,7 +145,7 @@ from azure.core.credentials import AzureKeyCredential
 from azure.ai.language.questionanswering import QuestionAnsweringClient
 from azure.ai.language.questionanswering import models as qna
 
-endpoint = "https://{YOUR-ENDPOINT}.api.cognitive.microsoft.com/"
+endpoint = "https://{YOUR-ENDPOINT}.cognitiveservices.azure.com/"
 credential = AzureKeyCredential("YOUR-LANGUAGE-RESOURCE-KEY")
 
 def main():
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python SDKに関するドキュメントの更新"
}
```

### Explanation
この変更は、Python SDKに関するドキュメントの修正を含んでおり、以下の重要なポイントがあります：

- 最終更新日が2025年6月30日から2025年8月7日に変更され、情報が最新のものに更新されています。
- APIエンドポイントのURLが`api.cognitive.microsoft.com`から`cognitiveservices.azure.com`に変更され、最新のAzureサービスに適合しています。
- 表現の整理が行われ、説明や手順がより明確になっています。特に、ユーザーが必要なアクションを理解しやすいように構成されています。
- 信頼度スコアの説明が具体化され、利用者がスコアをどのように解釈するべきかがより明確に示されています。
- 一部の文言が改善され、冗長な表現が削除されることで、全体の流れがスムーズになっています。

この更新により、Python SDKを使用したカスタム質問応答システムの利用に関するガイダンスが強化され、ユーザーがより容易に手続きを進めることができるようになっています。全体として、ドキュメントはより明確で、実用的な情報が提供されています。

## articles/ai-services/language-service/question-answering/tutorials/multiple-domains.md{#item-323a1c}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,11 @@
 ---
-title: "Tutorial: Create a FAQ bot for multiple categories with Azure AI Bot Service"
+title: "Tutorial: Create an FAQ bot for multiple categories with Azure AI Bot Service"
 description: In this tutorial, create a no code FAQ Bot for production use cases with custom question answering and Azure AI Bot Service.
 ms.service: azure-ai-language
 ms.topic: tutorial
 author: laujan
 ms.author: lajanuar
-ms.date: 06/21/2025
+ms.date: 08/07/2025
 ms.custom: language-service-question-answering, cogserv-non-critical-language
 ---
 
@@ -18,36 +18,36 @@ In this tutorial, you learn how to:
 > * Create a separate project for each domain
 > * Create a separate language resource for each domain
 
-When building a FAQ bot, you may encounter use cases that require you to address queries across multiple domains. Let's say the marketing team at Microsoft wants to build a customer support bot that answers common user queries on multiple Surface Products. For the sake of simplicity here, we will be using two FAQ URLs, [Surface Pen](https://support.microsoft.com/surface/how-to-use-your-surface-pen-8a403519-cd1f-15b2-c9df-faa5aa924e98), and [Surface Earbuds](https://support.microsoft.com/surface/use-surface-earbuds-aea108c3-9344-0f11-e5f5-6fc9f57b21f9) to create the project.
+When building an FAQ bot, you may encounter use cases that require you to address queries across multiple domains. Let's say the marketing team at Microsoft wants to build a customer support bot that answers common user queries on multiple Surface Products. For the sake of simplicity here, we use two FAQ URLs, [Surface Pen](https://support.microsoft.com/surface/how-to-use-your-surface-pen-8a403519-cd1f-15b2-c9df-faa5aa924e98), and [Surface Earbuds](https://support.microsoft.com/surface/use-surface-earbuds-aea108c3-9344-0f11-e5f5-6fc9f57b21f9) to create the project.
 
 ## Create project with domain specific metadata
 
-The content authors can use documents to extract question answer pairs or add custom question answer pairs to the project. In order to group these question and answers into specific domains or categories, you can add metadata.
+The content authors can use documents to extract question answer pairs or add custom question answer pairs to the project. In order to group the question and answers into specific domains or categories, you can add metadata.
 
 For the bot on Surface products, you can take the following steps to create a bot that answers queries for both product types:
 
-1. Add the following FAQ URLs as sources by selecting **Add source** > **URLs** > and then **Add all** once you have added each of the URLS below:
+1. Add the following FAQ URLs as sources by selecting **Add source** > **URLs** > and then **Add all** once you add each of the URLs:
    
    [Surface Pen FAQ](https://support.microsoft.com/surface/how-to-use-your-surface-pen-8a403519-cd1f-15b2-c9df-faa5aa924e98)<br>[Surface Earbuds FAQ](https://support.microsoft.com/surface/use-surface-earbuds-aea108c3-9344-0f11-e5f5-6fc9f57b21f9)
 
     >[!div class="mx-imgBorder"]
     >[![Screenshot of add URL UI.](../media/multiple-domains/add-url.png)](../media/multiple-domains/add-url.png#lightbox)
 
-2. In this project, we have question answer pairs on two products and we would like to distinguish between them such that we can search for responses among question and answers for a given product. In order to do this, we could update the metadata field for the question answer pairs.
+1. In this project, we have sets of question-and-answer pairs for two different products. Our goal is to clearly differentiate between these products so that users can search for relevant responses within the question and answer sets for a specific product.
 
-   As you can see in the example below, we have added a metadata with **product** as key and **surface_pen** or **surface_earbuds** as values wherever applicable. You can extend this example to extract data on multiple products and add a different value for each product.
+  In the example, we added a metadata with **product** as key and **surface_pen** or **surface_earbuds** as values wherever applicable. You can extend this example to extract data on multiple products and add a different value for each product.
 
    >[!div class="mx-imgBorder"]
    >[![Screenshot of metadata example.](../media/multiple-domains/product-metadata.png)](../media/multiple-domains/product-metadata.png#lightbox)
 
-4. Now, in order to restrict the system to search for the response across a particular product you would need to pass that product as a filter in the custom question answering REST API.
+1. Now, in order to restrict the system to search for the response across a particular product you would need to pass that product as a filter in the custom question answering REST API.
 
     The REST API prediction URL can be retrieved from the Deploy project pane:
 
    >[!div class="mx-imgBorder"]
    >[![Screenshot of the Deploy project page with the prediction URL displayed.](../media/multiple-domains/prediction-url.png)](../media/multiple-domains/prediction-url.png#lightbox)
 
-    In the JSON body for the API call, we have passed *surface_pen* as value for the metadata *product*. So, the system will only look for the response among the QnA pairs with the same metadata.
+    In the JSON body for the API call, we passed *surface_pen* as value for the metadata *product*. So, the system only looks for the response among the QnA pairs with the same metadata.
 
     ```json
         {
@@ -73,7 +73,7 @@ For the bot on Surface products, you can take the following steps to create a bo
 
     You can obtain metadata value based on user input in the following ways: 
 
-    * Explicitly take the domain as input from the user through the bot client. For instance as shown below, you can take product category as input from the user when the conversation is initiated.
+    * Explicitly take the domain as input from the user through the bot client. For instance, you can take the product category as input from the user when the conversation is initiated.
 
       ![Take metadata input](../media/multiple-domains/explicit-metadata-input.png)
 
@@ -93,10 +93,10 @@ You can add up to 50000 question answer pairs to a single project. If your data
 
 You can also create a separate project for each domain and maintain the projects separately. All APIs require for the user to pass on the project name to make any update to the project or fetch an answer to the user's question.  
 
-When the user question is received by the service, you would need to pass on the `projectName` in the REST API endpoint shown to fetch a response from the relevant project. You can locate the URL in the **Deploy project** page under **Get prediction URL**:
+When the service receives the user question, you need to pass on the `projectName` in the REST API endpoint shown to fetch a response from the relevant project. You can locate the URL in the **Deploy project** page under **Get prediction URL**:
 
-`https://southcentralus.api.cognitive.microsoft.com/language/:query-knowledgebases?projectName=Test-Project-English&api-version=2021-10-01&deploymentName=production`
+`https://southcentralus.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=Test-Project-English&api-version=2021-10-01&deploymentName=production`
 
 ## Create a separate language resource for each domain
 
-Let's say the marketing team at Microsoft wants to build a customer support bot that answers user queries on Surface and Xbox products. They plan to assign distinct teams to access projects on Surface and Xbox. In this case, it is advised to create two custom question answering resources - one for Surface and another for Xbox. You can however define distinct roles for users accessing the same resource.
+Let's say the marketing team at Microsoft wants to build a customer support bot that answers user queries on Surface and Xbox products. They plan to assign distinct teams to access projects on Surface and Xbox. In this case, you should create two custom question answering resources—one for Surface and another for Xbox. You can define distinct roles for users accessing the same resource.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "複数のドメインを持つFAQボット作成に関するチュートリアルの更新"
}
```

### Explanation
この変更は、複数のドメインを持つFAQボット作成に関するチュートリアルのドキュメントを更新したもので、以下の重要なポイントを含んでいます：

- 最終更新日が2025年6月21日から2025年8月7日に変更され、情報が最新のものに更新されています。
- タイトルの表現が「Create a FAQ bot」から「Create an FAQ bot」に修正され、文法的に正しくなっています。
- FAQボットに関連する手順や説明が明確化され、冗長な表現が削除されました。特に「質問と答え」を「質問と回答」とするなど、統一感が持たせられ、ユーザーが内容をより理解しやすくなっています。
- APIのエンドポイントに関する指示が更新され、URLが最新の形式に修正されています（`api.cognitive.microsoft.com`から`cognitiveservices.azure.com`へ）。
- ユーザーからの入力を明示的に取得する際の具体例が追加され、実際の使用方法がより具体的に説明されています。

この更新により、複数のドメインに対応したFAQボットを作成するためのガイダンスが強化され、ユーザーが手続きをよりスムーズに進めることができるようになっています。全体として、ドキュメントはより明確で、実用的な情報が提供されています。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -503,11 +503,11 @@ items:
         href: personally-identifiable-information/how-to/redact-conversation-pii.md
       - name: Redact PII from native documents
         href: personally-identifiable-information/how-to/redact-document-pii.md
-      - name: Use containers
+      - name:  Adapt PII to your domain
         href: personally-identifiable-information/how-to/adapt-to-domain-pii.md
-      - name: Adapt PII to your domain
+      - name: Use Docker containers
         items:
-          - name: Use Docker containers
+          - name: Install and run containers
             href: personally-identifiable-information/how-to/use-containers.md
           - name: Configure containers
             href: concepts/configure-containers.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PIIに関するTOCの更新"
}
```

### Explanation
この変更は、個人情報（PII）に関するドキュメントの目次（TOC）を更新したもので、以下の重要なポイントを含んでいます：

- 「Use containers」という項目が「Adapt PII to your domain」に変更され、内容がより具体的で関連性のあるものになっています。
- 「Adapt PII to your domain」の項目が「Use Docker containers」に修正されて内容の精度が向上しました。
- サブメニューの「Use Docker containers」が「Install and run containers」に変更され、具体的な行動を示す表現に改善されています。
- これにより、利用者が具体的にどのような手順を踏むのかが分かりやすくなります。

全体として、これらの変更はドキュメントの目次をより明確にし、読者が求める情報へと迅速にアクセスできるようにしています。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -56,7 +56,7 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 **PII detection enhancements**. Azure AI Language introduces new customization and entity subtype features for PII detection:
 *  [Customize PII detection using your own regex](personally-identifiable-information/how-to/adapt-to-domain-pii.md#customizing-pii-detection-using-your-own-regex-only-available-for-text-pii-container) (Text PII container only).
 *  [Specify values to exclude from PII output](personally-identifiable-information/how-to/adapt-to-domain-pii.md#customizing-pii-output-by-specifying-values-to-exclude).
-*  [Use entity synonyms for tailored PII detection](personally-identifiable-information/how-to/adapt-to-domain-pii.md#api-schema-for-the-entitysynoyms-parameter).
+*  [Use entity synonyms for tailored PII detection](personally-identifiable-information/how-to/adapt-to-domain-pii.md#api-schema-for-the-entitysynonyms-parameter).
 
 **Enhanced CLU and CQA Capabilities in Azure AI Foundry**. Azure AI Foundry now offers enhanced capabilities for fine-tuning with custom conversational language understanding (CLU) and conversational question-and-answer (CQA) AI features:
 *    CLU and CQA authoring tools are now available in Azure AI Foundry.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Languageに関する「新機能」ドキュメントの内容を更新したもので、以下の主なポイントが挙げられます：

- PII（個人情報）検出の機能に関連する項目の更新が行われました。「Use entity synonyms for tailored PII detection」という項目の文言が修正され、具体的には「entitysynoyms」から「entitysynonyms」に変更されています。この修正は、正しいパラメータ名を反映したものとなっています。
- これにより、ユーザーがAPIを利用する際に正確な情報を得られるようになり、混乱を避けることができます。

全体的に、今回の更新は新しい機能や変更点についての情報をより正確にユーザーに提供するための重要な改善です。情報の明確性と正確性が向上しており、利用者が最新の機能を理解しやすくなっています。


