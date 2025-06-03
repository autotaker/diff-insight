---
date: '2025-06-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:178e7a4...MicrosoftDocs:8d764d4
summary: この変更は、文書インテリジェンス、個人情報（PII）、健康情報（PHI）、および各種SDK（C#, Java, Node.js, Python）のクイックスタートドキュメントに関する軽微な更新を含んでいます。また、Azure
  AI Languageの新機能についても更新されています。主なポイントとしては、モデルの有効期限に関するガイドラインの追加、PII検出カスタマイズ、日付関連エンティティの導入が含まれます。特に大きな変更はなく、SDKやREST
  APIのドキュメントにおけるメタデータの整理や将来のリリース関連メタデータの追加が行われています。このような変更を通じて、ユーザーは最新の情報を得やすくなり、AI技術をより効果的に活用できるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:178e7a4...MicrosoftDocs:8d764d4){target="_blank"}

<format>
# Highlights
この変更は主に文書インテリジェンスおよび個人情報（PII）、健康情報（PHI）、さらに各種SDK（C#, Java, Node.js, Python）のクイックスタートドキュメントに関する軽微な更新を含んでいます。また、Azure AI Languageの新機能についての更新も行われています。

## New features
- `custom-lifecycle.md`にモデルの有効期限に関する明確なガイドライン追加。
- Azure AI LanguageにPII検出カスタマイズ、日付関連エンティティの導入。

## Breaking changes
- 特になし。

## Other updates
- 各SDKおよびREST APIのドキュメントにおけるメタデータの整理。
- `build-2025`など将来のリリース関連のメタデータ追加。
- APIバージョンの参照更新によるエンティティカテゴリの明確化。

# Insights
このコードの変更は、AI関連のドキュメントを整理し、最新情報を提供することを目的としています。各SDKのクイックスタートドキュメントには、著者情報やドキュメントの更新日だけでなく、将来のリリースに向けたメタデータが追加されており、ドキュメントの整備と管理性が向上しています。これにより、ユーザーは最新の開発進捗や機能を把握しやすくなりました。

特に、`custom-lifecycle.md`の更新では、AIモデルのライフサイクル管理の重要性が強調されました。モデルを最新のAPIで再トレーニングする必要があるというガイドラインは、長期使用する上でユーザーにとって不可欠な情報です。また、Azure AI Languageのドキュメントにも大幅な強化が加えられ、Microsoft Build Conferenceの発表内容が詳細に記載されています。これにより、新機能の理解が深まり、ユーザーはより効果的なAIサービスの活用が期待できるでしょう。

