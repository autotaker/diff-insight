---
date: '2024-10-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0bc728f...MicrosoftDocs:ceba2b5
summary: このコードの更新では、エンティティカテゴリーのサポートが拡張され、多言語対応が強化されました。また、画像ファイルに関連するメタデータの調整やクイックスタートガイドの内容が更新されています。特に重要な変更として、画像ファイル「playground-settings-select-language.png」の削除があります。全体として、これらの変更はAzure
  AI Studioの利用をより効果的にし、ユーザー体験の向上につながることが期待されます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0bc728f...MicrosoftDocs:ceba2b5){target="_blank"}

# Highlights
このコードの更新では、エンティティカテゴリーのサポートが拡張され、多言語対応が強化されました。また、画像ファイルに関連するメタデータの調整やクイックスタートガイドの内容が更新されています。一つの重大な変更として、特定の画像ファイルが削除されています。

## 新機能
- エンティティカテゴリーの拡張と新しい言語サポート
- クイックスタートドキュメントの内容および手順の改善

## ブレイキングチェンジ
- 画像ファイル「playground-settings-select-language.png」の削除

## その他の更新
- 複数の画像ファイルに対するメタデータなどの調整
- クイックスタートガイドの更新により、ユーザー体験の向上

# Insights
この記事は、Azure AI Servicesの言語サービスとAIスタジオ関連のドキュメントとメディアファイルの更新に関するものです。特に、エンティティカテゴリーの新言語追加は、多様なユーザーに対してAIサービスの利用の幅を広げるものであり、エンドユーザーが様々な言語で自然にアクセスできるようにする長期的な改善を示しています。

画像ファイルのメタデータ調整は、ドキュメントの整合性維持に寄与し、迅速なプロジェクト管理を可能にします。ただし、画像ファイル「playground-settings-select-language.png」の削除は、ドキュメントが不完全になるリスクを伴い、早期の代替情報の提供が必要です。

