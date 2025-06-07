---
date: '2025-06-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e10a743...MicrosoftDocs:b06c631
summary: このコードの差分は、文書に対するマイナーな更新と一件の重大な変更を含み、文書内容の最新化とスタイルの一貫性、情報の明確さの向上を目的としています。具体的には、エンティティタイプの追加や説明の強化、言語のリスト更新、`identification-entities.md`の全面的な改訂が行われました。特に、個々のエンティティに関する地域別の識別情報が新たに統合され、ユーザーが個人情報を識別しやすくなっています。また、他の文書でも日付の更新やスタイルの一貫性が強化されています。これにより、サービス文書の品質が向上し、ユーザーの満足度向上が期待されます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e10a743...MicrosoftDocs:b06c631){target="_blank"}

# Highlights
このコードの差分は、複数の文書に対するマイナーな更新と一件の重大な変更を伴うものであり、主に文書の内容を最新のものに保ち、スタイルの一貫性や情報の明確さを向上させることを目的としています。

## New features
- `entity-categories.md` におけるエンティティタイプの追加および説明の強化。
- 支援される言語のリストが最新情報に更新され、より多くの言語が含まれるようになりました。

## Breaking changes
- `identification-entities.md` の全面的な改訂により、古い情報が削除され、新しい情報が統合されました。特に、個々のエンティティに関する地域ごとの識別情報が追加されました。

## Other updates
- `data-formats.md`、`evaluation-metrics.md`、および`network-isolation.md`を含む複数の文書に渡る日付の更新やスタイルの一貫性を向上させるマイナーな修正。

# Insights
今回のコード差分では、ドキュメント全体を通じて一貫性や正確性を高めるための重要な変更が施されています。特に注目すべきは、`identification-entities.md`の破壊的変更で、ユーザーが個人情報をより正確に識別し、適切に管理するための基盤が強化されています。この変更により、システムが新たな法規制やグローバルなニーズに対応しやすくなっている点が重要です。

また、多言語対応の拡充は、グローバル展開を考慮した戦略の一環と考えられ、ユーザー層を広げ、異なる言語環境のユーザーに対しても均質なサービスを提供することが可能になります。さらに、丁寧な文体への修正や、詳細な手順の明確化は、ユーザビリティを高め、ユーザーの操作ミスを防ぐと同時に、学習コストを低減するための取り組みと言えるでしょう。

