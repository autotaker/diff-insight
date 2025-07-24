---
date: '2025-07-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e9c44be...MicrosoftDocs:bb78a31
summary: このコードの変更には、「エンティティコンポーネント」と「TOC（目次）」に関するマイナーな更新が含まれています。エンティティコンポーネントでは内容が明確化され使いやすさが向上し、TOCのYAMLファイルではC#関連の情報に関するアクセシビリティが改善されています。具体的には、エンティティの抽出方法や重複扱いに関する説明が追加され、古い「Text
  analysis」セクションが削除されました。これにより、情報のナビゲーションが効率化され、ユーザーが必要な情報に迅速にアクセスできるようになります。全体的な文書の改善は、ユーザビリティの向上と作業効率の促進につながります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e9c44be...MicrosoftDocs:bb78a31){target="_blank"}

# Highlights
このコードの変更には、「エンティティコンポーネント」と「TOC（目次）」の2つの文書部分に関するマイナーな更新が含まれています。「エンティティコンポーネント」では、内容が明確化され、使いやすさが向上しています。一方、TOCのYAMLファイルでは、セクションの項目名とリンクが最新化されており、特にC#関連の情報に関するアクセシビリティが向上しています。

## New features
- 「エンティティコンポーネント」文書において、エンティティの抽出方法と重複の扱いに関する説明が追加され、明確化。
- TOCファイルで、C#関連セクションに新しい項目とリンクが追加。

## Breaking changes
- TOC内の古い「Text analysis」セクションが削除され、新項目名に置き換え。

## Other updates
- 文書の全般的な言葉遣いや構文の改善により、読みやすさと情報の正確性が向上。

# Insights
この変更は、ユーザーがAIサービスに関連する重要な情報に、より効率的かつ理解しやすくアクセスできるようにすることを目的としています。「エンティティコンポーネント」についての説明が明確化されたことにより、ユーザーは具体的なエンティティ抽出方法やその結果の予測に関する理解を深めることができます。特に、大量のデータを扱う場合や、エンティティの予測が重複する複雑な状況でも、ユーザーが適切に対応できるような指針が提供されています。

さらに、TOCのアップデートにより、情報のナビゲーションが効率化されました。特にC#関連の情報が明確に区分けされることで、開発者は特定のAPIリファレンスやコンセプトに迅速にアクセスできるようになります。これらの変更は、ユーザビリティの向上とともに、ドキュメント構造の全体的な整理にも寄与しています。