このように、ドキュメント全体が最新の情報を反映し、実用的なリソースへと進化しています。特に組織がAIテクノロジーを長期的に活用するために、これらの更新は非常に有用です。各メタデータやAPIバージョンの更新を通じて、ユーザーは最新の環境下で継続して作業を進められるという安心感を得ることができます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [custom-lifecycle.md](#item-2b7401) | minor update | 文書インテリジェンスのカスタムライフサイクル更新 | modified | 4 | 2 | 6 | 
| [entity-categories.md](#item-ba2623) | minor update | 個人情報と健康情報のエンティティカテゴリのAPIバージョン変更 | modified | 2 | 2 | 4 | 
| [csharp-sdk.md](#item-67858f) | minor update | C# SDKのクイックスタートドキュメントの更新 | modified | 6 | 3 | 9 | 
| [java-sdk.md](#item-1f313c) | minor update | Java SDKのクイックスタートドキュメントの更新 | modified | 6 | 3 | 9 | 
| [nodejs-sdk.md](#item-e367fd) | minor update | Node.js SDKのクイックスタートドキュメントの更新 | modified | 6 | 3 | 9 | 
| [python-sdk.md](#item-3ba8dc) | minor update | Python SDKのクイックスタートドキュメントの更新 | modified | 6 | 3 | 9 | 
| [rest-api.md](#item-842eb5) | minor update | REST APIのクイックスタートドキュメントの更新 | modified | 6 | 3 | 9 | 
| [csharp-sdk.md](#item-041480) | minor update | C# SDKの要約ドキュメントの更新 | modified | 4 | 3 | 7 | 
| [java-sdk.md](#item-c604e9) | minor update | Java SDKの要約ドキュメントの更新 | modified | 6 | 3 | 9 | 
| [nodejs-sdk.md](#item-8bd4c1) | minor update | Node.js SDKの要約ドキュメントの更新 | modified | 6 | 3 | 9 | 
| [python-sdk.md](#item-c8a5f8) | minor update | Python SDKの要約ドキュメントの更新 | modified | 4 | 3 | 7 | 
| [csharp-sdk.md](#item-4e0f03) | minor update | C# SDKの要約ドキュメントの更新 | modified | 4 | 3 | 7 | 
| [java-sdk.md](#item-7011c4) | minor update | Java SDKの要約ドキュメントの更新 | modified | 6 | 3 | 9 | 
| [nodejs-sdk.md](#item-de5e8a) | minor update | Node.js SDKの要約ドキュメントの更新 | modified | 6 | 3 | 9 | 
| [python-sdk.md](#item-544ea5) | minor update | Python SDKの要約ドキュメントの更新 | modified | 4 | 3 | 7 | 
| [rest-api.md](#item-ba4862) | minor update | REST APIに関する要約ドキュメントの更新 | modified | 4 | 3 | 7 | 
| [whats-new.md](#item-69b272) | minor update | Azure AI Languageの新機能および更新内容の追加 | modified | 81 | 64 | 145 | 


# Modified Contents
## articles/ai-services/document-intelligence/train/custom-lifecycle.md{#item-2b7401}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 11/19/2024
+ms.date: 06/02/2025
 ms.author: lajanuar
 monikerRange: '>=doc-intel-3.1.0'
 ---
@@ -22,7 +22,9 @@ With the v3.1 (GA) and later APIs, custom models introduce a expirationDateTime
 
 ## Models trained with GA API version
 
-With the v3.1 API, custom models introduce a new model expiration property. The model expiration is set to two years from the date the model is built for all requests that use a GA API to build a model. To continue to use the model past the expiration date, you need to  train the model with a current GA API version. The API version can be the one that the model was originally trained with or a later API version. The following figure illustrates the options when you need to retrain an expiring or expired model.
+With the v3.1 API, custom models introduce a new model expiration property. The model is configured to expire two years after its creation for all requests utilizing a GA API to build it. The API version can be the one that the model was originally trained with or a later API version. The following figure illustrates the options when you need to retrain an expiring or expired model.
+
+> Note: The model expiration date for v3.1/4.0 models is only set if the training is done post release of v3.1/v4.0. If the models were created earlier with no expiration date associated with them and were not retrained after v3.1/v4.0, the expiration date will be null. The models with expiration date property will still be available until the API retires. Notification of retirement of any particular GA API version will be communicated at least 3 years before expiration.
 
 :::image type="content" source="../media/model-lifecycle.png" alt-text="Screenshot showing how to choose an API version and retrain a model.":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書インテリジェンスのカスタムライフサイクル更新"
}
```

### Explanation
この変更では、`custom-lifecycle.md`ドキュメントの内容が更新され、モデルの有効期限に関する詳細が追加されました。具体的には、カスタムモデルの有効期限が作成から2年間に設定されることが明確に記載され、モデルが有効期限を過ぎた後も利用を続けるためには、最新のGA APIバージョンでモデルを再トレーニングする必要があることに言及されています。また、新しい注意点として、モデルがv3.1またはv4.0以降にトレーニングされた場合のみ、有効期限の日付が設定されることが強調されています。これにより、以前に作成されたモデルについては、有効期限が設定されない可能性があることが説明されています。この変更は、ユーザーがモデルのライフサイクルを理解し、適切に管理できるようにするための重要な情報を提供します。

## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories.md{#item-ba2623}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ The PII feature includes the ability to detect personal (`PII`) and health (`PHI
 
 The following entity categories are returned when you're sending API requests PII feature.
 
-# [Generally Available API](#tab/ga-api)
+# [Preview API](#tab/preview-api)
 
 ## Category: Person
 
@@ -627,7 +627,7 @@ These entity categories include identifiable Azure information like authenticati
     :::column-end:::
 :::row-end:::
 
-# [Preview API](#tab/preview-api)
+# [Generally Available API](#tab/ga-api)
 
 ## Type: Person
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人情報と健康情報のエンティティカテゴリのAPIバージョン変更"
}
```

### Explanation
この変更では、`entity-categories.md`ドキュメント内で、個人情報（PII）および健康情報（PHI）を処理するAPIのバージョンが更新されました。具体的には、APIリクエストを送信する際に返されるエンティティカテゴリの参照が、一般提供（GA）APIからプレビューAPIへ、またその逆も行われています。この変更により、利用者はどのAPIバージョンを使用するかについての明確な指針を得ることができ、特にプレビュー版と一般提供版の違いについての理解が深まります。この微調整は、ユーザーが最適なAPIを選択する際に役立つ情報を提供しています。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/csharp-sdk.md{#item-67858f}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,14 @@
 ---
 author: laujan
+ms.author: lajanuar
 manager: nitinme
+ms.date: 12/19/2023
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 12/19/2023
-ms.author: lajanuar
-ms.custom: language-service-pii, ignite-2024
+ms.custom:
+  - language-service-pii
+  - ignite-2024
+  - build-2025
 ---
 
 [Reference documentation](/dotnet/api/azure.ai.textanalytics?preserve-view=true&view=azure-dotnet) | [More samples](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics/samples) | [Package (NuGet)](https://www.nuget.org/packages/Azure.AI.TextAnalytics/5.2.0) | [Library source code](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDKのクイックスタートドキュメントの更新"
}
```

### Explanation
この変更では、C# SDKに関するクイックスタートドキュメント`csharp-sdk.md`が更新され、いくつかのメタデータが修正されました。具体的には、著者情報として`ms.author`が再追加され、ドキュメントの日付が明確に設定されています。また、カスタムメタデータの項目に`build-2025`が追加され、これは将来のリリースに関連する情報を示唆しています。この変更により、ユーザーはドキュメントの作成日や著者に関する最新情報を確認でき、さらにリリース関連のキーワードが明示されることで、参照が容易になります。全体として、クイックスタートガイドの情報がより一貫性を持ち、管理しやすくなっています。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/java-sdk.md{#item-1f313c}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,14 @@
 ---
 author: laujan
+ms.author: lajanuar
 manager: nitinme
+ms.date: 12/19/2023
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 12/19/2023
-ms.author: lajanuar
-ms.custom: language-service-pii, ignite-2024
+ms.custom:
+  - language-service-pii
+  - ignite-2024
+  - build-2025
 ---
 
 [Reference documentation](/java/api/overview/azure/ai-textanalytics-readme?preserve-view=true&view=azure-java-stable) | [More samples](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics/src/samples) | [Package (Maven)](https://mvnrepository.com/artifact/com.azure/azure-ai-textanalytics/5.2.0) | [Library source code](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java SDKのクイックスタートドキュメントの更新"
}
```

### Explanation
この変更では、Java SDKに関するクイックスタートドキュメント`java-sdk.md`が更新され、いくつかのメタデータが改訂されています。具体的には、著者情報の設定が再確認され、ドキュメントの日付が明記されています。また、カスタムメタデータの項目に`build-2025`が追加され、今後のリリースに関連する情報が含まれています。この更新により、ドキュメントはより一貫性があり、利用者は最新の著者情報や日付を確認することができ、さらにリリース関連のキーワードが提供されることで、ナビゲーションが容易になります。全体として、クイックスタートガイドは管理のしやすさが向上し、ユーザーにとって役立つリソースとなっています。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/nodejs-sdk.md{#item-e367fd}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,14 @@
 ---
 author: laujan
+ms.author: lajanuar
 manager: nitinme
+ms.date: 12/19/2023
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 12/19/2023
-ms.author: lajanuar
-ms.custom: devx-track-js, ignite-2024
+ms.custom:
+  - devx-track-js
+  - ignite-2024
+  - build-2025
 ---
 
 [Reference documentation](/javascript/api/overview/azure/ai-language-text-readme) | [More samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/cognitivelanguage/ai-language-text/samples/v1) | [Package (npm)](https://www.npmjs.com/package/@azure/ai-language-text) | [Library source code](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/cognitivelanguage/ai-language-text) 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Node.js SDKのクイックスタートドキュメントの更新"
}
```

### Explanation
この変更では、Node.js SDKに関するクイックスタートドキュメント`nodejs-sdk.md`が更新され、一部のメタデータが修正されています。具体的には、著者情報に`ms.author`が明確に設定され、ドキュメントの日付が追記されています。また、カスタムメタデータに新たに`build-2025`が追加され、既存の情報に対して補足がされています。この更新によって、ユーザーは最新の著者情報や日付を確認しやすくなり、さらにリリース関連の重要なキーワードが示されることで、ドキュメントをより効果的に利用することが可能になります。全体として、クイックスタートガイドが整理され、ユーザーにとって利便性が高まる内容となっています。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/python-sdk.md{#item-3ba8dc}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +1,13 @@
 ---
 author: laujan
+ms.author: lajanuar
+ms.date: 12/19/2023
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 12/19/2023
-ms.author: lajanuar
-ms.custom: language-service-pii, ignite-2024
+ms.custom:
+  - language-service-pii
+  - ignite-2024
+  - build-2025
 ---
 
 [Reference documentation](/python/api/azure-ai-textanalytics/azure.ai.textanalytics?preserve-view=true&view=azure-python) |  [More samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics/samples) | [Package (PyPi)](https://pypi.org/project/azure-ai-textanalytics/5.2.0/) | [Library source code](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python SDKのクイックスタートドキュメントの更新"
}
```

### Explanation
この変更では、Python SDKに関連するクイックスタートドキュメント`python-sdk.md`が改訂され、いくつかのメタデータが追加されています。具体的には、著者情報に`ms.author`が設定され、ドキュメントの日付が追記されており、読者が最新の情報を把握しやすくなっています。また、カスタムメタデータに`build-2025`が追加されており、今後のリリースに関する情報が強調されています。この更新を通じて、クイックスタートガイドは整理され、さらなるナビゲーションの向上が図られています。全体として、ユーザーがこのドキュメントを有効に活用できるよう、重要な情報が明確に示されるようになっています。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/rest-api.md{#item-842eb5}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,14 @@
 ---
 author: laujan
+ms.author: lajanuar
 manager: nitinme
+ms.date: 12/19/2023
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 12/19/2023
-ms.author: lajanuar
-ms.custom: language-service-pii, ignite-2024
+ms.custom:
+  - language-service-pii
+  - ignite-2024
+  - build-2025
 ---
 
 [Reference documentation](https://go.microsoft.com/fwlink/?linkid=2239169)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIのクイックスタートドキュメントの更新"
}
```

### Explanation
この変更では、REST APIに関するクイックスタートドキュメント`rest-api.md`のいくつかのメタデータが更新されました。具体的には、著者情報の`ms.author`が追加され、ドキュメントの日付も新たに追記されています。さらに、カスタムメタデータセクションに`build-2025`が新たに加えられ、既存の情報と合わせて、今後のリリースに関連する重要なキーワードが示されています。この更新により、ドキュメントはより整理され、ユーザーが必要な情報を迅速に見つけられるよう改善が図られています。全体的に、ユーザーにとっての利便性が向上し、ドキュメントの価値が高まっています。

## articles/ai-services/language-service/summarization/includes/quickstarts/csharp-sdk.md{#item-041480}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +1,14 @@
 ---
 author: laujan
+ms.author: lajanuar
 manager: nitinme
+ms.date: 12/19/2023
 ms.service: azure-ai-language
+ms.topic: include
 ms.custom:
   - build-2024
   - ignite-2024
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: lajanuar
+  - build-2025
 ---
 
 # [Text summarization](#tab/text-summarization)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDKの要約ドキュメントの更新"
}
```

### Explanation
この変更では、C# SDKに関する要約ドキュメント`csharp-sdk.md`が更新され、いくつかの重要なメタデータが追加されました。主な更新内容として、著者情報の`ms.author`が明示され、ドキュメントの日付が再確認されています。また、`ms.custom`セクションには`build-2025`が加わり、既存の情報とともに、今後のリリースに関するトピックが整理されています。さらに、`ms.topic`が新たに追加され、ドキュメントのトピックが明確に示されています。この改訂により、ユーザーにとってのドキュメントの可読性が向上し、必要な情報にアクセスしやすくなることが期待されます。全体として、ドキュメントの専門性と利便性が高まっています。

## articles/ai-services/language-service/summarization/includes/quickstarts/java-sdk.md{#item-c604e9}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,14 @@
 ---
 author: laujan
+ms.author: lajanuar
 manager: nitinme
+ms.date: 12/19/2023
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 12/19/2023
-ms.custom: devx-track-java, ignite-2024
-ms.author: lajanuar
+ms.custom:
+  - devx-track-java
+  - ignite-2024
+  - build-2025
 ---
 
 [Reference documentation](/java/api/overview/azure/ai-textanalytics-readme?view=azure-java-preview&preserve-view=true) | [More samples](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics/src/samples) | [Package (Maven)](https://mvnrepository.com/artifact/com.azure/azure-ai-textanalytics/5.3.0) | [Library source code](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java SDKの要約ドキュメントの更新"
}
```

### Explanation
この変更では、Java SDKに関する要約ドキュメント`java-sdk.md`が更新され、いくつかのメタデータが追加されています。具体的には、著者情報として`ms.author`が記載され、ドキュメントの日付も新たに追加されています。加えて、`ms.custom`セクションには`build-2025`が追加され、その他のキーワードとともにプロジェクトのトラッキングやリリースに関連する情報が整理されています。この更新によって、ユーザーはドキュメント内の関連情報をより簡単に追跡できるようになるとともに、内容の可読性が向上しています。全体として、ドキュメントが最新の情報に基づいて管理されていることが示されており、利用者への利便性が高まる結果となっています。

## articles/ai-services/language-service/summarization/includes/quickstarts/nodejs-sdk.md{#item-8bd4c1}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,14 @@
 ---
 author: laujan
+ms.author: lajanuar
 manager: nitinme
+ms.date: 12/19/2023
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 12/19/2023
-ms.author: lajanuar
-ms.custom: devx-track-js, ignite-2024
+ms.custom:
+  - devx-track-js
+  - ignite-2024
+  - build-2025
 ---
 
 [Reference documentation](/javascript/api/overview/azure/ai-language-text-readme?view=azure-node-latest&preserve-view=true) | [Additional samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/textanalytics/ai-text-analytics/samples) | [Package (npm)](https://www.npmjs.com/package/@azure/ai-text-analytics/v/5.2.0-beta.1) | [Library source code](https://github.com/Azure/azure-sdk-for-js/tree/master/sdk/textanalytics/ai-text-analytics) 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Node.js SDKの要約ドキュメントの更新"
}
```

### Explanation
この変更では、Node.js SDKに関する要約ドキュメント`nodejs-sdk.md`が修正され、いくつかの重要なメタデータが追加されました。具体的には、著者情報に`ms.author`が追加され、ドキュメントの日付も新たに記載されています。また、`ms.custom`セクションには、新たに`build-2025`が追加され、既存のキーワードとともに、プロジェクトやリリースに関する情報が整理されています。この改訂により、ユーザーはドキュメント内の関連情報をより効率的に追跡できるようになり、内容の可読性が向上しています。全体的には、ドキュメントが最新の情報に基づいて整備され、利用者にとってより役立つ内容となっています。

## articles/ai-services/language-service/summarization/includes/quickstarts/python-sdk.md{#item-c8a5f8}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,13 @@
 ---
 author: laujan
+ms.author: lajanuar
+ms.date: 12/19/2023
 ms.service: azure-ai-language
+ms.topic: include
 ms.custom:
   - build-2024
   - ignite-2024
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: lajanuar
+  - build-2025
 ---
 
 # [Text summarization](#tab/text-summarization)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python SDKの要約ドキュメントの更新"
}
```

### Explanation
この変更では、Python SDKに関する要約ドキュメント`python-sdk.md`が修正され、いくつかの重要なメタデータが追加されました。具体的には、著者情報としての`ms.author`が追加され、ドキュメントの日付も新たに記載されています。また、`ms.custom`セクションには新たに`build-2025`が加わり、プロジェクトに関連する情報が整理されています。これにより、ユーザーはドキュメント内の関連情報をより簡単に把握できるようになるとともに、内容の整合性と可読性が向上しています。全体として、この更新は、利用者にとっての利便性を高めるための重要な改善となっています。

## articles/ai-services/language-service/text-analytics-for-health/includes/quickstarts/csharp-sdk.md{#item-4e0f03}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,13 @@
 ---
 author: laujan
+ms.author: lajanuar
 manager: nitinme
+ms.date: 12/19/2023
 ms.service: azure-ai-language
+ms.topic: include
 ms.custom:
   - ignite-2024
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: lajanuar
+  - build-2025
 ---
 
 [Reference documentation](/dotnet/api/azure.ai.textanalytics?preserve-view=true&view=azure-dotnet) | [More samples](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics/samples) | [Package (NuGet)](https://www.nuget.org/packages/Azure.AI.TextAnalytics/5.2.0) | [Library source code](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDKの要約ドキュメントの更新"
}
```

### Explanation
この変更では、C# SDKに関する要約ドキュメント`csharp-sdk.md`が修正され、いくつかの重要なメタデータが追加されました。具体的には、著者情報としての`ms.author`が追加され、ドキュメントの日付も新たに記載されています。また、`ms.custom`セクションには`build-2025`が追加され、プロジェクトに関連する情報が整理されています。これにより、ユーザーはドキュメントの関連情報をより簡単に把握でき、内容の整合性と可読性が向上しています。この更新は、利用者にとっての利便性を高めるための重要な改善といえます。

## articles/ai-services/language-service/text-analytics-for-health/includes/quickstarts/java-sdk.md{#item-7011c4}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,14 @@
 ---
 author: laujan
+ms.author: lajanuar
 manager: nitinme
+ms.date: 12/19/2023
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 12/19/2023
-ms.custom: devx-track-java, ignite-2024
-ms.author: lajanuar
+ms.custom:
+  - devx-track-java
+  - ignite-2024
+  - build-2025
 ---
 
 [Reference documentation](/java/api/overview/azure/ai-textanalytics-readme?preserve-view=true&view=azure-java-stable) | [More samples](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics/src/samples) | [Package (Maven)](https://mvnrepository.com/artifact/com.azure/azure-ai-textanalytics/5.2.0) | [Library source code](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java SDKの要約ドキュメントの更新"
}
```

### Explanation
この変更では、Java SDKに関する要約ドキュメント`java-sdk.md`が修正され、いくつかの重要なメタデータが追加されています。具体的には、著者情報としての`ms.author`が再度記載され、ドキュメントの日付が新たに追加されています。また、`ms.custom`セクションには新しいエントリ`build-2025`が追加され、従来の`devx-track-java`と`ignite-2024`と共に整理されています。これにより、ユーザーはドキュメントに関連する情報をより簡単に把握でき、内容の一貫性と可読性が向上しています。この更新は、利用者にとっての利便性を高めるための重要な改善といえます。

## articles/ai-services/language-service/text-analytics-for-health/includes/quickstarts/nodejs-sdk.md{#item-de5e8a}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,14 @@
 ---
 author: laujan
+ms.author: lajanuar
 manager: nitinme
+ms.date: 12/19/2023
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 12/19/2023
-ms.author: lajanuar
-ms.custom: devx-track-js, ignite-2024
+ms.custom:
+  - devx-track-js
+  - ignite-2024
+  - build-2025
 ---
 
 [Reference documentation](/javascript/api/overview/azure/ai-language-text-readme) | [More samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/cognitivelanguage/ai-language-text/samples/v1) | [Package (npm)](https://www.npmjs.com/package/@azure/ai-language-text) | [Library source code](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/cognitivelanguage/ai-language-text) 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Node.js SDKの要約ドキュメントの更新"
}
```

### Explanation
この変更では、Node.js SDKに関する要約ドキュメント`nodejs-sdk.md`が修正され、いくつかの重要なメタデータが追加されています。具体的には、著者情報としての`ms.author`が再び記載され、ドキュメントの日付も新しく追加されています。また、`ms.custom`セクションには`build-2025`という新しいエントリが追加され、既存の`devx-track-js`と`ignite-2024`と共に整理されています。これにより、ユーザーはドキュメントの関連情報をより簡単に把握でき、内容の整合性と可読性が向上しています。この更新は、利用者にとっての利便性を高めるための重要な改善と言えるでしょう。

## articles/ai-services/language-service/text-analytics-for-health/includes/quickstarts/python-sdk.md{#item-544ea5}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,12 @@
 ---
 author: laujan
+ms.author: lajanuar
+ms.date: 12/19/2023
 ms.service: azure-ai-language
+ms.topic: include
 ms.custom:
   - ignite-2024
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: lajanuar
+  - build-2025
 ---
 
 [Reference documentation](/python/api/azure-ai-textanalytics/azure.ai.textanalytics?preserve-view=true&view=azure-python) | [More samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics/samples) | [Package (PyPi)](https://pypi.org/project/azure-ai-textanalytics/5.2.0/) | [Library source code](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics) 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python SDKの要約ドキュメントの更新"
}
```

### Explanation
この変更では、Python SDKに関連する要約ドキュメント`python-sdk.md`が改訂され、いくつかの重要なメタデータが追加されています。具体的には、著者情報としての`ms.author`が再度記載され、ドキュメントの日付も新たに追加されています。また、`ms.custom`セクションには`build-2025`が追加され、既存の`ignite-2024`と共に整理されています。さらに、`ms.topic`フィールドも再配置され、一貫した情報提供が強化されています。この更新により、利用者はドキュメントから得られる情報をより効果的に活用できるようになり、内容の整合性と可読性が向上しています。これは、ユーザーにとっての利便性を向上させるための重要な改善と言えるでしょう。

## articles/ai-services/language-service/text-analytics-for-health/includes/quickstarts/rest-api.md{#item-ba4862}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,13 @@
 ---
 author: laujan
+ms.author: lajanuar
 manager: nitinme
+ms.date: 12/19/2023
 ms.service: azure-ai-language
+ms.topic: include
 ms.custom:
   - ignite-2024
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: lajanuar
+  - build-2025
 ---
 
 [Reference documentation](https://go.microsoft.com/fwlink/?linkid=2239169)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIに関する要約ドキュメントの更新"
}
```

### Explanation
このコードの変更では、REST APIに関する要約ドキュメント`rest-api.md`が改訂され、いくつかの重要なメタデータが追加されています。具体的には、著者情報を示す`ms.author`が追加され、ドキュメントの日付も新たに記載されています。また、`ms.custom`セクションに新たに`build-2025`が追加され、既存の`ignite-2024`と共に整理されています。さらに、`ms.topic`フィールドも新たに追加され、一貫性のある情報提供が強化されています。この更新により、ユーザーはドキュメントの内容をより効果的に活用できるようになり、情報の整合性と可読性が向上しています。この変更は、ユーザーの利便性を高めるための重要な改良といえるでしょう。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -6,35 +6,52 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: whats-new
-ms.date: 04/10/2025
+ms.date: 06/02/2025
 ms.author: lajanuar
 ---
 
 # What's new in Azure AI Language?
 
 Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent developments, this article provides you with information about new releases and features.
 
+## Build 2025 Releases (May 19 - 23)
+We released many new updates alongside the 2025 Microsoft Build Conference including:
+-    [Customizing PII detection using your own regex](personally-identifiable-information/how-to/adapt-to-domain-pii.md#customizing-pii-detection-using-your-own-regex-only-available-for-text-pii-container) (only available for Text PII container)
+-    Support for customizing PII output by [specifying values to exclude](personally-identifiable-information/how-to/adapt-to-domain-pii.md#customizing-pii-output-by-specifying-values-to-exclude)
+-    Customizing PII detection using [Entity Synonyms](personally-identifiable-information/how-to/adapt-to-domain-pii.md#api-schema-for-the-entitysynoyms-parameter)
+-    Model support for a new DateOfBirth entity subtype for PII detection.
+-    Updates to preview NER & PII API version: `2025-05-15-preview`. This API version includes DateOfBirth support, enhanced phone number AI quality, and umbrella entity type support for BankAccount, Passport, Drivers License
+
+More on these releases can be found on our TechCommunity Blog Post
+
 ## May 2025
 
 * Azure AI Language now supports the following agent templates:
-    *   [Intent routing](https://aka.ms/intent-triage-agent-template) detects user intent and provides exact answering. Perfect for deterministically intent routing and exact question answering with human controls.
-    *   [Exact question answering](https://aka.ms/exact-answer-agent-template) answers high-value predefined questions deterministically to ensure consistent and accurate responses.
+    *   [Intent routing](../agents/concepts/agent-catalog.md) detects user intent and provides exact answering. Perfect for deterministically intent routing and exact question answering with human controls.
+    *   [Exact question answering](../agents/concepts/agent-catalog.md) answers high-value predefined questions deterministically to ensure consistent and accurate responses.
+
+## April 2025
+
+* Updated and improved model GA release for NER
+* Expanded context window for [PII redaction](personally-identifiable-information/overview.md?tabs=text-pii) – This service update expands the window of detection the PII redaction service considers, enhancing quality and accuracy.
+* Added prediction capability for custom models, including conversational language Understanding (CLU), custom named entity recognition (NER), and custom text classification, are now available in three new regions: Jio India Central, UK West, and Canada East.
+* Scanned PDF PII - [Document input for PII redaction](personally-identifiable-information/how-to/redact-document-pii.md) now supports scanned PDFs, enabling PII detection and redaction in both digital and nondigital documents using `OCR`.
 
 ## March 2025
 
-* Azure AI Language resource now can be deployed to three new regions, Jio India Central, UK West, and Canada East, for the following capabilities: 
-    * Language detection 
-    * Sentiment analysis 
-    * Key phrase extraction 
-    * Named entity recognition (NER) 
-    * Personally identifiable information (PII) entity recognition 
-    * Entity linking 
-    * Text analytics for health 
-    * Extractive text summarization 
+* Azure AI Language resource now can be deployed to three new regions, Jio India Central, UK West, and Canada East, for the following capabilities:
+    * Language detection
+    * Sentiment analysis
+    * Key phrase extraction
+    * Named entity recognition (NER)
+    * Personally identifiable information (PII) entity recognition
+    * Entity linking
+    * Text analytics for health
+    * Extractive text summarization
 
-* Back-end infrastructure for the Named entity recognition (NER) and Text Personally identifiable information (PII) entity recognition models is now updated with extended context window limits. 
+* Back-end infrastructure for the Named entity recognition (NER) and Text Personally identifiable information (PII) entity recognition models is now updated with extended context window limits.
 
-* Our [Conversational PII redaction](personally-identifiable-information/how-to/redact-conversation-pii.md?tabs=client-libraries) service is now powered by an upgraded GA model. This updated version includes improved quality and accuracy in Credit card number entities and Numeric identification entities, such as Social Security numbers, Driver’s license numbers, Policy numbers, Medicare Beneficiary Identifiers, and Financial account numbers.
+* Our [Conversational PII redaction](personally-identifiable-information/how-to/redact-conversation-pii.md?tabs=client-libraries) service is now powered by an upgraded GA model. This revised version enhances the quality and accuracy of Credit Card Number entities and Numeric Identification entities. These entities include Social Security numbers, Driver's license numbers, Policy numbers, Medicare Beneficiary Identifiers, and Financial account numbers.
 
 ## February 2025
 
@@ -43,41 +60,41 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
 
 ## January 2025
 
-* .NET SDK for Azure AI Language text analytics, [Azure.AI.Language.Text 1.0.0-beta.2](https://www.nuget.org/packages/Azure.AI.Language.Text/1.0.0-beta.2#readme-body-tab), is now available. This client library supports the latest REST API version, 2024-11-01 and 2024-11-15-preview, for the following features:
+* .NET SDK for Azure AI Language text analytics, [Azure.AI.Language.Text 1.0.0-beta.2](https://www.nuget.org/packages/Azure.AI.Language.Text/1.0.0-beta.2#readme-body-tab), is now available. This client library supports the latest REST API version, `2024-11-01`, and `2024-11-15-preview`, for the following features:
     * Language detection
     * Sentiment analysis
     * Key phrase extraction
     * Named entity recognition (NER)
     * Personally identifiable information (PII) entity recognition
     * Entity linking
-    * Text analytics for health 
+    * Text analytics for health
     * Custom named entity recognition (Custom NER)
     * Custom text classification
     * Extractive text summarization
     * Abstractive text summarization
-* Custom sentiment analysis (preview), custom text analytics for health (preview) and custom summarization (preview) were retired on January 10, 2025, as Azure AI features are constantly evaluated based on customer demand and feedback. Based on the customers’ feedback of these preview features, Microsoft has decided to retire this feature and prioritize new custom model features leveraging the power of generative AI to better serve customers’ needs. 
+* Custom sentiment analysis (preview), custom text analytics for health (preview) and custom summarization (preview) were retired on January 10, 2025, as Azure AI features are constantly evaluated based on customer demand and feedback. Based on the customers' feedback of these preview features, Microsoft is retiring this feature and prioritize new custom model features using the power of generative AI to better serve customers' needs.
 
 ## November 2024
 
-* Azure AI Language is moving to [Azure AI Foundry](https://ai.azure.com). These skills are now available in AI Foundry playground: Extract health information, Extract PII from conversation, Extract PII from text, Summarize text, Summarize conversation, Summarize for call center. More skills follow.  
-* Runtime Container for Conversational Language Understanding (CLU) is available for on-premise connection.
-* Both our [Text PII redaction service](personally-identifiable-information/overview.md?tabs=text-pii) and our Conversational PII service preview API (version 2024-11-15-preview) now support the option to mask detected sensitive entities with a label beyond just redaction characters. Customers can specify if personal data content such as names and phone numbers, that is, "John Doe received a call from 424-878-9192", are masked with a redaction character, that is, "******** received a call from ************", or masked with an entity label, that is, "`PERSON_1` received a call from `PHONENUMBER_1`". More on how to specify the redaction policy style for your outputs can be found in our [how-to guides](personally-identifiable-information/how-to-call.md). 
+* Azure AI Language is moving to [Azure AI Foundry](https://ai.azure.com). These skills are now available in AI Foundry playground: Extract health information, Extract PII from conversation, Extract PII from text, Summarize text, Summarize conversation, Summarize for call center. More skills follow.
+* Runtime Container for Conversational Language Understanding (CLU) is available for on-premises connections.
+* Both our [Text PII redaction service](personally-identifiable-information/overview.md?tabs=text-pii) and our Conversational PII service preview API (version 2024-11-15-preview) now support the option to mask detected sensitive entities with a label beyond just redaction characters. Customers can specify if personal data content such as names and phone numbers, that is, "John Doe received a call from 424-878-9192" are masked with a redaction character, that is, "******** received a call from ************" or masked with an entity label, that is, "`PERSON_1` received a call from `PHONENUMBER_1`." More on how to specify the redaction policy style for your outputs can be found in our [how-to guides](personally-identifiable-information/how-to-call.md).
 * Native document support gating is removed with the latest API version, 2024-11-15-preview, allowing customers to access native document support for PII redaction and summarization. Key updates in this version include:
-    * Increased Maximum File Size Limits (from 1 MB to 10 MB). 
+    * Increased Maximum File Size Limits (from 1 MB to 10 MB).
     * Enhanced PII Redaction Customization: Customers can now specify whether they want only the redacted document or both the redacted document and a JSON file containing the detected entities.
-* Language detection is a preconfigured feature that can detect the language a document is written in and returns a language code for a wide range of languages, variants, dialects, and some regional/cultural languages. Today the general availability of [scription detection capability](language-detection/how-to/call-api.md#script-name-and-script-code), and 16 more languages support, which adds up to [139 total supported languages](language-detection/language-support.md) is announced.
-* [Named Entity Recognition service](named-entity-recognition/overview.md), [Entity Resolution](named-entity-recognition/concepts/entity-resolutions.md) was upgraded to the Entity Metadata starting in API version 2023-04-15-preview. If you're calling the preview version of the API equal or newer than 2023-04-15-preview, check out the Entity Metadata article to use the resolution feature. The service now supports the ability to specify a list of entity tags to be included into the response or excluded from the response. If a piece of text is classified as more than one entity type, the overlapPolicy parameter allows customers to specify how the service will handle the overlap. The inferenceOptions parameter allows for users to adjust the inference, such as excluding the detected entity values from being normalized and included in the metadata. Along with these optional input parameters  we support an updated output structure (with new fields tags, type, and metadata) to ensure enhanced user customization and deeper analysis Learn more on our documentation.
-* Text analytics for health (TA4H) is a preconfigured feature that extracts and labels relevant medical information from unstructured texts such as doctor's notes, discharge summaries, clinical documents, and electronic health records. Today, we released support for Fast Healthcare Interoperability Resources (FHIR) structuring and temporal [assertion detection](text-analytics-for-health/concepts/assertion-detection.md) in the Generally Available API.  
+* Language detection is a built-in feature designed to identify the language in which a document is written. It provides a language code that corresponds to a wide array of languages. This feature includes not only standard languages but also their variants, dialects, and certain regional or cultural languages. Today the general availability of [script detection capability](language-detection/how-to/call-api.md#script-name-and-script-code), and 16 more languages support, which adds up to [139 total supported languages](language-detection/language-support.md) is announced.
+* [Named Entity Recognition service](named-entity-recognition/overview.md), [Entity Resolution](named-entity-recognition/concepts/entity-resolutions.md) was upgraded to the Entity Metadata starting in API version 2023-04-15-preview. If you're calling the preview version of the API equal or newer than 2023-04-15-preview, check out the Entity Metadata article to use the resolution feature. The service now supports the ability to specify a list of entity tags to be included into the response or excluded from the response. If a piece of text is classified as more than one entity type, the overlapPolicy parameter allows customers to specify how the service handles the overlap. The `inferenceOptions` parameter enables users to modify the inference process, such as preventing detected entity values from being normalized and added to the metadata. Along with these optional input parameters, we support an updated output structure (with new fields tags, type, and metadata) to ensure enhanced user customization and deeper analysis Learn more on our documentation.
+* Text Analytics for Health (TA4H) is a specialized tool designed to extract and categorize key medical details from unstructured sources. These sources include doctor's notes, discharge summaries, clinical documentation, and electronic health records. Today, we released support for Fast Healthcare Interoperability Resources (FHIR) structuring and temporal [assertion detection](text-analytics-for-health/concepts/assertion-detection.md) in the Generally Available API.
 
 ## October 2024
 
-* Custom language service features enable you to deploy your project to multiple [resources within a single region](concepts/custom-features/multi-region-deployment.md) via the API, so that you can use your custom model wherever you need.
+* Custom language service features enable you to deploy your project to multiple [resources within a single region](concepts/custom-features/multi-region-deployment.md) via the API.
 
 ## September 2024
 
 * PII detection now has container support. See more details in the Azure Update post: [Announcing Text PII Redaction Container Release](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-text-pii-redaction-container-release/4264655).
-* Custom sentiment analysis (preview) will be retired January 10, 2025. You can transition to other custom model training services, such as custom text classification in Azure AI Language, by that date.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom sentiment analysis (preview) in Azure AI Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-sentiment-analysis-retirement).
-* Custom text analytics for health (preview) will be retired on January 10, 2025. Please transition to other custom model training services, such as custom named entity recognition in Azure AI Language, by that date.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom text analytics for health (preview) in Azure AI Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-text-analytics-for-health-retirement).
+* Custom sentiment analysis (preview) will be retired January 10, 2025. You can transition to other custom model training services, such as custom text classification in Azure AI Language.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom sentiment analysis (preview) in Azure AI Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-sentiment-analysis-retirement).
+* Custom text analytics for health (preview) will be retired on January 10, 2025. Transition to other custom model training services, such as custom named entity recognition in Azure AI Language, by that date.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom text analytics for health (preview) in Azure AI Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-text-analytics-for-health-retirement).
 
 ## August 2024
 * [CLU utterance limit in a project](conversational-language-understanding/service-limits.md#data-limits) increased from 25,000 to 50,000.
@@ -86,25 +103,25 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
 ## July 2024
 
 * [Conversational PII redaction](https://techcommunity.microsoft.com/blog/ai-azure-ai-services-blog/announcing-conversational-pii-detection-service-s-general/4162881) service in English-language contexts is now Generally Available (GA).
-* Conversation Summarization now supports 12 additional languages in preview as listed [here](summarization/language-support.md).
-* Summarization Meeting or Conversation Chapter titles features will now support reduced length to focus on the key topics.
-* Enable support for data augmentation for diacritics to generate variations of training data for diacritic variations used in some natural languages which is especially useful for Germanic and Slavic languages.
+* Conversation Summarization now supports 12 added languages in preview as listed [here](summarization/language-support.md).
+* Summarization Meeting or Conversation Chapter titles features support reduced length to focus on the key topics.
+* Enable support for data augmentation for diacritics to generate variations of training data for diacritic variations used in some natural languages which are especially useful for Germanic and Slavic languages.
 
 ## February 2024
 
-* Expanded [language detection](./language-detection/how-to/call-api.md#script-name-and-script-code) support for additional scripts according to the [ISO 15924 standard](https://wikipedia.org/wiki/ISO_15924) is now available starting in API version `2023-11-15-preview`.
+* Expanded [language detection](./language-detection/how-to/call-api.md#script-name-and-script-code) support for added scripts according to the [ISO 15924 standard](https://wikipedia.org/wiki/ISO_15924) is now available starting in API version `2023-11-15-preview`.
 
 ## January 2024
 
 * [Native document support](native-document-support/overview.md) is now available in `2023-11-15-preview` public preview.
 
 ## December 2023
 
-* [Text Analytics for health](./text-analytics-for-health/overview.md) new model 2023-12-01 is now available.
+* [Text Analytics for health](./text-analytics-for-health/overview.md) new model `2023-12-01` is now available.
 * New Relation Type: `BodySiteOfExamination`
  * Quality enhancements to support radiology documents
  * Significant latency improvements
- * Various bug fixes: Improvements across NER, Entity Linking, Relations and Assertion Detection
+ * Various bug fixes: Improvements across NER, Entity Linking, Relations, and Assertion Detection
 
 ## November 2023
 
@@ -116,12 +133,12 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
 
 ## May 2023
 
-* [Custom Named Entity Recognition (NER) Docker containers](./custom-named-entity-recognition/how-to/use-containers.md) are now available for on-premises deployment. 
+* [Custom Named Entity Recognition (NER) Docker containers](./custom-named-entity-recognition/how-to/use-containers.md) are now available for on-premises deployment.
 
 ## April 2023
 
 * [Custom Text analytics for health](./custom-text-analytics-for-health/overview.md) is available in public preview, which enables you to build custom AI models to extract healthcare specific entities from unstructured text
-* You can now use Azure OpenAI to automatically label or generate data during authoring. Learn more with the following links: 
+* You can now use Azure OpenAI to automatically label or generate data during authoring. Learn more with the following links:
     * Autolabel your documents in [Custom text classification](./custom-text-classification/how-to/use-autolabeling.md) or [Custom named entity recognition](./custom-named-entity-recognition/how-to/use-autolabeling.md).
     * Generate suggested utterances in [Conversational language understanding](./conversational-language-understanding/how-to/tag-utterances.md#suggest-utterances-with-azure-openai).
 * The latest model version (`2022-10-01`) for Language Detection now supports 6 more International languages and 12 Romanized Indic languages.
@@ -133,45 +150,45 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
 * New versions of the text analysis client library are available in preview:
 
     ### [C#](#tab/csharp)
-    
+
     [**Package (NuGet)**](https://www.nuget.org/packages/Azure.AI.TextAnalytics/5.3.0-beta.2)
-    
+
     [**Changelog/Release History**](https://github.com/Azure/azure-sdk-for-net/blob/Azure.AI.TextAnalytics_5.3.0-beta.2/sdk/textanalytics/Azure.AI.TextAnalytics/CHANGELOG.md)
-    
+
     [**ReadMe**](https://github.com/Azure/azure-sdk-for-net/blob/Azure.AI.TextAnalytics_5.3.0-beta.2/sdk/textanalytics/Azure.AI.TextAnalytics/README.md)
-    
+
     [**Samples**](https://github.com/Azure/azure-sdk-for-net/blob/Azure.AI.TextAnalytics_5.3.0-beta.2/sdk/textanalytics/Azure.AI.TextAnalytics/samples/README.md)
-  
+
     ### [Java](#tab/java)
-    
+
     [**Package (Maven)**](https://mvnrepository.com/artifact/com.azure/azure-ai-textanalytics/5.3.0-beta.2)
-    
+
     [**Changelog/Release History**](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/textanalytics/azure-ai-textanalytics/CHANGELOG.md#530-beta2-2023-03-07)
-    
+
     [**ReadMe**](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/textanalytics/azure-ai-textanalytics/README.md)
-    
+
     [**Samples**](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics/src/samples)
-    
+
     ### [JavaScript](#tab/javascript)
 
     [**Package (npm)**](https://www.npmjs.com/package/@azure/ai-language-text/v/1.1.0-beta.2)
-    
+
     [**Changelog/Release History**](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/cognitivelanguage/ai-language-text/CHANGELOG.md)
-    
+
     [**ReadMe**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/cognitivelanguage/ai-language-text)
-    
+
     [**Samples**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/cognitivelanguage/ai-language-text/samples/v1-beta)
 
     ### [Python](#tab/python)
-    
+
     [**Package (PyPi)**](https://pypi.org/project/azure-ai-textanalytics/5.3.0b2/)
-    
+
     [**Changelog/Release History**](https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-textanalytics_5.3.0b2/sdk/textanalytics/azure-ai-textanalytics/CHANGELOG.md)
-    
+
     [**ReadMe**](https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-textanalytics_5.3.0b2/sdk/textanalytics/azure-ai-textanalytics/README.md)
-    
+
     [**Samples**](https://github.com/Azure/azure-sdk-for-python/tree/azure-ai-textanalytics_5.3.0b2/sdk/textanalytics/azure-ai-textanalytics/samples)
-    
+
     ---
 
 ## February 2023
@@ -204,7 +221,7 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
         * [**Changelog/Release History**](https://github.com/Azure/azure-sdk-for-java/blob/azure-ai-textanalytics_5.3.0-beta.1/sdk/textanalytics/azure-ai-textanalytics/CHANGELOG.md)
         * [**ReadMe**](https://github.com/Azure/azure-sdk-for-java/blob/azure-ai-textanalytics_5.3.0-beta.1/sdk/textanalytics/azure-ai-textanalytics/README.md)
         * [**Samples**](https://github.com/Azure/azure-sdk-for-java/tree/azure-ai-textanalytics_5.3.0-beta.1/sdk/textanalytics/azure-ai-textanalytics/src/samples)
-    
+
     * JavaScript
         * [**Package (npm)**](https://www.npmjs.com/package/@azure/ai-language-text/v/1.1.0-beta.1)
         * [**Changelog/Release History**](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/cognitivelanguage/ai-language-text/CHANGELOG.md)
@@ -230,27 +247,27 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
     * [Key phrase extraction](./key-phrase-extraction/language-support.md)
     * [Named entity recognition](./named-entity-recognition/language-support.md)
     * [Text Analytics for health](./text-analytics-for-health/language-support.md)
-* [Multi-region deployment](./concepts/custom-features/multi-region-deployment.md) and [project asset versioning](./concepts/custom-features/project-versioning.md) for: 
+* [Multi-region deployment](./concepts/custom-features/multi-region-deployment.md) and [project asset versioning](./concepts/custom-features/project-versioning.md) for:
     * [Conversational language understanding](./conversational-language-understanding/overview.md)
     * [Orchestration workflow](./orchestration-workflow/overview.md)
-    * [Custom text classification](./custom-text-classification/overview.md) 
+    * [Custom text classification](./custom-text-classification/overview.md)
     * [Custom named entity recognition](./custom-named-entity-recognition/overview.md)
 * [Regular expressions](./conversational-language-understanding/concepts/entity-components.md#regex-component) in conversational language understanding and [required components](./conversational-language-understanding/concepts/entity-components.md#required-components), offering an added ability to influence entity predictions.
 * [Entity resolution](./named-entity-recognition/concepts/entity-resolutions.md) in named entity recognition
 * New region support for:
     * [Conversational language understanding](./conversational-language-understanding/service-limits.md#regional-availability)
     * [Orchestration workflow](./orchestration-workflow/service-limits.md#regional-availability)
-    * [Custom text classification](./custom-text-classification/service-limits.md#regional-availability) 
-    * [Custom named entity recognition](./custom-named-entity-recognition/service-limits.md#regional-availability) 
-* Document type as an input supported for [Text Analytics for health](./text-analytics-for-health/how-to/call-api.md) FHIR requests 
+    * [Custom text classification](./custom-text-classification/service-limits.md#regional-availability)
+    * [Custom named entity recognition](./custom-named-entity-recognition/service-limits.md#regional-availability)
+* Document type as an input supported for [Text Analytics for health](./text-analytics-for-health/how-to/call-api.md) FHIR requests
 
 ## September 2022
 
 * [Conversational language understanding](./conversational-language-understanding/overview.md) is available in the following regions:
   * Central India
   * Switzerland North
   * West US 2
-* Text Analytics for Health now [supports more languages](./text-analytics-for-health/language-support.md) in preview: Spanish, French, German Italian, Portuguese and Hebrew. These languages are available when using a docker container to deploy the API service. 
+* Text Analytics for Health now [supports more languages](./text-analytics-for-health/language-support.md) in preview: Spanish, French, German Italian, Portuguese and Hebrew. These languages are available when using a docker container to deploy the API service.
 * The Azure.AI.TextAnalytics client library v5.2.0 are generally available and ready for use in production applications. For more information on Language service client libraries, see the [**Developer overview**](./concepts/developer-guide.md).
     * Java
         * [**Package (Maven)**](https://mvnrepository.com/artifact/com.azure/azure-ai-textanalytics/5.2.0)
@@ -275,8 +292,8 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
 ## July 2022
 
 * New AI models for [sentiment analysis](./sentiment-opinion-mining/overview.md) and [key phrase extraction](./key-phrase-extraction/overview.md) based on [z-code models](https://www.microsoft.com/research/project/project-zcode/), providing:
-    * Performance and quality improvements for the following 11 [languages](./sentiment-opinion-mining/language-support.md) supported by sentiment analysis: `ar`, `da`, `el`, `fi`, `hi`, `nl`, `no`, `pl`,  `ru`, `sv`, `tr` 
-    * Performance and quality improvements for the following 20 [languages](./key-phrase-extraction/language-support.md) supported by key phrase extraction: `af`, `bg`, `ca`, `hr`, `da`, `nl`, `et`, `fi`, `el`, `hu`, `id`, `lv`, `no`, `pl`, `ro`, `ru`, `sk`, `sl`, `sv`, `tr` 
+    * Performance and quality improvements for the following 11 [languages](./sentiment-opinion-mining/language-support.md) supported by sentiment analysis: `ar`, `da`, `el`, `fi`, `hi`, `nl`, `no`, `pl`,  `ru`, `sv`, `tr`
+    * Performance and quality improvements for the following 20 [languages](./key-phrase-extraction/language-support.md) supported by key phrase extraction: `af`, `bg`, `ca`, `hr`, `da`, `nl`, `et`, `fi`, `el`, `hu`, `id`, `lv`, `no`, `pl`, `ro`, `ru`, `sk`, `sl`, `sv`, `tr`
 
 * Conversational PII is now available in all Azure regions supported by the Language service.
 
@@ -289,7 +306,7 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
     ```http
     <your-language-resource-endpoint>/language/:analyze-text?api-version=2022-07-01-preview
     ```
-    
+
 ## June 2022
 * v1.0 client libraries for [conversational language understanding](./conversational-language-understanding/how-to/call-api.md?tabs=azure-sdk#send-a-conversational-language-understanding-request) and [orchestration workflow](./orchestration-workflow/how-to/call-api.md?tabs=azure-sdk#send-an-orchestration-workflow-request) are Generally Available for the following languages:
     * [C#](https://github.com/Azure/azure-sdk-for-net/tree/Azure.AI.Language.Conversations_1.0.0/sdk/cognitivelanguage/Azure.AI.Language.Conversations)
@@ -388,4 +405,4 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
 
 ## Next steps
 
-* See the [previous updates](./concepts/previous-updates.md) article for service updates not listed here. 
+* See the [previous updates](./concepts/previous-updates.md) article for service updates not listed here.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Languageの新機能および更新内容の追加"
}
```

### Explanation
この変更は、Azure AI Languageの新機能と更新内容をまとめたドキュメント`whats-new.md`に関する重要な改訂です。変更には、様々な新機能やリリース情報の追加が含まれており、特に2025年5月のMicrosoft Build Conferenceにおける新機能の発表が目を引きます。具体的には、PII検出のカスタマイズ機能や、年齢・電話番号の品質向上、新たに導入された日付関連のエンティティなどの情報が盛り込まれています。

さらに、2025年4月と3月の更新も詳細に記載され、機能の拡張や地域ごとの対応状況が明確にされています。たとえば、今後利用できる地域の追加や、PDF文書のPII検出機能の強化が紹介されています。また、使用されるAPIのバージョン変更や新しい機能のサポートについての情報が提供されており、Azure AI Languageの利用者は最新の機能に関する知識を得ることができます。

このようなアップデートは、ユーザーがAzure AI Languageサービスをより効果的に利用できるようにするために重要です。変更が多岐にわたるため、文書全体の可読性と情報の整合性が向上しています。