クイックスタートドキュメントの更新は、ユーザーが最新のインターフェースに基づいたガイドラインを得られるようにし、ユーザビリティの向上を図るものです。これらの変更は、Azure AI Studioの利用をスムーズにし、ユーザーがAIサービスをより効果的に活用できるよう設計されています。これにより、Azure AIの利用拡大とユーザーエンゲージメント向上に繋がると考えられます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [entity-categories.md](#item-ba2623) | minor update | エンティティカテゴリーとサポートされている言語の更新 | modified | 38 | 19 | 57 | 
| [identification-entities.md](#item-9bf762) | minor update | サポートされている言語の拡張 | modified | 142 | 136 | 278 | 
| [chat-session-hear-response-natural.png](#item-a108c3) | minor update | 画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [chat-session-hear-response.png](#item-72bde8) | minor update | 画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [chat-session-speaking.png](#item-717e25) | minor update | 画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [chat-session-view-code-button.png](#item-7f1611) | minor update | 画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [chat-session-view-code.png](#item-055e0e) | minor update | 画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [playground-config-deployment.png](#item-04d5ed) | minor update | 画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [playground-settings-enable-speech.png](#item-6c35f3) | minor update | 画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [playground-settings-select-language.png](#item-faefab) | breaking change | 画像ファイルの削除 | removed | 0 | 0 | 0 | 
| [playground-settings-select.png](#item-1d682f) | minor update | 画像ファイルの更新 | modified | 0 | 0 | 0 | 
| [hear-speak-playground.md](#item-3167bc) | minor update | クイックスタートの内容更新 | modified | 11 | 16 | 27 | 


# Modified Contents
## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories.md{#item-ba2623}

<details>
<summary>Diff</summary>
````diff
@@ -48,7 +48,7 @@ This category contains the following entity:
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`   
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`    
       
    :::column-end:::
 :::row-end:::
@@ -77,7 +77,7 @@ This category contains the following entity:
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`  
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
       
    :::column-end:::
 :::row-end:::
@@ -135,7 +135,7 @@ This category contains the following entity:
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`  
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
       
    :::column-end:::
 
@@ -236,7 +236,7 @@ This category contains the following entity:
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
       
     :::column-end:::
 
@@ -264,7 +264,7 @@ This category contains the following entity:
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
+      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
       
     :::column-end:::
 :::row-end:::
@@ -293,7 +293,7 @@ This category contains the following entity:
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
+      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
       
     :::column-end:::
 
@@ -322,7 +322,7 @@ This category contains the following entity:
     :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
+      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
       
     :::column-end:::
 :::row-end:::
@@ -349,7 +349,7 @@ This category contains the following entities:
 :::column span="":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
       
    :::column-end:::
 :::row-end:::
@@ -376,12 +376,31 @@ The entity in this category can have the following subcategories.
     :::column span="2":::
       **Supported languages**
       
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`   
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`     
       
     :::column-end:::
 :::row-end:::
 
+:::row:::
+    :::column span="":::
+
+        DateAndTime
+        
+
+    :::column-end:::
+    :::column span="2":::
+
+        Dates and times of day.
+
+        To get this entity category, add DateAndTime to the piiCategories parameter. DateAndTime will be returned in the API response if detected.
 
+
+    :::column-end:::
+    :::column span="2":::
+      **Supported languages**
+      
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
+      
 ## Subcategory: Age
 
 The PII service supports the Age subcategory within the broader Quantity category (since Age is the personally identifiable piece of information). 
@@ -402,7 +421,7 @@ The PII service supports the Age subcategory within the broader Quantity categor
     :::column span="2":::
       **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`   
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
       
    :::column-end:::
 :::row-end:::
@@ -429,7 +448,7 @@ These entity categories include identifiable Azure information like authenticati
     :::column span="":::
       **Supported languages**
 
-      `en` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
     :::column-end:::
 :::row-end:::
@@ -449,7 +468,7 @@ These entity categories include identifiable Azure information like authenticati
     :::column-end:::
     :::column span="":::
 
-      `en` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
     :::column-end:::
 :::row-end:::
@@ -468,7 +487,7 @@ These entity categories include identifiable Azure information like authenticati
     :::column-end:::
     :::column span="":::
 
-      `en` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
     :::column-end:::
 :::row-end:::
@@ -487,7 +506,7 @@ These entity categories include identifiable Azure information like authenticati
     :::column-end:::
     :::column span="":::
 
-      `en` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
     :::column-end:::
 :::row-end:::
@@ -506,7 +525,7 @@ These entity categories include identifiable Azure information like authenticati
     :::column-end:::
     :::column span="":::
 
-      `en` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
     :::column-end:::
 :::row-end:::
@@ -525,7 +544,7 @@ These entity categories include identifiable Azure information like authenticati
     :::column-end:::
     :::column span="":::
 
-      `en` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
     :::column-end:::
 :::row-end:::
@@ -544,7 +563,7 @@ These entity categories include identifiable Azure information like authenticati
     :::column-end:::
     :::column span="":::
 
-      `en` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
     :::column-end:::
 :::row-end:::
@@ -563,7 +582,7 @@ These entity categories include identifiable Azure information like authenticati
     :::column-end:::
     :::column span="":::
 
-      `en` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
     :::column-end:::
 :::row-end:::
@@ -582,7 +601,7 @@ These entity categories include identifiable Azure information like authenticati
     :::column-end:::
     :::column span="":::
 
-      `en` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
 
     :::column-end:::
 :::row-end:::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティカテゴリーとサポートされている言語の更新"
}
```

### Explanation
この変更は、ドキュメント内のエンティティカテゴリーとそのサポートされている言語のリストを更新するもので、より多くの言語が追加されました。具体的には、元の文書にあった言語リストに対して、新たに多くの言語が追加され、全体でサポートされる言語の数が増加しました。特に、`nl`（オランダ語）、`sv`（スウェーデン語）、`tr`（トルコ語）、`hi`（ヒンディー語）など、様々な言語が含まれています。

また、いくつかのセクションで特定のコンセプトに対するサポートが新たに言及され、APIレスポンスでの識別が可能なエンティティカテゴリとして「DateAndTime」が追加されました。この変更は、言語サービスにおける多言語対応を強化し、より幅広いユーザーに利用できるようにすることを目的としています。全体として、元の38行の追加情報は、情報の明確さを高めつつ、エンドユーザーに対する利便性を向上させています。

## articles/ai-services/language-service/personally-identifiable-information/includes/identification-entities.md{#item-9bf762}

<details>
<summary>Diff</summary>
````diff
@@ -35,9 +35,9 @@ This category contains the following entity:
       
     :::column-end:::
     :::column span="2":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
       
    :::column-end:::
 :::row-end:::
@@ -63,9 +63,9 @@ This category contains the following entity:
       
     :::column-end:::
     :::column span="2":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `ja`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
       
    :::column-end:::
 :::row-end:::
@@ -90,9 +90,9 @@ This category contains the following entity:
 
     :::column-end:::
     :::column span="2":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `ja`,	`zh-hans`, `ja`, `ko`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
       
    :::column-end:::
 :::row-end:::
@@ -117,9 +117,9 @@ This category contains the following entity:
       
     :::column-end:::
     :::column span="2":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`  
       
    :::column-end:::
 :::row-end:::
@@ -144,15 +144,16 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="2":::
         **Details**
+
         Also returned with `domain=phi`.
         
         To get this entity category, add `ARNationalIdentityNumber` to the `piiCategories` parameter. `ARNationalIdentityNumber` will be returned in the API response if detected.
       
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`, `es`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -174,9 +175,9 @@ The following entities are grouped and listed by country/region:
       
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `de`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -193,7 +194,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `de`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -210,7 +211,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `de`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -234,9 +235,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -253,7 +254,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -270,7 +271,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -288,7 +289,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -306,7 +307,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -323,7 +324,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -340,7 +341,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -363,9 +364,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `fr`, `de`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -382,9 +383,12 @@ The following entities are grouped and listed by country/region:
         To get this entity category, add `BENationalNumberV2` to the `piiCategories` parameter. `BENationalNumberV2` will be returned in the API response if detected.
       
         Also returned with `domain=phi`.
+
+        This entity is deprecated
+
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
       `fr`, `de`
       
@@ -404,7 +408,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `fr`, `de`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -429,9 +433,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `pt-pt`, `pt-br`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -449,7 +453,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `pt-pt`, `pt-br`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -467,7 +471,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `pt-pt`, `pt-br`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -489,9 +493,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`, `fr`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -511,7 +515,7 @@ The following entities are grouped and listed by country/region:
 
     :::column span="":::
 
-      `en`, `fr`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -532,7 +536,7 @@ The following entities are grouped and listed by country/region:
 
     :::column span="":::
 
-      `en`, `fr`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -549,7 +553,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`, `fr`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -568,7 +572,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`, `fr`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -586,7 +590,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`, `fr`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -608,9 +612,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `es`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -632,9 +636,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `zh-hans`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -657,9 +661,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -677,7 +681,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -694,7 +698,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -712,7 +716,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -729,7 +733,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -747,7 +751,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -764,7 +768,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -786,9 +790,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `fr` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -805,7 +809,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `fr` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -823,7 +827,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `fr` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -840,7 +844,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `fr` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -858,7 +862,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `fr` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -875,7 +879,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `fr` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -892,7 +896,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `fr` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -914,9 +918,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `de` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -934,7 +938,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `de`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -951,7 +955,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `de` 
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -968,7 +972,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `de`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -986,7 +990,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `de`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1008,9 +1012,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1031,9 +1035,9 @@ The following entities are grouped and listed by country/region:
       
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1050,7 +1054,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1067,7 +1071,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1089,9 +1093,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1110,7 +1114,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1134,9 +1138,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1158,9 +1162,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1173,10 +1177,12 @@ The following entities are grouped and listed by country/region:
     :::column span="2":::
 
         To get this entity category, add `IEPersonalPublicServiceNumberV2` to the `piiCategories` parameter. `IEPersonalPublicServiceNumberV2` will be returned in the API response if detected.
+
+        This entity is deprecated
       
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
       `en`
       
@@ -1199,9 +1205,9 @@ The following entities are grouped and listed by country/region:
       
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1219,7 +1225,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1241,9 +1247,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `it`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1260,7 +1266,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `it`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1277,7 +1283,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `it`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1300,9 +1306,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `ja`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1320,7 +1326,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `ja`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1337,7 +1343,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `ja`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1354,7 +1360,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `ja`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1390,7 +1396,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `ja`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1408,7 +1414,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `ja`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1425,7 +1431,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `ja`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1446,9 +1452,9 @@ The following entities are grouped and listed by country/region:
       
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `fr`, `de`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1465,7 +1471,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `fr`, `de`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1486,9 +1492,9 @@ The following entities are grouped and listed by country/region:
       
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1505,7 +1511,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1527,9 +1533,9 @@ The following entities are grouped and listed by country/region:
       
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1546,7 +1552,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1563,7 +1569,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1581,7 +1587,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1598,7 +1604,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1621,9 +1627,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1645,9 +1651,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `pt-pt`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1665,7 +1671,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `pt-pt`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1686,7 +1692,7 @@ The following entities are grouped and listed by country/region:
       
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
       `en`, `zh-hans`
       
@@ -1711,9 +1717,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1736,9 +1742,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `ko`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1759,9 +1765,9 @@ The following entities are grouped and listed by country/region:
       
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `es`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1779,7 +1785,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `es`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1796,7 +1802,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `es`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1817,9 +1823,9 @@ The following entities are grouped and listed by country/region:
       
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `fr`, `de`, `it`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1842,9 +1848,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1862,7 +1868,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1879,7 +1885,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1901,9 +1907,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
     :::column-end:::
     
@@ -1940,7 +1946,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1958,7 +1964,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -1992,7 +1998,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -2015,9 +2021,9 @@ The following entities are grouped and listed by country/region:
         Also returned with `domain=phi`.
     :::column-end:::
     :::column span="":::
-      **Supported document languages**
+      **Supported languages**
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -2035,7 +2041,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -2052,7 +2058,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -2069,7 +2075,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -2087,7 +2093,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
@@ -2105,7 +2111,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="":::
 
-      `en`
+      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
       
    :::column-end:::
 :::row-end:::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サポートされている言語の拡張"
}
```

### Explanation
この変更は、ドキュメント内のエンティティに関連するサポート言語のリストを拡張するために行われました。元々は限られた数の言語が記載されていましたが、変更後は多くの言語が追加され、より多くのユーザーに対応できるようになっています。

具体的には、元の「Supported document languages」のタイトルが「Supported languages」に変更され、言語のリストには多様な言語が追加されています。例えば、英語（`en`）、スペイン語（`es`）、フランス語（`fr`）、ドイツ語（`de`）、イタリア語（`it`）、ポルトガル語（`pt-pt`, `pt-br`）、中国語（`zh`）、日本語（`ja`）、韓国語（`ko`）、オランダ語（`nl`）など、合計で50を超える言語が含まれています。

この変更の目的は、ユーザーが利用する際の言語の選択肢を広げ、より多くの地域や言語圏のニーズに応えることです。全体として、言語サービスの利用がよりフレキシブルで包括的になることを意図しています。

## articles/ai-studio/media/quickstarts/hear-speak/chat-session-hear-response-natural.png{#item-a108c3}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの更新"
}
```

### Explanation
この変更は、特定の画像ファイルに関するもので、ファイル自体の内容は更新されていませんが、メタデータや配置に関連する更新が行われた可能性があります。ファイル名は「chat-session-hear-response-natural.png」で、Azure AI Studioに関連するコンテンツの一部として使用されています。

現在の状態では、ファイルの追加や削除はなく、変更内容もありませんが、今後の参照や利用に向けた準備が整ったことで、ドキュメント全体の整合性が向上したと考えられます。このような軽微な更新は、プロジェクトの維持管理やリソースの整理において必要な作業の一環であり、将来の改善に向けた基盤を作るものです。

## articles/ai-studio/media/quickstarts/hear-speak/chat-session-hear-response.png{#item-72bde8}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの更新"
}
```

### Explanation
この変更は、画像ファイル「chat-session-hear-response.png」に関連しており、ファイル自体の中身についての変更はありません。具体的には、ファイルに対する追加や削除、そして内容の変更も行われていません。

ただし、この画像はAzure AI Studioのクイックスタートガイドに関連するものであり、ドキュメントの整合性や構造の中での位置付けに応じて何らかの調整やメタデータの更新が行われた可能性があります。このようなマイナーなアップデートは、プロジェクトのメンテナンスを支援し、資源の管理やドキュメント全体の品質を保つために重要です。

## articles/ai-studio/media/quickstarts/hear-speak/chat-session-speaking.png{#item-717e25}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの更新"
}
```

### Explanation
この変更は、画像ファイル「chat-session-speaking.png」に関連しています。ファイルに対する追加、削除、または内容の変更は行われていませんが、ファイルのメタデータや整理に関する更新があった可能性があります。

この画像は、Azure AI Studioのクイックスタートガイドの一部として利用されており、ドキュメントの整合性を保つためのメンテナンス作業の一環と考えられます。このようなマイナーな更新は、ドキュメント全体の品質向上やプロジェクト管理において重要なステップといえます。

## articles/ai-studio/media/quickstarts/hear-speak/chat-session-view-code-button.png{#item-7f1611}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの更新"
}
```

### Explanation
この変更は、画像ファイル「chat-session-view-code-button.png」に対するものであり、ファイル自体の中身に変更はありません。具体的には、追加、削除、または内容の変更は行われていない状態です。

この画像はAzure AI Studioのクイックスタートガイドに関連しており、ドキュメント全体の整合性や見栄えを維持するためのマイナーな更新と考えられます。こうした小規模な変更は、ドキュメントの品質向上やプロジェクトの管理において重要な役割を果たします。

## articles/ai-studio/media/quickstarts/hear-speak/chat-session-view-code.png{#item-055e0e}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの更新"
}
```

### Explanation
この変更は、画像ファイル「chat-session-view-code.png」に関連しており、ファイルに対する追加、削除、または内容の変更は行われていません。具体的には、ファイル自体の内容に変化はなく、全体的なメタデータの更新や管理上の調整が行われた可能性があります。

この画像はAzure AI Studioのクイックスタートにおける重要な要素であり、ドキュメントの品質を維持するために必要なマイナーな更新として位置づけられます。このような小規模な変更は、ドキュメントが一貫したメッセージとビジュアルを提供し続けるために不可欠です。

## articles/ai-studio/media/quickstarts/hear-speak/playground-config-deployment.png{#item-04d5ed}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの更新"
}
```

### Explanation
この変更は、画像ファイル「playground-config-deployment.png」に関連しています。この変更では、ファイルの中身自体に変更はありません。具体的には、追加、削除、または内容の変更が行われていないため、ファイルの構成や外観に影響を与えることはありません。

この画像はAzure AI Studioのクイックスタートにおいて重要な役割を果たしており、マイナーな更新が行われたことで、文書全体の整合性を保つことが意図されています。このような小規模な変更は、ドキュメントの整った状態を維持し、ユーザーに一貫した情報を提供するために必要です。

## articles/ai-studio/media/quickstarts/hear-speak/playground-settings-enable-speech.png{#item-6c35f3}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの更新"
}
```

### Explanation
この変更は、画像ファイル「playground-settings-enable-speech.png」に関するもので、内容に変更はありません。この変更では、ファイルへの追加、削除、または著しい内容の変更は行われておらず、ファイルの外観や実用性には影響を及ぼさないと考えられます。

この画像はAzure AI Studioのクイックスタートセクションにおいて重要な情報を提供しており、コンテンツの整合性を保つために行われたマイナーアップデートです。この種の更新は、ドキュメントの品質を維持し、利用者が一貫した情報を得るために不可欠です。

## articles/ai-studio/media/quickstarts/hear-speak/playground-settings-select-language.png{#item-faefab}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "画像ファイルの削除"
}
```

### Explanation
この変更は、画像ファイル「playground-settings-select-language.png」を削除するもので、内容の追加や修正は行われていません。ファイルが完全に削除されたため、これに関連する情報やコンテンツは利用できなくなります。

この画像は、Azure AI Studioのクイックスタートにおいて言語選択に関する重要な役割を果たしていた可能性があり、その削除によりドキュメント内のいくつかの手順や説明が不完全になる恐れがあります。このようなブレイキングチェンジは、ユーザーに影響を及ぼす可能性があるため、特に注意が必要です。今後、削除された内容に替わる情報の提供や、他の画像での補完が求められるでしょう。

## articles/ai-studio/media/quickstarts/hear-speak/playground-settings-select.png{#item-1d682f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの更新"
}
```

