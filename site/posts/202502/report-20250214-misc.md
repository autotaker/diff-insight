---
date: '2025-02-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:81f79a9...MicrosoftDocs:f2b9798
summary: このコード差分では、主にドキュメントの更新日付やリンクの修正、APIサンプルの正確性向上が行われました。また、C# SDKとJava SDKのバグ修正により、開発者にとって使いやすさが向上しています。特にデータ構造に関する命名の一貫性が確保されており、ユーザーにより明確な情報が提供されています。新機能の追加はありませんが、全体的にユーザビリティが改善されています。破壊的な変更はなく、プロパティ名の変更には適応が必要な場合があります。更新後、ドキュメントやSDKの質が向上し、ユーザーが最新情報にアクセスしやすくなっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:81f79a9...MicrosoftDocs:f2b9798){target="_blank"}

# ハイライト

このコード差分における主なハイライトは、ドキュメントの更新日付やリンクの修正、APIサンプルの正確性向上などが含まれています。また、C# SDKとJava SDK両方でのバグ修正も行われており、開発者がこれらのツールをより使いやすくなる改善がされています。特に、データ構造に関する命名の一貫性が確認され、ユーザーにより明確で誤解のない情報が提供されるようになっています。

## 新機能
特記すべき新機能の追加はありませんが、これらの更新によってドキュメントやSDKの使いやすさが向上しました。

## 破壊的変更
破壊的な変更は報告されていません。ただし、プロパティ名の変更があるため、名前変更に伴いコードの適応が必要な場合があります。

## その他の更新
- ドキュメントの日付やリンクの更新
- クエリフィールドに関するAPIサンプルや説明文の更新
- SDKの命名規則の修正とデバッグメッセージの更新

# インサイト

この更新では、ドキュメントとソフトウェア両方の質と整合性を向上させるための数々の修正が行われました。ドキュメントインテリジェンスに関する更新は、日付変更とAPIサンプルの正確性を重視しており、ユーザーが最新の状況についての情報を得やすくなっています。これにより、ドキュメントが最新の標準を満たしつつ、容易にユーザーに情報を提供できるようになっています。

C#およびJava SDKのバグ修正においては、特にデータ構造を参照する際の命名規則の統一が行われました。この変更は、開発者がより直感的にコードを書くことができ、かつ抜け漏れのないデバッグ情報を得られるようにするものです。このような修正は、特に複数のSDKを横断して開発している場合に重要です。各SDKでプロパティ名が一致していることにより、移植性を高め、開発時間を短縮することができます。

さらに、Azure Key Vaultに関するリンクのアップデートを含む環境変数に関するドキュメントの更新や、PIIサポート言語情報の書き換えも重要です。これにより、Azureサービスを利用するユーザーが最新のセキュリティ及びデータ保護の指針にアクセスしやすく見直されています。

