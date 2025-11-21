---
date: '2025-11-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:05b2bb7...MicrosoftDocs:ff7d49c
summary: 今回の変更では、主に日付の更新と文章の明確化が行われ、ユーザーが最新情報を得やすくなり、文書の流暢性と正確性が向上しました。新機能の追加や破壊的変更はありませんが、全ドキュメントの`ms.date`フィールドが更新され、マルチリージョンデプロイメントや名前付きエンティティ認識の説明が改善されています。これにより、ユーザーはAPIの変更をより理解しやすくなり、情報の受け取り方が良くなっています。全体的に、小さな改訂がユーザーの読みやすさを向上させ、サービスの利用価値を高めています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:05b2bb7...MicrosoftDocs:ff7d49c){target="_blank"}

# ハイライト

今回の変更において、日付の更新と文章の明確化がほとんどのドキュメントで行われました。これにより、ユーザーが最新情報を取得しやすくなり、文書の流暢性と正確性が向上しました。

## 新機能
特に新機能の追加はありませんでした。

## 破壊的変更
破壊的変更は今回の更新には含まれていません。

## その他の更新
- すべてのドキュメントで`ms.date`のフィールドが2025年11月18日から2025年12月05日に変更されました。
- マルチリージョンデプロイメントや名前付きエンティティ認識の説明が洗練され、より理解しやすく改善されています。
- テクニカルスペックの記述において、一貫性のあるフォーマットが適用されています。

# インサイト

今回のコード変更では、一貫してどのドキュメントでも日付の更新が行われ、ユーザーへ最新の情報提供が保証されています。これは、日々進化する技術における正確な情報が非常に重要であるためです。また、各ドキュメントにおいて文章の流暢さや明確さが改善されています。具体的には、表現がより直感的になるように修正され、冗長な説明が排除されています。

例えば、名前付きエンティティ認識のドキュメントでは、エンティティのタグやタイプに関する情報を明確にするために具体的な表現が追加され、ユーザーがAPIの最新の変更をより理解できるようになっています。さらに、個人情報保護に関するコンテナ使用においては、技術的仕様の表記が統一され、理解が容易になっています。

