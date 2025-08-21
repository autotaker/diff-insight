---
date: '2025-08-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1ecbb7d...MicrosoftDocs:8858310
summary: この報告書では、Azure AI Languageサービスに関するドキュメントの内容改善について概説しています。主に、情報の明確化や理解しやすさの向上が目指されており、特に文言の修正や自動化機能の説明が強調されています。また、情報を最新に保つための文書の日付更新も行われています。新機能の追加はないものの、多くの表現が改善され、技術的な説明がより分かりやすくなり、利用者にとって有益な情報が提供されています。さらに、「責任あるAI」に関する情報へのリンクが追加され、倫理的な観点からの理解を助けています。全体的には、ドキュメントの信頼性を保持しつつ、内容をより洗練されたものにする取り組みが行われています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1ecbb7d...MicrosoftDocs:8858310){target="_blank"}

<format>
# Highlights
数多くのドキュメントにおける文章構成や内容の微調整が行われました。特に、読者に情報をより明確に伝えるための文言の修正、自動化されたテキスト抽出や分析機能の説明が中心です。また、更新日を最新の情報に反映させる変更も含まれています。

## New features
- 特に新機能の追加は行われていませんが、文書内の情報の明確化と理解しやすさが向上しています。

## Breaking changes
- 重大な変更や後方互換性の問題を引き起こす変更はありません。

## Other updates
- 文書の日付更新により、情報が最新であることを示すための修正。
- いくつかのドキュメントで、「AIシステム」などの技術説明に関する改善が行われています。
- 一部のドキュメントで、利用者や影響を受ける人々、環境についての表現が包括的になっています。
- 「責任あるAI」に関するリンクが追加され、関連情報へのアクセスが容易になりました。

# Insights
今回のコード変更は、Azure AI Languageサービスに関するドキュメントでの内容改善を目的としたもので、多数の文章がより明確に、かつ正確に表現されるよう変更が加えられています。特に、様々なAIサービス（例えば、言語理解や感情分析、テキスト分析など）についての説明が洗練され、利用者視点でより使いやすくなっています。

また、「責任あるAI」セクションなどに関するリンク追加によって、ユーザーはAIの倫理的使用についてさらなる情報にアクセスしやすくなっています。これにより、Azure AI Languageサービスを使用する企業や個人が、技術的および倫理的視点を理解しながら製品を導入するサポートを強化しています。