今後の利用を見越した準備、ユーザビリティの向上を意図したこの差分は、すべてのユーザーにとって有益といえます。特に、更新された日付のみの修正であっても、コミュニケーション手段としての日付整理は容易な情報把握に寄与するという効果的な実践がなされていると言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [query-fields.md](#item-c58523) | minor update | クエリフィールドのドキュメント更新 | modified | 6 | 6 | 12 | 
| [csharp-sdk.md](#item-b72ebd) | bug fix | C# SDKのバグ修正 | modified | 10 | 10 | 20 | 
| [java-sdk.md](#item-65f910) | bug fix | Java SDKのバグ修正 | modified | 6 | 6 | 12 | 
| [csharp-sdk.md](#item-ee69c7) | bug fix | C# SDKのバグ修正 | modified | 16 | 16 | 32 | 
| [java-sdk.md](#item-166b2e) | bug fix | Java SDKのバグ修正 | modified | 8 | 8 | 16 | 
| [environment-variables.md](#item-7b1a27) | minor update | Azure Key Vaultのリンク更新 | modified | 1 | 1 | 2 | 
| [language-support.md](#item-d332b1) | minor update | PIIサポート言語情報の更新 | modified | 2 | 6 | 8 | 
| [azure-openai-in-ai-studio.md](#item-07639b) | minor update | 更新された文書の日付 | modified | 1 | 1 | 2 | 
| [management-center.md](#item-6e44f6) | minor update | 管理センター文書の日付更新 | modified | 1 | 1 | 2 | 
| [create-hub-project-sdk.md](#item-8c3e99) | minor update | HubプロジェクトSDKに関する文書の更新 | modified | 36 | 19 | 55 | 
| [healthcare-ai-models.md](#item-12fcfc) | minor update | ヘルスケアAIモデルに関する文書の更新 | modified | 10 | 10 | 20 | 
| [deploy-web-app.png](#item-189250) | minor update | チャットチュートリアル用画像の更新 | modified | 0 | 0 | 0 | 
| [deploy-chat-web-app.md](#item-987845) | minor update | デプロイチャットWebアプリチュートリアルの更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/concept/query-fields.md{#item-c58523}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 11/19/2024
+ms.date: 02/12/2025
 ms.author: nitinme
 monikerRange: 'doc-intel-4.0.0'
 ---
@@ -15,7 +15,7 @@ monikerRange: 'doc-intel-4.0.0'
 
 # Document Intelligence query field extraction
 
-**Document Intelligence now supports query field to extend the schema of any prebuilt model to extract the specific fields you need. Query fields can also be added to layout to extract fields in addition to structure from forms or documents.
+Document Intelligence now supports query field to extend the schema of any prebuilt model to extract the specific fields you need. Query fields can also be added to layout to extract fields in addition to structure from forms or documents.
 > [!NOTE]
 >
 > Document Intelligence Studio query field extraction is currently available with layout and prebuilt models, excluding the UX.Tax prebuilt models.
@@ -45,18 +45,18 @@ For query field extraction, specify the fields you want to extract and Document
 * In addition to the query fields, the response includes the model output. For a list of features or schema extracted by each model, see [model analysis features](../model-overview.md#model-analysis-features).
 
 
-## Query fields REST API request**
+## Query fields REST API request
 
-Use the query fields feature with the [general document model](../prebuilt/general-document.md), and add fields to the extraction process without having to train a custom model:
+Use the query fields feature with the [prebuilt layout](../prebuilt/layout.md) model, and add fields to the extraction process without having to train a custom model:
 
 ```http
-POST https://{endpoint}/documentintelligence/documentModels/prebuilt-layout:analyze?api-version=2024-02-29-preview&features=queryFields&queryFields=Terms,PaymentDate HTTP/1.1
+POST https://{endpoint}/documentintelligence/documentModels/prebuilt-layout:analyze?api-version=2024-11-30&features=queryFields&queryFields=OurReference,BookingDate HTTP/1.1
 Host: *.cognitiveservices.azure.com
 Content-Type: application/json
 Ocp-Apim-Subscription-Key:
 
 {
-  "urlSource": "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"
+  "urlSource": "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/layout.png"
 }
 ``````
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリフィールドのドキュメント更新"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスにおけるクエリフィールドに関する情報の更新を目的としています。主な変更には、日付の更新とAPIリクエストの例の修正があります。具体的には、`ms.date`が2024年11月19日から2025年2月12日に変更され、REST APIリクエストのバージョンも2024年2月29日から2024年11月30日に更新されています。

また、クエリフィールドに関する説明やAPIリクエストのサンプル内でも使われるフィールド名が更新され、より正確な内容となるように改善されています。これにより、ユーザーは最新の情報に基づいてクエリフィールドを利用することができ、ドキュメントは最新の状態を反映しています。

## articles/ai-services/document-intelligence/how-to-guides/includes/v4-0/csharp-sdk.md{#item-b72ebd}

<details>
<summary>Diff</summary>
````diff
@@ -129,9 +129,9 @@ foreach (DocumentPage page in result.Pages)
 
         Console.WriteLine($"    Its bounding polygon (points ordered clockwise):");
 
-        for (int j = 0; j < line.BoundingPolygon.Count; j++)
+        for (int j = 0; j < line.Polygon.Count; j++)
         {
-            Console.WriteLine($"      Point {j} => X: {line.BoundingPolygon[j].X}, Y: {line.BoundingPolygon[j].Y}");
+            Console.WriteLine($"      Point {j} => X: {line.Polygon[j].X}, Y: {line.Polygon[j].Y}");
         }
     }
 }
@@ -196,9 +196,9 @@ foreach (DocumentPage page in result.Pages)
 
         Console.WriteLine($"    Its bounding polygon (points ordered clockwise):");
 
-        for (int j = 0; j < line.BoundingPolygon.Count; j++)
+        for (int j = 0; j < line.Polygon.Count; j++)
         {
-            Console.WriteLine($"      Point {j} => X: {line.BoundingPolygon[j].X}, Y: {line.BoundingPolygon[j].Y}");
+            Console.WriteLine($"      Point {j} => X: {line.Polygon[j].X}, Y: {line.Polygon[j].Y}");
         }
     }
 
@@ -209,9 +209,9 @@ foreach (DocumentPage page in result.Pages)
         Console.WriteLine($"  Selection Mark {i} is {selectionMark.State}.");
         Console.WriteLine($"    Its bounding polygon (points ordered clockwise):");
 
-        for (int j = 0; j < selectionMark.BoundingPolygon.Count; j++)
+        for (int j = 0; j < selectionMark.Polygon.Count; j++)
         {
-            Console.WriteLine($"      Point {j} => X: {selectionMark.BoundingPolygon[j].X}, Y: {selectionMark.BoundingPolygon[j].Y}");
+            Console.WriteLine($"      Point {j} => X: {selectionMark.Polygon[j].X}, Y: {selectionMark.Polygon[j].Y}");
         }
     }
 }
@@ -308,9 +308,9 @@ foreach (DocumentPage page in result.Pages)
 
         Console.WriteLine($"    Its bounding polygon (points ordered clockwise):");
 
-        for (int j = 0; j < line.BoundingPolygon.Count; j++)
+        for (int j = 0; j < line.Polygon.Count; j++)
         {
-            Console.WriteLine($"      Point {j} => X: {line.BoundingPolygon[j].X}, Y: {line.BoundingPolygon[j].Y}");
+            Console.WriteLine($"      Point {j} => X: {line.Polygon[j].X}, Y: {line.Polygon[j].Y}");
         }
     }
 
@@ -321,9 +321,9 @@ foreach (DocumentPage page in result.Pages)
         Console.WriteLine($"  Selection Mark {i} is {selectionMark.State}.");
         Console.WriteLine($"    Its bounding polygon (points ordered clockwise):");
 
-        for (int j = 0; j < selectionMark.BoundingPolygon.Count; j++)
+        for (int j = 0; j < selectionMark.Polygon.Count; j++)
         {
-            Console.WriteLine($"      Point {j} => X: {selectionMark.BoundingPolygon[j].X}, Y: {selectionMark.BoundingPolygon[j].Y}");
+            Console.WriteLine($"      Point {j} => X: {selectionMark.Polygon[j].X}, Y: {selectionMark.Polygon[j].Y}");
         }
     }
 }
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "C# SDKのバグ修正"
}
```

### Explanation
この変更は、C# SDKにおけるバグ修正を目的としています。具体的には、ポリゴンのバウンディングを参照する際のプロパティ名を変更することによって、コードの一貫性と明瞭性を向上させています。修正されたコードでは、`BoundingPolygon`プロパティが`Polygon`に置き換えられ、各ポイントの座標を出力する処理もそれに合わせて修正されています。

この修正により、C# SDKを利用する開発者にとって、影響を与える新しいプロパティ名に対する理解が容易になり、正しいデータの取得が確実になります。また、これに伴うコード内の出力メッセージも変更され、ユーザーがデバッグやロギングの際に受け取る情報が整合性を持つようになっています。全体として、この修正はSDKの使いやすさを向上させる重要な更新です。

## articles/ai-services/document-intelligence/how-to-guides/includes/v4-0/java-sdk.md{#item-65f910}

<details>
<summary>Diff</summary>
````diff
@@ -192,7 +192,7 @@ analyzeLayoutResult.getPages().forEach(documentPage -> {
   documentPage.getLines().forEach(documentLine ->
     System.out.printf("Line %s is within a bounding polygon %s.%n",
       documentLine.getContent(),
-      documentLine.getBoundingPolygon().toString()));
+      documentLine.getPolygon().toString()));
 
   // words
   documentPage.getWords().forEach(documentWord ->
@@ -258,7 +258,7 @@ analyzeLayoutResult.getPages().forEach(documentPage -> {
   documentPage.getLines().forEach(documentLine ->
     System.out.printf("Line %s is within a bounding polygon %s.%n",
       documentLine.getContent(),
-      documentLine.getBoundingPolygon().toString()));
+      documentLine.getPolygon().toString()));
 
   // words
   documentPage.getWords().forEach(documentWord ->
@@ -270,7 +270,7 @@ analyzeLayoutResult.getPages().forEach(documentPage -> {
   documentPage.getSelectionMarks().forEach(documentSelectionMark ->
     System.out.printf("Selection mark is '%s' and is within a bounding polygon %s with confidence %.2f.%n",
       documentSelectionMark.getSelectionMarkState().toString(),
-      getBoundingCoordinates(documentSelectionMark.getBoundingPolygon()),
+      getBoundingCoordinates(documentSelectionMark.getPolygon()),
       documentSelectionMark.getConfidence()));
 });
 
@@ -290,8 +290,8 @@ for (int i = 0; i < tables.size(); i++) {
 }
 
 // Utility function to get the bounding polygon coordinates.
-private static String getBoundingCoordinates(List < Point > boundingPolygon) {
-  return boundingPolygon.stream().map(point -> String.format("[%.2f, %.2f]", point.getX(),
+private static String getBoundingCoordinates(List < Point > Polygon) {
+  return Polygon.stream().map(point -> String.format("[%.2f, %.2f]", point.getX(),
     point.getY())).collect(Collectors.joining(", "));
 }
 
@@ -351,7 +351,7 @@ analyzeResult.getPages().forEach(documentPage -> {
   documentPage.getLines().forEach(documentLine ->
     System.out.printf("Line %s is within a bounding polygon %s.%n",
       documentLine.getContent(),
-      documentLine.getBoundingPolygon().toString()));
+      documentLine.getPolygon().toString()));
 
   // words
   documentPage.getWords().forEach(documentWord ->
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "Java SDKのバグ修正"
}
```

### Explanation
この変更は、Java SDKにおけるバグの修正を目的としています。具体的には、ドキュメントラインや選択マークのポリゴンを参照する際のプロパティ名を修正しています。`getBoundingPolygon()`メソッドが`getPolygon()`に置き換えられ、それに伴い関連する出力メッセージも更新されています。

これにより、コード内での整合性が向上し、開発者がドキュメントのポリゴンに関する情報を扱う際の混乱が軽減されます。また、バウンディングポリゴンに関するユーティリティ関数も併せて修正され、関数の引数名も一貫性が持たせられています。全体として、この修正はJava SDKの使用時に発生する可能性のある誤解を防ぐための重要な更新です。

## articles/ai-services/document-intelligence/quickstarts/includes/csharp-sdk.md{#item-ee69c7}

<details>
<summary>Diff</summary>
````diff
@@ -344,10 +344,10 @@ foreach (DocumentPage page in result.Pages)
         Console.WriteLine($"  Line {i} has content: '{line.Content}'.");
 
         Console.WriteLine($"    Its bounding box is:");
-        Console.WriteLine($"      Upper left => X: {line.BoundingPolygon[0].X}, Y= {line.BoundingPolygon[0].Y}");
-        Console.WriteLine($"      Upper right => X: {line.BoundingPolygon[1].X}, Y= {line.BoundingPolygon[1].Y}");
-        Console.WriteLine($"      Lower right => X: {line.BoundingPolygon[2].X}, Y= {line.BoundingPolygon[2].Y}");
-        Console.WriteLine($"      Lower left => X: {line.BoundingPolygon[3].X}, Y= {line.BoundingPolygon[3].Y}");
+        Console.WriteLine($"      Upper left => X: {line.Polygon[0].X}, Y= {line.Polygon[0].Y}");
+        Console.WriteLine($"      Upper right => X: {line.Polygon[1].X}, Y= {line.Polygon[1].Y}");
+        Console.WriteLine($"      Lower right => X: {line.Polygon[2].X}, Y= {line.Polygon[2].Y}");
+        Console.WriteLine($"      Lower left => X: {line.Polygon[3].X}, Y= {line.Polygon[3].Y}");
     }
 
     for (int i = 0; i < page.SelectionMarks.Count; i++)
@@ -356,10 +356,10 @@ foreach (DocumentPage page in result.Pages)
 
         Console.WriteLine($"  Selection Mark {i} is {selectionMark.State}.");
         Console.WriteLine($"    Its bounding box is:");
-        Console.WriteLine($"      Upper left => X: {selectionMark.BoundingPolygon[0].X}, Y= {selectionMark.BoundingPolygon[0].Y}");
-        Console.WriteLine($"      Upper right => X: {selectionMark.BoundingPolygon[1].X}, Y= {selectionMark.BoundingPolygon[1].Y}");
-        Console.WriteLine($"      Lower right => X: {selectionMark.BoundingPolygon[2].X}, Y= {selectionMark.BoundingPolygon[2].Y}");
-        Console.WriteLine($"      Lower left => X: {selectionMark.BoundingPolygon[3].X}, Y= {selectionMark.BoundingPolygon[3].Y}");
+        Console.WriteLine($"      Upper left => X: {selectionMark.Polygon[0].X}, Y= {selectionMark.Polygon[0].Y}");
+        Console.WriteLine($"      Upper right => X: {selectionMark.Polygon[1].X}, Y= {selectionMark.Polygon[1].Y}");
+        Console.WriteLine($"      Lower right => X: {selectionMark.Polygon[2].X}, Y= {selectionMark.Polygon[2].Y}");
+        Console.WriteLine($"      Lower left => X: {selectionMark.Polygon[3].X}, Y= {selectionMark.Polygon[3].Y}");
     }
 }
 
@@ -459,9 +459,9 @@ foreach (DocumentPage page in result.Pages)
 
         Console.WriteLine($"    Its bounding polygon (points ordered clockwise):");
 
-        for (int j = 0; j < line.BoundingPolygon.Count; j++)
+        for (int j = 0; j < line.Polygon.Count; j++)
         {
-            Console.WriteLine($"      Point {j} => X: {line.BoundingPolygon[j].X}, Y: {line.BoundingPolygon[j].Y}");
+            Console.WriteLine($"      Point {j} => X: {line.Polygon[j].X}, Y: {line.Polygon[j].Y}");
         }
     }
 
@@ -472,9 +472,9 @@ foreach (DocumentPage page in result.Pages)
         Console.WriteLine($"  Selection Mark {i} is {selectionMark.State}.");
         Console.WriteLine($"    Its bounding polygon (points ordered clockwise):");
 
-        for (int j = 0; j < selectionMark.BoundingPolygon.Count; j++)
+        for (int j = 0; j < selectionMark.Polygon.Count; j++)
         {
-            Console.WriteLine($"      Point {j} => X: {selectionMark.BoundingPolygon[j].X}, Y: {selectionMark.BoundingPolygon[j].Y}");
+            Console.WriteLine($"      Point {j} => X: {selectionMark.Polygon[j].X}, Y: {selectionMark.Polygon[j].Y}");
         }
     }
 }
@@ -542,9 +542,9 @@ foreach (DocumentPage page in result.Pages)
 
         Console.WriteLine($"    Its bounding polygon (points ordered clockwise):");
 
-        for (int j = 0; j < line.BoundingPolygon.Count; j++)
+        for (int j = 0; j < line.Polygon.Count; j++)
         {
-            Console.WriteLine($"      Point {j} => X: {line.BoundingPolygon[j].X}, Y: {line.BoundingPolygon[j].Y}");
+            Console.WriteLine($"      Point {j} => X: {line.Polygon[j].X}, Y: {line.Polygon[j].Y}");
         }
     }
 
@@ -555,9 +555,9 @@ foreach (DocumentPage page in result.Pages)
         Console.WriteLine($"  Selection Mark {i} is {selectionMark.State}.");
         Console.WriteLine($"    Its bounding polygon (points ordered clockwise):");
 
-        for (int j = 0; j < selectionMark.BoundingPolygon.Count; j++)
+        for (int j = 0; j < selectionMark.Polygon.Count; j++)
         {
-            Console.WriteLine($"      Point {j} => X: {selectionMark.BoundingPolygon[j].X}, Y: {selectionMark.BoundingPolygon[j].Y}");
+            Console.WriteLine($"      Point {j} => X: {selectionMark.Polygon[j].X}, Y: {selectionMark.Polygon[j].Y}");
         }
     }
 }
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "C# SDKのバグ修正"
}
```

### Explanation
この変更は、C# SDKのバグ修正を目的としています。具体的には、行や選択マークのバウンディングボックスを表示する際に使用されるプロパティ名を、`BoundingPolygon`から`Polygon`に変更しています。この修正により、出力される情報が一貫性を持つようになり、開発者にとっての可読性が向上します。

修正内容は、各行と選択マークのバウンディングボックスを計算し、その各点の座標を表示する部分に関するものです。変更の結果、ユーザーが受け取るコンソール出力が、正しいプロパティを参照し、一貫した形式で座標を表示できるようになっています。

この更新は、ユーザーがSDKを使用する際に直面する可能性のある混乱を軽減し、より明確なデバッグ情報を提供するための重要な措置です。全体として、この修正はC# SDKの信頼性を向上させます。

## articles/ai-services/document-intelligence/quickstarts/includes/java-sdk.md{#item-166b2e}

<details>
<summary>Diff</summary>
````diff
@@ -424,7 +424,7 @@ public class FormRecognizer {
       documentPage.getLines().forEach(documentLine ->
         System.out.printf("Line %s is within a bounding polygon %s.%n",
           documentLine.getContent(),
-          documentLine.getBoundingPolygon().toString()));
+          documentLine.getPolygon().toString()));
 
       // words
       documentPage.getWords().forEach(documentWord ->
@@ -436,7 +436,7 @@ public class FormRecognizer {
       documentPage.getSelectionMarks().forEach(documentSelectionMark ->
         System.out.printf("Selection mark is %s and is within a bounding polygon %s with confidence %.2f.%n",
           documentSelectionMark.getState().toString(),
-          documentSelectionMark.getBoundingPolygon().toString(),
+          documentSelectionMark.getPolygon().toString(),
           documentSelectionMark.getConfidence()));
     });
 
@@ -454,8 +454,8 @@ public class FormRecognizer {
     }
   }
   // Utility function to get the bounding polygon coordinates
-  private static String getBoundingCoordinates(List < Point > boundingPolygon) {
-    return boundingPolygon.stream().map(point -> String.format("[%.2f, %.2f]", point.getX(),
+  private static String getBoundingCoordinates(List < Point > Polygon) {
+    return Polygon.stream().map(point -> String.format("[%.2f, %.2f]", point.getX(),
       point.getY())).collect(Collectors.joining(", "));
   }
 }
@@ -556,7 +556,7 @@ public class FormRecognizer {
       documentPage.getLines().forEach(documentLine ->
         System.out.printf("Line '%s' is within a bounding polygon %s.%n",
           documentLine.getContent(),
-          getBoundingCoordinates(documentLine.getBoundingPolygon())));
+          getBoundingCoordinates(documentLine.getPolygon())));
 
       // words
       documentPage.getWords().forEach(documentWord ->
@@ -568,7 +568,7 @@ public class FormRecognizer {
       documentPage.getSelectionMarks().forEach(documentSelectionMark ->
         System.out.printf("Selection mark is '%s' and is within a bounding polygon %s with confidence %.2f.%n",
           documentSelectionMark.getSelectionMarkState().toString(),
-          getBoundingCoordinates(documentSelectionMark.getBoundingPolygon()),
+          getBoundingCoordinates(documentSelectionMark.getPolygon()),
           documentSelectionMark.getConfidence()));
     });
 
@@ -593,8 +593,8 @@ public class FormRecognizer {
   /**
    * Utility function to get the bounding polygon coordinates.
    */
-  private static String getBoundingCoordinates(List < Point > boundingPolygon) {
-    return boundingPolygon.stream().map(point -> String.format("[%.2f, %.2f]", point.getX(),
+  private static String getBoundingCoordinates(List < Point > Polygon) {
+    return Polygon.stream().map(point -> String.format("[%.2f, %.2f]", point.getX(),
       point.getY())).collect(Collectors.joining(", "));
   }
 }
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "Java SDKのバグ修正"
}
```

### Explanation
この変更は、Java SDKにおけるバグ修正を目的としています。具体的には、文書内の行や選択マークのバウンディングポリゴンを表すメソッドにおいて、`getBoundingPolygon()`から`getPolygon()`という新しいメソッドに変更されました。この修正により、コード内の整合性が高まり、誤解を招くことが軽減されます。

修正された箇所では、行や選択マークの内容とそのポリゴンの情報を出力するためのシステムメッセージが改善されています。また、バウンディングポリゴンの座標を取得するユーティリティ関数においても同様の改修が行われており、引数名がより一貫性を持たせるように変更されています。この変更は、開発者がバウンディングボックスに関する情報を処理しやすくするためのものです。

全体として、この修正はJava SDKの使いやすさと信頼性を向上させる重要な更新となります。

## articles/ai-services/language-service/includes/environment-variables.md{#item-7b1a27}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ To set the environment variable for your Language resource key, open a console w
 - To set the `LANGUAGE_KEY` environment variable, replace `your-key` with one of the keys for your resource.
 - To set the `LANGUAGE_ENDPOINT` environment variable, replace `your-endpoint` with the endpoint for your resource.
 
-[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv-expanded.md)]
 
 #### [Windows](#tab/windows)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Key Vaultのリンク更新"
}
```

### Explanation
この変更は、環境変数に関するドキュメントの更新です。具体的には、Azure Key Vaultに関する情報へのリンクを更新しています。以前のリンクは古いものでしたが、新しいリンク `microsoft-entra-id-akv-expanded.md` に置き換えられています。

この修正は、利用者がAzure Key Vaultの最新の情報や機能を簡単にアクセスできるようにするためのもので、リソースキーやエンドポイントの設定に関連するガイドラインを強化しています。

全体として、この変更はドキュメントの正確性を向上させ、ユーザーが正しい情報を取得しやすくするための重要な更新となります。

## articles/ai-services/language-service/personally-identifiable-information/language-support.md{#item-d332b1}

<details>
<summary>Diff</summary>
````diff
@@ -191,12 +191,8 @@ Use this article to learn which natural languages are supported by the text PII,
 
 ## PII language support
 
-| Language              | Language code | Notes              |
-|-----------------------|---------------|--------------------|
-|German                 |`de`           |                    |
-|English                |`en`           |                    |
-|Spanish                |`es`           |                    |
-|French                 |`fr`           |                    |
+The Generally Available Conversational PII serivce currently supports English. Preview model version `2023-04-15-preview` supports English, German, Spanish, and French. 
+
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PIIサポート言語情報の更新"
}
```

### Explanation
この変更は、個人識別情報（PII）に対応した言語に関する情報を更新したものです。具体的には、PIIサービスがサポートする言語に関する表形式のデータが削除され、新しい文に置き換えられました。

新しい内容では、現在利用可能な会話型のPIIサービスが英語のみをサポートしていること、そしてプレビュー版のモデル `2023-04-15-preview` では英語、ドイツ語、スペイン語、フランス語がサポートされていることが明記されています。この修正により、ユーザーはPIIサービスにおける言語サポートについての最新情報をより理解しやすくなります。

全体として、この変更はドキュメントの情報を最新のものとし、ユーザーへの情報提供を強化するための重要な更新です。

## articles/ai-studio/azure-openai-in-ai-studio.md{#item-07639b}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: scottpolly
 keywords: Azure AI services, cognitive, Azure OpenAI
 ms.service: azure-ai-foundry
 ms.topic: overview
-ms.date: 11/04/2024
+ms.date: 02/13/2025
 ms.reviewer: shwinne
 ms.author: sgilley
 author: sdgilley
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新された文書の日付"
}
```

### Explanation
この変更は、文書の更新日を変更したものであり、特に `ms.date` フィールドの日付が `2024年11月4日` から `2025年2月13日` に変更されました。この修正は、文書の最新性を反映させるために重要であり、ユーザーに対して最新の情報が提供されるようにしています。

文書の内容自体には変更はありませんが、更新の日付を正確に示すことにより、ユーザーはこの文書がいつ更新されたのかを容易に把握できるようになります。このように、更新情報を適切に管理することは、信頼性の高い技術情報の提供において重要です。

## articles/ai-studio/concepts/management-center.md{#item-6e44f6}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-foundry
 ms.custom:
   - ignite-2024
 ms.topic: concept-article #Don't change.
-ms.date: 11/18/2024
+ms.date: 02/13/2025
 #customer intent: As an admin, I want a central location where I can perform governance and management activities.
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "管理センター文書の日付更新"
}
```

### Explanation
この変更では、管理センターに関する文書の日付を更新しました。具体的には、`ms.date` フィールドの日付が `2024年11月18日` から `2025年2月13日` へと変更されています。この修正により、文書の更新日が最新の情報を反映する形となり、利用者がいつこの情報が更新されたのかを把握しやすくなります。

文書の内容は変更されていませんが、更新日を適切に管理することは、情報の信頼性とユーザビリティを向上させる上で非常に重要です。これにより、ユーザーは最新の情報に基づいて意思決定を行うことができます。

## articles/ai-studio/how-to/develop/create-hub-project-sdk.md{#item-8c3e99}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: scottpolly
 ms.service: azure-ai-foundry
 ms.custom: build-2024, devx-track-azurecli
 ms.topic: how-to
-ms.date: 11/21/2024
+ms.date: 02/13/2025
 ms.reviewer: dantaylo
 ms.author: sgilley
 author: sdgilley
@@ -78,27 +78,40 @@ az ml workspace create --kind hub --resource-group {my_resource_group} --name {m
 
 ## Create an AI Services connection
 
-After creating your own AI Services, you can connect it to your hub:
+After creating your own AI Services, you can connect it to your hub.
 
 # [Python SDK](#tab/python)
 
-```python
-from azure.ai.ml.entities import AzureAIServicesConnection
+1. Your `ml_client` connection now needs to include your hub:
 
-# constrict an AI Services connection
-my_connection_name = "myaiservivce"
-my_endpoint = "demo.endpoint" # this could also be called target
-my_api_keys = None # leave blank for Authentication type = AAD
-my_ai_services_resource_id = "" # ARM id required
+    * Provide your subscription details.  For `<AML_WORKSPACE_NAME>`, use your hub name:
+    
+        [!notebook-python[](~/azureml-examples-main/sdk/python/resources/connections/connections.ipynb?name=details)]
 
-my_connection = AzureAIServicesConnection(name=my_connection_name,
-                                    endpoint=my_endpoint, 
-                                    api_key= my_api_keys,
-                                    ai_services_resource_id=my_ai_services_resource_id)
+    * Get a handle to the hub:
 
-# Create the connection
-ml_client.connections.create_or_update(my_connection)
-```
+        [!notebook-python[](~/azureml-examples-main/sdk/python/resources/connections/connections.ipynb?name=ml_client)]
+
+2. Use `ml_client` to create the connection to your AI Services:
+
+    ```python
+    from azure.ai.ml.entities import AzureAIServicesConnection
+
+    # construct an AI Services connection
+    my_connection_name = "myaiservivce" # any name you want
+    aiservices_resource_name = <resource_name> # copy from Azure AI Foundry portal
+    my_endpoint = "<endpoint>" # copy from Azure AI Foundry portal
+    my_api_keys = None # leave blank for Authentication type = AAD
+    my_ai_services_resource_id = f"/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.CognitiveServices/accounts/{aiservices_resource_name}"
+
+    my_connection = AzureAIServicesConnection(name=my_connection_name,
+                                        endpoint=my_endpoint, 
+                                        api_key= my_api_keys,
+                                        ai_services_resource_id=my_ai_services_resource_id)
+
+    # Create the connection
+    ml_client.connections.create_or_update(my_connection)
+    ```
 
 # [Azure CLI](#tab/azurecli)
 
@@ -113,26 +126,30 @@ You can use either an API key or credential-less YAML configuration file. For mo
     ```yml
     name: myazai_ei
     type: azure_ai_services
-    endpoint: https://contoso.cognitiveservices.azure.com/
+    endpoint: <endpoint for your AI Services>
     api_key: XXXXXXXXXXXXXXX
+    ai_services_resource_id: <fully_qualified_resource_id>
     ```
 
 - Credential-less
 
     ```yml    
     name: myazai_apk
     type: azure_ai_services
-    endpoint: https://contoso.cognitiveservices.azure.com/
+    endpoint: <endpoint for your AI Services>
+    ai_services_resource_id: <fully_qualified_resource_id>
     ```
 
+The <fully_qualified_resource_id> is the resource ID of your AI Services resource. It is in the format `/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.CognitiveServices/accounts/{aiservices_resource_name}`.
+
 ---
 
 ## Create an Azure AI Foundry hub using existing dependency resources
 
 You can also create a hub using existing resources such as Azure Storage and Azure Key Vault. In the following examples, replace the example string values with your own values:
 
 > [!TIP]
-> You can retrieve the resource ID of the storage account and key vault from the Azure Portal by going to the resource's overview and selecting __JSON view__. The resource ID is located in the __id__ field. You can also use the Azure CLI to retrieve the resource ID. For example, `az storage account show --name {my_storage_account_name} --query "id"` and `az keyvault show --name {my_key_vault_name} --query "id"`.
+> You can retrieve the resource ID of the storage account and key vault from the Azure portal by going to the resource's overview and selecting __JSON view__. The resource ID is located in the __id__ field. You can also use the Azure CLI to retrieve the resource ID. For example, `az storage account show --name {my_storage_account_name} --query "id"` and `az keyvault show --name {my_key_vault_name} --query "id"`.
 
 # [Python SDK](#tab/python)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "HubプロジェクトSDKに関する文書の更新"
}
```

### Explanation
この変更は、HubプロジェクトSDKに関する文書の内容を更新し、特にいくつかの手順やコードスニペットを明確化したものです。主な修正点は、日付の変更や説明文の追加、コード例の再構成が含まれています。

具体的には、`ms.date` フィールドが `2024年11月21日` から `2025年2月13日` に変更され、文書の最新性が反映されています。また、接続手順やコードの説明が見直され、一部のパラメータやコメントが追加されることで、ユーザーが理解しやすくなっています。例として、AIサービスの接続を構築する手順が詳細化され、特定の引数についてのヒントや構文が提供されています。

このような更新は、ユーザーが技術的な手順を理解しやすくするだけでなく、最新のAPIやサービスと整合性を保つためにも重要です。これにより、より良いユーザーエクスペリエンスが提供されることになります。

## articles/ai-studio/how-to/healthcare-ai/healthcare-ai-models.md{#item-12fcfc}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,8 @@ description: Learn about AI models that are applicable to the health and life sc
 ms.service: azure-ai-foundry
 manager: scottpolly
 ms.topic: concept-article
-ms.date: 10/20/2024
-ms.reviewer: itarapov
+ms.date: 02/13/2025
+ms.reviewer: franksolomon
 reviewer: ivantarapov
 ms.author: mopeakande
 author: msakande
@@ -18,30 +18,30 @@ author: msakande
 
 [!INCLUDE [health-ai-models-meddev-disclaimer](../../includes/health-ai-models-meddev-disclaimer.md)]
 
-In this article, you learn about Microsoft's catalog of multimodal healthcare foundation models. The models were developed in collaboration with Microsoft Research, strategic partners, and leading healthcare institutions for healthcare organizations. Healthcare organizations can use the models to rapidly build and deploy AI solutions tailored to their specific needs, while minimizing the extensive compute and data requirements typically associated with building multimodal models from scratch. The intention isn't for these models to serve as standalone products; rather, they're designed for developers to use as a foundation to build upon. With these healthcare AI models, professionals have the tools they need to harness the full potential of AI to enhance biomedical research, clinical workflows, and ultimately care delivery.
+In this article, you learn about the Microsoft multimodal healthcare foundation model catalog. The models were jointly developed by Microsoft Research, strategic partners, and leading healthcare institutions for healthcare organizations. Healthcare organizations can use the models to rapidly build and deploy AI solutions tailored to their specific needs, while minimizing the extensive compute and data requirements typically associated with building multimodal models from scratch. The intention isn't for these models to serve as standalone products. Instead, they're designed for developers to use as a foundation to build upon. With these healthcare AI models, professionals have the tools they need to harness the full potential of AI to enhance biomedical research, clinical workflows, and ultimately care delivery.
 
-The healthcare industry is undergoing a revolutionary transformation driven by the power of artificial intelligence (AI). While existing large language models like GPT-4 show tremendous promise for clinical text-based tasks and general-purpose multimodal reasoning, they struggle to understand non-text multimodal healthcare data such as medical imaging—radiology, pathology, ophthalmology—and other specialized medical text like longitudinal electronic medical records. They also find it challenging to process non-text modalities like signal data, genomic data, and protein data, much of which isn't publicly available.
+The power of artificial intelligence (AI) is driving a revolutionary transformation in the healthcare industry. While existing large language models like GPT-4 show tremendous promise for clinical text-based tasks and general-purpose multimodal reasoning, they struggle to understand non-text multimodal healthcare data - for example, medical imaging—radiology, pathology, and ophthalmology information resources. This problem covers other specialized medical text resources - for example, longitudinal electronic medical records. It becomes challenging to process non-text modalities like signal data, genomic data, and protein data, much of which isn't publicly available.
 
 :::image type="content" source="../../media/how-to/healthcare-ai/connect-modalities.gif" alt-text="Models that reason about various modalities come together to support discover, development and delivery of healthcare":::
 
-The Azure AI model catalog available in [Azure AI Foundry](../model-catalog-overview.md) and [Azure Machine Learning studio](../../../machine-learning/concept-model-catalog.md) provides healthcare foundation models that facilitate AI-powered analysis of various medical data types and expand well beyond medical text comprehension into the multimodal reasoning about medical data. These AI models can integrate and analyze data from diverse sources that come in various modalities, such as medical imaging, genomics, clinical records, and other structured and unstructured data sources. The models also span several healthcare fields like dermatology, ophthalmology, radiology, and pathology. 
+The Azure AI model catalog, available in [Azure AI Foundry](../model-catalog-overview.md) and [Azure Machine Learning studio](../../../machine-learning/concept-model-catalog.md), provides healthcare foundation models that facilitate AI-powered analysis of various medical data types. These AI models expand well beyond medical text comprehension into the multimodal reasoning about medical data. They can integrate and analyze data from diverse sources that come in various modalities - for example, medical imaging, genomics, clinical records, and other structured and unstructured data sources. The models also span several healthcare fields, including dermatology, ophthalmology, radiology, pathology, and more.
 
 ## Microsoft first-party models
 
-The following models are Microsoft's first party multimodal healthcare foundation models.
+These models are Microsoft's first party multimodal healthcare foundation models.
 
 #### [MedImageInsight](./deploy-medimageinsight.md)
-This model is an embedding model that enables sophisticated image analysis, including classification and similarity search in medical imaging. Researchers can use the model embeddings in simple zero-shot classifiers or to build adapters for their specific tasks, thereby streamlining workflows in radiology, pathology, ophthalmology, dermatology, and other modalities. For example, researchers can explore how the model can be used to  build tools that automatically route imaging scans to specialists or flag potential abnormalities for further review. These actions can enable improved efficiency and patient outcomes. Furthermore, the model can be leveraged for Responsible AI (RAI) safeguards such as out-of-distribution (OOD) detection and drift monitoring, to maintain stability and reliability of AI tools and data pipelines in dynamic medical imaging environments.  
+This model is an embedding model that enables sophisticated image analysis, including classification and similarity search in medical imaging. Researchers can use the model embeddings in simple zero-shot classifiers. They can also build adapters for their specific tasks, thereby streamlining workflows in radiology, pathology, ophthalmology, dermatology, and other modalities. For example, researchers can use the model to build tools that automatically route imaging scans to specialists, or flag potential abnormalities for further review. These actions can boost efficiency and improve patient outcomes. Furthermore, the model supports Responsible AI (RAI) safeguards, such as out-of-distribution (OOD) detection and drift monitoring. These safeguards maintain the stability and reliability of AI tools and data pipelines in dynamic medical imaging environments.  
 
 #### [CXRReportGen](./deploy-cxrreportgen.md)
-Chest X-rays are the most common radiology procedure globally. They're crucial because they help doctors diagnose a wide range of conditions—from lung infections to heart problems. These images are often the first step in detecting health issues that affect millions of people. This multimodal AI model incorporates current and prior images along with key patient information to generate detailed, structured reports from chest X-rays. The reports highlight AI-generated findings directly on the images to align with human-in-the-loop workflows. Researchers can test this capability and the potential to accelerate turnaround times while enhancing the diagnostic precision of radiologists. 
+Chest X-rays are the most common radiology procedure globally. They help doctors diagnose a wide range of conditions - lung infections, heart problems, and more. For millions of people, these images often become the first step in detecting health issues. This multimodal AI model incorporates current and prior images, along with key patient information, to generate detailed, structured reports from chest X-rays. The reports highlight AI-generated findings based directly on the images, to align with human-in-the-loop workflows. Researchers can test this capability and the potential to accelerate turnaround times while enhancing the diagnostic precision of radiologists.
 
 #### [MedImageParse](./deploy-medimageparse.md)
-This model is designed for precise image segmentation, and it covers various imaging modalities, including X-Rays, CT scans, MRIs, ultrasounds, dermatology images, and pathology slides. The model can be fine-tuned for specific applications, such as tumor segmentation or organ delineation, allowing developers to test and validate the model and the ability to build tools that leverage AI for highly sophisticated medical image analysis.
+This model is designed for precise image segmentation, and it covers various imaging modalities, including X-Rays, CT scans, MRIs, ultrasounds, dermatology images, and pathology slides. The model can be fine-tuned for specific applications, such as tumor segmentation or organ delineation. It allows developers to test and validate the model and the ability to build tools that leverage AI for highly sophisticated medical image analysis.
 
 ## Partner models
 
-The Azure AI model catalog also provides a curated collection of healthcare models from Microsoft partners with capabilities such as digital pathology slide analysis, biomedical research, and medical knowledge sharing. These models come from partners that include Paige.AI and Providence Healthcare. For a complete list of models, refer to the [model catalog page](https://aka.ms/healthcaremodelstudio). 
+The Azure AI model catalog also provides a curated collection of healthcare models from Microsoft partners with capabilities such as digital pathology slide analysis, biomedical research, medical knowledge sharing capabilities, and more. Partners including Paige.AI and Providence Healthcare provide these models. For a complete list of models, visit the [model catalog page](https://aka.ms/healthcaremodelstudio) resource.
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ヘルスケアAIモデルに関する文書の更新"
}
```

### Explanation
この変更は、ヘルスケアAIモデルに関する文書の内容を改善し、より明確で一貫性のある情報を提供することを目的としています。具体的には、いくつかの文言が修正され、また文書の構造が整えられています。

主な変更点には以下が含まれます：
- `ms.date` が `2024年10月20日` から `2025年2月13日` に更新され、レビュアーが `itarapov` から `franksolomon` に変更されています。
- 文書内の文言が一部変更され、情報の正確さと流暢さが向上しています。たとえば、AIモデルについての説明が明確化され、専門用語やフレーズの使い方が統一されています。
- 新しい内容の追加や説明の再構成が行われており、読者がAIモデルを活用する方法についてより理解しやすくなっています。

このようなマイナーな更新は、読者がテクノロジーの最新情報を把握し、特にヘルスケア分野におけるAIの応用に関する理解を深めるために重要です。文書の質を向上させることで、専門家や開発者が必要な情報に容易にアクセスできるようにしています。

## articles/ai-studio/media/tutorials/chat/deploy-web-app.png{#item-189250}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットチュートリアル用画像の更新"
}
```

### Explanation
この変更は、チャットに関するチュートリアルで使用される画像 `deploy-web-app.png` の更新を示しています。具体的には、変更行数がゼロであるため、画像そのものの内容は更新されていないか、メタデータの改善に関連している可能性があります。

画像のリンクは次の通りです：
- [画像のリンク](https://github.com/MicrosoftDocs/azure-ai-docs/blob/f2b97989f8f69b4bd21461059c352cbe95859c00/articles%2Fai-studio%2Fmedia%2Ftutorials%2Fchat%2Fdeploy-web-app.png)

このような更新は、特定のチュートリアルにおいて視覚的な要素を確認するために重要であり、ユーザーの体験向上や情報の明確さに役立ちます。画像が正確で関連性の高いものであることは、効果的な学習を促進するために必要不可欠です。

## articles/ai-studio/tutorials/deploy-chat-web-app.md{#item-987845}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: tutorial
-ms.date: 12/27/2024
+ms.date: 02/13/2025
 ms.reviewer: tgokal
 ms.author: sgilley
 author: sdgilley
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイチャットWebアプリチュートリアルの更新"
}
```

### Explanation
この変更は、「デプロイチャットWebアプリ」チュートリアル文書の更新を示しています。主な改訂内容は以下の通りです。

- 文書の最終更新日（`ms.date`）が `2024年12月27日` から `2025年2月13日` に変更されました。これにより、ユーザーに最新の情報であることを示しています。
- その他のメタ情報（レビュアーや著者に関する情報）はそのままとなっています。

このように、更新日を変更することは、文書を常に最新の状態に保つために重要であり、特に技術ドキュメントでは、日付が変更されることで、新しい知見や開発動向を反映することができます。これにより、ユーザーは信頼性の高い情報にアクセスしやすくなります。