全体として、今回の更新によりサービスドキュメントの品質が向上し、ユーザーの満足度を高める結果につながることが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [data-formats.md](#item-8559f6) | minor update | 日付の更新: データフォーマット文書 | modified | 1 | 1 | 2 | 
| [evaluation-metrics.md](#item-3803bc) | minor update | 評価指標文書のテキストの修正 | modified | 4 | 4 | 8 | 
| [entity-categories.md](#item-ba2623) | minor update | 個人情報情報に関するエンティティカテゴリ文書の改訂 | modified | 577 | 431 | 1008 | 
| [identification-entities.md](#item-9bf762) | breaking change | 個人情報に関連する識別エンティティ情報の完全な改訂 | modified | 222 | 222 | 444 | 
| [network-isolation.md](#item-8445fc) | minor update | ネットワーク隔離に関する手順の改訂 | modified | 6 | 6 | 12 | 


# Modified Contents
## articles/ai-services/language-service/conversational-language-understanding/concepts/data-formats.md{#item-8559f6}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/21/2024
+ms.date: 06/05/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-clu
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新: データフォーマット文書"
}
```

### Explanation
このコードの差分は、`data-formats.md` 文書内の日付を更新するためのマイナーな改良を示しています。元のリリース日が「11/21/2024」から「06/05/2025」に変更され、これにより最新の情報が反映されています。全体として、この修正は文書の内容を正確に保ち、ユーザーに正しいタイムスタンプの情報を提供することを目的としています。

## articles/ai-services/language-service/custom-text-classification/concepts/evaluation-metrics.md{#item-3803bc}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/21/2024
+ms.date: 6/6/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification
 ---
@@ -26,12 +26,12 @@ Model evaluation is triggered automatically after training is completed successf
 
     `Recall = #True_Positive / (#True_Positive + #False_Negatives)`
 
-* **F1 score**: The F1 score is a function of Precision and Recall. It's needed when you seek a balance between Precision and Recall.
+* **F1 score**: The F1 score is a function of precision and recall. It's needed when you seek a balance between precision and recall.
 
     `F1 Score = 2 * Precision * Recall / (Precision + Recall)` <br> 
 
 >[!NOTE]
-> Precision, recall and F1 score are calculated for each class separately (*class-level* evaluation) and for the model collectively (*model-level* evaluation).
+> Precision, recall, and F1 score are calculated for each class separately (*class-level* evaluation) and for the model collectively (*model-level* evaluation).
 ## Model-level and Class-level evaluation metrics
 
 The definitions of precision, recall, and evaluation are the same for both class-level and model-level evaluations. However, the count of *True Positive*, *False Positive*, and *False Negative* differ as shown in the following example.
@@ -89,7 +89,7 @@ The below sections use the following example dataset:
 **F1 Score** = `2 * Precision * Recall / (Precision + Recall) =  (2 * 0.8 * 0.67) / (0.8 + 0.67) = 0.73`
 
 > [!NOTE] 
-> For single-label classification models, the count of false negatives and false positives are always equal. Custom single-label classification models always predict one class for each document. If the prediction is not correct, FP count of the predicted class increases by one and FN of the actual class increases by one, overall count of FP and FN for the model will always be equal. This is not the case for multi-label classification, because failing to predict one of the classes of a document is counted as a false negative. 
+> For single-label classification models, the number of false negatives and false positives are always equal. Custom single-label classification models always predict one class for each document. If the prediction is not correct, FP count of the predicted class increases by one and FN of the actual class increases by one, overall count of FP and FN for the model will always be equal. This is not the case for multi-label classification, because failing to predict one of the classes of a document is counted as a false negative. 
 ## Interpreting class-level evaluation metrics
 
 So what does it actually mean to have a high precision or a high recall for a certain class?
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価指標文書のテキストの修正"
}
```

### Explanation
このコードの差分は、`evaluation-metrics.md` 文書におけるテキストの修正を含みます。具体的には、いくつかの文言が「Precision」「Recall」および「F1 score」の小文字表記への変更が行われ、より一貫したスタイルが適用されています。また、日付が「11/21/2024」から「6/6/2025」に更新され、新たな情報が反映されています。これにより、文書の情報が最新であり、読みやすさや文書全体の整合性が向上しています。全体として、これらの変更はユーザーに対して正確かつ理解しやすい内容の提供を目的としたものです。

## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories.md{#item-ba2623}

<details>
<summary>Diff</summary>
````diff
@@ -11,21 +11,51 @@ ms.author: lajanuar
 ms.custom: language-service-pii
 ---
 
-# Supported Personally Identifiable Information (PII) entity categories
-
-Use this article to find the entity categories that can be returned by the [PII detection feature](../how-to-call.md). This feature runs a predictive model to identify, categorize, and redact sensitive information from an input document.
+# Supported PII entities
+Use this article to find the entity categories that the [personally identifiable information (PII) detection feature](../how-to-call.md) returns. This feature runs a predictive model to identify, categorize, and redact sensitive information from an input document.
 
 The PII feature includes the ability to detect personal (`PII`) and health (`PHI`) information.
 
-## Entity categories
+## Supported entities
 
 > [!NOTE]
-> To detect protected health information (PHI), use the `domain=phi` parameter and model version `2020-04-01` or later.
+> * To detect protected health information (PHI), use the `domain=phi` parameter and model version `2020-04-01` or later.
+> * The `Type` and `Subtype` are new designations introduced in the `2025-05-15-preview` version.
 
-The following entity categories are returned when you're sending API requests PII feature.
+The following entity categories are returned when you're sending API requests PII feature:
 
 # [Preview API](#tab/preview-api)
 
+## Type: Person
+
+This type contains the following entity:
+
+:::row:::
+    :::column span="":::
+        **Entity**
+
+        Person
+
+    :::column-end:::
+    :::column span="2":::
+        **Details**
+
+        Names of people. Returned as both PII and PHI.
+
+        To get this entity type, add `Person` to the `piiCategories` parameter. `Person` is returned in the API response if detected.
+
+    :::column-end:::
+
+    :::column span="":::
+      **Supported languages**
+
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+
+   :::column-end:::
+:::row-end:::
+
+# [GA API](#tab/ga-api)
+
 ## Category: Person
 
 This category contains the following entity:
@@ -42,17 +72,51 @@ This category contains the following entity:
 
         Names of people. Returned as both PII and PHI.
 
-        To get this entity category, add `Person` to the `piiCategories` parameter. `Person` will be returned in the API response if detected.
-      
+        To get this entity category, add `Person` to the `piiCategories` parameter. `Person` is returned in the API response if detected.
+
     :::column-end:::
-    
+
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`    
-      
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+
    :::column-end:::
 :::row-end:::
+---
+
+# [Preview API](#tab/preview-api)
+
+## Type: PersonType
+
+This type contains the following entity:
+
+
+:::row:::
+    :::column span="":::
+        **Entity**
+
+        PersonType
+
+    :::column-end:::
+    :::column span="2":::
+        **Details**
+
+        Job types or roles held by a person.
+
+        To get this entity category, add `PersonType` to the `piiCategories` parameter. `PersonType` is returned in the API response if detected.
+
+    :::column-end:::
+
+    :::column span="":::
+      **Supported languages**
+
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+
+   :::column-end:::
+:::row-end:::
+
+# [GA API](#tab/ga-api)
 
 ## Category: PersonType
 
@@ -71,18 +135,53 @@ This category contains the following entity:
 
         Job types or roles held by a person.
 
-        To get this entity category, add `PersonType` to the `piiCategories` parameter. `PersonType` will be returned in the API response if detected.
-      
+        To get this entity type, add `PersonType` to the `piiCategories` parameter. `PersonType` is returned in the API response if detected.
+
+    :::column-end:::
+
+    :::column span="":::
+      **Supported languages**
+
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+
+   :::column-end:::
+:::row-end:::
+
+---
+
+# [Preview API](#tab/preview-api)
+
+## Type: PhoneNumber
+
+This type contains the following entity:
+
+:::row:::
+    :::column span="":::
+        **Entity**
+
+        PhoneNumber
+
+    :::column-end:::
+    :::column span="2":::
+        **Details**
+
+        Phone numbers (US and EU phone numbers only). Returned as both PII and PHI.
+
+        To get this entity category, add `PhoneNumber` to the `piiCategories` parameter. `PhoneNumber` is returned in the API response if detected.
+
     :::column-end:::
 
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      
+      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt` `pt-br`
+
    :::column-end:::
+
 :::row-end:::
 
+# [GA API](#tab/ga-api)
+
 ## Category: PhoneNumber
 
 This category contains the following entity:
@@ -99,23 +198,25 @@ This category contains the following entity:
 
         Phone numbers (US and EU phone numbers only). Returned as both PII and PHI.
 
-        To get this entity category, add `PhoneNumber` to the `piiCategories` parameter. `PhoneNumber` will be returned in the API response if detected.
-      
+        To get this entity type, add `PhoneNumber` to the `piiCategories` parameter. `PhoneNumber` is returned in the API response if detected.
+
     :::column-end:::
 
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt` `pt-br`
-      
+
    :::column-end:::
 
 :::row-end:::
+---
 
+# [Preview API](#tab/preview-api)
 
-## Category: Organization
+## Type: Organization
 
-This category contains the following entity:
+This type contains the following entity:
 
 :::row:::
     :::column span="":::
@@ -129,44 +230,44 @@ This category contains the following entity:
 
         Companies, political groups, musical bands, sport clubs, government bodies, and public organizations. Nationalities and religions are not included in this entity type. Returned as both PII and PHI.
 
-        To get this entity category, add `Organization` to the `piiCategories` parameter. `Organization` will be returned in the API response if detected.
-      
+        To get this entity category, add `Organization` to the `piiCategories` parameter. `Organization` is returned in the API response if detected.
+
     :::column-end:::
 
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+
    :::column-end:::
 
 :::row-end:::
 
-#### Subcategories
+#### Subtype
 
-The entity in this category can have the following subcategories.
+The entity in this type can have the following subcategories:
 
 :::row:::
     :::column span="":::
-        **Entity subcategory**
+        **Entity subtype**
 
-        Medical    
+        Medical
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
         Medical companies and groups.
 
-        To get this entity category, add `OrganizationMedical` to the `piiCategories` parameter. `OrganizationMedical` will be returned in the API response if detected.
-      
+        To get this entity category, add `OrganizationMedical` to the `piiCategories` parameter. `OrganizationMedical` is returned in the API response if detected.
+
     :::column-end:::
 
     :::column span="":::
       **Supported languages**
 
-      `en`   
-      
+      `en`
+
    :::column-end:::
 
 :::row-end:::
@@ -178,16 +279,16 @@ The entity in this category can have the following subcategories.
     :::column-end:::
     :::column span="2":::
 
-        Stock exchange groups. 
+        Stock exchange groups.
+
+        To get this entity category, add `OrganizationStockExchange` to the `piiCategories` parameter. `OrganizationStockExchange` is returned in the API response if detected.
 
-        To get this entity category, add `OrganizationStockExchange` to the `piiCategories` parameter. `OrganizationStockExchange` will be returned in the API response if detected.
-      
     :::column-end:::
 
     :::column span="":::
 
-      `en`   
-      
+      `en`
+
    :::column-end:::
 
 :::row-end:::
@@ -201,871 +302,918 @@ The entity in this category can have the following subcategories.
 
         Sports-related organizations.
 
-        To get this entity category, add `OrganizationSports` to the `piiCategories` parameter. `OrganizationSports` will be returned in the API response if detected.
-      
+        To get this entity category, add `OrganizationSports` to the `piiCategories` parameter. `OrganizationSports` is returned in the API response if detected.
+
     :::column-end:::
 
     :::column span="":::
 
-      `en`   
-      
+      `en`
+
    :::column-end:::
 
 :::row-end:::
 
+# [GA API](#tab/ga-api)
 
-## Category: Address
+## Category: Organization
 
 This category contains the following entity:
 
 :::row:::
     :::column span="":::
         **Entity**
 
-        Address
+        Organization
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
-        Full mailing address. Returned as both PII and PHI.
+        Companies, political groups, musical bands, sport clubs, government bodies, and public organizations. Nationalities and religions are not included in this entity type. Returned as both PII and PHI.
+
+        To get this entity type, add `Organization` to the `piiCategories` parameter. `Organization` is returned in the API response if detected.
 
-        To get this entity category, add `Address` to the `piiCategories` parameter. `Address` will be returned in the API response if detected.
-      
     :::column-end:::
 
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
-      
-    :::column-end:::
+
+   :::column-end:::
 
 :::row-end:::
 
-## Category: Email
+#### Subcategory
 
-This category contains the following entity:
+The entity in this category can have the following subcategories:
 
 :::row:::
     :::column span="":::
-        **Entity**
+        **Entity subcategory**
 
-        Email
+        Medical
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
-        Email addresses. Returned as both PII and PHI.
-      
-        To get this entity category, add `Email` to the `piiCategories` parameter. `Email` will be returned in the API response if detected.
+        Medical companies and groups.
+
+        To get this entity type, add `OrganizationMedical` to the `piiCategories` parameter. `OrganizationMedical` is returned in the API response if detected.
 
     :::column-end:::
+
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
-      
+      `en`
+
+   :::column-end:::
+
+:::row-end:::
+:::row:::
+    :::column span="":::
+
+        Stock exchange
+
+    :::column-end:::
+    :::column span="2":::
+
+        Stock exchange groups.
+
+        To get this entity type, add `OrganizationStockExchange` to the `piiCategories` parameter. `OrganizationStockExchange` is returned in the API response if detected.
+
+    :::column-end:::
+
+    :::column span="":::
+
+      `en`
+
+   :::column-end:::
+
+:::row-end:::
+:::row:::
+    :::column span="":::
+
+        Sports
+
+    :::column-end:::
+    :::column span="2":::
+
+        Sports-related organizations.
+
+        To get this entity type, add `OrganizationSports` to the `piiCategories` parameter. `OrganizationSports` is returned in the API response if detected.
+
     :::column-end:::
+
+    :::column span="":::
+
+      `en`
+
+   :::column-end:::
+
 :::row-end:::
 
+---
 
-## Category: URL
 
-This category contains the following entity:
+# [Preview API](#tab/preview-api)
+
+## Type: Address
+
+
+This type contains the following entity:
 
 :::row:::
     :::column span="":::
         **Entity**
 
-        URL
+        Address
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
-        URLs to websites. Returned as both PII and PHI.
+        Full mailing address. Returned as both PII and PHI.
+
+        To get this entity type, add `Address` to the `piiCategories` parameter. `Address` is returned in the API response if detected.
 
-        To get this entity category, add `URL` to the `piiCategories` parameter. `URL` will be returned in the API response if detected.
-      
     :::column-end:::
 
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
-      
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+
     :::column-end:::
 
 :::row-end:::
 
-## Category: IP Address
+# [GA API](#tab/ga-api)
 
-This category contains the following entity:
+## Category: Address
+
+This type contains the following entity:
 
 :::row:::
     :::column span="":::
         **Entity**
 
-        IPAddress
+        Address
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
-        Network IP addresses. Returned as both PII and PHI.
+        Full mailing address. Returned as both PII and PHI.
+
+        To get this entity category, add `Address` to the `piiCategories` parameter. `Address` is returned in the API response if detected.
 
-        To get this entity category, add `IPAddress` to the `piiCategories` parameter. `IPAddress` will be returned in the API response if detected.
-      
     :::column-end:::
 
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
-      
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+
     :::column-end:::
+
 :::row-end:::
 
-## Category: DateTime
+---
 
-This category contains the following entities:
+# [Preview API](#tab/preview-api)
+
+## Type: Email
+
+This category contains the following entity:
 
 :::row:::
     :::column span="":::
         **Entity**
 
-        DateTime
+        Email
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
-        Dates and times of day. 
+        Email addresses. Returned as both PII and PHI.
+
+        To get this entity type, add `Email` to the `piiCategories` parameter. `Email` is returned in the API response if detected.
 
-        To get this entity category, add `DateTime` to the `piiCategories` parameter. `DateTime` will be returned in the API response if detected.
-      
     :::column-end:::
-:::column span="":::
+    :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      
-   :::column-end:::
+      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
+
+    :::column-end:::
 :::row-end:::
 
-#### Subcategories
+# [GA API](#tab/ga-api)
 
-The entity in this category can have the following subcategories.
+## Category: Email
+
+This type contains the following entity:
 
 :::row:::
     :::column span="":::
-        **Entity subcategory**
+        **Entity**
 
-        Date
+        Email
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
-        Calendar dates. Returned as both PII and PHI.
+        Email addresses. Returned as both PII and PHI.
+
+        To get this category type, add `Email` to the `piiCategories` parameter. `Email` is returned in the API response if detected.
 
-        To get this entity category, add `Date` to the `piiCategories` parameter. `Date` will be returned in the API response if detected.
-      
     :::column-end:::
-    :::column span="2":::
+    :::column span="":::
       **Supported languages**
-      
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`     
-      
+
+      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
+
     :::column-end:::
 :::row-end:::
 
+---
+
+# [Preview API](#tab/preview-api)
+
+## Type: URL
+
+This type contains the following entity:
+
 :::row:::
     :::column span="":::
+        **Entity**
 
-        DateAndTime
-        
+        URL
 
     :::column-end:::
     :::column span="2":::
+        **Details**
 
-        Dates and times of day.
-
-        To get this entity category, add DateAndTime to the piiCategories parameter. DateAndTime will be returned in the API response if detected.
+        URLs to websites. Returned as both PII and PHI.
 
+        To get this entity type, add `URL` to the `piiCategories` parameter. `URL` is returned in the API response if detected.
 
     :::column-end:::
-    :::column span="2":::
+
+    :::column span="":::
       **Supported languages**
-      
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      :::column-end:::
+
+      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
+
+    :::column-end:::
+
 :::row-end:::
-## Subcategory: Age
 
-The PII service supports the Age subcategory within the broader Quantity category (since Age is the personally identifiable piece of information). 
+# [GA API](#tab/ga-api)
+
+## Category: URL
+
+This category contains the following entity:
 
 :::row:::
     :::column span="":::
-        **Entity subcategory**
+        **Entity**
 
-        Age
+        URL
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
-        Ages.
-      
+        URLs to websites. Returned as both PII and PHI.
+
+        To get this entity category, add `URL` to the `piiCategories` parameter. `URL` is returned in the API response if detected.
+
     :::column-end:::
-    :::column span="2":::
+
+    :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      
-   :::column-end:::
+      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
+
+    :::column-end:::
+
 :::row-end:::
+---
 
-### Azure information
+# [Preview API](#tab/preview-api)
 
-These entity categories include identifiable Azure information like authentication information and connection strings. Not returned as PHI.
+## Type: IP Address
+
+This category contains the following entity:
 
 :::row:::
     :::column span="":::
         **Entity**
 
-        Azure DocumentDB Auth Key 
+        IPAddress
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
-        Authorization key for an Azure Cosmos DB server.   
+        Network IP addresses. Returned as both PII and PHI.
+
+        To get this entity type, add `IPAddress` to the `piiCategories` parameter. `IPAddress` is returned in the API response if detected.
 
-        To get this entity category, add `AzureDocumentDBAuthKey` to the `piiCategories` parameter. `AzureDocumentDBAuthKey` will be returned in the API response if detected.
-      
     :::column-end:::
+
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
 
     :::column-end:::
 :::row-end:::
+
+# [GA API](#tab/ga-api)
+
+## Category: IP Address
+
+This category contains the following entity:
+
 :::row:::
     :::column span="":::
+        **Entity**
 
-        Azure IAAS Database Connection String and Azure SQL Connection String.
-        
+        IPAddress
 
     :::column-end:::
     :::column span="2":::
+        **Details**
 
-        Connection string for an Azure infrastructure as a service (IaaS) database, and SQL connection string.
+        Network IP addresses. Returned as both PII and PHI.
+
+        To get this entity category, add `IPAddress` to the `piiCategories` parameter. `IPAddress` is returned in the API response if detected.
 
-        To get this entity category, add `AzureIAASDatabaseConnectionAndSQLString` to the `piiCategories` parameter. `AzureIAASDatabaseConnectionAndSQLString` will be returned in the API response if detected.
-      
     :::column-end:::
+
     :::column span="":::
+      **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
 
     :::column-end:::
 :::row-end:::
+
+
+---
+
+# [Preview API](#tab/preview-api)
+
+## Type: DateTime
+
+This type contains the following entities:
+
 :::row:::
     :::column span="":::
+        **Entity**
 
-        Azure IoT Connection String  
+        DateTime
 
     :::column-end:::
     :::column span="2":::
+        **Details**
 
-        Connection string for Azure IoT. 
-      
-        To get this entity category, add `AzureIoTConnectionString` to the `piiCategories` parameter. `AzureIoTConnectionString` will be returned in the API response if detected.
+        Dates and times of day.
+
+        To get this entity type, add `DateTime` to the `piiCategories` parameter. `DateTime` is returned in the API response if detected.
 
     :::column-end:::
-    :::column span="":::
+:::column span="":::
+      **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
 
-    :::column-end:::
+   :::column-end:::
 :::row-end:::
+
+### Subtypes
+
+The entity in this type can have the following subtypes:
+
 :::row:::
     :::column span="":::
+        **Entity subtypes**
 
-        Azure Publish Setting Password  
+        Date
 
     :::column-end:::
     :::column span="2":::
+        **Details**
 
-        Password for Azure publish settings.
+        Calendar dates. Returned as both PII and PHI.
+
+        To get this entity type, add `Date` to the `piiCategories` parameter. `Date` is returned in the API response if detected.
 
-        To get this entity category, add `AzurePublishSettingPassword` to the `piiCategories` parameter. `AzurePublishSettingPassword` will be returned in the API response if detected.
-      
     :::column-end:::
-    :::column span="":::
+    :::column span="2":::
+      **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
 
     :::column-end:::
 :::row-end:::
+
 :::row:::
     :::column span="":::
 
-        Azure Redis Cache Connection String 
+        DateAndTime
+
 
     :::column-end:::
     :::column span="2":::
 
-        Connection string for a Redis cache.
+        Dates and times of day.
 
-        To get this entity category, add `AzureRedisCacheString` to the `piiCategories` parameter. `AzureRedisCacheString` will be returned in the API response if detected.
-      
-    :::column-end:::
-    :::column span="":::
+        To get this entity category, add `DateAndTime` to the `piiCategories` parameter. `DateAndTime` is returned in the API response if detected.
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
     :::column-end:::
+    :::column span="2":::
+      **Supported languages**
+
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+      :::column-end:::
 :::row-end:::
+
+#### Subtype: Age
+
+The PII service supports the Age subtype within the broader Quantity type (since Age is the personally identifiable piece of information).
+
 :::row:::
     :::column span="":::
+        **Entity subtype**
 
-        Azure SAS 
+        Age
 
     :::column-end:::
     :::column span="2":::
+        **Details**
 
-        Connection string for Azure software as a service (SaaS).
+        Ages.
 
-        To get this entity category, add `AzureSAS` to the `piiCategories` parameter. `AzureSAS` will be returned in the API response if detected.
-      
     :::column-end:::
+    :::column span="2":::
+      **Supported languages**
+
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+
+   :::column-end:::
+:::row-end:::
+
+#### Subtype: DateOfBirth
+
+:::row:::
     :::column span="":::
+        **Entity subtype**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+        Date of birth.
 
     :::column-end:::
+    :::column span="2":::
+        **Details**
+
+      Date
+
+      To get this entity type, add `DateOfBirth` to the `piiCategories` parameter. `DateOfBirth` is returned in the API response if detected. 
+
+    :::column-end:::
+    :::column span="2":::
+      **Supported languages**
+
+      `en`
+
+   :::column-end:::
 :::row-end:::
+
+# [GA API](#tab/ga-api)
+
+## Category: DateTime
+
+This category contains the following entities:
+
 :::row:::
     :::column span="":::
+        **Entity**
 
-        Azure Service Bus Connection String
+        DateTime
 
     :::column-end:::
     :::column span="2":::
+        **Details**
 
-        Connection string for an Azure service bus.
+        Dates and times of day.
+
+        To get this entity category, add `DateTime` to the `piiCategories` parameter. `DateTime` is returned in the API response if detected.
+
+    :::column-end:::
+:::column span="":::
+      **Supported languages**
+
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+
+   :::column-end:::
+:::row-end:::
 
-        To get this entity category, add `AzureServiceBusString` to the `piiCategories` parameter. `AzureServiceBusString` will be returned in the API response if detected.
-      
-    :::column-end:::
-    :::column span="":::
+### Subcategories
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+The entity in this category can have the following subcategory:
 
-    :::column-end:::
-:::row-end:::
 :::row:::
     :::column span="":::
+        **Entity subcategory**
 
-        Azure Storage Account Key 
+        Date
 
     :::column-end:::
     :::column span="2":::
+        **Details**
 
-        Account key for an Azure storage account. 
+        Calender dates. Returned as both PII and PHI.
+
+        To get this entity category, add `Date` to the `piiCategories` parameter. `Date` is returned in the API response if detected.
 
-        To get this entity category, add `AzureStorageAccountKey` to the `piiCategories` parameter. `AzureStorageAccountKey` will be returned in the API response if detected.
-      
     :::column-end:::
-    :::column span="":::
+    :::column span="2":::
+      **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
 
     :::column-end:::
 :::row-end:::
+
 :::row:::
     :::column span="":::
 
-        Azure Storage Account Key (Generic)
+        DateAndTime
+
 
     :::column-end:::
     :::column span="2":::
 
-        Generic account key for an Azure storage account.
+        Dates and times of day.
 
-        To get this entity category, add `AzureStorageAccountGeneric` to the `piiCategories` parameter. `AzureStorageAccountGeneric` will be returned in the API response if detected.
-      
-    :::column-end:::
-    :::column span="":::
+        To get this entity category, add `DateAndTime` to the `piiCategories` parameter. `DateAndTime` is returned in the API response if detected.
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
     :::column-end:::
+    :::column span="2":::
+      **Supported languages**
+
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+      :::column-end:::
 :::row-end:::
 :::row:::
     :::column span="":::
-
-        SQL Server Connection String 
+        **Entity**
 
     :::column-end:::
     :::column span="2":::
 
-        Connection string for a computer running SQL Server.
+        Calendar dates in diverse formats and years associated with date of birth of an individual. Examples include "born in 1994", "born in 990101", "birth date: February 14th, 1995", "date: 1992/06/30", "DATE: 05-12-1988", "04.10.1999"
 
-        To get this entity category, add `SQLServerConnectionString` to the `piiCategories` parameter. `SQLServerConnectionString` will be returned in the API response if detected.
-      
     :::column-end:::
     :::column span="":::
 
-      `en` 
+      `en`, `fr`, `de`, `it`, `es`, `pt-pt`, `pt-br`, `nl`, `zh-Hans`, `ja`, `ko`, `zh-Hant`
 
     :::column-end:::
 :::row-end:::
 
-# [Generally Available API](#tab/ga-api)
+#### Subcategory: Age
 
-## Type: Person
-
-This type contains the following entity:
+The PII service supports the Age subcategory within the broader Quantity type (since Age is the personally identifiable piece of information).
 
 :::row:::
     :::column span="":::
-        **Entity**
+        **Entity subcategory**
 
-        Person
+        Age
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
-        Names of people. Returned as both PII and PHI.
+        Numeric age.
 
-        To get this entity type, add `Person` to the `piiCategories` parameter. `Person` will be returned in the API response if detected.
-      
     :::column-end:::
-    
-    :::column span="":::
+    :::column span="2":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`    
-      
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+
    :::column-end:::
 :::row-end:::
 
-## Type: PersonType
+---
 
-This type contains the following entity:
+# [Preview API](#tab/preview-api)
 
+### Identification
+
+## Type: BankAccountNumber
 
 :::row:::
     :::column span="":::
         **Entity**
 
-        PersonType
-
     :::column-end:::
     :::column span="2":::
         **Details**
 
-        Job types or roles held by a person.
+        To get this entity type, add `BankAccountNumber` to the `piiCategories` parameter. `BankAccountNumber` is returned in the API response if detected.
 
-        To get this entity type, add `PersonType` to the `piiCategories` parameter. `PersonType` will be returned in the API response if detected.
-      
     :::column-end:::
-
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      
-   :::column-end:::
-:::row-end:::
+     `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
 
-## Type: PhoneNumber
+    :::column-end:::
+:::row-end:::
 
-This type contains the following entity:
+## Type: DriversLicenseNumber
 
 :::row:::
     :::column span="":::
         **Entity**
 
-        PhoneNumber
-
     :::column-end:::
     :::column span="2":::
         **Details**
 
-        Phone numbers (US and EU phone numbers only). Returned as both PII and PHI.
+        To get this entity type, add `DriversLicenseNumber` to the `piiCategories` parameter. `DriversLicenseNumber` is returned in the API response if detected.
 
-        To get this entity type, add `PhoneNumber` to the `piiCategories` parameter. `PhoneNumber` will be returned in the API response if detected.
-      
     :::column-end:::
-
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt` `pt-br`
-      
-   :::column-end:::
+     `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `sk`, `th`, `uk`
 
+    :::column-end:::
 :::row-end:::
 
-
-## Type: Organization
-
-This type contains the following entity:
+## Type: PassportNumber
 
 :::row:::
     :::column span="":::
         **Entity**
 
-        Organization
-
     :::column-end:::
     :::column span="2":::
         **Details**
 
-        Companies, political groups, musical bands, sport clubs, government bodies, and public organizations. Nationalities and religions are not included in this entity type. Returned as both PII and PHI.
+        To get this entity type, add `PassportNumber` to the `piiCategories` parameter. `PassportNumber` is returned in the API response if detected.
 
-        To get this entity type, add `Organization` to the `piiCategories` parameter. `Organization` will be returned in the API response if detected.
-      
     :::column-end:::
-
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      
-   :::column-end:::
+     `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `sk`, `th`, `uk`
 
+    :::column-end:::
 :::row-end:::
 
-#### Subtypes
 
-The entity in this type can have the following subtypes.
+# [GA API](#tab/ga-api)
+
+[!INCLUDE [supported identification entities](../includes/identification-entities.md)]
+
+---
+
+# [Preview API](#tab/preview-api)
+
+## Azure information
+
+These entity types include identifiable Azure information like authentication information and connection strings. Not returned as PHI.
 
 :::row:::
     :::column span="":::
-        **Entity subtype**
+        **Entity**
 
-        Medical    
+        Azure DocumentDB Auth Key
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
-        Medical companies and groups.
+        Authorization key for an Azure Cosmos DB server.
 
-        To get this entity type, add `OrganizationMedical` to the `piiCategories` parameter. `OrganizationMedical` will be returned in the API response if detected.
-      
-    :::column-end:::
+        To get this entity type, add `AzureDocumentDBAuthKey` to the `piiCategories` parameter. `AzureDocumentDBAuthKey` is returned in the API response if detected.
 
+    :::column-end:::
     :::column span="":::
       **Supported languages**
 
-      `en`   
-      
-   :::column-end:::
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
+    :::column-end:::
 :::row-end:::
 :::row:::
     :::column span="":::
 
-        Stock exchange
+        Azure IAAS Database Connection String and Azure SQL Connection String.
+
 
     :::column-end:::
     :::column span="2":::
 
-        Stock exchange groups. 
+        Connection string for an Azure infrastructure as a service (IaaS) database, and SQL connection string.
+
+        To get this entity type, add `AzureIAASDatabaseConnectionAndSQLString` to the `piiCategories` parameter. `AzureIAASDatabaseConnectionAndSQLString` is returned in the API response if detected.
 
-        To get this entity type, add `OrganizationStockExchange` to the `piiCategories` parameter. `OrganizationStockExchange` will be returned in the API response if detected.
-      
     :::column-end:::
-
     :::column span="":::
 
-      `en`   
-      
-   :::column-end:::
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
+    :::column-end:::
 :::row-end:::
 :::row:::
     :::column span="":::
 
-        Sports
+        Azure IoT Connection String
 
     :::column-end:::
     :::column span="2":::
 
-        Sports-related organizations.
+        Connection string for Azure IoT.
 
-        To get this entity type, add `OrganizationSports` to the `piiCategories` parameter. `OrganizationSports` will be returned in the API response if detected.
-      
-    :::column-end:::
+        To get this entity type, add `AzureIoTConnectionString` to the `piiCategories` parameter. `AzureIoTConnectionString` is returned in the API response if detected.
 
+    :::column-end:::
     :::column span="":::
 
-      `en`   
-      
-   :::column-end:::
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
+    :::column-end:::
 :::row-end:::
-
-
-## Type: Address
-
-This type contains the following entity:
-
 :::row:::
     :::column span="":::
-        **Entity**
 
-        Address
+        Azure Publish Setting Password
 
     :::column-end:::
     :::column span="2":::
-        **Details**
 
-        Full mailing address. Returned as both PII and PHI.
+        Password for Azure publish settings.
 
-        To get this entity type, add `Address` to the `piiCategories` parameter. `Address` will be returned in the API response if detected.
-      
-    :::column-end:::
+        To get this entity type, add `AzurePublishSettingPassword` to the `piiCategories` parameter. `AzurePublishSettingPassword` is returned in the API response if detected.
 
+    :::column-end:::
     :::column span="":::
-      **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
-      
-    :::column-end:::
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
+    :::column-end:::
 :::row-end:::
-
-## Type: Email
-
-This type contains the following entity:
-
 :::row:::
     :::column span="":::
-        **Entity**
 
-        Email
+        Azure Redis Cache Connection String
 
     :::column-end:::
     :::column span="2":::
-        **Details**
 
-        Email addresses. Returned as both PII and PHI.
-      
-        To get this entity type, add `Email` to the `piiCategories` parameter. `Email` will be returned in the API response if detected.
+        Connection string for a Redis cache.
+
+        To get this entity type, add `AzureRedisCacheString` to the `piiCategories` parameter. `AzureRedisCacheString` is returned in the API response if detected.
 
     :::column-end:::
     :::column span="":::
-      **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
-      
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+
     :::column-end:::
 :::row-end:::
-
-
-## Type: URL
-
-This type contains the following entity:
-
 :::row:::
     :::column span="":::
-        **Entity**
 
-        URL
+        Azure SAS
 
     :::column-end:::
     :::column span="2":::
-        **Details**
 
-        URLs to websites. Returned as both PII and PHI.
+        Connection string for Azure software as a service (SaaS).
 
-        To get this entity type, add `URL` to the `piiCategories` parameter. `URL` will be returned in the API response if detected.
-      
-    :::column-end:::
+        To get this entity type, add `AzureSAS` to the `piiCategories` parameter. `AzureSAS` is returned in the API response if detected.
 
+    :::column-end:::
     :::column span="":::
-      **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
-      
-    :::column-end:::
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
+    :::column-end:::
 :::row-end:::
-
-## Type: IP Address
-
-This type contains the following entity:
-
 :::row:::
     :::column span="":::
-        **Entity**
 
-        IPAddress
+        Azure Service Bus Connection String
 
     :::column-end:::
     :::column span="2":::
-        **Details**
 
-        Network IP addresses. Returned as both PII and PHI.
+        Connection string for an Azure service bus.
 
-        To get this entity type, add `IPAddress` to the `piiCategories` parameter. `IPAddress` will be returned in the API response if detected.
-      
-    :::column-end:::
+        To get this entity type, add `AzureServiceBusString` to the `piiCategories` parameter. `AzureServiceBusString` is returned in the API response if detected.
 
+    :::column-end:::
     :::column span="":::
-      **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
-      
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+
     :::column-end:::
 :::row-end:::
-
-## Type: DateTime
-
-This type contains the following entities:
-
 :::row:::
     :::column span="":::
-        **Entity**
 
-        DateTime
+        Azure Storage Account Key
 
     :::column-end:::
     :::column span="2":::
-        **Details**
-
-        Dates and times of day. 
-
-        To get this entity type, add `DateTime` to the `piiCategories` parameter. `DateTime` will be returned in the API response if detected.
-      
-    :::column-end:::
-:::column span="":::
-      **Supported languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      
-   :::column-end:::
-:::row-end:::
-
-#### Subtypes
-
-The entity in this type can have the following subtypes.
 
-:::row:::
-    :::column span="":::
-        **Entity subtype**
+        Account key for an Azure storage account.
 
-        Date
+        To get this entity type, add `AzureStorageAccountKey` to the `piiCategories` parameter. `AzureStorageAccountKey` is returned in the API response if detected.
 
     :::column-end:::
-    :::column span="2":::
-        **Details**
+    :::column span="":::
 
-        Calender dates. Returned as both PII and PHI.
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
-        To get this entity type, add `Date` to the `piiCategories` parameter. `Date` will be returned in the API response if detected.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported languages**
-      
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`     
-      
     :::column-end:::
 :::row-end:::
-
 :::row:::
     :::column span="":::
 
-        DateAndTime
-        
+        Azure Storage Account Key (Generic)
 
     :::column-end:::
     :::column span="2":::
 
-        Dates and times of day.
+        Generic account key for an Azure storage account.
+
+        To get this entity type, add `AzureStorageAccountGeneric` to the `piiCategories` parameter. `AzureStorageAccountGeneric` is returned in the API response if detected.
 
-        To get this entity type, add `DateAndTime` to the `piiCategories` parameter. `DateAndTime` will be returned in the API response if detected.
+    :::column-end:::
+    :::column span="":::
 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
     :::column-end:::
-    :::column span="2":::
-      **Supported languages**
-      
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      :::column-end:::
 :::row-end:::
 :::row:::
     :::column span="":::
 
-        DateOfBirth
+        SQL Server Connection String
 
     :::column-end:::
     :::column span="2":::
 
-        Calendar dates in diverse formats and years associated with date of birth of an individual. Examples include “born in 1994”, “born in 990101”, “birth date: February 14th, 1995”, “date: 1992/06/30”, “DATE: 05-12-1988”, “04.10.1999”
-      
-    :::column-end:::
-    :::column span="":::
+        Connection string for a computer running SQL Server.
 
-      `en`, `fr`, `de`, `it`, `es`, `pt-pt`, `pt-br`, `nl`, `zh-Hans`, `ja`, `ko`, `zh-Hant` 
+        To get this entity type, add `SQLServerConnectionString` to the `piiCategories` parameter. `SQLServerConnectionString` is returned in the API response if detected.
 
     :::column-end:::
-:::row-end:::
-## Subtype: Age
-
-The PII service supports the Age subtype within the broader Quantity type (since Age is the personally identifiable piece of information). 
-
-:::row:::
     :::column span="":::
-        **Entity subtype**
 
-        Age
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+      `en`
 
-        Ages.
-      
     :::column-end:::
-    :::column span="2":::
-      **Supported languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      
-   :::column-end:::
 :::row-end:::
 
-### Azure information
+# [GA API](#tab/ga-api)
 
-These entity types include identifiable Azure information like authentication information and connection strings. Not returned as PHI.
+## Azure information
+
+These entity categories include identifiable Azure information like authentication information and connection strings. Not returned as PHI.
 
 :::row:::
     :::column span="":::
         **Entity**
 
-        Azure DocumentDB Auth Key 
+        Azure DocumentDB Auth Key
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
-        Authorization key for an Azure Cosmos DB server.   
+        Authorization key for an Azure Cosmos DB server.
+
+        To get this entity category, add `AzureDocumentDBAuthKey` to the `piiCategories` parameter. `AzureDocumentDBAuthKey` is returned in the API response if detected.
 
-        To get this entity type, add `AzureDocumentDBAuthKey` to the `piiCategories` parameter. `AzureDocumentDBAuthKey` will be returned in the API response if detected.
-      
     :::column-end:::
     :::column span="":::
       **Supported languages**
@@ -1078,15 +1226,15 @@ These entity types include identifiable Azure information like authentication in
     :::column span="":::
 
         Azure IAAS Database Connection String and Azure SQL Connection String.
-        
+
 
     :::column-end:::
     :::column span="2":::
 
         Connection string for an Azure infrastructure as a service (IaaS) database, and SQL connection string.
 
-        To get this entity type, add `AzureIAASDatabaseConnectionAndSQLString` to the `piiCategories` parameter. `AzureIAASDatabaseConnectionAndSQLString` will be returned in the API response if detected.
-      
+        To get this entity category, add `AzureIAASDatabaseConnectionAndSQLString` to the `piiCategories` parameter. `AzureIAASDatabaseConnectionAndSQLString` is returned in the API response if detected.
+
     :::column-end:::
     :::column span="":::
 
@@ -1097,14 +1245,14 @@ These entity types include identifiable Azure information like authentication in
 :::row:::
     :::column span="":::
 
-        Azure IoT Connection String  
+        Azure IoT Connection String
 
     :::column-end:::
     :::column span="2":::
 
-        Connection string for Azure IoT. 
-      
-        To get this entity type, add `AzureIoTConnectionString` to the `piiCategories` parameter. `AzureIoTConnectionString` will be returned in the API response if detected.
+        Connection string for Azure IoT.
+
+        To get this entity category, add `AzureIoTConnectionString` to the `piiCategories` parameter. `AzureIoTConnectionString` is returned in the API response if detected.
 
     :::column-end:::
     :::column span="":::
@@ -1116,15 +1264,15 @@ These entity types include identifiable Azure information like authentication in
 :::row:::
     :::column span="":::
 
-        Azure Publish Setting Password  
+        Azure Publish Setting Password
 
     :::column-end:::
     :::column span="2":::
 
         Password for Azure publish settings.
 
-        To get this entity type, add `AzurePublishSettingPassword` to the `piiCategories` parameter. `AzurePublishSettingPassword` will be returned in the API response if detected.
-      
+        To get this entity category, add `AzurePublishSettingPassword` to the `piiCategories` parameter. `AzurePublishSettingPassword` is returned in the API response if detected.
+
     :::column-end:::
     :::column span="":::
 
@@ -1135,15 +1283,15 @@ These entity types include identifiable Azure information like authentication in
 :::row:::
     :::column span="":::
 
-        Azure Redis Cache Connection String 
+        Azure Redis Cache Connection String
 
     :::column-end:::
     :::column span="2":::
 
         Connection string for a Redis cache.
 
-        To get this entity type, add `AzureRedisCacheString` to the `piiCategories` parameter. `AzureRedisCacheString` will be returned in the API response if detected.
-      
+        To get this entity category, add `AzureRedisCacheString` to the `piiCategories` parameter. `AzureRedisCacheString` is returned in the API response if detected.
+
     :::column-end:::
     :::column span="":::
 
@@ -1154,15 +1302,15 @@ These entity types include identifiable Azure information like authentication in
 :::row:::
     :::column span="":::
 
-        Azure SAS 
+        Azure SAS
 
     :::column-end:::
     :::column span="2":::
 
         Connection string for Azure software as a service (SaaS).
 
-        To get this entity type, add `AzureSAS` to the `piiCategories` parameter. `AzureSAS` will be returned in the API response if detected.
-      
+        To get this entity category, add `AzureSAS` to the `piiCategories` parameter. `AzureSAS` is returned in the API response if detected.
+
     :::column-end:::
     :::column span="":::
 
@@ -1180,8 +1328,8 @@ These entity types include identifiable Azure information like authentication in
 
         Connection string for an Azure service bus.
 
-        To get this entity type, add `AzureServiceBusString` to the `piiCategories` parameter. `AzureServiceBusString` will be returned in the API response if detected.
-      
+        To get this entity category, add `AzureServiceBusString` to the `piiCategories` parameter. `AzureServiceBusString` is returned in the API response if detected.
+
     :::column-end:::
     :::column span="":::
 
@@ -1192,15 +1340,15 @@ These entity types include identifiable Azure information like authentication in
 :::row:::
     :::column span="":::
 
-        Azure Storage Account Key 
+        Azure Storage Account Key
 
     :::column-end:::
     :::column span="2":::
 
-        Account key for an Azure storage account. 
+        Account key for an Azure storage account.
+
+        To get this entity category, add `AzureStorageAccountKey` to the `piiCategories` parameter. `AzureStorageAccountKey` is returned in the API response if detected.
 
-        To get this entity type, add `AzureStorageAccountKey` to the `piiCategories` parameter. `AzureStorageAccountKey` will be returned in the API response if detected.
-      
     :::column-end:::
     :::column span="":::
 
@@ -1218,8 +1366,8 @@ These entity types include identifiable Azure information like authentication in
 
         Generic account key for an Azure storage account.
 
-        To get this entity type, add `AzureStorageAccountGeneric` to the `piiCategories` parameter. `AzureStorageAccountGeneric` will be returned in the API response if detected.
-      
+        To get this entity category, add `AzureStorageAccountGeneric` to the `piiCategories` parameter. `AzureStorageAccountGeneric` is returned in the API response if detected.
+
     :::column-end:::
     :::column span="":::
 
@@ -1230,26 +1378,24 @@ These entity types include identifiable Azure information like authentication in
 :::row:::
     :::column span="":::
 
-        SQL Server Connection String 
+        SQL Server Connection String
 
     :::column-end:::
     :::column span="2":::
 
         Connection string for a computer running SQL Server.
 
-        To get this entity type, add `SQLServerConnectionString` to the `piiCategories` parameter. `SQLServerConnectionString` will be returned in the API response if detected.
-      
+        To get this entity category, add `SQLServerConnectionString` to the `piiCategories` parameter. `SQLServerConnectionString` is returned in the API response if detected.
+
     :::column-end:::
     :::column span="":::
 
-      `en` 
+      `en`
 
     :::column-end:::
 :::row-end:::
 
-### Identification
-
-[!INCLUDE [supported identification entities](../includes/identification-entities.md)]
+---
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人情報情報に関するエンティティカテゴリ文書の改訂"
}
```

### Explanation
このコードの差分は、`entity-categories.md` 文書に関する大規模な改訂を示しています。主な変更点には、エンティティのカテゴリ名や構造の修正、新しいエンティティタイプの追加、説明の強化が含まれます。たとえば、「Supported PII entities」セクションが「Supported Personally Identifiable Information (PII) entity categories」から名称が変更され、各エンティティタイプおよびそれに関連する詳細情報が整理されています。

加えて、APIのリクエストに対するレスポンス形式が明確に示され、個々のエンティティに関する詳細な説明や、エンティティを取得するために必要なパラメータが記載されました。また、サポートされる言語のリストも更新され、より多くの言語が追加されています。これにより、ドキュメントは非常に充実し、利用者が情報を理解しやすくなることを目的として、最新の情報に更新されています。

## articles/ai-services/language-service/personally-identifiable-information/includes/identification-entities.md{#item-9bf762}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 12/19/2023
+ms.date: 06/05/2025
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
@@ -31,13 +31,13 @@ This category contains the following entity:
         American Banker Association (ABA) transit routing numbers. Also returned with `domain=phi`.
 
         To get this entity category, add `ABARoutingNumber` to the `piiCategories` parameter. `ABARoutingNumber` will also be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="2":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+
    :::column-end:::
 :::row-end:::
 
@@ -59,13 +59,13 @@ This category contains the following entity:
         SWIFT codes for payment instruction information. Also returned with `domain=phi`.
 
         To get this entity category, add `SWIFTCode` to the `piiCategories` parameter. `SWIFTCode` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="2":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+
    :::column-end:::
 :::row-end:::
 
@@ -91,12 +91,12 @@ This category contains the following entity:
     :::column span="2":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+
    :::column-end:::
 :::row-end:::
 
-## Category: International Banking Account Number (IBAN) 
+## Category: International Banking Account Number (IBAN)
 
 This category contains the following entity:
 
@@ -113,47 +113,47 @@ This category contains the following entity:
         IBAN codes for payment instruction information. Also returned with `domain=phi`.
 
         To get this entity category, add `InternationalBankingAccountNumber` to the `piiCategories` parameter. `InternationalBankingAccountNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="2":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
-      
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+
    :::column-end:::
 :::row-end:::
 
 ## Government and country/region-specific identification
 
 > [!NOTE]
-> The following financial and country/region-specific entities are not returned with the `domain=phi` parameter:
+> The following financial and country/region-specific entities aren't returned with the `domain=phi` parameter:
 > * Passport numbers
 > * Tax IDs
 
-The following entities are grouped and listed by country/region:
+The following entities are listed via country and/or region:
 
 ### Argentina
 
 :::row:::
     :::column span="":::
         **Entity**
 
-        Argentina National Identity (DNI) Number 
+        Argentina National Identity (DNI) Number
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
         Also returned with `domain=phi`.
-        
+
         To get this entity category, add `ARNationalIdentityNumber` to the `piiCategories` parameter. `ARNationalIdentityNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -171,13 +171,13 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `ATIdentityCard` to the `piiCategories` parameter. `ATIdentityCard` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -189,12 +189,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `ATTaxIdentificationNumber` to the `piiCategories` parameter. `ATTaxIdentificationNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -206,12 +206,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `ATValueAddedTaxNumber` to the `piiCategories` parameter. `ATValueAddedTaxNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -230,14 +230,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `AUBankAccountNumber` to the `piiCategories` parameter. `AUBankAccountNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -249,12 +249,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `AUBusinessNumber` to the `piiCategories` parameter. `AUBusinessNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -266,30 +266,30 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `AUCompanyNumber` to the `piiCategories` parameter. `AUCompanyNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
     :::column span="":::
 
-        Australia driver's license  
+        Australia driver's license
 
     :::column-end:::
     :::column span="2":::
 
         To get this entity category, add `AUDriversLicenseNumber` to the `piiCategories` parameter. `AUDriversLicenseNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -301,13 +301,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `AUMedicalAccountNumber` to the `piiCategories` parameter. `AUMedicalAccountNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -319,12 +319,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `AUPassportNumber` to the `piiCategories` parameter. `AUPassportNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -336,12 +336,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `AUTaxFileNumber` to the `piiCategories` parameter. `AUTaxFileNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -359,14 +359,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `BENationalNumber` to the `piiCategories` parameter. `BENationalNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -379,39 +379,39 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `BEValueAddedTaxNumber` to the `piiCategories` parameter. `BEValueAddedTaxNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
 
-### Brazil 
+### Brazil
 
 :::row:::
     :::column span="":::
         **Entity**
 
         Brazil legal entity number (CNPJ)
 
-        
+
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
         To get this entity category, add `BRLegalEntityNumber` to the `piiCategories` parameter. `BRLegalEntityNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -423,13 +423,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `BRCPFNumber` to the `piiCategories` parameter. `BRCPFNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -441,13 +441,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `BRNationalIDRG` to the `piiCategories` parameter. `BRNationalIDRG` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -464,14 +464,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `CABankAccountNumber` to the `piiCategories` parameter. `CABankAccountNumber` will be returned in the API response if detected.
-    
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -484,35 +484,35 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `CADriversLicenseNumber` to the `piiCategories` parameter. `CADriversLicenseNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
 
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
     :::column span="":::
 
         Canada health service number
 
-        
+
     :::column-end:::
 
     :::column span="2":::
 
         To get this entity category, add `CAHealthServiceNumber` to the `piiCategories` parameter. `CAHealthServiceNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
 
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -524,12 +524,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `CAPassportNumber` to the `piiCategories` parameter. `CAPassportNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -543,12 +543,12 @@ The following entities are grouped and listed by country/region:
         To get this entity category, add `CAPersonalHealthIdentification` to the `piiCategories` parameter. `CAPersonalHealthIdentification` will be returned in the API response if detected.
 
         Also returned with `domain=phi`.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -560,17 +560,17 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `CASocialInsuranceNumber` to the `piiCategories` parameter. `CASocialInsuranceNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
-### Chile 
+### Chile
 
 :::row:::
     :::column span="":::
@@ -583,14 +583,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `CLIdentityCardNumber` to the `piiCategories` parameter. `CLIdentityCardNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -607,14 +607,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `CNResidentIdentityCardNumber` to the `piiCategories` parameter. `CNResidentIdentityCardNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -632,14 +632,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `EUDebitCardNumber` to the `piiCategories` parameter. `EUDebitCardNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -651,13 +651,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `EUDriversLicenseNumber` to the `piiCategories` parameter. `EUDriversLicenseNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -669,12 +669,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `EUGPSCoordinates` to the `piiCategories` parameter. `EUGPSCoordinates` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -686,13 +686,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `EUNationalIdentificationNumber` to the `piiCategories` parameter. `EUNationalIdentificationNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -704,12 +704,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `EUPassportNumber` to the `piiCategories` parameter. `EUPassportNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -721,13 +721,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `EUSocialSecurityNumber` to the `piiCategories` parameter. `EUSocialSecurityNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -739,12 +739,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `EUTaxIdentificationNumber` to the `piiCategories` parameter. `EUTaxIdentificationNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -761,14 +761,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `FRDriversLicenseNumber` to the `piiCategories` parameter. `FRDriversLicenseNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -780,12 +780,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `FRHealthInsuranceNumber` to the `piiCategories` parameter. `FRHealthInsuranceNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -797,13 +797,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `FRNationalID` to the `piiCategories` parameter. `FRNationalID` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -815,12 +815,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `FRPassportNumber` to the `piiCategories` parameter. `FRPassportNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -832,13 +832,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `FRSocialSecurityNumber` to the `piiCategories` parameter. `FRSocialSecurityNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -850,12 +850,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `FRTaxIdentificationNumber` to the `piiCategories` parameter. `FRTaxIdentificationNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -867,12 +867,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `FRValueAddedTaxNumber` to the `piiCategories` parameter. `FRValueAddedTaxNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -889,14 +889,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `DEDriversLicenseNumber` to the `piiCategories` parameter. `DEDriversLicenseNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -908,13 +908,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `DEIdentityCardNumber` to the `piiCategories` parameter. `DEIdentityCardNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -926,12 +926,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `DEPassportNumber` to the `piiCategories` parameter. `DEPassportNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -943,12 +943,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `DETaxIdentificationNumber` to the `piiCategories` parameter. `DETaxIdentificationNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -961,12 +961,12 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `DEValueAddedNumber` to the `piiCategories` parameter. `DEValueAddedNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -983,14 +983,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `HKIdentityCardNumber` to the `piiCategories` parameter. `HKIdentityCardNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1007,13 +1007,13 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `HUPersonalIdentificationNumber` to the `piiCategories` parameter. `HUPersonalIdentificationNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1025,12 +1025,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `HUTaxIdentificationNumber` to the `piiCategories` parameter. `HUTaxIdentificationNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1042,12 +1042,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `HUValueAddedNumber` to the `piiCategories` parameter. `HUValueAddedNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1064,14 +1064,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `INPermanentAccount` to the `piiCategories` parameter. `INPermanentAccount` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1084,13 +1084,13 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `INUniqueIdentificationNumber` to the `piiCategories` parameter. `INUniqueIdentificationNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1109,14 +1109,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `IDIdentityCardNumber` to the `piiCategories` parameter. `IDIdentityCardNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1133,14 +1133,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `IEPersonalPublicServiceNumber` to the `piiCategories` parameter. `IEPersonalPublicServiceNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1157,13 +1157,13 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `ILNationalID` to the `piiCategories` parameter. `ILNationalID` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1175,13 +1175,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `ILBankAccountNumber` to the `piiCategories` parameter. `ILBankAccountNumber` will be returned in the API response if detected.
-    
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1198,14 +1198,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `ITDriversLicenseNumber` to the `piiCategories` parameter. `ITDriversLicenseNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1217,12 +1217,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `ITFiscalCode` to the `piiCategories` parameter. `ITFiscalCode` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1234,12 +1234,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `ITValueAddedTaxNumber` to the `piiCategories` parameter. `ITValueAddedTaxNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1257,14 +1257,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `JPBankAccountNumber` to the `piiCategories` parameter. `JPBankAccountNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1276,13 +1276,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `JPDriversLicenseNumber` to the `piiCategories` parameter. `JPDriversLicenseNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1294,12 +1294,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `JPMyNumberPersonal` to the `piiCategories` parameter. `JPMyNumberPersonal` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1311,12 +1311,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `JPMyNumberCorporate` to the `piiCategories` parameter. `JPMyNumberCorporate` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1328,13 +1328,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `JPResidentRegistrationNumber` to the `piiCategories` parameter. `JPResidentRegistrationNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
      `ja`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1346,13 +1346,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `JPResidenceCardNumber` to the `piiCategories` parameter. `JPResidenceCardNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1364,13 +1364,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `JPSocialInsuranceNumber` to the `piiCategories` parameter. `JPSocialInsuranceNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1382,12 +1382,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `JPPassportNumber` to the `piiCategories` parameter. `JPPassportNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1404,13 +1404,13 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `LUNationalIdentificationNumberNatural` to the `piiCategories` parameter. `LUNationalIdentificationNumberNatural` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1422,12 +1422,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `LUNationalIdentificationNumberNonNatural` to the `piiCategories` parameter. `LUNationalIdentificationNumberNonNatural` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1444,13 +1444,13 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `MTIdentityCardNumber` to the `piiCategories` parameter. `MTIdentityCardNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1462,12 +1462,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `MTTaxIDNumber` to the `piiCategories` parameter. `MTTaxIDNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1485,13 +1485,13 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `NZBankAccountNumber` to the `piiCategories` parameter. `NZBankAccountNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1503,12 +1503,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `NZDriversLicenseNumber` to the `piiCategories` parameter. `NZDriversLicenseNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1520,12 +1520,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `NZInlandRevenueNumber` to the `piiCategories` parameter. `NZInlandRevenueNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1537,13 +1537,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `NZMinistryOfHealthNumber` to the `piiCategories` parameter. `NZMinistryOfHealthNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1555,12 +1555,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `NZSocialWelfareNumber` to the `piiCategories` parameter. `NZSocialWelfareNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1578,18 +1578,18 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `PHUnifiedMultiPurposeIDNumber` to the `piiCategories` parameter. `PHUnifiedMultiPurposeIDNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
-### Portugal 
+### Portugal
 
 :::row:::
     :::column span="":::
@@ -1602,14 +1602,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `PTCitizenCardNumber` to the `piiCategories` parameter. `PTCitizenCardNumber` will be returned in the API response if detected.
-          
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1621,13 +1621,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `PTTaxIdentificationNumber` to the `piiCategories` parameter. `PTTaxIdentificationNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1644,13 +1644,13 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `PTTaxIdentificationNumber` to the `piiCategories` parameter. `PTTaxIdentificationNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `zh-hans`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1668,14 +1668,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `ZAIdentificationNumber` to the `piiCategories` parameter. `ZAIdentificationNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1693,14 +1693,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `KRResidentRegistrationNumber` to the `piiCategories` parameter. `KRResidentRegistrationNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1717,13 +1717,13 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `ESDNI` to the `piiCategories` parameter. `ESDNI` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1735,13 +1735,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `ESSocialSecurityNumber` to the `piiCategories` parameter. `ESSocialSecurityNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1753,15 +1753,15 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `ESTaxIdentificationNumber` to the `piiCategories` parameter. `ESTaxIdentificationNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
- 
+
 ### Switzerland
 
 :::row:::
@@ -1775,18 +1775,18 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `CHSocialSecurityNumber` to the `piiCategories` parameter. `CHSocialSecurityNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
 
-### Taiwan 
+### Taiwan
 
 :::row:::
     :::column span="":::
@@ -1799,14 +1799,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `TWNationalID` to the `piiCategories` parameter. `TWNationalID` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1818,13 +1818,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `TWResidentCertificate` to the `piiCategories` parameter. `TWResidentCertificate` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1836,12 +1836,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `TWPassportNumber` to the `piiCategories` parameter. `TWPassportNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1858,16 +1858,16 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `UKDriversLicenseNumber` to the `piiCategories` parameter. `UKDriversLicenseNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
     :::column-end:::
-    
+
 :::row-end:::
 :::row:::
     :::column span="":::
@@ -1878,13 +1878,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `UKElectoralRollNumber` to the `piiCategories` parameter. `UKElectoralRollNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1896,13 +1896,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `UKNationalHealthNumber` to the `piiCategories` parameter. `UKNationalHealthNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1914,13 +1914,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `UKNationalInsuranceNumber` to the `piiCategories` parameter. `UKNationalInsuranceNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1932,12 +1932,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `USUKPassportNumber` to the `piiCategories` parameter. `USUKPassportNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1949,12 +1949,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `UKUniqueTaxpayerNumber` to the `piiCategories` parameter. `UKUniqueTaxpayerNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 
@@ -1972,14 +1972,14 @@ The following entities are grouped and listed by country/region:
         **Details**
 
         To get this entity category, add `USSocialSecurityNumber` to the `piiCategories` parameter. `USSocialSecurityNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
       **Supported languages**
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -1991,13 +1991,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `USDriversLicenseNumber` to the `piiCategories` parameter. `USDriversLicenseNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -2009,12 +2009,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `USUKPassportNumber` to the `piiCategories` parameter. `USUKPassportNumber` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -2026,12 +2026,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `USIndividualTaxpayerIdentification` to the `piiCategories` parameter. `USIndividualTaxpayerIdentification` will be returned in the API response if detected.
-      
+
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -2043,13 +2043,13 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `DrugEnforcementAgencyNumber` to the `piiCategories` parameter. `DrugEnforcementAgencyNumber` will be returned in the API response if detected.
-      
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
 :::row:::
@@ -2061,12 +2061,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `USBankAccountNumber` to the `piiCategories` parameter. `USBankAccountNumber` will be returned in the API response if detected.
-        
+
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
 
       `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
-      
+
    :::column-end:::
 :::row-end:::
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "個人情報に関連する識別エンティティ情報の完全な改訂"
}
```

### Explanation
このコードの差分は、`identification-entities.md` 文書の全面的な改訂を示しています。全内容が都度見直され、新しい情報が統合されて、古い情報は削除されました。エンティティカテゴリに関連する情報が更新され、各カテゴリに対する詳細な説明やそれらの取得方法が改訂されました。

特に、個々のエンティティに関連する国や地域ごとの識別番号、翻訳可能なサポート言語が明確に整理され、より多くのエンティティが追加されました。また、全体的なテキストの言語がより明確で読みやすくなっています。

さらに、日付が更新され、文書の有効性が保たれています。これにより、ユーザーは最新の情報と手順に基づいて個人情報の識別に関する機能を利用しやすくなり、より正確なレスポンスを期待できるようになります。

## articles/ai-services/language-service/question-answering/how-to/network-isolation.md{#item-8445fc}

<details>
<summary>Diff</summary>
````diff
@@ -5,13 +5,13 @@ ms.service: azure-ai-language
 ms.topic: how-to
 author: laujan
 ms.author: lajanuar
-ms.date: 11/21/2024
+ms.date: 06/06/2025
 ms.custom: language-service-question-answering
 ---
 
 #  Network isolation and private endpoints
 
-The steps below describe how to restrict public access to custom question answering resources as well as how to enable Azure Private Link. Protect an AI Foundry resource from public access by [configuring the virtual network](../../../cognitive-services-virtual-networks.md?tabs=portal).
+The following steps describe how to restrict public access to custom question answering resources as well as how to enable Azure Private Link. Protect an AI Foundry resource from public access by [configuring the virtual network](../../../cognitive-services-virtual-networks.md?tabs=portal).
 
 ## Private Endpoints
 
@@ -21,12 +21,12 @@ Private endpoints are provided by [Azure Private Link](/azure/private-link/priva
 
 ## Steps to enable private endpoint
 
-1. Assign *Contributor* role to language resource (Depending on the context this may appear as a Text Analytics resource) in the Azure Search Service instance. This operation requires *Owner* access to the subscription. Go to Identity tab in the service resource to get the identity.
+1. Assign the *contributor* role to your resource in the Azure Search Service instance. This operation requires *Owner* access to the subscription. Go to Identity tab in the service resource to get the identity.
 
 > [!div class="mx-imgBorder"]
 > ![Text Analytics Identity](../../../QnAMaker/media/qnamaker-reference-private-endpoints/private-endpoints-identity.png)
 
-2. Add the above identity as *Contributor* by going to Azure Search Service IAM tab.
+2. Add the above identity as *Contributor* by going to the Azure Search Service access control tab.
 
 ![Managed service IAM](../../../QnAMaker/media/qnamaker-reference-private-endpoints/private-endpoint-access-control.png)
 
@@ -54,9 +54,9 @@ This will establish a private endpoint connection between language resource and
 
 ## Restrict access to Azure AI Search resource
 
-Follow the steps below to restrict public access to custom question answering language resources. Protect an AI Foundry resource from public access by [configuring the virtual network](../../../cognitive-services-virtual-networks.md?tabs=portal).
+Follow these steps to restrict public access to custom question answering language resources. Protect an AI Foundry resource from public access by [configuring the virtual network](../../../cognitive-services-virtual-networks.md?tabs=portal).
 
-After restricting access to an AI Foundry resource based on VNet, To browse projects on Language Studio from your on-premises network or your local browser.
+After you restrict access to an AI Foundry resource based on virtual network, to browse projects on Language Studio from your on-premises network or your local browser:
 - Grant access to [on-premises network](../../../cognitive-services-virtual-networks.md?tabs=portal#configure-access-from-on-premises-networks).
 - Grant access to your [local browser/machine](../../../cognitive-services-virtual-networks.md?tabs=portal#managing-ip-network-rules).
 - Add the **public IP address of the machine  under the Firewall** section of the **Networking** tab. By default `portal.azure.com` shows the current browsing machine's public IP (select this entry) and then select **Save**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ネットワーク隔離に関する手順の改訂"
}
```

### Explanation
このコードの差分は、`network-isolation.md` 文書に関する修正を示しています。文書は最新の情報に更新され、文体や言葉遣いの明確さが向上している点が特徴です。具体的には、役割の名称や操作手順が少し簡潔に表現され、読み手にとって理解しやすくなっています。

例えば、「*Contributor* role」が「*contributor* role」に変更され、より一貫したスタイルを維持しています。また、特定のタブの表現を明確に修正し、利便性を向上させています。

全編にわたって言い回しが改善され、内容が滑らかに流れるようになりました。この更新は、ネットワークの隔離設定に関する手順をより使いやすくし、ユーザーが目的の操作を効率的に実行するのに役立つことを目的としています。