さらに、更新日を最新に保つことで、ドキュメントの信頼性が確保され、ユーザーが安心して参照できるよう配慮されています。全体的に、内容の微調整を行いながら、ドキュメントをより分かりやすくすることを主眼に、読み手に対して有益な情報を提供する取組が強く感じられます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [overview.md](#item-bdc923) | minor update | 会話型言語理解に関する概要の微調整 | modified | 3 | 3 | 6 | 
| [overview.md](#item-ebc28d) | minor update | カスタムテキスト分類に関する概要の微調整 | modified | 1 | 1 | 2 | 
| [overview.md](#item-10e41c) | minor update | エンティティリンクに関する概要の微調整 | modified | 1 | 1 | 2 | 
| [overview.md](#item-4ff047) | minor update | キーフレーズ抽出に関する概要の修正 | modified | 3 | 3 | 6 | 
| [quickstart.md](#item-a6bafe) | minor update | クイックスタートの更新日付変更 | modified | 1 | 1 | 2 | 
| [overview.md](#item-efc346) | minor update | 言語検出に関する概要の修正 | modified | 4 | 5 | 9 | 
| [how-to-call.md](#item-c5709f) | minor update | 命名エンティティ認識の呼び出し方法の改善 | modified | 7 | 7 | 14 | 
| [overview.md](#item-a490e5) | minor update | ネイティブドキュメントサポートの概要の日付更新 | modified | 1 | 1 | 2 | 
| [overview.md](#item-53d49f) | minor update | オーケストレーションワークフローにおける責任あるAIセクションの修正 | modified | 1 | 1 | 2 | 
| [overview.md](#item-831fe6) | minor update | 感情分析と意見マイニングの概要の文書改善 | modified | 9 | 10 | 19 | 
| [quickstart.md](#item-bff856) | minor update | 要約機能のクイックスタート文書の更新日変更 | modified | 1 | 1 | 2 | 
| [overview.md](#item-982d4c) | minor update | 健康向けテキスト分析の概要文書の改善 | modified | 20 | 15 | 35 | 
| [quickstart.md](#item-9b06f2) | minor update | 健康向けテキスト分析のクイックスタート文書の更新日変更 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/language-service/conversational-language-understanding/overview.md{#item-bdc923}

<details>
<summary>Diff</summary>
````diff
@@ -51,7 +51,7 @@ Creating a CLU project typically involves several different steps.
 :::image type="content" source="media/llm-quick-deploy.png" alt-text="Chart of the LLM-powered quick deploy path." lightbox="media/llm-quick-deploy.png":::
 
 > [!NOTE]
-> In the Azure AI Foundry, you’ll create a fine-tuning task as your workspace for customizing your CLU model. Formerly, a CLU fine-tuning task was called a CLU project. You may see these terms used interchangeably in legacy CLU documentation.
+> In the Azure AI Foundry, you'll create a fine-tuning task as your workspace for customizing your CLU model. Formerly, a CLU fine-tuning task was called a CLU project. You may see these terms used interchangeably in legacy CLU documentation.
 
 CLU offers two paths for you to get the most out of your implementation.
 
@@ -61,7 +61,7 @@ Option 1 (LLM-powered quick deploy):
 
 2. **Deploy the model**: Deploying a model with the LLM-based training config makes it available for use via the Runtime API.
 
-3. **Predict intents and entities**: Use your custom model deployment to predict custom intents and prebuilt entities from user’s utterances. 
+3. **Predict intents and entities**: Use your custom model deployment to predict custom intents and prebuilt entities from user's utterances. 
 
 Option 2 (Custom machine learned model)
 
@@ -94,7 +94,7 @@ As you use CLU, see the following reference documentation and samples for Azure
 
 ## Responsible AI 
 
-An AI system includes not only the technology, but also the people who use it, the people who are affected by it, and the environment in which it's deployed. Read the transparency note for CLU to learn about responsible AI use and deployment in your systems. You can also see the following articles for more information:
+An AI system includes the technology, the individuals who operate the system, the people who experience its effects, and the broader environment where the system functions all play a role. Read the transparency note for CLU to learn about responsible AI use and deployment in your systems. 
 
 [!INCLUDE [Responsible AI links](../includes/overview-responsible-ai-links.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話型言語理解に関する概要の微調整"
}
```

### Explanation
この変更は、会話型言語理解（CLU）の導入に関するドキュメントの微調整を行うもので、主に文言や表現の修正が含まれています。具体的には、いくつかの文で少しの表現が変更され、構文が改善されました。これにより、CLUiのプロジェクトの説明がより明確に伝えられるようになっています。特に、「CLUプロジェクト」という用語の置き換えや、文章の流れを良くするための調整が行われました。この変更は、読み手が情報を理解しやすくすることを意図しており、ドキュメントの全体的な質を向上させています。

## articles/ai-services/language-service/custom-text-classification/overview.md{#item-ebc28d}

<details>
<summary>Diff</summary>
````diff
@@ -76,7 +76,7 @@ As you use custom text classification, see the following reference documentation
 
 ## Responsible AI 
 
-An AI system includes not only the technology, but also the people who will use it, the people who will be affected by it, and the environment in which it is deployed. Read the [transparency note for custom text classification](/azure/ai-foundry/responsible-ai/language-service/custom-text-classification-transparency-note) to learn about responsible AI use and deployment in your systems. You can also see the following articles for more information:
+An AI system includes not only the technology, but also the people who will use it, the people who will be affected by it, and the environment in which it is deployed. Read the [transparency note for custom text classification](/azure/ai-foundry/responsible-ai/language-service/custom-text-classification-transparency-note) to learn about responsible AI use and deployment in your systems. 
 
 [!INCLUDE [Responsible AI links](../includes/overview-responsible-ai-links.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムテキスト分類に関する概要の微調整"
}
```

### Explanation
この変更は、カスタムテキスト分類に関するドキュメントの内容を微調整するもので、主に文言の修正が行われています。具体的には、「AIシステムには技術だけでなく、利用する人々や影響を受ける人々、そして展開される環境が含まれる」という文章の修正が含まれています。変更によって、文のリズムや分かりやすさが改善され、読者に対して更に明確に情報を伝えることができるようになっています。この更新は、ドキュメントの品質を向上させ、責任を持ったAIの使用と展開に関する情報をより効果的に提供することを目的としています。

## articles/ai-services/language-service/entity-linking/overview.md{#item-10e41c}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ This documentation contains the following types of articles:
 
 ## Responsible AI 
 
-An AI system includes not only the technology, but also the people who will use it, the people who will be affected by it, and the environment in which it is deployed. Read the [transparency note for entity linking](/azure/ai-foundry/responsible-ai/language-service/transparency-note) to learn about responsible AI use and deployment in your systems. You can also see the following articles for more information:
+An AI system includes not only the technology, but also the people who will use it, the people who will be affected by it, and the environment in which it is deployed. Read the [transparency note for entity linking](/azure/ai-foundry/responsible-ai/language-service/transparency-note) to learn about responsible AI use and deployment in your systems. 
 
 [!INCLUDE [Responsible AI links](../includes/overview-responsible-ai-links.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティリンクに関する概要の微調整"
}
```

### Explanation
この変更は、エンティティリンクに関するドキュメントの内容を微調整するもので、主に文言の修正が行われています。具体的には、「AIシステムには技術だけでなく、利用する人々や影響を受ける人々、そして展開される環境が含まれる」という文章の繰り返しが削除され、文章の流れが改善されています。これにより、責任を持ったAIの使用と展開に関する情報がよりスムーズに導入され、読者が理解しやすくなっています。この更新は、情報の明確さを向上させ、読者に対して重要なメッセージをより効果的に伝えることを目的としています。

## articles/ai-services/language-service/key-phrase-extraction/overview.md{#item-4ff047}

<details>
<summary>Diff</summary>
````diff
@@ -6,14 +6,14 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 02/17/2025
+ms.date: 08/19/2025
 ms.author: lajanuar
 ms.custom: language-service-key-phrase
 ---
 
 # What is key phrase extraction in Azure AI Language?
 
-Key phrase extraction is one of the features offered by [Azure AI Language](../overview.md), a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. Use key phrase extraction to quickly identify the main concepts in text. For example, in the text "*The food was delicious and the staff were wonderful.*", key phrase extraction returns the main topics: "*food*" and "*wonderful staff*."
+Key phrase extraction is one of the features offered by [Azure AI Language](../overview.md). This capability is part of a suite of cloud-based machine learning and AI tools designed for building intelligent applications that process written language. Use key phrase extraction to quickly identify the main concepts in text. For example, in the text "*The food was delicious and the staff were wonderful.*", key phrase extraction returns the main topics: "*food*" and "*wonderful staff*."
 
 This documentation contains the following types of articles:
 
@@ -31,7 +31,7 @@ This documentation contains the following types of articles:
 
 ## Responsible AI 
 
-An AI system includes not only the technology, but also the people who use it, the people who are affected by it, and the environment in which it's deployed. Read the [transparency note for key phrase extraction](/azure/ai-foundry/responsible-ai/language-service/transparency-note-key-phrase-extraction) to learn about responsible AI use and deployment in your systems. For more information, see the following articles:
+An AI system includes the technology, the individuals who operate the system, the people who experience its effects, and the broader environment where the system functions all play a role. Read the [transparency note for key phrase extraction](/azure/ai-foundry/responsible-ai/language-service/transparency-note-key-phrase-extraction) to learn about responsible AI use and deployment in your systems. For more information, see the following articles:
 
 [!INCLUDE [Responsible AI links](../includes/overview-responsible-ai-links.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "キーフレーズ抽出に関する概要の修正"
}
```

### Explanation
この変更は、キーフレーズ抽出に関するドキュメントの内容を微調整するもので、文の構造や語彙が改善されています。具体的には、キーフレーズ抽出の機能の説明が明確化され、文の流れが改善されています。また、「AIシステム」についての説明がより包括的に修正され、技術や利用者、影響を受ける人々、さらにはシステムが機能する環境を強調しています。この更新は、情報の明確さと理解しやすさを高め、読者に対してキーフレーズ抽出の役割と責任を持ったAIの使用に関する情報をより効果的に伝えることを目的としています。

## articles/ai-services/language-service/key-phrase-extraction/quickstart.md{#item-a6bafe}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 02/17/2025
+ms.date: 08/20/2025
 ms.author: lajanuar
 ms.devlang: csharp
 # ms.devlang: csharp, java, javascript, python
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートの更新日付変更"
}
```

### Explanation
この変更は、キーフレーズ抽出のクイックスタートガイドにおける日付の更新を目的としています。具体的には、ドキュメントメタデータに含まれる「ms.date」のフィールドが「2025年2月17日」から「2025年8月20日」に変更されました。この更新は、文書が最新の情報を反映していることを示すためのものであり、ユーザーに対して信頼性を提供します。文書の内容自体は変更されていませんが、日付の更新により、最新の状態に保たれたことが明示されています。

## articles/ai-services/language-service/language-detection/overview.md{#item-efc346}

<details>
<summary>Diff</summary>
````diff
@@ -6,23 +6,22 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 02/17/2025
+ms.date: 08/19/2025
 ms.author: lajanuar
 ms.custom: language-service-language-detection
 ---
 
 # What is language detection in Azure AI Language?
 
-Language detection is one of the features offered by [Azure AI Language](../overview.md), a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. Language detection is able to detect more than 100 languages in their primary script. In addition, it offers [script detection](./how-to/call-api.md#script-name-and-script-code) to detect supported scripts for each detected language according to the [ISO 15924 standard](https://wikipedia.org/wiki/ISO_15924) for a [select number of languages](./language-support.md#script-detection) supported by Azure AI Language Service.
-
+Language detection is one of the features offered by [Azure AI Language](../overview.md), a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. Language detection is able to detect more than 100 languages in their primary script. In addition, the service offers [script detection](./how-to/call-api.md#script-name-and-script-code) for each detected language using  [ISO 15924 standard](https://wikipedia.org/wiki/ISO_15924) for a [select number of languages](./language-support.md#script-detection).
 This documentation contains the following types of articles:
 
 * [**Quickstarts**](quickstart.md) are getting-started instructions to guide you through making requests to the service.
 * [**How-to guides**](how-to/call-api.md) contain instructions for using the service in more specific or customized ways.
 
 ## Language detection features
 
-* Language detection: Returns one predominant language for each document you submit, along with its ISO 639-1 name, a human-readable name, confidence score, script name and script code according to ISO 15924 standard.
+* Language detection: For each document, returns the main language, its ISO 639-1 code, readable name, confidence score, script name, and ISO 15924 script code.
 
 * Script detection: To distinguish between multiple scripts used to write certain languages, such as Kazakh, language detection returns a script name and script code according to the ISO 15924 standard.  
 
@@ -37,7 +36,7 @@ This documentation contains the following types of articles:
 
 ## Responsible AI 
 
-An AI system includes not only the technology, but also the people who will use it, the people who will be affected by it, and the environment in which it's deployed. Read the [transparency note for language detection](/azure/ai-foundry/responsible-ai/language-service/transparency-note-language-detection) to learn about responsible AI use and deployment in your systems. You can also see the following articles for more information:
+An AI system includes not only the technology, but also individuals who operate the system, people who experience its effects, and the broader environment where the system functions. Read the [transparency note for language detection](/azure/ai-foundry/responsible-ai/language-service/transparency-note-language-detection) to learn about responsible AI use and deployment in your systems. 
 
 [!INCLUDE [Responsible AI links](../includes/overview-responsible-ai-links.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語検出に関する概要の修正"
}
```

### Explanation
この変更は、Azure AI Languageにおける言語検出機能に関するドキュメントの内容を微調整するもので、文の明確さと正確性を向上させることを目的としています。具体的には、言語検出機能の説明が簡潔に改善され、主要な言語やスクリプトのコードに関する表現がより明確になりました。

また、「AIシステム」についての説明が、利用者や影響を受ける人々、システムが機能する環境を強調する形で見直されています。このような変更により、情報の理解しやすさが増し、ユーザーが言語検出機能についての理解を深める手助けとなることを意図しています。

## articles/ai-services/language-service/named-entity-recognition/how-to-call.md{#item-c5709f}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 02/15/2025
+ms.date: 08/20/2025
 ms.author: lajanuar
 ms.custom: language-service-ner, ignite-2024
 ---
@@ -24,7 +24,7 @@ The NER feature can evaluate unstructured text, and extract named entities from
 
 ### Input languages
 
-When you submit input text to be processed, you can specify which of [the supported languages](language-support.md) they're written in. if you don't specify a language, key phrase extraction defaults to English. The API may return offsets in the response to support different [multilingual and emoji encodings](../concepts/multilingual-emoji-support.md). 
+When you submit input text to be processed, you can specify which of [the supported languages](language-support.md) they're written in. If you don't specify a language, key phrase extraction defaults to English. The API may return offsets in the response to support different [multilingual and emoji encodings](../concepts/multilingual-emoji-support.md). 
 
 ## Submitting data
 
@@ -86,7 +86,7 @@ The above examples would return entities falling under the `Location` entity typ
     
 ```
 
-This method returns all `Location` entities only falling under the `GPE` tag and ignore any other entity falling under the `Location` type that is tagged with any other entity tag such as `Structural` or `Geological` tagged `Location` entities. We could also further drill down on our results by using the `excludeList` parameter. `GPE` tagged entities could be tagged with the following tags: `City`, `State`, `CountryRegion`, `Continent`. We could, for example, exclude `Continent` and `CountryRegion` tags for our example:
+This method returns all `Location` entities only falling under the `GPE` tag and ignore any other entity falling under the `Location` type that is tagged with any other entity tag such as `Structural` or `Geological` tagged `Location` entities. We can also further analyze our results by using the `excludeList` parameter. `GPE` tagged entities could be tagged with the following tags: `City`, `State`, `CountryRegion`, `Continent`. We could, for example, exclude `Continent` and `CountryRegion` tags for our example:
 
 ```bash
 
@@ -107,19 +107,19 @@ This method returns all `Location` entities only falling under the `GPE` tag and
 
 Using these parameters we can successfully filter on only `Location` entity types, since the `GPE` entity tag included in the `includeList` parameter, falls under the `Location` type. We then filter on only Geopolitical entities and exclude any entities tagged with `Continent` or `CountryRegion` tags.
 
-## Additional output attributes
+## Supported output attributes
 
 In order to provide users with more insight into an entity's types and provide increased usability, NER supports these attributes in the output:
 
 |Name of the attribute|Type        |Definition                               |
 |---------------------|------------|-----------------------------------------|
-|`type`               |String      |The most specific type of detected entity.<br><br>For example, “Seattle” is a `City`, a `GPE` (Geo Political Entity) and a `Location`. The most granular classification for “Seattle” is that it is a `City`. The type would be `City` for the text “Seattle".|
-|`tags`               |List (tags) |A list of tag objects which expresses the affinity of the detected entity to a hierarchy or any other grouping.<br><br>A tag contains two fields:<br>1. `name`: A unique name for the tag.<br>2. `confidenceScore`: The associated confidence score for a tag ranging from 0 to 1.<br><br>This unique tagName is used to filter in the `inclusionList` and `exclusionList` parameters.
+|`type`               |String      |The most specific type of detected entity.<br><br>For example, "Seattle" is a `City`, a `GPE` (Geo Political Entity) and a `Location`. The most granular classification for "Seattle" is `City`. The type is `City` for the text "Seattle."|
+|`tags`               |List (tags) |A list of tag objects that expresses the affinity of the detected entity to a hierarchy or any other grouping.<br><br>A tag contains two fields:<br>- `name`: A unique name for the tag.<br>- `confidenceScore`: The associated confidence score for a tag ranging from 0 to 1.<br><br>This unique tagName is used to filter in the `inclusionList` and `exclusionList` parameters.
 |`metadata`           |Object      |Metadata is an object containing more data about the entity type detected. It changes based on the field `metadataKind`.
 
 ## Sample output
 
-This sample output includes an example of the additional output attributes.
+This sample output includes an example of output attributes.
 
 ```bash
 { 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "命名エンティティ認識の呼び出し方法の改善"
}
```

### Explanation
この変更は、命名エンティティ認識（NER）機能に関するドキュメント「呼び出し方法」の内容を更新するもので、主にテキストの表現を改善し、理解しやすさを向上させることを目的としています。

具体的には、いくつかの文の表現が修正されており、「if」の開始文字が大文字の「If」に変更され、より標準的で自然な読みやすさが示されるようになっています。また、出力属性に関するセクションのタイトルが「追加の出力属性」から「サポートされている出力属性」に変更され、より明確な表現となっています。

加えて、属性に関する説明がより簡潔になり、ユーザーが得られるデータのタイプやその定義が整理されています。このような変更により、ドキュメントは技術的な正確さを保ちながら、読者にとって理解しやすいものとなっています。

## articles/ai-services/language-service/native-document-support/overview.md{#item-a490e5}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-language
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 02/19/2025
+ms.date: 08/20/2025
 ms.author: lajanuar
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ネイティブドキュメントサポートの概要の日付更新"
}
```

### Explanation
この変更は、ネイティブドキュメントサポートに関するドキュメントの最終更新日を変更するためのものです。具体的には、`ms.date`フィールドの日付が2025年2月19日から2025年8月20日に修正されました。

このような日付の更新は、ユーザーに最新の情報を提供するために重要であり、ドキュメントの信頼性と最新性を保つために役立ちます。その他の内容についての変更はありませんが、日付の更新自体が、関連する他の情報が新しいものであることを示唆しています。

## articles/ai-services/language-service/orchestration-workflow/overview.md{#item-53d49f}

<details>
<summary>Diff</summary>
````diff
@@ -69,7 +69,7 @@ As you use orchestration workflow, see the following reference documentation and
 
 ## Responsible AI 
 
-An AI system includes not only the technology, but also the people who will use it, the people who will be affected by it, and the environment in which it is deployed. Read the transparency note for CLU and orchestration workflow to learn about responsible AI use and deployment in your systems. You can also see the following articles for more information:
+An AI system includes not only the technology, but also the people who will use it, the people who will be affected by it, and the environment in which it is deployed. Read the transparency note for CLU and orchestration workflow to learn about responsible AI use and deployment in your systems. 
 
 [!INCLUDE [Responsible AI links](../includes/overview-responsible-ai-links.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オーケストレーションワークフローにおける責任あるAIセクションの修正"
}
```

### Explanation
この変更は、オーケストレーションワークフローに関するドキュメント内の「責任あるAI」セクションを改善するためのものです。具体的には、AIシステムが技術だけでなく、それを使用する人々、影響を受ける人々、およびその導入環境を含むことを説明する文の後に、詳しい情報を提供するリンクが追加されました。

変更にあたって、元の文「次の記事も参照してください」という部分が削除され、その代わりに、別の文が追加されていませんが、[!INCLUDE [Responsible AI links](../includes/overview-responsible-ai-links.md)]というインクルードタグによって、関連情報が統合されるようになっています。このことにより、読者は責任あるAIの使用および展開に関するさらなる情報を簡単に参照できるようになります。全体として、文書の明確さと情報の提供方法が向上しています。

## articles/ai-services/language-service/sentiment-opinion-mining/overview.md{#item-831fe6}

<details>
<summary>Diff</summary>
````diff
@@ -6,20 +6,20 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 02/17/2025
+ms.date: 08/19/2025
 ms.author: lajanuar
 ms.custom: language-service-sentiment-opinion-mining
 ---
 
 # What is sentiment analysis and opinion mining?
 
-Sentiment analysis and opinion mining are features offered by [the Language service](../overview.md), a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. These features help you find out what people think of your brand or topic by mining text for clues about positive or negative sentiment, and can associate them with specific aspects of the text. 
+Sentiment analysis and opinion mining are features offered by [the Language service](../overview.md), a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. These features help you discover what people think about your brand or topic by analyzing text for signs of positive or negative sentiment. They can also link these sentiments to specific aspects of the text.
 
 Both sentiment analysis and opinion mining work with various [written languages](./language-support.md).
 
-## Sentiment analysis 
+## Sentiment analysis
 
-The sentiment analysis feature provides sentiment labels (such as "negative", "neutral" and "positive") based on the highest confidence score found by the service at a sentence and document-level. This feature also returns confidence scores between 0 and 1 for each document & sentences within it for positive, neutral, and negative sentiment. 
+The sentiment analysis feature assigns sentiment labels, such as "negative," "neutral," and "positive." The service determines these labels using the highest confidence score. Sentiment is evaluated at both the sentence level and the document level. This feature also returns confidence scores between 0 and 1 for each document & sentences within it for positive, neutral, and negative sentiment.
 
 ## Opinion mining
 
@@ -31,7 +31,7 @@ Opinion mining is a feature of sentiment analysis, also known as aspect-based se
 
 [!INCLUDE [development options](./includes/development-options.md)]
 
-[!INCLUDE [Developer reference](../includes/reference-samples-text-analytics.md)] 
+[!INCLUDE [Developer reference](../includes/reference-samples-text-analytics.md)]
 
 ## Reference documentation
 
@@ -42,13 +42,12 @@ As you use sentiment analysis, see the following reference documentation and sam
 |REST APIs (Authoring)   | [REST API documentation](https://aka.ms/ct-authoring-swagger)        |         |
 |REST APIs (Runtime)    | [REST API documentation](https://aka.ms/ct-runtime-swagger)        |         |
 
---- 
+---
 
-## Responsible AI 
+## Responsible AI
 
-An AI system includes not only the technology, but also the people who use it, the people who are affected by it, and the environment in which it's deployed. Read the [transparency note for sentiment analysis](/azure/ai-foundry/responsible-ai/language-service/transparency-note-sentiment-analysis) to learn about responsible AI use and deployment in your systems. You can also see the following articles for more information:
+An AI system encompasses more than just the technology itself. An AI system includes the individuals who operate the system, the people who experience its effects, and the broader environment where the system functions all play a role. Read the [transparency note for sentiment analysis](/azure/ai-foundry/responsible-ai/language-service/transparency-note-sentiment-analysis) to learn about responsible AI use and deployment in your systems. 
 
 ## Next steps
 
-* The quickstart articles with instructions on using the service for the first time.
-    * [Use sentiment analysis and opinion mining](./quickstart.md)
\ No newline at end of file
+Get started with our quickstart articles with instructions on using the service for the first time: [Use sentiment analysis and opinion mining](./quickstart.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "感情分析と意見マイニングの概要の文書改善"
}
```

### Explanation
この変更は、感情分析と意見マイニングに関する文書の改善を目的としています。具体的には、いくつかの文が rephrased（言い換えられ）て、より明確で読みやすい表現に修正されています。また、最終更新日が2025年2月17日から2025年8月19日に変更されました。

具体的な変更点には、感情ラベルの説明の方法が修正され、文章の一貫性を向上させています。たとえば、「これらの特徴は、ポジティブまたはネガティブな感情の兆候をテキスト中で分析することによって、人々がブランドやトピックについて考えていることを発見するのに役立ちます」という部分が、より直感的な表現に改訂されました。また、「責任あるAI」に関するセクションでも微妙な表現の改善が見られます。

全体的に、文書の流れや明瞭さが高まり、読者が感情分析と意見マイニングの特性や利用方法をより理解しやすくなっています。

## articles/ai-services/language-service/summarization/quickstart.md{#item-bff856}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 02/17/2025
+ms.date: 08/20/2025
 ms.author: lajanuar
 ms.devlang: csharp
 # ms.devlang: csharp, java, javascript, python
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "要約機能のクイックスタート文書の更新日変更"
}
```

### Explanation
この変更は、要約機能に関するクイックスタート文書の更新日を変更することを目的としています。具体的には、最終更新日が2025年2月17日から2025年8月20日に修正されました。この更新は、文書が最新の情報を反映するためのものであり、ユーザーが新しいリソースや情報を得る際に役立つようになっています。

文書の他の部分には変更は行われていないため、全体的な内容や構成には影響がありませんが、更新日を最新のものに反映させることで、ユーザーへの信頼性と透明性が高まります。

## articles/ai-services/language-service/text-analytics-for-health/overview.md{#item-982d4c}

<details>
<summary>Diff</summary>
````diff
@@ -7,19 +7,19 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 02/17/2025
+ms.date: 08/19/2025
 ms.author: lajanuar
-ms.custom: language-service-health, ignite-2024
+ms.custom: language-service-health
 ---
 
 # What is Text Analytics for health?
 
 [!INCLUDE [service notice](includes/service-notice.md)]
 
-Text Analytics for health is one of the prebuilt features offered by [Azure AI Language](../overview.md). It is a cloud-based API service that applies machine-learning intelligence to extract and label relevant medical information from a variety of unstructured texts such as doctor's notes, discharge summaries, clinical documents, and electronic health records. 
+Text Analytics for health is one of the prebuilt features offered by [Azure AI Language](../overview.md). Text Analytics for health uses machine learning to identify and label medical information in unstructured text such as doctor's notes, clinical documents, and electronic health records. It extracts key data from sources like discharge summaries to support healthcare analysis.
 
 > [!TIP]
-> Try out Text Analytics for health [in Azure AI Foundry portal](https://ai.azure.com/explore/language), where you can [utilize a currently existing Language Studio resource or create a new Azure AI Foundry resource](../../../ai-services/connect-services-ai-foundry-portal.md) in order to use this service. 
+> Try out Text Analytics for health [in Azure AI Foundry portal](https://ai.azure.com/explore/language). There you can [utilize a currently existing Language Studio resource or create a new Azure AI Foundry resource](../../../ai-services/connect-services-ai-foundry-portal.md) in order to use this service.
 
 This documentation contains the following types of articles:
 * The [**quickstart article**](quickstart.md) provides a short tutorial that guides you with making your first request to the service.
@@ -28,26 +28,31 @@ This documentation contains the following types of articles:
 
 ## Text Analytics for health features
 
-Text Analytics for health performs four key functions which are named entity recognition, relation extraction, entity linking, and assertion detection, all with a single API call.
+Text Analytics for health performs four key functions, all with a single API call:
+
+* Named entity recognition
+* Relation extraction
+* Entity linking
+* Assertion detection
 
 [!INCLUDE [Text Analytics for health](includes/features.md)]
 
 Text Analytics for health can receive unstructured text in English, German, French, Italian, Spanish, Portuguese, and Hebrew.
 
-Additionally, Text Analytics for health can return the processed output using the Fast Healthcare Interoperability Resources (FHIR) structure which enables the service's integration with other electronic health systems.  
+Additionally, Text Analytics for health can return the processed output using the Fast Healthcare Interoperability Resources (FHIR) structure that enables the service's integration with other electronic health systems.
 
 
 
 > [!VIDEO https://learn.microsoft.com/Shows/AI-Show/Introducing-Text-Analytics-for-Health/player]
 
 ## Usage scenarios
 
-Text Analytics for health can be used in multiple scenarios across a variety of industries.
+Text Analytics for health can be used in multiple scenarios across various industries.
 Some common customer motivations for using Text Analytics for health include:
 * Assisting and automating the processing of medical documents by proper medical coding to ensure accurate care and billing.
 * Increasing the efficiency of analyzing healthcare data to help drive the success of value-based care models similar to Medicare.
 * Minimizing healthcare provider effort by automating the aggregation of key patient data for trend and pattern monitoring.
-* Facilitating and supporting the adoption of HL7 standards for improved exchange, integration, sharing, retrieval, and delivery of electronic health information in all healthcare services.    
+* Facilitating and supporting the adoption of HL7 standards across the healthcare industry. By doing so, we help improve the exchange, integration, sharing, retrieval, and delivery of electronic health information in all areas of healthcare services.
 
 ### Example use cases: 
 
@@ -56,25 +61,25 @@ Some common customer motivations for using Text Analytics for health include:
 |Extract insights and statistics|Identify medical entities such as symptoms, medications, diagnosis from clinical and research documents in order to extract insights and statistics for different patient cohorts.|
 |Develop predictive models using historic data|Power solutions for planning, decision support, risk analysis and more, based on prediction models created from historic data.|
 |Annotate and curate medical information|Support solutions for clinical data annotation and curation such as automating clinical coding and digitizing manually created data.|
-|Review and report medical information|Support solutions for reporting and flagging possible errors in medical information resulting from reviewal processes such as quality assurance.|
-|Assist with decision support|Enable solutions that provide humans with assistive information relating to patients’ medical information for faster and more reliable decisions.|
+|Review and report medical information|potential medical information errors found during quality assurance reviews.|
+|Assist with decision support|Enable solutions that provide humans with assistive information relating to patients' medical information for faster and more reliable decisions.|
 
 ## Get started with Text Analytics for health
 
-[!INCLUDE [Development options](./includes/development-options.md)] 
+[!INCLUDE [Development options](./includes/development-options.md)]
 
 
 ## Input requirements and service limits
 
 Text Analytics for health is designed to receive unstructured text for analysis. For more information, see [data and service limits](../concepts/data-limits.md).
 
-Text Analytics for health works with a variety of input languages. For more information,  see [language support](language-support.md).
+Text Analytics for health works with various input languages. For more information,  see [language support](language-support.md).
 
-[!INCLUDE [Developer reference](../includes/reference-samples-text-analytics.md)] 
+[!INCLUDE [Developer reference](../includes/reference-samples-text-analytics.md)]
 
 
-## Responsible use of AI 
+## Responsible use of AI
 
-An AI system includes the technology, the people who will use it, the people who will be affected by it, and the environment in which it is deployed. Read the [transparency note for Text Analytics for health](/azure/ai-foundry/responsible-ai/language-service/transparency-note-health) to learn about responsible AI use and deployment in your systems. You can also refer to the following articles for more information:
+An AI system includes the technology, the individuals who operate the system, the people who experience its effects, and the broader environment where the system functions all play a role. Read the [transparency note for Text Analytics for health](/azure/ai-foundry/responsible-ai/language-service/transparency-note-health) to learn about responsible AI use and deployment in your systems. 
 
 [!INCLUDE [Responsible AI links](../includes/overview-responsible-ai-links.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "健康向けテキスト分析の概要文書の改善"
}
```

### Explanation
この変更は、健康向けテキスト分析に関する概要文書を改善するためのもので、いくつかの文が再構成され、内容がより明確にされました。また、最終更新日が2025年2月17日から2025年8月19日に変更されています。

具体的な変更点としては、機械学習によって医療情報を特定し、ラベル付けするプロセスがより明確に説明されるように書き換えられています。また、機能のリストが箇条書き形式に整理され、ユーザーが理解しやすくなっています。追加された情報により、情報の流れが向上し、内容がより直感的になっています。

さらに、医療文書の処理における利点や利用シナリオについても改善され、HL7基準のサポートが強調されています。これにより、利用者が健康向けテキスト分析の重要性や適用範囲をよりよく理解できるようになっています。全体として、文書はより使いやすく、情報が整理された形で提供されています。

## articles/ai-services/language-service/text-analytics-for-health/quickstart.md{#item-9b06f2}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 02/16/2025
+ms.date: 08/20/2025
 ms.author: lajanuar
 ms.devlang: csharp
 # ms.devlang: csharp, java, javascript, python
@@ -18,7 +18,7 @@ zone_pivot_groups: programming-languages-text-analytics
 
 # Quickstart: Using Text Analytics for health client library and REST API
 
-This article contains Text Analytics for health quickstarts that help with using the supported client libraries, C#, Java, NodeJS, and Python as well as with using the REST API.
+This article contains Text Analytics for health quickstarts that help with using the supported client libraries, C#, Java, NodeJS, and Python and the REST API.
 
 [!INCLUDE [Use Language Studio](../includes/use-language-studio.md)]
 ::: zone pivot="programming-language-csharp"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "健康向けテキスト分析のクイックスタート文書の更新日変更"
}
```

### Explanation
この変更は、健康向けテキスト分析のクイックスタート文書に関するもので、主に更新日を変更するために実施されました。具体的には、最終更新日が2025年2月16日から2025年8月20日に変更されています。

また、文中の一文がわずかに修正され、REST APIに関する言及が文の最後に追加されています。これにより、クイックスタートが提供する情報がより明確になり、ユーザーがさまざまなクライアントライブラリとREST APIの利用方法を理解しやすくなっています。この文書は、プログラミング言語におけるサポートを促進するため、テキスト分析の機能を活用する際のガイドとして引き続き役立つ内容になっています。全体として、大きな変更はないものの、ユーザー体験を向上させるための重要な更新が行われています。