これらの更新は、より洗練されたユーザーエクスペリエンスを提供し、AIサービスの効果的活用を促進することを目的としています。このような文書の改良は、技術者や開発者にとって大変価値が高く、作業効率の向上に直接結びつくポイントと言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [entity-components.md](#item-9168dd) | minor update | エンティティコンポーネントの内容更新 | modified | 11 | 10 | 21 | 
| [toc.yml](#item-12f1f0) | minor update | TOCの項目名とリンクの更新 | modified | 8 | 2 | 10 | 


# Modified Contents
## articles/ai-services/language-service/conversational-language-understanding/concepts/entity-components.md{#item-9168dd}

<details>
<summary>Diff</summary>
````diff
@@ -6,24 +6,24 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 06/04/2025
+ms.date: 07/22/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
 ---
 
 # Entity components
 
-In conversational language understanding, entities are relevant pieces of information that are extracted from your utterances. An entity can be extracted by different methods. They can be learned through context, matched from a list, or detected by a prebuilt recognized entity. Every entity in your project is composed of one or more of these methods, which are defined as your entity's components. 
+In conversational language understanding, entities are relevant pieces of information that are extracted from your utterances. You can extract an entity using several different methods. Entities can be detected through context, matched from a list, or detected by a prebuilt recognized entity. Every entity in your project is composed of one or more of these methods, which are defined as your entity's components.
 
-When an entity is defined by more than one component, their predictions can overlap. You can determine the behavior of an entity prediction when its components overlap by using a fixed set of options in the *entity options*.
+When more than one component defines an entity, predictions can overlap. You can determine the behavior of an entity prediction when its components overlap by using a fixed set of options in the *entity options*.
 
 ## Component types
 
 An entity component determines a way that you can extract the entity. An entity can contain one component, which determines the only method to be used to extract the entity. An entity can also contain multiple components to expand the ways in which the entity is defined and extracted.
 
 ### Learned component
 
-The learned component uses the entity tags you label your utterances with to train a machine-learned model. The model learns to predict where the entity is based on the context within the utterance. Your labels provide examples of where the entity is expected to be present in an utterance, based on the meaning of the words around it and as the words that were labeled. 
+The learned component uses the entity tags you label your utterances with to train a machine-learned model. The model learns to predict where the entity is based on the context within the utterance. Your labels provide examples of where the entity is expected to be present in an utterance. This determination is based on the meaning of the words around it and as the words that were labeled.
 
 This component is only defined if you add labels by tagging utterances for the entity. If you don't tag any utterances with the entity, it doesn't have a learned component.
 
@@ -53,13 +53,13 @@ In multilingual projects, you can specify a different expression for each langua
 
 ## Entity options
 
-When multiple components are defined for an entity, their predictions might overlap. When an overlap occurs, each entity's final prediction is determined by one of the following options.
+If multiple components define an entity, their predictions may overlap. When overlap happens, one of the following options determines each entity's final prediction:
 
 ### Combine components
 
 Combine components as one entity when they overlap by taking the union of all the components.
 
-Use this option to combine all components when they overlap. When components are combined, you get all the extra information that's tied to a list or prebuilt component when they're present.
+Use this option to combine all components when they overlap. When components are combined, you get all the extra information associated with a list or prebuilt component if present.
 
 #### Example
 
@@ -71,7 +71,7 @@ By using combined components, the entity returns with the full context as "Prose
 
 :::image type="content" source="../media/union-overlap-example-1-part-2.svg" alt-text="Screenshot that shows the result of a combined component." lightbox="../media/union-overlap-example-1-part-2.svg":::
 
-Suppose you had the same utterance, but only "OS 9" was predicted by the learned component:
+Suppose you had the same utterance, but only "OS 9" predicts the learned component:
 
 :::image type="content" source="../media/union-overlap-example-2.svg" alt-text="Screenshot that shows an utterance with O S 9 predicted by the learned component." lightbox="../media/union-overlap-example-2.svg":::
 
@@ -95,7 +95,7 @@ When you don't combine components, the entity returns twice:
 
 ### Required components
 
-Sometimes an entity can be defined by multiple components but requires one or more of them to be present. Every component can be set as *required*, which means the entity *won't* be returned if that component wasn't present. For example, if you have an entity with a list component and a required learned component, it's guaranteed that any returned entity includes a learned component. If it doesn't, the entity isn't returned.
+Sometimes, you can define an entity using multiple components, but the entity requires at least one or more of them to be present. You can mark any component as *required*, which means the system *doesn't* return the entity unless that component is present. For example, if an entity has a list component and a *required* learned component, the system guarantees that any returned entity includes a learned component. If an entity doesn't have the required component, the system doesn't return it.
 
 Required components are most frequently used with learned components because they can restrict the other component types to a specific context, which is commonly associated to *roles*. You can also require all components to make sure that every component is present for an entity.
 
@@ -120,8 +120,9 @@ Other times, you might be interested in extracting an entity through context, su
 When you don't combine components, you allow every component to act as an independent entity extractor. One way of using this option is to separate the entities extracted from a list to the ones extracted through the learned or prebuilt components to handle and treat them differently.
 
 > [!NOTE]
-> Previously during the public preview of the service, there were four available options: **Longest overlap**, **Exact overlap**, **Union overlap**, and **Return all separately**. **Longest overlap** and **Exact overlap** are deprecated and are only supported for projects that previously had those options selected. **Union overlap** has been renamed to **Combine components**, while **Return all separately** has been renamed to **Do not combine components**.
+> Previously during the public preview of the service, there were four available options: **Longest overlap**, **Exact overlap**, **Union overlap**, and **Return all separately**. **Longest overlap** and **Exact overlap** are deprecated and are only supported for projects that previously had those options selected. **Union overlap** is renamed to **Combine components**, while **Return all separately** is renamed to **Do not combine components**.
 
 ## Related content
 
-- [Supported prebuilt components](../prebuilt-component-reference.md)
+[Supported prebuilt components](../prebuilt-component-reference.md)
+
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティコンポーネントの内容更新"
}
```

### Explanation
この変更は、「エンティティコンポーネント」に関する文書の一部を更新したものです。主に言葉の使い方や構文に改善が行われ、いくつかの文章が明確化されました。具体的には、エンティティの抽出方法や、エンティティの予測の重複に関する説明が簡略化され、文の流れがスムーズになっています。また、日付も更新されています。

追加された内容としては、抽出方法の説明や、学習コンポーネントについての説明がさらなる明確さをもたらしています。重複の発生と、その際のエンティティの最終予測をどのように決定するかについても、より明確な表現が使用されています。全体として、ユーザーが理解しやすいように文が整えられており、情報の正確さを保ちながら読みやすさも向上させています。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -839,8 +839,14 @@ items:
       items:
       - name: C#
         items:
-        - name: Text analysis
-          href: /dotnet/api/overview/azure/ai.textanalytics-readme?view=azure-dotnet-preview&preserve-view=true
+        - name: Language Text
+          href: /dotnet/api/overview/azure/ai.language.text-readme?view=azure-dotnet-preview&preserve-view=true
+        - name: Conversational Language Understanding
+          href: /dotnet/api/overview/azure/ai.language.conversations-readme?view=azure-dotnet-preview&preserve-view=true
+        - name: Conversations Authoring
+          href: /dotnet/api/overview/azure/ai.language.conversations.authoring-readme?view=azure-dotnet-preview&preserve-view=true
+        - name: Text Authoring
+          href: /dotnet/api/overview/azure/ai.language.text.authoring-readme?view=azure-dotnet-preview&preserve-view=true
         - name: Custom question answering
           href: /dotnet/api/overview/azure/ai.language.questionanswering-readme?view=azure-dotnet-preview&preserve-view=true
       - name: Python
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCの項目名とリンクの更新"
}
```

### Explanation
この変更は、TOC（目次）のYAMLファイルにおいて、項目名やリンクを更新したものです。具体的には、C#に関連するセクションに新しい項目が追加されています。これには「Language Text」、「Conversational Language Understanding」、「Conversations Authoring」、「Text Authoring」などが含まれ、それぞれのリンクが新たに定義されています。

これまでの「Text analysis」といった項目は削除され、代わりにより具体的で関連性の高い名称が導入されました。これにより、ユーザーはより正確に情報をナビゲートできるようになり、AIサービスにおける言語関連のAPIへのアクセスが簡略化されています。全体として、目次が最新の情報に基づいて更新され、ユーザビリティが向上しています。