### Explanation
この変更は、画像ファイル「playground-settings-select.png」に関するもので、具体的な内容の変更は報告されていませんが、ファイルが更新されていることを示しています。ファイルの追加、削除、または著しい内容の変更は見られません。

この更新は、Azure AI Studioのクイックスタートにおいて、ユーザーに対して設定選択に関連する視覚的な情報を提供するためのものであり、ドキュメントの全体的な品質や一貫性の維持に寄与します。この種のマイナーアップデートは、利用者に対して役立つ情報を常に提供するために重要です。今後の利用者に対して、より明確で効果的なガイダンスを提供するための材料として機能するでしょう。

## articles/ai-studio/quickstarts/hear-speak-playground.md{#item-3167bc}

<details>
<summary>Diff</summary>
````diff
@@ -8,16 +8,14 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: quickstart
-ms.date: 5/21/2024
+ms.date: 10/27/2024
 ms.reviewer: eur
 ms.author: eur
 author: eric-urban
 ---
 
 # Quickstart: Hear and speak with chat models in the AI Studio chat playground
 
-[!INCLUDE [feature-preview](../includes/feature-preview.md)]
-
 Give your app the ability to hear and speak by pairing Azure OpenAI Service with Azure AI Speech to enable richer interactions.
 
 In this quickstart, you use Azure OpenAI Service and Azure AI Speech to:
@@ -30,39 +28,36 @@ The speech to text and text to speech features can be used together or separatel
 ## Prerequisites
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
-- An [AI Studio hub](../how-to/create-azure-ai-resource.md) with a chat model deployed. For more information about model deployment, see the [resource deployment guide](../../ai-services/openai/how-to/create-resource.md).
-- An [AI Studio project](../how-to/create-projects.md). 
-
+- An [AI Studio project](../how-to/create-projects.md).
+- A deployed [Azure OpenAI](../how-to/deploy-models-openai.md) chat model. This guide is tested with a `gpt-4` model.
 
 ## Configure the chat playground
 
 Before you can start a chat session, you need to configure the chat playground to use the speech to text and text to speech features.
 
 1. Sign in to [Azure AI Studio](https://ai.azure.com).
 1. Go to your project or [create a new project](../how-to/create-projects.md) in Azure AI Studio. 
-1. Select **Playground** > **Chat** from the left pane.
+1. Select **Chat** from the list of playgrounds.
 1. Select your deployed chat model from the **Deployment** dropdown. 
 
     :::image type="content" source="../media/quickstarts/hear-speak/playground-config-deployment.png" alt-text="Screenshot of the chat playground with mode and deployment highlighted." lightbox="../media/quickstarts/hear-speak/playground-config-deployment.png":::
 
-1. Select the **Playground settings** button. 
+1. Select the **Chat capabilities** button. 
 
-    :::image type="content" source="../media/quickstarts/hear-speak/playground-settings-select.png" alt-text="Screenshot of the chat playground with options to get to the playground settings." lightbox="../media/quickstarts/hear-speak/playground-settings-select.png":::
+    :::image type="content" source="../media/quickstarts/hear-speak/playground-settings-select.png" alt-text="Screenshot of the chat playground with options to get to the chat capabilities settings." lightbox="../media/quickstarts/hear-speak/playground-settings-select.png":::
 
     > [!NOTE]
-    > You should also see the options to select the microphone or speaker buttons. If you select either of these buttons, but haven't yet enabled speech to text or text to speech, you are prompted to enable them in **Playground settings**. 
+    > You should also see the options to select the microphone or speaker buttons. If you select either of these buttons, but haven't yet enabled speech to text or text to speech, you are prompted to enable them in **Chat capabilities**. 
 
-1. On the **Playground Settings** page, select the box to acknowledge that usage of the speech feature will incur additional costs. For more information, see [Azure AI Speech pricing](https://azure.microsoft.com/pricing/details/cognitive-services/speech-services/).
+1. On the **Chat capabilities** page, select the box to acknowledge that usage of the speech feature will incur additional costs. For more information, see [Azure AI Speech pricing](https://azure.microsoft.com/pricing/details/cognitive-services/speech-services/).
 
 1. Select **Enable speech to text** and **Enable text to speech**.  
 
-    :::image type="content" source="../media/quickstarts/hear-speak/playground-settings-enable-speech.png" alt-text="Screenshot of the playground settings page." lightbox="../media/quickstarts/hear-speak/playground-settings-enable-speech.png":::
+    :::image type="content" source="../media/quickstarts/hear-speak/playground-settings-enable-speech.png" alt-text="Screenshot of the chat capabilities page." lightbox="../media/quickstarts/hear-speak/playground-settings-enable-speech.png":::
 
 1. Select the language locale and voice you want to use for speaking and hearing. The list of available voices depends on the locale that you select.
 
-    :::image type="content" source="../media/quickstarts/hear-speak/playground-settings-select-language.png" alt-text="Screenshot of the playground settings page with a voice that speaks Japanese selected." lightbox="../media/quickstarts/hear-speak/playground-settings-select-language.png":::
-
-1. Optionally you can enter some sample text and select **Play** to try the voice.
+1. Optionally, you can try the voice before you return to the chat session. Enter some sample text and select **Play** to 
 
 1. Select **Save**.
  
@@ -99,7 +94,7 @@ In this chat session, you use both speech to text and text to speech. You use th
 
 ## View sample code
 
-You can select the **View Code** button to view and copy the sample code, which includes configuration for Azure OpenAI and Speech services. 
+You can select the **View code** button to view and copy the sample code, which includes configuration for Azure OpenAI and Speech services. 
 
 :::image type="content" source="../media/quickstarts/hear-speak/chat-session-view-code-button.png" alt-text="Screenshot of the button to view sample code in the playground." lightbox="../media/quickstarts/hear-speak/chat-session-view-code-button.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートの内容更新"
}
```

### Explanation
この変更は、Markdownファイル「hear-speak-playground.md」における内容の更新を示しています。具体的には、11行の追加と16行の削除、そして27行の変更が行われています。

更新内容には、日付の更新や、機能の説明の修正が含まれており、特に「Playground settings」から「Chat capabilities」への用語変更が目立ちます。これにより、ユーザーがチャットモデルを設定する手順がより明確になり、最新のユーザーインターフェースに適応しています。

また、マークダウンの一部では、新しい手順が追加され、ユーザーが音声機能を有効にする際の流れが改善されています。このようなマイナーアップデートは、ユーザーエクスペリエンスを向上させるために重要であり、内容が最新であることを保証します。最終的には、ユーザビリティを高め、Azure AI Studioの利用を促進することに寄与します。