こうした小さな改訂であっても、ユーザーの読みやすさが向上し、情報の受け取り方が良くなり、最終的にはサービスの利用価値が高まることにつながります。このようなきめ細やかな修正は、ドキュメント品質の向上において重要な役割を果たしています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [configure-containers.md](#item-6f87ab) | minor update | コンテナの構成に関するドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [multi-region-deployment.md](#item-a7351d) | minor update | マルチリージョンデプロイメントに関するドキュメントの内容更新 | modified | 4 | 3 | 7 | 
| [language-support.md](#item-6b7b2b) | minor update | 会話型言語理解に関するドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [overview.md](#item-bdc923) | minor update | 会話型言語理解に関する概要ドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-b67686) | minor update | 会話型言語理解に関するクイックスタートドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-29d53a) | minor update | カスタムテキスト分類のクイックスタートドキュメントの内容修正 | modified | 6 | 6 | 12 | 
| [ga-preview-mapping.md](#item-bed282) | minor update | 名前付きエンティティ認識のGAプレビュー変換に関するドキュメントの修正 | modified | 12 | 12 | 24 | 
| [skill-parameters.md](#item-e29e05) | minor update | 名前付きエンティティ認識スキルパラメータに関するドキュメントの修正 | modified | 3 | 3 | 6 | 
| [use-containers.md](#item-8c61d4) | minor update | 個人情報保護のためのコンテナ使用に関するドキュメントの修正 | modified | 2 | 2 | 4 | 
| [fhir.md](#item-7ef75f) | minor update | FHIRリソースバンドルに関するドキュメントの修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/language-service/concepts/configure-containers.md{#item-6f87ab}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - ignite-2024
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/18/2025
+ms.date: 12/05/2025
 ms.author: lajanuar
 ---
 # Configure Language docker containers
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテナの構成に関するドキュメントの日付更新"
}
```

### Explanation
この変更は、`configure-containers.md` ドキュメントにおける日付の更新を表しています。具体的には、`ms.date` フィールドの値が2025年11月18日から2025年12月05日に変更されました。この修正は、ドキュメントの正確性を保ち、ユーザーに最新の情報を提供するためのものです。全体として、1行の追加と1行の削除が行われています。これにより、内容が最新の状態に更新されました。

## articles/ai-services/language-service/concepts/custom-features/multi-region-deployment.md{#item-a7351d}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/18/2025
+ms.date: 12/05/2025
 ms.author: lajanuar
 ms.custom: language-service-clu, ignite-2024
 ---
@@ -20,7 +20,8 @@ ms.custom: language-service-clu, ignite-2024
 > * [Custom named entity recognition (NER)](../../custom-named-entity-recognition/overview.md)
 > * [Orchestration workflow](../../orchestration-workflow/overview.md)
 
-Custom Language features enable you to deploy your project to more than one region. This capability makes it much easier to access your project globally while you manage only one instance of your project in one place. As of November 2024, custom Language features also enable you to deploy your project to multiple resources within a single region via the API, so that you can use your custom model wherever you need.
+Custom Language features enable you to deploy your project to more than one region. This capability makes it much easier to access your project globally while you manage only one instance of your project in one place. Beginning in November 2024, custom Language features allow you to deploy your project to multiple resources within a single region using the API. Thus, you can access and utilize your custom model wherever needed.
+
 
 Before you deploy a project, you can assign *deployment resources* in other regions. Each deployment resource is a different Language resource from the one that you use to author your project. You deploy to those resources and then target your prediction requests to that resource in their respective regions and your queries are served directly from that region.
 
@@ -46,7 +47,7 @@ Assigning deployment resources requires Microsoft Entra authentication. Microsof
 
 Your project name and resource are used as its main identifiers. A Language resource can only have a specific project name in each resource. Any other projects with the same name can't be deployed to that resource.
 
-For example, if a project `ContosoSupport` was created by the resource `MyWestUS2` in West US 2 and deployed to the resource `MyEastUS` in East US, the resource `MyEastUS` can't create a different project called `ContosoSupport` and deploy a project to that region. Similarly, your collaborators can't then create a project `ContosoSupport` with the resource `MyCentralIndia` in Central India and deploy it to either `MyWestUS2` or `MyEastUS`.
+For example, if a project `ContosoSupport` was created via the resource `MyWestUS2` in West US 2 and deployed to the resource `MyEastUS` in East US, the resource `MyEastUS` can't create a different project called `ContosoSupport` and deploy a project to that region. Similarly, your collaborators can't then create a project `ContosoSupport` with the resource `MyCentralIndia` in Central India and deploy it to either `MyWestUS2` or `MyEastUS`.
 
 You can only swap deployments that are available in the exact same regions. Otherwise, swapping fails.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチリージョンデプロイメントに関するドキュメントの内容更新"
}
```

### Explanation
この変更は、`multi-region-deployment.md` ドキュメントにおける内容の更新を表しています。主な修正点は、日付の変更（2025年11月18日から2025年12月05日）と、文章の一部がより明確に修正されたことです。具体的には、プロジェクトをAPIを通じて複数のリソースにデプロイする能力についての説明が改良されています。また、リソースの認識に関する注意喚起の内容も保たれたまま、表現が洗練されています。これにより、利用者がマルチリージョンデプロイメントに関する現在の機能をより良く理解できるようになっています。全体として、4行の追加と3行の削除が行われています。

## articles/ai-services/language-service/conversational-language-understanding/language-support.md{#item-6b7b2b}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/18/2025
+ms.date: 12/05/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話型言語理解に関するドキュメントの日付更新"
}
```

### Explanation
この変更は、`language-support.md` ドキュメント内の日付を更新するものです。具体的には、`ms.date` フィールドの値が2025年11月18日から2025年12月05日に変更されました。この修正は、ドキュメントの内容が最新のものであることを確保し、ユーザーに正確な情報を提供するために行われました。全体として、1行の追加と1行の削除があり、主にこの日付の変更に焦点を当てています。

## articles/ai-services/language-service/conversational-language-understanding/overview.md{#item-bdc923}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 11/18/2025
+ms.date: 12/05/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話型言語理解に関する概要ドキュメントの日付更新"
}
```

### Explanation
この変更は、`overview.md` ドキュメントにおける日付の更新を示しています。具体的には、`ms.date` フィールドが2025年11月18日から2025年12月05日に変更されました。この修正により、ドキュメントは最新の情報を反映することができます。この変更は1行の追加と1行の削除を含み、主に日付の更新に焦点を当てています。ユーザーに対して正確で最新の情報を提供することが目的です。

## articles/ai-services/language-service/conversational-language-understanding/quickstart.md{#item-b67686}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 11/18/2025
+ms.date: 12/05/2025
 ms.author: lajanuar
 ms.custom: language-service-clu, mode-other
 zone_pivot_groups: foundry-rest-api
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話型言語理解に関するクイックスタートドキュメントの日付更新"
}
```

### Explanation
この変更は、`quickstart.md` ドキュメント内の日付を更新するものです。具体的には、`ms.date` フィールドが2025年11月18日から2025年12月05日に変更されました。この修正により、ユーザーに提供される情報が最新のものとなることを目的としています。この変更には1行の追加と1行の削除が含まれ、主に日付の更新が行われています。正確性を保ち、ユーザーへ最新情報をお知らせするための重要な更新です。

## articles/ai-services/language-service/custom-text-classification/quickstart.md{#item-29d53a}

<details>
<summary>Diff</summary>
````diff
@@ -7,21 +7,21 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 11/18/2025
+ms.date: 12/05/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification, mode-other
 zone_pivot_groups: usage-custom-language-features
 ---
 # Quickstart: Custom text classification
 
-Use this article to get started with creating a custom text classification project where you can train custom models for text classification. A model is artificial intelligence software that's trained to do a certain task. For this system, the models classify text, and are trained by learning from tagged data.
+Use this article to get started with creating a custom text classification project where you can train custom models for text classification. A model is AI software trained to do a certain task. For this system, the models classify text, and are trained by learning from tagged data.
 
 Custom text classification supports two types of projects: 
 
-* **Single label classification** - you can assign a single class for each document in your dataset. For example, a movie script could only be classified as "Romance" or "Comedy". 
-* **Multi label classification** - you can assign multiple classes for each document in your dataset. For example, a movie script could be classified as "Comedy" or "Romance" and "Comedy".
+* **Single label classification** - you can assign a single class for each document in your dataset. For example, a movie script could only be classified as "Romance" or "Comedy." 
+* **Multi label classification** - you can assign multiple classes for each document in your dataset. For example, a movie script could be classified as "Comedy" or "Romance" and "Comedy."
 
-In this quickstart you can use the sample datasets provided to build a multi label classification where you can classify movie scripts into one or more categories or you can use single label classification dataset where you can classify abstracts of scientific papers into one of the defined domains.
+In this quickstart, you can use the sample datasets provided to build a multi label classification to classify movie scripts into one or more categories. Alternatively, you can use single label classification dataset to classify abstracts of scientific papers into one of the defined domains.
 
 
 ::: zone pivot="language-studio"
@@ -38,7 +38,7 @@ In this quickstart you can use the sample datasets provided to build a multi lab
 
 ## Next steps
 
-After you've created a custom text classification model, you can:
+After you create a custom text classification model, you can:
 * [Use the runtime API to classify text](how-to/call-api.md)
 
 When you start to create your own custom text classification projects, use the how-to articles to learn more about developing your model in greater detail:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムテキスト分類のクイックスタートドキュメントの内容修正"
}
```

### Explanation
この変更は、`quickstart.md` ドキュメントの内容に対していくつかの修正を行ったものです。具体的には、文章の一部が修正され、特に言葉遣いの明確化が図られています。また、いくつかの文に対して句読点の調整も行われています。これにより、テキストの流暢さや読みやすさが向上しています。加えて、`ms.date` フィールドが2025年11月18日から2025年12月05日に更新され、最新の情報を反映するようにしています。トータルで6行の追加と6行の削除があり、全体で12行にわたって変更が行われています。これらの変更は、ユーザーにより良い体験を提供するための重要なステップとなります。

## articles/ai-services/language-service/named-entity-recognition/concepts/ga-preview-mapping.md{#item-bed282}

<details>
<summary>Diff</summary>
````diff
@@ -6,39 +6,39 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/18/2025
+ms.date: 12/05/2025
 ms.author: lajanuar
 ms.custom: language-service-ner, ignite-2024
 ---
 # Entity types and tags
 
-Use this article to get an overview of the new API changes starting from version `2024-11-01`. This API change mainly introduces two new concepts (`entity types` and `entity tags`) replacing the `category` and `subcategory` fields in the current Generally Available API. A detailed overview of each API parameter and the supported API versions it corresponds to can be found on the [Skill Parameters][../how-to/skill-parameters.md] page.
+Use this article to get an overview of the new API changes starting from version `2024-11-01`. This API change mainly introduces two new concepts (`entity types` and `entity tags`) replacing the `category` and `subcategory` fields in the current Generally Available API. A detailed overview of each API parameter and the corresponding supported API versions are found on the [Skill Parameters][../how-to/skill-parameters.md] page.
 
-Since an entity like “Seattle” could be classified as a City, GPE (Geo Political Entity), and a Location, the `type` attribute is used to define the most granular classification, in this case City. The `tags` attribute in the service output is a list all possible classifications (City, GPE, and Location) and their respective confidence score. A full mapping of possible tags for each type can be found below. The `metadata` attributes in the service output contains additional information about the entity, such as the integer value associated with the entity. 
+Since an entity like "Seattle" could be classified as a City, GPE (Geo Political Entity), and a Location, the `type` attribute is used to define the most granular classification, in this case City. The `tags` attribute in the service output is a list all possible classifications (City, GPE, and Location) and their respective confidence score. A full mapping of possible tags for each are listed. The `metadata` attributes in the service output contain additional information about the entity, such as the integer value associated with the entity. 
 
 ## Entity types
-Entity types represent the lowest (or finest) granularity at which the entity has been detected and can be considered to be the base class that has been detected.
+Entity types represent the lowest (or finest) granularity at which the entity is detected. Types are considered to be the base class detected.
 
 ## Entity tags
-Entity tags are used to further identify an entity where a detected entity is tagged by the entity type and additional tags to differentiate the identified entity. The entity tags list could be considered to include categories, subcategories, sub-subcategories, and so on.
+Entity tags are used to further identify an entity where a detected entity is tagged to indicate the entity type. The entity tags list can include categories, subcategories, and sub-subcategories.
 
 ## Changes from versions `2022-05-01` and `2023-04-01` to version `2024-11-01` API
 The changes introduce better flexibility for the named entity recognition service, including:
 
 Updates to the structure of input formats:
-•	InclusionList
-•	ExclusionList
-•	Overlap policy
+*    InclusionList
+*    ExclusionList
+*    Overlap policy
 
 Updates to the handling of output formats:
 
-* More granular entity recognition outputs through introducing the tags list where an entity could be tagged by more than one entity tag.
+* More granular entity recognition outputs through introducing the tags list where an entity is tagged with more than one entity tag.
 * Overlapping entities where entities could be recognized as more than one entity type and if so, this entity would be returned twice. If an entity was recognized to belong to two entity tags under the same entity type, both entity tags are returned in the tags list.
-* Filtering entities using entity tags, you can learn more about this by navigating to [this article](../how-to-call.md#select-which-entities-to-be-returned).
-* Metadata Objects which contain additional information about the entity but currently only act as a wrapper for the existing entity resolution feature. You can learn more about this new feature [here](entity-metadata.md).
+* Filtering entities using entity tags: to learn more, *see*  [Select returned entities](../how-to-call.md#select-which-entities-to-be-returned).
+* Metadata Objects that contain additional information about the entity but currently only act as a wrapper for the existing entity resolution feature. You can learn more about this new feature [here](entity-metadata.md).
 
 ## Versions `2022-05-01` and `2023-04-01` to current version API entity mappings
-You can see a comparison between the structure of the entity categories/types in the [Supported Named Entity Recognition (NER) entity categories and entity types article](./named-entity-categories.md). Below is a table describing the mappings between the results you would expect to see from versions `2022-05-01` and `2023-04-01` and the current version API.
+You can see a comparison between the structure of the entity categories/types in the [Supported Named Entity Recognition (NER) entity categories and entity types article](./named-entity-categories.md). The following table presents the mappings between the results you would expect to see from versions `2022-05-01` and `2023-04-01` and the current version API.
 
 | Type           | Tags                                   |
 |----------------|----------------------------------------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "名前付きエンティティ認識のGAプレビュー変換に関するドキュメントの修正"
}
```

### Explanation
この変更は、`ga-preview-mapping.md` ドキュメントの内容を更新するもので、主に文章の明確さと流暢さを向上させる修正が施されています。具体的には、`ms.date` フィールドの更新（2025年11月18日から2025年12月05日）に加え、文の構造が若干変更され、冗長な表現が簡潔にされました。例えば、「低い粒度」という表現が、「最も細かい粒度」に変更されたりするなど、より直接的な表現が使用されています。

また、エンティティのタグやタイプに関連する部分も修正され、情報の明確化が図られています。これにより、読者にとって理解しやすい内容に改善されています。全体で12行の追加と12行の削除が行われ、変更が目立つように整理されています。この更新は、利用者が最新のAPI変更を理解する助けとなります。

## articles/ai-services/language-service/named-entity-recognition/how-to/skill-parameters.md{#item-e29e05}

<details>
<summary>Diff</summary>
````diff
@@ -8,12 +8,12 @@ ms.service: azure-ai-language
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/18/2025
+ms.date: 12/05/2025
 ms.author: lajanuar
 ---
 # Using named entity recognition skill parameters
 
-Use this article to get an overview of the different API parameters used to adjust the input to a Named Entity Recognition (NER) API call. The Generally Available NER service now supports the ability to specify a list of entity tags to be included into the response or excluded from the response. If a piece of text is classified as more than one entity type, the `overlapPolicy` parameter allows customers to specify how the service will handle the overlap. The `inferenceOptions` parameter allows for users to adjust the inference, such as excluding the detected entity values from being normalized and included in the metadata.
+Use this article to get an overview of the different API parameters used to adjust the input to a Named Entity Recognition (NER) API call. The Generally Available NER service now supports the ability to specify a list of entity tags to be included into the response or excluded from the response. If a piece of text is classified as more than one entity type, the `overlapPolicy` parameter allows customers to specify how the service handles the overlap. The `inferenceOptions` parameter allows for users to adjust the inference, such as excluding the detected entity values from being normalized and included in the metadata.
 
 ## InclusionList parameter
 
@@ -34,7 +34,7 @@ Parameters by supported API version
 
 ## inferenceOptions parameter
 
-Defines a selection of options available for adjusting the inference. Currently we have only one property called `excludeNormalizedValues` which excludes the detected entity values to be normalized and included in the metadata. The numeric and temporal entity types support value normalization. 
+Defines a selection of options available for adjusting the inference. Currently we have only one property called `excludeNormalizedValues` that excludes the detected entity values to be normalized and included in the metadata. The numeric and temporal entity types support value normalization. 
 
 ## Sample
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "名前付きエンティティ認識スキルパラメータに関するドキュメントの修正"
}
```

### Explanation
この変更は、`skill-parameters.md` ドキュメントの更新に関するもので、文の流暢さと正確さを向上させるために一部の表現を修正しています。具体的には、`ms.date` フィールドが2025年11月18日から2025年12月05日に更新され、最新の情報を反映するようにされました。

また、文の構成に関しても小さな変更が行われており、「サービスが重複を扱う方法」という箇所で、文の形式が若干調整されています。特に、動詞の形式が一致するように修正されており、全体の文の整合性が高まっています。これにより、API呼び出しに必要なパラメータの理解が一層容易になることが期待されます。全体で3行の追加と3行の削除が行われ、変更が全体で6行にわたる形で整理されています。この更新は、ユーザーが名前付きエンティティ認識機能をより効果的に利用できるようにするための重要な改善となります。

## articles/ai-services/language-service/personally-identifiable-information/how-to/use-containers.md{#item-8c61d4}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.service: azure-ai-language
 ms.custom:
 ms.topic: how-to
-ms.date: 11/18/2025
+ms.date: 12/05/2025
 ms.author: lajanuar
 keywords: on-premises, Docker, container
 ---
@@ -42,7 +42,7 @@ We recommend that you have a CPU with AVX-512 instruction set, for the best expe
 
 |                     | Minimum host specs     | Recommended host specs |
 |---------------------|------------------------|------------------------|
-| **PII detection**   | 1 core, 2 GB memory     | 4 cores, 8 GB memory    |
+| **PII detection**   | 1-core, 2-GB memory     | 4-cores, 8-GB memory    |
 
 CPU core and memory correspond to the `--cpus` and `--memory` settings, which are used as part of the `docker run` command.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人情報保護のためのコンテナ使用に関するドキュメントの修正"
}
```

### Explanation
この変更は、`use-containers.md` ドキュメントの更新に関連しており、主に文の表記やスタイルに関する修正が行われています。具体的には、`ms.date` フィールドが2025年11月18日から2025年12月05日に更新され、情報の鮮度を保つための変更がなされています。

さらに、表内の最小および推奨ホスペックの記述が修正され、「1 core, 2 GB memory」という表記が、「1-core, 2-GB memory」に変更され、より一貫したフォーマットが適用されています。この変更により、技術的な仕様を読みやすくし、関連情報の理解を向上させることが目的とされています。全体で2行の追加と2行の削除が行われ、結果として4行の変更が記録されています。この更新は、個人情報保護に関連するコンテナ使用の情報をより明確に提供するための重要な改善です。

## articles/ai-services/language-service/text-analytics-for-health/concepts/fhir.md{#item-7ef75f}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/18/2025
+ms.date: 12/05/2025
 ms.author: lajanuar
 ms.custom: language-service-health, ignite-2024
 ---
@@ -41,7 +41,7 @@ When you use the REST API as part of building the request payload, you include a
 }
 ```
 
-Once the request has completed processing by Text Analytics for health and you pull the response from the REST API, you'll find the FHIR resource bundle in the output. You can locate the FHIR resource bundle inside each document processed using the property name `fhirBundle`. The following partial sample is output highlighting the `fhirBundle`.
+Once the request completes processing by Text Analytics for health and you pull the response from the REST API, you can find the FHIR resource bundle in the output. You can locate the FHIR resource bundle inside each document processed using the property name `fhirBundle`. The following partial sample is output highlighting the `fhirBundle`.
 
 ```json
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FHIRリソースバンドルに関するドキュメントの修正"
}
```

### Explanation
この変更は、`fhir.md` ドキュメントに対する更新で、主に文の流れを改善するための修正が行われています。具体的には、`ms.date` フィールドが2025年11月18日から2025年12月05日に更新されており、最新の情報を反映しています。

文の内容においても微細な変更が加えられており、「リクエストがText Analytics for healthによって処理を完了した後、REST APIからレスポンスを引き出すと、出力にFHIRリソースバンドルが見つかる。」という表現が、「リクエストが処理を完了した後」へと修正されています。この変更により、表現がより明確になり、読みやすさが向上しています。全体で2行の追加と2行の削除が行われ、結果として4行の変更がなされています。この更新は、FHIRリソースバンドルに関連する情報をユーザーが理解しやすくするための重要な改善となります。


